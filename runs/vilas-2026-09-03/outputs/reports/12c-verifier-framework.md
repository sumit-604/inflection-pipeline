# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)

Run: vilas-2026-09-03 | Company: VILAS (Vilas Transcore Ltd) | Model: claude-opus-4-8

SCOPE: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07) compliance.
Valuation adherence (B10/B11) is DEFERRED to phase 3 and is not audited here.

Method: rule application only, not company quality and not raw-number source
fidelity (Verifier A owns whether a number exists in the source PDF). Every
block score below is re-derived from the stated inputs using the stated
thresholds; the recomputed value sits beside any deviation.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Rule source: prompts/01-gate-0-pipeline.md. All numbers taken as stated in
B01 (their source fidelity is Verifier A's gate, not mine).

### Block A — Return on Capital (thresholds re-applied)

| Line | Input (as stated) | Threshold band | Score claimed | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 17.47% (4th of 7 sorted) | 15-19.9 = 3 | 3 | 3 | PASS |
| A2 Min single-year ROCE | 5.86% (FY20) | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | 15.27% (4th of 7 sorted) | 15-19.9 = 4 | 4 | 4 | PASS |
| A4 ROCE trend latest vs earliest | FY26 16.23 vs FY20 5.86 | latest >= earliest = 5 | 5 | 5 | PASS |

Median sort verified: 5.86 / 8.05 / 16.23 / 17.47 / 19.84 / 20.60 / 22.00 →
4th value 17.47. ROE sort: 3.76 / 5.34 / 12.83 / 15.27 / 15.58 / 15.88 /
16.45 → 4th value 15.27. Block A total 12/20. PASS.

MINOR (documented): the ROCE series mixes two capital-employed bases — FY20-23
on Net Worth + Borrowings, FY24-26 on the exact Total Assets − Current
Liabilities. The prompt lists ROCE = EBIT ÷ (Total Assets − Current
Liabilities) under "FORMULA DEFINITIONS (fixed, do not substitute
alternatives)." The FY20-23 substitution is a formula deviation. It is forced
by the missing CL split in screener, fully disclosed in the basis note and
data_notes, and does not move any A-block score across a band (the two
substituted low years drive A2=0 regardless; the median lands on an
exact-basis year). Non-decision-changing.

### Block B — Cash Generation Quality

| Line | Input | Threshold band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 79.55/143.76 = 0.553 | 0.50-0.69 = 1 | 1 | 1 | PASS |
| B2 FCF-positive years | 5 of 7 = 71.4% | 50-74 = 2 | 2 | 2 | PASS |
| B3 Cum FCF/PAT | −21.55/143.76 = −0.15 | negative = 0 | 0 | 0 | PASS |
| B4 Change WC days | FY24 41.38 → FY26 96.47 = +55.1 | increased >15 = 0 | 0 | 0 | PASS |

Cumulative CFO re-summed: 21.69+19.76+12.91+13.19+49.16−35.46−1.70 = 79.55.
Cumulative PAT re-summed: 3.60+5.23+17.91+20.21+23.08+34.17+39.56 = 143.76.
Cumulative FCF re-summed: 21.16+19.27+11.09+2.55+39.17−73.93−40.85 = −21.55.
All tie. Block B total 3/20. PASS.

MINOR (documented): two deviations from the fixed formulas, both disclosed and
non-decision-changing. (a) FCF capex for FY20-24 uses total Cash from Investing
Activities as a proxy, not the defined "purchase of PPE + intangibles"; this
feeds only B2/B3, and Block B is already at 3/20 and deal-breakered. (b) B4 is
computed FY24-vs-FY26, not the rule's "latest vs earliest" (FY20 vs FY26),
because Trade Payables is not broken out for FY20-23; the direction (worsening
>15 days) is unambiguous either way.

### Block C — Growth

| Line | Input | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | (460.67/161.91)^(1/6)−1 = 19.03% | 15-19.9 = 4 | 4 | 4 | PASS |
| C2 PAT CAGR | (39.56/3.60)^(1/6)−1 = 49.12% | >=20 = 5 | 5 | 5 | PASS |
| C3 Positive YoY yrs | 5 of 6 = 83.3% | 75-99 = 3 | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | 49.12 − 19.03 = +30.09pp | >=+3 = 5 | 5 | 5 | PASS |

CAGR edge rules honoured: no negative/zero endpoints (PAT positive all years,
noted correctly in data_notes as "no loss-to-profit swing"), so no N/M marks
required. Block C total 17/20. PASS.

