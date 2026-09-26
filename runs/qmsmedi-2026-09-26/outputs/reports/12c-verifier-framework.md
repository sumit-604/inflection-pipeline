# VERIFIER C: FRAMEWORK ADHERENCE, QMSMEDI, run 2026-09-26 (PHASE 1 SCOPE)

Model: claude-opus-5-5. Scope: Gate 0 (B01) and Emerging Moat (B07) only.
The valuation audit (B10/B11), rules 4-7 and 9-15, the expectation ledger,
and the narrative check are PENDING PHASE 3. Rule sources read:
prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Units: Rs Cr unless stated. This audit tests rule application. Verifier A owns
whether a number exists in the source. One source check was needed here (E4),
and it is labelled.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

Every block score was re-derived from the inputs the report states.

| # | Rule | Reported | Re-derived | Result |
|---|------|----------|-----------|--------|
| 1 | Opening data line, history window | 8 yrs FY19-FY26, FY18 stub excluded | Tier 7-9 either way | PASS (see observation O1) |
| 2 | A1 median ROCE | 25.12%, 5 | sorted 9.62/13.84/16.56/17.39/32.84/53.54/64.80/120.52; median (17.39+32.84)/2 = 25.115 -> 5 | PASS |
| 3 | A2 min ROCE | 9.62%, 1 | 8-11.9 band -> 1 | PASS |
| 4 | A3 median ROE | 23.15%, 5 | (11.84+34.45)/2 = 23.145 -> 5 | PASS |
| 5 | A4 ROCE trend | -110.9pp, 0 | >5pp decline -> 0 | PASS |
| 6 | B1 cum CFO / cum PAT | 43.28/63.49 = 0.68, 1 | sums re-added: 43.28 and 63.49; 0.682 -> 1 | PASS |
| 7 | B2 FCF-positive years | 2/2 = 100%, 5 | see F1 | **FAIL** (0 strict; max 4 bounded) |
| 8 | B3 cum FCF / cum PAT | 2.12, 5 | see F1 | **FAIL** (0 strict; max 3 bounded) |
| 9 | B4 WC days change | +15.79 (FY25->FY26), 0 | 193.14 -> 208.93 = +15.79 -> 0; 1-yr window labelled | PASS |
| 10 | C1 revenue CAGR | 16.61%, 4 | (152.13/51.89)^(1/7) - 1 = 16.61% -> 4 | PASS |
| 11 | C2 PAT CAGR | 11.77%, 3 | (6.69/3.07)^(1/7) - 1 = 11.77% -> 3 | PASS |
| 12 | C3 positive YoY years | 6/7, 3 | 85.7% -> 3 | PASS |
| 13 | C4 PAT minus revenue CAGR | -4.84pp, 1 | -3 to -8 band -> 1 | PASS |
| 14 | CAGR edge rules | none triggered | both endpoints positive; no loss-to-profit swing; C4 computable | PASS |
| 15 | D1 ND/EBITDA | 2.83x, 1 | 73.28/25.88 = 2.83 -> 1 | PASS |
| 16 | D2 interest cover | 3.51x, 2 | 22.99/6.55 = 3.51 -> 2 | PASS |
| 17 | D3 D/E | 0.71x, 3 | 74.48/104.20 = 0.715 -> 3 | PASS |
| 18 | D4 current ratio | 1.54x, 4 | 142.01/92.28 = 1.539 -> 4 | PASS |
| 19 | E1 promoter holding | 68.11%, 5 | >=60 -> 5 | PASS |
| 20 | E2 promoter change (3 yr) | -5.56pp (1 yr), 0 | score 0 stands; see F5 | **FAIL** (MINOR, rationale) |
| 21 | E3 pledge | 0%, 5 | -> 5 | PASS |
| 22 | E4 contingent liab / NW | N/A, 0 | see F2 | **FAIL** (5) |
| 23 | M1 pricing power | 5 | OPM +4.5pp, rev CAGR 16.6% -> 5 | PASS |
| 24 | M2 cost advantage | 0 PEER DATA NEEDED | rule-compliant | PASS |
| 25 | M3 capital efficiency | 0 | FAT 6.17x, ROCE FY26 9.62% < 12 -> 0 (latest-with-latest is consistent) | PASS |
| 26 | M4 customer stickiness | 3 | 1 decline year, recovered -> 3 | PASS |
| 27 | M5 scale | 0 PEER DATA NEEDED | rule-compliant | PASS |
| 28 | M6 R&D | 0 | no R&D line -> 0 | PASS |
| 29 | M7 regulatory | 0 | player count NOT FOUND -> 0 | PASS |
| 30 | M8 distribution | 0 | no metric -> 0 | PASS |
| 31 | M9 brand | 0 PEER DATA NEEDED | GM proxy stated, no peer median | PASS |
| 32 | M10 switching costs | 0 | 1 decline year, receivable days 56 -> 142 not stable -> 0 | PASS |
| 33 | M11 network effects | 0 | see F4 | **FAIL** (MINOR, reasoning) |
| 34 | M12 negative WC | 0 | 193/209 days > 45 -> 0 | PASS |
| 35 | Moat classification | 2 present, MODERATE | M1, M4 -> 2 -> MODERATE | PASS |
| 36 | Data confidence adjustment | 7-9 moderate, no downgrade | correct | PASS |
| 37 | Classification matrix | Core 53 -> AVERAGE | 40-59 -> AVERAGE | PASS |
| 38 | Deal-breaker application | none | DB2 fires on strict B2/B3 reading, see F3 | **FAIL** (MINOR) |
| 39 | FLAG-GATE0 and YAML schema | flag present, schema complete | correct | PASS |
| 40 | Anchors on every number | present | present | PASS |

