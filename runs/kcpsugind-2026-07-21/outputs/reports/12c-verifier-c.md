# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: K.C.P. Sugar and Industries (KCPSUGIND) | Run date: 2026-07-21
Model: claude-opus-4-8 | Scope: Gate 0 (B01) + Emerging Moat (B07) ONLY.
Valuation adherence (B10/B11) DEFERRED to phase 3 — those artifacts do not
exist yet and are not audited here.

Mandate: was each framework applied AS WRITTEN? I re-derive every block score
from the stated inputs against the stated thresholds and check the
classification matrix, confidence adjustment, deal-breaker logic, CAGR edge
rules, evidence multipliers, and the completionist guard. I audit rule
application, not raw source fidelity (Verifier A owns whether a number exists
in the source) and not company quality.

Run context weighed: NO-CONCALL MODE; Gate 0 ran off screener CSV +
FY26 audited results + CARE rating + FY25 AR text cache (AR pp.1-150 usable,
pp.151-275 scanned/unavailable); no SHP export supplied. I judge whether the
maker applied the framework CORRECTLY GIVEN those inputs, including its
NOT-FOUND / never-estimate handling.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### BLOCK A — Return on Capital (band re-derivation)

| Rule | Maker input | Threshold band | Maker score | My re-derivation | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 6.93% | <10 = 0 | 0 | median of the 10 ROCE values {2.00,2.40,4.00,4.92,6.75,7.11,10.37,15.19,15.39,20.20} = (6.75+7.11)/2 = 6.93 → <10 = 0 | PASS |
| A2 Min ROCE | 2.00% (FY20) | <8 = 0 | 0 | 2.00 <8 = 0 | PASS |
| A3 Median ROE | 4.86% | <12 = 0 | 0 | median of {-2.14,1.14,2.45,3.24,4.08,5.63,7.73,16.30,16.91,20.28} = (4.08+5.63)/2 = 4.855 → <12 = 0 | PASS |
| A4 ROCE trend | 4.00 vs 20.20 = -16.20pp | decline >5pp = 0 | 0 | -16.20pp is >5pp decline = 0 | PASS |

Block A total 0/20. Arithmetic and every band correct.

### BLOCK B — Cash Generation Quality

| Rule | Maker input | Band | Score | Re-derivation | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 152.63/255.45 = 0.5977 | 0.50-0.69 = 1 | 1 | 152.63/255.45 = 0.598 → band 1 | PASS |
| B2 FCF+ years | 5 of 9 = 55.6% | 50-74 = 2 | 2 | signs {-,-,+,+,+,-,+,+,-} = 5 positive of 9 → 55.6% → 2 | PASS |
| B3 Cum FCF/PAT | 50.23/198.28 = 0.2534 | 0.20-0.39 = 1 | 1 | FCF sum FY18-26 = 50.23; /198.28 = 0.253 → band 1 | PASS |
| B4 ΔWC Days | NOT FOUND | n/a | 0 | historical Trade Payables absent + no FY16 base for FY17 earliest-year leg → uncomputable; scored 0 per never-estimate (Operating Rule 5) | PASS |

Block B total 4/20. Correct. block_b_trend "deteriorating" (CFO +47.79 → -30.89) is a legitimate B-block payload field, correctly populated.

Note (MINOR, not a fail): B4 could in principle compute the LATEST-year WC leg
but not the earliest, so a latest-vs-earliest DELTA is genuinely impossible.
Scoring 0 rather than substituting a 2-leg proxy is the framework-faithful
choice (never estimate). Compliant.

### BLOCK C — Growth (CAGR edge rules honoured?)

| Rule | Maker input | Band | Score | Edge-rule check | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | (259.95/442.17)^(1/9)-1 = -5.74% | <5 = 0 | 0 | both endpoints POSITIVE → valid computed CAGR, NOT N/M; -5.74 <5 = 0. Edge rule correctly NOT triggered | PASS |
| C2 PAT CAGR | -16.62% | negative = 0 | 0 | both endpoints positive → computed; negative → 0 | PASS |
| C3 +YoY rev years | 3 of 9 = 33.3% | <50 = 0 | 0 | 33.3% <50 = 0 | PASS |
| C4 PAT-Rev CAGR | -16.62-(-5.74) = -10.88pp | <-8pp = 0 | 0 | PAT CAGR not N/M so difference computed (edge rule for N/M C4 correctly not invoked); -10.88 <-8 = 0 | PASS |

