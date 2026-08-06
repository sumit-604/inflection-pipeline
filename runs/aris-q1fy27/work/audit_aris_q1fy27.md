# A5 ADVERSARY / COMPLETENESS AUDIT — Arisinfra Solutions Limited (ARIS) — Q1 FY27
### Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only
### Unit convention re-derived independently: results filing in Rs Millions, x0.1 to Rs Cr (results header l.7-8). Deck natively Rs Mn.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF exists at review l.582 with all four labelled, non-empty parts:

| Part | Heading present | Location | Content check | Status |
|---|---|---|---|---|
| 1 — Summary narrative | yes | l.584-606 | 21 lines of prose (within 10-20 tolerance); covers headline, the half-one-time PAT split, the omitted QoQ decline, the undisclosed debtor-days master test, nil-ECL, HELD/NO-ADD. Real content. | PRESENT |
| 2 — SECTOR intelligence | yes | l.608-625 | Construction-materials TAM, fragmentation, the ~140-day credit-to-developer "disguised NBFC" channel, Maharashtra 65% / large-EPC 58% concentration. Real content. | PRESENT |
| 3 — BUSINESS-MODEL intelligence | yes | l.627-646 | Three streams with margin/mix, asset-light framing, profit-not-in-parent, GDV-vs-fee caution, payables-stretch WC caution. Real content. | PRESENT |
| 4 — COMPETITION intelligence | yes | l.648-666 | Full-stack orchestration moat claim, Shankara ~11.3x benchmark, credit-risk-premium bear read, Capacit'e shared-cycle risk, "underwriting dressed as software." Real content. | PRESENT |

**AUDIT 0 RESULT: PASS.** All four parts present and substantive. Gate not tripped on this axis.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/manual pass over both A1 extracts, diffed against the two A2 ledgers.

### Results filing (extract_results, 610 lines)
| Category | A2 count | My fresh count | Basis re-derived | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 16 | 16 | SA notes 1-8 (l.225-278) + CO notes 1-8 (l.552-604); CO note 8 numeral line-wraps to l.603 | none | MATCH |
| line_items | 77 | 77 | SA P&L 27 (l.180-222) + SA IPO subtable 6 (l.259-271) + CO P&L 38 (l.475-542) + CO IPO subtable 6 (l.585-595) | none | MATCH |
| zero_standing | 1 | 1 | CO l.493 share of associate net loss (near-nil/blank all periods) | none | MATCH |
| agenda_items | 1 | 1 | Board outcome results-approval item (l.37-44) | none | MATCH |
| auditor_paras | 13 | 13 | SA report 5 paras (l.84,91,100,111,130) + CO report 8 paras (l.308,317,326,352,378,387,412,424) | none | MATCH |
| entities | 8 | 8 | CO auditor para 4 list (l.359-374): 7 subsidiaries + 1 associate | none | MATCH |
| signatures | 5 | 5 | Khara/board (l.56-64), Shah/SA-auditor (l.140-153), Morbia/SA-results (l.281-291), Shah/CO-auditor (l.435-448), Morbia/CO-results (l.608-610) | none | MATCH |
| annexures | 4 | 4 | SA review report, SA results, CO review report, CO results | none | MATCH |

### Presentation deck (extract_presentation, 42 pages)
| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| slides | 42 | 42 | none | MATCH |
| slide_numbers | 211 | 211 (accept A2 exhaustive per-line digit-scan methodology; spot-checked slides 9/34/37/40) | none | MATCH |
| line_items | 70 | 70 (sl.37 16 + sl.38 16 + sl.39 38) | none | MATCH |
| zero_standing | 15 | 15 | none | MATCH |
| footnotes | 10 | 10 | none | MATCH |

