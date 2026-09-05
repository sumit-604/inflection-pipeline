# B00 — Input Validation and Corpus Audit — PITTIENG

Run: pittieng-2026-09-05 | Operator: Keerti Kaushik | Orchestrator stage 0.

## Spear gate
Spear: OVERRIDE 2026-09-05 (operator standing ruling 2026-09-05: Step-1
intake replaces the web spear). The /step1 intake for this name ran on
2026-09-05 and wrote runs/pittieng-2026-09-05/step1-business-brief.md, then
halted at the collector (mechanical browser-memory failure, recorded in the
brief). Its step G (create companies/<TICKER>.md with the OVERRIDE line) never
ran. The operator pushed the corpus afterwards and invoked /run-pipeline.
This session completed step G: companies/PITTIENG.md created from
companies/_template.md with the OVERRIDE line, the four load-bearing facts,
and the standing operator ruling. Gate satisfied. Run proceeds.

## Manifest
- company: Pitti Engineering Ltd | ticker: PITTIENG | BSE 513519 / NSE PITTIENG
- CIN L29253TG1983PLC004141 (AR FY26). 42nd AGM on 18-Sep-2026. Long listed;
  no prospectus expected.
- cmp: 1085.0 | market_cap_cr: 4085.0 | run_date: 2026-09-05
- run_type: full | concalls_available: true
- sector_cap_row: "Cables / Industrial products" (corrected by the step1 brief
  from the collector default "Pharma / CDMO"; flag for operator confirmation
  at Halt 1 / Phase 3)
- listed_date: not in manifest; company incorporated 1983 (CIN). Not recently
  listed.

## Operator confirmation (the single permitted question)
Asked once at stage 0, answered: "Proceed with these gaps (Recommended)".
Empty folders accepted as gaps. No further question is asked in this run.

## Folder inventory
| Folder | Count | Files used | Note |
|---|---|---|---|
| prospectus | 0 | none | Not expected (incorporated 1983, long listed). NOT a gap. |
| annual-report | 2 files, 1 AR | Annual_Report_2026_2.pdf (130 PDF pages, FY2025-26, filed 24-Aug-2026) | Annual_Report_2026.pdf is a 2-page Reg 36(1)(b) weblink letter, NOT an annual report (collector defect). The real AR carries two printed pages per PDF page: printed pp 1-238 on PDF pp 1-130. |
| results | 0 | none | ABSENT. Q1 FY27 results filing (Aug 2026) and FY26 audited results (May 2026) not in corpus. Quarter numbers reach stages via the Q1 FY27 investor presentation, the concalls and the screener Data_Sheet quarters row. |
| rating | 0 | none | ABSENT. No rating bulletin or rationale. Stage 10 rating_wc_quote unresolved (phase 3); FLAG-CASH INDETERMINATE guard applies if cash conversion questions arise. |
| concalls | 4 | Feb-2026 (Q3 FY26), May-2026 (Q4 and FY26), Aug-2026 (Q1 FY27): the 3 most recent, oldest first | Nov-2025 (Q2 FY26) available; not in stage 5 top-3 (contract cap 3); passed to stage 7 and verifier B as an extra. |
| peer-concalls | 12 | RKFORGE 4, SANSERA 4, VILAS 4 | Peers auto-selected by step1 (engine matched). |
| announcements | 0 | none | ABSENT. No Reg 30 record (acquisitions, capex approvals, order wins). Documented-ACTION cross-check runs on concall/AR/presentation only. |
| shareholding | 0 | none | ABSENT. UA institutional qualifier and pledge trend fall back to the AR FY26 corporate governance shareholding tables (as of 31-Mar-2026), staleness noted. |
| research | 0 | none | ABSENT. No anchored effect. .gitkeep planted. |
| screening | 6 company + 12 peer CSVs | screener-Data_Sheet.csv (FY20-FY26 P&L; FY21-FY26 BS and CF; quarters Mar-2024 to Jun-2026); RKFORGE-Data_Sheet.csv; SANSERA-Data_Sheet.csv | The separate Profit_Loss, Balance_Sheet, Cash_Flow, Quarters CSVs are header-only (empty) for company and both peers (collector defect). Customization.csv is a screener how-to sheet. VILAS has no screening CSVs in this run. |
| presentation | 1 | Investor_Presentation_1.pdf (30 pages, Q1 FY27, filed 10-Aug-2026) | Used by stages 4, 7, 9. |
| other | 0 | none | n/a |

