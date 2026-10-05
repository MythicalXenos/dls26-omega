# T102 — FTG `squad position` API query (partial)

Date: 2026-10-06 Asia/Dhaka. Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=squad%20position`. Retrieval tool: `functions.fetch_page`; six successful chunk fetches (chunkIndex 0–5). The tool reports `status=success`; HTTP status code is not exposed. API metadata in chunk 0: count=25, page=1, page_count=1, per_page=25. The rendered response has 10 chunks; chunks 6–9 remain unread. Resume at `chunkIndex=6`.

## What the returned portions show

Results are mixed. Among visible DLS help items are generic squad expansion, role/formation navigation, player stats/upgrades and formation selection. The output also includes leaderboard/final-league “position” as rank and Score! Match / Ultimate Clash Soccer content. These topics do not establish DLS26 squad-player position-lock behavior. No such DLS26 rule surfaced in chunks 0–5; the query is partial, so draw no absence conclusion. Do not transfer other-product mechanics to DLS26.

## T101 provenance repair

At T102, repaired the four T101 web-search records that had inherited stale `source_id`, `search_query`, `search_results` and timestamp values. They now have unique source IDs, exact queries/results, canonical `retrieval_tool`, HTTP-not-applicable status, and transparent closeout-reconciliation timestamps (the search tool did not expose per-call timestamps). T101 query result payloads remain in `source_archive/t101_ftg_official_surface_searches.md`. No new retrieval was performed for the repair.

## Recovery and ledger

T102 opened on reset `fb9a2c0`; clock recorded first (`2026-10-06 05:42:52 +06`). Archived 284 files to `/tmp/dls26-t102-recovery-20261006054256.tar.gz`, SHA-256 `38f0e1e3f3bd600407806b2f56c57feae9bdf4f6912228b3a61bbe6dcdde5278`; fetched/restored session tip `81663b1`, upstream, and repo-local identity. After overlay, only the T102 clock-start append differed. ISSUE-0014 recovery occurrence #64; no loss/force-push.

The six-retrieval ceiling was reached exactly (chunk indices 0–5). Ledger: **705 entries / 523 unique visited URLs / 406 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, route, cost and rewards remain unresolved. No spending advice, dimension closure, or exhaustion declaration.
