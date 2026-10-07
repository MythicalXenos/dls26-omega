# T119 — FTG support query (search result only)

Date: 2026-10-06 Asia/Dhaka. One retrieval execution; no linked page was fetched.

## Search execution

- Tool: `functions.web_search` (status `success`; HTTP status is not exposed by the search tool).
- Exact query: `site:support.ftgames.com/hc/en-us/articles "Cult Heroes collection" "Dream League Soccer"`
- Returned: five FTG Help Center result snippets. All five exact result URLs were already represented in `logs/sources_visited.json`; this execution discovered no new unvisited URL.

## Returned result snippets

1. **How do I backup/restore/transfer my save data?** — `https://support.ftgames.com/hc/en-us/articles/214387685-How-do-I-backup-restore-transfer-my-save-data`. For older games no longer generally available, such as Dream League Soccer (formally DLS19), backup/restore/transfer uses iCloud (iOS) or Google Play Saved Games (Android).
2. **How can I get Gems?** — `https://support.ftgames.com/hc/en-us/articles/360003914938-How-can-I-get-Gems`. Snippet lists league objectives, tournaments, Season Pass, Prize Ladder, and Dream League Live as Gem sources; quantity depends on circumstance; Gems can also be purchased. Generic and not Cult Heroes-specific.
3. **Can I change my team name?** — `https://support.ftgames.com/hc/en-us/articles/214385345-Can-I-change-my-team-name`. Search result title and related-article links only; unrelated to either question.
4. **How do I find my User ID?** — `https://support.ftgames.com/hc/en-us/articles/37082887837202-How-do-I-find-my-User-ID`. Search result title and related-article links only; unrelated to either question.
5. **Why have I been blocked from playing DLS?** — `https://support.ftgames.com/hc/en-us/articles/360008904718-Why-have-I-been-blocked-from-playing-DLS`. Generic fair-play policy snippet; unrelated to the target mechanics.

The search snippets returned no Cult Heroes-specific route, reward, cost, availability, or DLS26 position-lock information. Because the search was mixed/generic and linked pages were not fetched, it is not evidence of absence and adds no game-mechanics claim. Do not re-fetch the exact result URLs as part of this turn; they were already logged.
