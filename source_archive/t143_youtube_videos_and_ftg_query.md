# T143 — creator-video spot checks, FTG query, and screenshot failure

Date: 2026-10-06 Asia/Dhaka. Five new exact retrieval targets were attempted; per-call timestamps not exposed.

## Secondary YouTube pages

1. `https://www.youtube.com/watch?v=RrUBfS1aeRM` — YouTube page identifies uploader F T G HD BRO (`@MarifulIslam-xj5le`), title “DLS 26 CULT HEROES TOURNAMENT CHAMPION WITH MBAPPE. I GOT DYBALA”, upload date 2026-10-03, duration 13:56. The creator description claims a tournament win and getting Dybala. The returned transcript is mostly music/match commentary and contains no Agent opening or acquisition mechanics. No frames were inspected; treat title/description as unverified creator assertions, not route/reward evidence.
2. `https://www.youtube.com/watch?v=bI6nEX5hjBg` — uploader CHIGOOD, title “DLS 26 CULT HEROES TOURNAMENT CHAMPIONS WITH YAMAL - DLS CULT HEROES”, upload date 2026-10-02, duration 11:34. Its description claims a Cult Heroes Tournament play-through; transcript contains match commentary and generic “special event”/“strict objectives” phrases, but no reward screen or acquisition route. No frames were inspected. Secondary only.

## Media attempts

- Official Google Play screenshot #18 exact URL `https://play-lh.googleusercontent.com/zch8Ej8I06RJvHv9WBz8JeZYppkfxY-6ilBvYMlgG542kjqWzYfYb5IoDMFbkyDPFKIDveDZP6cp-CdJS__znCU=w526-h296-rw` returned HTTP 500 via `functions.fetch_page`; no image bytes/content. Retire this exact URL; do not retry. #19–24 remain uninspected.
- RrUB YouTube thumbnail exact URL `https://i.ytimg.com/vi_webp/RrUBfS1aeRM/maxresdefault.webp` returned HTTP 500; no image. Do not retry. The CHIGOOD page exposed thumbnail `https://i.ytimg.com/vi_webp/bI6nEX5hjBg/maxresdefault.webp`, not fetched; retained as a low-priority lead only, not as game evidence.

## FTG Help Center

Exact query URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Tournament` returned count=0/page_count=0/results=[]. This exact phrase only; no global absence inference.

## Recovery

T143 began on reset checkout `fb9a2c0`; clock was recorded first. Archived and byte-verified 371 working files at `/tmp/dls26-t143-recovery-20261006091855.tar.gz`, SHA-256 `3b231f6c16036a9d9ba57de6839349cb893a586b0d60de9928001ffbd2a3ce8f`; fetched/restored pushed tip `51fc3fd`, restored upstream and repo-local identity, and retained safety stash `d55a46d`. ISSUE-0014 occurrence #105.

No Cult Heroes route/reward or DLS26 position-lock fact established.
