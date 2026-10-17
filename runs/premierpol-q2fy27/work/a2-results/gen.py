import re,collections
rows=[l.rstrip("\n").split(" | ") for l in open("extracted/premierpol-results-q2fy27-structured.md",encoding="utf8") if re.match(r"R\d{3} ",l)]
ids=[r[0] for r in rows]
groups=collections.OrderedDict()
zero=[]
for r in rows:
    n=int(r[0][1:])
    if n<=310:
        lab=r[5]
        lab=re.sub(r", (Q2FY27|Q1FY27|Q2FY26|H1FY27|H1FY26|FY26|30/09/2026|31/03/2026|col1|col2)$","",lab)
        groups.setdefault(lab,[]).append((r[0],r[1],r[2],r[3:]))
        if "ZERO_STANDING" in " ".join(r): zero.append(r[0])
out=[]
out.append("| group | page | IDs | count | flags | note |\n|---|---|---|---|---|---|")
nm={}
for lab,g in groups.items():
    gi=[x[0] for x in g]
    fl=set()
    allr=[ " | ".join(x[3]) for x in g]
    for s in allr:
        for f in ["ZERO_STANDING","OCR_AS_READ","OCR_UNREADABLE","PERIOD_COLUMN_UNRESOLVED","LABEL_MISALIGNED_OCR","LABEL_ON_PRIOR_LINE","OCR_AMBIGUOUS"]:
            if f in s: fl.add(f)
    out.append(f"| {lab} | {g[0][1]} | {gi[0]}..{gi[-1]} ({len(gi)}) | {len(gi)} | {','.join(sorted(fl))} | |")
print(len(groups),len(zero))
open("work/a2-results/lineitems.md","w").write("\n".join(out))
