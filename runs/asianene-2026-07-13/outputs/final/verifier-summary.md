# Phase 3 Verifier Summary
Asian Energy Services Limited (ASIANENE) | Run date 2026-07-13

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance |
| --- | --- | --- | --- |
| Numerical acceptance | 91.4 | A (B12a) | 91.4 (35 numbers, 0 critical, 1 major, 4 minor) |
| Redflag coverage | 67 | B (B12b) | 67 (12 flags, 8 caught, 3 partial, 1 minor missed) |
| Framework adherence | 97 | C (B12c full) | 97 (Gate 0 + EM 84/87; phase-3 valuation 30/30) |
| Peer utilisation | 100 | D (B12d) | 100 (8/8 peers substantive) |
| Overall | 67 | min of four | Band 60-74; no REWORK (no CRITICAL, none below 60) |

Framework adherence is the FULL component: phase-1 Gate 0 + Emerging Moat (84/87
rules clean) plus the phase-3 valuation adherence and Role 2 decision audit
(30/30 rules clean, 0 critical, 0 major). The phase-3 audit confirmed the AVOID
as framework consistent, concurred with the pre-correction Track 2 13.2x and
Track 1 RRM 9.3x with no recompute, and confirmed the Tier A assignment and Small
(zero at CMP) sizing. Overall confidence 67 is unchanged from phase 1; redflag
coverage remains binding.

## Note on the two post-verification operator corrections

Two operator corrections were applied to Role 1 AFTER this verifier pass and do
not change any acceptance rate or the confidence delta. Both increase framework
compliance rather than reduce it, because each supplies a framework provision the
baseline had left off for missing data:

1. Undiscovered alpha 1.25x now applied. The full May 2026 shareholding pattern
   resolves the previously unresolved institutional test: FII 1.18% plus DII
   0.75% is 1.93%, below 3%, with all three qualifiers met. The baseline had
   declined undiscovered alpha only because the DII share was unresolved (a
   conservative gap the verifiers noted, not a rule failure). Applying it is the
   framework-correct treatment. Destination PE Track 2 additive moves from 13.2x
   to 19.1x via min(15.24 x 1.25, 20) = 19.05x, applied to the Track 2 additive
   row only, not the reverse rate track.

2. Pillar 3c duration premium now +2x. The Vedanta 4.75 year and Mahanadi 7 year
   documented contracts, about 76% of the standalone order book at 3.56x cover,
   satisfy the four year documented visibility test the framework prices. Pillar
   3 moves from +1x to +3x (3a 0, 3b +1, 3c +2).

Net effect on the audited items: the AVOID decision, the STOP Hurdle verdict, the
Tier A assignment, the triple bound decision trace, and the Small (zero at CMP)
sizing all hold unchanged. The phase-3 valuation adherence rate remains 100%; the
corrections would raise the count of framework provisions correctly applied, not
lower it.

## Findings, sorted by severity

### CRITICAL
None across all five verifier passes (A, B, C phase-1, C phase-3, D).

### MAJOR

| Verifier | Location | Finding |
| --- | --- | --- |
| A (B12a) | B02 Notes Report, Finding #2 | Related party trade receivables 56.4% of gross book cited from Note 44/50 (pp.100,123-129) but not independently re-derived from the source ledger in verification scope; material for RP concentration risk. |
| B (B12b) | B05 Section 1B / promise-delivery / red_flags | Standalone FY26 guidance miss under-weighted: the consolidated "+70% to Rs791cr" headline masks a ~20-28% standalone shortfall vs Rs650-700cr once ~Rs290cr of Kuiper (7 months at Rs40-45cr/mo) is stripped out. Anchors: May26 p.4; Nov25 p.10; Sep25 p.6. |

### MINOR

