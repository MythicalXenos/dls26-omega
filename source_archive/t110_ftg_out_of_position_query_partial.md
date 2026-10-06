# T110 — FTG Help Center “out of position” query (partial)

Date: 2026-10-06 Asia/Dhaka. Two retrievals, chunks 0 and 1 of 13 on page 1.

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=out%20of%20position`. Exact query: `out of position`. The first response reported 34 results across 2 pages. Page 1 rendered as 13 chunks; page 2 also remains unread. `fetch_page` reported success for the two requested chunks; HTTP status and per-call timestamps were not exposed.

Chunk 0 surfaced Score! Match’s player-types article, a Score! Hero camera-position article, and Ultimate Clash Soccer rules. Chunk 1 continued the Ultimate Clash Soccer rules and surfaced a Dream League Live leaderboard article plus Score! Match player-stats material. The Dream League Live “position” wording concerns leaderboard rank, not DLS26 squad placement. No DLS26 lock answer appeared in these two partial chunks. Do not transfer other FTG games’ mechanics to DLS26; this partial result does not establish absence.

Recovery: this turn opened on reset `fb9a2c0` with 300 non-ignored project files untracked. Archived them to `/tmp/dls26-t110-recovery-20261006061549.tar.gz` (SHA-256 `15119c10ea785f9dbabac4e419960c41e58d04b7593b9cec72c4d1f7d6237a0a`; 300 members), then fetched and restored `9fbc24d`, upstream, and repo-local identity. The initial archive command’s `tar -tzf | head` listing ended with SIGPIPE before any restore/cleanup; a second call verified the full archive before recovery. No files were discarded. The T110 start marker was restored into the committed clock.

Ledger at close: **719 entries / 537 visited URLs / 401 unvisited leads**. Two retrievals. Cult Heroes route/rewards remain unresolved; position locking remains `user-stated` and unverified. No absence inference or exhaustion declaration.
