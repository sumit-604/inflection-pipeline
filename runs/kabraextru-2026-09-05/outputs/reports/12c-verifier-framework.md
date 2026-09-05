# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: Kabra Extrusion Technik Ltd (KABRAEXTRU) | Run date: 2026-09-05 | Model: claude-opus-4-8
Status: **partial-phase1**

## SCOPE OF THIS PASS

This pass audits two frameworks only:
- Gate 0 scorecard rules — `prompts/01-gate-0-pipeline.md`
- Emerging Moat 22-category scan rules — `prompts/07-emerging-moat-pipeline.md`

Artifacts audited:
- `runs/kabraextru-2026-09-05/outputs/reports/01-gate0.md` and `outputs/blocks/B01-gate0.yaml`
- `runs/kabraextru-2026-09-05/outputs/reports/07-emoat.md` and `outputs/blocks/B07-emoat.yaml`
- One rule-source cross-check against `inputs/screening/screener-Data_Sheet.csv` (to test whether
  the source supplies its own ROCE, a Gate 0 formula rule). No other input document was read.

Deferred to phase 3 (not audited here, per the task scope):
- The valuation-adherence audit (verifier rule 4). B10 and B11 do not exist yet. Master Prompt
  v3.6, the Section 1B layer set, and FTTCP v2.1 were **not** loaded.
- Verifier rule 6 (B09 downstream candidates), rule 7 (method plurality in B11), rule 9 (Business
  Understanding Narrative in stage 13), rule 10 (B09b dossier at /finalize), rules 11 and 12
  (Role 1 exit construction and Amendment 19 FV path). None of the source artifacts exist yet.
- Verifier rule 8 (categories 21 and 22) **is** in scope and was run. See E-20 and E-21.

This verifier audits rule application. It does not audit company quality. It does not audit whether
a number exists in a source PDF. Verifier A owns source fidelity, and its verdicts bind.

---

## PART 1 — GATE 0 (B01) COMPLIANCE TABLE

Every block score below was re-derived from the inputs the B01 report itself states, using the
thresholds in `prompts/01-gate-0-pipeline.md`. "Recomputed" shows my independent value.

### 1.1 Pipeline operating rules

| # | Rule (source) | Verdict | Recomputed / evidence |
|---|---|---|---|
| G-01 | Entire scorecard in one response, no stops (rule 1) | PASS | Single report, all blocks present |
| G-02 | Opening line "Data available: [X] years (FY__ to FY__). Scoring adapted to [X]-year history." (rule 6) | PASS | Present verbatim in substance, line 11-13 |
| G-03 | Source anchor on every extracted number (rule 4) | PASS | Per-table blanket anchors plus per-line anchors; no bare number found in a scored line item |
| G-04 | Grounded claims; missing data marked N/A and scored 0, never estimated (rule 5) | PASS | E3 pledge NOT FOUND scored 0 with the explicit statement that absence is not evidence of 0% |
| G-05 | Use whatever history exists, minimum 3 years (rule 6) | PASS | 10-year window used; B2/B3/B4 constrained to 3 years, constraint disclosed inline and in data_notes |

### 1.2 Formula definitions

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| G-06 | ROCE = EBIT ÷ (Total Assets − Current Liabilities); use the source's own ROCE if provided; else compute and state "computed" | **FAIL (MINOR)** | Denominator substituted with (Equity + Reserves + Borrowings). Recomputed: the literal denominator is **not computable** from the stated source — I checked `screener-Data_Sheet.csv` and it carries no ROCE row and no current/non-current liability split (only an unsplit "Other Liabilities" row, line 42). Proxy validated against AR Note 43: FY26 0.62% computed vs 0.61% disclosed, FY25 8.63% vs 8.67%. A1 median unchanged at 10.31% → score 1. See finding F-01 for the two readings. |
| G-07 | ROE = PAT ÷ average Net Worth; earliest year may use closing, must state so | PASS | FY26 −5.37/451.94 = −1.19%; FY25 32.20/457.14 = 7.04%; FY17 closing-only basis stated |
| G-08 | WC Days = Rec + Inv − Pay, revenue basis unless COGS explicitly available and stated | PASS | FY24 59.5+143.3−48.7 = 154.1; FY26 64.7+231.6−52.6 = 243.7. Revenue basis used, matching the default |
| G-09 | FCF = CFO − capex (PPE + intangibles from cash flow, excluding acquisitions) | PASS | FY24/25/26 = −14.01 / −24.70 / −28.42. Screener's aggregate investing line correctly refused as a capex proxy |
| G-10 | CAGR = (End ÷ Start)^(1/years) − 1 | PASS | C1 over 10 observations uses 9 periods, which is correct |

