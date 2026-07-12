# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (AIMTRON)
Run date: 2026-07-12 | Model: claude-opus-4-8 | Scope: PHASE 1 ONLY (Gate 0 B01 + Emerging Moat B07)

Valuation adherence (B11/B10) is DEFERRED to phase 3 and NOT run here. The `valuation`
section of the handoff block is marked pending-phase-3.

Audit question (per rubric): was each framework applied AS WRITTEN? I re-derive every
score from the stated inputs against the stated thresholds. I do not re-audit raw source
numbers (Verifier A owns numbers) except where an arithmetic slip changes a score.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Inputs re-derived from the B01 report's own stated figures against
prompts/01-gate-0-pipeline.md thresholds.

### Block A — Return on Capital (reported 14/20)
| Rule | Input (from report) | Threshold applied | Recomputed | Reported | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | median{31.48, 20.79, 24.00} = 24.00% | 20-24.9 = 4 | 4 | 4 | PASS |
| A2 Min single-yr ROCE | 20.79% | ≥15 = 5 | 5 | 5 | PASS |
| A3 Median ROE | median{26.30, 24.89, 20.46} = 24.89% | ≥20 = 5 | 5 | 5 | PASS |
| A4 ROCE trend | 24.00 − 31.48 = −7.48pp | decline >5pp = 0 | 0 | 0 | PASS |
Block A = 4+5+5+0 = 14. PASS.

### Block B — Cash Generation (reported 0/20)
| Rule | Input | Threshold | Recomputed | Reported | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | −10.53 / 78.50 = −0.134 | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive yrs | 1/3 = 33.3% | <50 = 0 | 0 | 0 | PASS |
| B3 Cum FCF/PAT | −31.82 / 78.50 = −0.405 | negative = 0 | 0 | 0 | PASS |
| B4 ΔWC days | 220.0 − 183.5 = +36.5 | increased >15 = 0 | 0 | 0 | PASS |
Block B = 0. PASS. (Note: report states +36.6 days; exact subtraction is +36.5. No score
impact — MINOR arithmetic, number-domain / Verifier A.)

### Block C — Growth (reported 20/20)
| Rule | Input | Threshold | Recomputed | Reported | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR (2yr) | (257.13/92.98)^0.5−1 = 66.3% | ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR (2yr) | (39.16/13.60)^0.5−1 = 69.7% | ≥20 = 5 | 5 | 5 | PASS |
| C3 Positive YoY yrs | 2/2 = 100% | 100 = 5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | 69.7 − 66.3 = +3.4pp | ≥+3pp = 5 | 5 | 5 | PASS |
Block C = 20. PASS. CAGR edge rules honoured (no negative/zero endpoints; both positive,
2-year window correctly used).

### Block D — Balance Sheet (reported 20/20)
| Rule | Input | Threshold | Recomputed | Reported | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | net cash (−8.16 Cr) | net cash = 5 | 5 | 5 | PASS |
| D2 Interest coverage | 54.70/0.68 = 80.4x | ≥10 = 5 | 5 | 5 | PASS |
| D3 Debt/Equity | 0.49/227.86 = 0.002 | <0.1 = 5 | 5 | 5 | PASS |
| D4 Current ratio | 307.09/117.63 = 2.61 | ≥2.0 = 5 | 5 | 5 | PASS |
Block D = 20. PASS. (Report states IC = 80.6x; exact = 80.4x. No score impact — MINOR,
number-domain.) Non-financial issuer: Bank/NBFC alt-rules correctly NOT applied.

### Block E — Shareholder Alignment (reported 8/20)
| Rule | Input | Threshold | Recomputed | Reported | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding (latest avail) | 71.35% | ≥60 = 5 | 5 | 5 | PASS |
| E2 Promoter change | −18.59pp | decreased >3% = 0 | 0 | 0 | PASS |
| E3 Promoter pledge | NOT FOUND | rule 5: unavailable → 0 | 0 | 0 | PASS |
| E4 Cont. liab / NW | 20.91/155.09 = 13.48% | 5-15 = 3 | 3 | 3 | PASS |
Block E = 8. PASS.
- E1: rule wants "latest quarter"; no FY26 quarter provided, report used latest verified
  anchor (AR2025, 31-Mar-2025) and flagged the gap. Compliant NOT-FOUND handling.
