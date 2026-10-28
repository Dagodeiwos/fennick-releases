"""Write the compatibility table (site/compatibility.html) and the 'Works on' line on each add-on card
(site/index.html, site/addons/*.html) from site/data/compat.json. Edit the JSON, then run:
  python3 tools/build_compat.py          rewrite the generated parts
  python3 tools/build_compat.py --check  exit 1 if a page is out of date with compat.json (no writes)"""
import json,os,re,sys,html
R=os.environ.get('ART_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.environ.get('ART_SITE') or R+'/site'
D=json.load(open(SITE+'/data/compat.json',encoding='utf-8'))
E=html.escape
CELL={'yes':'✅ Supported','planned':'🛠 Planned','no':'⛔'}
MARK={'yes':'✅','planned':'🛠','no':'⛔'}
def cell(a,k):
    s=a[k]
    if k=='era_hc' and s=='no' and a['forever']=='yes': return '⛔ Forever only'
    return CELL[s]
def table():
    cl=D['clients']
    head=''.join(f'<th scope="col">{E(cl[k]["label"])}{" ("+cl[k]["build"]+")" if cl[k]["build"] else ""}</th>' for k in ('forever','era_hc','other'))
    rows=''.join(f'\n      <tr id="{a["slug"]}"><th scope="row">{E(a["name"])}</th><td>{a["version"]}</td>'
                 +''.join(f'<td>{cell(a,k)}</td>' for k in ('forever','era_hc','other'))+'</tr>' for a in D['addons'])
    return (f'<div class="tablewrap"><table class="compat">\n      <caption class="sr-only">Which WoW versions each add-on works on</caption>'
            f'\n      <thead><tr><th scope="col">Add-on</th><th scope="col">Released</th>{head}</tr></thead>\n      <tbody>{rows}\n      </tbody>\n    </table></div>')
def works(a):
    cl=D['clients']
    parts=[f'{cl["forever"]["short"]} {MARK[a["forever"]]}', f'{cl["era_hc"]["short"]} {MARK[a["era_hc"]]}']
    return f'<p class="works">Works on: {" · ".join(parts)} <a class="link" href="/compatibility.html#{a["slug"]}">Compatibility</a></p>'
def render(path,text):
    t=re.sub(r'(<!-- compat:table -->).*?(<!-- /compat:table -->)',lambda m:m.group(1)+table()+m.group(2),text,flags=re.S)
    for a in D['addons']:
        t=re.sub(r'<p class="works" data-addon="'+a['slug']+r'">.*?</p>|<p class="works">Works on:[^\n]*?compatibility\.html#'+a['slug']+r'">Compatibility</a></p>',works(a),t)
    return t
def pages(): return [SITE+'/compatibility.html',SITE+'/index.html']+sorted(f'{SITE}/addons/{f}' for f in os.listdir(SITE+'/addons'))
if __name__=='__main__':
    check='--check' in sys.argv; stale=[]
    for p in pages():
        old=open(p,encoding='utf-8').read(); new=render(p,old)
        if new!=old:
            stale.append(os.path.relpath(p,R))
            if not check: open(p,'w',encoding='utf-8').write(new)
    if check:
        print('\n'.join('STALE '+s+' (run tools/build_compat.py)' for s in stale) or 'compat pages match compat.json'); sys.exit(1 if stale else 0)
    print('updated: '+(', '.join(stale) or 'nothing'))
