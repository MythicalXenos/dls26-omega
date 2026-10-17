# KB SNAPSHOTS
Dated copies of `kb/claims.jsonl`. Kept indefinitely (KB SNAPSHOTS rule). Taken at every significant push and at session end.
Rollback procedure: identify the last snapshot before a corruption, diff forward to establish which claims it touched, re-verify or restore those claims, log the rollback with its scope and trigger.
| Snapshot | Claims | Note |
| --- | --- | --- |
| claims_2026-10-17T2032Z.jsonl | 117 | First snapshot on this branch after the two-corpora merge |
| claims_20261017T1728Z.jsonl | 118 | Turn-15 snapshot: CLAIM-119 added; CLAIM-020 corrected; frontier re-stamped; sha256 f8dea58ff1293b74 |
| claims_20261017T1731Z.jsonl | 122 | Turn-16 snapshot: cross-branch merge, CLAIM-120..123 added, 10 witnesses upgraded from summaries to service records, RETRYABLE_FAILURE -> 0; sha256 c613b7fc2f9a46b4 |
| claims_20261017T1738Z.jsonl | 129 | Turn-17 snapshot: sibling kb sweep, CLAIM-124..130, EV-230/231, EV-105 raw anchor re-validated; sha256 4e2146a0782e78c5 |
| claims_20261017T1746Z.jsonl | 129 | Turn-18 snapshot: retrieval-complete declaration, covers back-stamped, sample 8 clean, pre-connection safety items; sha256 7fc7f550e0bc1d03 |
| claims_20261017T1754Z.jsonl | 129 | Turn-19 snapshot: extraction wave 1 (13 EV service + 3 derived + 1 UGC added), every claim now EV-backed (except CLAIM-103 cross-ref-only), sample 9 clean, Step-2 plan draft, chunk triage; sha256 43087573185fb74a |
| claims_20261017T1801Z.jsonl | 129 | STEP 1 CLOSURE snapshot: 129 claims, 148 EV, 0 IN_PROGRESS/RETRYABLE on 163 refs; sha256 43087573185fb74a |
