# T161 — FTG position-lock query continuation

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls: `position lock` chunks 5–9 and `position locking` chunk 1. All returned tool status `success`; numeric HTTP status not exposed.

## Completed `position lock` query

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20lock`. T160 read chunks 0–4; T161 read chunks 5–9. Chunk 9 reported `hasMore=false`; all 10 rendered chunks are now read. The remaining body fragments continue the generic DLS player-stats article (not position-lock guidance), Score! Match player-types/gameplay material, and other FTG content. No DLS26-specific position-lock rule surfaced in this exact query.

## Partial `position locking` query

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20locking`. Chunks 0–1/10 are now read; chunks 2–9 remain unread. Chunk 1 continues Season Pass tier-lock and Score! Match stats results. This is a mixed-title search result, not DLS26 squad-position guidance.

## Boundaries

No result supports or refutes global DLS26 position-lock behavior. “DLS26 has no position locking” remains `user-stated`, verification owed. Cult Heroes route/rewards remain unconfirmed. No spending advice, dimension closure or exhaustion declaration.

Ledger after T161: **861 records / 636 visited URL attempts / 391 unvisited leads**.
