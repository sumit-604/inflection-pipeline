# Run Log — 526717 (HCP Plastene Bulkpack Ltd) — Q1 FY27

Pipeline: /run-quarterly. Orchestrator v1.0. Run date 2026-08-12.

## Documents supplied (4)
All from HCP Plastene Bulkpack Ltd, Scrip 526717, all dated 12 Aug 2026, period ended 30 Jun 2026.

| # | Input file | Pages | Class | Notes |
|---|---|---|---|---|
| D1 | results_boardoutcome_q1fy27.pdf | 18 | results | Board Outcome (Reg 30/33) + Unaudited Standalone & Consolidated Financial Results Q1 FY27 + Limited Review Reports |
| D2 | reg30_esop_allotment_q1fy27.pdf | 3 | results (Reg 30 event) | Allotment of 16,780 equity shares under ESOP 2022 + Annexure A |
| D3 | reg30_cfo_resignation_q1fy27.pdf | 3 | results (Reg 30 event) | Resignation of CFO Mr. Dhrumil PranavKumar Shah + Annexure A |
| D4 | reg30_aoa_adoption_q1fy27.pdf | 1 | results (Reg 30 event) | Board approval to adopt new Articles of Association (subject to AGM) |

Classification basis: D1 carries Reg 33 / "Unaudited Financial Results" / Board Outcome markers -> results. D2-D4 are single-topic Reg 30 event disclosures; no concall (speaker turns) or presentation (slide) markers present. Processed under `results` doctype (closest regulatory-filing fit) so each enters the line-numbered evidence spine and the forensic checklist. No concall or investor presentation was supplied (company is NO-CONCALL per manifest and Notion memory).

## Toolchain
pdftotext, pdfinfo, pdftoppm, tesseract — all MISSING at session start. Installed via apt-get (poppler-utils, tesseract-ocr) after `apt-get update` cleared stale 404s. All four verified present. Extraction proceeds normally.

## Protocol files (present)
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md (loaded but no concall this run)
- frameworks/Master_Project_Prompt_v3.3.md

## Company memory
No companies/526717.md file exists (never /finalize-d). Prior run folder: runs/526717-2026-07-15 (full evidence run). Manifest: CMP 194, mcap 207 cr, no concalls, sector row auto-tagged "Pharma/CDMO" (DEFECT — corrected to Packaging/FIBC in Notion).

## Live Notion thesis (fetched 2026-08-12; page 39fbb2b9-d3ab-815d-b7bf-ea258eb31581)
- **Decision Status: AVOID** (governance and leverage, not price). Evidence gate PROCEED WITH FLAGS. Position: None.
- CMP Rs 194 | mcap Rs 207 cr. Entry zone Rs 177-222 WITHDRAWN as value trap. MoS Rs 177.
- Gate 0: 27/100 core, 48/160 grand. Emerging Moat 12/100. FTTCP +6/8. Sector cap Packaging 22x.
- Promoter Verdict CONCERN. Devil DESTROYED. Confidence 63.
- Active flags: FLAG-GATE0 (binding leverage), FLAG-PROMOTER, FLAG-CASH (INDETERMINATE), FLAG-RPT, FLAG-GOVERNANCE, FLAG-DISCLOSURE, FLAG-EMOAT.

### Thesis-broken / re-engagement triggers
- Thesis broken: FY27 standalone OCF negative a 2nd consecutive year AND consolidated CFO reverts negative, with Net Debt/EBITDA above 3x.
- Re-engage: gearing below 2x, RPT concentration drops, CFO/PAT above 0.70x for two consecutive years.

### Monitoring checklist (passed inline to A3/A4)
1. Standalone & consolidated OCF; standalone turning positive alongside consolidated for two periods.
2. Net Debt/EBITDA below 3x, interest coverage above 3x; red if bank WC borrowings rise above Rs 98.68 cr.
3. Related-party COGS below 70.4% consolidated, revenue below 37.5%; red if RPT rises or new related-party financing added.
4. EBITDA margin at/above 9% for two full years; red below 7%.
5. Capacity utilisation disclosed and rising above FY25 31% base.
6. No further KMP/CS resignation within 12 months of the Jan-2026 CS exit; no repeat SEBI/BSE disclosure lapse.
7. Reported ROCE holds after adding RPT payables back to capital employed; red if collapses toward 18%.
8. Saudi Arabia BOPP Woven Bags JV: signed definitive agreement or committed capex vs continued silence.

### Governance sequence context (for A3/A4 weighing)
- Jan-2026: Company Secretary resigned citing unresolved concerns.
- 17-Jul-2026: Internal auditor (M/s S.A. Gadhia & Co) withdrew consent 7 weeks after appointment.
- 12-Aug-2026: CFO Mr. Dhrumil PranavKumar Shah resigns (THIS RUN, D3). **Directly touches monitoring item 6.** Orchestrator flags; A4 assesses; decision stays human.

## Gate log
- GATE A1 (per doc): PASS all 4 (100% page coverage: 18+3+3+1 pp). Units: results filing Lakhs (/100 -> Cr).
- GATE A2 (count test): PASS all 4 (results reconciled after tracing OCR undercounts on agenda_items 17->18 and line_items 143->149).
- GATE A3 (F1-F17 status + line cites): PASS all 4, 0 blank checks. 24 findings across 4 forensics files.
- A4: merged review PROCEED WITH FLAGS; cash conversion INDETERMINATE; Decision Status AVOID (flagged, not decided); 17 QFM rows; plain-language brief included.
- A5: loop 1 INCOMPLETE (JV Lakhs->Cr conversion error in PAT bridge; missing QFM row for A3-06) -> A4 fixed in place -> A5 re-audit COMPLETE (coverage/arithmetic/adversarial all PASS). GATE A5 PASS within 2-loop limit.
- Notion save: DONE (full review + plain-language brief + A3 forensics summary + A5 verdict appended; Key Notes prepended, prior entries preserved; Decision Status unchanged = AVOID).

## Monitoring-checklist firings this quarter
- ITEM 6 FIRED (RED): CFO resigned 12-Aug-2026 immediate/no successor = 3rd KMP exit in 7 months.
- ITEM 5 RED (non-disclosure): capacity utilisation not disclosed.
- ITEM 8 RED (continued silence): unnamed JV silent, Malaysia LLP dissolved, no Saudi JV update.
- ITEM 2 AMBER: coverage GREEN 5.68x but segment liabilities +Rs 183 cr QoQ, Net Debt/EBITDA ND.
- Thesis-broken trigger: NOT FIRED (cash-flow inputs unobservable at Q1). Re-test at Q2 FY27 half-year.
