# Stage 0: input inventory, ESCONET 2026-10-05

Inline orchestrator stage. The block below governs; this report restates it for the archive.

Spear gate: Spear: OVERRIDE 2026-10-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)

## Load-bearing facts (first verification priority)
- Q1 FY27 EBITDA margin 8.55% vs FY26 2.60%: mix shift or one-time inventory/price gain (inventory change, other income Rs 1.93 Cr, Rs 1.84 Cr warrant forfeiture treatment)
- Cash conversion: FY26 CFO negative, inventory about 2.7x, debt back to Rs 13 Cr, against the Q1 FY27 claim of 20.2 debtor days
- IPO and governance: Income Tax s.131(1A) summons (Feb 2026) tied to IPO lead manager Corporate Capital Ventures (pre-IPO allotments, IPO-proceeds use); lapsed Rs 345 warrants; NSE FY26 PDF vs XBRL EPS discrepancy
- Guidance vs delivery: FY27 revenue Rs 370-400 Cr; June 2025 call outlook vs FY26 actual; Singapore subsidiary revenue (about Rs 53 Cr) and related-party flows

## Sector cap row
- Cybersecurity / VAD: 25x, section-1b chunk 05 sector cap table. Value-added resale and integration of servers, storage and HPC with cybersecurity (Fluidech) and cloud (ZeaCloud) attached; management calls cloud very small of revenue (Q1 FY27 transcript), so Platform/SaaS/IT services 45x does not fit; Data centers/cloud 30x fits only the ZeaCloud slice (SOTP is a phase 3 question). Collector guess Pharma / CDMO rejected.

## Reporting units
- results: INR Lakhs (all three board outcomes)
- annual_report: INR Lakhs on the face of both ARs (AR FY26 p.132 'All amounts in lakhs'); corrected 2026-10-05 after stage 1 (stage 0 first wrote Crores in error)
- screener: INR Cr
- prospectus: INR Lakhs (cover page issue size)
- rating: INR crore

## Freshness pairs
- RESULTS to CONCALL: PASS (inputs/results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.pdf (Q1 FY27))
- RATING BULLETIN to RATIONALE: PASS (CRISIL 2026-07-02)
- SEBI ORDER to ORDER TEXT: PASS (none referenced (corpus grep for SEBI order, adjudication, show cause: no hit))
- AR to LATEST AUDITED ANNUAL RESULTS: PASS (FY2025-26 audited results (2026-05-28))
- Verdict: FRESHNESS PAIRS OK

## Input gaps
- collector_warning (verbatim): BSE scrip code not found on the screener page, so announcements/ is empty. This is a collector gap, not evidence that the company files nothing. REPAIRED by /step1: 33 NSE Reg 30 filings Sep 2025 to Sep 2026 fetched from the NSE API (28 kept in announcements/ after removing 3 byte-identical duplicates and moving 2 decks to presentation/ and other/); filings before Sep 2025 not collected.
- collector_warning (verbatim): shareholding/ is empty: no source is automated yet. REPAIRED by /step1: NSE SHP XBRL for Mar-2026 and Jun-2026 plus mechanical text extracts.
- collector_warning (verbatim): screener export sheets came out EMPTY (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization) for ESCONET, NETWEB, RPTECH, ORIENTTECH. Data_Sheet.csv files ARE populated with raw values; ESCONET screener history covers FY2023-FY2026 only plus Q1 FY27.
- collector_warning (verbatim): no results PDFs yet (screener has none). REPAIRED by /step1: H1 FY26, FY26 audited and Q1 FY27 board outcomes fetched from NSE.
- collector_warning (verbatim): no rating PDF yet. REPAIRED by /step1: CRISIL rationale 2026-07-02 saved as text (original HTML in inputs/other/). 2024 and 2025 rationales not collected.
- collector_warning (verbatim): only 2 concalls -> no-concall mode. OVERRIDDEN by /step1: concalls_available true on 2 transcripts (Jun 2025 FY25 investor meet; Aug 2026 Q1 FY27). SME reports half-yearly; Q1 FY27 was its first voluntary quarterly print.
- concalls: 2 transcripts held (contract allows 3). The 22 Jun 2026 FY26 investor meet has a deck (inputs/presentation/Investor_Presentation_Jun_2026.pdf) but no transcript (recording only). No H1 FY26 call.
- annual-report: FY2023-24 AR not collected (two-most-recent rule); the prospectus covers pre-IPO years.
- research/: empty, no broker notes (non-anchored; no effect on anchored evidence).
- prospectus: final prospectus held; the near-identical RHP (381 pages) moved to inputs/other/ to avoid double reading.
- announcements: SAST disclosure 2026-05-19 (team_bbodade) is scanned; its .txt is corrupt and OCR repair failed (no PDF renderer). Read the PDF page directly; take no number from the .txt.
- shareholding and rating: XBRL (.xml) and CRISIL HTML originals kept beside their text extracts; exchange or agency filings outside the collector allowlist, committed by hand by /step1.
- listed_date: exact NSE Emerge listing date NOT FOUND in corpus; prospectus dated 2024-02-20.
- EMPTY-FOLDER CONFIRMATION suppressed by the /step1 AUTONOMY CONTRACT; standing answer: proceed with the gaps. Empty at stage 0: research/.

