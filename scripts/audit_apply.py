#!/usr/bin/env python3
"""Apply crucible tier changes + audit notes to claims.jsonl, write snapshot, and produce audit manifest."""
import json,os,datetime,shutil
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
patch=json.load(open(os.path.join(ROOT,'logs','crucible_tier_patch.json')))
patch_by={p['claim_id']:p for p in patch}
claims=[json.loads(l) for l in open(CP) if l.strip()]
# Skeptic flags keyed by cid
skeptic={
 'CLAIM-145':'Crucible (2026-10-18): QR-OLS refit across 8 TrungTaHust versions (n=23,327) reproduces weights exactly (const=1.893, CON=0.211, STR=0.166, SPE=0.142, ACC=0.148, PAS=0.112, SHO=0.111, TAC=0.106, STA=0.037); MAE=0.376 (claimed 0.38); ±1=99.79%. v20251 shows an STA weight anomaly (0.011 vs ~0.055) — possibly one bad scrape column; formula otherwise stable.',
 'CLAIM-144':'Crucible (2026-10-18): Promo OVR ceiling disagreement across sources — Trung EV-251 special.json caps at 88; FBGD EV-248 at 96; Larrycr7 EV-252 at 98 (Champions Messi/Ronaldo only). Cap ≥96 established; 98 Champions is single-source to Larry.',
 'CLAIM-154':'Crucible (2026-10-18): Leo CB DP models 3 coach rarities (白/蓝/金 = +1/+2/+3). EV-247 SakPro lists COMMUNITY/RARE/EPIC. A possible 4th (yellow/epic?) tier is not present in CB DP; cannot generalize to all positions without APK.',
 'CLAIM-138':'Crucible (2026-10-18): GK stat remap SHO→GKR / STA→GKH confirmed on 3 EV-252 promo GKs that literally use column names GKR/GKH; base GKs in EV-251 still use 8 standard labels. Statistical OLS weight shift on GK subgroup supports the remap; not APK-confirmed for all GKs.',
 'CLAIM-152':'Crucible (2026-10-18): Ad rewards "coins or diamonds" + 15k gold/400 diamond targets come from bot-dls resource_targets defaults; not observed live packets.',
 'CLAIM-153':'Crucible (2026-10-18): HUD filled/hollow circles labeled stamina/boost by bot templates; "form-boost meter" alternative interpretation not ruled out.',
 'CLAIM-136':'Crucible (2026-10-18): Ad SDK list from academic APK scans (beerphilipp/taptrap, tabbed-out); APK hash not recorded.',
 'CLAIM-084':'Crucible (2026-10-18): Mod/cheat ecosystem EXISTS (source code of mod-menu SPAs + auto-farm bot literally captured in EV-215/217/254). Claim is about ecosystem existence, not about efficacy.',
 'CLAIM-060':'Crucible (2026-10-18): dreamkitsapp card counts are labeled "Approximate Calculations" on the site; taxonomy reliable, per-type counts may drift.',
 'CLAIM-103':'Crucible (2026-10-18): "Multiple in-season updates" empirically supported by 8 Trung versions + App Store history; "monthly cadence" remains anecdotal.',
 'CLAIM-139':'Crucible (2026-10-18): Price tiers mechanically verified: 86-OVR players all price=2800 in EV-251; price_map.json has 160 OVR sub-tiers.',
 'CLAIM-141':'Crucible (2026-10-18): Roster 2,518 base players in 20261; OVR 52-86; 4×86 players (Haaland/Kane/Mbappé/Dembélé) — all verified.',
 'CLAIM-147':'Crucible (2026-10-18): Base cap 86 consistent across 8 Trung versions (20231-20262, 23,327 rows).',
 'CLAIM-155':'Crucible (2026-10-18): CB weights CON=2, others=1; actions +1/+2/+3; Math.min(100,…) cap; capacity thresholds 12,6 — all confirmed by direct grep of EV-255 JS.',
 'CLAIM-150':'Crucible (2026-10-18): Button mapping A=pass, B=shoot, C=skill, SPRINT/TACKLE/SWITCH — verified by grep of bot-dls game_controller.py.',
 'CLAIM-151':'Crucible (2026-10-18): 30 in-match states enumerated from bot-dls game_state_detector.py; these are CV-template states, not necessarily FTG canonical states.',
 'CLAIM-104':'Crucible (2026-10-18): Team OVR = mean of Starting-11 agreed by two independent community tools (SakPro, Leo CB DP); no APK/official confirmation.',
 'CLAIM-105':'Crucible (2026-10-18): "+1 OVR per trained player" present in both SakPro tool and CB DP (both encode +1/+2/+3 coach boosts); boost size not APK-verified.',
}
applied=[]
for c in claims:
    cid=c['claim_id']
    if cid in patch_by:
        old=c['confidence_tier']; new=patch_by[cid]['new']
        note=f'Crucible 2026-10-18 tier reclass: {old} → {new}'
        ch=c.get('challenges') or []
        if note not in ch: ch=[note]+ch
        c['challenges']=ch
        c['confidence_tier']=new
        applied.append((cid,old,new))
    if cid in skeptic:
        ch=c.get('challenges') or []
        note=skeptic[cid]
        if note not in ch: ch.append(note)
        c['challenges']=ch

