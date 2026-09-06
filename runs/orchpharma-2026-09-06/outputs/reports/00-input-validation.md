# STAGE 0 — INPUT VALIDATION AND CORPUS AUDIT

Company: Orchid Pharma Ltd (ORCHPHARMA)
Run folder: runs/orchpharma-2026-09-06
Run date: 2026-09-06
Run type: full
CMP: Rs 954.65 (manifest Rs 955.0; screener Data_Sheet Rs 954.65)
Market cap: Rs 5,716.94 cr
Sector cap row (manifest): "Pharma / CDMO"

## 0.1 SPEAR GATE

Checked before any inventory, per CLAUDE.md SPEAR GATE and
prompts/00-orchestrator.md:145-164.

`companies/ORCHPHARMA.md` did not exist at run start. No Spear line existed
anywhere in the repository. The run stopped and the condition was reported to
the operator. The operator directed the pipeline to proceed.

Gate cleared under the OVERRIDE form:

    Spear: OVERRIDE 2026-09-06 (operator)

Recorded in `companies/ORCHPHARMA.md` at commit 58396df.

CONSEQUENCE FOR THIS RUN: no spear pass ran on live web, so no load-bearing
facts were named. The run carries NO pre-set first verification priority.
Every stage works to the standard evidence order. The pond, catch and price
steps that normally precede a heavy run were not performed, so this run
produces evidence without a prior opportunity-size guess to test it against.
Stage 09b and the gate recommendation must state this.

## 0.2 MANIFEST

manifest.yaml exists and parses. All required fields present.

    company: Orchid Pharma Ltd
    ticker: ORCHPHARMA
    cmp: 955.0
    market_cap_cr: 5717.0
    run_date: 2026-09-06
    run_type: full
    concalls_available: true
    sector_cap_row: "Pharma / CDMO"
    listed_date: ""

Manifest notes record: collected by collect_to_repo.py v3 on 2026-09-06;
sector row confirmed by hand; peers NEULANDLAB, KOPRAN, GRANULES chosen as
API-led, backward-integrated pharma; declared gaps results, rating,
announcements, shareholding, research; FY2026 AR not filed at run date.

SECTOR CAP NOTE. LESSONS.md records that collect_to_repo v3 defaults
sector_cap_row to "Pharma/CDMO" whichever the sector. Here the default and the
true sector coincide: Orchid Pharma is an API and finished-dosage pharma
maker. The manifest also states the row was confirmed by hand. The row stands
for this run. Phase 3 stage 11 must still confirm it against the live Section
1B cap table before it governs any multiple.

LISTED DATE. Field is empty. Company is long listed, not recently listed:
the screener export carries ten unbroken fiscal years of financials and
year-end prices from FY2017 to FY2026. An IPO prospectus is therefore NOT
expected and `inputs/prospectus/` being empty is NOT a gap under
RECENTLY-LISTED PRIORITY.

## 0.3 FOLDER INVENTORY

| Folder | Contract | Held | Status |
|---|---|---|---|
| prospectus | 0-2 | 0 | Not expected (long listed). Not a gap. |
| annual-report | 0-1 | 2 (FY2025, FY2024) | Above contract. Both retained. |
| results | 0-3 | 0 | GAP |
| rating | 0-1 | 0 | GAP |
| concalls | 0-3 | 4 | Above contract. See 0.4. |
| peer-concalls | 0-12 | 11 | Complete |
| announcements | 0-N | 0 | GAP |
| shareholding | 0-N | 0 | GAP |
| research | 0-N | 0 | GAP (non-anchored; no effect on evidence) |
| screening | 0-N | 24 CSV | Present, partly empty. See 0.5. |
| presentation | 0-N | 1 PDF | Present, low text yield. See 0.6. |
| other | 0-N | 0 | Nothing to preserve |

manifest.yaml present and parseable. inputs/ tree not empty. NO MECHANICAL
HALT CONDITION. The run proceeds degraded per the DEGRADATION MAP.

