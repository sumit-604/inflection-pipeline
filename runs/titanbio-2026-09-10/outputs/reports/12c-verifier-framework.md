# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: Titan Biotech Ltd (TITANBIO) | Run date: 2026-09-16
Model: claude-opus-5 | Emits: B12c

SCOPE. Phase 1 only: Gate 0 (B01) and Emerging Moat (B07). Stages 10 and 11
have not run; B10 and B11 do not exist. The valuation-adherence audit
(verifier rules 4, 7, 11-15), the Expectation Ledger audit (rules 13-14) and
the Business Understanding Narrative audit (rule 9) are NOT RUN here and are
deferred to phase 3. No valuation framework document was read.

RULE SOURCES READ IN FULL:
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md
- prompts/00-orchestrator.md lines 323-341 (NO-CONCALL MODE), for the F2
  substitution only.

ARTIFACTS AUDITED:
- runs/titanbio-2026-09-10/outputs/reports/01-gate0.md
- runs/titanbio-2026-09-10/outputs/blocks/B01-gate0.yaml
- runs/titanbio-2026-09-10/outputs/reports/07-emoat.md
- runs/titanbio-2026-09-10/outputs/blocks/B07-emoat.yaml

I audit rule application. I do not audit company quality, and I do not audit
whether a number exists in a source PDF (Verifier A owns that, and its
source-fidelity verdicts are non-overridable). Every recomputation below uses
ONLY the inputs the reports themselves state.

---

## HEADLINE

One CRITICAL. The Gate 0 working-capital-days line applies the framework's own
Payable Days formula with a 10x unit error. Correcting it on the report's own
stated inputs and its own stated revenue basis moves B4 from 5 to 3 and M12
from 1 to 0. Core score falls 81 to 79, moat score 15 to 14, grand total 96 to
93, and the classification flips GOOD+ to GOOD. The error also propagates into
`block_b_trend`, the B01 analyst_note, and B07's G2 category write-up.

Everything else in Gate 0 re-derives cleanly. The Emerging Moat scan is
methodologically sound: 23 categories addressed, multipliers correct, recount
performed, adverse evidence correctly separated from absent evidence, no FTTCP
content, no imported valuation arithmetic. Its defects are block-schema and
label-selection issues, not scoring issues.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### 1.1 Block A: Return on Capital — re-derived, all PASS

Stated inputs: ROCE FY23 24.37, FY24 23.07, FY25 16.11, FY26 22.76 (AR Note 45
own-year columns). ROE FY23 19.13, FY24 17.73, FY25 11.91, FY26 17.84.

| Rule | Stated inputs | Re-derived | Reported | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | sorted 16.11 / 22.76 / 23.07 / 24.37 | median 22.92% → band 20-24.9 | 4 | PASS |
| A2 Min single-year ROCE | 16.11% | ≥15% band | 5 | PASS |
| A3 Median ROE | sorted 11.91 / 17.73 / 17.84 / 19.13 | median 17.79% → band 15-19.9 | 4 | PASS |
| A4 ROCE trend | 22.76 vs 24.37 | −1.61pp → band decline 1-3pp | 3 | PASS |

Block A total 16/20 re-derives exactly. Formula-definition rule 1 honoured: the
source's own ROCE was used and anchored rather than computed. The 10-year
computed ROE cross-check (median 18.83%, same band) is a legitimate extra, not
a substituted figure.

### 1.2 Block B: Cash Generation — one CRITICAL

| Rule | Stated inputs | Re-derived | Reported | Verdict |
|---|---|---|---|---|
| B1 Cum CFO / Cum PAT | CFO 147.61, PAT 168.44 (10yr) | 0.8763 → band 0.85-0.99 | 4 | PASS |
| B2 FCF-positive years | 4 of 4 (FY23-FY26) | 100% band | 5 | PASS |
| B3 Cum FCF / Cum PAT | FCF 53.52, PAT 101.11 (4yr) | 0.529 → band 0.40-0.59 | 3 | PASS |
| B4 Change in WC Days | see below | −3.18 days → band ±5 | 5 | **FAIL, recomputed 3** |

I re-added both 10-year series digit by digit: CFO 147.61 and PAT 168.44 are
correct as stated.

**FINDING C-01 (CRITICAL). B4 Payable Days: the stated formula is applied with
a 10x unit error, and the resulting WC-days series is internally impossible.**

The framework defines Payable Days = Trade Payables ÷ Revenue × 365. The report
states Trade Payables in Rs lakh and Revenue in Rs crore, then divides without
converting correctly (revenue was scaled by 10 instead of 100).

| FY | Trade Payables (report's own figure) | Revenue (report's own figure) | Payable Days as reported | Payable Days re-derived |
|---|---|---|---|---|
| FY23 | Rs 554.97 lakh = Rs 5.55 cr | Rs 144.00 cr | 140.66 | **14.07** |
| FY24 | Rs 336.82 lakh = Rs 3.37 cr | Rs 164.07 cr | 74.94 | **7.49** |
| FY25 | Rs 521.65 lakh = Rs 5.22 cr | Rs 156.45 cr | 121.68 | **12.17** |
| FY26 reported rev | Rs 854.10 lakh = Rs 8.54 cr | Rs 206.19 cr | 151.19 | **15.12** |
| FY26 adjusted rev | Rs 854.10 lakh = Rs 8.54 cr | Rs 200.35 cr | 155.63 | **15.56** |

Two independent checks confirm the direction of the error, both using only the
report's own numbers:

1. The report's FY25 payable days of 121.68 imply payables of Rs 52.15 cr
   (Rs 5,215 lakh). The same report states FY25 Total Current Liabilities =
   Rs 1,773.64 lakh (Rs 17.74 cr). Payables cannot be three times total current
   liabilities. The receivable and inventory legs do not carry the error: the
   report's 40.41 receivable days sits close to the AR-disclosed trade
   receivables turnover of 9.90x (36.9 days), so only the payables leg is wrong.
2. The error is exactly 10x in every one of the five rows, the signature of a
   crore-to-lakh conversion applied once instead of twice.

Corrected WC Days, using the report's own receivable and inventory days:

| FY | Recv | Inv | Pay (corrected) | WC Days (corrected) | WC Days (as reported) |
|---|---|---|---|---|---|
| FY23 | 53.24 | 91.68 | 14.07 | **130.85** | 4.26 |
| FY24 | 41.52 | 101.36 | 7.49 | **135.39** | 67.94 |
| FY25 | 43.90 | 118.32 | 12.17 | **150.05** | 40.54 |
| FY26 reported rev | 40.41 | 98.72 | 15.12 | **124.01** | −12.06 |
| FY26 adjusted rev | 41.60 | 101.63 | 15.56 | **127.67** | −12.40 |

B4 re-scored on the report's OWN declared basis (it states: "Change, FY26
(adjusted, −12.40) vs FY23 (4.26)"): 127.67 − 130.85 = −3.18 days → band
"±5 days" → **Score 3**, not 5.

Basis sensitivity, stated for honesty: on the reported-revenue row the change
is −6.84 days, which would hold B4 at 5 and hold the classification at GOOD+.
The report chose the adjusted basis for this line and must be re-scored on the
basis it chose. The operator should note that B4 is basis-sensitive once the
unit error is fixed, and that the freight-gross-up adjustment therefore
becomes score-bearing at B4 (it is band-neutral at C1, C4, M1, M2, M3, M9 and
M11 — I checked each).

Block B re-derived total: 4 + 5 + 3 + 3 = **15/20**, not 17/20.

**FINDING C-03 (MAJOR). `block_b_trend` and the analyst_note assert a
working-capital release that the corrected series does not show.** The block
states "WC days swung from +4.26 (FY23) to −12.40 (FY26, adjusted basis),
driven by a jump in FY26 trade payables". Corrected, WC days moved 130.85 to
127.67, roughly flat, and the payables leg is a 14-to-16-day line that cannot
drive a swing of that size. The FLAG-CASH feed and the B01 analyst_note claim
("the working-capital release (WC days −12.4) ... freed up" cash) both rest on
the erroneous series. This assertion propagated downstream into B07's G2
write-up, which repeats "WC days per B01 swung from +4.26 (FY23) to −12.40".
B07 is not at fault for the arithmetic; it used the injected block as
instructed. The correction must be made at B01 and re-fed.

Note: Block B stays above the deal-breaker floor of 8 after correction, so
deal-breaker 2 remains untriggered.

### 1.3 Block C: Growth — re-derived, all PASS

| Rule | Re-derived | Reported | Verdict |
|---|---|---|---|
| C1 Revenue CAGR FY17 52.74 → FY26 200.35, 9yr | 15.99% → band 15-19.9 | 4 | PASS |
| C2 PAT CAGR 2.18 → 29.89, 9yr | 33.76% → band ≥20 | 5 | PASS |
| C3 Positive YoY years | 7 of 9 = 77.8% → band 75-99 | 3 | PASS |
| C4 PAT CAGR − Rev CAGR | +17.78pp → band ≥+3 | 5 | PASS |

CAGR edge rules honoured: no endpoint is negative or zero, no loss-to-profit
swing exists (all ten years positive, stated), so no synthetic CAGR was
attempted and C4 was correctly scored rather than zeroed. The non-monotonic
FY21 spike is disclosed in data_notes as the edge rules intend. Reported-basis
cross-check (16.35%) lands in the same band, correctly stated.

### 1.4 Block D: Balance Sheet — re-derived, all PASS

EBITDA build 38.17 − 5.41 + 4.93 + 0.91 = 38.60 is correct arithmetic.

| Rule | Re-derived | Reported | Verdict |
|---|---|---|---|
| D1 Net Debt / EBITDA | (5.71 − 1.87) / 38.60 = 0.0995x → band 0-1.0x | 4 | PASS |
| D2 Interest Coverage | 39.08 / 0.91 = 42.9x → band ≥10x | 5 | PASS |
| D3 Debt / Equity | 5.71 / 181.54 = 0.031 → band <0.1 | 5 | PASS |
| D4 Current Ratio | 3.28x → band ≥2.0 | 5 | PASS |

D1 correctly withheld the "net cash = 5" band: net debt is positive (Rs 3.84
cr), so band 0-1.0x = 4 is right. Block D total 19/20 re-derives.

### 1.5 Block E: Shareholder Alignment — re-derived, all PASS

| Rule | Re-derived | Reported | Verdict |
|---|---|---|---|
| E1 Promoter holding 55.78% | band 50-59.9 | 4 | PASS |
| E2 3-year change −0.10pp | band ±1% | 3 | PASS |
| E3 Pledge NOT FOUND | rule 5 → score 0 | 0 | PASS |
| E4 Contingent liab / NW 0.51% | band <5% | 5 | PASS |