## Corpus manifest

| path | issuer | type | period |
|---|---|---|---|
| inputs/announcements/2025-09-01-ESCONET_01092025172859_ESC_INT_Resq_01092025.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-09-01 |
| inputs/announcements/2025-09-12-ESCONET_12092025172709_ESC_AGM_12092025_PROCEEDINGS.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-09-12 |
| inputs/announcements/2025-09-29-ESCONET_29092025192642_Reciept_of_Order_29092025_FISPL.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-09-29 |
| inputs/announcements/2025-10-14-ESCONET_14102025163330_ESC_NSE_INT_Material_Order_14102025.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-10-14 |
| inputs/announcements/2025-11-07-ESCONET_07112025155406_NSE_Int_Zeacloud_RO_Change_0711.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-11-07 |
| inputs/announcements/2025-11-17-ESCONET_17112025184702_PR_ESC_H1_25_26.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-11-17 |
| inputs/announcements/2025-12-18-ESCONET_18122025150019_ESC_INT_HEXADATA_PR_18_12_2025.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2025-12-18 |
| inputs/announcements/2026-02-09-ESCONET_09022026135228_NSE_Intimation_ZSPL_Reg_30.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-02-09 |
| inputs/announcements/2026-02-28-ESCONET_28022026125257_NSE_Intimation_ITD_28022026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-02-28 |
| inputs/announcements/2026-02-28-ESCONET_28022026133751_PR_ITD_ETL_28022026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-02-28 |
| inputs/announcements/2026-03-03-ESCONET_03032026120822_NSE_ESC_INT_ONGC_03032026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-03-03 |
| inputs/announcements/2026-04-06-ESCONET_06042026123845_NSE_Int_ETL_LC_NA_06042026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-04-06 |
| inputs/announcements/2026-04-10-ESCONET_25062025163911_ESC_Response_25062025.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-04-10 |
| inputs/announcements/2026-04-29-ESCONET_29042026105220_NSE_INT_ETL_NVIDIA_29042026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-04-29 |
| inputs/announcements/2026-04-29-ESCONET_29042026120311_ESC_INT_Forfiture_29042026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-04-29 |
| inputs/announcements/2026-05-19-team_bbodade_16042026180304_ESCONET.pdf | Esconet Technologies Ltd | SAST takeover disclosure (scanned; .txt corrupt, OCR failed: read the PDF page directly) | filed 2026-05-19 |
| inputs/announcements/2026-05-28-ESCONET_28052026202231_Press_Release_Esconet_28052026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-05-28 |
| inputs/announcements/2026-06-17-ESCONET_17062026182449_ETL_int_NSE_investor_Meet.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-06-17 |
| inputs/announcements/2026-06-23-ESCONET_23062026185056_ETL_NSE_Int_WEBLINK_IM_22062026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-06-23 |
| inputs/announcements/2026-07-13-ESCONET_13072026165622_NSE_INT_ETL_Reg_30_13072026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-07-13 |
| inputs/announcements/2026-07-27-ESCONET_23072026182650_ETL_Revised_Clari.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-07-27 |
| inputs/announcements/2026-07-29-ESCONET_29072026151517_NSE_INT_ETL_29072026_AG_Appointment_CRO.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-07-29 |
| inputs/announcements/2026-08-03-ESCONET_03082026130747_ETL_PI_BM_12082026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-08-03 |
| inputs/announcements/2026-08-06-ESCONET_06082026163932_ETL_Intimation_Investor_Meet.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-08-06 |
| inputs/announcements/2026-08-12-ESCONET_12082026174325_ETL_PR_30062026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-08-12 |
| inputs/announcements/2026-08-24-ESCONET_24082026182859_ETL_NSE_int_Notice_AGM.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-08-24 |
| inputs/announcements/2026-09-25-ESCONET_25092026180638_Esconet_Proceedings_of_14_AGM.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-09-25 |
| inputs/announcements/2026-09-30-ESCONET_30092026132657_Revised_Outcome_14_AGM_ETL_2026.pdf | Esconet Technologies Ltd | Reg 30 exchange filing | filed 2026-09-30 |
| inputs/annual-report/Annual_Report_2025.pdf | Esconet Technologies Ltd | annual report | FY2024-25 |
| inputs/annual-report/Annual_Report_2026.pdf | Esconet Technologies Ltd | annual report | FY2025-26 |
| inputs/concalls/Concall_Aug_2026_Transcript.pdf | Esconet Technologies Ltd | earnings call transcript | Q1 FY2026-27 call, 17 Aug 2026 |
| inputs/concalls/Concall_Jun_2025_Transcript.pdf | Esconet Technologies Ltd | earnings call transcript | FY2024-25 results investor meet, 20 Jun 2025 |
| inputs/peer-concalls/NETWEB-Concall_Aug_2026_Transcript.pdf | Netweb Technologies India Ltd | peer earnings call transcript | call Aug 2026 |
| inputs/peer-concalls/NETWEB-Concall_Jan_2026_Transcript.pdf | Netweb Technologies India Ltd | peer earnings call transcript | call Jan 2026 |
| inputs/peer-concalls/NETWEB-Concall_May_2026_Transcript.pdf | Netweb Technologies India Ltd | peer earnings call transcript | call May 2026 |
| inputs/peer-concalls/NETWEB-Concall_Nov_2025_Transcript.pdf | Netweb Technologies India Ltd | peer earnings call transcript | call Nov 2025 |
| inputs/peer-concalls/ORIENTTECH-Concall_Aug_2025_Transcript.pdf | Orient Technologies Ltd | peer earnings call transcript | call Aug 2025 |
| inputs/peer-concalls/ORIENTTECH-Concall_Aug_2026_Transcript.pdf | Orient Technologies Ltd | peer earnings call transcript | call Aug 2026 |
| inputs/peer-concalls/ORIENTTECH-Concall_Feb_2026_Transcript.pdf | Orient Technologies Ltd | peer earnings call transcript | call Feb 2026 |
| inputs/peer-concalls/ORIENTTECH-Concall_Nov_2025_Transcript.pdf | Orient Technologies Ltd | peer earnings call transcript | call Nov 2025 |
| inputs/peer-concalls/RPTECH-Concall_Aug_2026_Transcript.pdf | Rashi Peripherals Ltd | peer earnings call transcript | call Aug 2026 |
| inputs/peer-concalls/RPTECH-Concall_Feb_2026_Transcript.pdf | Rashi Peripherals Ltd | peer earnings call transcript | call Feb 2026 |
| inputs/peer-concalls/RPTECH-Concall_May_2026_Transcript.pdf | Rashi Peripherals Ltd | peer earnings call transcript | call May 2026 |
| inputs/peer-concalls/RPTECH-Concall_Nov_2025_Transcript.pdf | Rashi Peripherals Ltd | peer earnings call transcript | call Nov 2025 |
| inputs/presentation/Investor_Presentation_Jun_2026.pdf | Esconet Technologies Ltd | investor presentation | Investor meet deck, 22 Jun 2026 |
| inputs/presentation/Investor_Presentation_Sep_2025.pdf | Esconet Technologies Ltd | investor presentation | Investor deck, Sep 2025 |
| inputs/prospectus/EsconetTechnologies_PROSP.pdf | Esconet Technologies Ltd | IPO prospectus | IPO prospectus dated 20 Feb 2024 |
| inputs/results/2025-11-14-ESCONET_14112025181122_Outcome_BM_ESC_14112025_signed.pdf | Esconet Technologies Ltd | board outcome with financial results | H1 FY2025-26 (half year to 30 Sep 2025) |
| inputs/results/2026-05-28-ESCONET_28052026185515_Outcome_BM_28052026.pdf | Esconet Technologies Ltd | board outcome with financial results | FY2025-26 audited (year to 31 Mar 2026) |
| inputs/results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.pdf | Esconet Technologies Ltd | board outcome with financial results | Q1 FY2026-27 (quarter to 30 Jun 2026) |
| inputs/rating/CRISIL_Esconet_Rating_Rationale_2026-07-02.txt | CRISIL Ratings (on Esconet) | rating rationale (full) | 2026-07-02 |
| inputs/shareholding/SHP_1650865_14042026063352_WEB_extract.txt | Esconet Technologies Ltd (NSE SHP XBRL) | shareholding pattern extract | quarter to 31 Mar 2026 |
| inputs/shareholding/SHP_1693906_16072026124525_WEB_extract.txt | Esconet Technologies Ltd (NSE SHP XBRL) | shareholding pattern extract | quarter to 30 Jun 2026 |
| inputs/screening/NETWEB-Data_Sheet.csv | screener.in export | Data Sheet (raw values populated; formula sheets exported empty) | FY2023-FY2026 annual + latest quarter |
| inputs/screening/ORIENTTECH-Data_Sheet.csv | screener.in export | Data Sheet (raw values populated; formula sheets exported empty) | FY2023-FY2026 annual + latest quarter |
| inputs/screening/RPTECH-Data_Sheet.csv | screener.in export | Data Sheet (raw values populated; formula sheets exported empty) | FY2023-FY2026 annual + latest quarter |
| inputs/screening/screener-Data_Sheet.csv | screener.in export | Data Sheet (raw values populated; formula sheets exported empty) | FY2023-FY2026 annual + latest quarter |

