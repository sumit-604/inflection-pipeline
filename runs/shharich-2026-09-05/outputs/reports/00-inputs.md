# STAGE 0 — INPUT VALIDATION AND CORPUS AUDIT (B00)

Company: Shree Hari Chemicals Export Ltd (SHHARICH, BSE 524336). Run date: 2026-09-05.
Run type: full. CMP Rs 248.0. Market cap Rs 156 cr. concalls_available: false (NO-CONCALL MODE).
Sector cap row (manifest): "Specialty chemicals" (caveat recorded: H-Acid is a commodity
converter, Amendment 17 binds; no dye-intermediates cap row exists; open for operator ruling).

## SPEAR GATE
companies/SHHARICH.md did not exist at Phase 1 start. The run folder is a Step-1 intake product
(step1-business-brief.md present; corpus merged via PR #154). Step G of .claude/commands/step1.md
(the recorded override line) had not been written. Completed at Phase 1 start under the operator
standing ruling 2026-09-05 ("Step-1 intake replaces the web spear"):
`Spear: OVERRIDE 2026-09-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)`.
The four Step-1 load-bearing facts are the run's first verification priority (listed below).

## EMPTY-FOLDER CONFIRMATION
Standing answer applied per the Step-1 autonomy contract: "proceed with the gaps". This session
runs autonomously with no operator present; the pause is recorded, not asked. Empty folders:
prospectus (not expected, listed 1987), results, rating, announcements, shareholding, research,
presentation. concalls and peer-concalls: concalls declared unavailable; peer-concalls present.

## INVENTORY (by subfolder)
| folder | files | classification |
|---|---|---|
| prospectus/ | 0 | Not expected. Listed 1987 (39th AGM in Sep-2026). Not a gap. |
| annual-report/ | 2 PDF | `Annual_Report_2026_2.pdf` = Annual Report FY2025-26, 181 pp, Reg 34(1) submission dated 02-Sep-2026 (THE AR). `Annual_Report_2026.pdf` = 2-page Reg 30/36(1)(b) cover letter dated 02-Sep-2026 dispatching the 39th AGM notice (AGM 24-Sep-2026, VC) and AR web-link. It is an ANNOUNCEMENT misfiled as an AR (collector defect); usable as anchored evidence for the AGM date only. |
| results/ | 0 | ABSENT. No quarterly results filing. Q1 FY27 (Jun-2026) results, load-bearing fact 1, absent. FY26 audited annual results filing absent (AR carries the audited FY26 statements). |
| rating/ | 0 | ABSENT. |
| concalls/ | 0 | Declared unavailable (manifest). NO-CONCALL MODE. Not a gap. |
| peer-concalls/ | 9 PDF | SHREEPUSHK 4 transcripts (Nov-2025, Feb-2026, May-2026, Aug-2026; current). BODALCHEM 4 transcripts (Nov-2024, Feb-2025, May-2025, Aug-2025; newest ~13 months before run date). AKSHARCHEM 1 file `AKSHARCHEM-Concall_Aug_2019_Transcript.pdf` is an INVESTOR PRESENTATION dated August 2019, not a transcript, 7 years stale (collector mislabel). Effective transcripts: 8 across 2 peers. |
| announcements/ | 0 | ABSENT. Missing the documented-ACTION record: 25-Aug-2026 Reg 30 board outcome (Rs 40.24 cr preferential warrants to promoter group), 23-Mar-2026 SDPL rights subscription (Rs 4.95 cr), any postal-ballot/EGM notice. PARTIAL FILL: the AGM notice bound inside the AR (approx. PDF pp. 13-48) carries the preferential-issue resolution text and explanatory statement. |
| shareholding/ | 0 | ABSENT. Latest quarterly (Jun-2026) shareholding pattern missing. Fallback: AR shareholding pattern as at 31-Mar-2026 (staleness noted). UA institutional qualifier cannot be affirmed on current data. |
| research/ | 0 | ABSENT. Non-anchored source; no effect on evidence. .gitkeep planted. |
| screening/ | 24 CSV | Populated: `screener-Data_Sheet.csv` (SHHARICH; 3 annual years FY24, FY25, FY26; 10 quarters Mar-2024 to Jun-2026; BS, CF, price) and one Data_Sheet per peer (BODALCHEM, AKSHARCHEM, SHREEPUSHK). EMPTY TEMPLATES (collector defect, ignore): all Profit_Loss, Balance_Sheet, Cash_Flow, Quarters, Customization CSVs for SHHARICH and the three peers. |
| presentation/ | 0 | ABSENT. |
| other/ | 0 | none. |

PDF readability: pypdf 6.17.0 after the documented cffi reinstall (poppler absent). All 11 PDFs
extract text. Pre-extracted page-marked text for every PDF sits in `work/*.txt` (git-ignored),
marker `=== PAGE n ===` = PDF page index. Stages and verifiers may read the .txt; the PDF path is
the anchor of record. AR near-empty pages: 1 of 181.

## AR SECTION MAP (from text grep; approximate PDF pages)
Corporate overview and CMD letter pp. 1-12; AGM Notice pp. 13-48 (preferential warrant
resolutions pp. 43-48); Board's Report and annexures pp. 59-95 (AOC-1 p. 62/74, AOC-2 p. 64/71,
MD&A p. 65, Corporate Governance report pp. 78-95); Standalone auditor report p. 99 onward,
standalone statements pp. 96-138 (BS/PL/CF ~pp. 110-112, notes ~pp. 113-138, RPT ~pp. 128-129);
Consolidated statements pp. 139-181 (BS/PL/CF ~pp. 149-151, notes ~pp. 152-181, RPT ~pp. 167-168).
Promoter/board DINs found: B.C. Agrawal (CMD, 00121080), Sarthak Agarwal (03613314), Nihit
Agarwal (07586882), Vikas Agarwal (00089659). Subsidiary: Shakambhari Dyechem Pvt Ltd (SDPL).

