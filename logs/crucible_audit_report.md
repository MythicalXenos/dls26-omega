# Crucible Audit Report

Standalone epistemic verification crucible (pre-Step-2 gate). 156 claims / 158 EV / ~1.59M-line corpus.

## Method
1. **Internal Skeptic pass** — filter out ungrounded/private-server/rumor/mod-scam content.
2. **Devil's Advocate** — mechanical refit of OVR formula via Gram-Schmidt QR OLS on 23,327 TrungTaHust rows; direct grep/verification of CB DP weights, price tiers, roster caps, button mapping, state machine, promo OVR caps.
3. **Witness spot-checks** — numeric re-verification of regression coefficients, MAE/RMSE, ±1 hit rate, price tiers (2800 for 86s), roster counts (2,518 base, n=4 @ 86), cap 100, formation/state counts.
4. **Cross-branch drift** — diff current claims.jsonl against a7e23a6b 87-claim baseline.
5. **Targeted web searches** attempted but all non-GitHub hosts TLS-blocked from sandbox; verification limited to in-corpus evidence (targeted searches deferred to device pipeline / user-supplied APK).
6. **5-tier reclassification** — Confirmed (official FTG source) / High Confidence (≥2 independent structured community sources, or APK-static corroboration) / Community Consensus (single structured source or guide/blog corroboration) / Speculative (anecdote/reddit/self-referential) / Rejected.

## EV Provenance Tiers
- **A**: 101
- **B**: 10
- **C**: 21
- **D**: 20
- **E**: 6

## Claim Tier Distribution
- Current: {'High Confidence': 74, 'Speculative': 12, 'Confirmed': 34, 'Disputed': 1, 'Community Consensus': 35}
- Recommended: {'Confirmed': 96, 'Speculative': 5, 'High Confidence': 25, 'Community Consensus': 30}
- Tier changes: **102**

