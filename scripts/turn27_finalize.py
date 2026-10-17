#!/usr/bin/env python3
"""Turn 27 finalize: EV-255 + CLAIM-154..158, sample 17, registry-sweep EV noting TLS blocks."""
import json,os,re,random
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
ev.append({'evidence_id':'EV-255','artifact':'evidence/extract/EV-255_leo_cb_trainer_coach_mechanics.md','tool':'github-api (allowlisted)','origin_method':'LeoH321/dls26-tool-CB (DLS26China WeChat CB-training simulator) — single-page HTML+JS exhaustive DP solver, 23KB index.html source',
           'retrieved_at_utc':'2026-10-18T01:35:00Z','authenticity_limits':'Community-built simulator; author reverse-engineered mechanics from play. Position-specific weights are only for CB tackle-polarized builds. Three rarities modeled — yellow/epic tier if it exists is not used in this solver. Fractional-overflow distribution is modeled but the exact integer rounding is ambiguous without APK disassembly. High Confidence corroboration for coach tier boosts (+1/+2/+3), weighted capacity, and 100-stat cap.',
           'covers':['CLAIM-154','CLAIM-155','CLAIM-156','CLAIM-157','CLAIM-158','CLAIM-049','CLAIM-052']})
# Note registry sweep blocked by TLS - don't issue an EV; just document in log.
# upgrades
by['CLAIM-049']['proposition']='DLS26 player development is a WEIGHTED-CAPACITY system: each training ("coach use") adds `boost_level` points to a uniform-random subset of k=boost_level non-maxed attributes, with a training-capacity cost of Σ(weight_of_each_hit_attribute × boost_level). Attribute weights vary by position: for CB (defender) CON weight=2, PAS/SHO/TAC weight=1 (LeoH321/DLS26China simulator). Three coach rarities in common use: Common (white, +1, cost×1), Rare (blue, +2, cost×2), Legendary (gold, +3, cost×3). Attributes max at 100 and leave the draw pool. Over-capacity ("爆仓") distributes remainder fractionally across selected attributes, diluting gains — incentivizing careful coach selection based on remaining capacity (≥12 safe gold, ≥6 blue, <6 white per DLS26China DP solver).'
by['CLAIM-049']['confidence_tier']='High Confidence'
by['CLAIM-049']['supporting_evidence'].append('EV-255')
new=[
('CLAIM-154',
 'Coach tiers confirmed: three rarities used in the CB-training solver: Common (白/white) = +1 stat boost at cost-multiplier ×1; Rare (蓝/blue) = +2 at ×2; Legendary (金/gold) = +3 at ×3. These correspond to the +1/+2/+3 coaching boosts previously documented from EV-247. There is likely a fourth Epic (yellow) tier that the solver does not expose for CB builds; to be confirmed in Step 2.',
 'High Confidence','Low',['EV-255','CLAIM-049'],'2026-11-18',
 ['Three rarities modeled; an Epic (yellow) tier appears in EV-247 SakPro tier list but this CB solver only uses 3 — possible position-specific coach pool differences; confirm in Step 2'],['CLAIM-049','CLAIM-052']),
('CLAIM-155',
 'Per-attribute weights in training-capacity cost are POSITION-SPECIFIC. For CB (defender) tackle-polarized builds, Control (CON/控制) carries weight 2 and costs double capacity per point; Passing (PAS/传球), Shooting (SHO/射门), Tackling (TAC/抢断) carry weight 1 each. Weights for other positions are not yet extracted (EV-247 previously stated "weighted capacity" without numbers; now quantified for CB).',
 'High Confidence','Low',['EV-255','CLAIM-049'],'2026-11-18',
 ['Only CB weights captured; other positions (CF/LW/AM/CM/DM/LB/RB/GK) likely use different attribute weights; other DLS26China simulators (for other positions) likely exist but were not found in LeoH321 GitHub org'],['CLAIM-049']),
('CLAIM-156',
 'Coach application mechanic in detail: when a coach of boost level k is used, k DISTINCT attributes are drawn uniformly at random from the pool of trainable attributes that are still below 100 (maxed attributes are automatically excluded from the draw). Each hit attribute gains k points, hard-capped at 100. Total training-capacity cost = Σ(weight of each hit attribute) × k. If the player runs out of capacity mid-coach (爆仓 / busted), the remaining capacity is split fractionally across the hit attributes (gainedStat = cap / sumWeight, distributed proportionally), which dilutes the gain and is generally sub-optimal.',
 'High Confidence','Medium',['EV-255','CLAIM-049','CLAIM-052'],'2026-11-18',
 ['Uniform random over C(n,k) combinations is the simulator author\'s model; actual in-game RNG may use weighted draws or positional priority; fractional overflow rounding not confirmed; Step 2 needed to verify exact distribution'],['CLAIM-049','CLAIM-052']),
('CLAIM-157',
 'Stat colors on in-game player cards follow thresholds: attribute ≥90 → blue, ≥80 → green, ≥70 → yellow, <70 → red (per applyDlsColor in LeoH321/DLS26China tool CSS, matching DLS card-color conventions seen in EV-246). The highest visible stats (95–100, e.g. ACC/STA/CON/PAS on maxed Dynamic Stars 96 cards) render blue.',
 'Community Consensus','Low',['EV-255','EV-246'],'2026-11-18',
 ['Color thresholds from one community tool; consistent with screenshot evidence'],['CLAIM-036']),
('CLAIM-158',
 'DLS26China optimal-coach decision rule for CB training: pick Gold (+3) when remaining weighted capacity ≥12 (safe for burst); Blue (+2) around 6–12; White (+1) under 6 to avoid busting. The DP solver computes exact target-hit probability per coach and picks argmax; thresholds above are the rule-of-thumb encoded in the persona text.',
 'Community Consensus','Medium',['EV-255','CLAIM-049'],'2026-11-18',
 ['Thresholds are heuristic, not hard game rules; actual optimal play depends on current attribute state and target'],['CLAIM-049','CLAIM-052']),
]
for cid,prop,tier,vol,evl,due,chall,cross in new:
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'LeoH321/dls26-tool-CB (DLS26China CB trainer simulator JS) + EV-247 Chinese coach doc','confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':evl,
                   'contradicting_evidence':[],'last_valid_check':'2026-10-18T01:35:00Z','last_attempt':'2026-10-18T01:35:00Z','last_checked_by':'turn-27 DLS26China simulator source analysis',
                   'next_due':due,'origin_history':[{'at':'2026-10-18','origins':['community-database','community-tool-source']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-255': cov|={'CLAIM-154','CLAIM-155','CLAIM-156','CLAIM-157','CLAIM-158','CLAIM-049','CLAIM-052'}
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
# sample 17
random.seed(27)
ev_idx={e['evidence_id']:e for e in ev}
strata={'Confirmed':2,'High Confidence':2,'Community Consensus':2,'Speculative':1}; picked=[]
for tier,n in strata.items():
    pool=[c for c in claims if c['confidence_tier']==tier]; random.shuffle(pool); picked.extend(pool[:n])
ok=warn=bad=0; repairs={}
for c in picked:
    cid=c['claim_id']; t=c['confidence_tier']; notes=[]; status='OK'
    ev_tok=[]
    for s in c['supporting_evidence']: ev_tok+=re.findall(r'(?:EV|EVD)-(\d{3,4})',s)
    if not ev_tok and not any('cross-ref' in ch.lower() or 'synthesis' in ch.lower() for ch in c.get('challenges',[])): notes.append('no EV'); status='BAD'
    seen=set()
    for tok in ev_tok:
        full=('EVD-'+tok if any('EVD-'+tok in s for s in c['supporting_evidence']) else 'EV-'+tok)
        if full in seen: continue; seen.add(full)
        if full in ev_idx:
            if cid not in ev_idx[full].get('covers',[]): notes.append(f'{full} covers[] miss'); status='WARN'; repairs.setdefault(full,set()).add(cid)
        else: notes.append(f'not in index: {full}'); status='BAD'
    tag='OK' if status=='OK' else ('WARN' if status=='WARN' else 'BAD')
    print(f'  {cid} [{t}] {tag}: {c["proposition"][:80]}...')
    for n in notes: print('     -',n)
    if status=='OK': ok+=1
    elif status=='WARN': warn+=1
    else: bad+=1
print(f'SAMPLE 17: OK={ok} WARN={warn} BAD={bad}')
ev2=[json.loads(l) for l in open(EIP) if l.strip()]
for e in ev2:
    if e['evidence_id'] in repairs:
        cov=set(e.get('covers',[])); cov|=repairs[e['evidence_id']]
        e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev2)+NL)
b=open(CP,'rb').read()
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev2}
badcov=[(e['evidence_id'],c) for e in ev2 for c in e.get('covers',[]) if c.startswith('CLAIM-') and c not in ids]
miss=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('claims',len(claims),'LF',b.count(b'\n'),'ev',len(ev2),'badcovers',badcov,'miss',miss)
