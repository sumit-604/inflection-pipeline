# Quarterly Analysis Run Log — IPCL Q1 FY27

**Ticker:** IPCL (INVPRECQ / BSE 504786) — Investment & Precision Castings Ltd
**Quarter:** Q1 FY27, quarter ended 30 June 2026 (filed 13.08.2026)
**Run date:** 2026-08-13
**Branch:** claude/quarterly-results-analysis-dwprvc

## Toolchain precheck
pdftotext / pdfinfo / pdftoppm / tesseract — MISSING at start; installed
poppler-utils + tesseract-ocr (apt; broken deadsnakes/ondrej PPAs removed to
let update proceed). All four verified present.

## Documents supplied (2 PDFs)
- `inputs/ipcl_q1fy27_results_full_7pg.pdf` (7 pages, 2.6MB, iLovePDF producer)
  — COMPLETE Reg 33 filing: BSE cover letter + standalone & consolidated
  results tables (rotated landscape image pages 3-4) + standalone auditor
  report + consolidated auditor report. **Doctype: results. AUTHORITATIVE.**
- `inputs/ipcl_q1fy27_results_subset_6pg.pdf` (6 pages, 2.0MB)
  — SUBSET of the 7-page file: identical content minus the page-1 BSE cover
  letter (its pages 1-6 == full file pages 2-7; identical rotated results
  tables and identical auditor-report text layers). **Duplicate; not run as a
  separate chain to avoid double-counting.** Retained in inputs/ for audit.

## Document-class detection
Both PDFs = `results` (Reg 33 / "Unaudited Financial Results" / SRE 2410
auditor review markers). No concall, no presentation supplied.
=> Role 4 runs (filing). Role 5 (concall) does NOT run this quarter.

## Notion thesis (fetched live 2026-08-13; page as of 2026-06-22, upd 10-Jul-26)
- **Decision Status: AVOID** at CMP ₹724
- Entry zone: raw ₹190-240; governance-adjusted ₹162-204; MoS ₹190; Entry Max 240
- Gate 0: 52/160 AVERAGE (Core 44/100, Moat 8/60); EM 36/80 STRENGTHENING
- Promoter Verdict: **CONCERN** (MD comp ₹4.32 Cr = 36.7% FY26 PAT ₹11.77 Cr;
  1% Guarantee Commission on sanctioned bank credit conflicts with deleveraging)
- Destination PE 22.7-23.8x (applied 21-24x) vs current 61.6x; prob-wtd CAGR
  -13.6% (Role 1) / -8.9% (FTTCP)
- **Q1 FY27 (Aug 2026) = BINDING pre-committed trigger.** Thresholds:
  EBITDA ≥ ₹9.5 Cr · A&D order book ≥ ₹100 Cr · Power & Fuel < 9.5% of revenue
- Monitoring: item 3 (External Processing / job work) RED (31%→33% of COS);
  item 9 (borrowings toward ₹50 Cr) Amber
- Re-evaluation triggers: (a) CMP < ₹240 (b) MD comp restructured (c) Q1 FY27 results
- FY26 base: TOI ₹165→189 Cr (+14%); PBILDT margin 13.92%→16.80%; PAT margin
  3.67%→6.22%; solar P&F intensity FY25 12.0%→FY26 10.5%→Q4 FY26 9.8%

## Sequence
Single results doc: A1 -> A2 -> A3 (gated) -> A4 (Role 4 only) -> A5 -> Notion save -> commit.

## Gate log
- (pending)
