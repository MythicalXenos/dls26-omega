#!/usr/bin/env python3
"""Turn 32 Wave 8 — Formations/tactics catalog + controller support (PS/Xbox/MFi, native DLS25+, mapping)."""
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

e334=E("mokoweb DLS formations guide (Oct2026) + dreamleaguesoccerkits.com May2026 beginner guide",
       "DLS offers 8 base formations (with 28 sub-formations total per mokoweb) and 3 tactics options. Catalog: (1) 4-4-2 Classic: balanced 4DEF/4MID/2ST; versatile defensive or attacking; wingers cross; central mids need good passing; pair tall target man + quick technician (e.g., Haaland + Messi/Neymar). (2) 3-5-2: 3DEF/5MID/2ST; possession-dominant via extra midfielder; wing-backs transition D-to-O; centerbacks must be strong/aerial; include a DM to shield backline (cited as best formation by author). (3) 4-3-3: 4DEF/3MID/3ST; wide-attack focused; wingers stretch defense for central ST + AM; need fast/skillful wingers + clinical finisher. (4) 4-2-3-1: 4DEF/2DM/3AM/1ST; solid D + potent central attack; fullbacks overlap for width (use pacy fullbacks). (5) 5-3-2: 5DEF/3MID/2ST; defensive/counter-attack; energetic wing-backs cover large areas; strikers hold up play and finish. (6) 4-5-1: 4DEF/5MID/1ST; possession-heavy, shifts to 4-3-3 when wingers push; playmaker CM dictates tempo. (7) 3-4-3: 3DEF/4MID/3FW; all-out attack; overloads defense; wide players cross and cut inside (pacy/skillful wingers); mid must win ball. (8) 4-1-4-1: 4DEF/1DM/4MID/1ST; balanced control + sudden attack; holding mid breaks up play and transitions. (9) 4-3-2-1 'Christmas Tree': 4DEF/3MID/2AM/1ST; central layered attack; mixed defensive/attacking mid trio. (10) 4-1-2-1-2 Diamond: 4DEF/1DM/2CM/1AM/2ST; narrow central short-passing game with triangle sequences; no wingers so fullbacks must provide width and need stamina; vulnerable to wide counter-attacks. Beginner guide top recs: 4-3-3 (attack/counter), 4-4-2 (balanced/crossing), 4-1-2-1-2 (quick central possession). In-match formation changes take effect only at next restart (kickoff/goal kick); throw-ins/corners/free-kicks allow subs but NOT formation changes.",
       "evidence/raw/community_turn32/EV-334_formations.html",
       typ='guide',reliability='High')
e335=E("App Store US DLS26 listing + gamingonphone controller guide + r/DLS controller threads + @dreamleaguesoccer.ftg TikTok + dls-wiki Analogue stick",
       "Controller support: DLS25 added official controller support (confirmed by FTG FAQ + FTG official TikTok Dec2024 'now fully supported'); DLS26 App Store officially lists 'Controller Supported: PlayStation, Xbox, MFi'. PS4/PS5 DualShock/DualSense connect via Bluetooth (hold Share+PS buttons until flashing ~5 sec, pair in phone BT settings); Xbox controllers also supported (BT); MFi for iOS. Game includes Gamepad Options menu with 'Classic' (default) vs 'Alternative' (custom) controller profiles; can hide on-screen touch buttons when controller active; supports custom button mapping. Auto-pressing defense (B button) requires steering with analogue stick simultaneously; holding B without stick input does nothing. Bluestacks/PC emulation historically used keymapping (pre-native support). Some third-party apps (e.g., ShootingPlus V3) used for non-standard controllers but not recommended. DLS26 controller mapping (inferred from DLS conventions + classic layout): Left stick = movement; A (cross on PS) = short pass / pressure (defense) / header; B (circle) = shoot / sliding tackle / clearance; C (square) = lob/through / player switch / GK rush. Exact button labels customizable via profile.",
       "evidence/raw/official_turn32/EV-335_controller.html",
       typ='official+community',reliability='Medium-High')

# CLAIMS
C("DLS26 features 8 base formations with 28 sub-formation variants total, and 3 selectable tactics. 10 common named formations appear across guides.",
  'High Confidence',[e334],['Mokoweb says 8/28 sub-formations but lists 10 named lineups — the extra two are likely diamond/xmas-tree variants.'],vol='Low')
C("Formation catalog & roles: 4-4-2 (balanced, one tall target man + one quick technician ST, crossing wingers, good-passing CMs); 3-5-2 (possession, strong/aerial CBs, DM shield, attacking wing-backs — author's top pick); 4-3-3 (wide attack, fast/skillful wingers, clinical ST); 4-2-3-1 (solid D + central attack, pacy overlapping fullbacks); 5-3-2 (defensive/counter, energetic wing-backs, hold-up STs); 4-5-1 (possession, shifts to 4-3-3 in attack, playmaker CM dictates); 3-4-3 (all-out attack, crossing/inside-cutting wingers); 4-1-4-1 (balanced control, DM anchors transitions); 4-3-2-1 Christmas Tree (central layered attack); 4-1-2-1-2 Diamond (narrow central short-pass triangles, fullbacks provide width, vulnerable to wide counters).",
  'High Confidence',[e334],vol='Low')
C("Beginner-favored formations: 4-3-3 (attack/wing play/fast counters, easiest for new players), 4-4-2 (simple/defensive balance/crossing), 4-1-2-1-2 (quick central possession play).",
  'Medium-High Confidence',[e334],vol='Low')
C("In-match formation changes only apply at next restart (kickoff, goal kick). Throw-ins/corners/free kicks allow substitutions but not formation switches.",
  'High Confidence',[e334])
# Controllers
C("Official controller support added in DLS25 and carried to DLS26 (FTG-confirmed). App Store listing: 'Controller Supported: PlayStation, Xbox, MFi'. No third-party software required.",
  'Very High Confidence',[e335])
C("Controller pairing: PS4/PS5 DualShock/DualSense — hold Share + PS buttons simultaneously for ~5 seconds until light bar flashes, pair via phone/tablet Bluetooth menu. Xbox/MFi controllers connect via standard BT pairing. On-screen touch controls can be hidden in Gamepad Options when controller active.",
  'High Confidence',[e335])
C("Gamepad Options menu offers 'Classic' (default) and 'Alternative' (custom) controller profiles, with support for creating custom button-mapping profiles.",
  'Medium-High Confidence',[e335],['Exact mapping details not fully confirmed in official docs; inferred layout from community.'],vol='Medium')
C("Inferred default controller layout (mirrors touch buttons): Left stick = player movement; A (Cross on PS) = short pass / pressure defense / header; B (Circle) = shot / sliding tackle / clearance; C (Square) = lob pass / through ball / manual player switch / GK rush. Auto-pressing (hold B on defense) requires simultaneous stick direction — holding B alone will not move the defender.",
  'Medium Confidence',[e335],["Button labels (A/B/C) from DLS touch naming; exact controller-face-button mapping requires in-game verification."],vol='Medium')
C("Pre-DLS25 controller play required BlueStacks PC emulation with keymapping or third-party apps (e.g., ShootingPlus V3 for iOS), neither of which is endorsed or needed post-DLS25.",
  'High Confidence',[e335])

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
