# STAGE 0 — INPUT VALIDATION AND CORPUS AUDIT
**Company:** Insolation Energy Ltd (INA Solar) | **Ticker:** INA (NSE) / 543620 (BSE)
**CIN:** L40104RJ2015PLC048445 | **Run date:** 2026-09-06 | **Run type:** full
**CMP:** Rs 90.24 | **Market cap:** Rs 1,989.36 cr | **Face value:** Rs 1
**Run folder:** runs/ina-2026-09-06

## 0.1 SPEAR GATE

PASS. `companies/INA.md` carries `Spear: OVERRIDE 2026-09-06 (operator)`.
No spear pass ran on this name, so no load-bearing facts were named. This run
starts with no pre-set verification priority. Stage 0 sets the priority list
from the corpus inventory instead (Section 0.6).

## 0.2 MANIFEST

`manifest.yaml` exists and parses. Fields read:

| Field | Value |
|---|---|
| company | Insolation Energy Ltd |
| ticker | INA |
| cmp | 90.2 |
| market_cap_cr | 1989.0 |
| run_date | 2026-09-06 |
| run_type | full |
| concalls_available | true |
| sector_cap_row | "EV charging / energy transition equipment" |
| listed_date | "" (empty) |

## 0.3 FOLDER INVENTORY

| Folder | Contract | Found | Status |
|---|---|---|---|
| prospectus/ | 0-2 PDF | 0 | **GAP — HIGH** |
| annual-report/ | 0-1 PDF | 1 (200 pp, FY2026) | OK |
| results/ | 0-3 PDF | 0 | **GAP** |
| rating/ | 0-1 PDF | 0 | **GAP** |
| concalls/ | 0-3 PDF | 3 (22+18+21 pp) | OK |
| peer-concalls/ | 0-12 PDF | 11 | OK (partial, see 0.5) |
| announcements/ | 0-N PDF | 1 (2 pp) | OK (thin) |
| shareholding/ | 0-N | 0 | **GAP** |
| research/ | 0-N | 0 | GAP (non-anchored; no effect on evidence) |
| screening/ | 0-N | 24 CSV | OK with defect (see 0.5) |
| presentation/ | 0-N | 1 (32 pp) | OK |
| other/ | 0-N | 0 | n/a, never consumed |

Total corpus: 17 PDFs, 536 pages, all text-extractable. Zero unreadable files.

**PDF readability.** Every input PDF was pre-extracted to page-marked text at
`work/extracted/<folder>__<name>.txt` (header `SOURCE:` / `PAGES:`, body split
by `===== PAGE N =====`). Every file returned real text; none is image-only.
Tooling needed the LESSONS.md fix: `pypdf` absent, then the `_cffi_backend`
break, then `poppler-utils` on a second apt attempt. No verifier may skip
source verification on rendering grounds in this run.

### Concall chronology (oldest first, for stage 5)

| Order | File | Period covered |
|---|---|---|
| 1 | Concall_Jun_2025_Transcript.pdf | H2 and full year ended 31-Mar-2025 (FY25) |
| 2 | Concall_Feb_2026_Transcript.pdf | Q3 and 9M ended 31-Dec-2025 (Q3FY26) |
| 3 | Concall_Jun_2026_Transcript.pdf | Q4 and full year ended 31-Mar-2026 (FY26) |

### Listing history (bears on the prospectus gap)

- Incorporated 2015 (CIN L40104RJ2015PLC048445, Rajasthan).
- IPO during FY2022-23: 58,32,000 shares of Rs 10, Rs 5.83 cr, BSE SME platform
  (AR FY2026, share capital note (f)).
- Migrated from BSE SME to Main Board; shares listed on BSE and NSE
  **9 March 2026** (AR FY2026, p. 644-647, 680-682).
- Rs 395.20 cr preferential issue on 11-Dec-2024 (12,02,300 shares at Rs 3,287)
  (AR FY2026, share capital note (e)).
- Face value split Rs 10 to Rs 1 in FY2025.

