"""Export the results filings for every universe row into filings/<TICKER>__<period>/ and write growth_rows.json.
Repo files are read with git cat-file (no checkout). PDFs are converted with pdftotext -layout and page-marked."""
import json, os, re, subprocess, sys, shutil
REPO = sys.argv[1]
u = json.load(open("universe.json", encoding="utf-8")); cm = json.load(open("company_map.json", encoding="utf-8"))
OUT = "filings"
def pdf_to_text(pdf, txt):
    r = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True)
    pages = r.stdout.decode("utf-8", "replace").split("\f")
    n = sum(len(p.strip()) for p in pages)
    with open(txt, "w", encoding="utf-8") as f:
        for i, p in enumerate(pages, 1):
            if p.strip() or i < len(pages): f.write(f"=== page {i} ===\n{p}\n")
    return len(pages) - 1, n
shas = sorted({f["sha"] for r in u for f in r["filings"] if "sha" in f})
env = dict(os.environ, GIT_NO_LAZY_FETCH="1")
chk = subprocess.run(["git", "-C", REPO, "cat-file", "--batch-check"], input=("\n".join(shas) + "\n").encode(), capture_output=True, env=env).stdout.decode()
missing = [l.split()[0] for l in chk.splitlines() if l.endswith("missing")]
print("blobs", len(shas), "missing", len(missing), flush=True)
for i in range(0, len(missing), 300):
    r = subprocess.run(["git", "-C", REPO, "-c", "fetch.negotiationAlgorithm=noop", "fetch", "origin", "--no-tags", "--no-write-fetch-head", "--recurse-submodules=no", "--filter=blob:none", "--stdin"],
                       input=("\n".join(missing[i:i + 300]) + "\n").encode(), capture_output=True)
    print("fetch", i, r.returncode, r.stderr[-200:].decode(errors="replace"), flush=True)
p = subprocess.Popen(["git", "-C", REPO, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
def blob(sha):
    p.stdin.write((sha + "\n").encode()); p.stdin.flush()
    h = p.stdout.readline().split()
    if h[1] == b"missing": return None
    d = p.stdout.read(int(h[2])); p.stdout.read(1); return d
rows = []
for r in u:
    key = f"{r['ticker']}__{r['period'].replace('/', '-').replace(' ', '')}"
    d = os.path.join(OUT, key); os.makedirs(d, exist_ok=True)
    cands = []
    kinds = {f["kind"] for f in r["filings"]}
    for i, f in enumerate(r["filings"]):
        k = f["kind"]
        if k in ("qr-text", "qr-text-other"):
            cands.append({"read": f["ref"], "cite": "QuarterlyReviewer/reviews/" + "/".join(f["ref"].replace("\\", "/").split("/")[-4:]), "type": "page-marked text of the filed PDF"})
        elif k == "repo-text":
            b = blob(f["sha"])
            if b is None: continue
            fn = os.path.join(d, f"{i:02d}_" + f["ref"].split("/")[-1]); open(fn, "wb").write(b)
            cands.append({"read": os.path.abspath(fn), "cite": "origin/" + f["ref"].split("origin/", 1)[-1], "type": "extracted text committed in repo"})
        elif k == "repo-pdf":
            stem = f["ref"].rsplit(".", 1)[0]
            if any(x["kind"] == "repo-text" and (x["ref"].rsplit(".", 1)[0] == stem) for x in r["filings"]): continue
            if "repo-text" in kinds and not re.search(r"inputs/results/", f["ref"]): continue   # quarterly folder already has extracted text
            b = blob(f["sha"])
            if b is None: continue
            fn = os.path.join(d, f"{i:02d}_" + f["ref"].split("/")[-1]); open(fn, "wb").write(b)
            np_, n = pdf_to_text(fn, fn + ".txt")
            cands.append({"read": os.path.abspath(fn + ".txt"), "pdf": os.path.abspath(fn), "cite": "origin/" + f["ref"].split("origin/", 1)[-1], "type": f"pdftotext of repo PDF ({np_} pages, {n} chars)" + (" - SCANNED, read the PDF pages instead" if n < 500 else "")})
        elif k == "cc-pdf":
            fn = os.path.join(d, f"{i:02d}_" + os.path.basename(f["ref"]) + ".txt")
            np_, n = pdf_to_text(f["ref"], fn)
            cands.append({"read": os.path.abspath(fn), "pdf": f["ref"], "cite": "ConcallPipeline/Q2 FY27 Results/" + "/".join(f["ref"].replace("\\", "/").split("/")[-2:]), "type": f"pdftotext of local PDF ({np_} pages, {n} chars)" + (" - SCANNED, read the PDF pages instead" if n < 500 else "")})
    if not cands and r["period"].startswith("Q2"):
        for q in cm.get(r["ticker"], {}).get("qr_dirs", []):
            for sub in ("text", "docs"):
                sd = os.path.join(q, sub)
                if os.path.isdir(sd):
                    for fn in sorted(os.listdir(sd)):
                        if fn.lower().endswith((".txt", ".pdf")) and not re.search(r"transcript|concall|R\d-ref|presentation|ppt", fn, re.I):
                            cands.append({"read": os.path.join(sd, fn), "cite": "QuarterlyReviewer/reviews/" + "/".join(os.path.join(sd, fn).replace("\\", "/").split("/")[-4:]), "type": "unclassified local file; check whether it is the results filing"})
    rows.append({"key": key, "ticker": r["ticker"], "name": r["name"], "period": r["period"], "where": r["where"], "candidates": cands})
p.stdin.close()
json.dump(rows, open("growth_rows.json", "w", encoding="utf-8"), indent=1)
import collections
print(len(rows), "rows; no candidates:", [(x["ticker"], x["period"]) for x in rows if not x["candidates"]])
print(collections.Counter(min(len(x["candidates"]), 6) for x in rows))
print("scanned:", sum(1 for x in rows for c in x["candidates"] if "SCANNED" in c["type"]))
