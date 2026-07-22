# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
Company: LAXMIINDIA (Laxmi India Finance Ltd, NBFC) | Run date: 2026-07-22
Verifier: C (framework compliance) | Model: claude-opus-4-8 | Fresh context

**SCOPE NOTICE.** This is PHASE 1 only: Gate 0 (B01) and Emerging Moat (B07)
compliance. The valuation-adherence audit (B11/B10) is DEFERRED to phase 3 —
stages 10 and 11 do not exist yet, so the `valuation` section of B12c is emitted
blank/PENDING. `framework_adherence` and `acceptance_rate` below are computed from
the Gate 0 + EM portion ONLY.

I audit rule APPLICATION, not company quality and not raw source fidelity (Verifier
A owns whether a number exists at its anchor). Where a figure is load-bearing for a
band decision I re-derive the band from the stated inputs; I do not re-verify the
input against the PDF.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) RULE-BY-RULE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (re-derived from stated inputs)

ROCE series stated: FY23 16.46, FY24 15.55, FY25 16.37, FY26 16.19 (%).
ROE series stated: FY23 12.18, FY24 12.77, FY25 13.73, FY26 15.63 (%).

| Rule | Threshold | Stated input | Re-derived band | Maker | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 15-19.9=3 | median(15.55,16.19,16.37,16.46)=16.28% | 3 | 3 | PASS |
| A2 Min ROCE | ≥15=5 | 15.55% (FY24) | 5 | 5 | PASS |
| A3 Median ROE | 12-14.9=2 | median(12.18,12.77,13.73,15.63)=13.25% | 2 | 2 | PASS |
| A4 ROCE trend | latest≥earliest=5 \| decline 1-3pp=3 | 16.19 vs 16.46 = −0.27pp | **framework gap** | 3 | **FAIL (MINOR)** |
| Block A sum | — | 3+5+2+3 | 13 | 13 | PASS |

**A4 finding (MINOR).** A 0.27pp decline falls in an unspecified gap: it is not
"latest ≥ earliest" (it is a decline), and it is below the "decline 1-3pp = 3"
floor. Neither band strictly applies. The maker chose the conservative lower band
(3) and flagged it. A defensible alternative reads a sub-1pp move as effectively
flat → 5. Impact: if A4=5, Block A=15, Core=58 — still in the 40-59 AVERAGE band,
still AVOID after the history downgrade. Immaterial to classification. Note: A3 uses
Total Comprehensive Income (incl OCI) per DRHP's own RoNW convention; the maker
confirms the pre-OCI series gives identical bands — acceptable definitional choice.

### Block B — Cash Generation Quality (scored literally, no NBFC override exists)

| Rule | Threshold | Stated input | Band | Maker | Verdict |
|---|---|---|---|---|---|
| B1 CumCFO/CumPAT | <0.50=0 | −984.42/124.23 = −7.93x | 0 | 0 | PASS |
| B2 FCF+ years | <50%=0 | 0/4 = 0% | 0 | 0 | PASS |
| B3 CumFCF/CumPAT | negative=0 | −1002.14/124.23 = −8.07x | 0 | 0 | PASS |
| B4 WC-days | — | marked IRRELEVANT (lender) | excluded | excluded | PASS* |
| Block B sum | — | 0/15 | 0 | 0 | PASS |

The Gate 0 prompt contains **no** NBFC override for Block B — the correct adherence
here is to score B1/B2/B3 literally (all zero) and flag, which the maker did. *B4
exclusion changes only the block denominator (0/15 vs 0/20); the numerator is 0
either way, so Core is unaffected. Consistent with rule 5's N/A handling. No
material issue. `block_b_trend: improving` is correctly evidenced (−10.57x→−5.63x)
and feeds FLAG-CASH per template.

### Block C — Growth

