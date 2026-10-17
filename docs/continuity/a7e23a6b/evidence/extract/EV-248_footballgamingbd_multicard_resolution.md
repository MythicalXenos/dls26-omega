# EV-248 — FBGD multi-card-per-player resolution and champion-88 corroboration
**Date:** 2026-10-17T23:40Z
**Tool:** github-api raw fetch + local JSON parse of logs/research/footballgamingbd/Player.json (+ New_Player/Upcoming_Player), cross-checked against EV-187 (dreamkitsapp player listing) and EV-190 (dreamkitsapp "best players" page).

## Findings

1. **Multi-card-per-player confirmed.** Star players (Messi, Ronaldo, etc.) have MULTIPLE cards in different collections/rarities with distinct OVRs. For example:
   - Cristiano RONALDO: legendary 82 Cf (base-legendary), champion 82 Rm (champion lower variant), **champion 88 Lw** (top Champion card), World Cup Heroes 87 Cf.
   - Lionel MESSI: legendary 83 Ss (base-legendary), champion 84 Rw, **champion 88 Cf** (top Champion card), World Cup Heroes 87 Ss.
   - This explains why prior OVR snapshots (CLAIM-007 Feb-2026 "top OVR 86") reported lower values: they sampled base-legendary cards only.
2. **Champion cards 82–88** (FBGD n=11: champion 82–88 range, not uniform 88). Card-art naming: "champion" cards use "Champion-max/nonmax-card.png" and rating-circle "Max-90-99.png" for ratings 90+ or "Nonmax-80-89.png" for 80–89. OVR 88 is the MAXIMUM observed champion card (Ronaldo/Messi LW/CF at 88); other champions sit at 82–87.
3. **World Cup Heroes 87** for both Messi (SS) and Ronaldo (CF), consistent with EV-190 and CLAIM-130.
4. **Legendary base 80–86** is confirmed (legendary n=167, min 80, max 86 — Yamal/Haaland/Olise/Kane/Dembele at 86).
5. **T26 cards 85–87** (T26 = likely "Team of 2026"): Dembélé/Mbappé/Kane at 87, Hakimi/Pedri/Yamal/Salah at 86. This collection name was previously rendered by dreamkitsapp as "Team of 2025" for 87-tier — likely seasonal (2025 → 2026) renaming per the real-world football calendar.
6. **Bio text for champion cards**: Ronaldo 88 references 2014 Real Madrid Champions League win (tenth title = "La Décima"); Messi 88 has a similar historical-season bio. These are themed "historic season" special cards, not current-form ratings.

## Corroboration with prior EVs
- EV-187 (dreamkitsapp): explicitly lists "Champion players (Cristiano Ronaldo 88 LW PT)" and "Messi 87" under World Heroes.
- EV-190 (dreamkitsapp /best-players/): lists Cristiano Ronaldo 88 (LW/CF PT), Lionel Messi 88 (CF/RW AR) as special cards under team t258.
- FBGD adds the card-level slugs (cristiano-ronaldo-88, lionel-messi-88), popup IDs (popup-ronaldo-88, popup-messi-88), bios, kit filenames (Ronaldo88-C.webp, Messi88-C.webp), and position boxes (Lw.png, Cf.png).
- **Two independent community databases agree on 88 as the current visible OVR cap.** The "87" ceiling in CLAIM-130 was a partial reading (World Heroes variant 87 exists alongside the 88 Champion variant).

## Resolution
- Champion 88 is real and two-source corroborated.
- Base-legendary cap remains 86.
- Dynamic Star 96 from L-001 is an UPGRADED end-of-event card, not the base — base Dynamic Stars are 82 flat (EV-246).
- OBSERVED MAX VISIBLE OVR in any collection is therefore 88 (champion Messi/Ronaldo), with event-upgraded Dynamic Stars reaching 96 (CLAIM-095/L-001 Nico Williams 96, etc. at end-of-event).
