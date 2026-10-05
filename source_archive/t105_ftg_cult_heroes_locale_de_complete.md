# T105 — FTG `Cult Heroes` Help Center `locale=de` query complete

Date: 2026-10-06 Asia/Dhaka. The exact search began in T104 at `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes&locale=de`. T104 completed page 1 chunks 0–5/6. T105 followed the API pagination URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?locale=de&page=2&per_page=25&query=Cult+Heroes` (page 2/3, chunks 0–4/5) and its returned `next_page` `https://support.ftgames.com/api/v2/help_center/articles/search.json?locale=de&page=3&per_page=25&query=Cult+Heroes` (page 3/3, chunk 0/1). All six T105 fetches returned `status=success`; HTTP status codes are not exposed. Page 3 reports `next_page=null` and `hasMore=false`.

## Full-query boundary and outcome

The API reports `count=52`, `page_count=3`, `per_page=25`; all pages are now read (25 + 25 + 2 results). The query is fuzzy: page 1 and page 2 are dominated by unrelated Score! Hero/8 Ball Hero help; the final two page-3 results are generic account/privacy help (one includes DLS account-deletion navigation and one DLS iCloud setup). Result records show `locale=en-us` despite the request's `locale=de` parameter.

No DLS26 Cult Heroes availability, acquisition route, cost, or reward information surfaced in this completed exact search. This is bounded to the search result set and does not prove absence elsewhere. Do not treat generic account help or other-product results as event evidence.

## Recovery and ledger

T105 opened on reset `fb9a2c0`; clock recorded first (`2026-10-06 05:53:30 +06`). Archived 290 files to `/tmp/dls26-t105-recovery-20261006055333.tar.gz`, SHA-256 `e51e4f0d7fd468a305d69bd5a8f5fa6e0d0f1c7ea7b6d96a2a73880efd06a9d1`; fetched/restored session tip `94465d0`, upstream, and repo-local identity. After overlay, only the T105 clock-start append differed. ISSUE-0014 recovery occurrence #67; no loss/force-push.

T105 used six retrievals (page2 chunks 0–4 and page3 chunk0). Ledger: **708 entries / 526 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes route/rewards remain unresolved; no spending advice, dimension closure, or exhaustion declaration.
