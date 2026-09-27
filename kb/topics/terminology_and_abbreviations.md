# TERMINOLOGY & ABBREVIATION RESOLUTION

Per PROMPT.md §1: abbreviations in the prompt are shorthand carried over from a conversation, **not** established DLS26 terms. Each must be resolved to the game's exact terminology during the Step 1 sweep and recorded here; the game's term is used in anything addressed to the user, the shorthand only in internal files. The prompt's use of a term is never evidence about the game.

Non-game abbreviations need no research: PR = pull request, ADB = Android Debug Bridge, APK = Android package, ToS = terms of service, KB = knowledge base.

**Status: UNRESOLVED — resolution owed by STATE_1_RESEARCH_SWEEP.** Nothing below may be filled from recall.

## Game abbreviations to resolve

| Shorthand | Candidate expansion | Resolved in-game term | Source (S-id) | Confidence | Volatility | Status |
|---|---|---|---|---|---|---|
| DLL | Dream League Live | **Dream League Live** — FTG's own store copy: "Dream League Live puts your club against the very best in the world... compete in Global Leaderboards and Events for exclusive prizes!" | S-0011 | Speculative (gate-capped: single source; origin DIRECT/checkable) — first-party listing | volatility-Frozen (a mode name changes only with a major version or FTG-stated replacement) | RESOLVED 2026-09-27 |
| OVR | overall rating? | | | | | UNRESOLVED |
| GK | goalkeeper? | | | | | UNRESOLVED |
| XI | starting eleven? | | | | | UNRESOLVED |

## Undefined game terms used by the prompt — each must be resolved to the actual mechanic

