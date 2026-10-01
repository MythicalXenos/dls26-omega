# TOOLS AND SCRIPTS

Self-contained, documented, versioned, each with its own CHANGELOG (PROMPT.md §8 TOOLS AND SCRIPTS).

| Directory | Purpose | Status |
|---|---|---|
| `state_extraction/` | On-demand ADB snapshot script the user runs on their MacBook with the Galaxy S9+ connected. Pulls game state/save files, writes METADATA.json, pushes to `raw_game_data/`, and reports push failures (auth/network/conflict) back to the user directly. Never scheduled, never persistent, no cron. | DESIGN OWED — STATE_3_DEVICE_PIPELINE |
| `capture_pipeline/` | risk Tier 3 API-capture design, only if research shows FTG's live traffic carries enough structured state to be worth it. Risk stated before the user considers it. | RESEARCH OWED — STATE_3 |

The agent cannot modify a script running on the user's MacBook from inside the sandbox. When raw data is absent, stale or malformed, the agent flags it, determines whether the game changed its file layout, and outputs a corrected script for the user to deploy.
