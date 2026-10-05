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

## Turn 16 update (2026-10-03) — second-database pass 3; family census near-complete

**Dimension 6 (subsystems / collection taxonomy) — the strongest dimension now:** event families enumerated from the second database — Cult Heroes 12, Champion 12, World Winners 8, World Heroes 8, Kick-off Stars 2, Classic 32 (vs 34 per SakibPro — conflict (i)), Dynamic Stars ≥15 of ~40, Team of 2025 11, Season Pass 1 catalogued. Plus a **separate non-event Secret class of ~250+ legacy-prefixed cards (Classic/Young/Legendary)** that must not be mixed into event counts. Highest OVR observed in the sweep: **Nico Williams 27509 at 96** (Dynamic Stars).

**Dimension 2 (currencies/what they buy) — new evidence angle:** the 96 ceiling implies the top of the card power curve materially exceeds anything in the imported ladder discussion; still no purchase-price data captured (the DBs show prices only on card pages, not indexes).

**Dimension 4 / 1:** unchanged this turn.

**Cross-source integrity:** conflict (i) filed (classic count); no value harmonised. All OVR figures from this pass remain estimates by the source's own disclaimer.

**Gate status:** no dimension closed; Step 2 still blocked. Remaining high-value second-database gaps: Dynamic Stars p2–p3 (closes ~40), Star family sample, dlsinside cross-read of one or two families to test the semi-independence caveat, then the SakibPro normal/tools indexes.

## Turn 17 update (2026-10-03) — families closed; render anomalies guarded against

**Dimension 6 (taxonomy):** four families now closed with archive-matching counts (Cult Heroes 12, Champion 12, World Winners 8, Dynamic Stars 40) plus World Heroes 8, Kick-off Stars 2, Team of 2025 11; two open counts remain (Classic 32 vs 34; Star ≈135 not enumerated; Secret ≈250+ legacy class). The **Star render anomaly** is logged as a data-handling hazard: page renders can duplicate a card template, so counts must always come from record-identity checks (id sets), never from list length.

**Cross-source integrity:** the semi-independence test could not be run on index pages (both sites JS-gallery them); recorded as unresolved rather than skipped silently.

**Gate status:** no dimension closed; Step 2 still blocked. Dims 1 and 4 remain thinnest.

## Turn 18 update (2026-10-03) — source-independence settled; two conflicts narrowed

**Cross-source integrity (applies to every dimension):** the dlsinside↔dreamkitsapp equivalence is now demonstrated at card level (identical values), so the KB's rule is: **one data family, treated as one source**. All earlier "second database confirms" statements carry the amendment note. Classic OVR disagreement confined to **±1** across ~10–12 of 31 shared records — a quantified estimate-band, recorded as a rule.

**Dimension 6 (taxonomy) — now fully bounded:** Classic closed (32 DK / 34 SakibPro, difference explained as classification boundary {26841, Irwin 5839}); **normal/base pool = 14,232 records**; base-card ceiling observed at 86 with two flagged anomalies (Crimaldi 27676 — 92; Moore 25806 — 88). Family list stands: Cult Heroes 12 · Champion 12 · World Winners 8 · World Heroes 8 · Dynamic Stars 40 · Kick-off Stars 2 · Classic 32–34 · Team of 2025 11 · Season Pass 1 catalogued · Star ~135 (unlisted) · Secret ~250+ (legacy class) · Normal ~14.2k records.

**Dimensions 1 and 4:** unchanged this turn — still the thinnest, still needing client-side or user-side evidence.

**Gate status:** no dimension closed; Step 2 still blocked. Official spine complete; database census effectively complete; remaining retrieval is verification-grade, not enumeration-grade.

## Turn 19 update (2026-10-03) — anomaly debunks and tool-surface note

**Data-hygiene rule (now twice-earned):** index rows are not evidence — two of the four "leading" normal-pool records (the 92 and the 88) were 404 stubs; the classic 26841 row is a stub page with blank stats. Counts and values from indexes must be opened card-by-card before use.

