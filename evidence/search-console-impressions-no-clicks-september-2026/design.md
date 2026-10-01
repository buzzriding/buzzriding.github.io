# Design note: Search Console, 1–28 September 2026

**Honest status:** this note was written on 2026-10-01 *after* the tables were read, not before. Nothing here is a pre-registered test. It is a descriptive report of BuzzRiding's own Search Console numbers, which `experiments.md` lists as a valid evidence source.

## Question
Where did BuzzRiding's September search visibility sit, and which pages and queries produced the 14 clicks?

## Method
- Source: Google Search Console, Performance report, Search type: Web, property `https://buzzriding.github.io/`.
- Date range: 1–28 September 2026 (the report's "28 days" view; the report showed data to 28 September).
- Views read: site totals, the Pages table (top 10 of 38 rows by clicks), the Queries table (top 10 of 135 rows), and page-filtered Queries tables for the Surfer/Clearscope/Frase, AI marketing job titles, Claude Projects, AI skills and ChatGPT vs Claude vs Gemini pages.
- Values were copied by hand from the on-screen tables into the CSV files in this folder. They are not native exports. A transcription slip is possible; the totals row reconciles the 14 clicks across the nine pages that earned any.

## Known limits (from Google's own documentation)
- Anonymized queries are omitted from the query tables but included in totals unless a query filter is applied.
- Search Console stores top rows only, so not every query is shown.
- Impressions in the totals are displayed rounded ("2.6K").

## Derived figures in the article
- "More than a third of impressions": 979 impressions on one page against roughly 2,600 total.
- "About 1,600 impressions remain" and "near 0.9%": roughly 2,600 minus 979, and 14 clicks divided by that remainder. Approximate because the total is rounded.
- "302 impressions" for seven comparison queries: 53 + 50 + 37 + 35 + 49 + 39 + 39.

## What would have made this not worth publishing
A descriptive report has no pass/fail threshold. It is published because the pattern (one dominant zero-click page, two page-one positions resting on 1 and 4 impressions) changes how the site reads its own data.

## Files
- `totals.csv`
- `pages-top10-by-clicks.csv`
- `page-detail.csv`
- `queries-top10-site.csv`
- `queries-surfer-page.csv`
- `queries-job-titles-page.csv`
