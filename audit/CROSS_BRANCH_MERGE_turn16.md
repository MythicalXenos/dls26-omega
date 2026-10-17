# CROSS-BRANCH SERVICE-LOG MERGE AND ID REPAIR (turn 16)

Date: 2026-10-17T21:0xZ. Trigger: executing the turn-15 resumption item "read the 22655f48 corpus directly for claims whose only witness is a derived summary". The corpus turned out to be 28 files with **no evidence directory at all** — but its `logs/sources_visited.json` (69 records) is a richer artefact than anything previously imported from that branch.

## 1. What was found

1. **No raw capture corpus exists on the sibling branch.** `git ls-tree` shows 28 files: prompt, rules, capability inventory, six `kb/*.md` topic files, logs, queues, profile, revision register. There is no `evidence/` tree and no `research/` tree. Therefore every claim witnessed only by a `kb/*.md` summary **cannot** be upgraded from that branch — the summary is the top of that chain.
2. **But the service log is primary.** Its 69 entries carry per-URL `payload_summary` text written at fetch time, which is one step closer to the source than a topic-file sentence. Ten claims were re-witnessed against it (§3).
3. **An ID collision.** Twelve IDs (`S-20261017-051…063`, except 057) hold different records on the two branches; the sibling continues to 069. Repaired, with mapping recorded in the log itself (OBS-017, `scripts/turn16_merge_sources.py`).
4. **The frontier's last three retryable refs were already captured.** The sibling fetched, in full, at 17:10Z on 2026-10-17:
   - 14369944135058 — hide control-button text (`S-20261017-061`)
   - 360020938198 — change emojis in DLL (`S-20261017-058`)
   - 360021064298 — can an opponent see my custom kit/logo (`S-20261017-059`)
   These were the three refs this workspace had carried as RETRYABLE_FAILURE since the t69 snapshot. **They are now VISITED and recorded as EV-226/227/228. RETRYABLE_FAILURE is zero.**
5. **Three further official articles were never in the frontier at all** and are now admitted as VISITED: 360000842697 (fairness stance), 360003945557 (can't connect), 37082887837202 (find your User ID).

## 2. Frontier after the merge

| Status | Before (turn 14) | After (turn 16) |
| --- | --- | --- |
| VISITED | 96 | **101** |
| IN_PROGRESS | 23 | 23 |
| NON_CONNECTED | 21 | 21 |
| UNVISITED | 8 | 8 |
| RETRYABLE_FAILURE | 3 | **0** |
| ACCESS_BOUNDARY | 2 | 2 |
| REPRESENTATION_DUPLICATE | 8 | 8 |
| **Total refs** | 161 | **163** |

File SHA-256 `9bfcc7de…`, sequence 1319. Verified by `frontier.py summary`.

## 3. Witness upgrades (summary → service record)

| Claim | Was | Now |
| --- | --- | --- |
| CLAIM-113 multiplayer networking | GS-024 (kb summary) | S-20261017-051 (service record, article 360004222118) |
| CLAIM-114 sell/release | GS-026 | S-20261017-053 |
| CLAIM-115 rewarded video | GS-027 | S-20261017-055 |
| CLAIM-116 special taxonomy counts | GS-029 | S-20261017-057 |
| CLAIM-117 DLS27 prep | L-008 | S-20261017-057 |
| CLAIM-101 eight substitutes | GS-022 | S-20261017-050 |
| CLAIM-102 50–60 OVR start | M-006 | S-20261017-008 |
| CLAIM-104 team-OVR formula | T-011 | S-20261017-008 |
| CLAIM-105 "trained = base+1" | T-012 | S-20261017-008 |
| CLAIM-097 OVR expansion | T-002 | S-20261017-008 |

**Honest reading:** this improves *traceability*, not *evidential strength*. A service summary and a topic summary are both second-hand; the difference is that the service summary names the URL and the fetch time. The independence limitation (degradation D-03) is unchanged, and each upgraded claim now says so in its own challenge.

## 4. Four claims added from the merge

- **CLAIM-120** — descriptive button text can be switched off (Game Settings > Display). This is very likely the mechanical answer to the launch-era "clear/pass input is wrong" complaint in CLAIM-091: the captions name buttons, not actions.
- **CLAIM-121** — six emojis active at once, selection path, and a full chat kill-switch.
- **CLAIM-122** — imported kits and logos are **not** visible to opponents in DLL. This contradicts what kit-showcase videos imply, and it is an official negative.
- **CLAIM-123** — the official fairness stance: luck forms part of the experience, "it's the same for all players", and not everything reported will be addressed.

**Why CLAIM-123 matters more than its tier suggests:** it is the only official text that addresses variance directly. It does not prove the implementation is unbiased — it is a policy statement — but it does two things for the mission: (a) it makes "the game scripted me" a claim that must be argued against a stated policy rather than asserted, and (b) it implies the "#1" target must be defined over a sample large enough for luck to average out. That is a design constraint for Step 5, not a research finding.

## 5. What is still true about the epoch

- **Retrieval debt is now zero for known articles.** What remains is 23 mid-capture refs (store chunks, comment chunks, community pages) and 8 refs owed behind the access boundary.
- **Extraction debt persists:** three sibling captures (fairness, can't-connect, user-ID) still lack EV records; only the fairness one was needed to support a claim, and the other two are recorded as captured-but-unclaimed.
- **The frontier has now been wrong about its own counts three times** (t69 staleness, disposition drift, phantom retryables). Each correction came from reading physical records. No count in this project should be trusted because it is written down; only because it was just recomputed.
