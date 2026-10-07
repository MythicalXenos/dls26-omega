# Turn 86 — FTG `Special Players Events` search (partial)

## Recovery
Opening reset to `fb9a2c0`, upstream unset, 250 project files untracked. Archived all 250 at `/tmp/dls26-t86-recovery-XrWHwC/workspace.tar.gz`, SHA-256 `0ddd81813e675ffe9ae21ae3500707bd86d1e7de8074e5add0075b94cce9a81b`; restored `origin/arena/01a1022d-dls26-omega` at `87421b0`; byte-verified all 250 after excluding only the T86 clock-start line. ISSUE-0014 #48 logged; upstream and repo-local identity restored. No force-push.

## New FTG Help Center query
- Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Special%20Players%20Events`
- `functions.fetch_page` chunk 0 returned `status=success`; numeric HTTP status not exposed. API reports 10 results, one page, 8 rendered chunks. Only chunk 0 was read; chunks 1–7 remain pending. Resume at `functions.fetch_page` chunkIndex 1.
- Visible first result cards include [Why are some players displaying a different player card colour?](https://support.ftgames.com/hc/en-us/articles/214385645-Why-are-some-players-displaying-a-different-player-card-colour), [How do I obtain more players?](https://support.ftgames.com/hc/en-us/articles/360004066417-How-do-I-obtain-more-players), [What is the Prize Ladder?](https://support.ftgames.com/hc/en-us/articles/23108987826962-What-is-the-Prize-Ladder), and generic DLS player-stat help. These generic card-colour/Agents/Prize Ladder results do not establish anything about the Cult Heroes event.
- Because chunks 1–7 are unread, this search is not complete and supports no absence conclusion.

## Status
Cult Heroes route/rewards remain unresolved. DLS26 position-lock remains unverified; user-stated “no position locking” is unchanged. No spending recommendation, scope closure, or exhaustion declaration.
