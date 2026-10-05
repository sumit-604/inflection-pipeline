# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE), ESCONET, run 2026-10-05

Model: claude-opus-5-5. Emits: B12c (partial; Gate 0 and Emerging Moat sections only).

## 0. Scope and inputs

This pass covers Gate 0 (B01) and Emerging Moat (B07) compliance only. Rules 2, 3 and 8 of the Verifier C section run here. Rule 6 needs B09 and B11, so it is not run. Rule 9 (stage 13 narrative) and rule 10 (B09b dossier) fire at /finalize. Rules 4, 5, 7 and 11 to 15 cover the valuation audit (B10, B11). They are PENDING PHASE 3.

Rule sources read:
- prompts/12-verifiers-pipeline.md, VERIFIER C section
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- runs/esconet-2026-10-05/outputs/reports/01-gate0.md and outputs/blocks/B01-gate0.yaml
- runs/esconet-2026-10-05/outputs/reports/07-emoat.md and outputs/blocks/B07-emoat.yaml

Data used for re-derivation:
- inputs/screening/screener-Data_Sheet.csv (Rs Cr, consolidated)
- inputs/prospectus/EsconetTechnologies_PROSP.txt (restated standalone Annexures I to III, Rs Lakhs)
- inputs/annual-report/Annual_Report_2026.txt (p.29, p.117, p.132, p.145)
- inputs/results/2026-05-28-ESCONET_28052026185515_Outcome_BM_28052026.txt (consolidated balance sheet, Rs Lakhs)

Not read: the valuation framework docs (dead context in phase 1), other verifiers' outputs, and the makers' reasoning.

Verifier A owns number fidelity. This report judges rule application. Some numbers here are ones the makers did not use: the FY2021 and FY2022 restated figures. Each carries an anchor so Verifier A or the operator can check it.

## 1. Summary

| Framework | Rules checked | Pass | Fail | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 46 | 41 | 5 | 1 | 0 | 4 |
| Emerging Moat (B07) | 26 | 25 | 1 | 0 | 0 | 1 |
| Valuation (B10, B11) | PENDING PHASE 3 | | | | | |
| Total, phase 1 | 72 | 66 | 6 | 1 | 0 | 5 |

There is one more MINOR finding outside the rule rows (F6, an undisclosed D4 sensitivity). Totals: 1 CRITICAL, 0 MAJOR, 6 MINOR. Acceptance rate: 66 of 72 rules passed = 91.7%.

Headline finding (F1, CRITICAL). B01 scored 4 years (FY2023 to FY2026). Gate 0 rule 6 says "minimum 3 years, maximum whatever exists". The run corpus holds audited restated standalone statements for FY2021 and FY2022 (PROSP p.48, Annexure I; p.50, Annexure II; p.51, Annexure III). Before May 2022 the company had no subsidiary (PROSP p.199, Annexure IV note 2: Zeacloud incorporated 11 May 2022). So the standalone figures cover the whole entity. With 6 years, the confidence table says "5-6 lower, flag 'may not have seen full cycle'", and no downgrade applies. The Gate 0 classification is AVERAGE, not AVOID. The B07 combined assessment inherits the same change, AVOID to AVERAGE.

REWORK status: under prompts/12, REWORK fires only on a CONFIRMED Verifier A CRITICAL or an acceptance rate below 60% on a denominator of 4 or more. So F1 does not trigger REWORK by itself. The orchestrator and the operator decide whether stage 1 re-issues B01 on FY2021 to FY2026 and stage 7 refreshes 6C and 6D.

## 2. Gate 0 (B01) compliance

### 2.1 Rule-by-rule table

All figures are Rs Cr from screener-data unless an anchor says otherwise.

