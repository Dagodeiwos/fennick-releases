# Builds hero, mockups and og images for fennickaddons.dev. Originals only.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random, os
B='/workspace/wow-forever/branding'; V2='/workspace/fennick-brand/final-v2'
OUT=os.environ.get('ART_OUT','/workspace/fennick-site-work/assets'); os.makedirs(OUT+'/mockups',exist_ok=True); os.makedirs(OUT+'/og',exist_ok=True); os.makedirs(OUT+'/hero',exist_ok=True)
TEAL=(14,74,85);DT=(8,52,60);GOLD=(212,166,74);LG=(240,208,138);AMB=(224,149,58);CR=(246,230,200)
CIN=V2+'/Cinzel-Bold-static.ttf'; SER='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'; SERB='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
F=lambda p,s: ImageFont.truetype(p,s)
def ic(name,size): return Image.open(f'{B}/{name}/icon_512.png').convert('RGBA').resize((size,size),Image.LANCZOS)
def pin(n,s=64): return Image.open(f'{B}/pins/{n}_64.png').convert('RGBA').resize((s,s),Image.LANCZOS)
FOX=Image.open(V2+'/fennick_icon_1024.png').convert('RGBA')
ADD=[('BeastCore',"Fennick's Beast Core",'beast-core'),('Guidepost',"Fennick's Guidepost",'guidepost'),('Rest','Fennick Rest','rest'),('Reputation','Fennick Reputation','reputation'),('MerchantsFavor',"Fennick Merchant's Favor",'merchants-favor'),('Trailmarks',"Fennick's Trailmarks",'trailmarks'),('Cartographer',"Fennick's Cartographer",'cartographer')]
def bg(w,h,seed=1):
    im=Image.new('RGB',(w,h),DT); d=ImageDraw.Draw(im)
    cx,cy=w*0.3,h*0.5
    for r in range(int(max(w,h)*0.9),0,-6):
        t=r/(max(w,h)*0.9); c=tuple(int(TEAL[i]*(1-t)+DT[i]*t) for i in range(3)); d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c)
    # original topographic contour lines (not map art)
    ov=Image.new('RGBA',(w,h),(0,0,0,0)); od=ImageDraw.Draw(ov); random.seed(seed)
    for k in range(14):
        pts=[];base=h*(k/13); ph=random.random()*6
        for x in range(0,w+20,20): pts.append((x,base+math.sin(x/140+ph)*h*0.05+math.sin(x/53+ph*2)*h*0.015))
        od.line(pts,fill=GOLD+(22,),width=2)
    random.seed(seed+7)
    for _ in range(int(w*h/9000)):
        x,y=random.random()*w,random.random()*h; a=random.randint(30,110); r=random.choice([1,1,1.5,2])
        od.ellipse([x-r,y-r,x+r,y+r],fill=LG+(a,))
    im=Image.alpha_composite(im.convert('RGBA'),ov); return im
def text_c(d,xy,s,f,fill,anchor='mm'): d.text(xy,s,font=f,fill=fill,anchor=anchor)
def glow(im,thing,pos,rad=18,col=GOLD,a=90):
    g=Image.new('RGBA',im.size,(0,0,0,0)); m=thing.split()[3]; sh=Image.new('RGBA',thing.size,col+(0,)); sh.putalpha(m.point(lambda v:min(a,v)))
    g.paste(sh,pos,sh); g=g.filter(ImageFilter.GaussianBlur(rad)); im.alpha_composite(g); im.alpha_composite(thing,pos)
def frame(im,col=GOLD): ImageDraw.Draw(im).rectangle([0,0,im.width-1,im.height-1],outline=col,width=1)

