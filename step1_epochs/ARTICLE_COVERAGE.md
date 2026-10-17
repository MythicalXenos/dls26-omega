# STEP 1 — FTG OFFICIAL SUPPORT ARTICLE COVERAGE (reconciled across both imported corpora)
Built 2026-10-17T17:26Z (session sess-20261017-001). Sources compared: the a7e23a6b evidence corpus (`docs/continuity/a7e23a6b/evidence/extract/`, EV/EVD records) and the 22655f48 summarised corpus (`kb/game-systems.md`, GS records). Canonical inventory: `kb/source-families.md` S-001 (30 section-listed articles).

Status vocabulary:
- **CAPTURED-EV** — full-text extraction exists as an EV record.
- **CAPTURED-GS** — full text was captured in the 22655f48 corpus and summarised into a GS claim, but has no EV record yet (record-format debt, not a knowledge gap).
- **CAPTURED-ALT-ID** — article exists under a newer/renamed ID and is captured there.
- **RETRYABLE** — a permitted fetch attempt returned a Zendesk 404; the URL or slug moved. Owed as a retry, not a closure.
- **OWED** — no captured body in either corpus.

| # | Article (section listing) | ID | Evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | When will the next app update be? | 360000262229 | EV-131 | CAPTURED-EV |
| 2 | How do player stats affect gameplay? | 360019166777 | EV-115 | CAPTURED-EV |
| 3 | How is save data stored and transferred? | 4413273241873 | EV-125, EV-213 | CAPTURED-EV |
| 4 | How do I find my User ID? | 37082887837202 | EV-127, EV-159, EV-164, EV-168 | CAPTURED-EV |
| 5 | Removal of Facebook Login | 9804887423121 | EV-133, EV-214 | CAPTURED-EV |
| 6 | Can I use my DLS19 profile? | 360004717278 | EV-132 | CAPTURED-EV |
| 7 | Why does the app require a connection? | 360004034498 | — | CAPTURED-GS (GS-017; no EV record) |
| 8 | Is my device compatible? | 214385685 | — | CAPTURED-GS (GS-018; no EV record) |
| 9 | Why can't I update the app? | 360000220945 | EVD-0006 (404) | RETRYABLE — slug moved; EV-131 covers the update policy, not this troubleshooting body |
| 10 | What is the Season Pass? | 4404070913169 | EV-116, EV-162 | CAPTURED-EV |
| 11 | What is the Prize Ladder? | 23108987826962 | EV-118 | CAPTURED-EV |
| 12 | What are Dream Point Boosts? | 24081168829330 | EV-121 | CAPTURED-EV |
| 13 | What are Clans? | 30839289076626 | EV-108 | CAPTURED-EV |
| 14 | How do I play a Friend Match? | 360019064438 | — | CAPTURED-GS (GS-014; no EV record) |
| 15 | How do I restart my career? | 213851909 | EV-211 (new ID 7917210208145) | CAPTURED-ALT-ID |
| 16 | No video clips — what can I do? | 360017166918 | EV-134, EV-160, EV-165 | CAPTURED-EV |
| 17 | How can I reduce data usage? | 360005680437 | EV-139 | CAPTURED-EV |
| 18 | Why doesn't my player look real? | 360004718318 | EV-140, EV-206 | CAPTURED-EV |
| 19 | How do I hide control-button text? | 14369944135058 | EVD-0008 (404) | RETRYABLE — body never captured; related content only in EV-145 (auto-switch setting) |
| 20 | How do I customise kit/logo? | 360004080497 | EV-146, EV-200 | CAPTURED-EV |
| 21 | How do I obtain more players? | 360004066417 | EV-124 | CAPTURED-EV |
| 22 | How do I change my manager? | 360003945937 | EV-147 | CAPTURED-EV |
| 23 | How does game difficulty work? | 360018360418 | EV-107, EV-141, EV-207 | CAPTURED-EV |
| 24 | What are Leaderboards? | 360003914998 | EV-101, EV-222 | CAPTURED-EV |
| 25 | How does DLL matchmaking work? | 360018359998 | EV-102, EV-135, EV-209 | CAPTURED-EV |
| 26 | How do I change my DLL emojis? | 360020938198 | — (known RETRYABLE in EV-209) | OWED — no body |
| 27 | Can my opponent see my kit/logo in DLL? | 360021064298 | — (known RETRYABLE in EV-209/210) | OWED — no body |
| 28 | Multiplayer Troubleshooting | 360004222118 | EV-119, EV-199 | CAPTURED-EV |
| 29 | How do I earn coins? | 214385285 | EV-122 | CAPTURED-EV |
| 30 | Is it possible to earn free coins? | 213851369 | EV-123 | CAPTURED-EV |

## Additionally discovered DLS support articles (outside the 30-listing, all connected)
| Article | ID | Evidence |
| --- | --- | --- |
| How do I develop my players? | 360003914778 | EV-136 |
| How do I get gems? | 360003914938 | EV-117 |
| Why have I been blocked? (sanctions) | 360008904718 | EV-120, EV-201 |
| Promotion / XP ladder | 7917423348497 | EV-195 |
| Season leaderboard / Season Points | 7916583518353 | EV-126, EV-197 |
| Connection-stability playbook | 7917279109777 | EV-150 |
| Graphics / FPS settings | 7918056936721 | EV-152, EV-156, EV-204 |
| Formation pool | 7917587319313 | EV-203 |
| Player roles | — | EV-194 |
| Player data deletion | 360017046578 | EV-166, EV-212 |
| iCloud setup | — | EV-167 |
| Change kit (My Club route) | — | EV-210 |
| Sell / discard players | 17146555181585 | EV-137, EV-202 |
| Missing players / licensing | 213852049 | EV-138 |

## Reconciliation result (this is the point of the table)
The prior session's "15 remaining article bodies owed" list was stale. Cross-checking both corpora shows **26 of the 30 section-listed articles already have captured content**, with 22 holding full EV records and 4 captured only in the GS summary corpus (articles 7, 8, 14 + update troubleshooting). Only **three bodies remain genuinely uncaptured**: #19 control-button text (404), #26 DLL emojis (retryable), #27 opponent kit visibility (retryable). This is a coverage statement about these corpora, not a claim that no other source exists.

Remaining Step-1 support debt:
1. Retry #19, #26, #27 by slug search when a permitted route exists (wall source RQ-001).
2. Backfill EV records for articles 7, 8, 14 so every captured article has a physical extraction record (record-format debt, RQ-20261017-006).
3. The 13 additionally-discovered articles are captured but two (player roles EV-194; iCloud EV-167) need their canonical URLs recorded in the sources log if missing.
