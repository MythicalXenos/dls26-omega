# Turn 75 — FTG API search completion and TikTok discovery attempts

## Reset recovery
T75 opened on the recurring sandbox-reset signature. The local branch was at `fb9a2c0` with 230 project files untracked. All 230 files (12,981,572 bytes) were archived; archive SHA-256 `fb0481d61fba1e3b2b01cc526365c3b0bf8f040ecbfe70055e4b19047cfa3e7d`. Remote fixed branch tip `8be1c4e` was restored and all 230 tracked files byte-verified with no mismatches after normalizing only the T75 clock-start append. ISSUE-0014 occurrence #37 records this; no loss/force-push.

## FTG Help Center API page 3
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=3&per_page=25&query=Cult+Heroes`
- `functions.fetch_page` status `success`, one complete chunk; numeric HTTP status not exposed. API reports `count=52`, page `3/3`, `per_page=25`, `next_page=null`. The last two results are generic Help Center articles “How do I have my personal data deleted?” (360017046578, section 203171905) and “How do I setup an iCloud account?” (360000613657, section 203171905). Neither addresses Cult Heroes or position locks.
- This completes pagination for the broad API query; the result set does not establish absence beyond the index/query and does not verify any DLS26 route/reward.

## Web-search discovery (not evidence)
Three queries were run:
1. `site:tiktok.com/@dreamleaguesoccer.ftg/video/ \"Cult Heroes\" Dream League Soccer 2026`
2. `\"Cult Heroes are still available for you to add to your squad\" \"dreamleaguesoccer.ftg\"`
3. `site:tiktok.com/@dreamleaguesoccer.ftg/video/ \"Cult Heroes are still available\" \"Get Cult Hero Agents\"`

Returned search results included previously visited URL `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809`, an older video URL `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008` described in the result title as a DLS25 Classic Players announcement, and an unrelated 2025 players video `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7588197165965593888`. Snippets interleaved additional Cult Heroes text under/near account labels but did not provide a distinct permalink tying those words to a specific post; one snippet also carried a secondary-source marker. No Cult Heroes statement is attributed to the older linked videos, and no route/reward claim is accepted from search snippets.

## Direct TikTok attempts
- `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7664965549348244758` — `functions.fetch_page` returned HTTP 403, no body. Do not repeat; this is not evidence of post contents or absence.
- `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008` — direct fetch returned HTTP 403, no body. Do not repeat; the search snippet was not mapped reliably to this URL.

## Current limits
Cult Heroes acquisition route/rewards and DLS26 position-lock behavior remain unverified. The broad 52-result FTG API search is complete, but its fuzzy matching is not an exhaustion test. No dimensions are closed; no spending recommendation.
