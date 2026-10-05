# T97 — FTG `player position` API search progressed

Date: 2026-10-06 Asia/Dhaka. Six retrievals; per-call timestamps are not exposed. Ledger close/reconciliation time: 2026-10-05T23:25:37Z.

## Recovery
Opening reset to `fb9a2c0` with 274 project files untracked and upstream unset. Clock was recorded first (`2026-10-06 05:24:41 +06`). Archived 274 files to `/tmp/dls26-t97-recovery-20261006052444.tar.gz`, SHA-256 `af7b1fcffea4dad53f426bd4337919b76424094e7069e236ae2b6b8516451c2e`. Fetched/restored the session branch at `2b1ab17`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After overlay, only `logs/turn_clock.txt` differed (T97 start append); no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #59.

## Retrievals (6 total)
Five successful calls completed API page 2 at chunks 2–6; chunk 6 reported `hasMore=false`, `totalChunks=7`. One successful call read page 3 at chunk 0; it reported `hasMore=true`, `totalChunks=9`.

Page 2 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=player+position`
Page 3 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=3&per_page=25&query=player+position`

The API reports 100 results, 25 per page, across 4 pages. Page 1 (chunks 0–9/10) and page 2 (0–6/7) are complete; page 3 is partial at 0/9 and page 4 is unread. HTTP status is not exposed by the fetch tool.

Page-2 results remain mixed-product. Visible DLS Leaderboards text (article 360003914998) uses “position” for end-of-season standing/rank, not squad placement. UCSS role/attribute/matchmaking results are explicitly another FTG product. Generic DLS squad-expansion help and unrelated results do not establish DLS26 position locking. Page 3 chunk 0 contains UCSS and Score! Hero help. No DLS26 squad-position rule surfaced in the chunks read; do not infer absence from unread content or beyond this search.

Resume page 3 at `chunkIndex=1` (chunks 1–8 remain; page 4 unread).

## Ledger and status
Ledger: **699 entries / 517 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