### 1.3 CAGR edge rules

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| G-11 | Negative or zero endpoint → mark "N/M (negative endpoint)" and score 0 | PASS | C2 marked with the exact phrase, scored 0 |
| G-12 | Swing noted in data_notes; no synthetic CAGR attempted | PASS | data_notes carries "profit-to-loss swing, FY25 to FY26". The rule names the loss-to-profit direction; the maker logged the mirror case, which is the conservative read. No synthetic CAGR |
| G-13 | C4 scored 0 and noted when PAT CAGR is N/M | PASS | C4 = 0 with the note |

### 1.4 Block scoring, line by line

| # | Line item | Stated input | Band applied | Score | Recomputed | Verdict |
|---|---|---|---|---|---|---|
| G-14 | A1 median ROCE | 10.31% | 10-14.9 | 1 | 10.31% (5th/6th of 10 sorted values = 10.07, 10.55) | PASS |
| G-15 | A2 min ROCE | 0.62% | <8 | 0 | 0.62% | PASS |
| G-16 | A3 median ROE | 8.86% | <12 | 0 | 8.86% (8.70, 9.02) | PASS |
| G-17 | A4 ROCE trend | −9.93pp | >5pp decline | 0 | 0.62 − 10.55 = −9.93pp | PASS |
| G-18 | B1 cum CFO/PAT | 0.543 | 0.50-0.69 | 1 | 122.26 / 225.18 = 0.5429 | PASS |
| G-19 | B2 FCF-positive years | 0 of 3 | <50% | 0 | 0% | PASS |
| G-20 | B3 cum FCF/PAT | −1.107 | negative | 0 | −67.13 / 60.65 = −1.107 | PASS |
| G-21 | B4 change in WC days | +89.6 | increase >15 | 0 | 243.7 − 154.1 = +89.6 | PASS |
| G-22 | C1 revenue CAGR | 5.61% | 5-9.9 | 1 | (451.05/276.08)^(1/9) − 1 = 5.61% | PASS |
| G-23 | C2 PAT CAGR | N/M | N/M | 0 | Negative endpoint | PASS |
| G-24 | C3 positive YoY years | 3 of 9 = 33.3% | <50 | 0 | FY21, FY22, FY23 up; six down | PASS |
| G-25 | C4 PAT − Rev CAGR | N/M | rule | 0 | Forced by edge rule | PASS |
| G-26 | D1 ND/EBITDA | 4.19x | >3x | 0 | 141.98 / 33.86 = 4.19x; narrower operating-EBITDA basis 13.6x, both clear the band | PASS |
| G-27 | D2 interest coverage | 0.317x | <1.5 | 0 | 3.61 / 11.39 = 0.317x | PASS |
| G-28 | D3 debt/equity | 0.329x | 0.1-0.5 | 4 | 145.06 / 441.49 = 0.329x | PASS |
| G-29 | D4 current ratio | 1.55x | 1.5-1.99 | 4 | Source's own figure used, AR Note 43 | PASS |
| G-30 | E1 promoter holding | 60.49% | ≥60 | 5 | 60.49% | PASS |
| G-31 | E2 3-year change | +0.26pp | ±1% | 3 | Derived FY23 60.23% from FY24 total 60.24% less the stated FY24 change +0.01%. Arithmetic from two disclosed figures, flagged as derived. Not an estimate | PASS |
| G-32 | E3 pledge | NOT FOUND | rule 5 | 0 | Correct application of the N/A-scores-0 rule | PASS |
| G-33 | E4 contingent liab / NW | 5.68% | 5-15 | 3 | 25.05 / 441.49 = 5.67% | PASS |
| G-34 | M1 pricing power | −8.51pp margin, CAGR 5.61% | else | 0 | No band fits above 0 | PASS |
| G-35 | M2 cost advantage | 16.09pp below peer median | below | 0 | Peer median 18.40% of three peers | PASS |
| G-36 | M3 capital efficiency | FAT 1.83x, ROCE <12% | else | 0 | 451.05 / 246.46 = 1.83x | PASS |
| G-37 | M4 customer stickiness | 6 decline years | 3+ decline | 0 | Six of nine | PASS |
| G-38 | M5 scale and dominance | 3rd of 4 mcap, lowest margin | top 5 mcap | 1 | Top-3 mcap tier fails on the margin leg; tier 3 applies | PASS |
| G-39 | M6 technology / R&D | 1.22% R&D, margin below peer median | else | 0 | ≥1% tier requires above-median margin, which fails | PASS |
| G-40 | M7 regulatory / licence | unregulated | unregulated | 0 | — | PASS |
| G-41 | M8 distribution | reach quantified, no growth | "mentioned unquantified" | 1 | **FAIL (MINOR)**. The band scored is worded for an *unquantified* mention; the report states reach IS quantified but static. Recomputed: no band fits cleanly. Strict alternative = 0 → moat 3 → 2, grand total 25 → 24, moats_confirmed 0 unchanged, class NONE unchanged, classification AVOID unchanged. See F-02 | FAIL |
| G-42 | M9 brand | GM proxy 35.72% vs 37.02% | at/below | 0 | Proxy formula and its use stated, as the rule requires | PASS |
| G-43 | M10 switching costs | growth with 6 decline years | 2+ decline | 1 | — | PASS |
| G-44 | M11 network effects | latest 3yr −12.4% vs prior +44.9% | else | 0 | Two-window test correctly run on 10 years | PASS |
| G-45 | M12 negative WC | 154-244 days | >45 | 0 | — | PASS |

