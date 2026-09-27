# TOPIC: Game identity, naming, package, and version history

**Sweep:** STATE_1_RESEARCH_SWEEP (bootstrap Step 1). **Opened:** 2026-09-27. **Exhaustion declaration:** NONE — this topic is open and actively being researched. Nothing here is settled.

Why this topic exists first: every other claim in the KB carries a `game_version` field, and advice is version-sensitive (PROMPT.md §7, §9). Without an established identity and version, nothing else can be temporally validated. The franchise-continuity rule in the PROMPT.md preamble also makes naming a Patch Response trigger, so the name has to be pinned down.

---

## Claims

- CLAIM: The game the user plays is published by First Touch Games Ltd. and is the continuously-updated product marketed as "Dream League Soccer 2026" (DLS26); FTG's own site titles it "Dream League Soccer" without a year.
  - source: S-0002 (page-render, firsttouchgames.com/games), S-0001 (discovery-search, appbrain echo of the Play listing)
  - first_published: FTG page undated; appbrain listing pageAge 2026-09-25
  - last_verified: 2026-09-27 by page-render + discovery-search
  - confidence: Speculative (two sources, but one is an aggregator echo of a store listing and the store listing itself has not been fetched; origin-tracing not yet done)
  - volatility: volatility-High
  - volatility_dimensions: patch-triggered: a rebrand or title change in a store listing or FTG channel | event-triggered: an annual re-title (the franchise has carried year suffixes), a licensing change
  - origin: PARTIAL DIRECT — FTG's own page is first-party documentation for the fact that FTG publishes a game called Dream League Soccer, but the "2026" title and its continuity with the older product rest on an unfetched store listing
  - independence: NOT DOCUMENTED — appbrain is an echo of Google Play, so it is not independent of the store. One real source so far (FTG) plus one echo.
  - deception_screen: FTG clean (marketing copy, no claim-specific incentive); appbrain none detected (aggregator)
  - datamining: pending-confirmation (flagged 2026-09-27; blocked because no APK or client asset has been obtained yet — see gaps G-0004)
  - evidence_class: verified (tool output), incomplete
  - game_version: n/a (identity claim)
  - notes: PROMPT.md's own use of "DLS26" is not evidence; the franchise-continuity rule requires treating a rebrand announcement as a Patch Response trigger.

