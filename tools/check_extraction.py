#!/usr/bin/env python3
"""Report per-page text coverage for every extracted corpus file.

A file whose pages are mostly blank has no usable text layer (scanned images),
and one whose pages carry bytes that are mostly non-ASCII is a custom-encoded
subset font. Both need OCR before any stage reads them. Run this after
tools/extract_pdfs.py and before dispatching stages.

Usage: python3 tools/check_extraction.py runs/<ticker>-<date> [more runs...]
Prints only the files that fail; prints "clean" for a run with none.
"""
import re
import sys
from pathlib import Path

PAGE = re.compile(r"\[\[PAGE \d+\]\]")


def check(txt: Path):
    body = txt.read_text(encoding="utf-8", errors="replace")
    pages = PAGE.split(body)[1:]
    if not pages:
        return "no page markers"
    filled = [p for p in pages if len(p.strip()) > 50]
    coverage = len(filled) / len(pages)
    sample = "".join(filled)[:20000]
    if sample:
        ascii_share = sum(1 for c in sample if 32 <= ord(c) < 127 or c in "\n\t")
        ascii_share /= len(sample)
    else:
        ascii_share = 0.0
    if coverage < 0.5:
        return "BLANK PAGES: only %d/%d pages carry text (%.0f%%)" % (
            len(filled), len(pages), coverage * 100)
    if ascii_share < 0.85:
        return "GARBLED: %.0f%% of sampled characters are non-ASCII (custom font encoding)" % (
            (1 - ascii_share) * 100)
    return None


def main():
    for run in sys.argv[1:]:
        root = Path(run) / "work" / "text"
        bad = []
        for txt in sorted(root.glob("*.txt")):
            problem = check(txt)
            if problem:
                bad.append((txt, problem))
        print("### %s" % run)
        if not bad:
            print("  clean")
        for txt, problem in bad:
            print("  %-60s %s" % (txt.name, problem))


if __name__ == "__main__":
    main()
