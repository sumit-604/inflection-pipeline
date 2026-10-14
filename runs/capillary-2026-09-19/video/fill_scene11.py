"""Fill scene 11 placeholders from scenario-rebuild-page64.md ONLY, and cross-check every
EBITDA / PAT figure used in scene 11 against the file (3 cases x 4 years, 5% tolerance).
Exit code 2 = STOP (file missing or a figure differs by more than 5%). Never estimates."""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "outputs" / "final" / "scenario-rebuild-page64.md"
TOL = 0.05

# Figures printed in the job prompt (scene 11, table A and the paths table, plus bear/bull EBITDA).
PROMPT = {
    "bear": {"ebitda": [161, 195, 230, 268], "pat": [43, 64, 86, 109]},
    "base": {"ebitda": [172, 244, 321, 405], "pat": [51, 101, 154, 212], "rev30": 1324},
    "bull": {"ebitda": [186, 303, 431, 512], "pat": [62, 144, 236, 293]},
}

def num(s):
    return float(s.replace(",", "").replace("%", "").strip())

def parse_case(text, case):
    sec = re.search(rf"^### {case}\s*$(.*?)(?=^###|^---|^## )", text, re.S | re.M | re.I)
    if not sec:
        raise SystemExit(f"STOP: case '{case}' not found in {SRC.name}")
    rows = {}
    for line in sec.group(1).splitlines():
        if line.startswith("|") and not set(line) <= set("|- "):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows[cells[0].lower()] = cells[1:]
    return rows

def main():
    if not SRC.exists():
        print(f"STOP: {SRC} is missing. Not rendering."); sys.exit(2)
    text = SRC.read_text(encoding="utf-8")
    report, bad = [], []
    parsed = {c: parse_case(text, c) for c in ("Bear", "Base", "Bull")}
    for case in ("bear", "base", "bull"):
        rows = parsed[case.capitalize()]
        f_e = [num(x) for x in rows["total adj. ebitda"]]
        f_p = [num(x) for x in rows["pat"]]
        for key, file_vals in (("ebitda", f_e), ("pat", f_p)):
            for i, (pv, fv) in enumerate(zip(PROMPT[case][key], file_vals)):
                diff = abs(pv - fv) / fv
                ok = diff <= TOL
                report.append((case, key, f"FY{27+i}", pv, fv, round(diff * 100, 2), ok))
                if not ok: bad.append(report[-1])
    base = parsed["Base"]
    rev = [num(x) for x in base["total revenue"]]
    rev_r = [int(round(v + 1e-9)) for v in rev]       # nearest crore (1,323.5 -> 1,324)
    if abs(rev_r[3] - PROMPT["base"]["rev30"]) / rev[3] > TOL:
        bad.append(("base", "rev", "FY30", PROMPT["base"]["rev30"], rev[3], 0, False))
    ebitda, pat = PROMPT["base"]["ebitda"], PROMPT["base"]["pat"]
    vals = {
        "REV27": rev_r[0], "REV28": rev_r[1], "REV29": rev_r[2], "REV30": rev_r[3],
        "M": [round(ebitda[i] / rev_r[i] * 100, 1) for i in range(4)],
        "PM": [round(pat[i] / rev_r[i] * 100, 1) for i in range(4)],
        "EBITDA": ebitda, "PAT": pat,
        "BEAR_PAT": PROMPT["bear"]["pat"], "BULL_PAT": PROMPT["bull"]["pat"],
        "file_margins_for_reference": [num(x) for x in base["adj. ebitda margin"]],
        "source": f"{SRC.relative_to(HERE.parent.parent.parent)} (commit 60d653a8)",
    }
    for r in report:
        print("%-5s %-6s %s prompt=%-5s file=%-7s diff=%5.2f%% %s" % (*r[:6], "OK" if r[6] else "FAIL"))
    if bad:
        print("STOP: figures differ by more than 5%:", bad); sys.exit(2)
    (HERE / "scene11_values.json").write_text(json.dumps(vals, indent=1), encoding="utf-8")
    print(json.dumps(vals))
    print("fill_scene11: PASS, wrote scene11_values.json")

if __name__ == "__main__":
    main()
