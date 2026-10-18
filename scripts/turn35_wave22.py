#!/usr/bin/env python3
"""Turn 35 Wave 22: weather (cosmetic confirmed / gameplay effect speculative), Youth Academy absent + Academy Division terminology hazard, full dlspedia stadium table, transfer market refresh, eslamgaming errata."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w22')

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

# ---------- EV-407: weather ----------
e_wx=new_ev("eslamgaming 'Visual Evolution of DLS' + 'Gameplay Breakdown' (Mar 2026), r/DreamLeagueSoccer rd0yux (Dec 2021, DLS22 snow), YouTube 'DLS 21 How to Change Weather' (Feb 2021), App Store / Google Play official DLS26 feature lists",
    "WEATHER — cosmetic existence CONFIRMED, gameplay effect SPECULATIVE. Weather visuals (notably snow, and rain) demonstrably exist in the series: r/DLS (Dec 2021, DLS22) shows snow weather screenshots praised purely for looks ('the snow weather goes hard', 'looks more fun and realistic'), and a DLS21 tutorial video exists titled 'How to Change Weather', indicating weather was a selectable visual setting. HOWEVER, every claim that weather affects gameplay physics comes from a SINGLE source: eslamgaming's 'Visual Evolution of Dream League Soccer' article (Mar 2026), which asserts rain makes the pitch slippery and alters traction and ball physics, snow reduces visibility and makes long passes riskier, fog exists, floodlight glare affects goalkeepers, and matches can transition between conditions mid-game. That article is unreliable: the same site publishes obviously fabricated material (a comparison table rating DLS26 as having 'ray-traced shadows on PC' versus FIFA's Frostbite engine, a claim that DLS is an 'open world' game, and a career-mode description listing non-existent 'Junior and Global divisions'). The OFFICIAL App Store and Google Play DLS26 feature lists mention no weather system at all. CONCLUSION: weather is a confirmed visual/cosmetic feature; its gameplay impact remains UNCONFIRMED and is carried at speculative confidence pending device verification.",
    "evidence/raw/turn35_w22/EV-407_weather.html",
    "Weather EXISTS as cosmetic (snow confirmed visually DLS22 r/DLS; DLS21 had a change-weather setting); gameplay effects (slippery pitch, traction, ball physics, visibility, GK glare, mid-match transitions) come ONLY from eslamgaming - an unreliable AI-generated APK site also claiming ray tracing, Frostbite, open world, and non-existent 'Junior/Global' divisions; official store lists mention no weather -> gameplay effect SPECULATIVE",
    quality="community")

add_claim("Weather effects (rain and notably snow) exist in the DLS series as a visual feature, confirmed by DLS22 snow-weather screenshots on r/DLS (Dec 2021) and a DLS21 'how to change weather' tutorial.", 2, "weather/existence-cosmetic", [e_wx])
add_claim("Claims that weather affects gameplay physics - slippery pitch, altered traction and ball physics, reduced visibility in snow, floodlight glare affecting goalkeepers, and mid-match weather transitions - rest on a single unreliable source (eslamgaming) and remain UNCONFIRMED.", 4, "weather/gameplay-effect-speculative", [e_wx], notes="OPEN GAP - was already flagged speculative; now narrowed to one discreditable source")
add_claim("The official App Store and Google Play DLS26 feature lists mention no weather system, which weakens the case for weather having any mechanical role.", 2, "weather/not-in-official-list", [e_wx])
add_claim("eslamgaming is flagged as an unreliable source: it claims DLS26 uses ray-traced shadows on PC, compares it against FIFA's Frostbite engine, describes a football game as 'open world', and lists non-existent 'Junior' and 'Global' divisions in the career ladder.", 3, "errata/eslamgaming-unreliable", [e_wx])

# ---------- EV-408: youth academy absence + stadium table completion + market refresh ----------
e_ya=new_ev("r/DreamLeagueSoccer 16b7z3z (Sep 2023, youth academy feature REQUEST thread), App Store / Google Play official DLS26 feature lists, gamingonphone DLS26 beginner guide, eslamgaming DLS26 career-mode descriptions, dlspedia.fandom stadium table (full), Bluestacks DLS26 character development guide, fifaworldcupnews v13.420 notes, softonic (Feb 2026)",
    "YOUTH ACADEMY ABSENT + TERMINOLOGY HAZARD. There is NO youth academy system in DLS26. The r/DLS thread 'Create player / Youth academy system in DLS 24 (your opinion?)' (Sep 2023) is a player FEATURE REQUEST proposing academy levels 1-5 (OVR 50-53 up to 62-65, 1-3 generated players per season) - proof the system did not exist as of DLS24. Neither the App Store nor Google Play DLS26 feature list mentions a youth academy, and the only player-creation mechanic in the game is 'Create Your Own Captain' during onboarding. TERMINOLOGY HAZARD: 'Academy Division' is the lowest COMPETITIVE DIVISION (division 1 of 8), not a youth academy - new players start there with a squad of unknown players plus one chosen Captain superstar. Softonic's claim (Feb 2026) that recent versions added 'youth academy systems' is unsupported by any official listing. STADIUM TABLE COMPLETION: the full dlspedia.fandom table also lists Elite Division at 80,000 seats and a 'Junior Elite Division' at 60,000 seats (a legacy division name), which narrows the gap to Table A's Elite 70,000 / Legendary 85,000. TRANSFER MARKET: the Live Transfer Market list refreshes after every match played, and as team rating and chemistry improve, higher-quality players appear in the market more frequently (Bluestacks DLS26). New players begin with a basic lineup rated roughly 50-60 OVR (gamingonphone DLS26). VERSION: v13.410 exists as the predecessor to v13.420 (Sep 1 2026, Cult Heroes).",
    "evidence/raw/turn35_w22/EV-408_youth_academy_absent.html",
    "NO youth academy in DLS26 (r/DLS Sep2023 was a feature REQUEST; official store lists omit it; only player creation = Create Your Own Captain at onboarding); 'Academy Division' = lowest of 8 competitive divisions, NOT a youth academy (terminology hazard); dlspedia full table adds Elite 80,000 + legacy 'Junior Elite Division' 60,000; transfer market refreshes after every match, better rating/chemistry = better players; new-player squad ~50-60 OVR; v13.410 precedes v13.420",
    quality="community")

add_claim("DLS26 has NO youth academy system: the r/DLS 'Create player / Youth academy system in DLS 24' thread (Sep 2023) is a player feature request, and no official store listing mentions one.", 2, "career/no-youth-academy", [e_ya], notes="Resolves the open Youth Academy gap as a negative finding")
add_claim("'Academy Division' is the lowest of the eight competitive divisions, NOT a youth academy - new clubs start there with a squad of unknown players plus one chosen Captain superstar. This naming is a recurring terminology hazard.", 2, "career/academy-division-terminology", [e_ya])
add_claim("The only player-creation mechanic in DLS26 is 'Create Your Own Captain' during onboarding; there is no generate-youth-player or regen system.", 2, "career/only-create-own-captain", [e_ya])
add_claim("The complete dlspedia.fandom stadium capacity table lists Elite Division 80,000, a legacy 'Junior Elite Division' 60,000, Division 1 45,000, Division 2 30,000, Division 3 15,000 and Academy 6,462 - bringing it closer to Table A's Elite/Legendary figures.", 3, "facilities/stadium-capacity-table-b-full", [e_ya], notes="'Junior Elite Division' is a legacy name absent from the current 8-division ladder")
add_claim("The Live Transfer Market list refreshes after every match played, and as team rating and chemistry improve, higher-quality players appear in the market more frequently.", 2, "transfers/market-refresh", [e_ya])
add_claim("New DLS26 players begin with a basic lineup rated roughly 50-60 OVR, which improves as more systems unlock.", 3, "career/starting-squad-ovr", [e_ya])
add_claim("DLS26 version 13.410 exists as the immediate predecessor to v13.420 (Sep 1 2026, Cult Heroes announcement).", 3, "patching/v13.410", [e_ya])

p=os.path.join(RAW_DIR,'EV-407_weather.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-408_youth_academy_absent.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
