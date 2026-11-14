# Verifier C, Framework Adherence: SUDARCOLOR, run 2026-11-12 (PHASE 1)

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation half (B10/B11; verifier rules 4, 6, 7, 11 to 15) is pending phase 3. Rule 9 (stage 13 narrative) and rule 10 (B09b dossier) fire at finalize. This verifier did not read the valuation framework documents.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, prompts/12-verifiers-pipeline.md (Verifier C section).
Artifacts read: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Lane: rule application only. Verifier A owns whether a number exists at its anchor. Every recompute below uses the stage's own stated inputs.

## Summary

- 45 rules checked: Gate 0 22, Emerging Moat 23. 35 pass, 10 fail. Acceptance rate 77.8%. The denominator is 4 or more and the rate is above 60%, so it does not trigger REWORK.
- Severity: 0 CRITICAL, 2 MAJOR, 8 MINOR. Both MAJORs are in B01.
- B01 states AVERAGE. That class rests on a substituted EBIT definition (C-G02). It also rests on a Block B that uses two missing-data rules at once (C-G09). With the fixed EBIT and one consistent window rule, the class is GOOD (core 62). The stage's AVERAGE holds only under the strict reading, where all missing-window metrics score 0. The stage did not apply that reading.
- B07 recomputes to 9.9 on its own rows. With the matrix floor on B1 it is 10.6. The class is NO MEANINGFUL EMERGING MOAT either way. The multipliers, the I1/I2 gates and the completionist recount are compliant.
- B07 6C/6D used the injected Gate 0 block correctly. If C-G02 stands under the available-window reading, the combined classification follows the Gate 0 class from AVERAGE to GOOD.

## Part 1. Gate 0 (B01) compliance

