# STAGE 12C: VERIFIER C, FRAMEWORK ADHERENCE (PHASE 1)
Company: INA (Insolation Energy Ltd) | Run date: 2026-09-06 | Model: claude-opus-4-8

## SCOPE OF THIS PASS

This is PHASE 1. Two artifacts are audited:

- B01 Gate 0, against prompts/01-gate-0-pipeline.md
- B07 Emerging Moat, against prompts/07-emerging-moat-pipeline.md

Stage 10 and stage 11 have not run. B10 and B11 do not exist. The valuation
adherence audit (verifier C rules 4, 7, 11, 12) is DEFERRED TO PHASE 3. The
valuation framework documents were not loaded, per the phase-1 scope rule in
prompts/12-verifiers-pipeline.md.

The framework_adherence figure below covers Gate 0 and Emerging Moat ONLY. It
is not a whole-pipeline score. The valuation portion is pending phase 3 and
carries no number yet.

Two further scope limits bind this report:

1. Source fidelity is verifier A's exclusive authority. Where a re-derivation
   of mine depends on whether a figure actually appears in a source document at
   its cited anchor, I say so and I do not rule on the figure. I re-derive from
   the stage's own stated inputs and I check rule application only.
2. I do not assess company quality. A low score correctly derived is a PASS.

---

# PART 1: GATE 0 (B01) COMPLIANCE

Artifacts: runs/ina-2026-09-06/outputs/reports/01-gate0.md and
runs/ina-2026-09-06/outputs/blocks/B01-gate0.yaml. The report's inline YAML and
the standalone block file are byte-identical in substance. No divergence found.

## 1.1 Operating rules and formula definitions

| # | Rule | Verdict | Note |
|---|---|---|---|
| G1 | Opening line "Data available: X years (FY__ to FY__). Scoring adapted..." | PASS | "Data available: 5 years (FY2022 to FY2026)... Scoring adapted to 5-year history." |
| G2 | ROCE = EBIT / (Total Assets - Current Liabilities); use source ROCE if present, else state "computed" | PASS | States "computed", source carries no ROCE row. Whether the CSV carries a ROCE row is verifier A's call. |
| G3 | ROE = PAT / average Net Worth; earliest year may use closing, must state so | PASS | Stated for FY2022. The implied net-worth chain (22.14 -> 52.88 -> 108.14 -> 608.36 -> 807.14) is internally consistent and closes on the 807.14 used in D3. |
| G4 | WC Days = RecDays + InvDays - PayDays, on Revenue basis unless COGS explicit, basis stated | PASS | "Basis: Sales, per formula default, COGS not separately available." |
| G5 | FCF = CFO - Capex, capex from the cash flow statement (PPE + intangibles) | FAIL, MINOR | Capex proxied from AR Note 4 gross-block Additions plus change in CWIP, and for FY2023/24 from delta Net Block + Depreciation + delta CWIP. The CF-statement capex line was unreadable after PDF extraction. Substitution is disclosed in data_notes and no double count is introduced. Deviation from the fixed formula stands as recorded. |
| G6 | CAGR = (End/Start)^(1/years) - 1 | PASS | Both CAGRs re-derived, see 1.4. |
| G7 | CAGR edge rules (negative or zero endpoint, loss-to-profit swing, C4 when PAT CAGR is N/M) | PASS | No endpoint is negative or zero. No loss-to-profit swing exists. No edge rule was applicable and none was invented. |

## 1.2 Block A, Return on Capital (reported 14/20)

ROCE re-derived from the stage's own stated inputs:

| Year | EBIT re-derived | Capital employed re-derived | ROCE re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| FY2024 | 67.53 + 10.49 - 4.15 = 73.87 | 274.69 - 135.08 = 139.61 | 52.91% | 52.91% | match |
| FY2025 | 153.62 + 7.57 - 9.05 = 152.14 | 851.00 - 209.63 = 641.37 | 23.72% | 23.72% | match |
| FY2026 | 245.28 + 23.54 - 17.50 = 251.32 | 2155.13 - 758.29 = 1396.84 | 17.99% | 17.99% | match |

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G8 | A1 median ROCE band | 23.72% -> 4 | median of (52.91, 23.72, 17.99) = 23.72, band 20-24.9 = 4 | PASS |
| G9 | A2 minimum single-year ROCE band | 17.99% -> 5 | min = 17.99, band >=15 = 5 | PASS |
| G10 | A3 median ROE band | 31.40% -> 5 | sorted (28.29, 28.47, 31.40, 35.23, 68.90), median 31.40, band >=20 = 5 | PASS |
| G11 | A4 ROCE trend latest vs earliest | -34.9pp -> 0 | 17.99 - 52.91 = -34.92pp, band >5pp decline = 0 | PASS |

Block A total re-derived: 4 + 5 + 5 + 0 = 14. Matches.

Observation, not a fail: A1 and A4 run on a 3-year ROCE window because no
FY2022/FY2023 current-liability split exists in the corpus. The stage discloses
this in data_notes. The framework permits "whatever history is available,
minimum 3 years". A4's "earliest" is therefore FY2024, a year with capital
employed of Rs 139.61 cr before a large equity raise. The mechanical result is
0 and would very likely stay 0 on any longer window, since capital employed
grew tenfold across the window. No score effect.

