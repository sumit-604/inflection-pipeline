# Phase-1 verifier summary — RATHIST 2026-07-20

## Phase-1 confidence delta

| Component | Score | Acceptance | Source |
|---|---|---|---|
| Numerical acceptance | 88.2 | 30 of 34 figures clean | B12a (Verifier A) |
| Red flag coverage | 85 | 11 of 13 flags caught | B12b (Verifier B) |
| Framework adherence (Gate 0 + Emerging Moat only) | 97 | 44 of 46 gate0 rules, 29 of 30 emoat | B12c (Verifier C, phase-1 portion) |
| Peer utilisation | 100 | 2 of 2 peers used substantively | B12d (Verifier D) |
| Overall (min of four) | 85 | band normal (75-89) | confidence |

Valuation framework adherence (Verifier C valuation portion) is PENDING phase 3. No confidence-driven downgrade or REWORK from the delta itself.

## Source-fidelity gate dispositions (nothing silent)

Verifier A is the sole, non-overridable authority on whether a number exists in the source. It raised 2 CRITICAL and 1 MAJOR source_fidelity findings, all on Gate 0 inputs. None is a fabrication or a material misread; each is a correctable source-data conflict with no change to the Gate 0 score band. The gate is therefore HELD, not forced to REWORK. Dispositions:

- FY25 equity 128.13 Cr (screener) vs 137.02 Cr (two audited sources): GATE HELD — corrected at source to 137.02 Cr (AR FY25 Balance Sheet p.79 / Q4 FY26 audited results FY25 comparative p.8). ROE moves from 9.25% to about 8.96%, stays below 12, A3 scores 0 either way, band unchanged.
- FY25 borrowings 37.74 Cr (AR) vs 0.00 Cr (Q4 comparative): GATE HELD — unresolved conflict between two audited filings, same auditor M. Lal & Co., no reconciling note; flagged for company or auditor clarification. Current Liabilities 121.23 Cr matches both sources; no Gate 0 band change; this is a source integrity conflict, not a pipeline misread, so not REWORK.
- FY26 other income 0.44 Cr (screener) vs 0.12 Cr (Q4 audited): GATE HELD — corrected at source to 0.12 Cr. EBITDA moves from 28.46 Cr to 28.78 Cr, coverage ratios marginally affected, band unchanged.

The formal outputs/final/verifier-disagreement-log.md is finalized in phase 3; its phase-1 rows are recorded at the end of this file.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note | Disposition |
|---|---|---|---|
| A (B12a) | Gate0 Block A ROE FY25 input | FY25 equity taken as 128.13 Cr (screener); two audited sources agree 137.02 Cr (-6.6%), feeds ROE (AR p.79 / Q4 FY26 results FY25 comparative p.8) | GATE HELD — corrected at source; band unchanged |
| A (B12a) | Gate0 Block D borrowings FY25 | Two audited filings irreconcilable: AR 37.74 Cr vs Q4 comparative 0.00 Cr, same date and auditor, no note | GATE HELD — flagged for clarification; band unchanged; not REWORK |

### MAJOR

| Verifier | Location | Note | Disposition |
|---|---|---|---|
| A (B12a) | Gate0 Block D EBITDA / coverage | FY26 other income 0.44 Cr (screener) vs 0.12 Cr (Q4 audited); affects Net Debt/EBITDA and interest coverage marginally | GATE HELD — corrected at source to 0.12 Cr |
| B (B12b) | B05 concall, omission | Q2 FY26 production number disclosure regression not captured; output dropped from disclosure pack, management declined figures on call (Concall_Nov_2025 p.19) | ADDED to contradicted claims and monitorables |
| D (B12d) | B06 Part 2C / capex_cycle | VRAJ capex overstated as IPO funded; the Rs 49 Cr solar was Rs 38 Cr HDFC term debt + Rs 11 Cr internal accruals; IPO Rs 171 Cr repaid Rs 70 Cr debt + funded Rs 59.5 Cr of first project (CARE Feb'26 p.2, p.4); source_fidelity true | CORRECTED — capital access cross-peer point softened before narrative |

### MINOR

| Verifier | Location | Note | Disposition |
|---|---|---|---|
| A (B12a) | Gate0 numerical set | 1 minor line item within tolerance; 30 of 34 figures clean, verdict-card core numbers traced to audit level or flagged | No action |
| B (B12b) | B05 4D#6 / headline claims | Green power >25% short of a ~30% headline is an overstated comparator; no 30% green power claim exists, the ~30% is TMT revenue share (Concall_Nov_2025 p.6) | REMOVED from narrative; rooftop solar downscaling portion retained |
| B (B12b) | B05 concall, omission | FY26 PAT +39.24% quoted ex FY25 exceptional items; comparability caveat not flagged (Concall_Jun_2026 p.3) | Comparability note only; openly disclosed by management |
| C (B12c) | B01 Block F M5 | Scored 1 while marked PEER DATA NEEDED; Block F rule requires 0; moat 5->4, grand 29->28 | APPLIED — classification unchanged AVOID |
| C (B12c) | B07 Section 2C | capex_embedded_growth_pct=0 on NIL committed basis excludes Rs 6.27 Cr CWIP (~7.5% alternative reading) | Immaterial to EM 9.9/NONE; carry to Pillar 3 phase 3 |
| D (B12d) | B06 Part 2, Scan Steels | Energy cost 12-15% of TMT structure and working capital ratios not mined (p.22, p.15/16) | Industry context miss only; not responsive to any peer question |
| D (B12d) | B06 pricing_inputs | PBILDT (FY24/FY25) and PBDIT (H1/9M FY26) presented as one continuous margin series; basis switch is CARE's own | Direction unaffected; precision slightly overstated |

## Verifier C — Gate 0 and Emerging Moat scope note

Verifier C ran phase-1 scope only: Gate 0 and Emerging Moat adherence, 76 rules checked, acceptance 97. Valuation adherence is deferred to phase 3 (B10/B11 not yet produced). recomputed_destination_pe and recomputed_decision are empty by design in phase 1.

## Verifier disagreement log — phase-1 rows

The formal file finalizes in phase 3; these rows are visible now per the handling rules.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition |
|---|---|---|---|---|---|
| 2026-07-20 | rathist-2026-07-20 | FY25 equity 128.13 Cr | MISMATCH; audited 137.02 Cr (AR p.79 / Q4 FY26 results FY25 comparative p.8) | Gate 0 Block A used 128.13 Cr for ROE | GATE HELD — corrected at source (137.02 Cr); band unchanged |
| 2026-07-20 | rathist-2026-07-20 | FY25 borrowings | CONFLICT; AR 37.74 Cr vs Q4 comparative 0.00 Cr, both audited, no note | Gate 0 Block D and B02 finding #12 cited a 0.00->37.74 re-leveraging | GATE HELD — unresolved audited-source conflict flagged for company/auditor clarification; band unchanged; not REWORK |
| 2026-07-20 | rathist-2026-07-20 | FY26 other income 0.44 Cr | MISMATCH; audited 0.12 Cr (Q4 FY26 results) | Gate 0 Block D EBITDA / coverage | GATE HELD — corrected at source (0.12 Cr) |
| 2026-07-20 | rathist-2026-07-20 | VRAJ capex IPO funded | Verifier D source_fidelity: overstated; actual HDFC debt + internal accruals (CARE p.2, p.4) | B06 capex_cycle / capital access cross-peer hypothesis | GATE HELD — corrected/softened in synthesis before narrative |
