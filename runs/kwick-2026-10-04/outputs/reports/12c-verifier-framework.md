# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, KWICK, run 2026-10-04

Scope: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07). The valuation audit (B10/B11), the expectation ledger (rules 13-14) and the Business Understanding Narrative (rule 9) are PENDING PHASE 3. The rule sources are prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md. Nothing else was loaded.

Artifacts audited:
- runs/kwick-2026-10-04/outputs/reports/01-gate0.md
- runs/kwick-2026-10-04/outputs/blocks/B01-gate0.yaml
- runs/kwick-2026-10-04/outputs/reports/07-emoat.md
- runs/kwick-2026-10-04/outputs/blocks/B07-emoat.yaml

Source data was used only to re-derive scores:
- inputs/screening/screener-Data_Sheet.csv (Rs Cr), cited as "screener-data"
- inputs/prospectus/KWICK-Prospectus-2026-08-31.txt (Rs lakh), cited as "prosp Lnnnn"

Verifier A owns source fidelity. This audit re-uses the stage's inputs to test rule application only.

## 1. GATE 0 (B01) COMPLIANCE TABLE

Every block score was re-derived from screener-data and the prospectus lines cited.

| # | Rule | Stage value | Re-derived | Result |
|---|---|---|---|---|
| 1 | Data-years opener, confidence tier (5-6 yrs lower, no downgrade) | 6 yrs FY21-FY26, no downgrade | 6 yrs (screener-data cols FY21-FY26); no downgrade | PASS |
| 2 | ROCE source rule (use source ROCE, else compute and say so) | computed, EBIT/(TA - Other Liabilities) | Screener sheet has no ROCE line. Computed series 50.9/7.1/30.5/39.2/38.2/45.0 reproduced. Prospectus ROCE 39.07/38.15/44.88 (prosp L7192) agrees within 0.1pp, so no score effect. | PASS |
| 3 | A1 median ROCE | 38.7% -> 5 | (38.2+39.2)/2 = 38.7 -> 5 | PASS |
| 4 | A2 min ROCE | 7.1% -> 0 | FY22 0.24/3.40 = 7.1% -> 0 | PASS |
| 5 | A3 median ROE | 41.3% -> 5 | 7.0/39.0/41.2/41.3/45.3/58.9, median 41.25 -> 5 | PASS |
| 6 | A4 ROCE trend | -5.9pp -> 0 | 45.0 vs 50.9 = -5.9pp (>5) -> 0 | PASS |
| 7 | B1 cum CFO/PAT | 0.459 -> 0 | 12.66/27.58 = 0.459 (screener-data) -> 0 | PASS |
| 8 | B2 FCF-positive proportion | 2/3 -> 2 | FY24 -310.09, FY25 +426.17, FY26 +555.71 lakh (prosp L3856-3859) -> 66.7% -> 2. With CWIP additions (prosp L3861): FY25 +364.47, FY26 +480.24, same sign pattern. | PASS |
| 9 | B3 cum FCF/PAT | 0.270 -> 1 | 6.72/24.90 = 0.270 -> 1. With CWIP: 5.35/24.90 = 0.215, still 1 (0.015 above the 0.20 edge). | PASS |
| 10 | B4 change in WC days, latest vs earliest | FY24 start, -59.8 days -> 5 | See finding G0-1. FY21 start: B4 <= 1 | **FAIL (MAJOR)** |
| 11 | C1 revenue CAGR | 55.5% -> 5 | (105.71/11.61)^(1/5)-1 = 55.5% -> 5 | PASS |
| 12 | C2 PAT CAGR | 76.0% -> 5 | (13.51/0.80)^(1/5)-1 = 76.0% -> 5 | PASS |
| 13 | C3 positive YoY years | 4/5 -> 3 | Only FY22 fell (screener-data) -> 80% -> 3 | PASS |
| 14 | C4 PAT CAGR minus revenue CAGR | +20.5pp -> 5 | 76.0-55.5 = +20.5 -> 5 | PASS |
| 15 | CAGR edge rules | none triggered; no loss-to-profit swing noted | No zero or negative endpoint; PAT positive every year (screener-data) | PASS |
| 16 | D1 ND/EBITDA | net cash -> 5 | Borrowings blank FY26 (screener-data), cash 13.16 -> net cash -> 5 | PASS |
| 17 | D2 interest cover | 46.6x / 50.6x -> 5 | 18.62/0.40 = 46.6x -> 5 | PASS |
| 18 | D3 D/E | 0 -> 5 | 0 -> 5 | PASS |
| 19 | D4 current ratio | 2.90 -> 5 | 5,471.68/1,884.55 = 2.90 (prosp L6341, L6349) -> 5 | PASS |
| 20 | E1 promoter holding | 64.65% -> 5 | Promoter and group post-offer 64.65% -> 5. Disclosed as pre-allotment, no filed pattern. | PASS |
| 21 | E2 3-yr change | -23.9pp -> 0 | Any reading (88.53 or ~96.97 to 64.65) is a fall of more than 3pp -> 0 | PASS |
| 22 | E3 pledge | 0% -> 5 | 0 -> 5 | PASS |
| 23 | E4 contingent/NW | 14.3% -> 3 | 592.85/4,140.67 = 14.32% (prosp L3924) -> 3 | PASS |
| 24 | M1 pricing power | 5 | EBITDA margin 15.3 to 18.0 (+2.7pp; PBT+Int+Dep-OI, screener-data), CAGR 55.5% -> 5. Window-sensitive, disclosed. | PASS |
| 25 | M2 cost advantage | 0, PEER DATA NEEDED | Rule: no peer data -> 0 and mark | PASS |
| 26 | M3 capital efficiency | 5 | FAT 105.71/3.00 = 35.2x, ROCE 45.0% -> 5 | PASS |
| 27 | M4 customer stickiness | 3 | 1 decline year (FY22), recovered FY23 -> 3 | PASS |
| 28 | M5 scale and dominance | 0, PEER DATA NEEDED | per rule | PASS |
| 29 | M6 technology/R&D | 0, R&D expense NOT FOUND | No R&D expense line in the prospectus grep (4 R&D staff, prosp L9734). NOT FOUND -> 0 | PASS |
| 30 | M7 regulatory/licence | 0, NOT FOUND | Gate 0 rule 2 bars qualitative judgement. No regulated-segment count in inputs -> 0 | PASS |
| 31 | M8 distribution | 0 | The company is itself an OEM channel partner (prosp L9213-9265). It discloses no own outlet network -> 0 | PASS |
| 32 | M9 brand | 0, PEER DATA NEEDED | per rule; GM proxy stated | PASS |
| 33 | M10 switching costs | 0 | Grew all but FY22; receivable days 44.6 to 79.0 (+34.4) not stable. No band fits 1 decline year with unstable days, so the rule reads "else 0" as written. Rubric gap noted in Section 3. | PASS |
| 34 | M11 network effects | 3 | Fallback trend: FY23-26 CAGR 73.1%, S&A/sales 14.2% to 3.7% (screener-data) -> 3. Rubric defect noted in Section 3. | PASS |
| 35 | M12 negative WC/float | 0 | 144.8/95.0/85.0 days, all >45 -> 0 | PASS |
| 36 | Moat count and class | 4 present, STRONG | M1, M3, M4, M11 >= 3 -> 4 -> STRONG | PASS |
| 37 | Core, moat, grand total arithmetic | 69 / 16 / 85 | 10+8+18+20+13 = 69; 5+5+3+3 = 16; 85 | PASS (on stage scores) |
| 38 | Classification matrix | GOOD+ | Core 60-79 + STRONG -> GOOD+ | PASS (on stage scores; see G0-1) |
| 39 | Deal-breaker application, which years drive it | DB4 caps AVERAGE; FY22, FY24 named | DB4 0.459 < 0.50 -> max AVERAGE; drivers named. DB2 status depends on G0-1. | PASS |
| 40 | FLAG-GATE0 emitted when <= AVERAGE with depressors | 2 flags | present | PASS |
| 41 | OUTPUT ends with the exact YAML block | embedded block uses pointers | See finding G0-2 | **FAIL (MINOR)** |