## 1.3 Block B, Cash Generation Quality (reported 2/20)

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G12 | B1 cumulative CFO / cumulative PAT | 0.194 -> 0 | CFO sum 8.79 - 1.40 + 30.27 + 113.10 - 73.13 = 77.63; PAT sum 399.52; ratio 0.1943; band <0.50 = 0 | PASS |
| G13 | B2 FCF-positive years proportion | 2 of 4 = 50% -> 2 | band 50-74 = 2 | PASS |
| G14 | B3 cumulative FCF / cumulative PAT | -1.33 -> 0 | FCF sum -32.57 + 13.42 + 21.12 - 523.81 = -521.84; PAT FY23-26 = 392.57; ratio -1.329; negative = 0 | PASS |
| G15 | B4 change in WC days, latest vs earliest | +18.86 days -> 0 | 62.58 - 43.72 = +18.86; band increased >15 = 0 | PASS |
| G16 | block_b_trend field carries the one number that shows it | "deteriorating", CFO +113.10 to -73.13 | present, quantified | PASS |

Working capital days re-derived from the stage's own balances and revenue:

| Year | RecDays | InvDays | PayDays | WC Days re-derived | Reported |
|---|---|---|---|---|---|
| FY2024 | 51.96/737.17*365 = 25.73 | 73.79/737.17*365 = 36.54 | 37.42/737.17*365 = 18.53 | 43.74 | 43.72 |
| FY2025 | 110.09/1333.76*365 = 30.13 | 76.98/1333.76*365 = 21.07 | 72.04/1333.76*365 = 19.71 | 31.49 | 31.48 |
| FY2026 | 281.59/2146.02*365 = 47.89 | 379.05/2146.02*365 = 64.47 | 292.73/2146.02*365 = 49.79 | 62.57 | 62.58 |

Differences are rounding only, below 0.03 days. No band is near an edge.

Observation, not a fail: B2 and B3 use a 4-year denominator because FY2022
capex cannot be computed (no FY2021 opening net block). Counting FY2022 as a
non-positive year would drop B2 to 0 (2 of 5 = 40%), a 2-point swing. The stage
did not do that, and it was right not to: scoring an uncomputable year would be
an estimate, which the framework's grounding rule forbids. The exclusion is
disclosed. PASS.

## 1.4 Block C, Growth (reported 20/20)

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G17 | C1 revenue CAGR band | 77.67% -> 5 | (2146.02/215.37)^0.25 - 1 = 77.67%; band >=20 = 5 | PASS |
| G18 | C2 PAT CAGR band | 131.7% -> 5 | (200.22/6.95)^0.25 - 1 = 131.68%; band >=20 = 5 | PASS |
| G19 | C3 positive YoY revenue years | 4 of 4 = 100% -> 5 | series rises every year; 100% = 5 | PASS |
| G20 | C4 PAT CAGR minus revenue CAGR | +54.0pp -> 5 | 131.68 - 77.67 = +54.01pp; band >=+3pp = 5 | PASS |

Block C total re-derived: 20. Matches. The consolidation-scope caveat is carried
in the report body and in data_notes, and the stage correctly declined to adjust
a series it cannot restate. That is the framework's grounding rule applied
properly.

## 1.5 Block D, Balance Sheet Strength (reported 13/20)

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G21 | D1 Net debt / EBITDA | 1.28x -> 3 | (887.91 - 520.94) / (251.32 + 35.80) = 366.97 / 287.12 = 1.278x; band 1-2x = 3 | PASS |
| G22 | D2 interest coverage | 10.68x -> 5 | 251.32 / 23.54 = 10.676x; band >=10x = 5 | PASS |
| G23 | D3 debt / equity | 1.10x -> 1 | 887.91 / 807.14 = 1.100x; band 1.0-1.5 = 1 | PASS |
| G24 | D4 current ratio | 1.86x -> 4 | 1409.71 / 758.29 = 1.859x; band 1.5-1.99 = 4 | PASS |

Block D total re-derived: 13. Matches. The stage flagged D1 as scoring-sensitive
to an unresolved Rs 232 cr internal cash reconciliation gap and reported the
lower, more conservative figure. That is correct conduct under the grounding
rule. The existence of the gap is verifier A's question, not mine.

## 1.6 Block E, Shareholder Alignment (reported 5/20)

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G25 | E1 promoter holding latest | 65.92% -> 5 | band >=60 = 5 | PASS |
| G26 | E2 promoter holding change over 3 years | -3.98pp -> 0 | see below | FAIL, MINOR |
| G27 | E3 promoter pledge | N/A -> 0 | grounding rule requires N/A scored 0 | PASS |
| G28 | E4 contingent liabilities / net worth | 205% -> 0 | 1654.01 / 807.14 = 204.9%; band >30% = 0 | PASS |

E2 detail. The framework specifies a 3-year change. The stage measured FY2024 to
FY2026, a 2-year window, and labelled it "over 3 years". No earlier promoter
figure exists in the corpus: the AR carries three shareholding dates only. The
score is almost certainly unaffected, because promoter dilution accumulates and
a true 3-year window would show a decline of at least 3.98pp, which still lands
in the ">3% decrease = 0" band. The defect is the mislabelled window and the
absence of a data_note recording the substitution, while every other window
substitution in this stage was recorded. Graded MINOR on that basis.

E3 detail, and this is good conduct worth naming. The stage scored 0 for missing
pledge data and then explicitly refused to read that 0 as a ">15% pledge"
deal-breaker trigger. Deal-breaker 5 is recorded as "cannot confirm", not as
"pass". The framework's grounding rule and its deal-breaker rules are both
honoured, and the ambiguity in the E3 band (where "no data" and "pledge >15%"
both score 0) is handled correctly.

