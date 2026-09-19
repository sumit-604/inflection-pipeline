# STAGE 12, VERIFIER C: FRAMEWORK ADHERENCE, GOODLUCK (Goodluck India Ltd)

Run date: 2026-09-19. Model: claude-opus-5. Scope: PHASE 1 ONLY (Gate 0 B01
and Emerging Moat B07). The valuation audit (B10/B11, rules 4, 5, 7, 11-15)
is PENDING PHASE 3. No valuation framework document was read.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Re-derivation sources: inputs/screening/screener-Data_Sheet.csv (Rs Cr,
consolidated), inputs/annual-report/Annual_Report_2026.txt (Rs lakh; page
references below are the "[page N]" markers in the text file, with the txt line).

This verifier audits rule application. Source fidelity of individual numbers
belongs to Verifier A. Where I re-derive a number, I re-derive it only to test
a rule.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Re-derivation of every block score

| Rule | Stated input (B01) | Re-derived input | Band applied | B01 score | Verifier score | Result |
|---|---|---|---|---|---|---|
| A1 median ROCE | 19.37% (FY24-26) | 20.05 / 19.32 / 19.37%, median 19.37% (EBIT and CE per B01 table; 259.90/1,295.99, 301.20/1,558.75, 351.47/1,814.78) | 15-19.9 = 3 | 3 | 3 | PASS |
| A2 min ROCE | 19.32% | 19.32% | >=15 = 5 | 5 | 5 | PASS |
| A3 median ROE | 13.26% (AR Key Ratios, FY24-26 only) | 11.80% (computed per the fixed formula, 10 years, see 1.2) | <12 = 0 | 2 | 0 | FAIL |
| A4 ROCE trend | -0.69pp | -0.69pp (19.37 vs 20.05/20.06) | rule gap, nearest band 1-3pp = 3 | 3 | 3 | PASS (documented edge case) |
| B1 cum CFO/PAT | 709.22 / 772.54 = 0.918 | 709.22 / 772.54 = 0.918 (screener-data rows 57, 24) | 0.85-0.99 = 4 | 4 | 4 | PASS |
| B2 FCF+ years | 0 of 3 | 0 of 3 (capex only in AR CF, FY24-26) | <50% = 0 | 0 | 0 | PASS |
| B3 cum FCF/PAT | -722.41 / 478.61 = -1.51 | -1.51 | negative = 0 | 0 | 0 | PASS |
| B4 WC days change | +19.47 | FY24 36.36+63.08-14.21 = 85.24; FY26 42.59+76.21-14.07 = 104.73; +19.5 | >15 = 0 | 0 | 0 | PASS |
| C1 revenue CAGR | 15.81% | (4,100.28/1,093.01)^(1/9)-1 = 15.8% | 15-19.9 = 4 | 4 | 4 | PASS |
| C2 PAT CAGR | 27.85% | (180.71/19.75)^(1/9)-1 = 27.9% | >=20 = 5 | 5 | 5 | PASS |
| C3 positive YoY | 7 of 9 | 7 of 9 (declines FY20, FY21) = 77.8% | 75-99 = 3 | 3 | 3 | PASS |
| C4 PAT minus rev CAGR | +12.04pp | +12.1pp | >=+3 = 5 | 5 | 5 | PASS |
| D1 ND/EBITDA | 2.69x | (1,119.46-49.33)/(245.63+105.84+67.03-20.24) = 1,070.13/398.26 = 2.69x | 2-3x = 1 | 1 | 1 | PASS |
| D2 IC | 3.32x | 351.47/105.84 = 3.32x | 3-4.9 = 2 | 2 | 2 | PASS |
| D3 D/E | 0.73x | 1,119.46/1,528.61 = 0.73x (0.75x on owners' equity 1,490.96; same band) | 0.5-1.0 = 3 | 3 | 3 | PASS |
| D4 current ratio | 1.38x | not re-derivable from screener (no CA/CL split); band correct for 1.38 | 1.2-1.49 = 2 | 2 | 2 | PASS |
| E1 promoter | 54.00% | band check only | 50-59.9 = 4 | 4 | 4 | PASS |
| E2 promoter change | -2.45pp over ~32 months | band check only; nearest-anchor lookback stated | down 1-3 = 1 | 1 | 1 | PASS |
| E3 pledge | N/A | rule 5: "mark N/A and score it 0" | N/A = 0 | 0 | 0 | PASS |
| E4 CL/NW | 353.23/1,528.61 = 23.11% | 119.52+219.28+13.43+0.99 = 353.22; 23.1% | 15-30 = 1 | 1 | 1 | PASS |
| M1 pricing power | FY17 7.96% to FY26 9.71%, +1.75pp; rev CAGR 15.8% | FY17 EBITDA 26.87+48.10+17.54-5.48 = 87.03 (screener rows 22, 21, 20, 19); +1.75pp | stable +/-2 and CAGR >=10 = 3 | 3 | 3 | PASS |
| M2, M5, M9 | PEER DATA NEEDED | no peer data in stage-1 inputs | rule: score 0 | 0 | 0 | PASS |
| M3 capital efficiency | FAT 3.41x, ROCE 19.37% | 4,100.28/1,202.68 = 3.41x | FAT>2 and ROCE>15 = 3 | 3 | 3 | PASS |
| M4 stickiness | 2 decline years | 2 decline years, CAGR positive | = 1 | 1 | 1 | PASS |
| M6 R&D | no R&D spend disclosed | AR confirms narrative only, no amount (AR [page 52], txt l.4750-4760) | = 0 | 0 | 0 | PASS |
| M7 regulatory | "unregulated, no licence gate evidenced" | Arms Act, 1959 Industrial Licence held by subsidiary (AR [page 16] l.1074-1076; [page 39] l.3573) | player count NOT FOUND, so PEER DATA NEEDED = 0 | 0 | 0 | FAIL (rationale, score stands) |
| M8 distribution | "no distribution-reach data in corpus" | BRSR: dealers/distributors 157 (FY26) vs 316 (FY25); dealer sales 9.30% vs 9.8% of sales (AR [page 104] l.7871-7872); 600+ customers in 100+ countries (AR [page 6] l.302) | reach quantified but shrinking: no band fits exactly; 0 or 1 | 0 | 0 or 1 | FAIL (premise false) |
| M10 switching | 2 decline years | same | = 1 | 1 | 1 | PASS |
| M11 network | latest 3yr 10.09% < prior 23.39% | 10.10% vs 23.36%; selling % FY17 5.83% vs FY25 5.75% (screener row 17; FY26 blank) | no tier met = 0 | 0 | 0 | PASS |
| M12 float | WC days 85, 105 | >45 | = 0 | 0 | 0 | PASS |

Block arithmetic (B01 as stated): A 13, B 4, C 17, D 8, E 6, core 48; moat 8;
grand 56. All sums correct as stated. PASS.

Moat presence: M1 and M3 at 3, count 2, MODERATE (2-3). PASS. The M8
correction cannot reach 3, so the moat count holds at 2 either way.

### 1.2 FAIL detail: A3 median ROE (MAJOR)

Rule text: "ROE = PAT ÷ average Net Worth (opening + closing ÷ 2)". Operating
rule 6: "Use whatever history is available: minimum 3 years, maximum whatever
exists." The formula block permits a source-provided figure for ROCE only
("If the data source provides its own ROCE ... use the source's figure"); it
grants no such licence for ROE.

B01 used the AR Key Ratios ROE for FY24-FY26 only and stated the reason as
"FY17-FY23 Balance Sheets are not in the corpus." That premise holds for the
current-liability split. It does not hold for Net Worth. The screener
Data_Sheet carries Equity Share Capital and Reserves for all 10 years (rows 39,
40). ROE is fully computable on the fixed formula for FY17-FY26.

Recomputed (screener-data; NW = Equity Share Capital + Reserves; FY17 on
closing NW, stated per the rule):

| FY | PAT | Avg NW | ROE |
|---|---|---|---|
| FY17 | 19.75 | 254.92 (closing) | 7.75% |
| FY18 | 15.99 | 266.61 | 6.00% |
| FY19 | 31.46 | 294.03 | 10.70% |
| FY20 | 33.87 | 327.91 | 10.33% |
| FY21 | 30.05 | 364.75 | 8.24% |
| FY22 | 75.01 | 424.68 | 17.66% |
| FY23 | 87.80 | 542.97 | 16.17% |
| FY24 | 132.27 | 869.69 | 15.21% |
| FY25 | 165.63 | 1,215.19 | 13.63% |
| FY26 | 180.71 | 1,400.99 | 12.90% |

Median = (10.70 + 12.90) / 2 = 11.80%, band <12 = 0. The result is robust to
the basis: splicing the AR's own FY24-26 ratios onto computed FY17-23 gives a
median of 11.70%, still 0.

Effect: A3 2 to 0. Block A 13 to 11. Core 48 to 46. Grand total 56 to 54.
Classification stays AVERAGE (core 40-59 band). No deal-breaker changes
(Block A 11 is not <8). Severity MAJOR: a wrong score, decision survives.

### 1.3 FAIL detail: M7 (MINOR)

B01 scores M7 = 0 on the premise "an unregulated manufacturing business, no
licence/quota gate evidenced." The AR states the subsidiary "received an
Industrial License under the Indian Arms Act, 1959 for manufacturing artillery
shells" (AR [page 16], txt l.1074-1076; again [page 39], l.3573). The defence
line is regulated. The 5/3/1 bands need a listed-player count, which is NOT
FOUND in the stage-1 inputs. The correct entry is 0 marked PEER DATA NEEDED,
not 0 marked "unregulated." Score unchanged; the rationale contradicts the
corpus and contradicts B07, which scores the same licence as its strongest
emerging moat.

### 1.4 FAIL detail: M8 (MINOR)

B01 states "no distribution-reach data (outlets, dealers) in the corpus." The
BRSR in AR2026 quantifies the dealer network: 157 dealers/distributors in FY26
against 316 in FY25, carrying 9.30% of sales against 9.8% (AR [page 104], txt
l.7871-7872). Reach is quantified and shrinking. No M8 band fits that state
exactly: 5 and 3 need a growing network, 1 is written for "mentioned
unquantified." Defensible scores are 0 or 1; moat presence (>=3) is not
reachable. Score effect 0 to +1 on moat_score; classification unaffected. The
finding is the false "not in corpus" premise, which a downstream reader would
carry forward.

### 1.5 Classification, confidence, deal-breakers, CAGR edge rules

| Rule | Check | Result |
|---|---|---|
| Classification matrix | Core 48 in 40-59 = AVERAGE regardless of moat tier. Recomputed core 46: same band. | PASS |
| Confidence adjustment | data_years 10 (FY17-FY26) for P&L and CF, so no tier downgrade. B01 flags the 3-year window on BS-dependent metrics as FLAG-DATA-LIMITED instead of a downgrade. The rule keys to history available; 10 years are available. | PASS |
| Deal-breakers | #2 (Block B 4 <8) recorded, non-binding, driving years FY24-26 named. #6 tested both legs (2.69x, 3.32x), not triggered. #3, #4, #5, #7, #8, #9 tested and correctly negative. | PASS |
| CAGR edge rules | No negative endpoint in C1/C2; no loss-to-profit swing, noted in data_notes; C4 computed on valid CAGRs; B3 negative ratio scored via the "negative" band. | PASS |
| Operating rule 6 opener | "Data available: 10 years (FY17 to FY26)" present; per-metric windows stated. The verbatim "Scoring adapted to [X]-year history" clause is replaced by per-metric statements. Acceptable. | PASS |

Observation (not scored as a fail): the B4 window. Payables exist only for
FY24-26, so the formula cannot run on 10 years, and B01's 3-year window is
correct. The partial 10-year read (receivable + inventory days, screener rows
49, 50, 11) runs the other way: 142.8 days FY17 against 118.8 days FY26. The
block_b_trend label "deteriorating" is a 3-year reading. Downstream stages
should read FLAG-CASH as a capex-cycle signal, not a 10-year trend.

Gate 0 tally: 36 rules checked, 3 FAIL (1 MAJOR, 2 MINOR), 33 PASS.
Recomputed Gate 0: core 46 (A 11, B 4, C 17, D 8, E 6), moat 8 or 9, grand
54 or 55, 2 moats present, MODERATE, classification AVERAGE (unchanged).

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Rule-by-rule

| # | Rule (prompts/07) | Check | Result |
|---|---|---|---|
| E1 | All 23 rows addressed (20 categories A1-H3, I1, I2, R1) or NO EVIDENCE FOUND | 23 rows in the Section 3 summary and the Section 5 scorecard | PASS |
| E2 | Six sections present | Sections 1-6 plus Optionality Register present | PASS |
| E3 | Raw score = likelihood x impact matrix | HH=4 (A1, R1), HM=3 (B2, E2), MM=2 (C1), LM=1 (E1, G1, H2, H3): all map correctly | PASS |
| E4 | Evidence multiplier arithmetic | 4+3+1.4+1+3+1+1+1+4 = 19.4; C1 at 0.7 is conservative, not a breach | PASS |
| E5 | Scores consistent with evidence tiers (verifier rule 3) | E2 scored 📄 1.0 at H likelihood on a single-quarter presentation figure | FAIL (MINOR) |
| E6 | One improvement, one mechanism | Arms Act licence + DGQA + CRISIL quote credited at 4.0 under A1 AND 4.0 under R1 | FAIL (MAJOR) |
| E7 | Completionist recount performed and stated | "📄 recount performed: 17 documented items across 9 scored categories" present | PASS |
| E8 | Recount integrity (📄 items are documented and traceable) | includes presentation export figures as 📄; four order filings named in the recount appear nowhere in the scan body with a date or anchor | FAIL (MINOR) |
| E9 | Completionist guard threshold (12+ active = stop) | 4 Strong/Moderate, 9 scored | PASS |
| E10 | Classification band | 19.4 in 12-24 = MODEST | PASS |
| E11 | Category 21 I1 (verifier rule 8) | present; scored 0; no (b) competitor-economics leg; (a) leg alone correctly scored 0 | PASS |
| E12 | Category 22 I2 (verifier rule 8) | present; scored 0 with the named test answered "nothing must be destroyed" | PASS |
| E13 | I1/I2 contribution stated separately | "I1/I2 contribution to the total: 0.0" | PASS |
| E14 | Section 2C arithmetic (capex under execution x historical FAT) | not run; CRISIL FY27 revenue guide substituted | FAIL (MAJOR) |
| E15 | Optionality register, table and block | 7 rows, four columns, carried in B07 optionality_register | PASS |
| E16 | 6C uses the injected B01 block | core 48, AVERAGE, 2 moats, MODERATE: matches B01 | PASS |
| E17 | 6D combined classification per matrix | AVERAGE backward + MODEST forward: not an EXPANSION transition setup; AVERAGE is consistent | PASS |
| E18 | Taxonomy note: not FTTCP | stated in the header | PASS |

### 2.2 FAIL detail: E6, A1/R1 double credit (MAJOR)

A1 is scored HH 📄 = 4.0 on the Arms Act Industrial Licence (Reg 30 filing
01-Oct-2025), the DGQA certificate (27-Jul-2026), the AR "select group"
statement and CRISIL's "negligible competition" line. R1 is scored HH 📄 =
4.0 on the same licence and the same DGQA certificate (4A table), with CRISIL's
same "negligible competition" line as "the closest documented,
competitor-relevant policy-tailwind statement" (4B). R1's own distinct
evidence, a Goodluck-specific policy tailwind (PLI, incentive, enrolment,
procurement preference), is NOT FOUND in the report's own words (4B).

The report applies the no-double-credit rule itself three times: E1 ("scored
once, under A1, per the no-double-credit rule"), H1 ("the same
regulatory-licence fact already scored once under A1"), and I2 ("already
credited once under A1 and R1"). It does not apply the rule to R1. One fact
earns 8.0 of the 19.4 total. CLAUDE.md NEVER: "Never credit one quality
improvement through two mechanisms."

Recomputed: R1 carries no evidence independent of A1, so R1 = 0. Adjusted
total 19.4 - 4.0 = 15.4, MODEST (unchanged band). The alternative reading is
a 🔍-tier credit for the Atmanirbhar alignment language (ML = 1 x 0.5 = 0.5),
giving 15.9, also MODEST. The observation that separates the two readings: a
named scheme, incentive amount or procurement-preference listing specific to
GDAL in a filed document. Severity MAJOR: em_score wrong by about 4 points,
classification and the EM >=25 UA qualifier outcome (not met) unchanged.

### 2.3 FAIL detail: E14, Section 2C methodology substitution (MAJOR)

Rule text: "total capex under execution × historical fixed asset turnover =
implied incremental revenue, expressed as % above current revenue; show the
arithmetic." B07 states the method "could not be run: no gross-block/net-block
schedule for property, plant and equipment was located in the extracted AR
text." That premise is false. The consolidated balance sheet carries
"Property, plant and equipment 4(a) 1,20,190.73 [FY26] 79,929.37 [FY25]" (Rs
lakh; AR [page 188], txt l.13000), and Note 4(a) is the PPE schedule (AR
[page 197], txt l.13788). Consolidated revenue from operations is 4,10,028.32
lakh (AR [page 189], txt l.13072).

Recomputed per the rule, on the documented capex under execution the report
itself carries (GDAL Phase 2, ~Rs 500 Cr, Reg 30 filing 06-Aug-2026, as cited
in B07):
- FAT FY26 = 4,100.28 / 1,201.91 = 3.41x
- Implied incremental revenue = 500 x 3.41 = Rs 1,706 Cr
- % above current revenue = 1,706 / 4,100.28 = 41.6%

B07 instead writes capex_embedded_growth_pct: 12, taken from CRISIL's FY27
consolidated revenue guide (Rs 4,500-4,700 Cr vs Rs 4,100 Cr). That is a
one-year guided growth rate, a different quantity from capex-embedded growth.
The report labels it a substitution, so it is not silent; the substitution is
still unnecessary, because the rule's inputs are in the corpus.

Both readings, for the downstream stage: the rule-as-written 41.6% applies a
group FAT built on the steel business to a defence line. The GDAL Phase-1 own
economics (AR: ~INR 5,000 Mn investment, AR [page 39] l.3574; FY27 guide Rs
250-300 Cr per B07 1A) imply a defence FAT near 0.5-0.6x. On that basis Rs
500 Cr adds roughly Rs 250-300 Cr, or 6-7%. The separating observation is the
first full-year GDAL segment revenue against its gross block. The rule
requires the 41.6% arithmetic to be shown; the defence-FAT reading belongs
beside it as the stated caveat, not in its place. Severity MAJOR: the field
feeds downstream stages with a figure that is not the defined metric; no
Gate 0 or EM classification changes.

### 2.4 FAIL detail: E5, E2 tier and likelihood (MINOR)

E2 is scored HM 📄 1.0 = 3.0. The H likelihood rests on "Export revenue grew
~53% YoY in Q1 FY27 ... ~29% of consolidated revenue that quarter (Inv. Pres.
slide 2, Q1 FY27)." Stage 7's taxonomy places presentation statements at 🎙️
unless backed by filed evidence. The report itself finds no supply-chain-shift
language, the category's defining evidence. The filed FY26 figure is modest:
standalone FOB exports Rs 1,00,347.15 lakh against Rs 91,534.41 lakh, +9.6%
(AR [page 52], txt l.4768-4770). Reading supported by the filed evidence: MM
📄 = 2.0. Adjusted total falls a further 1.0. Band unchanged.

### 2.5 FAIL detail: E8, recount integrity (MINOR)

The recount line lists "three GDAL order filings" and "one export order
filing" among the 17 📄 items. Neither appears in the Section 3 scan body
with a date, value or anchor, so the recount cannot be traced to the scored
categories. The recount also counts "the Q1 FY27 export-growth figures"
(an investor-presentation figure) as 📄, the exact 🎙️-as-📄 credit the
guard exists to catch. The guard outcome is unaffected (4 active categories,
far below 12). Fix: anchor each counted item to its category, or drop it from
the count.

### 2.6 Observations (not scored as fails)

- B2 (qualification lock-in, HM 📄 = 3.0) credits long-held certifications
  (ISO 9001:2008, IATF 16949:2016, AS9100D). The report says itself that the
  certs "do not yet prove lock-in." An emerging-moat scan credits what is
  forming; a long-held credential with no lock-in evidence sits nearer M/L
  likelihood. Judgment call; not scored.
- 6D rationale cites the "EM>=25" UA qualifier as the gate for lifting a
  combined classification. The operator ruling in prompts/07 fixes the bands
  and the UA qualifier; the combined matrix keys to EXPANSION. The outcome
  (AVERAGE) is correct either way.

Recomputed Emerging Moat: 19.4 as filed; 15.4 with the A1/R1 double credit
removed; 14.4 with the E2 tier correction as well. All three sit in 12-24,
MODEST. The EM >=25 UA qualifier is not met on any reading. Combined
assessment AVERAGE stands.

Emerging Moat tally: 18 rules checked, 4 FAIL (2 MAJOR, 2 MINOR), 14 PASS.

---

## PART 3: VALUATION (B10, B11)

PENDING PHASE 3. Not audited in this run. No valuation framework document,
B10 or B11 was read. Rules 4, 5, 7, 11, 12, 13, 14 and 15 of the Verifier C
rubric fire in phase 3. Rules 6 (B09 downstream candidates), 9 (stage 13
narrative) and 10 (B09b dossier) are outside the phase-1 scope given in the
task and were not run.

---

## SUMMARY

| Framework | Rules checked | PASS | FAIL | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 36 | 33 | 3 | 0 | 1 | 2 |
| Emerging Moat (B07) | 18 | 14 | 4 | 0 | 2 | 2 |
| Valuation (B11) | pending phase 3 | | | | | |
| Total | 54 | 47 | 7 | 0 | 3 | 4 |

Acceptance rate: 47 / 54 = 87.0%. Denominator 54 (>=4), so the rate applies.
It is above the 60% REWORK line. No CRITICAL finding. No classification
changes: Gate 0 stays AVERAGE (core 48 to 46); EM stays MODEST (19.4 to
15.4, or 14.4); combined stays AVERAGE.

Corrections the orchestrator should carry into B01/B07 consumers:
1. B01 A3 = 0 (10-year computed median ROE 11.80%); core 46, grand 54.
2. B01 M7 rationale: regulated (Arms Act licence), PEER DATA NEEDED; M8
   rationale: dealer network quantified and shrinking (157 vs 316).
3. B07 em_score 15 (R1 double credit removed), 14 with E2 corrected.
4. B07 capex_embedded_growth_pct: 41.6 per the rule (500 x 3.41 FAT on Rs
   4,100.28 Cr), with the defence-FAT reading (about 6-7%) and the CRISIL
   FY27 guide (about 12%) shown beside it as cross-checks.

```yaml
stage: B12c
company: "GOODLUCK"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase 1 (Gate 0 B01 + Emerging Moat B07); valuation pending phase 3"
gate0:
  rules_checked: 36
  fails:
    - {rule: "A3 median ROE", severity: MAJOR, stated: "13.26% (AR Key Ratios FY24-26 only) -> 2", recomputed: "11.80% (fixed formula, 10yr, screener-data NW rows 39-40) -> 0", effect: "Block A 13->11, core 48->46, grand 56->54; classification AVERAGE unchanged"}
    - {rule: "M7 regulatory/licence", severity: MINOR, stated: "unregulated, no licence gate evidenced -> 0", recomputed: "regulated (Arms Act 1959 Industrial Licence, AR [page 16] l.1074, [page 39] l.3573); player count NOT FOUND -> 0 PEER DATA NEEDED", effect: "score unchanged; rationale corrected"}
    - {rule: "M8 distribution", severity: MINOR, stated: "no distribution-reach data in corpus -> 0", recomputed: "BRSR dealers 157 FY26 vs 316 FY25, 9.30% vs 9.8% of sales (AR [page 104] l.7871-7872); quantified and shrinking -> 0 or 1", effect: "moat_score 8 or 9; moats present 2 unchanged"}
emoat:
  rules_checked: 18
  fails:
    - {rule: "one improvement one mechanism (A1/R1)", severity: MAJOR, stated: "A1 HH 4.0 and R1 HH 4.0 on the same Arms Act licence + DGQA + CRISIL quote; R1-specific policy tailwind NOT FOUND per 4B", recomputed: "R1 0 -> em 15.4 (15.9 if Atmanirbhar credited at inference tier)", effect: "MODEST unchanged; EM>=25 not met either way"}
    - {rule: "Section 2C capex x historical FAT", severity: MAJOR, stated: "method not run, 'no net-block schedule'; CRISIL FY27 guide substituted -> 12%", recomputed: "PPE 1,201.91 Cr (AR [page 188] l.13000), revenue 4,100.28 Cr (AR [page 189] l.13072), FAT 3.41x; 500 x 3.41 = 1,706 Cr = 41.6%; defence-FAT reading about 6-7% as caveat", effect: "capex_embedded_growth_pct field carries a non-defined metric; no classification change"}
    - {rule: "evidence tier consistency (E2)", severity: MINOR, stated: "E2 HM 📄 3.0 on a single-quarter presentation export figure", recomputed: "MM 📄 2.0 on filed FY26 FOB exports +9.6% (AR [page 52] l.4768-4770)", effect: "em 15.4 -> 14.4; MODEST unchanged"}
    - {rule: "completionist recount integrity", severity: MINOR, stated: "17 📄 items incl. 3 GDAL order filings, 1 export order filing, Q1 FY27 presentation export figures", recomputed: "order filings unanchored in scan body; presentation figure is 🎙️-tier", effect: "guard outcome unchanged (4 active)"}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}
business_understanding_narrative: {status: "not in phase-1 scope (stage 13)", present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: {core_score: 46, blocks: {A: 11, B: 4, C: 17, D: 8, E: 6}, moat_score: "8 or 9", grand_total: "54 or 55", moats_confirmed: 2, moat_class: "MODERATE", classification: "AVERAGE (unchanged)"}
recomputed_emoat: {em_score: "15.4 (A1/R1 fix); 14.4 (with E2 fix)", em_classification: "MODEST (unchanged)", capex_embedded_growth_pct: "41.6 per rule; 6-7 defence-FAT caveat; 12 CRISIL guide cross-check", combined_assessment: "AVERAGE (unchanged)"}
findings:
  - {severity: MAJOR, location: "01-gate0.md Block A, A3", finding: "ROE taken from AR ratios on 3 years; fixed formula computable on 10 years from screener NW; median 11.80% scores 0 not 2"}
  - {severity: MAJOR, location: "07-emoat.md Section 5, rows A1 and R1", finding: "same licence/DGQA/CRISIL evidence credited twice (8.0 of 19.4); R1 has no independent evidence"}
  - {severity: MAJOR, location: "07-emoat.md Section 2C; B07 capex_embedded_growth_pct", finding: "rule arithmetic not run on a false 'no net-block schedule' premise; rule value 41.6% vs substituted 12%"}
  - {severity: MINOR, location: "01-gate0.md Block F, M7", finding: "'unregulated' rationale contradicts the Arms Act licence in AR; should read PEER DATA NEEDED"}
  - {severity: MINOR, location: "01-gate0.md Block F, M8", finding: "'no distribution data' premise false; BRSR dealer count 157 vs 316"}
  - {severity: MINOR, location: "07-emoat.md Section 3/5, E2", finding: "H likelihood and 📄 tier rest on one presentation quarter; filed FY26 export growth +9.6%"}
  - {severity: MINOR, location: "07-emoat.md Section 3 recount line", finding: "recount includes unanchored order filings and a presentation figure as 📄"}
critical_count: 0
major_count: 3
minor_count: 4
acceptance_rate: 87.0
```
