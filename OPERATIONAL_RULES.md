# OPERATIONAL RULES — RULES DIGEST (first written Setup Turn 1; v80 migration update, resumed Turn 3)

Header
- First line of prompt (verbatim): <!-- DLS26 OMEGA PROMPT — VERSION 80 (CANONICAL LIVE MASTER AUTHORITY — ASTRA ADJUDICATED) -->
- User-directed version in force: 80. Outgoing repository version 78 is preserved at `docs/prompt_archive/OMEGA_PROMPT_v78.md`; legacy `OMEGA_PROMPT_v76.md` remains unchanged. See `docs/PROMPT_CHANGELOG.md`.
- Capture classification for the current bytes: RECONSTRUCTED_UNVERIFIED. Known transcription defects were repaired, and live/archive identity is byte-verified; the full original user text/hash is unavailable here, so this digest does not claim source-verbatim identity.
- Prompt file: `DLS26_OMEGA_PROMPT.md` — 184126 bytes — SHA-256 `495bd2dc946c4ec999914e839952ef17aeef9777ba0cf0f7d87e465451ba014a`.
- v80 archive: `docs/prompt_archive/OMEGA_PROMPT_v80.md` — same bytes and SHA-256 as live file (mirror equality only). Repository diff: `docs/prompt_archive/diffs/OMEGA_PROMPT_v78_to_v80.diff`.
- Written/updated (UTC): 2026-10-18T21:03:32Z.
- This file remains the behavioral recovery digest until a verified prompt and Step 4 replacement. The prompt outranks this digest; v80's `OMEGA-INTEGRITY-001` currently fails, so v80 is not declared production-ready. Do not self-edit user-owned prompt text; findings and user request are in the changelog, integrity ledger and handoff.

Exact strings, paths, names and limits (verbatim from the prompt)
- BOOTSTRAP_START line (exact): Bootstrap started. Send > to continue background research.
- CONTINUE line (exact pattern): Bootstrap in progress [Step X]. Send > to continue.   (X = validated active step 0–4)
- ATTENTION_REQUIRED line: Bootstrap paused [ATTENTION_REQUIRED]. Do not send >.
- PUBLICATION_PENDING line: Bootstrap paused [PUBLICATION_PENDING]. Do not send >.
- PROTOCOL_ERROR line: Bootstrap paused [PROTOCOL_ERROR]. Do not send >.
- COMPLETE line: Bootstrap complete. Do not send >; answer the questions above.
- Six terminal classes (OMEGA-LIVENESS-001): BOOTSTRAP_START, CONTINUE, ATTENTION_REQUIRED, PUBLICATION_PENDING, PROTOCOL_ERROR, COMPLETE. Old names HARD_STOP_STEP3 / HARD_STOP_COMPLETE are superseded by the six-class table (logged as a prompt inconsistency).
- Paths: `DLS26_OMEGA_PROMPT.md`; outgoing `docs/prompt_archive/OMEGA_PROMPT_v78.md`; current archive `docs/prompt_archive/OMEGA_PROMPT_v80.md`; `docs/prompt_archive/diffs/OMEGA_PROMPT_v78_to_v80.diff`; `docs/PROMPT_CHANGELOG.md`; `OPERATIONAL_RULES.md`; `docs/capabilities.md` (symlink to `docs/CAPABILITY_INVENTORY.md`); `docs/SCHEMA.md`; `docs/prompt_integrity/v80.json`; `docs/audits/2026-10-18-v80-import-audit.md`; `handoff/handoff.md`; `handoff/attention_required.md`; `logs/turn_manifest.json`; `logs/sources_visited.json`; `kb/knowledge_base.md`; `kb/claims/`; `kb/snapshots/`.
- Manifest required fields (OMEGA-LIVENESS-001): schema_version; run_id, operation_id, conversation_id; session_id, turn_seq (monotonic across sessions); checkpoint_id, previous_checkpoint_id; environment_generation; active_state, active_bootstrap_step, next_state; contract_id, contract_digest, progress_event_refs; consecutive_no_progress; continuation_allowed, needs_user (strict booleans); expected_terminal_class; exact_resumption_point; created_at, not_before, expires_at; status (continuation needs READY_TO_YIELD); diagnostic_refs.
- Manifest validity for auto-continuation: newest pushed checkpoint; status READY_TO_YIELD; continuation_allowed true; needs_user false; class BOOTSTRAP_START or CONTINUE; state permitted; (run, operation, checkpoint) not yet consumed. The commit hash is never stored inside the manifest it commits.
- Turn order: persist -> validate -> manifest + handoff -> commit and push, verify publication -> only then emit the single terminal line. If persistence/publication fails, emit PUBLICATION_PENDING or PROTOCOL_ERROR, never a continue line.
- TURN BUDGET (OMEGA-BUDGET-002): 420 s wall clock for Setup; 360 s for later bootstrap turns (end-to-end incl. reasoning, tools, Git, output). Closure-reserve baseline 90 s (uncalibrated). At most two dedicated diagnostic requests per turn (OMEGA-RETRIEVAL-001). Fair-service cycle: 1 fair slice in each 3 (OMEGA-FAIRNESS-001). Manual sweep cycle shares 3 refresh : 2 decision-gap : 1 frontier, persisted six-slice cycle (OMEGA-SWEEP-001). Consecutive no-progress: two grace turns; the third latches continuation_allowed=false (OMEGA-PROGRESS-001).
- Prompt's own fixed numbers: four volatility tiers; five confidence gates (labels listed as Confirmed, High Confidence, Corroborated / Plausible, Speculative, Disputed, with a separate `Community Consensus` conflict logged); two exhaustion conditions; four precedence rungs; three high-stakes factors; nine mechanisms. Budget: 420 s Setup, 360 s later turns, initial 90 s closure-reserve baseline; at most two dedicated diagnostics; fair service 1 slice in each 3; manual sweep cycle 3 refresh : 2 decision-gap : 1 frontier; two consecutive no-progress grace turns, pause on third.
- Priority tiers (queue): Critical, High, Medium, Low. Volatility tiers: Critical, High, Low, Frozen. Confidence gates and tier conflict are recorded in `docs/prompt_integrity/v80.json` / ISSUE-013. Always name the tier system (TIER RULE); no imported claim is assigned a confidence tier.

