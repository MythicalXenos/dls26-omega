# raw_game_data

Read-only inputs pushed by external scripts (ADB extractions, save pulls, API captures). The agent reads and interprets these files and never modifies them. Their format is the game's own. Empty at Setup. On each new file: process immediately, update club/game state in the User Profile, flag every change from the previous state, check extraction metadata for staleness, and assess implications for active recommendations.
