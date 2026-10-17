# STEP 3 — DEVICE PIPELINE PROTOCOL (DRAFT, no device contacted)
Prepared 2026-10-17T22:55Z. Defines how screenshots and observations from the player's device enter the repo as first-class evidence. No device has been contacted; this is protocol only.

## Consent and safety preconditions (MUST all be true before any device data is ingested)
1. **S1 verified** (CLAIM-128): Sign in with Google / Sign in with Apple is **Linked** on the player's device. Recorded in `raw_game_data/consent/SAFETY_S1_linked.txt` with timestamp.
2. **S2 captured** (CLAIM-125): System Info → Copy Info pasted back to chat. The build string is extracted and recorded in `raw_game_data/consent/build_and_user_id.txt`. User ID itself is stored locally only; it is never included in commit messages or pushed to public-facing chat.
3. **Explicit consent for screenshots** captured in chat: the player says they are willing to share screenshots. Recorded in `raw_game_data/consent/SCREENSHOT_CONSENT.txt`.
4. **OBS-013 resolved**: player confirms they are the legitimate owner of the installed copy and no ToU-prohibited action is requested.

All four files are git-ignored (`raw_game_data/consent/*` is in `.gitignore` by convention; verify before first commit) because they contain the User ID and consent text; the claims derived from them are committed, not the raw paste.

## Directory layout (created under `raw_game_data/`)
```
raw_game_data/
  consent/               (git-ignored: User ID, consent text)
  screenshots/
    session_YYYYMMDD_HHMMZ/
      00_main_menu.png
      01_season_leaderboard.png
      02_options_controls.png
      03_graphics.png
      ...
      manifest.json       (for each file: filename, screen name, claim(s) it supports, sha256)
  ocr/
    session_YYYYMMDD_HHMMZ/
      <filename>.txt      (ocr text, one per screenshot; human-corrected if needed)
  notes/
    session_YYYYMMDD_HHMMZ.md   (player's typed answers, in order of the first-contact script)
```

Naming rules:
- Two-digit zero-padded prefix preserves screen order.
- Filenames use English snake_case even if the UI is in another language; the notes file captures language.
- `manifest.json` is the index; nothing is referenced from a claim unless it is in the manifest.

## Ingestion procedure (per session)
1. Player sends screenshots via chat (Arena chat can accept image attachments). Save attachments verbatim to `screenshots/session_*/` with the ordered prefix.
2. For each screenshot, compute sha256 and write a manifest row.
3. For each screen, write an EV record in `docs/continuity/a7e23a6b/evidence/` of the form `EV-###_inclient_<screenname>.md` with:
   - `origin_method: in-client-observation`
   - `authenticity_limits: user-stated / single-device observation; tier limited to Community Consensus until corroborated across sessions or against official text`
   - `covers[]` listing the claim(s) the screenshot supports.
4. Where the player typed a textual answer instead of a screenshot, write a `notes/session_*.md` entry and cite it as supporting evidence the same way, with an EV record (a second EV per note is not required if the note is recorded inline in the EV file's "Player-stated answer" section).
5. Cross-check each new observation against the existing KB:
   - **Matches** → strengthen freshness / note `in_client_observed_at` on the claim.
   - **Differs in values** (build number, OVR range, label wording) → update the claim if the new observation is more current, but record what changed and why the older value is superseded.
   - **Contradicts a mechanism** → open a conflict in `logs/conflicts.md`, do not overwrite.
6. Take a snapshot `kb_snapshots/claims_<utc>.jsonl` after every session.

## OCR / transcription
- If screenshots are readable English and small enough, direct reading in the viewer is sufficient — no OCR required.
- If text is dense (e.g. full coach list, transfer-market prices, Prize Ladder milestones), produce a `.txt` transcription in `ocr/` and mark it `raw-transcribed` so later auditors know a human typed it.
- Screenshots with no readable text (e.g. kit customisation preview) are still useful as existence proofs for UI surfaces; record them with an EV file describing what they show.

## Prohibited device actions (Step 3)
These echo the Step 2 forbidden list and apply even when we are "only observing":
- No `adb` without consent documented in `consent/ADB_CONSENT.txt`.
- No packet capture, no debugger, no memory inspection.
- No save-file pulls or edits.
- No requests to install modded APKs or unknown-sourced tools.
- No gameplay automation; matches played for data are played manually by the player.
- No request that the player share passwords, payment info, or personal data beyond the User ID (which goes to FTG support, not to us — we only need build + whether it matches expected format).

## First session plan (after consent)
Session 0 targets the Priority 0 + Priority 1 items from the first-contact script, in order:
1. S1/S2 (paste + confirmation).
2. Item 0: Season Leaderboard screenshot (C-009 resolution).
3. Items 1–5: Controls / Graphics / Camera pre-kickoff / one starter's attribute panel / any visible build number.

After session 0, the bootstrap has enough data to:
- Resolve C-009 (mission definition).
- Confirm or correct control labels, graphics path, stat labels, build.
- Open a concrete follow-up (Priority 2/3) batched ask for the next session.

## Step 3 readiness check (to run just before first contact)
- [ ] `raw_game_data/` exists with `.gitignore` protecting `consent/*` from accidental commit.
- [ ] Manifest template `raw_game_data/_template_manifest.json` exists.
- [ ] OCR fallback plan documented (manual transcription if no OCR tool is installed in the sandbox).
- [ ] Step-3 protocol reviewed against OPERATIONAL_RULES.md.
- [ ] Sandbox network confirmed still at ACCESS_BOUNDARY (no outbound device traffic is expected — screenshots come in via chat, not via network to the device).