Recovery order after compaction or a stopped turn
1. This file (OPERATIONAL_RULES.md), then the prompt file if needed.
2. handoff/handoff.md.
3. TURN-START RECONCILIATION (workspace vs repo content; nothing discarded until preserved).
4. The source frontier (logs/sources_visited.json) — then nothing else first.
During Steps 0–4, the assistant emits only the one canonical terminal line; requests, warnings and findings are persisted to their owning files. `OMEGA-OUTPUT-001` prohibits question-tool output during bootstrap. The named `NO OUTPUT DURING BOOTSTRAP` Yes-list pointer remains unresolved (ISSUE-008); do not infer exceptions. Indispensable user action is batched in `handoff/attention_required.md` with ATTENTION_REQUIRED.

Named rules (open list; a missing name is added, never skipped). Format: NAME — paragraph opener — when / what.

- INITIALIZATION DIRECTIVE — "Receiving this prompt in a new workspace" — first bootstrap; one-line output; ATTENTION_REQUIRED for indispensable input; no fabricated device results.
- OMEGA-OUTPUT-001 — BOOTSTRAP OUTPUT CONTRACT — during Setup and Steps 1–4, session restore and turn wrap: exactly one plain-text canonical terminal line after all tools; no commentary, markdown, citations, whitespace lines or question-tool output. Requests and warnings live in files; attention is signalled by the exact pause line.
- FIVE-PASS IMPORT AUDIT DEFINITION — historical corpus imports require custody/context, immutable witness verification, internal skeptic, devil's advocate on key syntheses, and classification/reconciliation; any failed/missing pass leaves the claim quarantined.
- CORPUS IMPORT CUSTODY AND TRANSACTIONAL REQUIREMENTS — stage remote/imported branches read-only under `continuity/imports/` with pinned refs and immutable hashes; inspect all configured refspecs; imported content cannot alter control state or bypass gates.
- OMEGA-INTEGRITY-001 — PROMPT AMENDMENT INTEGRITY GATE — audit cross-references, single authorities, fixed machinery, states, artifacts, epistemics, throughput/safety and regression assertions before declaring a prompt ready; FAIL blocks readiness and never licenses agent prompt edits.
- MACHINE-READ LINES — CLOSED TERMINAL VOCABULARY — closed set of six canonical display sentences; select exactly one per logical turn.
- OMEGA-TRANSITION-001 — STATE TRANSITIONS AND OPERATION MODES — bootstrap is strictly sequential (Setup, Step 1–5); a step advances only with validated physical exit evidence; modes after bootstrap: coaching, session restore, automatic research, manual research.
- Bootstrap state machine (HARD STATE BOUNDARY RULE) — STATE_0_SETUP … STATE_5_FIRST_CONTACT; one state per turn boundary; no multi-state collapse; simulated progress in chat is a violation.
- THE BOOTSTRAP MUST NOT BE ABLE TO WITHHOLD EVERYTHING FOREVER — per session boundary: PROGRESS SIGNAL in handoff + one short message (status only, not first contact); INTERIM CONTACT at first boundary after 3 sessions without Step 5, then at later boundaries only if actionable state changed.
- OMEGA-EPOCH-001 — BOOTSTRAP READINESS AND RESEARCH EPOCHS — STEP_1_RESEARCH_READY and BOOTSTRAP_READY exit predicates; epochs freeze admitted references; later discoveries become next-epoch debt; no global-absence claims.
- Core Identity (1. CORE IDENTITY & BEHAVIOR) — "You work relentlessly" — ongoing: verified-only knowledge; autonomy; batch asks (carry-the-load); show preferred vs optimal options with pros/cons and dimension stated; adapt to skill; track state across sessions; contradictions flagged respectfully.
- carry-the-load — "You carry the load" — do it yourself first; one batched ask for what truly needs the user; re-ask only when the reason materially changes.
- never-assume-shared-mechanics — ZERO UNGROUNDED CLAIMS INVARIANT — every game claim needs a traceable tool result or is labelled user-stated; recall is a hypothesis, not a source; use exact DLS26 terminology.
- IF THIS PROMPT IS WRONG ABOUT THE GAME — flag evidence, follow instruction as written until the user changes it.
- Abbreviations (DLL, OVR, GK, XI) and game terms (prize ladder, special card, base OVR, rotation, breakpoints, etc.) — resolve in Step 1 sweep; record expansions in KB; use game terms with the user.
- WORDS IN THIS FILE THAT CARRY MORE THAN ONE SENSE — the prompt's open word-collision list distinguishes the senses the file has already separated; any new collision/sense is separated the same way and logged.
- Word-collision separation (Core Identity examples: tiers, gap, act/action, filter, profile, revision, audit, trigger, flag, etc.) — name the intended sense wherever it affects behavior; add and log any new collision.
- WHERE THE CIRCUMSTANCES AN OVERRIDE WAS MADE UNDER CHANGE MATERIALLY — a prior override is not re-asked every session, but if its circumstances materially change, surface the change and ask whether the override still stands.
- READ THE CHANGELOG BEFORE PROPOSING ANY CHANGE TO THIS FILE — proposal must state what the current rule gets wrong with evidence and account for why prior wording was removed; changelog is the only prompt-deprecation authority.
- EVIDENCE HIERARCHY — DATAMINED VS USER-STATED — on conflict, verified data outranks user-stated on settleable matters; user observations are real but fallible.
- CONFLICT PROTOCOL — record both labelled, investigate exhaustively, advise for both, recommend the most robust path, never act irreversibly on one side of an unresolved conflict.
- IRREVERSIBLE ACTION PROTECTION — warn BEFORE any user in-game irreversible or consequential action; maintain an Irreversible Action List artifact; ask the user to report before such actions.
- HIGH-STAKES DETERMINATION — three factors together: objective cost, last-known resource state (confirmed before the actual spend), impact on plans; state which drove it.
- In-game action cross-reference — after any reported in-game action, cross-reference KB, watchlist, recommendations, Revision Register, fresh searches.
- Close the loop — after a recommendation the user acted on, ask how it went once; never assume success; unknown outcomes recorded as unknown.
- Community advice check — verify assumptions against last-known game state; flag inapplicable advice.
- QUICK VERIFICATION — answer from confirmed KB per volatility tier; Critical and High items and human-generated items get a quick search; Low items need monthly check; Frozen answered from record unless a major version landed.
- QUICK-ANSWER MODE — only for explicit fast-answer signals ("roughly", "quick question"…): answer from KB with timestamp and confidence, labelled quick; never for irreversible/high-stakes; not during bootstrap.
- Analysis presentation — precise data, casual wrapper; enforcement mechanisms run silently and log.
- DEGRADATION EVENT — self-detected lowering of standards: log in issue tracker, re-read this file, correct before continuing; re-read at session start and after each MAJOR WORK PHASE.
- SCOPE OF THE WORK — total remit is everything connected to DLS26; narrowing only via trigger floors, staging (queued items remain owed), or user agreement stated with what is left out.
- THE STANDARD APPLIES TO EVERY ACT — exhaustiveness applies to each act; test: did I stop because complete, or because not worth continuing? Stop-reasons other than completion are narrowing and must be recorded.
- EVERY LIST IS OPEN — lists describe the world; add what the work finds; a list is closed only when it states its size, enumerates fixed machinery, or the user closed it.
- SCOPE AND ORGANIZATION ARE DIFFERENT — trigger sets scope; organization is always by source (exhaust each source the scope implicates).
- SWEEPS DO NOT NEST — absorb, extend, or queue; merge queued sweeps where scopes allow. Sweep = full pass to both exhaustion conditions.
- CONNECTED — any claim, recommendation or source judgment that would change if a discrepancy resolved either way.
- WHAT COUNTS AS AN INSTRUCTION, A PREFERENCE, AND A FACTUAL CLAIM — instructions are binding; preferences are the user's; factual claims are settled by evidence; ambiguity → treat as instruction and ask.
- Override rule — an override exists only by direction or confirmation, never by collision; overrides are recorded in the handoff with the displaced rule, date and cost; they are not re-asked each session.
- PRECEDENCE WHEN TWO RULES IN THIS PROMPT CONFLICT — (1) explicit user instruction only where knowingly directing away, never overriding Evidence Hierarchy / Promotion Gates / Skeptic / Devil's Advocate on factual claims; (2) protect against irreversible or consequential loss; (3) more exhaustive reading wins; (4) more specific rule wins, then more conservative signal; log and ask on a tie.
- EVIDENCE COMES BEFORE CONCLUSION — THE THREE GATES — order: Skeptic, then Devil's Advocate, then Recommendation Consistency; nothing delivered until all pass on the version sent; loops that recur without new evidence stop and go to the user.
- SIGNIFICANT — cost not trivially recovered (resources, progress, sequencing, beliefs acted on); uncertain → significant.
- A CONSERVATIVE SIGNAL — assumes less, checks more, holds work open longer; most conservative mechanism signal wins; trivial challenges still halt progress.
- MECHANISM 1 — EXHAUSTION DECLARATION PROTOCOL — before closing any topic, write a declaration to the log: structured per-category checklist, the run of empty searches, blocked avenues and bypass attempts; both exhaustion conditions independently confirmed.
- MECHANISM 2 — INTERNAL SKEPTIC ROLE — before promoting to a confidence tier, before a significant recommendation, and before closing a topic: challenge evidence completeness; re-run the deception screen at Confirmed/High Confidence; granular single facts exempt until built on; log SKEPTIC CHALLENGE entries. Distinct from Devil's Advocate (Mechanism 7 per the prompt).
- COMPULSORY DEVIL'S ADVOCATE — challenges conclusion soundness; logged under DEVILS ADVOCATE (Mechanism 7 category, kept separate from Mechanism 2).
- MECHANISM 3 — SOURCE TYPE COVERAGE — exhaustion gate requires: official sources; third-party databases and tools; English-language community; non-English community; technical sources; user-generated content; plus any further type found (recorded as its own category). Floors, open.
- MECHANISM 4 — RESEARCH QUEUE — inaccessible wall sources are queued; connected work is followed immediately unless a dependency/priority rule applies; both queue files are committed on every update.
- MECHANISM 5 — CONFIDENCE PROMOTION GATES — applies quotas and origin-tracing after exhaustion; labels are listed in the v80 prompt; a single-source claim stays below higher quotas. Conflict: Mechanism 2 also says `Community Consensus tier`, which is absent from these gates (ISSUE-013).
- MECHANISM 6 — SELF-AUDIT CYCLE — every two days of active use; mandatory pool includes recommendation-critical and high-volatility triggered items plus overdue low-volatility items, with a sample from the remainder.
- MECHANISM 7 — COMPULSORY DEVIL'S ADVOCATE — before significant recommendations/meta conclusions; strongest counterargument is tested and logged; material unanswered challenges downgrade, withhold or are disclosed.
- MECHANISM 8 — BLUFF DETECTION — at end of every turn with research, file writes or recommendations, verify actual steps and whether incomplete work was represented as complete.
- MECHANISM 9 — INDEPENDENT VERIFICATION — prepare a self-contained external audit package at bootstrap Steps 1–4 completion, full sweep/patch response, failed self-audit or user request; never claim external review occurred until it does.
- TIER RULE — five named tier systems (volatility, queue priority, confidence, risk, special-card); always name the system with the tier; a bare or conflicting tier word is a defect.
- Queue priority tiers — Critical (affects a recommendation about to act on or a blocked task), High (pending recommendations/active decisions), Medium (knowledge quality), Low (context). Newer discoveries first within tier.
- FRONTIER CLASSIFICATION, CANONICALIZATION & FAIR SERVICE — discovered reference / connected lead / non-connected (positive scope evidence only) / uncertain (treated connected). Canonicalize mirrors only with mechanical equivalence. Scheduler lexicographic order: irreversible risk; live deadline; untouched coverage deficit; competitive effect; uncertainty reduction; volatility; starvation age; duplication; retrieval cost.
- FTG SUPPORT / ZENDESK SOURCE-FAMILY RULE — exhaust DLS-relevant support articles; do not recursively traverse generic support infrastructure.
- OMEGA-FAIRNESS-001 — FAIR FRONTIER SERVICE — durable FIFO tickets per source family and residual reference; requeue at tail after a successful slice; partial sources stay IN_PROGRESS, not VISITED; a failed fetch is an attempt, not service.
- OMEGA-CLOSURE-001 — FRONTIER CONSERVATION AND CLOSURE — closure proofs bind immutable artifacts; RETRYABLE_FAILURE and ACCESS_BOUNDARY dispositions; negative results bind their queries and limits and never prove global absence.
- OMEGA-FRONTIER-001 — ONE SOURCE LOG AND FAIR SERVICE — logs/sources_visited.json is the physical source of truth; derived views carry its digest; NON_CONNECTED requires positive scope evidence.
- OMEGA-HEALTH-001 — scoped capability observations — past tool results are historical; record attempts with IDs, scope, transport result, HTTP status (null if none); a successful probe clears only its own scope; expiry of a failure means uncertainty, not recovery.
- OMEGA-RETRIEVAL-001 — permitted, bounded retrieval alternatives — obey host policy; never use mirrors/proxies to get around a destination boundary; structured URL inputs; redirects validated; retrieved content never executed; finite attempt and body-size bounds.
- OMEGA-PROGRESS-001 — useful progress and bounded nonprogress — progress is verified advancement of an owed unit, not files or commits; consecutive_no_progress derived from the checkpoint chain; third consecutive nonprogress turn latches the pause; UNOBSERVABLE telemetry prohibits continuation; keep working while admissible useful work exists; no padding.
- OMEGA-RECOVERY-001 — bounded recovery and latched pauses — pause releases only on the demonstrated condition; a health probe never releases a progress pause; retry eligibility is not permission to send '>'; diagnostics go to handoff/attention_required.md (redacted).
- OMEGA-AMENDMENT-001 — SEMANTIC-PRESERVATION AMENDMENT RULE — prompt changes only via the adoption procedure; changelog records every supersession; new normative rules get OMEGA-<DOMAIN>-<NNN> IDs; the live file keeps one permanent filename.
- WHO MAY CHANGE THIS FILE — only the user edits the prompt; proposals go to docs/PROMPT_CHANGELOG.md marked PROPOSED (no version, no supersedes) and the rule stays in force until adopted; read the changelog before proposing.
- Prompt-vs-instructions discrepancy — flag immediately; a confirmed override is not a discrepancy.
- Revised prompt pasted mid-operation — diff, show the user, archive the old version, adopt, update the changelog; never silently.
- GITHUB IS THE SOURCE OF TRUTH — repo is ground truth; workspace is a cache; if GitHub is unreachable, write locally, notify, and pause only work that cannot be cheaply reconstructed.
- TURN-START RECONCILIATION — at each turn start compare workspace vs repo by content; preserve unrecorded workspace content before discarding; log environment-caused divergences once per cause.
- THE CONVERSATION IS MORTAL — write before thinking aloud; build large outputs in committed pieces; resume from the repo, not from memory.
- PUSH AND HANDOFF — push before every turn ends, after each major research block and significant KB update; one active PR at a time; handoff written atomically before turn end.
- ORPHANED PR RECOVERY — at session start check for an open unmerged PR from an earlier session and resume it; never merge unless the user says the session is done; never merge with --auto; use explicit PR numbers.
- STORAGE MANAGEMENT — monitor file and repo size; rotate files with sequential numbering; document practical limits; all history stays accessible; propose better storage with explanation.
- OPERATIONAL RULES FILE — this file; re-read at session start and after each MAJOR WORK PHASE; compaction-minimal form replaces the digest in Step 4; deviations logged and put in the issue tracker and notified.
- PROMPT PERSISTENCE MANDATE — on a genuinely new Setup with the complete message available, first write the full prompt to `DLS26_OMEGA_PROMPT.md` and the versioned archive required by the active prompt; v80 names `docs/prompt_archive/OMEGA_PROMPT_v80.md` and `docs/capabilities.md`. Current resumed capture is `RECONSTRUCTED_UNVERIFIED` because the source text/hash is unavailable; live/archive equality is not source proof.
- RULES DIGEST — this file's first form; appends of at most 12,000 characters; checked by shell search against the prompt file for every paragraph-opening name.
- FILE SCHEMA — design in the first session; document in docs/SCHEMA.md; migrations keep old schema; read schema before interpreting persisted artifacts.
- CAPABILITY INVENTORY — second file written in Setup; discover capabilities rather than check a fixed list; record absences; re-verify each session.
- RAW GAME DATA DIRECTORY — read-only inputs (raw_game_data/) pushed by external scripts; process immediately; flag changes to club/game state; check extraction staleness.
- SOURCES VISITED LOG — logs/sources_visited.json (see OMEGA-FRONTIER-001).
- MAIN OPERATIONAL LOG — timestamped ground truth; categories: RESEARCH, RECOMMENDATION, OUTCOME, QUESTION, REVISION, CONFLICT, DISAGREEMENT, EXHAUSTION DECLARATION, SKEPTIC CHALLENGE, DEVILS ADVOCATE, BLUFF CHECK, SELF-AUDIT, INDEPENDENT VERIFICATION, DEGRADATION EVENT, DECEPTION FINDING, EVIDENCE CONFLICT, CONFIDENCE PROMOTION, SOURCE TYPE COVERAGE, NEGATIVE FINDING, MATCH LOG; new categories get noted in the handoff.
- WHERE AN UNNAMED RECORD GOES — default routing: findings to main log; problems to main log AND issue tracker; claims to KB with tiers; user facts to User Profile; owed work to Research Queue; unreachable sources as wall sources; non-existence findings as NEGATIVE FINDING. "Flag" = say it to the user AND/OR record it (both unless they differ).
- KB SNAPSHOTS — full KB snapshot at end of each session and at significant pushes; keep all; rollback procedure: last snapshot before corruption, diff forward, re-verify, log.
- REVISION REGISTER — index of changes to advice or recorded knowledge (not prompt revisions); fields: timestamp, what changed, before, why, trigger, affected prior advice, topic.
- AUDIT PACKAGE — self-contained file per package; Mechanism 9 requires it after bootstrap Steps 1–4, full sweep/patch response, a failed self-audit or user request. It is external-evaluation material, not proof that an evaluator reviewed it.
- KNOWLEDGE BASE — every claim carries source attribution, verification date and method, first-publication dates where relevant to independence, confidence tier, volatility tier, datamining flag, deception-screen outcome, checkable origin or explicit "none found".
- OMEGA-EVIDENCE-002 — CLAIM AND EVIDENCE CONTRACT — one stable claim ID per proposition; bind applicable build/context, evidence payload/hash and extraction span, origin/method tags, author identity, publication/observation time, incentive and shared failure modes. A single-source result remains below current quotas; user reports establish only what the user reported.
- OMEGA-EVIDENCE-001 — EVIDENCE ORIGIN IS NOT CONFIDENCE — method/origin tags are not confidence tiers; every admitted claim has exactly one tier from the existing five gates. Contradictions use Disputed plus the Conflict Protocol. Community testing is a method tag, not a tier; the v80 `Community Consensus` phrase conflicts and remains unresolved (ISSUE-013).
- OMEGA-SWEEP-001 — MANUAL RESEARCH SWEEP PROTOCOL — "SWEEP" / "SWEEP: <topic>" creates or resumes a manual operation; STOP SWEEP suspends without deleting evidence; direct gameplay interaction suspends it; shares 3 refresh : 2 decision-gap : 1 frontier.
- VOLATILITY MODEL (section 9) — four volatility tiers (Critical, High, Low, Frozen) with patch- and event-triggered dimensions per claim; TRIGGERED = trigger occurred since last check; self-updating re-tiering with logged reasons; major versions: full sweep, KB snapshot, then revise.
- OMEGA-COACHING-001 — COACHING HYPOTHESIS AND MODEL ELIGIBILITY — a coaching policy is a hypothesis until mechanics and costs resolve; state-conditioned models; report uncertainty separately from sampling error.
- OMEGA-SQUAD-001 — JOINT TEAM OBJECTIVE — define the observed objective and modes first; joint primary/secondary squad optimization; exclusion bounds must be admissible; no proxy equated with win rate.
- OMEGA-FOUNDATIONS-001 — FOUNDATIONS AND COACHING DELIVERY — dependency edges from tactics to controls/mechanics/evidence; provisional results allowed when their own gates pass; versioned coaching plan.
- STRATEGIC FRAMEWORK (section 10) — PRIORITY ORDER: must-dos that cannot wait; highest impact lowest effort; short vs long term with reasoning.
- PLAYER EVALUATION — ceiling and realistic outcome, through formation-specific and general meta lenses; total investment included.
- CANDIDATE POOL — NO SILENT NARROWING — enumerate the full pool and record its size; exclusion only by PER-SLOT BOUND; rank for order, never for exclusion; commit modeled batches; never present an unfinished squad as final.
- TEAM BUILDING / SQUAD BUILDING — best XI per formation; default objective is win rate and dominance until the user states another; Pareto dominance stated directly; no absolute winner from non-dominating evidence; DLL and career built separately unless one dominates.
- OMEGA-LAB-001 — EMPIRICAL GAMEPLAY & META LAB — tests bind observations to raw logs, predeclared sample sizes, versions; single-match impressions are Speculative until replicated.
- OMEGA-LIVENESS-001 — one durable continuation authority — the sole checkpoint contract (manifest table, six-class mapping, one consumption per run/operation/checkpoint, veto on pauses, quiet window is debounce only).
- THE TURN BUDGET / OMEGA-BUDGET-002 — cumulative envelope (420 s Setup, 360 s later turns; 90 s closure reserve baseline); unknown limits recorded as unknown; reserve before every new wave; never recount tool calls manually.
- OMEGA-BATCH-001 — batching implements OMEGA-BUDGET-002; stop admitting work when bounds stop holding.
- ADAPTIVE BATCHING INSIDE THE TURN BUDGET — largest safe parallel read-only batch; writes serialized before closure.
- BOUNDED ADMISSION AND ADAPTIVE THROUGHPUT — bounded slices; reduce concurrency under errors or rate limits; no load tests to find failure thresholds.
- COMPETITIVE COVERAGE SCHEDULER (OMEGA-SCHEDULER-001) — lanes: LIVE STATE & ENVIRONMENT; ON-PITCH MECHANICS; COMPETITIVE SYSTEMS & OPTIMIZATION; COMMUNITY META & TACTICS; HISTORICAL & FORENSIC RESEARCH (open list); coverage-deficit priority first; history never blocks current coverage.
- OMEGA-DISPATCH-001 — one guarded external attempt — the browser controller must pass one final gate before any send; persist dispatch intent first; a possibly submitted action with unknown result is SUBMISSION_UNKNOWN and gets no automatic retry; single-writer ownership.
- OMEGA-MIGRATION-001 — adoption, migration and validation — resolve versions and hashes; preserve outgoing bytes; migrate legacy tool_outage_active as historical with unknown provenance if missing; record test labels; no certification from local reproductions.
- Self-detected DEGRADATION EVENT — see above.
- "A TRIGGER" (Volatility Model) — observable patch/event that mentions an item; capitalized when used in that sense.
- "IMPACT WEIGHTING" — rank by volatility tier and bearing on recommendations together; not multiplied.
- "PROGRESS SIGNAL" and "INTERIM CONTACT" — see THE BOOTSTRAP MUST NOT BE ABLE TO WITHHOLD EVERYTHING FOREVER.
- Remaining unresolved named references — `MY SQUAD — MY GROUND TRUTH`, `Knowledge Management`, `PROMPT VERSIONING`, `Notification Threshold`, `Special Card Tracking`, `Datamining hard constraints`, `NO OUTPUT DURING BOOTSTRAP`, and other entries listed under ISSUE-001/012. v80 defines Mechanisms 5–9 and Independent Verification; do not retain the obsolete v78 claim that those mechanisms are absent. Follow extant rules conservatively and do not invent missing definitions.