| Rule | Threshold | Stated input | Band | Maker | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR (3y) | ≥20=5 | (319.59/130.67)^⅓−1 = 34.7% | 5 | 5 | PASS |
| C2 PAT CAGR (3y) | ≥20=5 | (49.68/16.03)^⅓−1 = 45.8% | 5 | 5 | PASS |
| C3 +YoY rev years | 100%=5 | 3/3 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | ≥+3pp=5 | +11.06pp | 5 | 5 | PASS |
| Block C sum | — | 20/20 | 20 | 20 | PASS |

CAGR edge rules honoured — no negative/zero endpoints, no loss-to-profit swing; not
applicable here and correctly not invoked.

### Block D — Balance Sheet Strength (NBFC overrides per prompt)

| Rule | Threshold (NBFC path) | Stated input | Band | Maker | Verdict |
|---|---|---|---|---|---|
| D1 CAR | ≥18=5 | CRAR 26.12% (FY26) | 5 | 5 | PASS |
| D2 PCR | <60=0 | 49.43% (FY26) | 0 | 0 | PASS |
| D3 D/E | Financials default 3 | — | 3 | 3 | PASS |
| D4 Current ratio | — | company filings: "Not Applicable" | excluded | excluded | PASS* |
| Block D sum | — | 8/15 | 8 | 8 | PASS |

D1/D2 use the prompt's EXPLICIT bank/NBFC redirections (CAR, PCR) — correct. *D4
exclusion is a denominator-only choice (8/15 vs 8/20); Core unaffected; the company's
own Reg.52(4)/DRHP disclosures independently state "Current Ratio: Not Applicable,"
so N/A treatment is sound.

### Block E — Shareholder Alignment

| Rule | Threshold | Stated input | Band | Maker | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | ≥60=5 | 70.22% anchored (60.17% screener, both ≥60) | 5 | 5 | PASS |
| E2 3y holding change | decreased>3%=0 | 99.41%→70.22% (−29.2pp) | 0 | 0 | PASS |
| E3 Pledge | 0%=5 | none pledged | 5 | 5 | PASS |
| E4 ContLiab/NW | <5%=5 | 0.003% (FY25, latest anchored) | 5 | 5 | PASS |
| Block E sum | — | 15/20 | 15 | 15 | PASS |

E1 uses the anchored DRHP post-Offer figure rather than the latest screener quarter;
both fall in the ≥60% band, so no score impact (imprecision only, flagged by maker).
E2 uses a "2-years-prior" anchored comparator as a 3-year proxy; the −29.2pp magnitude
lands in decreased>3%=0 under any reasonable window. Correct band.

### Core score, classification, downgrade, deal-breakers

- **Core = 13+0+20+8+15 = 56.** Re-derived: 56. PASS.
- **Classification matrix:** Core 40-59 → AVERAGE, regardless of STRONG moat (matrix
  needs Core≥60 for moat to lift the tier). Correct. PASS.
- **Data-confidence downgrade:** 4 data-years = "3-4 LIMITED, downgrade one tier."
  AVERAGE → one tier down → **AVOID**. Tier ordering (…GOOD, AVERAGE, AVOID) makes
  AVOID the correct one-tier-down destination. PASS.
- **Deal-breaker #9 (history <3y → AVERAGE):** 4 years, NOT triggered — correct;
  the LIMITED downgrade is the applicable mechanism, not #9. PASS.
- **Deal-breaker #2 (Block B<8 → max GOOD):** triggered, recorded non-binding. PASS.
- **Deal-breaker #4 (CumCFO/PAT<0.50 → max AVERAGE):** triggered, recorded, drivers
  (all 4 years) named per prompt requirement. PASS.
- **Deal-breakers #1,3,5,7,8:** correctly untriggered. PASS.
- **Deal-breaker #6 (ND/EBITDA>3x AND IC<3x → AVOID):** literal calc
  ND/EBITDA≈6.3x AND IC≈1.48x — **both legs satisfied, so the rule literally fires**.
  The maker did NOT apply it, arguing it duplicates the D1 leverage leg already
  redirected to CRAR for NBFCs. **FAIL (MINOR).** See finding below.
