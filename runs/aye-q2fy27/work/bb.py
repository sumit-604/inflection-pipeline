import re,sys
w=re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',open(sys.argv[1],encoding='utf8').read())
rows={}
for a,b,c,d,t in w:
    rows.setdefault(round(float(b)/3),[]).append((float(c),t))
for k in sorted(rows):
    print(k*3, ' '.join(f"{t}@{int(x)}" for x,t in sorted(rows[k])))
