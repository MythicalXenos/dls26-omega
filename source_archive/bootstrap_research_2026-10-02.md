# Bootstrap research capture — 2026-10-02

**Status: PARTIAL SOURCE NOTES, not a raw-source archive and not an exhaustion declaration.** Discovery and page outputs are recorded in `logs/sources_visited.json` under source IDs. Several long pages were retrieved in chunks but their full payloads, especially store reviews and help-center comments, have not been copied here or exhaustively screened. Those sources remain open. No claim in this file is promoted beyond the tier shown.

## Current version investigation

### Apple App Store (US)
- **URL:** https://apps.apple.com/us/app/dream-league-soccer-2026/id1462911602
- **Ledger:** `page-001-apple-us-dls-store`; fetched with `functions.fetch_page` in six chunks, all chunks returned.
- **Observed store content:** title “Dream League Soccer 2026”; seller First Touch Games Ltd.; page says free with in-app purchases, third-party advertising, and an internet connection requirement. The product description names Dream League Live, facilities, Agents and Scouts, Coaches, Seasons/events, scenarios, Dream Draft, and a Clan system. These are developer-provided store claims and are not yet independently checked as current in-game mechanics.
- **Version history excerpt:** page shows version **13.430** dated **Sep 16** and **13.420** dated **Sep 1** (2026 inferred from the listing context, but the year is not repeated beside each row). This supports a chronology of successive versions on the US storefront, not a completed claim about every regional storefront/platform.
- **Other extracted leads:** current “Cult Heroes” live-event card; a list of US-dollar in-app-purchase examples; privacy disclosures attributed by the developer and explicitly described by Apple as unverified; language list; many public reviews. Full raw page and review data are not archived. UGC is not mechanical evidence; duplicates and pure reactions remain to be filtered.
- **Evidence tier:** Speculative for the claim “the current US App Store listing displays version 13.430,” because only one checkable storefront source has been fully fetched and origin-independence/region comparison remains incomplete. Volatility: Critical pending model; patch-triggered dimension applies because the page lists successive releases. Direct evidence is only for the storefront text.

### Google Play (US)
- **URL:** https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en_US&gl=US
- **Ledger:** `page-002-google-play-us-dls`; two chunks retrieved.
- **Observed:** listing title Dream League Soccer 2026, developer First Touch Games Ltd., in-app purchases and ads, app description and community reviews. Page text says “Updated on Sep 14, 2026” and reproduces the late-summer update note about a Cult Heroes collection “coming soon” and bug fixes. The fetched page did not expose the version number.
- **Live-content clue:** the listing contains a Cult Heroes event link with “Ends on 10/14”; no year is shown in that text. This is a time-bounded lead; exact event details and regional availability still need checking.
- **Evidence tier:** store-page wording only; not enough to confirm the Android build number. Reviews are anecdotal UGC and remain unprocessed.

### Third-party version evidence (not independent until origin-traced)
- **APKMirror index:** https://www.apkmirror.com/apk/first-touch/dream-league-soccer-2020/ — `page-008-apkmirror-dls-index`, four chunks retrieved. Lists 13.430 (Sep 16, 2026), 13.420 (Sep 1), 13.410 (Aug 20), and earlier versions, with variants and download links. The page advertises display ads and a paid Premium option (observed commercial incentives). The page says “View on Play Store” and repeats store copy; do not count copied metadata as an independent origin. APK signature not checked; no APK downloaded.
- Search snippets from APKPure, AppBrain, APKCombo, AppMagic, Uptodown, Softonic, and Cafe Bazaar also show 13.430 around Sep 14–20, 2026; these may ultimately descend from Google Play metadata or a shared release file. Origins are unresolved and they are still unvisited leads.
- One third-party article reported 13.420 as a latest September update; its page metadata/search age and update date are inconsistent. Another result lists 13.130 from March 2026. The official Apple history dates 13.420 before 13.430, so the first apparent version conflict is likely temporal/staleness rather than an established contradiction. This is not closed until Android and third-party origins are checked.

## First-party FTG sources

