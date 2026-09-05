# STAGE 12c: VERIFIER C, FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: Shree Hari Chemicals Export Ltd (SHHARICH) | Run date 2026-09-05
Model: claude-opus-4-8 | Emits: B12c

## SCOPE AND LIMITS

Phase 1 scope only, as directed. I audited two artifacts against two rule
sources:

| Artifact | Path | Rule source |
| --- | --- | --- |
| B01 Gate 0 | outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml | prompts/01-gate-0-pipeline.md |
| B07 Emerging Moat | outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml | prompts/07-emerging-moat-pipeline.md |

NOT audited in this pass, deferred to phase 3: rules 4, 7, 11, 12 (B10/B11
valuation adherence), rule 9 (stage 13 business understanding narrative),
rule 10 (Halt 1 dossier), rule 6 (B09 downstream candidates). Those
artifacts do not exist yet. The valuation framework documents were
deliberately not loaded.

I audit rule application. I do not audit company quality, and I do not
adjudicate whether a number exists in a source PDF. Verifier A owns source
fidelity and its verdicts bind. Two cross-artifact numeric contradictions
found below are referred to Verifier A, not resolved here.

I do not hold the orchestrator's injected stage-7 task rules. B07 cites two
of them (NO-CONCALL mode substitution for F2, and a NOT FOUND rule for
capex_embedded_growth_pct). Where a B07 choice rests on injected text I
cannot read, I say so and mark the item UNRESOLVED rather than fail it.

---

## PART 1: GATE 0 (B01) COMPLIANCE

Verifier rule 2: re-derive every block score from the stated inputs using
the stated thresholds; check the classification matrix, confidence
adjustment, deal-breaker application, and the CAGR edge rules.

### 1.1 Block A, Return on Capital (max 20)

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| A1 Median ROCE | FY25 29%, FY26 17% (FY24 NOT FOUND) | (29+17)/2 = 23% into 20-24.9 = 4 | 23% -> 4 | PASS |
| A2 Min single-year ROCE | min(29, 17) = 17% | >=15% = 5 | 17% -> 5 | PASS |
| A3 Median ROE | 11.29 / 19.51 / 10.80 | median 11.29% into <12 = 0 | 11.29% -> 0 | PASS |
| A4 ROCE trend | 17% vs 29% (earliest available FY25) | decline 12pp into >5pp = 0 | -12pp -> 0 | PASS |
| Block A sum | 4+5+0+0 | | 9/20 | PASS |

A1, A2 and A4 rest on 2 of 3 years because FY24 ROCE is not computable from
the corpus. That adaptation is permitted: rule 6 of the Gate 0 prompt scores
on available history, and all three metrics are window-relative by
definition ("median", "minimum", "latest vs earliest"). The maker disclosed
the substitution in data_notes. See Observation O1 on the upward bias this
carries in A1 and A2.

