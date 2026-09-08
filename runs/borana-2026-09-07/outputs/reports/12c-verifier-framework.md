# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE (BORANA)
Run date: 2026-09-07 | Model: claude-opus-4-8 | Scope: PHASE 1 (B01 + B07 only)

Auditor status: independent, fresh context. No prior view of this company.
No upstream interpretation was passed to me.

## SCOPE AND LIMITS

Audited against two rule sources and nothing else:
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- runs/borana-2026-09-07/outputs/reports/01-gate0.md
- runs/borana-2026-09-07/outputs/blocks/B01-gate0.yaml
- runs/borana-2026-09-07/outputs/reports/07-emoat.md
- runs/borana-2026-09-07/outputs/blocks/B07-emoat.yaml

NOT audited, deferred to phase 3: the valuation adherence audit (rule 4 of
the Verifier C rubric). Stages 10 and 11 have not run. B10 and B11 do not
exist. The Master Prompt, the Section 1B layer set and FTTCP v2.1 were
deliberately not loaded, per the phase-1 scope rule in the rubric.

Boundary respected: I audit rule application, not company quality and not
source fidelity. Where I re-derive a number it is to test whether the
stage's own stated inputs produce the stage's own stated output. Verifier A
owns whether a number exists in the source PDF, and on that question its
finding governs over any re-derivation of mine.

---

# PART 1: GATE 0 (B01) COMPLIANCE

## 1.1 Block score re-derivation from the stage's own stated inputs

**BLOCK A — reported 20/20**

| Metric | Stage input | Threshold applied | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 17.10/24.21/33.54/42.94/48.12 → median 33.54% | >=25% = 5 | 5 | 5 | PASS |
| A2 Min single-year ROCE | 17.10% (FY22) | >=15% = 5 | 5 | 5 | PASS |
| A3 Median ROE | 35.0/59.4/65.7/99.4/125.8 → median 65.7% | >=20% = 5 | 5 | 5 | PASS |
| A4 ROCE trend | latest 24.21 vs earliest 17.10 | latest >= earliest = 5 | 5 | 5 | PASS |

Median of five sorted values is the third value. Both medians are taken
correctly (33.54, 65.7). Block A = 20. **CONCUR.**

**BLOCK B — reported 6/20**

| Metric | Stage input | Re-derived | Reported | Verdict |
|---|---|---|---|---|
| B1 Cum CFO / Cum PAT | SigmaCFO 80.30, SigmaPAT 146.50 → 0.548 | band 0.50-0.69 = 1 | 1 | PASS |
| B2 FCF-positive years | 1 of 5 = 20% | <50% = 0 | 0 | PASS |
| B3 Cum FCF / Cum PAT | -194.77 / 146.50 = -1.33 | negative = 0 | 0 | PASS |
| B4 Change in WC days | FY26 66.45 vs FY22 90.09 = -23.64 days | decreased >5 = 5 | 5 | PASS |

CFO sum check: -8.33 + 6.90 + 22.13 + 22.64 + 36.96 = 80.30 (stage states
80.31, rounding). PAT sum: 1.80 + 16.30 + 23.59 + 40.20 + 64.61 = 146.50.
FCF per year re-derived from the stage's CFO and capex columns and ties to
each printed FCF cell within 0.01. WC days re-derived from the stage's
receivable/inventory/payable columns and ties to every printed WC cell
exactly. Block B = 6. **CONCUR.**

**BLOCK C — reported 20/20**

CAGR interval count is the trap here and the stage passed it. FY22 to FY26
is four intervals, and the stage used ^(1/4), not ^(1/5).

| Metric | Re-derivation | Reported | Verdict |
|---|---|---|---|
| C1 Revenue CAGR | (388.59/42.33)^(1/4)-1 = 74.07% → >=20% = 5 | 5 | PASS |
| C2 PAT CAGR | (64.61/1.80)^(1/4)-1 = 144.8% → >=20% = 5 | 5 | PASS |
| C3 Positive YoY years | 4 of 4 = 100% = 5 | 5 | PASS |
| C4 PAT minus Rev CAGR | 144.8 - 74.1 = +70.7pp → >=+3pp = 5 | 5 | PASS |

Block C = 20. **CONCUR.**

CAGR edge rules: no endpoint is zero or negative, so the N/M rule does not
fire. No loss-to-profit swing exists, and the stage recorded that fact
affirmatively in data_notes rather than leaving it silent. C4 did not need
the PAT-CAGR-N/M fallback. All three edge rules honoured. **PASS.**

**BLOCK D — reported 18/20**

| Metric | Re-derivation | Reported | Verdict |
|---|---|---|---|
| D1 ND/EBITDA | 69.13/91.52 = 0.755x → band 0-1.0x = 4 | 4 | PASS |
| D2 Interest coverage | 81.89/3.49 = 23.46x → >=10x = 5 | 5 | PASS |
| D3 Debt/Equity | 70.81/281.58 = 0.2515 → band 0.1-0.5 = 4 | 4 | PASS |
| D4 Current ratio | 121.91/28.13 = 4.334x → >=2.0 = 5 | 5 | PASS |

Block D = 18. **CONCUR.** Non-financial issuer, so the bank/NBFC branches
of D1-D3 correctly do not apply.

**BLOCK E — reported 15/20**

| Metric | Re-derivation | Reported | Verdict |
|---|---|---|---|
| E1 Promoter holding 65.24% | >=60% = 5 | 5 | PASS |
| E2 3-year change | N/A, no 3-year window exists | 0 | PASS (see 1.3) |
| E3 Pledge 0% | 0% = 5 | 5 | PASS |
| E4 Contingent liab / NW = 0% | <5% = 5 | 5 | PASS |