**Row-review test (every ledger row either cited in A4 or explicitly "reviewed, no finding"):** A4's LEDGER-RECONCILIATION PREAMBLE (l.14-34) asserts row-by-row review at cited lines and "No ledger row is unreviewed," and A4 explicitly processes A3-01..A3-11 and F16-1..F16-7/F6-1/F10-1. Notes 1-8 walked in Step 0D; auditor paras in the 0D opinion check; entities in Step 2C/Q3/Q16; line items in Step 1 tables; deck flags NO_QTR_BALANCE_SHEET (F16-3), SEGMENT_AXIS_LABEL_ERROR (F16-2/Q9), segment non-reconciliation (F16-1/Q8), KPI-basis/footnote (F16-4/Q11). The ledger FOOTNOTE_ASTERISK_MISMATCH (F2, slide 9) is subsumed by A4's F16-4 slide-9 KPI-basis question. **No orphan row; no row my fresh pass found that the ledger lacks.**

**AUDIT 1 RESULT: PASS.** Counts reconcile 13/13 categories; no coverage FAIL.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers)

All derived metrics recomputed from the raw Mn lines (x0.1). Representative recomputations shown; every table cell was recomputed.

### Consolidated derived (Step 1C / 2A / 2C / 4)
| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBTbxc+D&A+FC-OI) | 30.55 | 26.667+1.902+6.362-4.383 = 30.55 | l.489/484/485/476 | PASS |
| Op EBITDA Q1FY26 | 18.16 | 9.19+0.757+11.738-3.526 = 18.16 | l.489/484/485/476 | PASS |
| Op EBITDA FY26 | 100.68 | 81.13+4.145+27.89-12.493 = 100.67 | l.489/484/485/476 | PASS (0.01 intermediate-rounding) |
| Op EBITDA Margin Q1FY27 | 10.51% | 30.55/290.81 = 10.51% | derived / l.475 | PASS |
| Op EBITDA Margin Q1FY26 | 8.56% | 18.16/212.08 = 8.56% | derived / l.475 | PASS |
| ETR Q1FY27 | 24.9% | 66.36/266.67 = 24.88% | l.508/502 | PASS |
| ETR Q1FY26 | 19.0% | 11.97/63.09 = 18.97% | l.508/502 | PASS |
| PAT Margin Q1FY27 | 6.89% | 20.03/290.81 = 6.89% | l.510/475 | PASS |
| Revenue YoY | +37.1% | (290.81-212.08)/212.08 = 37.12% | l.475 | PASS |
| Op EBITDA YoY | +68.2% | 12.39/18.16 = 68.23% | derived | PASS |
| Op EBITDA margin YoY | +195 bps | 10.51-8.56 = 1.95pp | derived | PASS |
| Finance costs YoY | -45.8% | (6.36-11.74)/11.74 = -45.83% | l.485 | PASS |
| Reported PBT YoY | +322.7% | 20.36/6.31 = 322.66% | l.502 | PASS |
| PAT YoY | +291.9% | 14.92/5.11 = 291.98% | l.510 | PASS |
| EPS diluted YoY | +279.6% | 1.51/0.54 = 279.6% | l.542 | PASS |

