# Knowledge base — current claims

**Status:** Preliminary DLS26 source captures are staged, but `STATE_0_SETUP` remains incomplete because the verbatim prompt capture is unresolved (`ISSUE-0001`, `ISSUE-0004`). Do not treat these files as evidence that the Step 1 transition or sweep is complete. No topic is exhausted and no claim has reached High Confidence or Confirmed. Entries are source-bounded records of what a source stated, not blanket confirmation of game behavior. User reports remain separately labeled `user-stated`.

## Current version and live listing

### U.S. Apple App Store version-history entry
- **Claim:** On retrieval, the U.S. Apple App Store page for Dream League Soccer 2026 displayed version 13.430 dated Sep 16 and prior version 13.420 dated Sep 1. This claim is strictly about the displayed U.S. storefront history; it does not establish that every Android/iOS region or installed client is on that version.
- **Evidence:** Direct `functions.fetch_page` retrievals `page-001-apple-us-dls-store` and `page-013-apple-de-listing` (six chunks each), captured 2026-10-02; U.S. and German Apple version histories both show 13.430 dated Sep 16 and 13.420 dated Sep 1. URLs: https://apps.apple.com/us/app/dream-league-soccer-2026/id1462911602 and https://apps.apple.com/de/app/dream-league-soccer-2026/id1462911602. These regional storefronts share the developer/listing origin and are not counted as two independent origins.
- **Confidence:** Speculative (one storefront source; broader current-version and origin checks remain incomplete).
- **Volatility:** Critical. Patch-triggered dimension observed from successive version entries; event-triggered dimension not yet established. Re-tier after the volatility model is built.
- **Checkable origin:** Apple U.S. App Store page as retrieved. This is direct evidence of what the listing displayed, not direct evidence of all client builds.
- **Independent-source dates/origins:** The U.S. and German Apple listings share the same App Store/developer-supplied product page; they are regional copies of one origin, not two independent confirmations. Google Play US/Bangladesh page text did not expose an Android version. Independent origin for any third-party catalogue claim remains to be established.
- **Status:** The current Android build and regional-store versions remain an open gap. See `knowledge/gaps.md` and source-ledger entries `discovery-003`, `discovery-006`, `discovery-007`, `discovery-008`, `discovery-011`, `page-001-apple-us-dls-store`, `page-002-google-play-us-dls`, `page-012-googleplay-bd-listing`, and `page-013-apple-de-listing`.

### Cult Heroes storefront event lead
- **Claim:** The U.S. Google Play listing retrieved on 2026-10-02 contained a Cult Heroes event link whose listing text says “Ends on 10/14”; the year is not shown in the returned text. The U.S. Apple App Store page also displayed a Cult Heroes “HAPPENING NOW” event card and stated the collection was available with boosted attributes.
- **Evidence:** Direct `functions.fetch_page` text from Google Play U.S. listing `page-002-google-play-us-dls` and event detail `page-009-googleplay-cult-heroes-event`; Apple U.S. app page `page-001-apple-us-dls-store` and event detail `page-010-apple-cult-heroes-event`; Google Play Bangladesh page `page-012-googleplay-bd-listing`. All were fetched on 2026-10-02. Google Play event detail states “Ends on 10/14” and calls the event limited-time; year is not displayed. Apple labels it “HAPPENING NOW / LIVE EVENT” and says the players have boosted attributes.
- **Confidence:** Speculative (storefront-level event evidence; exact in-game availability/deadline and year are not confirmed in-game).
- **Volatility:** Critical; patch/event-triggered dimensions require the model.
- **Checkable origin:** Direct storefront event text. No in-game observation or resource/cost data.
- **Status:** Time-sensitive lead. Preserve “10/14” exactly without supplying a year; verify the event-detail page and region immediately in the next research block. Do not make an acquisition recommendation from this alone.

## FTG help-center claims — single-source and version applicability unresolved

### Save/profile transfer article
- **Source assertion:** FTG's help article says one DLS account per player; identifies “Manage Devices” and “Link Profile” in Options > Advanced; describes Google/Apple sign-in transfer and a code-based transfer from an old device; code generation is subject to a device limit, cannot be used on the generating device, and requires access to the device holding the profile; signing out of Google/Apple unlinks the profile and may expose it to loss on uninstall/device change.
- **Evidence:** Article page fetched in full as one chunk on 2026-10-02 (`page-003-ftg-save-data-transfer`); search-result page-age metadata is 2024-12-06. URL: https://support.ftgames.com/hc/en-us/articles/4413273241873-How-is-save-data-stored-and-transferred-in-DLS
- **Confidence:** Speculative (one FTG help article; current applicability and independent corroboration not established).
- **Volatility:** Critical until the change model is built; patch-triggered status not yet tested against historical revisions, event-triggered status unknown.
- **Checkable origin:** FTG's published support article, directly fetched. The origin establishes what FTG documents, not whether every implementation detail matches the current client.
- **Status:** Current Link Profile requirements remain unpromoted. The user prompt's Link Profile statements are not evidence; the article wording is the tool-origin evidence. Follow linked continuity, sign-in, device and account-security sources.

### Player-stat help article
- **Source assertion:** FTG's qualitative help article describes SPE (Speed), ACC (Acceleration), STA (Stamina), CON (Ball Control), STR (Strength), TAC (Tackling), PAS (Passing), SHO (Shooting), GKH (Keeper Handling), GKR (Keeper Reactions/Shot stopping), and ENERGY. It says these affect running speed, acceleration to top speed, energy depletion/halftime boost, dribbling/touch and skills, collisions/stumbling, tackles, pass accuracy, shot accuracy/height/assist, keeper handling/reactions, and performance as energy declines. The article also cautions that DLS is not intended as a full/accurate soccer simulation and mentions unpredictability.
- **Evidence:** Full four-chunk page retrieved 2026-10-02 (`page-004-ftg-stat-mechanics`). Search-result page-age metadata is 2021-04-13. URL: https://support.ftgames.com/hc/en-us/articles/360019166777-How-do-the-various-player-stats-in-DLS-affect-gameplay
- **Confidence:** Speculative (single, older source; current build applicability and in-game/code corroboration unverified).
- **Volatility:** Critical pending an observed model; each mechanic may need a separate volatility assignment as evidence develops.
- **Checkable origin:** FTG support article text. No code extraction or reproduction has occurred.
- **Status:** Do not use for high-stakes player or coaching recommendations until current-version evidence, connected source coverage and the Skeptic gate are complete. Public comments are user-generated reports, not corroboration; they remain to be exhaustively screened and translated where informative.

## Official store description — publisher claims, not yet confirmed mechanics

- **Source assertion:** The Apple U.S. and Google Play listings describe modes/features such as Dream League Live, career progression, facilities, Agents, Scouts, Coaches, Seasons/events, scenarios, Dream Draft and Clans; the U.S. Apple page also gives an English-plus-14 language list and store-specific purchase examples. These are attributed to the developer's listing and not all have been checked in-game.
- **Evidence:** `page-001-apple-us-dls-store` and `page-002-google-play-us-dls`; exact page output exists in tool results but complete raw capture is not yet in the repo.
- **Confidence:** Speculative for each underlying current mechanic; the pages directly establish only the content of the listings.
- **Volatility:** Critical pending model; patch-triggered likely but not yet calibrated, event-triggered unknown.
- **Checkable origin:** Two official store pages, but independent origin between their product statements is not yet documented.
- **Status:** Use as a taxonomy of leads, not as the settled game taxonomy. Resolve all prompt shorthand into exact terms separately.

## User-stated report pending research

### Position locking
- **Report:** The user states that DLS26 has no position locking and that players can be deployed in any position.
- **Evidence label:** `user-stated` (received 2026-10-02; prompt). Not independently verified.
- **Confidence:** Speculative (user-stated only; verification owed).
- **Volatility:** Critical (no observed history yet; conservative default).
- **Origin:** User's first-session prompt, section “POSITION LOCKING — STATED BY ME, VERIFICATION OWED BY YOU.” This is direct evidence of what the user reported, not direct evidence of game behavior.
- **Next action:** Verify through DLS26-specific sources and in-game documentation/data if reachable; investigate all positions and any penalties without assuming the report is true. If findings conflict, preserve both and run the Conflict Protocol.

## Research topics

All gameplay systems, official terminology, current patch, modes, economy, progression/reward tracks, player ratings/development, match behavior, controls, formations/positioning, technical data, official account/linking documentation, career and online modes, events, tools/databases, community/language sources, and FTG history remain open. Expand this list as sources expose further topics; it is not an exhaustive scope boundary. No exhaustion declaration exists.

## Current version and live listings — 2026-10-03 re-check (STATE_1 sweep block)

### Google Play U.S. listing — update date and feature surface
- **Claim:** On 2026-10-03 the Google Play U.S. listing for Dream League Soccer 2026 displayed "Updated on Sep 14, 2026"; rating 4.5, 15M reviews, 100M+ downloads; "#10 top free sports"; first-party feature list naming 4,000+ FIFPRO players, Classic greats, 8 divisions, 10+ cup competitions, Stadium/Medical/Commercial/Training facilities, the Clan system, Agents and Scouts, Coaches, kit/logo import, regular seasons and events, Dream League Live with Global Leaderboards and Events, daily scenarios, and Dream Draft.
- **Evidence:** Direct page-render fetch 2026-10-03 (`page-032-play-us-listing-recheck`, chunk 0/2), URL https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en_US.
- **Confidence:** Speculative (single storefront origin; the feature list is first-party store copy, not verified in-game).
- **Volatility:** volatility-Critical until the model is built; patch-triggered dimension evident from the update date.
- **Checkable origin:** the storefront page as retrieved (direct evidence of what the listing displayed).
- **Status:** Replaces the earlier note that the Play page "did not expose a version" — it still does not expose a version string, but it does expose an update date. Android build number remains an open gap.

### Storefront promo windows — "Ends on 10/14", "Play Fest starts on October 13"
- **Claim:** The Play U.S. listing text carries a special-event banner reading "Ends on 10/14" and a "Play Fest starts on October 13" item, inside a "late summer update" note that also says the new "Cult Heroes" collection is "coming soon". The year is not shown in the promo text itself; the listing's own "Updated on Sep 14, 2026" date is the dating anchor.
- **Evidence:** discovery-032 (web_search depth 2, 2026-10-03) surfaced the banner text with result pageAge 2026-09-14; page-032 (direct fetch, same day, chunk 0) confirmed the Sep 14, 2026 update date but did not repeat the banner in chunk 0. Same origin (Play storefront listing) for both readings.
- **Confidence:** Speculative (one origin; partial corroboration between snippet and page; no in-game timer seen).
- **Volatility:** volatility-Critical (event windows).
- **Checkable origin:** storefront listing text. **Interpretation caution:** a storefront "special event" banner is not automatically the in-game event window; treat as a lead, not a game fact.
- **Status:** Queue-Critical. Needs in-game timer verification (consolidated ask) or an FTG first-party statement. Do not gate any spend on this yet.

### Third-party update narratives (no weighting yet)
- **dlskits.mobi** (pageAge 2026-08-28): claims 2026 brought ongoing updates — "Summer Spotlight" (World Tournament format; Clan interactions/emoji reactions) and "Winter Reload" (transfer-window team data, Dream Stars 26 with a 12th Man community vote, News System, Clan leaderboards/vice-captains/Clan Point boosts, UI/SFX), plus unlimited special players and Turkish and Arabic commentary. **Incentive screen owed (content/SEO site).** Speculative; not used.
- **thesoccerera.com** (two articles): feature/launch narrative (Clan as headline, 8 divisions, FIFPRO 4,000+, soundtrack names, top-rated list headlined by Dembele 86) with an internally inconsistent publication date and a "December 4, 2026" availability claim. **Incentive screen owed (content/SEO site).** Speculative; logged as a conflict candidate for a later Conflict Protocol pass.
- **r/DreamLeagueSoccer megathread 1rf90a7** (mid-season update): user-reported rating changes (e.g. Kane and Haaland retained, Foden +1, Semenyo +2, DiMarco to 84, Bremer +1, vdV −1); user-generated, Speculative, single author per claim, for later player-pool verification. One comment reports being blocked from updating with an "event is now available" message — matches the earlier FTG support lead.

