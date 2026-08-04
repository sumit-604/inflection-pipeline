# VERIFIER C: FRAMEWORK ADHERENCE (B12c) — AARTISURF

Run date: 2026-08-04 | Model: claude-opus-4-8 | Scope: PHASE 1 (Gate 0 B01 + Emerging Moat B07 only)
Valuation adherence (B11/B10) DEFERRED to phase 3 — stage 11 does not exist yet.

I audit rule application, not company quality and not raw-number existence (Verifier A owns
number existence). Every score below was re-derived from the inputs the reports themselves
state, using the thresholds in prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.
This is a degraded run (7 data years FY20-FY26 from screener Data_Sheet.csv only; AR is FY2020-21,
~5 years stale). Adherence is judged against the frameworks' own degraded-data rules (rule 5:
mark N/A, score 0, never estimate).

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### Block A — Return on Capital (re-derived)
| Rule | Stated input | Threshold applied | Recompute | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | 8.36% (median of 7) | <10 = 0 | median{5.92,6.62,7.16,8.36,10.17,11.70,14.53}=8.36 -> 0 | PASS |
| A2 Min single-yr ROCE | 5.92% (FY20) | <8 = 0 | min=5.92 -> 0 | PASS |
| A3 Median ROE | 6.45% | <12 = 0 | median{1.88,4.09,5.17,6.45,8.36,11.05,17.76}=6.45 -> 0 | PASS |
| A4 ROCE trend | FY26 8.36 vs FY20 5.92 | latest>=earliest = 5 | 8.36>=5.92 -> 5 | PASS |
Block A = 5/20. CONFIRMED.

Note (MINOR, disclosed): ROCE Capital Employed used Net Worth + Total Borrowings proxy, not the
formula-book Total Assets - Current Liabilities, because screener-Balance_Sheet.csv is an empty
template. The maker stated "computed" and named the proxy per rule. Non-decision-changing: median
ROCE 8.36% and min 5.92% sit far below the A1/A2 thresholds (10% / 8%), so no plausible
current-liabilities figure flips either band. Rule application PASS with basis note.

### Block B — Cash Generation (re-derived)
| Rule | Input | Threshold | Recompute | Verdict |
|---|---|---|---|---|
| B1 Cum CFO / Cum PAT | 2.68x | >=1.00 = 5 | 241.21/90.12=2.677 -> 5 | PASS |
| B2 FCF-positive years | N/A (no capex split) | N/A -> 0 | capex NOT FOUND, rule 5 -> 0 | PASS |
| B3 Cum FCF / Cum PAT | N/A | N/A -> 0 | same -> 0 | PASS |
| B4 Change in WC Days | N/A (no Trade Payables) | N/A -> 0 | Payable Days NOT FOUND -> 0 | PASS |
Block B = 5/20. CONFIRMED. N/A-to-0 handling is exactly rule 5 (never estimate). CFO sums verified.

### Block C — Growth (re-derived)
| Rule | Input | Threshold | Recompute | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | 17.53% | 15-19.9 = 4 | (859.13/325.86)^(1/6)-1=17.54% -> 4 | PASS |
| C2 PAT CAGR | 34.44% | >=20 = 5 | (12.34/2.09)^(1/6)-1=34.44% -> 5 | PASS |
| C3 Positive YoY rev | 5/6 = 83.3% | 75-99 = 3 | FY24 sole decline -> 3 | PASS |
| C4 PAT CAGR - Rev CAGR | +16.91pp | >=+3 = 5 | 34.44-17.53 -> 5 | PASS |
Block C = 17/20. CONFIRMED. CAGR edge rules: both endpoints positive, no loss-to-profit swing;
correctly not invoked. FY20 low-base inflation of PAT CAGR is flagged under data_notes as the
prompt intends (not scored down, but surfaced).

