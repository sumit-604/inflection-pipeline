# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
Company: Finolex Cables Ltd (FINCABLES) | Run date: 2026-08-12 | Model: claude-opus-4-8

SCOPE NOTE: This is a PHASE 1 run. Only the Gate 0 (B01) and Emerging Moat (B07)
framework-compliance checks are executed. The valuation-adherence audit (B11
valuation, B10 assembly) is DEFERRED to Phase 3 — those artifacts do not exist yet.
The `valuation` YAML section below is marked `pending-phase-3`.

Method: rule application only. I re-derived every Gate 0 block score from the stated
inputs against prompts/01-gate-0-pipeline.md thresholds, and re-computed the full
21-row Emerging Moat scorecard against prompts/07-emerging-moat-pipeline.md. I do not
re-verify whether the underlying numbers exist in the source PDFs — that is Verifier
A's non-overridable domain. I audit whether the frameworks were applied AS WRITTEN.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (thresholds re-applied)

| Rule | Stated input | Band applied | Recomputed | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | median 17.95% (5th+6th of 10 = (17.44+18.46)/2) | 15-19.9 → 3 | 17.95% → 3 | PASS |
| A2 Min single-yr ROCE | 14.84% (FY23) | 12-14.9 → 3 | 14.84 <15, in 12-14.9 → 3 | PASS |
| A3 Median ROE | median 14.19% ((13.99+14.38)/2) | 12-14.9 → 2 | 14.19% → 2 | PASS |
| A4 ROCE trend | 15.24% vs 23.71% = -8.47pp | >5pp decline → 0 | -8.47pp → 0 | PASS |

Block A = 8/20. Median arithmetic (5th/6th element average on a 10-element series)
correct. Band edges honoured (A2: 14.84 is <15, correctly excluded from the ≥15 tier).

### Block B — Cash Generation Quality

| Rule | Stated input | Band applied | Recomputed | Verdict |
|---|---|---|---|---|
| B1 Cum CFO/PAT | ΣCFO 2,688.26 / ΣPAT 5,159.88 = 0.521 | 0.50-0.69 → 1 | ΣCFO 2,688.26, ΣPAT 5,159.88, 0.5210 → 1 | PASS |
| B2 FCF-positive yrs | 7/9 computable = 77.8% | 75-99 → 4 | 7/9 = 77.8% → 4 | PASS |
| B3 Cum FCF/PAT | ΣFCF 1,548.65 / ΣPAT(FY18-26) 4,759.64 = 0.325 | 0.20-0.39 → 1 | 0.3254 → 1 | PASS |
| B4 ΔWC Days | Trade Payables absent → N/A | missing data → 0 | N/A, scored 0 per Rule 5 | PASS |

Block B = 6/20. Both cumulative sums reproduce to the penny. B3 correctly matches the
FCF window (FY18-26) to the PAT window rather than dividing FY18-26 FCF by 10-year PAT
— a common trap the maker avoided. B4 handled as data-absence-scored-0, not estimated.

### Block C — Growth

| Rule | Stated input | Band applied | Recomputed | Verdict |
|---|---|---|---|---|
| C1 Rev CAGR (9yr) | (6,321.01/2,444.84)^(1/9)-1 = 11.13% | 10-14.9 → 3 | 11.13% → 3 | PASS |
| C2 PAT CAGR (9yr) | (713.72/400.24)^(1/9)-1 = 6.64% | 5-9.9 → 1 | 6.64% → 1 | PASS |
| C3 Positive YoY yrs | 7/9 = 77.8% | 75-99 → 3 | 7/9 = 77.8% → 3 | PASS |
| C4 PAT-Rev CAGR gap | 6.64 - 11.13 = -4.49pp | -3 to -8pp → 1 | -4.49pp → 1 | PASS |

Block C = 8/20. CAGR edge rules honoured: no negative/zero endpoints, no loss-to-profit
swing (PAT positive all 10 years), so no N/M treatment needed and none applied — correct.

