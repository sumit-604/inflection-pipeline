# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: INDNIPPON | Run date: 2026-09-10 | Model: claude-opus (verifier-c-framework)
Scope: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07).
Valuation adherence (B10 / B11), Expectation Ledger, and Business Understanding
Narrative audits are PENDING PHASE 3. Stages 10, 11 and 13 do not exist for this
run. No valuation framework document was loaded, read, or reasoned about.

RULE SOURCES USED (the only two):
- `prompts/01-gate-0-pipeline.md`
- `prompts/07-emerging-moat-pipeline.md`

ARTIFACTS AUDITED:
- `runs/indnippon-2026-09-10/outputs/blocks/B01-gate0.yaml`
- `runs/indnippon-2026-09-10/outputs/reports/01-gate0.md`
- `runs/indnippon-2026-09-10/outputs/blocks/B07-emoat.yaml`
- `runs/indnippon-2026-09-10/outputs/reports/07-emoat.md`
- `runs/indnippon-2026-09-10/outputs/blocks/B00-inputs.yaml` (read only to confirm
  NO-CONCALL MODE was a declared run-level condition, for the F2 substitution test)

QUESTION ANSWERED: adherence, not agreement. A defensible score under the rules
passes even where a different scorer would land elsewhere. Only a rule actually
broken is a finding.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### 1.1 Block re-derivation from the stated inputs

Every band in `prompts/01-gate-0-pipeline.md` "SCORING BLOCKS" was re-read and
re-applied to the numbers the report itself states.

| Line | Stated input (report anchor) | Prompt band | Correct score | B01 score | Verdict |
|---|---|---|---|---|---|
| A1 | Median ROCE 13.68% (01-gate0.md L60) | `15-19.9 = 3 \| 10-14.9 = 1` | **1** | **3** | **FAIL** |
| A2 | Min ROCE 11.43% (L62) | `8-11.9 = 1` | 1 | 1 | PASS |
| A3 | Median ROE 11.54% (L85) | `<12 = 0` | 0 | 0 | PASS |
| A4 | 15.02% latest vs 11.43% earliest (L63) | `latest ≥ earliest = 5` | 5 | 5 | PASS |
| B1 | Cum CFO/PAT 411.07/583.11 = 0.705 (L117) | `0.70-0.84 = 2` | 2 | 2 | PASS |
| B2 | 1 of 2 FCF-positive years = 50% (L151) | `50-74 = 2` | 2 | 2 | PASS on band (window issue, F-GATE0-03) |
| B3 | Cum FCF/PAT 12.6% (L153) | `<0.20 = 0` | 0 | 0 | PASS |
| B4 | WC days +10.84 (L171) | `increased 5-15 = 1` | 1 | 1 | PASS |
| C1 | Rev CAGR 13.17% (L192) | `10-14.9 = 3` | 3 | 3 | PASS |
| C2 | PAT CAGR 14.44% adj (L216) | `10-14.9 = 3` | 3 | 3 | PASS on band (basis issue, F-GATE0-02) |
| C3 | 8 of 9 positive = 88.9% (L220) | `75-99 = 3` | 3 | 3 | PASS |
| C4 | +1.27pp (L224) | `±3pp = 3` | 3 | 3 | PASS |
| D1 | Net cash −Rs 4.32 cr (L237) | `net cash = 5` | 5 | 5 | PASS |
| D2 | IC 252x (L238) | `≥10x = 5` | 5 | 5 | PASS |
| D3 | D/E 0.0023 (L240) | `<0.1 = 5` | 5 | 5 | PASS |
| D4 | Current ratio 2.5 (L241) | `≥2.0 = 5` | 5 | 5 | PASS |
| E1 | Promoter 70.37% (L255) | `≥60% = 5` | 5 | 5 | PASS |
| E2 | NOT FOUND (L261-277) | rule 5 → 0 | 0 | 0 | PASS |
| E3 | NOT FOUND (L279-287) | rule 5 → 0 | 0 | 0 | PASS |
| E4 | Cont. liab / NW 1.98% (L289) | `<5% = 5` | 5 | 5 | PASS |

**Arithmetic re-derivation, as filed.** A 3+1+0+5 = 9. B 2+2+0+1 = 5. C 3+3+3+3 = 12.
D 5+5+5+5 = 20. E 5+0+0+5 = 10. Core = 9+5+12+20+10 = **56** ✓ matches
`core_score: 56`. Block maxima 20 each, core out of 100 ✓ matches the prompt.
Moat 3+0+3+3+0+0+0+1+0+3+5+1 = **19** ✓ matches `moat_score: 19`, max 60 ✓.
Grand total 56+19 = **75** ✓ matches `grand_total: 75` and the 160 ceiling ✓.
The `grand: 75` alias key is an extra key not in the prompt schema, is documented
in-line as an orchestrator schema alias, and carries the identical value. Not a
finding.

**Moat class.** 5 tests at ≥3 (M1, M3, M4, M10, M11). Prompt: `4-5 = STRONG`.
`moats_confirmed: 5`, `moat_class: STRONG` ✓ PASS.