- CLAIM: The Android package identifier for DLS26 is `com.firsttouchgames.dls7`.
  - source: S-0001 (appbrain URL path and body), S-0002 (FTG's own Google Play link `play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en`)
  - first_published: FTG page undated; appbrain pageAge 2026-09-25 and 2026-07-07
  - last_verified: 2026-09-27 by page-render (FTG's own outbound link) + discovery-search
  - confidence: High Confidence (2 sources, one of them first-party FTG; but see independence — the Play listing itself is still unfetched, so this is provisional)
  - volatility: volatility-Frozen (a package id cannot change without a new store listing, i.e. a major-version/FTG-stated replacement event)
  - volatility_dimensions: patch-triggered: none — package ids do not change with patches | event-triggered: a store relisting or rebrand that ships a new package
  - origin: DIRECT — FTG's own published store link contains the id; checkable against the Play Store URL itself
  - independence: FTG (official, first-party, published link) and appbrain (database-tool/aggregator). Different source types, but appbrain's id necessarily descends from the same store listing, so its independence is weak; the FTG link is the checkable origin and carries the claim.
  - deception_screen: clean on both
  - datamining: pending-confirmation (flagged 2026-09-27; blocked because no APK obtained — this id is exactly what Step 2 needs to target, so resolving it matters)
  - evidence_class: verified
  - game_version: all versions observed 2026-06 → 2026-09 (13.340, 13.410, 13.420, 13.430)
  - notes: CONSEQUENCE FOR STEP 2 — every search for APKs, datamining repos, and asset dumps must target `com.firsttouchgames.dls7`, not `dls2026`/`dls26`. A shell probe in this session used the wrong id (recorded in S-0007) and must not be cited as evidence about any URL. The `dls7` id also indicates the marketing year and the internal package numbering have diverged — relevant to how FTG versions the franchise.

- CLAIM: The Apple App Store listing for this product is `apps.apple.com/us/app/dream-league-soccer-2020/id1462911602`.
  - source: S-0002 (FTG's own outbound App Store link)
  - first_published: undated FTG page
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (single source; listing unfetched; the "2020" slug is a strong hint that the listing is the same continuously-updated product since 2019/2020, which is exactly what needs verifying rather than assuming)
  - volatility: volatility-Low (store slug/id stable once issued)
  - volatility_dimensions: patch-triggered: none | event-triggered: a store relisting
  - origin: DIRECT for "FTG links to this listing"; NONE FOUND for what the listing currently says
  - independence: single source
  - deception_screen: clean
  - datamining: not applicable (no iOS binary route)
  - evidence_class: verified (that the link exists), unverified (its contents)
  - game_version: n/a
  - notes: appbrain (S-0001) reports the Play listing has existed since December 2019 — consistent with the 2020 App Store slug, i.e. one product renamed by year, not a 2026 release. NOT ESTABLISHED. Also: PROMPT.md's franchise-continuity rule means all prior-version knowledge (DLS20 through DLS25) is in scope as continuity, not as discarded history.

- CLAIM: Client version numbers observed in the wild for DLS26 in 2026: 13.340 (reported updated 2026-06-19), 13.410 (reported as the version before 13.420), 13.420 (reported released 2026-09-01 by one source, and also reported as the "Summer Spotlight update" launched 2026-05-28 by the SAME source), 13.430 (reported latest, updated 2026-09-14).
  - source: S-0001 (three results: fifaworldcupnews, appbrain current mirror, appbrain stale mirror)
  - first_published: appbrain mirrors pageAge 2026-07-07 and 2026-09-25; fifaworldcupnews pageAge 2026-07-23
  - last_verified: 2026-09-27 by discovery-search (depth 1)
  - confidence: **Disputed-pending** — NOT yet Disputed in the confidence-tier sense, because research is far from exhausted. Currently Speculative at best; the conflict is open under the Conflict Protocol (log ref DLS26-C1).
  - volatility: volatility-Critical (changes roughly monthly by appearance; every other claim's `game_version` field depends on it)
  - volatility_dimensions: patch-triggered: any client update | event-triggered: seasonal content drops ("late summer update", "Cult Heroes" collection)
  - origin: NONE CHECKABLE YET — all three are secondary. The checkable origins are the Google Play listing's "What's new"/version field, the App Store version history, and an APK's own manifest. All three are owed.
  - independence: NOT independent. appbrain's two mirrors are the same aggregator at two dates; fifaworldcupnews is an SEO farm. Effective independent-source count for version data: possibly 1 (the store listings, unfetched).
  - deception_screen: fifaworldcupnews — incentive OBSERVED (SEO/ad content farm, "Everything You Need to Know" framing, self-contradictory dating: pageAge 2026-07-23 while asserting September 2026 release facts). Outcome: capped at Speculative, logged in deception_register.md screening-outcomes table. Its "13.420 = Summer Spotlight, launched May 28" and "13.420 released Sept 1" cannot both be right, which is a fabricated-specificity indicator. appbrain — no incentive detected, but it is an echo of the store.
  - datamining: pending-confirmation (flagged 2026-09-27; an APK manifest or `versionName` string would settle it directly — blocked on gaps G-0004)
  - evidence_class: verified tool output reporting UNVERIFIED claims
  - game_version: this IS the version claim
  - notes: TIME-ELAPSED AWARENESS (PROMPT.md §5 PATCH RESPONSE): today is 2026-09-27, so a 2026-09-14 update is ~13 days old — recent enough that community processing may be incomplete; findings about it must be flagged as early post-patch. Next actions, in order: (1) page-render the Play Store listing for `com.firsttouchgames.dls7`; (2) page-render the App Store listing; (3) page-render appbrain's current page directly rather than via snippet; (4) search FTG's own channels for patch notes; (5) check web.archive.org for version history.

- CLAIM: FTG states DLS has "over 4,000 FIFPro™ licensed players" and "8 divisions".
  - source: S-0002 (FTG official games page, marketing copy)
  - first_published: undated page, retrieved 2026-09-27
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (first-party but undated marketing copy; AUTHORITY IS NOT EVIDENCE and PLANTED AND DECOY DATA both apply — FTG-published values are never self-validating)
  - volatility: volatility-High
  - volatility_dimensions: patch-triggered: roster size changes with database updates; division count changes with a system overhaul | event-triggered: FIFPro licensing changes, season boundaries
  - origin: NONE CHECKABLE YET — the client's own player database and division config would be direct evidence; owed to Step 2
  - independence: single source (first-party)
  - deception_screen: clean; marketing incentive is general (sell the game) rather than claim-specific
  - datamining: pending-confirmation (flagged 2026-09-27; blocked on APK acquisition, gaps G-0004)
  - evidence_class: verified tool output, unverified claim
  - game_version: unknown — the page carries no version
  - notes: Both numbers matter downstream: player-count bounds the candidate pool enumeration (PROMPT.md §10 CANDIDATE POOL — the pool size must be recorded), and division count feeds career-mode progression research. Neither may be used as a working figure until checked against a database or the client.

- CLAIM: FTG's other current titles are Score! Hero 2 (`com.firsttouchgames.story`), Ultimate Clash Soccer (`com.firsttouchgames.mpx`), and Score! Match (`com.firsttouchgames.smp`).
  - source: S-0002 (FTG official games page)
  - first_published: undated page
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (single first-party source; low stakes)
  - volatility: volatility-Low
  - volatility_dimensions: patch-triggered: none | event-triggered: a new title launch or a title's discontinuation
  - origin: DIRECT (first-party documentation of FTG's own portfolio)
  - independence: single source
  - deception_screen: clean
  - datamining: not applicable
  - evidence_class: verified
  - game_version: n/a
  - notes: In scope because PROMPT.md §5 lists "FTG as a company" as a research target and because shared-engine lineage across FTG titles is a legitimate hypothesis source for how DLS26 systems may work — but per the never-assume-shared-mechanics rule, nothing may be transferred from those titles to DLS26 without DLS26-specific evidence. Score! Match is FTG's real-time multiplayer title, which makes it relevant background for DLL/online-infrastructure research only.

---

## Open questions this topic owns

1. What is the current client version, exactly, and what did each 2026 version change? (Conflict DLS26-C1.)
2. Is there a public FTG patch-notes archive, or are changelogs only in store listings?
3. Which regional store listings differ, and do any carry different version numbers or content ratings? (PROMPT.md §5 requires all regional stores checked.)
4. Has the title been rebranded, and does FTG announce rebrands anywhere monitorable? (Patch Response trigger.)
5. What is the mapping between marketing year (2026) and internal versioning (13.x) and package id (dls7)?
6. Does the client version differ between Android and iOS at any given time?
7. What is FTG's historical update cadence across DLS versions (evidence for the volatility model, PROMPT.md §9 — to be built from observation, not priors)?

## Leads discovered and not yet visited (mirrored in `logs/sources_visited.json` → `frontier.unvisited_leads`)

Play Store `com.firsttouchgames.dls7` (all regions); App Store id1462911602 (all storefronts); firsttouchgames.com root and /support; FTG Facebook, Instagram (@playdls), TikTok (@dreamleaguesoccer.ftg), Twitter/X (@firsttouchgames); the FTG YouTube trailer; appbrain current page fetched directly; web.archive.org for FTG and store-listing history.
