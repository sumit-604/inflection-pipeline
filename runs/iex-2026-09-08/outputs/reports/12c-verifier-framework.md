# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE
## Indian Energy Exchange Ltd (IEX) — run 2026-09-08 — PHASE 1 SCOPE

Auditor: independent, fresh context, artifact paths only. I did not see the
reasoning that produced B01 or B07.

**Scope.** Phase 1 only: Gate 0 (B01) and Emerging Moat (B07). The valuation
audit (B10/B11) does not run here. Stages 10 and 11 have not run and the
valuation framework documents were deliberately not supplied. The valuation
section of my block is marked `pending phase 3`, as are the expectation-ledger
and business-understanding-narrative sections, which key to stages 11 and 13.

**Rule sources used.**
- `prompts/01-gate-0-pipeline.md`
- `prompts/07-emerging-moat-pipeline.md`

**Artifacts audited.**
- `runs/iex-2026-09-08/outputs/blocks/B01-gate0.yaml`
- `runs/iex-2026-09-08/outputs/reports/01-gate0.md`
- `runs/iex-2026-09-08/outputs/blocks/B07-emoat.yaml`
- `runs/iex-2026-09-08/outputs/reports/07-emoat.md`

**Corroborating reads.** I opened three input CSVs to test two rule questions
that cannot be settled from the reports alone (see Rules G-5 and B2/B3 below):
`inputs/screening/screener-Data_Sheet.csv`, `inputs/screening/screener-Balance_Sheet.csv`,
`inputs/screening/screener-Cash_Flow.csv`. I did not audit source fidelity of
individual numbers. That is Verifier A's sole and non-overridable authority.

**Headline.** No CRITICAL. Two MAJOR, both non-decision-changing on
recomputation. Gate 0 classification EXCELLENT survives. Emerging Moat
classification MOAT STRENGTHENING survives, and so does the `EM >= 25` UA
qualifier that stage 11 will consume. Acceptance rate 84%.

---

# PART 1 — GATE 0 (B01) COMPLIANCE

## 1.1 Operating and formula rules

| # | Rule (prompts/01) | Verdict | Note |
|---|---|---|---|
| G-1 | Entire scorecard in one response, no stops | PASS | All five core blocks plus Block F scored. |
| G-2 | Opens with "Data available: X years (FY__ to FY__)" | PASS | "Data available: 8 years (FY19 to FY26)... Scoring adapted to 8-year history." |
| G-3 | Source anchor on every extracted number | PASS (MINOR) | Broadly excellent. One gap: the M5 market-cap line quotes four mcaps with no per-figure anchor. |
| G-4 | Grounded claims; unavailable data marked N/A and scored 0; never fill gaps | FAIL | One breach at E2. See 1.3. |
| G-5 | ROCE: use the source's own ROCE if provided; compute only when absent and state "computed" | PASS (MINOR) | I verified the branch. `screener-Balance_Sheet.csv` lines 18-19 carry "Return on Equity" and "Return on Capital Emp" as **label-only rows with no values**, and `screener-Data_Sheet.csv` carries no ROCE row and no Total Assets row. The source ROCE is genuinely absent, so computing is the correct branch. The report shows the full arithmetic and anchors capital employed to the audited AR balance sheets, but never uses the literal word "computed". Substance exceeds the label; the label is missing. |
| G-6 | ROE = PAT / average net worth; state where opening NW is unavailable | PASS | FY19 explicitly flagged "closing NW only, opening unavailable". |
| G-7 | WC Days = Recv + Inv − Pay, revenue basis unless COGS explicit; state the basis | PASS | Revenue basis stated. Inventory taken as 0 — correct, IEX holds no inventory; this is a real zero, not an absent-data zero. |
| G-8 | FCF = CFO − capex (PPE + intangibles, exclude acquisitions) | PASS | Capex taken from the audited AR cash-flow statements, PPE + intangibles, acquisitions not present. |
| G-9 | CAGR = (End/Start)^(1/years) − 1 | PASS | FY19 to FY26 correctly treated as 7 periods, not 8. |
| G-10 | CAGR edge rules (N/M on negative endpoint, loss-to-profit note, C4=0 when PAT CAGR N/M) | PASS | Correctly **not** invoked: every endpoint is positive, no loss-to-profit swing exists, so C4 scores normally. The rules were honoured by non-application. |

**Note on the mixed scoring windows.** Block C and B1 use the full 8-year
Data_Sheet window; A1/A2/A4, B2/B3, B4 and M12 use FY24-FY26 only. I tested
whether this is an unforced narrowing. It is not. `screener-Data_Sheet.csv`
carries no Total Assets row (so capital employed is not derivable pre-FY24) and
carries only "Cash from Investing Activity" with no separated purchase-of-PPE
line (so capex is not derivable pre-FY24). The prompt's "use whatever history is
available: minimum 3 years" is satisfied at 3 years, and every affected line is
flagged in the report. PASS.

## 1.2 Block-by-block re-derivation

I recomputed every metric from the inputs stated in the report.

**Block A — 20/20. Re-derived: 20.**

| Metric | Report input | My re-derivation | Band | Score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 45.88 / 47.66 / 45.71 | median = 45.88% | >=25 → 5 | 5 | PASS |
| A2 Min single-year ROCE | min = 45.71% (FY26) | 45.71% | >=15 → 5 | 5 | PASS |
| A3 Median ROE | 8 values FY19-FY26 | sorted 4th/5th = (40.72+44.58)/2 = 42.65% | >=20 → 5 | 5 | PASS |
| A4 ROCE trend | FY26 45.71 vs FY24 45.88 | decline of 0.16pp | see below | 5 | **FAIL (MINOR)** |