Block E total re-derived: 5. Matches.

## 1.7 Block F, Quantitative Moat Scoring (reported 15/60)

| # | Test | Reported | Rule check | Verdict |
|---|---|---|---|---|
| G29 | M1 pricing power | 5 | margin +6.93pp (>=2pp) AND revenue CAGR 77.67% (>=10%) = 5 | PASS |
| G30 | M2 cost advantage | 0 | 13.38% vs peer median 30.38%, below peers = 0; median of (22.27, 30.38, 43.99) = 30.38 correct | PASS |
| G31 | M3 capital efficiency | 3 | FAT 4.09x >3x but ROCE 17.99% <20%, so top band fails; FAT >2x AND ROCE >15% = 3 | PASS |
| G32 | M4 customer stickiness | 3 | zero decline years but receivable days not stable +/-10, so top band fails; falls to "max 1 decline year" band = 3. Ordered-band reading is standard | PASS |
| G33 | M5 scale and dominance | 0 | "PEER DATA NEEDED" marked, framework says score 0 in that case | PASS |
| G34 | M6 technology / R&D | 0 | no R&D line, N/A scored 0 per grounding rule | PASS |
| G35 | M7 regulatory / license | 0 | see below | FAIL, MINOR |
| G36 | M8 distribution | 0 | see below | FAIL, MINOR |
| G37 | M9 brand | 0 | GM proxy 9.87% vs peer median 36.06%, at/below = 0; proxy basis stated as the framework requires | PASS |
| G38 | M10 switching costs | 0 | revenue grew every year but receivable days +19.92 (>10), top band fails; band 3 needs stability, fails; band 1 needs 2+ decline years, not applicable; else 0 | PASS |
| G39 | M11 network effects | 3 | fewer than 6 years, scored conservatively on overall trend and said so, exactly as the framework directs; band 3 conditions met | PASS |
| G40 | M12 negative WC / float | 1 | see below | PASS with observation |
| G41 | "PEER DATA NEEDED" marking rule, never guess peer figures | marked on M5 | no peer figure invented anywhere | PASS |
| G42 | Moat classification band | 4 present = STRONG | M1, M3, M4, M11 score >=3; band 4-5 = STRONG | PASS |

M7 detail. The framework band reads "regulated but >10 players = 1 | unregulated
= 0". The stage's own text says solar module manufacturing "carries ALMM
(Approved List of Models and Manufacturers) listing requirements" and that more
than 10 listed module makers exist. Those two facts map to the "regulated but
>10 players" band, which scores 1, not 0. The stage instead reasoned that ALMM
is "not a scarce-license business" and scored 0. That reading is defensible on
the category's intent. The cost is 1 point of 60. Moat score would be 16, grand
total 70, and the moat count is unchanged because 1 is below the "present"
threshold of 3. No classification effect. Graded MINOR.

M8 detail. The stage wrote "no distribution-network or outlet data disclosed"
and scored 0. B07, reading the same annual report, cites AR p.96 BRSR for a
dealer/distributor count (93 falling to 82) and a channel sales share (12.44%
falling to 11.61%). Distribution reach is therefore quantified in the corpus,
and the M8 bands should have been tested against it. The score is unchanged at 0
on that data, because the network is shrinking, so bands 5 and 3 both fail and
band 1 ("mentioned unquantified") does not fit. The defect is an assertion of
absence that a sibling stage contradicts from the same document. Graded MINOR.
Whether the p.96 disclosure exists is verifier A's ruling, not mine.

M12 observation, no fail. The band text is "WC days negative in majority of
years = 5 | 0-15 days consistently = 3 | 15-45 = 1 | >45 = 0". Only the top band
names a basis ("majority of years"). The stage applied a majority basis to band
1 (two of three years inside 15-45) and flagged the latest year at 62.58 as
worsening. A latest-year reading, matching the convention Blocks D and E use
explicitly, would give 0. The framework text does not specify. One point, no
moat-count effect. Recorded as an observation rather than a fail.

Block F total re-derived: 5 + 0 + 3 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 1 = 15.
Matches.

Note for verifier A, not a ruling by me. M3 uses net block of Rs 524.89 cr for
FY2026. B07 uses closing net PPE of Rs 473.77 cr for the same year and the same
basis (AR p.116). The two stages disagree on the same balance by about Rs 51 cr.
M3 scores 3 on either figure, so nothing here moves. The existence question
belongs to verifier A.

## 1.8 Classification, confidence, deal-breakers

| # | Rule | Reported | Re-derived | Verdict |
|---|---|---|---|---|
| G43 | Core score arithmetic | 54 | 14 + 2 + 20 + 13 + 5 = 54 | PASS |
| G44 | Grand total arithmetic | 69 | 54 + 15 = 69 | PASS |
| G45 | Grand total maximum stated | "69 / 120" | maximum is 100 + 60 = 160; B07 6C states 69/160 correctly | FAIL, MINOR |
| G46 | Data confidence tiering | 5 years -> "5-6 lower" band, flag raised, no downgrade | downgrade triggers at 3-4 years only; history_downgrade false is correct | PASS |
| G47 | Classification matrix | Core 54 -> AVERAGE | band 40-59 = AVERAGE regardless of moat class; the stage states correctly that moat class can only lift a Core >=60 band | PASS |
| G48 | All 9 deal-breakers checked and recorded | all 9 listed | 2 and 4 triggered, both correctly; 6 correctly not triggered (1.28x, 10.68x); 3, 7, 8, 9 correctly not triggered; 1 correctly not triggered; 5 correctly recorded as unconfirmable | PASS |
| G49 | Deal-breaker note: state WHICH years drive it | "FY2026 alone", with the drivers named | present and specific | PASS |
| G50 | FLAG-GATE0 emitted when classification <= AVERAGE with depressors | emitted, with depressors named | required by the block schema comment | PASS |
| G51 | YAML schema complete, all fields present | all 16 fields present and typed | no field missing, no field invented | PASS |
| G52 | analyst_note <= 200 words | approx 176 words | inside the cap | PASS |
| G53 | Rule 4, source anchors on every extracted number | mostly anchored | see below | FAIL, MINOR |
| G54 | Rule 5, grounding, no estimated fills | no estimate found | every gap marked N/A and scored 0 | PASS |

