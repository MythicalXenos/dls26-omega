# T104 — FTG `Cult Heroes` Help Center search with `locale=de` (partial)

Date: 2026-10-06 Asia/Dhaka. Exact page-1 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes&locale=de`. Retrieval tool: `functions.fetch_page`; chunks 0–5/6 all returned `status=success`. HTTP status code is not exposed. API metadata: `count=52`, `page=1`, `page_count=3`, `per_page=25`; page 1 is complete, pages 2–3 remain unread. The returned `next_page` is exactly `https://support.ftgames.com/api/v2/help_center/articles/search.json?locale=de&page=2&per_page=25&query=Cult+Heroes`.

## Bounded observation

The visible page-1 results begin with generic Score! Hero and 8 Ball Hero support articles; article metadata in the response says `en-us` even though the request supplied `locale=de`. No DLS26 Cult Heroes availability, acquisition route, cost, or reward information surfaced in this page. This is a fuzzy, incomplete search; do not infer absence, assume the locale filter worked, or treat unrelated product results as DLS26 evidence.

## Recovery and ledger

T104 opened on reset `fb9a2c0`; clock recorded first (`2026-10-06 05:49:27 +06`). Archived 288 files to `/tmp/dls26-t104-recovery-20261006054929.tar.gz`, SHA-256 `b5d28b61c8b99a993004907adc201da6df3fc2e813b07c9e945c31aa24e6c17a`; fetched/restored session tip `d91624c`, upstream, and repo-local identity. After overlay, only T104 clock-start append differed. ISSUE-0014 recovery occurrence #66; no loss/force-push.

Six retrievals were used (chunks 0–5). Ledger: **706 entries / 524 unique visited URLs / 406 unvisited leads**. The page-2 `next_page` URL is retained for continuation. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes route/rewards remain unresolved; no spending advice, dimension closure, or exhaustion declaration.
