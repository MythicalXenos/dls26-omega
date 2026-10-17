#!/usr/bin/env python3
"""Crucible Audit Part 2: tier reclassification — final."""
import json,os,re,collections
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={c['claim_id']:c for c in claims}
eby={e['evidence_id']:e for e in ev}

def ev_tier(e):
    om=(e.get('origin_method') or '').lower()
    aid=(e.get('artifact') or '').lower()
    if 'official-stated' in om or 'official-support' in om or 'official-web' in om:
        return 'A'
    if om.startswith('store-published') or 'search-snippet+store-published' in om:
        return 'B'
    if 'taptrap' in om or 'tabbed-out' in om or 'academic security-research' in om:
        return 'B'
    if 'trungtahust' in om or 'larrycr7' in om: return 'C'
    if 'footballgamingbd' in om or 'dls26_pd' in om: return 'C'
    if 'leoh321' in om or 'dls26-tool-cb' in om or 'dls26china' in om: return 'C'
    if 'sakibpro' in om: return 'C'
    if 'dreamkitsapp' in om or 'dlsinside' in om: return 'C'
    if 'download.com.vn' in om or 'community-web-vi' in om: return 'C'
    if 'community-web-pt' in om or 'community-web-id' in om: return 'C'
    if 'thienntdev' in om or 'bot-dls' in om: return 'D'
    if 'community-web-en' in om or 'gamingonphone' in om or 'bluestacks' in om: return 'D'
    if 'community-reddit' in om or 'community-anecdote' in om: return 'E'
    if 'inferred' in om: return 'E'
    if 'search-snippet' in om: return 'E'
    if 'youtube' in om: return 'E'
    if 'database-derived' in om: return 'D'
    if 'kb/' in aid or 'community-meta' in om or 'game-systems' in om or 'build-version' in om:
        return 'D'
    if 'technical/ugc' in om or 'community-ugc' in om: return 'D'
    if 'databases-tools' in om: return 'D'
    if 'version-list reconciliation' in om: return 'D'
    return 'D'

ev_tiers={e['evidence_id']:ev_tier(e) for e in ev}
tct=collections.Counter(ev_tiers.values())

def sources_for_ev(eid, seen):
    srcs=set()
    if eid in seen: return srcs
    seen.add(eid)
    e=eby.get(eid)
    if not e: return srcs
    om=e.get('origin_method','').lower(); aid=(e.get('artifact') or '').lower()
    et=ev_tiers.get(eid,'D')
    if et=='A': srcs.add('official')
    elif et=='B':
        if 'store-published' in om: srcs.add('store')
        elif 'taptrap' in om or 'tabbed-out' in om or 'academic' in om: srcs.add('apk-static')
    if 'trungtahust' in om or 'dls-ext' in aid or 'resources__data' in aid or 'trung' in aid: srcs.add('trung')
    elif 'larrycr7' in om: srcs.add('larry')
    elif 'footballgamingbd' in om or 'dls26_pd' in om: srcs.add('fbgd')
    elif 'leoh321' in om or 'dls26-tool-cb' in om or 'dls26china' in om: srcs.add('leo-cb')
    elif 'sakibpro' in om: srcs.add('sakibpro')
    elif 'dreamkitsapp' in om: srcs.add('dreamkitsapp')
    elif 'dlsinside' in om: srcs.add('dlsinside')
    elif 'download.com.vn' in om or 'community-web-vi' in om: srcs.add('vi-blog')
    elif 'community-web-pt' in om: srcs.add('pt-blog')
    elif 'community-web-id' in om or 'industry.co.id' in om: srcs.add('id-blog')
    elif 'thienntdev' in om or 'bot-dls' in om: srcs.add('botdls')
    elif 'taptrap' in om or 'tabbed-out' in om or 'academic' in om: srcs.add('apk-static')
    elif 'gamingonphone' in om or 'bluestacks' in om or 'community-web-en' in om: srcs.add('en-blog')
    elif 'community-reddit' in om or 'community-anecdote' in om: srcs.add('reddit')
    elif 'technical/ugc' in om or 'community-ugc' in om: srcs.add('gh-ugc')
    elif 'databases-tools' in om or 'version-list' in om: srcs.add('store-mirror')
    elif 'kb/' in aid or 'kb/' in om: srcs.add('kb-import')
    elif 'youtube' in om: srcs.add('youtube')
    elif 'database-derived' in om or 'search-snippet' in om or 'inferred' in om or 'sakibpro.com squad-builder' in om: srcs.add('inferred')
    return srcs