Gate 0 result: 41 rules checked, 39 PASS, 2 FAIL (1 MAJOR, 1 MINOR). The filed final classification, AVERAGE, stands.

### Finding G0-1 (MAJOR): the B4 window, and DB2 with it, rests on an undisclosed window choice

The stage scored B4 from FY24, the first year with all three legs. FY24 WC days were 144.8 and FY26 were 85.0, a change of -59.8 days, so B4 = 5. That makes Block B exactly 8, so DB2 does not trigger, and the uncapped result is GOOD+.

The same report scores A4, C1-C4, M1 and M10 on the FY21-FY26 window. For M10 it computes FY21 receivable days of 44.6. B4 is the only full-data metric anchored on a later start.

On FY21 the band does not need FY21 payables:
- FY21 receivable days = 1.42/11.61 x 365 = 44.6 (screener-data).
- FY21 inventory days = 1.11/11.61 x 365 = 34.9 (screener-data).
- FY21 WC days = 79.5 less payable days, and payable days cannot be negative.
- FY26 WC days = 79.0 + 36.0 - 30.1 = 85.0 (prosp L6482, L6435, L6433-6434, L7176).
- Change = +5.4 days plus FY21 payable days. That is at least +5.4 days.

So B4 = 1 if FY21 payable days are 9.6 or fewer, and 0 otherwise. Block B falls to 3 or 4, below 8, so DB2 triggers (max GOOD). Core becomes 64-65, still in the 60-79 band.

