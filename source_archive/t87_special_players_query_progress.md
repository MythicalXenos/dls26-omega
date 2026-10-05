# Turn 87 — `Special Players Events` query progress

## Recovery integrity
Opening reset to `fb9a2c0`, upstream unset, and 252 project files untracked. Archived all 252 at `/tmp/dls26-t87-recovery-ZMLy8r/workspace.tar.gz`, SHA-256 `00e7bd6bbcb44bb077d6bdbdc18962779c2057f4f639816bce8af1dcd7aa0561`; restored `origin/arena/01a1022d-dls26-omega` at `6102fa1`; byte-verified all 252 after excluding only the T87 clock-start line. ISSUE-0014 #49 records this; upstream and repo-local identity restored.

## Continue the exact FTG query
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Special%20Players%20Events`
- T86 read chunk 0; T87 read chunks 1–6. All T87 calls returned `status=success`; numeric HTTP status is not exposed. The API reports 10 results on page 1/1 across 8 rendered chunks. Chunk 7 remains unread; resume at `functions.fetch_page` chunkIndex 7.
- Chunks 1–6 mostly continue the DLS stats article and include generic DLS Super Players help, age confirmation, player sale/type, an older DLS19 customization article, and Score! Match material. The generic Super Players article does not identify Cult Heroes as that type or state a Cult Hero Agent route/reward.
- This is still a partial mixed-product response. No absence conclusion until chunk 7 is read; even a complete query cannot prove absence outside this result set.

## Status
Cult Heroes route/rewards remain unresolved. DLS26 position lock remains unverified; user-stated “no position locking” is unchanged. No spending recommendation, scope closure, or exhaustion declaration.
