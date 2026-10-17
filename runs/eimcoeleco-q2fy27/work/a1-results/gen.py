import re,sys
L=open('extracted/eimcoeleco-results-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
tok=re.compile(r'\(?-?[\dS][\d,S]*(?:\s?\.\s?[\dS]+)?\)?')
def nums(s):
    s=re.sub(r'(\d)\s+\.(\d)',r'\1.\2',s)
    return re.findall(r'\(?[\d][\dS,]*\.[\dS]+\)?|\(?\d[\d,]*\)?',s)
def split_label(line):
    # label = text up to first numeric token that is followed only by numerics
    m=re.search(r'(?:\s)(\(?[\d][\dS,]*(?:\s?\.\s?[\dS]+)?\)?(?:\s+\(?[\d][\dS,]*(?:\s?\.\s?[\dS]+)?\)?)*)\s*$',line)
    return m
specs=[ # (first,last,page,cols)
 (153,186,4,['Q 30.09.26','Q 30.06.26','Q 30.09.25','H1 30.09.26','H1 30.09.25','FY 31.03.26']),
 (204,265,5,['30.09.26','31.03.26']),
 (273,326,6,['H1 30.09.26','FY 31.03.26','H1 30.09.25']),
]
out=[];skipped=[]
for a,b,pg,cols in specs:
    for ln in range(a,b+1):
        line=L[ln-1]
        m=re.search(r'\s((?:\(?\d[\d,S]*(?:\s?\.\s?[\dS]+)?\)?)(?:\s+\(?\d[\d,S]*(?:\s?\.\s?[\dS]+)?\)?)*)\s*$',line)
        if not m: continue
        label=line[:m.start()].strip()
        vals=re.findall(r'\(?\d[\d,S]*(?:\s?\.\s?[\dS]+)?\)?',m.group(1))
        vals=[re.sub(r'\s','',v) for v in vals]
        if len(vals)>len(cols) or not re.search(r'[A-Za-z]',label) or len(vals)<2 and False:
            skipped.append((ln,line.strip()));continue
        out.append((ln,pg,label,vals,cols))
import json
json.dump(out,open('work/a1-results/auto.json','w'))
for ln,pg,l,v,c in out:
    if len(v)!=len(c): print('PARTIAL',ln,l,v)
print('---skipped');[print(s) for s in skipped]