| ID | Rule (prompts/01-gate-0-pipeline.md) | Result | Stage value | Recomputed / note |
| --- | --- | --- | --- | --- |
| G01 | Rule 6: open with data-available line, scoring adapted to history | PASS | "Data available: 10 years (FY17 to FY26)" | Line present, as written |
| G02 | Fixed formula: ROCE = EBIT / (TA - CL); source ROCE first | FAIL (MAJOR) | EBIT = PBT + interest - other income; median 7.98% | EBIT = PBT + interest: median 10.2%, min 4.8% (FY19), Block A 6, DB3 off, GOOD. See finding C-G02 |
| G03 | ROE = PAT / average NW; earliest year on closing NW, stated | PASS | median 8.08%; FY17 closing NW stated | Median of the 10 stated values = (8.00 + 8.15) / 2 = 8.08% |
| G04 | WC days = receivable + inventory - payable days; basis stated | PASS | revenue basis stated | FY26 (179.39 + 156.15 - 166.33) / 780.63 x 365 = 79.1 days, matches |
| G05 | FCF = CFO - capex (PPE + intangibles, no acquisitions) | PASS | FY26 34.24 - 28.72 = 5.52 | Matches; FY25 110.59 - 11.89 = 98.70 matches |
| G06 | CAGR = (End / Start)^(1/years) - 1 | PASS | rev -2.50%, PAT 6.87% | Rev (780.63 / 980.98)^(1/9) - 1 = -2.51%; PAT 6.87%. Rounding only, bands unchanged |
| G07 | CAGR edge rules: negative endpoint N/M, loss-to-profit note, C4 N/M | PASS | all endpoints positive; "Loss-to-profit swing: none" in data_notes | Honoured |
| G08 | Block A thresholds on the stated series | PASS | A1 0, A2 0, A3 0, A4 5 = 5 | Median ROCE (6.46 + 9.50) / 2 = 7.98% < 10 = 0; min 1.00 = 0; ROE 8.08 < 12 = 0; 6.46 >= 4.11 = 5. Conditional on G02 |
| G09 | Rules 5 and 6 applied one way (missing data) | FAIL (MAJOR) | B2 5, B3 5 on FY24-FY26; B4 0 on missing FY17 | Reading 1: B4 1, Block B 16. Reading 2: B2 0, B3 0, B4 0, Block B 5. See finding C-G09 |
| G10 | Block C thresholds | PASS | C1 0, C2 1, C3 1, C4 5 = 7 | -2.51% < 5 = 0; 6.87% in 5-9.9 = 1; 5 of 9 = 55.6% = 1; +9.38pp >= 3 = 5 |
| G11 | Block D thresholds | PASS | 5, 5, 5, 5 = 20 | Net cash = 5; 38.29 / 2.52 = 15.2x = 5; 22.98 / 570.08 = 0.04 = 5; 588.08 / 203.35 = 2.89 = 5 |
| G12 | Block E thresholds | PASS | 5, 5, 0, 3 = 13 | 70.26% = 5; +15.89pp = 5 (window 2.75 years, disclosed); pledge NOT FOUND = 0 per rule 5; 50.76 / 570.08 = 8.9% = 3. See observation O1 |
| G13 | Block F band selection, M1 to M12 | FAIL (MINOR) | M8 0, "not quantified in supplied numbers" | Stated reason is the band-1 condition. See finding C-G13. M1 to M7 and M9 to M12 re-derive to 0 |
| G14 | PEER DATA NEEDED: score 0 and mark | PASS | M5 0 and marked | Segment universe not supplied; 3 of 4 in a 4-name set cannot prove top 5 in segment |
| G15 | Moat class: present at >= 3; 0 present = NONE | PASS | 0 present, NONE | Correct |
| G16 | Data confidence: 10+ years full, no downgrade | PASS | history_downgrade false | Correct |
| G17 | Classification matrix | PASS | Core 60 + NONE = GOOD before caps | "Core 60-79 + else = GOOD", correct |
| G18 | Deal-breaker tests, binding cap applied | PASS | DB3 caps at AVERAGE | DB1 fires (non-binding); DB2, DB4, DB6, DB7 (4 of 9 decline years), DB8, DB9 do not fire; DB5 not testable (pledge NOT FOUND), stated |
| G19 | Deal-breakers recorded, years named | FAIL (MINOR) | block lists DB3 only | Add DB1. See finding C-G19 |
| G20 | FLAG-GATE0 when class <= AVERAGE with depressors | PASS | flag raised, depressors named | Correct on the stage's class. Falls away if C-G02 stands under reading 1 |
| G21 | Rule 4: anchor after every extracted number | FAIL (MINOR) | several inputs unanchored | See finding C-G21 |
| G22 | Output: dashboard elements and full YAML schema | PASS | all block fields present in B01-gate0.yaml | Report ends with an abbreviated block and a pointer to the block file (observation O3) |

### Gate 0 classification recompute (two open rule readings)

The class depends on two rule readings. The stage's mix of the two is not one of the four consistent cells.

| EBIT convention / missing-data reading | Stage mix (B2, B3 on FY24-26; B4 = 0) | Reading 1: available window for all (B4 = 1) | Reading 2: NOT FOUND = 0 for all (B2 = B3 = B4 = 0) |
| --- | --- | --- | --- |
| Stage: PBT + interest - other income | A 5, B 15, core 60; DB1, DB3; AVERAGE (stage value) | A 5, B 16, core 61; DB1, DB3; AVERAGE | A 5, B 5, core 50; DB1, DB2, DB3; AVERAGE |
| Fixed: PBT + interest | A 6, B 15, core 61; DB1; GOOD (stage sensitivity) | A 6, B 16, core 62; DB1; GOOD | A 6, B 5, core 51; DB1, DB2; AVERAGE |

Governing cell on the rules as written: fixed EBIT with reading 1, which gives GOOD (core 62). Two caveats bind that cell. First, the stage used TA minus other liabilities as the capital-employed proxy, because the data sheet has no current-liability split for FY17 to FY25. The fixed TA minus CL median is NOT FOUND from B01's inputs. The 10.2% median sits 0.2pp above the DB3 line. Second, the 10.2% median and the 4.8% minimum come from the stage's sensitivity line. The yearly values behind them are not shown, so this verifier cannot re-derive A4 under that convention.

## Part 2. Emerging Moat (B07) compliance

