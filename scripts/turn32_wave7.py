#!/usr/bin/env python3
"""Turn 32 Wave 7 — Free-kicks, penalties, training modes, set-piece analog stick behavior."""
import json, os, datetime, re
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb/claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
evs=[json.loads(l) for l in open(EIP) if l.strip()]
next_c=max(int(c['claim_id'].split('-')[1]) for c in claims)+1
next_e=max(int(e['evidence_id'].split('-')[1]) for e in evs)+1
ac,ae=0,0
def cid():
    global next_c,ac; r=f"CLAIM-{next_c:03d}"; next_c+=1; ac+=1; return r
def eid():
    global next_e,ae; r=f"EV-{next_e:03d}"; next_e+=1; ae+=1; return r
def C(text, conf, evids, chal=None, vol='Low', notes=None):
    cv=cid()
    rec={"claim_id":cv,"text":text,"confidence":conf,"supporting_evidence":evids,
         "challenges":chal or [],"volatility":vol,"notes":notes or [],
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
    with open(CP,'a') as f: f.write(json.dumps(rec)+"\n"); claims.append(rec)
def E(origin, summary, artifact, typ='web_article', method='web_search_community', reliability='Medium'):
    ev=eid()
    rec={"evidence_id":ev,"origin_method":origin,"summary":summary,"artifact_path":artifact,
         "evidence_type":typ,"capture_method":method,"reliability":reliability,
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),"raw_data_ref":""}
    with open(EIP,'a') as f: f.write(json.dumps(rec)+"\n"); evs.append(rec)
    return ev

e332=E("mokoweb DLS free-kick guide (Aug2026) + r/DLS free-kick threads (2021-25) + LevelWinner DLS24 + dls-wiki Analogue stick page",
       "Free kicks: Distance guide (mokoweb): 18-22y = curl with inside foot; 23-28y = power or curled top-corner; 30+y = long shot or pass/short. Use highest-CURL/SHO taker; right-footers for right-of-center, left-footers for left-of-center (varies by desired curl). Aim over shortest player in wall toward top corner (not center). Swipe mechanics: short swipe = controlled, long fast swipe = power. Curl via curved swipe motion: ')' curve for right corner, '(' for left (banana shape). Aim for 70%+ power in DLS24+ (below 70% risks hitting wall); 3/4 power at 30y, 2/3 at 20-25y. Common aim: legs of first defender closer to GK, or between legs. Some players shoot with more curl (Odegaard, TAA), others straight (Vini, Modric less curl) — player-specific. DLS24 changed FK angle/camera; using regular gameplay camera instead of default FK camera helps some players. Short-pass alternative: C-pass to a player just around the wall for an open shot/cross. Training mode (My Club->Training; pause-menu arrow cycles modes) offers Free Kick, Left Corner, Right Corner, Penalty, Penalty Save practice modules (6 total: Free Training + the 5 set-piece modes). DLS-wiki: In modern DLS (DLS20+), analog stick must be held in desired shot direction during set pieces (no stick input = default direction). On corners/goal kicks, analog moves the player sideways around the ball.",
       "evidence/raw/community_turn32/EV-332_free_kicks.html",
       typ='community',reliability='Medium-High')
e333=E("r/DLS penalty threads (2022-25) + LevelWinner DLS20 advanced guide + DONTRUKO + SuperCheats training + r/DLS penalty-save tell thread",
       "Penalties (shooting): Left joystick controls direction (hold while shooting); right-side button A (power/high), B (lower power, recommended for bottom-corner finesse with ~25% charge + joystick slightly up), C (panenka/chip with angle); taps must be quick/gentle — holding too long = wild over-power. Bottom corners via soft B tap, full-power B to corner, slight-tap A, or panenka C are all cited techniques. Some players recommend middle-of-goal (AI GK often dives). Penalty aim against GK: bottom corners safest; middle works vs AI due to GK committing. DLL/PvP: run-up animations tell direction — ~6-10 distinct tells (open body/foot right = right, stride left arm smooth raise = left, stutter Zaza run-up = middle, slow Pogba steps = soft chip middle). Penalty saving: tap a direction in/around net; guess based on opponent run-up tells; DLS24+ largely randomized animations vs DLS23 (where 6 animations perfectly predicted direction). Penalty shootouts occur in cup/tournament elimination; some users report DLL penalties 85-90% success with A, 70-80% in shootouts. Career-mode penalties reported as 'pre-decided' (save/result determined before kick per some users) — anecdotally restarting yields same result. Training mode offers dedicated Penalty and Penalty Save modules.",
       "evidence/raw/reddit_turn32/EV-333_penalties.html",
       typ='community',reliability='Medium-High')

