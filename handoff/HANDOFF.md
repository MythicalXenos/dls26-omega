# HANDOFF — DLS26 OMEGA
Updated: 2026-10-17T22:25Z (session sess-20261017-001, turn 19, checkpoint ckpt-20261017-step1-018)
Branch: arena/b5d5681d-dls26-omega (from main fb9a2c0). One branch only; push here.

## Active state
- Active: STATE_1_RESEARCH_SWEEP (step 1). Setup exit validated and consumed at this turn boundary.
- Next state (next turn boundary): STATE_1_RESEARCH_SWEEP.
- Continuation: allowed; user not required; expected line this turn: `Bootstrap in progress [Step 1]. Send > to continue.`
- No user ask owed. Nothing irreversible has been done or recommended.

## Turn 10 result — integrity check, contract refresh, first-contact basis, degradation audit
- **Claim authority integrity: PASS.** 117/117 lines parse; IDs unique/ordered (OBS-014a: CLAIM-036 gap, unreferenced); 264 supporting and 22 context EV tokens all resolve; every claim has a tier and a valid `next_due`; no empty evidence basis; `claims_index.md` is 1:1. Report: `audit/CLAIM_INTEGRITY_step1_turn10.md`.
- **Contract refreshed:** `EPOCH_CONTRACT_DRAFT.md` §5 now records the turn-9 closures (numeric pass, NEG register, Mechanism-3 walk) and the new residual debts; still DRAFT, still unsealed.
- **First-contact basis written:** `step1_epochs/FIRST_CONTACT_BASIS.md` — four briefing tiers, the "#1 is undefined" opening, six batched user-only asks, delivery gate at Step 5. Not delivered.
- **Degradation self-audit:** `audit/DEGRADATION_SELF_AUDIT_turn10.md` — 8 events; dominant finding is that the entire knowledge base is second-hand and cross-corpus agreement is not independence.
- Schema conventions recorded (`SCHEMA.md` §4b); OBS-014 logged.

## Progress signal (prompt: "THE BOOTSTRAP MUST NOT BE ABLE TO WITHHOLD EVERYTHING FOREVER")
- **Step:** 1 of 5 — Exhaustive Research. Part: closing the evidence-integrity and readiness work while the web families are unreachable.
- **Established so far:** 117 claims over 8 divisions of the game (mechanics, economy, account safety, live-service, build history), all traceable to a preserved record; 123 EV artifacts + 7 failure records; a negative-finding register; a conflict ledger with 7 open items; the "#1" target still undefined because no verified global ranking surface exists.
- **What remains:** witness-testing 97 of 117 claims; 8 owed/23 in-progress source refs; 3 uncaptured support articles; 5 original conflicts; the sealed epoch contract; and Steps 2–5, none of which is entered.
- **Untouched:** English-language community pages (snippet-only), live in-client observation, all datamining, and any current-season state of the user's own account.
- **Shape of the remaining frontier:** small and contract-shaped offline; large and blocked online. Nothing left in Step 1 can be finished without either a retrieval channel or the user's ruling on Step 2.
- **Session estimate:** unmeasured projection — 2–4 more offline turns to finish the auditable parts of Step 1; zero estimate for the network-dependent remainder.

## Turn 2 result — environment boundary + continuity correction
- Actual reachability attempts (not inherited assumptions): support.ftgames.com, firsttouchgames.zendesk.com, dlsinside.com and a control host all fail at TLS (curl 35, null HTTP status). api.github.com, registry.npmjs.org, pypi.org return 200. This environment generation is allowlist-limited: web research families are ACCESS_BOUNDARY, not "site down".
- GitHub technical sweep (4 repo searches, 5 inspections, 1 code search) and npm search: no DLS26 APK, save-format, stat-table or decompilation corpus. NEGATIVE FINDING, bounded to queries/date; logged S-059..062, RQ-002.
- Major continuity correction: branch arena/a7e23a6b-dls26-omega (v77) holds a far more advanced corpus than 22655f48 — 87 claims, 118 evidence extracts, 157-ref coverage accounting (t69 pre-seal), schemas and preparation docs. Imported losslessly: kb/claims.jsonl is now the live claim authority; step1_epochs/coverage_accounting live; full corpus at docs/continuity/a7e23a6b/. Markdown topic files remain derived summaries. OBS-011 logged; reconciliation queued RQ-003.
- Episode status honesty: the imported epoch remains OPEN and unsealed; no closure is claimed.

