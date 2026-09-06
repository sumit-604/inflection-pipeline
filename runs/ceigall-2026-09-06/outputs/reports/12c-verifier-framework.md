# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: CEIGALL INDIA LTD (CEIGALL) | Run date: 2026-09-06 | Model: claude-opus-4-8

## SCOPE OF THIS PASS

Phase 1 scope as instructed. Two compliance audits run:

- **Gate 0 (B01)** against `prompts/01-gate-0-pipeline.md`
- **Emerging Moat (B07)** against `prompts/07-emerging-moat-pipeline.md`

Not run, and why:

| Verifier C rule | Status |
|---|---|
| Rule 4 (valuation B11) | NOT RUN — stage 11 runs in phase 3 |
| Rule 5 (destination-PE tolerance) | NOT RUN — no valuation artifact |
| Rule 6 (downstream candidates, B09) | NOT RUN — B09 not in scope |
| Rule 7 (method plurality, B11) | NOT RUN — no B11 |
| Rule 9 (Business Understanding Narrative, B13) | NOT RUN — stage 13 not yet run |
| Rule 10 (Halt 1 dossier B09b) | NOT RUN — fires at the /finalize verifier pass |
| Rules 11-12 (v3.8 exit, Amendment 19 FV path) | NOT RUN — no Role 1 output |

The valuation framework documents (Master v3.6, the Section 1B layer set, FTTCP v2.1)
were not loaded. They are consumed only by the deferred valuation audit.

Rules 2, 3 and 8 were run in full. Rule 1 governs: I audit rule application, not
company quality and not raw source fidelity. Number-existence questions belong to
Verifier A and are handed off, not adjudicated here.

Artifacts audited:
- `/home/user/inflection-pipeline/runs/ceigall-2026-09-06/outputs/blocks/B01-gate0.yaml`
- `/home/user/inflection-pipeline/runs/ceigall-2026-09-06/outputs/reports/01-gate0.md`
- `/home/user/inflection-pipeline/runs/ceigall-2026-09-06/outputs/blocks/B07-emoat.yaml`
- `/home/user/inflection-pipeline/runs/ceigall-2026-09-06/outputs/reports/07-emoat.md`

Re-derivation data: `inputs/screening/screener-Data_Sheet.csv` (the one populated
screener file; the other four are header-only, a collector defect, disclosed by the
stage at report line 6-13).

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### 1.1 Operating rules and formula definitions

| # | Rule (source line) | Check | Verdict |
|---|---|---|---|
| G01 | Opening line exact form "Data available: [X] years (FY__ to FY__). Scoring adapted to [X]-year history." (L25-26) | Report L4 carries it verbatim for 6 years FY2021-FY2026 | PASS |
| G02 | Source anchors mandatory on every extracted number (L15-19) | Every figure carries (screener-data) or a named computed basis | PASS |
| G03 | Grounded claims; unavailable data marked "N/A (not in provided data)" and scored 0; never fill with typical values (L20-23) | Applied at B2, B3, B4, D4, E1-E4, M12. No estimate anywhere | PASS |
| G04 | ROCE: use the source's ROCE if provided, else compute and state "computed" (L30-32) | Data_Sheet cut carries no ratios section (verified: CSV has no ROCE row). Stage computed and stated "computed" | PASS |
| G05 | ROE = PAT ÷ average net worth; earliest year may use closing, must state so (L33-34) | FY21 uses closing NW 305.29 and states the rule (report L51-52) | PASS |
| G06 | WC Days formula, and the basis (revenue vs COGS) must be stated (L35-39) | Revenue basis stated for receivable and inventory days | PASS |
| G07 | FCF = CFO − capex, capex from the cash flow statement (L40-41) | CF section carries only three aggregate lines. Capex line genuinely absent, verified in the CSV (rows 57-59). N/A is the correct fill | PASS |
| G08 | CAGR = (End÷Start)^(1/years) − 1 (L42) | Applied on a 5-period basis for a 6-point series. Correct | PASS |
| G09 | CAGR edge rules: N/M on a negative or zero endpoint; loss-to-profit note; C4 = 0 when PAT CAGR N/M (L44-51) | Both endpoints positive for revenue and PAT, so no N/M. The stage additionally records "No PAT loss-to-profit swing in the FY21-FY26 window" in data_notes, which is the affirmative statement the rule invites | PASS |

### 1.2 Block A — re-derived

EBIT = PBT + Interest; Capital Employed = Equity Share Capital + Reserves +
Borrowings. Cross-check on the prompt's own definition (Total Assets − Current
Liabilities): FY26 = 5523.36 − 2074.08 = 3449.28, identical to the stage's
3449.28. The "Other Liabilities" proxy is the only current-liability-equivalent
line the sheet carries, and the stage disclosed the substitution (report L23-28).

