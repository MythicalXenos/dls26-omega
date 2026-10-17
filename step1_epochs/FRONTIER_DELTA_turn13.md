# FRONTIER RECONCILIATION — live service log vs the recovered t69 frontier (turn 13)

Date: 2026-10-17T18:5xZ. Purpose: freeze-procedure step 1 (`EPOCH_CONTRACT_DRAFT.md` §5a). Until this turn the contract carried §2's counts as an inherited summary; the frontier log was recovered last turn and is executable, but it had never been diffed against this session's own service log. This document is that diff.

## 1. What the two objects are
- **Frontier** — `docs/continuity/a7e23a6b/logs/sources_visited.json`, recovered from branch `a7e23a6b` at commit `5ab3ec6`: **161 references**, each with `ref_id`, url, family, status, projections, and a service-event history. Single status per reference.
- **Service log** — `logs/sources_visited.json` (this workspace): **63 entries**, one per retrieval or probe, with free-text statuses and payload summaries. Many entries are search queries or environment probes, which are not references.
- They are complementary, not duplicate: the frontier answers "what is owed", the service log answers "what was actually done".

## 2. Matching
Normalising URLs (lower-case, strip `web_search:` prefixes, chunk suffixes, trailing slashes) and matching against the 161 references:

| Class | Count | Meaning |
| --- | --- | --- |
| Exact URL match to a frontier ref | **29** | the same reference has been served again |
| Search queries (`web_search: …`) | **19** | discovery-slice activity, not references |
| Repository / API operations (git, gh api, npm registry, archive) | **5** | environment and continuity work, not game sources |
| Environment probes (github, npm, google control) | **4** | capability tests |
| Game URLs with no frontier ref | **4** | `dlsinside.com/` and `dlsinside.com/players[…]` — these belong to refs whose recorded URL differs by path |
| **Total** | **63** | |

## 3. The finding: eleven frontier statuses are stale

The frontier is a **t69 snapshot**. FTG support pages that were 404 or unvisited at t69 were fetched successfully later the same day (13:30Z), after the tools returned at t1035. The frontier was never re-stamped, so the contract has been quoting a state that is nine refs out of date.

| Ref | Frontier says (t69) | What the service log shows | Correct state |
| --- | --- | --- | --- |
| ref-support-friend-match | RETRYABLE_FAILURE | S-…-040, full text + comments, 2026-10-17 | **captured**; EV extraction still owed (GS-014 note) |
| ref-support-restart-career | RETRYABLE_FAILURE | S-…-041, full text, 2026-10-17 | **captured**; content is CLAIM-082's source |
| ref-support-connection-required | RETRYABLE_FAILURE | S-…-042, full text, 2026-10-17 | **captured** (note: the EVD-0005 404 was on slug 360004575718; the live article is 360004034498) |
| ref-support-device-compat | RETRYABLE_FAILURE | S-…-043, full text, 2026-10-17 | **captured** — see §4 |
| ref-support-cant-update | RETRYABLE_FAILURE | S-…-045, full text, 2026-10-17 | **captured** |
| ref-support-next-update | UNVISITED | S-…-027, full text, 2026-10-17 | **captured**; already dispositioned REPRESENTATION_DUPLICATE → EV-131 |
| ref-support-dls19-profile | UNVISITED | S-…-047, full text + comments, 2026-10-17 | **captured**; already dispositioned REPRESENTATION_DUPLICATE → EV-132 |
| ref-store-appstore | IN_PROGRESS | chunks 0–1 of 6, 2026-10-17 | still partial (chunks 2–5 owed) |
| ref-support-player-stats | IN_PROGRESS | chunk 0 of 4, 2026-10-17 | still partial (comment chunks 1–3 owed) |
| ref-support-season-pass (rev2 ID 440407098513) | RETRYABLE_FAILURE | current article 4404070913169 captured (S-…-021 → EV-162) | **superseded ID** — the retry target no longer exists under that number; the live article is captured. Confirm, then reclassify REPRESENTATION_DUPLICATE |
| ref-ftg-zendesk-alias-dead | ACCESS_BOUNDARY | S-…-056, TLS failure, 2026-10-17 | **unchanged** — genuine boundary |

## 4. Consequence for CLAIM-100 (a real correction)
CLAIM-100 said: *"Device compatibility guidance exists as an official article … but the page returned a Zendesk 404 in the prior capture … No verified minimum-spec list is held."* The 404 was true on 2026-10-10 (EVD-0005). On **2026-10-17 at 13:30Z the same article served full text**:

> iOS: compatible with most devices; check the App Store for the minimum OS version (varies per app). Android: 3,000+ devices supported; availability restricted by device hardware, carrier restrictions, territory legislation; minimum Android OS varies per app — check Google Play.

So the *page* is alive and the *substance* (no published minimum-spec list) is confirmed by the article itself. CLAIM-100 was corrected this turn: the proposition now states the capture history, the content, and keeps the conclusion that only the store requirement is a hard anchor. Tier raised Speculative → **High Confidence** (one official full-text capture plus the historical failure record); the EVD-0005 record is retained as history, not deleted.

## 5. Effect on the epoch contract

| Status | Contract §2 (t69) | After this reconciliation | Notes |
| --- | --- | --- | --- |
| VISITED | 91 | 91 + 5 resolved = **96** (of the 161) | pending a re-stamp of the frontier file |
| IN_PROGRESS | 23 | **23** | two advanced by chunks, none completed |
| UNVISITED | 15 | **15** (8 dispositioned, 7 owed) | two were served but were already duplicates |
| RETRYABLE_FAILURE | 9 | **4** | five captured; see §3 (one of the four is a superseded ID) |
| NON_CONNECTED | 20 | 20 | unchanged |
| ACCESS_BOUNDARY | 2 | 2 | unchanged |
| REPRESENTATION_DUPLICATE | 1 | 1 (+1 pending) | |

**The honest description of the epoch is therefore: retrieval debt is much smaller than the contract said; extraction debt is unchanged.** Three articles have content in the service log that was never turned into an EV record, and two more have equivalent captures under superseding IDs — that is the actual remaining work, and it is work this environment *can* do.

## 6. What was deliberately not done
- The frontier file itself was **not edited**. It is an imported artifact at a named commit; re-stamping it would erase the evidence that a t69 snapshot existed and that the tools were down. The delta lives here and in the contract, and a future session re-stamps the frontier with a new commit and a written migration note.
- No EV records were fabricated for the five captures. Their payload summaries are in the service log; converting them to EV records requires reading the captures, which this turn did not do.
- The four `dlsinside` URLs were not force-matched to refs whose paths differ; that is an accounting question for the freeze, not a research one.

## 7. Next actions (queued, not done)
1. Promote the five captured bodies to EV records (F-1…F-5 in §3), which will also settle which article IDs are canonical.
2. Re-stamp the frontier at the next checkpoint with the eleven changes in §3 and a migration note.
3. Recheck `ref-support-season-pass-rev2` — if 440407098513 never resolves, reclassify as REPRESENTATION_DUPLICATE.
4. Then run freeze steps 2–7.
