# T96 — FTG `player position` API search progressed

Date: 2026-10-06 Asia/Dhaka. Six retrievals in this turn; exact-call timestamps are not exposed. Ledger close/reconciliation time: 2026-10-05T23:21:58Z.

## Recovery
Opening reset to `fb9a2c0`, with 272 project files untracked and upstream unset. Clock was recorded first (`2026-10-06 05:20:43 +06`). Archived 272 files to `/tmp/dls26-t96-recovery-20261006052046.tar.gz`, SHA-256 `dc541ea4a324d53fb1a8d7b2b4897db3f25a6cc4f500ae6fede1e7d1201fab6c`. Fetched/restored the session branch at `b1842b7`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After overlay, only `logs/turn_clock.txt` differed (T96 start append); no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #58.

## Retrievals (6 total)
Four successful calls completed page 1 of the FTG `player position` API search at chunks 6–9; chunk 9 reported `hasMore=false`, `totalChunks=10`. Two successful calls then read page 2 at chunks 0–1; both report `hasMore=true`, `totalChunks=7`.

Page 1 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=player%20position`
Page 2 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=player+position`

The API reports 100 results, 25 per page, across 4 pages. Page 1 is complete (0–9/10); page 2 is partial (0–1/7), with chunks 2–6 unread and pages 3–4 unread. HTTP status is not exposed by the fetch tool.

Visible results remain mixed: Score! Match player behavior/stats; Ultimate Clash Soccer rules/attributes (including article 7918507871505); generic DLS player stats and player-management articles; and DLS Leaderboards text where “position” denotes rank. These do not answer whether DLS26 locks a player to a squad position. Stamina/workload and in-match control selection are distinct concepts. Do not transfer UCSS/Score! Match behavior to DLS26. No query-wide conclusion.

Resume page 2 at `chunkIndex=2` (chunks 2–6 remain; pages 3–4 unread).

## Ledger and status
Ledger: **698 entries / 516 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
