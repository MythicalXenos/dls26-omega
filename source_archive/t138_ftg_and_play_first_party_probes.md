# T138 — distinct FTG queries and Play asset attempts

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls total: two FTG Help Center chunk-0 requests and four distinct Play asset GETs. Per-fetch timestamps are not exposed.

## FTG Help Center

1. Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Agents%20event`: `functions.fetch_page`, chunk 0, `status=success`; count=0, page_count=0, results=[]. Phrase-specific only; no global absence or route/availability conclusion.
2. Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=assign%20player%20position`: `functions.fetch_page`, chunk 0, `status=success`; count=9, page_count=1, totalChunks=9. Only chunk 0 was read. Visible initial results include Score! Match Captain-player-type article 360000002345 (section 115001619089) and Ultimate Clash Soccer rules article 7918507871505 (section 7900693036561). These are not DLS26 evidence. Chunks 1–8 unread; do not infer absence from this partial query or transfer cross-title mechanics.

## Official Google Play asset attempts

Each of the following distinct T114 screenshot URLs was attempted once with `curl -L --max-time 30 --silent --show-error`; each returned curl exit 35 (`OpenSSL SSL_ERROR_SYSCALL`), HTTP `000`, 0 bytes. No image was saved or inspected; do not retry or infer contents.

- #13 `https://play-lh.googleusercontent.com/aEh1y9_WcQ_lh4_WpvCdaC6aqbRj1IhTkAXUoIxMtEkdzPLPmWRAAD9dMmnn0jSxXPbRhqfATsW4Yu3T5iejstE=w526-h296-rw`
- #14 `https://play-lh.googleusercontent.com/1KTVasMZEZpgdCooDhb1L81XGVwfQWzMiV-lw0Yz-aMethwHiERgtRabZfL_qNQONHfWUu6aRnqUs5dKD13Plg=w526-h296-rw`
- #15 `https://play-lh.googleusercontent.com/mlHw1EYeuwRxmqytJOJHK-awo-Bsot29-rUaTWPsx4bZ-qt7tVzOH-3HWrzudJ0LDvijWZsRmN0pSLMd51RWHQ=w526-h296-rw`
- #16 `https://play-lh.googleusercontent.com/HzAJUsU0FT12jd3O8ojACvbHrgQLsWKgREy7zLy7lg_53wz8pcSxRd4DDaH9tRBdtYizuNglsC23ZrBBnD6e=w526-h296-rw`

URLs #17–24 remain untried. This is a record of transport failures, not evidence about the images or event.

## Recovery

T138 began on reset checkout `fb9a2c0`; clock was recorded first. Archived 361 files at `/tmp/dls26-t138-recovery-20261006084949.tar.gz`, SHA-256 `85fd6d22989a409224f41ea07ef7f1cb4f3db023a391ed11d26adbaa67618715`; fetched/restored pushed tip `c1ed75b`, restored upstream and repo-local identity, and byte-verified all 361 files. ISSUE-0014 occurrence #100.
