stage: B00-inputs
company: MMP
company_name: MMP Industries Ltd
run_date: 2026-10-04
model: claude-opus-5-5 (orchestrator session, inline)
status: complete
run_type: full
concalls_available: false
no_concall_mode: true
spear: "OVERRIDE 2026-10-04 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)"
load_bearing_facts:
  - "LBF1 guidance vs delivery: FY26 revenue +19.1% with EBITDA margin down 133 bps to 8.0%; FY27 pair +15-18% revenue, +40-50% exports, margin up"
  - "LBF2 April 2025 Umred incident: exceptional loss, insurance claim receivable recognised Q4 FY26, amount and collection"
  - "LBF3 associates and RPT: Star Circlips (26.06%) and Toyo JV (26%) share of profit as a share of PBT; promoter-group RPTs"
  - "LBF4 cash conversion and funding of new-subsidiary capex: CFO vs EBITDA, WC days, debt path behind bank lines Rs 80 Cr to Rs 135 Cr"
sector_cap_row: "Cables / Industrial products"
sector_cap_row_evidence: "No non-ferrous or aluminium row in the cap table. FY26 revenue mix (printed on the Q1 FY27 deck p.11, p.16): aluminium powders 62% (industrial input to explosives, AAC, pesticides), foils 26%, conductors and cables 12%; Q1 FY27 actual 66.1/26.0/7.3 per B04 (label corrected by orchestrator 2026-10-05 on stage 4 finding FLAG-MIX-LABEL). Row 'Cables / Industrial products' 25x, .claude/skills/section-1b/references/05-sector-cap.md line 38. Collector guess 'Pharma / CDMO' rejected. Converter slices subject to v3.7 Amendment 17 in phase 3; phase 3 to confirm the row."
reporting_units:
  results: "INR Lakhs (results filings, face of statement)"
  annual_report: "INR Lakhs (AR FY26: all amounts rounded off to the nearest INR in Lakhs)"
  press_releases: "INR Mn (Q1 FY27 and FY26 press releases)"
  investor_presentation: "INR Cr"
  rating: "INR Cr (CRISIL)"
  screener: "INR Cr"
freshness_pairs:
  - pair: "results to concall"
    trigger_doc: "inputs/results/MMP_14082026140309_MMPILBMOutcomeFR30062026MR.pdf (Q1 FY27)"
    mate_expected: "Q1 FY27 transcript"
    status: SKIPPED
    missing_doc: "none; concalls_available false (company holds about one call a year)"
  - pair: "rating bulletin to rationale"
    trigger_doc: "inputs/rating/MMP_30042026121825_MMPRating2026.pdf"
    mate_expected: "CRISIL rationale 27-Apr-2026"
    status: PASS
    missing_doc: ""
  - pair: "SEBI order to order text"
    trigger_doc: "none referenced; AR FY26 cites only the exchange circular on enforcement of SEBI orders on director appointments (boilerplate)"
    mate_expected: "n/a"
    status: PASS
    missing_doc: ""
  - pair: "AR to latest audited annual results"
    trigger_doc: "inputs/results/MMP_23052026151817_MMPILBMOutcomeFR31032026.pdf (FY26 audited)"
    mate_expected: "AR FY2025-26"
    status: PASS
    missing_doc: ""
freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict: CORPUS GAPPED
input_gaps:
  - "collector_warning (verbatim): BSE scrip code not found on the screener page, so announcements/ is empty. This is a collector gap, not evidence that the company files nothing. [Repaired by /step1: 11 NSE filings added by hand from the NSE announcements API list, Nov 2025 to Sep 2026; a selection, not the full list.]"
  - "collector_warning (verbatim): shareholding/ is empty: no source is automated yet. Push the latest quarterly shareholding pattern by hand; it closes the FII+DII UA qualifier and the promoter pledge trend. [Repaired by /step1: Jun 2026 SHP converted from NSE XBRL to markdown; machine conversion, values copied.]"
  - "collector_warning (verbatim): screener export sheets came out EMPTY (formulas with no cached values), so no CSV was written for them: screener:Profit & Loss, screener:Quarters, screener:Balance Sheet, screener:Cash Flow, screener:Customization, and the same five sheets for ARFIN, APARINDS, MAANALU. [NOT repaired: no LibreOffice on this machine. Data_Sheet.csv carries the raw values for all four companies.]"
  - "collector_warning (verbatim): no results PDFs yet (screener has none). [Repaired by /step1: Q1 FY27 machine-readable copy, Q4 and FY26 audited, Q3 FY26 added from NSE.]"
  - "collector_warning (verbatim): no rating PDF yet. [Repaired by /step1: CRISIL letter PDF 30-Apr-2026 plus rationale text 27-Apr-2026 from the crisil.com HTML page.]"
  - "collector_warning (verbatim): only 2 concalls -> no-concall mode. [Company holds about one call a year: May 2026 (Q4 FY26) and July 2022 present. NO-CONCALL MODE applies; both transcripts are usable as supplementary evidence.]"
  - "SCANNED RESULTS: inputs/results/MMP_23052026151817_MMPILBMOutcomeFR31032026.pdf (text on 2 of 21 pages) and inputs/results/MMP_13022026135642_MMPBMOutcomeResults31122025.pdf (2 of 10) are image scans; no OCR engine on this machine. Read them as page images; FY26 audited figures are also in the text-based AR FY26."
  - "MOVED: inputs/results/MMP_10082026130630_MMPILBMOutcomeFR30062026.pdf (scanned Q1 FY27) to inputs/other/; replaced by the machine-readable copy of the same Q1 FY27 outcome, inputs/announcements/MMP_14082026140309_MMPILBMOutcomeFR30062026MR.pdf moved to inputs/results/."
  - "REMOVED duplicate: inputs/presentation/Investor_Presentation_1.pdf (byte-identical to MMP_13082026171648_MMPILInvestorPPT30062026.pdf)."
  - "PEER TRANSCRIPTS: ARFIN has none collected; peer-concalls cover APARINDS (4) and MAANALU (4) only."
  - "EXCHANGE CLARIFICATIONS: NSE sought clarification on financial results on 2026-03-05 and 2026-06-23; no attachment on NSE and the company reply is not in the corpus."
  - "research/ empty (no effect on anchored evidence)."
  - "prospectus/ empty: not expected (long-listed; NSE filings from 2020)."