**E3 is the disclosure-absent-versus-adverse test, and B01 passes it cleanly.**
The report says the disclosure does not exist ("NOT FOUND ... no pledge or
encumbrance disclosure located ... searched 'pledge', 'encumbered'"), scores 0
per the framework's own rule 5, declines to trigger deal-breaker 5 ("cannot
confirm >15% — no trigger (not estimated)"), and then names the gap again in
the weakest-block commentary as "driven entirely by the E3 pledge data gap ...
rather than a promoter-quality finding". That is the correct handling: the zero
is recorded as a missing disclosure, not as adverse evidence, and it is
prevented from firing an override it cannot support.

E4's exclusion of the Rs 406.86 lakh uncalled liability (classified as a
Commitment in the note, not a Contingent Liability) is stated and non-material:
including it gives 2.75%, still band <5%, score 5 either way.

Block E total 12/20 re-derives.

### 1.6 Block F: 12 Moat Tests — one MAJOR

| Test | Re-derived from stated inputs | Reported | Verdict |
|---|---|---|---|
| M1 Pricing Power | margin 10.16% → 19.27% = +9.11pp (≥2pp) AND CAGR 15.99% (≥10%) | 5 | PASS |
| M2 Cost Advantage | 19.27% vs peer median 20.52% = 1.25pp below → ±2pp band | 1 | PASS |
| M3 Capital Efficiency | FAT 200.35/61.61 = 3.25x (>3x) AND ROCE 22.76% (>20%) | 5 | PASS |
| M4 Customer Stickiness | 2 decline years, CAGR positive | 1 | PASS |
| M5 Scale & Dominance | top-3 mcap but margin 4th of 4 → top-5 band | 1 | PASS |
| M6 Technology / R&D | 0.27/200.35 = 0.14% < 1% floor | 0 | PASS |
| M7 Regulatory / License | player count NOT FOUND | 0 | PASS |
| M8 Distribution | no quantified reach found | 0 | PASS |
| M9 Brand | GM proxy 50.51% vs peer median 63.22%, below | 0 | PASS |
| M10 Switching Costs | 2 decline years, overall growth | 1 | PASS |
| M11 Network Effects | latest 3yr 11.64% < prior 3yr 21.94%, and <15% | 0 | PASS |
| M12 Negative WC / Float | all 4 years >45 days (corrected) | 1 | **FAIL, recomputed 0** |

**FINDING C-02 (MAJOR). M12 inherits the C-01 unit error.** The rubric bands
are: negative in majority of years = 5 | 0-15 days consistently = 3 | 15-45 = 1
| >45 = 0. On the corrected series (130.85, 135.39, 150.05, 127.67) every year
exceeds 45 days → **Score 0**, not 1. Block F total re-derives to **14/60**.

**FINDING C-06 (MINOR). The M12 band was reached by an invented test.** The
report writes "median across the 4 years = 22.4 days, placing it in the 15-45
band". The rubric contains no median test; its bands are "negative in a
majority of years" and "0-15 days consistently". A series running −12.40 to
67.94 (as reported) is not "consistently" anything, and taking a median of four
scattered values is a rule the stage supplied for itself.

**FINDING C-07 (MINOR). "PEER DATA NEEDED" marker not used.** Block F's
instruction is explicit: "If a test needs peer data that is not provided, score
0 and mark PEER DATA NEEDED". M7 (segment player count) and the segment-census
leg of M5 are scored on absent data, and the B01 block's `data_notes` comment
line even names "PEER DATA NEEDED items" as the field's purpose, but the string
never appears. The substance is captured in input_gaps line 3, so this is
presentational, and the honest NOT FOUND wording at each test is correct.

Moat classification: 2 tests at ≥3 (M1, M3) → band "2-3 = MODERATE" is
correctly applied, and stays MODERATE after correction. `moats_confirmed: 2`
matches.

### 1.7 Classification, overrides, and framework-level rules

| Rule | Check | Verdict |
|---|---|---|
| Rule 6 opening history line | "Data available: 10 years (FY2017 to FY2026) ... Scoring adapted" present, with the mixed-window explanation | PASS |
| Rule 4 source anchors | every extracted number carries a source; anchors are specific (AR page, note, column) | PASS |
| Rule 5 grounded claims / never estimate | E3, M7, M8 all NOT FOUND and scored 0; no industry-typical fill anywhere | PASS |
| Data confidence tier | see C-08 | **FAIL (MINOR)** |
| Classification matrix | Core 81 + MODERATE → "Core ≥80 + MODERATE = GOOD+" correctly applied as computed | PASS (input now wrong, see below) |
| Deal-breakers 1-9 | all nine enumerated and tested individually; none triggered; none silently skipped | PASS |
| Block and grand totals | 16+17+17+19+12 = 81 and 81+15 = 96 add correctly from the stated line scores | PASS |
| `flags` field rule | FLAG-GATE0 required only if classification ≤ AVERAGE; not required here, and not required after correction to GOOD | PASS |
| YAML schema conformance | every schema key present, no extras | PASS |
| Institutional ownership / UA discipline | see 1.8 | PASS |

**FINDING C-08 (MINOR). The return blocks run on a 4-year window while the
block reports `data_years: 10`, and the effect on A1/A2 is never tested.**
Rule 6 ("use whatever history is available") permits the mixed window, and the
report states the window at each line, so this is not a rule breach. But Block
A and B2-B4 rest on FY23-FY26 only, which excludes FY17-FY20 when PAT ran
Rs 2.18-7.07 cr on revenue of Rs 52.74-79.44 cr. A1 (median ROCE) and A2
(minimum single-year ROCE) are the two scores most exposed to that exclusion,
and the block's headline `data_years: 10` invites a downstream reader to treat
Block A as a ten-year result. The report should have stated, at Block A, that
the return scores are window-limited and would likely fall on a longer window.
Not recomputable here: the corpus has no FY17-FY22 balance-sheet detail, and
inventing one would breach rule 5.