Block E = 15. **CONCUR.**

**CORE** = 20 + 6 + 20 + 18 + 15 = **79**. Ties to the reported 79 and to
the block. **CONCUR.**

## 1.2 Block F moat tests, all twelve re-derived

| Test | Rule band claimed | Check | Verdict |
|---|---|---|---|
| M1 = 5 | margin +11.3pp (>=2pp) AND rev CAGR 74.1% (>=10%) | both legs met | PASS |
| M2 = 5 | +14.82pp above FY26 peer median 8.73% (>=5pp) | median of 8.73/13.70/3.35 is 8.73, correct | PASS |
| M3 = 3 | FAT 2.63x (>2x) AND ROCE 24.21% (>15%) | 5 needs FAT>3x, not met; 3 is the right band | PASS |
| M4 = 3 | zero decline years but receivable days swing 38.7d, not stable +/-10 | 5 barred; 0 decline years satisfies "max 1 decline year" | PASS |
| M5 = 0 | PEER DATA NEEDED | prompt mandates score 0 + the label; both done | PASS |
| M6 = 0 | no R&D disclosure, marked N/A | grounding rule = 0 | PASS |
| M7 = 0 | unregulated segment | "unregulated = 0" | PASS |
| M8 = 0 | no quantified network | "none = 0" | PASS |
| M9 = 5 | GM proxy 41.39% vs peer median 27.92% = +13.47pp (>=10pp) AND CAGR >=10% | proxy declared per rule | PASS |
| M10 = 5 | revenue grew every year AND receivable days fell 38.7d (clears "rose <=10d") | both legs met | PASS |
| M11 = 1 | <6 years, conservative read stated; CAGR >=20% but selling % rose | 3-band needs selling stable/declining; 1 is correct | PASS |
| M12 = 0 | 4 of 5 years >45 days | majority >45 = 0 | PASS |

Moat sum re-derived: 5+5+3+3+0+0+0+0+5+5+1+0 = **27**. Ties. Moats present
at score >=3: M1, M2, M3, M4, M9, M10 = **6**. Threshold "6+ present =
FORTRESS" is met exactly. **CONCUR on 27, on 6, and on FORTRESS.**

M3's parenthetical is muddled prose ("ROCE 24.21% (>15% but not >20%
threshold pairing required for 5...)") — ROCE 24.21% does clear 20%; it is
the FAT leg that caps the score at 3. The clause does then name the binding
constraint correctly. Score is right, wording is loose. Not logged as a
finding.

M5 deserves a note in the stage's favour. Peer data was partially present
(three named peers), and the stage could have ranked Borana against those
three and claimed a band. It refused, invoked PEER DATA NEEDED, scored 0,
and recorded the label in data_notes. That is the prompt's rule applied
against the stage's own interest.

**GRAND TOTAL** = 79 + 27 = **106**. Ties. **CONCUR.**

## 1.3 The two working conditions the task flagged

**Five-year history (FY22-FY26), listed 27-May-2025.**
Prompt rule: "Use whatever history is available: minimum 3 years, maximum
whatever exists," and the report must open with the exact adaptation
sentence. Report line 4 reads: "Data available: 5 years (FY22 to FY26).
Scoring adapted to 5-year history." Format matched. **PASS.**

Data-confidence rule: "10+ yrs full | 7-9 moderate | 5-6 lower, flag 'may
not have seen full cycle' | 3-4 LIMITED, downgrade classification one tier
| <3 auto AVERAGE." Five years lands in the 5-6 band. That band carries a
flag, not a downgrade. The downgrade applies only at 3-4 years. The stage
set history_downgrade = false. **CORRECT.** A downgrade here would have
been a misapplication in the harsh direction; the stage did not invent one.

The flag half of that rule is where the stage falls short. The report body
states the flag in prose. The B01 block does not carry it: flags[] is
empty, and no data_notes entry mentions it. The YAML comment scopes flags[]
to "classification <= AVERAGE with historical depressors", which does not
fire at GOOD, so the field's own trigger is not met — but the confidence
flag then has no carrier at all, and a downstream stage reading only the
block loses it. Logged **MINOR (F-04)**.

**E2 marked N/A for want of a three-year window.**
Prompt rule 5 is explicit: "If a data point is not available, mark it 'N/A
(not in provided data)' and score it 0. Never fill gaps with typical-
industry values or estimates." E2 requires a three-year promoter-holding
change. The company has 13 months of listed history. No three-year window
exists in any provided source. The stage marked N/A, scored 0, stated the
best available evidence separately without scoring it, and recorded the
treatment in data_notes. **PASS — and this is the harsher of the two
available readings.**

Worth stating plainly, because it runs against the direction a bending
stage would have taken. Promoter holding is flat at 65.24% across the whole
listed history. Had the stage scored that as "+/-1% = 3" on best-available
evidence, Block E would be 18, Core would be 82, and the matrix lookup
would read "Core >=80 + FORTRESS = EXCELLENT" instead of GOOD+. The stage
took the zero. That is rule 5 applied correctly and against its own
headline.

The final classification is insensitive to this either way: the Block B
deal-breaker caps at GOOD, so both the 0 route (raw GOOD+) and the 3 route
(raw EXCELLENT) land on GOOD after the cap. The verdict is robust to the
choice.

