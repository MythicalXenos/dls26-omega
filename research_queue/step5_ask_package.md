# Step-5 Ask Package — CONSOLIDATED (prepared 2026-10-03, Turn 20)
**Status:** prepared to disk; NOT yet delivered. Per the operating rules, all clarifying asks are batched into one consolidated Step-5 ask. This file is the exact packet to send to the user, in order, when Step 5 is reached (or when a step hard-stop requires user input). Delivering it ends the `>`-only loop.

**Why now:** research is saturated on everything retrievable with available tools. Three things remain that no amount of retrieval can settle: (1) live game-state facts that only exist on the user's device; (2) dimensions 1 and 4 of the taxonomy gate, which need in-client evidence; (3) four bookkeeping decisions only the user can make. Everything else is already on disk in this repo.

---

## THE PACKET (send verbatim, in this order)

**1. The single most valuable datum — your in-game ladder screen.**
Open the Prize Ladder (the English League Classics one) and send me, in text: (a) the exact **"LADDER ENDS IN"** text/timer as displayed, (b) your **current Dream Point total**, (c) which milestone player is next and what it shows as the requirement. That settles an unresolved conflict about event timing (14 October vs a later ladder end) and lets me tell you exactly what is still reachable with your remaining matches.

**2. Your resources (rough is fine).** Coins, Gems, how many Coach items you hold (and of which types), any Agents/Scouts, and whether you have any unspent Dream Point Boosts. Approximate numbers are fine — I only need the scale, not the exact digits.

**3. Your spending stance.** Confirm: free-to-play only, watching ads for free coins (you've stated this), or are you open to in-app purchases? If you'd buy something, what's your ceiling and on what (Season Pass / Gems / something else)?

**4. Your squad and division.** Current team OVR (rough), formation you're actually using, division you're in, and the one special card you said you're building around. A screenshot of the squad screen would be ideal if you can attach one.

**5. Prompt capture upgrade (bookkeeping, important).** Right now the bootstrap prompt only exists as a digest, and per the rules no file may sit at `DLS26_OMEGA_PROMPT.md` unless it's a verbatim copy. If you want mechanical capture, commit the exact prompt text to the repository root of `main` as `DLS26_OMEGA_PROMPT.md` (you can do this in the GitHub web UI in about a minute). That upgrades the capture status from DIGEST-ONLY to MECHANICAL. Pasting it into chat also works and I'll place it.

**6. Two open PRs and one proposal.**
   - PR #3 is mine (this session's work). PRs #1 and #2 are earlier ones — do you want them closed, merged, or left alone? I will not merge anything until you explicitly say the session is done.
   - A prior session left a **PROPOSED amendment** to the confidence rules: a "direct-origin tier" so that first-party documentation (like FTG's own support articles) can score above the current single-source cap. I have documented the same tension again this session. Say **yes** to adopt it, **no** to keep the current rules, or **tell me your preferred wording** and I'll apply it.

**7. Optional, high-value screenshots (any one of these closes a real conflict instantly):**
   - Coaching screen → closes most of gate dimension 1.
   - Any one Cult Hero card you own → settles the 12th-Man OVR conflict (Vozinha 83 vs 84).
   - The Petit or Berbatov ladder card → settles the last ±1 estimate conflict.
   - Your transfer list showing a coin price → validates the price model (86 CF = 2,970 coins).

---

## WHAT THIS PACKET DOES NOT ASK
Nothing else is required. Twenty turns of research are on disk; the remaining open questions (gate dims 1 and 4, the `14 October` timer, live balances) are precisely the ones only you or your device can answer.

_End of package._
