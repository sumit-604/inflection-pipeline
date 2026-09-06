#!/usr/bin/env python3
"""OCR one PDF to page-marked text when its text layer is missing or broken.

Some filed PDFs are page images, and some carry a custom-encoded subset font
whose extracted "text" is glyph codes rather than characters. Either way pypdf
returns nothing usable. This renders each page with pdftoppm and reads it with
tesseract, writing the same [[PAGE n]] format tools/extract_pdfs.py produces so
stage prompts and page anchors are unchanged.

Usage: python3 tools/ocr_pdf.py <input.pdf> <output.txt> [dpi]
"""
import subprocess
import sys
import tempfile
from pathlib import Path


def page_count(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    raise SystemExit("could not read page count from pdfinfo")


def main():
    pdf = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    dpi = sys.argv[3] if len(sys.argv) > 3 else "200"
    total = page_count(pdf)
    chunks = []
    with tempfile.TemporaryDirectory() as td:
        for n in range(1, total + 1):
            stem = Path(td) / ("p%d" % n)
            subprocess.run(
                ["pdftoppm", "-r", dpi, "-f", str(n), "-l", str(n), "-png",
                 str(pdf), str(stem)],
                check=True, capture_output=True)
            pngs = sorted(Path(td).glob("p%d-*.png" % n)) or sorted(
                Path(td).glob("p%d.png" % n))
            text = ""
            if pngs:
                res = subprocess.run(
                    ["tesseract", str(pngs[0]), "stdout", "-l", "eng", "--psm", "1"],
                    capture_output=True, text=True)
                text = res.stdout
                pngs[0].unlink()
            chunks.append("[[PAGE %d]]\n%s\n" % (n, text.replace("\x00", "")))
            if n % 25 == 0:
                print("  ...ocr page %d/%d" % (n, total), flush=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(chunks), encoding="utf-8")
    body = "".join(chunks)
    print("%s pages=%d chars=%d" % (out_path, total, len(body)))


if __name__ == "__main__":
    main()
