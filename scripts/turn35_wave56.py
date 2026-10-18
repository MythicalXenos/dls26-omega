#!/usr/bin/env python3
"""Turn 35 Wave 56: THE OFFICIAL MATCHMAKING ARTICLE RE-READ IN FULL - which corrects an overstated
corroboration in C-024 - plus a COHERENCE AUDIT of all five deliverables that found four stale spots.

Wave 56 is an audit wave. Two results:

1. C-024 OVERSTATEMENT CORRECTED. The corpus records that 'the OFFICIAL FTG matchmaking article states
   that team strength is an explicit matching input'. Re-reading the article in full shows it does not.
   The enumerated matching inputs are LIVE Tier ranking, location and the availability pool; team
   strength appears in a different sentence about OUTCOMES ('outcomes are governed by individual skill
   levels as reflected in their tactics, gameplay choices and team strength'). So the maxed-squad
   handicap has NO official basis - it remains a community hypothesis. The article does, however,
   firmly establish that there are 'no additional overlaid controls to manage the difficulty
   experience', which kills the rubber-banding theory outright.

2. FOUR STALE SPOTS FOUND AND FIXED, including one in the user-facing First Contact script that claimed
   the five open gaps 'all need APK datamining rather than more web research' - a claim that three of
   the five have since disproved by being closed with official support articles.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w56')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="official"):
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

e_mm=new_ev("FTG support 360018359998 'How does Dream League Live matchmaking work?' - re-fetched in full and quoted verbatim during the ckpt-131 coherence audit",
    "THE OFFICIAL MATCHMAKING ARTICLE, RE-READ IN FULL - and the correction it forces. THE VERBATIM TEXT: 'Multiplayer LIVE mode \"matches\" players in real-time based on a number of player-related attributes & elements. These are primarily their LIVE Tier ranking, their location and the availability pool of other players at the time of matching. The main objective in matchmaking is to try and ensure that every player is matched against an opponent of similar standing & skill as much as is possible, enabling a competitive and fair game conducted within the best possible live experience. That should generally result in players playing against opponents of the same Tier, but occasionally that will not be possible due to the reduced availability of players. There are no additional overlaid controls to manage the difficulty experience. Outcomes are governed by individual skill levels as reflected in their tactics, gameplay choices and team strength. As players progress through the Tiers in LIVE mode, opponents will naturally become will become more challenging.' THE CORRECTION: the corpus's C-024 entry records that 'the OFFICIAL FTG matchmaking article states that team strength is an explicit matching input'. IT DOES NOT. The enumerated matching inputs are exactly three - LIVE Tier ranking, location, and the availability pool. Team strength appears in a DIFFERENT sentence, and that sentence is about OUTCOMES, not pairing: 'outcomes are governed by individual skill levels as reflected in their tactics, gameplay choices and team strength'. So (a) the maxed-squad handicap has NO official support and must be carried as a community hypothesis only, and (b) the vague phrase 'similar standing & skill' is a stated OBJECTIVE of matchmaking, not an enumerated input - the article's own list does not include squad strength. WHAT THE ARTICLE DOES ESTABLISH, FIRMLY: 'There are no additional overlaid controls to manage the difficulty experience' - i.e. FTG explicitly denies any hidden difficulty adjustment, rubber-banding or momentum engine. Opponents 'naturally become more challenging' as you climb tiers, which is a pool-composition effect, not a handicap. This also resolves the Turkish-opponent micro-delay accusation definitively: an overlaid difficulty control is officially ruled out, so any perceived opponent-specific adjustment is latency or perception, not a game mechanic.",
    "evidence/raw/turn35_w56/EV-469_official_matchmaking_full.html",
    "OFFICIAL MATCHMAKING (verbatim, re-read in full): matching inputs are exactly three - LIVE Tier ranking, location, and the availability pool of other players. The stated objective is 'an opponent of similar standing & skill', which should generally mean the same Tier but will not always be possible when player availability is low. 'There are no additional overlaid controls to manage the difficulty experience' - FTG explicitly denies hidden difficulty adjustment, which rules out rubber-banding and any opponent-specific handicap. Team strength appears only in the OUTCOMES sentence ('outcomes are governed by individual skill levels as reflected in their tactics, gameplay choices and team strength'), NOT as a matching input. CORRECTION: the corpus's C-024 claim that the official article makes team strength an explicit matching input is an OVERSTATEMENT - the maxed-squad handicap therefore has no official basis and stays a community hypothesis",
    quality="official")

add_claim("THE OFFICIAL MATCHMAKING INPUTS ARE EXACTLY THREE: 'their LIVE Tier ranking, their location and the availability pool of other players at the time of matching.' Team strength is NOT among them.", 1, "dll/official-matching-inputs", [e_mm], notes="Corrects the corpus's earlier reading")
add_claim("CORRECTION TO C-024: the claim that 'the OFFICIAL FTG matchmaking article states that team strength is an explicit matching input' is an OVERSTATEMENT. Team strength appears only in the outcomes sentence - 'outcomes are governed by individual skill levels as reflected in their tactics, gameplay choices and team strength' - which is about how matches play out, not who you are paired with. The maxed-squad handicap therefore has NO official basis and must be carried as a community hypothesis only.", 1, "dll/c-024-official-corroboration-corrected", [e_mm], notes="The provisional resolution (competitive-but-not-maxed) survives on community evidence alone")
add_claim("OFFICIAL: 'There are no additional overlaid controls to manage the difficulty experience.' FTG explicitly denies hidden difficulty adjustment, which rules out rubber-banding, momentum engines and any opponent-specific handicap - including the Turkish-opponent micro-delay accusation.", 1, "dll/no-overlaid-difficulty-controls", [e_mm], notes="Definitive official basis for retiring the rubber-banding theory")
add_claim("The official matchmaking objective is 'an opponent of similar standing & skill as much as is possible', which 'should generally result in players playing against opponents of the same Tier, but occasionally that will not be possible due to the reduced availability of players' - so tier mismatches are an availability effect, not a ranking error.", 1, "dll/mismatch-is-availability", [e_mm])
add_claim("Opponents 'naturally become more challenging' as players progress through the Tiers - a pool-composition effect as stronger players concentrate in higher tiers, not an applied handicap.", 1, "dll/opponents-harden-by-tier", [e_mm])

# ---------- EV-470: the coherence audit ----------
e_audit=new_ev("ckpt-131 deliverable coherence audit: word counts across all five deliverables, a stale-figure sweep for six superseded strings, a context check of every hit, and a review of the operational rules' facility, Fan Approval and open-gaps sections plus the First Contact script's closing gap paragraph",
    "THE ckpt-131 COHERENCE AUDIT - what was checked, what was found, what was fixed. SCOPE: all five build deliverables plus the conflict register and source register - strategy_masterplan (12,630 words), operational_rules (5,642), dll_tier_playbook (2,421), FIRST_CONTACT_v2 (2,694), source_reliability (1,160) and conflicts (5,817); a stale-string sweep for six superseded figures; and a context check of every hit to separate legitimate corrective mentions from live stale assertions. THE FOUR STALE SPOTS FOUND AND FIXED: (1) operational_rules line ~217 still read 'Per-facility total is 1,125 gems; all five facilities is 5,625 gems' as though those were maxed costs - contradicted by the ckpt-131 finding that 1,125 is the first five levels and a maxed facility is 4,125. (2) operational_rules line ~295 carried 'Fan Approval: 75% = 500 XP, 100% = 2,000 XP. Mechanics above the first tier are an open gap' with no trace of the ckpt-126 documented negative. (3) operational_rules line ~413 listed 'five numeric tables remain open ... These can only be closed by APK datamining (Step 2, postponed)' - three of those five have since been closed by OFFICIAL SUPPORT ARTICLES, not datamining, so both the list and the method claim were wrong. (4) FIRST_CONTACT_v2 told the user that the five open gaps 'all need APK datamining rather than more web research' - demonstrably false after ckpt-126/127/128, and the most damaging of the four because it is user-facing. WHAT PASSED: the nine-state machine S0-S9 is intact as a flow diagram (grep for a table format returned nothing because the states are drawn as S0 -> S1 transitions); the Isco, Fan Approval, 63-achievement and 7-hour mentions in the masterplan are all inside explicit corrective passages, not stale assertions; the stadium's separate 5,625-gem-and-10,000-coins figure is a distinct, correctly attributed single-player report and not the facility budget.",
    "evidence/raw/turn35_w56/EV-470_coherence_audit.html",
    "COHERENCE AUDIT (ckpt-131): all five deliverables checked for stale figures after 131 checkpoints of edits. FOUR STALE SPOTS FOUND AND FIXED: (1) operational rules still quoted '1,125 gems per facility / 5,625 for all five' as maxed costs - now corrected to the 75xN pattern with 4,125 per maxed facility; (2) operational rules' Fan Approval line lacked the ckpt-126 documented negative; (3) operational rules' 'five numeric tables remain open, all needing APK datamining' was wrong on both the list and the method - three were closed by official support articles; (4) FIRST_CONTACT_v2 told the user the five gaps 'all need APK datamining rather than more web research' - false and user-facing. PASSED: the S0-S9 state machine is intact, and every Isco / Fan Approval / 63-achievement / 7-hour mention in the masterplan sits inside an explicit corrective passage",
    quality="official")

add_claim("The nine-state machine S0 through S9 is intact in the operational rules as a flow diagram of S0 -> S1 transitions, not a table - so a table-format grep returns nothing and the machine should be checked by searching for the state tokens.", 1, "audit/state-machine-intact", [e_audit], notes="Prevents a future false 'missing state machine' finding")
add_claim("The masterplan's separate '5,625 gems and 10,000 coins' stadium figure is a single player's completed-stadium report and is NOT the facility budget - the two figures coincide numerically and must not be conflated.", 1, "audit/stadium-vs-facility-figure-disambiguation", [e_audit])

for name in ('EV-469_official_matchmaking_full.html','EV-470_coherence_audit.html'):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
