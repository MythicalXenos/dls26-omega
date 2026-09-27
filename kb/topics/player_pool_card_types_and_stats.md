# TOPIC: Player pool, card-type taxonomy, positions, and stat vocabulary

**Sweep:** STATE_1_RESEARCH_SWEEP. **Opened:** 2026-09-27T18:20Z. **Exhaustion declaration:** NONE — open.
Serves PROMPT.md §10 WORKFLOW step 3 (enumerate the candidate pool) and TAXONOMY-GATE dimension 4 (Special Card taxonomy).

**Source-quality warning first.** Everything on this page comes from ONE third-party source — sakibpro.com — whose extraction method is undisclosed, which admits to "manual overriding adjustments", and which self-certifies its own accuracy in machine-generated SEO prose (see `kb/deception_register.md`). Under the Evidence Hierarchy this is *recalled-grade at best* and is capped at Speculative; it is recorded because the enumerations below are checkable against FTG's own vocabulary and, later, against client assets. **None of it may be used to state a player's rating, price or stat.** Its value right now is that it names a bounded vocabulary of card types, positions and stat abbreviations to test.

---

## Card types claimed by the database's own filter (S-0018)

Verbatim filter list, in the order rendered: `Normal`, `Season Pass`, `Cult Heroes`, `Champion`, `World Winners`, `Dreamstar 25`, `Dreamstar 26`, `World Cup Heroes`, `Classic`, `Team 2025`, `Kickoff`, `Dynamic Star` — 12 values, plus an `All Card Types` default and sort options "Top Rated First" and "Sort by Card Type".

- CLAIM: DLS26 special-card vocabulary includes at least the 12 values above, of which **Cult Heroes** and **Season Pass** are card types rather than only event names.
  - source: S-0018 (page-render of sakibpro.com/players, filter controls)
  - first_published: page retrieved 2026-09-27 (the page carries no date or version stamp — freshness is unverifiable, which is itself recorded)
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single third-party origin, extraction method undisclosed, admitted manual overrides; origin NONE for the card-type→game mapping — SakibPro is not FTG)
  - volatility: volatility-High
  - volatility_dimensions: patch-triggered: a new collection ships with an update (Cult Heroes did, between 2026-09-14 and 2026-09-27) | event-triggered: event-scoped card types appear and expire with their events; a card type listed here may be defunct or may be missing entirely
  - origin: NONE FOUND for the mapping (third-party database); DIRECT only for what the page itself displays
  - independence: single origin — no second database discovered yet, so no cross-check exists
  - deception_screen: **incentive and authority inflation observed** — see register row; blanket accuracy self-certification ("Yes, absolutely") and pseudo-technical filler ("indexing engines", "cache structure", "aggregate processing metric")
  - datamining: pending-confirmation (flagged 2026-09-27; client card definitions would settle every value here — blocked, gaps G-0004)
  - evidence_class: verified that the page says this; recalled-grade for what it implies about the game
  - game_version: UNSTATED by the page. The presence of "Dreamstar 25", "Team 2025" and "Dynamic Star" alongside "Cult Heroes" suggests it spans more than one version, but that is inference
  - notes: **Cross-check against official FTG vocabulary (which outranks it):** FTG's own text confirms Special Players, the "Cult Heroes" collection, "Classic greats" / Classic Icons, Dynamic Stars, World Cup Heroes, World Winners and a paid Season Pass. So 8 of these 12 values have an official echo of some kind; **`Champion`, `Dreamstar 25/26`, `Team 2025`, `Kickoff` and the exact label `Dynamic Star` (vs FTG's "Dynamic Stars") have no official echo yet** — each is an open question, not a fact. Conversely, official terms NOT in SakibPro's list (e.g. FTG's "Classic Icons", "World Winners" appears in both) must be checked: an official card family absent from a database is a database gap, not proof the family does not exist.
  - **`Season Pass` as a card type is consequential:** it implies the paid $3.99 Season Pass (S-0017) yields cards, which changes its value calculation for the user's spending decision — and cannot be advised on until the pass's contents and whether a free track exists are researched.

## Positions claimed by the database's own filter (S-0018)

Raw rendered string, unsplit: `CFLWRWSSAMCMDMLMRMCBLBRBLWBRWBGK`, following `All Positions`. A cautious parse yields roughly: CF, LW, RW, SS, AM, CM, DM, DL, MR, MC, BL, BR, BLW, BRW, GK — **the parse is uncertain and the string is recorded verbatim so no false precision is created**. The page's own prose separately names "Center Back (CB)" and "Left Winger (LW)", so CB exists even though it is not clearly separable in the filter string.

