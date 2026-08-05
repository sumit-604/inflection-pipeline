import re

layout_path = "presentation_layout.txt"
data = open(layout_path, encoding="utf-8", errors="replace").read()

# Split on form feed. pdftotext emits a trailing \f after the last page,
# so the split yields 40 segments; the final one is an empty artifact.
raw_pages = data.split("\f")
assert raw_pages[-1].strip() == "", f"unexpected trailing content: {raw_pages[-1]!r}"
pages = raw_pages[:-1]
assert len(pages) == 39, f"expected 39 pages, got {len(pages)}"

# OCR text for the 6 pages that fell under the 100-character threshold
ocr_text = {}
for p in ["02", "05", "10", "19", "23", "30"]:
    with open(f"ocrpg-{p}.txt", encoding="utf-8", errors="replace") as f:
        ocr_text[int(p)] = f.read().strip()

ocr_pages = sorted(ocr_text.keys())

out_lines = []
for i, content in enumerate(pages, start=1):
    out_lines.append(f"[page {i}]")
    # strip trailing/leading blank lines but keep internal structure
    content_lines = content.split("\n")
    # remove leading/trailing fully-blank lines
    while content_lines and content_lines[0].strip() == "":
        content_lines.pop(0)
    while content_lines and content_lines[-1].strip() == "":
        content_lines.pop()
    out_lines.extend(content_lines)
    if i in ocr_text:
        out_lines.append("")
        out_lines.append(f"[OCR page {i}]")
        out_lines.extend(ocr_text[i].split("\n"))
    out_lines.append("")  # blank separator before next page marker

body = "\n".join(out_lines)
open("extract_body.txt", "w", encoding="utf-8").write(body)
print("body lines:", len(out_lines))
print("ocr_pages:", ocr_pages)
