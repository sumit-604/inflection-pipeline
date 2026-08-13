# Run Log — UTLSOLAR Q1 FY27 Quarterly Review

Pipeline: /run-quarterly (Quarterly Analysis Agent Pipeline v1.0)
Orchestrator session start: 2026-08-13

## Setup / Prechecks
- Ticker: UTLSOLAR (Fujiyama Power Systems Ltd) | BSE 544613 / NSE UTLSOLAR
- Docs supplied: 1 PDF (uploaded), 11 pages
- Protocol files: PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract INSTALLED this session (were missing; apt-get poppler-utils + tesseract-ocr succeeded)
- Document class detection: page 1 shows Reg 30/33 Board Outcome markers ("Outcome of the Board Meeting", "Un-audited Standalone and Consolidated financial results for the Quarter ended June 30, 2026", Limited Review Report) -> classified **results**
- Quarter detected: Q1 FY27 (quarter ended 30 June 2026)
- Run folder: runs/utlsolar-q1fy27/ (inputs/ work/)

## Company Memory / Notion (fetched live 2026-08-13)
- Notion page: Fujiyama Power Systems Limited (id 367bb2b9-d3ab-81a1-b741-e2d8bab5fbad)
- Decision Status: WATCHLIST (effectively AVOID at CMP Rs.265)
- Entry zone: Rs.186 (MoS) - Rs.215 (25% CAGR); prior MoS Rs.162
- Promoter Verdict: MONITOR (upgrade to TRUSTWORTHY pending BSE-CFO verification)
- No local companies/UTLSOLAR.md yet.

## Sequence
- A1 results: DONE — GATE A1 PASS (100% coverage, 11/11 pages). Units Rs million (x0.1 to Cr).
  DATA-QUALITY FLAG: source PDF text layer degraded/garbled on pp.7-8 (Online2PDF converter).
  A1 did a manual 300dpi fidelity pass; resolved 1 ambiguous tax cell (Consol current tax FY26)
  to 885.52 by arithmetic reconciliation vs printed Total tax 1,039.04. Auditor EoM paragraph
  (fire-related) present. Board Outcome items 1-4 enumerated.
- A2 results: DONE — GATE A2 PASS. Counts: 8 notes / 29 P&L line items / 4 agenda items /
  13 auditor paras / 3 entities. Standalone-vs-consol PAT gap Q1FY27 ~nil (57.795 vs 57.794 Cr).
  KEY: first-ever consolidation; 2 new 31% associates Zayo Cables + Zayo Energy (eff 25 Apr 2026).
  Flags: FIRST_TIME_CONSOLIDATION, ENTITY_CHANGE, EOM (fire), DATE_DISCREPANCY (Note3 fire "06 May
  2025" vs auditor EoM "06 May 2026"), AMBIGUOUS_CELL (A1-resolved), SIGNATURE_TIMESTAMP_ILLEGIBLE.
- A3 results: DONE — GATE A3 PASS. F1-F17: 11 FINDING / 4 PASS / 2 N.A., no blanks.
  Top: Bawal fire EoM both reports (Rs 143.58 Cr exceptional, unmodified); Zayo associates
  consideration undisclosed; Q1FY27 PAT Rs 57.795 Cr/EPS 1.88 (fire exceptional masked strong
  operating qtr); rev +125.3% YoY; EBITDA ~19%. NO thesis-broken/red trigger fires.
  forward_signals A3-01,02,04,09,11; ambiguous A3-05,07,08,10.
- A4 analyst: PENDING
