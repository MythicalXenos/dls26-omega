# Turn 73 — official Help Center search API, “Cult Heroes”

Requested `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes`. The public Zendesk API reports 52 matches across 3 pages. Page 1 (25 results) was completely rendered across chunks 0–5; pages 2–3 were not fetched. The broad search also returns unrelated Score! Hero/8 Ball Hero matches (the string “Hero” is overmatched), so it is not a focused Cult Heroes index.

One DLS FAQ result in the DLS section (`section_id` 203117809) is article 214386765, “What are Events?” Metadata in the API result: created 2016-12-07, updated 2026-07-09. Its returned body says: “We may offer permanent or time-based events, available in the ‘Events’ section. These can be played alongside your main story in the game.” This is general DLS help text; the body has no DLS26 version stamp and does not name Cult Heroes, Agents, Draft, Season Pass, event cost, or reward. It does not establish that the current Cult Heroes collection is accessed through that section.

The API exposes two reachable unvisited leads: the direct article URL `https://support.ftgames.com/hc/en-us/articles/214386765-What-are-Events` and its page-2 route `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=Cult+Heroes`. No conclusion is drawn from the unexamined pages 2–3.
