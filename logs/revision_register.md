# REVISION REGISTER

Fast-reference index of **changes** to advice or to recorded knowledge (PROMPT.md §8). Not a copy of recommendations — those live in the RECOMMENDATION category of `logs/main_operational_log.md`. Not prompt revisions — those live in `prompt_versions/CHANGELOG.md`. Read at session start; consulted whenever prior advice on a topic must be found fast.

Entry fields (floor): timestamp, what changed, what it was before, why, trigger, affected prior advice, the topic the advice concerned, and anything else that would let a later session find the change fast.

| # | Timestamp | Topic | What changed | Before | Why | Trigger | Affected prior advice |
|---|---|---|---|---|---|---|---|
| R-0001 | 2026-09-27T17:40Z | confidence-tiering policy (game_identity_and_version; gameplay_systems_inventory; live_ops_events_and_cards; terminology_and_abbreviations) | First-party single-source claims downgraded from High Confidence to **Speculative (gate-capped, origin DIRECT)**; tier policy note added to `kb/README.md` | High Confidence, on the reasoning that a first-party document with a checkable origin is strong evidence | Mechanism 5's count gate (2 independent sources) is not met by two surfaces of one origin, nor by an aggregator echo; the conservative signal wins | Self-detected during Mechanism 2 (Skeptic) at promotion — ISS-005 | No advice was ever delivered on these claims, so no prior recommendation is affected. Downstream effect: nothing may be promoted past Speculative on first-party documentation alone until an independent extraction exists (Step 2 APK work is the natural route) |
