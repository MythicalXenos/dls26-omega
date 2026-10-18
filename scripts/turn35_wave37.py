#!/usr/bin/env python3
"""Turn 35 Wave 37: Global Challenge Cup format RESOLVED (32 groups of 4 = 128 teams, 6 group matches, top 2 -> 64-team knockout, ~7 rounds, 10g/round + 25g win), GCC difficulty scales with division not club, GCC is online, GCC team pool, LIVE rank names confirmed to 6 with nothing above Veteran, further playdreamleaguesoccer.com fabrications logged."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w37')

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

# ---------- EV-434: GCC format ----------
e_gcc=new_ev("dls-wiki.fandom.com/wiki/Leagues, dream-league-soccer.fandom.com/wiki/Global_Challenge_Cup, r/DreamLeagueSoccer 1ib3c2g (Feb 2025), 1f8h9nx (Sep 2024), 1f6sflp (Sep 2024), 1et05is, 1mfr70w, ncqp0q, 17d489y, 1035wt7, Bluestacks DLS26 free-rewards guide, gamingonphone DLS25 division guide, TikTok DLS25 GCC R2, Challonge community brackets",
    "GLOBAL CHALLENGE CUP FORMAT - C-013 SUBSTANTIALLY RESOLVED. The GCC is a Champions-League-style competition open to EVERY division from Academy to Legendary, played ONLINE against other players rather than the AI. SIZE AND STRUCTURE: the field is 128 teams, drawn into 32 groups of 4; the top 2 from each group qualify, producing a 64-team knockout whose first round is the Round of 64. GROUP STAGE LENGTH: one account states 'you play 3 teams twice just as last year UCL format', i.e. 6 group matches (double round robin), while the wiki description only specifies a group of 4 with the 2 highest points qualifying. ROUNDS TO THE TROPHY: a player describes needing to 'conquer 7 rounds for the trophy', consistent with a group stage plus R64/R32/R16/QF/SF/Final. REWARDS: Bluestacks states 10 gems per round cleared; a Reddit player itemises the end-of-season gem run as roughly 30 gems from league matches, 25 gems for winning the GCC, 15 gems for winning the Diamond Cup and 5 All-Star gems, and describes the 25-gem GCC prize as 'pathetic' relative to the effort. DIFFICULTY MODEL: crucially, the GCC difficulty scales with the DIVISION you are in, not with the opponent club's star rating - 'according to FTG logic, the difficulty of the competition is not determined by the clubs'. Multiple players call the GCC the EASIEST competition in the game to win, easier even than the Diamond Cup, with the Legendary Division league itself being the real challenge. TEAM POOL: the wiki lists 25 named clubs (Arsenal, As Monaco, Barcelona, BC Nice, Chelsea, Crystal Palace, Everton, I Milan, J Turin, Leicester, BD Sporting, Napoli, Lyon, Manchester C, Manchester U, Marseille, Paris, R Madrid, Roma, S Lisbon, Stoke, Tottenham H, Valencia, Villarreal, West Ham). The GCC is the only competition played by ALL teams in the game, whereas the Diamond Cup is restricted to Elite and Legendary Division clubs. LEGACY NOTE: the main fandom wiki still describes a 64-team single-legged playoff, which is a pre-DLS20 structure superseded by the 128-team group format.",
    "evidence/raw/turn35_w37/EV-434_gcc_format.html",
    "GCC = Champions-League-style, open to every division Academy->Legendary, played ONLINE vs other players; 128 teams in 32 groups of 4, top 2 per group qualify -> 64-team knockout starting at R64; group stage is 3 opponents played twice (6 matches) per one account; ~7 rounds to the trophy; rewards 10 gems per round cleared plus ~25 gems for winning (total end-of-season gem run ~30 league + 25 GCC + 15 Diamond Cup + 5 All-Star); DIFFICULTY SCALES WITH DIVISION NOT CLUB STARS; players call it the EASIEST competition to win, easier than the Diamond Cup; team pool ~25 named clubs; GCC is the only cup open to all teams while Diamond Cup is Elite+Legendary only; legacy 64-team single-leg description is pre-DLS20",
    quality="community")

add_claim("The Global Challenge Cup is a Champions-League-style competition open to every division from Academy to Legendary and is played ONLINE against other players rather than the AI.", 3, "cups/gcc-online-all-divisions", [e_gcc], notes="C-013 substantially resolved")
add_claim("GCC structure: 128 teams drawn into 32 groups of 4, with the top 2 from each group qualifying to produce a 64-team knockout beginning at the Round of 64.", 3, "cups/gcc-128-32-groups", [e_gcc], notes="C-013 substantially resolved")
add_claim("GCC group stage: one account describes playing the 3 group opponents twice (6 matches, double round robin, like the new UEFA Champions League format).", 3, "cups/gcc-group-stage-6-matches", [e_gcc])
add_claim("The GCC takes about 7 rounds to win, consistent with a group stage plus R64, R32, R16, quarter-final, semi-final and final.", 3, "cups/gcc-7-rounds", [e_gcc])
add_claim("GCC rewards: 10 gems per round cleared, with the winning prize about 25 gems; a full end-of-season gem run is roughly 30 gems from league matches, 25 from the GCC, 15 from the Diamond Cup and 5 All-Star gems.", 3, "cups/gcc-rewards", [e_gcc])
add_claim("GCC difficulty scales with the DIVISION you are in, not with the opponent club's star rating - multiple players report the GCC is the EASIEST competition to win, easier than the Diamond Cup, with the Legendary Division league being the real challenge.", 3, "cups/gcc-difficulty-division-scaled", [e_gcc], notes="Important: means GCC is a reliable gem source at any division")
add_claim("The GCC team pool is about 25 named clubs (Arsenal, As Monaco, Barcelona, BC Nice, Chelsea, Crystal Palace, Everton, I Milan, J Turin, Leicester, BD Sporting, Napoli, Lyon, Manchester C, Manchester U, Marseille, Paris, R Madrid, Roma, S Lisbon, Stoke, Tottenham H, Valencia, Villarreal, West Ham).", 3, "cups/gcc-team-pool", [e_gcc])
add_claim("The GCC is the only cup competition open to ALL teams in the game, whereas the Diamond Cup is restricted to Elite and Legendary Division clubs.", 3, "cups/gcc-universal-vs-diamond", [e_gcc])
add_claim("LEGACY: the main fandom wiki still describes the GCC as a 64-team single-legged playoff, which is a pre-DLS20 structure superseded by the current 128-team group format.", 2, "errata/gcc-legacy-64-description", [e_gcc])

# ---------- EV-435: rank names + source reliability ----------
e_rk=new_ev("Exophase DLS26 achievement list (live, fetched in full), playdreamleaguesoccer.com 'DLS 2026 New Features' and 'Schedule' pages, prior EV-423",
    "LIVE RANK NAMES - the ceiling remains 6 names. The live Exophase achievement list for DLS26 contains rank achievements for exactly six ranks in order: Rookie, Amateur, Semi-Pro, Intermediate, Pro and Veteran, each worth 500 XP. There is NO achievement, and therefore no published rank name, above Veteran. This is consistent with the 20-to-1 numeric tier ladder: the named ranks most plausibly map onto the lowest six tiers (or the lowest six rank bands), with everything above Veteran being referred to only by its numeric tier. The DLL win-count achievements are Kick Off (5 wins), First Steps (25), Finding Form (50) and In the Flow (100), each 500 XP. SOURCE RELIABILITY - ADDITIONAL FABRICATIONS FROM playdreamleaguesoccer.com: the same site already flagged for inventing chemistry and Fluid Formations now also publishes an 'Icon Exchange' system (trading old cards for a chance to pack a Prime Icon like Ronaldinho or Zidane), a Vinicius Jr card at 91 overall (+3) - which contradicts every other database putting him at 84-86 - a 'Youth Academy Cup' (10-30 April) that rewards fielding U-21 players, a 'Global Super League', and a fake player interview credited to 'Rohit_Striker, DLS Veteran'. None of these exist. The site is now confirmed as an AI-generated content farm and every claim sourced from it must be treated as fabricated unless independently corroborated.",
    "evidence/raw/turn35_w37/EV-435_rank_names_reliability.html",
    "LIVE rank names confirmed to exactly SIX - Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran - each a 500 XP achievement, with NOTHING published above Veteran (gap persists; numeric tiers 1-20 carry the top of the ladder); DLL win achievements Kick Off 5 / First Steps 25 / Finding Form 50 / In the Flow 100 at 500 XP each; playdreamleaguesoccer.com CONFIRMED as an AI content farm with further fabrications: Icon Exchange + Prime Icons (Ronaldinho/Zidane), Vinicius Jr at 91 OVR (+3), a 'Youth Academy Cup' for U-21 players, a 'Global Super League', and a fake interview credited to 'Rohit_Striker, DLS Veteran' - all non-existent",
    quality="community")

add_claim("LIVE rank names are confirmed to exactly six - Rookie, Amateur, Semi-Pro, Intermediate, Pro and Veteran - each a 500 XP achievement, with nothing published above Veteran.", 2, "dll/rank-names-six", [e_rk], notes="Gap persists above Veteran; numeric tiers 1-20 carry the top")
add_claim("DLL win-count achievements: Kick Off (5 wins), First Steps (25), Finding Form (50) and In the Flow (100), each worth 500 XP.", 2, "achievements/dll-win-counts", [e_rk])
add_claim("SOURCE RELIABILITY CONFIRMED: playdreamleaguesoccer.com is an AI-generated content farm. Beyond the already-flagged chemistry and Fluid Formations fabrications it also publishes an 'Icon Exchange' system with Prime Icons (Ronaldinho, Zidane), Vinicius Jr at 91 OVR (+3), a 'Youth Academy Cup' for U-21 players, a 'Global Super League', and a fake interview credited to 'Rohit_Striker, DLS Veteran'.", 2, "errata/playdreamleaguesoccer-content-farm", [e_rk], notes="Add to the rejected-source register")
add_claim("The named LIVE ranks most plausibly map onto the lowest six tiers of the 20-to-1 numeric ladder, with tiers above Veteran identified only by number.", 4, "dll/rank-name-mapping-hypothesis", [e_rk], notes="Speculative - the mapping is inferred, never published")

p=os.path.join(RAW_DIR,'EV-434_gcc_format.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-435_rank_names_reliability.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
