# T158 — exact social-caption searches and attribution status

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls total: two direct profile fetches, two linked-account phrase searches, one candidate TikTok video fetch, and one exact-phrase general web search.

## Retrieval details

1. Facebook `https://www.facebook.com/dreamleaguesoccer` — `functions.fetch_page` returned HTTP 403; no page body. This was an unintended retry of the same URL already blocked in T157.
2. TikTok profile `https://www.tiktok.com/@dreamleaguesoccer.ftg` — `functions.fetch_page` returned HTTP 403; no profile body. This was also an unintended repeat of the T157 blocked URL. Do not retry either profile URL again.
3. Exact Facebook query `site:facebook.com/dreamleaguesoccer "Scoring team goals with a full squad of Cult Heroes hits different"` returned the profile URL and the caption “Scoring team goals with a full squad of Cult Heroes hits different … Collect them in game now.” No unique post permalink/date; the direct profile remains blocked. Treat as an unverified search-index snippet.
4. Exact TikTok query `site:tiktok.com/@dreamleaguesoccer.ftg "Cult Heroes are still available" "guaranteed Special Card"` returned `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008`, titled as a DLS25 European-Classics/Four Classic Players post, while the search description bundled “Cult Heroes are still available…” and “Get Cult Hero Agents for a guaranteed Special Card.” The text-to-post attribution is uncertain.
5. Direct fetch of `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008` returned HTTP 403; no page/video content. Do not retry.
6. Exact phrase query `"Cult Heroes are still available for you to add to your squad" "Cult Hero Agents"` returned only secondary/community/creator/database pages (DLSKitURL, Reddit, YouTube creator video, DLSInside). None were opened or used as evidence.

## Interpretation limits

The social snippets suggest route/reward wording but neither a stable first-party permalink/date nor directly retrieved post content was obtained. The TikTok URL is DLS25-titled and its DLS26 text may be bundled search output. Do not promote “Agents,” Events/Drafts/Season Pass, guaranteed-card or current-availability claims from these snippets. The secondary exact-phrase results were not promoted. No spending advice.

T158 made two unintended repeat attempts against exact T157-blocked Facebook/TikTok profile URLs. Both returned 403 again, with no content. This procedural error is explicitly logged; no further repeats.

Cult Heroes route/rewards remain unconfirmed. “DLS26 has no position locking” remains `user-stated`, verification owed. No global-absence inference, exhaustion declaration or dimension closure.

Ledger after T158: **852 records / 633 visited URL attempts / 390 unvisited leads**.
