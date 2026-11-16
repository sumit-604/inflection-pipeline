import json,csv,os,collections,shutil
OUT="C:/Users/sumit/repos/inflection-pipeline/.claude/worktrees/retro-2026-11/retro/2026-11/growth"
os.makedirs(OUT+"/tools",exist_ok=True)
rows=json.load(open("rows.json"))
TAX=0.2517
SL={"DHANBANK","KISSHT","NORTHARC"}
NC={("543916","Q2/H1 FY27"):"Subsidiary acquired 1-Jun-2026; half year not like-for-like",
 ("DIGITIDE","Q1 FY27"):"Demerger; last year's quarter carries demerger expenses and a different perimeter",
 ("ENTERO","Q2/H1 FY27"):"Several subsidiaries acquired during FY26; consolidated year-on-year not like-for-like",
 ("PARACABLES","Q2/H1 FY27"):"Valens Technologies divested 6-Nov-2025; last year's quarter includes it",
 ("UNIMECH","Q2/H1 FY27"):"Three entities consolidated from 27-Apr-2026",
 ("CAPILLARY","Q2/H1 FY27"):"Acquisitions (SessionM, Kognitiv); last year's quarter is an unreviewed balancing figure",
 ("RATEGAIN","Q1 FY27"):"Acquisition: revenue 2,729 to 7,850 (Rs million) year on year"}
def label(c,p):
    if c<0: return "LOSS",None
    if p<0: return "TURNAROUND",None
    if p==0: return "LOW BASE",None
    g=c/p-1
    if p<1: return "LOW BASE",g
    return ("ABOVE 25%" if g>0.25 else "0 TO 25%" if g>=0 else "FELL"),g
for r in rows:
    if r["label"]=="NO FILING": continue
    if r["ticker"] in SL and r["src_kind"].startswith("screener"):
        r["opc"]=r["pbt_c"]; r["opp"]=r["pbt_p"]; r["lmark"]="LENDER-REPORTED"; r["lender"]=True
        r["label"],r["g"]=label(r["opc"],r["opp"])
    k=(r["ticker"],r["period"])
    if k in NC: r["label"]="NOT COMPARABLE"; r["nc"]=NC[k]
def wh(r):
    return " | ".join(x for v in r["where"].values() for x in v)