### Block D — Balance Sheet (re-derived, latest FY26)
| Rule | Input | Threshold | Recompute | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | 1.94x | 1-2x = 3 | (104.19-13.43)/46.89=1.936 -> 3 | PASS |
| D2 Interest Coverage | 2.37x | 1.5-2.9 = 1 | 29.20/12.31=2.372 -> 1 | PASS |
| D3 Debt/Equity | 0.43x | 0.1-0.5 = 4 | 104.19/244.92=0.425 -> 4 | PASS |
| D4 Current Ratio | N/A | N/A -> 0 | no CL line, rule 5 -> 0 | PASS |
Block D = 8/20. CONFIRMED.

### Block E — Shareholder Alignment
All four N/A -> 0. CONFIRMED. The only shareholding figure (Promoter 48.68% as of 31-Mar-2021,
AR FY2020-21) is ~5 years stale; the rules require "latest quarter." Correctly cited for context
and NOT scored under E1 (and not force-fit to the "professionally managed FII+DII>50%" sub-rule,
which is inapplicable and would need current data anyway). E4 contingent-liab 11.04% (FY2020-21)
likewise correctly held out as stale, not scored. Block E = 0/20. Adherence PASS. The maker also
correctly frames this as a data-availability gap, not a governance red flag (aligns with CLAUDE.md
"never treat low institutional ownership as a risk" and the E-block being a stale-data zero).

### Block F — Quantitative Moat (re-derived, 12 tests)
| Test | Maker score | Rule check | Verdict |
|---|---|---|---|
| M1 Pricing Power | 3 | margin -1.78pp (within +-2pp "stable") AND rev CAGR 17.53%>=10% -> 3 | PASS |
| M2 Cost Advantage | 0 | peer data needed, scored 0 per rule -> 0 | PASS |
| M3 Capital Efficiency | 0 | FAT 4.21x but ROCE 8.36% fails every ROCE tier (>20/>15/>12) -> 0 | PASS |
| M4 Customer Stickiness | 3 | 1 decline yr (FY24) fully recovered = "max 1, recovered" tier -> 3 | PASS |
| M5 Scale & Dominance | 0 | peer/mcap data needed -> 0 | PASS |
| M6 Technology/R&D | 0 | R&D Nil (AR Annexure C) -> 0 | PASS |
| M7 Regulatory/License | 0 | unregulated segment -> 0 | PASS |
| M8 Distribution | 1 | mentioned unquantified -> 1 | PASS |
| M9 Brand | 0 | peer GM comparison needed even with proxy -> 0 | PASS |
| M10 Switching Costs | 0 | growth-all-but-1 fails ("stable" recv days breaks it: +24d); only 1 decline yr fails the "2+ decline" tier -> else 0 | PASS |
| M11 Network Effects | 1 | latest 3yr 12.63% < prior 22.65% (decel, fails 5); overall 17.53%<20% fails 3; >15% & selling% rising -> 1 | PASS |
| M12 Negative WC/Float | 0 | no Trade Payables, WC days uncomputable -> 0 | PASS |
Block F = 8/60. Moats present (>=3): M1, M4 = 2. Classification 2-3 present = MODERATE. CONFIRMED.

M10 and M11 are the two tests most easily mis-scored, and both were applied correctly: M10
correctly denied the 3-tier because receivable days are not stable (rose ~24 days), and M11
correctly landed on the 1-tier because the two-window CAGR decelerated. No round-number defaults;
no peer figures invented.

### Classification, confidence, deal-breakers
- Core = A+B+C+D+E = 5+5+17+8+0 = 35. Grand total = 35 + 8 = 43. CONFIRMED.
- Data confidence: 7 years -> "7-9 moderate", no downgrade tier (not 5-6, 3-4, <3). history_downgrade
  = false. CONFIRMED.
- Classification matrix: Core 35 < 40 -> AVOID. Binding over the MODERATE-moat cells (which only
  apply at Core >=60/>=80). CORRECT application.