The final classification is unchanged: DB4 caps AVERAGE in both readings. The uncapped result is what moves. The stage files GOOD+ in B01 flags[0] and B07 6C, and states "Deal-breakers 1, 2 and 8 not triggered". On the FY21 reading the uncapped result is GOOD. This matters at Halt 1 if the operator applies the post-IPO rebase override to DB4: DB2 then governs. The window-sensitivity note in B01 lists Block A, M1 and M10. It omits B4.

Two readings:
- (a) "Earliest" means the first year where the formula's three legs exist. This is the stage's reading, supported by rule 6 ("use whatever history is available").
- (b) "Earliest" means the start of the scoring window, which the stage used for every other trend metric.

Separating observation: an operator ruling on whether a trend metric may take a later start than the scoring window when the band is determinable from the earlier year. The FY21 margin is 0.4 day above the ±5-day edge, which is thin but determinate.

### Finding G0-2 (MINOR): the embedded YAML is not the block

The fenced block at the end of 01-gate0.md has `data_notes` as a pointer string, not a list. Its `analyst_note` reads "see B01-gate0.yaml". A prose line follows the fence. The block file B01-gate0.yaml is complete and the report names it as authoritative. This is presentational only.

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Stage | Check | Result |
|---|---|---|---|---|
| 1 | All six sections present | 1A-C, 2A-D, 3, 4A-C, 5, register, 6A-E | present | PASS |
| 2 | All 22 categories + R1 addressed or NO EVIDENCE FOUND | 22 in Section 3, R1 in Section 4 | every row addressed | PASS |
| 3 | Evidence taxonomy and anchors on evidence items | tags on table rows | present | PASS |
| 4 | Section 3 summary: 22 rows, Strong/Moderate count | 22 rows, count 0 | present | PASS |
| 5 | Completionist recount performed, line stated | "📄 recount performed: 12 documented items across 6 categories" | present. 8 categories score, under the 12 ceiling | PASS |
| 6 | evidence_mix counts reconcile with tagged evidence | 12 / 9 / 3 | counting rule unstated; see EM-2 | **FAIL (MINOR)** |
| 7 | L x I to raw mapping | A4 LL 1, C1 LM 1, C2 ML 1, F2 MM 2, G1 HL 2, G2 MM 2, H2 ML 1, R1 HM 3 | all match the matrix | PASS |
| 8 | Evidence multipliers from the rubric set only | F2 "mixed 0.7" | off-rubric; see EM-1 | **FAIL (MAJOR)** |
| 9 | Scores consistent with stated tiers (no 🎙️/🔍-only scored as 📄) | A4 🎙️, C1 🔍, C2/G1/G2/H2/R1 📄 | A4 and C1 sit at or below their best tag. R1 at 1.0x: the policies are 📄 and the Kwick link is 🔍. Defensible because the policy is the R1 evidence object; disclosed. | PASS (R1 note) |
| 10 | Adjusted total arithmetic | 11.6 | 0.7+0.5+1.0+1.4+2.0+2.0+1.0+3.0 = 11.6 | PASS |
| 11 | Classification band on stated total | <12 NONE | correct on 11.6; contingent on EM-1 | PASS |
| 12 | I1/I2 contribution stated separately | 0.0 | present | PASS |
| 13 | Rule 8: Category 21 present; >0 only with both legs, (b) leg 📄 | 0, both legs absent | compliant | PASS |
| 14 | Rule 8: Category 22 present; >0 only with a specific named sacrifice | 0, per-moat "what must be destroyed" table | compliant | PASS |
| 15 | 2C arithmetic shown; YAML field "from 2C" | arithmetic 42.5% shown, field 0 | see EM-3 | **FAIL (MINOR)** |
| 16 | Optionality register: format, carried in block | 10 rows, 4 columns, in YAML | present | PASS |
| 17 | 6C uses the injected Gate 0 block | core 69, 4 moats STRONG, AVERAGE | matches B01 | PASS |
| 18 | 6D combined classification; HIGH POTENTIAL and TURNAROUND reasoned | AVERAGE; both rejected with reasons | Matrix cells are not printed in the rule source, so this is checked for consistency only | PASS |
| 19 | active_categories holds only Strong/Moderate rows | R1 only | correct | PASS |
| 20 | catalysts_12m holds 12-month items | 2 items at 6-18m and 12-24m | see EM-4 | **FAIL (MINOR)** |
| 21 | F2 cross-references the promise-delivery record | B05 record used; NO-CONCALL MODE disclosed | present | PASS |
| 22 | YAML schema; analyst_note <= 200 words | about 120 words | compliant | PASS |
| 23 | Not conflated with FTTCP | scope note present | compliant | PASS |

