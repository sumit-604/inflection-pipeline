#!/usr/bin/env python3
"""Assemble census.csv, companies/, gaps.md and sources.md from per-company JSON.

Usage: python assemble.py <work_dir> <dest_dir> <laptop_name>
  work_dir holds out/*.json, out_md/*.md, company_map.json, inventory.json,
  corpus/run_index.json, session_excerpts/_summary.json (made by the other scripts).
"""
import csv, json, os, re, sys, glob, shutil, collections

WORK, DEST, LAPTOP = sys.argv[1], sys.argv[2], sys.argv[3]
NF = "NOT FOUND"
PERIODS = ["Q4 FY26", "Q1 FY27", "Q2/H1 FY27"]
COLS = [
 ("ticker", "ticker"), ("name", "name"), ("board", "board (SME or main)"),
 ("reporting", "reports (quarterly or half-yearly)"), ("archetype", "archetype"),
 ("first_analysis_date", "first analysis date"), ("verdict_at_first", "verdict at that date"),
 ("framework_date", "framework date (before/after 08-Sep-2026)"), ("projection_basis", "projection basis"),
 ("period", "period"),
 ("base_revenue", "our base-case revenue"), ("base_margin", "our base-case margin"), ("base_profit", "our base-case profit"),
 ("base_period", "base-case period"),
 ("guidance_quote", "management guidance at the time"), ("catalysts", "promised catalysts with dates"),
 ("actual_revenue", "actual revenue"), ("actual_margin", "actual margin"), ("actual_profit", "actual profit"),
 ("result_vs_base", "result vs our base case"), ("result_basis", "basis of result call"),
 ("mgmt_reason", "management's stated reason"),
 ("risk_flagged_before", "risk flagged before result"), ("risk_flag_ref", "risk flag file and line"),
 ("who_flagged", "who flagged it"), ("overruled", "overruled"), ("overruled_ref", "overruled reference"),
 ("src_identity", "source: board/reporting/archetype"), ("src_first", "source: first analysis and verdict"),
 ("projection_basis_source", "source: projection basis"), ("base_source", "source: base case"),
 ("guidance_source", "source: guidance"), ("catalysts_source", "source: catalysts"),
 ("actual_source", "source: actuals"), ("reason_source", "source: management reason"),
 ("branches_with_files", "branches with files"), ("on_main", "on main"), ("notes", "notes"),
]
VALID = {"BEAT", "IN LINE", "MISS", "NO BASELINE"}


def s(v):
    if v is None: return NF
    if isinstance(v, (list, dict)): v = json.dumps(v, ensure_ascii=False)
    v = re.sub(r"\s+", " ", str(v)).strip()
    return v if v else NF


def norm_period(p):
    p = s(p).upper().replace(" ", "")
    if "Q4" in p: return PERIODS[0]
    if "Q1" in p: return PERIODS[1]
    if "Q2" in p or "H1" in p: return PERIODS[2]
    return None


def norm_result(r):
    r = s(r).upper().replace("-", " ").replace("_", " ").replace("INLINE", "IN LINE")
    for v in ("NO BASELINE", "IN LINE", "BEAT", "MISS"):
        if r.startswith(v): return v
    return "NO BASELINE"


