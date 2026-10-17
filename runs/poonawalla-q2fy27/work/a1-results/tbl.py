import re,json
L=open('body.txt',encoding='utf-8').read().split('\n')
def toks(line):
    out=[];
    for m in re.finditer(r'\S+(?: \S+)*',line):
        pass
    # split on 2+ spaces keeping positions
    res=[];pos=0
    for m in re.finditer(r'(?:(?<=\s{2})|^)\S.*?(?=\s{2,}|$)',line):
        res.append((m.start(),m.end(),m.group()))
    return res
valre=re.compile(r'^[\(\-\d IlJO,\.\)/?\'~]+$')
def parse(ln,refs):
    line='  '+L[ln-1]; t=toks(line); vals=[]; 
    # take trailing value tokens
    i=len(t)-1
    while i>=0 and valre.match(t[i][2]) and (re.search(r'\d|^-$',t[i][2]) or t[i][2].strip()=='-'):
        vals.insert(0,t[i]); i-=1
    label=' '.join(x[2] for x in t[:i+1])
    return label,vals
def assign(vals,refs):
    out={}
    for s,e,v in vals:
        j=min(range(len(refs)),key=lambda k:abs(refs[k]-e))
        out.setdefault(j,[]).append(v)
    return out
specs=[('PL-C',7,274,326,'Total income',6),('PL-S',13,626,668,'Total income',6),
 ('BS-C',8,342,387,'Total Assets',2),('BS-S',14,695,745,'Total Assets',2),
 ('CF-C',9,402,449,'Profit before tax',2),('CF-S',15,760,808,'Profit before tax',2)]
res=[]
for name,pg,a,b,refkey,n in specs:
    # ref line: find line containing refkey in range
    ref=None
    for ln in range(a,b+1):
        if refkey in L[ln-1]:
            ref=ln;break
    _,rv=parse(ref,None)
    refs=[e for s,e,v in rv]
    print(name,'ref line',ref,'refs',refs)
    for ln in range(a,b+1):
        label,vals=parse(ln,refs)
        if not vals: continue
        asg=assign(vals,refs)
        flag=''
        if len(vals)!=len(asg) or any(len(x)>1 for x in asg.values()): flag='ALIGN?'
        res.append(dict(t=name,pg=pg,ln=ln,label=label,cols={k:v[0] for k,v in asg.items()},nv=len(vals),flag=flag))
json.dump(res,open('tbl.json','w'))
for r in res:
    if r['flag'] or (r['nv']!=len(set(r['cols']))): print('MISMATCH',r)
print(len(res))
# print rows w/ fewer than expected
for r in res:
    n=6 if r['t'].startswith('PL') else 2
    if len(r['cols'])!=n: print('SHORT',r['t'],r['ln'],r['label'][:40],sorted(r['cols'].items()))
