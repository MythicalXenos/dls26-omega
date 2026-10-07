# Turn 74 — FTG Help Center direct article and search page 2

## Recovery context
Turn opened on reset signature: local branch `fb9a2c0` with 228 project files untracked. Remote fixed branch tip `4367516` was restored; all 228 tracked files matched the preserved workspace byte-for-byte after normalizing only the T74 clock-start append. ISSUE-0014 occurrence #36 records the recovery.

## Direct article fetch
- URL: `https://support.ftgames.com/hc/en-us/articles/214386765-What-are-Events`
- Tool/status: `functions.fetch_page`, status `success`, one complete chunk; numeric HTTP status not exposed. Title: “What are Events? – First Touch Games Ltd”.
- Full body: “We may offer permanent or time-based events, available in the \"Events\" section. These can be played alongside your main story in the game.”
- The T73 API result assigns this article `section_id` 203117609. First-party section-map record `page-186-ftg-help-centre-root` identifies 203117609 as **Score! Hero FAQs** (DLS FAQs are 203117809). The generic body and related links do not make it DLS/DLS26 evidence. It does not mention Cult Heroes, cost/reward, or position locks.

## Search API page 2
- URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=Cult+Heroes`
- `functions.fetch_page` chunks 0–4 all succeeded; the API reports count 52, page 2/3, per_page 25. Page 2 is complete; page 3 is not. Results continue broad mixed-game Hero matches, including Score! Hero and 8 Ball Hero help topics and generic FTG help. No DLS26 Cult Heroes route/rewards or position-lock guidance surfaced on pages 1–2. This is not evidence of absence: page 3 remains unread and the query is broad.
- Explicit `next_page`: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=3&per_page=25&query=Cult+Heroes` (retained as an unvisited lead).

## T73 metadata/product-attribution correction
The API result for article 214386765 says `section_id` **203117609**, not 203117809. The existing FTG section map `page-186-ftg-help-centre-root` identifies that as Score! Hero FAQs; DLS FAQs are 203117809. T73’s “DLS FAQ” attribution was wrong and has been withdrawn in the ledger, KB, gap log, queue, snapshot, and handoff. Do not use this article as DLS26 route evidence.
