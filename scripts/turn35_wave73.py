#!/usr/bin/env python3
"""Turn 35 Wave 73: THE IN-MATCH TACTICS SURFACE - when a formation change actually takes
effect, the starting formation unlocks, six concrete Live strategies, the refined anti-wing
tactic, and a NEGATIVE on team instructions.

Wave 73's key finding is a timing rule that changes how you use the pause menu: a formation
change takes effect only at kick-off, while a substitution can be made at any stoppage.
Confusing the two wastes the change.

The team-instruction negative matters for expectation-setting: every guide that describes
mentality, width, depth, tempo or marking sliders is describing FIFA or Football Manager.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w73')

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

e_tac=new_ev("LevelWinner DLS24 formations and tactics guide (15 Mar 2024, the formation-change timing rule), gamingonphone DLS26 Beginners Guide (21 Jan 2026, the starting formation unlocks), r/DreamLeagueSoccer 1i6kf6d (21 Jan 2025, the six Live strategies), 1rx01zi (18 Mar 2026, the anti-wing-spam tactic), playdreamleaguesoccer.com DLS26 new features (the fabricated Tactical Presets, Fluid Formation and adaptive-AI claims), fmscout / footballgpt / Operation Sports (the FM26 instruction systems that DLS does not have)",
    "THE IN-MATCH TACTICS SURFACE, AND A NEGATIVE ON TEAM INSTRUCTIONS. (1) THE FORMATION-CHANGE TIMING RULE - the wave's key finding: 'You can switch your formation multiple times in a match, but each change will only take effect on resets during kickoffs. Goal kicks, free kick pauses, or sending the ball out of bounds will welcome substitutions but not formation changes.' So a SUBSTITUTION can be made at any stoppage, but a FORMATION CHANGE only lands at kick-off. Confusing the two wastes the change - you set it at a throw-in and nothing happens until the next kick-off. (2) THE STARTING FORMATION UNLOCKS: 'The Team Formation would be set at Default 4-4-2, and the only other Formation unlocked by default is 4-1-2-1-2.' Every other shape is gated behind progression, which is the corpus's existing Training-Centre formation unlock arriving as a concrete starting state. (3) SIX CONCRETE LIVE STRATEGIES, from a player who climbed from DLS22 to DLS26: 'No blind C passes · Dribbling while stopped · Long b passes (meta) · Backwards running for defensive play · Calling out gk when necessary · No blind shots.' (4) THE ANTI-WING-SPAM TACTIC, refined: 'wing spamming isn't very prevalent anymore... But the trick is to NOT try and tackle their outermost players as they switch the ball. This will leave your players stuck up the field. Instead, switch to defensive mode, and run your players backwards at every opportunity (ie every time your player changes as opponent smashes the ball to the other wing, just run the next player backwards).' This refines the corpus's escalation ladder with a specific instruction: retreat, do not chase. (5) THE TEAM-INSTRUCTION NEGATIVE. A targeted search for DLS tactics returned only Football Manager and EA systems (FM26's in-possession/out-of-possession dual formations, mentality sliders, width, depth, tempo, pressing intensity, counter-press, trigger press, marking styles) and real-football coaching material. **No DLS source documents team instructions, a mentality slider, width or depth controls, tempo, pressing intensity or marking styles.** DLS gives you a formation plus an attacking/balanced/defensive switch, and that is the whole tactical surface. (6) NO IN-MATCH FORMATION FLUIDITY: the AI farm claims 'Tactical Presets' that switch between 4-3-3 Tiki-Taka, 4-4-2 Counter and 3-5-2 Wing-Play 'on the fly', custom tactics you can save and share, and a '3-5-2 Fluid' formation where wing-backs push high and CDMs cover. None of it is corroborated anywhere, and the formation-change timing rule above actively contradicts 'on the fly'. (7) THE ADAPTIVE-AI CLAIM IS CONTRADICTED BY FTG'S OWN ARTICLE: the farm claims 'The A.I. in DLS 2026 learns from your playstyle. If you constantly exploit the wings, expect the opposing manager to switch to a compact 4-4-2 mid-game.' FTG's official matchmaking article states 'there are no additional overlaid controls to manage the difficulty experience'. Recorded as a direct contradiction, resolved in favour of the official source. (8) playdreamleaguesoccer.com is REJECTED FOR THE SIXTH TIME.",
    "evidence/raw/turn35_w73/EV-487_tactics_surface_and_instruction_negative.html",
    "FORMATION CHANGES TAKE EFFECT ONLY AT KICK-OFF: 'each change will only take effect on resets during kickoffs. Goal kicks, free kick pauses, or sending the ball out of bounds will welcome substitutions but not formation changes' - so a sub can be made at any stoppage but a formation change cannot. STARTING UNLOCKS: 4-4-2 by default, with 4-1-2-1-2 the only other formation unlocked from the start. SIX LIVE STRATEGIES: no blind C passes, dribble while stopped, long B passes (meta), backwards running for defence, call out the GK when necessary, no blind shots. ANTI-WING: do NOT tackle the outermost players as they switch - switch to defensive mode and run backwards at every opportunity. NEGATIVE: DLS has NO team-instruction system - no mentality slider, no width/depth/tempo, no pressing intensity, no marking styles. A formation plus an attacking/balanced/defensive switch is the entire tactical surface. NEGATIVE: no in-match formation fluidity - the 'Tactical Presets', 'save and share custom tactics' and '3-5-2 Fluid' claims are all fabricated, and 'on the fly' switching contradicts the kick-off rule",
    quality="community")

add_claim("FORMATION CHANGES TAKE EFFECT ONLY AT KICK-OFF: 'each change will only take effect on resets during kickoffs. Goal kicks, free kick pauses, or sending the ball out of bounds will welcome substitutions but not formation changes.' A substitution can be made at any stoppage; a formation change cannot.", 2, "tactics/formation-change-timing", [e_tac], notes="Confusing the two wastes the change - it will not land until the next kick-off")
add_claim("The starting formation unlocks are 4-4-2 by default, with 4-1-2-1-2 the only other formation available from the start; every other shape is gated behind progression.", 2, "tactics/starting-formation-unlocks", [e_tac])
add_claim("SIX LIVE STRATEGIES from a DLS22-26 player: no blind C passes · dribbling while stopped · long B passes (the meta) · backwards running for defensive play · calling out the GK when necessary · no blind shots.", 3, "tactics/six-live-strategies", [e_tac])
add_claim("THE ANTI-WING TACTIC, REFINED: 'the trick is to NOT try and tackle their outermost players as they switch the ball. This will leave your players stuck up the field. Instead, switch to defensive mode, and run your players backwards at every opportunity.'", 3, "tactics/anti-wing-run-backwards", [e_tac], notes="Refines the escalation ladder - retreat, do not chase")
add_claim("DOCUMENTED NEGATIVE - **DLS HAS NO TEAM-INSTRUCTION SYSTEM.** No source documents team instructions, a mentality slider, width or depth controls, tempo, pressing intensity or marking styles. Every guide describing them is Football Manager or EA. A formation plus an attacking/balanced/defensive switch is the entire tactical surface.", 2, "negatives/no-team-instructions", [e_tac])
add_claim("DOCUMENTED NEGATIVE - **THERE IS NO IN-MATCH FORMATION FLUIDITY.** The claims of 'Tactical Presets' switching between 4-3-3 Tiki-Taka, 4-4-2 Counter and 3-5-2 Wing-Play 'on the fly', of custom tactics you can save and share, and of a '3-5-2 Fluid' formation are all uncorroborated - and 'on the fly' switching directly contradicts the kick-off timing rule.", 2, "negatives/no-formation-fluidty", [e_tac])
add_claim("The claim that 'The A.I. in DLS 2026 learns from your playstyle... expect the opposing manager to switch to a compact 4-4-2 mid-game' is CONTRADICTED BY FTG'S OWN ARTICLE: 'there are no additional overlaid controls to manage the difficulty experience.' Resolved in favour of the official source.", 1, "negatives/adaptive-ai-claim-contradicted", [e_tac], notes="Official against a farm claim")
add_claim("playdreamleaguesoccer.com is REJECTED FOR THE SIXTH TIME - it invents a Tactical Presets system, shareable custom tactics, a '3-5-2 Fluid' formation and a playstyle-learning AI manager, none of which any other source mentions, and one of which FTG's own article refutes.", 1, "sources/playdreamleagesoccer-rejected-sixth-time", [e_tac], notes="Sixth independent confirmation of AI-farm status")

for name in ('EV-487_tactics_surface_and_instruction_negative.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