**CAGR mechanics.** FY2017→FY2026 is 9 periods; the report uses `^(1/9)` ✓.
Independent recompute: revenue (1068.48/351.09)^(1/9)−1 = 13.17% ✓;
PAT adjusted (99.58/29.57)^(1/9)−1 = 14.44% ✓; reported-basis 15.85% ✓ (report
says 15.86%, immaterial). M11 windows recompute to 17.65% and 11.08% ✓.
WC-day recomputes: FY24 71.45+34.87−65.68 = 40.64 ✓; FY26 70.53+31.06−50.12 =
51.47 ✓.

**CAGR edge rules.** No endpoint is zero or negative; no loss-to-profit swing;
PAT CAGR is not N/M so the C4 zero-out does not apply. All three edge rules
correctly not fired ✓ PASS.

### FINDING F-GATE0-01 — MAJOR — A1 scored from the wrong band

Location: `outputs/reports/01-gate0.md` L60; `outputs/blocks/B01-gate0.yaml`
`blocks: {A: 9}`, `core_score: 56`, `grand_total: 75`.

Rule breached, quoted from `prompts/01-gate-0-pipeline.md`, [BLOCK A: RETURN ON
CAPITAL, Max 20]:

> "A1 Median ROCE: ≥25% = 5 | 20-24.9 = 4 | 15-19.9 = 3 | 10-14.9 = 1 | <10 = 0"

Departure: B01 states "A1 Median ROCE (3 yrs: 11.43, 13.68, 15.02) = **13.68%** →
band 10-14.9% = **3**". The prompt assigns 3 to the 15-19.9 band. 13.68% falls in
10-14.9, which scores **1**. The stage read the score from the adjacent slot.

Recomputation and its reach:
- A1 = 1 → **Block A = 3+1+0+5 = 7 / 20** (filed: 9).
- Core score = 7+5+12+20+10 = **54 / 100** (filed: 56).
- Grand total = 54+19 = **73 / 160** (filed: 75).
- Classification matrix `Core 40-59 = AVERAGE`: **AVERAGE, unchanged.**
- Deal-breaker 1, "Block A <8 → max GOOD", flips from NOT TRIGGERED to
  **TRIGGERED** (non-binding, AVERAGE already sits below the GOOD cap). B01's
  deal-breaker line "1. Block A <8 → max GOOD: Block A = 9, NOT triggered"
  (L418) is wrong as a consequence.

Severity MAJOR, not CRITICAL: the classification, the moat class, the flags and
every downstream gate reading survive the correction. Two points and one
non-binding deal-breaker line move.

### FINDING F-GATE0-02 — MINOR — exceptional-item adjustment is outside the fixed formula set

Location: `01-gate0.md` L41-44 (EBIT basis), L207-218 (C2 basis);
`B01-gate0.yaml` `data_notes[1]`.

Rules breached, `prompts/01-gate-0-pipeline.md`:

> "2. No qualitative judgments. Only numbers and the scoring rules provided."
> "## FORMULA DEFINITIONS (fixed, do not substitute alternatives) ... CAGR =
> (End ÷ Start)^(1/years) − 1."

Departure: FY26 PAT and PBT were restated ex the Rs 15.21 cr HSVP land-
compensation gain (adjusted PAT Rs 99.58 cr against reported Rs 111.17 cr) and
that adjusted figure drives C2, C4 and the ROCE series. The prompt defines CAGR
on the stated PAT endpoints and does not define an EBIT normalisation. The
report cites an operator instruction; no such instruction appears in any
artifact I hold, so I cannot confirm it. **NOT FOUND**, recorded rather than
assumed either way.

Mitigation, which is why this is MINOR and not MAJOR: the adjustment is
disclosed in `data_notes`, both bases are printed side by side, and it moves the
score DOWN, not up. Recomputation on the literal formula: C2 = 15.85% → band
`15-19.9 = 4`; C4 = 15.85 − 13.17 = +2.68pp → band `±3pp = 3`, unchanged;
**Block C = 13** (filed 12), core +1. Classification AVERAGE in either reading.

### FINDING F-GATE0-03 — MINOR — B2 scored on a 2-year window, below the stated minimum

Location: `01-gate0.md` L142-155; `B01-gate0.yaml` `blocks: {B: 5}`.

Rule breached:

> "6. Use whatever history is available: minimum 3 years, maximum whatever
> exists."

and rule 5:

> "If a data point is not available, mark it 'N/A (not in provided data)' and
> score it 0."

Departure: capex is NOT FOUND for FY2017-FY2024, so FCF exists for two years
only. B2 ("FCF-positive years as proportion") was scored 2 on a 1-of-2 = 50%
window. Two years sits below the prompt's own three-year floor; the strict rule-5
treatment is N/A → 0. B3 already scored 0, so only B2 is exposed.

Recomputation under the strict reading: B2 = 0 → **Block B = 3 / 20** (filed 5);
core = 52 with F-GATE0-01 also applied. Classification **AVERAGE, unchanged**.
Deal-breaker 2 (Block B <8) stays triggered either way. The stage disclosed the
window and flagged it "LIMITED", which is why this is MINOR: a disclosed,
arguable reading, not a concealed fill.

