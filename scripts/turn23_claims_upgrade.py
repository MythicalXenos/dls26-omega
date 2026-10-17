#!/usr/bin/env python3
"""Turn 23: resolve CLAIM-132 champion-88 conflict — EV-187 already corroborates Champion 88 (CR7) and EV-190 lists Ronaldo/Messi 88 among special-card OVRs; FBGD adds a second independent source with multiple cards per player at different rarities. Upgrade the cap claim and reconcile."""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]; eby={e['evidence_id']:e for e in ev}
# Add EV-248 = FBGD detailed parse confirming champion 88 + multi-card-per-player
ev.append({'evidence_id':'EV-248','artifact':'evidence/extract/EV-248_footballgamingbd_multicard_resolution.md','tool':'github-api + local JSON parse','origin_method':'community database deep parse (FootballGamingBD/DLS26_PD)',
           'retrieved_at_utc':'2026-10-17T23:40:00Z',
           'authenticity_limits':'Cross-referenced against dreamkitsapp in EV-187/EV-190 which already list champion CR7 88 and Ronaldo/Messi 88 among special-card OVRs; FBGD adds concrete card roster with slugs and bio text. Two-database agreement.',
           'covers':['CLAIM-132','CLAIM-135','CLAIM-007','CLAIM-060','CLAIM-130']})
