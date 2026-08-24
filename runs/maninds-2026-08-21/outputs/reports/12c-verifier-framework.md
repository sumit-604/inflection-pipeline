# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Run: MANINDS (Man Industries (India) Ltd) | run_date 2026-08-21
Model: claude-opus-4-8 | Emits: B12c (gate0 + emoat only)
Scope: Gate 0 (B01) and Emerging Moat (B07) compliance. Valuation audit
(B10/B11) deferred to phase 3.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/reports/07-emoat.md.
I audit rule application only. Raw-number existence is Verifier A's gate.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Every block score re-derived from the stated inputs against the stated
thresholds. All 32 line-item scores reproduce exactly. Classification,
deal-breakers, CAGR edge rules, and data confidence all correct.

### BLOCK A — Return on Capital (re-derived 6/20) PASS
- A1 median ROCE. 10-year set median = (13.57+14.33)/2 = 13.95% → band
  10-14.9 → score 1. MATCH.
- A2 minimum single-year ROCE = 7.71% (FY17) → <8 → score 0. MATCH.
- A3 median ROE = (8.69+9.23)/2 = 8.96% → <12 → score 0. MATCH.
- A4 trend FY26 14.33% >= FY17 7.71% → score 5. MATCH.
Block A = 6. MATCH.

### BLOCK B — Cash Generation (re-derived 8/20) PASS
- B1 cum CFO 1607.43 / cum PAT 909.86 = 1.767 → >=1.00 → score 5. MATCH.
- B2 FCF-positive 6/10 = 60% → band 50-74 → score 2. MATCH.
- B3 cum FCF 312.07 / cum PAT 909.86 = 0.343 → band 0.20-0.39 → score 1. MATCH.
- B4 WC days FY26 260.66 vs FY17 154.78 = +105.88 → increased >15 → score 0. MATCH.
Block B = 8. MATCH.

### BLOCK C — Growth (re-derived 15/20) PASS
- C1 revenue CAGR (3563.90/1060.49)^(1/9)-1 = 14.41% → band 10-14.9 → score 3. MATCH.
- C2 PAT CAGR (170.48/33.57)^(1/9)-1 = 19.79% → band 15-19.9 → score 4. MATCH.
- C3 positive YoY 8/9 = 88.9% → band 75-99 → score 3. MATCH.
- C4 19.79 − 14.41 = +5.38pp → >=+3pp → score 5. MATCH.
Block C = 15. MATCH.
CAGR edge rules: no zero/negative endpoint on either CAGR; PAT did not
swing loss-to-profit in the window; C4 not driven by an N/M PAT CAGR.
Edge rules correctly not triggered.

### BLOCK D — Balance Sheet (re-derived 12/20) PASS
- D1 net debt 627.98 − 657.21 = −29.23 (net cash) → score 5. MATCH.
- D2 IC 388.97/152.03 = 2.56x → band 1.5-2.9 → score 1. MATCH.
- D3 D/E 627.98/2086.54 = 0.301 → band 0.1-0.5 → score 4. MATCH.
- D4 current ratio 3037.93/2287.96 = 1.328 → band 1.2-1.49 → score 2. MATCH.
Block D = 12. MATCH. The screener-vs-results borrowings discrepancy is
correctly carried as an unscored cross-check for stage 8, not silently
resolved.

### BLOCK E — Shareholder Alignment (re-derived 8/20) PASS
- E1 promoter 43.21% → band 40-49.9 → score 3. MATCH.
- E2 change −6.40pp → decreased >3% → score 0. MATCH. Window is 2.75yr
  (Sep-2023 earliest supplied) not the full 3yr; data-forced, and the
  score is unchanged since the decline already exceeds 3pp.
- E3 pledge N/A → score 0. MATCH, and correctly NOT converted from the
  raw 65,00,000-share AR disclosure into a % (the "never estimate" rule
  honoured; deal-breaker 5 correctly not applied on an unscored input).
