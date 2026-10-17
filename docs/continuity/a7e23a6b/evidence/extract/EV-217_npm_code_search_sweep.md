# EV-217 (sweep 1/1) — UGC/TECHNICAL: npm-registry + GitHub code-search probe (cheat ecosystem on npm; leaderboard residue negative)
source: registry.npmjs.org search API + api.github.com search/code (gh api) | community-ugc + databases-tools | fetched 2026-10-11T17:31:52Z
CHANNEL NOTE: fetch_page/web_search STILL unreachable (t61-t64, 4th turn); probes via whitelist hosts registry.npmjs.org + api.github.com. Listing metadata ONLY — no package installed, no tarball downloaded (do-not-execute / do-not-install).

OPERATIVE CONTENT (observed listings):
1. npm search "dream league soccer" (2995 total hits, mostly name-collision noise: @fontsource/league-*, soccer-go, openligadb etc.). Game-scope packages:
   - `dream-league-soccer-guide` 1.0.4 — "How to find a way to obtain more coin in Dream League Soccer" (thin guide content).
   - `dream-league-soccer-latest-tool-2023` 1.8.1 — "Dream League Soccer Hack Tool Working 100% [No Ban] 2023 [Eqwt(-)]" **HACK PACKAGE**.
   - `new-dream-league-soccer-h-ack-working-2023-march` 3.1.9 — "Dream League Soccer Hack Latest Working 100% 2023 [Avnp(-)]" **HACK PACKAGE**.
   Obfuscated bracket markers "[Eqwt(-)]"/"[Avnp(-)]" + "h-ack" split-word = classic npm **supply-chain malware / phishing distribution pattern**. Installing = malware/credential-theft risk ON TOP of game-ban risk.
2. GitHub code search REST: "Season Points" + "Dream League" -> 5 hits, ALL SEO content-farm pages (hairdu/games-console, gefile.github.io generic how-to spam; keyword-stuffed Halo/Snapchat/Minecraft pages). **ZERO** game-mechanics docs, leaderboards, trackers, or data.

ASSESSMENT: (a) CLAIM-084 ecosystem EXTENDED to npm (2 new independent origins) — public DLS hack distribution exists on GitHub AND npm; hard DO-NOT-INSTALL/EXECUTE (CLAIM-075 bannable + malware/phishing risk; treat downloads as untrusted). (b) NEGATIVE FINDING logged: no Season-Points/leaderboard implementation or docs discoverable via GitHub code search — CLAIM-003/071 season-leaderboard residue (tie-breaks/intervals/eligibility/visibility) remains OPEN and unclosed by any code-hosting avenue. (c) registry "league/soccer" name collision confirmed on npm too — future searches must use exact game name.
