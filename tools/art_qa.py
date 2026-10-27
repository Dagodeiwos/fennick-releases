"""Art accuracy checks. Run after build_assets.py and build_site.py. Exit 1 on any failure."""
import json,re,sys,os
from PIL import Image
R=os.environ.get('ART_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.environ.get('ART_SITE') or (R+'/site' if os.path.isdir(R+'/site') else R+'/src/site')
A=SITE if os.path.exists(SITE+'/assets/mockups') else R
C=json.load(open(R+'/tools/art_claims.json')); bad=[]
for im in C['images']:
    p=f"{A}/{im['file']}"
    if not os.path.exists(p): bad.append('missing '+im['file']); continue
    if list(Image.open(p).size)!=im['size']: bad.append(f"size {im['file']}")
# terrain placements: build_assets.py already fails on these; re-check the saved data exists
pl=json.load(open(R+'/tools/scene_placements.json'))
for n in ('trailmarks','cartographer'):
    if n not in pl: bad.append('no placement data for '+n)
# versions on every page match the suite
site=SITE; pages=[site+'/index.html']+[f'{site}/addons/{f}' for f in os.listdir(site+'/addons')]
want=C['suite']
for pg in pages:
    t=open(pg).read()
    import html as H
    for nm,v in re.findall(r'> ([^<>]+?) <span class="badge[^"]*">[^<]*</span> <span class="ver">([\d.]+)',t):
        nm=H.unescape(nm); key=[k for k in want if nm.endswith(k)]
        if not key: bad.append(f'{os.path.basename(pg)}: unknown add-on {nm}')
        elif want[key[0]]!=v: bad.append(f'{os.path.basename(pg)}: {nm} shows {v}, suite is {want[key[0]]}')
    for v in re.findall(r'Version (\d+\.\d+\.\d+)',t):
        if v not in want.values(): bad.append(f'{pg}: unknown version {v}')
    # every mockup figure is captioned as a mockup
    if t.count('/assets/mockups/') and t.count('class="badge mock">Mockup')*2 < t.count('/assets/mockups/'): bad.append(pg+': mockup without caption')
    if 'ko-fi' in t.replace('<!--','\x00').split('\x00')[0].lower(): bad.append(pg+': donation link visible')
print('\n'.join(bad) or 'ART QA: all automated checks passed'); sys.exit(1 if bad else 0)
