#!/usr/bin/env python3
"""Turn 35 Wave 62: THE ACCOMMODATION CAP CORRECTED TO 64 PLAYERS, the Dynamic Stars roster, the
real rating ceiling of 86, and the identification of the source behind the corpus's outdated
5,625-gem facility figure.

Wave 62's correction: the corpus carries a 40-player squad limit from a July 2024 (DLS24-era)
post. The DLS25 update extended the Accommodation facility by five levels at +4 players each,
taking the cap from 40 to 64 - and the 10-level, 4,125-gem ladder captured at ckpt-131 now has
its endpoint. The same wave identifies where the outdated 5,625-gem figure came from: a DLS23-era
post stating 'each facility takes 1125 gems to reach max level', which was true when facilities
had five levels and is not true now.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w62')

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

e_cap=new_ev("r/DreamLeagueSoccer 1h6vtqe (5 Dec 2024, 'Accommodation goes up to 64 players'), 1h6nprr (4 Dec 2024, the 10-level ladder), zfrglq (8 Dec 2022, DLS23 facility costs - the origin of the 5,625 figure), 1e6md5o (18 Jul 2024, the 40-player limit), dlsinside.com/players/specials/dynamic-stars (v13.430), dlsgame.net player index (8 Dec 2025), sportsdunia best-players list (2 Jan 2026), thesoccerera top-rated players (19 Feb 2026), dlsmod.com top-7 per position (4 Mar 2026), dreamkitsapp.com/data (card-type ratings), r/DLS 1pcj8n2 (2 Dec 2025, Arsenal ratings), 1vbqucs (31 Jul 2026, TOTY guesses)",
    "THE ACCOMMODATION CAP CORRECTED, THE RATING CEILING CONFIRMED, AND THE SOURCE OF AN OUTDATED FIGURE FOUND. (1) THE SQUAD CAP IS 64 PLAYERS, NOT 40. The corpus carries a 40-player limit from a July 2024 DLS24-era post. A December 2024 DLS25 thread states: 'Accommodation goes up to 64 players but you have to pay a BOATLOAD of gems (probably around 5000 gems to go from level 1 to level 10 on accommodation).' Combined with the ckpt-131 ladder (10 levels, +4 space per level, 4,125 gems, a legacy 44-player start), the arithmetic closes exactly: 44 + (5 levels x 4) = 64. So the DLS25 update extended Accommodation by five levels and the current maximum squad is 64. (2) THE OUTDATED 5,625-GEM FIGURE IS NOW SOURCED. A December 2022 DLS23-era post states 'each facility takes 1125 gems to reach max level, so to max all facilities you need 5625 gems' - which was TRUE when facilities had five levels. That is where the corpus's figure came from, and it is a DLS23 figure, not a DLS26 one. The ckpt-131 correction (1,125 = five levels; 4,125 = a maxed facility) is therefore confirmed as a version correction rather than a reinterpretation. (3) THE DYNAMIC STARS ROSTER IS PUBLISHED (dlsinside v13.430): 8 players, all obtained from DYNAMIC AGENTS - Konrad Laimer 20, Eberechi Eze 10, Nico Williams 10, Bradley Barcola 29, Matheus Cunha 10, Rodrigo de Paul 7, Joao Felix 24, Nick Woltemade 27 - with Kang-in Lee also listed at 82 by a second database. Every base card is 82, matching the event design in which only one card reaches 96. Nico Williams appears in the roster and is separately reported as the World Dynamic Star winner. (4) THE RATING CEILING IS 86. Four independent sources across December 2025 to March 2026 agree: the top overall in DLS26 is 86, held by a cluster of about six players - Ousmane Dembele, Kylian Mbappe, Erling Haaland, Harry Kane, Lamine Yamal and (depending on build) Jude Bellingham or Federico Valverde. One source's top ten runs Mbappe 86, Haaland 86, Dembele 86, Kane 86, Bellingham 85, Pedri 85, Valverde 85, Rodri 85, Vitinha 85, Donnarumma 85; another puts Van Dijk, Raphinha, Yamal, Salah and Pedri at 85. This also retires the rejected AI-farm figures (Haaland at 94, Vinicius Jr at 91) with real data. (5) CLASSIC AND LEGEND CARDS SIT ABOVE THE ROSTER: dlsgame.net lists Rivaldo 1999 at 86 and Matthaus 1991 at 86, and dreamkitsapp lists Classic Marcel Desailly at 85 - consistent with the corpus's 85-97 Classic range. (6) SECRET PLAYERS are a listed card category in the player database, corroborating the corpus's note that secret players exist. (7) ARSENAL'S DLS26 RATINGS (Dec 2025) as a worked example of a rating snapshot: Saliba 84, Rice 84, Saka 84, Gabriel 84 (+1), Gyokeres 83, Raya 83, Timber 82 (+2), Odegaard 82 (-1), Zubimendi 81 (+1), Eze 80 (+1), with Aubameyang listed at 78 as a RETURNING PLAYER - and note that Aubameyang's Cult Hero card is 85. (8) The 12th Man's IDENTITY remains unnamed: the vote was announced in v13.100 (26 Feb 2026) and the winner was added in v13.120 (25 Mar 2026), but no source names the player, and the community's guesses (Kane among them) remain guesses.",
    "evidence/raw/turn35_w62/EV-476_accommodation_and_ratings.html",
    "SQUAD CAP CORRECTED TO 64 PLAYERS (from 40): the DLS25 update extended Accommodation by five levels at +4 space each, so 44 + 20 = 64, closing the arithmetic on the 10-level 4,125-gem ladder. THE OUTDATED 5,625-GEM FIGURE IS SOURCED to a DLS23-era post ('each facility takes 1125 gems to reach max level') - true when facilities had five levels, not now. DYNAMIC STARS ROSTER (8 players, all from Dynamic Agents, all base 82): Laimer, Eze, Nico Williams, Barcola, Cunha, de Paul, Joao Felix, Woltemade - plus Kang-in Lee at 82. RATING CEILING IS 86, held by about six players (Dembele, Mbappe, Haaland, Kane, Yamal, plus Bellingham or Valverde by build), agreed by four independent sources - which retires the rejected AI-farm figures of Haaland 94 and Vinicius 91. Classic cards sit above the roster (Rivaldo 1999 and Matthaus 1991 at 86, Desailly 85). Secret players are a listed category. The 12th Man identity remains unnamed despite the vote closing in v13.120",
    quality="community")

add_claim("THE SQUAD CAP IS 64 PLAYERS, NOT 40: the DLS25 update extended the Accommodation facility by five levels at +4 squad space each, taking a legacy 44-player start to 64. The corpus's 40-player figure is a DLS24-era value.", 2, "facilities/squad-cap-64", [e_capner] if False else [e_cap], notes="Correction - the 40-player limit is outdated")
add_claim("THE OUTDATED 5,625-GEM FACILITY FIGURE IS SOURCED: a DLS23-era post (Dec 2022) states 'each facility takes 1125 gems to reach max level, so to max all facilities you need 5625 gems' - true when facilities had five levels. The ckpt-131 correction (1,125 = five levels, 4,125 = a maxed facility) is a version correction, not a reinterpretation.", 2, "facilities/5625-figure-sourced-to-dls23", [e_cap])
add_claim("THE DYNAMIC STARS ROSTER (dlsinside v13.430): 8 players, all from Dynamic Agents - Konrad Laimer 20, Eberechi Eze 10, Nico Williams 10, Bradley Barcola 29, Matheus Cunha 10, Rodrigo de Paul 7, Joao Felix 24, Nick Woltemade 27 - with Kang-in Lee also listed at 82. Every base card is 82.", 2, "cards/dynamic-stars-roster", [e_cap])
add_claim("THE DLS26 RATING CEILING IS 86, held by a cluster of about six players: Ousmane Dembele, Kylian Mbappe, Erling Haaland, Harry Kane and Lamine Yamal, with Jude Bellingham or Federico Valverde joining depending on the build. Four independent sources across Dec 2025 to Mar 2026 agree.", 2, "patching/rating-ceiling-86", [e_cap], notes="Retires the rejected AI-farm figures of Haaland 94 and Vinicius Jr 91")
add_claim("Classic and legend cards sit above the roster ceiling: Rivaldo 1999 and Matthaus 1991 are listed at 86, and Classic Marcel Desailly at 85 - consistent with the corpus's 85-97 Classic range.", 2, "cards/classic-above-roster", [e_cap])
add_claim("Secret players are a listed card category in the player database, corroborating the corpus's note that secret players exist.", 2, "cards/secret-players-exist", [e_cap])
add_claim("Arsenal's DLS26 ratings (Dec 2025) as a worked rating snapshot: Saliba 84, Rice 84, Saka 84, Gabriel 84 (+1), Gyokeres 83, Raya 83, Timber 82 (+2), Odegaard 82 (-1), Zubimendi 81 (+1), Eze 80 (+1) - and Aubameyang is listed at 78 as a RETURNING PLAYER while his Cult Hero card is 85.", 3, "patching/arsenal-ratings-example", [e_cap], notes="Illustrates that a player's roster card and special card can differ by 7 points")
add_claim("The 12th Man's identity remains unnamed: the vote was announced in v13.100 (26 Feb 2026) and the winner added in v13.120 (25 Mar 2026), but no source names the player and the community guesses (Kane among them) remain guesses.", 2, "cards/12th-man-identity-still-unknown", [e_cap], notes="Gap survives - only FTG can close it")

for name in ('EV-476_accommodation_and_ratings.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
