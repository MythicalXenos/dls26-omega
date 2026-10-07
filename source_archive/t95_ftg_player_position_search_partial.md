# T95 — FTG `player position` Help Center query, partial

Date: 2026-10-06 Asia/Dhaka. Six retrievals; per-call timestamps are not exposed. Ledger close/reconciliation time: 2026-10-05T23:18:00Z.

## Recovery
Opening reset to `fb9a2c0`, with 270 project files untracked and no upstream. Clock recorded first (`2026-10-06 05:16:39 +06`). Archived 270 files to `/tmp/dls26-t95-recovery-20261006051641.tar.gz`, SHA-256 `31d9085b977632d01bba142fdf98e8e4ac13bae737ef55a1e8512e7e640fb714`. Fetched/restored session branch at `2ce9c1e`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After recovery, only `logs/turn_clock.txt` differed (T95 start append); no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #57.

## Retrievals (6 total)
A new FTG Help Center API query was fetched at the exact URL below. Chunks 0–5 each returned `status=success`, `hasMore=true`, `totalChunks=10`.

`https://support.ftgames.com/api/v2/help_center/articles/search.json?query=player%20position`

The API response reports 100 results, 25 per page, 4 pages total. Only page 1 chunks 0–5/10 have been read. HTTP status is not exposed. Visible chunks include “Where can I see the different player types?” (article 360000250309, explicitly Score! Match); Score! Match player-stats content; “What are the rules of Ultimate Clash Soccer?” (article 7918507871505, section 7900693036561); and DLS player-stats article 360019166777. The UCSS article discusses default movement based on formation and ball position, but it is explicitly about a different product. The DLS article's stamina wording concerns differing workload by playing position, not squad assignment or locking. None of this verifies DLS26 behavior.

Resume this exact URL at `chunkIndex=6` (page 1 chunks 6–9 and API pages 2–4 unread). Do not make a query-wide or absence conclusion from the partial response.

## Ledger and status
Ledger: **697 entries / 515 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
