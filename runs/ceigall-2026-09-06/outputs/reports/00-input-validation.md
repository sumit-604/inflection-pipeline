# STAGE 0 — INPUT VALIDATION

**Company:** Ceigall India Ltd (CEIGALL)
**Run folder:** runs/ceigall-2026-09-06
**Run date:** 2026-09-06
**Run type:** full
**CMP:** Rs 356.0 | **Market cap:** Rs 6,198 cr
**Sector cap row (manifest):** EPC / Civil construction

---

## 1. SPEAR GATE

No spear pass was run on this name. `companies/CEIGALL.md` did not exist at
run start. The orchestrator stopped the run and asked the operator. The
operator answered "Please start with the run. Do not stop." on 2026-09-06.

`companies/CEIGALL.md` now carries:

```
Spear: OVERRIDE 2026-09-06 (operator)
```

**Consequence for this run:** no load-bearing facts were named by a spear
pass. No stage carries a spear-derived first verification priority. The run
proceeds on its own corpus evidence alone. The POND / CATCH / PRICE work the
spear normally does before the pipeline has not been done, so nothing in this
run has sized the opportunity on live web or set a 25%-CAGR entry price
independently of the pipeline.

---

## 2. MANIFEST

`manifest.yaml` exists and parses. All required fields present.
`listed_date` is empty; the manifest notes text states the company listed in
August 2024. That is within ~3 years of the run date, so the RECENTLY-LISTED
PRIORITY rule applies and the absent IPO prospectus is a HIGH-priority gap.
Stage 8 must confirm the listing date from the corpus or web.

---

## 3. FOLDER INVENTORY

| Folder | Contract | Found | Status |
|---|---|---|---|
| prospectus/ | 0-2 PDF | 0 | **ABSENT — HIGH gap** (listed Aug 2024) |
| annual-report/ | 0-1 PDF | 1 (FY2025-26, 151pp) | PRESENT — **scanned, no text layer** |
| results/ | 0-3 PDF | 0 | ABSENT |
| rating/ | 0-1 PDF | 0 | ABSENT |
| concalls/ | 0-3 PDF | 4 | PRESENT (3 most recent used at stage 5) |
| peer-concalls/ | 0-12 PDF | 12 | PRESENT (HGINFRA, KNRCON, PNCINFRA x4) |
| announcements/ | 0-N PDF | 1 (Reg 30 AGM dispatch, 3pp) | PRESENT — broken font encoding |
| shareholding/ | 0-N | 0 | ABSENT |
| research/ | 0-N | 0 | ABSENT |
| screening/ | 0-N | 24 CSV | PRESENT — **4 of 6 company CSVs empty** |
| presentation/ | 0-N | 1 (Q1 FY27, 42pp) | PRESENT |
| other/ | 0-N | 0 | ABSENT (never consumed) |

Halt test: `manifest.yaml` parses and `inputs/` is not empty. **No halt.**

---

## 4. CORPUS DEFECTS FOUND AT VALIDATION

Three mechanical defects were found. None halts the run. Each changes how a
downstream stage must work.

### 4.1 The annual report is a scanned document (MATERIAL)

`Annual_Report_2026.pdf` carries 151 pages. 150 of them contain **zero
extractable text**. Only page 1 (the covering letter) has a text layer, and
that in a broken custom font encoding that decodes to garbage. Poppler's
`pdftotext` recovers digits and punctuation only; every letter is dropped.

OCR was attempted and **rejected**. Tesseract 5.3.4 at 300 dpi ran over
three minutes per page on these full-bleed design pages, and the output was
not fit for purpose: running prose came through, but **numeric tables came
through mangled or empty**. A financial schedule read off that OCR text
would have been a fabricated number. The attempt was abandoned and its
artifacts deleted.

**Mitigation applied instead: direct page rendering.** The Read tool renders
PDF pages natively and reads them accurately, tables included. Every
AR-consuming stage reads the PDF itself in page ranges, up to 20 pages per
call, guided by the page map in section 6 below.

Rule carried to every AR-consuming stage: **there is no AR text file. Read
the PDF pages.** Any number taken from the annual report is read off the
rendered page and cited by PDF sheet number. Where a figure cannot be read,
the fill is NOT FOUND.

### 4.2 Screener CSVs are mostly empty (known collector defect)

`screener-Profit_Loss.csv`, `screener-Balance_Sheet.csv`,
`screener-Cash_Flow.csv` and `screener-Quarters.csv` contain header rows
only. This is the recorded `collect_to_repo.py` v3 defect in LESSONS.md.

`screener-Data_Sheet.csv` **is** fully populated and carries the whole
series: FY2021 to FY2026 P&L, balance sheet and cash flow, plus ten quarters
from Q4 FY24 to Q1 FY27. Gate 0 runs from `screener-Data_Sheet.csv`. The
three peer CSV sets were not audited at stage 0; stage 6 and stage 1 read
what they need and record any further gap.

