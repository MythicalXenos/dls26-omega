# T133 — FTG lineup and Agent-rewards Help Center searches

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls total: `lineup` chunks 0–2 (complete) and `Agent rewards` chunks 0–2 (partial). Per-call timestamps not exposed.

## `lineup` query — complete

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=lineup`. API reports count=9, page_count=1, rendered across 3 chunks. All chunks 0–2 returned `status=success`. One DLS article, “How do I change between Home and Away kits before a match?”, says the pre-match screen displays both team lineups and allows kit cycling. Other results include generic/other-product account, graphics and help material. Nothing describes formation editing, position locking, or out-of-position penalties. This does not establish absence.

## `Agent rewards` query — partial

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Agent%20rewards`. API reports count=18, page_count=1, rendered across 10 chunks. T133 retrieved chunks 0–2/10 only; all returned `status=success`. Visible hits are generic/repeated FAQs (including “How do I obtain more players?”, Season Pass, coins, Prize Ladder and clan material) and other product content. No Cult Heroes-specific route, Agent guarantee, cost, or reward is visible in these chunks. **Do not infer absence from a partial result.** Resume at chunkIndex=3; chunks 3–9 remain. The continuation is retained in the source frontier and active queue.

## Interpretation and recovery

No new DLS26 position-lock behavior or Cult Heroes route/reward fact established. User-stated position-lock status remains unverified.

T133 began on reset `fb9a2c0`; clock was recorded first. Archived 352 files at `/tmp/dls26-t133-recovery-20261006022134.tar.gz`, SHA-256 `16f305ca5aaf34d2c9ea1a294397c3d0b2b9fed1808dbc65ad9fb40b05c72226`; restored fixed branch `3938397`, upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`, and byte-verified all files. ISSUE-0014 occurrence #95; no content loss.


## T134 continuation — chunks 3–8

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls were used for requested chunkIndex 3, 4, 5, 6, 7, and 8 of the same exact query (`https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Agent%20rewards`). Explicit successful response metadata confirmed chunks 3, 4, 5, 6, and 8; the one remaining call returned HTTP 502/no payload and, by set difference, was chunk 7. Chunk 9 was not requested. The query reports 18 results and 10 rendered chunks.

Chunks 3–6 and 8 returned only general/older DLS Help Center material in the visible excerpts (player-stat article, friend-bonus/ad help, and other generic content). No Cult Heroes-specific route, guarantee, cost, or reward appeared in retrieved content. This is not an absence finding: chunk 7 failed and chunk 9 is unread. Retry only chunk 7 and fetch chunk 9 in T135; do not repeat successful chunks 0–6 or 8.

T134 began on reset checkout `fb9a2c0`. Recovery archive: `/tmp/dls26-t134-recovery-20261006082850.tar.gz`; SHA-256 `68f09c560da531c54f29e566ea034c8cd7767bd25ea164eb5a461d53a168750c`; 354 files were byte-verified against the restored pushed tip `fc33db1`. Upstream and repo-local identity restored; ISSUE-0014 occurrence #96.
