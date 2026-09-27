# GAPS — two states, and they are not the same thing

Per PROMPT.md §8 GAPS.

- **CLOSED — "evidence confirms this does not exist."** The question closes. Recorded as a NEGATIVE FINDING in `logs/main_operational_log.md` with the sources establishing it and the game version it was established against. Never volatility-Frozen: a patch that could plausibly have added or changed the thing reopens it, decided by comparison against the recorded version.
- **OPEN — "no evidence either way."** The question stays open, and this is not neutral: it normally means the thing may exist and simply has not been recorded yet. Re-checked on later passes and after any patch touching the area.

**Never record "no records found" as "does not exist."** Where it is unclear which state applies, use OPEN.

An open gap and an exhaustion declaration are not in conflict: the declaration closes the *research done so far*; the open state names what would reopen it.

## CLOSED gaps (negative findings)

| # | Question | Establishing sources | Game version | Date | Log ref |
|---|---|---|---|---|---|
| — | none yet | | | | |

## OPEN gaps

| # | Question | What has been searched so far | What would reopen/answer it | Owed by | Added |
|---|---|---|---|---|---|
| G-0001 | Does DLS26 have position locking / out-of-position penalties? (user-stated: no position locking — verification owed per PROMPT.md §7) | nothing yet | Step 1 sweep: official docs, databases, community testing, APK data | STATE_1 | 2026-09-27 |
| G-0002 | What is the current client version, exactly? (13.420 vs 13.430 conflict) | 1 search + 1 official page render | Conflict Protocol: Play Store + App Store listings across regions, FTG channels, APK metadata | STATE_1 | 2026-09-27 |
| G-0003 | Is DLS26 the game's actual name, or has the franchise rebranded? (franchise-continuity rule) | FTG /games page still says "Dream League Soccer"; store listing says "Dream League Soccer 2026"; package id is `com.firsttouchgames.dls7` | Step 1 sweep across FTG channels and stores | STATE_1 | 2026-09-27 |
| G-0004 | Can a real DLS26 APK be obtained from inside this sandbox? | shell egress map only (§4 CAPABILITY_INVENTORY.md) | Step 2: GitHub-hosted APK/asset repos via codeload, community dumps, databases | STATE_2 | 2026-09-27 |
| G-0006 | Does the game work offline? The Play Store tags it "Offline" while FTG's own description says it "requires an internet connection" | 1 official page carrying both statements (S-0011, S-0012) | FTG support docs, community testing, client behaviour; likely reconciliation is offline career play with online requirements for some modes — NOT established | STATE_1 | 2026-09-27 |
| G-0007 | What are `ftgames.com` and its privacy policy, and how do the two official domains divide responsibility? | domain discovered via the store listing (S-0012); never fetched | page-render ftgames.com root + /privacy-policy (also a source for SDK/anti-cheat disclosure → risk Tier 3 and ban-risk research) | STATE_1 | 2026-09-27 |
| G-0008 | What is the Play Store event ending 10/14 ("The names the fans remember, from their peak years"), and is it the "Cult Heroes" collection? | event block on the official listing (S-0012) | page-render eventdetails/4830045897422713648; FTG channels; in-game. A live cycle timer — the user is grinding a ladder now | STATE_1 | 2026-09-27 |
| G-0009 | Which specific systems do the three Play Store reviews describe (input/player-switch desync, "c spamming" exploit, no coin refund on selling a player, coach double-fee, classic-player pricing, no control remapping, pass-target selection, goalkeeper quality)? | 3 user-generated reviews on the official listing (S-0012) | each becomes its own research question: full review set, community reports, databases, and Step 2 client data. Reviews are leads, never facts | STATE_1 | 2026-09-27 |
| G-0005 | Exact in-game terminology for the prompt's shorthand (DLL, OVR, GK, XI, prize ladder, special card, base OVR, rotation, coaching state, reset cycles, breakpoints, matchup matrix, gameplans, touch patterns, facilities, ceiling, bonus development, division, season points) | nothing yet | Step 1 sweep | STATE_1 | 2026-09-27 |
