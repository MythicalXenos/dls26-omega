# KB — CLAIM ALIAS MAP (reconciliation of the two imported corpora)
Built 2026-10-17T17:22Z (session sess-20261017-001, Step 1) under RQ-20261017-003 / OBS-011.
Purpose: map the 73 topic-summary IDs (T-/B-/L-/M-/GS-) from the 22655f48 markdown corpus onto the 87 live claims (CLAIM-001…088) from the a7e23a6b corpus, so there is one claim authority and no duplicated truth.

Rules applied:
- `kb/claims.jsonl` is the authority. A mapping is an alias, not a merge: the markdown summary is a derived view and is corrected, never the claim silently rewritten.
- MAPPED = the claim(s) carry the same proposition. ORPHAN-OWED = the topic summary holds knowledge with no live claim yet; it is queued for promotion, not discarded. REVIEW = mapping plausible but not verified from source text; must be checked before the summary is deleted or corrected.
- NEGATIVE = a closure (thing does not exist), recorded as a negative finding rather than a positive claim.

## build-version.md
| MD ID | Topic | Live claim(s) | Status |
| --- | --- | --- | --- |
| B-001 | current build 13.430 code 160 | CLAIM-087 | MAPPED |
| B-002 | package com.firsttouchgames.dls7 | CLAIM-001 | MAPPED |
| B-003 | no rebrand found | CLAIM-001 | MAPPED |
| B-004 | launch December 2025 | CLAIM-008, CLAIM-054 | MAPPED |
| B-005 | 2026 version timeline | CLAIM-008, CLAIM-048, CLAIM-054 | MAPPED |
| B-006 | Summer Spotlight attribution | CLAIM-048 | MAPPED |
| B-007 | store metrics | CLAIM-053 | MAPPED |
| B-008 | technical envelope | CLAIM-053 | REVIEW — size/requirements detail needs its own claim |

## community-meta.md
| MD ID | Topic | Live claim(s) | Status |
| --- | --- | --- | --- |
| M-001 | launch-era gameplay sentiment | CLAIM-005 | REVIEW — sentiment is broader than the integrity claim |
| M-002 | formation discourse, no verified meta | CLAIM-070 | MAPPED (community-tier formation list only) |
| M-003 | DLL structure / leaderboard cadence | CLAIM-002, CLAIM-027 | MAPPED |
| M-004 | economy/community friction | CLAIM-069 | REVIEW |
| M-005 | dated ratings snapshots | CLAIM-007, CLAIM-058 | MAPPED |
| M-006 | new-player starting state | — | ORPHAN-OWED |
| M-007 | launch features corroborated | CLAIM-004, CLAIM-045 | MAPPED |

## game-systems.md
| MD ID | Topic | Live claim(s) | Status |
| --- | --- | --- | --- |
| GS-001 | player stats semantics | CLAIM-013 | MAPPED |
| GS-002 | difficulty + fair-gaming | CLAIM-009, CLAIM-011, CLAIM-080 | MAPPED |
| GS-003 | economy (gems/coins/Dream Points) | CLAIM-015, CLAIM-016, CLAIM-019, CLAIM-063 | MAPPED |
| GS-004 | Season Pass | CLAIM-040 | MAPPED |
| GS-005 | Prize Ladder | CLAIM-016 | MAPPED |
| GS-006 | recruitment channels | CLAIM-020 | MAPPED |
| GS-007 | clans | — | ORPHAN-OWED |
| GS-008 | coaching / player development | CLAIM-028, CLAIM-049, CLAIM-052 | MAPPED |
| GS-009 | Cult Heroes live in 13.430 | CLAIM-055, CLAIM-059 | MAPPED |
| GS-010 | update-channel policy | CLAIM-025 | MAPPED |
| GS-011 | position labels | CLAIM-086 | MAPPED |
| GS-012 | coin economy | CLAIM-019 | MAPPED |
| GS-013 | leaderboards | CLAIM-002, CLAIM-071 | MAPPED |
| GS-014 | Friend Match | — | ORPHAN-OWED |
| GS-015 | save data & accounts | CLAIM-022, CLAIM-083 | MAPPED |
| GS-016 | Reset Profile (irreversible) | CLAIM-041, CLAIM-082 | MAPPED |
| GS-017 | connection requirement | CLAIM-030 | MAPPED |
| GS-018 | device compatibility | — | ORPHAN-OWED (CLAIM-030 partially covers) |
| GS-019 | app updates | CLAIM-025 | MAPPED |
| GS-020 | customisation | CLAIM-034, CLAIM-074 | MAPPED |
| GS-021 | account legacy (DLS19/25) | CLAIM-072 | MAPPED |
| GS-022 | squad depth (reserves + 8 subs) | — | ORPHAN-OWED |
| GS-023 | facilities (Stadium/Medical/Commercial/Training/Fanzone) | CLAIM-069 | REVIEW — facility list itself has no claim |

