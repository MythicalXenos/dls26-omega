# T127 — Canada event endpoint and direct Reddit parent search

Date: 2026-10-06 Asia/Dhaka. Two retrieval calls in parallel; per-call timestamps not exposed.

## First-party store event endpoint

`functions.fetch_page` requested `https://amp-api.apps.apple.com/v1/catalog/ca/apps/1462911602/in-app-events?l=en`. Tool status was `success`, with an empty content string. No JSON, title, event metadata, or error was returned. This does not establish whether the app has events or whether Cult Heroes is available/unavailable. The exact URL is new relative to previously recorded US and UK endpoints; do not infer absence from the empty payload.

## Parent Reddit post trace

`functions.fetch_page` requested `https://www.reddit.com/r/DreamLeagueSoccer/search.json?q=sci9uc0c02th1%20OR%20%22cult-heroes-v0-sci9uc0c02th1.jpeg%22&restrict_sr=1&sort=new&limit=100` to search the DLS subreddit for image identifier `sci9uc0c02th1` and filename `cult-heroes-v0-sci9uc0c02th1.jpeg`. The tool returned HTTP 403 and no body/results. This does not show whether a parent post exists. Do not repeat this exact URL. The source lead remains: Resolve the original Reddit post permalink, uploader, and date for image-search preview `cult-heroes-v0-sci9uc0c02th1.jpeg`; the returned page link was only the subreddit root. The saved in-game image is `source_archive/t125_image_search_results/reddit_cult_heroes_agent_event_ui.jpg`.

## State

No gameplay fact, route/reward detail, cost, current availability, or position-lock evidence was established. T125’s user-generated screenshot remains a limited visual observation; the parent post/date remain unknown. Keep all research dimensions open and avoid absence inferences.

## Reset recovery

T127 began on the recurring reset signature (`fb9a2c0`). The opening clock entry was written first. Archived 337 files to `/tmp/dls26-t127-recovery-20261006015438.tar.gz`, SHA-256 `b11db1fd0e79357a1ed31059416e459b092f7b34c416c57a2f19875333eaf32d`; fetched/restored the fixed remote branch at `0f0bffe`, upstream, and repo-local identity `DLS26 Omega <omega@dls26.local>`. All 337 files were byte-verified after restoring. ISSUE-0014 occurrence #89; no content loss.