## FRESHNESS PAIR CHECK
| pair | trigger_doc | mate_expected | status | missing_doc |
|---|---|---|---|---|
| 1 RESULTS to CONCALL | none present | same-quarter concall | SKIPPED | n/a (concalls_available false; no results filing present either) |
| 2 RATING BULLETIN to RATIONALE | none present | full rationale | PASS (no trigger) | none |
| 3 SEBI ORDER to ORDER TEXT | none referenced (AR grep: only a tax show-cause/demand notice in contingent liabilities) | order text | PASS (no trigger) | none |
| 4 AR to LATEST AUDITED ANNUAL | AR FY2025-26 | audited FY26 = latest audited year | PASS | none |
freshness_verdict: FRESHNESS PAIRS OK. Corpus verdict for 09b: CORPUS GAPPED (results, announcements,
shareholding absent; screening CSVs partly empty; peer set effectively 2 of 3), not GAPPED-FRESHNESS.

## DEGRADATION APPLIED
- No results: Gate 0 runs from screener Data_Sheet plus AR statements; stage 10 (phase 3) marks latest-period fields unresolved.
- No rating: stage 10 rating_wc_quote unresolved; Pillar 2 defaults conservative (phase 3).
- NO-CONCALL MODE: stage 5 degraded (AR MD&A, CMD letter, results commentary); credibility_grade defaults C, may rise to B only, never A; stage 6 runs on peer transcripts; verifier B audits against AR; stage 7 F2 test uses capex-completion evidence.
- No announcements: stages 5, 7, 8 lose the Reg 30 action record; AGM-notice resolutions inside the AR are the partial substitute; stage 8 relies on web search.
- No shareholding: FII+DII unresolved; UA withheld in phase 3; promoter holding from AR 31-Mar-2026.
- Screening partial: only Data_Sheet populated; 3 annual years.
- Peer set: AKSHARCHEM has no transcript (2019 presentation only); coverage map will show it.

## LOAD-BEARING FACTS (first verification priority, from Step-1 brief)
1. VOLUME VS SPREAD in the Q1 FY27 jump (sales Rs 54.91 cr, +126% YoY; PAT Rs 5.92 cr). Corpus carries only the screener quarter row for Jun-2026 and the FY26 AR; the Q1 FY27 filing is absent.
2. EXPANSION AND CAPITAL ALLOCATION: Rs 40.24 cr warrants at Rs 176.10 to promoter group; SDPL capex and product mix. Corpus: AR AGM-notice resolutions and explanatory statement; Reg 30 filing absent.
3. CASH CONVERSION AND CAPITALISED INTEREST: OCF vs PAT, receivables and inventory, capitalised interest, no dividend. Corpus: AR cash flow and notes.
4. SUBSIDIARY AND RELATED PARTY: SDPL financials (AOC-1), RPTs (AOC-2, notes), promoter money into the group. Corpus: AR.

