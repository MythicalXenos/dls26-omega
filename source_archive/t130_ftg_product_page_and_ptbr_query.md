# T130 — DLS-specific FTG page paths and Portuguese Help Center query

Date: 2026-10-06 Asia/Dhaka. Three distinct first-party requests; per-call timestamps not exposed.

## FTG product-page paths

1. `functions.fetch_page` requested `https://www.ftgames.com/games/dls`. It returned a 404 page: Code `NoSuchKey`, Message `The specified key does not exist`, Key `release/games/dls`. No game content returned.
2. `functions.fetch_page` requested `https://www.firsttouchgames.com/games/dls`. It returned the same 404/NoSuchKey key path. No game content returned.

These exact paths do not establish that no other FTG/DLS pages exist; do not infer global absence.

## Brazilian Portuguese FTG Help Center search

Requested `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Agentes%20Her%C3%B3is%20Cultos&locale=pt-br`. The exact query returned `count=0`, `page_count=0`, `results=[]`, tool status `success`. This records only that localized query response; it does not establish game/event absence. No article or mechanics text was returned.

## Interpretation and recovery

No route, reward, cost, current availability, or position-lock evidence was found. Cult Heroes acquisition details and DLS26 position behavior remain open; no exhaustion declaration.

T130 began at reset `fb9a2c0`; clock was recorded first. Archived 343 files at `/tmp/dls26-t130-recovery-20261006020936.tar.gz`, SHA-256 `b94b10e35d484918874f490f52b7c84d94aa8198ec32f7ef15c7fd0c350f7715`; restored the fixed branch at `dd2c801`, upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`, and verified all archived files. ISSUE-0014 occurrence #92; no content loss.