def hero(w,h,mobile=False):
    im=bg(w,h,3); d=ImageDraw.Draw(im)
    # faint pins scattered on right as "trail"
    pts=['ore_copper','herb_peacebloom','chest','quest','herb_silverleaf','ore_mithril','herb_mageroyal','ore_tin','chest']
    random.seed(5)
    if not mobile:
        for i,p in enumerate(pts):
            x=int(w*0.62+i*w*0.04); y=int(h*0.22+math.sin(i*0.9)*h*0.18+ (i%2)*h*0.35)
            t=pin(p,44); t.putalpha(t.split()[3].point(lambda v:v*0.55)); im.alpha_composite(t,(x,y))
        fs=int(h*0.62); fox=FOX.resize((fs,fs),Image.LANCZOS); glow(im,fox,(int(w*0.05),(h-fs)//2),30)
        x0=int(w*0.05)+fs+int(w*0.03)
        text_c(d,(x0,int(h*0.30)),"FENNICK'S ADDONS",F(CIN,int(h*0.12)),GOLD,'lm')
        d.line([x0,int(h*0.40),x0+int(w*0.42),int(h*0.40)],fill=AMB,width=3)
        text_c(d,(x0,int(h*0.49)),"Free add-ons for WoW Forever.",F(SER,int(h*0.055)),CR,'lm')
        text_c(d,(x0,int(h*0.57)),"One window, one arrow, out of your way.",F(SER,int(h*0.055)),LG,'lm')
        s=int(h*0.11)
        for i,(k,_,_) in enumerate(ADD): im.alpha_composite(ic(k,s),(x0+i*(s+14),int(h*0.68)))
    else:
        fs=int(w*0.5); fox=FOX.resize((fs,fs),Image.LANCZOS); glow(im,fox,((w-fs)//2,int(h*0.06)),26)
        text_c(d,(w//2,int(h*0.06)+fs+int(h*0.07)),"FENNICK'S",F(CIN,int(w*0.11)),GOLD)
        text_c(d,(w//2,int(h*0.06)+fs+int(h*0.15)),"ADDONS",F(CIN,int(w*0.11)),GOLD)
        y=int(h*0.06)+fs+int(h*0.205); d.line([w*0.25,y,w*0.75,y],fill=AMB,width=3)
        text_c(d,(w//2,y+int(h*0.045)),"Free add-ons for WoW Forever.",F(SER,int(w*0.045)),CR)
        s=int(w*0.1); tot=7*s+6*10; x=(w-tot)//2
        for i,(k,_,_) in enumerate(ADD): im.alpha_composite(ic(k,s),(x+i*(s+10),y+int(h*0.09)))
    frame(im); return im
h=hero(1600,560); h.save(OUT+'/hero/hero-desktop.png',optimize=True); h.convert('RGB').save(OUT+'/hero/hero-desktop.webp',quality=86)
m=hero(800,1000,True); m.save(OUT+'/hero/hero-mobile.png',optimize=True); m.convert('RGB').save(OUT+'/hero/hero-mobile.webp',quality=86)

# ---------- mockups (UI-1 style) ----------
def window(im,x,y,w,h,title,key):
    d=ImageDraw.Draw(im); d.rectangle([x,y,x+w,y+h],fill=DT+(240,),outline=GOLD,width=1)
    im.alpha_composite(ic(key,28),(x+10,y+9)); d.text((x+46,y+23),title,font=F(CIN,20),fill=GOLD,anchor='lm')
    d.line([x+8,y+44,x+w-8,y+44],fill=GOLD+(110,),width=1); return y+56
def card(im,x,y,w,label,line,sub=None):
    d=ImageDraw.Draw(im); hh=70 if sub else 50
    d.rectangle([x,y,x+w,y+hh],fill=TEAL+(255,),outline=GOLD+(120,)); d.rectangle([x,y,x+5,y+hh],fill=AMB)
    d.text((x+16,y+8),label,font=F(CIN,13),fill=GOLD); d.text((x+16,y+26),line,font=F(SERB,16),fill=CR)
    if sub: d.text((x+16,y+48),sub,font=F(SER,14),fill=LG)
    return y+hh+10
def lines(im,x,y,items,size=15,col=CR,gap=24,bullet=True):
    d=ImageDraw.Draw(im)
    for s in items:
        if bullet: d.ellipse([x,y+7,x+6,y+13],fill=AMB)
        d.text((x+(16 if bullet else 0),y),s,font=F(SER,size),fill=col); y+=gap
    return y
def bar(im,x,y,w,frac,label):
    d=ImageDraw.Draw(im); d.rectangle([x,y,x+w,y+12],fill=(4,30,35),outline=GOLD+(150,)); d.rectangle([x+1,y+1,x+1+int((w-2)*frac),y+11],fill=AMB)
    d.text((x,y+18),label,font=F(SER,13),fill=LG); return y+42
def stamp(im,caption,pos=None,sc=1.0,rot=18):
    w,h=im.size; s=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(s)
    t=Image.new('RGBA',(520,120),(0,0,0,0)); td=ImageDraw.Draw(t); td.rectangle([4,4,515,115],outline=AMB+(150,),width=5); td.text((260,62),'MOCKUP',font=F(CIN,72),fill=AMB+(120,),anchor='mm')
    if sc!=1.0: t=t.resize((int(t.width*sc),int(t.height*sc)),Image.LANCZOS)
    t=t.rotate(rot,expand=True,resample=Image.BICUBIC); im.alpha_composite(t,pos or (w-t.width-20,h-t.height-60))
    d=ImageDraw.Draw(im); d.rectangle([0,h-40,w,h],fill=(4,30,35,235)); d.line([0,h-40,w,h-40],fill=GOLD,width=1)
    d.text((16,h-20),'Mockup: '+caption,font=F(SER,15),fill=CR,anchor='lm'); d.text((w-16,h-20),'Not an in-game screenshot',font=F(SER,13),fill=LG,anchor='rm')
W,H=960,600
def scene(seed): 
    im=bg(W,H,seed); return im
def mk_core():
    im=scene(11); y=window(im,40,40,430,470,"Fennick's Beast Core",'BeastCore')
    d=ImageDraw.Draw(im); d.text((56,y),'Focus:  Auto',font=F(SERB,15),fill=LG); y+=30
    y=card(im,56,y,398,'GUIDANCE','Accept Wildmane Totem','Grull Hawkwind  (example step)')
    y=lines(im,56,y,['Rest: hearth is ready','Reputation: 2 turn-ins in your bags','Trailmarks: 3 finds nearby'],gap=26)
    y+=8; d.text((56,y),'Settings',font=F(CIN,15),fill=GOLD); y+=26
    lines(im,56,y,['Style: teal and gold / dark / minimal','Text size  ±N, follows your UI scale','Colour-blind colours for every module','Move frames: Edit Mode or /beast move'],size=14,gap=23)
    # arrow + tooltip
    ax,ay=640,150; d.polygon([(ax,ay-50),(ax+34,ay+30),(ax,ay+12),(ax-34,ay+30)],fill=AMB,outline=LG); d.text((ax,ay+58),'Waypoint arrow',font=F(SER,15),fill=CR,anchor='mm')
    tx,ty=520,270; d.rectangle([tx,ty,tx+400,ty+190],fill=(6,36,42,245),outline=GOLD)
    d.text((tx+14,ty+10),'Monster tooltip',font=F(CIN,16),fill=GOLD)
    lines(im,tx+14,ty+40,['Level range, elite / rare, health when known','Quests in your log or on your route','Quest-starting and notable drops','XP per kill and kills to level (with Guidepost)','Max 8 lines, quiet in combat by default'],size=14,gap=27)
    stamp(im,"Beast Core: one window, one arrow, shared tooltip",pos=(660,474),sc=0.45,rot=6); return im
def mk_guide():
    im=scene(12); y=window(im,40,40,560,480,"Fennick's Guidepost",'Guidepost')
    d=ImageDraw.Draw(im); d.text((56,y),'Mulgore  •  Hunter  •  Lv 6  •  XP/hr',font=F(SER,14),fill=LG); 
    d.rectangle([500,y-4,584,y+18],outline=GOLD,fill=TEAL); d.text((542,y+7),'HC',font=F(CIN,13),fill=GOLD,anchor='mm'); y+=32
    y=card(im,56,y,528,'NEXT','Accept Wildmane Totem from Grull Hawkwind','Mulgore (45, 78)')
    d.text((56,y),'Safe path: avoid the elite camp to the east (hover)',font=F(SER,14),fill=AMB); y+=30
    y=lines(im,56,y,['Kill 8 Plainstriders','Turn in at Bloodhoof Village','Train new spells at your class trainer','Profession hint (only professions you trained)'],gap=27)
    y=bar(im,56,y+6,528,0.42,'Route progress 42%')
    for i,b in enumerate(['Back','Skip']): d.rectangle([56+i*100,y,140+i*100,y+28],outline=GOLD,fill=TEAL); d.text((98+i*100,y+14),b,font=F(CIN,14),fill=GOLD,anchor='mm')
    rx=640; d.text((rx,70),'Rulesets',font=F(CIN,22),fill=GOLD)
    for i,(n,t) in enumerate([('PvE','Fastest route, optional shortcuts'),('HC','No death routing, safe transport'),('PvP','Contested zones as quick trips')]):
        yy=110+i*90; d.rectangle([rx,yy,rx+280,yy+72],fill=DT,outline=GOLD); d.rectangle([rx,yy,rx+5,yy+72],fill=AMB)
        d.text((rx+18,yy+12),n,font=F(CIN,18),fill=GOLD); d.text((rx+18,yy+42),t,font=F(SER,13),fill=CR)
    d.text((rx,374),'Every race and class, 1-60.',font=F(SER,15),fill=CR); d.text((rx,396),'No RXPGuides needed.',font=F(SER,15),fill=LG)
    stamp(im,"Guidepost: the next step, the route and the ruleset",pos=(632,428),sc=0.55,rot=10); return im
def mk_rest():
    im=scene(13); y=window(im,180,70,600,400,'Fennick Rest','Rest'); d=ImageDraw.Draw(im)
    y=bar(im,200,y+4,560,0.63,'Rested 63% of cap  •  full here in 3 d 4 h')
    y=card(im,200,y,560,'WHERE TO LOG OUT','Hearth to your inn and log out (no travel)','Hearthstone ready')
    y=lines(im,200,y+4,['Outside earns a quarter of inn rest per day','Cap includes Well Rested when measured','Cozy Sleeping Bag reminder when outside a rest area','Camp Tent line at a campfire when rested is low'],gap=28)
    stamp(im,'Rest: rested XP, time to full and where to log out',pos=(620,478),sc=0.42,rot=6); return im
def mk_rep():
    im=scene(14); y=window(im,180,60,600,420,'Fennick Reputation','Reputation'); d=ImageDraw.Draw(im)
    d.text((200,y),'Turn-ins you can do now (from your bags)',font=F(SER,15),fill=LG); y+=32
    for n,c,f in [('Timbermaw Hold','Deadwood Headdress Feather x5','Ready'),('Argent Dawn',"Minion's Scourgestone x20",'Ready'),('City cloth donation','Wool Cloth x60','Ready'),('Cenarion Circle','Encrypted Twilight Text x10','Ready')]:
        d.rectangle([200,y,760,y+60],fill=TEAL,outline=GOLD+(120,)); d.rectangle([200,y,205,y+60],fill=AMB if f=='Ready' else GOLD)
        d.text((218,y+10),n,font=F(CIN,16),fill=GOLD); d.text((218,y+34),c,font=F(SER,14),fill=CR); d.text((744,y+30),f,font=F(SERB,14),fill=AMB if f=='Ready' else LG,anchor='rm'); y+=70
    d.text((200,y+4),'Checks your side; Darkmoon Faire only in its week',font=F(SER,13),fill=LG)
    stamp(im,'Reputation: hand-ins already in your bags (example data)',pos=(640,486),sc=0.4,rot=6); return im
def mk_mf():
    im=scene(15); y=window(im,160,60,640,430,"Fennick Merchant's Favor",'MerchantsFavor'); d=ImageDraw.Draw(im)
    y=card(im,180,y,600,'READY TO TURN IN','Waylaid crate: deliver at the camp','Right-click in bags to start')
    d.text((180,y),"Craftsman's Writ",font=F(CIN,16),fill=GOLD); y+=28
    y=lines(im,180,y,['Item A   have 12 / need 20   (bags 12)','Item B   have 4 / need 4   done','Customer: name and map spot (unconfirmed)','Materials: buy or gather'],gap=27)
    y=bar(im,180,y+4,600,0.7,'Writ objectives 70%')
    d.text((180,y),'Delivered daily writ  •  daily reset in 5 h 12 m',font=F(SER,14),fill=LG)
    stamp(im,"Merchant's Favor: crates, writs and labels to turn-in",pos=(690,492),sc=0.38,rot=6); return im

# ---------- terrain with an explicit land/water mask (used by the QA checks) ----------
CLAIMS=[]   # every placed icon/route with its context claim; checked by check_scene()
class Scene:
    def __init__(s,name,ox,oy,w,h,land,water=(),seed=1):
        s.name,s.ox,s.oy,s.w,s.h=name,ox,oy,w,h
        m=Image.new('L',(w,h),0); md=ImageDraw.Draw(m)
        for poly in land: md.polygon(poly,fill=255)
        for poly in water: md.polygon(poly,fill=0)
        s.mask=m; s.towers=[]; s.piers=[]; s.fms=[]; s.items=[]
        t=Image.new('RGBA',(w,h),(36,70,96,255)); td=ImageDraw.Draw(t)   # water
        random.seed(seed); lnd=Image.new('RGBA',(w,h),(60,84,56,255)); ld=ImageDraw.Draw(lnd)
        for _ in range(40):
            cx,cy,r=random.randint(0,w),random.randint(0,h),random.randint(25,90); c=random.choice([(74,92,58),(96,84,60),(48,68,50),(64,90,64)])
            ld.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c+(255,))
        lnd=lnd.filter(ImageFilter.GaussianBlur(8)); t.paste(lnd,(0,0),m.filter(ImageFilter.GaussianBlur(1.5)))
        s.img=t
    def land(s,x,y): 
        x=min(max(int(x),0),s.w-1); y=min(max(int(y),0),s.h-1); return s.mask.getpixel((x,y))>127
    def ring(s,x,y,r): return [s.land(x+r*math.cos(a/8*math.pi*2),y+r*math.sin(a/8*math.pi*2)) for a in range(8)]+[s.land(x,y)]
    def seg(s,p,q,n=40): return [s.land(p[0]+(q[0]-p[0])*i/n,p[1]+(q[1]-p[1])*i/n) for i in range(n+1)]
def check_scene(sc):
    errs=[]
    for it in sc.items:
        k,need=it['kind'],it['terrain']; x,y=it.get('xy',(0,0))
        if need=='land' and not all(sc.ring(x,y,it.get('r',8))): errs.append(f"{sc.name}: {it['label']} must sit on land at {it['xy']}")
        if need=='water' and any(sc.ring(x,y,it.get('r',8))): errs.append(f"{sc.name}: {it['label']} must sit on water at {it['xy']}")
        if need=='coast':
            r=sc.ring(x,y,14)
            if all(r) or not any(r): errs.append(f"{sc.name}: pier {it['label']} must be on a coast")
        if need=='land-route' and not all(sc.seg(*it['pts'])): errs.append(f"{sc.name}: flight route {it['label']} leaves land")
        if need=='water-route':
            p,q=it['pts']; mid=sc.seg(p,q)[3:-3]
            if any(mid): errs.append(f"{sc.name}: ship route {it['label']} crosses land")
            if not (it['from'] in sc.piers and it['to'] in sc.piers): errs.append(f"{sc.name}: ship route {it['label']} must join two piers")
        if need=='tower-route' and not (it['from'] in sc.towers and it['to'] in sc.towers): errs.append(f"{sc.name}: zeppelin route {it['label']} must join two towers")
        if need=='flight-ends' and not (it['from'] in sc.fms and it['to'] in sc.fms): errs.append(f"{sc.name}: flight route {it['label']} must join two flight masters")
        if need=='air':   # zeppelin: at a tower or on a tower-tower route
            ok=any(math.dist((x,y),t)<6 for t in sc.towers) or any(abs(math.dist(r['pts'][0],(x,y))+math.dist((x,y),r['pts'][1])-math.dist(*r['pts']))<3 for r in sc.items if r['terrain']=='tower-route')
            if not ok: errs.append(f"{sc.name}: zeppelin {it['label']} not at a tower or on a tower route")
        if need=='ship':   # ship: on water and on a ship route, or at a pier
            onroute=any(abs(math.dist(r['pts'][0],(x,y))+math.dist((x,y),r['pts'][1])-math.dist(*r['pts']))<3 for r in sc.items if r['terrain']=='water-route')
            if any(sc.ring(x,y,6)) and not any(math.dist((x,y),p)<26 for p in sc.piers): errs.append(f"{sc.name}: ship {it['label']} not on water")
            if not onroute and not any(math.dist((x,y),p)<26 for p in sc.piers): errs.append(f"{sc.name}: ship {it['label']} not on a route or at a pier")
    return errs
def put(im,sc,icon,x,y,size,terrain,label,**kw):
    sc.items.append(dict(kind='icon',icon=icon,xy=(x,y),terrain=terrain,label=label,size=size,**kw))
    im.alpha_composite(pin(icon,size),(sc.ox+int(x-size/2),sc.oy+int(y-size/2)))
def route(im,sc,p,q,terrain,label,col,style,frm=None,to=None,width=3,curve=0):
    sc.items.append(dict(kind='route',pts=(p,q),terrain=terrain,label=label,**({'from':frm,'to':to} if frm else {})))
    d=ImageDraw.Draw(im); P=(sc.ox+p[0],sc.oy+p[1]); Q=(sc.ox+q[0],sc.oy+q[1]); n=int(math.dist(P,Q)/6)
    pts=[(P[0]+(Q[0]-P[0])*i/n,P[1]+(Q[1]-P[1])*i/n) for i in range(n+1)]
    for i in range(n):
        if style=='solid' or (style=='dash' and i%3!=2) or (style=='dot' and i%2==0): d.line([pts[i],pts[i+1]],fill=col,width=width)
def tower(im,sc,x,y,label):
    sc.towers.append((x,y)); sc.items.append(dict(kind='tower',xy=(x,y),terrain='land',label=label,r=6))
    d=ImageDraw.Draw(im); X,Y=sc.ox+x,sc.oy+y
    d.polygon([(X-7,Y+14),(X-3,Y-12),(X+3,Y-12),(X+7,Y+14)],fill=(70,52,40),outline=LG); d.rectangle([X-8,Y-16,X+8,Y-12],fill=GOLD)
def pier(im,sc,x,y,dx,dy,label):
    sc.piers.append((x,y)); sc.items.append(dict(kind='pier',xy=(x,y),terrain='coast',label=label))
    d=ImageDraw.Draw(im); X,Y=sc.ox+x,sc.oy+y; d.line([X-dx*0.6,Y-dy*0.6,X+dx*0.6,Y+dy*0.6],fill=(150,110,70),width=6)
def fm(sc,x,y): sc.fms.append((x,y))
SCENES=[]
def mk_tm():
    im=scene(16); d=ImageDraw.Draw(im)
    mx,my,mw,mh=40,40,560,480
    LAND=[[(0,0),(560,0),(560,480),(0,480)]]
    LAKE=[[(360,40),(470,30),(520,90),(500,170),(420,190),(350,140)]]
    sc=Scene('trailmarks',mx,my,mw,mh,LAND,LAKE,4); SCENES.append(sc); im.alpha_composite(sc.img,(mx,my)); d.rectangle([mx,my,mx+mw,my+mh],outline=GOLD)
    d.text((mx+12,my+10),'Example terrain (original art, not a game map)',font=F(SER,12),fill=CR)
    sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh); sd.ellipse([mx+110,my+220,mx+290,my+360],fill=AMB+(70,),outline=AMB+(160,)); im.alpha_composite(sh)
    sc.items.append(dict(kind='area',xy=(200,290),terrain='land',label='shaded area (6+ quest-target finds)',r=60))
    for icon,x,y,t,l in [('ore_copper',90,110,'land','Copper ore node'),('ore_tin',250,90,'land','Tin ore node'),('herb_peacebloom',150,420,'land','Peacebloom'),
        ('herb_silverleaf',320,410,'land','Silverleaf'),('herb_earthroot',470,330,'land','Earthroot'),('herb_stranglekelp',440,110,'water','Stranglekelp (grows in water)'),
        ('chest',60,300,'land','Treasure chest'),('quest',170,270,'land','Quest target'),('quest',230,320,'land','Quest target'),('quest',200,300,'land','Quest target'),('quest',150,300,'land','Quest target'),('quest',260,280,'land','Quest target'),('quest',190,335,'land','Quest target'),('user',520,420,'land','Quest giver (npc kind uses the user pin)')]:
        put(im,sc,icon,x,y,32,t,l)
    y=window(im,630,40,300,480,"Fennick's Trailmarks",'Trailmarks')
    for k,n in [('ore','Ore (13 kinds)'),('herb','Herbs (28 kinds)'),('chest','Treasure chests'),('quest','Quest targets'),('user','Quest givers')]:
        im.alpha_composite(pin(k,24),(646,y)); d.text((680,y+12),n,font=F(SER,14),fill=CR,anchor='lm'); d.rectangle([898,y+4,914,y+20],outline=GOLD,fill=AMB); y+=34
    y+=6; y=bar(im,646,y,268,0.6,'Area opacity')
    lines(im,646,y,['Shaded areas: 6+ finds','Pin size  •  per-type toggles','Share my finds (copy text)'],size=13,gap=24)
    stamp(im,'Trailmarks: finds on your world map and minimap',pos=(652,410),sc=0.5,rot=10); return im
def mk_cg():
    im=scene(17); d=ImageDraw.Draw(im)
    mx,my,mw,mh=40,40,600,480
    WEST=[[(0,0),(200,0),(235,110),(250,220),(220,330),(240,480),(0,480)]]
    EAST=[[(600,0),(400,0),(372,150),(392,260),(362,360),(380,480),(600,480)]]
    sc=Scene('cartographer',mx,my,mw,mh,WEST+EAST,(),9); SCENES.append(sc); im.alpha_composite(sc.img,(mx,my))
    # flight masters (west), towers (both shores inland), piers (coast)
    fm(sc,80,130); fm(sc,140,400); fm(sc,500,300); fm(sc,520,420)
    tower(im,sc,150,90,'West zeppelin tower'); tower(im,sc,470,110,'East zeppelin tower')
    pier(im,sc,246,250,24,0,'West pier'); pier(im,sc,368,320,-24,0,'East pier')
    route(im,sc,(80,130),(140,400),'land-route','West flight path',AMB,'solid',frm=(80,130),to=(140,400))
    route(im,sc,(500,300),(520,420),'land-route','East flight path',AMB,'solid',frm=(500,300),to=(520,420))
    sc.items[-1]['terrain']='land-route'
    for it in [dict(kind='route',pts=((80,130),(140,400)),terrain='flight-ends',label='West flight path ends',**{'from':(80,130),'to':(140,400)}),dict(kind='route',pts=((500,300),(520,420)),terrain='flight-ends',label='East flight path ends',**{'from':(500,300),'to':(520,420)})]: sc.items.append(it)
    route(im,sc,(258,252),(356,318),'water-route','Ship route',(200,230,240),'dash',frm=(246,250),to=(368,320))
    sc.items[-1]['pts']=((246,250),(368,320))
    route(im,sc,(150,78),(470,98),'tower-route','Zeppelin route',LG,'dot',frm=(150,90),to=(470,110),width=2)
    sc.items[-1]['pts']=((150,90),(470,110))
    for x,y in sc.fms: put(im,sc,'flight',x,y,30,'land','Flight master')
    put(im,sc,'ship',307,285,34,'ship','Ship on its route')
    put(im,sc,'zeppelin',310,100,34,'air','Zeppelin in the air on its route')
    put(im,sc,'user',110,260,30,'land','Your pin')
    d.rectangle([mx,my,mx+mw,my+40],fill=DT+(235,)); d.rectangle([mx,my,mx+mw,my+mh],outline=GOLD,width=1)
    im.alpha_composite(ic('Cartographer',28),(mx+8,my+6)); d.text((mx+44,my+20),"Fennick's Cartographer",font=F(CIN,18),fill=GOLD,anchor='lm')
    for i,s_ in enumerate(['+','−']): d.rectangle([mx+mw-80+i*36,my+6,mx+mw-52+i*36,my+34],outline=GOLD,fill=TEAL); d.text((mx+mw-66+i*36,my+20),s_,font=F(SERB,18),fill=GOLD,anchor='mm')
    d.text((mx+12,my+mh-16),'Example terrain (original art, not a game map)',font=F(SER,12),fill=CR,anchor='lm')
    y=window(im,660,40,270,480,'Trip planner','Cartographer'); y=card(im,672,y,246,'HOW DO I GET THERE?','Shift-click a spot','known flights, boats, walk')
    lg=[(AMB,'solid','Flight path'),((200,230,240),'dash','Ship'),(LG,'dot','Zeppelin')]
    for c,st,n in lg:
        for i in range(6):
            if st=='solid' or (st=='dash' and i%3!=2) or (st=='dot' and i%2==0): d.line([672+i*6,y+9,678+i*6,y+9],fill=c,width=3)
        d.text((716,y+9),n,font=F(SER,14),fill=CR,anchor='lm'); y+=24
    y=lines(im,672,y+4,['Minutes for each leg','Icon filters per map','Your pins, any icon','Square minimap, 16 px pins'],size=14,gap=26)
    stamp(im,'Cartographer: world map, routes and trip planner',pos=(676,400),sc=0.48,rot=10); return im
MK={'beast-core':mk_core,'guidepost':mk_guide,'rest':mk_rest,'reputation':mk_rep,'merchants-favor':mk_mf,'trailmarks':mk_tm,'cartographer':mk_cg}
for k,f in MK.items():
    im=f(); im.save(f'{OUT}/mockups/{k}.png',optimize=True); im.convert('RGB').save(f'{OUT}/mockups/{k}.webp',quality=85)

# ---------- og images ----------
def og(title,sub,key=None,path='site'):
    im=bg(1200,630,21); d=ImageDraw.Draw(im)
    big=ic(key,300) if key else FOX.resize((340,340),Image.LANCZOS); glow(im,big,(70,(630-big.height)//2),26)
    x=430 if key else 460
    fs=64
    while F(CIN,fs).getlength(title)>1200-x-50: fs-=2
    d.text((x,240),title,font=F(CIN,fs),fill=GOLD,anchor='lm'); d.line([x,290,1150,290],fill=AMB,width=3)
    yy=330
    for ln in sub: d.text((x,yy),ln,font=F(SER,30),fill=CR,anchor='lm'); yy+=44
    d.text((x,560),'fennickaddons.dev  •  free for WoW Forever',font=F(SER,24),fill=LG,anchor='lm')
    if key: im.alpha_composite(FOX.resize((64,64),Image.LANCZOS),(1110,540))
    frame(im); im.convert('RGB').save(f'{OUT}/og/{path}.png',optimize=True)
og("FENNICK'S ADDONS",['Free add-ons for WoW Forever:','a 1-60 leveling guide and helpers','for rest, rep, maps and more.'])
SUBS={'beast-core':['One window, one waypoint arrow,','shared settings and a smart','monster tooltip.'],
'guidepost':['A stand-alone 1-60 leveling guide','for every race and class, with','PvE, Hardcore and PvP rulesets.'],
'rest':['Your rested XP, time until full,','and the best friendly place','to log out.'],
'reputation':['The reputation turn-ins you can','hand in right now with what is','already in your bags.'],
'merchants-favor':['Tracks Merchant\'s Favor crates,','writs and labels in your bags','from start to turn-in.'],
'trailmarks':['Remembers where you found ore,','herbs, chests and quest targets,','and pins them on your maps.'],
'cartographer':['A world map and square minimap','with travel routes, icon filters','and a "how do I get there?" planner.']}
for k,t,s in ADD: og(t.upper() if len(t)<26 else t.upper(),SUBS[s],k,s)
errs=[e for sc in SCENES for e in check_scene(sc)]
import json
json.dump({sc.name:sc.items for sc in SCENES},open(os.environ.get('ART_PLACEMENTS','/workspace/fennick-site-work/tools/scene_placements.json'),'w'),indent=1,default=list)
if errs: print('\n'.join(errs)); raise SystemExit('ART QA FAILED')
print('scene checks passed:',sum(len(sc.items) for sc in SCENES),'placements'); print('done')
