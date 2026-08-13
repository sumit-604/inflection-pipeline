# A5 ADVERSARY / COMPLETENESS AUDIT — IPCL Q1 FY27 (results only)

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Doctype:** results (Role 5 N.A.)
**Under audit:** `review_ipcl_q1fy27.md` (A4) | **Re-derived from:** `extract_results_ipcl_q1fy27.txt` (A1), `ledger_results_ipcl_q1fy27.md` (A2)
Independence: I did not read A3; every count and metric below is re-run from the raw extract/ledger. Units: source Lakhs; Cr = Lakhs x 0.01.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

| Brief part | Location in A4 | Present / Empty | Real content? |
|---|---|---|---|
| (1) Summary narrative | l.362-364 | PRESENT | Yes — dense single block, revenue/core-PBT/trigger/debt all anchored |
| (2) SECTOR intelligence | l.366-369 | PRESENT | Yes — certifications, demand cycle, input-cost, outsourcing headwind |
| (3) BUSINESS-MODEL intelligence | l.371-374 | PRESENT | Yes — cost-stack %, external-processing drift, debt model, subsidiary shell |
| (4) COMPETITION intelligence | l.376-379 | PRESENT | Yes — moat wall, small-cap disadvantage, A&D opacity, no-peer-data gap named |

**Gate result: PASS.** All four labelled parts present and non-empty.

---

## 1. COVERAGE AUDIT (fresh grep/sweep vs A2 ledger)

| Category | A2 count | My fresh count | Orphan rows (ledger → absent from A4) | Status |
|---|---|---|---|---|
| notes | 6 | 6 (l.206,208,210,212,214,216) | none — all 6 in Step 0D table | PASS |
| line_items | 42 (35 main + 7 Format-C) | 42 (main table l.146-184 = 35 after 4 wrap + header strip; Format-C l.99-108 = 7) | none — all in Step 1 tables / Step 5 | PASS |
| zero_standing | 8 | 8 (3 main: l.153,163,167; 5 Format-C: l.103,104,105,106,107) | none — Format-C dash + exceptional/EYT cited | PASS |
| agenda_items | 6 | 6 (results approval l.41-44 + Format A-E l.90-116) | none — board outcome + Format C/D cited; B/E N.A. reviewed | PASS |
| auditor_paras | 10 (4 SA + 6 CO) | 10 (SA para 1-4 l.238-266; CO para 1-6 l.300-350) | none — both reports + para-5 other-matter cited | PASS |
| entities | 2 | 2 (Parent l.300; I&PCL Vacuum Cast l.301/332) | none — both cited | PASS |
| turns/questions/slides | N.A. | N.A. (results doctype, 0 concall/0 slides) | n/a | PASS |

**Rows my fresh pass found that the ledger lacks:** NONE. My enumeration reproduces the ledger exactly (including the reconciled agenda 5-vs-6 line-wrap and the auditor-para DN-string false positives).

**Orphan rows (in ledger, absent from A4):** NONE material. A4's preamble (l.20) blanket-marks 100% reviewed; every substantive ledger row (notes, line items, Format-C, auditor paras, both entities) is individually cited. Minor A2 QA flags (TIMESTAMP_NOT_AVAILABLE x2, SIGNATORY_NOT_LEGIBLE x2) are not surfaced individually by A4 but fall under "reviewed, no finding" and are non-substantive. **Coverage: PASS, no loop-back.**

---

## 2. ARITHMETIC AUDIT (recomputed from raw Lakhs)