## 1.4 Classification and the deal-breaker cap

Matrix: "Core 60-79 + STRONG/FORTRESS = GOOD+". Core 79 sits inside 60-79
(79 < 80, so the >=80 rows do not apply). Moat class FORTRESS. Raw lookup =
**GOOD+**. **CONCUR.**

All nine deal-breakers were evaluated and the result of each recorded:

| # | Rule | Stage finding | Check |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | not triggered, A=20 | correct |
| 2 | Block B <8 → max GOOD | **TRIGGERED, B=6** | correct |
| 3 | Median ROCE <10% → max AVERAGE | not triggered, 33.54% | correct |
| 4 | Cum CFO/PAT <0.50 → max AVERAGE | not triggered, 0.548 | correct |
| 5 | Pledge >15% → max AVERAGE | not triggered, 0% | correct |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | not triggered, 0.755x / 23.46x | correct |
| 7 | Revenue declined in majority of years → max AVERAGE | not triggered, 0 decline years | correct |
| 8 | PAT negative in any of last 3 years → max AVERAGE | not triggered | correct |
| 9 | History <3 years → AVERAGE | not triggered, 5 years | correct |

Rule 4 is the near miss and the stage did not hide it. 0.548 clears 0.50 by
0.048. Had it fallen below, rule 4 would cap at AVERAGE, a two-tier drop.
The stage flagged the thinness of the margin in the report, in
block_b_trend and in analyst_note. That is a stage surfacing its own
fragility rather than burying it.

**Is the cap applied the way the prompt specifies?** Yes. The prompt phrases
deal-breakers as ceilings ("max GOOD"), not as fixed one-tier downgrades.
Rule 2 sets a ceiling of GOOD. The raw lookup is GOOD+, which exceeds the
ceiling, so the ceiling binds and the result is GOOD. Applying it as a
one-tier downgrade would have produced the same answer here by coincidence;
applying it as a ceiling is what the text says and what the stage did.
**PASS.**

**Is GOOD what the rules produce given those inputs?** Yes. Core 79 +
FORTRESS = GOOD+ raw; deal-breaker 2 caps at GOOD; final GOOD. I re-derived
every input to that chain and concur at each step. **recomputed_decision:
blank, concur.**

One shortfall on the deal-breaker instruction. The prompt says to "state
WHICH years drive any deal-breaker". The deal_breakers[] entry in the block
names the block and the score but not the years. The report body and
analyst_note do name them (FY26 capex Rs 178.98cr against CFO Rs 36.96cr,
1 of 5 years FCF-positive), so the information does propagate via
analyst_note. Partial compliance. Logged **MINOR (F-05)**.

## 1.5 Formula, basis and grounding discipline

| Rule | Check | Verdict |
|---|---|---|
| ROCE: use source figure if present, else compute and state "computed" | screener carries no ROCE field for this name; stage computed and stated so, with the EBIT and capital-employed definitions declared up front | PASS |
| ROE: average net worth; earliest year may use closing if opening unavailable, state so | FY22 uses closing, stated, with the reason (Rs 1 lakh incorporation capital) | PASS |
| WC days: state Revenue or COGS basis | Revenue basis declared in the basis notes and repeated in data_notes | PASS |
| FCF = CFO - capex, capex excludes acquisitions | cash-flow-basis capex column, definition consistent | PASS |
| M9 GM proxy must be stated if used | stated at the metric and in data_notes | PASS |
| M11 <6 years: score conservatively, state so | stated at the metric | PASS |
| Source anchors mandatory on every extracted number | dense; page-level anchors throughout, including direct-PDF-read confirmations where OCR was suspect | PASS |
| Never estimate a missing number | three metrics zeroed for absent data (E2, M6, M8) and one for absent peer data (M5); no substitutions found anywhere | PASS |
| analyst_note <=200 words | ~188 words | PASS |
| block_b_trend carries direction plus the one number | "deteriorating", WC days 39.4 → 66.5 | PASS |

The stage also documented four screener-versus-audited conflicts and
resolved every one to the audited figure, showing both values. That exceeds
what the prompt requires and is the right direction of resolution.

## 1.6 Gate 0 verdict

30 rules checked, 28 pass, 2 MINOR fails, both propagation gaps rather than
method errors. Every block score, the core, the moat sum, the moat count,
the moat class, the grand total, the matrix lookup and the cap re-derive to
the reported values. No arithmetic error found. No threshold misread found.
No estimated fill found.

This stage reached a capped, unflattering classification and reached it
honestly. Where the rules left room to be generous (E2, M5) it took the
zero.

---

# PART 2: EMERGING MOAT SCAN (B07) COMPLIANCE

## 2.1 Were all 22 categories plus Family I actually worked?

Yes. Row-by-row presence check against the prompt's family structure:

| Family | Required | Present in Section 3 | Verdict |
|---|---|---|---|
| A product & technology | A1-A4 (4) | 4 | PASS |
| B supply chain | B1-B3 (3) | 3 | PASS |
| C customer | C1-C2 (2) | 2 | PASS |
| D data & digital | D1-D2 (2) | 2 | PASS |
| E geographic & access | E1-E2 (2) | 2 | PASS |
| F talent & organisational | F1-F2 (2) | 2 | PASS |
| G financial & structural | G1-G2 (2) | 2 | PASS |
| H ecosystem & external | H1-H3 (3) | 3 | PASS |
| I structural asymmetries | I1-I2 (2) | 2 | PASS |
| R1 regulatory (Section 4) | 1 | 1 | PASS |

