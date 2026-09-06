#!/usr/bin/env python3
"""Pre-extract every PDF under a run's inputs/ to page-marked .txt.

Per LESSONS.md RECURRING PATTERNS: pointing stages at page-marked text
avoids the image-render wall and keeps page anchors valid.

Usage: python3 tools/extract_pdfs.py runs/<ticker>-<date>
Writes runs/<ticker>-<date>/work/text/<subfolder>__<stem>.txt
Each page is preceded by a line: [[PAGE n]]
Prints one line per file: path, pages, chars, OK|EMPTY|FAIL
"""
import sys
import os
from pathlib import Path

from pypdf import PdfReader


def extract(pdf_path: Path, out_path: Path):
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:  # unreadable container
        return 0, 0, "FAIL:%s" % type(exc).__name__
    chunks = []
    chars = 0
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        text = text.replace("\x00", "")  # null bytes make the file read as binary
        chars += len(text)
        chunks.append("[[PAGE %d]]\n%s\n" % (i, text))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(chunks), encoding="utf-8")
    status = "OK" if chars > 200 else "EMPTY"
    return len(reader.pages), chars, status


def main():
    run = Path(sys.argv[1])
    inputs = run / "inputs"
    out_root = run / "work" / "text"
    for pdf in sorted(inputs.rglob("*.pdf")):
        sub = pdf.parent.name
        out = out_root / ("%s__%s.txt" % (sub, pdf.stem))
        pages, chars, status = extract(pdf, out)
        print("%-70s pages=%-5s chars=%-9s %s" % (
            str(pdf.relative_to(run)), pages, chars, status))


if __name__ == "__main__":
    main()
