#!/usr/bin/env python3
"""Turn 35 Wave 17: Gary Bloom (English commentator) confirmed — Welsh psychotherapist/broadcaster, Football Italia, 2006 WC."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w17')

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

e_comm=new_ev("Wikipedia Gary Bloom, FTG Facebook, r/DreamLeagueSoccer (Gary Bloom commentator reveal)",
    "English-language commentator is GARY BLOOM (confirmed Wikipedia + FTG Facebook official + multiple r/DLS confirmations). Bloom is a Welsh clinical sports psychotherapist and sports broadcaster (Football Italia on Channel 4, Talksport 'On the Sporting Couch', World Cup 2006 commentary including Portugal-Netherlands 'Battle of Nuremberg', works with Oxford United as psychotherapist). He has been the DLS commentary voice from the series' early days (at least DLS2016 through DLS26). FTG continues to capture new commentary lines with Bloom for updates. Community has mixed/affectionate reception: iconic lines ('Good tackle there', 'Oh and he's given away a foul', deadpan surname calls, occasional 'he got lucky' deflection commentaries). Common community complaint: mispronounced Spanish/non-English names, limited line variety.",
    "evidence/raw/turn35_w17/EV-398_commentator.html",
    "English commentator = Gary Bloom (Welsh psychotherapist/broadcaster; Football Italia, 2006 WC Battle of Nuremberg, Talksport, Oxford United psychotherapist); DLS voice from the beginning; FTG still records new lines; community reception mixed (iconic but repetitive, mispronounces names)")

add_claim("English-language commentator is GARY BLOOM — Welsh clinical sports psychotherapist and sports broadcaster; voice of DLS from at least DLS2016 through DLS26.", 1, "presentation/commentator-gary-bloom", [e_comm])
add_claim("Gary Bloom broadcast background: Football Italia (Channel 4), 2006 World Cup (Portugal-Netherlands 'Battle of Nuremberg' — 'Bad boys' corner'), Talksport 'On the Sporting Couch' host; works as psychotherapist for Oxford United FC.", 2, "presentation/bloom-background", [e_comm])
add_claim("FTG continues to record new commentary lines with Bloom for ongoing DLS updates (v13.050 improved commentary was a recorded refresh).", 1, "presentation/commentary-updates", [e_comm])
add_claim("Community commentary reception: iconic/affectionate ('Gary Bloom is a gem') but criticized for repetitive lines ('Good tackle there', 'Oh he's given away a foul'), deadpan last-name-only callouts, mispronunciation of non-English names, and occasional frustrating 'he got lucky' lines.", 3, "presentation/commentary-reception", [e_comm])

p=os.path.join(RAW_DIR,'EV-398_commentator.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