### 1.5 Classification, overrides, and output

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| G-46 | Moat "present" at ≥3; classification band | PASS | 0 of 12 at ≥3 → NONE. Highest single score is 1 |
| G-47 | Block totals and core arithmetic | PASS | A1+B1+C1+D8+E11 = 22. Moat 3. Grand total 25 |
| G-48 | Data confidence tier and history downgrade | PASS | 10 years → "10+ yrs full", no downgrade, `history_downgrade: false` |
| G-49 | Classification matrix | PASS | Core 22 < 40 → AVOID |
| G-50 | All nine deal-breakers evaluated, correct triggers | PASS | 1, 2, 6, 7, 8 fire. 3 (median ROCE 10.31%) and 4 (0.543) correctly not fired. 5 correctly not fired on absent pledge data. 9 not fired |
| G-51 | Deal-breaker application (caps do not upgrade a base-matrix AVOID) | PASS | Base matrix AVOID plus deal-breaker 6's direct AVOID. The GOOD and AVERAGE caps are ceilings, not floors, and are correctly non-binding |
| G-52 | State which years drive any deal-breaker | PASS | Years stated for 6, 7, 8. Deal-breakers 1 and 2 are whole-window block scores with no driving year to name |
| G-53 | Dashboard output format (blocks, line items, moat bars, classification box, strongest/weakest, decision line) | PASS | All present |
| G-54 | YAML block schema complete and consistent with the report | PASS | Every field populated; block file and report block are byte-consistent |
| G-55 | FLAG-GATE0 emitted when classification ≤ AVERAGE with depressors identified | PASS | Present, with the depressor named at segment level |
| G-56 | `block_b_trend` carries the one number that shows it | PASS | "deteriorating", WC days 154 → 244 |
| G-57 | `analyst_note` ≤ 200 words | PASS | ~157 words |
| G-58 | `data_notes` carry swings, proxy bases, and PEER DATA NEEDED items | PASS | 13 notes including both proxy bases and the peer-comparability caveat. No PEER DATA NEEDED item arises: peer sheets were supplied |

**Gate 0 result: 58 rules checked, 56 PASS, 2 FAIL (both MINOR).**

