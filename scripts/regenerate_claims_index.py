#!/usr/bin/env python3
"""Regenerate kb/claims_index.md from kb/claims.jsonl (derived view). Handles both the legacy confidence_tier schema and the current integer confidence schema."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
OUT=os.path.join(ROOT,'kb/claims_index.md')

TIER={1:'Confirmed',2:'High Confidence',3:'Community Consensus',4:'Speculative',5:'Disputed'}
LEGACY={'Confirmed':1,'High Confidence':2,'Medium-High Confidence':2,'Medium Confidence':3,'Community Consensus':3,'Low Confidence':4,'Speculative':4}

def conf_of(r):
    if 'confidence' in r:
        c=r['confidence']
        return c if isinstance(c,int) else LEGACY.get(str(c),3)
    return LEGACY.get(r.get('confidence_tier',''),3)

def text_of(r):
    return r.get('text') or r.get('proposition') or ''

recs=[json.loads(l) for l in open(CLAIMS_PATH) if l.strip()]
counts={}
domains={}
for r in recs:
    c=conf_of(r); counts[c]=counts.get(c,0)+1
    d=(r.get('domain') or 'unscoped').split('/')[0]
    domains[d]=domains.get(d,0)+1

n=len(recs)
ev_of={}
for r in recs:
    for e in (r.get('supporting_evidence') or []):
        ev_of.setdefault(e,[]).append(r['claim_id'])

lines=[]
lines.append('# KB — CLAIM INDEX (derived view)')
lines.append(f"Generated mechanically from `kb/claims.jsonl` at {datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}. Do not edit by hand. `kb/claims.jsonl` is the claim authority.")
lines.append(f"Total claims: **{n}**")
dist=' / '.join(f"{TIER[k]} {counts.get(k,0)}" for k in sorted(counts))
lines.append(f"Distribution: {dist}. Volatility: not tracked on the current record schema.")
lines.append(f"Distinct evidence records cited: **{len(ev_of)}**.")
lines.append('')
lines.append('## Domain coverage (top-level)')
lines.append('| Domain | Claims |')
lines.append('| --- | --- |')
for d,c in sorted(domains.items(), key=lambda x:(-x[1],x[0])):
    lines.append(f'| {d} | {c} |')
lines.append('')
lines.append('## Claims')
lines.append('| Claim | Proposition (truncated) | Confidence | Domain | Evidence |')
lines.append('| --- | --- | --- | --- | --- |')
for r in sorted(recs, key=lambda r:(conf_of(r), r['claim_id'])):
    t=text_of(r).replace('|','/').replace('\n',' ')
    if len(t)>150: t=t[:147]+'...'
    evs=','.join(r.get('supporting_evidence') or []) or '-'
    if len(evs)>60: evs=evs[:57]+'...'
    lines.append(f"| {r['claim_id']} | {t} | {TIER[conf_of(r)]} | {r.get('domain') or 'unscoped'} | {evs} |")

with open(OUT,'w') as f:
    f.write('\n'.join(lines)+'\n')
print(f"wrote {OUT}: {n} claims, {len(ev_of)} distinct evidence records")
print("distribution:", dist)
