#!/usr/bin/env python3
"""
ar_section.py -- split an extracted annual-report text file into two slices so
that AR-reading stages can be routed to the slice they need instead of
re-ingesting the whole report every time.

WHY THIS EXISTS
    The annual report is the largest single input (~250-270k tokens) and it is
    read in full by several stages that only need part of it: stage 2 (notes)
    needs the financial statements and notes; stages 4 and 7 (business model,
    emerging moat) need the business / MD&A front matter. Feeding each of them
    the whole report is pure waste. This tool cuts the report once, up front,
    at the one boundary every Indian annual report shares.

THE SLICES (exact text, nothing paraphrased, page markers carried through)
    AR_front.txt      start .. Independent Auditor's Report
                      Business overview, MD&A, Director's Report, Chairman's
                      letter, corporate governance, front matter.
    AR_financial.txt  Independent Auditor's Report .. EOF
                      Auditor's report(s) (standalone + consolidated), the face
                      financial statements, and EVERY note (accounting policies,
                      RPT, contingent liabilities, receivables ageing, segment
                      schedule, and the rest). Statements are kept alongside the
                      notes on purpose so the notes stage can still cross-check
                      note figures against the main statements.

THE BOUNDARY
    The first line that begins the Independent Auditor's Report. In an Indian
    annual report the auditor's report always sits between the business front
    matter and the financial statements, so this single, universal heading
    splits the document cleanly. When both standalone and consolidated sections
    exist, the FIRST auditor's report (standalone) is the split point, which
    keeps ALL financial content -- both standalone and consolidated -- together
    in AR_financial.txt.

FAIL SAFE (the point of the whole design)
    If a confident boundary is not found, NO slice files are written; the script
    prints a line beginning "FALLBACK" with the reason and exits 0. The caller
    (stage 0 of the pipeline) must then route every stage to the full annual
    report -- exactly today's behaviour. A slice is NEVER allowed to silently
    starve a stage of content. Losing the optimisation is fine; losing content
    is not.

USAGE
    python3 tools/ar_section.py <extracted_AR.txt> [--outdir DIR]
        default outdir: <dir-of-input>/AR_sections/
    Exit 0 on both success and fail-safe fallback (both are valid outcomes).
    Exit 2 only on a usage error (missing input file).

Byte-exact: the file is read and written as latin-1, which round-trips all 256
byte values, so the slices are byte-for-byte substrings of the source even when
the extraction contains non-UTF8 bytes.
"""

import os
import re
import sys

# A detected boundary must fall within this fraction of the document. A split at
# 2% or 98% means detection latched onto the wrong line; fall back instead.
MIN_FRAC = 0.10
MAX_FRAC = 0.90


def norm_key(raw_line):
    """Flatten one raw (latin-1-decoded) line to a lowercase ASCII match key.

    The file is read as latin-1 to keep the slices byte-exact, but that turns a
    UTF-8 curly apostrophe (bytes E2 80 99) into three junk characters, which
    breaks naive heading matching. Recover the real unicode first, then reduce
    every non-alphanumeric run to a single space so that "Independent Auditor's
    Report" and "INDEPENDENT AUDITORS' REPORT" both normalise to the same key
    "independent auditor s report".
    """
    try:
        u = raw_line.encode("latin-1").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        u = raw_line
    return re.sub(r"[^a-z0-9]+", " ", u.lower()).strip()


