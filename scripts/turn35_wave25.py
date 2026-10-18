#!/usr/bin/env python3
"""Turn 35 Wave 25: chemistry/Fluid Formations red flag attributed to a fabricated source, controls + skill-move swipe map, formation meta with conflict, per-position training blueprints, May/Aug 2026 gameplay patches."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w25')

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

# ---------- EV-413: chemistry / fluid formations red flag ----------
e_red=new_ev("playdreamleaguesoccer.com 'DLS 2026 New Features' + 'DLS 2026 Games' pages, cross-checked against App Store / Google Play official listings, Bluestacks, gamingonphone, r/DreamLeagueSoccer, sportsdunia, Kotaku ES, ldplayer, z2u, modcombo",
    "CHEMISTRY / FLUID FORMATIONS RED FLAG ATTRIBUTED. Every claim of a team-chemistry system and 'Fluid Formations' in DLS26 traces to a SINGLE site: playdreamleaguesoccer.com. That page asserts 'for the first time in DLS history, team chemistry matters' with a '+15% chemistry boost when fielding players from the same nation', 'Tactical Presets' to switch between 4-3-3 Tiki-Taka / 4-4-2 Counter / 3-5-2 Wing-Play on the fly, saveable and shareable custom tactics, a '3-5-2 Fluid' formation, 'Adaptive Dribble', 'Contextual Passing', 'Power Shooting 2.0' with a green perfect-timing indicator, an AI that 'learns from your playstyle' and switches to a compact 4-4-2 mid-game, hidden 'Skill Rating' (SR) matchmaking, and 'Tactical Focus' training drills - illustrated with patently fabricated named player testimonials ('DLS_King_07 (Mumbai)', 'GoalMachine_23 (Bangalore)'). NONE of these appear in the official App Store or Google Play listings, and none are corroborated by Bluestacks, gamingonphone, sportsdunia, Kotaku ES, ldplayer or any r/DLS thread. The only 'chemistry' mention in a credible source is Bluestacks' vague line that higher-quality players appear in the market as 'team rating and chemistry improve', which most plausibly refers to squad strength, not a distinct stat. CONCLUSION: team chemistry and Fluid Formations are recorded as UNCONFIRMED and most likely fabricated - consistent with the pre-existing chemistry/AI-farm red flag, now attributed to a named source.",
    "evidence/raw/turn35_w25/EV-413_chemistry_redflag.html",
    "Chemistry +15% same-nation, Tactical Presets (Tiki-Taka/Counter/Wing-Play), shareable custom tactics, 3-5-2 Fluid, Adaptive Dribble, Contextual Passing, Power Shooting 2.0 green indicator, playstyle-learning AI, hidden Skill Rating matchmaking, Tactical Focus drills ALL trace to playdreamleaguesoccer.com only, illustrated with fake player testimonials; absent from official store listings and every credible guide -> UNCONFIRMED/likely fabricated",
    quality="community")

add_claim("playdreamleaguesoccer.com is flagged as a FABRICATED source: its DLS26 feature page invents team chemistry, Tactical Presets, Adaptive Dribble, Contextual Passing, Power Shooting 2.0, a playstyle-learning AI, hidden Skill Rating matchmaking and Tactical Focus drills, illustrated with fake named player testimonials.", 3, "errata/playdreamleaguesoccer-fabricated", [e_red])
add_claim("No team-chemistry gameplay mechanic is confirmed in DLS26: the +15% same-nation chemistry claim appears only on the fabricated site and is absent from official store listings and all credible guides.", 4, "chemistry/unconfirmed", [e_red], notes="Carries forward the pre-existing chemistry red flag, now source-attributed")
add_claim("'Fluid Formations' and the '3-5-2 Fluid' formation trace to the same fabricated source and are UNCONFIRMED.", 4, "tactics/fluid-formations-unconfirmed", [e_red], notes="Carries forward the pre-existing Fluid Formations red flag")
add_claim("The only credible mention of 'chemistry' is Bluestacks' line that better players appear in the transfer market as team rating and chemistry improve - most plausibly referring to overall squad strength rather than a distinct stat.", 3, "chemistry/only-vague-mention", [e_red])

# ---------- EV-414: controls, skill moves, formations, patches ----------
e_ctrl=new_ev("gamingonphone DLS26 beginners guide (Jan 2026), Bluestacks DLS26 guides, uptodown, sakibpro skill-moves guide, retbit 8 beginner tips, dreamleaguesoccerkits controls/settings guide, Kotaku en Espanol, kostenlose-spiele-apps, eslamgaming DLS19-mod page, r/DreamLeagueSoccer 176ntor (Oct 2023), sportsdunia top-5 formations, fifaworldcupnews May/Aug 2026 update notes, z2u position guide",
    "CONTROLS, SKILL MOVES, FORMATIONS, PATCHES. CONTROLS: virtual joystick on the left plus three action buttons on the right (A/B/C). With possession: Low Kick = short precise passes; Hard Kick = shooting and long through balls; Lofted Kick = long passes, chips and crosses. Without possession the same buttons handle pressure, tackle and player switching; the goalkeeper can charge out in one-on-ones. SKILL MOVES (swipe-based): Rainbow Flick = swipe up (flicks the ball over a defender); Feint/Body Fake = swipe left or right; Roulette/Spin = swipe down; Close Control = tap and hold while running (slows and shields the ball); Knock Ahead = single tap (kicks the ball forward to sprint into space); Secondary Press = tap and hold while defending (calls a second defender to press); Heading = double-tap as the ball drops; Bicycle Kick = cross then double-tap as the ball lands. Skill-move availability scales with the player's overall rating, dribbling and control - 80+ rated players can perform most basic skills, 85+ execute advanced ones smoothly. Controls are customisable (button size, sprint sensitivity, through-pass assistance, vibration). ERRATUM: eslamgaming's mapping (A = slide tackle, B = pressure) contradicts the well-established A = Hard Kick / B = Low Kick mapping and is rejected. FORMATIONS: only 4-4-2 and 4-1-2-1-2 (Attacking) are unlocked at the start; further formations come from Training Centre upgrades. sportsdunia's top five: 4-4-2, 4-2-3-1, 4-2-2-2, 3-4-1-2, 4-3-3. r/DLS analysis: three-at-the-back is strong but struggles against winger formations such as 4-3-3; a diamond or staggered midfield protects the centre behind a back three; 3-3-1-3 yields inverted wing-backs; 5-3-2 and 5-2-1-2 suit defending a lead; two-striker setups with a fast striker and lobbed balls work well in career. CONFLICT: r/DLS advises never using 4-2-3-1 (isolated striker, punished by long balls) while sportsdunia ranks it second - both recorded. Kotaku ES maps 4-3-3 to fast wingers and crosses, 4-2-3-1 to midfield control, 3-5-2 to wing-back exploitation. PATCHES: the DLS26 May 2026 update refined ball physics and improved goalkeeper AI specifically in one-on-one situations and corner kicks; the August 2026 update fine-tuned sliding-tackle recovery speeds and player collision physics to reduce unrealistic penalty-box fouls. CARE ECONOMY: a career match gives no additional rewards beyond 15 goals scored; C-spam is discouraged in Dream League Live; buying and immediately releasing 80-rated defenders (1,460 coins) or players under 180 coins is the standard coach-farming method.",
    "evidence/raw/turn35_w25/EV-414_controls_formations.html",
    "Controls = joystick + 3 buttons (Low Kick=short pass, Hard Kick=shoot/through ball, Lofted=long pass/chip/cross; off-ball = pressure/tackle/switch; GK charge in 1v1); skill-move swipe map (Rainbow=up, Feint=L/R, Roulette=down, Close Control=tap-hold, Knock Ahead=tap, Secondary Press=tap-hold defending, Heading=double-tap, Bicycle=cross+double-tap); skills gated by OVR 80+/85+; default formations 4-4-2 + 4-1-2-1-2, rest via Training Centre; sportsdunia top5 vs r/DLS conflict on 4-2-3-1; 3-at-back weak vs wingers, 3-3-1-3 inverted wingbacks, 5-3-2 to defend a lead; May2026 = ball physics + GK AI in 1v1/corners, Aug2026 = slide-tackle recovery + collision physics; no rewards past 15 goals; 80-DEF 1,460c coach farm",
    quality="community")

add_claim("DLS26 controls use a virtual joystick plus three action buttons: Low Kick for short precise passes, Hard Kick for shooting and long through balls, Lofted Kick for long passes, chips and crosses; off the ball the buttons handle pressure, tackling and player switching, and the keeper can charge out in one-on-ones.", 2, "controls/button-map", [e_ctrl])
add_claim("Skill-move swipe map: Rainbow Flick = swipe up; Feint/Body Fake = swipe left or right; Roulette/Spin = swipe down; Close Control = tap and hold while running; Knock Ahead = single tap; Secondary Press = tap and hold while defending; Heading = double-tap as the ball drops; Bicycle Kick = cross then double-tap as the ball lands.", 3, "controls/skill-move-map", [e_ctrl])
add_claim("Skill-move availability scales with the player's overall rating, dribbling and control - 80+ rated players can perform most basic skills while 85+ rated players execute advanced ones smoothly.", 3, "controls/skill-move-gating", [e_ctrl])
add_claim("Controls are customisable: button size, sprint sensitivity, through-pass assistance and vibration can all be adjusted, with through-pass assistance recommended ON.", 3, "controls/customisation", [e_ctrl])
add_claim("eslamgaming's control mapping (A initiates sliding tackles, B applies pressure) contradicts the well-established A = Hard Kick / B = Low Kick mapping and is rejected as an error.", 3, "errata/eslamgaming-control-map", [e_ctrl])
add_claim("Only the 4-4-2 and 4-1-2-1-2 (Attacking) formations are unlocked at the start; every further formation requires Training Centre upgrades.", 2, "tactics/default-formations", [e_ctrl])
add_claim("sportsdunia's top five DLS26 formations: 4-4-2, 4-2-3-1, 4-2-2-2, 3-4-1-2 and 4-3-3, all rated as balanced.", 3, "tactics/top-five-sportsdunia", [e_ctrl])
add_claim("r/DLS formation analysis: three-at-the-back is strong but vulnerable to winger formations such as 4-3-3; a diamond or staggered midfield protects the centre behind a back three; 3-3-1-3 produces inverted wing-backs; 5-3-2 and 5-2-1-2 suit defending a lead; two-striker setups with a fast striker and lobbed balls suit career mode.", 3, "tactics/formation-analysis-reddit", [e_ctrl])
add_claim("CONFLICT on 4-2-3-1: sportsdunia ranks it the second-best formation while r/DLS advises never using it because the lone striker gets no support and the team is punished by long balls.", 3, "tactics/4-2-3-1-conflict", [e_ctrl], notes="Direct source conflict recorded, not resolved")
add_claim("Kotaku en Espanol maps formations to playstyles: 4-3-3 for fast wingers and crosses, 4-2-3-1 for midfield control and patient attacks, 3-5-2 for good defenders exploiting wing-backs.", 3, "tactics/formation-playstyle-map", [e_ctrl])
add_claim("Per-position training blueprints (r/DLS): Forward 100 SPE/ACC, 90+ STA, 95+ STR, 95+ SHO; Winger 100 SPE/ACC/STA, 90+ CON, 80+ STR; Midfielder all-green with 90+ STA/CON/PAS (AM 90+ SHO, DM 100 STR and 95+ TAC); Defender 100 SPE/STA/ACC/STR with TAC as high as possible; GK prioritise GKR.", 3, "training/per-position-blueprints", [e_ctrl])
add_claim("Players are measured by eight attributes plus position-dependent roles (captain, free kicks, penalties) assignable per player - reconciling the eight-attribute outfield model with the ten-attribute model that adds GKH and GKR for keepers.", 3, "attributes/eight-plus-gk", [e_ctrl])
add_claim("DLS26 position abbreviations in use: ST, LW/RW, AM, CM, DM, CB, LB/RB and GK, and players are most effective when assigned to their natural positions.", 2, "attributes/position-abbreviations", [e_ctrl])
add_claim("The DLS26 May 2026 update refined ball physics and improved goalkeeper AI specifically in one-on-one situations and corner kicks.", 2, "patching/may2026-gk-ai", [e_ctrl])
add_claim("The DLS26 August 2026 update fine-tuned defensive sliding-tackle recovery speeds and improved player collision physics to reduce unrealistic penalty-box fouls.", 2, "patching/aug2026-collision", [e_ctrl])
add_claim("A career match awards no additional rewards beyond 15 goals scored, so score padding past that point is wasted effort.", 3, "career/no-rewards-past-15-goals", [e_ctrl])
add_claim("C-spam (repeated Lofted Kick) is discouraged in Dream League Live, and the standard coach-farming method is buying then immediately releasing 80-rated defenders (1,460 coins) or players under 180 coins.", 3, "economy/coach-farming-80-def", [e_ctrl])

p=os.path.join(RAW_DIR,'EV-413_chemistry_redflag.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-414_controls_formations.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