### Help-center article: save data/profile transfer
- **URL:** https://support.ftgames.com/hc/en-us/articles/4413273241873-How-is-save-data-stored-and-transferred-in-DLS
- **Ledger:** `page-003-ftg-save-data-transfer`; one complete page response retrieved. Search metadata labels the article December 6, 2024.
- **Fetched-body summary (normalized, not a line-for-line transcript; raw capture still owed):** FTG says each player is limited to one DLS account. The page places “Manage Devices” and “Link Profile” in the main menu under Options > Advanced. It describes transfer by signing into the same Google/Apple account on another device, with platform-specific sign-in availability. Its code-transfer path requires access to the old device, uses “Generate Code” under “Manage Devices” and “Link Profile” on the new device, is subject to a device limit, and disallows using the code on the generating device. The article advises not sharing personal details/codes and says they cannot be recovered if lost. It says signing out of Google or Apple unlinks the profile and can expose it to loss if the game is uninstalled or the device is changed.

- **Status:** one official support source; direct evidence of what FTG currently publishes, but only one source and the article may be stale. Confidence remains Speculative until the required research and corroboration. This independently verifies the wording of the user-prompt claims only to a limited extent; the “current mechanism” claim is not yet promoted.
- **Related leads:** DLS19-to-DLS25 continuity, Facebook-login removal, ban policy, stat article. They are logged in the source ledger and not all fetched.

### Help-center article: player-stat descriptions
- **URL:** https://support.ftgames.com/hc/en-us/articles/360019166777-How-do-the-various-player-stats-in-DLS-affect-gameplay
- **Ledger:** `page-004-ftg-stat-mechanics`; four chunks retrieved, including extensive comments. Search metadata dates the article April 13, 2021.
- **Article assertions (qualitative, not independently confirmed):** SPE affects top speed; energy and CON affect speed while running/dribbling; ACC affects time to top speed; STA affects energy depletion and halftime energy; CON affects touch/dribbling/skill actions; STR affects collision/stumble impact; TAC affects tackle likelihood/range; PAS affects pass accuracy; SHO affects shot accuracy/height/assist and certain special shots; GKH affects catching/cross claiming/stability; GKR affects reaction and shot-stopping; energy decline gradually reduces other performance attributes. FTG also says the game is not intended as a full, accurate soccer simulation and includes unpredictability.
- **Caution:** single old help page, not version-tied to the current build in the fetched content; every specific mechanic remains Speculative and pending corroboration. Comments contain English, Indonesian, Persian/Arabic script, Cyrillic and other short remarks; most are reactions, requests for coins/player changes, or low-information. One old comment says Haaland’s stats are fake without values/evidence. A three-years-old comment asks about fixtures; neither is proof of a current mechanic. Full comments are not archived or exhausted.
- **Connected links:** FTG support article on app updates (the first guessed URL returned a not-found page; the actual linked ID is 360000262229); kit/logo customization; ban policy; player appearance; DLS25 profile continuity. All are follow-up leads.

### FTG website homepage
- **URL:** https://www.ftgames.com/ — `page-006-ftgames-home`, one complete response.
- It describes FTG as an independent studio established in 2011, lists multiple games and links to a games page and a Twitter/X account. This is company marketing; no DLS26 mechanics/version data was present in the returned text.

## Third-party database: SakibPro

- **URL:** https://sakibpro.com/players/ — `page-007-sakibpro-player-db`; `functions.fetch_page` retrieved one static response.
- The returned page says “Loading Players Database...” then “No players found matching your search”; it does not expose player records. It advertises filters and claims a 14,000+ database, live game-file syncing, accuracy, max upgrades and price/comparison tools. Those are claims made by SakibPro only, not verified values.
- **Source screen:** promotional/engagement incentive inferred from the calls to use its tools and squad-planning service; direct ad/affiliate revenue was not established. The page asserts accuracy and proprietary syncing without showing evidence in the returned text. Keep any claims Speculative; do not add a deception-register entry without the required screening/corroboration outcome.
- **Access status:** the fetch confirms only that the static page was retrievable. The page-render tool did not show the dynamic database; shell `curl` failed at TLS to this domain, but discovery search, API/JS inspection, and other routes have not been exhausted. Not declared inaccessible or a wall.

