# VERIFIER C: FRAMEWORK ADHERENCE, TLL, run 2026-09-26 (PHASE 1 SCOPE)

Model: claude-opus-5-5. Scope: Gate 0 (B01) and Emerging Moat (B07) only.
The valuation audit (B10, B11; verifier rules 4-7 and 9-15) is pending
phase 3. No valuation framework document was loaded.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Re-derivation inputs: inputs/screening/screener-Data_Sheet.csv and the
CAPLIPOINT, SENORES, INNOVACAP Data_Sheet.csv files (INR Cr);
inputs/annual-report/Annual_Report_2026.txt (INR lakh);
inputs/shareholding/screener-shareholding-pattern.csv.
Not opened: outputs/superseded/, outputs/final/.

This audit covers rule application only. Verifier A owns whether each number
exists in the source. Figures below were used only to re-run the scoring
rules.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

### 1a. Block re-derivation

| # | Rule | B01 value / score | Recomputed from stated inputs | Verdict |
|---|---|---|---|---|
| 1 | Opening "Data available" statement | 5 yrs FY22-FY26, windows stated per row | Present at line 12; a rework preamble precedes it; wording "Scoring adapted" is paraphrased | PASS (note) |
| 2 | ROCE formula; source ROCE used if provided | Computed, stated "computed" | Data_Sheet has no ROCE row (screener-Data_Sheet.csv rows 9-63), so computing is correct | PASS |
| 3 | A1 median ROCE | 17.33% -> 3 | FY24 (8.69+0.65)/(87.08-20.26) = 13.98%; FY25 17.76/(156.01-53.55) = 17.33%; FY26 31.31/(236.83-87.89) = 21.02% (CL 8,789.27 L, AR2026 line 9998). Median 17.33 -> band 15-19.9 = 3 | PASS |
| 4 | A2 min ROCE | 13.98% -> 3 | Band 12-14.9 = 3 | PASS |
| 5 | A3 median ROE, average net worth | 23.6% -> 5 | FY23 6.02/avg(4.78,45.64) = 23.9%; FY24 12.9%; FY25 11.75/avg(52.90,64.46) = 20.0%; FY26 19.04/avg(64.46,96.68) = 23.6%; FY22 closing-only 82.6% (rule permits, stated). Median 23.6 -> 5. Ex-FY22 median 21.8, same band | PASS |
| 6 | A4 ROCE trend | 21.02 vs 13.98 -> 5 | Latest >= earliest -> 5 | PASS |
| 7 | B1 cum CFO / cum PAT | -0.478 -> 0 | -22.53 / 47.10 = -0.478 -> <0.50 = 0 | PASS |
| 8 | B2 FCF-positive years | 0% -> 0 | FY24-26 defined FCF (CFO - Purchase of Fixed Assets) all negative; FY22-23 proxy. CFO is negative in FY22 (-0.21) and FY23 (-19.00), so FCF is negative on any capex >= 0. Proxy is not load-bearing | PASS |
| 9 | B3 cum FCF / cum PAT | -2.05 -> 0 | -96.69 / 47.10 -> negative = 0 | PASS |
| 10 | B4 change in WC days | +51.7 -> 0 | Payables AR2026 lines 9985-9986 (3,843.48 L FY26; 1,478.83 L FY25). FY26 rec 208.4 + inv 103.1 - pay 108.7 = 202.8; FY24 151.1. +51.7 -> >15 = 0 | PASS |
| 11 | C1 revenue CAGR | 56.05% -> 5 | (129.02/21.77)^(1/4) - 1 = 56.0% -> 5 | PASS |
| 12 | C2 PAT CAGR | 48.16% -> 5 | (19.04/3.95)^(1/4) - 1 = 48.2% -> 5 | PASS |
| 13 | C3 positive YoY years | 4/4 -> 5 | All four YoY positive -> 5 | PASS |
| 14 | C4 PAT CAGR - Rev CAGR | -7.89pp -> 1 | Inside -3 to -8pp -> 1 (0.11pp from the 0 band) | PASS |
| 15 | D1 ND/EBITDA | 2.45x -> 1 | 68.77/28.11 = 2.45x -> 1 on operating EBITDA. On all-in EBITDA 37.38 Cr: 1.84x -> 3 | PASS (note, finding G3) |
| 16 | D2 interest cover | 7.60x -> 4 | 31.31/4.12 = 7.60 -> 4 | PASS |
| 17 | D3 D/E | 0.76x -> 3 | 72.99/96.68 = 0.755 -> 3; same band on 100.40 and 104.17 bases | PASS |
| 18 | D4 current ratio | 1.59x -> 4 | 13,951.49 / 8,789.27 L (AR2026 lines 10087, 9998) = 1.587 -> 4 | PASS |
| 19 | E1 promoter holding | 62.59% -> 5 | Jun-2026 62.59% (shareholding CSV row 3) -> 5 | PASS |
| 20 | E2 promoter change ~3 yrs | -7.45pp -> 0 | Sep-2023 70.04% is the earliest column (2.75 yrs); decrease >3 on any reading -> 0 | PASS |
| 21 | E3 pledge | NOT FOUND -> 0 | Rule 5: unavailable = 0, no estimate | PASS |
| 22 | E4 contingent liabilities / NW | 5.17% -> 3 | 500.00 L consolidated guarantees (AR2026 line 13914) / 96.68 Cr = 5.17% -> 3. Boundary-sensitive: 4.98% on screener NW 100.40, 4.80% on NW incl. MI 104.17 -> 5 | PASS (note, finding G4) |

