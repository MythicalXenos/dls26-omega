#!/usr/bin/env python3
"""Turn 30 Wave 6: ad reward specifics; events (World Heroes, TOTY, Champions, Kickoff Stars, Summer Spotlight)."""
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
    c={'claim_id':cid_full,'proposition':prop,'confidence_tier':tier,'supporting_evidence':evr,'challenges':chal or [],'context_build':ctx,'last_checked_by':f'turn 30 wave 6 ({ts})','last_valid_check':ts,'last_attempt':ts,'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),'volatility_tier':vol,'cross_refs':[],'replacements':None,'contradicting_evidence':[]}
    claims.append(c); return cid_full
mc=max_c
def C(prop,tier,evr,chal=None,vol='Low',ctx='DLS26'):
    global mc; mc+=1; return mk_claim(mc,prop,tier,evr,chal,vol,ctx)
e291=mk_ev(max_e+1,'community-web-en (bluestacks free rewards guide; sportsdunia how to get coins DLS26; r/DLS ad issues 2024; r/DLS ad coin amounts 2021)','evidence/raw/community_turn30/EV-291_ads.html',"Ad rewards: post-match 30-sec ad DOUBLES coin earnings for that match (min 30, max ~100 coins per doubled match); home-screen ad button earns 30 coins per view with a DAILY CAP (developers fixed the exploit of relaunching to spam ads; max 30 coins from home-screen ad per 24 hours after fix). Missing a daily login day resets the 20-day login cycle to day 1. Daily scenarios: hard-AI comeback scenarios, 50 coins/day reset.")
e292=mk_ev(max_e+2,'community-web-youtube (DLS 26 NEW EVENT UPDATE! YouTube June 2026); r/DLS DLS Special Events Looking Ahead Jan 2026; r/DLS DLS26 Kickoff Stars maxed Raphinha Dec 2025; fifaworldcupnews July Summer Spotlight; EV-280 press release; r/DLS DLS25 Champions Players)','evidence/raw/community_turn30/EV-292_events.html',"Known DLS25/DLS26 events/promos: Kickoff Stars (DLS26 launch, Dec 2025, e.g. maxed Raphinha 95 Kickoff Stars card); World Heroes Event (announced for July 1, 2026 per YouTube update video); TOTY (Team of the Year) event debut expected in DLS26 (Jan 2026 community speculation); Champions Players promo existed in DLS25; Dynamic Agent Special Draft events tied to Dynamic Stars signings; Summer Spotlight (July 2026, v13.410) — major rating changes (Rare↔Legendary upgrades/downgrades), added Daily Bonus, added Turkish+Arabic commentary. DLS25 Champion Players (predecessor promo template).")
C("Ad reward specifics (DLS26): (1) Post-match 30-second video ad DOUBLES match coin earnings (min 30, max ~100 coins bonus per doubled match). (2) Home-screen ad button gives a flat 30 coins per view with a strict DAILY CAP — developers patched the older exploit of relaunching to grind ads; home-screen ad coin rewards are limited to ~30 coins per 24h (ad availability may also be capped per session).",'Community Consensus',[e291],['Exact daily cap varies by report; post-match ad limit is one per match played.'],vol='Medium')
C("Daily login streak rule: missing a single day resets the 20-day login cycle back to Day 1 (losing accumulated progress toward later, higher-value login rewards).",'High Confidence',[e291])
C("Daily Scenarios mode: daily-challenge mode where user is placed in a losing/comeback situation against Hard AI and must win/come back; awards 50 coins/day, resets every 24h.",'High Confidence',[e291])
C("Confirmed/named DLS26 events/promos to date: (1) Kickoff Stars (launch window Dec 2025, e.g. 95-OVR Raphinha Kickoff Stars card); (2) World Heroes Event (announced start July 1, 2026); (3) Summer Spotlight (July 2026, v13.410, major rating reshuffles Rare↔Legendary, added Daily Bonus reward, added Turkish+Arabic commentary, +new Classic Players expected); (4) Dynamic Agent Special Draft (recurring, for Dynamic Stars signings); (5) TOTY (Team of the Year) event anticipated by community for Jan 2026 (DLS25 introduced 'Champions Players' as a precedent promo). Exact event calendar/rewards still TBD but follows real-world football cadence (TOTY = Jan, Summer Spotlight = pre-season/July, Kickoff = launch/Dec).",'Community Consensus',[e292,'EV-280'],['Promo names/dates largely from community sources; full event calendar not officially published.'],vol='High')
C("Promo/limited-offer 'slightly upgraded' special cards in store are priced ~990 gems (community consensus = poor value; cheaper to buy base player with coins and train via Common coaches).",'Community Consensus',[e292,'EV-286'])
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c)+'\n')
with open(EIP,'w') as f:
    for e in ev: f.write(json.dumps(e)+'\n')
print(f"Added 5 new claims and 2 EVs (EV-291..EV-292). Totals: {len(claims)} claims, {len(ev)} EVs")
