# CONFLICTS LEDGER — DLS26 OMEGA
Consolidated 2026-10-17T19:15Z (session sess-20261017-001, turn 6); extended 2026-10-18 (turn 35, waves 18-29) with C-010..C-016. Authority: CONFLICT PROTOCOL (Core Identity) and the EVIDENCE CONFLICT log category.
Each entry: the two sides with origin and date, the status, what would settle it, and what the system may say meanwhile. An unresolved conflict is never resolved by picking the more convenient side; where advice depends on one, both are presented with the cost of being wrong.

## OPEN

### C-001 — Language count: 15 vs 24
- **Side A:** 15 languages — App Store listing snapshot, captured 2026-10-11 (CLAIM-053, store-published).
- **Side B:** 24 languages — static APK listing metadata, captured through 2026-10 (CLAIM-094, APKMirror-derived).
- **Status:** UNRESOLVED. Hypothesis to test first: the store field counts *localised store listings* while the APK field counts *packaged language resources*; they would then both be true of different objects.
- **Settles it:** a datamined resource count (`res/values-*` directories) or an official statement of supported languages.
- **May say meanwhile:** "the store lists 15 localised listings, the APK metadata lists 24 languages — these may count different things." Never quote either as "the" language count.
- **Reopening/verification:** RQ-20261017-012.

### C-002 — Leaderboard reward cadence: "weekly gems" vs 3–30 day resets
- **Side A:** official FTG text says multiplayer leaderboards reset at regular intervals of 3–30 days (CLAIM-002, Confirmed).
- **Side B:** an Indonesian community guide says Dream League Live pays gems weekly by leaderboard position (CLAIM-051, Community Consensus), and CLAIM-066 repeats "weekly-leaderboard gems".
- **Status:** UNRESOLVED but narrowed — the official 3–30 day window does not forbid a weekly *reward* cycle; the conflict is about whether the words describe the same clock.
- **Added turn 15 (EV-117):** the official gem article says gems come from "completing league objectives, completing tournaments, through the Season Pass and Prize Ladder and by participating in Multiplayer (Dream League Live) mode… quantity depends on the circumstance". It does **not** mention leaderboard position. That neither confirms nor refutes the community claim; it means the community wording describes a *mechanism* the official text does not describe, which is a second, separate gap.
- **Settles it:** an in-game leaderboard screen capture showing both the reset timer and the reward statement.
- **May say meanwhile:** "resets are officially 3–30 days; weekly gem payouts are a community report and are not confirmed."

### C-003 — Release payout: "coach" vs "bux/coins"
- **Side A:** v12.200+ release grants a *coach* (official article 360003945617, CLAIM-032 / CLAIM-114, Confirmed).
- **Side B:** earlier captures describe a specified payout of "bux"/coins (CLAIM-029, inherited summary).
- **Status:** UNRESOLVED, most likely a version change (payout model changed at 12.200) rather than a contradiction.
- **Settles it:** a current-build release observation, or an article revision captured after 12.200 that mentions both.
- **May say meanwhile:** "in v12.200+ you receive a coach; older text describes a coin payout, so the payout may depend on build."

### C-004 — iCloud save toggle
- **Side A:** an older official article documents an in-game iCloud toggle for DLS (preserved in the inherited corpus).
- **Side B:** the current save/account model is Google/Apple sign-in plus a one-time transfer code (CLAIM-022/083, Confirmed).
- **Status:** DISPUTED (CLAIM-042) — the older article is not obviously wrong, it is older.
- **Settles it:** a current-build Settings capture on iOS.

### C-005 — "Weekly" DLL structure vs multi-ladder reality
- **Side A:** community descriptions treat DLL as a weekly ladder (CLAIM-066).
- **Side B:** progression is multi-track with no single global rank (CLAIM-088, High Confidence), and the mission's "#1 global" target has no verified surface at all (CLAIM-003, Speculative).
- **Status:** UNRESOLVED in wording; the underlying facts are compatible if "weekly" refers to one of several ladders.
- **Settles it:** a capture of the live leaderboard surface with its timer.

