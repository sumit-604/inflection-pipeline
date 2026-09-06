# STAGE 0 — INPUT VALIDATION AND CORPUS AUDIT
## CYIENTDLM (Cyient DLM Ltd) — run 2026-09-06

Performed inline by the orchestrator. No subagent.

## SPEAR GATE

`companies/CYIENTDLM.md` carries:

```
Spear: OVERRIDE 2026-09-06 (operator)
```

The gate is satisfied by operator override. No Claude web spear pass was run.
NO LOAD-BEARING FACTS were supplied. This run therefore carries no pre-set
verification priority list. Every stage works from the corpus alone.

## MANIFEST

| Field | Value |
|---|---|
| company | Cyient DLM Ltd |
| ticker | CYIENTDLM |
| cmp | Rs 857.00 |
| market_cap_cr | Rs 6,803 cr |
| run_date | 2026-09-06 |
| run_type | full |
| sector_cap_row | "Cables / Industrial products" (25x) |
| concalls_available | true |
| listed_date | "" (empty in manifest) |

`manifest.yaml` exists and parses. `inputs/` is not empty. No halt condition.

LISTED DATE DERIVED: the manifest field is empty. AR FY2024-25 states "With
the launch of the IPO (Initial Public Offering) in FY 2023-24, Cyient DLM
created significant value to our investors" (AR FY2024-25, chairman/MD
letter). The IPO therefore fell in FY2023-24, roughly 3.2 years before
run_date. This sits at the RECENTLY-LISTED PRIORITY boundary. The manifest
notes already declare the prospectus a HIGH-priority gap. Stage 0 confirms
that classification.

SECTOR CAP CAVEAT (carried from manifest notes): no ESDM/EMS row exists in
the Section 1B cap table. "Cables / Industrial products" (25x) was taken by
hand as the conservative fit. The aerospace-and-defence revenue mix may argue
the Defence / strategic row (38x). This is a PHASE 3 confirmation item. No
phase 1 stage sets an exit multiple.

## FOLDER INVENTORY

| Folder | Contract | Held | Status |
|---|---|---|---|
| prospectus | 0-2 | 0 | **ABSENT — HIGH-priority gap** |
| annual-report | 0-1 | 2 | Over contract. Both retained |
| results | 0-3 | 0 | ABSENT |
| rating | 0-1 | 0 | ABSENT |
| concalls | 0-3 | 4 | Over contract. 3 most recent to stage 5 |
| peer-concalls | 0-12 | 12 | Full |
| announcements | 0-N | 0 | ABSENT |
| shareholding | 0-N | 0 | ABSENT |
| research | 0-N | 0 | ABSENT (no effect on anchored evidence) |
| screening | 0-N | 20 CSV | PARTIAL — see defect below |
| presentation | 0-N | 1 | Present, image-heavy |
| other | 0-N | 0 | Absent. Never consumed, not a gap |

Operator ruling 2026-09-06: the empty folders are accepted as gaps. The
operator declined to push the missing documents before the run.

### Annual reports (both retained)

Year labels verified against the document text, per the standing collector
defect (LESSONS: mislabeled AR year).

| File | Cover text | Pages | Role |
|---|---|---|---|
| Annual_Report_2026.pdf | "ANNUAL REPORT FY2025-26" | 174 | PRIMARY (latest) |
| Annual_Report_2025.pdf | "ANNUAL REPORT FY2024-25" | 287 | Backward baseline |

Both labels are CORRECT. No override needed.

### Concall quarter map (verified from each transcript's first page)

Oldest first:

| # | File | Call date | Quarter |
|---|---|---|---|
| 1 | Concall_Oct_2025_Transcript.pdf | 14 Oct 2025 | Q2 FY26 |
| 2 | Concall_Jan_2026_Transcript.pdf | 20 Jan 2026 | Q3 FY26 |
| 3 | Concall_Apr_2026_Transcript.pdf | 21 Apr 2026 | Q4 FY26 |
| 4 | Concall_Jul_2026_Transcript.pdf | 21 Jul 2026 | Q1 FY27 |