**A4 is the one Block A defect.** The rubric reads: `latest >= earliest = 5 |
decline 1-3pp = 3 | decline 3-5pp = 1 | decline >5pp = 0`. 45.71 is not >= 45.88,
so the top band's stated condition is literally false. A 0.16pp decline also
falls below the smallest defined decline band. The rubric has a genuine gap at
declines under 1pp, and the stage chose the top band, showed the raw 0.16pp
figure, and explicitly invited a verifier to rescore at band 3. That disclosure
is why this is MINOR and not MAJOR. **Recomputed at band 3: A4 = 3, Block A = 18,
core = 83, still >=80, classification EXCELLENT unchanged.**

**Block B — 18/20. Re-derived: 18.**

| Metric | My re-derivation | Band | Score | Verdict |
|---|---|---|---|---|
| B1 Cum CFO / Cum PAT | 2,468.83 / 2,434.87 = 1.0139 (both sums re-added term by term, both tie) | >=1.00 → 5 | 5 | PASS |
| B2 FCF-positive years | 3 of 3 = 100% | 100% → 5 | 5 | PASS |
| B3 Cum FCF / Cum PAT | 1,120.55 / 1,272.87 = 0.8804 | >=0.60 → 5 | 5 | PASS |
| B4 WC days change | FY24 −1.46 (0.64 − 2.10), FY26 −1.61 (1.17 − 2.78); change = 0.15 days more negative | within ±5 → 3 | 3 | PASS |

All four day-count computations reproduce to two decimals. B4 is correctly
scored 3 and not 5: the rubric's 5-band needs a decrease **greater than 5 days**,
and a 0.15-day move is inside the ±5 band. The stage did not reach for the
higher band. Correct.

**Block C — 15/20. Re-derived: 15.**

| Metric | My re-derivation | Band | Score | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | (615.65/254.08)^(1/7) − 1 = 13.48% | 10-14.9 → 3 | 3 | PASS |
| C2 PAT CAGR | (492.92/165.04)^(1/7) − 1 = 16.92% | 15-19.9 → 4 | 4 | PASS |
| C3 Positive YoY years | 6 of 7 = 85.7% | 75-99 → 3 | 3 | PASS |
| C4 PAT less Revenue CAGR | 16.92 − 13.48 = +3.44pp | >=+3 → 5 | 5 | PASS |

C4 sits 0.44pp inside the top band. I recomputed both CAGRs independently to
four decimals before accepting it; the margin is real, not a rounding artifact.

**Block D — 19/20. Re-derived: 19.**

| Metric | My re-derivation | Band | Score | Verdict |
|---|---|---|---|---|
| D1 Net debt / EBITDA | 11.16 − 2,098.28 = −2,087.12, net cash | net cash → 5 | 5 | PASS |
| D2 Interest coverage | 647.84 / 2.28 = 284x | >=10 → 5 | 5 | PASS |
| D3 Debt / Equity | 11.16 / 1,364.56 = 0.0082 | <0.1 → 5 | 5 | PASS |
| D4 Current ratio | 203,222.96 / 101,852.98 = 1.9953 | 1.5-1.99 → 4 | 4 | PASS |

D4 is the discipline test in this block and the stage passed it: 1.9953 is
0.0047 short of the 2.0 threshold and was **not** rounded up. Correct.

The Banks/NBFC/Insurance carve-outs in D1/D2/D3 were correctly not invoked. IEX
is a market-infrastructure company, not a lender, and the report scores it on the
general bands.

**Block E — 13/20. Re-derived: 10. One MAJOR.**

| Metric | My re-derivation | Band | Reported | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 0.00%; carve-out tested at FII+DII = 44.10% | <30 → 0; carve-out needs >50% | 0 | PASS |
| E2 Promoter holding change over 3 years | 3-year window NOT FOUND in corpus; 1-year window used | see below | 3 | **FAIL (MAJOR)** |
| E3 Promoter pledge | 0% across 5 filings | 0% → 5 | 5 | PASS |
| E4 Contingent liab / net worth | 5.0376 / 1,364.56 = 0.369% | <5 → 5 | 5 | PASS |

**E1 = 0 is a correct application, not a data-absence penalty.** This was one of
the not-applicable judgements I was asked to rule on. The prompt provides two
routes and the stage walked both. Route one: the band table ends at `<30 = 0`,
and 0.00% is below 30. Route two: the prompt's own escape hatch,
"Professionally managed: 3 if FII+DII >50%", was tested and fails at 44.10%. The
prompt anticipated exactly this company type and set a threshold IEX does not
clear. The stage applied the rule as written and flagged the zero as mechanical
rather than a governance signal. **PERMITTED.**

**E2 = 3 is the MAJOR.** The metric is defined as "Promoter holding change over
3 years". The report states plainly that the corpus holds five shareholding
filings spanning 30-Jun-2025 to 30-Jun-2026, that this is "a **1-year window, not
the 3-year window the metric calls for**", and that "the full 3-year comparison
is NOT FOUND in this run's corpus". Operating rule 5 then binds: "If a data point
is not available, mark it 'N/A (not in provided data)' and **score it 0**." The
stage instead scored 3 on the 1-year window, bridged by an inference that a
3-year comparison "would almost certainly also read flat at 0.00%". The report
even names the problem, writing that the promoter-less status since 2017 is
"noted as context, not substituted as evidence" — and then substitutes it. The
counter-argument is real: with no promoter category in existence, the change is
definitionally zero. But the prompt does not grant a definitional exemption, and
the structural claim carries no filed anchor inside the required window.
**Recomputed: E2 = 0, Block E = 10, core = 82.**

**Block F, moats — 30/60. Re-derived: 30.**

