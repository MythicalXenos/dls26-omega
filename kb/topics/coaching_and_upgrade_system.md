# TOPIC: Coaching, stat upgrades, the OVR ceiling, and the facility discount

**Sweep:** STATE_1_RESEARCH_SWEEP. **Opened:** 2026-09-27T18:35Z. **Exhaustion declaration:** NONE — open.
Serves TAXONOMY-GATE dimension 1 (Training & Coaching architecture: coach categories and rarity, stat yields, breakthrough probability, stat ceiling and progression pacing) and dimension 2 (facility compounding return curve).

**Read the source-quality warning before using anything here.** The entire model below comes from ONE third-party tool — sakibpro.com's Upgrade Simulator (S-0020) — which repeatedly claims to mirror FTG's *internal* logic ("official in-game weight progression", "official hidden weighting system", "mirrors this official internal logic used by First Touch Games", "mathematically identical to the live transfer market", "precise overflow algorithm"). Those are unverifiable claims about another company's internals made by a party with a commercial interest in the tool being trusted, from a domain whose authority over numbers was already withdrawn (DR-001). So: **every figure here is a HYPOTHESIS with a stated verification route, not a game fact.** Nothing on this page has been echoed by FTG, by a second database, by client data, or by the user.

That warning does not make the find worthless — it makes it the most testable artifact in the KB. A coaching model this specific can be falsified or confirmed by a single in-game look at a coach's price, which the user can do. That is why it is written up in full rather than discarded.

---

## 1. The four coach types, their stat groups, and their claimed gem prices

Rendered verbatim from the simulator's Pro panel (S-0020):

| Coach | Stats it covers (verbatim) | Common | Rare | Legend |
|---|---|---|---|---|
| 🏃‍♂️ **Fitness Coach** | SPE, ACC, STA, STR | 25 💎 | 75 💎 | 225 💎 |
| ⚽ **Technical Coach** | CON, PAS, SHO, TAC | 25 💎 | 75 💎 | 225 💎 |
| 🌟 **Special Coach** | ALL STATS | 90 💎 | 240 💎 | 400 💎 |
| 🧤 **Goalkeeping** | GKR, GKH | 15 💎 | 40 💎 | 150 💎 |

