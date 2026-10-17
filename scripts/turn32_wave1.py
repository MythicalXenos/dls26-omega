#!/usr/bin/env python3
"""Turn 32 Wave 1: Form Boost, player switch, FTG corporate."""
import json,os,datetime
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
    c={'claim_id':cid_full,'proposition':prop,'confidence_tier':tier,'supporting_evidence':evr,'challenges':chal or [],'context_build':ctx,'last_checked_by':f'turn 32 wave 1 ({ts})','last_valid_check':ts,'last_attempt':ts,'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),'volatility_tier':vol,'cross_refs':[],'replacements':None,'contradicting_evidence':[]}
    claims.append(c); return cid_full
mc=max_c
def C(prop,tier,evr,chal=None,vol='Low'):
    global mc; mc+=1; return mk_claim(mc,prop,tier,evr,chal,vol)
e310=mk_ev(max_e+1,'official-support (ftgames 360003914778); levelwinner guides; r/DLS form boost threads; gamingonphone; r/DLS advice','evidence/raw/official_turn32/EV-310_form_boost.html',"OFFICIAL: Form Boost temporary, duration set by Training facilities level (min 1 match). Levelwinner DLS20/21/24 (consistent across versions): Common Form=5 gems=+1 OVR/1 match; Rare=8 gems=+2; Legendary=10 gems=+3. Accessed via player card -> Form Boost bottom-right. Halftime team form boost costs 30 coins. Reddit 2024: lucky rolls can yield +4 STR/+4 CON (weight-2 attributes) giving effective +4-5 OVR. Training Centre upgrades extend Form Boost duration and unlock formations and discount coaches. Strategic: no first-half subs unless injured; players regain stamina at half; subs 65+ mins.")
e311=mk_ev(max_e+2,'r/DLS controls threads; r/DLS DLS26 complaints; Play Store reviews Sep 2026; sportsdunia settings','evidence/raw/reddit_turn32/EV-311_player_switch.html',"Auto Switch: Off/Low/High; C-button=manual switch. Cross Assist/Kick Assist: Off/On/High. Competitive: Auto Switch Low, all assists Off. Button Size, Fixed Stick, Stick Visible, Stick Size, In-Game Tactics configurable. DLS26 launch complaints: auto-switch picks wrong player (far from ball); 0.5-2 sec delay on C-press; 3-4 taps needed vs DLS25's 1-2. Persistent complaints through Mar 2026 and Sep 2026 Play Store reviews.")
e312=mk_ev(max_e+3,'Tracxn/Crunchbase/Endole/LinkedIn/MobyGames/CompaniesHouse/Pomanda/IMDb/Wikipedia','evidence/raw/corporate_turn32/EV-312_ftg_corporate.html',"First Touch Games Ltd (CH 07638595). Incorporated 18 May 2011; spun out of Exient Sep 2011. Oxford, UK; PO Box 390 Oxford OX1 9RW. Founder/CEO Charles Edward Chapman (b Oct 1974, Oxford 1993, co-founded Exient 2001 w/ Dave Hawkins, 90% shareholder). Co-director Siobhan Cooney. 36-45 employees (2026). Revenue ~$6.4M. SIC 58210. Named staff: Andy Dunn (CPO), Gino Magnotta (COO), Lee Gumbrell (Head Product/Data Sci Oct2023), Ed Richards (UA Sep2022), Thomas Cather (Social Dec2023), Adam Finch (Sr Artist), Ben Jones (Sr Artist), Peter Smith (Programmer/Systems Design), Chris Hull (Sr Programmer), Leo Pettecrew (Dev Aug2022), Andrew Weinkove (Sr Programmer), Andrew Stevens (Programmer), Charles Clark (Marketing).")
C("Form Boost (per-player temporary upgrade): Common=5 gems=+1 OVR, Rare=8 gems=+2 OVR, Legendary=10 gems=+3 OVR. BASE DURATION=1 match; Training Centre upgrades extend duration, unlock formations, and discount coach hire. Accessed via player card -> Form Boost button bottom-right.",'High Confidence',[e310],['Price points from Level Winner guides; assumed consistent in DLS26.'],vol='Low')
C("Form Boost attribute distribution is random. Lucky rolls can award +4 STR +4 CON (weight-2 attributes) producing effective OVR jumps of +4 to +5 beyond headline tier (community observation).",'Community Consensus',[e310],vol='Medium')
C("At halftime in matches, a TEAM form boost / stamina refresh is offered for 30 coins. Best practice: no first-half subs unless injured (stamina partially recovers); subs from 65th+ minute to exploit fatigue.",'Community Consensus',[e310],vol='Low')
C("Control settings: Auto Switch Off/Low/High (C-button = manual switch); Cross Assist and Kick Assist each Off/On/High; Button Size, Fixed Virtual Stick, Virtual Stick Visible, Virtual Stick Size, In-Game Tactics all configurable. Competitive baseline: Auto Switch Low, all assists Off.",'High Confidence',[e311])
C("DLS26 player switching was widely reported as buggy at launch and through Sep 2026: auto-switch selects player far from the ball; 0.5-2s delay after C-press; 3-4 taps needed to reach correct defender vs 1-2 in DLS25. Some players felt the new manual-switch emphasis improved control, but the bug reports persist.",'Community Consensus',[e311],vol='Medium')
C("FTG corporate identity: First Touch Games Ltd, UK private company (Companies House 07638595), incorporated 18 May 2011 in Oxford (spun out of Exient Entertainment Sep 2011). Mailing: PO Box 390 Oxford OX1 9RW. Founder/CEO Charles Chapman (b Oct 1974; 90% shareholder; co-founded Exient 2001). Co-director Siobhan Cooney. 36-45 employees (2026). Revenue ~$6.4M (estimate). SIC 58210 computer games publishing.",'High Confidence',[e312],vol='Low')
C("Named FTG employees (LinkedIn/business directories): Andy Dunn (CPO/Production Manager), Gino Magnotta (COO), Lee Gumbrell (Head of Product & Data Science, Oct 2023), Ed Richards (UA Manager, Sep 2022), Thomas Cather (Social Media, Dec 2023), Adam Finch (Senior Artist), Ben Jones (Senior Artist), Peter Smith (Programmer/Systems Designer), Chris Hull (Senior Programmer), Leo Pettecrew (Developer, Aug 2022), Andrew Weinkove (Senior Programmer), Andrew Stevens (Programmer), Charles Clark (Marketing Director).",'Medium Confidence',[e312],['Current employment not independently verified beyond public listings.'],vol='Medium')
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c)+'\n')
with open(EIP,'w') as f:
    for e in ev: f.write(json.dumps(e)+'\n')
print(f"Added {mc-max_c} new claims and 3 EVs (EV-310..EV-312). Totals: {len(claims)} claims, {len(ev)} EVs")
