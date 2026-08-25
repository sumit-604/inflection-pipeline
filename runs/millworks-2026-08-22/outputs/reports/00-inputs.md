# B00 — Input Validation (Stage 0)

Company: Millworks Technologies Limited (MILLWORKS)
Run date: 2026-08-22 | run_type: full | concalls_available: false

## Manifest
- cmp 828.0, market_cap_cr 1458.0
- sector_cap_row: "Pharma / CDMO" — **WRONG, DO NOT USE**. Auto-picked by
  collector, flagged "verify" in manifest notes. Evidence below.
- listed_date: not set in manifest. RHP dated 2026-07-07. Company listed on
  BSE SME ~July 2026, so RECENTLY-LISTED (well within ~3 years). Prospectus
  is the foundational document.

## Inventory (by folder)
| Folder | Count | Contents |
|---|---|---|
| prospectus | 0 | empty — but see routing note 1 |
| annual-report | 1 | RHP_Millworks-07.07.2026 (1).pdf — this is the RHP, not a true AR |
| results | 0 | empty |
| rating | 0 | empty |
| concalls | 0 | declared absent (concalls_available: false); NOT a gap |
| peer-concalls | 7 | Airfloa Rail (544516) Nov-2025, Jun-2026; Apsis Aero Jun-2026; Unimech Aerospace Feb/May/Jun/Aug-2026 |
| announcements | 0 | empty — but see routing note 2 |
| shareholding | 0 | empty |
| research | 0 | empty |
| screening | 30 | Millworks = screener-*.csv (6 files); peers 523606, 544516 (Airfloa), APSISAERO, UNIMECH (6 each) |
| presentation | 1 | 786241e4-...pdf — this is a SEBI Reg 30 order-book intimation, not an investor deck. See routing note 2 |
| other | 0 | empty |

## Routing decisions (misfiled inputs corrected at source, files not moved)
1. **RHP routed as prospectus.** The RHP sits under annual-report/. It is
   the foundational filing for a recently-listed company: promoter/group
   history, group-company map, restated pre-IPO financials, risk factors,
   MD&A-equivalent business section. It serves TWO roles this run:
   (a) the prospectus (stages 3, 8 promoter/group, backward baseline), and
   (b) the annual-report substitute for stages 2, 3, 4 (restated financial
   statements with schedules stand in for AR notes). There is no separate
   standalone annual report.
2. **Reg 30 order letter routed as the documented-ACTION record.** The file
   in presentation/ is a Reg 30 intimation dated 2026-08-20: multiple
   purchase orders 2026-07-21 to 2026-08-19 totalling ~₹53.74 cr; stated
   confirmed order book ₹121.88 cr for FY27; scrip 544826; CIN matches RHP.
   It is Millworks' own filing (anchored evidence, not research). It routes
   to stages 5 (guidance/action), 7 (F2 capex/promise-delivery proxy), and
   8 (material events). It is NOT an investor presentation, so stage 4 has
   no true deck and runs from the RHP business section.

## Sector correction (analytical routing input, operator ruling needed pre-Phase 3)
Manifest sector "Pharma / CDMO" contradicts all evidence:
- Presentation/Reg 30 letter: machined OEM assembly components (bracket,
  casting, housing, manifold, fastener, valve, gauge, sheet metal).
- Peer set is aerospace/defence/rail precision engineering: Unimech
  Aerospace, Apsis Aero, Airfloa Rail Technology.
- RHP page 1: Millworks Technologies Ltd, CIN U29200KA2021PLC153863,
  Bengaluru.
Correct archetype: **Build-to-Print / Build-to-Spec precision component
maker** (aerospace, defence, rail, semiconductors, drones, instrumentation).
The Section 1B sector_cap "Pharma / CDMO" MUST NOT govern the exit multiple.
Operator must set the correct sector_cap_row before Phase 3 valuation. This
is a routing flag, not a company-quality flag; it does not halt.

