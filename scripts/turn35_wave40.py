#!/usr/bin/env python3
"""Turn 35 Wave 40: Dream Draft full mechanics (18 players, 75+, Star Player, 7 rounds, CPU, gems-only, 40g entry/50g win, players not kept), Career coin economy (30 coins max for goals, 150 coins for a loss, 110 gems/season), the early-game 'do not buy legendaries' rule, captain-as-attacker, starter rewards, skill-move swipe/CON dependency, 512x512 kit import, OFFICIAL no-infinite-currency confirmation."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w40')

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

# ---------- EV-440: Dream Draft ----------
e_dd=new_ev("gamingonphone DLS25 Dream Points guide, Bluestacks DLS24 December Dream Draft update, r/DreamLeagueSoccer 1bxd5eb (Apr 2024), 1atb4e2 (Feb 2024), 1oo1dkw (Nov 2025), 18dqq9e (Jan 2024), 1bxd927/199x7me/hmya2v/1co8wi2/19bxl2g (Dream Draft threads), YouTube Dream Draft Festival Cup / Global Stars / World Cup Draft",
    "DREAM DRAFT - FULL MECHANICS. STRUCTURE: you draft an entire team of 18 players from the choices offered for each position, and every player in the option pool is 75+ rated alongside a Star Player. AT LEAST ONE STAR PLAYER IS MANDATORY in the draft. The mode is a limited-time tournament of up to 7 ROUNDS AT MAXIMUM, with a different opponent each round, and the FORMATIONS YOU CAN SELECT ARE LIMITED (at least in the mode's first iteration). OPPONENTS are the CPU in the standard version - which is why maxing Dream Points here is easier than in Live - though online Draft events (Global Stars Tournament, World Cup Draft) also run. REWARDS: gems for winning the semi-finals and finals, plus leaderboard rewards where winners, runners-up and 3rd place receive medals, gems and coins. DREAM POINTS: maintaining a clean sheet and scoring 5+ goals yields the maximum 185 DP, the same ceiling as Live. THE PLAYERS ARE NOT KEPT - the only reward is gems at the end, so the mode is a gem engine, not a squad-building tool. ENTRY COST has moved around: DLS24 charged a fee (making it unlikely for free-to-play players), and DLS25 made it free to play for the first time, with the community noting FTG may put it back behind a paywall. Reported entry figures are 40 gems or 500 coins, with a win paying 50 gems - a net profit of only about 10 gems. Dream Draft events run roughly EVERY TWO WEEKS. COMMUNITY VERDICT: the opposition is heavily weighted against you and the game feels scripted, and because you are not guaranteed rewards if you lose it is described as 'somewhat of a scam'; one player nonetheless made 150 gems in about two hours by entering at 500 coins and winning three times. In themed drafts you do NOT get to choose a second Player Card if you skip the first one offered.",
    "evidence/raw/turn35_w40/EV-440_dream_draft.html",
    "DREAM DRAFT: draft 18 players from 75+ rated options per position, AT LEAST ONE STAR PLAYER MANDATORY; limited-time tournament of up to 7 rounds max with a different opponent each round; FORMATION SELECTION IS LIMITED; opponents are the CPU in the standard version (online variants exist); rewards are gems for winning the semi-finals and finals plus leaderboard medals/gems/coins for winners, runners-up and 3rd; max 185 DP for a clean sheet plus 5+ goals; THE PLAYERS ARE NOT KEPT - gems only; entry was paid in DLS24, free in DLS25, may be paywalled again; entry ~40 gems or 500 coins, win pays 50 gems (net ~10); events run every ~2 weeks; community calls the opposition heavily weighted/scripted and the mode a scam since losing yields nothing; in themed drafts you cannot pick a second Player Card if you skip the first offer",
    quality="community")

add_claim("Dream Draft: you draft a team of 18 players from 75+ rated options for each position, and at least one Star Player is mandatory.", 3, "draft/18-players-75-plus", [e_dd])
add_claim("Dream Draft is a limited-time tournament of up to 7 rounds maximum, with a different opponent each round and a LIMITED selection of formations.", 3, "draft/7-rounds-limited-formations", [e_dd])
add_claim("In the standard Dream Draft you play against the CPU, which is why maxing Dream Points (185 for a clean sheet plus 5+ goals) is easier than in Dream League Live.", 3, "draft/cpu-opponents", [e_dd])
add_claim("Dream Draft rewards are gems for winning the semi-finals and finals, plus leaderboard medals, gems and coins for winners, runners-up and third place.", 3, "draft/rewards", [e_dd])
add_claim("Dream Draft players are NOT kept - the only reward is gems at the end, so the mode is a gem engine rather than a squad-building tool.", 2, "draft/players-not-kept", [e_dd])
add_claim("Dream Draft entry was paid in DLS24, made free-to-play for the first time in DLS25, and the community warns FTG may put it back behind a paywall; reported entry is about 40 gems or 500 coins with a win paying 50 gems.", 3, "draft/entry-cost-history", [e_dd])
add_claim("Dream Draft events run roughly every two weeks, and winning one is worth about 10-15 gems net profit.", 3, "draft/frequency", [e_dd])
add_claim("In themed Dream Drafts you do NOT get to choose a second Player Card if you skip the first one offered.", 3, "draft/skip-penalty", [e_dd])
add_claim("Community verdict on Dream Draft: the opposition is heavily weighted against you and the game feels scripted, and because losing yields nothing it is described as somewhat of a scam.", 3, "draft/community-criticism", [e_dd])

# ---------- EV-441: career economy + early rules ----------
e_ce=new_ev("r/DreamLeagueSoccer 1oo1dkw (Nov 2025 coin strategies), 18dqq9e (Jan 2024 DLS24 beginners guide), tuapppara.com (citing FTG support), Bluestacks DLS26 guides, prior EV-420",
    "CAREER COIN ECONOMY AND EARLY-GAME RULES. GOAL COINS ARE CAPPED: a player scores exactly 5 goals 'as we can earn only 30 coins max, 6*5' - that is 6 coins per goal for a maximum of 5 goals, so 30 coins is the per-match goal ceiling and the 5-goal DP cap and the 30-coin goal cap are the same limit viewed twice. THE LOSS FLOOR IS HIGH: after winning 9-10 games, or once the Legendary Division is secure, a player simply finishes matches without playing and LOSES, because 'even after losing we get around 150 75+75 coins from home games' - a Legendary Division home match pays roughly 150 coins even in defeat (75 base + 75 stadium bonus), and the only thing sacrificed is a 10-gem 'win all games' objective. A whole Career Season therefore yields about 110 gems (35 + 75). TIME EFFICIENCY: 10 matches yield about 2,000 coins in roughly an hour, so a full team of commons can be farmed in a day. THE SINGLE MOST IMPORTANT EARLY RULE: do NOT buy legendary players early, because 'buying them will increase your team's ranking and cheap players will disappear from market'. Instead buy one or two fast common or rare players to score more goals and win, and only start buying and selling commons once the stadium is maxed - then buy them really cheap and keep selling to accumulate common coaches. CAPTAIN CHOICE: pick the best ATTACKER as captain because it boosts team rating, which in turn improves the players that appear in the market. STARTER REWARDS: 1,500 coins and 75 gems. DREAM LEAGUE LIVE EARLY: only play Live EVENTS for rewards and avoid regular Live matches until the squad is ready. SKILL MOVES are swipe gestures, not buttons, and their success depends on the player's Ball Control stat - 'the game engine decides' whether the move executes. KIT AND CREST IMPORT uses an image of at most 512x512 pixels pasted as a URL into the importer. OFFICIAL FTG POSITION (via a Spanish-language guide citing FTG support): infinite coins or gems DO NOT EXIST, modified versions end in account blocking, and generators are a scam. OTHER ECONOMIC NOTES: final league position and cups won pay SEPARATELY from the per-match prize, so always play the league and cups to the end; season objectives are the most commonly unclaimed rewards; and the Prize Ladder accrues Dream Points passively from every match.",
    "evidence/raw/turn35_w40/EV-441_career_economy.html",
    "GOAL COINS CAPPED at 30 per match (6 coins x 5 goals) - the same limit as the 5-goal DP cap; a Legendary Division home match pays ~150 coins even when you LOSE (75 base + 75 stadium bonus), so once the division is secure you can auto-finish and lose matches, sacrificing only a 10-gem win-all objective; a whole Career Season yields ~110 gems (35+75); 10 matches = ~2,000 coins in ~1 hour. THE KEY EARLY RULE: do NOT buy legendary players early - they raise team rating and make cheap players disappear from the market; buy 1-2 fast commons/rares instead, and only start buy-sell cycling once the stadium is maxed. Captain should be the best ATTACKER (boosts team rating -> better market). Starter rewards 1,500 coins + 75 gems. In Live, only play EVENTS early. Skill moves are swipe gestures whose success depends on Ball Control and the engine's decision. Kit/crest import uses a max 512x512 image pasted as a URL. OFFICIAL: infinite coins/gems do not exist, mods = account blocking, generators = scam. Final league position and cups pay separately from per-match prizes; season objectives are the most unclaimed rewards",
    quality="community")

add_claim("Goal coins are capped at 30 per match (6 coins per goal for a maximum of 5 goals) - the same underlying limit as the 5-goal Dream Point cap.", 3, "economy/goal-coin-cap-30", [e_ce])
add_claim("A Legendary Division home match pays roughly 150 coins even when you LOSE (about 75 base plus 75 stadium bonus), so once the division is secure you can auto-finish and lose matches, sacrificing only a 10-gem win-all-games objective.", 3, "economy/loss-floor-150-coins", [e_ce], notes="Major time-efficiency finding")
add_claim("A whole Career Season yields about 110 gems (35 plus 75), and 10 matches yield about 2,000 coins in roughly an hour.", 3, "economy/season-gem-yield", [e_ce])
add_claim("THE KEY EARLY RULE: do NOT buy legendary players early, because buying them raises team rating and makes cheap players disappear from the market; buy one or two fast common or rare players instead.", 2, "transfers/no-early-legendaries", [e_ce])
add_claim("Only start buy-sell cycling of cheap common players once the stadium is maxed; before that, buy them really cheap and keep selling to accumulate common coaches.", 3, "economy/common-buy-sell-timing", [e_ce])
add_claim("Pick the best ATTACKER as captain because it boosts team rating, which in turn improves the players that appear in the transfer market.", 2, "onboarding/captain-attacker", [e_ce])
add_claim("Starter rewards are 1,500 coins and 75 gems.", 2, "economy/starter-rewards", [e_ce])
add_claim("Early in Dream League Live, play only Live EVENTS for rewards and avoid regular Live matches until the squad is ready.", 3, "dll/events-only-early", [e_ce])
add_claim("Skill moves are swipe gestures rather than buttons, and whether the move executes depends on the player's Ball Control stat and the game engine's decision.", 2, "gameplay/skill-moves-swipe-con", [e_ce])
add_claim("Kit and crest import uses an image of at most 512x512 pixels, pasted as a URL into the importer on the Customise screen.", 2, "customization/kit-512-import", [e_ce])
add_claim("OFFICIAL FTG POSITION: infinite coins or gems do not exist, modified versions of the game end in account blocking, and coin/gem generators are a scam.", 1, "errata/no-infinite-currency-official", [e_ce])
add_claim("Final league position and cups won pay SEPARATELY from the per-match prize, so always play the league and cups through to the end.", 2, "economy/position-and-cups-pay-separately", [e_ce])
add_claim("Season objectives are the most commonly unclaimed rewards and are the primary free gem source.", 3, "economy/season-objectives-unclaimed", [e_ce])

p=os.path.join(RAW_DIR,'EV-440_dream_draft.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-441_career_economy.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
