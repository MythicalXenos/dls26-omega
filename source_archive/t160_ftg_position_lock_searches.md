# T160 — FTG Help Center exact position-lock searches

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls: two distinct query URLs at chunk 0, then chunks 1–4 of `position lock`. All returned tool status `success`; numeric HTTP statuses were not exposed.

## `position lock`

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20lock`. Response metadata: count=16, page_count=1, totalChunks=10. Chunks 0–4 read; chunks 5–9 remain. Visible material includes Score! Match captain/player-type content, camera controls, Season Pass tier-lock material, DLS Leaderboards, an Ultimate Clash Soccer rules article and the generic DLS player-stats article (already read elsewhere). The formation/ball-position snippet belongs to the Ultimate Clash Soccer rules result, not DLS26. No DLS26-specific squad-position lock guidance in chunks 0–4.

## `position locking`

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20locking`. Response metadata also count=16, page_count=1, totalChunks=10. Only chunk 0 read; its visible first-chunk results match the mixed `position lock` result. Chunks 1–9 remain unread.

## Interpretation limits

These are phrase-specific partial searches. The queried “lock” terms matched Season Pass tier locks and other-title content; that does not answer DLS26 squad-position behavior and does not support global absence. “DLS26 has no position locking” remains `user-stated`, verification owed. Cult Heroes route/rewards remain unconfirmed. No spending advice or research-dimension closure.

Ledger after T160: **859 records / 636 visited URL attempts / 392 unvisited leads**.
