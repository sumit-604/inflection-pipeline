import re,sys,json
rows=[]
for l in open('runs/supremepwr-h1fy27/extracted/supremepwr-results-h1fy27-structured.md',encoding='utf-8'):
    if re.match(r'R\d{3} \|',l):
        p=[x.strip() for x in l.rstrip('\n').split(' | ')]
        rows.append(p)
json.dump(rows,open('runs/supremepwr-h1fy27/work/a2-results/rows.json','w'))
g=[]
for p in rows[:441]:
    n=int(p[0][1:]); pg=p[1][5:]; ln=p[2][5:]
    ctx=p[5] if len(p)>5 else ''; fl=p[6] if len(p)>6 else ''
    key=(pg,ln,re.sub(r', (standalone|consolidated).*','',ctx.split(',')[0]) if False else ctx.split(', standalone')[0].split(', consolidated')[0])
    if g and g[-1][0]==key: g[-1][1].append((n,p[4],fl))
    else: g.append([key,[(n,p[4],fl)]])
for key,m in g:
    ids=f"R{m[0][0]:03d}-R{m[-1][0]:03d}"
    fl=sorted({x[2] for x in m if x[2]})
    zs=any(re.fullmatch(r'[-–—]|nil|0|0\.00|-',x[1].strip(),re.I) for x in m)
    print(ids,len(m),key[0],key[1],key[2][:70],'|',[x[1] for x in m][:2] if len(m)<=2 else '', 'FL' if fl else '', 'ZERO' if zs else '')
