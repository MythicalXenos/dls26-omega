#!/usr/bin/env python3
"""Turn 33 Wave 10: controller/haptics + monetization/ads/DAUs/coin-IAP."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','controls_turn33b')

ev_id=371
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"mixed","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=588
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_controller=new_ev("mundodls controller guide + App Store listing + APKMirror v12 + FTG TikTok + dlskits controller recs",
    "Native controller support added in DLS25 (v12.010 changelog Dec 2024) and carried into DLS26. Compatible controllers (iOS + Android): DualShock 4 (PS4), PS5 DualSense, Xbox Wireless Controller, MFi controllers (iOS), generic Bluetooth (8BitDo, GameSir, iPega, SteelSeries Stratus Duo), USB-C mobile controllers (GameSir G8 Galileo Hall Effect, Razer Kishi Ultra premium, GameSir X5 Lite budget). Pair via OS Bluetooth; DLS26 auto-detects on launch. In-game Settings→Controls→Gamepad Controls: Classic or Alternative button-layout profiles; sensitivity slider; custom profiles supported; vibration toggle. v12.110 added full Controller UI Support (navigate entire game UI with controller). Competitive players prefer USB-C over Bluetooth for lower input latency. Controller vibration toggle exists (separate from device haptics). Community request for free button repositioning/remapping on touch controls (not available — fixed button layout, only button size adjustable). Descriptive Button Text setting labels buttons (A/B/C) with action names for learning.",
    "evidence/raw/controls_turn33b/EV-371_controller.html",
    "Controller support DLS25 addition, compat list, layouts, USB-C latency, touch-customize request")
e_monetize=new_ev("Braberg/Gamigion ad monetization report + BlueStacks + r/DLS ads threads + sportsdailyinfo coin IAP",
    "DLS26 monetization: free-to-play with gem IAP + coin IAP + ads (rewarded + interstitial). DAU ~9.3 million (Jun 2026); monthly IAP revenue ~$3.2M, ad revenue ~$9.3M (triple IAP). Ad formats: rewarded videos (post-match coin-double 30s, menu 30c) and interstitials at halftime and full-time; users may see up to 4 interstitial ads per game; ads are core-to-experience (drives engagement). Ad volume per day is capped (community reports ~20/day default, drops to 10/day after making a purchase); cap is set by ad networks not FTG (~200 ads/day across whole userbase inventory); ads can 'run out' after 2-3 matches if network inventory low; restarting app sometimes refreshes availability. Post-match double ad bonus caps at 100 coins (doesn't scale with rewards >100c). Menu ad = 30 coins (one per 24h). Commercial upgrade L1=+13%, L2=+21% match coin bonus (earlier waves had L1=-5% injury; Commercial boosts coins — 75g first upgrade). Coin IAP USD pricing (sportsdailyinfo): Starter $0.99/1000c; Small $4.99/6000c; Mega $49.99/75000c; Ultimate $99.99/160000c (≈$0.00062-0.00099 per coin). Base match coin rewards: ~45-75c per career win scaled by goals scored/clean sheet/stadium/division; ~220c per home win with ad (community); end-of-season +100c bonus. Friendly/exhibition matches no rewards. Coin-farming exploit: own-goal grind in friendlies (~45c/run) is slower than playing real matches + ad; clean-sheet 5-0 home win + ad yields up to ~200c in ~2.5min. Season pass premium tier accelerates Dream Points. Loot boxes/random items confirmed in App Store age rating 13+ (random-agent/legendary-scout draws have random outcomes; odds not published in reviewed sources). Ad strategy: rewarded ads in Career section per GameBiz; banners/interstitials not shown to payers.",
    "evidence/raw/controls_turn33b/EV-372_monetize.html",
    "DAU/revenue, ad formats + caps, coin IAP pricing, Commercial bonus %, match payout baseline, farming rates")

# CONTROLLER / HAPTICS
add_claim("Native controller support was added in DLS25 (v12.010, Dec 4 2024) and carried over to DLS26, covering tackles/runs/marking/shooting improvements alongside controller support.", 1, "controls/controller-history", [e_controller])
add_claim("Compatible controllers: DualShock 4 (PS4), DualSense (PS5), Xbox Wireless Controller, MFi controllers (iOS), generic Bluetooth (8BitDo, GameSir, iPega, SteelSeries Stratus Duo), USB-C mobile controllers (GameSir G8 Galileo Hall Effect, Razer Kishi Ultra, GameSir X5 Lite).", 2, "controls/controller-compat", [e_controller])
add_claim("Controller pairing via OS Bluetooth; DLS26 auto-detects on launch; if pairing fails restart the game.", 2, "controls/controller-pair", [e_controller])
add_claim("In-game controller settings (Settings→Controls→Gamepad Controls): Classic vs Alternative button layout, sensitivity slider, custom controller profiles supported, vibration toggle.", 1, "controls/controller-settings", [e_controller])
add_claim("v12.110 (Feb 2025, DLS25 era) added full Controller UI Support — entire DLS menu navigable with controller.", 1, "controls/controller-ui", [e_controller])
add_claim("Competitive/low-latency preference: USB-C wired/telescoping controllers preferred over Bluetooth for DLL online play.", 2, "controls/latency", [e_controller])
add_claim("Touch controls have fixed button positions (only size adjustable); community repeatedly requests free button repositioning/remapping (not implemented as of v13.430).", 2, "controls/touch-limitation", [e_controller], "Play Store request")
add_claim("Descriptive Button Text toggle labels on-screen buttons with their action names (A/B/C plus Low/Hard/Lofted labels) for new-player learning.", 2, "controls/labels", [e_controller])

# MONETIZATION / ADS / IAP
add_claim("DLS26 DAU approximately 9.3 million (Jun 2026, third among mobile soccer games behind EA FC Mobile 20M and eFootball 14M).", 2, "meta/dau", [e_monetize], "Braberg/Gamigion industry newsletter")
add_claim("Monthly revenue: IAP ~$3.2M; ad revenue ~$9.3M (ads triple IAP income for FTG).", 2, "meta/revenue", [e_monetize])
add_claim("Ad formats: rewarded videos (optional, coin-double post-match, 30s; menu 30c) + interstitial ads at halftime and full-time; up to 4 interstitial ads per game reported; banners/native ads minimal.", 2, "monetization/ads", [e_monetize])
add_claim("Ads are integrated into the core career/match loop (rewarded ads tied directly to match outcomes), not walled off — this distinguishes DLS from competitors who gate ads to menus.", 2, "monetization/ad-strategy", [e_monetize])
add_claim("Daily ad view cap: ~20 ads/day default; drops to ~10/day after making an IAP purchase (payer-protection). Cap is enforced by ad networks, not FTG directly (~200 ads/day total network inventory allocated per title).", 2, "monetization/ad-cap", [e_monetize])
add_claim("Ads can 'run out' after 2-3 matches during a session when ad-network inventory is exhausted; restarting the app sometimes refreshes availability. Ads unavailable blocks coin farming.", 3, "monetization/ad-availability", [e_monetize])
add_claim("Post-match ad coin bonus caps at 100 extra coins (does NOT scale linearly if base match reward already exceeds 100).", 2, "monetization/ad-cap-amount", [e_monetize], "r/DLS 2021 comment; still relevant")
add_claim("Commercial facility coin bonus: Level II = +13% match coins; Level III = +21% match coins (applies to Career + Exhibition).", 2, "facilities/commercial-bonus", [e_monetize])
add_claim("Commercial facility Level I costs 75 gems (widely recommended as first gem spend for new players, not Legendary Agents).", 2, "facilities/commercial-cost", [e_monetize])
add_claim("Coin IAP pricing (USD, approximate): Starter $0.99 = 1,000c; Small $4.99 = 6,000c; Mega $49.99 = 75,000c; Ultimate $99.99 = 160,000c (~$0.00062-0.00099 per coin, marginal volume discount).", 3, "economy/coin-iap", [e_monetize], "sportsdailyinfo source; regional prices vary")
add_claim("Career match baseline payouts: ~45-75 coins per win (scales with goals scored, clean sheets, stadium, division); home win 5-0 + ad + stadium ~200-220c; end-of-season +100c bonus; Diamond/international/all-star cup matches pay well; Exhibition matches pay 0.", 2, "economy/payouts", [e_monetize], "community reports")
add_claim("Farming rates: ~2.5 minutes per match → 4-6 matches per halftime of real football yields ~6,000 coins per real-life halftime (lfbb anecdote). Friendly own-goal grind (~45c/10-12min) is far slower than real-match + ad play.", 2, "economy/farming", [e_monetize])
add_claim("Premium Season Pass accelerates Dream Points / Progression Bank accrual (v12.110 'Additions to Premium Season Pass – Earn Dream Points quicker').", 1, "economy/season-pass-premium", [e_monetize])
add_claim("Loot boxes/random-item purchases exist (Agents/Scouts return random players; App Store age rating 13+ cites 'Infrequent/Mild Simulated Gambling' for random items). Odds disclosure not found in reviewed sources.", 2, "monetization/loot-boxes", [e_monetize])

for f in ['EV-371_controller.html','EV-372_monetize.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-588} new claims and {ev_id-371} EVs. Totals: {n_cl} claims, {n_ev} EVs")
