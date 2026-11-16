#!/usr/bin/env python3
"""Compute operating-profit growth and the label for extracted result rows.

Input: a JSON list of rows as described in ../README.md (fields copied from the
results statement or the review table, as printed, with the unit).
Output: a JSON list with the computed columns of growth.csv.

    python label_rows.py extracted_rows.json computed_rows.json

Rule: operating profit before tax = PBT before exceptional items - other income
(- share of associates/JV when that share sits inside the PBT line).
Lenders: PBT - treasury gains where both years are stated, else reported PBT
(mark LENDER-REPORTED). After tax = x (1 - 25.17%). Growth = this / last - 1.
"""
import json,glob,re,csv,os,collections
def num(s):
    if s is None: return None
    s=s.strip()
    if not s or re.search(r"NOT FOUND|UNREADABLE|NOT STATED|^ND$|N\.?A\.?$",s,re.I): return None
    if re.fullmatch(r"(NIL|-|–|—|0|0\.0+|\(0\.0+\))",s,re.I): return 0.0
    t=s.replace(",","").replace("₹","").replace("Rs.","").replace("Rs","").strip()
    neg=bool(re.match(r"^\(\s*[\d.]",t)) or t.startswith("-") or t.startswith("−")
    m=re.search(r"\d+(?:\.\d+)?",t)
    if not m: return None
    v=float(m.group(0)); return -v if neg else v
def factor(unit):
    u=unit.lower()
    if "lakh" in u or "lac" in u: return 0.01,"lakh"
    if "million" in u or re.search(r"\bmn\b",u): return 0.1,"million"
    if "thousand" in u or "'000" in u: return 1e-5,"thousand"
    if "crore" in u or re.search(r"\bcr\b",u): return 1.0,"crore"
    return None,unit
TAX=0.2517
ONEOFF={("WELCORP","Q1FY27"):("547.93","0","gain on sale of associate shares shown as a separate line inside PBT")}
def core_ok(e,lender):
    ks=["pbt_before_exceptional_cur","pbt_before_exceptional_prev"]+([] if lender else ["other_income_cur","other_income_prev"])
    return all(num(e.get(k)) is not None for k in ks)
def calc(e,ticker,period):
    fx,un=factor(e.get("unit",""))
    if fx is None or ("lakh" in e.get("unit","").lower() and re.search(r"\bcr\b|crore",e.get("unit","").lower())): return None,"unit not single or not stated"
    lender=e.get("is_lender","").upper().startswith("Y") and ticker!="SHAREINDIA"
    if not core_ok(e,lender): return None,"PBT or other income missing"
    g=lambda k: num(e.get(k))
    pc,pp=g("pbt_before_exceptional_cur"),g("pbt_before_exceptional_prev"); oc,op_=g("other_income_cur"),g("other_income_prev")
    marks=[]
    if lender:
        tc,tp=g("treasury_gains_cur"),g("treasury_gains_prev")
        if tc is not None and tp is not None: a,b=pc-tc,pp-tp; marks.append("LENDER: PBT less "+e.get("treasury_label","treasury gains")[:50]); so=(tc,tp)
        else: a,b=pc,pp; marks.append("LENDER-REPORTED"); so=(None,None)
    else: a,b=pc-oc,pp-op_; so=(oc,op_)
    inc=e.get("share_included_in_pbt","").upper()
    sc,sp=g("share_assoc_cur"),g("share_assoc_prev"); shr=""
    if inc.startswith("Y"):
        if sc is not None and sp is not None: a-=sc; b-=sp; shr=f"{sc*fx:.2f} / {sp*fx:.2f}"
        else: marks.append("share of associates inside PBT, amount not available; not removed")
    if (ticker,period) in ONEOFF:
        c1,p1,why=ONEOFF[(ticker,period)]; a-=num(c1); b-=num(p1); marks.append(f"one-off removed: {why} ({c1} / {p1} as filed)")
    c=lambda v: "" if v is None else f"{v*fx:.2f}"
    o=dict(basis=e.get("basis",""),reporting=e.get("reporting",""),unit_as_filed=e.get("unit",""),pbt_cr=c(pc),pbt_prev_cr=c(pp),other_income_cr=c(so[0]),other_income_prev_cr=c(so[1]),
           exceptional_cr=c(g("exceptional_cur")),exceptional_prev_cr=c(g("exceptional_prev")),share_assoc_excluded_cr=shr,
           op_pbt_cr=c(a),op_pbt_prev_cr=c(b),op_pat_cr=f"{a*fx*(1-TAX):.2f}",op_pat_prev_cr=f"{b*fx*(1-TAX):.2f}",growth_pct="",results_file=e.get("file",""),page=e.get("page",""),notes=e.get("notes",""))
    if un!="crore": o["original_figures"]=f"Rs {un}: PBT {e.get('pbt_before_exceptional_cur')} / {e.get('pbt_before_exceptional_prev')}; other income {e.get('other_income_cur')} / {e.get('other_income_prev')}; exceptional {e.get('exceptional_cur')} / {e.get('exceptional_prev')}; PAT {e.get('pat_cur')} / {e.get('pat_prev')}"
    A,B=a*fx,b*fx; gr=None
    if B>0: gr=(A/B-1)*100; o["growth_pct"]=f"{gr:.1f}"
    if A<0: lab="LOSS"
    elif B<=0 and A>0: lab="TURNAROUND"
    elif B<=0: lab="LOSS"
    elif B<1.0: lab="LOW BASE"
    elif gr>25: lab="ABOVE 25%"
    elif gr>=0: lab="0 TO 25%"
    else: lab="FELL"
    o["label"]=lab
    qc,qp=g("pat_cur"),g("pat_prev"); o["reported_pat_cr"]=c(qc); o["reported_pat_prev_cr"]=c(qp)
    o["reported_profit_growth_pct"]=(f"{(qc/qp-1)*100:.1f}" if qc is not None and qp is not None and qp>0 else ("n/m" if qc is not None and qp is not None else ""))
    o["mark"]="; ".join(marks); o["_gr"]=gr
    return o,None


if __name__ == "__main__":
    import sys
    rows = json.load(open(sys.argv[1], encoding="utf-8"))
    out = []
    for e in rows:
        e = {k: ("" if v is None else str(v)) for k, v in e.items()}
        res, err = calc(e, e.get("ticker", ""), e.get("period", ""))
        if res is None:
            res = {"label": "NO FILING", "notes": err}
        res.pop("_gr", None)
        out.append({"ticker": e.get("ticker"), "period": e.get("period"), **res})
    json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), indent=1)
    print(len(out), "rows")