`manifest.listed_date` is empty. The IPO is ~3.5 years before run_date, which
sits on the edge of the ~3-year RECENTLY-LISTED test. The main-board listing is
six months old. Stage 0 rules the prospectus a **HIGH-priority gap** on the
evidence-maximizing default: the pre-IPO restated financials and the full
promoter/group map exist nowhere else in this corpus, and the screener backward
series starts only at FY2022.

## 0.4 FRESHNESS PAIR CHECK

| # | Pair | Trigger present | Mate | Status |
|---|---|---|---|---|
| 1 | Newest results filing to same-quarter concall | see below | Q1FY27 concall | **FAIL** |
| 2 | Rating bulletin to full rationale | No (rating/ empty) | n/a | N/A, no trigger |
| 3 | SEBI order to order text | No (no SEBI order referenced anywhere in corpus) | n/a | N/A, no trigger |
| 4 | AR not older than latest audited annual results | AR FY2026 (YE 31-Mar-2026) | latest audited annual = FY2026 | **PASS** |

**Pair 1 reasoning.** `inputs/results/` is empty, so on a literal reading the
trigger document is absent and the pair does not fire. Stage 0 rules it FAIL on
substance. `screener-Data_Sheet.csv` carries a reported quarter ended
**30-Jun-2026 (Q1FY27)**: sales Rs 740.70 cr, net profit Rs 37.04 cr. That print
exists and is public as of the run date. Neither its results filing nor its
concall is in the corpus, and the newest concall held is Jun 2026, which covers
FY26, not Q1FY27. This is the MANINDS pattern the check was written for: a
newer primary filing that can move a decision variable before the model is
signed. The Q1FY27 print is not a minor refresh. Against Q4FY26 (sales Rs 793.93
cr, net profit Rs 70.07 cr) it shows net profit roughly halving on a 7% sales
decline. Every stage runs blind to the company's own explanation of that quarter.

**freshness_verdict: CORPUS GAPPED-FRESHNESS.**

Consequences, applied automatically:
- The phase-1 gate recommendation caps at PROCEED WITH CAVEATS regardless of
  flag count. A more severe verdict still stands on its own grounds.
- The missing mate is the first line of `outputs/final/gate-recommendation.md`.
- Missing documents named for the operator's Halt 1 upload list:
  **Q1FY27 results filing (quarter ended 30-Jun-2026)** and the
  **Q1FY27 earnings call transcript**, both from BSE/NSE filings or the
  company investor-relations page.

## 0.5 CORPUS DEFECTS

**D1 — Screening CSVs are header-only shells (collector defect, recurring).**
For the subject AND all three peers, `Profit_Loss.csv`, `Balance_Sheet.csv`,
`Cash_Flow.csv` and `Quarters.csv` contain column headers and empty rows only.
Identical byte counts across all four tickers confirm the shells. Only
`Data_Sheet.csv` is populated. This is the known `collect_to_repo v3` defect in
LESSONS.md. Mitigation: `Data_Sheet.csv` does carry FY2022-FY2026 P&L, balance
sheet and cash flow plus seven quarters to Q1FY27, so Gate 0 has a real backward
series. Stage 1 reads `screener-Data_Sheet.csv` and the AR financial statements,
not the empty shells.

**D2 — sector_cap_row is wrong.** The manifest sets "EV charging / energy
transition equipment". Insolation Energy makes solar modules and cells. The
operator's own manifest note records the row was set by hand and flags it. This
is the recurring collector defect. Recorded here and flagged for phase-3
confirmation; the Section 1B cap is ruled at stage 11, not here.

**D3 — Peer concall set is uneven.** 11 of a possible 12. WAAREEENER and
PREMIERENE have four transcripts each; WEBELSOLAR has three (Aug 2026, May 2026,
Feb 2026), with no Nov 2025 call. Stage 6 and verifier D work the set as given.

**D4 — Announcements folder is thin.** One document, and it is a two-page
Reg 30 covering letter dated 04-Sep-2026 that only points to the AR weblink. It
carries no material-event content. The documented-ACTION record for the
intent-and-action cross-check is effectively absent: no Reg 30 filings for the
Rs 780 cr borrowing increase, the capex programme, or the main-board migration.
Stages 5, 7 and 8 lose the 📄 action grade and run on AR and concall evidence.

