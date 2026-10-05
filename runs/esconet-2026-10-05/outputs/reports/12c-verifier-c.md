# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE), ESCONET, run 2026-10-05, RUN 2 (re-audit)

Model: claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter). Emits: B12c run 2 (partial; Gate 0 and Emerging Moat sections only).

## 0. Scope and inputs

This pass re-audits the re-issued Gate 0 (B01 run 2) and the scoped re-issue of the Emerging Moat scan (B07 run 2). Rules 2, 3 and 8 of the Verifier C section run here. Rule 6 needs B09 and B11, so it is not run. Rules 9 and 10 fire at /finalize. Rules 4, 5, 7 and 11 to 15 are the valuation audit. They are PENDING PHASE 3 and the valuation section below is blank.

Rule sources read (only these two, plus the Verifier C section):
- prompts/12-verifiers-pipeline.md, VERIFIER C section
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- runs/esconet-2026-10-05/outputs/reports/01-gate0.md and outputs/blocks/B01-gate0.yaml (stage 1 run 2)
- runs/esconet-2026-10-05/outputs/reports/07-emoat.md and outputs/blocks/B07-emoat.yaml (stage 7 run 2, scoped)

Prior audit: outputs/reports/12c-verifier-c-run1.md and outputs/blocks/B12c-run1.yaml (my own run 1).

Read for one check each: outputs/reports/07-emoat-run1.md, to confirm that the carried Section 5 scorecard is unchanged and to compare the 6E map.

Source data used for re-derivation (Rs Lakhs unless stated):
- inputs/prospectus/EsconetTechnologies_PROSP.txt: [page 190] and [page 192] (FY23 restated consolidated balance sheet and P&L); [page 215] (FY23 consolidated other expenses); [page 232] and [page 233] (FY21 share capital reconciliation and reserves note); [page 254] (FY21 and FY22 standalone other expenses)
- inputs/annual-report/Annual_Report_2025.txt [page 124] (FY24 other expenses)
- inputs/annual-report/Annual_Report_2026.txt [page 144] (FY25 and FY26 other expenses)
- Run 1 checks of screener-Data_Sheet.csv, AR FY26 [page 132] and results 2026-05-28 [page 14] carry over and were not repeated.

Not read: other verifiers' outputs (12a, 12b, 12d), the valuation framework docs (dead context in phase 1), and maker reasoning outside the reports.

Verifier A owns number fidelity. This report judges rule application. Numbers here that the makers did not use carry an anchor so Verifier A or the operator can check them.

## 1. Summary

| Framework | Rules checked | Pass | Fail | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| Gate 0 (B01 run 2) | 49 | 46 | 3 | 0 | 0 | 3 |
| Emerging Moat (B07 run 2) | 27 | 26 | 1 | 0 | 0 | 1 |
| Valuation (B10, B11) | PENDING PHASE 3 | | | | | |
| Total, phase 1 | 76 | 72 | 4 | 0 | 0 | 4 |

Acceptance rate: 72 of 76 = 94.7%. The denominator is 4 or more, so the rate applies. It is above 60%. There is no CRITICAL finding. B12c triggers no REWORK.

Headline. Run 2 resolves all seven run 1 findings. The CRITICAL F1 is fixed: B01 now scores 6 years (FY2021 to FY2026), applies no history downgrade, and classifies AVERAGE under the DB4 cap. I concur with AVERAGE, and with the B07 combined assessment AVERAGE. The blocks match my run 1 recompute exactly (A 13, B 5, C 10, D 17, E 15, core 60).

Four new MINOR findings. None moves a block score, the Gate 0 classification or the combined assessment.
- N1. M11 at 6 years. The rubric runs the two-window test at 6 years or more. B01 used the "if fewer" fallback and scored 3. Every two-window construction scores 5. Moat score 20, grand total 80, class STRONG unchanged.
- N2. FY21 opening net worth is in the corpus (278.57 Lakhs). B01 marks it NOT FOUND. This is the run 1 F2 defect moved to FY21. My run 1 recompute made the same error. A3 does not change.
- N3. The B01 analyst_note says a FY22 start "drops core to 55". A consistent FY22 to FY26 window gives core 63. The loss-year FY21 start lowers core by 3 on net. It does not lift it. B07 6C copies the claim.
- N4. The B07 6E map shows no existing moat in any family. Its reason is that "B01 does not name which four moats". B01 names them (M1, M4, M10, M11). Run 1 had the same gap and my run 1 audit passed it.

## 2. Run 1 findings: resolution status