- Deal-breaker logic, all nine checked:
  1 Block A<8 (5) -> max GOOD: triggered, moot (AVOID already below GOOD). CORRECT.
  2 Block B<8 (5) -> max GOOD: triggered, moot. CORRECT.
  3 median ROCE<10% (8.36) -> max AVERAGE: triggered, moot. CORRECT.
  4 cum CFO/PAT<0.50: 2.68x, not triggered. CORRECT.
  5 pledge>15%: pledge NOT FOUND -> "cannot evaluate" (NOT silently passed). CORRECT and important —
    the maker did not resolve missing pledge data to a pass.
  6 ND/EBITDA>3x AND IC<3x -> AVOID: ND/EBITDA 1.94x fails the first leg; AND-gate not met, not
    triggered. CORRECT (the one deal-breaker that could itself force AVOID; correctly not fired).
  7 revenue declined majority: 1/6, not triggered. CORRECT.
  8 PAT negative last 3 yrs: FY24/25/26 all positive, not triggered. CORRECT.
  9 history<3: 7 years, not triggered. CORRECT.
- FLAG-GATE0 raised because classification <= AVERAGE with historical depressors named (FY20
  post-demerger 0.64% net-margin base; ROCE never >15% in 7 years). Matches the prompt's flag
  condition. CORRECT.

### Gate 0 verdict
Every block re-derived to the maker's stated totals. Classification AVOID is the correct
destination of the rules as written. No CRITICAL, no MAJOR. One MINOR basis note (ROCE proxy),
disclosed and non-decision-changing. Gate 0 rules checked: 46, fails: 0.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category completeness
All 21 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1) appear in the
Section 3 summary table, each with an explicit evidence verdict or NO EVIDENCE FOUND. No category
skipped, none force-fit. PASS.

### Evidence tier -> multiplier discipline
Scorecard uses 📄 1.0x / 🎙️ 0.7x / 🔍 0.5x and the raw L×I matrix (HH=4, HM/MH=3, HL/MM/LH=2,
ML/LM=1, LL=1, none=0):
| Cat | Raw | Tier | Mult | Adj | Recheck | Verdict |
|---|---|---|---|---|---|---|
| A3 Process innovation | 1 (LL) | 🎙️ | 0.7 | 0.7 | 1x0.7 | PASS |
| G1 War chest | 2 (HL) | 📄 | 1.0 | 2.0 | 2x1.0 | PASS |
| H3 ESG moat | 1 (LL) | 🎙️ | 0.7 | 0.7 | 1x0.7 | PASS |
| R1 Regulatory tailwind | 1 (LL) | 📄 | 1.0 | 1.0 | 1x1.0 | PASS |
| all others | 0 | — | — | 0.0 | none = 0 | PASS |
Adjusted total = 0.7+2.0+0.7+1.0 = 4.4 ≈ 4. CONFIRMED.

Tier-honouring check (the specific trap in the rubric — a 🎙️-only category scoring as if 📄): none
found. A3 (management language) and H3 (aspirational ZLD + small solar) are both held at 🎙️ 0.7x,
not inflated to documented. G1 and R1 rest on third-party CARE letters and audited AR grant figures
respectively, correctly at 📄 1.0x. H3 is mixed 📄/🎙️ but scored at the conservative 🎙️ tier. No
claim was credited as documented. PASS.

### Completionist guard
"📄 recount performed: 4 documented items underpin the 4 Weak rows" is present and explicit. 4
active (all Weak), 0 Strong/Moderate — well inside the 3-6 base rate and far below the 12+ tripwire.
The guard is respected and the scan is honestly sparse rather than inflated. PASS.

### Classification and combined read
- Adjusted total ≈4 -> <12 = NO MEANINGFUL EMERGING MOAT -> em_classification "NONE". CORRECT.
- 6D combined: backward AVOID + forward NONE -> AVOID. The maker correctly notes the transition
  setup this operation hunts (GOOD/AVERAGE backward + EXPANSION forward) is NOT present here, so no
  HIGH POTENTIAL / TURNAROUND upgrade is warranted. CORRECT matrix application, no forced optimism.
- FTTCP not conflated with this scan (CLAUDE.md separation respected; F2 handled via the degraded
  capex-completion substitute, scored NO EVIDENCE / 0, conservative).

