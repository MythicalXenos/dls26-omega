#!/usr/bin/env python3
"""Turn 17: sibling kb sweep. Two new EV records, six new claims from sibling's GS/B items not yet captured here, EV-token integrity verified."""
import json,os,hashlib
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl')
NL=chr(10)
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')

records=[json.loads(l) for l in open(CP) if l.strip()]
by={c['claim_id']:c for c in records}
now='2026-10-17T21:40:00Z'

def challenge_add(cid,txt):
    by[cid].setdefault('challenges',[]).append(txt)

def add(cid,prop,tier,vol,ev,due,chall,cross=None,ctx='cross-branch sibling kb sweep, turn 17; article text not captured — summary provenance'):
    records.append({
      'claim_id':cid,'proposition':prop,'context_build':ctx,
      'confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':ev,
      'contradicting_evidence':[],'last_valid_check':'2026-10-17T17:10:00Z','last_attempt':'2026-10-17T17:10:00Z',
      'last_checked_by':'turn-17 sibling kb sweep',
      'next_due':due,'origin_history':[{'at':'2026-10-17','note':'recorded on sibling branch; merged turn 17','origins':['official-stated']}],
      'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]
    })

# 1) corroboration additions to existing claims (new EVs)
for cid in ('CLAIM-019','CLAIM-023','CLAIM-072'):
    by[cid]['supporting_evidence'].append('EV-230 (cross-branch capture, summary-only)')
    challenge_add(cid,'EV-230 corroborates the offline-exhibition and stable-connection-for-multiplayer statements from the sibling service log; single-sentence summary, no new numeric detail.')
for cid in ('CLAIM-023','CLAIM-035'):
    by[cid]['supporting_evidence'].append('EV-231 (cross-branch capture, summary-only)')
challenge_add('CLAIM-023','EV-231 gives the exact User ID retrieval steps (Options > Advanced > System Info > Copy Info) and frames User ID as a support-handle path, not a public identifier — consistent with existing wording.')
challenge_add('CLAIM-042','GS-037 from the sibling kb clarifies the iCloud-vs-current-games split: legacy DLS19-era games used iCloud (iOS) / Google Play Saved Games (Android) with no cross-platform transfer, while 8 Ball Hero alone uses Facebook; current DLS uses Sign in with Apple/Google. This strengthens the "two systems, different eras" reading of CLAIM-042 rather than contradicting it. EV-225 (cant-update) and EV-167 (older backup article) remain the witnesses.')

# 2) new claims
add('CLAIM-124',
  "Offline modes (official 360003945557): most game modes require an internet connection, mobile or Wi-Fi both work, but Dream League Live (multiplayer) specifically needs a stable connection. Without an active connection, **Exhibition matches remain playable** — that is the only explicitly offline mode named.",
  'Confirmed','Low',['EV-230 (summary-only)','CLAIM-019','CLAIM-023','CLAIM-072'],
  '2027-01-17',
  ['Summary-only witness', 'The article does not say whether other modes (Dream Draft, Scenarios) also work offline; only Exhibition is named'],
  ['CLAIM-019','CLAIM-023','CLAIM-072'])

add('CLAIM-125',
  "User ID retrieval path (official 37082887837202): open DLS → Options (gear, top left) → Advanced → System Info (the \"i\" button) → Copy Info, then paste into a support message. FTG frames User ID as a support handle, not a public identifier. The Terms-of-Use warning is that users are responsible for not loaning, exchanging, sharing, selling or buying game profiles, and that FTG cannot recover accounts lost through such sharing; personal details should not be shared.",
  'Confirmed','Low',['EV-231 (summary-only)','CLAIM-023','CLAIM-035'],
  '2027-01-17',
  ['Summary-only witness', 'This is a procedural prerequisite for Step-3 device-pipeline support, not a gameplay mechanic', 'OBS-013 still forbids making contact until Step 5; the retrieval procedure is recorded now so a lost-account event has a known path'],
  ['CLAIM-023','CLAIM-035','CLAIM-042'])

