import subprocess, json, collections, sys, re
REPO = sys.argv[1]
def git(*a):
    return subprocess.run(["git","-C",REPO,*a],capture_output=True,text=True,encoding="utf-8",errors="replace").stdout
branches=[b.strip() for b in git("branch","-r").splitlines() if "->" not in b]
runs=collections.defaultdict(lambda: {"branches":{}, })   # run folder -> branch -> {path: sha}
comp=collections.defaultdict(dict)  # ticker file -> branch -> sha
other=collections.defaultdict(dict)
for b in branches:
    out=git("ls-tree","-r",b)
    for line in out.splitlines():
        meta,path=line.split("\t",1)
        sha=meta.split()[2]
        if path.startswith("runs/"):
            parts=path.split("/")
            if len(parts)<3: continue
            runs[parts[1]]["branches"].setdefault(b,{})[path]=sha
        elif path.startswith("companies/"):
            comp[path][b]=sha
        elif path in("LESSONS_ARCHIVE.md","LESSONS.md"):
            other[path][b]=sha
json.dump({"branches":branches,"runs":runs,"companies":comp,"other":other},open("inventory.json","w"))
main="origin/main"
print("branches",len(branches),"run folders",len(runs),"company files",len(comp))
# summary per run folder
rows=[]
for r,d in sorted(runs.items()):
    bs=d["branches"]
    onmain= main in bs
    # distinct content versions
    vers=collections.defaultdict(list)
    for b,files in bs.items():
        vers[hash(frozenset(files.items()))].append(b)
    nonmain=[b for b in bs if b!=main]
    # pick richest branch
    best=max(bs,key=lambda b:(len(bs[b]), b==main))
    rows.append((r,onmain,len(bs),len(vers),len(bs[best]),best))
with open("runs_summary.tsv","w") as f:
    for row in rows: f.write("\t".join(map(str,row))+"\n")
notmain=[r for r in rows if not r[1]]
print("run folders not on main:",len(notmain))
for r in notmain: print("  ",r[0],r[2],r[4],r[5])
print("run folders on main:",len(rows)-len(notmain))
multi=[r for r in rows if r[1] and r[3]>1]
print("on main but differing versions on other branches:",len(multi))
cm=[p for p in comp if main in comp[p]]
cn=[p for p in comp if main not in comp[p]]
print("company files on main",len(cm),"only elsewhere",len(cn))
for p in cn: print("  ",p,list(comp[p])[:3])