**Recomputed Gate 0 outcome: core 22 / 100, moat 3 / 60, grand total 25 / 160, moat class NONE,
classification AVOID. I concur with B01 on every headline value.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE TABLE

### 2.1 Structure and coverage

| # | Rule (source) | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-01 | All six sections executed in one response (rule 1) | PASS | Sections 1-6 plus the optionality register all present |
| E-02 | Section 1A/1B/1C with the required columns | PASS | 1A carries status, evidence type, launch, revenue potential, differentiation. 1C carries current %, 3-year %, margin direction, profitability impact |
| E-03 | Section 2A capex table with the required columns | PASS | Project, ₹Cr, funding, status, commissioning, capacity, % over current. NOT FOUND used where the AR is silent |
| E-04 | Section 2B utilisation per facility | PASS | NOT FOUND stated; the <10% inference explicitly graded 🔍 |
| E-05 | Section 2C arithmetic shown | PASS | 40.89 × 1.83 = 74.83; 74.83 / 451.05 = 16.6%. Recomputed identical |
| E-06 | Section 2D new geography | PASS | NO EVIDENCE FOUND, supported by declining export earnings |
| E-07 | All 22 categories addressed or explicitly NO EVIDENCE (verifier rule 3) | PASS | Counted: A1-A4 (4), B1-B3 (3), C1-C2 (2), D1-D2 (2), E1-E2 (2), F1-F2 (2), G1-G2 (2), H1-H3 (3), I1-I2 (2) = 22. Each carries a verdict |
| E-08 | R1 addressed with 4A, 4B, 4C | PASS | 23rd row present and scored |
| E-09 | Section 3 summary table, all rows, four required columns | PASS | 23 rows with evidence?, type, strength, time to materialise |
| E-10 | Strong/Moderate count stated | PASS | "2 of 22 (A4, C2)" |

### 2.2 The completionist guard

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-11 | Recount performed and stated in the mandated form | PASS | "📄 recount performed: 9 documented items across 4 categories" |
| E-12 | Guard threshold (12+ active categories triggers re-examination) | PASS | 4 categories score above 0. The guard does not fire. The report still compares itself to the 3-6 base rate and justifies landing below it |

### 2.3 Evidence taxonomy and multipliers

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-13 | Taxonomy applied to every evidence item, three tiers only (rule 2) | **FAIL (MINOR)** | A fourth tier, 📰 MEDIA-REPORTED, is introduced for the 2026 preferential issue. Recomputed: the item scores 0 and sits in the optionality register, so em_score is unaffected. The defect is formal, plus one downstream leak. See F-03 |
| E-14 | Source anchor on every evidence item (rule 3) | PASS | Page-marked AR anchors and dated slide anchors throughout |
| E-15 | Raw scores match the likelihood × impact matrix | PASS | A4 HM = 3, C2 HM = 3, F2 LM = 1, R1 HL = 2. All correct against HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1 |
| E-16 | Multipliers 📄 1.0 / 🎙️ 0.7 / 🔍 0.5 applied correctly | PASS | All four scored rows are 📄 at 1.0. Arithmetic exact |
| E-17 | Scores consistent with the stated evidence tiers (no 🎙️-only row scoring as 📄) | PASS | A4 rests on a launched product (📄 AR26 p.5, p.29) and a documented no-cell-manufacture strategy (📄 p.34, p.36). C2 rests on a Note 38 disclosure. F2 rests on the CWIP schedule. R1 rests on cited policy documents. No 🎙️-only category is scored |
| E-18 | Adjusted total arithmetic | PASS | 3.0 + 3.0 + 1.0 + 2.0 = 9.0 |
| E-19 | Classification band (absolute, no rescale) | PASS | 9 < 12 → NO MEANINGFUL EMERGING MOAT. Ceiling stated as 92 |

