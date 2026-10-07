# T99 — FTG `player position` query: page 3 complete, page 4 partial

Date: 2026-10-06 Asia/Dhaka. Six retrievals; per-call timestamps are not exposed. Ledger close/reconciliation time: 2026-10-05T23:31:47Z.

## Recovery
Opening reset to `fb9a2c0`, with 278 project files untracked and upstream unset. Clock recorded first (`2026-10-06 05:30:47 +06`). Archived 278 files to `/tmp/dls26-t99-recovery-20261006053051.tar.gz`, SHA-256 `7ab61d3daf0cd8dc4b10e54cb75d77507590a16711b569d172b709744137e24d`. Fetched/restored the session branch at `b7a3e1e`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After overlay, only `logs/turn_clock.txt` differed (T99 start append); no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #61.

## Retrievals (6 total)
Two successful calls completed page 3 at chunks 7–8; chunk 8 reported `hasMore=false`, `totalChunks=9`. Four successful calls read page 4 chunks 0–3; each reported `hasMore=true`, `totalChunks=9`.

Page 3 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=3&per_page=25&query=player+position`
Page 4 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=4&per_page=25&query=player+position`

The API reports 100 results across 4 pages. Pages 1–3 are complete; page 4 is partial at chunks 0–3/9. HTTP status is not exposed by the fetch tool.

Page 4 visibly includes generic DLS Season Pass help (article 4404070913169, section 203117809): its tier-lock language governs progression through season rewards, not a player's squad position. Other “position” wording in this mixed response refers to leaderboard/final-league rank. These results do not verify DLS26 squad-position locking. Chunks 4–8 remain unread; do not infer absence from this partial page or beyond the search.

Resume page 4 at `chunkIndex=4` (chunks 4–8 remain).

## Ledger and status
Ledger: **700 entries / 518 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