Block C total 0/20. CAGR edge rules applied correctly. The FY2020 mid-window
PAT loss (-6.26cr) is correctly logged in data_notes and correctly NOT forced
into a loss-to-profit-swing note (endpoints are both profits, so that edge
clause does not fire). Compliant.

### BLOCK D — Balance Sheet Strength

| Rule | Maker anchor | Band | Score | Check | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | CARE (standalone FY25) "net debt negative" | net cash = 5 | 5 | see D1 note below | PASS (instruction-driven basis; deviation from "latest" flagged, decision-immaterial) |
| D2 Interest Cov | CARE FY25 -0.46x; FY26 standalone 0.67x | <1.5x = 0 | 0 | both standalone bases <1.5 = 0; consolidated 3.03x would be 2 but standalone anchor chosen consistently | PASS |
| D3 Debt/Equity | CARE 0.30x; FY26 0.382x | 0.1-0.5 = 4 | 4 | both in 0.1-0.5 band = 4 | PASS |
| D4 Current Ratio | CARE 2.73x; FY26 2.19x | ≥2.0 = 5 | 5 | both ≥2.0 = 5 | PASS |

Block D total 5+0+4+5 = 14/20. Arithmetic correct.

**D1 note (the single largest judgment in the scorecard).** The framework
specifies "Net Debt ÷ EBITDA (latest)". "Latest" is FY2026 (audited cache
exists). The maker instead anchored D1 to CARE's FY2025 standalone
"net-debt-negative" characterization (D1 = 5), which nets ~₹250cr of liquid
investments against debt. Under the framework's LATEST year on a strict
mechanical basis, D1 would be 0 (consolidated ND/EBITDA ≈ 3.0x boundary;
standalone ≈ 10.5x), taking Block D to 9/20.

Adherence assessment: this is a deviation from "latest" AS WRITTEN, but (a) the
orchestrator explicitly instructed CARE as the primary anchor for
gearing/coverage/current-ratio/DB6 — an injected instruction the maker was
directed to follow; (b) the maker showed BOTH figures inline, quantified the
5-point block swing, and raised FLAG-DATA-JUDGMENT prominently; (c) it does not
change the classification (AVOID under both — see below). Severity: MINOR
(fully disclosed, instruction-driven, decision-immaterial). It is the one item
worth operator eyes, and the maker already put it there.

### BLOCK E — Shareholder Alignment

| Rule | Maker input | Band | Score | Check | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 40.59% (AR FY25 Note 17.4) | 40-49.9 = 3 | 3 | band correct; source is annual AR snapshot not "latest quarter" SHP (no SHP supplied) — substitution disclosed | PASS (MINOR basis note) |
| E2 3yr promoter Δ | NOT FOUND (only 2 yrs visible) | n/a | 0 | 3-yr lookback genuinely absent → 0 per never-estimate | PASS |
| E3 Pledge | NOT FOUND (no encumbrance column) | n/a | 0 | not disclosed → 0; correctly NOT asserted as a DB5 breach | PASS |
| E4 Contingent/NW | 2.54% | <5 = 5 | 5 | 9.27/365.27 = 2.54% <5 = 5 | PASS |

Block E total 3+0+0+5 = 8/20. Correct.

E1 note (MINOR): framework says "latest quarter"; maker used the AR FY25 annual
promoter note as best-available substitute because no SHP export was supplied.
The figure genuinely exists in a filing and is anchored, so scoring it (3)
rather than zeroing it is the more faithful call; the annual-vs-quarterly basis
is disclosed. Immaterial to classification. Compliant.

### BLOCK F — Quantitative Moat (12 tests)

