# B00 — Input Validation (Stage 0)

**Company:** Asian Energy Services Limited (ASIANENE)
**Run date:** 2026-07-13 | **Run type:** full | **CMP:** ₹340.0 | **Market cap:** ₹1,654 Cr

## Inventory (by subfolder)

| Folder | Count | Used | Notes |
|--------|-------|------|-------|
| annual-report | 1 | Annual_Report.pdf (229pp) | Clean text extraction verified |
| results | 2 | both | Investor releases/results PDFs |
| rating | 1 | ratings.pdf | Most recent |
| concalls | 4 | 3 most recent | May2025, **Sep2025, Nov2025, May2026** — May2025 dropped (oldest of 4) |
| peer-concalls | 8 | 8 | DEEPINDS ×4, JINDRILL ×4 |
| screening | 24 csv | main + peers | screener-*, DEEPINDS-*, JINDRILL-*, DOLPHIN-* |
| presentation | 1 | Investor_Presentation_1.pdf | |
| other | absent | — | Never consumed |

## Concall chronology (3 most recent, oldest first)
1. Concall_Sep_2025_Transcript.pdf — held 12 Sep 2025, quarter to confirm from content (likely Q1 FY26)
2. Concall_Nov_2025_Transcript.pdf — Q2/H1 FY26 (quarter & half year ended 30 Sep 2025)
3. Concall_May_2026_Transcript.pdf — Q4 FY26 (quarter & year ended 31 Mar 2026)

Stage 5 confirms the quarter map from each transcript's internal dates.

## Peer coverage
- Concalls provided for: **DEEPINDS** (Deep Industries), **JINDRILL** (Jindal Drilling)
- Screening-only peer (no concall): **DOLPHIN** (Dolphin Offshore)

## Financial anchors (screener Data_Sheet, consolidated, to be re-verified by stages)
- FY26 Sales ₹791.05 Cr; Net profit ₹51.16 Cr. FY25 Sales ₹465.04 Cr; NP ₹42.12 Cr.
- Q4 FY26 (Mar-26) Sales ₹338.23 Cr; NP ₹31.96 Cr (strong seasonal quarter).

## Flags for downstream / operator
- **SECTOR_CAP_ROW MISMATCH:** manifest sets `sector_cap_row: "Agri processing"`, auto-picked by collector. Company is an oilfield/energy services business (seismic data acquisition, drilling, well/gas services). Peers are oilfield-services names. The "Agri processing" cap row is almost certainly wrong and must be corrected before Section 1B v3.3 exit-PE selection in PHASE 3. Surfaced now, decision deferred to operator/phase 3.
- No prior run folder for ASIANENE; no companies/ASIANENE.md. Normal full run.

```yaml
stage: B00-inputs
company: ASIANENE
run_date: 2026-07-13
model: orchestrator
status: complete
run_type: full
cmp: 340.0
market_cap_cr: 1654.0
concalls_available: true
no_concall_mode: false
prior_run: none
company_memory: none
inventory:
  annual_report: 1
  results: 2
  rating: 1
  concalls_present: 4
  concalls_used: 3
  peer_concalls: 8
  screening_files: 24
  presentation: 1
  other: 0
concall_map:
  - {file: Concall_Sep_2025_Transcript.pdf, quarter: "Q1 FY26 (to confirm)", order: 1}
  - {file: Concall_Nov_2025_Transcript.pdf, quarter: "Q2/H1 FY26", order: 2}
  - {file: Concall_May_2026_Transcript.pdf, quarter: "Q4 FY26", order: 3}
concalls_dropped: [Concall_May_2025_Transcript.pdf]
peers_with_concalls: [DEEPINDS, JINDRILL]
peers_screening_only: [DOLPHIN]
revenue_anchor_fy26_cr: 791.05
input_gaps: []
flags:
  - type: SECTOR_CAP_ROW_MISMATCH
    detail: "manifest sector_cap_row 'Agri processing' inconsistent with oilfield/energy-services business; correct before Section 1B exit-PE in phase 3"
    severity: MAJOR
    decision: deferred_to_phase3
```
