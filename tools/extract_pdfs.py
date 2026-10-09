#!/usr/bin/env python3
"""Pre-extract every PDF under a run's inputs/ to page-marked .txt.

Implements the TOOLING GATE fallback in .claude/commands/run-pipeline.md:
each PDF gets a .txt beside it (same folder, same stem) with one "[page N]"
marker line before each page's text. Stages and verifiers then read the
.txt in place of the PDF, which keeps page anchors valid and avoids the
image-render wall.

Usage: python3 tools/extract_pdfs.py runs/<ticker>-<date> [--force]
An existing .txt is kept unless --force is given.
Prints one line per PDF: path, pages, chars, OK | EMPTY | FAIL | KEPT.
Run tools/check_extraction.py afterwards; an EMPTY or flagged file needs
OCR (tools/ocr_repair.py) before any stage reads it.
"""
import sys
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
        chunks.append("[page %d]\n%s\n" % (i, text))
    out_path.write_text("".join(chunks), encoding="utf-8")
    status = "OK" if chars > 200 else "EMPTY"
    return len(reader.pages), chars, status


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv[1:]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    run = Path(args[0])
    for pdf in sorted(p for p in (run / "inputs").rglob("*") if p.suffix.lower() == ".pdf"):
        out = pdf.with_suffix(".txt")
        if out.exists() and not force:
            print("%-70s %s" % (str(pdf.relative_to(run)), "KEPT"))
            continue
        pages, chars, status = extract(pdf, out)
        print("%-70s pages=%-5s chars=%-9s %s" % (
            str(pdf.relative_to(run)), pages, chars, status))


if __name__ == "__main__":
    main()
