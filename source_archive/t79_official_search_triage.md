# Turn 79 — FTG follow-up search reconciliation

## Recovery integrity
At opening the session again had `fb9a2c0` plus 236 project files untracked, and no upstream. All 236 files were archived to `/tmp/dls26-t79-recovery-2hqnGn/workspace.tar.gz` (SHA-256 `c275d5bc9bc30928152c0e5bdadcece68b72eaceb4215f01e269d62539d8ccb4`). Remote branch `arena/01a1022d-dls26-omega` was restored at `a51eed8`; all 236 archived files byte-matched the restored tip after excluding only the T79 opening-marker line. Upstream and repo-local identity were restored; no force-push. ISSUE-0014 occurrence #41 records this.

## Completed FTG Help Center API query
- Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=formation%20position`
- `functions.fetch_page`: chunks 6, 7, and 8, each `status=success`; numeric HTTP status is not exposed. Together with T78 chunks 0–5, the complete response reports 14 results, page 1/1, across 9 rendered chunks.
- Chunks 6–7 complete DLS player-stat explanatory content; chunk 8 contains a Score! Match Facebook-login result. The full result set is mixed across Score! Match, Ultimate Clash Soccer, and DLS FAQs/stats. No DLS26 squad formation-position-lock behavior is established. Do not transfer other-game formation behavior to DLS26, and do not treat this completed query as proof of absence.

## First-party-oriented discovery searches (result cards only)
All tool calls returned `status=success`; `functions.web_search` does not expose an HTTP status or its request URL. No result page was fetched. Search cards are discovery output, not evidence from the underlying pages. No actionable new lead was retained because returned items were general/old or off-topic; the result cards and URLs are recorded here for provenance.

1. Query `site:ftgames.com "Cult Heroes" "Dream League Soccer"` (depth 2; 5 cards):
   - [FTG games](https://www.ftgames.com/games) — general game overview, no event route/rewards in the returned description.
   - [DLS19 save transfer](https://support.ftgames.com/hc/en-us/articles/214387685-How-do-I-backup-restore-transfer-my-save-data) — old-game account help.
   - [How can I get Gems?](https://support.ftgames.com/hc/en-us/articles/360003914938-How-can-I-get-Gems) — generic currency help, not Cult Heroes-specific.
   - [DLS Classic download](https://support.ftgames.com/hc/en-us/articles/214387905-Why-can-t-I-download-Dream-League-Soccer-Classic) and [blocked-play policy](https://support.ftgames.com/hc/en-us/articles/360008904718-Why-have-I-been-blocked-from-playing-DLS) — unrelated to the DLS26 event.
   - No DLS26 Cult Heroes availability, acquisition route, cost, or reward was established.

2. Query `site:support.ftgames.com/hc/en-us/articles/ "Dream League Soccer" formation players position DLS26` (depth 2; 5 cards):
   - [Player development](https://support.ftgames.com/hc/en-us/articles/360003914778-How-do-I-develop-my-players), [multiplayer troubleshooting](https://support.ftgames.com/hc/en-us/articles/360004222118-Multiplayer-Troubleshooting), [graphics settings](https://support.ftgames.com/hc/en-us/articles/360000598437-How-can-I-change-my-graphics-settings), [blocked-play policy](https://support.ftgames.com/hc/en-us/articles/360008904718-Why-have-I-been-blocked-from-playing-DLS), and [Google Play Games setup](https://support.ftgames.com/hc/en-us/articles/360000603398-How-do-I-setup-a-Google-Play-Games-account). Returned snippets were generic/older; no position-lock rule.

3. Query `site:x.com/FirstTouchGames "Cult Heroes" "Dream League Soccer"` (depth 3; 9 cards):
   - Returned official-account posts linked to older releases/support, including DLS 2016 and DLS 2017: [2016 release](https://x.com/firsttouchgames/status/702839782536306689), [2017 release](https://x.com/firsttouchgames/status/842378261799829513), plus older support, anniversary, Score! Hero, DLS 2023, licensing, and DLS 24 posts (2017–2023). No DLS26 Cult Heroes result card appeared. Search/X indexing is limited; nonappearance is not evidence of absence.

## Status
DLS26 position locking remains unverified; preserve the user's statement “no position locking” as user-stated. Cult Heroes route/rewards remain unresolved. No dimension is closed; no exhaustion declaration. Source ledger now records 666 entries / 509 unique visited URLs / 404 unvisited leads.
