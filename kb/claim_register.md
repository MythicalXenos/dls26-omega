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
