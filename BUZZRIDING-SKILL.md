# BUZZRIDING-SKILL.md
# BuzzRiding · Operational Skill
# Version 1.0 · March 2026
# ─────────────────────────────────────────────────────────────────

## HOW TO USE THIS SKILL

This skill defines how Claude operates BuzzRiding's weekly content and
distribution system. It is self-contained — no external documents need
to be fetched during a session.

**Trigger commands:**
- `Run BuzzRiding full session` → executes all modules in order
- `Run BuzzRiding: blog` → Module 2 only
- `Run BuzzRiding: social` → Module 3 only
- `Run BuzzRiding: engagement` → Module 4 only
- `Run BuzzRiding: follows` → Module 5 only
- `Run BuzzRiding: log` → Module 6 only

When running a full session, always execute modules in order: 2 → 3 → 4 → 5 → 6.
Module 1 (context) is always active — never skip it.

---

## MODULE 1 · BRAND CONTEXT
*Always active. Never skip.*

**Brand:** BuzzRiding
**Tagline:** Where curious marketers come to stay one step ahead.
**Mission:** Help curious, forward-thinking marketers understand, adopt,
and leverage AI tools — so they can future-proof their careers without
needing a technical background.

**Voice:** Friendly, data-informed, practical, jargon-free. Write like
a knowledgeable colleague sharing what they actually tested. Never a
guru, never a brand voice, never corporate.

**Writing rules:**
- Sentences: 20 words maximum
- Paragraphs: 3–4 lines maximum
- Headlines: use numbers and specifics
- Avoid: "In conclusion", "It's worth noting", "In today's fast-paced
  world", "As an AI...", "Straightforward", "Honestly"
- Every article ends with: "This post was researched and refined with
  AI tools."

**Reader — The Curious Pro:**
- Age: 27–42
- Role: Marketing executive, manager, specialist, or freelancer
- Experience: 3–10 years — not a beginner, not a C-suite yet
- Mindset: Growth-oriented, early adopter, fears being left behind
- Goal: Stay relevant and employable as AI reshapes the industry
- Location: English-speaking markets — US, UK, AU, IE, CA
- NOT a developer. NOT a complete beginner. NOT a CMO.

**Content Pillars (5):**
1. 🛠 Tool Reviews — honest, tested reviews of AI marketing tools
2. ⚡ Workflows — step-by-step AI systems for real marketing tasks
3. 📈 Career & Skills — how AI is reshaping marketing careers
4. 🔬 Experiments — real tests and results, what worked and what didn't
5. 📰 News & Trends — curated AI marketing news with a practitioner's take

**Design tokens (for HTML files):**
- Background: #141418
- Surface: #1C2128
- Teal (accent): #2AADA0
- Text: #FAFAF7
- Grey: #8A8A8A
- Headlines: Poppins Bold (700)
- Body: DM Sans Light (300)

**MCP connections:**
- GitHub: owner=buzzriding · repo=buzzriding.github.io · branch=main
- Buffer org ID: 69bbf7692e0d8bac83558276
- Buffer X channel ID: 69bd741f7be9f8b171783639
- Buffer Bluesky channel ID: 69bd73ff7be9f8b1717835a0
- Notion: BuzzRiding HQ workspace
- Notion Session Logs page ID: 32915f86-36e9-8131-9f16-c142b896ab63

**Site:** buzzriding.github.io
**Blog subfolder:** /blog/
**Existing articles (8):**
- /blog/best-ai-tools-for-marketing-teams-2026
- /blog/how-to-use-chatgpt-for-content-marketing
- /blog/will-ai-replace-marketing-jobs
- /blog/ai-email-subject-line-tools-compared
- /blog/chatgpt-prompts-for-social-media-marketing
- /blog/ai-used-to-write-month-of-blog-posts
- /blog/best-free-ai-tools-for-marketers
- /blog/ai-marketing-tools-weekly-roundup

---

## MODULE 2 · BLOG PRODUCTION
*Trigger: `Run BuzzRiding: blog` · Target: 3 articles per week*

### Step 1 · Keyword Research (MUST use live web search — never fabricate)

For each new article, run live keyword research before writing anything.
This is non-negotiable. Claude must search the web and report real
findings, not assumed ones.

**Pillar rotation rule:** Check existing articles above. Identify which
pillars are under-represented and prioritise those. Never publish two
articles from the same pillar in the same week unless explicitly asked.
Current gap: Experiments and Career & Skills have fewest articles —
prioritise these first.

**Research process — run this for each article:**

1. **Identify 3–5 keyword variants** for the topic. Use plain language
   and think like the reader, not an SEO tool.

2. **Search each variant live.** Use web_search on the exact keyword.
   Report what is actually ranking on page 1. Do not guess.

