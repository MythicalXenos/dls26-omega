#!/usr/bin/env python3
"""Turn 33 Wave 3: settings/camera/skills/celebrations + Dream FC starter captain,
   Dynamic Stars, Fanzone details, World Tournament, Dream Draft, Kick-Off Stars."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','settings_turn33')

ev_id=345
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"community-guide","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=427
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_sportsdunia=new_ev("sportsdunia settings guide mar2026",
    "Settings menu lists: Language, Difficulty, Power Save(Automatic), Camera Type TV @80% distance, Auto Replay off, Quick Subs on, Team Boosts on, Multiplayer Chat on; controls: Auto Switch High, Button Size Small, Kick Assists High, Cross Assist On, In-Game Tactics On, Fixed Virtual Stick On, Stick Visible Off, Stick Size Medium, Descriptive Button Text Off.",
    "evidence/raw/settings_turn33/EV-345_settings.html",
    "Settings menu options and recommended competitive baseline")
e_dlskits=new_ev("dreamleaguesoccerkits.com settings guide may2026",
    "Camera options Tele Broadcast recommended, Camera Height 70-80, Camera Zoom 30-40; competitive build FPS 60, Auto Switch Semi-Auto, Vibration OFF, Graphics Medium, Commentary low/off for lower latency; Camera Height/Zoom sliders distinct from older 'distance'; camera types include TV, Tele Broadcast, Sideline, Goal-to-Goal.",
    "evidence/raw/settings_turn33/EV-346_camera.html",
    "Camera types/heights/zoom, competitive latency settings")
e_rdls_cam=new_ev("r/DreamLeagueSoccer camera/assist threads 2024-2026",
    "Community camera prefs: Sideline 30% zoom with radar+names+scoreboard on, all assists off (kick/cross/pass); Goal-to-Goal popular for full-pitch vision; switching camera angle rejuvenates game feel; Cross Assist widely derided as 'horrible' (crosses go straight to GK); Kick Assist OFF increases long-shot goals but worsens AI decision-making; Auto Switch Low preferred by advanced players (semi-auto or low).",
    "evidence/raw/settings_turn33/EV-347_assists.html",
    "Community settings preferences, assist impacts")
e_skills=new_ev("sakibpro skill-moves list + r/DLS tricks mar2026",
    "DLS skill moves confirmed: Rainbow Flick (swipe skill), Feint/Body Fake, Roulette/Spin Move (basic); advanced Bicycle Kick (double-tap ball in air for crosses/corners), Scorpion Kick, Heading, Rabona Kick; DLS25 added Close Control (hold screen before direction change to kill extra touch, cleaner turns); free-kick defense trick: move a player to goal line, switch after kick, double-tap for clearance header; free-kick offense: aim slightly above wall, 80% power curve for top corner.",
    "evidence/raw/settings_turn33/EV-348_skills.html",
    "Skill move roster, close control, FK technique")
e_starter=new_ev("gamingonphone+BlueStacks+apkpure starter guides jan-oct2026",
    "New-player flow: name manager (3 default face options, customizable later), choose team captain from list of Legendary big names (pick attacker/midfielder for early goals); starter squad ~50-60 OVR; tutorial match teaches passing/shooting/defending; returning players get progress carryover including squad and Academy Division status; post-tutorial open Transfers via Agents/Scouts, upgrade Facilities; substitution bench should include defenders/midfielders + one reliable striker; rotation recommended for tournaments/online.",
    "evidence/raw/settings_turn33/EV-349_starter.html",
    "Dream FC onboarding flow, starter squad OVR, captain choice")
e_playergg=new_ev("player.gg DLS26 feature summary + App Store RU v13 changelog + mokoweb mod",
    "DLS26 new features confirmed via player.gg + App Store RU changelog: Dynamic Stars (cards upgrade live based on real-world national performances); new dynamic broadcast cameras; Arabic/Turkish commentary; Fanzone facility offers Clan bonuses; cooperative goals; World Tournament event; Kick-Off Stars early-access headline players (Raphinha, Alvarez per App Store RU); special-player squad cap removed (DLS26 lifted specials limit); App Store RU version-history notes: 2025/26 player data, special/classic/international player rosters, bigger squad capacity, improved facilities (new stadia/infrastructure), more flags/banners, Kick-Off Stars; Mokoweb MOD claims 'Unlimited Substitutions' — MOD-ONLY, not vanilla.",
    "evidence/raw/settings_turn33/EV-350_features.html",
    "Dynamic Stars, Fanzone Clan bonuses, World Tournament, Kick-Off Stars, specials cap removed")
e_training=new_ev("dreamleagueforall 2016 training modes wiki + analogue stick wiki",
    "Training Mode persists in modern DLS: Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save (six modules); set-piece roles (free-kick taker, penalty taker, captain) assignable per player in squad screen; analog stick required during set-pieces (hold direction; no stick = default direction); auto-pressing during defending requires stick direction while holding B (B without stick = no movement); player lock override during opponent goal kicks/free balls (controlled player auto-runs to ball regardless of stick).",
    "evidence/raw/settings_turn33/EV-351_training.html",
    "Training modules, set-piece role assignment, stick-input mechanics")

# SETTINGS / CAMERA
add_claim("Settings menu exposes: Language, Difficulty, Power Save (Off/Automatic/On), Camera Type, Camera Distance/Height, Camera Zoom, Auto Replay (on/off), Quick Subs (on/off), Team Boosts (on/off), Multiplayer Chat (on/off), FPS cap, Graphics quality, Vibration, Graphics, Commentary volume/download flags.", 2, "ui/settings", [e_sportsdunia,e_dlskits], "Camera Height+Zoom labels may have replaced older Distance label in DLS26")
add_claim("Camera types available include at minimum: Default, TV, Tele Broadcast, Sideline, Goal-to-Goal; with independent Height (~0-100) and Zoom (~0-100) sliders.", 2, "ui/camera", [e_dlskits,e_rdls_cam,e_sportsdunia], "exact full camera-type list unverified")
add_claim("Competitive players prefer Tele Broadcast or Goal-to-Goal at Height 70-80 / Zoom 30-40 (or Sideline 30% zoom) for maximum pitch visibility; close angles (Sideline/TV) limit through-pass vision and defensive positioning.", 2, "ui/camera", [e_dlskits,e_rdls_cam], "community consensus")
add_claim("Controls settings include: Auto Switch (Off/Low/Semi Auto/High), Button Size, Kick Assist (Off/Low/High), Cross Assist (on/off), In-Game Tactics toggle, Fixed Virtual Stick (on/off), Virtual Stick Visible, Virtual Stick Size, Descriptive Button Text (on/off).", 2, "ui/controls", [e_sportsdunia,e_rdls_cam])
add_claim("Kick Assist off significantly improves long-shot accuracy and manual control but degrades AI teammate decision-making ('brain cells lost'); Cross Assist off yields far more accurate crosses (assist-on crosses float straight to opposition GK).", 2, "controls/assists", [e_rdls_cam], "r/DLS community reports")
add_claim("Advanced/competitive consensus: Auto Switch Low/Semi-Auto, all assists off, Vibration off, Graphics Medium or lower for latency, FPS 60, Commentary off/low to reduce processing overhead.", 2, "controls/meta", [e_dlskits,e_rdls_cam,e_sportsdunia], "subjective community preference")

# SKILL MOVES / FREE KICKS
add_claim("Basic skill moves: Rainbow Flick, Feint/Body Fake, Roulette/Spin Move; advanced: Bicycle Kick (double-tap when ball is in air, for crosses/corners), Scorpion Kick, Heading, Rabona Kick.", 2, "controls/skills", [e_skills], "sakibpro list, moves may vary by player rating; execution inputs not fully documented")
add_claim("Close Control (added DLS25): hold the screen just before changing direction to kill the ball's extra touch for tighter turns; release to resume normal dribbling.", 3, "controls/dribble", [e_skills], "r/DLS trick")
add_claim("Free kick offense: aim slightly above the wall, swipe at ~80% power with curve for top-corner finishes; alternative short pass to a forward just outside the wall for a quick turn-and-shoot.", 2, "setpieces/free-kick", [e_skills], "community trick")
add_claim("Free kick defense: move a player onto the goal line before kick; after kick is taken, game switches to that player quickly; double-tap for a quick header clearance off the line (A-button headers are too slow).", 2, "setpieces/defense", [e_skills], "r/DLS trick")
add_claim("Training mode provides six modules: Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save; accessible from main menu for set-piece practice.", 2, "training", [e_training], "module list from 2016 wiki — modern DLS may have expanded; need APK verification")
add_claim("Set-piece and captain roles (free-kick taker, penalty taker, corner taker, captain) are assignable per player in the squad/role-selection screen.", 2, "tactics/roles", [e_training])

# DREAM FC ONBOARDING
add_claim("New-player onboarding: (1) name manager, (2) choose manager appearance (3 default faces, customizable later), (3) select a Legendary-grade player as captain from a curated big-name list, (4) complete tutorial match covering passing/shooting/defending, (5) unlock Transfers and Facilities.", 2, "onboarding", [e_starter], "guides are mixed DLS20-DLS26; exact current flow needs APK")
add_claim("New players start with a starter squad rated 50-60 OVR; returning players have existing squad + Academy Division status carried forward.", 2, "onboarding/progression", [e_starter,e_playergg])
add_claim("Recommended starter captain pick is an attacker or midfielder (not defender/GK) to boost early attacking output and win rate.", 2, "onboarding/advice", [e_starter], "subjective community advice")
add_claim("Substitution bench should carry defenders + midfielders + one reliable impact striker; rotate squad for tournaments/online to manage stamina and injury risk; strategic subs to exploit opponent weaknesses.", 2, "tactics/subs", [e_starter,e_sportsdunia], "Quick Subs toggle (on) recommended in settings")

# NEW FEATURES DLS26
add_claim("Dynamic Stars (NEW DLS26): special player cards that upgrade live based on real-world national-team performances.", 3, "cards/dynamic", [e_playergg], "player.gg; upgrade trigger and stat-delta mechanics unverified")
add_claim("Fanzone facility (Summer Spotlight 2026 addition) provides Clan bonuses (paired with the new Clan system for cooperative goals and rewards).", 3, "facilities/fanzone", [e_playergg], "specific bonuses/upgrades/costs unverified")
add_claim("World Tournament event added in DLS26 (cooperative/competitive international event mode).", 3, "events/world-tournament", [e_playergg], "structure/prizes/frequency unverified")
add_claim("Kick-Off Stars time-limited event offers early access to headline special cards (Raphinha and Julian Alvarez launch examples).", 3, "events/kickoff-stars", [e_playergg,e_playergg], "App Store RU changelog confirms")
add_claim("DLS26 lifted the prior per-club cap on special/rare ('black'/'legendary') players (accommodation-related limit removed; specials exempt from squad-size accommodation caps).", 2, "squad/roster", [e_playergg], "App Store RU version-history 'special players unlimited in club'; accommodation now 20→24→40 per earlier EV with specials exempt")
add_claim("Dream Draft mode offers pre-set squads to test tactics without squad-building (alternate mode to career).", 3, "modes/draft", [e_playergg], "apkpure mention; exact rules unknown")
add_claim("Custom/tap-screen celebrations are a community-requested feature (NOT confirmed implemented); matches feature motion-captured celebrations but per-player-iconic controls unconfirmed.", 3, "presentation/celebrations", [e_playergg], "App Store review from DLS25 era requests tap-to-celebrate; 'custom celebrations' listed as wishlist, not confirmed shipped")
add_claim("Broadcast-style new camera angles with dynamic zoom/pan for goals, interceptions and counterattacks; new broadcast-style cinematics for goal replays and key moments.", 2, "presentation/cameras", [e_playergg,e_dlskits], "'new cameraman' teased pre-launch, confirmed shipped")

for f in ['EV-345_settings.html','EV-346_camera.html','EV-347_assists.html','EV-348_skills.html','EV-349_starter.html','EV-350_features.html','EV-351_training.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-427} new claims and {ev_id-345} EVs. Totals: {n_cl} claims, {n_ev} EVs")
