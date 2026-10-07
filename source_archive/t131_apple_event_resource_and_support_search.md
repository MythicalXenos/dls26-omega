# T131 — Apple event resource and FTG Special Card/Agents query

Date: 2026-10-06 Asia/Dhaka. Two first-party retrievals; individual timestamps not exposed.

## Apple direct event resource

`functions.fetch_page` requested `https://amp-api.apps.apple.com/v1/catalog/us/in-app-events/6802988564?l=en`, for the already known Cult Heroes App Store event ID `6802988564`. Tool status was `success`, but content was empty. No event attributes, route, reward, cost, or current-status fields were returned. This is not evidence of event absence or in-game availability.

## FTG Help Center query

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Special%20Card%20Agents`. Response status `success`, one page/chunk, count=2. The returned results are the already-read general FAQ “How do I obtain more players?” (article 360004066417) and a generic card-colour FAQ (article 214385645). The generic Agent material is not Cult Heroes-specific; do not use it to infer Cult Hero Agent guarantees, sources, costs, or card outcomes. No position-lock rule appears in these result summaries.

## Interpretation and recovery

No new game fact. Cult Heroes route/rewards and DLS26 position-lock remain open; no absence inference or exhaustion declaration.

T131 began on reset `fb9a2c0`; clock was recorded first. Archived 345 files at `/tmp/dls26-t131-recovery-20261006021338.tar.gz`, SHA-256 `61d8b14a7b18249ae1635add81dd124ca25892ccd39ed2ae184d6ffdcbf1ff7d`; restored the fixed branch at `ff69681`, upstream and repo-local identity `DLS26 Omega <omega@dls26.local>`, and byte-verified all files. ISSUE-0014 occurrence #93; no content loss.