| Test | My check | Score | Verdict |
|---|---|---|---|
| M1 Pricing power | +4.62pp margin (>=2pp) and 13.48% CAGR (>=10%) | 5 | PASS |
| M2 Cost advantage | Peer margins recomputed from each Data_Sheet: MCX 71.31%, BSE 67.92%, CDSL 50.84%; median 67.92%; IEX 84.47% = +16.55pp | 5 | PASS |
| M3 Capital efficiency | FAT 6.37x (>3x) and ROCE 45.7% (>20%) | 5 | PASS |
| M4 Customer stickiness | 1 decline year fully recovered; receivable days not stable ±10, so the 5-band correctly fails | 3 | PASS |
| M5 Scale and dominance | 4th of 4 by mcap → "top 5 mcap" band | 1 | PASS (MINOR obs) |
| M6 Technology / R&D | No R&D line disclosed → rubric's "else 0" and rule 5 both give 0 | 0 | PASS |
| M7 Regulatory / licence | 3 named exchanges (<=5, so also <=10); margin +4.62pp fails ±3pp, clears ±5pp → 3-band | 3 | PASS |
| M8 Distribution | Rubric names "none or **purely digital** = 0" explicitly | 0 | PASS |
| M9 Brand | See ruling below | 0 | PASS |
| M10 Switching costs | Growth in all but FY23 disqualifies the 5-band regardless of the favourable receivable-day fall | 3 | PASS |
| M11 Network effects | Latest 3yr 15.38% vs prior 3yr 15.95%; all three bands fail literally | 0 | PASS |
| M12 Negative WC / float | Negative in 3 of 3 years | 5 | PASS |

Sum: 5+5+5+3+1+0+3+0+0+3+0+5 = **30**. Ties.

**M9 = 0 is a correct treatment, and it survives both routes.** This was the
second not-applicable judgement I was asked to rule on. The rubric's fixed GM
proxy is `(Revenue − Material Cost) / Revenue`. Neither IEX nor any of MCX, BSE
or CDSL discloses a material or COGS line. Route one, the prompt's Block F
instruction: "If a test needs peer data that is not provided, score 0" — peer
data **is** now provided, so the stage correctly removed the PEER DATA NEEDED
marker and re-labelled the zero as structural. Route two, the literal rubric: if
material cost is nil for all four names, every GM is 100%, IEX sits **at** the
peer median, and the rubric's bottom band is "at/below = 0". Both routes land on
0. The stage stated the proxy used, stated why it is not computable, and did not
guess a figure. **PERMITTED.** The distinction the stage drew — structural
absence of a cost category, not a collection failure — is the honest one and it
is correctly recorded in `data_notes`.

**M5 = 1, one observation.** The literal application is right: 4th of 4 is inside
"top 5 mcap". The stage flagged the small-n artifact itself and noted that
management claims 80-85% share within power exchanges specifically. Read against
that narrower segment, IEX is largest by mcap and top by margin, which is the
5-band. The stage chose the conservative reading tied to the supplied comparison
set. **Recomputed at the narrow-segment reading: M5 = 5, moat = 34,
moats_confirmed = 8, still FORTRESS, grand 119, classification unchanged.** The
conservative choice costs nothing and is disclosed. Not a fail.

**M11 = 0 deserves a sentence.** Every band fails on a literal read, including
the 1-band, which requires selling expense **rising** while IEX's is falling. The
company is penalised for a favourable trend by a rubric artifact. The stage
applied the rule as written and said so. That is correct behaviour for a
compliance audit: the rubric is the authority, and the stage flagged the
near-miss rather than reaching for a score.

## 1.3 Classification, confidence, deal-breakers

| Rule | Check | Verdict |
|---|---|---|
| Block sums | A 20 + B 18 + C 15 + D 19 + E 13 = **core 85**; moat 30; grand **115**. All tie. | PASS |
| Moat classification | 7 tests at >=3 (M1, M2, M3, M4, M7, M10, M12). M5 at 1 correctly excluded. 6+ → **FORTRESS**. | PASS |
| Data confidence | 8 years → the "7-9 moderate" band. No downgrade tier applies (downgrade needs 3-4 years). | PASS |
| Classification matrix | Core 85 in the >=80 band + FORTRESS → **EXCELLENT**. | PASS |
| Deal-breakers 1-9 | I re-tested all nine: A=20 not <8; B=18 not <8; median ROCE 45.88% not <10%; CFO/PAT 1.014 not <0.50; pledge 0% not >15%; net cash so the ND/EBITDA-and-IC conjunction cannot fire; revenue declined 1 of 7 years, not a majority; PAT positive FY24/FY25/FY26; 8 years not <3. **None triggered.** | PASS |
| `flags[]` empty | The prompt requires a FLAG-GATE0 entry only when classification is <= AVERAGE. Classification is EXCELLENT. Empty is correct. | PASS |
| `history_downgrade: false` | Consistent with the 8-year window. | PASS |
| `data_notes` carries proxy bases and PEER DATA NEEDED items | Present, and correctly records that no PEER DATA NEEDED item survives. | PASS |
| `block_b_trend` with one number | "stable - cumulative FCF/PAT 0.8804..." | PASS |
| `analyst_note` <= 200 words | ~162 words. | PASS |

**Data-confidence observation, not a fail.** ROCE, FCF and WC-days rest on a
3-year sub-window while the headline confidence reads off the 8-year P&L window.
Had 3 years governed the whole-run confidence, the prompt's "3-4 LIMITED,
downgrade classification one tier" would have taken EXCELLENT to GOOD+. I do not
read the prompt that way: the confidence ladder keys off history available, which
is 8 years, and the sub-window is flagged at every affected line. Recording it so
the operator can see the sensitivity.

## 1.4 Run-2 specific checks

The block is a rescore. Run 1 scored 99/160 without the annual report and without
peer data; run 2 scores 115/160 with both. I checked that the deltas are new
evidence rather than re-readings of the same evidence.

| Delta | Driver | Legitimate? |
|---|---|---|
| A 18 → 20 | FY24 comparative balance sheet in Annual_Report_2025.txt extended the ROCE window from 2 years to 3, changing A4's earliest-year comparator | Yes. New source. |
| B 15 → 18 | B4 computable for the first time on the same new FY24 comparative | Yes. New source. |
| E 8 → 13 | E4 moved from NOT FOUND to 0.369% on AR Note 39/38 | Yes. New source. |
| F 24 → 30 | M2 scored 5 on newly supplied peer Data_Sheets | Yes. New source. |
| C, D unchanged | No new P&L history | Consistent. |