| # | Rule (source) | B01 value | Verifier re-derivation | Result |
|---|---|---|---|---|
| 1 | Opening line "Data available: [X] years" (01 rule 6) | Present (01-gate0.md line 3) | Present | PASS |
| 2 | History window "maximum whatever exists" plus the data-confidence table (01 rule 6; CLASSIFICATION AND OVERRIDES) | 4 years, FY2023 to FY2026; LIMITED; one-tier downgrade; history_downgrade true | 6 years exist, FY2021 to FY2026 (PROSP p.48, p.50, p.51, restated standalone; no subsidiary before 11 May 2022, PROSP p.199). Band 5-6 = "lower, flag", no downgrade. history_downgrade false | FAIL, CRITICAL (F1) |
| 3 | ROCE: use the source's ROCE if given, else compute and state (01 FORMULA) | Computed and stated | Data_Sheet carries no ROCE row (screener-data rows 9 to 63) | PASS |
| 4 | ROE = PAT / average net worth; use closing only if opening is unavailable (01 FORMULA) | FY23 on closing net worth, "opening NOT FOUND" | Opening exists: 76.71 + 173.74 = 250.45 Lakhs at 31 Mar 2022 (PROSP p.48, Annexure I). FY23 ROE on average = 3.03 / ((2.50 + 5.54) / 2) = 75.3%. A3 median stays 20.3%, score 5 | FAIL, MINOR (F2) |
| 5 | WC days formula, basis stated (01 FORMULA) | Revenue basis, stated | Revenue basis is the default | PASS |
| 6 | FCF = CFO minus capex (01 FORMULA) | Applied | Applied | PASS |
| 7 | CAGR = (End / Start)^(1/years) - 1 (01 FORMULA) | Applied, 3 years | (354.40 / 94.59)^(1/3) - 1 = 55.3% | PASS |
| 8 | CAGR edge rules (01) | No negative endpoint; "No loss-to-profit swing" | Correct on the window B01 used. On the full window, FY21 PAT is -100.48 Lakhs (PROSP p.50). C2 and C4 then go N/M, and data_notes need "loss-to-profit swing, FY21 to FY22". Carried under F1 | PASS (window-dependent) |
| 9 | A1 median ROCE (15-19.9 = 3) | 19.7%, scored 3 | ROCE 58.46%, 23.28%, 16.13%, 11.96%; median (16.13 + 23.28) / 2 = 19.70%, scores 3 | PASS |
| 10 | A2 minimum ROCE (12-14.9 = 3; 8-11.9 = 1) | 11.96%, scored 1 | Below 12 on a continuous reading, so 1. The rubric leaves 11.91 to 11.99 unassigned (observation O1). B01 disclosed this (B01-gate0.yaml data_notes item 3) | PASS |
| 11 | A3 median ROE (≥20 = 5) | 20.3%, scored 5 | Median of 8.20%, 14.96%, 25.60% and the FY23 figure = 20.28%, scores 5 | PASS |
| 12 | A4 ROCE trend (decline >5pp = 0) | 58.5% to 11.96%, scored 0 | Decline 46.5pp, scores 0 | PASS |
| 13 | B1 cumulative CFO / cumulative PAT | -0.44, scored 0 | -10.01 / 22.62 = -0.44, scores 0 | PASS |
| 14 | B2 FCF-positive years | 0 of 4, scored 0 | FCF -3.02, -3.47, -1.63, -16.80; scores 0 | PASS |
| 15 | B3 cumulative FCF / cumulative PAT | Negative, scored 0 | -24.92 / 22.62; scores 0 | PASS |
| 16 | B4 change in WC days (±5 = 3) | -0.5 days, scored 3 | FY23: 48.58 + 33.07 - 38.82 = 42.83 days. FY26: 45.59 + 53.04 - 56.30 = 42.33 days. Change -0.50; scores 3 | PASS |
| 17 | C1 revenue CAGR | 55.3%, scored 5 | Confirmed | PASS |
| 18 | C2 PAT CAGR | 26.7%, scored 5 | (6.16 / 3.03)^(1/3) - 1 = 26.7%; scores 5 | PASS |
| 19 | C3 positive YoY revenue years | 3 of 3, scored 5 | Confirmed | PASS |
| 20 | C4 PAT CAGR minus revenue CAGR | -28.6pp, scored 0 | Confirmed | PASS |
| 21 | D1 net debt / EBITDA | Net cash, scored 5 | 13.24 - 27.38 = -14.14; scores 5 | PASS |
| 22 | D2 EBIT / interest (5-9.9 = 4) | 8.3x, scored 4 | 9.80 / 1.18 = 8.31x; scores 4 | PASS |
| 23 | D3 debt / equity (0.1-0.5 = 4) | 0.17, scored 4 | 13.24 / 80.19 = 0.165; scores 4 | PASS |
| 24 | D4 current ratio (1.5-1.99 = 4) | 1.85, scored 4 | 13,647.86 / 7,372.96 Lakhs = 1.85 (AR FY26 p.132); scores 4. The AR basis is the audited, screener-consistent choice. The results-filing basis gives 2.28, which scores 5 and is undisclosed (F6) | PASS |
| 25 | E1 promoter holding (≥60 = 5) | 60.19%, scored 5 | Scores 5 | PASS |
| 26 | E2 promoter change over 3 years | -4.75pp over 2.4 years, scored 0 | Decrease >3, scores 0. A full 3-year window reaches before the IPO, when the holding was higher, so the score cannot rise | PASS |
| 27 | E3 pledge | 0%, scored 5 | Confirmed | PASS |
| 28 | E4 contingent liabilities / net worth | 0%, scored 5 | AR FY26 p.145 item 1 and p.117 item 1 both say the company "does not have any contigent liabilities" (sic). Commitments sit in item 2, outside the E4 formula | PASS |
| 29 | Block sums and core | 9 + 3 + 15 + 17 + 15 = 59 | Confirmed | PASS |
| 30 | M1 pricing power | -3.9pp with CAGR 55.3%, scored 1 | EBITDA ex other income: 6.04 / 94.59 = 6.39% to 8.81 / 354.40 = 2.49%. "Declined 2-5pp despite growth" = 1 | PASS |
| 31 | M2 cost advantage | 2.49% vs peer median 4.99%, scored 0 | 2.5pp below, scores 0. Still below without Orient (median 7.99%) | PASS |
| 32 | M3 capital efficiency | FAT 19.3x, ROCE 11.96%, scored 0 | Latest-year pair; ROCE is not >12, so 0. The rubric does not name the ROCE year (observation O3) | PASS |
| 33 | M4 customer stickiness | Receivable days 48.6 to 45.6, scored 5 | The endpoint reading matches M10's "over period" wording. B01 disclosed the FY24 peak of 96.9 days. A full-series reading gives 3, and the moat stays present | PASS |
| 34 | M5 scale | PEER DATA NEEDED, scored 0 | Applied as written | PASS |
| 35 | M6 R&D | NOT FOUND, scored 0 | AR row blank. Margin is below the peer median, so the 1-band fails too | PASS |
| 36 | M7 regulatory | Unregulated, scored 0 | Applied | PASS |
| 37 | M8 distribution ("mentioned unquantified = 1") | "Reach not quantified in AR; NOT FOUND", scored 0 | AR FY26 p.29, "Regional diversification", names operations across Bengaluru, Chennai and Hyderabad, with no count. That is the 1-band condition. Recomputed 1 | FAIL, MINOR (F3) |
| 38 | M9 brand (GM proxy) | 10.9% vs 21.0%, scored 0 | (354.40 - 315.92) / 354.40 = 10.86%; at or below peers, scores 0 | PASS |
| 39 | M10 switching costs | Scored 5 | Revenue grew every year; receivable days -3.0 over the period; scores 5 | PASS |
| 40 | M11 network effects (under 6 years: "score conservatively on the overall trend") | Selling % 4.81, 3.91, 3.95, 4.27; scored 1 on "rising since FY24" | The overall trend runs 4.81% (FY23) to 4.27% (FY26), so it declines. With revenue CAGR 55.3% (≥20%) the rule gives "stable/declining = 3". The 1-band needs "selling % rising", and the overall trend does not show that. Recomputed 3 | FAIL, MINOR (F4) |
| 41 | M12 negative WC (>45 = 0) | Median 45.3 days, scored 0 | The rubric names no statistic. The median is reasonable, and B01 disclosed that the latest year (42.3) would score 1 | PASS |
| 42 | Moat count and class | 2 present, MODERATE | Correct on B01's scores. With F3 and F4: M4, M10 and M11 are present (3), still MODERATE; moat_score 15, grand total 74 | PASS |
| 43 | Classification matrix | Core 59 gives AVERAGE before the downgrade | Core 40-59 = AVERAGE | PASS |
| 44 | Deal-breakers with driving years | DB2 and DB4, years named; others not triggered | Confirmed. DB8 is not triggered on either window, because FY24 to FY26 PAT is positive | PASS |
| 45 | FLAG-GATE0 (classification ≤ AVERAGE with depressors) | Raised | Still required at AVERAGE | PASS |
| 46 | YAML block per the 01 template | The block embedded in the report has data_notes as a string pointer and a shorter analyst_note. The block file has an 18-item list | The template needs data_notes as a list and "exactly this fenced YAML block". The two copies diverge | FAIL, MINOR (F5) |