### 2.4 Family I (verifier rule 8)

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-20 | Category 21 (I1) present; scored above 0 only if both legs evidenced with a 📄 (b) leg | PASS | I1 present, scored 0. Leg (a) shown absent: no patents to carry named inventors, no ex-major staff concentration, remuneration annexure covers only directors, CFO, and CS. Scoring 0 needs no leg evidence, so no violation |
| E-21 | Category 22 (I2) present; scored above 0 only if the sacrifice is named and specific | PASS | I2 present, scored 0, with the honest "nothing must be destroyed" answer applied to each candidate moat |
| E-22 | I1/I2 contribution stated separately | PASS | "I1/I2 contribution: 0", with the 20-Aug-2026 ruling cited |

### 2.5 Optionality register and Section 6

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-23 | Register present with the four required columns, holding 0-scored or 🎙️/🔍-only items | PASS | Six rows, four columns, all covering unscored or claim-grade items |
| E-24 | Register items watched, never scored | PASS | No register item appears in the Section 5 scoring table |
| E-25 | 6A timeline across four windows | PASS | 12m, 12-24m, 24-36m, 3-5yr |
| E-26 | 6B risks with early warning signs for the top-scoring moats | PASS | A4 and C2 each carry a risk and a named early warning |
| E-27 | 6C uses the injected Gate 0 block | PASS | Core 22, moat 3, moats_confirmed 0, AVOID, NONE. Matches B01 exactly |
| E-28 | 6D combined classification from the standard set, with full reasoning on HIGH POTENTIAL and TURNAROUND | PASS | AVOID selected; both rows reasoned even though neither applies |
| E-29 | 6E final card: evolution map, 12-month catalysts, biggest risk | PASS | All three present, map given per family |

### 2.6 Block payload

| # | Rule | Verdict | Recomputed / evidence |
|---|---|---|---|
| E-30 | YAML schema complete; block file matches the report | PASS | Every field populated; block file and report block are consistent |
| E-31 | `active_categories` holds Strong/Moderate rows only | PASS | A4 and C2 only. F2 (Weak) and R1 (Weak/Low) correctly excluded |
| E-32 | `evidence_mix` item counts substantiated | **FAIL (MINOR)** | The body supports only "roughly 25" documented items and never enumerates claim or inference items. Recomputed: not verifiable from the artifact. The one auditable count is the recount line's 9 documented scoring-weight items. See F-04 |
| E-33 | `catalysts_12m` entries sit inside the 12-month window with evidence type and anchor | **FAIL (MINOR)** | Catalyst 4 carries `window: "12-24m"` inside a 12-month field, and drifts from 6A, which places the same item in the next-12m bucket as "begins showing in the CWIP schedule". Recomputed: either restate the window as 0-12m for the CWIP appearance, or move the item out of `catalysts_12m`. See F-05 |
| E-34 | `capex_embedded_growth_pct` matches Section 2C | PASS | 16.6 in both |
| E-35 | `time_to_materialise` consistent with the stated evidence | **FAIL (MINOR)** | A4 carries "HV e-bus packs 12-24m" while Section 1A records the same product's expected launch as "NOT FOUND (no date given)". Recomputed: "ongoing (RESS live now; HV e-bus packs NOT FOUND)". No score change. See F-06 |
| E-36 | `analyst_note` ≤ 200 words | PASS | ~107 words |
| E-37 | Never force-fit; NO EVIDENCE FOUND stated where evidence is absent (rule 5) | PASS | 19 of 23 rows carry an explicit no-evidence verdict, several with negative counter-evidence named |
| E-38 | Skepticism: management claims not credited as documented (rule 4) | PASS | Dropped Dec-2023 claims scored 0 and flagged; the "Rs 1,500+ Cr optimal" claim held at 🎙️ and unscored |

**Emerging Moat result: 38 rules checked, 34 PASS, 4 FAIL (all MINOR).**

**Recomputed em_score: 9.0 / 92. Recomputed classification: NO MEANINGFUL EMERGING MOAT (NONE).
I concur with B07 on both.**

---

## PART 3 — VALUATION ADHERENCE (B11)

**NOT RUN. Out of phase-1 scope.** B10 and B11 do not exist for this run. The valuation framework
documents were not loaded. `valuation: {rules_checked: 0, fails: []}` in the block below.
`recomputed_destination_pe` and `recomputed_decision` are both marked "pending phase 3".

