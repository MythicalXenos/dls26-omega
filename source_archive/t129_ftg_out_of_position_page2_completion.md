# T129 — FTG “out of position” query completion and X search attempt

Date: 2026-10-06 Asia/Dhaka. Five retrieval calls: FTG Help Center page-2 chunks 1–4 (parallel) and one direct X search URL.

## FTG Help Center query completion

Exact page-2 URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=out+of+position`. T112 had read chunk 0/5; T129 retrieved chunks 1, 2, 3, and 4. All four returned `status=success`; numeric HTTP status is not exposed. Page 1 had already been completed across T110–T112. This closes the exact two-page query.

Page-2 chunks show mixed FTG material, including DLS19 kit/logo customization, player appearance, DLS25 profile transfer, generic save/account/friend-match topics, and Score! Match/Score! Hero articles. The search matches are not DLS26 squad-position-lock instructions. No explicit DLS26 lock rule surfaced in the fetched results; this is not proof of absence and no conclusion is drawn about current game behavior. The T112 continuation lead is closed.

## Direct X search

Requested `https://x.com/search?q=from%3Afirsttouchgames%20%22Cult%20Heroes%22&src=typed_query` with `functions.fetch_page`. It returned HTTP 403 and no page body. Do not retry this exact URL and do not infer that no post exists. No post content was assessed.

## Recovery

T129 began on reset `fb9a2c0`; clock was recorded first. Archived 341 files at `/tmp/dls26-t129-recovery-20261006020329.tar.gz`, SHA-256 `b58a8587c6be8d0b5a7845ac62b8327633b2cece482012f6c6f39aa98a86a114`; fetched/restored the fixed branch at `4937e60`, upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`, and byte-verified all archived files. ISSUE-0014 occurrence #91; no content loss.