### Standalone derived (Step 1C / 2B)
| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| PBT-bef-exc Q1FY26 (OCR-garbled l.194, reconstructed) | (4.14) | Total Inc 132.11 - Total Exp 136.24 = (4.14); ties to PBT (7.02) via exc 2.88 | l.182/192/198/196 | PASS (A4 correctly ignored ledger's mis-carried (70.16) at l.194) |
| Op EBITDA Q1FY26 | (0.37) | -4.135+0.565+9.211-6.012 = (0.37) | l.194/189/190/181 | PASS |
| Op EBITDA Q1FY27 | 7.62 | 9.75+1.362+4.81-8.295 = 7.62 | l.194/189/190/181 | PASS |
| Op EBITDA FY26 | 16.55 | 33.17+3.05+19.95-39.62 = 16.55 | reconstructed l.194 33.17 | PASS |
| ETR Q1FY26 | 31.8% | -2.234/-7.016 = 31.8% | l.204/198 | PASS |
| PAT Margin Q1FY27 | 5.80% | 7.46/128.73 = 5.80% | l.206/180 | PASS |
| Revenue YoY | +2.1% | 2.64/126.09 = 2.09% | l.180 | PASS |

### S-vs-C gap (Step 2C), unreviewed-subs shares, QoQ, PAT bridge
| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| S/C PAT Q1FY27 | 37.2% | 7.46/20.03 = 37.24% | l.206/510 | PASS |
| Subs as % of S Q1FY27 | 168.5% | 12.57/7.46 = 168.5% | derived | PASS |
| Unreviewed subs revenue share | 55.7% | 1,620.83/2,908.09 = 55.74% | l.388/475 | PASS |
| Unreviewed subs PAT share | 63.5% | 127.28/200.31 = 63.54% | l.388/510 | PASS |
| Standalone rev QoQ | -37.9% | (128.73-207.36)/207.36 = -37.92% | l.180 | PASS |
| Consol rev QoQ | -15.3% | (290.81-343.36)/343.36 = -15.30% | l.475 | PASS |
| Consol PAT QoQ | -7.5% | (20.03-21.65)/21.65 = -7.48% | l.510 | PASS |
| Diluted EPS QoQ | -20.5% | (2.05-2.58)/2.58 = -20.54% | l.542 | PASS |
| Debtor days FY26 | 140 | 4,100/10,675 x365 = 140.2 | deck L1152/L1089 | PASS |
| PAT bridge sum | +14.92 | 12.39-1.14+5.38+0.85+0.00+2.88-5.44 = +14.92 | Step 4 lines | PASS (fully reconciles) |
| ESOP grant | 1,633 options, nil vested/exercised/lapsed, EP>=FV Rs 2 | ESOP l.21/72-77/81/84/90 | ESOP extract | PASS (verified) |
| Paid-up +0.07 Mn | +0.07 Mn (~35,000 sh) | 163.59-163.52 = 0.07 Mn; /2 = 35,000 | l.216 | PASS |

### **ARITHMETIC FAIL (1) — Step 8.5 Q8 segment-revenue sum**
- **A4 value (l.536, repeated in YAML l.700):** "slide 36 ... 1,302 / 1,774 / 361 Mn **(sum 3,353)**".
- **Recomputed:** 1,302 + 1,774 + 361 = **3,437 Mn**. Discrepancy **+84 Mn** vs A4's stated 3,353 (well above rounding). A4's stated sum is internally inconsistent with the three components it lists (3,353 is what 1,302+1,774+277 gives; A4 appears to have summed the slide-36 pair with the slide-29 Services figure while printing 361).
- **Source:** deck ledger l.1025 (B2B 1,302 / CM 1,774 / Services 361, all Q1-FY27) vs l.767/786/847 (1,092 / 1,540 / 277).
- **Effect on A4's own point:** the reconciliation gap it raises is actually LARGER (slide-36 sum 3,437 vs cross-slide 2,909 = 528 Mn, not the implied 444 Mn), so the finding survives — but the printed figure is wrong and must be corrected in both l.536 and the YAML question (l.700).
- **Loop back: A4.**

**AUDIT 2 RESULT: FAIL (1 error).** All 40+ other recomputed cells reconcile within rounding; the FY26 consol Op EBITDA 100.67 vs 100.68 is a 0.01 intermediate-rounding artifact and is NOT a FAIL.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the SAME extract)

### Positive claim 1 — "PAT grew ~4x, +291.9% YoY" (Step 2A/2D)
**Bear counter (from extract):** ~40% of the uplift is non-recurring — finance costs -45.8% (+5.38 Cr, IPO debt repayment, l.485) and the absence of the Q1FY26 Rs 2.88 Cr exceptional (note 4, l.196) together = +8.26 Cr pre-tax; finance costs are already at a 6.36 Cr floor on a near-net-cash sheet and will not step down again.
**Survives / already grafted?** ALREADY INCORPORATED — A4 Step 4 bridge, Step 2D #4, and flags decompose the ~4x into "roughly half operating, half one-time balance-sheet reset." Counter does NOT survive as a new graft.

