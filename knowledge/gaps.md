# Research gaps and negative findings

Preliminary DLS26 source retrieval has been performed prematurely while STATE_0 prompt capture was incomplete; the sweep is partial, and no topic is exhausted. The following are open questions, not negative findings:

- Current game version and official terminology for all systems and abbreviations in the user prompt; route: official FTG channels, regional stores, community and technical sources.
- Whether the game has position locking, positional restrictions, or position-based effects; route: DLS26-specific sources and possible in-game/client evidence. User-stated no-locking claim is not yet verified.
- Fundamental gameplay taxonomy dimensions listed in Step 1 of the bootstrap; route: community guides, wikis, archives, official, database/tool, technical, and multilingual sources.
- Current FTG Link Profile rules, if relevant; route: current FTG support documentation plus corroboration.
- Retrieval availability of APKs and transcripts; route: search/fetch tools and shell methods.
- Current user roster, resources, progress, and settings not supplied; route: user confirmation or a future user-run extraction.

## Additional gaps raised by initial retrieval (2026-10-02)

- **Current Android build/version:** US and Bangladesh Google Play page retrievals show update information but no version number in extracted page text; third-party search snippets report 13.430, and U.S./German Apple histories list 13.430 above 13.420. Route: official Google Play data/API and regional listings, FTG announcements, and origin-traced APK metadata. No global current-version claim is closed.
- **Cult Heroes event:** official Google Play event page says “Ends on 10/14” but omits a year; Apple calls the event live. Route: current in-game/store event detail and regional listings. Player list, cost, exact deadline and eligibility are unknown.
- **SakibPro live database:** its static page returned a loading placeholder and no player rows. Route: inspect linked frontend JavaScript/API endpoints, indexed pages, alternative render methods and mirrors. Not declared inaccessible or a wall.
- **Direct-shell HTTPS:** `curl` failed to five tested domains with TLS `SSL_ERROR_SYSCALL`, while `fetch_page` succeeded for the same pages. Route: page/search tools and alternative technical methods; not a global network-access gap.
- **Full page archival:** several long Apple/Google review and FTG comment pages were fetched in chunks but their complete raw text has not been committed. Route: archive complete payloads or explicitly continue staging; no affected source is considered exhaustively processed.
- **Prompt capture:** live prompt file remains a capture-status placeholder; `ISSUE-0001` is open. The current turn contains only a condensed summary, not the verbatim original. Route: ask the user to attach/paste the exact source and write it to the stable path; do not reconstruct missing wording from the summary.
- **Prompt abbreviations/terms:** `DLL`, `OVR`, `GK`, and `XI` are prompt shorthands whose exact current DLS26 UI/game terminology remains unverified. The Apple U.S. store description (`page-001-apple-us-dls-store`) exposes “Dream League Live”, and an FTG help-search result (`discovery-001-ftg-official-search`) uses “DLL (multiplayer) matches”; this is a candidate mapping, not yet an in-game terminology confirmation. Route: follow all FTG source links and inspect current in-game/help UI evidence; do not guess expansions for OVR/GK/XI.

No item is closed as “does not exist.” Research absence has not been established.


## Turn 57 — position/formation search note

Searches of FTG support returned generic development/stat pages and a formation-related link, but no DLS26-specific position-lock rule. The formation help article 7917587319313 was previously mapped by section/API metadata to Ultimate Clash Soccer (section 7900693036561); it is not DLS evidence. User-stated “no position locking” remains explicitly unverified.


## Turn 65 — blocked official TikTok embed routes

Two distinct alternate endpoints for the already-identified FTG Cult Heroes TikTok post (`/oembed` metadata and `/embed/v2/`) both returned HTTP 403 with no body (`page-321-tiktok-oembed-t65`, `page-322-tiktok-embed-t65`; details in `source_archive/t65_tiktok_embed_endpoint_attempts.md`). The original search snippet remains ambiguous, and these failures neither confirm nor refute its Cult Heroes route wording. Route, costs, and rewards remain open; position-lock behavior remains unverified.


