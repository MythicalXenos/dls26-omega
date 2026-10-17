#!/usr/bin/env python3
"""Turn 23: continue GitHub code-search pagination for the DLS26 query (1122 hits, 200 captured turn 22) + additional precise queries."""
import json,urllib.request,urllib.parse,time,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'logs/research/github_sweep_turn23.jsonl')
QUERIES=[
  ('code','DLS26'),
  ('code','"dream league soccer" coach'),
  ('code','"dream league soccer" ovr'),
  ('code','"dream league soccer" stamina'),
  ('code','"DLS Manager"'),
  ('code','footballgamingbd'),
]
def gh(path):
    req=urllib.request.Request('https://api.github.com'+path,headers={'Accept':'application/vnd.github+json','User-Agent':'dls26-omega'})
    with urllib.request.urlopen(req,timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))
def search(kind,q,max_pages=6):
    all_items=[]; page=1
    while True:
        qq=urllib.parse.quote(q,safe='')
        url=f'/search/{kind}?q={qq}&per_page=100&page={page}'
        try:
            data=gh(url)
        except Exception as e:
            print('   err',e); break
        items=data.get('items',[]); total=data.get('total_count',0)
        all_items.extend(items)
        print(f'   page {page}: {len(items)}/{total}')
        if not items or len(items)<100: break
        page+=1; time.sleep(2.2)
        if page>max_pages: break
    return {'kind':kind,'query':q,'total':total,'items':all_items}
results=[]
for kind,q in QUERIES:
    print(f'--- {kind}: {q}')
    r=search(kind,q); results.append(r); time.sleep(2)
with open(OUT,'w') as fh:
    for r in results: fh.write(json.dumps(r)+'\n')
# report top non-trivial repos
import collections
repos=collections.Counter()
for r in results:
    for it in r['items']:
        repo=it.get('repository',{}).get('full_name') if 'repository' in it else it.get('full_name')
        repos[repo]+=1
print('\nTop repos captured:')
for name,c in repos.most_common(25): print(f'  {c:4d} {name}')
print('wrote',OUT)