Stage 5 takes the 3 most recent (Q3 FY26, Q4 FY26, Q1 FY27), oldest first.
The Q2 FY26 call stays available to stages 7 and to verifier B.

### Peer concalls (12, all three peers, 4 calls each)

AVALON: Nov 2025, Feb 2026, May 2026, Aug 2026.
KAYNES: Dec 2025, Feb 2026, May 2026, Aug 2026.
SYRMA: Nov 2025, Feb 2026, Jun 2026, Aug 2026.

### Screening data — COLLECTOR DEFECT CONFIRMED

`screener-Profit_Loss.csv`, `screener-Balance_Sheet.csv`,
`screener-Cash_Flow.csv` and `screener-Quarters.csv` carry HEADER ROWS ONLY.
No data. The same holds for all three peers. This is the standing
collect_to_repo v3 defect recorded in LESSONS.

`screener-Data_Sheet.csv` IS populated and carries:
- Annual P&L, balance sheet and cash flow for FY2023, FY2024, FY2025, FY2026
  (four years, report dates 2023-03-31 through 2026-03-31)
- Ten quarters, Q4 FY24 (2024-03-31) through Q1 FY27 (2026-06-30)
- Share count, face value, CMP Rs 856.95, market cap Rs 6,802.76 cr

Peer Data_Sheet files are likewise populated (AVALON, KAYNES, SYRMA).

CONSEQUENCE: Gate 0 (stage 1) has usable screening data from Data_Sheet, but
only FOUR years of annual history, not ten. The company listed in FY2023-24,
so no longer public series exists in the screener file. Stage 1 must set
`data_years: 4` and apply `history_downgrade` per its own rules, and must
supplement from the AR FY2025-26 and AR FY2024-25 financial statements where
the four-year series is too short for a trend test. `inputs/results/` is
empty, so the DEGRADATION MAP fallback for Gate 0 is the annual report
financial statements.

## FRESHNESS PAIR CHECK

| # | Pair | Trigger present | Mate | Status |
|---|---|---|---|---|
| 1 | Newest results filing to same-quarter concall | NO — `inputs/results/` is empty | n/a | NO TRIGGER |
| 2 | Rating bulletin to full rationale | NO — `inputs/rating/` is empty | n/a | NO TRIGGER |
| 3 | Referenced SEBI order to order text | NO — no SEBI order, penalty, adjudication or show-cause reference found in AR FY2025-26 | n/a | NO TRIGGER |
| 4 | AR not older than latest audited annual results | AR FY2025-26 (year ended 31 March 2026) held | No audited annual results filing newer than FY26 in corpus | **PASS** |

**freshness_verdict: FRESHNESS PAIRS OK**

No pair fails. The gate recommendation is NOT capped by the freshness rule.

Read the verdict precisely. Pairs 1 to 3 do not fire because the TRIGGER
document is itself absent. That absence is a plain document-type gap, already
recorded in `input_gaps`, not a freshness failure. The freshness rule catches
a present filing whose companion is missing. Here whole document types are
missing, which the corpus audit verdict below carries instead.

## CORPUS AUDIT VERDICT

**CORPUS GAPPED.**

Six document types are absent: prospectus, results, rating, announcements,
shareholding, research. The prospectus gap is HIGH priority.

## DEGRADATION APPLIED (per orchestrator DEGRADATION MAP)

- **No prospectus (HIGH).** Stages 2 and 3 build the notes and backward
  history from the two annual reports alone, so from FY2024-25 and FY2025-26
  and whatever comparatives they carry. The FTTCP backward baseline runs on
  post-listing years only and must say so. Stage 8 sources promoter and group
  background from web search and the AR governance section, and flags the
  group-company map as web-derived, not filing-anchored.
