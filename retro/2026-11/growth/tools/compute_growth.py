#!/usr/bin/env python3
"""Compute operating-profit growth and labels from the per-row extraction files.

Usage: python compute_growth.py <work_dir> <dest_dir>
  work_dir holds growth_rows.json (universe + filing candidates), census_only.json and gout/<key>.json.

Method (same for both years):
  operating profit before tax = profit before exceptional items and tax - other income
                                (- share of associates/JV when the filed PBT line includes it)
  operating profit after tax  = operating profit before tax x (1 - 25.17%)
  lenders: PBT - treasury/trading gains where the filing states them, else reported PBT (LENDER-REPORTED)
  growth = this year / last year - 1
"""
import csv, json, os, re, sys, collections

WORK, DEST = sys.argv[1], sys.argv[2]
TAX = 0.2517
NF = "NOT FOUND"
TO_CR = {"rs lakh": 1 / 100, "rs lakhs": 1 / 100, "rs lacs": 1 / 100, "rs crore": 1.0, "rs crores": 1.0, "rs cr": 1.0,
         "rs million": 1 / 10, "rs millions": 1 / 10, "rs mn": 1 / 10, "rs thousand": 1e-5, "rs thousands": 1e-5,
         "rs '000": 1e-5, "rs": 1e-7, "rs hundred": 1e-5 / 10, "rs hundreds": 1e-6, "usd million": None}
PERIODS = ["Q4 FY26", "Q1 FY27", "Q2/H1 FY27"]
LABELS = ["ABOVE 25%", "0 TO 25%", "FELL", "LOSS", "TURNAROUND", "LOW BASE", "NO FILING", "NOT COMPARABLE"]


def num(v):
    """Parse the figure at the START of a cell. Trailing remarks are ignored; a bare dash or nil is zero."""
    if v is None: return None
    t = str(v).strip().replace("−", "-").replace("–", "-").replace("—", "-")
    if not t or t.upper().startswith(("NOT FOUND", "NOT STATED", "NA", "N/A", "ND", "NONE")): return None
    t = re.sub(r"^(Rs\.?|INR|₹)\s*", "", t)
    if re.match(r"^(-{1,2}|nil)(\s|$|\()", t, re.I): return 0.0
    m = re.match(r"^(\()?\s*(-)?\s*(\d[\d,]*(?:\.\d+)?|\.\d+)\s*(\))?", t)
    if not m: return None
    x = float(m.group(3).replace(",", ""))
    return -x if (m.group(1) or m.group(2)) else x


def tnum(v):
    """Lender treasury/trading gain = the 'net gain on fair value changes' figure. Derecognition gains are not removed."""
    if v is None: return None
    tot, found = 0.0, False
    for seg in str(v).split(";"):
        if re.search(r"derecogn", seg, re.I) or re.match(r"\s*\(e\)", seg): continue
        seg = re.sub(r"^\s*\([a-z]\)\s*", "", seg.strip())
        x = num(seg)
        if x is None:
            m = re.search(r"(\()?\s*(-)?\s*(\d[\d,]*(?:\.\d+)?)\s*(\))?\s*$", seg.strip())
            if m: x = float(m.group(3).replace(",", "")) * (-1 if (m.group(1) or m.group(2)) else 1)
        if x is not None: tot += x; found = True
    return tot if found else None


def unit_factor(u):
    k = re.sub(r"[^a-z' 0]", "", str(u).lower().replace("₹", "rs").replace("inr", "rs").replace("in ", " ")).strip()
    k = re.sub(r"\s+", " ", k)
    for name in sorted(TO_CR, key=len, reverse=True):
        if k.startswith(name) or k == name: return TO_CR[name]
    for word, f in (("lakh", 1 / 100), ("lac", 1 / 100), ("crore", 1.0), ("million", 1 / 10), ("mn", 1 / 10), ("thousand", 1e-5), ("000", 1e-5)):
        if word in k: return f
    return None


def fmt(x, nd=2):
    return NF if x is None else f"{x:.{nd}f}"


def pct(a, b):
    if a is None or b is None or b <= 0: return None
    return (a / b - 1) * 100


CORE = ("pbt_before_exceptional_this", "pbt_before_exceptional_last", "other_income_this", "other_income_last")


def load(key, folder, problems):
    p = os.path.join(WORK, folder, key + ".json")
    if not os.path.exists(p): return {}
    try: return json.load(open(p, encoding="utf-8"))
    except Exception as e:
        problems.append(f"{key}: unreadable {folder} file ({e})"); return {}


