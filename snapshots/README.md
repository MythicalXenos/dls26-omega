# KB SNAPSHOTS

Full KB snapshots: `kb_snapshot_{YYYY-MM-DD}_{seq}/`. Taken at the end of every session **and** as part of every significant push during it — which push turns out to be last is never knowable in advance. Kept indefinitely; never pruned, never overwritten.

**Rollback procedure (the reason snapshots exist):** where a defect turns out to have corrupted several claims rather than one — a bad source weighted too highly, a misread value propagated, a promotion that should never have happened — identify the last snapshot taken before the corruption entered, diff forward to establish exactly which claims it touched, re-verify or restore those claims, and log the rollback with its scope and trigger. A defect in one claim is an issue-tracker entry; the same defect in claims sharing an origin is a rollback.

**Status: the first snapshot is taken at the end of this session (and at the first significant push).**