### C-006 — Auto-switch article: live text vs reported dead link
- **Side A:** the article "Why are my players auto-switching all the time?" (360008315158) is **live and fully captured** — EV-145 holds its complete text, fetched 2026-10-10T22:58Z, and CLAIM-106 is built on it verbatim.
- **Side B:** the sibling session on `arena/22655f48-dls26-omega` records the same article as a dead link (GS-030), captured on its own timeline.
- **Status:** UNRESOLVED. Both captures are physical; the most probable explanation is a transient Zendesk outage or a removal-and-restore between the two fetches, not a contradiction about content.
- **Settles it:** one fresh fetch of the slug in a permitted environment, recording HTTP status and timestamp.
- **May say meanwhile:** quote CLAIM-106 from EV-145 (full text exists) and note that the URL's liveness is not guaranteed; the *behaviour* claim does not depend on the URL staying up.
- **Note:** this is the residual "cross-branch contradiction" item carried since turn 6.

### C-007 — Which stores are authorised: four vs two
- **Side A:** the Terms of Use / EULA (last updated 25 Jul 2025, EV-170, full page) names **four** authorised stores — Apple App Store, Google Play, Amazon App Store, Windows Phone Store — and says FTG "does not publish to any other store".
- **Side B:** the sanction-policy article (EV-201, verbatim) says **"The only authorised versions of DLS are available from Apple's App Store or Google's Play Store."**
- **Status:** UNRESOLVED. The two official texts are not reconcilable as written. Likely explanations: the EULA is the older, broader legal list (Windows Phone Store is defunct), while the sanction article reflects current distribution. Neither side is a community claim.
- **Impact on the mission:** **none for the red line** — mods, hacks and third-party builds are prohibited under both texts, and only Play/App Store builds are what the user can install today. It matters for precision: CLAIM-043 must not be quoted as "the EULA says Play and App Store only".
- **Settles it:** a current FTG store-availability statement, or an EULA revision listing two stores.
- **May say meanwhile:** "FTG's EULA lists four storefronts; its sanctions article recognises Play and App Store. Only those two are current for DLS26."

### C-008 — Promotion: Division Objectives vs XP ladder
- **Side A (community, VI):** each Division season = 15 matches, and promotion runs through **Division Objectives** — required wins + goals totals, no need to win every match (EV-192 snippet, EV-196 full page; CLAIM-062, Community Consensus).
- **Side B (official, verbatim):** *"The more matches you win, the more XP you will earn. When you reach the maximum XP for your current rank, you will be promoted. Similarly, losing matches will cause you to lose XP and get relegated."* (EV-195, article 7917423348497; CLAIM-067, Confirmed). The article does **not** name the surface (Career division vs Dream League Live rank).
- **Status:** UNRESOLVED, and it is the sharpest conflict found in the interpretive sample, because the two accounts imply different strategies: objective-completion efficiency (Side A) vs win-rate/XP accumulation (Side B).
- **Plausible reconciliation:** objectives grant the XP, or the two mechanics govern different ladders (Career vs DLL). Neither is documented.
- **Settles it:** a Career screen capture showing the promotion requirement (objectives list vs XP bar), or an official article that names the surface.
- **May say meanwhile:** "the only official promotion text describes an XP ladder; a community guide describes division objectives. Which governs Career is unverified — check your division screen before optimising for objectives."
- **Impact on coaching:** blocks any advice that trades wins for goal-farming until resolved.

### C-009 — Is the Season Leaderboard the same board as the DLL leaderboards?
- **Side A:** the article defining leaderboards scopes them to **Multiplayer (Dream League Live)**, resets 3–30 days, prizes by end position (EV-101; CLAIM-002, High Confidence).
- **Side B:** a different official article says Season Points "and your current total is shown on the **season leaderboard accessed from the Main Menu**" (EV-126/EV-197; CLAIM-071, Confirmed).
- **Status:** UNRESOLVED. Both are official and neither mentions the other. Three readings are open: (i) two separate boards; (ii) one board with two entry points; (iii) the Main Menu board is a personal/personal-plus standings view with no public ranking at all.
- **Why it matters:** the mission target is "#1". CLAIM-003 lists the Season Leaderboard as a candidate surface. If it is not a public, cross-player ranking, it cannot define "#1", and the only public surfaces left are the DLL leaderboards (3–30 day resets) and LIVE Tier.
- **Settles it:** a Main Menu → Season Leaderboard capture showing whether other players appear and whether a rank/position is displayed, or an official sentence linking the two.
- **May say meanwhile:** "there are two official boards with different names and no documented relationship; neither has been shown to display a global position."

