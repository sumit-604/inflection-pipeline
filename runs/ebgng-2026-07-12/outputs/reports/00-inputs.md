# Stage 0 — Input Validation (B00)

**Company:** GNG Electronics Ltd (EBGNG)
**Run date:** 2026-07-12
**Run type:** full
**CMP:** ₹634.0 | **Market cap:** ₹7,227 cr
**manifest.yaml:** present and parseable.

## Inventory (by subfolder)

| Subfolder | Count | Used | Notes |
|---|---|---|---|
| annual-report/ | 1 | 1 | `1743048928831.pdf` — **Draft Red Herring Prospectus dated 2025-03-25**, 419 pp. Not a post-listing annual report. |
| results/ | 2 | 2 | Feb-05-2026 board = Q3 FY26 (Dec-31-2025) unaudited; May-05-2026 board = Q4/FY26 (Mar-31-2026) audited annual. |
| rating/ | 1 | 1 | CARE press release, Apr-08-2026. Upgraded to CARE BBB; Stable / A3+. |
| concalls/ | 4 | 3 | 3 most recent used: Nov-2025 (Q2 FY26), Feb-2026 (Q3 FY26), May-2026 (Q4 FY26). Aug-2025 (Q1 FY26, first post-IPO call) available but unused per 3-most-recent rule. |
| peer-concalls/ | 12 | 12 | CNL x4, REDINGTON x4, RPTECH x4. |
| screening/ | 30 CSV | main + peers | `screener-*` (main company) plus CNL, DLINKINDIA, REDINGTON, RPTECH data sheets. |
| presentation/ | 0 | — | **EMPTY.** |
| other/ | 0 | — | Empty (never consumed). |

## Concall chronology (confirmed from transcript cover dates)

| File | Board/call date | Quarter |
|---|---|---|
| Concall_Aug_2025 | Aug-25-2025 | Q1 FY26 (Jun-30-2025) — unused |
| Concall_Nov_2025 | Nov-10-2025 | Q2 FY26 (Sep-30-2025) |
| Concall_Feb_2026 | Feb-11-2026 | Q3 FY26 (Dec-31-2025) |
| Concall_May_2026 | May-11-2026 | Q4/FY26 (Mar-31-2026) |

## Company facts (orchestrator-level, for marker filling only — every downstream number is re-anchored by the stage against source PDFs)

- **Business:** One of India's largest refurbishers of ICT (Information and Communication Technology) devices — laptops, desktops, IT hardware. Brand "Electronics Bazaar (EB) certified"; R2v3 certified. Markets: India, US, Middle East, Europe via subsidiaries. (rating p1-2)
- **Promoters:** Sharad Khandelwal, Vidhi Sharad Khandelwal, Kay Kay Overseas Corporation (KKOC), Amiable Electronics Private Limited. (DRHP cover p1)
- **Financials (consolidated, rating p4):** Revenue FY24 ₹1,140.80 cr, FY25 ₹1,414.21 cr, 9MFY26 ₹1,239.40 cr. PAT FY24 ₹52.31 cr, FY25 ₹69.03 cr, 9MFY26 ₹89.90 cr. Overall gearing ~2.0x. IPO July 2025 (fresh proceeds ~₹400 cr gross).

## Input gaps and characterizations

1. **presentation_absent** — `inputs/presentation/` empty. Stage 4 (business model) degrades to the DRHP + results commentary per the AR-priority rule. The single stage-0 operator pause could not be delivered: the AskUserQuestion stream closed in this remote session (same failure recorded in LESSONS.md 2026-07-11 on KARNIKA). Proceeded on the evidence-maximizing default. Carried on every downstream block.
2. **annual_report_is_drhp** — the `annual-report/` document is an IPO Draft Red Herring Prospectus (2025-03-25), not a post-listing annual report. Its restated financial statements run through FY24 (FY22-24); FY25 audited and FY26 numbers live in the `results/` PDFs and the CARE rating. Stages 2, 3, 4, 7 read the DRHP as the primary long-form document; it is rich (business, risk factors, RPTs, promoter detail, restated accounts) but pre-IPO in framing. Stage 1 and stage 10 take latest-period financials from the results PDFs.
3. **sector_cap_mismatch** — `manifest.sector_cap_row: "Pharma / CDMO"` contradicts the business (ICT device refurbishment / IT hardware distribution / electronics retail). This is a collect_to_repo v3 auto-pick defect, identical in kind to the KARNIKA mis-tag (LESSONS 2026-07-11). Flagged for PHASE 3 stage-11 sector-cap selection; the correct Section 1B cap row is an IT hardware / electronics / distribution row, not Pharma. Does not affect phase-1 evidence gathering.
4. **concalls_4_available_3_used** — 4 transcripts exist; the 3 most recent (Q2/Q3/Q4 FY26) feed stage 5. Aug-2025 (Q1 FY26) is preserved but unused.

## Halt check

manifest present and parseable; `inputs/` tree non-empty. **No halt condition.** Run proceeds.

```yaml
stage: B00-inputs
company: EBGNG
run_date: 2026-07-12
model: orchestrator
status: complete
concalls_available: true
no_concall_mode: false
run_type: full
prior_run_found: false
inventory:
  annual_report: 1        # DRHP 2025-03-25, not a post-listing AR
  results: 2              # Q3 FY26 unaudited, Q4/FY26 audited
  rating: 1               # CARE BBB;Stable / A3+, 2026-04-08
  concalls_present: 4
  concalls_used: 3        # Nov2025 Q2FY26, Feb2026 Q3FY26, May2026 Q4FY26
  peer_concalls: 12       # CNL x4, REDINGTON x4, RPTECH x4
  screening_csv: 30
  presentation: 0
  other: 0
concall_quarter_map:
  Concall_Nov_2025: Q2 FY26
  Concall_Feb_2026: Q3 FY26
  Concall_May_2026: Q4 FY26
input_gaps:
  - presentation_absent: "inputs/presentation/ empty; stage 4 degrades to DRHP + results commentary; operator pause undeliverable (AskUserQuestion stream closed, remote session); proceeded on default"
  - annual_report_is_drhp: "annual-report/ is an IPO DRHP dated 2025-03-25 (restated accounts through FY24), not a post-listing annual report; FY25/FY26 numbers from results PDFs and rating"
  - sector_cap_mismatch: "manifest sector_cap_row 'Pharma / CDMO' wrong for an ICT-refurbishment / IT-hardware business; collect_to_repo auto-pick defect; flag for phase-3 stage-11 sector cap"
  - concalls_4_available_3_used: "Aug-2025 (Q1 FY26, first post-IPO call) preserved but unused per 3-most-recent rule"
flags: []
```
