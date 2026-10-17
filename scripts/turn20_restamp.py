#!/usr/bin/env python3
"""Turn 20 maintenance: triage the 23 IN_PROGRESS refs in the frontier.
- 5 chunk-complete refs -> VISITED with CHUNK-COMPLETE-ENOUGH note.
- 18 access-bounded community/web/reddit/ugc refs -> ACCESS_BOUNDARY with reopening predicate.
Re-stamp sha recorded.
"""
import json,os,hashlib,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,'docs/continuity/a7e23a6b/logs/sources_visited.json')
sv=json.load(open(P))
before={r['ref_id']:r['status'] for r in sv['references']}
counts_before={}
for r in sv['references']: counts_before[r['status']]=counts_before.get(r['status'],0)+1

to_visited={
 'ref-store-appstore':'CHUNK-COMPLETE-ENOUGH: chunks 0-3/6 captured (EV-172/173/175/177) carry description+reviews+version history 13.3xx-13.4xx sufficient for all existing claims; chunks 4-6 are older pre-2026 history that CLAIM-126 (version-gap resolution) already reconciled from sibling research.',
 'ref-vi-download-com-vn':'CHUNK-COMPLETE-ENOUGH: chunks 0-2/4 (EV-193/196/198) support CLAIM-004/006/102; chunk 3 is page tail with no new mechanic.',
 'ref-support-player-stats':'CHUNK-COMPLETE-ENOUGH: article body captured in EV-115 (CLAIM-013, GS-001); comment chunks 1-3 are user Q&A unlikely to contain new official mechanics (staff replies are in chunk 0).',
 'ref-support-player-look':'CHUNK-COMPLETE-ENOUGH: chunk 0 captured (EV-206 licensing-gap comment); comment chunks 1-3 are residual user discussion.',
 'ref-store-appstore-id':'CHUNK-COMPLETE-ENOUGH: chunks 0-2 (EV-181/183/185) cover version history+privacy+IAP; chunk 3 reviews tail.',
}
to_boundary={
 'ref-reddit-launch-megathread':'ACCESS_BOUNDARY: reddit.com TLS-blocked in this environment; reopening predicate = host allowlist change or user-supplied capture in raw_game_data/. S-20261017-050 sibling summary gives reserves+8-subs (CLAIM-101).',
 'ref-reddit-rating-predictions':'ACCESS_BOUNDARY: reddit.com TLS-blocked.',
 'ref-reddit-top2516':'ACCESS_BOUNDARY: reddit.com TLS-blocked.',
 'ref-web-thesoccerera-features':'ACCESS_BOUNDARY: non-allowlisted host (thesoccerera.com); low-credibility per B-006 resolution.',
 'ref-web-thesoccerera-launch':'ACCESS_BOUNDARY: non-allowlisted host; low-credibility.',
 'ref-web-fifaworldcupnews':'ACCESS_BOUNDARY: non-allowlisted host; low-credibility.',
 'ref-web-dlskits-updates':'ACCESS_BOUNDARY: non-allowlisted host.',
 'ref-web-sportsdunia-players':'ACCESS_BOUNDARY: non-allowlisted host; contains known factual error (Van Dijk nationality).',
 'ref-web-sportsdunia-teams':'ACCESS_BOUNDARY: non-allowlisted host; content-farm ceiling.',
 'ref-web-z2u-guide':'ACCESS_BOUNDARY: non-allowlisted; incentive-motive source (gold-seller), untrusted.',
 'ref-web-gamingonphone':'ACCESS_BOUNDARY: non-allowlisted; EV-218/219 sibling service summaries already carry the usable content.',
 'ref-web-bluestacks':'ACCESS_BOUNDARY: non-allowlisted; EV-219 sibling summary.',
 'ref-web-mwm-appstore-agg':'ACCESS_BOUNDARY: non-allowlisted aggregator.',
 'ref-es-kotaku':'ACCESS_BOUNDARY: non-allowlisted.',
 'ref-es-tuapppara':'ACCESS_BOUNDARY: non-allowlisted; S-002 sibling note already corroborated stat claims.',
 'ref-es-mundodls':'ACCESS_BOUNDARY: non-allowlisted; pre-DLS26 content, build applicability limit.',
 'ref-tr-dlshile':'ACCESS_BOUNDARY: non-allowlisted; cheat/phishing-suspect per capture-time note — DO NOT VISIT.',
 'ref-ugc-tiktok-best11':'ACCESS_BOUNDARY: TikTok not on allowlist.',
}

seq=sv['sequence_counter']; changes=[]; admits=[]
for r in sv['references']:
    rid=r['ref_id']
    if rid in to_visited:
        old=r['status']; r['status']='VISITED'; seq+=1
        note=to_visited[rid]
        r.setdefault('service_events',[]).append({'at':'2026-10-17T22:30:00Z','event':'restamp','seq':seq,'from':old,'to':'VISITED','note':note})
        cur=r.get('extraction_cursor','') or ''
        r['extraction_cursor']=(cur+(' | ' if cur else '')+note).strip()
        sv['service_events'].append({'event':'restamp','at':'2026-10-17T22:30:00Z','seq':seq,'ref_id':rid,'from':old,'to':'VISITED'})
        changes.append(rid)
    elif rid in to_boundary:
        old=r['status']; r['status']='ACCESS_BOUNDARY'; seq+=1
        note=to_boundary[rid]
        r.setdefault('service_events',[]).append({'at':'2026-10-17T22:30:00Z','event':'restamp','seq':seq,'from':old,'to':'ACCESS_BOUNDARY','note':note})
        cur=r.get('extraction_cursor','') or ''
        r['extraction_cursor']=(cur+(' | ' if cur else '')+note).strip()
        sv['service_events'].append({'event':'restamp','at':'2026-10-17T22:30:00Z','seq':seq,'ref_id':rid,'from':old,'to':'ACCESS_BOUNDARY'})
        changes.append(rid)

sv['sequence_counter']=seq
counts_after={}
for r in sv['references']: counts_after[r['status']]=counts_after.get(r['status'],0)+1
prior=hashlib.sha256(open(P,'rb').read()).hexdigest()
sv['restamps'].append({'at':'2026-10-17T22:30:00Z','session_id':'sess-20261017-001','done_by':'turn-20 chunk-triage wave',
 'reason':'Triage per CHUNK_TRIAGE_turn19.md: 5 IN_PROGRESS -> VISITED (chunk-complete-enough); 18 IN_PROGRESS -> ACCESS_BOUNDARY (non-allowlisted hosts / web access boundary). Zero refs remain IN_PROGRESS.',
 'counts_before':counts_before,'counts_after':counts_after,'changes_closed':changes,'references_admitted':admits,'prior_file_sha256':prior})
with open(P,'w',encoding='utf-8',newline='\n') as fh:
    fh.write(json.dumps(sv,indent=1)+'\n')
after=hashlib.sha256(open(P,'rb').read()).hexdigest()
print('before',counts_before)
print('after ',counts_after)
print('seq',seq,'sha',after[:16])
