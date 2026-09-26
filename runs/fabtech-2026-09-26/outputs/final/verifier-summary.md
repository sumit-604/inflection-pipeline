# Fabtech Technologies (FABTECH): Verifier Summary (Phase 1)

_Phase 1 verifiers only: A (numerical, B12a run 2), B (red flag coverage, B12b), D (peer utilisation, B12d), and the Gate 0 plus Emerging Moat half of C (framework, B12c). Verifier C's valuation half is pending Phase 3. Findings sorted CRITICAL, then MAJOR, then MINOR._

## Phase 1 confidence delta

| Component | Score | Acceptance basis |
|---|---|---|
| Numerical acceptance (Verifier A / B12a run 2) | 98.6 | 69 clean of 70 checked (material universe about 110); 0 CRITICAL, 1 MAJOR, 0 MINOR; 2 false positives struck |
| Red flag coverage (Verifier B / B12b) | 67 | material_caught 14 of material_found 21 (7 caught + 7 partially caught); 33 on full catches only (7 of 21) |
| Framework adherence (Verifier C / B12c, Phase 1 half) | 72.1 | 49 of 68 rules passed (Gate 0 32 of 41, EM 17 of 27) |
| Peer utilisation (Verifier D / B12d) | 83.3 | 10 of 12 peer transcripts substantive, 2 cited only, 0 unused (orchestrator basis); B12d reports acceptance 100 |
| **Overall** | **67** | min of four; set by red flag coverage; band 60 to 74 (PROCEED verdicts downgrade one level); REWORK not forced |

**Alternative reading (named, not substituted).** Red flag coverage on full catches only is 33. That reading sits below 60 and would force REWORK. The section 5 rule counts material_caught as B12b reports it (caught plus partially caught), which gives 67.

**Verifier A identity check (run log).** Verifier A run 1 carried two CRITICAL rows, both on B01 D2 (interest coverage):
1. Depreciation: claimed Rs 5.30 Cr; run 1 source_truth "Rs 53.02 Cr (530.15 lakh)". 530.15 lakh = Rs 5.30 Cr (inputs/results/20260427-Results_FY26_audited.txt line ~243). Same value; struck.
2. Finance costs: claimed Rs 4.16 Cr; run 1 source_truth "Rs 41.59 Cr (4158.6 lakh)". The filing reads "41590" = 415.90 lakh = Rs 4.16 Cr (same file, line ~242). Same value; struck.

Cause: a 10x lakh to crore conversion inside the verifier. Verifier A was re-invoked once with the severity addendum. Run 2 governs: 70 figures, 0 CRITICAL, 1 MAJOR, acceptance 98.6, both run 1 CRITICALs struck by Verifier A itself as false positives. Run 1 files are kept as *-run1-superseded.

---

## Findings (sorted by severity)

### CRITICAL

