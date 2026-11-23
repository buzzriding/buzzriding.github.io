# Design note — search-console-november-2026-zero-click-rankings

Written from the raw Search Console pull below, before the article body was drafted.

## Question

Across BuzzRiding's current 28-day Search Console window (25 Oct–21 Nov 2026), how many
pages rank at or near page one (average position ≤12, with at least 20 impressions to rule
out single-impression noise) and still earned zero clicks — and is that pattern consistent
with, or worse than, what published 2026 CTR-by-position research would predict?

## Method

1. Open the Performance report for property `https://buzzriding.github.io/`, Search type:
   Web (text), date range set to the in-app "28 days" preset (resolved to 25 Oct–21 Nov 2026).
2. Enable the CTR and Position columns (off by default).
3. Read the **Pages** tab at 50 rows per page (every page with at least one impression in
   the window) and transcribe Clicks / Impressions / CTR / Position for all 50 rows by hand
   into `pages-28d.csv`.
4. For the single highest-impression zero-click page, apply the `page` URL filter and read
   its **Queries** breakdown, transcribing the top 10 rows into
   `certifications-queries-28d.csv`.
5. Compare the resulting per-page CTRs against two independent, dated 2026 CTR-by-position
   studies: First Page Sage's "Google Click-Through Rates (CTRs) by Ranking Position" (blended
   and AI-answer-split CTR, Mar–Aug 2026, 1,184 domains) and Anicca's "Organic CTR by Position
   in 2026" (non-brand searches, six UK ecommerce/service sites, 20 Sep–8 Nov 2026).

## Sample

50 pages with at least one impression in the 28-day window. Six of those sit at position ≤12
with 20 or more impressions — those six are the ones discussed individually in the post.
Everything else is a single data point from one property in one month; it is reported as
exactly that, not as a trend.

## If absent

What would make this not worth publishing: if the pages ranking page-one-or-better also
earned a click share roughly in line with what First Page Sage's or Anicca's benchmarks
predict for that position band — i.e. if the numbers just confirmed "we match the published
average." That would be a null result worth a line in a monthly round-up, not its own post.
That is not what the pull showed: our single biggest page (434 impressions, position 5.4)
landed at 0% CTR against benchmarks that predict roughly 0.7–0.8% at that position, and five
more page-one-adjacent pages showed the same pattern.

## Caveats acknowledged before writing

- Transcribed by hand from the Search Console UI, not an automated export — a copying error
  is possible, which is why the raw rows are committed alongside this note.
- We did not check the live SERP for an AI Overview on the two biggest driving queries this
  session (browser time this session was reserved for Search Console only). The AI-answer
  explanation is presented as a plausible, cited hypothesis, not a confirmed cause.
- Two comparison studies are themselves single-vendor, proprietary-panel reports with
  disclosed samples of 1,184 domains and 6 sites respectively — cited as such, not as
  ground truth.
