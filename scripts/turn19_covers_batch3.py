#!/usr/bin/env python3
"""Turn 19 covers back-stamp batch 3 — sample-9 WARNs plus CLAIM-090/EV-102."""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
NL=chr(10)
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={e['evidence_id']:e for e in ev}
adds={'EV-142':['CLAIM-048'],'EV-172':['CLAIM-048'],'EV-174':['CLAIM-059'],'EV-180':['CLAIM-059'],'EV-177':['CLAIM-059'],
      'EV-181':['CLAIM-066'],'EV-182':['CLAIM-066'],'EV-102':['CLAIM-090']}
ch=0
for eid,cids in adds.items():
    if eid not in by: print('MISS',eid); continue
    rec=by[eid]; cov=set(rec.get('covers',[])); b=len(cov)
    for cid in cids: cov.add(cid)
    rec['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
    if len(cov)!=b: ch+=1
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
print('changed',ch)
