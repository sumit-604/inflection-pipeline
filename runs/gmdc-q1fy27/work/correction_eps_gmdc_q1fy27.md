# EXTRACTION CORRECTION MEMO — GMDC Q1FY27 EPS

**Status:** VERIFIED and RESOLVED by orchestrator (mechanical extraction check, not analysis).
**Trigger:** A2 enumerator flagged two `OCR_SUSPECT` EPS figures where the pdftotext
text layer produced a "2" that was inconsistent with Basic=Diluted parity in every
other column and with the cross-table summary/detailed figures.

## Method
The A1 extract used the pdftotext text layer (all 10 pages passed the char-count
test, so no OCR was run at A1). For the four EPS cells in question, the orchestrator
rendered the source pages to 300-DPI PNG (`pdftoppm`) and OCR'd them (`tesseract`)
to read the actual printed glyph. GMDC has no dilutive instruments, so Basic must
equal Diluted in every column; every non-current column already shows that parity.

## Resolution (source of truth = rendered page image)
| Statement | Table | Text-layer read | TRUE value (rendered image) |
|---|---|---|---|
| Standalone | Summary (page 3) | Basic 5.13 / Diluted 5.13 | 5.13 / 5.13 (already correct) |
| Standalone | Detailed (page 4) | Basic 5.13 / Diluted **2.13** | Basic 5.13 / Diluted **5.13** |
| Consolidated | Summary (page 3) | Basic **2.14** / Diluted 5.14 | Basic **5.14** / Diluted 5.14 |
| Consolidated | Detailed (page 6) | Basic 5.14 / Diluted 5.14 | 5.14 / 5.14 (already correct) |

**Authoritative EPS for Q1 FY27 (quarter ended 30 Jun 2026), not annualised:**
- Standalone: Basic = Diluted = **Rs 5.13** per share (face value Rs 2)
- Consolidated: Basic = Diluted = **Rs 5.14** per share (face value Rs 2)

The stray "2.13" (standalone detailed Diluted) and "2.14" (consolidated summary
Basic) are text-layer glyph misreads of "5.13" and "5.14". Use 5.13 / 5.14.

## Instruction to downstream agents (A3, A4, A5)
Treat 5.13 (standalone) and 5.14 (consolidated) as the correct Q1FY27 EPS. Do NOT
raise a Basic-vs-Diluted divergence finding for this quarter; there is none. The A1
extract line-number spine is otherwise trusted; only these EPS cells are corrected
here, and only for the current-quarter column.
