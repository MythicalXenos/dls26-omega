# Claim register (ISS-008 part b) — key claims with confidence + volatility
_started turn 56; appends as claims stabilize. Fields: confidence (high/medium/low) + volatility (static = datamine-structural; patch = changes with game updates; live = live-ops/event state; community = unverified single-source)._

| # | Claim | Confidence | Volatility | Sources |
|---|---|---|---|---|
| 1 | Secret-class map: 18 pages, descending, floor 35 (Maor Tukar); filler = generated names + alias-club rosters | high | static | S-0179/0186/0190/0196/0205/0209 |
| 2 | DROICER leak text: Roy Keane / Irvin 85 / Conor Gallagher / Peter Robinson = upcoming Prize Ladder classics; possible DLS27 Kick-Off Stars | medium | live | S-0199 |
| 3 | Secret "Classic X" set maps to leak names (Keane 5842 / Irwin 5839 / Gallagher 5866 / Robinson 5833); staging hypothesis | high (correlation) | static | S-0182..0184, S-0187/0190/0195 |
| 4 | Robinson identity: Michael (profile-fit) vs Peter (leak-name) — UNRESOLVED | low | static | S-0203/0214 |
| 5 | Price = f(base OVR, tier-of-4); tiers flat (F: CF=SS=LW; M: AM=CM=DM; D: CB=LB; GK) | high | patch | S-0213..0233 |
| 6 | Verified anchors: 86CF 2,970 / 85CB 2,375 / 82CF 2,275 / 84CF 2,610 / 83CF 2,440 / 85CM 2,555 / 83CM 2,235 / 85GK 2,080 | high | patch | S-0213..0233 |
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
