# VERIFIER C — FRAMEWORK ADHERENCE (B12c)
Company: Venus Remedies Ltd (VENUSREM) | Run date: 2026-09-02
Scope: PHASE 1 (Gate 0 B01 + Emerging Moat B07 only). Valuation audit (B10/B11)
deferred to phase 3. Model: claude-opus-4-8.

Rule sources used: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml;
outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.

I audit rule APPLICATION only. Raw source-fidelity of individual numbers is
Verifier A's domain; where a number's correctness (not its scoring) is in doubt
I flag it for Verifier A and do not count it as a framework fail.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Data-availability opener present ("Data available: 10 years FY17 to FY26",
line 5). Compliant with rule 6.

### Block A — Return on Capital (re-derived)
| Item | Input (anchor) | Band applied | Score | Re-derive | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 15.815% (median FY25 13.07% / FY26 18.56%) | 15-19.9=3 | 3 | mean of 2 pts = 15.815; band 3 | PASS |
| A2 Min single-yr ROCE | 13.07% (FY25) | 12-14.9=3 | 3 | 13.07 in 12-14.9 | PASS |
| A3 Median ROE | 5.955% (10-yr computed) | <12=0 | 0 | sorted 5th/6th = 5.90/6.01, mean 5.955; band 0 | PASS |
| A4 ROCE trend | FY26 18.56 ≥ FY25 13.07 | latest≥earliest=5 | 5 | PASS |
Block A = 11/20. Re-derived 11. PASS.

### Block B — Cash Generation (re-derived)
| Item | Input | Band | Score | Verdict |
|---|---|---|---|---|
| B1 Cum CFO/PAT (10-yr) | 702.12/219.31 = 3.20x | ≥1.00=5 | 5 | PASS |
| B2 FCF-positive proportion | 2/2 computable = 100% | 100%=5 | 5 | PASS (data-limited, see MINOR-1) |
| B3 Cum FCF/PAT (FY25-26) | 186.49/148.10 = 1.259x | ≥0.60=5 | 5 | PASS (2-yr subset, MINOR-1) |
| B4 Change WC Days | 68.96→56.52, −12.44d | decreased >5d=5 | 5 | PASS |
Block B = 20/20. Re-derived 20. PASS. block_b_trend "improving" supported by the
one number rule (CFO/PAT 1.52x + 12.44d WC improvement). PASS.

### Block C — Growth (re-derived)
| Item | Input | Band | Score | Verdict |
|---|---|---|---|---|
| C1 Rev CAGR | (769.6/400.04)^(1/9)−1 = 7.54% | 5-9.9=1 | 1 | PASS |
| C2 PAT CAGR | FY17 PAT −17.08 → N/M (neg endpoint) | N/M=0 | 0 | PASS (CAGR edge rule + data_notes swing logged) |
| C3 Positive YoY yrs | 6/9 = 66.7% | 50-74=1 | 1 | PASS |
| C4 PAT−Rev CAGR | PAT CAGR N/M | edge rule → 0 | 0 | PASS (C4 edge rule honoured + noted) |
Block C = 2/20. Re-derived 2. PASS. CAGR edge rules applied exactly as written
(negative endpoint → N/M → 0; loss-to-profit swing noted; C4=0 on N/M PAT).

### Block D — Balance Sheet (re-derived)
D1 net cash → 5 (PASS). D2 IC ~3,355x ≥10x → 5 (PASS). D3 D/E 0.00 <0.1 → 5
(PASS). D4 current ratio 2.56 ≥2.0 → 5 (PASS). Block D = 20/20. PASS.

### Block E — Shareholder Alignment (re-derived)
E1 promoter 41.76% → band 40-49.9 = 3 (PASS). E2 3-yr change N/A (FY23 baseline
NOT FOUND) → 0 (PASS — grounded-claims rule 5, no estimation). E3 pledge 0% → 5
(PASS). E4 contingent/net worth 2.88% <5% → 5 (PASS). Block E = 13/20. PASS.

### Block F — Quantitative Moat (12 tests, re-derived)
| Test | Applied | Score | Verdict |
|---|---|---|---|
| M1 Pricing | margin +6.45pp but Rev CAGR 7.55% < 10% gate | 0 | PASS |
| M2 Cost adv | PEER DATA NEEDED | 0 | PASS |
| M3 Cap efficiency | FAT 2.72x >2 AND ROCE 18.56 >15 | 3 | PASS (see MINOR-3 on FAT base) |
| M4 Stickiness | 3 decline years | 0 | PASS |
| M5 Scale | PEER DATA NEEDED | 0 | PASS |
| M6 Tech/R&D | 2.40% <3% tier; ≥1% tier needs peer median | 0 | PASS |
| M7 Regulatory | PEER DATA NEEDED | 0 | PASS |
| M8 Distribution | 100+ countries mentioned, unquantified trend | 1 | PASS |
| M9 Brand | PEER DATA NEEDED | 0 | PASS |
| M10 Switching | overall growth, 3 decline years | 1 | PASS |
| M11 Network | latest 3yr CAGR 11.69% < prior 18.09% | 0 | PASS |
| M12 Neg WC | both yrs >45d | 0 | PASS |
Block F = 5/60. Re-derived 5. Moats present (≥3) = 1 (M3). Class THIN (1=THIN). PASS.
PEER DATA NEEDED handling correct: every peer-dependent test scored 0, never
guessed (rule "never guess peer figures" honoured). PASS.