- CLAIM: The position vocabulary in circulation includes at least CF, LW, RW, SS, AM, CM, DM, MC, MR, GK and CB, with additional values that may be wing-back or defensive-line variants (BL/BR/BLW/BRW/DL).
  - source: S-0018 (filter string + prose)
  - first_published / last_verified: retrieved and verified 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single third-party origin; the string itself is ambiguous)
  - volatility: volatility-Low for a position vocabulary (it changes with a positional-system overhaul, if ever)
  - volatility_dimensions: patch-triggered: a rework of the positional system | event-triggered: none
  - origin: NONE FOUND for the mapping to the game; DIRECT for the page text
  - independence: single origin
  - deception_screen: as above
  - datamining: pending-confirmation (flagged 2026-09-27)
  - evidence_class: verified (the string) / inference (the parse)
  - game_version: unstated
  - notes: **Directly relevant to the user's formations.** The user plays 3-2-3-2 and has unlocked 3-1-4-2 (user-stated) — both are wing-back-heavy shapes, so which of BL/BR/BLW/BRW/DL are real position codes and how they map to a back three matters more to this user than an abstract position list does. Also relevant to the user's "no position locking" statement (user-stated, verification owed): whether DLS26 has position locking at all, and what codes like SS (second striker) imply about role flexibility, is an OPEN gap — never to be answered by analogy to another game.

## Stat vocabulary and rating ceiling claimed (S-0018)

Named on the page: **OVR** (overall rating), **SPE** (Speed) and **ACC** (Acceleration) — the two stat abbreviations the page says its "Fastest Players" sort aggregates; "**maximum potential (+10 OVR upgrades)**"; "real-world transfer coin costs"; "hidden gems"; filters for Tallest/Shortest/Fastest players; club and national-team groupings ("All Clubs", "All Countries", "🛡️ Clubs", "🌍 National Teams"); and a claimed pool size of **"over 14,000 players"**.

