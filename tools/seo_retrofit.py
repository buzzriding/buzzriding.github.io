#!/usr/bin/env python3
"""
Idempotent on-page SEO retrofit for buzzriding.github.io.

Adds, only where missing:
  - <link rel="canonical">
  - og:image / og:image:alt / og:site_name / og:description
  - twitter:card (summary_large_image) + twitter:title/description/image
  - Article JSON-LD (with author, publisher, mainEntityOfPage, image)
  - FAQPage JSON-LD built from the .faq-item markup already on the page
  - the inline Beehiiv subscribe form in the newsletter strip

Safe to run repeatedly: every insertion is guarded by a presence check.
Run:  python3 tools/seo_retrofit.py [--check]
"""

import glob
import html
import json
import os
import re
import sys

SITE = "https://buzzriding.github.io"
OG_IMAGE = f"{SITE}/assets/og-card.png"
OG_ALT = "BuzzRiding — where curious marketers come to stay one step ahead"
BEEHIIV_FORM = "https://subscribe-forms.beehiiv.com/94bede40-6aee-45ce-8ddc-36b0f283b97d"

FORM_EMBED = (
    '<div style="width:100%;max-width:520px;">'
    f'<iframe src="{BEEHIIV_FORM}" data-test-id="beehiiv-embed" frameborder="0" '
    'scrolling="no" title="Subscribe to The Buzz" style="width:100%;height:207px;'
    "margin:0;border-radius:0px;background-color:transparent;box-shadow:0 0 #0000;"
    'max-width:100%;"></iframe></div>'
)

NL_STRIP = (
    '<div class="nl-strip" style="flex-direction:column;align-items:flex-start;">'
    '<div style="margin-bottom:16px;"><h3>Get The Buzz every Tuesday \U0001F4EC</h3>'
    "<p>One newsletter. The best AI marketing insights of the week. Free, always.</p></div>"
    '<div style="width:100%;max-width:520px;">'
    f'<iframe src="{BEEHIIV_FORM}" data-test-id="beehiiv-embed" frameborder="0" '
    'scrolling="no" style="width:100%;height:207px;margin:0;border-radius:0px;'
    'background-color:transparent;box-shadow:0 0 #0000;max-width:100%;"></iframe>'
    "</div></div>"
)

TAGS = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def text_of(fragment: str) -> str:
    return WS.sub(" ", html.unescape(TAGS.sub(" ", fragment))).strip()


def meta(doc: str, prop: str, attr: str = "property") -> str | None:
    m = re.search(
        rf'<meta\s+{attr}=["\']{re.escape(prop)}["\']\s+content=["\'](.*?)["\']\s*/?>',
        doc,
        re.S,
    )
    return html.unescape(m.group(1)).strip() if m else None


def title_of(doc: str) -> str:
    m = re.search(r"<title>(.*?)</title>", doc, re.S)
    return html.unescape(m.group(1)).strip() if m else "BuzzRiding"