## PART 4 — BUSINESS UNDERSTANDING NARRATIVE (verifier rule 9)

**NOT AUDITABLE. Stage 13 has not run.** Every field of `business_understanding_narrative` is left
at its pending default. No fail is recorded: a rule cannot fail against an artifact that does not
exist. This check must run in the phase-3 pass, and a missing or bullet-formatted narrative there
is a hard REWORK for stage 13.

---

## FINDINGS

Severity scale: CRITICAL (fabricated or materially wrong, would change a decision) | MAJOR (wrong
but the decision likely survives) | MINOR (imprecision, weak anchor, cosmetic).

### F-01 — MINOR — B01 Formula Notes, ROCE denominator (rule G-06)

The Gate 0 formula set is fixed: ROCE = EBIT ÷ (Total Assets − Current Liabilities). B01 substituted
(Equity Share Capital + Reserves + Borrowings).

Recomputed. The literal denominator cannot be built from the stated source. I opened
`inputs/screening/screener-Data_Sheet.csv`: it carries no ROCE row, and its balance sheet has a
single unsplit "Other Liabilities" line (line 42), so current liabilities cannot be isolated. Two
readings follow:

- As filed (proxy, cross-validated): median ROCE 10.31% → A1 = 1 → Block A = 1 → core 22 → AVOID.
- Strict (input unavailable, rule 5 forces N/A → 0): A1 = 0 and A4 = 0 → Block A = 0 → core 21 →
  grand total 24 → AVOID.

Classification is AVOID under both. The proxy also matches the company's own disclosed Schedule III
ROCE to within 0.05pp (FY26 0.62% vs 0.61%; FY25 8.63% vs 8.67%), so the filed reading is the
better analysis. Graded MINOR, not MAJOR: no band moves, no deal-breaker changes state, and the
deviation is disclosed twice in the artifact. One live caution for phase 3: deal-breaker 3 (median
ROCE <10%) sits 0.31pp away, and its state depends on the capital-employed basis. Deal-breaker 3
caps at AVERAGE, which is above the AVOID already in force, so it cannot bind here.

### F-02 — MINOR — B01 Block F, M8 Distribution band language (rule G-41)

M8 was scored 1 under the band "mentioned unquantified". The report's own text says the reach IS
quantified (100+ countries, 15,000+ installations) and simply shows no growth trend. The scored
band therefore does not describe the evidence.

Recomputed: the four M8 bands leave a gap for quantified-but-static reach. Tiers 5 and 3 both fail
on the growth leg (revenue CAGR 5.61% < 15%). The strict alternative is 0, giving moat 3 → 2 and
grand total 25 → 24, with moats_confirmed 0, moat class NONE, and classification AVOID all
unchanged. Scoring 1 is the conservative in-band choice and the reasoning was shown. Action for the
framework owner, not for this run: close the M8 rubric gap.

### F-03 — MINOR — B07 mode note, taxonomy extension (rule E-13)

The stage 7 taxonomy has three tiers. B07 adds a fourth, 📰 MEDIA-REPORTED, for the reported 2026
preferential issue, which sits entirely outside the run's corpus.

Recomputed: em_score is unaffected. The item scores 0, is excluded from Section 5, and is carried in
the optionality register, which is the correct conservative handling. Two residual risks: the
extension was made on the launching agent's instruction, which the stage prompt does not authorise;
and the item then appears as catalyst 1 in `catalysts_12m` with `evidence_type: "media-reported"`, a
value outside the taxonomy. `catalysts_12m` feeds Pillar 3 catalyst proximity at stage 11. Phase-3
guard: stage 11 must either exclude this catalyst or carry the MODERATE cap, and must not treat it
as pipeline-verified evidence.

### F-04 — MINOR — B07 block, `evidence_mix` counts (rule E-32)

`evidence_mix: {documented: 25, claim: 10, inference: 6}`. The report body says "roughly 25"
documented items and never enumerates the claim or inference populations.

Recomputed: not verifiable from the artifact. The only auditable count is the recount line, "9
documented items across 4 categories" carrying scoring weight. A hedged "roughly" in prose should
not become an exact integer in a structured field. No score impact.