**D5 — `No. of Equity Shares` blank for FY2026** in `screener-Data_Sheet.csv`.
Adjusted equity shares show 22.04 cr. Stage 1 and stage 10 must take the share
count from the AR share-capital note, not the blank cell.

## 0.6 FIRST VERIFICATION PRIORITY

No spear ran, so no load-bearing facts were handed down. Stage 0 sets the
priority list from the inventory. Every later stage checks these before its own
work. These are questions, not findings.

1. **FY2026 cash conversion.** `screener-Data_Sheet.csv` shows FY2026 net profit
   Rs 200.22 cr against cash from operating activity of **minus Rs 73.13 cr**,
   after FY2025 CFO of positive Rs 113.10 cr. Receivables Rs 110.09 cr to
   Rs 281.59 cr; inventory Rs 76.98 cr to Rs 379.05 cr. This is a FLAG-CASH
   determination the run must make on evidence: STRUCTURAL, GROWTH-INDUCED or
   INDETERMINATE.
2. **The FY2026 balance-sheet step-up.** Borrowings Rs 108.09 cr to Rs 887.91 cr;
   net block Rs 77.29 cr to Rs 524.89 cr; total assets Rs 847.39 cr to
   Rs 2,155.13 cr. What was built, what is commissioned, what is funded.
3. **The Q1FY27 profit drop the corpus cannot explain.** Net profit Rs 70.07 cr
   (Q4FY26) to Rs 37.04 cr (Q1FY27) on sales Rs 793.93 cr to Rs 740.70 cr. The
   corpus holds no filing or call for this quarter.
4. **Promoter and group history without a prospectus.** Stage 8 sources the
   group map from web search and the AR governance section, and must mark it
   web-derived, not filing-anchored.

## 0.7 DEGRADATION APPLIED

| Absent type | Degradation (per orchestrator DEGRADATION MAP) |
|---|---|
| prospectus | Stages 2 and 3 build notes and backward history from the AR alone. FTTCP backward baseline runs on post-listing years only and says so. Stage 8 sources promoter/group background from web search and AR governance, flagged web-derived. |
| results | Gate 0 (stage 1) runs from screening data and the AR financial statements. Stage 10 marks latest-period fields unresolved. |
| rating | Stage 10 marks `rating_wc_quote` unresolved. Stage 11 Pillar 2 proceeds without rating evidence, defaulting conservative. FLAG-CASH INDETERMINATE handling applies if cash conversion cannot be resolved. |
| shareholding | Stage 10 marks FII+DII unresolved. Stage 11 withholds the UA multiplier (all-three-qualifier rule). Promoter holding and pledge fall back to the AR figure with staleness noted. |
| research | No effect on anchored evidence. |
| announcements (thin) | Stages 5, 7, 8 lose the documented-ACTION record; intent-and-action cross-check runs on concall and AR evidence only. |

NO-CONCALL MODE does not apply. `concalls_available: true` and three transcripts
are present.

## 0.8 HALT CHECK

`manifest.yaml` parses and the inputs tree is not empty. **No mechanical halt.**
Four folders are empty and one is thin. The operator was asked once and answered
on 2026-09-06: proceed with the gaps. Recorded in `companies/INA.md`. The
question is not asked again in this run.

## 0.9 OPERATOR RULINGS CARRIED

- 2026-09-06: Spear OVERRIDE granted; pipeline runs shield-first on this name.
- 2026-09-06: Empty input folders accepted as gaps; run proceeds.

## COMPANY MEMORY

`companies/INA.md` exists but was created this run to satisfy the spear gate. It
carries no prior thesis, no decision status, no tripwires and no prior run. There
is no prior-run context: this is the first pipeline run on INA. Nothing in it is
evidence.