| Test | Maker basis | Band applied | Score | Verdict |
|---|---|---|---|---|
| M1 Pricing Power | margin -10.1pp, rev CAGR -5.74% | else = 0 | 0 | PASS (decline >5pp AND no growth → 0) |
| M2 Cost Advantage | PEER DATA NEEDED | 0 | 0 | PASS (never guess peers) |
| M3 Capital Efficiency | FAT 2.62x, ROCE 4.00% | else = 0 | 0 | PASS (ROCE fails 15% and 12% gates) |
| M4 Customer Stickiness | 6 decline years | 3+ decline = 0 | 0 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED | 0 | 0 | PASS |
| M6 Technology/R&D | no R&D/Rev ratio | else = 0 | 0 | PASS (even if computed, R&D 18.03L/259.95cr ≈0.007% <1% → 0) |
| M7 Regulatory/License | regulated, >10 players | regulated but >10 = 1 | 1 | PASS (band correct; player-count anchor is general knowledge — MINOR soft anchor, but conservative and band-safe) |
| M8 Distribution | none disclosed | none = 0 | 0 | PASS |
| M9 Brand | GM proxy 21.81%, PEER DATA NEEDED | 0 | 0 | PASS (proxy stated per rule, unscored w/o peer) |
| M10 Switching Costs | no overall growth | else = 0 | 0 | PASS |
| M11 Network Effects | ≥6yr test; -3.53% vs -9.65%, selling% rising | else = 0 | 0 | PASS (two-window test applied; selling% rising kills every qualifying band) |
| M12 Negative WC | NOT FOUND trend; FY26 ~280 days | 0 | 0 | PASS (>45 days = 0 even on the one computable year) |

Block F total 1/60. Moats present (≥3): none → moat class NONE (0 present).
Framework moat map: 0 = NONE. Correct. PEER-DATA-NEEDED items correctly scored
0, never guessed.

### Classification, confidence, deal-breakers

- **Classification matrix**: Core = 26 (<40) → AVOID. Matrix "Core <40 = AVOID".
  Correct. Verified robust: even under the strict-mechanical D1 alternative
  (core 21) the result is still AVOID. PASS.
- **Data confidence**: 10 years = "full"; history_downgrade: false. Rule "10+
  yrs full". Correct — no one-tier downgrade applies. PASS.
- **Deal-breaker application** (record and cap only; can only make the tier MORE
  restrictive, never more permissive):
  - DB1 Block A 0<8 → max GOOD: triggered, correctly superseded by AVOID. PASS.
  - DB2 Block B 4<8 → max GOOD: triggered, superseded. PASS.
  - DB3 median ROCE 6.93%<10% → max AVERAGE: triggered, superseded. PASS.
  - DB4 cum CFO/PAT 0.5977: NOT <0.50 → correctly not triggered. PASS.
  - DB5 pledge >15%: E3 NOT FOUND → correctly NOT asserted as triggered (genuine
    gap treated as neither pass nor breach). PASS — correct handling of the
    "never let a missing input silently resolve" spirit.
  - DB6 ND/EBITDA >3x AND IC <3x: correctly flagged basis-dependent (does not
    trigger under CARE net-cash; WOULD trigger AVOID under strict standalone
    10.5x/0.67x; consolidated 3.0x/3.03x sits right at the boundary and does not
    trigger). Outcome unaffected — classification already AVOID. PASS.
  - DB7 revenue declined majority (6 of 9) → max AVERAGE: triggered, superseded.
    PASS.
  - DB8 PAT negative in any of last 3 years: evaluated on the consolidated
    screener spine (FY24/25/26 all positive) → not triggered. See MINOR note.
  - DB9 history <3yr: not triggered (10 yrs). PASS.
  - Cap logic: none of the caps is more permissive than the AVOID base, so none
    alters the outcome. Correct framework logic. PASS.

DB8 note (MINOR, immaterial): DB8 was applied on CONSOLIDATED PAT (all three
years positive). On a STANDALONE basis the core entity was loss-making
(FY25 total segment profit ≈ -₹1.72cr; FY26 standalone PBT -₹2.73cr), which
would independently trigger DB8's max-AVERAGE cap. Because the classification is
already AVOID (strictly more restrictive than max-AVERAGE), the basis choice
does not change the outcome. No decision impact; logged for completeness.

### Gate 0 verdict

