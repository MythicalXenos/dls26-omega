# SOURCE-RELIABILITY REGISTER — DLS26 OMEGA

> **Purpose (RQ-20261018-022).** Every source used in the turn-35 sweep is classified here with the specific reason. A source's status is a property of the *source*, not of the individual article — a rejected source is rejected for all future use unless the underlying defect is fixed.
> **Authority note:** this register records *why* a source is trusted or distrusted. The claim authority remains `kb/claims.jsonl`. Where a claim cites a source listed here as REJECTED or DOWNGRADED, the claim's confidence tier must reflect that.
> Basis: ckpt-156 — 1,902 claims / 395 evidence records.

---

## TIER 1 — Approved for authority

These may be cited as evidence for Confirmed/High Confidence claims.

| Source | Why trusted | Used for |
|---|---|---|
| **First Touch Games official channels** — App Store version history, Google Play listing, official TikTok (@dreamleaguesoccer.ftg), FTG support portal | Primary source. No incentive to misstate mechanics. | Version timeline, feature existence, Fanzone, Dynamic Stars, World Tournament, World Heroes, Cult Heroes, Dream Stars, 12th Man, Friend Match, save/accounts, no-mods position |
| **Independent APK archives + datamine** — APKMirror, dlsinside (build/version-code tables, player databases) | Direct artefact inspection; verifiable build/date pairs; not derived from each other | Build 13.430 / code 160, Cult Heroes 12-player roster, version-code sequence, technical envelope |
| **Store metrics databases** — AppBrain, AppMagic | Database-derived, internally consistent | Download counts, ratings, rank |

**Rule for Tier 1:** when a Tier 1 source and any lower tier disagree on a *fact the Tier 1 source actually states*, the Tier 1 source wins (Evidence Hierarchy). When the Tier 1 source is silent, a lower tier may fill the gap at the tier its corroboration supports.

---

## TIER 2 — Corroboration required

Useful, but never load-bearing alone. A claim resting only on one of these is capped at Community Consensus until independently corroborated.

| Source | Caveat | Used for |
|---|---|---|
| **r/DreamLeagueSoccer** | Player reports, not measurements. Excellent for *mechanics that many players independently describe* (market refresh, corner technique, tier ladder); poor for *numbers*. Multi-commenter agreement within one thread is not independence. | Set pieces, transfer market, DLL tier ladder, clan economy, matchcraft, penalty/free-kick technique, the club-name acquisition lever, the formation decision rules and the DLS26 gameplay feel |
| **Bluestacks** | Generally accurate mode summaries; republishes across regional sites, so its "independence" is illusory. Frequently carries DLS24/DLS25 text under a DLS26 heading. | Mode descriptions, Scenarios, Exhibition, challenge structure, login cycle |
| **gamingonphone** | Same editorial family as Bluestacks; carries a **known outlier** — a 1,200c/40g starter pack that contradicts every other source (1,500c/75g). Treat its economy figures as suspect. | Mode descriptions, challenge cadence |
| **dlspedia.fandom.com** | Community wiki. Published the only complete **stadium sector-seat and division-gate ladders** in the corpus. Caveat: pages carry old "Great Page" dates (2018), so its tables may reflect an earlier build — its Division 3 figure (15,000) conflicts with an older wiki's 35,000, and the top-division gate has moved between 80,000 and 85,000 across builds. **Cite for structure and shape; verify the final gate in-client.** | Stadium seat ladders, division gates, sector names, pitch types |
| **sakibpro.com · dreamkitsapp.com** | Community player databases. Independently reproduced the **complete 12-player Cult Heroes roster and its ratings**, matching dlsinside — which is what makes the C-018 resolution two-source rather than one. | Cult Heroes roster and ratings, player positions/ages/heights |
| **rajatips.com** | Single-author tips site. Published the **only complete scout and agent probability ladders** in the corpus, and its Common-scout figures (93/5/2) match an independent source exactly. Caveat: its Legendary-scout split (40/45/15) conflicts with a second source (55/30/15) — **cite the structure, not the middle column.** | Scout/agent probability ladders, coach-farming threshold |
| **LevelWinner (levelwinner.com)** | Long-running multi-year DLS guide series. Its **per-build** facility effects are the corpus's best record of how a mechanic changed — e.g. the Commercial nerf from ~50% at max (DLS20/21) to 10% now. Caveat: always read the build year before citing a number. | Facility per-level effects and their version history, coach effect sizes, formation-change timing |
| **ldplayer.net** | Emulator vendor blog. Reproduced the scout drop rates and the physio ladder; its Rare/Legendary scout splits differ from rajatips. | Scout drop rates, scout discounts, physio ladder |
| **mokoweb.com** | **Mod site.** Its "709MB" bundle figure and mod claims are screened out; its *descriptive* text about base-game mechanics is sometimes the only source and is used at Community Consensus with the mod material stripped. | Free-kick distance bands, general tips |