| ID | Run 1 severity | Run 1 finding | Run 2 status | Evidence in the re-issued output |
|---|---|---|---|---|
| F1 | CRITICAL | 4 years scored; LIMITED downgrade; AVOID | RESOLVED | B01 line 3: "Data available: 6 years (FY2021 to FY2026)". data_years 6, history_downgrade false, blocks {A 13, B 5, C 10, D 17, E 15}, core 60, classification AVERAGE (DB4). C2 and C4 N/M, "Loss-to-profit swing, FY21 to FY22" in data_notes. B07 6C, 6D and combined_assessment now AVERAGE. Blocks and classification equal my run 1 recompute |
| F2 | MINOR | FY23 ROE on closing net worth, "opening NOT FOUND" | RESOLVED for FY23; same defect recurs at FY21 (N2) | FY23 ROE 304.00 / avg(250.45, 554.19) = 75.6% (B01 section 2) |
| F3 | MINOR | M8 scored 0 | RESOLVED | M8 = 1, AR FY26 [page 29] regional footprint, unquantified |
| F4 | MINOR | M11 scored 1 on a "rising since FY24" sub-window under the fewer-than-6-years fallback | RESOLVED as raised; superseded by N1 | The sub-window reading is gone and the overall trend is used. In the 6-year frame the written rule routes to the two-window test (N1). The run 1 recompute of 3 was right for 4 years only |
| F5 | MINOR | Report-embedded YAML differed from the block file | RESOLVED | 01-gate0.md lines 203 to 271 and B01-gate0.yaml lines 1 to 69 are identical; data_notes is a 24-item list |
| F6 | MINOR | D4 sensitivity to the FY26 source conflict not disclosed | RESOLVED | Section 0 table, D4 row, data_notes item 13, FLAG-SOURCE-CONFLICT reason: 1.85 (score 4) on the AR basis, 2.28 (score 5) on the results basis |
| F7 | MINOR | Recount 6 items across 3 categories; evidence_mix 6/5/1 | RESOLVED | "12 documented items (11 unique) across 5 categories (A4, B2, C1, C2, H2)"; evidence_mix {12, 9, 1}. My recount of the re-issued tables agrees (section 4.2) |

## 3. Gate 0 (B01 run 2) compliance

### 3.1 Rule-by-rule table

All figures Rs Lakhs from the B01 run 2 input table (sources: prospectus [page 48], [page 50], [page 51], [page 190], [page 192], [page 194]; AR FY25 [page 112] to [page 114]; AR FY26 [page 132] to [page 134]) unless an anchor says otherwise.