All 45 checked rules applied as written. Zero band errors, zero arithmetic
errors, zero classification errors. The two documented basis choices (D1 CARE
anchor; E1 annual SHP substitute) are instruction-driven, fully disclosed, and
immaterial to the AVOID classification. NOT-FOUND handling (B4, E2, E3, M-tests)
is framework-faithful — every gap is zeroed, none estimated, none silently
resolved. **Gate 0: fails = 0. MINOR notes = 3 (D1 basis, E1 basis, DB8 basis).
Decision CONCUR: AVOID.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category coverage (all 21 addressed or explicit NO EVIDENCE?)

Section 3 table carries all 20 categories A1-A4, B1-B3, C1-C2, D1-D2, E1-E2,
F1-F2, G1-G2, H1-H3; Section 4 carries R1. Count = 21. Every row is either an
evidence entry or an explicit "NO EVIDENCE FOUND." 17 of 20 marked NO EVIDENCE
FOUND. **Coverage complete. PASS.**

### Evidence-multiplier re-derivation (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x)

| Cat | L×I | Raw (matrix) | Evidence | Adjusted | My check | Verdict |
|---|---|---|---|---|---|---|
| A3 | L/L | 1 (LL=1) | 📄 1.0x | 1.0 | 1×1.0 = 1.0 | PASS |
| B1 | L/L | 1 | 🔍 0.5x | 0.5 | inferred → correctly downgraded to 0.5x | PASS |
| H1 | L/M | 1 (LM=1) | 🔍 0.5x | 0.5 | 1×0.5 = 0.5 | PASS |
| R1 | H/M | 3 (HM=3) | 📄 1.0x | 3.0 | 3×1.0 = 3.0 | PASS (see R1 note) |
| all others | no evidence | 0 | — | 0 | 0 | PASS |

Adjusted total = 1.0+0.5+0.5+3.0 = **5.0 → em_score 5**. Re-derivation matches.
Classification threshold: <12 → NO MEANINGFUL EMERGING MOAT (NONE). Correct.
**PASS.**

R1 note (MINOR, immaterial): R1 likelihood is scored High (H/M, raw 3) on the
strength of the E20 mandate being active nationally, while the report's own text
repeatedly stresses "zero current company-specific capture" (distillery
utilisation -82% YoY as the mandate rolled out). Read strictly through the
emerging-COMPANY-moat lens, an argument exists for L/M (raw 1, adjusted 1.0).
Even at that lower score the total is 3.0, still <12, still NONE. No
classification impact. The generic likelihood×impact matrix does not force the
company-capture read, so H/M is defensible; logged as a MINOR observation only.

### Evidence-tier consistency (any 🎙️/🔍 scored as if 📄?)

No 🎙️ items exist (NO-CONCALL MODE) — correctly reflected (claim: 0 in
evidence_mix). The two inferred rows (B1 farmer-relationship, H1 consolidation
benefit) are correctly carried at 🔍 0.5x, not 📄. G1 (war chest) has real 📄
balance-sheet facts but was deliberately scored 0 for moat purposes with stated
reasoning (no investment programme, CFO drawing down) — this is conservative,
the opposite of inflation, and honours the completionist guard's intent. F2 and
G2 carry documented NEGATIVE evidence, correctly scored 0. **No tier inflation.
PASS.**

### Completionist guard / recount

Guard applied up front AND the explicit recount line is present: "📄 recount
performed: 6 documented items across 5 categories (A3, G1, G2, F2, H1)" — well
under the 12-category inflation threshold. The guard's required "�ecount
performed: [n] documented items across [m] categories" format is satisfied. An
honest sparse scan (3 Weak signals + 1 Moderate R1), consistent with the guard's
3-6 base-rate expectation. **PASS.**

### Downstream fields

- capex_embedded_growth_pct = 0: from Section 2C (CWIP ₹25.11L ÷ FY25 revenue
  ₹22,735.39L ≈ 0.11%, immaterial). Arithmetic-not-judgment call applied
  correctly. PASS.
- active_categories: only Strong/Moderate rows required — only R1 (Moderate)
  listed; A3/B1/H1 (Weak) correctly excluded. PASS.
