# T93 — FTG `position changes` page-2 continuation

Date: 2026-10-06 Asia/Dhaka. Six retrievals were executed; individual retrieval timestamps are not exposed. Ledger close/reconciliation time: 2026-10-05T23:09:31Z.

## Recovery
Opening reset to `fb9a2c0` with project files untracked and upstream unset. Recorded the clock first (`2026-10-06 05:06:38 +06`). Archived the 266-file workspace to `/tmp/dls26-t93-recovery-20261006050656.tar.gz`, SHA-256 `ea7a10aae3cbf5b51850ce21802888cebb326d33bb30b012aabab6d790b47f07`. Fetched and restored `origin/arena/01a1022d-dls26-omega` at `354d364`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After overlay, only `logs/turn_clock.txt` differed (the T93 start append); there were no untracked paths. No loss or force-push. ISSUE-0014 recovery occurrence #55.

## Retrievals (6 total)
All six calls continued the exact FTG Help Center API URL below at `chunkIndex=7` through `12`; each tool response reported `status=success`, `totalChunks=15`, and `hasMore=true`.

`https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=position+changes`

HTTP status is not exposed by the fetch tool. The page-2 response remains a mixed full-text search, not a DLS26-specific manual. Across the newly rendered chunks 7–12, visible content includes generic/older-game customization and profile/help material. One DLS Help Center result is “Why are my players auto-switching all the time?” (article 360008831518, section 203117809). Its text explains automatic control switching while defending to help select a nearby player; this is about in-match control selection, not changing a squad position or locking a player into one. It is not a DLS26 position-lock answer. Do not conflate this with squad assignment.

Earlier chunks in the same response included generic DLS player-stats stamina/workload text and an Ultimate Clash Soccer rules article; neither establishes DLS26 position-lock behavior. The new chunks do not resolve the target question. No query-wide absence conclusion is warranted.

## Ledger and status
Ledger remains **696 entries / 514 unique visited URLs / 405 unvisited leads**. The existing exact-URL page-2 record is updated through chunks 0–12/15; chunks 13–14 remain. Resume at `chunkIndex=13`.

DLS26 position-lock remains `user-stated` and unverified. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