| Year | EBIT (mine) | CE (mine) | ROCE (mine) | ROCE (stage) |
|---|---|---|---|---|
| FY21 | 157.80 | 334.99 | 47.11% | 47.10% |
| FY22 | 180.02 | 747.56 | 24.08% | 24.08% |
| FY23 | 276.90 | 1295.99 | 21.36% | 21.36% |
| FY24 | 499.50 | 1953.97 | 25.56% | 25.56% |
| FY25 | 518.95 | 3229.63 | 16.07% | 16.07% |
| FY26 | 577.99 | 3449.28 | 16.76% | 16.76% |

Median ROCE = (21.36 + 24.08) ÷ 2 = 22.72%. Min = 16.07%.
Median ROE = (32.66 + 34.18) ÷ 2 = 33.42%.

| # | Rule | Input | Band | Score | Verdict |
|---|---|---|---|---|---|
| G10 | A1 Median ROCE | 22.72% | 20-24.9 = 4 | 4 | PASS |
| G11 | A2 Min single-year ROCE | 16.07% | ≥15 = 5 | 5 | PASS |
| G12 | A3 Median ROE | 33.42% | ≥20 = 5 | 5 | PASS |
| G13 | A4 ROCE trend latest vs earliest | 16.76 vs 47.10, −30.34pp | decline >5pp = 0 | 0 | PASS |
| G14 | Block A total | 4+5+5+0 | — | 14/20 | PASS |

A4 note: the stage scored the rule as written and refused to soften it, while
recording that FY21 sits on a 982,100-share pre-IPO base. That is the correct
order of operations. Score by rule, flag by note.

### 1.3 Block B — re-derived

Cumulative CFO = 103.18 −134.59 −72.66 −210.83 −519.56 −91.28 = **−925.74**.
Cumulative PAT = 112.50+125.86+167.27+306.14+294.02+311.89 = **1317.68**.
Ratio = **−0.7026x**. Both sums reproduce the stage exactly.

| # | Rule | Input | Band | Score | Verdict |
|---|---|---|---|---|---|
| G15 | B1 Cumulative CFO/PAT | −0.70x | <0.50 = 0 | 0 | PASS |
| G16 | B2 FCF-positive years | capex line absent | N/A → 0 per L20-23 | 0 | PASS |
| G17 | B3 Cumulative FCF/PAT | same | N/A → 0 | 0 | PASS |
| G18 | B4 Change in WC Days | trade payables lumped inside "Other Liabilities" | N/A → 0 | 0 | PASS |
| G19 | Block B total | — | — | 0/20 | PASS |

B4 handling is the correct call and worth naming. The formula requires Trade
Payables specifically. Row 42 of the CSV carries only an undifferentiated "Other
Liabilities" line. Using it as a payables proxy would have been an estimate, which
the never-estimate rule forbids. The stage instead reported the ex-payables
receivable-plus-inventory move (26.97 → 66.71 days) as informational and explicitly
not the scored metric. That is the right separation.

`block_b_trend` is populated with the required "one number that shows it"
(−0.70x, CFO negative 5 of 6 years). PASS.

### 1.4 Block C — re-derived

Revenue CAGR = (4022.40 ÷ 873.20)^(1/5) − 1 = **35.73%**.
PAT CAGR = (311.89 ÷ 112.50)^(1/5) − 1 = **22.62%** (stage: 22.63%; rounding at
the second decimal, band-neutral, handed to Verifier A).

| # | Rule | Input | Band | Score | Verdict |
|---|---|---|---|---|---|
| G20 | C1 Revenue CAGR | 35.73% | ≥20 = 5 | 5 | PASS |
| G21 | C2 PAT CAGR | 22.62% | ≥20 = 5 | 5 | PASS |
| G22 | C3 Positive YoY revenue years | 5 of 5 = 100% | 100% = 5 | 5 | PASS |
| G23 | C4 PAT CAGR − Revenue CAGR | −13.10pp | <−8pp = 0 | 0 | PASS |
| G24 | Block C total | 5+5+5+0 | — | 15/20 | PASS |

### 1.5 Block D — re-derived

EBITDA FY26 = 417.62 + 61.70 + 160.37 − 54.26 = **585.43**. All six years reproduce.
Net Debt = 1311.14 − 378.68 = **932.46**.

