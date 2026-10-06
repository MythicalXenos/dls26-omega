# T137 — FTG `change formation` page completion and page-2 probe

Date: 2026-10-06 Asia/Dhaka. Two retrieval calls. Per-fetch timestamps not exposed.

## Page 1, exact query `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=change%20formation`

Fetched chunkIndex=2, `status=success`, retrying the T136 call whose response/status was not visible. Combined with prior chunks 0,1,3,4,5,6, page 1 (7/7 chunks) is now complete. The returned chunk overlaps general graphics-settings help; no DLS26 squad position edit/lock rule. The DLS Running-behaviour excerpt documented in T136 remains an in-match movement statement, not a lock mechanic.

## Page 2, exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=change+formation`

`functions.fetch_page` chunkIndex=0 returned `status=success`; API reports count=48, page=2/2, page_count=2, totalChunks=15, `hasMore=true`. Only chunk 0/15 was read. Visible results include Score! Match article 360000250309 (section 115001619089) and “What are the rules of Ultimate Clash Soccer?” article 7918507871505 (section 7900693036561). The latter’s returned rules describe position following formation and ball position for Ultimate Clash Soccer. Do not transfer any of this to DLS26. Chunks 1–14 are unread; the long, cross-title page is retained as a low-priority frontier item. No query-wide absence conclusion.

## Recovery

T137 began on reset checkout `fb9a2c0`; clock was recorded first. Archived 359 files at `/tmp/dls26-t137-recovery-20261006084542.tar.gz`, SHA-256 `b041ab7c77fe0da05bfe641c2a4ba3159c4a4d9e87412ea73b737243690a6314`; fetched/restored pushed tip `7bb069a`, restored upstream and repo-local identity, and byte-verified all 359 files. ISSUE-0014 occurrence #99.