### 2.2 Full-history recompute (F1)

FY2021 and FY2022 inputs. Rs Lakhs come from the restated standalone statements, divided by 100 to give Rs Cr.

| Item | FY21 | FY22 | Anchor |
|---|---|---|---|
| Revenue | 44.12 | 68.56 | PROSP p.50, Annexure II: 4,411.89; 6,856.29 Lakhs |
| Other income | 0.08 | 0.03 | PROSP p.50: 8.45; 3.08 Lakhs |
| Finance cost | 0.72 | 0.77 | PROSP p.50: 72.35; 77.21 Lakhs |
| Depreciation | 0.44 | 0.65 | PROSP p.50: 43.97; 64.98 Lakhs |
| PBT | -1.05 | 0.60 | PROSP p.50: -104.84; 60.17 Lakhs |
| PAT | -1.00 | 0.72 | PROSP p.50: -100.48; 72.36 Lakhs |
| Total assets | 17.48 | 25.88 | PROSP p.48, Annexure I: 1,748.40; 2,587.76 Lakhs |
| Current liabilities | 12.27 | 19.11 | PROSP p.48: 321.49 + 875.67 + 24.42 + 4.94; 378.40 + 1,455.22 + 71.74 + 5.41 Lakhs |
| Net worth | 1.78 | 2.50 | PROSP p.48: 76.71 + 101.38; 76.71 + 173.74 Lakhs |
| Receivables / inventory / payables | 8.65 / 5.86 / 8.76 | 15.46 / 5.86 / 14.55 | PROSP p.48 |
| CFO | -0.22 | 0.80 | PROSP p.51, Annexure III: -22.13; 80.24 Lakhs |
| Capex (PPE purchase) | 0.58 | 1.52 | PROSP p.51: 58.36; 151.87 Lakhs |

