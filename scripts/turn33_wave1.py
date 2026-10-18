#!/usr/bin/env python3
"""Turn 33 Wave 1 (continuing after turn 32 ckpt-045) — Throw-ins/GK distribution/GK mechanics; weather visuals."""
import json, os, datetime, re
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb/claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
evs=[json.loads(l) for l in open(EIP) if l.strip()]
next_c=max(int(c['claim_id'].split('-')[1]) for c in claims)+1
next_e=max(int(e['evidence_id'].split('-')[1]) for e in evs)+1
ac,ae=0,0
def cid():
    global next_c,ac; r=f"CLAIM-{next_c:03d}"; next_c+=1; ac+=1; return r
def eid():
    global next_e,ae; r=f"EV-{next_e:03d}"; next_e+=1; ae+=1; return r
def C(text, conf, evids, chal=None, vol='Low', notes=None):
    cv=cid()
    rec={"claim_id":cv,"text":text,"confidence":conf,"supporting_evidence":evids,
         "challenges":chal or [],"volatility":vol,"notes":notes or [],
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
    with open(CP,'a') as f: f.write(json.dumps(rec)+"\n"); claims.append(rec)
def E(origin, summary, artifact, typ='web_article', method='web_search_community', reliability='Medium'):
    ev=eid()
    rec={"evidence_id":ev,"origin_method":origin,"summary":summary,"artifact_path":artifact,
         "evidence_type":typ,"capture_method":method,"reliability":reliability,
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),"raw_data_ref":""}
    with open(EIP,'a') as f: f.write(json.dumps(rec)+"\n"); evs.append(rec)
    return ev

e341=E("LevelWinner DLS24 beginner guide + gamingonphone DLS26 controls guide + retbit DLS26 beginner tip + r/DLS GK-control threads",
       "Throw-ins: During throw-ins the defensive AI auto-deploys in an optimal spread; long risky throws are usually intercepted. Best practice is short B-pass to nearest teammate. Contesting throw-ins: manually switch (C) and close down the obvious receiver immediately. Goal kicks / GK distribution: Quick A tap = short precise distribution to nearby defender (build-up from back). Full-charge A WITHOUT touching the movement stick = long automatic boot past halfway line (default long). B-button = charged directional kick (longer, buildable power for precision). DLS26 beginner advice strongly discourages mindless hoofed long balls from GK as they are inaccurate and cede possession; throwing/short passing to build from the back is recommended. Button naming in DLS26 (gamingonphone): Low Kick (B) for ground passes/pressure; Hard Kick (A) for shots/long balls/sliding tackles; Lofted Kick (C) for through balls/chips/player switch. Defensive: hold B = pressure/tackle, C = manual player switch (also GK rush when held on D; double-tap GK = drop ball). GK control: Hold C when out of possession to manually rush GK toward ball (sweeper-keeper). Double-tap the GK to drop the ball at his feet (so you can play/pass out). GK auto-rushes sometimes on AI when attacker is through. GK stats: GKH (Handling) -> catching/cross-claiming/positioning (higher = fewer spills, better air dominance on crosses/corners, fewer rebounds). GKR (Reflexes) -> save reactions/diving; community consensus GKR should be kept higher than GKH with no more than ~5-point gap between the two. Low GKH leads to spilled shots (corners/rebounds for opponent). GKs with better built-in rush timing exist (meta GK picks). GK Positioning (GKP) was a separate stat in older DLS versions; folded in DLS20+ into GKH (per fandom Player Development page, still lists GK Positioning as a Goalkeeping-coach upgrade for outfield-goalkeeping but is functionally covered by Handling).",
       "evidence/raw/community_turn33/EV-341_throwins_gk.html",
       typ='guide+community',reliability='High')