```yaml
stage: B00-inputs
company: ESCONET
run_date: '2026-10-05'
model: claude-opus-5-5 (orchestrator session, inline)
status: complete
spear_line: 'Spear: OVERRIDE 2026-10-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)'
load_bearing_facts:
- 'Q1 FY27 EBITDA margin 8.55% vs FY26 2.60%: mix shift or one-time inventory/price gain (inventory change, other income Rs 1.93 Cr, Rs 1.84 Cr warrant
  forfeiture treatment)'
- 'Cash conversion: FY26 CFO negative, inventory about 2.7x, debt back to Rs 13 Cr, against the Q1 FY27 claim of 20.2 debtor days'
- 'IPO and governance: Income Tax s.131(1A) summons (Feb 2026) tied to IPO lead manager Corporate Capital Ventures (pre-IPO allotments, IPO-proceeds use);
  lapsed Rs 345 warrants; NSE FY26 PDF vs XBRL EPS discrepancy'
- 'Guidance vs delivery: FY27 revenue Rs 370-400 Cr; June 2025 call outlook vs FY26 actual; Singapore subsidiary revenue (about Rs 53 Cr) and related-party
  flows'
company_memory:
- companies/ESCONET.md
- runs/esconet-2026-10-05/step1-business-brief.md
concalls_available: true
no_concall_mode: false
sector_cap_row: Cybersecurity / VAD
sector_cap_row_evidence: 25x, section-1b chunk 05 sector cap table. Value-added resale and integration of servers, storage and HPC with cybersecurity (Fluidech)
  and cloud (ZeaCloud) attached; management calls cloud very small of revenue (Q1 FY27 transcript), so Platform/SaaS/IT services 45x does not fit; Data
  centers/cloud 30x fits only the ZeaCloud slice (SOTP is a phase 3 question). Collector guess Pharma / CDMO rejected.
listed_within_3y: true
listed_evidence: IPO prospectus dated 20 Feb 2024 (inputs/prospectus/EsconetTechnologies_PROSP.pdf p1), NSE Emerge. Prospectus present.
reporting_units:
  results: INR Lakhs (all three board outcomes)
  annual_report: INR Lakhs on the face of both ARs (AR FY26 p.132 'All amounts in lakhs'); corrected 2026-10-05 after stage 1 (stage 0 first wrote Crores in error)
  screener: INR Cr
  prospectus: INR Lakhs (cover page issue size)
  rating: INR crore
pdf_route: pre-extracted page-marked .txt beside every PDF (tools/extract_pdfs.py); check_extraction flagged one blank file (SAST disclosure), OCR repair
  failed (no renderer); stages read .txt, verifiers may open PDFs
freshness_pairs:
- pair: RESULTS to CONCALL
  trigger_doc: inputs/results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.pdf (Q1 FY27)
  mate_expected: Q1 FY27 transcript (inputs/concalls/Concall_Aug_2026_Transcript.pdf)
  status: PASS
  missing_doc: ''
- pair: RATING BULLETIN to RATIONALE
  trigger_doc: CRISIL 2026-07-02
  mate_expected: full rationale
  status: PASS
  missing_doc: ''
- pair: SEBI ORDER to ORDER TEXT
  trigger_doc: 'none referenced (corpus grep for SEBI order, adjudication, show cause: no hit)'
  mate_expected: n/a
  status: PASS
  missing_doc: ''
- pair: AR to LATEST AUDITED ANNUAL RESULTS
  trigger_doc: FY2025-26 audited results (2026-05-28)
  mate_expected: FY2025-26 AR
  status: PASS
  missing_doc: ''
freshness_verdict: FRESHNESS PAIRS OK
input_gaps:
- 'collector_warning (verbatim): BSE scrip code not found on the screener page, so announcements/ is empty. This is a collector gap, not evidence that the
  company files nothing. REPAIRED by /step1: 33 NSE Reg 30 filings Sep 2025 to Sep 2026 fetched from the NSE API (28 kept in announcements/ after removing 3 byte-identical duplicates and moving 2 decks to presentation/ and other/); filings before Sep 2025 not collected.'
- 'collector_warning (verbatim): shareholding/ is empty: no source is automated yet. REPAIRED by /step1: NSE SHP XBRL for Mar-2026 and Jun-2026 plus mechanical
  text extracts.'
- 'collector_warning (verbatim): screener export sheets came out EMPTY (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization) for ESCONET, NETWEB,
  RPTECH, ORIENTTECH. Data_Sheet.csv files ARE populated with raw values; ESCONET screener history covers FY2023-FY2026 only plus Q1 FY27.'
- 'collector_warning (verbatim): no results PDFs yet (screener has none). REPAIRED by /step1: H1 FY26, FY26 audited and Q1 FY27 board outcomes fetched from
  NSE.'
- 'collector_warning (verbatim): no rating PDF yet. REPAIRED by /step1: CRISIL rationale 2026-07-02 saved as text (original HTML in inputs/other/). 2024
  and 2025 rationales not collected.'
- 'collector_warning (verbatim): only 2 concalls -> no-concall mode. OVERRIDDEN by /step1: concalls_available true on 2 transcripts (Jun 2025 FY25 investor
  meet; Aug 2026 Q1 FY27). SME reports half-yearly; Q1 FY27 was its first voluntary quarterly print.'
- 'concalls: 2 transcripts held (contract allows 3). The 22 Jun 2026 FY26 investor meet has a deck (inputs/presentation/Investor_Presentation_Jun_2026.pdf)
  but no transcript (recording only). No H1 FY26 call.'
- 'annual-report: FY2023-24 AR not collected (two-most-recent rule); the prospectus covers pre-IPO years.'
- 'research/: empty, no broker notes (non-anchored; no effect on anchored evidence).'
- 'prospectus: final prospectus held; the near-identical RHP (381 pages) moved to inputs/other/ to avoid double reading.'
- 'announcements: SAST disclosure 2026-05-19 (team_bbodade) is scanned; its .txt is corrupt and OCR repair failed (no PDF renderer). Read the PDF page directly;
  take no number from the .txt.'
- 'shareholding and rating: XBRL (.xml) and CRISIL HTML originals kept beside their text extracts; exchange or agency filings outside the collector allowlist,
  committed by hand by /step1.'
- 'listed_date: exact NSE Emerge listing date NOT FOUND in corpus; prospectus dated 2024-02-20.'
- 'EMPTY-FOLDER CONFIRMATION suppressed by the /step1 AUTONOMY CONTRACT; standing answer: proceed with the gaps. Empty at stage 0: research/.'
flags: []
corpus_commit: 17a4d6a7
corpus_manifest:
- path: inputs/announcements/2025-09-01-ESCONET_01092025172859_ESC_INT_Resq_01092025.pdf
  text: inputs/announcements/2025-09-01-ESCONET_01092025172859_ESC_INT_Resq_01092025.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-09-01
  folder_match: true
- path: inputs/announcements/2025-09-12-ESCONET_12092025172709_ESC_AGM_12092025_PROCEEDINGS.pdf
  text: inputs/announcements/2025-09-12-ESCONET_12092025172709_ESC_AGM_12092025_PROCEEDINGS.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-09-12
  folder_match: true
- path: inputs/announcements/2025-09-29-ESCONET_29092025192642_Reciept_of_Order_29092025_FISPL.pdf
  text: inputs/announcements/2025-09-29-ESCONET_29092025192642_Reciept_of_Order_29092025_FISPL.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-09-29
  folder_match: true
- path: inputs/announcements/2025-10-14-ESCONET_14102025163330_ESC_NSE_INT_Material_Order_14102025.pdf
  text: inputs/announcements/2025-10-14-ESCONET_14102025163330_ESC_NSE_INT_Material_Order_14102025.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-10-14
  folder_match: true
- path: inputs/announcements/2025-11-07-ESCONET_07112025155406_NSE_Int_Zeacloud_RO_Change_0711.pdf
  text: inputs/announcements/2025-11-07-ESCONET_07112025155406_NSE_Int_Zeacloud_RO_Change_0711.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-11-07
  folder_match: true
- path: inputs/announcements/2025-11-17-ESCONET_17112025184702_PR_ESC_H1_25_26.pdf
  text: inputs/announcements/2025-11-17-ESCONET_17112025184702_PR_ESC_H1_25_26.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-11-17
  folder_match: true
- path: inputs/announcements/2025-12-18-ESCONET_18122025150019_ESC_INT_HEXADATA_PR_18_12_2025.pdf
  text: inputs/announcements/2025-12-18-ESCONET_18122025150019_ESC_INT_HEXADATA_PR_18_12_2025.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2025-12-18
  folder_match: true
- path: inputs/announcements/2026-02-09-ESCONET_09022026135228_NSE_Intimation_ZSPL_Reg_30.pdf
  text: inputs/announcements/2026-02-09-ESCONET_09022026135228_NSE_Intimation_ZSPL_Reg_30.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-02-09
  folder_match: true
- path: inputs/announcements/2026-02-28-ESCONET_28022026125257_NSE_Intimation_ITD_28022026.pdf
  text: inputs/announcements/2026-02-28-ESCONET_28022026125257_NSE_Intimation_ITD_28022026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-02-28
  folder_match: true
- path: inputs/announcements/2026-02-28-ESCONET_28022026133751_PR_ITD_ETL_28022026.pdf
  text: inputs/announcements/2026-02-28-ESCONET_28022026133751_PR_ITD_ETL_28022026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-02-28
  folder_match: true
- path: inputs/announcements/2026-03-03-ESCONET_03032026120822_NSE_ESC_INT_ONGC_03032026.pdf
  text: inputs/announcements/2026-03-03-ESCONET_03032026120822_NSE_ESC_INT_ONGC_03032026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-03-03
  folder_match: true
- path: inputs/announcements/2026-04-06-ESCONET_06042026123845_NSE_Int_ETL_LC_NA_06042026.pdf
  text: inputs/announcements/2026-04-06-ESCONET_06042026123845_NSE_Int_ETL_LC_NA_06042026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-04-06
  folder_match: true
- path: inputs/announcements/2026-04-10-ESCONET_25062025163911_ESC_Response_25062025.pdf
  text: inputs/announcements/2026-04-10-ESCONET_25062025163911_ESC_Response_25062025.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-04-10
  folder_match: true
- path: inputs/announcements/2026-04-29-ESCONET_29042026105220_NSE_INT_ETL_NVIDIA_29042026.pdf
  text: inputs/announcements/2026-04-29-ESCONET_29042026105220_NSE_INT_ETL_NVIDIA_29042026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-04-29
  folder_match: true
- path: inputs/announcements/2026-04-29-ESCONET_29042026120311_ESC_INT_Forfiture_29042026.pdf
  text: inputs/announcements/2026-04-29-ESCONET_29042026120311_ESC_INT_Forfiture_29042026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-04-29
  folder_match: true
- path: inputs/announcements/2026-05-19-team_bbodade_16042026180304_ESCONET.pdf
  text: inputs/announcements/2026-05-19-team_bbodade_16042026180304_ESCONET.txt
  issuer: Esconet Technologies Ltd
  type: 'SAST takeover disclosure (scanned; .txt corrupt, OCR failed: read the PDF page directly)'
  period: filed 2026-05-19
  folder_match: true
- path: inputs/announcements/2026-05-28-ESCONET_28052026202231_Press_Release_Esconet_28052026.pdf
  text: inputs/announcements/2026-05-28-ESCONET_28052026202231_Press_Release_Esconet_28052026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-05-28
  folder_match: true
- path: inputs/announcements/2026-06-17-ESCONET_17062026182449_ETL_int_NSE_investor_Meet.pdf
  text: inputs/announcements/2026-06-17-ESCONET_17062026182449_ETL_int_NSE_investor_Meet.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-06-17
  folder_match: true
- path: inputs/announcements/2026-06-23-ESCONET_23062026185056_ETL_NSE_Int_WEBLINK_IM_22062026.pdf
  text: inputs/announcements/2026-06-23-ESCONET_23062026185056_ETL_NSE_Int_WEBLINK_IM_22062026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-06-23
  folder_match: true
- path: inputs/announcements/2026-07-13-ESCONET_13072026165622_NSE_INT_ETL_Reg_30_13072026.pdf
  text: inputs/announcements/2026-07-13-ESCONET_13072026165622_NSE_INT_ETL_Reg_30_13072026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-07-13
  folder_match: true
- path: inputs/announcements/2026-07-27-ESCONET_23072026182650_ETL_Revised_Clari.pdf
  text: inputs/announcements/2026-07-27-ESCONET_23072026182650_ETL_Revised_Clari.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-07-27
  folder_match: true
- path: inputs/announcements/2026-07-29-ESCONET_29072026151517_NSE_INT_ETL_29072026_AG_Appointment_CRO.pdf
  text: inputs/announcements/2026-07-29-ESCONET_29072026151517_NSE_INT_ETL_29072026_AG_Appointment_CRO.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-07-29
  folder_match: true
- path: inputs/announcements/2026-08-03-ESCONET_03082026130747_ETL_PI_BM_12082026.pdf
  text: inputs/announcements/2026-08-03-ESCONET_03082026130747_ETL_PI_BM_12082026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-08-03
  folder_match: true
- path: inputs/announcements/2026-08-06-ESCONET_06082026163932_ETL_Intimation_Investor_Meet.pdf
  text: inputs/announcements/2026-08-06-ESCONET_06082026163932_ETL_Intimation_Investor_Meet.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-08-06
  folder_match: true
- path: inputs/announcements/2026-08-12-ESCONET_12082026174325_ETL_PR_30062026.pdf
  text: inputs/announcements/2026-08-12-ESCONET_12082026174325_ETL_PR_30062026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-08-12
  folder_match: true
- path: inputs/announcements/2026-08-24-ESCONET_24082026182859_ETL_NSE_int_Notice_AGM.pdf
  text: inputs/announcements/2026-08-24-ESCONET_24082026182859_ETL_NSE_int_Notice_AGM.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-08-24
  folder_match: true
- path: inputs/announcements/2026-09-25-ESCONET_25092026180638_Esconet_Proceedings_of_14_AGM.pdf
  text: inputs/announcements/2026-09-25-ESCONET_25092026180638_Esconet_Proceedings_of_14_AGM.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-09-25
  folder_match: true
- path: inputs/announcements/2026-09-30-ESCONET_30092026132657_Revised_Outcome_14_AGM_ETL_2026.pdf
  text: inputs/announcements/2026-09-30-ESCONET_30092026132657_Revised_Outcome_14_AGM_ETL_2026.txt
  issuer: Esconet Technologies Ltd
  type: Reg 30 exchange filing
  period: filed 2026-09-30
  folder_match: true
- path: inputs/annual-report/Annual_Report_2025.pdf
  text: inputs/annual-report/Annual_Report_2025.txt
  issuer: Esconet Technologies Ltd
  type: annual report
  period: FY2024-25
  folder_match: true
- path: inputs/annual-report/Annual_Report_2026.pdf
  text: inputs/annual-report/Annual_Report_2026.txt
  issuer: Esconet Technologies Ltd
  type: annual report
  period: FY2025-26
  folder_match: true
- path: inputs/concalls/Concall_Aug_2026_Transcript.pdf
  text: inputs/concalls/Concall_Aug_2026_Transcript.txt
  issuer: Esconet Technologies Ltd
  type: earnings call transcript
  period: Q1 FY2026-27 call, 17 Aug 2026
  folder_match: true
- path: inputs/concalls/Concall_Jun_2025_Transcript.pdf
  text: inputs/concalls/Concall_Jun_2025_Transcript.txt
  issuer: Esconet Technologies Ltd
  type: earnings call transcript
  period: FY2024-25 results investor meet, 20 Jun 2025
  folder_match: true
- path: inputs/peer-concalls/NETWEB-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/NETWEB-Concall_Aug_2026_Transcript.txt
  issuer: Netweb Technologies India Ltd
  type: peer earnings call transcript
  period: call Aug 2026
  folder_match: true
- path: inputs/peer-concalls/NETWEB-Concall_Jan_2026_Transcript.pdf
  text: inputs/peer-concalls/NETWEB-Concall_Jan_2026_Transcript.txt
  issuer: Netweb Technologies India Ltd
  type: peer earnings call transcript
  period: call Jan 2026
  folder_match: true
- path: inputs/peer-concalls/NETWEB-Concall_May_2026_Transcript.pdf
  text: inputs/peer-concalls/NETWEB-Concall_May_2026_Transcript.txt
  issuer: Netweb Technologies India Ltd
  type: peer earnings call transcript
  period: call May 2026
  folder_match: true
- path: inputs/peer-concalls/NETWEB-Concall_Nov_2025_Transcript.pdf
  text: inputs/peer-concalls/NETWEB-Concall_Nov_2025_Transcript.txt
  issuer: Netweb Technologies India Ltd
  type: peer earnings call transcript
  period: call Nov 2025
  folder_match: true
- path: inputs/peer-concalls/ORIENTTECH-Concall_Aug_2025_Transcript.pdf
  text: inputs/peer-concalls/ORIENTTECH-Concall_Aug_2025_Transcript.txt
  issuer: Orient Technologies Ltd
  type: peer earnings call transcript
  period: call Aug 2025
  folder_match: true
- path: inputs/peer-concalls/ORIENTTECH-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/ORIENTTECH-Concall_Aug_2026_Transcript.txt
  issuer: Orient Technologies Ltd
  type: peer earnings call transcript
  period: call Aug 2026
  folder_match: true
- path: inputs/peer-concalls/ORIENTTECH-Concall_Feb_2026_Transcript.pdf
  text: inputs/peer-concalls/ORIENTTECH-Concall_Feb_2026_Transcript.txt
  issuer: Orient Technologies Ltd
  type: peer earnings call transcript
  period: call Feb 2026
  folder_match: true
- path: inputs/peer-concalls/ORIENTTECH-Concall_Nov_2025_Transcript.pdf
  text: inputs/peer-concalls/ORIENTTECH-Concall_Nov_2025_Transcript.txt
  issuer: Orient Technologies Ltd
  type: peer earnings call transcript
  period: call Nov 2025
  folder_match: true
- path: inputs/peer-concalls/RPTECH-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/RPTECH-Concall_Aug_2026_Transcript.txt
  issuer: Rashi Peripherals Ltd
  type: peer earnings call transcript
  period: call Aug 2026
  folder_match: true
- path: inputs/peer-concalls/RPTECH-Concall_Feb_2026_Transcript.pdf
  text: inputs/peer-concalls/RPTECH-Concall_Feb_2026_Transcript.txt
  issuer: Rashi Peripherals Ltd
  type: peer earnings call transcript
  period: call Feb 2026
  folder_match: true
- path: inputs/peer-concalls/RPTECH-Concall_May_2026_Transcript.pdf
  text: inputs/peer-concalls/RPTECH-Concall_May_2026_Transcript.txt
  issuer: Rashi Peripherals Ltd
  type: peer earnings call transcript
  period: call May 2026
  folder_match: true
- path: inputs/peer-concalls/RPTECH-Concall_Nov_2025_Transcript.pdf
  text: inputs/peer-concalls/RPTECH-Concall_Nov_2025_Transcript.txt
  issuer: Rashi Peripherals Ltd
  type: peer earnings call transcript
  period: call Nov 2025
  folder_match: true
- path: inputs/presentation/Investor_Presentation_Jun_2026.pdf
  text: inputs/presentation/Investor_Presentation_Jun_2026.txt
  issuer: Esconet Technologies Ltd
  type: investor presentation
  period: Investor meet deck, 22 Jun 2026
  folder_match: true
- path: inputs/presentation/Investor_Presentation_Sep_2025.pdf
  text: inputs/presentation/Investor_Presentation_Sep_2025.txt
  issuer: Esconet Technologies Ltd
  type: investor presentation
  period: Investor deck, Sep 2025
  folder_match: true
- path: inputs/prospectus/EsconetTechnologies_PROSP.pdf
  text: inputs/prospectus/EsconetTechnologies_PROSP.txt
  issuer: Esconet Technologies Ltd
  type: IPO prospectus
  period: IPO prospectus dated 20 Feb 2024
  folder_match: true
- path: inputs/results/2025-11-14-ESCONET_14112025181122_Outcome_BM_ESC_14112025_signed.pdf
  text: inputs/results/2025-11-14-ESCONET_14112025181122_Outcome_BM_ESC_14112025_signed.txt
  issuer: Esconet Technologies Ltd
  type: board outcome with financial results
  period: H1 FY2025-26 (half year to 30 Sep 2025)
  folder_match: true
- path: inputs/results/2026-05-28-ESCONET_28052026185515_Outcome_BM_28052026.pdf
  text: inputs/results/2026-05-28-ESCONET_28052026185515_Outcome_BM_28052026.txt
  issuer: Esconet Technologies Ltd
  type: board outcome with financial results
  period: FY2025-26 audited (year to 31 Mar 2026)
  folder_match: true
- path: inputs/results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.pdf
  text: inputs/results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.txt
  issuer: Esconet Technologies Ltd
  type: board outcome with financial results
  period: Q1 FY2026-27 (quarter to 30 Jun 2026)
  folder_match: true
- path: inputs/rating/CRISIL_Esconet_Rating_Rationale_2026-07-02.txt
  issuer: CRISIL Ratings (on Esconet)
  type: rating rationale (full)
  period: '2026-07-02'
  folder_match: true
- path: inputs/shareholding/SHP_1650865_14042026063352_WEB_extract.txt
  issuer: Esconet Technologies Ltd (NSE SHP XBRL)
  type: shareholding pattern extract
  period: quarter to 31 Mar 2026
  folder_match: true
- path: inputs/shareholding/SHP_1693906_16072026124525_WEB_extract.txt
  issuer: Esconet Technologies Ltd (NSE SHP XBRL)
  type: shareholding pattern extract
  period: quarter to 30 Jun 2026
  folder_match: true
- path: inputs/screening/NETWEB-Data_Sheet.csv
  issuer: screener.in export
  type: Data Sheet (raw values populated; formula sheets exported empty)
  period: FY2023-FY2026 annual + latest quarter
  folder_match: true
- path: inputs/screening/ORIENTTECH-Data_Sheet.csv
  issuer: screener.in export
  type: Data Sheet (raw values populated; formula sheets exported empty)
  period: FY2023-FY2026 annual + latest quarter
  folder_match: true
- path: inputs/screening/RPTECH-Data_Sheet.csv
  issuer: screener.in export
  type: Data Sheet (raw values populated; formula sheets exported empty)
  period: FY2023-FY2026 annual + latest quarter
  folder_match: true
- path: inputs/screening/screener-Data_Sheet.csv
  issuer: screener.in export
  type: Data Sheet (raw values populated; formula sheets exported empty)
  period: FY2023-FY2026 annual + latest quarter
  folder_match: true
analyst_note: Results, prospectus and both ARs are INR Lakhs; screener is INR Cr. Name the unit with every figure; convert only at stage 10.
```