None surviving across all four verifiers. The two run 1 Verifier A CRITICAL rows were struck (identity check above).

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A (B12a) | B07 Section 1C revenue mix table, Africa line | Africa named list omits Morocco (5.4%); Kenya 10.6% + Morocco 5.4% + Egypt 1.6% + Algeria 1.5% = 19.1%. Rest of World cited as Rs 14,366.08 lakh (35%); AR segment note shows Rs 8,596.94 lakh (20.9%). source_fidelity: false |
| B (B12b) | B05 overall | MISSED: founder admission of discretionary shipment and revenue timing (Concall_Feb_2026 p.12) |
| B (B12b) | B05 overall | MISSED: contradictory revenue recognition descriptions across speakers and calls (Concall_Apr_2026 p.16; Concall_Aug_2026 p.3, p.8, p.9) |
| B (B12b) | B05 4B peer question 4 | MISSED: retention terms contradiction; B05 adopts the Aug version as fact (Concall_Feb_2026 p.13; Concall_Aug_2026 p.11) |
| B (B12b) | B05 1B | MISSED: hot lead pipeline figure swings USD 455m to USD ~200m to Rs 3,800 Cr (Concall_Feb_2026 p.7; Concall_Apr_2026 p.11; Concall_Aug_2026 p.4) |
| B (B12b) | B05 1B, 2A row 4, 3D, trigger 1 | MISSED contradiction and misread: SACE incorporated per CEO, Saudi acquisition still proposed; B05 states "closed" (Concall_Aug_2026 p.4-5 vs p.6, p.19) |
| B (B12b) | B05 2A | MISSED broken promise: FY26 margins "better than last year, for sure" (Concall_Nov_2025 p.15; Concall_Apr_2026 p.9) |
| B (B12b) | B05 overall | MISSED: forex heavy other income (~Rs 12 Cr of ~Rs 21 Cr) against PAT Rs 38.36 Cr (Concall_Apr_2026 p.18) |
| B (B12b) | B05 4D | UNDER-WEIGHTED: order book and segment split refused in all four calls (repeated evasion) graded LOW-MEDIUM; Apr "I'll just pull up the data" never delivered (Concall_Nov_2025 p.11; Concall_Feb_2026 p.12; Concall_Apr_2026 p.14; Concall_Aug_2026 p.13, p.15) |
| B (B12b) | B05 2D | PARTIAL: related party procurement 11% FTCL panels plus ~15% AHU via Advantek (Apr) restated as "not more than 11%" (Aug); B05 misattributes the 15% to FTCL and misses the Aug understatement (Concall_Apr_2026 p.17; Concall_Aug_2026 p.19) |
| B (B12b) | B06 Part 1 Q2, flags | NOT SUPPORTED: 33%/43% read as cost inflation; it is rupee cost growth vs revenue +28% (Concall_Apr_2026 p.9, p.21) |
| B (B12b) | B06 Part 2E(i), risks_peers_raise | NOT SUPPORTED: claim that Fabtech never cites client side slippage (Concall_Feb_2026 p.12; Concall_Apr_2026 p.12, p.19; Concall_Aug_2026 p.7) |
| B (B12b) | B06 Part 1 Q3 VERIFIED | OVERSTATED: HLEGLAS deferral is domestic CDMO/agro; PRAJIND delays are domestic CBG plus Praj's own deferral on RM cost uncertainty; only SETL May-2026 is export/war linked. "Meaningfully de-risks LBF1" does not follow (HLEGLAS-Concall_Jun_2026 L588-596; PRAJIND-Concall_Jun_2026 L162-165, L188-190, L306-309; SETL-Concall_May_2026 L443) |
| B (B12b) | B05 2A row 4 | PROMISE ROW WRONG: "Apr-2026: two acquisitions in next 2-3 quarters" is not in the Apr call; outcome "Saudi closed" contradicts CEO (Concall_Apr_2026 p.15; Concall_Aug_2026 p.4-5, p.19) |
| B (B12b) | B05 2A row 10 | PROMISE ROW WRONG: Nov-2025 promised receivable improvement only, not deleveraging; row marks Delivered while row 7 marks the same Nov promise Missed (Concall_Nov_2025 p.7; Concall_Apr_2026 p.3) |
| C (B12c) G-B3 | 01-gate0.md B3/B2 | Screener FCF used; FY26 FCF 5 > CFO 0.48 impossible under the fixed formula; B3 likely 1 to 0 |
| C (B12c) G-B4 | 01-gate0.md B4 | Working Capital Days substituted for the fixed formula; CCC row +4 days gives B4 = 3 |
| C (B12c) G-M11 | 01-gate0.md M11 | Sole moat awarded on an unconfirmed component with mislabelled windows; strict 0, moat class NONE |
| C (B12c) G-DB-YEARS | 01-gate0.md deal-breakers; B01 analyst_note | FY25 labelled post listing; it is pre listing (listing 07-Oct-2025) |
| C (B12c) E-R1 | 07-emoat.md Section 5 R1 vs 4B | Management claim tailwinds scored as documented at 1.0; 3.0 to 2.1 |
| C (B12c) E-H3 | 07-emoat.md H3 | Registered optionality scored; KP Group double credit; 0.7 to 0 |
| C (B12c) E-H2 | 07-emoat.md H2 | SACE credited in H1, H2, R1; HH contradicts Moderate; 2.8 to 1.0; with E-R1 and E-H3, MODEST to NONE (em_score 13.3 stated, 9.9 recomputed) |

### MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| B (B12b) | B05 2A | PARTIAL: Apr promise "Q1 and Q2 the receivable will be reduced immediately" broken (Rs 211 to 215 Cr); Saudi receivable Rs 72.57 Cr vs Saudi Q1 revenue Rs 17.14 Cr, one ~Rs 120 Cr contract (Concall_Apr_2026 p.18; Concall_Aug_2026 p.3-4, p.11) |
| B (B12b) | B05 trigger 5, B06 Part 5 | PARTIAL: Africa called margin dilutive (Apr) then a higher margin growth driver (Aug); PRAJIND says construction heavy Africa orders dilute margin (Concall_Apr_2026 p.8-9; Concall_Aug_2026 p.6; PRAJIND-Concall_Mar_2026 L358-367) |
| B (B12b) | B05 3B, B06 Q2 | PARTIAL: same call contradiction on cost impact ("very small... compensated" vs RMC +33%, execution +43%) and on pass through (Apr "I would not say pass on" vs Aug ">5% passing over") (Concall_Apr_2026 p.10, p.11, p.21; Concall_Aug_2026 p.16-17; SETL-Concall_Aug_2026 L258-263) |
| B (B12b) | B05 2D | PARTIAL: FY28 PAT 12-14% "we're on track" (Aman) vs Karan's PAT 9-11% target in the same call (Concall_Apr_2026 p.20, p.21) |
| B (B12b) | B05 3D | PARTIAL: repeat customer share ~10% accepted as a "deliberate strategy" reframe; cuts against the Nov-2025 repeat client moat narrative (Concall_Aug_2026 p.13-14; Concall_Nov_2025 p.6) |
| B (B12b) | B06 Part 1 Q6 | OVERSTATED: CONTRADICTED verdict rests on equipment makers' competitive sets; none operates in turnkey pharma plant EPC (Concall_Aug_2026 p.18; SETL-Concall_Nov_2025 L263-273) |
| B (B12b) | B05 2A row 6 | Misstatement: 9-11% is a higher ceiling than 9.9-10.5%, not lower; Apr call itself also gives 9-11% (Concall_Apr_2026 p.4, p.21) |
| B (B12b) | B05 overall | MISSED: recurring Rs 20-22 Cr quarter end port inventory (Concall_Feb_2026 p.6; Concall_Aug_2026 p.16) |
| B (B12b) | B05 overall | MISSED: execution tenor drift 9-18 to 12-36 months (Concall_Feb_2026 p.7; Concall_Aug_2026 p.9) |
| B (B12b) | B05 3D | MISSED: ticket size unit confusion, USD vs Rs Cr (Concall_Apr_2026 p.6, p.8) |
| B (B12b) | B05 3D | MISSED: CGO/CEO contradiction on civil contracts (Concall_Aug_2026 p.14) |
| B (B12b) | B05 overall | MISSED: Nov-2025 analyst insistence on guidance (Concall_Nov_2025 p.4-5, p.15-16) |
| B (B12b) | B05 1C | PARTIAL: win rate 15% (Feb) falls to "now 11%" (Apr); noted only as "basis shifts" (Concall_Feb_2026 p.9; Concall_Apr_2026 p.13) |
| B (B12b) | B05 trigger 1 | PARTIAL: scope drift from "not focused on non-pharma" (Nov) to non-pharma MEP/civil via SACE (Aug) treated as a positive trigger only (Concall_Nov_2025 p.12; Concall_Aug_2026 p.4, p.19) |
| B (B12b) | B05 2C | PARTIAL: FY23 revenue fall question dodged and "not discussing in a forum" not logged (Concall_Feb_2026 p.21, p.22) |
| B (B12b) | B05 2D | OVERSTATED: Company Secretary resignation (24-Sep-2026) post-dates every call; its absence from transcripts is not a disclosure failure (Concall_Aug_2026 cover letter dated 03-Aug-2026) |
| B (B12b) | B06 Part 1 Q4, Part 3 | Misattribution: 220-240 days is the analyst's figure in SETL Aug-2026 (not May-2026); SETL management said 320 days last year (SETL-Concall_Aug_2026 L558-566) |
| B (B12b) | B05 1B | Nov-2025 "120 to 150 days" was a market average receivable range, not the company WC cycle (Concall_Nov_2025 p.7) |
| C (B12c) G-A3 | 01-gate0.md A3 | FY20 ROE omitted; median 27.8%; score unchanged |
| C (B12c) G-D2 | 01-gate0.md D2 | EBIT basis undeclared; 4 to 5 on PBT + interest |
| C (B12c) G-D1D3 | 01-gate0.md D1, D3 | Two debt bases in one block; no score change |
| C (B12c) G-E2 | 01-gate0.md E2 | RHP provided but not read; N/A misapplied |
| C (B12c) G-M1 | 01-gate0.md M1 | Peak to latest instead of endpoints; 0 to 1 |
| C (B12c) E-E1 | 07-emoat.md E1 | First mover rests on management claim Djibouti; 1.0x generous |
| C (B12c) E-RECOUNT | 07-emoat.md Section 3 recount | 6 vs 7 categories; Djibouti counted as documented |
| C (B12c) E-YAML-CONSIST | B07-emoat.yaml | Labels differ from report; register 7 vs 8 rows; Weak rows listed |
| C (B12c) E-2C | B07-emoat.yaml capex_embedded_growth_pct | Numeric 0 where NOT FOUND belongs |
| C (B12c) E-SM-COUNT | 07-emoat.md Section 3 count line | G1 counted as Moderate; true count 4 |
| D (B12d) | B06 Part 3 peer coverage map, HLEGLAS Q4 FY25 row | CITED-ONLY is correct, but the transcript also carries an unused tangential domestic competitor remark (Kinam sub-business); industry context miss, not claim relevant (HLEGLAS-Concall_May_2025_Transcript.txt, p.~14, line ~670) |