Derived figures for FY21 and FY22:
- ROCE = EBIT / (total assets minus current liabilities): FY21 -32.49 / 521.88 = -6.2%; FY22 137.38 / 676.99 = 20.3%.
- ROE: FY21 -56.4% on closing net worth (opening NOT FOUND in the corpus); FY22 0.72 / 2.14 = 33.8%.
- FCF: FY21 -0.80; FY22 -0.72.
- WC days: FY21 71.6 + 48.5 - 72.4 = 47.6; FY22 82.3 + 31.2 - 77.5 = 36.0.
- EBITDA margin ex other income: FY21 3.03 / 4,411.89 Lakhs = 0.07%; FY22 2.91%.

FY2023 to FY2026 inputs stay as B01 used them.

Recomputed blocks, 6 years:

| Item | Value | Score |
|---|---|---|
| A1 median ROCE | -6.2, 11.96, 16.1, 20.3, 23.3, 58.5; median 18.2% | 3 |
| A2 minimum ROCE | -6.2% (FY21) | 0 |
| A3 median ROE | -56.4, 8.2, 15.0, 25.6, 33.8, 75.3; median 20.3% | 5 |
| A4 ROCE trend | 11.96% latest ≥ -6.2% earliest | 5 |
| Block A | | 13 |
| B1 | Cumulative CFO -9.43 / cumulative PAT 22.34 = -0.42 | 0 |
| B2 | 0 of 6 FCF-positive years | 0 |
| B3 | Cumulative FCF -26.44, negative | 0 |
| B4 | 47.6 to 42.3 days = -5.3 (0.3 days past the 5-day line) | 5 |
| Block B | | 5 |
| C1 | (354.40 / 44.12)^(1/5) - 1 = 51.7% | 5 |
| C2 | N/M (FY21 PAT negative endpoint) | 0 |
| C3 | 5 of 5 years positive | 5 |
| C4 | N/M (PAT CAGR N/M) | 0 |
| Block C | | 10 |
| Block D | Latest-year tests, unchanged | 17 |
| Block E | Unchanged | 15 |
| Core | 13 + 5 + 10 + 17 + 15 | 60 |

Moat block, 6 years:
- M1 = 5 (margin 0.07% to 2.49%, +2.4pp, CAGR 51.7%).
- M4 = 3 (receivable days 71.6 to 45.6, not stable; zero decline years).
- M8 = 1 (F3).
- M10 = 5.
- M11 is not re-derived. The two-window test becomes available with 6 years, but the FY21 and FY22 selling-expense split sits in PROSP Annexure II note II.6, which this pass did not extract. Its range is 1 to 5.
- All other tests score 0, as in B01. M12 median 45.2 days still scores 0.
- Moat score 15 to 19, with 3 or 4 present: MODERATE or STRONG.

Classification, 6 years:
1. Core 60 falls in the 60-79 band: GOOD (MODERATE) or GOOD+ (STRONG).
2. Data confidence for 6 years is "lower, flag 'may not have seen full cycle'", so there is no downgrade.
3. DB2 (Block B 5 < 8) caps at GOOD. DB4 (-0.42 < 0.50) caps at AVERAGE. DB8 is not triggered.
4. Result: **AVERAGE**.

The result is robust. If B4 drops to 3, core is 58 (AVERAGE). With D4 on the results-filing basis, core is 61 (DB4 caps it at AVERAGE). M11 can only move the moat class. In every case the classification is AVERAGE.

