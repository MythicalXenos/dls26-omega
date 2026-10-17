#!/usr/bin/env python3
"""Back-stamp covers for sample-15 WARNs."""
import json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if False else '/home/user/dls26-omega'
import os
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl'); NL='\n'
stamps={'EV-185':'CLAIM-053','EV-173':'CLAIM-118','EV-182':'CLAIM-070'}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
for e in ev:
    if e['evidence_id'] in stamps:
        cov=set(e.get('covers',[])); cov.add(stamps[e['evidence_id']])
        e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
print('stamped 3 EVs')
