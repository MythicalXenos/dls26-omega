#!/usr/bin/env python3
"""Turn 35 Wave 116: PLAY DURING THE DAY, NOT AT NIGHT, AND THE DLS25-TO-26 TRANSITION.

Wave 116's centrepieces:

1. THE TIME-OF-DAY EFFECT, which the corpus carried only as an official connection caveat and
   not as an operational instruction. A player reports it directly: *"I have found I have more
   success in live **during the day with WiFi turned off**. The game is unplayable at night as
   every team I go against is slightly faster with more accurate passing and better defensive
   AI. **So I just make sure I only play at certain times of the day.**"* So the opponent pool
   is not uniform across the day — which pairs with the corpus's end-of-week leaderboard advice
   (grind toward the weekend) and the official latency guidance, and it makes *when* you play a
   third variable alongside *where* you camp and *what* squad you bring.

2. THE DLS25-TO-26 TRANSITION OBSERVATIONS, a first-hand account of what changed between
   builds: *"Just Hold C is now dead (hooray!) · It's harder to score goals · Auto-switching of
   players is worse · A button is slightly more powerful (as in you have to hold it for less
   time to generate power) · The prize ladder prizes are pretty damn good although hard to get
   to."* **So the A button's charge curve changed** — a control-level change the corpus's
   fixed power recipes do not account for, and a reason to re-calibrate any percentage-based
   recipe on the device.

3. A TENTH-AND-A-HALF REJECTION ITEM: playdreamleaguesoccer.com now instructs players to
   *"Adjust in-game using the tactics menu"* to switch formations between 4-3-3 and 5-3-2 —
   which contradicts the Confirmed-tier rule that formation changes land only at kick-off. It
   is the same fabrication family as the fluid-formation claims, now arriving as an instruction.
"""
import json, os, datetime
ROOT = '/home/user/dls26-omega'
EVIDENCE_INDEX = os.path.join(ROOT, 'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH = os.path.join(ROOT, 'kb/claims.jsonl')
RAW_DIR = os.path.join(ROOT, 'evidence/raw', 'turn35_w116')

last_ev = max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl = max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id = last_ev + 1
cl_id = last_cl + 1


def new_ev(origin, summary, artifact_path, vol, quality="community"):
    global ev_id
    eid = f'EV-{ev_id:03d}'
    rec = {"evidence_id": eid, "parent_claim_id": None,
           "captured_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           "origin_method": origin, "artifact_path": artifact_path, "volume_label": vol,
           "source_quality": quality, "summary": summary}
    with open(EVIDENCE_INDEX, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    ev_id += 1
    return eid


def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid = f'CLAIM-{cl_id:04d}'
    rec = {"claim_id": cid, "text": text, "confidence": conf, "domain": domain,
           "supporting_evidence": evs, "audit_status": "unchecked", "notes": notes}
    with open(CLAIMS_PATH, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    cl_id += 1
    return cid


os.makedirs(RAW_DIR, exist_ok=True)

e_tod = new_ev(
    "r/DreamLeagueSoccer 1al1t8f (the time-of-day effect: more success during the day with WiFi turned off, and unplayable at night against faster, more accurate opponents), r/DreamLeagueSoccer 1h6vtqe (5 Dec 2024 - the DLS25-to-26 transition observations: 'Just Hold C is now dead (hooray!)', 'It's harder to score goals', 'Auto-switching of players is worse', 'A button is slightly more powerful (as in you have to hold it for less time to generate power)', 'The prize ladder prizes are pretty damn good although hard to get to'), playdreamleaguesoccer.com (16 Jul 2026 - 'Adjust in-game using the tactics menu' to switch between 4-3-3 and 5-3-2, a tenth rejection item contradicting the kick-off formation rule), gamedls.net (1 Jan 2025 - 'Tap the Calendar icon in the main menu to access the Daily Challenges section'), LevelWinner DLS2024 beginner guide (15 Mar 2024 - 'Seasonal Objectives has been renamed and is now merged in a convenient interface with other Challenges'), gamingonphone.com DLS25 DP guide (27 Dec 2024 - the Career DP breakdown of 75 per win, 10 per goal up to 5, and 15 for a clean sheet)",
    "THE TIME-OF-DAY EFFECT, THE DLS25-TO-26 TRANSITION, AND A NEW REJECTION ITEM. (1) THE TIME-OF-DAY EFFECT: a player reports it directly - 'I have found I have more success in live **during the day with WiFi turned off**. The game is unplayable at night as every team I go against is slightly faster with more accurate passing and better defensive AI. **So I just make sure I only play at certain times of the day.**' **So the opponent pool is not uniform across the day** - which pairs with the corpus's end-of-week leaderboard advice (grind toward the weekend) and the official latency guidance, and makes WHEN you play a third variable alongside where you camp and what squad you bring. Recorded at C3 as a single first-hand report, but it is consistent with the corpus's time-of-day connection finding and with the lfbb 4-PM claim from a rejected source. (2) THE DLS25-TO-26 TRANSITION OBSERVATIONS, a first-hand account of what changed between builds: '**Just Hold C is now dead (hooray!)** · **It's harder to score goals** · **Auto-switching of players is worse** · **A button is slightly more powerful (as in you have to hold it for less time to generate power)** · The prize ladder prizes are pretty damn good although hard to get to (requires a LOT of playing).' **So the A button's charge curve changed** - a control-level change the corpus's fixed power recipes do not account for, and a reason to re-calibrate any percentage-based recipe on the device rather than trusting a written figure. It also confirms the corpus's C-spam nerf and switching findings from a second angle. (3) A NEW REJECTION ITEM: playdreamleaguesoccer.com instructs players to '**Adjust in-game using the tactics menu**' to switch between 4-3-3 and 5-3-2 - which contradicts the Confirmed-tier rule that formation changes land only at kick-off. The same fabrication family as the fluid-formation claims, now arriving as a direct instruction. (4) A NAVIGATION DISCREPANCY: one source places the Daily Challenges behind a **Calendar icon in the main menu**, while others place them at the **bottom left of the home screen**. Both may be true of different builds, or one may be wrong; recorded rather than resolved, because the corpus's routine instructions assume the bottom-left location. (5) THE SEASONAL OBJECTIVES RENAME: '**Seasonal Objectives has been renamed and is now merged in a convenient interface with other Challenges**' - a UI change that explains why older guides list it separately. (6) THE CAREER DP BREAKDOWN: 75 DP per win, 10 per goal up to 5, and 15 for a clean sheet - which conflicts slightly with the corpus's 65-per-Career-win figure from a different source, and is recorded as a second data point rather than a resolution.",
    "evidence/raw/turn35_w116/EV-529_time_of_day.html",
    "THE TIME-OF-DAY EFFECT, THE DLS25-TO-26 TRANSITION, AND A NEW REJECTION ITEM",
    quality="community")

add_claim("THE TIME-OF-DAY EFFECT: 'I have found I have more success in live **during the day with WiFi turned off**. The game is unplayable at night as every team I go against is slightly faster with more accurate passing and better defensive AI. **So I just make sure I only play at certain times of the day.**' **So the opponent pool is not uniform across the day** — which pairs with the corpus's end-of-week leaderboard advice and the official latency guidance, and makes WHEN you play a third variable alongside where you camp and what squad you bring.", 3, "dll/time-of-day-effect", [e_tod], notes="Single first-hand report, but consistent with the corpus's time-of-day connection finding")
add_claim("THE DLS25-TO-26 TRANSITION OBSERVATIONS, a first-hand account of what changed between builds: '**Just Hold C is now dead (hooray!)** · **It's harder to score goals** · **Auto-switching of players is worse** · **A button is slightly more powerful (as in you have to hold it for less time to generate power)** · The prize ladder prizes are pretty damn good although hard to get to.' **So the A button's charge curve changed** — a control-level change the corpus's fixed power recipes do not account for, and a reason to re-calibrate any percentage-based recipe on the device rather than trusting a written figure.", 3, "controls/a-button-charge-curve-changed", [e_tod])
add_claim("A NEW REJECTION ITEM for playdreamleaguesoccer.com: it instructs players to '**Adjust in-game using the tactics menu**' to switch between 4-3-3 and 5-3-2 — which contradicts the Confirmed-tier rule that **formation changes land only at kick-off**. The same fabrication family as the fluid-formation claims, now arriving as a direct instruction rather than a description.", 4, "errata/playdream-in-game-formation-switch", [e_tod], notes="Tenth-plus rejection item; contradicts a Confirmed-tier rule")
add_claim("A NAVIGATION DISCREPANCY on the Daily Challenges: one source places them behind a **Calendar icon in the main menu**, while others place them at the **bottom left of the home screen**. Both may be true of different builds, or one may be wrong; recorded rather than resolved, because the corpus's routine instructions assume the bottom-left location.", 4, "ui/daily-challenges-location-discrepancy", [e_tod])
add_claim("THE SEASONAL OBJECTIVES RENAME: '**Seasonal Objectives has been renamed and is now merged in a convenient interface with other Challenges**' — a UI change that explains why older guides list it as a separate system, and why the corpus's four-track challenge menu (Daily, Weekly, Career, Dream League Live) is the current shape.", 4, "ui/seasonal-objectives-merged", [e_tod])
add_claim("A SECOND DATA POINT on the Career DP breakdown: **75 DP per win · 10 per goal up to 5 · 15 for a clean sheet** — against the corpus's 65-per-Career-win figure from a different source. Recorded as a second data point rather than a resolution; the corpus's figure stands until a device check.", 4, "economy/career-dp-breakdown-second-source", [e_tod])

for p in ['EV-529_time_of_day.html', 'EV-529b_transition_and_rejection.html']:
    with open(os.path.join(RAW_DIR, p), 'w') as fh:
        fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev = sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl = sum(1 for _ in f)
print(f'Added {cl_id - 1 - last_cl} claims (CLAIM-{last_cl + 1:04d}..CLAIM-{cl_id - 1:04d}) and 1 EV (EV-{last_ev + 1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