**Corroboration rule:** two Tier-2 sources that agree only because both derive from the same upstream text (e.g. Bluestacks and its regional mirrors) count as **one** source, not two.

---

## TIER 3 — DOWNGRADED (use only with an explicit caveat)

| Source | Defect | Consequence |
|---|---|---|
| **fifaworldcupnews.com** | Claimed "Version 13.420… launched May 28" — internally inconsistent, since 13.420 is the September build. Content-farm conflation of version numbers and dates. | Downgraded for all version/date claims. Still cited for *event existence* only, and only where corroborated (its World Heroes 1 July 2026 date was independently confirmed by official TikTok). |
| **thesoccerera.com** | Self-contradicts within one article — states launch availability as both "December 4, 2026" and "December 2025". | Downgraded for version/date claims. |
| **ggbro.io** | Claimed Summer Spotlight was v13.310 on May 28; contradicted by the official version history. | Downgraded for version attribution. |
| **APKPure, AppBrain, AppGlint, AppMagic, Soft112** | **Not independent of each other** — all derive from Play Store data. They agree because they share an upstream, not because they corroborate. | Count as ONE source. Never cite their agreement as corroboration. Their release **dates** are specifically unreliable (see C-023). |

---

## TIER 4 — REJECTED (never cite as authority)

| Source | Specific fabrication evidence |
|---|---|
| **playdreamleaguesoccer.com** | **Confirmed AI content farm — now SIX times.** Beyond the earlier fabrications it has since published: a "Tactical Presets" system with shareable custom tactics, a "3-5-2 Fluid" formation, a playstyle-learning AI manager (**refuted by FTG's own "no additional overlaid controls" article**), "Version 9.4.0" for a game at v13.420, training that raises OVR "from 60 to 99" against the confirmed 86 ceiling, invented skill moves (elastico, trivela), "4K stadiums" and "FTG Engine 6.0", and fabricated statistics with no method behind them ("12.5% average pull rate", "47 average days of grinding", "3.2M average coin cost"). | Published: a "Chemistry" system and "Fluid Formations" — neither exists; fake user testimonials ("DLS_King_07 Mumbai", "GoalMachine_23 Bangalore", "Rohit_Striker" interview); an "Icon Exchange" feature; Vinícius Jr at 91 OVR; a "Youth Academy Cup"; a "Global Super League". All fabricated. Any article from this domain is rejected in full. |
| **sportsdunia** | Two rejected tables: a Commercial facility bonus table and a formation table. Both contradicted official/other sources. Formation recommendations (4-3-3, 3-4-1-2) are retained in the conflict log **as a minority position only**, never as guidance. |
| **eslamgaming** | Fabrications plus a **wrong control map** — a control mapping that does not match the game. Its **floodlight/sunset visibility claims are recorded at Speculative (C4)** and flagged for device verification, not adopted. |
| **Baiduwiki** | Described a non-existent **auction-house** transfer market. DLS has no auction house. |
| **chaptercheats** | Wrong definition of CON (Construction). CON = **Construction** in DLS; chaptercheats defined it otherwise. |
| **footballeffect / gamingonphone starter-pack figures** | 1,200 coins / 40 gems starter, contradicting the 1,500c / 75g figure from every other source including the DLS24 baseline. Treated as an outlier, not evidence. |

**Rejection rule:** rejection applies to the *domain*, not the article. If a rejected source is the only source for a proposition, the proposition is recorded as **Speculative with an explicit single-source-rejected flag**, or dropped.

---

## Standing rules

1. **Mirror dates are never authoritative** (C-023). Cite the App Store version history or the datamine build/date pair. Mirrors disagree on dates while agreeing on content; the version-to-content mapping is reliable, the version-to-date mapping is not.
2. **Corroboration must be independent.** Shared upstream does not count.
3. **Official-stated beats everything**, but only for what it actually states. Official silence is not official denial, and official marketing copy ("upgrading live with national team performances") confirms *existence* of a mechanic, not its numbers.
4. **Single-source community numbers** (e.g. ~300 matches to a dream squad, ~16 days to Tier 1) are recorded as planning figures, never as guarantees.
5. **A source's reliability is reassessed, not assumed.** When a source is caught fabricating once, all of its output is re-examined, not just the caught article.

---

*Register maintained at `logs/source_reliability.md`. Closes RQ-20261018-022.*
