# A5 ADVERSARY / COMPLETENESS AUDIT — Sambhv Steel Tubes Ltd (SAMBHV) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Audit date:** 03-Aug-2026
**Under audit:** `review_sambhv_q1fy27.md` (A4) | **Re-derived from:** A1 extracts (results + presentation) and A2 ledgers only. A3 reasoning not consulted; all A4 cites checked, not deferred to.

Fresh-context method: I re-read the standalone clean-copy statement (extract L456-681), the consolidated clean-copy statement (extract L1312-1625), the Board Outcome / Annexures (L40-142), and the deck KPI/income slides (8, 13, 15, 33, 34, 39), then recomputed every derived metric from raw ₹ million cells (÷10 to ₹ Cr) and re-ran the enumeration by grep. Foot was taken against the **clean-copy printed subtotals**; garbled-pass cells were ignored except where the clean pass was itself ambiguous (noted below).

---

## 1. COVERAGE AUDIT

Fresh grep pass vs A2 ledger. Results-filing categories re-counted against the extract; presentation slide inventory re-grepped.

| Category | A2 count | My fresh count | Method / anchor | Orphan rows | Status |
|---|---|---|---|---|---|
| Agenda / meeting items (results) | 7 | 7 | grep `^\s*[a-e]\.` = a–e (L40,45,51,56,65) + commenced/concluded (L75-76) | none | PASS |
| Annexure items (A 8 + B 6) | 14 | 14 | Annexure A L90-116 (8 rows), Annexure B L118-142 (6 rows) read in full | none | PASS |
| Notes / footnotes (results) | 14 | 14 | 5 standalone + 5 consol numbered + 4 footnotes; keyword sweep = 14 hits (IPO/4,400/3,900/balancing/segment) | none | PASS |
| Line items — standalone (27) | 27 | 27 | Every row L456-681 read; all clean-copy values match ledger Table 4 | none | PASS |
| Line items — consolidated (35) | 35 | 35 | Every row L1312-1625 read; all clean-copy values match ledger Table 5 | none | PASS |
| Zero-standing (results) | 6 | 6 | Excep nil std (L562); NCI×3 (L1559/1572/1585); Share-of-investees (L1457); AnnexA existing-cap Nil (L96) | none | PASS |
| Auditor paragraphs | 10 | 10 | Std paras 1-4 (L195-355) + consol paras 1-5 incl. unnumbered Reg33(8) sub-para (L1001-1235) | none | PASS |
| Entities | 3 | 3 | Reporting entity + Holding + Subsidiary "Sambhv Tubes Ltd" (L1157/1161) | none | PASS |
| Signature blocks | 5 | 5 | CS F8459 (L88); MD DIN 00318182 std+consol (L897/1897×2); Auditor 092671 std+consol (L376/1258×2) | none | PASS |
| Slides (presentation) | 43 | 43 | `grep -c "^\[page [0-9]+\]"` = 43 | none | PASS |
| Slide atomic numbers | 1,111 | not simple-grep recountable | methodology-dependent tally; spot-verified slides 8 (L201/207), 13, 15, 33 (L1039), 34, 39 tie exactly — no disclosed number found missing | none surfaced | PASS (spot-verified) |

**Orphan-row check (ledger row present, absent from A4):** none. Every flagged/material ledger row is cited or reconciled in A4:
- EXCEPTIONAL_ITEM_DIVERGENCE (₹35.10 mn consol-only, L1435) → A4 S-vs-C section + Q3 (FIND-01). ✓
- DATE_DISCREPANCY (Bikash Agrawal May 09 appt L58 vs May 08 cessation L130) → A4 Q2 (FIND-08). ✓
- NOTE_LABEL_ANOMALY (std Note 2 "*" marker) → A4 Note-2 row 0D (FIND-09). ✓
- OCR_AMBIGUOUS consol Q4FY26 total-expenses / consol EPS → A4 handled as Q4FY26 comparative, A3-resolved by PBT foot. ✓
- Presentation flags NUMERIC_DISCREPANCY (GP margin) → FND-10; CHART_ONLY_DATA 20MW → FND-04/Q11; FORWARD_COMMITMENT → FND-02; whole-row-nil business-combination line (L1290) → FND-01. ✓
- Filing silence on warrants independently confirmed: grep for `warrant|86,95,400|Anjaneya|convertible` in the results extract = **0 hits**, corroborating A4's FIND-07 ("this filing does NOT disclose the warrant issue"). ✓

