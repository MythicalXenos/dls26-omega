# T100 — FTG `player position` API search completed; budget audit

Date: 2026-10-06 Asia/Dhaka. Ledger close/reconciliation time: 2026-10-05T23:34:54Z.

## Recovery
Opening reset to `fb9a2c0`, with 280 project files untracked and upstream unset. Clock recorded first (`2026-10-06 05:33:49 +06`). Archived 280 files to `/tmp/dls26-t100-recovery-20261006053354.tar.gz`, SHA-256 `500f729ad4b821d5305d95448a57dc5032fb3b0f541249474361c641e49690e9`. Fetched/restored the session branch at `5f0d876`, restored upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`. After overlay, only `logs/turn_clock.txt` differed (T100 start append); no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #62.

## Retrievals and budget audit
**Eleven retrieval executions occurred**, exceeding the six-retrieval turn ceiling by five. This was a budget-control error: three parallel fetch batches contained 3, 3, and 5 calls. Four were exact repeats of page-4 chunks 0–3, already fetched in T99; seven were new chunks (page 3 chunks 7–8 and page 4 chunks 4–8). No retrievals were made after this overrun.

All calls returned `status=success`. Page 3 chunks 7–8 completed that 9-chunk response. Page 4 chunks 0–3 were repeats; new chunks 4–8 completed page 4/4, with chunk 8 reporting `hasMore=false`, `totalChunks=9`.

Page 3 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=3&per_page=25&query=player+position`
Page 4 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=4&per_page=25&query=player+position`

The FTG Help Center API search reports 100 results across 4 pages. All pages are complete: page 1 10/10 chunks, page 2 7/7, page 3 9/9, page 4 9/9. HTTP status is not exposed by the fetch tool. Repeated page-4 chunks added no new evidence or unique URL.

The completed response remains mixed-product/older-help content. “Position” in DLS Leaderboards/final-league items means rank; DLS Season Pass tier locks govern reward progression, not player assignments; UCSS/Score! content is another product. No DLS26 squad-position locking rule surfaced in this specific completed search. Do not infer absence outside the search or beyond its wording.

## Ledger and unresolved targets
Ledger: **700 entries / 518 unique visited URLs / 404 unvisited leads**. The completed page-4 continuation lead has been retired. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration.