add('CLAIM-126',
  "VERSION-GAP RESOLUTION (B-009, sibling research): the two apparent gaps in the 2026 version timeline are real periods without a public release, not missing data. APKMirror runs 13.130 (27 Mar 2026) directly to 13.300 (27 May 2026) — corroborated by APKPure, Softonic (old-versions jumps 13.130→13.300), appglint, and TouchArcade listing 13.130 as current with \"Updated: Mar 27, 2026\" — so late-Mar through late-May 2026 (~2 months) had no public update. Between mid-Jul and 20 Aug, APKMirror runs 13.350 (14 Jul) directly to 13.410 (20 Aug) and dlsinside's code table shows code 154 = 13.350 and code 158 = 13.410, meaning version codes 155–157 existed but never shipped publicly (internal/QA builds).",
  'High Confidence','Frozen',['S-20261017-057 (sibling service record, APKMirror/APKPure/Softonic/appglint/TouchArcade/dlsinside)', 'CLAIM-048'],
  '2026-11-17',
  ['The gap resolution is database-corroborated but was produced by the sibling branch; corroboration here consists of the service record for that research, not independent page fetches in this workspace'],
  ['CLAIM-048'])

add('CLAIM-127',
  "Stat display scale (GS-042 sibling observation): dlsinside publishes raw attribute values on a 0–1000 scale (e.g. David Luiz TAC 899 / STR 859 / SPE 789) while in-game cards display ratings on ~0–99. No official conversion formula exists; treat the 0–1000 values as one-decimal-place representations of the displayed value (899 ≈ 89.9). Useful because the underlying per-stat granularity is finer than the displayed OVR — a player showing \"TAC 90\" can vary at the decimal, which matters when two 90s are compared.",
  'High Confidence','Frozen',['S-20261017-057 (sibling service record, dlsinside raw stat pages)','CLAIM-011','CLAIM-060'],
  '2027-01-17',
  ['Arithmetic inference from the database, not official documentation; datamining in Step 2 should confirm the divisor is exactly 10', 'CLAIM-060 already notes dreamkitsapp values are self-declared approximations; dlsinside raw values are presented as database truth, but the 0–1000 ↔ 0–99 mapping is analyst reasoning'],
  ['CLAIM-011','CLAIM-060','CLAIM-080'])

add('CLAIM-128',
  "Save-data backup surface (official 214387685, restated in GS-037 by sibling): FTG's current recommendation is to link the profile to **Sign in with Google** or **Sign in with Apple** (iOS 13.0+), performed MANUALLY through the in-game settings (not automatic). Unlinked profiles carry a no-recovery guarantee after uninstall, device reset, or device change. Save data is NOT secured on Google Play Games or iCloud — those are different cloud services FTG's current games do not use. Legacy games (DLS19 era) used iCloud (iOS) or Google Play Saved Games (Android) with no cross-platform transfer; 8 Ball Hero alone uses Facebook.",
  'Confirmed','Low',['CLAIM-042','CLAIM-072','EV-213','EV-167','EV-130'],
  '2027-01-17',
  ['Sibling GS-037 wording used to consolidate existing claims 042/072; primary evidence remains the existing EV records (EV-167 legacy iCloud article, EV-213/130 current article); no new page was fetched this turn', 'Resolves CLAIM-042 Disputed reading: the two wordings are legacy vs current, not contradictory; downgrade the dispute after user confirms on their device in Step 3'],
  ['CLAIM-042','CLAIM-072','CLAIM-023'])

