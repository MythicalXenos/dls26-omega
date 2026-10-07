# T121 — targeted Reddit discovery and FTG Help Center query

Date: 2026-10-06 Asia/Dhaka. Three retrieval executions.

## Reddit-scoped web searches

1. Exact query: `site:reddit.com/r/DreamLeagueSoccer "Cult Heroes" "Agent" "DLS26" screenshot`. `functions.web_search` returned status `success`, an empty result array; the tool exposes no HTTP status. No page, post, image, or gameplay capture was fetched.
2. Exact query: `site:reddit.com/r/DreamLeagueSoccer "out of position" "DLS26" formation players`. `functions.web_search` returned status `success`, an empty result array; the tool exposes no HTTP status. No page, post, image, or gameplay capture was fetched.

Each search result is limited to its exact query and does not establish absence.

## FTG Help Center API

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20unlock`. `functions.fetch_page` status `success` (HTTP status not exposed). The response reported one result, no next page: “What does the ‘Reset Game’ button do?” (article 360001808418, section ID 360000489137). The embedded article is about game reset/Hero Bux; it is not a DLS26 Cult Heroes acquisition or position-lock source. No direct article-page fetch was performed.

No Cult Heroes route/reward or DLS26 position-lock evidence was obtained. Both questions remain open; position-lock remains user-stated/unverified. No absence inference or spending advice.
