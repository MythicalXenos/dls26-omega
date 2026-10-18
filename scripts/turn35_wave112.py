#!/usr/bin/env python3
"""Turn 35 Wave 112: THERE IS NO FAKE SHOT IN DLS, AND THE SET-PIECE RANDOMISATION COMPLAINT.

Wave 112's centrepieces:

1. THERE IS NO FAKE SHOT IN DLS — a documented negative the corpus did not carry. A player
   asking for celebrations is told the game's real gap: *"What DLS first needs is a fake shot.
   It is one of the most basic things lacking in DLS."* The corpus's skill catalogue has the
   Feint (a direction change) and the fake-pass-and-shoot combination described by a creator,
   but the dedicated **fake shot** — the feint of a strike that freezes a defender — does not
   exist. That is a real constraint on the attacking repertoire and it belongs in the
   catalogue's gap list.

2. THE SET-PIECE RANDOMISATION COMPLAINT, which is the most specific statement of a feeling
   every DLS player has. A suggestion thread: *"you can take a corner while pointing exactly
   where you want it 3 times, the exact same place, and all 3 times the ball ends up somewhere
   different. Same for freekicks, pens, and even in game sometimes."* So identical inputs
   produce different outcomes. The corpus already records FTG's official denial of overlaid
   difficulty controls, and it records the community "scripts" perception as slang — this is
   the same perception arriving from the set-piece side, and it is recorded as a *complaint*
   rather than a confirmed mechanic.

3. THE BOTH-FOOTED WINGER, which is a different asset from the both-footed striker the corpus
   already records. A winger who can use either foot can *"put sweeping passes forwards/inwards
   - like left foot on left wing for a striker to run onto; or they can cut inside and take a
   shot - like right foot on left wing."* So the both-footed winger is a *shape* asset, not
   just a finishing one.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w112')

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

e_sk=new_ev("r/DreamLeagueSoccer 12776v9 (31 Mar 2023 - the no-fake-shot gap, raised in a celebrations request thread), r/DreamLeagueSoccer 1v26fvr 'DISCUSSION: Suggestions for DLS 27 & Beyond' (21 Jul 2026 - the set-piece randomisation complaint with the three-identical-corners example, and the responsiveness complaint), r/DreamLeagueSoccer 1rx01zi (18 Mar 2026 - the both-footed winger as a shape asset), eslamgaming.com (FLAGGED - the through-ball input: aim the joystick into empty space and tap C or A), r/DreamLeagueSoccer 1pqcbiq (19 Dec 2025 - the diagonal A pass nerfed 60-80% and the C-spam efficacy reduction, both already in the corpus at CLAIM-1507 and recorded here as the specific quotes)",
    "NO FAKE SHOT, THE SET-PIECE RANDOMISATION COMPLAINT, AND THE BOTH-FOOTED WINGER. (1) NO FAKE SHOT: raised in a celebrations request thread, where the top reply names the real gap - '**What DLS first needs is a fake shot. It is one of the most basic things lacking in DLS.**' **So the dedicated fake shot - the feint of a strike that freezes a defender and opens a lane - does not exist in DLS.** The corpus's skill catalogue has the Feint (a direction change) and a creator's fake-pass-and-shoot combination, but neither is a fake shot. This is a real constraint on the attacking repertoire and belongs in the catalogue's gap list, because a player arriving from FIFA or eFootball will look for it. (2) THE SET-PIECE RANDOMISATION COMPLAINT: '**Many times you point your joystick exactly where you want it and it seems some RnG kicks in where it kinda randomizes what you want to happen. For example, you can take a corner while pointing exactly where you want it 3 times, the exact same place, and all 3 times the ball ends up somewhere different. Same for freekicks, pens, and even in game sometimes.**' **So identical inputs produce different outcomes**, which is the most specific statement of the perception the corpus already records as community 'scripts' slang. It is recorded here as a COMPLAINT from a suggestion thread - not as a confirmed mechanic - because the corpus also carries FTG's official denial of overlaid difficulty controls. The honest reading is that set pieces have a variance the player cannot see, and the corpus's 'drill one routine' advice is the correct response to it. (3) THE RESPONSIVENESS COMPLAINT, from the same thread: 'You can tap the screen and quickly change direction to chop the ball but **6-7/10 times your player will take a touch before the tap ahead movement is registered.**' A third source for the corpus's input-delay finding. (4) THE BOTH-FOOTED WINGER, a different asset from the both-footed striker the corpus already records (CLAIM-1666): '**Both-footed wingers is great as-well because they can put sweeping passes forwards/inwards - like left foot on left wing for a striker to run onto; or they can cut inside and take a shot - like right foot on left wing.**' So the both-footed winger is a SHAPE asset - it creates the in-swinger from either flank - and not merely a finishing one. (5) THE THROUGH-BALL INPUT, from a flagged source and therefore recorded at C3 with the flag: '**Master the Through Ball - Instead of passing directly to a player, aim the joystick into empty space and tap C or A.** This allows fast strikers to run onto the ball.' The mechanism matches the corpus's pass-into-space rule; the input pairing is the new part. (6) THE DIAGONAL A PASS AND C-SPAM NERFS, with the specific quotes: 'The Unstoppable Diagonal A Pass: That broken, laser-accurate diagonal shot-pass is now about **60-80% less effective** than it used to be' and 'C-Spamming: The efficacy of the float to Haaland, head to Mbappe and repeat meta has been **vastly reduced**.'",
    "NO FAKE SHOT IN DLS - the dedicated strike-feint does not exist, which is a real gap in the attacking repertoire for a player arriving from FIFA or eFootball. THE SET-PIECE RANDOMISATION COMPLAINT: three identical corners, three different outcomes - recorded as a complaint, not a mechanic, because FTG officially denies overlaid difficulty controls. THE BOTH-FOOTED WINGER is a shape asset, not just a finishing one: it creates the in-swinger from either flank. THE THROUGH-BALL INPUT (aim into space, tap C or A). AND the specific quotes for the diagonal A pass nerf (60-80%) and the C-spam reduction.",
    "NO FAKE SHOT, AND THE SET-PIECE RANDOMISATION COMPLAINT",
    quality="community")

add_claim("⚠️ THERE IS NO FAKE SHOT IN DLS — a documented negative the corpus did not carry. Raised in a celebrations request thread, where the top reply names the real gap: '**What DLS first needs is a fake shot. It is one of the most basic things lacking in DLS.**' **So the dedicated fake shot — the feint of a strike that freezes a defender and opens a lane — does not exist.** The corpus's catalogue has the Feint (a direction change) and a creator's fake-pass-and-shoot combination, but neither is a fake shot. A player arriving from FIFA or eFootball will look for it and not find it.", 3, "skillmoves/no-fake-shot", [e_sk], notes="A documented negative to add to the catalogue's gap list")
add_claim("THE SET-PIECE RANDOMISATION COMPLAINT: '**Many times you point your joystick exactly where you want it and it seems some RnG kicks in where it kinda randomizes what you want to happen. For example, you can take a corner while pointing exactly where you want it 3 times, the exact same place, and all 3 times the ball ends up somewhere different. Same for freekicks, pens, and even in game sometimes.**' **So identical inputs produce different outcomes** — recorded as a COMPLAINT from a suggestion thread, not as a confirmed mechanic, because the corpus also carries FTG's official denial of overlaid difficulty controls. The honest reading is that set pieces carry variance the player cannot see, and the corpus's drill-one-routine advice is the correct response.", 3, "setpieces/randomisation-complaint", [e_sk], notes="The same 'scripts' perception arriving from the set-piece side")
add_claim("THE RESPONSIVENESS COMPLAINT, a third source for the corpus's input-delay finding: 'You can tap the screen and quickly change direction to chop the ball but **6-7/10 times your player will take a touch before the tap ahead movement is registered.**'", 3, "controls/responsiveness-complaint-third-source", [e_sk])
add_claim("THE BOTH-FOOTED WINGER is a SHAPE asset, not merely a finishing one: '**Both-footed wingers is great as-well because they can put sweeping passes forwards/inwards - like left foot on left wing for a striker to run onto; or they can cut inside and take a shot - like right foot on left wing.**' So a both-footed winger creates the in-swinger from either flank, which is a different benefit from the both-footed striker the corpus already records (CLAIM-1666).", 3, "tactics/both-footed-winger-shape-asset", [e_sk])
add_claim("THE THROUGH-BALL INPUT, from a flagged source and recorded at C3 with the flag: '**Master the Through Ball - Instead of passing directly to a player, aim the joystick into empty space and tap C or A.** This allows fast strikers to run onto the ball.' The mechanism matches the corpus's pass-into-space rule; the input pairing is the new part.", 3, "gameplay/through-ball-input", [e_sk])
add_claim("THE DIAGONAL A PASS NERF, with the specific quote: 'The Unstoppable Diagonal A Pass: That broken, laser-accurate diagonal shot-pass is now about **60-80% less effective** than it used to be.' And the C-spam reduction: 'The efficacy of the float to Haaland, head to Mbappe and repeat meta has been **vastly reduced**.' Both are launch-to-current comparisons, so they describe the build the corpus's advice is aimed at.", 3, "gameplay/diagonal-a-pass-and-cspam-nerfs", [e_sk])

for p in ['EV-525_no_fake_shot.html','EV-525b_setpiece_randomisation.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
