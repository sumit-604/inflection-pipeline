# A5 ADVERSARY / COMPLETENESS AUDIT — Ram Ratna Wires Ltd (RAMRAT) — Q1 FY27
# Under audit: review_ramrat_q1fy27.md (A4). Fresh context; re-derived from A1 extracts + A2 ledgers.
# All results-extract figures are in ₹ Lakhs; I converted independently (÷100) and recomputed.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers, then A4 citation check)

I re-ran the category counts with my own grep/sweep over each extract and diffed against the
three A2 ledgers. Every A2 count reproduces. The diff bites on **flagged** ledger rows (rows that
carry an open forensic question): each must be cited in A4 or explicitly dismissed.

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| results — notes | 19 | 19 (SA 8 roman + CN 9 roman + 2 asterisk = 19; markers L262-298, L586-624, L202, L523) | none | PASS |
| results — line_items | 121 | 121 (SA P&L 29 + SA seg 25 + CN P&L 37 + CN seg 30) | none | PASS |
| results — zero_standing | 3 | 3 (SA OCI B(i) L191, SA OCI B(ii) L192, CN OCI B(ii) L506) | nil-in-all-periods lines, no economic content | PASS (reviewed, no finding) |
| results — agenda_items | 1 | 1 (single board approval, L17-23) | none | PASS |
| results — auditor_paras | 15 | 15 (SA LRR 4 + CN LRR 11) | none | PASS |
| results — entities | 3 | 3 (TPPL sub; EEPL, RRIEL JV; L381-386 / L595-598) | none | PASS |
| results — signature_blocks | 5 | 5 ("Digitally signed" L52, L136, L304, L444, L628) | none | PASS |
| presentation — slides | 31 | 31 (pages 1-31, no gaps) | none | PASS |
| presentation — slide_numbers | 530 | 530 (re-summed per-slide column: 10+31+12+41+12+27+5+7+1+4+2+32+25+3+7+19+22+9+84+176+1 = 530) | none | PASS |
| pressrelease — summary_table | 5 | 5 (L80-84) | none | PASS |
| pressrelease — quantified_claims | 11 | 11 | none | PASS |
| pressrelease — mgmt_forward_phrases | 18 | 18 | none | PASS |
| pressrelease — structural_narrative | 16 | 16 | none | PASS |

**No row exists in my fresh pass that the ledger lacks** → nothing to loop back to A2. All A2/A3
gate counts are honest.