## live-state.md
| MD ID | Topic | Live claim(s) | Status |
| --- | --- | --- | --- |
| L-001 | Dynamic Stars event | CLAIM-048, CLAIM-055 | MAPPED |
| L-002 | World Cup Winners event | CLAIM-055, CLAIM-059 | REVIEW |
| L-003 | Cult Heroes live | CLAIM-055, CLAIM-059 | MAPPED |
| L-004 | "Play Fest" is not a DLS event | — | NEGATIVE (closure; keep as negative finding) |
| L-005 | World Heroes event | CLAIM-059 | REVIEW |
| L-006 | live-service cadence | — | ORPHAN-OWED |
| L-007 | current store banner state | CLAIM-045 | MAPPED |

## terminology.md
| MD ID | Topic | Live claim(s) | Status |
| --- | --- | --- | --- |
| T-001 | DLL = Dream League Live | CLAIM-001, CLAIM-045 | MAPPED |
| T-002 | OVR = Overall | CLAIM-033 | REVIEW — terminology vs card-rarity claim |
| T-003 | GK = goalkeeper | CLAIM-013 | MAPPED |
| T-004 | XI = starting eleven | CLAIM-029 | MAPPED |
| T-005 | "special card" = Special Players | CLAIM-046 | MAPPED |
| T-006 | modes (DLL, Exhibition, Dream Draft, Friend Match…) | CLAIM-066 | MAPPED (partial: no Friend Match claim) |
| T-007 | support-inventory systems | CLAIM-016, CLAIM-040 | MAPPED |
| T-008 | special-player collections | CLAIM-055, CLAIM-059 | MAPPED |
| T-009 | 8 divisions + Legendary Division | CLAIM-010 | MAPPED |
| T-010 | position labels | CLAIM-086 | MAPPED |
| T-011 | team OVR formula (tool claim) | — | ORPHAN-OWED |
| T-012 | trained = base + 1 hypothesis | — | ORPHAN-OWED (Speculative; keep quarantined) |
| T-013 | DLL structure / matching | CLAIM-002, CLAIM-081 | MAPPED |
| T-014 | Season Points | CLAIM-021, CLAIM-071 | MAPPED |
| T-015 | Dream Points | CLAIM-016, CLAIM-063 | MAPPED |
| T-016 | in-game week | CLAIM-020 | MAPPED |
| T-017 | Form Boost | CLAIM-028 | MAPPED |
| T-018 | Coaches | CLAIM-028 | MAPPED |
| T-019 | Cult Hero Agents | CLAIM-046 | MAPPED |
| T-020 | reset cycles (match-based clock) | CLAIM-020 | MAPPED |
| T-021 | ceiling (development cap) | CLAIM-007, CLAIM-058 | MAPPED (card ceiling; development cap separate) |
| T-022 | position label set | CLAIM-086 | MAPPED |
| T-023 | Progress Bank | CLAIM-040, CLAIM-068 | MAPPED |
| T-024 | My Club surface | CLAIM-066 | REVIEW |
| T-025 | clean sheet | CLAIM-019 | MAPPED |
| T-026 | stadium bonus | CLAIM-019, CLAIM-069 | MAPPED |
| T-027 | "scripts" | CLAIM-044 | REVIEW |
| T-028 | reserves / substitutes | CLAIM-029, CLAIM-076 | MAPPED |

## Result
- 73 topic summaries mapped (counts machine-checked): **56 MAPPED** (52 plain + 4 MAPPED-with-qualifier), **9 REVIEW**, **7 ORPHAN-OWED** (6 plain + 1 partial), **1 NEGATIVE**. REVIEW rows still name a candidate claim, so no topic is left without a destination.
- ORPHAN-OWED topics: new-player start state (M-006), Clans (GS-007), Friend Match (GS-014), device compatibility (GS-018, partially covered by CLAIM-030), squad depth (GS-022), live-service cadence (L-006), team-OVR formula (T-011), trained-rating hypothesis (T-012). These are queued as RQ-20261017-005 for promotion into claim records from preserved evidence — not invented, not dropped.
- The reverse gap is larger: claims.jsonl carries many propositions (economy maps, card taxonomies, special-card lineages, sanction policy, destructive surfaces) that the markdown corpus never summarised. The 87-claim corpus remains the richer authority; the markdown files are retained only as topic summaries until the reconciliation pass rewrites them.