## Turn 66 — UK Play storefront text remains ambiguous

The en-GB Google Play DLS26 listing (page-323) links the previously identified Cult Heroes event page and renders `Ends on 10/14` without a year, while the same listing’s update note says the Cult Heroes collection is “coming soon.” This is the same Play listing family as the U.S. page and storefront-only text; it does not verify an in-game deadline, route, or reward. Linked TikTok/Instagram profiles were blocked (403; page-324/page-325). In-game timer and acquisition route remain open.


## Turn 67 — official Play event-art URLs returned no image

The two Google Play image variants linked to the DLS26 Cult Heroes promo (`page-326`, `page-327`) returned HTTP 500 through `fetch_page`; no image bytes or visual/OCR data were received. This is a route/access failure, not a negative finding. No event-art, route/reward, or position-lock claim is inferred.


## Turn 71 — first-party general position wording is not a lock test

The existing FTG `core-principles` record (page-066) lists formation choices and pitch positioning as general AI inputs, but says nothing about DLS26 position eligibility, locks, or penalties. This is not DLS26-specific evidence and does not verify/refute the user-stated no-lock report. The T71 TikTok mobile URL for post 7437552025958763809 returned HTTP 403; no caption/body was obtained.


## Turn 72 — Apple storefront timing strings conflict

The structured U.S. Apple Lookup API record (`page-332`) reports DLS version 13.430, currentVersionReleaseDate 2026-09-16, and release notes calling Cult Heroes “coming soon,” while the existing Apple event card (`page-316`) says “LIVE EVENT” with boosted attributes. Same Apple/storefront source family; neither string establishes in-game availability, route, costs, or rewards. The unresolved user questions remain open.


## Turn 73 — FTG Events article is Score! Hero help, not DLS route evidence

FTG Help Center API result `What are Events?` (article 214386765) has `section_id` 203117609. The first-party section map `page-186-ftg-help-centre-root` identifies that as Score! Hero FAQs; DLS FAQs are 203117809. T73 mistyped the ID and misattributed the article to DLS; corrected in T74. The generic article does not establish any DLS26 Cult Heroes route/rewards. Page 1/3 was read in T73; page 2/3 in T74; page 3 remains unexamined.


## Turn 75 — broad Help Center query complete; gaps remain

FTG Help Center API pages 1–3 (52 search results) have been read. The final page contains generic account/privacy articles; the broad Hero query produced no explicit DLS26 Cult Heroes route/reward or position-lock instructions. This is not an exhaustion/absence finding. Web-search snippets were not tied to a unique post permalink; two direct TikTok URLs returned 403/no body. Do not use them as evidence. Route/rewards and position locks remain open.


## Turn 76 — official searches do not settle either open question

The focused FTG `Cult Hero Agents` API query matched only the already-read general DLS “How do I obtain more players?” article; it does not describe the event item. The `position lock` API query is only partially read (chunks 0–3/10 of 16 results, mixed FTG games). Resume at chunk 4; do not classify yet. A new TikTok URL returned 403/no body. Cult Heroes route/rewards and DLS26 position-lock verification remain open.


## Turn 77 — full FTG position-lock query still does not settle DLS26 behavior

The FTG `position lock` search (16 results, 10 chunks) is complete. DLS results mention Season Pass tier locks and general player stats, not a DLS26 squad-position lock rule. This is not proof of in-game absence. Preserve the user-stated no-lock claim as unverified; Step-3 device setup remains necessary.


## Turn 78 — formation-position query incomplete

FTG Help Center query `formation position`: 14 results, 9 rendered chunks. Only chunks 0–5 are read; visible hits are mixed across Score! Match, Ultimate Clash Soccer, and DLS. Resume chunks 6–8 before product-aware classification. The query does not verify DLS26 position-lock behavior.


## Turn 79 — official search follow-up

