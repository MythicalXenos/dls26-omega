# Turn 83 — FTG Events help and Apple storefront event detail

## Reset recovery
At opening: branch reset to `fb9a2c0`, upstream unset, 244 project files untracked. Archived all 244 at `/tmp/dls26-t83-recovery-u0e1JL/workspace.tar.gz`, SHA-256 `7bc7ce8a6206570dc10f08fa18b6f49967b850ea8807862bcfb98c0d338885a2`; restored `origin/arena/01a1022d-dls26-omega` at `3849c5d`; byte-verified all 244 after excluding only the T83 clock-start line. ISSUE-0014 #45 logged, identity/upstream restored, no force-push.

## FTG Help Center “live events” query (partial)
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=live%20events`
- Chunk 0 returned success; API reports 18 results on page 1/1 across 10 rendered chunks. Only chunk 0 was read; chunks 1–9 are pending. Do not classify the full query or infer absence.
- The first result was [What are Events?](https://support.ftgames.com/hc/en-us/articles/214386765-What-are-Events). Direct fetch returned success. It says FTG may offer permanent or time-based events in the in-game “Events” section, playable alongside the main story. This is generic event navigation and does not identify Cult Heroes or its route/reward.
- Resume the exact API URL at `functions.fetch_page` chunkIndex 1 (chunks 1–9 unread).

## Position terminology search
`functions.web_search` query `site:support.ftgames.com/hc/en-us/articles "out of position" "Dream League Soccer"` returned five generic/older DLS Help Center cards; none of the snippets addressed positional assignment or locking. These were search cards only, and nonappearance is not evidence of absence. DLS26 behavior remains unverified.

## Apple App Store U.S. listing and event page
- Search: `site:apps.apple.com "Cult Heroes" "Dream League Soccer 2026"` returned U.S., GW, and TN App Store listing cards. The U.S. DLS26 listing was fetched directly: `https://apps.apple.com/us/app/dream-league-soccer-2026/id1462911602`. It labels the developer First Touch Games Ltd. and shows an Events section with “HAPPENING NOW” and a “LIVE EVENT Cult Heroes” card.
- Direct event detail: `https://apps.apple.com/us/app/dream-league-soccer-2026/id1462911602?eventid=6802988564`; fetched successfully, title “Cult Heroes,” labels HAPPENING NOW / LIVE EVENT, description: “Sign these top stars who are remembered by passionate football fans. Now available with boosted attributes.”
- This establishes what the Apple storefront currently displays, not that a particular user can access the event in-game. It does not state the in-game route, cost/currency, names, or exact rewards. Treat as the same event/localization family as prior App Store copy, not independent corroboration; do not use it to override the user’s explicit correction about store text.

## Current status
Cult Heroes route/rewards remain unresolved; no spend recommendation. User-stated DLS26 “no position locking” remains unverified; device setup remains needed. No scope closure or exhaustion declaration.
