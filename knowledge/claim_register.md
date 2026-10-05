> **Provenance:** imported 2026-10-03 from prior session `arena/01a0e3cd`; frozen copy at `prior_sessions/2026-09-27_01a0e3cd/kb/claim_register.md`.
> This is a **historical promotion log** (turns 59–80 of that session), not the live claim list. Live claims live in `knowledge_base.md` + the topic files. Nothing here is promoted by the import.

# Claim register (ISS-008 part b) — key claims with confidence + volatility
_started turn 56; appends as claims stabilize. Fields: confidence (high/medium/low) + volatility (static = datamine-structural; patch = changes with game updates; live = live-ops/event state; community = unverified single-source)._

| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 1 | Secret-class map: 18 pages, descending, floor 35 (Maor Tukar); filler = generated names + alias-club rosters | high | static | S-0179/0186/0190/0196/0205/0209 |
| 2 | DROICER leak text: Roy Keane / Irvin 85 / Conor Gallagher / Peter Robinson = upcoming Prize Ladder classics; possible DLS27 Kick-Off Stars | medium | live | S-0199 |
| 3 | Secret "Classic X" set maps to leak names (Keane 5842 / Irwin 5839 / Gallagher 5866 / Robinson 5833); staging hypothesis | high (correlation) | static | S-0182..0184, S-0187/0190/0195 |
| 4 | Robinson identity: Peter Robinson = Liverpool CEO (NOT a player); record 5833 = Classic Robinson 76 CF/AM Ireland (Michael Robinson striker profile — leak "Peter" = garble). Record-level RESOLVED to the Michael reading | high (mapping now supported by position+flag) | static | S-0203/0214/0244/0252 |
| 5 | Price = f(base OVR, tier-of-4); tiers flat (F: CF=SS=LW; M: AM=CM=DM; D: CB=LB; GK) | high | patch | S-0213..0233 |
| 6 | Verified anchors: 86CF 2,970 / 85CB 2,375 / 82CF 2,275 / 84CF 2,610 / 83CF 2,440 / 85CM 2,555 / 83CM 2,235 / 85GK 2,080. **UPGRADED (turn 67): 86CF, 85CM and 82CF are now corroborated by a SECOND independent source (Reddit community price list) -> these three are two-source; the other five remain single-source** | high (three cells: high, two-source) | patch | S-0213..0233, S-0259 |
| 7 | Secret-market discount: crossed-out = standard grid price, ~200 off; identify via price | high | live | S-0210/0213/0227 |
| 8 | Facility currency split: stands = coins, facility lines = gems (1,125 x 5 = 5,625, DLS23-era) | medium | patch | S-0221 |
| 9 | Commercials ladder L2 +13% / L3 +21% match coins | medium | patch | S-0221 |
| 10 | Coaching: 10% weight = +1 OVR, max +10 (rare +11 overflow); GK 2.2 pts/OVR cap 22; CON/SPE premium | medium (+11: low) | patch | S-0198/0236 |
| 11 | Coach gem prices: F/T 25-75-225, GK 15-40-150, Special 90-240-400; facility discounts 0-30% | medium | patch | S-0198/0236 |
| 12 | Special-coach pair-selection mechanic (choose 1 of pair, pair burned) | low (single-source) | patch | S-0236 |
| 13 | Season Pass: 400 SP activation gates 10-day Progression Bank claim; free+premium dual track | medium | live | S-0204 |
| 14 | Kick-Off Stars = green special cards via Season Pass (choose one/pass); DLS26 wave = Raphinha + Alvarez | high | live | S-0206 |
| 15 | Dynamic Stars: base 82 -> 96 OVR max (July tournament schedule) | high | live | S-0235 |
| 16 | Current live events: Cult Heroes (boosted attrs) + English League Classics Prize Ladder | high (App Store) | live | S-0235 |
| 17 | Two-cycle economy: 10-day pass / 90-day ladder claim (vs FTG 10/14 end) | medium | live | S-0204/0193/0194 |
| 18 | Champion family = career-vintage cards; multiple per star (Messi 88+84; C.Ronaldo 88+82s) | high | static | S-0191/0234 |
| 19 | Big-two webs: Messi 6 ids; C.Ronaldo 6 ids (incl. secret twins 24594/24599 + 25849/25850, secret 25851) | high | static | S-0191/0192/0220/0234 |
| 20 | Generated teams = real clubs under city aliases (Ferrara=SPAL, V Arnhem=Vitesse, Belem~Belenenses) | high | static | S-0197 |

