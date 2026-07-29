# A5 ADVERSARY / COMPLETENESS AUDIT — TRUALT Q1 FY27

Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-29
Fresh context: derived only from A1 extracts (results/presentation/press/chairman), A2 ledgers (results/presentation), and the A4 review. All A4 and A3 cites re-checked, not trusted. Unit conversion: results filing Lakhs x0.01 -> Cr; presentation/press Cr x1.

---

## AUDIT 1 — COVERAGE

Fresh enumeration re-run independently (grep + manual sweep of each extract) and diffed against the two A2 ledgers; then every ledger category checked for citation in A4.

| Category | A2 count | My fresh count | Match | Cited in A4 / reviewed-no-finding | Status |
|---|---|---|---|---|---|
| results: notes | 12 | 12 (6 cons L308-388 + 6 std L574-587) | yes | Step 0D notes table (all 6 subjects) | PASS |
| results: line_items | 67 | 67 (37 cons L211-281 + 30 std L518-547) | yes | Step 1A/1B tables reproduce every row | PASS |
| results: zero_standing | 3 | 3 (Exc L236, Exc L531, Std CurTax L534) | yes | Exceptional nil (Step1); Std current tax zero (F1/F8) | PASS |
| results: agenda_items | 1 | 1 (L50-53) | yes | Preamble + governance note (F13/inter-alia) | PASS |
| results: auditor_paras | 11 | 11 (6 cons + 5 std) | yes | Auditor-opinion check (unmodified + EoM, F5) | PASS |
| results: entities | 3 | 3 (Holding, Leafiniti, TruAlt Gas) | yes | Q11 (F3/F15 Leafiniti trace) | PASS |
| results: segment_tables | 4 | 4 (4A/4B P&L+BS Q1FY27; 4C/4D Q1FY26) | yes(count) | **assets/liabs only (4B/4D) cited in Step 5; segment P&L PBT rows (4A L331 / 4C L350) NOT cited** | **FAIL — orphan** |
| results: signature_blocks | 5 | 5 | yes | Preamble (MD DIN 07413777; CS; auditor) | PASS |
| pres: slides | 32 | 32 (grep ^\[page = 32) | yes | Preamble "ALL 32 reviewed"; body cites each substantive slide | PASS |
| pres: line_items | 47 | 47 (B1-B6: 6+5+7+8+14+7) | yes | Step 1/5/7 reproduce P&L, ratios, capacity | PASS |
| pres: mgmt_numbers | 104 | 104 (Table C sum) | yes | KPI boxes, capacity, guidance surfaced across steps | PASS |
| pres: zero_standing | 1 | 1 (CBG Unit1 partner NA, B3.1) | yes | Leafiniti Unit-1 operational (F3/F15) | PASS |

**Missing-from-ledger (fresh pass found, ledger lacks): NONE.** My independent counts reproduce every A2 count exactly. No under-enumeration by A2.

**ORPHAN ROW (in ledger, absent from A4) — FAIL, return to A3 (missed forensic reconciliation):**
The reviewed filing's consolidated **segment P&L rows** (ledger Section 4A line 331 and 4C line 350: Segment Result, PBT, Tax, PAT per segment) are enumerated by A2 and asserted "reviewed" in A4's preamble, but are **never cited in A4's body**, and where A4 does discuss segment PBT it uses the UNREVIEWED presentation figure that the reviewed filing contradicts:

- Reviewed filing (Note 4, consolidated basis): **CBG segment PBT Q1FY26 = 166.02L = Rs 1.66 Cr -> Q1FY27 = 513.52L = Rs 5.14 Cr, i.e. +209% YoY.**
- Deck slide 11 (C7.6, unreviewed): CBG PBT 5.90 -> 5.28, i.e. **-10.51% YoY.**
- A4's STANDALONE-vs-CONSOLIDATED PAT GAP section (review L408) asserts *"the subsidiary contribution is shrinking YoY at the segment level (CBG PBT -10.51%, presentation C7.6)"* — a bear conclusion built on the deck number and **directly contradicted by the reviewed filing segment P&L (+209%)**, which A4 left uncited and unreconciled.
- Same conflict on the ethanol side: filing ethanol segment PBT Q1FY26 = 413.93L = 4.14 Cr vs deck ethanol PBT Q1FY26 = 0.02 Cr (a ~4 Cr base-quarter reallocation between segments; deck totals tie to consolidated but the segment split does not match the reviewed Note 4 split).

This is a reviewed row left unreviewed in substance AND a reviewed-vs-unreviewed contradiction resolved in favour of the unreviewed source. Loop to A3 to raise the deck-vs-filing segment-PBT reconciliation as a forensic finding; A4 must then re-state the "CBG/subsidiary shrinking" claim against the reviewed +209% figure or explicitly reconcile the two bases.

---

## AUDIT 2 — ARITHMETIC

Every derived metric recomputed from raw Lakhs (x0.01). Named targets first, then a sample of the wider recompute. Values in Rs Cr.

| Metric | A4 value | Recomputed (raw) | Source line | Status |
|---|---|---|---|---|
| **QoQ PAT, consolidated** | -13.9% | (59.27-68.84)/68.84 = **-13.90%** | L245 (6,883.95->5,927.14) | PASS |
| **QoQ PAT, standalone** | **-13.9%** (same tag applied) | (55.01-64.62)/64.62 = **-14.87%** | L536 (6,462.13->5,500.64) | **FAIL (A4)** |
| SC-vs-Cons PAT gap % Q1FY26 | 99.4% | 4.70/4.73 = 99.37% | L245/L536 | PASS |
| SC-vs-Cons PAT gap % Q4FY26 | 6.13% | 4.22/68.84 = 6.13% | L245/L536 | PASS |
| SC-vs-Cons PAT gap % Q1FY27 | 7.19% | 4.26/59.27 = 7.19% | L245/L536 | PASS |
| SC-vs-Cons PAT gap % FY26 | 16.07% | 16.84/104.76 = 16.07% | L245/L536 | PASS |
| ETR cons Q1FY27 | 24.44% | 19.17/78.45 = 24.44% | L239/L237 | PASS |
| ETR cons Q1FY26 | 18.45% | 1.07/5.80 = 18.45% | L239/L237 | PASS |
| ETR std Q1FY27 | 24.96% | 18.30/73.31 = 24.96% | L533/L532 | PASS |
| ETR std Q1FY26 | 84.6% (near-zero base) | 0.11/0.13=84.6% (raw 10.62/13.19=80.5%) | L533/L532 | PASS (flagged nonsense base; immaterial) |
| CBG segment ASSET growth YoY | +278.5% | (227.64-60.14)/60.14 = 278.5% | L339 vs L358 | PASS |
| CBG segment LIAB growth YoY | +187.6% | (131.69-45.79)/45.79 = 187.6% | L340 vs L359 | PASS |
| Ethanol segment asset growth | +38.6% | (3,526.84-2,545.32)/2,545.32 = 38.6% | L339 vs L358 | PASS |
| Op EBITDA cons Q1FY27 | 132.76 | 78.45+24.80+44.03-14.52 = 132.76 | L237/228/226/213 | PASS |
| Op EBITDA cons Q1FY26 | 41.54 | 5.80+20.69+37.79-22.74 = 41.54 | L237/228/226/213 | PASS |
| Op EBITDA margin +bps cons | +751 bps | 21.18%-13.67% = 7.51pp | derived | PASS |
| Op EBITDA margin +bps std | +869 bps | 20.56%-11.87% = 8.69pp | derived | PASS |
| Core PBT ex-OI cons Q1FY26->27 | (16.94)->63.93 | 5.80-22.74=-16.94; 78.45-14.52=63.93 | L237/213 | PASS |
| Core PBT ex-OI std Q1FY26->27 | (22.43)->58.86 | 0.13-22.56=-22.43; 73.31-14.45=58.86 | L532/519 | PASS |
| Revenue YoY cons / std | +106.3% / +109.5% | 322.99/303.89=106.3%; 321.99/293.93=109.5% | L211/L518 | PASS |
| PBT YoY cons (near-zero base) | +1,252.6% | 72.65/5.80 = 1,252.6% | L237 | PASS (artefact, flagged) |
| PAT YoY cons (near-zero base) | +1,153.4% | raw 5,454.62/472.52 = 1,154.4% | L245 | PASS (base-rounding, flagged artefact) |
| PAT bridge cons (sum to +54.54) | +80.87 -8.22 -18.10 +... = +54.54 | 63.93-(-16.94)=80.87; OI -8.22; tax -18.10; net 59.27-4.73=54.54 | Step4 | PASS |
| Core PBT QoQ cons | +1.7% | (63.93-62.86)/62.86 = 1.70% | L237/213 | PASS |
| Revenue QoQ cons | +5.3% | (626.88-595.52)/595.52 = 5.27% | L211 | PASS |

**FAIL detail (loop to A4):** review L205 reads *"Reported PAT actually FELL -13.9% QoQ (68.84->59.27 consolidated; 64.62->55.01 standalone)."* The single figure -13.9% is exact for the consolidated pair only. The standalone pair 64.62->55.01 computes to **-14.87%**, which rounds to **-14.9%**, not -13.9% (0.97pp error, above rounding). The narrative direction (sequential PAT declined) and the consolidated headline are correct everywhere else (Q1 mgmt question, verdict, flags); only the standalone parenthetical on L205 carries the wrong percentage. A4 must correct standalone QoQ PAT to -14.9%.

All other recomputes reconcile within rounding; near-zero-base YoY optics (cons +1,252%/+1,154%, std +55,481%/+213,933%) are internally consistent with the raw figures and already flagged by A4 as artefacts.

---

## AUDIT 3 — ADVERSARIAL READ

A4's three most positive claims, each attacked from the same extracted text.

### Positive claim 1 — "Core operating PBT swung negative->positive (cons (16.94)->63.93); the operating business, not treasury, drove the profit — the cleanest possible read." (Combined Verdict; Step 2 diag 3)
**Bear counter:** The "operationally loss-making before Other Income" framing is an artefact of A4's own PBT-minus-all-Other-Income definition applied to a near-zero base. The reviewed segment note shows **Segment Result** (gross operating result) was already strongly positive in the base quarter: Q1FY26 ethanol 74.85 Cr + CBG 9.29 Cr = **84.14 Cr** (L348), rising to 235.09 Cr (L329). Operations were not "loss-making" at the segment-result line; the negative core-PBT sign in Q1FY26 comes from finance+depreciation on the near-zero-PBT base A4 itself flags. Gross material-cost ratio also improved partly via inventory timing (Q4FY26 built inventory -243.52 / Q1FY27 destocked +47.69, L222), so a single quarter's core PBT is not yet a clean run-rate.
**Verdict:** SURVIVES PARTIALLY but LARGELY GRAFTED. A4 already flags near-zero base (A3-F16-02), OI decline, and inventory timing (Step 3). The one un-grafted element — that the reviewed **Segment Result was positive in the base quarter (84.14 Cr)**, softening the "operationally loss-making" absolute — should be folded into the Combined-Verdict wording. Minor; does not by itself force INCOMPLETE.

### Positive claim 2 — "Operating margin expanded +751 bps (cons)/+869 bps (std), OI-independent, a real operating margin gain; management's ~6% grain-vs-sugar profitability edge CONFIRMED." (Step 2 diag 2; Step 7 cross-check)
**Bear counter:** A ~6% relative profitability edge on grain vs sugar, applied to the 65% (1,300 of 2,000 KLPD) of capacity that is dual-feed (L335), cannot arithmetically generate a **7.51pp (751 bps)** total-EBITDA-margin jump — the order of magnitude is off by roughly 10x. The residual (the great majority of the margin gain) must come from fixed-cost absorption at higher volume (operating leverage), which is **utilisation-dependent at only 60.57%** (L341) and would compress if ESY allocations or utilisation slip. A4 stamps management's 6% attribution "CONFIRMED" (review L331) without testing whether it is sufficient to explain the magnitude.
**Verdict:** SURVIVES — GRAFT INTO A4. The counter is built entirely on extract figures (6% at L338, 751 bps at Step 2, 65%/1,300 KLPD at L335, 60.57% at L341) plus arithmetic. A4 should downgrade the "CONFIRMED" label to "confirmed as a contributor, insufficient to explain the magnitude; the residual is volume-driven fixed-cost absorption that is utilisation-dependent and reverses if the 60.57% run-rate slips."

### Positive claim 3 — "Revenue doubled YoY (cons +106%, std +110%); operating leverage strongly positive, the pre-existing cost base absorbed by the volume step-up; D&A +19.9% and finance +16.5% scaling below revenue." (Step 2 diag 5; Combined Verdict)
**Bear counter:** The favourable D&A/finance-below-revenue optic exists only because the growth capex has not yet hit the P&L: Unit-4 componentization is incomplete so its full depreciation is deferred (EoM, L165-168), and CBG segment assets rose +278.5% YoY (227.64 vs 60.14 Cr, L339/358) with those plants still in CWIP pre-commissioning (Aug-Dec 2026). The Rs 340 Cr Phase-I outlay (L631) precedes revenue. Once these capitalise, the D&A/finance-below-revenue relationship inverts.
**Verdict:** FULLY GRAFTED — does not survive as new. A4 already carries this as F5/F12 in Step 2 diag 5, Step 4, and the Combined Verdict flags. (Note: the ESY 2025-26 disruption, deck L230, falls in the CURRENT periods Q4FY26/Q1FY27, not the Q1FY26 base, so it does not weaken the YoY comparator — no additional bear survival there.)

**Surviving counters requiring graft:** claim 2 (margin-attribution sufficiency) fully survives; claim 1's segment-result nuance partially survives. Both loop to A4.

---

## VERDICT

**INCOMPLETE.**

Three defects block save:

1. **A3 (missed forensic / orphan reviewed row):** the reviewed filing consolidated segment P&L (ledger 4A L331 / 4C L350) is uncited in A4's body, and its **CBG segment PBT +209% YoY (1.66->5.14 Cr)** directly contradicts the unreviewed deck figure **-10.51%** that A4 used to assert the subsidiary/CBG is "shrinking at the segment level" (review L408). A3 must raise the deck-vs-filing segment-PBT reconciliation; A4 must then restate or reconcile the SC-gap conclusion against the reviewed number.

2. **A4 (arithmetic):** standalone QoQ PAT on review L205 is labelled -13.9% but recomputes to **-14.87% (-14.9%)** from L536 (64.62->55.01). Correct the standalone figure; consolidated -13.9% is exact.

3. **A4 (unincorporated surviving bear counter):** the +751 bps margin expansion cannot be explained by a ~6% grain-vs-sugar edge on 65% of capacity; the residual is utilisation-dependent (60.57%) operating leverage. Downgrade the "CONFIRMED" attribution and surface the durability caveat. (Secondary: fold the reviewed base-quarter Segment Result of 84.14 Cr into the "operationally loss-making" wording.)

Counts fully reconcile (no A2 under-enumeration; missing_from_ledger empty). The block is a forensic/reconciliation orphan plus one arithmetic slip and one surviving counter — all cheap, specific fixes. Re-audit after A3 raises the segment-PBT reconciliation and A4 grafts the three corrections.

```yaml
stage: A5-adversary
company: "TRUALT"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows:
    - "results ledger 4A (L331) / 4C (L350) consolidated segment P&L: Segment Result + PBT + Tax + PAT per segment reviewed by A2 but uncited in A4 body; reviewed CBG segment PBT 1.66->5.14 Cr (+209% YoY) contradicts deck CBG PBT -10.51% (C7.6) that A4 relied on at review L408; ethanol segment PBT base-quarter 4.14 Cr vs deck 0.02 Cr also unreconciled"
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "QoQ PAT standalone", a4_value: "-13.9%", recomputed: "-14.87%", source_line: "results L536 (Q4FY26 6,462.13L->Q1FY27 5,500.64L); review L205"}
surviving_bear_counters:
  - {claim: "Operating margin +751 bps is a real, OI-independent gain; ~6% grain-vs-sugar edge CONFIRMED", counter: "A ~6% profitability edge on 65% (1,300/2,000 KLPD) of capacity cannot arithmetically produce a 7.51pp EBITDA-margin jump; the residual is volume-driven fixed-cost absorption, utilisation-dependent at 60.57% and reversible if allocations/utilisation slip", source_line: "pres L338 (6%), L335 (65%/1,300 KLPD), L341 (60.57%); review Step2 diag2, Step7 L331"}
  - {claim: "Core operating PBT swung negative->positive; operations, not treasury, drove profit (operationally loss-making in Q1FY26)", counter: "Reviewed Segment Result was positive in the base quarter (Q1FY26 ethanol 74.85 + CBG 9.29 = 84.14 Cr); the negative sign is an artefact of A4's PBT-minus-all-OI construct on a near-zero base, not a loss at the operating-result line", source_line: "results L348 (Q1FY26 segment result), L329 (Q1FY27); review Step2 diag3, Combined Verdict"}
loop_back_to: "A3"
gap: "A3: raise deck-vs-filing segment-PBT reconciliation as a forensic finding (reviewed consolidated CBG segment PBT +209% YoY, L331/L350, contradicts the unreviewed deck -10.51% that A4 used for its 'subsidiary shrinking' claim at review L408; ethanol base-quarter split 4.14 Cr vs deck 0.02 Cr also unreconciled) so A4 can restate the SC-gap conclusion against reviewed data. Then A4: (a) correct standalone QoQ PAT from -13.9% to -14.9% at review L205; (b) graft the surviving margin-attribution counter (6% edge cannot explain 751 bps; residual is utilisation-dependent operating leverage) and downgrade the 'CONFIRMED' label; (c) fold the positive base-quarter Segment Result (84.14 Cr) into the 'operationally loss-making' wording."
```
