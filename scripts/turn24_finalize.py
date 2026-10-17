#!/usr/bin/env python3
"""Turn 24 finalize: add EV-251/252, CLAIM-137..145, run sample 14."""
import json,os,re,random,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]

def evadd(eid,artifact,method,lim,covers):
    ev.append({'evidence_id':eid,'artifact':artifact,'tool':'github-api (allowlisted)','origin_method':method,'retrieved_at_utc':'2026-10-18T00:20:00Z','authenticity_limits':lim,'covers':covers})

evadd('EV-251','evidence/extract/EV-251_trungtahust_dls_ext_full_roster.md',
      'TrungTaHust/dls-ext (Vietnamese DLSStats PWA) — pulled resources/data/20261.json, special.json, formations.json, price_map.json, checklist.json, player_id.json, id_stats.csv',
      'Community PWA data; build version / last live-sync date not stated in repo; corroborated against EV-085/EV-078 on prices and EV-190/EV-248 on card ceiling. High Confidence community, not Confirmed.',
      ['CLAIM-137','CLAIM-138','CLAIM-139','CLAIM-140','CLAIM-141','CLAIM-142','CLAIM-143','CLAIM-078','CLAIM-085','CLAIM-007','CLAIM-060','CLAIM-130','CLAIM-132','CLAIM-001','CLAIM-094'])
evadd('EV-252','evidence/extract/EV-252_larrycr7_promo_cards_full_stats.md',
      'Larrycr7aaaa/DLS26-API (Spanish DLS26 cards API) — dls26-cards.json (41 promo cards, full 8-attribute statlines)',
      'Spanish community fan-API; snapshot of 41 current-event promo cards; no APK provenance; cross-validates OLS formula within ±1 OVR across all 38 outfield promos.',
      ['CLAIM-137','CLAIM-138','CLAIM-144','CLAIM-145','CLAIM-006','CLAIM-024'])