### Verifier totals

| Verifier | CRITICAL | MAJOR | MINOR | Acceptance |
|---|---|---|---|---|
| A (B12a run 2) | 0 (2 struck in run 1) | 1 | 0 | 98.6 |
| B (B12b) | 0 | 14 | 18 | 67 (33 full catches only) |
| C (B12c, Phase 1 half) | 0 | 7 | 10 | 72.1 |
| D (B12d) | 0 | 0 | 1 | 100 (orchestrator basis 83.3) |

Verifier C classification concurrence: Gate 0 AVERAGE survives every recomputation (core 58, range 58 to 60; deal-breakers #2 and #4 still fire). Combined assessment AVERAGE unchanged. EM classification recomputed MODEST to NONE.

Verifier B credibility concurrence: lower, C to D.

---

## Verifier disagreement log (source fidelity)

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-26 | fabtech-2026-09-26 | FY26 consolidated depreciation Rs 5.30 Cr (B01 D2) | Run 1 CRITICAL MISMATCH, source_fidelity true, "Rs 53.02 Cr (530.15 lakh)"; audited results p.7 | Orchestrator identity check: 530.15 lakh = Rs 5.30 Cr, same value | FLAG CLEARED: source re-check found the number at the correct anchor (inputs/results/20260427-Results_FY26_audited.txt line ~243); re-checked by the orchestrator, confirmed by Verifier A run 2 | 10x lakh to crore slip in the verifier; run 2 struck it as a false positive |
| 2026-09-26 | fabtech-2026-09-26 | FY26 consolidated finance costs Rs 4.16 Cr (B01 D2) | Run 1 CRITICAL MISMATCH, source_fidelity true, "Rs 41.59 Cr (4158.6 lakh)"; audited results p.7 | Orchestrator identity check: filing reads 41590 = 415.90 lakh = Rs 4.16 Cr | FLAG CLEARED: source re-check found the number at the correct anchor (same file, line ~242); re-checked by the orchestrator, confirmed by Verifier A run 2 | Same cause; interest coverage stands |
| 2026-09-26 | fabtech-2026-09-26 | FY26 consolidated trade receivables Rs 24,151.90 lakh (AR balance sheet face, OCR) | Run 1 MAJOR, source_fidelity true; AR Note 13, MD&A and audited results show Rs 20,433.51 lakh | B02 settled the face figure as a filing drafting error | GATE HELD: figure corrected at source; Rs 20,433.51 lakh (AR Note 13; FY26 audited results) carried in every downstream use | The Rs 24,151.90 lakh figure appears nowhere as a valid input in the final files |

Run 2 of Verifier A raised no source fidelity finding. No other downstream step leaned on a flagged number.
