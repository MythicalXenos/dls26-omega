# KNOWLEDGE BASE — DLS26 OMEGA
The KB is the authority on the current state of every claim. Empty at bootstrap; first entries written turns 2–3 (2026-10-17). Every claim carries: confidence tier, volatility tier, evidence origin, source URLs, verification date (OMEGA-EVIDENCE-002). Claim IDs are stable (prefix per file).

## Topic files
- terminology.md — resolved shorthands and official terms (T-001…T-028): DLL=Dream League Live (Confirmed), OVR=Overall, GK=goalkeeper, XI=starting eleven, Special Players, modes, systems (Season Points, Dream Points, in-game week, Form Boost, coaches, Cult Hero Agents, Progress Bank, My Club, clean sheet, stadium bonus, scripts, reserves/eight subs), collections; unresolved prompt terms listed.
- build-version.md — build/version state (B-001…B-008): current build 13.430 code 160 (Sep 16 2026), package com.firsttouchgames.dls7, NO rebrand, launch Dec 2025, full 2026 version timeline (13.020→13.430 with two enumerated gaps), Summer Spotlight attribution conflict resolution, store metrics, technical envelope.
- live-state.md — time-limited events and live-service state (L-001…L-007): Dynamic Stars (Jun 8–Jul 20 2026, 82→96 OVR, Dynamic Agents), World Cup Winners event, Cult Heroes LIVE (12 players), Play Fest NEGATIVE FINDING, update cadence.
- community-meta.md — community state and early meta (M-001…M-007): launch-era gameplay sentiment, formation discourse (no verified meta yet), DLL structure (leaderboard cadence corrected per R-001), economy friction, dated ratings snapshots, new-player start state.
- game-systems.md — official system semantics (GS-001…GS-023): player stats, difficulty/DLL no-manipulation guarantee, economy, Season Pass, Prize Ladder, recruitment, Clans, coaching/Form Boost, Cult Heroes, update-channel policy, position labels, coin economy, Leaderboards, Friend Match, save/accounts, Reset Profile, connection requirement, compatibility, app updates, customisation, account legacy, squad depth, facilities.
- source-families.md — FTG support canonical inventory (S-001, 30 articles with IDs, 25 fetched in full), incentive-screen registry (S-002), NON_CONNECTED sources (S-003), source-type coverage matrix (S-004).

## Claim-entry requirements (per OMEGA-EVIDENCE-002)
Statement; confidence tier (Confirmed / High Confidence / Community Consensus / Speculative / Disputed); volatility tier (Critical / High / Low / Frozen); evidence origin (official-stated / database-derived / community-reported / user-stated / tool-derived / community-anecdote); source URLs; verification date; notes (conflicts, independence assessments, single-source flags). Unconfirmed or contradicted claims stay quarantined as hypotheses and are never delivered as advice.

## Standing obligations (Step-1 first obligations, in force until done)
Resolve every remaining unnamed prompt term to DLS26 exact terminology; keep build/version and rebrand status current; maintain the six-source-type and six-lane coverage matrix; log every fetch to logs/sources_visited.json and every claim to kb/ with tiers and origin.

## Continuity merge — 2026-10-17T16:53Z (session sess-20261017-001)
- Live claim authority is now **kb/claims.jsonl** — 87 claims (CLAIM-001…088, no 087 duplicate gap) imported verbatim from branch arena/a7e23a6b-dls26-omega (v77 research run, checkpoint 5ab3ec6, 2026-10-10…15). Schema: claim_id, proposition, confidence_tier, volatility_tier, context_build, supporting_evidence, contradicting_evidence, challenges, origin_history, replacements, last_valid_check, last_attempt, last_checked_by, next_due.
- The markdown topic files above (T-/B-/L-/M-/GS- IDs) are retained as **topic summaries and derived views** from branch 22655f48. They are not a second claim authority; where a summary and claims.jsonl disagree, claims.jsonl wins and the summary is corrected in the next reconciliation pass (queue item RQ-20261017-003).
- Epoch coverage accounting imported to step1_epochs/coverage_accounting/ (pre-seal dry run, t69, 157 refs, epoch OPEN — no seal claimed).
- Imported evidence corpus (118 evidence extracts) and tools/schemas preserved at docs/continuity/a7e23a6b/ and schema/imported_a7e23a6b/.

## Index state — turn 15 (2026-10-17T17:28Z)
- Claim authority: **118 claims** (CLAIM-001…CLAIM-119; CLAIM-036 is a documented gap, OBS-014a). Tier spread: Confirmed 31 / High Confidence 51 / Community Consensus 23 / Speculative 12 / Disputed 1. Snapshot: `kb_snapshots/claims_20261017T1728Z.jsonl` (sha256 `f8dea58f…`).
- Evidence registry: **127 records** in `docs/continuity/a7e23a6b/evidence/index.jsonl` (124 inherited + EV-223/224/225 written turn 14), plus 7 unregistered `EVD-*` failure records that exist only as files.
- Frontier: **161 refs**, re-stamped turn 14 — 96 VISITED / 23 IN_PROGRESS / 21 NON_CONNECTED / 8 UNVISITED / 3 RETRYABLE / 2 ACCESS_BOUNDARY / 8 DUPLICATE. Reproduce with `cd docs/continuity/a7e23a6b && python3 tools/frontier.py summary`.
- Conflicts: **9 open** (C-001…C-009), 3 resolved (C-R01…C-R03). The most consequential open question is **C-009** — whether the Season Leaderboard is a public ranking at all, which decides whether "#1" can be measured on it.
- Witness coverage: **54 of 118 claims** (46%) have had a textual comparison against their cited records across six samples; the rest are structurally verified only. Each sample so far has found at least one defect, so the remainder should not be assumed clean.
- Topic-file note: the T-/B-/L-/M-/GS- summaries remain derived views and still describe the pre-merge claim set. They are now **older than the claim authority by 31 claims** (CLAIM-089…119 have no summary entry). This is a known, recorded lag, not an error to be fixed by inventing summaries.

## Index state — turn 21 / post-Step-1 prep (2026-10-17T23:00Z)
- Claim authority: **129 claims** (CLAIM-001…CLAIM-130). Confirmed 34 / High 59 / Community 23 / Speculative 12 / Disputed 1. Closure snapshot `kb_snapshots/claims_20261017T1801Z.jsonl`.
- Evidence registry: **148 EV/EVD records**. Every claim carries a witness; 6 accounting-only EVs classified.
- Frontier: 163 refs / 106 VISITED / 20 ACCESS_BOUNDARY / 8 UNVISITED / 21 NON_CONNECTED / 8 DUPLICATE / **0 IN_PROGRESS / 0 RETRYABLE** (file sha `d014f307…`).
- Step 1 **sealed** turn 20. Turn 21 deliverables:
  - `step5_first_contact/FIRST_CONTACT_SCRIPT_draft.md` (S1/S2 safety → P0 mission-definition → P1–P3 tiered).
  - `step3_device_pipeline/PROTOCOL_draft.md` (consent gating, `raw_game_data/` layout, ingestion procedure, prohibited actions).
  - `step2_datamining/STEP2_PLAN_DRAFT.md` updated against actual sandbox tooling probe (all APK tooling MISSING; python stdlib sqlite3 and `pip install androguard` available; install plan deferred to consent gate).
  - `raw_game_data/` scaffold + `.gitignore` for consent records.
- Sample 11: 7/7 OK post-repair; five consecutive clean samples; ~2.6% cumulative substantive error rate.