| Term as used in the prompt | What the prompt implies | Actual DLS26 term & mechanic | Source (S-id) | Confidence | Volatility | Status |
|---|---|---|---|---|---|---|
| prize ladder | a progression track yielding a special player | **RESOLVED — "Prize Ladder" IS an official FTG term.** FTG's App Store in-app-event copy for the LIVE event "English League Classics": "Relive the glory days – Unlock top players and claim big rewards in our this new Prize Ladder." "this new Prize Ladder" implies a recurring event format. Mechanics (accumulation, milestones, rewards, reset) NOT established. | S-0015 | Speculative (gate-capped: single origin = FTG; origin DIRECT) | volatility-Critical | TERM RESOLVED 2026-09-27; mechanics OWED — see kb/topics/prize_ladder_and_current_events.md |
| special card / special player | a non-standard player card | Official term is **"Special Players"** (FTG changelog: 'New Special Players - "Cult Heroes" collection'). Non-official card-family names in circulation, all unverified: "Legendary Agent", "Dynamic Stars", "Classic Icons", "Classic greats". | S-0012 (official changelog); S-0013/S-0014 (sakibpro, incentivised) | Speculative (gate-capped: single source; origin DIRECT/checkable) that "Special Players" is FTG's term; Speculative for everything else | volatility-High | PARTIAL — official term RESOLVED, card families OWED |
| base OVR | a card's starting rating | | | | | UNRESOLVED |
| rotation | two XIs switched by a decision tree | No official term found yet. Adjacent verified systems that rotation research must interact with: **daily scenarios**, **Dream Draft**, **Dream League Live**, **Clan system**, and the match-fitness/recovery systems (Medical facility is named officially; its effect is not established). | S-0011 | Speculative | volatility-High | OPEN |
| coaching state | which coaches have been applied to a player | Partially resolved from official changelog text: **Coaches** develop "technical and physical abilities" (S-0011/S-0015) and **Special Coach Packs** exist ("Develop your favourite players more easily", S-0017). Categories, rarity, yields and caps unknown. | S-0011, S-0017 | Speculative (gate-capped: single origin; DIRECT) | volatility-High | PARTIAL |
| reset cycles | repeating a coaching/stat process | No official term found. Related official mechanic discovered: **Player Recovery** — "Changed your mind? Buy a sold player back within a limited time" (S-0017), which is a reversal mechanic for sales, not for coaching. Whether any coaching/stat reset exists is unknown. | S-0017 | Speculative | volatility-High | OPEN |
| breakpoints | thresholds where a stat's effect changes | | | | | UNRESOLVED |
| matchup matrix | formation-vs-formation outcomes | | | | | UNRESOLVED |
| gameplans | tactical presets | | | | | UNRESOLVED |
| touch patterns | how often/where a position receives the ball | | | | | UNRESOLVED |
| facilities | upgradeable club buildings | FTG official games page mentions "team customisations" broadly (S-0002) — marketing copy, not a mechanic source | S-0002 | Speculative | volatility-High | UNRESOLVED |
| ceiling | a player's maximum potential (game term) vs upper bound of a list (not a game term) | No official term found yet. Non-official candidate in circulation: "Max Ratings" (sakibpro event-guide framing, incentivised source). SakibPro also runs an "Upgrade Simulator" tool, which implies a computable growth path — its model is a research target, not evidence. | S-0013 | Speculative | volatility-High | OPEN |
| bonus development | extra stat growth from some mechanic | No official term found. Candidate official phrasings in circulation: "**boosted attributes**" (Cult Heroes event card, S-0015) and "develop your players **more easily**" (Special Coach Packs, S-0017). Neither is established as a mechanic. | S-0015, S-0017 | Speculative | volatility-High | OPEN |
| division | league tier | **8 divisions**, top one named the **Legendary Division**; plus "more than 10 cup competitions" | S-0011 (official Play listing) corroborating S-0002 (FTG site) | Speculative (gate-capped: ONE origin — FTG — appearing on two first-party surfaces, which is not two independent sources; checkable origin = the listing); Speculative for promotion/relegation mechanics | volatility-Low for the count; volatility-High for mechanics | RESOLVED (name+count) 2026-09-27; mechanics OWED |
| season points | points accumulated within a season | No official term found yet. Officially confirmed adjacent structures: "regular **seasons** and events", a paid **Season Pass** ($3.99 US, S-0017), "**Global Leaderboards and Events**" inside Dream League Live, "**daily scenarios**", "**Dream Draft**", and **Prize Ladder** event tracks (S-0015). What accumulates, and what resets, is unknown. | S-0011, S-0015, S-0017 | Speculative | volatility-Critical | PARTIAL |

Where research shows a prompt term corresponds to nothing real, or to something different from what the words suggest, the research wins: correct it here, note the correction against PROMPT.md per IF THIS PROMPT IS WRONG ABOUT THE GAME, stop treating the term as a game fact, and keep following any framework rule that used it under the verified terminology.

## Newly resolved official terms this session (all Speculative, gate-capped; origin DIRECT)

| Official term | Where it appears | Source |
|---|---|---|
| **Dream League Live** | mode name; resolves the prompt's shorthand DLL | S-0011, S-0015 |
| **Prize Ladder** | event structure; resolves the prompt's shorthand "prize ladder" | S-0015 |
| **Special Players** | card family; FTG changelog wording | S-0012 |
| **Cult Heroes** | live Special Players collection, "boosted attributes", window ends 10/14 | S-0015, S-0016 |
| **English League Classics** | live event described as "our this new Prize Ladder" | S-0015 |
| **Coins** / **Gems** | the two purchasable currencies, from IAP product names | S-0017 |
| **Season Pass** | paid seasonal track, $3.99 US | S-0017 |
| **Player Recovery** | buy a sold player back within a limited time | S-0017 |
| **Special Coach Packs** | coaching consumable pack | S-0017 |
| **Coaches** (technical / physical) | "Use Coaches to develop your players technical and physical abilities" | S-0011, S-0015 |
| **Stadium / Medical / Commercial / Training facilities** | the four officially named facility categories | S-0011, S-0015 |
| **Agents** / **Scouts** | "Recruit Agents and Scouts to help identify top talent in the transfer market" | S-0011, S-0015 |
| **Clan system** | "all-new"; team up, achieve goals, win rewards | S-0011, S-0015 |
| **Dream Draft** / **daily scenarios** | "Challenge yourself in daily scenarios and Dream Draft!" | S-0011, S-0015 |
| **Legendary Division** | the top of 8 divisions | S-0011, S-0015 |
| **Classic greats** | "4,000+ FIFPRO licensed players and legendary Classic greats of the game" | S-0011, S-0015 |
| **Loot Boxes** | Apple's content declaration for the app's randomised purchases | S-0017 |

