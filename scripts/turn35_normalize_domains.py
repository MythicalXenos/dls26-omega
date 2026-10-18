#!/usr/bin/env python3
"""Turn 35: domain taxonomy normalisation — collapse spelling variants to canonical prefixes so the machine-read line and audits are unambiguous."""
import json, os
ROOT='/home/user/dls26-omega'
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')

# canonical mapping: variant prefix -> canonical prefix
MAP={
 'customisation':'customization',
 'patches':'patching',
 'refereeing':'referee',
 'prize-ladder':'prizeladder',
 'form-boost':'formboost',
 'license':'licensing',
 'seasonpass':'economy/season-pass',
 'iap':'economy/iap',
}

recs=[]
for l in open(CLAIMS_PATH):
    if not l.strip(): continue
    recs.append(json.loads(l))

changed=[]
for r in recs:
    d=r.get('domain')
    if not d: continue
    head,_,tail=d.partition('/')
    if head in MAP:
        new=MAP[head]+(('/'+tail) if tail else '')
        if new!=d:
            r['domain']=new
            changed.append((r['claim_id'],d,new))

tmp=CLAIMS_PATH+'.tmp'
with open(tmp,'w') as f:
    for r in recs: f.write(json.dumps(r)+'\n')
os.replace(tmp,CLAIMS_PATH)

print(f"normalised {len(changed)} domain values")
for cid,old,new in changed: print(f"  {cid}: {old} -> {new}")

from collections import Counter
c=Counter(r['domain'].split('/')[0] for r in recs if r.get('domain'))
dupes=[k for k,v in c.items() if k in MAP]
print("remaining variant prefixes:", dupes or "none")
print("total claims:", len(recs))