The `run_note` and the two CLOSED `input_gaps` entries state the supersession
explicitly. Dependency alignment holds: `moats_confirmed` moved 6 → 7 in step
with M2, the dashboard's Run 1 column reconciles to 99, and the analyst_note
carries the tier change. No stale run-1 figure survives in the run-2 artifact.
PASS.

## 1.5 Two presentational defects

- **The report does not end with the fenced YAML block.** The prompt's OUTPUT
  section says "Then end with exactly this fenced YAML block". `01-gate0.md` ends
  at DATA NOTES. The block exists only as `blocks/B01-gate0.yaml`. Note the
  inconsistency inside this same run: `07-emoat.md` **does** carry its fenced
  block at the end. MINOR.
- **YAML schema extras.** `run_number` and `run_note` are not in the prompt's
  schema, and `input_gaps` is a list of typed objects where the schema shows a
  bare list. Both are additive and informative for a rescore. MINOR.

---

# PART 2 — EMERGING MOAT (B07) COMPLIANCE

## 2.1 Structural rules

| # | Rule (prompts/07) | Verdict |
|---|---|---|
| E-1 | All six sections in one response | PASS. Sections 1-6 plus the Optionality Register, all present, in order. |
| E-2 | Evidence taxonomy on every item | PASS. 📄/🎙️/🔍 applied throughout. |
| E-3 | Source anchors in the (AR p.__) / (Q_ FY__ call) / (slide __) form | **FAIL (MINOR).** Several anchors are extracted-text line numbers, not pages: "AR line 11332" (A2), "AR line 4363" (Section 2), "AR lines 4678-4711" (F1). All three sit in NO-EVIDENCE categories, so materiality is low, but the anchor form is not the one the prompt specifies and a downstream reader cannot resolve a line number to a page. |
| E-4 | Skepticism; hard evidence over promises | PASS, and conspicuously so. The 🎙️ tag is applied to management's own framing repeatedly ("well positioned", the BESS 80% claim), and the B05 credibility grade C is carried into the scan's own risk list. |
| E-5 | "NO EVIDENCE FOUND" stated, never force-fit | PASS. Ten categories carry it with a reason. |
| E-6 | Completionist guard: recount performed and stated | PASS on performance, **FAIL (MINOR) on arithmetic.** See 2.4. |
| E-7 | All 23 categories addressed | PASS. The Section 3 summary table carries 23 rows: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1. |
| E-8 | Section 5 scoring table "all 23 rows" | **FAIL (MINOR).** The table lists 14 scored rows plus one collapsed "All other categories (0 evidence)" line. Every category's score is unambiguous and the total is unaffected, but the table is not the 23-row table the prompt asks for. |
| E-17 | Bands absolute, ceiling 92, no rescale | PASS. Stated in Section 5 verbatim. |
| E-21 | Optionality register, four columns, registered items watched never scored | PASS. Nine rows, all four columns populated. I verified the non-scoring rule holds: A4 states the pending tranche (Green RTM, Peak, 11-month TAM) is "carried in the optionality register, **not scored here**", and none of the three appears in the scoring table. |
| E-27 | analyst_note <= 200 words | PASS. ~75 words. |
| E-28 | YAML block at report end, schema complete | PASS. |

## 2.2 Scorecard re-derivation

Raw matrix per prompt: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.
Multipliers per prompt: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x.

| Cat | Stated L x I | Raw | Matrix check | Stated mult | Mult check | Adjusted |
|---|---|---|---|---|---|---|
| A3 | LL | 1 | correct | 0.7 🎙️ | correct | 0.7 |
| A4 | HM | 3 | correct | 1.0 📄 | correct | 3.0 |
| B3 | MH | 3 | correct | **0.85 "Blend"** | **not a permitted value** | 2.55 |
| C1 | HM | 3 | correct | 1.0 📄 | correct | 3.0 |
| C2 | "H x L/M (MM)" | 2 | value correct, **label inconsistent** | 1.0 📄 | **tier mismatch** | 2.0 |
| D1 | LM | 1 | correct | 0.5 🔍 | correct | 0.5 |
| D2 | HH | 4 | correct | **0.85 "Blend"** | **not a permitted value** | 3.4 |
| E1 | HM | 3 | correct | 1.0 📄 | correct | 3.0 |
| G1 | HM | 3 | correct | 1.0 📄 | correct | 3.0 |
| H1 | MH | 3 | correct | **0.85 "Blend"** | **not a permitted value** | 2.55 |
| H2 | LL | 1 | correct | 0.7 🎙️ | correct | 0.7 |
| I1 | — | 0 | correct | — | — | 0 |
| I2 | — | 0 | correct | — | — | 0 |
| R1 | HH | 4 | correct | 1.0 📄 | correct | 4.0 |

**Arithmetic ties exactly.** My sum: 0.7 + 3.0 + 2.55 + 3.0 + 2.0 + 0.5 + 3.4 +
3.0 + 3.0 + 2.55 + 0.7 + 0 + 0 + 4.0 = **28.40 → 28**. Reported 28.4 → 28. PASS.

Every raw score conforms to the likelihood-impact matrix. The one label defect:
C2 is written "H x L/M" but bracketed "(MM)". The assigned raw of 2 is correct
under either HL or MM, so no score moves, but the two labels contradict each
other. MINOR.

## 2.3 The two MAJOR findings

**MAJOR-1: an unauthorised evidence multiplier.** The prompt defines exactly
three multipliers: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x. It defines no blend rule. The
scorecard applies **0.85** to B3, D2 and H1. The value is transparently labelled
"Blend", so this is disclosed invention rather than concealment, but 0.85 is not
a value the framework grants.

