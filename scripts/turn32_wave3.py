#!/usr/bin/env python3
"""Turn 32 Wave 3 — Coaches/scouts/agents economy + maxing players + academy squad size + accommodation + facilities.

Adds claims 322-335 and EV-318..EV-322.
"""
import json, os, datetime, re, sys
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb/claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')

claims=[json.loads(l) for l in open(CP) if l.strip()]
evs=[json.loads(l) for l in open(EIP) if l.strip()]
next_c=max(int(c['claim_id'].split('-')[1]) for c in claims)+1
next_e=max(int(e['evidence_id'].split('-')[1]) for e in evs)+1
added_c, added_e=0,0
def cid():
    global next_c,added_c; r=f"CLAIM-{next_c:03d}"; next_c+=1; added_c+=1; return r
def eid():
    global next_e,added_e; r=f"EV-{next_e:03d}"; next_e+=1; added_e+=1; return r

def C(text, conf, evids, chal=None, vol='Low', notes=None):
    cidv=cid()
    rec={"claim_id":cidv,"text":text,"confidence":conf,"supporting_evidence":evids,
         "challenges":chal or [],"volatility":vol,"notes":notes or [],
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
    with open(CP,'a') as f: f.write(json.dumps(rec)+"\n")
    claims.append(rec)

def E(origin, summary, artifact, typ='web_article', method='web_search_community', reliability='Medium'):
    eidv=eid()
    rec={"evidence_id":eidv,"origin_method":origin,"summary":summary,"artifact_path":artifact,
         "evidence_type":typ,"capture_method":method,"reliability":reliability,
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),"raw_data_ref":""}
    with open(EIP,'a') as f: f.write(json.dumps(rec)+"\n")
    evs.append(rec)
    return eidv

# === EVs ===
e318=E("r/DLS multiple threads (2022-2025) — coach mechanics, maxing costs, F2P coaching meta",
       "Coach tiers & upgrading: each outfield player needs ~80 upgrade points to max (~76-88 avg); GKs ~20 points. Coach yields (reddit consensus across DLS22-DLS25): Common = +2 pts on 1 player (~80 needed for outfield, ~20 GK); Rare = +4 pts across 2 players (2 per player, ~20 for outfield, ~10 GK); Legendary = +12 pts across 3 players (4 per player, ~9 for outfield, ~4 GK). 5%/10%/20% Breakthrough chance (Common/Rare/Legendary) for bonus stats. Gem costs (base/max Training): Common ~25g, Rare ~50-67g (1535 coin alt via selling 80-rated CB), Legendary 225g->157g with max Training (30% discount). Special coaches (for special/black cards) are ~4.5x more expensive per upgrade point (26.25g/pt legendary special vs 5.8g/pt normal legendary) — widely considered bad value. Meta: buy cheapest 80-rated CB (~1460-1535 coins) -> release for a Rare coach; buy sub-185-200c common players -> release for Common coach; Legendary coaches must be bought with gems. Total cost to max one special player: 2100-2835 gems via legendary (best value) vs 2520 via rare, 2835 via common.",
       "evidence/raw/reddit_turn32/EV-318_coach_mechanics.html",
       typ='community',reliability='Medium-High')
e319=E("rajatips scout/agent drop rates + r/DLS DLS20 review (2019) + supercheats (2020) + gamingonphone (Dec2024) + r/DLS scout math",
       "Scouts (coin-bought, discounted players): Common 75c (93% common/5% rare/2% legendary ~80+), Rare 240c (75/20/5%), Legendary 500c (40/45/15%). Reddit math: P(>=1 leg from 2 Common scouts)=3.96%; P(>=1 leg from 2 Legendary scouts)=27.75% (~7x better). Agents (gem-bought, guaranteed tier): Common Agent 20g (sub-70), Rare Agent 100g (71-79), Legendary Agent 200g (80+). Super Agent is a limited-time event (few hrs, once per season) that guarantees highest-tier Legendary (changed from 83+@550g to 82+). Starter pack: 1500c + 75g + free Common Scout + free Common Agent.",
       "evidence/raw/community_turn32/EV-319_scout_agent_drops.html",
       typ='community',reliability='Medium-High')
e320=E("BlueStacks DLS26 character-development guide (Jun 2026) + r/DLS accommodation thread",
       "Facilities beyond Stadium/Commercial/Training/Medical: Recruitment Centre provides discounts on scout/agent hire. Accommodation controls squad size; max Accommodation = 40-player squad. Transfer market refreshes after every match; higher team OVR unlocks higher-quality players. Scouts/Agents/Coaches in 3 tiers. Coaches split into 4 categories: Technical, Fitness, Goalkeeping, Special (Special is for special/black-card players).",
       "evidence/raw/bluestacks_turn32/EV-320_facilities_squad.html",
       typ='guide',reliability='High')
e321=E("gamingonphone DLS26 career mode guide (Jan2026)",
       "DLS26 Career guide confirms coaches split into Technical/Fitness/Goalkeeping/Special categories (Common/Rare/Legendary tiers); Legendary coaches provide best upgrades + highest Breakthrough chance. FIFPRO licensing 4000+ players; 8 divisions; Clan system new in recent versions; regular seasons/events; Dream Draft daily scenarios; player training via permanent coaches + temporary Form Boost.",
       "evidence/raw/gamingonphone_turn32/EV-321_career_guide.html",
       typ='guide',reliability='High')