**Dimension 2 (currencies/prices):** SakibPro exposes a **price calculator** (coin price from OVR + position) and an upgrade simulator (+10 model). These are site models — usable only as labelled models, never as observations. Base-pool ceiling confirmed at 86 for real cards.

**Dimension 6:** classic 26841 is a stub ("Classic 2006", GK, Spain, 86 OFFICIAL, blank stats) — excluded from the playable card census; family census otherwise unchanged.

**Dimensions 1 and 4:** unchanged; still the open frontier requiring client-side or user-side evidence.

**Gate status:** no dimension closed; Step 2 still blocked. **Research saturation note:** enumeration work is now largely complete; remaining retrievals are verification-grade. The highest-value next input is user-side (Step-5 ask) or client-side (capability probes).

## Turn 20 update (2026-10-03) — coin-price model; narrative sweep closed

**Dimension 2 (currencies/what they buy): strongest turn yet.** The coin-price model is now captured: **price = f(base OVR, exact field position)**, attackers > defenders at equal rating; documented example **86 CF = 2,970 coins**; two data classes defined by the source (Verified-in-market vs Extrapolated-from-formula); secret players carry a discount. Combined with the earlier first-party coin-source list, dimension 2 now has both **income** and **price** structure — the remaining gap is rate data, which is likely user-side only.

**Dimension 6:** clan progression detail filled in (leaderboards, vice-captains, Clan Point boosts, emoji interactions) — consistent with first-party clan-point statements.

**Conflict status:** (j) added — dlskits.mobi misattributes Cult Heroes to 13.410 (secondary-source error; first-party chronology stands).

**Narrative sweep CLOSED:** both remaining narrative sources (thesoccerera, dlskits.mobi) are now read; Reddit is confirmed fetch-blocked (403 ×2). With those done and the official spine complete, **no high-value unread narrative source remains identified**.

**Gate status:** no dimension closed; dims 1 and 4 remain the open frontier and are **not closable by retrieval** — they need client-side or user-side evidence. This is the natural point for the Step-5 ask package.

## Turn 21 update (2026-10-04) — dimension 1 materially filled

**Dimension 1 (player upgrade mechanics) advanced from "thin" to "substantially mapped", with an explicit provenance flag.** The coaching model is now on record (100% development weight, 10% = +1 OVR, +10 cap; unequal stat weights with CON/SPE heavier than STA; four coach types with gem prices; 1-of-3 +2 coach offers; facility discount tiers 0–30%; a separate GK points rule at 2.2 points per OVR to a 22-point cap). **Caveat carried forward: this is a third-party site model, not first-party text** — it is enough to plan and to design a verification test, not enough to promote a claim. The remaining gap in dim 1 is confirmation, which is client-side or user-side.

**Dimensions 1 and 4 status:** both now have model-level content but no in-client confirmation. Neither is closable by retrieval.

**Conflicts:** (k) Pedri 85 (pre-launch article) vs 87/86 (DBs) — extends (g); (l) Kane 86 vs 85 **within one article** — the source disqualifies itself as a tie-breaker.

**Rule reinforced:** count by id sets, never list length (Star p2 = 5 unique in 15 slots); nested pagination means DreamKits type pages cannot be enumerated by URL walking.

**Gate status:** no dimension closed; no exhaustion declared.

### CORRECTION (Turn 21) to the Turn-20 note above
The Turn-20 line "no high-value unread narrative source remains" is **retracted**: the frontier had never been reconciled against the visited set (79 stale strings removed this turn). A **first-party** block of **33 unread support.ftgames.com articles** sits behind them, including **"How do I develop my players" (360003914778)** — developer-authored, directly on dimension 1. Gate status unchanged (no dimension closed), but the "next input = user" framing was premature: **developer text on dim 1 is still retrievable and unread.**

