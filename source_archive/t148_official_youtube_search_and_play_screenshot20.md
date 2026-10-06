# T148 — official-channel search and Play screenshot requests #20

Date: 2026-10-06, Asia/Dhaka. Four retrieval calls; exact per-call timestamps were not exposed.

## Retrieval log

1. `functions.web_search`, exact query `site:youtube.com/@firsttouchgames "Cult Heroes" "DLS26"` — status `success`; one result card, title `firsttouchgames`, URL `https://www.youtube.com/@firsttouchgames`. Snippet: “First Touch Games is an award-winning independent studio focusing on developing sports games for digital platforms.” No Cult Heroes video result. Search endpoint and HTTP status are not exposed.
2. `functions.fetch_page`, attempted URL `https://play-lh.googleusercontent.com/3wD-_bDOwy1DKi1t1kV_YSPX4VbMkOM1OsnKC2EE_1dsIswKVYDTWqk5mLRba5sw6-h9n4cJjNNlS5fKntQw=w526-h296-rw` — tool status `success`, title `Error 400 (Bad Request)!!1`, body says “400. That’s an error. Your client has issued a malformed or illegal request.” Transport status not exposed; no image bytes. The submitted string omits `Tp` from the canonical screenshot lead. This malformed near-match is not the canonical screenshot URL; no visual inference.
3. `functions.web_search`, exact query `site:youtube.com/@firsttouchgames "Cult Heroes" Agents announcement` — status `success`; same single channel-profile result, no event video/mechanics. Search endpoint and HTTP status are not exposed. Profile not fetched; snippets alone do not verify ownership.
4. `functions.fetch_page`, canonical screenshot #20 URL `https://play-lh.googleusercontent.com/3wD-_bDOwy1DKi1t1kV_YSPX4VbMkOM1OsnKC2EE_1dsIswKVYDTWqkTp5mLRba5sw6-h9n4cJjNNlS5fKntQw=w526-h296-rw` — failed with HTTP 500; no image/page content. No visual inference. Retire this exact URL; do not retry.

## Result and boundaries

No new game-mechanics evidence. The two searches surfaced only a channel-profile result, not a Cult Heroes video. The malformed URL returned an error page; the canonical screenshot #20 request independently returned HTTP 500. Screenshots #21–24 remain uninspected; neither failed request says anything about them. Cult Heroes route/rewards/current availability remain unconfirmed. “DLS26 has no position locking” remains `user-stated`; verification is owed. No spending advice, global-absence claim, exhaustion declaration, or research-dimension closure.

Ledger after T148: **814 records / 613 visited URL attempts / 394 unvisited leads**. The channel profile remains an unvisited lead if not previously recorded; it was not fetched.
