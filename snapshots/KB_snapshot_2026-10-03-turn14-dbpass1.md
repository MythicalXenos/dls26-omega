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