### Classification, confidence, deal-breakers
- Core = 11+20+2+20+13 = 66. Moat = 5. Grand total = 71/160. Re-derived, PASS.
- Confidence: 10-yr history → full, no history downgrade. PASS.
- Matrix: Core 60-79 + THIN (else) → GOOD. PASS.
- Deal-breakers 1-9 all evaluated, none triggered; each re-checked against re-derived
  inputs (A=11≥8, B=20≥8, median ROCE 15.8%≥10, CFO/PAT 3.20≥0.50, pledge 0%,
  ND/EBITDA net cash, rev decline 33% not majority, PAT positive last 3 yrs,
  history 10 yrs). PASS.
- flags: [] correct — classification GOOD is above AVERAGE, so no FLAG-GATE0
  required by the flag rule. PASS.

### Gate 0 verdict
Every block score, the classification matrix, the confidence tier, the CAGR edge
rules, and all nine deal-breakers re-derive to the reported values. No framework
misapplication. No CRITICAL, no MAJOR. Recomputed decision CONCURS: GOOD.

MINOR observations (no score impact, all transparently disclosed by the maker):
- MINOR-1: B2/B3 (and A1/A2/A4) rest on a 2-year window (FY25-FY26) forced by a
  Data_Sheet gap. Scoring on available data is permitted by rule 6, and the
  limitation is flagged in DATA NOTES. Confidence caveat only, not a fail.
  Anchor: 01-gate0.md lines 89-96, 109-128, 326-349.
- MINOR-2: basis mix — A1/A2/A4 use standalone ROCE (AR Note 39), A3 uses
  consolidated computed ROE. Both anchored and the divergence is explained
  (lines 84-87). The formula definitions do not mandate one basis, so no fail;
  noted for cross-block consistency.
- MINOR-3 (refer Verifier A): M3 FAT uses screener "Net Block" 231.60 (line 208),
  while B07 2C uses AR net PP&E 110.23 / gross 322.52 (07-emoat.md lines 84-87).
  Different fixed-asset base across the two reports. M3's rule application is
  correct on its stated input and the score (3) is unaffected either way, so this
  is a number-reconciliation item for Verifier A, not a framework fail.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category coverage (rule 3: all 23 addressed or explicit NO EVIDENCE)
Section 3 covers A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G3? — verified:
A1-A4 (4), B1-B3 (3), C1-C2 (2), D1-D2 (2), E1-E2 (2), F1-F2 (2), G1-G2 (2),
H1-H3 (3), I1-I2 (2) = 22 categories; R1 in Section 4 = 23 rows. All present, each
with evidence table or "NO EVIDENCE FOUND". PASS.

### I1 / I2 gate (verifier rule 8)
- I1 Talent asymmetry (Cat 21): both legs (a) and (b) NOT FOUND → score 0. Rule
  requires score >0 only if both legs evidenced with the (b) leg carrying ≥1 📄.
  Score 0 is compliant. PASS.
- I2 Cannibalization barrier (Cat 22): honest answer "nothing must be destroyed"
  → score 0. Rule requires a specific named sacrifice for any score >0. Score 0
  compliant. PASS.
- Both categories present and I1/I2 contribution stated separately (0), feeding the
  operator's 10-15-scan review checkpoint. PASS.

### Evidence multipliers and tier consistency (rule 3)
Raw = L×I matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0); multiplier
📄 1.0 / 🎙️ 0.7 / 🔍 0.5. Re-derived every scored row:

| Cat | L×I → Raw | Type | ×Mult | Adjusted | Verdict |
|---|---|---|---|---|---|
| A1 | HH 4 | 📄 | 1.0 | 4.0 | PASS |
| A2 | MH 3 | 📄 | 1.0 | 3.0 | PASS |
| A3 | HM 3 | 📄 | 1.0 | 3.0 | PASS |
| A4 | LM 1 | 🎙️ | 0.7 | 0.7 | PASS |
| C1 | LM 1 | 🎙️ | 0.7 | 0.7 | PASS |
| C2 | MM 2 | 📄 | 1.0 | 2.0 | PASS |
| E1 | HM 3 | 📄 | 1.0 | 3.0 | PASS |
| F1 | LL 1 | 🔍 | 0.5 | 0.5 | PASS |
| F2 | MM 2 | 📄 | 1.0 | 2.0 | PASS |
| G1 | HH 4 | 📄 | 1.0 | 4.0 | PASS |
| G2 | MM 2 | 📄 | 1.0 | 2.0 | PASS |
| H2 | MM 2 | 📄 | 1.0 | 2.0 | PASS |
| H3 | LL 1 | 🔍 | 0.5 | 0.5 | PASS |
| R1 | HH 4 | 📄 | 1.0 | 4.0 | PASS |
(B1-B3, D1-D2, E2, H1, I1, I2 all 0 — PASS.)
Sum = 31.4, reported as 31. Re-derived 31.4. PASS.
Classification 25-39 = MOAT STRENGTHENING. 31 → STRENGTHENING. PASS.

Tier-honesty spot-checks (the "🎙️-only scoring as 📄" finding the rule targets):
- C1 customer ecosystem: narrative reach only → scored 🎙️ 0.7, NOT 📄. Correct discipline. PASS.
- A3 process innovation: "same-energy" claim is 🎙️ but cross-checked with documented
  financials (EBITDA doubled vs +Rs3.63 Cr P&M, 44% oncology productivity) → 📄 defensible. PASS.
- F1 talent density: absence-of-data → 🔍 0.5. PASS.
- H3 ESG: compliance facts documented but advantage inferred → 🔍 0.5. Conservative. PASS.
No category with only-claim evidence is scored as documented. PASS.

### Completionist guard (rule 3 + prompt 07 rule 6)
Guard performed explicitly: "📄 recount performed: [n] documented items across [m]
categories" line present; 10 active categories < 12 trigger, so no inflation alarm.
Outcome correct.
FINDING (MINOR-4): the recount TOTAL is internally inconsistent. The line states
"26 documented items" but the per-category breakdown sums to 27
(A1:4 + A2:4 + A3:2 + C2:1 + E1:4 + F2:3 + G1:4 + G2:1 + H2:2 + R1:2 = 27). Same
off-by-one carried into the B07 YAML completionist_recount field. The guard's
decision (10 categories, below the 12 trigger, no 🎙️-as-📄 inflation) is unaffected,
so this is presentational, not decision-changing. Anchor: 07-emoat.md lines 291-301;
B07-emoat.yaml line 30.

### Other structural checks
- active_categories YAML lists exactly the 10 Strong/Moderate rows (A1,A2,A3,C2,E1,
  F2,G1,G2,H2,R1); Weak rows (A4,C1,F1,H3) correctly excluded. PASS.
- 2C capex-embedded growth: arithmetic shown for both bases (net-block 46.4% rejected
  as depreciated-denominator artefact; gross-block 15.9% carried as conservative 16).
  Complies with "show the arithmetic" and "never estimate." PASS. capex_embedded_growth_pct: 16. PASS.
- catalysts_12m each carry evidence_type + anchor; VRP-048 CTA correctly typed as
  "claim" (management timeline). PASS.
- Combined assessment 6D: GOOD (backward) + STRENGTHENING (forward) → GOOD+, with
  HIGH POTENTIAL/TURNAROUND explicitly reasoned out. Uses the injected B01 block.
  Judgment within framework. PASS.
- G2 double-credit awareness: the maker explicitly reduced forward weight on WC
  improvement to avoid double-crediting the Gate 0 core score. Consistent with the
  one-improvement-one-mechanism principle. PASS.

### Emerging Moat verdict
Full category coverage, correct evidence taxonomy, correct multipliers, correct
band, I1/I2 gate honoured, completionist guard performed with the correct outcome.
One MINOR arithmetic inconsistency in the recount tally (26 vs 27). No CRITICAL,
no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) — DEFERRED
═══════════════════════════════════════════════════════════════════
Out of scope in phase 1. B10/B11 blocks do not exist yet. Valuation-adherence audit
(continuous Pillar 1, FTTCP ROCE authority, UA Amendment 3, dual-track, Hurdle Ratio,
method plurality, downstream candidates, exit construction v3.8, Amendment 19 FV path)
deferred to phase 3. Not attempted here. Valuation framework docs were not loaded.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: every score, matrix, confidence tier, CAGR edge rule, and all 9
  deal-breakers re-derive to the reported values. Decision CONCURS: GOOD.
- Emerging Moat: coverage, taxonomy, multipliers, band, I1/I2 gate all compliant;
  one MINOR off-by-one in the completionist recount tally.
- No CRITICAL, no MAJOR. 4 MINOR (3 Gate 0 disclosure/cross-report notes, 1 Emoat
  recount arithmetic). None changes a score, classification, or decision.
- Recomputed destination PE: N/A (phase 1, no valuation in scope).
- Recomputed decision: concur (Gate 0 GOOD stands; Emoat STRENGTHENING / GOOD+ stands).
