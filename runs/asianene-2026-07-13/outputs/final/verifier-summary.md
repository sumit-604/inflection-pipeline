# Phase 1 Verifier Summary
Asian Energy Services Limited (ASIANENE) | Run date 2026-07-13

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance |
| --- | --- | --- | --- |
| Numerical acceptance | 91.4 | A (B12a) | 91.4 (35 numbers, 0 critical, 1 major, 4 minor) |
| Redflag coverage | 67 | B (B12b) | 67 (12 flags, 8 caught, 3 partial, 1 minor missed) |
| Framework adherence | 97 | C (B12c) | 97 (84/87 rule applications clean; Gate 0 + EM only) |
| Peer utilisation | 100 | D (B12d) | 100 (8/8 peers substantive) |
| Overall | 67 | min of four | Band 60-74; no REWORK (no CRITICAL, none below 60) |

Valuation adherence (Verifier C rule 4, B11/B10) is deferred to phase 3 and
not scored here.

## Findings, sorted by severity

### CRITICAL
None across all four verifiers.

### MAJOR

| Verifier | Location | Finding |
| --- | --- | --- |
| A (B12a) | B02 Notes Report, Finding #2 | Related party trade receivables 56.4% of gross book is cited from Note 44/50 (pp.100,123-129) but not independently re-derived from the source ledger in verification scope; material for RP concentration risk. |
| B (B12b) | B05 Section 1B / promise-delivery table / red_flags | Standalone FY26 guidance miss under-weighted: the consolidated "+70% to Rs791cr" headline masks a ~20-28% standalone shortfall versus Rs650-700cr once ~Rs290cr of Kuiper (7 months at Rs40-45cr/mo) is stripped out. Anchors: May26 p.4; Nov25 p.10; Sep25 p.6. |

### MINOR

| Verifier | Location | Finding |
| --- | --- | --- |
| A (B12a) | B04 Business Model, Revenue Mix Table | O&G Rs632.8cr (80%) + Minerals Rs158.3cr (20%) = Rs791.1cr reconciles to audited consolidated revenue; presentation clarity gap on consolidated vs standalone, verified correct (Investor Presentation slide 11). |
| A (B12a) | B09 TAM Report, Section 3B | AESL standalone FY26 revenue Rs491.8cr directionally plausible (implied Kuiper Rs299.25cr / 7 months = Rs42.75cr/mo, consistent with mgmt Rs40-45cr/mo); source not independently readable, plausibility cross-checks pass (Investor Presentation slide 9). |
| A (B12a) | B02/B08 MD remuneration | Rs277 Lakh (CG Report p.51) vs Rs157 Lakh (Note 44 p.125) FY25 correctly flagged as cross document inconsistency; reconciliation not provided; governance concern valid, no revenue/profit impact. |
| B (B12b) | B05 promise-delivery table (Kuiper run-rate row) | Kuiper FY27 guide ($60-65mn) is essentially flat on the Rs530-540cr annualized run rate, contradicting Nov25 "grow significantly"; pipeline marks it "delivered" without flagging the soft walk-back. Anchors: Nov25 p.10; May26 p.6, p.9-10. |
| B (B12b) | B05 repeated-question tracker / red_flags | ESOP deflection on Oilmax PAT margin comparability not connected to the 50x valuation fairness flag; the one metric that would test the valuation is waved off. Anchor: May26 p.5-6. |
| B (B12b) | B05 disclosure completeness | Unexplained "write-off" bundled into the Rs9cr Kuiper acquisition exceptional item is not surfaced or probed. Anchor: May26 call p.5 (Sumit Maheshwari). This is the one MISSED flag (not caught upstream). |
| C (B12c) | B01 saved artifact | Mandatory closing YAML block absent from 01-gate0.md (ends line 351); FLAG-GATE0 not confirmable in the file, though B07 consumed B01 values so the block was likely emitted at runtime. Structural / presentational only. |
| C (B12c) | B01 Block A4 | 0.80pp ROCE decline falls in an un-enumerated band gap; resolved conservatively to 3 and disclosed. Had it been 5, core=39, still AVOID. Non-material. |
| C (B12c) | B01 Block F M11 | Held at =3 band rather than =5 because FY26 selling-expense figure NOT FOUND; conservative and disclosed. Had it been 5, moats_confirmed, moat_class and core unchanged, AVOID unchanged. Non-material. |
| C (B12c) | B07 Section 5 F1 | F1 labelled documented in narrative/summary but scored with the 0.7x concall multiplier in the scorecard; conservative direction. At 1.0x, em_score 28.0 -> 28.3, band unchanged (STRENGTHENING). |
| C (B12c) | B07 completionist recount | Recount states "17 documented items across 7 categories" but the enumerated items span 8 categories (F1 ESOP item included); cosmetic count mismatch, guard purpose served. |
| D (B12d) | B06 Part 3 coverage map, "DEEPINDS Q1 FY26 (Aug 2025 call)" | Contribution text cites "69% revenue growth" for Q1 FY26; actual Q1 FY26 figure is 61.6% YoY (Rs199.5cr). The 69.2% figure belongs to Q2 FY26 and is used correctly elsewhere. No verdict affected. |

## Verifier notes

- B (redflag coverage) concurs with credibility grade C (Mixed), judged fair at
  the low end, given the related party 50x deflection and the standalone
  guidance miss partly masked by Kuiper consolidation. Promise-delivery spot
  checks: 5 checked, 5 confirmed, 0 wrong.
- C (framework adherence) concurs with Gate 0 AVOID (core 37, grand 47) and
  Emerging Moat em_score 28.0, STRENGTHENING, combined TURNAROUND. All block
  scores, the classification matrix, data confidence tier, 9 deal-breakers, the
  21-category coverage, every evidence multiplier, the completionist recount and
  the double-credit rule re-derived clean.
- D (peer utilisation) confirms all 8 peer inputs substantive with findable
  citations; no unsupported claims, no verdict discipline fails.