### FINDING F-GATE0-04 — MINOR — deal-breaker recorded without its driving years

Location: `B01-gate0.yaml` `deal_breakers[0]`.

Rule breached, "## CLASSIFICATION AND OVERRIDES":

> "Deal-breaker overrides (record them; they cap classification per the original
> rules, but note for the pipeline: downstream position sizing may override
> AVERAGE for documented post-IPO rebase / legacy cleanup cases, so state WHICH
> years drive any deal-breaker)"

Departure: the payload entry reads only "Block B <8 -> max GOOD (triggered,
non-binding: AVERAGE already below GOOD cap)". No years. The driving years
(FY26 FCF negative, FY24→FY26 WC-day rise) do appear in `flags[FLAG-CASH]`,
`block_b_trend` and the Block B narrative, so the information reaches the
downstream reader; it is absent from the field the prompt points at.

### FINDING F-GATE0-05 — MINOR — PEER DATA NEEDED items not carried in `data_notes`

Location: `B01-gate0.yaml` `data_notes[]` vs `input_gaps[6]`.

Rule breached, the prompt's own YAML schema comment:

> "data_notes: []  # loss-to-profit swings, proxy bases used, PEER DATA NEEDED
> items"

Departure: M2 and M5 are marked "PEER DATA NEEDED" and scored 0 in the report
(correctly), but the payload records them under `input_gaps` ("Peer data for M2,
M5, M9 moat tests: NOT SUPPLIED"). Only M9's proxy basis reaches `data_notes`.
Placement defect, no scoring consequence.

### FINDING F-GATE0-06 — MINOR — approximate page anchors

Location: `01-gate0.md` L72 ("p.~30"), L259 ("p.~13", "p.~108"), L263 ("p.~208"),
L241 ("p.~232"), L345 ("p.~122").

Rule breached:

> "4. SOURCE ANCHORS ARE MANDATORY. Every extracted number is immediately
> followed by its source in parentheses: (screener-data), (results Q4 FY26 p.3),
> (AR p.187, Note 27)."

Departure: six anchors carry a tilde-prefixed approximate page. The prompt's
anchor form is an exact page or note. Several of the affected numbers are E1
(promoter 70.37%) and E4 (net worth Rs 821.32 cr), which are load-bearing for
Block E. Existence-of-the-number is Verifier A's gate, not mine; I record only
the anchor form.

### 1.2 Deal-breaker handling (task check 2)

The prompt's deal-breaker semantics are **caps**, not verdict-setters:

> "Deal-breaker overrides (record them; they cap classification per the original
> rules ...)"
> "2 Block B <8 → max GOOD"

B01 records "Block B <8 -> max GOOD (triggered, non-binding: AVERAGE already
below GOOD cap)". A cap of GOOD applied to an AVERAGE classification does not
move it; AVERAGE is already the lower value. **This is exactly how the prompt
says a triggered deal-breaker must be treated.** PASS. All nine deal-breakers are
enumerated and individually checked at L417-430; each non-trigger is anchored to
its number. PASS.

Classification matrix applied as written:

> "Core 60-79 + STRONG/FORTRESS = GOOD+ | ... | Core 40-59 = AVERAGE"

Core 56 (or 54 corrected, or 52 on the strictest reading) sits in 40-59 and the
40-59 row is not moat-conditioned, so the STRONG moat class cannot lift it. B01
states this explicitly at L413-415. PASS.

Data confidence: "10+ yrs full" against `data_years: 10`, `history_downgrade:
false`. The confidence tier keys to available history, which is 10 years for the
revenue/PAT/CFO series. The sub-metric windows (3-year ROCE, 2-year FCF) are
disclosed separately. PASS, with the B2 window exposure carried at F-GATE0-03.

### 1.3 NOT FOUND discipline (task check 3)

Rule quoted:

> "5. GROUNDED CLAIMS. Before reporting any figure, confirm it exists in the
> provided data. If a data point is not available, mark it 'N/A (not in provided
> data)' and score it 0. Never fill gaps with typical-industry values or
> estimates."

and, for the moat block:

> "If a test needs peer data that is not provided, score 0 and mark 'PEER DATA
> NEEDED' (never guess peer figures)."

| NOT FOUND item | Treatment in B01 | Rule verdict |
|---|---|---|
| Current liabilities / trade payables pre-FY2024 | ROCE and WC days scored on FY24-FY26 only; gap in `input_gaps` | Compliant. Rule 6 permits adapting to available history; three years meets the floor |
| Capex pre-FY2025 | FCF window 2 years, disclosed and flagged LIMITED | Window below the 3-year floor; see F-GATE0-03 |
| Promoter holding 3 years back (E2) | Scored **0**, "NOT FOUND, per rule 5; not evidence of an actual decrease" | Compliant, and correctly refuses the inference that the intra-group transfer left the total flat |
| Promoter pledge (E3) | Scored **0**, states nil pledge is the common Indian AR practice but does not score it as nil | Compliant. This is the exact temptation rule 5 forbids and the stage refused it |
| Peer data for M2, M5, M9 | Each scored **0**, "PEER DATA NEEDED" | Compliant |
| Export rupee figure and 2W-industry comparator (LB4) | Marked NOT FOUND, not estimated | Compliant |

