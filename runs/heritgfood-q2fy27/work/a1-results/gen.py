import re,sys
L=open('extracted/heritgfood-results-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
PL=['Q 30.09.2026','Q 30.06.2026','Q 30.09.2025','6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']
BS=['30.09.2026','31.03.2026']
CF=['6M 30.09.2026','6M 30.09.2025','FY 31.03.2026']
specs=[ (2,'standalone P&L',77,115,PL),(3,'standalone segment',136,164,PL),(4,'standalone balance sheet',183,237,BS),
(5,'standalone cash flow',259,319,CF),(9,'consolidated P&L',473,521,PL),(10,'consolidated segment',547,581,PL),
(11,'consolidated balance sheet',600,654,BS),(12,'consolidated cash flow',679,742,CF)]
# overrides: line -> list of col idx for the value tokens
ov={95:[2,4,5],87:[0,1,2,3,4],89:[5],90:[5],491:[4,5],493:[2,4,5],487:[5],
 262:[2] ,516:[], 562:[4,5],503:[4],}
def isval(t):
    return (len(re.findall('[A-Za-z]',t))<=2 and (re.search(r'\d',t) or t.strip() in '-–')) and len(t)<=18
rows=[];n=0
def add(pg,ln,typ,val,ctx,flag=''):
    global n; n+=1
    rows.append((typ,'R%03d | page %d | line %d | %s | %s | %s%s'%(n,pg,ln,typ,val,ctx,(' | '+flag) if flag else '')))
for pg,name,a,b,cols in specs:
    for ln in range(a,b+1):
        s=L[ln-1]
        if not s.strip(): continue
        toks=re.split(r'\s{2,}',s.strip())
        vals=[]
        while toks and isval(toks[-1]): vals.insert(0,toks.pop())
        if not vals: continue
        label=' '.join(toks) if toks else '(value-only continuation line)'
        label=re.sub(r'^\S{1,3}\s+(?=[A-Za-z(])','',label) if len(toks)>0 and re.match(r'^\d{1,2}\s',label) else label
        idx=ov.get(ln)
        if idx is None:
            idx=list(range(len(cols))) if len(vals)==len(cols) else None
        for i,v in enumerate(vals):
            if idx is not None and i<len(idx):
                col=cols[idx[i]]; fl=''
            else:
                col='column UNMAPPED (value %d of %d on line)'%(i+1,len(vals)); fl='COLUMN_MISMATCH'
            if re.search(r'[^\d\.,\-\(\)\s]',v): fl=(fl+' ' if fl else '')+'OCR_NOISE'
            if v.strip() in ('-','–'): fl=(fl+' ' if fl else '')+'ZERO_STANDING'
            add(pg,ln,'NUMBER',v,'%s: %s, %s'%(name,label[:70],col),fl)
import json
json.dump(rows,open('work/a1-results/numrows.json','w'))
print(n)