def headline_of(doc: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", doc, re.S)
    return text_of(m.group(1)) if m else title_of(doc).split(" — ")[0]


def ld_blocks(doc: str):
    for m in re.finditer(
        r'<script type="application/ld\+json">(.*?)</script>', doc, re.S
    ):
        try:
            yield m, json.loads(m.group(1))
        except json.JSONDecodeError:
            continue


def published_date(doc: str) -> str | None:
    for _, data in ld_blocks(doc):
        if isinstance(data, dict) and data.get("datePublished"):
            return data["datePublished"]
    return None


def faq_pairs(doc: str):
    pairs = []
    for m in re.finditer(
        r'<div class="faq-item"[^>]*>\s*<div class="faq-q"[^>]*>(.*?)</div>\s*'
        r'<div class="faq-a"[^>]*>(.*?)</div>\s*</div>',
        doc,
        re.S,
    ):
        q, a = text_of(m.group(1)), text_of(m.group(2))
        if q and a and not q.lower().startswith("replace with"):
            pairs.append((q, a))
    return pairs


def insert_after(doc: str, anchor_re: str, block: str) -> str:
    m = re.search(anchor_re, doc)
    if not m:
        return doc.replace("</head>", block + "\n</head>", 1)
    end = m.end()
    return doc[:end] + "\n" + block + doc[end:]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def retrofit(path: str, doc: str) -> tuple[str, list[str]]:
    changed = []
    slug = os.path.basename(path)
    url = f"{SITE}/blog/{slug}" if "/blog/" in path.replace(os.sep, "/") else f"{SITE}/{slug}"
    if slug == "index.html":
        url = f"{SITE}/"

    title = title_of(doc)
    desc = meta(doc, "description", attr="name") or ""

    # 1. canonical
    if 'rel="canonical"' not in doc:
        doc = insert_after(
            doc, r"<title>.*?</title>", f'  <link rel="canonical" href="{url}" />'
        )
        changed.append("canonical")

    # 2. Open Graph gaps
    og_add = []
    if not meta(doc, "og:image"):
        og_add += [
            f'  <meta property="og:image" content="{OG_IMAGE}" />',
            '  <meta property="og:image:width" content="1200" />',
            '  <meta property="og:image:height" content="630" />',
            f'  <meta property="og:image:alt" content="{esc(OG_ALT)}" />',
        ]
    if not meta(doc, "og:site_name"):
        og_add.append('  <meta property="og:site_name" content="BuzzRiding" />')
    if not meta(doc, "og:title"):
        og_add.append(f'  <meta property="og:title" content="{esc(title)}" />')
    if not meta(doc, "og:description") and desc:
        og_add.append(f'  <meta property="og:description" content="{esc(desc)}" />')
    if not meta(doc, "og:url"):
        og_add.append(f'  <meta property="og:url" content="{url}" />')
    if og_add:
        doc = insert_after(doc, r'<link rel="canonical"[^>]*>', "\n".join(og_add))
        changed.append("og")

    # 3. Twitter card
    if not meta(doc, "twitter:card", attr="name"):
        tw = [
            '  <meta name="twitter:card" content="summary_large_image" />',
            f'  <meta name="twitter:title" content="{esc(title)}" />',
            f'  <meta name="twitter:image" content="{OG_IMAGE}" />',
        ]
        if desc:
            tw.insert(2, f'  <meta name="twitter:description" content="{esc(desc)}" />')
        doc = insert_after(doc, r'<meta property="og:[^>]*>(?![\s\S]*<meta property="og:)', "\n".join(tw))
        changed.append("twitter")

    if "/blog/" not in path.replace(os.sep, "/"):
        return doc, changed

    # 4. Article JSON-LD — create if absent, enrich if thin
    article = None
    for m, data in ld_blocks(doc):
        if isinstance(data, dict) and data.get("@type") == "Article":
            article = (m, data)
            break

    if article is None:
        node = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline_of(doc),
            "description": desc,
            "url": url,
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "image": OG_IMAGE,
            "author": {"@type": "Organization", "name": "BuzzRiding", "url": SITE},
            "publisher": {"@type": "Organization", "name": "BuzzRiding", "url": SITE},
        }
        doc = doc.replace(
            "</head>",
            '  <script type="application/ld+json">'
            + json.dumps(node, ensure_ascii=False)
            + "</script>\n</head>",
            1,
        )
        changed.append("article-ld")
    else:
        m, data = article
        before = json.dumps(data, sort_keys=True)
        data.setdefault("url", url)
        data.setdefault("mainEntityOfPage", {"@type": "WebPage", "@id": url})
        data.setdefault("image", OG_IMAGE)
        data.setdefault(
            "author", {"@type": "Organization", "name": "BuzzRiding", "url": SITE}
        )
        if desc:
            data.setdefault("description", desc)
        pub = data.get("datePublished")
        if pub:
            data.setdefault("dateModified", pub)
        if json.dumps(data, sort_keys=True) != before:
            doc = (
                doc[: m.start()]
                + '<script type="application/ld+json">'
                + json.dumps(data, ensure_ascii=False)
                + "</script>"
                + doc[m.end() :]
            )
            changed.append("article-ld+")

    # 5. FAQPage JSON-LD from the FAQs already on the page
    if "FAQPage" not in doc:
        pairs = faq_pairs(doc)
        if len(pairs) >= 2:
            node = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a},
                    }
                    for q, a in pairs
                ],
            }
            doc = doc.replace(
                "</head>",
                '  <script type="application/ld+json">'
                + json.dumps(node, ensure_ascii=False)
                + "</script>\n</head>",
                1,
            )
            changed.append(f"faq-ld({len(pairs)})")

    # 6. Inline subscribe form — swap the link-out button for the embedded form.
    #    Two layouts exist in the wild: .nl-strip and .newsletter-strip. Both end
    #    in an <a href="/newsletter.html" class="btn-primary">, so replace that.
    if BEEHIIV_FORM not in doc:
        doc, n = re.subn(
            r'<a href="/newsletter\.html" class="btn-primary">.*?</a>',
            FORM_EMBED,
            doc,
            flags=re.S,
        )
        if n:
            changed.append(f"inline-form(x{n})")

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
        if "post-template" in path:
            continue
        updated, changed = retrofit(path, original)
        if changed and updated != original:
            touched += 1
            print(f"{os.path.relpath(path, root):70} {', '.join(changed)}")
            if not check:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(updated)
    print(f"\n{touched} file(s) {'would be' if check else ''} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
