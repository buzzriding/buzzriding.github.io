# Design — Claude Cowork marketing blog case study

**Date:** 2026-10-16
**Slug:** claude-cowork-marketing-blog-case-study

## Question
What does running BuzzRiding's entire content-and-distribution operation
through an autonomous agent on Claude Cowork actually produce — stated
plainly, with the operational record attached so a reader can check it?

## Method
This is a self-report, not a blind test — BuzzRiding is both the operator and
the subject. It draws only on sources that are public and dated:

1. `HANDOVER.md` in `buzzriding/buzzriding-skills` — the 2026-09-01 audit of
   the first 64 posts.
2. `tools/integrity.py`, `tools/integrity.json` and `EVIDENCE.md` in
   `buzzriding/buzzriding.github.io` — the enforcement system and its current
   state, read live during this session.
3. The June–September cadence/traffic table already published in `blog.md`.
4. A live Google Search Console pull taken during this session: Performance
   report, property `https://buzzriding.github.io/` (URL-prefix), Web search
   type, 28-day window (16 Sep – 13 Oct 2026), and the Page Indexing report
   for the same property. Raw rows copied by hand into
   `gsc-28day-2026-10-13.md` in this folder, the same method the September
   Search Console post used, because the GitHub MCP cannot push a binary
   screenshot.

## What would make this piece not worth publishing
If the numbers were flattering and there was nothing to learn from them, or
if a figure in the post could not be traced to one of the four sources above.
Several numbers below are unflattering — 36 fabricated claims, 7 clicks in 28
days — and are published anyway, per BuzzRiding's own evidence rule.

## Known limits, stated up front
- n=1 property, n=1 operator. Nothing here generalizes to another site or
  another agent.
- The GSC pull is one 28-day window, copied by hand, not exported — a
  transcription slip is possible; the raw rows are in this folder to check.
- This is a report on BuzzRiding's own practice, not an independent audit of
  Claude Cowork. Where third-party coverage of Cowork is cited, it is
  attributed and linked, not restated as BuzzRiding's own finding.