**No NOT FOUND field was silently filled.** Every zero is labelled as a
conservative default rather than as evidence of a bad fact, and `FLAG-DATA-GAP`
routes E2/E3 to live-web verification. PASS on all six.

### 1.4 Gate 0 rule ledger

29 rules checked, 23 passed, 6 failed (1 MAJOR, 5 MINOR). Gate 0 acceptance
rate: **79%**.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### 2.1 Score re-derivation (task check 4)

Matrix quoted from `prompts/07-emerging-moat-pipeline.md` SECTION 5:

> "raw score from the likelihood × impact matrix (HH=4, HM/MH=3, HL/MM/LH=2,
> ML/LM=1, LL=1, no evidence=0), then multiply by evidence quality (📄 1.0x,
> 🎙️ 0.7x, 🔍 0.5x)"

| Row | Stated L×I | Prompt raw | Filed raw | Tier | Prompt multiplier | Filed adjusted | Verdict |
|---|---|---|---|---|---|---|---|
| A2 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | PASS |
| A3 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| A4 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| B1 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| B2 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | PASS |
| C1 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| C2 | LL | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| E2 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | PASS |
| F1 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| F2 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | PASS |
| G1 | LM | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| H2 | MM | 2 | 2 | 🎙️ | 0.7 | 1.4 | PASS |
| H3 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | PASS |
| I2 | MM | 2 | 2 | 🔍 | 0.5 | 1.0 | PASS |
| R1 | HL | 2 | 2 | 📄 | 1.0 | 2.0 | PASS |
| A1, B3, D1, D2, E1, G2, H1, I1 | no evidence | 0 | 0 | — | — | 0 | PASS |

Independent sum: 3+1+1+1+3+1+1+3+1+3+1+1.4+1+1+2 = **24.4** ✓ matches the filed
raw total. All 23 rows present (22 categories + R1) as the prompt requires ✓.

**Rounding.** 24.4 → 24. The prompt states no rounding rule, so nearest-integer
applies; it is also the conservative direction here. No band manipulation: 24.4
and 24 both sit inside `12-24 MODEST MOAT DEVELOPMENT`. PASS.

**Band boundaries.** Quoted: "≥40 MOAT EXPANSION UNDERWAY | 25-39 MOAT
STRENGTHENING | 12-24 MODEST MOAT DEVELOPMENT | <12 NO MEANINGFUL EMERGING
MOAT". 24 → MODEST ✓. `em_classification: "MODEST"` matches the enum ✓. The
one-point shortfall against both the STRENGTHENING band and the "EM ≥25" UA
qualifier is stated in the report and raised as `FLAG-EM-BELOW-UA` rather than
rounded away. The bands were applied absolute, per the 20-Aug-2026 operator
ruling in the prompt header, with no rescale ✓ PASS.

**I1/I2 separate statement.** Prompt: "State the I1/I2 contribution separately in
the scoring table". Report L531-535 states 1.0 point total and shows the score
holds at 23.4 with I1/I2 removed ✓ PASS.

**Evidence-tier consistency (Verifier C rule 3: a 🎙️-only category scoring as
if 📄 is a finding).** Checked every 1.0x row for at least one genuine 📄 item.
All fifteen 1.0x rows anchor to Annual Report text, Ind AS notes, BRSR, or a
dated completed operational fact in a Reg-30 filing. The stage declared its tier
rule at L17-25 and held BorgWarner, the ECU MoU, the TFT/LCD clusters and the 4W
showcase at 🎙️, and the I2 implausibility inference at 🔍. Treating a
commissioned plant or a commenced SoP as 📄 is consistent with the prompt's own
📄 list ("plant under construction, product launched") which keys to the nature
of the fact, not to the document it appears in. **No tier inflation found.**
PASS.

### 2.2 Completionist guard (task check 4, second half)

Rule quoted:

> "6. COMPLETIONIST GUARD: the realistic base rate is 3 to 6 categories with
> genuine evidence for most companies. If you find yourself scoring 12 or more
> categories as active, stop and re-examine ... Recount the 📄 items
> specifically before finalising the scorecard."

and, from Section 3:

> "apply the completionist guard check explicitly: '📄 recount performed: [n]
> documented items across [m] categories.'"

The recount line is present and in the mandated shape (report L462-471; block
`completionist_recount`). The remedy the guard demands, a 📄-specific recount
before finalising, was performed and published. The outcome is genuinely sparse:
0 Strong rows, 4 Moderate, 24.4 against a 92 ceiling. PASS on substance, with
the counting defects below.

### FINDING F-EMOAT-01 — MINOR — Section 3 strength tally does not reconcile to 23 rows

Location: `07-emoat.md` L459-460; `B07-emoat.yaml` `completionist_recount`.

