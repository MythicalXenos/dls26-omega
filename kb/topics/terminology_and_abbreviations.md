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