| # | Rule | Input | Band | Score | Verdict |
|---|---|---|---|---|---|
| G25 | D1 Net Debt/EBITDA | 932.46 ÷ 585.43 = 1.593x | 1-2x = 3 | 3 | PASS |
| G26 | D2 Interest coverage | 577.99 ÷ 160.37 = 3.604x | 3-4.9 = 2 | 2 | PASS |
| G27 | D3 Debt/Equity | 1311.14 ÷ 2138.14 = 0.613x | 0.5-1.0 = 3 | 3 | PASS |
| G28 | D4 Current ratio | no current/non-current split in the sheet | N/A → 0 | 0 | PASS |
| G29 | Block D total | 3+2+3+0 | — | 8/20 | PASS |

The non-financial banding was used throughout, correct for an EPC contractor.
The Banks/NBFC alternates (CAR, PCR, default D3 = 3) were rightly not invoked.

### 1.6 Block E

| # | Rule | Check | Verdict |
|---|---|---|---|
| G30 | E1-E4 with no shareholding source | All four marked "N/A (not in provided data)" and scored 0 per L20-23 | PASS |

This is the scored-zero-versus-evidence-gap distinction the framework cares about,
and the stage held it. Block E's 0/20 is carried into `core_score` because the rule
says score 0, and it is simultaneously labelled an evidence gap rather than a
governance finding in `flags`, `data_notes`, the analyst note, the weakest-block
line and the decision line. The framework demands the score; the operator needs the
distinction. Both are present. PASS.

### 1.7 Block F — 12 moat tests

Supporting re-derivations: EBITDA margin FY21 18.29% → FY26 14.55%, a 3.74pp
decline. FAT FY26 = 4022.40 ÷ 341.15 = 11.79x. Receivable days FY21 15.11 → FY26
57.68. Selling and admin as % of sales 0.80% (FY21) → 1.84% (FY25); the FY26 cell
is genuinely blank in the CSV (row 17), as the stage stated.

| # | Test | Stage score | My re-derivation | Verdict |
|---|---|---|---|---|
| G31 | M1 Pricing power | 1 | Margin −3.74pp with revenue CAGR 35.73% ≥10% → "declined 2-5pp despite growth" = 1 | PASS |
| G32 | M2 Cost advantage | 0 | No peer source. Rule L100-101 mandates 0 + "PEER DATA NEEDED". Marked | PASS |
| G33 | M3 Capital efficiency | 3 | FAT 11.79x, FY26 ROCE 16.76% → FAT>2x AND ROCE>15% = 3. See finding C-05 | PASS (advisory) |
| G34 | M4 Customer stickiness | 3 | Zero decline years, but receivable days +42.6 breaks the ±10 leg of the 5-band; "max 1 decline year" tier = 3 | PASS |
| G35 | M5 Scale and dominance | 0 | No mcap/margin ranking source. PEER DATA NEEDED marked | PASS |
| G36 | M6 Technology/R&D | 0 | No R&D line item. Else-branch = 0 regardless | PASS |
| G37 | M7 Regulatory/licence | 0 | Listed-player count unavailable. PEER DATA NEEDED marked | PASS |
| G38 | M8 Distribution | 0 | "none or purely digital = 0" for an EPC contractor | PASS |
| G39 | M9 Brand | 0 | Peer GM median unavailable. GM proxy computed and labelled a proxy per L126 | PASS |
| G40 | M10 Switching costs | 0 | Growth every year but receivable days +42.6 fails bands 5 and 3; band 1 requires 2+ decline years, of which there are none; else = 0. Literal application confirmed | PASS |
| G41 | M11 Network effects | 1 | Latest window 15.23% < prior window 53.90% kills the 5-band; overall CAGR 35.73% >15% with selling % rising → 1. Window choice disclosed; see observation O-02 | PASS |
| G42 | M12 Negative WC/float | 0 | WC days not computable without payables. Consistent with B4 | PASS |
| G43 | Block F total | 8/60 | 1+0+3+3+0+0+0+0+0+0+1+0 = 8 | PASS |
| G44 | Moats "present" at ≥3 | 2 (M3, M4) | Confirmed | PASS |
| G45 | Moat classification | MODERATE | 2-3 present = MODERATE | PASS |

M10 deserves a note in the stage's favour. The tempting error was to award a
consolation 1 for six years of unbroken revenue growth. The rule's third band is
gated on "2+ decline years", which zero decline years does not satisfy, so the
else-branch fires and the score is 0. The stage read the AND-conditions literally
and took the harsher outcome. Correct.

### 1.8 Totals, confidence, matrix, deal-breakers

