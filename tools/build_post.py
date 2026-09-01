#!/usr/bin/env python3
"""
Build a new post by cloning a live post's shell and swapping the content.

Guarantees the new article matches the site template exactly — same nav, CSS,
footer, subscribe strip — without anyone hand-copying 20KB of markup, which is
how `href="#"` placeholders and drifting layouts got into the archive.

Content lives in content/<slug>.json. CI runs `--all`, which builds any post
whose HTML is missing or older than its spec, and inserts its card into
blog.html. Writing a post therefore means writing one JSON file, never 20KB of
markup.

Usage: python3 tools/build_post.py content/<slug>.json
       python3 tools/build_post.py --all
"""

import glob
import json
import os
import re
import sys


def swap(doc: str, pattern: str, replacement: str, label: str) -> str:
    new, n = re.subn(pattern, lambda _m: replacement, doc, count=1, flags=re.S)
    if not n:
        raise SystemExit(f"build_post: could not find {label} in the shell post")
    return new


def add_card(root: str, spec: dict) -> bool:
    """Insert the listing card into blog.html, before the first existing card."""
    path = os.path.join(root, "blog.html")
    doc = open(path, encoding="utf-8").read()
    if f'/blog/{spec["slug"]}.html' in doc:
        return False
    card = (
        f'<a href="/blog/{spec["slug"]}.html" class="post-card" data-category="{spec["category"]}">'
        f'<span class="post-tag">{spec["pillar"]}</span>'
        f'<p class="post-title">{spec["title"]}</p>'
        f'<p class="post-excerpt">{spec["excerpt"]}</p>'
        f'<div class="post-meta"><span>{spec["read_time"]} · {spec["date_label"]}</span>'
        f'<span class="post-read">Read →</span></div></a>'
    )
    m = re.search(r'<a href="/blog/[^"]+" class="post-card"', doc)
    if not m:
        raise SystemExit("build_post: no post-card found in blog.html")
    doc = doc[: m.start()] + card + doc[m.start():]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return True


def build(root: str, spec_path: str) -> str:
    spec = json.load(open(spec_path, encoding="utf-8"))
    shell_path = os.path.join(root, spec.get("shell", "blog/best-geo-tracker-tools-2026.html"))
    doc = open(shell_path, encoding="utf-8").read()

    # head
    doc = swap(doc, r"<title>.*?</title>", f"<title>{spec['title']} — BuzzRiding</title>", "<title>")
    doc = swap(doc, r'<meta name="description" content=".*?"\s*/?>',
               f'<meta name="description" content="{spec["description"]}" />', "meta description")
    # strip every existing head tag CI regenerates, plus the shell's JSON-LD
    doc = re.sub(r'\s*<link rel="canonical"[^>]*>', "", doc)
    doc = re.sub(r'\s*<meta property="og:[^>]*>', "", doc)
    doc = re.sub(r'\s*<meta name="twitter:[^>]*>', "", doc)
    doc = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", doc, flags=re.S)
    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": spec["title"], "description": spec["description"],
        "datePublished": spec["date"], "dateModified": spec["date"],
        "author": {"@type": "Organization", "name": "BuzzRiding", "url": "https://buzzriding.github.io"},
        "publisher": {"@type": "Organization", "name": "BuzzRiding", "url": "https://buzzriding.github.io"},
    }
    doc = doc.replace("</head>", '  <script type="application/ld+json">'
                      + json.dumps(ld, ensure_ascii=False) + "</script>\n</head>", 1)

    # header furniture
    doc = swap(doc, r'<span style="color:var\(--teal\)">.*?</span>',
               f'<span style="color:var(--teal)">{spec["pillar"]}</span>', "breadcrumb pillar")
    doc = swap(doc, r'<span class="post-tag">.*?</span>',
               f'<span class="post-tag">{spec["pillar"]}</span>', "post tag")
    doc = swap(doc, r'<span class="post-date">.*?</span>',
               f'<span class="post-date">{spec["date_label"]}</span>', "post date")
    doc = swap(doc, r'<span class="post-read-time">.*?</span>',
               f'<span class="post-read-time">{spec["read_time"]}</span>', "read time")
    doc = swap(doc, r"<h1>.*?</h1>", f"<h1>{spec['title']}</h1>", "h1")
    doc = swap(doc, r'<p class="article-intro">.*?</p>',
               f'<p class="article-intro">{spec["intro"]}</p>', "intro")

    # body
    doc = swap(doc, r'(<article class="article-body"><div class="article-container">).*?(</div></article>)',
               '<article class="article-body"><div class="article-container">'
               + spec["body"] + "</div></article>", "article body")

    # related cards
    cards = "".join(
        f'<a href="/blog/{c["slug"]}.html" class="related-card">'
        f'<p class="related-tag">{c["pillar"]}</p>'
        f'<p class="related-title-text">{c["title"]}</p>'
        f'<p class="related-read">{c["read"]} →</p></a>'
        for c in spec["related"])
    doc = swap(doc, r'(<div class="related-grid">).*?(</div>\s*</section>)',
               f'<div class="related-grid">{cards}</div></section>', "related grid")

    out = os.path.join(root, "blog", spec["slug"] + ".html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    carded = add_card(root, spec)
    print(f"built blog/{spec['slug']}.html ({os.path.getsize(out)} bytes)"
          + ("  + blog.html card" if carded else "  (card already listed)"))
    return out


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--all" in sys.argv:
        specs = sorted(glob.glob(os.path.join(root, "content", "*.json")))
        built = 0
        for spec_path in specs:
            slug = os.path.basename(spec_path)[:-5]
            out = os.path.join(root, "blog", slug + ".html")
            if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(spec_path):
                continue
            build(root, spec_path)
            built += 1
        print(f"{built} post(s) built from {len(specs)} content file(s).")
        return 0
    if len(sys.argv) < 2:
        raise SystemExit("usage: build_post.py content/<slug>.json | --all")
    build(root, sys.argv[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
