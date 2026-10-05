# Turn 76 — FTG Help Center focused searches and a blocked TikTok post

## Recovery
Opened on the recurring sandbox-reset signature: `fb9a2c0`, 232 project files untracked. Archived 232 files (13,175,704 bytes), archive SHA-256 `63515a39b795d4963f7a4a613bcac4c9ce74e9712bd2247a6bb79074509d6166`; restored remote `0146b79`; all 232 files matched after normalizing only the T76 clock-start append. ISSUE-0014 #38 records this. No loss/force-push.

## Narrow FTG search: “Cult Hero Agents”
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Hero%20Agents`
- `functions.fetch_page`, success, one chunk; numeric HTTP status not exposed. API reports one result: article 360004066417, “How do I obtain more players?”, DLS FAQs `section_id` 203117809, labels include `agent`, `updated_at` 2026-09-19, `edited_at` 2024-12-06.
- The returned body lists Transfers, Scouts, Agents (“Agents will immediately add a player to your squad”), and Prize Ladder (special rare players when criteria is met). This article was already directly read as `page-063-ftg-obtain-players-faq`; the search result is a metadata refresh, not a new page fetch. It is general DLS mechanism text, not evidence about Cult Hero Agents, their route, cost, guarantee, or reward. The newer `updated_at` metadata does not prove the body changed.

## FTG search: “position lock” (partial; do not classify yet)
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20lock`
- API reports 16 results on one page, rendered across 10 chunks. Chunks 0–3 only were read this turn (six retrieval-call budget exhausted). Visible results mix Score! Match, Ultimate Clash Soccer, and DLS FAQs; some matches are Season Pass tier locks or unrelated position wording. Product-specific DLS26 position behavior is not established.
- Continue the exact response at `functions.fetch_page` `chunkIndex=4` through 9 before classifying. The URL is retained in the frontier with this continuation note.

## TikTok direct fetch
- `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7653879317407059203` returned HTTP 403/no body. Do not repeat this exact URL; blocked access is not evidence about the post.

## Current state
Cult Heroes route/rewards remain unverified. Position locking remains the explicit user-stated “none” claim, with verification owed. No dimension closure, no exhaustion, and no spending recommendation.
