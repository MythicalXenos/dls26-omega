# T114 — Bangladesh Google Play event page and screenshot leads

Date: 2026-10-06 Asia/Dhaka. Six retrievals: candidate Instagram profile, FTG About page, one localized Play event page, and three direct screenshot GETs.

## Play event page
Exact URL: `https://play.google.com/store/apps/eventdetails/4830045897422713648?gl=BD&hl=en`. `fetch_page` succeeded; HTTP status not exposed. The page renders “Event • Ends on 10/14” (year not shown) and generic copy about signing names and obtaining them for a limited time. It does not name players, state a route, cost, or reward list. It identifies the associated app as Dream League Soccer 2026 / First Touch Games Ltd. This is storefront text only; do not infer in-game availability or mechanics.

The page response exposed 24 screenshot links, while the historical S-0023 note says 20. Keep the count discrepancy open rather than harmonizing it. First three direct GETs returned `URLError: TLS/SSL connection has been closed (EOF) (_ssl.c:992)`; no HTTP response or image bytes. Do not retry those exact URLs. The remaining 21 exact URLs are listed below and queued individually. No screenshot was visually assessed.

## Exact screenshot URLs returned by the page (24)

The page response exposes 24 `w526-h296-rw` screenshot links. The older S-0023 notes say 20; retain this count discrepancy instead of harmonizing it. URLs 1–3 were each attempted once via `urllib.request`; all failed TLS/SSL before HTTP with no image bytes. Do not retry these exact three or infer visual contents. URLs 4–24 remain unvisited.

