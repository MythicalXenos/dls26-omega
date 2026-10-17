# EV-251 — TrungTaHust/dls-ext (Vietnamese DLSStats PWA): full stat schema + roster + formula
**Date:** 2026-10-18T00:15Z
**Tool:** api.github.com raw pull (allowlisted) of `TrungTaHust/dls-ext` (the full DLSStats Sencha/Ext JS PWA, not the earlier shell).
**Origin:** Single-Vietnamese-dev offline DLS26 stats companion app. The repo ships ~24 MB of season data JSONs:
- `resources/data/20261.json` (Season 2026, update 1): **2,518 players**, full attribute rows + club/nat/pos/height/foot/OVR/price/id/status.
- `resources/data/20251.json`, `20252.json`, `20253.json`, `20262.json`, `20263.json`, `20241.json`, `20242.json`, `20231.json`: prior seasons/live updates (not yet pulled individually; sizes 0.5–2.4 MB each → tens of thousands of historical rows in total).
- `resources/data/special.json`: **70 special/legendary cards** (Champion/Classic/Star/Team) across vintages 1984–2026.
- `resources/data/formations.json`: default formations for **149 clubs and 79 nations**.
- `resources/data/price_map.json`: 160 price-tier entries; keys encode OVR + sub-tier (e.g. 864=top price 2800 for OVR 86, 863=2600, 862/861=0 = reserved/locked).
- `resources/data/player_id.json`: 6,534 player ID→name records (range 1000–7460).
- `resources/data/checklist.json`: 179 clubs × 40 nations with update flags.
- `resources/data/id_stats.csv`: 6,461 player id→fname/lname records.

**Authenticity limits:** Fan/community PWA. Data schema matches in-game attributes 1:1 (same 8-attribute names DLS uses across versions) and the 20261 price of 2800 for top-tier gold players matches EV-085 (SakPro gold cap 2800) and EV-078 (Ferdi Akgul 59 CB 120 coins — within the 120 band for 59 per price_map 59x tiers). Two-source corroboration is strong but build version / last live sync date is not stated in the repo. Treat as High-Confidence community data rather than Confirmed official.

## Attribute schema (8 core attributes, outfield)
Every outfield player row carries these eight integer stats (0–100), in this order:
`SPE` (Speed), `ACC` (Acceleration), `STA` (Stamina), `STR` (Strength), `CON` (Control), `PAS` (Passing), `SHO` (Shooting), `TAC` (Tackling).
GK rows reuse the same 8 fields but with GK semantics (SHO behaves as GK reflexes/handling proxy per the GK-only OLS; see EV-252). Larrycr7aaaa's API (EV-252) confirms that for dedicated GK cards the columns are literally renamed `GKR` (GK Reflexes) and `GKH` (GK Handling) in place of two of the outfield slots — the underlying 8-attribute grid is the same width.

Additional per-row fields: `fname`, `lname`, `nat`, `club`, `pos`, `foot` (L/R/B), `rate` (OVR 1–100), `hgt` (cm), `prc` (transfer-market coin price), `id`, `version` (season-update code), `status` (1=active).

## 2026 season 1 distribution (2518 players)
- OVR range 52–86 (base/regular cards only — no special/promo cards in this file).
- Attribute ranges: SPE 39–94, ACC 36–95, STA 43–93, STR 41–95, CON 37–95, PAS 36–93, SHO 20–96, TAC 15–94.
- Heights 162–206 cm; foot R 1793 / L 650 / B 75.
- Top of base roster: OVR 86 = Mbappé (Real Madrid), Haaland (Man City), Kane (Unlicensed/Bayern), Dembélé (Paris SG) — all at the cap price 2800 coins.
- 367 players on team "Unlicensed" (confirms licensing gaps — e.g., Kane listed as Unlicensed because Bayern is not licensed in DLS26).
- Positions: CB 477, CF 324, CM 290, GK 263, DM 230, RB 156, AM 153, LB 143, LW 109, RW 104, RM 88, LM 81, LWB 48, RWB 34, SS 18.
- Clubs: 124 (some nations are under "Unlicensed").

## Special cards (special.json, 70 rows, vintages 1984–2026)
- Types: Classic (24), Star (23), Champion (12), Team (11). Same 8-attribute schema plus `version` year and `pos_id` (1=forward/attacker, 2=midfielder, per-row inspection — not fully enumerated).
- **Cap for vintage/historical Champion cards in special.json is 88** (Cristiano Ronaldo Champion CF 88, Lionel Messi Champion LW 88) — corroborates EV-248 resolution.
- "Team of 2025" (Team type, year 2025) peaks at 87 (Kane CF, Mbappé CF, Dembélé RW).
- 2025/2026 "Star" type is 82–84 (rising/breakout players: Trafford 82 GK, Wood 84 CF, Thiago 84 CF, Yildiz 84 SS, etc.).
- **NOTE:** special.json max is 88, which is LOWER than EV-246/248 FBGD OVR ceilings (Dynamic Stars 96 Nico Williams per dreamkitsapp; Champions 98 Messi/Ronaldo per Larrycr7aaaa API EV-252). Special.json in dls-ext appears to hold only the **vintage Champions/Classics/Stars/Team-of-Year** subset, not the current-event Dynamic Stars / WC Heroes / Dream Stars / WC Champions / Cult Heroes / Legends cards — those are in the per-season update files (20262/20263 etc.) or in separate promo lists (EV-252).

## Default formations (149 clubs, 79 nations)
Examples: Man City 4-1-4-1, Man Utd/Liverpool/Chelsea/Barcelona/Juventus/AC Milan 4-2-3-1, Arsenal/Tottenham/Real Madrid 4-1-2-3, Paris SG 4-3-3, Inter 3-5-2, Napoli 3-4-2-1; nations: Argentina/England/Spain/Portugal/Netherlands/Belgium 4-3-3, Brazil/France/Germany/Croatia 4-2-3-1, Italy 3-5-2. Full table in the JSON.

## Price tier structure
Keys in price_map.json are 3-digit numbers `ABc` where `AB` is OVR (52–86) and `c` is a 1–4 sub-tier within that OVR (higher = better statline). Values are in coins. Top of the table is 2800 (86_4); 86_3=2600, 86_2/86_1=0 (locked/not-on-market variants, likely special/promo cards that can't be sold). At the bottom, 54_1=20 coins. Per-OVR there are exactly 4 sub-tiers. **The "prc" value in the 20261 flat roster appears to be the tier-4 price for each OVR** (all 86s = 2800, all 85s = 2625, etc.), which means in-game market price refines within each OVR by actual stat spread — confirming EV-085's community observation that players of the same OVR trade at different prices.

## Covers
CLAIM-137 (8-attribute outfield stat schema), CLAIM-138 (GK schema uses two GK-specific sub-attributes), CLAIM-139 (price_map 4 sub-tiers per OVR, coin values 20–2800), CLAIM-140 (default formations for 149 clubs + 79 nations), CLAIM-141 (2026s1 roster 2518 players, OVR 52–86 base), CLAIM-142 (vintage special card ceiling 88, separate from promo cards), CLAIM-143 (Unlicensed team bucket, 367 players incl. Kane), CLAIM-078 (Ferdi Akgul-like prices match tier bands), CLAIM-085 (SakPro gold price cap 2800 corroborated), CLAIM-007/060/130/132 (Messi/Ronaldo multi-card structure), CLAIM-001/094 (position set / build version context).