### Block D — Balance Sheet Strength

| Rule | Stated input | Band applied | Recomputed | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | 19.14 - 168.12 = -148.98 net cash | net cash → 5 | net cash → 5 | PASS |
| D2 Interest Coverage | 930.27 / 1.75 = 531.6x | ≥10x → 5 | 531.6x → 5 | PASS |
| D3 Debt/Equity | 19.14 / 6,085.88 = 0.003x | <0.1 → 5 | 0.003x → 5 | PASS |
| D4 Current Ratio | no current split → N/A | missing data → 0 | N/A, scored 0 per Rule 5 | PASS |

Block D = 15/20. Correct.

### Block E — Shareholder Alignment (DATA-ABSENCE handling — audited closely)

E1-E4 all scored 0 on "N/A (not in provided data)". Framework Rule 5 is explicit:
absent data points are marked N/A and scored 0, never estimated. **This is the correct
handling, not a misapplication.** The maker additionally (a) flagged Block E 0/20 as a
pure data-absence outcome rather than a measured governance weakness, and (b) raised
FLAG-GATE0. Both are consistent with CLAUDE.md ("flags propagate; only mechanical
failures halt"). Block E = 0/20. PASS.

Note (not a fail): the report also presents an ex-Block E view (37/80 = 46.3%, AVERAGE
tier) as a CAVEAT. The official `core_score` remains 37/100 and the official
`classification` remains AVOID. The framework has no provision to drop a block from the
denominator, and the report does not do so in the scored output — it keeps AVOID and
uses the ex-Block E figure only as narrative transparency. Compliant.

### Block F — Quantitative Moat (12 tests)

| Test | Band logic | Recomputed | Verdict |
|---|---|---|---|
| M1 Pricing Power | EBITDA margin -6.4pp (>5pp) → outside "declined 2-5pp" band → else 0 | 0 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 7.44x (>2x) AND ROCE 15.24% (>15%) → tier-3 | 3 | PASS |
| M4 Customer Stickiness | 2 decline yrs, CAGR positive → 1 | 1 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 Technology/R&D | no R&D line, cannot meet ≥1% → else 0 | 0 | PASS |
| M7 Regulatory/License | unregulated segment → 0 | 0 | PASS |
| M8 Distribution | quantified+growing but rev/outlet unverifiable & CAGR 11.1%<15% → 1 | 1 | PASS (see MINOR) |
| M9 Brand | PEER DATA NEEDED → 0 (GM proxy informational only) | 0 | PASS |
| M10 Switching Costs | overall growth, 2 decline yrs → 1 | 1 | PASS |
| M11 Network Effects | latest 3yr 12.14% not > prior 15.93%, neither ≥20%, 12.14%<15% → 0 | 0 | PASS |
| M12 Negative WC/Float | Trade Payables absent → N/A → 0 | 0 | PASS |

Block F = 6/60. Data-absence zeros (M2, M5, M9) correctly use "PEER DATA NEEDED → 0"
exactly per the Block F instruction ("If a test needs peer data that is not provided,
score 0 and mark PEER DATA NEEDED, never guess"). This is the correct distinction
between missing-data zero and measured-weakness zero. M3's tier-3 boundary is a genuine
edge (ROCE 15.24 vs >15 threshold) and is correctly on the pass side. M11's boundary
logic (band-1 requires >15% latest growth; 12.14% fails) correctly resolves to 0.

M8 — MINOR: scored 1 on a ~6-year-stale FY2019-20 AR distribution narrative (5,000+
distributors; retailers 30k→50k) with no current FY26 confirmation. A stricter reading
would score 0 for lack of current evidence. The maker scored conservatively (1, not the
tier-3 "network growing AND rev CAGR ≥15%" it explicitly rejected) and flagged the
staleness in data_notes. Within tolerance; noted, not a decision-mover.

### Classification, Data Confidence, Deal-Breakers

- Core = 8+6+8+15+0 = 37/100. Moat = 6/60. Grand total = 43/160. Arithmetic PASS.
- Moat class: 1 test ≥3 (M3 only) → THIN, per "1 = THIN". PASS.
- Data confidence: 10 years = "10+ yrs full" → no downgrade. `history_downgrade: false`. PASS.
- Classification matrix: Core <40 → AVOID. 37 < 40 → AVOID (moat class does not lift the
  tier). **Recomputed classification = AVOID. Concur.** PASS.
- Deal-breakers (all 9 re-tested):
  1. Block A <8 → A=8, NOT triggered (8 is not <8). PASS.
  2. Block B <8 → B=6, TRIGGERED, cap "max GOOD" — non-binding (already AVOID). PASS.
  3. Median ROCE <10% → 17.95%, no. PASS.
  4. Cum CFO/PAT <0.50 → 0.521, no (near-miss correctly reported as above threshold). PASS.
  5. Pledge >15% → data absent, correctly not asserted as triggered. PASS.
  6. ND/EBITDA >3x AND IC <3x → net cash, no. PASS.
  7. Revenue declined majority → 2/9, not majority. PASS.
  8. PAT negative in last 3 yrs → positive FY24-26, no. PASS.
  9. History <3 yrs → 10 yrs, no. PASS.

  Deal-breaker caps are ceilings that lower, never raise; with classification already at
  AVOID the triggered #2 cap is correctly noted non-binding. Framework logic applied
  correctly.

- FLAG-GATE0: framework requires the flag when classification ≤ AVERAGE with historical
  depressors identified. AVOID + identified depressors (A4, M1, B1/B3) → flag raised. PASS.

**GATE 0 VERDICT: fully compliant. 44 of 45 checked rules PASS; 1 MINOR (M8 stale-data
scoring). No MAJOR/CRITICAL. Recomputed classification AVOID reproduces the maker's.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category completeness

All 21 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1) appear in
the Section 3 summary table AND the Section 5 scorecard, each either scored or marked NO
EVIDENCE FOUND. PASS.

### Scorecard re-computation (raw = likelihood×impact matrix, × evidence factor)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Factors: 📄 1.0, 🎙️ 0.7, 🔍 0.5.

| # | L×I | raw | factor | recomputed | maker | Verdict |
|---|---|---|---|---|---|---|
| A1 | MH | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| A2 | none | 0 | — | 0 | 0 | PASS |
| A3 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| A4 | LL | 1 | 🎙️ 0.7 | 0.7 | 0.7 | PASS |
| B1 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| B2 | MM | 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |
| B3 | none | 0 | — | 0 | 0 | PASS |
| C1 | LL | 1 | 🔍 0.5 | 0.5 | 0.5 | PASS |
| C2 | none | 0 | — | 0 | 0 | PASS |
| D1 | none | 0 | — | 0 | 0 | PASS |
| D2 | none | 0 | — | 0 | 0 | PASS |
| E1 | none | 0 | — | 0 | 0 | PASS |
| E2 | ML | 1 | 📄 1.0 | 1.0 | 1.0 | PASS |
| F1 | none | 0 | — | 0 | 0 | PASS |
| F2 | MM | 2 | 📄 1.0 | 2.0 | 2.0 | PASS (see MINOR) |
| G1 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| G2 | none | 0 | — | 0 | 0 | PASS |
| H1 | none | 0 | — | 0 | 0 | PASS |
| H2 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| H3 | none | 0 | — | 0 | 0 | PASS |
| R1 | MM | 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |

**Recomputed adjusted total = 22.0** (3.0+3.0+0.7+3.0+1.4+0.5+1.0+2.0+3.0+3.0+1.4).
Matches the maker's 22.0 exactly. Banding: 12-24 → MODEST MOAT DEVELOPMENT. **Recomputed
classification = MODEST. Concur.** PASS.

### Evidence-tier discipline (the key EM audit: no 🎙️-only category scored as 📄)

Checked every 1.0-factor row for the "🎙️-only scored as 📄" failure mode:
- A1 (1.0): anchored on the preform plant COMMISSIONED mid-March 2026 (📄); the "second
  domestic maker" rarity assertion is 🎙️ but is not the scored fact. Documented core → 1.0 OK.
- A3 (1.0): e-beam facility commissioned and product in market (📄). OK.
- B1 (1.0): preform commissioned (📄) is the scored anchor; fibre-draw is mixed but the
  backward-integration capability itself is documented. OK.
- E2 (1.0): export revenue actuals ₹30cr→₹52cr (📄); the 2-3% target is 🎙️ but scored on
  achieved growth. OK.
- F2 (1.0): dated concall statements are on-record (📄). OK — but see MINOR below.
- G1 (1.0): near-zero-borrowings balance sheet (📄). OK.
- H2 (1.0): Sumitomo JV FY26 revenue/PBT/order-book disclosed (📄); TAM is 🎙️ but not
  scored. OK.

Conversely, categories resting on claims are correctly discounted: B2 and R1 (🎙️ → 0.7),
A4 (🎙️ → 0.7), C1 (stale → 🔍 0.5). No inflation of claim/inference to documented found.
The discipline holds. PASS.

MINOR (F2 / B05): The framework instructs F2 to "cross-reference the injected concall
promise-delivery record" (B05). Stage 5 did not run in this configuration, so B05 was not
available. The maker SELF-DERIVED F2 from the four FY26 transcripts, flagged this
explicitly in the document base note and in input_gaps, and scored MM (raw 2) reflecting
the genuinely mixed record (one clean delivery, one JV turnaround, two repeatedly-slipped
capex programs). This is a transparent input-gap workaround, not a fabrication; the 📄
factor is defensible because the underlying dated statements are on record. Deviation from
the intended cross-reference is real but properly disclosed and does not move the score
beyond tolerance. MINOR.

MINOR (mixed-evidence resolution): A1, B1 and H2 are labelled 📄/🎙️ in the summary table
yet each takes the full 1.0 documented factor. Each is individually justified by a
documented core fact (commissioned plant, commissioned plant, disclosed JV financials), so
no single row is wrong; noted only because three consecutive mixed rows all resolving to
1.0 is the pattern the completionist guard exists to police. The maker's own recount
addresses this (below). MINOR / observation.

### Completionist guard

Active (Strong/Moderate) categories = 7 (A1, A3, B1, B2, F2, G1, H2). Base rate 3-6; the
hard guard triggers at ≥12. 7 < 12, so no forced re-examination is mandatory, but the
maker performed the 📄 recount anyway: "9 documented items across 6 categories," concentrating
the above-base-rate excess in genuinely documented capex/financial facts rather than claims.
The recount is present and substantive, exactly as the instruction requires. PASS.

### FTTCP separation

The report header and taxonomy note state explicitly that this is the Emerging Competitive
Advantages scan (A1-R1, ~0-80 scale) and "is NOT FTTCP... FTTCP is a separate synthesis
inside the Stage 11 valuation framework and is not touched here." No FTTCP naming or logic
bleeds into the scan. Separation maintained per the CLAUDE.md NEVER rule. PASS.

### Section 2C capex-embedded-growth & combined classification

- 2C: ₹300cr × blended FAT 7.6x ≈ ₹2,280cr ≈ 36% of FY26 revenue; `capex_embedded_growth_pct:
  36` carried per instruction, with an explicit "be skeptical" caveat that the honest
  bottom-up read is ~₹250cr (~4%). Mechanical calc shown + skepticism rule (Rule 4) honoured. PASS.
- 6D combined: AVOID (ex-Block E AVERAGE) backward + MODEST forward → does not meet HIGH
  POTENTIAL/TURNAROUND (both need STRENGTHENING/EXPANSION forward) and does not meet
  GOOD/GOOD+ (moat count 1, THIN) → AVERAGE. Matrix logic applied correctly. PASS.

**EMERGING MOAT VERDICT: compliant. Recomputed total 22.0 and MODEST classification
reproduce the maker's exactly. 25 of 27 checked rules PASS; 2 MINOR (F2/B05 self-derivation,
mixed-evidence 1.0 resolution). No MAJOR/CRITICAL.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) / ASSEMBLY (B10)
═══════════════════════════════════════════════════════════════════

