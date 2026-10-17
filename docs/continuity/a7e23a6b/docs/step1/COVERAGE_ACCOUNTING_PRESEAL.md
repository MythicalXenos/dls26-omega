# STEP 1 COVERAGE ACCOUNTING (PRE-SEAL) — dry run, epoch NOT sealed
Session sess-bb22126f679b | Updated 2026-10-11T17:47:59Z | Per OMEGA-EPOCH-001: coverage accounting kept SEPARATE from information extraction. This is the accounting side only. The epoch REMAINS OPEN; this document does not seal it.

## 1. Coverage dimensions vs mission requirements (frontier snapshot t69)
| family | refs | VISITED | IN_PROGRESS | UNVISITED | RETRYABLE | NON_CONNECTED | other | verdict |
|---|---|---|---|---|---|---|---|---|
| official-support | 110 | 70 | 2 | 10 | 9 | 18 | 1 dup | OPEN — full inventory owed (OMEGA-FRONTIER-001, no arbitrary cutoff) |
| official-stores | 3 | 1 | 2 | 0 | 0 | 0 | 0 | OPEN — chunked captures (Play chunk 1/2, App Store chunks 3-5) |
| official-web | 4 | 2 | 0 | 2 | 0 | 0 | 0 | OPEN — firsttouchgames.com + tiktok unvisited |
| databases-tools | 9 | 9 | 0 | 0 | 0 | 0 | 0 | CLOSED-ish for discovery; sakibpro JS-gap + tools pages debt remains |
| community-web-en | 10 | 0 | 10 | 0 | 0 | 0 | 0 | OPEN — ALL 10 mid-capture (player-look/stats comments etc.) |
| community-web-es | 3 | 0 | 3 | 0 | 0 | 0 | 0 | OPEN — mid-capture |
| community-web-vi | 5 | 0 | 1 | 4 | 0 | 0 | 0 | OPEN — 4 guides unvisited |
| community-web-tr | 3 | 0 | 1 | 0 | 0 | 2 | 0 | PARTIAL — 1 mid-capture; 2 scope-excluded (phishing-suspect family discipline) |
| community-web-id | 2 | 2 | 0 | 0 | 0 | 0 | 0 | VISITED (family-note 'no ID source' is STALE — 2 ID refs visited since) |
| community-web-pt | 1 | 1 | 0 | 0 | 0 | 0 | 0 | VISITED (family-note stale as above) |
| community-reddit | 4 | 0 | 3 | 0 | 0 | 0 | 1 ACCESS_BOUNDARY | BLOCKED — 403 bot-wall (ISS-0006); reopen or family-classify |
| community-ugc | 3 | 2 | 1 | 0 | 0 | 0 | 0 | PARTIAL — gh/npm sweep done (EV-215/217); 1 mid-capture |

Totals: 157 refs — 87 VISITED / 23 IN_PROGRESS / 16 UNVISITED / 9 RETRYABLE_FAILURE / 20 NON_CONNECTED / 1 ACCESS_BOUNDARY / 1 REPRESENTATION_DUPLICATE. Service events 130; frontier sequence 322.

## 2. Extraction accounting (separate ledger)
- Evidence: 118 IDs (111 standalone EV files + raw-digest anchors EV-001/002 + EV-104/105/106 + EV-112-in-EV-109) + 7 EVD 404-failure records.
- Claims: 85 — Confirmed 22 / High Confidence 39 / Community Consensus 16 / Speculative 6 / Disputed 2.
- New this outage window (t61-t68): EV-215/216/217 (github/npm/data probes) + CLAIM-084/085/086; drift links (CLAIM-021/050/068); residue + perimeter + templates docs.

## 3. Residual debt carried (33 ledger items; classes)
1. **Support-closure debt**: 10 UNVISITED + 9 RETRYABLE + 2 IN_PROGRESS support refs; moved-article re-discovery (control-buttons, friend-match, cant-update, connection-required, device-compat); stale-ID 404s documented (EVD-0005..0012).
2. **Community-capture debt**: 15 IN_PROGRESS community refs (EN/ES/VI/TR + comment chunks 1-3 of player-look & player-stats).
3. **Store-chunk debt**: Play chunk 1/2; App Store chunks 3-5; version-notes drift.
4. **Access debt**: reddit 403 (ISS-0006 reopen condition recorded); tiktok/official-site unvisited.
5. **Unresolved disputes**: version marker 12200-vs-13.4x; CLAIM-042 iCloud; EV-137 bux-vs-coach release wording; 'recent results' matchmaking divergence (CLAIM-027/081).
6. **Mission residue** (not coverage debt): CLAIM-003/071 tie-breaks/intervals/eligibility/verification; CLAIM-067 XP-ladder surface; CLAIM-006 Legendary Fitness; CLAIM-005/021 critical-drift checks due 2026-10-17.

## 4. SEAL CONDITIONS (all must hold; none hold today)
1. Full official-support inventory complete (every discovered ref VISITED/NON_CONNECTED/REPRESENTATION_DUPLICATE, no RETRYABLE left or explicitly carried) — **CANNOT close while fetch_page is down (outage t61-t69)**.
2. All IN_PROGRESS projections completed or explicitly carried as debt with owner.
3. Reddit family resolved (reachable probe OR documented family-classification closure).
4. residual_debt items each marked resolved/carried-disposition (no dangling).
5. PT/ID family notes reconciled with actual refs (stale-note fix already identified above).

## 5. What sealing unlocks
Step 2 transition gate (docs/step2_3_preparation/CLAIM043_PERIMETER_AND_OBSERVATION_CHECKLIST.md §6): epoch seal OR direct user direction. Until then Step 1 stays WORKING and the cursor keeps priority when fetch tools return.

## 6. Decision recorded (t69)
Between "Medium/Low claim pass" and "coverage-accounting seal prep", chose SEAL PREP: it produces the accounting artifact the epoch will need regardless, while claim passes can run any turn. Medium/Low claim pass remains available as a local fallback.
