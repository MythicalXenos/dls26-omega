#!/usr/bin/env python3
"""Turn 22: add new claims EV-246/247 from GitHub sweep. Then integrity check."""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL=chr(10)
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
eby={e['evidence_id']:e for e in ev}

def add_ev(eid,artifact,origin,covers,auth):
    if eid in eby: return
    ev.append({'evidence_id':eid,'artifact':artifact,'tool':'github-api (allowlisted host)','origin_method':origin,
               'retrieved_at_utc':'2026-10-17T23:25:00Z','authenticity_limits':auth,'covers':covers})
    eby[eid]=ev[-1]

add_ev('EV-246','evidence/extract/EV-246_footballgamingbd_player_db.md',
       'community database (FootballGamingBD/DLS26_PD, card-creator web-app PWA, last push 2026-10-12)',
       ['CLAIM-131','CLAIM-133','CLAIM-007','CLAIM-129','CLAIM-130','CLAIM-059'],'SINGLE COMMUNITY DATABASE not corroborated against dlsinside/dreamkitsapp per record; treat as Community-High at best until cross-checked.')
add_ev('EV-247','evidence/extract/EV-247_dls26_china_cb_coach_dp.md',
       'community tool (LeoH321/dls26-tool-CB, DLS26China WeChat public-account single-file coach DP)',
       ['CLAIM-134','CLAIM-104','CLAIM-105','CLAIM-091'],
       'SINGLE COMMUNITY TOOL encoding a reverse-engineered model; mechanics are Community Consensus with unusually strong specificity but NOT confirmed until Step-2 datamining.')

# cover updates to existing EVs / claims
for cid in ['CLAIM-007','CLAIM-129','CLAIM-130','CLAIM-059','CLAIM-104','CLAIM-105','CLAIM-091']:
    pass  # will wire below

