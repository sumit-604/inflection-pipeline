# PDF re-read brief (second pass). Read GROWTH_BRIEF.md first: same fields, same rules, same output JSON shape.

Differences for this pass:
- Your batch is `g2batches/g2batch_NN.json`. Each row lists `pdfs` (original PDF files) and a `hint` from the first pass
  (which file and page the first reader used, and its note). The first pass worked from extracted text that was
  image-only, garbled or OCR-damaged for this row.
- You must read the figures from the PDF PAGE IMAGES: use the Read tool on the PDF with the `pages` parameter
  (e.g. pages "5-7"; at most 20 pages per call). Find the page with the statement of profit and loss (consolidated if the
  filing has one, else standalone). The hint page is usually right or within 1-3 pages. If a row has several PDFs,
  pick the one that is the Reg 33 results filing for the period (results / board outcome / approval of results).
- Copy digits exactly as printed on the page image. Do NOT repair, reconcile or infer digits. If a digit is unreadable on
  the image, write NOT FOUND for that value and say so.
- Do not look at the first pass's numbers (you are an independent second reader). Do not open gout/.
- `page` = the PDF page number you read (1-based page of the PDF file). `file_cite` = the `cite` of the PDF you used.
- If none of the PDFs holds the results statement for this period: status NO FILING, say what the PDFs are.
- Write `gout2/<key>.json` (same keys as the brief). Validate with json.load. Helper scripts go in a folder named after your
  batch under the scratchpad parent, never in `retro`.
Final reply: one line per row: `key | status | basis | pbt this/last | other income this/last | unit | pdf page`.