ROE formula check: FY24 uses closing net worth with the exception stated
("if opening net worth unavailable for the earliest year, use closing and
state so"). FY25 and FY26 use average net worth. Formula honoured. PASS.

ROCE formula check: the source's own disclosed ROCE was used where it
exists, per the fixed rule ("If the data source provides its own ROCE, use
the source's figure"), and the absence of a FY24 current/non-current split
is named as the reason the computed fallback cannot run. PASS.

### 1.2 Block B, Cash Generation Quality (max 20)

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| B1 Cum CFO / Cum PAT | CFO 9.96, -0.80, 6.63; PAT 2.29, 5.10, 4.12 | 15.79/11.51 = 1.37 into >=1.00 = 5 | 1.372 -> 5 | PASS |
| B2 FCF-positive years | 0 of 2 assessable | 0% into <50 = 0 | 0 | PASS |
| B3 Cum FCF / Cum PAT | FCF -12.40; PAT 9.22 (same 2-yr window) | -1.35 into negative = 0 | -1.345 -> 0 | PASS |
| B4 Change in WC days | FY25 13.71, FY26 12.70 | -1.01 days into +/-5 = 3 | -1.01 -> 3 | PASS |
| Block B sum | 5+0+0+3 | | 8/20 | PASS |

WC days arithmetic re-derived: FY25 72.83 + 56.35 - 115.47 = 13.71. FY26
48.22 + 37.06 - 72.58 = 12.70. Both correct. Basis rule honoured: inventory
and payables on COGS basis with COGS explicitly available and the basis
stated; receivables on revenue basis, the formula's only option. PASS.

B3 uses a 2-year PAT denominator to match its 2-year FCF numerator. That is
the internally consistent choice. A 3-year PAT denominator gives -1.08,
still negative, still 0. No score sensitivity. PASS.

FCF definition (CFO minus capex, capex from the cash flow statement,
acquisitions excluded) honoured, with FY24 capex marked NOT FOUND rather
than inferred from the lump investing total. PASS.

### 1.3 Block C, Growth (max 20), and the CAGR edge rules

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| C1 Revenue CAGR | 138.33 -> 184.50, 2 yrs | 15.49% into 15-19.9 = 4 | 15.488% -> 4 | PASS |
| C2 PAT CAGR | 2.29 -> 4.12, 2 yrs | 34.13% into >=20 = 5 | 34.131% -> 5 | PASS |
| C3 Positive YoY revenue years | +2.07%, +30.66% | 2/2 = 100% = 5 | 5 | PASS |
| C4 PAT CAGR minus Rev CAGR | 34.13 - 15.49 | +18.64pp into >=+3pp = 5 | +18.64pp -> 5 | PASS |
| Block C sum | 4+5+5+5 | | 19/20 | PASS |
| CAGR edge: negative or zero endpoint | all four endpoints positive | rule not triggered | correct | PASS |
| CAGR edge: loss-to-profit note | PAT positive all 3 years | data_notes states no swing | correct | PASS |
| CAGR edge: C4 when PAT CAGR is N/M | PAT CAGR is not N/M | rule not triggered | correct | PASS |

CAGR formula ((End/Start)^(1/years) - 1) applied with years = 2 across a
3-point series. Correct. The maker added an unrequested caveat that the
FY24-FY26 endpoints straddle a FY25 spread peak and carried it into
data_notes. That is beyond the rule and improves the block. PASS.

### 1.4 Block D, Balance Sheet Strength (max 20)

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| D1 Net debt / EBITDA | 25.60 / 9.70 | 2.64x into 2-3x = 1 | 2.639x -> 1 | PASS |
| D2 Interest coverage | 7.36 / 2.16 | 3.41x into 3-4.9 = 2 | 3.407x -> 2 | PASS |
| D3 Debt / Equity | 33.21 / 44.30 | 0.75x into 0.5-1.0 = 3 | 0.750x -> 3 | PASS |
| D4 Current ratio | 0.95 | <1.0 = 0 | 0 | PASS |
| Block D sum | 1+2+3+0 | | 6/20 | PASS |

Non-financial entity, so the bank/NBFC variants of D1, D2 and D3 correctly
do not apply. D3 uses gross debt over equity per the plain formula and names
the AR's netted 0.58x alternative, noting both land in the same band. Sound
handling. PASS.

D1 EBITDA basis: see Finding F5. The framework does not define an EBITDA
basis, so I score D1 as a PASS on the threshold applied to the stated input.
The basis choice is recorded as an observation, not a rule fail.

### 1.5 Block E, Shareholder Alignment (max 20)

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| E1 Promoter holding, latest | 59.25% at 31-Mar-2026 | 50-59.9 = 4 | 4 | PASS |
| E2 Promoter change over 3 years | 3-year change NOT in corpus; 1-year change +5.04pp substituted | increased >=1% = 5 | **N/A -> 0** | **FAIL (MAJOR)** |
| E3 Promoter pledge, latest | not disclosed anywhere in corpus | N/A rule -> 0 | 0 | PASS |
| E4 Contingent liabilities / net worth | Rs 1.3472 cr / Rs 44.30 cr | 3.04% into <5 = 5 | 3.041% -> 5 | PASS |
| Block E sum as filed | 4+5+0+5 | | 14/20 | fails on E2 |
| Block E sum recomputed | 4+0+0+5 | | **9/20** | |

E2 is the only Gate 0 metric with a hard-coded window ("change over 3
years"). Every other window-substitution in this report (A1, A2, A4, B2, B3,
B4, M12) applies to a metric defined relative to the available window
("median", "minimum", "latest vs earliest", "majority of years",
"consistently"), so rule 6 covers those cleanly. It does not cover E2. Rule
5 does, and it is unconditional: a data point that is not available is
marked N/A and scored 0. The maker applied exactly that rule to E3 in the
same block, three lines below. The internal inconsistency is what makes this
a finding rather than a judgment difference. Full marks were awarded on a
proxy the framework does not authorise.

E1 check: the metric asks for the latest quarter and the corpus has no
quarterly shareholding pattern. The AR pattern is dated 31-Mar-2026, itself
a quarter end, so the substitution is a source change, not a window change.
PASS.

### 1.6 Block F, Quantitative Moat Scoring (max 60)

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| M1 Pricing power | margin 2.71% -> 3.57% (+0.86pp), rev CAGR 15.49% | stable +/-2pp AND CAGR >=10% = 3 | 3 | PASS |
| M2 Cost advantage | 3.57% vs peer median 9.28% | below = 0 | 0 | PASS |
| M3 Capital efficiency | FAT 8.82x, ROCE 17% | FAT>2x AND ROCE>15% = 3 (not >20% for 5) | 3 | PASS |
| M4 Customer stickiness | 0 decline years; receivable days -24.6 | top band needs both; band 2 needs max 1 decline year = 3 | 3 | PASS |
| M5 Scale and dominance | mcap 156 cr, rank 4 of 4 in the provided set | peer-data-insufficient default = 0, mark required | 0, **mark missing** | **FAIL (MINOR)** |
| M6 Technology / R&D | R&D NIL (AR p.63) | else = 0 | 0 | PASS |
| M7 Regulatory / licence | unregulated segment | unregulated = 0 | 0 | PASS |
| M8 Distribution | no quantified reach disclosure | none = 0 | 0 | PASS |
| M9 Brand | GM proxy 31.76% vs peer median 41.28% | at/below = 0 | 0 | PASS |
| M10 Switching costs | revenue grew every year; receivable days 57.53 -> 48.22 | grew every year AND days rose <=10 = 5 | 5 | PASS |
| M11 Network effects | 3 years, test needs >=6; CAGR 15.49%; selling % not isolable | score conservatively and state so = 0 | 0 | PASS |
| M12 Negative WC / float | 13.71 and 12.70 days | 0-15 consistently = 3 | 3 | PASS |
| Moat sum | 3+0+3+3+0+0+0+0+0+5+0+3 | | 17/60 | PASS |
| Moats present (>=3) | M1, M3, M4, M10, M12 | count 5 | 5 | PASS |
| Moat classification | 5 present | 4-5 = STRONG | STRONG | PASS |

M4 detail. The maker wrote that no band literally fits and scored 3 as a
judgment call. The score is right and the framing is wrong: band 2 reads
"max 1 decline year, fully recovered", and zero decline years satisfies "max
1". The threshold applies literally. Score confirmed at 3, framing noted.

M5 detail. The framework is explicit: "If a test needs peer data that is not
provided, score 0 and mark PEER DATA NEEDED (never guess peer figures)." The
score of 0 is therefore the framework's own prescribed value and I do not
disturb it. Two things are wrong with how it was reached. The mandated PEER
DATA NEEDED mark is absent from both the M5 row and data_notes, while the
same convention is discussed for M2 and M9. And the stated basis for 0 is
company memory ("Kiri, Bhageria, Sudarshan per company memory, no data
provided"), which CLAUDE.md defines as memory to weigh, never anchored
evidence. On the provided 4-company set SHHARICH ranks 4th, which reads into
the literal "top 5 mcap = 1" band. Recomputed on the literal read: moat
18/60, grand total 74, moats_confirmed 5 unchanged (1 is below the >=3
present threshold), moat_class STRONG unchanged, classification unchanged.

M11 detail. The framework instructs a conservative score with fewer than 6
years and says to state so. Both done. Band 3 fails on CAGR 15.49% < 20%.
Band 1 ("growth >15% but selling % rising") cannot be established because
the selling expense line is not isolable, so the conservative 0 is the
correct application of an unverifiable condition. PASS.

### 1.7 Classification, confidence adjustment, deal-breakers

| Rule | Stated input | Re-derived | Verdict |
| --- | --- | --- | --- |
| Core score | 9+8+19+6+14 | 56/100 | PASS |
| Grand total | 56+17 | 73/160 | PASS |
| Classification matrix | Core 56, moat STRONG | Core 40-59 = AVERAGE regardless of moat class | PASS |
| Data confidence | 3 years | 3-4 = LIMITED, downgrade one tier | PASS |
| Downgrade applied | AVERAGE one tier down | AVOID on the EXCELLENT > GOOD+ > GOOD > AVERAGE > AVOID ladder | PASS |
| DB1 Block A <8 | A = 9 | no trigger | PASS |
| DB2 Block B <8 | B = 8 | no trigger (8 is not <8) | PASS |
| DB3 Median ROCE <10% | 23% | no trigger | PASS |
| DB4 Cum CFO/PAT <0.50 | 1.37 | no trigger | PASS |
| DB5 Pledge >15% | unknown, not asserted | no trigger, cannot fire on unknown | PASS |
| DB6 ND/EBITDA >3x AND IC <3x | 2.64x and 3.41x | conjunction fails on both legs | PASS |
| DB7 Revenue declined in majority | grew both periods | no trigger | PASS |
| DB8 PAT negative in last 3 years | 2.29, 5.10, 4.12 | no trigger | PASS |
| DB9 History <3 years | 3 years | no trigger | PASS |
| deal_breakers field | none triggered | [] correct | PASS |

DB6 is handled well. The maker tested the conjunction under both EBITDA
bases and showed the deal-breaker cannot fire either way, because interest
coverage stays above 3x regardless. That is the right way to close a
sensitivity.

The classification recomputation matters little. E2 at 0 gives Core 51. M5
at the literal 1 gives grand total 74. Both EBITDA bases give Core 55 or 56.
Every one of these lands inside the same 40-59 AVERAGE band and every one
carries the same one-tier LIMITED-history downgrade to AVOID. The Gate 0
decision is robust to all three findings.

### 1.8 Operating rules and output contract

| Rule | Verdict | Note |
| --- | --- | --- |
| Rule 1, one response, no stops | PASS | complete report with terminal YAML |
| Rule 4, source anchors on every number | **FAIL (MINOR)** | Block F derived inputs carry a source class, not a page or line |
| Rule 5, grounded claims, N/A rule | PASS on E3, M6, capex, pledge | fails at E2, counted there |
| Rule 6, opening history statement | PASS | "Data available: 3 years (FY2024 to FY2026). Scoring adapted to 3-year history." |
| Output, dashboard elements | **FAIL (MINOR)** | moat profile bars absent, table substituted; all other elements present |
| YAML flags rule | PASS | classification <= AVERAGE with depressors named, FLAG-GATE0 present |
| YAML field completeness | PASS | all template fields populated, block file matches report block byte for byte |
| Cross-artifact consistency of shared metrics | **FAIL (MINOR)** | current ratio and EBITDA contradict B07, see F6 and F7 |
| analyst_note <=200 words | PASS | approximately 180 words |

Rule 4 detail. The scored line items in Blocks A through E are anchored
properly. The gap is in Block F's derived inputs: net block Rs 20.92 cr
inside the M3 FAT calculation carries no anchor at all, and the operating
EBITDA margin series (2.71 / 7.49 / 3.57) and the GM proxy 31.76% carry only
"screener/AR-derived". Those three inputs drive M1, M2, M3 and M9. The
proxy basis for M9 is stated as the framework requires. Verifier A owns
whether the values are right; I flag only that the anchors are missing.

**Gate 0 tally: 64 rules checked, 59 pass, 5 fail (1 MAJOR, 4 MINOR).**

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

Verifier rule 3: all 23 categories addressed or explicitly NO EVIDENCE;
evidence multipliers applied correctly; the completionist recount performed;
scores consistent with the stated evidence tiers. Verifier rule 8:
categories 21 and 22 present and gated.

### 2.1 Category coverage

| Check | Re-derived | Verdict |
| --- | --- | --- |
| 23 scored rows in the Section 3 summary table | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1 = 4+3+2+2+2+2+2+3+2+1 = 23 | PASS |
| 23 scored rows in the Section 5 scorecard | same 23 plus a Total row | PASS |
| Each category addressed or explicitly NO EVIDENCE | 17 marked NO EVIDENCE FOUND with reasons, 6 carry evidence (A3, E2, F2, G2, H3, R1) | PASS (23/23) |
| Missing categories = REWORK trigger | none missing | not triggered |

Seventeen of the negative rows do more than say NO EVIDENCE. A2, A4, F1, G1
and H1 name the contradicting disclosure (NIL R&D, single-segment note,
rising borrowings, the MD&A Threats section on Chinese price competition).
C2 distinguishes "not disclosed in either direction" from "concentration is
stable", which is the right distinction and rarely made.

### 2.2 Scoring, multipliers, thresholds

| # | Likelihood x Impact | Matrix value | Evidence tier | Multiplier | Weighted | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| A3 | Low x Low | LL = 1 | doc | 1.0 | 1 | PASS |
| E2 | Low x High | LH = 2 | inference | 0.5 | 1 | PASS |
| F2 | Low x Medium | LM = 1 | doc | 1.0 | 1 | PASS |
| G2 | Medium x Low | ML = 1 | doc | 1.0 | 1 | PASS |
| H3 | High x Medium | HM = 3 | doc | 1.0 | 3 | PASS |
| R1 | Low x Medium | LM = 1 | doc | 1.0 | 1 | PASS |
| 17 others | no evidence | 0 | none | none | 0 | PASS |
| Total | | | | | **8** | PASS |

| Rule | Stated | Re-derived | Verdict |
| --- | --- | --- | --- |
| Matrix mapping (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) | 6 scored rows | all 6 map correctly | PASS |
| Multiplier set (doc 1.0, claim 0.7, inference 0.5) | applied to 6 rows | all 6 correct | PASS |
| Adjusted total | 8 | 1+1+1+1+3+1 = 8 | PASS |
| Classification band | <12 = NO MEANINGFUL EMERGING MOAT | 8 < 12 | PASS |
| em_classification enum | "NONE" | matches EXPANSION / STRENGTHENING / MODEST / NONE | PASS |
| Ceiling and scale stated | "8 / 92" | 92 is the post-20-Aug ceiling with I1/I2 | PASS |
| Bands absolute, no rescale | bands applied unchanged | operator ruling 20-Aug-2026 honoured | PASS |
| I1/I2 contribution stated separately | "I1/I2 contribution to the total: 0" | mandated by the same ruling | PASS |
| EM >=25 UA qualifier | 8, stated as failing the qualifier by a wide margin | correct | PASS |

No inflation anywhere in this scan. The one place a maker usually inflates,
a big audited number attached to a moat story, was scored DOWN: E2's export
jump is an audited fact but the China+1 causal claim rests on a data
pattern, so 0.5x is the taxonomy's own correct tier for an inference. The
taxonomy's documented tier lists forward commitment events (capex committed,
patent filed, contract signed, plant under construction, product launched,
application submitted), and an export revenue line is not one of them.
Correct application, and conservative.

### 2.3 Completionist guard and evidence tiers

| Rule | Stated | Verdict |
| --- | --- | --- |
| Recount performed and in the mandated sentence form | "recount performed: 5 items scored at documented quality across 5 categories" | PASS |
| Recount names its items | A3, F2, G2, H3, R1 | PASS |
| Recount matches the scorecard's documented rows | scorecard documented rows are A3, F2, G2, H3, R1, exact match | PASS |
| Base rate 3-6 categories with genuine evidence | 6 categories touch evidence | PASS, at the top of the base rate |
| Guard trigger at 12+ active categories | 6 active, 1 Moderate | not triggered, correctly |
| No claim-only category scored as documented | zero categories are claim-primary; the one management claim (SDPL "near term") is scored against F2, not credited elsewhere | PASS |
| evidence_mix internally consistent | doc 5, claim 1, inference 1 | PASS, see Observation O3 |
| active_categories = Strong/Moderate only | H3 only, matching "Count with Strong/Moderate evidence: 1 (H3)" | PASS |

The verifier's specific test for this rule is a microphone-only category
scoring as if it were documented. Nothing in this scan does that. The
opposite bias is present, which is the correct direction under stage 7's
own scepticism rule.

### 2.4 Categories 21 and 22 (verifier rule 8)

| Rule | Stated | Verdict |
| --- | --- | --- |
| Category 21 (I1 TALENT ASYMMETRY) present | present in narrative, summary table and scorecard | PASS |
| I1 scored above 0 only with both legs evidenced and a documented (b) leg | scored 0; leg (a) fails outright, so the gate cannot be breached | PASS |
| I1 reasoning matches the rule's own language | rejects "management quality / strong team", checks named inventors, ex-DRDO/HAL hires, remuneration annexure | PASS |
| Category 22 (I2 CANNIBALIZATION BARRIER) present | present in narrative, summary table and scorecard | PASS |
| I2 scored above 0 only if the named sacrifice is specific | scored 0 with the explicit "nothing must be destroyed" finding | PASS |
| I2 applied to each moat claimed anywhere in the scan | enumerated against A3, E2, F2, G2, H3, R1, with the named comparator (Bodal Chemicals) | PASS |
| Missing categories = REWORK for stage 7 | not triggered | PASS |
| I1 evidence anchored | remuneration annexure claim carries no page number | **FAIL (MINOR)** |

I2 is the best-executed section of this artifact. The rule asks for the test
to run against every moat claimed anywhere in the scan, which most scans
skip. This one enumerates all six and reaches the honest zero, quoting the
category's own reasoning that an execution lead is not a configuration.

### 2.5 Sections, register, downstream fields, output contract

| Rule | Verdict | Note |
| --- | --- | --- |
| Section 1 (1A, 1B, 1C) executed | PASS | mix table present, every forward cell NOT FOUND rather than estimated |
| Section 2 (2A, 2B, 2C, 2D) executed | PASS on 2A, 2B, 2D | 2C arithmetic not shown, see F8 |
| Section 3 executed, 23 rows plus counts | PASS | |
| Section 4 (4A, 4B, 4C) executed | PASS | R1 assessed active vs emerging as required |
| Section 5 executed, full table, adjusted total | PASS | |
| Optionality register present, 4 columns | PASS | 6 rows, all four columns populated |
| Register scope (scored 0, or claim/inference only) | PASS | see Observation O4 on the H3-adjacent row |
| Section 6 (6A, 6B, 6C, 6D, 6E) executed | PASS | 6A carries all four windows |
| 6C uses the INJECTED Gate 0 block | PASS | Core 56, Moat 17, Grand 73/160, AVOID, moats 5/12, block_b_trend all match B01 |
| 6D combined classification from the standard set | PASS | AVOID, the only consistent cell for AVOID backward plus NONE forward |
| capex_embedded_growth_pct from 2C | **FAIL (MINOR)** | string "NOT FOUND" in a numeric field, arithmetic not shown, see F8 |
| catalysts_12m structure and window | **FAIL (MINOR)** | two of four rows carry 12-24m windows in a 12-month field |
| One improvement, one mechanism | PASS | solar to H3 only, by-product to A3 only, B1 left at NO EVIDENCE, stated explicitly |
| Emerging Moat not conflated with FTTCP | PASS | stated in the header |
| Rule 1, all six sections in one response | PASS | |
| Rule 3, source anchors on evidence items | FAIL at I1 only, counted in 2.4 | all other evidence items anchored |
| YAML field completeness | PASS | block file matches the report block |
| analyst_note <=200 words | PASS | approximately 145 words |

**Emerging Moat tally: 67 rules checked, 64 pass, 3 fail (0 MAJOR, 3 MINOR).**

---

## PART 3: FINDINGS

Severity per the stage 12 scale. CRITICAL means it would change a decision.
MAJOR means wrong but the decision survives. MINOR means imprecision, weak
anchor or cosmetic.

| # | Severity | Location | Rule | Finding | Recomputed value |
| --- | --- | --- | --- | --- | --- |
| F1 | MAJOR | B01 Block E, E2 | Gate 0 rule 5, N/A scores 0 | The metric is promoter holding change over 3 years. The corpus holds only a 1-year change (54.21% to 59.25%). The maker scored full marks 5 on the 1-year proxy. Rule 5 prescribes N/A and 0 for a data point that is not available, and the same maker applied that rule to E3 three lines below. | E2 = 0 (from 5). Block E = 9/20 (from 14). Core = 51/100 (from 56). Grand total = 68 (from 73). Classification unchanged: 51 stays in the 40-59 AVERAGE band, LIMITED-history downgrade still gives AVOID. |
| F2 | MINOR | B01 Block F, M5 | Block F peer-data rule | Score 0 is the framework's prescribed value when peer data is insufficient, so the score stands. The mandated "PEER DATA NEEDED" mark is absent, and the stated basis is company memory (Kiri, Bhageria, Sudarshan), which is memory to weigh, not anchored evidence. On the provided 4-company set SHHARICH ranks 4th, which reads into the literal "top 5 mcap = 1" band. | If read literally: M5 = 1, moat = 18/60, grand total = 74. moats_confirmed 5, moat_class STRONG and classification all unchanged. |
| F3 | MINOR | B01 Block F preamble and M3 | Gate 0 rule 4, mandatory anchors | Net block Rs 20.92 cr (the M3 FAT denominator) carries no anchor. The operating EBITDA margin series (2.71 / 7.49 / 3.57) and the GM proxy 31.76% carry only "screener/AR-derived", not a page or line. These four inputs drive M1, M2, M3 and M9. | No score change. Anchors to be supplied. |
| F4 | MINOR | B01 output format | Gate 0 output contract | The mandated dashboard element "moat profile bars" is absent; a table is substituted. All other mandated elements (blocks, anchored line items, classification, strongest and weakest block, decision line) are present. | Presentational only. |
| F5 | MINOR | B01 Block D, D1 | observation, framework is silent | The EBITDA used for leverage includes Other Income of Rs 3.13 cr, which is 32% of the Rs 9.70 cr denominator. The framework defines no EBITDA basis, and the maker disclosed the sensitivity in the report and in data_notes. Recorded because an Other-Income-inclusive denominator flatters a leverage ratio. Not counted as a rule fail. | Stricter operating basis: ND/EBITDA 3.90x, D1 = 0, Block D = 5/20, Core = 55/100. Band and classification unchanged. Deal-breaker 6 still cannot fire, since interest coverage stays at 3.41x. |
| F6 | MINOR | B01 D4 vs B07 G2 and 6E | cross-artifact consistency | FY26 current ratio contradicts across the run. B01 reports 0.95, rising from 0.87 (AR p.176, consolidated Note 35.22). B07 reports 0.81, falling from 0.87 (MD&A ratio table p.77), and 6E repeats 0.81. The two artifacts disagree on the direction of the change. Referred to Verifier A, whose source-fidelity verdict binds. | No rule outcome changes. D4 = 0 under both readings. G2 raw = 1 under both readings, so em_score stays 8. |
| F7 | MINOR | B01 EBITDA note vs B07 1C | cross-artifact consistency | B01 states its computed EBITDA "reproduces the AR's own disclosed line exactly" at Rs 11.45 cr FY25 and Rs 9.70 cr FY26. B07 quotes the same AR MD&A table as Rs 1,147.66 lakh and Rs 980.64 lakh, which is Rs 11.48 cr and Rs 9.81 cr. "Exactly" does not hold. Referred to Verifier A. | On B07's figure ND/EBITDA is 2.61x, the same 2-3x band. D1 = 1 unchanged. |
| F8 | MINOR | B07 Section 2C and capex_embedded_growth_pct | Stage 7 Section 2C | 2C prescribes an arithmetic (capex under execution x historical fixed asset turnover = implied incremental revenue) and says to show it. Both inputs exist: consolidated CWIP Rs 11.30 cr and the FAT of 8.82x that B01 computed. The maker instead returned NOT FOUND, citing an orchestrator-injected task rule I do not hold, plus Amendment 17. Amendment 17 bars spot-year converter inputs from feeding Section 1B and FTTCP; it does not bar the stage 7 computation itself. The field is also emitted as a string in a numeric slot. UNRESOLVED: the orchestrator must adjudicate against the injected stage-7 text. | If computed: Rs 11.30 cr x 8.82 = about Rs 99.7 cr implied incremental revenue, about +54% of FY26 revenue of Rs 184.50 cr. em_score and classification are unaffected either way. |
| F9 | MINOR | B07 catalysts_12m | field contract | The field feeds Pillar 3 catalyst proximity and is named for a 12-month window. Two of four rows carry 12-24m windows and one carries 12-18m. Each row states its own window, so a downstream consumer can filter. | Presentational. One row (the FY27 volume disclosure) is a true 12m catalyst. |
| F10 | MINOR | B07 I1 | Stage 7 rule 3, anchors | The I1 rejection cites the remuneration annexure ("only promoter-family executives, commerce/CA/MBA/B.Tech backgrounds") with no page number. Every other evidence item in the scan is anchored. | No score change. I1 = 0 stands. |

Counts: CRITICAL 0, MAJOR 1, MINOR 9. F5 is an observation and is not
counted in the rule-fail tally, so it does not affect the acceptance rate.

## PART 4: RECOMPUTATION SUMMARY

Every finding was carried through to the classification to test whether any
of them, alone or together, moves a decision.

| Scenario | Core | Moat | Grand | Band | Confidence adjustment | Final |
| --- | --- | --- | --- | --- | --- | --- |
| As filed | 56 | 17 | 73 | AVERAGE (40-59) | LIMITED, one tier down | AVOID |
| F1 applied (E2 = 0) | 51 | 17 | 68 | AVERAGE | one tier down | AVOID |
| F2 applied (M5 = 1) | 56 | 18 | 74 | AVERAGE | one tier down | AVOID |
| F5 applied (strict EBITDA) | 55 | 17 | 72 | AVERAGE | one tier down | AVOID |
| All three together | 50 | 18 | 68 | AVERAGE | one tier down | AVOID |

The Gate 0 verdict is robust. Core would have to fall below 40 to reach
AVOID on merit rather than on the history downgrade, and would have to rise
above 60 to leave the AVERAGE band. The findings move Core by 6 points at
most in either direction.

The Emerging Moat verdict is equally robust. em_score would have to more
than double, from 8 to 12, to leave the NO MEANINGFUL EMERGING MOAT band.
No finding here moves the score at all. F6, the current ratio contradiction,
is the only finding that touches a scored input (G2), and G2 sits at the
matrix floor of 1 under both readings.

I therefore concur with both stage verdicts as applied: Gate 0 AVOID and
Emerging Moat NONE, combined AVOID.

## PART 5: OBSERVATIONS (not counted as rule fails)

O1. Block A's upward bias. A1 (median ROCE, 4 points) and A2 (minimum
single-year ROCE, 5 points) both rest on 2 of 3 years, and both land in an
upper band. Nine of Block A's 20 points sit on a 2-year window. The
substitution is permitted by rule 6 and disclosed, but a minimum computed
over a subset can only be too high, never too low. The operator should read
A2's 5 as a ceiling, not a measurement. If FY24 ROCE were later recovered
and fell below 15%, A2 would drop by 2 to 5 points.

O2. A framework inconsistency, not a maker error. Deal-breaker 9 caps a
company with under 3 years of history at AVERAGE. The data-confidence rule
sends a company with exactly 3 years one tier below AVERAGE, to AVOID. A
company with less history therefore scores better than one with more. The
maker spotted the interaction and named the two rules as separate. The
framework owner may want to reconcile them, since this run's final label
turns entirely on that one-tier downgrade.

O3. evidence_mix reads item counts as scored-category counts. Sections 1 and
2 carry documented items (the board-approved warrant object clause, the
CWIP ageing note, the solar capex figure) that are not among the five in
evidence_mix. The five match the scorecard's documented rows exactly, which
is the more useful reading, but the field comment says "item counts". Worth
a convention note for the framework rather than a correction here.

O4. Optionality register row 4. "Captive renewable power could structurally
lower unit power cost as revenue scales" extends H3, which scored 3 at
documented quality. The register's scope is items that scored 0 or rest only
on claim and inference evidence. The registered item is the unproven forward
extension rather than the scored capacity addition, so it is defensible, and
the converting evidence named (a second consecutive year of falling Power
and Fuel cost) is exactly right for that extension.

O5. Both artifacts carry unrequested skeptical caveats that improve them:
B01's note that C2 and C4 read strong only because the window starts before
the FY25 spread peak, and B07's downgrade of the export jump to inference
quality against the company's own no-FX-exposure risk note. Neither was
required by the rules. Both are the correct instinct for a converter name.

## PART 6: COVERAGE STATEMENT

131 framework rules checked across two artifacts: 64 on Gate 0, 67 on the
Emerging Moat scan. Every Gate 0 block score was re-derived from the stated
inputs. Every threshold band, every classification cell, all nine
deal-breakers and all three CAGR edge rules were checked. All 23 Emerging
Moat categories, all six scored multipliers and all six matrix mappings were
re-derived.

Not covered, by design: whether any stated input actually appears in the
source PDF at its cited anchor. That is Verifier A's exclusive and
non-overridable domain. F6 and F7 are referred there. Also not covered: the
orchestrator-injected stage-7 task rules, which I do not hold, and which F8
turns on.

Acceptance rate: 123 of 131 rules passed, 94%. Above the 60% REWORK
threshold. No CRITICAL findings. No REWORK trigger fires from this verifier
in phase 1.

```yaml
stage: B12c
company: "SHHARICH"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 64
  fails:
    - "E2 promoter-holding change over 3 years scored 5 on a 1-year proxy; Gate 0 rule 5 prescribes N/A and 0. Recomputed E2=0, Block E=9/20, Core=51/100. Classification unchanged (AVERAGE band, AVOID after history downgrade). MAJOR"
    - "M5 scored 0 without the mandated PEER DATA NEEDED mark, with company-memory peer names as the stated basis; literal read of the provided 4-company set gives M5=1, moat 18/60, grand total 74, classification unchanged. MINOR"
    - "Gate 0 rule 4 anchors: Block F derived inputs unanchored (net block Rs 20.92 cr; operating EBITDA margin series 2.71/7.49/3.57; GM proxy 31.76%). MINOR"
    - "Output contract: mandated dashboard element 'moat profile bars' absent, table substituted. MINOR"
    - "Cross-artifact consistency: FY26 current ratio 0.95 rising (B01, AR p.176) contradicts 0.81 falling (B07, MD&A p.77); FY26/FY25 EBITDA 9.70/11.45 cr (B01, claimed exact) contradicts 980.64/1,147.66 lakh (B07). Referred to Verifier A. No score or classification change under either reading. MINOR"
emoat:
  rules_checked: 67
  fails:
    - "Section 2C prescribed arithmetic (capex under execution x historical FAT) not shown though both inputs exist (CWIP Rs 11.30 cr x FAT 8.82x = about Rs 99.7 cr, about +54% of FY26 revenue); capex_embedded_growth_pct emitted as the string 'NOT FOUND' in a numeric field. Maker cites an orchestrator-injected NOT FOUND rule not in my rule sources. UNRESOLVED, for orchestrator adjudication. MINOR"
    - "catalysts_12m carries two 12-24m rows and one 12-18m row in a 12-month field that feeds Pillar 3 catalyst proximity; each row states its own window. MINOR"
    - "Stage 7 rule 3 anchors: the I1 remuneration-annexure evidence statement carries no page anchor; every other evidence item in the scan is anchored. MINOR"
valuation: {rules_checked: 0, fails: ["pending phase 3"]}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["pending phase 3"]}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "B01 Block E, E2", claimed: "E2 = 5 on a 1-year promoter-holding change of +5.04pp", rule: "Gate 0 rule 5, unavailable data point is N/A and scores 0", recomputed: "E2 = 0, Block E = 9/20, Core = 51/100, grand total 68; classification AVOID unchanged", note: "Metric window is hard-coded at 3 years; the corpus holds 1 year. The same maker applied the N/A rule correctly to E3 in the same block."}
  - {severity: "MINOR", location: "B01 Block F, M5", claimed: "M5 = 0 justified by company-memory peer names", rule: "Block F peer-data rule, score 0 and mark PEER DATA NEEDED", recomputed: "literal read on the provided set gives M5 = 1, moat 18/60, grand total 74; moat_class STRONG and classification unchanged", note: "Score 0 is the framework's prescribed value; the mandated mark is missing and the basis is unanchored memory."}
  - {severity: "MINOR", location: "B01 Block F preamble and M3", claimed: "net block Rs 20.92 cr; margins 2.71/7.49/3.57; GM proxy 31.76%", rule: "Gate 0 rule 4, mandatory source anchors", recomputed: "no score change", note: "Source class given instead of a page or line; these inputs drive M1, M2, M3, M9."}
  - {severity: "MINOR", location: "B01 output format", claimed: "moat scoring presented as a table", rule: "Gate 0 output contract, dashboard elements", recomputed: "presentational only", note: "Moat profile bars absent; every other mandated element present."}
  - {severity: "MINOR", location: "B01 Block D, D1", claimed: "EBITDA Rs 9.70 cr includes Other Income Rs 3.13 cr", rule: "observation, framework defines no EBITDA basis", recomputed: "strict operating basis: ND/EBITDA 3.90x, D1 = 0, Block D = 5/20, Core = 55/100; classification unchanged; deal-breaker 6 still cannot fire", note: "Disclosed by the maker with the sensitivity shown. Observation, not counted in the rule-fail tally."}
  - {severity: "MINOR", location: "B01 D4 vs B07 G2 and 6E", claimed: "FY26 current ratio 0.95 rising vs 0.81 falling", rule: "cross-artifact consistency", recomputed: "D4 = 0 and G2 raw = 1 under both readings; em_score 8 unchanged", note: "Referred to Verifier A, whose source-fidelity verdict binds."}
  - {severity: "MINOR", location: "B01 EBITDA note vs B07 Section 1C", claimed: "B01 says its 9.70/11.45 cr reproduces the AR line exactly; B07 quotes 980.64/1,147.66 lakh", rule: "cross-artifact consistency", recomputed: "ND/EBITDA 2.61x on B07's figure, same 2-3x band, D1 = 1 unchanged", note: "Referred to Verifier A."}
  - {severity: "MINOR", location: "B07 Section 2C and capex_embedded_growth_pct", claimed: "NOT FOUND, arithmetic not run", rule: "Stage 7 Section 2C, show the arithmetic", recomputed: "Rs 11.30 cr x 8.82 = about Rs 99.7 cr, about +54% of FY26 revenue; em_score and classification unaffected", note: "UNRESOLVED. Maker cites an orchestrator-injected rule not in my rule sources. Amendment 17 bars the input from Section 1B and FTTCP, not the stage 7 computation."}
  - {severity: "MINOR", location: "B07 catalysts_12m", claimed: "four catalysts, windows 12m, 12-18m, 12-24m, 12-24m", rule: "field contract, 12-month window feeding Pillar 3", recomputed: "one row is a true 12m catalyst", note: "Each row states its own window, so downstream can filter."}
  - {severity: "MINOR", location: "B07 I1", claimed: "remuneration annexure shows only promoter-family executives", rule: "Stage 7 rule 3, source anchors on every evidence item", recomputed: "I1 = 0 stands", note: "No page number given; every other evidence item in the scan is anchored."}
critical_count: 0
major_count: 1
minor_count: 9
acceptance_rate: 94
```
