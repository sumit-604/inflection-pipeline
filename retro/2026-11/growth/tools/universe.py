import os,re,json,csv,collections
R="C:/Users/sumit/repos/inflection-pipeline"
CEN=R+"/.claude/worktrees/retro-2026-11/retro/2026-11/census.csv"
census=list(csv.DictReader(open(CEN,encoding="utf-8-sig")))
names={r["ticker"]:r["name"] for r in census}
rep={r["ticker"]:r["reports (quarterly or half-yearly)"] for r in census}
MERGE={"540686":"SMRUTHI","543709":"GARGI","544091":"QLL","544518":"LTELEVATOR","544710":"ACCORD","544740":"TIPCO","544793":"SUSAN","544826":"MILLWORKS","544895":"KWICK","544186":"TOTEM","544555":"AMEENJI"}
U=collections.defaultdict(lambda: collections.defaultdict(list))  # (ticker,period)->kind->[where]
# QR
qr=json.load(open("qr_rows.json")); qrmap={}
for t,e in qr.items():
    c=MERGE.get(t,t)
    ok=[x for x in e if x["rev"] or x["leds"]]
    if not ok: continue
    qrmap[c]=t
    for x in ok: U[(c,"Q2/H1 FY27")]["QR"].append("QuarterlyReviewer/reviews/%s/%s"%(x["batch"],t))
# repo quarterly folders
meta=json.load(open("repo_meta.json")); inv=json.load(open("inventory.json"))["runs"]; run2t=json.load(open("run2t.json"))
PER={"q4fy26":"Q4 FY26","q1fy27":"Q1 FY27","q2fy27":"Q2/H1 FY27","h1fy27":"Q2/H1 FY27","q2cy26":"Q1 FY27"}
repo_q={}
for r,m in meta.items():
    per=PER[m["suffix"]]; t=m["ticker"]
    br=sorted(inv[r],key=lambda b:-len(inv[r][b]))[0]
    U[(t,per)]["REPOQ"].append("%s:runs/%s"%(br,r)); repo_q.setdefault((t,per),[]).append(r)
# concall pipeline
CP="C:/ConcallPipeline/Daily Concall Intelligence/Q2 FY27 Results/"
al=json.load(open(R+"/.claude/worktrees/retro-2026-11/retro/2026-11/tools/aliases.json"))
for f in ("_Operator_Briefs_Q2FY27.md","_Operator_Briefs_Q2FY27_2026-10-28.md"):
    for l in open(CP+f,encoding="utf-8",errors="replace"):
        m=re.match(r"##\s+OPERATOR BRIEF\W+(.*)",l,re.I)
        if m:
            h=m.group(1); t=None
            mm=re.search(r"\(([A-Z0-9]{3,12})\)",h)
            if mm: t=mm.group(1)
            else:
                mm=re.match(r"([A-Z0-9]{3,12})\b",h); t=mm.group(1) if mm else None
            if t: U[(MERGE.get(t,t),"Q2/H1 FY27")]["CP"].append("ConcallPipeline/Q2 FY27 Results/"+f)
            else: print("CP header unparsed:",h[:60])
U[("LT","Q2/H1 FY27")]["CP"].append("ConcallPipeline/Q2 FY27 Results/_Operator_Briefs_Q2FY27.md")
for t in ("KROSS","HFCL","TATVA","GOCLCORP","GALLANTT"):
    U[(t,"Q2/H1 FY27")]["CP"].append("ConcallPipeline/Q2 FY27 Results/_Overnight_Review_2026-10-20.md")
# census rows with actuals
for r in census:
    has=any(r[k].strip() and not r[k].strip().upper().startswith("NOT FOUND") for k in ("actual revenue","actual margin","actual profit"))
    if has: U[(r["ticker"],r["period"])]["CENSUS"].append("retro/2026-11/census.csv")
for k in U:
    for kk in U[k]: U[k][kk]=sorted(set(U[k][kk]))
out={"%s|%s"%k:dict(v) for k,v in U.items()}
json.dump(out,open("universe.json","w"),indent=0)
json.dump({"names":names,"rep":rep,"qrmap":qrmap,"repo_q":{"%s|%s"%k:v for k,v in repo_q.items()}},open("umeta.json","w"),indent=0)
c=collections.Counter(k[1] for k in U); print(c, len(U), len(set(k[0] for k in U)))
c2=collections.Counter((k[1],"+".join(sorted(v))) for k,v in U.items())
for k,v in sorted(c2.items()): print(k,v)
print("no name:",sorted(set(k[0] for k in U if k[0] not in names)))