### 4.3 The announcement PDF does not extract

`Reg30_AGM_notice_dispatch_2026-09-05.pdf` uses the same broken font
encoding as the AR covering letter. Its text extract is garbage. It is a
3-page AGM notice dispatch letter of low evidential weight; stage 8 reads it
by page render if it needs it. The documented-ACTION record for this run is
therefore **one routine AGM dispatch and nothing else**: no Reg 30 order
wins, acquisitions, capital raises or divestments are in the corpus.

---

## 5. FRESHNESS PAIR CHECK

| # | Pair | Trigger present? | Mate | Status |
|---|---|---|---|---|
| 1 | Newest results filing to same-quarter concall | NO — `results/` is empty | n/a | PASS (not triggered) |
| 2 | Rating bulletin to full rationale | NO — `rating/` is empty | n/a | PASS (not triggered) |
| 3 | Referenced SEBI order to order text | NO — no SEBI order referenced in the searchable corpus | n/a | PASS (not triggered) |
| 4 | AR not older than latest audited annual results | YES — audited FY2026 annuals exist (screener Data_Sheet, year ended 2026-03-31) | AR FY2025-26 | **PASS** |

**freshness_verdict: FRESHNESS PAIRS OK**

Two notes on the verdict:

- Pairs 1 to 3 pass because their trigger document is absent, not because
  the corpus is complete. An empty `results/` folder cannot fail a
  results-to-concall pair. The absence is captured in `input_gaps`, not here.
- Pair 3 was tested against the concalls, the presentation and the
  announcement. The annual report has no text layer and cannot be grepped,
  so it was not searched. Stage 3 reads the Directors' Report and the
  contingent-liability and litigation notes; if it finds a SEBI order
  referenced there, this pair reopens and the verdict moves to CORPUS
  GAPPED-FRESHNESS.

The corpus audit verdict is **CORPUS GAPPED**, not CORPUS GAPPED-FRESHNESS.
The gate is not capped by the freshness rule. It is still short five
document types.

---

## 6. ANNUAL REPORT PAGE MAP (PDF sheet numbers)

The report prints two-up: one PDF sheet carries two printed pages. The
printed page numbers run 02 to 297 across 151 sheets. Conversion, verified
against the contents page and three sampled sheets:

> **PDF sheet = (printed page / 2) + 2**

Stages address pages by **PDF sheet number**, which is what the Read tool
takes. The map below is built from the report's own "WHAT'S INSIDE" contents
page (sheet 3) and is the navigation aid for every AR-consuming stage.

| Section | Printed pages | **PDF sheets** |
|---|---|---|
| Cover, covering letter | — | 1-2 |
| **Corporate Overview** | 02-47 | **3-25** |
| — About the Company | 04 | 4 |
| — Key Highlights (business, financial, order book) | 06 | 5 |
| — Pan India Growth | 08 | 6 |
| — Our Landmark Project | 10 | 7 |
| — Building Our Legacy | 12 | 8 |
| — Chairman cum MD's Message | 14 | 9 |
| — Financial Highlights | 16 | 10 |
| — Opportunities in the Infrastructure Space | 18 | 11 |
| — Our Strengths and Strategies | 26 | 15 |
| — Our Business Model | 28 | 16 |
| — Product Portfolio, Key Ongoing Projects | 30 | 17 |
| — Operational Excellence | 42 | 23 |
| — Corporate Governance / Board / Management Team | 43-46 | 23-25 |
| **Management Discussion and Analysis** | 48-63 | **26-33** |
| **Directors' Report** | 64-91 | **34-47** |
| **Corporate Governance Report** | 92-109 | **48-56** |
| **BRSR** | 110-143 | **57-73** |
| **Standalone Financial Statements** | 144-201 | **74-102** |
| **Consolidated Financial Statements** | 202-261 | **103-132** |
| **Notice of AGM** | 262-297 | **133-151** |

Reading guide by stage:

- **Stage 2 (notes triple-pass):** consolidated notes, sheets 103-132; the
  standalone set at sheets 74-102 where a standalone-only disclosure matters.
- **Stage 3 (AR deep dive):** Directors' Report sheets 34-47, MD&A sheets
  26-33, Corporate Governance Report sheets 48-56, plus the notes above for
  related-party and contingent-liability work.
- **Stage 4 (business model):** sheets 4-17 (about, key highlights, business
  model, project portfolio) plus MD&A sheets 26-33.
- **Stage 8 (promoter/governance):** Corporate Governance Report sheets
  48-56, Board of Directors sheets 24-25, Directors' Report related-party
  and remuneration annexures within sheets 34-47.

