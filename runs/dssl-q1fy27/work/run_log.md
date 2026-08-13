# Run Log — DSSL Q1 FY27 Quarterly Review

Pipeline: /run-quarterly (five-agent extraction-first)
Run date: 2026-08-13
Ticker: DSSL (Dynacons Systems & Solutions Ltd; BSE 532365 / NSE DSSL)
Quarter: Q1 FY27 (quarter ended 30-Jun-2026)

## Setup
- Toolchain precheck: pdftotext/pdfinfo/pdftoppm all MISSING at start; tesseract MISSING.
  Installed poppler-utils + tesseract-ocr via apt-get (main Ubuntu repos; third-party
  PPAs 403 but irrelevant). All four tools now OK.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md,
  Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md.
- Documents supplied: 1 PDF.
- Document-class detection: PDF is a Reg 33 / Reg 30 Board Outcome filing with
  Unaudited Financial Results + Limited Review Report -> doctype = results.
  6 pages. Per-page char test 1701-4599 chars/page, text layer trustworthy
  (A1 confirms OCR need).
- Run folder: runs/dssl-q1fy27/ (inputs/ work/). Source copied to
  inputs/results_dssl_q1fy27.pdf.

## Company memory / Notion (fetched live 2026-08-13)
- No companies/DSSL.md on disk (link in Notion points to it; not committed locally).
- Notion page fetched: "Dynacons Systems & Solutions Ltd".
  - Decision Status: WATCHLIST / BUY ON DIPS.
  - CMP (as of thesis) Rs1,231.6; conservative entry zone Rs851-1,064; MoS Rs851.
    CMP ~16% above zone top -> not buyable at CMP; Q1 FY27 print is the binary buy trigger.
  - Gate 0 GOOD 78/160; Emerging Moat 22.7/80 MODEST. Evidence gate PROCEED WITH CAVEATS,
    confidence 84. FTTCP +3 DEEP WATCH. Devil WEAKENED BUT ALIVE.
  - FY26 baseline: revenue Rs1,424cr (+12%), EBITDA margin 10.25%, PAT Rs84.78cr (+17%).
    Order book Rs2,964cr (2.08x); +NPCI Rs267.58cr on 28-Jul-2026 -> pro-forma ~Rs3,232cr.
    RBI private-cloud win Rs750.82cr.
  - Flags: FLAG-CASH (structural WC intensity, cash multiplier 1.00x); promoter CAUTION
    (2019 SEBI settlement + Cybercons Infosec subsidiary/associate contradiction);
    accounting quality 4/10. Sector cap 30x (data centres & cloud).
  - Thesis-broken triggers:
    1. Q1 FY27 EBITDA margin near 9% (<11%) for two consecutive quarters. green>=11%, red<9%.
    2. Debtor days >160 with 1-2yr overdue bucket widening on frozen Rs0.14cr ECL.
       green debtor days <=154, overdue flat/shrinking, ECL topped up.
    3. RBI Rs750.82cr order cancelled/materially slipped.
    4. HARD OVERRIDE: any Cybercons consolidated restatement -> promoter CONCERN, verdict AVOID.
  - Monitoring checklist (6): EBITDA margin; trade receivables/ECL & debtor days;
    RBI order go-live; order book / book-to-bill; annuity mix / leverage D/E;
    Cybercons classification.

## Agent progress
- A1 extractor: PASS (6/6 pages, no OCR, units Lakhs x0.01). Cybercons Infosec Pvt Ltd named as subsidiary in consolidated LRR.
- A2 enumerator: dispatched.