Emerging Moat result: 23 rules checked, 19 PASS, 4 FAIL (1 MAJOR, 3 MINOR).

### Finding EM-1 (MAJOR): F2 uses a multiplier the rubric does not contain, and the band flips on it

Section 5 allows three multipliers, keyed to evidence type: 📄 1.0x, 🎙️ 0.7x and 🔍 0.5x. F2 is tagged "mixed 📄/🔍". The stage applied 0.7x, which is the management-claim multiplier, to evidence that contains no management claim. F2 was MM raw 2, adjusted to 1.4.

What F2 rests on:
- 📄: prospectus timeline statements tested against restated FY24-FY26 results (4 delivered, 3 partial, 1 missed, per B05).
- 📄: vehicle deliveries with acceptance certificates.
- 📄: no bank guarantee invoked.
- 🔍: the reading that a lean team scales.

Recomputed:

| Reading | F2 adjusted | EM total | Band |
|---|---|---|---|
| 📄 (rating rests on the documented delivery record) | 2.0 | 12.2 | MODEST MOAT DEVELOPMENT |
| 🔍 (rating rests on the scalability inference) | 1.0 | 11.2 | NO MEANINGFUL EMERGING MOAT |
| Filed (off-rubric 0.7x) | 1.4 | 11.6 | NONE |

The stage did disclose F2 as a judgement call and stated that one raw point reaches MODEST. It did not state that the multiplier itself is outside the rubric. Its R1 sensitivity ("at 0.7x R1 = 2.1, total 10.7") uses the same off-rubric value. The rubric 🔍 reading of R1 is 3 x 0.5 = 1.5, which gives a total of 10.1.

Separating observation: does the MM likelihood rest on the documented delivery record or on the scalability inference? The stage should name one and score on that tag.

Why MAJOR and not CRITICAL: no reading reaches the "EM >= 25" UA qualifier or EXPANSION. 6D AVERAGE is unchanged, and no decision exists in phase 1. PHASE 3 CHECK: if any Pillar 3 step keys to NONE versus MODEST, re-grade this finding against the destination-PE test in rule 5.

### Finding EM-2 (MINOR): the recount uses an unstated counting rule

The recount reads "12 documented items across 6 categories (C2 1, G1 1, G2 1, F2 2, H2 2, R1 5)". The Section 3 tables tag more 📄 rows than that: A4 1, C1 1 (counter), C2 4, G1 3, G2 4 and H2 3. The count appears to keep supporting items only, about one per category. Undercounting 📄 is the conservative direction, and the guard's purpose is met. The counting rule should be stated so that evidence_mix can be audited.

### Finding EM-3 (MINOR): capex_embedded_growth_pct overrides 2C

As written, 2C is capex under execution times historical FAT: Rs 1.37 Cr x 32.77x = Rs 44.95 Cr, which is 42.5% of Rs 105.71 Cr. The YAML field is defined as "from 2C". The stage showed the arithmetic, rejected it as an artefact (software CWIP, near-zero asset base on a resale model) and filed 0. The reasoning is sound and disclosed in the analyst_note. But 0 is a number the template did not produce. The override stops a spurious CAPACITY basis from reaching stage 11's 26.1 hierarchy, so the direction is protective. Stage 11 must read the analyst_note and must not take the field at face value.

### Finding EM-4 (MINOR): catalysts_12m holds items outside 12 months

Two of the five items fall outside 12 months: the E-Forensics CWIP (12-24m) and the state DNA/cyber awards (6-18m). The field feeds Pillar 3 catalyst proximity. Stage 11 should key proximity to each item's window field, not to list membership.

