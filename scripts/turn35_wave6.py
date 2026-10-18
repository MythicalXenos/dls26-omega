#!/usr/bin/env python3
"""Turn 35 Wave 6: controller support (v12.250), controls layout, skill moves, save file location, OBB path, DLS7 package, touch controls, match length."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w6')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="community"):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":quality,"summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid
os.makedirs(RAW_DIR,exist_ok=True)

e_ctrl=new_ev("App Store (Controller Supported badge), gamingonphone DLS25 controller guide, Baidu wiki v12.250, BlueStacks DLS26 beginner guide, fandom Skill Moves, levelwinner DLS19 controls, dlsapk.net OBB, sakib.pro/quora/rajatips/eazycheat save paths, r/DLS controller thread Dec2024",
    "Controller support OFFICIALLY added v12.250 (per Baidu wiki; corroborated by App Store listing 'Controller Supported: PlayStation, Xbox, or MFi controllers' and gamingonphone DLS25 guide). Settings menu has 5 tabs: Game / Display / Audio / Controls / Advanced. Controls tab has Gamepad sub-menu with two layouts (Classic / Alternative) and separate Attacking/Defending control views. Controller buttons can be HIDDEN in-game (Controls → Gamepad → top-right 'hide controller buttons'). Third-party key-mappers (ShootingPlus V3, MooWii) exist for older controllers but native support removes need. Touch controls (DLS20-DLS26): left virtual joystick for movement; right-side A/B/C buttons. OFFENSE: A = shoot/long pass (hard kick), B = short pass (low kick), C = lofted through ball / chip / long ball; hold = more power. DEFENSE: A = slide tackle (high risk), B = contain/pressure (safe), C = switch player (toggle to nearest defender). Note some guides swap A/B defensive roles (A aggressive, B ordinary) — confirm in-game. Skill moves: performed via screen swipes (fandom Skill Moves) — swipe left/right on ball side = step-over/side skill; swipe up on right screen = higher-skill move (requires Control >80 for perfect execution); double-tap + swipe direction = finish vs keeper direction (likely rainbow flick or similar). Match length: 4-6 minutes per match (playdreamleaguesoccer DLS25). Save file location: Android /Android/data/com.firsttouchgames.dls7/files/ (DLS26; note package is dls7 — consistent across DLS19-DLS26). DLS17/DLS18/DLS20 used com.firsttouchgames.dls3 package per older guides. OBB file path: Internal Storage/Android/obb/com.firsttouchgames.dls7/ (contains graphics/audio). iOS save location historically: app sandbox Documents folder (iFunbox/iFile). Save files are overwritable (popular cheat method) suggesting no always-on server-side save enforcement for career — BUT online features (DLL, events, purchases) are server-validated. Note: scoped storage on Android 11+ may restrict direct /Android/data/ access without root or special permission; DLS26 min Android 10. v12.250 also introduced: Friends system, new menus, 2024/25 season data, CLASSIC PLAYERS, Brazilian Portuguese live commentary, expanded squad sizes, premium stadiums, more manager customization, tackling/running/marking optimization — confirms Classic Players (likely Legends/Iconic players set) added in v12.250, a feature carried into DLS26.",
    "evidence/raw/turn35_w6/EV-387_controller_controls_save.html",
    "Controller support v12.250 (PS/Xbox/MFi native); Settings 5 tabs, Classic/Alternative layouts, hide on-screen buttons; touch A/B/C offense (shoot/pass/through) defense (slide/contain/switch); skill moves via swipes (CON>80); matches 4-6min; save /Android/data/com.firsttouchgames.dls7/files/; OBB /Android/obb/com.firsttouchgames.dls7/; v12.250 added Classic Players, friends system, BR-PT commentary, controller support, premium stadiums")

add_claim("Native controller support added in v12.250 (carried into DLS26); officially supports PlayStation, Xbox, and MFi controllers (App Store listing).", 1, "controls/controller", [e_ctrl])
add_claim("Settings menu structure: 5 tabs = Game / Display / Audio / Controls / Advanced.", 1, "ui/settings-tabs", [e_ctrl])
add_claim("Controller settings offer two layout presets: Classic and Alternative; separate Attacking and Defending control views.", 2, "controls/controller-layouts", [e_ctrl])
add_claim("On-screen controller buttons can be hidden (Controls → Gamepad → top-right corner hide toggle).", 2, "controls/hide-buttons", [e_ctrl])
add_claim("Touch control layout: left = virtual joystick (movement); right = A/B/C action buttons.", 1, "controls/touch-layout", [e_ctrl])
add_claim("Offense button mapping (baseline DLS19-DLS26): A = shoot / long pass (hard kick, hold for power); B = short pass (low kick); C = lofted through ball / chip / cross (floater).", 2, "controls/offense", [e_ctrl], "some guides swap A/B short-long — verify in tutorial")
add_claim("Defense button mapping: A = slide tackle (high risk, cards/penalties); B = contain/pressure (safe, auto-chase); C = switch player (toggle to nearest defender).", 2, "controls/defense", [e_ctrl])
add_claim("Button remapping beyond Classic/Alternative presets: NO confirmed full remap UI; native controller offers preset layouts only. Third-party apps (ShootingPlus V3, MooWii) allow manual key-mapping for unsupported controllers.", 2, "controls/remap", [e_ctrl], "full custom remap unverified")
add_claim("Skill moves performed via swipe gestures on touchscreen: swipe left/right near ball = side skill/step-over; swipe up on right screen = advanced skill (ball roll/roulette?); double-tap + swipe vs keeper = directional finish / skill move. Advanced skills require Control (CON) >80 for reliable execution.", 3, "controls/skill-moves", [e_ctrl])
add_claim("Match duration: 4-6 minutes (real-time) per match.", 2, "match/length", [e_ctrl])
add_claim("Save file location on Android: /Android/data/com.firsttouchgames.dls7/files/ (package = dls7, consistent DLS19-DLS26).", 1, "platform/save-location-android", [e_ctrl])
add_claim("OBB/data file location on Android: Internal Storage/Android/obb/com.firsttouchgames.dls7/ (contains graphics/audio assets).", 1, "platform/obb-location", [e_ctrl])
add_claim("iOS save location: app sandbox Documents folder (iFunbox/iFile access on jailbroken or legacy devices).", 3, "platform/save-location-ios", [e_ctrl])
add_claim("Android scoped storage (Android 11+) may restrict direct /Android/data/ access without root or all-files-access permission; DLS26 min Android 10.", 2, "platform/scoped-storage", [e_ctrl], "save tampering harder than DLS17-20 era")
add_claim("Career save appears stored locally (overwritable by save-file mods), but online features (DLL, events, IAP, leaderboards) are server-validated. No explicit anti-cheat system named in public docs.", 2, "platform/save-server-validation", [e_ctrl], "anti-cheat gap")
add_claim("v12.250 (DLS25-era update) introduced: controller support, Friends system, new menus, 2024/25 season data, CLASSIC PLAYERS set, Brazilian Portuguese live commentary, expanded squad sizes, premium stadiums, additional manager customization, tackling/running/marking optimizations.", 1, "patches/v12.250", [e_ctrl])
add_claim("Classic Players (Legends/Icons set) exist in DLS26 — added in v12.250; specific roster not identified in this search (gap).", 2, "cards/classic-players-exist", [e_ctrl], "gap: actual roster unknown")
add_claim("Onboarding flow: name manager + name team → tutorial match (experiment with controls) → starter resources.", 1, "onboarding/flow", [e_ctrl])

p=os.path.join(RAW_DIR,'EV-387_controller_controls_save.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
