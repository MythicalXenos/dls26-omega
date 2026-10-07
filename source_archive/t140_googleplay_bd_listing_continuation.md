# T140 — Google Play Bangladesh listing continuation and banner attempt

Date: 2026-10-06 Asia/Dhaka. Two fetch_page calls in the research portion; exact per-fetch timestamps are not exposed.

## Complete the partial Google Play BD listing

Exact URL: `https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en&gl=bd`. Retrieved chunk 1/2 only (chunk 0/2 was read in T139); the page is now complete. Chunk 1 shows a Google Play event tile with “Ends on 10/14” and “The names the fans remember, from their peak years,” linking to `https://play.google.com/store/apps/eventdetails/4830045897422713648`. That destination was already retrieved and recorded as `page-009-googleplay-cult-heroes-event`; do not repeat it or count it as an independent confirmation. The tile has no displayed year. The listing’s What’s New copy also says the Cult Heroes collection is “coming soon.” These are storefront contexts; they do not establish live in-game availability, route, cost, or rewards, and the apparent timing is not reconciled. Chunk 1 also exposes generic review/data-safety/developer content; none supplies game mechanics.

## Direct event-banner URL attempt

Exact URL: `https://play-lh.googleusercontent.com/AjvOMta70YWNd3eTjJO3i0hNzkEprOZzxtc45nWUgRLgH07HqTLkO-RRBL07AcqLlVwFxgYDyTb3T_Hj-UnXwSc=w648-h364-rw`. `functions.fetch_page` returned `Failed to fetch page (HTTP 500)`; no image bytes or visual contents were obtained. **This exact URL was already represented in the source ledger under `page-327-google-play-event-art-landscape-t67` before this call.** It was accidentally requested again after appearing in chunk 1 but before the exact-URL ledger check. No new source entry or unique-URL count was added; the repeat is logged as an attempt on the existing record. Do not retry. Its prior ledger payload summary is retained: `Direct fetch of the landscape image variant linked from the UK DLS26 Google Play listing returned HTTP 500; no bytes/image content were returned. No visual or OCR claims.`.

## Recovery before retrieval

At turn start the checkout was reset to `fb9a2c0` with all 365 non-ignored working files untracked and no upstream. Before reset/restore, archived and byte-verified 365 working files at `/tmp/dls26-t140-recovery-20261006090205.tar.gz`, SHA-256 `7850bd5ee4276051cd23c3aead143fd95f021d87d500ebadc2713ebb69683fd1`. Fetched pushed tip `cd9610e`, stashed the checkout as `e849699`, restored the fixed branch/upstream and repo-local identity, and restored the T140 clock entry.


## Reconciliation

The T139 Google Play BD listing entry was updated from partial to complete; its chunk-1 continuation was removed from the unvisited frontier. The already-ledgered banner URL attempt was added to its existing source record instead of creating a duplicate source record. Updated ledger count: 792 records / 595 unique visited URLs / 401 unvisited leads.