### C-010 — Stadium capacity per division: three incompatible tables
- **Side A:** r/DLS DLS24 beginner guide (Mar 2024, EV-403) — Academy 5,000 / Amateur 15,000 / Div 4 25,000 / Div 3 35,000 / Div 2 45,000 / Div 1 55,000 / Elite 70,000 / Legendary 85,000; max capacity 92,000; ~1,400 coins per promotion.
- **Side B:** dlspedia.fandom (EV-403/EV-408) — Academy 6,462 (starting) / Div 3 15,000 / Div 2 30,000 / Div 1 45,000 / Junior Elite 60,000 / Elite 80,000; max seats 90,456; max autobuild 80,000.
- **Side C:** mundodls (Spanish, EV-403) — Amateur 4,000 / Primera 20,000 / Legendary 45,000.
- **Partial corroboration:** dream-league-soccer.fandom's Division 3 page (entry 35,000; progression to Division 2 at 45,000) matches Side A exactly, and the Exophase achievements (40,000 and 80,000 thresholds) are consistent with both A and B.
- **Status:** UNRESOLVED. Side A is best-supported but all three are community-derived; "Junior Elite Division" in Side B is a confirmed historical division name (Exophase "Time To Step Up" achievement), so Side B may describe an older ladder.
- **Status:** SUBSTANTIALLY RESOLVED 2026-10-18 (EV-423). Vietnamese Wikipedia records that the 2016-2019 era had only SIX divisions - Academy, Division 3, Division 2, Division 1, Junior Elite and Elite, across 96 teams - and the Exophase "Time To Step Up" achievement confirms Junior Elite as a real historical division. Side B is therefore the LEGACY six-division ladder, not the current one, so Side A (eight divisions) is the only table describing the current structure. Side C (Spanish, 4,000/20,000/45,000) remains an unexplained outlier.
- **Settles it fully:** an in-game Stadium & Facilities capture showing the next division seat requirement for the current eight-division ladder.
- **May say meanwhile:** "Side A describes the current eight-division ladder and is the only table that fits it; the dlspedia figures are a legacy six-division table. The promotion seat requirement sits in the 35,000-45,000 band around Division 3/2, and the cheapest first capacity upgrade costs about 446 coins."

### C-011 — Commercial Centre bonus scale: 13%/21% vs 2-10% vs DLS21 +6%
- **Side A:** 13% at Level II and 21% at Level III — Bluestacks 2026, gamingonphone (three separate guides) and gamedls.net, three independent sources (EV-404).
- **Side B:** sportsdunia's table 2% / 4% / 6% / 8% / 10% by level (EV-404) — internally inconsistent (its Level 3 kit discount is listed as 1%, breaking monotonicity) and contradicted by three sources.
- **Side C:** DLS21-era first upgrade gave +6% match winnings (LevelWinner, EV-404) and rajatips says Level 1 = 6%.
- **Status:** RESOLVED in favour of Side A on multi-source grounds; Side B REJECTED; Side C recorded as version drift showing the scale was re-tuned between DLS21 and DLS24+.
- **May say meanwhile:** "Commercial Level II = +13% and Level III = +21% post-match coins."

### C-012 — Custom kit import gem cost: 150 vs 300
- **Side A:** 150 gems one-time unlock — dlskiturl.com, dlsgame.net and mundodls.com, three independent kit sites (EV-402).
- **Side B:** 300 diamonds one-time unlock — Bluestacks custom-kit guide (EV-402).
- **Status:** RESOLVED in favour of Side A on multi-source grounds (three specialist kit sites against one general guide). Note mundodls additionally prices the custom crest at 75 gems (225 total) and one site reports the iOS unlock is cheaper than Android.
- **May say meanwhile:** "budget 150 gems for the custom kit unlock (225 with the crest); 300 is a single-source outlier."

### C-013 — Global Challenge Cup format
- **Side A:** any single loss eliminates you (dream-league-soccer.fandom, EV-416).
- **Side B:** round-robin groups of 4 with the top 2 qualifying, then a single-legged knockout — Bluestacks, dls-wiki.fandom, and r/DLS quantifying 32 groups of 4 = 128 teams feeding a 64-team Round 1 (EV-416).
- **Side C:** you play three group opponents twice, Champions-League style (r/DLS, EV-416).
- **Status:** UNRESOLVED. Side B has the most support and the most internal consistency (32 x 4 = 128 reconciles the "128 teams" report), but the two-legged and any-loss-eliminates variants are not refuted.
- **Settles it:** an in-game GCC group-table capture.
- **May say meanwhile:** "the GCC is best documented as groups of four with two qualifiers, then a knockout; it pays 10 gems per round cleared and 25 for winning it."

