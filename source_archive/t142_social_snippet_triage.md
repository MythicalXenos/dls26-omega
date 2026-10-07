# T142 — first-party social snippet triage

Date: 2026-10-06 Asia/Dhaka. Four web_search retrieval calls (depth 2); per-call timestamps not exposed. Search-result text only; no Facebook, Instagram, or TikTok target page was retrieved.

## Instagram Reel search

Exact query: `site:instagram.com/reel/ "playdls" "Cult Heroes" "Dream League Soccer 2026"`. The search returned an empty results array. No absence inference.

## Facebook page search and follow-up

Query: `site:facebook.com/dreamleaguesoccer "Cult Heroes" "Agents" DLS26`. Three result cards appeared; the top card labels “Dream League Soccer (@dreamleaguesoccer)” and links to `https://www.facebook.com/dreamleaguesoccer/`. The snippet includes “Page · App page FIRST TOUCH GAMES LIMITED is responsible for this Page” and “Scoring team goals with a full squad of Cult Heroes hits different 😤 Collect them in game now. #DLS #DreamLeagueSoccer #CultHeroes #DLS26”. This is search-result snippet text, not a fetched post. The direct Facebook profile URL has prior HTTP 403 records (`page-303-facebook-dls-profile-attempt-t55`, `page-319-facebook-dls-profile-t64`); do not retry that blocked URL. The snippet provides no post date/permalink and no acquisition route, cost, or reward.

Follow-up exact query: `site:facebook.com/dreamleaguesoccer/posts "Scoring team goals with a full squad of Cult Heroes"`. It returned an empty results array. No absence inference.

## Cross-domain phrase attribution check

Exact query: `"Scoring team goals with a full squad of Cult Heroes hits different"`. One result card points to TikTok `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008`, titled “Four new Classic Players will be available tomorrow” and tagged DLS25/EuropeanClassics. The search description concatenates this older Classic-Players material with Cult Heroes Agent and “Collect them in game now” wording. This same exact TikTok result/source ambiguity is already documented in T81/T75; no page was fetched and it must not be used to attribute the Cult Heroes wording to that older clip. The Facebook search snippet remains unverified and does not establish game route or availability.

## Recovery

T142 began on reset checkout `fb9a2c0`; clock was recorded first. Archived and byte-verified 369 working files at `/tmp/dls26-t142-recovery-20261006091359.tar.gz`, SHA-256 `ca68fe0a9c29aa01bd5fe7f395b5223e8fbeb5e29e9a2d12b8f03970e6f7959c`; fetched/restored pushed tip `08f57cc`, restored upstream and repo-local identity, and retained safety stash `2b999af`. ISSUE-0014 occurrence #104.

Ledger after recording all four search calls: 797 records / 600 unique visited URLs / 400 unvisited leads. No Cult Heroes route/reward or DLS26 position-lock evidence established.