Fields B01 should carry on re-issue:
- data_years 6; fy_range "FY2021 to FY2026"; history_downgrade false
- blocks {A: 13, B: 5, C: 10, D: 17, E: 15}; core_score 60; classification "AVERAGE"
- deal_breakers DB2 and DB4, with FY21 and FY22 added to the driving years
- data_notes add "loss-to-profit swing, FY21 to FY22" and "may not have seen full cycle"
- FLAG-GATE0 stays raised

Downstream effect: the B07 6C table and the 6D combined assessment change from AVOID to AVERAGE. Gate 0 AVERAGE with Emerging Moat NONE (5.5) gives AVERAGE. HIGH POTENTIAL still fails on its forward half. B07's TURNAROUND reasoning does not depend on the label.

Basis note: FY21 and FY22 are standalone under Indian GAAP. FY23 onward is consolidated, also under Indian GAAP (PROSP p.199). The only subsidiary was incorporated 11 May 2022, so the two bases cover the same entity for FY21 and FY22.

### 2.3 Boundary sensitivities in B01's own 4-year frame (observations)

AVOID sits at core 59, one point under the 60 line. In the 4-year frame, each of two readings below lifts core to 60 or 61. That gives GOOD before the downgrade and AVERAGE after it.

- O1, A2 rubric gap. Bands "12-14.9 = 3" and "8-11.9 = 1" leave 11.91 to 11.99 unassigned. 11.96% scores 1 on a continuous reading and 3 on a one-decimal rounding reading. B01 disclosed this. This is a framework text gap to be fixed in prompts/01 by operator ruling, not a maker error. Other bands in 01 have the same gap pattern.
- O2, D4 under the source conflict. On the results-filing basis (results 2026-05-28, consolidated balance sheet), current assets are 5,149.87 + 1,963.93 + 2,737.70 + 186.21 + 1,147.15 = 11,184.86 Lakhs. Current liabilities are 1,219.34 + 3,004.26 + 403.57 + 282.79 = 4,909.96 Lakhs. The ratio is 2.28, which scores 5. Capital employed is the same on both bases (8,192.12 Lakhs), so ROCE does not move. B01 disclosed the M4 sensitivity but not this one (F6).
- O3, M3 ROCE year. The rubric does not say latest or median. Median ROCE 19.7% with FAT 19.3x would score 3. That adds one present moat; the class stays MODERATE.
- O4, FY23 basis mix. FY23 ROCE uses the consolidated balance sheet (PROSP p.190) with screener PBT, which equals the restated standalone figure. B01 disclosed this. The band outcome does not change.

After F1 is corrected, O1 and O2 no longer move the classification. DB4 caps at AVERAGE and no downgrade applies.

## 3. Emerging Moat (B07) compliance

### 3.1 Rule-by-rule table

