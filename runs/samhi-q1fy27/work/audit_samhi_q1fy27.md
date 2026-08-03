# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT
# SAMHI Hotels Limited (SAMHI) — Q1 FY27 (quarter ended 30 June 2026)
# Auditor: A5 (fresh context: A4 review + A1 extracts + A2 ledgers only). All figures re-derived.

---

## 0. SCOPE OF RE-DERIVATION
I re-ran the A2 enumeration with my own pass over all three extracts, recomputed every derived metric in A4's tables from the raw OCR line items, re-tested the four items the task flagged, and constructed bear counters to A4's three most positive claims. I did not defer to A4's or A3's cites; line numbers below are my own reads of the extracts.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration vs A2 ledger (diff)

| Category | A2 count | My fresh count | Source | Orphan / missing | Status |
|---|---|---|---|---|---|
| Results — notes | 18 (10 SA + 8 CO) | 18 (SA L514,518,520,522,524,534,536,538,541,544 = 10; CO L803,808,811,813,815,826,829,835 = 8) | results | none | PASS |
| Results — line items | 102 (40 SA + 52 CO + 10 exc) | 102 | results | none | PASS |
| Results — agenda items | 5 | 5 (L52,60,68,102,106) | results | none | PASS |
| Results — auditor paras | 13 (6 SA + 7 CO) | 13 | results | none | PASS |
| Results — consolidation entities | 18 | 18 (Annexure 1, L678-700) | results | none | PASS |
| Results — zero-standing | 12 | 12 | results | none | PASS |
| Results — annexure rows | 18 (8 + 10) | 18 | results | none | PASS |
| Results — signature blocks | 9 | 9 | results | none | PASS |
| Presentation — slides | 52 | 52 | presentation | none | PASS |
| Presentation — footnotes | 56 | 56 | presentation | none | PASS |
| Presentation — KPI slides | 39 | 39 (reconciled set) | presentation | none | PASS |
| Presentation — FLS | 13 | 13 | presentation | none | PASS |
| Presentation — discrepancy flags | 7 (ND-01..04, ENUM-05/06, CLASS-07) | 7 | presentation | see 1C | PASS |
| Press — pages | 4 | 4 | pressrelease | none | PASS |
| Press — numbered footnotes | 10 | 10 | pressrelease | none | PASS |
| Press — table line items | 16 (10 + 6) | 16 | pressrelease | none | PASS |
| Press — mgmt quote units | 7 | 7 | pressrelease | none | PASS |
| Press — mgmt numbers | 11 | 11 | pressrelease | none | PASS |

**No row my fresh pass found is absent from the A2 ledgers (nothing to loop back to A2).** The two A2 count adjustments (notes 20→18 on OCR false positives; auditor paras 17→13 on letterhead/`(cont'd)` artifacts) reproduce exactly on my read.

### 1B. Every material ledger row carried into A4? (orphan test — loop to A3 if any absent)
Traced each flagged ledger row to an A4 destination (QFM row / flag / step-narrative / monitorable):

