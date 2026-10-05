# Turn 78 — FTG “formation position” search (partial)

## Recovery
T78 opened on the recurring reset signature: branch `fb9a2c0`, 236 project files untracked. Archived all 236 files (13,551,259 bytes), archive SHA-256 `2fc03af1aebed0479a8198a45a89990707fb932f4f499e413baee26ece26c294`; restored remote `a5e5653`; all 236 files matched after normalizing only the T78 clock-start append. ISSUE-0014 #40 records this; no loss/force-push.

## FTG Help Center query
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=formation%20position`
- `functions.fetch_page` chunks 0–5 were read; all returned status `success`, numeric HTTP status not exposed. The API reports 14 results on page 1/1, rendered across 9 chunks. Chunks 6–8 remain unread.
- Visible results include Score! Match player-stats/player-types and “How do I unlock a new formation?” articles; Ultimate Clash Soccer rules and “How do I change my formation?”; and DLS FAQ hits such as “What are Leaderboards?” and a previously read player-stats article. Product identities come from each result’s title/section metadata; no Score! Match or Ultimate Clash behavior is transferred to DLS.
- No DLS26 formation/position-lock rule is established from chunks 0–5. This response is incomplete and provides no absence conclusion.
- Resume exactly at `functions.fetch_page` chunkIndex 6 for the same URL; chunks 6–8 remain.

## Current status
DLS26 position-lock verification remains owed; user-stated “no position locking” remains unverified. Cult Heroes route/rewards remain unverified. No dimension closure or exhaustion declaration.