Rule breached, Section 3:

> "Section 3 summary table: all 22 rows with evidence?, type, strength
> (Strong/Moderate/Weak/None), time to materialise. State the count with
> Strong/Moderate evidence ..."

Departure: the filed tally reads "4 Moderate (A2, B2, E2, F2), 9 Weak, 8 None/0,
plus one explicit negative finding (G2)". Recount from the stage's own summary
table:

- Moderate = 4 (A2, B2, E2, F2) ✓
- Weak = **11** (A3, A4, B1, C1, C2, F1, G1, H2, H3, I2, R1), not 9
- None = 8 (A1, B3, D1, D2, E1, G2, H1, I1), with G2 already inside that 8

Filed tally sums to 21 (or 22 counting G2 twice) against 23 rows. Correct tally:
**4 Moderate / 11 Weak / 8 None, G2 being one of the 8**. The mandated count,
"the count with Strong/Moderate evidence", is correct at 0 Strong and 4
Moderate, and the scorecard total is computed from the table rather than the
tally, so no score moves. Presentational.

### FINDING F-EMOAT-02 — MINOR — recount line hedged and its category count mislabelled

Location: `07-emoat.md` L462-471; `B07-emoat.yaml` `completionist_recount`.

Rule breached: the guard's mandated line format, "📄 recount performed: [n]
documented items across [m] categories", and the guard's own trigger wording,
"scoring 12 or more categories as active".

Departures, three, all small:
1. The count is stated as "**approximately** 34 documented evidence items". A
   mandated count is a count. Re-adding the stage's own enumerated groups lands
   at roughly 35-37, not 34.
2. "[m]" is filed as "13 non-zero-scored categories". Non-zero-scored rows number
   **15**; 13 is the count of non-zero rows carrying 📄 evidence (15 less H2 at
   🎙️ and I2 at 🔍). The number is defensible under the second reading; the
   label is not.
3. The stage concludes it is "well inside the realistic 3 to 6 base rate" by
   counting the 4 Moderate rows. The guard's base rate speaks of "categories with
   genuine evidence", of which there are 15 here, so the trigger arguably fired.
   The required remedy was nonetheless performed, and no tier inflation was found
   on my own row-by-row check, so the guard's purpose was served.

### FINDING F-EMOAT-03 — MINOR — `evidence_mix.claim` undercounts the 🎙️ items in the report

Location: `B07-emoat.yaml` `evidence_mix: {documented: 34, claim: 4, inference: 1}`.

Rule breached: the prompt's YAML schema, `evidence_mix: {documented: 0, claim: 0,
inference: 0}   # item counts`.

Departure: distinct 🎙️ items in the report are five, not four: TFT instrument
cluster (L82), coloured LCD cluster (L83), BorgWarner licence (L84, restated at
L381), 4W tech showcase (L99), unnamed ECU MoU (L382). `inference: 1` (I2) ✓
correct. `documented: 34` is filed as an exact integer while the report calls the
same number "approximately 34"; see F-EMOAT-02. No score consequence: the
multipliers are applied per row, not per item count.

### FINDING F-EMOAT-04 — MINOR — three anchors use extraction line numbers, not the mandated form

Location: `07-emoat.md` L79 ("AR2026 p.20/**p.1306-1311**"), L326 ("AR2026 BRSR,
**extracted L14968**"), L390 ("AR2026 BRSR, **extracted L10410-10411**").

Rule breached:

> "3. SOURCE ANCHORS on every evidence item: (AR p.__), (Q_ FY__ call), (Inv.
> Pres. slide __)."

Departure: three items anchor to text-extraction line offsets or an out-of-range
page number rather than an AR page or note. The affected items are the
mid-pressure sensor row, the attrition figure (F1) and the ZLD compliance item
(H3), none of them load-bearing on the total. Anchor form only; the existence of
the underlying number is Verifier A's gate.

### 2.3 Combined assessment (task check 5)

Rule quoted, Section 6D:

> "6D combined classification per the standard matrix (EXCEPTIONAL / EXCELLENT+ /
> HIGH POTENTIAL / GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID), remembering that
> GOOD or AVERAGE backward scores with EXPANSION forward scores are exactly the
> transition setups this operation hunts; give HIGH POTENTIAL and TURNAROUND rows
> full reasoning."

Findings on the check:
- The forward score is 24 = MODEST. The transition setup the rule names requires
  an **EXPANSION** forward score (≥40). 24 is below EXPANSION and below
  STRENGTHENING (25-39). B07's statement that the AVERAGE+EXPANSION setup "does
  not fire here" is **correct on the prompt's own band definitions.** PASS.
- Gate 0 inputs were carried unchanged into 6C: `core_score: 56`, `moat_score:
  19`, `moats_confirmed: 5`, `moat_class: STRONG`, `classification: AVERAGE`,
  each cited to the injected B01 block (report L609-610) ✓ PASS. Note: the
  F-GATE0-01 correction moves the injected core to 54, which stays in the same
  40-59 AVERAGE band, so 6C's conclusion is unaffected.