| # | Rule (source) | B07 | Result |
|---|---|---|---|
| 1 | All six sections plus the optionality register, in order (07 rule 1) | Sections 1 to 6 and the register are present. Section 0 (verification priorities) is extra | PASS |
| 2 | Evidence taxonomy tag on every evidence item (07 rule 2) | Every Section 3 table row is tagged 📄, 🎙️ or 🔍 | PASS |
| 3 | Source anchor on every evidence item (07 rule 3) | Anchored. The 🔍 shared-chassis row says "none filed", which fits an inference | PASS |
| 4 | Section 1: 1A, 1B and 1C per spec | Present, with NOT FOUND where data is missing | PASS |
| 5 | Section 2: 2A, 2B and 2D per spec | Present | PASS |
| 6 | 2C: capex under execution × historical FAT, arithmetic shown | Committed capital contracts are NIL (AR p.117, p.145), so the result is 0. The mechanical alternative (450 Lakhs × 48.4x) is shown and rejected with a reason. The 450 Lakhs are issue proceeds earmarked for Zeacloud, not capex under execution | PASS |
| 7 | All 22 categories plus R1 addressed, or NO EVIDENCE FOUND (Verifier C rule 3) | A1 to I2 plus R1 = 23 rows in Section 3, the summary table and the Section 5 scorecard | PASS |
| 8 | NO EVIDENCE FOUND discipline, no force-fit (07 rule 5) | 17 rows say NO EVIDENCE FOUND. F2 and G2 cite counter-evidence and score 0 | PASS |
| 9 | Summary table: evidence, type, strength, time to materialise | All 23 rows | PASS |
| 10 | Strong or Moderate count stated | "Strong or Moderate rows: 0" | PASS |
| 11 | Completionist recount: present AND accurate; evidence_mix item counts (07 rule 6, Section 3) | The line is present: "6 documented items across 3 categories (A4, B2, H2)". The Section 3 tables tag 12 📄 items across 5 categories. evidence_mix {6, 5, 1} against the tables' {12, 9, 1} | FAIL, MINOR (F7) |
| 12 | Completionist guard: 12 or more active categories means re-examine | 6 categories carry evidence; the guard does not trip | PASS |
| 13 | Likelihood × impact matrix values (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1) | ML = 1, LL = 1, MM = 2, LM = 1 | PASS |
| 14 | Evidence multiplier consistent with the stated tier (Verifier C rule 3) | A4 1.0, B2 1.0 (📄 Reg 30 filings); C1, C2, H2 and R1 at 0.7 | PASS (observation O5) |
| 15 | Adjusted total arithmetic | 1.0 + 1.0 + 0.7 + 0.7 + 1.4 + 0.7 = 5.5 | PASS |
| 16 | Classification band (<12 = NO MEANINGFUL EMERGING MOAT) | 5.5, NONE | PASS |
| 17 | I1/I2 contribution stated separately (Section 5 ruling) | "I1/I2 contribution: 0.0 of 5.5" | PASS |
| 18 | Category 21, I1: above 0 only if both legs are evidenced and the (b) leg has at least one 📄 (Verifier C rule 8) | Neither leg evidenced, scored 0 | PASS |
| 19 | Category 22, I2: above 0 only if the named sacrifice is specific (Verifier C rule 8) | The sacrifice test is run for each claimed advantage (NVIDIA Elite, Red Hat, ONGC, GeM, HexaData, Zeacloud, NCIIPC). Answer: nothing must be destroyed; scored 0 | PASS |
| 20 | Section 4 (R1): 4A, 4B and 4C | Present. R1 = LM 1 × 0.7 = 0.7. GeM is not counted twice | PASS |
| 21 | Optionality register: four columns, in both report and block, items scored 0 or resting on 🎙️/🔍 | 7 rows in both | PASS |
| 22 | 6A timeline and 6B risks with early warnings | Present | PASS |
| 23 | 6C uses the injected B01 values | Core 59, moats 12 / 2, AVOID, DB2 and DB4 match B01 | PASS |
| 24 | 6D combined classification, with full reasoning on the HIGH POTENTIAL and TURNAROUND rows | Both rows reasoned. AVOID follows from the injected Gate 0 AVOID. On the F1-corrected input the label becomes AVERAGE (inherited, not a B07 error) | PASS |
| 25 | 6E output card: evolution map, 12-month catalysts, biggest risk | Present | PASS |
| 26 | YAML block per template; report copy matches the block file | Fields and enums valid. em_classification "NONE"; active_categories empty, which fits 0 Strong or Moderate rows. Report copy and block file match | PASS |

### 3.2 Completionist recount check (F7)

📄-tagged items in B07's own Section 3 tables:
- A4: 2 (ResQ launch; AI supercomputers)
- B2: 4 (Red Hat; ONGC LOR; GeM "📄 statement"; ISO "📄 statement")
- C1: 2 (service charges 2.39%; Army HQ engagement)
- C2: 2 (top-5 41.35% FY23; Info Edge and C-DAC single orders)
- H2: 2 (NVIDIA Elite letter; ResQ on Scality and Veeam)
- Total: 12 items (11 unique, because ResQ appears twice) across 5 categories.

🎙️-tagged items: A4 1, C1 2, C2 3, H2 3 (one in the mixed ResQ/Cato row) = 9. 🔍-tagged items: A4 1.

The B07 recount names 6 items across 3 categories. It drops ISO, both C1 📄 items and both C2 📄 items, and evidence_mix copies the short count. The undercount does not inflate any score, and the guard outcome stays the same (6 categories with evidence, well under 12). The rule asks for a recount of the 📄 items, and the recount line is a block field. It should match the tables.

### 3.3 Observations (no fail)

- O5, multiplier approach. H2 takes 0.7 because the load-bearing benefit is 🎙️, although the tier letter is 📄. A4 takes 1.0 on 📄 launches, and its R&D-light leg rests on AR p.72 (R&D blank) plus AUG26 p.11 (🎙️). The shared-architecture leg is 🔍. 1.0 is defensible, but it is a more generous standard than the one H2 used. On the H2 standard, A4 is 0.7 and the total is 5.2. The class stays NONE.
- O6, one fact in two tables. ResQ appears in A4 (launch) and in H2 (partner software). The H2 score (MM) rests on the NVIDIA tier, so no score is double-credited.
- O7, FAT basis. B07 2C uses 48.4x on average tangible net block (AR p.132). B01 M3 uses 19.3x on screener net block. The two stages use different FAT bases. 2C has NIL committed capex, so there is no effect.