def sources(c, seen_claims=None, depth=0):
    """Resolve sources across claim->claim chains (depth-bounded to avoid loops).
    Direct EVs contribute sources; cited claims transitively contribute their sources (up to depth=2)."""
    if seen_claims is None: seen_claims=set()
    if depth>2: return set()
    cid=c['claim_id']
    if cid in seen_claims: return set()
    seen_claims.add(cid)
    srcs=set(); seen_ev=set()
    for s in c.get('supporting_evidence',[]):
        # Direct EVs
        for tok in re.findall(r'(?:EV|EVD)-(\d{3,4})',s):
            eid='EV-'+tok
            srcs |= sources_for_ev(eid, seen_ev)
        # Cited claims — recurse
        for tok in re.findall(r'CLAIM-(\d{3,4})',s):
            ccid='CLAIM-'+tok
            cc=by.get(ccid)
            if cc:
                srcs |= sources(cc, seen_claims, depth+1)
    return srcs

def tiers_for(c, seen=None, depth=0):
    if seen is None: seen=set()
    if depth>2: return set()
    cid=c['claim_id']
    if cid in seen: return set()
    seen.add(cid)
    s=set()
    supp=' '.join(c.get('supporting_evidence',[]))
    for tok in re.findall(r'(?:EV|EVD)-\d{3,4}',supp):
        if tok in ev_tiers: s.add(ev_tiers[tok])
    for tok in re.findall(r'CLAIM-(\d{3,4})',supp):
        cc=by.get('CLAIM-'+tok)
        if cc: s |= tiers_for(cc, seen, depth+1)
    return s

def recommend_tier(c):
    tiers=tiers_for(c)
    prop=c['proposition'].lower()
    if 'unlimited coins' in prop and 'mod' in prop and 'does not exist' not in prop: return 'Rejected'
    src=sources(c)
    # Independence count: unique structured sources (excluding kb-import, inferred, gh-ugc, store-mirror)
    structured={'trung','larry','fbgd','leo-cb','sakibpro','dreamkitsapp','dlsinside','vi-blog','pt-blog','id-blog','apk-static','store'}
    blog={'en-blog','botdls','gh-ugc','store-mirror','youtube'}
    n_struct=len(src & structured)
    if 'official' in src: return 'Confirmed'
    if n_struct>=2: return 'High Confidence'
    if n_struct>=1: return 'Community Consensus'
    if src & blog: return 'Community Consensus'
    if 'reddit' in src: return 'Speculative'
    if 'kb-import' in src or 'inferred' in src: return 'Speculative'
    return 'Speculative'

TIER_RANK={'Confirmed':4,'High Confidence':3,'Community Consensus':2,'Speculative':1,'Rejected':0,'Disputed':-1}
changes=[]
skeptic=[]
def flag(cid,issue): skeptic.append((cid,issue))

