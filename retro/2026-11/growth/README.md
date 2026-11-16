# Operating-profit growth: results analysed in Q4 FY26, Q1 FY27, Q2/H1 FY27

Cloud session, 2026-11-17. Facts only. No web. No estimates.

## What is here

- `universe.csv`: every company and period for which a review exists. 505 results, 318 companies.
- `growth.csv`: one row per result with the profit lines, operating profit, growth, label, source and page.
- `names.md`: per period, the companies under each label, sorted by growth.
- `missing.md`: every NO FILING row.
- `tools/label_rows.py`: the computation. `tools/extraction_rules.md`: what was copied from each filing.
- `LAPTOP_PROMPT.md`: the prompt for the laptop session that fills the rows this session could not reach.

## Universe

| period | results |
|---|---|
| Q4 FY26 | 121 |
| Q1 FY27 | 177 |
| Q2/H1 FY27 | 207 |
| total | 505 (318 companies) |

A result is in the universe when one of these exists:
1. A repo quarterly folder for the period (`runs/<ticker>-q4fy26`, `-q1fy27`, `-q2fy27`, `-h1fy27`), on any branch.
2. A repo full-run folder whose reports carry that period's reported result (taken from the earlier census).
3. A Quarterly Reviewer review or a Concall pipeline note for Q2/H1 FY27, as cited in the laptop census (PR 245). 139 results exist only there.

Duplicates merged: IPCL into INVPRECQ, plus the merges of the earlier census.
Q4 FY26 and Q1 FY27 figures that appear only as comparison columns inside a later review are not counted as analysed results.

## Method

- Operating profit before tax = profit before tax and exceptional items, less other income. Share of associates and joint ventures is removed when it sits inside the PBT line.
- Operating profit after tax = operating profit before tax x (1 - 25.17%).
- Growth = this period / same period last year - 1. Quarterly reporters: quarter against the same quarter. Half-yearly reporters: half year against the same half.
- Consolidated where filed, otherwise standalone. The row says which.
- Lenders: PBT less the treasury line where the statement prints it for both years; otherwise reported PBT, marked LENDER-REPORTED.
- Both years come from the same statement.
- Labels: ABOVE 25%, 0 TO 25%, FELL, LOSS, TURNAROUND, LOW BASE (last year under Rs 1 Cr; growth still shown), NO FILING, NOT COMPARABLE.
- One named one-off was removed: WELCORP Q1 FY27, gain on sale of associate shares shown as its own line inside PBT.

## Where each number came from (`number source` column)

| source | rows | meaning |
|---|---|---|
| FILING TEXT | 146 | read from the results statement text stored in the repo; clean |
| FILING TEXT, OCR DAMAGED | 77 | read from damaged statement text; some digits or decimal points were restored by the reader. Marked NOT VERIFIED |
| REVIEW TABLE | 33 | taken from the table our review copied from the filing (operator ruling, 2026-11-17) |
| PDF PAGE IMAGE | 18 | read from the original PDF page in the 20-row check |
| NONE | 92 | review is in the repo, but neither the statement for the period nor a review table with PBT and other income for both years is there. NO FILING |
| LAPTOP ONLY | 139 | review is only in the Quarterly Reviewer or Concall folder on the laptop. NO FILING here |

The `results file or review file` column gives `<branch>:<run folder>/<path>`; `page or line` gives the PDF page, or the line range where the stored text has no page marker.

## 20-row check

Twenty rows were drawn at random (seed 20261117) from the 260 rows with numbers and a PDF in the repo. A separate reader, who did not see the first numbers, read the statement from the PDF page image.

- 18 of 18 checkable rows matched: same growth to 0.1 percentage point and same label.
- 2 rows could not be checked: the original results PDF is not in the repo (KARNIKA Q2 FY27, RAYMONDREL Q2 FY27; only a transcription is stored).
- 5 of the 18 were OCR DAMAGED rows; all 5 matched.
- 1 of the 18 was a REVIEW TABLE row (ECOSMOBLTY Q1 FY27). Its growth matched, but the rupee figures in the review table were ten times too small against the PDF. The row now carries the PDF figures. Other REVIEW TABLE rows may have the same unit problem; their growth percentage is not affected by it, their rupee values may be.

## Limits

- 231 of 505 rows are NO FILING in this session: 139 laptop-only, 92 unreadable or absent in the repo.
- 77 rows rest on damaged text and are marked NOT VERIFIED.
- Lakh, million and thousand figures were converted to crore; `original figures` shows the figures as filed.
- LOW BASE and TURNAROUND rows can show very large percentages. Read the rupee values.
- No holdings, prices paid or position sizes are in these files.
