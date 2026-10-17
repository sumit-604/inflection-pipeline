import re,sys,json
rows=[]
for ln in open('extracted/tatacomm-results-q2fy27-structured.md',encoding='utf-8'):
    m=re.match(r'^(R\d+) \| page (\d+) \| line (\d+) \| (\w+) \| (.*)$',ln.rstrip('\n'))
    if m:
        rest=m.group(5); 
        v,_,c=rest.partition(' | ')
        rows.append(dict(id=m.group(1),pg=int(m.group(2)),ln=int(m.group(3)),t=m.group(4),v=v,c=c))
json.dump(rows,open('work/a2-results/rows.json','w'))
print(len(rows))