22 categories + R1 = 23 rows. All 23 appear in the Section 5 scoring table.
**No category skipped.**

Verifier rubric rule 8 checks: Category 21 (I1) and Category 22 (I2) are
both present. I1 scored 0, with the reason stated in the framework's own
terms: part (a) exists as promoter-tenure narrative, part (b) has zero
evidence, and the prompt bars a score without the structural-economics leg.
I2 scored 0, with the honest answer named ("nothing" must be destroyed) and
tied to the prompt's own instruction that this is execution lead, not
configuration. Neither row was force-fitted upward. **PASS.**

The row-count arithmetic in the Section 3 summary reconciles. 23 rows minus
F2, H3, R1 (evidence-bearing) minus I1, I2 (zero by rule, not "no evidence")
= 18 rows carrying NO EVIDENCE FOUND. I counted the NO EVIDENCE FOUND
labels directly: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1, G1-G2, H1-H2 = 18.
Exact. The summary and the analyst_note both state 18 and both are right.

## 2.2 Evidence tiering against the prompt's definitions

The prompt defines three tiers: documented (capex committed, patent filed,
contract signed, plant under construction, product launched, regulatory
application submitted), management claim (stated but not backed by
committed capital or signed contract), analyst inference.

Tier assignments on the only two rows that score:

| Row | Item | Tier assigned | Test against the definition | Verdict |
|---|---|---|---|---|
| H3 | 19.79 MW hybrid project | documented | under construction, EPC contractor named, CWIP-funded — squarely "plant under construction" | correct |
| H3 | Rs 18-20 Cr/yr savings figure | claim | concall-sourced, not yet realised | correct |
| R1 | PLI Round 3 Letter of Approval | documented | approval received, disclosed via Reg 30 — squarely "regulatory application submitted" or better | correct |
| R1 | incentive amount | not credited | unquantified anywhere in corpus, so not scored | correct |

The rubric's specific trap is "a claim-only category scoring as if
documented". The reverse happened here. H3 has a genuinely documented capex
leg that would support a 1.0x multiplier, but the stage applied 0.7x
because the figure driving its *impact* rating is a concall claim. Applying
the multiplier to the weakest leg that drives the rating is the
conservative reading and it costs the stage 0.9 points. **PASS, and in the
strict direction.**

Contrary-evidence handling is also correct. B1, B2, C1, C2, G1 and G2 each
found evidence pointing the opposite way from what the category tests for.
The prompt has no negative scores, so 0 is the floor; the stage scored 0
and carried the contrary findings into flags[] and top_moat_risks[] so they
survive into downstream stages rather than vanishing into a zero.

## 2.3 Does the scoring produce 3.1 and NONE?

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0. Then
multiply by evidence quality: documented 1.0x, claim 0.7x, inference 0.5x.

| Row | Raw | Multiplier | Adjusted |
|---|---|---|---|
| H3 | 3 (labelled HM) | 0.7x | 2.1 |
| R1 | 1 (LL) | 1.0x | 1.0 |
| all other 21 rows | 0 | — | 0.0 |
| **Total** | | | **3.1** |

Arithmetic from the stage's own raw scores: 3 x 0.7 = 2.1, plus 1 x 1.0 =
1.0, total 3.1. **Ties to the reported em_score.**

**But the H3 raw score does not follow from the stage's own description.**
The cell reads: "3 (HM: medium likelihood on the phased Sep/Oct-2026
target, medium impact — Rs 18-20 Cr/yr savings vs FY26 PBT of Rs 78.40 Cr,
~23-26%)". Medium likelihood combined with medium impact is MM, and MM maps
to 2, not 3. HM maps to 3 but requires a High leg, and the stage's own text
describes neither leg as high. On the description as written, H3 raw = 2,
adjusted = 1.4, and em_score = **2.4**, not 3.1.

The error direction is flattering, by 0.7 points. It changes nothing that
matters. 2.4 and 3.1 both sit deep inside the <12 NO MEANINGFUL EMERGING
MOAT band, nowhere near the 12 boundary, and both sit far below the EM>=25
qualifier used in Section 6D. Classification, active_categories and the
combined assessment are all unchanged. Logged **MINOR (F-01)**.

Classification bands: >=40 EXPANSION | 25-39 STRENGTHENING | 12-24 MODEST |
<12 NONE. Either 3.1 or 2.4 gives **NONE**. The block records "NONE" and
the report records "NO MEANINGFUL EMERGING MOAT (<12 band)". **CONCUR.**