| # | Rule (source) | B01 value | Verifier re-derivation | Result |
|---|---|---|---|---|
| 1 | Opening line (01 rule 6) | "Data available: 6 years (FY2021 to FY2026). Scoring adapted to 6-year history." (line 3) | Present | PASS |
| 2 | History "maximum whatever exists" plus data-confidence table (01 rule 6; CLASSIFICATION) | 6 years; LOWER; flag; no downgrade | 6 is the maximum. The corpus has no FY2020 P&L or balance sheet; the only FY2020 figure is the PPE schedule "As at April 01, 2020" (PROSP line 14981). Band 5-6 = "lower, flag", no downgrade | PASS (F1 resolved) |
| 3 | ROCE: source figure if given, else compute and state (01 FORMULA) | Computed, stated | Data_Sheet has no ROCE row (run 1 check) | PASS |
| 4 | ROE = PAT / average net worth; closing only if opening is unavailable (01 FORMULA) | FY23 on average (fixed). FY21 on closing, "opening NOT FOUND" | FY21 opening exists: share capital at the start of FY21 76.71 (PROSP [page 232], Note I.1 reconciliation, "Share capital at the beginning of the period", 31 March 2021 column) plus surplus "As per Last Balance Sheet" 201.86 (PROSP [page 233], Note I.2, 31 March 2021 column) = 278.57. Check: 201.86 - 100.48 = 101.38, the FY21 closing surplus. FY21 ROE = -100.48 / ((278.57 + 178.09) / 2) = -100.48 / 228.33 = -44.0%. A3 median stays 20.27%, score 5 | FAIL, MINOR (N2) |
| 5 | WC days formula and basis stated (01 FORMULA) | Revenue basis, stated | Default basis | PASS |
| 6 | FCF = CFO - capex, acquisitions excluded (01 FORMULA) | Applied; FY26 goodwill 851.11 excluded | Applied | PASS |
| 7 | CAGR = (End / Start)^(1/years) - 1 (01 FORMULA) | C1 over 5 years | (35,440.48 / 4,411.89)^(1/5) - 1 = 51.7% | PASS |
| 8 | CAGR edge rules (01) | C2 N/M; C4 0; swing noted in data_notes | Required text present: "Loss-to-profit swing, FY21 to FY22" | PASS |
| 9 | A1 median ROCE (15-19.9 = 3) | 18.2%, 3 | -6.23, 11.96, 16.12, 20.29, 23.30, 60.56; median (16.12 + 20.29) / 2 = 18.21% | PASS |
| 10 | A2 minimum ROCE (<8 = 0) | -6.23%, 0 | FY21 EBIT -32.49 / CE 521.88 | PASS |
| 11 | A3 median ROE (≥20 = 5) | 20.27%, 5 | (14.95 + 25.59) / 2 = 20.27%. Same with N2 corrected, because FY21 is the lowest value on either basis | PASS |
| 12 | A4 ROCE trend, latest vs earliest | 5 | 11.96% ≥ -6.23%. Rule applied as written; FY22 sensitivity disclosed | PASS |
| 13 | B1 cumulative CFO / PAT | -0.36, 0 | -798.86 / 2,234.14 = -0.358 | PASS |
| 14 | B2 FCF-positive years | 0 of 6, 0 | -80.49, -71.63, -158.11, -346.92, -162.94, -1,679.63 | PASS |
| 15 | B3 cumulative FCF / PAT | Negative, 0 | -2,499.72 / 2,234.14 | PASS |
| 16 | B4 change in WC days (decreased >5 = 5) | -5.3, 5 | FY21 71.59 + 48.50 - 72.45 = 47.64; FY26 45.59 + 53.04 - 56.31 = 42.32; change -5.32 | PASS |
| 17 | C1 revenue CAGR | 51.7%, 5 | Confirmed | PASS |
| 18 | C2 PAT CAGR | N/M, 0 | FY21 PAT -100.48 is a negative endpoint | PASS |
| 19 | C3 positive YoY revenue years | 5 of 5, 5 | Every year rises, also with FY23 standalone 9,465.96 | PASS |
| 20 | C4 | 0, PAT CAGR N/M | 01 edge rule | PASS |
| 21 | D1 net debt / EBITDA | Net cash, 5 | 1,324.33 - 2,737.70 = -1,413.37 | PASS |
| 22 | D2 EBIT / interest (5-9.9 = 4) | 8.3x, 4 | 979.93 / 118.13 = 8.30x | PASS |
| 23 | D3 debt / equity (0.1-0.5 = 4) | 0.17, 4 | 1,324.33 / 8,019.19 = 0.165; ex warrant money 184.23 it is 0.169; same band | PASS |
| 24 | D4 current ratio (1.5-1.99 = 4) | 1.85, 4 | 13,647.86 / 7,372.96 (AR FY26 [page 132]) | PASS |
| 25 | E1 promoter holding | 60.19%, 5 | ≥60 = 5 | PASS |
| 26 | E2 change over 3 years | -4.75pp, 0 | Window is 2.4 years since IPO. A full 3-year window starts before the IPO, at a higher holding (Santosh Agrawal 50.20% plus Sunil Agrawal 36.63% at 31 March 2023, PROSP [page 232]), and also scores 0 | PASS |
| 27 | E3 pledge | 0%, 5 | Confirmed | PASS |
| 28 | E4 contingent liabilities / net worth | 0%, 5 | AR FY26 [page 145]; commitments outside the formula | PASS |
| 29 | Block sums and core | 13 + 5 + 10 + 17 + 15 = 60 | Confirmed | PASS |
| 30 | M1 pricing power (≥2pp AND CAGR ≥10% = 5) | +2.42pp, 5 | 3.03 / 4,411.89 = 0.07% to 881.61 / 35,440.48 = 2.49%; +2.42pp; CAGR 51.7%. Endpoint sensitivity disclosed | PASS |
| 31 | M2 cost advantage | 2.49% vs 4.99%, 0 | Below; also below the 7.99% median without Orient | PASS |
| 32 | M3 capital efficiency | 0 | FY26 ROCE 11.96% is not above 12% on either FAT basis (observation O3) | PASS |
| 33 | M4 customer stickiness | 3 | Zero decline years; receivable days 71.6 to 45.6 (-26.0) is outside ±10; the "max 1 decline year" band gives 3 | PASS |
| 34 | M5 scale | 0, PEER DATA NEEDED | Segment universe incomplete; applied as written | PASS |
| 35 | M6 R&D | 0, NOT FOUND | AR R&D row blank; the 1-band also fails on margin | PASS |
| 36 | M7 regulatory | 0 | Unregulated | PASS |
| 37 | M8 distribution ("mentioned unquantified = 1") | 1 | AR FY26 [page 29] | PASS (F3 resolved) |
| 38 | M9 brand | 0 | GM proxy 10.9% vs peer median 21.0% | PASS |
| 39 | M10 switching costs | 5 | Revenue grew 5 of 5 years; receivable days fell, so "rose ≤10" holds | PASS |
| 40 | M11 network effects ("needs ≥6 years for the two-window test; if fewer, score conservatively on the overall trend") | 3, fallback path: "prior 3-year window ... needs FY20, NOT FOUND" | 6 years meets the stated threshold, so the fallback ("if fewer") does not apply. Every two-window construction 6 years allow gives 5 (section 3.2) | FAIL, MINOR (N1) |
| 41 | M12 negative WC (15-45 = 1; >45 = 0) | Median 44.98, 1 | Sorted 36.02, 37.66, 42.32, 47.64, 47.80, 58.45; median (42.32 + 47.64) / 2 = 44.98. FY23 inputs tie to PROSP [page 190] and [page 192]. The rubric names no statistic; median accepted as in run 1 (observation O4) | PASS |
| 42 | Moat count and class (4-5 = STRONG) | 4 present (M1, M4, M10, M11), STRONG, 18 | Confirmed on B01's scores. With N1: 4 present, STRONG, moat score 20 | PASS |
| 43 | Classification matrix | Core 60 + STRONG = GOOD+ pre-cap | Core 60-79 + STRONG = GOOD+ | PASS |
| 44 | Deal-breakers, with driving years | DB2 (max GOOD), DB4 (max AVERAGE, binds); others named as not triggered | Confirmed. DB8 not triggered: PAT positive FY24 to FY26 | PASS |
| 45 | FLAG-GATE0 (classification ≤ AVERAGE with depressors) | Raised | Required at AVERAGE | PASS |
| 46 | YAML per the 01 template; one identical block | Report copy and block file identical, 69 lines; data_notes a list; extra key "run: 2" | Template fields all present; the extra key is the run convention | PASS (F5 resolved) |
| 47 | Data-confidence flag for 5-6 years ("may not have seen full cycle") | Report line 5; data_notes item 1 | Present | PASS |
| 48 | FY26 source-conflict sensitivity stated for each score it moves | D4 4 vs 5; core 60 vs 61; ROCE, WC days, D1 to D3 unchanged | Disclosed in section 0, D4 row, data_notes and FLAG-SOURCE-CONFLICT | PASS (F6 resolved) |
| 49 | Sensitivity statements match what the scoring rules give (01 rule 2 "only numbers and the scoring rules"; 01 rule 3; analyst_note purpose) | analyst_note: "Several scores rest on loss-year FY21 endpoints: A4 (5), M1 (5), B4 (5). Moving the start to FY22 drops core to 55 and cuts M1 to 3." | A consistent FY22 to FY26 window gives core 63 (A 10, B 1, C 20, D 17, E 15), moat 16, 4 present, STRONG, total 79, AVERAGE (DB4 -0.33). Core 55 is the A4-only swap. The note names the FY21 endpoints that lift the score and omits the ones that cut it (C2, C4, A1, A2) (section 3.4) | FAIL, MINOR (N3) |

