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

## Addendum 2026-09-28T00:25Z (session 1 turn 9) — pass themes and cycle banners from captures (S-0036)

- Dec-2024 season pass theme: **CHRISTMAS**, 1d 5h left on 27 Dec 2024; its ACTIVATE PASS! row shows a **Hermoso** card as a pass reward. Jan-2026 pass theme: **'january'**, 9h 2m 53s left on the capture — pass themes appear monthly/calendar-bound while ladder cycles run ~90 days, i.e. two independent live-ops clocks (G-0052).
- Ladder cycle banners: WORLD CUP CLASSICS (Dec-2024, 69d 22h left), MIDFIELD CLASSICS (Jan-2026, 41d 21h left). Combined with the current English League Classics banner, three named cycles span Dec-2024 to Sep-2026, consistent with ~90-day recycling (seven-plus cycles).

## Addendum (turn 48): KICK-OFF STARS = real DLS26 mechanic (S-0206)
- **What:** special-edition **GREEN cards** — the DLS26 wave = **Raphinha + Alvarez** (the two DLS26 cover stars).
- **Delivery: VIA THE SEASON PASS** — you can only choose **ONE per pass**; both require buying a second pass (community: "clever but greedy"). Reddit Dec-13-2025: "Kick off stars Raphinha and Alvarez are here in season pass"; "the next season pass which arrives in 9 days" (10-day pass cycle echo).
- **Upgrade path:** improved with **special trainers** (choose the stats) + gems (community description). Rating band community-guessed **80-86**. Green card colour "confirmed by server leaks" (dlsmod — mod site, rumor-grade).
- **Mechanic echoes:** special players excluded from accommodation/squad count (Nov-2025 thread — matches the "specials don't eat accommodation" line).
- **G-0063 link:** the DROICER leak's "DLS 27 Kick-Off Stars" phrase refers to THIS program — a Gallagher/Robinson (or Ronaldo/Raphinha) DLS27 wave is structurally plausible as the follow-up to the DLS26 cover-star wave.

## Addendum (turn 56): LIVE-OPS STATE + Dynamic Stars schedule + English League Classics ladder (S-0235)
- **CURRENT LIVE EVENTS (App Store listing):** (1) **Cult Heroes** — "sign these top stars... Now available with **boosted attributes**" (new phase vs the original Sept-16 launch?). (2) **English League Classics** — "unlock top players and claim big rewards in our this **new Prize Ladder**" — THE leak context: Roy Keane / Irvin = English-league classic players on this ladder.
- **Dynamic Stars (June-July 2026) schedule (sportsdunia):** base **82 OVR** cards upgraded by national-team performance — group win +1 (from Jun 29), R32 +2 (Jul 6), R16 +2 (Jul 9), QF +2 (Jul 13), SF +2 (Jul 16), **FINAL WINNER = 96 OVR (Jul 20)**. Season 1 pass: 3 premium + 2 free Dynamic Agents. (The "Nico Williams 96" in the user queue = a maxed Dynamic Star.)
- **Update history (fifaworldcupnews):** Feb-2026 = live events + Season Pass objectives; May-2026 = "Summer Showdown" global cups; Jul-2026 = "World Heroes" (started Jul 1) + "World Winners" upcoming; Sept-2026 = small.
- **DECEPTION EXEMPLAR:** playdreamleaguesoccer.com "2026 schedule" = AI-fabricated (fake tournaments, fake prize pools, "mined from the backend" claim, 2024 date) — REJECTED, recorded here as a caution.

## Addendum (turn 59): Cult Heroes roster named + Season Pass card + taxonomy (S-0242/0243)
- Cult Heroes = a distinct card family in the 12-type taxonomy; roster = 12 named records (see player_pool addendum) — the "boosted attributes" phase lifts base OVRs (de Gea base 79 -> CH 85; Aubameyang CH 85 CF).
- Season Pass family = named cards too (João Pedro 28356 CF 82 = current).
- World Winners = the Jul-2026 event family (App Store history) now confirmed as a distinct card type; Dreamstar 25/26 = two waves of the Dreamstar family.

## Addendum (turn 60): update cadence + squad-rule change + community toolkit (S-0245)
- **Update cadence (fifaworldcupnews + App Store):** May-2026 = end-of-season rating tweaks; Jul-2026 = Cult Heroes tweaks (Pickford/ter Stegen/Fermín/Pedro Gonçalves/Vivian/João Pedro) + World Heroes launch; Aug-2026 = 2026/27 pre-season transfer sync; Sep-2026 = Cult Heroes wave + English League Classics ladder (V13420/159, Sept-1).
- **SQUAD RULE CHANGE (App Store, first-party):** "Increased squad size — now with **unlimited special players** in your club" — the specials-capped squad rule was LIFTED (G-0076 user question now includes WHEN this changed).
- **"Improved Venues — upgraded club facilities"** (App Store) = the facilities-refresh hint (G-0074: DLS26 costs may differ from the 2023 numbers).
- **Clans** = "join and work towards prizes" (new social/prize layer).
- **Community toolkit (reddit Dec-2024):** trungta-hust database (dead/JS now) + **CokeStudios Python transfer-market-screenshot stat recognizer (gist)** + community secret-ID testimony ("now I can see what secret players are; got tricked for 79 rare guys for legendary ones") — the market-screen user ask has a ready-made community OCR tool.