- Combined verdict AVERAGE. **Limitation, recorded rather than papered over:**
  the "standard matrix" that maps a backward class against a forward class is
  named in the prompt but is not reproduced anywhere in
  `prompts/07-emerging-moat-pipeline.md`. Its cell-by-cell text is **NOT FOUND**
  in my rule sources, so I can verify only the rule that IS stated (the
  AVERAGE+EXPANSION line), which B07 applies correctly. AVERAGE backward plus
  MODEST forward mapping to AVERAGE contradicts nothing in the stated text.
  PASS on what is verifiable; not a finding against the stage.
- The prompt asks for full reasoning on HIGH POTENTIAL and TURNAROUND rows only.
  Neither fired; B07 supplied full reasoning anyway (L616-643). PASS.

### 2.4 The NO-CONCALL F2 substitution: sanctioned degradation or breach? (task check 6)

Rule quoted, FAMILY F:

> "F2 execution moat (capex on time and budget across ARs, ramp speed
> post-commissioning, revenue per employee trend, guidance delivery;
> cross-reference the injected concall promise-delivery record)."

and the injected-input slot:

> "CONCALL PROMISE-DELIVERY RECORD (from B05, for F2): {{B05_PROMISE_DELIVERY}}"

and rule 5:

> "5. If no evidence exists for a category, state 'NO EVIDENCE FOUND' and move
> on. Never force-fit."

**Verdict: SANCTIONED DEGRADATION, not a rule breach.** Four reasons, each tied
to text:

1. F2's what-to-look-for list is a list, not a conjunctive test. Capex delivery
   "across ARs" is the FIRST named leg; the promise-delivery record is a
   "cross-reference", the last-named leg. Evidence exists for the capex leg, so
   rule 5's "NO EVIDENCE FOUND" branch does not apply.
2. The missing input is a genuine absence, not a skipped read. `B00-inputs.yaml`
   records it at run level: "concalls/: EMPTY. DECLARED, NOT A GAP ... INEL
   publishes no earnings-call transcripts; verified against BSE announcement
   history for scrip 532240 across 01-Jul-2025 to 10-Sep-2026 (zero transcript
   filings, seven investor presentations). NO-CONCALL MODE is active."
3. The stage labelled the substitution rather than passing it off. The report
   header (L8-15) and the F2 row (L343-348) both state it is "a record of
   sequential completion without a disclosed miss, not a verified promise-kept
   record", and name the reason: no original committed date or budget exists in
   the corpus. `input_gaps[0]` carries the same. The Verifier C concern that a
   category is scored on weaker evidence than it claims does not arise: the claim
   is downgraded to match the evidence.
4. The degradation is priced into the score. Impact is capped at Medium
   explicitly because the milestones are "unverifiable against a plan", giving
   HM = 3 rather than HH = 4, and the limitation is repeated in `top_moat_risks`
   and in 6B's F2 early-warning line.

The five milestone items themselves are dated, completed operational facts in
exchange-filed (Reg-30) documents, which sit inside the prompt's 📄 definition
("plant under construction, product launched"). The 1.0x multiplier on F2 is
therefore correct. PASS.

### 2.5 Section and schema completeness

| Requirement | Verdict |
|---|---|
| All six sections in one response | PASS |
| 1A statuses, evidence type, launch, revenue potential, differentiation | PASS; unknowns marked NOT FOUND, not estimated |
| 1C mix-shift table with forward % | PASS; forward % NOT FOUND and named as the scan's central gap, not filled |
| 2A capex table | PASS; all rupee/capacity cells NOT FOUND, disclosed as an input gap |
| 2B utilisation | PASS; NOT FOUND, and the renewable-energy utilisation figures were explicitly refused as a substitute |
| 2C arithmetic shown | PASS; recomputed 6.82 × 6.55 = 44.67 → 4.18% of 1,068.48 ≈ 4.2%; FAT 1068.48/163.03 = 6.554 ✓; `capex_embedded_growth_pct: 4.2` matches |
| 2D geography/market entries | PASS |
| Section 3, all 22 categories addressed or NO EVIDENCE FOUND | PASS, 23 rows with R1 |
| Categories 21 (I1) and 22 (I2) present (Verifier C rule 8) | PASS |
| I1 above 0 only with both legs, (b) carrying ≥1 📄 | PASS; scored **0**, the (b) structural-economics leg absent, and the prompt's "hiring story scores 0" rule quoted in-line |
| I2 above 0 only with a specific named sacrifice; top band needs a 📄 competitor source | PASS; scores 2 × 0.5 = 1.0 on the prompt's second sanctioned direction ("decades-old institutional customer relationships no capex can shortcut"), top band withheld for want of a competitor filing, and the "nothing must be destroyed → 0" rule applied to every other moat in the scan |
| Section 4 R1 with 4A/4B/4C | PASS; GST 2.0 correctly failed on the "do competitors share the benefit" test and scored shared/weak, not moat |
| Optionality register, 4 columns, carried as `optionality_register[]` | PASS, 7 rows, all either 0-scored or 🎙️/🔍-resting |
| Section 6A-6E | PASS |
| `active_categories` = Strong/Moderate rows only | PASS, 4 rows |
| `catalysts_12m` with evidence type and anchor | PASS, 5 rows |
| `analyst_note` ≤ 200 words | PASS (~120) |
| YAML schema keys present and matching the report | FAIL (F-EMOAT-03) |