## Turn 22 update (2026-10-04) — first-party text lands on dims 1, 2, 4, 6

**Dimension 4 (stats → gameplay) now has first-party coverage for every one of the eight outfield stats plus both GK stats and energy** — from FTG's own article 360019166777. This was one of the two thinnest dimensions and is now the best-evidenced dimension after the card census. Note the publisher's own caveat: it is a game, not a simulation, with deliberate unpredictability — so this is directional mechanics, not a formula.

**Dimension 1 (upgrade mechanics) now has BOTH a first-party statement and a third-party model, and they disagree on targeting** (random coach pick vs user-chosen player) — logged as conflict (m). First-party also gives the Form Boost rule (duration = Training facility level, min one match).

**Dimension 2:** gem income itemised first-party (league objectives, tournaments, Season Pass, Prize Ladder, multiplayer); and the **sell-a-player → receive-a-coach** loop (version-gated at "12200 onwards").

**Dimension 6:** leaderboard reset window (**3–30 days**) and prize-on-final-position.

**Gate status:** still **no dimension closed** — closing requires the sweep's own bar, not coverage. But the "thinnest dimensions" framing has changed: dims 1 and 4 are no longer thin on *evidence*; what remains thin is *DLS-26-specific confirmation* of the first-party text (the support articles carry no version stamp) and in-client verification.

## Turn 23 update (2026-10-04) — dims 2 and 5 advanced; two new first-party conflicts

**Dimension 2 (currencies) is now the best-evidenced dimension in the sweep:** first-party income lists exist for **both** currencies (coins: 11 sources; gems: 5 sources), plus a third-party price model (86 CF = 2,970 coins). What is missing is *rates* — no first-party source states an amount, and the sale-reward currency is itself contested ("bux" vs "coins"; bux vs coach).

**Dimension 5 (controls/settings) opened:** the Controls sub-menu and the Auto Switch setting are first-party confirmed.

**New conflicts, both internal to first-party text:** (n) **"bux" vs "coins"**; (o) **sale reward = bux vs coach**. Neither is harmonised. Recorded rather than averaged.

**Monitoring policy settled:** FTG states in writing that it does not pre-announce updates, so the storefront "What's New" text is the only authoritative version signal.

**Lead generation:** the related-articles blocks on each support page are now the most productive source of new first-party leads (six more added this turn, incl. "How do I change my player roles" 7917583876625 and "Why are some players displaying a different player card colour" 214385645).

**Gate status:** no dimension closed. Dims 1, 2, 4, 5, 6 all now carry first-party text; dim 3 (card families) is the only dimension whose evidence is entirely third-party.

## Turn 24 update (2026-10-05) — dimension 3 finally has first-party ground

**Dimension 3 (card families/tiers) is no longer wholly third-party.** FTG's own colour ladder — **common bronze / rare blue / legendary gold / max red / special black** — is now on record, with the important structural detail that the ladder is driven by **two independent inputs (OVR band, and special-player status)**. What is still missing: the OVR thresholds for bronze/blue/gold, and any first-party enumeration of the special families themselves (Cult Heroes, Dynamic Stars, Champion, etc. remain third-party names).

**Dimension 5 (controls) filled out:** skill-move inputs (down/up/left-right) now sit alongside Auto Switch, and both connect to the first-party stat bible (CON → skill-move success; SHO → special kicks).

**New sub-system recorded with its gap stated:** the **Roles** button on the Squad screen exists; what roles are and what they do is unknown. Listed as a known-unknown rather than left implicit.

**Practical rule recorded for the user:** selling a player risks permanent loss if that player later leaves the database for licensing reasons (first-party).

**Gate status:** no dimension closed. Every dimension now carries at least some first-party text; the remaining gaps are (i) OVR thresholds for card tiers, (ii) the Roles system's mechanics, (iii) rates/amounts for currencies, (iv) DLS-26-specific confirmation of all unstamped support text, (v) in-client verification.

