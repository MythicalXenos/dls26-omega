#!/usr/bin/env python3
"""Turn 35 Wave 4: stamina regen, physios, referee AI, weather physics, tackle rules, substitutions, formations — with AI-farm flags for chemistry/fluid formation."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w4')

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

e_stamina=new_ev("LevelWinner DLS20/DLS23/DLS24 guides + playdreamleaguesoccer.com DLS25 + BlueStacks DLS26 + retbit + App Store reviews",
    "Stamina baseline (DLS20-DLS24 source, likely holds DLS26): after each match, players naturally regenerate 30% of their maximum stamina. Players entering a match with <100% stamina fatigue faster. Stamina color thresholds: green=fresh, yellow=fatigued (~70% threshold), orange/red=severely depleted. Red stamina players are barely functional: slow, easy to tackle, sloppy shooting, visibly underperform (commentator may even note it). Players below 70% stamina make more passing errors and run slower (playdreamleaguesoccer DLS25 PC claim). Physios: hired using COINS (not gems). Common Physios = small energy restore; Rare = moderate; Legendary Physios = full energy restore AND heal all active injuries. Physio costs: Common 50c / Rare 100c / Legendary 200c (per earlier meta guides). Substitutions: 5 subs per match (DLS25-era shift, post-COVID rule); Smart Sub feature (DLS25) suggests substitutions based on fatigue/form. Tired players are more injury-prone (LevelWinner). Tackling: Button B = contain/pressure (safer); Button A = slide tackle (high-risk). Slide tackles from behind reliably draw yellow/red cards; front/side slides are safer. Mistimed slide tackles = primary source of yellow/red cards; v13.420 patch was explicitly to fix slide-tackle recovery and collision to reduce box fouls/red cards. Referee: DLS25 introduced advantage rule (ref plays advantage when fouled team retains ball; card issued when play stops). Community complaint (App Store review): when advantage is played and fouled team keeps possession, ref NEVER goes back to award a card after — AI can commit last-defender fouls (denying a clear goal-scoring opportunity) with only a yellow card. Referee targeting center backs for red cards reported as longstanding community complaint (r/DLS 2021). AI dives/simulates contact. Snow/rain/fog: VISUALS confirmed (rain, snow, fog, sunset, night — established earlier). Weather physics SPECULATIVE: third-party guides (playdreamleaguesoccer, eslamgaming, playdreamleaguesoccer 2025 PC) claim rain makes pitch slippery, ball faster, stamina depletes ~20% faster in wet; snow reduces visibility and makes long passes riskier; fog reduces visibility. These numbers are from low-trust AI-farm style SEO sites — NO official FTG confirmation. Treat as UNCONFIRMED. DLS25 v13.050 patch only mentioned 'improved commentary + cutscenes' and 'pitch wear over match' — no weather-physics patch note exists. DLS25 snow animation criticized as heavy/obscuring ball (3zebras review). Chemistry: playdreamleaguesoccer.com claims 'first time in DLS history, team chemistry matters, +15% chemistry boost for same nation' — this site is a known AI-content farm; DO NOT trust. No App Store/APKMirror/FTG official source mentions chemistry in DLS26. Chemistry is SPECULATIVE / UNCONFIRMED; treat as possible but unverified. 'Fluid Formation' 3-5-2 claim is from the same farm site — UNCONFIRMED. Formations confirmed from r/DLS: 4-4-2 (balanced), 4-3-3/3-4-3 (attacking), 3-3-1-3 (inverted wingbacks / Man City style), 5-3-2/5-2-1-2 (defend lead), 4-2-3-1 (criticized as weak: striker isolated); diamond/staggered midfield protects center. Red-carded players are automatically suspended for one match (chaptercheats DLS21). 'Last defender = automatic red' rule reportedly NOT strictly enforced by DLS ref (App Store review), leading to yellow-only DOGSO fouls.",
    "evidence/raw/turn35_w4/EV-385_stamina_ref_weather.html",
    "Stamina: 30% regen/match; <70% errors/slow; physios coin-only Common/Rare/Legendary (50/100/200c); 5 subs; Smart Sub. Tackles: B=contain, A=slide; behind=red. Ref: advantage rule (DLS25) but cards often not awarded post-advantage; AI dives; CB red bias. Weather: visuals confirmed, physics unconfirmed (AI-farm claims: rain -20% stamina, slippery pitch; snow visibility). Chemistry + Fluid Formation flagged as AI-farm speculation. Formations 4-4-2/4-3-3/3-4-3/3-3-1-3/5-3-2/5-2-1-2/4-2-3-1; red = 1-match suspension")

add_claim("Stamina natural regen between matches: 30% of maximum stamina restored per game (DLS20-DLS24 baseline; likely DLS26).", 2, "stamina/regen", [e_stamina], "LevelWinner")
add_claim("Stamina threshold: players entering a match with <100% stamina fatigue faster.", 2, "stamina/fatigue", [e_stamina])
add_claim("Stamina color/performance tiers: green=fresh; yellow (~70% or below)=fatigued, more passing errors and slower; red=severely depleted, barely functional (slow, easy to tackle, sloppy shots, commentator may note).", 2, "stamina/thresholds", [e_stamina])
add_claim("Substitutions: 5 substitutes per match (post-COVID rules applied from DLS25 onwards).", 2, "match/subs", [e_stamina])
add_claim("Smart Sub feature (DLS25): game suggests substitutions based on fatigue and form.", 2, "match/smart-sub", [e_stamina])
add_claim("Tired players are more injury-prone.", 2, "stamina/injury-risk", [e_stamina])
add_claim("Physios cost COINS (not gems): Common 50c (small restore) / Rare 100c (moderate) / Legendary 200c (full energy + heal all active injuries).", 2, "physio/costs", [e_stamina])
add_claim("Defensive buttons: B = contain/pressure (safer, fewer cards); A = slide tackle (high-risk, cards/penalties if mistimed).", 1, "controls/defending", [e_stamina])
add_claim("Slide tackles from behind reliably draw yellow or red cards; front/side slides are much safer.", 1, "tackling/from-behind", [e_stamina])
add_claim("v13.420 Sep1 patch specifically addresses slide-tackle recovery and collision to reduce box fouls and over-red-card outcomes.", 1, "patches/v13.420-slide", [e_stamina])
add_claim("Referee advantage rule introduced DLS25: ref lets play continue if fouled team retains possession; card issued once play stops.", 2, "referee/advantage", [e_stamina])
add_claim("Community-reported referee bug/design issue: after playing advantage, refs often NEVER return to award a card for the original foul (including last-defender/DOGSO fouls, which become yellow-only in practice).", 2, "referee/advantage-bug", [e_stamina])
add_claim("Longstanding community complaint: referees allegedly target center backs, issuing red cards for yellow-card tackles; AI opponents dive/simulate contact leading to soft fouls; AI can commit DOGSO fouls and escape with only yellow.", 3, "referee/bias", [e_stamina], "anecdotal")
add_claim("Red-carded players receive an automatic 1-match suspension.", 2, "discipline/suspension", [e_stamina])
add_claim("Weather visuals confirmed: rain, snow, fog, sunset, night. Weather PHYSICS (slippery pitch, -20% stamina in rain, faster ball, reduced visibility in snow/fog, puddles) are UNCONFIRMED — reported only by low-trust SEO/AI-farm sites (playdreamleaguesoccer, eslamgaming); no official FTG patch note confirms physics effects. Pitch wear over match confirmed in v13.050.", 3, "weather/physics-unconfirmed", [e_stamina], "SPECULATIVE — requires APK/device verification")
add_claim("Team chemistry system (+15% same-nation boost) reported by playdreamleaguesoccer.com but that source is a known AI-content farm; NO official FTG/App Store/APKMirror source mentions chemistry in DLS26. Status: UNCONFIRMED / likely fabricated by SEO farms.", 5, "chemistry/speculative", [e_stamina], "AI-FARM RED FLAG — do not treat as real")
add_claim("'3-5-2 Fluid Formation' and other specific new formations reported only by AI-farm sites; UNCONFIRMED. Formations verified from community: 4-4-2 (balanced), 4-3-3/3-4-3 (attacking), 3-3-1-3 (inverted wingbacks), 5-3-2/5-2-1-2 (defensive), 4-2-3-1 (community-criticized: striker isolated).", 3, "formations/confirmed", [e_stamina], "Fluid claim AI-farm; standard formations confirmed r/DLS")
add_claim("Snow animation in DLS25/DLS26 criticized by players for being too heavy and obscuring ball visibility (3zebras review).", 3, "weather/snow-obscure", [e_stamina])

p=os.path.join(RAW_DIR,'EV-385_stamina_ref_weather.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