---

## 7. CONCALL QUARTER MAP (confirmed from transcript first pages)

| Order | File | Quarter | Call date |
|---|---|---|---|
| 1 (oldest) | Concall_Nov_2025_Transcript.pdf | Q2 & H1 FY26 | 17-11-2025 |
| 2 | Concall_Feb_2026_Transcript.pdf | Q3 & 9M FY26 | 13-02-2026 |
| 3 | Concall_May_2026_Transcript.pdf | Q4 & FY26 | 12-05-2026 |
| 4 (newest) | Concall_Aug_2026_Transcript.pdf | Q1 FY27 | 14-08-2026 |

Four transcripts are held; the contract passes three to stage 5. The three
most recent are used, oldest first: **Q3 FY26, Q4 FY26, Q1 FY27**. The
Nov 2025 (Q2 FY26) transcript stays in the corpus and is available to
stage 7 and to verifier B.

---

## 8. PEER CORPUS

Twelve peer transcripts, four each for three road-EPC peers with HAM
portfolios: **HGINFRA, KNRCON, PNCINFRA**. All twelve extract cleanly to
text. Peer set matches the manifest and matches the archetype.

---

## 9. TEXT PREPARATION APPLIED

Every text-layer PDF was pre-extracted to a page-marked `.txt` beside the
PDF (`===== [PAGE N] =====`), per the LESSONS.md standing fix, so no stage
hits the image-render wall. 18 files extracted: 4 company concalls, 12 peer
concalls, the investor presentation, and the announcement (garbled, unusable).

The annual report is the one exception. It has **no `.txt`**. It is read by
page render, per 4.1 and the page map in section 6.

Stages cite the PDF filename and page number. The `.txt` files are reading
aids, not new sources.

---

## 10. DEGRADATION CARRIED FORWARD

| Absent | Effect per DEGRADATION MAP |
|---|---|
| prospectus (HIGH) | Stages 2 and 3 build the backward history from the AR alone. FTTCP backward baseline runs on post-listing years only. Stage 8 sources promoter and group background from web search plus the AR governance section, and flags the group-company map as web-derived, not filing-anchored. |
| results | Gate 0 runs from screener data alone. Stage 10 (phase 3) marks latest-period fields unresolved. |
| rating | Stage 10 marks `rating_wc_quote` unresolved. Stage 11 Pillar 2 proceeds without rating evidence and defaults conservative. Bears directly on the cash-conversion determination: the rating rationale is the usual evidence that separates STRUCTURAL from GROWTH-INDUCED. |
| shareholding | Stage 10 marks FII+DII unresolved. Stage 11 cannot affirm the UA institutional-absence qualifier, so UA is withheld under the all-three-qualifier rule. Promoter holding and pledge trend fall back to the AR figure with staleness noted. |
| research | No effect on anchored evidence. |
| announcements (effectively) | The one filing held is a routine AGM dispatch. Stages 5, 7 and 8 lose the documented-ACTION record. Stage 8 relies on web search for material events. |

---

## 11. OPERATOR PAUSE

The contract requires one pause here to confirm the empty folders. The
operator pre-answered it on 2026-09-06 with "Please start with the run. Do
not stop." Per the LESSONS.md standing fallback, the run proceeds on
documented evidence-maximizing defaults and the gaps are recorded here and
carried to Halt 1. The question is not asked again for the rest of this run.

The five absent document types are listed for the operator at Halt 1:
**prospectus (HIGH), results, rating, shareholding, research.**

---

