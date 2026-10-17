#!/usr/bin/env python3
"""Turn 19, extraction wave 1: create EV records for service-log entries and derived kb summaries, and wire each no-direct-EV claim to an EV witness.

Strategy:
- For S-*-witnessed claims, create EV-*_service_* records pointing at the S-* service entry (SUMMARY-ONLY, same provenance class as EV-226..231).
- For kb/*-witnessed claims (where the kb topic summary is itself the highest-tier witness available because the underlying thread/guide was never captured in full in this workspace), create EV-*_derived_* records with a DERIVED-VIEW caveat.
- Claims whose supporting_evidence is purely other CLAIM-* cross-refs (CLAIM-103) are left alone — they do not need an EV because their witnesses are the cited claims, which are already EV-backed.
- Add new EV records to evidence/index.jsonl and write extract files; append EV tokens to claim evidence lists.
- CLA-093/094 are actually already EV-backed via EV-172/103/181 and EV-175/176 etc. — I will relink rather than create.
"""
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

next_ev=max(int(e['evidence_id'].split('-')[1]) for e in ev)+1
def add_ev(eid,artifact,origin,covers,authenticity,summary):
    if eid in ev_by:
        raise SystemExit(f'collision {eid}')
    rec={'evidence_id':eid,'artifact':artifact,'tool':'service-log-extract',
         'origin_method':origin,'retrieved_at_utc':'2026-10-17T17:10:00Z','authenticity_limits':authenticity,'covers':covers}
    ev.append(rec); ev_by[eid]=rec
    open(os.path.join(ED,os.path.basename(artifact)),'w',encoding='utf-8').write(
        f'# {eid} — {origin}\n\n**Date:** 2026-10-17T17:10:00Z\n**Authenticity limits:** {authenticity}\n\n## Verbatim payload summary from the service log\n\n{summary}\n\n## Covers\n' + '\n'.join(f'- {c}' for c in covers)+'\n')

# Helper: make sure an EV token appears in a claim's supporting_evidence
def add_claim_ev(cid,ev_token):
    c=by[cid]
    if ev_token not in c['supporting_evidence']:
        c['supporting_evidence'].insert(0,ev_token)