| ID | Rule (prompts/07-emerging-moat-pipeline.md; verifier rules 3 and 8) | Result | Stage value | Recomputed / note |
| --- | --- | --- | --- | --- |
| E01 | All 23 categories addressed or NO EVIDENCE FOUND | PASS | 22 in Section 3, R1 in Section 4 | All 22 rows in the summary table; R1 scored in Section 4C and Section 5 |
| E02 | Evidence taxonomy applied to every item | PASS | tier marked on each item | Product launches, registration, BRSR measures and balance-sheet facts are documented; letters and MD&A forward text are claims |
| E03 | Rule 3: source anchor on every evidence item | FAIL (MINOR) | two AR FY25 cites have no page | See finding C-E03 |
| E04 | Matrix floor (LL = 1 for any evidence); NO EVIDENCE FOUND only where none | FAIL (MINOR) | B1 0 with a quoted claim | 0.7; EM 10.6; NONE unchanged. See finding C-E04 |
| E05 | L x I values match the matrix | PASS | A1 LL 1, A3 LL 1, C1 MM 2, G1 ML 1, H2 MH 3, H3 HL 2, R1 MM 2 | All match "HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1" |
| E06 | Evidence multipliers (documented 1.0, claim 0.7, inference 0.5) | PASS | 1.0 on A1, A3, G1, H3; 0.7 on C1, H2, R1 | H2 taken at 0.7 because the benefit is claimed although the acquisition is documented. That is the stricter tier and complies |
| E07 | Adjusted total | PASS | 9.9 | 1.0 + 1.0 + 1.4 + 1.0 + 2.1 + 2.0 + 1.4 = 9.9 |
| E08 | Bands absolute, no rescale (operator ruling 20-Aug-2026) | PASS | NONE | 9.9 < 12 = NO MEANINGFUL EMERGING MOAT |
| E09 | I1/I2 contribution stated separately | PASS | 0.0 | Stated; "Not a threshold crosser via I1/I2" |
| E10 | Category 21 (I1) present; > 0 only with both legs and a documented (b) leg | PASS | 0, both legs absent | Compliant |
| E11a | Category 22 (I2) present; > 0 only with a named, specific sacrifice | PASS | 0, "execution lead at best" | Compliant |
| E11b | I2 question answered for each claimed moat | FAIL (MINOR) | one sentence for the business | See finding C-E11b |
| E12 | Completionist guard: recount line in the stated form | PASS | "📄 recount performed: 9 documented items across 6 categories" | Line present; 7 scored categories, under 12 |
| E13 | Recount accuracy | FAIL (MINOR) | R1 credited "NIR launch" | See finding C-E13 |
| E14 | Scores consistent with evidence tiers (no claim-only row scored as documented) | PASS | C1 and R1 at 0.7; H2 at 0.7 | No claim-only row carries the 1.0 multiplier. See observation O5 on H3 |
| E15 | Section 3 summary table and Strong/Moderate count | PASS | Strong 0, Moderate 1 (H2) | active_categories carries H2 only, as the block schema requires |
| E16 | Section table schemas as written | FAIL (MINOR) | columns and rows short | See finding C-E16 |
| E17 | 2C arithmetic shown: capex under execution x FAT | PASS | 7.63 x 5.71 = 43.6 Cr = 5.6% | 780.63 / 136.67 = 5.71x; 43.6 / 780.63 = 5.6%. See observation O2 on the FAT basis |
| E18 | Optionality register: 0 or claim/inference-only rows, four columns, in block, not scored | PASS | 5 rows | Each row has converting evidence, first-appearance point and window. C1 and the H2 synergies sit on the register and in the score. Both rest on claims only, which the register definition allows |
| E19 | 6C uses the injected Gate 0 block | PASS | core 60, AVERAGE, 0 moats, NONE | Matches B01-gate0.yaml |
| E20 | 6D label from the named set; HIGH POTENTIAL and TURNAROUND test | PASS | AVERAGE; both rows tested and rejected | EM 9.9 < 25 rules out both. The matrix cells are not in the supplied rule source (observation O6) |
| E21 | 6A four windows; 6B early warnings; 6E evolution map, catalysts, biggest risk | PASS | all present | Compliant |
| E22 | YAML block schema complete; analyst_note under 200 words | PASS | all fields present | Note about 110 words |