DEFERRED to Phase 3 per task scope. Artifacts do not yet exist. Not audited here.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

Gate 0 and the Emerging Moat scan were both applied as written. Every Gate 0 block score,
the moat classification, the classification matrix, the data-confidence rule, and all nine
deal-breakers reproduce exactly on independent re-derivation; the AVOID classification is
confirmed. The Emerging Moat 21-row scorecard re-computes to 22.0 → MODEST, matching the
maker, with correct evidence-tier discipline (no claim inflated to documented), a performed
completionist recount, and clean FTTCP separation. Data-absence zeros (Block E, M2/M5/M9,
B4, D4, M12) are all handled per the framework's missing-data rule (mark N/A, score 0, never
estimate) and are correctly distinguished from measured weakness in the narrative and flags.

No CRITICAL or MAJOR framework misapplications. Three MINOR items, none decision-moving:
1. [Gate 0, MINOR] M8 Distribution scored 1 on ~6-year-stale FY2019-20 AR data.
2. [EM, MINOR] F2 execution moat self-derived (B05 unavailable); disclosed workaround.
3. [EM, MINOR] Three mixed 📄/🎙️ categories (A1, B1, H2) all take the full 1.0 factor;
   each individually justified.

Framework adherence for the audited (Gate 0 + EM) portion: ~96%. Recomputed Gate 0
classification (AVOID) and EM classification (MODEST) both CONCUR with the maker.

