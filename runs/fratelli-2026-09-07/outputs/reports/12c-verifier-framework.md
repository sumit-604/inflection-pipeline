# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
## Fratelli Vineyards Ltd (FRATELLI) | Run date 2026-09-07 | Model: Opus

**Scope of this audit: Gate 0 (B01) and Emerging Moat (B07) ONLY.**
Stages 10 and 11 have not executed. The valuation-adherence audit (B11, B10),
the Business Understanding Narrative check (stage 13), the Halt 1 dossier check
(B09b), and the downstream-candidate / method-plurality rules are all deferred
to phase 3. The Master Prompt, the Section 1B layer set, and FTTCP were NOT
loaded for this pass: in phase 1 they are dead context.

Rule sources used, and only these two:
- `/home/user/inflection-pipeline/prompts/01-gate-0-pipeline.md`
- `/home/user/inflection-pipeline/prompts/07-emerging-moat-pipeline.md`

Artifacts audited:
- `outputs/blocks/B01-gate0.yaml` + `outputs/reports/01-gate0.md`
- `outputs/blocks/B07-emoat.yaml` + `outputs/reports/07-emoat.md`

I audit rule application. I do not audit company quality, and I do not audit
whether a number exists in a source PDF. Source fidelity is Verifier A's
non-overridable gate. Where a finding below turns on which of two source figures
is correct, I say so and refer it to Verifier A rather than resolving it.

---

# PART 1 — GATE 0 (B01) COMPLIANCE TABLE

28 rule checks. 26 PASS, 2 FAIL (both MINOR).

