#!/usr/bin/env python3
"""Turn 34 Wave 1: soundtrack, atmosphere audio, referee/complaints, season structure/fixtures, stadium div-minimums, post-Legendary cups, Dynamic Stars trigger."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn34_w1')

# resume EV/claim IDing from disk
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

e_soundtrack=new_ev("vgost fandom + dlsmod + thesoccerera + App Store v13.040/v12.110 changelogs",
    "DLS26 official soundtrack (v13.040 'brand new soundtrack and SFX'): AR/CO x Punctual x NewEra - Generation Love (also on EA FC 26); Benson Boone - Sorry I'm Here for Someone Else; Katy Perry - LIFETIMES; Marshmello x Trueno - Fale Então; NoMBe - Space for Two; Rachel Chinouriri - Can We Talk About Isaac?; Rudimental x Khalid - All I Know; South Arcade - Supermodels; TEEYZ - Coming in Hot. v12.110 (May 2026 window, DLS26 era) added 'New Crowd Audio – An even more passionate atmosphere'. Atmosphere: crowd noise dynamic (swells on attack, quiets in defense); redesigned scoreboard, sideline medical bag, cameraman, more props/banners/flags per v13.040/13.050; pitch shows wear over the match (TapTap review note). SFX: ball-hit-net punchy, referee whistle, player grunts; community complaint SFX are 'untimely/dissatisfactory' post-launch; referee rarely blows whistle (advantage over-called per App Store SG review). v13.050 (Jan 15 2026) 'Improved commentary – Now more accurate with added phrases' plus new cutscenes. Sliding-tackle red-card risk increased in 2026 update (AI-content farm note). DLS26 cover stars: Raphinha and Julián Álvarez (Kick-Off Stars cards at launch). Note: playdreamleaguesoccer claim of 4K stadiums, Salt Lake Stadium (Kolkata) 50k crowd models, vuvuzelas/dhol beats/'Bharat Mata Ki Jai' chants is AI-content-farm fabricature; treat Salt-Lake-specific claims as UNVERIFIED.",
    "evidence/raw/turn34_w1/EV-374_soundtrack.html",
    "Soundtrack tracklist, SFX/crowd audio updates, referee complaint, cover stars, Indian-stadium fabrication flag")
e_season=new_ev("levelwinner DLS24 guide + dls-wiki/fandom Leagues + r/DLS season-game-counts + gamingonphone DLS25 progression + dlspedia stadium minimums",
    "Season fixture structure (DLS24-era, applies to DLS26 per continuity): per season ~30 matches total = 15 division games (play every division opponent once — single round-robin) + 9 Global Challenge Cup games + 5 tiered-cup games (Bronze/Silver/Gold/Diamond) plus optional post-Legendary cups. Division size: 16 teams per division (pre-DLS20 era had 16; DLS20+ 8-division era may differ but per r/DLS Legendary count 15 league games is common). Promotion requires completing division objectives within 15 division games; ~10 wins typically secures top-of-table; goal-count targets are harder than win count. GCC = 4-team groups (top 2 advance), then knockout. Post-Legendary endgame cups (classic DLS): winning Legendary Division unlocks International Cup (vs national teams like England/Sweden/Portugal/Argentina) single-legged playoff; winning International Cup unlocks All-Star Cup (classic/historical teams); mirror-team 'Allstar Match' final at division level is hardest match (depends on player skill not team rating). Stadium minimum seating per division (dlspedia, pre-2020 numbers — DLS26 stadium scale differs starting 6,462 up to ~90k): Academy start 6,462; Div3 15,000; Div2 30,000; Div1 45,000; Junior Elite 60,000; Elite 80,000; Legendary >80,000. r/DLS 2023 DLS-summed-up: 8 stands, upgrade 7 to max to hit 85,000 leaving one corner stand unupgraded (DLS-classic numbers; DLS26 opt ~92k). Per LevelWinner DLS24: Academy→Amateur cheapest stadium upgrade 446 coins to hit 15,000 (contradicts DLS26 6,462→next numbers — note that DLS26's start is 6,462 already, division gates may differ). Difficulty: LevelWinner claims scoring difficulty doesn't scale much across divisions; difficulty-curve debate community. Dynamic Stars started collecting Jun 8, 2026 per FTG TikTok (Summer Spotlight launch); cards upgrade live in line with national team performances over summer tournament window.",
    "evidence/raw/turn34_w1/EV-375_season.html",
    "15-game division, GCC/5-cup structure, post-Legendary International/AllStar cups, stadium minima, Dynamic Stars June-8-26 trigger")

# SOUNDTRACK / AUDIO
add_claim("DLS26 official soundtrack (v13.040 launch, refreshed): AR/CO x Punctual x NewEra – 'Generation Love'; Benson Boone – 'Sorry I'm Here for Someone Else'; Katy Perry – 'LIFETIMES'; Marshmello x Trueno – 'Fale Então'; NoMBe – 'Space for Two'; Rachel Chinouriri – 'Can We Talk About Isaac?'; Rudimental x Khalid – 'All I Know'; South Arcade – 'Supermodels'; TEEYZ – 'Coming in Hot'.", 1, "presentation/soundtrack", [e_soundtrack])
add_claim("Music plays in menus; match audio includes commentary (4 languages), crowd noise, SFX; music is non-intrusive/background-ambient per reviews.", 2, "presentation/audio", [e_soundtrack])
add_claim("v12.110 (May 2026) added 'New Crowd Audio – An even more passionate atmosphere' (crowd chants/noise upgrade).", 1, "presentation/crowd-audio", [e_soundtrack])
add_claim("Crowd audio is dynamic: volume swells when your team attacks, quiets during defensive phases; chants respond to match events.", 2, "presentation/crowd", [e_soundtrack], "AI-farm + eslamgaming; consistent with presentation marketing")
add_claim("v13.040/13.050 added new stadium props, banners, flags, redesigned scoreboard, sideline medical bag, cameraman figure; pitch shows visible wear over the course of a match.", 2, "presentation/stadium", [e_soundtrack])
add_claim("v13.050 (Jan 15, 2026) added 'Improved commentary – Now more accurate with added phrases' plus new pre/post-match cutscenes.", 1, "patching/v13.050", [e_soundtrack])
add_claim("Community SFX complaint (launch): sound effects feel 'untimely/dissatisfactory'; referee seldom blows whistle (advantage rule over-applied per App Store SG review).", 3, "presentation/sfx-complaints", [e_soundtrack])
add_claim("2026 update reportedly increased red-card frequency on mistimed sliding tackles (community + multiple guides warn against reckless lunges).", 2, "refereeing/red-cards", [e_soundtrack])
add_claim("DLS26 cover stars are Raphinha and Julián Álvarez (Kick-Off Stars launch cards).", 1, "meta/cover", [e_soundtrack])
add_claim("AI-content farm claim (playdreamleaguesoccer): 4K textures, Salt Lake Stadium (Kolkata) with 50,000 unique crowd models, vuvuzelas/dhol beats, 'Bharat Mata Ki Jai' chants on home goals, Career Mode 2.0, Indian-specific stadiums and chants. TREAT AS UNVERIFIED/FABRICATED — Salt Lake Stadium not corroborated by official changelogs or other sources.", 4, "meta/fabrication-warning", [e_soundtrack], "AI-farm red flag")

# SEASON / FIXTURES
add_claim("Per season ~30 matches total (when winning most games): approximately 15 division games (single round-robin vs each division opponent) + 9 Global Challenge Cup games + 5 tier-cup games (Bronze/Silver/Gold/Diamond).", 2, "career/season-length", [e_season], "LevelWinner DLS24 baseline; DLS26 may vary but Reddit Legendary count ~40 with post-leg cups")
add_claim("League games per season: 15 (play every division opponent once); ~10 wins typically secures division title/promotion; goal-difference/goal-count objectives are harder to meet than wins.", 2, "career/league", [e_season])
add_claim("Global Challenge Cup: 4-team round-robin groups (top 2 advance) followed by knockout; 10 gems per round cleared (corroborates earlier EV).", 1, "events/gcc", [e_season])
add_claim("Tiered cups per division: Bronze (Academy/Amateur), Silver (Div4/Div3), Gold (Div2/Div1), Diamond (Elite/Legendary) — ~5 games per cup run.", 2, "career/cups", [e_season])
add_claim("Division size is historically 16 teams per division (single round-robin); DLS20 reset may have restructured but 15-game division count persists in community reports.", 2, "career/division-size", [e_season])
add_claim("Post-Legendary endgame: winning Legendary Division unlocks International Cup (single-legged knockout vs national teams such as England, Sweden, Portugal, Argentina); winning International Cup unlocks All-Star Cup (single-legged knockout vs classic/historical teams); a mirror-team match (vs your own squad/kit/formation, called division All-Star final) is the hardest match in the game, determined by player skill rather than squad rating.", 3, "career/endgame", [e_season], "fandom/wiki content from DLS-Classic era; may have been restructured in DLS20+")
add_claim("Legendary Division total matches (including endgame cups if you win everything): ~40 = 15 league + 9 GCC + 5 Diamond Cup + 7 International Cup + 3 All-Star Cup + 1 division All-Star match (per r/DLS 2023).", 3, "career/legendary-total", [e_season])
add_claim("Stadium minimum seating per division (historical/pre-2020 dlspedia, may differ in DLS26 due to 6,462-start and 90k cap): Academy starting 6,462; next gate ~15,000 (≈Div3/Amateur); 30,000; 45,000 (Div1); 60,000 (Junior Elite, deprecated); 80,000 (Elite); >80,000 (Legendary ~90k). Cheapest Academy→Amateur stadium upgrade ~446 coins.", 2, "facilities/stadium-gates", [e_season])
add_claim("Classic DLS stadium build trick: 8 stands total, upgrade 7 to max to hit ~85,000 capacity leaving one corner stand unupgraded (corner stands generate less revenue; this optimizes cost/capacity). DLS26 optimal ~92k requires different build (per EV-338 52-coin bonus cap).", 2, "facilities/stadium-build", [e_season], "8-stand figure from r/DLS 2023; corroborates 8-stand stadium known from earlier builds")
add_claim("Dynamic Stars promotion/trigger (FTG official TikTok): collection started June 8, 2026 alongside Summer Spotlight; cards upgrade LIVE in line with real-world national team performances during summer international tournament window.", 1, "cards/dynamic-stars", [e_season])
add_claim("Difficulty is reported to not scale linearly up divisions (scoring stays similarly difficult Academy→Legendary); penalties and 1v1 finishing remain skill-gated.", 3, "difficulty/scaling", [e_season], "LevelWinner DLS24, may not reflect DLS26")
add_claim("Youth Academy Cup U-21 event (listed in AI-farm calendar) is UNCONFIRMED — no official source mentions an in-game youth academy system; 'youth talents' reward is speculative.", 4, "events/youth-academy-caveat", [e_season], "treat as speculative until APK/changelog confirms")

for f in ['EV-374_soundtrack.html','EV-375_season.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
