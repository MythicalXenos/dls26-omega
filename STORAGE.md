# STORAGE MANAGEMENT — DLS26 OMEGA
Checked 2026-10-17T20:30Z (turn 8). Owner: system (STORAGE MANAGEMENT rule — the user never needs to think about this).

## Current measurements
| Metric | Value |
| --- | --- |
| Working tree (excl. `.git`) | 2.3 MB |
| `.git` | 3.0 MB |
| Tracked files | 198 |
| Largest tracked file | 172 KB (`DLS26_OMEGA_PROMPT.md` and its three archive copies, identical) |
| Evidence records imported | 123 files under `docs/continuity/a7e23a6b/evidence/` |
| Claims | 117 in one JSONL (136 KB) |

## Limits and thresholds
- GitHub hard limits: 100 MB per file, ~5 GB per repository; a warning appears around 1 GB.
- Chosen operational ceiling for this repo: **250 MB**, with a review at 150 MB. At the current growth rate (≈2 MB per session including the prompt copies) the ceiling is decades away; the binding limit will be the prompt archive, which duplicates 172 KB per version.
- Rotation plan: the only high-frequency file is `logs/main_operational_log.md`. It will be rotated at **2 MB** into `logs/archive/main_log_<year>_<seq>.md`, referenced from an index, and never truncated.
- Snapshots: `kb_snapshots/` holds dated copies of `claims.jsonl`. At 136 KB per snapshot, a yearly cadence is trivially cheap; a per-session cadence is affordable until roughly 1,000 sessions.
- Raw game data (`raw_game_data/`): user-supplied, potentially large. Not committed if a capture exceeds 20 MB — it will be summarised into an EV record and the original kept outside Git, with a pointer recorded in `logs/sources_visited.json`.

## What will be done, not asked
- Rotate the main log before it reaches 2 MB.
- Keep the prompt live file plus one archive per adopted version; older archives move to `docs/prompt_archive/older/` if the directory exceeds 50 files.
- Re-measure at every Step-4 rebuild and at each bootstrap completion.

## Current verdict
No action required. Repo is 0.1% of the operational ceiling.
