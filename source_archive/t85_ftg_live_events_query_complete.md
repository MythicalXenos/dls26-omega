# Turn 85 — FTG `live events` query completed

## Recovery integrity
Opening reset to `fb9a2c0`, upstream unset, 248 project files untracked. Archived all 248 at `/tmp/dls26-t85-recovery-t2Upcd/workspace.tar.gz`, SHA-256 `4fbf512939db4eb29b4b64dba684ffd35730a37f3e4c6a8e0e400194006be663`; restored `origin/arena/01a1022d-dls26-omega` at `2826f8a`; byte-verified all 248 after excluding only the T85 clock-start line. ISSUE-0014 #47 logged; upstream and repo-local identity restored. No force-push.

## Complete response
- Exact API URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=live%20events`
- API reports 18 results on page 1/1, rendered across 10 chunks. T83 read chunk 0, T84 read chunks 1–6, and T85 read chunks 7–9. All three T85 calls returned `status=success`; numeric HTTP status is not exposed. Chunk 9 reports `hasMore=false`.
- Chunks 7–9 finish generic DLS player-stat material and include older DLS account/support entries plus a Score! Match Facebook-login result. The full mixed-product set includes the generic “What are Events?” and “What are Super Players?” DLS articles. “Super Players” text says enhanced players can be won in Events and occasionally rarer packages; no response links Cult Heroes/Cult Hero Agents to that category.
- No result specifically explains Cult Heroes/Cult Hero Agents acquisition, route, cost, or reward. This only describes the returned search result set; do not infer absence of unindexed content or in-game evidence.

## Status
Cult Heroes route/rewards remain unresolved. DLS26 position locking remains unverified; user-stated “no position locking” is unchanged. No spending recommendation, dimension closure, or exhaustion declaration.
