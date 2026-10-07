# T125 — image search for Cult Heroes Agent/event screen

Date: 2026-10-06 Asia/Dhaka. One `functions.image_search` query and two exact follow-up `functions.web_search` queries; three returned image files were read locally and preserved.

## Image search

Exact query: `Dream League Soccer 2026 Cult Heroes Agent reward screen in-game screenshot`. `functions.image_search` returned status `success`; HTTP status is not exposed. The result metadata pointed to the subreddit root `https://www.reddit.com/r/DreamLeagueSoccer/` for the first two images, not a post permalink. The three saved files and SHA-256 values are:

1. `source_archive/t125_image_search_results/reddit_cult_heroes_agent_event_ui.jpg` — 2435d7a9d0337ca8c2e8fa6db70e24aba5ece9db8afe8b88d8fe8b2120488848. Search result title “r/DreamLeagueSoccer - Cult heroes”. Visually, the image appears to show a Portuguese-language Cult Heroes event UI. It reads: `Colete nossa seleção de jogadores especiais. Receba Agentes Heróis Cultos jogando em vários eventos!` Manual translation: “Collect our selection of special players. Receive Cult Heroes Agents by playing in various events!” It also has a green `USAR AGENTE` button (“USE AGENT”) and displays `TEMPO RESTANTE 12d 22h 48m` without an absolute date. This supports only the wording visible in one user-generated screenshot. The direct post, author, date, client version, and authenticity are unresolved; do not present it as an FTG-authored statement or current event state. It does not specify event names, thresholds, cost, or card result.
2. `source_archive/t125_image_search_results/reddit_dele_alli_card_render.png` — 560afea3ce73bd0c9ed6faa2366edc5c06d2c744c17713e33e55ac465903f7fc. Search result “Dele Alli Cult Heroes card”; visible `DREAM KITS` watermark and designed card/price layout. Classified as third-party render, not an in-game screen.
3. `source_archive/t125_image_search_results/taptap_cult_heroes_promo_banner.jpg` — 8597e44fec49ba1ab90acfe0cf6af2984ea24ba6c6c14188bac2cf485504fd00. Search result “Dream League Soccer 2026 Game Screenshot”; TapTap source `https://taptap.io/app/180521`. It is a promotional collage/banner reading “COLLECT CULT HEROES”, not an acquisition UI. Not used for mechanics.

## Parent-link checks

- Exact filename query: `"cult-heroes-v0-sci9uc0c02th1.jpeg"`. `functions.web_search` returned five unrelated results; no Reddit parent permalink identified.
- Exact UI-text query: `"Receba Agentes Heróis Cultos jogando em vários eventos"`. `functions.web_search` returned five unrelated results; no Reddit parent permalink identified.

These zero-relevance searches do not establish absence. A concrete unresolved lead is to identify the parent Reddit post/date for preview image `cult-heroes-v0-sci9uc0c02th1.jpeg`.

## Interpretation boundary

The on-screen instruction is direct visual UI content but comes from a single user-generated image-search result with no identified parent post. It suggests an Agent/event-play path in that captured screen; it does not prove a complete or current acquisition route, exact rewards, costs, thresholds, or position-lock behavior. Do not promote any poster caption or third-party card render. Position-lock remains `user-stated` and unverified.
