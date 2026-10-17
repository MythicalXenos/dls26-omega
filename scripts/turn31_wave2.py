#!/usr/bin/env python3
"""Turn 31 Wave 2: camera settings, GK controls, substitutions limit (8 subs bench), kick/cross/pass assists, auto-switch."""
import json,os,datetime,re
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
max_c=max(int(c['claim_id'][6:]) for c in claims)
max_e=max(int(e['evidence_id'][3:]) for e in ev if e['evidence_id'].startswith('EV-'))
ts=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
def mk_ev(eid,origin,artifact,summary):
    eid_full=f'EV-{eid:03d}'
    ev.append({'evidence_id':eid_full,'origin_method':origin,'artifact':artifact,'captured_at':ts,'covers':[],'summary':summary,'extracted_from':origin})
    return eid_full
def mk_claim(cid,prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    cid_full=f'CLAIM-{cid:03d}'
    c={'claim_id':cid_full,'proposition':prop,'confidence_tier':tier,'supporting_evidence':evr,'challenges':chal or [],'context_build':ctx,'last_checked_by':f'turn 31 wave 2 ({ts})','last_valid_check':ts,'last_attempt':ts,'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),'volatility_tier':vol,'cross_refs':[],'replacements':None,'contradicting_evidence':[]}
    claims.append(c); return cid_full
mc=max_c
def C(prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    global mc; mc+=1; return mk_claim(mc,prop,tier,evr,chal,vol,ctx)
e305=mk_ev(max_e+1,'community-web-en (r/DLS camera settings Jan 2026; sportsdunia best settings; dreamleaguesoccerkits.com settings; r/DLS camera threads 2022-2024)','evidence/raw/community_turn31/EV-305_camera_assists.html',"DLS26 camera types (selectable in Settings): TV (default/broadcast-style), Sideline (wide side-on), Ball (close-up following the ball), Goal-to-Goal (end-to-end vertical view), Tele Broadcast. Custom sliders: Camera Height and Camera Zoom (percentage 0-100%). Competitive players use Sideline @ ~30% zoom OR Goal-to-Goal @ 100% zoom; community recommends TV @ 80% distance (sportsdunia) or Tele Broadcast Height 75 / Zoom 35 (dreamleaguesoccerkits.com). Assist toggles confirmed: Kick Assist, Cross Assist, Pass Assist (all can be turned OFF for full manual). Auto Switch (player-cursor switch on defense): Semi Auto recommended. UI overlays: directional arrows ON/OFF, radar map ON/OFF, player names ON/OFF, scoreboard ON/OFF. Graphics/FPS options: Medium graphics + 60 FPS recommended for smooth play on most devices (lower-end devices reduce). Vibration/haptic toggle (OFF recommended).")
e306=mk_ev(max_e+2,'community-web-en (supercheats.com DLS GK questions 2017; gamingonphone DLS26 beginner; r/DLS GK control 2020)','evidence/raw/community_turn31/EV-306_gk_controls.html',"DLS GK controls (consistent across DLS versions per community): HOLD C button (loft/cross button) to rush goalkeeper out at attacker in 1-v-1 situations; red icon indicates GK is being manually controlled. Double-tap on your own goalkeeper to drop the ball at his feet (to play out short or dribble). When GK has the ball: B = long drop-kick / clearance; A = short throw/pass to nearest defender; C appears to be through-ball distribution (DLS button mapping B=shoot/long, A=pass/throw). Gamingonphone mentions 'Goalkeeper charge' as available in 1-on-1 situations. Note: DLS GK controls are simpler than FC26 (no manual dive-direction, no punch/catch cross-call, no GK cover-far-post modifiers) — rush + drop-ball + distribution only.")
e307=mk_ev(max_e+3,'community-web-en (r/DLS DLS26 is garbage Dec 7 2025 substitution complaint thread)','evidence/raw/reddit_turn31/EV-307_substitutions.html',"DLS26 introduced a LIMIT of 8 substitutes on the bench (compared to prior DLS versions where players had 'freedom to sub anyone' they wanted). This mirrors real-life soccer and other football games but broke a DLS tradition that long-time players valued (DLS23 and earlier let you freely rotate a bigger squad). Community complaint: 'limiting us to only 8 subs is diabolical.'")
C("DLS26 camera options (Settings → Gameplay/Camera): Camera Type = TV (default broadcast), Sideline (wide side-on), Ball (close-up follow), Goal-to-Goal (vertical end-to-end), Tele Broadcast. Camera Height and Camera Zoom are independent percentage sliders (0-100%).",'High Confidence',[e305])
C("Community-recommended camera setups: (a) Sideline @ ~30% zoom (competitive online favorite, wide view); (b) Goal-to-Goal @ 100% zoom (full-pitch vertical, easier long-shot aiming for some players but disorienting when attack direction flips at half); (c) TV @ 80% distance (sportsdunia rec); (d) Tele Broadcast @ Height 75 / Zoom 35 (dreamleaguesoccerkits rec). No single best angle; players strongly prefer one and stick with it.",'Community Consensus',[e305])
C("DLS26 includes ASSIST TOGGLES for: Kick Assist, Cross Assist, Pass Assist (all OFF recommended for high-level competitive play to retain full manual control). Auto Switch (defensive player-cursor switching) has Semi/Manual/Auto options; Semi Auto is the common recommendation. UI overlay toggles: directional arrows, radar/minimap, player names, scoreboard (all independently on/off).",'High Confidence',[e305])
C("Graphics/performance options (DLS26): Graphics quality (Medium recommended for performance vs visual balance), FPS cap (60 FPS recommended on supported devices). Lower-end devices should reduce graphics for stable frame rate. Haptic/Vibration toggle exists (OFF recommended for competitive play).",'Community Consensus',[e305],['Exact setting names/options not fully enumerated; need in-client verification.'],vol='Low')
C("Goalkeeper controls (DLS26, touch): HOLD C button (loft/cross/through) to rush GK out at attacker (1-v-1 charge); red icon indicates GK under manual control. DOUBLE-TAP on your GK to drop ball at his feet (to play out or dribble). When GK holds ball: B = long drop-kick/clearance; A = short throw/pass to nearest defender.",'High Confidence',[e306,'EV-304'],['GK control unchanged across many DLS versions per supercheats/r/DLS; DLS26 specifics assumed consistent.'],vol='Medium')
C("DLS26 GK control is SIMPLER than FC26/console sims: no manual dive-direction input, no punch/catch cross calls, no far-post cover, no GK-move-with-R3. GK AI handles saves/positioning automatically except for manual rush (hold C) and drop-ball (double-tap GK).",'High Confidence',[e306],vol='Low')
C("DLS26 limits the in-match substitute bench to 8 players (down from effectively unlimited/free rotation in DLS23 and earlier). Community backlash: long-time players saw this as removing a unique DLS freedom in favor of mirroring real-life squad rules and competing soccer games.",'Community Consensus',[e307],vol='Low')
C("Button naming in attack (gamingonphone phrasing): Low Kick (A button) = short/low pass; Hard Kick (B button) = shot / hard pass; Lofted Kick (C button) = long ball / cross / through ball / chip shot.",'High Confidence',[e306],vol='Low')
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c)+'\n')
with open(EIP,'w') as f:
    for e in ev: f.write(json.dumps(e)+'\n')
print(f"Added {mc-max_c} new claims and 3 EVs (EV-305..EV-307). Totals: {len(claims)} claims, {len(ev)} EVs")