### 1.8 The two CLAUDE.md rules that bear on this stage

**Low institutional ownership is never a risk; UA arithmetic belongs to stage
11.** B01 contains no institutional-ownership risk language. E1 scores promoter
holding on the stated band (55.78% → 4) and correctly leaves the "professionally
managed: 3 if FII+DII >50%" alternative unused, because the company is
promoter-held. No Amendment 3 multiplier, no Raw x 1.25, no sector cap and no
UA qualifier arithmetic appears anywhere in B01 — correct, because the Gate 0
prompt does not ask for it and stage 11 owns it. PASS.

**Verification-priority section.** B01 opens with four findings against the
run's load-bearing facts before scoring. That is not a breach of the stage's
"no qualitative judgments" rule: CLAUDE.md requires every stage to check the
Spear line's load-bearing facts before its own work. The freight gross-up,
Peptech reconciliation, TM Media naming and investing-split findings are all
anchored, and each unresolved sub-question is named rather than filled.

### 1.9 Gate 0 recomputation summary

| Field | Reported | Re-derived | Driver |
|---|---|---|---|
| Block B | 17 | **15** | B4 5 → 3 (C-01) |
| Block F moat score | 15 | **14** | M12 1 → 0 (C-02) |
| Core score | 81 | **79** | Block B |
| Grand total | 96 | **93** | Core + moat |
| moats_confirmed | 2 | 2 | unchanged |
| moat_class | MODERATE | MODERATE | unchanged |
| **classification** | **GOOD+** | **GOOD** | Core 79 falls into "Core 60-79 + else = GOOD" |
| deal_breakers | [] | [] | Block B 15 still ≥ 8 |

Blocks A, C, D and E are unchanged at 16, 17, 19 and 12.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### 2.1 Category coverage and scoring mechanics — PASS

All 22 categories plus R1 are addressed. The Section 3 summary table carries 23
rows; the Section 5 scorecard carries 23 rows. Every category with no evidence
states "NO EVIDENCE FOUND" rather than force-fitting. Source anchors are
present on every evidence item, at AR page and note level.

Raw score matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) and
evidence multipliers (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x) re-derived:

| Cat | Likelihood/Impact | Raw | Type | Multiplier | Adjusted | Verdict |
|---|---|---|---|---|---|---|
| B2 | LL | 1 | 🔍 | 0.5 | 0.5 | PASS |
| E2 | MH | 3 | 🔍 (cause) | 0.5 | 1.5 | PASS |
| G2 | LM | 1 | 📄 | 1.0 | 1.0 | PASS |
| all others | — | 0 | — | — | 0.0 | PASS |

Total 3.0. Classification <12 → NO MEANINGFUL EMERGING MOAT, correctly applied
against the absolute bands (no rescale, per the 20-Aug-2026 operator ruling).
The 92 ceiling is stated. em_score 3 and em_classification "NONE" match the body.

Verifier rule 3 asks whether any 🎙️-only category scores as if 📄. None does.
The error runs the other way at E2: a documented, audited, twice-anchored export
fact is graded 🔍 because its CAUSE is inferred. That is conservative
interpretation of filed evidence, which CLAUDE.md expressly preserves for
document-reading stages, and it is reasoned in the text rather than silently
applied. Sensitivity: grading E2 at 📄 1.0x gives 3.0 for the category and 4.5
in total, still far below the 12-point MODEST band. Non-material either way.

### 2.2 The completionist recount — PASS with one clerical MINOR

The guard triggers at 12+ active categories; this scan has 1, so the guard was
never at risk. The recount was still performed and stated in the required
format: "📄 recount performed: 2 documented items across 2 categories".

**FINDING C-13 (MINOR).** The report body's recount sentence contradicts itself:
"plus 2 categories carry documented ADVERSE evidence (A3, F2, G1 — three
categories ...)". Two, then three, in one sentence. The emitted block gets it
right ("3 additional categories (A3, F2, G1)"). Clerical.

### 2.3 Categories 21 and 22 — PASS

| Check (verifier rule 8) | Finding | Verdict |
|---|---|---|
| I1 present | Category 21 scored and reasoned | PASS |
| I1 above 0 only if both legs evidenced, (b) leg with ≥1 📄 | Part (a) fails first: no named inventors (no patents exist), no ex-DRDO/HAL concentration, no above-norm technical remuneration line; the highest-paid are promoter-family directors. Part (b) correctly declared moot. Score 0 | PASS |
| I2 present | Category 22 scored and reasoned | PASS |
| I2 above 0 only if the named sacrifice is specific | Test applied to the one surviving moat claim (E2) as the rubric directs; answer is "nothing must be destroyed", which the rubric says is an execution lead. Score 0 | PASS |
| I1/I2 contribution stated separately | "I1/I2 contribution: 0.0", with the explicit note that no threshold crossing occurs via I1/I2 and nothing needs flagging for the operator's 10-15-scan review checkpoint | PASS |

This is the rubric applied as written, including the design expectation that
I1/I2 score 0 for typical companies.

### 2.4 Disclosure-absent versus adverse-evidence — PASS, and done well

This is the distinction the task asks me to test, and B07 holds it consistently:

- **A3** process innovation: flat material-cost ratio (48.3% → 48.1%) despite
  31.8% reported revenue growth is recorded as evidence AGAINST the category,
  with the score at 0 and the reason stated as adverse, not blank.