## 3. RUBRIC NOTES FOR THE OPERATOR (not stage failures)

- Gate 0 M11 states that the two-window test "needs >= 6 years". Two non-overlapping 3-year CAGR windows need 7 annual points. KWICK has 6 (screener-data FY21-FY26), so the stage correctly used the fallback (3). A two-year prior window (FY21-FY23, 32.5%) against FY23-FY26 (73.1%), with S&A share falling, would score 5. M11 is present on either reading, and the class stays STRONG. The rubric text needs a fix.
- Gate 0 M10 has no band for exactly one decline year with unstable receivable days. As written this falls to "else 0", which is below the band for two or more decline years (1). The rubric text needs a fix.
- These two notes, together with G0-1, show how much of the B01 moat count is mechanical. B07 FLAG-GATE0-DIVERGENCE already carries this point. This audit concurs.

## 4. NOT CHECKED IN THIS SCOPE

- Rules 4, 5 (valuation severity), 7, 11-15: B10/B11 and the expectation ledger do not exist yet. PENDING PHASE 3.
- Rule 6 (B09 downstream candidates): outside the phase-1 task scope.
- Rule 9 (stage 13 narrative) and rule 10 (B09b at finalize): not yet due.
- Per-number source fidelity belongs to Verifier A.

## 5. SUMMARY

- 64 rules checked. 58 passed and 6 failed, an acceptance rate of 90.6%.
- 0 CRITICAL, 2 MAJOR (G0-1, EM-1), 4 MINOR.
- No REWORK trigger from this verifier. The rate is above 60% on a denominator of 64, and there is no CRITICAL.
- Both MAJOR findings leave the filed classifications intact: Gate 0 AVERAGE and combined AVERAGE.
- Two labels are contingent on a reading and should reach Halt 1 named as such. The uncapped Gate 0 result is GOOD+ or GOOD (G0-1). The EM band is NONE or MODEST (EM-1).

