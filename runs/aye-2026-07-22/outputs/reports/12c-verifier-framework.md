# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)
## Aye Finance Limited (AYE) | Run date: 2026-07-22 | Model: claude-opus-4-8

**SCOPE — PHASE 1 ONLY.** This audit covers Gate 0 (B01) and the Emerging
Moat scan (B07) only. The valuation-adherence audit (B11 / B10, Section 1B
pillars, Hurdle Ratio, UA multiplier, destination/exit PE, fair value) is
DEFERRED to PHASE 3 and is NOT run here — B10 and B11 do not yet exist in
this run. No exit PE, destination PE, or fair value is recomputed or
opined on below. The `valuation` section of the emitted YAML is marked
`pending: phase-3`.

**Method.** Fresh context. I re-derived every Gate 0 block score from the
stated inputs against the thresholds in `prompts/01-gate-0-pipeline.md`, and
re-computed every Emerging Moat scorecard row against the raw-matrix and
evidence-multiplier rules in `prompts/07-emerging-moat-pipeline.md`. I audit
RULE APPLICATION, not raw source fidelity (Verifier A owns whether a number
appears in a PDF) and not company quality. Per the task framing: AYE is a
lending NBFC, so I judge whether each documented metric SUBSTITUTION
(ROA/ROE for ROCE, CRAR/PCR for ND-EBITDA/interest cover, LCR for current
ratio, GNPA/dpd as the lender analog, N/A for inventory/receivables/
EV-EBITDA) is reasonable AND named — not whether the manufacturing metric
was literally used. A reasonable, disclosed lender-substitution is not a
deviation.

Artifacts audited:
- `runs/aye-2026-07-22/outputs/reports/01-gate0.md`
- `runs/aye-2026-07-22/outputs/reports/07-emoat.md`

Authorities: `prompts/01-gate-0-pipeline.md`,
`prompts/07-emerging-moat-pipeline.md`, `CLAUDE.md` NEVER-rules,
`frameworks/Master_Project_Prompt_v3.3.md` (Role 1 scope).

---

## PART 1 — GATE 0 (B01) RULE-BY-RULE

### Block A — Return on Capital (ROA/ROE substitute for ROCE), Max 20

| Line | Rule (prompt band) | Reported input | Correct band | Reported score | Recompute | Verdict |
|---|---|---|---|---|---|---|
| A1 | Median ROCE <10 = 0 | ROA 2.94% (named substitute) | <10 → 0 | 0 | 0 | PASS |
| A2 | Min single-yr ROCE <8 = 0 | ROA 1.28% (FY23 closing-only) | <8 → 0 | 0 | 0 | PASS |
| A3 | Median ROE <12 = 0 | ROE 10.68% | <12 → 0 | 0 | 0 | PASS |
| A4 | latest ≥ earliest = 5 | ROA +1.47pp / ROE +3.96pp FY26 vs FY23 | latest ≥ earliest → 5 | 5 | 5 | PASS |

Block A = 5/20. Recompute = 5. **PASS.** ROCE→ROA substitution named at the
line and in the adaptation header; A3 uses framework-native ROE. Both are
legitimate NBFC substitutions.

### Block B — Cash Generation Quality, Max 20 (INDETERMINATE)

| Line | Rule | Reported value | Correct band | Score | Verdict |
|---|---|---|---|---|---|
| B1 | Cumul CFO/PAT <0.50 = 0 | −7.25x | <0.50 → 0 | 0 | PASS |
| B2 | FCF-pos years <50% = 0 | 0/4 = 0% | <50 → 0 | 0 | PASS |
| B3 | Cumul FCF/PAT <0.20/neg = 0 | −7.33x | negative → 0 | 0 | PASS |
| B4 | Change in WC days | N/A (no trade receivables/inventory for a lender) | — | 0 (N/A) | PASS |