### Flagged-row → A4 citation map (this is where the failure is)
| A2 flag (ledger row) | Carried into A4? | Where |
|---|---|---|
| LABEL_INCONSISTENCY — "Enamelled" vs "Winding" capital-employed (results §4 row 22, L249) | YES | M8 / FND-05 / A3-10 |
| ZERO_STANDING — 3 nil OCI-reclassify lines | YES (implicit; nil content) | reviewed-no-finding |
| SIGNATURE_TIMESTAMP — deck cover letter (Slide 1) | YES (implicit) | results ledger established board concluded 16:39, all sigs after; no anomaly |
| LABEL_AMBIGUITY — Slide 5 "H1"/"FY" panel prints full-year values | YES | FND-08 / Q14 / QFM |
| EMERGING_LINE_ITEM — first-ever 3.6 Cr exceptional (Slide 29) | YES | FND-01 / Q11 |
| Margin-row Y-o-Y blank (PR Table 1 rows 3, 5) | YES | Step 2 supplies bps |
| ROUNDING (PR 89.6→90, 120.8%→121% etc.) | YES | Reconciliation section |
| UNVERIFIABLE_STANDALONE — 26% copper mix, no comparator (PR) | YES | Q6 / Q13; A4 notes filing discloses 489.98 |
| **LABEL_AMBIGUITY — Slide 27 dividend hash: footnote says Rs 5.0 (2.5+2.5) relates to FY23-24, but the "#" sits on the FY26 column bar (5.0#) while FY24 shows only 2.5** (presentation ledger §E and Slide 27 detail item 22, L393/L402-408) | **NO** | **ORPHAN — not cited, not dismissed anywhere in A4** |

**COVERAGE FAIL (1).** A4's contractual preamble asserts *"All ledger rows reviewed. No unreviewed
rows"* and lists FND-01…FND-11. None of them is the Slide-27 dividend LABEL_AMBIGUITY. A2 explicitly
punted it ("Flag for A3/A4 verification against the statutory dividend history; not resolved here").
A3 produced no finding for it and A4 carries no question, monitorable, or dismissal. It is a live,
unresolved disclosure-quality flag that vanished between A2 and A4. → **return to A3** (missed
forensic; A3 must either raise a finding or explicitly mark it reviewed-no-finding), then **A4** to
incorporate. Materiality is low (a dividend chart footnote on an AVOID-rated name), but the rule is
absolute and A4's blanket "no unreviewed rows" claim is falsified by it.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw ₹ Lakhs, ÷100; A4 value vs my recompute)

Spot-and-full recompute of every derived line in A4's Steps 1-4. Source lines are the results
extract unless noted "deck".

| Metric (period) | A4 value | My recompute (raw source) | Source line | Status |
|---|---|---|---|---|
| SA Operating EBITDA Q1FY27 (PBT+D+FC−OI) | 87.49 | 47.64+11.77+30.36−2.28 = 87.49 | L178/175/174/167 | PASS |
| SA Op EBITDA margin Q1FY27 | 4.78% | 87.49/1831.99 = 4.78% | L166 | PASS |
| SA ETR Q1FY27 | 22.92% | 10.92/47.64 = 22.92% (raw 1092.36/4763.98 = 22.93%) | L186/181 | PASS (rounding) |
| CN Operating EBITDA Q1FY27 (PBTbJV+D+FC−OI) | 89.59 | 47.51+12.77+31.65−2.34 = 89.59 | L487/483/482/475 | PASS |
| CN Operating EBITDA Q1FY26 | 42.88 | 22.18+8.25+16.12−3.67 = 42.88 | L487/483/482/475 | PASS |
| CN Operating EBITDA Q4FY26 | 93.21 | 58.76+12.64+27.83−6.02 = 93.21 | L487/483/482/475 | PASS |
| CN Op EBITDA FY26 (+3.56 excep add-back) | 263.61 | 156.86+37.87+83.82−18.50+3.56 = 263.61 | L490-492/483/482/475/489 | PASS |
| CN Op EBITDA margin Q1FY27 | 4.83% | 89.59/1853.28 = 4.83% | L474 | PASS |
| CN ETR Q1FY27 | 23.72% | 10.93/46.09 = 23.72% (raw 1093.13/4609.48 = 23.71%) | L499/494 | PASS (rounding) |
| CN ETR Q1FY26 | 28.88% | 6.47/22.40 = 28.88% (raw 647.42/2239.66 = 28.91%) | L499/494 | PASS (rounding-propagation; ≤0.03pp, verdict-neutral) |
| CN ETR FY26 | 29.01% | 4437.17/15296.88 = 29.01% | L499/494 | PASS |
| Revenue YoY CN | +88.6% | (1853.28−982.47)/982.47 = +88.64% | L474 | PASS |
| Op EBITDA YoY CN | +108.9% | 46.71/42.88 = +108.9% | derived | PASS (deck +109.0% is deck rounding) |
| Core Op PBT ex-OI YoY CN | +133.6% | (43.75−18.73)/18.73 = +133.6% | L494/475 | PASS |
| PAT YoY CN | +120.8% | 19.24/15.92 = +120.8% | L500 | PASS |
| Finance costs YoY CN | +96.3% | 15.53/16.12 = +96.3% | L482 | PASS |
| Depreciation YoY CN | +54.8% | 4.52/8.25 = +54.8% | L483 | PASS |
| Core Op PBT ex-OI YoY SA | +170.3% | (45.36−16.78)/16.78 = +170.3% | L181/167 | PASS |
| PAT YoY SA | +152.5% | 22.18/14.54 = +152.5% | L187 | PASS |
| Revenue QoQ CN | +5.7% | 100.43/1752.85 = +5.73% | L474 | PASS |
| Op EBITDA QoQ CN | −3.9% | −3.62/93.21 = −3.88% | derived | PASS |
| PAT QoQ CN | −10.4% | −4.07/39.23 = −10.37% | L500 | PASS |
| Copper-tube rev YoY | +256.6% | (489.98−137.39)/137.39 = +256.6% | L223/542 | PASS |
| Copper-tube margin QoQ | 6.58%→4.69% | 22.86/347.20=6.58%; 22.99/489.98=4.69% | L230/223 | PASS |
| PAT bridge: GP change | +68.51 | 164.77−96.26 = +68.51 | L474-480 | PASS |
| PAT bridge: Op EBITDA change | +46.70 | 68.51−6.63−15.18 = +46.70 | derived | PASS |
| PAT bridge: JV drag | −1.64 | −1.42−0.22 = −1.64 | L493 | PASS |
| PAT bridge: reported PAT change | +19.24 | 35.16−15.92 = +19.24 | L500 | PASS |
| ETR tax-shield estimate | ~2.4 Cr (~7% PAT) | PAT@28.88% = 46.09×0.7112 = 32.78; 35.16−32.78 = 2.38 | derived | PASS |
| Residual share capital | ~263 lakh / ~52.6 lakh sh | 4667.45−4404.20 = 263.25 lakh; /5 = 52.65 lakh sh | L195-196 | PASS |
| EEPL implied JV loss | ~(2.03) Cr | (1.42)−(+0.61 RRIEL) = (2.03) | L493/409 | PASS |
| Consol reserves vs SA | 8.7 Cr below | 539.99−531.28 = 8.71 | L197/519 | PASS |
| S-vs-C PAT gap Q1FY26 | +9.52 | (15.9224−14.5379)/14.5379 = +9.52% | L500/187 | PASS |
| S-vs-C PAT gap Q1FY27 | −4.23 | (35.1635−36.7162)/36.7162 = −4.23% | L500/187 | PASS |
| S-vs-C gap swing | 13.7pp | 9.52−(−4.23) = 13.75pp | derived | PASS |
| Deck Net Debt/Equity (recomputed true) | ~1.1x | (265.3+388.8+18.2+2.8−7.8−6.0)/584.9 = 661.3/584.9 = 1.13x | Slide 30 | PASS (A4's "≈660.5" is a 0.8-Cr rounding slip in the addition; ratio conclusion unaffected) |
| Deck formula reproduces 0.46x | 0.46x | (265.3+18.2−7.8−6.0)/584.9 = 0.461 | Slide 28 L822/30 | PASS — confirms current borrowings 388.8 excluded |

**No arithmetic mismatch above rounding.** All ETR variances (≤0.03pp) trace to A4 computing from
2-dp ₹Cr rounded inputs rather than raw Lakhs; every one is verdict-neutral. One trivial addition
slip (net-debt sum 660.5 vs 661.3) does not move the ~1.1x leverage conclusion. **ARITHMETIC PASS.**

### One advisory (not a FAIL) for A4's ledger accuracy
A4 Step 3's **consolidated-labelled** QoQ table cites winding-wire segment result **70.68 → 59.90
(L229, margin 5.08%→4.41%)**, which are the **standalone** segment figures. The consolidated
winding result is **73.15 → 58.43 (L549)** = margin 5.25%→4.31%. Copper is identical SA/CN
(22.86→22.99). The conclusion "both segments lost margin QoQ" holds under either basis, so this is
a source-selection nuance, not an arithmetic error — flagged for tidiness only.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims)

**Positive claim 1 — "Cleanest positive of the quarter: core operating PBT (ex-OI) +133.6% CN;
the operating engine genuinely scaled, not treasury-driven" (Step 2C.3 / Verdict).**
Bear counter from the same extract: the +133.6% is measured off a **pre-Bhiwadi Q1FY26 base**, and
**sequentially the same metric FELL** — core PBT ex-OI 51.36 (Q4FY26) → 43.75 (Q1FY27), −14.8%
(L494/475), with GP% at an all-period low of 8.9% (deck L209). The "engine scaled" YoY while
deteriorating QoQ.
→ **Does NOT survive as new.** A4 already carries this in Step 3, FND-06, and Q5.

**Positive claim 2 — "Copper-tube ramp real (489.98 Cr, +256% YoY); M1 GREEN, T2 favourable and NOT
fired" (Step 2C.1 / 6B-M1 / 6C-T2).**
Bear counter: the ramp added +142.78 Cr of copper-tube revenue QoQ (347.20→489.98, L223) for only
+0.13 Cr of segment result (22.86→22.99, L230) — margin collapsed 6.58%→4.69%. Volume is being
bought at near-zero incremental profit; the ramp is **dilutive to consolidated margin**, so "GREEN"
overstates a metric that is green on revenue and red on profit.
→ **Does NOT survive as new.** A4 already carries this in Step 3, 6D, FND-10, and Q6.

**Positive claim 3 — "PAT +120.8% YoY; the YoY bridge is overwhelmingly recurring/operating"
(Step 4 / Verdict Positive).**
Bear counter: ~7% of PAT (~2.4 Cr) is an unexplained sub-statutory ETR benefit (23.72% vs 25.17%),
JV share is now a −1.64 Cr structural drag, PAT **fell −10.4% QoQ**, and the whole comparison rides
a pre-Bhiwadi base; negative NCI (−0.05 Cr vs +0.47, L511) even lifts owners' PAT above total PAT.
→ **Does NOT survive as new.** A4 already carries the ETR wedge (A3-06/FND-03/Q7), JV drag
(FLAG-JV-DILUTIVE), and QoQ fall (FND-06).

**Adversarial result: NO surviving bear counter to graft.** A4's symmetric bull-bear treatment of
its own positives is genuinely complete — each headline positive is already paired with its
extract-supported rebuttal. This axis passes cleanly.

---

## VERDICT

**INCOMPLETE.**

- **Arithmetic:** clean — no mismatch above rounding across ~40 recomputed metrics.
- **Adversarial:** clean — all three strongest bear counters already incorporated by A4; none survives.
- **Coverage:** ONE orphan. A raised A2 flag (Slide-27 dividend LABEL_AMBIGUITY: the "#" hash on
  the FY26 5.0# bar vs a footnote assigning Rs 2.50+2.50 to FY23-24) was punted by A2 to A3/A4,
  produced no A3 forensic, and appears nowhere in A4 — yet A4's preamble certifies "no unreviewed
  rows." That certification is falsified.

**Loop back to A3:** raise a finding on the Slide-27 dividend LABEL_AMBIGUITY (reconcile the FY24 vs
FY26 dividend attribution against statutory dividend history) **or** explicitly mark it
reviewed-no-finding; then **A4** must incorporate the resolution (a QFM line and/or a one-line
dismissal) and correct the "no unreviewed rows" claim. Only after that does the review proceed to
Notion save.

```yaml
stage: A5-adversary
company: "RAMRAT"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows:
    - "presentation Slide 27 dividend LABEL_AMBIGUITY (ledger Section E / Slide 27 detail item 22, L393/L402-408): '#' hash sits on FY26 5.0# bar while footnote assigns Rs 2.50 interim + Rs 2.50 final to FY23-24; A2 punted to A3/A4, no A3 finding produced, absent from A4 — contradicts A4 'no unreviewed rows'"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: "A3"
gap: "Slide-27 dividend LABEL_AMBIGUITY is an orphan flagged row: A2 raised it and deferred to A3/A4, A3 generated no forensic, and A4 neither cites nor dismisses it despite certifying all ledger rows reviewed. A3 must raise a finding (or explicitly mark reviewed-no-finding) reconciling the FY23-24 vs FY26 dividend attribution; A4 must then incorporate it and correct the 'no unreviewed rows' claim before Notion save."
```