- **F2** execution moat: "Scored as adverse: an execution deficit is
  documented, not an execution moat. This is not 'NO EVIDENCE FOUND' — evidence
  exists and it cuts against a moat forming here." Explicit.
- **G1** war chest: the pattern the category tests for is named as "specifically
  ABSENT", with the FVTPL buildup recorded as evidence against reinvestment
  capacity rather than credited as a war chest.
- **H3** ESG: the AR's own statement of zero energy-conservation capex is called
  "a documented absence, not merely a gap".
- **B2** qualification lock-in: the complete absence of any cGMP / ISO / NABL /
  WHO-GMP / USFDA / pharmacopoeia disclosure for a pharma-facing B2B supplier is
  called "itself a notable finding, not merely a gap", while the structural
  switching-cost argument is held at 🔍 because Titan's own filings do not make
  it. Correctly scored 0.5, not credited upward.

The scan also states the inverse comparison explicitly: Gate 0's thin moat
score was mostly missing disclosure, while this scan's thinness is mostly
documented absence plus three categories of adverse evidence. That is the right
reading of the two findings and it is carried into the analyst_note.

### 2.5 F2 under NO-CONCALL MODE — PASS

prompts/07 line 107 asks F2 to "cross-reference the injected concall
promise-delivery record". No transcripts exist for this company. The governing
rule is prompts/00-orchestrator.md lines 339-340: "Stage 7's F2 test uses
capex-completion evidence across AR timeline statements in place of the
promise-delivery record."

B07 did exactly that, and its F2 rests on a genuine AR capex timeline: gross PPE
additions Rs 1,948.49 lakh FY24 → Rs 936.88 lakh FY25 → Rs 740.08 lakh FY26
(AR FY24/FY25/FY26 Note 2(a)), set against the "build capacity and capabilities
for future business growth" sentence reused near-verbatim across all three
MD&As, and against the FY26 outflow of which 77% went to a quoted-debt FVTPL
portfolio. It supplements this with B05's cross-annual-report promise tracker
(3 delivered, 1 partial, 3 missed, grade C), which in degraded mode is itself
built from ARs and results rather than transcripts, so no transcript evidence is
claimed that does not exist. It also records the one offsetting positive
(revenue per employee Rs 34.2 → Rs 39.1 lakh) rather than suppressing it. The
substitution is compliant and well executed.

### 2.6 Sections 1, 2, 4, 6 — PASS, one MINOR

| Section | Requirement | Verdict |
|---|---|---|
| 1A | pipeline table with status, evidence type, launch, potential, differentiation | PASS |
| 1B | five diversification directions each answered | PASS |
| 1C | mix shift table; forward cells NOT FOUND, not estimated | PASS |
| 2A | capex programme table | PASS |
| 2B | utilisation per facility → NO EVIDENCE FOUND | PASS |
| 2C | arithmetic shown: Rs 1.73 cr × 4.02x = Rs 6.95 cr = 3.4% of Rs 206.19 cr | PASS on form, see C-14 |
| 2D | new geography entries → NO EVIDENCE FOUND | PASS |
| 4A/4B/4C | R1 assessed, export-incentive scheme correctly rejected as non-differential, R1 scored 0 | PASS |
| 6A-6E | all five sub-sections present | PASS |
| 6C | uses the INJECTED Gate 0 block (core 81, 2 moats, 15/60 MODERATE, GOOD+) | PASS |
| 6D | see C-04 | **FAIL (MAJOR)** |

