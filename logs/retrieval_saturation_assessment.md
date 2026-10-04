# Retrieval-saturation assessment — STATE_1 (assembled 2026-10-04, Turn 21; **corrected after frontier reconciliation**)

Machine-derived from `logs/sources_visited.json`. This is an **assessment of remaining yield, NOT an exhaustion declaration** — exhaustion is defined solely by that log, and no dimension has been declared exhausted.

Ledger at reconciliation: **465 leads**, of which **318 are URL-shaped** and **147 are descriptive research notes** (not addresses — open questions awaiting a route).

## Correction first (self-caught error)
A first pass at this file concluded that the unvisited set was 'dominated by low-yield buckets'. **That conclusion was wrong**, because the frontier had never been reconciled against the visited set. Reconciliation found **79 stale lead strings** — URLs already fetched in earlier turns but never removed from the frontier — and, behind them, a **genuinely unvisited first-party block**. The Turn-20 statement that 'no high-value unread source remains identified' is therefore **retracted** (see the correction block in `knowledge/knowledge_base.md`, Turn 21).

After reconciliation: **239 genuinely unvisited URLs** + 147 descriptive notes.

## Genuinely unvisited URLs by domain (top)

- **sakibpro.com** — 86
- **support.ftgames.com** — 33
- **apps.apple.com** — 15
- **apkmirror.com** — 11
- **dlskiturl.com** — 8
- **gamingonphone.com** — 8
- **dreamkitsapp.com** — 7
- **reddit.com** — 7
- **play.google.com** — 6
- **facebook.com** — 5
- **dlsinside.com** — 4
- **thesoccerera.com** — 4
- **bluestacks.com** — 4
- **fifaworldcupnews.com** — 4

## Reading

- **support.ftgames.com (33) — FIRST-PARTY, HIGHEST VALUE, and the reason the 'saturated' call was premature.** Includes **'How do I develop my players' (360003914778)**, which speaks directly to gate dimension 1 (upgrade/coaching) from the developer's own text; plus 'How can I get Gems' (360003914938), 'What are Leaderboards' (360003914998), 'Can I sell my players' (360003945617), 'How do I change my manager' (360003945937), 'Why doesn't my player look like the real person' (360004718318), 'How do I play a Friend Match' (360019064438), 'Removal of Facebook Login from DLS' (9804887423121). Non-DLS titles (Score Hero / Score Match / Ultimate Clash Soccer save-data articles) are out of scope but cheap to note. **This block is the planned work for Turn 22.**
- **sakibpro.com (86)** — mostly per-card pages and tool routes. Value is per-card verification and family membership, not new mechanics; reading them one by one is low-yield except where a specific conflict needs a specific card.
- **apps.apple.com (15) / play.google.com (6)** — regional and duplicate storefront URLs; our version chain is already fixed from first-party 'What's New' text, and third-party trackers are not authoritative for current version.
- **reddit.com (7) / tiktok (2)** — **fetch-blocked** (403 on every attempt this session, both platforms). No route out; the shell has no working TLS either.
- **apkmirror.com (11)** — binary-hosting pages; even a successful fetch would not be an APK download+parse, and the sandbox has no extraction route (no /dev/kvm, no java, shell TLS broken). Retained but not actionable.
- **dlskiturl (8), gamingonphone (8), dreamkitsapp (7), dlsinside (4), thesoccerera (4), dlskits.mobi (2), fifaworldcupnews (4), bluestacks (4, rejected source), facebook/instagram (8)** — secondary/SEO or social surfaces, or already-rejected sources.

## Honest status

**Retrieval is NOT saturated: a first-party block of 33 unread support articles remains, and at least one of them ('How do I develop my players') targets the single thinnest gate dimension with developer-authored text.** The previous 'saturated' framing was an artefact of an unreconciled frontier, not a finding.

What genuinely cannot be retrieved by any route available here is unchanged: the ladder timer and live balances (device-only), in-client confirmation (client-side), and the two fetch-blocked platforms.

**Planned Turn 22 order:** (1) monitoring; (2) `How do I develop my players` (360003914778); (3) `How can I get Gems`, `What are Leaderboards`, `Can I sell my players`; (4) `Why doesn't my player look like the real person` if budget allows. Reconcile the frontier each turn from here on.
