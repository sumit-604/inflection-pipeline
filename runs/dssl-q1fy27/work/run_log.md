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
- A2 enumerator: PASS (7 count tests reconciled: 5 notes, 2 agenda, 3 entities, 13 segment rows, 11 auditor paras, 36 line items, 5 sigs). Flagged page-5 OCR_MISALIGNMENT (column-to-value scramble), new segment "Technology Workforce Augmentation Services" w/ restated priors, Consol-LRR paras 2/4/5 dropped, unlabeled OCI row, no balance sheet/receivables in filing.
- ORCHESTRATOR OCR FALLBACK (rule 4): page-5 combined P&L re-extracted via 400dpi tesseract + 200dpi image Read + arithmetic reconciliation. Verified reference at work/scratch_page5_verified.md. A1 re-invoked to append corrected page-5 block + recover Consol-LRR paragraph list + label OCI B(i) row.
- A1 (correction pass): DONE. Appended corrected page-5 block (extract lines 411-560, lakh+crore, both books, all nil rows). 27/28 rows reconciled. ONE genuine filing inconsistency flagged: CON Q1FY26 "TCI attrib to Shareholders" 1,966.53 lakh fails internal tie by 9.58 lakh (prior-year comparative). Consol-LRR paras 2/4/5/6 recovered (text-layer drop, not content gap). Crore figures tie to Notion FY26 baseline (net sales 1,424.28cr, PAT 84.81cr).
- A3 forensics: PASS (F1-F17 all statused, no blanks). No thesis-broken trigger fired: EBITDA margin 12.81% GREEN; Cybercons subsidiary, no restatement (HARD OVERRIDE not fired). Forward-signals: rev -4.6% YoY, TWAS focus segment -20.7% YoY, dep x5.5 + finance +46% in parent fully consuming +315bp EBITDA gain (PBT flat). Casting error 9.58 lakh in restated PY comparative. Monitorables 2/3/4/5 UNCLEARABLE (no balance sheet/receivables/order book in filing).
- A4 analyst (merged): DONE. Verdict PROCEED WITH CAVEATS (cash conversion INDETERMINATE). CON Q1FY27 rev 313.69cr -4.61% YoY, Op EBITDA margin 12.81% +315bps, PBT +0.65%, PAT 19.80cr +0.77%, EPS 15.54. Core PBT ex-OI FELL ~2% (dep x5.48 + finance +45.8% consumed margin gain). No thesis-broken trigger fired; buy-gate half-satisfied (margin GREEN, receivables UNVERIFIABLE) -> pushed to H1/Q2. Decision Status unchanged. 8 Questions-for-Management. Plain-language brief written.
- A5 adversary: dispatched.
- A5 adversary: VERDICT COMPLETE. Deliverable gate PASS, coverage 7/7 match, arithmetic reproduced zero discrepancies (incl the 9.58 lakh casting cell), adversarial PASS (FS/AMB->question rule holds 8 rows; INDETERMINATE capped at CAVEATS; no monitorable upgraded; no re-rate; 3 positive claims' bear counters already grafted). No loop-back.
- NOTION SAVE: done inline. Full review appended to Dynacons page (4 sequential inserts: financials both books + YoY; S-vs-C gap + cash-quality + triggers + monitorables + position; Questions-for-Management + catalysts + verdict; plain-language brief + A3 F1-F17 scorecard + A5 verdict). Key Notes prepended with 2026-08-13 dated line, all prior entries preserved. Decision Status unchanged (no trigger fired).

## Final reconciliation line
1 document (results) / 5 notes / 0 concall turns / 0 slides — all reviewed. 2 agenda items, 3 entities, 13 segment rows, 11 auditor paras, 36 line items, 5 signatures. A5 COMPLETE.

## Close
clean run except: page-5 combined P&L required an orchestrator OCR fallback (pdftotext -layout scrambled the AcroForm column-to-value mapping; char-test passed but mapping did not). A2 caught it; repaired via 400dpi tesseract + image Read + arithmetic reconciliation; A5 re-verified zero discrepancies. Toolchain (poppler-utils, tesseract) was absent at session start and had to be installed. Lesson candidate: high per-page char count does NOT prove column-mapping integrity on wrapped-header AcroForm results tables; A2's OCR_MISALIGNMENT flag is the real gate, not A1's char-test.