## Part 3. Valuation (B10/B11)

PENDING PHASE 3. The artifacts do not exist yet. This verifier did not run rules 4, 6, 7 and 11 to 15. The expectation_ledger and business_narrative block fields are null, not false. A null means "not checked". It is not a fail.

## Findings

**C-G02 (MAJOR), B01 ROCE formula substitution.**
The rule text reads: "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" and "ROCE = EBIT ÷ (Total Assets − Current Liabilities)... If the data source provides its own ROCE (screener.in does), use the source's figure". The stage defined EBIT as PBT plus interest minus other income (B01 line 12). EBIT means earnings before interest and tax, which is PBT plus interest. The rule's first choice is the screener ROCE, and screener includes other income. To remove other income is a different definition. It is also a judgment the gate bars ("No qualitative judgments", operating rule 2).
- Stage value: median 7.98%, Block A 5, DB3 fires, AVERAGE.
- Recomputed on the stage's own sensitivity (B01 line 18; data_notes): median 10.2%, minimum 4.8% (FY19). A1 1, A2 0, A3 0, A4 5, so Block A is 6. DB3 does not fire. DB1 caps at GOOD and does not bind. Core is 61, or 62 with the C-G09 fix. The class is GOOD. FLAG-GATE0 then has no trigger, because that flag needs a class of AVERAGE or lower.
- Unchanged: D2 is 60.14 / 2.52 = 23.9x, still 5. M3 still scores 0, because FY26 ROCE of 10.1% is under the 12% bar.
- Severity: MAJOR, not CRITICAL. Gate 0 does not halt the run, and the stage showed both readings in its FLAG-GATE0 text. The class flip changes a flag and the B07 combined label. It does not change a decision.

**C-G09 (MAJOR), B01 missing-data rule applied two ways.**
The stage scored B2 and B3 on FY24 to FY26 because capex before FY24 is NOT FOUND. That applies rule 6, which allows a 3-year minimum. It scored B4 at 0 because FY17 payables are NOT FOUND. That applies rule 5, although FY24 to FY26 WC days are stated. Block B 15 fits neither reading.
- Reading 1 (available window for all three): B4 = 66.4 days (FY24) to 79.1 days (FY26) = +12.7, in the "increased 5-15" band, so 1. Block B is 16 and core is 61 or 62.
- Reading 2 (NOT FOUND = 0 for all three): B2, B3 and B4 are 0. Block B is 5 and DB2 fires. Core is 50 or 51, and the class is AVERAGE under both EBIT conventions.
- Reading 1 has the better evidence. The rule 6 minimum is 3 years, and the stage already applied it to B2 and B3. The choice also decides whether C-G02 moves the class.

**C-G13 (MINOR), B01 M8 band.**
The band text reads "mentioned unquantified = 1 | none or purely digital = 0". The stage scored 0 with the reason "not quantified in supplied numbers", and that reason is the band-1 condition. B07 cites a reach statement: exports "to more than 75 countries" through associated entities (AR FY26 p.17). If that statement was in B01's inputs, M8 is 1. The moat score is then 1, the grand total 61, and the class stays NONE. M8 is not a peer test, so the PEER DATA NEEDED tag on it is wrong.

**C-G19 (MINOR), B01 deal-breaker record.**
The block's deal_breakers lists DB3 only. DB1 (Block A 5 < 8, max GOOD) also fires and does not bind. The years that drive it are FY17 to FY20, at 1.00% to 4.11% ROCE. The sensitivity line says "no cap", but DB1 still caps that reading at GOOD, again without binding.

**C-G21 (MINOR), B01 anchors.**
These numbers have no inline anchor: the C1 and C2 endpoints (980.98, 780.63, 24.48, 44.53), D2 EBIT 38.29 and interest 2.52, D3 net worth 570.08, M3 FAT 4.72x, M9 39.26% and 42.71%, M11 selling 6.80% and 8.93%, and E2 54.37% (Dec 2023). FY24 and FY25 payables carry "AR FY25 p.65 area". All are Gate 0 scorecard inputs, in the OR-32 mandatory tier. Verifier A decides whether each one exists at a source.