- **No results.** Gate 0 runs from `screener-Data_Sheet.csv` plus the AR
  financial statements. Stage 10 (phase 3) marks latest-period fields
  unresolved.
- **No rating.** Stage 10 marks `rating_wc_quote` unresolved. Phase 3
  Pillar 2 proceeds without rating evidence, conservative default. FLAG-CASH
  INDETERMINATE handling applies if cash evidence is short.
- **No announcements.** Stages 5, 7 and 8 lose the documented-ACTION record.
  The intent-and-action cross-check runs on concall and AR evidence only and
  cannot grade recent documented actions. Stage 8 relies on web search for
  material events.
- **No shareholding filing, PARTLY SUBSTITUTED.** The standard degradation
  does not apply in full. The AR FY2025-26 corporate governance section carries
  the ownership-category table at 31 March 2026 (AR FY2025-26, p.100) and the
  over-1% shareholder list (AR FY2025-26, p.101). FII+DII is therefore
  derivable and anchored, one quarter stale against a Q1FY27 filing. Stage 10
  should populate FII+DII from the AR with the staleness noted, not mark it
  unresolved. Phase 3 may test the UA institutional qualifier on that basis and
  must state the as-at date. Promoter holding is 52.1222% held by Cyient
  Limited, the sole promoter. No pledge disclosure has been located; pledge
  status stays an open item.
- **No research.** No effect on anchored evidence.
- **Partial screening.** Gate 0 works from Data_Sheet plus the ARs, four
  annual years only.

Stages 1 through 9 all run. Nothing is skipped. `concalls_available: true`,
so NO-CONCALL MODE does not apply.

## PDF EXTRACTION

pypdf verified working. All 19 input PDFs extracted to page-marked text under
`work/text/`, one `.txt` per PDF, each page delimited
`===== PAGE n of N | <relative path> =====`. No file failed. This is the
LESSONS reliable default: stages and verifiers read the page-marked text and
never hit the image-render wall. Every anchor stays a real page number in the
source PDF.

The investor presentation extracts thin at 646 characters per page against
about 2,900 for the transcripts. It is a graphics-heavy deck. Stage 4 must
treat it as partial and lean on the annual report.