G53 detail. Anchor discipline is strong through Blocks A to E. It thins in Block
F: the peer comparison table gives a collective basis line but no per-cell
anchor, and three figures used in moat scoring carry no inline anchor at all,
namely the FY2022 EBITDA margin of 6.45% (M1), the FY2022 receivable days of
27.98 (M10), and the FY2022-FY2025 selling and admin percentages (M11). All
three sit inside scoring decisions. Graded MINOR because the basis is stated and
the source file is named in the anchor index. Verifier A owns whether the
figures are in the file.

## 1.9 Gate 0 result

Rules checked: 52. Fails: 6, all MINOR (G5, G26, G35, G36, G45, G53).
Gate 0 rule acceptance: 46 of 52 = 88.5%.

Recomputed Gate 0 outcome: Core 54, moat 15, grand total 69, moat class STRONG,
classification AVERAGE. I concur with every headline value. Under the two
alternate readings I flagged (M7 = 1), the moat score would be 16 and the grand
total 70. Nothing moves the classification.

---

# PART 2: EMERGING MOAT (B07) COMPLIANCE

Artifacts: runs/ina-2026-09-06/outputs/reports/07-emoat.md and
runs/ina-2026-09-06/outputs/blocks/B07-emoat.yaml. Report inline YAML and block
file are identical. No divergence found.

## 2.1 Operating rules

| # | Rule | Verdict | Note |
|---|---|---|---|
| E1 | All six sections in one response, no stops | PASS | Sections 1 to 6 present, plus the Optionality Register |
| E2 | Evidence taxonomy applied to every item (documented / claim / inference) | PASS | Applied per row in Section 1A, per category in Section 3, and per cell in the Section 5 table |
| E3 | Source anchor on every evidence item | PASS | AR page, call date, or slide number carried throughout |
| E4 | Skeptical stance, no force-fit, "NO EVIDENCE FOUND" where empty | PASS | 17 of 23 categories carry an explicit NO EVIDENCE FOUND with reasoning |
| E5 | Completionist guard: recount performed | PASS | Recount performed and stated, and the guard's 12-category trigger is not reached (2 active) |
| E6 | Recount stated in the prescribed line form | FAIL, MINOR | Framework specifies the exact sentence "documented recount performed: [n] documented items across [m] categories." The stage wrote a prose paragraph carrying the same two counts (1 item, 1 category). Substance present, prescribed form not used. Presentational only |

## 2.2 Sections 1 and 2

| # | Rule | Verdict | Note |
|---|---|---|---|
| E7 | 1A pipeline table with status from the prescribed vocabulary | PASS | LAUNCHED-recent, UNDER DEVELOPMENT, CONCEPT all drawn from the named set; all six required columns present |
| E8 | 1B diversification direction with evidence and timeline | PASS | Four directions covered, each with evidence tier |
| E9 | 1C revenue mix shift table, four required columns | PASS | Present, with an explicit caveat that no 3-year cell has a documented anchor |
| E10 | 2A capex table, seven required columns | PASS | Five projects, all columns filled or marked not separately disclosed |
| E11 | 2B utilisation trajectory per facility | PASS | Correctly reports that no unit-wise utilisation has ever been disclosed, and anchors the refusal |
| E12 | 2C arithmetic shown | PASS | Every step shown |
| E13 | 2C result expressed correctly as % above current revenue | FAIL, MAJOR | See below |
| E14 | 2D new geography or market entries | PASS | Zero exports, documented |

E13 detail, and this is the largest finding in this pass. The framework
specifies: "total capex under execution x historical fixed asset turnover =
implied incremental revenue, expressed as % above current revenue; show the
arithmetic."

The stage computed Rs 2,500 cr x 4.57 = Rs 11,420 cr and named that figure
"implied incremental revenue". It then reported "+428% above FY2026 revenue of
Rs 2,163.52cr". Those two statements contradict each other. If Rs 11,420 cr is
incremental, then as a percentage above current revenue it is 11,420 / 2,163.52
= 528%. The reported 428% is 528 minus 100, which is only correct if Rs 11,420
cr were the total post-capex revenue base rather than the increment.

Recomputed: capex_embedded_growth_pct = 528, not 428.

Severity is MAJOR, not CRITICAL. The stage itself labels the whole number not
credible and gives the reason (a 4.57x turnover measured on an immature,
mostly-unbuilt asset base). It also carries management's own +131% figure beside
it. The emerging moat classification does not depend on this field. But
capex_embedded_growth_pct is a block field that downstream stages consume, and
it is wrong against the framework's own formula by 100 percentage points.

