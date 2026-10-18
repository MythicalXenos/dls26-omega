# Issue Tracker

Each entry: ID, opened (UTC), status, severity, description, action, owner.

## ISSUE-001 — prompt references undefined sections — opened 2026-10-18T15:32:51Z — OPEN — severity High
- The pasted prompt refers to sections and mechanisms it never defines. Grep check during Setup: Session Start, Session Handoff, First Session Bootstrap, Knowledge Management, Analysis & Reasoning Standards, Patch Response, Notification Threshold, Communication Style, Confidence Promotion Gates, Scope Division, Mechanisms 5–9 (Mechanism 7 = DEVILS ADVOCATE and Mechanism 9 = Independent Verification are referenced by name only), Special Card Tracking, Planted And Decoy Data, Deterministic Versus Variable, Gaps, Named Set, Irreversible Action List, NO OUTPUT DURING BOOTSTRAP (Yes list), PROMPT VERSIONING, PROMPT CAPTURE, MY SQUAD — MY GROUND TRUTH, Mid-Session Monitoring, Independent Verification, Recommendation Consistency, Intelligence Pipeline, Datamining hard constraints, Origin-tracing in the Promotion Gates, WORKFLOW under SQUAD BUILDING.
- Action: follow the conservative default named in each referring rule; record blockers here; one consolidated ask at end of bootstrap. Proposed fix: PROPOSED-A in docs/PROMPT_CHANGELOG.md.
- Owner: user (text), agent (tracking).

## ISSUE-002 — prompt version label vs archive filename — opened 2026-10-18T15:32:51Z — OPEN — severity Low
- Header says VERSION 78. Bootstrap text mandates docs/prompt_archive/OMEGA_PROMPT_v76.md. Kept the mandated filename; version identity recorded as 78 in the digest and changelog.
- Action: user confirms which label to keep; no change until then.

## ISSUE-003 — two manifest vocabularies — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- See CONFLICT entry in the main log and PROPOSED-B. Followed OMEGA-LIVENESS-001.

## ISSUE-004 — digest append-size deviation — opened 2026-10-18T15:32:51Z — CLOSED-WITH-NOTICE — severity Low
- Second digest block exceeded the 12,000-character append rule in a single write. Recorded as DEGRADATION EVENT. Future digest edits use appends of at most 12,000 characters.

## ISSUE-005 — conversation identity not exposed to the agent — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- OMEGA-LIVENESS-001 requires conversation_id bound to the configured controller. The agent cannot see the controller's conversation identifier, so logs/turn_manifest.json records conversation_id = "host-unexposed". The controller must bind its own identity and validate the manifest (OMEGA-DISPATCH-001). The manifest's continuation permission is therefore a checkpoint claim, not an identity check.
- Action: the controller owner must confirm the binding before unattended continuation. Nothing automatic is enabled by this manifest alone.

## ISSUE-006 — device and APK tooling absent — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- No adb, no Java, no apktool or jadx, no Android device or emulator, and no KVM (docs/CAPABILITY_INVENTORY.md). STATE_2 static analysis and STATE_3 device work are blocked by the environment. When they are reached, an ATTENTION_REQUIRED pause with the needed device or tool details goes in handoff/attention_required.md. No fabricated results.

## ISSUE-007 — Irreversible Action List not defined in pasted text — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- kb/irreversible_actions.md created empty. Step 1 must populate it from research. The first-contact list is owed to the user at Step 5.

## ISSUE-008 — NO OUTPUT DURING BOOTSTRAP Yes list absent — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- Without the Yes list, no question is asked during Steps 0–4. Default applied: questions go to the consolidated ask at the end of the bootstrap.

## ISSUE-009 — confidence tiers not defined in pasted text — opened 2026-10-18T15:32:51Z — OPEN — severity High
- The text names Confirmed, High Confidence, Community Consensus, Speculative and Disputed, and says "five tiers". Their order, names and promotion quotas (Confidence Promotion Gates) are not present. Until defined, no claim is promoted above Speculative; every claim is recorded with tier "unassigned-pending-gates" and the reason in the claim record.

## ISSUE-010 — tier words named by system — opened 2026-10-18T15:32:51Z — CLOSED — severity Low
- TIER RULE applied from the start: every tier is written with its system name in all files (volatility, queue priority, confidence, risk, special-card).

## ISSUE-011 — source conflicts from turn 2 — opened 2026-10-18T15:41:35Z — OPEN — severity Medium
- CONF-001 (launch date): Wikipedia lead says 1 Dec 2025; a news article dated Feb 2026 says global availability 4 Dec 2026. The live store listings show a September 2026 update. Status: Disputed (CLM-0012). Owed: fetch the Wikipedia page (language version to be recorded) and the news article, then the official launch announcement if one exists.
- CONF-002 (Summer Spotlight): App Store snippet attributes Summer Spotlight to 13.120 (Mar 25); third-party sites place it in May and July 2026. Status: Disputed (CLM-0011). Owed: App Store version-history chunks 1-4.
- Not a conflict: Google Play 'Updated Sep 14, 2026' vs App Store 13.430 'Sep 16' (platform dates may differ).
- Action: no claim is promoted until resolved against a fetched official page.
