# Design — AI answer citation index, run 2

Run 2 of the monthly index. **The method was fixed in advance of collection** by
run 1's design note (`evidence/ai-answer-citations-september-2026/design.md`)
and by the stored prompt of the scheduled task that executes this run, which
pins the eight prompts, the engine, the logged-out condition and the recording
step. This note records run 2's conditions and the measurement problems found,
and changes nothing about the method.

## Question
Unchanged from run 1: when a marketer asks Google's AI Mode a question
BuzzRiding has published an article about, which sources get cited — and does
BuzzRiding ever appear?

Run 2 adds the only question a second run can answer: **what moved?**

## Method
- Engine: Google AI Mode (`google.com/search?q=...&udm=50`), logged out.
- The same 8 prompts as run 1, unchanged, in the same order.
- ~8 seconds after each navigation, every external citation link in the AI
  answer body is enumerated and its domain recorded, in the order it appears.
- Run date: 2026-10-01, from Ireland (results are region-influenced).

## Engines attempted and dropped
- **Perplexity** and **ChatGPT** — still require a logged-in session. Excluded
  again, for run 1's reason: a result produced under a personal account is not
  reproducible by a reader. Open gap, declared, not quietly omitted.

## Measurement problems found in run 2

Recorded here because they limit what the month-on-month comparison can claim.

1. **Within-answer repeat citations.** In run 2, 19 of the 78 citations were a
   domain cited more than once inside the *same* answer. Run 1's CSV contains
   no within-answer duplicates at all. Two explanations fit: the answers
   genuinely changed shape, or run 1's recording collapsed duplicates. There is
   no way to tell from the artifacts, so **the raw citation totals (55 vs 78)
   are not safely comparable.** The comparison the post leads with instead is
   distinct domains per answer (55 vs 59), which is unaffected either way.
2. **Unstable element counts.** The enumeration step reported differing totals
   ("12", then "11") across two consecutive reads of the same unchanged page,
   while enumerating the same 10 links both times. The enumerated list, not the
   reported total, is what the CSV records.
3. **Answer-body scope.** One link on the *best GEO tracker tools 2026* page was
   identified as sitting in a related-results section rather than the answer
   body, and was excluded. Run 1's note does not say whether it drew the same
   boundary.

## Sample size
n=8 on one engine, two runs. Every prompt is reported individually in the CSV
and in the post. No averages across prompts, no percentage extrapolated from
this n.

## What would make this not worth publishing
Run 1's conditions, unchanged: if AI Mode refused or errored on most prompts, or
if the cited set were simply the top organic results. Neither happened.

A null result — nothing moved since September — was a publishable outcome under
the standing rule for this index: the run is published either way, and run 2 was
committed before it was known whether the comparison would be interesting.