- STANDALONE_CONSOL_PAT_GAP → A4 Step 1A correction + QFM Q4 + sc_gap YAML. Carried (and corrected).
- EXCEPTIONAL_ITEMS_COMPOSITION_DIFFERS → notes S-5/C-5 + QFM Q4. Carried.
- CAPITAL_STRUCTURE_CHANGE / FUNDRAISE → Step 0C + QFM Q5 + monitorables. Carried.
- M&A_APPROVAL (Itmenaan) → QFM Q8 + monitorables. Carried.
- ENTITY_UNAUDITED x2 → Step 0D + QFM Q7. Carried.
- Deck ND-01/ND-02 (slide-12 figure/rate mispairing) → QFM Q12 (P-10). Carried.
- ND-03a (segment sum 12,499 vs 12,790, Rs 291 mn gap) → QFM Q11 (P-09). Carried.
- 3.0x vs 3.2x (press A3-03 / mgmt-number #11) → QFM Q13 + Role-5 cross-ref table. Carried.
- RevPAR moving same-store base (slide-21 fns) → QFM Q14 (P-13). Carried.
- GST-ITC structural (slide-49 L1789) → QFM Q3 + diagnostic 2. Carried.

**Non-material rows not individually surfaced (noted, not FAIL):**
- **SAMHI Skyline Pvt Ltd (entity #17, "from 16 January 2026")** — ledger NEW_ENTITY flag. A4 reviews RARE India (#18) in depth but does not name SAMHI Skyline. The ledger itself records PRIOR_LEDGER_NOT_AVAILABLE, so it cannot be confirmed as a this-period addition; A4's blanket "18 entities reviewed" covers it and it is immaterial. Not an orphan FAIL, but logged.
- **ND-03b (Rs 3 mn segment/asset-income gap)** and **ND-04 (FY26 EBITDA 4,721 pre-ESOP/TTM vs 4,626 reported)** — A4 keeps the two EBITDA bases correctly distinct (1C uses 4,628 reported; Step 5 uses 4,721 TTM ex-ESOP ex-Caspia), so no conflation error; the Rs 3 mn gap is rounding. Neither seeded a QFM row; immaterial, not a FAIL.

### 1C. Task item 3 — does every AMBIGUOUS / FORWARD-SIGNAL item have a QFM row?
Every materially identifiable AMBIGUOUS/FORWARD-SIGNAL item maps to a QFM row (16 rows):
DTA/ETR→Q1; NCI→Q2; GST→Q3; standalone PAT & exceptional→Q4; Rs750cr→Q5; RARE revenue→Q6; unreviewed entities→Q7; Itmenaan→Q8; Hyatt Pune apartments→Q9; Westin opening-year conflict→Q10; segment gap→Q11; slide-12 mispairing→Q12; 3.0x/3.2x→Q13; RevPAR base→Q14; intl-travel/pipeline firmness→Q15; Annual-Report timing→Q16.
Finding tags incorporated but not appearing in a QFM `from_finding` cell (P-04, P-11, P-14, P-15, A3-04, F14) are either A4-classified NEUTRAL-FACT (F14, the mis-dated notes heading, explicitly) or their substance is already discharged inside the 16 rows and the Monitorables list (P-04's forward catalysts → Q3/Q6/Q8/Q10 + monitorables). Pure forward guidance (margin 36→40%, upscale 41→60% by FY30) is correctly routed to Monitorables, which is the protocol channel for FLS. **Task item 3: PASS** — no FORWARD-SIGNAL/AMBIGUOUS item is left without a management question.

**COVERAGE VERDICT: PASS. No orphan rows requiring A3, no missing rows requiring A2.**

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines)

Consolidated column mapping confirmed from source header (extract L715): 30-Jun-26 = Q1FY27, 31-Mar-26 = Q4FY26, 30-Jun-25 = Q1FY26, 31-Mar-26 = FY26.

### 2A. Metrics that RECONCILE (within rounding) — spot list

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Operating EBITDA ex-OI Q1FY27 | 982.31 | 1,013.08 − 30.77 = 982.31 | L729,L721 | OK |
| Op EBITDA margin Q1FY27 | 32.19% | 982.31/3,052.06 = 32.19% | L720 | OK |
| Reported EBITDA margin Q1FY27 | 32.9% | 1,013.08/3,082.83 = 32.86% | L729,L722 | OK |
| Core op PBT ex-OI Q1FY27 | 296.56 | 327.33 − 30.77 = 296.56 | L735(slide15),L721 | OK |
| Revenue YoY | +12.1% | 3,052.06/2,722.11 − 1 = +12.12% | L720 | OK |
| Op EBITDA YoY | +8.5% | 982.31/905.01 − 1 = +8.54% | derived | OK |
| Reported EBITDA YoY | −4.1% | 1,013.08/1,055.87 − 1 = −4.05% | L729 | OK |
| Finance cost YoY | −25.5% | 376.89/506.16 − 1 = −25.54% | L731 | OK |
| Other income YoY | −79.6% | 30.77/150.86 − 1 = −79.61% | L721 | OK |
| Core op PBT YoY | +174.1% | 296.56/108.19 − 1 = +174.1% | derived | OK |
| PAT total YoY | +29.7% | 249.27/192.16 − 1 = +29.72% | L749/L760 | OK |
| NCI YoY | +244.9% | 66.77/19.36 − 1 = +244.9% | L759 | OK |
| Minority share of PAT increment | 83% | 47.41/57.11 = 83.0% | L759,L760 | OK |
| PAT bridge (all components) | sums to +57.11 | +77.30−120.09−18.17+129.27+28.22−39.39 = +57.14 (ties to +57.11) | L720-759 | OK |
| Effective tax rate Q1FY27 | 23.9% | 78.06/327.33 = 23.85% | L740,L735 | OK |
| PAT margin owners Q1FY27 | 5.98% | 182.50/3,052.06 = 5.98% | L758,L720 | OK |

### 2B. Task item 2 — standalone vs consolidated PAT, every period, and the Q4FY26 column mis-read
Standalone P&L column order (extract L439): 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | 31-Mar-26 = Q1FY27 | Q4FY26 | Q1FY26 | FY26.
Line L467/L473 read `[garbled] | 2,467.85 | 487.10/458.88 | 3,897.88/3,843.37`. **The 2,467.85 sits in the SECOND (31-Mar-26 = Q4FY26) column, not the first (Q1FY27) column.** Standalone Q1FY27 basic EPS = 0.05 (L487, corroborated L499) → PAT ≈ 0.05 × 222.13 = **11.1 mn**, corroborated by standalone TCI 12.43 mn (L481). **A4's correction of A2's "Rs 247 cr standalone Q1FY27" as a Q4FY26 column mis-read is CONFIRMED independently.**

| Period | Standalone PAT (L473) | Consol PAT (L760) | Consol owners (L758) | SA/Consol | A4 sc_gap | Status |
|---|---|---|---|---|---|---|
| Q1FY27 | ~11.1 (EPS-implied) | 249.27 | 182.50 | 4.4% | 1.1 / 24.93 / 18.25, 4.4% | OK |
| Q1FY26 | 458.88 | 192.16 | 172.80 | 238.8% | 45.89 / 19.22 / 17.28, 238.8% | OK |
| Q4FY26 | 2,467.85 | 3,993.96 | 3,536.71 | 61.8% | 246.79 / 399.40 / 353.67, 61.8% | OK |
| FY26 | 3,843.37 | 5,665.45 | 5,029.90 | 67.8% | 384.34 / 566.55 / 502.99, 67.8% | OK |

All four periods reconcile to A4's YAML `sc_gap_pat_pct`. **Task item 2: PASS.**

### 2C. Task item 4 — FY26 DTA-credit normalisation
Reported FY26 consol PAT = 5,665.45 (L760). FY26 PBT continuing 2,725.09 (L737, OCR) − discontinued 54.51 = reported PBT **2,670.58 (≈ A4's 2,671)**. Total tax = **credit 2,994.87** (deferred credit 2,995.45 L740 less current 0.58 L739). Check: 2,670.58 + 2,994.87 = **5,665.45 = reported PAT.** Confirmed: FY26 PAT exceeds PBT by the ~Rs 2,994 mn tax credit; "~Rs 3,000 mn DTA credit" is accurate.
Normalised proxy: PBT-before-exceptional 1,649.83 (L735) × 0.75 = **1,237.4 ≈ A4's ~1,238 mn.** Confirmed.
**BUT the distortion MULTIPLE A4 quotes is wrong:** 5,665.45 / 1,237.4 = **4.58x ≈ 4.6x**, not the "~4.9x" A4 states at L262 and L332. A4's own stated normalised (1,238 at 25%) yields 4.6x; the 4.9x reconciles only with a ~30%-tax normalised (~1,155), which A4 does not use. Internal inconsistency. **FAIL — see 2D item (ii).**

### 2D. ARITHMETIC MISMATCHES (above rounding)

| # | Metric | A4 value | Recomputed | Source line | Note |
|---|---|---|---|---|---|
| (i) | Owners'/SAMHI-attributable PAT YoY | **+5.8%** (Step 2 L163, bridge L216, flag L506, YAML) | (182.50−172.80)/172.80 = **+5.6%** | extract L758 | A4 used deck-rounded 183/173 (=+5.78%). A4's own bridge states the increment as +9.70 mn, which on the 172.80 base is +5.6%, so A4 is internally inconsistent; by A4's own "filing wins over deck" house rule the correct figure is +5.6%. |
| (ii) | Reported FY26 PAT ÷ normalised PAT | **~4.9x** (L262, L332) | 5,665.45 / 1,237.4 = **~4.6x** | extract L760, L735 | Inconsistent with A4's own stated normalised of ~1,238 mn (25% tax). |
| (iii) | Effective tax rate Q1FY26 (minor) | **16.9%** (39/231, 1C L141) | 38.67/230.83 = **16.7%** | extract L740; PBT 259.05−28.22 | A4 rounded the tax numerator to 39 before dividing; precise inputs give 16.7%. Borderline, but above one-decimal rounding. |

None of the three changes the direction, the flag set, or the verdict logic — (i) marginally understates the owners'-PAT lag, (ii) marginally overstates the DTA distortion — but all three are above rounding and appear in A4's tables/flags/YAML, so per the arithmetic-audit rule each is a FAIL routed to **A4** for correction before save.

---

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counter from the same extract

**Claim 1 (L150/diag 1): "Revenue from operations +12.1% YoY — GENUINE operating growth (occupancy 74.2%→79.3%, RevPAR +9.6%)."**
Bear counter (same extract): RevPAR +9.6% is on a MOVING same-store base — slide-21 footnotes (ledger L469-473; extract slide 21) show the exclusion set itself changes across the 13-quarter window (ACIC/Trinity/HIEX Gr.Noida/HIEX Kolkata/Caspia Delhi/Sheraton phased in and out), so the series is not constant-composition; occupancy 79.3% is likewise same-store; and total income grew only +7.3%. "GENUINE like-for-like" is therefore softer than stated.
**Survives?** Substantially ALREADY in A4 — logged as QFM Q14 (P-13) and the total-income-vs-operations split in diagnostic 1. No new graft required; recommend only that the word "GENUINE" in Step 2 carry the same-store-base caveat inline. Not a blocking add.

**Claim 2 (L159): "Core operating PBT ex-OI +174.1% — cleanest signal, genuine core improvement."**
Bear counter (same extract): the +174% is finance-cost-led (−25.5%, +Rs 129 mn), NOT operating leverage — operating EBITDA alone was only +8.5%; and A4 itself notes finance cost and D&A "re-ramp" as the 1,669-room pipeline commissions and the Rs 750 cr raise deploys (L221). So +174% is not a sustainable run-rate.
**Survives?** ALREADY fully incorporated by A4 (diagnostic 3 L173, bridge, Step 4). No graft required.

**Claim 3 (L157 / Section C): "Deleveraged to 3.2x with A+ rating; finance costs −25.5% major tailwind."**
Bear counter (same extract): net debt ROSE +Rs 42 cr QoQ (14,507→14,928, deck slide 16 / press L144), leverage ticked UP 3.1x→3.2x, TTM EBITDA FELL 4,721→4,664, and the Rs 750 cr enabling resolution + authorized-capital increase pre-position the balance sheet for a heavier capex/M&A cycle (more leverage/dilution ahead). CEO quote frames 3.0x while tables say 3.2x.
**Survives?** ALREADY incorporated (Step 5 net-debt row, QFM Q13, flags). No graft required.

**Adversarial-read result:** A4's review is symmetric; all three bear counters are already present. **No surviving un-incorporated counter → no additional A4 graft on this axis.**

---

## 4. TASK ITEM 1 — verdict vs cash-conversion cap (contradiction check)
Framework rule (CLAUDE.md): INDETERMINATE cash conversion caps the ceiling at PROCEED WITH CAVEATS with missing evidence named. Verdict set ordering, most-positive to least: PROCEED > PROCEED WITH CAVEATS > PROCEED WITH FLAGS > REWORK > INSUFFICIENT EVIDENCE. The "cap" forbids a verdict MORE positive than PROCEED WITH CAVEATS (i.e., forbids a clean PROCEED). A4's verdict **PROCEED WITH FLAGS is LESS positive than the ceiling, so it sits below the cap and does not violate it**, and A4 names the missing evidence (H1 FY27 cash-flow statement, due Q2). The two statements are **reconciled, not contradictory** (A4 L399 and YAML L460 record the cap explicitly). **Task item 1: PASS.** (Advisory only: the verdict label "PROCEED WITH FLAGS" carries the CAVEATS cap in prose/YAML rather than in the label; this is consistent with the ordered verdict set and the rule's intent, so no change required.)

---

## 5. VERDICT

**INCOMPLETE.** Coverage is complete (no orphan rows, no A2 miss; task items 1, 2, 3 pass and the Q4FY26 column mis-read correction is independently confirmed). However, the ARITHMETIC audit found three internal-consistency mismatches above rounding in A4's tables/flags/YAML (Section 2D): (i) owners' PAT YoY stated +5.8% vs recomputed +5.6%; (ii) FY26 DTA distortion multiple stated ~4.9x vs recomputed ~4.6x (inconsistent with A4's own normalised ~Rs 1,238 mn); (iii) Q1FY26 ETR stated 16.9% vs recomputed 16.7%.

**Loop back to: A4.** Correct the three figures (and their downstream repeats: owners'-PAT +5.6% at L163/L216/flag L506/YAML; DTA multiple ~4.6x at L262/L332; ETR 16.7% at L141) and re-emit. None affects the flag set, the NO-POSITION/8A-W decision, or the PROCEED WITH FLAGS verdict — these are precision corrections, so re-review can be narrow.

---

```yaml
stage: A5-adversary
company: "SAMHI"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Owners'/SAMHI-attributable PAT YoY", a4_value: "+5.8%", recomputed: "+5.6%", source_line: "extract_results L758 (182.50 vs 172.80); A4 review L163/L216/L506"}
  - {metric: "Reported FY26 PAT / normalised PAT multiple", a4_value: "~4.9x", recomputed: "~4.6x (5,665.45 / 1,237.4)", source_line: "extract_results L760, L735; A4 review L262/L332"}
  - {metric: "Effective tax rate Q1FY26", a4_value: "16.9% (39/231)", recomputed: "16.7% (38.67/230.83)", source_line: "extract_results L740; A4 review L141"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Three arithmetic internal-consistency errors above rounding in A4's tables/flags/YAML: (1) owners' PAT YoY +5.8% should be +5.6% (deck-rounded 183/173 used instead of filing 182.50/172.80; contradicts A4's own +9.70mn increment on 172.80 base); (2) FY26 DTA distortion multiple ~4.9x should be ~4.6x, inconsistent with A4's own stated normalised ~Rs 1,238mn at 25% tax; (3) Q1FY26 ETR 16.9% should be ~16.7% on precise inputs. Correct all downstream repeats and re-emit. Coverage, Q4FY26 column-mis-read correction, cash-conversion-cap reconciliation, and QFM completeness all PASS."
```