Core on the stated bases: A16 + B0 + C16 + D12 + E8 = 52. Concur.

### 1b. Block F moat tests

| # | Test | B01 | Recomputed | Verdict |
|---|---|---|---|---|
| 23 | M1 pricing power | 5 | Op. EBITDA margin 12.5% (FY22) to 21.8% (FY26), +9.3pp, rev CAGR 56% -> 5 | PASS |
| 24 | M2 cost advantage | 0 | Peer FY26 op. EBITDA margins: CAPLIPOINT 765.03/2,187.19 = 34.98%; SENORES 168.32/632.63 = 26.61%; INNOVACAP 242.92/1,630.02 = 14.90%. Median 26.61. TLL 21.8 is 4.8pp below -> 0 | PASS |
| 25 | M3 capital efficiency | 3 | FAT 129.02/60.73 = 2.12x; ROCE 21.02% -> FAT>2 and ROCE>15 = 3 | PASS |
| 26 | M4 customer stickiness | 3 | Zero decline years fails tier 5 (receivable days not stable); tier 3 "max 1 decline year" met literally -> 3 | PASS |
| 27 | M5 scale and dominance | 1 | Peer set holds 3 names. TLL ranks 4th of 4. A 4-name set cannot show rank in the segment, so "top 5 mcap" is not established. Recomputed 0, PEER DATA NEEDED (segment universe) | FAIL (MINOR, G1) |
| 28 | M6 technology / R&D | 0 | No R&D line; margin below peer median, so tier 1 also fails -> 0 | PASS |
| 29 | M7 regulatory / licence | 1 | Regulated, >10 listed players -> 1 | PASS |
| 30 | M8 distribution | 1 | Mentioned, unquantified -> 1 | PASS |
| 31 | M9 brand | 0 | GM proxy (Rev - RM)/Rev: TLL 46.4%; CAPLIPOINT 57.5%, SENORES 60.2%, INNOVACAP 48.6%, median 57.5 -> below -> 0. Proxy stated, same basis for peers | PASS |
| 32 | M10 switching costs | 0 | Grew every year, receivable days +98 (FY24-26), tier 5 and tier 3 fail on the stability leg; tier 1 needs 2+ decline years -> 0 | PASS |
| 33 | M11 network effects | 1 | <6 yrs, fallback stated; CAGR 56%, selling % 3.9% (FY22) to 6.3% (FY25) rising -> 1 | PASS |
| 34 | M12 negative WC / float | 0 | WC days 151-203, >45 -> 0 | PASS |
| 35 | Moat classification | 3 present, MODERATE | M1, M3, M4 >= 3; count 3 -> 2-3 = MODERATE. After M5 fix moat_score 14, class unchanged | PASS |