## NO-CONCALL MODE (main company)
concalls_available: false. Stage 5 runs degraded: reads the RHP business /
MD&A-equivalent section and the Reg 30 order letter; credibility_grade
defaults to C, may rise to B only on documented guidance-vs-delivery, never
A. Stage 6 runs normally (7 peer transcripts present). Stage 7 F2 uses RHP
capex-timeline evidence in place of a promise-delivery record.

## input_gaps (carried on every downstream block)
- no_results_pdf: Gate 0 (stage 1) runs from screening CSVs; stage 10 marks
  latest-period fields unresolved.
- no_rating: stage 10 rating_wc_quote unresolved; Pillar 2 conservative default.
- no_standalone_annual_report: stages 2/3/4 build from RHP restated financials
  (fewer independent AR years; RHP restated statements cover the pre-IPO years).
- no_shareholding_pattern: UA institutional qualifier withheld; promoter
  holding/pledge from RHP capital-structure section, staleness noted.
- no_dedicated_prospectus_folder: RHP present under annual-report/, routed as
  prospectus (gap is cosmetic, document exists).
- no_investor_presentation: presentation/ holds a Reg 30 letter, not a deck;
  stage 4 runs from RHP.
- no_research_notes: no effect on anchored evidence.
- announcements_folder_empty: the single Reg 30 order letter (in presentation/)
  is the only documented-ACTION record; no other Reg 30 events available.
- sector_mismatch: manifest sector_cap_row wrong (see above).
- concalls: declared absent, NOT counted as a gap.

## Company memory
No companies/MILLWORKS.md — first run for this ticker. No PRIOR RUN CONTEXT.

```yaml
stage: B00-inputs
company: MILLWORKS
run_date: 2026-08-22
model: orchestrator
status: complete
run_type: full
concalls_available: false
recently_listed: true
listed_evidence: "RHP dated 2026-07-07; BSE SME listing ~July 2026"
inventory:
  prospectus: 0
  annual_report: 1
  results: 0
  rating: 0
  concalls: 0
  peer_concalls: 7
  announcements: 0
  shareholding: 0
  research: 0
  screening: 30
  presentation: 1
  other: 0
routing:
  rhp_path: "inputs/annual-report/RHP_Millworks-07.07.2026 (1).pdf"
  rhp_roles: [prospectus, annual_report_substitute]
  reg30_order_letter_path: "inputs/presentation/786241e4-c123-4c8a-a102-7c8c944e9c49.pdf"
  reg30_roles: [documented_action_record, stage5, stage7_f2, stage8]
  main_company_screening_prefix: "screener-"
  peers:
    - {name: "Unimech Aerospace", ticker: UNIMECH, concalls: 4, screening: true}
    - {name: "Apsis Aero", ticker: APSISAERO, concalls: 1, screening: true}
    - {name: "Airfloa Rail Technology", code: "544516", concalls: 2, screening: true}
    - {name: "peer 523606 (screening only)", code: "523606", concalls: 0, screening: true}
input_gaps:
  - no_results_pdf
  - no_rating
  - no_standalone_annual_report
  - no_shareholding_pattern
  - no_dedicated_prospectus_folder_rhp_routed
  - no_investor_presentation_reg30_only
  - no_research_notes
  - announcements_folder_empty_reg30_is_sole_action_record
  - sector_mismatch_manifest_pharma_cdmo_actual_aero_defence_precision
flags:
  - type: SECTOR-MISMATCH
    detail: "manifest sector_cap_row 'Pharma / CDMO' is wrong; actual archetype Build-to-Print/Build-to-Spec precision component maker (aero/defence/rail/semi). Operator must set correct sector_cap_row before Phase 3."
    halts: false
no_concall_mode: true
analyst_note: "First run. RHP carries both prospectus and AR roles. Sole documented-action record is one Reg 30 order letter (order book Rs 121.88cr FY27). Sector tag wrong; peers are aerospace/defence/rail. Gate 0 runs from screening CSVs (no results PDF)."
```