1. `https://play-lh.googleusercontent.com/ffYSk5S2cc5I1rt9T1hglwjmwu6cPPgsU_T6gAsJYzK_Jjln2WoQYKSwP4awob0FaCCJvETCjJVNiTRFuqaz=w526-h296-rw` — T114 direct GET attempted; TLS/SSL EOF before HTTP response; no bytes; do not retry.
2. `https://play-lh.googleusercontent.com/x_246-bsFC08UuCT4MFBba4FP_4OAwmn79JdNkKn3_c71xRbic_g_786PS7EqU5vUI6wjD0bV9sRguW5qFnQAQ=w526-h296-rw` — T114 direct GET attempted; TLS/SSL EOF before HTTP response; no bytes; do not retry.
3. `https://play-lh.googleusercontent.com/NF-ERjicP1xzbkCWkQOGZIeR0RWe-RokxLAocXvIB74LMSuX1FbFiEiAf7S7IQmSFtse3PTUwhgH1W5XYHCx=w526-h296-rw` — T114 direct GET attempted; TLS/SSL EOF before HTTP response; no bytes; do not retry.
4. `https://play-lh.googleusercontent.com/d0Pfspg2Bqdqp0RHUGGru-ilO-Pyq-4pmCB2_DRIqukkxoDt_vdIHdpAAtf7PWbY53rbLGZfuOLWQDXgJFUTVw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
5. `https://play-lh.googleusercontent.com/1guviZqNIulGQp-FTbh0BEEYw6lsgdPYFAKPqLXg1nUn3vxji_VERojgeE2UaX42Zt_swIFdlrA1Y8UJVDr4_g=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
6. `https://play-lh.googleusercontent.com/YK5LCoglhj8ZXB5yaM7zM8pRmzYWpetlhsVj3Zgsx0ah2pO5BqI10R8sl3Eyh0Tu6KWngVuGkvT3R9O4RtXM=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
7. `https://play-lh.googleusercontent.com/xnrPfNzmQ4sOl1YwIGBbKJScDSj9Hqx57Xg4m63GC6Swu-5Z8E7D-k0v_C5Qj9DfmcVJZOKRkFmFGp4VVb0HXQ=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
8. `https://play-lh.googleusercontent.com/8djmQFQ5-YRLHpUDyUmR3NyNPdTvd6cNFIfTxAKnRri0ZvstRwNZyGkjZs2LoRO5c3PyVNzFJi_5sCugZv_3yus=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
9. `https://play-lh.googleusercontent.com/QfnGqBQUfptOCmqKvFPByO9IrpJhdQOMbEqGcYURer53RF7z5xCGVnd9TT6J9cUSGUkzve1iGDo5yYEWcknROSw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
10. `https://play-lh.googleusercontent.com/LE_Ru9LmfZThTqc78Z3xvI_yabngdY-WohS9348FUnH-DawIc4R7U30s9VT86vYDiA0EKVlVQDXLDcRgr3eV3g=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
11. `https://play-lh.googleusercontent.com/tEgeHK-qliU3iD1mI1Hm_mCOHRTLTGwqzdNOx0fFt8XraGUVAiTwcuCQTnWLUAwEgcMB7jPI25cqKP9SzusKHw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
12. `https://play-lh.googleusercontent.com/_XzQcNoEgW7X1Fb8Jx0yjwMH90YYO3LNTkzdbZPnPyhaLLPHUrBty5-8WJimr9Y9eeLTMT_FbnHObPs3vJHOFnM=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
13. `https://play-lh.googleusercontent.com/aEh1y9_WcQ_lh4_WpvCdaC6aqbRj1IhTkAXUoIxMtEkdzPLPmWRAAD9dMmnn0jSxXPbRhqfATsW4Yu3T5iejstE=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
14. `https://play-lh.googleusercontent.com/1KTVasMZEZpgdCooDhb1L81XGVwfQWzMiV-lw0Yz-aMethwHiERgtRabZfL_qNQONHfWUu6aRnqUs5dKD13Plg=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
15. `https://play-lh.googleusercontent.com/mlHw1EYeuwRxmqytJOJHK-awo-Bsot29-rUaTWPsx4bZ-qt7tVzOH-3HWrzudJ0LDvijWZsRmN0pSLMd51RWHQ=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
16. `https://play-lh.googleusercontent.com/HzAJUsU0FT12jd3O8ojACvbHrgQLsWKgREy7zLy7lg_53wz8pcSxRd4DDaH9tRBdtYizuNglsC23ZrBBnD6e=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
17. `https://play-lh.googleusercontent.com/3MqyvMOcLFhKs21WwXGcXKfuJCvTyXEPYk65XayN1biuDRrA0mV-ur9LP0Fr6BVz65jcCYLv10lqptUw0r-Fbw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
18. `https://play-lh.googleusercontent.com/zch8Ej8I06RJvHv9WBz8JeZYppkfxY-6ilBvYMlgG542kjqWzYfYb5IoDMFbkyDPFKIDveDZP6cp-CdJS__znCU=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
19. `https://play-lh.googleusercontent.com/F6iyUl_VUu2750o_S0azaxZF2B-er2p2cuF8rIdduT0mkQfXvQ5wNQsYGCRfalHSgdsu-3fduzCbg70WFIT3Xw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
20. `https://play-lh.googleusercontent.com/3wD-_bDOwy1DKi1t1kV_YSPX4VbMkOM1OsnKC2EE_1dsIswKVYDTWqkTp5mLRba5sw6-h9n4cJjNNlS5fKntQw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
21. `https://play-lh.googleusercontent.com/Git6SsoIxbLP80JjxU-vDZRUWT8m7AWfKDZj97zn5BXJ_N59Uae6Jv1RgFoXILQ_7-zne8GuoIiNPZNdiR0Zdw=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
22. `https://play-lh.googleusercontent.com/p8RqYbUMuBC9zE00JJOHvaUve4l0x3FlP0AuzV6xD4CdG1w-tu5L46XDoJRPPdXeEbVZ95MnjRkKxD1Wr7qwoQ=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
23. `https://play-lh.googleusercontent.com/OR7NRBrBLI3FkmlQOrKcZ3qZWjvl8lz26WSPnYNnPHAz3zvunpZWxkQYmoUBl3z453aFibmQzBZfaocm6OxI=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.
24. `https://play-lh.googleusercontent.com/kKbi-9I70rkHHpSnlD2T6UIas-5VD10niN36mi5v3WCv7_J8j8TQPLbGSzXkwFmk07fwhdpt2hW5NwmhrFOIyWU=w526-h296-rw` — Discovered-not-yet-visited; exact URL queued in frontier.

## Other T114 sources

- `https://www.instagram.com/firsttouchgames_official`: HTTP 403/no payload; profile identity and contents remain unverified; no retry.
- `https://www.ftgames.com/about`: successful FTG corporate About page, broad studio context only; no Cult Heroes route/rewards or DLS26 position-lock statement.

## Recovery and closeout

T114 opened on reset `fb9a2c0`; 308 non-ignored files were archived to `/tmp/dls26-t114-recovery-20261006063654.tar.gz` (SHA-256 `152081a062bd91e433ea45c71036a2d4508c3f8fa5a2edcedaefc10a841cebb3`, 308 members), then `70878db`, upstream, and repo-local identity were restored. No files discarded. A first closeout helper stopped on a local `NameError` after updating the source ledger but before writing other closeout files; the persisted ledger was validated and closeout resumed without rerunning research.

Ledger: **726 entries / 544 visited URLs / 418 unvisited leads**. Cult Heroes route/rewards and position-lock remain unresolved; position locking remains `user-stated` and unverified. No absence inference or exhaustion declaration.