### Block D — Balance Sheet Strength (latest = FY26)

| Line | Input | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | Borrow 38.96 − Cash 94.36 = net cash | net cash = 5 | 5 | 5 | PASS |
| D2 Interest Coverage | 53.77/2.12 = 25.4x | >=10 = 5 | 5 | 5 | PASS |
| D3 Debt/Equity | 38.96/328.53 = 0.119 | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 Current Ratio | 287.51/75.05 = 3.83x | >=2.0 = 5 | 5 | 5 | PASS |

Block D total 19/20. PASS. (Converter/non-financial, so the standard D1/D2
rows apply, not the bank CAR/PCR variants. Correct.)

### Block E — Shareholder Alignment

| Line | Input | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 73.14% | >=60 = 5 | 5 | 5 | PASS |
| E2 Holding change | 73.17 → 73.14 = −0.03pp | +-1% = 3 | 3 | 3 | PASS |
| E3 Pledge | N/A (not in data) | score 0 | 0 | 0 | PASS |
| E4 Contingent liab/NW | N/A (not in data) | score 0 | 0 | 0 | PASS |

E3/E4 correctly scored 0 under the grounded-claims rule (data absent, not
estimated). Block E total 8/20. PASS. E2's ~2-year window (post-May-2024 IPO)
short of the assumed 3-year window is disclosed, not papered over.

### Block F — Quantitative Moat (12 tests)

| Test | Basis stated | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| M1 Pricing Power | margin +6.75pp (>=2) AND rev CAGR 19.03 (>=10) | =5 | 5 | 5 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED | =0 | 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 4.38x, ROCE 16.23 (>2x AND >15%) | =3 | 3 | 3 | PASS |
| M4 Customer Stickiness | 1 decline yr recovered | =3 | 3 | 3 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED | =0 | 0 | 0 | PASS |
| M6 Technology/R&D | not disclosed | =0 | 0 | 0 | PASS |
| M7 Regulatory/License | player count not quantified | =0 | 0 | 0 | PASS |
| M8 Distribution | not quantified | =0 | 0 | 0 | PASS |
| M9 Brand | PEER DATA NEEDED | =0 | 0 | 0 | PASS |
| M10 Switching Costs | growth all but 1 yr, rec days net down | =3 | 3 | 3 | PASS |
| M11 Network Effects | latest-3yr CAGR 17.69 < prior 20.41, selling% rising | =1 | 1 | 1 | PASS |
| M12 Negative WC/Float | WC days positive, rising | =0 | 0 | 0 | PASS |

Moat score re-summed: 5+0+3+3+0+0+0+0+0+3+1+0 = 15/60. Moats present (>=3):
M1, M3, M4, M10 = 4. Classification band "4-5 = STRONG." PASS. PEER DATA NEEDED
correctly scored 0 (never guessed), per the M-block rule.

### Classification, deal-breakers, confidence

- Core score 12+3+17+19+8 = 59/100. Re-derived 59. PASS.
- Grand total 59+15 = 74 (informational; matrix uses Core + moat class). PASS.
- Classification matrix: Core 59 in the "40-59" band → AVERAGE regardless of
  moat class (overlay applies only at Core >=60). Re-derived AVERAGE. PASS.
  The STRONG moat class correctly does NOT lift AVERAGE at Core 59.
- Deal-breaker sweep (all 9): Rule 2 (Block B 3 <8 → max GOOD) TRIGGERED and
  recorded, correctly noted non-binding since AVERAGE already sits below GOOD,
  with the driving years (FY25, FY26) named per the "state WHICH years" rule.
  Rule 4 (cum CFO/PAT <0.50 → max AVERAGE): 0.553 >= 0.50, correctly NOT
  triggered. Rules 1,3,5,6,7,8,9 correctly not triggered. PASS.
- Data confidence: 7 years → "7-9 = moderate," no history downgrade (applies
  only below 5 years). history_downgrade: false. PASS.
- No STOP/halt asserted; AVERAGE carried forward as evidence, correct per the
  NEVER-halt-on-quality rule.

GATE 0 VERDICT: every block score, the classification matrix, the deal-breaker
sweep, the CAGR edge rules, and the confidence tier are applied as written. No
CRITICAL, no MAJOR. Three MINOR formula-substitution notes, all data-forced,
disclosed, and non-decision-changing.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Rule source: prompts/07-emerging-moat-pipeline.md.

