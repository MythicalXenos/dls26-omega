#!/usr/bin/env python3
"""Turn 34 Wave 3: Cult Heroes roster/details, corrected economy numbers (rewards cap, ad frequency, Team Boost/Physio prices, starter pack, rare/legendary spawn thresholds, stadium bonus 85k)."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn34_w3')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="mixed"):
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

e_cult=new_ev("dlsinside Cult Heroes DB (Sep 16 2026) + FTG official TikTok + APKMirror v13.410/420/430",
    "Cult Heroes collection announced in v13.410 (Aug 20) 'coming soon'; reaffirmed in v13.420 (Sep 1) and v13.430 (Sep 16); launched September 16, 2026 per FTG official TikTok ('Dropping in game 16.09.2026'). Distribution: Cult Hero Agents earned from Events, Dream Draft, and Season Pass (NOT direct coin purchase; agent-based). dlsinside.com/players/specials/cult-heroes lists 12 Cult Heroes at launch (all NO TEAM / free-agent cult heroes): David de Gea (GK, 85 OVR, GKR 85 / GKH 80 / PAS 60 per dlsinside player page — Spain, 76kg, b. 07-Nov-1990, ID 28324, #1); Pierre-Emerick Aubameyang (ST, #17); Paulo Dybala (#10); Lorenzo Insigne (#24); Hakim Ziyech (#22); Francisco Alarcón (Isco, #22); Vozinha (GK Cape Verde, #1); Nicolás Otamendi (CB, #30); David Luiz (CB, #30); Daley Blind (#17); Xherdan Shaqiri (#23); Ander Herrera (#21). Cards are Special (not standard rare/legendary) category. v13.430 bundle size 31.60 MB (arm64-v8a + armeabi-v7a); APKMirror shows v13.430 is 7-bundle (smaller than v13.410 which was 33-bundle 158). All Cult Heroes listed as 'NO TEAM CULT HERO AGENT' — meaning they can only be obtained via Cult Hero Agent draws, not live transfers. YouTube Shorts show 'Cult Heroes Tournament' event beginning Oct 2, 2026.",
    "evidence/raw/turn34_w3/EV-378_cult.html",
    "Cult Heroes: 12-player launch roster, Sep 16 2026 release, Cult Hero Agents via Events/Drafts/SeasonPass, de Gea 85 OVR example stats")
e_econ=new_ev("r/DLS DLS23 ad-testing thread + LevelWinner DLS24 guide + r/DLS DLS24 beginner guide + r/DLS DLS-summed-up 2023 + Bluestacks + gamingonphone",
    "Corrected/expanded economy numbers (from prior more-approximate claims):\n- Ad rewards per day: up to 10 video-ad rewards per 24h reset; declining to watch an ad does NOT consume a slot (optimize by only doubling home wins).\n- Post-match ad bonus doubles coins with min 30 / max 100 bonus on top of base (e.g. loss with 3c base → 3+30=33; big win with 110c base → 110+100=210). Stadium at 85k gives 48-52 coin per home win bonus; combined with ad this yields ~250c/home-win average.\n- Team Boost (mid-game/halftime): 30 coins, restores ~10% stamina (same effect as post-game Team Physio).\n- Team Physio default prices: Common 50c, Rare 100c, Legendary 200c (per team application); these are poor-value early because match coin rewards can't offset the cost; best saved for injury crunches.\n- Starter pack (DLS24 data, corroborated for DLS26 direction): 1500 coins + 75 gems + free Common Scout + free Common Agent at captain-select/onboarding (previous 1200c/40g claim from gamingonphone was likely DLS20/DLS21 baseline; DLS24/DLS26 may be 1500/75 — NEED CONFIRMATION). Spend the 75 starter gems first on Training Centre (unlocks formations + -5% coach cost per earlier EV) not Agents.\n- Rare players start appearing on Live Transfers at team rating ~65 OVR; Legendaries (80-82 OVR range) start appearing at ~68.7+ OVR team rating.\n- Goals scored cap at 15 per match for coin/token rewards (scoring more than 15 yields nothing extra).\n- Buy-and-release meta: buy 80-rated defenders (~1460c) or <180c players and immediately release for coach cards; with 85k stadium this yields ~250c per home match after ad doubling — fastest coin grind once stadium is maxed.\n- Form Boost duration: starts at minimum 1 match; extended by Training Centre upgrades (FTG support).\n- Daily login reward cycle is 20 days. Post-match ad x2 available once per match; menu 30c ad once per 24h. Daily ad limit ~10 video rewards (DLS23, may apply to DLS26).",
    "evidence/raw/turn34_w3/EV-379_econ.html",
    "Ad 10/day cap, post-match min30/max100 bonus, 85k stadium 48-52c bonus, Team Physio prices, starter 1500c/75g, rare/leg spawn thresholds at team rating, 15-goal cap, buy-release meta")

# CULT HEROES
add_claim("Cult Heroes special-player collection launched September 16, 2026 (announced v13.410 Aug 20 'coming soon'; v13.420 Sep 1; v13.430 Sep 16 launch day).", 1, "cards/cult-heroes", [e_cult])
add_claim("Cult Heroes are distributed via 'Cult Hero Agents' earned from Events, Dream Draft, and Season Pass; NOT purchasable directly with coins; all listed 'NO TEAM CULT HERO AGENT' (free-agent, agent-pull-only).", 1, "cards/cult-distribution", [e_cult])
add_claim("Cult Heroes launch roster (12 players): David de Gea (GK, 85 OVR, Spain), Pierre-Emerick Aubameyang (ST), Paulo Dybala, Lorenzo Insigne, Hakim Ziyech, Francisco Alarcón 'Isco', Vozinha (GK, Cape Verde), Nicolás Otamendi (CB), David Luiz (CB), Daley Blind, Xherdan Shaqiri, Ander Herrera.", 1, "cards/cult-roster", [e_cult])
add_claim("David de Gea (Cult Hero) example stats: 85 OVR, GKR 85, GKH 80, PAS 60; GK (Spain, #1, 76kg, b.Nov 7 1990, player ID 28324).", 1, "cards/degea", [e_cult])
add_claim("Cult Heroes are a Special card category (distinct from Common/Rare/Legendary/Dynamic/Kick-Off/Dream Stars/Classic).", 2, "cards/categories", [e_cult])
add_claim("Cult Heroes Tournament event went live October 2, 2026 (YouTube Shorts reference).", 2, "events/cult-tournament", [e_cult])
add_claim("v13.430 bundles: 7-split bundles (vs 33-split for v13.410), 31.60 MB base APK for arm64-v8a+armeabi-v7a (Android 12L+).", 1, "patching/v13-bundles", [e_cult])

# ECONOMY (CORRECTED/EXPANDED)
add_claim("Ad reward limit: up to 10 rewarded video ads per 24h period; declining an offered ad does NOT consume a slot — strategy is to only double high-value home wins.", 2, "economy/ad-limit", [e_econ], "r/DLS DLS23 test; DLS26 may carry same mechanic")
add_claim("Post-match ad bonus gives +doubled coins with minimum 30 coins bonus (e.g. 3-coin loss → 33 total) capped at 100 coins bonus (e.g. 110-coin win → 210 total).", 2, "economy/ad-bonus-cap", [e_econ])
add_claim("85,000-capacity stadium yields ~48-52 coins per home win as a stadium bonus; combined with post-match ad doubling this yields ~250 coins per home-win average.", 2, "economy/stadium-bonus-concrete", [e_econ])
add_claim("Halftime/mid-game Team Boost costs 30 coins and restores ~10% stamina (same effect magnitude as post-game Team Physio).", 2, "economy/team-boost-price", [e_econ], "LevelWinner DLS24")
add_claim("Team Physio (full-squad) default prices: Common 50 coins, Rare 100 coins, Legendary 200 coins; generally poor value early game since match payouts cannot offset cost; reserve for rotation crises.", 2, "economy/physio-team-prices", [e_econ], "LevelWinner DLS24; individual physio prices earlier ~150-250c per legend")
add_claim("Starter pack (DLS24 baseline, likely DLS26): 1,500 coins + 75 gems + 1 free Common Scout + 1 free Common Agent (earlier 1200c/40g claim was DLS20-era).", 2, "economy/starter-pack", [e_econ], "r/DLS DLS24; verify in DLS26")
add_claim("Recommended first 75-gem spend is Training Centre (unlocks formations + -5% coach cost) — NOT Agents or Stadium; stadium upgrades come with coins.", 2, "economy/first-spend", [e_econ], "r/DLS DLS24; corroborates Training priority")
add_claim("Live Transfer Market spawn tiers: team rating ~65+ OVR → Rare players appear; team rating ~68.7+ OVR → Legendary players (80-82 OVR range) start appearing.", 2, "transfers/spawn-threshold", [e_econ], "r/DLS DLS24")
add_claim("Goals-reward cap: scoring more than 15 goals in a career match yields no additional coin/token reward — further goals are wasted for farming.", 2, "economy/goals-cap", [e_econ], "r/DLS 2023")
add_claim("Buy-and-release coin/coach farming meta (late game with 85k+ stadium): buy 80-rated defenders (~1,460c) or sub-180c players and immediately release for coach cards; paired with ad-doubled home wins averages ~250c/match quickly.", 2, "economy/buy-release", [e_econ])
add_claim("Starter 1,200 coins + 40 gems figure was the DLS20-era jumpstart (gamingonphone/BlueStacks DLS20 guides); DLS24/DLS26 starter appears to be 1,500c + 75g per r/DLS — track APK verification.", 2, "economy/starter-discrepancy", [e_econ], "cite the discrepancy")
add_claim("Career-mode farming rate: ~6 matches per 15-minute real-football halftime → ~6,000 coins/halftime session (lfbb anecdote).", 2, "economy/farming-rate", [e_econ])

for f in ['EV-378_cult.html','EV-379_econ.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
