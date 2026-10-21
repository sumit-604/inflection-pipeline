#!/usr/bin/env python3
"""Build a section index for an annual report's page-marked text cache.

Input: the .txt written beside the annual-report PDF by tools/extract_pdfs.py
(one "[page N]" marker line per page; the TOOLING GATE format).
Output: <same stem>.index.yaml beside it, mapping four canonical sections to
page and line ranges with a confidence flag:

  financials_and_notes  Independent Auditor's Report .. end (statements + all notes)
  mdna                  Management Discussion and Analysis
  governance            Directors' / Board's Report and Corporate Governance Report
  business_overview     front matter before MD&A and the Directors' Report

RULES (quality-neutral by design)
- Generous slices: every range is widened by one page at each end.
- A heading counts only near the top of a page (first 12 non-blank lines) and
  only as a short line; a mention inside prose is not a section start.
- A section whose heading is not found is written with confidence: low and the
  full range. The orchestrator then routes that stage to the FULL text.
- The full text is always the fallback of record; the index never removes it.

Usage: python3 tools/ar_index.py <annual-report.txt> [--print]
Exit 0 on success and on low-confidence output; exit 2 on a usage error.
"""
import re
import sys
from pathlib import Path

PAGE = re.compile(r"^\[page (\d+)\]$")
PATTERNS = {
    "auditor": re.compile(r"^independent auditor s report\b"),
    "mdna": re.compile(r"^management s? ?discussion (and|&)? ?analysis\b|^management discussion and analysis\b"),
    "directors": re.compile(r"^(directors|board s|boards) report\b|^report of the (board of )?directors\b"),
    "governance": re.compile(r"^(report on )?corporate governance( report)?\b"),
    "brsr": re.compile(r"^business responsibility (and sustainability )?report\b"),
}


def key(line):
    return re.sub(r"[^a-z0-9&]+", " ", line.lower().replace("’", "'").replace("'", " ")).strip()


def load(path):
    pages = []  # (page_no, first_line_no, [lines])
    cur = None
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
        m = PAGE.match(line.strip())
        if m:
            cur = [int(m.group(1)), n, []]
            pages.append(cur)
        elif cur is not None:
            cur[2].append(line)
    return pages


def first_heading(pages, name, lo=0.0, hi=1.0):
    total = len(pages)
    for i, (pno, _, lines) in enumerate(pages):
        if not (lo <= i / max(total, 1) <= hi):
            continue
        top = [l for l in lines if l.strip()][:12]
        for l in top:
            k = key(l)
            if len(k) <= 80 and PATTERNS[name].search(k):
                return i
    return None


def rng(pages, a, b, total_lines):
    a = max(0, a - 1)
    b = min(len(pages) - 1, b + 1)
    first_line = pages[a][1]
    last_line = pages[b + 1][1] - 1 if b + 1 < len(pages) else total_lines
    return {"pages": "%d-%d" % (pages[a][0], pages[b][0]), "lines": "%d-%d" % (first_line, last_line)}


def build(path):
    pages = load(path)
    if not pages:
        return {"error": "no [page N] markers; route every stage to the full text"}
    total_lines = len(path.read_text(encoding="utf-8", errors="replace").split("\n"))
    last = len(pages) - 1
    aud = first_heading(pages, "auditor", 0.10, 0.95)
    mdna = first_heading(pages, "mdna", 0.0, 0.9)
    dirs = first_heading(pages, "directors", 0.0, 0.9)
    gov = first_heading(pages, "governance", 0.0, 0.9)
    brsr = first_heading(pages, "brsr", 0.0, 0.95)
    full = rng(pages, 0, last, total_lines)
    out = {"source": path.name, "full": full, "sections": {}}
    s = out["sections"]

    def sec(name, start, end, ok, note=""):
        if ok and start is not None and end is not None and end >= start:
            r = rng(pages, start, end, total_lines)
            r.update({"confidence": "high", "note": note})
        else:
            r = dict(full)
            r.update({"confidence": "low", "note": note or "heading not found; use the full text"})
        s[name] = r

    sec("financials_and_notes", aud, last, aud is not None, "auditor's report to end of document")
    starts = sorted(x for x in (aud, mdna, dirs, gov, brsr) if x is not None)

    def end_after(i):
        nxt = [x for x in starts if x > i]
        return (nxt[0] - 1) if nxt else last

    sec("mdna", mdna, end_after(mdna) if mdna is not None else None, mdna is not None)
    g0 = min([x for x in (dirs, gov) if x is not None], default=None)
    g1 = (aud - 1) if aud is not None else None
    sec("governance", g0, g1, g0 is not None and aud is not None, "directors' report and corporate governance report")
    fm_end = min([x for x in (mdna, dirs, gov) if x is not None], default=None)
    sec("business_overview", 0, (fm_end - 1) if fm_end else None, fm_end is not None and fm_end > 0,
        "front matter before MD&A and the directors' report; read mdna with it")
    return out


def to_yaml(d, ind=0):
    pad = "  " * ind
    lines = []
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append("%s%s:" % (pad, k))
            lines.append(to_yaml(v, ind + 1))
        else:
            lines.append('%s%s: "%s"' % (pad, k, v))
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1 or not Path(args[0]).is_file():
        print(__doc__)
        sys.exit(2)
    path = Path(args[0])
    idx = build(path)
    text = "ar_index:\n" + to_yaml(idx, 1) + "\n"
    out = path.with_name(path.stem + ".index.yaml")
    out.write_text(text, encoding="utf-8")
    if "--print" in sys.argv:
        print(text)
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