### 3.2 N1: M11 at exactly 6 years

Rule text (prompts/01, M11): "needs ≥6 years for the two-window test; if fewer, score conservatively on the overall trend and state so". The bands: "latest 3yr rev CAGR > prior 3yr AND selling exp % declining = 5 | rev CAGR ≥20% AND selling % stable/declining = 3".

B01 has 6 years. The written threshold is met, so the fallback is not the written path. B01 says the prior window "needs FY20". That substitutes a 7-point data requirement for the rubric's own 6-year threshold. The rubric's count only works if each window is three fiscal years of data.

Two-window recompute. Selling proxy per B01 (advertisement, sales and marketing, sales promotion, commission, freight outward). I tied every sum to source:
- FY21 47.71 + 52.22 + 10.13 = 110.06 and FY22 71.98 + 117.51 + 16.90 = 206.39 (PROSP [page 254], standalone Note II.7)
- FY23 102.88 + 124.69 + 21.67 = 249.24 (PROSP [page 215], consolidated Note II.7)
- FY24 10.99 + 49.03 + 40.80 + 32.85 + 149.08 = 282.75 (AR FY25 [page 124], Note 2.23)
- FY25 3.84 + 36.45 + 47.20 + 57.14 + 333.04 = 477.67 and FY26 24.58 + 85.37 + 64.44 + 44.26 + 484.35 = 703.00 (AR FY26 [page 144], Note 2.23)

| Construction | Prior window revenue CAGR | Latest window revenue CAGR | Selling % | Score |
|---|---|---|---|---|
| (a) Three-year blocks: FY21-FY23 vs FY24-FY26 | (9,659.26 / 4,411.89)^(1/2) - 1 = 48.0% | (35,440.48 / 14,054.99)^(1/2) - 1 = 58.8% | Block means 2.69% to 2.02%, declining | 5 |
| (b) B01's adapted reading: FY21-FY23 vs FY23-FY26 | 48.0% | (35,440.48 / 9,659.26)^(1/3) - 1 = 54.2% | 2.49% (FY21) to 1.98% (FY26), declining | 5 |

Recomputed M11 = 5. Moat score 18 becomes 20 and grand total 78 becomes 80. moats_confirmed stays 4 (M11 is already present at 3). Class STRONG and classification AVERAGE do not change. B01 disclosed the score-5 reading in its sensitivities, so this is a path error, not a hidden one. The rubric text has a real gap (observation O2), and B01 called its choice "literal". Severity MINOR.

### 3.3 N2: FY21 opening net worth

The 01 ROE rule allows closing net worth "if opening net worth unavailable for the earliest year". It is available:
- Share capital at the beginning of FY21: 7,67,100 shares, 76.71 (PROSP [page 232], Note I.1 reconciliation).
- Surplus "As per Last Balance Sheet" for the year ended 31 March 2021: 201.86 (PROSP [page 233], Note I.2). Securities premium opening: nil.
- Opening net worth 278.57. FY21 ROE -44.0% on the average, not -56.4% on closing.

The B01 input_gaps line "FY21 opening net worth NOT FOUND" and data_notes item 8 should change. A3 does not move, because FY21 is the lowest ROE on either basis and the median sits on FY24 and FY25. Severity MINOR. Disclosure: my run 1 recompute (12c run 1, section 2.2) also wrote "opening NOT FOUND in the corpus" for FY21. B01 run 2 followed that text. The error is shared.

### 3.4 N3: the FY22-start sensitivity

