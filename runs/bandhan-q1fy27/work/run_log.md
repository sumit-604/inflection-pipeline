# RUN LOG — BANDHAN Q1 FY27 quarterly review

Run date: 2026-07-22. Quarter detected: Q1 FY27 (quarter ended June 30, 2026).
Orchestrator: /run-quarterly. Pipeline v1.0.

## Toolchain precheck
- pdftotext, pdfinfo, pdftoppm, tesseract: INSTALLED (poppler-utils + tesseract-ocr installed this session). PASS.
- Python pymupdf/pdfplumber also available (not the evidence spine; A1 uses pdftotext -layout).

## Protocol files (all present)
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md  ✓
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md ✓
- frameworks/Master_Project_Prompt_v3.3.md ✓

## Documents supplied and classification
1. 5f02af59...pdf (13 pg) -> RESULTS. Board Outcome (Reg 30) + Reg 33 Unaudited
   Financial Results (standalone) + Independent Auditor Review Report + KMP changes.
   -> inputs/results_bandhan_q1fy27.pdf
2. 74bc2d63...pdf (48 pg) -> PRESENTATION. Earnings Update Presentation (Ref 096).
   -> inputs/presentation_bandhan_q1fy27.pdf
3. Pasted transcript -> CONCALL. Q1 FY27 earnings call, saved verbatim.
   -> inputs/concall_bandhan_q1fy27.txt
4. bbeaa33b...pdf (3 pg) -> SUBSUMED. Abridged Board Outcome cover letter (Ref 095),
   fully contained within doc #1 (same Mantri resignation, KMP, AGM text). Retained
   as inputs/boardoutcome_abridged_bandhan_q1fy27.pdf for reference; NOT run
   separately to avoid double-counting. Confirmed subset by content diff.

## Company memory / Notion
- companies/BANDHAN.md: ABSENT. No prior Inflection coverage.
- Prior runs for ticker: NONE.
- Notion: greenfield — no pre-existing company page / Decision Status / tripwires.
  This is a fresh quarterly review, not a monitor against a committed thesis.
  Fetch attempt logged below.

## Immediate orchestrator-level flags (pre-analysis, to be verified by subagents)
- CFO Rajeev Mantri RESIGNED (KMP exit); Vinay Jain appointed Interim CFO eff.
  Sep 26 2026 to Mar 31 2027. Yet Mantri presented this concall. -> A3 F-check.
- ROA guidance CUT: 1.6-1.8% (exit Q4FY27) -> 1.2-1.4%. Management attributes to
  external factors (energy crisis, funding cost, tech cost). -> A4 to assess.
