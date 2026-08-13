# A5 ADVERSARY / COMPLETENESS AUDIT — IPCL Q1 FY27 (results only) — RE-RUN vs REVISED A4

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Doctype:** results (Role 5 N.A.)
**Under audit:** REVISED `review_ipcl_q1fy27.md` (A4, carries post-A5 revision note l.7) | **Re-derived from:** `extract_results_ipcl_q1fy27.txt` (A1), `ledger_results_ipcl_q1fy27.md` (A2)
Independence: re-read the current review file fresh; every count and metric below is re-run from the raw extract/ledger, not taken from A4.

This is the second pass. Pass 1 returned INCOMPLETE → A4 for one unincorporated surviving bear counter (the l.154 inventory build). This pass re-verifies deliverable, coverage, arithmetic, and whether that counter is now grafted.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Present / Empty | Real content? |
|---|---|---|---|
| (1) Summary narrative | l.366-368 | PRESENT | Yes — now leads with the cash-quality caveat, all figures anchored |
| (2) SECTOR intelligence | l.370-373 | PRESENT | Yes — inventory-build demand-backing caveat added |
| (3) BUSINESS-MODEL intelligence | l.375-378 | PRESENT | Yes — inventory build named as key model signal |
| (4) COMPETITION intelligence | l.380-383 | PRESENT | Yes — unchanged, still complete |

**Gate result: PASS.** All four present and non-empty.

---

## 1. COVERAGE AUDIT (fresh enumeration vs A2 ledger)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| notes | 6 | 6 (l.206,208,210,212,214,216) | none — Step 0D table | PASS |
| line_items | 42 (35 main + 7 Format-C) | 42 | none — Step 1 tables / Step 5 | PASS |
| zero_standing | 8 | 8 | none | PASS |
| agenda_items | 6 | 6 (results approval + Format A-E) | none | PASS |
| auditor_paras | 10 (4 SA + 6 CO) | 10 (SA 1-4; CO 1-6, para-5 other-matter) | none | PASS |
| entities | 2 | 2 (Parent + I&PCL Vacuum Cast) | none | PASS |
| turns/questions/slides | N.A. | N.A. | n/a | PASS |

Fresh pass reproduces the ledger exactly; no rows found that the ledger lacks. Every substantive row is cited in A4 or covered by the 100%-reviewed preamble. QFM count grew from 7 to 8 (new row #3 on the inventory build) — additive, no coverage loss. **Coverage: PASS, no loop-back.**

---

## 2. ARITHMETIC AUDIT (recomputed from raw Lakhs)

All prior-pass recomputes still hold (revision note l.7 confirms no figure changed; verified by spot-check — Op EBITDA 11.06, Rep EBITDA 11.21, core PBT 6.95, ETR 29.75%, PAT +129.5%, ext-proc 33.17%, P&F 8.17% all reproduce). New/graft figures re-derived:

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Inventory build row (Q1FY26/Q4FY26/Q1FY27/FY26) | 1.02 / 1.69 / 2.60 / 1.13 | −(change in inv) = 1.02 / 1.69 / 2.60 / 1.13 | l.154 | PASS |
| Larger YoY inventory build | Rs 1.58 Cr | 259.92 − 102.31 = 157.61 L | l.154 | PASS |
| Inventory build as % of PBT gain | ~38% | 157.61 / 408.83 = 38.6% | l.154 / l.162,164 | PASS |
| Trigger #1 comparator Q4FY26 EBITDA | Rs 9.49 Cr | 549.94+167.09+231.78 = 948.81 L | l.162,156,157 | PASS (≈ at the Rs 9.5 bar) |
| Trigger #3 comparator Q4FY26 P&F | 9.08% | 459.67 / 5062.61 | l.158,147 | PASS |

**Rounding NOTE (unchanged from pass 1, within tolerance):** A4 continues to label the reported-PBT change "Rs 4.08 Cr" (Step 2 diag 3, Step 4 bridge, flags). Raw delta 710.48 − 301.65 = 408.83 L = 4.0883 Cr, which rounds to 4.09. A4 is 0.01 Cr (sub-lakh) low — below the rounding threshold, so PASS. Critically, the ~38% ratio is computed on the raw 408.83 L, so the graft's headline figure is unaffected.

**Arithmetic verdict: PASS.** No mismatch above rounding.

---

## 3. ADVERSARIAL READ — surviving counter now incorporated?

**Pass-1 surviving counter:** A4's "core-driven / ~100% recurring / highest-quality composition possible" claim ignored the Rs 1.58 Cr larger YoY inventory build (l.154, ~38% of the PBT gain) against INDETERMINATE Q1 cash conversion.

Verification of the three required graft points:

1. **Step 2 diagnostic 3 (l.152):** GRAFTED. Nets the build explicitly — "Rs 1.58 Cr larger YoY non-cash credit to expenses (259.92 − 102.31 = 157.61 L, l.154), equal to ~38% of the Rs 4.08 Cr reported-PBT increase," concludes the "core-driven" magnitude is "overstated until H1 FY27 CFO confirms the build converts to cash." Table verdict on the Core-PBT row (l.144) now reads "(but see inventory-build caveat, diagnostic 3)."

2. **Step 4 mandatory-answer (a) (l.196):** GRAFTED. The "~100% recurring / highest-quality" framing is explicitly **withdrawn as overstated**; states "the true recurring share sits materially below 100% and is only resolvable at the H1 FY27 cash-flow filing." Bridge table adds an "of which: larger YoY inventory-build credit (l.154) +1.58 ... Non-cash; quality unverified at Q1" sub-line.

3. **Step 6C (l.259-267):** GRAFTED. New "Bar quality" column marks trigger #1 "LOW-BAR / soft beat" (already ~met by Q4FY26 Rs 9.49 Cr; ~38% inventory-flattered) and trigger #3 "NEAR-THRESHOLD trend" (continuation of a pre-existing glide). Scorecard outcome (l.265) now warns "2 of 3 MET must NOT be read as a strong beat."

Additional propagation (beyond the three required): Step 3 trajectory table (inventory build per quarter, l.167-169), Step 5 (l.209,212,225 tie the INDETERMINATE read to the build), Step 6D margin-transition row and net-thesis read (l.273,278), Step 8/8C (l.311,315), new QFM row #3 (l.329), monitorables (l.353), and two flags (l.428-429). The counter is fully and consistently incorporated.

**No new surviving bear counter emerges from the revised text.** The revision does not introduce arithmetic or coverage regressions. The secondary soft item from pass 1 (low-bar trigger framing) is also now incorporated.

---

## VERDICT

**COMPLETE.**

The single pass-1 blocker — the unincorporated inventory-build bear counter — is fully grafted at all three required locations (Step 2 diagnostic 3, Step 4 answer (a), Step 6C) and propagated consistently through the trajectory, thesis-reconciliation, questions, monitorables, flags, and plain-language brief. Deliverable gate PASS (four brief parts present), coverage PASS (fresh enumeration reproduces the ledger; no orphans, none missing), arithmetic PASS (all metrics reproduce; only a sub-lakh 4.08-vs-4.09 rounding display, within tolerance, and the load-bearing ~38% ratio is computed on raw). No loop-back. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "IPCL"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
