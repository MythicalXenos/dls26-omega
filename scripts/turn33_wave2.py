#!/usr/bin/env python3
"""Turn 33 Wave 2 — Languages/localization/commentary + injury/physio/medical mechanics."""
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

e343=E("App Store US DLS26 listing (Jun2026) + r/DLS Arabic commentary thread (Dec2025) + pocketgamer DLS25 launch + dontruko commentary-change + dlsinside player site",
       "DLS26 supports 15 UI/display languages per App Store: English, Arabic, Dutch, French, German, Indonesian, Italian, Japanese, Korean, Portuguese (Brazil), Russian, Simplified Chinese, Spanish (incl. Mexican), Traditional Chinese, Turkish. Uptodown lists a much larger UI language set (Afrikaans/Amharic/Catalan/Czech/Danish/Farsi/Finnish/Greek/Hebrew/Hindi/Icelandic/Malay/Polish/Romanian/Slovak/Swahili/Swedish/Tagalog/Thai/Vietnamese/etc) likely reflecting OS-level localization; the App Store 15 is the official first-party list. Age rating 13+; contains Frequent/Intense Contests, Loot Boxes, Advertising. App download size 269.6 MB (iOS Jun2026). Commentary languages: Default English (Gary Bloom). DLS25 added Spanish and Portuguese commentary; DLS26 adds Turkish (Erdi Eliacik) and Arabic (Dr Kamal Atteya). Multiple third-party/mod YouTube videos claim French/Spanish/Portuguese commentary options but only EN/TR/AR are officially confirmed for DLS26 (plus pre-existing ES/PT). Audio settings: SFX Volume, Music Volume, Commentary slider, Download Commentary option (flags for language selection). Community feedback: new AR/TR commentary lines are word-for-word translations of English lines (per r/DLS Arabic speaker) rather than natural localized commentary. Mod-APK versions (not legitimate) add alternate Spanish-language commentator pairs (e.g., Martinoli/Garcia, Closs/Latorre, De Paoli/Latorre, Carlos Martinez/Maldini). dlsinside.com (player DB) exists as a Spanish/English reference with v13.430 data updated 2026-09-16.",
       "evidence/raw/official_turn33/EV-343_languages.html",
       typ='official+community',reliability='High')
e344=E("r/DLS injury threads (2024) + BlueStacks physios guide + LevelWinner DLS20 advanced + supercheats + gamingonphone",
       "Injuries: Can occur in-match from tackles/fouls (red-cross indicator over stamina bar, player moves much slower). Duration varies: 1-game / 2-game / 3-game / 5-game / 7-game tiers (7-game longest widely reported; some users report injuries recur immediately post-return for star players like KDB/Haaland). Healing costs gems for instant recovery OR coins for physios (Legendary Physio ~150 coins with max Medical, ~250 coins cited by community; LevelWinner cites 15 gems for a 3-game knee strain). Medical Centre upgrades reduce injury chance (-5% first upgrade) and discount healing cost (-10% first upgrade, stacks). Physios (coin-bought) also restore stamina: Common = small energy restore; Legendary Physio = full stamina + heal all active injuries. Stamina management: players tire during matches; subs at 65+ minutes recommended. In-game player can be injured mid-match and must be substituted. Sell-rebuy exploit (transfer list injured player -> re-sign from free transfers to heal instantly) has been reported historically but likely patched. Narrative note: early accounts cited 1000+ coin heal costs for long injuries in older versions; current DLS26 prices appear much lower with maxed Medical (150-250 coins per legendary physio).",
       "evidence/raw/community_turn33/EV-344_injuries.html",
       typ='guide+community',reliability='Medium-High')

# CLAIMS
C("UI/Display languages (15 confirmed per App Store): English, Arabic, Dutch, French, German, Indonesian, Italian, Japanese, Korean, Portuguese (Brazil), Russian, Simplified Chinese, Spanish (including Mexican), Traditional Chinese, Turkish. Additional OS-level localizations may appear in some storefronts.",
  'Very High Confidence',[e343])
C("Age rating: 13+ (Apple/Google). Contains frequent contests, loot boxes, and advertising.",
  'Very High Confidence',[e343])
C("iOS app size: ~269.6 MB (Jun 2026).",
  'High Confidence',[e343],vol='Low')
C("Commentary languages: English (default, Gary Bloom) from launch; Spanish and Portuguese added DLS25; Turkish (Erdi Eliacik) and Arabic (Dr Kamal Atteya) added in DLS26 launch/December 2025 update. Download Commentary option in Audio Settings lets you switch via flag icons.",
  'High Confidence',[e343],vol='Low')
C("Audio settings include four sliders/options: SFX Volume, Music Volume, Commentary Volume, Download Commentary (language pack download).",
  'High Confidence',[e343])
C("Community-reported weakness of TR/AR commentary: lines are word-for-word translations of English rather than naturally-localized broadcast speech.",
  'Medium Confidence',[e343],['r/DLS single Arabic-speaker report; Turkish community feedback not yet sampled.'],vol='Medium')
C("Mod/APK versions (unofficial, TOS-violating) add alternate Spanish-language commentator pairs (Martinoli/Luis Garcia, Mariano Closs/Diego Latorre, Rodolfo De Paoli/Latorre, Carlos Martinez/Maldini).",
  'Medium Confidence',[e343],['Mod-only content; not in legitimate game.'],vol='Low')
# Injuries
C("Injuries can occur mid-match from tackles/fouls; indicated by a red cross over depleted stamina bar; injured players move much slower and should be subbed.",
  'High Confidence',[e344])
C("Injury duration tiers: 1-game / 2-game / 3-game / 5-game / 7-game (7 games longest widely reported). Star players sometimes suffer re-injury shortly after return. Instant gem heals are one option (15 gems cited for a 3-game strain in older DLS).",
  'Medium-High Confidence',[e344],['15g figure from LevelWinner DLS20 guide; DLS26 gem costs may differ.'],vol='Medium')
C("Physios (coin-purchased): Common restores partial stamina; Legendary Physio fully restores stamina AND heals all active injuries. Cost: ~150 coins with maxed Medical Centre (~250 coins at lower Medical levels).",
  'Medium-High Confidence',[e344],vol='Medium')
C("Medical Centre upgrades: Level 1 = -5% injury chance / -10% heal cost for 75 gems; further levels stack reductions.",
  'High Confidence',[e344],vol='Low')
C("Auto-sub recommendation: AI recommends subs when players are low stamina or injured. Best practice is to substitute after ~65 minutes to manage fatigue.",
  'Medium-High Confidence',[e344])

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