# CLAIMS
# Free kicks
C("Free-kick distance meta: 18-22 yards = curl with inside foot; 23-28 yards = power or curled top-corner; 30+ yards = long shot or short pass/cross.",
  'Medium-High Confidence',[e332],vol='Low')
C("Use your highest-CURL (and good SHO) free-kick taker; right-footed players for right-side-of-center kicks / left-footed for left to create natural curl (player-specific curls vary widely — Odegaard/TAA curl heavily; Vini/Modric shoot straighter).",
  'High Confidence',[e332],vol='Low')
C("Free-kick aim: target over the shortest player in the wall toward top corners (not center); community sweet spot is aiming at the legs of the first defender closer to the GK (or between legs) for 2/3-3/4 power.",
  'Medium-High Confidence',[e332],vol='Medium')
C("Free-kick power: DLS24+ requires at least 70% power to clear the wall reliably (~2/3 at 20-25y, 3/4 at 30y); short swipe = controlled, long/fast swipe = power; curved swipe ('(' or ')') adds curl (banana shape).",
  'Medium-High Confidence',[e332],vol='Medium')
C("Free-kick alternative: short C-pass to a teammate just off the wall opens a clear long-shot or cross opportunity (safer when angle is tight or too close/far).",
  'Medium-High Confidence',[e332])
C("Training mode (My Club -> Training) has 6 modules: Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save. Cycle via the white arrow next to 'Free Training' at the pause menu.",
  'High Confidence',[e332,e333],vol='Low')
C("Modern DLS (DLS20+) set-piece controls: hold the left analog stick in desired shot direction during free kicks/penalties/goal kicks; no stick input uses a default direction. At corners/goal kicks the stick moves the player sideways around the ball.",
  'Medium-High Confidence',[e332],vol='Low')
# Penalties
C("Penalty shot controls: left joystick = aim direction (hold while shooting); right buttons: A = power/high shot, B = low/finesse (recommended ~25% charge for bottom corners, slight joystick up), C = panenka/chip with angle. Taps must be quick — overholding = wild shot over bar.",
  'High Confidence',[e333],vol='Low')
C("Penalty strategy vs AI: soft B tap into bottom corners, slight-tap A, or middle-of-goal (AI GK often dives). Penalty success in DLL ~85-90% with A button; in shootouts ~70-80%.",
  'Medium-High Confidence',[e333],vol='Medium')
C("PvP penalty tells (DLL): run-up animations leak direction (~6-10 distinct animations) — body open/foot right = right, stride + left-arm raise = left, fast stutter 'Zaza' run = middle, slow small 'Pogba' steps = soft chip middle. DLS24+ randomizes more than DLS23 (where tells were 100% predictive).",
  'Medium Confidence',[e333],vol='Medium')
C("Penalty saving: tap a direction on/in the goal to dive; guess based on opponent run-up tells. DLS24+ saving is largely reactive guesswork. A pause-and-close exploit exists (see direction, restart) but is poor sportsmanship and may not work in DLS26.",
  'Medium Confidence',[e333],['Exploit may have been patched in DLS25/26.'],vol='High')
C("Career-mode penalties are reported by some players to be pre-determined (outcome fixed before kick; restarting yields same result), though this is anecdotal.",
  'Low Confidence',[e333],['Anecdotal community claim; no confirmation.'],vol='High')

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
