# Turn 82 — FTG Help Center searches for Cult Hero Agents and Drafts

## Recovery integrity
At opening the branch had reset to `fb9a2c0`, upstream unset, and 242 project files untracked. Archived them to `/tmp/dls26-t82-recovery-y0OoeQ/workspace.tar.gz` (SHA-256 `3ff04d44c40b0b1cce347fec9e48191a63dd7e2f4e35dfc241ee3d5bc6eb32f1`). Restored `origin/arena/01a1022d-dls26-omega` at `7b9e5c3`; all 242 files byte-matched after excluding only the T82 clock-start line. ISSUE-0014 #44 logged; upstream and repo-local identity restored. No force-push.

## Search 1: `Cult Hero Agent`
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Hero%20Agent`
- `functions.fetch_page` chunk 0 returned `status=success`; numeric HTTP status not exposed. API count 1, page 1/1, one chunk.
- Result: [How do I obtain more players?](https://support.ftgames.com/hc/en-us/articles/360004066417-How-do-I-obtain-more-players), article 360004066417, updated 2026-09-19. The returned body describes generic transfers, scouts, agents (“immediately add a player”), and Prize Ladder. It does not mention Cult Hero Agents, the Cult Heroes event, event-specific availability, or a guaranteed Special Card. Do not transfer generic-agent mechanics to Cult Hero Agents.

## Search 2: `Drafts Season Pass`
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Drafts%20Season%20Pass`
- API count 12, page 1/1, 4 rendered chunks. All chunks 0–3 were read in this turn; every fetch returned `status=success` (numeric HTTP status not exposed).
- Results included general DLS Season Pass documentation (including a version-12200-onwards article), “How do I get new players?” (generic packages/shop/Season Pass), Prize Ladder, Dream Point/Season Point material and some Ultimate Clash Soccer documentation. No result provided Cult Heroes/Cult Hero Agent event-route or event-reward instructions. This is a completed query with no answer, not proof of absence.

## Search 3: `Drafts`
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Drafts`
- One chunk, three results; fetch returned `status=success` (numeric HTTP status not exposed). The DLS result [What are Dream Point Boosts?](https://support.ftgames.com/hc/en-us/articles/24081168829330-What-are-Dream-Point-Boosts) says boosts can apply to Dream Draft matches. The other results are Ultimate Clash Soccer help. Nothing describes Cult Hero Agent acquisition or rewards.

## T81 audit correction
T81 used six retrieval calls, but a validation assertion aborted the first data-write attempt; a separate inspection call preceded the successful retry, bringing the turn to 11 total tool calls (one over the 10-call cap). The failed script made no source-artifact writes. Ledger inspection also showed the Facebook page URL was already recorded before T81; the T81 HTTP-403 fetch was a repeat, and only the new TikTok candidate increased the unique-URL count. The repeat is logged; no content or absence inference.

## Status
These FTG support results provide generic DLS mechanics only and do not verify the TikTok snippets. Cult Heroes route/rewards remain unresolved. DLS26 position-lock behavior remains unverified; the user-stated “no position locking” stays user-stated. No spending recommendation, scope closure, or exhaustion declaration.
