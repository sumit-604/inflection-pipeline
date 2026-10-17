import re,sys,json
sys.path.insert(0,'work/a1-results')
from pages import PAGES
def num(s):
    s=s.strip()
    if s in ('','-'): return 0.0
    neg=s.startswith('(') or s.startswith('-')
    v=float(re.sub(r'[^\d.]','',s))
    return -v if neg else v
# ---- tie-out
res=[]
def tie(name,pg,idx):
    rows={}
    for lab,v in PAGES[pg][4]: rows.setdefault(lab,[]).append(v)
    rl=PAGES[pg][4]
    def g(i): return rl[i][1]
    return rl
ties=[]
for pg,name in ((2,'standalone'),(9,'consolidated')):
    rl=PAGES[pg][4]
    byl={}
    for i,(l,v) in enumerate(rl): byl[l]=v
    labs=[l for l,_ in rl]
    def row(prefix,nth=0):
        c=[l for l in labs if l.startswith(prefix)]
        return byl[c[nth]]
    cols=['Q 30.09.2026','Q 30.06.2026','Q 30.09.2025','6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']
    for c in range(6):
        rev=num(row('a. Revenue')[c]); oth=num(row('b. Other income')[c]); ti=num(row('Total income')[c])
        exp=sum(num(row(p)[c]) for p in ['a. Cost','b. Purchases','c. Changes','d. Employee','e. Finance','f. Depreciation','g. Impairment','h. Other expenses'])
        te=num(row('Total expenses')[c])
        if pg==2:
            pbei=num(row('3 Profit before exceptional')[c]); exc=num(row('4 Exceptional')[c]); pbt=num(row('5 Profit before tax')[c])
            tax=num(row('a. Current tax')[c])+num(row('b. Deferred tax')[c]); pat=num(row('7 Profit for')[c])
            chk=[('TI=rev+oth',rev+oth,ti),('TE=sum',exp,te),('PBEI=TI-TE',ti-te,pbei),('PBT=PBEI+exc',pbei+exc,pbt),('PAT=PBT-tax',pbt-tax,pat)]
        else:
            p3=num(row('3 Profit before share')[c]); sh=num(row('4 Share')[c]); p5=num(row('5 Profit before tax')[c]); exc=num(row('6 Exceptional')[c]); p7=num(row('7 Profit before tax')[c])
            tax=num(row('a. Current tax')[c])+num(row('b. Deferred tax')[c]); pat=num(row('9 Profit for')[c])
            chk=[('TI=rev+oth',rev+oth,ti),('TE=sum',exp,te),('P3=TI-TE',ti-te,p3),('PBT5=P3+share',p3+sh,p5),('PBT7=PBT5+exc',p5+exc,p7),('PAT=PBT-tax',p7-tax,pat)]
        for nm,calc,rep in chk:
            ok=abs(calc-rep)<=0.0151
            ties.append((name,cols[c],nm,round(calc,2),rep,ok))
bad=[t for t in ties if not t[5]]
print('tie checks',len(ties),'fail',len(bad))
for t in bad: print('FAIL',t)
json.dump(ties,open('work/a1-results/ties.json','w'))
# cash flow / balance checks
for pg in (4,11):
    rl={l:v for l,v in PAGES[pg][4]}
    print('BS',pg,rl['Total assets'],rl['Total equity and liabilities'])
# ---- build fulltext
body=open('work/a1-results/body.txt',encoding='utf-8').read().split('\n')
pg_txt={}
cur=None
for l in body:
    m=re.match(r'^\[page (\d+)\]$',l)
    if m: cur=int(m.group(1)); pg_txt[cur]=[]; continue
    if cur: pg_txt[cur].append(l)
FOOT=["HERITAGE FOODS LIMITED","CIN: L15209TG1992PLC014332    FSMS 002","AN ISO: 22000 CERTIFIED COMPANY",
"Regd. Off: H.No. 8-2-293/82/A/1286, Plot No. 1286, Road No. 1 & 65, Jubilee Hills, Hyderabad - 500033, Telangana, INDIA.",
"Tel.: +91-40-23391221, 23391222, Fax: 23326789, 23318090 Email: hfl@heritagefoods.in, Website: www.heritagefoods.in"]
def fmt(pg):
    t1,unit,colhdr,nc,rows=PAGES[pg]
    out=[]
    if pg in (2,9):
        out+=["HERITAGE FOODS LIMITED","Registered & Corporate Office: # H. No.8-2-293/82/A/1286 Plot No: 1286, Road No. 1 & 65, Jubilee Hills, Hyderabad- 500033 Telangana, India",
        "CIN: L15209TG1992PLC014332, website: www.heritagefoods.in, Tel.No: 040-23391221/23391222, Fax: 23318090, email: hfl@heritagefoods.in"]
    out+=t1.split(' / ')+[unit,'COLUMNS: '+colhdr,'']
    for lab,v in rows:
        if v and any(x.strip() for x in v):
            out.append('%-96s'%lab[:96]+''.join('%15s'%x for x in v))
        else: out.append(lab)
    out.append('')
    return out+FOOT
def notes(pg):
    o=open('work/a1-results/%s.txt'%{6:'pg6-06',13:'pg13-13'}[pg],encoding='utf-8').read().split('\n')
    s=[i for i,l in enumerate(o) if l.strip()=='Notes:'][0]
    e=[i for i,l in enumerate(o) if 'DIN: 00003741' in l][0]
    t=[re.sub(r'%(?=\d)','Rs ',l) for l in o[s:e+1]]
    t=[l.replace('2U13','2013').replace('2U15','2015').replace('Committce','Committee').replace('uaudited','unaudited').replace('1/25)','2025)').replace('gencrally','generally').replace('acceptc!','accepted').replace('recogustion','recognition').replace('Ru juitements','Requirements').replace('secon 133','section 133').replace('becn','been').replace('accepted in','accepted in') for l in t]
    t=[l for l in t if l.strip()]
    return t+FOOT[:0]+['']+FOOT
hdr=open('work/a1-results/hdr.txt',encoding='utf-8').read().rstrip('\n').split('\n')
out=[]
for p in range(1,17):
    out.append('[page %d]'%p)
    if p in PAGES: out+=fmt(p)
    elif p in (6,13): out+=notes(p)
    else: out+=pg_txt[p]
total=len(hdr)+len(out)
hdr=[h.replace('LINECOUNT',str(total)) for h in hdr]
open('extracted/heritgfood-results-q2fy27-fulltext.md','w',encoding='utf-8').write('\n'.join(hdr+out)+'\n')
print('lines',total)