| # | Rule | Check | Verdict |
|---|---|---|---|
| G46 | Core score | 14+0+15+8+0 = 37/100 | PASS |
| G47 | Grand total | 37+8 = 45/160 | PASS |
| G48 | Data confidence band (L143-145) | 6 years → "5-6 lower", flagged "may not have seen full cycle"; the one-tier downgrade belongs to the 3-4 band only, so `history_downgrade: false` | PASS |
| G49 | Classification matrix (L147-150) | Core 37 < 40 → AVOID | PASS |
| G50 | Deal-breakers 1-9 (L156-160) | See table below | PASS |
| G51 | Output format + YAML schema | See 1.9 | PASS |

Deal-breaker re-derivation, all nine:

| Rule | Condition | Actual | Fires? | Stage | Verdict |
|---|---|---|---|---|---|
| 1 | Block A <8 → max GOOD | A = 14 | No | Not fired | Correct |
| 2 | Block B <8 → max GOOD | B = 0 | **Yes** | Fired, recorded | Correct |
| 3 | Median ROCE <10% → max AVERAGE | 22.72% | No | Not fired | Correct |
| 4 | Cumulative CFO/PAT <0.50 → max AVERAGE | −0.70x | **Yes** | Fired, recorded | Correct |
| 5 | Pledge >15% → max AVERAGE | no pledge data | No | Not fired; stage states it can neither confirm nor deny | Correct |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | 1.59x and 3.60x | No | Not fired | Correct |
| 7 | Revenue declined in majority of years | 0 decline years | No | Not fired | Correct |
| 8 | PAT negative in any of last 3 years | FY24-26 all positive | No | Not fired | Correct |
| 9 | History <3 years → AVERAGE | 6 years | No | Not fired | Correct |

Rule 5 is the one that could have gone wrong. A deal-breaker cannot fire on absent
data, and it also cannot be quietly assumed clear. The stage did neither: it left
the rule unfired and said in the report why. That is the correct handling.

Cap-versus-matrix interaction: the two fired caps are max GOOD and max AVERAGE. The
matrix result is AVOID, which sits below both. Caps are therefore non-binding and
there is no conflict. The stage states this explicitly (report L270-273). Correct.

The framework's instruction to "state WHICH years drive any deal-breaker" (L155)
is satisfied. FY22-FY26 is named in `flags`, in `block_b_trend`, in the analyst note
and in the Block B section. It is not repeated inside the `deal_breakers[]` strings
themselves, which is a presentational point, not a gap.

### 1.9 Output and block conformance

Dashboard elements required at L163-166: all blocks with line items and anchors
(present), moat profile bars (report L236), classification box (L226-241),
strongest/weakest block (L243-249), decision line (L279-289). All present.

B01 YAML carries every schema field: `input_gaps`, `flags`, `data_years`,
`fy_range`, `blocks`, `core_score`, `moat_score`, `grand_total`, `moats_confirmed`,
`moat_class`, `classification`, `deal_breakers`, `history_downgrade`, `data_notes`,
`block_b_trend`, `analyst_note`. The `flags` trigger condition is met
(classification ≤ AVERAGE with historical depressors identified) and a FLAG-GATE0
entry is present. `analyst_note` runs about 145 words, inside the 200-word cap.

**Gate 0 result: 51 rules checked, 51 passed, 0 fails. One advisory (C-05).**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### 2.1 Structure and operating rules

| # | Rule | Check | Verdict |
|---|---|---|---|
| E01 | All six sections executed in one response (L28) | Sections 1-6 plus the Optionality Register all present | PASS |
| E02 | Section 1: 1A pipeline with status/evidence/launch/potential/differentiation, 1B diversification, 1C mix shift | All three present with the mandated columns | PASS |
| E03 | Section 2: 2A capex table, 2B utilisation, 2D new geographies | All present | PASS |
| E04 | Section 2C: capex × FAT arithmetic shown (L61-63) | **Not computed.** See finding C-01 | **FAIL (MINOR)** |
| E05 | All 22 categories addressed or explicit NO EVIDENCE FOUND (L39-40) | Summary table carries 23 rows: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1. Every non-scoring row states NO EVIDENCE FOUND, NOT APPLICABLE, or "evidence against" | PASS |
| E06 | R1 addressed via Section 4 (4A/4B/4C) | All three sub-parts present | PASS |
| E07 | Evidence taxonomy 📄/🎙️/🔍 applied to every item (L29-35) | Applied item by item throughout Sections 1-4 | PASS |
| E08 | Source anchors on every evidence item (L32-33) | (AR sheet __), (Inv. Pres. p.__), (Mon-Year call) throughout. Anchor style differs from the prompt's examples (AR sheets because the AR is a scanned document read by sheet, disclosed at report L3; calls dated rather than Q_ FY__), but every item is traceable | PASS |
| E09 | Skepticism, never force-fit (L38-40) | The scan argues against itself in five places (G1, G2, H1 fold-in, I1, I2). No force-fit found | PASS |
| E10 | Completionist guard recount performed with the required line (L41-46, L158-159) | "📄 recount performed: 6 documented items across 4 categories" present at report L132 | PASS |
| E11 | Base-rate statement accurate against the framework text | Report calls 4 categories "below the base rate of 3-6". Four is inside 3-6. See finding C-02 | **FAIL (MINOR)** |
| E12 | Section 3 summary table, all rows, four columns, Strong/Moderate count stated | Table complete; "Categories with Strong/Moderate evidence: 0" stated | PASS |