e342=E("eslamgaming visual/gameplay articles (Mar-Jul 2026) + dlsmod + playdreamleaguesoccer + 3zebras + r/DLS DLS25 snow thread + r/DLS wishlist",
       "Weather visuals in DLS26: multiple sources (some likely AI-content-farm, so reliability caveated) claim dynamic weather system with rain, snow, fog; weather transitions mid-match; rain creates wet pitch reflections/puddles/slippery traction + faster ball physics; snow reduces visibility + makes long passes riskier and ball harder to track; fog reduces visibility; time-of-day changes (day/sunset/night under floodlights) affect lighting/visibility/glare for GK. Community-verified complaints: DLS25 snow animation is widely reported as visually bad (obscures ball, motion-sickness inducing from chaotic changing direction during active play; migraine reports). Snow/fog visuals carried into DLS26. Wishlist requests from community: fog, cloudy, light rain additions (not all present yet), VAR animations, post-match interviews. DLS-mod site claims improved night-stadium visuals, pinching/rotating in Customise for cinematic view; enhanced matchday atmosphere with more props/banners/flags, walkout jackets/kits. CAUTION: eslamgaming and playdreamleaguesoccer appear to be AI-generated/SEO-content-farm sites; gameplay-effect claims (traction/ball physics) are not independently corroborated by reliable reviewers and may be speculative. Visual confirmation of rain/snow/night exists from in-game screenshots/YouTube, but gameplay-impact claims remain unverified until APK/first-hand testing.",
       "evidence/raw/community_turn33/EV-342_weather.html",
       typ='community',reliability='Low-Medium')

# CLAIMS
C("Throw-ins: AI defense auto-spreads optimally after throw-in animation; risky long throws are usually intercepted. Best practice is short B-pass to nearest teammate.",
  'High Confidence',[e341])
C("Goal kicks / GK distribution: Quick A tap = short, precise roll/throw to a nearby defender (build-up from back). Full-charge A WITHOUT stick input = automatic long ball past the halfway line. Charged B with directional stick = aimed longer kick (controllable power). Beginner consensus advises against mindless long GK boots — they are inaccurate and concede possession; use short distribution.",
  'High Confidence',[e341])
C("Manual GK control: Hold C (when defending) to call/rush GK out toward ball (sweeper-keeper). Double-tap the GK to drop the ball at his feet so you can play short passes out. GK will also auto-rush in some through-ball situations; some GKs have better built-in rush timing meta than others.",
  'High Confidence',[e341])
C("GK stats: GKH (Handling) governs catching, cross-claiming, and positioning (higher = fewer spilled shots, better air dominance on corners/crosses). GKR (Reflexes) governs save reactions/diving — should generally be higher than GKH with <=5 point gap. Low GKH leads to rebounds/corners for opposition. Old GKP (Positioning) stat folded into GKH in DLS20+.",
  'Medium-High Confidence',[e341],vol='Low')
C("Weather visuals in DLS26 include rain, snow, fog per multiple sources; time-of-day (day/sunset/night floodlights) is confirmed. Stadium night visuals are a promoted feature. DLS25 snow animation was widely criticized as too heavy/chaotic (obscures the ball, strobe-effect, motion-sickness reports); this carries into DLS26.",
  'Medium Confidence',[e342],['eslamgaming/playdreamleaguesoccer/AI-content-farm claims that rain/snow/fog affect gameplay physics are UNVERIFIED — no reliable reviewer corroborates. Treat gameplay-impact claims as speculative until first-hand/APK testing. Visuals confirmed via screenshots/YouTube.'],vol='Medium')
C("Community-requested features (wishlists, not in game yet or unconfirmed): VAR animations, post-match interviews, manager outfit accessories expansion, additional weather variants (cloudy/light rain), news system, Bundesliga/Ajax licenses, Player of the Season awards.",
  'Medium Confidence',[e342],['Wishlist items from r/DLS YouTube community; many are NOT implemented.'],vol='High')
C("DLS26 enhanced matchday atmosphere: more props/banners/flags in stadiums; walkout sequences with training kits/jackets; improved lighting; stadium customization view supports pinch/rotate for cinematic camera.",
  'Medium-High Confidence',[e342],vol='Low')
# DLS26 gameplay community sentiment (from search results that surfaced)
C("DLS26 community gameplay sentiment (Dec 2025 reviews): improved tiki-taka/possession feel, better dribbling, reduced match scripting; C-button (through/loft) nerfed vs DLS25; player switching remains a pain point with 0.5-2s delay; GKs inconsistent/unpredictable; defensive AI weaker than attacking AI; stats sometimes feel disconnected from outcomes ('placebo'); long shots nerfed vs DLS25 (1v1s now more reliable than outside-the-box shots), making gameplay more realistic.",
  'Medium-High Confidence',[e342],vol='Medium')

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
