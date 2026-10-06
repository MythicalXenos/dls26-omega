# T155 — targeted FTG social-channel discovery

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls total: four `functions.web_search`, two `functions.fetch_page`. Exact per-call timestamps and web-search numeric HTTP statuses were not exposed.

## Queries and results

1. Exact search query: `site:instagram.com/firsttouchgames "Cult Heroes" "Dream League Soccer"`. The result set returned an Instagram profile, `First Touch Games (@firsttouchgames_official)`, whose snippet self-identifies as the official account; no Cult Heroes post or route appeared in the returned result. Direct fetch of `https://www.instagram.com/firsttouchgames_official/` returned HTTP 403, with no profile body/posts. Treat the account label as a search-result self-description, not retrieved post evidence.
2. Exact search query: `site:x.com/firsttouchgames "Cult Heroes" "Dream League Soccer"`. Returned sample: historical @firsttouchgames X posts about DLS16 (2016), a support response (2017), Score! Hero (2020), DLS2023 (2022) and a DLS24 teaser (2023). No Cult Heroes-specific post appeared in this sample. No post fetched; not a global-absence result.
3. Exact search query: `site:facebook.com/firsttouchgames "Cult Heroes" "Dream League Soccer"`. Results included `https://www.facebook.com/firsttouchgames/` (general FTG profile text), its mentions page, and the similarly named `https://www.facebook.com/firsttouchgamess/` page (affiliation unverified). Direct fetch of `https://www.facebook.com/firsttouchgames/` returned HTTP 403; no page body/posts.
4. Exact search query: `site:youtube.com "DLS26" "Cult Heroes" "First Touch Games"`. Search-only results included DLS26/Cult Heroes tournament gameplay titles. Uploaders/ownership were not verified; no videos were opened. New low-priority unverified hits: `https://www.youtube.com/watch?v=xTqeXimUjv4` and `https://www.youtube.com/watch?v=RrUBfS1aeRM`. Existing overlapping results were already on the frontier. Do not use search snippets as first-party or in-game evidence, and do not promote any gameplay/route/reward claim.

## Limits and next step

No first-party Cult Heroes artwork, player-list, acquisition route or reward evidence was retrieved. Direct Instagram/Facebook profile failures reveal no page contents. No absence inference. Continue through a distinct first-party surface if useful; candidate next test is the unverified Instagram public-profile data URL in the handoff, not a retry of either blocked HTML page.

No position-lock conclusion changed: “DLS26 has no position locking” remains `user-stated`, verification owed. No research dimension closed; no exhaustion declaration or spending advice.

Ledger after T155: **834 records / 623 visited URL attempts / 390 unvisited leads**.