- E4 contingent liab 63.96 / net worth 1607.27 = 3.98% → <5 → score 5. MATCH.
Block E = 8. MATCH.

### BLOCK F — Quantitative Moat (re-derived 11/60) PASS
M1 3 (margin stable +0.39pp AND rev CAGR 14.41% >=10%). M2 0 (−3.05pp
below peer median 16.18). M3 1 (FAT 4.13x >3x but ROCE 14.33% only >12%).
M4 3 (1 decline year, recovered). M5 0. M6 0 (R&D N/A). M7 0 (unregulated).
M8 0. M9 0 (GM proxy −10.96pp below peer median). M10 3 (growth 8/9,
receivable days fell). M11 1 (conservative, selling% incomplete FY26).
M12 0. Total 3+0+1+3+0+0+0+0+0+3+1+0 = 11. MATCH.
Moats present (>=3): M1, M4, M10 = 3 → band 2-3 → MODERATE. MATCH.
Note M5: scored 0 with "PEER DATA NEEDED / full segment universe not
supplied." Literal "top 5 mcap = 1" reading against only 4 supplied names
could give 1, but the framework's own rule "if a test needs peer data
that is not provided, score 0" supports the 0. Compliant, not a fail.

### CLASSIFICATION AND OVERRIDES PASS
Core = 6+8+15+12+8 = 49. MATCH. Grand total 49+11 = 60. MATCH.
Data confidence: 10 years → full, no history downgrade. MATCH.
Matrix: core 40-59 → AVERAGE (band does not branch on moat tier). MATCH.
Deal-breakers: only #1 (Block A 6 <8 → max GOOD) triggers; correctly
flagged non-binding since AVERAGE already sits below GOOD. #2 not
triggered (Block B = 8, not <8). #3-#9 correctly not triggered. MATCH.
FLAG-GATE0 emitted (classification <=AVERAGE with named depressors). MATCH.

### GATE 0 — MINOR DEVIATIONS (data-forced, documented, non-score-changing)
The screener source lacks a current/non-current split and a separate
capex line, so three fixed formulae were substituted. Each is anchored,
labelled, and none flips a score band. They are recorded, not waved
through:
1. ROCE denominator: framework = EBIT ÷ (Total Assets − Current
   Liabilities); report used EBIT ÷ (Net Worth + Borrowings). MINOR.
2. FCF: framework = CFO − Capex (PPE+intangibles, exclude acquisitions);
   report used CFO + CFI (full net investing, may include investments).
   Feeds B2/B3. MINOR.
3. WC Days: framework includes − Payable Days; report used Receivable +
   Inventory only (payables not disclosed). Feeds B4 and block_b_trend.
   MINOR.
No CRITICAL, no MAJOR. All scored rules reproduce exactly.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### COMPLETENESS PASS
All 23 categories addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2,
G1-G2, H1-H3, I1-I2, R1). Every empty category carries an explicit
NO EVIDENCE FOUND. Section 3 summary table lists all 23 rows.

### SCORECARD — raw × evidence multiplier re-derived PASS
Raw map (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) and multiplier
(📄1.0, 🎙️0.7, 🔍0.5) checked row by row:
A1 4×0.7=2.8 | A4 1×1.0=1.0 | B2 4×1.0=4.0 | C1 3×0.7=2.1 |
C2 1×0.7=0.7 | E1 3×1.0=3.0 | E2 3×0.7=2.1 | F1 1×1.0=1.0 |
F2 2×1.0=2.0 | G1 2×1.0=2.0 | H1 4×1.0=4.0 | H2 4×0.7=2.8 |
H3 1×1.0=1.0 | R1 3×1.0=3.0. All others 0.
Sum = 31.5 → 32. MATCH. em_score 32 → band 25-39 → MOAT STRENGTHENING. MATCH.

### EVIDENCE-TIER CONSISTENCY PASS
No 🎙️-only category is scored as if 📄. Every mixed-evidence category
(A1, C1, E2, H2) is graded at the conservative 🎙️ 0.7x, not 📄. Pure-📄
categories (A4, B2, E1, F1, F2, G1, H1, H3, R1) take 1.0x correctly.
This is the exact failure mode rule 3 targets, and it is clean.