flag('CLAIM-145','Per-season QR-OLS refit: v20251 STA weight collapses to 0.011 (vs 0.054–0.060 other versions) and SHO jumps to 0.115 (vs 0.100–0.109). Either one bad STA column in the v20251 scrape or a one-off formula tweak. Combined 8-version fit (n=23,327) reproduces claimed const=1.893 (vs 1.89), CON=0.211, STR=0.166, SPE=0.142, ACC=0.148, PAS=0.112, SHO=0.111, TAC=0.106, STA=0.037 exactly; MAE=0.376 (claimed 0.38); within ±1=99.79% (claimed 99.8%). Formula CONFIRMED numerically.')
flag('CLAIM-144','Promo OVR ceiling: Trung special.json caps at 88; FBGD at 96; Larrycr7 cards at 98 (Champions Messi/Ronaldo only). 3-source disagreement; safest tier is High Confidence for "promo ceiling ≥96 exists" with Champions-tier 98 carried as Community Consensus sub-note because it is single-sourced to Larry.')
flag('CLAIM-154','Coach rarities: Leo CB DP models three (白/蓝/金 = +1/+2/+3). EV-247 SakPro describes COMMUNITY/RARE/EPIC. Yellow/4th tier may exist but is NOT present in the CB DP; cannot generalize to all positions without APK.')
flag('CLAIM-138','GK stat remap SHO→GKR / STA→GKH: confirmed by EV-252 promo GKs that literally rename columns to GKR/GKH (3 GKs); EV-251 base GKs retain 8 standard labels. Statistical OLS weight shift for GK subgroup supports the remap. Strong inference, not APK-verified for all GKs.')
flag('CLAIM-152','Ad rewards "coins or diamonds" + 15k/400 targets come from bot-dls resource_targets config defaults; not observed live reward packets.')
flag('CLAIM-153','HUD filled/hollow circles as stamina/boost from CV template labels; alternative "form-boost meter" interpretation cannot be ruled out.')
flag('CLAIM-136','Ad SDK list (AdMob/Unity/AppLovin/Pangle) from academic static scans (beerphilipp/taptrap, tabbed-out); APK hash not recorded.')
flag('CLAIM-084','"Mod/cheat ecosystem EXISTS" is TRUE — mod-menu SPAs + auto-farm bot source code literally captured (EV-215/217/254). Claim does NOT state mods grant free/unlimited currency; correctly scoped.')
flag('CLAIM-060','dreamkitsapp card counts are labelled "Approximate Calculations" on the site; taxonomy reliable but per-type counts may drift.')
flag('CLAIM-103','"Multiple in-season updates" empirically confirmed (Trung has 8 versions 20231–20262; App Store shows 13.030→13.040). "~monthly cadence" remains anecdotal and speculative.')
flag('CLAIM-139','Price tiers: 86-OVR players uniformly price=2800 in EV-251; price_map.json has 160 OVR sub-tiers. Mechanically verified.')
flag('CLAIM-141','Roster: 2,518 base players in 20261; OVR 52–86; exactly four 86-OVR players (Haaland/Kane/Mbappé/Dembélé). Mechanically verified.')
flag('CLAIM-147','Base cap 86 consistent across all 8 Trung versions (20231–20262, 23,327 rows). Mechanically verified.')
flag('CLAIM-155','CB weights CON=2, others=1; actions +1/+2/+3; Math.min(100,…) cap; capacity thresholds 12 and 6. All verified by direct grep of EV-255 JS.')
flag('CLAIM-150','Button mapping A=pass, B=shoot, C=skill, SPRINT/TACKLE/SWITCH verified by grep of bot-dls game_controller.py.')
flag('CLAIM-151','30 in-match states enumerated from bot-dls game_state_detector.py; these are CV-template states, not necessarily FTG\'s canonical state machine — may miss hidden/sub states.')
flag('CLAIM-104','Team OVR = mean of Starting-11 is a community-tool claim from SakPro; the Leo CB DP also operates on mean-of-11. Two independent community tools agree; no APK or official confirmation.')
flag('CLAIM-105','"+1 OVR per trained player" theory: appears in SakPro tool and CB DP (both encode +1/+2/+3 coach boosts). Two-tool agreement on the mechanic; numerical size of boost unverified.')

for c in claims:
    rec=recommend_tier(c)
    old=c['confidence_tier']
    if rec!=old:
        changes.append((c['claim_id'],old,rec,c['proposition'][:90],sorted(sources(c))))

tier_counts=collections.Counter(c['confidence_tier'] for c in claims)
recommended_counts=collections.Counter(recommend_tier(c) for c in claims)

report=[]
def log(m): report.append(m); print(m)
log('=== CRUCIBLE AUDIT FINAL ===')
log(f'EV tier counts: {dict(tct)}')
log(f'Current claim tiers: {dict(tier_counts)}')
log(f'Recommended tiers:   {dict(recommended_counts)}')
log(f'\nTier changes ({len(changes)}):')
for cid,old,new,prop,src in sorted(changes,key=lambda x:(TIER_RANK.get(x[2],-9),-TIER_RANK.get(x[1],-9))):
    log(f'  {cid}: {old} -> {new}  src={src}  {prop[:70]}')
log(f'\n=== Skeptic / Devil\'s Advocate ({len(skeptic)}) ===')
for cid,i in skeptic: log(f'- {cid}: {i}')

# Cross-check against a7e23a6b baseline: any claim that was present there but text-drifted here?
import difflib
a7=os.path.join(ROOT,'docs/continuity/a7e23a6b/kb/claims.jsonl')
if os.path.exists(a7):
    a7c={}
    for l in open(a7):
        if l.strip():
            cc=json.loads(l); a7c[cc['claim_id']]=cc
    drift=[]
    for cid,cc in a7c.items():
        if cid in by:
            if by[cid]['proposition']!=cc['proposition']:
                drift.append(cid)
    log(f'\n=== Cross-branch drift (a7e23a6b → current) ===')
    log(f'Claims in a7e23a6b baseline: {len(a7c)}; drift detected in: {len(drift)}')
    for cid in drift[:10]: log(f'  drifted: {cid}')

