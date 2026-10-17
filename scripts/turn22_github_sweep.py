#!/usr/bin/env python3
"""Turn 22 — exhaustive GitHub search sweep across code, repos, and issues on api.github.com.
Paginates until empty and captures results; does NOT clone (no git clone of large repos inside turn ceiling).
Outputs logs/research/github_sweep_turn22.jsonl
"""
import json, urllib.request, urllib.parse, time, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'logs/research')
os.makedirs(OUT,exist_ok=True)
OUT+='/github_sweep_turn22.jsonl'
QUERIES=[
  # code
  ('code','com.firsttouchgames.dls7 filename:build.gradle'),
  ('code','com.firsttouchgames.dls7 extension:json'),
  ('code','"dream league soccer" dls26 "formula"'),
  ('code','"dream league soccer" "OVR"'),
  ('code','"Dream League Soccer 2026"'),
  ('code','"DLS26"'),
  ('code','"firsttouchgames" "Dream League" save'),
  ('code','"Dream League Live"'),
  ('code','"com.firsttouchgames"'),
  ('code','"dream league soccer" coach rarity'),
  ('code','"dream league soccer" "form boost"'),
  # repos
  ('repositories','dream league soccer 2026'),
  ('repositories','dls26'),
  ('repositories','dream league soccer save editor'),
  ('repositories','dream league soccer squad builder'),
  ('repositories','first touch games dls'),
  ('repositories','dls kit'),
  ('repositories','dream league soccer 2026 apk'),
  ('repositories','dream league soccer hack'),
  # issues/PRs mentioning mechanics
  ('issues','"dream league soccer" script'),
  ('issues','"dream league soccer" algorithm'),
  ('issues','dream league soccer 2026 bug'),
]
def gh(path):
    req=urllib.request.Request('https://api.github.com'+path,headers={'Accept':'application/vnd.github+json','User-Agent':'dls26-omega'})
    with urllib.request.urlopen(req,timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))
results=[]
for kind,q in QUERIES:
    print(f'--- {kind}: {q}')
    all_items=[]
    page=1
    while True:
        qq=urllib.parse.quote(q, safe='')
        if kind=='code':
            url=f'/search/code?q={qq}&per_page=100&page={page}'
        elif kind=='repositories':
            url=f'/search/repositories?q={qq}&per_page=100&page={page}'
        else:
            url=f'/search/issues?q={qq}&per_page=100&page={page}'
        try:
            data=gh(url)
        except Exception as e:
            print('   err',e); break
        items=data.get('items',[])
        total=data.get('total_count',0)
        all_items.extend(items)
        print(f'   page {page}: {len(items)}/{total}')
        if not items or len(all_items)>=min(total,300) or 'Link' not in data and len(items)<100: break
        # crude: stop if items fewer than 100 and we didn't see a Link header; api.github.com omits rel=next then
        if len(items)<100: break
        page+=1; time.sleep(2)
        if page>4: break  # 400 cap per query
    results.append({'kind':kind,'query':q,'total':total,'items':all_items})
    time.sleep(2)
with open(OUT,'w') as fh:
    for r in results:
        fh.write(json.dumps(r)+'\n')
# summary
for r in results:
    print(r['kind'],'|',r['query'],'| total',r['total'],'captured',len(r['items']))
print('wrote',OUT)
