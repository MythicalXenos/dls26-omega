# T144 — Season Pass query, creator forecast, and duplicate screenshot attempt

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls: one accidental repeat of a blocked Play screenshot; one YouTube page; four chunks (0–3/5) of one FTG Help Center query. Per-call timestamps not exposed.

## Creator video (secondary; claims unverified)

Exact URL `https://www.youtube.com/watch?v=vklnY84gMRU`. Page identifies Gam Man Soccer (`@gamman1889`), title “Cult Hero All Season Confirmed: Everything You Need To Know”, uploaded 2026-08-30, duration 2:26. Its Bengali description/transcript promotes season schedule, card, and event details. Transcript claims a Sep 16 start, “one or two free agents” in season one, later pass dates Sep 26 and Oct 6, and nine-day seasons; it also self-corrects Oct 3 to Oct 6, while the listed date intervals are about ten days. These are creator assertions/predictions, not first-party facts. No frames were inspected; no specific route, cost, or reward condition was established. Do not use as current event status or spending guidance.

## FTG Help Center phrase query (partial)

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Season%20Pass`. `functions.fetch_page` chunks 0–3/5 returned success; chunk 4 remains unread and is queued as a continuation, not a new query. API reports 16 results on one page. The visible DLS Season Pass FAQ (article 4404070913169, updated 2026-09-21, states applicability from version 12.200 onward) describes generic free/premium tracks and Season Points; it does not mention Cult Heroes Agents/cards in the returned text. Other results are generic or other FTG titles. In particular “How do I get new players?” id 17146272243473 belongs to section 7900693036561 (Ultimate Clash Soccer); do not transfer it to DLS26. No route/reward inference.

## Screenshot #18 duplicate attempt

T144 accidentally requested the already-retired screenshot #18 URL `https://play-lh.googleusercontent.com/zch8Ej8I06RJvHv9WBz8JeZYppkfxY-6ilBvYMlgG542kjqWzYfYb5IoDMFbkyDPFKIDveDZP6cp-CdJS__znCU=w526-h296-rw` again. It again returned HTTP 500 with no bytes/image. This is logged on the T143 source record’s attempt history; it is not a new source/URL and must not be retried.

## Recovery

T144 began on reset checkout `fb9a2c0`; clock was recorded first. Archived and byte-verified 373 working files at `/tmp/dls26-t144-recovery-20261006121817.tar.gz`, SHA-256 `d43d7c53552dfa49969c326dd8dd0144efeb7b3f45691302d5838e854288b0ac`; fetched/restored pushed tip `166c29e`, restored upstream and repo-local identity, and retained safety stash `1054d51`. ISSUE-0014 occurrence #106.

Ledger: 804 records / 607 unique visited URLs / 398 unvisited leads. Cult Heroes route/rewards and DLS26 position-lock remain open.
