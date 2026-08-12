# A5 ADVERSARY / COMPLETENESS AUDIT — Stallion India Fluorochemicals, Q1 FY27

Independent re-derivation from A1 extract + A2 ledger only. A4 cites checked, not trusted.
Unit convention verified: filing = Lakhs; conversion to Rs Cr = x0.01 (A1 header lines 7-8).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF (review lines 498-569): all four labelled parts present and non-empty.

| Part | Heading | Location | Content present? |
|------|---------|----------|------------------|
| 1 Summary narrative | "### 1. Summary narrative" | l.500-522 (~21 lines) | PRESENT — real narrative, numbers anchored |
| 2 Sector intelligence | "### 2. Sector intelligence" | l.524-536 | PRESENT — provenance-tagged, Kigali/HFC framing + 30x cap |
| 3 Business-model intelligence | "### 3. Business-model intelligence" | l.539-553 | PRESENT — sourcing/blending model, WC-intensive, IPO reshape |
| 4 Competition intelligence | "### 4. Competition intelligence" | l.556-569 | PRESENT — structural moat/vulnerability, peers deferred |

Gate 0: PASS. All four parts present, none a placeholder.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger vs A4 citation)

Fresh grep-equivalent count re-run over the extract, diffed against the A2 count test (ledger lines 13-23).

| Category | A2 count | My fresh count | Match | Orphan rows (in ledger, absent from A4) | Status |
|----------|:-------:|:-------------:|:-----:|------------------------------------------|--------|
| Financial-results notes | 6 | 6 (l.116,118,120,122,124,140) | yes | none — all 6 in Step 0D table (l.70-75) | PASS |
| Board agenda items | 7 | 7 (main + a-f) | yes | item (a) Secretarial Audit Report (l.32-33) not individually named — see note | PASS (with note) |
| Standalone P&L lines w/ values | 24 | 24 (l.68-97) | yes | none — Step 1 table + memo (incl. ZERO_STANDING l.82, OCI l.88-91) | PASS |
| IPO utilisation rows | 5 | 5 (l.127-133) | yes | none — Step 5 table (l.284-288), incl. ZERO_STANDING row (d) | PASS |
| Auditor limited-review paragraphs | 4 | 4 (paras 1-4, l.172-205) | yes | none — para 3 (l.197) + para 4 (l.198-205) named; paras 1-2 via scope framing | PASS |

Zero-value / standing lines confirmed carried: earlier-period tax adjustment (l.82, nil all periods) addressed at review l.121 & l.251; IPO row (d) GCP 100%/nil-unutilised at review l.287. Both ZERO_STANDING units survived into A4.

No row my fresh pass found is missing from the ledger (nothing to return to A2). No consolidated/segment rows exist (zero grep hits on "consolidat|subsidiar", confirmed independently).

COVERAGE NOTE (not a gate failure): Agenda item (a) — "Took on record the Secretarial Audit Report FY26" (l.32-33, A2 sec 1 row 2, no A2 flag) — is not named individually in the A4 review. It is covered at the grouped level: it belongs to the FY26 annual-report cluster that A4 routes through A3-05 (monitorable l.458, Question 6 l.433). A4's preamble also states "7 board agenda items — reviewed" (l.24) and the count reconciles. Because the unit carries no forensic flag and is dispositioned within the AR cluster, this is a naming-granularity observation, not an orphan FAIL. Recommend A4 name it explicitly for cleanliness.

AUDIT 1 verdict: PASS. Counts reconcile 6/7/24/5/4; no silently dropped disclosure unit.

---

## AUDIT 2 — ARITHMETIC (every derived figure recomputed from raw Lakhs)

Every Step 1 raw conversion (x0.01) re-checked cell-by-cell against l.68-97: all 4 columns of all 24 lines tie (Revenue 121.45/109.99/110.47/430.68; PBT 24.79/16.67/13.86/58.98; PAT 18.57/10.93/10.36/43.84; Net Worth 699.18/680.60/310.27/680.60; etc.). No conversion error.

Derived metrics recomputed:

| Metric (period) | A4 value | Recomputed | Source lines | Status |
|-----------------|:--------:|:----------:|--------------|--------|
| Op EBITDA (all 4 cols) | 14.30/16.35/22.04/57.90 | 14.30/16.35/22.04/57.90 | l.68,69,75,76,79 | PASS |
| Op EBITDA margin | 12.94/14.86/18.15/13.44% | 12.94/14.86/18.15/13.45% | derived / l.68 | PASS (FY26 13.445 rounds either way) |
| Reported EBITDA | 14.37/17.65/25.27/61.35 | 14.37/17.65/25.27/61.35 | l.79,76,75 | PASS |
| Reported EBITDA margin | 13.01/16.04/20.81/14.24% | 13.01/16.04/20.81/14.24% | derived | PASS |
| Core PBT ex-OI | 13.79/15.37/21.56/55.53 | 13.79/15.37/21.56/55.53 | l.79,69 | PASS |
| Other Income / PBT | 0.53/7.80/13.03/5.84% | 0.53/7.80/13.03/5.84% | l.69,79 | PASS |
| Effective Tax Rate | 25.24/34.40/25.10/25.67% | 25.24/34.40/25.10/25.67% | l.84,79 | PASS |
| PAT Margin | 9.38/9.94/15.29/10.18% | 9.38/9.94/15.29/10.18% | l.85,68 | PASS |
| **Gross materials cost / Rev** | 79.54/79.35/76.26/**76.31%** | 79.54/79.35/76.26/**80.14%** | l.72,73,68 | **FAIL (FY26 col)** |
| Revenue YoY | +9.9% | +9.93% | l.68 | PASS |
| Op EBITDA YoY | +54.2% | +54.16% | derived | PASS |
| Op EBITDA margin YoY | +521 bps | +520.7 bps | derived | PASS |
| Depreciation YoY | +33.3% | +33.32% | l.76 | PASS |
| Finance cost YoY | -57.8% | -57.77% | l.75 | PASS |
| Other Income YoY | +4,282.2% | +4,282.2% | l.69 | PASS |
| Core PBT YoY | +56.4% | +56.36% | l.79,69 | PASS |
| Reported PBT YoY | +78.8% | +78.83% | l.79 | PASS |
| PAT YoY | +79.2% | +79.15% | l.85 | PASS |
| EPS YoY | +39.1% | +39.13% | l.93 | PASS |
| Revenue QoQ | +10.4% | +10.41% | l.68 | PASS |
| Op EBITDA margin QoQ | +329 bps | +328.5 bps | derived | PASS |
| Core PBT QoQ | +40.3% | +40.29% | derived | PASS |
| Q1 PAT QoQ | +69.8% | +69.80% | l.85 | PASS |
| PAT bridge: PAT chg | +8.20 | +8.20 | l.85 | PASS |
| — Op EBITDA chg | +7.74 | +7.74 | derived | PASS |
| — Dep chg | (0.10) | (0.097) | l.76 | PASS |
| — Finance chg | +0.13 | +0.126 | l.75 | PASS |
| — Core op PBT chg | +7.77 | +7.77 | derived | PASS |
| — Other Income chg | +3.16 | +3.156 | l.69 | PASS |
| — Tax increase | (2.72) | (2.725) | l.84 | PASS |
| Reported PBT chg | +10.93 | +10.93 | l.79 | PASS |
| Run-rate PBT (ex-OI revert) | ~21.63 | 21.63 | l.79,69 | PASS |
| Run-rate PAT (~25.1% ETR) | ~16.2 | 16.20 | derived | PASS |
| Recurring/non-recurring split | ~71% / ~29% | 70.7% / 29.3% | derived | PASS |
| IPO deploy (a) | 108.8% | 108.78% | l.127 | PASS |
| IPO deploy (b) | 103.4% | 103.38% | l.128 | PASS |
| IPO deploy (c) | 52.0% | 51.98% | l.130 | PASS |
| IPO deploy (d) | 100.0% | 100.0% | l.132 | PASS |
| IPO deploy (e) | 75.0% | 75.03% | l.133 | PASS |
| Net proceeds | 144.75 | 144.75 (14,474.87 x0.01) | l.124 | PASS |

### FAIL detail — the one discrepancy above rounding

**Metric:** Gross materials cost / Revenue, FY26 column (review l.135).
- A4 value: **76.31%**
- Recomputed: **80.14%**
- Raw: (Cost of materials 36,910.24 + Change in inventories (2,395.94)) / Revenue 43,067.80 = 34,514.30 / 43,067.80 = 0.80139.
- Source lines: l.72 (materials), l.73 (inventory change; note FY26 change is NEGATIVE — inventory BUILD, so it reduces the cost base), l.68 (revenue).
- Magnitude: 383 bps error — far above any rounding tolerance.
- The other three columns of this same row are correct (Q1FY26 79.54%, Q4FY26 79.35%, Q1FY27 76.26% all reconcile). The error is isolated to the FY26 cell; the printed value (76.31%) sits suspiciously adjacent to the correct Q1FY27 value (76.26%), consistent with a mis-carried/mis-keyed figure.
- Containment: this FY26 cell is a memo-diagnostic; the load-bearing YoY narrative (Step 1 l.137-139, Step 2 answer 2) uses Q1FY26 79.54% -> Q1FY27 76.26% = ~328 bps, which IS correct and is not affected. But per protocol, any derived-metric mismatch above rounding is a FAIL. Loop back to **A4** to correct the FY26 cell to 80.14%.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest same-text bear counter)

**Claim 1 (l.156, l.169, l.506): "Core operating PBT +56.4% YoY — clean core growth, real."**
Bear counter from the same extract: the 328 bps gross-materials-cost improvement that drives the operating step-up coincides with an unusual inventory DRAWDOWN of +Rs 16.76 Cr (l.73), versus an inventory BUILD of Rs 7.39 Cr in Q1 FY26 — a ~Rs 24 Cr swing in the change-in-inventories line year over year. A material share of the quarter's gross profit therefore reflects selling down accumulated stock rather than a demonstrably repeatable cost structure; the run-rate is unconfirmed until inventory rebuilds (which the WC-object overspend to 108.8%, l.127, suggests is already underway). **SURVIVES** — the inventory swing is on the extract at l.73 and the durability risk is not stated in these terms. A4 notes the destock (l.272, l.545) and asks for a Q2 >=18% margin hold (l.214-215) but does not surface it as an earnings-quality qualifier on the core-PBT claim. Recommend grafting into A4 (Step 2/QoE and the caveats list).

**Claim 2 (l.470, l.511, l.561): "Debt-light, net-cash balance sheet."**
Bear counter: no balance sheet was filed (Reg 33, Q1), so "net cash" is inferred only from finance cost Rs 0.09 Cr and idle IPO FDs; gross debt and exact net position are ND. **DOES NOT SURVIVE as unaddressed** — A4 already caveats this explicitly as qualitative with the exact figure ND (l.277, l.306) and does not overclaim a number.

**Claim 3 (l.151, l.166, l.503): "Operating EBITDA margin +521 bps YoY to 18.15%, genuine not treasury-driven."**
Bear counter: same root as Claim 1 (the margin gain rides the same gross-materials ratio move that is entangled with the inventory drawdown), plus the QoQ comparison base (Q4 FY26) is a Note-4 balancing/derived figure, weakening "durable step-up" read. **PARTIALLY SURVIVES** but is materially covered — A4 flags Q4 as a derived balancing figure (l.200, l.208-209) and defers durability to a Q2 margin test. Net incremental content over Claim 1 is small; folds into the Claim-1 graft.

Net: one surviving bear counter to graft into A4 (inventory-drawdown / destocking earnings-quality qualifier on the core-PBT and margin claims).

---

## OTHER GATE CHECKS

- A3 findings -> management questions: all seven (A3-01..A3-07) map to at least one question (Q1->A3-01, Q2->A3-07, Q3->A3-03, Q4->A3-01/03, Q5->A3-02, Q6->A3-05, Q7->A3-06, Q8->A3-04). PASS.
- Cash conversion: INDETERMINATE, verdict capped at PROCEED WITH CAVEATS with the missing evidence named (H1 FY27 cash flow statement + balance sheet). Does not resolve above CAVEATS. PASS.
- NOT FOUND / ND used instead of estimates throughout (Notion projections, CFO rows, exact net-cash). No fabricated figures. PASS.
- Unit conversion x0.01 applied consistently. PASS.

---

## VERDICT

**INCOMPLETE.**

Loop back to: **A4.**

Gaps (both to A4):
1. **Arithmetic FAIL (mandatory fix):** Step 1 derived table, FY26 "Gross materials cost / Revenue" cell = 76.31% is wrong; correct value is **80.14%** ((369.10 + (23.96 build)) / 430.68). 383 bps error, above rounding. Correct the cell. Load-bearing YoY narrative is unaffected but the metric must reconcile.
2. **Surviving bear counter (graft before save):** add the inventory-drawdown / destocking earnings-quality qualifier — the +Rs 16.76 Cr inventory release (vs a Rs 7.39 Cr build a year prior, l.73) means part of the 328 bps gross-margin gain and the +56.4% core-PBT growth may reflect stock liquidation rather than a repeatable cost structure; durability unconfirmed until inventory rebuilds.

All other gates (deliverable-completeness, coverage 6/7/24/5/4, unit conversion, A3->question mapping, INDETERMINATE cash-conversion cap, NOT-FOUND discipline) PASS. No loop-back to A2 (enumeration reconciles) or A3 (no orphan forensic row; the one coverage note is a naming-granularity item, not a dropped unit).

---

```yaml
stage: A5-adversary
company: "STALLION"
quarter: "Q1FY27"
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
  - metric: "Gross materials cost / Revenue (FY26 column)"
    a4_value: "76.31%"
    recomputed: "80.14%"
    source_line: "l.72 (materials 36,910.24) + l.73 (inv change (2,395.94)) / l.68 (revenue 43,067.80) = 34,514.30/43,067.80"
surviving_bear_counters:
  - claim: "Core operating PBT +56.4% YoY and Op EBITDA margin +521 bps are clean/genuine (l.156,166,169)"
    counter: "The 328 bps gross-materials gain coincides with a +Rs 16.76 Cr inventory drawdown vs a Rs 7.39 Cr build a year earlier (~Rs 24 Cr swing); part of gross profit reflects stock liquidation, run-rate unconfirmed until inventory rebuilds (WC object already overspent to 108.8%)"
    source_line: "l.73 (change in inventories); l.127 (WC object 108.8%)"
loop_back_to: "A4"
gap: "A4 Step 1 derived table FY26 'Gross materials cost / Revenue' = 76.31% is arithmetically wrong (correct 80.14%, a 383 bps error above rounding); and the inventory-drawdown/destocking earnings-quality bear counter survives from l.73 and must be grafted into A4's Step 2/QoE and caveats before save."
```