## Turn 25 update (2026-10-05) — progression and presentation rules land first-party

**Dimension 6 (progression/online) filled out:** rank is an **XP meter that falls on defeats**, with promotion at max XP and relegation on loss of XP. Combined with the earlier leaderboard reset window (3-30 days) and clan features, dim 6 now has first-party structure on both the solo and multiplayer sides.

**New cross-cutting constraint recorded (formations):** formation choice is **season-gated** — a planning constraint for the user that no database source carries.

**Fairness/randomness:** FTG's own statement puts luck in the design and asserts identical rules for all players, while explicitly refusing to call the game a simulation. This is the publisher's position on the rubber-banding allegation; it is **not** treated as evidence resolving it.

**Gate status:** no dimension closed. Remaining known gaps: OVR thresholds for card tiers, the Roles system's mechanics, currency rates/amounts, Season Points definition, and DLS-26-specific confirmation of unstamped support text.

## Turn 26 update (2026-10-05) — the two-ladder economy separated; ad income bounded

**Major disambiguation (dims 2 and 6):** **Season Points** (from wins; season leaderboard; unlock Season Pass tiers) and **Dream Points** (from matches; feed the Prize Ladder; boostable) are **two separate economies**. Any plan that treats them as one is wrong. Recorded as a standing rule.

**Dream Point Boost rules captured first-party:** purchasable in the ladder; apply to career/draft/scenario/DLL only; unusable once the ladder is complete or inactive; **unused boosts carry over to the next ladder**; subject to live-service change. This is the single most actionable item found for the user's situation, and it makes the unresolved ladder end-date matter more, not less.

**Ad income bounded:** FTG states no guarantee of clip frequency and that supply is provider-controlled; LAT-enabled devices may receive no ads at all. The "watch ads for coins" route is therefore **variable income**, which is how it must be modelled in any plan.

**Offline boundary:** Exhibition matches are playable offline.

**Gate status:** no dimension closed. New leads: the Season Pass article under a **second article id** (17143633310225, distinct from 4404070913169) — both need checking for divergence.

## Turn 27 update (2026-10-05) — monetisation mapped; a second in-game timer found

**Dimension 2/6 (monetisation and progression) is now mapped first-party:** the Season Pass is a two-track, non-subscription, per-season purchase that is retroactive, time-lock-removing on late purchase, and tied to a **Progress Bank paid at season end**; and **a countdown timer on the Season Pass message box gives the season end for all users**.

**Why that matters:** we now know there are **two separate in-game timers** — the Prize Ladder timer (the one behind conflict (a)/(b)) and the **Season Pass season countdown**. Both are device-only. The Step-5 ask should request **both** readings, not just the ladder one.

**New conflict (p):** Season Points from "completing matches" (17143633310225) vs "winning matches" (7916583518353), both first-party. Unharmonised — and it changes whether a draw-heavy grind can progress the Season Pass.

**Risk item for the user (dim 7/practical):** DLS saves are **not** protected by Google Play Games or iCloud; only an in-game Sign in with Google / Apple link secures them, and it is not automatic.

**Gate status:** no dimension closed. Next first-party comparison to run: the **second Season Pass article (4404070913169)** against 17143633310225.

## Turn 28 update (2026-10-05) — first-party texts now disagreeing with each other; scripting denial scoped

**A pattern worth naming:** now that many first-party articles are on record, **FTG's own support text contradicts itself in several places** — Progress Bank basis (q), Season Point source (p), sale reward (o), currency naming (n), coach targeting (m). None of these is a third-party error. The rule is unchanged: **record both, never harmonise, never average.** Where two surfaces outvote one (conflict p) that is noted as a lean, not a resolution.

