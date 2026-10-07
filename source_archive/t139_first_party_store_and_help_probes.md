# T139 — first-party store and FTG phrase probes

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls; successful page chunks noted below. Per-fetch timestamps are not exposed.

## Apple U.S. current listing via iTunes Lookup

Exact URL: `https://itunes.apple.com/lookup?id=1462911602`. `functions.fetch_page` chunks 0–1 returned success; API resultCount=1. The record reports version 13.430, currentVersionReleaseDate `2026-09-16T14:03:27Z`, and releaseNotes: “It’s our late summer update. Check out what’s new: •New Special Players – ‘Cult Heroes’ collection, coming soon! •Bug Fixes – Dozens of issues sorted…” It also returns USD and a U.S. trackViewUrl, so this is the same Apple U.S. storefront family/data as T72, not independent corroboration. This endpoint returned one current app record, not a historical version list. The dated listing copy does not establish current in-game availability, route, cost, or reward.

## Bangladesh regional storefront probes

- Apple events API exact URL `https://amp-api.apps.apple.com/v1/catalog/bd/apps/1462911602/in-app-events?l=en`: `functions.fetch_page` chunk 0 returned success with empty content. No event payload was available; do not infer regional/global absence.
- Apple Lookup exact URL `https://itunes.apple.com/lookup?id=1462911602&country=bd`: `functions.fetch_page` chunk 0 returned success with resultCount=0/results=[]. This exact regional lookup is not an app-wide or in-game absence finding.
- Google Play exact URL `https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en&gl=bd`: chunk 0/2 returned success. It renders the DLS 2026 listing and generic app copy/features (including generic Agents/Scouts and regular events) and re-lists the already-known Play screenshots #1–24. No Cult Heroes-specific route or reward is stated in the visible chunk. Chunk 1 remains unread; the listing is a storefront, not an in-game capture. Do not infer absence.

## FTG Help Center phrase query

Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Drafts%20Agents`: chunk 0 returned success, count=0/page_count=0/results=[]. This phrase only; no global absence or event-mechanics conclusion.

## Recovery

T139 began on reset checkout `fb9a2c0`; clock was recorded first. Archived 363 files at `/tmp/dls26-t139-recovery-20261006085546.tar.gz`, SHA-256 `661713573ed41f5eac2258a4eabce2d5ae5ce0b70178b291519b680bb811cd81`; fetched/restored pushed tip `678a73a`, restored upstream and repo-local identity, and byte-verified all 363 files. ISSUE-0014 occurrence #101.
