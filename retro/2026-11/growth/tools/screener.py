import json,re,subprocess,csv,io,collections
R="C:/Users/sumit/repos/inflection-pipeline"
own=json.load(open("own.json")); run2t=json.load(open("run2t.json")); inv=json.load(open("inventory.json"))["runs"]
def cat(sha): return subprocess.run(["git","-C",R,"cat-file","-p",sha],capture_output=True).stdout.decode("utf-8","replace")
def rundate(r):
    m=re.search(r"(\d{4}-\d\d-\d\d)",r); return m.group(1) if m else "0000"
S={}
log=[]
for sha,(r,p) in own.items():
    fn=p.split("/")[-1]
    if not fn.lower().endswith(".csv"): log.append(("nocsv",r,fn)); continue
    t=run2t[r]; txt=cat(sha)
    rows=list(csv.reader(io.StringIO(txt)))
    name=""
    if rows and rows[0]:
        name=rows[0][1] if rows[0][0].strip().upper()=="COMPANY NAME" and len(rows[0])>1 else rows[0][0]
    # find quarters block
    blk=None
    if "data_sheet" in fn.lower():
        for i,row in enumerate(rows):
            if row and row[0].strip().lower()=="quarters": blk=rows[i+1:i+12]; break
    elif "quarters" in fn.lower():
        blk=rows[1:]
    if not blk: log.append(("noblk",r,fn)); continue
    d={}
    hdr=None
    for row in blk:
        if not row: continue
        k=row[0].strip().lower()
        if k in("report date","narration"): hdr=[c[:10] for c in row[1:]]
        elif hdr and k in("sales","other income","profit before tax","net profit","expenses","depreciation","interest","operating profit"):
            for dt,v in zip(hdr,row[1:]):
                try: d.setdefault(dt,{})[k]=float(v)
                except: pass
    d={k:v for k,v in d.items() if "profit before tax" in v and re.match(r"\d{4}-\d\d-\d\d",k)}
    if not d: log.append(("empty",r,fn)); continue
    br=sorted(inv[r],key=lambda b:-len(inv[r][b]))[0]
    for b in inv[r]:
        if p in inv[r][b]: br=b;break
    e={"run":r,"path":p,"branch":br,"name":name,"q":d,"date":rundate(r)}
    if t not in S or (max(d),e["date"])>(max(S[t]["q"]),S[t]["date"]): 
        if t in S: e["alt"]=S[t].get("alt",[])+[{k:S[t][k] for k in("run","path","branch","q")}]
        S[t]=e
    else: S[t].setdefault("alt",[]).append({k:e[k] for k in("run","path","branch","q")})
json.dump(S,open("screener.json","w"),indent=0)
print(len(S)); print(collections.Counter(x[0] for x in log)); print([x for x in log if x[0]!="empty"][:30])
U=json.load(open("universe.json"))
PD={"Q4 FY26":("2026-03-31","2025-03-31"),"Q1 FY27":("2026-06-30","2025-06-30"),"Q2/H1 FY27":("2026-09-30","2025-09-30")}
cov=collections.Counter()
for k,v in U.items():
    t,per=k.split("|"); a,b=PD[per]
    has=t in S and a in S[t]["q"] and b in S[t]["q"]
    cov[(per,"+".join(sorted(x for x in v if x!="CENSUS")) or "CENSUS",has)]+=1
for k,v in sorted(cov.items()): print(k,v)