def find_boundary(lines):
    """Return (index, method) of the line that starts the Independent Auditor's
    Report -- the boundary between business front matter and the financial
    statements + notes -- or (None, reason) if it is not confidently found.

    The auditor's report is the ONLY boundary used. It is universal in Indian
    annual reports and sits exactly between the two halves we want to separate.
    When it cannot be found inside the sane middle band, we return None so the
    caller falls back to the full AR rather than risk a wrong cut.
    """
    n = len(lines)
    lo, hi = int(n * MIN_FRAC), int(n * MAX_FRAC)

    for i, line in enumerate(lines):
        key = norm_key(line)
        # Heading-anchored: the line must BEGIN with "independent auditor" so a
        # mid-sentence reference in the Director's Report is not mistaken for
        # the section start. First such line inside the band wins, which picks
        # the standalone auditor's report and keeps consolidated content (which
        # comes later) in the financial slice too.
        if key.startswith("independent auditor") and "report" in key:
            if lo <= i <= hi:
                return i, "auditor-report"

    return None, ("Independent Auditor's Report heading not found within the middle %d-%d%% of the document" % (int(MIN_FRAC * 100), int(MAX_FRAC * 100)))


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        sys.stderr.write(__doc__)
        return 2
    src = argv[1]
    outdir = None
    if "--outdir" in argv:
        outdir = argv[argv.index("--outdir") + 1]
    if not os.path.isfile(src):
        sys.stderr.write("ar_section: input file not found: %s\n" % src)
        return 2
    if outdir is None:
        outdir = os.path.join(os.path.dirname(os.path.abspath(src)), "AR_sections")

    with open(src, "r", encoding="latin-1") as fh:
        text = fh.read()
    # keepends so re-joining is byte-exact
    lines = text.splitlines(keepends=True)
    total = len(lines)

    if total < 200:
        # Too short to be a real annual report (likely a scanned/failed
        # extraction). Do not slice; let the stage read whatever exists.
        print("FALLBACK: source has only %d lines; too short to slice safely, route stages to the full AR" % total)
        return 0

    idx, method = find_boundary(lines)
    if idx is None:
        print("FALLBACK: %s; route stages to the full AR" % method)
        return 0

    front = "".join(lines[:idx])
    financial = "".join(lines[idx:])

    os.makedirs(outdir, exist_ok=True)
    front_path = os.path.join(outdir, "AR_front.txt")
    fin_path = os.path.join(outdir, "AR_financial.txt")
    with open(front_path, "w", encoding="latin-1") as fh:
        fh.write(front)
    with open(fin_path, "w", encoding="latin-1") as fh:
        fh.write(financial)

    fb = len(front.encode("latin-1"))
    nb = len(financial.encode("latin-1"))
    total_b = fb + nb

    index_path = os.path.join(outdir, "index.txt")
    with open(index_path, "w", encoding="latin-1") as fh:
        fh.write("source: %s\n" % os.path.abspath(src))
        fh.write("boundary_method: %s\n" % method)
        fh.write("boundary_line: %d of %d (%.0f%%)\n" % (idx + 1, total, 100.0 * idx / total))
        fh.write("AR_front.txt:     lines 1-%d, %d bytes, ~%dk tokens\n" % (idx, fb, round(fb / 4000)))
        fh.write("AR_financial.txt: lines %d-%d, %d bytes, ~%dk tokens\n" % (idx + 1, total, nb, round(nb / 4000)))
        fh.write("\nROUTING (stage 0 uses this):\n")
        fh.write("  stage 2 notes        -> AR_financial.txt (full AR on demand for accounting-policy front matter)\n")
        fh.write("  stage 4 business     -> AR_front.txt      (AR_financial.txt on demand for a segment/financial note)\n")
        fh.write("  stage 7 emerging moat-> AR_front.txt      (AR_financial.txt on demand)\n")
        fh.write("  stage 3 AR deep dive -> FULL AR           (unchanged, whole-document read)\n")
        fh.write("  verifier A           -> FULL source PDFs  (unchanged, source-fidelity gate)\n")

    print("OK boundary=%s at line %d/%d (%.0f%%)" % (method, idx + 1, total, 100.0 * idx / total))
    print("  AR_front.txt      %8d bytes  ~%3dk tok  %s" % (fb, round(fb / 4000), front_path))
    print("  AR_financial.txt  %8d bytes  ~%3dk tok  %s" % (nb, round(nb / 4000), fin_path))
    print("  full AR           %8d bytes  ~%3dk tok" % (total_b, round(total_b / 4000)))
    print("  index             %s" % index_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