Gate 0: 40 rules checked, 34 PASS, 6 FAIL.

### Gate 0 findings

**F1 (MAJOR). B2 and B3 scored on a favourable 2-year sub-window.**
The report computes FCF on FY25-FY26 only because capex is not broken out for
FY19-FY24. Rule 5 of 01 says a data point not available is marked N/A and
scored 0. The report instead scored a sub-window and gave 5 + 5. The window
choice is not neutral. FY25 + FY26 CFO is Rs 44.86 Cr (26.09 + 18.77), which
exceeds the 8-year cumulative CFO of Rs 43.28 Cr. The two best cash years
stand in for the whole period.
The full-window bound is computable from the report's own table. FY22 CFO is
-1.72 and FY23 CFO is -7.54. Capex cannot be negative, so FCF is negative in
both years whatever capex was. FCF-positive years are therefore at most 6/8 =
75%, which scores at most 4. Cumulative FCF is at most 43.28 - 8.62 (FY25 +
FY26 capex) = 34.66, so B3 is at most 34.66/63.49 = 0.546, which scores at
most 3.
Recomputed: strict rule 5 reading, B2 = 0, B3 = 0, Block B = 1. Bounded
reading, Block B <= 8. Core falls from 53 to 48 (strict) or at most 50
(bounded), before the E4 correction.

**F2 (MAJOR). E4 scored N/A although the note exists.**
The report and B01 input_gaps say a full-text search of both ARs found no
contingent-liabilities note. The FY26 AR text holds one twice:
Annual_Report_2026.txt line 9442 (NOTE 42, CONTINGENT LIABILITY, standalone)
and line 12945 (NOTE 40, consolidated). Both show an outstanding TDS demand
totalling Rs 5.30 lakh, with the line "There are no outstanding demands under
GST and Income Tax (Other than TDS as shown above)." Against net worth Rs
104.20 Cr, the ratio is about 0.05%. The <5% band scores 5.
Recomputed: E4 = 5, Block E = 15, core +5. Verifier A owns the number
itself. The finding here is that the N/A rule was applied to a disclosed
item.

**F3 (MINOR). Deal-breaker 2 not recorded under the strict reading.**
With F1 on the strict rule, Block B = 1 < 8, so deal-breaker 2 fires and caps
at GOOD. The cap does not bind, because the classification is already
AVERAGE. It still belongs in deal_breakers with the driving years named
(FY22 and FY23 negative CFO, FY19-FY24 capex N/A).

