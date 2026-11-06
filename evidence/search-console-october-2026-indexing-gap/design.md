# Design note — October 2026 Search Console check

**Written:** 2026-11-06, before pulling the October/November custom date ranges below.
**Question:** Did reverting from 4 articles/month (September) back to 14 articles/month
(October) increase Search Console impressions and clicks, as the 2026-10-02 update
to `blog.md` argued the Jun–Sep trend predicted?

**Method:** Pull three custom date ranges from the Search Console Performance report
for `https://buzzriding.github.io/` (Web search type, no filters): 1–30 September 2026,
1–31 October 2026, 1–5 November 2026. Record total clicks, total impressions, average
CTR, average position for each. Separately record the Page indexing report's indexed/
not-indexed counts and "Last update" date, then live-inspect any URL it lists as
"Crawled – currently not indexed" or "Discovered – currently not indexed" via URL
Inspection to confirm the aggregate count is current.

**Sample:** One property, three date ranges, N=1 site. Not a controlled experiment —
September and October differ in both publishing volume and topic mix.

**What would make this not worth publishing:** If October's numbers simply continued
the Jun–Sep upward trend, confirming the volume argument, it would still be worth
publishing (per `experiments.md`: "Publish the bad result... publish the result even
when it is boring"). The only outcome that would make this *not* worth publishing is
if the three date-range pulls disagreed with each other in a way that suggested a
measurement error rather than a real pattern — in which case the post would report
that the data was inconclusive, not invent a conclusion.

**Result actually found:** October impressions and clicks both fell versus September,
against the volume thesis. Average position improved. Indexed-page growth slowed
sharply relative to articles published. The Pages report's aggregate "not indexed"
count was confirmed stale by live URL Inspection. See `gsc-data.csv` for the raw
figures and `../../content/search-console-october-2026-indexing-gap.json` for the
published post.