**Missing-from-ledger check (fresh pass found a row the ledger lacks):** none.

**Minor note (non-blocking):** A4's reconciliation preamble prose lists "62 line items (27+35), 6 zero-standing" in a way that reads as additive (would sum 121); the headline "115 rows" is nonetheless correct — the 6 zero-standing are a *subset* of the 62 line items / annexure, exactly as the A2 SUMMARY ROW COUNT computes (7+8+6+27+35+14+10+3+5=115). No enumeration is lost; presentational only.

**Coverage verdict: PASS** — no orphan rows, no missing rows.

---

## 2. ARITHMETIC AUDIT

Every derived figure recomputed from raw ₹ mn cells (÷10). Source lines are the results-extract clean-copy rows.

### Standalone
| Metric | A4 value | My recompute | Source (extract L) | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 95.178 | 76.875+12.530+10.721−4.948 = **95.178** | L557/534/528/484 | PASS |
| Op EBITDA Q1FY26 | 72.710 | 45.043+12.003+16.437−0.773 = **72.710** | L559/536/529/486 | PASS |
| Op EBITDA margin Q1FY27 | 13.00% | 95.178/732.173 = **12.9994% → 13.00%** | — | PASS |
| Op EBITDA margin YoY | −2 bps (flat) | 13.00% vs 13.016% = **−1.6 bp** | — | PASS |
| Effective tax rate Q1FY27 | 26.36% | 20.263/76.875 = **26.36%** | L594/569 | PASS |
| ETR Q1FY26 / Q4FY26 / FY26 | 25.85 / 24.87 / 25.29% | 25.85 / 24.87 / 25.29% | L596/595/597 | PASS |
| Core PBT ex-OI Q1FY27 | 71.927 | 76.875−4.948 = **71.927** | L557/484 | PASS |
| Revenue YoY | +31.07% | 173.544/558.629 = **+31.07%** | L476/478 | PASS |
| Core PBT ex-OI YoY | +62.47% | 27.657/44.270 = **+62.47%** | — | PASS |
| Reported PAT YoY | +69.50% | 23.213/33.399 = **+69.50%** | L602/604 | PASS |
| EPS YoY | +38.13% | 0.53/1.39 = **+38.13%** | L670/672 | PASS |
| PAT bridge foot (std) | +23.213 | 22.468−0.527+5.716+4.175 (=+31.832 PBT) −8.619 tax = **+23.213** | — | PASS |

### Consolidated
| Metric | A4 value | My recompute | Source (extract L) | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (III+D+Fin−OI) | 95.144 | 76.860+12.477+10.620−4.813 = **95.144** | L1431/1487(dep 124.77)/1472(fin 106.20)/1354 | PASS |
| Op EBITDA margin Q1FY27 | 13.00% | 95.144/732.173 = **12.9948% → 12.99%** | — | PASS (≤1 bp, rounding) |
| ETR Q1FY27 (Tax/VII) | 26.46% | 20.337/76.860 = **26.46%** | L1492/1462 | PASS |
| Reported PAT YoY | +66.89% | 22.652/33.871 = **+66.88%** | L1501/1503 | PASS (≤0.01 pp, rounding) |
| PBT (VII) YoY | +68.30% | 31.190/45.670 = **+68.30%** | L1462/1463 | PASS |
| PAT bridge foot (consol) | +22.652 | 22.462−0.487+5.176+4.038+0.001 (=+31.190 PBT) −8.538 tax = **+22.652** | — | PASS |

