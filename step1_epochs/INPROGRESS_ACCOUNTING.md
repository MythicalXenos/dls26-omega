# STEP 1 — ACCOUNTING OF THE 23 IN_PROGRESS REFERENCES (t69 snapshot)

Built 2026-10-17T19:45Z (session sess-20261017-001, turn 7). Source: `logs/sources_visited.json` at checkpoint 5ab3ec6, `references[status=IN_PROGRESS]`. Each row names the projections the ref was admitted for, how far the cursor actually got, and what is still owed.

Rule applied: a ref stays IN_PROGRESS until its required projections are complete or an explicit disposition is recorded. Nothing here is closed for being low value — the block is access, and each row's reopening predicate is the same sandbox allowlist change or a user-supplied capture.

| Ref | Family | Projections admitted | Cursor reached | Still owed |
| --- | --- | --- | --- | --- |
| ref-store-appstore | official-stores | version history / release notes; feature claims | chunks 0-3/6 captured (EV-172/173/175/177); 4-6 residual (older history) | chunks 4-6: older version history (pre-13.310). Low knowledge value now that the ID-locale listing carried 13.010-13.430, but not closed on that judgement — owed. |
| ref-reddit-launch-megathread | community-reddit | launch-day observations; Prize Ladder Midfield Classics; rating changes | snippet extracted; thread comments OWED | full thread comments (launch-day observations, rating changes). Blocked: reddit bot-wall. |
| ref-reddit-rating-predictions | community-reddit | community rating predictions (pre-launch, historical) | snippet extracted; thread OWED | full thread (pre-launch rating predictions — historical). Blocked. |
| ref-reddit-top2516 | community-reddit | community-revealed rating tiers | snippet extracted; thread OWED | full thread (community-revealed rating tiers). Blocked. |
| ref-web-thesoccerera-features | community-web-en | feature breakdown quoting App Store notes; update history | snippet extracted; full article OWED | full article text; snippet only. Blocked. |
| ref-web-thesoccerera-launch | community-web-en | launch claims (date CONTRADICTION noted); ratings table | snippet extracted; full article OWED | full article text; date contradiction recorded (C-R01). Blocked. |
| ref-web-fifaworldcupnews | community-web-en | update timeline claims (Jan/May/Sep 2026); feature list | snippet extracted; full article OWED | full article (Jan/May/Sep 2026 update timeline claims). Blocked. |
| ref-web-dlskits-updates | community-web-en | update list (v13.410 Cult Heroes, Summer Spotlight, Winter Reload); clan/facility details | snippet extracted; full article OWED | full article (update list, clan/facility detail). Blocked. |
| ref-web-sportsdunia-players | community-web-en | top player ratings list; stat claims | snippet extracted (contains at least one factual error: Van Dijk nationality) ; full article OWED | full article; snippet already contains at least one factual error (Van Dijk nationality), so the family is capped at Community Consensus. Blocked. |
| ref-web-sportsdunia-teams | community-web-en | best-teams opinions | snippet extracted; full article OWED | full article (opinion piece). Blocked. |
| ref-web-z2u-guide | community-web-en | player guide claims; incentive check (RMT marketplace) | snippet extracted; incentive-motive source — see notes | full article; RMT marketplace motive recorded, incentive screen active. Blocked. |
| ref-web-gamingonphone | community-web-en | game modes; DLL weekly leaderboard + gems; controls system; progression tips | snippet extracted; full article OWED | full article (game modes, controls system, progression tips) — the controls projection is the highest-value unpaid item in this group. Blocked. |
| ref-web-bluestacks | community-web-en | facilities effects (Medical/Training); DLL weekly leaderboard; economy tips | snippet extracted (page age metadata inconsistent: 2021) ; full article OWED | full article; page metadata inconsistent (2021), so build applicability is doubtful. Blocked. |
| ref-web-mwm-appstore-agg | community-web-en | app store aggregation claims (DLL global leaderboards) | snippet extracted; full page OWED | full page (store aggregation). Blocked. |
| ref-es-kotaku | community-web-es | tactics/formations; camera/controls advice; training specialization; club upgrade order | snippet extracted (ES, interpreted in research/turn1_discovery.md); full article OWED | full ES article (tactics/formations, camera/controls advice, club upgrade order) — second-highest-value unpaid item. Blocked. |
| ref-es-tuapppara | community-web-es | speed+acceleration training pairing; free progression routes (Prize Ladder/Dream Points); kit import | snippet extracted (ES); full article OWED | full ES article (training pairing, free progression routes, kit import). Blocked. |
| ref-es-mundodls | community-web-es | position roles and key attributes | snippet extracted (ES, page dated 2025-02 pre-DLS26 — build applicability limit); full article OWED | full ES article (position roles and key attributes); page dated 2025-02, pre-DLS26 — applicability must be checked. Blocked. |
| ref-tr-dlshile | community-web-tr | community cheat-claims (risk analysis only); squad-building tips (TR) | snippet extracted (TR); FULL PAGE MUST BE TREATED AS UNTRUSTED (cheat/phishing-suspect, do not execute or enter any credentials); risk record OWED | full page is UNTRUSTED (cheat content); only risk analysis and squad tips in scope, treated as untrusted evidence. Blocked. |
| ref-vi-download-com-vn | community-web-vi | Android version (13.420); Prize Ladder English League Classics; rank-up tips (Division Objectives 15-match seasons); player-release for fitness coaches claim | chunks 0-2/4 captured (EV-193/196/198); chunk 3 residual (tail) | chunk 3 (tail) only. Blocked. |
| ref-ugc-tiktok-best11 | community-ugc | creator-demonstration content index | snippet extracted (ES/EN mixed); deeper UGC sampling OWED | deeper UGC sampling (creator demonstrations). Blocked. |
| ref-support-player-stats | official-support | full-page extraction | chunks 0/4 extracted (EV-115 full stat model); comment chunks 1-3 OWED | comment chunks 1-3 (user questions under the stat article). Blocked; the article body itself is fully captured (EV-115). |
| ref-support-player-look | official-support | full-page extraction | chunk 0/4 captured (EV-206: licensing-gap comment GOLD); comment chunks 1-3 residual (low) | comment chunks 1-3 (licensing-gap user reports). Blocked; chunk 0 captured (EV-206). |
| ref-store-appstore-id | official-stores | older version history 13.100/13.110; Dream Points / Premium Season Pass notes | chunks 0-2/4 captured (EV-181/183/185): version history+privacy+IAP COMPLETE; chunk 3 residual (reviews tail) | chunks 3-4 residual after EV-181/183/185. Blocked. |