### 1c. Classification, overrides, edge rules, schema

| # | Rule | B01 | Audit | Verdict |
|---|---|---|---|---|
| 36 | Data confidence / history downgrade | 5 yrs, "5-6 lower" flag, history_downgrade false | The rule keys to years of history (5), not per-metric sub-windows. The 3-year ROCE/WC window is a stated input gap. Literal reading holds | PASS |
| 37 | Classification matrix | Core 52 -> AVERAGE | 40-59 band does not branch on moat class -> AVERAGE. Holds at Core 54-56 on alternative D1/E4 bases | PASS |
| 38 | Deal-breaker application | #2 (max GOOD), #4 (max AVERAGE) triggered; others not | Re-run all nine: #1 A=16 no; #2 B=0 yes; #3 17.33% no; #4 -0.478 yes; #5 pledge NOT FOUND, cannot trigger; #6 2.45x and 7.60x no (1.84x on all-in basis, still no); #7 no; #8 PAT positive FY24-26 no; #9 no. Binding cap AVERAGE | PASS |
| 39 | Deal-breaker year attribution | Not stated in the deal-breaker block | Rule: "state WHICH years drive any deal-breaker". Years appear only in LBF1 prose. Recomputed below | FAIL (MINOR, G2) |
| 40 | CAGR edge rules | No negative endpoints, no swing | FY22 PAT 3.95 and FY26 19.04 both positive; no loss-to-profit swing; C4 not N/M | PASS |
| 41 | FLAG-GATE0 when <= AVERAGE with depressors | Present | Present with reason | PASS |
| 42 | YAML schema, analyst_note <= 200 words | All keys present, extra rework keys | analyst_note about 165 words; extra keys are additive | PASS |

Gate 0: 42 rules checked, 40 passed, 2 FAIL. Acceptance 95.2%.

### 1d. Gate 0 findings

**G1 (MINOR). M5 scored on a degenerate peer set.** The test reads "top 5 mcap"
in the segment. B01 has only three peers (CAPLIPOINT, SENORES, INNOVACAP,
Data_Sheet row 8). TLL ranks last of four. In a four-name set every name is
"top 5", so the test cannot fail. That gives no evidence of segment rank. The
rule says score 0 and mark PEER DATA NEEDED when peer data is not provided.
Recomputed: M5 = 0, moat_score 15 -> 14, grand total 67 -> 66. Moats
confirmed stay 3; class stays MODERATE; classification stays AVERAGE.

**G2 (MINOR). Deal-breaker years not attributed.** The rule asks the stage to
state which years drive each deal-breaker, so downstream sizing can judge a
post-IPO rebase case. B01 lists #2 and #4 with no years. Recomputed for #4:
cumulative CFO -22.53 Cr comes from FY22 -0.21, FY23 -19.00, FY25 -10.24,
offset by FY24 +2.23 and FY26 +4.69 (screener-Data_Sheet.csv row 57). FY23,
the IPO year, is 84% of the total. With FY23 removed, CFO/PAT = -3.53/41.08
= -0.086. The trigger still holds. The cap is not a single-year IPO artefact.
#2 (Block B 0/20) is driven by all years on B1-B3 and by FY24-FY26 on B4.

**G3 (MINOR, PASS WITH NOTE). D1 basis sensitivity not disclosed.** Rework item
12 rules that an unqualified "EBIT" means PBT + Interest. D1 then uses
operating EBITDA (28.11 Cr, excluding Other Income 9.27 Cr). The prompt does
not define EBITDA, and the operating basis matches M1 and M2, so the choice
is defensible and stated. But the score is basis-sensitive. On all-in EBITDA
(27.19 + 4.12 + 6.07 = 37.38 Cr) ND/EBITDA = 1.84x, band 1-2x = 3, not 1.
Core would be 54. Classification unchanged. B01 should state the sensitivity.

