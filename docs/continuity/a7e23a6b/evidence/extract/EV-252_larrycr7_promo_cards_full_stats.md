# EV-252 — Larrycr7aaaa/DLS26-API (Spanish): 41 current-event promo cards with full statlines, up to OVR 98
**Date:** 2026-10-18T00:15Z
**Tool:** api.github.com raw pull of `Larrycr7aaaa/DLS26-API/dls26-cards.json` (16.5 KB).
**Origin:** Spanish-language DLS26 cards API/spa built by community dev Larrycr7aaaa. One of ~12 sibling repos (UPDATED-DLS26-data-PF, dls26-UPDTD, ultra-updated-dls26-and-api, specialcardsdls-api-and-database-css-html-js-json, 26dls-41-cards-data, DLS-FIFA-FC-PES-UCS--FTG-API, DLS-DATA-BASE) with overlapping/evolving copies of the same promo-card dataset.

## Card types observed (in this 41-card snapshot)
- Champions (5): OVR 95–98, avg 96.4. The 98s are **Lionel Messi (DC/CF, Barcelona)** and **Cristiano Ronaldo (EI/LW, Real Madrid)** — this is a historical/vintage "Champions" tier (different from EV-251's 88-rated Champion vintage, which used a smaller card pool; these are the all-time-great endgame cards).
- WC Champions (8): OVR 94–97 — World Cup Champions promo (Lamine Yamal 97 RW, Rodri 97 DM, Emiliano Martínez 96 GK, etc.).
- WC Heroes (4): OVR 95–97 (Ronaldo 97 CF, Navas 95 GK, etc.).
- Dynamic Stars (6): all OVR 96 (Arda Güler, Eze, De Paul, Ríos, McKennie, plus others). **Corroborates EV-190's Nico Williams 96 Dynamic Stars cap**, and slightly refines CLAIM-006 ceiling (which had said 96 — confirmed, but Champions tier reaches 98).
- Cult Heroes (6): 93–95 (Vozinha 93 GK, etc.).
- Dream Stars (4): 93–94.
- Team of 2025 (4): 87–97 (Mbappé 97, Kane 97).
- Legends (3): 93–96.
- Nuevas Especiales (1): 82.

## Attribute schema (confirms EV-251)
Outfield cards use the same 8 attributes as dls-ext's base roster: SPE, ACC, STA, STR, CON, PAS, SHO, TAC (0–100). GK cards (3 in this set) replace two of the outfield slots with explicit **GKR (GK Reflexes) and GKH (GK Handling)** labels:
- Keylor Navas (WC Heroes, 95 GK): uses GKR=100/GKH=85 in place of STA/SHO.
- Vozinha (Cult Heroes, 93 GK): GKR=100/GKH=81.
- E. Martínez (WC Champions, 96 GK): GKR=95/GKH=94.
This confirms the 8-attribute grid is universal, with two columns re-interpreted per position.

## OVR formula corroboration
A simple OLS linear fit on EV-251's 2,255 non-GK base cards produced weights const=1.86, SPE=0.143, ACC=0.137, STA=0.055, STR=0.164, CON=0.225, PAS=0.107, SHO=0.100, TAC=0.099 (MAE=0.37, RMSE=0.46 — i.e. rate = 1.86 + 0.225·CON + 0.164·STR + 0.144·SPE + 0.137·ACC + 0.107·PAS + 0.100·SHO + 0.099·TAC + 0.055·STA). **Applied to Larrycr7aaaa's outfield promo cards, the same coefficients predict all 38 promo outfield cards within ±1 OVR point at MAE=0.70**, strongly suggesting DLS26 uses a single linear formula across base AND promo cards rather than a position-weighted formula. CON (ball control) is the heaviest-weighted attribute; STA (stamina) the lightest. The small residual bias (~+0.3 to +0.9 on top promos) is within card-rounding tolerance.

## Corrections to prior claims
- CLAIM-006 ("Max visible OVR 96 (Nico Williams Dynamic Stars)") is incomplete: Champions-tier cards reach **98** (Messi/Ronaldo in Larrycr7aaaa's pull). EV-251's vintage-cap 88 is for an older card class (Champion 2014/2012/2018 vintage subset); current-event Champions can reach 98. **Downgrade CLAIM-006 to Community Consensus and add CLAIM-144 for the corrected ceiling hierarchy.**

## Covers
CLAIM-137 (schema corroborate), CLAIM-138 (GK-specific columns GKR/GKH), CLAIM-144 (OVR ceiling 98 Champions tier), CLAIM-145 (linear OVR formula weights, MAE<0.5 base; <1.0 promo cross-validated), CLAIM-006 (corrigendum), CLAIM-024 (Dynamic Stars 96 corroborated, not max overall).
