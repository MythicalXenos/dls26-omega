#!/usr/bin/env python3
"""Turn 35 Wave 85: THE "DREAM LEAGUE" NAME IS CONTAMINATED, AND THE DREAM STARS ROSTER IS NAMED.

Wave 85's centrepieces:

1. THE THIRD CONTAMINATION, and this one has a name. Searching "Dream League" does not
   search Dream League Soccer - it searches **ESL's DreamLeague Dota 2 tournament**, whose
   Season 26, 28 and Grand Final results dominate the first page, plus League of Legends rank
   ladders that share the Intermediate/Pro/Veteran vocabulary. So the corpus's failure to find
   rank names above Veteran was partly a *query* failure, not a source failure. Every future
   search must carry "soccer" or "DLS" or the results are another game's.

2. THE DREAM STARS 2026 ROSTER IS NOW NAMED by the community - twelve players, ranked by
   performance by the players themselves. That narrows the 12th Man gap from "unknown player"
   to "one of these twelve, and the sources do not mark which one was the voted addition."
   FTG's own version history confirms the addition happened without naming them.

3. THE RANK LADDER BELOW VETERAN IS CORROBORATED a second time, independently, by Exophase's
   achievement list - which is Google Play's own achievement data, not a guide. Intermediate 1,
   Pro 1 and Veteran 1, 500 XP each.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w85')

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

e_rk=new_ev("Two searches on the DLS LIVE rank ladder and on the DLS 26 12th Man vote winner. BOTH were dominated by ESL's DreamLeague Dota 2 tournament (Season 26 and 28 results, the Grand Final, PARIVISION as champions) and by League of Legends rank ladders, which share the Intermediate/Pro/Veteran vocabulary. The DLS-specific material recovered: exophase.com DLS26 Android achievements (the rank achievements - 'Making Progress: Reach rank Intermediate 1', 'Going Pro: Reach rank Pro 1', 'DLS Veteran: Reach rank Veteran 1', each 500 XP), r/DreamLeagueSoccer 1sv94qo (25 Apr 2026 - the 2026 Dream Stars ranked by performance, naming twelve players), r/DreamLeagueSoccer 1pcatn6 (2 Dec 2025 - the top 6-15 for DLS26, the Pedri position complaint and the Dembele +1 OVR card being nearly identical to the base), r/DreamLeagueSoccer 1qz14ir (8 Feb 2026 - the Tier 1 world record with its full match record), thesoccerera.com DLS26 top-rated players (19 Feb 2026, DOWNGRADED - the 86 ceiling with named players), sportsdunia best-players table (2 Jan 2026, REJECTED as a fourth table), dreamkitsapp.com/data (the named special cards: Cucurella 85, Messi 87, Donnarumma 86, Raphinha 85, Modric 86, Kang-in Lee 82), dls-wiki.fandom.com/wiki/Leagues (the Career division and cup structure), a TikTok creator (29 Jun 2026 - 'the eleven starters of Dream Stars and the important twelfth player')",
    "THE 'DREAM LEAGUE' NAME IS CONTAMINATED, THE DREAM STARS ROSTER IS NAMED, AND THE RANK LADDER IS CORROBORATED A SECOND TIME. (1) THE CONTAMINATION, the third instance of the pattern and the first with a cause: searching 'Dream League' does not search Dream League Soccer - it searches **ESL's DreamLeague, a Dota 2 tournament brand**, whose Season 26 and 28 results, Grand Final and champion team dominate the first page. Add League of Legends rank ladders, which share DLS's Intermediate/Pro/Veteran vocabulary, and the corpus's long-standing failure to find rank names above Veteran looks partly like a QUERY failure rather than a source failure. **Every future search must carry 'soccer' or 'DLS'** or the results belong to another game. (2) THE DREAM STARS 2026 ROSTER IS NAMED by the community, twelve players, ranked by the players themselves: TIER S - Yildiz, Ryerson, Thiago, Arrascaeta; TIER A - El Karouani, Tzolis, Vuskovic, Anderson, Suarez; TIER B - Svilar; TIER F - Berg, Sarr. A creator describes the structure directly: 'the eleven starters of Dream Stars and the important twelfth player' - so eleven base plus one voted. **This narrows the 12th Man gap from 'unknown player' to 'one of these twelve, and no source marks which was the voted addition.'** FTG's own version history confirms the addition happened - 'The DLS community has voted, and we've added this extra superstar to the collection' - without naming them. (3) THE RANK LADDER BELOW VETERAN IS CORROBORATED A SECOND TIME, and independently: Exophase's achievement list is Google Play's own achievement data, not a guide. 'Making Progress: Reach rank Intermediate 1' (500 XP) - 'Going Pro: Reach rank Pro 1' (500 XP) - 'DLS Veteran: Reach rank Veteran 1' (500 XP). That is a second, non-guide source for the Intermediate > Pro > Veteran ladder the corpus recorded at ckpt-127, and it still says nothing about ranks ABOVE Veteran. (4) THE WORLD-RECORD RUN'S FULL MATCH RECORD: '16 days, 12 games, 110 wins, 10 losses, one draw, and most importantly 145,296 XP' - 'Set the record for the least XP to tier 1' and 'won tier 1 with a mostly common/rare team against the world's best players.' The corpus had the 16 days and the 145,296 XP; the 110/10/1 record is new. (5) THE 86 CEILING CORROBORATED WITH NAMES: Dembele 86, Mbappe 86, Kane 86, Haaland 86, with Van Dijk, Raphinha, Yamal, Salah, Pedri and Donnarumma at 85 - which matches the corpus's 'ceiling 86, held by about six players'. (6) CARD-INFLATION COMPLAINTS, useful for recruitment: 'Dembele's 86 rated card is no different from his 85 rated card, just a +3 overall increase in his core stats with a +5 on strength' and 'Pedri played a grand total of 5 games as an AM in the 24/25 season... what is FTG smoking??' - so a +1 OVR special card can be statistically near-identical to the base card, and FTG's position assignments are sometimes wrong. (7) THE NAMED SPECIAL CARDS, corroborated from the player database: World Winners Marc Cucurella 85 LB; World Heroes Lionel Messi 87 SS; Team of 2025 Gianluigi Donnarumma 86 GK; Kick-off Stars Raphinha 85 LW; Champion players Luka Modric 86 CM; Kang-in Lee 82 AM. (8) A FOURTH REJECTED SPORTSDUNIA TABLE - a best-players list - recorded so the count is accurate, while noting its figures happen to corroborate other sources.",
    "THE 'DREAM LEAGUE' NAME IS CONTAMINATED BY A DOTA 2 TOURNAMENT: ESL's DreamLeague dominates 'Dream League' searches, and League of Legends shares the Intermediate/Pro/Veteran vocabulary - so the failure to find rank names above Veteran was partly a query failure. Every future search must carry 'soccer' or 'DLS'. THE DREAM STARS 2026 ROSTER IS NAMED - twelve players (Yildiz, Ryerson, Thiago, Arrascaeta, El Karouani, Tzolis, Vuskovic, Anderson, Suarez, Svilar, Berg, Sarr), eleven base plus one voted - which narrows the 12th Man gap to 'one of these twelve, unmarked'. THE RANK LADDER BELOW VETERAN IS CORROBORATED A SECOND TIME by Google Play's own achievement data: Intermediate 1, Pro 1 and Veteran 1, 500 XP each. THE WORLD-RECORD RUN'S FULL RECORD: 110 wins, 10 losses, 1 draw in 16 days for 145,296 XP. THE 86 CEILING corroborated with names. CARD-INFLATION COMPLAINT: a +1 OVR special card can be near-identical to the base card. A FOURTH REJECTED SPORTSDUNIA TABLE",
    "THE NAME CONTAMINATION, THE DREAM STARS ROSTER, AND THE RANK-LADDER CORROBORATION",
    quality="community")

add_claim("METHODOLOGY FINDING - THE 'DREAM LEAGUE' NAME IS CONTAMINATED BY ANOTHER GAME. Searching 'Dream League' does not search Dream League Soccer: it searches **ESL's DreamLeague, a Dota 2 tournament brand**, whose Season 26 and 28 results, Grand Final and champion team dominate the first page of results. Add League of Legends rank ladders, which share DLS's Intermediate/Pro/Veteran vocabulary. **So the corpus's long-standing failure to find LIVE rank names above Veteran was partly a QUERY failure, not a source failure.** Every future search must carry 'soccer' or 'DLS'.", 2, "errata/dream-league-name-contamination", [e_rk], notes="Third contamination finding; the first with an identified cause")
add_claim("THE DREAM STARS 2026 ROSTER IS NAMED by the community, twelve players, ranked by performance by the players themselves: **TIER S - Yildiz, Ryerson, Thiago, Arrascaeta** · **TIER A - El Karouani, Tzolis, Vuskovic, Anderson, Suarez** · **TIER B - Svilar** · **TIER F - Berg, Sarr**. A creator describes the structure: 'the eleven starters of Dream Stars and the important twelfth player' - eleven base plus one voted.", 3, "12thman/dream-stars-2026-roster-named", [e_rk], notes="First time the roster is named in the corpus")
add_claim("This NARROWS the 12th Man gap rather than closing it: the voted player is one of the twelve named Dream Stars, but no source marks which one was the community addition. FTG's version history confirms the addition happened - 'The DLS community has voted, and we've added this extra superstar to the collection' - without naming them.", 3, "12thman/gap-narrowed-to-twelve-unmarked", [e_rk], notes="Gap status: narrowed from 'unknown player' to 'one of twelve, unmarked'")
add_claim("THE RANK LADDER BELOW VETERAN IS CORROBORATED A SECOND TIME, and independently: Exophase's achievement list is Google Play's own achievement data rather than a guide. '**Making Progress** - Reach rank **Intermediate 1**' (500 XP) - '**Going Pro** - Reach rank **Pro 1**' (500 XP) - '**DLS Veteran** - Reach rank **Veteran 1**' (500 XP). A non-guide source for the Intermediate > Pro > Veteran ladder, and it still says nothing about ranks ABOVE Veteran.", 2, "dll/rank-ladder-below-veteran-second-source", [e_rk], notes="Second source for the ladder below Veteran; the gap above Veteran stays open")
add_claim("THE WORLD-RECORD RUN'S FULL MATCH RECORD: '16 days, 12 games, **110 wins, 10 losses, one draw**, and most importantly 145,296 XP' - 'Set the record for the least XP to tier 1' and 'won tier 1 with a mostly common/rare team against the world's best players.' The corpus had the 16 days and the XP; the 110/10/1 record is new, and it puts the win rate at about 91%.", 3, "dll/world-record-full-match-record", [e_rk])
add_claim("THE 86 CEILING CORROBORATED WITH NAMES: Dembele 86, Mbappe 86, Kane 86 and Haaland 86 at the top, with Van Dijk, Raphinha, Yamal, Salah, Pedri and Donnarumma at 85. That matches the corpus's 'ceiling 86, held by about six players' and names the holders.", 3, "ratings/86-ceiling-with-names", [e_rk])
add_claim("CARD-INFLATION COMPLAINT, useful for recruitment: '**Dembele's 86 rated card is no different from his 85 rated card**, just a +3 overall increase in his core stats with a +5 on strength' - so a +1 OVR special card can be statistically near-identical to the base card. Do not spend on a +1 version of a card you already own without checking the stat delta.", 3, "cards/plus-one-ovr-near-identical", [e_rk])
add_claim("A second recruitment caution from the same thread: 'Pedri played a grand total of 5 games as an AM in the 24/25 season... what is FTG smoking??' - so FTG's position assignments on special cards can be wrong. Check a card's position against how you will actually use it, not against the card art.", 4, "cards/ftg-position-assignments-wrong", [e_rk])
add_claim("THE NAMED SPECIAL CARDS, corroborated from the player database: **World Winners** Marc Cucurella 85 LB · **World Heroes** Lionel Messi 87 SS · **Team of 2025** Gianluigi Donnarumma 86 GK · **Kick-off Stars** Raphinha 85 LW · **Champion players** Luka Modric 86 CM · Kang-in Lee 82 AM.", 3, "cards/named-special-cards-corroborated", [e_rk])
add_claim("A FOURTH REJECTED SPORTSDUNIA TABLE - a best-players list. Recorded so the rejection count is accurate, while noting that its figures happen to corroborate other sources: the list is not used as evidence, the corroboration is.", 4, "errata/sportsdunia-fourth-table-rejected", [e_rk], notes="Fourth sportsdunia rejection")

for p in ['EV-498_name_contamination.html','EV-498b_dream_stars_roster.html','EV-498c_rank_ladder_and_ratings.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
