rows=[]
for ln in open('work/a1-presentation-scratch/spec1.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln: continue
    f=ln.split('|')
    if f[0]=='T':
        _,p,l,ctx,per,val=f[:6]
        for a,b in zip(per.split(';'),val.split(';')):
            fl=' ZERO_STANDING' if b in('0.00',) else ''
            rows.append((int(p),int(l),'NUMBER',b+fl,f'{ctx}, {a}'))
    elif f[0]=='O':
        _,p,l,n,val,cust,prod,ex=f[:8]
        rows.append((int(p),int(l),'NUMBER',val,f'H1 FY27 order {n} value'))
        rows.append((int(p),int(l),'NUMBER',ex,f'H1 FY27 order {n} execution period'))
        rows.append((int(p),int(l),'ENTITY',cust,f'H1 FY27 order {n} customer'))
        rows.append((int(p),int(l),'ENTITY',prod,f'H1 FY27 order {n} product'))
    else:
        p,l,t=f[0],f[1],f[2]
        rest=f[3:]
        v=rest[0]; c=rest[-1] if len(rest)>1 else ''
        rows.append((int(p),int(l),t,v,c))
order=['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']
def key(t): return 1 if t=='ENTITY-SUMMARY' else order.index(t)
groups={}
for i,r in enumerate(rows):
    t='ENTITY' if r[2]=='ENTITY-SUMMARY' else r[2]
    groups.setdefault(t,[]).append((r[0],i,r))
out=[];n=0;ranges={};counts={}
for t in order:
    g=sorted(groups.get(t,[]),key=lambda x:(x[0],x[1]))
    counts[t]=len(g)
    start=n+1
    out.append(f'\n## {t} TABLE\n')
    for _,_,(p,l,ty,v,c) in g:
        n+=1
        out.append(f'R{n:03d} | page {p} | line {l} | {ty} | {v} | {c}')
    ranges[t]=f'R{start:03d}-R{n:03d}'
hdr=f'''=== A1 STRUCTURED EXTRACTION ===
source: SupremePower_H1FY27_Presentation.pdf (doctype presentation, H1 FY27, 41 pages)
fulltext: runs/supremepwr-h1fy27/extracted/supremepwr-presentation-h1fy27-fulltext.md (line numbers refer to that file)
ID range: R001-R{n:03d}  (total rows {n})
counts: NUMBER {counts['NUMBER']} ({ranges['NUMBER']}) | ENTITY {counts['ENTITY']} incl. ENTITY-SUMMARY ({ranges['ENTITY']}) | FORWARD {counts['FORWARD']} ({ranges['FORWARD']}) | DATE {counts['DATE']} ({ranges['DATE']}) | QUALIFIER {counts['QUALIFIER']} ({ranges['QUALIFIER']})
unit: Rs Crores (x1); page N = PDF page N; slide number printed = page minus 1
row format: R### | page N | line L | TYPE | verbatim value | short context
notes: tables anchored to RAW-ORDER SUPPLEMENT lines (aligned) where layout columns interleave; multi-period cells split one row per period; ZERO_STANDING flag on 0.00 values; slide-number footers captured as NUMBER rows; chart rows with unresolved series mapping are flagged in QUALIFIER rows on their page
=== END HEADER ===
'''
open('extracted/supremepwr-presentation-h1fy27-structured.md','w',encoding='utf-8').write(hdr+'\n'.join(out)+'\n')
print(n,counts,ranges)