I recomputed both bounds. Taking the weaker tier for all three blended rows
(0.7x, the reading the prompt's own scepticism rule 4 points to, since the
load-bearing leg of B3 and H1 is management's claim to capture the Coal Exchange
licence): B3 2.10, D2 2.80, H1 2.10, total **26.9 → 27**. Taking the stronger
tier (1.0x): B3 3.00, D2 4.00, H1 3.00, total **29.9 → 30**. The band 25-39 holds
across the whole range, so **MOAT STRENGTHENING survives** and the `EM >= 25` UA
qualifier that stage 11 will consume survives with 1.9 points of headroom at the
strict bound. Decision unchanged. MAJOR, not CRITICAL.

**MAJOR-2: an evidence-tier mismatch on C2.** Verifier C rule 3 names this
failure mode directly: "a 🎙️-only category scoring as if 📄 is a finding." C2 is
"Customer concentration **improving** / base diversification" — the scored
proposition is a direction of travel. The report's own text concedes the
direction is not documented: "No multi-year participant-count trend is disclosed
in this corpus (single data point), so the DIRECTION is claimed rather than shown
across years — evidence is 📄 for the current count, **🎙️/implicit for the
'continues to grow and diversify' framing**." The row is nonetheless scored at
1.0x. The documented leg supports a static participant count, not the
improvement the category scores. At 0.7x, C2 = 1.4, a 0.6-point reduction.

**Combined worst case across both MAJORs:** 28.4 − 1.5 − 0.6 = **26.3 → 26**.
Still >= 25. Still MOAT STRENGTHENING. Still clears the UA qualifier. No
downstream input flips.

## 2.4 The completionist recount

The prompt's guard triggers at 12+ active categories. This scan has 9, below the
trigger, and the stage performed the recount anyway and stated the mandated line.
That is the right instinct. The arithmetic inside it does not hold.

The itemisation reads: A4:2, B3:2, C1:3, C2:1, D2:2, E1:5, G1:3, H1:2 = **20
unique documented items across 8 categories**. The line then adds "plus R1's VPPA
Gazette notification counted once against A4 to avoid double-counting" and
reports the total as **21 across 8 categories**. If the R1 item is the same VPPA
notification already counted inside A4's two, it cannot also be a 21st item. The
stated total double-counts the very item the clause says it is not
double-counting. Either the total is 20 across 8 categories, or it is 21 across
9. It cannot be 21 across 8.

`evidence_mix.documented: 21` inherits the same figure. Neither the scores, the
adjusted total, nor the classification depend on it. MINOR, but it sits inside a
framework-mandated control, so I am recording it rather than waving it through.

A second tally slip in the same paragraph: "10 score None/0 (A1, A2, B1, B2, E2,
F1, F2, G2, H3, I1, I2)" lists **11** categories. The list is right and the count
is wrong: 9 active + 3 weak + 11 zero = 23, which is the correct category total.
Written as "10", the paragraph sums to 22. MINOR.

## 2.5 Categories 21 and 22, and the F2 zero

| Rule | Check | Verdict |
|---|---|---|
| Cat 21 (I1) present | Present, scored 0 | PASS |
| I1 above 0 only if both legs evidenced with a 📄 (b) leg | Scored 0. The report checks both legs by name — no named inventors, no ex-DRDO/ex-PSU concentration, no remuneration-annexure evidence — and cites the operator ruling that I1/I2 score 0 for typical companies. | PASS |
| Cat 22 (I2) present | Present, scored 0 | PASS |
| I2 above 0 only if the named sacrifice is specific | Scored 0, with the test actually run rather than skipped. The report walks two candidate sacrifices and rejects both: a rival exchange would face an execution lead, not a configuration sacrifice; and Coal India's forced e-auction exit is regulator-imposed, not a sacrifice IEX's model forces on a moat-mirror competitor. It lands on the prompt's own words, "nothing must be destroyed", and scores 0. | PASS |
| I1/I2 contribution stated separately | "I1/I2 contribution: 0 of 28 (0%)... there is no threshold crossing to flag for the operator's review checkpoint." | PASS |

**F2 = 0 as a deliberate negative finding: PERMITTED.** This was the third
judgement I was asked to rule on. Three things make it compliant. First, the
prompt's own F2 definition instructs the stage to "cross-reference the injected
concall promise-delivery record", which is precisely what produced the finding
(B05 grade C, 8 promises, 2 delivered, 3 partial, 3 missed). Second, the scoring
matrix has no negative values; its floor is 0, so an adverse execution record and
an absent execution record necessarily collapse to the same number. Third, and
this is what separates a correct negative from a lazy zero, the stage did not let
the finding vanish into that shared zero. It labelled the summary row "Yes
(negative)", distinguishing it from the ten "No" rows; it raised the finding to
`flags[]`; it carried it into `top_moat_risks`; and it used it as a global
scepticism weight on every 🎙️ item in the scan. The information survives the
floor. That is the right handling of a scale that cannot express what the
evidence says.

## 2.6 Remaining sections

| Rule | Check | Verdict |
|---|---|---|
| Section 2, 2A-2D and the 2C arithmetic | 2A/2B/2C declared NOT APPLICABLE with a reason (asset-light, no capex programme, no facility list, no utilisation metric; technology spend is opex). 2D covered under 1B and E1. `capex_embedded_growth_pct` set to 0 "not estimated". Compliant with rule 5 and with the never-estimate law. | PASS |
| Section 4, 4A/4B/4C | All three present. 4C is notably even-handed: it names the active headwind before the tailwinds. | PASS |
| Section 5 classification | 28 sits in 25-39 → MOAT STRENGTHENING. | PASS |
| Section 6, 6A-6E | All five present. 6C uses the injected B01 figures and they tie to the B01 block (core 85, moat 30, grand 115, EXCELLENT, 7 confirmed, FORTRESS). | PASS |
| 6D label from the permitted set | "EXCELLENT+" is in the prompt's list, with reasoning given. The stage also states honestly that the ladder-transition setup does **not** apply here, rather than forcing IEX into the transition-alpha frame. | PASS |
| catalysts_12m with evidence_type and anchor | Four rows, all four fields populated on each. | PASS |

