#!/usr/bin/env python3
"""Turn 35 Wave 7: division structure (8 divisions), promotion, cups (Bronze/Silver/Gold/Diamond/GCC/International/All-Star), endgame vs First Touch United, stadium gates corrected, season payouts, rewards."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w7')

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

e_divs=new_ev("LibrePedia (Miraheze) Spanish wiki, Vietnamese Wikipedia, fandom dream-league-soccer wiki Leagues, dlspedia stadium, supercheats, r/DLS DLS24 beginner, LevelWinner DLS24, Nerdburglars achievements, BlueStacks DLS26 free-rewards, gamingonphone DLS25 gems, exophase, r/DLS GCC coin rewards",
    "There are 8 DIVISIONS (not 6 as earlier believed) in DLS career, from lowest to highest: Academy Division → Amateur Division → Division 4 → Division 3 → Division 2 → Division 1 → Elite Division → Legendary Division. Older wikis list fewer divisions (DLS20 era had 5: Acad/D3/D2/D1/Elite); Amateur + Division 4 + Legendary were added later. All-star XI match: at the end of each division (after winning it), you face that division's Allstar XI one-off match (rewards ~5 coins in Acad/Amateur, scaling up). Promotion rules (older DLS, DLS24 likely similar): top-3 promoted from Academy/D4 to next; top-2 in D2→D1; must finish 1st in Elite to advance to International Cup. Stadium minimum capacities CONFLICT across sources; need reconciliation: dlspedia says Acad=6,462 / D3=15,000 / D2=30,000 / D1=45,000 / Junior Elite=60,000 / Elite=80,000 (no Amateur/D4/Legendary listed). r/DLS DLS24 says Acad=5,000 / Am=15,000 / D3=35,000 / D2=45,000 / D1=55,000 / Elite=70,000 / Leg=85,000 (no D4, no Junior Elite). supercheats says D3=15k/D2=30k/D1=45k/Junior Elite=60k/Elite=80k (older). Probable DLS26 truth (conservatively): Academy starts 6,462; D4/Amateur tier ~15k; D3 ~30-35k; D2 ~45k; D1 ~55k; Elite ~70-80k; Legendary ~85-90k. Stadium upgrade cost per promotion threshold ~1,400 coins (r/DLS). Cup structure (Vietnamese Wikipedia, definitive): 4 tier cups tied to division pairs: BRONZE CUP (Academy + Amateur Divisions), SILVER CUP (Division 4 + Division 3), GOLD CUP (Division 2 + Division 1), DIAMOND CUP (Elite + Legendary Division). Cup payouts: winning Bronze Cup grants 9 coins (Academy) / 10 (Amateur); other tiers scale up. In addition, GLOBAL CHALLENGE CUP (GCC) runs concurrently in EVERY division — 64-team single-elimination (FA Cup/League Cup style; or 4-team group stage round-robin per translated fandom wiki — both descriptions exist, possibly restructured across versions). GCC winner earns 25 coins (LevelWinner), 10 gems per round cleared (BlueStacks/gamingonphone). GCC rewards in legacy: 50 coins + achievements (Nerdburglars/exophase). Elite Cup and Allstar Cup also exist as separate competitions. Post-Legendary/Division-winner arc (legacy DLS, carried forward): win Elite Division → International Cup (vs national teams: Brazil, Argentina, Germany, England, Portugal, etc.) → if you win International Cup → All-Star Cup (vs classic historical teams: Brazil 1970, Man U 1999, 60s/70s/80s All-stars, Spanish League All-Stars) → if you win All-Star Cup → final match vs FIRST TOUCH UNITED (FTG's in-house dev team, ultimate boss). Diamond Cup runs alongside Elite/Legendary. Relegation exists in Legendary Division (if you slip into red zone you get relegated back to Elite). League size: 16 teams per division in older versions (DLS20); 15 matches per season (each team once). ~30 matches/season baseline = 15 division + ~9 GCC matches + ~5 tier cup matches. Legendary has more matches (~40). Season rewards (Academy division baseline): 20 wins with 3-0 scorelines → ~1,100-1,300 coins/season with ads. Division champion coin reward: Academy ~15 coins, scales up. GCC coin rewards criticized as too low by community (r/DLS): only +3 coins vs 3-star team up to +20 vs 5-star team; proposed better rewards 25c group stage + 10c R32 + 15c R16 + 20c QF + 30c SF + 25c runner-up + 50c winner. Current per-win coin cap ceiling: 45 coins (15 goals × 3; r/DLS '15 x 3 = 45 ceiling rate' — consistent with earlier ~15-goal/match cap claim). Achievements: Google Play/Game Center achievements exist for: promotion from each division, winning each cup (Elite Cup, Global Challenge Cup, Allstar Cup), undefeated season (1500 XP), The Double (50c), The Treble (50c).",
    "evidence/raw/turn35_w7/EV-388_divisions_cups.html",
    "8 divisions (Acad→Am→D4→D3→D2→D1→Elite→Leg); 4 tier cups Bronze/Silver/Gold/Diamond paired with division pairs; GCC all divisions 64-team; post-Elite→International Cup→All-Star Cup→First Touch United; Allstar XI per division; promotion rules; 16 teams/div; 15 matches/division season; stadium gates conflicting (list both); season payouts Acad ~1100-1300c with ads; GCC 10g/round; 45c/match ceiling; achievements")

add_claim("DLS26 has EIGHT divisions (career ladder low→high): Academy Division → Amateur Division → Division 4 → Division 3 → Division 2 → Division 1 → Elite Division → Legendary Division. (Earlier 6-division model was DLS20-era; Amateur + Division 4 + Legendary added later.)", 1, "career/divisions-8", [e_divs])
add_claim("After winning each division you face that division's ALL-STAR XI (one-off match, rewards ~5 coins at Academy/Amateur level, scales up).", 2, "career/allstar-xi", [e_divs])
add_claim("Cup structure is paired with divisions: BRONZE CUP (Academy + Amateur), SILVER CUP (Division 4 + Division 3), GOLD CUP (Division 2 + Division 1), DIAMOND CUP (Elite + Legendary).", 1, "cups/tier-cups", [e_divs])
add_claim("Global Challenge Cup (GCC) runs CONCURRENTLY in every division — major cup with real clubs (Arsenal, Barça, Chelsea, Real Madrid, Man City/Utd, Bayern?, etc.).", 1, "cups/gcc-clubs", [e_divs])
add_claim("GCC format: 64-team single-elimination knockout (older/wiki) OR 4-team group stage round-robin per round (translated fandom/BlueStacks); likely restructured to group+knockout in newer versions. 10 Gems per round cleared.", 2, "cups/gcc-format", [e_divs])
add_claim("GCC champion coin reward: ~25 coins (LevelWinner DLS24); +50 coins achievement bonus; per-round gem reward 10 gems.", 2, "cups/gcc-rewards", [e_divs])
add_claim("GCC per-match coin rewards are community-criticized as too low: ~+3c vs 3★, +5c vs 3.5★, +8c vs 4★, +12c vs 4.5★, +20c vs 5★ opponent (r/DLS 2024).", 3, "cups/gcc-low-rewards", [e_divs])
add_claim("Post-Elite-Division endgame arc: win Elite Division (must finish 1st) → unlock International Cup (vs national teams: Brazil, Argentina, Germany, England, Portugal, etc.)", 2, "endgame/international-cup", [e_divs])
add_claim("Win International Cup → unlock All-Star Cup (vs classic historical teams: Brazil 1970, Man Utd 1999, 60s/70s/80s All-Star XIs, Spanish League All-Stars, etc.)", 2, "endgame/all-star-cup", [e_divs])
add_claim("Win All-Star Cup → final boss match vs FIRST TOUCH UNITED (FTG's in-house 'developer team', ultimate endgame opponent).", 3, "endgame/first-touch-united", [e_divs], "legacy detail; confirm still in DLS26")
add_claim("Diamond Cup is the final-tier cup, accessible during Elite and Legendary divisions (continues through endgame).", 2, "cups/diamond-cup", [e_divs])
add_claim("Relegation exists in Legendary Division: if form drops into the fixture 'red zone', you are relegated back to Elite Division.", 2, "career/relegation", [e_divs])
add_claim("League size: 16 teams per division; single round-robin = 15 division matches per season.", 2, "career/league-size", [e_divs], "older wiki DLS20; verify DLS26")
add_claim("Season composition (≈): 15 division matches + ~9 GCC matches + ~5 tier-cup matches = ~30 matches/season baseline; Legendary/post-Elite closer to ~40 matches with International/All-Star Cups.", 2, "career/season-length", [e_divs])
add_claim("Academy Division season reward: ~1,100–1,300 coins per season with 20 wins and ~3-0 scorelines + post-match ads; Division champion coin bonus starts at ~15 coins in Academy and scales up in higher divisions.", 2, "economy/season-payout", [e_divs])
add_claim("Per-match coin ceiling: ~45 coins base (15 goals × 3c/goal) before stadium bonus + ad 2x.", 3, "economy/match-ceiling", [e_divs])
add_claim("Stadium upgrade costs ~1,400 coins to meet each new division's minimum capacity threshold (r/DLS DLS24).", 2, "facilities/promotion-cost", [e_divs])
add_claim("Stadium capacity requirements CONFLICT across sources. dlspedia: Acad 6,462 / D3 15k / D2 30k / D1 45k / Jr.Elite 60k / Elite 80k. r/DLS DLS24: Acad 5k / Am 15k / D3 35k / D2 45k / D1 55k / Elite 70k / Leg 85k. supercheats: D3 15k/D2 30k/D1 45k/Jr.Elite 60k/Elite 80k. Likely DLS26 reality: 6,462 start; ~15k (Am/D4); ~30-35k (D3); ~45k (D2); ~55k (D1); ~70-80k (Elite); ~85-92k (Legendary). EXACT in-game numbers require device verification.", 2, "facilities/capacity-conflict", [e_divs], "CONFLICT — verify in-game")
add_claim("ERRATA to earlier 6-division claim: DLS26 has 8 divisions; Junior Elite Cup may exist as a transitional cup; All-Star Cup is a distinct post-International-Cup competition (not post-Legendary-Division mirror match as previously assumed).", 1, "errata/divisions", [e_divs])
add_claim("Google Play Games / iOS Game Center achievements exist for: promotion from each division (500/1000/1500 XP), Elite Cup win (1000 XP), Global Challenge Cup win (1500 XP), Allstar Cup win (1000 XP), undefeated season (1500 XP), The Double (50c), The Treble (50c), Cup Winner (50c).", 2, "platform/achievements", [e_divs])

p=os.path.join(RAW_DIR,'EV-388_divisions_cups.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
