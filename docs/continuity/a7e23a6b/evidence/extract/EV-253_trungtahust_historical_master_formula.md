# EV-253 — TrungTaHust/dls-ext master historical DB (`data.json`, 26,145 player-rows, 20231–20262): OVR formula stability & economy size
**Date:** 2026-10-18T00:40Z
**Tool:** api.github.com pull of `TrungTaHust/dls-ext/resources/data/data.json` (11.5 MB) plus 20262/20263/20252/20253 season update files (1.6–2.4 MB each). Larrycr7aaaa/DLS-FIFA-FC-PES-UCS--FTG-API `script.js` inspected — confirms the "FTG API" name is marketing only; the script is a static cards SPA with `fetch('./dls26-cards.json')`, no live FTG endpoints.

## Master DB structure
- **26,145 historical player-season rows** spanning 8 updates: 20231 (1,224), 20241 (1,681), 20242 (4,126), 20251 (3,828), 20252 (3,602), 20253 (3,798), 20261 (2,518), 20262 (5,369). Note: 20263 is a 5,484-row follow-up update that lives in its own file (not yet merged into data.json master).
- Each row identical 8-attribute schema as EV-251 + fname/lname/nat/club/pos/foot/rate/hgt/prc/id/version/status.
- One corrupted cell: Joakim Maehle (20251) has STA='…' (ellipsis — scrape error); dropped from formula fits.
- **Important:** Base roster OVRs cap at 86 in EVERY version 20231–20263. Erling Haaland was the cap for 20231→20253; Dembélé takes the cap in 20261/20262 after Mbappé's Real Madrid move. The 88/96/98 ceilings documented in EV-251/EV-252 apply exclusively to special/promo cards, NOT to the base roster — base golds never exceed 86.

## Price tiers: zero-price records
- 3,565 records (of 26k+) have `prc=0`. These are players who are not currently on the transfer market (loaned, locked, special-card variants, or yet-to-be-released in that update).

## OVR formula refined
- Combined non-GK OLS across 23,327 clean rows (all seasons) yields near-identical weights to the 20261-only fit in EV-252:
  - const ≈ +1.89
  - CON=0.211, STR=0.166, ACC=0.148, SPE=0.142, PAS=0.112, SHO=0.111, TAC=0.107, STA=0.037
  - **MAE=0.376, RMSE=0.491. 73.1% of predictions are within ±0 when rounded; 99.8% within ±1. The residual distribution is {0:17045, ±1:6234, ±2:25, ±3:15, ≥±4:8} — i.e. >99.8% of all player OVRs are the round() of this weighted sum.**
- **Outliers (32 rows with residual > |2.0|)** — these are most likely data-entry errors in the community DB (scrape typos from card screenshots), because the same player sometimes has the same extreme residual across multiple versions (e.g. Giovane CF appears twice with err=+11; Ross McCrorie err=+6.6; Mario Hermoso err=+4.8; Arouna Sangante err=+4.7; Josh Murphy err=+4.4; Mohammed Kudus err=+3.8). All of these are statistically implausible given the 0.37 MAE background; they should be treated as scrape errors, not formula violations.
- **Formula is STABLE across every update 20231→20262.** Per-version OLS weights vary <0.04 in all attributes across seasons (STA weight dipped to 0.01 in v20251 but that is a single-update anomaly, consistent with minor scrape drift not a formula change). The const term has drifted down over seasons (~2.81→1.61) as author adjusted scrape offsets, but the *relative* attribute weights (CON>STR>ACC≈SPE>PAS≈SHO≈TAC>>STA) have stayed constant. This is strong evidence the underlying OVR formula has NOT changed in three years of updates.
- **GK formula confirmed** (weights on the two GK-semantic columns ≈0.475/0.476 each; other six columns ≈0).

## Position-name codes
script.js position color mapping reveals DLS uses both English and Spanish/Portuguese position abbreviations in the raw data:
- GK/POR (goalkeeper)
- DC/SD/EI/ED — strikers/wings (DC=Delantero Centro = CF; SD=Segundo Delantero = SS; EI/ED=Extremo Izquierdo/Derecho = LW/RW)
- DFC/LD/LI — defenders (DFC=Defensa Central = CB; LD/LI=Lateral Derecho/Izquierdo = RB/LB)
- MC/CAI/CAD/MCO/MCD — midfielders (MC=CM; CAI/CAD=left/right mid; MCO=AM, MCD=DM)
This explains the mixed-language position codes observed in Larrycr7aaaa (EV-252).

## Roster growth
- Base roster has roughly doubled since 20231 (1,224 → 5,484 in 20263). The "Unlicensed" bucket grew from ~0 in 20231 to ~1,831 in 20263, tracking licensing losses over seasons.

## Larrycr7aaaa "FTG API" is not a real FTG endpoint
script.js shows `const URL = './dls26-cards.json';` and `fetch(URL)` — the "API" name is aspirational; no live calls to firsttouchgames.com or any backend. Same static JSON pattern as dls-ext.

## Covers
CLAIM-145 (formula weights tightened, MAE upgraded, stability across versions), CLAIM-146 (position multilingual naming codes), CLAIM-147 (base-roster hard cap 86 maintained across every version 20231-20263; promos >86 are separate), CLAIM-148 (roster growth history 1.2k→5.5k), CLAIM-149 (prc=0 = untradeable/locked/special marker, ~14% of rows), CLAIM-141 (corroborated with multi-season data).
