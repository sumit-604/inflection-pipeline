import re
base = "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-aequs-q2fy27-f2613d/runs/aequs-q2fy27/"
ft = open(base + "extracted/aequs-presentation-q2fy27-fulltext.md", encoding="utf8").read().split("\n")
def L(n): return ft[n-1]

rows = {"N": [], "E": [], "F": [], "D": [], "Q": []}
for ln in open(base + "work/rows.txt", encoding="utf8"):
    ln = ln.rstrip("\n")
    if not ln: continue
    t, p, l, v, c = ln.split("|", 4)
    l = int(l[1:]) if l.startswith("S") else int(l)
    rows[t].append((int(p), l, v, c))

tok = re.compile(r"\(?>?[\d,\.]+%?\)?(?: bps)?|\(>100 ?%\)|\(>100 bps\)|—")
def vals(s):
    # extract numeric tokens after label
    return re.findall(r"\(>100%\)|\(>100 bps\)|\(?\d[\d,]*\.?\d*%?\)?|—", s)

# P/L page 16, supplement lines 1114-1131
pl_cols7 = ["Q2 FY27", "Q2 FY26", "YoY change (Q2)", "Q1 FY27", "H1 FY27", "H1 FY26", "YoY change (H1)"]
pl_cols5 = ["Q2 FY27", "Q2 FY26", "Q1 FY27", "H1 FY27", "H1 FY26"]
for n in range(1114, 1132):
    s = L(n)
    m = re.match(r"^(.*?)\s+(\(?>?\d.*)$", s)
    label, rest = m.group(1), m.group(2)
    v = vals(rest)
    cols = pl_cols7 if len(v) == 7 else pl_cols5
    assert len(v) in (5, 7), (n, s, v)
    for c, x in zip(cols, v):
        rows["N"].append((16, n, x, "consolidated P/L %s, %s (Rs Mn)" % (label, c)))
# Balance sheet supplement 1146-1182
for n in range(1146, 1183):
    s = L(n)
    m = re.match(r"^([A-Za-z][A-Za-z ,\-&/\(\)]*?)\s+(\d[\d,]*)\s+(\d[\d,]*)$", s)
    if m:
        rows["N"].append((17, n, m.group(2), "balance sheet %s, 30 Sep 2026 (Rs Mn)" % m.group(1)))
        rows["N"].append((17, n, m.group(3), "balance sheet %s, 31 Mar 2026 (Rs Mn)" % m.group(1)))
# Cash flow layout lines 496-517
cf_lines = range(496, 518)
pending = None
for n in cf_lines:
    s = L(n).strip()
    if not s or s.startswith("Particulars"): continue
    if s.startswith("Proceeds from issue of equity"):
        pending = "Proceeds from issue of equity shares (net of treasury shares)"; continue
    m = re.match(r"^(.*?)\s+(\(?[\d,]+\)?|—)\s+(\(?[\d,]+\)?|—)$", s)
    if not m: continue
    lab = pending if pending and m.group(1) == "" else m.group(1)
    lab = lab or pending
    if pending and s.startswith("—"):
        lab = pending
    pending = None
    for per, x in (("H1 FY27", m.group(2)), ("H1 FY26", m.group(3))):
        rows["N"].append((18, n, x, "cash flow %s, %s (Rs Mn)" % (lab, per)))
# handle the equity row: line starts with dash
for n in cf_lines:
    s = L(n).strip()
    if s.startswith("—") and "1,282" in s:
        rows["N"].append((18, n, "—", "cash flow Proceeds from issue of equity shares, H1 FY27 (Rs Mn)"))
        rows["N"].append((18, n, "1,282", "cash flow Proceeds from issue of equity shares, H1 FY26 (Rs Mn)"))

def flag(v):
    return " ZERO_STANDING" if v.strip() in ("—", "0", "-") else ""

# fix: dedupe equity row if regex also matched it
seen = set(); out_n = []
for r in rows["N"]:
    k = (r[0], r[1], r[2], r[3])
    if k in seen: continue
    seen.add(k); out_n.append(r)
rows["N"] = out_n

# ordered by page, line within type
names = {"N": "NUMBER", "E": "ENTITY", "F": "FORWARD", "D": "DATE", "Q": "QUALIFIER"}
idn = 0
body = []
counts = {}
for t in ["N", "F", "D", "Q", "E"]:
    rs = sorted(rows[t], key=lambda r: (r[0], r[1])) if t == "N" else rows[t]
    counts[t] = len(rs)
    body.append("\n## %s TABLE (%d rows)\n" % (names[t], len(rs)))
    for p, l, v, c in rs:
        idn += 1
        extra = flag(v) if t == "N" else ""
        if t == "N" and v.strip() == "—" and "ZERO_STANDING" not in c: c += ""
        body.append("R%03d | page %d | line %d | %s | %s | %s%s" % (idn, p, l, names[t], v, c, extra))
hdr = """=== A1 STRUCTURED EXTRACTION ===
source: Aequs_Q2FY27_Investor_Presentation.pdf (doctype presentation, quarter Q2 FY27)
fulltext: runs/aequs-q2fy27/extracted/aequs-presentation-q2fy27-fulltext.md (line anchors refer to that file)
unit_convention: Rs Mn (millions); conversion to Rs Crores x0.1 (values NOT converted here)
row_id_range: R001-R%03d
counts: NUMBER %d | FORWARD %d | DATE %d | QUALIFIER %d | ENTITY %d
anchor_note: pages 7,11,12,14,15,16,17,19 interleave columns under -layout; P/L, balance sheet and key metrics rows anchor to the raw-order supplement at file end (lines 889+). Chart-page rows anchor to layout lines; value-to-period assignments on charts follow axis order and are flagged where ambiguous.
dedup_note: chart pages show some values twice (layout and supplement); each atomic value is one row.
materiality: presentation deck; cert list, address blocks, disclaimer, IR contacts grouped as SUMMARY rows (ENTITY-SUMMARY / QUALIFIER summary).
""" % (idn, counts["N"], counts["F"], counts["D"], counts["Q"], counts["E"])
open(base + "extracted/aequs-presentation-q2fy27-structured.md", "w", encoding="utf8").write(hdr + "\n".join(body) + "\n")
print(idn, counts)