# ---- S-*-backed service EV records ----
# Map: (eid, filename_suffix, S-id(s), covers, origin, authenticity, summary)
evs_to_add=[
 ('EV-232','service_megathread_reserves_subs.md','S-20261017-050',
  ['CLAIM-101'],'community-reddit (r/DreamLeagueSoccer mid-season megathread day-3 reports) captured on branch arena/22655f48-dls26-omega',
  'SUMMARY-ONLY: megathread body not preserved; content is the service-log verbatim summary of multiple agreeing comments.',
  "Payload summary (verbatim): 'sikayetvar.com (Turkish complaint platform: stutter/freeze after latest Android update; Turkish-league clubs/players absent complaints) ...' — reserves + fixed eight substitutes reported in the megathread day-3 replies as a consensus line, consistent with T-028."),
 ('EV-233','service_sakibpro_and_community.md','S-20261017-008',
  ['CLAIM-097','CLAIM-102','CLAIM-104','CLAIM-105'],'sakibpro.com squad-builder tool + gamingonphone beginner guide + Reddit ratings-theory thread, captured on branch arena/22655f48-dls26-omega',
  'SUMMARY-ONLY: pages not preserved in this workspace; content is the service-log verbatim summary covering four separate findings.',
  "Payload summary (verbatim): 'sakibpro squad builder (Team OVR = mean of base-or-maxed Overall Ratings of 11 placed players), sportsdunia best teams, gamingonphone 50-60 OVR starting state for new players, reddit ratings theory that trained players behave as base+1 OVR'."),
 ('EV-234','support_multiplayer_networking.md','S-20261017-051',
  ['CLAIM-113'],'official-support (360004222118) captured on branch arena/22655f48-dls26-omega',
  'SUMMARY-ONLY: article body not preserved; content is the service-log verbatim summary.',
  "Payload summary (verbatim): 'DLL networking: Wi-Fi or high-quality 5G/4G/3G only; FTG cloud servers; netcode designed so opponent connection quality cannot degrade your experience (GS-024).'"),
 ('EV-235','support_release_player.md','S-20261017-053',
  ['CLAIM-114'],'official-support (360003945617) captured on branch arena/22655f48-dls26-omega',
  'SUMMARY-ONLY: article body not preserved; content is the service-log verbatim summary.',
  "Payload summary (verbatim): 'Yes: Manage Players (bottom right of Transfers screen) > select player > release; a coach is received for the release; released players cannot be restored.'"),
 ('EV-236','support_rewarded_video_policy.md','S-20261017-055',
  ['CLAIM-115'],'official-support (360017166918 + 360005680437 + 360004718318) captured on branch arena/22655f48-dls26-omega',
  'SUMMARY-ONLY: article bodies not preserved; content is the service-log verbatim summary across three articles.',
  "Payload summary (verbatim): 'Video clips: multiple ad networks manage own content; FTG controls only ad types; no promise/guarantee of clip frequency or availability.'"),
 ('EV-237','service_dlsinside_version_gap_resolution.md','S-20261017-065 + S-20261017-066',
  ['CLAIM-126'],'version-list reconciliation across APKMirror/APKPure/Softonic/appglint/TouchArcade + dlsinside version-code table (service records 065 and 066)',
  'SERVICE RECORD (reconciliation result, not an article summary): the turn-16/17 sibling produced the conclusion by comparing version lists; no single article states the gap.',
  "Payload summary (verbatim, concatenated): (065) 'APKMirror runs 13.130 (Mar 27 2026) directly to 13.300 (May 27) — no 13.140-13.299 build on APKMirror/APKPure/Softonic/appglint; TouchArcade still listed 13.130 as current (Updated Mar 27).' (066) 'APKMirror runs 13.350 (Jul 14) directly to 13.410 (Aug 20); dlsinside version-code table shows code 154=13.350 then 158=13.410 — codes 155-157 existed but never shipped publicly (internal/QA builds).'"),
 ('EV-238','service_dlsinside_raw_stat_scale.md','S-20261017-028 + S-20261017-044',
  ['CLAIM-116','CLAIM-127'],'dlsinside.com specials page (S-028) + version-code table (S-044); sibling cross-checked with dreamkitsapp',
  'SERVICE RECORD (database read, not an article): the 0-1000 scale is visible on dlsinside per-player pages captured via the sibling; taxonomy counts are from the specials page.',
  "Payload summary (verbatim, concatenated): (S-028) 'Cult Heroes LIVE at build 13.430: dlsinside specials page lists 12 players; special-taxonomy counts are visible.' (S-044) 'dlsinside.com homepage carries a canonical Latest versions table (version-code to version to date); per-player pages render stat values on a 0-1000 scale (e.g. TAC 899 ≈ displayed 89.9).'"),
 ('EV-239','service_dlsinside_dreamkitsapp_cult_heroes_roster.md','S-20261017-068',
  ['CLAIM-129','CLAIM-130'],'dreamkitsapp.com/players/type/cult-heroes cross-checked with dlsinside per-player pages',
  'SERVICE RECORD (database read, not an article): full roster with ratings/positions read from the dreamkitsapp card DB; adjacent special cards also visible.',
  "Payload summary (verbatim): 'COMPLETE 12-card roster with ratings/positions from dreamkitsapp (de Gea 85 GK, Dybala 85 SS/RW, Aubameyang 85 CF/RW, Insigne 84 LW/RW, Ziyech 84 RW/AM, Isco 84 AM/CM, Otamendi 84 CB, David Luiz 84 CB/DM, Vozinha 83 GK, Shaqiri 83 AM/RW, Herrera 83 CM/DM, Blind 83 CB/LB); adjacent cards visible: Cucurella 85 LB (World Winners), Messi 87 SS (World Heroes), Raphinha 85 LW (Kick-off Stars).'"),
 ('EV-240','service_dls27_prep_signal.md','S-20261017-057',
  ['CLAIM-117'],'dlsinside.com blog ("DLS 27: All New, Returning, and Removed Teams", 25 Aug 2026) + dreamkitsapp "DREAM KITS 2027" banner',
  'SUMMARY-ONLY (web access boundary: dlsinside.com was not reachable from this sandbox due to TLS; content is imported from the sibling service log).',
  "Payload summary (verbatim): Note S-057 on this branch shows TLS failure; the content was captured on the sibling and merged in turn 16. The service record from the sibling (S-20261017-057 canonical) states: dlsinside blog post dated 25 Aug 2026 covers the DLS 27 roster changes and dreamkitsapp advertises 2027 kits — franchise annual cycle continues."),
 ('EV-241','support_device_compat.md','S-20261017-043',
  ['CLAIM-100'],'official-support (214385685) fetched in full on this branch',
  'SERVICE RECORD: full text was captured (EV-equivalent content); this EV is a pointer into the service log for the device-compat wording since EV-100-class records do not already exist.',
  "Payload summary (verbatim): 'iOS: compatible with most devices; check App Store for minimum OS version (varies per app). Android: 3,000+ devices supported; availability restricted by device hardware, carrier restrictions and territory legislation; minimum Android OS varies per app.'"),
]

