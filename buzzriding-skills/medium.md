## Medium cross-post failures

### 2026-07-26 — Rate limit: max 2 published stories per 24 hours

**What happened:** Ran the weekly cross-post job to import the 3 oldest missing blog articles to Medium. The first two imported and published successfully:

1. "I A/B Tested AI Email Subject Lines for 60 Days" — https://buzzriding.github.io/blog/ai-email-subject-line-ab-test-results.html → https://medium.com/@buzzriding/i-a-b-tested-ai-email-subject-lines-for-60-days-buzzriding-66a1b95908a9
2. "I Let AI Write All My Social Posts for 30 Days" — https://buzzriding.github.io/blog/ai-wrote-my-social-posts-30-day-experiment.html → https://medium.com/@buzzriding/i-let-ai-write-all-my-social-posts-for-30-days-buzzriding-d1489c6fe59b

The third article imported cleanly (content, headings, images, and the canonical link back to buzzriding.github.io all rendered correctly), tags were added, but clicking **Publish** returned:

> "The author of this story has published or scheduled the maximum of two stories in the past 24 hours. Please try to publish or schedule again in 24 hours."

Trying **Schedule for later** as a workaround hit the same limit — it also counts against the same daily cap.

**Article left as an unpublished draft:**
"This Week in AI Marketing: March 27, 2026" — https://buzzriding.github.io/blog/ai-marketing-weekly-march-27-2026.html
Draft edit link: https://medium.com/p/6e72bd4591cf/edit
Tags already applied: Artificial Intelligence, Marketing, News

**Workaround / fix for next run:** Medium enforces a rolling 24-hour cap of 2 published (or scheduled) stories per author. When cross-posting 3+ articles in one session, only import and publish 2 per run, or space imports so each publish happens on a separate day. The next scheduled run should check for existing unpublished drafts first (via https://medium.com/me/stories?tab=drafts) and publish this pending draft before importing anything new, to avoid re-importing "This Week in AI Marketing: March 27, 2026" as a duplicate.
