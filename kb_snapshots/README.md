# KB SNAPSHOTS
Full KB snapshots are committed here at the end of every session and additionally as part of every significant push during a session (which push turns out to be last is never knowable in advance — snapshotting only at a presumed "last" one risks having none at all). All snapshots are kept indefinitely.

Naming: `kb_snapshot_<UTC-date>_<seq>.md` (sequential numbering, all files accessible — per STORAGE MANAGEMENT rotation).

Rollback procedure (per KB SNAPSHOTS): where a defect turns out to have corrupted several claims rather than one (a bad source weighted too highly, a misread value propagated through the KB, a promotion that should never have happened), identify the last snapshot taken before the corruption entered, diff forward from it to establish exactly which claims it touched, re-verify or restore those claims, and log the rollback with its scope and its trigger. A defect found in one claim is an issue-tracker entry; the same defect found in claims that share an origin is a rollback.

**Status: no snapshots yet** — the KB is empty at bootstrap start (Turn 1, STATE_0_SETUP).