All A4 derived values reproduced independently. Representative recomputes (standalone unless noted):

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Revenue YoY | +21.2% | 5333.58/4401.96 = +21.16% | l.147 | PASS |
| Op EBITDA Q1FY27 | 11.06 | 710.48+238.64+171.82−15.26 = 1105.68 L | l.162,157,156,149 | PASS |
| Op EBITDA margin Q1FY27 | 20.73% | 1105.68/5333.58 | l.147 | PASS |
| Op EBITDA margin YoY | +619 bps | 20.73 − 14.54 | l.147 | PASS |
| Reported EBITDA Q1FY27 (trigger #1) | 11.21 | 710.48+171.82+238.64 = 1120.94 L | l.162,156,157 | PASS (≥9.5 MET) |
| Reported EBITDA margin Q1FY27 | 21.02% | 1120.94/5333.58 | l.147 | PASS |
| Core PBT ex-OI Q1FY27 | 6.95 | 710.48−15.26 = 695.22 L | l.164,149 | PASS |
| Core PBT ex-OI YoY | +148.9% | 695.22/279.35 = +148.87% | l.164,149 | PASS |
| Effective Tax Rate Q1FY27 | 29.75% | 211.36/710.48 | l.169,164 | PASS |
| PAT margin Q1FY27 | 9.36% | 499.12/5333.58 | l.170,147 | PASS |
| PAT YoY | +129.5% | 499.12/217.51 = +129.47% | l.170 | PASS |
| Ext-processing / total exp Q1FY27 | 33.17% | 1539.65/4641.98 | l.159,161 | PASS (RED) |
| P&F / rev Q1FY27 (trigger #3) | 8.17% | 435.80/5333.58 | l.158,147 | PASS (<9.5 MET) |
| P&F / rev FY26 | 9.20% | 1706.49/18539.50 = 9.205% | l.158,147 | PASS |
| S-vs-C PAT gap Q4FY26 | +0.122% (sign flip) | (376.97−376.51)/376.51 | l.170 | PASS |
| S-vs-C PAT gap Q1FY27 | −0.046% | (498.89−499.12)/499.12 | l.170 | PASS |
| EBIT(op) YoY | +97.8% | 867.04/438.43 = +97.76% | l.162,157 | PASS |

**Two rounding-direction NOTES (within tolerance, not FAIL):** In the Step-4 PAT bridge, A4 shows Reported PBT change **+4.08** and PAT change **+2.81**. Raw deltas are PBT 710.48−301.65 = 408.83 L = **4.0883 Cr (rounds 4.09)** and PAT 499.12−217.51 = 281.61 L = **2.8161 Cr (rounds 2.82)**. A4 is 0.01 Cr (1 lakh) low on each — a sub-lakh rounding-boundary display, below the rounding threshold, so PASS. Flagged for tidiness only; the headline percentages (+135.5% / +129.5%) are computed from raw and correct.

**Arithmetic verdict: PASS.** No mismatch above rounding.

---

## 3. ADVERSARIAL READ — three most positive A4 claims, strongest bear counter from the same extract

**Positive claim A (Step 2 diag 3 / Step 4a, l.150,193):** "core operating PBT +148.9% ... headline PAT growth is UNDERPINNED by core operations ... ~100% of the YoY PAT increase is recurring/core ... the highest-quality composition possible."
**Strongest bear counter (from l.154 + Step 5):** Changes in inventories (l.154, standalone) was **(259.92) L in Q1FY27 vs (102.31) L in Q1FY26** — a **Rs 1.58 Cr larger inventory build** credited against Total Expenses. That single non-cash swing is **~38% of the entire Rs 4.09 Cr reported-PBT increase**. Because this is a Q1 filing with **no cash-flow statement (CFO/PAT INDETERMINATE, Step 5, l.206)**, the claim that the uplift is "~100% recurring / highest quality possible" is **unverifiable and arguably overstated**: profit on goods produced-not-sold cannot be confirmed as cash-backed this quarter. A4 mentions the line only to dismiss it ("a P&L line, not a WC bridge," l.209) and never nets it against the quality claim.
**Verdict: SURVIVES.** Must be grafted into A4 (Step 2 diag 3 and Step 4a) before save. → **loop A4.**

**Positive claim B (Step 6C, l.262):** "2 of 3 pre-committed binding thresholds MET" (EBITDA ≥Rs 9.5 Cr; P&F <9.5% of revenue).
**Strongest bear counter (from l.158,162 trajectory):** Both cleared bars were **already near-met on the printed trajectory** — Q4 FY26 EBITDA was Rs 9.49 Cr (l.162 build) i.e. essentially at the Rs 9.5 Cr bar a quarter earlier, and P&F was 9.62% (Q1 FY26) / 9.08% (Q4 FY26), i.e. the <9.5% bar was one soft quarter away. Meanwhile the **one trigger that actually tests the growth thesis — A&D order book ≥Rs 100 Cr (#2) — was made structurally un-testable by Note 2's segment collapse in the SAME filing (l.208).** So "2 of 3 MET" reads stronger than the substance: two low-bar/mechanical passes plus the decisive one going dark.
**Verdict: PARTIALLY incorporated.** A4 does flag #2 un-testable and that valuation/governance are unrepaired (l.264, l.308), but does **not** characterise #1/#3 as low-bar/near-met. Recommend a one-line graft; not a standalone hard fail.

**Positive claim C (Step 6B / Step 6D, l.250,270):** "P&F intensity 8.17% GREEN, improved from 9.62%" and "Margin transition ON TRACK / STRENGTHENING."
**Strongest bear counter (from Step 3, l.161-168):** Only **three data points** exist (Q1FY26, a balancing-figure Q4FY26, Q1FY27; PRIOR_LEDGER_NOT_PROVIDED); P&F intensity and margin can swing on fuel price and product mix, and there is no 4-6 quarter sequence to establish durability.
**Verdict: does NOT survive.** A4 already caps this — explicitly labels Q4 a soft balancing-figure base (l.170), defers durability to Q2 (l.172), and sets a Q2 confirm threshold. Adequately hedged.

---

## VERDICT

**INCOMPLETE.**
- **loop_back_to: A4**
- **gap:** One surviving bear counter is not incorporated. A4's "core-driven / ~100% recurring / highest-quality composition possible" quality claim (l.150, l.193) ignores that the YoY inventory build widened to Rs 2.60 Cr from Rs 1.02 Cr (l.154) — a Rs 1.58 Cr non-cash tailwind = ~38% of the Rs 4.09 Cr PBT gain — while cash conversion is INDETERMINATE (no Q1 cash-flow statement, Step 5). A4 must graft this counter into Step 2 (diagnostic 3) and Step 4 (bridge / mandatory answer a), qualifying the quality claim, before save. Secondary (soft): add a one-line "low-bar / near-met" note to the Step 6C trigger scorecard for triggers #1 and #3.

Coverage PASS, arithmetic PASS, deliverable gate PASS — the only blocker is the unincorporated surviving bear counter above.

```yaml
stage: A5-adversary
company: "IPCL"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Core operating PBT +148.9%; ~100% of YoY PAT increase is recurring/core, 'highest-quality composition possible' (Step 2 diag 3 / Step 4a)"
    counter: "Changes in inventories widened to Rs 2.60 Cr build from Rs 1.02 Cr YoY, a Rs 1.58 Cr non-cash credit to expenses = ~38% of the Rs 4.09 Cr reported-PBT increase; with CFO/PAT INDETERMINATE at Q1 (no cash-flow statement) the quality claim is unverifiable and overstated. A4 only dismisses l.154 as a P&L line, never nets it against the quality claim."
    source_line: "l.154 (Q1FY27 (259.92) vs Q1FY26 (102.31)); Step 5 l.206 INDETERMINATE"
loop_back_to: "A4"
gap: "A4 must graft the inventory-build bear counter (l.154: Rs 1.58 Cr larger YoY inventory build = ~38% of the PBT gain, against INDETERMINATE Q1 cash conversion) into Step 2 diagnostic 3 and Step 4 mandatory-answer (a), qualifying the 'highest-quality / ~100% recurring' claim, before Notion save. Secondary soft add: mark triggers #1/#3 as low-bar/near-met in Step 6C."
```