```yaml
stage: B00-inputs
company: CYIENTDLM
run_date: 2026-09-06
model: orchestrator-inline
status: complete
spear_gate: OVERRIDE
spear_date: 2026-09-06
spear_load_bearing_facts: []
listed_date_derived: "FY2023-24 (IPO; AR FY2024-25 chairman letter)"
recently_listed: true
data_years: 4
input_gaps:
  - type: prospectus
    status: ABSENT
    priority: HIGH
    reason: "Listed FY2023-24, about 3.2 years before run_date. Carries promoter and group history, group-company map, restated pre-IPO financials. Nothing else holds them."
  - type: results
    status: ABSENT
    priority: MEDIUM
    reason: "No quarterly or annual results filings. Gate 0 falls back to screener Data_Sheet plus AR financial statements."
  - type: rating
    status: ABSENT
    priority: MEDIUM
    reason: "No rating rationale. Phase 3 Pillar 2 runs without it; FLAG-CASH INDETERMINATE risk."
  - type: announcements
    status: ABSENT
    priority: MEDIUM
    reason: "No Reg 30 record. Intent-and-action cross-check loses the documented-ACTION half."
  - type: shareholding
    status: ABSENT_BUT_PARTLY_SUBSTITUTED
    priority: LOW
    reason: "No quarterly shareholding pattern filing. The AR FY2025-26 corporate governance section substitutes at 31-Mar-2026: full ownership-category table (AR FY2025-26, p.100) and the over-1% shareholder list (AR FY2025-26, p.101). FII+DII IS derivable and anchored at FY26 year end; it is one quarter stale against a Q1FY27 filing. Promoter holding 52.1222% (Cyient Limited, sole promoter). No pledge disclosure located yet."
  - type: research
    status: ABSENT
    priority: LOW
    reason: "Never anchored evidence. Lead generation only."
  - type: screening
    status: PARTIAL
    priority: MEDIUM
    reason: "screener-Profit_Loss, -Balance_Sheet, -Cash_Flow, -Quarters are header-only for the company and all three peers (standing collect_to_repo v3 defect). screener-Data_Sheet.csv is populated: FY2023-FY2026 annuals plus ten quarters Q4FY24-Q1FY27."
  - type: annual-report
    status: OVER_CONTRACT
    priority: NONE
    reason: "Two ARs held (FY2024-25, FY2025-26) against a 0-1 contract. Both retained; FY2025-26 primary, FY2024-25 backward baseline. Year labels verified correct against document text."
  - type: concalls
    status: OVER_CONTRACT
    priority: NONE
    reason: "Four transcripts held against a 0-3 contract. Stage 5 takes the three most recent; Q2FY26 stays available to stage 7 and verifier B."
freshness_pairs:
  - pair: "newest results filing to same-quarter concall"
    trigger_doc: "NONE - inputs/results/ empty"
    mate_expected: "n/a"
    status: NO_TRIGGER
    missing_doc: ""
  - pair: "rating bulletin to full rationale"
    trigger_doc: "NONE - inputs/rating/ empty"
    mate_expected: "n/a"
    status: NO_TRIGGER
    missing_doc: ""
  - pair: "referenced SEBI order to order text"
    trigger_doc: "NONE - no SEBI order, penalty, adjudication or show-cause reference found in AR FY2025-26"
    mate_expected: "n/a"
    status: NO_TRIGGER
    missing_doc: ""
  - pair: "AR not older than latest audited annual results"
    trigger_doc: "Annual_Report_2026.pdf (FY2025-26, year ended 31 March 2026)"
    mate_expected: "no audited annual results filing newer than FY26"
    status: PASS
    missing_doc: ""
freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict: CORPUS GAPPED
concalls_available: true
no_concall_mode: false
concall_quarter_map:
  - {file: "inputs/concalls/Concall_Oct_2025_Transcript.pdf", date: "2025-10-14", quarter: "Q2FY26"}
  - {file: "inputs/concalls/Concall_Jan_2026_Transcript.pdf", date: "2026-01-20", quarter: "Q3FY26"}
  - {file: "inputs/concalls/Concall_Apr_2026_Transcript.pdf", date: "2026-04-21", quarter: "Q4FY26"}
  - {file: "inputs/concalls/Concall_Jul_2026_Transcript.pdf", date: "2026-07-21", quarter: "Q1FY27"}
peer_concalls_held: {AVALON: 4, KAYNES: 4, SYRMA: 4}
text_extraction: "all 19 input PDFs extracted to work/text/*.txt, page-marked, zero failures"
sector_cap_row: "Cables / Industrial products"
sector_cap_caveat: "No ESDM/EMS row exists in the Section 1B cap table. Aerospace-and-defence mix may argue the Defence / strategic row (38x). PHASE 3 confirmation item."
flags: []
analyst_note: "Operator override satisfied the spear gate with no load-bearing facts, so this run has no pre-set verification priority. Two structural constraints shape every stage. First, only four years of annual history exist (FY23-FY26) because the company listed in FY2023-24 and no prospectus was supplied, so every backward test runs short and Gate 0 must downgrade history. Second, the corpus holds no results filings, no rating rationale, no announcements and no shareholding filing, so the documented-ACTION record cannot be built from filings at all. The UA qualifier is the exception: the AR corporate governance section carries the ownership-category table at 31-Mar-2026, so FII+DII is anchored and derivable, one quarter stale. The freshness pairs pass only because their trigger documents are themselves missing; do not read FRESHNESS PAIRS OK as a complete corpus."
```