| Verifier | Location | Finding |
| --- | --- | --- |
| C-p3 (B12c-valuation) | B11 Pillar 2 offset | Offset tempered +0.20 to +0.05; conservative, FTTCP-authorized; immaterial (strict +0.20 still Hurdle STOP). |
| C-p3 (B12c-valuation) | B14 Section 7 re-engagement zone | Re-engagement zone offered under Gate0-AVOID + Promoter-CONCERN; mitigated by ceiling caps + checklist gate; current AVOID unaffected. |
| C-p3 (B12c-valuation) | B11 Hurdle Ratio track choice | Hurdle uses the Track 2 mid, not the governing Track 1 mid; Track 1 gives a deeper STOP; verdict robust either way. |
| A (B12a) | B04 Revenue Mix Table | O&G Rs632.8cr (80%) + Minerals Rs158.3cr (20%) = Rs791.1cr reconciles to audited consolidated revenue; consolidated vs standalone clarity gap, verified correct (Inv. Pres. slide 11). |
| A (B12a) | B09 TAM Report, Section 3B | AESL standalone FY26 revenue Rs491.8cr directionally plausible (implied Kuiper Rs42.75cr/mo, consistent with mgmt Rs40-45cr/mo); source not independently readable, cross-checks pass (Inv. Pres. slide 9). |
| A (B12a) | B02/B08 MD remuneration | Rs277 Lakh (CG Report p.51) vs Rs157 Lakh (Note 44 p.125) FY25 correctly flagged as cross document inconsistency; reconciliation not provided; no revenue/profit impact. |
| B (B12b) | B05 promise-delivery (Kuiper run-rate) | Kuiper FY27 guide ($60-65mn) essentially flat on the Rs530-540cr annualized run rate, contradicting Nov25 "grow significantly"; marked "delivered" without flagging the soft walk-back. Anchors: Nov25 p.10; May26 p.6, p.9-10. |
| B (B12b) | B05 repeated-question tracker | ESOP deflection on Oilmax PAT margin comparability not connected to the 50x valuation fairness flag; the one metric that would test the valuation is waved off. Anchor: May26 p.5-6. |
| B (B12b) | B05 disclosure completeness | Unexplained "write-off" bundled into the Rs9cr Kuiper acquisition exceptional item not surfaced; the one flag MISSED upstream. Anchor: May26 call p.5 (Sumit Maheshwari). |
| C (B12c) | B01 saved artifact | Mandatory closing YAML block absent from 01-gate0.md (ends line 351); FLAG-GATE0 not confirmable in-file, though B07 consumed B01 values so it was likely emitted at runtime. Structural only. |
| C (B12c) | B01 Block A4 | 0.80pp ROCE decline in an un-enumerated band gap; resolved conservatively to 3 and disclosed. At 5, core=39, still AVOID. Non-material. |
| C (B12c) | B01 Block F M11 | Held at =3 rather than =5 because FY26 selling-expense NOT FOUND; conservative and disclosed. At 5, moat class and core unchanged, AVOID unchanged. |
| C (B12c) | B07 Section 5 F1 | F1 labelled documented but scored with the 0.7x concall multiplier; conservative direction. At 1.0x, em_score 28.0 to 28.3, band unchanged (STRENGTHENING). |
| C (B12c) | B07 completionist recount | Recount states "17 documented items across 7 categories" but enumerated items span 8 categories; cosmetic count mismatch, guard purpose served. |
| D (B12d) | B06 Part 3 coverage map, DEEPINDS Q1 FY26 | Contribution text cites "69% revenue growth" for Q1 FY26; actual is 61.6% YoY (Rs199.5cr); the 69.2% figure belongs to Q2 FY26 and is used correctly elsewhere. No verdict affected. |

## Verifier notes

- A (numerical) verified ~35 material figures: 100% of verdict-critical metrics
  (Gate 0 blocks, ROCE, classification drivers), 100% of major P&L/cash-flow
  figures; RP concentration figure anchored but not re-derived.
- B (redflag) concurs with credibility grade C (Mixed), judged fair at the low
  end. Promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong.
- C (framework, phase-1) re-derived Gate 0 AVOID (core 37, grand 47) and
  Emerging Moat 28.0 STRENGTHENING clean, including the 21-category coverage,
  every evidence multiplier, the completionist recount, and the double-credit rule.
- C (framework, phase-3) checked 22 valuation rules and 8 Role 2 rules, all
  substantively passed; AVOID triple-bound (Gate0 AVOID + Promoter CONCERN +
  Hurdle STOP), destination PE and decision concur, no recompute needed. The two
  operator corrections were applied after this pass and increase, not reduce,
  framework compliance.
- D (peer) confirms all 8 peer inputs substantive with findable citations; no
  unsupported claims, no verdict discipline fails.
