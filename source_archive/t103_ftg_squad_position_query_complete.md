# T103 — FTG `squad position` Help Center query complete

Date: 2026-10-06 Asia/Dhaka. Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=squad%20position`. Retrieval tool: `functions.fetch_page`; T103 fetched chunks 6–9, each `status=success`. HTTP code is not exposed. Chunk 9 reports `hasMore=false`, `totalChunks=10`. T102 had fetched chunks 0–5.

## Complete query boundary and findings

The API response reports `count=25`, `page=1`, `page_count=1`, `per_page=25`; rendered payload is 10 chunks. The exact search is now complete. Returned material is mixed and mostly generic/older DLS Help Center content (squad expansion, role/formation navigation, player statistics/upgrades), leaderboard/final-league “position” as rank, and Score! Match/Ultimate Clash Soccer material. A UCSS rules result describes players following a formation- and ball-position-based pattern during play; it is explicitly UCSS and is not DLS26 evidence. DLS role/formation navigation likewise does not answer whether player cards can be position-locked.

No DLS26 squad-position-lock rule surfaced in this specific completed mixed search. This does not prove absence elsewhere and does not resolve the `user-stated` no-lock position. Do not transfer other-product behavior or older generic Help Center text to DLS26.

## Recovery and ledger

T103 opened on reset `fb9a2c0`; clock recorded first (`2026-10-06 05:46:54 +06`). Archived 286 files to `/tmp/dls26-t103-recovery-20261006054656.tar.gz`, SHA-256 `c6ed29b52f78ac5e6bfaadf6603530b49001c5e1d2cbc4fcb12165f5e3be1c38`; fetched/restored session tip `4cdf938`, upstream, and repo-local identity. After overlay, only the T103 clock-start append differed. ISSUE-0014 recovery occurrence #65; no loss/force-push.

Four retrievals (chunks 6–9) completed the page; combined with T102, the six-chunk T102 call budget is not relevant to this turn. T103 used four retrievals. Ledger: **705 entries / 523 unique visited URLs / 405 unvisited leads**. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending advice, dimension closure, or exhaustion declaration.
