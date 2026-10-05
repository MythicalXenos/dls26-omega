# Turn 65 — official TikTok alternate endpoint attempts

The targeted FTG TikTok post is `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809`. Its direct-page fetches were previously recorded as HTTP 403 (T54/T56). A search-result snippet had combined a DLS25 title/date with Cult Heroes route text; attribution to that exact post remained unclear.

## page-321 — official oEmbed metadata endpoint
- Requested: `https://www.tiktok.com/oembed?url=https%3A%2F%2Fwww.tiktok.com%2F%40dreamleaguesoccer.ftg%2Fvideo%2F7437552025958763809`
- `fetch_page` returned HTTP 403. No JSON, metadata, caption, or body.

## page-322 — official embed player endpoint
- Requested: `https://www.tiktok.com/embed/v2/7437552025958763809`
- `fetch_page` returned HTTP 403. No player, caption, metadata, or body.

These were two distinct official TikTok endpoint URLs, not retries of the original video-page URL. The failures do not confirm or refute the search-snippet route wording; no Cult Heroes route, cost, reward, or position-lock claim is promoted. Do not repeat either exact endpoint.