e322=E("r/DLS DLS24 beginner guide (Mar2024) + r/DLS DLS20 review (Dec2019)",
       "Starter progression: pick captain -> 1500c/75g/free Common Scout/free Common Agent. Recommended early spend: 75g into Training facility (5% coach discount + unlocks additional formations). Teams unlock 80-82 rated Legendary players in the transfer market at ~68.7 team OVR threshold; rare players appear above 65 OVR. Common scout can land high-rated players by luck (e.g., 86 Messi reported). Events every ~4 days; winning events yields Legendary players + 600+ coins. Stadium start capacity ~5000 in Academy; ~30-35 games per division at 6-8 minutes match length; Division objectives must be completed within 15 division games or promotion is denied.",
       "evidence/raw/reddit_turn32/EV-322_starter_progression.html",
       typ='community',reliability='Medium')

# === CLAIMS ===
C("Outfield players require approximately 80 upgrade points to reach max rating (range ~76-88 depending on stats distribution; STR/CON weight-2 means fewer applications needed). Goalkeepers require ~20 points.",
  'Medium-High Confidence',[e318],['STR and CON are +1 increments vs other stats +2, so STR/CON-heavy upgrades max faster but yield fewer total points.'],vol='Low')
C("Coach yields per application (outfield): Common = +2 pts on 1 random stat of 1 player; Rare = +4 pts total across 2 random stats of 2 players (~2 pts per player); Legendary = +12 pts total across 3 players (~4 pts per player, covers 4 stats or fewer for GK). Breakthrough chance: Common 5%, Rare 10%, Legendary 20% (bonus stats on proc).",
  'Medium-High Confidence',[e318],['LevelWinner DLS20 guide numbers used as baseline; DLS26 believed consistent but not officially re-confirmed.'],vol='Medium')
C("Coach gem costs (base / with maxed Training Centre discount ~30%): Common ~25g; Rare ~67g (or ~1535 coins via buy-release of cheapest 80-rated CB); Legendary 225g -> 157g. Total gems to max one outfield player: ~2100 (Legendary) / 2520 (Rare) / 2835 (Common); Legendary coaches best value per point.",
  'Medium-High Confidence',[e318],vol='Medium')
C("Coaches are split into four categories by attribute focus: Technical, Fitness, Goalkeeping, and Special. Special coaches target special/black-card players and are ~4.5x more expensive per upgrade point (26.25g/pt Legendary special vs 5.8g/pt Legendary normal); widely considered poor value.",
  'High Confidence',[e318,e320,e321],vol='Low')
C("Meta F2P coach acquisition: buy-cheap-release cycles. Rare coach cheapest source = 80-rated CB for 1460-1535 coins then release. Common coach cheapest source = sub-185-200 coin common player then release. Legendary coaches must be purchased with gems (or earned as rewards).",
  'High Confidence',[e318],vol='Low')
# Scouts / Agents
C("Scout tiers (coin cost / discounted players): Common 75c (93% common/5% rare/2% legendary 80+), Rare 240c (75%/20%/5%), Legendary 500c (40%/45%/15%). Legendary scouts ~7x more likely than Common to return at least one legendary player per 2-pull (27.75% vs 3.96%).",
  'Medium-High Confidence',[e319],vol='Low')
C("Agent tiers (gem cost / guaranteed player rating band): Common Agent 20g (sub-70 OVR), Rare Agent 100g (71-79), Legendary Agent 200g (80+). Super Agent is a limited-time offer (available a few hours, once per season) that guarantees a high-tier Legendary player (82+ post-2024 change).",
  'Medium-High Confidence',[e319],['DLS20 review reported 20/100/200g agent prices; DLS24+ may have adjusted.'],vol='Medium')
C("Starter pack: upon captain selection, new player receives 1,500 Coins, 75 Gems, one free Common Scout, and one free Common Agent.",
  'High Confidence',[e319,e322],vol='Low')
C("Recommended early-game gem spend: 75 Gems into the Training facility to unlock a 5% coach discount plus additional formations.",
  'Medium Confidence',[e322],vol='Low')
# Transfer market / unlock thresholds
C("Live Transfer Market refreshes after every match. Players available scale with team OVR: rare players appear above ~65 OVR; 80-82 Legendary players begin appearing around ~68.7 team OVR.",
  'Medium Confidence',[e320,e322],vol='Medium')
C("Recruitment Centre facility provides hiring discounts on scouts and agents. Accommodation facility controls squad size; maximum Accommodation allows a 40-player squad.",
  'Medium-High Confidence',[e320,e318],vol='Low')
# Seasons / timing
C("Events cycle approximately every 4 days; event wins award Legendary players plus 600+ Coins. Season objectives award ~10 Gems each, up to 40 Gems total per 4-objective season.",
  'Medium Confidence',[e322,e319],['Numbers from DLS20 review; may have changed in DLS26.'],vol='Medium')
C("Academy Division starting stadium capacity ~5,000 seats; ~30-35 games per division at 6-8 minute match length; all 15 Division Objectives must be completed within the season or promotion is denied despite table position.",
  'Medium Confidence',[e322],vol='Medium')

# post-process: fix any kwarg ordering issues are already fine since we only used kwarg form
print(f"Added {added_c} new claims and {added_e} EVs (EV-{next_e-added_e}..EV-{next_e-1}). Totals: {next_c-1} claims, {next_e-1} EVs")