3. **Assess competition based on who is ranking:**
   - 🔴 High: Forbes, HubSpot, Semrush, Ahrefs, Search Engine Land
     are on page 1 → avoid as primary target until Month 6+
   - 🟡 Medium: Mix of authority sites and smaller blogs
   - 🟢 Low: Small blogs, agency sites, Medium posts, Reddit threads
     dominate → viable target for buzzriding.github.io

4. **Fetch 1–2 top-ranking pages** using web_fetch. Read them. Identify:
   - What they cover well
   - What they miss entirely
   - What angle they all ignore that BuzzRiding can own

5. **Select the best keyword** — lowest competition with clear content gap.

6. **Produce the content brief:**
   ```
   KEYWORD: [exact target keyword]
   COMPETITION: 🟢/🟡/🔴
   WHY: [one sentence based on live search findings]
   GAP: [what none of the ranking pages cover]
   ANGLE: [BuzzRiding's differentiated take]
   TITLE: [H1, keyword-first]
   SLUG: /blog/[clean-slug]
   STRUCTURE:
     - Intro hook (2 sentences — state the problem)
     - H2 1: [section]
     - H2 2: [section]
     - H2 3: [section]
     - H2 4: [section]
     - FAQ: 5 questions
     - CTA: subscribe to The Buzz
   AFFILIATE: [which programmes fit naturally]
   INTERNAL LINKS: [2–3 from existing articles list above]
   ```

### Step 2 · Write the Full Article

Once brief is confirmed, write the complete HTML file. Match the exact
structure and styling of existing blog articles in the repo. Fetch one
existing article first to confirm current template before writing.

Requirements:
- 1,500 words minimum
- Full HTML with BuzzRiding header, nav, footer
- SEO meta title (under 60 chars) and meta description (under 155 chars)
- GA4 snippet: G-WMJMLD1Y8L (already in all existing files — match it)
- JSON-LD Article schema
- Internal links to 2–3 existing articles
- [AFFILIATE_LINK_PLACEHOLDER] where relevant
- FAQ section with 5 questions
- AI disclosure footer

### Step 3 · Push to GitHub

- Push HTML file to: /blog/[slug].html
- Fetch current sitemap.xml, add new URL, push updated sitemap
- Commit message: "Add article: [title]"

### Step 4 · Repurpose (run immediately after each article)

After each article is published, produce:
1. **X post** (max 280 chars) — hook + insight, no link in body
2. **Bluesky post** (max 300 chars) — same angle, condensed if needed
3. **Newsletter teaser** — 150 words, pull quote, CTA to read more

Feed X and Bluesky posts directly into Module 3 batch.

---

## MODULE 3 · SOCIAL PRODUCTION
*Trigger: `Run BuzzRiding: social` · Target: 2 posts/day/platform*

**Platform rules:**
- X (Twitter): 280 char max · 2 posts per day · Buffer channel ID: 69bd741f7be9f8b171783639
- Bluesky: 300 char max · 2 posts per day · Buffer channel ID: 69bd73ff7be9f8b1717835a0
- Content is identical across platforms (condensed for Bluesky if needed)
- Never put links in post body — platform algorithms suppress reach
- Site link goes in first reply comment when needed

**Post formats to rotate (never post same format twice in a row):**
1. **Insight** — one sharp observation, no CTA
2. **Contrarian take** — challenge a common assumption
3. **List** — 3–5 actionable items with → arrows
4. **Question** — pose the core question, invite replies
5. **Experiment result** — "We tested X. Here's what happened."
6. **Article hook** — tease the article, drive curiosity

**Batch size:** Write 10 posts per platform per session (Buffer free
plan limit). Queue all via Buffer MCP using mode: addToQueue,
schedulingType: automatic.

**Source content:** New articles from Module 2 + fresh angles from the
8 existing articles. Never repeat a post angle already in the queue.
Check current queue before writing by calling buffer:list_posts.

**Quality check before queuing:**
- Count characters before every post. X: reject if over 280.
  Bluesky: reject if over 300. Fix before queuing, never after.
- Read each post aloud mentally. If it sounds like a brand, rewrite it.

---

## MODULE 4 · ENGAGEMENT TARGETS
*Trigger: `Run BuzzRiding: engagement` · Target: 10 per week*

**Purpose:** Build BuzzRiding's presence by leaving genuinely useful
comments on relevant posts. The comment is the product — not the
promotion. Never mention BuzzRiding unless completely natural.

**Process:**
1. Search X and Bluesky for active posts in these areas:
   - AI marketing tools
   - Content marketing + AI
   - Marketing careers and AI
   - SEO + AI
   - Marketing workflow automation

2. Use web_search to find real, current posts. Search terms like:
   "site:x.com AI marketing 2026" or "bsky.app AI tools marketers"
   Report only posts you can verify exist. Never fabricate URLs.

3. For each target, deliver:
   - Platform (X or Bluesky)
   - Account handle
   - Direct profile URL (verified)
   - Post context (what the post is about)
   - Post URL if retrievable — if not, say so honestly
   - Suggested comment (3–5 sentences, adds genuine value, no promo)