- CLAIM: A +10 upgrade ceiling above base OVR is in circulation as this database's model of maximum potential.
  - source: S-0018 (page prose: "view their maximum potential (+10 OVR upgrades)")
  - first_published / last_verified: retrieved and verified 2026-09-27
  - confidence: Speculative (gate-capped: single third-party origin, undisclosed method, admitted manual overrides)
  - volatility: volatility-High — an upgrade ceiling is exactly the kind of number an economy rebalance changes; SakibPro's own timeline alleges an "Economy Reset" on 2026-05-27 (S-0013/S-0014), so any ceiling from an unknown date may predate it
  - volatility_dimensions: patch-triggered: balance or economy changes | event-triggered: event cards may carry their own ceilings (Cult Heroes' "boosted attributes" hints at a different baseline)
  - origin: NONE FOUND
  - independence: single origin
  - deception_screen: as above; note the incentive — a tool that promises to compute "maximum potential" and a price has a direct interest in the user trusting those numbers
  - datamining: pending-confirmation (flagged 2026-09-27; the client's upgrade curve is the checkable route)
  - evidence_class: recalled-grade (a third party's model, not an extraction)
  - game_version: unstated — this is the decisive weakness: an undated ceiling claim cannot be placed against 13.430
  - notes: PROMPT.md's terminology list carries "ceiling" as OPEN. **This does not resolve it.** It records one third party's model. The pool size (14,000+) is also unreconciled with FTG's official "4,000+ FIFPRO licensed players" (S-0002/S-0011) — a 3.5× gap that must be explained before either number is used: plausible explanations include counting every card variant as a separate row (12 card types × a base pool would multiply fast), counting non-FIFPRO/"Classic greats" and generated players, or double-counting across versions. **HYPOTHESIS, not knowledge — owed.** If the database counts card variants as players, then its "14,000" is a card count and the two numbers are not in conflict at all.

## Tools and endpoints discovered (technical layer, S-0018)

Beyond the three tools already recorded (Player Database, Upgrade Simulator `/players/simulator.html`, Card Creator), this page names **two more**: the **Price Calculator** (`/players/price-calculator.php`) and **Player Comparison** (`/players/compare.php`), plus an **"Upcoming Players"** page (`/players/trending.php`).

The database itself renders client-side — the page body returned only "Loading Players Database..." with no player rows — so **the actual data sits behind a script or endpoint that page-rendering alone will not return**. That is a TECHNICAL LAYER finding and the route to the candidate pool: find the data endpoint (candidates to probe by page-render: `/players/trending.php`, which is a server-rendered page and may list real player names; then common data paths under `/players/`; then read the site's own JS for the endpoint it calls). If no endpoint is reachable from here, the candidate pool cannot be enumerated from this source and a second database or client extraction becomes mandatory rather than optional.

## Open questions this page raises (all OPEN gaps — none may be closed as "does not exist")

Whether each of the 12 card types exists in the game as claimed, and what each grants; whether Cult Heroes cards are already in the database (the filter says the type exists — the rows are unfetchable); whether Season Pass cards are paid-track rewards and whether a free track exists; what "+10 OVR" means mechanically (coaching? upgrade items? both?) and whether it applies to special cards; how 14,000+ reconciles with FTG's official 4,000+; what the real position codes are and whether position locking exists; whether SPE/ACC are the game's own stat names or SakibPro's labels; which version this data reflects; and whether the data is extracted from the client at all.

## Research order for this topic (by source)

1. Official: FTG's store copy and channels for each card family name (the only origin that can confirm a card type); in-game card art and labels via community screenshots; FTG support text on Season Pass and coaches.
2. Databases and tools: a SECOND database (mandatory — no cross-check exists today); SakibPro's `/players/trending.php`, `/players/price-calculator.php`, `/players/compare.php`, `/players/simulator.html` and the site's own JS to locate the data endpoint; every other database found in any of the 15 client languages.
3. English community: card-type guides ("all special cards explained"), upgrade-ceiling threads, position-code discussions, Season Pass worth-it threads.
4. Non-English community: the 14 non-English client languages (ar, nl, fr, de, id, it, ja, ko, pt, ru, zh-Hans, es, zh-Hant, tr), plus any non-client-language community found — card lists are often published first in tr/pt/id for this franchise (HYPOTHESIS to test).
5. Technical: client card definitions and the upgrade curve (Step 2); the database's network endpoint (this file); Wayback captures of this page to date its data and detect silent changes.
6. User-generated: comments and review mining on card value, upgrade costs and price formation, processed for unique information.

---

## ADDENDUM 2026-09-27T18:40Z — the rows ARE reachable: /players/trending.php is server-rendered (S-0019)

Gap G-0019 is **partially closed**: the probe order's step 1 worked. `https://sakibpro.com/players/trending.php` returns real content to a page-render, unlike `/players/`. The master database's 14,000+ rows are still not retrievable this way — this page exposes only the "latest update" additions — so the candidate-pool enumeration required by PROMPT.md §10 step 3 remains unmet and steps 2-6 of the probe order still stand.

### The 17 players listed as "newly added in the latest update"

Claimed "Last Updated: September 27, 2026" (the retrieval date — see gap G-0022 on why that marker carries no information yet) and described by the site as "the complete, officially verified list of the 17 newly added players". No version number is given, so **it cannot be tied to 13.430**.

**CULT HEROES (12)** — the live collection whose window is stated to end 10/14:

| Player | Pos | OVR | Height | Age | Nat. | id |
|---|---|---|---|---|---|---|
| David de Gea | GK | 85 | 192cm | 36 | Spain | 28324 |
| Pierre-Emerick Aubameyang | CF | 85 | 187cm | 37 | Gabon | 28331 |
| Paulo Dybala | SS | 85 | 177cm | 33 | Argentina | 28333 |
| David Luiz | CB | 84 | 189cm | 39 | Brazil | 28325 |
| Francisco Alarcón | AM | 84 | 176cm | 34 | Spain | 28327 |
| Lorenzo Insigne | LW | 84 | 163cm | 35 | Italy | 28328 |
| Hakim Ziyech | RW | 84 | 180cm | 33 | Morocco | 28332 |
| Nicolás Otamendi | CB | 84 | 183cm | 38 | Argentina | 28334 |
| Daley Blind | CB | 83 | 180cm | 36 | Netherlands | 28326 |
| Ander Herrera | CM | 83 | 182cm | 37 | Spain | 28329 |
| Xherdan Shaqiri | AM | 83 | 169cm | 35 | Switzerland | 28330 |
| Josimar José Évora Dias | GK | 83 | 189cm | 40 | Cape Verde | 28658 |

**CLASSIC (4):** Michael Essien DM 85 178cm 44 Ghana id 26838; Andy Cole CF 84 178cm 55 England id 27096; Emmanuel Petit DM 84 185cm 56 France id 27203; Dimitar Berbatov CF 84 189cm 45 Bulgaria id 27675.
**SEASON PASS (1):** João Pedro CF 82 182cm 25 Brazil id 28356.

- CLAIM: The Cult Heroes collection consists of (or includes) the 12 players above, at OVR 83-85, and the same update added 4 Classic cards and 1 Season Pass card.
  - source: S-0019 (page-render of sakibpro.com/players/trending.php)
  - first_published: page dated 2026-09-27 by its own marker (unverifiable, G-0022); retrieved 2026-09-27
  - last_verified: 2026-09-27 by page-render (verified that the page says this — NOT that the game contains it)
  - confidence: Speculative (gate-capped: single third-party origin; authority over this domain's numbers withdrawn at DR-001; origin NONE FOUND)
  - volatility: volatility-Critical
  - volatility_dimensions: event-triggered: the collection's window is stated to end 10/14 (S-0016) | patch-triggered: further additions could extend the list at any time — the site claims it syncs automatically
  - origin: NONE FOUND for the game mapping; DIRECT for the page text
  - independence: single origin — no second database in the frontier yet, and FTG has published no player list on any surface reached
  - deception_screen: authority inflation OBSERVED and escalated — "officially verified" and "Is this the official list? Yes" are self-asserted against an official record that publishes no list at all
  - datamining: pending-confirmation (flagged 2026-09-27; client card definitions would settle names, ids, OVRs and the whole collection in one pass — blocked, gaps G-0004)
  - evidence_class: verified (the page) / recalled-grade (the game)
  - game_version: UNSTATED by the source
  - notes: **This advances gap G-0010 from "nothing known" to "a candidate list awaiting first-party confirmation", and it is the single most time-sensitive item in the KB** — the window it describes is stated to close 10/14 while the user states they are grinding a prize ladder for a special player. Two named first-party confirmation routes: FTG's own Cult Heroes event artwork (the Play event page carries a tall image, S-0016) and FTG's social channels. Weak positive signals worth recording without inflating them: the ages are internally consistent with the players' real birth years as of 2026 (Cole 55, Petit 56, Berbatov 45, Essien 44, de Gea 36), and the OVR band 82-85 with GK/defence/midfield/attack spread looks like a designed collection rather than a random list. Neither verifies the numbers DR-001 withdrew authority over. **Recorded anomaly, not smoothed:** Évora Dias (id 28658) sits far outside the contiguous Cult Heroes block 28324-28334, and Cape Verde is an unusual inclusion for a collection described by FTG as "the names the fans remember" — either a later addition, a mis-categorisation by the site, or evidence that the collection is larger than this page shows. All three readings stay open.

### Structure recovered (technical layer — useful regardless of whether the stats are right)

- Per-player URL pattern: `/players/{card-type-slug}/{player-slug}/{numeric-id}/`, with slugs observed: `cult-heroes`, `classic`, `season-pass` — so the site's own taxonomy is encoded in its URL space and can be enumerated per card type.
- Card art: `https://cdn.sakibpro.com/assets/dls26/{id}.webp`. **The site GENERATES "maxed" card images, so images from this domain are renders, not extractions, and are not evidence of in-game appearance.**
- **Id contiguity hypothesis (G-0025):** 11 of the 12 Cult Heroes ids run 28324→28334 with no gaps, and the Season Pass card sits at 28356. If ids are allocated sequentially per release batch in the client, a new collection is detectable by probing neighbouring ids before any announcement — an early-warning sensor with real lead time. This is inferred from a third party's id space, so it is a hypothesis to confirm against client data, never a fact to act on.
- A `/tools/` index exists (seen in the simulator's breadcrumb) and may list tools not linked from the home page — an unvisited lead.

## ADDENDUM 2026-09-27T19:02Z — the Cult Heroes collection is enumerated as exactly 12 (S-0022), and per-card-type index pages exist

The card-type index `/players/cult-heroes/` is server-rendered and states "**Showing 12 of 12 Players Found**" and "a total of **12 verified players** cataloged in our Cult Heroes roster section". Its 12 rows are **identical in name, id and OVR to the trending page's Cult Heroes subset** (S-0019), and it supplies the common display names for the two players listed there by legal name: Francisco Alarcón = **Isco** (AM, 84, id 28327) and Josimar José Évora Dias = **Vozinha** (GK, 83, id 28658).

Two consequences, both recorded rather than asserted:
1. **The "17 new players" page was not a subset view of a larger collection** — the index gives the Cult Heroes total as 12, matching. Same author, so this is still ONE source and the tier cannot rise; but the main alternative explanation for the data is now closed, and the id-28658 outlier is better explained as an id-allocation quirk rather than a mis-categorisation, since Vozinha (a Cape Verdean goalkeeper) is a plausible cult hero on the merits.
2. **There is one server-rendered index page per card type** (`/players/{card-type-slug}/`), which is the fastest available route to the whole special-card taxonomy (TAXONOMY-GATE dimension 4): each page yields that family's membership and count without needing the client-side master database. Unvisited: `classic`, `season-pass`, `team2025`, `world-winners`, `normal`, `dynamic-star` and any other slug the 12 filter values imply.

New vocabulary from this page's FAQ, recorded with its provenance: special-edition cards are upgradable — "By using **team training coaches (Fitness and Technical)**, you can boost any player by **up to +10 over their current base rating**, transforming them into **maxed-out black cards**". "**Black card**" is the first lead on a visual card-art tier at maximum development, which the Special Card Tracking framework needs for rarity and recognisability; and "team training coaches" is a phrase grouping the Fitness and Technical types. Both are third-party claims from a domain whose authority over numbers is withdrawn (DR-001), and note the same page calls its own rows "12 **verified** records" while the per-card pages flag their OVRs as "⚠️ **ESTIMATED**" — the inflation and the honest caveat continue to sit on different pages of one site.

Also on this page, and recorded as an UNCONFIRMED term rather than a mode: "aiming to dominate the **Global Dream League**". FTG's official vocabulary is "Dream League Live" and "Global Leaderboards and Events" (S-0011/S-0015), so this reads as SEO filler blending two official terms. It is not evidence of a game mode and must not be used as one.

---

## ADDENDUM 2026-09-27T19:46Z — two cards captured in-game: the first DIRECT values in the project (S-0025)

Two user-generated in-game captures (saved under `kb/evidence/`) show signed Cult Heroes cards with their full stat octets. Per Mechanism 5 these are the first DIRECT origins in the project — the origin is the game itself. **The numeric values remain Speculative by the count gate (one origin each), with origin quality recorded as DIRECT; the OVRs alone are High Confidence (R-0003) because three databases independently state them too.**

| Card | Locale | OVR | Year | Stat octet as displayed | Height | Foot | Position badge |
|---|---|---|---|---|---|---|---|
| Paulo Dybala | es ("JUGADOR FICHADO") | 85 | **2020** | VEL 81, ACE 90, FON 80, POT 62, CON 92, PAS 90, DIS 90, ENT 49 | 177 cm | Izquierda (left) | SD |
| Isco | en ("PLAYER SIGNED") | 84 | **2017** | SPE 81, ACC 87, STA 79, STR 65, CON 93, PAS 86, SHO 81, TAC 53 | 176 cm | Right | AM |

Readings worth recording:
1. **The decisive DR-001 test now exists and is unrun.** SakibPro publishes per-player pages with stat octets for both of these players (`/players/cult-heroes/paulo-dybala/28333/`, `/players/cult-heroes/francisco-alarc-n/28327/`). If its octets match these captures exactly, its data has an extraction-like fidelity its prose does not advertise; if they differ, its "official hidden weighting" claims are further undermined. Either outcome is information, and it is now the single highest-value cheap check on the frontier. Recorded as a named lead, not yet run.
2. **Year stamps are on the card face** (2020, 2017) and the Reddit post titles treat them as identifying ("1st Cult Hero - Isco (2017)"), which is how the community names these cards too. Dybala=2020 and Isco=2017 now outrank SakibPro's elided article list for these two players.
3. **The octets are asymmetric in a way the simulator's weighting story predicts**: both cards show high CON/PAS (92-93, 86-90) and low tackling/entry (49-53) and low strength/potencia (62-65) — attacking profiles. Nothing here confirms the weighting model; it merely fails to contradict it. Recorded as a non-test, not a test.
4. **Card design observed**: gold/cream frame, rainbow-gradient upper band, green circular OVR badge, gold year banner, name bar, flag + localized position badge, red star at the foot. The claimed maxed "black card" state is still unobserved (G-0030).
5. **Heights match the database** (Dybala 177 cm, Isco 176 cm against S-0019's 177/176) — a second quiet agreement between capture and database, on fields SakibPro would have no incentive to invent.

## Card-family vocabulary after this turn's discovery search (S-0024)

The special-card taxonomy is no longer one source's filter list. Across three nominally independent databases (SakibPro's filter values; dreamkitsapp.com's family headings; dlsinside's per-player route labels) plus official echoes, the family set now reads: Normal, **Cult Heroes**, **Season Pass**, **Classic** (dreamkitsapp: "Classic players"; FTG: "Classic greats"), **Dynamic Stars** (dreamkitsapp; FTG timeline), **World Winners** (dreamkitsapp; SakibPro timeline), **World Heroes** (dreamkitsapp — vs SakibPro's "World Cup Heroes"; label variance recorded, not harmonised), **Team of 2025 / Team 2025** (dreamkitsapp / SakibPro), **Kick-off Stars / Kickoff** (dreamkitsapp / SakibPro), **Champion players / Champion** (dreamkitsapp / SakibPro), **Dreamstar 25 / Dreamstar 26** (SakibPro only), **Star players** (dreamkitsapp only), **Secret players** (dreamkitsapp only). Of these, the five that had NO official echo in turn 3 (Champion, Dreamstar 25/26, Team 2025, Kickoff) now have a **second independent database** agreeing on four of them (Champion, Team of 2025, Kick-off Stars; Dreamstar still single-sourced), which moves them from "one source's claim" to "two independent third parties agreeing" — still Speculative (no checkable origin, no official echo), but the frontier item "a second database" that DR-001 made mandatory has now been FOUND, and its agreement pattern is the thing to watch. **Secret players and Star players are new families with a single source each; both stay open questions.**

## ADDENDUM 2026-09-27T20:16Z — the decisive check: one card matched the game on ten of ten fields (S-0027, R-0004)

SakibPro's Dybala row matches the in-game capture exactly on all eight stats (after the es→en code mapping), OVR, height, foot and card year. Its Total (634) is the correct sum of its own eight values. The page also confirms: position **SS** in English against **SD** in the Spanish capture (localization re-confirmed); a third row for Dybala (normal, 79 OVR, id 9553); and card-type slugs **world-cup-heroes** (Messi 87) and **dynamicstar** (Cunha 86, João Félix 85) via per-player URLs.
Method consequence now standing: **per-card second-source checks are the routine promotion path for database rows.** The Isco half of the check is queued (G-0033 second card) so the fidelity sample is two before any generalisation is entertained, and captures for further Cult Heroes cards are named leads. Nothing about the database's PROSE changed status: still withdrawn (DR-001).

## ADDENDUM 2026-09-27T20:41Z — fidelity sample is now two cards: one perfect, one nine-of-ten (S-0029, R-0005)

Isco's SakibPro row matches the in-game capture on seven of eight stats (SPE 81, ACC 87, STA 79, STR 65, CON 93, SHO 81, TAC 53) plus OVR 84, height, foot and card year 2017 — but **Passing disagrees: 86 as read from the capture, 88 on the page**. Three explanations stay open (my own misread of a small bubble; a client stat tweak between capture and page dates — a documented phenomenon via ladder recycling; a genuine database error consistent with the site's admitted manual overrides), and none is chosen by preference.
The sample therefore reads exactly as real extracted data with drift looks: Dybala ten-of-ten, Isco nine-of-ten with one disputed field. **This is the result that justifies the case-by-case promotion rule**: the first match alone would have invited blanket trust; the second correctly refuses it. R-0005 promotes Isco's seven agreeing values (the OVR/height/foot/year were already promoted at R-0003); the Passing field stays Speculative (G-0041) pending a higher-resolution or second capture, a correction, or client data.
Also from this page: Isco weight 79 kg, DOB April 21 1992, age 34 (correct), max 94; a second Isco row (normal 79 OVR id 7293); and via Similar Players, the highest rating seen anywhere so far — **Eberechi Eze 90 OVR** (dynamicstar) — plus Matthäus 86 (classic) and De Bruyne 86 (world-cup-heroes), each confirming another card-type slug through a per-player URL.
