# raw_game_data — player-supplied observations
This directory holds screenshots, typed answers, and (only with separate explicit consent)
pulled files from the player's device.

Layout per PROTOCOL_draft.md:
  consent/   GIT-IGNORED — User ID, consent text, S1/S2 safety confirmations
  screenshots/session_*/   ordered screenshots + manifest.json
  ocr/session_*/           manual transcriptions where text is dense
  notes/session_*.md       player's typed answers

Do NOT commit anything under consent/. Device filenames should not contain the player's
real name, email, or User ID prefix.
