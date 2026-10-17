# research/turn1_discovery.md — Step 1 initial epoch, discovery slices DS-1/DS-2 (2026-10-10)

Session sess-bb22126f679b. All statements below are research findings with confidence
labels, NOT new rules and NOT certified game facts. Snippet-only evidence is marked;
search snippets prove only visible content (OMEGA-EVIDENCE-001).

## 1. Game identity (mission foundation)

- DLS26 = "Dream League Soccer 2026", First Touch Games (FTG), FIFPRO-licensed mobile game
  (Android: com.firsttouchgames.dls7; iOS: id1462911602). Delivered as a seasonal update of
  the existing app rather than a new listing (store listings + multiple community sources).
  Community sources date the DLS26 season update to early December 2025 (Reddit "Update
  Megathread Day 1" 2025-12-01; VI portal article 2025-12-03), with live updates through at
  least 2026-09-14 (Google Play "Updated on Sep 14, 2026").
  → CLAIM-001 (kb/claims.jsonl). CONTRADICTION recorded: thesoccerera (2026-02) claims
  "full global availability December 4, 2026"; this conflicts with Dec-2025 community
  megathreads and 2026 store update history. Both preserved (CLAIM-008, Disputed).

## 2. Competitive ranking — what actually appears to exist (MISSION-CRITICAL, OPEN)

- Official store text (Google Play / App Store, via snippets): "Compete against players from
  across the globe with Dream League Live"; "Work your way through the ranks ... compete in
  Global Leaderboards and Events for exclusive prizes".
- FTG official support (support.ftgames.com) — "What are Leaderboards?" (EV-101): "Leaderboards
  are a way to compare your performance against other players in Multiplayer (Dream League
  Live). Leaderboards reset at regular intervals (from 3-30 days) and users will receive
  prizes based on their position at the end time."
- FTG official support — "How does Dream League Live matchmaking work?" (EV-102): matching is
  based "primarily [on] their LIVE Tier ranking, their location and the availability pool";
  opponents should "generally" be same Tier; "As players progress through the Tiers in LIVE
  mode, opponents will naturally become more challenging."
- Community guides (gamingonphone 2026-01, bluestacks): Dream League Live has a leaderboard
  that "resets every week" with position-based Gem rewards. (Not necessarily contradictory
  with official 3–30 day range; different leaderboard instances may differ — UNRESOLVED.)
- Reddit (community anecdote): "Tier 5-10 is tough like Tier 1" (Oct 2026) implies a LIVE
  Tier ladder is active in the current build.
- NOT ESTABLISHED yet: precise definition of the global rank, season boundaries, eligibility,
  tie-breaks, how a rank is verified/measured externally, and whether any ranking beyond DLL
  leaderboard position + LIVE Tier (e.g. Clan leaderboards, Game Centre friend leaderboards,
  career 8-division progress) could count as "highest verifiable global competitive ranking".
  → CLAIM-002/003. Next action targets FTG support inventory + in-game screenshots from user.

## 3. Current build / events timeline (partial)

- Launch (DLS26 season): early Dec 2025 regionally (community); Kick-Off Stars (Raphinha,
  Alvarez launch cards).
- Winter Reload: Dream Stars 26 + 12th Man community vote, News System, Clan leaderboards /
  vice-captains / Clan Point boosts, Game Centre (iOS) achievements + friend leaderboards.
- Jan 2026: live-service balance updates (per fifaworldcupnews).
- May 2026: end-of-season rating adjustments (per fifaworldcupnews).
- Summer Spotlight: Dynamic Stars (upgrade with national-team performances), Fanzone
  facility (Clan bonuses + stadium discounts), World Tournament event, manager accessories,
  friend-match options, Transfer upgrades (player lock/manage), Daily Bonus, Scenario update,
  Player Recovery change ("Changed your mind?").
- Late summer: v13.410 — Cult Heroes special collection + "dozens of bug fixes" (dlskits.mobi).
- VI portal lists Android "13.420" and a Prize Ladder "English League Classics" (Berbatov,
  Essien). Reddit launch thread: Prize Ladder "Midfield Classics" (Matthäus '91 86, Valderrama
  '93 83, Rivaldo '99 86, Pires '02 84).
- Build reconciliation (13.410 vs 13.420) UNRESOLVED — claim pending.

## 4. Roster / development / economy (partial; user-plan-critical)

- Top base ratings cluster at 86 OVR (Mbappé/Haaland/Dembélé/Kane per multiple lists; lists
  disagree on ordering and contain errors — e.g. sportsdunia lists Van Dijk as Portugal).
  Special collections (Dynamic Stars, Champion, Team2025, Cult Heroes, World Cup Heroes,
  Classics, Kick-Off Stars, Dream Stars) exceed base (e.g. Dynamic Star Nico Williams 96 on
  sakibpro.com). 14,000+ player DB + upgrade simulator + squad builder at sakibpro.com.
- Training: "Coaches" develop technical/physical abilities (store text); ES Kotaku advises
  role-specialized training (forwards: shooting/control/speed; midfielders: passing/stamina/
  control; defenders: strength/tackling/positioning); tuapppara (ES) advises pairing speed +
  acceleration when developing players. Legendary Fitness item mechanics NOT yet identified.
- VI community claim (EV-105, single origin, Speculative): releasing unused players grants
  "fitness coaches" (HLV thể lực) that speed injured-player recovery and keep the transfer
  market rotating for classic players. DIRECTLY relevant to Saad's Legendary Fitness plan and
  no-coin-physio stance — verification is a top next action.
- Facilities: Stadium (match income), Medical (injury likelihood + recovery cost), Commercial,
  Training (unlocks formations per BlueStacks), Fanzone (Clan bonuses/stadium discounts).
  Economy routes: career/cups payouts, Division Objectives, Daily Challenges, Scenario,
  Prize Ladder (Dream Points per match), rewarded videos, Live Transfer market (activity-based
  refresh per BlueStacks). Store review complaints: no coin refund on player sales.

## 5. Controls / execution / competitive integrity (partial)

- Community (Google Play review text surfaced across multiple searches): 0.5–2s player-switch
  input delay desync; "c spam" and sideways-dribble exploits; pass mis-targeting; GK issues.
  Community-anecdote, Speculative, volatility Critical (build-dependent).
- ES Kotaku: camera choice (wider view to read play), control sensitivity, placed shots over
  power shots, through-ball moderation. gamingonphone: DLS26 control scheme differs from
  standard Shoot/Pass/Skill buttons (swipe/legacy DLS scheme — needs full extraction).

## 6. Risk record (community sources)

- dlshile.com (TR): "coin/diamond cheat" site asking for player ID/username and platform —
  classic credential-phishing / scam pattern. NOT evidence of any working cheat. Do not
  execute, do not enter any credentials anywhere. Treated as risk-analysis material only.
  Account-safety coaching note: never enter account/link codes on third-party sites
  (consistent with OMEGA-DEVICE-001 secret handling).
- z2u.com: real-money trading marketplace (incentive motive) — its "guide" content is
  marketing-adjacent; incentive alone proves nothing about accuracy (OMEGA-EVIDENCE-001).

## 7. Language coverage note

- EN/ES/TR/VI searches produced dedicated sources. PT ("dicas jogadores elenco") and ID
  ("tips pemain terbaik") queries surfaced only cross-language content (reddit EN, z2u, a
  TikTok discover page) — translated queries were ATTEMPTS; PT/ID community coverage is a
  recorded deficit owed in this still-open epoch. Bangla not yet triggered.

## 8. What was NOT done this turn (honesty)

- No full-page fetches (fetch_page) yet — all extraction is search-result-projection level.
- No APK/IPA acquisition or static analysis (Step 2).
- No device access (Step 3, UNASSESSED).
- No claim was promoted beyond Speculative/High-Confidence-with-conditions as recorded in
  kb/claims.jsonl; nothing here is a Confirmed game mechanic.