## Stat-code vocabulary — PROMOTED to High Confidence for the English display set (R-0003); values still gated separately

**Tier change 2026-09-27 (logs/revision_register.md R-0003):** the English eight-stat display set is no longer a third-party claim. An in-game capture posted to r/DreamLeagueSoccer (saved at `kb/evidence/reddit_cult_heroes_isco_signed_en.jpg`, S-0025) shows the live client displaying exactly **SPE 81, ACC 87, STA 79, STR 65, CON 93, PAS 86, SHO 81, TAC 53** on a signed Cult Heroes card — the same eight codes SakibPro's card pages and simulator use. Two independent sources, documented independence, checkable origin ⇒ **High Confidence** per Mechanism 5. Individual VALUES remain gated on their own (the capture's octet is single-origin ⇒ Speculative with origin DIRECT).

**NEW from the same evidence: stat codes are LOCALIZED.** A second capture of a SPANISH client (`kb/evidence/reddit_cult_heroes_dybala_signed_es.jpg`, screen headed "JUGADOR FICHADO") displays **VEL, ACE, FON, POT, CON, PAS, DIS, ENT** for the same eight slots. Self-evident mappings: VEL=SPE, ACE=ACC, CON=CON, PAS=PAS. Inferred (recorded as inference): FON=STA (fondo), POT=STR (potencia), DIS=SHO (disparo), ENT=TAC (entrada). **Consequence for the sweep: every non-English community source speaks its own stat-code dialect, and cross-language comparisons must map codes first.** es is one of the client's 15 official languages, so this is the expected pattern, not an anomaly.

Recovered from a card page whose prose pairs names with codes ("reactions (85 GKR)", "handling (80 GKH)") and from the simulator's coach groupings (S-0020):

| Code | Stat name | Grouped under (per the third-party simulator) |
|---|---|---|
| SPE | Speed | Fitness Coach |
| ACC | Acceleration | Fitness Coach |
| STA | Stamina | Fitness Coach |
| STR | Strength | Fitness Coach |
| CON | Control | Technical Coach |
| PAS | Passing | Technical Coach |
| SHO | Shooting | Technical Coach |
| TAC | **Tackling** — NOT "Tactics". Confirmed in-game (S-0025) | Technical Coach |
| GKR | Reactions (goalkeeper) | Goalkeeping Coach |
| GKH | Handling (goalkeeper) | Goalkeeping Coach |

A goalkeeper row displays 8 stats — SPE, ACC, STR, CON, PAS, TAC, GKR, GKH — where the outfield set is SPE, ACC, STA, STR, CON, PAS, SHO, TAC: **Stamina and Shooting are replaced by the GK pair**. "OVR" is the overall rating and a GK row's eight displayed stats summed to a "Total" (503 in the example). Whether the game itself displays a stat total, and whether OVR is computed from these eight values, is UNKNOWN — a third party's display is not the game's formula, and the formula must never be assumed from another game.
Status: the code→name MAPPING is resolved as a hypothesis with strong internal support (two pages of one source agree, and the names are ordinary football attributes). Every VALUE remains unverified. The source that produced this mapping has had its authority over numbers withdrawn (DR-001), and its own page flags the OVR as "⚠️ ESTIMATED".

## Additional terms encountered this turn