ANNUAL REPORT COUNT. The contract says 0-1; two are held (FY2025 and
FY2024). Two ARs is more evidence, not less. Both are passed to stages 2 and
3. FY2025 is the primary AR; FY2024 is the backward comparative. Stage 3's
backward deep dive gains a second filed year.

CONCALL COUNT. The contract says 0-3; four are held. Per the chronology
rule the three most recent are the main stage 5 set, with the fourth passed
as the backward comparative. Chronology confirmed in 0.4.

## 0.4 CONCALL CHRONOLOGY MAP

`concalls_available: true`. NO-CONCALL MODE does not apply.

Ordered oldest first, quarter derived from filename month and confirmed
against the screener quarterly series:

| # | File | Call month | Quarter covered |
|---|---|---|---|
| 1 | Concall_Nov_2025_Transcript.pdf | Nov 2025 | Q2 FY26 (Sep-2025 quarter) |
| 2 | Concall_Feb_2026_Transcript.pdf | Feb 2026 | Q3 FY26 (Dec-2025 quarter) |
| 3 | Concall_Jun_2026_Transcript.pdf | Jun 2026 | Q4 FY26 and FY26 full year |
| 4 | Concall_Aug_2026_Transcript.pdf | Aug 2026 | Q1 FY27 (Jun-2026 quarter) |

Stage 5 main set: Nov 2025, Feb 2026, Jun 2026, Aug 2026, passed oldest
first. The stage reads all four rather than dropping the oldest, because the
four calls are the only primary coverage the corpus holds for FY26, the year
the annual report does not reach.

Peer concall chronology:

| Peer | Calls held | Span |
|---|---|---|
| GRANULES | 4 | Nov 2025, Jan 2026, May 2026, Jul 2026 |
| NEULANDLAB | 4 | Nov 2025, Feb 2026, May 2026, Aug 2026 |
| KOPRAN | 3 | Nov 2024, Feb 2025, Mar 2025 |

KOPRAN COVERAGE NOTE. The three KOPRAN calls all predate April 2025. The
GRANULES and NEULANDLAB sets both run to mid-2026. KOPRAN's peer evidence is
therefore roughly 18 months staler than the other two and cannot speak to
FY26 or FY27 conditions. Stage 6 and verifier D must weight KOPRAN
accordingly and must not read a FY25 KOPRAN statement as current.

## 0.5 SCREENING DATA AUDIT

24 CSV files, four companies (ORCHPHARMA as "screener", plus GRANULES,
KOPRAN, NEULANDLAB), six exports each.

KNOWN COLLECTOR DEFECT CONFIRMED. LESSONS.md records that collect_to_repo v3
ships empty screener P&L, Balance_Sheet, Cash_Flow and Quarters CSVs with only
Data_Sheet populated. That defect is present here for all four companies:

| Export | Populated? |
|---|---|
| Data_Sheet.csv | YES. Full ten-year P&L, ten-quarter series, balance sheet, cash flow, price, derived share count. |
| Profit_Loss.csv | NO. Row labels only, every value blank. |
| Balance_Sheet.csv | NO. Row labels only. |
| Cash_Flow.csv | NO. Row labels only. |
| Quarters.csv | NO. Row labels only. |
| Customization.csv | NO. Template only. |

EVIDENCE-MAXIMIZING OVERRIDE, per the LESSONS.md recurring-pattern rule:
`<TICKER>-Data_Sheet.csv` is the sole populated screener source and every
stage that would otherwise read Profit_Loss, Balance_Sheet, Cash_Flow or
Quarters reads Data_Sheet instead. The four empty exports carry no
information; a stage must not report a value as NOT FOUND merely because the
named file is empty when Data_Sheet holds it.

