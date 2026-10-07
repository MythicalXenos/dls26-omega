# T157 — linked DLS social-page attempts and search-index snippets

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls: two direct profile fetches, two broad targeted searches, one exact-phrase TikTok search, and one direct TikTok result fetch.

## Direct profile attempts

- Facebook `https://www.facebook.com/dreamleaguesoccer` — `functions.fetch_page` HTTP 403; no page body/posts.
- TikTok `https://www.tiktok.com/@dreamleaguesoccer.ftg` — `functions.fetch_page` HTTP 403; no profile body/posts.
- The queried TikTok video `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809` — `functions.fetch_page` HTTP 403; no video/page body.

## Search outputs (not direct page retrievals)

1. Exact Facebook query: `site:facebook.com/dreamleaguesoccer "Cult Heroes" "Dream League Soccer"`. The search result described the linked DLS Facebook profile as an App page and said First Touch Games Limited is responsible for it. The returned snippet said: “Scoring team goals with a full squad of Cult Heroes hits different … Collect them in game now.” No post permalink was provided; profile fetch returned 403. Log this as search-index text only, not a verified availability or acquisition-route claim.
2. Exact TikTok query: `site:tiktok.com/@dreamleaguesoccer.ftg "Cult Heroes"`. The output bundled multiple snippets attributed to `@dreamleaguesoccer.ftg`, including “Cult Heroes are still available… Get Cult Hero Agents for a guaranteed Special Card” and “Collect them in game now.” It did not supply stable post permalinks for those lines. A returned DLS25 European-Classics video title was adjacent to some Cult Heroes text; do not attribute the text to that post without verification.
3. Exact-phrase TikTok query: `site:tiktok.com/@dreamleaguesoccer.ftg "Cult Heroes are coming" "Events, Drafts" "Season Pass"`. It returned `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809`, titled “A new era, a new card. #DLS25,” with a description that also included: “Cult Heroes are coming to #DLS26 on September 16th. Find them by collecting Cult Hero Agents, available in Events, Drafts and the Season Pass.” The DLS25 title and DLS26 snippet conflict/mismatch; direct fetch returned 403. The year, post attribution and route claim remain unverified.

## Interpretation limits and next step

These search snippets are discovery leads from accounts linked to the FTG YouTube channel, but the direct pages could not be inspected and one returned TikTok URL is a DLS25-labelled post. Do not promote them to confirmed DLS26 availability, route, reward or cost. No spending advice and no inference from blocked pages. Next, resolve the exact post permalink/date for the two snippets using fresh exact-phrase searches on the linked handles, then inspect only a directly attributable FTG post.

Position locking remains `user-stated`, verification owed. No global-absence inference, exhaustion declaration or research-dimension closure.

Ledger after T157: **846 records / 630 visited URL attempts / 390 unvisited leads**.
