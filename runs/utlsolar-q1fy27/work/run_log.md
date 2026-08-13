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
- A2 results: PENDING