**FINDING C-14 (MINOR). The 2C fixed-asset turnover is on a different basis
from B01's.** B07 uses standalone revenue Rs 206.19 cr over standalone net PPE
Rs 51.34 cr = 4.02x. B01's M3 uses Rs 200.35 cr over net block Rs 61.61 cr =
3.25x for the same ratio on the same company. The higher turnover inflates the
implied incremental revenue (3.4% versus 2.7% on B01's basis). Both numbers are
trivial and B07's own conclusion — that there is no capex pipeline of a size
that could explain a re-rating — survives either. Flagged so stage 10 does not
carry two fixed-asset turnovers for one company.

Note on propagation: 6C reproduces B01's core score of 81 and the GOOD+ label.
Both change under C-01. B07 followed instruction by using the injected block; the
fix belongs at B01 and must be re-fed to 6C and to `combined_assessment`.

### 2.7 Block schema and field discipline — four findings

**FINDING C-04 (MAJOR). 6D returns a coined label instead of one of the eight
matrix values.** The prompt requires "6D combined classification per the
standard matrix (EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL / GOOD+ / GOOD /
TURNAROUND / AVERAGE / AVOID)". `combined_assessment` reads "GOOD+ (backward) /
NO MEANINGFUL EMERGING MOAT (forward) — GOOD, NOT TRANSITIONING". "GOOD, NOT
TRANSITIONING" is not in the enumerated set, so a downstream consumer keying on
this field gets a value it cannot match. The re-derived value from the stated
inputs is **GOOD** (and it remains GOOD after the B01 correction, which is a
coincidence worth noting, not a reason to leave the field as it is). Two
mitigations, stated fairly: the prompt names the eight labels but does not
reproduce the mapping table, and the stage did supply the full reasoning the
prompt demands for a non-obvious cell. The prompt should carry the mapping; the
stage should still have picked from the list.

**FINDING C-05 (MAJOR). `active_categories` includes a row the field excludes.**
The schema comment reads "only Strong/Moderate rows". The block lists E2
(Moderate, correct) and G2 (Weak). The report body contradicts the block on the
same page: "Count with Strong/Moderate evidence: 1 (E2, Moderate). No category
scores Strong." The treatment is also internally inconsistent, because B2 is
likewise Weak and is correctly kept out. A downstream reader takes 2 active
categories where the rubric yields 1. No score changes; em_score stays 3 and the
classification stays NONE.

**FINDING C-11 (MINOR). `evidence_mix` counts do not reconcile with the body.**
The field is documented as item counts and reads {documented: 2, claim: 1,
inference: 1}. The body anchors documented evidence in at least five categories
(E2 export note, G2 turnover ratios, A3 material-cost ratio, F2 PPE-additions
series, G1 FVTPL portfolio) and carries inference at B2, at E2's cause and at
1B's vertical-integration read. The field appears to count only the scored-active
rows, which understates the documented evidence this scan actually produced.

**FINDING C-12 (MINOR). Two `catalysts_12m` rows carry `evidence_type:
"DOCUMENTED (pending)"`.** An event that has not happened cannot be documented.
The schema comment says this field feeds Pillar 3 catalyst proximity at stage
11, where the evidence tier earns credit, so the label matters beyond B07. The
"(pending)" qualifier and the anchors make the intent readable, which keeps this
MINOR, but stage 11 must not read these rows as 📄.

**FINDING C-10 (MINOR). The block carries two keys the schema does not
define**, `data_years: 3` and `fy_range`. The prompt says "end with exactly this
fenced YAML block". Harmless in content, and `data_years: 3` is an accurate
statement about the AR window, but it is a schema deviation and it reads oddly
beside B01's `data_years: 10` for the same company.

**FINDING C-09 (MINOR). Optionality register scope.** The rule is "forward
advantages that scored 0 or rest only on 🎙️/🔍 evidence". B2 (qualification
lock-in) rests only on 🔍 evidence and is not registered, although its converting
evidence is obvious and already named in input_gaps (a disclosed cGMP / ISO /
pharmacopoeia certification). Two of the six registered rows (the FVTPL
composition and the Peptech PAT reconciliation) are verification items rather
than forward advantages, which stretches the register's purpose. All six rows do
carry the four required columns, and the closing line "Registered options are
watched, never scored" is present and honoured.

### 2.8 The two CLAUDE.md rules that bear on this stage

**Emerging Moat is not FTTCP.** B07 opens with the taxonomy note and keeps to
it. There is no FTTCP verdict card, no ROCE verdict, no pillar, no destination
PE, no exit multiple, no price and no entry zone anywhere in the report or the
block. The one adjacent phrase, "no capex pipeline of a size that could
plausibly explain a multi-year re-rating case" (Section 2C), asserts no multiple
and no number; it explains why the 3.4% figure is trivial. The taxonomy holds.
PASS.

**Institutional ownership and the UA qualifier.** B07 contains no
institutional-ownership language and no Amendment 3 arithmetic: no Raw x 1.25,
no sector cap, no qualifier scoring. Correct — the Gate 0 and Emerging Moat
prompts do not ask for the UA multiplier, and importing it here would be stage
11's work done in the wrong place. The one UA-relevant duty these two stages
carry is to emit the inputs stage 11 will test, and B07 emits `em_score: 3`
against the absolute "EM ≥25" qualifier, which stage 11 can evaluate directly.
Observation, not a finding: neither stage states in words that em_score 3 fails
the EM ≥25 UA qualifier. The number is carried faithfully, so nothing is lost,
but a one-line statement in B07 Section 5 would remove any chance of stage 11
reading a 92-point-scale score against a 25-point bar incorrectly.

**Single credit for one improvement.** The scan handles this correctly at C2:
the export-growth improvement is scored once, at E2, and C2 explicitly declines
to count it again, citing the rule. PASS.

---

## PART 3 — RULE LEDGER AND ACCEPTANCE

### Gate 0 (B01): 46 rules checked, 5 fails

Rules 1-20 the twenty scored lines A1-E4; rules 21-32 the twelve moat tests;
rule 33 CAGR edge rules; 34 data-confidence tier; 35 classification matrix;
36 deal-breakers 1-9; 37 rule-6 history statement; 38 rule-4 anchors;
39 rule-5 grounded claims; 40 PEER DATA NEEDED marking; 41 block and total
arithmetic; 42 YAML schema; 43 institutional-ownership / UA discipline;
44 flags-field condition; 45 moat classification band; 46 block_b_trend accuracy.

FAILS: B4 (C-01, CRITICAL), M12 (C-02 and C-06, MAJOR), rule 34 (C-08, MINOR),
rule 40 (C-07, MINOR), rule 46 (C-03, MAJOR).
Passed 41 of 46 = **89%**.

### Emerging Moat (B07): 40 rules checked, 8 fails

Rules cover: 23-category coverage; six-section execution; evidence taxonomy;
anchors; NO EVIDENCE FOUND discipline; completionist recount and its format;
raw-score matrix; multipliers; adjusted-total arithmetic; classification band;
I1 both-legs rule; I2 named-sacrifice rule; I1/I2 separate contribution; ceiling
and absolute bands; sections 1A-1C, 2A-2D, 4A-4C, 6A-6E; 6C injected-block use;
6D matrix selection; 6D reasoning depth; optionality register presence, columns
and scope; block schema conformance; active_categories filter; evidence_mix
consistency; catalysts_12m taxonomy; capex_embedded_growth_pct carry-through;
FTTCP taxonomy separation; NO-CONCALL F2 substitution; adverse-versus-absent
discipline; single-credit rule; UA / institutional-ownership discipline;
summary-table completeness; Strong/Moderate count; block-body agreement.