The analyst_note says the FY21 loss-year start props up A4, M1 and B4, and that a FY22 start "drops core to 55". The robustness paragraph (01-gate0.md line 185) is accurate. It labels each swap as single-metric: "A4 against FY22 gives core 55", "B4 against FY22 gives core 56". The analyst_note drops that label, and B07 6C repeats the claim as a whole-window statement: "Starting at FY22 drops core to 55".

Consistent FY22 to FY26 window, same inputs, same rules:

| Item | FY22 to FY26 value | Score | FY21 start score |
|---|---|---|---|
| A1 median ROCE | 11.96, 16.12, 20.29, 23.30, 60.56; median 20.29% | 4 | 3 |
| A2 minimum ROCE | 11.96% (continuous reading; observation O1) | 1 | 0 |
| A3 median ROE | 8.19, 14.95, 25.59, 33.77, 75.56; median 25.59% | 5 | 5 |
| A4 | 11.96% vs 20.29%, decline 8.3pp | 0 | 5 |
| Block A | | 10 | 13 |
| B1 | CFO -776.73 / PAT 2,334.62 = -0.33 | 0 | 0 |
| B2, B3 | 0 of 5 FCF-positive; cumulative FCF -2,419.23 | 0, 0 | 0, 0 |
| B4 | 36.02 to 42.32 = +6.30 days | 1 | 5 |
| Block B | | 1 | 5 |
| C1 | (35,440.48 / 6,856.29)^(1/4) - 1 = 50.8% | 5 | 5 |
| C2 | (615.50 / 72.36)^(1/4) - 1 = 70.8% | 5 | 0 (N/M) |
| C3 | 4 of 4 | 5 | 5 |
| C4 | 70.8 - 50.8 = +20.0pp | 5 | 0 |
| Block C | | 20 | 10 |
| Blocks D, E | Latest-year tests | 17, 15 | 17, 15 |
| Core | | 63 | 60 |
| Moat | M1 3 (2.91% to 2.49%, stable), M4 3, M8 1, M10 5, M11 3 (5 years, fallback), M12 1 (median 42.32) | 16, STRONG | 18, STRONG |
| Classification | GOOD+ pre-cap; DB2 (B 1); DB4 (-0.33) | AVERAGE | AVERAGE |

On net the FY21 start lowers core by 3 points: it adds 9 (A4 +5, B4 +4) and removes 12 (C2 -5, C4 -5, A1 -1, A2 -1). The note shows only the adds. CLAUDE.md sets the same bar for bull and bear claims, and this note shows one side. The classification is AVERAGE on both windows, so the decision survives. The risk is downstream: the Halt 1 dossier or stage 13 may repeat "FY22 start gives 55". Severity MINOR. Fix: replace the sentence with the single-metric labels from line 185, or with the consistent-window result (core 63, AVERAGE).

### 3.5 Observations (no fail)

- O1, A2 rubric gap (carried). Bands "12-14.9 = 3" and "8-11.9 = 1" leave 11.91 to 11.99 unassigned. It does not bite on the 6-year frame (minimum -6.23%). It does bite in any FY22-start view (11.96%). Fix belongs in prompts/01 by operator ruling.
- O2, M11 window definition. The rubric says 6 years enable the two-window test but writes "3yr rev CAGR" per window. On an interval reading that needs 7 data points. prompts/01 should define the windows (for example FY(n-5) to FY(n-3) vs FY(n-2) to FY(n), or 3-interval windows with ≥7 years). Both available constructions give 5 for ESCONET, so the outcome does not depend on the ruling.
- O3, M3 ROCE year (carried). The rubric does not say latest or median. On the median (18.2%) M3 is 3, and moats present become 5 (still STRONG). B01 disclosed this.
- O4, M12 boundary. The median 44.98 sits 0.02 day under the 45 line. Run 1 used screener FY23 (WC 42.83 days) and got a median of 45.2 (score 0). Run 2 uses restated consolidated FY23 (WC 37.66 days; receivables 1,146.16, inventory 856.96, payables 1,006.32, revenue 9,659.26; PROSP [page 190], [page 192]), which gives a score of 1. The basis choice is sound: screener FY23 ties to neither restated set, and consolidated FY23 matches the FY24 to FY26 basis. B01 disclosed the neighbouring reading. Moat score 18 vs 17; no class change.
- O5, selling-proxy scope. The FY24 to FY26 AR note carries "Conference & Exhibition" (FY24 40.67, FY25 54.77, FY26 41.20; AR FY25 [page 124], AR FY26 [page 144]), which B01 excludes. Including it gives 2.30%, 2.31%, 2.10%. That is still below FY21 2.49% and the prior-window mean 2.69%. No score changes. The B01 label "freight outward" maps to the AR line "Freight Charges".

## 4. Emerging Moat (B07 run 2) compliance

### 4.1 Rule-by-rule table

