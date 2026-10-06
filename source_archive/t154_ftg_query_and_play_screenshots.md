# T154 — FTG position-query completion, Play screenshot attempts, and transcription correction

Date: 2026-10-06, Asia/Dhaka. Five retrieval calls total; exact per-call timestamps were not exposed.

## FTG Help Center query completion

Exact endpoint: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=assign%20player%20position`. Chunks 6, 7 and 8 returned tool status `success`; chunk 8 reported `hasMore=false`. Together with chunk 0 (T138) and chunks 1–5 (T153), all 9 rendered chunks are now read. The results are mixed across FTG products and include generic DLS stats/customisation material and older/other-title entries. A snippet in an earlier chunk says default player positions follow formation and ball position, but the available fragment does not identify its owning article/version. No DLS26-specific position-lock guidance surfaced; this exact phrase search does not establish global absence.

## Official Google Play screenshot attempts

- Screenshot #23: `https://play-lh.googleusercontent.com/OR7NRBrBLI3FkmlQOrKcZ3qZWjvl8lz26WSPnYNnPHAz3zvunpZWxkQYmoUBl3z453aFibmQzBZfaocm6OxI=w526-h296-rw` — `functions.fetch_page` returned HTTP 500; no image content.
- Screenshot #24: `https://play-lh.googleusercontent.com/kKbi-9I70rkHHpSnlD2T6UIas-5VD10niN36mi5v3WCv7_J8j8TQPLbGSzXkwFmk07fwhdpt2hW5NwmhrFOIyWU=w526-h296-rw` — `functions.fetch_page` returned HTTP 500; no image content.

Both exact URLs are retired; do not infer image contents.

## T149 transcription correction

The T149 result #3 Brave proxy URL was corrected in `source_archive/t149_image_search_visual_triage.md` and the ledger: base64 tail `dzUyNi1oMzk2` (embedded size `w526-h396`) corrected to `dzUyNi1oMjk2` (embedded size `w526-h296`), using the original image-search output. No refetch; the archived PNG and SHA-256 are unchanged.

## Boundaries and ledger

Cult Heroes route/rewards/current availability remain unconfirmed. “DLS26 has no position locking” remains `user-stated`, verification owed. No spending advice, global-absence inference, exhaustion declaration or research-dimension closure.

Ledger after T154: **828 records / 621 visited URL attempts / 390 unvisited leads**.