### Cult Heroes collection — database index (SakibPro), 2026-10-03
- **Claim:** SakibPro's Cult Heroes index page lists **12** player records, server-rendered, with base OVR, position, nation and player id, stating "12 of 12 Players Found": Aubameyang CF(GA) 85 / 28331; Dybala SS(AR) 85 / 28333; de Gea GK(ES) 85 / 28324; David Luiz CB(BR) 84 / 28325; Insigne LW(IT) 84 / 28328; Isco AM(ES) 84 / 28327; Otamendi CB(AR) 84 / 28334; Ziyech RW(MA) 84 / 28332; Ander Herrera CM(ES) 83 / 28329; Blind CB(NL) 83 / 28326; Shaqiri AM(CH) 83 / 28330; Vozinha GK(CV) 83 / 28658. The page also carries a FAQ claim that special-edition cards can be raised "up to +10 over their current base rating" with team training coaches (Fitness and Technical) into "maxed-out black cards".
- **Evidence:** Direct page-render fetch 2026-10-03 (`page-033-sakibpro-cult-heroes-index`), https://sakibpro.com/players/cult-heroes/ — complete in one chunk; the prior session's "loading placeholder" issue is specific to other SakibPro routes, not this index.
- **Confidence:** Speculative (one database origin; nothing promoted; the OVR/position values are the site's own catalog, not yet cross-checked against a second database, card art, or in-game text). The coach "+10" FAQ line is Speculative and incentive-screen-owed.
- **Volatility:** volatility-Critical while the collection is live; patch/event-triggered.
- **Checkable origin:** the retrieved index page itself; player ids give a stable route to per-player pages for stat-octet extraction.
- **Status:** Directly relevant to the user's live-event/prize-ladder context (one special card already owned, career grinding). Open items: (a) reconcile 12-vs-17 counts before any collection-completeness claim; (b) harvest per-player pages for the full stat octets; (c) verify in-game whether the collection is live today and its exact window.

### Cult Heroes — per-card records (SakibPro, fetched 2026-10-03)
Stat fields are the site's own octet labels (Speed, Acceleration, Strength, Control, Passing, Tackling, Stamina, Shooting). Both cards below are flagged **"⚠️ ESTIMATED"** for base OVR by the source itself.
- **Paulo Dybala — Cult Heroes 2020, id 28333.** SS · Argentina · Free Agent · 177 cm / 75 kg · left foot · born 1993-11-15 (age 32). SPE 81 / ACC 90 / STR 62 / CON 92 / PAS 90 / TAC 49 / STA 80 / SHO 90 = **634**. Base OVR **85** (site-estimated) · acquisition: **Cult Heroes Agent** · site-claimed max **95** (+10 via coaches). Evidence: `page-034-sakibpro-dybala-28333`. Confidence: Speculative (one database origin; values are the catalog's). Volatility: volatility-Critical while the collection is live.
- **Isco ("Francisco Alarcón") — Cult Heroes 2017, id 28327.** AM · Spain · Free Agent · 176 cm / 79 kg · right foot · born 1992-04-21 (age 34). SPE 81 / ACC 87 / STR 65 / CON 93 / PAS 88 / TAC 53 / STA 79 / SHO 81 = **627**. Base OVR **84** (site-estimated) · acquisition: **Cult Heroes Agent** · site-claimed max **94**. Evidence: `page-035-sakibpro-alarcon-28327`; **cross-check: CON 93 / PAS 88 / STA 79 match the prior session's independently captured values exactly**. Confidence: Speculative.
- **Collection structure note:** each card carries an era label ("Cult Heroes 2020", "Cult Heroes 2017"), and acquisition is stated as the **Cult Heroes Agent** rather than direct purchase. The "+10 maximum via coaches" line is the database's own claim and is **not yet independently verified** (coach mechanics are a Step 1 taxonomy dimension).
- **Open conflict (unchanged):** 12 records in this index vs the prior session's 17-card note — not resolved; both Speculative.

### Cult Heroes — per-card records, batch 2 (SakibPro, fetched 2026-10-03)
- **David de Gea — Cult Heroes 2018, id 28324.** GK · Spain · Free Agent · 192 cm / 76 kg · right foot · born 1990-11-07 (age 35). **GK stat set differs from outfield:** Speed 62 / Acc 60 / Str 56 / Control 57 / Passing 60 / Tackling 43 / **Reactions (GKR) 85** / **Handling (GKH) 80** = 503. Base OVR **85** (site-estimated) · site-claimed max **95** · acquisition route: see the route conflict below. Evidence: `page-036-sakibpro-degea-28324`.
- **Pierre-Emerick Aubameyang — Cult Heroes 2018, id 28331.** CF · Gabon · Free Agent · 187 cm / 80 kg · right foot · born 1989-06-18 (age 37). SPE 93 / ACC 92 / STR 77 / CON 85 / PAS 79 / TAC 34 / STA 81 / SHO 94 = **635**. Base OVR **85** (site-estimated) · site-claimed max **95**. Evidence: `page-037-sakibpro-aubameyang-28331`.
- **CONFLICT (open, same-source contradiction): how Cult Heroes cards are acquired.** The per-card data tables and FAQ on SakibPro state "obtained exclusively through the **Cult Heroes Agent**"; the editorial text on the Aubameyang page states the cards "will arrive through the upcoming **Season Pass** track" and mentions early leak lists. One source, two incompatible routes ⇒ Verification Protocol step 4 (internal consistency) fails on this claim, and both routes are capped at Speculative. Conflict Protocol opened; scope = the acquisition route and everything connected (event delivery mechanics, Season Pass, Agents). Resolution routes queued: FTG first-party channels (Play/Apple event cards, in-app News), an in-game check by the user (cheapest decisive evidence), and a second database.
- **Position-dependent stat set (new structural finding):** the database's stat octet for a GK is Speed / Acc / Str / Control / Passing / Tackling / **Reactions** / **Handling**, with no Stamina or Shooting fields — consistent with FTG's help-center naming (GKH, GKR). Confidence: Speculative (one database origin + one FTG help article, same-era applicability unverified).

### Cult Heroes — per-card records, batch 3 (SakibPro, fetched 2026-10-03)
All base OVRs are site-flagged "⚠️ ESTIMATED"; acquisition shown as "Cult Heroes Agent" in every data table (see the open acquisition-route conflict); all six are Free Agents.
- **Lorenzo Insigne — Cult Heroes 2021, id 28328.** LW · Italy · 163 cm / 60 kg · right foot · born 1991-06-04 (35). SPE 90 / ACC 94 / STR 54 / CON 90 / PAS 86 / TAC 40 / STA 83 / SHO 87 = **624**. OVR 84 (est.) · site max 94.
- **David Luiz — Cult Heroes 2017, id 28325.** CB · Brazil · 189 cm / 84 kg · right foot · born 1987-04-22 (39). SPE 78 / ACC 74 / STR 85 / CON 80 / PAS 80 / TAC 89 / STA 82 / SHO 67 = **635**. OVR 84 · max 94.
- **Nicolás Otamendi — Cult Heroes 2018, id 28334.** CB · Argentina · 183 cm / 75 kg · right foot · born 1988-02-12 (38). SPE 75 / ACC 73 / STR 89 / CON 80 / PAS 80 / TAC 93 / STA 83 / SHO 58 = **631**. OVR 84 · max 94.
- **Hakim Ziyech — Cult Heroes 2019, id 28332.** RW · Morocco · 180 cm / 74 kg · left foot · born 1993-03-19 (33). SPE 83 / ACC 85 / STR 61 / CON 87 / PAS 90 / TAC 58 / STA 84 / SHO 83 = **631**. OVR 84 · max 94.
- **Ander Herrera — Cult Heroes 2017, id 28329.** CM · Spain · 182 cm / 71 kg · right foot · born 1989-08-14 (37). SPE 74 / ACC 75 / STR 73 / CON 86 / PAS 86 / TAC 82 / STA 91 / SHO 73 = **640**. OVR 83 · max 93.
- **Daley Blind — Cult Heroes 2019, id 28326.** CB · Netherlands · 180 cm / 72 kg · left foot · born 1990-03-09 (36). SPE 75 / ACC 72 / STR 81 / CON 81 / PAS 82 / TAC 87 / STA 83 / SHO 67 = **628**. OVR 83 · max 93.
- **Player-pool signal (to verify, not yet usable):** linked card values visible on these pages imply card-type OVR ranges — dynamicstar up to **96** (Nico Williams 27509), world-winners **87** (Lamine Yamal 27845), champion **88** (Cristiano Ronaldo 25842), team2025 **87** (Dembélé 27136, Mbappé 27137) / **86** (Kane 27199), classic **86** (Cannavaro 26842, Matthäus 27201), normal **86** (Olise 18158). Single database; the OVR threshold for the watchlist/candidate pool is NOT set from these (Step 1 research determines it).

### Cult Heroes — final card and collection structure (2026-10-03, Turn 6)
- **Vozinha (Josimar José Évora Dias) — Cult Heroes 2026, id 28658** (12th and final index record). GK · Cape Verde · Free Agent · 189 cm / 75 kg · right foot · born 1986-06-03 (40). GK set: SPE 54 / ACC 47 / STR 62 / CON 54 / PAS 55 / TAC 43 / GKR 81 / GKH 81 = 477. OVR 83 (site-estimated) · site max 93. dlskiturl labels him "(12th Man)", matching the community-vote mechanic seen in a Play review ("12th Man – the DLS community has voted, and we've added this extra superstar to the collection").
- **Collection = 12 cards** (11 heroes + community-voted 12th Man), consistent across SakibPro's index, its per-card pages and dlskiturl's table. The earlier "17" figure from the prior session remains unexplained and is queued for re-read in the archived session before any final count claim.
- **Acquisition route — conflict RESOLVING (was: Agent vs Season Pass):** the mechanism is now clear at Speculative-to-converging confidence: **Cult Hero Agents** are collected from the **Season Pass** (1 free + 1 paid per season), **Online Events** (in the Dream League Live section) and the **Market**; SakibPro's article adds **Dream Draft**; agents are opened in **Transfer → Event section**, and the player signed is **random**. Corroborated across SakibPro's article and data tables, the dlskiturl article, a Reddit user summary ("12 players, using special agent to get them, and 3 season pass"), and the FTG TikTok caption ("collecting Cult Hero Agents, available in Events, Drafts and the Season Pass" — first-party, partial capture).
- **Event window (strengthened, still not in-game-confirmed):** dlskiturl states the event **commenced 16 September 2026** — matching Apple's 13.430 build dated Sep 16 and the Play listing's Sep 14 "coming soon" copy. The storefront banner "Ends on 10/14" then reads naturally as **14 October** of the same year; still a storefront lead, not a game fact. In-game timer remains the decisive evidence.
- **Smaller claims logged, unverified (Speculative; single third-party source unless noted):** "15 agents per guaranteed special player" (Reddit user); "3 Season Passes × 2 heroes = 6; Online Events 3; Dream Draft up to 3 each" (SakibPro article); "upgrading needs gems via special trainers; max only one player" (dlskiturl); 2026 event sequence TotS 2025 (green) → Dream Stars 2026 (pink) → Dynamic Stars → World Heroes → Cult Heroes (dlskiturl).

### Card-collection map (SakibPro indexes, fetched 2026-10-03 — one database origin, Speculative)
Index pages are server-rendered and state a verified-record count each; all carry the same boilerplate FAQ claiming special cards can be raised "+10 over base" with team training coaches.
| Collection | Records (as stated) | Top base OVR seen | Notes |
|---|---|---|---|
| Cult Heroes | 12 | 85 (de Gea, Dybala, Aubameyang) | Live event; 11 heroes + 12th Man (Vozinha) |
| Dynamic Star | 40 | 96 (Nico Williams, linked card) | Paginated; 12/page |
| Classic | 34 | 86 | Includes ladder classics (Essien 26838, Cannavaro 26842…) |
| Champion | 12 | 88 (Messi 25841, Ronaldo 25842) | |
| World Winners | 8 | 87 (Yamal 27845, Rodri 27843) | |
| Team 2025 / normal / season-pass | not yet counted | 87 / 86 seen | Index pages queued |

### Cult Heroes — "100% Official" guide article (SakibPro, dated 2026-08-21; fetched 2026-10-03)
- **Cross-surface consistency:** the article's tables carry **decimal** stat values; the per-card pages round them down. E.g. Aubameyang SPE 93.0 / ACC 92.0 / SHO 94.0; Dybala CON 92.9 / PAS 90.9 / SHO 90.9; Otamendi TAC 93.9 / STR 89.9; Insigne ACC 94.9; Vozinha GKR 81.4. Every per-card integer captured earlier is the floor of these values — same-origin consistency (one source, two surfaces), which is corroboration *within* an origin, not independence.
- **Unlock distribution (article claim):** 3 Season Passes × 2 heroes (1 free + 1 paid each) = 6; Online Events = 3; Dream Draft (1 free + 2 paid) with up to 3 each; together the 12-card collection. A separate "Season Pass cards" roster (6 cards) is also claimed.
- **English League Classics ladder preview (article claim, full stats):** Petit DM 84 [1999] (79/77/90/72/84/85/81/82), Andy Cole CF 84 [1994] (88/88/85/92/80/30/83/79), Essien DM 84 [2006] (77/78/91/75/82/86/81/83), Berbatov CF 84 [2011] (79/78/76/92/85/39/91/85). Order here is SPE/ACC/STA/SHO/STR/TAC/CON/PAS as printed.
- **Open conflict (new):** Essien appears as **84** in the ladder preview but **85** in the Classic index (id 26838); and this 4-card ladder set differs from the prior session's sheet set (Souness 25089, Crespo 27095, Trezeguet 26837, Cole 27096, Essien 26838, Petit 27203). Unresolved; the in-game ladder screen is the decisive evidence.
- **Timeline claim:** the article (Aug 21) says the World Winners event was finishing that day, with Cult Heroes to follow — consistent with the 16 Sep 2026 event start found elsewhere.

---

# KB structure (from 2026-10-03)

Live claims are held in `knowledge/knowledge_base.md` (this file) plus the topic files under `knowledge/topics/`. The topic files were imported on 2026-10-03 from prior session `arena/01a0e3cd` (frozen copies under `prior_sessions/`); their internal references (S-####, R-####, G-####) point into that session's archived ledger and logs. Historical promotion log: `knowledge/claim_register.md`.

## Merge notes — reconciliations between this session's research and the imported topics (2026-10-03)
1. **The "17 Cult Heroes" question (ISSUE-0009) is RESOLVED — no conflict.** The 17 was the total of a roster-update listing: **12 Cult Heroes + 4 ladder Classics (Essien, Cole, Petit, Berbatov) + 1 Season Pass card (João Pedro 28356, CF 82)**. The collection itself is **12**. Source: `knowledge/topics/prize_ladder_and_current_events.md` (§ S-0019) and the archived handoff (turn 59).
2. **Essien OVR conflict (84 vs 85) RESOLVED.** The ladder four are **Essien 26838 DM 85 · Cole 27096 CF 84 · Petit 27203 DM 84 · Berbatov 27675 CF 84** (IDs and labels from the archived census, dlsinside-extracted). SakibPro's guide article printed all four at 84 because **SakibPro's OVRs are its own computed estimates and run −1 on some cards** (that session's G-0083; the site itself flags OVRs "⚠️ ESTIMATED"). Rule adopted for this branch: **structure/stat values from a database = data; database OVR labels = estimates; extracted or in-game OVR = ground truth.**
3. **Cult Heroes acquisition route — conflict RESOLVING, now four-source.** The imported topics independently carried the same mechanism (Cult Hero Agents from Season Pass / Online Events / Dream Draft / Market, signed via Transfer → Event). Corroboration is now broad but **independence is still not documented** (two sources are guide sites that may share an origin; the TikTok caption is first-party but only partially captured) — so it stays Speculative pending a full first-party capture or the user's in-game glance.
4. **Ladder mechanics — imported topics carry substantially more than this session found.** Key imported facts to read before planning (`knowledge/topics/prize_ladder*.md`): milestone order **62,500 Berbatov → 115,000 Essien → 175,000 Cole → 250,000 Petit** (mapping unconfirmed; one anomaly suggests Cole could be first); milestone rewards include coins, gems, coaches and **special agents**; **DLS Live PvP pays significantly higher Dream Points than Career**; ladder launch **6–7 Sep 2026** (FTG's own TikTok announcement); the 90-day ladder cycle vs the 28-day Cult Heroes event still separates the two "10/14" readings (G-0040) — the in-game timer settles it.
5. **Cult Heroes year-stamp conflict (imported, still open):** Aubameyang's card header reads "Cult Heroes 2018" while the same site's article table reads [2017]. Unresolved, intra-source.
6. **Do not re-derive:** the imported topic files already contain the classic census (34 records, IDs, year stamps 34/34), the 12-family card-type taxonomy, currency/IAP inventory, coaching mechanics and gap list. They are the starting point for those topics, not a blank slate.

### Taxonomy-gate outputs (2026-10-03, Turn 9)
- **FTG corporate site is not a DLS26 news surface** (direct fetch of `www.ftgames.com` root: product tiles only — DLS, Score! Hero, Ultimate Clash Soccer, Score Match — no DLS26 news, notes or event copy). Official DLS26 communications live on the storefronts and FTG's social channels. Further official leads queued: `ftgames.com/games`, `support.ftgames.com` index, @firsttouchgames (X), @playdls (IG), facebook.com/dreamleaguesoccer, TikTok.
- **Season Pass card index: 1 record — João Pedro CF 82, id 28356** (SakibPro). This matches the archived prior-session record exactly (João Pedro 28356, CF 82), validating the imported KB on that point. Same-source discrepancy recorded: the site's own events article claims **6** Season Pass cards, its index catalogues **1** — open, not resolved.
- **Taxonomy gate ledger created:** `knowledge/taxonomy_gate.md` — per-dimension sourced/open status for all six dimensions, with the thinnest coverage identified (dimension 4, in-match conditions) and the cheapest user-settable checks listed (coaching screen, ladder screen, currency balances).

### Official support surface mapped (2026-10-03, Turn 10)
- **FTG's DLS FAQ section lists 30 articles**, all first-party, canonical URLs recorded in the ledger (`page-055-ftg-dls-faq-section`). This is the official backlog's spine. The nine most mechanism-relevant, none yet fetched in this branch: **What is the Season Pass?** · **What is the Prize Ladder?** · **What are Dream Point Boosts?** · **What are Clans?** · **How does game difficulty work?** · **How do I obtain more players?** · **How do I earn coins in the app?** · **Is it possible to earn free coins?** · **How does Dream League Live matchmaking work?** (plus the stat-mechanics article already fetched in a prior session, and "Why can't I update the app?" — the archived sweep's first open result). Prior corpus already shows this surface is stale-ish in places (e.g. 2021-era page ages) — every article is version-checked on fetch.
- **Card-collection map, Team of 2025 = 11 records** (SakibPro, matches the imported KB exactly — second independent validation of the import): Kane 87 CF · Mbappé 87 CF · Dembélé 87 RW · Donnarumma 86 GK · Hakimi 86 RB · Yamal 86 RW · Salah 86 RW · Pedri 86 CM · Gabriel 85 CB · N. Mendes 85 LB · Vitinha 85 CM.

### Dimension 4 leads — energy, injuries, recovery (Speculative, single stale vendor source)
- The bluestacks guide (pageAge 2021, DLS-2020-era URL; emulator-vendor content marketing, so incentive present and version applicability unverified) names a third development pillar alongside players and coaches: **Physios** — hired with **coins**, they recover energy and heal injuries, with **Common** restoring a small amount and **Legendary** fully restoring energy and healing all active injuries; the **Medical Centre** reduces injury chance and recovery cost; the **Training Centre** unlocks formations and boosts player form. It also independently lists coach categories as **Technical / Fitness / Goalkeeping / Special**, weakly corroborating the imported four-coach-type model (same caveats: stale, incentive, capped at Speculative).
- A second guide claims **stamina depletion is more aggressive than in previous versions** and references "expensive energy recovery items" — content-farm quality, logged as a lead only.
- **Implication for the user's stated no-bench-substitution preference:** if physio/energy-recovery items are the recovery mechanism, a no-subs rotation plan still needs a recovery budget. Flagged as an open question, not advice; the user's preference stands until they say otherwise.

## OFFICIAL MECHANICS BLOCK — FTG first-party support articles (fetched 2026-10-03)
All four fetched directly; each rests on a **checkable origin** (FTG's own published documentation = direct evidence). Tier note per the Promotion Gates: a single origin, however direct, does **not** by itself reach Confirmed or High Confidence (both require independent corroboration) — these sit at **Speculative-with-direct-origin** until a second independent route confirms them. Independence caveat recorded with each. Issue logged: see ISSUE-0013.

### Season Pass — two tiers, Progress Bank, tier locks (FTG, "version 12200 onwards")
- Two tiers: **FREE** and **SEASON PASS** (premium; activated by "Activate Pass!").
- Buying the pass **unlocks the Progress Bank**, which "rewards currency based on your **DLL (multiplayer) XP**", **paid at the end of the season**.
- Premium turns profile elements gold (cosmetic).
- **Not a subscription**; must be bought each season; the season's end date is shown on the Season Pass message-box countdown for all users.
- Late purchase still allows all content "regardless of time locks between tiers", provided **Season Points** are earned (example given: buying on day four still allows working toward tier five; the first tier is free).
- **Season Points are earned from completing matches; the amount varies by game mode.**
- Buying the pass instantly unlocks Premium content for the tiers already unlocked on the free track.
- **Tier locks correspond to the day the season is on**: rewards up to the current tier are claimable; later ones unlock day by day. Premium removes all tier locks.
- **Resolves in part** the imported KB's open "Bank-claim gate": the Progress Bank is explicitly a **DLL-XP-driven, season-end payout**.

### Prize Ladder — what it awards (FTG)
- "Awards items based on your progression. The items can include — **coins, gems, coaches, dream point boosts, special players and more!**"
- **Dream Points are given in matches**; the more you earn, the more rewards you unlock.
- **Dream Point Boosts are purchasable** (inside the ladder) and temporarily increase DP awarded.

### Dream Point Boosts — scope and carry-over (FTG) — **RESOLVES an open community question**
- Bought within the Prize Ladder; temporarily increase DP awarded.
- Apply to **career, Dream Draft, scenario and DLL (multiplayer)** matches; **do NOT apply to exhibition or friend matches**.
- Cannot be used if the ladder is complete or no longer active.
- **Unused boosts remain in inventory for the next Prize Ladder** — the community question about boost carry-over is answered by FTG directly. Caveat recorded: FTG writes "all of the above is of course subject to change as we run live services."

### Coin sources (FTG)
- Winning matches · drawing matches · clean sheets · scoring goals · **stadium bonuses** · season objectives · season pass rewards · prize ladder rewards · final league positions · cup wins · **watching video clips (where available)**. Rates are not published on this page.

### Patch/version history — first-party version list recovered (Apple storefront histories)
| Version | Date | First-party notes (abridged) |
|---|---|---|
| 13.430 | Sep 16, 2026 | "Late summer update" — Cult Heroes collection (coming soon at listing time); bug fixes |
| 13.410 | Aug 20, 2026 | "Summer Spotlight update" — **Dynamic Stars** ("upgrading live with national team performances"), **new facility: Fanzone** ("Clan bonuses and Stadium discounts"), **World Tournament** event type, manager accessories, Clan improvements |
| 13.320 | Jun 8, 2026 | updated 2025/26 player data, unlimited special players in club, venues, Kick-Off Stars (Raphinha/Alvarez), soundtrack/SFX |
| 13.060 | Feb 6 (2026) | bug fixes (version history entry) |
| 13.050 | Jan 15 (2026) | Clans, Turkish + Arabic commentary, updated player data, squad size, venues, atmosphere, Kick-Off Stars, soundtrack, commentary, cutscenes, gameplay improvements, bug fixes |

**Live event card (Apple, current):** "Cult Heroes — Sign these top stars who are remembered by passionate football fans. **Now available with boosted attributes.**" — first-party event description (the "boosted attributes" phrase now has a first-party home).

### Official block, part 2 — gem sources · free coins · difficulty · player acquisition (FTG, fetched 2026-10-03)
Same caveat as the part-1 block: single-origin first-party direct evidence → **Speculative-with-direct-origin** (ISSUE-0013).

**Gems (FTG):** obtained by completing **league objectives**, **tournaments**, through the **Season Pass and Prize Ladder**, and by **participating in multiplayer (Dream League Live)**; quantities vary by circumstance; also purchasable in the shop. (No rates.)

**Free coins (FTG):** "you can watch short video clips to earn free coins (subject to availability)" — confirms the ad route independently of the coins list, and matches the user's stated career ad-watching loop exactly.

**Difficulty (FTG):** single-player difficulty starts easy and **tracks division progress up and down**; a **base difficulty setting (Medium / Hard)** has existed since DLS25; in **Dream League Live** players always face another real user — "no bots are used", no difficulty control, no manipulation of any in-game situation including team-mate AI, and no influencing of match outcomes (links FTG's Core Principles). → For the user's career grind, division is the difficulty dial; the base setting is separate and still Medium/Hard only.

**Player acquisition (FTG) — four routes:** Transfers (buy; **the transfer pool refreshes each in-game week, i.e. after each single-player match**), Scouts (discounted selection), Agents (immediate player), **Prize Ladder ("awards special rare players when the criteria is met")**.

### Version chronology — conflict (a) CLOSED
13.320 (Jun 8, 2026) → 13.410 (Aug 20, "Summer Spotlight") → **13.420 (Sep 1)** → 13.430 (Sep 16, "late summer": Cult Heroes). The earlier 13.420/13.430 confusion is resolved as a three-release sequence, not a contradiction.

### Official block, part 3 — Clans · DLL matchmaking · Core Principles · update policy (FTG, fetched 2026-10-03)

**Clans (FTG):** one clan at a time; one leader (leadership passes on; clan dissolves if none remain); clans may set entry requirements (invite code works even when hidden from search); **clan points are earned through matches, challenges and season passes** and are pooled to unlock clan rewards; FTG does not mediate internal disputes and may remove players/clans for ToU breaches. Linked system: the **Fanzone** facility (v13.410) grants Clan bonuses and Stadium discounts.

**Dream League Live matchmaking (FTG):** real-time matching primarily on **LIVE Tier ranking, location, availability pool**; normally same Tier, deviations only when the player pool is thin; **no overlaid difficulty controls**; outcomes governed by skill (tactics, gameplay choices) and **team strength**; opponents get stronger as Tiers progress.

**Core Principles (FTG policy, portfolio-wide):** no tolerance of cheating; consistency of AI for all players; **"we never pre-determine any result in advance, nor do we artificially bias the performance of one player"**; matchmaking accounts for level achieved and recent results; support response norm 24–48 h. **"Our games are not a simulation — luck and unpredictability do play a part."** Named simulated inputs to the AI: passing/shooting quality, **formation choices**, a character's **development profile**, **pitch positioning**, predicted player movement, plus "**weather, ball spin, stadium influence and more**".

**Update policy (FTG):** no advance notice of releases or schedules via support ("we don't provide indications of our future game releases, update schedules or planned activities when requested"); official announcement channels are **TikTok @dreamleaguesoccer.ftg**, **Instagram @playdls**, **Facebook /dreamleaguesoccer** — no X/Twitter channel named there. Update troubleshooting steps (iOS/Android) now in the KB, closing the archived sweep's first open result.

**Dimension-4 note (named lead, not a mechanic):** the Core Principles page is the first first-party text to name **weather, ball spin and stadium influence** as simulated match elements — but it is a portfolio policy page applying to all FTG games, so it is logged as a lead; no DLS26-specific values.

## SECOND-DATABASE PASS — dreamkitsapp.com (fetched 2026-10-03, Turn 14)
**Independence caveat first (matters for every line below):** dreamkitsapp serves all player images from `img.dlsinside.com` and runs a banner ad for `dlsinside.com/players` — the two sites share infrastructure and plausibly a data pipeline, so their agreement is **not** proof of independence. Treated as a second *presentation* of the same data family, not as an independent origin. Cross-source agreement + this caveat = corroboration-lite, recorded as such, never promoted on this basis alone.

**Cult Heroes, full set — 12/12 from the second database, with IDs:** Dybala 28333 SS/RW **85** · De Gea 28324 GK **85** · Aubameyang 28331 CF/RW **85** · F. Alarcón 28327 AM/CM **84** · Vozinha (Évora Dias) 28658 GK **84** · Ziyech 28332 RW/AM **84** · Otamendi 28334 CB **84** · Insigne 28328 LW/RW **84** · David Luiz 28325 CB/DM **84** · Shaqiri 28330 AM/RW **83** · Herrera 28329 CM/DM **83** · Blind 28326 CB/LB **83**.
- The **count of 12 and the three 85s** agree with our archive. The **84/83 split does not**: DreamKits 84×6 / 83×3 vs the earlier-recorded 84×5 / 83×4 → **open conflict, two cards to localise** against the archived octet list. Note also that the page flags its own ratings as "approximate calculations" — consistent with the standing rule (DB OVR labels = estimates).
- Comment-level observation: the earlier "ladder-four" ground truth (Cole 27096 CF 84) is echoed by DreamKits' Classic category sample — the same ID and OVR.

**Collection taxonomy is wider than the seven types we had.** The hub indexes: Cult heroes · **World Winners** · **World Heroes** (world-cup-heroes) · Dynamic Stars · Team of 2025 · **Kick-off Stars** · Champion · **Star** · Classic · **Secret**. Newly named categories: World Heroes, Star, Secret, Kick-off Stars (the last had appeared in storefront notes but not as a tracked type). Sample records captured: Yamal 27845 RW 87 (World Winners) · James Rodríguez 25839 AM 85 (World Heroes) · Jonathan David 27519 CF 85 (Dynamic Stars) · Raphinha 27191 LW 85 (Kick-off Stars) · Arrascaeta 27482 AM 84 (Star) · Messi 25847 RW 84 (Champion) · Avdijaj 24230 GK 59 (Secret).

**Cross-database OVR conflict (new, open):** **Pedri (27133): DreamKits 87 vs SakibPro 86** — same ID, same player, different estimated OVR. Filed as a conflict, not resolved by preference; the resolution test is the in-game card.

## FIRST-PARTY LISTING TEXT (Apple storefront, Turn 14) — facilities, coaches, world size
- **Facilities named by FTG:** "Stadium to **Medical**, **Commercial** and **Training** facilities" — first-party confirmation that a **Medical** facility exists and of the facility family (dimension 4's "Medical Centre" lead now has a first-party home).
- **"Use Coaches to develop your players technical and physical abilities"** — first-party coach statement, consistent with the imported Technical/Fitness type model (dimension 1).
- World size: **4,000+ FIFPRO licensed players**, **8 divisions**, **10+ cup competitions**.
- Monitoring: no new event (Cult Heroes still the only live event), no version bump since 13.430.

## SECOND-DATABASE PASS, part 2 (2026-10-03, Turn 15) — classic / champion / world-winners / Season Pass card

**Champion family COMPLETE (12/12):** Messi 25841 88 · C. Ronaldo 25842 88 · Modrić 25837 86 · Di María 25845 85 · Kanté 26022 85 · Messi 25847 84 · Sánchez 25844 84 · Vidal 25977 84 · Di María 25846 83 · Vardy 25836 83 · C. Ronaldo 25849 82 · Balotelli 25835 82. → Count and top pair match the SakibPro index; the earlier "Messi 25847 84" sample is explained as the **second Messi**, not a contradiction.

**World Winners COMPLETE (8/8):** Rodri 27843 88 · E. Martínez 27849 87 · Yamal 27845 87 · Pogba 27846 87 · Enzo 27838 85 · Cubarsí 27844 85 · Cucurella 28188 85 · Pavard 27847 84. Yamal agrees with our record; Rodri and E. Martínez read **+1 vs the archive** — estimate drift, logged.

**Classic family, pages 1–2 of 3 (30 records so far; page 3 pending).** Highlights: Matthäus 24596 & 27201 both 87 · Rivaldo 26843 & 27094 both 86 · Cannavaro 26842 86 · **Essien 26838 85** · **Cole 27096 84** · **Petit 27203 85** · **Berbatov 27675 85** · Zola 25094 85 · Gascoigne 24598 85 · Batistuta 24595 & 27204 85 · Trezeguet 26837 85 · Chiellini 25099 85 · Petit 25090 85 · Bergkamp 27202 & 25100 85 · Pires 26839 85 · Desailly 26836 & 27093 · Souness 25089 · Zenga 25097 GK · Crespo 27095 & 25095 · Cole 25091 · Valderrama 26840 · Šuker 25096 · Adams 25093 · Bergkamp 25092.

**Duplicate-name pattern is systematic** (two of several: Matthäus, Rivaldo, Petit, Berbatov?/no, Cole 27096+25091, Crespo, Bergkamp, Batistuta, Desailly, Di María, Messi, Ronaldo). Implication: any "one card per player" assumption is wrong at family level; matching must be by **id**, never by name.

**Season Pass card CONFIRMED on a second database:** João Pedro **28356**, Brazil, CF/SS/AM, right, 182/72, b. 2001-09-26; rating table lists **V13430 = 82**; other version 17565 @80. Stats (×10 scale) SPE 830 / ACC 830 / STA 801 / STR 800 / CON 860 / PAS 830 / SHO 870 / TAC 290, GKR 122 / GKH 121.

**New/updated conflicts:** (f) localised — the Cult Heroes 84/83 split is **only Vozinha 28658** (DreamKits/dlsinside 84 vs SakibPro/dlskiturl 83); every other card agrees across sources. (h) **NEW:** DK estimates read **85 for Petit 27203 and Berbatov 27675** vs our resolved ladder-four record of 84 — while Cole 27096 (84) and Essien 26838 (85) agree, so the drift is confined to two cards. The in-game ladder screen remains decisive.

## SECOND-DATABASE PASS, part 3 (2026-10-03, Turn 16) — remaining families + monitoring failure
**Monitoring attempt failed and that is itself recorded:** shell `curl` to dlskiturl.com failed with TLS `SSL_ERROR_SYSCALL` (HTTP 000) while the fetch tool succeeds on the same host → **sandbox shell HTTPS is unreliable at the TLS layer** (feeds G-0004). Use the fetch tool for all retrievals; do not plan monitoring around shell curl.

**Kick-off Stars COMPLETE (2):** Raphinha 27191 LW/AM 85 · Julián Álvarez 27127 CF/SS 84 — the exact launch pair advertised on the storefront; first-party claim now independently data-backed.

**World Heroes COMPLETE (8):** Messi 27848 87 · C. Ronaldo 27841 87 · De Bruyne 27840 86 · James Rodríguez 25839 85 · Perišić 27850 85 · Navas 27837 85 · Gvardiol 27842 84 · Walker 27839 84. Note a second C. Ronaldo special (27841) alongside the Champion pair — parallel families, not aliases.

**Dynamic Stars (p1 of 3, 15 records):** **Nico Williams 27509 — 96, the highest OVR seen anywhere in this sweep**; De Paul 27512 93 · Barcola 27510 91 · Eze 27508 90 · Akanji 27517 88 · Bounou 27529 88 · Sørloth 27523 88 · Onana 27516 87 · Fidalgo 27520 87 · Matheus Cunha 27511 86 · Ríos 27525 86 · McKennie 27518 86 · Alderete 28243 85 · Marmoush 27531 85 · Jonathan David 27519 85.

**Classic COMPLETE in this database (32, not 34):** p3 closes with Gascoigne 24597 82 (a third Gascoigne) and Mendieta 25098 82. → **Open conflict (i): classic count 32 (DK) vs 34 (SakibPro).**

**Secret family — structural clarification:** 18 pages (~250+ records), not an event collection. Prefix system: **Classic / Young / Legendary** variants with low legacy ids (e.g. 2459 Cannavaro, 5666 Matthäus, 5839 Irwin, 5842 Keane, 24594 Young Messi, 24599 Legendary Messi). Top of the class as listed: Classic Bergkamp 5604 91. This class must be treated separately from the ten event families.

**Family counts now standing (DK-sourced, all estimates flagged):** Cult Heroes 12 · Champion 12 · World Winners 8 · World Heroes 8 · Kick-off Stars 2 · Classic 32 · Dynamic Stars ≥15 (3 pages) · Secret ~250+ · Team of 2025 11 (SakibPro) · Season Pass 1 catalogued (6 announced) · Star (not yet sampled).

## SECOND-DATABASE PASS, part 4 (2026-10-03, Turn 17) — Dynamic Stars closed at 40; Star anomaly

**Dynamic Stars COMPLETE — 40 records (15+15+10), matching the archive's "Dynamic Star 40" exactly.** Range 82–96. Full-tier names: p1 Nico Williams 96 · De Paul 93 · Barcola 91 · Eze 90 · Akanji 88 · Bounou 88 · Sørloth 88 · Onana 87 · Fidalgo 87 · Cunha 86 · Ríos 86 · McKennie 86 · Alderete 85 · Marmoush 85 · J. David 85. p2 João Félix 85 · Woltemade 84 · Ndicka 84 · Stanišić 84 · Laimer 84 · Malen 84 · Irvine 83 · Kubo 83 · Ndiaye 83 · Wissa 83 · I. Williams 83 · R. Williams (GK) 83 · Hincapié 83 · Elanga 83 · Muharemović 83. p3 Aït-Nouri 83 · Isidor 82 · Schick 82 · Robertson 82 · Wood 82 · Kang-in Lee 82 · Abdulhamid 82 · Güler 82 · Khusanov 82 · Núñez 82.
→ Families now **closed and cross-checked**: Cult Heroes 12 ✓(archive 12) · Champion 12 ✓ · World Winners 8 ✓ · World Heroes 8 ✓ · Dynamic Stars **40 ✓** · Kick-off Stars 2 · Classic 32 (vs 34, conflict (i) open) · Team of 2025 11 ✓ · Season Pass 1 catalogued.

**Star family p1 — RENDER ANOMALY (recorded to prevent a false count):** "Elliot Anderson 27832 85 DM/CM" appears **nine times** in the rendered output; only McTominay 25987 85, Álex Baena 25989 85, Igor Thiago 27483 84 (×2) and Antonee Robinson 25985 84 are distinct records. Treated as a template-duplication artifact; **no counts derived**. Star spans 9 pages (≈135 records) — largest event-class family after Secret; not yet enumerated.

**Semi-independence test attempted and blocked:** dlsinside's `/players/specials` index is also a JS gallery (12 unlabeled numerals only, semantics unknown, not interpreted). The cross-read must be done on **individual card pages**, which have rendered successfully before (e.g. the João Pedro card page in past sessions).

**Monitoring (second route check):** dlskiturl front page unchanged from Turn 15 — no DLS26 post newer than the English League Classics item, nothing October-dated.

## TURN 18 (2026-10-03) — semi-independence test, classic census closed, base-pool scale

### ⚠️ AMENDMENT to an earlier KB line (correction, not a silent edit)
The Turn-15 line "João Pedro 82 **confirmed on a second database**" is **amended**: the two databases return *byte-identical* data for the same card (dlsinside `/player/joao-pedro/28356` shows ID 28356, version 160-13430, CF/SS/AM, Brazil, right, 182 cm, age 25, rating 82, Shooting 87 / Speed 83 / Acc 83 — every value identical to the dreamkitsapp record). This is **confirmation twice within ONE data family**, i.e. corroboration-lite, not independent corroboration. The shared-CDN evidence from Turn 14 now has a behavioural match. **Standing rule reinforced:** dreamkitsapp + dlsinside count as ONE source family; never as two independent sources for any promotion.

### Classic family census CLOSED on both sides — conflict (i) characterised
- **SakibPro: 34 records** (p1 12 + p2 12 + p3 10). Full id set captured in the ledger (pages 092–094).
- **DreamKits: 32 records** (15+15+2).
- **The difference = {26841, Irwin 5839}.** SakibPro's p1 carries an **unnamed record 26841 (GK, Spain, 86)** with a placeholder slug; and SakibPro files **Irwin 5839 as Classic** where DreamKits files him under Secret. **Conclusion: the 32↔34 gap is a classification/coverage boundary, not a different card universe** — one record (26841) is unexplained and only appears on the SakibPro side.

### Cross-source OVR disagreement is CONFINED TO ±1 (quantified rule)
Direct comparison of all 31 shared classic records between the two databases: **~19 agree exactly, ~10–12 differ by exactly one point, and none differ by more than one** (examples: Matthäus 24596/27201 87 vs 86; Berbatov 27675 85 vs 84; Petit 25090/27203 85 vs 84; Souness 25089 85 vs 84; Pires 26839 85 vs 84; Rivaldo 26843 86 vs 85; Zola 25094 85 vs 84; Zenga 25097 84 vs 83; Bergkamp 25092 83 vs 82; Cole 27096 84/84 ✓; Essien 26838 85/85 ✓; Cannavaro 26842 86/86 ✓). **Rule of record: in this dataset, cross-source OVR conflicts are ±1 estimate-band noise; the in-game/extracted value remains the only ground truth.**

### Base (normal) pool scale — first hard figure
SakibPro's **normal** index: **14,232 verified records across 1,186 pages** — the base-pool scale behind the storefront's "4,000+ FIFPRO licensed players". Top of the OVR-ordered list: **Crimaldi 27676 AM 92 (anomaly** — 92 on a "normal" card, id in the special block**)**; **Moore 25806 RM 88 (anomaly** — no nation flag rendered, id in the 258xx special block**)**; then the real base ceiling: Haaland 17196 86 · **Kane 10159 86** · Yamal 21929 86 · Mbappé 14756 86 · O. Dembélé 15403 86 · **Olise 18158 86** · B. Fernandes 12434 85 · Donnarumma 14078 85 · Gabriel 16347 85 · Hakimi 15932 85. (Kane's base id and Olise's 86 both match earlier archive notes independently.) Both anomalies are flagged for verification, not accepted.

## TURN 19 (2026-10-03) — index anomalies debunked; 26841 resolved; tools surface mapped

**Two index anomalies verified as BOGUS (both 404 as cards):** "Crimaldi 27676 AM 92" and "Moore 25806 RM 88" do **not exist** as card pages. They are index artifacts. → **The normal/base-pool ceiling stands at the observed 86 class** (Haaland 17196, Kane 10159, Yamal 21929, Mbappé 14756, O. Dembélé 15403, Olise 18158). **Rule reinforced: never use a value from an index row without opening the card page.**

**Unnamed Classic 26841 resolved as a stub:** the page exists, titled "**Classic 2006**" — GK, Spain, Free Agent, **left foot, 180 cm**, base rating **86 marked "OFFICIAL"**, acquisition "Classic Agent", max +10 → 96 — but **the name is empty and all eight stat fields render 0/blank**: an auto-generated record. Treated as an unreleased/placeholder Classic entry; not counted as a playable card. Conflict (i) refined but not fully closed.

**SakibPro tools surface mapped (nine tools):** Player Database · Kit Creator · Card Creator · Kits Engine Hub · Logo Link Generator · **Price Calculator (coin price from OVR + position)** · **Upgrade Simulator (+10 coaching model)** · **Squad Builder (formations/lineups)** · **Compare Players**. Tools are *calculators* (model outputs), not evidence; queued leads: price calculator and squad builder (relevant to gate dims 2 and 6 planning, but must be labelled as site models).

## TURN 20 (2026-10-03) — narrative sources closed out; coin-price model captured

### Two previously-unfetched secondary narratives, now read (both classified: content/SEO, corroboration only)
- **thesoccerera.com** — matches the first-party storefront notes we already hold (4,000+/8 divisions/10+ cups/facility list; Summer Spotlight = Dynamic Stars + Fanzone + World Tournament + manager accessories + clan improvements; Winter Reload = Dream Stars 26 + 12th Man Vote + News System + clan leaderboards/vice-captains/**Clan Point boosts** + UI/SFX + Game Centre). Adds one detail consistent with first-party clan text: **Clan Point boosts** exist as a clan-progression feature.
- **dlskits.mobi** — same broad content; **ERRORS on version attribution**: it assigns the Cult Heroes collection to **13.410**, contradicting the storefront chain (13.410 = Summer Spotlight Aug 20; 13.420 = Sep 1 with 'Cult Heroes coming soon'; 13.430 = Sep 16 'late summer update'). Logged as **conflict (j) — a secondary-source error, not a live contradiction**; the first-party version history stands.
- **reddit.com/r/DreamLeagueSoccer 1vtm4ty** — **HTTP 403** (second Reddit wall in the sweep; treat Reddit as fetch-blocked).

### Coin price model — dimension 2 (third-party tool, methodology stated)
- A player's **coin price = f(base OVR, exact position)**; attackers cost more than defenders at equal rating. Worked data point: **86 OVR CF = 2,970 coins** (Kane 10159, Mbappé 14756, O. Dembélé 15403, Haaland 17196 all shown at 2,970 coins).
- The site distinguishes **"Verified Data"** (coin amount manually confirmed in the live transfer market) from **"Extrapolated"** (computed from the game's pricing formula) — a useful methodological note; only "Verified" rows could ever support a promoted claim, and even then from a third-party tool.
- **Secret players are offered at a discount** vs the standard price: the discount is how the community guesses the secret player's identity.

## TURN 21 (2026-10-04) — upgrade/coaching model captured; pre-launch source triaged

### Upgrade / coaching model (dimension 1) — third-party tool, recorded as a MODEL
From `sakibpro.com/players/simulator.html` (site model, NOT first-party data — it markets itself as using "the official hidden weighting system", which we cannot verify):
- **Development weight**: allocate up to **100%**; **every 10% of total progression weight = +1 OVR**; hard cap **+10 OVR** at 100%.
- **Stat weights are unequal** — CON and SPE consume more capacity than STA.
- **Coach types and gem prices**: Fitness (SPE, ACC, STA, STR) Common 25 / Rare 75 / Legend 225 gems · Technical (CON, PAS, SHO, TAC) 25 / 75 / 225 · **Special (ALL STATS) 90 / 240 / 400** · Goalkeeping (GKR, GKH) 15 / 40 / 150.
- **Coach selection**: a 1-of-3 offer, **+2 to the chosen attribute**, with DISCARD & RESHUFFLE; the tool tracks "coaches wasted".
- **Facility discount tiers**: 0 / 5 / 10 / 15 / 20 / 30 %.
- **Goalkeepers use a different rule**: classic points system, **every 2.2 visual points to GKR/GKP = +1 OVR, capped at 22 points total allocation**.
- Source inconsistency noted: the manual-coaching panel lists **GKR/GKH**, the FAQ says **GKR/GKP**.

### Pre-launch news article triaged (thesoccerera "new clans upgraded")
File is **pre-launch era** (launches-window claims, references the app as v13.060 updated 5 Feb 2026) and **self-contradictory** (Kane listed 86 in one table, 85 in another). Classified LOW-RELIABILITY. Two uses:
1. **It independently corroborates the base-pool ceiling of 86** and names the same attackers our DB reads give at 86 (Dembélé, Mbappé, Kane, Haaland).
2. It introduces **conflict (k) Pedri 85 (article) vs 87/86 (DBs)** and **conflict (l) Kane 86 vs 85 inside the same article** — which is precisely why it cannot settle conflict (g). It also lists Vini Jr, Salah and Rodri at 86, unsupported by any database read (Rodri's 88 is a World Winners special, not a base card).

### Star family (DreamKits page 2)
- **5 unique records in 15 rendered slots** (render-duplication hazard, second occurrence): Igor Thiago 27483 84 CF · de Arrascaeta 27482 84 AM/LW · Ryerson 27828 84 RB/LB · Svilar 27827 84 GK · Yıldız 27481 84 SS/LW — **all 84 OVR**, all team image t258.
- Pagination is **nested/broken** (page 2 exposes its own /p/1…/p/9 sub-pager) ⇒ the Star family is **structurally unlistable by pagination**; it stays recorded as "sampled, not enumerated".
- **Asset-level proof of the one-family finding**: DreamKits serves its card/flag/team images from `img.dlsinside.com`.

### CORRECTION (Turn 21) — the Turn-20 "saturation" statement is RETRACTED
Turn 20 recorded that "no high-value unread narrative source remains identified". **That was wrong.** It was derived from an **unreconciled frontier**: the unvisited list still contained **79 stale lead strings** (URLs already fetched in earlier turns but never removed), and behind them a genuinely unvisited **first-party** block of **33 support.ftgames.com URLs** — including **"How do I develop my players" (article 360003914778)**, developer-authored text that speaks directly to gate dimension 1, the thinnest dimension. Also unread: "How can I get Gems" (360003914938), "What are Leaderboards" (360003914998), "Can I sell my players" (360003945617), "How do I change my manager" (360003945937), "Why doesn't my player look like the real person" (360004718318), "How do I play a Friend Match" (360019064438), "Removal of Facebook Login from DLS" (9804887423121).
**Lesson recorded:** never read yield off the frontier list without normalising and subtracting the visited set first; a frontier that is never reconciled inflates and then hides real work. Retrieval is **not** saturated — that block is the Turn-22 target.

## TURN 22 (2026-10-04) — FIRST-PARTY BLOCK OPENED: dims 1, 2, 4, 6 filled from FTG's own support text

The frontier reconciliation at Turn 21 exposed 33 unread first-party articles. Five of the highest-value ones are now read. **Everything below is first-party (support.ftgames.com) unless marked otherwise.**

### Coaching / player development (dimension 1) — article 360003914778
- **Coaches** are the development item: tap the **"Coaches" button in the Team Management screen** to select your coach.
- **"Coaches will then randomly select a player to permanently upgrade."** ← the publisher states the target player is **random**, not chosen.
- **Form Boosts** are the temporary alternative: more powerful but time-limited, lasting **a set number of matches determined by your Training facility level** (minimum one match).
- **CONFLICT (m):** first-party says the coach picks the player at random; the SakibPro simulator (page-106) lets the user pick the player and allocate development weight. Unresolved — either the support article predates DLS 26 or the third-party model misrepresents targeting. Both are on record; neither is promoted to a claim.

### Currencies (dimension 2)
- **Gem income (360003914938):** completing **league objectives**, completing **tournaments**, the **Season Pass**, the **Prize Ladder**, and **playing Multiplayer (Dream League Live)**; quantity varies by circumstance; purchasable in the shop.
- **Selling players (360003945617, stated as applicable "from DLS version 12200 onwards"):** press **"Manage Players"** at the bottom-right of the **Transfers** screen and release the player. **You receive a COACH for releasing a player.** Recently sold players sit in the **"Recover"** section of Manage Players for a limited time. → a coach ↔ transfer loop exists.

### Stats → gameplay (dimension 4) — article 360019166777, the most complete first-party mechanics text found this session
FTG's own framing: *"DLS is a 'game' and is not intended to be a full and accurate simulation… part of the 'game' is to discover yourself how different stats affect the game, whilst managing elements of unpredictability."* Then, per stat:
- **SPE** — top speed. Top speed **drops as ENERGY drops**. The **dribbling speed penalty is inversely proportional to CON**: equal SPE, higher CON dribbles faster. FTG states outright that a lower-SPE player can outrun a higher-SPE one.
- **ACC** — how quickly top speed is reached.
- **STA** — how fast energy depletes when running **and how much energy is restored at half time**; matters more for positions that cover more ground (a centre-back covers far less than a midfielder).
- **CON** — smaller dribbling speed penalty; quicker kick after the first touch; closer touches (sharper direction changes); higher chance of **skill kicks** (rabona, overhead) and **skill controls** (heel-chops); success of **skill shots** (double-tap/swipe), together with SHO.
- **STR** — collision outcomes against the other player (who keeps or wins the ball) and **shorter stumble time after being tackled**.
- **TAC** — likelihood of a successful tackle and the **reach of both standing and sliding tackles**.
- **PAS** — accuracy of **all** pass types.
- **SHO** — shot accuracy; the **"assist" applied to shots (moves the shot away from the keeper)**; keeping shots **low** (low SHO skies them); skill-shot success (with CON); special kicks/headers (overhead kick, diving header); **curl on free kicks**.
- **GKH** — handling/presence: **catch vs deflect**, coming to claim crosses, stability when opponents are close or colliding.
- **GKR** — reaction/shot-stopping: faster reaction time, save chance scaled to **shot speed and save distance**, and **"anticipate" saves** made without time to react.
- **ENERGY** — below a threshold, **all** other stats degrade gradually as energy falls; most noticeable on speed.
- This is the mechanism behind the CON/SPE weighting asymmetry the third-party simulator asserts — but it does **not** confirm that simulator's numbers.

### Online / social (dimension 6) — article 360003914998
- **Leaderboards** track performance against other players in **Multiplayer (Dream League Live)**; they **reset on intervals from 3 to 30 days**, with prizes awarded on final position.

### New first-party leads discovered inside these articles (added to the frontier)
`213852049 Why are some players missing from the app` · `17146555181585 How do I sell players` · `360008831518 Why are my players auto-switching all the time` · `4408249822609 Age Confirmation, Personal Ads and Notifications` · `360000262229 When will the next app update be` · `214385285 How do I earn coins in the app`.

## TURN 23 (2026-10-04) — first-party block, second pass: currency, roster churn, controls, and FTG's own disclosure policy

(All first-party, support.ftgames.com; none of these articles carries a version stamp.)

### Coin income — the definitive first-party list (article 214385285, dimension 2)
Eleven coin sources, verbatim: **Winning Matches · Drawing Matches · Clean Sheets · Scoring Goals · Stadium Bonuses · Season Objectives · Season Pass rewards · Prize Ladder rewards · Final League Positions · Cup Wins · Watching Video Clips (where available)**.
- This **extends** the previously held coin-source list with Clean Sheets, Scoring Goals, Season Objectives, Final League Positions and Cup Wins.
- It also **confirms the user's own ad-watching route as an officially listed coin source** ("Watching Video Clips").
- No amounts or rates are given anywhere.

### Selling players — two first-party articles that disagree (dimension 2)
- Article **360003945617** ("Can I sell my players", v12200+): Manage Players on the Transfers screen; you receive **a coach**.
- Article **17146555181585** ("How do I sell players"; assigned to the UCS Help Center section): you may discard squad players **not in your Starting 11**, provided you keep the necessary number of players, and you receive **"a specified amount of bux"**.
- **Conflict (n) — terminology:** this article says **"bux"** where every other DLS surface says **coins**. Unresolved: either stale generic FTG wording, or a distinct/legacy term.
- **Conflict (o) — reward:** **bux** in one article vs **a coach** in the other, both first-party. Not harmonised; possibly both are granted.

### Update disclosure — FTG's own policy (article 360000262229)
"We don't provide indications of our future game releases, update schedules or planned activities when requested." Official channels named: **TikTok @dreamleaguesoccer.ftg**, **Instagram @playdls**, **Facebook /dreamleaguesoccer/**.
**Consequence for monitoring: no first-party source will ever pre-announce an update.** The storefront "What's New" text is therefore the *only* authoritative version signal, and third-party "coming soon" posts are not first-party information.

### Roster churn and licensing (article 213852049, dimension 4)
"We are constantly updating our player database, so you may find that new players are added whilst some players may be removed every now and then. Also, unfortunately, some players cannot be included for licensing reasons."
→ **Licensing, not oversight, is the stated cause of absences**, and the pool is explicitly fluid — which is the structural reason base-pool counts drift between sources and between dates.

### Controls (article 360008831518, dimension 5)
With default settings, control **auto-switches between players when defending**. Change it via the **gear icon (top-left) → Controls → "Auto Switch"**. This confirms a **Controls** sub-menu inside settings — the same menu family that holds the user's Kick Assist / Cross Assist preferences.

### Monitoring
dlskiturl front page unchanged on the **seventh** check.

## TURN 24 (2026-10-05) — first-party block, third pass: card colours, roles, skill moves, re-signing

(All first-party, support.ftgames.com; no version stamps.)

### Card colour ladder — the first first-party evidence for dimension 3 (article 214385645)
Verbatim: *"Depending on the overall rating of your player **or if they are a special player**, they will have a different player card colour, for example - **common (bronze), rare (blue), legendary (gold), max (red) and special (black)**."*
- This is a **two-driver ladder**: the OVR band sets the tier for ordinary cards, and **special-player status is an independent driver** that puts a card in the **black** tier regardless.
- **"max (red)"** is the tier reached at the upgrade cap — consistent with the **+10 OVR** cap in the third-party simulator model (page-106).
- **"special (black)"** settles the open question about the black card design seen on card art (28324): black is the special tier, not a distinct event family.
- The article gives **no OVR thresholds** for the bronze/blue/gold bands, so those boundaries remain unevidenced.

### Player Roles (article 7917583876625) — UCS Help Center section; not a DLS-specific source
"Navigate to the **'Squad' screen from the Main Menu** and tap the **'Roles' button**." A Roles system exists as a first-class part of the Squad screen. **What the roles are and what they do is not stated anywhere we have read** — recorded as a known-unknown.

### Selling and re-signing (article 214385465, "version 12200 onwards")
Yes, a sold player can be re-signed, but it may be some time before they are available again; recently sold players sit in **"Recover"** for a limited time. **Risk rule: "some players are subject to licensing restrictions, so if you sell a player that is no longer available in the game, you will not be able to re-sign them."** → selling a player who later leaves the database for licensing reasons is a permanent loss.

### Free coins (article 213851369)
"Yes, you can watch short video clips to earn free coins (**subject to availability**)." — first-party confirmation of the user's ad-watching income route, with the publisher's own availability caveat.

### Skill moves (article 213851489, dimension 5)
Swipe the **right-hand side of the screen near the controls while in possession**: **down = Marseille turn · up = rainbow flick · left/right = stepover**.
This joins up with the stat bible (360019166777): **CON** raises the chance of successfully executing a skill move (step-over, Marseille turn, heel-flick) and **SHO** raises the chance of special kicks. Inputs and success modifiers are now both on record — from first-party text in both cases.

### New first-party leads harvested
`7917587319313 How do I change my formation` (relevant to the user's 3-2-3-2) · `7917423348497 How do I get promoted` · `17144107973265 How do I add a friend` · `360000842697 Something happened in the game that's not realistic. Why is this?` · `214385385 How do I change between Home and Away kits before a match` · `7918056936721 How can I change my graphics settings`.

### Monitoring
dlskiturl front page unchanged on the **eighth** check.

## TURN 25 (2026-10-05) — first-party block, fourth pass: formations, promotion/relegation, fairness, customisation

(All first-party, support.ftgames.com; no version stamps.)

### Formations are season-gated (article 7917587319313) — UCS Help Center section; not DLS evidence
"Navigate to the **Squad** section and tap the **formation grid button** to change your formation." Then: **"Formations are limited by season, so for example, in one season you may only have 2 formations to choose from."**
- **This is a first-party constraint on squad planning that no database carries:** the user's preferred 3-2-3-2 (and the unlocked 3-1-4-2) may simply **not be selectable in a given season**.
- The "2 formations" figure is given as an *example*, not a rule — the actual per-season count is unevidenced.

### Promotion and relegation run on an XP meter (article 7917423348497, dimension 6) — UCS Help Center section; not DLS evidence
"The more matches you win, the more XP you will earn. When you reach the **maximum XP for your current rank**, you will be promoted. Similarly, **losing matches will cause you to lose XP and get relegated to a lower rank**."
- **New mechanic:** rank is an XP meter that **decreases on defeats**, and relegation is live. No thresholds or rank names are given.

### FTG's own position on luck, realism and fairness (article 360000842697)
DLS "is not intended to be a fully accurate simulation of the sport or physics of soccer"; it "aims to balance fun with realism"; unpredictable situations occur "just like in real life"; and **"like most games, luck forms a part of the experience. Ultimately it is the same for all players and above all else we consider our games 'fair'."** FTG reviews feedback and fixes what it judges to harm enjoyment, but states not everything will be addressed.
- **Relation to the open rubber-banding allegation** (a storefront review claims comeback/balance scripting): this article **does not admit any balancing mechanic**, and it asserts identical rules for all players. That is a **publisher position, not evidence either way** — the allegation remains recorded as player perception, now with the counter-position beside it.

### Customisation and likeness (articles 214385345, 360004718318)
- Team name: **Customise button → Team Name** (a Customise hub holds team identity settings).
- Player likeness: "DLS is an ever expanding app... over time you will see improvements." The page's comments are **5–6 years old** and must not be read as current evidence; one **FTG staff reply** there repeats the licensing cause — "for licensing reasons some players may not be in DLS" — corroborating article 213852049 from a second first-party surface.

### New first-party leads harvested
`7916583518353 What are Season Points` · `7917023109009 How do I edit my team crest`.

### Monitoring
dlskiturl front page unchanged on the **ninth** check.

## TURN 26 (2026-10-05) — first-party block, fifth pass: Dream Point Boosts, Season Points, ad supply, offline play

(All first-party, support.ftgames.com.)

### Dream Point Boosts (article 24081168829330) — the operationally most useful article of the session
1. Boosts are **purchased within the Prize Ladder** and temporarily increase the Dream Points awarded in matches.
2. They apply **only** to **career, dream draft, scenario and DLL (multiplayer)** matches — **not** to exhibition or friend matches.
3. They **cannot be used if the Prize Ladder is complete or no longer active**.
4. **Unused boosts stay in your inventory for the next Prize Ladder.**
5. FTG states all of it is **"subject to change as we run live services"**.
→ **There is no use-it-or-lose-it pressure from the boost side (they carry over), but a boost is dead weight once the ladder ends** — so its value depends entirely on the still-unresolved ladder end date. This sharpens, without resolving, the timing question behind the 14 October timer.

### Season Points are NOT Dream Points (article 7916583518353)
Season Points are **earned from winning matches**, the running total is shown on the **season leaderboard reached from the Main Menu**, and they **unlock prize tiers in the Season Pass ladder**.
→ Two separate economies: **Season Points → Season Pass ladder (from wins)**; **Dream Points → Prize Ladder (from matches, boostable)**. Conflating them would corrupt any ladder plan.

### Ad supply — the user's coin route is variable income by design (article 360017166918)
- FTG runs **several ad networks, each managing its own content**; it controls the *types* of advert but **availability and per-provider limits are not set by FTG**.
- Verbatim: **"there is never a promise or guarantee made by our company to any player about the frequency of video clips or reward doublers."**
- **If LAT (Limit Ad Tracking) is enabled, ad networks may simply offer no ads at all** — FTG says this worsened on iOS after iOS 14 — so LAT on works against a player who *wants* ads (personal choice either way).
- Suggested fixes when clips vanish: latest app version; reinstall after backing up the profile; disable VPN; prefer Wi-Fi over mobile data; restart the device; force-close and reopen the app regularly; or wait a few days.
→ This **bounds** the earlier finding that video clips are an official coin source: supply is provider-controlled and no frequency is guaranteed.

### Offline play (article 360004034498)
Online is required for the majority of features "to make DLS our most secure version to date", which FTG says reduces unfair exploits; benefits claimed are server-side progress backup and restore across devices, faster fixes, and a larger base on the current version. **Some sections work offline and Exhibition matches are playable offline.**

### Customisation (article 360003945937)
Manager name and appearance: **Customise button inside My Club → Manager** — the same hub that holds Team Name.

### Monitoring
dlskiturl front page unchanged on the **tenth** check.

## TURN 27 (2026-10-05) — first-party block, sixth pass: Season Pass economics, multiplayer tech, save-data risk, enforcement

(All first-party, support.ftgames.com.)

### Season Pass — article 17143633310225 (far more detailed than the id we already held)
- **Two tracks: FREE (everyone) and PREMIUM (paid, via the "Activate Pass!" button).**
- **Buying the Season Pass does NOT unlock the Season VIP** (stated explicitly).
- Purchase effects: cosmetic profile changes shown to other players; **unlocks the Progress Bank, which pays out currency based on your Season Points — at the END of the season**.
- **Not a subscription**; must be repurchased each season; no auto-renewal and no charge without permission.
- **A countdown timer on the Season Pass message box shows when the current season ends for ALL users** — a second in-game timer, distinct from the Prize Ladder timer.
- **Late purchase removes the time locks:** buy on day four and you can work towards tier five immediately (first tier is free).
- **Retroactive:** buying instantly converts every free-track tier you have already unlocked into Premium rewards, with no extra Season Points needed (unlocked to tier 15 = 15 Premium tiers claimable at once).
- **Tier locks track the day the pass is on:** everything up to the current tier is claimable; later tiers open the next day.
- **Conflict (p):** this article says **Season Points come from completing matches** and can be bought in the Shop when offered; article 7916583518353 says they come from **winning** matches. Both are FTG text; not harmonised.

### Multiplayer (article 360004222118)
Wi-Fi or high-quality 5G/4G/3G only; **~2 MB per match**; IPv6 and 5G supported; modest bandwidth needs but **sensitive to latency and packet loss**; **both players connect to FTG cloud servers and the opponent's connection quality does not degrade your experience, so lag-switching is ineffective**; the opponent is never given your network address; some public Wi-Fi is unsuitable; **no Facebook invites, but local multiplayer works between two devices on the same platform on the same Wi-Fi router**; disable Bluetooth for smoother Wi-Fi play.

### Friend Match (article 360019064438)
Private matches by shared code from the **Dream League Live button on the home screen**; codes accept **A–Z, 0–9 and hyphen only**; a code already in use can drop you into the wrong match, so pick something unique; Friend Match stats are tracked in the DLL area. (Friend matches are excluded from Dream Point Boosts per the boost article.)

### Save data — a live risk for the user's career (article 214387685)
Link the profile to **"Sign in with Google"** or **"Sign in with Apple"** (iOS 13.0+) **from inside the game's settings — it is not automatic**. Without it, FTG **cannot guarantee recovery** after uninstall, device reset, or device change. And explicitly: **save data is NOT secured on Google Play Games or iCloud** — those are different cloud-save services the games do not use.

### Enforcement (article 360008904718)
Bans follow modded APKs, external hacks, or exploiting unknown bugs — examples given are improper currency gain, interference with gameplay AI, and bypassing normal progression. **Only App Store / Play Store builds are authorised.** Offensive team or manager names can also draw action. Support will not lift a ban on request.

### Monitoring
dlskiturl front page unchanged on the **eleventh** check.

## TURN 28 (2026-10-05) — first-party block, seventh pass: the two Season Pass texts diverged; difficulty denial scoped

(All first-party, support.ftgames.com.)

### The two Season Pass articles disagree on what the Progress Bank pays on
Reading **4404070913169** (older, version-gated "12200 onwards") beside **17143633310225** (newer):
- **Conflict (q):** the Progress Bank rewards currency based on **DLL (multiplayer) XP** in the older article, but on **Season Points** in the newer one. Both first-party; not harmonised.
- Naming differs too: FREE + **"SEASON PASS"** (older) vs FREE + **"PREMIUM"** (newer).
- **Only the older article states that buying the pass REMOVES ALL TIER LOCKS** — you are then unrestricted by how much of the season is left, provided you earn the Season Points.
- **Only the newer article states that buying the pass does NOT unlock the Season VIP.**
- Shared: not a subscription; repurchase each season; no auto-renewal; season-end countdown on the message box; retroactive conversion of unlocked free tiers; late purchase removes time locks; tier locks track the current day.
- **Season Points source (conflict p) now leans:** **both** Season Pass articles say Season Points come from **completing matches**, with the older one adding that **the amount varies by game mode**; only the standalone Season Points article (7916583518353) says **winning** matches. Two surfaces against one — but no surface is discarded and the conflict stays open.

### Save data in DLS — exact menu path and the silent-unlink trap (article 4413273241873)
- **One DLS account per player.**
- Menu path: **main menu → Options (gear, top left) → Advanced tab** → **Manage Devices** and **Link Profile**.
- Route A — **Sign in with Google (Android only) / Sign in with Apple (iOS only)**: sign in on the new device with the same account.
- Route B — **code transfer** (the recommended cross-platform route, Android↔iOS): old device → Manage Devices → **Generate Code** (subject to a device limit) → enter it under **Link Profile** on the new device. **The code cannot be used on the device that generated it.**
- **Trap: signing out of Sign in with Google / Apple at any point unlinks the profile**, after which uninstall or a device change can lose it. Shared credentials or codes are unrecoverable if lost.

### Prize Ladder reward pool (article 23108987826962)
The ladder "awards items based on your progression": **coins, gems, coaches, dream point boosts, special players and more**. **Dream Points are given in matches**; boosts raise them temporarily.
→ **The ladder itself grants coaches** — closing the loop between ladder rewards, the coaching system, and the sell-a-player-for-a-coach rule.

### Clans (article 30839289076626)
One clan at a time; one leader (leadership passes on; the clan vanishes if empty); **clans with entry requirements are hidden from search unless you meet them, but an invite code still gets you in**; **clan points come from matches, challenges and season passes**; FTG will not mediate disputes and may remove players or whole clans.

### Difficulty and scripting (article 360018360418) — the denial is multiplayer-only
- **Single player:** difficulty starts easy and **changes as you move up and down the divisions**; **DLS25 added a base difficulty setting of Medium or Hard**.
- **Dream League Live:** always a real opponent, **no bots**, and verbatim — **"no control of difficulty and **no manipulation of any in-game situation, including team mate AI**. There is **no influencing of any outcome to any match**."**
- **Scope is the whole point:** the denial covers **multiplayer**. For **single player** FTG instead confirms difficulty that **scales with division movement**. The rubber-banding allegation therefore stays **open for career play** and **closed as far as FTG's word goes for DLL** — two facts recorded side by side, neither promoted.

### Monitoring
dlskiturl front page unchanged on the **twelfth** check.

## TURN 29 (2026-10-05) — first-party block, eighth pass: account recovery, customisation, multiplayer etiquette

(All first-party, support.ftgames.com.)

### Account recovery — the complete picture
- **Facebook Login is dead:** removed from DLS several years ago, and **profiles previously stored via Facebook Login cannot be recovered** (article 9804887423121).
- **Live routes:** **Sign in with Apple (iOS 13+) or Sign in with Google** only.
- **Never routes:** Google Play Games and iCloud (article 214387685).
- **Silent trap:** signing out of Google/Apple unlinks the profile (article 4413273241873).
- → If the user's profile was ever Facebook-linked and never migrated, it is unrecoverable; if it is currently unlinked, the fix is Options → Advanced → Link Profile.

### Customisation, mapped (article 360004080497)
Customise screen holds team name, manager name, shirt numbers and boot colours, and kit/logo import. Tabs: **Players** (per-player boot colour and shirt number), **Manager** (name, appearance, outfit), **Kit** (home/away colours via sliding scales, kit types, trim). **Logos** come as cyclable templates, and **the current team name is rendered inside the logo and auto-updates when you change it**. **Custom logo import** needs the **Custom Logo section unlocked** and a **URL to a 512×512 image**. **Kit import** uses the same URL-paste flow but demands a **specific png layout** (template provided); **shading and creases are applied by the game at run-time**. Deletion: Download → **Reset** for logos, **Delete** on Edit Kit for kits.
→ This explains the entire third-party kit-site category (dlskiturl, dlskits.mobi): they exist to supply URLs and correctly-laid-out 512×512 pngs.

### Multiplayer etiquette and limits
- **Emojis (360020938198):** 6 by default; extras are earned or purchased; **only 6 can be equipped at a time**; swap them in **My Profile (top right of the Main Menu) → Emojis**. **Emojis can be switched off entirely: gear (settings) → Game → Multiplayer Chat → OFF.**
- **Imported kits and logos are local-only (360021064298):** they are **not transferred across multiplayer matches**, so an opponent never sees them. FTG states this is not possible, without giving a reason.
→ Before investing in kit imports, note the audience is you alone in DLL.

### New failure class recorded
Article 360015150438 (DLS24 → DLS25 profile carry-over) returned **HTTP 200 with a Zendesk sign-in interstitial** — no article content. Unlike the Reddit/TikTok 403s, this block is a login wall behind a success status. **Rule: an HTTP 200 from support.ftgames.com does not prove an article was read**; the ledger entry keeps status and payload together so this cannot be mistaken for a visit.

### Monitoring
dlskiturl front page unchanged on the **thirteenth** check.

## TURN 30 (2026-10-05) — the FAQ index corrected our own coverage claim

### Correction: the first-party corpus is bigger than we said
The **FAQ category index** gives the site's own section counts: **Core Principles 1 · Parents' Guide 8 · General FAQs 21 · Dream League Soccer FAQs 52** · Score! Hero 24 · Ultimate Clash Soccer 43 · Score! Match 43 · 8 Ball Hero.
Earlier turns called our ~30-URL list "the complete official spine". It is not: **the DLS FAQ section alone holds 52 articles**, so coverage is roughly **30 of 52**. **That claim is retracted here.** The complete DLS section listing is now the priority fetch, because it is the only way to know what we have not read.
New titles surfaced by the index (all now on the frontier):
- DLS: `37082887837202 How do I find my User ID`, `360004717278 Can I use my DLS19 profile in DLS25`.
- General: `213853309 What languages are your apps available in`, `213689249 When is the next app update being released`, **`360001369698 Some game values and content have changed. Is this a bug?`** (potentially the first-party explanation for rating/stat drift between updates — directly relevant to our ±1 conflict set), plus two Google Play download-error articles.
- Parents' Guide: age limits (360000204889), refunds (360000205049), restricting in-app purchases (360000191385), purchase not received (360000205129), and **`360000191445 Other Sites Offering In-App products`** (relevant to the modded-currency risk already covered by the ban policy).
- Core Principles: `360009168377 Our Commitment to Fair Gaming` — the Zendesk copy of the page we read at ftgames.com/core-principles; worth checking for divergence.

### Smaller first-party captures this turn
- **Changing kit (7916959134737; assigned to the UCS Help Center section):** Main Menu → **My Club** → kit section edits your current **home and GK kit**. (The customisation article describes **home and away** — a small internal divergence, recorded as a gap rather than forced into agreement.)
- **Control button labels (14369944135058):** the in-match buttons read **"Low Kick", "Hard Kick", "Lofted Kick"** and similar; hide the text via **Game Settings → Display → Descriptive Button Text → OFF**, available in-game or from the Main Menu.
- **Device compatibility (214385685):** iOS — most devices, minimum OS varies by app; Android — **over 3,000 devices**, availability limited by hardware, carrier restrictions and territory legislation.
- **Mobile data (360005680437):** FTG strongly recommends Wi-Fi and limited mobile data because most features require being online (no figures; the ~2 MB per multiplayer match figure is from the multiplayer article).

### Monitoring
dlskiturl front page unchanged on the **fourteenth** check.

## TURN 31 (2026-10-05) — the live-service sentence that reframes the ±1 conflicts

### "Values change, and the change may be temporary" — article 360001369698
Verbatim: *"As our games are run as **live services**, we **regularly make changes to values or content** within the games, so in all likelihood if you've seen something changed then it's unlikely to be a bug. **Changes are made for a variety of creative, technical or business reasons, and can sometimes be temporary.**"*

**This is the most consequential single sentence we have for how to read the card databases.** Until now the ±1 cross-source OVR differences (conflict h) were carried as "third-party estimation error, plus a possible real difference". FTG now states in writing that published values move, deliberately, for creative/technical/business reasons, **and sometimes temporarily**. Therefore:
- A ±1 gap between two databases is **equally consistent with real value drift over time** as with estimation error, and the two **cannot be separated from outside the game**.
- The estimate-band rule stands unchanged as a rule, but its **cause is now explicitly open** rather than assumed.
- A historic player comment on the same page (7 years old) calls the currency **"buks"**, which supports reading the "bux" in article 17146555181585 as **legacy FTG terminology** rather than a live second currency (conflict n) — supporting context, not proof.

### First-party coverage: precisely stated, still open
The DLS FAQ section page rendered **30 titles**, while the category index advertises **52**. Four of the 30 are still unread: `360000220945 why can't I update the app`, `213851909 restart my career`, `37082887837202 find my User ID`, `360004717278 DLS19 profile in DLS25`. Up to **22 further titles are unaccounted for** because of the count discrepancy. The "complete official spine" claim stays retracted.

### Two smaller first-party checks
- **360009168377 Our Commitment to Fair Gaming** — a one-sentence pointer to ftgames.com/core-principles. **No divergence** from the page we already read; the check had one purpose and it returned a negative, which is worth having on record.
- **213689249 When is the next app update being released** — older duplicate; names **Twitter/X and YouTube** as the update channels, whereas **360000262229 names TikTok, Instagram and Facebook**. Two first-party channel lists that disagree. The substantive policy (FTG does not pre-announce updates) is **identical in both**, so the monitoring conclusion is unaffected.

### Languages (213853309)
**13 UI languages:** English, French, German, Italian, Spanish, Japanese, Dutch, Portuguese, Turkish, Korean, Chinese, Russian, Arabic. (UI translation is a separate fact from the Turkish/Arabic **commentary** noted in the store copy — adjacent, not identical.)

### Monitoring
dlskiturl front page unchanged on the **fifteenth** check.

## TURN 32 (2026-10-05) — coverage gap closed; the destructive control found

### The 30-vs-52 discrepancy is resolved: the section paginates
Page 2 of the DLS FAQ section renders **22 further titles**, so **30 + 22 = 52**, exactly matching the category index. **Every DLS FAQ title has now been seen; nine remain unread:**
`360003945917 What are facilities` · `360003945677 How can I expand my squad` · `214229005 Can I make an in-app purchase` · `360003945557 I can't connect to the game` · `19336294718098 What is Haptic Feedback` · `214385385 How do I change between Home and Away kits before a match` · `214385405 How do I watch my saved replays` · `213851469 Is there any way to view my team's stats` · `213851429 How do I change my nationality`.
The "complete official spine" claim stays retracted until those nine are read. **Facilities and squad expansion are the two highest-value of the nine** — they are core progression systems we have only seen through storefront marketing copy.

### Reset Profile — the irreversible control (article 213851909)
- The career restart is the **"Reset Profile" button**, marked with a **skull and crossbones symbol**, at **Settings (gear, top left) → Advanced**.
- **Consequences, verbatim in substance:** previous profiles held before the reset **cannot be recovered and the process cannot be undone**; **you lose all current progress including coins, gems and other consumables — and this includes in-app purchases**; **resets are limited to one every 30 days**.
- **A menu hazard worth stating plainly:** the *same* Settings → Advanced menu also holds **Link Profile**, **Manage Devices** and **System Info** — the protective controls and the destructive one sit side by side.

### Other captures
- **User ID (37082887837202):** Options → Advanced → **System Info** (the little "i") → **Copy Info**. FTG also states users must not loan, exchange, share, sell or buy profiles.
- **DLS19 → DLS25 (360004717278):** **No.** DLS25 is standalone; DLS19 profiles do not work in the latest DLS and **DLS19 in-app purchases do not transfer**.
- **Cannot update the app (360000220945):** iOS — close DLS, App Store → Updates → pull to refresh → locate DLS → Update (or search for DLS). Android — install via the Play Store website; try mobile data instead of Wi-Fi; clear Play Store cache and data; or remove, restart and re-add the Google account. **This is also the publisher's own procedure for when a store listing appears not to show the current version**, which is precisely the failure mode that could make our storefront version reading look stale when it is not.

### Monitoring
dlskiturl front page unchanged on the **sixteenth** check.

## TURN 33 (2026-10-05) — squad size is a facility upgrade; kit functions disambiguated

### Squad expansion (360003945677) — directly relevant to the rotation plan
- To gain squad space you must **upgrade the accommodation facility**: open the **"Stadiums & Facilities"** screen and tap **accommodation**.
- **"For each level this is increased, you can add more players to your squad."**
- **Consequence for the user's rotation plan:** squad size is **not a fixed cap** — it is a **spendable progression target**. A second XI is bought with facility levels, not granted. The per-level slot count **and the upgrade cost remain unknown** (first-party articles give neither).

### Facilities (360003945917)
- Facilities are **different buildings belonging to your club that grant unique bonuses** which help career progression. **That is the entire article** — no facility list, no bonus magnitudes, no costs. Marketing copy names facilities, but marketing is not a mechanics source, so the individual bonuses stay a **known-unknown**.

### Other captures
- **Shop / IAP (214229005):** tap your **coin or gem tally on any screen** to open the Shop. FTG adds "Please seek the bill payer's permission." **No prices anywhere in first-party text — pricing remains third-party-only.**
- **Home/Away kits (214385385):** on the **pre-match screen** (both lineups shown), **click the player models to cycle through the kits**. **This disambiguates the T30 kit divergence:** *editing* is My Club (home + GK, per 7916959134737); *selecting* on match day cycles home/away. Recorded as a scope clarification, not a harmonisation — whether an away kit is separately editable is still open.
- **Team stats (213851469):** **My Profile** (tap team/manager name, top right) → **Records** for lifetime stats; **Career** → tap a competition for current-competition stats.
- Monitoring: dlskiturl unchanged (**seventeenth** check).
- **DLS FAQ unread count now 4:** `360003945557` (can't connect), `19336294718098` (haptic feedback), `214385405` (saved replays), `213851429` (nationality).

## TURN 34 (2026-10-05) — the DLS FAQ section is now fully enumerated AND fully read (52/52)

**All 52 DLS FAQ titles are known and all 52 have been read.** This is the first block of the first-party corpus where both conditions hold. **It is not an exhaustion claim** — the General FAQs (21) and Parents' Guide (8) sections, the auth-walled articles and the blocked routes remain open.

### Captures
- **Connectivity (360003945557):** most modes need a connection; **mobile data or Wi-Fi both work**; **a stable connection is required for multiplayer**; and — importantly — **with no active internet connection you can still play exhibition matches**. This independently corroborates the earlier offline-Exhibition finding from a second first-party article.
- **Haptic Feedback (19336294718098):** vibrations emphasise certain actions (e.g. scoring). Toggle: **Options (gear) > Audio > Haptic Feedback** — note it lives under **Audio**, not Controls or Display.
- **Saved replays (214385405):** **My Profile > Highlights**.
- **Nationality (213851429):** **My Profile > click the flag near your manager**. No cost, limit or cooldown is stated; **absence of a stated limit is not evidence that none exists**.

### The My Profile menu, now mapped
Three separate functions sit behind **My Profile** (tap the team/manager name, top right): **Records** (lifetime stats), **Highlights** (saved replays), and the **nationality flag**.

### Help-centre structure, and one census question
The help-centre root renders only four section links: **DLS FAQs (203117809)**, **Score! Hero FAQs (203117609)**, **Ultimate Draft Soccer (7900693036561)**, **Score! Match FAQs (115001619089)**. **No General FAQs section id was rendered**, so that section's enumeration stays blocked for now.
**Open census question:** our family census covers DLS, Score! Hero, **Ultimate Champion Soccer (UCS)** and Score! Match. A section called **"Ultimate Draft Soccer"** appears here — either a rename of UCS or a distinct title. **Not resolved.**
- Monitoring: dlskiturl unchanged (**eighteenth** check).

## TURN 35 (2026-10-05) — netcode answered; a CORRECTION that touches existing DLS claims

### CORRECTION (read this first) — five "DLS" sources are actually Ultimate Clash Soccer articles
The **Ultimate Clash Soccer** section listing (43 articles) contains these article ids, several of which we have previously cited as DLS sources:
`7916959134737` (change kit) · `7917587319313` (change formation) · `7917423348497` (how do I get promoted) · `7917583876625` (change player roles) · `17146555181585` (sell players — the "bux" article).
Some of these ids also appeared in earlier listings we read as DLS, and Zendesk can surface one article under more than one section, so the honest status is **ATTRIBUTION UNCERTAIN, not "definitely UCS"**. **What follows must not be repeated as DLS fact until the attribution is settled:** the season-gating of formations, the promotion/relegation XP meter, the Player Roles sub-system, the home+GK kit route, and the "bux" sale reward.
**Turn-35 conflict framing was too strong and is withdrawn:** neither the "bux" article nor the kit article is proven UCS-only. Their UCS-section membership is confirmed, but the article body does not identify the product. The **bux-versus-coins direct contradiction is not established** by this evidence, and the kit scope remains unresolved. Both stay open; do not harmonise or label them as resolved.
*Turn 36 direct reads are complete; the bodies do not settle exclusive product attribution. Turn 37 should check Zendesk article metadata.*

### Census alias resolved; Turn-35 count correction
- **Ultimate Draft Soccer = Ultimate Clash Soccer.** The URL slug is stale; the section renders as Ultimate Clash Soccer. **Slugs are not evidence; page content is.**
- **Correction:** Turn 35 incorrectly described 8 Ball Hero as a newly discovered sixth title section. The Turn-30 category-index note already listed 8 Ball Hero. The total category census is not verified from the partial Turn-35 response (two tool chunks were returned and only chunk 0 was read). Do not use the sixth/new label.

### Help-centre structure now mapped (section ids unlock the rest)
Core Principles `360002602258` (1) · Parents' Guide `360000030369` (8) · **General FAQs `203171905` (21)** · DLS FAQs `203117809` (52) · Score! Hero `203117609` (24) · Ultimate Clash Soccer `7900693036561` (43) · Score! Match `115001619089` (43) · 8 Ball Hero `360000489137`.

### Netcode — the open gap is now filled, first-party
- Multiplayer is allowed only on **Wi-Fi or high-quality 5G/4G/3G**; some Wi-Fi (e.g. hotel public Wi-Fi) is unsuitable.
- **In DLL both players connect to FTG's cloud servers. The netcode is designed so the opponent's connection quality has no impact on your experience ⇒ lag-switch cheats are not effective, and your opponent is not told your network address, so DoS is hard.**
- If *you* lag, the problem is **between your device and their server — usually the last mile**. Avoid background downloads and other devices on the same router.
- **Data use ≈ 2MB per match** (approximate; varies with connection quality and match length). Bandwidth demand is low but the game is **sensitive to latency and packet loss**.
- **IPv6: yes. 5G: yes.** Tip: **Wi-Fi multiplayer runs more smoothly with Bluetooth disabled.**
- **No Facebook friend invites**, but **local multiplayer works on the same platform (Android↔Android, iOS↔iOS) on the same Wi-Fi router**.
- **Nuance to keep:** the article insulates you from *your opponent's* connection; it does not promise low latency on your own.

### Two different destructive controls — do not confuse them
| | **Reset Profile** (213851909) | **Delete Profile** (360017046578) |
|---|---|---|
| Path | Settings (gear) > Advanced | Main Menu > Settings (gear) > Advanced > **Delete (trash can)** > Delete Profile |
| Effect | Loses all progress incl. purchases | **Removes all profiles saved on the device, wiping it entirely** |
| Escape | none | **"Cancel Request" before the countdown ends** |
| Rate limit | **one per 30 days** | not stated |
Both live in the same Advanced menu, next to Link Profile and Manage Devices.

### Save-data transfer, confirmed cross-game
For **DLS, Ultimate Clash Soccer, Score! Hero and Score! Match**: link to **Sign in with Google** or **Sign in with Apple (iOS 13.0+)** via the login option in the game's settings — **not automatic**; without it FTG **cannot guarantee recovery** after uninstall, reset or device change. **Save data is NOT secured on Google Play Games or iCloud.** For retired games (DLS19): iCloud or Google Play Saved Games only, **no cross-platform transfer**, no Facebook or Game Center. **8 Ball Hero** uses Facebook.
- Monitoring: dlskiturl unchanged (**nineteenth** check).


## TURN 36 (2026-10-05) — attribution check and General FAQ enumeration

### Product-scope correction: five articles are listed under Ultimate Clash Soccer
Turn 35 established that the UCS section listing includes `7916959134737` (kit), `7917587319313` (formation), `7917423348497` (promotion), `7917583876625` (roles), and `17146555181585` (sell players / bux). Turn 36 directly reopened three article bodies:
- **7917423348497:** wins earn XP; reaching the current rank's maximum XP promotes; losses remove XP and can relegate. Its body does not name the game; related links include UCS-specific blocking and matchmaking pages and Season Points.
- **7917587319313:** Squad > formation-grid button; formation choices are limited by season (example: two in a season). Its body does not name the game; its related links include a DLS19 legacy help page.
- **17146555181585:** players outside the Starting 11 can be sold if the required squad size is maintained; the reward is a specified amount of bux. Its body does not name the game; related links include UCS-specific gameplay and career-reset pages.

**Turn 37 resolves the canonical Help Center assignment:** all five article JSON records return `section_id: 7900693036561`, the Ultimate Clash Soccer section. The earlier claim that these are DLS section sources is withdrawn. These records have no DLS-version stamp or separate product field; their canonical Help Center classification is UCS, so do not use them as DLS-specific evidence. The sale-reward and home/GK kit discrepancies are not established DLS-internal contradictions on this evidence. Cross-product reuse is not documented.

### General FAQs — title enumeration complete, article reading still partial
The section `203171905` renders all 21 titles on page 1. `?page=2` renders `_empty` and links back to the section root. **21/21 titles enumerated; this is not 21/21 articles read.** The listing contains both general support and legacy-game material. The page's full title list:
1. `213853309` — What languages are your apps available in?
2. `214387685` — How do I backup/restore/transfer my save data?
3. `213689249` — When is the next app update being released?
4. `214388065` — Why does it say on the Google Play Store that my device is incompatible with the app?
5. `214388105` — I keep getting an error message when I try and download the app from the Google Play Store, how do I fix it?
6. `360001369698` — Some game values and content have changed. Is this a bug?
7. `115003073485` — Why aren't your apps available on other platforms?
8. `360017046578` — How do I have my personal data deleted?
9. `213853729` — Is it possible to use a Bluetooth controller with your apps?
10. `213853769` — Why do I keep seeing a black screen with grey buttons called Safe Mode?
11. `37352328553106` — How do I find my User ID in your game?
12. `360009450097` — How do I setup a "Sign in with Apple" account?
13. `9580096555281` — How do I setup a "Sign in with Google" account?
14. `360000603398` — How do I setup a Google Play Games account?
15. `360000613657` — How do I setup an iCloud account?
16. `360001099097` — Can I use your games in my videos?
17. `214387905` — Why can't I download Dream League Soccer - Classic?
18. `214421705` — How do I customise my kit in Dream League Soccer - Classic?
19. `213853689` — Why can't I download First Touch Soccer 15?
20. `213892809` — How do I customise my kit in FTS 15?
21. `360000309705` — I can't find my answer here, how can I contact you?
The index does not establish article content. The FTS 15 kit page `213892809` remains excluded under the standing different-game rule.

### Correction to the Turn-35 title census
8 Ball Hero was already present in the Turn-30 category-index note, so Turn 35 did not newly discover it and the "sixth title section" wording is withdrawn. The full category census is still not certified from the partial two-chunk Turn-35 category render.

### Monitoring
The dlskiturl home page is unchanged on the **twentieth** check: same nine items, none October-dated.


## TURN 37 (2026-10-05) — Zendesk metadata resolves canonical source section

### Five disputed articles are assigned to the Ultimate Clash Soccer Help Center section
The public Zendesk article JSON for **all five** returns `section_id: 7900693036561`, which the rendered section page identifies as **Ultimate Clash Soccer**. This resolves their canonical Help Center placement; it does not create a DLS version stamp. The API supplies an article title, body, `section_id`, and update timestamp, but no independent `product_id` or DLS version field.

| Article ID | Title | `updated_at` | Section assignment |
|---|---|---|---|
| `7916959134737` | How do I change my kit? | 2026-09-25 | Ultimate Clash Soccer |
| `7917587319313` | How do I change my formation? | 2026-07-09 | Ultimate Clash Soccer |
| `7917423348497` | How do I get promoted? | 2026-07-09 | Ultimate Clash Soccer |
| `7917583876625` | How do I change my player roles? | 2026-07-09 | Ultimate Clash Soccer |
| `17146555181585` | How do I sell players? | 2026-09-10 | Ultimate Clash Soccer |

**Correction to earlier DLS attribution:** treat these as UCS-section support articles, not DLS-specific evidence. The five old DLS claims are removed as DLS claims: season-limited formations; XP-based promotion/relegation; the Roles screen; the My Club home/GK kit-edit route; and the bux sale reward. This does not prove FTG never reuses generic guidance across games; it means this corpus contains no DLS-specific provenance for these claims.

**Conflict impact:** the bux sale reward is from the UCS section, while the DLS-specific sale article `360003945617` (version 12200 onwards) says a coach is received. Do not count this as a DLS internal contradiction. The earlier `bux`/`coins` and sale-reward contradiction labels require re-audit; the prior lower bound of “at least six FTG self-contradictions” is no longer safe to repeat until the remaining items are rechecked. The home/GK kit-edit route is also UCS; DLS pre-match home/away selection in `214385385` is a separate documented action, not contradicted by this UCS page.

### Monitoring
The dlskiturl front page is unchanged on the **twenty-first** check: same nine items and no newer visible post than the prior check.


## TURN 38 (2026-10-05) — General FAQ article reading: compatibility, controllers, and sign-in

### Google Play compatibility and download support
- **214388065 — device marked incompatible:** FTG lists graphical limitations/incompatible chipset, country restrictions, and carrier restrictions as possible reasons. Clearing Google Play Store data may help; if it does not, the article says there is no other workaround. General support text; no DLS-26 version stamp.
- **214388105 — Play Store download error:** try the Play Store website; try downloading/updating over mobile data with Wi-Fi disabled; clear the Play Store cache and data; remove the Google account, restart, re-add it, and retry; contact Google if unresolved. General support text; no DLS-26 version stamp. This download workaround is not a recommendation for mobile-data gameplay.

### Controller compatibility
- **213853729:** FTG says its apps support some Bluetooth controllers, but it cannot guarantee every brand. It names no tested controller model and is not a DLS-26-specific device list.

### Cloud-account setup (security distinction retained)
- **360009450097 — Sign in with Apple:** a cloud-saving feature using Apple ID; **not iCloud**, though iCloud must be set up with the same Apple ID. Apple ID must have two-factor authentication. **DLS path in the article:** Settings cog (top left) > Advanced > toggle Sign in with Apple to Connected using either arrow. Play a few matches to ensure upload; stable Wi-Fi recommended. Score! Match has a separate path. No DLS version stamp.
- **9580096555281 — Sign in with Google:** cloud saving uses a Google account and **is not Google Play Games**. Create an account if needed, then sign in on FTG games wherever the Sign in with Google option appears. The article gives no DLS-specific settings path and no version stamp.
- These first-party setup pages support the existing distinction: **Sign in with Apple/Google is not iCloud/Google Play Games save-sync**. Do not infer automatic upload; use the settings link and allow the game to upload.

### General FAQ coverage and monitoring
- The General FAQs section remains **21/21 titles enumerated**; the ledger now records **10/21** article bodies read. Enumeration is not content-completion or exhaustion.
- dlskiturl home page unchanged on the **twenty-second** check: same nine front-page items, no new October-dated item.


## TURN 39 (2026-10-05) — General FAQ articles: platform, safety, and cloud-save conflict

### Remaining general support articles sampled
- **115003073485 — platform availability:** FTG says it had no plans at that time to release on PC or Windows Phone. The rendered article has no date/version stamp; this is not a current 2026 platform announcement.
- **213853769 — Safe Mode:** tap Exit Safe Mode; if the issue persists, contact FTG. No reason or version-specific explanation is provided.
- **37352328553106 — User ID hub:** warns against loaning, exchanging, sharing, selling, or buying game profiles and says not to share personal details with other users. It links to separate User ID instructions for DLS, Score! Match, Ultimate Clash, and Score! Hero. DLS-specific article ID 37082887837202 was already read in the DLS FAQ sweep.

### First-party contradiction: DLS save data vs Google Play Games and iCloud
These are **three conflicting first-party support articles**, all without a version stamp. Preserve both sides; do not harmonize or assume which route is current:
- **214387685 (cross-game backup/restore/transfer):** says DLS, UCS, Score! Hero, and Score! Match save data is not secured on Google Play Games or iCloud, describing these as different services not used by the games; recommends linking the profile with Sign in with Google or Sign in with Apple instead.
- **360000603398 (Google Play Games account setup):** explicitly instructs DLS users to Main Menu > Options > Game Settings > Advanced, enable **Google Play Games Services** and **Google Play Cloud**, then make game progress online (preferably Wi-Fi) to upload save data.
- **360000613657 (iCloud account setup):** explicitly instructs DLS users to Main Menu > Options > Game Settings > Advanced Settings, enable **iCloud**, play a few matches to upload, and check iCloud storage for the app.

This is a real documentation conflict about DLS backup services, not a fact we can resolve from unstamped web copy. The distinct names **Sign in with Google** vs **Google Play Games**, and **Sign in with Apple** vs **iCloud**, remain distinct services; that does not settle whether older DLS builds support the latter backup toggles. The metadata route proposed for Turn 40 can establish article-section/update dates but cannot supply a missing game version. For the user's actual save, ask which controls are visible; do not direct a change based on either article alone.

### General FAQ coverage and monitoring
- General FAQs: **21/21 titles enumerated**; article bodies read now **15/21** per the reconciliation output. This is partial content coverage, not exhaustion.
- dlskiturl front page unchanged on the **twenty-third** check: same nine items; no new October-dated item.


## TURN 40 (2026-10-05) — metadata dates clarify, not resolve, the save-route conflict

### Zendesk metadata: section, edit/update dates, and status
| Article | Section ID | Created | `edited_at` | `updated_at` | `outdated` |
|---|---:|---|---|---|---|
| `214387685` backup/restore/transfer | `203171905` General FAQs | 2016-12-07 | 2024-05-15 | 2026-09-28 09:53Z | false |
| `360000603398` Google Play Games setup | `203171905` General FAQs | 2018-11-26 | 2020-06-04 | 2026-07-19 08:27Z | false |
| `360000613657` iCloud setup | `203171905` General FAQs | 2018-11-26 | 2020-06-04 | 2026-07-19 08:27Z | false |
| `4413273241873` DLS save data/transfer | `203117809` DLS FAQs | 2021-12-09 | 2024-12-06 | 2026-09-28 19:25Z | false |
These are Zendesk metadata dates, **not DLS version stamps**. `updated_at` and `edited_at` differ; do not treat either field, nor `outdated=false`, as proof that an instruction matches the current DLS build.

### Save-route conflict remains unresolved
The records confirm all three disputed account articles are in the General FAQs section, while `4413273241873` is in the DLS FAQs section. The DLS-specific page `4413273241873` describes Manage Devices/Link Profile under Options > Advanced, Google sign-in for Android, Apple sign-in for iOS, and code transfer (only if the old device is accessible; the generated code cannot be used on the device that created it). It warns that signing out of Apple/Google unlinks the profile and risks loss after uninstall/device change.

The conflict is not safely dismissed as merely an old article: the two setup pages are marked `outdated=false` and have `updated_at` metadata in July 2026, while their `edited_at` is 2020; the cross-game backup page and DLS-specific save-data page have September 2026 `updated_at` metadata and later `edited_at` values. The site gives no version applicability. Keep the three bodies side by side:
- `214387685`: DLS saves are not secured on Google Play Games or iCloud; those services are not used by the games.
- `360000603398`: DLS setup says to enable Google Play Games Services and Google Play Cloud and play online to upload.
- `360000613657`: DLS setup says to enable iCloud and play matches to upload/check iCloud storage.

Do not harmonize these, infer which UI the user has, or recommend toggling a save setting from web copy alone. Ask which options are visible in the user's own DLS Settings/Advanced screen if needed.

### Gameplay-video guidance — official article body only
Article `360001099097` generally permits fan gameplay footage subject to non-commercial use, no recorded game music, no implication of FTG sponsorship, narrow descriptive trademark use, no mixing publishers or repurposing/splitting game content, EULA compliance, no false implication of an unpublished sequel/update, and non-offensive content. FTG reserves action and says use is at the creator's risk. The fetched page also rendered old player comments; **they are excluded as current-state evidence**, and the second comments chunk was not fetched.

### General FAQ coverage and monitoring
- General FAQ titles: 21/21 enumerated. Article bodies read: **16/21** from the reconciliation output.
- dlskiturl front page unchanged on the **twenty-fourth** check.


## TURN 41 (2026-10-05) — General FAQ reading nearly complete; legacy scope and Super Players

### General FAQ article bodies
- **360000309705 — contact:** submit a support request with details; alternatively search or post in the community forum for peer help.
- **214387905 — Dream League Soccer Classic download:** Classic was removed from stores for strategic reasons and is unavailable to new users. Existing-user recovery links are provided; the article says old 32-bit apps do not run on iOS 11 or later. This is a legacy product, not DLS26.
- **214421705 — DLS Classic kit:** describes a PNG template (shirt, sleeves, shorts, socks), adding logos to the image, runtime shading/creases, importing via Edit Kit > Import Kit from a direct hosted PNG URL, and logo URLs up to 512x512. This is DLS Classic only, not DLS26.
- **213853689 — FTS 15 download:** FTS 15 was removed from stores for strategic reasons and is unavailable to new users; the page gives existing-user recovery links and repeats the iOS 11/32-bit limitation. Different game, not DLS26.

### New first-party lead: Super Players
Article **360017063617** says Super Players are enhanced player types, earned from Events and sometimes rarer packages; they appear less often than standard players and have a grey or gold shiny background. The body does not name a title or version. **Do not treat this as DLS26 card-tier evidence or overwrite the current card ladder.** Check the article's API `section_id` and metadata before assigning a game. Related lead: `360000001969` “What does each player type do?”

### General FAQ coverage and monitoring
- Section 203171905 remains **21/21 titles enumerated**; article bodies read: **20/21** per the reconciliation output. The only remaining unread listed body is the FTS15 kit article `213892809`, intentionally excluded under the standing different-game rule.
- dlskiturl home page unchanged on the **twenty-fifth** check: same nine items, no new October-dated item.


## TURN 42 (2026-10-05) — Score! Match attribution and player-type scope resolved

### Super Players and player-type FAQ are Score! Match sources, not DLS
Zendesk JSON metadata returns **`section_id: 115001619089` (Score! Match FAQs)** for both:
- **360017063617 — What are Super Players?** `created_at` 2021-01-20; `edited_at` 2021-01-20; `updated_at` 2026-07-09; `outdated=false`. Body: enhanced player types won in Events and occasionally rarer packages, lower frequency than standard players, grey or gold shiny background.
- **360000001969 — What does each player type do?** `created_at` 2018-01-15; `edited_at` 2018-01-30; `updated_at` 2026-07-09; `outdated=false`. Body: player types specialize (height/air play, dribbling, creative passing); tap in squad menu for an attribute breakdown.

**Correction to Turn 41:** product scope is no longer unknown. Both pages are canonically assigned to the Score! Match section; they are not DLS evidence. Do not compare the grey/gold Super Player appearance to DLS26’s card ladder or use the player-type description to explain DLS attributes. The Zendesk section assignment is not a DLS build/version stamp.

### Unscoped Gem and network support articles
- **360000002405 — purchase Gems:** tap the plus beside the Gem balance to reach Store packages; purchases cost real money and FTG says to seek the bill payer’s permission. The body names no game/version and gives no price table or rates. Its product section remains unverified.
- **360000420025 — connection issues:** disable VPN; seek stronger 4G/5G signal; on Wi-Fi move near the router, reset it, or try another connection. It also describes platform-specific steps to set DNS to `8.8.8.8` and toggle Airplane mode for five seconds. Turn 43 API metadata assigns it to Score! Match FAQs section `115001619089`; this is not DLS-specific network guidance. Do not advise changing this user's settings from that page.
- Turn 43 API metadata resolves both pages to the Score! Match FAQs section; related-page leads remain product-scoped accordingly.

### General FAQ coverage and monitoring
- General FAQ titles remain **21/21 enumerated**; bodies read **20/21** per the reconciliation output.
- dlskiturl unchanged on the **twenty-sixth** check.


## TURN 43 (2026-10-05) — Parents’ Guide enumerated; gem and connection sources reattributed

### Product-scope correction from Zendesk metadata
Both articles that Turn 42 had kept unscoped now return `section_id: 115001619089`, the **Score! Match FAQs** section:
- `360000002405` How do I purchase Gems? — created 2018-01-15; edited 2021-01-20; updated 2026-09-24; `outdated=false`.
- `360000420025` I keep having connection issues, what can I do? — created 2018-03-09; edited 2021-01-20; updated 2026-08-24; `outdated=false`.
These are Score! Match articles, not DLS Gem-price or DLS network evidence. The metadata contains no DLS build/version.

### Parents’ Guide title enumeration and two article reads
Section `360000030369` renders all **8/8** advertised article titles on this page:
1. `360000204889` — What are the Age Limits and General Policies for our Apps?
2. `4408249822609` — Age Confirmation & Personal Ads and Notifications
3. `360000205049` — How to get a refund on an in-app purchase
4. `360000191385` — How to restrict in-app purchases
5. `360000205129` — In-app purchase not received
6. `360000191445` — Other Sites Offering In-App products
7. `360000191485` — In-App Chats
8. `360000191545` — Contact Details

- **360000191445:** warns third-party “free gems” or “unlimited currency” offers may take money or personal information without delivery. Says the safest purchase route is within the game on mobile; selling, redeeming, or trading virtual currency outside the game is prohibited by FTG Terms. General Parents’ Guide scope; no DLS version.
- **360000205129:** first confirm purchase history shows Charged; Cancelled or Payment Declined means it did not process. If charged, restart with strong internet, reopen the game, enter the Shop to trigger validation, then contact FTG if still missing. General Parents’ Guide scope; no DLS version.
- At the end of Turn 44, **7/8** Parents’ Guide article bodies have been read; `360000191485` (In-App Chats) remains unread. Title enumeration is complete, but article-body coverage is not.

### General FAQ coverage and monitoring
- General FAQ titles remain **21/21 enumerated**; bodies read **20/21** per the reconciliation output.
- dlskiturl unchanged on the **twenty-seventh** check.


## TURN 44 (2026-10-05) — Parents’ Guide policy and purchase-safety sweep

### Five more Parents’ Guide articles read
These are general, unversioned FTG help pages; they do not establish DLS26-specific behavior or current operating-system menus.

- **360000191385 — restrict in-app purchases:** Apple section describes requiring account authentication or disabling in-app purchases through Screen Time; Android section describes Google Play purchase authentication, including “all purchases”, “every 30 minutes”, and “never”. The article cautions that disabling authentication can permit unauthorized purchases and leave charges to the account holder. Do not copy its dated menu paths as verified current instructions or change the user’s settings without consent.
- **360000205049 — refunds:** FTG says it cannot issue Apple refunds and directs users to Apple. For Google Play, it directs the user to purchase history and “Report a problem”; if Google refers them to FTG, use the support form and include the reason and receipt. Store flows and eligibility were not independently checked; not a guarantee of refund.
- **360000204889 — age/general policy:** states FTG games are made/offered to people at least 13, that app-store maturity ratings refer to game content, and links Apple/Google parental-control pages. This is a general policy statement, not a verified DLS26 store rating.
- **4408249822609 — age confirmation/personal ads and notifications:** says age banding is selected on first download; younger bands receive the same ad volume but less-personalized ads, no personalized alerts/promotions/offers, and can still receive general offers/gameplay notifications. It says disabling personalization makes ads more generic rather than removing them; the youngest age band cannot enable personalization. The page also says to contact support with the User ID for a birthday-related age-band change, despite describing first-download selection as not user-changeable. No DLS26 build or menu label was verified.
- **360000191545 — Contact Details:** says FTG provides no phone support and recommends its support form; sensitive billing details should go through the form, not a public forum.

Parents’ Guide section remains **8/8 titles enumerated**; body coverage is **7/8**. `360000191485` (In-App Chats) is the one unread body.

### Monitoring and coverage
- dlskiturl unchanged on the **twenty-eighth** check: same nine front-page items, no new October-dated item.
- General FAQ titles remain **21/21 enumerated**; bodies read **20/21** per reconciliation output. FTS15 article `213892809` remains intentionally unfetched.
- Correction: DLS articles `360017166918` (video clips) and `9804887423121` (Facebook Login) had already been read as page-138 and page-152 before Turn 44; the Turn-44 handoff incorrectly described them as new. Turn 45 did not refetch their bodies; it fetched API metadata only.


## TURN 45 (2026-10-05) — Parents’ Guide closed; DLS metadata verified

### Parents’ Guide completion
Article `360000191485` (In-App Chats) body says FTG apps do not use **private chat facilities**. This is not a claim that the games have no preset reactions/emojis or other interaction. Zendesk metadata assigns the article to Parents’ Guide section `360000030369`; created 2018-02-02, edited 2018-02-05, updated 2026-06-16, `outdated=false`, with no game/version stamp. With this body, Parents’ Guide coverage is **8/8 titles enumerated and 8/8 bodies read**. Its generic text is not DLS26-specific.

### DLS FAQ metadata checks
- `360017166918` (“I am not seeing any video clips…”) belongs to DLS FAQs section `203117809`; created/edited 2021-01-20; updated 2026-07-16; `outdated=false`. The body is already recorded under Turn 26 and was not re-fetched. It says ad-network availability and limits are provider-controlled and no video-clip/reward-doubler frequency is promised; it also discusses LAT and troubleshooting. No DLS26 build/version is named.
- `9804887423121` (“Removal of Facebook Login from DLS”) belongs to DLS FAQs section `203117809`; created 2022-10-12; edited 2024-12-06; `updated_at` 2026-10-05 13:54:05Z; `outdated=false`. The known body says old Facebook-stored profiles cannot be recovered and recommends Sign in with Apple (iOS 13+) or Google. The metadata timestamp is current-day, but `edited_at` remains 2024; do not infer that the text changed today.
- Age-confirmation article `4408249822609` is in Parents’ Guide section `360000030369`; created/edited 2021-09-30; updated 2024-02-07; `outdated=false`. This is unversioned, general FTG guidance, not verified DLS26 menu behavior.

### Handoff correction and monitoring
- Turn 44 handoff mistakenly called the video-clips and Facebook Login articles “new DLS-specific leads.” The ledger shows they were already visited as page-138 and page-152. Turn 45 appropriately fetched only their previously unvisited API metadata URLs; no duplicate article-body retrieval.
- dlskiturl unchanged on the **twenty-ninth** check: same nine items, no new October-dated item.
- General FAQ titles remain **21/21 enumerated**; bodies read **20/21** per reconciliation output. FTS15 article `213892809` remains intentionally unfetched.


## TURN 46 (2026-10-05) — DLS metadata sweep and User ID product split

### Metadata for already-read DLS support articles
Turn 46 checked the ledger before retrieval: bodies for `360008904718` (blocked from DLS), `360004717278` (DLS19 profile in DLS25), and `360005680437` (mobile data) were already read. Their article bodies were **not** fetched again; only API metadata was retrieved.

- **360005680437 — mobile data:** DLS FAQs section `203117809`; created 2020-02-11, edited 2022-12-02, updated 2026-07-13, `outdated=false`. Body says most DLS features require online access, recommends Wi-Fi and limiting mobile data, and links Apple/Android data-usage instructions. No DLS26 build or measured data-use rates.
- **360008904718 — blocked from playing DLS:** DLS FAQs section `203117809`; created 2020-05-18, edited 2021-08-21, updated 2026-09-26, `outdated=false`. Says Apple App Store/Google Play are the authorized DLS sources and rejects modded APKs, external hacks, and exploitative bugs. It says contact support only for an incorrect flag and that bans are not lifted on request absent an error. No DLS26 build stamp.
- **360004717278 — DLS19 profile in DLS25:** DLS FAQs section `203117809`; created 2020-01-09, edited 2024-12-06, `updated_at` 2026-10-05 02:15:31Z, `outdated=false`. Body says DLS25 is a separate standalone game and DLS19 profiles/purchases do not transfer into it. It does **not** establish DLS25-to-DLS26 transfer behavior. Current-day `updated_at` is not proof of a new text edit.
- **37082887837202 — DLS User ID:** DLS FAQs section `203117809`; created/edited 2026-07-09; updated 2026-10-03; `outdated=false`. Body route: open DLS → Options gear (top left) → Advanced → System Info (i) → Copy Info. Warns against sharing personal details with other users or exchanging/trading profiles. This matches the previously read page-172.
- **37083387788434 — separate Score! Match User ID article:** Score! Match FAQs section `115001619089`; created/edited 2026-07-09; updated 2026-10-03; `outdated=false`. Its different route is Score! Match → blue gear on main menu → information → Copy To Clipboard. Do not confuse its UI steps with DLS.

### Scope and completeness
- All five Zendesk records are not marked outdated, but none adds a DLS26-specific build/version stamp. The Score! Match duplicate is explicitly excluded as DLS evidence.
- Parents’ Guide remains **8/8 titles and bodies**; General FAQs remain **21/21 titles and 20/21 bodies**. `213892809` remains intentionally unfetched.
- dlskiturl unchanged on the **thirtieth** check: same nine front-page items, no new October-dated item.


## TURN 47 (2026-10-05) — Score! Match scope corrections; DLS graphics article; save-ID typo

### Three previously unvisited “player type/currency” Help Center records
Zendesk API metadata resolves all three to **Score! Match FAQs section `115001619089`**, not DLS:
- `360000011145` (free currency): created 2018-01-16; edited 2018-02-12; updated 2026-07-09; `outdated=false`. The body explicitly names Score! Match: Bux/Gems from Packages, extra Bux via Video Packages/ads, which appear occasionally.
- `360000002205` (unlock player types): created 2018-01-15; edited 2018-01-30; updated 2026-09-10; `outdated=false`. Packages, per-Arena limits, and Arena-cover info are Score! Match mechanics.
- `360000250309` (where to see player types): created/edited 2018-02-09; updated 2026-07-09; `outdated=false`. Body gives Score! Match Squad → Captain → Customise → green player button.
Do not use any of these as DLS free-currency routes, player-acquisition rules, or role instructions.

### DLS graphics Help Center article
`360000598437` belongs to DLS FAQs section `203117809`; created 2018-11-20; edited 2021-12-09; updated 2026-07-22; `outdated=false`. Its unversioned body says Android only: Options → Advanced → Graphics Options. It describes FPS and quality settings, hardware dependence, a 30-FPS cap in low-battery/power-saving conditions, and troubleshooting; safe mode after three immediate launch/shutdown cycles is offered to revert graphics settings if the game will not run. No DLS26 build stamp; verify the user's device/menu before giving actionable steps.

### Broken save-data URL distinction
The unvisited candidate URL with article ID `441327324187` rendered FTG’s “page you were looking for doesn’t exist” message. `fetch_page` reported overall success but exposed no numeric HTTP code; the ledger therefore records the exact HTTP status as unknown, not guessed. This is **not** the different, previously read DLS save-data article `4413273241873`; do not merge them.

### Monitoring and coverage
- dlskiturl unchanged on the **thirty-first** check: same nine front-page items, no new October-dated item.
- General FAQ titles remain **21/21 enumerated**, bodies read **20/21**. Parents’ Guide remains **8/8 titles and bodies**. FTS15 article `213892809` remains intentionally unfetched.


## TURN 48 (2026-10-05) — Current storefront/publisher pages and event-state caveats

### Google Play listing (DLS package `com.firsttouchgames.dls7`)
The listing identifies Dream League Soccer 2026 by First Touch Games Ltd.; says Contains ads and in-app purchases; shows 100M+ downloads, Everyone, in-game purchases including random items, and “Updated on Sep 14, 2026”. Its store description markets 4,000+ licensed players, 8 divisions, 10+ cups, Dream League Live, Clans, facilities, Coaches, ads and an internet requirement. This is publisher/store copy, not proof of every feature’s current in-game implementation, and the returned render has no app version number. Review count conflicted within the two chunks (15M vs 14.4M); disregard it.

Chunk 1 also shows a Google Play event teaser with “Ends on 10/14” and “The names the fans remember, from their peak years”; this render did not reveal the event name. The listing’s late-summer update text says the Cult Heroes collection is “coming soon” and mentions bug fixes. Treat that phrase as potentially stale listing copy, not proof of current event availability or a date. Event-details ID `4830045897422713648` remains an unvisited lead.

### Google Play Data Safety (developer-provided disclosure)
The page explicitly cautions that practices may vary by app version, use, region, and age. It lists approximate location, device IDs, purchase history, crash logs/diagnostics as data shared in some contexts; collected categories include app interactions/actions, approximate location, optional device IDs, user IDs, purchase history, crash logs, and diagnostics. It says data is encrypted in transit and deletion can be requested. These are developer-provided store disclosures, not independently verified runtime behavior or a privacy audit.

### Apple event card and FTG publisher site
- Apple’s “English League Classics” event card says users can relive glory days and unlock top players in a Prize Ladder. A single render displays both **“EVENT ENDED”** and **“LIVE EVENT”**; no event date or player list appears. State is internally inconsistent; do not infer the current schedule from it.
- FTG’s undated generic Games page describes DLS as 4,000+ FIFPRO players, 8 divisions, 3D motion capture, commentary, and team customisation. It links Google Play package `com.firsttouchgames.dls7` and App Store numeric ID `1462911602`, while its Apple anchor labels the app “Dream League Soccer 2020” and the current Apple event page labels it DLS 2026. This is a legacy publisher-page title mismatch, not evidence of two different app IDs or a current DLS26 feature list.

### Recovery, monitor, and coverage
- Turn opened at local HEAD `fb9a2c0` with all project files untracked. Safeguarded the worktree (5,938,573-byte tar excluding `.git`), fetched the correct branch, reset to remote `09c31e1`, and compared 197 regular files; every backed-up file was byte-identical after repair. No content lost, no force-push; occurrence #10 recorded under ISSUE-0014. Only the current-turn clock was dirty after repair.
- dlskiturl unchanged on the **thirty-second** check: same nine front-page items, no new October-dated item.
- General FAQ titles remain **21/21 enumerated**, bodies **20/21**; Parents’ Guide remains **8/8 titles and bodies**. No exhaustion declaration.


## TURN 49 (2026-10-05) — database family check and first privacy-policy chunk

### DLSInside and DreamKitsApp: one family, not independent confirmation
- DLSInside root reports version name 13430, version code 160, last update 2026-09-16; 14,435 players, 263 teams, and 255 stadiums. It lists category counts including 12 Cult Heroes, 8 World Cup Champions, 8 World Cup Heroes, 40 Dynamic Stars, 11 Team of 2025, 2 Kickoff Stars, 12 Champions, 23 Stars, 32 Classics, 270 Hidden and 7,388 Exclusives. These are site claims, not FTG-confirmed totals; repeated values in one rendered page are not independent corroboration.
- DreamKitsApp’s DLS26 player index explicitly warns that its ratings are approximate calculations, may differ from in-game ratings, and can affect prices. Treat its displayed OVRs/prices as estimates. The index does not show an update date in the fetched page.
- The sites cross-link one another, consistent with the standing rule that **DLSInside and DreamKitsApp are one source family**. Do not count them as two independent confirmations.

### FTG Privacy & Data Policy — partial read only
The requested HTTP URL rendered at HTTPS. Policy heading says **Last Updated: 13 February 2026** and applies generally to FTG games/online services. Chunk 0/5 describes possible collection of device ID/name, preferences, gameplay progression/currency/activity/ad-view statistics; support contact information; advertising-network/device/network/locale/IP/advertiser-ID data depending on permissions; analytics including user ID, sessions, purchases, coarse location, ads viewed/clicked and crash data; and social login data if used. This is generic policy language, not proof every field is collected from every DLS26 player. Only chunk 0 of 5 has been read; remaining sections are open.

### Failed retrievals and stale-lead correction
- Reddit DLS26 midseason thread: HTTP 403; no body retrieved.
- FTG support landing page: HTTP 500; no body retrieved.
- The T48 handoff incorrectly called Google Play eventdetails `4830045897422713648` unvisited; the reconciled ledger shows it was already fetched as `page-009-googleplay-cult-heroes-event`. No duplicate fetch. The US Apple Cult Heroes card, DLSKitURL Cult Heroes article, DLSInside Cult Heroes page, and SakibPro Cult Heroes article were also already visited; annotated frontier duplicates were normalized away.
- dlskiturl unchanged on the **thirty-third** check: same nine front-page items, no new October-dated item.
- General FAQs remain **21/21 titles, 20/21 bodies**; Parents’ Guide remains **8/8 titles and bodies**. No exhaustion declaration.

### Git recovery
Turn opened at `fb9a2c0` with all project paths untracked. Safeguarded tree excluding `.git`, fetched/reset to remote `14914bd`, and byte-compared 198 regular files: all identical. No content lost, no force-push. ISSUE-0014 occurrence #11 is recorded.


## TURN 50 (2026-10-05) — FTG Privacy Policy fully read; DLSInside roster render failed

### FTG Privacy & Data Policy (last updated 13 February 2026)
All five chunks were read. The policy applies generally to FTG games and online services; it does **not** show that every described category is collected from every DLS26 player or in every region/version.

- It says FTG may collect device ID/name, preferences and gameplay statistics (progress, virtual-currency balances, activity such as purchases/ad views); support contact data; advertising data from third-party networks subject to permissions; and analytics such as user ID, device/OS, attempts/results, session times, virtual-item purchase/spend, coarse location/time zone, install source, ad views/clicks and crash/defect data.
- It describes use for gameplay/service operation, analytics, support, user acquisition and IAP monetization; possible targeted ads and temporary personalized offers. It says users confirmed under 16 are not segmented for those IAP promotions. Ads may provide in-game benefits. It names third-party ad/user-acquisition and analytics providers; do not assume every named provider serves this particular user.
- The policy says targeted-ad and personalized-notification opt-outs are available via device privacy or in-game Options; promotional personalization can also be disabled in-game. Targeted-ad opt-out prevents sharing the Advertiser ID. It also says profile/personal-data deletion can be requested from each game’s Options menu, and lists access, correction, deletion/objection, portability and complaint rights.
- The policy describes automated detection of suspected cheating by comparing virtual-currency/content levels against completed gameplay/purchases. It says possible actions include more ads, more frequent matching with suspected cheaters, and blocking; for a block it describes notification and a right to human intervention/contest. This is generic policy text, not confirmation of a DLS26-specific detection implementation or an inference about this user.
- The California/CCPA section says FTG disclosed/sold personal information to third-party ad networks in the prior 12 months and lists access/deletion/opt-out rights. Keep that statement in its California-specific context; it is not a Bangladesh legal conclusion.
- Policy also describes data retention, under-13 restrictions, security and international transfers. No region- or DLS26-version-specific collection matrix was established.

### DLSInside World Cup Champions category page
The category page title says Dream League Soccer 2026, but names/cards did not render; only unlabelled numeric entries `16, 6, 10, 23, 24, 3, 5, 2` appeared. Do not interpret them as player identities, OVRs, positions or IDs. The DLSInside/DreamKitsApp family remains one non-FTG source family.

### Recovery, monitor and coverage
- Turn opened at `fb9a2c0` with all project paths untracked. Backup/fetch/reset to remote `3bde4fc`; byte comparison verified **199 files identical**. No content loss or force-push. ISSUE-0014 occurrence #12 recorded.
- dlskiturl unchanged on the **thirty-fourth** check: same nine front-page items, no new October-dated item.
- General FAQs: **21/21 titles, 20/21 bodies**. Parents’ Guide: **8/8 titles and bodies**. No exhaustion declaration.


## TURN 51 (2026-10-05) — category archives and partial secondary career guide

### DLSKitURL archives
- The DLS 26 archive renders ten recent posts (Cult Heroes, English League Classics and club kit guides). The Classic archive renders ten kit-related posts, including English League Classics and vintage international/club kits. These are secondary blog archives with `hasMore=false`; they do not establish in-game player rosters, event availability or gameplay mechanics. Links are in the source ledger.

### DLSInside Champions and Classic pages
Both pages identify their titles as DLS 2026, but player names/cards failed to render. Champions showed only 12 unlabeled numbers: `7, 10, 10, 14, 22, 10, 23, 7, 22, 9, 9, 7`; Classic showed 12 unlabeled numbers: `10, 10, 11, 10, 5, 10, 9, 11, 8, 9, 19, 10`. Do not interpret these sequences as player IDs, OVRs, positions or names. DLSInside and DreamKitsApp remain one non-FTG family.

### GamingOnPhone DLS26 career guide (chunk 0/2 only)
The guide’s first chunk makes secondary-source claims that the transfer market refreshes after matches; market quality is affected by team rating/“chemistry”; Scouts cost Coins and Agents Gems; training-center levels unlock formations; Accommodation expands squad size; Stadium capacity and Commercial Centre increase coin rewards; Physios restore stamina/injuries; and releasing a Legendary player does not guarantee a Legendary Coach. It also describes coach tiers and random/stat boosts. These claims are **not FTG-confirmed** and must be reconciled against first-party sources or user screens before being used in a plan. Chunk 1 remains unread; no date surfaced in the fetched chunk.

### Git recovery and coverage
- Turn opened at `fb9a2c0` with project paths untracked. Backup/fetch/reset to `deb5672`; byte comparison verified **200 files identical**. No content lost or force-push; ISSUE-0014 occurrence #13 recorded.
- dlskiturl unchanged on the **thirty-fifth** check: same nine front-page items, no new October-dated item.
- General FAQ bodies **20/21**; Parents’ Guide **8/8**. No exhaustion declaration.


## TURN 52 (2026-10-05) — secondary guide pages read; version caveats retained

### GamingOnPhone DLS26 Career guide now complete
Chunk 1 completes the DLS26 Career Mode guide; byline Saurabh Shetty, published/updated 27 Jan 2026. It says Challenges reward Coins and Gems and most Daily Challenges are simple/under an hour. The article remains secondary and should not be used as FTG-confirmed mechanics without first-party/user-screen verification.

### GamingOnPhone DLS2025 resource/progression guides (partial)
Three pages fetched are explicitly DLS2025, each only chunk 0/2 read. Historical numbers/rules must not be silently carried forward into DLS26:
- **Coins:** Commercial Level II/III claimed +13%/+21% bonus; login cycle 20 days; 400 SP Season Pass activation; 40 free SP/day; 10-day season; 1,095 free-pass Coins; Progression Bank; Daily Scenario 50 Coins; monthly/special cup and DLP claims.
- **Gems:** claimed 20-day login cycle; challenge/Academy Gem rewards; higher-division increases; 10 Gems per Global Challenge Cup round; Dream League Live weekly/match rewards; 400-SP activation and 10-day bank; suggested gem spending on facilities, coaches, agents and boosts.
- **Division progression:** claimed 15-game objective window; max Medical Centre; release unwanted players for Fitness Coaches; Common Scout 75 Coins vs Legendary 500 and a 5% Common-Scout Legendary chance.
These are secondary, dated to the DLS2025 generation in their titles; remaining chunk(s) unread.

### BlueStacks DLS26 character guide (partial; wording overlap)
BlueStacks guide is dated June 2, 2026, but its chunk 0/3 uses very close wording and structure to the GamingOnPhone DLS26 article about Players/Coaches/Physios, facilities and transfer “chemistry”. Treat the pair as non-independent until provenance is established. BlueStacks restates (without FTG verification) the facility/market claims above; chunks 1–2 remain unread.

### Recovery, monitoring and coverage
- Turn opened at `fb9a2c0` with project paths untracked. Backup/fetch/reset to remote `0f9ee4c`; byte comparison verified **201 files identical**. No content loss or force-push; ISSUE-0014 occurrence #14 recorded.
- dlskiturl unchanged on the **thirty-sixth** check: same nine front-page items, no new October-dated item.
- General FAQs **21/21 titles, 20/21 bodies**; Parents’ Guide **8/8 titles and bodies**. No exhaustion declaration.


## TURN 53 (2026-10-06) — secondary-source continuations and homepage check

### DLSKitURL homepage monitor (`page-295`)
The current fetch rendered ten post cards: Atlético Madrid kits, Cult Heroes, Tottenham kits, English League Classics, Dortmund kits, Juventus kits, Real Madrid kits, Liverpool 2006/07 kits, PES 2017 and PES 2021. The previous Turn-52 entry described the homepage as the “same nine”; the present count of ten conflicts with that count, but no prior raw render was retained to identify a changed card versus a counting error. No publication dates are visible in this render. Treat it as a secondary kit/event blog, not evidence of roster completeness, event state or game mechanics. Exact unvisited card links are retained in the frontier.

### GamingOnPhone DLS2025 resources guides complete (`page-296`–`page-298`)
All three guides are explicitly DLS2025 and by Akash Roy, dated Dec 16, 2024; completing their chunks does not verify current DLS26 rules.
- **Coins (`page-296`):** the remainder claims a 90-day Prize Ladder cycle, four additional Classic Players associated with the 1998 World Cup, and 30 Coins from in-game advertising once per 24 hours. Historical secondary claims only.
- **Gems (`page-297`):** the ending recommends saving Gems for Live Transfers, avoiding Agents, and using Gems for player OVR/training only after accumulating a balance. Treat these as DLS2025 author advice, not a DLS26 recommendation.
- **Divisions (`page-298`):** the final chunk completes the article and exposes its Dec 16, 2024 byline/date; it adds no basis for transferring the DLS2025 division/reward figures into DLS26.

### BlueStacks DLS26 character guide (`page-299`, still partial)
Chunk 1/3 includes FAQ claims about coaches improving attributes/OVR, Physios restoring stamina and healing injuries, prioritizing Stadium, Scout-versus-Agent costs/odds, and Live Transfer refreshes after matches. These overlap closely with the GamingOnPhone guide and remain secondary—not independent FTG confirmation. The related-article rail surfaces free-rewards, redeem-codes and custom-kits pages as leads; chunk 2 remains unread.

### Recovery and scope
Turn 53 opened with the recurring sandbox restore signature. The remote branch was recovered at `d0fbe82`; 201 non-clock target files were byte-identical, and the only expected divergence was this turn’s start line in `logs/turn_clock.txt`. ISSUE-0014 occurrence #15 is logged. No content loss or force-push. Five retrievals were logged; no first-party mechanic was validated, no preference or recommendation changed, no dimension was closed, and no exhaustion declaration was made.


## TURN 54 (2026-10-06) — BlueStacks guide complete; first-party route probe blocked

### DLSKitURL monitor (`page-300`)
The T54 homepage render matches the T53 render: the same ten cards and snippets (eight DLS-related kit/event posts and two PES posts). The T52 note said “same nine,” which conflicts with both T53 and T54. No dates are visible in either current render, so neither a newly posted October item nor a content change is established. Secondary kit/event blog only; no game-mechanics inference.

### BlueStacks DLS26 guide complete (`page-301`)
Chunk 2/3 completes the page. Its returned remainder contains comments, related recommendations/news and BlueStacks promotional material, with no additional DLS26 mechanic evidence. All three chunks have now been read. The guide remains secondary and closely overlaps GamingOnPhone; do not count the pair as independent corroboration.

### Cult Heroes acquisition-route follow-up (`discovery-t54-tiktok-cult-heroes-7437552025958763809`, `page-302`, `discovery-t54-ftgames-cult-heroes-search`)
A targeted TikTok search result links to the known FTG-handle video, but the extracted item combines a DLS25 title/date (“A new era, a new card,” 2024-11-15) with DLS26 Cult Heroes copy mentioning September 16 and availability through Events, Drafts and the Season Pass. Its internal attribution is unclear. A direct `fetch_page` attempt returned **HTTP 403** with no body. A separate FTG-site search found no Cult Heroes-specific official page; it surfaced generic, dated support snippets (including Season Pass content marked version 12200 onwards and general player-acquisition routes). None resolves the DLS26 Cult Heroes conflict. Keep the existing route evidence status unchanged; the first-party video body or an in-game capture is still needed.

No new gameplay claim or recommendation was promoted. No dimension closed and no exhaustion declaration made.


## TURN 55 (2026-10-06) — social-source probes and a current creator video

### First-party Cult Heroes route probes (search-only / blocked)
- Targeted YouTube/Instagram/FTG search (`discovery-t55-youtube-cult-heroes-search`) returned creator gameplay/tutorial results; it did not surface an FTG-authored route explanation. The official-looking DLS26 teaser result is from 2025 and is not route evidence.
- The targeted `@playdls` Instagram search (`discovery-t55-instagram-playdls-search`) returned only the general profile, no Cult Heroes post.
- The Facebook search result (`discovery-t55-facebook-cult-heroes-search`) attributed a snippet to Dream League Soccer: “Scoring team goals with a full squad of Cult Heroes hits different” / “Collect them in game now.” It contains no date or acquisition method. Direct profile fetch `page-303` returned **HTTP 403**; an exact-phrase search (`discovery-t55-facebook-caption-exact-search`) returned unrelated pages. This is not a direct post capture and does not establish the current event window or route.

### Secondary Cult Heroes tutorial (`page-304`)
A public YouTube page identifies creator **Raven Exe**, upload date **2026-10-03**, 4:09 duration, and 46 views / 2 likes when fetched. Its transcript claims: (1) a Draft costs 225 Gems and takes seven matches to award a Cult Hero Agent; (2) a Season Pass Agent is at the end; (3) an online Cult Hero Challenge awards an Agent after wins and offers three attempts; and (4) an Events section in the Transfer Market shows a calendar of upcoming Cult Heroes events. The creator also says the Agent may yield a random hero rather than the specific desired player.

These are **creator assertions**, not FTG-confirmed facts. The fetched transcript is not independent gameplay verification; no UI state was inspected separately. Treat the 225-Gem cost, seven-match requirement, three-attempt rule, calendar path and reward timing as unverified. Do not recommend spending or change the existing confidence tier based on this one video. The first-party route remains unresolved.

### Scope and budget
No game mechanic was promoted to verified and no user strategy changed. Seven retrieval calls were made (six-call cap exceeded by one); the overrun is recorded in the operational log. No dimension closed and no exhaustion declaration made.


## TURN 56 (2026-10-06) — support search and SakibPro event-route article

### First-party availability check
A targeted FTG support search (`discovery-t56-ftg-support-cult-search`) returned only generic 2024/2020 guidance on Transfers/Scouts/Agents/Prize Ladder and Accommodation; no Cult Heroes page. The `@playdls` Instagram profile fetch (`page-305`) returned **HTTP 403**, with no body/posts. An official-handle TikTok search returned only WorldWinners/WorldHeroes and Skills snippets, not Cult Heroes mechanics (`discovery-t56-ftg-tiktok-challenge-search`). No first-party route or UI confirmation was obtained.

### SakibPro article re-read — duplicate retrieval (`page-306`–`page-307`)
The exact URL was already recorded as S-0114, page-047-sakibpro-events-article; the T56 chunk calls are repeat retrievals of the same SakibPro source family, not independent corroboration. The Aug 21, 2026 article calls itself “100% Official,” but the fetched page does not establish FTG provenance. It claims: Cult Hero Agents come from Season Pass, Online Events and Dream Draft (one earlier sentence also says Market); Agents choose a player randomly; three Season Passes yield one free + one paid Cult Hero each; Online Events offer three top-tier heroes; and one Free plus two Paid Dream Drafts each offer up to three Cult Heroes. It separately says the World Winners event would finish “today,” a time-bound claim tied to its Aug 21 publication and not a current timer. Chunk 1 adds an expected total of six Season Pass cards and English League Classics material, but no first-party route evidence. Treat the whole article as SakibPro secondary-source-family claims; its “official” wording is not proof.

### Cross-check of Raven Exe claims (`discovery-t56-cult-hero-cost-search`)
Searching the exact **225 Gems / seven matches** claim returned the Raven Exe video already read, the DLSKitURL and SakibPro articles, community discussion and generic currency pages. No FTG result independently confirms either number. SakibPro’s broader Dream Draft counts are not necessarily the same as Raven Exe’s claim that one 225-Gem, seven-match Draft awards an Agent; do not merge these into one mechanic. All Draft cost, match counts, retries and reward structures remain unverified and are not spending advice. One modified-APK search result was screened out and not opened.

No confidence promotion or strategy change. No dimension closed; no exhaustion declaration.


## TURN 57 (2026-10-06) — official-channel, store and position searches

### Cult Heroes first-party search follow-up
- A targeted First Touch Games YouTube search returned only its general channel profile (`discovery-t57-youtube-ftg-cult-search`), no Cult Heroes video or route instructions. The channel profile is retained as a future lead if needed.
- A Google Play eventdetails query (`discovery-t57-play-eventdetails-search`) returned an event for **Football League 2026**, not Dream League Soccer; it is not merged with DLS event evidence.
- A support-domain search for Cult Heroes/Agents/Draft returned no Cult Heroes-specific FTG support article. A separate X search (`discovery-t57-x-ftg-cult-search`) surfaced historical 2020–2022 posts from `@firsttouchgames` and recent Cult Heroes material from fan accounts; no current FTG X post resolved the route. Search snippets are not direct captures.

### Position and formation source-scope check
The support search (`discovery-t57-support-position-search`) returned generic DLS support results on development, stats, multiplayer and squad expansion, but no DLS26 position-lock answer. A formation-related help link surfaced again; the actual formation article 7917587319313 is already classified by its section/API metadata as **Ultimate Clash Soccer**, not DLS (`page-189`, `page-201`, revisited context in `page-128`/`page-195`). Do not transfer its formation text to DLS26. The user-stated no-position-lock claim remains unverified.

No gameplay claim was promoted, no recommendations changed, and no dimension was closed. No exhaustion declaration.


## TURN 58 (2026-10-06) — FTG YouTube channel and official page review

### FTG YouTube channel (`page-308`, `page-309`)
The channel-home response starts with an embedded **“Error 401 (Bad Request)”** banner, followed by YouTube shell and a partial channel view. It shows a DLS26 Launch Trailer (video `9Iw8nZRpijA`, labeled seven months old) and older DLS teaser/Champions/Dream Stars videos. The separate Videos-tab response shows the same error banner and signed-out shell but no usable full listing. No Cult Heroes route instructions were returned. These incomplete renders do not prove no such post exists; do not retry the same requests.

### FTG `/dls` alias (`page-310`)
The requested `https://www.ftgames.com/dls` path resolved to the generic `/games` page already recorded as `page-269`. It repeats the undated product description and app links, including the Apple label “Dream League Soccer 2020.” This is not DLS26-specific and adds no Cult Heroes or position-lock evidence.

No new first-party mechanic was established. The route and DLS26 position-lock questions remain open; no recommendation or confidence tier changed, and no exhaustion declaration was made.


## TURN 61 (2026-10-06) — secondary video/playlist follow-up

### Cult Heroes Plate event creator claims (`page-312`–`page-314`)
- **Source assertions, not verified mechanics:** DroidCheat’s public YouTube playlist lists a “Cult Heroes Plate Event - 42 Points & Agent Reward!” final-part video; its creator-written description says the player reaches 42 points, wins the tournament, and unlocks an Agent reward. A separate DroidCheat video is titled as Cult Heroes Tournament gameplay, but its returned transcript is match commentary and does not explain event acquisition or position locking.
- **Evidence:** `page-312-droidcheat-cult-heroes-gameplay-t61` (all page-render chunks read; extracted transcript remains incomplete as a video record); `page-313-droidcheat-dls26-playlist-t61` (chunk 0/5 only; embedded 401 banner but playlist items rendered); `page-314-droidcheat-cult-heroes-plate-final-t61` (chunks 0–1/4 only; hasMore=true). Exact URLs and retrieval notes: `source_archive/t61_droidcheat_video_review.md`.
- **Confidence:** Speculative (one secondary creator/source family; no FTG confirmation, no independent in-game screen review, and the direct 42-point page is incomplete).
- **Volatility:** Critical; event eligibility and rewards may change, and the returned material has no verified build stamp.
- **Checkable origin:** YouTube page-render output for the DroidCheat creator channel. Playlist, titles, and creator description establish what that creator published, not that the described game route or reward is accurate.
- **Status:** Do not merge this with Raven Exe’s 225-Gem/seven-match claim or SakibPro’s reward counts. It adds no independent corroboration and is not spending advice. Cult Heroes acquisition route/reward and DLS26 position-lock behavior remain unverified; no confidence promotion or strategy change. T62 may resume `page-314` at chunkIndex 2 if the remaining page content can answer an active question.


## TURN 62 (2026-10-06) — same-family Cult Heroes video continuation

### DroidCheat “Road to 42 Points” video (`page-315`)
- **Source assertion, not verified mechanic:** the creator-written description says 42 points are needed to claim victory and secure top rewards in a Cult Heroes Plate Event. Its extracted transcript is primarily match commentary; it does not establish an Agent reward, cost, eligibility, exact route, or retries.
- **Evidence:** `page-315-droidcheat-cult-heroes-42points-part2-t62`, all page-render chunks 0–3. Turn 62 also completed chunks 2–3 of `page-314-droidcheat-cult-heroes-plate-final-t61`; those remainder chunks added only playlist/recommendation metadata. Notes: `source_archive/t61_droidcheat_video_review.md`. No video frames were inspected.
- **Confidence:** Speculative (creator assertion from the same DroidCheat source family as page-312–page-314; not independent confirmation or FTG evidence).
- **Volatility:** Critical; the event is live/rotating and no verified build stamp is present.
- **Status:** This repeats a 42-point creator claim within one source family; it does not validate the 42-point Agent-reward claim or settle Cult Heroes acquisition. Keep route, cost, reward, and position-lock behavior unverified; no spending advice or confidence promotion.


## TURN 63 (2026-10-06) — German App Store event page

### Cult Heroes localized storefront copy (`page-316`)
- **Claim:** The German DLS26 App Store event page renders “FINDET JETZT STATT / LIVE-EVENT / Kulthelden” and says the remembered top stars are available with boosted attributes. English translation: “Happening now / live event / Cult Heroes. Sign these top stars that many fans remember. Now available with boosted attributes!”
- **Evidence:** Direct `functions.fetch_page` retrieval, complete chunk 0, `page-316-apple-de-cultheroes-event-t63`; original German and translation are preserved at `source_archive/t63_apple_de_cult_heroes_event.md`.
- **Confidence:** Speculative (storefront-level evidence; same Apple/developer origin family as the existing U.S. event page, not independent in-game confirmation).
- **Volatility:** Critical; this is a live-event listing and has no verified client/build stamp.
- **Checkable origin:** German Apple App Store event page for Dream League Soccer 2026. It establishes only what that regional storefront displayed when fetched.
- **Status:** Adds a German localized event label, not an acquisition route, price, reward, or exact deadline. “Happening now” is not treated as proof of in-game availability. Cult Heroes route/rewards and position-lock behavior remain open; no confidence promotion or spending advice.


## TURN 64 (2026-10-06) — FTG corporate-site and linked-profile checks

### Corporate site / generic Dream League Soccer copy (`page-317`, `page-318`)
- **Source assertion:** FTG’s corporate homepage describes the studio as established in 2011. Its Games page describes Dream League Soccer generically as offering 4,000+ FIFPRO players and 8 divisions; the returned panel uses DLS18 background-art alt text, links to an Apple page titled DLS 2020, and points to Google Play package `com.firsttouchgames.dls7`.
- **Evidence:** direct page-render of `https://www.firsttouchgames.com/` and `https://www.firsttouchgames.com/games#games-dls` (`page-317-firsttouchgames-home-t64`, `page-318-firsttouchgames-games-dls-t64`); note `source_archive/t64_ftg_corporate_and_social.md`.
- **Confidence:** Speculative for any current DLS26 mechanic (generic, undated corporate copy; no current build stamp).
- **Volatility:** Critical for current event/mechanics; the page does not establish a DLS26 event or implementation.
- **Status:** No Cult Heroes route, cost/reward, or position-lock information; do not assign generic/legacy copy to DLS26.

### FTG-linked social profiles (`page-319`, `page-320`)
- FTG’s Games page links to `facebook.com/dreamleaguesoccer`; its direct fetch returned HTTP 403 with no body. The corporate site also links to `@firsttouchgames`; the resolved X profile identifies itself as DLS26/FTG and rendered five posts, newest dated 2026-03-04 and directing support queries to FTG’s help center. The limited list contained no Cult Heroes route instruction.
- **Evidence:** `page-319-facebook-dls-profile-t64` (blocked) and `page-320-x-firsttouchgames-profile-t64` (complete limited render). The X profile’s five visible items do not establish that no other/current post exists.
- **Confidence:** Speculative for game mechanics; no route/position-lock claim was promoted.
- **Status:** Facebook blocked; X timeline limited and no event route. Continue seeking distinct first-party or in-game evidence; no spending advice.


## TURN 66 (2026-10-06) — UK Google Play listing and linked social profiles

### Google Play UK locale (`page-323-google-play-dls-uk-listing-t66`)
- **Source assertion:** the developer listing displays an update date of 14 Sept 2026. Its event card, linked to existing Google Play event ID `4830045897422713648` (page-009), says “Ends on 10/14” and “The names the fans remember, from their peak years.” The date omits a year. The same render’s “What’s new” text calls the Cult Heroes collection “coming soon.”
- **Evidence:** complete page-render chunks 0–1 at the UK locale; note `source_archive/t66_googleplay_uk_and_social.md`. This is the same Google Play app/listing source family as the U.S. listing, not independent confirmation.
- **Confidence:** Speculative for current in-game event state; the storefront strings are mixed/ambiguous and do not establish the timer.
- **Volatility:** Critical.
- **Status:** No acquisition route, cost/reward, or position-lock information. Do not infer an in-game end date from `10/14`; verify only in-game before any advice.

### Linked official social profiles (`page-324`, `page-325`)
- The UK Play listing links to FTG TikTok `@dreamleaguesoccer.ftg` and Instagram `@playdls`; both direct profile requests returned HTTP 403 with no body. No posts or mechanics were observed. These are access failures, not negative findings.
- **Status:** No new claim; both Cult Heroes route/rewards and position-lock questions remain open.


## TURN 71 (2026-10-06) — first-party position/formation context, not a DLS26 lock rule

- **Existing first-party source:** FTG’s general `core-principles` page (`page-066-ftg-core-principles`, `https://www.ftgames.com/core-principles`, earlier in-session retrieval, HTTP 200) is summarized in the source ledger as naming **formation choices** and **pitch positioning** among inputs to its game AI. This is a studio-wide policy statement; the record does not establish its DLS26/version scope.
- **Interpretation limit:** the page summary says nothing about whether DLS26 permits every player/position combination, imposes position locks, or applies out-of-position penalties. It neither verifies nor refutes the user-stated no-lock claim. No fresh fetch was made this turn.
- **Confidence:** first-party wording is traceable to the existing source record; application to the specific DLS26 question remains Speculative. **Volatility:** Critical.
- **Status:** verification still requires DLS26-specific documentation or in-game evidence; no dimension closed.


## TURN 72 (2026-10-06) — structured Apple listing metadata

- **Source record:** Apple Lookup API for the U.S. DLS26 listing (`page-332-apple-lookup-us-t72`) returns seller “First Touch Games Ltd.”, version **13.430**, `currentVersionReleaseDate` **2026-09-16T14:03:27Z**, and release notes that call the Cult Heroes collection “coming soon.”
- **Scope:** the generic description mentions Agents/Scouts, regular events, and Dream Draft, but does not describe the Cult Heroes route, event costs/rewards, or position locks. This is App Store metadata, not an in-game screen.
- **Conflict note:** existing Apple event page `page-316` describes a live Cult Heroes event with boosted attributes. The version note and event card are both Apple/storefront-family messages; the tension does not establish the event's actual in-game state or route.
- **Confidence:** Speculative for current in-game status. **Volatility:** Critical. No route/reward/position claim promoted; verification remains open.


## TURN 73 (2026-10-06) — FTG Help Center search result for Events

- The public FTG Zendesk search API (`discovery-t73-ftg-help-center-api-cult-search`) returned article 214386765, “What are Events?” Its metadata gives `section_id` **203117609**. The existing first-party FTG help-center section map (`page-186-ftg-help-centre-root`) maps 203117609 to **Score! Hero FAQs** and 203117809 to **DLS FAQs**. T73 mistyped the ID and incorrectly attributed the result to DLS; corrected in T74.
- The generic article body says permanent or time-based events are available in the “Events” section and can be played alongside the main story. This is Score! Hero help text, not DLS/DLS26 route evidence; it does not mention Cult Heroes, DLS26, costs, rewards, or position locks.
- The broad search overmatches Hero titles. Page 1/3 was read in T73; pages 2–3 were then unexamined. **Confidence:** first-party article text, product context Score! Hero per section map; no application to DLS26. **Volatility:** Critical.


## TURN 75 (2026-10-06) — FTG search pagination complete; social discovery unresolved

- Completed page 3/3 of the public FTG Help Center query `Cult Heroes` (52 total results). The final two results are general account/privacy articles; across the returned 52 items, no explicit DLS26 Cult Heroes route/reward or position-lock instruction was surfaced. This broad search does not establish absence from DLS26 or exhaust sources.
- Three web searches returned interleaved snippets resembling Cult Heroes captions without a unique permalink for the text. Those snippets—including any secondary-source fragments—were recorded as discovery only, not evidence. Two distinct TikTok video URLs returned HTTP 403 with no body; do not repeat exact URLs or infer their contents.
- **Status:** Cult Heroes route/rewards and DLS26 position-lock behavior remain unverified; Step-3 device setup remains needed for direct in-game verification.


## TURN 76 (2026-10-06) — focused FTG Agent query; position search pending

- The FTG API query `Cult Hero Agents` returns one result, DLS FAQ article 360004066417, “How do I obtain more players?” (`section_id` 203117809; API `updated_at` 2026-09-19, `edited_at` 2024-12-06). It is already body-read at `page-063-ftg-obtain-players-faq`. The general article says Agents immediately add a player and Prize Ladder rewards special rare players when criteria are met. This does **not** identify Cult Hero Agents’ event route, price, guarantee, or card reward; metadata timestamp does not prove current-body applicability.
- A separate FTG search for `position lock` reports 16 mixed-game results, but only chunks 0–3/10 have been read. Do not classify or infer DLS behavior until chunks 4–9 are read. Visible Season Pass “tier locks” are unrelated to player-position locking.
- A new TikTok video URL returned 403/no body. It provides no evidence about the post. **Status:** DLS26 position-lock verification remains owed; user-stated position-lock absence is preserved, not silently replaced. Cult Heroes route/rewards remain open.


## TURN 77 (2026-10-06) — position-lock Help Center query complete

- Completed the FTG Help Center API query `position lock`: 16 results on one page, all 10 rendered chunks read across T76–T77. The mixed results include DLS Season Pass article 4404070913169, where “locks” refer to Season Pass reward tiers, and DLS player-stats article 360019166777 (already read as `page-004-ftg-stat-mechanics`). These do not answer whether DLS26 squad positions can be locked.
- **No conclusion about in-game absence:** the user-stated claim that DLS26 has no position locking remains explicitly unverified; direct device setup is still owed. Cult Heroes route/rewards remain unverified.


## TURN 78 (2026-10-06) — FTG formation-position search is partial

- New public Help Center query `formation position` returned 14 results on one page but renders across 9 chunks. Chunks 0–5 only were read this turn. Visible results mix Score! Match/UCS formation material with DLS stats/leaderboard FAQs; no DLS26 squad-position-lock rule is established. Resume the exact query at chunkIndex 6; do not classify before chunks 6–8 are complete.
- Preserve the user-stated DLS26 “no position locking” as unverified. Cult Heroes route/rewards remain open; no absence, closure, or exhaustion inference.


## TURN 79 (2026-10-06) — formation-position query completed; no rule established

- FTG Help Center API query `formation position` is now complete (14 results, page 1/1, 9 rendered chunks; T78 read chunks 0–5, T79 read chunks 6–8). The later chunks finish player-stat material and include Score! Match account help. The complete mixed-product result set provides no DLS26 squad position-lock rule. This is not evidence that locking is absent; do not transfer Score! Match/UCS behavior to DLS.
- Three targeted FTG/official-account searches returned only general or old support/game posts and no DLS26 Cult Heroes route/reward or position-lock instruction. They were search-result cards only, not fetched source pages; details and URLs are recorded at `source_archive/t79_official_search_triage.md`.
- Keep both target questions open. User-stated no-lock remains unverified; Cult Heroes route/rewards remain unresolved.


## TURN 80 (2026-10-06) — official TikTok search lead, not verified

- A `functions.web_search` result set under `@dreamleaguesoccer.ftg` included Cult Heroes text mentioning Cult Hero Agents in Events/Drafts/Season Pass and a guaranteed Special Card. The result mixed captions across multiple cards and did not map them reliably to exact video URLs. This is a lead, not an accepted game fact; direct post-page verification is pending. Two surfaced URLs were already logged as blocked; a new candidate is queued. See `source_archive/t80_official_social_leads.md`.
- The official YouTube channel URL was fetched again despite a prior T58 visit; its partial payload includes an embedded 401 text and no new target evidence. The `@playdls` Instagram fetch repeated earlier HTTP 403 attempts; neither limitation is evidence of absence. Avoid duplicate fetches.
- Cult Heroes route/rewards and DLS26 position-lock behavior remain unresolved.


## TURN 81 (2026-10-06) — social search snippets remain unmapped

- Three exact-phrase TikTok searches associated Cult Hero Agent/guaranteed-card text with cards titled as unrelated DLS25 videos (dated 2024-11-15 and 2025-03-04) or a DLS26/TO25 clip. The snippets are mixed and no exact Cult Heroes post was confirmed. A new candidate direct fetch returned HTTP 403. Do not assert the route or guarantee.
- An official Dream League Soccer Facebook search card showed “collect them in game now” wording, but had no date/route detail; direct fetch returned HTTP 403. Search-card content remains unverified.
- No change to target conclusions: Cult Heroes route/rewards unresolved; user-stated DLS26 no-position-lock remains unverified. Full trace at `source_archive/t81_tiktok_snippet_mapping.md`.


## TURN 82 (2026-10-06) — FTG generic-agent and Draft help checked

- FTG Help Center query `Cult Hero Agent` returned one generic “How do I obtain more players?” result. Its body says generic Agents immediately add a player, but does not mention Cult Hero Agents or the event. Do not transfer that statement to Cult Heroes.
- Complete `Drafts Season Pass` query (12 results/4 chunks) and `Drafts` query (3 results/1 chunk) supplied only general Season Pass, Prize Ladder, player-acquisition, Dream Point Boost, and some Ultimate Clash Soccer material. No event-specific Cult Heroes route/reward was established.
- Cult Heroes route/rewards remain unresolved; position-lock remains unverified and user-stated. Full provenance: `source_archive/t82_ftg_agent_draft_searches.md`.


## TURN 83 (2026-10-06) — Apple storefront event card, not in-game verification

- FTG’s generic “What are Events?” Help Center article says permanent or time-based events are available in the in-game Events section alongside the main story. This does not identify Cult Heroes.
- The directly fetched U.S. Apple App Store DLS26 listing/event page displays “HAPPENING NOW / LIVE EVENT Cult Heroes” and “Now available with boosted attributes.” This verifies the storefront wording only; it does not prove account-level in-game access, a route, cost, or a specific reward. It may be the same event listing localized from the previously examined German store text, not independent corroboration.
- The partial FTG `live events` API search has only chunk 0/10 read; resume chunks 1–9. An “out of position” search returned no relevant snippet, which is not evidence of absence. Cult Heroes route/rewards and DLS26 position-lock remain open. See `source_archive/t83_live_event_and_storefront.md`.


## TURN 84 (2026-10-06) — partial FTG events-query progress

- Continued FTG `live events` API query through chunks 1–6/10 (18 results total); chunks 7–9 remain. A generic “What are Super Players?” result says enhanced players may be won in Events and occasionally rarer packages. It does not identify Cult Heroes as Super Players or explain Cult Hero Agents; do not conflate them. Visible results otherwise include generic currencies/multiplayer and the already-seen player-stats material. No Cult Heroes-specific route/reward is established.
- T83's three direct URLs were already in the ledger, so those fetches were repeats and not independent corroboration; exact audit is in `source_archive/t84_ftg_live_events_query_progress.md`.
- Cult Heroes route/rewards remain open; DLS26 position locking remains user-stated and unverified.


## TURN 85 (2026-10-06) — FTG `live events` query complete

- The 18-result, 10-chunk FTG Help Center response is complete (T83 chunk0; T84 chunks1–6; T85 chunks7–9). It mixes DLS FAQs/stats, the generic Events and Super Players articles, and other FTG titles. The Super Players article says such enhanced players may be won in Events/rare packages, but does not identify Cult Heroes as Super Players or explain Cult Hero Agents.
- No result specifically gives a Cult Heroes route, cost, or reward. This is not proof of absence outside this search response. Cult Heroes route/rewards and DLS26 position lock remain open. See `source_archive/t85_ftg_live_events_query_complete.md`.


## TURN 86 (2026-10-06) — new FTG query is partial

- FTG Help Center query `Special Players Events` reports 10 results across 8 chunks; only chunk 0 read. Visible cards are generic card-colour, player acquisition/Agents, Prize Ladder, and player-stat material. Do not equate these categories with Cult Heroes. Resume chunks 1–7; no query-wide conclusion.
- Cult Heroes route/rewards and DLS26 position-lock remain unresolved. Provenance: `source_archive/t86_special_players_search_partial.md`.


## TURN 87 (2026-10-06) — FTG special-player query progressed

- Continued `Special Players Events` through chunks 1–6/8 (after T86 chunk0). Results continue generic DLS stats/help, generic Super Players, older DLS19 customization, and Score! Match content. No Cult Heroes-specific route/reward surfaced in these chunks. Chunk7 remains unread; do not make a query-wide absence conclusion.
- Cult Heroes route/rewards and DLS26 position locking remain unresolved. See `source_archive/t87_special_players_query_progress.md`.


## Turn 88 — FTG special-player query completed; specific Cult Heroes evidence remains open

FTG Help Center `Special Players Events` is complete (10 results, chunks 0–7/8). Final chunk 7 contains generic account/profile/friend-match/update help; the response does not specifically explain Cult Heroes. The `Cult Hero Agents` API query was repeated at an exact URL already present from earlier work and again returned the generic “How do I obtain more players?” FAQ; it is not independent evidence. Exact searches `Cult Heroes Event` and `Cult Heroes rewards` returned zero results. A targeted FTG-site search yielded generic/older result cards only; snippets are not page evidence. These bounded search outcomes do not establish in-game absence or a route/reward.

Cult Heroes availability, acquisition route, cost, and rewards remain unresolved. DLS26 position-lock behavior remains explicitly `user-stated` and unverified pending Step-3 device setup. Provenance: `source_archive/t88_ftg_special_players_searches.md` and T88 entries in `logs/sources_visited.json`.


## Turn 89 — YouTube discovery was secondary and repeated
A targeted YouTube search returned secondary creator video cards, not a verified FTG publication. The top result, a DroidCheat video, had already been fully rendered as `page-312` in T61; T89 fetched the same exact URL again. The page metadata/creator description and match-commentary text are not independent or first-party evidence and do not establish event availability, route, cost, or reward. A follow-up query against a YouTube game-channel ID returned zero search results; this is not proof of absence or channel ownership. Provenance: `source_archive/t89_droidcheat_video_repeat_and_youtube_search.md`. Cult Heroes route/rewards and position-lock remain unresolved.


## Turn 90 — `position changes` Help Center search is partial
A new FTG query returned 49 results across 2 API pages; page 1 contains 7 rendered chunks, of which chunks 0–4 were read. Visible mixed results include generic formation-grid and player-role help snippets. Neither states whether DLS26 locks a player to a position; do not conflate formation editing/player roles with squad-position locking. Chunks 5–6 and API page 2 remain unread; no query-wide conclusion. An Instagram post search for `@playdls` + Cult Heroes returned no result cards; this does not prove absence. Provenance: `source_archive/t90_ftg_position_changes_query_partial.md`. User-stated no-lock remains unverified; Cult Heroes route/rewards remain unresolved.


## Turn 91 — FTG `position changes` page 1 complete, page 2 partial
FTG API page 1/2 is complete (chunks 0–6/7) and page 2 chunk0/15 is read. The mixed first-page results include generic Squad formation-grid/player-role help, a Score! Match stats article mentioning formation-position behavior, and a DLS Leaderboards FAQ using “position” for ranking. Do not transfer Score! Match wording to DLS26 or interpret leaderboard rank as squad position. Direct FTG formation/roles article text gives menu paths only; neither specifies DLS26 position locking. Page 2 remains incomplete; no query-wide conclusion. User-stated no-lock remains unverified. Provenance: `source_archive/t91_ftg_position_changes_page1_complete_page2_partial.md`.


## Turn 92 — FTG position-changes page 2 remains partial
Page 2/2 now has chunks 0–6/15 read. The generic DLS player-stats result (360019166777) includes a stamina note about workload varying by playing position; that is not a statement about assignment or position locks. Another result is explicitly a UCSS rules FAQ; its formation/ball-position behavior is not DLS26 evidence. Chunks 7–14 remain unread, so no query-wide conclusion. Position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t92_position_changes_page2_progress.md`.


## TURN 93 (2026-10-06) — FTG `position changes` page-2 continuation

Continued the mixed FTG Help Center API response through page-2 chunks 7–12; chunks 0–12/15 are now read, with chunks 13–14 still pending. A generic DLS auto-switch FAQ (article 360008831518) describes switching defensive control to a nearby player. That concerns in-match control selection, not squad-position assignment or a position lock, and is not direct DLS26 evidence. Other visible hits are generic/older-game customization and profile help. No query-wide conclusion. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes availability/route/cost/rewards remain unresolved. Provenance: `source_archive/t93_position_changes_page2_progress.md`.


## TURN 94 (2026-10-06) — FTG `position changes` search completed

Completed API page 2 through chunks 13–14 (15/15 total); page 1 was already complete (7/7). The 49-result, two-page Help Center search is mixed across products/eras. Final chunks include UCSS player-attribute help, generic DLS player-appearance/profile compatibility material (including a DLS19-to-DLS25 transfer item), and Score! Match content. No DLS26-specific squad-position assignment/lock rule surfaced in this bounded search; this is not evidence of universal absence. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t94_position_changes_page2_complete.md`.


## TURN 95 (2026-10-06) — new FTG `player position` search is partial

A distinct FTG Help Center API query reports 100 results across four pages. Page 1 chunks 0–5/10 are read; the remaining four chunks and pages 2–4 are pending. Visible material mixes Score! Match player types/stats, explicit Ultimate Clash Soccer formation/ball-position behavior, and generic DLS player-stat content. UCSS behavior is not DLS26 evidence; the DLS stamina/workload wording does not address squad-position assignment or locking. No DLS26 position-lock conclusion. Resume at `chunkIndex=6`. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t95_ftg_player_position_search_partial.md`.


## TURN 96 (2026-10-06) — FTG `player position` query progressed

Completed page 1 of the 100-result/four-page Help Center query (`player position`; chunks 0–9/10), then read page 2 chunks 0–1/7. The response mixes Score! Match and UCSS text with generic DLS stats/player-management and a DLS Leaderboards result using “position” for rank. No DLS26 squad-position lock guidance is established. Page 2 chunks 2–6 and API pages 3–4 remain unread; resume at chunkIndex 2. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain open. Provenance: `source_archive/t96_ftg_player_position_page2_progress.md`.


## TURN 97 (2026-10-06) — FTG `player position` query progressed

Completed API page 2 (chunks 0–6/7) and read page 3 chunk 0/9. The 100-result/four-page search remains partial. DLS Leaderboards text uses “position” for ranking; UCSS role/attribute/matchmaking material concerns a different product; generic DLS squad expansion and player workload do not address DLS26 squad-position assignment/locking. No DLS26 lock rule surfaced in the portions read; no absence inference. Resume page 3 at chunkIndex 1. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t97_ftg_player_position_query_progress.md`.


## TURN 98 (2026-10-06) — FTG `player position` query progressed

Continued page 3 through chunks 1–6/9 (after chunk 0 in T97). Pages 1–2 are complete; page 3 chunks 7–8 and page 4 remain unread. Visible page-3 material mixes older DLS/FTS customization/profile help, generic DLS settings/Season Pass material, and other FTG products. Season Pass tier locks do not answer squad-position locking. No DLS26 lock rule surfaced in the read portions; no absence inference. Resume page 3 at chunkIndex 7. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t98_ftg_player_position_page3_progress.md`.


## TURN 99 (2026-10-06) — FTG `player position` query progressed

Completed API page 3 (chunks 0–8/9) and read page 4 chunks 0–3/9; chunks 4–8 remain. The mixed page-4 results include DLS Season Pass tier-lock text and leaderboard/final-league “position” language. These refer to reward progression and rank, not squad-player positions. No DLS26 position-lock rule surfaced in the read portions; no absence inference. Resume page 4 at chunkIndex 4. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards remain unresolved. Provenance: `source_archive/t99_ftg_player_position_page4_progress.md`.


## TURN 100 (2026-10-06) — FTG `player position` query completed; retrieval-budget audit

Completed the 100-result/four-page FTG Help Center query (pages 1–4: 10, 7, 9, and 9 rendered chunks). The mixed results did not surface a DLS26 squad-position assignment/lock rule. “Position” in DLS leaderboard/final-league items means rank; Season Pass tier locks concern reward progression; UCSS/Score! text belongs to other products. This bounded search does not establish global absence. **Budget audit:** 11 retrieval executions (six-call ceiling exceeded by five); four were repeats of page-4 chunks 0–3 from T99, and seven were new chunk fetches. No retrieval followed the overrun. DLS26 no-position-lock remains user-stated/unverified; Cult Heroes route/rewards unresolved. Provenance: `source_archive/t100_ftg_player_position_query_complete.md`.


## TURN 101 (2026-10-06) — targeted first-party search audit

Four targeted FTG/YouTube searches returned generic or already-known landing pages and one unverified YouTube channel; no page-level evidence was retrieved. Search snippets are not evidence for Cult Heroes availability/acquisition/rewards or DLS26 position locking. Keep the unverified account out of primary-source claims unless FTG affiliation is established. Both core questions remain open. Provenance: `source_archive/t101_ftg_official_surface_searches.md`.


## TURN 102 (2026-10-06) — FTG `squad position` query partial

FTG Help Center query `squad position` returned 25 results on one API page. Chunks 0–5/10 were read; chunks 6–9 remain. Visible DLS role/formation/player-management text and rank/other-product material do not answer DLS26 squad-position locking. No absence inference. Resume at chunkIndex 6. T101 search-ledger entries were corrected to canonical provenance fields in this turn. Provenance: `source_archive/t102_ftg_squad_position_query_partial.md`.


## TURN 103 (2026-10-06) — FTG `squad position` search complete

Completed chunks 6–9/10 for the FTG API query (25 results, one page); chunk 9 returned `hasMore=false`. The mixed results include generic DLS squad/role/formation/stat help, rank wording, and other FTG products. No DLS26 squad-position lock rule surfaced in this bounded search; no global absence conclusion. UCSS behavior is not DLS26 evidence. Provenance: `source_archive/t103_ftg_squad_position_query_complete.md`.


## TURN 104 (2026-10-06) — FTG Help Center `Cult Heroes` localized query partial

A distinct `locale=de` query returned 52 results/3 pages. Page 1 chunks 0–5/6 are complete; visible results begin with unrelated Score! Hero/8 Ball Hero material and are marked `en-us`. Page 2 exact continuation is recorded; pages 2–3 are unread. No DLS26 event-specific route/reward evidence in page 1; no absence inference. Provenance: `source_archive/t104_ftg_cult_heroes_locale_de_partial.md`.