```yaml
stage: B00-inputs
company: INA
run_date: 2026-09-06
model: orchestrator-inline
status: complete
input_gaps:
  - type: prospectus
    severity: HIGH
    note: "IPO FY2022-23 on BSE SME; main-board listing 09-Mar-2026. Pre-IPO restated financials and full promoter/group map unavailable elsewhere. Backward series starts FY2022."
  - type: results
    severity: HIGH
    note: "0 of 2-3 PDFs. Q1FY27 print (QE 30-Jun-2026) exists per screener but no filing in corpus."
  - type: rating
    severity: MEDIUM
    note: "0 PDFs. No rating rationale for the FY26 borrowing step-up (Rs 108cr to Rs 888cr)."
  - type: shareholding
    severity: MEDIUM
    note: "0 files. FII+DII unresolved; UA multiplier withheld at stage 11; pledge trend falls back to AR."
  - type: research
    severity: LOW
    note: "0 files. Non-anchored source; no effect on evidence."
  - type: screening-csv-shells
    severity: MEDIUM
    note: "Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs header-only for subject and all 3 peers. Only Data_Sheet.csv populated. Known collect_to_repo v3 defect."
  - type: sector_cap_row-mismatch
    severity: MEDIUM
    note: "Manifest says 'EV charging / energy transition equipment'; company makes solar modules and cells. Flagged for phase-3 confirmation; Section 1B cap ruled at stage 11."
  - type: announcements-thin
    severity: MEDIUM
    note: "1 file, a 2-page Reg 30 AR-weblink letter with no material-event content. Documented-ACTION record effectively absent."
  - type: peer-concalls-partial
    severity: LOW
    note: "11 of 12. WEBELSOLAR has 3 (no Nov-2025 call); WAAREEENER and PREMIERENE have 4 each."
  - type: share-count-blank-FY26
    severity: LOW
    note: "screener-Data_Sheet 'No. of Equity Shares' blank for FY2026. Take share count from AR share-capital note."
freshness_pairs:
  - pair: "results-to-concall"
    trigger_doc: "Q1FY27 print (QE 30-Jun-2026) evidenced in screener-Data_Sheet.csv"
    mate_expected: "Q1FY27 results filing and Q1FY27 earnings call transcript"
    status: FAIL
    missing_doc: "Q1FY27 results filing (QE 30-Jun-2026) and its concall transcript"
  - pair: "rating-bulletin-to-rationale"
    trigger_doc: "none"
    mate_expected: "n/a"
    status: "N/A"
    missing_doc: ""
  - pair: "sebi-order-to-order-text"
    trigger_doc: "none; no SEBI order referenced in any corpus document"
    mate_expected: "n/a"
    status: "N/A"
    missing_doc: ""
  - pair: "ar-to-latest-audited-annual"
    trigger_doc: "Latest audited annual: FY2026 (YE 31-Mar-2026)"
    mate_expected: "AR FY2026"
    status: PASS
    missing_doc: ""
freshness_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_inventory:
  prospectus: 0
  annual_report: 1
  results: 0
  rating: 0
  concalls: 3
  peer_concalls: 11
  announcements: 1
  shareholding: 0
  research: 0
  screening: 24
  presentation: 1
  total_pdfs: 17
  total_pages: 536
  unreadable: 0
concalls_available: true
no_concall_mode: false
spear_gate: "PASS - OVERRIDE 2026-09-06 (operator); no load-bearing facts named"
listed_date_derived: "IPO FY2022-23 (BSE SME); main-board BSE+NSE listing 2026-03-09"
prior_run: none
flags:
  - id: FLAG-FRESHNESS
    severity: MEDIUM
    detail: "CORPUS GAPPED-FRESHNESS. Q1FY27 results and concall absent. Gate caps at PROCEED WITH CAVEATS."
analyst_note: "Corpus is AR-and-concall heavy and filing-light. No results, rating, shareholding or prospectus PDFs at all, so four of the eleven input types are empty and the documented-ACTION record is effectively absent. The backward series survives only because screener Data_Sheet.csv is populated FY2022-FY2026 while its four companion CSVs are empty shells. The single most consequential gap is the Q1FY27 quarter: the print exists publicly, shows net profit roughly halving against Q4FY26, and the corpus holds neither its filing nor its call. Every downstream stage reasons about a company whose newest disclosed quarter it cannot read."
```