```yaml
stage: B12c
company: "FINCABLES"
run_date: "2026-08-12"
model: claude-opus-4-8
status: complete
phase: 1
scope: "gate0 + emerging-moat only; valuation deferred to phase 3"
gate0:
  rules_checked: 45
  fails:
    - {severity: "MINOR", rule: "M8 Distribution", note: "scored 1 on ~6-year-stale FY2019-20 AR distribution narrative with no current FY26 confirmation; conservative and flagged, within tolerance"}
emoat:
  rules_checked: 27
  fails:
    - {severity: "MINOR", rule: "F2 execution moat", note: "self-derived from four FY26 transcripts because B05 promise-delivery record unavailable (Stage 5 did not run); framework intends F2 to cross-reference injected B05; disclosed workaround, score within tolerance"}
    - {severity: "MINOR", rule: "evidence-factor resolution (A1/B1/H2)", note: "three mixed documented/claim categories each take the full 1.0 documented factor; each individually justified by a documented core fact"}
valuation: {status: pending-phase-3}
recomputed_destination_pe: ""   # n/a in phase 1 (valuation deferred)
recomputed_decision: ""         # concur: Gate 0 = AVOID, EM = MODEST both reproduce
framework_adherence: 96         # % for the Gate 0 + EM portion only
findings:
  - {severity: "MINOR", location: "B01 Block F / M8", note: "moat score of 1 rests on ~6yr-stale AR distribution data; flagged by maker"}
  - {severity: "MINOR", location: "B07 Section 3 / F2", note: "F2 self-derived without B05; transparent input-gap workaround"}
  - {severity: "MINOR", location: "B07 Section 5 / A1,B1,H2", note: "mixed-evidence rows all resolved to 1.0 documented factor; each defensible"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 96             # rules passed (69) / rules checked (72), %
```