### 2.2 Scoring mechanics re-derived

Matrix per L172-173: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.
Multipliers: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x.

| Row | Stated L×I | Raw (mine) | Weight | Adjusted (mine) | Stage | Verdict |
|---|---|---|---|---|---|---|
| C2 | Medium × Low | ML = 1 | 📄 1.0 | 1.0 | 1.0 | PASS |
| E1 | Low × Low | LL = 1 | 🔍 0.5 | 0.5 | 0.5 | PASS |
| F2 | Medium × Medium | MM = 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |
| R1 | Medium × Medium | MM = 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |
| I1 | — | 0 | — | 0.0 | 0.0 | PASS |
| I2 | — | 0 | — | 0.0 | 0.0 | PASS |
| Other 17 | none | 0 | — | 0.0 | 0.0 | PASS |
| **Total** | | | | **4.3** | **4.3** | PASS |

| # | Rule | Check | Verdict |
|---|---|---|---|
| E13 | Likelihood × impact matrix applied per scored row | Re-derived above, all four correct | PASS |
| E14 | Evidence multipliers applied correctly | Re-derived above, all four correct | PASS |
| E15 | No 🎙️-only category scored as if 📄 (Verifier C rule 3) | **No instance.** Every deviation runs the conservative way, not the credited way. E1 is tagged 🔍/📄 in the summary table but weighted at 0.5x, the lower of the two. F2 is tagged 📄/🎙️ and weighted 0.7x. R1 is tagged 🎙️/📄 and weighted 0.7x. In each case the stage applied the weaker multiplier to a mixed-evidence row | PASS |
| E16 | Adjusted total arithmetic | 1.0+0.5+1.4+1.4 = 4.3 | PASS |
| E17 | Classification band, absolute thresholds, no rescale (L175-181) | 4.3 < 12 → NO MEANINGFUL EMERGING MOAT. Stage states the absolute-threshold ruling and applies no rescale | PASS |
| E18 | I1/I2 contribution stated separately (L180-181) | Report L168: "I1/I2 contribution: 0.0", with the non-crossing noted for the operator's post-10/15-scan review checkpoint | PASS |

The direction of the evidence-tier discipline is the finding that matters here.
The failure mode this rule exists to catch is a management claim scored as a
documented fact. The stage did the reverse on all three mixed rows: it took the
lower multiplier every time, and at F2 it netted a genuinely documented delivery
record down against the B05 promise-delivery grade because guidance delivery is
part of F2's own definition. That netting is defensible on the category text, and
it is disclosed in its own flag (FLAG-EMOAT-NETTED).

### 2.3 Categories 21 and 22 (Verifier C rule 8)

| # | Rule | Check | Verdict |
|---|---|---|---|
| E19 | Category 21 (I1) present | Present, scored 0 | PASS |
| E20 | I1 scored above 0 only if both legs evidenced with the (b) leg carrying ≥1 📄 | Scored 0. Part (a) exists as 📄 bios (WTD PhD IIT Roorkee; COO ex-NHAI/ex-BRO). Part (b), the structural-economics leg, has no evidence: no PSU pay-ceiling arithmetic, no documented failed poaching. The stage cites the rule that part (a) alone is a hiring story and zeroes the row | PASS |
| E21 | Category 22 (I2) present | Present, scored 0 | PASS |
| E22 | I2 scored above 0 only if the named sacrifice is specific | Scored 0. The stage answers the framework's own question ("what must the best-resourced competitor destroy") with "nothing", names the peers who already run HAM SPV structures, and applies the rule that an execution lead is a category-0 finding | PASS |

I1 and I2 are where an analyst reaching for a score would have found room. The
company hands over exactly the material that invites a soft I1 credit: named
senior hires with PSU and defence-infrastructure pedigree. The stage refused it on
the missing (b) leg. That is the rule working as designed.

### 2.4 Optionality register and Section 6