| # | Rule (source: 01-gate-0-pipeline.md) | Verdict | Re-derivation / note |
|---|---|---|---|
| G1 | Rule 6: open with "Data available: [X] years... Scoring adapted to [X]-year history" | PASS | Report opens with 8 years, FY2017-FY2021 + FY2024-FY2026, and names the FY22-23 gap. More informative than the template, not less. |
| G2 | ROCE formula; use source ROCE if provided, else compute and state "computed" | PASS | Screener Data Sheet carries no ROCE column; stage computed and labelled "computed" on every row. Capital employed = Total Assets − Current Liabilities per formula for FY24-26 (AR figures). See G28 for the FY17-21 proxy. |
| G3 | A1 median ROCE + band | PASS | Re-derived. Sorted: −9.0, −6.3, −2.3, −2.0, 3.3, 8.7, 11.8, 14.5. Median = (−2.0 + 3.3)/2 = **0.65%**. Report states 0.6%. Band <10 → **0**. Correct. |
| G4 | A2 minimum single-year ROCE + band | PASS | Min = −9.0% (FY26). Band <8 → **0**. Correct. |
| G5 | A3 ROE formula (avg net worth; closing-only for earliest year, stated) + median + band | PASS | Sorted: −17.1, −15.7, −10.5, −6.0, −1.1, −0.7, 5.7, 14.5. Median = (−6.0 + −1.1)/2 = **−3.55%**. Report states −3.5%. Band <12 → **0**. Closing-only NW used for FY17 (earliest, authorised) and FY24 (authorised extension: FY23 absent from every source, stated). Both medians land <12 under either treatment. |
| G6 | A4 ROCE trend latest vs earliest + band | PASS | FY26 −9.0% vs FY17 8.7% = 17.6pp decline. Band >5pp → **0**. Correct. Alternative FY24 anchor tested by the stage; same band. |
| G7 | B1 cumulative CFO ÷ cumulative PAT + band | PASS | 54.41 / −38.18 = **−1.43**. Band <0.50 → **0**. The band delivers 0 on its own terms; no override was needed and none was applied in substance. |
| G8 | B2 FCF-positive proportion + band | PASS | 0 of 3 = 0%. Band <50 → **0**. Window restricted to FY24-26 because pre-FY24 capex is NOT FOUND; per rule 5 the missing years score 0 regardless, so outcome is band-identical. |
| G9 | B3 cumulative FCF ÷ cumulative PAT + band | PASS (with note) | Cumulative FCF −66.74, cumulative PAT −39.04. Literal ratio +1.71. The band text reads "≥0.60 = 5 ... \|**<0.20 or negative = 0**". Cumulative FCF is negative, so the "or negative" clause applies and **0** is the compliant read. NOTE: the report frames this as "flagged as a scoring artifact, not applied" — an override framing — rather than citing the "or negative" clause it is actually entitled to. Presentational only. Even at the literal 5, Block B = 5, core = 15, classification AVOID unchanged, deal-breaker 2 still fires. |
| G10 | B4 WC-days formula, basis rule stated, band | PASS | Basis stated (Sales, not COGS) per the formula's own basis rule. Re-derived FY26: 105.11/181.29×365 = 211.6; payables 27.076/181.29×365 = 54.5; 211.6 + 191.5 − 54.5 = **348.6**. FY24: 116.6 + 80.2 − 47.7 = **149.1**. Change +199.5 days. Band >15 → **0**. Correct. |
| G11 | C1 revenue CAGR formula + band | PASS (with note) | (181.29/421.35)^(1/2) − 1 = **−34.4%**. Correct. Memo (181.29/416.28)^(1/9) − 1 = **−8.83%**, matches the stated −8.8%. NOTE: rule 6 says use whatever history is available; the stage restricted Block C to FY24-26 on a documented basis break. Both windows land in the "<5% = 0" band, so the deviation carries zero score impact and is disclosed in `data_notes`. |
| G12 | CAGR edge rule: negative endpoint → "N/M (negative endpoint)", score 0 | PASS | C2: FY24 −0.15 → FY26 −24.91, both negative, marked N/M, scored 0. Exactly the rule. |
| G13 | C3 positive-YoY proportion + band | PASS | 0 of 2 → <50 → **0**. Cross-checked on the full available set: 2 of 6 computable transitions positive = 33%, same band. |
| G14 | CAGR edge rule: PAT CAGR N/M → C4 = 0 and note | PASS | C4 scored 0 with the rule cited by name. |
| G15 | D1-D4 bands and arithmetic | PASS | D1 negative EBITDA against Rs 119.66 cr net debt → 0. D2 −16.63/13.26 = **−1.25x**, <1.5 → 0. D3 119.74/135.96 = **0.881**, band 0.5-1.0 → **3**. D4 219.36/160.64 = **1.366**, band 1.2-1.49 → **2**. Block D = **5**. Matches YAML. |
| G16 | E1-E4 bands; rule 5 (missing → N/A, score 0, never estimate) | PASS | E1 57.19% → 50-59.9 band → **4**. E2 NOT FOUND (only a 1-year, +0.29pp change exists; the metric specifies 3 years) → **0**, correctly refusing the 1-year proxy. E3 NOT FOUND → **0**. E4 37.88/135.96 = **27.9%**, band 15-30 → **1**. Block E = **5**. Matches YAML. |
| G17 | Block F: 12 tests scored; "PEER DATA NEEDED" where peer data absent, never guessed | PASS | All 12 scored. M2, M5, M7, M9 marked PEER DATA NEEDED and scored 0 per the explicit Block F instruction, and carried into `data_notes`. No peer figure invented anywhere. |
| G18 | M8 distribution band assignment | **FAIL (MINOR)** | See detail below. Band gap resolved downward to 0 without rubric authority. Recomputed alternative: **M8 = 1**, moat_score 1/60. No classification change. |
| G19 | M11 <6-year rule: score conservatively on overall trend and state so | PASS | Stated explicitly. The two-window 3yr+3yr test is genuinely unrunnable on contiguous data given the FY22-23 gap. Negative CAGR fails every non-zero band regardless. |
| G20 | Moat classification band | PASS | 0 tests at ≥3 → 0 present → **NONE** (band "0 = NONE"). Correct. |
| G21 | Core arithmetic + classification matrix | PASS | 0 + 0 + 0 + 5 + 5 = **10**. Core <40 → **AVOID**. Grand total 10 + 0 = **10**. All match YAML. |
| G22 | Data-confidence tier and one-tier downgrade | PASS | 8 raw years = "7-9 moderate"; comparable wine-era history = 3 years = "3-4 LIMITED, downgrade one tier". Stage applied the stricter (conservative) read, set `history_downgrade: true`, and correctly noted AVOID is already the floor so the downgrade cannot bite. |
| G23 | Deal-breaker application, all 9 evaluated | PASS (with note) | 1 (Block A 0 <8) ✓ · 2 (Block B 0 <8) ✓ · 3 (median ROCE 0.6% <10%) ✓ · 4 (CFO/PAT −1.43 <0.50) ✓ · 5 (pledge) correctly declared unevaluable, NOT FOUND, and excluded from the fired list · 6 fired ✓ (see note) · 7 (4 of 6 computable transitions declined = majority) ✓ · 8 (PAT negative FY24, FY25, FY26) ✓ · 9 (history <3y) correctly not fired, exactly 3 comparable years. `deal_breakers: [1,2,3,4,6,7,8]` matches. NOTE on 6: the rule is "ND/EBITDA >3x AND IC <3x". IC = −1.25x clears the second leg. ND/EBITDA is **undefined** (negative EBITDA), not >3x. The stage fired it on the reasoning that positive net debt against negative EBITDA is economically worse than any finite multiple. Defensible and disclosed, but it is an extension of a numeric threshold to an undefined case. Zero outcome impact: AVOID is already core-driven. |
| G24 | Deal-breaker preamble: "state WHICH years drive any deal-breaker" | PASS | Years named for 3, 6, 7, 8; implicit-by-block for 1, 2. Substantially compliant. |
| G25 | Rule 5: never fill a gap with a typical value or estimate | PASS | E2, E3, M2, M5, M7, M9, pre-FY24 capex, and the task brief's Rs 215.6 cr FY24 wine figure are all NOT FOUND rather than estimated. The brief's own figure being refused is the strongest evidence of this rule holding. |
| G26 | Rule 4: source anchor on every extracted number | PASS | Every scoring table carries a source column; AR page and note numbers given for the AR-sourced figures. Existence of those figures at those anchors is Verifier A's call, not mine. |
| G27 | YAML block: all fields present, correct semantics | PASS | All 21 template fields present. `flags` carries FLAG-GATE0, correctly triggered ("classification ≤ AVERAGE with historical depressors identified"). `block_b_trend` gives a direction plus the one number, per the field comment. `analyst_note` ≈145 words, inside the 200-word cap. |
| G28 | `data_notes` field must carry "proxy bases used" | **FAIL (MINOR)** | Two proxy bases are disclosed in the report body but absent from the YAML `data_notes`: (a) FY2017-FY2021 capital employed uses screener "Other Liabilities" as a proxy for Current Liabilities, explicitly flagged as an approximation in the report; (b) WC-days components computed on a Sales basis rather than COGS. The field comment names "proxy bases used" as required content. Downstream stages read the block, not the report body. |