The operator's 20-Aug-2026 absolute-thresholds ruling is honoured: no
rescale was attempted despite the ceiling moving from 84 to 92, and the
I1/I2 contribution is stated separately as the ruling requires ("I1/I2
contribution to total: 0.0"). **PASS.**

## 2.4 Is an empty active_categories consistent with the thresholds?

The block field is scoped by the prompt to "only Strong/Moderate rows". The
Section 3 summary table assigns strength per row. Every one of the 23 rows
is None or Weak: H3 is Weak, R1 is Weak (Section 4C: "R1 is scored WEAK on
the PLI leg alone"), the other 21 are None. No row reaches Strong or
Moderate. **active_categories: [] is correct**, and the block's inline
comment explains why the two non-zero rows are still excluded. **PASS.**

Completionist guard: the prompt's guard fires in the inflation direction at
12-plus active categories. Zero active categories cannot trip it. The
recount line is still mandatory and it is present, in the required form:
"Completionist recount performed: 5 documented items across 3 categories",
with the items enumerated. **PASS.**

The stage substituted ASCII tags ([DOC], [CLAIM], [INF]) for the prompt's
glyphs, and declared the mapping in the first four lines of the report.
Meaning is preserved. Not logged.

## 2.5 The two documented-item counts do not reconcile

completionist_recount says 5 documented items across 3 categories.
evidence_mix says documented: 11. Both can be true — the recount is scoped
to the Section 3 category scan, while evidence_mix is a whole-report count
including Sections 1, 2 and 4 — but neither field states its scope, and a
downstream reader sees 5 and 11 side by side in one block with no
explanation.

I checked whether 11 is defensible by enumerating distinct documented items
across the whole report: Unit 4 base-tranche delivery, Unit 4B slippage,
Unit 4 Expansion under construction, hybrid power under construction,
rooftop solar PPE addition, RHP utilisation table, C2 concentration table,
G1 cash and debt position, PLI Letter of Approval, GTP interest subsidy
quantified in Other Income, and the RHP no-long-term-contract disclosure.
Roughly 11. Defensible, not fabricated.

The inference count is the harder problem. evidence_mix reports
inference: 2. I grepped the report for the [INF] tag: it appears exactly
once, in the taxonomy definition on line 7, and never as a tag on any
evidence item. The block asserts two inference items that the report never
marks. The count is not reproducible from the artifact.

Immaterial to every output — no scored row rests on inference, and the 0.5x
multiplier is never used — but the block carries a number its own report
does not support. Logged **MINOR (F-02)**.

## 2.6 The combined assessment with Gate 0

Section 6C uses the injected Gate 0 block and every value ties to B01: core
79, moat 27 / 6 confirmed, GOOD (capped from GOOD+), FORTRESS. No drift
between the two blocks. **PASS.**

Section 6D reaches GOOD. Testing the combination rule is complicated by the
prompt itself: 6D says to apply "the standard matrix (EXCEPTIONAL /
EXCELLENT+ / HIGH POTENTIAL / GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID)"
but **prompts/07 never reproduces that matrix**. The only numeric
combination threshold printed anywhere in the file is the "EM >=25" UA
qualifier, which the file describes as a UA (unrecognised-alpha) qualifier
rather than as the combined-classification rule.

The stage borrowed EM>=25 as its combination criterion and said so
explicitly: a GOOD backward score needs EM >=25 to lift toward GOOD+, EM is
3.1, so the combined verdict stays at Gate 0's GOOD. It also reasoned
through why HIGH POTENTIAL and TURNAROUND do not apply, which 6D
specifically demands full reasoning on.

Assessment: the substitution is a rule gap in the prompt more than a defect
in the stage, it was declared rather than hidden, and the outcome is robust
to it. The prompt's own steer in 6D is that uplift comes from EXPANSION
forward scores; this scan is NONE, the lowest of four bands. No plausible
combined matrix lifts GOOD-backward plus NONE-forward above GOOD. The
substitution also cannot inflate — it can only refuse an uplift. Logged
**MINOR (F-03)**, addressed to the prompt as much as to the stage.

The stage also correctly declined the transition-setup uplift that 6D
invites ("GOOD or AVERAGE backward scores with EXPANSION forward scores are
exactly the transition setups this operation hunts"). That invitation is
the single most tempting place in this prompt to inflate a forward score,
because a GOOD backward score plus a manufactured EXPANSION forward score
produces the exact setup the operation is built to hunt. The stage had a
GOOD backward score in hand and returned 3.1 forward. It did not take the
bait.

## 2.7 NO-CONCALL MODE and the F2 substitution

The degradation required: only one transcript exists, so F2's
promise-delivery leg cannot be tested across calls, and capex-completion
evidence substitutes for it.

Was the substitution made as the rule requires?

The prompt's own F2 definition is "capex on time and budget across ARs,
ramp speed post-commissioning, revenue per employee trend, guidance
delivery; cross-reference the injected concall promise-delivery record."
Capex-on-time-and-budget is already native to F2. The degradation therefore
drops only the promise-delivery cross-reference and leans on a leg the
category already owns. That is the minimal possible degradation, not a
reinvention of the test. **PASS.**

Was it declared? Three times, and specifically:
1. A dedicated section, "WHAT THIS SCAN COULD NOT TEST (NO-CONCALL MODE)",
   before any scoring, naming the orchestrator's degradation map, naming
   the substitute evidence, and naming what is not attempted (Section 2E
   repeated-question and tone-drift testing).
2. In the F2 row label itself: "(CAPEX-COMPLETION EVIDENCE substitute, per
   NO-CONCALL degradation)".
3. In the block's input_gaps[].

**PASS on declaration.** The stage also stated that the single transcript is
used as one source among several rather than as the three-call record,
which is the right framing.

Was the F2 finding handled correctly? The substitute evidence returned
mixed: one clean delivery (Unit 4 base tranche, Rs 71.35 Cr, 100% proceeds
utilised, nil delay per an independent monitoring agency) against two
failures on live commitments (the 160-loom tranche silently redefined as a
192-loom tranche with no reconciliation; the hybrid power project slipped
four times across seven months and still uncommissioned). Net 0 for 2 on
currently-live commitments.

The stage scored F2 at 0 and declined to credit it as a positive category.
This is correct on two independent grounds. The scan hunts advantages
*forming*; a net-negative execution record is not one. And the prompt's
matrix has no negative values, so 0 is the floor. Crucially the evidence
was not discarded — it went to flags[], to top_moat_risks[] and to Section
6B as a cross-cutting risk, so the finding survives into downstream stages
instead of being erased by a zero. **PASS.**

A stage bending its method here would have credited the one clean delivery
as an execution moat and left the two failures in the prose. This one did
the opposite.

## 2.8 Remaining structural requirements

| Rule | Check | Verdict |
|---|---|---|
| All six sections executed in one response | 1, 2, 3, 4, 5, Optionality Register, 6 all present | PASS |
| 1A status/evidence/launch/potential/differentiation columns | present, three pipeline items, all CONCEPT-tier | PASS |
| 1C forward mix table | present, mostly NOT FOUND, refusal to infer stated | PASS |
| 2A capex table, all seven columns | present, six projects | PASS |
| 2B utilisation per facility | present, RHP-sourced, Unit 3 marked NOT FOUND rather than filled | PASS |
| 2C arithmetic shown | 80.94 x 2.68 = 216.9; 216.9 / 388.59 = 55.8% → 56 | PASS |
| 2D new geography | present, NOT FOUND with reason | PASS |
| Section 3 summary with strength and time-to-materialise | present | PASS |
| Section 4 R1 with 4A/4B/4C | present | PASS |
| Optionality register, four columns, scored-0 or claim-only items | 7 rows, all four columns, carried as optionality_register[] | PASS |
| 6A/6B/6C/6D/6E | all present | PASS |
| catalysts_12m with anchors | 5 items, each with window, evidence type, anchor | PASS |
| analyst_note <=200 words | ~95 words | PASS |
| NOT FOUND rather than estimate | used throughout 1A, 1C, 2A, 2B, 2C, 4B | PASS |

2C arithmetic re-derived: Rs 80.94 Cr CWIP x 2.68x FY24 fixed-asset
turnover = Rs 216.92 Cr; 216.92 / 388.59 = 55.82%, rounded to 56. Ties to
capex_embedded_growth_pct: 56. The stage stated three caveats on the proxy
(stale multiplier, unsplit CWIP composition, near-zero FY26 capitalisation)
rather than presenting it as a forecast, which the prompt's "show the
arithmetic" instruction invites but does not require. **PASS.**

## 2.9 Emerging Moat verdict

30 rules checked, 27 pass, 3 MINOR fails. One is a genuine scoring-label
defect (H3 raw score, F-01), one is an unreproducible block count (F-02),
one is a prompt gap the stage papered over transparently (F-03).

The scan returned a near-empty result and defended it as the honest floor
rather than an incomplete run. On the evidence in front of me, that defence
holds: 18 categories with no evidence, six categories with evidence running
the wrong way, and the one positively-scored row resting on capex that has
slipped four times.

---

# PART 3: VALUATION ADHERENCE — PENDING PHASE 3

Not run. Stages 10 and 11 have not executed; B10 and B11 do not exist.
Rubric rule 4 (Pillar 1 continuous formula, FTTCP ROCE authority,
single-credit rule, Pillar 2 multiplier and offsets, Pillar 3 inputs,
Amendment 3 UA ordering, sector cap, dual tracks, Hurdle Ratio, 4D
weights, SOM cross-check), rule 7 (method plurality), rule 11 (v3.8 exit
construction) and rule 12 (Amendment 19 FV path) are all deferred.

The Master Prompt, the Section 1B layer set and FTTCP v2.1 were not loaded,
per the phase-1 scope rule. No valuation judgment of any kind is offered
here, and none should be read into this report.

Rule 6 (downstream signal candidates in B09) and rule 9 (Business
Understanding Narrative in stage 13) are likewise outside phase-1 scope as
invoked: B09 and B13 are not among my inputs.

---

# PART 4: CONSOLIDATED FINDINGS

| ID | Severity | Location | Description |
|---|---|---|---|
| F-01 | MINOR | 07-emoat.md Section 5, H3 row | Likelihood x impact label contradicts its own description. Cell labelled HM (=3) but describes "medium likelihood... medium impact", which is MM (=2). On the stage's own words H3 raw = 2, adjusted = 1.4, em_score = 2.4 not 3.1. Direction is flattering. No gate moves: both values sit deep inside the <12 NONE band and far below the EM>=25 qualifier. |
| F-02 | MINOR | B07-emoat.yaml evidence_mix | inference: 2 is unsupported — the [INF] tag appears only in the taxonomy definition (line 7) and never tags an evidence item. Separately, documented: 11 (whole-report scope) sits beside completionist_recount's 5 (Section 3 scope) with no stated scope difference. Counts are not reproducible from the artifact. No scored row rests on inference, so no output changes. |
| F-03 | MINOR | 07-emoat.md Section 6D / prompts/07 | The "standard matrix" 6D instructs the stage to apply is never reproduced in prompts/07. The stage substituted the EM>=25 UA qualifier as its combination rule and declared the substitution. Outcome robust: EM 3.1 (or 2.4) is in the lowest of four bands and no plausible matrix lifts GOOD-backward + NONE-forward above GOOD. Substitution can only refuse an uplift, never grant one. Rule gap in the prompt as much as a stage defect; recommend printing the matrix in prompts/07. |
| F-04 | MINOR | B01-gate0.yaml flags / data_notes | The data-confidence rule for the 5-6 year band requires the flag "may not have seen full cycle". Stated in the report body, not carried anywhere in the block: flags[] is empty and no data_notes entry mentions it. The flags[] field's own trigger (classification <= AVERAGE) does not fire at GOOD, so the flag has no carrier and a downstream stage reading only the block loses it. |
| F-05 | MINOR | B01-gate0.yaml deal_breakers[] | The prompt requires stating WHICH years drive any deal-breaker. The deal_breakers[] entry names the block and score but not the years. The driving years (FY26 capex Rs 178.98cr vs CFO Rs 36.96cr; 1 of 5 years FCF-positive) appear in the report body and in analyst_note, so the information does propagate, but not in the field the instruction points at. |

Zero CRITICAL. Zero MAJOR.

**Rules checked: 60. Passed: 55. Acceptance rate: 92%.**
(Gate 0: 28 of 30. Emerging Moat: 27 of 30.)

No REWORK trigger fires. Acceptance rate is far above the 60% floor and
there are no CRITICAL findings from this verifier.

# PART 5: THE HONESTY TEST

The brief asked me to separate a stage that reached a harsh conclusion
honestly from one that reached a flattering conclusion by bending its
method. My finding is the former, on both stages, and the evidence is that
every discretionary call ran against the stage's own headline:

- Gate 0 scored E2 at zero rather than crediting flat 65.24% promoter
  holding as "+/-1% = 3". The generous route would have put Core at 82 and
  the raw matrix at EXCELLENT.
- Gate 0 invoked PEER DATA NEEDED on M5 and scored 0, with three named
  peers sitting in the file that it could have ranked against.
- Gate 0 disclosed that its own CFO/PAT deal-breaker clears by 0.048, and
  repeated that fragility in three separate fields.
- Gate 0 attached distortion notes to both of its 20/20 blocks, naming the
  near-zero FY22 base and the spot-year ROCE depression, and supplied the
  lower FY24-FY26 CAGRs beside the headline ones.
- Gate 0 applied the Block B cap that took its own classification down a
  tier, and stated the cap in the decision line, the block and the note.
- Emerging Moat applied the 0.7x claim multiplier to its only meaningful
  scored row when the documented capex leg could have argued for 1.0x.
- Emerging Moat declined to credit F2 as a positive category on a 1-for-3
  record, and routed the negative evidence into flags and risks rather than
  burying it in a zero.
- Emerging Moat declined the transition-setup uplift that 6D explicitly
  dangles, holding a GOOD backward score and returning 3.1 forward.

The one flattering-direction error I found (F-01, H3 raw 3 vs 2) is worth
0.7 points on a scale where the nearest threshold is nine points away.

Both stages ran under real degradation: five years of history against a
framework built for ten, and one transcript against a scan that expects
three. Both handled the degradation by declaring it and narrowing the
claim, not by substituting a proxy and calling it evidence.

I concur with the Gate 0 classification of GOOD and with the Emerging Moat
classification of NONE. recomputed_decision: blank.

---

```yaml
stage: B12c
company: "BORANA"
run_date: "2026-09-07"
model: claude-opus-4-8
status: complete
scope: "phase-1 (B01 + B07); valuation audit deferred to phase 3"
gate0:
  rules_checked: 30
  rules_passed: 28
  fails:
    - "F-04: data-confidence flag 'may not have seen full cycle' (5-6 year band) stated in report body but not carried in the block - flags[] empty, no data_notes entry"
    - "F-05: deal_breakers[] entry does not name WHICH years drive the Block B deal-breaker as the prompt instructs; years appear in report prose and analyst_note only"
  blocks_rederived: {A: 20, B: 6, C: 20, D: 18, E: 15}
  core_rederived: 79
  moat_score_rederived: 27
  moats_confirmed_rederived: 6
  moat_class_rederived: "FORTRESS"
  grand_total_rederived: 106
  raw_matrix_lookup: "GOOD+ (Core 79 in 60-79 band + FORTRESS)"
  deal_breaker_cap: "rule 2 (Block B 6 < 8) caps at max GOOD; applied as a ceiling per the prompt's wording, binds because raw GOOD+ exceeds it"
  classification_rederived: "GOOD"
  classification_concur: true
  history_downgrade_correct: true
  history_downgrade_note: "5 years lands in the 5-6 'lower confidence, flag' band; the one-tier downgrade applies only at 3-4 years, so history_downgrade=false is correct"
  e2_na_correct: true
  e2_na_note: "prompt rule 5 mandates N/A + score 0 for unavailable data; no 3-year window exists on 13 months of listed history. Stage took the harsher route: scoring flat 65.24% as '+/-1% = 3' would have put Core at 82 and the raw lookup at EXCELLENT. Final classification insensitive either way - the Block B cap dominates both paths to GOOD."
  cagr_edge_rules_honoured: true
  arithmetic_errors_found: 0
emoat:
  rules_checked: 30
  rules_passed: 27
  fails:
    - "F-01: H3 raw score labelled HM (=3) but described as 'medium likelihood... medium impact' = MM (=2); on the stage's own description em_score is 2.4 not 3.1. Flattering direction, no gate moves."
    - "F-02: evidence_mix inference:2 unsupported - [INF] tag never applied to any item in the report; documented:11 (whole-report) sits beside completionist_recount's 5 (Section 3 scope) with no stated scope difference"
    - "F-03: Section 6D 'standard matrix' is not reproduced in prompts/07; stage substituted the EM>=25 UA qualifier as the combination rule and declared it. Prompt gap as much as stage defect; outcome robust."
  categories_present: 23           # 22 categories + R1, none skipped
  family_i_present: true
  i1_scored: 0
  i2_scored: 0
  i1_i2_contribution_stated: true
  em_score_reported: 3.1
  em_score_rederived: 3.1          # from the stage's own raw scores; 2.4 on its own written description of H3, see F-01
  em_classification_concur: true   # NONE either way, <12 band
  active_categories_empty_correct: true
  active_categories_note: "every row is None or Weak; H3 Weak, R1 Weak; no row reaches Strong/Moderate, so the Strong/Moderate-only field is correctly empty"
  evidence_tiering_correct: true
  evidence_tiering_note: "no claim-only category scored as documented; H3 took the conservative 0.7x on a row whose capex leg could have argued 1.0x"
  completionist_recount_performed: true
  no_concall_f2_substitution:
    declared: true
    declared_in: "dedicated pre-scoring section, the F2 row label, and block input_gaps[]"
    substitution_correct: true
    note: "capex-on-time-and-budget is native to F2's own definition, so the degradation drops only the promise-delivery cross-reference leg - the minimal possible substitution, not a reinvented test"
    f2_not_credited_correct: true
    f2_note: "net 0-for-2 on live commitments; scored 0 and routed to flags[] and top_moat_risks[] rather than erased by the zero"
  combined_assessment_concur: true
  combined_assessment_note: "GOOD stands unchanged; EM 3.1 (or 2.4) sits far below EM>=25 and in the lowest of four bands. No plausible matrix lifts GOOD-backward + NONE-forward above GOOD."
valuation:
  status: "PENDING PHASE 3"
  rules_checked: 0
  fails: []
  note: "NOT RUN. Stages 10 and 11 have not executed; B10 and B11 do not exist. Rubric rules 4, 7, 11 and 12 deferred. Master Prompt, Section 1B layer set and FTTCP v2.1 deliberately not loaded per the phase-1 scope rule. No valuation judgment is offered or implied."
business_understanding_narrative:
  present: false
  five_questions_answered: false
  prose_only: false
  section6_candidates_named: 0
  valuation_vocab_leak: false
  fails: []
  note: "NOT APPLICABLE IN PHASE 1 - rubric rule 9 governs stage 13, which has not run and is not among this verifier's inputs. The false values above are 'not assessed', not 'assessed and failed'."
recomputed_destination_pe: ""      # out of scope, no valuation audit in phase 1
recomputed_decision: ""            # blank, concur: Gate 0 GOOD and emoat NONE both re-derive
findings:
  - {severity: "MINOR", location: "07-emoat.md Section 5, H3 scorecard row", description: "Likelihood x impact label contradicts its own description: cell labelled HM (=3) while describing medium likelihood and medium impact, which is MM (=2). On the stage's own words H3 raw = 2, adjusted = 1.4, em_score = 2.4 not 3.1. Flattering direction, magnitude 0.7 on a scale whose nearest threshold is 9 points away. Classification, active_categories and combined assessment all unchanged."}
  - {severity: "MINOR", location: "B07-emoat.yaml evidence_mix", description: "inference:2 is unsupported by the report - the [INF] tag appears only in the taxonomy definition on line 7 and never tags an evidence item. Separately documented:11 (whole-report count) sits beside completionist_recount's 5 (Section 3 scan scope) with no stated scope difference. Both counts are defensible on enumeration but neither is reproducible from the artifact as written. No scored row rests on inference, so no output changes."}
  - {severity: "MINOR", location: "07-emoat.md Section 6D and prompts/07-emerging-moat-pipeline.md", description: "6D instructs the stage to apply 'the standard matrix' but prompts/07 never reproduces that matrix. The stage substituted the EM>=25 UA qualifier as its combination rule and declared the substitution openly. Outcome robust and the substitution can only refuse an uplift, never grant one. This is a rule gap in the prompt as much as a defect in the stage; recommend printing the combined matrix in prompts/07."}
  - {severity: "MINOR", location: "B01-gate0.yaml flags[] / data_notes[]", description: "The data-confidence rule for the 5-6 year band requires the flag 'may not have seen full cycle'. It is stated in the report body but carried nowhere in the block: flags[] is empty and no data_notes entry mentions it. The flags[] field's own documented trigger (classification <= AVERAGE) does not fire at GOOD, so the confidence flag has no carrier and a downstream stage reading only the block loses it."}
  - {severity: "MINOR", location: "B01-gate0.yaml deal_breakers[]", description: "The prompt's deal-breaker instruction requires stating WHICH years drive any deal-breaker. The deal_breakers[] entry names the block and the score but not the years. The driving years (FY26 capex Rs 178.98cr against CFO Rs 36.96cr; 1 of 5 years FCF-positive) do appear in the report body and in analyst_note, so the information propagates, but not in the field the instruction points at."}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 92                # 55 of 60 rules passed
rework_triggered: false
honesty_assessment: "Both stages reached unflattering conclusions honestly. Every discretionary call ran against the stage's own headline: Gate 0 scored E2 at zero rather than crediting flat promoter holding (the generous route gave Core 82 and a raw EXCELLENT), invoked PEER DATA NEEDED on M5 with three usable peers in the file, disclosed that its CFO/PAT deal-breaker clears by 0.048, attached distortion notes to both 20/20 blocks, and applied the Block B cap that cost it a tier. The Emerging Moat scan applied the 0.7x claim multiplier to its only meaningful scored row when the documented capex leg could have argued 1.0x, declined to credit F2 on a 1-for-3 execution record while routing the negatives into flags and risks, and declined the transition-setup uplift 6D explicitly dangles while holding a GOOD backward score. The single flattering-direction error found is worth 0.7 points on a 9-point margin. No method bending detected."
```
