# Turn 84 — FTG `live events` query progress

## Reset recovery
Opening again found branch `fb9a2c0`, upstream unset, and 246 project files untracked. Archived all 246 to `/tmp/dls26-t84-recovery-GnTLXq/workspace.tar.gz`, SHA-256 `d414bc2903f9775287395997b79fa9d0514dd6f7e73d9de10bf02194e3dfb50e`; restored `origin/arena/01a1022d-dls26-omega` at `ac8641f`; byte-verified all 246 after excluding only the T84 clock-start line. ISSUE-0014 #46 records this; upstream and repo-local identity restored.

## Continue the exact FTG query
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=live%20events`
- T83 read chunk 0; T84 read chunks 1–6. Each returned `status=success`; numeric HTTP status is not exposed. API reports 18 results on page 1/1 across 10 rendered chunks. Chunks 7–9 remain unread; resume at `functions.fetch_page` chunkIndex 7.
- Chunk 1 includes [What are Super Players?](https://support.ftgames.com/hc/en-us/articles/360017063617-What-are-Super-Players), article 360017063617: “Super Players are enhanced player types which can be won in Events and occasionally in the rarer packages.” This is generic DLS help. Nothing in the result says Cult Heroes are Super Players or that Cult Hero Agents come from those routes; do not conflate card categories.
- The rest of visible chunks 1–6 includes general Dream League Live, currency, Dream Point Boosts and player-stat material (including a previously encountered DLS stats article), with some unrelated results. The visible partial response establishes no Cult Heroes-specific route/reward and is not an absence conclusion.

## T83 duplicate-URL audit correction
Post-fetch URL comparison showed all three T83 direct pages (`What are Events?`, U.S. App Store listing, and eventid `6802988564`) were already present in the ledger. Their T83 fetches were repeats; the unique URL counter correctly stayed at 510. Treat the App Store wording as the same localized event family as T63, not independent corroboration.

## Current status
Cult Heroes acquisition route/rewards remain unresolved. The Apple page is storefront metadata, not proof of account-level in-game access. DLS26 position-lock behavior remains unverified; user-stated “no position locking” is unchanged. No spending recommendation, scope closure, or exhaustion declaration.