def main():
    cm = json.load(open(os.path.join(WORK, "company_map.json"), encoding="utf-8"))
    os.makedirs(os.path.join(DEST, "companies"), exist_ok=True)
    rows, problems, comp = [], [], {}
    for t in sorted(cm):
        p = os.path.join(WORK, "out", f"{t}.json")
        if not os.path.exists(p):
            problems.append(f"{t}: no extraction output; rows written as NOT FOUND")
            d = {"ticker": t, "name": cm[t]["name"].lstrip("?") or NF, "rows": []}
        else:
            try:
                d = json.load(open(p, encoding="utf-8"))
            except Exception as e:
                problems.append(f"{t}: unreadable JSON ({e})"); d = {"ticker": t, "rows": []}
        d["ticker"] = t
        byp = {}
        for r in d.get("rows", []):
            k = norm_period(r.get("period"))
            if k and k not in byp: byp[k] = r
        fad = s(d.get("first_analysis_date"))
        m = re.match(r"(\d{4}-\d\d-\d\d)", fad)
        d["framework_date"] = (("before" if m.group(1) < "2026-09-08" else "after") if m else NF)
        for k, opts in (("board", ("SME", "main")), ("reporting", ("quarterly", "half-yearly"))):
            raw = s(d.get(k)); low = raw.lower()
            hit = [o for o in opts if low.startswith(o.lower())]
            if not hit or raw != hit[0]:
                d[k + "_source"] = f"{s(d.get(k + '_source'))} [as recorded: {raw}]"
            d[k] = hit[0] if hit else NF
        d["src_identity"] = " | ".join(f"{k}: {s(d.get(k + '_source'))}" for k in ("board", "reporting", "archetype"))
        d["src_first"] = f"first: {s(d.get('first_analysis_source'))} | verdict: {s(d.get('verdict_source'))}"
        comp[t] = d
        for per in PERIODS:
            r = dict(byp.get(per, {})); r["period"] = per
            r["result_vs_base"] = norm_result(r.get("result_vs_base"))
            row = {}
            for key, _ in COLS:
                row[key] = s(r.get(key)) if key in r else s(d.get(key))
            rows.append(row)
        src_md = os.path.join(WORK, "out_md", f"{t}.md")
        body = open(src_md, encoding="utf-8", errors="replace").read() if os.path.exists(src_md) else f"# {t}\n\nNo excerpts extracted.\n"
        sx = os.path.join(WORK, "session_excerpts", f"{t}.md")
        if os.path.exists(sx) and os.environ.get("APPEND_RAW_SESSIONS") == "1":  # off by default: raw chat text stays local
            x = open(sx, encoding="utf-8", errors="replace").read()
            if x.count("\n## ") > 0:
                body += "\n\n---\n\n## Raw session-history excerpts (script output, extract_sessions.py)\n\n" + x.split("\n", 1)[1]
        open(os.path.join(DEST, "companies", f"{t}.md"), "w", encoding="utf-8").write(body)
    with open(os.path.join(DEST, "census.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow([h for _, h in COLS])
        for r in rows: w.writerow([r[k] for k, _ in COLS])

    # ---- gaps
    idx = {r["run"]: r for r in json.load(open(os.path.join(WORK, "corpus", "run_index.json"), encoding="utf-8"))}
    g_nobase, g_noact, g_onebranch, g_local = [], [], [], []
    tally_rows = collections.Counter(r["result_vs_base"] for r in rows)
    best = {}
    rank = {"MISS": 3, "BEAT": 2, "IN LINE": 1, "NO BASELINE": 0}
    percomp = collections.defaultdict(list)
    for r in rows: percomp[r["ticker"]].append(r)
    comp_any = collections.Counter()
    for t, rs in percomp.items():
        res = {r["result_vs_base"] for r in rs}
        for v in VALID:
            if v in res and not (v == "NO BASELINE" and res != {"NO BASELINE"}): comp_any[v] += 1
        if res == {"NO BASELINE"}: g_nobase.append(t)
        if all(r["actual_revenue"] == NF and r["actual_profit"] == NF and r["actual_margin"] == NF for r in rs): g_noact.append(t)
        e = cm[t]
        brs = set()
        for run in e["runs"]:
            brs |= set(idx.get(run, {}).get("branches", []))
        if e["runs"] and len(brs) == 1: g_onebranch.append((t, sorted(brs)[0], ", ".join(e["runs"])))
        if not e["runs"] or (not brs): g_local.append((t, len(e["qr_dirs"])))
    with open(os.path.join(DEST, "gaps.md"), "w", encoding="utf-8") as f:
        f.write(f"# Gaps - results census 2026-11 ({LAPTOP})\n\nFacts only. A company can appear in more than one list.\n\n")
        f.write(f"## 1. No baseline in any of the three periods ({len(g_nobase)} companies)\n\n")
        f.write("No like-for-like base case of ours exists in the files read, or the base case is full-year only and no file compares the period to it, or it was written after the result. See the `basis of result call` column per row.\n\n")
        f.write(", ".join(g_nobase) + "\n\n")
        f.write(f"## 2. No actuals in any of the three periods ({len(g_noact)} companies)\n\n" + ", ".join(g_noact) + "\n\n")
        f.write(f"## 3. Repo files on one branch only ({len(g_onebranch)} companies)\n\n| ticker | branch | run folders |\n|---|---|---|\n")
        for t, b, r in g_onebranch: f.write(f"| {t} | {b} | {r} |\n")
        f.write(f"\n## 4. No repo run folder on any pushed branch; local files only ({len(g_local)} companies)\n\n| ticker | Quarterly Reviewer folders |\n|---|---|\n")
        for t, n in g_local: f.write(f"| {t} | {n} |\n")
        f.write(f"\n## 5. Extraction problems ({len(problems)})\n\n" + ("\n".join(f"- {p}" for p in problems) if problems else "None.") + "\n")
        extra = os.path.join(WORK, "gaps_extra.md")
        if os.path.exists(extra): f.write("\n" + open(extra, encoding="utf-8").read())

    # ---- sources
    inv = json.load(open(os.path.join(WORK, "inventory.json"), encoding="utf-8"))
    brs = inv["branches"]
    ss = json.load(open(os.path.join(WORK, "session_excerpts", "_summary.json")))
    files_read = collections.Counter()
    for d in comp.values():
        for x in d.get("files_read", []) or []:
            x = str(x)
            k = "repo (origin/...)" if x.startswith("origin/") else "Quarterly Reviewer" if "QuarterlyReviewer" in x else \
                "Concall pipeline" if "Concall" in x else "session history" if x.startswith("session") else "other local"
            files_read[k] += 1
    ncorp = sum(len(fs) for _, _, fs in os.walk(os.path.join(WORK, "corpus")))
    qr_dirs = sum(len(e["qr_dirs"]) for e in cm.values())
    with open(os.path.join(DEST, "sources.md"), "w", encoding="utf-8") as f:
        f.write(f"# Sources - results census 2026-11 ({LAPTOP})\n\n")
        f.write("## A. Repo\n\n")
        f.write(f"- Remote branches listed after `git fetch --all`: {len(brs)} "
                f"(run/*: {sum(b.startswith('origin/run/') for b in brs)}, claude/*: {sum(b.startswith('origin/claude/') for b in brs)}, "
                f"other: {sum(not b.startswith(('origin/run/', 'origin/claude/')) for b in brs)})\n")
        f.write(f"- Run folders found across all branches: {len(inv['runs']) - 1} (excluding runs/_template); on main: {sum(1 for r in idx.values() if r['on_main'])}; not on main: {sum(1 for r in idx.values() if not r['on_main'])}\n")
        f.write(f"- companies/*.md files across all branches: {len(inv['companies'])} paths\n")
        f.write(f"- Text files exported for reading with git cat-file (no checkout): {ncorp}\n")
        f.write("- Files kept per full run: manifest.yaml, run-log.md, step1-business-brief.md, outputs/final/*.md, outputs/qa/*.md, outputs/reports for stages 10 and later (assembly, valuation, synthesis, thesis, devil's advocate). Per quarterly folder: review, audit, ledger, notion payload, run log, SOURCES.md. Excluded: PDFs, CSVs, YAML blocks, full-text extracts, forensic notes, stage 01-09 reports.\n")
        f.write("- LESSONS_ARCHIVE.md and LESSONS.md read from origin/main.\n\n")
        f.write("## B. Claude Code session history\n\n")
        f.write(f"- .jsonl files read: {ss['jsonl_files']}; with user/assistant text: {ss['sessions_with_text']}; with company excerpts: {ss['sessions_with_hits']}\n")
        f.write(f"- Excerpts saved: {ss['excerpts']}. Script: extract_sessions.py (user and assistant text only; tool calls and tool results skipped). Per-session list: sessions_index.tsv\n\n")
        f.write("## C. Local folders\n\n")
        f.write(f"- Quarterly Reviewer: C:\\QuarterlyReviewer\\QuarterlyReviewer\\reviews, {len(set(os.path.basename(os.path.dirname(q)) for e in cm.values() for q in e['qr_dirs']))} batch folders, {qr_dirs} company folders, {sum(1 for e in cm.values() if e['qr_dirs'])} companies\n")
        f.write("- Concall pipeline: C:\\ConcallPipeline\\Daily Concall Intelligence\\Q2 FY27 Results (top-level .md files searched per company)\n\n")
        f.write("## Files cited by the per-company extraction (files_read lists)\n\n")
        for k, v in files_read.most_common(): f.write(f"- {k}: {v}\n")
        f.write(f"\n## Census size\n\n- Companies: {len(cm)}\n- Rows: {len(rows)} (three periods per company)\n")
        f.write("- Rows by result: " + ", ".join(f"{k} {tally_rows[k]}" for k in ("MISS", "IN LINE", "BEAT", "NO BASELINE")) + "\n")
        f.write("- Companies with at least one row of each result (NO BASELINE counts only companies with no other result): "
                + ", ".join(f"{k} {comp_any[k]}" for k in ("MISS", "IN LINE", "BEAT", "NO BASELINE")) + "\n")
        extra = os.path.join(WORK, "sources_extra.md")
        if os.path.exists(extra): f.write("\n" + open(extra, encoding="utf-8").read())
    for fn in ("inventory.py", "export_corpus.py", "build_map.py", "extract_sessions.py", "assemble.py", "AGENT_BRIEF.md", "aliases.json"):
        p = os.path.join(WORK, fn)
        if os.path.exists(p):
            os.makedirs(os.path.join(DEST, "tools"), exist_ok=True); shutil.copy(p, os.path.join(DEST, "tools", fn))
    sx = os.path.join(WORK, "session_excerpts", "_sessions.tsv")
    if os.path.exists(sx): shutil.copy(sx, os.path.join(DEST, "sessions_index.tsv"))
    print("companies", len(cm), "rows", len(rows))
    print("rows by result", dict(tally_rows))
    print("companies by result", dict(comp_any))
    print("problems", len(problems)); [print("  ", p) for p in problems[:40]]


if __name__ == "__main__":
    main()
