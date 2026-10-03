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
