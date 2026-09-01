#!/usr/bin/env python3
"""
Keep the affiliate disclosure truthful, and strip unfilled placeholders.

As of 2026-09-01 the site carried an affiliate disclosure on all 64 posts and
had zero outbound links of any kind — so it disclosed commissions it could not
earn, while seven pages showed a raw [AFFILIATE_LINK_PLACEHOLDER] to readers.

This script makes the disclosure follow reality on every run:
  - a page with NO external outbound links gets the no-commission wording
  - a page that HAS external links gets the affiliate wording back
  - the raw placeholder token is removed wherever it still appears

So the moment real affiliate links are added, the correct disclosure returns by
itself. Run: python3 tools/fix_disclosures.py [--check]
"""

import glob
import os
import re
import sys

AFFILIATE_FOOT = (
    "This site contains affiliate links. We may earn a commission if you sign up "
    "for a tool — at no extra cost to you. Posts are researched and refined with AI tools."
)
HONEST_FOOT = (
    "BuzzRiding has no affiliate relationships and earns no commission on the tools "
    "covered here. Posts are researched and refined with AI tools."
)
AFFILIATE_POST = (
    "This post was researched and refined with AI tools. Some links are affiliate "
    "links — we may earn a commission if you sign up, at no extra cost to you."
)
HONEST_POST = (
    "This post was researched and refined with AI tools. BuzzRiding earns no "
    "commission on any tool mentioned."
)

# Any disclosure sentence we have ever shipped, so the swap is reversible.
FOOT_VARIANTS = [AFFILIATE_FOOT, HONEST_FOOT]
POST_VARIANTS = [
    AFFILIATE_POST,
    HONEST_POST,
    "This post was researched and refined with AI tools. Some links may be affiliate "
    "links — we may earn a commission if you sign up, at no extra cost to you.",
    "This post was researched and refined with AI tools. Some links may be affiliate links.",
]

PLACEHOLDER = "[AFFILIATE_LINK_PLACEHOLDER]"


def has_external_links(doc: str) -> bool:
    body = doc[doc.find("</style>"):]
    for m in re.finditer(r'href="(https?://[^"]+)"', body):
        host = m.group(1).split("/")[2]
        if "buzzriding" in host:
            continue
        if host.endswith(("googletagmanager.com", "googleapis.com", "gstatic.com",
                          "beehiiv.com", "twitter.com", "linkedin.com")):
            continue
        return True
    return False


def strip_placeholder(doc: str) -> tuple[str, int]:
    n = doc.count(PLACEHOLDER)
    if not n:
        return doc, 0
    # A paragraph that is nothing but the placeholder goes entirely.
    doc = re.sub(r"\s*<p>\s*" + re.escape(PLACEHOLDER) + r"\s*</p>", "", doc)
    # Otherwise drop the token and any dangling separator around it.
    doc = doc.replace(" " + PLACEHOLDER, "").replace(PLACEHOLDER + " ", "")
    doc = doc.replace(PLACEHOLDER + " — ", "").replace(PLACEHOLDER, "")
    doc = re.sub(r"<p>\s*—\s*", "<p>", doc)
    doc = re.sub(r"\s{2,}", " ", doc)
    return doc, n


def apply(doc: str) -> tuple[str, list[str]]:
    changed = []
    doc, n = strip_placeholder(doc)
    if n:
        changed.append(f"placeholder(x{n})")

    affiliate = has_external_links(doc)
    foot_target = AFFILIATE_FOOT if affiliate else HONEST_FOOT
    post_target = AFFILIATE_POST if affiliate else HONEST_POST

    for variant in FOOT_VARIANTS:
        if variant != foot_target and variant in doc:
            doc = doc.replace(variant, foot_target)
            changed.append("footer-disclosure")
    for variant in POST_VARIANTS:
        if variant != post_target and variant in doc:
            doc = doc.replace(variant, post_target)
            changed.append("post-disclosure")
    return doc, changed


def main() -> int:
    check = "--check" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    targets = sorted(glob.glob(os.path.join(root, "blog", "*.html"))) + [
        os.path.join(root, f)
        for f in ("index.html", "blog.html", "about.html", "start-here.html", "newsletter.html")
        if os.path.exists(os.path.join(root, f))
    ]
    touched = 0
    for path in targets:
        with open(path, encoding="utf-8") as fh:
            original = fh.read()
        updated, changed = apply(original)
        if changed and updated != original:
            touched += 1
            print(f"{os.path.relpath(path, root):70} {', '.join(sorted(set(changed)))}")
            if not check:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(updated)
    print(f"\n{touched} file(s) {'would be' if check else ''} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
