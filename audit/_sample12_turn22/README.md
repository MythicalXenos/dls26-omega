# SAMPLE 12 (turn 22) — post-reopen verification after GitHub sweep
Date: 2026-10-17T23:30Z. Same stratified draw.

## Draw
| Claim | Tier | First-pass | Post-repair |
| --- | --- | --- | --- |
| CLAIM-106 | Confirmed | WARN (covers) | OK |
| CLAIM-125 | Confirmed | OK | OK |
| CLAIM-034 | High Confidence | OK | OK |
| CLAIM-021 | High Confidence | WARN (covers) | OK |
| CLAIM-052 | Community Consensus | WARN (covers) | OK |
| CLAIM-110 | Community Consensus | OK | OK |
| CLAIM-112 | Speculative | OK | OK |

**Post-repair: 7 OK / 0 WARN / 0 BAD.** Three covers-lag WARNs back-stamped (EV-145, EV-116, EV-181/175/179).

## Turn-22 new deliverables (research only, first real net-new research since the corpus import)
- Outbound probe confirms all non-allowlisted hosts remain TLS-blocked (curl 35 across 30 hosts including Reddit/YT/TikTok/IG/FB/APKMirror/Play/App Store/support.ftgames/Google). `api.github.com` returns 200; `raw.githubusercontent.com` also fails TLS (000). ACCESS_BOUNDARY unchanged — the only research surface still reachable is GitHub code/repo search + registry metadata.
- Exhaustive GitHub code/repo sweep (`scripts/turn22_github_sweep.py`, 733 hits) surfaced two material non-spam repositories:
  1. **`FootballGamingBD/DLS26_PD`** (JS PWA card-creator tool, last push 2026-10-12): full player/card/team JSON DB, 1024 visible cards, OVR ranges per card type, Vozinha 83 confirmed, two Messi/Ronaldo "champion" cards at 88 OVR (potential conflict with dreamkitsapp's 87 ceiling). Saved under `logs/research/footballgamingbd/`. EV-246.
  2. **`LeoH321/dls26-tool-CB`** (single-file HTML/JS tool, DLS26China WeChat community): encodes a Chinese-community DP model of coach upgrades — +1/+2/+3 gains per rarity, weighted stat selection with CON weight 2, capacity pool cost = sum(weight)×rarity, stat cap 100, fractional over-cap allocation. EV-247.
- Three new claims added:
  - **CLAIM-131** High Confidence: card-roster distribution from the FootballGamingBD snapshot (counts/ranges/position labels/212 clubs).
  - **CLAIM-132** Speculative: POTENTIAL CONFLICT — champion 88 ceiling vs prior 87 ceiling; flagged for Step 2.
  - **CLAIM-133** Community Consensus: coach DP model (+1/+2/+3, weights, capacity pool, random k-combinations); revises CLAIM-105 (the "+1" rumor was common-coach-only) and partially corroborates/revises CLAIM-104.
- Sample 12: 7/7 OK post-repair. Cumulative over 84 sampled claims: **2 substantive errors (~2.4%)**, six consecutive clean samples.

## What was examined and was junk/spam
- `wasswacosmas/*`: polyglot fan-site boilerplate (DLS26GameManager.cs/.cpp/.java/.swift stubs with no real game logic); fan template.
- `upcashh/dls`: static HTML phishing-style login pages.
- `iSharaf6/blocky-league`: unrelated football game clone, TypeScript/Capacitor, not DLS data.
- `Beexly/gse-competitive-intel`: SEO/sports-betting intelligence corpus, not DLS-specific.
- `crepeia/google-play-store-scraper-game-addiction`: generic Google Play scraper, no DLS game data.
- `danielionut883-eng/DLS-26-Hack-Mod-Apk-…`: hack-spam landing page.
- Search hits for `com.firsttouchgames.dls7` are package-list mentions in unrelated analytics/launcher apps; no save editors, no stat tables, no code.
- Code search returned 213 hits for `"dream league soccer" OVR` and 155 for `"Dream League Soccer 2026"`; after filtering, the two repos above are the only ones with primary DLS26 data content. This corroborates earlier negative findings (no legitimate stat editor, no decompiled source, no useful code on GitHub).

## Cumulative tracking
| Sample | Turn | OK (post) | BAD | Subst errors |
| --- | --- | --- | --- | --- |
| 3 | 12 | 7 | 0 | 0 |
| 4 | 13 | 7 | 0 | 0 |
| 5 | 14 | 3 | 1 | 1 (C-009) |
| 6 | 15 | 5 | 1 | 1 (CLAIM-020) |
| 7–12 | 17–22 | 7 each | 0 | 0 |