**G4 (MINOR, PASS WITH NOTE). E4 sits on the 5% band edge.** E4 = 5.17% on parent
equity 96.68 Cr, which excludes share application money 372.67 L and
minority interest 749.02 L (AR2026 lines 9942, 9949). Both exclusions are
correct under the stated single-basis ruling. On screener net worth 100.40
Cr the ratio is 4.98% and E4 = 5. On net worth with MI, 104.17 Cr, it is
4.80% and E4 = 5. Rework item 16 says "none of the three scores changes
band"; that is true against run 1, but the band edge is not disclosed. With
G3, Core could reach 56. Still AVERAGE, and deal-breaker #4 binds on every
basis.

Recomputed Gate 0 card: Core 52 (54-56 on alternative D1/E4 bases), moat 14,
MODERATE, AVERAGE. The classification is robust to every finding above.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 | Audit | Verdict |
|---|---|---|---|---|
| 1 | All six sections present | 1A-1C, 2A-2D, 3, 4A-4C, 5, register, 6A-6E | Complete | PASS |
| 2 | Evidence taxonomy applied | Tags on scan items | Applied across Sections 1, 3, 5 | PASS |
| 3 | Source anchor on every evidence item | Many primary anchors | Several items anchor to other stages (B01/B02, B04, B05) or to "gate-recommendation rework item 4"; one AR anchor is approximate ("p. ~46") | FAIL (MINOR, E2) |
| 4 | All 23 rows addressed (22 + R1) | Section 3 summary and Section 5 table each carry 23 rows | Complete; no row silently dropped | PASS |
| 5 | NO EVIDENCE FOUND used, no force-fit | 13 rows None | Used correctly; A2 contradiction scored None, conservative on filed evidence | PASS |
| 6 | Completionist recount performed, line present | "4 documented items across 4 categories" | Present, exact form | PASS |
| 7 | evidence_mix consistent with recount | documented 5, claim 1, inference 1 | Recount says 4 documented items. The fifth is not named | FAIL (MINOR, E3) |
| 8 | Completionist guard (12+ active) | 6 rows with evidence | Below 12; no re-examination required | PASS |
| 9 | Section 2C arithmetic | 28.8% | CWIP 17.50 Cr x FAT 2.1245 = 37.18 Cr; / 129.02 = 28.8%. CWIP used as "capex under execution" in absence of a programme table; caveat stated | PASS |
| 10 | Raw L x I values valid | A4 LL=1, C1 LL=1, C2 HL=2, E1 HM=3, H2 ML=1, H3 ML=1 | All map correctly to the matrix | PASS |
| 11 | Multipliers applied | 0.5, 0.7, 1.0 | A4 0.5; C1 0.7; C2 2.0; E1 3.0; H2 1.0; H3 1.0. Sum 8.2. Concur | PASS |
| 12 | Scores consistent with stated tiers | C1 claim-only at 0.7, A4 inference at 0.5 | No claim-only row scored at 1.0 | PASS |
| 13 | E1 category fit | HM=3 x 1.0 on registration footprint | Tier literal-compliant; first-mover leg unevidenced | PASS (note, E5) |
| 14 | I1 (Cat. 21) present, 0 unless both legs evidenced | 0; (a) and (b) both absent | Correct; "strong team" pattern named and scored 0 | PASS |
| 15 | I2 (Cat. 22) present, 0 unless named sacrifice | 0; "nothing must be destroyed" | Correct per category text | PASS |
| 16 | I1/I2 contribution stated separately | 0 of 8.2 | Present | PASS |
| 17 | Classification band | 8.2 -> NONE | <12 -> NO MEANINGFUL EMERGING MOAT | PASS |
| 18 | active_categories Strong/Moderate only | E1 only | Matches Section 3 count of 1 | PASS |
| 19 | Optionality register: table, columns, YAML | 10 rows, four columns, YAML mirrors | Complete; C1 and A4 now registered | PASS |
| 20 | catalysts_12m tiers consistent with report | All four "documented" | Parenterals and Wellness catalysts are deck claims per the report's own 1A | FAIL (MAJOR, E1) |
| 21 | F2 cross-references promise-delivery record | NO-CONCALL substitution plus B05 record | Done; negative finding scored 0 | PASS |
| 22 | R1 Section 4 (4A-4C) | Industry-wide, 0 | Complete; no company-specific capture, 0 correct | PASS |
| 23 | 6C uses injected Gate 0 block | Core 52, moat 15, 3 moats, MODERATE, AVERAGE | Matches B01-gate0.yaml exactly | PASS |
| 24 | 6D combined classification in standard set | AVERAGE | In the set; consistent with AVERAGE backward and NONE forward | PASS |
| 25 | Inference labelled (6C/6D/6E) | "M1 and M4 sit on the E1 platform" | Unlabelled inference; conflicts with own A3 finding | FAIL (MINOR, E4) |
| 26 | YAML schema, analyst_note <= 200 words | All keys present | analyst_note about 180 words | PASS |

