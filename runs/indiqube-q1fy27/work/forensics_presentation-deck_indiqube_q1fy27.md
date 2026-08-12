# A3 FORENSIC NOTES — IndiQube Spaces Limited (INDIQUBE)
Quarter: Q1 FY27 | Doctype: presentation (35-slide investor deck) | Model: claude-opus-4-8
Extract: extract_presentation-deck_indiqube_q1fy27.txt | Ledger: ledger_presentation-deck_indiqube_q1fy27.md
Prior extract: NONE (first pipeline run — NO_PRIOR_LEDGER; every slide is baseline for next quarter's diff)

Ledger reconciliation: 234/234 data-point rows (D001–D234) read at their cited slide/line; Tables 1–6
all swept. 100% reconciled. No unread rows.

---
## FINDINGS TABLE
| id | check | ledger row | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | D133/D134/D135, D141, D162, D225 | slide 15 (lines 385-392); slide 16 (line 409); slide 19 (line 528); slide 28 (lines 754-755) | "Signed ₹52 Cr workspace deal with a leading consulting and management services company in Bangalore"; "LOI Signed ... expected to become operational in next 12 to 18 months" | FORWARD-SIGNAL | Dated pipeline: ₹52 Cr signed deal + 39K sqft D&B + 3.9 Lakh sqft Noida supply + 2.77 Mn sqft LOI converting over 12-18M = revenue already contracted but not yet in AUM. Track conversion next quarter. |
| A3-F7-01 | F7 | p22 footnote (line 636); D203 | slide 22 (lines 636-637) | "such revenues are expected to remain a recurring feature of our revenue mix" | AMBIGUOUS | Pre-emptive hedge. VAS One-Time leapt ₹7Cr→₹39Cr (D203) and drove VAS% from 11% to 17%; management is defending durability of a lumpy line before anyone asks. Next-quarter VAS% may fall back if one-time does not repeat. A4 question. |
| A3-F14-01 | F14 | D108 vs D109 | slide 12 (line 318 "96" vs line 321 "97") | "EBIT (A – B – C – D – E) ... 96" vs "EBIT (Ind AS) ... 97" | NEUTRAL-FACT | Internal contradiction: same metric (Q1FY27 EBIT Ind AS) printed as both 96 and 97 on one slide. Direct recompute 449−27−24−188−113 = 97; the "96" cell is the error. ₹1 Cr, immaterial, but a QC lapse in a bridge slide. |
| A3-F14-02 | F14 | D222 | slide 26 (line 729) | "Net Impact on P & L ... 75" | NEUTRAL-FACT | Q1FY27: 264−190 = 74, slide prints 75 (off ₹1 Cr); Q1FY26 column ties exactly (213−140=73). Rounding per p34 disclaimer, but sits beside an exact-tying column. |
| A3-F14-03 | F14 | D155 vs D217 | slide 18 (line 468) vs slide 26 (line 708) | "one cycle of ~3 years" vs "lock in period of around 3.5 years" | AMBIGUOUS | Two different figures for the same client/landlord contractual lock-in cycle. Bears on ALM/payback credibility (capex recovered at 36M vs lock-in 35M/38M). A4 question: true weighted lock-in. |
| A3-F16-01 | F16 | Table 6; D150/D153, D043/D205, D038/D051, D049/D073 | slide 18 (lines 491/493); slide 22 (line 630); slide 8 (line 176) | "₹1,650/sq. ft. Recovered" (only restated numeric) | FORWARD-SIGNAL | Of 7 forward numerics management gave on the Q4 FY26 concall, only 1 is restated here (fit-out capex ₹1,650/sqft). Six hard forward ranges dropped; four survive only as Q1 actuals, two vanish entirely. Post-listing retreat from numeric guidance. |

---
## GUIDANCE / DROPPED-NUMERICS TEST (F16 core — Management-Grade-A tracker)
Seven forward numerics from the Q4 FY26 concall, searched across all 35 slides:

| # | Q4 FY26 concall forward numeric | Status in this deck | Evidence |
|---|---|---|---|
| 1 | FY27 revenue growth 25-30% | PARTIAL | Only Q1 actual YoY +37% shown (slide 8 D045, line 168; slide 6 D029). No FY27 full-year range. |
| 2 | FY27 EBITDA margin 18-21% | PARTIAL | Only Q1 actual 20% shown (slide 8 D049, line 176; slide 10 D073). No forward range. |
| 3 | VAS target 17-18% | PARTIAL | VAS% shown at 17% actual (slide 22 D205, line 630; slide 6 D043). Not framed as a forward target. |
| 4 | FY27 solar 30-35 MW / ₹125-150 Cr capex | ABSENT | "Solar Power" named only as an Eco service line (slide 5, line 121). No MW, no capex figure anywhere. |
| 5 | RPA additions 1.5-2 mn sqft/yr | ABSENT | RPA stock 7.84 Mn shown (D138); LOI pipeline 2.77 Mn (D141). No forward annual RPA-addition rate. |
| 6 | Fit-out capex ~₹1,650/sqft | RESTATED | ₹1,650/sq.ft on slide 18 (D150 line 491, D153 line 493). Value re-committed. |
| 7 | FY27 PAT margin 8-10% | PARTIAL | Only Q1 actual 8% shown (slide 8 D051, line 176; slide 6 D038). No forward range. |

RESTATED = 1 of 7. PARTIAL (actual only, forward range dropped) = 4. ABSENT = 2 (solar, RPA additions).
The two hardest-to-hit capex programs (solar MW/capex, RPA-addition run-rate) are the two that
vanished completely. Classified FORWARD-SIGNAL. First deck post-listing (Jul 30 2025): NO_PRIOR_LEDGER
means the chart-baseline / axis-start half of F16 cannot be diffed this quarter — captured as baseline.

---
## ARITHMETIC-VARIANCE CHASE (recomputed from raw slide numbers)
- **EBIT Ind AS 96 vs 97 (slide 12):** Ind AS EBIT = Total Income 449 − Purchases 27 − Employee 24 −
  D&A 188 − Other exp 113 = **97**. The EBIT-row cell prints **96** (line 318); the Reconciliation
  Summary two rows below prints **97** (line 321). Real ₹1 Cr internal contradiction → A3-F14-01. Q4FY26
  (95=95) and Q1FY26 (60=60) tie cleanly; only the Q1FY27 Ind AS cell is inconsistent.
- **Net Impact on P&L 75 vs 74 (slide 26):** Q1FY27 = 264 − 190 = **74**; slide prints **75** (line 729).
  Q1FY26 = 213 − 140 = 73 ties exactly. Real ₹1 Cr variance → A3-F14-02.
- Both are within the p34 rounding disclaimer in magnitude, but both are *real* (recomputed), so logged
  as FINDINGs per mandate. Classified NEUTRAL-FACT (immaterial ₹1 Cr, no thesis impact) — not escalated
  to A4, but recorded for the promise-vs-delivery QC trail.
- Note (not a variance): IGAAP-Eq EBIT summed from components gives 54 (Q1FY27) / 35 (Q1FY26) vs printed
  55 / 34 — whole-crore rounding of components; consistent with disclaimer, not flagged.

## Ind AS ↔ IGAAP RECONCILIATION CONSISTENCY
Internal deck bridge (slides 11-12) foots within rounding on every period except the 96/97 contradiction
above. The requested deck-vs-**press-release** bridge comparison could NOT be run — no press-release
artifact was provided in A3 inputs. Flag for A4: reconcile slide-11/12 IGAAP-Eq PAT (35/30/19) and EBIT
(55/47/34) against the Q1 FY27 press-release bridge when available.

---
## KPI CORROBORATION — Notion 7-item monitoring checklist
| # | Checklist item | Deck evidence | Read |
|---|---|---|---|
| 1 | Occupancy RPA basis >83%/<80% | Overall Occupancy **86%** (D132 line 142); glossary defines Occupancy = Rent Yielding ÷ Rent Paying = 6.74/7.84 = 85.97% (D137/D138, slide 16/28). RPA-basis occupancy IS disclosed. | GREEN (>83%). Steady-State 90% is a separate mature-center (>12mo) basis, not RPA. |
| 2 | IGAAP-adj PAT positive & growing | PAT (IGAAP Eq) ₹35 Cr, +91% YoY, positive all 3 periods (D080). | GREEN |
| 3 | RPT declining / no new promoter entities | NOT in deck. Innoprop receivable (₹4→₹14Cr) absent. | Carry to Aug 13 concall (pre-committed Q). |
| 4 | Auditor clean & stable board | NOT in deck. Prior-auditor identity absent. | Carry to concall / AR deep-dive. |
| 5 | Net debt IGAAP ex-lease <0.5x/>1.5x | Net Debt **(66)** i.e. net cash; D-E **0.05x** (D060/D062, slide 9); explicitly IGAAP-Eq ex-lease basis. | GREEN (net cash post-IPO). |
| 6 | VAS crossing 15%+/stalling<12% | VAS% **17%** (D205), up from 11%. | GREEN — but One-Time-driven (₹7→₹39Cr); see A3-F7-01 hedge. |
| 7 | CMP vs IGAAP EPS re-rate | EPS (annualized) 6.6 (D054). Valuation not a deck matter. | n/a here. |

Pre-committed Q1 questions (IPO ₹374Cr deployment plan & promoter-linked recipient; prior-auditor
identity; Innoprop receivable ₹4→₹14Cr) are ALL absent from the deck → forwarded to the concall silence
audit (F17 rationale below).

## FTTCP transition evidence (FY26 baseline)
- Revenue Growth FIRING → corroborated: ₹428 vs ₹313 Cr, +37% (D045).
- Margin FIRING → corroborated: EBIT margin 11%→13%, PAT margin 6%→8% (D050/D051).
- Cash Conversion PARTIAL → corroborated: Adjusted Cash EBIT ₹52→₹75 Cr (+44%), margin 17%→18% (D122/D123);
  payment of lease liabilities ₹190 Cr remains the drag (D119).
- ROCE FIRING-SEQUENCED (Y1 dip) → corroborated: net worth ₹395→₹1,194 Cr post-IPO primary raise (D061)
  inflates the denominator and parks ₹343 Cr in cash/deposits (D058/D059) → near-term ROCE dilution expected.

---
## CHECKLIST SCORECARD (all 17)
| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | PASS | 10 ZERO_STANDING rows all explained: 6 are reconciliation-template zeros (Ind AS Adj=0 / IGAAP-Eq=0 for lease-only constructs — canonical), 4 are pre-IPO comparatives now funded (Q1FY26 cash/bank/other-income = 0 → 18/325/8). No hidden exceptional / profit-on-sale / discontinued line anticipated. |
| F2 Standalone vs consolidated | N.A. | No standalone-vs-consolidated statements in deck. |
| F3 Shell-entity detection | N.A. | No S-vs-C cost lines; no entity structure disclosed. |
| F4 Unaudited contribution ratio | N.A. | No auditor report / Other Matters in a presentation. |
| F5 Going concern / EoM | N.A. | No auditor report / EoM paragraph. |
| F6 Forward-commitment phrase mining | FINDING | A3-F6-01: ₹52Cr signed deal, 39K D&B, 3.9 Lakh Noida supply, 2.77 Mn LOI (12-18M), 0.96 Mn under certification. Commitment register below. |
| F7 Hedge phrase mining | FINDING | A3-F7-01: VAS One-Time "expected to remain a recurring feature" — pre-emptive hedge on a lumpy line. |
| F8 Tax forensics | PASS | IGAAP ETR Q1FY27 = 8/43 = 18.6% vs statutory 25.17% (~650bps below), modest and unexplained-but-not-anomalous; current-tax schedule (FY24 8.4 / FY25 7.67 / FY26 21.73 / Q1FY27 est 8.14, D211-214) shows rising cash tax, corroborating real profitability. No "earlier-year" adjustment line. Verify DTA at AR. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in deck. |
| F10 Share count & dilution | PASS | EPS annualized 4.1→6.6 (D054); net worth 395→1194 = IPO primary issuance. No basic-vs-diluted spread or share count disclosed → no dilutive-instrument spread to flag. |
| F11 Reserves / net worth tie-out | PASS | Single Net Worth (B) 1194 (D061); no reserves breakdown and no third-party net-worth figure in context to reconcile against. Nothing to tie out. |
| F12 Segment forensics | N.A. | Business lines described qualitatively; no segment asset/liability/revenue tables. |
| F13 Board outcome beyond results | N.A. | Investor deck; no board resolutions / AGM notice / director-term dates. |
| F14 Note-drafting inconsistencies | FINDING | A3-F14-01 (EBIT 96 vs 97, slide 12); A3-F14-02 (Net Impact 75 vs 74, slide 26); A3-F14-03 (lock-in ~3yr slide 18 vs ~3.5yr slide 26). |
| F15 Entity-list diffs | N.A. | No consolidation entity list; NO_PRIOR_LEDGER. |
| F16 Dropped / reframed disclosures | FINDING | A3-F16-01: 7 Q4FY26 forward numerics → only 1 restated, 4 partial (actual only), 2 absent (solar, RPA additions). Chart-baseline diff deferred (NO_PRIOR_LEDGER). |
| F17 Concall silence audit | N.A. | Concall-specific; this deck PRECEDES the Aug 13 2026 call. No transcript to cross-reference. Pre-committed items (Innoprop RPT, prior auditor, IPO ₹374Cr deployment) absent from deck → handed to the concall silence audit and F3 checklist rows above. |

---
## COMMITMENT REGISTER (F6)
| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| North India expansion — 3.9 Lakh Sq.ft office supply, Noida Expressway | near-term (not yet in AUM) | slide 15, D133, line 385 | "Accelerated" (underway) |
| Signed 39K sqft Design & Build project, Bengaluru (Canadian VFX/animation client) | future revenue recognition | slide 15, D134, line 388 | signed |
| Signed ₹52 Cr workspace deal, Bangalore (consulting/mgmt client) | future revenue | slide 15, D135, line 391 | signed |
| LOI Signed & yet to be Rent Paying — 2.77 Mn sqft pipeline | operational in next 12-18 months | slide 16 D141 line 409; glossary slide 28 D225 lines 754-755 | signed (LOI) |
| Green certification — 0.96 Mn Sq.ft (7 centers) | in-process | slide 19, D162, line 528 | "under certification" (underway) |
| VAS One-Time revenue to "remain a recurring feature of our revenue mix" | ongoing / forward | slide 22 footnote, line 636 | forward claim (also A3-F7-01) |

---
## GATE A3
All 17 checks marked (no blanks). Ledger 100% reconciled. gate_a3 = pass.

```yaml
stage: A3-forensics
company: "INDIQUBE"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/forensics_presentation-deck_indiqube_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F6-01", check: "F6", line: "slide 15 (lines 385-392); slide 16 line 409; slide 28 lines 754-755", classification: "FORWARD-SIGNAL", implication: "Dated contracted pipeline (₹52Cr deal + 39K D&B + 3.9L Noida + 2.77Mn LOI over 12-18M) not yet in AUM; track conversion"}
  - {id: "A3-F7-01", check: "F7", line: "slide 22 lines 636-637", classification: "AMBIGUOUS", implication: "Pre-emptive hedge on VAS One-Time durability (₹7→₹39Cr spike drove VAS% to 17%); next-quarter VAS% may retrace"}
  - {id: "A3-F14-01", check: "F14", line: "slide 12 line 318 vs line 321", classification: "NEUTRAL-FACT", implication: "EBIT Ind AS printed 96 and 97 on same slide; correct = 97; ₹1Cr QC lapse"}
  - {id: "A3-F14-02", check: "F14", line: "slide 26 line 729", classification: "NEUTRAL-FACT", implication: "Net Impact on P&L 75 vs computed 74; ₹1Cr; prior-period column ties exactly"}
  - {id: "A3-F14-03", check: "F14", line: "slide 18 line 468 vs slide 26 line 708", classification: "AMBIGUOUS", implication: "Lock-in stated ~3yr vs ~3.5yr; bears on ALM/capex-payback credibility; A4 question"}
  - {id: "A3-F16-01", check: "F16", line: "slide 18 lines 491/493; slide 22 line 630; slide 8 line 176", classification: "FORWARD-SIGNAL", implication: "Of 7 Q4FY26 forward numerics only 1 restated (fit-out ₹1,650/sqft); 4 partial-as-actuals, 2 absent (solar MW/capex, RPA additions); post-listing retreat from numeric guidance"}
forward_signals: ["A3-F6-01", "A3-F16-01"]
ambiguous: ["A3-F7-01", "A3-F14-03"]
commitments:
  - {commitment: "North India 3.9 Lakh sqft supply, Noida Expressway", implied_date: "near-term (not yet in AUM)", ref: "slide 15 D133 line 385", status_word: "underway"}
  - {commitment: "Signed 39K sqft Design & Build, Bengaluru (Canadian VFX client)", implied_date: "future revenue recognition", ref: "slide 15 D134 line 388", status_word: "signed"}
  - {commitment: "Signed ₹52 Cr workspace deal, Bangalore (consulting client)", implied_date: "future revenue", ref: "slide 15 D135 line 391", status_word: "signed"}
  - {commitment: "LOI pipeline 2.77 Mn sqft yet to be Rent Paying", implied_date: "operational in 12-18 months", ref: "slide 16 D141 / slide 28 D225 line 754", status_word: "signed"}
  - {commitment: "Green certification 0.96 Mn sqft (7 centers)", implied_date: "in-process", ref: "slide 19 D162 line 528", status_word: "underway"}
  - {commitment: "VAS One-Time to remain a recurring feature of revenue mix", implied_date: "ongoing/forward", ref: "slide 22 line 636", status_word: "forward-claim"}
gate_a3: pass
blank_checks: []
```