DATA_SHEET COVERAGE (ORCHPHARMA):
- P&L: FY2017 to FY2026, ten fiscal years, annual.
- Quarters: Mar-2024 to Jun-2026, ten quarters.
- Balance sheet: FY2017 to FY2026.
- Cash flow: FY2017 to FY2026.
- Year-end price: FY2017 to FY2026.
- Share count: FY2017 to FY2025 populated; FY2026 blank in `No. of Equity
  Shares`, but `Adjusted Equity Shares in Cr` carries 5.07 for FY2026.
- Face value Rs 10. Current price Rs 954.65. Market cap Rs 5,716.94 cr.

DATA_SHEET FIELD GAPS (mechanical, recorded not filled):
- `Number of shares` (META): blank.
- `Dividend Amount`: blank every year.
- `Tax`: blank in FY2019 to FY2023.
- FY2026 `Power and Fuel`, `Other Mfr. Exp`, `Selling and admin`: blank,
  while `Other Expenses` jumps to 237.10 from 11.40. The FY2026 cost
  breakdown appears collapsed into one line rather than genuinely absent.
  Stage 1 and stage 10 must not read this as a real FY2026 cost explosion in
  "other expenses" without a primary source. NO PRIMARY FY2026 SOURCE EXISTS
  IN THIS CORPUS (see 0.7). The FY2026 cost split is NOT FOUND.

## 0.6 PDF EXTRACTION AUDIT

pypdf was unavailable at session start and its cffi backend was broken, the
recurring failure LESSONS.md names. Fixed by upgrading cffi. All 18 corpus
PDFs were then pre-extracted to page-marked text under `work/text/`, per the
LESSONS.md reliable default, so no stage or verifier hits the image-render
wall. Each extract carries `===== PAGE n =====` markers, so a page anchor in
a stage report maps to the source PDF page.

| Document | Pages | Extracted chars | Verdict |
|---|---|---|---|
| Annual_Report_2024.pdf | 318 | 932,912 | Good |
| Annual_Report_2025.pdf | 300 | 855,567 | Good |
| Concall_Nov_2025 | 14 | 36,640 | Good |
| Concall_Feb_2026 | 18 | 48,039 | Good |
| Concall_Jun_2026 | 16 | 44,690 | Good |
| Concall_Aug_2026 | 18 | 47,290 | Good |
| GRANULES x4 | 15-18 | 35,314-48,455 | Good |
| KOPRAN x3 | 10-14 | 24,172-36,254 | Good |
| NEULANDLAB x4 | 15-19 | 46,039-56,535 | Good |
| Investor_Presentation_1.pdf | 14 | 3,124 | LOW YIELD |

PRESENTATION LOW YIELD. 3,124 characters across 14 pages is about 223
characters per page. The deck is image based; its slides carry text as
pictures that text extraction cannot reach. Stage 4 must treat the
presentation as near-absent and build the business model from the annual
reports and concalls. Any figure a stage claims from the presentation must be
checked against the page-marked extract before it is anchored. Verifier A
must not accept a presentation anchor it cannot find in the text.

Source PDFs remain in place; the text extracts are a convenience layer, not a
replacement. Verifier A audits against the source PDFs.

## 0.7 FRESHNESS PAIR CHECK

Run per the orchestrator FRESHNESS PAIR CHECK section, after the inventory.

**Pair 1 — RESULTS to CONCALL.** `inputs/results/` is empty, so the pair has
no trigger document in the corpus. Cannot fail on its own terms.
Status: NO TRIGGER. The empty results folder is recorded as an input gap in
its own right.

**Pair 2 — RATING BULLETIN to RATIONALE.** `inputs/rating/` is empty, so no
bulletin triggers the pair. Status: NO TRIGGER. Recorded as an input gap. Its
consequence is carried under FLAG-CASH: the rating rationale is the usual
evidence that resolves an INDETERMINATE cash-conversion determination, and it
is absent.

**Pair 3 — SEBI ORDER to ORDER TEXT.** No SEBI order is visible at stage 0,
which reads no filing narrative. Status: PENDING STAGE EVIDENCE. Stages 2, 3
and 8 must surface any SEBI or regulatory order referenced in the annual
reports or concalls; any such reference with no order text in the corpus
fails this pair retrospectively and must be named in the 09b dossier.

