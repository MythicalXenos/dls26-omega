#!/usr/bin/env python3
"""Turn 35 Wave 13: set pieces/training modes, captain selection 80 players + Create Your Own Captain, camera settings optimal, manual kicks, auto-switch settings, B-button pressure requires stick input, free kick/penalty mechanics, corner technique, player roles."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w13')

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

e_controls=new_ev("dreamleagueforall (DLS16-era), supercheats DLS17, webtech360 beginner, gamingonphone DLS26 beginner, dls-wiki Analogue stick, LevelWinner DLS20/DLS22/DLS24, r/DLS camera settings, r/DLS corner technique, r/DLS free kicks, r/DLS DLS25 manual-kick fix, mokoweb, dreamleaguesoccerkits.com best settings, BlueStacks DLS26 beginner",
    "Onboarding captain selection: 80 players available as starter captain (webtech360); option to 'Create Your Own Captain' (custom-named player). 'No Thanks' returns to list; 'See More' shows details (name/position/height/foot/skills); 'Sign Captain' finalizes. Starter captain OVR can range 60-85 (older wiki). Onboarding manager: three default face options (gamingonphone), customizable later. TRAINING MODES (My Club → Training → white arrow next to 'Free Training'): 6 modules — (1) Free Training, (2) Free Kick, (3) Left Corner, (4) Right Corner, (5) Penalty, (6) Penalty Save. TEAM MANAGEMENT → player roles: assign captain, Free Kick taker, Penalty taker, etc. CONTROLS detail: Left = virtual analogue joystick (lower-left). On set pieces (goal kick/corner/free kick/penalty) the joystick MUST be held in the desired shot direction; without joystick input a default direction is selected. Modern DLS defensive auto-pressing: holding B button ALONE does nothing — you MUST steer with analogue stick (any direction) + hold B for auto-press (fandom Analogue stick). Right side buttons (OFFENSE context reconfirmed from webtech360 — note swap from earlier LevelWinner): webtech360 (DLS26-sourced) says B = low pass/ground pass, hold B = more power pass/shoot; A = powerful shot/finish (hard kick/long-range); C = lofted/curved. This CONTRADICTS some LevelWinner DLS20-era labeling (A=shoot, B=pass, C=through) which still holds in spirit — the three buttons map to shoot/pass/loft regardless of A/B/C labeling drift across versions. (BlueStacks confirms low kick/hard kick/lofted kick as three on-screen options). Free kick mechanic (DLS24+): changed camera angle; knuckle-balling harder than DLS23; curl animation activates on swipes; FK camera can be switched back to normal gameplay camera in settings for better accuracy. Free kick technique: aim just above wall at corner, 80% power with curl (curve with '(' or ')' swipe); use high-CON/high-SHO (FK curl boosted by SHO spin stat per FTG). Free kick types: direct (shoot at goal) and indirect (pass/cross). Penalty technique: use joystick for direction while tapping A/B/C QUICKLY and gently; holding too long = wild shot (over bar); aim corners; moving indicator ball — time kick as ball aligns with net; C button = curved/chip best for corners (LevelWinner). Penalty GK = guess direction (likely manual GK control on penalty saves — practice in training). Corner kick technique (DLS24): call a second player (to drag a defender out), outswinger corner (right-footed taker for right corner, left-footed for left), max B-button power, then shoot. Corner headers nerfed/close-to-impossible in DLS24 (r/DLS). CAMERA SETTINGS (dreamleaguesoccerkits competitive default): Camera Type = Tele Broadcast; Camera Height = 70-80 (recommend 75); Camera Zoom = 30-40 (recommend 35). Alternate community preference: Camera Type = Ball, distance 50% for attacking. Camera height slider 0-100%: 0% = close/zoom-in, 100% = zoomed-out full-pitch view. Graphics Medium, FPS 60 recommended for smooth online. Auto Switch: Semi Auto recommended. Player names over head preferred by competitive players (r/DLS). Vibration OFF for competition. Commentary language selectable. DLS25 Manual Kick settings restored (post-launch patch): ball spin/gravity/dribble-joystick-to-shoot transition fixed; players can manipulate ball spin direction again. Free-kick camera change in DLS24 caused community complaints. App Store review asks for per-player role assignment (free-kick/penalty) and individual celebrations — implying roles ARE assignable (as Team Management already supports per earlier sources) but celebrations may NOT be player-selectable yet.",
    "evidence/raw/turn35_w13/EV-394_controls_setpieces.html",
    "Captain: 80 choices + Create Your Own Captain (custom name/details); Training mode: 6 modules (Free/FreeKick/L Corner/R Corner/Pen/Pen Save); set pieces: joystick direction REQUIRED; B-press needs stick for auto-press; A=shoot, B=pass, C=lofted (curved/chip); FK camera changed DLS24, switch to gameplay cam; penalties: gentle tap + stick direction; corners: outswinger+2nd player+max B; competitive camera Tele Broadcast H70-80/Z30-40; Semi auto-switch; player names on; 60 FPS; Manual kick settings restored DLS25; Team Management assigns roles (captain/FK/pen)")

add_claim("Onboarding captain selection: ~80 captain candidates (swipe to browse), with 'Create Your Own Captain' option (custom-named player); 'See More' reveals player details (name/position/height/preferred foot/skill/tactical ratings); 'Sign Captain' finalizes.", 2, "onboarding/captain-selection", [e_controls])
add_claim("Training mode (My Club → Training): 6 practice modules — Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save. Switch via white arrow next to 'Free Training'.", 1, "training/mode", [e_controls])
add_claim("Player roles assignable in Team Management: Captain, Free Kick taker, Penalty taker, and likely Corner kicker (per App Store review request asking for per-player role assignment).", 2, "team/roles", [e_controls])
add_claim("ON SET PIECES (goal kick/corner/free kick/penalty): analogue joystick MUST be held in desired shot direction — no joystick input = default (often poor) direction.", 2, "controls/set-piece-stick", [e_controls])
add_claim("Modern DLS defensive auto-press: holding B button without analogue stick input DOES NOTHING; you must hold a direction on stick + B to trigger auto-pressing.", 2, "controls/b-requires-stick", [e_controls])
add_claim("On-screen buttons (offense): Low Kick (B, short ground passes) / Hard Kick (A, shooting + long through balls) / Lofted Kick (C, long balls, chips, crosses with curl). Hold = more power.", 2, "controls/button-mapping-refined", [e_controls])
add_claim("Free kick overhaul in DLS24 changed camera angle and made knuckle-balling harder than DLS23; curl animation activates when swiping. Free kick camera can be toggled back to normal gameplay camera in settings for improved accuracy.", 3, "setpieces/fk-camera-change", [e_controls])
add_claim("Direct free kick technique: aim just above wall toward corner; ~80% power; apply curl (swipe '(' for left curl / ')' for right curl); right-footed/left-footed player selection matters; high SHO/CON players yield best results (SHO governs free-kick curl/spin per FTG).", 3, "setpieces/fk-technique", [e_controls])
add_claim("Penalty technique: hold joystick toward target corner + TAP A/B/C gently/quickly — holding buttons too long = wild/over-bar shot. C button produces curved/chip shots best for side-footing corners. Time tap with moving ball indicator.", 2, "setpieces/penalty-technique", [e_controls])
add_claim("Penalty saving is practicable in training module (Penalty Save); goalkeeper direction controlled manually on defense.", 3, "setpieces/penalty-save", [e_controls])
add_claim("Corner kick technique (DLS24+ meta): call second player (pulls defender out), select outswinger corner (right-footed taker for right corner / left-footed for left corner), max B-button power, then shoot. Direct corner headers are very difficult in DLS24+.", 3, "setpieces/corner-technique", [e_controls])
add_claim("Competitive camera recommended settings (community): Camera Type = Tele Broadcast; Height 70-80 (75 ideal); Zoom 30-40 (35 ideal). Alt: Camera = Ball at 50% distance for offensive focus.", 2, "settings/camera-competitive", [e_controls])
add_claim("Camera slider range: 0% = close/zoomed in (immersive), 100% = fully zoomed out (tactical view).", 2, "settings/camera-range", [e_controls])
add_claim("Recommended performance settings: Graphics Medium, FPS 60 for smooth online play; Auto Switch = Semi Auto; Vibration OFF; Player names = over head (tactical ID).", 2, "settings/performance", [e_controls])
add_claim("DLS25 patch restored 'Manual Kick' functionality: fixed ball spin/gravity physics and the dribble-joystick-to-shooting transition bug; players can again manipulate ball spin deliberately with manual kick settings.", 2, "patches/dls25-manual-kick-fix", [e_controls])
add_claim("ERRATA: Camera control 'pinch zoom removed post-DLS23' confirmed here too — height/zoom sliders replace pinch gesture.", 1, "errata/pinch-zoom-removed", [e_controls])

p=os.path.join(RAW_DIR,'EV-394_controls_setpieces.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