| # | Rule | Check | Verdict |
|---|---|---|---|
| E23 | Optionality register table, four mandated columns, covering rows scored 0 or resting only on 🎙️/🔍 (L183-193) | Present, six rows, all four columns populated. Covers D2 (AI tools), I1 (talent), R1 derivative (bid-norm share gain), renewables/T&D, international, HAM monetisation. E1 is not registered; defensible since its LOAs are 📄. See observation O-03 | PASS |
| E24 | 6A timeline with all four windows | Next 12m, 12-24m, 24-36m, 3-5yr all present with a milestone each | PASS |
| E25 | 6B risks per top-scoring moat with early warning signs | One risk plus one early-warning signal for each of F2, C2, E1, R1 | PASS |
| E26 | 6C combined table using the INJECTED Gate 0 block | Core 37/100 AVOID, moat 8/60 MODERATE 2/12, both reproduce B01 exactly. No drift, no re-derivation of the injected block | PASS |
| E27 | 6D combined classification from the standard matrix, with full reasoning where HIGH POTENTIAL / TURNAROUND are in play | AVOID backward + NONE forward → AVOID. The stage gives the full reasoning for why neither transition cell applies, which is what L204-208 asks for | PASS |
| E28 | 6E final card: evolution map per family, 12m catalysts, biggest risk | All three present | PASS |

On E27: the framework goes out of its way to say a GOOD or AVERAGE backward score
paired with an EXPANSION forward score is the setup this operation hunts. That is
an invitation to find a transition. The stage checked the cell honestly and
declined it, because neither leg qualifies. No forced transition narrative.

### 2.5 Block conformance

| # | Rule | Check | Verdict |
|---|---|---|---|
| E29 | B07 YAML schema complete | All fields present: `input_gaps`, `flags`, `em_score`, `em_classification`, `active_categories`, `evidence_mix`, `completionist_recount`, `catalysts_12m`, `capex_embedded_growth_pct`, `optionality_register`, `combined_assessment`, `combined_reasoning`, `top_moat_risks`, `analyst_note` | PASS |
| E30 | `active_categories` carries only Strong/Moderate rows | Empty. Zero rows reached Strong or Moderate, so empty is correct, and the four WEAK rows were correctly excluded rather than promoted to fill the field | PASS |
| E31 | `evidence_mix` internally consistent with the report body | documented: 6 matches the recount. claim: 5 understates the 🎙️ items actually tagged. See finding C-03 | **FAIL (MINOR)** |
| E32 | `em_classification` uses the schema enum | "NONE" is a valid enum value for the <12 band | PASS |
| E33 | `analyst_note` ≤200 words | About 120 words | PASS |
| E34 | Block YAML matches the report's terminal YAML | One text difference beyond the disclosed brace repair. See finding C-04 | **FAIL (MINOR)** |

**Emerging Moat result: 34 rules checked, 30 passed, 4 fails, all MINOR.**

---

## PART 3 — FINDINGS

| ID | Severity | Location | Finding | Recomputed / correct value |
|---|---|---|---|---|
| C-01 | MINOR | B07 report Section 2C; block `capex_embedded_growth_pct: 0` | Section 2C mandates "total capex under execution × historical fixed asset turnover = implied incremental revenue; show the arithmetic". The stage declined to compute it and wrote a prose justification (PP&E ~6% of standalone assets, equipment rented, the assets that matter are SPV equity). The justification is sound and rests on the framework's own never-force-fit rule, but the arithmetic was available and the block now carries a numeric 0 that means "not applicable", which a downstream consumer will read as a measured zero | On CWIP under execution (Rs3.58cr FY26) × FAT 11.79x = ~Rs42cr = **~1.0%** of FY26 revenue. On FY27 guided capex (Rs30-35cr) × 11.79x = ~Rs354-413cr = **~9-10%**. Both immaterial; no decision impact |
| C-02 | MINOR | B07 report L132 | The recount line says 4 categories is "below the completionist guard's stated base rate of 3-6 categories". Four sits inside 3-6, not below it. The scan is genuinely sparse on strength (zero Strong/Moderate rows), but the count itself is within the framework's stated base rate | Correct statement: 4 categories carry evidence, inside the 3-6 base rate; zero reach Strong or Moderate |
| C-03 | MINOR | B07 block `evidence_mix: {documented: 6, claim: 5, inference: 2}` | The 🎙️ count understates the report body. Distinct management claims tagged 🎙️ include the renewables EBITDA-parity claim, the 20-25% of FY27 revenue guide, the Romania/Dubai bids, "equity is not a problem", the AI/data-tools exploration, the MoRTH monthly-billing WC claim, and the bid-norms-favour-Ceigall claim. That is at least 7, not 5. `documented: 6` reconciles cleanly to the recount; the claim leg does not | claim: ≥7 on the items tagged in the report body. No score impact; `evidence_mix` does not feed em_score |
| C-04 | MINOR | B07 block L15 vs report L245 | The orchestrator repair is disclosed as a single added closing brace with nothing else altered. A second change exists: in the FLAG-EMOAT-NETTED reason string, the report's "tunnel/elevated-corridor progress, all 📄)" appears in the block as "tunnel/elevated-corridor progress, all documented)". Semantically identical, so no judgement changed, but the repair note's claim that "no word was altered" is not exact. Attributable to the orchestrator, not to stage 7 | Block should read "all 📄)" to match the stage's emitted text, or the repair note should record the glyph substitution |
| C-05 | MINOR (advisory) | B01 M3 | The M3 rule states "FAT >3x AND ROCE >20% = 5 \| FAT >2x AND ROCE >15% = 3" without naming the ROCE basis, unlike A1 ("Median"), A2 ("Minimum single-year") and D1 ("latest"). The stage used FY26 ROCE (16.76%) and scored 3, stating the basis. On median ROCE (22.72%) with the same FAT (11.79x), M3 would score 5. The stage's reading is defensible and disclosed, so the rule is scored as applied, but the operator should know a second defensible reading exists | On a median-ROCE basis: M3 = 5, Block F = 10/60, grand total = 47/160. `moats_confirmed` stays 2 (M3 is ≥3 either way), `moat_class` stays MODERATE, `core_score` stays 37, classification stays AVOID. **No decision impact** |