Emerging Moat: 26 rules checked, 22 passed, 4 FAIL. Acceptance 84.6%.

### 2a. Emerging Moat findings

**E1 (MAJOR). catalysts_12m upgrades claims to documented.** B07 YAML
catalysts_12m[0] (TLL Parenterals first booked revenue against the Rs 200
Cr deck peak) and [1] (TLL Wellness commercialisation against the Rs 10 Cr
peak) carry evidence_type "documented". The report's own Section 1A tiers
both expected events as management claims: the Parenterals status change
to "commercial implementation" is from the Aug-2026 deck, and Wellness
"commercialisation expected from FY27" is deck p.14. Only the test is
documented: AOC-1 shows nil turnover. The YAML comment says catalysts_12m
feeds Pillar 3 catalyst proximity. A claim entering Pillar 3 labelled as
documented overstates evidence quality downstream. Rows [2] and [3] are
monitoring events. Their current state is documented. The expected
step-up and resolution are not. Recomputed: evidence_type "claim" for [0]
and [1]. For [2] and [3], split the documented state from the undocumented
expectation. The em_score is unaffected, and so is the NONE band. Decision
likely survives. Stage 11 must read these as claims.

**E2 (MINOR). Secondary anchors.** Rule 3 of the stage file requires AR page,
call or slide anchors on every evidence item. Several items anchor to other
pipeline stages: 1C "per B04", C2 "debtor days 116 to 208, B01/B02", and
C2/6B "gate-recommendation rework item 4" for the Rs 15.71 Cr related-party
sales. The solar capex anchor is "p. ~46 in extracted text". These should
carry primary AR note/page or filing anchors.

**E3 (MINOR). evidence_mix does not reconcile to the recount.** YAML
evidence_mix documented = 5. The completionist recount line, in both the
report and the YAML, says 4 documented items across 4 categories. The fifth
documented item is not named. em_score is unaffected.

**E4 (MINOR). Unlabelled inference in 6C/6D/6E.** The report says two of the
three Gate 0 moats (M1 pricing power, M4 customer stickiness) "sit on the
same underlying registration/subsidiary/pricing platform" scored here as E1.
That link is an inference and carries no inference label. It also conflicts
with the report's own A3 finding. That finding says the FY26 margin gain
came from overhead absorption while gross margin fell 690bps. M1 is a
margin-expansion test, so its link to the registration asset is not
evidenced. Recomputed: label the link as analyst inference. Stage 11
should check for one-improvement-two-mechanisms overlap before it credits
E1 in Pillar 3 beside the M1/M4 moat count.

**E5 (MINOR, PASS WITH NOTE). E1 category fit.** E1 is a geographic
first-mover test: first licence, or export markets peers have not entered.
B07 scores E1 on the documented registration footprint: 46 countries,
1,091 registered, 2,534 in process, and a Rs 13.54 Cr capitalised
intangible. The 1.0x tier is literal-compliant, because "regulatory
application submitted" is a documented item in the taxonomy. But nothing
shows these are markets peers have not entered. The report's own 2D found
no dated first-registration event. The first-mover element rests on
inference at best. Sensitivity: E1 at 0.5x = 1.5, em_score 6.7. At 0,
em_score 5.2. The NONE band holds either way. The EM >= 25 UA qualifier is
not met on any reading.

