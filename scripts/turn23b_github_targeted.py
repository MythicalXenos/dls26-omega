#!/usr/bin/env python3
"""Turn 23 wave 2: targeted code searches with 30 fresh search calls, slow pagination (2.5s), inspect code snippets for meaningful content."""
import json,urllib.request,urllib.parse,time,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'logs/research/github_sweep_turn23b.jsonl')
QUERIES=[
  ('code','"Form Boost" "dream league"'),
  ('code','"Dream Points" DLS'),
  ('code','"Season Pass" DLS'),
  ('code','"com.firsttouchgames.dls7"'),
  ('code','"dream league soccer" stats formula'),
  ('code','"dream league" coach rarity'),
  ('code','"dream league soccer" algorithm'),
  ('code','DLS26 coach'),
  ('code','dls26 squad'),
  ('code','"Dream League" pack simulator'),
  ('code','"dream league soccer" discord'),
]
def gh(url):
    req=urllib.request.Request('https://api.github.com'+url,headers={'Accept':'application/vnd.github.v3.text-match+json','User-Agent':'dls26-omega'})
    with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode('utf-8'))
def search(kind,q,max_pages=2):
    items=[]; page=1
    while True:
        qq=urllib.parse.quote(q,safe='')
        url=f'/search/{kind}?q={qq}&per_page=100&page={page}'
        try: data=gh(url)
        except Exception as e: print(' err',e); break
        it=data.get('items',[]); tot=data.get('total_count',0); items+=it
        print(f'  p{page}: {len(it)}/{tot}')
        if not it or len(it)<100: break
        page+=1; time.sleep(2.5)
        if page>max_pages: break
    return {'kind':kind,'query':q,'total':tot,'items':items}
results=[]
for kind,q in QUERIES:
    print(f'--- {kind}: {q}')
    r=search(kind,q); results.append(r); time.sleep(2.5)
with open(OUT,'w') as fh:
    for r in results: fh.write(json.dumps(r)+'\n')
# Analyze
import collections
repos=collections.Counter()
for r in results:
    for it in r['items']:
        repos[it.get('repository',{}).get('full_name','?')]+=1
print('\nTop repos:')
for n,c in repos.most_common(25): print(f'  {c:4d} {n}')
# look for DLS-specific repos (>3 hits) and non-trivial file paths
print('\nFiles in non-polyglot/non-fork repos:')
for r in results:
    for it in r['items']:
        repo=it.get('repository',{}).get('full_name','')
        if repos[repo]>=2 and 'wasswacosmas' not in repo and 'gpsyrou' not in repo:
            print(f"  {repo:40s} {it.get('path','')}")
