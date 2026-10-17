# EV-254 — thienntdev/bot-dls (Vietnamese community DLS auto-bot): control surface, game states, ad types
**Date:** 2026-10-18T01:05Z
**Tool:** api.github.com raw pull of 23 Python source files + README/USAGE/log from thienntdev/bot-dls (a Vietnamese-developed automation/farming bot that plays DLS on BlueStacks/Nox/LDPlayer/GameLoop via ADB + OpenCV + ML).
**Origin:** Community tool for automating resource farming (gold/coins and diamonds). The bot uses screen-capture + template-matching rather than reading game memory, so it only reveals information visible in the HUD/UI — but that in itself is a rich signal about what states/buttons/menus DLS26 exposes.

**Authenticity limits:** Third-party bot; not official. Region layout assumes 1920×1080 landscape (BlueStacks default) and Vietnamese/English UI labels. Some "config" numbers (15000 gold, 400 diamond targets) are the author's defaults, not in-game prices. State machine enumerations reflect what the bot author could detect in screenshots; if there are additional game states the bot does not branch to, those are invisible here. Nevertheless this corroborates several control-surface claims with high precision.

## Confirmed control layout
**On-screen action buttons:**
- `A` = PASS (chuyền bóng)
- `B` = SHOOT (sút bóng)
- `C` = SKILL (kỹ thuật/skill moves)
- Virtual buttons for SPRINT (chạy nhanh), TACKLE (xoạc bóng), SWITCH (đổi cầu thủ) are also recognized.
- Movement is a 360° virtual joystick (the bot generates mouse movements at BlueStacks level).
This refines CLAIM-026/D-010 ("three virtual buttons A/B/C + sprint") by naming the A/B/C mapping explicitly (A=pass, B=shoot, C=skill) — earlier evidence had listed them generically.

## Game state machine (as observed by the bot)
Top-level UI states:
- `MAIN_MENU`, `CAREER_MODE`, `LIVE_MODE`
- `MATCH_LOADING`, `MATCH_PLAYING`, `MATCH_PAUSED`, `MATCH_END`
In-match set-piece/special states:
- `PENALTY_KICK`, `CORNER_KICK`, `THROW_IN`, `GOAL_KICK`, `KICKOFF`
- `FREE_KICK`, `INDIRECT_FREE_KICK` (from special_situations.py)
Goal events:
- `GOAL_SCORED`, `GOAL_CONCEDED`
In-match AI play contexts:
- `ATTACKING`, `DEFENDING`, `COUNTER_ATTACK`

## Ad types and ad UI geometry
Three ad classes are handled, at specific screen coordinates in 1920×1080:
- `reward_ad` (rewarded ad, center-screen region 400,200–1520,800, no skip available, expected reward = coins OR diamonds)
- `interstitial_ad` (full-screen, no skip, no reward)
- `skip_ad` (skippable interstitial, skip button near top-right at ~1750,100, appears after ~5s wait)
This corroborates CLAIM-115/136 (rewarded + interstitial coexist) and adds a third skippable-interstitial class; rewards from ads can be coins OR diamonds (diamonds ≈ gems).

## HUD elements detected by CV
- Two HUD indicator templates (filled / hollow) — stamina/boost indicator icons (from HUD templates `hud_filled.png`, `hud_hollow.png`).
- Team colour detection via jersey sampling (own / opponent / own GK / opponent GK) at relative coordinates in the kick-off circle.
- Goals are white posts detected by HSV mask.
- Score region at ~(50,800)-(100,1120) — score read via OCR.
- Ball detection via `ball.png` template.
- Player detection via a set of `players/*.png` templates plus colour-based jersey classification.

## Farming targets
- Default config targets 15,000 gold / 400 diamonds per account before switching to next emulator. These are author defaults, not in-game caps — do not take as game-economy numbers. Multi-emulator support (>=3 simultaneous instances).
- Auto-restart after 5 minutes, max 4 hours daily play, 30-minute break interval.

## Career vs Live mode
Bot explicitly switches between CAREER_MODE and LIVE_MODE as two separate top-level game modes — confirms the PvE-career (offline/event) vs PvP-online split described in CLAIM-012/017.

## Match action vocabulary (what the bot can press)
Attack options: MOVE, PASS, SHOOT, SKILL
Defence options: MOVE, TACKLE, SWITCH_PLAYER
Set pieces: WAIT + appropriate kick/throw
Cooldowns: e.g. tackle cooldown ≈ 500ms.

## Resolution / performance
- Default 1920×1080 at 30 FPS; ADB input mode recommended for GameLoop.

## Covers
CLAIM-150 (A=pass B=shoot C=skill button mapping), CLAIM-151 (game state machine / set-piece list), CLAIM-152 (ad types include rewarded/interstitial/skip; rewards can be coins or gems), CLAIM-153 (control-surface: 360° joystick + sprint/tackle/switch), CLAIM-026 (refine button mapping), CLAIM-115 (ad-network/model corroboration), CLAIM-012 (career vs live split), CLAIM-017 (multiplayer/online split context).
