import re
S='extracted/paracables-presentation-q2fy27-structured.md'
FT=open('extracted/paracables-presentation-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
lines={l:FT[l-1].replace(' bps','bps').split() for l in range(416,430)}
cols=["Q2 FY27","Q1 FY27","QoQ","Q2 FY26","YoY","H1 FY27","H1 FY26","H1 YoY"]
img=[("revenue from operations",["560.4","529.4","5.9%","427.6","31.1%","1089.8","878.5","24.1%"]),
("other income",["3.8","3.1","23.0%","19.9","(81)%","6.9","37.9","(81.8)%"]),
("total income",["564.2","532.5","6.0%","447.5","26.1%","1096.7","916.4","19.7%"]),
("operating profit",["40.9","34.7","17.8%","5.7","616.5%","75.6","20.9","262.5%"]),
("operating margin %",["7.3%","6.6%","70bps","1.3%","600bps","6.9%","2.4%","450bps"]),
("EBITDA (incl. OI)",["44.7","37.8","18.2%","25.6","74.2%","82.5","58.8","40.3%"]),
("EBITDA margin %",["7.9%","7.1%","80bps","5.7%","220bps","7.5%","6.4%","110bps"]),
("depreciation",["4.4","4.4","0.0%","3.8","15.7%","8.8","7.4","20.4%"]),
("finance cost",["7.9","6.9","15.0%","4.0","96.8%","14.8","7.9","85.3%"]),
("PBT",["32.4","26.5","22.0%","17.8","81.8%","58.9","43.5","35.5%"]),
("PAT",["24.2","19.7","23.0%","13.3","82.8%","43.9","32.3","36.2%"]),
("EPS (Rs.)",["0.74","0.64","15.6%","0.44","68.2%","1.38","1.06","30.2%"])]
used=set();loc={}
for nm,vals in img:
    for c,v in zip(cols,vals):
        vv=v.replace(' bps','bps')
        for l in sorted(lines):
            for k,t in enumerate(lines[l]):
                if t==vv and (l,k) not in used:
                    used.add((l,k));loc[(nm,c)]=l;break
            else: continue
            break
        else: loc[(nm,c)]=None
miss=[k for k,v in loc.items() if v is None];print("missing",miss)
bs={"equity share capital":(447,447),"other equity":(448,448),"total shareholders' funds":(449,449),"long-term borrowings":(450,450),"lease+provisions+DTL":(451,451),"total non-current liabilities":(452,452),"short-term borrowings":(453,453),"trade payables":(454,454),"other current liabilities":(455,455),"total current liabilities":(456,456),"total equity & liabilities":(458,458),"PPE":(447,448),"CWIP":(448,450),"ROU + other non-current assets":(449,451),"total non-current assets":(450,452),"investments":(451,453),"inventories":(452,454),"trade receivables":(453,455),"cash & bank balances":(454,456),"other current assets":(455,457),"total current assets":(456,458),"total assets":(457,459)}
out=[]
for ln in open(S,encoding='utf-8').read().split('\n'):
    m=re.match(r'(R\d+) \| page (28|30) \| line (\d+) \| (\w+) \| (.*) \| (.*)$',ln)
    if m:
        rid,pg,l,ty,val,ctx=m.groups()
        if pg=='28':
            mm=re.match(r'income statement (.*), (Q2 FY27|Q1 FY27|QoQ|Q2 FY26|YoY|H1 FY27|H1 FY26|H1 YoY)$',ctx)
            if mm:
                nm,c=mm.groups(); v=val.split(' [')[0]
                img_v=dict(img)[nm][cols.index(c)]
                fl="LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC"
                if nm in("depreciation","finance cost") and c in("Q2 FY26","H1 FY26"): fl="CORRECTED_FROM_IMAGE"
                ln=f"{rid} | page 28 | line {loc[(nm,c)]} | NUMBER | {img_v} [{fl}] | {ctx}"
            elif 'near depreciation' in ctx: ln=f"{rid} | page 28 | line {loc[('depreciation','YoY')]} | NUMBER | 15.7% [CORRECTED_FROM_IMAGE] | income statement depreciation, YoY (Q2 FY27 vs Q2 FY26)"
            elif 'near finance' in ctx: ln=f"{rid} | page 28 | line {loc[('finance cost','YoY')]} | NUMBER | 96.8% [CORRECTED_FROM_IMAGE] | income statement finance cost, YoY (Q2 FY27 vs Q2 FY26)"
            elif 'stray' in ctx: ln=f"{rid} | page 28 | line {loc[('EPS (Rs.)','YoY')]} | NUMBER | 68.2% | duplicate stray capture of EPS YoY, Q2 FY27 vs Q2 FY26 (see EPS row)"
        else:
            mm=re.match(r'balance sheet (.*), (H1 FY27|FY26)$',ctx)
            if mm:
                nm,per=mm.groups(); a,b=bs[nm]
                ln=f"{rid} | page 30 | line {b if per=='FY26' else a} | {ty} | {val} | {ctx}"
            elif 'unassigned' in ctx or 'row unassigned' in ctx:
                v=val.split(' [')[0]; nm={'285':('inventories',454),'413':('trade receivables',455),'33':('cash & bank balances',456),'81':('other current assets',457)}[v]
                ln=f"{rid} | page 30 | line {nm[1]} | NUMBER | {v} [LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC] | balance sheet {nm[0]}, FY26"
    out.append(ln)
txt='\n'.join(out).rstrip('\n')
last=int(re.findall(r'^R(\d+) ',txt,re.M)[-1]);assert last==522
add=[("page 28","NUMBER",f"{loc[('depreciation','H1 YoY')]}","20.4% [CORRECTED_FROM_IMAGE]","income statement depreciation, H1 YoY (H1 FY27 vs H1 FY26)"),
("page 28","NUMBER",f"{loc[('finance cost','H1 YoY')]}","85.3% [CORRECTED_FROM_IMAGE]","income statement finance cost, H1 YoY (H1 FY27 vs H1 FY26)"),
("page 30","NUMBER","453","- [ZERO_STANDING LAYOUT_SCRAMBLED]","balance sheet investments, FY26 (second dash cell; first is CWIP FY26 at L450)")]
extra="\n\n## ADDENDUM rows (A3 follow-up fixes)\n"
for k,(p,t,l,v,c) in enumerate(add):
    extra+=f"R{523+k} | {p} | line {l} | {t} | {v} | {c}\n"
extra+="""
## CORRECTIONS LOG (A1, follow-up)
- Slide 28 and 30 line cites re-checked against fulltext; value lines corrected (rows keep IDs).
- Slide 28 image check (page 28 rendered at 150 dpi, PNG deleted): depreciation Q2 FY26 = 3.8 and H1 FY26 = 7.4; finance cost Q2 FY26 = 4.0 and H1 FY26 = 7.9. Earlier rows had these swapped; corrected, flagged CORRECTED_FROM_IMAGE. Stray values 15.7%, 96.8%, 20.4%, 85.3% are the YoY cells of depreciation and finance cost.
- Slide 30: FY26 asset-column values re-mapped by row order: investments FY26 dash (L453), inventories 285, trade receivables 413, cash 33, other current assets 81. CWIP FY26 dash at L450 (R371 corrected).
- Fulltext not edited (header unchanged).
"""
txt=re.sub(r'ID range: R001-R522','ID range: R001-R525',txt)
txt=re.sub(r'NUMBER 404','NUMBER 407',txt)
txt=re.sub(r'(note: tables.*)',r'\1',txt)
open(S,'w',encoding='utf-8').write(txt+extra)