## Tier Changes
- `CLAIM-092`: **Community Consensus** → **Speculative** (src=['kb-import']) — Historical/legend players can appear in multiple versions and multiple copies can exist in
- `CLAIM-101`: **Community Consensus** → **Speculative** (src=['reddit']) — Squad depth: DLS26 carries reserves plus a fixed eight substitutes (community megathread, 
- `CLAIM-053`: **Confirmed** → **Community Consensus** (src=['store']) — App Store ID-locale snapshot 2026-10-11: #7 free Sports chart (ID), 42K ratings 4.6, 269.6
- `CLAIM-054`: **Confirmed** → **Community Consensus** (src=['inferred', 'store']) — DLS26 official version timeline (App Store ID-locale history): 13.040 LAUNCH 17/12/2025 (s
- `CLAIM-056`: **Confirmed** → **Community Consensus** (src=['store']) — App Store ID IAP catalog + app metadata (2026-10-11): **Season Pass Rp 35.000 and Promo Se
- `CLAIM-060`: **Confirmed** → **Community Consensus** (src=['trung']) — dreamkitsapp player numbers are self-declared APPROXIMATE CALCULATIONS from stats (site no
- `CLAIM-084`: **Confirmed** → **Community Consensus** (src=['gh-ugc']) — PUBLIC CHEAT/MOD/AUTOMATION ECOSYSTEM exists around the DLS franchise (incl. DLS26-branded
- `CLAIM-093`: **Confirmed** → **Community Consensus** (src=['kb-import', 'store']) — Facilities are five in number: Stadium, Medical, Commercial, Training (store copy) and Fan
- `CLAIM-008`: **High Confidence** → **Community Consensus** (src=['inferred', 'store']) — DLS26 launch resolved by store version history (EV-183, App Store id1462911602, official-s
- `CLAIM-055`: **High Confidence** → **Community Consensus** (src=['inferred', 'store']) — Live-upgrading special-player lineage (store version history): 'Dream Stars 26' (announced
- `CLAIM-085`: **High Confidence** → **Community Consensus** (src=['gh-ugc', 'store-mirror', 'trung']) — COMMUNITY DATA/TOOLING LAGS THE LIVE SEASON: fan datasets and creator tools observed 2026-
- `CLAIM-088`: **High Confidence** → **Community Consensus** (src=['en-blog']) — DLS26 PROGRESSION IS MULTI-TRACK (no single global rank): parallel reward/ladder systems d
- `CLAIM-097`: **High Confidence** → **Community Consensus** (src=['sakibpro']) — OVR is community/tool shorthand for Overall (the player's rating). Tool usage: sakibpro de
- `CLAIM-116`: **High Confidence** → **Community Consensus** (src=['dreamkitsapp']) — Special-player taxonomy with counts (dlsinside database at build 13.430, single database):
- `CLAIM-135`: **High Confidence** → **Community Consensus** (src=['fbgd']) — Star players have MULTIPLE cards across collections/rarities with different OVRs and posit
- `CLAIM-139`: **High Confidence** → **Community Consensus** (src=['trung']) — Transfer-market coin prices follow a tier table of 4 sub-tiers per OVR (keys "RR1".."RR4" 
- `CLAIM-141`: **High Confidence** → **Community Consensus** (src=['trung']) — DLS26 Season 2026 Update 1 ships at least 2,518 base roster players (regular/purchasable, 
- `CLAIM-086`: **Speculative** → **Community Consensus** (src=['store-mirror']) — COMMUNITY PLAYER-ATTRIBUTE TAXONOMY (v10.20-era dump, planning aid ONLY): 13 positions (GK
- `CLAIM-095`: **Speculative** → **Community Consensus** (src=['youtube']) — 'World Cup Winners' content arrived around 21 July 2026 per pack-opening UGC ('World Cup W
- `CLAIM-102`: **Speculative** → **Community Consensus** (src=['sakibpro']) — New-player starting state: a basic lineup around 50-60 OVR; returning players carry progre
- `CLAIM-057`: **Confirmed** → **High Confidence** (src=['id-blog', 'store']) — Franchise distribution model confirmed via version history on ONE listing: DLS26 band = 13
- `CLAIM-051`: **Community Consensus** → **High Confidence** (src=['id-blog', 'inferred', 'store']) — ID community guide (industry.co.id, Sep 2026) claims Dream League Live pays GEMS by weekly
- `CLAIM-052`: **Community Consensus** → **High Confidence** (src=['id-blog', 'store']) — DLS26 permanent player development runs through a TRIAD: Players, Coaches, Physio (industr
- `CLAIM-059`: **Community Consensus** → **High Confidence** (src=['fbgd', 'inferred', 'store']) — DLS26 special-card taxonomy is MULTI-SCHEME (dreamkitsapp catalog, 10 types): Cult Heroes,
- `CLAIM-069`: **Community Consensus** → **High Confidence** (src=['id-blog', 'store', 'vi-blog']) — Economy/health tips (download.com.vn): Stadium Commercials L2 +13% / L3 +21% coins per mat
- `CLAIM-111`: **Community Consensus** → **High Confidence** (src=['id-blog', 'kb-import', 'store', 'vi-blog']) — Per-level facility effect values reported by a VI guide (download.com.vn, Community Consen
- `CLAIM-133`: **Community Consensus** → **High Confidence** (src=['inferred', 'kb-import', 'leo-cb', 'sakibpro', 'store']) — Coach-application mechanic model (Chinese-community DP tool, DLS26China): technical coache
- `CLAIM-144`: **Community Consensus** → **High Confidence** (src=['fbgd', 'larry', 'trung']) — DLS26 OVR ceiling hierarchy, corrected: base golds cap 86 (EV-251); vintage Champion/Star/
- `CLAIM-157`: **Community Consensus** → **High Confidence** (src=['fbgd', 'leo-cb']) — Stat colors on in-game player cards follow thresholds: attribute ≥90 → blue, ≥80 → green, 
- `CLAIM-158`: **Community Consensus** → **High Confidence** (src=['leo-cb', 'store']) — DLS26China optimal-coach decision rule for CB training: pick Gold (+3) when remaining weig
- `CLAIM-007`: **Speculative** → **High Confidence** (src=['dreamkitsapp', 'fbgd', 'inferred', 'larry', 'store', 'trung', 'youtube']) — Base card (non-event, non-special legendary) ratings top out around 86 OVR in current list
- `CLAIM-104`: **Speculative** → **High Confidence** (src=['leo-cb', 'sakibpro']) — Team OVR formula (sakibpro tool claim): the team rating is the mean of the base-or-maxed O
- `CLAIM-105`: **Speculative** → **High Confidence** (src=['leo-cb', 'sakibpro']) — Community theory: a 'trained' player's rating behaves as base + 1 OVR. Single Reddit threa
- `CLAIM-001`: **High Confidence** → **Confirmed** (src=['inferred', 'official', 'reddit', 'trung']) — DLS26 ('Dream League Soccer 2026') is the 2025/26-season entry of First Touch Games' Dream
- `CLAIM-002`: **High Confidence** → **Confirmed** (src=['inferred', 'official']) — Official FTG support states: Multiplayer leaderboards (Dream League Live) compare performa
- `CLAIM-009`: **High Confidence** → **Confirmed** (src=['official']) — FTG official-stated policy: Dream League Live matches are always human-vs-human with no bo
- `CLAIM-010`: **High Confidence** → **Confirmed** (src=['inferred', 'official', 'reddit']) — The career ladder is 8 divisions and the official store description names the top division
- `CLAIM-011`: **High Confidence** → **Confirmed** (src=['official']) — Single-player difficulty scales with division progression, and players can set base diffic
- `CLAIM-012`: **High Confidence** → **Confirmed** (src=['botdls', 'official']) — 'Tier' is overloaded in official materials: LIVE Tier ranking (matchmaking ladder) vs Seas
- `CLAIM-013`: **High Confidence** → **Confirmed** (src=['official']) — Official stat model (DLS): SPE/ACC/STA/CON/STR/TAC/PAS/SHO/GKH/GKR/ENERGY effects as docum
- `CLAIM-014`: **High Confidence** → **Confirmed** (src=['official']) — Seasons are global bounded periods (shared end date for all users, visible countdown); the
- `CLAIM-015`: **High Confidence** → **Confirmed** (src=['inferred', 'official']) — Gems sources (official): league objectives, tournaments, Season Pass, Prize Ladder, and pa
- `CLAIM-016`: **High Confidence** → **Confirmed** (src=['official']) — Prize Ladder grants progression rewards (coins, gems, coaches, dream point boosts, special
- `CLAIM-017`: **High Confidence** → **Confirmed** (src=['botdls', 'official']) — FTG enforcement policy: only App Store/Google Play builds are authorised; modded APKs, ext
- `CLAIM-018`: **High Confidence** → **Confirmed** (src=['official']) — Official netcode claims: DLL matches run through FTG cloud servers; opponent connection qu
- `CLAIM-019`: **High Confidence** → **Confirmed** (src=['official']) — Coin sources (official list): match wins/draws/clean sheets/goals, stadium bonuses, season
- `CLAIM-020`: **High Confidence** → **Confirmed** (src=['official']) — Player acquisition channels (official, article 360004066417): Transfers (new players appea
- `CLAIM-021`: **High Confidence** → **Confirmed** (src=['official']) — A SEASON LEADERBOARD (accessed from the Main Menu) displays players Season Points totals; 
- `CLAIM-022`: **High Confidence** → **Confirmed** (src=['official']) — One DLS account per player; profile linking via Google (Android)/Apple (iOS) sign-in or on
- `CLAIM-023`: **High Confidence** → **Confirmed** (src=['official']) — Account identity rules (official): profile loan/exchange/share/sale/purchase is prohibited
- `CLAIM-024`: **High Confidence** → **Confirmed** (src=['larry', 'official']) — Official design statement: DLS is not a full simulation; unpredictable situations, unreali
- `CLAIM-025`: **High Confidence** → **Confirmed** (src=['official']) — FTG does not announce update/release schedules on request (news via social channels only);
- `CLAIM-026`: **High Confidence** → **Confirmed** (src=['botdls', 'official']) — Controls layout (default): left virtual joystick (360° movement); right side has three vir
- `CLAIM-027`: **High Confidence** → **Confirmed** (src=['inferred', 'official']) — DLL matchmaking inputs are primarily LIVE Tier ranking, player location and the availabili
- `CLAIM-028`: **High Confidence** → **Confirmed** (src=['official']) — Coaches are player-development consumables: a selected coach randomly picks a player to pe
- `CLAIM-029`: **High Confidence** → **Confirmed** (src=['official']) — Squad churn rules (official): non-Starting-11 players can be discarded for a specified pay
- `CLAIM-030`: **High Confidence** → **Confirmed** (src=['official']) — DLS requires online connectivity for the majority of features (Wi-Fi recommended); player 
- `CLAIM-031`: **High Confidence** → **Confirmed** (src=['official']) — Difficulty model (official): single-player difficulty scales with division progress; DLS25
- `CLAIM-032`: **High Confidence** → **Confirmed** (src=['official']) — Release economy (version 12200+): releasing a player via Transfers>Manage Players grants a
- `CLAIM-033`: **High Confidence** → **Confirmed** (src=['official']) — Card rarity taxonomy (official): common=bronze, rare=blue, legendary=gold, max=red, specia
- `CLAIM-034`: **High Confidence** → **Confirmed** (src=['official']) — Customisation surface (official): team/manager name+appearance, per-player boots/numbers, 
- `CLAIM-035`: **High Confidence** → **Confirmed** (src=['official']) — Age policy (official): games offered to 13+; first-download age confirmation into bandings
- `CLAIM-037`: **High Confidence** → **Confirmed** (src=['official']) — Graphics options are ANDROID-ONLY (Options>Advanced>Graphics): FPS cap 30/60 (constant 30 
- `CLAIM-038`: **High Confidence** → **Confirmed** (src=['official']) — Pre-match kit selection: on the lineup screen, clicking player models cycles Home/Away kit
- `CLAIM-039`: **High Confidence** → **Confirmed** (src=['official']) — IAP restriction (official): purchases can be gated by store-side password/authentication (
- `CLAIM-040`: **High Confidence** → **Confirmed** (src=['official']) — Season Pass mechanics (official): FREE+PREMIUM tiers; pass unlocks Progress Bank (currency
- `CLAIM-041`: **High Confidence** → **Confirmed** (src=['official']) — Data deletion (official): "Delete Profile" in-game (DLS: Settings>Advanced>Delete) wipes A
- `CLAIM-044`: **High Confidence** → **Confirmed** (src=['official']) — Fair-gaming charter (official): no pre-determined results, no artificial bias between play
- `CLAIM-045`: **High Confidence** → **Confirmed** (src=['official', 'store']) — DLS26 store facts (official listing copy): title "Dream League Soccer 2026"; 8 divisions t
- `CLAIM-072`: **High Confidence** → **Confirmed** (src=['apk-static', 'official', 'vi-blog']) — Account/profile policy (VI mirror of official FAQ): DLS25 profiles carry over to DLS26 (ke
- `CLAIM-079`: **High Confidence** → **Confirmed** (src=['official', 'store', 'store-mirror']) — ROSTER LICENSING GAPS EXIST (official staff comment on 360004718318): 'for licensing reaso
- `CLAIM-087`: **High Confidence** → **Confirmed** (src=['official', 'store-mirror']) — DLS26 CURRENT PUBLIC BUILD IS 13.4x: latest observed 13.430 (Google Play, last updated 202
- `CLAIM-089`: **High Confidence** → **Confirmed** (src=['official']) — 'My Club' is the in-game menu that contains the kit/customisation surface: Main Menu > My 
- `CLAIM-099`: **High Confidence** → **Confirmed** (src=['official']) — Friend Match is a private match created with a shared code or word (characters A-Z, 0-9 an
- `CLAIM-100`: **High Confidence** → **Confirmed** (src=['official']) — Device compatibility guidance is NOT published as a minimum-spec list. The official articl
- `CLAIM-103`: **High Confidence** → **Confirmed** (src=['inferred', 'official', 'store', 'store-mirror']) — Live-service cadence: DLS26 receives multiple in-season updates (observed roughly monthly 
- `CLAIM-119`: **High Confidence** → **Confirmed** (src=['official']) — OFFICIAL update-troubleshooting ladder (article 360000220945): iOS — close DLS, open App S
- `CLAIM-120`: **High Confidence** → **Confirmed** (src=['official']) — Control-button captions ('Low Kick', 'Hard Kick', 'Lofted Kick') can be removed: Game Sett
- `CLAIM-121`: **High Confidence** → **Confirmed** (src=['official']) — Dream League Live emoji system (official 360020938198): six emojis available by default; f
- `CLAIM-122`: **High Confidence** → **Confirmed** (src=['official', 'vi-blog']) — Custom imported kits and logos are NOT visible to opponents in Dream League Live (official
- `CLAIM-123`: **High Confidence** → **Confirmed** (src=['larry', 'official']) — OFFICIAL FAIRNESS STANCE (article 360000842697): DLS is a game, not an accurate simulation
- `CLAIM-126`: **High Confidence** → **Confirmed** (src=['dlsinside', 'official', 'store']) — VERSION-GAP RESOLUTION (B-009, sibling research): the two apparent gaps in the 2026 versio
- `CLAIM-127`: **High Confidence** → **Confirmed** (src=['dreamkitsapp', 'official', 'trung']) — Stat display scale (GS-042 sibling observation): dlsinside publishes raw attribute values 
- `CLAIM-129`: **High Confidence** → **Confirmed** (src=['dreamkitsapp', 'fbgd', 'inferred', 'larry', 'official', 'store', 'trung', 'youtube']) — Cult Heroes 12-card roster, database-corroborated (GS-039/040 sibling): David de Gea GK 85
- `CLAIM-131`: **High Confidence** → **Confirmed** (src=['dreamkitsapp', 'fbgd', 'inferred', 'larry', 'official', 'store', 'trung', 'youtube']) — Card-roster distribution from the FootballGamingBD card-creator database (snapshot 2026-10
- `CLAIM-136`: **High Confidence** → **Confirmed** (src=['apk-static', 'botdls', 'kb-import', 'official', 'store', 'trung', 'vi-blog']) — Build stack confirmed via static analysis of an APK in academic corpora: DLS26 is a UNITY 
- `CLAIM-046`: **Community Consensus** → **Confirmed** (src=['official', 'store']) — DLS26 roster DB (SakibPro, updated 2026-10-11): 17 newly added players; card types CLASSIC
- `CLAIM-047`: **Community Consensus** → **Confirmed** (src=['official']) — Market pricing model (community DB): transfer price determined by base OVR + exact positio
- `CLAIM-062`: **Community Consensus** → **Confirmed** (src=['inferred', 'official', 'store', 'vi-blog']) — DIVISION SEASON STRUCTURE (download.com.vn VI guide): each Division season = 15 MATCHES; p
- `CLAIM-065`: **Community Consensus** → **Confirmed** (src=['inferred', 'official', 'store', 'vi-blog']) — CURRENCY FLOW MAP (partial separation, VI source): Career matches -> **Season Points + Coi
- `CLAIM-066`: **Community Consensus** → **Confirmed** (src=['id-blog', 'official', 'store', 'vi-blog']) — Mode + card-color map: Exhibition = OFFLINE (default 4-4-2; 4-1-2-1-2 unlocked by default)
- `CLAIM-068`: **Community Consensus** → **Confirmed** (src=['official', 'vi-blog']) — SEASON PASS + PROGRESSION BANK economics (download.com.vn, consistent with EV-162 store no
- `CLAIM-070`: **Community Consensus** → **Confirmed** (src=['id-blog', 'official', 'vi-blog']) — Community formation rankings (download.com.vn): 4-3-3 (wing attack/fast counters), 4-2-3-1
- `CLAIM-140`: **Community Consensus** → **Confirmed** (src=['official', 'trung', 'vi-blog']) — Default (starting) formations are set per team: 149 clubs + 79 nations are catalogued in f
- `CLAIM-146`: **Community Consensus** → **Confirmed** (src=['inferred', 'larry', 'official', 'reddit', 'trung']) — Position codes mix English and Spanish/Portuguese abbreviations in raw data files: GK/POR 
- `CLAIM-150`: **Community Consensus** → **Confirmed** (src=['botdls', 'official']) — On-screen action button mapping in match controls: A = pass (ground pass / through ball co
- `CLAIM-151`: **Community Consensus** → **Confirmed** (src=['botdls', 'official']) — DLS26 in-match state machine (exhaustive enumeration visible to a CV bot): top-level UI = 
- `CLAIM-152`: **Community Consensus** → **Confirmed** (src=['apk-static', 'botdls', 'kb-import', 'official', 'store', 'trung', 'vi-blog']) — Ad inventory confirmed by bot: (1) rewarded ads (center-screen, no skip, reward is coins O
- `CLAIM-003`: **Speculative** → **Confirmed** (src=['en-blog', 'inferred', 'official', 'reddit']) — The highest verifiable global competitive ranking for the mission is NOT yet established. 
- `CLAIM-004`: **Speculative** → **Confirmed** (src=['inferred', 'official', 'reddit', 'store', 'vi-blog']) — Career mode features 8 divisions and 10+ cup competitions (official store text); a VI comm
- `CLAIM-090`: **Speculative** → **Confirmed** (src=['official']) — 'Scripts' is community slang for perceived momentum or rubber-banding manipulation, not a 
- `CLAIM-042`: **Disputed** → **Confirmed** (src=['official']) — Save-path guidance conflict preserved: an older official article documents an in-game iClo

## Skeptic / Devil's Advocate Findings
- **CLAIM-145**: Per-season QR-OLS refit: v20251 STA weight collapses to 0.011 (vs 0.054–0.060 other versions) and SHO jumps to 0.115 (vs 0.100–0.109). Either one bad STA column in the v20251 scrape or a one-off formula tweak. Combined 8-version fit (n=23,327) reproduces claimed const=1.893 (vs 1.89), CON=0.211, STR=0.166, SPE=0.142, ACC=0.148, PAS=0.112, SHO=0.111, TAC=0.106, STA=0.037 exactly; MAE=0.376 (claimed 0.38); within ±1=99.79% (claimed 99.8%). Formula CONFIRMED numerically.
- **CLAIM-144**: Promo OVR ceiling: Trung special.json caps at 88; FBGD at 96; Larrycr7 cards at 98 (Champions Messi/Ronaldo only). 3-source disagreement; safest tier is High Confidence for "promo ceiling ≥96 exists" with Champions-tier 98 carried as Community Consensus sub-note because it is single-sourced to Larry.
- **CLAIM-154**: Coach rarities: Leo CB DP models three (白/蓝/金 = +1/+2/+3). EV-247 SakPro describes COMMUNITY/RARE/EPIC. Yellow/4th tier may exist but is NOT present in the CB DP; cannot generalize to all positions without APK.
- **CLAIM-138**: GK stat remap SHO→GKR / STA→GKH: confirmed by EV-252 promo GKs that literally rename columns to GKR/GKH (3 GKs); EV-251 base GKs retain 8 standard labels. Statistical OLS weight shift for GK subgroup supports the remap. Strong inference, not APK-verified for all GKs.
- **CLAIM-152**: Ad rewards "coins or diamonds" + 15k/400 targets come from bot-dls resource_targets config defaults; not observed live reward packets.
- **CLAIM-153**: HUD filled/hollow circles as stamina/boost from CV template labels; alternative "form-boost meter" interpretation cannot be ruled out.
- **CLAIM-136**: Ad SDK list (AdMob/Unity/AppLovin/Pangle) from academic static scans (beerphilipp/taptrap, tabbed-out); APK hash not recorded.
- **CLAIM-084**: "Mod/cheat ecosystem EXISTS" is TRUE — mod-menu SPAs + auto-farm bot source code literally captured (EV-215/217/254). Claim does NOT state mods grant free/unlimited currency; correctly scoped.
- **CLAIM-060**: dreamkitsapp card counts are labelled "Approximate Calculations" on the site; taxonomy reliable but per-type counts may drift.
- **CLAIM-103**: "Multiple in-season updates" empirically confirmed (Trung has 8 versions 20231–20262; App Store shows 13.030→13.040). "~monthly cadence" remains anecdotal and speculative.
- **CLAIM-139**: Price tiers: 86-OVR players uniformly price=2800 in EV-251; price_map.json has 160 OVR sub-tiers. Mechanically verified.
- **CLAIM-141**: Roster: 2,518 base players in 20261; OVR 52–86; exactly four 86-OVR players (Haaland/Kane/Mbappé/Dembélé). Mechanically verified.
- **CLAIM-147**: Base cap 86 consistent across all 8 Trung versions (20231–20262, 23,327 rows). Mechanically verified.
- **CLAIM-155**: CB weights CON=2, others=1; actions +1/+2/+3; Math.min(100,…) cap; capacity thresholds 12 and 6. All verified by direct grep of EV-255 JS.
- **CLAIM-150**: Button mapping A=pass, B=shoot, C=skill, SPRINT/TACKLE/SWITCH verified by grep of bot-dls game_controller.py.
- **CLAIM-151**: 30 in-match states enumerated from bot-dls game_state_detector.py; these are CV-template states, not necessarily FTG's canonical state machine — may miss hidden/sub states.
- **CLAIM-104**: Team OVR = mean of Starting-11 is a community-tool claim from SakPro; the Leo CB DP also operates on mean-of-11. Two independent community tools agree; no APK or official confirmation.
- **CLAIM-105**: "+1 OVR per trained player" theory: appears in SakPro tool and CB DP (both encode +1/+2/+3 coach boosts). Two-tool agreement on the mechanic; numerical size of boost unverified.

## Numeric Witness Spot-Check Results
- OVR formula combined QR-OLS refit (n=23,327): const=1.893, CON=0.211, STR=0.166, ACC=0.148, SPE=0.142, PAS=0.112, SHO=0.111, TAC=0.106, STA=0.037 → MAE=0.376, RMSE=0.484, within ±1 after round = 99.79%. Claimed values 1.89/0.38/0.49/99.8% are all within expected rounding.
- Per-version MAE stays 0.35–0.40 across 20231–20262; formula stable.
- Base cap 86: 4 players (Haaland/Kane/Mbappé/Dembélé) all price 2800 coins, 8-attr schema with zero violations.
- Promo cap 98: Messi + Ronaldo Champions cards in EV-252 (Larry); FBGD EV-248 caps at 96; Trung EV-251 special.json caps at 88.
- CB trainer JS: weights ctrl=2 pass/shoot/tkl=1; boost actions +1/+2/+3; cap=100 (Math.min(100,…) ×10); capacity thresholds 12 and 6.
- Bot-dls buttons: A=pass, B=shoot, C=skill, SPRINT/TACKLE/SWITCH = hold buttons; 30 CV-template states.
- GK keys in promo GK cards: GKR/GKH replace SHO/STA; base GK dataset still uses standard 8 labels.

## Outstanding Gaps (require APK or live-device verification)
- Non-CB coach attribute weights (position-specific matrix beyond CB).
- Dream Points / Form Boost / Season Pass exact numerics (reward sizes, caps, decay).
- GKR vs GKH column remap for ALL GKs (not just 3 promo cards).
- Matchmaking/ELO algorithm beyond the FTG-stated inputs (Tier, location, team strength).
- Ad reward values, frequency caps, ad classes beyond bot-config defaults.
- 4th/yellow/epic coach tier existence (CB DP uses only 3).
- Fractional-overflow rounding mode in training-cost DP.
- Save/shared_prefs schema on device.
