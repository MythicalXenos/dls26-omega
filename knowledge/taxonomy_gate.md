# Taxonomy gate ledger (Step 1 → Step 2 gate)

**Purpose:** the prompt's MANDATORY CORE GAMEPLAY TAXONOMY GATE. Step 1 exhaustion cannot be declared and Step 2 cannot begin until each dimension below is answered either by a positive, sourced finding or by an exhaustively-searched-and-documented open gap. This ledger records, per dimension, **what is sourced, at what tier, and what is still open**. It is a status document, not new research; every claim cited here lives in `knowledge/knowledge_base.md` or `knowledge/topics/`.

**Updated:** 2026-10-03 (Turn 9), session `arena/01a1022d-dls26-omega`.
**Tier key:** Confirmed / High Confidence / Community Consensus / Speculative / Disputed — as recorded at the cited location; nothing is upgraded by being listed here.

---

## Dimension 1 — How a player's ratings are developed, and what limits that

**Sourced:**
- Two currencies appear in the upgrade path debate: coaches are the development instrument (FTG's own store copy: "Use Coaches to develop your players technical and physical abilities", `knowledge/knowledge_base.md`, Play US listing direct fetch). **Tier:** existence, Speculative→High-in-progress (first-party copy; mechanics unverified).
- A four-coach-type model (Fitness / Technical / Special / Goalkeeping × Common/Rare/Legend, gem prices 15/40/150 → 90/240/400) from one third-party tool with withdrawn authority. **Tier: Speculative**, capped by a single origin. Source: `knowledge/topics/coaching_and_upgrade_system.md` §1.
- A progression model claiming a **100% development-weight budget = +10 OVR ceiling**, with attribute costs differing (CON/SPE expensive, STA cheap), and a GK variant (22 points at 2.2 points per +1 OVR). **Tier: Speculative**, same single origin; internally self-consistent (22 ÷ 2.2 = 10). Source: same file §2.
- A facility discount on coaching cost in six steps (0/5/10/15/20/30%). **Tier: Speculative**, same origin. Source: same file §3.
- Special/event cards: a database FAQ claims they can be coached "+10 over base" into "maxed-out black cards". **Tier: Speculative** (database boilerplate; repeated site-wide — flagged for incentive screening).

**Open:** whether the +10 ceiling applies to special cards; whether the coach-selection step is a "pick 1 of 3, +2, discard & reshuffle" gamble and what a reshuffle costs; what a Common/Rare/Legend coach actually yields; whether coaching is reversible/resettable (the prompt's "reset cycles" term — no game mechanic established yet); GK stat-label inconsistency (GKH vs GKP) recorded, unresolved.
**Datamining flag:** all coach/ceiling values are **pending datamining confirmation** (client definitions would settle them in one pass; blocked on APK acquisition → G-0004).

## Dimension 2 — Currencies: what exists, what each buys, how spending compounds

**Sourced:**
- **Coins** and **Gems** are FTG's own currency names (IAP product names: Bundle/Stack/Cup of Coins; Bundle/Stack/Locker of Gems; US list $1.99–$16.99). **Tier:** existence High (first-party storefront), amounts unknown.
- **Dream Points (DP)** — the prize-ladder progression currency, earn-only, paid by matches; **DLS Live (online) pays significantly more DP than Career** (multiple sources incl. one official); DP is claimed purchasable with Coins AND Diamonds in one addendum (unreconciled with the earn-only framing — open). Sources: `knowledge/topics/economy_currencies_and_iap.md` (§ DP economy addenda), `knowledge/topics/prize_ladder*.md`.
- A price formula for base-card transfers with a verified anchor (86 CF = 2,970) and a 20-of-24-cell two-source grid; one crossed-price collision found (83 CB = 82 CM = 2,085). **Tier:** the anchor and grid cells are Speculative→Community-Consensus-track with two independent operators; the formula is third-party-derived.
- Facility set: **seven facilities**; stadium/commercial/medical/training named officially; upgrade-order consensus from community. **Tier:** Speculative.
- Gem-income model for a 10-day season from one user's accounting; ad-doubling of post-match coins (community). **Tier:** Speculative, single user.

**Open:** coin amounts per IAP tier; whether DP can genuinely be bought (and with what); whether **boost carry-over** between ladders exists (open community question — matters for stockpiling advice); exact coach cost currency (gems per the tool model, but a Play review alleges a coin-side fee — unreconciled); what compounding "spending" the prompt asks about looks like across facilities.

## Dimension 3 — Recurring reward / progression tracks: how they accumulate and reset

**Sourced:**
- **Prize Ladder** is FTG's own term; the current cycle is **English League Classics** (launch dated 6–7 Sep 2026 from FTG's own social announcement). Milestones at 62,500 / 115,000 / 175,000 / 250,000 DP; rewards include coins, gems, coaches and **special agents**. **Tier:** structure Speculative→converging; launch date first-party.
- **Season Pass**: dual-track (free + premium) claimed; premium "adds faster Dream Points earning" (first-party changelog text); a **Progression Bank** inside the pass (community); a **Bank-claim gate** reported (dual-sourced per import). **Tier:** Speculative.
- **Dream Draft** (1 free + 2 paid per cycle claimed), **Online Events** (DLS Live section), **Clans** (rewards + leaderboards), **daily/weekly challenges**, **daily login reset rule**, **12th Man community vote**. **Tier:** existence mixed; mechanics mostly Speculative.
- Cycle-length mechanisms on record: 90-day ladder cycle (screen-observed on a prior ladder), 10-day season pass/gem model, 28-day event (Cult Heroes). **Tier:** Speculative.
- **Open/unresolved:** the "Ends on 10/14" storefront lead — reading (A) 28-day Cult Heroes event end vs reading (B) ladder end; the in-game timer settles it.

**Open:** reset/rollover rules per track; what happens to unclaimed milestones; whether event windows and pass windows align; the ladder-end date question above.

## Dimension 4 — How match conditions change player performance over a match

**Sourced:**
- FTG's own stat article (fetched in a prior session; page-age 2021) names the stat set and qualitative effects — SPE/ACC/STA/CON/STR/TAC/PAS/SHO + GKH/GKR + ENERGY — including energy depletion, a halftime boost, and performance declining as energy falls. **Tier:** Speculative (single FTG article, older era; current-build applicability unverified).
- The imported KB records stamina as having real in-match effect and marks the precise rates as open (G-0019-class gaps; see `knowledge/topics/gameplay_systems_inventory.md` and the coaching file's stat notes).
- Community: input/pass-assist and cursor-switching complaints (ownership/behaviour, not conditions). **Tier:** user-generated.

**Open:** actual energy/stamina drain rates, halftime recovery value, whether the +10 coaching STA investment changes match duration materially; substitutions/recovery systems (**no healing/recovery item inventory yet**); the interaction of rotation with energy.

## Dimension 5 — How positioning, formations and control settings change outcomes

**Sourced:**
- Position vocabulary and codes exist in the database (GK/CB/LB/RB/DM/CM/AM/LM/RM/LW/RW/CF/SS etc.); the prompt's position-locking question is **user-stated as no locking**, with an imported **DLS21-era community precedent** consistent with it and **no DLS26-specific confirmation yet**. **Tier:** user-stated + franchise-continuity precedent (not usable as verified).
- Controls: the toggle set exists — imported notes describe **Auto-Switch / Kick Assist / Cross Assist** behaviours with community guidance; the user's Kick Assist and Cross Assist are off. **Tier:** Speculative.
- Formations: user's 3-2-3-2 preferred, 3-1-4-2 unlocked, 4-4-2 dropped (user-stated). No formation-effect research captured yet.
- Match AI complaints on record (players out of position, cursor delay) — user-generated.

**Open:** whether DLS26 has any position-based penalty or proficiency mechanic (must be verified, not assumed); what each formation does mechanically; the full toggle list and each toggle's effect; mid-match switching behaviour.

## Dimension 6 — Any further gameplay subsystem

**Sourced (existence, mostly first-party copy):** Divisions (8 + Legendary) and 15-game division seasons; 10+ cup competitions (Global Challenge Cup, Bronze Cup observed); Facilities (7); Agents and Scouts (panels observed in-game); Transfer market incl. Live Transfers (refreshes after completing 1 match — in-game caption); Clan system; Dream League Live (divisions, leaderboards, events); Daily Scenarios; Dream Draft; Fanzone and World Tournament (single third-party origin, no official echo). **Tier:** existence mostly Speculative→High-in-progress; mechanics largely open.

**Open:** every mechanic behind those systems (costs, rates, resets), plus discovering subsystems no source has named yet (the dimension is deliberately open-ended).

---

## Gate status

- **Dimensions 1–6: none is closed yet.** Each has sourced material and named open sub-questions. Under the gate's own rule, a dimension is satisfied by a sourced finding **or** by an exhaustively-searched, documented open gap — so the remaining work is (a) fill the cheap gaps (mostly the in-game checks the user can settle in seconds), and (b) write exhaustion evidence per dimension (Mechanism 1) once the sweep's coverage is complete.
- **Thinnest coverage:** dimension 4 (in-match conditions) — the only substantive source is one older FTG article plus the imported stat notes; it needs a DLS26-version source.
- **Cheapest lever for the user (batched into the Step-5 ask):** the coaching screen (coach types, rarities, prices, the +10 ceiling, whether special cards can be coached), the ladder screen (timer + DP total + milestone labels), and the currency balances. Three screenshots would move most of dimensions 1–3 from Speculative to user-stated or better.
- **Step 2 remains blocked** from beginning until this ledger's dimensions are either sourced or carry documented exhaustion of the search (patches aside, per PATCH RESPONSE).

---

## Turn 10 update (2026-10-03) — dimension 4 leads + official source spine

- **Dimension 4 (in-match conditions):** still the thinnest, but no longer empty. New leads (all Speculative): **Physios** as the energy/injury recovery system (coins, Common/Legendary tiers), **Medical Centre** (injury chance + recovery cost), **Training Centre** (unlocks formations + player form). Source: one stale emulator-vendor guide (2021 page age) plus a content-farm echo. **Officially confirmable:** the FTG FAQ article "How do the various player stats in DLS affect gameplay?" (already fetched, 2021-era) is the only first-party source; no first-party article on energy, stamina, substitutions or injuries was found in the 30-article index — that absence is now itself a finding to record in the exhaustion declaration.
- **Dimension 1 (development):** weak third-party corroboration of the four-coach-type model (Technical / Fitness / Goalkeeping / Special) from the same stale guide. Still Speculative; still pending datamining.
- **Dimensions 2–3 (currencies, tracks):** the official article index supplies four directly relevant first-party articles — **What is the Season Pass?**, **What is the Prize Ladder?**, **What are Dream Point Boosts?**, **How do I earn coins in the app?** (+ "Is it possible to earn free coins?"). These are the cheapest promotion path for those dimensions and are queued as the next official fetches.
- **Gate status unchanged:** no dimension closed; Step 2 still blocked. The official backlog (9 mechanism-relevant FTG articles) is now the highest-value queued retrieval block.

---

## Turn 11 update (2026-10-03) — official first-party block fetched (four articles + version history)

**Dimension 2 (currencies, what they buy):** FTG's own coin-source list captured (winning, drawing, clean sheets, goals, **stadium bonuses**, season objectives, pass rewards, ladder rewards, final league positions, cup wins, **watching video clips**). Prize Ladder reward set confirmed first-party: coins, gems, coaches, **dream point boosts**, special players. DLL XP named as the Progress Bank driver (DLL = Dream League Live, multiplayer). **Remaining open:** rates, gem sources (article "How can I get Gems?" queued), whether DP itself is purchasable with gems/coins (imported claim, unreconciled).

**Dimension 3 (recurring tracks — how they accumulate and reset):** substantially strengthened by first-party evidence:
- Season Pass: two tiers, **Season Points earned from completing matches (amount varies by game mode)**, tier locks advance **one day at a time**, premium removes locks, late purchase still unlocks everything if points are earned, **Progress Bank pays at season end based on DLL XP**, season end shown on a countdown for everyone.
- Prize Ladder: DP from matches, rewards at milestones, DP Boosts purchasable inside the ladder and applicable to career/Draft/scenario/DLL only.
- **Boost carry-over RESOLVED first-party:** unused DP Boosts persist into the next ladder.
- **Remaining open:** exact reset rules for unclaimed ladder milestones, whether the ladder and pass seasons share boundaries, gem-income rates, and the still-unsettled storefront "Ends on 10/14" reading (event vs ladder).

**Dimension 6 (further subsystems):** **Fanzone confirmed as a facility by first-party text** ("Upgrade your Fanzone for Clan bonuses and Stadium discounts", v13.410 notes) — previously only a third-party event name. **World Tournament** confirmed as a first-party event type. **Dynamic Stars** confirmed first-party with a mechanic description worth following ("upgrading live with national team performances").

**Dimension 1 (development):** unchanged this turn (still needs the coaching screen or the client).

**Dimension 4 (in-match conditions):** unchanged this turn; still the thinnest.

**Gate status:** dimensions 2 and 3 are now the strongest (first-party mechanics + imported community models converging); 1 and 4 remain the thinnest. Still no dimension closed; Step 2 still blocked.

## Turn 12 update (2026-10-03) — official block part 2

**Dimension 2 (currencies):** gem sources now first-party (league objectives, tournaments, Season Pass, Prize Ladder, Dream League Live participation, shop purchase; quantities vary). Free coins = video clips, explicitly "(subject to availability)" — matches the user's ad loop. Remaining open: rates, and whether DP/agents are gem-purchasable.

**Dimension 3 (tracks/resets):** ladder special players confirmed first-party ("awards special rare players when the criteria is met"); transfer pool refresh cadence confirmed (per in-game week / after each single-player match). Remaining open: exact unclaimed-milestone reset behaviour; ladder↔pass season alignment (weak lead: a DLS25-era British Classics ladder ended the day before the version switchover).

**Dimension 1 (development):** unchanged (needs client/coaching screen).

**Dimension 4 (in-match conditions):** touched, not closed: **difficulty in single-player is division-driven, with a base Medium/Hard setting from DLS25**; DLL is stated to be bot-free with no difficulty manipulation. Energy/stamina/physio leads remain stale-vendor-only. Still the thinnest dimension alongside dim 1.

**Dimension 6 (further subsystems):** DLL matchmaking article and Core Principles page queued (still unfetched). Blocked-player article queued.

**Gate status:** dimensions 2–3 first-party-strong but not closed (rates/resets open); 1 and 4 thinnest. Step 2 still blocked.

## Turn 13 update (2026-10-03) — official block part 3; official article set effectively complete

**Dimension 3 (tracks/resets):** **clan points are earned through matches, challenges and season passes** — a third parallel accumulation track alongside Season Points and DP, first-party. Remaining open: ladder reset/allocation rules, exact season boundaries.

**Dimension 4 (in-match conditions):** still thinnest, but stronger first-party naming of variables: **weather, ball spin, stadium influence, formation, pitch positioning, development profile** (Core Principles, portfolio-level — lead only). DLL difficulty controls explicitly denied; single-player difficulty still division-driven with a Medium/Hard base setting.

**Dimension 6 (further subsystems):** clan system documented (one clan, one leader, entry requirements, invite codes, pooled points); Fanzone linked to Clan bonuses; DLL Tier system named as the primary matchmaking axis; Core Principles captured; update policy + official comms channels captured (also an operational fact for monitoring).

**Dimension 1:** unchanged (needs client/coaching screen). **Dimension 2:** unchanged this turn.

**Official article coverage:** 12 of the 30 enumerated articles now fetched across this branch (4 in prior sessions incl. stats + this branch's 8) — remaining official leads are mostly operational/account topics (save data, User ID, device compatibility, blocked-playing, etc.), none gate-critical. **The official mechanics spine is complete.**

## Turn 14 update (2026-10-03) — second-database pass (semi-independent) + first-party facilities

**Dimension 4 (in-match conditions):** **"Medical" facility is now first-party named** (Apple listing: "Stadium to Medical, Commercial and Training facilities") — the stale-vendor "Medical Centre" lead is partially confirmed at the facility-name level; its *effects* (injury chance, recovery cost) remain unconfirmed. Energy/stamina mechanics still lack any first-party statement. Still the thinnest dimension, but no longer unfounded.

**Dimension 1 (development):** first-party statement captured — "Use Coaches to develop your players technical and physical abilities" (Apple listing). This is the first first-party anchor for the coach mechanic; the four-type model (Technical / Fitness / Goalkeeping / Special) remains imported-vendor tier.

**Dimension 6 (subsystems):** taxonomy widened by the second database — **World Heroes, Star, Secret, Kick-off Stars** now tracked alongside the seven earlier types; 8 divisions and 10+ cups confirmed first-party.

**Cross-source integrity finding (applies to all dimensions):** dreamkitsapp and dlsinside share image infrastructure and cross-advertise → the "second database" is **semi-independent**; agreement between the two databases is corroboration-lite and must be labelled as such wherever used.

**Gate status:** unchanged in structure — dims 1 and 4 thinnest, no dimension closed, Step 2 still blocked. Two new open conflicts logged (Cult Heroes 84/83 split; Pedri 27133 87 vs 86).

## Turn 15 update (2026-10-03) — second-database pass 2

**Dimension 6 / collection taxonomy:** **Champion 12/12** and **World Winners 8/8** now fully enumerated from the second database, with the duplicate-name pattern confirmed (two Messis, two Ronaldos, two Di Marías in Champion alone) — family membership is by id block, not by name. Classic 30 of ~34. Season Pass card (João Pedro 28356, V13430 = 82) confirmed on a second database, closing that cross-source doubt.

**Cross-source integrity:** estimate drift is now characterised on both sides — SakibPro runs −1 on some cards (documented), DreamKits reads +1 vs the archive on Rodri/E. Martínez/Petit/Berbatov. Consequence recorded: **no OVR is ever promoted across sources; only counts, ids and the in-game/extracted value are treated as ground truth.**

**Gate status:** structure unchanged — dims 1 and 4 thinnest, no dimension closed, Step 2 still blocked. The second-database pass has now covered: Cult Heroes (12/12), Champion (12/12), World Winners (8/8), Classic (30/~34), Team of 2025 (validated earlier via SakibPro), Kick-off Stars / Star / Secret / Dynamic Stars / World Heroes still to sample.
