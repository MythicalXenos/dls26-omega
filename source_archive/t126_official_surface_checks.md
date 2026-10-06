# T126 — distinct first-party surface checks and parent-link search

Date: 2026-10-06 Asia/Dhaka. Four retrieval calls: one direct YouTube channel-page fetch, one Apple in-app-events API fetch, and two web searches. Per-call timestamps are not exposed; timestamps in ledger are T126 closeout reconciliation time.

## Direct page/API checks

1. `functions.fetch_page` requested `https://www.youtube.com/@firsttouchgames/videos` (a URL distinct from the previously read launch-trailer video and the failed `feeds/videos.xml?user=firsttouchgames` request). Tool status was `success`, but the response body began `Error 401 (Bad Request)` followed by a generic signed-out YouTube shell and channel label. No video list, post, caption, gameplay, or Cult Heroes item was returned. Do not retry this exact URL or infer absence from it.
2. `functions.fetch_page` requested `https://amp-api.apps.apple.com/v1/catalog/gb/apps/1462911602/in-app-events?l=en`, a distinct UK catalog endpoint. Tool status was `success`; content was empty. No JSON, event metadata, title, or error was received. Empty response does not establish event absence or current Cult Heroes status.

## Search-result checks

- Exact query: `site:tiktok.com/@dreamleaguesoccer.ftg "Cult Heroes" Agents events DLS26 First Touch Games`. Search status `success`, results array empty. No page fetched and no absence inference.
- Exact query: `site:reddit.com/r/DreamLeagueSoccer "Agentes Heróis Cultos" OR "sci9uc0c02th1"`. Search status `success`; three result cards were returned, all previously visited TikTok URLs: `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7588197165965593888`, `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7477999051343007008`, `https://www.tiktok.com/@dreamleaguesoccer.ftg/video/7437552025958763809`. No Reddit parent URL surfaced. Captions in the search payload are interleaved/mixed and do not reliably bind Cult Heroes route wording to a particular video. The ambiguity was already documented in T75/T81; no caption is promoted here, and none of those exact URLs was fetched again.

## Interpretation

No new game fact, event-availability claim, cost/reward statement, or position-lock evidence was established. T125’s single Reddit-labeled UI screenshot remains an unverified visual observation; exact route thresholds, current status, and parent post/date remain unresolved. DLS26 position-lock remains `user-stated` and unverified. No exhaustion declaration or spending advice.

## Reset recovery

The first T126 shell call was made on reset commit `fb9a2c0` with workspace files untracked. A recovery tar at `/tmp/dls26-t126-recovery-20261006014551.tar.gz` contains 335 files/members, SHA-256 `64217662963d78ed158005d69084deddb02fbdfc44a39eae8fcc9b1bc7dda555`. The file was created before the malformed clock timestamp was corrected. The remote fixed branch was fetched and restored at `ed04d77`; all 335 files were byte-verified against the archive before clock normalization. Repo-local identity restored to `DLS26 Omega <omega@dls26.local>`, upstream `origin/arena/01a1022d-dls26-omega`. The initial pipeline wrote only `2026-10-06 01:45:51 +0000` rather than a prefixed local clock line; it was corrected to `T126 START 2026-10-06 07:45:51 +0600` and documented as ISSUE-0014 occurrence #88.