### Completeness — 23 rows addressed

All 22 categories plus R1 are addressed or explicitly marked NO EVIDENCE
FOUND (A2, A3, A4, B1, B2, B3, C2, D1, D2, E1, E2, G1, G2 = NO EVIDENCE, each
with a reason). Categories 21 (I1) and 22 (I2) are both present. PASS.

### Scorecard — raw matrix and evidence multipliers re-derived

| # | Likelihood/Impact | Raw (matrix) | Evidence | Mult | Adjusted claimed | Re-derived | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | M/M | 2 | management | 0.7 | 1.4 | 1.4 | PASS |
| C1 | H/M | 3 | management | 0.7 | 2.1 | 2.1 | PASS |
| F1 | L/M | 1 | management | 0.7 | 0.7 | 0.7 | PASS |
| F2 | H/M | 3 | management | 0.7 | 2.1 | 2.1 | PASS |
| H1 | L/L | 1 | inference | 0.5 | 0.5 | 0.5 | PASS |
| H2 | L/H | 2 | management | 0.7 | 1.4 | 1.4 | PASS |
| H3 | L/L | 1 | management | 0.7 | 0.7 | 0.7 | PASS |
| R1 | M/H | 3 | management | 0.7 | 2.1 | 2.1 | PASS |
| I1 | — | 0 | — | — | 0 | 0 | PASS |
| I2 | — | 0 | — | — | 0 | 0 | PASS |
| all others | no evidence | 0 | — | — | 0 | 0 | PASS |

Matrix values verified against HH=4 / HM,MH=3 / HL,MM,LH=2 / ML,LM=1 / LL=1 /
none=0. Adjusted total re-summed: 1.4+2.1+0.7+2.1+0.5+1.4+0.7+2.1 = 11.0.
Claimed 11.0. PASS.

### Classification band

Adjusted total 11 → "<12 = NO MEANINGFUL EMERGING MOAT." em_classification
"NONE." Re-derived NONE. PASS. Bands applied absolute per the 20-Aug-2026
operator ruling (no rescale); ceiling stated as 92. PASS.

### Evidence-tier discipline (the key B07 test)

No category was scored as 📄 (1.0x). Every non-zero row used 0.7x (management)
or 0.5x (inference). F2 carries genuine 📄 items (Unit 3 on-time
commissioning, FY25 above-nameplate output) yet was still discounted to 0.7x —
conservative, and the opposite of the failure mode the rule guards against
(a management-claim category scoring as if documented). No tier inflation
found. PASS.

### Completionist recount

Base rate is 3-6 categories; only 3 rows score Strong/Moderate (C1, F2, R1) —
an honest sparse scan, well below the 12-category over-crediting trigger. The
recount line is present: "📄 recount performed: 5 documented items across 2
categories." PASS.

MINOR (labeling): the completionist_recount states "5 documented items" while
evidence_mix.documented = 12. The two count different scopes — 12 is all
documented evidence pieces across the whole report (including Section 1/2 and
context-only items such as the ICRA action and IPO fund-utilisation table); 5
is the subset feeding scored moat rows. Both are internally defensible, but the
report does not reconcile the two figures, and a reader could read them as a
contradiction. Cosmetic; no score effect.

### Categories 21 and 22 (Verifier C rule 8)

- I1 (Talent Asymmetry): scored 0. Correct — leg (a) has one credentialed
  individual at a 25%-owned JV, short of a "class"; leg (b) has no
  competitor-economics evidence. The rule bars a score above 0 without both
  legs and a 📄 (b) source; 0 is compliant. PASS.
- I2 (Cannibalization Barrier): scored 0. Correct — the report runs the test
  and shows the honest answer is "nothing must be destroyed" (TRIL
  backward-integrated into CRGO lamination and still buys from VILAS), which
  the rule scores as execution lead, not configuration. PASS.
- I1/I2 contribution stated separately ("0") per the operator ruling. PASS.

### Combined assessment (6C/6D)

6C uses the injected Gate 0 block as-is (Core 59, 4 confirmed moats, AVERAGE).
6D returns AVERAGE, correctly applying the EM>=25 qualifier: EM 11 < 25, so the
forward overlay cannot lift the backward classification, and the setup is
correctly identified as NOT a HIGH POTENTIAL / TURNAROUND transition (forward
score is NONE, not EXPANSION). PASS. active_categories lists only the three
Strong/Moderate rows, per the "only Strong/Moderate rows" rule. PASS.
capex_embedded_growth_pct 46 matches the shown 2C arithmetic (Rs37.5 Cr x 5.66x
= Rs212 Cr; /Rs460.7 Cr = 46%), correctly excluding already-commissioned Unit 3.
PASS.

