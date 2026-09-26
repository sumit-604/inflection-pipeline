# QMSMEDI verifier summary (phase 1, run 2026-09-26)

Units: All figures in ₹ Cr unless the source says otherwise; the source unit is on the face of the document, not in the filename.

## Phase 1 confidence delta

| Component | Score | Verifier | Scope |
|---|---|---|---|
| numerical_acceptance | 87 | A (B12a run 2, governs; claude-haiku-4-5) | 30 numbers checked: 26 clean, 3 partial, 1 mismatch; material universe 94 across B01 to B09 |
| redflag_coverage | 83.3 | B (B12b; claude-opus-5-5) | 10 of 12 material flags had (5 fully, 5 partially, 2 missed); strict fully caught rate 41.7% recorded, not the rate of record |
| framework_adherence | 79.4 | C (B12c; claude-opus-5-5) | 50 of 63 rules passed (Gate 0 34 of 40, Emerging Moat 16 of 23); valuation half PENDING PHASE 3 |
| peer_utilisation | 100 | D (B12d; claude-sonnet-5) | 12 of 12 peer transcripts substantive and supported |
| overall | 79.4 | min of four | band 75 to 89, normal; set by framework_adherence |

Acceptance rates: A 87, B 83.3, C 79.4 (phase 1 half), D 100. No CRITICAL finding in any verifier. No acceptance rate below 60. Verifier A identity check: B12a run 2 carries 0 CRITICAL rows; nothing struck. Verifier A run 1 (21 numbers, mostly B01) is superseded by run 2.

Counts: CRITICAL 0. MAJOR 13 (A 1, B 9, C 3, D 0). MINOR 19 (A 0, B 9, C 9, D 1).

## CRITICAL

None.

## MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| A | B06 Claim 2 (peer verification, supply chain disruption); POLYMED-Concall_Nov_2025_Transcript.txt, 10-Nov-2025 | Claimed: supply chain or shipping disruption in Oct-2025 to Mar-2026 delayed QMS product orders. Source truth: POLYMED Q2 FY26 call says Suez transit improved from 2.5 months to 1 month in that window; POLYMED's own Gulf logistics disruption starts Q4 FY26 (25-May-2026) and runs export side. Source fidelity: true. Non overridable. |
| B | F1, B05 1A/1B/4A#1; Concall_Aug_2026 Finance Team p.7, Mohit Tamhankar p.8-9; Concall_Jun_2026 p.10 | MISSED: FY27 PSP guide conflicts across speakers (Finance ~Rs 70 Cr run rate and Rs 90 to 100 Cr services vs Mohit Rs 100 to 105 Cr PSP) and does not reconcile with the Rs 216 Cr guide. |
| B | F2, B05 3D; Concall_Aug_2025 Mahesh Makhija p.10; Concall_Jun_2026 Mahesh Makhija p.6 | MISSED: Humrahi (Lupin) 6 to 7% of turnover disclosure withdrawn in Jun-26 ("not allowed to share"). |
| B | F3, B05 1B employee cost row; Jun-26 p.12; Aug-26 p.12 | NOT SUPPORTED: analyst's Rs 16 to 17 Cr a year shown as management guidance; actual ~Rs 11 Cr a quarter settled. |
| B | F4, B05 2B, 4C; Nov-25 p.6 | NOT SUPPORTED: SEBI/IPO fund answer misclassified as proactive positive; it was reactive, non specific and open. Carry as open governance flag. |
| B | F5, B05 1A/3B; B06 Claim 3; INDGN Aug-26 p.16, Feb-26 p.6 | NOT SUPPORTED/misclassified: 60 to 70% rollover = 30 to 40% churn; peer INDGN >100% NRR contradicts; visibility claims shifted Jun-26 to Aug-26. |
| B | F6, B06 Part 5; ENTERO May-26 p.3; POLYMED Aug-26 p.3; INDGN Aug-26 p.10 | NOT SUPPORTED: cross peer margin slippage hypothesis contradicted by all three peers; strike it. |
| B | F7, B05 2D, 3C | PARTIAL: Aug-26 admission that PSP margin is below camps (combined 20 to 25%) not flagged; Q1 FY27 misquoted as ~25%. |
| B | F8, B05 3C, 4D | PARTIAL: Saarathi disclosure regression, Rs 45 Cr for 51% entry price vs ~Rs 2 Cr annualised profit [derived], mixed EBITDA/PAT tranche basis; under weighted at LOW-MEDIUM. |
| B | F9, B05 1C | PARTIAL: services target Rs 60 Cr cut to Rs 50 Cr within a quarter; growth target 50%, then 25%, then 100%; labelled STRENGTHENING. |
| C | 01-gate0.md Block B, B2/B3 | FCF metrics scored on a two year FY25 to FY26 sub window holding Rs 44.86 Cr of CFO against Rs 43.28 Cr for all eight years; rule 5 requires N/A = 0; FY22/FY23 negative CFO proves FCF negative in those years. Recomputed: Block B 11 to 1 strict (DB2 fires) or 8 or less bounded; AVERAGE unchanged. |
| C | 01-gate0.md Block E, E4; B01 input_gaps; Annual_Report_2026.txt line 9442 (Note 42) and line 12945 (Note 40) | Contingent liability note declared absent but present (Rs 5.30 lakh TDS demand, 0.05% of net worth Rs 104.20 Cr); N/A score applied to disclosed data. Recomputed: E4 = 5; Block E 10 to 15. |
| C | 07-emoat.md Section 5, rows D1/D2/F2/R1 | LM scored raw 2; rule is ML/LM = 1. Recomputed: EM 17.1 to 14.25; MODEST unchanged. |

## MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| B | F10, B06 Claim 2 | OVERSTATED: should be PARTIALLY CONTRADICTED; add ENTERO Q4 +42.6% evidence. |
| B | F11, B06 flags; ENTERO May-26 p.11 | ENTERO did not raise Chinese dumping; POLYMED only. |
| B | F12, B05 2A#7 | Promise misrecorded; spot check WRONG. |
| B | F13, B05 1B/2E/4D | "Too early to revise" was the revenue guide; margin answer was a 16 to 20% hedge, missed. |
| B | F14, B05 1A; Concall_Jun_2026 p.5; Concall_Aug_2026 p.10 | "4-5 named" GLP-1 programmes overstated; none named; count moved from 7. |
| B | F15, B06 2B; Aug-26 p.2 | Margin did not fall three straight quarters (Q1 FY27 14.6% > Q4 FY26 13.3%). |
| B | F16, B05 1C | Missed broken "Q4 highest quarter" seasonality claim (Nov-25). |
| B | F17, B05 | Nine minor company items missed (I14, I15, I17 to I21, I23, I26). |
| B | F18, B06; ENTERO-Concall_Feb_2026 p.4-5; ENTERO-Concall_Jun_2026 p.3, p.10-11 | Peer items missed or partial: INDGN price concessions, ENTERO POCT/private label overlap, ENTERO Q4 domestic strength. |
| C | B01 deal_breakers | DB2 not recorded under the strict B2/B3 reading. Recomputed: DB2 fires, cap GOOD, non binding. |
| C | 01-gate0.md M11 | Tier 3 condition misread. Recomputed: 0 or 1; moat count unchanged. |
| C | 01-gate0.md E2 / B01 data_notes | One year window justified by an unsupported "short listing history"; true cause is a corpus gap (only 2025-06-30, 2026-03-31, 2026-06-30 SHP files). Score 0 stands. |
| C | 07-emoat.md Section 5 F2/R1 | Averaged multipliers not in rule; state the governing tier. |
| C | 07-emoat.md B2 | Documented multiplier on an effect the report calls inference; HEINE double credited with H2. Recomputed: B2 2.0 to 1.0. |
| C | 07-emoat.md A1 | Scored while text says NO EVIDENCE FOUND / optionality only; BeamOptics credited in A1 and H1. Recomputed: A1 1.0 to 0. |
| C | 07-emoat.md completionist recount / B07 completionist_recount | Item and category counts do not reconcile with the listed items; restate count. |
| C | 07-emoat.md Section 5 table | 12 zero rows collapsed; presentational. |
| C | B07 capex_embedded_growth_pct | 0 in YAML vs NOT FOUND in text; NOT FOUND. |
| D | B06 Part 2B / industry_cross_read.pricing_inputs; ENTERO Q1 FY27 call | Claimed ENTERO net working capital ~59 to 66 days; source states 61 days, improved from 66 a year ago; 59 day endpoint not located. Non material. |

## Verifier B register detail (as written by Verifier B)