**C-E03 (MINOR), B07 anchors.**
Two AR FY25 cites carry no page: "(line ref. MD&A innovations)" in the 1A NIR row and "(MD&A, India Speciality Chemical Industry)" under E2. The stage did not score either item.

**C-E04 (MINOR), B07 B1 label and matrix floor.**
B1 reads "NO EVIDENCE FOUND", then quotes a management claim: "forward, backward, and lateral integration have strengthened supply reliability" (AR FY26 p.17). The matrix gives LL = 1 to any evidence, so a claim scores at least 1 x 0.7 = 0.7. The stage's reason for 0 is that group purchases rose to 99.62 from 45.38 (AR FY26 p.93), which contradicts the claim. The reason is sound, but the rule has no "contradicted claim = 0" clause. C1 is also an unquantified claim, and it scored 1.4. The recompute gives B1 0.7 and an EM total of 10.6. The class stays NONE, 1.4 points under the 12 edge.

**C-E11b (MINOR), B07 I2 per-moat answer.**
The rule asks the I2 question "For each moat claimed anywhere in this scan". The stage answered once for the whole business. The answer for H2, the only Moderate row, is missing: what would a rival have to destroy to copy access to the group platform? I2 stays 0, because buying a global group is capital spend, not a sacrifice. The rule still asks for that answer to be written.

**C-E13 (MINOR), B07 recount attribution.**
The recount gives R1 one documented item, "NIR launch". Section 4 lists no NIR item. Its only documented item is the EPA registration of Novotex Red ARCY (AR FY26 p.11), and the recount already counts that under A1. On Section 4 as written, the recount is 8 items across 5 categories. It is 9 across 6 only if Section 4 shows the NIR link to a regulation. The score does not change, because R1 carries the 0.7 claim multiplier.

**C-E16 (MINOR), B07 table schemas.**
- 1C has no "profitability impact" column.
- 2A has no "% over current" column.
- Section 3 gives one prose line per category, not "evidence table or NO EVIDENCE FOUND".
- Section 5 folds 16 zero rows into one line, but the rule asks for "all 23 rows".

The Section 3 summary table shows the zero rows. The missing columns would read NOT FOUND.

## Observations (not counted, no score change)

- O1. B01 line 9 says the 15.89% transfer from Sudarshan Europe to Sudarshan Chemical left the "promoter total unchanged". E2 scores a +15.89pp rise (54.37% Dec 2023 to 70.26% Sep 2026), and data_notes says "Rise is an intra-group transfer". Both statements cannot hold for one holding measure. The Dec 2023 base predates the Heubach acquisition (completed 3 Mar 2025, B07 H2). [INFERENCE] The stake may have entered the promoter category through an earlier acquisition, and note 10 may record a later internal move. B01 does not show which. E2 = 5 is mechanical and stands. The meaning of the rise does not. If the promoter bought from the public, the rise signals alignment. If the rise is an internal move, it signals nothing. Route this to Verifier A and the operator.
- O2. FY26 fixed-asset turnover is 4.72x in B01 (M3) and 5.71x in B07 (2C, revenue / net PPE 136.67). Nobody reconciled the two figures. On 4.72x, capex-embedded growth is 7.63 x 4.72 = 36.0 Cr = 4.6%, against the stage's 5.6%. Neither figure crosses a threshold.
- O3. The report 01-gate0.md ends with a 6-field YAML extract and a pointer line. The full schema is at outputs/blocks/B01-gate0.yaml, the path the orchestrator reads.
- O4. B01 sorts ROCE years FY17 to FY20 at 1.00% to 4.11%, before the group change of control. The rules treat every year the same. A post-acquisition rebase is a downstream position-sizing question, as Gate 0's deal-breaker note allows. It is not a scoring question.
- O5. H3 cites "Cuddalore 62% to 75%" from the MD letter (AR FY26 p.10). If that is a forward target, it is a claim, not a documented item. H3 keeps its 1.0 multiplier on the other two items (58% renewable, Nagda ZLD). The score does not change.
- O6. The 6D "standard matrix" cells are not in prompts/07. This verifier checked the label against the named set and the HIGH POTENTIAL and TURNAROUND conditions only.