### Standalone-vs-consolidated PAT gap and sign flip
| Period | A4 gap % | My recompute (C−S)/S | Std / Consol PAT (extract L) | Status |
|---|---|---|---|---|
| Q1FY26 | +1.41% | (33.871−33.399)/33.399 = **+1.413%** | L604 / L1503 | PASS (Consol PREMIUM) |
| Q4FY26 | −4.42% | (53.312−55.775)/55.775 = **−4.416%** | L603 / L1502 | PASS (Consol DISCOUNT) |
| Q1FY27 | −0.16% | (56.523−56.612)/56.612 = **−0.157%** | L602 / L1501 | PASS |
| FY26 | −0.78% | (142.151−143.268)/143.268 = **−0.780%** | L605 / L1504 | PASS |
| Sign-flip swing Q1FY26→Q4FY26 | 5.83 pp (>5 pp) | 1.413 − (−4.416) = **5.83 pp** | — | PASS |

Driver of the sign flip re-verified: consol PBT-before-exceptional Q4FY26 (744.03 mn) is **above** standalone (742.35 mn); the flip to a −4.42% PAT discount is caused **entirely** by the ₹35.10 mn consol-only exceptional (extract L1435, nil in standalone L562, carried in no numbered note). A4's diagnosis is arithmetically correct.

### Deck figures — traceability
| Deck figure | A4 use | Traced to | Status |
|---|---|---|---|
| Op EBITDA/tonne ₹9,355 | thesis gate GREEN | presentation extract **L207**, slide 8 | PASS (printed) |
| Op EBITDA/tonne ex-sponge ₹10,002 | secondary | presentation extract **L201**, slide 8 | PASS (printed) |
| Net Debt / Op.EBITDA 1.00x | trigger (e) GREEN | presentation extract **L207**, slide 8; footnote L225 "annualized basis" (A4 flagged) | PASS (printed, basis-caveated) |
| FY26 ROCE deck 15.97% vs Notion 19.1% | discrepancy flagged | presentation extract **L1039**, slide 33 | PASS (real cross-source gap, A4 caught it) |
| FY26 Op EBITDA/tonne ₹6,964; ND/EBITDA 0.78x | comparators | presentation extract **L1039** | PASS |

**Note on OCR twin-pass:** every Q1FY27 cell footed identically on the clean pass and against printed subtotals. The only cells that reconcile "one way only" are the **Q4FY26 consolidated** total-expenses (component-sum ≈6,147.9 vs PBT-implied 6,147.95; ₹0.003 Cr spread) and the **Q4FY26/Q1FY26 consolidated EPS** (1.81 / 1.41, garbled pass) — both are **comparative-period** cells, correctly flagged by A2 and quarantined by A4 with zero effect on any Q1FY27 metric.

**Arithmetic verdict: PASS** — every metric ties; the two consolidated deltas (margin 13.00 vs 12.99%, PAT YoY 66.89 vs 66.88%) are ≤1 bp / ≤0.01 pp presentational rounding, not mismatches above rounding.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each with the strongest bear counter buildable **from the same extracted text**, and whether it survives (i.e., is supported and NOT already incorporated, therefore must be grafted).

