#!/usr/bin/env python3
"""Turn 18b: second batch of covers[] back-stamps from sample-8 WARN list. Also patch CLAIM-007 EV list to reflect reality: EV-001/EV-002 are #ds-1/#ds-2 anchors in evidence/raw/search_digest_turn1.md, not broken; covers-lag only."""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CP=os.path.join(ROOT,'kb','claims.jsonl')
NL='\n'
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={e['evidence_id']:e for e in ev}
adds={
  'EV-171':['CLAIM-073'],
  'EV-183':['CLAIM-057'],
  'EV-184':['CLAIM-057'],
  'EV-218':['CLAIM-088'],
  'EV-219':['CLAIM-088'],
  'EV-140':['CLAIM-034'],
  'EV-192':['CLAIM-064'],
  'EV-186':['CLAIM-061','CLAIM-007'],
  'EV-187':['CLAIM-061'],
  'EV-189':['CLAIM-007'],
  'EV-190':['CLAIM-007'],
  # EV-001/EV-002 already cover CLAIM-004/006 per their index; add 007 if not there
  'EV-001':['CLAIM-007'],
  'EV-002':['CLAIM-007'],
}
ch=0
for eid,cids in adds.items():
    if eid not in by:
        print('MISSING',eid); continue
    rec=by[eid]
    cov=set(rec.get('covers',[])); before=len(cov)
    for cid in cids: cov.add(cid)
    rec['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
    if len(cov)!=before:
        ch+=1; print('  +',eid,'adds',cids,'total',len(cov))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
print('changed',ch)
# add a clarifying challenge to CLAIM-007 about EV-001/002 anchors
claims=[json.loads(l) for l in open(CP) if l.strip()]
for c in claims:
    if c['claim_id']=='CLAIM-007':
        c.setdefault('challenges',[]).append(
            "Sample 8 false-positive: EV-001 and EV-002 are valid #ds-1/#ds-2 anchors inside evidence/raw/search_digest_turn1.md (they reference search-result snippets from turn 1), not broken file references. Sample-8 integrity script flagged them as 'no file found' because its anchor-matching looked for lowercase '#ev-001' while the anchor label is '#ds-1' (listed in index.jsonl artifact field).")
        break
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
import hashlib
b=open(CP,'rb').read(); print('claims',len(claims),'LF',b.count(b'\n'),'blank',b.count(b'\n\n'))