**F4 (MINOR). M11 reasoning misstates tier 3.**
The report says rising selling % fails "every tier that would otherwise
score". Tier 3 ("growth >15% but selling % rising = 1") requires rising
selling %. Whether tier 3 fires depends on the growth window. The full-period
CAGR of 16.61% clears >15%. The latest 3-year CAGR of 13.54% does not. The
score is 0 or 1. The moat count is unchanged, because a moat needs >= 3.

**F5 (MINOR). E2 window rationale is unsupported.**
E2 uses a 1-year change (Jun-2025 to Jun-2026) and says the company's
listed history is short. The corpus holds only three SHP files
(2025-06-30, 2026-03-31, 2026-06-30, inputs/shareholding/). The real reason
is a corpus gap, not listing age. The score of 0 stands on either reading
(-5.56pp in one year, or N/A = 0). The data note should name the gap, and
the rights-issue attribution should stay labelled as unverified in this
stage.

**Observation O1 (not scored).** FY18 is excluded as a stub year (sales Rs
0.08 Cr). Rule 6 says to use whatever history exists. The exclusion is
disclosed and defensible, because FY18 as a CAGR start would be meaningless.
The confidence tier is 7-9 either way.

**Observation O2 (not scored).** The report mixes bases: A/B/C standalone, D
consolidated. Rule 01 does not forbid this, and every number carries its basis
label.

### Gate 0 recomputation

| Reading | A | B | C | D | E | Core | Class |
|---------|---|---|---|---|---|------|-------|
| As reported | 11 | 11 | 11 | 10 | 10 | 53 | AVERAGE |
| E4 fix only | 11 | 11 | 11 | 10 | 15 | 58 | AVERAGE |
| E4 fix + B2/B3 bounded max | 11 | <=8 | 11 | 10 | 15 | <=55 | AVERAGE |
| E4 fix + B2/B3 strict rule 5 | 11 | 1 | 11 | 10 | 15 | 48 | AVERAGE (DB2 fires, non-binding) |

The classification is AVERAGE in every reading, so no finding is CRITICAL.
Moat score is 8 (or 9 if M11 tier 3 applies). Moat class stays MODERATE.
The E4-only reading gives 58, two points below the GOOD band. That is why
the B2/B3 treatment matters. The sub-window scoring moved the core toward the
boundary.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Result | Note |
|---|------|--------|------|
| 1 | All 23 rows (22 categories + R1) addressed or NO EVIDENCE | PASS | Section 3 summary lists 23 rows |
| 2 | Section 1 (1A, 1B, 1C) | PASS | |
| 3 | Section 2 (2A-2D) | PASS | |
| 4 | 2C arithmetic shown or gap stated | PASS | not computed; reason stated |
| 5 | Likelihood x impact matrix | **FAIL (MAJOR)** | see G1 |
| 6 | Evidence multipliers 1.0 / 0.7 / 0.5 on single-tier rows | PASS | A1, B2, C1, D1, D2, H1, H2 apply listed values |
| 7 | Mixed-tier multiplier | **FAIL (MINOR)** | see G2 |
| 8 | Score consistent with stated tier | **FAIL (MINOR)** | B2, see G3 |
| 9 | No force-fit; one item, one mechanism | **FAIL (MINOR)** | A1, see G4 |
| 10 | Completionist recount performed | PASS | 5 active < 12 |
| 11 | Recount line reconciles | **FAIL (MINOR)** | see G5 |
| 12 | Section 5 shows all 23 rows | **FAIL (MINOR)** | 12 zero rows collapsed to one line; all accounted |
| 13 | Adjusted total arithmetic as stated | PASS | 1+2+1.4+1.4+1.4+1.7+3+4+1.2 = 17.1 |
| 14 | Classification band | PASS | 17 -> 12-24 MODEST |
| 15 | I1 both legs (rule 8 of Verifier C) | PASS | (a)-only scale hiring -> 0 |
| 16 | I2 named sacrifice | PASS | "nothing must be destroyed" -> 0 |
| 17 | I1/I2 contribution stated separately | PASS | 0 |
| 18 | Optionality register (table + YAML) | PASS | 6 rows, 4 columns |
| 19 | Section 4 R1 (4A-4C) | PASS | |
| 20 | Section 6 (6A-6E) | PASS | |
| 21 | 6C uses injected B01 block | PASS | Core 53, AVERAGE, 2 moats (inherits F1/F2) |
| 22 | YAML schema complete | PASS | |
| 23 | capex_embedded_growth_pct matches 2C | **FAIL (MINOR)** | see G6 |