```yaml
stage: B00-inputs
company: CEIGALL
run_date: 2026-09-06
model: orchestrator
status: complete
input_gaps:
  - type: prospectus
    priority: HIGH
    reason: "Company listed August 2024, within ~3 years of run_date. RECENTLY-LISTED PRIORITY applies. Promoter/group history, group-company map and restated pre-IPO financials are unavailable."
  - type: results
    priority: MEDIUM
    reason: "inputs/results/ empty. Gate 0 runs from screener Data_Sheet alone. No quarterly/annual filing PDF to anchor latest-period figures."
  - type: rating
    priority: HIGH
    reason: "inputs/rating/ empty. No rating rationale. This is the usual evidence separating STRUCTURAL from GROWTH-INDUCED cash conversion. Bears on FLAG-CASH."
  - type: shareholding
    priority: MEDIUM
    reason: "inputs/shareholding/ empty. FII+DII unresolved; UA institutional-absence qualifier cannot be affirmed; promoter pledge trend falls back to AR."
  - type: research
    priority: LOW
    reason: "inputs/research/ empty. Never anchored evidence. Lead-generation and management-intent cross-check lost only."
  - type: announcements-substantive
    priority: MEDIUM
    reason: "Only filing held is a routine Reg 30 AGM dispatch letter (3pp, 2026-09-05). No order wins, acquisitions, capital raises or divestments in the corpus. Documented-ACTION record unavailable to stages 5, 7, 8."
corpus_defects:
  - defect: "annual-report-no-text-layer"
    detail: "Annual_Report_2026.pdf is scanned. 150 of 151 pages have zero extractable text. Tesseract OCR was attempted and rejected: >3 min/page and numeric tables came through mangled or empty. Mitigation is direct page rendering (Read the PDF with a page range, max 20 sheets per call), guided by the section-6 page map. There is NO AR text file. Every AR figure is read off the rendered page and cited by PDF sheet; NOT FOUND is the only other fill."
  - defect: "screener-csvs-empty"
    detail: "screener-Profit_Loss.csv, -Balance_Sheet.csv, -Cash_Flow.csv, -Quarters.csv are header-only. Known collect_to_repo v3 defect. screener-Data_Sheet.csv IS populated: FY2021-FY2026 P&L/BS/CF plus 10 quarters Q4FY24-Q1FY27. Gate 0 uses Data_Sheet."
  - defect: "announcement-broken-font"
    detail: "Reg30_AGM_notice_dispatch_2026-09-05.pdf text layer decodes to garbage (same broken encoding as AR cover letter). OCR'd."
  - defect: "sector-cap-row-hand-set"
    detail: "manifest sector_cap_row set by hand to 'EPC / Civil construction' after the auto-picker chose 'Cables / Industrial products'. Confirm at phase 3."
spear_gate:
  status: OVERRIDE
  date: 2026-09-06
  load_bearing_facts: []
  note: "Operator override. No spear pass run. No spear-derived verification priority exists for this run."
freshness_pairs:
  - pair: "results-to-concall"
    trigger_doc: "NONE (inputs/results/ empty)"
    mate_expected: "n/a"
    status: PASS
    missing_doc: null
  - pair: "rating-bulletin-to-rationale"
    trigger_doc: "NONE (inputs/rating/ empty)"
    mate_expected: "n/a"
    status: PASS
    missing_doc: null
  - pair: "sebi-order-to-order-text"
    trigger_doc: "NONE (no SEBI order referenced in searchable corpus)"
    mate_expected: "n/a"
    status: PASS
    missing_doc: null
  - pair: "ar-to-latest-audited-annual-results"
    trigger_doc: "Audited FY2026 annual results (year ended 2026-03-31, screener Data_Sheet)"
    mate_expected: "Annual report for FY2025-26"
    status: PASS
    missing_doc: null
freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict: CORPUS GAPPED
manifest:
  company: "Ceigall India Ltd"
  ticker: CEIGALL
  cmp: 356.0
  market_cap_cr: 6198.0
  run_type: full
  concalls_available: true
  sector_cap_row: "EPC / Civil construction"
  listed_date_declared: ""
  listed_date_inferred: "2024-08 (manifest notes; confirm at stage 8)"
inventory:
  prospectus: 0
  annual_report: 1
  results: 0
  rating: 0
  concalls: 4
  peer_concalls: 12
  announcements: 1
  shareholding: 0
  research: 0
  screening: 24
  presentation: 1
  other: 0
concall_quarter_map:
  - {order: 1, file: "Concall_Nov_2025_Transcript.pdf", quarter: "Q2 & H1 FY26", date: "2025-11-17", used_by_stage5: false}
  - {order: 2, file: "Concall_Feb_2026_Transcript.pdf", quarter: "Q3 & 9M FY26", date: "2026-02-13", used_by_stage5: true}
  - {order: 3, file: "Concall_May_2026_Transcript.pdf", quarter: "Q4 & FY26", date: "2026-05-12", used_by_stage5: true}
  - {order: 4, file: "Concall_Aug_2026_Transcript.pdf", quarter: "Q1 FY27", date: "2026-08-14", used_by_stage5: true}
peer_set: [HGINFRA, KNRCON, PNCINFRA]
peer_transcripts_count: 12
no_concall_mode: false
company_memory_present: true
company_memory_note: "companies/CEIGALL.md created this run to carry the operator spear override. It holds no prior thesis, no prior decision status, no prior operator rulings and no prior run links. There is no COMPANY MEMORY to weigh."
prior_run_context: none
flags: []
analyst_note: "Two gaps dominate this corpus and both bear on the same question. The annual report has no text layer, so its financial schedules must be read off the page image rather than searched; and there is no rating rationale, no results filing and no shareholding pattern. The screener Data_Sheet shows operating cash flow negative in five of six years while reported profit rises, so the cash-conversion determination is likely to be the run's load-bearing question, and the single document that usually settles it (the rating rationale) is the one that is missing."
```