**One observation on scope-splitting, not a fail.** The two highest-scoring rows
are scoped to exclude the live threat: D2 is "(RTM/BESS/API lock-in, **ex-DAM**)"
and R1 is "(**ex-coupling**)". Together they contribute 7.4 of 28.4, a quarter of
the total. The exclusions are defensible for a forward-looking emerging-moat scan
and they are disclosed everywhere they matter — the report opens with "THE MOAT
QUESTION UP FRONT" on coupling, and the threat runs through 4C, 6B, 6D and
`top_moat_risks`. But the scored total itself does not net the headwind, so a
downstream reader who takes em_score 28 without the surrounding prose gets a
gross number, not a net one. Recording it for the operator; not scoring it as a
breach.

---

# PART 3 — FINDINGS

| # | Severity | Location | Finding | Recomputed |
|---|---|---|---|---|
| 1 | MAJOR | B07 Section 5 scoring table; B07 YAML `em_score` | Evidence multiplier 0.85 ("Blend") applied to B3, D2, H1. The prompt authorises only 1.0x, 0.7x, 0.5x and defines no blend. | 26.9 (all blends at 0.7x) to 29.9 (all at 1.0x) vs 28. Band STRENGTHENING and the EM>=25 UA qualifier hold across the range. |
| 2 | MAJOR | B01 report Block E, metric E2 | Promoter-holding change scored 3 on a 1-year window after the report itself states the required 3-year comparison is NOT FOUND. Operating rule 5 requires N/A → score 0. | E2 = 0, Block E = 10, core = 82. Still >=80. Classification EXCELLENT unchanged. |
| 3 | MINOR | B07 Section 5 / Section 3, category C2 | Tier mismatch. The scored proposition (base **diversifying**) is conceded in the report's own text to be 🎙️/implicit, while the row is scored at 📄 1.0x. | C2 = 1.4 at 0.7x. Combined with finding 1, worst case em_score 26.3 → 26. Band holds. |
| 4 | MINOR | B01 report Block A, metric A4 | Scored 5 where the band's stated condition ("latest >= earliest") is false. The 0.16pp decline falls in an undefined gap below the 1-3pp band. Disclosed by the stage with an explicit invitation to rescore. | A4 = 3, Block A = 18, core = 83. Classification unchanged. |
| 5 | MINOR | B07 completionist recount; YAML `completionist_recount`, `evidence_mix.documented` | The itemisation sums to 20 unique documented items across 9 named categories; the stated total is 21 across 8. The R1 item is counted both as folded into A4 and as a 21st item. | 20 unique. No score depends on it. |
| 6 | MINOR | B07 Section 3 completionist guard paragraph | "10 score None/0" followed by a list of 11 categories. As written the paragraph sums to 22 of 23. | 11 zero-scored categories. 9 + 3 + 11 = 23. |
| 7 | MINOR | B07 Section 5 scoring table | The prompt requires "all 23 rows"; the table shows 14 scored rows plus one collapsed zero row. Section 3 does address all 23. | No score effect. |
| 8 | MINOR | B07 Section 3, categories A2, F1; Section 2 | Anchors given as extracted-text line numbers ("AR line 11332", "AR line 4363", "AR lines 4678-4711") rather than the page form the prompt specifies. All three sit in NO-EVIDENCE categories. | No score effect. |
| 9 | MINOR | B07 Section 5, category C2 | Likelihood-impact label written "H x L/M" but bracketed "(MM)". The two disagree; the assigned raw of 2 is correct under either. | No score effect. |
| 10 | MINOR | B01 report, formula notes | ROCE computed without the prompt's required "computed" statement. I verified the compute branch is the correct one: the source's ROCE rows are label-only, no values. | Branch correct; label absent. |
| 11 | MINOR | B01 report, M5 | The four market-cap figures carry no per-figure source anchor, against operating rule 4. | No score effect. |
| 12 | MINOR | `outputs/reports/01-gate0.md` | The report does not end with the fenced YAML block the prompt's OUTPUT section requires. The block exists only as `blocks/B01-gate0.yaml`. `07-emoat.md` does carry its block, so the run is internally inconsistent. | Structural only. |
| 13 | MINOR | `outputs/blocks/B01-gate0.yaml` | Schema extras: `run_number` and `run_note` are not in the prompt's schema, and `input_gaps` is a list of typed objects where the schema shows a bare list. Both additive and useful for a rescore. | Structural only. |

**Observations recorded, not scored as breaches:** M5's conservative
broad-segment reading (narrow-segment reading would give M5 = 5, moat 34, grand
119, still FORTRESS/EXCELLENT); the Gate 0 data-confidence sensitivity between
the 8-year P&L window and the 3-year ROCE/FCF/WC sub-window; and B07's
scope-splitting on D2 (ex-DAM) and R1 (ex-coupling), which is disclosed but not
netted inside em_score.

---

# PART 4 — VERDICT

**No CRITICAL findings.** Nothing I found changes either classification.

- **Gate 0.** Core 85, moat 30, grand 115, FORTRESS, EXCELLENT — all re-derived
  and all tie. Under the strictest correction of both scoring defects (E2 → 0 and
  A4 → 3), core falls to 80, which is still inside the >=80 band, so EXCELLENT
  holds and no deal-breaker fires. All nine deal-breakers re-tested clean. The
  three not-applicable treatments I was asked to rule on — E1 = 0 for no
  promoter, M9 = 0 for no COGS line anywhere in the comparison set, and the
  correctly-removed PEER DATA NEEDED markers — are all **permitted by the prompt
  as written**, and each is the rubric's own stated branch rather than a
  penalty for missing data.