**Scripting allegation, now properly scoped:** FTG denies bots, difficulty control, AI manipulation and outcome influence **in Dream League Live only**, while confirming that **single-player difficulty scales with division movement**. The allegation stands for career play; it is answered (on FTG's word) for multiplayer.

**Practical frontier items closed:** the exact save-data menu path (Options → Advanced), the one-account rule, the silent-unlink trap, the clan entry-requirement/invite-code rule, and the Prize Ladder reward pool (which includes coaches).

**Gate status:** no dimension closed. Dimensions 1–6 all carry first-party text; the live gaps are rates, thresholds, the Roles system, DLS-26-specific confirmation of unstamped text, and the two device-only timers.

## Turn 29 update (2026-10-05) — account-security closed; customisation mapped; a new block class

**Account security is now fully characterised first-party:** Facebook is a dead recovery route, Google/Apple are the only live link routes, Google Play Games and iCloud were never routes, and signing out silently unlinks. This is the practical risk item with the largest downside for the user, and it is now in the Step-5 package with the exact menu path.

**Customisation mapped end to end** (tabs, import specs, run-time shading, deletion) and **bounded**: imported kits/logos are invisible to DLL opponents.

**New retrieval failure class:** a Zendesk **auth wall returning HTTP 200**. Recorded so that no future pass mistakes a 200 for a read. (Do not retry 360015150438 with the fetch tool — it will return the login page again.)

**Gate status:** no dimension closed. Support-article coverage is now deep; the remaining unread first-party items are mostly device/account/legacy-topic articles with low mechanics yield, plus a few auth-walled ones.

## Turn 30 update (2026-10-05) — coverage claim corrected; first-party block NOT exhausted

**Self-correction (important):** earlier turns described the first-party corpus as complete on the strength of a ~30-URL list. The FAQ index shows **52 DLS FAQ articles**, so roughly 22 remain unread. **The block is not exhausted and no exhaustion claim stands.** The full DLS section listing (`sections/203117809`) is the next fetch, because until it is read we cannot know what we are missing.

**Why this matters beyond counting:** the unread titles include `Some game values and content have changed. Is this a bug?` — a likely first-party statement on rating/stat drift, which is the mechanism behind our ±1 cross-source conflicts and the DB estimate caveat. That single article could reframe conflict (h) from "database sloppiness" to "published values move between updates".

**Standing lesson, second time this session:** do not infer completeness from a list that was never reconciled against an index. (First instance: the Turn-20 saturation claim; second: the "complete official spine" claim.)

**Gate status:** no dimension closed; no exhaustion declared.

## Turn 31 update (2026-10-05) — the drift question is now explicitly open, not assumed

**The important change is to how we read evidence, not to a dimension.** FTG's live-service statement (values change regularly, for creative/technical/business reasons, sometimes temporarily) means **every cross-source numeric difference could be real drift rather than estimation error**, and we cannot tell which from outside the game. Consequences carried forward:
- The ±1 band stays a band; the *cause* moves from "assumed estimation error" to **open**.
- Any single third-party OVR is now understood as **a reading at a point in time**, not a stable property of the card.
- The Step-5 ask's value rises again: only an in-game reading can anchor a value, and even then only for that moment.

**Coverage, precisely:** 30 DLS FAQ titles rendered vs 52 advertised; 4 of the 30 unread; up to 22 unaccounted for. Block remains open; no exhaustion claim.

**Gate status:** no dimension closed. Note that this turn improved *method* rather than *coverage*, and that is recorded as such rather than dressed up as new game knowledge.

## Turn 32 update (2026-10-05) — coverage gap closed; an irreversible-action rule added

**Coverage:** the DLS FAQ corpus is **52 articles across two listing pages**; all 52 titles are now known; **nine remain unread**. No exhaustion claim; the retracted "complete spine" claim stays retracted until those nine are read.

**New standing rule (safety, not research):** **Reset Profile** (Settings → Advanced, skull-and-crossbones) destroys all progress **including in-app purchases**, is unrecoverable, and is limited to **one per 30 days**. It must never appear in a plan without an explicit warning. Note the menu hazard: the destructive control sits alongside Link Profile and Manage Devices in the same menu.

**Next two targets are substantive, not incidental:** `What are facilities` and `How can I expand my squad` are core progression systems we have so far only seen in storefront marketing language.

**Gate status:** no dimension closed.

## Turn 33 update (2026-10-05) — a progression lever with a spend attached

**Squad size is a facility upgrade, not a constant.** Accommodation (Stadiums & Facilities screen) adds squad slots per level. Any squad-planning recommendation therefore has a **cost dimension** and must be phrased as conditional on the user's current accommodation level. Per-level slots and upgrade costs remain unknown — this is now a named gap that blocks sizing advice.

**Facilities defined but not enumerated:** buildings granting unique career-progression bonuses. The individual bonuses are a known-unknown; do not fill them from marketing copy.

**Kit functions disambiguated (not harmonised):** editing (My Club) vs match-day selection (tap player models). Whether an away kit is separately editable stays open.

**First-party pricing still absent:** the IAP article gives the Shop route and nothing else. All pricing in this corpus remains third-party.

**DLS FAQ:** 48 of 52 read; **4 unread**. **Gate status:** no dimension closed.

## Turn 34 update (2026-10-05) — DLS FAQ section: 52/52 enumerated and read

**Milestone, stated precisely:** every one of the **52 DLS FAQ articles** has been enumerated **and** read. First block where both hold. **Not an exhaustion declaration** — General FAQs (21), Parents' Guide (8), the auth-walled articles and blocked routes are all still open, and the DLS section is only one of the sections in the help centre.

**Corroboration:** offline Exhibition play now has **two independent first-party articles** behind it.

**New open item (family census):** a fifth title section, **Ultimate Draft Soccer (7900693036561)**, appears on the help-centre root. Either a rename of UCS or a distinct title — unresolved, do not assume.

**High-value new lead:** `360004222118 Multiplayer Troubleshooting` — the most promising remaining first-party route into netcode behaviour, which is currently a named gap.

**Gate status:** no dimension closed.

## Turn 35 update (2026-10-05) — CORRECTION: five sources re-attributed; netcode closed

**CORRECTION (highest priority in the corpus right now):** article ids `7916959134737`, `7917587319313`, `7917423348497`, `7917583876625`, `17146555181585` appear in the **Ultimate Clash Soccer** section listing. Some also appeared in listings we read as DLS. Status is **ATTRIBUTION UNCERTAIN** — not "definitely UCS", not "DLS". **Suspended as DLS facts until settled:** formation season-gating, the promotion/relegation XP meter, Player Roles, the home+GK kit route, the "bux" sale reward. **Conflicts (n) and the kit divergence are re-opened**, not resolved. **Turn 36: open the affected articles and read their section/game.**

**Census:** Ultimate Clash Soccer is confirmed as the canonical name (slug "Ultimate-Draft-Soccer" is stale — **slugs are not evidence**), and a **sixth title section, 8 Ball Hero FAQs (360000489137)**, needs adding to the family census.

**Netcode gap CLOSED** with first-party detail: cloud servers, opponent's connection cannot degrade your experience, opponent never learns your address, ~2MB/match, latency- and packet-loss-sensitive, IPv6 and 5G supported, local same-platform multiplayer over the same router, no Facebook invites. Retain the nuance: insulation from the *opponent's* line is not a promise about your own.

**Two destructive controls, distinct:** Reset Profile (progress loss, 30-day limit) vs Delete Profile (device wipe, cancellable countdown). Both in Settings > Advanced.

**Gate status:** no dimension closed.


## Turn 36 update (2026-10-05) — provenance correction; General FAQ title census

**As of Turn 36, product attribution was unresolved; Turn 37 API metadata supersedes that status.** The five ids `7916959134737`, `7917587319313`, `7917423348497`, `7917583876625`, `17146555181585` are listed under the Ultimate Clash Soccer section. Turn 36 reopened three article bodies; they do not name a game, though promotion/sell pages link to UCS-specific articles and formation links to DLS19 legacy help. The saved ledger did not substantiate the prior claim that these ids also appeared in a DLS section listing; that claim is withdrawn. Do not label the articles DLS-specific or UCS-exclusive. Suspend the DLS claims until API metadata or explicit product language is captured. The bux/sell and kit conflicts remain open.

**General FAQs enumeration is complete: 21 titles on section 203171905 page 1; page 2 empty.** Article-content coverage is still partial; enumeration alone does not close the source dimension or authorize an exhaustion declaration. FTS15 kit article 213892809 remains excluded.

**Correction:** Turn 35's "new sixth title section" claim for 8 Ball Hero is wrong; it appears in Turn 30's category-index note. The complete category census is not verified from the partial two-chunk Turn-35 render.

**Gate status:** no dimension closed; netcode is a first-party resolved sub-question, not a closed research dimension.


## Turn 37 update (2026-10-05) — canonical section assignment verified

Public Zendesk article JSON returns `section_id: 7900693036561` for all five disputed IDs (`7916959134737`, `7917587319313`, `7917423348497`, `7917583876625`, `17146555181585`). The section renders as **Ultimate Clash Soccer**. Canonical Help Center attribution for these sources is therefore UCS, not DLS. No DLS version stamp or separate product field is present; cross-product reuse is not documented. Remove these five as DLS evidence. The sale-reward and kit inconsistencies are not established DLS internal contradictions; **re-audit the old FTG contradiction count**, especially entries n/o. No dimension closed.


## Turn 38 update (2026-10-05) — General FAQ contents sampled

Five General FAQ bodies read: Android Play Store compatibility, Play Store download errors, Bluetooth-controller compatibility, Sign in with Apple setup, and Sign in with Google setup. First-party setup content clarifies that Apple/Google cloud sign-in is distinct from iCloud/Google Play Games; the Apple page gives a DLS Settings > Advanced path but no DLS version stamp. Controller and download guidance is general and not DLS-26-specific. General FAQ body-reading coverage is 10/21 per the reconciliation output; title enumeration is complete, but content coverage and the dimension remain open. No dimension closed.


## Turn 39 update (2026-10-05) — cloud-save documentation conflict

First-party DLS account pages conflict: `214387685` says Google Play Games and iCloud do not secure DLS saves and are not used by the games; `360000603398` tells DLS users to enable Google Play Games Services and Google Play Cloud; `360000613657` tells DLS users to enable iCloud and play matches to upload. All are unstamped. Preserve the claims side by side; do not choose one as current or advise changing the save route. Ask the user which controls are visible if a device-specific recommendation is needed. Sign in with Google/Apple remain distinct account services, but that distinction does not resolve this storage conflict.

General FAQs: 15/21 article bodies read, 21/21 titles enumerated. No dimension closed; no exhaustion declaration.


## Turn 40 update (2026-10-05) — account-save conflict retained

Zendesk metadata places `214387685`, `360000603398`, and `360000613657` in General FAQs (`203171905`); DLS article `4413273241873` is in DLS FAQs (`203117809`). Metadata reports `outdated=false` for all, but `edited_at` differs from `updated_at`; none carries DLS build/version applicability. The Google Play Games/iCloud save-route contradiction therefore remains unresolved. Do not promote the support text into a current DLS-26 instruction or advise switching settings. General FAQ body coverage: 16/21. No dimension closed.


## Turn 41 update (2026-10-05) — General FAQ body coverage

Four remaining FAQ bodies read: contact, DLS Classic availability/kit instructions, and FTS15 availability. They concern support workflow or legacy titles and do not establish DLS26 behavior. Coverage is 20/21 bodies; the only un-read title is FTS15 kit article 213892809, intentionally excluded. New lead `360017063617` describes Super Players with grey/gold shiny backgrounds, but its product/version scope is unstated; verify API section metadata before using it in the card-tier taxonomy. No dimension closed.