FAILS: 6D matrix selection (C-04, MAJOR); active_categories filter (C-05,
MAJOR); optionality register scope (C-09, MINOR); block schema (C-10, MINOR);
evidence_mix (C-11, MINOR); catalysts taxonomy (C-12, MINOR); recount prose
(C-13, MINOR); 2C turnover basis (C-14, MINOR).
Passed 32 of 40 = **80%**.

### Combined

73 of 86 rules passed = **85%**. Denominators are well above 4, so the rate is
applicable. It sits above the 60% REWORK threshold.

### Recommendation

The acceptance rate does not trigger REWORK, and a Verifier C CRITICAL is not
itself a REWORK trigger (only a confirmed Verifier A critical or a sub-60% rate
is). I do not claim a trigger I do not own. I do recommend, plainly:

1. Return B4 and M12 to stage 1 for correction of the payable-days unit error,
   and re-emit B01 with core 79, moat 14, grand total 93, classification GOOD,
   and a corrected `block_b_trend` and analyst_note.
2. Re-feed the corrected block to B07 Section 6C and `combined_assessment`, and
   set `combined_assessment` to one of the eight matrix labels (GOOD on the
   stated inputs).
3. Fix `active_categories` to carry E2 only.
4. Carry C-08 into Halt 1: Block A rests on four years, not the ten the block
   header implies.

Nothing here touches company quality, and nothing here halts the run. Flags
propagate; only mechanical failures halt.

---