| Term | Meaning as used | Provenance | Status |
|---|---|---|---|
| **Cult Heroes Agent** | the stated exclusive acquisition route for Cult Heroes special cards | third-party card page (S-0021) | OPEN — FTG officially names "Agents and Scouts" (S-0011/S-0015), so an agent-mediated acquisition is consistent with official vocabulary, but no FTG source names a "Cult Heroes Agent" and its cost/randomness is unknown. Gap G-0026 |
| **SPECIAL EDITION** | a flag on special cards | third-party (S-0021) | OPEN — plausible echo of FTG's "Special Players"; not confirmed |
| **Max Upgrade (+10 OVR)** | a card fully developed by coaches | third-party (S-0020/S-0021) | OPEN — resolves the SHAPE of the prompt's "ceiling" term; every value unverified. Gap G-0017 |
| **Cult Heroes 2018** | a year-stamped card variant ({family} {year}) | third-party (S-0021) | OPEN as a convention, but it CORROBORATES FTG's own "Frozen in time from their peak years" (S-0016) from an independent direction |
| **Position Proficiency** | a section on card pages, content unknown | third-party (S-0021) | OPEN — bears directly on the user's "no position locking" statement and their 3-2-3-2 / 3-1-4-2 shapes. Gap G-0027 |
| **Free Agent** | a club value for players unattached to a club | third-party (S-0021) | OPEN — ordinary football usage; whether DLS26 uses it as a literal club label is unconfirmed |
| **Development Weight** / **progression capacity** | the budget a player's upgrades draw down | third-party (S-0020) | OPEN — no official echo |
| **Coaches Wasted** | a cost readout implying coaches can be spent with poor result | third-party (S-0020) | OPEN — no official echo; connects to the prompt's unresolved "reset cycles" and to a possible failure/overflow mechanic |

## Screens and panels now directly observed in-game (S-0025) — High-tier evidence that they EXIST; their mechanics stay gated

| Observed label | What it is | Locale seen |
|---|---|---|
| **PLAYER SIGNED** / **JUGADOR FICHADO** | the confirmation modal shown when a player is signed, with confetti, the stat octet and the card | en / es |
| **LIVE TRANSFERS** | a screen/panel listing transfer targets, containing a **CULT HEROES** subsection (three card thumbnails visible) and a second subsection labelled "MEJOR CALIFICADOS" in the capture | en heading, es subsection in the same frame — recorded, not interpreted |
| **SCOUTS** | a right-hand panel with thumbnails — FTG's officially named Scouts, now seen as a real panel | en |
| **AGENTS** | a right-hand panel with thumbnails — FTG's officially named Agents, now seen as a real panel; the strongest in-game confirmation yet of the "Cult Hero Agent" acquisition route | en |
| **MANAGE PLAYERS** | a button, bottom right | en |
| two currency counters | top bar, reading "5.177" and "3.214" with distinct icons — consistent with the officially purchasable Coins and Gems, but **which counter is which is NOT determinable from the capture** and is not asserted | numeric, European thousands separator |
| "**Live Transfers will refresh with new players after completing 1 match.**" | an in-game rule caption, quoted verbatim | en |

Also observed on the cards themselves: a green circular OVR badge, a gold **year banner** on the card face (2020 on Dybala, 2017 on Isco — promoted to High Confidence that special cards carry a year stamp, R-0003), the player name, a national flag, a **position badge that localizes** (AM in the English client, SD in the Spanish client for the second-striker/attacking-midfielder roles), and a red star at the card's foot. Un-maxed Cult Heroes cards show a gold/cream frame with a rainbow-gradient upper band; the claimed "black card" maxed state remains unobserved (G-0030).

