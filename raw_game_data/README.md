# RAW GAME DATA DIRECTORY
Dedicated directory for game files pushed by external scripts: ADB extractions, save pulls, API captures (per the RAW GAME DATA DIRECTORY rule).

- These are **read-only inputs** — the agent reads and interprets them, never modifies them. They are not agent-designed files; their format is the game's.
- When new raw data appears: process immediately; update the persistent club and game state fields of the User Profile (excluding individual match results and mid-session resource deltas, which go to the main operational log's MATCH LOG category per Knowledge Management); flag every change from the previous state; verify extraction metadata for staleness; assess implications for active recommendations.
- **Status: EMPTY** — no raw game data has been received (Turn 1, STATE_0_SETUP).
- Sandbox limitation: ADB is not installed in this environment (see CAPABILITY_INVENTORY.md §4); device-side extraction will require user-provided data dropped here.