### 2.6 Emerging Moat rule ledger

28 rules checked, 24 passed, 4 failed (0 MAJOR, 4 MINOR). Emerging Moat
acceptance rate: **86%**.

---

## PART 3 — VALUATION ADHERENCE: PENDING PHASE 3

Not run, by scope instruction. Stages 10 and 11 do not exist for this run.
The following Verifier C rules are DEFERRED, not passed and not failed:

- Rule 4, growth symmetry and pillar mechanics (B11)
- Rule 5, destination-PE / Hurdle tolerance thresholds
- Rule 6, downstream signal candidates against B09 and stage 11 catalysts
- Rule 7, method plurality (Section 1A matrix, ≥2 methods, triangulation)
- Rule 9, Business Understanding Narrative (stage 13)
- Rule 10, Halt 1 dossier at the /finalize pass
- Rules 11-12, v3.8 exit construction and Amendment 19 FV path
- Rules 13-14, Expectation Ledger and the two hard gates

No valuation framework document was loaded. `recomputed_destination_pe` and
`recomputed_decision` are blank because no valuation exists to recompute.

---

## PART 4 — SUMMARY

**Rules checked: 57. Passed: 47. Failed: 10 (0 CRITICAL, 1 MAJOR, 9 MINOR).
Phase-1 acceptance rate: 82%.** Above the 60% REWORK floor.

**The one finding that moves a number: F-GATE0-01.** A1 was scored 3 where the
prompt's band table says 1. Block A recomputes 9 → 7, core 56 → 54, grand total
75 → 73, and deal-breaker 1 flips to triggered-but-non-binding.

**The decision is robust across every reading.** Applying all three scoring
findings together (A1 corrected down, B2 zeroed on the window rule, C2 restored
to the reported-PAT basis) puts the core score between 52 and 56. Every value in
that envelope sits inside the matrix's 40-59 row. Classification **AVERAGE** in
all readings, moat class **STRONG** in all readings, Emerging Moat **MODEST (24)**
untouched, combined **AVERAGE** untouched.

**What the two stages got right and it is worth naming.** The NOT FOUND
discipline held under pressure at exactly the two places it usually breaks: E3
promoter pledge, where the stage wrote out the reason nil is the likely truth and
still scored 0; and Section 1C, where the absent product-mix split is named as
the scan's central gap rather than proxied from the end-market split. B07's
evidence tiering held every deck-only claim at 🎙️ and produced a genuinely
sparse scan (0 Strong rows, 24.4 of a 92 ceiling) with the one-point UA shortfall
reported rather than rounded through. Neither stage shaded a number to reach a
conclusion.

---