- E2: rule wants a 3-year change; only a 1-year change exists (company listed Jun-2024).
  Direction/magnitude (>3% decrease) locks the score at 0 under any window, so no score
  impact; report disclosed the limitation. Compliant.
- E3: NOT FOUND scored 0 per Gate 0 operating rule 5 ("mark N/A and score 0"). Compliant.
  Importantly, deal-breaker #5 (pledge >15% → max AVERAGE) was correctly NOT triggered off
  a NOT FOUND (unconfirmed ≠ confirmed >15%). Correct — matches the CLAUDE.md discipline
  of never manufacturing a deal-breaker from missing data.

### Core Score = 14+0+20+20+8 = 62. PASS.

### Block F — Quantitative Moat (reported 10/60)
| Test | Reported | Threshold check | Verdict |
|---|---|---|---|
| M1 Pricing power | 1 | EBITDA margin declined 2.17pp (2-5pp) despite growth = 1 | PASS |
| M2 Cost advantage | 0 | PEER DATA NEEDED → 0 | PASS |
| M3 Capital efficiency | 5 | FAT 8.83x (>3x) AND ROCE 24% (>20%) = 5 | PASS |
| M4 Customer stickiness | 3 | 0 decline yrs but rec-days not stable ±10 → falls to "≤1 decline yr" tier = 3 | PASS |
| M5 Scale & dominance | 0 | PEER DATA NEEDED → 0 | PASS |
| M6 Technology/R&D | 0 | R&D/Rev NOT FOUND → 0 | PASS |
| M7 Regulatory/license | 0 | unregulated segment = 0 | PASS |
| M8 Distribution | 1 | mentioned unquantified = 1 | PASS |
| M9 Brand | 0 | GM proxy computed but no peer median → PEER DATA NEEDED = 0 | PASS |
| M10 Switching costs | 0 | rec days rose >10 (+101d); 0 decline yrs so no lower tier matches → 0 | PASS |
| M11 Network effects | 0 | <6yr; selling-exp % not disclosed → conservative 0 per rule | PASS |
| M12 Negative WC/float | 0 | WC days >45 all years → 0 | PASS |
Moat score = 1+5+3+1 = 10. Moats present (≥3): M3, M4 → 2 → "2-3 = MODERATE". PASS.
Grand total = 62 + 10 = 72. PASS.

M4 note: the =5 tier fails (rec days not stable ±10); the report drops to the =3 tier
("max 1 decline year") on the basis of zero decline years. The tiers are ambiguous here
(the =3 tier text is about decline years, not receivable stability), but a descending-tier
reading places a zero-decline company at =3 when it misses =5. Defensible. PASS.

### SECTOR-INDEPENDENCE CHECK (task-flagged)
The manifest `sector_cap_row` was mis-set to "Pharma / CDMO" (collector defect; correct
row is EMS/electronics manufacturing). Gate 0 handled this CORRECTLY:
- The SECTOR NOTE (B01 lines 246-254) explicitly states the mislabel "has not been used
  anywhere in the scoring."
- The four peer-dependent moat tests (M2, M5, M6, M9) were scored 0 / PEER DATA NEEDED
  rather than borrowed from an unrelated Pharma peer set.
- No Pharma-specific threshold, margin, or cap entered any Block A-F computation.
Gate 0 scoring is sector-independent as required. The sector-cap defect is quarantined to
the phase-3 valuation UA step (out of scope here). PASS — no finding.