### Positive claim 2 — "Operating EBITDA margin +195 bps YoY is genuine expansion" (Step 2D #2)
**Bear counter (from extract):** the Q1FY27 absolute margin carries ZERO loss-allowance provisioning (l.482 nil) on a ~140-day book; a normalized ~4.5 Cr ECL would cut Op EBITDA to ~26 Cr and the margin to ~9.0%.
**Survives / already grafted?** DOES NOT SURVIVE against the *expansion* claim: the YoY base (Q1FY26) ALSO booked nil ECL (l.482 "-"), so the +195 bps delta is like-for-like clean on provisioning. The absolute-level flattery from nil ECL is a separate point already prominently flagged by A4 (Step 5 l.385-390, flags, Q2). No new graft required.

### Positive claim 3 — "Q1FY27 is at or above the trajectory the thesis needs; annualised EPS ~8.2 vs FY26 6.84 = ahead of run-rate" (Step 6A, l.416/420)
**Bear counter (from extract):** annualising the quarter's diluted EPS (2.05 x4) is invalid on A4's own evidence — the quarter is ~40% one-time (Step 4 bridge), revenue fell -15.3% QoQ and diluted EPS fell -20.5% QoQ (deck L1048/L1078), and the share count is rising (implied ~+16% QoQ, F10-1; diluted-basic spread collapsed to nil, A3-08). The run-rate is decelerating, not "ahead." A4 caveats the ROCE annualisation in the same table ("single-quarter, not reliable") but leaves the EPS annualisation uncaveated, an internal asymmetry.
**Survives / already grafted?** **SURVIVES.** The one-time and QoQ facts live elsewhere in A4 (Steps 3-4) but Step 6A presents the annualised-EPS trajectory as supportive without cross-referencing them and concludes "the blocker is not the headline level." Per the completeness rule this counter must be **grafted into Step 6A**: the annualised-EPS trajectory read is itself flattered by the same non-recurring items Step 4 identified and runs against the sequential decline, so "at or above trajectory" overstates the headline. **Loop back: A4.**

---

## VERDICT

**INCOMPLETE.** Loop back to **A4** on two gaps, both fixable in place:
1. **Arithmetic error (Audit 2):** Step 8.5 Q8 and YAML question segment sum "3,353" must be corrected to **3,437** (1,302+1,774+361); the cross-slide comparison gap is 528 Mn, not the implied figure.
2. **Surviving bear counter (Audit 3, claim 3):** graft into Step 6A the caveat that the annualised-EPS "ahead of run-rate" read is flattered by the ~40% one-time PBT uplift (Step 4) and contradicted by the -15.3% revenue / -20.5% EPS QoQ decline and rising share count; align it with the ROCE annualisation caveat already present.

Audit 0 (deliverable brief) PASS; Audit 1 (coverage) PASS. Only Audits 2 and 3 fail. After A4 applies the two fixes, the review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "ARIS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Step 8.5 Q8 / YAML segment-revenue sum (slide 36 Q1FY27 B2B 1,302 + CM 1,774 + Services 361)", a4_value: "3,353 Mn", recomputed: "3,437 Mn", source_line: "review l.536 & l.700; deck ledger l.1025"}
surviving_bear_counters:
  - {claim: "Step 6A: annualised diluted EPS ~8.2 vs FY26 6.84 = 'ahead of run-rate'; Q1FY27 at or above trajectory", counter: "Annualising is invalid on A4's own evidence: ~40% of the quarter's PBT uplift is one-time (finance-cost reset +5.38 + exceptional absence +2.88, Step 4) and revenue -15.3% / diluted EPS -20.5% QoQ with rising share count (F10-1/A3-08); run-rate is decelerating. A4 caveats ROCE annualisation but not EPS annualisation.", source_line: "review l.416/420; deck L1048/L1078; results l.485/196/542"}
loop_back_to: "A4"
gap: "(1) Arithmetic: correct segment-revenue sum in Step 8.5 Q8 and YAML from 3,353 to 3,437 Mn (1,302+1,774+361); cross-slide gap is 528 Mn. (2) Graft surviving bear counter into Step 6A: annualised-EPS 'ahead of run-rate' is flattered by the ~40% one-time PBT uplift (Step 4) and contradicted by the QoQ revenue/EPS decline and rising share count; caveat it as ROCE annualisation already is."
```