Cumulative CFO cross-check: −(720.39+1322.83+811.78+1354.64) = −4,209.64;
cumulative PAT = 39.87+171.68+175.25+193.63 = 580.43; −4,209.64 ÷ 580.43 =
−7.25x. Ties. Block B = 0/20. **PASS.** The INDETERMINATE label and the
CLAUDE.md cap ("caps downstream verdict at PROCEED WITH CAVEATS minimum,
named explicitly") are correctly invoked — B1-B3 apply the literal formula
(0), and the structural Ind AS 7 disbursement-outflow explanation is
carried as context, not as a silent PROCEED. Complies with the "never let
INDETERMINATE cash conversion silently resolve to PROCEED" NEVER-rule.

### Block C — Growth, Max 20

| Line | Rule | Reported value | Correct band | Score | Verdict |
|---|---|---|---|---|---|
| C1 | Rev CAGR ≥20 = 5 | 42.8% | ≥20 → 5 | 5 | PASS |
| C2 | PAT CAGR ≥20 = 5 | 69.4% | ≥20 → 5 | 5 | PASS |
| C3 | Positive YoY rev 100% = 5 | 3/3 = 100% | 100 → 5 | 5 | PASS |
| C4 | PAT−Rev CAGR ≥+3pp = 5 | +26.6pp | ≥+3 → 5 | 5 | PASS |

CAGR cross-check: Rev (1814.73/623.43)^(1/3)−1 = 42.8%; PAT
(193.63/39.87)^(1/3)−1 = 69.4%. Both endpoints positive, so the CAGR edge
rule (negative endpoint → N/M) does not bind — correctly not invoked. Block
C = 20/20. **PASS.** The restated-vs-audited PAT basis mix is disclosed in
`data_notes` (both endpoints natively anchored), satisfying the "never
estimate" rule.

### Block D — Balance Sheet Strength (CRAR/PCR/LCR substitutes), Max 20

| Line | Rule (with NBFC carve-out) | Reported value | Correct band | Score | Verdict |
|---|---|---|---|---|---|
| D1 | NBFC: CAR ≥18% = 5 | CRAR 42.38% | ≥18 → 5 | 5 | PASS |
| D2 | NBFC: PCR 60-70 = 3 | PCR 63.80% | 60-70 → 3 | 3 | PASS |
| D3 | Financials: default 3 | D/E 2.22x, default applied | default → 3 | 3 | PASS |
| D4 | Current ratio ≥2.0 = 5 (LCR substitute) | LCR 269.61% | ≥2.0x-equiv → 5 | 5 | PASS |

Block D = 16/20. **PASS.** D1 (CRAR) and D2 (PCR) are the prompt's own
explicit Banks/NBFC carve-outs — literal compliance, not improvisation. D3
applies the prompt's literal "Financials: default 3." D4 (LCR for current
ratio) is a NON-framework-specified substitute and is named as such at the
line and header; 269.61% mapping to the ≥2.0x band is a reasonable, disclosed
lender analog. Substitution discipline satisfied.

### Block E — Shareholder Alignment (no-promoter adaptation), Max 20

| Line | Rule | Reported value | Applied band | Score | Verdict |
|---|---|---|---|---|---|
| E1 | Promoter ≥60=5 … 30-39.9=1; prof-managed 3 if FII+DII>50% | FII+DII 35.45% (proxy) | 35.45% <50% carve-out fails; analog to 30-39.9 band → 1 | 1 | PASS |
| E2 | Promoter change over 3yr | N/A — listed Feb-2026, no 3yr window | — | 0 (N/A) | PASS |
| E3 | Pledge 0% = 5 | 0% (no promoter to pledge) | 0% → 5 | 5 | PASS |
| E4 | Cont. liab / NW <5% = 5 | 0.92% | <5 → 5 | 5 | PASS |

