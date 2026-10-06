# T124 — App Store/YouTube/archive probes and local screenshot reinspection

Date: 2026-10-06 Asia/Dhaka. Three distinct external retrievals plus two local image reads.

## External endpoint checks

1. Apple AMP: `https://amp-api.apps.apple.com/v1/catalog/us/apps/1462911602/in-app-events?l=en`. `functions.fetch_page` returned status `success` but an empty content string; no JSON or event data. This is not evidence that the app has no events.
2. YouTube legacy feed: `https://www.youtube.com/feeds/videos.xml?user=firsttouchgames`. Returned a 404 page stating the requested `/feeds/videos.xml?user=firsttouchgames` was not found. No feed items; this does not establish absence of official videos.
3. Internet Archive CDX: `https://web.archive.org/cdx/search/cdx?url=www.firsttouchgames.com%2Fgames%2Fdls&output=json&filter=statuscode%3A200&fl=timestamp%2Coriginal%2Cstatuscode%2Cdigest&collapse=digest`. Returned JSON `[]` for this exact archived URL query. No snapshot URL discovered; this is not archive-wide absence.

## Existing S-0025 images re-read in this turn

These are the already saved Reddit-sourced, user-generated in-game captures from `prior_sessions/2026-09-27_01a0e3cd/kb/evidence/`, originally logged as S-0025. This is a local reinspection, not a new or independent source. SHA-256: Dybala `8064e27c3f00a08586a79554e527ae54b782bd4b2ec524b3ad277536522e3773`; Isco `4711c206e454504e76a819e989f192f3394dd047a5b8a0266a3c5aff3753231c`.

- Dybala screenshot: visibly shows a Spanish `JUGADOR FICHADO` confirmation and a PAULO DYBALA card. It does not identify an acquisition route.
- Isco screenshot: visibly shows a `PLAYER SIGNED` ISCO modal while the background shows `LIVE TRANSFERS` and a `CULT HEROES` subsection. This co-presence is consistent with a transfer-market route, but the image does not show which listing produced the modal or a transaction price. It does not establish reward terms or position behavior. Treat the screenshot as user-generated in-game UI with the original S-0025 authenticity caveats; do not promote the Reddit post title/text as game fact.

The screenshots add limited in-game UI context, not a confirmed route, price, or reward. Cult Heroes route/rewards and DLS26 position-lock remain unresolved; position-lock remains `user-stated` and unverified.
