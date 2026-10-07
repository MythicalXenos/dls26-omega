# T151 — FTG `change formation` response, page 2 chunks 5–10

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls (chunks 5, 6, 7, 8, 9 in parallel and chunk 10); exact per-call timestamps and HTTP statuses were not exposed. All tool responses reported `success`.

## Retrieved content

Endpoint: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=change+formation`. Chunks 0–10 of 15 are now read (chunk 0 in T137, 1–4 in T150, 5–10 in T151); chunks 11–14 remain unread. This is page 2 of a mixed 48-result FTG Help Center query, not a DLS26-specific document.

Visible results include:
- DLS help article ID `360008831518`, “Why are my players auto-switching all the time?” (updated 2026-07-29 in returned metadata). Its text describes default control switching to the closest player while defending and a Settings > Controls > Auto Switch option. This concerns player control selection; it is not a squad-position lock rule and is not version-stamped as DLS26. The direct article URL `https://firsttouch.zendesk.com/api/v2/help_center/en-us/articles/360008831518.json` was returned but not fetched; retained as a low-priority unvisited lead.
- A game-difficulty article explicitly discussing DLS25, a generic Season Pass article, and other FTG-title results. Do not transfer DLS25/other-title details to DLS26.
- The T150 chunk-boundary snippet about default player positions following formation/ball position remains unattributed to a title/ID/version in the captured fragment; do not promote it.

## Conclusion and limits

No DLS26-specific position-lock behavior is established. The user's “DLS26 has no position locking” remains `user-stated` and unverified. No Cult Heroes route/reward evidence. The query remains partial; no global-absence inference, spending advice, exhaustion declaration or dimension closure.

Ledger after T151: **822 records / 618 visited URL attempts / 395 unvisited leads**.