### CLASSIFICATION CASCADE — one substantive FAIL
| Step | Rule | Applied in report |
|---|---|---|
| Baseline | Core 62 (60-79) + MODERATE → "else" → GOOD | GOOD — PASS |
| Data confidence | 3 yrs = LIMITED (3-4 band) → downgrade one tier | applied — PASS on identification |
| Deal-breaker #2 | Block B <8 → max GOOD | applied, non-binding — PASS |
| Deal-breaker #4 | cum CFO/PAT −0.13x <0.50 → max AVERAGE | applied — PASS |
| Deal-breaker #9 | history <3 yrs → AVERAGE | correctly NOT triggered (exactly 3 yrs, not <3) — PASS |
| **Order of operations** | cap vs downgrade sequencing | **see finding G0-1** |

**FINDING G0-1 (MAJOR, decision-sensitive).** The framework is SILENT on the order in
which the deal-breaker cap and the LIMITED-history one-tier downgrade compose. The two
orders diverge:
- Order used by report (cap → then downgrade): GOOD →(#4 cap)→ AVERAGE →(LIMITED −1 tier)→
  **AVOID**.
- Alternative (downgrade → then cap): GOOD →(LIMITED −1 tier)→ AVERAGE →(#4 cap, AVERAGE ≤
  AVERAGE, no change)→ **AVERAGE**.

A deal-breaker is written as a CAP ("max AVERAGE" = a ceiling), not a fixed re-assignment.
Under the alternative order the one-tier downgrade lands the case on AVERAGE and the cap is
already satisfied, yielding AVERAGE. The report's order stacks the two depressors for a
two-tier total drop (AVOID). This flips the Gate 0 label (AVERAGE vs AVOID) — decision
relevant, since AVERAGE is precisely the "GOOD/AVERAGE backward score" band the transition
strategy hunts and the documented-post-IPO-rebase note contemplates downstream position
sizing over, whereas AVOID reads more terminal.

There is a further internal-consistency argument for the AVERAGE reading: a company with
<3 years of history gets "auto AVERAGE" (a fixed floor). Under the report's order a company
with exactly 3 years (AVOID) ends up strictly WORSE than a company with less history
(AVERAGE) — a perverse outcome that argues the downgrade should not push below the AVERAGE
floor that shorter-history peers enjoy.

Severity: MAJOR not CRITICAL, because (a) the framework text does not fix the order, so this
is an unresolved ambiguity rather than a violated written rule; (b) the report chose the
conservative branch and disclosed every step transparently; (c) flags propagate and Gate 0
does not halt. But it flips the Gate 0 destination label, so it must be surfaced for an
operator/Keerti ruling and for the phase-3 combined read. Recomputed Gate 0 under the
alternative order = AVERAGE.

**Gate 0 verdict: 40 of 41 rule checks pass. Every block score, every deal-breaker trigger
test, the moat classification, and the sector-independence handling are correct as written.
The single fail is the unspecified cap/downgrade ordering, which is decision-sensitive.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Completeness — all 21 categories
Section 3 + Section 4 address all 21: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3, R1. Each is either scored with anchored evidence or marked "NO EVIDENCE FOUND"
(A1, A4, B3, C2, D1, E1, H1). PASS — no silent omissions.

### Evidence multipliers (📄 1.0 / 🎙️ 0.7 / 🔍 0.5) and matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1)
| ID | Rating | Raw | Type | Mult | Weighted (report) | Recomputed | Verdict |
|---|---|---|---|---|---|---|---|
| A3 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| B1 | MH | 3 | 🎙️ | 0.7 | 2.1 | 2.1 | PASS |
| B2 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| C1 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| D2 | LL | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| E2 | HH | 4 | 🎙️ | 0.7 | 2.8 | 2.8 | PASS |
| F1 | ML | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| F2 | ML | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| H2 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| H3 | LL | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| R1 | MH | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
Adjusted total = 23.2 → 23. Recomputed sum = 23.2. PASS.
Classification: 23 in 12-24 → MODEST MOAT DEVELOPMENT. PASS.

### Evidence-tier discipline (no 🎙️-only category inflated to 📄)
Checked the specific risk called out in the rubric. The report is CONSERVATIVE, not
inflationary:
- E2 (China+1): has some 📄 support (European order, AIC close) yet the scorecard applies
  the 🎙️ 0.7x multiplier to the narrative rating. Under-credits rather than over-credits.
- B1 (backward integration): 🎙️ 0.7x applied despite a 📄 subsidiary incorporation. Same.
- A3, B2, H2, H3, R1 scored 📄 1.0x each rest on genuinely documented items (AR process
  disclosures, held certifications, closed AIC acquisition, ISO 14001 cert, filed+
  MeitY-acknowledged ECMS application). Appropriate.
PASS — no category scored as 📄 on 🎙️-only evidence.

### Completionist recount
Report states: "📄 recount performed: 11 documented items across 6 categories" — format
matches the prompt's required line. Active (Strong/Moderate) categories = 6, within the
3-6 base rate; nonzero-weighted rows = 11, below the 12-category inflation trigger. Report
explicitly concludes "no completionist inflation triggered." PASS.

### capex_embedded_growth_pct — FAIL
**FINDING EM-1 (MAJOR).** Section 2C reports `capex_embedded_growth_pct: 331` as the
headline figure fed forward to stage 9. Per the prompt, 2C's method is "total capex under
execution × historical fixed asset turnover = implied incremental revenue." That formula,
run on the only documented capex available, yields **41.9%** (FY25 capex Rs12.96cr × FAT
4.88x = Rs63.2cr on the Rs151cr base). The 331% headline instead comes from a 🎙️ capacity
assertion ("6 SMT lines × ~Rs100cr/line") for a greenfield facility with **no disclosed
total project cost** and CWIP of only Rs0.15cr at FY26 year-end. Reporting the 🎙️ figure
(8x the documented floor) as the primary output departs from the prescribed capex×FAT
methodology and from operating rule 4 ("prioritise hard evidence over promises"). The
report is transparent — it carries the 41.9% documented floor alongside and flags the
figure as claim-heavy — which mitigates severity, but the number a downstream growth input
consumes should be the documented 41.9%, not the 331% claim. Severity MAJOR: it does not
change em_score or em_classification, but it can materially inflate a downstream growth
assumption if taken at face value.

### active_categories label consistency — MINOR
**FINDING EM-2 (MINOR).** C1 (customer ecosystem) is labelled "Weak-Moderate" in the
Section 3 table but is excluded from the `active_categories` YAML list (which the spec
defines as "only Strong/Moderate rows"). The exclusion is defensible for a weak-leaning
borderline row, but the Section 3 "Moderate" tag and the YAML omission are not fully
consistent. No score impact (C1's 1.4 weighted contribution is unchanged). Cosmetic.

### Combined assessment (6C/6D)
6C table reproduces the injected B01 block faithfully (core 62, MODERATE, AVOID, EM 23).
6D carries AVOID forward from Gate 0. Consistent with the inputs as given. NOTE: this
inherits Gate 0's AVOID label, which is itself subject to FINDING G0-1 — if Gate 0 resolves
to AVERAGE, the combined read becomes "AVERAGE backward + MODEST forward," which is closer
to (though still short of, MODEST < STRENGTHENING) the transition band. Dependency flagged;
6D's arithmetic given its input is correct. PASS on internal logic.

**Emerging Moat verdict: 24 of 26 rule checks pass. Completeness, multipliers, matrix
arithmetic, adjusted total, classification band, evidence-tier discipline, and the
completionist recount are all correct as written. One MAJOR (capex 331% vs documented
41.9% methodology departure) and one MINOR (C1 label) finding.**

═══════════════════════════════════════════════════════════════════
## CONSOLIDATED FINDINGS
═══════════════════════════════════════════════════════════════════
| # | Severity | Location | Description |
|---|---|---|---|
| G0-1 | MAJOR | B01 Classification cascade (01-gate0.md ~L173-194) | Deal-breaker cap vs LIMITED-history downgrade ordering is unspecified by the framework. Report order (cap→downgrade) → AVOID; alternative (downgrade→cap) → AVERAGE. Decision-sensitive; recomputed alternative = AVERAGE. Perverse-outcome argument (3yr worse than <3yr auto-AVERAGE) favours AVERAGE. Needs Keerti ruling. |
| EM-1 | MAJOR | B07 Section 2C + YAML L279 (07-emoat.md) | capex_embedded_growth_pct=331% is a 🎙️ capacity claim, not the prescribed capex×FAT output (41.9% documented). Transparent but the headline fed downstream should be the documented floor. |
| EM-2 | MINOR | B07 Section 3 L98 / YAML L264-270 | C1 tagged "Weak-Moderate" in Section 3 but omitted from active_categories. Cosmetic, no score impact. |
| G0-2 | MINOR | B01 Block B / Block D | Arithmetic rounding: ΔWC 220.0−183.5 = 36.5 (reported 36.6); IC 54.70/0.68 = 80.4x (reported 80.6x). No score impact; number-domain (Verifier A). |

Critical: 0 | Major: 2 | Minor: 2

Scope coverage: Gate 0 = 41 rule checks (40 pass); Emerging Moat = 26 rule checks (24 pass).
Combined 67 checks, 64 pass → acceptance 95%. Valuation adherence (B11/B10) deferred to
phase 3 — not run.

═══════════════════════════════════════════════════════════════════

```yaml
stage: B12c
company: "AIMTRON"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation deferred to phase 3"
gate0:
  rules_checked: 41
  fails:
    - {rule: "classification cap/downgrade ordering", severity: "MAJOR", reported: "AVOID", recomputed_alt: "AVERAGE", note: "framework silent on order of deal-breaker cap vs LIMITED-history one-tier downgrade; decision-sensitive; all block scores and deal-breaker triggers themselves correct; sector-independence handled correctly"}
emoat:
  rules_checked: 26
  fails:
    - {rule: "2C capex_embedded_growth_pct methodology", severity: "MAJOR", reported: "331 (management capacity claim)", recomputed: "41.9 (capex x FAT documented)", note: "headline is a claim, not the prescribed capex*FAT output; documented floor carried but 331 fed forward"}
    - {rule: "active_categories label consistency (C1)", severity: "MINOR", note: "C1 tagged Weak-Moderate in Section 3 but omitted from active_categories; no score impact"}
valuation:
  status: "pending-phase-3"
  rules_checked: 0
  fails: []
recomputed_destination_pe: ""   # pending phase 3
recomputed_decision: ""         # pending phase 3; note Gate 0 label is AVOID vs AVERAGE under G0-1
findings:
  - {severity: "MAJOR", location: "B01 classification cascade (01-gate0.md L173-194)", description: "Deal-breaker #4 cap (max AVERAGE) vs LIMITED-history one-tier downgrade ordering is unspecified. Report order (cap then downgrade) yields AVOID; alternative order (downgrade then cap) yields AVERAGE. Decision-sensitive; perverse-outcome argument favours AVERAGE. Needs operator ruling."}
  - {severity: "MAJOR", location: "B07 Section 2C / YAML capex_embedded_growth_pct (07-emoat.md L279)", description: "capex_embedded_growth_pct=331% is a management capacity claim, not the prompt-specified capex x FAT computation (41.9% documented). Transparent but claim-based headline fed downstream."}
  - {severity: "MINOR", location: "B07 Section 3 L98 / active_categories (07-emoat.md L264-270)", description: "C1 labelled Weak-Moderate in Section 3 but excluded from active_categories list; cosmetic, no score impact."}
  - {severity: "MINOR", location: "B01 Block B ΔWC / Block D interest coverage", description: "Rounding: WC delta 36.5 shown as 36.6; interest coverage 80.4x shown as 80.6x. No score impact; number-domain (Verifier A)."}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 95
```
