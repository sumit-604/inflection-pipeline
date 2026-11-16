import re
KEY=re.compile(r"other income|before (exceptional|tax)|before share|PBT|exceptional|profit/?\s*\(?loss\)? before|share of (profit|loss|net)|total income|revenue from operations|^\|\s*(net )?profit (after tax|for the)|\bPAT\b|tax expense|treasury|trading gain",re.I)
def snippet(text,maxlines=70,head=10):
    L=text.splitlines()
    out=[l[:400] for l in L[:head] if l.strip()]
    i=0;n=len(L);tables=0
    while i<n and len(out)<maxlines:
        if L[i].lstrip().startswith("|"):
            j=i
            while j<n and L[j].lstrip().startswith("|"): j+=1
            tab=L[i:j]
            hits=[t for t in tab[2:] if KEY.search(t)]
            if any(re.search(r"other income|before tax|PBT|before exceptional",t,re.I) for t in tab):
                ctx=[l for l in L[max(0,i-4):i] if l.strip()][-3:]
                out.append("--- table @line %d ---"%(i+1))
                out+= [c[:300] for c in ctx]
                out.append(tab[0][:600])
                out+= [h[:600] for h in hits[:14]]
                tables+=1
            i=j
        else: i+=1
    return "\n".join(out[:maxlines]),tables

G=re.compile(r"other income|before (exceptional|tax)|\bPBT\b|exceptional|share of (profit|loss|net)|total income|revenue from operations|profit (after tax|for the (period|quarter|year|half))|\bPAT\b|quarter ended|half year ended|year ended|particulars|consolidated|standalone|lakh|crore|million",re.I)
def grepsnip(text,maxlines=60,head=6):
    L=text.splitlines()
    out=[l[:300] for l in L[:head] if l.strip()]
    for i,l in enumerate(L[head:],head+1):
        if G.search(l) and re.search(r"\d",l) or re.search(r"other income|before (exceptional |)(items |)(and |)tax|exceptional item",l,re.I):
            out.append("L%d: %s"%(i,l.strip()[:500]))
            if len(out)>=maxlines: break
    return "\n".join(out)
def best(text,maxlines=60):
    s,nt=snippet(text,maxlines=maxlines)
    if nt==0: return grepsnip(text,maxlines=maxlines),0
    return s,nt