def usable(g):
    if not g or str(g.get("status", "")).upper().startswith("NO FILING"): return False
    return num(g.get("pbt_before_exceptional_this")) is not None


def opvals(g):
    """Operating profit before tax (Rs Cr) for this year and last year from one read."""
    f = unit_factor(g.get("unit", ""))
    lender = str(g.get("is_lender", "NO")).upper().startswith("Y")
    inc = str(g.get("share_included_in_pbt_line", "NA")).upper() == "YES"
    out = []
    for yr in ("this", "last"):
        pbt = num(g.get(f"pbt_before_exceptional_{yr}")); oi = num(g.get(f"other_income_{yr}"))
        sh = num(g.get(f"share_of_associates_jv_{yr}")) or 0.0
        tg = tnum(g.get(f"treasury_or_trading_gains_{yr}")) or 0.0
        if pbt is None or f is None or (oi is None and not lender): out.append(None); continue
        out.append((pbt - (tg if lender else oi) - (sh if inc else 0.0)) * f)
    return out


def close(a, b):
    if a is None or b is None: return a is None and b is None
    return abs(a - b) <= max(0.011, 0.002 * max(abs(a), abs(b)))


def main():
    rows = json.load(open(os.path.join(WORK, "growth_rows.json"), encoding="utf-8"))
    os.makedirs(DEST, exist_ok=True)
    out, problems = [], []
    DUP = {"IPCL": "INVPRECQ"}   # same company under two tickers
    keys = {(r["ticker"], r["period"]) for r in rows}
    merged_where = {}
    for r in rows:
        if r["ticker"] in DUP and (DUP[r["ticker"]], r["period"]) in keys:
            merged_where.setdefault((DUP[r["ticker"]], r["period"]), []).extend(r["where"])
    rows = [r for r in rows if not (r["ticker"] in DUP and (DUP[r["ticker"]], r["period"]) in keys)]
    for r in rows:
        r["where"] = r["where"] + merged_where.get((r["ticker"], r["period"]), [])
        g1, g2 = load(r["key"], "gout", problems), load(r["key"], "gout2", problems)
        ok1, ok2 = usable(g1), usable(g2)
        if ok2:
            g = g2
            if ok1:
                v1, v2 = opvals(g1), opvals(g2)
                same = close(v1[0], v2[0]) and close(v1[1], v2[1]) and str(g1.get("basis")).split()[0:1] == str(g2.get("basis")).split()[0:1]
                read_check = "two independent reads agree" if same else "two reads differ; page-image read used"
                if not same:
                    g = dict(g2); g["notes"] = str(g2.get("notes", "")) + " | FIRST READ (from extracted text) HAD: " + "; ".join(f"{k}={g1.get(k)}" for k in CORE) + f"; unit={g1.get('unit')}; basis={g1.get('basis')}"
            else: read_check = "page-image read only (text unusable)"
        elif ok1:
            g = g1; read_check = "single read from extracted text" + ("; page-image reader could not confirm" if g2 else "")
        else:
            g = g2 or g1; read_check = "no usable read"
        status = str(g.get("status", "NO FILING")).upper().strip() if g else "NO FILING"
        o = {"ticker": r["ticker"], "name": r["name"], "period": r["period"],
             "basis": g.get("basis", NF), "reporting": g.get("reporting", NF), "unit": g.get("unit", NF),
             "column_this": g.get("column_this", NF), "column_last": g.get("column_last", NF),
             "file": g.get("file_cite", NF), "page": g.get("page", NF), "notes": re.sub(r"\s+", " ", str(g.get("notes", ""))).strip(),
             "not_comparable_reason": g.get("not_comparable_reason", ""), "read_check": read_check}
        f = unit_factor(g.get("unit", "")) if g else None
        raw = {k: g.get(k, NF) for k in ("pbt_before_exceptional_this", "pbt_before_exceptional_last", "other_income_this", "other_income_last",
                                          "exceptional_items_this", "exceptional_items_last", "share_of_associates_jv_this", "share_of_associates_jv_last",
                                          "reported_pat_this", "reported_pat_last", "treasury_or_trading_gains_this", "treasury_or_trading_gains_last")}
        o.update({"raw_" + k: str(v) for k, v in raw.items()})
        o["pbt_line_label"] = g.get("pbt_line_label", NF); o["share_included"] = str(g.get("share_included_in_pbt_line", "NA")).upper()
        lender = str(g.get("is_lender", "NO")).upper().startswith("Y")
        o["lender"] = "YES" if lender else "NO"
        cr = {k: (((tnum(v) if k.startswith("treasury") else num(v)) * f) if ((tnum(v) if k.startswith("treasury") else num(v)) is not None and f) else None) for k, v in raw.items()}
        label, opb = None, {}
        if not g or status.startswith("NO FILING"):
            label = "NO FILING"
            if not r["candidates"]: o["notes"] = "No results filing for this period on this machine (review used a concall or other document)."
        else:
            for yr in ("this", "last"):
                pbt = cr[f"pbt_before_exceptional_{yr}"]; oi = cr[f"other_income_{yr}"]
                sh = cr[f"share_of_associates_jv_{yr}"] or 0.0
                if pbt is None: opb[yr] = None; continue
                if lender:
                    tg = cr[f"treasury_or_trading_gains_{yr}"]
                    opb[yr] = pbt - (tg or 0.0) - (sh if o["share_included"] == "YES" else 0.0)
                else:
                    if oi is None: opb[yr] = None; continue
                    opb[yr] = pbt - oi - (sh if o["share_included"] == "YES" else 0.0)
            a, b = opb.get("this"), opb.get("last")
            if status.startswith("NOT COMPARABLE"): label = "NOT COMPARABLE"
            elif f is None: label = "NO FILING"; problems.append(f"{r['key']}: unit not understood ({g.get('unit')})")
            elif a is not None and b is None and cr["pbt_before_exceptional_last"] is None and re.search(r"no .{0,60}(column|comparative)|not available|not presented|comparatives? (is|are) not|no half-year", str(g.get("notes", "")) + str(g.get("not_comparable_reason", "")), re.I):
                label = "NOT COMPARABLE"
                o["not_comparable_reason"] = o["not_comparable_reason"] or "The filing has no same-period-last-year column for this statement."
            elif a is None or b is None:
                label = "NO FILING"; o["notes"] = "Filing found but a needed figure cannot be read (PBT or other income). " + o["notes"]
            elif a <= 0: label = "LOSS"
            elif b <= 0: label = "TURNAROUND"
            elif b < 1.0: label = "LOW BASE"
            else:
                gr = pct(a, b)
                label = "ABOVE 25%" if gr > 25 else ("0 TO 25%" if gr >= 0 else "FELL")
        a, b = opb.get("this"), opb.get("last")
        o["op_pbt_this"], o["op_pbt_last"] = a, b
        o["op_pat_this"] = None if a is None else a * (1 - TAX); o["op_pat_last"] = None if b is None else b * (1 - TAX)
        o["growth"] = pct(a, b) if label not in ("NO FILING",) else None
        o["reported_growth"] = pct(cr["reported_pat_this"], cr["reported_pat_last"])
        o["cr"] = cr; o["label"] = label
        if lender and label not in ("NO FILING",):
            o["lender_note"] = "LENDER: PBT less stated treasury/trading gains" if cr["treasury_or_trading_gains_this"] is not None else "LENDER-REPORTED"
        else: o["lender_note"] = ""
        o["where"] = " ; ".join(r["where"])
        out.append(o)

    with open(os.path.join(DEST, "universe.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh); w.writerow(["ticker", "name", "period", "where the review lives"])
        for o in out: w.writerow([o["ticker"], o["name"], o["period"], o["where"]])

    def both(o, k):
        r_, c = o["raw_" + k], o["cr"][k]
        return f"{r_} {o['unit']} = Rs {c:.2f} Cr" if c is not None and "crore" not in str(o["unit"]).lower() else (f"Rs {c:.2f} Cr" if c is not None else str(r_))
    with open(os.path.join(DEST, "growth.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["ticker", "name", "period", "consolidated or standalone", "quarterly or half-yearly", "column this year", "column last year",
                    "PBT before exceptional items, this year", "PBT before exceptional items, last year", "PBT line used",
                    "other income, this year", "other income, last year", "exceptional items, this year", "exceptional items, last year",
                    "share of associates/JV, this year", "share of associates/JV, last year", "share included in PBT line (removed if YES)",
                    "lender treatment", "operating profit before tax this year (Rs Cr)", "operating profit before tax last year (Rs Cr)",
                    "operating profit after tax this year (Rs Cr)", "operating profit after tax last year (Rs Cr)", "growth %",
                    "reported PAT this year", "reported PAT last year", "reported profit growth %", "label",
                    "results file name", "page", "read check", "notes"])
        for o in out:
            w.writerow([o["ticker"], o["name"], o["period"], o["basis"], o["reporting"], o["column_this"], o["column_last"],
                        both(o, "pbt_before_exceptional_this"), both(o, "pbt_before_exceptional_last"), o["pbt_line_label"],
                        both(o, "other_income_this"), both(o, "other_income_last"), both(o, "exceptional_items_this"), both(o, "exceptional_items_last"),
                        both(o, "share_of_associates_jv_this"), both(o, "share_of_associates_jv_last"), o["share_included"], o["lender_note"],
                        fmt(o["op_pbt_this"]), fmt(o["op_pbt_last"]), fmt(o["op_pat_this"]), fmt(o["op_pat_last"]),
                        fmt(o["growth"], 1), both(o, "reported_pat_this"), both(o, "reported_pat_last"), fmt(o["reported_growth"], 1),
                        o["label"], o["file"], o["page"], o["read_check"], (o["not_comparable_reason"] + " " + o["notes"]).strip()])

    tally = collections.defaultdict(collections.Counter)
    with open(os.path.join(DEST, "names.md"), "w", encoding="utf-8") as fh:
        fh.write("# Operating profit growth by period\n\nOperating profit before tax = PBT before exceptional items, minus other income. Growth is year on year. "
                 "Lists are sorted by growth, highest first. Source of every figure: `growth.csv`.\n")
        for per in PERIODS:
            pr = [o for o in out if o["period"] == per]
            fh.write(f"\n## {per} ({len(pr)} results)\n")
            for lab in LABELS:
                ls = [o for o in pr if o["label"] == lab]; tally[per][lab] = len(ls)
                ls.sort(key=lambda o: (-(o["growth"] if o["growth"] is not None else -1e18), o["ticker"]))
                fh.write(f"\n### {lab} ({len(ls)})\n\n")
                if not ls: fh.write("None.\n"); continue
                for o in ls:
                    if lab in ("ABOVE 25%", "0 TO 25%", "FELL", "LOW BASE"):
                        extra = f": {o['growth']:+.1f}% (Rs {o['op_pbt_last']:.2f} Cr to Rs {o['op_pbt_this']:.2f} Cr)"
                    elif lab == "LOSS": extra = f": operating loss Rs {o['op_pbt_this']:.2f} Cr (last year Rs {o['op_pbt_last']:.2f} Cr)" if o["op_pbt_last"] is not None else f": operating loss Rs {o['op_pbt_this']:.2f} Cr"
                    elif lab == "TURNAROUND": extra = f": Rs {o['op_pbt_last']:.2f} Cr loss to Rs {o['op_pbt_this']:.2f} Cr profit"
                    elif lab == "NOT COMPARABLE": extra = ": " + (o["not_comparable_reason"] or o["notes"])[:200]
                    else: extra = ""
                    tag = f" [{o['lender_note']}]" if o["lender_note"] else ""
                    fh.write(f"- {o['ticker']} ({o['name']}){extra}{tag}\n")
    with open(os.path.join(DEST, "missing.md"), "w", encoding="utf-8") as fh:
        ms = [o for o in out if o["label"] == "NO FILING"]
        fh.write(f"# Results filings to fetch ({len(ms)} rows)\n\nA review exists for each row, but the results filing for that period is not on this machine, or it could not be read.\n\n| ticker | name | period | what was found | review location |\n|---|---|---|---|---|\n")
        for o in ms: fh.write(f"| {o['ticker']} | {o['name']} | {o['period']} | {o['notes'][:220].replace('|', '/')} | {o['where'][:160].replace('|', '/')} |\n")
    json.dump([{k: v for k, v in o.items()} for o in out], open(os.path.join(WORK, "growth_computed.json"), "w", encoding="utf-8"), indent=1)
    print("rows", len(out), "companies", len({o["ticker"] for o in out}))
    for per in PERIODS: print(per, sum(tally[per].values()), dict(tally[per]))
    q2 = {o["ticker"] for o in out if o["period"] == PERIODS[2] and o["label"] == "ABOVE 25%"}
    q1 = {o["ticker"]: o["label"] for o in out if o["period"] == PERIODS[1]}
    print("Q2 ABOVE 25%:", len(q2), "| also ABOVE 25% in Q1:", sum(1 for t in q2 if q1.get(t) == "ABOVE 25%"), "| with any Q1 row:", sum(1 for t in q2 if t in q1))
    print("problems", len(problems)); [print("  ", p) for p in problems[:30]]


if __name__ == "__main__":
    main()