- **Emerging Moat.** em_score 28.4 → 28 re-derived exactly. Classification
  STRENGTHENING holds across every correction I can justify (range 26.3 to 29.9).
  Categories 21 and 22 both present and both correctly zero. The completionist
  recount was performed. **F2 = 0 as a deliberate negative finding is permitted**,
  and more than permitted: the scale floors at 0, and the stage preserved the
  adverse information in the summary row label, `flags[]`, `top_moat_risks` and as
  a global weight on management claims, rather than letting it disappear into the
  same zero as the ten absent categories.
- **Acceptance rate 84%**, above the 60% REWORK floor.
- **Valuation audit: pending phase 3.** Stages 10 and 11 have not run. The
  expectation-ledger and business-understanding-narrative checks (rules 13-14 and
  9) key to stages 11 and 13 and are likewise deferred.

**Recommended dispositions.** Finding 1 (0.85 multiplier) needs an operator
ruling, not a rework: the prompt has a genuine gap on blended-evidence rows and
either a blend rule or a weaker-tier-governs rule should be written into
`prompts/07` so the next scan does not have to invent one. Finding 2 (E2) is a
stage-1 correction if the operator wants strict rule-5 compliance; it costs 3
points and changes nothing else. Findings 3 to 13 are cleanup.

---

*Verifier C, phase 1 scope. Gate 0 and Emerging Moat only. I audited rule
application, not raw source fidelity — every number's existence at its cited
anchor is Verifier A's call and mine cannot override it.*

## HANDOFF BLOCK