## G18 detail — M8 distribution, the band gap

The M8 rubric is a descending ladder:
- 5 = reach quantified AND growing AND revenue per outlet stable/growing
- 3 = network growing AND rev CAGR ≥15%
- 1 = **mentioned unquantified**
- 0 = **none or purely digital**

Fratelli's network is quantified and growing (31,000 touch points; Shotgun ~9,000
outlets, +2,000 added in FY26, AR FY26 p.11-12 per the stage). Bands 5 and 3 fail
on the revenue conditions — the stage is right about that. But band 1's condition
is "mentioned **unquantified**", which is false here (it is quantified), and band
0's condition is "none or purely digital", which is also false (there is a real
physical network). Unlike M1, M3, M6, M9 and M10, the M8 rubric carries **no
"else 0" clause**. The stage fell through the gap and chose 0.

A quantified, growing network is strictly stronger evidence than an unquantified
mention. Resolving the gap upward to 1 is the reading that respects the ladder's
own ordering; resolving it downward to 0 asserts a condition ("none or purely
digital") that the stage's own evidence contradicts.

Recomputed: **M8 = 1**, moat_score **1/60**. Moats "present" requires ≥3, so
moats_confirmed stays **0**, moat_class stays **NONE**, classification stays
**AVOID**. MINOR: no decision moves. The stage disclosed the choice and flagged
it as "likely understating a real network", which is why this is a MINOR and not
a MAJOR — it is a documented conservative call, not a shortcut.

## Gate 0 verdict

**26 of 28 rule checks PASS (92.9%).** No CRITICAL. No MAJOR. Two MINOR.

I concur with the classification. **AVOID stands under every alternative
treatment I tested**: at the literal B3 = 5 the core is 15, still <40; at M8 = 1
the moat class is still NONE; under the full-history Block C the CAGRs still land
in the zero band. The deal-breaker set is correctly derived and the one
unevaluable deal-breaker (5, pledge) is declared rather than assumed away.

The stage's discipline on NOT FOUND is the strongest thing in this block. It
refused the task brief's own cited FY24 figure rather than adopt it. That is the
never-estimate rule working as designed.

---

# PART 2 — EMERGING MOAT (B07) COMPLIANCE TABLE

29 rule checks. 21 PASS, 8 FAIL (1 MAJOR, 7 MINOR).

| # | Rule (source: 07-emerging-moat-pipeline.md) | Verdict | Re-derivation / note |
|---|---|---|---|
| E1 | All 23 rows scored in Section 5 (22 categories + R1) | PASS | Counted: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1 = **23 rows**. None skipped. |
| E2 | Rule 5: no evidence → state "NO EVIDENCE FOUND", never force-fit | PASS | 14 categories carry the exact phrase. Four of them (A2, F2, G1, G2) go further and name anti-evidence, which is the honest treatment, not a force-fit in either direction. |
| E3 | Rule 2: evidence taxonomy (📄 / 🎙️ / 🔍) applied to every item | PASS | Taxonomy declared at the head of the report and marked per item throughout Sections 1-4. |
| E4 | Rule 3: source anchor on every evidence item | PASS | Filename + page or call + quarter on the evidence items. Existence at anchor is Verifier A's call. |
| E5 | Section 5: raw score from the defined likelihood × impact matrix | **FAIL (MAJOR)** | B2 scored "Likelihood **Medium-High** × Impact Medium (raw 3)", tabled as "3 (MH×M)". "Medium-High" is not a level the matrix defines. See detail below. |
| E6 | Section 5: evidence-quality multiplier (📄 1.0 / 🎙️ 0.7 / 🔍 0.5) | **FAIL (MINOR)** | H2 scored "evidence blended 🎙️/🔍 → weighted 0.7 → 0.7". The report's own text puts H2's load-bearing item (the Mayank Singhal / PI Industries relationship) at "🔍/MEDIA-REGISTRY tier per B08", and calls the older Boisset / Masi / Spurrier collaborations "established, not emerging" — i.e. outside this scan. Rule 4 (be skeptical, prioritise hard evidence) points to **0.5x** on a 🔍-load-bearing blend. Recomputed H2 = **0.5**, total **12.5 → 13**. Classification unchanged. |
| E7 | Adjusted-total arithmetic | PASS | Re-derived: 3.0 + 3.0 + 3.0 + 1.0 + 1.0 + 0.7 + 1.0 = **12.7**. Report states 12.7 → 13. `em_score: 13` matches. |
| E8 | Classification band (≥40 / 25-39 / 12-24 / <12), ABSOLUTE per the 20-Aug-2026 ruling | PASS | 13 → **12-24 MODEST MOAT DEVELOPMENT**. No rescale attempted. `em_classification: "MODEST"` matches the enum. |
| E9 | State the I1/I2 contribution separately (operator review checkpoint) | PASS | "I1/I2 contribution: 0.0", plus an explicit statement that this name should be excluded from the post-10/15 review list because it crosses no threshold at all. Exactly what the ruling asks for. |
| E10 | I1 (Cat 21): score >0 only if BOTH legs evidenced, (b) leg with ≥1 📄 | PASS | Scored 0. Leg (a) fails outright: no patents to name inventors on, no R&D headcount, no above-sector technical remuneration. The stage notes the one remuneration disclosure on file runs the opposite way (KMP table showing Rs 0.00 against Note 33 payments, per B03). Zero is the rule-compliant score, and the stage cites the 20-Aug ruling by name. Not a shortcut. |
| E11 | I2 (Cat 22): score >0 only if the named sacrifice is specific; 0 when "nothing must be destroyed" | PASS | The stage ran the test against each moat it claimed elsewhere (B1 clones, B2 CSD, distribution) and concluded nothing in a competitor's P&L or org must be destroyed. That is the framework's own prescribed answer for an execution lead. Zero here is compliance, not a skip. |
| E12 | Completionist guard performed and stated in the mandated form | PASS | Required sentence present: "📄 recount performed: 14 documented items across 6 categories". Active-category count (3 Strong/Moderate, 7 with any evidence) is far below the 12-category red flag, so no re-scoring was triggered. |
| E13 | Completionist recount internal consistency | **FAIL (MINOR)** | The recount's own arithmetic: A4 5 + B1 3 + B2 2 + C2 1 + F1 1 + H3 1 = 13 across 6 categories, "plus the explicit R&D=NIL anti-evidence item under A2 = 14". The 14th item sits in **A2**, a seventh category. The line therefore reads either 13 items / 6 categories or 14 items / 7 categories, not 14 / 6. Carried into the YAML `completionist_recount` verbatim. |
| E14 | Section 1: 1A, 1B, 1C with the mandated columns | PASS | 1A carries status / evidence type / launch / revenue potential / differentiation. 1C carries current % / expected % / margin direction / profitability impact, with every forward cell marked NOT FOUND rather than interpolated. |
| E15 | Section 2: 2A, 2B, 2C, 2D; 2C must show the arithmetic | PASS | 2A table carries all seven mandated columns. 2B is a clean NOT FOUND (no utilisation % anywhere in corpus). 2C shows the arithmetic explicitly. 2D present. |
| E16 | 2C: "historical fixed asset turnover" basis | **FAIL (MINOR)** | B07 uses FY26 net PP&E Rs 81.56 cr → FAT **2.22x**. B01's M3 uses FY26 net block Rs 96.41 cr → FAT **1.88x**. Same company, same year, two fixed-asset bases and two turnovers. At 1.88x the arithmetic gives Rs 8 cr × 1.88 = Rs 15.0 cr = **8.3%**, not the reported 9.8%/10%. `capex_embedded_growth_pct` would read 8, not 10. Which figure is the correct net fixed-asset base is a source question: **referred to Verifier A**. The framework fault I own is that two pipeline stages ran the same ratio on two bases without reconciling them. |
| E17 | Section 4: 4A, 4B, 4C; R1 assessed | PASS | All three sub-sections present. R1 scored 0 with named reasoning (CSD access is contestable, not exclusive; EU-FTA is a sector-wide headwind, not a company-specific tailwind, and is carried to Section 6 as risk rather than netted into a score). Refusing to book a sector-wide tariff as a company moat is correct discipline. |
| E18 | Optionality register: four mandated columns, table form | PASS | All four columns present, 8 rows, carried into the YAML as `optionality_register[]`. |
| E19 | Register scope: items that scored 0 or rest only on 🎙️/🔍; watched, never scored | PASS (with note) | NOTE: two rows sit adjacent to scored categories — CSD scale-up (B2 scored 3.0) and ESOP grant allocation (F1 scored 1.0). On a careful read both are compliant: what was scored is the 📄 fact (8% of FY26 revenue and the approval dates; the board-approved scheme), and what is registered is the un-evidenced forward extension (scale-up beyond 8%; grants not yet allocated). Neither register row was scored. Flagged only because the boundary is thin enough to invite double-counting in a later stage. |
| E20 | Section 6: 6A-6E, with full reasoning on a TURNAROUND row | PASS | All five sub-sections present. The stage explicitly argues why this is **not** TURNAROUND (B03/B04's turnaround framing was conditioned on a proof gate that has not fired; the wine segment itself posted Ind AS 108 losses two years running). That is the "full reasoning" the prompt demands. |
| E21 | 6C uses the injected B01 block | PASS | Core 10/100, moat_score 0, moat_class NONE, classification AVOID — all four match B01-gate0.yaml exactly. EM shown as 13/92, the correct post-20-Aug ceiling. |
| E22 | 6D combined classification from the standard matrix | PASS | AVOID is in the allowed set. Consistent with the matrix: an AVOID backward score with a MODEST (not EXPANSION) forward score is not the transition setup the operation hunts. |
| E23 | YAML fields present with correct semantics | PASS | All 19 template fields present. `active_categories` correctly limited to the three Strong/Moderate rows (A4, B1, B2); the four Weak rows (C2, F1, H2, H3) are correctly excluded. `analyst_note` ≈90 words, inside cap. |
| E24 | `catalysts_12m` window discipline | **FAIL (MINOR)** | Five entries. One — "Hospitality venture decision point" — carries window **CY27-28**, which is 15 to 28 months from the 2026-09-07 run date, outside the 12-month field. The report's own 6A timeline places hospitality in the **12-24m** bucket, so the block and the narrative disagree. The narrative 6E catalyst list has four items; the YAML has five. This field feeds Pillar 3 catalyst proximity downstream, so a stale window travels. |
| E25 | `evidence_mix` reconciles with the completionist recount | **FAIL (MINOR)** | `evidence_mix: {documented: 15, ...}` against `completionist_recount: "14 documented items"`. The prompt does not define whether `evidence_mix` counts all report evidence or only scored-category evidence, so the populations may legitimately differ — but then they should be stated, and 15 vs 14 is close enough to read as a single population miscounted. Unreconciled in the same block payload. |
| E26 | Stage input scope (AR + 3 main concalls + investor presentation + B01) | **FAIL (MINOR)** | The Section 6E peer cross-check uses `SULA-Investor_Presentation_Q1FY27_2026-08-06.pdf`, which the stage itself names as "not originally listed in this stage's injected inputs". The stage disclosed the deviation in `input_gaps`, marked the finding supplementary, and — correctly — let it change **no score**: E1 stayed 0, hospitality stayed in the register. The output is FLAG-PEER-CONFLICT, a flag, not a number. MINOR and conservative in direction, but it is still material read outside the stage's declared consumption. |
| E27 | Rules 4 and 5: be skeptical, never force-fit | PASS | The strongest compliance in this block. Four categories are scored against the company on documented anti-evidence rather than left blank (A2 R&D = NIL, F2 8 missed promises, G1 cash down 84.5%, G2 WC days 149→349). B1's impact is capped because the contract-farming duration is never stated as a number. C2's 📄 improvement is discounted because it may be an involuntary write-off. This is the taxonomy doing real work. |
| E28 | `analyst_note` ≤200 words | PASS | ≈90 words. |
| E29 | Accurate restatement of the Gate 0 deal-breaker framework in 6C/6D | **FAIL (MINOR)** | 6D says "seven of eight deal-breakers firing"; the YAML `combined_reasoning` repeats "7 of 8 deal-breakers fired". The Gate 0 rubric lists **nine** deal-breakers. Seven fired, one (5, pledge) is unevaluable NOT FOUND, one (9, history <3y) did not fire. The denominator is wrong in both the report and the block. |

## E5 detail — B2's undefined likelihood level, and why it is MAJOR

The Section 5 matrix defines exactly three levels per axis: **HH=4, HM/MH=3,
HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0**. "HM/MH=3" lists both orderings of the
{High, Medium} pair. There is no fourth level.

B2 is scored "Likelihood **Medium-High** × Impact Medium (raw 3)" in Section 3 and
tabled as "3 (MH×M)" in Section 5. Read as written, likelihood is a hybrid the
rubric does not define. The raw 3 is only supportable if likelihood is **High**
(HM = 3). If likelihood is **Medium**, the pair is MM and the raw score is **2**.

Recomputed at MM:

| Variant | Total | Band | Classification |
|---|---|---|---|
| As scored (B2 raw 3, H2 0.7x) | **12.7 → 13** | 12-24 | MODEST |
| B2 raw 2 (MM), H2 as scored | **11.7 → 12** | boundary | MODEST if rounded, **NONE if not** |
| B2 as scored, H2 at 0.5x (E6) | **12.5 → 13** | 12-24 | MODEST |
| Both corrections | **11.5 → 12** | boundary | MODEST if rounded, **NONE if not** |

This is why it is MAJOR rather than MINOR: a one-point swing on an undefined
likedhood level lands the score on the 12.0 MODEST/NONE boundary, where the
classification label depends entirely on a rounding convention the prompt never
states. The stage should restate B2's likelihood as H or M explicitly.

**No decision moves.** Under all four variants em_score sits far below the EM≥25
UA qualifier, `combined_assessment` stays AVOID, and no active category changes
tier. The exposure is to the classification **label**, not to the run's outcome.

One point in the stage's favour on B2's evidence tier: the 1.0x multiplier is
correctly justified. The load-bearing evidence is the 📄 CSD revenue contribution
and the approval-to-sale dates; the 🎙️ "~45% CSD share" claim is explicitly
excluded from the load-bearing set. This is not a 🎙️-only category scoring as 📄,
which is the failure mode my rubric asks me to hunt.

## Emerging Moat verdict

**21 of 29 rule checks PASS (72.4%).** No CRITICAL. One MAJOR (E5). Seven MINOR.

Every one of the eight fails is a block-payload or scoring-notation defect. None
of them is a case of evidence being upgraded to a tier it does not hold, which is
the failure this framework exists to catch. The 23 categories are all scored, the
completionist guard ran, I1 and I2 are both present and both correctly zeroed
against their two-leg and named-sacrifice tests, and the scan's headline number
survives every correction I applied to it.

The credibility-grade-D framing carried at the head of the report — treat every
🎙️ item as unproven narrative until a filed number backs it — is not a rule the
prompt mandates, but it is the rule the prompt intends, applied without being
asked. Worth recording as the opposite of a finding.

---

# PART 3 — CONSOLIDATED FINDINGS

| # | Severity | Location | Rule | Finding | Recomputed |
|---|---|---|---|---|---|
| 1 | MAJOR | B07 Section 3 B2 / Section 5 row B2 | Section 5 likelihood × impact matrix | Likelihood stated as "Medium-High", a level the matrix does not define; raw 3 requires High | B2 raw 2 → em_score 11.7; MODEST/NONE band boundary. Classification label at risk; AVOID unchanged |
| 2 | MINOR | B01 Block F, M8 | M8 band ladder | Quantified, growing network resolved to 0 through a band gap ("mentioned unquantified = 1" / "none or purely digital = 0", no else-clause) | M8 = 1, moat_score 1/60; moat_class NONE and AVOID unchanged |
| 3 | MINOR | B01-gate0.yaml `data_notes` | Field comment: "proxy bases used" | FY17-21 Current Liabilities proxy and the WC-days Sales basis disclosed in the report, absent from the block | — |
| 4 | MINOR | B07 Section 5 row H2 | Evidence multiplier | 0.7x (🎙️) applied where the report's own load-bearing item is 🔍 tier | H2 = 0.5; total 12.5 → 13, unchanged |
| 5 | MINOR | B07 Section 3 guard line / YAML `completionist_recount` | Completionist guard | "14 documented items across 6 categories" — the 14th item is in A2, a seventh category | 13/6 or 14/7 |
| 6 | MINOR | B07 Section 2C vs B01 M3 | 2C fixed-asset turnover | Two fixed-asset bases across two stages: net PP&E 81.56 (FAT 2.22x) vs net block 96.41 (FAT 1.88x). Source question referred to Verifier A | `capex_embedded_growth_pct` 8, not 10, on the B01 basis |
| 7 | MINOR | B07-emoat.yaml `catalysts_12m` | 12-month catalyst field | Hospitality decision point carries a CY27-28 window, outside 12m; the report's own 6A puts it in the 12-24m bucket | Four compliant catalysts, not five |
| 8 | MINOR | B07-emoat.yaml `evidence_mix` | Block payload consistency | documented: 15 against a stated recount of 14; populations undefined and unreconciled | — |
| 9 | MINOR | B07 Section 6E | Stage input scope | Peer deck read outside the stage's declared inputs; disclosed, supplementary, no score impact | — |
| 10 | MINOR | B07 6D / YAML `combined_reasoning` | Gate 0 deal-breaker framework | "seven of eight deal-breakers" — the rubric lists nine (7 fired, 1 unevaluable, 1 not fired) | 7 of 9 |

**No CRITICAL findings.** No misapplication in this phase-1 scope changes a
classification, a deal-breaker set, or the combined assessment. The Gate 0 AVOID
and the B07 MODEST / AVOID both survive every recomputation I ran.

## Recomputed values

- **Gate 0 classification: AVOID.** Concur. Survives B3 at the literal band (core
  15), M8 at 1 (moat class still NONE), and Block C on full history (still zero
  band).
- **Emerging Moat em_score: 13 as scored; 11.5 to 12.7 across the correction
  range.** The classification label is boundary-sensitive; the AVOID combined
  assessment and the EM<25 UA conclusion are not.
- **Destination PE: not in scope.** Phase 3.

## REWORK assessment

No REWORK trigger fires from this verifier. There is no CRITICAL, and
acceptance_rate 82% is well above the 60% floor. My rubric's REWORK-for-stage-7
condition (categories 21 and 22 missing from B07) does **not** fire: both are
present, both scored 0, and both zeros are the rule-compliant treatment rather
than a skip.

Recommended non-blocking corrections before stage 11 consumes these blocks:
1. Restate B2's likelihood as H or M and re-issue em_score (finding 1).
2. Reconcile the FY26 fixed-asset base between B01 M3 and B07 2C, and re-issue
   `capex_embedded_growth_pct` (finding 6) — this one feeds valuation.
3. Drop the CY27-28 hospitality entry from `catalysts_12m` or re-window it
   (finding 7) — this one feeds Pillar 3 catalyst proximity.

## Coverage statement

57 rule checks across two frameworks: 28 on Gate 0 (all six scoring blocks, all
12 moat tests, the classification matrix, the data-confidence tier, all nine
deal-breakers, the CAGR edge rules, and the block payload), 29 on Emerging Moat
(all 23 scored rows, the likelihood × impact matrix, the evidence multipliers,
the completionist guard, the I1/I2 rules, all six sections, the optionality
register, and the block payload). Every arithmetic computation the two prompts
specify was re-derived independently: eight medians and CAGRs, the WC-days
build-up for three years, all four Block D ratios, E4, the core total, the
23-row adjusted total, and the 2C embedded-growth arithmetic.

Not covered, by instruction: B10, B11, the Business Understanding Narrative, the
Halt 1 dossier structural check, downstream signal candidates, method plurality,
and all Section 1B / FTTCP / Master Prompt rules. These are phase 3.

**framework_adherence: 82% (47 of 57 checks passed), Gate 0 and Emerging Moat
scope only.**

---

```yaml
stage: B12c
company: "FRATELLI"
run_date: "2026-09-07"
model: claude-opus-4-8
status: complete
scope_note: "PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07) adherence. Valuation audit (B11/B10), business understanding narrative, Halt 1 dossier, downstream candidates and method plurality are NOT covered; deferred to phase 3. Valuation framework docs not loaded."
gate0:
  rules_checked: 28
  fails:
    - {rule: "Block F M8 band assignment", severity: MINOR, detail: "Quantified, growing 31,000-touchpoint network scored 0 through a band gap; M8 has no else-clause and band 0 reads 'none or purely digital'", recomputed: "M8=1, moat_score 1/60, moat_class NONE and AVOID unchanged"}
    - {rule: "YAML data_notes must carry proxy bases used", severity: MINOR, detail: "FY17-21 Current Liabilities proxy for capital employed, and WC-days Sales basis, disclosed in report body but absent from the block payload", recomputed: ""}
emoat:
  rules_checked: 29
  fails:
    - {rule: "Section 5 likelihood x impact matrix", severity: MAJOR, detail: "B2 scored 'Medium-High x Medium (raw 3)'; Medium-High is not a defined level. Raw 3 requires High; at MM raw is 2", recomputed: "em_score 11.7 vs 12.7; lands on the 12.0 MODEST/NONE boundary. AVOID and EM<25 unchanged"}
    - {rule: "Evidence quality multiplier", severity: MINOR, detail: "H2 given 0.7x where the report's own load-bearing item is 🔍/media-registry tier per B08", recomputed: "H2=0.5, total 12.5 -> 13, classification unchanged"}
    - {rule: "Completionist recount internal consistency", severity: MINOR, detail: "'14 documented items across 6 categories' — the 14th item sits in A2, a seventh category", recomputed: "13 items / 6 categories, or 14 / 7"}
    - {rule: "Section 2C historical fixed asset turnover basis", severity: MINOR, detail: "B07 uses net PP&E 81.56 (FAT 2.22x); B01 M3 uses net block 96.41 (FAT 1.88x). Unreconciled across stages; which base is correct referred to Verifier A", recomputed: "capex_embedded_growth_pct 8 not 10 on the B01 basis"}
    - {rule: "catalysts_12m window discipline", severity: MINOR, detail: "Hospitality decision point windowed CY27-28, 15-28 months out; report's own 6A places it in the 12-24m bucket. Feeds Pillar 3 catalyst proximity", recomputed: "4 compliant catalysts, not 5"}
    - {rule: "Block payload consistency: evidence_mix vs completionist_recount", severity: MINOR, detail: "documented: 15 against a stated recount of 14; populations undefined and unreconciled", recomputed: ""}
    - {rule: "Stage input scope (AR + 3 concalls + presentation + B01)", severity: MINOR, detail: "Section 6E peer cross-check read a SULA deck the stage itself names as outside its injected inputs; disclosed, marked supplementary, changed no score", recomputed: ""}
    - {rule: "Accurate restatement of the Gate 0 deal-breaker framework", severity: MINOR, detail: "6D and combined_reasoning say 'seven of eight deal-breakers'; the Gate 0 rubric lists nine (7 fired, 1 unevaluable, 1 not fired)", recomputed: "7 of 9"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 — B10/B11 do not exist; not audited"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["PENDING PHASE 3 — stage 13 has not executed; not audited, this is not a fail"]}
recomputed_destination_pe: ""
recomputed_decision: ""   # concur: Gate 0 AVOID and B07 MODEST/AVOID survive every recomputation
findings:
  - {severity: MAJOR, location: "B07 Section 3 B2 / Section 5 row B2", claimed: "Likelihood Medium-High x Impact Medium, raw 3, adjusted 3.0", rule: "Section 5 matrix defines only H/M/L per axis; HM/MH=3, MM=2", note: "Undefined likelihood level; one-point swing lands em_score on the 12.0 MODEST/NONE boundary where the label depends on an unstated rounding convention. No decision moves: EM stays far below the EM>=25 UA qualifier and combined_assessment stays AVOID"}
  - {severity: MINOR, location: "B01 Block F, M8", claimed: "M8 = 0", rule: "M8 ladder: 'mentioned unquantified = 1', 'none or purely digital = 0', no else-clause", note: "Network is quantified and growing, so band 1's condition ('unquantified') and band 0's condition ('none') are both false. Gap resolved downward. M8=1 gives moat_score 1/60; moats_confirmed still 0, class still NONE, AVOID unchanged. Disclosed and flagged by the stage, hence MINOR"}
  - {severity: MINOR, location: "B01-gate0.yaml data_notes", claimed: "data_notes omits both proxy bases", rule: "Field comment: data_notes carries 'proxy bases used'", note: "FY17-21 'Other Liabilities' proxy for Current Liabilities in capital employed, and the Sales (not COGS) basis for WC-days, are in the report body only. Downstream stages read the block"}
  - {severity: MINOR, location: "B07 Section 5 row H2", claimed: "blended 🎙️/🔍 weighted 0.7x", rule: "📄 1.0x / 🎙️ 0.7x / 🔍 0.5x, plus rule 4 skepticism", note: "Load-bearing item is the Singhal/PI relationship, which the report itself puts at 🔍/media-registry tier. At 0.5x, H2=0.5 and total 12.5 -> 13"}
  - {severity: MINOR, location: "B07 Section 3 guard line and YAML completionist_recount", claimed: "14 documented items across 6 categories", rule: "Completionist guard recount line", note: "A4 5 + B1 3 + B2 2 + C2 1 + F1 1 + H3 1 = 13 across 6; the 14th (A2 R&D=NIL anti-evidence) is a seventh category"}
  - {severity: MINOR, location: "B07 Section 2C vs B01 Block F M3", claimed: "FAT 2.22x (B07) vs 1.88x (B01), same company same year", rule: "2C uses 'historical fixed asset turnover'", note: "Net PP&E 81.56 vs net block 96.41. Which figure is correct is a source question referred to Verifier A. On the B01 basis capex_embedded_growth_pct is 8, not 10. Feeds valuation"}
  - {severity: MINOR, location: "B07-emoat.yaml catalysts_12m", claimed: "Hospitality venture decision point, window CY27-28", rule: "catalysts_12m = next 12 months; feeds Pillar 3 catalyst proximity", note: "15-28 months from the 2026-09-07 run date. The report's own 6A timeline places it in the 12-24m bucket, so block and narrative disagree"}
  - {severity: MINOR, location: "B07-emoat.yaml evidence_mix", claimed: "documented: 15", rule: "Block payload internal consistency with the stated 📄 recount of 14", note: "Populations may legitimately differ but are never stated; 15 vs 14 reads as one population miscounted"}
  - {severity: MINOR, location: "B07 Section 6E peer cross-check", claimed: "SULA Q1FY27 deck read", rule: "Stage consumes AR + 3 main concalls + investor presentation + B01", note: "Stage itself names the file as outside its injected inputs. Disclosed in input_gaps, marked supplementary, changed no score (E1 stayed 0, hospitality stayed in the register); output was a flag, not a number"}
  - {severity: MINOR, location: "B07 6D and YAML combined_reasoning", claimed: "'seven of eight deal-breakers fired' / '7 of 8'", rule: "Gate 0 lists nine deal-breakers", note: "Seven fired, deal-breaker 5 (pledge) unevaluable NOT FOUND, deal-breaker 9 (history <3y) did not fire. Wrong denominator in both report and block"}
critical_count: 0
major_count: 1
minor_count: 9
acceptance_rate: 82            # 47 of 57 rule checks passed
framework_adherence_note: "82% over 57 checks. COVERS GATE 0 (B01) AND EMERGING MOAT (B07) SCOPE ONLY. Gate 0: 26/28 = 93%. Emerging Moat: 21/29 = 72%. No CRITICAL; no REWORK trigger fires (no Verifier A-grade finding here, acceptance_rate well above the 60% floor). Categories 21 and 22 are both present in B07 and both correctly scored 0 against their two-leg and named-sacrifice tests, so the stage-7 REWORK condition does not fire. Gate 0 AVOID and B07 MODEST/AVOID survive every recomputation run."
```