**Positive claim 1 — "The quarter is genuinely core-driven; treasury is a minor contributor" (core PBT ex-OI +62.5% YoY; ~70% of the PBT delta is core operating EBITDA; Steps 2/4).**
Bear counter (same extract): (a) Operating EBITDA margin is *not* expanding — flat/−2 bp YoY at 13.00% and actually **down 46 bp QoQ** (13.46%→13.00%, deck L375); the deck's own series shows the margin troughed at **8.68%** in Q3FY26 (L377) and 10.39% in Q2FY26 (L376), so "recovery" is two quarters young. (b) Other Income is **6.4×** YoY and OI/PBT rose 1.72%→6.44%. (c) The −34.8% finance-cost fall is a **non-repeatable base effect** vs a pre-IPO quarter, and sequentially finance cost **rose +8.7% QoQ** (98.63→107.21 mn, L528/L530) — the deleverage benefit has already spent itself and interest is climbing a year before Kesda commissions.
Survives? **No — incorporated.** A4 states the margin is flat/volume-driven, flags the rising OI mix, tags finance-cost relief as IPO-funded and warns it "steps up" as Kesda draws down, shows the Q3FY26 8.68% trough (Step 3), and routes absolute/TTM net debt to FND-06 Q5. The QoQ +8.7% finance-cost tick is the one specific data point A4 does not print; it *strengthens but does not overturn* a bear thesis A4 already carries (rising leverage, non-durable finance relief). Recommended non-blocking add, not a surviving new counter.

**Positive claim 2 — "EBITDA/tonne ₹9,355 clears the gate (GREEN), ~56% above the ₹6,000 line; SS-mix thesis confirming" (Step 6B / 6D).**
Bear counter (same extract): the metric is **historically volatile** — the deck itself (slide 35, L1130) shows FY25 EBITDA/tonne fell to **₹5,321**, *below* the ₹6,000 break line; one quarter above proves nothing, and per-series SS realisation (200-/300-series thresholds) is **disclosed nowhere** in filing or deck, so "SS-mix confirming" is unverifiable from the extract.
Survives? **No — incorporated.** A4 explicitly writes "EBITDA/tonne gate cleared but historically volatile (FY25 dipped to ₹5,321)" and marks monitoring #13 SS realisations UNKNOWN/ND with a management question (FND-05).

**Positive claim 3 — "Q1FY27 lands AT or ABOVE base; zero thesis-broken triggers fired; net thesis MAINTAINED / on track" (Steps 6A / 8 / Section C).**
Bear counter (same extract): "at/above base" is measured against **FY29-anchored** projections used as a proxy because **no FY27 quarterly Bear/Base/Bull exists** (A4's own cells are ND) — a Q1 run-rate mapped to an FY29 endpoint is not a genuine variance test. Two thesis-broken triggers (promoter pledge (c), audit-trail (d)) are **CANNOT ASSESS / NOT DUE** data gaps, and Q1 cash conversion is **INDETERMINATE** (no Reg 33 CFO) — so "on track" rests partly on undisclosed monitorables.
Survives? **No — incorporated.** A4 states the projections are FY29-anchored/ND, caps the verdict at PROCEED WITH CAVEATS on the INDETERMINATE cash reading, and classifies triggers (c)/(d) as data gaps not fires — the full bear qualification is already present and symmetric.

**Adversarial-read verdict:** A4's review is genuinely symmetric — every strongest bear counter constructible from the extract is already carried. **No surviving unincorporated bear counter.** One optional, non-blocking enhancement is offered to A4 (print the +8.7% QoQ finance-cost rise, L528/L530, and soften the "Recurring" tag on the −34.8% YoY finance-cost relief), but the substantive point already lives in Steps 4/5 and FND-06.

---

## VERDICT

**COMPLETE.** Coverage PASS (115/115 results rows + 43 slides re-enumerated, zero orphans, zero missing). Arithmetic PASS (Op EBITDA, margins, ETR, YoY/QoQ walks, both PAT bridges, and the S-vs-C sign flip all re-derived to the cent from the clean-copy cells; the two ≤1 bp consolidated rounding deltas are within tolerance). Adversarial read PASS (A4 is symmetric; no surviving bear counter requiring graft). The deck's ₹9,355 EBITDA/tonne and 1.00x ND/Op.EBITDA both trace to printed slide-8 lines (extract L201/L207). This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "SAMBHV"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