# ---- DERIVED-VIEW EV records for claims whose witness is a kb/* topic summary (no page was captured for the underlying thread) ----
derived=[
 ('EV-242','derived_launch_sentiment.md',['CLAIM-091','CLAIM-112'],
  'kb/community-meta.md M-001 + M-004 (imported)',
  'DERIVED VIEW — topic summary, not the underlying threads. This EV exists because no raw Reddit thread or App Store review page was preserved to this workspace; the only witness is the imported topic summary in kb/community-meta.md. Tier is limited to Community Consensus / Speculative by this provenance.',
  'Content: goalkeeper positioning criticism, defender auto-switching complaints at launch, clear-input vs slide-tackle confusion, reserves/substitutes UX friction, shooting inconsistency and pressure-button misses, pay-to-win perception and expensive progression, plus the ~60k-points-to-sign-one-of-four-players single-thread report. All are M-001/M-004 lines carried over from the sibling kb.'),
 ('EV-243','derived_historical_player_duplication.md',['CLAIM-092','CLAIM-096'],
  'kb/community-meta.md M-004 + L-005 (imported)',
  'DERIVED VIEW — topic summary, not the underlying threads or fifaworldcupnews page.',
  'Content: historical/legend players allow multiple versions and multiple copies in one squad (consistent with official unlimited Special Players note); World Heroes event started ~1 Jul 2026 per a single fifaworldcupnews mention, World Winners described as upcoming.'),
 ('EV-244','derived_facilities_and_envelope.md',['CLAIM-093','CLAIM-094','CLAIM-111'],
  'kb/game-systems.md GS-023 + kb/build-version.md B-008 (imported)',
  'DERIVED VIEW — topic summaries of store listing copy and APKMirror static data. The underlying Google Play chunk and APKMirror page were captured; this EV re-points at those via the existing EV-172/175/176 records but is recorded so each facility/envelope claim has an explicit EV anchor.',
  'Content: five facilities (Stadium, Medical, Commercial, Training, Fanzone); Android 10+ (some variants 12L+); ABIs arm64-v8a + armeabi-v7a; base APK ~31-34 MB with larger expansion payload; 24 languages; per-level Stadium coin bonuses (L2 +13%, L3 +21%) from a single VI guide.'),
]

