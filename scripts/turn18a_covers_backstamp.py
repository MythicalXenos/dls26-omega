#!/usr/bin/env python3
"""Turn 18a: back-stamp EV index covers[] for sample-7 WARN claims, plus CLAIM-124/125/129/130
for EV-230/231 which already have covers set but double-check. Also include CLAIM-006/EV-105 fix."""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
NL='\n'
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={e['evidence_id']:e for e in ev}

# required additions: (ev_id -> [claim_ids to add])
adds={
  'EV-150':['CLAIM-108'],
  'EV-192':['CLAIM-065'],
  'EV-162':['CLAIM-065'],
  'EV-185':['CLAIM-065','CLAIM-063'],
  'EV-180':['CLAIM-063'],
  'EV-213':['CLAIM-128'],
  'EV-167':['CLAIM-128'],
  'EV-130':['CLAIM-128'],
}
changed=0
for eid,cids in adds.items():
    if eid not in by:
        print('MISSING EV',eid); continue
    rec=by[eid]
    cov=set(rec.get('covers',[]))
    before=len(cov)
    for cid in cids:
        cov.add(cid)
    rec['covers']=sorted(cov,key=lambda s:int(s.split('-')[1]) if s.startswith('CLAIM-') else 0)
    if len(cov)!=before:
        changed+=1; print('  +',eid,'->',rec['covers'])

with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
print('changed',changed,'records; total ev',len(ev))
