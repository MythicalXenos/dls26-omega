# IRREVERSIBLE ACTIONS — DLS26 OMEGA
Standing list of verified irreversible actions, maintained per the Knowledge Management rules. An action enters this list only when its irreversibility is itself verified from evidence — never assumed (ZERO UNGROUNDED CLAIMS INVARIANT). First entry written turn 4 (2026-10-17); the list was empty at bootstrap pending Step-1 verification.

Entry format: ID | action | what it destroys | cooldown/limits | evidence origin | source | verified date | system duties (warn-before, never-initiate, handoff note).

## IRREV-001 — Reset Profile (in-game)
- **Action**: Settings (gear icon, top left) → Advanced → "Reset Profile" (skull-and-crossbones button).
- **Destroys**: ALL game progress — coins, gems, consumables, and in-app purchases. FTG: "it will not be possible to recover any previous game profiles… this process cannot be undone."
- **Limits**: one reset per 30 days.
- **Evidence origin**: official-stated (FTG support article 213851909, "How do I restart my career from the beginning?", full text fetched 2026-10-17).
- **Confidence**: Confirmed. **Volatility**: Low (mechanic).
- **System duties**: (1) warn the user before any action that could trigger it; (2) never initiate or recommend it — if the user asks, state the consequences verbatim from the article before proceeding; (3) record any user-executed reset in the main operational log and update user_profile.md (club/game state becomes "new career"); (4) distinguish it from legitimate save transfer (GS-015), which is the non-destructive alternative.

## Related destructive-risk surfaces (not irreversible actions by the system, but loss-bearing)
- Signing out of Sign in with Google / Apple unlinks the profile; loss-susceptible on uninstall or device change (GS-015, official-stated).
- Facebook-Login-stored profiles are unrecoverable (GS-021, official-stated).
- Modded APKs / hacks / bug exploitation: ban surface — FTG ("Why have I been blocked from playing DLS?", 360008904718): only App Store / Google Play versions are authorised; bans are not lifted on request unless incorrectly flagged. Recommending mods is therefore prohibited (ToS + irreversible account risk).
