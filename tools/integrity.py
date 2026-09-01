#!/usr/bin/env python3
"""
Content integrity pass.

Three jobs, all driven by tools/integrity.json so the decisions live in data,
not in code:

  1. RETIRE — remove posts whose central claim could not have happened, take
     their cards out of blog.html, and turn any internal link pointing at them
     back into plain text so nothing 404s.
  2. NOTE — put a visible editorial note at the top of every post that makes a
     first-person testing claim without evidence behind it.
  3. CHECK — report every post that still claims first-hand testing while
     carrying no evidence (no image, no outbound citation). This is the guard
     that stops the problem recurring; it prints, it does not fail the build.

Run: python3 tools/integrity.py [--check]
"""

import glob
import json
import os
import re
import sys

CLAIM = re.compile(
    r"\b(we tested|we ran|we tried|we used|our test|our experiment|we spent|"
    r"we compared|we measured|in our test|our results|i tested|i ran|i let ai|"
    r"i a/b tested|i spent|i tracked)\b",
    re.I,
)

NOTE_CSS = (
    "background:rgba(223,164,92,0.08);border:1px solid rgba(223,164,92,0.35);"
    "border-radius:10px;padding:18px 22px;margin:0 0 28px;font-size:14.5px;line-height:1.65;"
)
NOTE_MARK = "data-editorial-note"


def note_html(text: str) -> str:
    return (
        f'<div {NOTE_MARK} style="{NOTE_CSS}">'
        '<strong style="display:block;margin-bottom:6px;">Editorial note — September 2026</strong>'
        f"{text}</div>"
    )


def body_text(doc: str) -> str:
    m = re.search(r'<article[^>]*class="article-body"[^>]*>(.*?)</article>', doc, re.S)
    seg = m.group(1) if m else doc[doc.find("</style>"):]
    seg = re.sub(r"<script.*?</script>", "", seg, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", seg))


def has_evidence(doc: str) -> bool:
    body = doc[doc.find("</style>"):]
    if re.search(r"<img\b", body):
        return True
    for m in re.finditer(r'href="(https?://[^"]+)"', body):
        host = m.group(1).split("/")[2]
        if "buzzriding" in host:
            continue
        if host.endswith(("googletagmanager.com", "googleapis.com", "gstatic.com",
                          "beehiiv.com", "twitter.com", "linkedin.com")):
            continue
        return True
    return False


def load_config(root: str) -> dict:
    with open(os.path.join(root, "tools", "integrity.json"), encoding="utf-8") as fh:
        return json.load(fh)


def unlink_retired(doc: str, slugs: set[str]) -> tuple[str, int]:
    """Turn <a href="/blog/<retired>.html">text</a> into plain text."""
    n = 0
    for slug in slugs:
        # related-post / listing cards wrap several elements: drop the whole card
        doc, k = re.subn(
            rf'<a href="/blog/{re.escape(slug)}\.html"[^>]*class="[^"]*(?:related-card|post-card)[^"]*"[^>]*>.*?</a>',
            "", doc, flags=re.S,
        )
        n += k
        # inline links become their own anchor text
        doc, k = re.subn(
            rf'<a href="/blog/{re.escape(slug)}\.html"[^>]*>(.*?)</a>',
            lambda m: m.group(1), doc, flags=re.S,
        )
        n += k
    return doc, n


def strip_card(doc: str, slug: str) -> tuple[str, int]:
    """Remove a blog.html listing card for a retired post."""
    return re.subn(
        rf'<a href="/blog/{re.escape(slug)}\.html"[^>]*class="post-card"[^>]*>.*?</a>',
        "", doc, flags=re.S,
    )


def main() -> int:
    check = "--check" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cfg = load_config(root)
    retired = {r["slug"]: r["reason"] for r in cfg.get("retire", [])}
    note_text = cfg["note_text"]
    noted = set(cfg.get("note", []))

    actions = []

    # 1. retire
    for slug in retired:
        path = os.path.join(root, "blog", f"{slug}.html")
        if os.path.exists(path):
            actions.append(f"RETIRE  blog/{slug}.html")
            if not check:
                os.remove(path)

    # 2 + 3. notes, link cleanup, evidence report
    unevidenced = []
    pages = sorted(glob.glob(os.path.join(root, "blog", "*.html"))) + [
        os.path.join(root, f) for f in ("index.html", "blog.html", "start-here.html")
        if os.path.exists(os.path.join(root, f))
    ]
    for path in pages:
        with open(path, encoding="utf-8") as fh:
            doc = original = fh.read()
        name = os.path.relpath(path, root)
        slug = os.path.basename(path)[:-5]

        doc, n = unlink_retired(doc, set(retired))
        if n:
            actions.append(f"UNLINK  {name} ({n} link(s) to retired posts)")
        if os.path.basename(path) == "blog.html":
            for s in retired:
                doc, k = strip_card(doc, s)
                if k:
                    actions.append(f"CARD    removed {s} from blog.html")

        if slug in noted and NOTE_MARK not in doc:
            m = re.search(r'(<article[^>]*class="article-body"[^>]*>\s*<div class="article-container">)', doc)
            if m:
                doc = doc[: m.end()] + note_html(note_text) + doc[m.end():]
                actions.append(f"NOTE    {name}")

        if "/blog/" in path.replace(os.sep, "/") and slug not in retired:
            if CLAIM.search(body_text(doc)) and not has_evidence(doc):
                unevidenced.append(slug)

        if doc != original and not check:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(doc)

    for a in actions:
        print(a)
    print(f"\n{len(actions)} action(s) {'would be ' if check else ''}applied.")
    print(f"\nEVIDENCE CHECK: {len(unevidenced)} live post(s) claim first-hand testing "
          f"with no image and no outbound citation.")
    for s in sorted(unevidenced):
        print(f"  - {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