The complete FTG `formation position` response (14 results/9 chunks) mixes games and DLS player-stat/leaderboard material; it establishes no DLS26 position-lock behavior and does not establish absence. Three additional FTG/official-account search-result queries supplied no event-specific or lock-specific DLS26 evidence; their result cards are not fetched pages. Position-lock and Cult Heroes route/rewards remain open. See `source_archive/t79_official_search_triage.md`.


## Turn 80 — direct verification of official social lead pending

TikTok search results attributed to `@dreamleaguesoccer.ftg` contain potentially relevant Cult Heroes route/reward text, but mix captions and do not map the claims to exact video URLs. Two candidate TikTok URLs had already been blocked in earlier turns; one new candidate is queued. Do not promote search snippets to facts. Repeat YouTube/Instagram fetches yielded no new content (YouTube partial; Instagram 403). Position-lock remains open. See `source_archive/t80_official_social_leads.md`.


## Turn 81 — official social snippets unresolved

TikTok exact-phrase searches still blend Cult Heroes captions with unrelated DLS25 cards; the new candidate fetch returned 403. Facebook search card says “collect them in game now” but does not identify route/reward; direct page fetch returned 403. None establishes a current in-game route or reward. Position-lock remains unverified. See `source_archive/t81_tiktok_snippet_mapping.md`.


## Turn 82 — general FTG help does not verify Cult Heroes

The completed `Cult Hero Agent`, `Drafts Season Pass`, and `Drafts` Help Center queries returned generic DLS agent, Season Pass, Prize Ladder, and Dream Draft information plus other-game material. No Cult Heroes-specific event route or reward is described. Do not conflate generic Agents with Cult Hero Agents. Position-lock remains unverified. See `source_archive/t82_ftg_agent_draft_searches.md`.


## Turn 83 — storefront wording does not establish in-game route

The U.S. Apple App Store event page displays Cult Heroes as HAPPENING NOW / LIVE EVENT, with “Now available with boosted attributes.” This is a platform-store claim only and may be the same event localization previously seen in German; it does not establish in-game accessibility, route, cost, or exact reward. FTG’s generic Events article is not Cult-specific. Position lock remains unverified. See `source_archive/t83_live_event_and_storefront.md`.


## Turn 84 — live-events query still partial

FTG `live events` query: chunks 0–6/10 read; resume chunks 7–9. A generic DLS “Super Players” article mentions Events/rare packages, but no source links Cult Heroes to that category or to Cult Hero Agents. Do not infer route/reward or absence. Position locking remains unverified.


## Turn 85 — completed FTG `live events` query

All 10 chunks/18 results were read. The mixed response gives generic Events/Super Players help and unrelated material, not a Cult Heroes-specific route/reward. It does not establish absence beyond the query result set. Position-lock remains unverified.


## Turn 86 — `Special Players Events` query partial

FTG query has 10 results/8 chunks; only chunk0 read. Visible generic card-colour, Agent, Prize Ladder, and stats articles do not answer Cult Heroes. Resume chunks1–7; do not infer absence. Position-lock remains unverified.


## Turn 87 — `Special Players Events` still partial

FTG Help Center query now read through chunk6/8; chunk7 remains. Visible content is generic player/stats help, not Cult Heroes-specific. No absence inference; position-lock remains unverified.


## T88 update — unresolved first-party checks
The FTG `Special Players Events` response is complete (chunks 0–7/8). One exact Help Center query was repeated from an existing URL; two new exact queries yielded zero matches, and official-site search results were generic/older. None verifies Cult Heroes availability, route, cost, or rewards. DLS26 position-lock remains user-stated/unverified; device setup and in-game capture remain the decisive path. No gap closed. Provenance: `source_archive/t88_ftg_special_players_searches.md`.


## T89 update — source repetition, no gap closure
The `DroidCheat` Cult Heroes gameplay page re-fetched in T89 is the same exact URL already read in T61; do not treat it as independent evidence. The YouTube search results are secondary/discovery-only, and a channel-ID query returning zero results is not an absence finding. Route/rewards and DLS26 position-lock remain open.
