#!/usr/bin/env python3
"""Turn 30 Wave 9: APK/package metadata (version, size, requirements)."""
import json,os,datetime
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
max_c=max(int(c['claim_id'][6:]) for c in claims)
max_e=max(int(e['evidence_id'][3:]) for e in ev if e['evidence_id'].startswith('EV-'))
ts=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
def mk_ev(eid,origin,artifact,summary):
    eid_full=f'EV-{eid:03d}'
    ev.append({'evidence_id':eid_full,'origin_method':origin,'artifact':artifact,'captured_at':ts,'covers':[],'summary':summary,'extracted_from':origin})
    return eid_full
def mk_claim(cid,prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    cid_full=f'CLAIM-{cid:03d}'
    c={'claim_id':cid_full,'proposition':prop,'confidence_tier':tier,'supporting_evidence':evr,'challenges':chal or [],'context_build':ctx,'last_checked_by':f'turn 30 wave 9 ({ts})','last_valid_check':ts,'last_attempt':ts,'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),'volatility_tier':vol,'cross_refs':[],'replacements':None,'contradicting_evidence':[]}
    claims.append(c); return cid_full
mc=max_c
def C(prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    global mc; mc+=1; return mk_claim(mc,prop,tier,evr,chal,vol,ctx)
e300=mk_ev(max_e+1,'official-store (Google Play com.firsttouchgames.dls7; APKPure; AppBrain; mokoweb; liteapks)','evidence/raw/official_turn30/EV-300_apk_metadata.html',"DLS26 technical metadata (Sep 2026): Package = com.firsttouchgames.dls7 (same since DLS20, annual seasonal updates). Current version = 13.430 (Sep 16 2026 update; also 13.420 seen, 13.410 = July Summer Spotlight, 13.310 = May 28 update referenced). APK size ~185-200 MB (199.9 MB APKPure; 185.97 MB AppBrain). Minimum Android = Android 10+ (API 29) per APKPure Sep 2026 (older sources say 5.0/6.0/7.0 — appears to have been raised). iOS App Store listing id1462911602. Content rating 13+ (Apple) / Everyone (Google Play). Contains ads + IAP + loot boxes. APK architecture armeabi-v7a (32-bit ARM). OBB folder path: Android/obb/com.firsttouchgames.dls7/ (older DLS/dls3 path referenced in mod community; for dls7 the OBB location is same pattern). Google Play listing since Dec 2019 (initially as DLS20, updated annually through DLS26).")
C("DLS26 package identifiers: Android = com.firsttouchgames.dls7 (same package since DLS20; seasonal updates delivered as app updates, NOT new installs); iOS App Store id = 1462911602.",'Confirmed',[e300,'EV-280'])
C("Current version (Sep 14-16 2026): v13.430. Version progression confirmed so far: 13.030 (late 2025/launch era); 13.310 (May 28 2026, Summer Spotlight AI changes); 13.410 (July 2026, Summer Spotlight rating refresh + Daily Bonus + TR/AR commentary); 13.420 (Sep 1 2026); 13.430 (Sep 14 2026, latest).",'High Confidence',[e300,'EV-296'],['Minor patch versions (hotfixes) between these may not be captured.'],vol='Medium')
C("APK download size: ~185-200 MB (AppBrain 185.97 MB; APKPure 199.9 MB). Additional space required for install/cache/OBB. Architecture: armeabi-v7a (32-bit ARM primary build).",'High Confidence',[e300])
C("Minimum OS requirement: Android 10+ (API 29) per APKPure Sep 2026 listing. Older 3rd-party APK host sites claim Android 5/6/7 compatibility — appears minimum OS was raised at some point; treat Android 10+ as the current requirement.",'Medium Confidence',[e300],vol='Medium')
C("Content ratings: Apple App Store = 13+ (frequent contests, contains loot boxes, advertising); Google Play = Everyone. Both stores note presence of ads and in-app purchases (including random items = loot boxes).",'High Confidence',[e300,'EV-288'])
C("OBB (asset data) folder path: Android/obb/com.firsttouchgames.dls7/ (follows standard Android OBB pattern; older DLS23 used com.firsttouchgames.dls3 but DLS24+ use dls7). Installing modified APKs requires placing OBB contents correctly or the game crashes at launch.",'Community Consensus',[e300],['Mod-community source; to be confirmed during device pipeline.'],vol='Medium')
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c)+'\n')
with open(EIP,'w') as f:
    for e in ev: f.write(json.dumps(e)+'\n')
print(f"Added 6 new claims and 1 EV (EV-300). Totals: {len(claims)} claims, {len(ev)} EVs")
