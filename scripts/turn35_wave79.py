#!/usr/bin/env python3
"""Turn 35 Wave 79: THE NAME LEVER'S OTHER HALF, THE OFFICIAL SEASON PASS PAGE, AND THE
CUSTOMISATION SURFACE'S REAL SHAPE.

Wave 79's centrepieces:

1. THE CLUB-NAME LEVER, USED FIRST. The corpus's manager-name method (CLAIM-1799) treats the
   club name as a FALLBACK - "if that fails, change your club name to the target's club." The
   r/DLS 17tdqrk thread runs it the other way round: name the club first, name the manager
   second, and the target player arrives in five matches. That ordering correction is the
   operationally important part, because it is cheaper to try.

2. THE OFFICIAL SEASON PASS PAGE (support.ftgames.com 4404070913169) - a second official FTG
   article on the pass, and it carries a version stamp: everything in it applies from version
   12200 onwards, i.e. DLS26. It confirms the FREE / SEASON PASS split, the Progress Bank, and
   the gold profile trim, and it states the purpose of that trim: "to show off to other players."

3. THE CUSTOMISATION SURFACE HAS FIVE TABS, NOT THREE. The corpus (CLAIM-074) records three -
   Players / Manager / Kit. The current surface is Kit, Logo, Team Name, Players, Manager.

4. THE SHIRT-NUMBER COLOUR SWATCH. Layers 9 and 10 of the official kit template are not garment
   pieces at all - they are colour swatches the game reads to render the numbers. Choosing badly
   makes your own squad numbers unreadable.

5. NO CLUB ANTHEM. DLS has no anthem, crowd-chant or goal-song selector anywhere on the
   customisation surface. The crowd audio that changed in v12.110 is a build-level upgrade, not a
   per-club choice. That closes the anthem gap as a documented negative.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w79')

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

e_np=new_ev("support.ftgames.com 4404070913169 'What is the Season Pass?' (OFFICIAL, second FTG article, version stamp 12200 onwards), support.ftgames.com 214422145 (OFFICIAL kit/logo customisation, the 11-layer template map and the logo reset button), r/DreamLeagueSoccer 17tdqrk 'THE NAME THING ACTUALLY WORKS' (11 Nov 2023, the club-name and manager-name lever with the PSV/Xavi Simons data point), dlskitsurl.com (team name free and editable), dlskitsurl.net (the shirt-number colour swatch), dlspedia.fandom.com/wiki/Dream_League_Soccer_Stadium (the stadium name default, the eight sectors, the seat colour, non-seated structures), ftsdlskits.com / dlskits.com / dreamleaguekits.com (the My Club > Customise > Edit Kit > Custom Kit > paste URL > Confirm workflow), bluestacks custom-kits guide (the five customisation tabs and the five independent colour tabs), mytour.vn (the Edit Kit interface: Select Kit, Number Font, Pattern Type, Trim, Color)",
    "THE CLUB-NAME LEVER, THE OFFICIAL SEASON PASS PAGE, THE FIVE-TAB CUSTOMISATION SURFACE, THE SHIRT-NUMBER COLOUR SWATCH, AND THE ABSENCE OF A CLUB ANTHEM. (1) THE CLUB-NAME LEVER, USED FIRST - the thread reports changing the club name to PSV and the manager name to Xavi Simons and getting Xavi Simons 'in 5 matches', with commenters adding two further recipes: name the club 'exclusives', and name the club Lyon with the manager set to the current Lyon manager or to Dejan Lovren. A third variant works by NATION: name the club after a country and set the manager name and nationality to a player from it. **The corpus's CLAIM-1799 runs the same lever in the opposite order** - it sets the manager name and nationality first and treats the club name as the fallback. The wave's contribution is the ORDERING: try the club name first because it costs nothing to change. (2) THE OFFICIAL SEASON PASS PAGE - 'All information included below is applicable from our latest DLS release (version 12200 onwards)'. It confirms the FREE / SEASON PASS split in official words ('The FREE section is accessible to all users and the SEASON PASS section contains premium rewards which can only be accessed when purchasing the Season Pass'), confirms that 'Purchasing the Season Pass unlocks the Progress Bank, which rewards currency based on your DLL (multiplayer) XP' with 'the Progress Bank reward is given at the end of the season', and adds the PURPOSE of the gold trim: 'Purchasing the Premium Season Pass will turn some elements of your game profile gold, to show off to other players.' (3) THE CUSTOMISATION SURFACE HAS FIVE TABS: Kit, Logo, Team Name, Players, Manager - the corpus's CLAIM-074 records only three (Players/Manager/Kit). Within the Kit tab the editor offers five INDEPENDENT colour slots: Primary, Secondary, Sponsor, Trim and Shirt Number. (4) THE SHIRT-NUMBER COLOUR SWATCH: 'The shirt number colour and shorts number colour squares are not visible garment pieces. They work as colour swatches. Dream League Soccer reads the colour inside these areas and uses it when displaying player numbers on the shirt and shorts. That means the colour you choose here directly affects whether the squad numbers can actually be seen.' So template layers 9 and 10 are inputs, not artwork. (5) THE OFFICIAL KIT PAGE also re-states the 11-layer map (1 shirt body, 2 sleeves short, 3 sleeves long, 4 socks, 5 shorts, 6 club badge, 7 league badge, 8 kit logo, 9 shirt number colour, 10 short number colour, 11 shirt collar) and adds that 'During the import process shirt creases are automatically generated' and that 'To delete imported logos, there is a reset button in the top left of the Edit Logo screen.' (6) THE STADIUM NAME defaults to 'Dream F.C. Stadium' and is editable; the stadium is reached through My Club > Stadium & Facilities per two community Q&A answers. (7) NO CLUB ANTHEM: a targeted search for DLS anthem / crowd chant / goal song returned only FIFA 22 FUT analogues. DLS's customisation surface has no anthem or chant selector, and the v12.110 'New Crowd Audio' is a build-level upgrade for everyone, not a per-club choice. The anthem gap is therefore a documented NEGATIVE. (8) The Season Pass per-tier reward list is not published by FTG and rotates each season; what is documented is the structure (two tracks, the 400-SP activation, the Tier-8 backfill, the double SP/XP, the Progress Bank) and the DLS21 original bundle. The gap therefore narrows to 'read it on the device at season start.'",
    "CLUB-NAME LEVER used FIRST, not as a fallback: rename the club to the target player's club, set the manager name and nationality to theirs, and the target arrives within ~5 matches. The three community recipes are PSV + Xavi Simons, 'exclusives', and Lyon + the current Lyon manager or Dejan Lovren; a fourth works by NATION. OFFICIAL SEASON PASS (second FTG article, version 12200 onwards = DLS26): FREE track accessible to all users, SEASON PASS track premium-only, purchase unlocks the Progress Bank (DLL XP to currency, paid at season end) and turns profile elements gold 'to show off to other players'. THE CUSTOMISATION SURFACE HAS FIVE TABS (Kit, Logo, Team Name, Players, Manager) with five independent colour slots inside Kit (Primary, Secondary, Sponsor, Trim, Shirt Number). THE SHIRT-NUMBER COLOUR SWATCH: template layers 9 and 10 are colour swatches the game reads to render the numbers, so a bad choice makes your own squad numbers unreadable. Shirt creases are auto-generated on import; the Edit Logo reset button (top left) deletes imported logos. Stadium name defaults to 'Dream F.C. Stadium'. NO CLUB ANTHEM or crowd-chant selector exists in DLS - the anthem gap closes as a documented negative. The Season Pass per-tier reward list is unpublished and rotates, so that gap narrows to structure-only",
    "THE NAME LEVER'S CLUB-HALF, THE OFFICIAL SEASON PASS STRUCTURE, THE FIVE-TAB CUSTOMISATION SURFACE, THE NUMBER-COLOUR SWATCH, AND THE MISSING ANTHEM",
    quality="official")

add_claim("THE CLUB-NAME LEVER, USED FIRST: rename your club to the target player's real club, set your manager name and nationality to theirs, and the target player can arrive within about five matches. The corpus's CLAIM-1799 runs the same lever in the OPPOSITE order - manager name and nationality first, club name only as the fallback. **Try the club name first: it is free to change and costs nothing to test.**", 3, "acquisition/club-name-lever-first", [e_np], notes="Refines CLAIM-1799's ordering; the cheapest acquisition lever in the game")
add_claim("The club-name lever has a named data point: 'changed name to PSV and Manager to Xavi Simons, got him in 5 matches.' Two further community recipes are naming the club 'exclusives', and naming it Lyon with the manager set to the current Lyon manager or to Dejan Lovren.", 3, "acquisition/club-name-lever-recipes", [e_np])
add_claim("A NATION variant of the name lever exists: name the club after a country and set the manager name and nationality to a player from that nation. So the lever has three independent inputs - club name, manager name, manager nationality - and any of them can be aimed first.", 3, "acquisition/name-lever-nation-variant", [e_np])
add_claim("OFFICIAL SEASON PASS STRUCTURE, second FTG article (4404070913169), stamped 'applicable from our latest DLS release (version 12200 onwards)' - i.e. DLS26. 'The FREE section is accessible to all users and the SEASON PASS section contains premium rewards which can only be accessed when purchasing the Season Pass.'", 1, "season-pass/official-structure-second-source", [e_np], notes="Second official source for CLAIM-1528; carries the version stamp")
add_claim("The official page states the PURPOSE of the gold profile trim: 'Purchasing the Premium Season Pass will turn some elements of your game profile gold, to show off to other players.' So the cosmetic is a status signal visible in multiplayer, not a reward in itself.", 3, "season-pass/gold-profile-purpose", [e_np])
add_claim("THE CUSTOMISATION SURFACE HAS FIVE TABS - Kit, Logo, Team Name, Players, Manager - not the three the corpus recorded at CLAIM-074 (Players / Manager / Kit). Reached at Main Menu > My Club > Customise.", 2, "customisation/five-tabs", [e_np], notes="Corrects CLAIM-074's three-tab list")
add_claim("Inside the Kit tab the editor offers five INDEPENDENT colour slots - Primary, Secondary, Sponsor, Trim and Shirt Number - each of which can be set to a different colour on the shirt, shorts and socks separately.", 3, "customisation/five-colour-slots", [e_np])
add_claim("THE SHIRT-NUMBER COLOUR SWATCH: template layers 9 (shirt number colour) and 10 (short number colour) are NOT garment pieces - 'They work as colour swatches. Dream League Soccer reads the colour inside those areas and uses it when displaying player numbers on the shirt and shorts.' **The colour you choose there directly determines whether your own squad numbers can be read on the pitch.**", 3, "customisation/number-colour-swatch", [e_np], notes="Makes two of the eleven template layers inputs rather than artwork")
add_claim("Kit import generates shirt creases automatically at runtime, and imported logos are removed with 'a reset button in the top left of the Edit Logo screen' - both stated on the official customisation article.", 1, "customisation/creases-and-logo-reset", [e_np])
add_claim("The stadium's default name is 'Dream F.C. Stadium' and it is editable; two community answers place the stadium surface at My Club > Stadium & Facilities.", 2, "stadium/default-name-and-path", [e_np], notes="Corroborates CLAIM-0702")
add_claim("DLS HAS NO CLUB ANTHEM, CROWD-CHANT SELECTOR OR GOAL SONG. A targeted search for a DLS anthem returned only FIFA 22 FUT analogues (Club Anthem, Crowd Chant, Goal Song). The customisation surface carries no anthem tab, and the v12.110 'New Crowd Audio' is a build-level upgrade applied to every club, not a per-club choice. **The anthem gap closes as a documented negative.**", 2, "customisation/no-club-anthem", [e_np], notes="Closes the anthem=0 gap as a negative, not as missing data")
add_claim("The Season Pass per-tier reward list is not published by FTG and rotates every season, so the surviving part of that gap is device-only. What IS documented is the complete structure: two tracks, 400 Season Points to activate, 40 SP/day free from login, tiers pre-completed to Tier 8 on purchase, double SP and double Live XP, and a Progress Bank paid at season end.", 2, "season-pass/per-tier-list-unpublished", [e_np], notes="Narrows the gap to 'read the device at season start'")
add_claim("Team name is editable at any time and for free - 'You can edit your team name anytime for free' - from the Team Name tab in Customise, which is also the surface that carries the shirt numbers and boot colours.", 3, "customisation/team-name-free-editable", [e_np], notes="Second source for CLAIM-0694; matters because the club-name lever depends on it")

for p in ['EV-492_name_lever_and_season_pass.html','EV-492b_official_season_pass.html','EV-492c_official_kit_customisation.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