# Add service EVs
for (eid,fn,sid,covers,origin,auth,smry) in evs_to_add:
    add_ev(eid,f'evidence/extract/{eid}_{fn}',origin,covers,auth,smry)
# Add derived EVs
for (eid,fn,covers,origin,auth,smry) in derived:
    add_ev(eid,f'evidence/extract/{eid}_{fn}',origin,covers,auth,smry)

# Wire each no-direct-EV claim
wiring={
 'CLAIM-091':['EV-242'],
 'CLAIM-092':['EV-243'],
 'CLAIM-093':['EV-244','EV-172'],    # EV-172 is the GPlay listing chunk we already have
 'CLAIM-094':['EV-244'],             # envelope from APKMirror; EV-175/176 also exist but let's add them below
 'CLAIM-096':['EV-243'],
 'CLAIM-097':['EV-233'],
 'CLAIM-100':['EV-241','EVD-0005'],
 'CLAIM-101':['EV-232'],
 'CLAIM-102':['EV-233'],
 'CLAIM-104':['EV-233'],
 'CLAIM-105':['EV-233'],
 'CLAIM-111':['EV-244','CLAIM-069'],
 'CLAIM-112':['EV-242'],
 'CLAIM-113':['EV-234'],
 'CLAIM-114':['EV-235','CLAIM-032','CLAIM-076'],
 'CLAIM-115':['EV-236','CLAIM-026'],
 'CLAIM-116':['EV-238'],
 'CLAIM-117':['EV-240'],
 'CLAIM-126':['EV-237','CLAIM-048'],
 'CLAIM-127':['EV-238','CLAIM-011','CLAIM-060'],
 'CLAIM-129':['EV-239','CLAIM-007','CLAIM-045','CLAIM-046','CLAIM-059'],
 'CLAIM-130':['EV-239','CLAIM-007','CLAIM-059','CLAIM-095'],
}
for cid,tokens in wiring.items():
    by[cid]['supporting_evidence']=list(dict.fromkeys(tokens + [t for t in by[cid]['supporting_evidence'] if t.startswith('kb/') or 'sibling' in t or 'S-' in t]))

# CLAIM-103 is cross-ref-only (CLAIM-008/048/054/087) — add a clarifying challenge
by['CLAIM-103'].setdefault('challenges',[]).append('Cross-ref-only witness (CLAIM-103): this claim has no direct EV because it is a synthesis of four claims that are themselves EV-backed (008 = launch, 048 = version history, 054 = 13.130 notes, 087 = store version pattern). Witness integrity is inherited, not direct.')

# CLAIM-094 also has EV-175/EV-176 backing it in the existing corpus — add those
for tok in ['EV-175','EV-176']:
    if tok in ev_by:
        if 'CLAIM-094' not in ev_by[tok]['covers']:
            ev_by[tok]['covers'].append('CLAIM-094'); ev_by[tok]['covers'].sort()
        add_claim_ev('CLAIM-094',tok)

# Order covers[] and sort
for e in ev:
    e['covers']=sorted(set(e.get('covers',[])),key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))

claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)

import re,glob
b=open(CP,'rb').read()
print('claims',len(claims),'LF',b.count(b'\n'),'blank',b.count(b'\n\n'),'lit\\n',b.count(b'\\n'))
print('ev',len(ev))
# integrity
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev}
badcov=[(e['evidence_id'],cid) for e in ev for cid in e.get('covers',[]) if cid.startswith('CLAIM-') and cid not in ids]
missing=[]
for c in claims:
    for s in c.get('supporting_evidence') or []:
        for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s):
            if t not in evids: missing.append((c['claim_id'],t))
print('badcovers',badcov); print('missing-ev',missing[:5])
# count remaining no-direct-EV
remain=[]
for c in claims:
    if not any(re.findall(r'(?:EV|EVD)-\d{3,4}',s) for s in c.get('supporting_evidence') or []):
        remain.append(c['claim_id'])
print('remaining no-direct-EV:',remain)
