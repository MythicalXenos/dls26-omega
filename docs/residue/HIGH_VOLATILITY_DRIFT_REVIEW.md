# HIGH-VOLATILITY CLAIM DRIFT REVIEW (t66) — vs EV corpus
Session sess-bb22126f679b | Updated 2026-10-11T17:39:57Z | Method: index "covers" graph vs claim supporting_evidence, classified by judgment (NOT bulk-linked — origin-count integrity preserved).

## Verdict classes
- **STABLE** — claim support set matches corpus; no drift.
- **LINK-APPLIED** — genuine supporting evidence existed in corpus but was unlinked; link added this turn (no tier change; same-origin-family or already-counted origins only).
- **CONTEXT-ONLY** — covered EVs are surface-naming/negative/adjacent; recorded in `context_evidence` (NEW field) instead of supporting_evidence (avoids origin inflation).
- **OWED-SOURCE** — drift can only be closed by pending fetches (listed).

## Findings (32 Critical/High claims reviewed)
1. **CLAIM-003 (Critical)**: 14 covered EVs are surface-map/negative context (clans EV-108, inventory EV-109, store EV-111/172, stats EV-115, season-pass EV-116, season-points EV-126, matchmaking EV-135/209, age EV-149, XP ladder EV-195, season-points EV-197, playerdata EV-216, code-search negative EV-217). Classified **CONTEXT-ONLY** → `context_evidence` added. Target-pin still open (staged ask #6). OWED-SOURCE: in-client leaderboard observation + user decision.
2. **CLAIM-006 (High)**: 7 covered EVs; the release→fitness-coach proposition traces to EV-002 (VI snippets, origin, already linked). EV-118 (prize-ladder coaches), EV-136 (develop-players coach mechanics, AGED), EV-114/172/182/196 = context. Classified **CONTEXT-ONLY** (`context_evidence` added). OWED-SOURCE: develop-players comments/re-fetch + VI guides + in-client item catalogue.
3. **CLAIM-005 (Critical)**: covered EV-115/119/120/129 = official troubleshooting/sanctions/design-statement corpus (integrity environment). Context; the claim itself is community-review-reported (store review chunks owed). OWED-SOURCE: gplay review chunks 1+, appstore chunks 3-5.
4. **CLAIM-021 (Critical)**: **LINK-APPLIED** EV-162 (season-pass rev1, Progress Bank/leaderboard basis) into supporting_evidence (official family, already-counted origin class). Tie-breaks/eligibility remain open (CLAIM-071 residue).
5. **CLAIM-050 (High)**: **LINK-APPLIED** EV-195 + EV-197 (official Season Points naming) into supporting_evidence — naming-across-surfaces proposition directly supported. No tier change.
6. **CLAIM-068 (High)**: **LINK-APPLIED** EV-197 (official season-points/prize-tier link) into supporting_evidence. No tier change.
7. **CLAIM-028/032 (High, coaches/release)**: covered EV-142/175/179/202 classified **CONTEXT-ONLY** (release-yield and simulator adjacency; EV-137 bux-wording conflict remains preserved in CLAIM-032 challenges). OWED-SOURCE: can-i-sell comments.
8. **CLAIM-013 (High)**: covered EV-129 (design "not realistic" statement — qualifies determinism) + EV-138/143/145/151 = adjacent. **CONTEXT-ONLY**; comment chunks 1-3 of player-stats article still owed (360019166777).
9. **CLAIM-027 (Medium, checked for drift)**: EV-209 correctly linked; 'recent results' divergence preserved. **STABLE**.
10. Remaining HV claims (001/004/007/009/014/016/017/018/019/020/040/045/046/047/062 + others): gaps classified context/adjacent after spot-check; **STABLE** for tier purposes. Version-marker discrepancy (12200 vs 13.4x) still open across CLAIM-014/032/040.

## Integrity notes
- No tier was changed by this review. Origin-count semantics protected: `context_evidence` is explicitly NOT an origin input.
- Over-linking was rejected deliberately (e.g., EV-216/217 are negative results; counting them as CLAIM-003 support would corrupt the Speculative tier).
- Next drift review due with the 2026-10-17 window (CLAIM-005/021) or after any major fetch epoch.