- **FLAG-GATE0 presence rule** (add when classification ≤ AVERAGE with historical
  depressors identified): present and well-specified. PASS.

**Deal-breaker #6 finding (MINOR, flagged for operator ruling).** As written, #6 has
no NBFC carve-out and it fired on both legs — literal application forces AVOID. The
maker declined and flagged it. Two things make this MINOR rather than MAJOR/CRITICAL:
(1) **outcome-neutral** — the final classification is AVOID via the history downgrade
regardless of #6; the destination does not move; (2) the framework's own lender logic
(D1→CAR, D2→PCR in this prompt; Section 1B "CFO/PAT meaningless for lenders" +
Asset-Quality Multiplier carve-out; Master lender-ROE substitution) all point to
reading #6's IC<3x leg — which is structurally ~1.5x for ANY NBFC because interest is
the cost of goods — as a formula-fit artefact, not a genuine deal-breaker. The
deviation from as-written text is real but defensible and transparently surfaced.
Recommend the operator/framework-owner codify #6's NBFC treatment so this stops being
a per-run judgment call.

### Block F — Quantitative moat (does not affect classification; Core<60)

M3, M12 excluded (FAT / negative-WC-float, not meaningful for a lender); M2/M5/M9
scored 0 as PEER DATA NEEDED per the prompt's explicit instruction ("score 0 and
mark PEER DATA NEEDED, never guess"). Scored sum 3+0+5+0+0+1+5+0+5+3 = 22; present
(≥3): M1,M4,M8,M10,M11 = 5 → band 4-5 = STRONG. Re-derived: consistent. PASS. Moat
does not lift the tier (Core 56 < 60). PASS.