Recomputed em_score: 8.2 on the stated inputs (concur). The range is 5.2 to
6.7 if the E1 first-mover leg is re-tiered. The classification is NONE on
every reading.

---

## 3. VALUATION (B10, B11)

Pending phase 3. Not audited. Verifier rules 4-7 and 9-15
(growth symmetry, pillar mechanics, downstream candidates, method
plurality, business understanding narrative, dossier, exit construction,
FV path, expectation ledger, decomposition gates, skill-to-source fidelity)
run when B10/B11 are in scope.

---

## 4. SUMMARY

| Scope | Rules checked | Passed | Fails | Acceptance |
|---|---|---|---|---|
| Gate 0 (B01) | 42 | 40 | 2 (both MINOR) | 95.2% |
| Emerging Moat (B07) | 26 | 22 | 4 (1 MAJOR, 3 MINOR) | 84.6% |
| Valuation | pending phase 3 | | | |
| Total | 68 | 62 | 6 | 91.2% |

CRITICAL 0, MAJOR 1, MINOR 8. The MINOR count includes three PASS WITH
NOTE items: G3, G4, E5. No finding moves the Gate 0 classification (AVERAGE)
or the Emerging Moat band (NONE). Acceptance is above 60% on denominators
of 4 or more, so no REWORK trigger fires from this verifier. The MAJOR item
(E1) needs a stage 7 YAML fix, or at least a stage 11 read-as-claim
instruction, before Pillar 3 consumes catalysts_12m.