Block E = 11/20. **PASS.** E1 handling is correct: the >50% FII+DII
"professionally managed → 3" carve-out is tested and legitimately fails
(35.45% < 50%), so the fallback to the promoter-band analogy is the right
path, not an arbitrary score. The CLAUDE.md NEVER-rule ("never treat low
institutional ownership as a risk … UA multiplier not triggered") is
explicitly honoured — E1's low mechanical score is flagged as a band-fit
artefact, not an alignment concern, and no UA penalty is applied. E2 N/A→0
is the conservative floor and does not inflate.

**Core Score = 5 + 0 + 20 + 16 + 11 = 52/100. Recompute = 52. PASS.**

### Block F — Quantitative Moat Scoring, Max 60

| Test | Rule outcome | Reported score | Verdict |
|---|---|---|---|
| M1 Pricing Power | margin +5.18pp (≥2pp) AND rev CAGR 42.8% (≥10%) → 5 | 5 | PASS |
| M2 Cost adv. | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Capital eff. | N/A (no FAT for a lender) → 0 | 0 | PASS |
| M4 Cust. stickiness | receivable-days N/A; not double-counted with GNPA → 0 | 0 | PASS |
| M5 Scale/dominance | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 Tech/R&D | PEER DATA NEEDED (no anchored R&D/Rev) → 0 | 0 | PASS |
| M7 Regulatory | player count PEER DATA NEEDED → 0 | 0 | PASS |
| M8 Distribution | reach quantified but no anchored growth trend → conservative 1 | 1 | PASS |
| M9 Brand | PEER DATA NEEDED → 0 | 0 | PASS |
| M10 Switching | receivable-days N/A, not double-counted → 0 | 0 | PASS |
| M11 Network | <6yr; selling% not broken out; scored conservatively → 1 | 1 | PASS |
| M12 Neg WC/float | N/A for a lender → 0 | 0 | PASS |

Moat score = 5+1+1 = 7/60. Moats present (≥3): M1 only = 1 → **THIN**
(prompt: 1 = THIN). **PASS.** PEER DATA NEEDED items are scored 0, never
guessed — complies with the "never estimate a missing number" rule. M4/M10/
M12 N/A rulings correctly avoid re-using the Block D GNPA/dpd read, honouring
the "never credit one quality improvement through two mechanisms" NEVER-rule.

### Classification, deal-breakers, confidence downgrade

- **Grand total = 52 + 7 = 59/160.** PASS.
- **Classification matrix:** Core 52 falls in 40-59 → AVERAGE (flat
  regardless of moat class). Correctly stated. PASS.
- **Deal-breakers:** #1 Block A<8→GOOD (non-binding), #2 Block B<8→GOOD
  (non-binding), #3 median ROCE-substitute 2.94%<10%→AVERAGE (binding,
  non-differentiating; ROE 10.68% alternative disclosed), #4 cumul CFO/PAT
  −7.25x<0.50→AVERAGE (binding). #5-9 correctly not triggered (no pledge,
  no ND/EBITDA+IC breach, no revenue-decline majority, no negative PAT,
  history 4yr ≥3). All applied per the stated rules, WHICH-years disclosed
  (all four FY23-FY26). PASS.
- **History-length / confidence downgrade — the primary audit focus:**
  data_years = 4 → prompt's "3-4 LIMITED, downgrade classification one
  tier" → AVERAGE → **AVOID**. This is applied on the DATA-LENGTH rule
  ALONE. It is NOT conflated with a transition/recovery depressor: the
  report frames the downgrade purely as listing-recency (IPO Feb-2026, four
  FY periods by construction) and explicitly separates it from
  fundamental deterioration and from the asset-quality/transition context.
  The sequence (matrix → deal-breaker caps → one-tier confidence downgrade)
  is correct. **PASS — no conflation.**
- **Final classification: AVOID**, propagated as FLAG-GATE0, not a halt.
  Complies with the "no STOP verdict / flags propagate, only mechanical
  failures halt" NEVER-rule.

**GATE 0 RESULT: 13 rules checked, 0 fails. Every block re-derives to the
reported score; every substitution is reasonable and named; the history
downgrade is DATA-LENGTH-only with no transition/recovery double-count.**