corpus_manifest:
  - {path: inputs/annual-report/Annual_Report_2026.pdf, issuer: MMP Industries Ltd, type: annual report, period: "FY2025-26 (filed 18-Aug-2026)", matched_folder: true}
  - {path: inputs/annual-report/Annual_Report_2025.pdf, issuer: MMP Industries Ltd, type: annual report, period: "FY2024-25 (filed 14-Aug-2025)", matched_folder: true}
  - {path: inputs/results/MMP_14082026140309_MMPILBMOutcomeFR30062026MR.pdf, issuer: MMP Industries Ltd, type: "board outcome + unaudited results, machine-readable", period: "Q1 FY27 (30-Jun-2026)", matched_folder: true}
  - {path: inputs/results/MMP_23052026151817_MMPILBMOutcomeFR31032026.pdf, issuer: MMP Industries Ltd, type: "board outcome + audited results, scanned", period: "Q4 and FY26 (31-Mar-2026)", matched_folder: true}
  - {path: inputs/results/MMP_13022026135642_MMPBMOutcomeResults31122025.pdf, issuer: MMP Industries Ltd, type: "board outcome + unaudited results, scanned", period: "Q3 FY26 (31-Dec-2025)", matched_folder: true}
  - {path: inputs/rating/MMP_30042026121825_MMPRating2026.pdf, issuer: "MMP Industries Ltd cover enclosing CRISIL Ratings letter", type: rating disclosure, period: Apr 2026, matched_folder: true}
  - {path: inputs/rating/CRISIL_RatingRationale_MMP_2026-04-27.md, issuer: CRISIL Ratings, type: "rating rationale (HTML text)", period: 27-Apr-2026, matched_folder: true}
  - {path: inputs/concalls/Concall_May_2026_Transcript.pdf, issuer: MMP Industries Ltd, type: earnings call transcript, period: "Q4 FY26 call held 25-May-2026", matched_folder: true}
  - {path: inputs/concalls/Concall_Jul_2022_Transcript.pdf, issuer: MMP Industries Ltd, type: earnings call transcript, period: "Q1 FY23 call, July 2022", matched_folder: true}
  - {path: inputs/presentation/MMP_13082026171648_MMPILInvestorPPT30062026.pdf, issuer: MMP Industries Ltd, type: investor presentation, period: Q1 FY27, matched_folder: true}
  - {path: inputs/presentation/MMP_25052026103403_MMPInvestorPresentationMarch2026.pdf, issuer: MMP Industries Ltd, type: investor presentation, period: Q4 FY26, matched_folder: true}
  - {path: "inputs/announcements/ (11 PDFs)", issuer: MMP Industries Ltd, type: "Reg 30 filings: press releases Nov 2025, Feb 2026, May 2026, Jul 2026, Aug 2026 x2; board outcomes Mar and Jun 2026; AGM proceedings Sep 2026; analyst meets Mar and Sep 2026; SAST disclosure Jun 2026", period: Nov 2025 to Sep 2026, matched_folder: true}
  - {path: inputs/shareholding/SHP_MMP_2026-06-30.md, issuer: "MMP Industries Ltd (NSE XBRL)", type: shareholding pattern, period: Q1 FY27, matched_folder: true}
  - {path: "inputs/peer-concalls/APARINDS-* (4)", issuer: Apar Industries, type: transcripts, period: Nov 2025 to Jul 2026, matched_folder: true}
  - {path: "inputs/peer-concalls/MAANALU-* (4)", issuer: Maan Aluminium, type: transcripts, period: Nov 2025 to Aug 2026, matched_folder: true}
  - {path: "inputs/screening/*-Data_Sheet.csv (4)", issuer: screener.in, type: raw data sheet, period: to FY26, matched_folder: true}
tooling: "pypdf extraction OK; every PDF pre-extracted to a page-marked .txt beside it (tools/extract_pdfs.py). Stages read the .txt; scanned results pages are read as PDF page images."
flags: []
analyst_note: "Units differ across sources: Lakhs in results and AR, Mn in press releases, Cr in PPT, rating and screener. No conversion before stage 10."