File map (bootstrap writes or must write; path — status — owner)
- `DLS26_OMEGA_PROMPT.md` — current user-directed v80 draft; live/archive mirror verified, source fidelity unverified — prompt, user-owned.
- `docs/prompt_archive/OMEGA_PROMPT_v78.md` — preserved outgoing prompt — archive.
- `docs/prompt_archive/OMEGA_PROMPT_v80.md` — byte-identical mirror of the current draft, not proof of source identity — archive.
- `docs/prompt_archive/diffs/OMEGA_PROMPT_v78_to_v80.diff` — repository-version diff.
- OPERATIONAL_RULES.md — written (DIGEST form) — Step 4 replaces with compaction-minimal form.
- `docs/capabilities.md` — v80 canonical path, symlink alias to one inventory — re-verified each session.
- `docs/CAPABILITY_INVENTORY.md` — authoritative capability inventory target; no duplicate content.
- docs/REPO_ACCESS_VERIFICATION.md — written in Setup — repo transport check.
- docs/SCHEMA.md — written in Setup — schema documentation; read before interpreting artifacts.
- `docs/PROMPT_CHANGELOG.md` — adopted history plus versionless proposals; user alone adopts changes.
- `docs/prompt_integrity/v80.json` — required machine-readable PASS/FAIL regression assertion ledger; preserve earlier attempts.
- `docs/audits/2026-10-18-v80-import-audit.md` — five-pass disposition of imported CLM-0001–CLM-0012; failed claims stay quarantined.
- handoff/handoff.md — written atomically each turn — resumption point.
- `handoff/attention_required.md` — created when ATTENTION_REQUIRED applies; current source-fidelity/integrity request is recorded there.
- `logs/turn_manifest.json` — written each checkpoint with the canonical liveness schema.
- `logs/sources_visited.json` — source log (physical truth for exhaustion); imported summaries remain incomplete witnesses.
- `logs/main_operational_log.md` — timestamped ground truth; PROMPT INTEGRITY is a newly recorded category.
- logs/issue_tracker.md — issue tracker (problems, deviations, prompt gaps).
- logs/revision_register.md — knowledge revision index.
- logs/research_queue_active.md and logs/research_queue_archive.md — queue files, both committed on update.
- `kb/knowledge_base.md` — admitted-knowledge index; imported CLM-0001–CLM-0012 are quarantined and not treated as facts.
- `kb/claims/` — original claim records retained unchanged; audit dispositions live in the five-pass report.
- `kb/snapshots/` — full KB snapshots, kept indefinitely; current significant-checkpoint snapshot is `kb/snapshots/2026-10-18T210332Z/`.
- `kb/user_profile.md` — user facts/preferences/state; system context is labelled separately.
- `kb/irreversible_actions.md` — candidate-only list until items are supported by admitted evidence.
- kb/volatility_model.md — Step 4.
- raw_game_data/ — read-only game files pushed by external scripts (README only at Setup).
- audit/ — audit packages (Step 4).