| # | Rule (source) | B07 run 2 | Result |
|---|---|---|---|
| 1 | All six sections plus the optionality register (07 rule 1) | Present; Section 0 is extra | PASS |
| 2 | Evidence tag on every item (07 rule 2) | Every Section 3 table row tagged | PASS |
| 3 | Source anchor on every item (07 rule 3) | Anchored; the 🔍 chassis row says "none filed" | PASS |
| 4 | Section 1: 1A, 1B, 1C | Present, NOT FOUND where missing | PASS |
| 5 | Section 2: 2A, 2B, 2D | Present | PASS |
| 6 | 2C: capex under execution × FAT, arithmetic shown | NIL committed (AR p.117, p.145); the 450 × 48.4x test is shown and rejected with a reason | PASS |
| 7 | All 22 categories plus R1, or NO EVIDENCE FOUND (Verifier C rule 3) | 23 rows in Section 3, the summary table and Section 5 | PASS |
| 8 | No force-fit (07 rule 5) | 17 rows NO EVIDENCE FOUND; F2 and G2 cite counter-evidence | PASS |
| 9 | Summary table: evidence, type, strength, time | All 23 rows | PASS |
| 10 | Strong or Moderate count stated | 0; Weak 6 | PASS |
| 11 | Completionist recount present and accurate; evidence_mix item counts (07 rule 6) | "12 documented items (11 unique) across 5 categories (A4, B2, C1, C2, H2)"; mix {12, 9, 1} | PASS (F7 resolved; section 4.2) |
| 12 | Guard: 12 or more active categories means re-examine | 6 rows carry evidence | PASS |
| 13 | Matrix values (HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1, LL 1) | ML 1, LL 1, MM 2, LM 1 | PASS |
| 14 | Multiplier consistent with the stated tier (Verifier C rule 3) | A4 1.0, B2 1.0; C1, C2, H2, R1 0.7. No 🎙️-only row takes 1.0. C1 and C2 now show 📄 items but stay at 0.7, which is under the tier, not over it | PASS (observation O6) |
| 15 | Adjusted total | 1.0 + 1.0 + 0.7 + 0.7 + 1.4 + 0.7 = 5.5 | PASS |
| 16 | Band (<12 = NO MEANINGFUL EMERGING MOAT) | 5.5, NONE | PASS |
| 17 | I1/I2 contribution stated separately (Section 5 ruling) | "I1/I2 contribution: 0.0 of 5.5" | PASS |
| 18 | Category 21 (Verifier C rule 8) | Neither leg evidenced; 0 | PASS |
| 19 | Category 22 (Verifier C rule 8) | Sacrifice test run per claimed advantage; "nothing must be destroyed"; 0 | PASS |
| 20 | Section 4 (R1): 4A, 4B, 4C | Present; GeM not counted twice | PASS |
| 21 | Optionality register: four columns, report and block | 7 rows in both | PASS |
| 22 | 6A timeline, 6B risks | Present | PASS |
| 23 | 6C uses the injected B01 values | Core 60, blocks 13/5/10/17/15, moat 18 / 4 STRONG, total 78, AVERAGE, DB2 and DB4, no downgrade: all match B01 run 2. The sentence "Starting at FY22 drops core to 55" is carried from the B01 analyst_note (N3, inherited, not a B07 rule error) | PASS |
| 24 | 6D combined classification; full reasoning on HIGH POTENTIAL and TURNAROUND | AVERAGE; both rows reasoned on the run 2 Gate 0 | PASS |
| 25 | 6E output card: moat evolution map (existing to emerging per family), 12-month catalysts, biggest risk | Catalysts and risk present. Existing column is "none" in every family. Stated reason: "B01 does not name which four moats" | FAIL, MINOR (N4) |
| 26 | YAML per template; report copy equals block file | 07-emoat.md lines 375 to 432 equal B07-emoat.yaml lines 1 to 58; all template fields present; extra key "run: 2"; analyst_note about 150 words | PASS |
| 27 | Scoped re-issue discipline | Section 5 rows equal 07-emoat-run1.md lines 251 to 271 (A4 1.0, B2 1.0, C1 0.7, C2 0.7, H2 1.4, R1 0.7, total 5.5). Run 1 Gate 0 phrasing in Section 0.2 and G1 is labelled as run 1, and input_gaps says so | PASS |

### 4.2 Recount verification (F7)

My count of the 📄 rows in the re-issued Section 3 tables:
- A4: 2 (ResQ launch; AI supercomputers)
- B2: 4 (Red Hat; ONGC LOR; GeM "📄 statement"; ISO "📄 statement")
- C1: 2 (service charges 2.39%; Army HQ engagement)
- C2: 2 (top-5 41.35% FY23; Info Edge and C-DAC single orders)
- H2: 2 (NVIDIA Elite letter; ResQ on Scality and Veeam)
- Total 12 across 5 categories, 11 unique.

🎙️: A4 1, C1 2, C2 3, H2 3 = 9. 🔍: A4 1. This matches B07's line and evidence_mix. B07 excludes the R1 claims in Section 4 from the mix and says so. That matches the scope of my run 1 recompute.

### 4.3 N4: 6E existing column

The 07 spec asks for "the moat evolution map (existing → emerging per family)". B07 run 2 keeps the run 1 existing column ("none" in all ten rows). Its reason: "B01 does not name which four moats, so the family-level existing column stays at the run 1 reading". That premise is false:
- 01-gate0.md line 162: "Moats present (score 3 or more): M1, M4, M10, M11 = 4."
- The injected B01 block itself scores each one in data_notes: M1 "scores 5", M4 "scores 3", M10 "scores 5", M11 "(3)".

