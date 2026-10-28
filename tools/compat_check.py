"""Compatibility checks: site/data/compat.json vs the .toc files, the site versions and the pages.
Fails (exit 1) on:
  - a client marked 'yes' whose interface number is missing from every .toc of that add-on
    (e.g. era_hc 'yes' without 11509), or a .toc that ships an interface the table marks 'no'
  - compat.json versions that differ from the released versions in tools/art_claims.json (the site shows those)
  - an add-on folder in addons/ with no compat.json row, or a row with no folder
  - pages out of date with compat.json (tools/build_compat.py --check)
Informational: compat.json version vs the branch .toc ## Version (the site follows releases).
Without an addons/ folder (fennick-releases) the .toc checks are skipped and said so."""
import json,os,re,sys,glob,subprocess
R=os.environ.get('ART_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.environ.get('ART_SITE') or R+'/site'
D=json.load(open(SITE+'/data/compat.json',encoding='utf-8'))
C=json.load(open(R+'/tools/art_claims.json',encoding='utf-8'))
bad=[];info=[]
for a in D['addons']:
    for k,v in a.items():
        if k in D['clients'] and v not in ('yes','planned','no'): bad.append(f'{a["short"]}: {k} is {v!r}, use yes/planned/no')
    rel=C['suite'].get(a['short'])
    if rel and rel!=a['version']: bad.append(f'{a["short"]}: compat.json {a["version"]}, site/release {rel}')
for a in D['addons']:
    if a['short']=='Fox Trials' and (a['era_hc']!='no' or a['other']!='no'): bad.append('Fox Trials must stay Forever only until approved')
if os.path.isdir(R+'/addons'):
    folders={os.path.basename(p) for p in glob.glob(R+'/addons/Fennick_*') if glob.glob(p+'/*.toc')}
    rows={a['folder'] for a in D['addons']}
    for f in sorted(folders-rows): bad.append(f'{f}: no row in compat.json')
    for f in sorted(rows-folders): bad.append(f'{f}: in compat.json but no add-on folder')
    for a in D['addons']:
        tocs=glob.glob(f'{R}/addons/{a["folder"]}/*.toc')
        if not tocs: continue
        ifaces=set(); ver=None
        for t in tocs:
            s=open(t,encoding='utf-8').read()
            m=re.search(r'^## Interface:\s*(.+)$',s,re.M)
            if m: ifaces|={x.strip() for x in m.group(1).split(',')}
            v=re.search(r'^## Version:\s*(\S+)',s,re.M); ver=ver or (v and v.group(1))
        for k,c in D['clients'].items():
            n=c['interface']
            if not n: continue
            if a[k]=='yes' and n not in ifaces: bad.append(f'{a["short"]}: marked supported on {c["label"]} but no .toc has Interface {n}')
            if a[k]=='no' and n in ifaces: bad.append(f'{a["short"]}: a .toc has Interface {n} but {c["label"]} is marked not supported')
            if a[k]=='planned' and n in ifaces: info.append(f'{a["short"]}: .toc has {n}; switch {k} to yes after the in-game checks pass')
        if ver and ver!=a['version']: info.append(f'{a["short"]}: site {a["version"]}, branch toc {ver}')
    print(f'toc check: {len(D["addons"])} add-ons, {len(folders)} folders')
else: print('toc check skipped: no addons/ folder here (run it in fennick-addons)')
r=subprocess.run([sys.executable,R+'/tools/build_compat.py','--check'],capture_output=True,text=True)
if r.returncode: bad+=r.stdout.strip().split('\n')
for i in info: print('INFO '+i)
print('\n'.join(bad) or 'COMPAT: all checks passed'); sys.exit(1 if bad else 0)