- 6C combined table uses the injected B01 block (core 26, moats_confirmed 0,
  both classifications) verbatim. PASS.
- 6D combined classification AVOID: backward AVOID + forward NONE. The framework
  flags GOOD/AVERAGE-backward + EXPANSION-forward as the transition setups this
  operation hunts; this is neither (backward at AVOID floor, forward below the
  MODEST threshold of 12), so AVOID is correct and the reasoning is explicit.
  PASS.
- F2 execution-moat: concall promise-delivery cross-reference is unavailable
  (NO-CONCALL); the maker applied the injected substitute methodology
  (capex-completion + ramp evidence) and found documented NEGATIVE evidence.
  Appropriate adaptation. PASS.

### Emerging Moat verdict

All 27 checked rules applied as written. Multiplier arithmetic exact, tier
discipline clean, completionist recount performed and passed, classification
threshold correct. **B07: fails = 0. MINOR notes = 1 (R1 likelihood).
CONCUR: em_score 5, NO MEANINGFUL EMERGING MOAT (NONE), combined AVOID.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10/B11) — DEFERRED
═══════════════════════════════════════════════════════════════════

Out of phase-1 scope. B10/B11 artifacts do not exist yet; the continuous
Pillar 1 formula, FTTCP ROCE authority, single-credit rule, Pillar 2/3,
UA Amendment-3 order, dual-track carry-through, Hurdle Ratio, 4D weights, and
SOM cross-check are NOT audited in this run. To be run in phase 3.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

- Gate 0: 45 rules checked, 0 fails, 3 MINOR basis notes. Every block score
  re-derives exactly; classification AVOID confirmed and robust to the D1
  sensitivity.
- Emerging Moat: 27 rules checked, 0 fails, 1 MINOR note. em_score 5 re-derives
  exactly; NONE / combined AVOID confirmed.
- No CRITICAL, no MAJOR. All MINOR items are instruction-driven or
  immaterial-to-decision basis choices that the makers themselves disclosed.
- I CONCUR with both destinations. No recomputed classification.
- The single item most worth operator attention (D1 net-cash vs strict-mechanical
  swing) is already surfaced by B01 as FLAG-DATA-JUDGMENT; my audit confirms it
  is decision-immaterial (AVOID either way).

```yaml
stage: B12c
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-opus-4-8
status: complete   # phase-1 scope: gate0 + emoat only; valuation deferred to phase 3
gate0: {rules_checked: 45, fails: []}
emoat: {rules_checked: 27, fails: []}
valuation: {rules_checked: 0, fails: [], note: "DEFERRED to phase 3 - B10/B11 artifacts do not exist yet"}
recomputed_destination_pe: ""   # n/a this phase; concur on gate0/emoat
recomputed_decision: ""         # blank - concur: Gate 0 AVOID, Emerging Moat NONE, combined AVOID
findings:
  - {severity: MINOR, location: "B01 Block D / D1", note: "D1 anchored to CARE FY25 standalone net-cash (=5) rather than framework 'latest' (FY26); instruction-driven, both figures shown, FLAG-DATA-JUDGMENT raised, swings Block D 14->9 but classification AVOID under both. Decision-immaterial."}
  - {severity: MINOR, location: "B01 Block E / E1", note: "Promoter holding scored from AR FY25 annual note, not 'latest quarter' SHP (none supplied); figure is filing-anchored and disclosed. Immaterial to AVOID."}
  - {severity: MINOR, location: "B01 deal-breaker DB8", note: "DB8 evaluated on consolidated PAT (all 3 yrs positive); standalone core was loss-making FY25/FY26 and would independently trigger DB8's max-AVERAGE cap. Classification already AVOID (more restrictive), so no outcome change."}
  - {severity: MINOR, location: "B07 Section 5 / R1", note: "R1 likelihood scored High (H/M, raw 3) while report text stresses zero company-specific capture; L/M (raw 1) arguable. Total falls to 3.0 either way, still <12/NONE. No classification impact."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100   # 72 of 72 checked rules (45 gate0 + 27 emoat) applied as written; MINOR items are disclosed basis choices, not rule failures
```