Related MINOR, listed separately below: 2C uses revenue of Rs 2,163.52 cr while
B01 uses Rs 2,146.02 cr for the same year. On the B01 basis the FAT is 4.53x and
the implied increment is Rs 11,325 cr, or +524%. The conclusion is unchanged.

## 2.3 Section 3, the 23-row scan

| # | Rule | Verdict | Note |
|---|---|---|---|
| E15 | All 22 categories plus R1 addressed or explicitly NO EVIDENCE FOUND | PASS | 23 rows counted: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1 |
| E16 | Category 21 (I1) and Category 22 (I2) present (verifier rule 8) | PASS | Both present and both scored |
| E17 | I1 scores above 0 only if both legs evidenced, (b) leg with at least one documented source | PASS | Scored 0. Part (a) fails on all three evidence routes: no patent inventors (R&D spend 0.00%), no ex-DRDO/HAL/global-major technical concentration, remuneration below not above sector norms. Part (b) correctly declared moot. The stage also correctly refused to count independent directors' PSU backgrounds as technical talent |
| E18 | I2 scores above 0 only if the named sacrifice is specific | PASS | Scored 0. The stage ran the test against each moat claimed elsewhere in the scan and reached the framework's own null answer, "nothing must be destroyed", which the framework instructs to score 0 |
| E19 | I1/I2 contribution stated separately (20-Aug-2026 ruling) | PASS | "I1/I2 contribution to the total: 0", with the review-checkpoint context named |
| E20 | Section 3 summary table with all rows and the four required columns | PASS | 23 rows, columns evidence / type / strength / time to materialise |
| E21 | Strong-or-Moderate count stated | PASS | "2 of 23 (B1, R1). No category scores Strong." |

## 2.4 Section 4 and Section 5

| # | Rule | Verdict | Note |
|---|---|---|---|
| E22 | 4A, 4B, 4C all present | PASS | Approvals pipeline, policy tailwinds, and the moat assessment each answered |
| E23 | Likelihood x impact matrix values applied as specified | FAIL, MAJOR | See below |
| E24 | Evidence multipliers applied as specified (1.0 / 0.7 / 0.5) | PASS | No 0.5 needed; no category is inference-only |
| E25 | No documented-tier multiplier on a claim-only category (verifier rule 3) | PASS | H1, H2 and R1 all carry 0.7 despite R1 resting partly on documented policy. Conservative and correct: the moat leg is capture, and capture is a claim |
| E26 | Mixed-tier category multiplier justified | FAIL, MINOR | See below |
| E27 | Full scoring table, all 23 rows, adjusted total | PASS | All 23 rows shown with raw, multiplier and adjusted columns |
| E28 | Adjusted-total arithmetic consistent with the values used | PASS | 3.0 + 1.4 + 2.1 + 2.1 = 8.6, rounded to 9 and stated as such |
| E29 | Classification bands >=40 / 25-39 / 12-24 / <12 applied absolutely, no rescale | PASS | 9 < 12 = NO MEANINGFUL EMERGING MOAT; block enum value "NONE" correct; ceiling correctly stated as 92 |

E23 detail. The framework's matrix is fixed: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1,
LL=1. The scoring table gives H1 a raw score of "2 (LM)". LM maps to 1, not 2.
The label and the number disagree. Either the label is wrong or the score is.
Read on the stage's own label, H1 adjusted becomes 1 x 0.7 = 0.7, and the total
becomes 3.0 + 0.7 + 2.1 + 2.1 = 7.9, rounding to 8.

Recomputed: em_score = 8, not 9.

The other three scored rows check out. B1 "3 (HM)" is a valid pair at 3. H2 "3
(MH)" is valid at 3. R1 "3 (HM)" is valid at 3. Classification is unchanged: 8
and 9 both fall below the 12-point floor, so NO MEANINGFUL EMERGING MOAT stands
either way. Severity MAJOR because it is a plain mismatch against an explicit
lookup table that moves a block field, not CRITICAL because no verdict turns on
it.

E26 detail. B1 carries a 1.0x documented multiplier. The Section 3 summary table
itself grades B1 as "documented (construction), claim (margin benefit)". The
likelihood leg is documented: construction progress and an IREDA drawdown are
real. The impact leg, the 400-500bps margin uplift that makes the impact
"Medium" rather than "Low", rests entirely on a management claim. Applying a
full documented multiplier to a raw score whose impact half is claim-grade
credits a claim at documented weight, which is the exact failure mode verifier
rule 3 exists to catch. It is not the pure case (the category is not
claim-only), so this is MINOR. A blended or 0.7 treatment would take B1 from 3.0
to about 2.1 and the total to about 7.0. Classification unchanged.

## 2.5 Optionality register and Section 6

| # | Rule | Verdict | Note |
|---|---|---|---|
| E30 | Register covers advantages scoring 0 or resting only on claim/inference | PASS | Seven rows, all drawn from zero-scored or claim-only material |
| E31 | Register carries the four prescribed columns | PASS | Optionality, converting evidence, where it first appears, conversion window |
| E32 | Register carried in the block as optionality_register[] | PASS | Seven entries, fields match |
| E33 | Registered options watched, never scored | PASS | None of the seven contributes to em_score |
| E34 | 6A timeline across all four windows | PASS | 12m, 12-24m, 24-36m, 3-5yr all populated with a named milestone |
| E35 | 6B risks per top-scoring moat with early warning signs | PASS | B1, R1, H2 each carry a risk and a named early warning |
| E36 | 6C uses the INJECTED Gate 0 block | PASS | Core 54, moat count 4, moat class STRONG, classification AVERAGE, grand total 69/160 all carried correctly from B01. The 160 denominator here is right, which is what exposes B01's own 120 |
| E37 | 6D combined classification from the standard eight-label matrix | PASS | "AVERAGE" is a valid label, with reasoning that correctly identifies the missing transition pairing |
| E38 | 6E final card: evolution map, 12m catalysts, biggest risk | PASS | All three present, evolution map given per family |