No CRITICAL findings. No MAJOR findings.

### Observations, no severity attached

- **O-01, deferred to Verifier A.** Small rounding drift on non-scoring figures:
  ROE FY22 (stage 34.17%, mine 34.18%), PAT CAGR (stage 22.63%, mine 22.62%),
  receivable days FY22/FY24/FY25/FY26 each ~0.01-0.03 days high, inventory days
  FY21 0.01 high. Every one is band-neutral. Numbers are Verifier A's authority,
  not mine; recorded here only so the hand-off is complete.
- **O-02, M11 window.** The rule says the two-window test needs ≥6 years, else
  score conservatively on the overall trend "and state so". Six annual points give
  only five growth periods, so a clean 3-and-3 split is impossible. The stage used
  FY21→FY23 against FY24→FY26 and stated the windows. On the alternative split
  (latest 3 periods FY23→FY26 = 24.83% against prior FY21→FY23 = 53.90%) the top
  band still fails and selling % is still rising, so M11 = 1 either way. Outcome
  invariant, which is why this is an observation and not a finding.
- **O-03, E1 and the optionality register.** E1 scored on a 🔍 multiplier but is
  not carried in the register. The register rule covers rows that "scored 0 or rest
  only on 🎙️/🔍 evidence". E1's underlying LOAs are 📄, so exclusion is defensible.
  Borderline, no action needed.
- **O-04, input count.** The stage prompt specifies 3 main concalls; the report
  header records four transcripts consumed (Nov-2025, Feb-2026, May-2026,
  Aug-2026). More evidence, not less. Worth noting only because the F2 netting
  cites "silence across three calls" from the B05 record while the scan itself read
  four.

### On the two things the task flagged in advance

**Block E scoring 0 on a missing shareholding filing.** Correct under the framework.
Operating rule 5 says an unavailable data point is marked N/A and scored 0, with no
gap-filling. Block E therefore enters `core_score` as 0, which is what drags Core to
37 and fires the Core <40 AVOID cell. The stage did not soften the score, and it did
not let the score masquerade as a governance finding. The evidence-gap label appears
in `flags`, `data_notes`, `analyst_note`, the weakest-block line and the decision
line. That is the framework applied as written, plus the disclosure the operator
needs to re-score it when the filing lands.

**Moat tests scoring 0 for PEER DATA NEEDED or non-applicability.** Also correct.
Block F's own text mandates a 0 with the "PEER DATA NEEDED" mark when peer data is
absent, and forbids guessing peer figures. M2, M5, M7 and M9 are marked exactly that
way; M6 and M8 fall to their rules' else-branches for an EPC contractor and would
score 0 on any reading. The stage recorded in `data_notes` which zeros are
unconfirmed versus which are genuine absences. The moat read is unconfirmed, not
disproven, and the artifact says so.

Neither of these is a framework failure. Both are the framework doing what it is
built to do on a gapped corpus.

---

## PART 4 — VERDICT

| Audit | Rules checked | Passed | Fails |
|---|---|---|---|
| Gate 0 (B01) | 51 | 51 | 0 |
| Emerging Moat (B07) | 34 | 30 | 4 (all MINOR) |
| Valuation (B11) | 0 | — | pending phase 3 |
| **Total** | **85** | **81** | **4** |