### C-014 — Is 4-2-3-1 a good formation?
- **Side A:** sportsdunia ranks 4-2-3-1 second of its top five DLS26 formations (EV-414).
- **Side B:** r/DLS advises never using 4-2-3-1 because the lone striker gets no support and the team is punished by long balls (EV-414).
- **Status:** UNRESOLVED and playstyle-dependent; both recorded.
- **May say meanwhile:** "4-2-3-1 suits midfield control; players who concede long balls are advised against it."

### C-015 — International Cup / All-Star Cup availability
- **Side A:** older wiki and long-term players report 18+ International Cup and All-Star Cup wins after winning the Legendary Division (EV-416).
- **Side B:** an Aug 2025 r/DLS thread reports the International Cup appearing only in the trophies list and not being playable in DLS25 (EV-416).
- **Status:** UNRESOLVED, version-dependent.
- **Settles it:** a current-build main-menu competition list.
- **May say meanwhile:** "the International and All-Star Cups are documented but their current-build availability is unconfirmed."

### C-016 — Facility roster: five official vs seven in-game
- **Side A:** official store copy names five facilities — Stadium, Medical, Commercial, Training, Fanzone (GS-023, official-stated).
- **Side B:** community guides (ldplayer, chaptercheats) place Recruitment Centre and Accommodation in the in-game Stadium & Facilities screen as well (EV-419).
- **Status:** RESOLVED as a scope difference, not a contradiction: five facilities are official-stated; Recruitment and Accommodation are in-game surfaces reported only by community sources. The earlier "seven confirmed facilities" claim is corrected.
- **May say meanwhile:** "five facilities are officially named; Recruitment and Accommodation also appear in the facility screen."

**UPDATE 2026-10-18 (ckpt-091):** SUBSTANTIALLY RESOLVED. GCC is a Champions-League-style ONLINE competition open to every division: **128 teams in 32 groups of 4, top 2 per group qualify -> 64-team knockout from R64**, group stage played as 3 opponents twice (6 matches), about 7 rounds to the trophy. Rewards: **10 gems per round cleared + ~25 gems for winning** (full season run ~30 league + 25 GCC + 15 Diamond Cup + 5 All-Star). Difficulty scales with DIVISION not club stars, and players call it the easiest competition to win. The residual conflict is only the group-stage match count (6 double round-robin vs an unspecified single pass) — see EV-434.

## RESOLVED (kept for history, with the evidence that resolved them)

### C-R01 — Launch date: Dec 4 2026 vs Dec 17 2025
- Community text (thesoccerera, EV-001/002) claimed "full global availability December 4, 2026"; the store version history shows build 13.040 dated 17/12/2025 and continuous updates since.
- **Resolved** in favour of the store timeline (CLAIM-008). The community claim is retained in-record as a historical anomaly, not deleted.

### C-R02 — Summer Spotlight attribution
- Two candidate update windows; resolved by the version-history mapping to the 13.310–13.350 band (CLAIM-048). Retained as resolved.

### C-R03 — XP transcription 145,299 vs 145,296
- A Tier-1 world-record total was transcribed as 145,299; the source states 145,296. **Resolved** by re-reading the source; corrected in the KB with the transcription lesson recorded (numeric transcriptions get a second check).

## Standing rule for this ledger
A conflict is closed only with evidence that settles the proposition, never because a later claim simply repeated one side. Where a conflict depends on the current build and cannot be checked in this environment, it stays open and its advice states the dependency.

## C-017: Clan top-contributor gem reward (50 vs 100)
- **Source A:** r/DreamLeagueSoccer 1pk9dae (Dec 2025, Spanish-language clan-leader thread) — the clan's number-one contributor receives **50 gems** at season end; a comment adds that contributions above 350k only help you become first in-clan, not the clan total.
- **Source B:** sportsdunia DLS26 Clans guide — "having the highest clan points gives you the reward of **100 gems**".
- **Status:** OPEN. Both are community sources; no official FTG figure found. Recorded in EV-429 / CLAIM on clan reward. Needs an in-game screenshot or FTG support confirmation.

