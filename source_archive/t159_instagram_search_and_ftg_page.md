# T159 — first-party social-post lookup and FTG landing page

Date: 2026-10-06, Asia/Dhaka. Five retrieval calls: four targeted `functions.web_search` queries and one `functions.fetch_page`.

## Instagram and YouTube search results

1. Exact query `site:instagram.com/playdls "Cult Hero Agents" "Events" "Drafts"` — only the `@playdls` Instagram profile result; no Cult Heroes post/permalink/date.
2. Exact query `site:instagram.com/p/ "Cult Hero Agents" "DLS26" "Dream League Soccer"` — empty result set.
3. Exact query `site:instagram.com/playdls "Cult Heroes are coming" "Cult Hero Agents"` — only the same profile-level result.
4. Exact query `site:youtube.com/@firsttouchgames "Cult Hero Agents" "DLS26"` — only the `firsttouchgames` YouTube channel profile; no Cult Hero Agents post/video.

These searches did not retrieve a post. Do not infer that no such post exists. The direct Instagram page/API failures from T156 remain unchanged; no retries were made in T159.

## FTG product page

`functions.fetch_page` requested `https://www.ftgames.com/dls` and returned final URL `https://www.ftgames.com/games` with tool status `success` (numeric HTTP status not exposed). The generic FTG Games page describes DLS in general terms (players, divisions, motion capture, commentary/customization) and lists store/Facebook/trailer links. It contains no Cult Heroes acquisition route/reward details and is not DLS26-version-specific evidence.

## Limits

No first-party Cult Heroes post or permalink/date retrieved. Route/rewards remain unconfirmed; “DLS26 has no position locking” remains `user-stated`, verification owed. No global-absence inference, spending advice, exhaustion declaration or dimension closure.

Ledger after T159: **857 records / 634 visited URL attempts / 390 unvisited leads**.