new_claims=[
('CLAIM-137',
 'Outfield players have exactly 8 core integer attributes, each 0–100, in this fixed schema: SPE (Speed), ACC (Acceleration), STA (Stamina), STR (Strength), CON (Control — heaviest-weighted in OVR), PAS (Passing), SHO (Shooting), TAC (Tackling). Observed in TrungTaHust/dls-ext 20261 base roster (2,518 players) and cross-validated in Larrycr7aaaa/DLS26-API promo set (41 cards). Same schema applies to base gold/rare and promo cards.',
 'High Confidence','Low',['EV-251','EV-252'],'2026-11-18',
 ['Schema confirmed from 2,559 player/card rows across two independent community databases; direct APK datamine (Step 2) should verify exact in-game attribute names'],['CLAIM-001','CLAIM-094']),
('CLAIM-138',
 'Goalkeepers use the same 8-column stat grid but two columns are semantically re-mapped: GK Reflexes (GKR) and GK Handling (GKH) replace STA and SHO for GK in promo-card views. Outfield-like SPE/ACC/STR/CON/PAS/TAC remain (plus GKR/GKH), all 0–100. GK OLS fit on 263 base GKs gives STA≈0.475+SHO≈0.476 weights with near-zero others, i.e. the OVR formula routes GK-specific weight through the two columns that become GKR/GKH in promo labels.',
 'High Confidence','Medium',['EV-251','EV-252'],'2026-11-18',
 ['Re-labelling observed on 3 promo GKs only (Navas/Vozinha/Martínez); base GKs in 20261 use the outfield-short labels (sho/tac) with the same semantic swap; Step 2 must confirm the exact column re-mapping'],['CLAIM-137','CLAIM-145']),
('CLAIM-139',
 'Transfer-market coin prices follow a tier table of 4 sub-tiers per OVR (keys "RR1".."RR4" in price_map.json, RR=OVR). Tier-4 is the max price at that OVR; tiers 1–3 are cheaper; tier 1/2 can be 0 (locked/not-sellable for special/promo variants). Observed prices span 20 coins (OVR 54 tier-1) to 2800 coins (OVR 86 tier-4 — top base gold). 20261 base roster ships every player at their tier-4 price; the market adjusts downward based on actual stat spread.',
 'High Confidence','Low',['EV-251'],'2026-11-18',
 ['Corroborates EV-085 SakPro gold cap 2800 and EV-078 Ferdinand Akgul 120-coin 59-CB band; promo-card prices (above 86 OVR) not yet enumerated'],['CLAIM-078','CLAIM-085','CLAIM-141']),
('CLAIM-140',
 'Default (starting) formations are set per team: 149 clubs + 79 nations are catalogued in formations.json. Examples: Man City 4-1-4-1; Man Utd/Liverpool/Chelsea/Barca/Juve/ACM 4-2-3-1; Arsenal/Spurs/Real Madrid 4-1-2-3; PSG 4-3-3; Inter/Italy 3-5-2; Napoli 3-4-2-1; Argentina/England/Spain/Portugal/Netherlands/Belgium 4-3-3; Brazil/France/Germany/Croatia 4-2-3-1. Formation codes use DLS notation (hyphenated 3-5 segments including GK implicitly; first digit is defensive line count).',
 'Community Consensus','Low',['EV-251','CLAIM-077'],'2026-11-18',
 ['Only 149 clubs are mapped; many smaller clubs and current promotions (e.g. Bayern, Atletico, Dortmund) are missing from the formations.json as pulled — likely the PWA author filled the table partially'],['CLAIM-077']),
('CLAIM-141',
 'DLS26 Season 2026 Update 1 ships at least 2,518 base roster players (regular/purchasable, non-promo), OVR 52–86, across 124 club teams + national sides. 367 players are in an "Unlicensed" bucket (e.g. Kane/Bayern at launch). The 4 base-gold players at OVR 86 are Mbappé (Real Madrid), Haaland (Man City), Kane (Unlicensed/Bayern), Dembélé (Paris SG), all priced 2800 coins. Base attribute ranges: SPE 39–94, ACC 36–95, STA 43–93, STR 41–95, CON 37–95, PAS 36–93, SHO 20–96, TAC 15–94.',
 'High Confidence','Low',['EV-251'],'2026-11-18',
 ['2518 is 2026 update 1 roster only; 20262/20263 and special-event cards add more. Live transfers will shift OVRs over the season'],['CLAIM-006','CLAIM-137','CLAIM-139']),
('CLAIM-142',
 'Vintage/historical "special" cards (special.json) cover Champion (12, vintage years 2004–2018), Classic (24, 1984–2018), Star (23, 2025/2026 rising players), Team-of-Year (11, 2025). Vintage Champion cap is 88 (Ronaldo CF, Messi LW — corroborates EV-248). Team-of-2025 cap 87; Star (2025/26) cap 84.',
 'High Confidence','Low',['EV-251','EV-248','CLAIM-132'],'2026-11-18',
 ['special.json in dls-ext does NOT contain current-event promos (Dynamic Stars, WC Champions/Heroes, Dream Stars, Cult Heroes, Legends) — those live in per-season update files or separate promo sets (EV-252)'],['CLAIM-132','CLAIM-135','CLAIM-144']),
('CLAIM-143',
 'Unlicensed teams/players are present in DLS26 (e.g. Kane listed under "Unlicensed" team at Bayern due to missing Bundesliga license; 367 players in Unlicensed bucket in 20261). Players on unlicensed teams still appear in the game and transfer market, just under the team label "Unlicensed".',
 'Community Consensus','Low',['EV-251'],'2026-11-18',
 ['Cannot confirm which specific teams are unlicensed from this data alone beyond Kane/Bayern; Step 2 should enumerate missing team IDs'],[]),
('CLAIM-144',
 'DLS26 OVR ceiling hierarchy, corrected: base golds cap 86 (EV-251); vintage Champion/Star/Team-of-Year special cards cap 88 (EV-251); current-event promos (Dynamic Stars, WC Heroes, WC Champions, Cult Heroes, Dream Stars, Legends, Team of 2025) cap 96–97; the highest visible cards are the all-time "Champions" endgame tier reaching OVR 98 (Lionel Messi DC Barcelona, Cristiano Ronaldo EI/LW Real Madrid, per Larrycr7aaaa/DLS26-API). CLAIM-006 ("max visible OVR 96 Nico Williams") is upgraded to reflect this 98 ceiling for Champions endgame.',
 'Community Consensus','Medium',['EV-252','EV-251','EV-248'],'2026-11-18',
 ['Larrycr7aaaa data is a single Spanish community snapshot; EV-190 and EV-246 never showed the 98 Messi/Ronaldo Champions — only 96 Nico Williams. Two sources corroborate up to 96; one source (Larrycr7aaaa) pushes to 98; Step 2 APK/assets will resolve. Treat 98 as the reported ceiling until contradicted, not a Confirmed value'],['CLAIM-006','CLAIM-132','CLAIM-142']),
('CLAIM-145',
 'DLS26 OVR is computed as a linear weighted sum of the 8 attributes plus a constant. Best-fit across 2,255 non-GK base cards gives: OVR ≈ 1.86 + 0.225·CON + 0.164·STR + 0.144·SPE + 0.137·ACC + 0.107·PAS + 0.100·SHO + 0.099·TAC + 0.055·STA (MAE 0.37, RMSE 0.46 on base; MAE 0.70 cross-validated on Larrycr7aaaa promo outfield cards). Control (CON) is the highest-weighted attribute; Stamina (STA) is the lowest. For GKs, the two highest weights (≈0.475 each) map onto the columns labelled GKH and GKR in promo data. Position-specific re-weighting is small (top-N average MAE by position was 0.68–1.1 with varying N, vs 0.37 for the single global linear model), implying no strong position-specific OVR curve.',
 'Community Consensus','Medium',['EV-251','EV-252','CLAIM-137','CLAIM-138'],'2026-11-18',
 ['OLS residuals of ±1–3 OVR exist on ~30 players (worst Emegha CF: rate 71 vs pred 74.2, +3.2); possible rounding edge cases, position-specific intercepts, or hidden bonus/malus. Promo cards MAE 0.70 is well within ±1 rounding, supporting the formula but not proving it is the exact in-game calculation. Step 2 disassembly/asset inspection needed to confirm exact weights and rounding'],['CLAIM-137','CLAIM-138','CLAIM-141','CLAIM-144']),
]
for cid,prop,tier,vol,evl,due,chall,cross in new_claims:
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'TrungTaHust/dls-ext 20261 base roster (2518) + special (70) + Larrycr7aaaa/DLS26-API promo (41)','confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':evl,
                   'contradicting_evidence':[],'last_valid_check':'2026-10-18T00:20:00Z','last_attempt':'2026-10-18T00:20:00Z','last_checked_by':'turn-24 github community-DB deep sweep',
                   'next_due':due,'origin_history':[{'at':'2026-10-18','origins':['community-database']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
# Upgrade CLAIM-006 note
by['CLAIM-006']['challenges'].append('Turn-24 EV-252 (Larrycr7aaaa/DLS26-API) reports Champions-tier endgame cards at OVR 98 (Messi DC Barcelona, Ronaldo EI Real Madrid). Existing EV-190/246 max was 96 (Nico Williams Dynamic Stars). CLAIM-144 captures corrected hierarchy; CLAIM-006 remains as "Dynamic Stars cap 96" reference, not overall max.')
# add EV tokens to older claims that are corroborated
for cid,toks in {'CLAIM-078':['EV-251'],'CLAIM-085':['EV-251'],'CLAIM-007':['EV-251'],'CLAIM-060':['EV-251'],'CLAIM-130':['EV-251'],'CLAIM-132':['EV-251','EV-252'],'CLAIM-001':['EV-251'],'CLAIM-094':['EV-251'],'CLAIM-024':['EV-252'],'CLAIM-077':['EV-251']}.items():
    if cid in by:
        for t in toks:
            if t not in by[cid]['supporting_evidence']: by[cid]['supporting_evidence'].append(t)
by={c['claim_id']:c for c in claims}
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
# Build covers from EV metadata
for e in ev:
    e['covers']=sorted(set(e.get('covers',[])),key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)

# Sample 14
random.seed(24)
ev_idx={e['evidence_id']:e for e in ev}
ev_dirs=['docs/continuity/a7e23a6b/evidence/extract','docs/continuity/a7e23a6b/evidence/raw']
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
print(f'SAMPLE 14: OK={ok} WARN={warn} BAD={bad}')
# stamp
ev2=[json.loads(l) for l in open(EIP) if l.strip()]
for e in ev2:
    if e['evidence_id'] in repairs:
        cov=set(e.get('covers',[])); cov|=repairs[e['evidence_id']]
        e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev2)+NL)
print('stamped',len(repairs),'EVs')
b=open(CP,'rb').read()
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev2}
badcov=[(e['evidence_id'],c) for e in ev2 for c in e.get('covers',[]) if c.startswith('CLAIM-') and c not in ids]
miss=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('claims',len(claims),'LF',b.count(b'\n'),'ev',len(ev2),'badcovers',badcov,'miss',miss)
