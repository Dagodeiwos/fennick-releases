"""Art checks: the one art tool (main's art QA + the suite-UX 6b bookkeeping, merged).
  python3 tools/art_qa.py              full art accuracy checks (run after build_assets.py and build_site.py; see ART_QA.md)
  python3 tools/art_qa.py --changed    bookkeeping for the images changed since the merge base (RANGE env, default
                                       origin/main...HEAD, plus the working tree): every changed image needs a checklist line
                                       (in tools/art_claims.json, reviews/artzy/*.md as "<file> | pass/fix | note", or ART_NOTES);
                                       add-on versions on the site vs the .toc files are listed (informational: the site follows
                                       releases). The full checks also run when a site image or page changed.
Exit 1 on any failure."""
import json,re,sys,os,glob,subprocess
R=os.environ.get('ART_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.environ.get('ART_SITE') or (R+'/site' if os.path.isdir(R+'/site') else R+'/src/site')
A=SITE if os.path.exists(SITE+'/assets/mockups') else R
C=json.load(open(R+'/tools/art_claims.json'))
IMG=('.png','.webp','.tga','.jpg','.jpeg','.svg','.blp')
def full_checks():
    from PIL import Image
    bad=[]
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
    # compat.json vs .toc interfaces/versions and the generated compatibility table (tools/compat_check.py)
    if os.path.exists(SITE+'/data/compat.json'):
        r=subprocess.run([sys.executable,R+'/tools/compat_check.py'],capture_output=True,text=True)
        print(r.stdout.strip())
        if r.returncode: bad.append('compat check failed (see above)')
    return bad
def git(*a): return subprocess.run(['git','-C',R,*a],capture_output=True,text=True).stdout.split('\n')
def changed_bookkeeping(rng):
    files={f for f in git('diff','--name-only','--diff-filter=AM',rng)+git('diff','--name-only','--diff-filter=AM')+git('ls-files','--others','--exclude-standard') if f.endswith(IMG)}
    moved={l.split('\t')[-1] for l in git('diff','--name-status','-M','-C',rng) if l[:1] in 'RC' and l[1:4]=='100'}
    notes=''.join(open(p,encoding='utf-8').read() for p in glob.glob(R+'/reviews/artzy/*.md'))
    if os.environ.get('ART_NOTES') and os.path.exists(os.environ['ART_NOTES']): notes+=open(os.environ['ART_NOTES'],encoding='utf-8').read()
    claimed={os.path.splitext(im['file'])[0] for im in C['images']}
    missing=[]
    for f in sorted(files):
        base=os.path.basename(f); stem=os.path.splitext(f.split('site/',1)[-1])[0]
        if f in moved or stem in claimed or re.search(r'^\s*\|?\s*[^|\n]*'+re.escape(base)+r'[^|\n]*\|\s*(pass|fix)\b',notes,re.M|re.I): continue
        missing.append(f)
    toc={}
    for t in glob.glob(R+'/addons/*/*.toc'):
        m=re.search(r'^## Version:\s*(\S+)',open(t).read(),re.M); toc[os.path.basename(os.path.dirname(t))]=m.group(1) if m else None
    NAMES={'Beast Core':'Fennick_BeastCore','Guidepost':'Fennick_Guidepost','Rest':'Fennick_Rest','Reputation':'Fennick_Reputation',
           "Merchant's Favor":'Fennick_MerchantsFavor','Fox Trials':'Fennick_FoxTrials','Trailmarks':'Fennick_Trailmarks','Cartographer':'Fennick_Cartographer'}
    drift=sorted({f'{label}: site/claims {v}, toc {toc[folder]}' for label,folder in NAMES.items() for v in [C['suite'].get(label)] if v and toc.get(folder) and v!=toc[folder]})
    for f in sorted(files): print(('MOVED ' if f in moved else 'NO-CHECKLIST ' if f in missing else 'CHECKED ')+f)
    for d in drift: print('VERSION '+d)
    site_touched=any(f.startswith('site/') for f in files) or any(f.startswith(('site/','tools/compat','tools/build_compat')) or f.endswith('.toc') for f in git('diff','--name-only',rng)+git('diff','--name-only')+git('ls-files','--others','--exclude-standard'))
    return files,missing,drift,site_touched
if __name__=='__main__':
    if '--changed' in sys.argv:
        rng=os.environ.get('RANGE','origin/main...HEAD')
        files,missing,drift,site=changed_bookkeeping(rng)
        bad=full_checks() if site else []
        for b in bad: print(b)
        print(f'{len(files)} changed images, {len(missing)} without a checklist line, {len(drift)} site versions behind the branch (informational)'
              + (', full art checks '+('failed' if bad else 'passed') if site else ''))
        sys.exit(1 if (missing or bad) else 0)
    bad=full_checks()
    print('\n'.join(bad) or 'ART QA: all automated checks passed'); sys.exit(1 if bad else 0)