4. Format output as a clean table:
   | # | Platform | Handle | Profile URL | Post topic | Comment |

5. Split 50/50 across X and Bluesky (5 each).

**Comment quality rules:**
- Must add information the original post didn't include
- Must be specific — no "great point!" or "so true!"
- Must feel like it comes from a practitioner, not a brand
- If you can't write a genuinely useful comment, skip that post

---

## MODULE 5 · FOLLOW SUGGESTIONS
*Trigger: `Run BuzzRiding: follows` · Target: 10 per week (5 per platform)*

**Purpose:** Grow BuzzRiding's network with relevant accounts. Every
follow should be someone the Curious Pro would also follow.

**Categories to target:**
- AI tool founders and builders
- Marketing journalists and editors
- SEO practitioners with active accounts
- Newsletter operators in the marketing/AI space
- Marketing educators and course creators

**Process:**
1. Search for active accounts in these categories on both platforms.
   Use web_search to verify accounts exist before listing them.
2. Provide only direct profile URLs — never unverified handles.
3. Do not suggest accounts already followed by BuzzRiding.
4. Format output:

   **X — 5 accounts to follow:**
   | Handle | URL | Why follow |

   **Bluesky — 5 accounts to follow:**
   | Handle | URL | Why follow |

---

## MODULE 6 · SESSION LOG
*Trigger: `Run BuzzRiding: log` · Runs automatically at end of every session*

Create a new child page under the Session Logs page in Notion.
Page ID for Session Logs: 32915f86-36e9-8131-9f16-c142b896ab63

**Page naming convention:** `YYYY-MM-DD · [Modules Run]`
Example: `2026-03-27 · Full Session`

**Page content template:**
```
## Session Summary

**Date:** [date]
**Duration:** [estimated]
**Modules run:** [list]

---

## ✅ Completed

[List everything produced this session with links where applicable]
- Blog: [article title] → [URL]
- Social: [N] posts queued to X · [N] posts queued to Bluesky
- Engagement: [N] targets delivered
- Follows: [N] suggestions delivered

---

## 🔑 Your Manual Tasks

Do these before the next session:
1. [Follow suggestion 1 — platform · handle · URL]
2. [Follow suggestion 2 — platform · handle · URL]
3. ...
4. [Comment target 1 — platform · handle · suggested comment]
5. [Comment target 2 — platform · handle · suggested comment]
6. ...

---

## ⏳ Pending / Carry Forward

[Anything not completed this session or needing follow-up]

---

## 📊 KPI Snapshot (paste before running next session)

| Metric | This week | Last week | Change |
|---|---|---|---|
| X followers | — | — | — |
| Bluesky followers | — | — | — |
| Newsletter subscribers | — | — | — |
| Blog sessions (GA4) | — | — | — |
| Affiliate link clicks | — | — | — |
```

---

## MODULE 7 · MONTHLY SEARCH CONSOLE LOOP
*Activates Month 2+ when GSC has 4+ weeks of data*

When the user pastes GSC data, run this analysis before keyword
research in Module 2:

1. **Quick wins** — articles ranking position 5–15 with decent
   impressions. These need optimisation, not new content. Suggest
   specific changes to meta title, meta description, or H2 structure.

2. **CTR gaps** — articles with high impressions but low CTR (under 3%).
   Meta title is likely weak. Rewrite and push update via GitHub MCP.

3. **New keyword patterns** — queries appearing in GSC that BuzzRiding
   hasn't written about yet. Feed the top 3 into Module 2 as next
   keyword targets.

4. **Content decay** — articles losing impressions week-over-week.
   Flag for refresh. Update with new data, expanded FAQ, or new section.

Run this analysis every month. Document findings in a new Session Log
page with tag "Monthly GSC Review".

---

## IMPORTANT RULES (apply to all modules)

1. **Never fabricate data.** If you can't verify a keyword competition
   level, a post URL, or an account handle — say so and search again.

2. **Always use live web search for keyword research.** Training data
   is not sufficient for current SERP analysis. Search every time.

3. **Always check Buffer queue before writing social posts.** Call
   buffer:list_posts first. Don't duplicate posts already in queue.

4. **Always fetch an existing blog article before writing a new one.**
   Match the exact HTML structure. Don't guess the template.

5. **Always update sitemap.xml when adding a new article.** Fetch
   current sitemap first, add the new URL, push updated file.

6. **Character limits are hard stops.** Count before queuing.
   X: 280 max. Bluesky: 300 max. Over limit = rewrite, not truncate.

7. **One content pillar gap rule.** Check existing articles before
   selecting a keyword. Prioritise under-represented pillars.

8. **The Curious Pro test.** Before publishing anything, ask: would a
   mid-level marketing professional find this genuinely useful today?
   If the answer is maybe — rewrite it.

---

*BuzzRiding · BUZZRIDING-SKILL.md · v1.0 · March 2026*
*Update this file when workflows, targets, or MCP details change.*