## Grouped summary
- **Official store listings (2):** the US App Store and the ID-locale App Store. Substantively captured (version history, IAP catalogue, metrics, privacy, reviews); residuals are older history chunks and the tail of the ID listing. Not a knowledge gap today; owed.
- **Official support (2):** the stat article and the player-look article, both fully captured as bodies; what remains is user *comments* under them. Comments are user-generated content, useful for licensing-gap reports but not authoritative.
- **Reddit (3):** bot-wall; every one is snippet-only. Highest blocking severity because Reddit is the main English community source type.
- **English community web (8):** snippet-only; the gamingonphone controls projection and the thesoccerera feature breakdown are the two most valuable unpaid items.
- **Spanish community (3):** snippet-only; the kotaku ES tactics/camera piece matters for the controls gap.
- **Turkish (1):** untrusted family, risk-analysis scope only.
- **Vietnamese (1):** one tail chunk only; the substantive chunks (EV-193/196/198) are captured.
- **UGC (1):** TikTok creator index — sampling depth only.

## Consequence
Of the 23, **4 are substantively complete** (store listings x2, support x2 — residuals are comments/tails), **1** is a single tail chunk, and **18 are snippet-only captures awaiting a permitted fetch**. Condition 2 therefore remains unmet principally because 18 refs cannot be finished, not because they were skipped.
