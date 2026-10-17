# IN-CLIENT OBSERVATION CHECKLIST — the batched ask
Prepared 2026-10-17T20:48Z (session sess-20261017-001). Updated turn 18 (2026-10-17T21:55Z) with pre-connection safety items. This file holds the observations only the player can make, written now so that when the bootstrap reaches first contact the ask is specific, batched and short — not a vague "tell me about your team". Nothing here is asked yet; it is prepared.

**Why these and not others:** each item fills a gap that currently blocks a coaching decision (`step1_epochs/TOPIC_MAP.md`). Anything already answered by official text is excluded on purpose — the ask is only for what the KB cannot supply.

## Pre-connection safety (turn 18 addition — ask BEFORE any execution advice is followed)
These two items must be confirmed on the player's device the very first time contact happens, and before any experimentation. Both derive from claims added turn 17 (CLAIM-125, CLAIM-128).

| # | Where to look | What to report | Why it matters |
| --- | --- | --- | --- |
| **S1** | Options (gear, top-left) > **Game Settings / account settings screen** | Is **Sign in with Google** (or Sign in with Apple on iOS) shown as **LINKED / CONNECTED**? If not, stop here and link it before making any change. | CLAIM-128: unlinked profiles carry a no-recovery guarantee after uninstall/reset. We do not want to be the cause of a lost account. |
| **S2** | Options > Advanced > **System Info** (the "i" button) > **Copy Info** | Paste the copied text somewhere (it contains User ID, build, device). We only need the build string and User ID prefix — the ID itself goes to support, not to chat. | CLAIM-125: confirms the build the player is actually on (13.430? newer?) and gives a recovery handle in case anything goes wrong. This also settles freshness for B-001 on the actual device. |

## Priority 0 — one question that defines the mission (moved here turn 15)
| # | Where to look | What to report | Why it matters |
| --- | --- | --- | --- |
| **0** | Main Menu > **Season Leaderboard** | (a) Does it list **other players**, or only your own total? (b) Is a **rank/position number** shown? (c) Any **reset timer or season label**? (d) Is there an option to change scope (global/friends/division)? | **This single screen decides whether "#1" can be measured at all.** C-009: the official Leaderboards article scopes boards to Multiplayer (3–30 day resets, EV-101), while the Season Leaderboard is a Main Menu board by Season Points (EV-197) — no text links them and nothing states whether Season Points ranking is public. If it is not public, the mission target must be redefined on the DLL leaderboards or LIVE Tier. |

## Priority 1 — unblocks execution advice (five minutes, one sitting)
| # | Where to look | What to report | Why it matters |
| --- | --- | --- | --- |
| 1 | Controls: settings gear (top-left) > Controls | The full list of options and their current values (auto-switch, assist toggles, control layout if present) | Nothing about execution can be precise until the option set is known |
| 2 | Profile > Graphics (Android) or the equivalent iOS screen | FPS cap and quality preset you actually run | Frame rate changes timing feel; advice must match your setting |
| 3 | Any match, pre-kick-off screen | Camera height/zoom options offered and which you use | Camera choice changes passing angles and defensive reading |
| 4 | Squad screen | One player's attribute panel: exact stat labels shown (SPE/ACC/… or renamed?) | Confirms the official stat model still uses those labels in 13.430 |
| 5 | Main menu | Whether a version/build number is displayed, and what it says | Settles whether you are on 13.430 or newer |

## Priority 2 — unblocks progression and economy planning
| # | Where to look | What to report | Why it matters |
| --- | --- | --- | --- |
| 6 | Your current division and Season Points | Division name, points, matches played this season | Every progression projection needs a starting point |
| 7 | Season Leaderboard (Main Menu) | The exact **label** and the metric wording — the scope question moved to item 0 | Label precision only; scope is Priority 0 now |
| 8 | One completed career match | Coins earned, Season Points earned, XP shown (if any), clean-sheet/goal bonuses listed | The KB has source lists but no rates |
| 9 | Transfers > Manage Players > select one reserve | Whether a release preview shows a coach, coins, or both | Settles conflict C-003 on current build |
| 10 | Prize Ladder screen | Current event name and the reward milestones visible | Confirms the live event against the last capture (Oct 2026) |

## Priority 3 — squad reality (needed before any squad recommendation)
| # | Where to look | What to report | Why it matters |
| --- | --- | --- | --- |
| 11 | Squad | Your formation, and each starter's position + OVR | The candidate work cannot start from a squad nobody has described |
| 12 | Squad | Number of substitutes allowed and whether reserves are visible | Confirms CLAIM-101 (reserves + eight subs, community tier only) |
| 13 | Transfers | The transfer market refresh state and one player's price | Tests CLAIM-110 (market quality scales with progress) |
| 14 | Items/inventory | Whether you hold any coaches, and their rarity names | Coach ROI is unmeasured; rarity names are also unsettled |

## Format that makes this cheap for you
Screenshots are ideal and need no transcription — one folder pushed into `raw_game_data/` is read as a read-only input. If screenshots are not practical, one line per numbered item is enough: `7: "Season Leaderboard", shows Season Points, resets in 12d`.

## What happens with each answer
Each observation becomes a claim with `user-stated` origin (Evidence Hierarchy), tiered at whatever the observation can support — a single screen is usually Community Consensus at best until it corroborates an official value — and the relevant gap in `TOPIC_MAP.md` is closed or narrowed. Answers that contradict the KB are recorded as conflicts (`logs/conflicts.md`) rather than overwritten.