add('CLAIM-129',
  "Cult Heroes 12-card roster, database-corroborated (GS-039/040 sibling): David de Gea GK 85 (ESP, #1); Paulo Dybala SS/RW 85 (ARG, #10); Pierre-Emerick Aubameyang CF/RW 85 (GAB, #17); Lorenzo Insigne LW/RW 84 (ITA, #24); Hakim Ziyech RW/AM 84 (MAR, #22); Francisco Alarcón (Isco) AM/CM 84 (ESP, #22); Nicolás Otamendi CB 84 (ARG, #30); David Luiz CB/DM 84 (BRA, #30); **Vozinha GK 83** (CPV, #1); Xherdan Shaqiri AM/RW 83 (SUI, #23); Ander Herrera CM/DM 83 (ESP, #21); Daley Blind CB/LB 83 (NED, #17). Example raw stat lines (dlsinside 0–1000 scale): De Gea GKR 850/GKH 800; David Luiz TAC 899/STR 859/SPE 789; Dybala SHO 909/ACC 909/CON 929; Vozinha GKR 814/GKH 812; Herrera STA 910/CON 860. Vozinha 83 is adopted over dreamkitsapp's 84 because dlsinside (with per-stat detail) and dlskiturl independently agree.",
  'High Confidence','Critical',['S-20261017-057 (sibling service record, dreamkitsapp+dlsinside)', 'CLAIM-007','CLAIM-045','CLAIM-046','CLAIM-059'],
  '2026-10-22',
  ['Volatility Critical because special collections rotate; roster is correct for build 13.430 but may change with any event or new collection', 'The dreamkitsapp 84 vs dlsinside/dlskiturl 83 conflict for Vozinha is flagged for datamining confirmation (Step 2)'],
  ['CLAIM-007','CLAIM-045','CLAIM-046','CLAIM-059','CLAIM-127'])

add('CLAIM-130',
  "Adjacent special cards observed in build 13.430 (dreamkitsapp via sibling GS-041, single database): World Winners — Marc Cucurella LB 85 (ESP); World Heroes — Lionel Messi SS 87 (ARG); Kick-off Stars — Raphinha LW 85 (BRA). Messi at 87 is the highest OVR observed in any 2026 special collection so far, which is consistent with the pattern that special cards exceed base ratings (base top ~86 per CLAIM-007). The presence of Cucurella/World Winners corroborates the World-Winners event claim (CLAIM-095) as having shipped in-card, not just as a UGC report.",
  'High Confidence','Critical',['S-20261017-057 (sibling service record, dreamkitsapp)', 'CLAIM-007','CLAIM-059','CLAIM-095'],
  '2026-10-22',
  ['Single database; dlsinside per-player pages were not independently re-checked here for these three cards', 'Volatility Critical — event cards rotate'],
  ['CLAIM-007','CLAIM-059','CLAIM-095','CLAIM-096'])

records.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in records)+NL)
b=open(CP,'rb').read(); print('claims records',len(records),'LF',b.count(b'\n'),'blank',b.count(b'\n\n'),'lit\\n',b.count(b'\\n'))

# EV index append
import io
ev_new=[
 {'evidence_id':'EV-230','artifact':'evidence/extract/EV-230_support_cant_connect.md','tool':'page-render','origin_method':'official-support (360003945557) captured on branch arena/22655f48-dls26-omega','retrieved_at_utc':'2026-10-17T17:10:00Z','authenticity_limits':'SUMMARY-ONLY: body not preserved; content is the sibling branch verbatim service summary','covers':['CLAIM-019','CLAIM-023','CLAIM-072','CLAIM-124']},
 {'evidence_id':'EV-231','artifact':'evidence/extract/EV-231_support_find_user_id.md','tool':'page-render','origin_method':'official-support (37082887837202) captured on branch arena/22655f48-dls26-omega','retrieved_at_utc':'2026-10-17T17:10:00Z','authenticity_limits':'SUMMARY-ONLY: body not preserved; content is the sibling branch verbatim service summary','covers':['CLAIM-023','CLAIM-035','CLAIM-125']},
]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
ids={e['evidence_id'] for e in ev}
for e in ev_new:
    if e['evidence_id'] not in ids:
        ev.append(e)
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
print('ev total',len(ev))

# integrity
import re,glob
ev_files={os.path.basename(p).split('_')[0] for p in glob.glob(os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract/*'))}
unresolved=[]
for c in records:
    for s in c.get('supporting_evidence') or []:
        for t in re.findall(r'(?:EVD|EV)-\d{3,4}',s):
            if t not in ids and t not in ev_files: unresolved.append((c['claim_id'],t))
badcov=[(e['evidence_id'],cid) for e in ev for cid in e.get('covers',[]) if cid.startswith('CLAIM-') and cid not in {r['claim_id'] for r in records}]
print('unresolved',unresolved); print('bad covers',badcov)
import collections; print(collections.Counter(c['confidence_tier'] for c in records))