Missed items with anchors:

| Severity | Item | Anchor |
|---|---|---|
| MAJOR | FY27 PSP/services guide conflicts across speakers on one call and does not reconcile with the Rs 216 Cr revenue guide | Concall_Aug_2026 Finance Team p.7; Mohit Tamhankar p.8-9; Concall_Jun_2026 p.10 |
| MAJOR | Humrahi (Lupin) disclosure regression: 6 to 7% of turnover disclosed Aug-25, withheld Jun-26 | Concall_Aug_2025 Mahesh Makhija p.10; Concall_Jun_2026 Mahesh Makhija p.6 |
| MINOR | Camps doubling contradiction within one call | Concall_Jun_2026 p.10; p.9; p.14 |
| MINOR | Single programme needs 1,200 hires vs ~250 plus company headcount (concentration) | Concall_Jun_2026 Management p.11; Concall_Aug_2025 p.2 |
| MINOR | Brand ambassador cost refused under NDA | Concall_Aug_2025 Mahesh Makhija p.4 |
| MINOR | Digital/online sales only ~Rs 20 lakh per month | Concall_Aug_2025 Mahesh Makhija p.5 |
| MINOR | Mainboard eligibility Oct-2025 vs migration 18-Jun-2026, lag unexplained | Concall_Aug_2025 p.10; Concall_Aug_2026 p.2 |
| MINOR | GLP-1 programme count 7 (Jun-26) vs 4 to 5 (Aug-26) | Concall_Jun_2026 p.5; Concall_Aug_2026 p.10 |
| MINOR | Saarathi consolidation explanation changes across three calls | Concall_Nov_2025 p.3; Concall_Jun_2026 p.11; Concall_Aug_2026 p.13 |
| MINOR | Educamedics negligible due to regulation; education not scalable | Concall_Aug_2025 p.3; Concall_Jun_2026 p.13 |
| MINOR | ENTERO scaling MedTech/POCT/IVD distribution and home healthcare private label, overlapping QMS products and Q-Devices | ENTERO-Concall_Feb_2026 Prabhat Agrawal p.4-5 |
| MINOR | ENTERO Q4 FY26 domestic +42.6% and "largely insulated" from the late Feb conflict | ENTERO-Concall_Jun_2026 p.3; p.10-11 |

Promise delivery spot checks: 6 checked, 5 confirmed, 1 wrong. Credibility grade concurrence: "lower: C is the ceiling. B05's only positive (the SEBI answer) is not one, and two disclosure regressions (Humrahi, Saarathi) plus a same-call PSP guidance conflict put it at the C/D boundary".

## Recomputed scores (Verifier C, phase 1)

| Item | Reported | Recomputed | Classification |
|---|---|---|---|
| Gate 0 core | 53 | 48 (strict rule 5) to 55 (bounded); 58 if only E4 corrected | AVERAGE, unchanged in every reading |
| Emerging Moat | 17 (17.1) | 14 (matrix fix only); 12 if A1 and B2 also corrected | MODEST, unchanged (12.25 sits at the band floor) |

## Disagreement record (carried for the phase 3 verifier disagreement log)

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-26 | QMSMEDI-2026-09-26 | B01 consolidated FY26 EBITDA Rs 25.88 Cr | B12a run 1 (superseded) MAJOR: vs AR Rs 26.93 Cr | Orchestrator source re-check: AR consolidated MD&A table (Annual_Report_2026.txt lines 3868-3889) prints EBITDA 2,693.08 lakh including other income 105.31 lakh; ex other income 2,587.77 lakh = Rs 25.88 Cr, the B01 screener basis figure | FLAG CLEARED: source re-check found the number at a correct anchor on the ex other income basis (re-checked by the orchestrator, 2026-09-26) | Run 2 did not re-raise it. |
| 2026-09-26 | QMSMEDI-2026-09-26 | B06 Claim 2, POLYMED Suez quote | B12a run 2 MAJOR, source_fidelity true: POLYMED-Concall_Nov_2025_Transcript.txt | The row restates B06's own conclusion; report and source agree. Verifier B separately reads the claim as PARTIALLY CONTRADICTED | GATE HELD: carried as a candidate false positive, NOT struck (the identity check strikes CRITICAL rows only); the finding stands in all phase 1 outputs | For the phase 3 log. |