**Pair 4 — AR to LATEST AUDITED ANNUAL RESULTS. FAIL.**

The newest annual report in the corpus is FY2025. The screener Data_Sheet,
itself a corpus document, carries a complete audited FY2026 column: sales
1,232.78, PBT 10.43, net profit 9.96, and a full FY2026 balance sheet and
cash flow dated 2026-03-31. FY2026 audited annual results therefore exist and
were filed. The corpus holds neither the FY2026 annual report nor the FY2026
audited annual results filing. The annual report held trails the latest
audited annual results by one full year. The pair fails.

MISSING DOCUMENT: **Orchid Pharma FY2026 audited annual results filing (Q4
FY26 / full-year Reg 33 submission), and the FY2026 Annual Report when
filed.** Expected source: BSE/NSE corporate filings, or the company investor
relations page. The manifest records that the FY2026 AR was not yet filed at
run date, so the results filing is the document that can actually be pushed
now.

WHY THIS MATTERS FOR THIS RUN. FY2026 is the year the corpus is thinnest on
and the year the numbers moved most. Against FY2025 the screener shows sales
up 33.7% to 1,232.78, PBT down from 95.56 to 10.43, capital work in progress
up from 80.71 to 340.52, and borrowings up from 174.61 to 362.59. The corpus
holds no audited FY2026 statements, no FY2026 notes to accounts, no FY2026
related-party schedule and no FY2026 contingent-liability schedule. The four
concall transcripts are the only primary FY2026 narrative coverage, and a
transcript is management commentary, not an audited statement. Every FY2026
balance-sheet or accounting-quality judgment in this run rests on screener
aggregates alone.

**freshness_verdict: CORPUS GAPPED-FRESHNESS**

CONSEQUENCES, binding on later steps:
1. The 09b dossier Section 1 verdict line reads CORPUS GAPPED-FRESHNESS.
2. The gate recommendation caps at PROCEED WITH CAVEATS regardless of flag
   count. A more severe verdict still stands on its own grounds.
3. The missing document above is the FIRST line of
   `outputs/final/gate-recommendation.md`, before any flag block.

## 0.8 DEGRADATION MAP APPLIED

| Absent | Rule applied |
|---|---|
| results | Gate 0 runs from screener Data_Sheet. Stage 10 marks latest-period fields unresolved in phase 3. |
| rating | Stage 10 marks rating_wc_quote unresolved. Phase 3 Pillar 2 proceeds without rating evidence, defaulting conservative. FLAG-CASH INDETERMINATE handling applies. |
| announcements | Stages 5, 7, 8 lose the documented-ACTION record. The intent-and-action cross-check runs on concall and AR evidence only and cannot grade recent Reg 30 actions. Stage 8 relies on web search for material events. |
| shareholding | Stage 10 marks FII+DII unresolved. Phase 3 stage 11 cannot affirm the UA institutional-absence qualifier, so UA is WITHHELD under the all-three-qualifier rule. Promoter holding and pledge fall back to the FY2025 AR figure with staleness noted. |
| research | No effect on anchored evidence. |
| prospectus | Not expected; company long listed. No degradation. |
| presentation (low yield) | Stage 4 builds from the two annual reports and four concalls. Presentation treated as near-absent. |
| screener P&L/BS/CF/Quarters empty | Overridden to Data_Sheet, which holds the same series populated. No real degradation. |

## 0.9 EMPTY-FOLDER CONFIRMATION

Five input folders are empty: results, rating, announcements, shareholding,
research. Prospectus is empty but not expected.

The orchestrator's single permitted question was NOT asked in this run. The
operator answered it in advance with the instruction to continue and not
stop, given on 2026-09-06 alongside the spear override. Recorded as an
operator ruling in `companies/ORCHPHARMA.md`. The run proceeds with the gaps
above rather than pausing to collect. The gaps go on the operator's upload
list at Halt 1.

