# Design — AI answer citation index, run 3

Run 3 of the monthly index. **Committed before any data was collected on
2026-11-01.** The method is not mine to change: it was fixed by run 1's design
note (`evidence/ai-answer-citations-september-2026/design.md`) and by the stored
prompt of the scheduled task that executes this run, which pins the eight
prompts, the engine, the logged-out condition and the recording step. This note
records run 3's conditions and the comparisons it is allowed to make. A separate
"measurement notes" section is appended to this file after collection; anything
written there is an observation about the run, never a change to the method.

## Question
Unchanged from runs 1 and 2: when a marketer asks Google's AI Mode a question
BuzzRiding has published an article about, which sources get cited — and does
BuzzRiding ever appear?

Run 3 adds the question a third run can start to answer: **is anything stable?**
Two runs give a difference. Three give the first weak signal about whether a
difference is a trend or noise.

## Method
- Engine: Google AI Mode (`google.com/search?q=...&udm=50`), logged out.
- The same 8 prompts as runs 1 and 2, unchanged, in the same order.
- ~8 seconds after each navigation, every external citation link in the AI
  answer body is enumerated and its domain recorded, in the order it appears,
  **including repeats within the same answer** (run 2's convention).
- Run date: 2026-11-01, from Ireland (results are region-influenced).

## Engines attempted and dropped
- **Perplexity** and **ChatGPT** — excluded again for run 1's reason, unless
  logged-out access has opened since: a result produced under a personal account
  is not reproducible by a reader. Checked each run; declared, not quietly
  omitted.

## Comparisons this run is allowed to make
Carried forward from run 2's measurement findings, which still bind:

- **Distinct domains per answer** is the primary comparable series (run 1: 55,
  run 2: 59). It is unaffected by whether a run collapsed within-answer
  duplicates.
- **Raw citation totals are NOT safely comparable across run 1 and run 2**
  (55 vs 78), because run 1's CSV contains no within-answer duplicates at all
  and there is no way to tell from the artifacts whether the answers changed or
  the recording did. Run 3 shares run 2's recording convention, so **run 3 may
  be compared to run 2 on raw totals, and to run 1 only on distinct domains.**
- **Per-prompt reporting only.** n=8. No averages across prompts, no percentage
  extrapolated from this n.
- Domain persistence across runs (a domain cited in 2 or 3 of 3 runs) is
  reported as a count of domains, never as a percentage.

## What would make this not worth publishing
Runs 1 and 2's conditions, unchanged: if AI Mode refused or errored on most
prompts, or if the cited set were simply the top organic results.

A null result — nothing moved since October, BuzzRiding still absent — is a
publishable outcome under the standing rule for this index. The run is published
either way, and this note was committed before it was known whether the
comparison would be interesting.
