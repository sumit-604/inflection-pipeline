
## A1 EXTRACTOR — both GATE A1 PASS
- results: 9 pp, 100% coverage, no OCR, units Crores x1. extract_results_atlantaelec_q1fy27.txt (512 lines, 9 markers).
- presentation: 30 pp, 100% coverage, OCR pages [2,5,10,15,23,26], units Crores x1. extract_presentation_atlantaelec_q1fy27.txt (918 lines, 30 markers).

## NOTION — fetched live 2026-07-21
- Page: "Atlanta Electricals Ltd". Decision Status: WATCHLIST / BUY ON DIPS (14 May 2026).
- Entry zone Rs 1,104-1,243; MoS Rs 883-994. Base FV Rs 2,157.
- Thesis-broken triggers + SBPDCL yellow flag + Voltamp sector signal + 10-item Section 8 monitoring checklist captured in work/notion_thesis_pack.md and passed inline to A3/A4.

## A2 ENUMERATOR — launched (both background)

## EXTRACTION-QUALITY HALT + REMEDY (orchestrator, mechanical)
- A2 results ledger flagged pervasive OCR_GARBLED cells across the core financial table.
- Root cause: results PDF is a SCANNED filing with a CORRUPT embedded text layer. A1 char-count heuristic (>100 chars/page) gave a FALSE PASS; pdftotext returned garbage numbers (e.g. Revenue text-layer "4633|7762 31511" vs true 466.33/747.62/315.11; prior-yr qtr rev mis-rendered "3sa1"~358.1 vs true 315.11; "Changes in Inventories" row lost).
- Verification: fresh pdftoppm@400dpi + tesseract on page 6 recovers clean, decimal-correct numbers.
- Remedy per NON-NEGOTIABLE RULE 4 (text layer not trusted; OCR mandatory): re-run A1 for results with FORCED OCR on all 9 pages; then re-run A2 on the clean spine. Presentation extract unaffected (already OCR'd its low-char slides).

## A2 ENUMERATOR results — GATE A2 PASS (on original extract; see note)
- Count test all match: 5 notes / 24 line items / 9 zero-standing / 2 agenda / 13 auditor paras / 3 entities.
- BUT ledger built on garbled text layer -> superseded by forced-OCR re-extract; A2 will re-run on clean spine.

## A2 ENUMERATOR presentation — GATE A2 PASS
- 30 slides / 148 metrics / 11 footnotes / 17 people / 10 milestones = 186 disclosure units. Counts re-verified.
- Flags: DEFINITION_MISMATCH (EBITDA incl/excl Other Income slides 7/9 vs 27), PERIOD_LABEL_CHECK (FY26 RoCE on Q1FY27 slide), TABLE_STRUCTURE_DIFFERS (slide 29 vs 9), DATA_PLACEHOLDER [TBU] slide 16, DIN_NOT_DISCLOSED slide 13, LAYOUT_AMBIGUOUS charts.

## IN FLIGHT
- A1 results forced-OCR re-extract (background).
- A3 presentation forensics (background).