## Operator questions (rule readings this run cannot settle)

- Q1. Gate 0 EBIT for cash-rich names: should EBIT be PBT plus interest, as the fixed formula and screener precedence say? Or should it be operating EBIT without other income? Here the choice moves the class between AVERAGE and GOOD.
- Q2. Gate 0 missing data inside the scored window: should a metric score on its available years (3 or more), or score NOT FOUND = 0? Here the choice moves Block B between 16 and 5.
- Q3. Emerging Moat: does a claim that documented data contradicts score LL x 0.7, or 0? A written rule makes B1 and C1 carry the same bar.

## Propagation

- B07 6C/6D: correct on the injected block. If the operator upholds C-G02 under reading 1, combined_assessment moves from AVERAGE to GOOD. The EM score of 9.9 qualifies for no HIGH POTENTIAL or TURNAROUND cell.
- FLAG-GATE0: lapses if the class becomes GOOD. FLAG-CASH does not depend on the class. B01 records Block B as deteriorating, with CFO 110.59 (FY25), 34.24 (FY26) and -24.11 (H1 FY27).

```yaml
stage: B12c
company: "SUDARCOLOR"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "PHASE 1 ONLY: Gate 0 (B01) and Emerging Moat (B07). Valuation half (B10/B11, rules 4, 6, 7, 11-15) and rules 9-10 not run; pending phase 3 / finalize."
gate0:
  rules_checked: 22
  fails:
    - "G02 MAJOR: ROCE EBIT taken as PBT + interest - other income; fixed formula EBIT is PBT + interest, source (screener) ROCE first. Recomputed on the stage's own sensitivity: median 10.2%, Block A 6, DB3 off, GOOD."
    - "G09 MAJOR: B2/B3 scored on the FY24-FY26 available window, B4 zeroed for missing FY17 payables. Block B 15 fits neither consistent reading: 16 (available window, B4 = 1) or 5 (NOT FOUND = 0 for all three)."
    - "G13 MINOR: M8 reason 'not quantified' names the band-1 condition ('mentioned unquantified = 1') but scores 0."
    - "G19 MINOR: block deal_breakers omits DB1 (Block A 5 < 8, max GOOD, non-binding); report line 65 says 'no cap' where DB1 still applies."
    - "G21 MINOR: several Gate 0 scorecard inputs carry no inline anchor (C1/C2 endpoints, D2 EBIT and interest, D3 net worth, M3, M9, M11, E2 start value)."
  recomputed_classification: "GOOD under the fixed EBIT definition with the available-window reading (core 62, DB1 non-binding, DB3 off). AVERAGE only under the strict NOT-FOUND-equals-0 reading (core 50 or 51, DB2 fires), which the stage did not apply. Stage value AVERAGE. Fixed TA - CL denominator NOT FOUND in B01 inputs; recomputed median sits 0.2pp over the DB3 line."
emoat:
  rules_checked: 23
  fails:
    - "E03 MINOR: two AR FY25 citations carry no page (1A NIR row, E2 line)."
    - "E04 MINOR: B1 labelled NO EVIDENCE FOUND while citing a management claim (AR FY26 p.17); matrix floor LL = 1 x 0.7 = 0.7 gives EM 10.6, class NONE unchanged."
    - "E11b MINOR: I2 answered once for the whole business, not per claimed moat (A1, A3, C1, G1, H2, H3, R1). I2 stays 0."
    - "E13 MINOR: recount assigns a documented item to R1 ('NIR launch') that Section 4 does not list; Section 4's only documented item (EPA registration) is already counted under A1. 8 or 9 items; no score effect."
    - "E16 MINOR: table schemas short of the text (1C no profitability-impact column, 2A no '% over current' column, Section 3 prose not evidence tables, Section 5 collapses 16 zero rows)."
  recomputed_em_score: "9.9 concur on the stated rows; 10.6 with the B1 matrix floor; NONE either way (band edge 12)."
  propagation_note: "B07 6C/6D used the injected Gate 0 AVERAGE correctly. If G02 is upheld under the available-window reading, combined_assessment follows the Gate 0 class to GOOD (EM 9.9, no HIGH POTENTIAL or TURNAROUND cell)."
valuation: {rules_checked: 0, fails: [], scope: "PENDING PHASE 3 (B10/B11 not yet produced; valuation framework documents not loaded)"}
expectation_ledger: {scope: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {scope: "PENDING (stage 13 not run; rule 9 fires at finalize)", present: null, five_questions: null, prose_only: null, downstream_refs: null, no_valuation_vocab: null, fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # phase 3
recomputed_decision: ""        # no decision-bearing output in phase-1 scope; Gate 0 class recompute is in gate0.recomputed_classification
findings:
  - {id: "C-G02", stage: "B01", severity: "MAJOR", rule: "Gate 0 FORMULA DEFINITIONS (fixed, do not substitute): ROCE = EBIT / (Total Assets - Current Liabilities); use the source's ROCE (screener) when present", stage_value: "EBIT = PBT + interest - other income; median ROCE 7.98%; A1 0; Block A 5; DB3 fires; core 60; AVERAGE", recomputed: "EBIT = PBT + interest (the stage's own sensitivity, B01 line 18 and data_notes): median 10.2%, min 4.8% (FY19); A1 1, A2 0, A3 0, A4 5; Block A 6; DB3 off; DB1 caps at GOOD (non-binding); core 61, or 62 with the C-G09 available-window fix; GOOD; FLAG-GATE0 trigger (class <= AVERAGE) not met. D2 23.9x and M3 0 unchanged.", note: "Removing other income is a substituted definition and a judgment the Gate 0 rules bar (rule 2, no qualitative judgments). The stage disclosed both readings in FLAG-GATE0, so the decision likely survives. Denominator: stage used TA - other liabilities as a proxy; the fixed TA - CL median is NOT FOUND from B01 inputs and the 10.2% median sits 0.2pp over the line. Operator question Q1."}
  - {id: "C-G09", stage: "B01", severity: "MAJOR", rule: "Gate 0 operating rule 5 (data point not available = NOT FOUND, score 0) and rule 6 (use available history, minimum 3 years), applied one way across the scorecard", stage_value: "B2 5 and B3 5 scored on FY24-FY26 (capex FY17-FY23 NOT FOUND); B4 0 because FY17 payables NOT FOUND although FY24-FY26 WC days are stated; Block B 15", recomputed: "Reading 1, available window for all: B4 = FY24 66.4 to FY26 79.1 days = +12.7 = band 'increased 5-15' = 1; Block B 16; core 61 (stage EBIT, AVERAGE via DB3) or 62 (fixed EBIT, GOOD). Reading 2, NOT FOUND = 0 for all: B2 0, B3 0, B4 0; Block B 5; DB2 fires (max GOOD); core 50 (stage EBIT) or 51 (fixed EBIT); AVERAGE under both.", note: "Block B 15 is supported by neither consistent reading. The reading also decides whether C-G02 moves the class. Reading 1 is the better-evidenced one (rule 6 minimum is 3 years and the stage already applied it to B2/B3). Operator question Q2."}
  - {id: "C-G13", stage: "B01", severity: "MINOR", rule: "M8 Distribution bands: reach quantified and growing = 5 | network growing and rev CAGR >= 15% = 3 | mentioned unquantified = 1 | none or purely digital = 0", stage_value: "M8 0, reason 'distribution not quantified in supplied numbers'; M8 also listed under PEER DATA NEEDED", recomputed: "1 if any distribution statement was in the B01 inputs (B07 cites 'exports to more than 75 countries through associated entities', AR FY26 p.17); moat score 0 to 1; grand total 60 to 61; moats present 0, class NONE unchanged", note: "The stated reason names the band-1 condition while the score is band 0. M8 is not a peer test, so the PEER DATA NEEDED tag is wrong."}
  - {id: "C-G19", stage: "B01", severity: "MINOR", rule: "Deal-breaker overrides: record them and state which years drive each", stage_value: "block deal_breakers lists DB3 only; report classification box names DB1 in prose; sensitivity line 65 says 'no cap'", recomputed: "deal_breakers should add DB1 (Block A 5 < 8, max GOOD, non-binding under DB3, driven by FY17-FY20 ROCE 1.00-4.11%). Under the sensitivity DB1 still caps at GOOD (non-binding).", note: "presentational; class unchanged"}
  - {id: "C-G21", stage: "B01", severity: "MINOR", rule: "Gate 0 operating rule 4: every extracted number immediately followed by its source", stage_value: "no inline anchor on C1/C2 endpoints (980.98, 780.63, 24.48, 44.53), D2 EBIT 38.29 and interest 2.52, D3 net worth 570.08, M3 FAT 4.72x, M9 39.26%/42.71%, M11 selling 6.80%/8.93%, E2 54.37% (Dec 2023); FY24-FY25 payables anchored 'AR FY25 p.65 area'", recomputed: "n/a", note: "These are Gate 0 scorecard inputs, the OR-32 mandatory tier. Existence is Verifier A's call, not this verifier's."}
  - {id: "C-E03", stage: "B07", severity: "MINOR", rule: "Stage 7 operating rule 3: source anchor on every evidence item", stage_value: "AR FY25 cited as '(line ref. MD&A innovations)' in the 1A NIR row and '(MD&A, India Speciality Chemical Industry)' under E2, no page", recomputed: "n/a", note: "weak anchors; neither item is scored"}
  - {id: "C-E04", stage: "B07", severity: "MINOR", rule: "Section 5 matrix: LL = 1 for any evidence, no evidence = 0; operating rule 5 reserves NO EVIDENCE FOUND for categories with none", stage_value: "B1 labelled NO EVIDENCE FOUND while quoting a management claim ('forward, backward, and lateral integration have strengthened supply reliability', AR FY26 p.17); scored 0", recomputed: "B1 LL 1 x 0.7 = 0.7; EM total 9.9 to 10.6; class NONE unchanged (band edge 12)", note: "The stage gave a reason (claim contradicted by group purchases 99.62 vs 45.38, AR FY26 p.93). The label and the zero depart from the text, not the reasoning. C1, an unquantified claim, scored 1.4 on the same tier, so the bar needs one written rule. Operator question Q3."}
  - {id: "C-E11b", stage: "B07", severity: "MINOR", rule: "I2: 'For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy'", stage_value: "one sentence for the whole business ('would destroy nothing in its own P&L')", recomputed: "I2 stays 0", note: "Per-moat answer missing for the seven scored rows; H2 (the only Moderate row) is the one that matters."}
  - {id: "C-E13", stage: "B07", severity: "MINOR", rule: "Completionist guard: 'Recount the documented items specifically before finalising the scorecard'", stage_value: "9 documented items across 6 categories, with R1 credited one item ('NIR launch')", recomputed: "Section 4 lists no NIR item; its only documented item is the EPA registration (AR FY26 p.11), already counted under A1. 8 items across 5 categories on Section 4 as written; 9 across 6 only if Section 4 is amended to show the NIR link.", note: "No score effect: R1 is scored at the 0.7 claim multiplier and the 12-category guard is far away."}
  - {id: "C-E16", stage: "B07", severity: "MINOR", rule: "Section schemas as written: 1C columns, 2A columns, Section 3 'evidence table or NO EVIDENCE FOUND', Section 5 'all 23 rows'", stage_value: "1C has no profitability-impact column; 2A has no '% over current' column; Section 3 is one prose line per category; Section 5 collapses 16 zero rows into one line", recomputed: "n/a", note: "Presentational. The zero rows appear in the Section 3 summary table; the missing columns would read NOT FOUND."}
critical_count: 0
major_count: 2
minor_count: 8
acceptance_rate: 77.8             # 35 passed / 45 checked (Gate 0 17/22, Emerging Moat 18/23); denominator >= 4, above 60%, no REWORK trigger
```