EMERGING MOAT VERDICT: 23 rows addressed, raw matrix and evidence multipliers
correctly applied, tier discipline strict (no 📄 inflation), completionist
recount performed, I1/I2 rules honoured, combined-assessment rule correct. No
CRITICAL, no MAJOR. One MINOR labeling note.

---

## PART 3 — VALUATION (B10/B11) ADHERENCE

PENDING — deferred to phase 3. B10/B11 do not exist for this run and the
valuation framework docs (Master v3.6 Role 1, the Section 1B layer set, FTTCP
v2.1) are out of scope for this phase-1 pass. Not audited.

---

## SUMMARY

Both in-scope frameworks were applied as written. Gate 0 re-derives to the
same 59/100 core, 15/60 moat, STRONG moat class, AVERAGE classification, with
the deal-breaker sweep and CAGR edge rules correct. Emerging Moat re-derives to
the same 11/92, NONE, AVERAGE combined, with strict evidence-tier discipline
and the I1/I2 structural rules correctly returning 0. No CRITICAL and no MAJOR
finding in either. Four MINOR findings, all disclosure/labeling imprecision,
none affecting a score or the classification. No REWORK trigger.

```yaml
stage: B12c
company: "VILAS"
run_date: "2026-09-03"
model: claude-opus-4-8
status: complete
scope: phase-1  # Gate 0 + Emerging Moat only; valuation deferred to phase 3
gate0:
  rules_checked: 20
  fails:
    - {severity: MINOR, rule: "ROCE formula (fixed) — FY20-23 use Net Worth + Borrowings, not Total Assets − Current Liabilities", note: "data-forced (CL split absent in screener), disclosed, non-decision-changing; A-block scores unchanged"}
    - {severity: MINOR, rule: "FCF formula (fixed) — FY20-24 capex proxied by total Cash from Investing, not PPE+intangibles", note: "disclosed; feeds only B2/B3, Block B already 3/20 and deal-breakered"}
    - {severity: MINOR, rule: "B4 latest-vs-earliest — computed FY24 vs FY26, not FY20 vs FY26", note: "Trade Payables not broken out FY20-23; disclosed; direction (worsening >15d) unambiguous, score 0 unchanged"}
emoat:
  rules_checked: 12
  fails:
    - {severity: MINOR, rule: "completionist_recount vs evidence_mix labeling", note: "recount says 5 documented items, evidence_mix.documented=12; different scopes (scored-row 📄 subset vs all 📄 items), not reconciled in-report; cosmetic, no score effect"}
valuation: {rules_checked: 0, fails: [], status: pending, note: "deferred to phase 3; B10/B11 absent and valuation framework docs out of phase-1 scope"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # not in phase-1 scope (stage 13 not audited)
recomputed_destination_pe: ""   # concur / not applicable in phase-1 scope
recomputed_decision: ""         # concur: Gate 0 AVERAGE, Emerging Moat NONE, combined AVERAGE
findings:
  - {severity: MINOR, location: "01-gate0.md Block A / basis note", description: "ROCE for FY20-23 computed on Net Worth + Borrowings, a substitution for the fixed Total Assets − Current Liabilities denominator; data-forced, disclosed, no A-block score changes across a band"}
  - {severity: MINOR, location: "01-gate0.md Block B / data_notes", description: "FCF capex for FY20-24 proxied by total Cash from Investing Activities rather than the fixed PPE+intangibles definition; disclosed, feeds only B2/B3 which sit inside an already deal-breakered Block B"}
  - {severity: MINOR, location: "01-gate0.md Block B B4", description: "WC-days change computed FY24 vs FY26 rather than the rule's latest-vs-earliest (FY20 vs FY26) because Trade Payables is not broken out FY20-23; disclosed, direction and score 0 unaffected"}
  - {severity: MINOR, location: "07-emoat.md Section 3 recount vs B07 evidence_mix", description: "completionist_recount reports 5 documented items while evidence_mix.documented=12; the two count different scopes and are not reconciled in the report; cosmetic, no score impact"}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100   # no rule materially misapplied; all 4 findings are MINOR imprecision/labeling per the severity scale
```
