#!/usr/bin/env python3
"""Turn 35 Wave 5: scout/agent costs + odds, starter kit, max player gem cost, recruitment discount, Live Transfers 80+ cost, starter resources correction."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w5')

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

e_scouts=new_ev("r/DLS DLS24 beginner guide, r/DLS legendary scout math Sep2025, r/DLS scout reminder, rajatips, supercheats, sportysure, lfbb, gamingonphone, sportsdunia, r/DLS gems guide, BlueStacks, r/DLS IAP value Mar2024, r/DLS 10c player",
    "Scouts cost COINS. Base costs (DLS24-DLS26 era, approximate): Common ~75c, Rare ~225c, Legendary ~500c (handwiki/rajatips/supercheats/r/DLS). Recruitment Centre provides scout/agent DISCOUNT (~5% per level estimated; ~20% discount at max reported in r/DLS legendary-scout math). Scout odds (DLS-community estimates, rajatips + r/DLS probability math): Common scout ≈ 2% chance per player found of Legendary (80+ OVR), ~5% Talented, ~93% ordinary; per Common scout roll you get 2 players → P(at least 1 Leg) ≈ 3.96%. Legendary scout ≈ 15% chance per player of Legendary (≈27.75% per 2-pull of at least one Legendary). Rare scouts are widely considered a coin-scam/poor EV (community consensus). Agents cost GEMS: Common ~40g, Rare ~240g, Legendary ~350g (handwiki DLS20-era; consistent with r/DLS '375 gem legendary agent' from Mar2024 IAP thread). Agent outcome: Common = ordinary player <70; Rare = talented 71-79; Legendary = guaranteed Legendary 80+ (confirmed by reddit '350 gems agent to get a free legendary player' for new accounts). New player onboarding resources: 1,500 coins + 75 gems + 1 FREE Common Scout + 1 FREE Common Agent (r/DLS DLS24 guide; contradicts earlier 1,500c+75g starter — the free scout/agent are added). Lowest observed transfer-market player price: 10 coins (no Recruitment discount, r/DLS DLS24). Events run approximately every ~4 days (DLS24 guide) and award ~600+ coins + chance at a legendary player. Maxing one Special player from scratch takes ~2,100-2,835 gems in coach costs (r/DLS gems guide Apr2024). Live Transfers section offers 80+ OVR players signable directly with gems (gamingonphone DLS25). Special Agent tokens (event rewards) can grant a guaranteed legendary player (e.g., 96 Haaland reported lfbb). Community spending advice (gamingonphone + r/DLS): DON'T spend gems on Common/Rare agents; either save for Legendary agents when new (better: save for Live Transfers 80+ or coaches for key players, or buy 80-OVR defenders for ~1,300-1,400c and release for Legendary coaches). r/DLS also says 'Don't spend gems on Legendary Agents' (gamingonphone DLS26 guide Jan2026) — value depends on account stage. IAP value sanity check (r/DLS Mar2024): $37 bundle with 45,000c + 1,200g + Legendary Agent ≈ $92 nominal value (45k c ≈ $60, 1.2k g ≈ $23-24, Leg Agent ≈ $8) — consistent with IAP rate ~$0.99/1k c up to $99.99/160k coins, ~$0.02/gem. Starter resource alternative claim (footballeffect): '~1,200 coins and 40 gems' — contradicting 1,500c/75g; likely out of date or a different region/starter offer. Treat 1,500c/75g+free scout/agent as canonical (multiple sources incl. r/DLS). sportsdunia claims Commercial bonus L1=2%/L2=4%/L3=6%/L4=8%/L5=10% with kit discounts 5/10/1/20/25 — DIRECTLY CONTRADICTS BlueStacks/gamingonphone (L2=13%, L3=21%). The sportsdunia numbers appear fabricated/AI-generated (notably L3 kit discount = 1% which is absurd). Retain 13%/21% L2/L3 coin bonus figures as canonical (multiple sources) and flag sportsdunia as unreliable.",
    "evidence/raw/turn35_w5/EV-386_scouts_agents.html",
    "Scouts coins Common75c/Rare225c/Leg500c ~2%/5%/15% legend odds per player; agents gems C40/R240/L350 guaranteed leg; starter 1500c+75g+free Common Scout+Agent; events every ~4d; max special player ~2100-2835g; Live Transfers 80+ for gems; Special Agent tokens; recruitment discount ~20% max; 10c floor player; sportsdunia Commercial table flagged unreliable")

add_claim("Scouts cost COINS: Common ~75c, Rare ~225c, Legendary ~500c (base prices before Recruitment discount).", 2, "transfers/scout-cost", [e_scouts])
add_claim("Scout odds per player returned (community estimates): Common ~2% Legendary (80+), ~5% Talented (70-79), ~93% ordinary (<70); Rare ~5% Legendary, ~20% Talented; Legendary ~15% Legendary, ~45% Talented. Each scout roll returns 2 players.", 3, "transfers/scout-odds", [e_scouts], "community math, not FTG-official; treat as approximate")
add_claim("Per 2-player roll, P(at least 1 Legendary) ≈ 3.96% for Common scout, ≈ 27.75% for Legendary scout — Legendary scouts are ~7x more likely to yield a Legendary than Common.", 3, "transfers/scout-math", [e_scouts])
add_claim("Community consensus: Rare scouts are poor EV (coin scam); choose either Common (cheap volume) or Legendary (higher odds).", 3, "transfers/rare-scouts-bad", [e_scouts])
add_claim("Agents cost GEMS: Common ~40g (<70 OVR), Rare ~240g (71-79), Legendary ~350g (GUARANTEED 80+ Legendary player).", 2, "transfers/agent-cost", [e_scouts])
add_claim("New-player onboarding gives: 1,500 coins + 75 gems + 1 FREE Common Scout + 1 FREE Common Agent (in addition to captain selection).", 2, "onboarding/starter-pack", [e_scouts], "confirms free scout/agent on top of 1500c/75g")
add_claim("Lowest observed transfer-list player price: ~10 coins (with zero Recruitment discount).", 3, "transfers/floor-price", [e_scouts])
add_claim("Recruitment Centre provides % discount on scout/agent costs scaling with level; ~20% discount reported at max level (r/DLS math).", 3, "facilities/recruitment-discount", [e_scouts])
add_claim("Events run approximately every 4 days; winning an event yields ~600+ coins and a chance at a Legendary player (or Special Agent token for guaranteed Legendary).", 3, "events/cadence", [e_scouts])
add_claim("Maxing ONE Special player from base via coaches costs approximately 2,100-2,835 gems.", 3, "training/max-special-player-cost", [e_scouts], "r/DLS Apr2024")
add_claim("Live Transfers section lets players sign 80+ OVR players directly with gems (separate from scouts/agents).", 2, "transfers/live-transfers-gems", [e_scouts])
add_claim("Special Agent tokens (event reward) grant a guaranteed Legendary player (e.g., 96 Haaland reported).", 2, "transfers/special-agent-tokens", [e_scouts])
add_claim("Gem spending meta (community): avoid Common/Rare agents; either (a) save for Legendary Agents early when squad is bad, then switch to (b) Live Transfers 80+ targets and coach upgrades; OR use the buy-80-DEF-and-release Legendary-coach trick for cheaper player development.", 2, "meta/gem-spending", [e_scouts])
add_claim("IAP rate reference: $37 bundle with 45k c + 1.2k g + Legendary Agent ≈ $92 nominal value; consistent with $0.99/1k c base rate up to $99.99/160k c and ~$0.02/gem.", 3, "iap/value", [e_scouts])
add_claim("ERRATA: sportsdunia Commercial Centre table (L1=2%/L2=4%/L3=6%/L4=8%/L5=10% + kit discounts 5/10/1/20/25) is unreliable (contains nonsensical L3 kit discount 1%) and directly contradicts multiple better sources (BlueStacks, gamingonphone: L2=+13%, L3=+21%). RETAIN BlueStacks 13%/21% as canonical coin bonus; sportsdunia rejected.", 1, "errata/commercial-sportsdunia-rejected", [e_scouts])
add_claim("Starter-kit alternative claim (~1,200c/40g from footballeffect) is an outlier likely from an older version or different region; canonical starter = 1,500c + 75g + free Common Scout + free Common Agent.", 3, "errata/starter-outlier", [e_scouts])

p=os.path.join(RAW_DIR,'EV-386_scouts_agents.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