```yaml
stage: B12c
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-opus-5
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation audit deferred to phase 3"
gate0:
  rules_checked: 46
  fails:
    - {rule: "B4 Change in WC Days", detail: "Payable Days formula applied with a 10x lakh/crore unit error in all five rows; recomputed WC days FY23 130.85 and FY26 127.67 (adjusted basis) give a 3.18-day decrease, band +/-5", reported: 5, recomputed: 3, severity: CRITICAL}
    - {rule: "M12 Negative WC / Float", detail: "inherits the same unit error; corrected series 130.85 / 135.39 / 150.05 / 127.67 is >45 days in every year", reported: 1, recomputed: 0, severity: MAJOR}
    - {rule: "block_b_trend field accuracy", detail: "asserts a WC-days swing from +4.26 to -12.40 and a working-capital release that the corrected series does not show; propagated into the B01 analyst_note and into B07 category G2", severity: MAJOR}
    - {rule: "Data confidence tier vs stated window", detail: "block reports data_years 10 while Block A and B2-B4 rest on FY23-FY26 only; effect of excluding FY17-FY20 on A1/A2 never tested or flagged", severity: MINOR}
    - {rule: "Block F 'PEER DATA NEEDED' marking", detail: "M7 and the segment-census leg of M5 scored 0 on absent peer data without the required marker; substance captured in input_gaps", severity: MINOR}
  recomputed: {block_b: 15, core_score: 79, moat_score: 14, grand_total: 93, moats_confirmed: 2, moat_class: "MODERATE", classification: "GOOD"}
  passed: 41
  rate_pct: 89
emoat:
  rules_checked: 40
  fails:
    - {rule: "6D combined classification from the eight-label matrix", detail: "combined_assessment returns the coined label 'GOOD, NOT TRANSITIONING' instead of one of EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL / GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID; re-derived value is GOOD. Mitigation: the prompt names the eight labels but omits the mapping table", severity: MAJOR}
    - {rule: "active_categories = Strong/Moderate rows only", detail: "G2 is graded Weak in the body and still listed; the body states 'Count with Strong/Moderate evidence: 1 (E2)'. B2 is also Weak and correctly excluded, so the treatment is internally inconsistent. No score effect", severity: MAJOR}
    - {rule: "Optionality register scope", detail: "B2 qualification lock-in rests only on inference and is not registered; two registered rows (FVTPL composition, Peptech PAT reconciliation) are verification items, not forward advantages", severity: MINOR}
    - {rule: "Block schema conformance", detail: "data_years and fy_range are emitted but are not in the prompt's block schema", severity: MINOR}
    - {rule: "evidence_mix item counts", detail: "{documented: 2, claim: 1, inference: 1} counts only scored-active rows; the body anchors documented evidence in five categories (E2, G2, A3, F2, G1)", severity: MINOR}
    - {rule: "catalysts_12m evidence taxonomy", detail: "two rows carry evidence_type 'DOCUMENTED (pending)' for events that have not occurred; this field feeds Pillar 3 catalyst proximity at stage 11 and must not be read as documented", severity: MINOR}
    - {rule: "Completionist recount prose consistency", detail: "body sentence says '2 categories carry documented ADVERSE evidence (A3, F2, G1 - three categories)'; the emitted block states 3 correctly", severity: MINOR}
    - {rule: "2C fixed-asset turnover basis", detail: "4.02x standalone (206.19/51.34) against B01 M3's 3.25x consolidated (200.35/61.61) for the same ratio; implied embedded growth 3.4% vs 2.7%. Conclusion unaffected", severity: MINOR}
  passes_of_note:
    - "All 23 categories addressed or explicitly NO EVIDENCE FOUND; anchors on every evidence item"
    - "Multipliers re-derived exactly: B2 LL x 0.5 = 0.5, E2 MH x 0.5 = 1.5, G2 LM x 1.0 = 1.0, total 3.0, band <12 NONE"
    - "Categories 21 and 22 present; I1 scored 0 on the failed (a) leg, I2 scored 0 on 'nothing must be destroyed', both per rubric; I1/I2 contribution stated separately as 0.0"
    - "Completionist recount performed and stated in the required format"
    - "NO-CONCALL F2 substitution matches prompts/00-orchestrator.md lines 339-340: AR capex-completion timeline used in place of the transcript promise-delivery record"
    - "Adverse evidence kept distinct from absent evidence at A3, F2, G1, H3 and B2; F2 states it explicitly"
    - "No FTTCP content: no verdict card, pillar, destination PE, price or entry zone anywhere"
    - "Single-credit rule honoured: export improvement scored once at E2, declined again at C2"
  passed: 32
  rate_pct: 80
valuation: {rules_checked: 0, fails: []}   # NOT RUN. Phase-1 scope; B10/B11 do not exist. Deferred to phase 3.
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}   # NOT ASSESSED in phase 1; stage 11 artifact. Deferred to phase 3.
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}   # NOT ASSESSED in phase 1; stage 13 artifact. Deferred to phase 3.
ua_qualifier_check: {b01_imported_valuation_arithmetic: false, b07_imported_valuation_arithmetic: false, low_institutional_ownership_treated_as_risk: false, em_score_emitted_for_stage11: 3, note: "Neither stage imports Amendment 3 arithmetic, which is correct: stage 11 owns it. Neither states in words that em_score 3 fails the absolute EM >=25 UA qualifier; the number is carried faithfully so nothing is lost."}
emoat_is_not_fttcp: true
disclosure_absent_vs_adverse_handled: true   # B01 E3 pledge NOT FOUND scored 0 as a gap, deal-breaker 5 correctly not triggered; B07 A3/F2/G1/H3 scored 0 as adverse and said so
recomputed_destination_pe: ""   # out of scope in phase 1
recomputed_decision: "B01 classification GOOD+ -> GOOD (core 81 -> 79, moat 15 -> 14, grand total 96 -> 93) on correction of the B4 payable-days unit error; B07 combined_assessment -> GOOD"
findings:
  - {id: C-01, severity: CRITICAL, location: "B01 Block B, B4 and the WC-days table", detail: "Payable Days = Trade Payables / Revenue x 365 applied with revenue scaled by 10 instead of 100; all five rows are 10x too high. FY25's 121.68 days implies payables of Rs 52.15 cr against the report's own FY25 Total Current Liabilities of Rs 17.74 cr. B4 5 -> 3, core 81 -> 79, classification GOOD+ -> GOOD. Basis-sensitive: the reported-revenue row would hold B4 at 5, and the report declared the adjusted basis"}
  - {id: C-02, severity: MAJOR, location: "B01 Block F, M12", detail: "same unit error; corrected WC days exceed 45 in all four years, M12 1 -> 0, moat score 15 -> 14, moat class MODERATE unchanged"}
  - {id: C-03, severity: MAJOR, location: "B01 block_b_trend and analyst_note", detail: "asserts a working-capital release from the erroneous series; propagated into B07 category G2"}
  - {id: C-04, severity: MAJOR, location: "B07 Section 6D and combined_assessment", detail: "coined label instead of one of the eight matrix values; re-derived value GOOD"}
  - {id: C-05, severity: MAJOR, location: "B07 block active_categories", detail: "Weak row G2 listed in a Strong/Moderate-only field, contradicting the body's own count of 1"}
  - {id: C-06, severity: MINOR, location: "B01 M12", detail: "band reached via a median-of-four-years test the rubric does not contain"}
  - {id: C-07, severity: MINOR, location: "B01 M5, M7", detail: "'PEER DATA NEEDED' marker required by the Block F instruction not used"}
  - {id: C-08, severity: MINOR, location: "B01 Block A and data_years", detail: "return blocks run on FY23-FY26 while the block reports data_years 10; the exclusion of FY17-FY20 from A1/A2 is not tested or flagged. Not recomputable: the corpus has no FY17-FY22 balance-sheet detail"}
  - {id: C-09, severity: MINOR, location: "B07 Optionality Register", detail: "B2 omitted though inference-only; two rows are verification items rather than forward advantages"}
  - {id: C-10, severity: MINOR, location: "B07 block", detail: "data_years and fy_range emitted outside the prompt's schema"}
  - {id: C-11, severity: MINOR, location: "B07 block evidence_mix", detail: "counts only scored-active rows; body anchors documented evidence in five categories"}
  - {id: C-12, severity: MINOR, location: "B07 block catalysts_12m", detail: "'DOCUMENTED (pending)' evidence_type on two future events; feeds Pillar 3 proximity at stage 11"}
  - {id: C-13, severity: MINOR, location: "B07 Section 3 recount prose", detail: "'2 categories ... three categories' in one sentence; the block states 3 correctly"}
  - {id: C-14, severity: MINOR, location: "B07 Section 2C", detail: "fixed-asset turnover 4.02x standalone against B01 M3's 3.25x consolidated for the same ratio"}
critical_count: 1
major_count: 4
minor_count: 9
acceptance_rate: 85   # 73 of 86 rules passed; gate0 41/46, emoat 32/40
rework_recommendation: "Stage 1 correction of B4 and M12 and re-emission of B01 (core 79, moat 14, classification GOOD), then re-feed to B07 6C, combined_assessment and active_categories. Not a mechanical halt; the acceptance rate clears 60% and a Verifier C critical is not itself the REWORK trigger."
```