Emerging Moat: 23 rules checked, 16 PASS, 7 FAIL.

### Emerging Moat findings

**G1 (MAJOR). LM scored as 2; the matrix says ML/LM = 1.**
Rule 07 Section 5: "HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1". The report
scores D1, D2, F2 and R1 at LM with raw 2.
Recomputed: D1 1 x 0.7 = 0.7; D2 0.7; F2 1 x 0.85 = 0.85; R1 1 x 0.6 = 0.6.
The total falls by 2.85, from 17.1 to 14.25, rounded 14. MODEST holds.

**G2 (MINOR). Averaged multipliers have no rule basis.**
F2 uses 0.85 (mean of 1.0 and 0.7) and R1 uses 0.6 (mean of 0.7 and 0.5).
Rule 07 names three multipliers and no averaging. The report should name the
governing tier. For R1, Section 4 says 4A and 4B are NOT FOUND and the 4C
tailwind is a management claim, so 0.7 or 0.5 applies. The score effect is
under 0.2 points.

**G3 (MINOR). B2 takes the documented multiplier for an effect the report
calls inference.**
The SOC 2 certificate is documented. The report states that the
certificate-to-contract link is inference. The moat is the lock-in, not the
certificate. B2 also cites the HEINE exclusivity clause, and H2 credits the
same agreement. HEINE exclusivity is a lock-in granted by the supplier, not
a customer qualification. That is one item credited through two categories.
Recomputed: B2 on SOC 2 alone at 0.5x = 1.0, down from 2.0.

**G4 (MINOR). A1 is scored although its own text says no evidence.**
The A1 text reads "NO EVIDENCE FOUND for QMS itself" and "WEAK, optionality
only (see Optionality Register)". The scorecard still gives LL x 1.0 = 1.0.
The evidence is a binding MOU for BeamOptics, which is not completed and had
Rs 1.14 Cr FY26 revenue. H1 credits the same MOU, and the optionality
register carries it too. Rule 5 of 07 says never force-fit.
Recomputed: A1 = 0.

**G5 (MINOR). The completionist recount line does not reconcile.**
The text lists six documented items (HEINE, Saarathi completion, BeamOptics
MOU, SOC 2, HCAH scheme, capex line). It counts "5 items across 4 scored
categories" but names three (B2, H1, H2). A1 also carries a documented
BeamOptics item. A separate sentence says "the two ... categories" and then
lists five. The recount was done, but its line needs restating.

**G6 (MINOR). capex_embedded_growth_pct is 0 in YAML and NOT FOUND in text.**
Section 2C says NOT FOUND and says "this 0/NOT-FOUND figure" should carry
forward. A numeric 0 downstream reads as a measured zero. The emitted value
should be NOT FOUND, or 0 labelled "no capex programme".

### Emerging Moat recomputation

| Reading | Adjusted score | Class |
|---------|---------------|-------|
| As reported | 17.1 | MODEST |
| G1 matrix fix (rule-mandated) | 14.25 | MODEST |
| G1 + G3 + G4 | 12.25 | MODEST (at the 12 floor) |

MODEST holds and the EM >= 25 UA qualifier stays NOT MET in all readings.
Note for downstream: the fully corrected score sits 0.25 above the NONE band.
One more down-tier on any scored row moves the class to NO MEANINGFUL
EMERGING MOAT. The combined assessment (6D, AVERAGE) does not change.

