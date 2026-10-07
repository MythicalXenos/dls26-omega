# Turn 73 — official Help Center search API, “Cult Heroes”

Requested `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes`. The public Zendesk API reports 52 matches across 3 pages. Page 1 (25 results) was completely rendered across chunks 0–5; pages 2–3 were not fetched at the time. The broad search returns unrelated Score! Hero/8 Ball Hero matches (the string “Hero” is overmatched).

One result is article 214386765, “What are Events?” The API metadata gives `section_id` **203117609** (created 2016-12-07, updated 2026-07-09). The already-recorded first-party FTG section map (`page-186-ftg-help-centre-root`) identifies 203117609 as **Score! Hero FAQs** and 203117809 as **DLS FAQs**. T73 had transcribed the ID as 203117809 and incorrectly called the article a DLS FAQ; T74 corrects that mistake. The returned article body says: “We may offer permanent or time-based events, available in the ‘Events’ section. These can be played alongside your main story in the game.” This is Score! Hero help text, not DLS/DLS26 route evidence.

The API exposed the direct article URL and page-2 route, both followed in T74. No conclusion was drawn from page 3, which remains unexamined.