def add_claim(cid,prop,tier,vol,ev_list,due,chall,cross=None):
    records={'claim_id':cid,'proposition':prop,'context_build':'community databases and tools fetched via api.github.com 2026-10-17','confidence_tier':tier,
             'volatility_tier':vol,'supporting_evidence':ev_list,'contradicting_evidence':[],
             'last_valid_check':'2026-10-17T23:25:00Z','last_attempt':'2026-10-17T23:25:00Z','last_checked_by':'turn-22 github sweep',
             'next_due':due,'origin_history':[{'at':'2026-10-17','note':'fetched via api.github.com in turn 22 reopen of Step 1','origins':['community-database','community-tool']}],
             'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]}
    claims.append(records); by[cid]=records

add_claim('CLAIM-131',
 "Card-roster distribution from the FootballGamingBD card-creator database (snapshot 2026-10-12): visible/special cards total 1024 — Rare 695 (70-79), legendary 167 (80-86), Dynamic 40 (base 82 flat), Classic 36 (82-86), Cult 24 (83-85), champion 11 (82-88), Dream Star 2026 11 (82-84), T26 10 (85-87), Dream Star 2025 10 (83-84), World Cup Heroes 8 (84-87), World Cup Winners 8 (84-87), Season Pass Player 4 (82-85). Position-box filenames use: Gk, Rw, Lw, Cb, Lb, Rb, Cm, Am, Dm, Lm, Rm, Cf, Ss, St, Cd (CDM). Team list 212 club sides.",
 'High Confidence','Critical',
 ['EV-246','CLAIM-059','CLAIM-007','CLAIM-129'],'2026-10-20',
 ['Community database; does NOT include the 7000+ Hidden/Exclusives/base generic pool that CLAIM-116 counted from dlsinside',
  'Counts and OVR ranges reflect a visible-card snapshot, not the full in-game card pool',
  'T26 label may stand for "Team of 2026" — name unconfirmed (dreamkitsapp uses "Team of 2025")'],
 ['CLAIM-007','CLAIM-059','CLAIM-116','CLAIM-129'])

add_claim('CLAIM-132',
 "POTENTIAL CONFLICT — champion card ceiling: FootballGamingBD lists two champion cards (RONALDO Lw, MESSI Cf) at OVR 88, which is one point higher than the Messi 87 previously observed from dreamkitsapp (CLAIM-130/GS-041). If the FootballGamingBD ratings are correct, the ceiling for champion cards is 88, not 87, and Messi/Ronaldo have 88 champion cards distinct from their 87 World Cup Heroes cards. If dreamkitsapp is correct, FootballGamingBD has an over-rating error. Flagged for Step 2 datamining.",
 'Speculative','Critical',
 ['EV-246','CLAIM-130','CLAIM-060','CLAIM-007'],'2026-10-20',
 ['Two-database conflict; do not upgrade any advice to rely on 88 until a third source or the APK confirms',
  'The two Messi/Ronaldo entries may be duplicates or double-counted cards — verify in the raw JSON'],
 ['CLAIM-007','CLAIM-059','CLAIM-130','CLAIM-060'])

add_claim('CLAIM-133',
 "Coach-application mechanic model (Chinese-community DP tool, DLS26China): technical coaches grant +1/+2/+3 stat points depending on rarity (Common/White/Rare/Blue/Legendary/Gold = +1/+2/+3). Each use picks k=rarity stats UNIFORLY AT RANDOM from the eligible (non-maxed) stat pool of the coach category, and COSTS capacity = sum(stat_weight for selected stats) × rarity. Stat cap is 100; capped stats leave the pool. For TECHNICAL coaches the observed weights are CON weight 2, PAS/SHO/TKL weight 1 each (defender-focused tool). Over-capacity applications produce fractional stat gain (gainedStat = remaining_cap / sumWeight). The target-stat strategy is a combinatorial gamble, not directed training. Recorded as a high-specificity community model; Step-2 must verify.",
 'Community Consensus','High',
 ['EV-247','CLAIM-008','CLAIM-104','CLAIM-105','CLAIM-091'],'2026-10-20',
 ['Single community tool; reverse-engineered, not official',
  'Only technical-coach defender case modeled; fitness/GK/special coach weights unknown',
  'Fractional over-cap allocation is the most speculative line',
  'CLAIM-105 (trained = base+1) is partially wrong per this model — +1 is common-coach single-stat behaviour, not a universal rule'],
 ['CLAIM-008','CLAIM-091','CLAIM-104','CLAIM-105','CLAIM-123'])

# Wire EV tokens to existing claims that EV-246/247 corroborate
for cid,evs in {'CLAIM-007':['EV-246'],'CLAIM-129':['EV-246'],'CLAIM-130':['EV-246'],'CLAIM-059':['EV-246'],
                'CLAIM-104':['EV-247'],'CLAIM-105':['EV-247'],'CLAIM-091':['EV-247']}.items():
    c=by[cid]
    for e in evs:
        if e not in c['supporting_evidence']: c['supporting_evidence'].append(e)
by['CLAIM-105'].setdefault('challenges',[]).append("Turn-22 Chinese-community DP tool (EV-247) shows coaches grant +1/+2/+3 points depending on rarity, not a flat +1; the '+1' theory likely observed only common-coach single-stat outcomes. Tier remains Speculative; mechanic model updated by CLAIM-133.")
by['CLAIM-104'].setdefault('challenges',[]).append("Turn-22 EV-247 corroborates the weighted-progression intuition but gives a different weight table (CON 2, PAS/SHO/TKL 1 for technical coaches on defenders) from sakibpro's percentage model. Both models are community; Step-2 datamining adjudicates.")

# Re-sort and write
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
# EV index: covers[] updated for new EVs already; ensure new claims are in existing EV covers
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-246':
        for c in ['CLAIM-131','CLAIM-132','CLAIM-007','CLAIM-129','CLAIM-130','CLAIM-059']: cov.add(c)
    if e['evidence_id']=='EV-247':
        for c in ['CLAIM-133','CLAIM-104','CLAIM-105','CLAIM-091']: cov.add(c)
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)

# integrity
import glob
b=open(CP,'rb').read(); print('claims',len(claims),'LF',b.count(b'\n'),'blank',b.count(b'\n\n'))
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev}
badcov=[(e['evidence_id'],cid) for e in ev for cid in e.get('covers',[]) if cid.startswith('CLAIM-') and cid not in ids]
miss=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('ev',len(ev),'badcovers',badcov,'missing',miss)