**framework_adherence: 95%** (81 ÷ 85 rules passed).

The checks that produced that percentage are the 51 Gate 0 rules in Part 1 (G01-G51:
operating rules and formula definitions, every one of the 20 core line-item
thresholds re-derived from the CSV, all 12 moat tests, both block totals and the
core total, the data-confidence band, the classification matrix, all nine
deal-breakers, and output/block conformance) and the 34 Emerging Moat rules in
Part 2 (E01-E34: six-section structure, category completeness, evidence taxonomy and
anchoring, the completionist guard, the full likelihood × impact and multiplier
re-derivation, the classification band, Categories 21 and 22 under Verifier C rule 8,
the optionality register, all five Section 6 sub-parts, and block conformance).

Concurrence:
- I concur with Gate 0 classification **AVOID** (Core 37/100, moat MODERATE).
- I concur with the emerging-moat score **4.3** and classification **NONE**.
- I concur with the combined assessment **AVOID**.
- `recomputed_destination_pe`: not applicable in phase 1.
- No REWORK trigger. No CRITICAL from any verifier rule I ran, and acceptance rate
  is well above the 60% floor.

One closing note on where the risk actually sits in these two artifacts. Both stages
scored a gapped corpus, and both had obvious room to soften a zero: Block E on a
missing filing, five moat tests on missing peers, I1 on a genuinely impressive set
of senior hires, F2 on a real early-completion bonus record. Neither took the room.
Every deviation I found runs conservative. The four fails are bookkeeping (an
uncomputed but immaterial 2C figure, a misquoted base rate, an understated claim
count, an under-disclosed repair), not scoring failures. The scores in these two
blocks can be relied on downstream as applied.

---

```yaml
stage: B12c
company: "CEIGALL"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
scope: "phase-1 only: Gate 0 (B01) + Emerging Moat (B07). Valuation audit deferred to phase 3."
gate0: {rules_checked: 51, fails: []}
emoat:
  rules_checked: 34
  fails:
    - "E04: Section 2C capex-embedded-growth arithmetic not shown; capex_embedded_growth_pct reported as 0 meaning not-applicable"
    - "E11: completionist recount line states 4 categories is 'below' the 3-6 base rate; 4 is inside it"
    - "E31: evidence_mix claim count (5) understates the >=7 management-claim items tagged in the report body"
    - "E34: block YAML differs from report YAML beyond the disclosed brace repair ('all 📄' -> 'all documented')"
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # NOT ASSESSED - stage 13 runs after phase 1; empty fails, no REWORK implied
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MINOR, location: "B07 Section 2C / capex_embedded_growth_pct", finding: "Mandated capex x FAT arithmetic not shown; justified as force-fit avoidance but block carries numeric 0 for not-applicable", recomputed: "~1.0% on CWIP basis (Rs3.58cr x 11.79x); ~9-10% on FY27 guided capex Rs30-35cr; no decision impact"}
  - {severity: MINOR, location: "B07 report L132 recount line", finding: "States 4 categories is below the 3-6 completionist base rate; 4 sits inside 3-6", recomputed: "4 categories with evidence, inside base rate; 0 reach Strong/Moderate"}
  - {severity: MINOR, location: "B07 block evidence_mix", finding: "claim: 5 understates the management-claim items tagged in the report body (>=7 distinct)", recomputed: "claim >=7; documented: 6 reconciles correctly to the recount"}
  - {severity: MINOR, location: "B07 block flags[1] vs report YAML", finding: "Orchestrator repair altered '📄' to 'documented' in the FLAG-EMOAT-NETTED reason, beyond the disclosed single closing brace; no judgement changed", recomputed: "orchestrator-attributable, not stage 7"}
  - {severity: MINOR, location: "B01 Block F M3", finding: "ADVISORY. M3 rule does not name the ROCE basis; stage used FY26 (16.76%) and scored 3, stating the basis. Median ROCE (22.72%) would score 5", recomputed: "M3=5 -> Block F 10/60, grand total 47/160; moats_confirmed 2, moat_class MODERATE, core 37, classification AVOID all unchanged"}
gate0_concur: "AVOID (Core 37/100, moat 8/60 MODERATE, 2 moats confirmed) - all 51 rules re-derived from screener-Data_Sheet.csv, no fails"
emoat_concur: "em_score 4.3/92, NONE, combined AVOID - likelihood x impact and evidence multipliers re-derived, all correct; evidence-tier discipline conservative throughout, no 🎙️-as-📄 credit found"
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 95             # 81 of 85 rules passed (51/51 gate0 + 30/34 emoat)
```