## 2.6 Block schema

| # | Rule | Verdict | Note |
|---|---|---|---|
| E39 | All schema fields present and correctly typed | PASS | Every field in the prescribed block appears |
| E40 | Block ends with exactly the prescribed field set | FAIL, MINOR | Two fields added off-schema: capex_fy2026_cr and capex_fy2026_anchor. The addition is useful and well anchored, but the framework says "exactly this fenced YAML block". A downstream consumer parsing on the schema will not expect them |
| E41 | active_categories restricted to Strong/Moderate rows | PASS | B1 and R1 only, both graded Moderate in the summary table. H1 and H2 are graded Weak and Weak-moderate and are correctly excluded |
| E42 | evidence_mix supported by the report body | FAIL, MINOR | {documented: 11, claim: 24, inference: 3} cannot be reconstructed from the report. No item-by-item tally is shown, and no row anywhere in the report is tagged as an analyst inference, so the inference count of 3 has no visible support. The completionist guard depends on exactly this tally being honest |
| E43 | catalysts_12m each carry evidence_type and anchor | PASS | Six catalysts, each anchored to a call date or slide, each tiered |
| E44 | capex_embedded_growth_pct carried from 2C | PASS as a carry, value wrong per E13 | The block faithfully carries the section's number; the number itself is the E13 fail |
| E45 | combined_assessment and combined_reasoning present | PASS | One line each, consistent with 6D |
| E46 | analyst_note <= 200 words | PASS | Approx 110 words |
| E47 | Revenue basis consistent with the injected B01 block | FAIL, MINOR | 2C uses Rs 2,163.52 cr; B01 uses Rs 2,146.02 cr for FY2026 revenue. One is likely total income and the other revenue from operations. Neither stage states which. Affects the FAT and therefore 2C. Which figure is in which document is verifier A's ruling |

## 2.7 Emerging Moat result

Rules checked: 42. Fails: 7 (2 MAJOR at E13 and E23, 5 MINOR at E6, E26, E40,
E42, E47).
Emerging Moat rule acceptance: 35 of 42 = 83.3%.

Recomputed Emerging Moat outcome: em_score 8 (reported 9),
capex_embedded_growth_pct 528 (reported 428), em_classification NO MEANINGFUL
EMERGING MOAT (concur), combined_assessment AVERAGE (concur). No decision moves.

---

# PART 3: VALUATION (B10 / B11)

PENDING PHASE 3. Stage 10 and stage 11 have not run in this phase. B10 and B11
do not exist. Verifier C rules 4, 7, 11 and 12 are not evaluated here, and the
valuation framework documents were not loaded, per the phase-1 scope rule.
Nothing in this report should be read as an opinion on the valuation. The
valuation section of the block below carries zero rules checked and is marked
pending.

Verifier C rule 6 (downstream signal candidates in B09) and rule 9 (Business
Understanding Narrative in stage 13) are likewise outside this invocation. B09
was not named among my inputs and stage 13 has not run. The
business_understanding_narrative block section is marked not applicable for
phase 1 rather than failed.

---

# PART 4: WHAT THE TWO STAGES DID WELL

Framework audits list defects. Three pieces of conduct deserve naming because
they are the behaviours the framework is trying to buy.

First, both stages refused to estimate. Gate 0 marked pledge data N/A and scored
it 0, then explicitly declined to treat that 0 as a deal-breaker trigger. It
reported the conservative D1 figure while naming the alternative. It flagged a
restatement it could not resolve rather than papering over it. Emerging Moat
reported that no utilisation number has ever been disclosed instead of inferring
one.

Second, the Emerging Moat scan resisted the completionist pull hard. Seventeen
categories carry an explicit NO EVIDENCE FOUND. B2 was scored 0 with the reason
stated as "to avoid crediting table-stakes compliance as differentiation". The
scan treated documented negatives (R&D at 0.00%, exports NIL, dealer count
falling) as findings rather than as blanks. That is the framework working as
designed.

Third, I1 and I2 were applied as written rather than as flattery. I1 correctly
separated governance appointments from technical talent. I2 correctly reached
"nothing must be destroyed" and scored 0, which is the honest answer for a
capacity race.

---

# PART 5: SUMMARY

| Portion | Rules checked | Fails | Acceptance |
|---|---|---|---|
| Gate 0 (B01) | 52 | 6 (0 CRITICAL, 0 MAJOR, 6 MINOR) | 88.5% |
| Emerging Moat (B07) | 42 | 7 (0 CRITICAL, 2 MAJOR, 5 MINOR) | 83.3% |
| Valuation (B10/B11) | 0 | pending phase 3 | not scored |
| TOTAL IN SCOPE | 94 | 13 | 86.2% |

framework_adherence: 86%, covering Gate 0 and Emerging Moat only. The valuation
portion is pending phase 3. This figure is not a whole-pipeline score and must
not be read as one.

No CRITICAL finding. No REWORK trigger fires from this verifier: acceptance sits
well above the 60% floor and the CRITICAL count is zero.

