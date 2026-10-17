# BRANCH PROVENANCE MAP — DLS26 OMEGA
Built 2026-10-17T19:52Z (session sess-20261017-001, turn 7) under RQ-20261017-013 / OBS-012.
Purpose: attribute every imported artifact to the branch and checkpoint it came from, so a later session can tell what is verified in this session from what was inherited, and can reconcile the three unmerged branches without guessing.

## Live state of the repository (verified by `git ls-remote` this turn)
| Branch | Head | Meaning |
| --- | --- | --- |
| `main` | fb9a2c0 | Initial commit only (README, .gitignore). No research. |
| `arena/22655f48-dls26-omega` | a78595c | v78 Setup + Step 1 turns 2–5. Owner of the markdown topic KB (T/B/L/M/GS records) and the irreversible-actions register. |
| `arena/a7e23a6b-dls26-omega` | 5ab3ec6 | v77 long research run (≈1,034 log files, 87 claims, 118 evidence extracts, t69 coverage accounting). Owner of `kb/claims.jsonl` before this session. |
| `arena/b5d5681d-dls26-omega` | **this branch** | v78 Setup re-done, both corpora imported, reconciliation, Skeptic/DA passes, disposition and accounting work. |
No PR is open for any of them (PRs #1–#5 are closed).

## What this branch imported, and from where
| Artifact now live | Source | Import method | Integrity note |
| --- | --- | --- | --- |
| `DLS26_OMEGA_PROMPT.md` (175,596 B, SHA-256 b7fd30da…) | This session's delivered prompt | Written mechanically in four chunks | 25/25 rule blocks balanced; 25 unique IDs |
| `docs/prompt_archive/OMEGA_PROMPT_v76.md`, `…_v78_2026-10-17.md` | Same | Copies | Byte-identical to the live file at write time |
| `kb/claims.jsonl` (87 claims at import) | a7e23a6b @ 5ab3ec6 | Verbatim copy | Column set unchanged; 87 → 117 claims by append + in-place field edits recorded in the log |
| `docs/continuity/a7e23a6b/` (evidence 123 files, schemas, tools, prep docs, coverage accounting) | a7e23a6b @ 5ab3ec6 | `git archive` extraction | Preserved verbatim; never edited |
| `step1_epochs/coverage_accounting/` | a7e23a6b | Copy of `docs/step1` | Preserved verbatim |
| `kb/build-version.md`, `community-meta.md`, `game-systems.md`, `live-state.md`, `terminology.md`, `source-families.md` | 22655f48 @ d12a84c, updated to a78595c delta | Checkout + appended turn-5 additions | Now carry a DERIVED VIEW banner; `claims.jsonl` outranks them |
| `knowledge_management/irreversible_actions.md` | 22655f48 @ a78595c | Replaced with newer version | IRREV-001 and IRREV-002 both present |
| `logs/sources_visited.json` (50 entries at import) | 22655f48 @ d12a84c | Checkout | Entries S-001…050 inherited; S-051…063 added this session |
| `logs/main_operational_log.md`, `revision_register.md`, `user_profile.md`, `issue_tracker.md` | 22655f48 | Checkout + appended entries | Inherited entries untouched; this session appends |
| `logs/research_queue.json` | 22655f48 | Checkout, then rewritten to a queue with IDs | Original content preserved inside the new items where it was actionable |
| Prior prompt/rules/capability/schema snapshots | 22655f48 @ d12a84c | Copies | `docs/continuity/22655f48/` |
| Claim additions CLAIM-089…105 | Synthesised this session from 22655f48 markdown summaries | New records | Each cites the summary and its underlying capture; tier set from the summary, no inflation |
| Claim additions CLAIM-106…112 | Synthesised this session from **a7e23a6b EV records** (EV-145/150/151/156/191 + guideline) | New records | Each cites the EV record |
| Claim additions CLAIM-113…118 | Imported from 22655f48 @ a78595c turn-5 (GS-024…030, L-008) | New records | Each cites the GS/L record and its article ID |

## Known provenance risks
1. **Same content in two branches.** GS-001…GS-023 (22655f48) and EV-101…EV-222 (a7e23a6b) describe overlapping facts captured in different sessions. Where they agree, independent capture is not proven — both sessions may have read the same article text from the same FTG pages. Agreement is therefore **corroboration of transcription, not independent confirmation**, and no claim was promoted on it in this branch.
2. **Claim edits by this branch.** Claims imported from a7e23a6b were edited in place (field additions, challenge strings, two splits). Any future comparison against 5ab3ec6 must expect those diffs; they are all logged in the main operational log and the two audit files.
3. **Derived summaries can lag.** The markdown files were updated to a78595c only insofar as the turn-5 additions were appended; the rest of their text is from d12a84c. A reader must prefer `claims.jsonl`.
4. **The three branches are not merged.** Nothing in this branch is merged into `main`. A later session must not treat any one branch as "the" complete state without this map.

## Branch reconciliation procedure (for a later session, or for me if time allows)
1. `git fetch` all `refs/heads/*` and compare each head to the values above; a moved head is a new delta to import, exactly as a78595c was in turn 6.
2. Diff each branch's KB against `claims.jsonl` claim-by-claim. New propositions become new claim IDs; conflicting values go to `logs/conflicts.md` with both sides.
3. Never overwrite a claim record with another branch's text; append a replacement history entry instead (the schema has `replacements`).
4. After import, log the delta in the main log as an ANOMALY with the branch and commit hash, as was done for OBS-012.
