import re
_F=open('extracted/heritgfood-results-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
_OLD=open('work/a1-results/body.txt',encoding='utf-8').read().split('\n')
_pgstart={}
for i,l in enumerate(_F):
    m=re.match(r'^\[page (\d+)\]$',l)
    if m:_pgstart[int(m.group(1))]=i+1
def _pgrange(pg):
    a=_pgstart[pg]; b=_pgstart.get(pg+1,len(_F)+1)-1
    return a,b
_MISS=[]
def resolve(pg,ln,val,ctx):
    a,b=_pgrange(pg)
    if ln==0: return a
    old=_OLD[ln-17] if 0<=ln-17<len(_OLD) else ''   # old fulltext line = body line+16 header
    OV={'001076N':'Firm Registration','CIN L15209':'CIN: L15209','Flavoured milk':'flavoured milk','Feed segment':'c. Feed','30.09.2026, 30.06':'COLUMNS:','30 September 2026; 31':'Statement of','(Unaudited)/(Audited)':'COLUMNS:','(Unaudited) 30 Sep':'COLUMNS:','asterisk marker':'*Basic and Diluted','Note 2:':'have been prepared in accordance','Note 4a':'4. a.','Note 1: consolidated':'1. The consolidated','Pages 2-6':'[page 2]'}
    for k,v in OV.items():
        if str(val).startswith(k) or ctx.startswith(k):
            if k=='Note 2:' and False: pass
            for i in range(a,b+1):
                if v.lower() in _F[i-1].lower(): return i
    cands=[old.strip()[:28],str(val).strip()[:22],ctx.strip()[:18]]
    for c in cands:
        if len(c)>=6:
            for i in range(a,b+1):
                if c.lower() in _F[i-1].lower(): return i
    _MISS.append((pg,ln,val[:40])); return a
NUMROWS=[]
_n=0
def _addnum(pg,ln,v,ctx,flag):
    NUMROWS.append(('NUMBER','R%03d | page %d | line %d | NUMBER | %s | %s%s'%(len(NUMROWS)+1,pg,ln,v,ctx,(' | '+flag) if flag else '')))
CT={2:('standalone P&L',['Q 30.09.2026','Q 30.06.2026','Q 30.09.2025','6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']),
3:('standalone segment',None),4:('standalone balance sheet',['30.09.2026','31.03.2026']),5:('standalone cash flow',['6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']),
9:('consolidated P&L',None),10:('consolidated segment',None),11:('consolidated balance sheet',['30.09.2026','31.03.2026']),12:('consolidated cash flow',['6M 30.09.2026','6M 30.09.2025','FY 31.03.2026'])}
P6=['Q 30.09.2026','Q 30.06.2026','Q 30.09.2025','6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']
for pg,(nm,cols) in CT.items():
    cols=cols or P6
    nc=len(cols); a,b=_pgrange(pg)
    st=[i for i in range(a,b+1) if _F[i-1].startswith('COLUMNS:')][0]
    en=[i for i in range(st+2,b+1) if _F[i-1]==''][0]
    for i in range(st+1,en):
        l=_F[i-1]
        if len(l)<96+15 : continue
        label=l[:96].strip()
        fields=[l[96+15*k:96+15*(k+1)].strip() for k in range(nc)]
        if not label.startswith(('')): pass
        for k,v in enumerate(fields):
            if v=='': continue
            _addnum(pg,i,v,'%s: %s, %s'%(nm,label[:70],cols[k]),'ZERO_STANDING' if v=='-' else '')
