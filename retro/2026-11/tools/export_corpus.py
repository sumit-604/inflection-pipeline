"""Export the census-relevant text files from every branch into a flat corpus dir.
Reads blobs with git cat-file (no checkout). Usage: export_corpus.py <repo> <outdir>"""
import subprocess, json, sys, os, re, collections
REPO, OUT = sys.argv[1], sys.argv[2]
inv = json.load(open("inventory.json"))
runs, comp = inv["runs"], inv["companies"]
MAIN = "origin/main"
PERIOD = re.compile(r"-(q\d(fy|cy)\d\d|h\dfy\d\d)$")
def relevant(run, rel):
    r = rel.lower()
    if r.endswith((".pdf",".png",".jpg",".csv",".xml",".zip",".gitkeep",".py",".html",".js",".json",".tsv")): return False
    base = r.split("/")[-1]
    if PERIOD.search(run) or "/" not in r or r.startswith("work/") or r.startswith("extracted/"):
        # quarterly-style folder
        if r.startswith("inputs/") : return base == "sources.md"
        if "fulltext" in base or base.startswith("extract_") or r.startswith("work/blocks/"): return False
        if base.startswith("forensics"): return False
        return r.endswith(".md") or base in ("manifest.yaml",)
    if r == "manifest.yaml" or r in ("run-log.md","step1-business-brief.md"): return True
    if r.startswith("outputs/final/") and r.endswith(".md"): return True
    if r.startswith("outputs/reports/"):
        return bool(re.match(r"(10|11|13|14|15|16|17|18|19|2\d)[a-z]?-", base)) or any(k in base for k in ("valuation","thesis","devil","synthesis","quarter","rde","halt"))
    if r.startswith("outputs/qa/") and r.endswith(".md"): return True
    return False
want = {}   # sha -> dest path ; header
index = []
for run, d in runs.items():
    if run == "_template": continue
    bs = d["branches"]
    order = sorted(bs, key=lambda b: (-len(bs[b]), b != MAIN, b))
    seen = {}
    for b in order:
        for p, sha in bs[b].items():
            rel = p[len("runs/"+run)+1:]
            if rel in seen or not relevant(run, rel): continue
            seen[rel] = (b, sha)
    for rel, (b, sha) in seen.items():
        dest = os.path.join(OUT, "runs", run, rel.replace("/", "__"))
        want[dest] = (sha, f"{b}:runs/{run}/{rel}")
    index.append({"run": run, "branches": sorted(bs), "on_main": MAIN in bs, "n_files_exported": len(seen), "primary_branch": order[0]})
for p, bs in comp.items():
    if not p.endswith(".md"): continue
    byver = collections.defaultdict(list)
    for b, sha in bs.items(): byver[sha].append(b)
    name = p.split("/")[-1][:-3]
    for i, (sha, bl) in enumerate(sorted(byver.items(), key=lambda kv: (MAIN not in kv[1], kv[1][0]))):
        b = MAIN if MAIN in bl else sorted(bl, key=lambda x: (not x.startswith("origin/run/"), x))[0]
        dest = os.path.join(OUT, "companies", f"{name}__v{i}.md")
        want[dest] = (sha, f"{b}:{p}  (also on {len(bl)-1} other branches)")
for p, bs in inv["other"].items():
    sha = bs.get(MAIN) or list(bs.values())[0]
    want[os.path.join(OUT, p)] = (sha, f"{MAIN}:{p}")
shas = sorted({s for s, _ in want.values()})
env = dict(os.environ, GIT_NO_LAZY_FETCH="1")
chk = subprocess.run(["git","-C",REPO,"cat-file","--batch-check"], input="\n".join(shas)+"\n", capture_output=True, text=True, env=env).stdout
missing = [l.split()[0] for l in chk.splitlines() if l.endswith("missing")]
print("files", len(want), "blobs", len(shas), "missing", len(missing), flush=True)
for i in range(0, len(missing), 500):
    r = subprocess.run(["git","-C",REPO,"-c","fetch.negotiationAlgorithm=noop","fetch","origin","--no-tags","--no-write-fetch-head","--recurse-submodules=no","--filter=blob:none","--stdin"], input=("\n".join(missing[i:i+500])+"\n").encode(), capture_output=True)
    print("fetch batch", i, r.returncode, r.stderr[-300:].decode(errors="replace"), flush=True)
chk = subprocess.run(["git","-C",REPO,"cat-file","--batch-check"], input="\n".join(shas)+"\n", capture_output=True, text=True, env=env).stdout
print("still missing", sum(1 for l in chk.splitlines() if l.endswith("missing")), flush=True)
total = 0
p = subprocess.Popen(["git","-C",REPO,"cat-file","--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
for dest, (sha, src) in want.items():
    p.stdin.write((sha+"\n").encode()); p.stdin.flush()
    hdr = p.stdout.readline().split()
    if hdr[1] == b"missing": print("MISSING", src); continue
    n = int(hdr[2]); data = p.stdout.read(n); p.stdout.read(1)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(f"<!-- SOURCE {src} -->\n".encode()); f.write(data)
    total += n
p.stdin.close()
json.dump(index, open(os.path.join(OUT, "run_index.json"), "w"), indent=1)
print("bytes", total)
