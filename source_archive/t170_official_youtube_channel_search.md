# T170 — FTG YouTube channel search attempt for Cult Heroes

Date: 2026-10-06, Asia/Dhaka. One retrieval call: `functions.fetch_page` requested `https://www.youtube.com/@firsttouchgames/search?query=Cult%20Heroes`. The returned URL was `https://www.youtube.com/@firsttouchgames/search` (the query was dropped); tool status was `success`, while the rendered page contained an `Error 401 (Bad Request)` banner stating the request was malformed. Numeric HTTP status was not separately exposed.

## Observed output and limits

The YouTube shell displayed “This channel has no content that matched ‘Cult Heroes.’” Because the request is explicitly malformed and the query disappears from the returned URL, treat this as a failed/limited channel-search attempt, not a reliable zero-result search. It does not establish absence of official FTG Cult Heroes content and supplies no route, reward, cost, player-list, or DLS26 position-lock evidence. Do not retry this exact URL.

Local provenance check before retrieval showed the two known Google Play event-art variants (`w851-h2160` and `w648-h364`) are already recorded as HTTP 500 in T67; neither was retried. The next attempt should use a different, not-yet-visited first-party or in-game surface and should be checked against the exact-URL/blocked history.

Cult Heroes route/rewards remain unconfirmed. “DLS26 has no position locking” remains `user-stated`, verification owed. No global-absence inference, spending advice, dimension closure, or exhaustion declaration.

Ledger after T170: **870 records / 637 visited URL attempts / 390 unvisited leads**.