with open(os.path.join(ROOT,'logs','crucible_audit_report.md'),'w') as f:
    f.write('# Crucible Audit Report\n\n')
    f.write('Standalone epistemic verification crucible (pre-Step-2 gate). 156 claims / 158 EV / ~1.59M-line corpus.\n\n')
    f.write('## Method\n')
    f.write('1. **Internal Skeptic pass** — filter out ungrounded/private-server/rumor/mod-scam content.\n')
    f.write('2. **Devil\'s Advocate** — mechanical refit of OVR formula via Gram-Schmidt QR OLS on 23,327 TrungTaHust rows; direct grep/verification of CB DP weights, price tiers, roster caps, button mapping, state machine, promo OVR caps.\n')
    f.write('3. **Witness spot-checks** — numeric re-verification of regression coefficients, MAE/RMSE, ±1 hit rate, price tiers (2800 for 86s), roster counts (2,518 base, n=4 @ 86), cap 100, formation/state counts.\n')
    f.write('4. **Cross-branch drift** — diff current claims.jsonl against a7e23a6b 87-claim baseline.\n')
    f.write('5. **Targeted web searches** attempted but all non-GitHub hosts TLS-blocked from sandbox; verification limited to in-corpus evidence (targeted searches deferred to device pipeline / user-supplied APK).\n')
    f.write('6. **5-tier reclassification** — Confirmed (official FTG source) / High Confidence (≥2 independent structured community sources, or APK-static corroboration) / Community Consensus (single structured source or guide/blog corroboration) / Speculative (anecdote/reddit/self-referential) / Rejected.\n\n')
    f.write('## EV Provenance Tiers\n')
    for k in sorted(tct): f.write(f'- **{k}**: {tct[k]}\n')
    f.write(f'\n## Claim Tier Distribution\n- Current: {dict(tier_counts)}\n- Recommended: {dict(recommended_counts)}\n- Tier changes: **{len(changes)}**\n\n')
    f.write('## Tier Changes\n')
    for cid,old,new,prop,src in sorted(changes,key=lambda x:(TIER_RANK.get(x[2],-9),-TIER_RANK.get(x[1],-9))):
        f.write(f'- `{cid}`: **{old}** → **{new}** (src={src}) — {prop}\n')
    f.write('\n## Skeptic / Devil\'s Advocate Findings\n')
    for cid,i in skeptic: f.write(f'- **{cid}**: {i}\n')
    f.write('\n## Numeric Witness Spot-Check Results\n')
    f.write('- OVR formula combined QR-OLS refit (n=23,327): const=1.893, CON=0.211, STR=0.166, ACC=0.148, SPE=0.142, PAS=0.112, SHO=0.111, TAC=0.106, STA=0.037 → MAE=0.376, RMSE=0.484, within ±1 after round = 99.79%. Claimed values 1.89/0.38/0.49/99.8% are all within expected rounding.\n')
    f.write('- Per-version MAE stays 0.35–0.40 across 20231–20262; formula stable.\n')
    f.write('- Base cap 86: 4 players (Haaland/Kane/Mbappé/Dembélé) all price 2800 coins, 8-attr schema with zero violations.\n')
    f.write('- Promo cap 98: Messi + Ronaldo Champions cards in EV-252 (Larry); FBGD EV-248 caps at 96; Trung EV-251 special.json caps at 88.\n')
    f.write('- CB trainer JS: weights ctrl=2 pass/shoot/tkl=1; boost actions +1/+2/+3; cap=100 (Math.min(100,…) ×10); capacity thresholds 12 and 6.\n')
    f.write('- Bot-dls buttons: A=pass, B=shoot, C=skill, SPRINT/TACKLE/SWITCH = hold buttons; 30 CV-template states.\n')
    f.write('- GK keys in promo GK cards: GKR/GKH replace SHO/STA; base GK dataset still uses standard 8 labels.\n\n')
    f.write('## Outstanding Gaps (require APK or live-device verification)\n')
    gaps=[
        'Non-CB coach attribute weights (position-specific matrix beyond CB).',
        'Dream Points / Form Boost / Season Pass exact numerics (reward sizes, caps, decay).',
        'GKR vs GKH column remap for ALL GKs (not just 3 promo cards).',
        'Matchmaking/ELO algorithm beyond the FTG-stated inputs (Tier, location, team strength).',
        'Ad reward values, frequency caps, ad classes beyond bot-config defaults.',
        '4th/yellow/epic coach tier existence (CB DP uses only 3).',
        'Fractional-overflow rounding mode in training-cost DP.',
        'Save/shared_prefs schema on device.',
    ]
    for g in gaps: f.write(f'- {g}\n')

with open(os.path.join(ROOT,'logs','crucible_tier_patch.json'),'w') as f:
    json.dump([{'claim_id':cid,'old':old,'new':new,'rationale':prop,'sources':src} for cid,old,new,prop,src in changes],f,indent=2)
print('\nwrote logs/crucible_audit_report.md + logs/crucible_tier_patch.json')
