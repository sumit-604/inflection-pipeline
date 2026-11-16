import json,os,re,random,subprocess,glob,warnings
warnings.filterwarnings("ignore")
import pymupdf
R="C:/Users/sumit/repos/inflection-pipeline"; QR="C:/QuarterlyReviewer/QuarterlyReviewer/reviews"
rows=json.load(open("rows.json")); cand=json.load(open("cand.json")); um=json.load(open("umeta.json"))
byrun={}
for sha,(r,p) in cand.items(): byrun.setdefault(r,[]).append((p,sha))
def pdfs_for(row):
    out=[]
    s=row["src"]
    if s.startswith("QR:"):
        t=s[3:]
        for w in row["where"].get("QR",[]):
            d=os.path.join(QR,w.split("/")[-2],t,"docs")
            for f in glob.glob(d+"/**/*.pdf",recursive=True):
                out.append(("QR",f))
    else:
        r=s[5:]
        for p,sha in byrun.get(r,[]): out.append(("REPO",(p,sha)))
    return out
def fmts(v):
    if v is None: return []
    a=abs(v); s=set()
    for dec in (2,1,0):
        x=("%."+str(dec)+"f")%a
        if abs(float(x)-a)>1e-6: continue
        ip,_,fp=x.partition(".")
        # western and indian grouping
        w="{:,}".format(int(ip)); 
        if len(ip)>3:
            h=ip[:-3]; ind=",".join([h[max(0,i-2):i] for i in range(len(h),0,-2)][::-1])+","+ip[-3:]
        else: ind=ip
        for g in (ip,w,ind):
            s.add(g+("."+fp if fp else ""))
    return s
def pages(kind,ref):
    if kind=="QR": doc=pymupdf.open(ref)
    else:
        b=subprocess.run(["git","-C",R,"cat-file","-p",ref[1]],capture_output=True).stdout
        doc=pymupdf.open(stream=b,filetype="pdf")
    return [pg.get_text() for pg in doc]
elig=[r for r in rows if r.get("src_kind")=="review file" and pdfs_for(r)]
random.seed(20261117)
sample=random.sample(elig,20)
res=[]
for r in sample:
    need={"pbt_c":r["pbt_c"],"oi_c":r["oi_c"],"pbt_p":r["pbt_p"],"oi_p":r["oi_p"]}
    best=None
    for kind,ref in pdfs_for(r):
        try: pg=pages(kind,ref)
        except Exception as e: continue
        name=os.path.basename(ref) if kind=="QR" else ref[0].split("/")[-1]
        for i,t in enumerate(pg):
            tt=re.sub(r"\s+"," ",t)
            found={k:any(re.search(r"(?<![\d.,])"+re.escape(f)+r"(?![\d])",tt) for f in fmts(v)) for k,v in need.items()}
            sc=sum(found.values())
            if best is None or sc>best[0]: best=(sc,name,i+1,found,len(tt))
    res.append((r["ticker"],r["period"],r["src"],need,best,len(pdfs_for(r))))
    print(r["ticker"],r["period"],r["basis"],need,"->",best)
json.dump(res,open("check20.json","w"),default=str)
print(len(elig),"eligible")