```yaml
stage: B12c
company: "KWICK"
run_date: "2026-10-04"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "PHASE 1 ONLY: Gate 0 (B01) + Emerging Moat (B07). Valuation audit (B10/B11), expectation ledger and rule 9 are PENDING PHASE 3."
gate0:
  rules_checked: 41
  fails:
    - "G0-1 MAJOR: B4 scored on an FY24 start (B4 = 5, Block B = 8, DB2 not triggered, uncapped GOOD+). On the FY21-FY26 window the stage used for A4, C1-C4, M1 and M10, B4 <= 1 for any FY21 payables (WC days change >= +5.4 days), Block B <= 4, DB2 triggers (max GOOD), uncapped result is GOOD, not GOOD+. Final AVERAGE unchanged (DB4). Window dependence not disclosed."
    - "G0-2 MINOR: the YAML inside 01-gate0.md is not the block. data_notes and analyst_note are pointer strings, and prose follows the fence. Block file B01-gate0.yaml is complete."
emoat:
  rules_checked: 23
  fails:
    - "EM-1 MAJOR: F2 adjusted with an off-rubric 0.7x 'mixed' multiplier on 📄/🔍 evidence (raw 2 -> 1.4). The rubric allows 1.0 / 0.7 / 0.5 by evidence type only. 📄 reading: F2 2.0, total 12.2 = MODEST. 🔍 reading: F2 1.0, total 11.2 = NONE. Filed: 11.6 NONE. The band flips on the reading. The R1 sensitivity also uses 0.7x; the rubric 🔍 reading is 1.5 (total 10.1)."
    - "EM-2 MINOR: evidence_mix {documented 12} and the 📄 recount use an unstated counting rule (supporting items only, about one per category). Section 3 tables tag more 📄 rows (A4 1, C1 1, C2 4, G1 3, G2 4, H2 3). Direction is conservative."
    - "EM-3 MINOR: capex_embedded_growth_pct filed as 0. The 2C arithmetic as written gives 42.5% (Rs 1.37 Cr CWIP x 32.77x = Rs 44.95 Cr on Rs 105.71 Cr). Override is reasoned and disclosed, but the field is not 'from 2C'. Stage 11 must read the analyst_note."
    - "EM-4 MINOR: catalysts_12m carries two items outside 12 months (E-Forensics CWIP 12-24m; state DNA/cyber awards 6-18m). The field feeds Pillar 3 catalyst proximity."
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 (B10/B11 not produced yet)"}
expectation_ledger: {status: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_understanding_narrative: {status: "PENDING (stage 13 not run)", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # valuation scope not run
recomputed_decision: ""        # Gate 0 final classification AVERAGE concurs; see G0-1 for the uncapped result
findings:
  - {id: "G0-1", severity: "MAJOR", location: "01-gate0.md Block B (B4), Section 3 classification box; B01-gate0.yaml flags[0], blocks.B", rule: "Gate 0 B4 + deal-breaker 2; CAGR/window consistency (rule 2)", stated: "B4 = 5 (WC days 144.8 FY24 to 85.0 FY26); Block B 8; DB2 not triggered; uncapped GOOD+", recomputed: "FY21 start: receivable days 44.6 + inventory days 34.9 = 79.5 less payables days >= 0 (screener-data FY21); FY26 WC days 85.0 (prosp L6433-6435, L6482, L7176). Change >= +5.4 days -> B4 = 1 (payables days <= 9.6) or 0. Block B 3-4 < 8 -> DB2 max GOOD. Core 64-65, still 60-79.", note: "Two readings: earliest = first year with all three legs (stage) vs earliest = start of the scoring window the stage used everywhere else. Separator: operator ruling on per-metric windows. FY21 payables are not needed to fix the band. Final AVERAGE survives via DB4. Uncapped GOOD+ in B01 flags and B07 6C is window-contingent and matters if the post-IPO rebase override lifts DB4."}
  - {id: "G0-2", severity: "MINOR", location: "01-gate0.md lines 116-147", rule: "Gate 0 OUTPUT: end with exactly this fenced YAML block", stated: "embedded block with pointer strings; trailing prose", recomputed: "n/a", note: "Block file is authoritative and complete; presentational."}
  - {id: "EM-1", severity: "MAJOR", location: "07-emoat.md Section 5 row 15 (F2); B07-emoat.yaml em_score, em_classification", rule: "Stage 7 Section 5 evidence multipliers (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x)", stated: "F2 MM raw 2 x 'mixed 0.7' = 1.4; total 11.6 NONE", recomputed: "📄 reading 2.0 -> 12.2 MODEST; 🔍 reading 1.0 -> 11.2 NONE", note: "F2 rests on prospectus statements tested against restated FY24-FY26 results (4 delivered, 1 missed) and vehicle acceptance certificates, which are 📄; the scalability claim is 🔍. Separator: whether the MM rating rests on the documented delivery record or on the scalability inference. No reading reaches the EM >= 25 UA qualifier or EXPANSION, so 6D AVERAGE stands. Phase 3: check whether any Pillar 3 step keys to NONE vs MODEST; if one does, re-grade."}
  - {id: "EM-2", severity: "MINOR", location: "07-emoat.md Section 3 recount line; B07 evidence_mix", rule: "Stage 7 rule 6 completionist recount; evidence_mix item counts", stated: "12 documented / 9 claim / 3 inference", recomputed: "counting basis not stated; tagged 📄 rows exceed 12", note: "Undercounting 📄 is the conservative direction; the guard purpose is met (8 categories score, ceiling 12)."}
  - {id: "EM-3", severity: "MINOR", location: "07-emoat.md 2C; B07 capex_embedded_growth_pct", rule: "Stage 7 Section 2C, YAML field 'from 2C'", stated: "0", recomputed: "42.5% mechanical", note: "Override reasoned (software CWIP, asset-light resale turnover) and disclosed in analyst_note. Prevents a spurious CAPACITY basis at stage 11."}
  - {id: "EM-4", severity: "MINOR", location: "B07 catalysts_12m items 3 and 4", rule: "catalysts_12m feeds Pillar 3 catalyst proximity", stated: "windows 6-18m and 12-24m inside the 12m list", recomputed: "3 of 5 items sit inside 12 months", note: "Stage 11 should read the window field, not list membership."}
rubric_notes:
  - "Gate 0 M11 says the two-window test 'needs >= 6 years', but two non-overlapping 3-year CAGR windows need 7 annual points. KWICK has 6; the stage used the fallback (3). A FY21-FY23 two-year prior window would give 5. M11 is present either way. Operator fix to the rubric text."
  - "Gate 0 M10 has no band for exactly 1 decline year with unstable receivable days. As written it falls to 'else 0', below the 2+ decline-year band (1). Operator fix to the rubric text."
critical_count: 0
major_count: 2
minor_count: 4
acceptance_rate: 90.6             # 58 passed / 64 checked (Gate 0 41, Emerging Moat 23)
```