| **Dream Points (DP)** | the Prize Ladder's progression currency, earned by playing matches; cumulative; tiers and milestones | third-party guide (S-0026), single origin | OPEN as official terminology — FTG's own event copy says "claim big rewards in our this new Prize Ladder" without naming a currency; DP is the community/guide name until FTG or the client confirms it. The user's ladder screen will show the real name |
| **milestone / tier** (ladder) | cumulative-DP thresholds at which rewards unlock (62.5k/115k/175k/250k per one guide) | third-party guide (S-0026) | OPEN — values Speculative |
| **Version {year}** on Classic cards | year stamp on ladder/Classic cards (Essien "Version 2006"; Cult Heroes cards 2017-2026) | guide (S-0026) + in-game captures (S-0025) | the year-stamp mechanic is High Confidence (R-0003); per-card years gated individually |

| **Dream Points / Dream League Points (DP)** | the ladder currency; two names in circulation (dlskiturl "Dream Points", bluestacks "Dream League Points") | guides (S-0026/S-0031) | NAME UNRESOLVED between variants; the user's ladder screen settles it |
| **DP Boost (Common/Rare/Legendary)** | timed multipliers on DP earnings, bought with gems (+50%/25 gems/3 matches; +75%/35 gems/5; Legendary exists) | Reddit users Jan+May 2026 (S-0031) | OPEN — prices version-sensitive |
| **Season Points** | Career Mode match reward alongside Coins, scaling with division | bluestacks (S-0031) | OPEN — candidate official referent for the prompt's shorthand "season points"; single source |
| **Progression Bank** | accumulates Coins+Gems from DLL XP over a 10-day season, paid at season end | bluestacks (S-0031) | OPEN — single source (G-0045) |
| **Global Challenge Cup** | a named competition | bluestacks (S-0031) | OPEN — single source |

| **Legendary DP Boost** | top boost tier: +150% for 125 gems over 8 matches (price High Confidence, R-0007; multiplier/duration Speculative) | two Reddit threads, Jan 2026 + current clan thread (S-0031/S-0033) | PARTIAL |
| **"Prize Ladder points"** | a third community name for DP (Jan-2025 thread) | Reddit (S-0033) | NAME QUESTION WIDENS: Dream Points / Dream League Points / Prize Ladder points; the user's ladder screen arbitrates |
| Dream Draft | Game mode | Draft 18 players (all 75+ plus a star player), tournament structure vs CPU-tier opponents, gem prizes; pays the same DP as Dream League Live per the Dec-2024 FTG capture (185 max) — a third DP grind mode between Career and DLL in difficulty | gamingonphone guide + FTG capture, Dec 2024 (S-0035/36) | Speculative |
| SP (Season-Pass points) | Currency | Third match-reward column (100/10/5 per career win/goal/clean sheet in Dec-2024); pass banner shows running SP total (195 in Jan-2026); pass objectives also pay DP | FTG captures Dec-2024 + Jan-2026 (S-0036) | Speculative |
| World Cup Classics / Midfield Classics / English League Classics | Live-ops cycle names | Prize-ladder cycle banner themes: Dec-2024, Jan-2026, and current Sep-2026 respectively | FTG banner text in captures (S-0036) + earlier sweeps | High Confidence for existence of the three names; cycle ordering Speculative |
| Physio | Item | Consumable used by a weekly challenge ('Use 1 Physio'); presumably heals injuries; system undocumented | FTG challenges capture Dec-2024 (S-0036) | Speculative |
| Team Recovery | Mechanic | Post-match button offering '+10%' team recovery next to CONTINUE in a Jun-2024 capture; relation to Physio unknown | reddit capture via S-0036 | Speculative |
| Bronze Cup / Global Challenge Cup | Competition names | Cup hierarchy panels on the DLS26 home screen: Global Challenge Cup (group stage vs e.g. Cornella) and Bronze Cup (round 1); presumably a ladder of cup tiers by team rating | DLS26 home capture Jan-2026 (S-0036) | Speculative |
| Academy Division / Legendary Division | Career division names | Lowest and a top career division respectively, each 15 games ('GAME 1 OF 15', 'GAME 11 OF 15'); standings show real club names (Heerenveen, Charlton, Oxford, Hearts) | FTG captures Dec-2024 + Jun-2024 (S-0036) | Speculative |