### FAMILY I STRICT TESTS PASS
I1 (talent asymmetry) scored 0: neither leg evidenced (no named
inventors, no ex-major staff concentration, no remuneration-annexure
technical class). Correct per the both-legs rule; not scored above 0
without the (b) leg carrying a 📄 source.
I2 (cannibalization barrier) scored 0: honest "nothing must be destroyed"
answer, tested against B2/E1/R1 candidates and correctly rejected (Aramco
= time not configuration; Saudi play replicated by peers concurrently;
NCSS open to any locator). Correct per the named-sacrifice rule.
I1/I2 contribution stated separately (0 of 32) for the operator review
checkpoint. Rule honoured.

### COMPLETIONIST GUARD PASS
📄 recount line present and explicit. Active (Strong/Moderate) count = 9,
above the 3-6 base rate but below the 12-category auto-recheck trigger.
The report performed the recount, justified the density (a closed,
exchange-filed acquisition mid-run), and deliberately downgraded four
claim-heavy items (A4, C2, F1, H3) to Weak/None rather than crediting
them. Guard applied as written.

### NOTE (not a fail)
6D combined classification HIGH POTENTIAL: prompt 07 names the label set
but does not embed the full backward×forward mapping matrix, so the exact
cell is not re-derivable from the rule source. AVERAGE-near-top (49) +
MOAT STRENGTHENING (32) → HIGH POTENTIAL with full reasoning is
consistent with the stated transition-setup intent. No deviation found.

### EMERGING MOAT — no MINOR/MAJOR/CRITICAL findings.

═══════════════════════════════════════════════════════════════════
## PHASE-1 CONCLUSION
═══════════════════════════════════════════════════════════════════
Gate 0: all scores, classification, deal-breakers, and CAGR edge rules
applied as written. Three data-forced formula substitutions flagged
MINOR (documented, non-score-changing). No decision-changing deviation.
Emerging Moat: all 23 categories, all multipliers, the completionist
recount, the Family I strict tests, and the classification band applied
exactly as written. No findings.
No CRITICAL, no MAJOR. Recomputed classification concurs: AVERAGE (Gate 0)
/ MOAT STRENGTHENING (Emerging Moat). Valuation audit pending phase 3.

```yaml
stage: B12c
company: "MANINDS"
run_date: "2026-08-21"
model: claude-opus-4-8
status: complete
phase: 1
gate0:
  rules_checked: 40
  findings:
    - {severity: MINOR, location: "B01 Block A ROCE basis", issue: "ROCE denominator substituted EBIT/(NetWorth+Borrowings) for framework EBIT/(Total Assets - Current Liabilities); data-forced (no current-liability split in screener), anchored, no score-band change", recomputed: "no change"}
    - {severity: MINOR, location: "B01 Block B FCF (B2/B3)", issue: "FCF proxied as CFO+CFI for framework CFO-Capex(PPE+intangibles, ex-acquisitions); data-forced (no capex line), stated as proxy, no score-band change", recomputed: "no change"}
    - {severity: MINOR, location: "B01 Block B4 / block_b_trend WC days", issue: "WC days computed ex-payables (Receivable+Inventory only) as payables not separately disclosed; framework formula subtracts Payable Days; stated basis, no score-band change", recomputed: "no change"}
  adherence_pct: 97
emoat:
  rules_checked: 51
  findings: []
  adherence_pct: 100
valuation: pending-phase-3
recomputed_gate0_classification: ""   # concur: AVERAGE (core 49)
recomputed_emoat_classification: ""   # concur: MOAT STRENGTHENING (em 32)
critical_count: 0
major_count: 0
minor_count: 3
framework_adherence: 98   # combined gate0+emoat, phase-1
acceptance_rate: 98       # rules passed / rules checked, phase-1
```