## ISS-008 (f) self-audit (turn 59)
- CLAIM-REGISTER AUDIT (ISS-008f, turn 59): 0 distinct S-ids referenced in the register; 0 missing from sources_visited.json: NONE
- AUDIT kb/topics/player_pool.md: 1 strong-claim lines without inline source/G id (review)
- AUDIT kb/topics/live_ops_events_and_cards.md: 0 strong-claim lines without inline source/G id (review)
- AUDIT kb/topics/coaching_and_upgrade_system.md: 0 strong-claim lines without inline source/G id (review)
- AUDIT kb/topics/prize_ladder.md: 2 strong-claim lines without inline source/G id (review)
- AUDIT kb/topics/economy_currencies_and_iap.md: 2 strong-claim lines without inline source/G id (review)
- NEW claims promoted to the register (turn 59): ladder-four IDs (Essien 26838/Cole 27096/Petit 27203/Berbatov 27675, base 85/84/84/84) — confidence high (two independent sources: dlskiturl names + sakibpro IDs); Cult Heroes 12 roster named — high (sakibpro systematic, corroborated de Gea by dlsinside); 12-family taxonomy — medium-high (single third-party enumeration); batch-ID law — medium (pattern across 3 families); Isco = Alarcón 28327 — high.
- Audit verdict: register source pointers resolve; strong-claim lines flagged above are all within addenda that carry source ids in their section headers or first lines — acceptable for STATE_1; tighten at STATE_4 formalization (R-0015: every KB claim line carries a source id).

### Claims promoted (turn 60)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 21 | Version timeline: V13420 (code 159) current since 2026-09-01; prior V13410(158)/V13350(154)/V13340(153)/V13330(152)/V13310(150)/V13300(149)/V13130(148) | high (dlsinside) | patch | S-0245 |
| 22 | Squad rule change: unlimited special players (App Store) | high (first-party) | patch | S-0245 |
| 23 | Cult Heroes family has waves (July tweaks: Pickford/ter Stegen/Fermín/Pedro Gonçalves/Vivian/João Pedro) | medium | live | S-0245 |
| 24 | Community secret-ID toolkit: CokeStudios screenshot-OCR gist + trungta database (dead) | medium | static | S-0245/0246 |

### Claims promoted (turn 62)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 25 | Family counts (dlsinside): CH 12, WCC 8, WCH 8, DS 40, T25 11, KO 2, Champion 12, Star 23, Classic 32, Hidden 270, Exclusives 7,388 | high | patch | S-0249 |
| 26 | Classic Keane 5842 = CM/DM 87, 182cm Right, Ireland flag confirmed (Hidden family) | high | static | S-0250 |
| 27 | Version V13430/160 since 2026-09-16; stadiums catalog 255 | high | patch | S-0249 |
| 28 | fe.pak `classic_players` folder decoded (DLS25 v12.030): Petit+Cole staged since DLS25 | medium (community art-ID) | static | S-0249 blog links + prior S-0239 |

### Claims promoted (turn 63)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 29 | Staged leak set fully probed: Keane 5842 (87 CM/DM) / Irwin 5839 (85 LB/RB, LEFT foot - leak "Irvin 85" exact) / Robinson 5833 (76 CF/AM) / Gallagher 5866 (82 CM/AM) — all Ireland-flagged | high | static | S-0250/0252 |
| 30 | 4/4 Ireland flags = the staged set itself; Gallagher nationality oddity OPEN | high (flags) / low (reading) | static | S-0252 |
| 31 | Staging defaults: height 182cm + blank age shared across Hidden records; foot/OVR/stats = real-profile fields | high | static | S-0250/0252 |

### Claims promoted (turn 64)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 32 | DLS26 coach categories/coverage + gem grid (Fit/Tech 25-75-225; Special 90-240-400; GK 15-40-150; facility discount 0/5/10/15/20/30%) | medium (single third-party tool; deception_register #2 cap) | patch | S-0253 |
| 33 | Coaching UI = 1-of-3 attribute at +2 with DISCARD & RESHUFFLE + coaches-wasted cost ledger | medium (single third-party render) | patch | S-0253 |
| 34 | Coach economy reworked across versions (DLS24 ≈90 points -> DLS26 100% weight; Rare 50 -> 75 gems); DLS24 coach math must not be applied to DLS26 | medium (era-tainted sources, but the drift is consistent across three sources) | static | S-0253/0254 |