**GATE 0 RESULT:** 37 discrete rule checks, 2 FAILs, both MINOR and both
outcome-neutral (A4 edge; deal-breaker #6). The AVOID classification is correctly
derived and correctly framed as mechanical (Block B structural zero + LIMITED
history downgrade), consistent with the CLAUDE.md "flags propagate, no STOP on
quality" law. **I concur with the AVOID classification.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) RULE-BY-RULE
═══════════════════════════════════════════════════════════════════

### Coverage and taxonomy

| Rule | Check | Verdict |
|---|---|---|
| All 21 rows (A1–R1) addressed or NO EVIDENCE FOUND | 21-row summary + 21-row scorecard both complete | PASS |
| Evidence taxonomy (📄/🎙️/🔍) applied per item | applied throughout with anchors | PASS |
| Not conflated with FTTCP | explicit taxonomy note in header | PASS |
| Skepticism / no force-fit | A1,A2,E2,G2,H2,H3,B2 correctly NO EVIDENCE; F2 execution scored 0 as a NEGATIVE read (guidance miss), not force-fit up | PASS |

### Evidence multipliers (📄 1.0x / 🎙️ 0.7x / 🔍 0.5x)

| Cat | Raw | Tier | Correct adj | Maker adj | Verdict |
|---|---|---|---|---|---|
| A3 | 3 | 📄 | 3.0 | 3.0 | PASS |
| A4 | 3 | 📄 | 3.0 | 3.0 | PASS |
| B1 | 4 | 📄 | 4.0 | 4.0 | PASS |
| B3 | 1 | 🎙️ | 0.7 | 0.7 | PASS |
| C1 | 1 | 🎙️ | 0.7 | 0.7 | PASS |
| C2 | 3 | 📄 | 3.0 | 3.0 | PASS |
| D1 | 1 | 🔍 | **0.5** | **0.7** | **FAIL (MINOR)** |
| D2 | 1 | 📄 | 1.0 | 1.0 | PASS |
| E1 | 3 | 🎙️/📄→🎙️ | 2.1 | 2.1 | PASS |
| F1 | 3 | 🎙️/📄→🎙️ | 2.1 | 2.1 | PASS |
| G1 | 4 | 📄 | 4.0 | 4.0 | PASS |
| H1 | 3 | 📄 | 3.0 | 3.0 | PASS |
| R1 | 3 | 🎙️/📄→🎙️ | 2.1 | 2.1 | PASS |

The three mixed 🎙️/📄 categories (E1, F1, R1) were all treated conservatively as
🎙️ (0.7x) — correct; no 🎙️-only category was scored as if 📄. The single exception
runs the OTHER way: **D1 (finding, MINOR).**

**D1 finding (MINOR).** D1 is assigned the 🔍 inference tier in both the summary and
scorecard tables, which mandates a 0.5x multiplier → adjusted 0.5. The maker's
footnote overrides this to 0.7 ("blend with a partial 📄 bureau-integration anchor").
That is inconsistent with the category's own assigned tier and nudges the total up
+0.2. Strict re-derivation of the adjusted total:
`3.0+3.0+4.0+0.7+0.7+3.0+0.5+1.0+2.1+2.1+4.0+3.0+2.1 = 29.2` vs the maker's **29.4**.
Both 29.2 and 29.4 sit in the 25-39 band → **STRENGTHENING either way.** No
classification change; MINOR.

### Classification, recount, structural fields

| Rule | Check | Verdict |
|---|---|---|
| em_classification band | 29.4 (or 29.2) → 25-39 = STRENGTHENING | PASS |
| Completionist recount line present | "📄 recount performed — 9 documented items across 7 categories (A3,A4,B1,C2,D2,G1,H1)" | PASS |
| Completionist guard (≥12 active → re-examine) | 9 active (<12); excess over 3-6 base rate explicitly explained by KPI-certified IPO-prospectus disclosure regime | PASS |
| active_categories = Strong/Moderate only | 9 rows (B1,G1 Strong; A3,A4,C2,E1,F1,H1,R1 Moderate) | PASS |
| evidence_mix internal consistency | documented 7 (A3,A4,B1,C2,D2,G1,H1), claim 5 (B3,C1,E1,F1,R1), inference 1 (D1) = 13 evidenced rows; counts reconcile | PASS |
| optionality_register (0-scored/🎙️/🔍-only, watched never scored) | 7 rows, all convertible-evidence specified; correctly excluded from score | PASS |
| capex_embedded_growth_pct | 0 — 2C N/A for a lender, left NOT FOUND not estimated | PASS |
| catalysts_12m populated (feeds Pillar 3) | 5 catalysts with windows/tiers/anchors | PASS |
| 6C combined table uses injected B01 | pulls core_score 56, AVOID, moat 22/STRONG from B01 | PASS |

### 6D combined_assessment = HIGH POTENTIAL

The label HIGH POTENTIAL is a valid combined-matrix outcome (Section 1B Amendment 4.3
names TURNAROUND/HIGH POTENTIAL explicitly), and the prompt requires **full reasoning**
for HIGH POTENTIAL/TURNAROUND rows — which the maker supplies at length (6D). Rule
satisfied → PASS. **Judgment observation (not a rule fail):** the assessment leans
hard on discounting the Gate 0 AVOID as mechanical to lift a below-AVERAGE backward
score plus a STRENGTHENING (not EXPANSION) forward score all the way to HIGH
POTENTIAL. That is the optimistic end of the defensible range, and it sits on top of
the maker's own live F2 guidance-credibility flag. It is a judgment call the prompt
delegates to this stage with a reasoning requirement that was met; I flag the
optimism for the synthesis stage to weigh, but it is not a mechanical misapplication.

**EMERGING MOAT RESULT:** 18 discrete rule checks, 1 FAIL (D1 multiplier), MINOR and
band-neutral. Category scoring, evidence_mix, completionist recount, and
combined_assessment all follow the prompt.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10) — DEFERRED
═══════════════════════════════════════════════════════════════════