## C-018: Cult Heroes OVR (92 vs 95 max)
- **Source A:** r/DreamLeagueSoccer 1wele5q (17 Sep 2026) — shows Insigne, Aubameyang, Dybala and De Gea all at **92**.
- **Source B:** dlsinside.com / sakibpro.com datamine (build 13430, 2026-09-16) — max rating **95** for de Gea, Aubameyang and Dybala; **94** for Insigne. dreamkitsapp lists Vozinha at 84 while dlsinside lists 83.
- **Status:** OPEN. Most likely Source A is showing post-boost/in-game OVR or an earlier build. Recorded in EV-430.

## C-019: Commercial facility bonus (13%/21% vs "10% at L5, biggest FTG scam")
- **Source A:** gamingonphone DLS25/DLS26 coin guides — Commercial Level II gives a **13%** in-game coin bonus and Level III a **21%** bonus, with the first upgrade at 75 gems.
- **Source B:** r/DreamLeagueSoccer 176ntor (Oct 2023) — "Commercial facility is the biggest FTG scam, it was good in DLS20, but don't put your gems there", with a comment claiming **10% for level 5** costing a total of **1,000+ gems**.
- **Status:** OPEN. The two sources disagree on both the magnitude and the shape of the curve, and Source B is a DLS23-era complaint. Recorded in EV-437. The masterplan's facility-priority table should be re-checked once resolved.

## C-020: Special Player max cost (2,100 gems / 7.5 coaches vs 6-7 coaches vs 2,100-2,835)
- **Source A:** r/DreamLeagueSoccer 1hnll1u (Dec 2024) — 90 upgrade points / 12 points per Legendary Special Coach = **7.5 coaches**, at 280 gems each = **2,100 gems**; Rares would be 15 x 168 = 2,520 gems.
- **Source B:** r/DreamLeagueSoccer 1b4ovuj (Mar 2024) — "roughly **2100-2835 gems** to max a special player".
- **Source C:** r/DreamLeagueSoccer 1pp07c2 (Dec 2025) — "it takes **6-7 Legendary Special Coaches** to max a special player".
- **Status:** OPEN, low impact. The spread is explained by breakthroughs and by the choice mechanic letting you land points more efficiently. Recorded in EV-439. Use 2,100 gems as the planning figure.

## C-021: Transfer market refresh cadence (per-match vs every 7 hours)
- **Source A:** Bluestacks + gamingonphone DLS26 guides — the Live Transfer Market **refreshes after every match you play**.
- **Source B:** r/DreamLeagueSoccer 18gl9ob (Dec 2023) — a commenter states the market "**refreshes every 7 hours**".
- **Status:** OPEN, low impact. Most likely Source B refers to a different surface (the shop) or an older build. Operationally, treat per-match refresh as the rule and note that forfeits, scenarios, exhibition matches and ads do NOT trigger it. Recorded in EV-442.

## C-017 UPDATE (2026-10-18, ckpt-098): clan top-contributor gem reward — now leans 100
- A detailed community calculation post itemises the clan component of a season as **275 gems = 25 + 150 (10M Clan Points ladder) + 100 for being number one in-clan**, which supports the **100-gem** figure from sportsdunia.
- The **50-gem** figure comes from a single Spanish-language clan-leader thread (r/DLS 1pk9dae).
- **Status:** still formally OPEN, but the weight of evidence now favours **100 gems**. No official FTG figure has been found.

## C-022: Corner footedness (same-foot vs opposite-foot corner)
- **Source A (majority):** r/DreamLeagueSoccer 1lyxfag (Jul 2025), 1pp7fzd (Dec 2025) — a RIGHT-footed player takes the RIGHT corner and a LEFT-footed player the LEFT corner, which makes corners "more accurate" and is described as the mistake most players make in reverse.
- **Source B (minority):** r/DreamLeagueSoccer 1lyxfag (same thread, different commenter) — "Use a right footed player when taking the left corner and vice-versa."
- **Status:** OPEN, low impact. Both are community reports with no official basis. The outswinger routine in CLAIM (EV-444) uses the SAME-foot pairing. Recorded in EV-444. **Resolution path: test both in the free training ground before committing.**