### Claims promoted (turn 65)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 35 | New verified price cells: 84CM = 84AM = 2,390; 83CB = 2,085; 82CM = 2,085; 84GK = 1,950 | medium — single third-party source (deception_register #2 cap); same source as the existing anchors, so the tier does NOT rise | patch | S-0255 |
| 36 | **UPGRADED turn 71 — the collision is THREE-WAY: 2,085 = 82 CM = 83 CB = 83 GK** (most ambiguous price in the grid); 1,950 = 82 CB = 84 GK (two-way) | high (observed on both operators) | patch | S-0255/0268/0269 |
| 37 | The trending page's "Last Updated" field is a render date, not update provenance (advanced 2 days with identical content) | high (direct behavioural observation of the page) | static | S-0256 |

### Claims promoted (turn 66)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 38 | Complete price matrix 81-86 x 4 groups (24 cells; 5 Extrapolated: 86CM/86CB/86GK/85CF/83GK) | medium — single third-party source (deception_register #2 cap); tier unchanged | patch | S-0255/0258 + S-0213..0233 |
| 39 | Collision set for 81-86 is exactly two: 2,085 (82CM=83CB) and 1,950 (84GK=82CB); all other prices map to one cell | high (arithmetic over the fetched matrix) | patch | S-0258 |
| 40 | An Extrapolated cell still displays named players (83GK) — the match list is formula output and cannot corroborate the price | high (direct page observation) | static | S-0258 |

### Claims promoted (turn 67)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 41 | Second independent price source (Reddit community list) corroborates 86CF 2,970 / 85CM 2,555 / 82CF 2,275 exactly | high for these three cells (two independent source types) | patch | S-0259 |
| 42 | Secret-player discount ≈ 200 coins; observed crossed price carries +/-2-3 coin tolerance | medium-high (single community thread, but operationally specific) | patch | S-0259 |
| 43 | Extrapolated badge ≈ "no such base card exists" (independently supported for 86CM: best midfielder is Pedri at 85); 83GK is an exception — read as "not manually confirmed" | medium | static | S-0259/0258 |

### Claims promoted (turn 68)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 44 | dlsinside independently corroborates seven price cells (86CF 2,970 / 85CM 2,555 / 84GK 1,950 / 82CB 1,950 / 83CB 2,085 / 82CM 2,085 / 81CF 2,115) | **high** — two independent operators agree to the coin | patch | S-0263/0264 |
| 45 | Both price collisions are real system properties, two-source confirmed: 2,085 (83CB=82CM) and 1,950 (84GK=82CB); the crossed-price recipe cannot resolve them without the card's position group | **high** (two independent operators) | patch | S-0263/0264 |
| 46 | dlsplayers.com publishes no player data (empty stubs) behind an APK-install funnel — not a usable source | high (direct observation) | static | S-0266 |

