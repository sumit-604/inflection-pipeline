# A3 FORENSIC NOTES — Exicom Tele-Systems Limited (EXICOM), Q1 FY27 — DOCTYPE: PRESS RELEASE (presentation branch)

Source extract: extract_pressrelease_exicom_q1fy27.txt (4 pages, 146 body lines).
Ledger reconciled: 100% — every A2 row (P1-P4, QC1-QC26, LI1-LI4, NE1-NE14, MQ1, FN1-FN3, SB1) read at its cited line before judging.
Prior-quarter extract: NONE (first run). prior_context.md used as memory-to-weigh for F16 framing comparison only, never as this quarter's anchored evidence.

Doctype scoping applied per instruction line 128-131 and task brief: F16 applies; F6 forward-commitment mining applies; F10/F11 apply only to numbers the release carries (it carries none). F17 N.A. (not a concall). Balance-sheet checks F1-F5, F7-F9, F12-F15 N.A. — a 4-page Reg. 30 press release carries no notes, no auditor letter, no cost lines, no share count, no segment assets/liabilities, no entity list.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| FND-01 | F16 | QC1-QC3 / MQ1 / LI2 | 60-63, 71 | "Exicom Opens FY27 with Order Wins... as Revenue Grows Sharply Year on Year" / "Standalone revenue up ~57% YoY, EBITDA more than doubles" / consol EBITDA loss "narrowing to ~₹22 crore" | AMBIGUOUS | Headline + first bullet lead with standalone-positive; the pre-committed BEAR metric (consol EBITDA ~-Rs22 Cr, per prior_context) is framed only as "narrower YoY," never as a loss in the headline. A4: convert to management question on the consolidated profitability path. |
| FND-02 | F16 | LI4 (`PAT_EBITDA_GAP_UNEXPLAINED`) | 145 | table: Consol PAT "(73.5)" vs "(54.3)" prior quarter | FORWARD-SIGNAL | Consolidated PAT loss WIDENED sequentially (Rs73.5 Cr vs Rs54.3 Cr) even as consol EBITDA loss narrowed YoY. The ~Rs51.6 Cr below-EBITDA delta (D&A / finance cost / exceptional / minority) is unexplained in narrative; narrative cites only EBITDA. A4 must ask what drove the widening PAT loss. |
| FND-03 | F16 | QC-narrative / LI1-LI2 | 76 | "Revenue and profitability, however, declined sequentially, from Q4 FY26, as is usually the case in the first quarter." | AMBIGUOUS | Consol EBITDA swung +0.27 Cr (Q4 FY26) to (21.9) Cr QoQ; framed as routine seasonality. DC "ran softer" (line 88) similarly attributed to budget-setting. Lean bear: verify whether the QoQ EBITDA reversal is fully seasonal or margin-structural. |
| FND-04 | F16 | QC9 / MQ1 | 77-79, 129 | "gross margin - 31.7% against 39.4% a year ago. A bulk of this can be attributed to the external cost environment including exchange rate volatility and input cost pressures" / "cost pressure took more out of margins than what we anticipated" | AMBIGUOUS | 770 bps YoY gross-margin compression attributed wholly to external factors (FX + input costs); CEO concedes the miss exceeded internal expectation. Forward: is recovery FX-timing dependent or mix/pricing-structural? A4 question on margin bridge. |
| FND-05 | F16 (cross-source) | QC11 (`XCHECK_CONCALL`) | 87-88 | "Exicom recorded a YoY growth of 35% in Q1 FY27" | AMBIGUOUS | Press release states AC +35% YoY; task flags concall reportedly says "AC may have grown by 30%." Concall not in this input set — reconcile the 35% vs ~30% variance at A4. Directional overstatement in the reader-facing release if concall is lower. |
| FND-06 | F16 | QC12 (prior-context cross-note) | 89 | "Exicom's India EV business grew revenue 15% year-on-year" | FORWARD-SIGNAL | Prior_context T3 recorded India-EV "was FIRING +60% YoY" at the Q4 FY26 / Delhi-policy review. If the base is definitionally the same, +15% is a sharp deceleration. Lean bear; A4 to verify segment-scope consistency before treating as a trend break. |
| FND-07 | F6 | QC14, QC15, QC21 / NE8, NE10 | 96, 98, 114-117, 124 | "working towards doubling its AC line capacity starting Q3" / "orders for over 180 DC chargers... till October 2026" / "on track for EBITDA breakeven in Q4 FY27" | FORWARD-SIGNAL | Dated management commitments feeding the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. See Commitment Register below. |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | A2 zero_standing count = 0; the 4 summary line items (LI1-LI4, lines 139-145) are populated in all 6 periods. No template zero lines exist in a press-release table. |
| F2 STANDALONE vs CONSOL DECOMP | N.A. | Release carries only summary SA/Consol totals (lines 139-145); no entity-level data (JV/associate share, subsidiary, eliminations) to decompose. SA-vs-Consol PAT gap (+4.9 vs -73.5) observed and routed to FND-02. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines (materials/employee/depreciation) disclosed; SA-vs-Consol cost comparison impossible in a press release. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters / component-auditor disclosure in a Reg. 30 press release. |
| F5 GOING CONCERN / EoM | N.A. | No auditor's report or EoM paragraph present. Prior_context notes prior auditor unmodified, no EoM (Q4 FY26) — memory only. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Multiple dated commitments (lines 96, 98, 116-117, 124); see Commitment Register and FND-07. |
| F7 HEDGE PHRASE MINING | N.A. | Presentation doctype has no financial-statement notes to mine for pre-emptive legal hedges; only the standard statutory forward-looking disclaimer (line 159-160, "Actual results may differ materially"), which is boilerplate not a newly-added risk hedge. Seasonality/"building resilience into our supply chain" language captured under F16 (FND-03/04). |
| F8 TAX FORENSICS | N.A. | No tax line, ETR, or deferred-tax disclosure in the release. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in the release. |
| F10 SHARE COUNT & DILUTION | N.A. | Release carries NO paid-up capital, share count, or EPS figure (table = Revenue/EBITDA/EBITDA%/PAT only, lines 139-145). Nothing to check. Prior_context (rights issue, 13.91 Cr sh) is memory, not this doc. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No Other Equity or net-worth figure carried in the release; no third-party (rating/slide) number to reconcile against. |
| F12 SEGMENT FORENSICS | N.A. | Only narrative segment revenue-growth mentions; no segment assets/liabilities table. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Cover letter states results approved by Audit Committee and Board "today, i.e., August 10, 2026" (lines 38-39); no AGM notice, dividend, record date, director appointment, or AR/MD&A approval disclosed. Nothing beyond the results. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No formal notes / auditor letter to cross-check. (Trivial typo "Pess Release" line 57 noted, immaterial, not a governance data point.) |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in the release; no prior-quarter press-release ledger (`FIRST_RUN_NO_PRIOR_LEDGER`). |
| F16 DROPPED/REFRAMED DISCLOSURES + FRAMING | FINDING | Core check for this doctype. FND-01 (headline buries consol loss), FND-02 (widening PAT loss unexplained), FND-03 (seasonal framing of QoQ EBITDA reversal), FND-04 (gross-margin compression attribution), FND-05 (AC +35% cross-source), FND-06 (India-EV deceleration vs prior +60%). |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall. Note: this press release pre-empts NONE of the 11 carried monitoring questions in Q&A form; it touches data points for Q3 (Tritium order intake $20.8M, line 113), Q6 (SA margin 8.8% down from 10.6%; margin-miss admission, line 129), and Q8/Q11 (India-EV +15% vs prior +60%, FND-06). Full silence audit deferred to the concall ledger. |

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref (line) | status word |
|-----------|--------------|-----------|-------------|
| Double AC line capacity | Q3 FY27 | 96 | initiated ("working towards... starting Q3") |
| Deliver 180+ DC chargers to Bus/Truck OEMs & CPOs | by October 2026 | 98 | underway (orders secured) |
| Tritium meaningful scale | from Q2 FY27 onwards | 116 | forward (guided) |
| Tritium EBITDA breakeven | Q4 FY27 | 117 | on-track (guidance reaffirmed vs prior_context T2) |
| TRI-FLEX high-power system to revenue | pending validation | 114 | underway ("under lab validation" with largest US open network) |
| GRID-FLEX first live site | June 2026 | 115 | completed (first unit operating at hyperscale customer) |
| BESS base to scale | FY27 | 124 | forward ("early base we expect to scale") |
| Broad delivery on order book | through FY27 | 132 | forward (CEO: "commitments that deliver through FY27") |

---

## NOTES FOR A4
- FND-02 and FND-06 and FND-07 are FORWARD-SIGNAL; FND-01, FND-03, FND-04, FND-05 are AMBIGUOUS — all seven flagged for A4 to convert into management questions.
- The pre-committed Q1 FY27 decision metric (consol EBITDA >= 0 bull / < -Rs20 Cr bear; prior_context) resolves to the BEAR outcome at ~-Rs22 Cr (LI2, line 141) and reverses Trigger T1 from the Q4 FY26 +Rs0.27 Cr print. This is framing context for FND-01; decision stays human, flag prominently.
- GRID-FLEX first-live (line 115) is a completed milestone (confirmatory positive) that partially addresses monitoring Q4 (hyperscaler); the FAT sign-off DATE is still not stated — carry to concall.
