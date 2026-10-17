#!/usr/bin/env python3
"""Turn 31 Wave 3: Team OVR = mean of starting-11 (sakibpro), chemistry effect on transfer market, no redeem codes observed."""
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
    c={'claim_id':cid_full,'proposition':prop,'confidence_tier':tier,'supporting_evidence':evr,'challenges':chal or [],'context_build':ctx,'last_checked_by':f'turn 31 wave 3 ({ts})','last_valid_check':ts,'last_attempt':ts,'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),'volatility_tier':vol,'cross_refs':[],'replacements':None,'contradicting_evidence':[]}
    claims.append(c); return cid_full
mc=max_c
def C(prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    global mc; mc+=1; return mk_claim(mc,prop,tier,evr,chal,vol,ctx)
e308=mk_ev(max_e+1,'community-tool (sakibpro.com DLS26 Squad Builder FAQ Aug 2026)','evidence/raw/sakibpro_turn31/EV-308_team_ovr.html',"SakibPro Squad Builder FAQ: 'The Team OVR is automatically calculated by taking the average (mean) base or maxed Overall Ratings of all 11 players currently placed in your starting formation on the pitch. Empty slots are not counted in the division.' This is a direct plain-English statement of the Team OVR formula from a widely-used community tool; it supersedes my earlier QR-decomposition MAE-0.376 attempt which was fit on a small sample. Note: Team OVR is MEAN of 11 starters; substitutes/benched players do not count. This is consistent with the sakibpro coach simulator already cited and the Bluestacks observation that higher team rating yields better Transfer Market appearances.")
e309=mk_ev(max_e+2,'community-web-en (wethrift DLS promo codes; BlueStacks redeem codes page; web search DLS26 redeem codes Oct 2026)','evidence/raw/community_turn31/EV-309_redeem_codes.html',"Search for DLS26 free redeem/gift codes (Oct 2026) did not surface any reliable FTG-issued code. The BlueStacks 'Redeem Codes' page exists for DLS but specific codes shown (e.g. '55SCOOBYWRX' on wethrift) appear to be affiliate/coupon codes for unrelated shopping, not in-game currency. No confirmed active FTG-issued promo-code redemption system found. DLS26 uses in-game Events, Prize Ladder, Season Pass, and Daily Login as reward channels — NOT a promo-code text-entry system (unlike some Asian gacha titles).")
C("Team OVR is calculated as the ARITHMETIC MEAN of the 11 players in the starting formation on the pitch (substitutes/benched players NOT counted). Empty slots are excluded. This supersedes my earlier QR-decomposition OVR model which used a small sample and produced MAE 0.376; per the community's most-used Squad Builder tool it is a simple mean.",'High Confidence',[e308],['Sakibpro community tool statement; to be cross-verified against in-client team-OVR display during device pipeline.'],vol='Low')
C("DLS26 does NOT appear to operate an active promo-code/gift-code redemption system (text-code entry for free coins/gems). Searches did not surface any FTG-issued codes; coupon-code sites show affiliate/shopping codes unrelated to DLS. Rewards are delivered via Events, Prize Ladder, Season Pass, Daily Login, Challenges, ads, and Dream Draft/Clan/Leaderboards rather than one-shot text codes.",'Community Consensus',[e309],['Redeem-code systems can be added in updates; BlueStacks hosts a DLS redeem-codes page but no currently-active codes verified.'],vol='Medium')
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c)+'\n')
with open(EIP,'w') as f:
    for e in ev: f.write(json.dumps(e)+'\n')
print(f"Added {mc-max_c} new claims and 2 EVs (EV-308..EV-309). Totals: {len(claims)} claims, {len(ev)} EVs")
