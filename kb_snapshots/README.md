# KB SNAPSHOTS
Dated copies of `kb/claims.jsonl`. Kept indefinitely (KB SNAPSHOTS rule). Taken at every significant push and at session end.
Rollback procedure: identify the last snapshot before a corruption, diff forward to establish which claims it touched, re-verify or restore those claims, log the rollback with its scope and trigger.
| Snapshot | Claims | Note |
| --- | --- | --- |
| claims_2026-10-17T2032Z.jsonl | 117 | First snapshot on this branch after the two-corpora merge |
| claims_20261017T1728Z.jsonl | 118 | Turn-15 snapshot: CLAIM-119 added; CLAIM-020 corrected; frontier re-stamped; sha256 f8dea58ff1293b74 |
