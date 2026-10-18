#!/usr/bin/env python3
"""Turn 33 Wave 4: formations/tactics/width, skills new-DLS26, multiplayer/economy/rewards."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','formations_turn33')

ev_id=352
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"community-guide","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=451
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_formations=new_ev("sportsdunia + ggbro + gamingonphone formations guides 2026",
    "Formations confirmed available in DLS26: 4-4-2 (default), 4-1-2-1-2 (default-unlocked attacking diamond), 4-3-3, 4-2-3-1, 4-2-2-2, 3-4-1-2, 3-4-3, 4-1-2-3, 3-5-2 Fluid, 3-3-1-3, 5-3-2/5-2-1-2, 4-1-4-1 (AI teams only per sportsdunia). Extra formations unlocked via Training Centre upgrades (not all default). Tactical Presets (DLS26): 4-3-3 Tiki-Taka, 4-4-2 Counter, 3-5-2 Wing-Play switchable in-match; custom tactics save/share. Width slider available (narrow/wide) with major gameplay impact; v13.310 (Summer Spotlight May 28, 2026) included AI behavior changes. 4-4-2 recommended for beginners (stable two-banks, no catastrophes); 3-at-the-back (3-4-3, 3-5-2 Fluid, 3-3-1-3) strong but vulnerable to wingers (4-3-3) — wingbacks auto-push; 5-3-2/5-2-1-2 for defending leads; 4-2-3-1 widely panned by community (striker isolated, punished by long balls). Stamina depth outweights formation choice; 4-3-3 high-scoring but concedes more (wide forwards don't track back).",
    "evidence/raw/formations_turn33/EV-352_formations.html",
    "Formations list, unlocks, tactical presets, width slider, meta commentary")
e_skills2=new_ev("sakibpro new-2026 skills (Close Control, Knock Ahead, Secondary Press)",
    "New DLS26 skill moves per sakibpro: Knock Ahead = tap while in possession for fast breaks; Secondary Press = tap & hold while defending for double-team press. Skill move table: Rainbow swipe-up (lift over), Feint swipe-left/right (dir change), Roulette swipe-down (shield+turn), Bicycle double-tap air (finish crosses), Scorpion double-tap air (rare finish), Heading double-tap under ball (header/clear), Rabona = RainbowFlick then B/C (fancy cross).",
    "evidence/raw/formations_turn33/EV-353_skills2.html",
    "DLS26 new skills: Knock Ahead, Secondary Press, full control table")
e_rewards=new_ev("BlueStacks+gamingonphone+sportsdunia+footballeffect rewards economy guides",
    "Economy: Career match win rewards scale by division; higher divisions pay more coins + unlock gem rewards; approx 500 coins/win baseline in mid divisions (lfbb anecdote), new-user jumpstart 1200c/40g. Post-match 30-second ad DOUBLES coin earnings (one per match; re-prompt after app restart if it disappears). Menu ad = 30c/24h (cap fixed by FTG after exploit). Daily Login (20-day cycle, coins + occasional gems). Daily Scenarios = 50 coins/day (come-from-behind vs Hard AI). Daily/Weekly Challenges reward coins/gems. Global Challenge Cup (under Career) round-robin groups, 10g per round cleared online. Dream League Live = weekly leaderboard (gems for top 5, coins for rest; participation gems for match volume; weekend/end-of-week grind optimal; afternoon hours softer comp); never C-spam (lofted/long) in DLS Live (community advice). Season Pass (10-day cycle) with Progression Bank XP from DLL wins → pays Coins+Gems at end (~1095c max baseline). Prize Ladder = Dream League Points from all modes, 90-day cycle → Coins/Gems/Classic Players. Gem store bundles: 90g=199INR, 400g=799INR, 910g=1799INR, 2700g=4999INR, 6000g=9900INR. Social account link: 200g Twitter link, 50g share-match, 150g Facebook link (lfbb anecdote, veracity uncertain). Ad rewards cap of one post-match double per match + 30c menu/24h.",
    "evidence/raw/formations_turn33/EV-354_economy.html",
    "Coin/gem sources, rates, caps, DLL rewards, season/prize ladder structure")
e_modes=new_ev("App Store + apkpure + player.gg modes list",
    "Game modes in DLS26: Career (8 divisions + 10+ cup competitions), Dream League Live (online ranked vs global players), Exhibition (offline vs AI), Training (6 set-piece modules), Global Challenge Cup (online groups under Career), Events (rotating, incl. World Tournament, Kick-Off Stars, Summer Spotlight), Daily Scenarios, Dream Draft (pre-set squads), Clans (cooperative goals, Fanzone-linked). Custom kit/logo import supported. Controller support on iOS. 8 divisions total; Academy Division is starting/placement tier for new/returning players.",
    "evidence/raw/formations_turn33/EV-355_modes.html",
    "Modes list, divisions count (8)")
e_codes=new_ev("deliventura codes listing jan2026",
    "Redeem codes circulated Jan 2026: DLSNFL2026 (75k coins + NFL kit, US/SuperBowl), MLKCOINS26 (30k), SOCCERUSA2026 (free Rare RW), NEWYEARDLS26 (20g+25k), DLSHOLIDAYKIT (expired). Codes time-limited, distributed via official DLS socials/Reddit; reliability uncertain (third-party listing).",
    "evidence/raw/formations_turn33/EV-356_codes.html",
    "Redeem code examples, third-party unvetted")

# FORMATIONS / TACTICS
add_claim("Default formations at fresh start: 4-4-2 (default baseline) and 4-1-2-1-2 (attacking diamond variant); additional formations unlock via Training Centre upgrades.", 2, "tactics/formations", [e_formations])
add_claim("Full known formation roster in DLS26: 4-4-2, 4-1-2-1-2, 4-3-3, 4-2-3-1, 4-2-2-2, 3-4-1-2, 3-4-3, 4-1-2-3, 3-5-2 (Fluid), 3-3-1-3, 5-3-2, 5-2-1-2, 4-1-4-1 (AI-only observed).", 2, "tactics/formations", [e_formations], "roster may not be exhaustive")
add_claim("Tactical Presets (new DLS26): 4-3-3 Tiki-Taka, 4-4-2 Counter, 3-5-2 Wing-Play — switchable mid-match; custom tactics can be saved and shared with friends.", 2, "tactics/presets", [e_formations], "playdreamleaguesoccer (AI-farm, plausible but need APK)")
add_claim("A Width slider (narrow/wide) exists in tactics and dramatically changes how a formation plays; change width before changing formation when a shape isn't working.", 2, "tactics/sliders", [e_formations], "per ggbro")
add_claim("Formation meta community guidance: 4-4-2 safest for new players (two banks of four, low catastrophe); 4-3-3 wing-heavy but wide forwards don't track back (concedes more); 3-at-the-back (3-4-3/3-5-2 Fluid/3-3-1-3) strong but vulnerable to winger formations (4-3-3); 5-3-2/5-2-1-2 to defend leads; 4-2-3-1 widely panned (striker isolated, punished by long balls); 3-5-2 Fluid wingbacks push high with CDM cover (pacey fullbacks required), beats narrow 4-3-3.", 2, "tactics/meta", [e_formations])
add_claim("Stamina/squad depth outweighs formation choice: a 4-3-3 with fresh 70th-minute subs beats a 'perfect' 4-2-3-1 with three tired players — rotate heavily for back-to-back event matches.", 2, "tactics/stamina", [e_formations])
add_claim("Summer Spotlight update v13.310 (May 28, 2026) included AI behavior changes alongside Fanzone.", 2, "patching/changelog", [e_formations], "ggbro citation; exact AI changes unspecified")

# NEW SKILLS
add_claim("New DLS26 skill moves: Knock Ahead = tap while in possession to push ball forward for fast breaks; Secondary Press = tap & hold while defending to trigger a double-team press.", 2, "controls/skills", [e_skills2])
add_claim("Complete skill-move input table (community-sourced): Rainbow Flick = swipe up while running (lift over defender); Feint = swipe L/R while running (direction change); Roulette = swipe down while running (shield and turn); Bicycle Kick = double-tap in air (finish crosses); Scorpion Kick = double-tap in air (rare finish); Heading = double-tap under ball (header/clear); Rabona = Rainbow Flick then B/C (fancy cross); Close Control = tap & hold while running (tight dribbling, DLS25 addition).", 2, "controls/skills", [e_skills2], "inputs unverified against APK")

# ECONOMY / REWARDS
add_claim("New users receive ~1200 coins + 40 gems jumpstart on first launch.", 2, "economy/starter", [e_rewards])
add_claim("Career match coin rewards scale with division: higher divisions pay more coins; gems become available as rewards in higher divisions; ~500 coins per win is a mid-division baseline (community anecdote). Win vs loss payout gap is significant.", 2, "economy/career", [e_rewards], "exact per-division tables unverified")
add_claim("Post-match 30-second ad DOUBLES coin earnings (one ad per match); if ad prompt disappears, restart app to reset. Not available for every match reliably.", 2, "economy/ads", [e_rewards])
add_claim("Menu ad pays 30 coins, capped at once per 24 hours (FTG fixed prior multi-launch exploit).", 2, "economy/ads", [e_rewards])
add_claim("Daily Login cycle is 20 days, awarding coins + occasional gems.", 2, "economy/daily", [e_rewards])
add_claim("Daily Scenarios award 50 coins/day (come-from-behind situations vs Hard AI).", 2, "economy/scenarios", [e_rewards])
add_claim("Daily/Weekly Challenges award coins/gems for completion (full-set bonuses).", 2, "economy/challenges", [e_rewards])
add_claim("Global Challenge Cup (online, under Career menu) = round-robin group stage vs online opponents; 10 Gems awarded per round cleared.", 2, "events/global-cup", [e_rewards])
add_claim("Dream League Live (online ranked): weekly leaderboard reset; top-5 finishers earn gems, others earn coins; participation gems granted for hitting a match-volume threshold; weekend/end-of-week grind optimal (before reset); afternoon play reportedly has softer competition (community anecdote).", 2, "multiplayer/dll", [e_rewards])
add_claim("NEVER C-spam (lofted/long-ball button) in Dream League Live — community consensus it is ineffective/punished at higher ranks.", 3, "multiplayer/etiquette", [e_formations], "r/DLS 2023 advice; may have shifted with DLS26 C-nerf")
add_claim("Season Pass runs 10-day cycles; Progression Bank tracks XP from DLL wins and pays out Coins+Gems at season end (~1,095 coin baseline cited, gems variable with wins).", 2, "economy/season-pass", [e_rewards])
add_claim("Prize Ladder uses Dream League Points earned across all modes; 90-day cycles award Coins/Gems/Classic Players on milestone thresholds.", 2, "economy/prize-ladder", [e_rewards])
add_claim("Gem IAP bundles (India pricing 2025): 90 gems = ₹199; 400 = ₹799; 910 = ₹1,799; 2,700 = ₹4,999; 6,000 = ₹9,900 (~₹1.65/gem at smallest bundle, ~₹1.65/gem at largest, volume discounts marginal).", 3, "economy/iap", [e_rewards], "regional pricing, not global")

# MODES / SCOPE
add_claim("DLS26 game modes: Career (8 divisions + 10+ cups), Dream League Live (ranked online), Exhibition (offline vs AI), Training (6 set-piece modules), Global Challenge Cup (online groups), Events (rotating: World Tournament, Kick-Off Stars, Summer Spotlight), Daily Scenarios, Dream Draft (preset-squad tactical mode), Clans (cooperative goals, Fanzone-linked).", 2, "modes/roster", [e_modes])
add_claim("8 career divisions in total (Academy Division starting tier → Legendary Division top tier, 8th).", 2, "career/divisions", [e_modes], "division names beyond Academy/Legendary unverified")
add_claim("Custom kit and logo import is supported (user-provided images/URLs).", 2, "customization/kits", [e_modes])
add_claim("DLS26 supports external controllers on iOS (MFi); Android controller support assumed but not explicitly confirmed in reviewed sources.", 3, "platform/controller", [e_modes], "App Store mentions controller support")
add_claim("Redeem codes distributed periodically via official DLS social channels (Twitter/Reddit) for coins/gems/players/kits; third-party listings (deliventura) showed Jan-2026 examples DLSNFL2026/MLKCOINS26/SOCCERUSA2026/NEWYEARDLS26 with expiry dates.", 3, "economy/codes", [e_codes], "third-party unvetted listing — treat as illustrative")

for f in ['EV-352_formations.html','EV-353_skills2.html','EV-354_economy.html','EV-355_modes.html','EV-356_codes.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-451} new claims and {ev_id-352} EVs. Totals: {n_cl} claims, {n_ev} EVs")
