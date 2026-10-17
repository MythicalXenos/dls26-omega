# EV-246 — FootballGamingBD/DLS26_PD player-database and card-creator JSON
**Date:** 2026-10-17T23:20Z
**Tool:** GitHub API (api.github.com — allowlisted) raw-content fetch; no clone.
**Origin:** community-maintained card-creator web app at footballgamingbd.online, repository `FootballGamingBD/DLS26_PD` (JavaScript PWA, 446 MB repo, last push 2026-10-12).
**Authenticity limits:** community database, not official; card-type labels are from the tool and may differ from FTG's internal names. OVRs and positions are community-scraped/hand-curated and may contain individual errors; the Cult Heroes list (CLAIM-129) matches our 12-name roster, which is a corroboration point. File sizes: `Player.json` 1.05 MB, `New_Player.json` 19 KB, `Upcoming_Player.json` 4 KB, `Cardcreator.json` 8.7 KB, `Method.json` 1.2 KB.

## What the data contains (verbatim schema inspection)
`Player.json` (n=1006): per-card `id`, `popup_id`, `name`, `searchName`, `slug`, `card_type`, `rating` (0–99), `year`, `Position-box` (filename; e.g. `Rw.png`, `Cf.png`, `Gk.png`, `Cb.png`, `Am.png`, `Dm.png`), `card-bg`, `border`, `rating_circle`, `game-card-bg`.
`New_Player.json` (n=15): 12 Cult additions + 3 Season Pass players announced after initial DB.
`Upcoming_Player.json` (n=3): 3 Classic players announced as upcoming (Torres 86 Classic 2006, plus two others of similar profile).
`Cardcreator.json`: maps card-art assets to rating-circle thresholds (NonMax 1-59/60-69/70-79/80-89; Max 90-99 implied by filename) and folder layout.
`Method.json`: acquisition icons — coins (legendary/rare/common), star_agent (DS25/DS26/Dream Star), cult (cult keyword match), plus implicit tier mapping.

## Numerical findings (computed from the file)
- **Roster size at snapshot**: 1024 cards (1006 base + 15 new + 3 upcoming). This is MUCH smaller than CLAIM-116's dlsinside totals (14,435 players, including generics/Hidden/Exclusives). The footballgamingbd set covers only visible/special-card artwork, not the grey/rare base pool.
- **Card-type distribution (base)**: Rare 695, legendary 167, Dynamic 40, Classic 33, Cult 12 (+12 new = 24 Cult total), champion 11, Dream Star 2026 11, T26 10, Dream Star 2025 10, World Cup Heroes 8, World Cup Winners 8, Season Pass Player 1 (+3 new = 4).
- **Rating ranges by card_type** (min/max):
  - Rare 70–79 (n=695)
  - Dynamic 82 flat (n=40) — confirms base Dynamic Star cards are 82 (matches CLAIM-007 upgrade-path structure in L-001 which described +1/+2 upgrades from 82)
  - Dream Star 2026 82–84 (n=11)
  - Dream Star 2025 83–84 (n=10)
  - Cult 83–85 (n=24)
  - Classic 82–86 (n=36)
  - World Cup Heroes 84–87 (n=8)
  - World Cup Winners 84–87 (n=8)
  - Season Pass Player 82–85 (n=4)
  - T26 85–87 (n=10)
  - legendary 80–86 (n=167)
  - champion 82–88 (n=11)
- **Top OVRs observed** (ties broken arbitrarily):
  - 88 champion — RONALDO Lw, MESSI Cf (two champion cards at 88, not 87; this is the highest observed)
  - 87 T26 — O. DEMBÉLÉ Rw, MBAPPÉ Cf, KANE Cf
  - 87 World Cup Heroes — RONALDO Cf, MESSI Ss
  - 87 World Cup Winners — RODRI Dm, YAMAL Rw
  - 86 legendary (L. YAMAL Rw, HAALAND Cf, OLISE Rw, KANE Cf, O. DEMBELE Cf); T26 (HAKIMI Rb, PEDRI Cm, LAMINE YAMAL Rw, M. SALAH Rw); Classic (MATTHÄUS Am/Dm, RIVALDO Lw, CANNAVARO Cb); World Cup Heroes (DE BRUYNE Am); World Cup Winners (POGBA Cm, MARTÍNEZ Gk); plus Cult capped at 85.
- **Position labels** observed in `Position-box` filenames: Gk, Rw, Cf, Rb, Cm, Am, Dm, Cb, Lw, Lm, Rm, Cd (implies CDM), Lb, St, Ss. These match GS-011/T-022.
- **Teams**: 212 team entries in `Team.json` (club sides; national teams not enumerated).
- **Vozinha confirmation**: Vozinha at GK 83 Cult 2026 (slug vozinha-83-Cult-2026) — confirms GS-040/CLAIM-129 resolution (83, not 84).
- **Newly-observed Season Pass Player João Pedro 82** per news item dated 2026-09-06 — confirms that Season Pass continues to release cards outside the named collections.

## Corroborations
- Cult Heroes 12-card roster exactly matches CLAIM-129 (names/positions/ratings agree).
- World Cup Heroes Messi 87 (SS) corroborates CLAIM-130.
- Dynamic Stars base 82 corroborates L-001 (CLAIM-094-range), CLAIM-007 (base 82).
- T26 max 87 — Dembélé/Mbappé/Kane at 87, not 86. This is new (the previous claim set had base top at 86 and specials could exceed).

## Caveats
- This is a card-ART database, not a stat database — only OVR and position, not the 0–1000 scale attributes.
- `champion` Ronaldo/Messi at 88 would be new information; we must not upgrade CLAIM-007/060/130 beyond High Confidence without cross-check, because dreamkitsapp/dlsinside previously capped Messi at 87 in GS-041. Mark as potential conflict rather than immediate overwrite.
- Tooling language is Chinese; the app is clearly a fan tool (DLS26China WeChat public-account branding in `index.html`), not affiliated with FTG.

## Covers
CLAIM-131 (new, roster distribution), CLAIM-132 (new, coach DP model in separate EV-247), CLAIM-133 (new, top-OVR update and champion-88 potential conflict), CLAIM-007 (corroborates 82 Dynamic base), CLAIM-129 (corroborates Cult 12 roster), CLAIM-130 (corroborates Messi/Raphinha/Cucurella), CLAIM-059 (corroborates multi-scheme taxonomy).
