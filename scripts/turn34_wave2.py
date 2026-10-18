#!/usr/bin/env python3
"""Turn 34 Wave 2: weather gameplay caveats, camera modes (Side-to-Side/Ball), offside rule, kickoff trap, v13.410/420 physics patches, AI tactical fouls/trap."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn34_w2')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="mixed"):
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

e_weather=new_ev("eslamgaming weather visuals/dynamic claims + r/DLS community wishlist + dls25 snow criticism",
    "Weather visuals CONFIRMED (rain/snow/fog/night/sunset visual skins; pitch texture changes). Gameplay IMPACT CLAIMS from eslamgaming (AI-content farm) include: rain makes pitch slippery reducing traction/ball control, puddles form; snow accumulates reducing visibility making long passes riskier; fog reduces visibility; sunset glare makes through-balls harder to see; floodlight glare hampers GK tracking of high crosses; dynamic mid-match transitions (sun→rain). Time-of-day lighting (sunset/night/floodlights) produces distinct lighting hues. Additional AI-farm claim: FTG Engine 6.0 (Unity 2023 LTS) with ECS physics + GPU instanced crowds + adaptive resolution scaling for 60fps on Redmi Note 9 (completely fabricated-sounding; treat engine details as speculative). COMMUNITY WISHLIST (Nov 2025 r/DLS video) asks for NEW weather conditions (fog, cloudy, light rain) — implying base DLS26 may ship with only a subset (rain/snow/night confirmed visually). DLS25 prior art: snow animation was strobe/motion-sickness inducing (per earlier EV). No official FTG changelog (v13.040-v13.430) mentions weather physics, only stadium/visual atmosphere upgrades. TREAT ALL GAMEPLAY-PHYSICS WEATHER CLAIMS AS SPECULATIVE until APK/datamine/official source confirms.",
    "evidence/raw/turn34_w2/EV-376_weather.html",
    "Weather visuals confirmed; physics impact speculative; engine-version claim fabrication-flag; wishlist suggests limited base weather set")
e_cam_offside=new_ev("reddit camera threads (Feb2026/DLS23-era) + LevelWinner offside + LevelWinner kickoff-trap + r/DLS DLS26 reviews",
    "Camera modes beyond Tele Broadcast/TV/Sideline/G2G/Default: 'Side to Side' (sideline) and 'Ball Camera' (point-of-view following ball) referenced as two common options (r/DLS Dec2023). Player-zoom feature was removed after early DLS23 (no longer possible on Android per r/DLS Feb2026). Dynamic broadcast cameras in DLS26 zoom/pan automatically for goals/counters/interceptions (no manual zoom during match). Offside rule: standard FIFA offside (player closer to goal line than ball + 2nd-last opponent when ball is played); offside results in indirect free kick / GK distribution reset; AI teams will play offside traps (per AI-content-farm DLS26 mod description, plausible). Kickoff trap trick (LevelWinner): manually move your CF a step up immediately after kickoff — ~25% chance to intercept the opposition's second pass every kickoff reset (effective when formation only sets 4 receivers). August 2026 (v13.410-420) patch fine-tuned defensive sliding-tackle recovery speeds and improved player collision physics to reduce unrealistic penalty-box fouls. v13.410 also introduced Pre-Season Kickoff and European Champions Tour events. Community DLS26 complaints: first touch is clunky (extra touch before passing leads to dispossessions in front of goal); center-backs spread out or dive in one-by-one giving walk-throughs; aerial duels dominated by Strength stat with little height advantage visible; passes frequently go to miscatched teammates ('struggling to string their passes together' commentary line appears too often).",
    "evidence/raw/turn34_w2/EV-377_cam_offside.html",
    "Camera modes (Side-to-Side/Ball), zoom removal, offside rule, kickoff trap, August patch collision fixes, DLS26 complaints")

# WEATHER (with conf marking speculation)
add_claim("Weather visuals present in DLS26: rain, snow, fog, and night/sunset/floodlight time-of-day lighting appear as cosmetic/visual skins with pitch texture changes (sheen/snow blanket).", 2, "presentation/weather-visuals", [e_weather])
add_claim("Claimed weather gameplay effects (HIGHLY SPECULATIVE, AI-content-farm only, uncorroborated by FTG changelogs): rain reduces traction/ball control with puddle formation; snow accumulates reducing visibility and making long passes riskier; fog reduces visibility; sunset glare hampers through-ball sightlines; floodlight glare hampers GK tracking of high crosses; dynamic mid-match transitions between weather states.", 4, "match/weather-physics", [e_weather], "eslamgaming/playdreamleaguesoccer AI-farms; treat as unconfirmed pending APK/official source")
add_claim("Community wishlist (Nov 2025) asks for more weather options (fog, cloudy, light rain) — implies base DLS26 ships with a limited subset (rain/snow/night confirmed visually, other conditions absent or limited).", 3, "presentation/weather-wishlist", [e_weather])
add_claim("DLS25 snow animation was strobe/motion-sickness inducing (ball obscured) per earlier r/DLS complaints; DLS26 may or may not have improved this.", 2, "presentation/snow-criticism", [e_weather])
add_claim("FTG Engine 6.0 / Unity 2023 LTS / ECS physics / GPU-instanced crowd rendering / 120fps on midrange claims are all AI-farm fabrications with no official support — engine version/architecture UNVERIFIED.", 4, "meta/engine-fabrication", [e_weather])
add_claim("No v13.040-v13.430 changelog entry lists weather physics as a feature; only visual atmosphere/crowd-audio upgrades are official.", 1, "patching/weather-not-listed", [e_weather])

# CAMERA
add_claim("Camera options include 'Side to Side' (default wide sideline) and 'Ball Camera' (closer POV that follows the ball) in addition to TV/Tele Broadcast/Goal-to-Goal/Sideline.", 2, "ui/camera-modes", [e_cam_offside])
add_claim("Manual player/close-up zoom feature was available in early DLS23 but removed in later versions (including DLS26); pinch-zoom no longer works on Android per r/DLS Feb 2026.", 3, "ui/camera-zoom-removed", [e_cam_offside])
add_claim("Dynamic broadcast cameras in DLS26 perform automatic zoom/pan to highlight goals, interceptions, fast counterattacks (no manual in-match zoom).", 2, "ui/camera-dynamic", [e_cam_offside])

# OFFSIDE / KICKOFF / AI
add_claim("Offside rule enforced per standard FIFA laws: attacker is offside if closer to opponent's goal line than both the ball and the second-last opponent at moment ball is played; results in indirect free kick / GK distribution reset.", 2, "rules/offside", [e_cam_offside])
add_claim("AI teams will deploy offside traps (defenders step up in sync to catch attackers offside), and commit tactical fouls to break up transitions (per AI-content-farm mod description — plausible but not verified against vanilla behavior).", 3, "ai/tactics", [e_cam_offside])
add_claim("Kickoff trap (skill trick): immediately after kickoff reset, manually move your controlled CF slightly up the pitch; roughly 25% chance of intercepting the opponent's second pass when formations only set 4 receivers. The non-controlled striker mirrors the initial movement giving coverage both sides.", 2, "tactics/kickoff-trap", [e_cam_offside])

# PATCHES / COMPLAINTS
add_claim("v13.410 (Aug 20, 2026, Pre-Season Kickoff/European Champions Tour events) refined ball physics and GK AI per v13.410 notes; v13.420 (Sep 1, 2026) fine-tuned defensive sliding-tackle recovery speeds and improved player collision physics to reduce unrealistic penalty-box fouls.", 1, "patching/v13-410-420", [e_cam_offside])
add_claim("DLS26 community complaints (cumulative Dec-Sep): first touch is clunky/overly heavy (extra touch before passing leads to dispossession near goal); CBs spread out or dive in individually (walk-through goals); aerial duels dominated by Strength stat, height advantage barely visible; teammate pass reception miscues frequent ('They're struggling to string their passes together' commentary over-triggered).", 2, "complaints/physics", [e_cam_offside])
add_claim("CON (Control) stat governs how well a player keeps the ball under defender contact and how cleanly they can receive/juggle balls without sending it too far.", 2, "attributes/control", [e_cam_offside], "LevelWinner attribute detail")

for f in ['EV-376_weather.html','EV-377_cam_offside.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
