# RUN LOG — /run-quarterly SFL Q1 FY27

Run date: 2026-08-04. Operator: Keerti Kaushik. Orchestrator: quarterly-00 v1.0.

## 0. SETUP AND PRECHECKS
- **Args**: TICKER = SFL (Sheela Foam Ltd). Quarter = Q1 FY27 (ended 30 Jun 2026).
- **Protocol files**: all present — Quarterly_Results_Review_Protocol_v1_2.md,
  Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md.
- **Toolchain**: pdftotext/pdfinfo/pdftoppm/tesseract were MISSING; installed
  poppler-utils + tesseract-ocr via apt (index refreshed after a stale-404).
  All four now resolve.
- **Document-class detection** (by content, pdfinfo page counts authoritative;
  upload-wrapper page counts were wrong and ignored):
  1. results_sfl_q1fy27.pdf (12 pp) — RESULTS. Reg 30/33/52 Board Outcome +
     Un-Audited Standalone & Consolidated Financial Results, quarter ended
     30 Jun 2026. → full A1→A2→A3.
  2. presentation_sfl_q1fy27.pdf (51 pp) — PRESENTATION. Investor Presentation
     on Q1 FY27 results. Image-heavy (11 MB); A1 OCR fallback expected. →
     full A1→A2→A3.
  3. pressrelease_sfl_q1fy27.pdf (3 pp) — PRESS RELEASE (Reg 30). Management
     commentary + highlight numbers. No Reg-33 note table / no slide deck →
     A1 extraction spine only; folded into A4 as management commentary +
     number cross-check. Extracted under presentation-class tooling.
  4. directorintimation_sfl_q1fy27.pdf (2 pp) — DIRECTOR APPOINTMENT INTIMATION
     (Reg 30). Ms. Avantika Singh Gautam, non-executive non-independent
     director, 5 yrs w.e.f. 04 Aug 2026. Governance / F13 Board-Outcome item →
     A1 extraction spine only; folded into A4 (F13 governance assessment).
  - No concall transcript supplied (investor call was 31 Jul 2026; no transcript
    in the set). Role 5 concall analysis therefore N.A. this run.
- **Company memory**: companies/SFL.md read. **Notion fetched LIVE** (page
  39ebb2b9-d3ab-810c-9910-ec6f31fb982c, run 2026-07-14).
  - Decision Status: WATCHLIST / AVOID (on valuation). CMP Rs 807. Entry
    Rs 362 (MoS) to Rs 453. Must fall ~44% to enter.
  - Thesis-broken triggers: (a) Operating Cash ROCE fails >14% by FY28;
    (b) Kurlon synergy slips a fifth consecutive quarter with no hard date;
    (c) Q1 or Q2 FY27 core EBITDA margin compresses >150bps YoY OR prints <10%.
  - Monitoring checklist: 1) core EBITDA ex-other-income >12% both Q1 & Q2 FY27;
    2) Kurlon synergy installed with Rs 40-60 Cr step-up in Q1 FY27; 3) Cash
    ROCE >14% by FY28; 4) net debt toward FY28 net cash; 5) receivables growth
    <= revenue growth with CFO/PAT >1.0x; 6) second consecutive dividend FY27,
    stable board; 7) entry conjunction; 8) falsification: Q1 FY27 core EBITDA <10%.
  - THIS QUARTER IS THE TRIPWIRE QUARTER. The whole SFL call turns on the
    Q1/Q2 FY27 core-EBITDA-margin print. A3/A4 receive this checklist inline.
