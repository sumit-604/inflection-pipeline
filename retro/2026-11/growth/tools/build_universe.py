"""Universe of analysed results (one row per company per period) and the filing candidates for each row.
Usage: build_universe.py <repo> <census.csv> <QR reviews dir> <Concall 'Q2 FY27 Results' dir>"""
import json, re, os, sys, csv, collections, subprocess
REPO, CENSUS, QR, CC = sys.argv[1:5]
inv = json.load(open("inventory.json")); cm = json.load(open("company_map.json", encoding="utf-8"))
P = {"q4fy26": "Q4 FY26", "h2fy26": "Q4 FY26", "q1fy27": "Q1 FY27", "q2fy27": "Q2/H1 FY27", "h1fy27": "Q2/H1 FY27",
     "q1cy26": "Q4 FY26", "q2cy26": "Q1 FY27", "q3cy26": "Q2/H1 FY27"}
SUF = re.compile(r"-(q\d(?:fy|cy)\d\d|h\dfy\d\d)$")
def period_from_name(fn):
    f = fn.lower().replace("_", "").replace("-", "").replace(" ", "")
    for k, v in P.items():
        if k in f: return v
    m = re.search(r"(2026)(\d\d)\d\d", f)
    if m:
        mo = int(m.group(2))
        if mo in (4, 5, 6): return "Q4 FY26"
        if mo in (7, 8, 9): return "Q1 FY27"
        if mo in (10, 11): return "Q2/H1 FY27"
    return None
run2t = {r: t for t, e in cm.items() for r in e["runs"]}
uni = collections.defaultdict(lambda: {"where": [], "filings": []})
MAIN = "origin/main"
for run, d in inv["runs"].items():
    t = run2t.get(run)
    if not t: continue
    files = {}
    for b in sorted(d["branches"], key=lambda b: (-len(d["branches"][b]), b != MAIN, b)):
        for p, sha in d["branches"][b].items(): files.setdefault(p, (b, sha))
    m = SUF.search(run)
    if m:
        per = P.get(m.group(1))
        if not per: continue
        u = uni[(t, per)]; b0 = sorted(d["branches"], key=lambda b: (-len(d["branches"][b]), b))[0]
        u["where"].append(f"repo {b0}:runs/{run}")
        for p, (b, sha) in files.items():
            rel = p[len("runs/" + run) + 1:].lower()
            if re.search(r"ledger|forensic|structured|blocks/|press|director|layout|marked|hdr\.txt|/pg-", rel): continue
            if re.search(r"extracted/.*results.*fulltext\.md$|work/extract_results[^/]*\.txt$|work/a1-results/(body|raw)\.txt$|results[^/]*-plain\.txt$", rel):
                u["filings"].append({"kind": "repo-text", "ref": f"{b}:{p}", "sha": sha})
            elif re.search(r"inputs/.*result.*\.pdf$", rel):
                u["filings"].append({"kind": "repo-pdf", "ref": f"{b}:{p}", "sha": sha})
    else:
        for p, (b, sha) in files.items():
            rel = p[len("runs/" + run) + 1:]
            if rel.startswith("inputs/results/") and rel.lower().endswith((".txt", ".pdf")):
                per = period_from_name(rel.split("/")[-1])
                if not per: continue
                u = uni[(t, per)]
                w = f"repo {b}:runs/{run} (pipeline run; results filing in inputs)"
                if w not in u["where"]: u["where"].append(w)
                u["filings"].append({"kind": "repo-text" if rel.lower().endswith(".txt") else "repo-pdf", "ref": f"{b}:{p}", "sha": sha})
for t, e in cm.items():
    for q in e["qr_dirs"]:
        mds = [f for f in os.listdir(q) if f in ("REVIEW.md", "NARRATIVE.md", "SIMPLE_BRIEF.md", "2-review-draft.md")]
        if not mds: continue
        u = uni[(t, "Q2/H1 FY27")]
        u["where"].append("QuarterlyReviewer/reviews/" + "/".join(q.replace("\\", "/").split("/")[-2:]))
        td = os.path.join(q, "text")
        if os.path.isdir(td):
            for f in sorted(os.listdir(td)):
                if re.match(r"D\d*-results.*\.txt$", f): u["filings"].append({"kind": "qr-text", "ref": os.path.join(td, f)})
            if not any(x["kind"] == "qr-text" and x["ref"].startswith(td) for x in u["filings"]):
                for f in sorted(os.listdir(td)):
                    if re.match(r"D\d", f) and f.endswith(".txt") and not re.search(r"transcript|concall|presentation", f):
                        u["filings"].append({"kind": "qr-text-other", "ref": os.path.join(td, f)})
al = json.load(open("aliases.json", encoding="utf-8"))
if os.path.isdir(CC):
    for d in sorted(os.listdir(CC)):
        full = os.path.join(CC, d)
        if not os.path.isdir(full) or d.startswith("_"): continue
        name = re.sub(r"^\d+\s+", "", d).lower()
        hit = [t for t, a in al.items() if any(x.lower() in name or name.split(" (")[0] in x.lower() for x in a if len(x) > 5 and not x.isupper())]
        FIX = {"fabtech technologies": "FABTECH", "kotyark industries": "KOTYARK", "womancart": "WOMANCART", "zota health care": "ZOTA"}
        t = FIX.get(name) or (hit[0] if len(hit) == 1 else ("CC:" + d))
        u = uni[(t, "Q2/H1 FY27")]
        u["where"].append("ConcallPipeline/Q2 FY27 Results/" + d)
        for f in os.listdir(full):
            if re.search(r"result", f, re.I) and f.lower().endswith(".pdf"): u["filings"].append({"kind": "cc-pdf", "ref": os.path.join(full, f)})
cen = list(csv.DictReader(open(CENSUS, encoding="utf-8-sig")))
names = {}; census_only = []
for r in cen:
    names[r["ticker"]] = r["name"]
    k = (r["ticker"], r["period"])
    if k not in uni and any(r[x] != "NOT FOUND" for x in ("actual revenue", "actual profit")):
        census_only.append({"ticker": r["ticker"], "name": r["name"], "period": r["period"], "actuals_quoted_in": r["source: actuals"]})
json.dump(census_only, open("census_only.json", "w", encoding="utf-8"), indent=1)
out = [{"ticker": t, "name": names.get(t, cm.get(t, {}).get("name", "").lstrip("?")), "period": p, **v} for (t, p), v in sorted(uni.items())]
json.dump(out, open("universe.json", "w", encoding="utf-8"), indent=1)
c = collections.Counter(r["period"] for r in out)
print(len(out), dict(c), "companies", len({r["ticker"] for r in out}))
print("rows with no filing candidate", collections.Counter(r["period"] for r in out if not r["filings"]))
print("census-only (not counted)", len(census_only))
print("CC unmatched", [r["ticker"] for r in out if r["ticker"].startswith("CC:")])
print(collections.Counter(f["kind"] for r in out for f in r["filings"]))