```yaml
stage: B00-inputs
company: SHHARICH
run_date: 2026-09-05
model: orchestrator-session (claude-fable-5-1; stage 0 run by the orchestrator per run-pipeline.md step 1)
status: complete
spear_gate: "OVERRIDE 2026-09-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear); companies/SHHARICH.md written at Phase 1 start"
empty_folder_confirmation: "standing answer 'proceed with the gaps' applied (Step-1 autonomy contract); no operator present"
no_concall_mode: true
run_type: full
prior_run: none
company_memory: [companies/SHHARICH.md, runs/shharich-2026-09-05/step1-business-brief.md]
inventory:
  prospectus: {count: 0, note: "not expected; listed 1987"}
  annual_report: {count: 1, file: inputs/annual-report/Annual_Report_2026_2.pdf, year: FY2025-26, pages: 181, misfiled: "inputs/annual-report/Annual_Report_2026.pdf is a 2-page Reg 30/36(1)(b) AGM-notice dispatch letter dated 02-Sep-2026 (announcement, not an AR)"}
  results: {count: 0}
  rating: {count: 0}
  concalls: {count: 0, declared_unavailable: true}
  peer_concalls: {count: 9, effective_transcripts: 8, peers: {SHREEPUSHK: [Nov-2025, Feb-2026, May-2026, Aug-2026], BODALCHEM: [Nov-2024, Feb-2025, May-2025, Aug-2025], AKSHARCHEM: ["Aug-2019 INVESTOR PRESENTATION mislabeled as transcript; not a concall; 7y stale"]}}
  announcements: {count: 0}
  shareholding: {count: 0}
  research: {count: 0}
  screening: {count: 24, populated: [screener-Data_Sheet.csv, BODALCHEM-Data_Sheet.csv, AKSHARCHEM-Data_Sheet.csv, SHREEPUSHK-Data_Sheet.csv], empty_templates: "all Profit_Loss / Balance_Sheet / Cash_Flow / Quarters / Customization CSVs", annual_years: [FY24, FY25, FY26], quarters: "Mar-2024 to Jun-2026 (10)"}
  presentation: {count: 0}
  other: {count: 0}
input_gaps:
  - "results: no quarterly or annual results filing; Q1 FY27 (Jun-2026) results absent (load-bearing fact 1); FY26 audited annual results filing absent (AR carries audited FY26 statements)"
  - "rating: no credit rating document"
  - "announcements: no Reg 30 filings; 25-Aug-2026 board outcome on Rs 40.24 cr preferential warrants absent (load-bearing fact 2); 23-Mar-2026 SDPL rights subscription filing absent; AGM notice inside the AR is the partial substitute"
  - "shareholding: no quarterly shareholding pattern; Jun-2026 pattern absent; fallback AR pattern at 31-Mar-2026"
  - "research: none (non-anchored; no evidence effect)"
  - "presentation: none"
  - "screening: only Data_Sheet CSVs populated (3 annual years FY24-FY26); Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization CSVs are empty templates (collector defect)"
  - "peer-concalls: AKSHARCHEM file is an Aug-2019 investor presentation, not a transcript; peer transcript coverage effectively 2 of 3 peers (8 transcripts); BODALCHEM newest transcript Aug-2025 (~13 months stale)"
  - "annual-report: Annual_Report_2026.pdf misfiled (2-page AGM-notice dispatch letter, an announcement)"
  - "concalls: declared unavailable (NO-CONCALL MODE); not a gap"
  - "prospectus: not expected (listed 1987); not a gap"
freshness_pairs:
  - {pair: "RESULTS to CONCALL", trigger_doc: "none present", mate_expected: "same-quarter concall", status: SKIPPED, missing_doc: "n/a (concalls_available false)"}
  - {pair: "RATING BULLETIN to RATIONALE", trigger_doc: "none present", mate_expected: "full rating rationale", status: PASS, missing_doc: "none (no trigger)"}
  - {pair: "SEBI ORDER to ORDER TEXT", trigger_doc: "none referenced in AR", mate_expected: "order text", status: PASS, missing_doc: "none (no trigger)"}
  - {pair: "AR to LATEST AUDITED ANNUAL", trigger_doc: "Annual Report FY2025-26", mate_expected: "AR for latest audited year (FY26)", status: PASS, missing_doc: "none"}
freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict_for_09b: CORPUS GAPPED
load_bearing_facts:
  - "1 VOLUME VS SPREAD: split Q1 FY27 sales Rs 54.91 cr (+126% YoY) / PAT Rs 5.92 cr into H-Acid spread vs volume; if spread, spot-year ROCE must not feed Section 1B / FTTCP (v3.7 Amendment 17)"
  - "2 EXPANSION AND CAPITAL ALLOCATION: Rs 40.24 cr warrants at Rs 176.10 to promoter group vs CMP Rs 248; SDPL capex and product mix"
  - "3 CASH CONVERSION AND CAPITALISED INTEREST: OCF vs PAT, receivables and inventory trend, capitalised interest, no dividend"
  - "4 SUBSIDIARY AND RELATED PARTY: SDPL financials, RPTs with parent, promoter warrant money into the group"
pdf_extraction: "pypdf 6.17.0 (cffi reinstalled); all 11 PDFs readable; page-marked text in work/*.txt (git-ignored)"
flags: []
analyst_note: "Corpus is AR-heavy and filing-light. The two load-bearing facts the Step-1 thesis rests on (Q1 FY27 volume-vs-spread, the 25-Aug-2026 warrant filing) have no primary filing in the corpus; only the screener quarter row and the AGM-notice resolution text stand in. Every stage must say so where it leans on them."
```
