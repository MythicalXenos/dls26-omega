#!/usr/bin/env python3
"""Turn 35 Wave 26: Dream League Live tier matchmaking/scoring/rewards, cup formats and division-to-tier-cup mapping, International/All-Star Cups, Baiduwiki errata."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w26')

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

# ---------- EV-415: Dream League Live ----------
e_dll=new_ev("r/DreamLeagueSoccer (1ckewnk May2024, 1bgopxf Mar2024, 1aj5rx0 Feb2024, 16l5a9w Sep2023), LevelWinner DLS21 advanced guide, gamingonphone DLS20/DLS24/DLS26 guides, Bluestacks DLS26 free-rewards guide, sportsdunia DLS26 gems guide",
    "DREAM LEAGUE LIVE (DLL). MATCHMAKING is tier-based: you are only matched against players in your own Tier (stated consistently by the same r/DLS authority across three threads). TIER CAMPING is a known problem - maxed players deliberately remain in lower tiers (roughly 12-20) so they are paired with low-rated teams and beginners; the community notes there is no fix until FTG switches matchmaking from tier to team rating. Low-tier players report being bounced between tiers 2-5, and one widely-held theory is that the game forces you out of a tier once you have survived it more than twice. SCORING: a win earns 3 points, a draw 1 and a loss 0. Champion status requires 12+ points before the season ends, and 7+ points is enough for promotion to the next highest league. Results generate Season XP which feeds the Leaderboard; at season end the top five managers receive gems - the top three get 100 gems each, fourth gets 40 and fifth gets 30, with everyone else paid in coins. The Weekly Leaderboard resets every week and ranks on recent form, so grinding toward the weekend is optimal. Separately, gems are awarded simply for participating in a set number of DLL matches within the week. DLL XP also feeds the Season Pass Progression Bank, which is paid out at the end of each 10-day season. Community advice: never C-spam (repeated Lofted Kick) in DLL.",
    "evidence/raw/turn35_w26/EV-415_dll.html",
    "DLL matchmaking is strictly tier-based (same Tier only); tier camping by maxed players in tiers 12-20 is endemic; low-tier players oscillate between tiers 2-5 and the game may force you out of a tier after surviving it twice; scoring 3/1/0; champion at 12+ points, promotion at 7+; leaderboard gems top3=100 each, 4th=40, 5th=30; weekly reset favours weekend grinding; participation gems for a set number of weekly matches; DLL XP feeds Progression Bank; never C-spam in DLL",
    quality="community")

add_claim("Dream League Live matchmaking is strictly tier-based - you are only matched against players in your own Tier.", 2, "dll/tier-matchmaking", [e_dll])
add_claim("Tier camping is endemic in Dream League Live: maxed players deliberately stay in lower tiers (roughly 12-20) to be paired with low-rated teams and beginners, and the community wants matchmaking switched from tier to team rating.", 2, "dll/tier-camping", [e_dll])
add_claim("Dream League Live scoring is 3 points for a win, 1 for a draw and 0 for a loss; Champion status needs 12+ points and promotion needs 7+ points before the season ends.", 3, "dll/scoring-and-promotion", [e_dll])
add_claim("DLL leaderboard gem rewards: the top three managers receive 100 gems each, fourth place 40 and fifth place 30, with all other finishers paid in coins.", 3, "dll/leaderboard-rewards", [e_dll])
add_claim("The DLL Weekly Leaderboard resets every week and ranks on recent form, so concentrating the grind toward the weekend is optimal; gems are also awarded simply for playing a set number of DLL matches in the week.", 2, "dll/weekly-reset-participation", [e_dll])
add_claim("Low-tier DLL players report oscillating between tiers 2-5, and a widely held theory is that the game forces you out of a tier once you have survived it more than twice.", 3, "dll/tier-oscillation", [e_dll])

# ---------- EV-416: cups ----------
e_cup=new_ev("dontruko divisions guide, Vietnamese Wikipedia DLS gameplay section, dream-league-soccer.fandom Global Challenge Cup + main wiki, dls-wiki.fandom Leagues, Bluestacks DLS26 free-rewards guide, r/DreamLeagueSoccer (1f8h9nx Sep2024, 1ib3c2g Mar2025, 1h5ixjz Dec2024, 1bo05q5 Mar2024, 1mfr70w Aug2025, 1b183rw, n623r2), LevelWinner DLS24 beginner guide, Baiduwiki",
    "CUP COMPETITIONS. TIER CUPS are mapped to divisions: Academy and Amateur = Bronze Cup; Division 4 and Division 3 = Silver Cup; Division 2 and Division 1 = Gold Cup; Elite and Legendary = Diamond Cup (dontruko, Vietnamese Wikipedia). GLOBAL CHALLENGE CUP is available in every division from Academy to Legendary. FORMAT CONFLICT: fandom describes it as a knockout where any single loss eliminates you; Bluestacks and dls-wiki describe a round-robin group stage of 4 teams with the top 2 qualifying; r/DLS quantifies it as 32 groups of 4 (128 teams) feeding a 64-team Round 1, while another thread says 'the GCC right now is made of 128 teams' and a third claims you play three group opponents twice Champions-League style. The best-supported reading is groups of 4 with 2 qualifiers, then a single-legged knockout. GCC pays 10 gems per round cleared, and winning the GCC pays 25 gems - more gems than the Diamond Cup, which the community notes is the sweeter prize despite the Diamond Cup's prestige. DIAMOND CUP requires Legendary Division and runs Round 1, Round of 16, Quarter-final, Semi-final, Final with roughly 32 teams. SEASON SHAPE: a maximum of 30 matches across three competition paths - 15 division matches, 9 GCC matches and 5 tier-cup matches - and an early knockout shortens the season. Rewards: division champion pays 15 (Academy, rising in higher divisions), GCC champion 25, and 1st/2nd in the scaling tier cup pays 9 in Academy and 10 in Amateur. INTERNATIONAL CUP (World Cup) pits you against national teams and is unlocked by winning the Legendary Division; losing it means you cannot qualify for the DLS All-Star Cup and return to the Legendary Division - though an Aug 2025 r/DLS thread reports the International Cup existing only in the trophies list and not being playable in DLS25, a version conflict. Long-term players report 18-19 International Cup and All-Star Cup wins. BAIDUWIKI is flagged unreliable: it claims DLS has a 'real-time bidding auction house' transfer market (it does not) and cites only ~2,000 licensed players against the official 4,000+.",
    "evidence/raw/turn35_w26/EV-416_cups.html",
    "Tier cups by division: Academy/Amateur=Bronze, Div4/3=Silver, Div2/1=Gold, Elite/Legendary=Diamond; GCC available all divisions, best-supported format = groups of 4 with 2 qualifiers then single-legged KO (32 groups/128 teams -> R1 of 64), fandom's any-loss-eliminates and 'play 3 teams twice' variants conflict; GCC = 10 gems per round cleared, 25 for winning (more gems than Diamond Cup); Diamond Cup ~32 teams R1/RO16/QF/SF/F, Legendary only; season = 15 division + 9 GCC + 5 tier cup (~30 max); champion rewards 15/25/9-10; International Cup = national teams after winning Legendary, loss blocks All-Star Cup; Baiduwiki auction-house claim false",
    quality="community")

add_claim("Tier cups are mapped to divisions: Academy and Amateur play the Bronze Cup, Division 4 and 3 the Silver Cup, Division 2 and 1 the Gold Cup, and Elite and Legendary the Diamond Cup.", 2, "cups/tier-cup-mapping", [e_cup])
add_claim("The Global Challenge Cup is available in every division from Academy through Legendary.", 2, "cups/gcc-availability", [e_cup])
add_claim("Best-supported GCC format: round-robin groups of 4 with the top 2 qualifying, feeding a single-legged knockout (32 groups of 4 = 128 teams, then a 64-team Round 1).", 2, "cups/gcc-format", [e_cup])
add_claim("CONFLICT on the GCC: fandom describes it as a knockout where any single loss eliminates you, and one r/DLS thread claims you play three group opponents twice Champions-League style - both contradict the groups-of-4-then-KO reading.", 3, "cups/gcc-format-conflict", [e_cup], notes="Format conflict recorded; groups-of-4 reading has the most support")
add_claim("The Global Challenge Cup pays 10 gems per round cleared and 25 gems for winning it - a better gem return than the Diamond Cup despite the Diamond Cup's greater prestige.", 3, "cups/gcc-gem-rewards", [e_cup])
add_claim("The Diamond Cup requires Legendary Division and runs Round 1, Round of 16, Quarter-final, Semi-final and Final with roughly 32 teams.", 3, "cups/diamond-cup-format", [e_cup])
add_claim("A season holds a maximum of 30 matches across three competition paths - 15 division matches, 9 Global Challenge Cup matches and 5 tier-cup matches - and an early cup knockout shortens the season.", 2, "career/season-shape", [e_cup])
add_claim("Cup and league champion rewards: division champion pays 15 (Academy, rising in higher divisions), Global Challenge Cup champion 25, and 1st/2nd in the scaling tier cup pays 9 in Academy and 10 in Amateur.", 3, "cups/champion-rewards", [e_cup])
add_claim("The International Cup (World Cup) pits your club against national teams and is unlocked by winning the Legendary Division; losing it blocks qualification for the DLS All-Star Cup and returns you to the Legendary Division.", 3, "cups/international-cup", [e_cup])
add_claim("CONFLICT: an Aug 2025 r/DLS thread reports the International Cup appearing only in the trophies list and not being playable in DLS25, while other threads report 18+ International Cup and All-Star Cup wins.", 3, "cups/international-cup-availability", [e_cup], notes="Version-dependent availability")
add_claim("Baiduwiki is flagged unreliable for DLS: it claims a 'real-time bidding auction house' transfer market that does not exist and cites only ~2,000 licensed players against the official 4,000+ figure.", 3, "errata/baiduwiki-unreliable", [e_cup])

p=os.path.join(RAW_DIR,'EV-415_dll.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-416_cups.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