## 0.10 FIRST VERIFICATION PRIORITY

Normally the Spear line's load-bearing facts are the run's first
verification priority. This run has an OVERRIDE and no named facts, so no
pre-set priority exists.

In its place, stage 0 records the corpus-derived question every later stage
must carry, stated as a question and not as a finding, because stage 0 does
no analysis: FY2026 revenue rose about 34% while pre-tax profit fell about
89%, capital work in progress rose about 4x and borrowings roughly doubled,
all per the screener Data_Sheet and all unverified against any primary FY2026
filing, because none is in the corpus. Every stage that touches FY2026 states
which source it used and whether the source is primary.

## 0.11 SCAFFOLD

Created: `outputs/blocks/`, `outputs/reports/`, `outputs/final/`,
`work/text/`. Planted `inputs/research/.gitkeep`.

No COMPANY MEMORY of substance exists: `companies/ORCHPHARMA.md` was created
at this run start and carries only the spear override and two operator
rulings. It is passed to stages as COMPANY MEMORY with that stated, so no
stage mistakes it for prior-run evidence. `run_type` is `full`, not
`refresh`, so no PRIOR RUN CONTEXT applies.

```yaml
stage: B00-inputs
company: ORCHPHARMA
run_date: 2026-09-06
model: claude-opus-5
status: complete
spear_gate:
  form: OVERRIDE
  line: "Spear: OVERRIDE 2026-09-06 (operator)"
  recorded_at: companies/ORCHPHARMA.md
  commit: 58396df
  load_bearing_facts: []
  note: "No spear pass ran. No pre-set first verification priority for this run."
manifest:
  parses: true
  company: Orchid Pharma Ltd
  ticker: ORCHPHARMA
  cmp: 954.65
  cmp_source: "inputs/screening/screener-Data_Sheet.csv META Current Price"
  market_cap_cr: 5716.94
  run_type: full
  concalls_available: true
  sector_cap_row: "Pharma / CDMO"
  sector_cap_confirmed_hand: true
  sector_cap_phase3_recheck_required: true
  listed_date: ""
  listed_recently: false
  listed_evidence: "screener Data_Sheet carries FY2017-FY2026 financials and year-end prices"
inventory:
  prospectus: 0
  annual_report: 2
  results: 0
  rating: 0
  concalls: 4
  peer_concalls: 11
  announcements: 0
  shareholding: 0
  research: 0
  screening: 24
  presentation: 1
  other: 0
input_gaps:
  - "results: no quarterly or annual results filing in corpus"
  - "rating: no credit rating bulletin or rationale in corpus"
  - "announcements: no exchange / Reg 30 filings in corpus"
  - "shareholding: no quarterly shareholding pattern in corpus"
  - "research: no broker notes in corpus (non-anchored; no evidence effect)"
  - "screening: Profit_Loss, Balance_Sheet, Cash_Flow, Quarters CSVs are empty templates for all four companies (collect_to_repo v3 defect); Data_Sheet is the sole populated screener source and is used in their place"
  - "presentation: Investor_Presentation_1.pdf is image-based, 3124 chars over 14 pages; treated as near-absent for stage 4"
  - "FY2026 primary filings absent: no FY2026 annual report and no FY2026 audited annual results filing; FY2026 figures available only as screener aggregates"
  - "FY2026 cost breakdown (Power and Fuel, Other Mfr. Exp, Selling and admin) blank in Data_Sheet with Other Expenses at 237.10 vs 11.40 prior year; FY2026 cost split is NOT FOUND"
  - "KOPRAN peer concalls all predate Apr-2025, roughly 18 months staler than the GRANULES and NEULANDLAB sets"
not_gaps:
  - "prospectus: company long listed (FY2017-FY2026 price history); IPO prospectus not expected"
freshness_pairs:
  - pair: "RESULTS to CONCALL"
    trigger_doc: "none in corpus (inputs/results/ empty)"
    mate_expected: "same-quarter concall transcript"
    status: NO TRIGGER
    missing_doc: ""
  - pair: "RATING BULLETIN to RATIONALE"
    trigger_doc: "none in corpus (inputs/rating/ empty)"
    mate_expected: "full rating rationale"
    status: NO TRIGGER
    missing_doc: ""
  - pair: "SEBI ORDER to ORDER TEXT"
    trigger_doc: "not determinable at stage 0"
    mate_expected: "order text for any order referenced in filings"
    status: PENDING STAGE EVIDENCE
    missing_doc: ""
    note: "stages 2, 3, 8 must surface any referenced regulatory order; an unmatched reference fails this pair retrospectively"
  - pair: "AR to LATEST AUDITED ANNUAL RESULTS"
    trigger_doc: "FY2026 audited annual results, evidenced by the complete FY2026 column in inputs/screening/screener-Data_Sheet.csv (sales 1232.78, PBT 10.43, balance sheet and cash flow dated 2026-03-31)"
    mate_expected: "FY2026 annual report, or the FY2026 audited annual results filing"
    status: FAIL
    missing_doc: "Orchid Pharma FY2026 audited annual results filing (Q4 FY26 / full-year Reg 33), and the FY2026 Annual Report when filed. Source: BSE/NSE corporate filings or company IR page."
freshness_verdict: CORPUS GAPPED-FRESHNESS
gate_cap_applied: "PROCEED WITH CAVEATS (freshness cap; more severe verdicts still stand)"
no_concall_mode: false
concall_chronology:
  - {file: "inputs/concalls/Concall_Nov_2025_Transcript.pdf", call_month: "Nov 2025", quarter: "Q2 FY26"}
  - {file: "inputs/concalls/Concall_Feb_2026_Transcript.pdf", call_month: "Feb 2026", quarter: "Q3 FY26"}
  - {file: "inputs/concalls/Concall_Jun_2026_Transcript.pdf", call_month: "Jun 2026", quarter: "Q4 FY26 + FY26 full year"}
  - {file: "inputs/concalls/Concall_Aug_2026_Transcript.pdf", call_month: "Aug 2026", quarter: "Q1 FY27"}
peer_set:
  - {peer: GRANULES, calls: 4, span: "Nov 2025 - Jul 2026"}
  - {peer: NEULANDLAB, calls: 4, span: "Nov 2025 - Aug 2026"}
  - {peer: KOPRAN, calls: 3, span: "Nov 2024 - Mar 2025", note: "stale relative to the other two"}
text_extracts:
  path: "work/text/"
  files: 18
  page_markers: "===== PAGE n ====="
  note: "convenience layer; verifier A audits against the source PDFs"
degradation_applied:
  - "Gate 0 runs from screener Data_Sheet (no results PDFs)"
  - "stage 4 builds from annual reports and concalls (presentation near-absent)"
  - "stage 10 will mark latest-period fields, rating_wc_quote and FII+DII unresolved in phase 3"
  - "UA withheld in phase 3: no shareholding pattern, institutional-absence qualifier cannot be affirmed"
  - "stages 5, 7, 8 lose the documented-ACTION record (no announcements)"
operator_rulings_this_run:
  - "2026-09-06: spear gate overridden; pipeline proceeds without a live-web spear pass"
  - "2026-09-06: empty-folder confirmation answered in advance; proceed with declared gaps, do not pause"
halt: false
flags: []
analyst_note: "Corpus is strong on narrative and weak on FY2026 primary filings. Two annual reports and four own concalls cover the business well through FY2025 and give management's FY2026 account, but no audited FY2026 statement exists anywhere in the corpus while the screener shows FY2026 as the year of largest change. Pair 4 fails on that basis and caps the gate. The empty screener P&L/BS/CF/Quarters files are a known collector defect, not missing data: Data_Sheet holds the same series and every stage reads it instead. The investor presentation is image-based and cannot be relied on for figures."
```