# Snapshot pre-audit already exists at kb_snapshots/claims_20261018T0150Z.jsonl; take post-audit snapshot
ts=datetime.datetime.utcnow().strftime('%Y%m%dT%H%MZ')
post_path=os.path.join(ROOT,'kb_snapshots',f'claims_{ts}_postaudit.jsonl')
shutil.copy(CP,post_path)

# Write claims.jsonl back
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c,ensure_ascii=False)+'\n')
print(f'Applied {len(applied)} tier changes. Post-audit snapshot: {post_path}')

# Write audit manifest
manifest={
 'audit_id':'crucible-20261018',
 'audit_timestamp_utc':ts,
 'audit_type':'standalone-epistemic-verification',
 'pre_audit_snapshot':'kb_snapshots/claims_20261018T0150Z.jsonl',
 'post_audit_snapshot':os.path.relpath(post_path,ROOT),
 'claims_total':len(claims),
 'ev_total':sum(1 for l in open(os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')) if l.strip()),
 'tier_changes_applied':len(applied),
 'skeptic_flags_added':len(skeptic),
 'numeric_spotchecks':{
  'ovr_formula_qr_ols_combined':{
   'n':23327,'const':1.893,'con':0.211,'str':0.166,'spe':0.142,'acc':0.148,'pas':0.112,'sho':0.111,'tac':0.106,'sta':0.037,
   'mae':0.376,'rmse':0.484,'within_pm1_pct':99.79,
   'note':'v20251 STA anomaly (0.011 vs ~0.055) flagged as possible scrape issue'
  },
  'base_roster_20261':{'n':2518,'rate_min':52,'rate_max':86,'non_gk':2255,'gk':263,'ovr86_count':4,'ovr86_price':2800},
  'promo_larry':{'n':41,'rate_min':82,'rate_max':98,'ovr98_players':['Lionel Messi (Champions)','Cristiano Ronaldo (Champions)']},
  'cb_trainer_js':{'weights_ctrl':2,'weights_other':1,'actions':[1,2,3],'cap':100,'capacity_thresholds':[6,12]},
  'botdls_buttons':{'A':'pass','B':'shoot','C':'skill','hold':['sprint','tackle','switch']},
  'botdls_states_count':30
 },
 'tier_distribution_post':{t:sum(1 for c in claims if c['confidence_tier']==t) for t in ['Confirmed','High Confidence','Community Consensus','Speculative','Disputed','Rejected']},
 'tier_changes':[{'claim_id':cid,'old':o,'new':n} for cid,o,n in applied],
 'cross_branch_drift':['CLAIM-007','CLAIM-020','CLAIM-026','CLAIM-049','CLAIM-087'],
 'outstanding_gaps_require_apk':[
  'Non-CB coach attribute weights (position-specific matrix beyond CB)',
  'Dream Points / Form Boost / Season Pass exact numerics',
  'GKR vs GKH column remap for all GKs (not just 3 promos)',
  'Matchmaking/ELO algorithm beyond FTG-stated inputs',
  'Ad reward values, frequency caps, ad classes beyond bot-default configs',
  '4th/yellow/epic coach tier existence',
  'Fractional-overflow rounding mode in training-cost DP',
  'Save/shared_prefs schema on device',
 ],
 'blocker_step2':'APK unavailable from sandbox allowlist; user upload requested to /home/user/dls26-omega/apk/dls26.apk (com.firsttouchgames.dls7)'
}
mpath=os.path.join(ROOT,'handoff','audit_manifest.json')
with open(mpath,'w') as f: json.dump(manifest,f,indent=2)
print(f'Wrote {mpath}')