```yaml
stage: B12c
company: "TLL"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "phase 1 (Gate 0 B01 + Emerging Moat B07 only); valuation audit deferred to phase 3"
gate0:
  rules_checked: 42
  items_checked: 42
  rules_passed: 40
  acceptance_rate: 95.2
  fails:
    - "M5 Scale and Dominance scored 1 on a 4-name peer set where TLL ranks last; the set cannot establish segment top-5 rank. Recomputed M5 = 0 (PEER DATA NEEDED for segment universe); moat_score 15 -> 14; moats_confirmed 3 and MODERATE unchanged"
    - "Deal-breaker year attribution not stated in the deal-breaker block (rule requires naming which years drive each deal-breaker). Recomputed: FY23 CFO -19.00 Cr is 84% of cumulative -22.53 Cr; ex-FY23 CFO/PAT = -3.53/41.08 = -0.086, still triggers #4, so the cap is not a single post-IPO year artefact"
  findings:
    - severity: MINOR
      location: "01-gate0.md Block F M5; B01 moat_score"
      rule: "M5 top-5 mcap in segment"
      claimed: "M5 = 1 (TLL 4th of 4 = top 5)"
      recomputed: "M5 = 0; moat_score 14; moat_class MODERATE unchanged; classification AVERAGE unchanged"
    - severity: MINOR
      location: "01-gate0.md CLASSIFICATION deal-breaker check; B01 deal_breakers"
      rule: "state WHICH years drive any deal-breaker"
      claimed: "#2 and #4 listed without driving years"
      recomputed: "#4 driven by FY22, FY23, FY25 negative CFO; FY23 alone -19.00 Cr; ex-FY23 ratio -0.086, trigger holds"
    - severity: MINOR
      location: "01-gate0.md Block D D1"
      rule: "D1 Net Debt / EBITDA band; basis consistency with item-12 EBIT ruling"
      claimed: "D1 = 1 on operating EBITDA 28.11 Cr (2.45x)"
      recomputed: "On all-in EBITDA (PBT+Interest+Dep = 37.38 Cr) ratio 1.84x, D1 = 3; score sensitivity undisclosed; Core 52 -> 54, classification unchanged. PASS WITH NOTE, basis is stated"
    - severity: MINOR
      location: "01-gate0.md Block E E4"
      rule: "E4 Contingent Liabilities / Net Worth band boundary at 5%"
      claimed: "E4 = 3 at 5.17% on Rs 96.68 Cr parent-equity basis"
      recomputed: "Screener basis Rs 100.40 Cr gives 4.98% (E4 = 5); with Minority Interest Rs 104.17 Cr gives 4.80% (E4 = 5). Boundary sensitivity undisclosed; Core max 56 with D1, still 40-59 AVERAGE. PASS WITH NOTE"
  recomputed_card: "Core 52 (54-56 on alternative D1/E4 bases), moat 14 after M5, MODERATE, AVERAGE; deal-breaker #4 binding on every basis"
emoat:
  rules_checked: 26
  items_checked: 26
  rules_passed: 22
  acceptance_rate: 84.6
  fails:
    - "catalysts_12m evidence_type labels the TLL Parenterals and TLL Wellness revenue catalysts as documented, but the report's own Section 1A tiers the expected event as deck claim; only the test (AOC-1 nil turnover) is documented. Feeds Pillar 3 catalyst proximity. Recomputed evidence_type: claim"
    - "Source anchors: several evidence items anchor to other stages (B01/B02/B04/B05) or to gate-recommendation rework items, and one AR anchor is approximate (p. ~46), not primary source pages"
    - "evidence_mix documented 5 vs completionist recount 4 documented items; mismatch unexplained"
    - "Sections 6C/6D/6E assert M1 and M4 sit on the E1 registration platform without an inference label; contradicts own A3 finding that the FY26 margin gain came from overhead absorption with gross margin down 690bps"
  findings:
    - severity: MAJOR
      location: "B07-emoat.yaml catalysts_12m[0], [1] (also [2], [3] expectation legs)"
      rule: "scores and tiers consistent with stated evidence tiers (verifier rule 3); catalysts feed Pillar 3"
      claimed: "evidence_type documented"
      recomputed: "evidence_type claim for Parenterals Rs 200 Cr and Wellness FY27 commercialisation (deck p13/p14); documented applies to the AOC-1 nil-turnover test only"
    - severity: MINOR
      location: "07-emoat.md Sections 1B, 1C, 2A, 3 C2, 6B"
      rule: "SOURCE ANCHORS on every evidence item (AR p.__, call, slide)"
      claimed: "anchors such as B04, B05, B01/B02, gate-recommendation rework item 4, AR p. ~46"
      recomputed: "replace with primary AR page/note or filing anchors"
    - severity: MINOR
      location: "B07-emoat.yaml evidence_mix vs completionist_recount"
      rule: "completionist recount of documented items"
      claimed: "evidence_mix documented 5; recount 4 documented items across 4 categories"
      recomputed: "reconcile; em_score unaffected"
    - severity: MINOR
      location: "07-emoat.md 6C, 6D, 6E; B07 combined_reasoning"
      rule: "evidence taxonomy applied to every piece of evidence (inference must be labelled)"
      claimed: "M1 and M4 sit on the same registration platform scored as E1"
      recomputed: "label as inference; flag possible one-improvement-two-mechanisms overlap for stage 11"
    - severity: MINOR
      location: "07-emoat.md Section 3 E1 and Section 5 E1 row"
      rule: "category fit; E1 tests first-mover (markets peers have not entered)"
      claimed: "E1 HM=3 x 1.0 = 3.0 on registration footprint"
      recomputed: "Tier 1.0x is literal-compliant (regulatory application submitted = documented), but no first-mover or peer-absence evidence; report 2D finds no dated first-registration event. At inference tier E1 = 1.5, em_score 6.7; band NONE unchanged. PASS WITH NOTE"
  recomputed_em_score: "8.2 concur on stated inputs (6.7 if E1 first-mover leg taken at inference tier); NONE band holds either way"
valuation: "pending phase 3"
expectation_ledger: "pending phase 3"
business_understanding_narrative: "pending phase 3"
recomputed_destination_pe: ""
recomputed_decision: ""
critical_count: 0
major_count: 1
minor_count: 8
rules_checked_total: 68
rules_passed_total: 62
acceptance_rate: 91.2
rework_trigger: false
```