### F-05 — MINOR — B07 block, `catalysts_12m` window drift (rule E-33)

Catalyst 4 (commissioning of the Rs 31.77 Cr commitment) carries `window: "12-24m"` inside a field
scoped to 12 months, and it contradicts Section 6A, which places the same item in the next-12m
bucket on the narrower test of whether the spend "begins showing in the CWIP schedule".

Recomputed: restate as 0-12m for the CWIP appearance, or move the commissioning test out of
`catalysts_12m`. Material because Pillar 3 scores catalyst proximity, and a 12-24m item scored as a
12m item overstates proximity.

### F-06 — MINOR — B07 Section 3 and block, A4 time to materialise (rule E-35)

The summary table and `active_categories` give A4 as "HV e-bus packs 12-24m". Section 1A records the
same product's expected launch as "NOT FOUND (no date given)".

Recomputed: "ongoing (RESS live now; HV e-bus packs NOT FOUND)". No score impact. The house rule is
that NOT FOUND is the only valid fill for a missing number, and a window assigned to an undated
development item is a soft estimate.

### F-07 — INFO (scope note, not a defect)

Business Understanding Narrative and valuation adherence are pending phase 3. Stage 13 and stage 11
have not run. No fail is recorded against either.

---

## OBSERVATIONS (no rule broken, carried for the operator)

1. **B2/B3/B4 sit on a 3-year window while B1 sits on 10.** Rule 6 permits it and the constraint is
   disclosed. Sensitivity: with a full 10-year capex series, B2 could reach 2 and B3 could reach 3.
   Even at Block B = 6, deal-breaker 2 (<8) still fires, core rises only to 27, and classification
   stays AVOID. The gap is corpus coverage, not rule application. FY17-FY23 annual reports would
   close it.
2. **E2 rests on a derived FY23 promoter figure.** 60.24% less the stated +0.01% change gives
   60.23%. That is arithmetic from two disclosed figures, not an estimate, and it is flagged as
   derived. Had it been treated as NOT FOUND, E2 = 0 and Block E = 8, core = 19, classification
   still AVOID.
3. **M5 rests on a four-company universe.** "Top 5 mcap" is close to automatic when only four
   companies are compared. The rule was applied as written and the thin comparator set is disclosed.
   Worth a wider peer set before any phase-3 relative work.
4. **B01 and B07 agree without collusion risk.** B07 consumed the B01 block as an injected input,
   which the stage prompt requires, and reproduced core 22, moat 3, and moats_confirmed 0 exactly.
   No unexplained drift between the two artifacts.
5. **Both stages emitted their flags.** FLAG-GATE0 in B01; FLAG-EMOAT and FLAG-DROPPED-CLAIMS in
   B07. The dropped-claims flag is a genuine addition beyond the rubric and is well evidenced.

---

## VERDICT

Both frameworks were applied as written. 96 rules checked across Gate 0 and the Emerging Moat scan,
90 passed, 6 failed, all six MINOR. No CRITICAL and no MAJOR finding. Acceptance rate 93.8%, well
above the 60% REWORK trigger.

I recompute Gate 0 at core 22 / 100, moat 3 / 60, grand total 25 / 160, moat class NONE,
classification AVOID. I recompute the Emerging Moat scan at 9.0 / 92, classification NONE. I concur
with both makers on every headline value and on the combined AVOID assessment.

The two artifacts share one pattern worth naming: every deviation found was disclosed by the maker
in the artifact itself, and every deviation was forced by a corpus gap rather than by a shortcut.
That is the correct failure mode.

---