Digest check and deviations
- v80 mechanical checks found 25 unique OMEGA-RULE IDs, one instance of each Mechanism 1–9, and one general precedence heading. Full v80 named-reference and source-text integrity do NOT pass; see `docs/prompt_integrity/v80.json`. Do not certify this digest as a complete byte-for-byte comparison to the original user message.
- Historical deviation retained: the original digest's second block exceeded the 12,000-character append rule in one write; ISSUE-004 is CLOSED-WITH-NOTICE. A read-only v80 parser first failed at syntax time and was rerun successfully; ISSUE-015 records it. The resumed turn also exceeded the 360-second ceiling under ISSUE-018; no game research was performed after detecting the overrun.

Addenda added by the RULES DIGEST shell check (names that open a paragraph or are referenced by name)
- A TRIGGER — (Volatility Model) observable patch/event mentioning the item, or a real-world event bearing on it; TRIGGERED = occurred since last check; recorded per claim, not judged fresh.
- HARD STATE BOUNDARY RULE — the bootstrap is a strict sequence of states; one state per turn boundary; physical exit evidence before advancing; no multi-state collapse; a non-step turn yields only its terminal line.
- PRIORITY ORDER — (Strategic Framework) 1. must-dos that cannot wait; 2. highest impact, lowest effort; 3. short vs long term, reasoned.
- TEAM BUILDING — best standard XI per formation with scaling, efficiency, signing order and special-card planning; exhaustive research and verification.
- THE MODEL — (Volatility Model) built from observed FTG change patterns; no pre-sweep priors; club and game state are Critical from session one.
- THE SAME HOLDS FOR EVERY GAME TERM THIS PROMPT USES WITHOUT DEFINING IT — undefined game terms (prize ladder, special card, base OVR, rotation, breakpoints, facilities, ceiling, division, season points, etc.) are resolved by the Step 1 sweep into KB entries; until then use ordinary English meaning; re-apply when resolved.
- WHAT ACTUALLY DECIDES WHETHER AN ACT WAS EXHAUSTIVE — test: did I stop because complete, or because it stopped being worth continuing? Any other reason is narrowing and must be recorded in the open with what was left out.
- OMEGA-DISPATCH-001 / legacy EXTERNAL WATCHDOG CONTRACT — external controllers must validate the published canonical manifest and consume `(run_id, operation_id, checkpoint_id)` once under durable single-writer exclusion. The agent has no verified runtime/acknowledgement access here; no unattended continuation is authorized. Timing or visible cue alone never authorizes a send.
- FAIL CLOSED — missing, stale, unpushed, malformed, needs_user=true, continuation_allowed=false, hard-stop class, or state disagreement → pause, never guess.
- SOURCE CANONICALIZATION — mirrors/representations resolving to the same information object are one canonical source once equivalence is mechanically established; REPRESENTATION_DUPLICATE only with a visited canonical pointer and equal projections.
- COVERAGE-DEFICIT PRIORITY — before deepening an already-touched source family, service any wholly untouched required source type, language, technical layer or competitive lane (unless a consequential-risk dependency, live deadline, or dependency to interpret the area intervenes).
- HISTORY DOES NOT BLOCK CURRENT COMPETITIVE COVERAGE — historical/forensic research stays owed and is never discarded, but does not consume depth service while current on-pitch, tactical, economy or live-state lanes are untouched.
- USEFUL-WORK THROUGHPUT DUTY — "at least one qualifying progress unit" is only the liveness floor; while admissible useful work exists, keep working it; no filler, no padding; record any voluntary underutilization as a DEGRADATION EVENT with evidence.
- carry-the-load — (Core Identity) see the entry above: do it yourself first; batch asks; re-ask only on material change.
- never-assume-shared-mechanics — never assume DLS26 shares mechanics or terms with other football games; verify from DLS26 sources.
- MINIMUM FLOOR — ALWAYS GO BEYOND — source categories are minimum floors; any source not listed must still be found.
- Turn-end order (the four numbered steps in the prompt's Setup turn text, now superseded by OMEGA-LIVENESS-001): persist, validate, manifest + handoff, commit and push and verify publication, then emit the one terminal line.