Recomputed map, existing side:
- C Customer: existing M4 customer stickiness (3) and M10 switching costs (5), both receivable-day and revenue-growth proxies, to emerging Weak.
- M1 pricing power (5, an endpoint artefact of the FY21 loss year) and M11 network effects (3, or 5 under N1) have no clean family home in the 07 taxonomy. They should be listed beside the map as existing quantitative moats.
- The emerging side does not change.

No score, class or combined assessment changes. Severity MINOR. Disclosure: run 1 had the same gap. B01 run 1 confirmed M4 (5) and M10 (5), while 07-emoat-run1.md line 332 read "C Customer: none to Weak", and my run 1 audit passed rule 25. That was a miss on my side.

### 4.4 Observations (no fail)

- O6, multiplier approach (carried as run 1 O5). B07 now states the rule it applies: score on the load-bearing leg. H2 takes 0.7 because its benefit leg is 🎙️. A4 takes 1.0 on the 📄 launches, but its platform leg (shared chassis) is 🔍 and its low-R&D leg is 🎙️. On the H2 standard, A4 is 0.7 and the total is 5.2. Class NONE either way.
- O7, undefined threshold. completionist_recount says "none reaches Moderate (adjusted 2.0)". prompts/07 defines no numeric mapping from adjusted score to the Strong / Moderate / Weak labels. No effect on any score.
- O8, FAT basis (carried). B07 2C uses 48.4x on average PP&E; B01 M3 uses 35.8x on FY26 PP&E or 19.3x on screener net block. 2C has NIL committed capex, so there is no effect.

## 5. Valuation (B10, B11): PENDING PHASE 3

Not run, left blank. B10 and B11 are not phase 1 inputs, and the valuation framework docs were not loaded. Rules 4, 5, 7 and 11 to 15 run at /finalize step 5. Rule 6 runs with them. Rules 9 and 10 fire at /finalize.

## 6. Findings

| ID | Severity | Location | Claimed | Recomputed / rule truth | Note |
|---|---|---|---|---|---|
| N1 | MINOR | B01 M11; moat_score; grand_total | 3 on the "if fewer than 6 years" fallback | 5: 6 years meets the stated two-window threshold. FY21-FY23 48.0% vs FY24-FY26 58.8% (or FY23-FY26 54.2%), selling proxy 2.69% to 2.02% block means. Moat score 20, grand total 80, 4 present, STRONG | Classification AVERAGE unchanged. Rubric gap O2 for operator ruling |
| N2 | MINOR | B01 ROE FY21; input_gaps; data_notes item 8 | FY21 opening net worth NOT FOUND; ROE -56.4% on closing | Opening 278.57 = 76.71 (PROSP [page 232]) + 201.86 (PROSP [page 233]); ROE -44.0% | A3 median 20.27%, score 5 unchanged. Same class as run 1 F2; my run 1 recompute shared the error |
| N3 | MINOR | B01 analyst_note; inherited by B07 6C | FY22 start "drops core to 55" | Consistent FY22 to FY26 window: core 63 (A 10, B 1, C 20, D 17, E 15), moat 16 STRONG, AVERAGE. 55 is the A4-only swap. On net, the FY21 start costs 3 points | One-sided sensitivity. Decision unchanged. Fix before the Halt 1 dossier quotes it |
| N4 | MINOR | B07 6E moat evolution map; input_gaps last line | Existing "none" in every family; "B01 does not name which four moats" | B01 names M1, M4, M10, M11 (line 162; block data_notes). C Customer existing = M4 (3) and M10 (5); M1 and M11 listed beside the map | Run 1 had the same gap; my run 1 audit missed it |

Run 1 findings F1 to F7: all RESOLVED (F4 superseded by N1 in the 6-year frame; F2 recurs at FY21 as N2).

Counts: CRITICAL 0, MAJOR 0, MINOR 4. Acceptance rate 72 of 76 = 94.7%. No REWORK trigger from B12c.

## 7. B12c block (phase 1, run 2)