```yaml
stage: B12c
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-opus-4-8
status: partial-phase1
gate0:
  rules_checked: 58
  fails:
    - "G-06 ROCE denominator substituted (NW+Borrowings) for the fixed Total Assets - Current Liabilities; literal denominator not computable from the source; proxy cross-validated to AR Note 43 within 0.05pp; A1 unchanged at 10.31% -> 1; MINOR"
    - "G-41 M8 scored 1 under the 'mentioned unquantified' band though the report states reach is quantified but static; strict alternative 0 -> moat 3 to 2, grand total 25 to 24, class NONE and AVOID unchanged; MINOR"
emoat:
  rules_checked: 38
  fails:
    - "E-13 fourth evidence tier (media-reported) introduced outside the three-tier taxonomy; item unscored so em_score unaffected; leaks into catalysts_12m evidence_type; MINOR"
    - "E-32 evidence_mix counts {25,10,6} not enumerated in the report body ('roughly 25'); only the 9-item recount is auditable; MINOR"
    - "E-33 catalysts_12m entry 4 carries a 12-24m window inside a 12-month field and drifts from Section 6A; overstates Pillar 3 catalyst proximity; MINOR"
    - "E-35 A4 time_to_materialise '12-24m' for HV e-bus packs contradicts Section 1A 'NOT FOUND (no date given)'; recomputed 'NOT FOUND'; MINOR"
valuation: {rules_checked: 0, fails: []}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: "pending phase 3"
recomputed_decision: "pending phase 3"
findings:
  - {severity: "MINOR", location: "B01 Formula Notes / Block A", item: "ROCE denominator substituted for the fixed formula", claimed: "median ROCE 10.31% -> A1 = 1, Block A = 1, core 22", recomputed: "literal denominator not computable from screener-Data_Sheet.csv (no ROCE row, no current/non-current split); strict N/A reading gives A1 = 0, Block A = 0, core 21, grand total 24; classification AVOID under both", note: "Disclosed twice by the maker and cross-validated against AR Note 43 (FY26 0.62% vs 0.61%; FY25 8.63% vs 8.67%). Deal-breaker 3 sits 0.31pp away and depends on this basis, but it caps at AVERAGE and cannot bind an AVOID."}
  - {severity: "MINOR", location: "B01 Block F, M8", item: "Band language does not describe the evidence", claimed: "M8 = 1 under 'mentioned unquantified'", recomputed: "no band fits; strict alternative M8 = 0 -> moat 3 to 2, grand total 25 to 24", note: "Rubric gap for quantified-but-static reach. Conservative in-band choice, reasoning shown. No change to moats_confirmed, moat class, or classification."}
  - {severity: "MINOR", location: "B07 mode note / catalysts_12m", item: "Evidence tier outside the three-tier taxonomy", claimed: "media-reported tier for the 2026 preferential issue", recomputed: "em_score unaffected (item scores 0, held in the optionality register)", note: "Phase-3 guard: stage 11 must exclude this catalyst from Pillar 3 or carry the MODERATE cap. It is not pipeline-verified evidence."}
  - {severity: "MINOR", location: "B07 block, evidence_mix", item: "Item counts not substantiated in the report body", claimed: "{documented: 25, claim: 10, inference: 6}", recomputed: "not verifiable; only the recount line (9 documented items across 4 categories) is auditable", note: "A hedged 'roughly 25' in prose became an exact integer in a structured field. No score impact."}
  - {severity: "MINOR", location: "B07 block, catalysts_12m entry 4", item: "Window exceeds the field scope and contradicts Section 6A", claimed: "window 12-24m inside catalysts_12m", recomputed: "0-12m for the CWIP appearance, or move the commissioning test out of the field", note: "Pillar 3 scores catalyst proximity; a 12-24m item inside a 12m field overstates proximity."}
  - {severity: "MINOR", location: "B07 Section 3 summary and active_categories", item: "Time to materialise contradicts the stated evidence", claimed: "A4 'HV e-bus packs 12-24m'", recomputed: "'ongoing (RESS live now; HV e-bus packs NOT FOUND)'", note: "Section 1A records the same product's expected launch as NOT FOUND. NOT FOUND is the only valid fill for a missing date. No score impact."}
  - {severity: "INFO", location: "scope", item: "Phase-1 scope note, not a defect", claimed: "n/a", recomputed: "n/a", note: "Valuation adherence (B10/B11) and the Business Understanding Narrative (stage 13) are pending phase 3; neither artifact exists yet, so no rule was failed against them. Both must be audited in the phase-3 pass."}
critical_count: 0
major_count: 0
minor_count: 6
acceptance_rate: 93.8
```
