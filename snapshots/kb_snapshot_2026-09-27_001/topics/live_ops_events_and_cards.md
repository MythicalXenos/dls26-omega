# TOPIC: Live operations — events, seasons, and special-card collections

**Sweep:** STATE_1_RESEARCH_SWEEP. **Opened:** 2026-09-27. **Exhaustion declaration:** NONE — open, and this is the topic the user's stated current activity sits inside ("grinding the prize ladder for a special player", user-stated), so it carries queue-priority weight in practice even though the queue itself is inactive during the sweep.

Taxonomy-gate dimension 3 (Live Operations & Progression tracks) is answered here: how season milestone reward ladders, season passes, and tournament event points accumulate and reset.

**Source quality warning for this whole file:** almost everything below currently comes from ONE non-official domain (sakibpro.com) with an OBSERVED incentive (ad revenue + its own downloadable kit products + authority framing "100% Official ... this is not a rumor"). Per PROMPT.md §5 every such claim is capped at **Speculative** until corroborated by an unrelated source type. The only first-party item is FTG's changelog line (S-0012).

---

## First-party (official) evidence

- CLAIM: The latest client update is described by FTG as "our late summer update", announcing **New Special Players – "Cult Heroes" collection, coming soon** plus "Bug Fixes – Dozens of issues sorted".
  - source: S-0012 (page-render, official Play Store "What's new")
  - first_published: listing updated 2026-09-14; retrieved 2026-09-27
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single source) that FTG published this text (checkable origin = the listing itself); **Speculative** as to what the collection contains, when it lands, or what it costs
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: any client update replaces the changelog | event-triggered: the collection's release, and the store event ending 10/14
  - origin: DIRECT (FTG's own store text) for the announcement; NONE FOUND for the mechanics
  - independence: single first-party source; appbrain's identical changelog text (S-0001) is an ECHO of this listing, not a second source
  - deception_screen: clean
  - datamining: pending-confirmation (flagged 2026-09-27; blocked — no client assets obtained, gaps G-0004)
  - evidence_class: verified tool output
  - game_version: the version published 2026-09-14 (number unresolved — DLS26-C1)
  - notes: "coming soon" means the collection was NOT live in the client as of the changelog. A Play Store event block on the same page ends **10/14** with copy "The names the fans remember, from their peak years" — thematically consistent with "Cult Heroes", but the identity link is NOT established.

## Non-official event timeline (all Speculative, one incentivised source, corroboration owed)

| Date (as published) | Event / collection | Source claims | Confidence | Corroboration owed from |
|---|---|---|---|---|
| 2026-02-19 | Custom kits/logos guide era | site content, not a game event | n/a | n/a |
| 2026-03-26 | **Dream Star Event 2026** — "Full Guide, Players, Dates & Rewards" | S-0013/S-0014 | Speculative | FTG channels, store listings, second unrelated community source |
| 2026-05-26/27 | **Summer Update** — "Dynamic Stars, Classic Icons, and Economy Reset"; site's thumbnail is a Play Store screenshot dated 2026-05-26 | S-0013 | Speculative (but the screenshot-as-evidence pattern is a checkable route — retrieve it) | Play Store update history / Wayback of the listing around 2026-05-26 |
| 2026-07-01 | **World Cup Heroes** — "launches ... on July 1, 2026, bringing exclusive **Legendary Agent** cards" | S-0013 | Speculative | FTG channels, in-game, second source |
| 2026-07-13 | **World Winners** — "officially confirmed as the next major **Legendary Agent** event ... direct follow-up to [World Cup Heroes]" | S-0013 | Speculative | same |
| 2026-08-12 | **DLS 27** release-date speculation page ("updated the moment FTG makes an official announcement") | S-0013 | Speculative — speculation about a future title, not a DLS26 fact | FTG announcement (none found yet) |
| 2026-08-21 | "DLS 26 New Update: All New Events, Special Cards & Upcoming Player Details" | S-0013 | Speculative | fetch the article itself (not yet visited) |
| 2026-09-14 → 10/14 | "Cult Heroes" collection + a store event ending 10/14 | S-0012 (official) + S-0013 (site) | announcement Speculative (gate-capped: single source, DIRECT origin) / mechanics Speculative | the event page, FTG channels, in-game |

**Terminology leads to resolve (prompt shorthand → game terms):** "Legendary Agent" appears to be an event/card family name; "Dynamic Stars" and "Classic Icons" appear to be card categories introduced by the Summer Update; "Economy Reset" implies a periodic economy action with consequences for spending — potentially an IRREVERSIBLE/CONSEQUENTIAL action type for `kb/irreversible_action_list.md` once verified; "Max Ratings" implies per-card maximums (the prompt's "ceiling" sense). None of these are established; all are recorded so the sweep resolves them rather than assuming.

## Prize ladder (the user's stated current activity)

- CLAIM: none yet. The prompt's term "prize ladder" has NOT been resolved to any in-game system, and the user has not said which ladder or which special player they are grinding.
  - status: OPEN GAP — `kb/gaps.md`
  - what would answer it: the store event page (eventdetails/4830045897422713648), the Cult Heroes article, SakibPro's event guides, FTG channels, and ultimately the user's own screen (a first-contact question, batched per carry-the-load)
  - why it matters: the user is spending effort there NOW, so the first actionable advice of this system probably concerns it. Under NO OUTPUT DURING BOOTSTRAP no advice is given yet; under the interim-contact rule nothing is due until session 3.

## Season structure and reset behaviour

Unanswered: whether seasons are calendar-bound or rolling; how season points accumulate; what resets and when; whether "Economy Reset" is a real recurring mechanic or a site's phrasing for a one-off patch change. All owed. **Never record "no records found" as "does not exist"** — these stay OPEN gaps.

## Research order for this topic (organized by source, per PROMPT.md §2)

1. Official: Play Store event page + data-safety page; `ftgames.com` and `firsttouchgames.com` (both domains — the listing names a different one from the marketing site); FTG support pages; FTG Facebook/Instagram/TikTok/X/YouTube.
2. Database/tool: SakibPro's three tools and each event article; every other DLS26 database/tool discovered (the list is discovered, not prescribed).
3. English community: Reddit, YouTube (with subtitle/transcript text), X, TikTok, Facebook groups, forums, wikis, guide sites, and the full Play Store review set (only 3 of many were retrieved).
4. Non-English community: tr, ar, pt, es, fr, id, and any other language found.
5. Technical: client data for event configs (Step 2), Wayback history of the listing and of FTG pages, any public API.
6. User-generated: comments on all of the above, processed for unique information.
