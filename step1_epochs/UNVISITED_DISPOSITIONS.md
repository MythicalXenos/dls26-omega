# STEP 1 — DISPOSITION OF THE 15 UNVISITED FRONTIER REFERENCES (t69 snapshot)
Built 2026-10-17T19:10Z (session sess-20261017-001, turn 6). Source of the list: `logs/sources_visited.json` at checkpoint 5ab3ec6 (branch a7e23a6b), `references[status=UNVISITED]` — 15 refs. Method: for each ref, search the preserved evidence corpus (123 EV/EVD records) for the article ID or slug, and classify only on that evidence. No ref is closed for being low-value, expensive or unlikely to matter.

Dispositions per OMEGA-CLOSURE-001: **REPRESENTATION_DUPLICATE** (a VISITED canonical capture of the same article exists, with the proof named), **NON_CONNECTED** (positive scope evidence — a different game), **CANONICALIZED-ADMIN** (directory/contact infrastructure carrying no DLS-specific information), **OWED / ACCESS_BOUNDARY** (still owed; the reopening predicate is the network allowlist or a user-supplied capture).

| Ref | Article | Disposition | Proof / reason |
| --- | --- | --- | --- |
| ref-support-next-update | 360000262229 When will the next app update be? | **REPRESENTATION_DUPLICATE** → ref-support-app-update (EV-131) | Identical article ID; EV-131 records the full text. |
| ref-support-dls19-profile | 360004717278 Can I use my DLS19 profile? | **REPRESENTATION_DUPLICATE** → EV-132 | Identical ID; EV-132 is a full-page capture. |
| ref-support-age-policies | 360000204889 Age Limits and General Policies | **REPRESENTATION_DUPLICATE** → EV-148 | Identical ID; EV-148 is the full text (13+ policy). |
| ref-support-graphics-settings-old | 360000598437 How can I change my graphics settings? | **REPRESENTATION_DUPLICATE** → EV-152 / EV-156 / EV-204 | Identical ID; EV-152 is the original capture and EV-156/204 are revisions of the same article. |
| ref-support-video-clips-new | 7917682153361 I am not seeing any video clips | **REPRESENTATION_DUPLICATE** → EV-160 / EV-165 | Same article slug; EV-160 is the revision capture. |
| ref-support-connection-general | 360000420025 I keep having connection issues | **REPRESENTATION_DUPLICATE** → EV-155 (older revision) | EV-155 captures the older connection article; EV-150 covers the current revision. |
| ref-support-contact | 360000309705 I can't find my answer — how can I contact you | **CANONICALIZED-ADMIN** | Contact-routing page; no DLS-specific information. Per the FTG SUPPORT / ZENDESK SOURCE-FAMILY RULE, administrative endpoints are canonicalized rather than treated as substantive sources. This is not a claim that its content is irrelevant — only that the DLS-bearing projection is empty. |
| ref-support-restart-career-3rd | 3600017167418 How do I restart my career | **NON_CONNECTED (scope evidence recorded in EV-208 lineage)** | The ref appears only in a scope decision record; the live restart article is 7917210208145 (EV-211), which is captured. If a capture later shows this ID serves a distinct DLS page, the disposition reopens. |
| ref-support-name-change | 360000001989 Can I change my in-game name | **OWED — ACCESS_BOUNDARY** | No captured body. Name-change rules are unresolved game knowledge; reopening predicate: allowlisted route or user-supplied capture. |
| ref-support-name-facebook | 360001808378 Can I change my name whilst connected to Facebook | **OWED — ACCESS_BOUNDARY** | No captured body. Likely legacy (Facebook Login was removed — EV-133/214), but "likely obsolete" is not proof; it stays owed, with the obsolescence hypothesis recorded. |
| ref-official-social-tiktok | @dreamleaguesoccer.ftg | **OWED — ACCESS_BOUNDARY** | Official social channel; no capture. Events and patch announcements live here. |
| ref-vi-new-features | download.com.vn "new information" | **OWED — ACCESS_BOUNDARY** | No capture of this page; the VI family is otherwise partially captured (EV-193/196/198). |
| ref-vi-whats-new | download.com.vn "new season" | **OWED — ACCESS_BOUNDARY** | Not captured. |
| ref-vi-update-guide | download.com.vn update guide | **OWED — ACCESS_BOUNDARY** | Not captured. |
| ref-vi-friends-guide | download.com.vn how to play with friends | **OWED — ACCESS_BOUNDARY** | Not captured; Friend Match mechanics are otherwise claimed at CLAIM-099 from an official source, so this is corroboration debt, not primary coverage. |

## Result
- 15 UNVISITED refs: **6 closed as REPRESENTATION_DUPLICATE** (each with a named visited canonical capture), **1 CANONICALIZED-ADMIN**, **1 NON_CONNECTED with recorded scope evidence**, **7 remain OWED under ACCESS_BOUNDARY**.
- The frontier's own status field is not edited here — this file is the disposition record; the authoritative status update will be applied when the frontier is next regenerated from its physical log, so that a derived index never silently overwrites the append-only record.
- Nothing was closed on a utility judgement. The seven owed refs are exactly those with no captured body and no equivalence proof.

## Consequence for the closure test
Condition 1 improves from "15 UNVISITED" to "7 owed, 8 reconciled", but it cannot be met while the web is unreachable: the 9 RETRYABLE refs and the 23 IN_PROGRESS refs remain, and the IN_PROGRESS group includes the Reddit family, the store listing chunks and several community pages.
