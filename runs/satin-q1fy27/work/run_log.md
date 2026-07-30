# Run Log — SATIN Q1 FY27 Quarterly Review

**Orchestrator:** /run-quarterly
**Company:** Satin Creditcare Network Limited (NSE: SATIN, BSE: 539404)
**Quarter:** Q1 FY27 (quarter ended June 30, 2026)
**Run date:** 2026-07-30
**Sector:** Financials / NBFC-MFI (lending business — 1L/5L variants per protocol v1.2)

## Setup / prechecks
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md — PASS
- Toolchain: pdftotext, pdfinfo, pdftoppm, tesseract — installed at session start (poppler-utils + tesseract-ocr), all present — PASS
- Company memory companies/SATIN.md: ABSENT (no local per-company file; Notion is the memory of record)

## Document-class detection (from content, not filename)
| Input file | Pages (pdfinfo) | Class markers | Doctype |
|---|---|---|---|
| results_satin_q1fy27.pdf (3b8c3101) | 15 | "Outcome of the Board Meeting", Reg 30/33/52/63, "Un-Audited Financial Results (Standalone & Consolidated)", Limited Review Report by J C Bhalla & Co. | **results** |
| pressrelease_satin_q1fy27.pdf (830bd6ba) | 6 | "Sub: Press Release", Reg 30, "Satin Creditcare Reports Consolidated PAT of Rs 123 Crores in Q1 FY27, 172% up YoY", 20th profitable quarter | **press release** (enumerated under `presentation` doctype) |
| presentation_satin_q1fy27.pdf (e9bac09e) | 42 | "Sub: Investor Presentation", Reg 30, slide structure | **presentation** |

No concall transcript supplied. Role 4 (results) runs in full; Role 5 (concall) is N.A. this run (no transcript). Press release and investor presentation feed Role 4 as company-narrative corroboration.

## Notion live-fetch (Decision Status verified before any framing)
Page: "Satin Creditcare Network" (id 38fbb2b9-d3ab-8106-9639-d7e1e9d39d57), fetched 2026-07-30.
See thesis_brief_notion.md for the inline brief passed to A3/A4.

## Gate results
### GATE A1 (page coverage 100%) — ALL PASS
- results: 15/15 pages, unit Lakhs (x0.01 -> Cr), text-native
- press release: 6/6 pages, unit Crores, text-native
- presentation: 42/42 slides, unit Crores, 6 slides OCR'd (2,4,13,28,34,42 dividers)

### GATE A2 (count test) — ALL PASS
- results: 32 notes / 1 Board agenda item / 2 statements (SA+CONSOL) / 2 auditor reports / 6 entities / 144 line items. FLAG: source text-layer corrupt on Reg 52(4) tables (page 13 standalone, page 14 consolidated) -> A1 OCR-repair invoked.
- press release: 112 units (44 bullets / 19 table rows / 2 footnotes / 10 headings / 6 pages / 20 prose / 11 grep-confirmed-absent). FLAG: NNPA, gross write-off, cost of funds, cost/income, PAR buckets absent from PR (ZERO_STANDING).
- presentation: 42 slides / 240 line items. FLAGS: slide16 Active Clients "xx" placeholder (company artifact), SGAL no metrics disclosed, DELTA_OMITTED on ratio tables + income statements, CHART_LAYOUT_AMBIGUOUS on 8 chart slides.

### Extraction repair
- A1 targeted OCR-repair of results pages 13-14 (Reg 52(4)) at 400 DPI invoked before A3/A4 rely on consolidated asset-quality ratios. Recoverable consolidated figures confirmed: Net worth Rs 2,943.62 Cr, PAT Rs 122.65 Cr, EPS 11.45/11.15, D/E 3.97x, debt/assets 0.78, net profit margin 16.04%.

