# raw_game_data — read-only inputs from external scripts

Contents: none. Setup found no device and no extraction.

Files here come from ADB extractions, save pulls and API captures pushed by the user's scripts. Formats are the game's own. The agent reads and interprets them and never modifies them. Each file needs extraction metadata: time, device or build, and method.

On arrival: process immediately; update the persistent fields of user/USER_PROFILE.md (not match results or mid-session deltas); flag every change from the previous state; verify extraction metadata for staleness; assess the implications for active recommendations. See OPERATIONAL_RULES.md (RAW GAME DATA DIRECTORY).
