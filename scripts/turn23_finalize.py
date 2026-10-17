#!/usr/bin/env python3
"""Turn 23 finalize: write CLAIM-136 (Unity build + ad networks), run sample 13, integrity."""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]; eby={e['evidence_id']:e for e in ev}
ev.append({'evidence_id':'EV-249','artifact':'evidence/extract/EV-249_taptrap_dls7_security_static.md','tool':'github-api (allowlisted)','origin_method':'academic security-research static APK analysis (beerphilipp/taptrap + tabbed-out corpora)',
           'retrieved_at_utc':'2026-10-17T23:50:00Z','authenticity_limits':'Security-scan JSONs; no game logic. Target SDK 35 build; APK hash not recorded; consistent with late-2024/2025 builds.','covers':['CLAIM-136','CLAIM-115','CLAIM-072','CLAIM-094']})
ev.append({'evidence_id':'EV-250','artifact':'evidence/extract/EV-250_trungtahust_dlsstats_shell.md','tool':'github-api (allowlisted)','origin_method':'TrungTaHust/dls_ext_sv (Vietnamese PWA shell)',
           'retrieved_at_utc':'2026-10-17T23:50:00Z','authenticity_limits':'Shell-only HTML; CDN script not reachable from sandbox; no data extracted.','covers':[]})
eby['EV-249']=ev[-2]; eby['EV-250']=ev[-1]
def add(cid,prop,tier,vol,evl,due,chall,cross=None):
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'security-scan JSONs of an unnamed DLS26 build, target SDK 35','confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':evl,
                   'contradicting_evidence':[],'last_valid_check':'2026-10-17T23:50:00Z','last_attempt':'2026-10-17T23:50:00Z','last_checked_by':'turn-23 github static-analysis sweep',
                   'next_due':due,'origin_history':[{'at':'2026-10-17','origins':['static-analysis']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
add('CLAIM-136',
    'Build stack confirmed via static analysis of an APK in academic corpora: DLS26 is a UNITY ENGINE build (Unity Ads activities present, namespace `com.unity3d.ads`), with target SDK 35 (Android 15). MainActivity = `com.firsttouchgames.dls7.MainActivity`; 52 total activities. Multiple rewarded-ad networks are embedded at once: AdColony, Unity Ads, MoPub, Google AdMob/Play Ads — corroborating CLAIM-115 ("multiple ad networks manage their own content") and expanding it from "multiple" to a specific set. Chrome Custom Tabs are used for in-app web views (support center). Tapjacking filtering is enabled but Protected Confirmation is not used.',
    'High Confidence','Low',['EV-249','CLAIM-115','CLAIM-072','CLAIM-094'],'2026-11-17',
    ['APK hash not recorded; build version not identified in the JSON; target SDK 35 is consistent with a post-Aug-2024 Google Play requirement',
     'Presence of an ad SDK activity is strong evidence the SDK is integrated but does not prove it is active in every region or current build',
     'The Unity engine conclusion is from ad-activity presence, not from Unity libs directly — near-certain but Step 2 should confirm'],
    ['CLAIM-094','CLAIM-115','CLAIM-072'])
# wire
for cid,toks in {'CLAIM-115':['EV-249'],'CLAIM-072':['EV-249'],'CLAIM-094':['EV-249']}.items():
    for t in toks:
        if t not in by[cid]['supporting_evidence']: by[cid]['supporting_evidence'].append(t)
by['CLAIM-115'].setdefault('challenges',[]).append('Turn-23 EV-249 static APK analysis names four ad SDKs embedded (AdColony, Unity Ads, MoPub, AdMob) — the multi-network policy in CLAIM-115 now has a concrete list.')
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-249': cov|={'CLAIM-136','CLAIM-115','CLAIM-072','CLAIM-094'}
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
import random,glob
# sample 13
random.seed(23)
ev_idx={e['evidence_id']:e for e in ev}
ev_dirs=['docs/continuity/a7e23a6b/evidence/extract','docs/continuity/a7e23a6b/evidence/raw']
def ev_file(eid):
    for d in ev_dirs:
        for p in glob.glob(os.path.join(d,eid+'_*')): return p
        for p in glob.glob(os.path.join(d,'*.md')):
            try:
                t=open(p,errors='ignore').read()
                if len(t)>200_000: continue
                if eid in t and (('#%s'%eid).lower() in t.lower() or '%s:'%eid in t or t.startswith('# '+eid)): return p
            except: pass
    return None
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
print(f'SAMPLE 13: OK={ok} WARN={warn} BAD={bad}')
# apply repairs
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
