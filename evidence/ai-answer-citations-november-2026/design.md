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

---

## Measurement notes — appended after collection, 2026-11-01

Observations about how run 3 went. Nothing here changes the method above.

1. **The logged-out re-check on Perplexity and ChatGPT could not be performed
   this month.** Navigation to `perplexity.ai` was refused by the browser
   permissions available to this session, so the engine was never reached. This
   is **not** an observation that it still requires a login — it is a check that
   did not happen. Both engines remain excluded on run 1's reasoning, and the
   re-check is still owed. Recorded rather than quietly skipped.
2. **Run 1's published total does not match run 1's own CSV.** The September
   post states 55 citations; the `citation_count` column of
   `citations-2026-09-01.csv` sums to **56**. Run 2's design note inherited the
   55. Where run 1 is cited for a number in run 3's post, the CSV figure (56) is
   used and the discrepancy is stated. Run 1's CSV also contains one malformed
   entry (`visbyblog`, not a domain), so run 1's domain-level data is the least
   clean of the three.
3. **Google's own properties were excluded, as in runs 1 and 2.** Two answer-body
   links pointed at Google surfaces (a Google Search Console link on *how to
   measure GEO ROI*, a Gemini link on *ChatGPT vs Claude vs Gemini*). Neither is
   an external citation and neither is recorded. Runs 1 and 2 contain no
   `google.com` entries either, with one exception: run 2 recorded
   `ads.google.com` on *what AI skills do marketers need in 2026*. That is an
   inconsistency in run 2, not a rule change here.
4. **Enumeration omitted links the DOM showed inside the answer region.** On
   *best GEO tracker tools 2026* two `youtube.com` links sat between enumerated
   citations and were not enumerated; on *ChatGPT vs Claude vs Gemini* a fourth
   `reddit.com` link was likewise not enumerated. Following run 2's rule — the
   enumerated list, not a count, is what the CSV records — they are excluded.
   Both answers' YouTube and Reddit presence is therefore recorded at or below
   the true figure, never above it.
5. **Answer-body scope, same boundary as run 2.** On *best AI tools for marketing
   teams 2026* two links were identified as sitting in a related-results section
   rather than the answer body and were excluded (a second `finance.yahoo.com`
   and a second `averi.ai`); `onelittleweb.com` appeared only in that section
   and so is absent from run 3's data entirely, despite being cited twice in run
   2's answer body for the same prompt.
6. **Vendor homepages are counted as citations.** Several answer-body links point
   at a product's own site rather than at editorial coverage of it
   (`otterly.ai`, `peec.ai`, `radarkit.com`, `heygen.com`, `synthesia.io`,
   `chatgpt.com`, `make.com`, `n8n.io`, `samsara.com`, `gomotive.com`,
   `bouncie.com`). Runs 1 and 2 counted these the same way. It means the
   citation count is not a count of publishers, and a share of the slots in a
   tool-comparison answer are structurally unavailable to a publisher.