---

## 3. VALUATION (B11), EXPECTATION LEDGER, NARRATIVE

PENDING PHASE 3. Not run. B10/B11 do not exist yet. The valuation framework
docs were not loaded, per the phase-1 scope rule.

---

## 4. SUMMARY

- Rules checked: 63 (Gate 0 40, Emerging Moat 23). Passed: 50. Acceptance
  rate: 79.4%.
- CRITICAL 0, MAJOR 3 (F1, F2, G1), MINOR 9.
- No finding changes a classification. Gate 0 stays AVERAGE (core 48-58
  across readings). EM stays MODEST (12-17).
- Rework advice: none is triggered under the orchestrator rule, since
  acceptance is at or above 60% and Verifier C has no CRITICAL. Corrections
  to carry forward are E4 = 5 with its anchor, B2/B3 re-scored to N/A or to
  the bounded values with DB2 recorded, and LM = 1 in the EM scorecard.

```yaml
stage: B12c
company: "QMSMEDI"
run_date: "2026-09-26"
model: claude-opus-5-5
status: complete
scope: "PHASE 1 ONLY (Gate 0 B01 + Emerging Moat B07). Valuation audit (B10/B11), expectation ledger and narrative checks PENDING PHASE 3."
gate0:
  rules_checked: 40
  fails:
    - {rule: "B2 FCF-positive years", severity: MAJOR, reported: 5, recomputed: "0 strict (rule 5 N/A) | max 4 bounded (FY22 CFO -1.72, FY23 CFO -7.54 force negative FCF)"}
    - {rule: "B3 cumulative FCF / cumulative PAT", severity: MAJOR, reported: 5, recomputed: "0 strict | max 3 bounded (ceiling (43.28 - 8.62) / 63.49 = 0.546)"}
    - {rule: "E4 contingent liabilities / net worth", severity: MAJOR, reported: 0, recomputed: "5 (Rs 5.30 lakh TDS demand, Annual_Report_2026.txt Note 42 line 9442 standalone, Note 40 line 12945 consolidated; vs NW Rs 104.20 Cr = 0.05%)"}
    - {rule: "Deal-breaker 2 (Block B < 8)", severity: MINOR, reported: "not triggered", recomputed: "triggers under strict reading (Block B = 1); cap GOOD, non-binding under AVERAGE"}
    - {rule: "M11 tier-3 reasoning", severity: MINOR, reported: 0, recomputed: "0 or 1; report says rising selling % fails every tier, but tier 3 requires rising selling %; outcome turns on growth window (16.61% full period clears >15%, 13.54% latest 3yr does not)"}
    - {rule: "E2 3-year window", severity: MINOR, reported: 0, recomputed: "0 (score stands); rationale 'short listing history' unsupported; correct label is 3-year-ago SHP not in corpus (only 2025-06-30, 2026-03-31, 2026-06-30 files)"}
  recomputed_core: "48 (strict rule 5) to 55 (bounded) ; 58 if only E4 corrected"
  recomputed_classification: "AVERAGE (unchanged in every reading)"
emoat:
  rules_checked: 23
  fails:
    - {rule: "Likelihood x impact matrix (ML/LM = 1)", severity: MAJOR, reported: "D1, D2, F2, R1 scored LM = 2", recomputed: "LM = 1; total 17.1 -> 14.25"}
    - {rule: "Mixed-tier multiplier", severity: MINOR, reported: "F2 0.85, R1 0.6 averaged", recomputed: "no averaging rule exists in 07; state the governing tier"}
    - {rule: "Score consistent with stated tier (B2)", severity: MINOR, reported: "MM x 1.0 (documented)", recomputed: "report states SOC2-to-contract link is inference; HEINE exclusivity also credited in H2; 1.0 at 0.5x"}
    - {rule: "No force-fit / one item one mechanism (A1)", severity: MINOR, reported: "LL x 1.0 = 1.0", recomputed: "0; text says NO EVIDENCE FOUND for QMS, optionality only; BeamOptics MOU also credited in H1 and registered as optionality"}
    - {rule: "Completionist recount line accuracy", severity: MINOR, reported: "5 items across 4 categories", recomputed: "6 items listed (5 moat + 1 capex); categories named are B2, H1, H2 (3) while A1 also carries a documented BeamOptics item"}
    - {rule: "Section 5 all 23 rows shown", severity: MINOR, reported: "12 zero rows collapsed into one line", recomputed: "presentational; all 23 accounted for"}
    - {rule: "capex_embedded_growth_pct consistent with 2C", severity: MINOR, reported: "YAML 0, text NOT FOUND", recomputed: "NOT FOUND (or 0 with 'no programme' label); pick one"}
  recomputed_em_score: "14 (matrix fix only, rule-mandated); 12 if A1 and B2 also corrected"
  recomputed_em_classification: "MODEST (unchanged; 12.25 sits at the 12 band floor)"
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: [], status: "PENDING PHASE 3"}
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: [], status: "PENDING STAGE 13"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MAJOR, location: "01-gate0.md Block B, B2/B3", issue: "FCF metrics scored on a 2-year FY25-FY26 sub-window that holds Rs 44.86 Cr of CFO against Rs 43.28 Cr for all 8 years; rule 5 requires N/A = 0; FY22/FY23 negative CFO proves FCF negative in those years regardless of capex", recomputed: "Block B 11 -> 1 strict (DB2 fires) or <= 8 bounded; classification AVERAGE unchanged"}
  - {severity: MAJOR, location: "01-gate0.md Block E, E4; B01 input_gaps", issue: "Contingent liability note declared absent but present (Rs 5.30 lakh TDS demand, Annual_Report_2026.txt line 9442 Note 42 and line 12945 Note 40); N/A score applied to disclosed data. Number existence is Verifier A's domain; the scoring rule is misapplied", recomputed: "E4 = 5; Block E 10 -> 15"}
  - {severity: MAJOR, location: "07-emoat.md Section 5, rows D1/D2/F2/R1", issue: "LM scored raw 2; rule is ML/LM = 1", recomputed: "EM 17.1 -> 14.25; MODEST unchanged"}
  - {severity: MINOR, location: "B01 deal_breakers", issue: "DB2 not recorded under the strict B2/B3 reading", recomputed: "DB2 fires, cap GOOD, non-binding"}
  - {severity: MINOR, location: "01-gate0.md M11", issue: "tier-3 condition misread", recomputed: "0 or 1; moat count unchanged"}
  - {severity: MINOR, location: "01-gate0.md E2 / B01 data_notes", issue: "1-year window justified by an unsupported 'short listing history'; true cause is corpus gap", recomputed: "score 0 stands"}
  - {severity: MINOR, location: "07-emoat.md Section 5 F2/R1", issue: "averaged multipliers not in rule", recomputed: "state governing tier"}
  - {severity: MINOR, location: "07-emoat.md B2", issue: "documented multiplier on an effect the report calls inference; HEINE double-credited with H2", recomputed: "B2 2.0 -> 1.0"}
  - {severity: MINOR, location: "07-emoat.md A1", issue: "scored while text says NO EVIDENCE FOUND / optionality only; BeamOptics credited in A1 and H1", recomputed: "A1 1.0 -> 0"}
  - {severity: MINOR, location: "07-emoat.md completionist recount / B07 completionist_recount", issue: "item and category counts do not reconcile with the listed items", recomputed: "restate count"}
  - {severity: MINOR, location: "07-emoat.md Section 5 table", issue: "12 zero rows collapsed", recomputed: "presentational"}
  - {severity: MINOR, location: "B07 capex_embedded_growth_pct", issue: "0 in YAML vs NOT FOUND in text", recomputed: "NOT FOUND"}
critical_count: 0
major_count: 3
minor_count: 9
acceptance_rate: 79.4   # 50 passed of 63 checked (gate0 34/40, emoat 16/23); phase-1 scope only
```