```yaml
stage: B12c
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation audit deferred to phase 3"
gate0:
  rules_checked: 29
  fails:
    - "F-GATE0-01 (MAJOR): A1 median ROCE 13.68% scored 3; prompt band 10-14.9 = 1. Block A 9 -> 7, core 56 -> 54, grand 75 -> 73, deal-breaker 1 flips to triggered-non-binding. Classification AVERAGE unchanged."
    - "F-GATE0-02 (MINOR): ex-exceptional restatement of FY26 PAT/EBIT is outside the fixed formula set; disclosed and conservative. On the literal formula C2 = 4, Block C = 13."
    - "F-GATE0-03 (MINOR): B2 scored on a 2-year FCF window, below the prompt's 3-year minimum; strict rule-5 reading gives B2 = 0, Block B = 3."
    - "F-GATE0-04 (MINOR): deal_breakers[] entry omits the driving years the prompt requires; years appear only in flags and narrative."
    - "F-GATE0-05 (MINOR): PEER DATA NEEDED items for M2/M5 recorded in input_gaps, not data_notes as the schema directs."
    - "F-GATE0-06 (MINOR): six approximate tilde page anchors (p.~13, p.~30, p.~108, p.~122, p.~208, p.~232) against the prompt's exact-page anchor form."
emoat:
  rules_checked: 28
  fails:
    - "F-EMOAT-01 (MINOR): Section 3 strength tally states 9 Weak; actual 11. Tally sums to 21-22 against 23 rows. Correct: 4 Moderate / 11 Weak / 8 None (G2 inside the 8). No score effect."
    - "F-EMOAT-02 (MINOR): recount line hedged ('approximately 34') and labels 13 as non-zero-scored categories; non-zero rows are 15, 13 being the 📄-carrying subset. Guard remedy was nonetheless performed."
    - "F-EMOAT-03 (MINOR): evidence_mix.claim = 4 against 5 distinct 🎙️ items in the report (TFT, LCD, BorgWarner, ECU MoU, 4W showcase)."
    - "F-EMOAT-04 (MINOR): three anchors use extraction line offsets or an out-of-range page (p.1306-1311, L14968, L10410-10411) instead of the mandated (AR p.__) form."
valuation:
  rules_checked: 0
  status: "PENDING PHASE 3 - stages 10 and 11 do not exist for this run; no valuation framework document loaded"
  fails: []
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: ["PENDING PHASE 3 - stage 11 not run"]}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["PENDING PHASE 3 - stage 13 not run"]}
recomputed_destination_pe: ""
recomputed_decision: ""     # concur: Gate 0 AVERAGE and EM MODEST stand; core score recomputes 56 -> 54, same 40-59 band
findings:
  - {severity: "MAJOR", location: "B01 reports/01-gate0.md L60; blocks/B01-gate0.yaml blocks.A, core_score, grand_total", description: "A1 median ROCE 13.68% scored 3. prompts/01-gate-0-pipeline.md [BLOCK A] band table: '15-19.9 = 3 | 10-14.9 = 1'. Correct score 1. Block A 9 -> 7, core 56 -> 54, grand total 75 -> 73. Deal-breaker 1 (Block A <8 -> max GOOD) flips from NOT TRIGGERED to TRIGGERED, non-binding at AVERAGE. Classification AVERAGE unchanged."}
  - {severity: "MINOR", location: "B01 reports/01-gate0.md L41-44, L207-218; data_notes[1]", description: "prompts/01 rule 2 ('No qualitative judgments. Only numbers and the scoring rules provided') and 'FORMULA DEFINITIONS (fixed, do not substitute alternatives)'. FY26 PAT/EBIT restated ex the Rs 15.21cr exceptional gain, which the prompt does not define. Cited operator instruction NOT FOUND in the artifacts held. Disclosed, both bases printed, and it lowers the score: on the literal formula C2 = 4 and Block C = 13."}
  - {severity: "MINOR", location: "B01 reports/01-gate0.md L142-155", description: "prompts/01 rule 6 ('minimum 3 years') with rule 5 ('mark N/A and score it 0'). B2 scored 2 on a 2-year FCF window. Strict reading gives B2 = 0 and Block B = 3. Window disclosed and flagged LIMITED."}
  - {severity: "MINOR", location: "B01 blocks/B01-gate0.yaml deal_breakers[0]", description: "prompts/01 'CLASSIFICATION AND OVERRIDES' requires 'state WHICH years drive any deal-breaker'. The deal-breaker entry names no years; FY26 and FY24-FY26 appear only in flags, block_b_trend and narrative."}
  - {severity: "MINOR", location: "B01 blocks/B01-gate0.yaml data_notes vs input_gaps[6]", description: "prompts/01 YAML schema comment: 'data_notes: [] # ... PEER DATA NEEDED items'. M2 and M5 PEER DATA NEEDED recorded under input_gaps instead. No scoring effect; both scored 0 correctly."}
  - {severity: "MINOR", location: "B01 reports/01-gate0.md L72, L241, L259, L263, L345", description: "prompts/01 rule 4 mandates an exact page/note anchor form. Six anchors use approximate tilde pages, including E1 promoter holding and E4 net worth."}
  - {severity: "MINOR", location: "B07 reports/07-emoat.md L459-460; blocks/B07-emoat.yaml completionist_recount", description: "prompts/07 Section 3 requires the summary table's strength counts. Filed '4 Moderate, 9 Weak, 8 None/0, plus one explicit negative (G2)' sums to 21-22 against 23 rows. Recount: 4 Moderate, 11 Weak, 8 None with G2 inside the 8. Scorecard total computed from the table, so no score moves."}
  - {severity: "MINOR", location: "B07 reports/07-emoat.md L462-471", description: "prompts/07 rule 6 mandates '📄 recount performed: [n] documented items across [m] categories'. Filed count hedged as 'approximately 34' and [m] labelled '13 non-zero-scored categories' where non-zero rows number 15 (13 being the 📄-carrying subset). The guard trigger ('12 or more categories as active') arguably fired on 15 non-zero rows; the required 📄 recount was performed and no tier inflation was found on independent row-by-row check."}
  - {severity: "MINOR", location: "B07 blocks/B07-emoat.yaml evidence_mix", description: "prompts/07 YAML schema 'evidence_mix ... # item counts'. claim = 4 against 5 distinct 🎙️ items in the report (TFT cluster, coloured LCD cluster, BorgWarner licence, unnamed ECU MoU, 4W tech showcase). inference = 1 correct. No score effect: multipliers are applied per row."}
  - {severity: "MINOR", location: "B07 reports/07-emoat.md L79, L326, L390", description: "prompts/07 rule 3 mandates '(AR p.__), (Q_ FY__ call), (Inv. Pres. slide __)'. Three items anchor to extraction line offsets or an out-of-range page: p.1306-1311 (mid-pressure sensors), extracted L14968 (attrition, F1), extracted L10410-10411 (ZLD, H3)."}
critical_count: 0
major_count: 1
minor_count: 9
acceptance_rate: 82            # 47 of 57 phase-1 rules passed; gate0 79% (23/29), emoat 86% (24/28)
```
