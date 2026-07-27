# AEROFLEX Q1 FY27 — Quarterly Pipeline Run Log

Run date: 2026-07-27. Ticker: AEROFLEX (Aeroflex Industries Limited, Scrip 543972 / NSE AEROFLEX). Quarter: Q1 FY27 (ended June 30, 2026).

## 0. Setup and prechecks
- Arguments: TICKER=AEROFLEX; 3 docs supplied.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md. OK.
- Document class detection:
  - 3d6e46ec* (10pp) -> results (Board Outcome Reg 30/33 + financial results + LRRs + Reg 30 tax-auditor disclosure). Renamed inputs/results_aeroflex_q1fy27.pdf.
  - aece38fc* (3pp) -> results-class supplementary: Reg 32 Statement of Deviation/Variation in fund utilisation. Renamed inputs/reg32_deviation_aeroflex_q1fy27.pdf.
  - ae5a3d4d* (28pp) -> presentation (investor presentation Q1 FY27). Renamed inputs/presentation_aeroflex_q1fy27.pdf.
  - No concall transcript supplied. Role 5 (concall) not run this cycle.
- Company memory: no companies/AEROFLEX.md file; no prior run folder. Notion page EXISTS (Aeroflex Industries, id 345bb2b9-d3ab-804c-9f04-d7c8117a2f84) — fetched live, thesis snapshot saved to work/_notion_thesis_snapshot.md. Decision Status WATCHLIST / HOLD-NOT-ADD.

## TOOLCHAIN DEVIATION (disclosed)
- pdftotext / pdfinfo / pdftoppm / tesseract are NOT installed; apt-get install poppler-utils/tesseract FAILED (mirror 404, security.ubuntu.com). The Read tool's PDF rendering also requires poppler (pdftoppm) and was unavailable.
- Substitution used: PyMuPDF 1.28.0 (pip-installed) for text-layer extraction AND for rasterising pages (no poppler dependency). This produces a genuine line-numbered text-layer evidence spine (NOT the Read-tool rendering the protocol forbids).
- All three PDFs are text-based (825-2181 chars/page). Text layer was CLEAN for: reg32 (all 3pp), presentation (all 28pp), and the results filing's PROSE pages (1,2,3,7 cover letter + LRR narrative).
- The results filing's SCANNED financial-statement/table pages (4,5,6,8,9,10) had a GARBLED embedded text layer (e.g. "2,s89_39", "1,90t89", "L479.31") — char-count test PASSES but content is corrupted. This is the qualitative-OCR-failure trap. Fallback: pages rasterised at 220 dpi with PyMuPDF and transcribed by vision-OCR; every number cross-checked against the standalone/consolidated cross-foot and the deck. Presentation chart slides 7 and 10 had positionally-scrambled data labels -> vision-OCR'd.
- GATE A1: page coverage 100% for both extract files (results 10pp + reg32 3pp; presentation 28pp).

## Cross-checks logged at extraction
- Consolidated PAT Q1FY27 1,879.31 L = standalone PAT 1,905.89 L minus Hyd-Air subsidiary loss 26.58 L. Subsidiary is loss-making (revenue 765.66 L, PAT (26.58) L). Standalone > Consolidated.
- Deck consolidated Total Income 145.97 Cr = filing 14,597.38 L; deck consolidated PAT 18.79 Cr = filing 1,879.31 L. Reconcile.
- Only ONE subsidiary consolidates: Hyd-Air Engineering Pvt Ltd (page 3). Italica Global FZC (Notion RPT concern) is a fellow subsidiary, not consolidated here.

## Pipeline steps
- A1 EXTRACTOR: done by orchestrator via PyMuPDF+vision (toolchain-forced). Extracts: extract_results_*.txt, extract_presentation_*.txt. GATE A1 PASS.
- A2 ENUMERATOR: dispatched (results, presentation) — running.
- A3 FORENSICS: pending A2 gates.
- A4 ANALYST: pending.
- A5 ADVERSARY: pending.

## Notion save (2026-07-27, after A5 COMPLETE, user-authorised)
- Page: Aeroflex Industries (id 345bb2b9-d3ab-804c-9f04-d7c8117a2f84), COMPANIES MASTER db.
- update_properties: PREPENDED dated [27-Jul-26] Q1 FY27 Key Notes entry; all 6 prior entries preserved. Decision Status LEFT UNCHANGED (WATCHLIST / HOLD-NOT-ADD) — no trigger fired.
- insert_content (position end, 3 sequential inserts): full Q1 FY27 review as Notion tables — headline consol/standalone, growth-quality/skid economics, watchlist status, tripwire test, governance, 14 Questions-for-Management, monitorables, verdict, plain-language callout, A3 forensics findings table, A5 COMPLETE verdict.
- A5 verdict COMPLETE; protocol verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE.
