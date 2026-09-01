#!/usr/bin/env python3
"""Rebuild sitemap.xml from what is actually on disk.

Every root page and every blog post is included — the previous hand-maintained
sitemap was missing about.html and start-here.html. lastmod is preserved from
the existing sitemap where a URL is already listed, otherwise it falls back to
the post's datePublished in its Article JSON-LD, then to the file mtime.
"""

import datetime as dt
import glob
import json
import os
import re

SITE = "https://buzzriding.github.io"
ROOT_PAGES = [
    ("index.html", "1.0", "weekly"),
    ("blog.html", "0.9", "weekly"),
    ("start-here.html", "0.8", "monthly"),
    ("newsletter.html", "0.8", "monthly"),
    ("about.html", "0.6", "monthly"),
]


def existing_lastmod(root: str) -> dict[str, str]:
    path = os.path.join(root, "sitemap.xml")
    if not os.path.exists(path):
        return {}
    raw = open(path, encoding="utf-8").read()
    return {
        m.group(1): m.group(2)
        for m in re.finditer(r"<loc>(.*?)</loc><lastmod>(.*?)</lastmod>", raw)
    }


def published(path: str) -> str | None:
    doc = open(path, encoding="utf-8").read()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("datePublished"):
            return str(data["datePublished"])[:10]
    return None


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    known = existing_lastmod(root)
    rows = []

    for name, priority, freq in ROOT_PAGES:
        path = os.path.join(root, name)
        if not os.path.exists(path):
            continue
        loc = f"{SITE}/" if name == "index.html" else f"{SITE}/{name}"
        rows.append((loc, known.get(loc) or dt.date.today().isoformat(), freq, priority))

    for path in sorted(glob.glob(os.path.join(root, "blog", "*.html"))):
        loc = f"{SITE}/blog/{os.path.basename(path)}"
        lastmod = (
            known.get(loc)
            or published(path)
            or dt.date.fromtimestamp(os.path.getmtime(path)).isoformat()
        )
        rows.append((loc, lastmod, "monthly", "0.8"))

    # root pages first (in the order declared), then posts newest first
    roots = rows[: sum(1 for n, _, _ in ROOT_PAGES if os.path.exists(os.path.join(root, n)))]
    posts = sorted(rows[len(roots):], key=lambda r: r[1], reverse=True)
    rows = roots + posts

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, freq, priority in rows:
        out.append(
            f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>"
            f"<changefreq>{freq}</changefreq><priority>{priority}</priority></url>"
        )
    out.append("</urlset>")
    out.append("")

    with open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"sitemap.xml rebuilt with {len(rows)} URLs")


if __name__ == "__main__":
    main()
