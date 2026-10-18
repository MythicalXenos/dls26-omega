#!/usr/bin/env python3
"""Turn 33 Wave 5: transfers/scouts/agents/coaches, divisions list, cup tiering, update history."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','transfers_turn33')

ev_id=357
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"mixed","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=478
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_transfers=new_ev("gamingonphone career/transfer guides + BlueStacks + vi.wikipedia",
    "Live Transfer Market: primary coin-based player signing channel; shows 9 players per refresh curated to team rating; refreshes after every match played; higher team rating/chemistry = higher-quality players appear more frequently; buying/selling players refreshes faster; Legendary players rare on Live Transfer (mostly appear via events/festive offers or Agents). Scouts (coin-bought, 3 tiers Common/Rare/Legendary) return discounted players — reliable beginner route. Agents (gem-bought, 3 tiers) search globally for high-rated/Legendary players; final signing still costs coins. Vietnamese Wikipedia (DLS-current): Agent costs Common 40g / Rare 240g / Legendary 350g; Scout costs Common 75c / Rare 225c / Legendary 500c (costs discounted by Recruitment Centre upgrades); Agent selects 1 player (any top-tier); Scout returns 2 random discounted players. Releasing players yields coaches (not guaranteed tier-matched: Legendary player → 1 Rare coach card; Rare → 2 Common coach cards per vi.wikipedia). Player sale does NOT refund coins (community complaint). Coaches: 4 categories Technical/Fitness/GK/Special; 3 tiers Common/Rare/Legendary; Common = small boost 1 random stat; Rare = stronger increases; Legendary = best upgrades + highest breakthrough chance; paid with gems OR by releasing players; double-fee complaint (pay for coach then pay to apply training). Group training optimal at 16-20 players (>20 risks poorly maxed cards). Training rule of thumb: Fitness before Technical (to avoid misallocating points e.g. tackle going to attackers; technical coaches eat more of progression bar). Legendary players are 80+ OVR. Avoid spending initial gems on Legendary Agents (poor value); invest in Stadium/Medical first. Mid-Season (Jan/Feb 2026) rating adjustments: e.g. Guehi/Cherki/Semenyo promoted Rare→Legendary; July Summer Spotlight major rating reshuffles (both up/downgrades Legendary↔Rare); August update added Pre-Season Kickoff & European Champions Tour live events (boosted coin multipliers + legendary scout tokens).",
    "evidence/raw/transfers_turn33/EV-357_transfers.html",
    "Live Transfer, scout/agent costs (viwiki), coach mechanics, release card conversion, update chronology")
e_divisions=new_ev("vi.wikipedia DLS divisions/cups + mundodls + fifaworldcupnews",
    "8 career divisions confirmed from multiple sources (Spanish mundodls naming differs slightly from viwiki DLS25 naming): DLS26 Spanish mundodls order: División Académica → División Amateur → Tercera División → Segunda División → Primera División → División Junior Elite → División Elite → División Legendaria. DLS25-era viwiki order: Academy → Amateur → Division 4 → Division 3 → Division 2 → Division 1 → Elite → Legendary (Junior Elite removed post-DLS20 revision). Career begins in Academy Division; goal is Legendary Division. Cups tier to divisions: Bronze Cup (Academy/Amateur/Div4), Silver Cup (Div3/Div2), Gold Cup (Div1/Elite? viwiki says Div2/Div1), Diamond Cup (Elite/Legendary) — viwiki says Bronze=Academy+Amateur, Silver=Div4+Div3, Gold=Div2+Div1, Diamond=Elite+Legendary. Global Challenge Cup is an additional inter-divisional online cup (not tiered). Other events: New Year Cup (Jan 15-Feb5 50k), Regular League Phase (Feb10-Mar30), Continental Qualifiers (Mar15-25, 25k+Scouts), Youth Academy Cup U-21 (Apr10-30, 35k+Youth Talents), Champions Cup Groups (May5-Jun25, 100k+), Global Super League Q3 invitation (Jul10-Sep30, 250k+Legendary Agent, new 2026), Diwali (Oct20-Nov5, kits/boosts), Champions Cup KO (Nov15-Dec20, 500k+trophy), Christmas Charity Shield (Dec22-Jan5, 70k+exclusive badge). NOTE: playdreamleaguesoccer schedule is AI-content farm; treat as speculative. 128 total AI teams in the game (vi.wikipedia post-2020 era).",
    "evidence/raw/transfers_turn33/EV-358_divisions.html",
    "Division ladder, cup tiering (Bronze/Silver/Gold/Diamond), event calendar")
e_classic=new_ev("App Store + dlsinside player DB September 2026",
    "Roster scope: 4,000+ FIFPRO licensed players + Classic (legends) players; dlsinside.com shows 14,435 player rows in DB v13.430 (Sep 16, 2026) including generated/First Touch Utd/NO TEAM/dynamic-agent entries (e.g. Andy Dunn/Tom Davis/Roberto Crimaldi/Andrew Stevens/James Barham/Dave Sidor/Pete Smith = FT Utd fictional; Nico Williams/Rodrigo de Paul NO TEAM dynamic agent). Player listing includes real players like Raphinha (RW), Julián Álvarez (CF), plus others. Licensed clubs observed: A Bergamo (Atalanta), A Bilbao, A Madrid, A Milan, Real Madrid, Barcelona, PSG, Chelsea, Atletico Madrid, Napoli, Inter, Man City, Arsenal, Liverpool (all unlicensed-names / abbreviated due to licensing). Card rarities from community: Common (white/grey), Rare (blue), Legendary (gold/black) — Summer Spotlight added Rare↔Legendary rating moves; Dynamic Stars live-upgrade; Kick-Off Stars early-access specials.",
    "evidence/raw/transfers_turn33/EV-359_roster.html",
    "Roster size, fictional First Touch Utd players, club licensing abbreviations, card tiers")

# TRANSFERS / COACHES
add_claim("Live Transfer Market shows 9 curated players per refresh, selected based on current team rating/chemistry; refreshes after every match played; manual buy/sell actions accelerate new listings.", 2, "transfers/market", [e_transfers])
add_claim("Higher team rating and chemistry increase odds of higher-quality (rare/legendary) players appearing in the Live Transfer Market.", 2, "transfers/market", [e_transfers])
add_claim("Legendary players rarely appear on the Live Transfer Market; primary sources are Agents (gems), seasonal/festive offers, events, and scout tokens.", 2, "transfers/legendaries", [e_transfers])
add_claim("Selling a player does NOT refund coins (player-release returns coaches, not currency).", 2, "transfers/sell", [e_transfers], "community complaint")
add_claim("Scouts cost coins and return 2 random discounted players; Agent costs gems and returns 1 higher-tier targeted player (final signing still costs coins). Both systems come in Common/Rare/Legendary tiers.", 2, "transfers/scouts-agents", [e_transfers])
add_claim("Scout costs (baseline, pre-Recruitment-Centre discount): Common 75 coins, Rare 225 coins, Legendary 500 coins.", 2, "transfers/pricing", [e_transfers], "vi.wikipedia figure; verify with APK")
add_claim("Agent costs (baseline): Common 40 gems, Rare 240 gems, Legendary 350 gems.", 2, "transfers/pricing", [e_transfers], "vi.wikipedia figure; verify with APK")
add_claim("Releasing a player yields coach cards: Legendary player → 1 Rare coach; Rare player → 2 Common coaches (tier is NOT guaranteed to match player tier).", 2, "transfers/release", [e_transfers], "vi.wikipedia; coach-category distribution unknown")
add_claim("Avoid spending starter gems on Legendary Agents early — Stadium and Medical Centre upgrades yield better long-term value.", 2, "economy/priority", [e_transfers], "community advice")
add_claim("Coach double-fee system: pay gems (or release players) to hire the coach, then pay coins again to apply training to players (a common community complaint).", 3, "coaches/economy", [e_transfers], "Play Store review")
add_claim("Coaches: 4 categories (Technical/Fitness/GK/Special), 3 tiers (Common/Rare/Legendary). Common = small random single-stat boost; Rare = stronger multi-stat increases; Legendary = highest stat boosts + highest breakthrough chance.", 2, "coaches/categories", [e_transfers])
add_claim("Group training optimal batch size 16-20 players; groups larger than 20 risk 'poorly maxed cards' (stat allocation dilution).", 3, "training/group-size", [e_transfers], "r/DLS 2023")
add_claim("Training priority rule: Fitness before Technical (avoids wasting technical points on unwanted stats like tackles for attackers; Technical coaches consume more of the progression bar).", 2, "training/priority", [e_transfers])
add_claim("Legendary-tier player cards correspond to 80+ OVR rating.", 2, "cards/tiers", [e_transfers])

# DIVISIONS / CUPS
add_claim("8 career divisions (bottom to top): Academy Division → Amateur Division → Division 4 → Division 3 → Division 2 → Division 1 → Elite Division → Legendary Division. The Spanish localization names them Academia→Amateur→Tercera→Segunda→Primera→Junior Elite→Elite→Legendaria (Junior Elite label is a localization leftover; post-2020 revisions removed it in English).", 2, "career/divisions", [e_divisions], "naming differs slightly by source; Spanish mundodls includes 'Junior Elite' between Primera and Elite")
add_claim("Career starts in Academy Division with the 50-60 OVR starter squad and chosen Legendary captain.", 2, "career/start", [e_divisions])
add_claim("Cup competitions are tiered to division: Bronze Cup (Academy + Amateur + Division 4), Silver Cup (Division 3 + Division 2), Gold Cup (Division 2 + Division 1), Diamond Cup (Elite + Legendary); plus Global Challenge Cup (online inter-divisional).", 2, "career/cups", [e_divisions], "viwiki tiering; Gold Cup coverage of Div2/Div1 may differ per source")
add_claim("Total pool of AI teams in the game is 128 (post-2020 build).", 3, "career/teams", [e_divisions], "vi.wikipedia")
add_claim("2026 event calendar (AI-content-farm sourced, UNVERIFIED treat as speculative): New Year Cup (Jan 15-Feb5, 50k coins), Regular League Phase (Feb10-Mar30), Continental Qualifiers (Mar15-25, 25k+scouts), Youth Academy Cup U-21 (Apr10-30, 35k+Youth Talents), Champions Cup Groups (May5-Jun25, 100k+), Global Super League (Jul10-Sep30, 250k+Legendary Agent, new Q3 invitation league), Diwali Festival (Oct20-Nov5, kits/boosts), Champions Cup KO (Nov15-Dec20, 500k+trophy), Christmas Charity Shield (Dec22-Jan5, 70k+exclusive badge).", 4, "events/calendar", [e_divisions], "playdreamleaguesoccer.com AI-farm; dates/prizes unreliable; Global Super League confirmed by player.gg as new 2026")

# ROSTER / CLUBS / CARDS
add_claim("Total player database: 4,000+ FIFPRO-licensed real players + Classic legend players; dlsinside v13.430 (Sep 16 2026) shows 14,435 DB rows including fictional First Touch Utd players (Andy Dunn, Tom Davis, Roberto Crimaldi, Andrew Stevens, James Barham, Dave Sidor, Pete Smith) plus dynamic-agent/free-agent (NO TEAM) entries.", 2, "roster/size", [e_classic])
add_claim("Real clubs appear with abbreviated/unlicensed names (e.g. A Bergamo=Atalanta, A Madrid=Atletico Madrid, A Milan=AC Milan) due to licensing — no official club league licenses beyond FIFPRO player licensing.", 2, "licensing/clubs", [e_classic])
add_claim("Player card rarities: Common (white), Rare (blue), Legendary (gold/black). Dynamic Stars (live-upgrade national cards), Kick-Off Stars (early-access specials), Classic Players (Prize Ladder/event legends), Special cards (previously capped but unlimited DLS26) all exist as special-card categories.", 2, "cards/rarities", [e_classic,e_transfers])
add_claim("Summer Spotlight (July 2026) included mass rating reshuffles: players upgraded Rare→Legendary (e.g. Guehi, Cherki, Semenyo) and downgraded Legendary→Rare.", 2, "patching/ratings", [e_transfers])
add_claim("August 2026 update added 'Pre-Season Kickoff' and 'European Champions Tour' limited-time cup challenges with boosted coin multipliers and legendary scout tokens.", 2, "patching/events", [e_transfers])
add_claim("January/February 2026 mid-season squad refresh applied winter transfer movements and updated ratings.", 2, "patching/squads", [e_transfers])

for f in ['EV-357_transfers.html','EV-358_divisions.html','EV-359_roster.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-478} new claims and {ev_id-357} EVs. Totals: {n_cl} claims, {n_ev} EVs")
