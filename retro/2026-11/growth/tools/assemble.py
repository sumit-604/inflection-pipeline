import json,os,re,csv,collections,glob,sys
U=json.load(open("universe.json")); um=json.load(open("umeta.json")); S=json.load(open("screener.json"))
names=um["names"]; rep=um["rep"]; qrmap=um["qrmap"]; repo_q=um["repo_q"]; meta=json.load(open("repo_meta.json"))
R={}
for f in sorted(glob.glob("out/batch_*.json")):
    try:
        for o in json.load(open(f,encoding="utf-8")): R[o["id"]]=o
    except Exception as e: print("BAD",f,e)
ov={}
if os.path.exists("overrides.json"): ov=json.load(open("overrides.json"))
TAX=0.2517
PD={"Q4 FY26":("2026-03-31","2025-03-31"),"Q1 FY27":("2026-06-30","2025-06-30"),"Q2/H1 FY27":("2026-09-30","2025-09-30")}
def unitf(u):
    u=(u or "").lower()
    if "lakh" in u or "lac" in u: return 0.01,"Rs lakh"
    if "crore" in u or re.search(r"bcrs?b",u): 
        return 1,"Rs crore"
    if "million" in u or "mn" in u: 
        return (None,u) if "usd" in u or "$" in u else (0.1,"Rs million")
    if "thousand" in u or "'000" in u or "000" in u: return 0.0001,"Rs thousand"
    if "hundred" in u: return 0.00001,"Rs hundred"
    return None,u
def num(x):
    if x is None: return None
    if isinstance(x,(int,float)): return float(x)
    s=str(x).replace(",","").strip()
    neg=s.startswith("(") and s.endswith(")")
    s=s.strip("()")
    try: v=float(s)
    except: return None
    return -v if neg else v
def op_of(d,o,which):
    """returns (pbt_before_exc_ex_share, other_income, exceptional, how) in file units"""
    oi=num(d.get("other_income")); exc=num(d.get("exceptional")); sh=num(d.get("share_assoc"))
    pbe=num(d.get("pbt_before_exc")); pbt=num(d.get("pbt"))
    how=""
    if pbe is not None:
        base=pbe
        if o.get("pbt_before_exc_includes_share_assoc") and sh is not None: base-=sh; how="less share of associates"
    elif pbt is not None:
        base=pbt-(exc or 0)
        if o.get("pbt_includes_share_assoc") and sh is not None: base-=sh; how="less share of associates"
    else: return None
    return base,oi,exc,how
def label(c,p,cr):
    # c,p operating profit before tax in Rs Cr
    if c is None or p is None: return "NO FILING",None
    if c<0: return "LOSS",None
    if p<0: return "TURNAROUND",None
    if p==0: return "LOW BASE",None
    g=c/p-1
    if p<1: return "LOW BASE",g
    if g>0.25: return "ABOVE 25%",g
    if g>=0: return "0 TO 25%",g
    return "FELL",g
rows=[]
for k,src in sorted(U.items()):
    t,per=k.split("|")
    row={"ticker":t,"name":names.get(t,""),"period":per,"where":src}
    cands=[]
    if per=="Q2/H1 FY27" and t in qrmap and "QR:"+qrmap[t] in R: cands.append(R["QR:"+qrmap[t]])
    for r in repo_q.get(k,[]):
        if "REPO:"+r in R: cands.append(R["REPO:"+r])
    def score(o):
        c=op_of(o.get("cur") or {},o,"c"); p=op_of(o.get("prev") or {},o,"p")
        full=bool(c and p and c[1] is not None and p[1] is not None)
        return (full, o.get("doc_type")=="results filing", o.get("basis")=="consolidated")
    cands.sort(key=score,reverse=True)
    got=False
    for o in cands:
        c=op_of(o.get("cur") or {},o,"c"); p=op_of(o.get("prev") or {},o,"p")
        f,ulabel=unitf(o.get("unit"))
        if not(c and p and c[1] is not None and p[1] is not None and f): continue
        opc=(c[0]-c[1])*f; opp=(p[0]-p[1])*f
        patc=num(o["cur"].get("pat")); patp=num(o["prev"].get("pat"))
        row.update(basis=o.get("basis"),reporter=o.get("reporter"),unit=ulabel,f=f,
            pbt_c=c[0],oi_c=c[1],exc_c=c[2],pbt_p=p[0],oi_p=p[1],exc_p=p[2],opc=opc,opp=opp,
            pat_c=patc,pat_p=patp,src_kind="review file",src=o["id"],cite=o.get("cite",""),doc_type=o.get("doc_type"),
            lender=bool(o.get("lender")),tg_c=num(o["cur"].get("treasury_gain")),tg_p=num(o["prev"].get("treasury_gain")),
            note=o.get("note",""),labels=(o.get("cur_label"),o.get("prev_label")),how=c[3])
        got=True;break
    if not got and t in S:
        a,b=PD[per]; q=S[t]["q"]
        srcs=[S[t]]+S[t].get("alt",[])
        for s in srcs:
            q=s["q"]
            if a in q and b in q and "other income" in q[a] and "other income" in q[b]:
                half=not any(d[5:7] in("06","12") for d in q)
                pc=q[a]["profit before tax"];pp=q[b]["profit before tax"];oc=q[a]["other income"];opv=q[b]["other income"]
                row.update(basis="as exported by screener (basis not stated in file)",reporter="half-yearly" if half else "quarterly",unit="Rs crore",f=1,
                    pbt_c=pc,oi_c=oc,exc_c=None,pbt_p=pp,oi_p=opv,exc_p=None,opc=pc-oc,opp=pp-opv,
                    pat_c=q[a].get("net profit"),pat_p=q[b].get("net profit"),src_kind="screener table in run folder",
                    src="%s:%s"%(s["branch"],s["path"]),cite="Quarters block, columns %s and %s"%(a,b),doc_type="screener export",lender=False,tg_c=None,tg_p=None,
                    note="Screener puts exceptional items inside other income, so PBT minus other income leaves both out.",labels=(a,b),how="")
                got=True;break
    if got:
        if row["lender"]:
            # lenders: PBT minus treasury gains where stated, else reported PBT
            if row["tg_c"] is not None and row["tg_p"] is not None:
                row["opc"]=(row["pbt_c"]-row["tg_c"])*row["f"]; row["opp"]=(row["pbt_p"]-row["tg_p"])*row["f"]; row["lmark"]="LENDER: PBT less treasury gains"
            else:
                row["opc"]=row["pbt_c"]*row["f"]; row["opp"]=row["pbt_p"]*row["f"]; row["lmark"]="LENDER-REPORTED"
        lab,g=label(row["opc"],row["opp"],1)
        row["label"]=lab;row["g"]=g
        pc,pp=row.get("pat_c"),row.get("pat_p")
        row["rg"]=(pc/pp-1) if (pc is not None and pp and pp>0 and pc>0) else None
    else:
        row["label"]="NO FILING"; row["cands"]=[(o["id"],o.get("status"),o.get("note")) for o in cands]
    o2=ov.get(k)
    if o2: row.update(o2)
    rows.append(row)
json.dump(rows,open("rows.json","w"),indent=0,default=str)
c=collections.Counter((r["period"],r["label"]) for r in rows)
for k,v in sorted(c.items()): print(k,v)
print(len(R),"reader records")