```yaml
stage: B12c
company: "IEX"
run_date: "2026-09-08"
model: claude-opus-4-8
status: complete
scope: phase-1 (Gate 0 + Emerging Moat only; B10/B11 not run, valuation framework docs deliberately not loaded)
gate0:
  rules_checked: 53
  blocks_rederived: {A: 20, B: 18, C: 15, D: 19, E: 13}
  core_rederived: 85
  moat_rederived: 30
  grand_rederived: 115
  moats_confirmed_rederived: 7
  moat_class_concur: "FORTRESS"
  classification_concur: "EXCELLENT"
  deal_breakers_retested: 9
  deal_breakers_triggered: 0
  cagr_edge_rules_honoured: true
  na_treatments_ruled:
    - {metric: "E1", treatment: "0, no promoter (0.00%)", verdict: PERMITTED, basis: "rubric band <30 = 0; professionally-managed carve-out tested and correctly failed at FII+DII 44.10% < 50%"}
    - {metric: "M9", treatment: "0, no Material/COGS line for IEX or any of MCX/BSE/CDSL", verdict: PERMITTED, basis: "GM proxy not computable; literal rubric also lands at 0 via the at/below-peers band; proxy stated, nothing guessed"}
    - {metric: "M2/M5", treatment: "PEER DATA NEEDED markers removed, scored on supplied peers", verdict: PERMITTED, basis: "Block F rule scores 0 only where peer data is not provided; it is provided this run"}
  fails:
    - "E2 scored 3 on a 1-year window after the report states the required 3-year comparison is NOT FOUND; operating rule 5 requires score 0 (MAJOR)"
    - "A4 scored 5 where the band condition 'latest >= earliest' is literally false (0.16pp decline, undefined gap below the 1-3pp band) (MINOR)"
    - "ROCE computed without the prompt's required 'computed' statement; compute branch itself verified correct, source ROCE rows are label-only (MINOR)"
    - "M5 market-cap figures carry no per-figure source anchor (operating rule 4) (MINOR)"
    - "01-gate0.md does not end with the fenced YAML block the OUTPUT section requires (MINOR)"
    - "B01 YAML schema extras: run_number, run_note, typed input_gaps objects (MINOR)"
emoat:
  rules_checked: 29
  em_score_rederived: 28.4
  em_score_reported: 28
  arithmetic_ties: true
  classification_concur: "STRENGTHENING"
  categories_addressed: 23
  cat21_present: true
  cat21_score: 0
  cat21_both_legs_rule_respected: true
  cat22_present: true
  cat22_score: 0
  cat22_named_sacrifice_rule_respected: true
  i1_i2_contribution_stated: true
  completionist_recount_performed: true
  f2_negative_finding: {treatment: "scored 0 as a deliberate negative finding, not missing data", verdict: PERMITTED, basis: "prompt's F2 definition mandates the B05 promise-delivery cross-reference; scoring scale floors at 0; adverse finding preserved in the summary-row label, flags[], top_moat_risks and as a global weight on management claims"}
  recomputed_range: "26.3 to 29.9 under every justifiable multiplier correction; band 25-39 STRENGTHENING holds throughout; EM >= 25 UA qualifier holds"
  fails:
    - "Evidence multiplier 0.85 ('Blend') applied to B3, D2, H1; prompt authorises only 1.0x / 0.7x / 0.5x and defines no blend rule (MAJOR)"
    - "C2 scored at 1.0x while the report concedes the scored proposition (base diversifying) rests on 🎙️/implicit evidence (MINOR)"
    - "Completionist recount states 21 documented items across 8 categories; itemisation sums to 20 unique across 9 named categories, double-counting the R1/A4 VPPA item it claims not to double-count; evidence_mix.documented inherits it (MINOR)"
    - "Section 3 guard paragraph says '10 score None/0' then lists 11 categories; as written it sums to 22 of 23 (MINOR)"
    - "Section 5 scoring table shows 14 scored rows plus one collapsed zero row; prompt requires all 23 rows (MINOR)"
    - "Anchors given as extracted-text line numbers (AR line 11332 / 4363 / 4678-4711) rather than the page form the prompt specifies (MINOR)"
    - "C2 likelihood-impact label written 'H x L/M' but bracketed '(MM)' (MINOR)"
valuation:
  status: "pending phase 3"
  rules_checked: 0
  fails: []
  note: "Not run. Stages 10 and 11 have not executed and the valuation framework documents (Master v3.7 Role 1, Section 1B layer set, FTTCP) were deliberately not supplied to this phase-1 invocation as dead context."
expectation_ledger:
  status: "pending phase 3"
  present: false
  note: "Rules 13-14 key to stage 11 output; not run."
business_understanding_narrative:
  status: "pending phase 3"
  present: false
  note: "Keys to stage 13 synthesis; not run."
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MAJOR, location: "B07 Section 5 scoring table / B07 YAML em_score", description: "Unauthorised evidence multiplier 0.85 applied to B3, D2, H1; framework grants only 1.0x, 0.7x, 0.5x and defines no blend. Recomputed 26.9 (all 0.7x) to 29.9 (all 1.0x) vs 28; STRENGTHENING band and EM>=25 UA qualifier hold across the range."}
  - {severity: MAJOR, location: "B01 report Block E metric E2", description: "Promoter-holding change scored 3 on a 1-year window after the report itself states the required 3-year comparison is NOT FOUND; operating rule 5 requires N/A to score 0. Recomputed E2=0, Block E=10, core=82, still >=80, classification EXCELLENT unchanged."}
  - {severity: MINOR, location: "B07 category C2", description: "Evidence-tier mismatch. The scored proposition (customer base diversifying) is conceded in the report's own text to rest on management claim and implication, while the row is scored at documented 1.0x. At 0.7x, C2 = 1.4; combined worst case em_score 26.3, band still STRENGTHENING."}
  - {severity: MINOR, location: "B01 report Block A metric A4", description: "Scored 5 where the band's stated condition 'latest >= earliest' is false; the 0.16pp decline falls in an undefined gap below the smallest 1-3pp band. Stage disclosed it and invited rescoring. Recomputed A4=3, Block A=18, core=83, classification unchanged."}
  - {severity: MINOR, location: "B07 completionist_recount and evidence_mix.documented", description: "Recount states 21 documented items across 8 categories; the itemisation sums to 20 unique across 9 named categories and double-counts the R1/A4 VPPA notification the clause says is counted once. Defect sits inside a framework-mandated control; no score depends on it."}
  - {severity: MINOR, location: "B07 Section 3 completionist guard paragraph", description: "States '10 score None/0' then lists 11 categories (A1, A2, B1, B2, E2, F1, F2, G2, H3, I1, I2). As written the paragraph sums to 22 of 23; the correct split is 9 active + 3 weak + 11 zero."}
  - {severity: MINOR, location: "B07 Section 5 scoring table", description: "Prompt requires a full 23-row scoring table; the table carries 14 scored rows plus one collapsed 'All other categories' row. All 23 are addressed in the Section 3 summary, so the substantive requirement is met and the total is unaffected."}
  - {severity: MINOR, location: "B07 Section 3 categories A2, F1 and Section 2", description: "Source anchors given as extracted-text line numbers (AR line 11332, AR line 4363, AR lines 4678-4711) rather than the (AR p.__) form the prompt specifies. All three sit in NO-EVIDENCE categories; a reader cannot resolve a line number to a page."}
  - {severity: MINOR, location: "B07 Section 5 category C2 row", description: "Likelihood-impact label written 'H x L/M' but bracketed '(MM)'. The two disagree; the assigned raw score of 2 is correct under either reading, so no score moves."}
  - {severity: MINOR, location: "B01 report formula-notes section", description: "ROCE computed without the prompt's required 'computed' statement. I verified the branch is correct: screener-Balance_Sheet.csv rows 18-19 carry Return on Equity and Return on Capital Emp as label-only rows with no values, and screener-Data_Sheet.csv has no ROCE row and no Total Assets row, so the source figure is genuinely absent."}
  - {severity: MINOR, location: "B01 report M5", description: "Four market-cap figures quoted with no per-figure source anchor, against operating rule 4 which requires an anchor on every extracted number."}
  - {severity: MINOR, location: "runs/iex-2026-09-08/outputs/reports/01-gate0.md", description: "Report does not end with the fenced YAML block the prompt's OUTPUT section requires; the block exists only as blocks/B01-gate0.yaml. 07-emoat.md does carry its block, so the run is internally inconsistent on this point."}
  - {severity: MINOR, location: "runs/iex-2026-09-08/outputs/blocks/B01-gate0.yaml", description: "Schema extras beyond the prompt's block: run_number, run_note, and input_gaps as a list of typed objects where the schema shows a bare list. Additive and useful for a rescore, but not the block as specified."}
observations:
  - "M5 = 1 is the literal and conservative reading of a four-name comparison set. Read against the narrower power-exchange segment where management claims 80-85% share, M5 = 5, moat = 34, moats_confirmed = 8, grand = 119, still FORTRESS / EXCELLENT. The conservative choice is disclosed and costs nothing."
  - "Gate 0 data confidence reads 8 years off the P&L window while ROCE, FCF and WC-days rest on a 3-year sub-window. Had 3 years governed the whole run, the prompt's LIMITED tier would have downgraded EXCELLENT one tier. I do not read the prompt that way; recorded for operator sensitivity."
  - "B07 scopes its two highest-scoring rows to exclude the live threat (D2 ex-DAM, R1 ex-coupling), together 7.4 of 28.4. Disclosed throughout the prose and in top_moat_risks, but em_score itself is a gross number, not net of the coupling headwind."
  - "Run-2 supersession is clean: every score delta versus run 1 traces to a named new source (FY24 AR comparative, full AR text, peer Data_Sheets), not to a re-reading of the same evidence. No stale run-1 figure survives in the run-2 artifact."
critical_count: 0
major_count: 2
minor_count: 11
acceptance_rate: 84             # 69 of 82 framework-governed claims verified compliant (gate0 47/53, emoat 22/29)
rework_triggered: false
```