## Setup exit evidence (all written and verified on disk)
1. Prompt persistence MECHANICAL: DLS26_OMEGA_PROMPT.md, 175,596 bytes, SHA-256 b7fd30da008740723e62241002a447adf2ccda57fc23a68da4bb1f6b8db6dd7b; archived at docs/prompt_archive/OMEGA_PROMPT_v76.md and OMEGA_PROMPT_v78_2026-10-17.md.
2. Rules digest: OPERATIONAL_RULES.md (header, exact strings/paths/limits/orderings, 48+ named-rule entries, recovery order, file map; name-check run, 3 misses added; mechanically rewritten in 6 ≤11,900-char chunks).
3. Capability inventory: CAPABILITY_INVENTORY.md (observed presences/absences, allowlist, repo verification, no device/ADB/java).
4. Repository access: gh authenticated; git ls-remote OK; branch pushed with this checkpoint.
5. Schema documentation: SCHEMA.md (artifact ownership, manifest/sources/KB schemas, migration + rollback).
6. Liveness manifest: logs/turn_manifest.json (this checkpoint, READY_TO_YIELD).
7. Initial artifacts: sources log (50 inherited + 4 new entries), main log, revision register, issue tracker, KB topic files, queues, profile, irreversible-actions register.

## Continuity reconciliation (important)
- Prior session work was found on origin/arena/22655f48-dls26-omega: complete STATE_0 (2026-10-16, ckpt-20261016-setup-001) and STATE_1 turns 2–4 (ckpt-20261017-step1-003), with KB, sources log, logs, queues, profile and irreversible-action register.
- That work was imported losslessly into this branch (kb/, knowledge_management/, logs/, revision_register.md, user_profile.md, issue_tracker.md, kb_snapshots/, raw_game_data/). Prior handoff, prompt, rules digest, capability inventory and schema are preserved under docs/continuity/22655f48/ for provenance.
- No open PR existed (PRs #1–#5 all CLOSED). No second PR opened yet; one branch per session.
- Prompt discrepancy: prior capture was 173,446 bytes labelled v78; this session's delivered prompt is 175,596 bytes labelled v78 (43 changed lines, ~31 added clauses). The current delivered text is authoritative for this session; discrepancy logged OBS-007.

## Turn 9 result — numeric pass closed, checklist, negatives, Mechanism 3 walk
- Numeric transcription pass completed across 62 EV-backed claims: 4 corrections, including one figure removed for having no witness (CLAIM-087 "~186 MB").
- In-client checklist prepared (14 items, 3 tiers) as the future batched first-contact ask.
- Negative-finding register consolidated: 8 entries, each with queries, version and reopening condition; the weakest one is labelled as a failure-to-find.
- Mechanism 3 walk done: English community is the epoch's largest coverage deficit (snippet-level); technical depth is prohibited rather than unfound; no exhaustion declared.

## Turn 8 result — Step-2 collision, epoch draft, spot-check, storage
- **OBS-013 (first-contact decision):** the prompt's Step 2 requires APK decompilation; the verified EULA and sanction policy prohibit it and make it bannable. Precedence rung 2 resolves the collision in favour of not decompiling. Nothing was downloaded or decompiled. PROPOSED amendment written (not adopted). Step 2 is user-decision-blocked.
- Epoch contract drafted (DRAFT, not a seal) with counts, floors, lanes, projection definition, 7 placeholders and 6 final checks.
- Transcription spot-check: 10 claims read against their EV records; 2 defects fixed (CLAIM-007 evidence mis-attribution, CLAIM-005 missing witness); 53 more queued.
- Storage check: 2.3 MB tree, 3 MB .git, 198 files, far under the 250 MB ceiling. First KB snapshot committed.

## Turn 7 result — provenance, IN_PROGRESS accounting, exit readiness
- Branch provenance map written (docs/continuity/BRANCH_PROVENANCE.md): every artifact attributed; three unmerged branches remain (22655f48 / a7e23a6b / this one) and must be reconciled by any later session.
- All 23 IN_PROGRESS refs accounted individually; 18 are snippet-only pending access, 4 substantively complete, 1 a tail chunk.
- Exit readiness memo: STEP_1_RESEARCH_READY is **not met** — sealed contract absent, extraction incomplete, community coverage snippet-level; gap documentation and handoff are met. Recommendation: do not seal while the sandbox blocks the web.
- Coverage matrix refreshed with this environment's real reachability.

## Turn 6 result — parallel-branch delta, dispositions, Devil's Advocate
- OBS-012: branch 22655f48 had advanced to a78595c; its turn-5 block (GS-024…030, L-008, IRREV-002) was imported as CLAIM-113…118 and merged into the derived views. Three unmerged branches now exist; reconciliation queued (RQ-013).
- 15 UNVISITED refs dispositioned: 6 alias duplicates closed, 1 administrative, 1 scope-excluded, 7 still owed under access boundary (step1_epochs/UNVISITED_DISPOSITIONS.md).
- Devil's Advocate pass corrected three readiness overstatements in the topic map and the closure tone; one of this turn's own claims was demoted. Ledger: audit/DEVILS_ADVOCATE_step1_turn6.md.
- logs/conflicts.md consolidates five open and three resolved conflicts with the test that would settle each.
- Claims now 117.

## Turn 5 result — Skeptic pass and topic map
- Mechanism 2 pass over the 22 promoted claims found two provenance-mixing errors (official list carrying community numbers, multi-source finding carrying a single-thread number). Both corrected by splitting; five challenges recorded; nothing promoted. Ledger: audit/SKEPTIC_PASS_step1_turn5.md.
- EVIDENCE CONFLICT logged: 15 languages (store listing) vs 24 (APK listing data); unresolved, both kept labeled.
- step1_epochs/TOPIC_MAP.md built — every coaching-relevant topic mapped to claim IDs, with gaps named. It is the input for Step 4's dependency record and delivers no advice.
- Claim count 111; index regenerated with an open-challenges section; SCHEMA.md records the cross_refs[] addition.

## Turn 4 result — reconciliation closed, KB grown to 109 claims
- All 9 REVIEW alias rows resolved by promoting them (no claim covered them), so all 73 topic summaries now map to a live claim and no orphan remains.
- 22 claims added from already-captured evidence (CLAIM-089…110) at honest tiers; five remain Speculative with recorded challenges. KB tiers: Confirmed 27 / High 49 / Community Consensus 20 / Speculative 12 / Disputed 1.
- Coaching-relevant official mechanics now in the KB: Auto Switch default (CLAIM-106), skill-move swipe map (CLAIM-107), connection ladder + DNS fix (CLAIM-108), Graphics path (CLAIM-109), market-quality scaling (CLAIM-110).
- Derived views: kb/claims_index.md generated; six markdown files bannered as derived, claims.jsonl is the authority.
- Evidence accounting: 101/123 preserved EV/EVD records cited; 22 uncited classified (7 failure, 5 inventory, 9 revision tails, 1 gap). Both closure conditions still NOT MET.

## Turn 3 result — reconciliation and coverage
- Environment git reset recurred at turn start (OBS-006 recurrence); verified byte-identical content, rebuilt the index, nothing lost.
- Claim reconciliation: kb/claim_alias_map.md maps all 73 markdown summaries → 56 mapped / 9 review / 7 orphan-owed / 1 negative. kb/claims_index.md generated from the 87 live claims. Single authority: kb/claims.jsonl.
- Article coverage: the inherited "15 owed FTG bodies" was stale — 26/30 already captured across both corpora; only #19 (404), #26 (emojis) and #27 (kit visibility) remain uncaptured, plus a moved update slug.
- Closure test documented in step1_epochs/CLOSURE_STATUS.md: Condition 1 NOT MET, Condition 2 NOT MET, epoch stays OPEN. No seal claimed.
- Queue now carries the promotion (RQ-005), EV backfill (RQ-006), overdue-claim refresh (RQ-007, no date bump under access boundary) and retries (RQ-008).

## Turn 19 result — extraction wave 1 complete, every claim EV-backed, sample 9 clean, Step-2 plan drafted, chunk triage
- **Extraction wave 1**: 14 new EV records (EV-232..EV-245): 10 service-record EVs for S-*-witnessed claims (multiplayer networking, release-player, video-ads, version-gap resolution, stat scale, Cult Heroes roster, DLS27 signal, device-compat, sakibpro/community thread, reserves/subs megathread); 3 derived-view EVs (EV-242 launch-sentiment, EV-243 historical-player duplication and World Heroes, EV-244 facilities/envelope); 1 UGC EV for CLAIM-095 (EV-245). EVD-0005 registered in the index (old gap).
- **Result:** 129 claims, 148 EV records. Every claim has at least one EV/EVD token except CLAIM-103 (documented cross-ref-only synthesis of four EV-backed claims). 0 missing, 0 bad covers.
- **Sample 9**: 7 OK, 0 BAD (four covers-lag WARNs back-stamped). Three consecutive clean samples; ~3.2% cumulative substantive error rate over 63 sampled claims.
- **Step 2 plan drafted** (`step2_datamining/STEP2_PLAN_DRAFT.md`) with preconditions, forbidden actions, tool chain, and batched workflow S0–S7. Execution blocked on OBS-013; first contact does NOT wait for Step 2.
- **Chunk triage** (`step1_epochs/CHUNK_TRIAGE_turn19.md`): 6 CHUNK-COMPLETE-ENOUGH, 2 VISITED re-stamps owed as maintenance, 15 ACCESS-BOUNDED community families. No existing claim depends on unfinished chunks.

## Turn 18 result — RETRIEVAL-COMPLETE declared, covers back-stamped, sample 8 clean, safety gates added
- **Covers[] back-stamp**: 19 EV records (turn18a + turn18b) re-stamped so their `covers[]` lists the claims that cite them; closes the five sample-7 WARNs and the six sample-8 WARNs. One sample-8 BAD was a script false-positive (EV-001/EV-002 are `#ds-1/#ds-2` anchors in `evidence/raw/search_digest_turn1.md`); documented in CLAIM-007's challenges.
- **Sample 8**: 7 OK after repair, 0 substantive errors. Cumulative ~3.6% substantive-error rate over 56 sampled claims, dropping.
- **Pre-connection safety (S1/S2)** added to `IN_CLIENT_CHECKLIST.md`: verify Sign-in-with-Google/Apple is linked, and copy System-Info text, before any first-contact advice is followed. These derive from CLAIM-125 (User-ID path) and CLAIM-128 (save-backup no-recovery guarantee).
- **Epoch §5 closure review** (`EPOCH_CLOSURE_REVIEW_turn18.md`): all seven conditions met for coverage. **Step 1 = RETRIEVAL-COMPLETE / EXTRACTION-IN-PROGRESS.** 163 refs, 0 RETRYABLE, 2 ACCESS_BOUNDARY. 24 claims still lack a direct EV-* token; 23 IN_PROGRESS refs to triage.
- `CLOSURE_STATUS.md` updated with the turn-18 verdict; no seal claimed — extraction must finish first.

## Turn 17 result — sibling kb sweep completed, two captured-but-unclaimed articles claimed, sample 7 clean
- The six sibling kb topic files were read line by line against `claims.jsonl`. Their missing items were: (a) GS-036/034 can't-connect and find-user-ID — captured-but-unclaimed in turn 16, now EV-230/EV-231 supporting CLAIM-124 and CLAIM-125; (b) B-009 version-gap resolution — CLAIM-126; (c) GS-042 stat 0-1000 scale — CLAIM-127; (d) GS-037 save-backup nuance — CLAIM-128 (consolidates 042/072); (e) GS-039/040 Cult Heroes 12-card roster — CLAIM-129; (f) GS-041 adjacent special cards incl. Messi 87 — CLAIM-130. 129 claims, 133 EV records.
- CLAIM-042 strengthened (legacy iCloud vs current Sign-in-with-Apple/Google). DERIVED VIEW kb files synced.
- Sample 7: 0 substantive errors over 7 claims (5 covers-lag WARNs, 1 self-inflicted script-bug WARN). Cumulative ~4% substantive error rate over 49 tested claims.

## Turn 16 result — cross-branch merge: ID collision repaired, retryable debt driven to zero, four claims added
- **The sibling branch has no raw capture corpus** (28 files, no `evidence/`), so claims witnessed only by a `kb/*.md` summary cannot be upgraded from it. But its **service log** (69 records) is primary-adjacent, and ten claims were re-witnessed against it (traceability, not evidential strength — stated in each claim).
- **OBS-017, severe: source-log ID collision.** Twelve IDs (051–063, except 057) carried different records on the two branches; any citation of `S-20261017-05x` was ambiguous. Repaired by script: ours renumbered to 070–081, the sibling's 051–069 imported as canonical, full mapping written into the log's `id_repairs[]`, verified 81 entries / 81 unique IDs.
- **RETRYABLE_FAILURE is now 0.** The three articles carried as retryable since the t69 snapshot (control-button text, emojis, kit visibility) were fetched in full on the sibling at 17:10Z. EV-226/227/228 written; frontier 96 → 101 visited, 163 refs total.
- **Three never-admitted articles** discovered and admitted: fairness stance (360000842697), can't-connect (360003945557), find-user-ID (37082887837202).
- **Four new claims:** CLAIM-120 descriptive button text toggle (likely the mechanical answer to the "wrong input" complaint), CLAIM-121 emoji cap and chat kill-switch, CLAIM-122 imported kits are NOT visible to opponents, CLAIM-123 official fairness stance — the last sets a mission constraint: a "#1" target must span enough matches for luck to average out.

## Turn 15 result — a real error found and fixed, C-009 promoted to Priority 0, snapshot taken
- **Sample 6 (four mechanism pairs, economy and cadence):** one substantive error, three structural flags.
  - **CLAIM-020 was wrong**: it said "Free coins only via short video clips". EV-123 says *you can* watch clips to earn free coins (subject to availability) — no exclusivity — and the official coin list credits match wins, draws, clean sheets and goals. Rewritten; the acquisition channels and the ad-dependent clause are now separated because they carry different volatility.
  - **Three compound claims** (020, 025, 033) bundle two mechanisms under one tier. Flagged in place, not split (splitting would renumber evidence and invalidate the witness record). New rule: one mechanism per claim (`SCHEMA.md` §4c).
  - **CLAIM-103 is derived-only** (cites claims, not evidence) and now says so. No rate data exists anywhere in the corpus, which is why in-client item 8 matters.
- **C-009 promoted to Priority 0** of the in-client checklist: the Season Leaderboard screen decides whether "#1" is measurable at all.
- **C-002 strengthened** with EV-117: the official gem article lists five sources and never mentions leaderboard position.
- **Snapshot taken**: `kb_snapshots/claims_20261017T1728Z.jsonl` (118 claims, sha256 `f8dea58f…`); `kb/index.md` now carries the live index state, including the honest note that the topic summaries lag the claim authority by 31 claims.
- **Witness coverage 54/118 (46%).** Six samples, six findings, none empty.

## Turn 14 result — extraction debt paid, frontier re-stamped, pair sample found C-009
- **Three EV records written** (EV-223/224/225) for the captured-but-unpreserved support bodies (friend match, connection requirement, can't update). Each states **summary-only provenance** in its first lines — no body text was invented. A new claim, **CLAIM-119**, carries the official update-troubleshooting ladder, which had no claim before.
- **Frontier re-stamped** (RQ-018) in two waves: 8 status changes for refs actually served on 2026-10-17, then 5 alignments with the turn-6 disposition document. Final, tool-verified distribution: **96 VISITED / 23 IN_PROGRESS / 21 NON_CONNECTED / 8 UNVISITED / 3 RETRYABLE / 2 ACCESS_BOUNDARY / 8 DUPLICATE = 161**. File SHA-256 `78d689b8…`; the pre-stamp artifact stays unmodified in git history. Contract §2 rewritten from the tool output.
- **Pair-based witness sample (sample 5):** four mechanism pairs; three clean, one exposed a scope gap. **C-009**: the article that defines Leaderboards scopes them to Multiplayer (3–30 day resets), while the Season Leaderboard is a Main Menu board by Season Points — no official text links them, and nothing shows whether it is public. Because "#1" is the mission's success condition, this is the most consequential open question in the KB. CLAIM-003 amended; RQ-019 queued for an in-client look.
- **Witness coverage 46/118 claims (39%).** No tier lowered; no date bumped without a check.

## Turn 13 result — frontier reconciled (the count was nine refs stale), CLAIM-100 corrected, sample 4
- **The epoch's debt profile is now correct.** Diffing this workspace's 63-entry service log against the recovered 161-ref frontier found **11 stale statuses**: five refs recorded as RETRYABLE_FAILURE and two as UNVISITED had already been captured in full on 2026-10-17, and two IN_PROGRESS refs advanced by chunk. The contract's "9 retryable" is really **4** (one of which is a superseded article ID). The frontier was never re-stamped after the tools returned — the count was inherited from the t69 snapshot. Report: `step1_epochs/FRONTIER_DELTA_turn13.md`.
- **CLAIM-100 corrected and promoted.** The device-compatibility article that 404'd on 2026-10-10 served full text on 2026-10-17: "iOS compatible with most devices… Android 3,000+ devices… availability restricted by hardware/carrier/territory… minimum OS varies per app". The claim now states the capture history and the content; Speculative → **High Confidence**. NEG-009 records the general lesson: a 404 on one date does not prove permanent removal.
- **Sample 4 (8 High Confidence single-witness claims):** seven pass verbatim or at derived-summary level; CLAIM-014 reproduces a 12200-era rule that the current official article has replaced (Season Points, not DLL XP) — supersession note added; CLAIM-094 now discloses that its "24 languages" is one side of C-001. Union of witness-tested claims: **38/117 (32%)**.
- **Two queue items added** (RQ-017 extraction of three captured bodies; RQ-018 frontier re-stamp with a migration note).

## Turn 12 result — interpretive sample, C-008, freshness repair, executable frontier
- **The most consequential finding so far.** Community says Career promotion runs on Division Objectives (wins+goals); the only official text says promotion is an XP ladder (wins +XP, losses −XP, max XP promotes). Both cannot be the same mechanism as described. **C-008** added; CLAIM-062 carries a challenge blocking objective-efficiency coaching until a Career screen is captured.
- **Sample 3** (`audit/WITNESS_SPOTCHECK_sample3_turn12.md`): 10 low-tier claims; 9 faithful, 1 conflict, 2 wording drifts. Union of textually witnessed claims now 30/117 (26%).
- **Freshness repaired**: CLAIM-003/006 were verified on/after their due dates — the `next_due` field, not the knowledge, was stale. Re-derived from `last_valid_check` + modal interval and the repair written into each claim.
- **Frontier is now executable**: recovered the missing 161-ref frontier log from branch a7e23a6b (`5ab3ec6`) into `docs/continuity/a7e23a6b/logs/`; `frontier.py summary` reproduces the contract's §2 distribution exactly (91/23/2/9/15/20/1). The epoch count is no longer an inherited number.
- **Contract §5a** is now a seven-step freeze procedure ending in a digest; epoch still DRAFT and unsealed.

## Exact resumption point (next turn — turn 20)
1. **Maintenance re-stamps**: two refs (ref-cant-update, ref-support-section-inventory) are actually fully captured (EV-225, EV-114) but still marked IN_PROGRESS in the frontier. Re-stamp them VISITED; CHUNK-COMPLETE-ENOUGH the 6 chunked refs per the triage note.
2. **Extraction pass, wave 2**: iterate over uncited EV records (the 22 classified uncited at turn 4 plus any new ones added since) to confirm the classification still holds and that no EV is silently supporting an unwritten claim. If any EV contains a meaningful mechanic that is not yet a claim, write it.
3. **Sample 10** of the witness pass.
4. **Topic-summary DERIVED view sync**: after chunk re-stamp, update the derived-view kb/*.md files to reflect the final EV-backed claim set (last sync was turn 17).
5. If all of the above are clean, **call EXTRACTION-COMPLETE** and mark the Step 1 epoch CLOSED (retrieval + extraction both complete under access-bounded conditions). That transitions the bootstrap to Step 2 plan-execution-prep and Step 3 device-pipeline readiness.
6. Web remains ACCESS_BOUNDARY. OBS-013 remains a first-contact decision. No new registers (D-06). JSONL rewrites through scripts/ with byte verification.

## Owed debt / open items
- OBS-001, OBS-002, OBS-003, OBS-007 (same-version byte drift), OBS-008 (continuity import), OBS-009 (repaired), OBS-010 (Setup wall-clock), OBS-011 (two claim systems, reconciliation queued), OBS-014 (claim-schema hygiene, documented non-propositional).
- Step 1 gaps: web families ACCESS_BOUNDARY this environment; version gaps 13.140-13.299 and 13.360-13.400; true non-English forums; technical/decompilation layer unavailable; UGC partial.
- Step 2/3 blocked in this sandbox: no java/ADB/APK tooling/device. Recorded as capability limits, never as done.
- Optional user-side unblock (for first contact, not asked now): push captured pages/APK/save files into raw_game_data/ — the system will process them as read-only input.
