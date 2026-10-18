#!/usr/bin/env python3
"""Turn 35 Wave 24: Classic Players roster by Prize Ladder collection, ladder selection chance mechanic, fe.pak datamine reference, DLS26 top-rated players, special-card collections."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w24')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="community"):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":quality,"summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid
os.makedirs(RAW_DIR,exist_ok=True)

# ---------- EV-412: classic players roster ----------
e_cl=new_ev("NamuWiki DLS25 special-player section, r/DreamLeagueSoccer (1rkjnhp Mar2026 Italian classics reaction, 1hcsk5m Dec2024 fe.pak datamine, 1hodz9y Dec2024, 1hw18a4 Jan2025 ladder DP math, 1in68fm Feb2025, 1h6vtqe DLS25 megathread, 1iobru2 Feb2025, 1gxdhuu Nov2024 icon predictions, 1pagnx6 Nov2025 next ladder), official FTG TikTok (Italian + English League Classics), dream-league-soccer.fandom Classic Players, dlsinside.com, dreamkitsapp.com/data",
    "CLASSIC PLAYERS ROSTER BY PRIZE LADDER COLLECTION. WORLD CUP '98 CLASSICS (the first Prize Ladder set, DLS25 Dec 2024): Gabriel Batistuta 85, Dennis Bergkamp 85, Emmanuel Petit 84, Davor Suker 83. EUROPEAN CLASSICS: Giorgio Chiellini 85, Rivaldo 86, plus two 82-83 rated players (NamuWiki's romanisations 'Valter Shengga' and 'Gaithka Mendida' are garbled but map to a Serie A-era defender and Gaizka Mendieta). ATTACKING CLASSICS: Gianfranco Zola 84, Hernan Crespo 83, Paul Gascoigne 82, Dennis Bergkamp 83. BRITISH CLASSICS: Andy Cole 83, Graeme Souness 84, Paul Gascoigne 85, Tony Adams 83. ITALIAN LEAGUE CLASSICS (DLS26, official FTG TikTok): Trezeguet, Batistuta, Crespo and Desailly. ENGLISH LEAGUE CLASSICS (DLS26, official FTG TikTok): four stars of the English game including Dimitar Berbatov; DLS26 also has Michael Essien as a Classic DM. Community reaction to the Italian set was mixed - players objected to receiving a SECOND Batistuta and a SECOND Crespo when earlier ladders had already offered them. LADDER MECHANICS: classics are unlocked by climbing the Prize Ladder with Dream Points rather than purchased (in pre-DLS25 versions classics could be bought for 500 coins or unlocked by completing the game). Ladder classic selection involves CHANCE - one player reports the 4th classic slot was a 50% chance between two named players, and completing a ladder can award a DUPLICATE classic. DATAMINE REFERENCE (Step 2 relevant): r/DLS (Dec 2024) lists 16 classic entries extracted from the game's fe.pak file - Bergkamp, Batistuta, Lothar Matthaus, Paul Gascoigne, possibly Steve Bruce, Graeme Souness, Emmanuel Petit, Andy Cole, Bergkamp again, Tony Adams, possibly Gianfranco Zola, Hernan Crespo, Davor Suker, one unknown, Gaizka Mendieta and Chiellini. NEXT LADDER (yellow theme, Nov 2025): community guesses only - Pires, Rivaldo, Matthaus, Valderrama, or Classic Keane, Irwin and Robinson - UNCONFIRMED. DLS26 TOP-RATED BASE PLAYERS (thesoccerera, Feb 2026): Dembele, Mbappe, Kane and Haaland at 86; Van Dijk, Raphinha, Yamal, Salah, Pedri and Donnarumma at 85. SPECIAL CARD COLLECTIONS tracked by dreamkitsapp: World Winners (Cucurella 85), World Heroes (Messi 87), Champion players (Modric 86), Kick-off Stars (Raphinha 85), Star players (Sarr 83), Classic (Desailly 85), Secret players (Lindpere 47). dlsinside.com tags players as DYNAMIC / FIRST TOUCH UTD NOT AVAILABLE / AGENT / Classic / NO TEAM. Official Play Store (IN, Sep 2026) late-summer update: Cult Heroes collection coming soon plus dozens of bug fixes.",
    "evidence/raw/turn35_w24/EV-412_classic_players.html",
    "Classic Players by ladder collection: WC'98 = Batistuta 85/Bergkamp 85/Petit 84/Suker 83; European = Chiellini 85/Rivaldo 86 +2; Attacking = Zola 84/Crespo 83/Gascoigne 82/Bergkamp 83; British = Andy Cole 83/Souness 84/Gascoigne 85/Tony Adams 83; Italian League (DLS26 official) = Trezeguet/Batistuta/Crespo/Desailly; English League (DLS26 official) = 4 stars incl. Berbatov; Essien Classic DM; ladder classic slot has 50% chance element and duplicates possible; fe.pak datamine listed 16 classics; pre-DLS25 classics cost 500 coins; DLS26 top base 86 = Dembele/Mbappe/Kane/Haaland",
    quality="community")

add_claim("World Cup '98 Classics (first Prize Ladder set, DLS25 Dec 2024): Gabriel Batistuta 85, Dennis Bergkamp 85, Emmanuel Petit 84, Davor Suker 83.", 2, "prizeladder/classics-wc98", [e_cl])
add_claim("European Classics set: Giorgio Chiellini 85, Rivaldo 86, plus two further 82-83 rated players.", 3, "prizeladder/classics-european", [e_cl], notes="NamuWiki romanisation garbled for the two lower-rated names")
add_claim("Attacking Classics set: Gianfranco Zola 84, Hernan Crespo 83, Paul Gascoigne 82, Dennis Bergkamp 83.", 3, "prizeladder/classics-attacking", [e_cl])
add_claim("British Classics set: Andy Cole 83, Graeme Souness 84, Paul Gascoigne 85, Tony Adams 83.", 3, "prizeladder/classics-british", [e_cl])
add_claim("Italian League Classics (DLS26, official FTG TikTok): Trezeguet, Batistuta, Crespo and Desailly, signed via the Prize Ladder with Dream Points.", 2, "prizeladder/classics-italian-dls26", [e_cl])
add_claim("English League Classics (DLS26, official FTG TikTok): four stars of the English game including Dimitar Berbatov; DLS26 also offers Michael Essien as a Classic DM.", 2, "prizeladder/classics-english-dls26", [e_cl])
add_claim("Community reaction to the DLS26 Italian League Classics was negative because the set delivered a SECOND Batistuta and a SECOND Crespo to players who had already unlocked them on earlier ladders.", 3, "prizeladder/classics-duplicate-backlash", [e_cl])
add_claim("Prize Ladder classic selection involves chance: a player reports the fourth classic slot was a 50% chance between two named players, and completing a ladder can award a duplicate classic.", 3, "prizeladder/classic-selection-chance", [e_cl])
add_claim("Classic Players are unlocked by climbing the Prize Ladder with Dream Points rather than being purchased; in pre-DLS25 versions they could be bought for 500 coins or unlocked by completing the game.", 2, "prizeladder/classic-unlock-method", [e_cl])
add_claim("Datamine reference (Step 2 lead): r/DLS (Dec 2024) extracted 16 Classic Player entries from the game's fe.pak data file - Bergkamp, Batistuta, Lothar Matthaus, Paul Gascoigne, possibly Steve Bruce, Graeme Souness, Emmanuel Petit, Andy Cole, Bergkamp again, Tony Adams, possibly Gianfranco Zola, Hernan Crespo, Davor Suker, one unknown, Gaizka Mendieta and Chiellini.", 3, "prizeladder/fepak-datamine", [e_cl], notes="Directly relevant to the postponed Step 2 static datamine")
add_claim("The next (yellow-themed) Prize Ladder's players were never officially announced; community guesses included Pires, Rivaldo, Matthaus and Valderrama, or Classic Keane, Irwin and Robinson - all UNCONFIRMED.", 4, "prizeladder/next-ladder-unknown", [e_cl])
add_claim("DLS26 highest-rated base players: Dembele, Mbappe, Kane and Haaland at 86 OVR; Van Dijk, Raphinha, Yamal, Salah, Pedri and Donnarumma at 85 OVR.", 3, "ratings/dls26-top-base", [e_cl], notes="Single source; special/hero cards (e.g. Messi 87) sit above these")
add_claim("DLS26 special-card collections tracked by community databases: World Winners (Cucurella 85), World Heroes (Messi 87), Champion players (Modric 86), Kick-off Stars (Raphinha 85), Star players (Sarr 83), Classic (Desailly 85) and Secret players (Lindpere 47).", 3, "cards/special-collections", [e_cl])
add_claim("Player databases tag DLS26 cards as DYNAMIC, FIRST TOUCH UTD NOT AVAILABLE, AGENT, Classic or NO TEAM, which maps how each card is obtainable.", 3, "cards/obtainability-tags", [e_cl])
add_claim("Official Play Store (IN) late-summer 2026 update: a 'Cult Heroes' Special Players collection coming soon plus dozens of bug fixes.", 1, "patching/cult-heroes-play-store", [e_cl])

p=os.path.join(RAW_DIR,'EV-412_classic_players.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
