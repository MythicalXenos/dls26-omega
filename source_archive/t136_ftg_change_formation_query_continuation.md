# T136 — FTG `change formation` query continuation

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls requested page-1 chunkIndex 1 through 6 of the exact query `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=change%20formation`. Per-fetch timestamps are not exposed.

## Response coverage and interpretation

The exact query reports 48 results over 2 API pages; page 1 is rendered in 7 chunks. T135 had fetched chunk 0. In T136, the session output visibly returned `status=success` and explicit `chunkIndex` values 1, 3, 4, 5, and 6. Chunk 2 was among the six requested calls, but no result object or status is visible in the session output. Do not label it successful or failed; keep it pending for a single retry. The page-2 endpoint `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=change+formation` has not been fetched.

The visible results are mixed FTG help material. They include DLS help about manager/profile/kit changes and other product sections; the “change formation” and “change player roles” articles in section 7900693036561 are already mapped in the local taxonomy as non-DLS, and Score! Match formation/stat articles are not transferable to DLS26.

One DLS player-stats/behaviour article excerpt returned in the query states: “Players with this behaviour attribute will actively make runs into attacking positions or to find space. Players without this behaviour will stay more closely to their formation position.” In context this is the `Running` behaviour and in-match movement relative to formation position. It does not establish whether a user can assign a player to a different squad position or lock that position, and the article is not version-stamped DLS26. Preserve this as narrow first-party context only; no absence inference.

## Recovery

T136 began on reset checkout `fb9a2c0`; clock was recorded first. Archived 357 files at `/tmp/dls26-t136-recovery-20261006084055.tar.gz`, SHA-256 `1722e2a0a96d60c699f143b948365c7857657434a5fa148b5a42902df0ef38b6`; fetched/restored pushed tip `85c38d4`, restored upstream and repo-local identity, and byte-verified all 357 files. ISSUE-0014 occurrence #98.
