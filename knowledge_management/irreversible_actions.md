# IRREVERSIBLE ACTIONS — DLS26 OMEGA
Standing list of verified irreversible actions, maintained per the Knowledge Management rules. An action enters this list only when its irreversibility is itself verified from evidence — never assumed (ZERO UNGROUNDED CLAIMS INVARIANT). First entry written turn 4 (2026-10-17); second entry turn 5.

Entry format: ID | action | what it destroys | cooldown/limits | evidence origin | source | verified date | system duties (warn-before, never-initiate, handoff note).

## IRREV-001 — Reset Profile (in-game career restart)
- **Action**: Settings (gear icon, top left) → Advanced → "Reset Profile" (skull-and-crossbones button).
- **Destroys**: ALL game progress — coins, gems, consumables, and in-app purchases. FTG: "it will not be possible to recover any previous game profiles… this process cannot be undone."
- **Limits**: one reset per 30 days.
- **Evidence origin**: official-stated (FTG support article 213851909, "How do I restart my career from the beginning?", full text fetched 2026-10-17).
- **Confidence**: Confirmed. **Volatility**: Low (mechanic).
- **System duties**: (1) warn the user before any action that could trigger it; (2) never initiate or recommend it — if the user asks, state the consequences verbatim from the article before proceeding; (3) record any user-executed reset in the main operational log and update user_profile.md (club/game state becomes "new career"); (4) distinguish it from legitimate save transfer (GS-015), which is the non-destructive alternative.

## IRREV-002 — Delete Profile (personal-data deletion)
- **Action**: Main Menu → Settings (gear icon) → Advanced → Delete (trash can) → Delete Profile.
- **Destroys**: any and all existing profiles saved on the device — wiped entirely; "this process cannot be reversed once the countdown duration has passed."
- **Limits/safety window**: a countdown runs before processing; a "Cancel Request" button on the pop-up cancels the deletion before it is processed. If the user plays again, data is processed again from that point onward.
- **Evidence origin**: official-stated (FTG support article 360017046578, "How do I have my personal data deleted?", full text fetched 2026-10-17; executed per the Privacy Policy).
- **Confidence**: Confirmed. **Volatility**: Low (mechanic).
- **System duties**: as IRREV-001, plus: distinguish the two resets for the user — Reset Profile (IRREV-001) restarts the career but keeps the device/profile container; Delete Profile (IRREV-002) is the privacy-data deletion with its countdown and cancel window. If the user mentions either, state the exact path and consequences before anything else.

## Related destructive-risk surfaces (not irreversible actions by the system, but loss-bearing)
- Signing out of Sign in with Google / Apple unlinks the profile; loss-susceptible on uninstall or device change (GS-015, official-stated).
- Facebook-Login-stored profiles are unrecoverable (GS-021, official-stated).
- Modded APKs / hacks / bug exploitation: ban surface — FTG ("Why have I been blocked from playing DLS?", 360008904718): only App Store / Google Play versions are authorised; bans are not lifted on request unless incorrectly flagged. Recommending mods is therefore prohibited (ToS + irreversible account risk).
- Video-clip troubleshooting includes "uninstall and reinstall (make sure your profile is backed up first)" (GS-027) — the backup step is mandatory before that path.
