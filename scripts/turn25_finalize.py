#!/usr/bin/env python3
"""Turn 25 finalize: EV-253 + CLAIM-146..149 + sample 15."""
import json,os,re,random
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
ev.append({'evidence_id':'EV-253','artifact':'evidence/extract/EV-253_trungtahust_historical_master_formula.md','tool':'github-api (allowlisted)','origin_method':'TrungTaHust/dls-ext master data.json (26145 rows, 8 updates 20231-20262) + 20263/20252/20253 + Larrycr7aaaa script.js inspection',
           'retrieved_at_utc':'2026-10-18T00:45:00Z','authenticity_limits':'Community PWA data; 32/26145 rows are likely scrape typos (residuals >|2|). Weights derived via OLS not direct APK disassembly; formula MAE 0.38 leaves room for rounding quirks / hidden bonuses on ~0.2% of players. Formula const drift across versions likely reflects author scrape alignment, not an in-game change.','covers':['CLAIM-145','CLAIM-146','CLAIM-147','CLAIM-148','CLAIM-149','CLAIM-141']})
for cid,toks in {'CLAIM-145':['EV-253'],'CLAIM-141':['EV-253']}.items():
    for t in toks:
        if t not in by[cid]['supporting_evidence']: by[cid]['supporting_evidence'].append(t)
by['CLAIM-145']['proposition']='DLS26 OVR is computed as a weighted linear sum of the 8 attributes plus a constant, STABLE across all updates 20231→20263. Best-fit across 23,327 non-GK base-card rows (all versions pooled): OVR ≈ round(1.89 + 0.211·CON + 0.166·STR + 0.148·ACC + 0.142·SPE + 0.112·PAS + 0.111·SHO + 0.107·TAC + 0.037·STA). MAE=0.38, RMSE=0.49; 73.1% of predictions exact-after-round, 99.8% within ±1, 32/26,145 rows are likely community-DB scrape typos (not formula violations). CON (Control) is the highest-weighted attribute; STA (Stamina) the lowest. For GKs, the two heaviest weights (≈0.48 each) are carried by the two columns labelled GKR/GKH in promo data, with the other six near-zero. Per-version OLS weights vary by <0.04 on all attributes across 8 updates — no evidence of formula retuning in 3 years.'
by['CLAIM-145']['context_build']='TrungTaHust/dls-ext master historical DB: 26,145 rows across 8 updates (20231-20262 + 20263 separate); validated on 38 Larrycr7aaaa promo outfield cards (MAE 0.70)'
by['CLAIM-145']['confidence_tier']='High Confidence'  # upgraded from Community Consensus with 26k-row dataset + cross-version stability
new=[
('CLAIM-146',
 'Position codes mix English and Spanish/Portuguese abbreviations in raw data files: GK/POR (goalkeeper); CF and DC (striker); SS and SD (second striker); LW/RW and EI/ED (wings); CB and DFC (center-back); RB/LB and LD/LI (fullbacks); CM and MC; AM and MCO (attacking mid); DM and MCD (defensive mid); LM/RM and CAI/CAD. The code set observed is {GK,POR,CF,DC,SS,SD,AM,MCO,CM,MC,DM,MCD,LM,CAI,RW,RM,CAD,LW,EI,CB,DFC,LB,LI,RB,LD,LWB,RWB} (17 positions accounting for language aliases; underlying positional groups: GK, CB, LB/RB, LWB/RWB, DM, CM, AM, LM/RM, LW/RW, SS, CF).',
 'Community Consensus','Low',['EV-253','EV-251','EV-252','CLAIM-001'],'2026-11-18',
 ['Aliases inferred from script.js colour mapping (pos-gk/pos-del/pos-med/pos-def); Step 2 to enumerate internal position IDs and any additional positions (e.g. SW, false 9)'],['CLAIM-001','CLAIM-137']),
('CLAIM-147',
 'Base/purchasable roster OVR hard cap is 86 in EVERY version 20231–20263 (3 years of updates). OVRs 87–98 exist ONLY on special/promo/legend/event cards (Champion, Classic, Star, Team, Dynamic Stars, WC Champions, WC Heroes, Cult Heroes, Dream Stars, Legends, Nuevas Especiales), which are NOT part of the regular transfer-market base roster. Erling Haaland held the 86 cap through 20231–20253; Ousmane Dembélé takes the cap (alongside Haaland/Kane/Mbappé) from 20261 onward. No base player has ever exceeded 86 in the historical DB.',
 'High Confidence','Low',['EV-253','EV-251','CLAIM-141','CLAIM-142','CLAIM-144'],'2026-11-18',
 ['Only 8 version slices (20231-20262 in master + 20263 separate) inspected; future updates may raise base cap. Cap confirmed only via community DB; Step 2 should verify against the in-game max-OVR constant'],['CLAIM-141','CLAIM-142','CLAIM-144']),
('CLAIM-148',
 'Base roster size has grown ~4.5× across updates: 20231=1,224, 20241=1,681, 20242=4,126, 20251=3,828, 20252=3,602, 20253=3,798, 20261=2,518, 20262=5,369, 20263=5,484 players. DLS26 ships with over 5,400 base players by the third 2026 update; the Unlicensed bucket has grown from ~0 in 20231 to ~1,831 in 20263.',
 'Community Consensus','Low',['EV-253','EV-251','CLAIM-143'],'2026-11-18',
 ['Counts are from one community DB; actual in-game roster likely larger if national-teams-only players are added separately'],['CLAIM-143']),
('CLAIM-149',
 'Transfer price `prc=0` in roster data marks players that are NOT on the open transfer market in that update (loaned, not yet released, untradeable special-card variants, or otherwise locked). ~14% (≈3,565) of historical player-rows carry prc=0; these players are visible in the game but cannot be bought/sold at that update.',
 'Community Consensus','Medium',['EV-253','EV-251','CLAIM-139'],'2026-11-18',
 ['Alternative interpretation (prc missing in scrape) cannot be fully ruled out without APK evidence; pattern of zero-prices matching player-move windows (loans, transfers) supports the locked/loaned explanation'],['CLAIM-139']),
]
for cid,prop,tier,vol,evl,due,chall,cross in new:
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'TrungTaHust/dls-ext master 20231-20263 (26k+ rows)','confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':evl,
                   'contradicting_evidence':[],'last_valid_check':'2026-10-18T00:45:00Z','last_attempt':'2026-10-18T00:45:00Z','last_checked_by':'turn-25 historical DB formula analysis',
                   'next_due':due,'origin_history':[{'at':'2026-10-18','origins':['community-database']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-253': cov|={'CLAIM-145','CLAIM-146','CLAIM-147','CLAIM-148','CLAIM-149','CLAIM-141'}
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
# sample 15
random.seed(25)
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
print(f'SAMPLE 15: OK={ok} WARN={warn} BAD={bad}')
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