with open(OUT+"/universe.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["ticker","name","period","where the review lives"])
    for r in rows: w.writerow([r["ticker"],r["name"],r["period"],wh(r)])
def n(x,d=2): return "" if x is None else ("%."+str(d)+"f")%x
H=["ticker","name","period","reports","consolidated or standalone","unit in file","PBT before exceptional items, this year (file unit)","PBT before exceptional items, last year (file unit)","other income, this year (file unit)","other income, last year (file unit)","exceptional items, this year (file unit; gain +, charge -)","exceptional items, last year (file unit)","operating profit before tax, this year (Rs Cr)","operating profit before tax, last year (Rs Cr)","operating profit after tax at 25.17%, this year (Rs Cr)","operating profit after tax at 25.17%, last year (Rs Cr)","growth %","reported profit after tax, this year (file unit)","reported profit after tax, last year (file unit)","reported profit growth %","label","lender mark","source type","source file","page or table","note"]
with open(OUT+"/growth.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(H)
    for r in rows:
        if r["label"]=="NO FILING":
            w.writerow([r["ticker"],r["name"],r["period"]]+[""]*17+["NO FILING","","","","",""]); continue
        src=r["src"]
        if src.startswith("QR:"): src=[x for x in r["where"].get("QR",["QuarterlyReviewer/reviews/?/"+src[3:]])][-1]
        elif src.startswith("REPO:"): src=[x for x in r["where"].get("REPOQ",[]) if x.endswith("runs/"+src[5:])][0]
        note=(r.get("nc","")+" " if r.get("nc") else "")+(r.get("note") or "")+((" Share of associates removed." ) if r.get("how") else "")
        g=r.get("g")
        w.writerow([r["ticker"],r["name"],r["period"],r.get("reporter",""),r["basis"],r["unit"],n(r["pbt_c"]),n(r["pbt_p"]),n(r["oi_c"]),n(r["oi_p"]),n(r["exc_c"]),n(r["exc_p"]),
            n(r["opc"]),n(r["opp"]),n(r["opc"]*(1-TAX)),n(r["opp"]*(1-TAX)),"" if g is None else n(g*100,1),n(r.get("pat_c")),n(r.get("pat_p")),"" if r.get("rg") is None else n(r["rg"]*100,1),
            r["label"],r.get("lmark",""),r["src_kind"],src,r["cite"],note.strip()])
ORDER=["ABOVE 25%","0 TO 25%","FELL","LOSS","TURNAROUND","LOW BASE","NOT COMPARABLE","NO FILING"]
PERS=["Q2/H1 FY27","Q1 FY27","Q4 FY26"]
cnt=collections.Counter((r["period"],r["label"]) for r in rows)
md=["# Operating profit growth, by period and label","","Operating profit before tax = PBT before exceptional items minus other income (lenders: see README). Growth = this year / last year - 1. Sorted by growth, highest first.",""]
md+=["| period | results | "+" | ".join(ORDER)+" |","|---|---|"+"---|"*len(ORDER)]
for p in PERS: md.append("| %s | %d | "%(p,sum(cnt[(p,l)] for l in ORDER))+" | ".join(str(cnt[(p,l)]) for l in ORDER)+" |")
for p in PERS:
    md+=["","## "+p]
    for l in ORDER:
        rs=[r for r in rows if r["period"]==p and r["label"]==l]
        if not rs: continue
        rs.sort(key=lambda r:(-(r.get("g") if r.get("g") is not None else -9e9),r["ticker"]))
        md+=["","### %s (%d)"%(l,len(rs)),""]
        for r in rs:
            g=r.get("g")
            if l=="NO FILING": md.append("- %s %s"%(r["ticker"],r["name"]))
            elif g is None: md.append("- %s %s: operating profit %s vs %s Rs Cr"%(r["ticker"],r["name"],n(r["opc"]),n(r["opp"])))
            else: md.append("- %s %s: %+.1f%%%s"%(r["ticker"],r["name"],g*100,(" ("+r["nc"]+")") if r.get("nc") else ""))
open(OUT+"/names.md","w",encoding="utf-8").write("\n".join(md)+"\n")
ms=["# Missing: rows with no figures for both years","","A review or census row exists, but our review files do not hold PBT and other income for both this year and last year, and the filing itself was not opened in this run. Fetch or open the results filing for each.","","| ticker | name | period | where the review lives | why |","|---|---|---|---|---|"]
for r in rows:
    if r["label"]!="NO FILING": continue
    c=r.get("cands") or []
    why="; ".join("%s: %s"%(x[0].split(":",1)[1],(x[2] or x[1] or "")[:140].replace("|","/")) for x in c) if c else "census row only: no ledger or quarter table for this period in our files"
    ms.append("| %s | %s | %s | %s | %s |"%(r["ticker"],r["name"],r["period"],wh(r).replace("|",";"),why))
open(OUT+"/missing.md","w",encoding="utf-8").write("\n".join(ms)+"\n")
for f in ("universe.py","screener.py","snip.py","assemble.py","write_out.py","check20.py"): shutil.copy(f,OUT+"/tools/"+f)
json.dump(rows,open("rows_final.json","w"),default=str)
for p in PERS: print(p,sum(cnt[(p,l)] for l in ORDER),{l:cnt[(p,l)] for l in ORDER})
q2={r["ticker"]:r for r in rows if r["period"]=="Q2/H1 FY27" and r["label"]=="ABOVE 25%"}
q1={r["ticker"]:r for r in rows if r["period"]=="Q1 FY27"}
both=[t for t in q2 if t in q1 and q1[t]["label"]=="ABOVE 25%"]
hasq1=[t for t in q2 if t in q1 and q1[t]["label"]!="NO FILING"]
print(len(q2),"Q2 above; with a Q1 number",len(hasq1),"also above in Q1",len(both),sorted(both))
print(collections.Counter(q1[t]["label"] if t in q1 else "not in Q1 universe" for t in q2))
print(collections.Counter(r["src_kind"] for r in rows if r["label"]!="NO FILING"))
print("; ".join("%s %+.0f%%"%(r["ticker"],r["g"]*100) for r in sorted(q2.values(),key=lambda r:-r["g"])))
