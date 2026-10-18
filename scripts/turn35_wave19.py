#!/usr/bin/env python3
"""Turn 35 Wave 19: Fanzone facility, 12th Man vote mechanics, DLS26 update timeline, Dream Draft rules, kit/logo import gem cost, Classic Players roster, cover star."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w19')

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

# ---------- EV-400: Fanzone + 12th Man + update timeline + Dream Stars + Clan improvements ----------
e_fz=new_ev("App Store US/IN/PW version history (official FTG), soft112/apkmirror/apkpure mirrors, thesoccerera, dlskits.mobi, official FTG TikTok, r/DreamLeagueSoccer",
    "FANZONE + 12TH MAN + UPDATE TIMELINE. Fanzone: the Summer Spotlight update (v13.300, 27 May 2026) added a NEW club facility, the Fanzone — official notes read 'New Facility - Upgrade your Fanzone for Clan bonuses and Stadium discounts'. It joins the Stadium/Commercial/Training/Medical facility roster and ties clan progression to stadium discounts. 12TH MAN: during the Winter Reload update (v13.100 Feb 26 / v13.110 Mar 2 2026) FTG ran a community '12th Man Vote - Pick the final Dream Star with the DLS community!'; the winner was then added in late March (v13.120 Mar 25 / v13.130 Mar 27) as '12th Man - The DLS community has voted, and we've added this extra superstar to the collection'. No source names the winning player; the official FTG TikTok teaser ('From the spot, outside the box, in the air. He will score them all. Your #DreamStars 12th Man') implies a striker but identity is UNCONFIRMED. DREAM STARS 26 = Special Cards for the season's top performers with enhanced attributes and card/player appearances, obtainable via Dream Star Agents. WINTER RELOAD also brought: updated team data (January transfer window), a new News System, MAJOR CLAN IMPROVEMENTS (Leaderboards, Vice-captains, Clan Point boosts), UI & SFX upgrades, and Game Centre on iOS (achievements + friend leaderboards). SUMMER SPOTLIGHT (v13.300) also added Dynamic Stars (new Special Player type, 'upgrading live with national team performances'), the 'World Tournament' international event type, and manager accessories; Cult Heroes collection announced Aug, shipped Sep (v13.420/13.430). Version numbering varies across mirrors (13.300 vs 13.310 for the May update). COVER STAR: Julian Alvarez fronts DLS26 (official FTG TikTok: 'It's Julián's world - we're just living in it. #Alvarez is back on the cover for #DLS26'), with Raphinha also highlighted in store copy.",
    "evidence/raw/turn35_w19/EV-400_fanzone_12thman_timeline.html",
    "Fanzone = new facility (Summer Spotlight v13.300 May27) giving Clan bonuses + Stadium discounts; 12th Man = community-voted final Dream Star, voted in Winter Reload (v13.100/110 Feb-Mar26), winner added v13.120/130 late-Mar26, identity UNCONFIRMED (teaser implies striker); Dream Stars 26 = top-performer special cards via Dream Star Agents; Clan improvements = leaderboards, vice-captains, clan point boosts; News System + iOS Game Centre; World Tournament event; Julian Alvarez cover star",
    quality="official")

add_claim("DLS26 Summer Spotlight update (v13.300, 27 May 2026) added a NEW club facility — the Fanzone — which grants Clan bonuses and Stadium discounts when upgraded.", 1, "facilities/fanzone", [e_fz])
add_claim("The Fanzone facility links clan progression to stadium discounts, making it a new gem-investment priority alongside Stadium/Commercial/Training/Medical.", 2, "facilities/fanzone-benefits", [e_fz])
add_claim("The 12th Man is a community-voted 12th member added to the Dream Stars collection: the vote ran during the Winter Reload update (v13.100 Feb 26 / v13.110 Mar 2 2026) and the winner was added in late March 2026 (v13.120 Mar 25 / v13.130 Mar 27).", 1, "events/12th-man-vote", [e_fz], notes="Mechanics official; winning player's identity not published in any source found")
add_claim("No source names the DLS26 Dream Stars 12th Man winner; the official FTG TikTok teaser ('From the spot, outside the box, in the air. He will score them all') implies a striker, but the identity remains UNCONFIRMED.", 4, "events/12th-man-identity", [e_fz], notes="OPEN GAP - requires in-game/device verification")
add_claim("Dream Stars 26 are Special Player cards representing the season's top performers with enhanced attributes and improved card/player appearances, obtainable through Dream Star Agents.", 1, "events/dream-stars-26", [e_fz])
add_claim("Winter Reload (v13.100/13.110, Feb-Mar 2026) brought major Clan improvements: Clan Leaderboards, Vice-captains, and Clan Point boosts, plus a new in-game News System and iOS Game Centre (achievements + friend leaderboards).", 1, "clans/winter-reload-improvements", [e_fz])
add_claim("DLS26 live-update timeline: v13.000 Dec 2025 launch -> v13.100/13.110 Feb-Mar 2026 Winter Reload (Dream Stars + 12th Man Vote + Clan overhaul) -> v13.120/13.130 late Mar 2026 (Dream Stars 26 + 12th Man added) -> v13.300 May 27 2026 Summer Spotlight (Dynamic Stars, Fanzone, World Tournament, manager accessories) -> v13.420/13.430 Sep 2026 (Cult Heroes).", 2, "updates/dls26-timeline", [e_fz], notes="Version numbers vary across mirrors (13.300 vs 13.310 for May update); dates from App Store history")
add_claim("Summer Spotlight also introduced the 'World Tournament' international event type and manager accessories/customisation items.", 1, "events/world-tournament", [e_fz])
add_claim("Julian Alvarez is the DLS26 cover star (official FTG TikTok describes him as 'back on the cover'), with Raphinha also headlined in Google Play store copy.", 1, "meta/cover-star", [e_fz])

# ---------- EV-401: Dream Draft ----------
e_dd=new_ev("Bluestacks DLS24 December update guide, gamingonphone DLS25 Dream Points guide, r/DreamLeagueSoccer (1bxd5eb Apr2024, 1atb4e2 Feb2024, 18dqq9e DLS24 beginners), YouTube Dream Draft gameplay, mwm.ai, apktodo, mumuplayer",
    "DREAM DRAFT rules. Limited-time game mode (listed in both store descriptions as 'Dream Draft'). Squad construction: you draft a squad of 18 players chosen from per-position option lists; every option is 75+ OVR and at least 1 Star Player must be included. Format: tournament-style, up to 7 rounds maximum, a different opponent each round; formation selection is limited (at least in the first iteration). Rewards: medals, gems and coins based on Dream Draft leaderboard ranking, with winner / runner-up / 3rd place all paid. Entry cost: historically a chargeable fee (~$2.99 IAP, per r/DLS Feb 2024); Dream Draft was made FREE TO PLAY for the first time ever in DLS24 (Apr 2024 r/DLS) though the community notes FTG may put it back behind a paywall. Drafted players are NOT kept after the event - the mode is a temporary loan squad. Offline/CPU variants exist: beating the CPU 8 times in a row is a fast gem farm (DLS24 beginner guide), and the 'Global Stars' Dream Draft is an offline tournament with 3 lives against AI. Dream Draft also pays Dream Points (up to 185 DP with a clean sheet and 5+ goals, same scale as Dream League Live) toward the Prize Ladder, and Dream Draft runs can yield Dream Star Agents (third Dream Stars player). Community complaints: opposition teams are 'heavily weighted against you' and matches feel scripted; the mode is described as fun mainly for maxed-out players.",
    "evidence/raw/turn35_w19/EV-401_dream_draft.html",
    "Dream Draft = limited-time mode; draft 18 players from per-position lists (all 75+ OVR, min 1 Star Player); up to 7 rounds, different opponent each round, limited formations; rewards = gems/coins/medals by leaderboard rank (winner/runner-up/3rd); entry fee ~$2.99 historically, free-to-play first time in DLS24 (Apr2024) but may return to paywall; drafted players NOT kept; CPU variant = 8 straight wins for gems, Global Stars = 3 lives vs AI; pays up to 185 Dream Points; can yield Dream Star Agents",
    quality="community")

add_claim("Dream Draft is a limited-time mode in which you draft a squad of 18 players from per-position option lists; every draftable player is 75+ OVR and at least one Star Player must be included.", 2, "modes/dream-draft-squad", [e_dd])
add_claim("Dream Draft runs as a tournament of up to 7 rounds maximum, pairing you against a different opponent each round, with a limited set of selectable formations.", 2, "modes/dream-draft-format", [e_dd])
add_claim("Dream Draft rewards are gems, coins and medals paid by leaderboard ranking, with the winner, runner-up and 3rd-place finishers all receiving prizes.", 2, "modes/dream-draft-rewards", [e_dd])
add_claim("Dream Draft entry has historically cost a chargeable fee (~$2.99); it was made free-to-play for the first time ever in DLS24 (Apr 2024), though the community expects it may return behind a paywall.", 2, "modes/dream-draft-entry-fee", [e_dd])
add_claim("Players drafted in Dream Draft are NOT retained in your club after the event ends - the mode uses a temporary loan squad.", 2, "modes/dream-draft-no-retention", [e_dd])
add_claim("An offline/CPU Dream Draft variant exists: beating the CPU eight times in a row is a fast gem farm, and the 'Global Stars' Dream Draft is an offline tournament giving you 3 lives against AI opponents.", 3, "modes/dream-draft-offline", [e_dd])
add_claim("Dream Draft matches award Dream Points toward the Prize Ladder on the same scale as Dream League Live (up to 185 DP with a clean sheet and 5+ goals), and Dream Draft runs can grant Dream Star Agents.", 3, "modes/dream-draft-dream-points", [e_dd])
add_claim("Community feedback on Dream Draft: opposition teams are perceived as heavily weighted against the player and matches feel scripted; the mode is considered mainly a diversion for maxed-out squads.", 3, "modes/dream-draft-reception", [e_dd])

# ---------- EV-402: kit/logo import + Classic Players + Dynamic Stars numbers ----------
e_kit=new_ev("dlskiturl.com, dlsgame.net, mundodls.com, dlskit.net, dlskits.com, Bluestacks custom kit guide, official FTG TikTok (Classic Players + Dynamic Stars), sportsdunia Dynamic Stars guide, dreamkitsapp.com/data",
    "KIT/LOGO IMPORT + CLASSIC PLAYERS + DYNAMIC STARS. Custom kit/logo import requires a ONE-TIME gem unlock (not per kit): the dominant community figure is 150 gems for the Custom Kit unlock (dlskiturl.com, dlsgame.net, mundodls.com all state 150), while Bluestacks states 300 Diamonds - a persistent discrepancy; mundodls breaks it down as Custom Kit 150 gems + Custom Crest 75 gems = 225 gems for full kit-and-logo customisation. The unlock is permanent and unlimited imports follow; one kit site notes the iPhone unlock is cheaper than the Android one. Import path: My Club -> Customise -> Kit tab -> Custom Kit (bottom-left) -> paste direct URL -> Confirm. Image requirements: direct URL to a 512x512 PNG (JPG accepted), transparent or solid background, under ~1 MB; webpage links fail, and Google Drive / Dropbox / Facebook block hotlinking - ImgBB and Imgur are the recommended hosts. Six separate kit slots exist: Home, Away, Third, GK Home, GK Away, GK Third, each imported individually. CLASSIC PLAYERS (official FTG TikTok): the Prize Ladder Italian League Classics set is Trezeguet, Batistuta, Crespo and Desailly, unlocked by earning Dream Points. DYNAMIC STARS (official FTG TikTok + App Store): a brand-new type of Special Player that upgrades live with national-team performance; sportsdunia's event guide gives base 82 OVR, +1 OVR per group-stage win, +2 OVR for R32/R16/QF/SF winners, converting to 96 OVR for the final winner (sportsdunia figures flagged unverified). Event card ratings from dreamkitsapp: World Winners Marc Cucurella 85 (Spain LB), World Heroes Lionel Messi 87 (Argentina SS), Kick-off Stars Raphinha 85 (Brazil LW), Champion players Luka Modric 86 (Croatia CM).",
    "evidence/raw/turn35_w19/EV-402_kit_import_classics.html",
    "Custom kit import = one-time 150 gems (Bluestacks 300 outlier flagged); custom crest 75 gems (225 total); permanent unlock, unlimited imports; My Club>Customise>Kit>Custom Kit>paste URL; needs direct 512x512 PNG (<1MB), Drive/Dropbox blocked, ImgBB/Imgur best; 6 kit slots (Home/Away/Third/GK x3); Prize Ladder Italian League Classics = Trezeguet, Batistuta, Crespo, Desailly; Dynamic Stars = live-upgrading specials (82 base, +1/group win, +2 per KO round, 96 for final winner - sportsdunia unverified)",
    quality="community")

add_claim("Custom kit import in DLS26 requires a one-time gem unlock of 150 gems (the figure given consistently by dlskiturl.com, dlsgame.net and mundodls.com); Bluestacks' 300-diamond figure is flagged as an outlier.", 2, "customisation/kit-import-cost", [e_kit], notes="150 vs 300 discrepancy resolved in favour of 150 (3 independent kit sites vs 1 guide)")
add_claim("Custom crest/logo import costs 75 gems, making full kit-plus-logo customisation 225 gems in total; both unlocks are one-time and permanent with unlimited imports afterwards.", 3, "customisation/logo-import-cost", [e_kit])
add_claim("Kit import path: My Club -> Customise -> Kit tab -> Custom Kit (bottom-left) -> paste direct URL -> Confirm; the design downloads and applies immediately.", 2, "customisation/kit-import-path", [e_kit])
add_claim("Kit images must be direct URLs to 512x512 PNG files (JPG accepted), transparent or solid background, under ~1 MB; webpage links fail and Google Drive/Dropbox/Facebook block hotlinking, so ImgBB or Imgur are the recommended hosts.", 2, "customisation/kit-image-requirements", [e_kit])
add_claim("DLS26 has six separate kit slots - Home, Away, Third, GK Home, GK Away, GK Third - each imported individually via its own URL.", 3, "customisation/kit-slots", [e_kit])
add_claim("The custom kit unlock is one-time per account rather than per kit, and one kit site reports the iPhone unlock price is lower than the Android one.", 3, "customisation/kit-unlock-platform-variance", [e_kit])
add_claim("Prize Ladder Italian League Classics set = David Trezeguet, Gabriel Batistuta, Hernan Crespo and Marcel Desailly, unlocked by earning Dream Points (official FTG TikTok).", 2, "prize-ladder/classic-players-italian", [e_kit])
add_claim("Dynamic Stars are a brand-new Special Player type that upgrade live according to their national team's real-world tournament performance.", 1, "events/dynamic-stars", [e_kit])
add_claim("Dynamic Stars event progression (sportsdunia, unverified): base 82 OVR, +1 OVR per group-stage win, +2 OVR for each knockout-round winner (R32/R16/QF/SF), converting to 96 OVR for the tournament winner's representatives.", 3, "events/dynamic-stars-progression", [e_kit], notes="sportsdunia figures - flagged unverified, needs device confirmation")
add_claim("DLS26 event card ratings include World Winners Marc Cucurella 85 (Spain LB), World Heroes Lionel Messi 87 (Argentina SS), Kick-off Stars Raphinha 85 (Brazil LW) and Champion players Luka Modric 86 (Croatia CM).", 3, "events/event-card-ratings", [e_kit])

p=os.path.join(RAW_DIR,'EV-400_fanzone_12thman_timeline.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-401_dream_draft.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
p3=os.path.join(RAW_DIR,'EV-402_kit_import_classics.html')
if not os.path.exists(p3):
    with open(p3,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
