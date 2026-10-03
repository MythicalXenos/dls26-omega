# RAW GAME DATA — READ-ONLY INPUTS

Files pushed here by user-side scripts: ADB extractions, save pulls, API captures. **The agent reads and interprets these; it never modifies them.** Their format is the game's, not a design choice.

Layout: `{YYYY-MM-DD_HHMM}__{device}__{account}/` containing `METADATA.json` (SCHEMA.md §2.7) plus the raw files.

On new data appearing: process immediately → update the persistent club/game-state fields of `kb/user_profile.md` (excluding individual match results and mid-session resource deltas, which go to MATCH LOG) → flag every change from the previous state → verify metadata for staleness → assess implications for active recommendations.

**OWNERSHIP VS EXISTENCE (PROMPT.md §13 Step 3):** the presence of an asset, model, face pack, name or database record in static client files is never evidence that the user owns or has unlocked it. Roster/ownership claims require direct game-state evidence: extracted save telemetry from this directory, or the user's confirmation with verified UI screenshots.

Credential redaction is applied before anything here is committed (PROMPT.md §6 DATA SANITIZATION).

**Status: empty. No extraction has ever been pushed.**
