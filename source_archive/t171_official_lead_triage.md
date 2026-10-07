# T171 — distinct FTG first-party lead triage

Date: 2026-10-06, Asia/Dhaka. Two retrieval calls.

## 1. FTG corporate-domain search

`functions.web_search` exact query: `site:firsttouchgames.com "Cult Heroes" "DLS26"`. The tool returned `status=success` with an empty result set. This is a query-specific search-index outcome only; it does not establish absence of FTG content or event availability.

## 2. FTG-linked official teaser page, chunk 1

`functions.fetch_page` requested `https://www.youtube.com/watch?v=gpvjf6qVl5c` at `chunkIndex=1` only. Tool status was `success`; numeric HTTP status was not exposed. The page title is “Dream League Soccer 2026 | OFFICIAL TEASER TRAILER.” This chunk returned a large player-configuration payload rather than a transcript or rendered gameplay. No Cult Heroes route, reward, cost, player list, or position-lock information surfaced.

T146 recorded chunk 0 of this same page as a 154-chunk response; T171 reports `totalChunks=163` and `hasMore=true`. Preserve this discrepancy; do not infer the unrendered chunks. The page remains script-heavy and low priority, with chunks 2–162 unread under the latest response. Continue only if a later distinct reason makes it useful.

## Scope and limits

The FTG-site search and teaser-page continuation did not resolve Cult Heroes route/rewards or DLS26 squad-position behavior. “DLS26 has no position locking” remains `user-stated`, verification owed. The exact FTG Help Center `position lock` and `position locking` searches remain complete and must not be repeated. The YouTube channel search from T170 is malformed and must not be retried; the known Google Play event-art variants were already recorded HTTP 500 and were not retried in T171. No global-absence inference, spending advice, dimension closure, or exhaustion declaration.

Ledger after T171: **872 records / 637 visited URL attempts / 390 unvisited leads**.