---

## PART 2 — EMERGING MOAT (B07) RULE-BY-RULE

### Category coverage (21 rows)

All 20 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3)
plus R1 are addressed or explicitly marked NO EVIDENCE FOUND / NOT
APPLICABLE in the Section 3 summary. Count = 21. **PASS.** N/A rulings on
manufacturing/supply-chain categories (A1, A4, B1, B2, E2, G2) are
reasonable for a balance-sheet lender and named; NO EVIDENCE FOUND used
where evidence is genuinely absent (A4, E1, H3), never force-fit.

### Scorecard recompute (raw L×I × evidence multiplier)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multiplier:
📄 1.0, 🎙️ 0.7, 🔍 0.5.

| Cat | Raw (stated) | Type | Mult | Reported adj | Recompute | Verdict |
|---|---|---|---|---|---|---|
| A3 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| B3 | 1 (ML) | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| C1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| D1 | 4 (HH) | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| F1 | 1 (LL) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| F2 | 1 (LL) | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| G1 | 4 (HH) | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| H1 | 1 (LL) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H2 | 1 (ML) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| R1 | 2 (HL) | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| others | 0 | — | — | 0 | 0 | PASS |

Sum = 3.0+1.0+3.0+4.0+0.7+0.5+4.0+0.7+0.7+2.0 = **19.6.** Recompute = 19.6.
**PASS.** Every raw→matrix mapping and every multiplier is correct.

- **Classification band:** 19.6 → 12-24 band → **MODEST MOAT DEVELOPMENT.**
  Correct. PASS.
- **Evidence-tier consistency (the "🎙️-only scored as 📄" test):** Each
  �-scored category (A3, B3, C1, D1, G1, R1) rests on filing/document
  evidence (Prospectus, Investor Presentation, ICRA letter). D1's dominant
  evidence is documented (70+ clusters, five named in-house models,
  underwriting split, cluster methodology) with only the AI/ML *tenure*
  specific flagged 🎙️ — the 1.0x multiplier is justified by the documented
  core, not the concall detail. F1/H1/H2 (🎙️) carry 0.7x, F2 (🔍) carries
  0.5x. No 🎙️-only or 🔍-only category is scored as if documented. PASS.
- **Completionist recount:** performed and stated — "20 documented items
  across 5 categories (D1, G1, C1, A3, R1)"; 4 Strong/Moderate categories,
  within the 3-6 base rate; 10 of 21 rows non-zero (< the 12-category
  re-examination trigger). Guard correctly applied. PASS.
- **Double-count discipline:** D2 (digital platform) scored 0 with an
  explicit note that its digitisation metrics are already credited under
  D1/A3 and its distinct platform (SwitchPe) already scored at B3 —
  correctly honours the "never credit one improvement through two
  mechanisms" NEVER-rule. G2 N/A mirrors the Gate 0 B4/M4/M10/M12 ruling.
  PASS.
- **C2 direction rule:** concentration is worsening (top-5 55.1%→57.0%),
  so the "improving" category correctly scores 0 and is carried as a risk,
  not forced positive. PASS.
- **capex_embedded_growth (2C) lender analog:** headroom (4.5×2,603) −
  5,557 = 6,156.5; 6,156.5 / 7,324 = 84%. Arithmetic ties. The
  borrowing-headroom-to-rating-ceiling substitution for the non-applicable
  "capex × FAT" calculation is named as a 🔍 analyst computation on 📄
  inputs and flagged as a mechanical ceiling, not a committed plan.
  Reasonable, disclosed. PASS.
- **evidence_mix {documented:20, claim:4, inference:2}:** item counts are
  consistent with the recount line and the 🎙️/🔍 category set. PASS
  (loose by construction, no inflation).