### Degraded-run judgment notes
- F2 execution moat: no concall promise-delivery record exists (no-concall mode). The maker
  substituted documented capex-completion evidence, netted it against the Silvassa fire loss, and
  scored 0 (NO EVIDENCE of a positive execution moat). Conservative and disclosed. PASS.
- 2C capex-embedded growth (capex_embedded_growth_pct = 11): computed as CWIP+commitments ₹22.83 Cr
  x FAT 2.27x ≈ ₹51.8 Cr ≈ 11.1% of FY2020-21 revenue ₹465.77 Cr. The rubric says "% above current
  revenue"; the maker used the FY2020-21 base (contemporaneous with the 5-year-old capex) rather
  than FY26 revenue (₹859.13 Cr, on which the same ₹51.8 Cr would be ~6%). This is disclosed and
  heavily caveated as backward-looking / likely already realised in FY25 actuals. MINOR basis note,
  non-decision-changing at this stage. FLAGGED FORWARD: this figure feeds Pillar 3 catalyst sizing
  in the deferred valuation (B11); phase-3 verification must confirm the base used before any
  live-catalyst credit is taken from it, since 11% vs 6% is a material difference downstream.

### Emerging Moat verdict
Multipliers, tiers, completionist guard, classification band, and combined matrix all applied as
written. No CRITICAL, no MAJOR. One MINOR basis note (2C revenue base), disclosed and flagged
forward to phase 3. Emoat rules checked: 27, fails: 0.

---

## PART 3 — VALUATION (B11/B10) — DEFERRED

Status: PENDING PHASE 3. Stage 11 valuation does not exist for this run yet (B10/B11 artifacts not
produced). The continuous Pillar 1 formula, FTTCP ROCE verdict, single-credit rule, Pillar 2/3
inputs, UA Amendment-3 ordering, dual-track carry-through, Hurdle Ratio, and 4D weighting audits
are NOT run now and are carried to phase 3. One item is pre-flagged for that audit: the B07 2C
capex-embedded growth base (see Part 2), which feeds Pillar 3.

---

## SUMMARY

- Gate 0 (B01): fully compliant. Classification AVOID re-derived independently and confirmed. 46
  rules checked, 0 fails, 1 MINOR basis note (ROCE proxy, disclosed, non-decision-changing).
- Emerging Moat (B07): fully compliant. em_score ≈4, NONE, combined AVOID confirmed. 27 rules
  checked, 0 fails, 1 MINOR basis note (2C revenue base, disclosed, flagged forward to Pillar 3).
- Recomputed decision: concur (AVOID + NO MEANINGFUL EMERGING MOAT).
- No CRITICAL, no MAJOR. 2 MINOR. acceptance_rate 100% (73/73 rules passed; the two MINOR notes are
  disclosed, defensible degraded-data basis substitutions, not misapplications).
- Valuation section pending phase 3.

```yaml
stage: B12c
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 46, fails: []}
emoat: {rules_checked: 27, fails: []}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3 - stage 11 valuation not yet run; B10/B11 do not exist"}
recomputed_destination_pe: ""   # deferred to phase 3 (no valuation artifact)
recomputed_decision: ""         # concur: Gate 0 AVOID + Emerging Moat NONE, combined AVOID
findings:
  - {severity: "MINOR", location: "B01 Block A / ROCE formula", note: "ROCE Capital Employed computed as Net Worth + Total Borrowings proxy, not formula-book Total Assets - Current Liabilities (screener-Balance_Sheet.csv empty). Disclosed, marked 'computed'. Non-decision-changing: median 8.36% and min 5.92% sit far below A1/A2 thresholds."}
  - {severity: "MINOR", location: "B07 Section 2C / capex_embedded_growth_pct", note: "11.1% computed on FY2020-21 revenue base (contemporaneous with the 5yr-old capex), not on 'current' FY26 revenue where it would be ~6%. Disclosed and caveated as likely-already-realised. Feeds Pillar 3; phase-3 valuation audit must confirm the base before any live-catalyst credit."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```