- CLAIM: Coaching in DLS26 is organised into (at least) four coach types — Fitness, Technical, Special and Goalkeeping — each covering a fixed group of attributes, each available in three rarities (Common, Rare, Legend), and each priced in **GEMS** rather than coins, with the claimed price ladder above (GK cheapest at 15/40/150, Special most expensive at 90/240/400).
  - source: S-0020 (page-render of sakibpro.com/players/simulator.html, Pro Simulator panel)
  - first_published: page retrieved 2026-09-27; the page carries no version stamp, so the model cannot be placed against client 13.430
  - last_verified: 2026-09-27 by page-render (verified that the page says this — NOT that the game does this)
  - confidence: Speculative (gate-capped: single third-party origin, undisclosed provenance, admitted manual overrides at DR-001, authority withdrawn; origin NONE FOUND for the game mapping)
  - volatility: volatility-Critical — prices and rarity tiers are exactly what an economy rebalance changes, and SakibPro's own timeline alleges an "Economy Reset" on 2026-05-27 (S-0013/S-0014), so this model may predate or postdate it with no way to tell from the page
  - volatility_dimensions: patch-triggered: any economy or coaching rebalance | event-triggered: promotions, Season Pass boundaries, event-specific coach packs (FTG's own 12.200 changelog names "Special Coach Packs", S-0017, which may be a different purchase route entirely)
  - origin: NONE FOUND (third-party tool; not FTG, not an extraction of record)
  - independence: single origin — no second database or tool exists in the frontier yet
  - deception_screen: **authority inflation OBSERVED, escalating** — five separate claims of access to FTG's internal logic; the best version of the tool is gated behind a "👑" Pro tier, so the incentive is to make the free tier look like a taste of paid certainty
  - datamining: pending-confirmation (flagged 2026-09-27; the client's coach definitions would settle type, rarity, price and yield in one pass — blocked, gaps G-0004)
  - evidence_class: verified that the page states this; **recalled-grade** as a claim about the game
  - game_version: UNSTATED by the source — the decisive weakness
  - notes: Three things make this worth pursuing hard rather than ignoring. (a) **It is internally coherent**: four types × three rarities × two stat families (outfield: fitness vs technical; GK separate) is a plausible design, and it agrees with FTG's own words that "Coaches develop your players technical and physical abilities" (S-0011/S-0015) — a *technical/physical split* is exactly what Technical vs Fitness coaches are. That is a real, if weak, official echo. (b) **It is user-verifiable in seconds**: the user plays career mode daily and can open the coaching screen. One answer ("what does a Legend Special Coach cost?") would move this whole table from recalled-grade to user-stated, which outranks it. (c) **It resolves terminology**: the prompt's "coaches by type and rarity" is answered in shape (types + three rarities) even though the values are unverified. The gem currency itself is official (S-0017 IAP list: Bundle/Stack/Locker of Gems), so "coaches cost gems" is at least consistent with an officially named purchasable currency.

## 2. The claimed progression model: development weight, the +10 OVR ceiling, and the GK exception

Verbatim mechanics from the tool's own copy and FAQ (S-0020):
- "Allocate up to **100% Development Weight**. Strategic stat allocation determines your max OVR."
- "Every **10% of total progression weight** directly translates to a **+1 OVR** boost."
- "Once a player hits their **+10 OVR limit (100% weight capacity)**, the tool automatically locks progression."
- "not all stats are created equal. Upgrading crucial attributes like **Control (CON) or Speed (SPE) consumes significantly more progression capacity** than raising **Stamina (STA)**."
- "A player reaches their absolute **+10 OVR limit** when their total cumulative development weight hits 100%."
- Goalkeepers: "operate on a **classic points system** rather than complex dynamic weights. Every **2.2 visual points** added to **GKR or GKP** equals **+1 OVR**, capping at a strict **22 points** total allocation."
- The UI also shows a "**COACHES WASTED (DETAILED COST)**" readout and a coach-selection step reading "**COACH SELECTION (1/3) — Pick one attribute to boost by +2**" with a "**DISCARD & RESHUFFLE**" control.

- CLAIM: Outfield progression is a weighted-budget system in which 100% of "development weight" yields exactly +10 OVR (10% → +1), with per-attribute costs differing (CON and SPE expensive, STA cheap); goalkeeping progression instead uses a flat points budget of 22 points at 2.2 points per +1 OVR (which also yields +10 OVR); coaching involves choosing one attribute from three offered to boost by +2, with a discard/reshuffle option; and coaches can be "wasted".
  - source: S-0020
  - first_published / last_verified: retrieved and verified 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single third-party origin; origin NONE FOUND)
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: the ceiling and weighting are balance parameters | event-triggered: event cards ("boosted attributes", S-0015) may not obey the base-card ceiling at all — unknown
  - origin: NONE FOUND
  - independence: single origin, but note it is **corroborated in one narrow respect by the same site's other page** — `/players` also claims "maximum potential (+10 OVR upgrades)" (S-0018). Same author, so it counts as one source for tier purposes; it does show the two pages were not written independently of each other's numbers, which is weak evidence of an internal model rather than random copy
  - deception_screen: as above
  - datamining: pending-confirmation (flagged 2026-09-27)
  - evidence_class: verified (page text) / recalled-grade (game claim)
  - game_version: unstated
  - notes: **The arithmetic is self-consistent, which is the strongest thing that can be said for it**: 22 points ÷ 2.2 points per OVR = exactly +10 OVR, matching the outfield ceiling via a different mechanism. A fabricated model would not usually close that loop. It also *resolves the shape* of the prompt's open term "ceiling" (+10 OVR above base, reached at a fixed budget) while leaving every value unverified. **Internal inconsistency found and recorded, not smoothed over:** the coach list says the Goalkeeping coach covers **GKR, GKH**, while the GK FAQ says points are added to **GKR or GKP** — GKH vs GKP for the same stat. Either the tool has a typo, or the GK stat set is larger than either line shows, or the two lines were written at different times against different data. All three readings stay open; the pair is logged as a conflict rather than resolved by picking the more convenient label.
  - **Two mechanics here are not in the prompt's terminology at all and are new leads:** the "1 of 3, pick one attribute, +2" coach-selection step with a discard/reshuffle (a randomised or drafted allocation, which would make coaching partly luck-managed rather than purely deterministic — and would connect to the "Coaches Wasted" readout, i.e. a coach can be spent with poor or no result), and the possibility that reshuffling costs something. If real, both change how a coaching plan should be built, and both are exactly the kind of mechanic that must never be assumed from another game.

## 3. The claimed facility discount — first concrete lead on the facility return curve

Verbatim UI element (S-0020): a "**FACILITY DISCOUNT**" control with the values **0% 5% 10% 15% 20% 30%**, sitting directly above the "COACHES WASTED (DETAILED COST)" readout and the gem total.

- CLAIM: A facility produces a discount on coaching cost, in six discrete steps: 0%, 5%, 10%, 15%, 20% and 30%.
  - source: S-0020 (simulator UI)
  - first_published / last_verified: retrieved and verified 2026-09-27
  - confidence: Speculative (gate-capped: single third-party origin; origin NONE FOUND)
  - volatility: volatility-High
  - volatility_dimensions: patch-triggered: facility levels and their benefits are balance parameters | event-triggered: none obvious
  - origin: NONE FOUND for the mapping; DIRECT only for what the tool displays
  - independence: single origin
  - deception_screen: as above
  - datamining: pending-confirmation (flagged 2026-09-27; the client's facility table is the checkable route)
  - evidence_class: verified (the UI values) / recalled-grade (that they are the game's)
  - game_version: unstated
  - notes: **This is the first quantitative lead on taxonomy-gate dimension 2's "facility compounding return curve".** FTG officially names four facilities — Stadium, Medical, Commercial, **Training** (S-0011/S-0015) — and a coaching-cost discount is what a Training facility would plausibly do, so the shape is consistent with official vocabulary. But: the non-uniform steps (5/5/5/5/10) imply the last level is worth double the others, or that the sequence maps to facility levels unevenly, or that one value is a typo. Which facility, how many levels, what each level costs to build or upgrade in coins, and whether the discount applies to gem prices, coin prices or both — all OPEN. If real, this is a **compounding economy lever**: a 30% coach discount changes the gem cost of every future upgrade, which for a career-mode grinder who watches ads for rewards is precisely the kind of long-horizon decision PROMPT.md asks to be optimised rather than guessed. Nothing may be recommended from it yet.

## 4. What this topic still does not know (all OPEN — none may be closed as "does not exist")

Whether coaches cost gems, coins or both (FTG's IAP list sells gems, and a Play review alleges a *coin*-side double fee when applying a coach — S-0012 — so coin involvement is live and unreconciled). The actual per-rarity yields (how many stat points a Common vs Rare vs Legend coach grants). Whether "wasted" coaches are a failure roll, an overflow loss, or a mis-allocation the tool simply accounts for. Whether the 1-of-3 selection is random and whether reshuffling is free. Whether the +10 ceiling applies to special/event cards, and what Cult Heroes' "boosted attributes" (S-0015) means relative to a base card's ceiling. Whether the six discount steps map to Training-facility levels and what those levels cost. Whether coaching is reversible or resettable (the prompt's "reset cycles" term is still OPEN). Whether the Special Coach's "ALL STATS" coverage means it distributes weight across every attribute or lets the player choose. Any per-position differences beyond the GK exception. The role of the officially named **Special Coach Packs** (S-0017) relative to these four coach types.

## 5. Verification plan — ordered by cost and by strength of result

1. **The user, in-game (strongest, cheapest, and the only route that outranks a third-party model without client access):** one look at the coaching screen answers type names, rarity names, currency, prices, yields and whether a 1-of-3 pick exists. This is a batched first-contact verification item, recorded in `kb/user_profile.md` and staged for the earliest permitted advisory output — NOT asked now, because NO OUTPUT DURING BOOTSTRAP governs and the user expressed no active decision.
2. **A second independent database or tool** (mandatory frontier item since DR-001): if two unrelated tools agree on 25/75/225 gems, the tier still cannot rise on count alone (both are third parties of unknown provenance) but the hypothesis becomes strong enough to prioritise.
3. **Community reports** across all 15 client languages: "coach prices", "legend coach gems", "training facility discount", "+10 OVR" — communities enumerate prices quickly and often publish screenshots.
4. **Client data (Step 2):** the decisive route. Coach definitions, price tables, facility tables and the upgrade curve are all static data.
5. **Wayback captures of this tool** to date the model and detect silent changes to its numbers — a tool that edits its own figures without a changelog is how a stale model comes to look current.

## Cross-references
`kb/topics/economy_currencies_and_iap.md` (gems are officially named; IAP ladder); `kb/topics/player_pool_card_types_and_stats.md` (the +10 ceiling first appeared there, S-0018); `kb/irreversible_action_list.md` IA-05 (gem spending on coaches, added this turn); `kb/deception_register.md` DR-001 (authority withdrawn; escalated this turn); `kb/gaps.md` G-0017 (ceiling), G-0020..G-0024; `logs/research_queue_active.md`.

---

## ADDENDUM 2026-09-27T18:52Z — the stat codes are resolved, and one worked example of the ceiling (S-0021)

A per-player card page pairs codes with names in its own prose — "impressive reactions (85 **GKR**) and handling (80 **GKH**)" — which **closes gap G-0023**: the goalkeeper stats are GKR (Reactions) and GKH (Handling), and the simulator FAQ's "GKR or GKP" is a typo, not a third stat. The full mapping is in `kb/topics/terminology_and_abbreviations.md`; the two consequences that matter here are that **TAC means Tackling, not Tactics** (the Technical Coach therefore covers Control, Passing, Shooting and Tackling), and that a goalkeeper row displays SPE ACC STR CON PAS TAC GKR GKH — Stamina and Shooting replaced by the GK pair. Any coaching model that treats a GK like an outfielder is wrong on its face, which is consistent with the simulator's separate Goalkeeping coach and its separate "classic points system" for GKs.

The same page supplies **one worked example of the +10 ceiling**: base OVR 85 → "maximum potential overall rating of 95", attributed explicitly to coaching ("When fully developed **via coaches**"), and the page header reads "Max Upgrade (+10 OVR)". That is the simulator's model applied to a real row, and the arithmetic closes. It is still ONE third-party source agreeing with itself across two pages — same author, so it counts as one source and cannot promote the tier — but it does mean the model is at least internally applied rather than merely asserted.

Also relevant to this topic, from the same page: the card is flagged "✔️ SPECIAL EDITION" with "💎 Acquired Via | Cult Heroes Agent". **Whether the +10 ceiling applies to special-edition cards at all is unknown**, and it is the decisive question for the user's one special card — a special card that cannot be coached, or that starts already boosted ("boosted attributes", S-0015), would make the whole gem-cost model irrelevant to it. Recorded as part of gap G-0017, not resolved.

**Verification plan unchanged and re-ordered by leverage:** the user's own coaching screen now settles MORE than prices — it can settle the stat names shown in-game, whether a GK screen differs, whether a 1-of-3 pick with a discard/reshuffle exists, whether special cards can be coached, and whether a facility discount is visible. That is still one screen and one question, and it outranks everything on this page.

## ADDENDUM 2026-09-27T19:02Z — special cards are claimed to be coachable to +10, and a "black card" end-state appears (S-0022)

The Cult Heroes index FAQ answers "Are the special attributes on these cards upgradable?" with "**Yes, absolutely.** All special edition cards found inside the Cult Heroes database page can be systematically upgraded. By using **team training coaches (Fitness and Technical)**, you can boost any player by **up to +10 over their current base rating**, transforming them into **maxed-out black cards**."

- CLAIM: Special-edition cards (including the live Cult Heroes collection) can be coached by +10 over base using the Fitness and Technical coaches, and a fully developed card becomes a visually distinct "black card".
  - source: S-0022 (card-type index FAQ); consistent with S-0021 (de Gea 85 → "maximum potential overall rating of 95", "When fully developed via coaches") and with S-0020's +10 ceiling model
  - first_published / last_verified: retrieved and verified 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: one author across three pages — a single origin; authority over this domain's numbers withdrawn at DR-001; origin NONE FOUND)
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: coaching rules and card visuals are balance/art parameters | event-triggered: event cards may carry their own rules — and "boosted attributes" (FTG's own words for Cult Heroes, S-0015) is unexplained, so a special card's baseline may not be its displayed base OVR
  - origin: NONE FOUND for the game mapping
  - independence: single origin (three pages, one author)
  - deception_screen: as DR-001 — including that this page calls its rows "verified" while the per-card pages label their OVRs "ESTIMATED"
  - datamining: pending-confirmation (flagged 2026-09-27)
  - evidence_class: verified (the pages say this) / recalled-grade (as a claim about the game)
  - game_version: unstated
  - notes: This **partially answers gap G-0029**, which is the user-specific question that matters most in this topic: the user holds one special card, and whether it can be coached at all decides whether any gem spend on it is meaningful. Three pages of one source now say yes, to +10, with Fitness and Technical coaches named. That is a strong hypothesis and still not evidence. **Open and consequential:** whether the Special Coach (90/240/400 💎, "ALL STATS") also applies to special cards — this FAQ names only Fitness and Technical, which could mean the Special Coach is excluded, or could mean nothing at all; whether "boosted attributes" changes the baseline the +10 is added to; whether the GK point system (22 points / 2.2 per OVR) applies to the two Cult Heroes goalkeepers (de Gea, Vozinha) — the simulator's GK exception and this collection's GK cards have never been considered together; and what a "black card" actually looks like, which is checkable by fetching the card art (an unvisited lead) but must be treated cautiously because this domain GENERATES card images, so its art may be its own render rather than the game's.

## Addendum (turn 18): coach architecture + acquisition economy + breakthrough mechanics (S-0081/82)
**COACH CATEGORIES (4):** Technical (control/passing/shooting/tackling), Fitness (speed/acceleration/stamina/strength), Goalkeeping (reactions/handling), Special. **TIERS (3):** Common = +1 to one random stat; Rare = +2 to two random stats; Legendary = +3 to three random stats + highest Breakthrough chance. Sources: bluestacks character guide + gamingonphone (27 Jan 2026) + r/DreamLeagueSoccer beginner coaching guide (18 Apr 2024) — the +1/+2/+3 yields are community-documented, DLS24-era, needs DLS26 re-check (community-consensus tier, version risk).
**ACQUISITION:** Coaches hired with **Gems** (Legendary: gems only) or by **releasing players**; releasing a Legendary player does NOT guarantee a Legendary coach (gamingonphone, DLS26-era). Community feed-loop math (DLS23/24-era, r/ 5 Feb 2024 + 18 Apr 2024): buy+release 80-rated CBs (not wingbacks) for Rare coaches; players <180 coins for Common; club minimum squad = 16 players (feed with full roster); ~142 Legendary / ~320 Rare / ~1280 Common to max one outfield player (community estimate; a comment disputes 160 Rare for 16 players). **Technique claims (unverified DLS26):** fitness coaches first, technical near the end; train 2-3 players together → more breakthroughs (DLS23-era anecdote); GK loop = 1 Rare + 4 Common, use Legendary when GKR > GKH.
**BREAKTHROUGH MECHANICS (community model):** a total stat-point limit exists per card; the "progress bar" can grow FASTER than the stat ceiling (esp. on Common breakthroughs or none), and when the bar is nearly full even a breakthrough adds nothing (r/ 11 Mar 2023 + comments). "Legendary coaches do NOT increase the cap" (maxed Son: +4 one stat only). Claim level: Community Consensus on the existence of a cap + bar behavior; the exact formulas are unextracted (datamining flag: coaching tables in APK/client).
**PHYSIO SYSTEM:** hired with **Coins** (Common = small energy; Rare = more; Legendary = full energy restore + heals ALL active injuries). Medical Centre facility = lower injury chance + lower recovery cost. Training Centre = formation unlocks (bluestacks, old page). Scouts (Coins, discounted players, 3 tiers) / Agents (Gems, global high-rated/legendary search, riskier) — acquisition economy adjacent.

## Addendum (turn 27): DLS26-era coaching source — SPECIAL COACHES = TARGETED ALLOCATION (S-0104, r/ 24 Dec 2025)
**SPECIAL COACHES (4th category) — the special-card training system:** "Special coaches are only used for upgrading special players like the ones in prize ladder viz Rivaldo, Matthaus, etc." + comment: **"You choose the player and the stat for special players"** — MANUAL allocation of both target player AND target stat for special cards (unlike the RNG fitness/tech coaches for base cards). This explains community build-guides (the maxed Blind "DM build" = targeted allocation). Coach acquisition: **season pass, prize ladder, live events, gems, real money** (DLS26-era source).
**MAX-RATING RULE (DLS26-era statement):** "A card's max rating is the +10 of its base overall, but in some very rare cases it could go up to +11" — R-0012 refined: specials max at base+10 with a documented +11 rare-case exception (community-source; the Blind capture remains the +10 evidence). GK coaches = GKR/GKH only. RNG mechanics for fitness/tech as previously logged.

## Addendum (turn 45): SAKIBPRO simulator model + coach gem-price grid + facility discount ladder (S-0198)
Source = sakibpro.com/players/simulator.html (high-quality third-party tool; its "official hidden weighting system" / "mathematically identical to live transfer market" claims are UNVERIFIED — recorded as third-party model, consistent with our recovered coaching model).
- **Coach gem-price grid (6 tiers):** Fitness (SPE/ACC/STA/STR) Common 25 / Rare 75 / Legend 225 · Technical (CON/PAS/SHO/TAC) 25/75/225 · **Special (ALL STATS) 90/240/400** · Goalkeeping (GKR/GKH) 15/40/150. Coaching is GEM-denominated.
- **Development weight model:** total allocation = 100%; **every 10% weight consumed = +1 OVR**; max **+10 OVR** at 100% (then "Maxed" card). Per-stat weights DIVERGE: CON/SPE consume significantly more capacity than STA (the numeric per-stat coefficients live in the tool's JS, not the rendered page — asset-level lead remains).
- **GK model (separate):** classic points system — **2.2 visual points per +1 OVR on GKR/GKH, 22-point cap** (22/2.2 = 10 OVR ✓).
- **Facility discount ladder: 0 / 5 / 10 / 15 / 20 / 30%** off coaching costs (facility levels' practical benefit; quantified for the first time).
- **Coach application mechanic (matches in-game +2 model):** pick 1 of 3 offered attributes to boost by +2; discard & reshuffle; "coaches wasted" cost tracking implies random-offer waste (the reshuffle economy).

## Addendum (turn 56): +11 overflow; special pair-selection; coach sourcing (S-0236)
- **+11 OVERFLOW (community, Dec-2025):** "a card's max rating is the +10 of its base overall, but in some very rare cases it could go upto +11" — the overflow algorithm's 11th point is REAL per community (single-source).
- **SPECIAL-CARD COACH MECHANIC (footballgamingbd, single-source clone site):** "Choose coach -> select 1 from each pair -> both of the pair are removed forever -> Finalise. Multiple sessions until +10 OVR." Special coaches: +1 stat + 2 random chosen (85-90 gems, 5% bonus dev chance) / +2 + 3 random (~240, 10%) / +3 + 4 random (380-400, 20%). Normal cards: Fitness/Technical coaches + RANDOM stats ("purely luck based").
- **COACH SOURCING (Dec-2025 reddit):** RELEASE players for coaches — common coach from releasing a <80 player, rare from 80+, special from releasing a special player OR diamonds. "Special coaches are only used for upgrading SPECIAL players like the ones in prize ladder (Rivaldo, Matthaus)."
- **Economy notes (DLS23-era + May-2026):** common-vs-legendary "costs the same when maxed" (community); 'common boost' method = churn cheap players (common scout 75 coins, ~63 with recruitment facility) into common coaches; legendary coach "gives only 4 stat points" (community variance vs the 3-random-stat claim).
- **Stadium config trick (DLS23):** E/W stands set 26 + S/N 20 + corners 51 = **92,632 capacity / 52 coins** match bonus.
- Per-stat NUMERIC coefficients remain unretrieved (model documented; numbers not).