- **combined_assessment rule (6D):** = AVERAGE. Backward AVOID (flagged;
  core-implied AVERAGE pre-downgrade), Forward MODEST → not HIGH POTENTIAL
  or TURNAROUND (both require STRENGTHENING/EXPANSION forward), nets to
  AVERAGE. See the single MINOR observation below — the derivation is
  transparent and defensible, not a rule breach.

**EMERGING MOAT RESULT: 11 rules checked, 0 fails. Total re-derives to
19.6; band, multipliers, recount, tier-consistency, and double-count
discipline all correct.**

---

## PART 3 — OBSERVATIONS (non-fail)

**MINOR-1 — combined_assessment feeds the pre-downgrade backward tier.**
Location: 07-emoat.md Section 6D, lines 418-445; YAML `combined_assessment:
AVERAGE`. Section 6C is instructed to use the injected Gate 0 block, whose
`classification` is AVOID. The stage instead reasons through the
*core-implied* AVERAGE (pre-LIMITED-history downgrade) to avoid
double-penalising the same listing-recency issue Gate 0 already flagged
once, and lands combined = AVERAGE rather than AVOID. The standard combined
matrix in the prompt lists labels but does not fully specify the AVOID-
backward + MODEST-forward cell, so this is a genuine ambiguity resolved by a
transparent, reasoned judgment that is consistent with CLAUDE.md's
no-double-penalty posture. Not a deviation; recorded for the operator's
awareness because it is the one place the forward stage nudges the backward
tier upward. No score or number changes.

No CRITICAL or MAJOR findings. No fabricated inputs, no unnamed
substitutions, no PEER-DATA guesses, no history/transition conflation, no
double-crediting, no INDETERMINATE-to-PROCEED leak within the Gate0+EM
scope.

---

## PART 4 — VALUATION (B11/B10) — DEFERRED

Not audited. B10 and B11 do not exist in this run. Section 1B pillars,
FTTCP ROCE verdict, UA/Amendment-3 order, sector cap, dual-track fair
value, Hurdle Ratio, and destination/exit PE are all PHASE 3 scope. No exit
PE, destination PE, or fair value is recomputed here. `valuation` is emitted
as `pending: phase-3`; `recomputed_destination_pe` and `recomputed_decision`
are left blank by design.

---

## SUMMARY

- Gate 0 (B01): 13 rules checked, 0 fails. Every block re-derives exactly;
  history downgrade is DATA-LENGTH-only, not conflated with a
  transition/recovery depressor (primary audit focus — clean).
- Emerging Moat (B07): 11 rules checked, 0 fails. Score re-derives to 19.6;
  evidence-mix discipline and combined_assessment rule applied correctly
  (one transparent MINOR judgment noted).
- Lender substitutions (ROA/ROE, CRAR, PCR, LCR, GNPA analog, N/A rulings)
  are each reasonable and NAMED — none is a deviation.
- Framework adherence for the Gate0+EM scope: **CLEAN.**
- acceptance_rate = 24/24 rules passed = 100%.

```yaml
stage: B12c
company: "Aye Finance Limited (AYE)"
run_date: "2026-07-22"
model: claude-opus-4-8
status: complete
scope: "PHASE 1 - Gate 0 (B01) + Emerging Moat (B07) only; valuation (B10/B11) deferred to Phase 3"
gate0: {rules_checked: 13, fails: []}
emoat: {rules_checked: 11, fails: []}
valuation: {pending: phase-3}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "07-emoat.md Section 6D / YAML combined_assessment", note: "combined_assessment=AVERAGE derived from the pre-downgrade core-implied AVERAGE rather than the injected AVOID classification, to avoid double-penalising the LIMITED-history downgrade; transparent and defensible judgment on a matrix cell the prompt underspecifies. No number changes."}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 100
framework_adherence: "CLEAN for Gate0+EM scope: all block math re-derives, all NBFC substitutions named and reasonable, history downgrade DATA-LENGTH-only (no transition/recovery conflation), no double-crediting, no unanchored/estimated fills, INDETERMINATE cash-conversion cap correctly invoked."
```
