#!/usr/bin/env python3
"""Turn 19 fix-ups: register EVD-0005 in the EV index; add EV-245 for CLAIM-095 UGC witness."""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
ED=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
NL=chr(10)
claims=[json.loads(l) for l in open(CP) if l.strip()]
by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
ev_by={e['evidence_id']:e for e in ev}

# Register EVD-0005 if missing
if 'EVD-0005' not in ev_by:
    ev.append({'evidence_id':'EVD-0005','artifact':'evidence/extract/EVD-0005_page_missing_404.md','tool':'fetch-failure-record',
               'origin_method':'official-support (alt slug 360004441177 attempted 2026-10-10)','retrieved_at_utc':'2026-10-10T17:45:00Z',
               'authenticity_limits':'FAILURE RECORD: Zendesk 404 on alt slug; primary slug 214385685 was later captured in full (EV-241).',
               'covers':['CLAIM-100']})
    ev_by['EVD-0005']=ev[-1]

# EV-245 for CLAIM-095 YouTube UGC
ev.append({'evidence_id':'EV-245','artifact':'evidence/extract/EV-245_ugc_world_cup_winners_youtube.md',
           'tool':'ugc-summary','origin_method':'YouTube pack-opening UGC (single video, identified in sibling corpus)',
           'retrieved_at_utc':'2026-10-17T17:45:00Z',
           'authenticity_limits':'SUMMARY-ONLY / UGC: video not preserved; content is the sibling kb L-002 line. Single UGC source ⇒ Speculative ceiling.',
           'covers':['CLAIM-095']})
ev_by['EV-245']=ev[-1]
open(os.path.join(ED,'EV-245_ugc_world_cup_winners_youtube.md'),'w').write(
 '# EV-245 — YouTube pack-opening UGC ("World Cup Winners pack" arrival ~21 Jul 2026)\n\n'
 '**Date:** 2026-10-17T17:45:00Z\n**Authenticity limits:** SUMMARY-ONLY / UGC. Video URL was identified during sibling corpus capture but the video itself was not downloaded to this workspace; the witness is the kb/live-state.md L-002 summary line. Single-source ⇒ Speculative.\n\n'
 '## Summary\n\nPer the imported live-state record, a pack-opening UGC video dated ~21 July 2026 shows a "World Cup Winners pack" alongside a Dynamic Stars final upgrade. Event naming overlaps the World Winners/World Heroes family and is unverified.\n\n## Covers\n- CLAIM-095\n')

by['CLAIM-095']['supporting_evidence']=['EV-245']

# Sort
for e in ev:
    e['covers']=sorted(set(e.get('covers',[])),key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
def ekey(eid):
    pfx,num=eid.split('-'); return (0 if pfx=='EVD' else 1,int(num))
ev.sort(key=lambda e:ekey(e['evidence_id']))
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)

import re
b=open(CP,'rb').read(); print('claims',len(claims),'LF',b.count(b'\n'))
print('ev',len(ev))
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev}
badcov=[(e['evidence_id'],cid) for e in ev for cid in e.get('covers',[]) if cid.startswith('CLAIM-') and cid not in ids]
missing=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('badcovers',badcov); print('missing',missing)
remain=[c['claim_id'] for c in claims if not any(re.findall(r'(?:EV|EVD)-\d{3,4}',s) for s in c.get('supporting_evidence') or [])]
print('remaining no-direct-EV',remain)
