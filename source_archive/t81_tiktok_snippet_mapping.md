# Turn 81 — TikTok caption mapping and official Facebook snippet

## Recovery integrity
Opening reset to `fb9a2c0` with 240 project files untracked. Archived all 240 files at `/tmp/dls26-t81-recovery-7qeOjD/workspace.tar.gz`, SHA-256 `859308621bd1cfd2976f726d8e58d218054470fa1a8cb5699cc5813e4f80ed4e`; restored remote branch at `375cb96` and byte-verified all 240 files after excluding only the T81 clock-start line. Upstream and repo-local identity restored; ISSUE-0014 #43 records this. No force-push.

## TikTok exact-phrase searches — captions still not attributable
All `functions.web_search` calls returned `status=success`; numeric HTTP status and request URL are not exposed. Search-result cards only: no underlying TikTok result page was retrieved successfully.

1. Query `site:tiktok.com/@dreamleaguesoccer.ftg "Find them by collecting Cult Hero Agents"` returned [7437552025958763809](https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809), titled “A new era, a new card. #DLS25” with result date 2024-11-15, and [7588197165965593888](https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7588197165965593888), titled “Get ready for the best players of 2025...” (DLS26/TO25). The route phrase appeared in the search text, but the result does not prove it belongs to either URL; the older DLS25 title/date makes the mapping especially ambiguous.
2. Query `"Cult Hero Agents" "Events" "Drafts" "Season Pass" "dreamleaguesoccer.ftg"` returned the same cards and mapping ambiguity.
3. Direct `functions.fetch_page` of new candidate URL 7588197165965593888 returned HTTP 403 and no payload. This is now a logged attempted URL, not an unvisited lead; do not infer absence or retry without a distinct access method.
4. Query `site:tiktok.com/@dreamleaguesoccer.ftg "Get Cult Hero Agents for a guaranteed Special Card"` returned [7477999051343007008](https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008), a DLS25 European Classics card dated 2025-03-04, with Cult Heroes text appended in the result. This URL was already blocked at T75; it was not fetched again. Do not map the guarantee to this video.

## Facebook result card — direct access blocked
- Query `site:facebook.com/dreamleaguesoccer "Cult Heroes" DLS26` returned one Dream League Soccer page card. Its snippet identifies First Touch Games Limited as responsible for the page and includes “Scoring team goals with a full squad of Cult Heroes hits different ... Collect them in game now.” It is undated search-result text and specifies no route/reward.
- Direct fetch of `https://www.facebook.com/dreamleaguesoccer/` returned HTTP 403 and no page payload. Do not infer absence or treat the snippet as a verified current in-game route.

## Status
These results are discovery leads, not verified game facts. They do not verify Cult Heroes availability, event dates, acquisition route, cost, or rewards. DLS26 position-lock behavior also remains unverified; the user's “no position locking” remains user-stated. No spending recommendation, scope closure, or exhaustion declaration.