## 4. Valuation (B10, B11): PENDING PHASE 3

Not run. B10 and B11 are not among the phase-1 inputs, and the valuation framework docs were not loaded. Rules 4, 5, 7 and 11 to 15 (growth symmetry, pillar mechanics, method plurality, v3.8 exit construction, A19 FV path, expectation ledger, ledger gates, skill-to-source fidelity) run at /finalize step 5. Rule 6 (B09 downstream candidates and stage 11 catalyst citations) runs with them. Rule 9 (narrative) and rule 10 (B09b dossier) fire at /finalize.

## 5. Findings

| ID | Severity | Location | Claimed | Recomputed / rule truth | Note |
|---|---|---|---|---|---|
| F1 | CRITICAL | B01 line 3; B01-gate0.yaml data_years, fy_range, history_downgrade, classification; inherited by B07 6C, 6D and combined_assessment | 4 years (FY2023 to FY2026); LIMITED; downgrade; AVOID | 6 years (FY2021 to FY2026); "5-6 lower, flag"; no downgrade; core 60; AVERAGE (DB4 cap). C2 and C4 N/M with loss-to-profit swing FY21 to FY22. B07 combined AVOID becomes AVERAGE | Rule 6 "maximum whatever exists". FY21 and FY22 restated statements are in PROSP p.48, p.50 and p.51, a document B01 itself cites. Flips the Gate 0 decision line. FLAG-GATE0 stays raised |
| F2 | MINOR | B01 section 2; data_notes item 5 | FY23 ROE on closing net worth, "opening NOT FOUND" | Opening 250.45 Lakhs exists (PROSP p.48). FY23 ROE 75.3% on average. A3 median 20.3%, score 5 unchanged | Same root cause as F1. NOT FOUND applied to a number that exists |
| F3 | MINOR | B01 M8 | 0 ("reach not quantified; NOT FOUND") | 1 ("mentioned unquantified"): AR FY26 p.29 names Bengaluru, Chennai and Hyderabad operations | Moat score +1. Not a present moat |
| F4 | MINOR | B01 M11 | 1 ("rising since FY24") | 3: overall trend 4.81% to 4.27% (screener-data, Selling and admin / Sales), CAGR 55.3% | Rule says "on the overall trend". moats_confirmed 2 becomes 3. Class stays MODERATE. moat_score 15 with F3 |
| F5 | MINOR | 01-gate0.md embedded YAML vs B01-gate0.yaml | data_notes as a string pointer; shorter analyst_note | Template needs a data_notes list and one identical block | Two copies of the block disagree |
| F6 | MINOR | B01 D4 and FLAG-SOURCE-CONFLICT reason | Sensitivity not stated | Results-filing basis: 11,184.86 / 4,909.96 Lakhs = 2.28, D4 = 5. In the 4-year frame, core 60 gives AVERAGE after the downgrade | The flag says the gap decides debtor days. It also decides D4 and, in B01's frame, the classification. Outside the rule rows |
| F7 | MINOR | B07 Section 3 recount line; evidence_mix | 6 📄 items across 3 categories; mix {6, 5, 1} | 12 📄 items (11 unique) across 5 categories; mix {12, 9, 1} | Score and guard unaffected. Recount must match the tables |

Counts: CRITICAL 1, MAJOR 0, MINOR 6. Acceptance rate: 66 of 72 rules = 91.7%. The denominator is at least 4, so the rate applies.

## 6. B12c block (phase 1)

