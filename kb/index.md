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
