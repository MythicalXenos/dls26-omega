# Step-1 Research Observation — Q-009 official DLS FAQ sweep

Recorded: 2026-10-23T16:29:26Z UTC (turn 6; `functions.fetch_page` batch completion clock). User instruction at 2026-10-23T16:24:17Z: “Clear handoff/attention_[required.md](http://required.md) and continue Step 1 background research.” Prior attention checkpoint was archived to `handoff/archive/attention_required_ckpt-0005.md`; manual Step-1 continuation is authorized.

## Section index and pagination observations

Canonical section: https://support.ftgames.com/hc/en-us/sections/203117809-Dream-League-Soccer-FAQs

The direct section render returned page 1 with 30 article links (`totalChunks=1`, `hasMore=false`). Explicit `?page=2` returned 22 additional links. Explicit `?page=3` returned an empty section render. This supports a two-page index with an empty page-3 sentinel; page 4 was not queried. The source log records the exact attempts as R-0017–R-0019. The list below is the full set of 52 article links observed across pages 1–2; link discovery does not mean article content was fetched.

### Page 1 — 30 article links
- DR-0008 — [When will the next app update be?](https://support.ftgames.com/hc/en-us/articles/360000262229-When-will-the-next-app-update-be)
- DR-0007 — [How do the various player stats in DLS affect gameplay?](https://support.ftgames.com/hc/en-us/articles/360019166777-How-do-the-various-player-stats-in-DLS-affect-gameplay)
- DR-0025 — [How is save data stored and transferred in DLS?](https://support.ftgames.com/hc/en-us/articles/4413273241873-How-is-save-data-stored-and-transferred-in-DLS)
- DR-0026 — [How do I find my User ID?](https://support.ftgames.com/hc/en-us/articles/37082887837202-How-do-I-find-my-User-ID)
- DR-0013 — [Removal of Facebook Login from DLS](https://support.ftgames.com/hc/en-us/articles/9804887423121-Removal-of-Facebook-Login-from-DLS)
- DR-0027 — [Can I use my Dream League Soccer (formally DLS19) profile in DLS25?](https://support.ftgames.com/hc/en-us/articles/360004717278-Can-I-use-my-Dream-League-Soccer-formally-DLS19-profile-in-DLS25)
- DR-0028 — [Why does the app require a connection to play?](https://support.ftgames.com/hc/en-us/articles/360004034498-Why-does-the-app-require-a-connection-to-play)
- DR-0029 — [Is my device compatible with the app?](https://support.ftgames.com/hc/en-us/articles/214385685-Is-my-device-compatible-with-the-app)
- DR-0030 — [Why can't I update the app?](https://support.ftgames.com/hc/en-us/articles/360000220945-Why-can-t-I-update-the-app)
- DR-0010 — [What is the Season Pass?](https://support.ftgames.com/hc/en-us/articles/4404070913169-What-is-the-Season-Pass)
- DR-0006 — [What is the Prize Ladder?](https://support.ftgames.com/hc/en-us/articles/23108987826962-What-is-the-Prize-Ladder)
- DR-0011 — [What are Dream Point Boosts?](https://support.ftgames.com/hc/en-us/articles/24081168829330-What-are-Dream-Point-Boosts)
- DR-0009 — [What are Clans?](https://support.ftgames.com/hc/en-us/articles/30839289076626-What-are-Clans)
- DR-0031 — [How do I play a Friend Match?](https://support.ftgames.com/hc/en-us/articles/360019064438-How-do-I-play-a-Friend-Match)
- DR-0032 — [How do I restart my career from the beginning?](https://support.ftgames.com/hc/en-us/articles/213851909-How-do-I-restart-my-career-from-the-beginning)
- DR-0033 — [I am not seeing any video clips, what can I do?](https://support.ftgames.com/hc/en-us/articles/360017166918-I-am-not-seeing-any-video-clips-what-can-I-do)
- DR-0034 — [How can I reduce my mobile data usage?](https://support.ftgames.com/hc/en-us/articles/360005680437-How-can-I-reduce-my-mobile-data-usage)
- DR-0035 — [Why doesn't my player look like the real person?](https://support.ftgames.com/hc/en-us/articles/360004718318-Why-doesn-t-my-player-look-like-the-real-person)
- DR-0036 — [How do I hide the text on the control buttons?](https://support.ftgames.com/hc/en-us/articles/14369944135058-How-do-I-hide-the-text-on-the-control-buttons)
- DR-0037 — [How do I customise my kit/logo?](https://support.ftgames.com/hc/en-us/articles/360004080497-How-do-I-customise-my-kit-logo)
- DR-0038 — [How do I obtain more players?](https://support.ftgames.com/hc/en-us/articles/360004066417-How-do-I-obtain-more-players)
- DR-0039 — [How do I change my manager?](https://support.ftgames.com/hc/en-us/articles/360003945937-How-do-I-change-my-manager)
- DR-0040 — [How does game difficulty work?](https://support.ftgames.com/hc/en-us/articles/360018360418-How-does-game-difficulty-work)
- DR-0041 — [What are Leaderboards?](https://support.ftgames.com/hc/en-us/articles/360003914998-What-are-Leaderboards)
- DR-0012 — [How does Dream League Live matchmaking work?](https://support.ftgames.com/hc/en-us/articles/360018359998-How-does-Dream-League-Live-matchmaking-work)
- DR-0042 — [How do I change my emojis in Dream League Live?](https://support.ftgames.com/hc/en-us/articles/360020938198-How-do-I-change-my-emojis-in-Dream-League-Live)
- DR-0043 — [Can my opponent see my custom kit and logo in Dream League Live?](https://support.ftgames.com/hc/en-us/articles/360021064298-Can-my-opponent-see-my-custom-kit-and-logo-in-Dream-League-Live)
- DR-0044 — [Multiplayer Troubleshooting](https://support.ftgames.com/hc/en-us/articles/360004222118-Multiplayer-Troubleshooting)
- DR-0045 — [How do I earn coins in the app?](https://support.ftgames.com/hc/en-us/articles/214385285-How-do-I-earn-coins-in-the-app)
- DR-0046 — [Is it possible to earn free coins?](https://support.ftgames.com/hc/en-us/articles/213851369-Is-it-possible-to-earn-free-coins)

### Page 2 — 22 article links
- DR-0047 — [How can I get Gems?](https://support.ftgames.com/hc/en-us/articles/360003914938-How-can-I-get-Gems)
- DR-0048 — [Can I make an in-app purchase?](https://support.ftgames.com/hc/en-us/articles/214229005-Can-I-make-an-in-app-purchase)
- DR-0049 — [What are facilities?](https://support.ftgames.com/hc/en-us/articles/360003945917-What-are-facilities)
- DR-0050 — [How can I expand my squad?](https://support.ftgames.com/hc/en-us/articles/360003945677-How-can-I-expand-my-squad)
- DR-0051 — [Can I sell my players?](https://support.ftgames.com/hc/en-us/articles/360003945617-Can-I-sell-my-players)
- DR-0052 — [How do I develop my players?](https://support.ftgames.com/hc/en-us/articles/360003914778-How-do-I-develop-my-players)
- DR-0053 — [Why have I been blocked from playing DLS?](https://support.ftgames.com/hc/en-us/articles/360008904718-Why-have-I-been-blocked-from-playing-DLS)
- DR-0054 — [I can’t connect to the game, what can I do?](https://support.ftgames.com/hc/en-us/articles/360003945557-I-can-t-connect-to-the-game-what-can-I-do)
- DR-0055 — [What is Haptic Feedback?](https://support.ftgames.com/hc/en-us/articles/19336294718098-What-is-Haptic-Feedback)
- DR-0056 — [Why are my players auto-switching all the time?](https://support.ftgames.com/hc/en-us/articles/360008831518-Why-are-my-players-auto-switching-all-the-time)
- DR-0057 — [How can I change my graphics settings?](https://support.ftgames.com/hc/en-us/articles/360000598437-How-can-I-change-my-graphics-settings)
- DR-0058 — [Can I change my team name?](https://support.ftgames.com/hc/en-us/articles/214385345-Can-I-change-my-team-name)
- DR-0059 — [How do I perform a skill move?](https://support.ftgames.com/hc/en-us/articles/213851489-How-do-I-perform-a-skill-move)
- DR-0060 — [Why are some players missing from the app?](https://support.ftgames.com/hc/en-us/articles/213852049-Why-are-some-players-missing-from-the-app)
- DR-0061 — [Why are some players displaying a different player card colour?](https://support.ftgames.com/hc/en-us/articles/214385645-Why-are-some-players-displaying-a-different-player-card-colour)
- DR-0062 — [Can I re-sign a player that I have sold previously?](https://support.ftgames.com/hc/en-us/articles/214385465-Can-I-re-sign-a-player-that-I-have-sold-previously)
- DR-0063 — [How do I change between Home and Away kits before a match?](https://support.ftgames.com/hc/en-us/articles/214385385-How-do-I-change-between-Home-and-Away-kits-before-a-match)
- DR-0064 — [How do I customise my kit / logo in Dream League Soccer (19)?](https://support.ftgames.com/hc/en-us/articles/214422145-How-do-I-customise-my-kit-logo-in-Dream-League-Soccer-19)
- DR-0065 — [How do I watch my saved replays?](https://support.ftgames.com/hc/en-us/articles/214385405-How-do-I-watch-my-saved-replays)
- DR-0066 — [Is there any way to view my team’s stats?](https://support.ftgames.com/hc/en-us/articles/213851469-Is-there-any-way-to-view-my-team-s-stats)
- DR-0067 — [How do I change my nationality?](https://support.ftgames.com/hc/en-us/articles/213851429-How-do-I-change-my-nationality)
- DR-0068 — [Something happened in the game that’s not realistic. Why is this?](https://support.ftgames.com/hc/en-us/articles/360000842697-Something-happened-in-the-game-that-s-not-realistic-Why-is-this)

## Article content fetched in this slice

All eight support-article renders returned successfully. Seven returned one complete tool chunk; Friend Match returned chunk 0 of 3, so its comments/article projection remains partial. The tool exposed no HTTP status or original source-payload digest; this note is a selected extraction, not an immutable/full page payload. Its SHA-256 protects only this local note. Do not treat these observations as admitted claims without the required evidence gates.

### Clans — DR-0009
- URL: https://support.ftgames.com/hc/en-us/articles/30839289076626-What-are-Clans
- Returned-page observation: Clan article describes one-clan membership, leader succession, optional entry conditions/invite codes, conduct rules; clan points via matches, challenges, Season Passes.

### Season Pass — DR-0010
- URL: https://support.ftgames.com/hc/en-us/articles/4404070913169-What-is-the-Season-Pass
- Returned-page observation: Article says applicable from DLS release version 12200 onward; free and paid tracks; paid unlocks Progress Bank rewards based on DLL XP at season end; Season Points come from matches and vary by mode; pass is per-season, not subscription. Version mapping/current DLS26 applicability unverified.

### Dream Point Boosts — DR-0011
- URL: https://support.ftgames.com/hc/en-us/articles/24081168829330-What-are-Dream-Point-Boosts
- Returned-page observation: Article says boosts temporarily increase Dream Points; apply to career, Dream Draft, scenario and DLL matches; not exhibition/Friend Matches; unavailable when Prize Ladder is complete/inactive; unused boosts carry to next ladder.

### Friend Match — DR-0031
- URL: https://support.ftgames.com/hc/en-us/articles/360019064438-How-do-I-play-a-Friend-Match
- Returned-page observation: Chunk 0 of 3: code-based private match; allowed characters A–Z, 0–9 and hyphen; accessed through Dream League Live button; Friend Match stats tracked. Remaining chunks/comments not fetched.

### Player acquisition — DR-0038
- URL: https://support.ftgames.com/hc/en-us/articles/360004066417-How-do-I-obtain-more-players
- Returned-page observation: Article lists transfers, scouts, agents and Prize Ladder as acquisition routes; says transfers refresh each in-game week after a single-player match.

### Game difficulty — DR-0040
- URL: https://support.ftgames.com/hc/en-us/articles/360018360418-How-does-game-difficulty-work
- Returned-page observation: Undated support text: single-player difficulty changes with division; DLS25 introduced Medium/Hard base difficulty; says Live matches use real users and no difficulty manipulation. DLS26 applicability not established.

### Coin earning — DR-0045
- URL: https://support.ftgames.com/hc/en-us/articles/214385285-How-do-I-earn-coins-in-the-app
- Returned-page observation: Article lists match results, clean sheets, goals, stadium bonuses, season objectives, Season Pass/Prize Ladder rewards, league positions, cups and video clips where available.

### Dream League Live matchmaking — DR-0012
- URL: https://support.ftgames.com/hc/en-us/articles/360018359998-How-does-Dream-League-Live-matchmaking-work
- Returned-page observation: Undated support text says matching considers LIVE Tier, location and availability pool; same-tier matching is intended but may fail when players are scarce; no additional difficulty controls described. Current DLS26 applicability unverified.

## UGC and applicability boundaries

The Friend Match page projection visibly includes user comments (some in non-English languages) in addition to FTG article text. This is a distinct user-generated-content layer, recorded as DR-0069; only comments visible in chunk 0 were encountered, and the remaining chunks were not fetched. Do not use comments as publisher-authored mechanics evidence.

Several support pages are undated or explicitly refer to DLS25 / version 12200 onward. Their content is recorded as publisher-stated text, not asserted as current DLS26 mechanics. No claim was promoted, no imported claim file was edited, no confidence tier was assigned, and the epoch remains OPEN.

## Queue disposition

Q-009 remains OPEN. Section pages 1–2 were inventoried and page 3 returned empty; eight article pages were fetched, with Friend Match partial. The remaining listed article references remain in `logs/sources_visited.json` as UNVISITED/IN_PROGRESS. Resume at the first remaining owed article in the physical frontier; do not skip Q-009 or infer DLS26 applicability.