Two block fields should be corrected before they travel downstream:
em_score 9 should be 8, and capex_embedded_growth_pct 428 should be 528. Neither
correction changes a classification. Both are mechanical.

I concur with both stage verdicts. Gate 0 AVERAGE is correctly derived. Emerging
Moat NO MEANINGFUL EMERGING MOAT is correctly derived and survives every
alternate reading I tested. The combined AVERAGE is correctly reasoned against
the transition-setup rule.

```yaml
stage: B12c
company: "INA"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
scope: "PHASE 1 - Gate 0 (B01) and Emerging Moat (B07) only. Valuation audit deferred to phase 3."
gate0:
  rules_checked: 52
  fails:
    - "G5 FCF/capex definition: capex proxied from AR Note 4 gross-block additions plus change in CWIP instead of the cash-flow-statement PPE line the framework fixes. Disclosed in data_notes, forced by a PDF extraction defect."
    - "G26 E2 promoter holding change: measured FY2024 to FY2026 (2 years) but labelled 'over 3 years'; substitution not recorded in data_notes. Score almost certainly unchanged, since dilution accumulates and a longer window still lands in the >3pp band."
    - "G35 M7 regulatory/license: stage states ALMM listing requirements exist AND >10 listed module makers exist, which maps to the 'regulated but >10 players = 1' band, but scored 0. Recomputed moat score 16, grand total 70, moat count and classification unchanged."
    - "G36 M8 distribution: stage asserts 'no distribution-network or outlet data disclosed' while B07 cites AR p.96 BRSR dealer count 93 to 82 and channel share 12.44% to 11.61% from the same AR. Score stays 0 on that data because the network is shrinking, so no score effect."
    - "G45 Grand total maximum stated as 120 in the classification table; the correct maximum is 160 (100 core + 60 moat). B07 6C states 69/160 correctly, which exposes the B01 typo. Presentational."
    - "G53 Anchor discipline (framework rule 4): Block F peer comparison table carries a collective basis line but no per-cell anchors, and three scoring inputs are unanchored inline - FY2022 EBITDA margin 6.45% (M1), FY2022 receivable days 27.98 (M10), FY2022-FY2025 selling and admin percentages (M11)."
emoat:
  rules_checked: 42
  fails:
    - "E13 Section 2C: framework requires implied incremental revenue expressed as % ABOVE current revenue. Stage names Rs 11,420cr as incremental then reports +428%, which subtracts 100 as if Rs 11,420cr were the total post-capex base. Correct value is 11,420/2,163.52 = +528%. Recomputed capex_embedded_growth_pct = 528."
    - "E23 Section 5 scoring matrix: H1 raw score entered as '2 (LM)'. The framework matrix sets ML/LM = 1, not 2. On the stage's own label H1 adjusted is 0.7, not 1.4, and the total is 7.9 rounding to 8. Recomputed em_score = 8. Classification unchanged (both below the 12 floor)."
    - "E6 Completionist recount stated as a prose paragraph rather than the prescribed line form 'documented recount performed: [n] documented items across [m] categories'. Both counts (1 item, 1 category) are present. Presentational."
    - "E26 B1 carries a 1.0x documented multiplier although the stage's own summary table grades it 'documented (construction), claim (margin benefit)'. The impact half of the raw score rests on the claim-grade 400-500bps margin uplift. A blended or 0.7 treatment gives B1 2.1 and a total near 7.0. Classification unchanged."
    - "E40 Block schema extended off-spec with capex_fy2026_cr and capex_fy2026_anchor. Useful and well anchored, but the framework specifies 'exactly this fenced YAML block'."
    - "E42 evidence_mix {documented: 11, claim: 24, inference: 3} is not reconstructable from the report. No item tally is shown and no row anywhere is tagged as an analyst inference, so the inference count of 3 has no visible support. The completionist guard depends on this tally."
    - "E47 FY2026 revenue basis differs from the injected B01 block: 2C uses Rs 2,163.52cr, B01 uses Rs 2,146.02cr. Neither states whether the figure is total income or revenue from operations. Affects the FAT in 2C. Existence of each figure is verifier A's ruling, not mine."
valuation:
  rules_checked: 0
  fails: []
  status: "PENDING PHASE 3 - stage 10 and stage 11 have not run; B10 and B11 do not exist; valuation framework docs not loaded per phase-1 scope. Verifier C rules 4, 7, 11 and 12 not evaluated."
business_understanding_narrative:
  present: false
  five_questions_answered: false
  prose_only: false
  section6_candidates_named: 0
  valuation_vocab_leak: false
  fails: []
  status: "NOT APPLICABLE IN PHASE 1 - stage 13 has not run. Not a fail, not a REWORK trigger. Deferred with the valuation audit."
recomputed_destination_pe: ""    # not applicable in phase 1, no valuation stage has run
recomputed_decision: ""          # concur: Gate 0 AVERAGE, Emerging Moat NONE, combined AVERAGE
recomputed_values:
  em_score: "reported 9, recomputed 8 (H1 matrix value, finding E23)"
  capex_embedded_growth_pct: "reported 428, recomputed 528 (finding E13)"
  gate0_core_score: "reported 54, concur"
  gate0_moat_score: "reported 15, recomputed 16 under the M7 alternate reading (finding G35); moat count and classification unchanged either way"
  gate0_classification: "reported AVERAGE, concur"
  em_classification: "reported NO MEANINGFUL EMERGING MOAT, concur (8 and 9 both below the 12 floor)"
findings:
  - severity: "MAJOR"
    location: "B07 Section 2C / block capex_embedded_growth_pct"
    description: "Framework 2C requires implied incremental revenue expressed as % above current revenue. The stage names Rs 11,420cr as incremental, then reports +428%, treating that figure as the total post-capex base instead. Correct application gives 11,420/2,163.52 = +528%. The block field 428 travels downstream. The stage does flag the whole number as not credible and carries management's own +131% beside it, which contains the damage."
  - severity: "MAJOR"
    location: "B07 Section 5 scoring table, row H1 / block em_score"
    description: "H1 raw score entered as '2 (LM)' against a framework matrix that sets ML/LM = 1. Label and number disagree. On the stage's own label the adjusted score is 0.7 and the total is 7.9, rounding to em_score 8 rather than 9. Classification is unchanged because both sit below the 12-point floor."
  - severity: "MINOR"
    location: "B01 formula definitions / Block B FCF"
    description: "Capex proxied from AR Note 4 gross-block additions plus change in CWIP instead of the cash-flow-statement PPE and intangibles line the framework fixes. Forced by a PDF extraction defect, disclosed in data_notes, and no double count introduced. Recorded as a deviation from a fixed formula."
  - severity: "MINOR"
    location: "B01 Block E, E2"
    description: "Promoter holding change measured over a 2-year window (FY2024 to FY2026) but labelled 'over 3 years', and the substitution is absent from data_notes while every comparable substitution in this stage was recorded. Score is almost certainly unaffected: dilution accumulates, so a true 3-year window still lands in the '>3pp decrease = 0' band."
  - severity: "MINOR"
    location: "B01 Block F, M7"
    description: "The stage states that ALMM listing requirements apply and that more than 10 listed module makers exist. Those two facts map to the framework's 'regulated but >10 players = 1' band, but M7 was scored 0. Defensible on the category's intent. Cost is 1 point: moat score 16, grand total 70, moat count 4 and moat class STRONG unchanged."
  - severity: "MINOR"
    location: "B01 Block F, M8"
    description: "Stage asserts 'no distribution-network or outlet data disclosed' and scores 0. B07 cites AR p.96 BRSR for a dealer/distributor count (93 to 82) and channel sales share (12.44% to 11.61%) from the same annual report. The M8 bands were therefore not tested against available data. Score stays 0 because the network is shrinking. Whether the p.96 disclosure exists is verifier A's ruling."
  - severity: "MINOR"
    location: "B01 classification table, Grand Total row"
    description: "Grand total maximum stated as 120. The correct maximum is 160 (100 core plus 60 moat). B07 Section 6C states 69/160 correctly. Presentational, no score effect."
  - severity: "MINOR"
    location: "B01 Block F peer table and moat scoring inputs"
    description: "Framework rule 4 requires an anchor on every extracted number. The peer comparison table carries a collective basis line but no per-cell anchors, and three figures used in scoring carry no inline anchor: FY2022 EBITDA margin 6.45% (M1), FY2022 receivable days 27.98 (M10), FY2022-FY2025 selling and admin percentages (M11). Source file named in the anchor index. Existence is verifier A's ruling."
  - severity: "MINOR"
    location: "B07 Section 3 completionist recount"
    description: "Recount stated as a prose paragraph rather than the prescribed line form. Both required counts (1 documented item, 1 category) are present, and the guard's 12-category trigger is not reached. Presentational."
  - severity: "MINOR"
    location: "B07 Section 5, row B1 multiplier"
    description: "B1 carries a 1.0x documented multiplier while the stage's own summary table grades it 'documented (construction), claim (margin benefit)'. The impact half of the raw score rests on the claim-grade 400-500bps margin uplift, so a full documented multiplier credits a claim at documented weight. Blended or 0.7 treatment gives B1 2.1 and a total near 7.0. Classification unchanged."
  - severity: "MINOR"
    location: "B07 block schema"
    description: "Two fields added off-schema, capex_fy2026_cr and capex_fy2026_anchor, against a framework instruction to end with exactly the prescribed block. The addition is useful and well anchored, but a schema-strict downstream parser will not expect it."
  - severity: "MINOR"
    location: "B07 block evidence_mix"
    description: "evidence_mix {documented: 11, claim: 24, inference: 3} cannot be reconstructed from the report body. No item-by-item tally is shown, and no row anywhere in the report is tagged as an analyst inference, so the inference count of 3 has no visible support. The completionist guard depends on this tally being honest."
  - severity: "MINOR"
    location: "B07 Section 2C vs B01 Block C, FY2026 revenue basis"
    description: "2C uses FY2026 revenue of Rs 2,163.52cr while B01 uses Rs 2,146.02cr for the same year, and neither stage states whether its figure is total income or revenue from operations. Affects the fixed asset turnover in 2C (4.57x vs 4.53x) and therefore the 2C output. Conclusion unchanged. Which figure sits in which document is verifier A's ruling, not mine."
critical_count: 0
major_count: 2
minor_count: 11
acceptance_rate: 86        # 81 rules passed of 94 checked, Gate 0 + Emerging Moat only
framework_adherence: 86    # PARTIAL SCORE. Gate 0 88.5% (46/52) + Emerging Moat 83.3% (35/42).
                           # Valuation portion PENDING PHASE 3 and excluded from this figure.
                           # Not a whole-pipeline score.
rework_triggered: false    # zero CRITICAL findings; acceptance well above the 60% floor
```
