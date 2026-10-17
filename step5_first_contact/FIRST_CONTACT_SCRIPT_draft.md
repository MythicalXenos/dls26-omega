# FIRST CONTACT SCRIPT — turn 21 (DRAFT, not sent)
Prepared 2026-10-17T22:50Z. This is the message that will be sent to the player when the machine reaches Step 5 and OBS-013 is resolved. It is drafted now so it can be audited against OPERATIONAL_RULES before transmission. The script is short, batched, and leads with safety.

## Design constraints
- **Lead with safety, not tactics.** Before any advice, we must know the profile is secured (CLAIM-128) and have a build/User-ID recovery handle (CLAIM-125). A lost account overrides every coaching goal.
- **One question unlocks the mission definition (C-009 Priority 0).** Everything else is tiered by how much it blocks advice.
- **Screenshots over transcription.** Where a screenshot is easier than typing, say so.
- **No jargon, no unexplained acronyms.** The player is not expected to know OVR, DLL, etc., until the game surfaces the term.
- **No premature optimisation.** Don't ask about squad/formation before we know which platform/build/tier they are on.

## The message (candidate v1)

> Before we start — two quick safety checks so nothing we do can risk your account:
>
> **S1.** Open DLS → Options (gear, top-left). In account settings, is "Sign in with Google" (iOS: "Sign in with Apple") shown as **Linked / Connected**? If not, please tap it and link the profile now — unlinked accounts can't be recovered if something goes wrong.
>
> **S2.** Still in Options → Advanced → **System Info** (the "i" button) → tap **Copy Info**, then paste it here. That gives me your exact build and a User ID recovery handle; you don't need to share anything else from that screen.
>
> Once those are confirmed, I have one question that decides what "#1" means on your account:
>
> **0.** On the Main Menu there's a **Season Leaderboard** tile. Could you open it and tell me — (a) does it list **other players** by name, or only your own total? (b) is there a visible **rank/position number**? (c) any **reset timer** or season label (e.g. "resets in 12 days")? (d) a scope toggle (global / friends / division)? A screenshot of this screen is ideal if that's easier.
>
> After that, five quick checks (each is one screen, ~5 minutes total):
> 1. **Controls**: Options → Controls — the full list of toggles and their current values (auto-switch, any "assist" switches, layout choice if there is one). Screenshot works.
> 2. **Graphics**: Profile (or Options) → Graphics — FPS cap and quality preset you run.
> 3. **Camera**: start any match, pre-kick-off — what camera height/zoom options are offered, and which do you use?
> 4. **Squad → pick any starter**: open their attribute panel and tell me the exact stat labels shown (do they read SPE/ACC/STA/CON/…, or are they renamed?).
> 5. **Main menu**: is a version/build number displayed anywhere, and what does it say?
>
> Take your time — each answer becomes a fact I can coach from, not a quiz.

## Why this ordering
1. S1/S2 are non-negotiable: they precede every other item because the consequences of getting them wrong are irreversible (lost profile).
2. Item 0 is Priority 0 per C-009: the answer determines whether "#1" is a measurable global/season rank, a DLL Tier, or a self-competition target. We cannot write any operational rule that mentions "rank" until this is known.
3. Items 1–5 are Priority 1 (execution advice blockers): controls, FPS, camera, stat labels, build. None is intrusive; none reveals personal data.
4. Priorities 2–3 (division, coin rates, squad, transfers, inventory) are asked in a follow-up message AFTER the Priority 0/1 answers are back, because some of them become unnecessary depending on the answers (e.g. if the player is on a pre-13.430 build or on iOS where Graphics is elsewhere).

## What happens when answers come back
- Each observation is recorded as a claim with `user-stated` origin at the tier it supports (single-screen = Community Consensus until corroborated).
- Screens that contradict the KB go into `logs/conflicts.md`, not silent overwrite.
- S1/S2 failure modes (profile not linked; Copy Info doesn't match expected format) have their own short follow-up ("please go to … and tap Link") before we proceed.
- If the player cannot answer an item for any reason, we mark it unknown and move on — nothing is forced.

## What the message explicitly does NOT do
- Does not ask the player to spend coins/gems or make any squad/formation change yet.
- Does not ask them to win/lose/play matches for data on first contact.
- Does not ask them to download, install, or mod anything.
- Does not reveal internal codenames (CLAIM, EV, CKPT, etc.).
- Does not promise any specific rank or outcome.
