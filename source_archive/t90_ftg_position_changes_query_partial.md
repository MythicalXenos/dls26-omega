# T90 — FTG `position changes` search (partial) and Instagram discovery

Date: 2026-10-06 Asia/Dhaka. Ledger record time: 2026-10-05T22:55:19Z; retrieval tools do not expose per-call timestamps.

## Recovery
The opening checkout reset to `fb9a2c0`, with 260 project files untracked and upstream unset. Archive `/tmp/dls26-t90-recovery-1791240766.tar.gz`, SHA-256 `cf0207c37d5337b99aeea8396583520534696d2547b235f69d72418625697091`. Restored `origin/arena/01a1022d-dls26-omega` at `b271ea5`, tracking and repo-local identity; extracted and byte-verified 260/260 files. No loss/force-push. ISSUE-0014 occurrence #52.

## Retrievals (6 total)
1. `functions.web_search` depth 2, `site:instagram.com/p/ "@playdls" "Cult Heroes" "Dream League Soccer"`: zero result cards. This is not proof of absence or a page block.
2–6. FTG API exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=position%20changes`, chunks 0–4; each returned success. API reports 49 results across 2 pages and 7 rendered chunks for page 1. Chunks 5–6 remain unread; page 2 remains unread. Visible results mix generic/older product help. Chunk 4 includes search-result bodies for “How do I change my formation?” and “How do I change my player roles?” (section ID 7900693036561); those generic Squad UI snippets do not answer position-lock behavior or establish DLS26 applicability. No query-wide conclusion.

Resume page-1 chunkIndex 5, then 6; page 2 is separately retained as an unvisited URL. The two canonical formation/roles help pages are retained as leads only if not already visited. Ledger: 695 entries / 513 unique visited URLs / 406 unvisited leads.

## Status
The user-stated DLS26 no-position-lock claim remains unverified, and Cult Heroes availability/acquisition route/cost/rewards remain unresolved. No spending recommendation, dimension closure, or exhaustion declaration. Provenance and pending leads are in `logs/sources_visited.json`.
