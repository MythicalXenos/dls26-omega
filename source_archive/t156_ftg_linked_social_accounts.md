# T156 — FTG-linked DLS social accounts

Date: 2026-10-06, Asia/Dhaka. Six retrieval calls; exact per-call timestamps not exposed.

## Attempts

1. `functions.fetch_page` requested `https://www.instagram.com/api/v1/users/web_profile_info/?username=firsttouchgames_official` — HTTP 403, no profile JSON/content.
2. `functions.web_search` exact query `site:youtube.com/@FirstTouchGames "Cult Heroes" "Dream League Soccer"` returned the `firsttouchgames` YouTube channel result `https://www.youtube.com/@firsttouchgames`.
3. `functions.fetch_page` requested `https://www.youtube.com/@firsttouchgames` — tool status `success`; numeric HTTP status not exposed. The body starts with a generic `Error 401 (Bad Request)` stanza, then renders the channel page and profile content. Do not call that a numeric HTTP 401 response. The page shows a DLS26 launch trailer and general launch text, and links to Instagram `https://www.instagram.com/playdls/`, Facebook `https://www.facebook.com/dreamleaguesoccer`, TikTok `https://www.tiktok.com/@dreamleaguesoccer.ftg`, and `https://www.ftgames.com/dls`. It lists the official DLS26 teaser `https://www.youtube.com/watch?v=gpvjf6qVl5c` and older DLS videos. No Cult Heroes acquisition route or reward details in the visible channel content.
4. `functions.fetch_page` requested the channel-linked Instagram `https://www.instagram.com/playdls/` — HTTP 403, no profile/posts.
5. `functions.fetch_page` requested `https://www.instagram.com/api/v1/users/web_profile_info/?username=playdls` — HTTP 403, no profile JSON/posts.
6. `functions.web_search` exact query `site:instagram.com/playdls "Cult Heroes" "Dream League Soccer"` returned one `Dream League Soccer (@playdls)` profile result with general DLS26 bio text; no Cult Heroes-specific post/result. Search coverage is limited, not absence evidence.

## Interpretation boundaries

The FTG YouTube channel's own page links the DLS Instagram, Facebook and TikTok handles above; this is a first-party account-discovery lead, not proof of current Cult Heroes availability or route. The Instagram pages and data endpoints were blocked; no content was retrieved. The visible YouTube page is general launch material. Cult Heroes route/rewards remain unconfirmed; “DLS26 has no position locking” remains `user-stated`, verification owed. No global-absence inference, spending advice, dimension closure or exhaustion declaration.

Ledger after T156: **840 records / 627 visited URL attempts / 390 unvisited leads**.