```yaml
stage: B12c
company: "ESCONET"
run_date: "2026-10-05"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete          # phase-1 scope complete; valuation half PENDING PHASE 3
scope: "PHASE 1: Gate 0 (B01) + Emerging Moat (B07) only; valuation audit (B10/B11) PENDING PHASE 3"
gate0:
  rules_checked: 46
  rules_passed: 41
  fails:
    - {id: "F1", rule: "01 rule 6 history window + data-confidence table", severity: "CRITICAL", b01: "data_years 4 (FY2023-FY2026), LIMITED, history_downgrade true, classification AVOID", recomputed: "data_years 6 (FY2021-FY2026, PROSP p.48/p.50/p.51 restated standalone; no subsidiary before 11 May 2022, PROSP p.199), 5-6 lower flag, no downgrade, blocks A13 B5 C10 D17 E15, core 60, classification AVERAGE (DB4 cap); C2/C4 N/M, loss-to-profit swing FY21 to FY22"}
    - {id: "F2", rule: "01 FORMULA ROE opening net worth", severity: "MINOR", b01: "FY23 ROE on closing net worth, opening NOT FOUND", recomputed: "opening 250.45 Lakhs exists (PROSP p.48); FY23 ROE 75.3%; A3 median 20.3%, score 5 unchanged"}
    - {id: "F3", rule: "01 M8 distribution", severity: "MINOR", b01: "0", recomputed: "1 (mentioned unquantified: AR FY26 p.29 Bengaluru, Chennai, Hyderabad)"}
    - {id: "F4", rule: "01 M11 under 6 years, overall trend", severity: "MINOR", b01: "1", recomputed: "3 (selling and admin % 4.81 FY23 to 4.27 FY26, declining; revenue CAGR 55.3%); moats_confirmed 3, class MODERATE, moat_score 15 with F3"}
    - {id: "F5", rule: "01 OUTPUT YAML template", severity: "MINOR", b01: "report-embedded block has data_notes as a string pointer and a different analyst_note from B01-gate0.yaml", recomputed: "one identical block, data_notes as a list"}
emoat:
  rules_checked: 26
  rules_passed: 25
  fails:
    - {id: "F7", rule: "07 rule 6 completionist recount + evidence_mix", severity: "MINOR", b07: "6 documented items across 3 categories; evidence_mix {documented 6, claim 5, inference 1}", recomputed: "12 documented items (11 unique) across 5 categories (A4, B2, C1, C2, H2); evidence_mix {documented 12, claim 9, inference 1}; em_score 5.5 and class NONE unchanged"}
  inherited_from_gate0: "6C/6D combined_assessment AVOID becomes AVERAGE on the F1-corrected Gate 0 input (not a B07 rule error)"
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3 (B10/B11 not in phase-1 inputs)
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; PENDING PHASE 3
business_understanding_narrative: {checked: null, fails: []}  # rule 9; any fail = REWORK stage 13; PENDING /finalize
recomputed_destination_pe: ""  # PENDING PHASE 3
recomputed_decision: ""        # PENDING PHASE 3
recomputed_gate0_classification: "AVERAGE (B01 states AVOID; see F1)"
recomputed_emoat_combined_assessment: "AVERAGE (B07 states AVOID; inherited from F1)"
findings:
  - {id: "F1", severity: "CRITICAL", location: "B01 data_years/history_downgrade/classification; B07 6C/6D", claimed: "4 years, LIMITED downgrade, AVOID", recomputed: "6 years, no downgrade, core 60, AVERAGE", note: "01 rule 6 'maximum whatever exists'; FY21-FY22 restated statements in PROSP p.48-51; flips the Gate 0 decision line; FLAG-GATE0 stays"}
  - {id: "F2", severity: "MINOR", location: "B01 ROE FY23", claimed: "opening net worth NOT FOUND", recomputed: "250.45 Lakhs (PROSP p.48); FY23 ROE 75.3%; A3 unchanged", note: "same root cause as F1"}
  - {id: "F3", severity: "MINOR", location: "B01 M8", claimed: "0", recomputed: "1", note: "AR FY26 p.29 regional footprint, unquantified"}
  - {id: "F4", severity: "MINOR", location: "B01 M11", claimed: "1", recomputed: "3", note: "rubric scores the overall trend under 6 years; 4.81% to 4.27% declining"}
  - {id: "F5", severity: "MINOR", location: "01-gate0.md YAML vs B01-gate0.yaml", claimed: "data_notes string pointer", recomputed: "data_notes list, identical copies", note: "template compliance"}
  - {id: "F6", severity: "MINOR", location: "B01 D4 / FLAG-SOURCE-CONFLICT", claimed: "sensitivity not stated", recomputed: "results-filing basis current ratio 2.28 (11,184.86 / 4,909.96 Lakhs, results 2026-05-28) scores D4 = 5; in the 4-year frame core 60 gives AVERAGE", note: "disclosure gap; moot once F1 is corrected"}
  - {id: "F7", severity: "MINOR", location: "B07 completionist_recount, evidence_mix", claimed: "6 items, 3 categories; mix 6/5/1", recomputed: "12 items (11 unique), 5 categories; mix 12/9/1", note: "no score or guard change"}
critical_count: 1
major_count: 0
minor_count: 6
acceptance_rate: 91.7           # 66 rules passed / 72 rules checked (gate0 46 + emoat 26), %; phase 1 only
```