## Retrieval environment finding

Direct shell `curl` requests to the FTG help center, Apple, Google Play, SakibPro, and APKMirror all failed with `OpenSSL SSL_connect: SSL_ERROR_SYSCALL` and HTTP status 000. This is recorded per URL in the source ledger. The same pages were retrievable using `functions.fetch_page`, so this is a direct-shell network limitation, not an inaccessible-source finding or a global network gap.

## Scope still open

No research topic is exhausted. No confidence promotion has been made. Outstanding source work includes all regional store listings, other official FTG channels and help articles, current Android version confirmation, source-origin tracing for APK/catalogue pages, every connected version-history route, database JavaScript/API layers, other database tools, full treatment of retrieved UGC, technical/APK sources, and community sources across languages and platforms. The mandatory gameplay taxonomy and the no-position-locking verification remain open.

## Event and regional listing follow-up

### Google Play Cult Heroes event detail
- **URL:** https://play.google.com/store/apps/eventdetails/4830045897422713648 — ledger `page-009-googleplay-cult-heroes-event`, one chunk.
- **Observed text:** “Ends on 10/14” (no year displayed); event title “The names the fans remember, from their peak years”; description says the featured players are available for a limited time and urges users to obtain them now. It identifies Dream League Soccer 2026 and First Touch Games Ltd. as the associated app/developer. The store event page gives no exact in-game prices or player list in the returned text.
- **Separate Apple event:** https://apps.apple.com/us/app/dream-league-soccer-2026/id1462911602?eventid=6802988564 — ledger `page-010-apple-cult-heroes-event`. It is labeled HAPPENING NOW / LIVE EVENT and says Cult Heroes are available with boosted attributes, but shows no end date.
- **Interpretation ceiling:** These are direct observations of current storefront event copy. They do not establish the exact in-game deadline, acquisition cost, which players are available, or whether a specific user can still acquire them. This is a time-sensitive lead, not an acquisition recommendation.

### FTG update-schedule article
- **URL:** https://support.ftgames.com/hc/en-us/articles/360000262229-When-will-the-next-app-update-be — ledger `page-011-ftg-update-schedule`, one chunk.
- **Observed:** FTG says it does not provide future release dates, update schedules, or planned activities on request and sometimes shares news on social media. The article links DLS TikTok, Instagram and Facebook pages; these remain account-verification leads. The previously attempted guessed article ID 360006059618 returned a not-found page; the correct link was found on the FTG stat article.

### Bangladesh Google Play listing
- **URL:** https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en&gl=BD — ledger `page-012-googleplay-bd-listing`, two chunks.
- **Observed:** Bangladesh-localized page title and developer match the US listing; it displays a different store content-rating label (Rated for 3+ vs US “Everyone”), shows the same late-summer update text and the same 10/14 event link, and does not expose the version number. This is a storefront metadata difference, not a DLS gameplay claim; reason not investigated.
- **UGC:** The visible reviews include reports of online lag, perceived tackling/referee issues and a request for one-button player recovery. These are user reports, with no date/version/control verification, and do not establish mechanics. Full review processing remains open.

### Germany Apple App Store listing
- **URL:** https://apps.apple.com/de/app/dream-league-soccer-2026/id1462911602 — ledger `page-013-apple-de-listing`, six chunks.
- **Observed:** German-language store copy identifies FTG and the game, shows the Cult Heroes event, purchase/privacy metadata and version history. It lists 13.430 on Sep 16 and 13.420 on Sep 1, matching the U.S. listing. The same developer-provided copy across locales is not assumed to be an independent origin.
- **UGC:** Visible German reviews report subjective gameplay, connectivity, controls, monetization and progression experiences; some reviews are repeated in the extracted page text. Some reviewers comment on early earnings/bonuses and progression, but these old, unverified anecdotes do not establish resource mechanics. Full UGC corpus still needs deduplication, source-date/version tracing, and archival.