```yaml
stage: B12c
run: 2
company: "ESCONET"
run_date: "2026-10-05"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete          # phase-1 re-audit complete; valuation half PENDING PHASE 3
scope: "PHASE 1 RE-AUDIT: Gate 0 (B01 run 2) + Emerging Moat (B07 run 2, scoped) only; valuation audit (B10/B11) PENDING PHASE 3"
run1_findings:
  - {id: "F1", run1_severity: "CRITICAL", status: "RESOLVED", evidence: "B01 data_years 6 (FY2021-FY2026), history_downgrade false, blocks A13 B5 C10 D17 E15, core 60, AVERAGE (DB4); C2/C4 N/M with loss-to-profit swing FY21 to FY22; B07 6C/6D/combined_assessment AVERAGE"}
  - {id: "F2", run1_severity: "MINOR", status: "RESOLVED for FY23; recurs at FY21 as N2", evidence: "FY23 ROE 304.00 / avg(250.45, 554.19) = 75.6%"}
  - {id: "F3", run1_severity: "MINOR", status: "RESOLVED", evidence: "M8 = 1 (AR FY26 [page 29])"}
  - {id: "F4", run1_severity: "MINOR", status: "RESOLVED as raised; superseded by N1", evidence: "sub-window reading removed; overall trend used; at 6 years the written path is the two-window test"}
  - {id: "F5", run1_severity: "MINOR", status: "RESOLVED", evidence: "01-gate0.md lines 203-271 identical to B01-gate0.yaml; data_notes 24-item list"}
  - {id: "F6", run1_severity: "MINOR", status: "RESOLVED", evidence: "D4 1.85 (4) AR basis vs 2.28 (5) results basis disclosed in section 0, D4 row, data_notes, FLAG-SOURCE-CONFLICT"}
  - {id: "F7", run1_severity: "MINOR", status: "RESOLVED", evidence: "12 documented items (11 unique) across 5 categories; evidence_mix 12/9/1; verifier recount agrees"}
gate0:
  rules_checked: 49
  rules_passed: 46
  fails:
    - {id: "N1", rule: "01 M11 two-window test at >=6 years", severity: "MINOR", b01: "3 (overall-trend fallback; 'prior window needs FY20')", recomputed: "5 (FY21-FY23 48.0% vs FY24-FY26 58.8%, or FY23-FY26 54.2%; selling proxy block means 2.69% to 2.02%); moat_score 20, grand_total 80, moats_confirmed 4, STRONG; classification AVERAGE unchanged"}
    - {id: "N2", rule: "01 FORMULA ROE opening net worth (earliest year)", severity: "MINOR", b01: "FY21 opening net worth NOT FOUND; ROE -56.4% on closing", recomputed: "opening 278.57 Lakhs = share capital 76.71 (PROSP [page 232]) + opening surplus 201.86 (PROSP [page 233]); FY21 ROE -44.0%; A3 median 20.27%, score 5 unchanged"}
    - {id: "N3", rule: "01 rules 2-3 and analyst_note purpose: sensitivity must match the scoring rules", severity: "MINOR", b01: "analyst_note: FY22 start drops core to 55", recomputed: "consistent FY22-FY26 window: A10 B1 C20 D17 E15 = core 63, moat 16 STRONG, AVERAGE (DB4 -0.33); 55 is the A4-only swap; FY21 start costs 3 points net"}
emoat:
  rules_checked: 27
  rules_passed: 26
  fails:
    - {id: "N4", rule: "07 Section 6E moat evolution map existing to emerging per family", severity: "MINOR", b07: "existing column none in all families; 'B01 does not name which four moats'", recomputed: "B01 names M1, M4, M10, M11 (01-gate0.md line 162; B01 data_notes); C Customer existing = M4 (3) + M10 (5); M1 (5) and M11 (3, or 5 per N1) listed beside the map; emerging side unchanged"}
  inherited_from_gate0: "6C sentence 'Starting at FY22 drops core to 55' carried from B01 analyst_note (N3); not a B07 rule error"
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3 (B10/B11 not in phase-1 inputs)
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; PENDING PHASE 3
business_understanding_narrative: {checked: null, fails: []}  # rule 9; any fail = REWORK stage 13; PENDING /finalize
recomputed_destination_pe: ""  # PENDING PHASE 3
recomputed_decision: ""        # PENDING PHASE 3
recomputed_gate0_classification: ""  # concur: AVERAGE
recomputed_gate0_moat: "moat_score 20, grand_total 80, moats_confirmed 4, STRONG (N1); B01 states 18 / 78 / 4 / STRONG"
recomputed_emoat_combined_assessment: ""  # concur: AVERAGE
findings:
  - {id: "N1", severity: "MINOR", location: "B01 M11, moat_score, grand_total", claimed: "3", recomputed: "5; moat_score 20; grand_total 80", note: "6 years meets the rubric's two-window threshold; fallback is 'if fewer'; rubric window definition needs an operator ruling (O2); classification unchanged"}
  - {id: "N2", severity: "MINOR", location: "B01 ROE FY21, input_gaps, data_notes", claimed: "opening net worth NOT FOUND", recomputed: "278.57 Lakhs (PROSP [page 232] + [page 233]); ROE -44.0%; A3 unchanged", note: "same class as run 1 F2; verifier run 1 recompute shared the error"}
  - {id: "N3", severity: "MINOR", location: "B01 analyst_note; B07 6C (inherited)", claimed: "FY22 start gives core 55", recomputed: "consistent FY22 window gives core 63, AVERAGE", note: "one-sided sensitivity; correct it before the Halt 1 dossier or stage 13 quotes it"}
  - {id: "N4", severity: "MINOR", location: "B07 6E moat evolution map", claimed: "existing none in all families; B01 does not name the four moats", recomputed: "C Customer existing M4 (3) + M10 (5); M1 and M11 listed", note: "premise false; run 1 had the same gap and the run 1 audit missed it"}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 94.7           # 72 rules passed / 76 rules checked (gate0 49 + emoat 27), %; phase 1 only
rework_trigger: false           # no CRITICAL; rate above 60% on a denominator of 76
```