## Text sidecars (reading copies)
Every PDF was extracted with pypdf to a page-marked text file at
inputs/_text/<folder>__<filename>.txt. Marker "===== PAGE N =====" gives the
PDF page index N. Stages and verifiers read the sidecar and anchor to the PDF
page; the PDF stays the source of record. Extraction verified: the AR
sidecar is 762 KB, transcripts 36-70 KB each, presentation 27 KB.

AR sidecar page map (PDF page index; printed page is about 2x minus 5):
- MD&A from PDF p.27 (printed 34). Directors' Report from PDF p.25-28
  (printed 44). BRSR PDF p.37-48 (printed 69). Corporate Governance report
  PDF p.49-59 (printed 92); shareholding tables PDF p.55-56.
- Standalone: auditor's report PDF p.60 (printed 114); Balance Sheet and
  P&L PDF p.65; Cash Flow PDF p.66-67; notes follow to about PDF p.91.
- Consolidated: Balance Sheet and P&L PDF p.96 (printed 179); Cash Flow
  PDF p.97-98; notes follow to PDF p.130. Related party note near PDF p.87
  (standalone) and in the consolidated notes; contingent liabilities PDF
  p.99-102; segment information PDF p.102 and p.114.
- Subsidiaries: Pitti Industries Private Limited (PIPL, material unlisted
  subsidiary) and Dakshin Foundry Private Limited (DFPL), both wholly owned
  (AR PDF p.25-26 Directors' Report; AOC-1 PDF p.25).

## Concall quarter map (chronological, confirmed from cover letters)
1. Concall_Nov_2025_Transcript.pdf = Q2 FY26 (call 10-Nov-2025) [extra; not in stage 5 top-3]
2. Concall_Feb_2026_Transcript.pdf = Q3 FY26 (call 6-Feb-2026)
3. Concall_May_2026_Transcript.pdf = Q4 and FY26 (call 18-May-2026)
4. Concall_Aug_2026_Transcript.pdf = Q1 FY27 (call 11-Aug-2026)
Stage 5 receives 2, 3, 4 oldest first.

## Peer concall map
- RKFORGE (Ramkrishna Forgings): Nov_2025 = Q2/H1 FY26; Feb_2026 = Q3 FY26; May_2026 = Q4 FY26; Jul_2026 = Q1 FY27.
- SANSERA (Sansera Engineering): Nov_2025 = Q2/H1 FY26; Feb_2026 = Q3 FY26; May_2026 = Q4 FY26; Aug_2026 = Q1 FY27.
- VILAS (Vilas Transcore): Nov_2024 = H1 FY25; May_2025 = FY25; Nov_2025 = H1 FY26; May_2026 = FY26.

## Input gaps
- results: ABSENT (MEDIUM). Latest-period numbers come from the Q1 FY27
  presentation, the concalls and the screener Data_Sheet quarters row; no
  results PDF anchors. Stage 10 latest-period fields unresolved in phase 3.
- rating: ABSENT (MEDIUM). No rating rationale for the working-capital and
  debt read. INDETERMINATE cash conversion, if it arises, caps at PROCEED
  WITH CAVEATS with "rating rationale" named as the missing evidence.
- announcements: ABSENT (MEDIUM). No documented-ACTION record. The Rs 290 Cr
  machined-components capex approval, the casting expansion, and any order
  wins are checked from concalls/AR/presentation only.
- shareholding: ABSENT (LOW). AR FY26 tables (31-Mar-2026) stand in; the
  Jun-2026 quarter pattern and pledge trend are not in corpus.
- research: ABSENT (none). Non-anchored source only.
- collector defects: Annual_Report_2026.pdf is a weblink letter, not an AR;
  screener Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs empty for
  company and peers (Data_Sheet populated); manifest sector_cap_row was
  auto-picked wrong and corrected by the brief.
- prospectus: not expected (long listed). Not a gap.

## Freshness pair check
| Pair | Trigger | Mate expected | Status | Missing |
|---|---|---|---|---|
| 1 Results->Concall | none (results/ empty) | same-quarter concall | PASS (no trigger); Q1 FY27 concall present regardless | none |
| 2 Rating->Rationale | none (rating/ empty) | full rationale | PASS (no trigger) | none |
| 3 SEBI order->text | none referenced (grep of AR, concalls, presentation: only labour-court matters at the Chhatrapati Sambhajinagar facility, AR BRSR, PDF p.44) | order text | PASS (no trigger) | none |
| 4 AR->latest audited annual | FY26 audited annual results (Q4 FY26 call 18-May-2026) | FY26 annual report | PASS (AR FY2025-26 present, filed 24-Aug-2026) | none |

freshness_verdict: FRESHNESS PAIRS OK. No freshness cap on the gate.

## Corpus audit verdict
CORPUS GAPPED. The AR FY26, four concalls, the Q1 FY27 presentation, twelve
peer transcripts and the screener Data_Sheet are present and readable. Four
document types are absent: results filings, rating rationale, exchange
announcements, shareholding pattern. None is a freshness-pair mate. Each is
findable on BSE (results, announcements, shareholding) or the rating agency
site (rationale) and goes on the operator's Halt 1 upload list.

## Load-bearing facts carried (COMPANY MEMORY leads; verify from corpus)
1. Guidance vs delivery: FY28 turnover above Rs 2,500 Cr at 90,000 tons,
   EBITDA margin 17-17.2%; FY27 EBITDA near Rs 370 Cr.
2. Cash conversion and the PAT dip: FY26 adjusted EBITDA up ~20% yet PAT
   fell; net debt Rs 525+ Cr guided down toward Rs 300 Cr.
3. Concentration: railway/traction ~40% of revenue via Wabtec and Alstom.
4. Capex funding and value-add proof: Rs 290 Cr machined-components program;
   casting capacity to 36,000 MT by Q1 FY29.
Every stage checks these before its own work; every number still comes from
this run's inputs.

```yaml
stage: B00-inputs
company: PITTIENG
run_date: 2026-09-05
model: orchestrator (claude-fable-5-1)
status: complete
run_type: full
concalls_available: true
listed_recently: false
incorporated: 1983 (CIN L29253TG1983PLC004141)
spear_gate: "OVERRIDE 2026-09-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear); companies/PITTIENG.md created this session (step1 step G completed here)"
operator_confirmation: "asked once at stage 0; answer: Proceed with these gaps"
sector_cap_row_manifest: "Cables / Industrial products"
sector_cap_row_note: "corrected by step1 brief from collector default Pharma / CDMO; confirm at Halt 1 / Phase 3"

inputs_present:
  annual_report: [FY26 (Annual_Report_2026_2.pdf, 130 PDF pages, filed 2026-08-24)]
  annual_report_nonreport_files: [Annual_Report_2026.pdf (2-page weblink letter, not an AR)]
  results: []
  rating: []
  concalls_used: [Feb-2026_Q3FY26, May-2026_Q4FY26, Aug-2026_Q1FY27]
  concalls_available_unused: [Nov-2025_Q2FY26 (passed to stage 7 and verifier B as extra)]
  peer_concalls: {RKFORGE: 4, SANSERA: 4, VILAS: 4}
  presentation: [Q1FY27_2026-08-10 (30 pages)]
  research: []
  screening_company: screener-Data_Sheet.csv (FY20-FY26 P&L, FY21-FY26 BS/CF, quarters Mar-2024..Jun-2026)
  screening_peers: [RKFORGE-Data_Sheet.csv, SANSERA-Data_Sheet.csv]
  screening_empty_csvs: [Profit_Loss, Balance_Sheet, Cash_Flow, Quarters (company and both peers, header-only)]
  shareholding: []
  announcements: []
  text_sidecars: inputs/_text/<folder>__<file>.txt (page-marked, PDF page index)

input_gaps:
  - type: results
    severity: MEDIUM
    reason: "no results PDFs; Q1FY27 and FY26 audited results reached only via presentation, concalls, screener quarters row"
  - type: rating
    severity: MEDIUM
    reason: "no rating rationale; WC/debt read has no agency anchor; INDETERMINATE cash conversion would cap at PROCEED WITH CAVEATS"
  - type: announcements
    severity: MEDIUM
    reason: "no Reg 30 record; capex approvals, acquisitions, order wins not filing-anchored"
  - type: shareholding
    severity: LOW
    reason: "AR FY26 tables (31-Mar-2026) stand in; Jun-2026 pattern and pledge trend absent"
  - type: research
    severity: NONE
    reason: "non-anchored source; no effect on evidence"
  - type: collector_defects
    severity: LOW
    reason: "AR weblink letter misfiled as AR; screener P&L/BS/CF/Quarters CSVs empty; sector_cap_row auto-pick wrong (corrected)"

freshness_pairs:
  - pair: results_to_concall
    trigger_doc: none (results/ empty)
    mate_expected: same-quarter concall
    status: PASS
    missing_doc: null
  - pair: rating_bulletin_to_rationale
    trigger_doc: none (rating/ empty)
    mate_expected: full rationale
    status: PASS
    missing_doc: null
  - pair: sebi_order_to_text
    trigger_doc: none referenced
    mate_expected: order text
    status: PASS
    missing_doc: null
  - pair: ar_to_latest_audited_annual
    trigger_doc: FY26 audited annual results (Q4FY26 call 2026-05-18)
    mate_expected: FY26 annual report
    status: PASS
    missing_doc: null

freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict: CORPUS GAPPED
gate_cap: none (no freshness failure)

concall_quarter_map:
  - {file: Concall_Nov_2025_Transcript.pdf, quarter: Q2 FY26, call_date: 2025-11-10, stage5: false}
  - {file: Concall_Feb_2026_Transcript.pdf, quarter: Q3 FY26, call_date: 2026-02-06, stage5: true}
  - {file: Concall_May_2026_Transcript.pdf, quarter: Q4 and FY26, call_date: 2026-05-18, stage5: true}
  - {file: Concall_Aug_2026_Transcript.pdf, quarter: Q1 FY27, call_date: 2026-08-11, stage5: true}

load_bearing_facts:
  - "FY28 turnover > Rs 2,500 Cr at 90,000 t, EBITDA margin 17-17.2%; FY27 EBITDA ~Rs 370 Cr (guidance vs delivery)"
  - "FY26 adj. EBITDA up ~20% yet PAT fell; net debt Rs 525+ Cr guided toward Rs 300 Cr (cash conversion)"
  - "Railway/traction ~40% of revenue via Wabtec and Alstom (concentration)"
  - "Rs 290 Cr machined-components capex; castings to 36,000 MT by Q1 FY29 (capex funding, value-add proof)"

flags: []
analyst_note: "Long-listed lamination maker turned integrated component platform; FY26 AR, four concalls, Q1FY27 presentation and screener Data_Sheet carry the run. No results, rating, announcements or shareholding filings: cash-conversion and UA evidence will be thinner than the AR alone can fix. No freshness failure; corpus is GAPPED, not GAPPED-FRESHNESS."
```