Out of scope for phase 1. Stages 10 and 11 have not run; no B11/B10 artifacts exist.
The `valuation` section of the B12c block is emitted PENDING and must be completed in
phase 3 (continuous Pillar 1, FTTCP ROCE/ROE authority, single-credit rule, Pillar 2L
Asset-Quality Multiplier for this NBFC, UA Amendment-3 ordering, both-tracks carry,
Hurdle Ratio, 4D weights, SOM cross-check). NOT AUDITED HERE.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

- Rules checked (Gate 0 + EM): **55.** Passed: **52.** Failed: **3** — all MINOR,
  all outcome-neutral.
- No CRITICAL, no MAJOR. AVOID (Gate 0) and STRENGTHENING → HIGH POTENTIAL (EM) are
  correctly derived; no recomputation flips a classification.
- **framework_adherence (Gate0+EM only) = 52/55 = 94.5%.**
- The three MINOR items: (1) A4 sub-1pp-decline scored 3 in a framework gap; (2)
  deal-breaker #6 literally fired but was not applied (outcome-neutral AVOID; needs an
  operator ruling on NBFC treatment); (3) D1 evidence multiplier bumped 0.5→0.7,
  em_score 29.4 vs strict 29.2 (STRENGTHENING either way).

```yaml
stage: B12c
company: "LAXMIINDIA"
run_date: "2026-07-22"
model: claude-opus-4-8
status: partial-phase1        # Gate0 + EM audited; valuation deferred to phase 3
phase: "1 of 3 (Gate 0 + Emerging Moat); B11/B10 valuation audit deferred — stages 10/11 not yet run"
gate0:
  rules_checked: 37
  fails:
    - "A4 ROCE-trend: −0.27pp decline scored 3 in a framework gap (below 'decline 1-3pp' floor, not 'latest>=earliest'); conservative, a case exists for 5; Block A 13 vs 15, Core 56 vs 58, AVERAGE->AVOID unchanged (MINOR)"
    - "Deal-breaker #6 (ND/EBITDA>3x AND IC<3x -> AVOID) literally fired (~6.3x AND ~1.48x FY26) but was NOT applied; outcome-neutral (AVOID via history downgrade regardless); no NBFC carve-out in prompt text; recommend operator/framework ruling (MINOR)"
emoat:
  rules_checked: 18
  fails:
    - "D1 evidence multiplier: 🔍 tier mandates 0.5x but adjusted score set to 0.7x ('blend'); em_score 29.4 vs strict 29.2; STRENGTHENING band either way (MINOR)"
valuation:
  rules_checked: 0
  fails: []
  status: "PENDING — phase 3; stages 10/11 not yet run; B11/B10 not audited"
recomputed_destination_pe: ""   # pending phase 3
recomputed_decision: ""         # blank — concur with AVOID (Gate 0) and STRENGTHENING/HIGH POTENTIAL (EM)
findings:
  - {severity: "MINOR", location: "B01 Block A / A4 ROCE trend", description: "0.27pp ROCE decline falls in an unspecified band gap; maker scored 3 (conservative), 5 is arguable; immaterial to classification (AVOID either way)"}
  - {severity: "MINOR", location: "B01 deal-breaker #6", description: "ND/EBITDA~6.3x AND IC~1.48x FY26 literally triggers #6->AVOID but not applied; maker cites duplication with D1 CRAR redirection; outcome-neutral; no NBFC carve-out in text; flag for operator ruling"}
  - {severity: "MINOR", location: "B07 scorecard / D1 multiplier", description: "🔍-tier D1 multiplied at 0.7x instead of 0.5x, inflating em_score to 29.4 vs strict 29.2; STRENGTHENING band unchanged"}
critical_count: 0
major_count: 0
minor_count: 3
framework_adherence: 94.5       # Gate0 + EM portion only: 52 passed / 55 checked
acceptance_rate: 94.5           # rules passed ÷ rules checked (Gate0+EM), %
```
