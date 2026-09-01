# Design — AI answer citation index, run 1

Written **before** any data was collected, per `experiments.md`.

## Question
When a marketer asks Google's AI Mode a question BuzzRiding has published an
article about, which sources get cited — and does BuzzRiding ever appear?

## Method
- Engine: Google AI Mode (`google.com/search?q=...&udm=50`), logged out.
- 8 prompts, each mapped to a live BuzzRiding article on the same topic.
- For each: record every external domain cited in the AI answer, and whether
  buzzriding.github.io appears anywhere.
- Run date: 2026-09-01, from Dublin, Ireland (results are region-influenced).

## Engines attempted and dropped
- **Perplexity** — returned "Sign up and repeat your request" when logged out.
  Excluded from run 1 rather than run under an account, which would make the
  result non-reproducible for a reader.
- **ChatGPT** — requires a logged-in session; same reasoning. Both are noted as
  open gaps rather than quietly dropped.

## Sample size
n=8 on one engine. Small. Every prompt is reported individually in the CSV; no
averages, no percentages extrapolated from this.

## What would make this not worth publishing
- If AI Mode refused or errored on most prompts.
- If the cited set were simply the top organic results, making the exercise
  identical to reading a SERP.

Neither happened — the cited set includes domains that do not rank on page one,
which is the finding.