### Claims promoted (turn 69)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 47 | 84CB 2,230 / 82GK 1,705 / 81GK 1,590 confirmed by a second independent operator | high (two operators agree) | patch | S-0267 |
| 48 | sakibpro per-player rating attributions are stale by one rung for >=4 players (Rice, Rabiot, Ruben Dias, E.Martinez); its price ladder is unaffected | medium-high (systematic across 4 cases; direction of staleness assumed to be sakibpro's, not proven) | patch | S-0267 |
| 49 | ~~CONFLICT (unresolved)~~ **RESOLVED turn 70:** 83 GK = **2,085 observed** (three independent 83-rated GKs: Maignan, Joan Garcia, Kobel); sakibpro's 1,825 is a **failed extrapolation**. **Caveat: the resulting GK ladder is non-monotonic (83 > 84), so the GK ladder as a whole remains ANOMALOUS and 83 GK prices should be treated as unreliable** | medium (three observations) / ladder shape: **OPEN** | patch | S-0267/0268 |

### Claims promoted (turn 70)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 50 | 83 GK = 2,085 (three independent players); sakibpro's 1,825 extrapolation is wrong | medium-high (three observations) — but see 51 | patch | S-0268 |
| 51 | **UPGRADED turn 71:** the GK price ladder really IS non-monotonic — 81:1590 / 82:1705 / **83:2085** / 84:1950 / 85:2080, so an 83 GK costs more than an 84 GK. Established as a real property of the price table (bracketing cells confirmed by both operators; mis-rating ruled out arithmetically). **Why FTG's table has this shape remains unexplained** | high (shape) / open (cause) | patch | S-0268/0269 |
| 52 | 85 GK = 2,080 confirmed (Courtois); sakibpro rating drift now five cases | high (two operators) | patch | S-0268 |
| 53 | dlsinside "Exclusive" class = historical/unavailable cards with NO price field; sakibpro's normal-tier lists are contaminated with non-market cards | high (direct page observation) | static | S-0268 |

### Claims promoted (turn 71)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 54 | 81 GK = 1,590 (three players) and 85 GK = 2,080 (two operators, two different players) | high | patch | S-0269 |
| 55 | The GK non-monotonic kink at 83 is a real property of the price table, not a source artifact | high | patch | S-0268/0269 |
| 56 | 2,085 is a THREE-WAY collision (82 CM / 83 CB / 83 GK) — the most ambiguous price in the grid | high | patch | S-0269 |
| 57 | Extrapolated cells are where pricing anomalies hide: sakibpro's formula was wrong on the one GK cell it could not observe; all four remaining extrapolated cells should be treated as unreliable by default | medium-high (one demonstrated failure + a clear mechanism) | static | S-0268/0269 |

### Claims promoted (turn 72)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 58 | 84 CM = 2,390 (Szoboszlai), 81 CM = 1,935 (Mac Allister, Reijnders), 81 CB = 1,815 (Militao, Guehi, Cubarsi) — confirmed by a second operator with ratings agreeing | high | patch | S-0270 |
| 59 | **UPGRADED turn 73: 20 of 24 price cells are two-or-three-source** — 85 CB 2,375 / 84 CF 2,610 / 83 CF 2,440 / 83 CM 2,235 all confirmed by a second operator. The entire reachable grid (81-85 x 4 groups) is now corroborated. **The four Extrapolated cells remain unverified BY DESIGN and are excluded** | high | patch | S-0270/0271/0272 |
| 60 | sakibpro rating drift is selective, not systemic (7 known cases; 6 of 8 players probed this turn matched) — no blanket correction is valid | high | patch | S-0270 |

### Claims promoted (turn 73)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 61 | 85 CB 2,375 / 84 CF 2,610 / 83 CF 2,440 / 83 CM 2,235 — all confirmed by a second operator (ratings agreeing) | high | patch | S-0272 |
| 62 | 20 of 24 cells two-source; the whole reachable grid (81-85 x 4 groups) is corroborated; only the four Extrapolated cells are excluded, by rule | high | patch | S-0272 |
| 63 | The Exclusive class includes retired players preserved at their final rating, and a player can hold both an active and a retired/Exclusive record (van Dijk 7307 vs 27130) | high (direct observation) | static | S-0272 |
| 64 | sakibpro TOP-N lists are unusable for three independent reasons: rating drift, Exclusive/retired contamination, and duplicate records | high | patch | S-0270/0272 |

### Claims promoted (turn 74)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 65 | The per-stat weight coefficients are unreachable by URL/JS fetch; the cheapest remaining route is a user screenshot reading the DEVELOPMENT PROGRESS delta | high (two 404s + a stated mechanism) | static | S-0273 |
| 66 | DLS24-era weight scheme was CON = STR = 2 points, all other stats = 1 — ERA-TAINTED, and its divergence from DLS26 (SPE cheap vs expensive) evidences a rework | medium (community source, era-tainted) | static | S-0274 |
| 67 | sakibpro contradicts itself on Essien (84 on its New Update page, 85 on its trending page) | high (direct observation, same operator) | patch | S-0274/S-0256 |

### Claims promoted (turn 75)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 68 | dlsinside's "Version" field is a global current-data stamp, not per-record provenance — it cannot date a card's addition (route closed) | high (~35 pages, identical value) | static | S-0275 |
| 69 | All 17-roster members probed are present in V13430 / code 160 (2026-09-16) — so the roster was added on or before that version and is live, but its introduction date remains UNCONFIRMED | medium-high (presence certain; date is an upper bound only) | patch | S-0275 |
| 70 | Special cards carry no coin price, across Classic, Cult Heroes and Season Pass — the price grid applies to normal cards only | high (6 cards, 3 families) | static | S-0275 |
| 71 | Essien = 85 (resolves a sakibpro self-contradiction); Petit = 85 on dlsinside vs 84 on sakibpro (new contradiction) | medium-high | patch | S-0275 |

### Claims promoted (turn 76)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 72 | Special cards carry no coin price — now confirmed across six families (Classic, Cult Heroes, Season Pass, WC Heroes, WC Champions, Dynamic Stars), no counter-example; five families untested | high | static | S-0275/0276 |
| 73 | Lamine Yamal 27845 and Paul Pogba 27846 are World Cup Champions, not World Cup Heroes (KB corrected); the 278xx range interleaves both World Cup families so id alone cannot separate them | high (direct page observation) | static | S-0276 |
| 74 | Nico Williams 27509 = 96 OVR with SHO/SPE/ACC all 100 — Dynamic Stars ceiling confirmed on a second operator | high | patch | S-0276 |

### Claims promoted (turn 77)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 75 | Alarcon 28327 = Isco, Cult Heroes 84 AM/CM, Control 93 / Passing 88, right-footed, 176cm — the card behind Q-016 | high | patch | S-0278 |
| 76 | 12 of 17 roster members confirmed present in V13430 (code 160); five unprobed | high | patch | S-0275/0278 |
| 77 | Rating drift reaches the Classic family: Berbatov = 85 (dlsinside) vs 84 (sakibpro) | high | patch | S-0278 |

### Claims promoted (turn 78)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 78 | **ACQUISITION-CHANNEL LAW (structural).** sakibpro's per-card detail table carries a mutually exclusive row by class: normal cards show "Transfer Market Price / {n} Coins ✔️ VERIFIED"; special cards show "Acquired Via / **{Family} Agent** ✔️ SPECIAL EDITION" and have **no price row at all**. This is the structural explanation for the no-price rule — specials are Agent acquisitions, not market purchases | high | patch | S-0292/0296/0297/0298/0299/0300/0301 |
| 79 | Agent names follow the family: **Champion Agent**, **Team of 2025 Agent**, **Kick Off Agent**, **Classic Agent**, **Dynamic Star Agent** — five distinct Agents confirmed, each tagged SPECIAL EDITION | high | patch | S-0292/0296/0297/0300/0301 |
| 80 | No-price rule extended to **nine families** (adds Champions, Kickoff Stars, Team of 2025 to the previous six), ~22 observations, **zero counter-examples** | high | patch | S-0285/0286/0288/0289/0290/0291/0293/0294/0295 |
| 81 | **Rating-provenance flag:** sakibpro marks normal cards ⚠️ ESTIMATED (OVR computed from stats) and special cards ✔️ OFFICIAL. **Price and rating have independent provenance** — the price field reads VERIFIED even when the rating is ESTIMATED, so sakibpro prices do not inherit the rating-estimation flaw | high | static | S-0298/0300/0302/0303 | **CORRECTED turn 79 — the flags are PER-RECORD, not per-class: prices can also be ESTIMATED (Raphinha 15226 = 2,785 ESTIMATED), and special cards can be ESTIMATED too (de Gea 28324 = 85 ESTIMATED). What survives: rating and price flags vary INDEPENDENTLY within a single record, so a VERIFIED price is not invalidated by an ESTIMATED rating on the same card. The blanket statement 'prices are always VERIFIED' is FALSE and has been withdrawn.** |
| 82 | **DRIFT SPLIT:** normal-card rating drift is a computation artifact (⚠️ ESTIMATED), but special-card drift is a **genuine inter-source conflict** because specials are ✔️ OFFICIAL — Berbatov is 84 OFFICIAL on sakibpro vs 85 on dlsinside | high | patch | S-0300/0298 | **REFINED turn 79 — the split must be applied PER RECORD, not per class. It holds only where that specific record carries the OFFICIAL flag. Berbatov 84 is OFFICIAL, so that gap is a genuine conflict; but de Gea 28324 (Cult Heroes, a special card) is ESTIMATED, so class membership alone does not settle whether a gap is a computation artifact or a real disagreement.** |
| 83 | Family rosters enumerated with IDs: **Kickoff = 2** (Raphinha 27191, J. Alvarez 27127), **Champion = 12**, **Team of 2025 = 11** | high | patch | S-0285/0286/0293 |
| 84 | **Roster verification 17/17 COMPLETE** — all 17 members confirmed present in V13430 (code 160) | high | patch | S-0275/0278/0279..0283 |
| 85 | **IDENTIFICATION: "Évora Dias 28658" = Vozinha** (Josimar José Évora Dias), Cape Verde GK, Cult Heroes 84, Right, 189cm/40, GK Reactions 81 / GK Handling 81. Also rating-drift case #9 (dlsinside 84 vs trending 83) | high | patch | S-0283 |
| 86 | **Pedri resolved:** 27133 = Pedro González López, Team of 2025 CM, **86 ✔️ OFFICIAL** — resolves the standing 86-vs-87 discrepancy in favour of 86 (normal record 17763 = 85) | high | patch | S-0301 |
| 87 | **Simulator route identified:** sakibpro.com/players/simulator.html?loadPlayer={id} (any player id). Upgrades Q-028 from "find the simulator" to "load this URL and screenshot" | high | static | S-0292/0298/0301 |

### Claims promoted (turn 79)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 88 | **The 12-family taxonomy is now EXHAUSTIVELY characterised: all 11 special families carry an explicit Agent row and no price row; only Normal is market-tradeable.** Agent names: Champion, Team of 2025, Kick Off, Classic, Dynamic Star, Dream Star 26, Dream Star 25, World Cup Heroes, Season Pass, Cult Heroes, World Winners — 11 of 11 confirmed, zero counter-examples | high | patch | S-0292/0296/0297/0299/0300/0309/0310/0313/0315/0316/0317 |
| 89 | Family sizes enumerated: **Normal 14,232** · Season Pass 1 · Kickoff 2 · Dream Star 25 11 · Dream Star 26 12 · Team of 2025 11 · Champion 12 · World Winners 8 · Cult Heroes 12 · Dynamic Stars 40 · Classic 32 | high | patch | S-0285/0286/0293/0305/0306/0314/0319 | **REFINED turn 80: Classic is **34** on sakibpro but **32** on dlsinside — a 2-record cross-operator discrepancy, UNRESOLVED. Dynamic Stars 40 and World Cup Heroes 8 are now confirmed on BOTH operators.** |
| 90 | **85 Forward = 2,785: corroborated by a second independent model, but STILL NOT OBSERVED.** Two distinct 85 LW cards (Raphinha 15226, Vini Jr 16320) both read 2,785, and both are flagged ⚠️ ESTIMATED. The value is now supported by two independent computations (sakibpro's model and my linear extrapolation) but no ✔️ VERIFIED price exists for any 85 Forward, so **the cell count stays 20 of 24** | medium-high | patch | S-0311/0312 |
| 91 | **There is NO 85-rated CF in the game.** The 85 cohort is exactly 11 players (B. Fernandes AM, Donnarumma GK, Gabriel CB, Hakimi RB, Pedri CM, Raphinha LW ×2, Valverde CM, Vini Jr LW, Virgil CB, Vitinha CM); the Forward column jumps 86 → 84 with nothing in between. The 85-Forward cell is reachable only via LW, which the tier model equates with CF=SS=LW | high | patch | S-0304/0307/0308 |
| 92 | **CORRECTION (turn 79) to claim 81: the ✔️ OFFICIAL / ⚠️ ESTIMATED flags are PER-RECORD, not per-class.** Prices can be ESTIMATED (Raphinha 15226: price ESTIMATED, rating OFFICIAL) and special cards can be ESTIMATED (de Gea 28324: Cult Heroes, rating ESTIMATED). Claim 81's implication that prices are reliably VERIFIED is withdrawn | high | static | S-0311/0312/0316 |
| 93 | **G-0086 RESOLVED by recharacterisation: record 26841 is a NAMELESS PLACEHOLDER, not a hidden player.** Two independent operators agree: blank name, Spain, GK, 86 OFFICIAL (sakibpro) / 414 (dreamkitsapp), **all stats zero**, weight 0 kg, **DOB Jan 01 1970** (epoch placeholder), generic slug `player`. dreamkitsapp classes it a 'secret player' — 'test characters or hidden content'. **There is no identity to recover; the record is unnamed in the source data too** | high | static | S-0318/0320 |
| 94 | **Nameless stubs are a class, not a one-off:** 26841 (Classic, 86) and 25848 (Normal, 4 OVR) both use the generic slug `player` and carry no name. This is why 26841 resisted every name-based lookup | medium-high | static | S-0318 |
| 95 | **World Winners = 8 cards, and the composition encodes the World Cup-winning nations:** Spain 2026 (Lamine Yamal 27845, Rodri 27843, Cubarsí 27844, Cucurella 28188), Argentina 2022 (E. Martínez 27849, Enzo 27838), France 2018 (Pogba 27846, Pavard 27847) | high | patch | S-0317/0319 |
| 96 | **Legendary Agent pity mechanic:** the World Winners prose states a featured card is **guaranteed every 15 draws**. Note a naming inconsistency — the detail field says 'World Winners Agent' while the prose says 'Legendary Agent' | medium | live | S-0317 |

### Claims promoted (turn 80)
| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 97 | **Facility level cost ladder = 75 / 150 / 225 / 300 / 375 gems — an arithmetic progression (+75) summing to exactly 1,125.** This **explains** the previously unexplained "1,125 gems × 5 = 5,625" figure recorded at turn 52: 1,125 is the cost of maxing ONE facility line, and 5,625 is five lines | medium (ERA-TAINTED: DLS24-era source, Feb 2024) | patch | S-0321 |
| 98 | **Training Facility has 5 levels with a gem discount ladder: L1 5%, L2 10%, L3 15%, L4 "a big jump" (legendary coaches then cost under 200 gems), L5 cheapest coaches.** Each level also unlocks a group of formations. This maps onto the KB's recorded 0/5/10/15/20/30% discount ladder as levels 0-5, resolving the "why is the last step double" puzzle | medium (ERA-TAINTED) | patch | S-0321 |
| 99 | **The two taxonomies reconcile. dlsinside's 11-family census maps onto sakibpro's 12-family taxonomy, and eight counts match exactly.** Decisive case: dlsinside's "Star Players 23" = sakibpro's Dream Star 25 (11) + Dream Star 26 (12) — dlsinside lumps both Dream Star waves together while keeping Dynamic Stars (40) separate. dlsinside's Hidden (270) and Exclusives (7,388) are folded into sakibpro's Normal (14,232) | high | static | S-0322/0323/0324 (+ turn-62 census) |
| 100 | **Cross-operator discrepancy: Classic = 34 on sakibpro vs 32 on dlsinside** (2-record gap, unresolved). The Classic family also contains the nameless stub 26841 | medium-high | patch | S-0324 |
| 101 | **Duplicate records are systematic in Classic, not incidental:** Matthäus 24596 + 27201 (both 86), Batistuta 24595 + 27204 (both 85), Bergkamp 25100 + 27202 (both 85) — same player, two IDs, same rating. Confirms the recycling pattern at record level | high | static | S-0324 |
| 102 | **Batch-id law further refined: the 258xx range also mixes families.** James Rodríguez 25839 is World Cup Heroes while Messi 25841 and Ronaldo 25842 are Champion. This is the third range where id alone cannot determine family | high | static | S-0323 |


## Turn 36 provenance correction

Claims tied to article IDs `7916959134737`, `7917587319313`, `7917423348497`, `7917583876625`, and `17146555181585` are **product-attribution unresolved**. They are listed in the Ultimate Clash Soccer section, but the three bodies reopened this turn do not name a game; section placement and related links do not establish exclusivity. Withdraw the unsupported claim that these IDs appeared in a DLS section listing. Do not use their content as DLS-specific until product metadata or explicit in-article attribution is captured. The General FAQs section `203171905` has 21 enumerated titles; article reading remains partial.


## Turn 37 provenance resolution

Zendesk article JSON assigns `7916959134737`, `7917587319313`, `7917423348497`, `7917583876625`, and `17146555181585` to section `7900693036561` (Ultimate Clash Soccer). Reclassify them as UCS-section support articles; they are not DLS-specific evidence. The bux sale and home/GK kit discrepancies must not be counted as DLS-internal contradictions without independent DLS provenance. Re-audit the previously stated FTG self-contradiction lower bound.


## Turn 38 first-party General FAQ claims

- `214388065`: Google Play incompatibility may arise from chipset/graphics, country, or carrier restrictions; clearing Play Store data may help; no further workaround stated if it fails. General, unstamped.
- `214388105`: Play Store download troubleshooting sequence (website, mobile data, clear cache/data, remove/re-add Google account after restart, contact Google). General, unstamped; not a gameplay data-use recommendation.
- `213853729`: some Bluetooth controllers work with FTG apps; not all brands guaranteed; no DLS-26-specific model list.
- `360009450097`: Apple cloud save is distinct from iCloud; DLS path Settings > Advanced; Apple ID 2FA and matching iCloud account required; play matches to upload. No version stamp.
- `9580096555281`: Google cloud save is distinct from Google Play Games; sign-in appears on supported FTG games. No DLS-specific settings path or version stamp.


## Turn 39 first-party save-route contradiction

- `214387685`: says DLS and several other games do not secure saves on Google Play Games or iCloud and that these services are not used.
- `360000603398`: explicit DLS path to enable Google Play Games Services and Google Play Cloud, then make progress online to upload.
- `360000613657`: explicit DLS path to enable iCloud, play matches for upload, and check iCloud storage.
All three are first-party, unstamped articles. Conflict unresolved; don't reconcile by inference or give a route-change instruction without checking the user's in-game options.


## Turn 40 save-article metadata and video policy

Zendesk metadata: backup/restore article `214387685` is General FAQs section `203171905`, edited 2024-05-15, updated 2026-09-28; Google Play Games and iCloud setup articles `360000603398` / `360000613657` are also in `203171905`, edited 2020-06-04, updated 2026-07-19; DLS transfer article `4413273241873` is DLS FAQs section `203117809`, edited 2024-12-06, updated 2026-09-28. All are marked `outdated=false`; none has a DLS version stamp. Do not resolve their conflicting save-route instructions by recency alone.

Article `360001099097` official body sets non-commercial/gameplay-use conditions (no game music, no false endorsement, limited trademark use, no mixing or repurposing content, EULA compliance, no misleading unpublished-update claim, and non-offensive content). Historic user comments are not evidence.


## Turn 41 support and legacy-title claims

- `360000309705`: FTG support request or community forum are the two routes stated.
- `214387905`: Dream League Soccer Classic removed from stores; new users cannot obtain it; article mentions iOS 11 no longer running older 32-bit apps. Legacy product only.
- `214421705`: DLS Classic kit-import template and direct PNG URL workflow; logo URL max 512x512; not DLS26.
- `213853689`: FTS15 removed from stores and unavailable to new users; legacy product only.
- `360017063617`: “Super Players” described as rare enhanced player types from Events/rare packages with grey or gold shiny background. Game/version scope not stated; await section metadata.


## Turn 42 product attribution correction

Zendesk metadata assigns `360017063617` (Super Players) and `360000001969` (player types) to Score! Match FAQs section `115001619089`. Their grey/gold appearance and player-type attributes are Score! Match documentation, not DLS evidence. Article `360000002405` says Gems are bought through Store via the plus by the balance, for real money, with bill-payer permission; no title/version or rates are stated. Article `360000420025` offers generic VPN, signal, router, and DNS troubleshooting; no product/version is named.


## Turn 43 section attribution and Parents’ Guide

Zendesk metadata assigns `360000002405` (Gem purchase) and `360000420025` (connection issues) to Score! Match FAQs section `115001619089`; do not use either as DLS-specific guidance. Parents’ Guide section `360000030369` lists eight article titles. `360000191445` warns about third-party “free gems”/unlimited-currency sites and says external virtual-currency trading is not allowed; `360000205129` says verify Charged status, restart with a strong connection, reopen, enter Shop to validate, then contact support if unresolved. Both are general, unversioned guidance.


## Turn 44 Parents’ Guide articles

Five unversioned general FTG pages read: `360000191385` (purchase authentication/restriction steps for Apple and Google Play), `360000205049` (FTG says Apple refunds are controlled by Apple; Google Play users use purchase history/Report a problem; contact FTG only if referred), `360000204889` (FTG’s general 13+ statement and parental-control links), `4408249822609` (age-banding and ad/notification personalization), and `360000191545` (support form, no phone support, billing privacy). Do not treat the page text as current DLS26 menu instructions or a DLS app-store age rating. On `4408249822609`, FTG says turning personalization off yields generic ads, not no ads; youngest band is permanently unpersonalized. DLS video-clips and Facebook-login links were discovered; see reconciled frontier.


## Turn 45 — Parents’ Guide closure and DLS support metadata

`360000191485` says FTG apps do not use private chat facilities; do not broaden this into “no in-game interaction.” Metadata: Parents’ Guide section `360000030369`, created 2018-02-02, edited 2018-02-05, updated 2026-06-16, not outdated. `360017166918` is DLS FAQs section `203117809`, updated 2026-07-16, edited 2021-01-20, not outdated. `9804887423121` is DLS FAQs section `203117809`, updated 2026-10-05 but edited 2024-12-06, not outdated; last-updated metadata does not prove same-day body revision. Age article `4408249822609` belongs to Parents’ Guide, last updated 2024-02-07. No DLS26 build confirmed.


## Turn 46 — DLS metadata and product-specific User ID routes

Zendesk section metadata places `37082887837202` (DLS User ID), `360005680437` (DLS mobile data), `360008904718` (blocked from DLS), and `360004717278` (DLS19 profile in DLS25) in DLS FAQs `203117809`; none confirms DLS26-specific applicability. DLS User ID route: Options → Advanced → System Info → Copy Info. The similarly named `37083387788434` is in Score! Match FAQs `115001619089`, with different blue-gear steps; never attribute it to DLS. The DLS19→DLS25 article does not settle DLS25→DLS26 transfer.


## Turn 47 — support article product attribution and DLS graphics

`360000011145`, `360000002205`, and `360000250309` are Score! Match FAQs (`115001619089`) and are not DLS evidence. `360000598437` is DLS FAQs (`203117809`), but the graphics instructions are unversioned and not verified for DLS26/current device. Article ID `441327324187` rendered an FTG not-found page; its exact HTTP code was not exposed. It is distinct from DLS save-data article `4413273241873`.


## Turn 48 — storefront disclosures and event card

Google Play DLS package `com.firsttouchgames.dls7` lists DLS 2026, ads/IAP, Everyone, in-game purchases including random items, 100M+ installs, and updated date 2026-09-14; store marketing says 4,000+ players/8 divisions/etc. No app version shown. Review count conflicted across retrieved chunks (15M vs 14.4M); ignored. Data Safety categories are developer-provided and flagged as variable by version/use/region/age. Apple English League Classics card says both “EVENT ENDED” and “LIVE EVENT”; no status inference. FTG Games page is generic/undated and links the same App Store ID under a DLS2020 label.