eby['EV-248']=ev[-1]
open(os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract/EV-248_footballgamingbd_multicard_resolution.md'),'w').write('''# EV-248 — FBGD multi-card-per-player resolution and champion-88 corroboration
**Date:** 2026-10-17T23:40Z
**Tool:** github-api raw fetch + local JSON parse of logs/research/footballgamingbd/Player.json (+ New_Player/Upcoming_Player), cross-checked against EV-187 (dreamkitsapp player listing) and EV-190 (dreamkitsapp "best players" page).

## Findings

1. **Multi-card-per-player confirmed.** Star players (Messi, Ronaldo, etc.) have MULTIPLE cards in different collections/rarities with distinct OVRs. For example:
   - Cristiano RONALDO: legendary 82 Cf (base-legendary), champion 82 Rm (champion lower variant), **champion 88 Lw** (top Champion card), World Cup Heroes 87 Cf.
   - Lionel MESSI: legendary 83 Ss (base-legendary), champion 84 Rw, **champion 88 Cf** (top Champion card), World Cup Heroes 87 Ss.
   - This explains why prior OVR snapshots (CLAIM-007 Feb-2026 "top OVR 86") reported lower values: they sampled base-legendary cards only.
2. **Champion cards 82–88** (FBGD n=11: champion 82–88 range, not uniform 88). Card-art naming: "champion" cards use "Champion-max/nonmax-card.png" and rating-circle "Max-90-99.png" for ratings 90+ or "Nonmax-80-89.png" for 80–89. OVR 88 is the MAXIMUM observed champion card (Ronaldo/Messi LW/CF at 88); other champions sit at 82–87.
3. **World Cup Heroes 87** for both Messi (SS) and Ronaldo (CF), consistent with EV-190 and CLAIM-130.
4. **Legendary base 80–86** is confirmed (legendary n=167, min 80, max 86 — Yamal/Haaland/Olise/Kane/Dembele at 86).
5. **T26 cards 85–87** (T26 = likely "Team of 2026"): Dembélé/Mbappé/Kane at 87, Hakimi/Pedri/Yamal/Salah at 86. This collection name was previously rendered by dreamkitsapp as "Team of 2025" for 87-tier — likely seasonal (2025 → 2026) renaming per the real-world football calendar.
6. **Bio text for champion cards**: Ronaldo 88 references 2014 Real Madrid Champions League win (tenth title = "La Décima"); Messi 88 has a similar historical-season bio. These are themed "historic season" special cards, not current-form ratings.

## Corroboration with prior EVs
- EV-187 (dreamkitsapp): explicitly lists "Champion players (Cristiano Ronaldo 88 LW PT)" and "Messi 87" under World Heroes.
- EV-190 (dreamkitsapp /best-players/): lists Cristiano Ronaldo 88 (LW/CF PT), Lionel Messi 88 (CF/RW AR) as special cards under team t258.
- FBGD adds the card-level slugs (cristiano-ronaldo-88, lionel-messi-88), popup IDs (popup-ronaldo-88, popup-messi-88), bios, kit filenames (Ronaldo88-C.webp, Messi88-C.webp), and position boxes (Lw.png, Cf.png).
- **Two independent community databases agree on 88 as the current visible OVR cap.** The "87" ceiling in CLAIM-130 was a partial reading (World Heroes variant 87 exists alongside the 88 Champion variant).

## Resolution
- Champion 88 is real and two-source corroborated.
- Base-legendary cap remains 86.
- Dynamic Star 96 from L-001 is an UPGRADED end-of-event card, not the base — base Dynamic Stars are 82 flat (EV-246).
- OBSERVED MAX VISIBLE OVR in any collection is therefore 88 (champion Messi/Ronaldo), with event-upgraded Dynamic Stars reaching 96 (CLAIM-095/L-001 Nico Williams 96, etc. at end-of-event).
''')
# reconcile CLAIM-132 Speculative -> resolved
by['CLAIM-132']['confidence_tier']='High Confidence'
by['CLAIM-132']['proposition']='SPECIAL-CARD OVR CEILING: current visible special cards reach 88 OVR (Champion cards for Cristiano Ronaldo LW 88 PT and Lionel Messi Cf 88 AR), corroborated across two independent community databases (EV-187 dreamkitsapp + EV-190 dreamkitsapp/best-players + EV-246/EV-248 FBGD). Each star player has multiple cards across rarities (e.g. Ronaldo: legendary 82, champion 82, World Cup Heroes 87, champion 88; Messi: legendary 83, champion 84, World Cup Heroes 87, champion 88). Base-legendary cap remains 86; World Cup Heroes cap is 87; event-upgraded Dynamic Stars can reach 96 at end-of-event (L-001 / Nico Williams 96). Prior CLAIM-130 "Messi 87" was the World Cup Heroes variant, not the top Champion.'
by['CLAIM-132']['supporting_evidence']=['EV-248','EV-187','EV-190','EV-246','CLAIM-007','CLAIM-130','CLAIM-095']
by['CLAIM-132']['challenges']=['Both community-database sources are community-tier; in-game or datamined confirmation still owed (Step 2)',
                              'Nico Williams 96 in EV-190 is a MAXED Dynamic Star under the site\'s approximate calculation, not a base card; base Dynamic Stars are 82 (EV-246)',
                              'The "Champion" card name is in English; FTG may label this collection differently in-game']
by['CLAIM-132']['cross_refs']=['CLAIM-007','CLAIM-060','CLAIM-095','CLAIM-130','CLAIM-131']
# fix CLAIM-130 text about Messi 87
by['CLAIM-130']['proposition']='Adjacent special cards observed in build 13.430 (dreamkitsapp via sibling GS-041 + FBGD cross-check, EV-239+EV-248): World Winners — Marc Cucurella LB 85 (ESP); World Heroes — Lionel Messi SS 87 ARG and Cristiano Ronaldo Cf 87 PRT; Kick-off Stars — Raphinha LW 85 (BRA); Champion — Cristiano Ronaldo Lw 88 PT, Lionel Messi Cf 88 ARG (the current visible 88-OVR cap, see CLAIM-132). Messi at 87 is his World Cup Heroes variant; 88 is his Champion variant.'
by['CLAIM-130']['supporting_evidence']=['EV-239','EV-248','CLAIM-007','CLAIM-059','CLAIM-095']
# tighten CLAIM-007
by['CLAIM-007']['proposition']='Base card (non-event, non-special legendary) ratings top out around 86 OVR in current lists (Mbappé/Haaland/Dembélé/Kane/Olise/Yamal cluster at 86); special collections extend higher — Champion cards reach 88 (Messi/Ronaldo, CLAIM-132), World Cup Heroes/Winners 84–87, Dynamic Stars base 82 upgrading to 96 at event end (L-001), Cult Heroes 83–85, Classic 82–86; a community DB enumerates ~14k entries including generics (CLAIM-116) while visible-card PWA lists 1024 (CLAIM-131).'
by['CLAIM-007']['supporting_evidence']=['EV-246','EV-248','EV-001','EV-002','EV-114','CLAIM-132','CLAIM-060','CLAIM-095','CLAIM-131']
# CLAIM-060 (dreamkitsapp provenance) now corroborated by FBGD — note
by['CLAIM-060'].setdefault('challenges',[]).append('Turn-23 EV-248 FBGD cross-check: dreamkitsapp listings for champion-88 cards match FBGD (slugs, bios, filenames agree); the "approximate calculation" disclaimer in EV-190 applies to the MAXED dynamic-star 96s, not the base special-card OVRs.')
# add the new claim: multi-card-per-player structure
def add(cid,prop,tier,vol,ev,due,chall,cross=None):
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'cross-checked community databases (dreamkitsapp + FBGD) 2026-10-17','confidence_tier':tier,
                   'volatility_tier':vol,'supporting_evidence':ev,'contradicting_evidence':[],'last_valid_check':'2026-10-17T23:40:00Z','last_attempt':'2026-10-17T23:40:00Z','last_checked_by':'turn-23 github deep parse',
                   'next_due':due,'origin_history':[{'at':'2026-10-17','origins':['community-database']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
add('CLAIM-135',
    'Star players have MULTIPLE cards across collections/rarities with different OVRs and positions. Example concrete roster from FBGD: Cristiano Ronaldo appears as legendary 82 Cf, champion 82 Rm, World Cup Heroes 87 Cf, and champion 88 Lw; Lionel Messi appears as legendary 83 Ss, champion 84 Rw, World Cup Heroes 87 Ss, and champion 88 Cf. Themed bios (e.g. Ronaldo 88 = 2014 Real Madrid La Décima season) indicate Champion cards are historic-season specials. Consequence: when scouting an opponent or streaming/YT card list, "Messi" or "Ronaldo" without card-type annotation is under-specified; both players appear in 4+ distinct cards with different ratings and positions.',
    'High Confidence','Critical',['EV-248','EV-246','EV-187','EV-190'],'2026-10-20',
    ['Community-database tier; confirm in Step 2',
     'Multiple variants may be event-locked and not simultaneously available; acquisition paths not enumerated here'],
    ['CLAIM-007','CLAIM-132','CLAIM-059','CLAIM-130'])
# sort and write
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
# covers
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-248': cov|={'CLAIM-132','CLAIM-135','CLAIM-007','CLAIM-060','CLAIM-130'}
    if e['evidence_id']=='EV-187': cov|={'CLAIM-132','CLAIM-135'}
    if e['evidence_id']=='EV-190': cov|={'CLAIM-132','CLAIM-135'}
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
b=open(CP,'rb').read()
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev}
bad=[(e['evidence_id'],c) for e in ev for c in e.get('covers',[]) if c.startswith('CLAIM-') and c not in ids]
miss=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('claims',len(claims),'LF',b.count(b'\n'),'ev',len(ev),'badcovers',bad,'miss',miss)
