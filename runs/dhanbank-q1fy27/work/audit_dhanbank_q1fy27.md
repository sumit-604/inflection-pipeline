# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT — DHANBANK (Dhanlaxmi Bank Ltd) Q1 FY27

Agent: A5 ADVERSARY. Fresh context: I see only the A4 review, the A1 extract, and the A2 ledger. All checks re-derived from the A1 extract; I do not defer to A4's or A3's cites. Unit basis: source prints Rs Lakh; divide by 100 for Rs Crore. Extract line numbers cited as L###.

VERDICT: **INCOMPLETE** — loop back to **A3** (missed forward-signal forensic on enumerated ratio rows 17(vii) L281 and 17(viii) L282), with **A4** to graft the surviving bear counter before save. Detail in the ADVERSARIAL section and verdict block. All three audits completed in full below.

---

## 1. COVERAGE AUDIT (fresh grep + sweep, diffed against A2 ledger)

| Category | A2 count | My fresh count | Orphan rows (enumerated, absent from A4) | Status |
|---|---|---|---|---|
| Numbered notes | 14 | 14 | none — Notes 1-14 all in A4 Step 0D table | PASS |
| P&L line items | 22 (of 87) | 22 | none material — all P&L rows carried into Step 1L | PASS |
| Balance-sheet line items | 13 (of 87) | 13 | none — Capital, Reserves, Deposits, Borrowings, Advances, Investments etc. all used | PASS |
| Segment rows | 36 (of 87) | 36 | Corp/Wholesale cited (FN5); Treasury/Retail/Other feed NII/PPOP, no independent finding | PASS (soft) |
| Note 11 project rows | 16 (of 87) | 16 | none — closing pool 110.41 Cr and nil resolution-failure rows cited | PASS |
| Zero-standing rows | 24 | 24 | none — Exceptional/Extraordinary nil, GoI Nil, Note 11 nils all surfaced | PASS |
| **Analytical ratios** | **14** | **14** | **17(vii) Debt-Equity L281; 17(viii) Total-Debts-to-Assets L282; 17(ix) Operating Margin L283; 17(x) Net Profit Margin L284** | **FAIL** |
| Segments (reportable) | 4 | 4 | none | PASS |
| Comparative periods | 4 | 4 | none — Q1FY27/Q4FY26/Q1FY26/FY26 all used | PASS |
| Agenda items | 1 | 1 | none | PASS |
| Auditor paras | 5 | 5 | none — paras 1-5 cited (L156-219) | PASS |
| Entities | 3 | 3 | none — Bank + 2 audit firms | PASS |
| Signatures | 4 | 4 | none | PASS |
| Footnotes | 3 | 3 | ** (L223) and *** (L224) uncited — tied to the two uncited ratios below | FAIL (same root) |

**Fresh-pass rows the ledger lacks:** none. A2 enumeration reproduces exactly (14/87/24/14/4/4/1/5/3/4/3). No loop-back to A2.

**Orphan-row finding (loop to A3/A4).** Four disclosed Analytical Ratios are enumerated in ledger Table 3 but appear nowhere in A4's review, and A4 gives no "reviewed, no finding" disposition for them (verified by grep: no hit for "Debt Equity", "Total Debts", "Operating Margin", "Net Profit Margin", "3.88", "0.11" in the review body):
- 17(ix) Operating Margin (10.62% Q1FY27, L283) and 17(x) Net Profit Margin (5.14%, L284) are immaterial orphans — they are pure re-expressions of PPOP/Total Income and PAT/Total Income, both of which A4 analyses; I reconcile them (5,145/48,425 = 10.62%; 2,491/48,425 = 5.14%) and treat them as covered-by-derivation, not a substantive gap.
- 17(vii) Debt-Equity 0.11x (L281) and 17(viii) Total-Debts-to-Assets 3.88% (L282) are a **substantive** orphan: together they resolve the tenor of the FN12 borrowings surge, which A4 explicitly treats as undisclosed. This is the load-bearing coverage failure and is developed in the ADVERSARIAL section (surviving bear counter).

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines, Lakh /100 = Cr)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Unit conversion (Lakh /100) | Cr throughout | 44,936 lakh = 449.36 Cr; 15,57,166 = 15,571.66 Cr | L241, L364 | CONFIRMED |
| NII Q1FY27 | 177.62 | (44,936 − 27,174)/100 = 177.62 | L241, L249 | CONFIRMED |
| NII Q4FY26 | 187.05 | (44,305 − 25,600)/100 = 187.05 | L241, L249 | CONFIRMED |
| NII Q1FY26 | 139.10 | (36,776 − 22,866)/100 = 139.10 | L241, L249 | CONFIRMED |
| NII FY26 | 622.33 | (1,60,148 − 97,915)/100 = 622.33 | L241, L249 | CONFIRMED |
| **Cost-to-income Q1FY27 (LOAD-BEARING)** | **75.79%** | 16,106 / (17,762 + 3,489) = 16,106/21,251 = **75.789%** | L250, L241, L249, L247 | **CONFIRMED** |
| Cost-to-income Q4FY26 | 55.66% | 14,267 / (18,705 + 6,929) = 14,267/25,634 = 55.655% | L250,241,249,247 | CONFIRMED |
| Cost-to-income Q1FY26 | 81.35% | 14,512 / (13,910 + 3,930) = 14,512/17,840 = 81.345% | L250,241,249,247 | CONFIRMED |
| **PCR ex tech w/o Q1FY27 (LOAD-BEARING)** | **74.66%** | 1 − 7,261/28,657 = 1 − 0.25337 = **74.663%** | L275, L276 | **CONFIRMED** |
| PCR ex tech w/o Q4FY26 | 73.67% | 1 − 7,540/28,638 = 73.672% | L275, L276 | CONFIRMED |
| PCR ex tech w/o Q1FY26 | 65.51% | 1 − 13,862/40,195 = 65.513% | L275, L276 | CONFIRMED |
| **RoA annualised Q1FY27 (LOAD-BEARING)** | **0.45%** (as disclosed) | annPAT 99.64 / avg assets (22,126.24+21,237.66)/2 = 99.64/21,681.95 = **0.460%** | L279 disc.; L262, L359/367 | CONFIRMED (disclosed 0.45%; my ×4/2-pt proxy 0.46%, within method/rounding — daily-average denominator explains the 0.01pp; not a mismatch) |
| Advances YoY | +27.4% | (15,57,166 − 12,21,820)/12,21,820 = 27.446% | L364 | CONFIRMED |
| Deposits YoY | +17.1% | (19,40,405 − 16,56,962)/16,56,962 = 17.108% | L356 | CONFIRMED |
| Borrowings YoY | +104% | (85,871 − 41,996)/41,996 = 104.47% | L357 | CONFIRMED |
| Borrowings QoQ | +16.6% | (85,871 − 73,663)/73,663 = 16.57% | L357 | CONFIRMED |
| EPS Q1FY27 (Basic) | 0.63 | 2,491 lakh PAT / 3,947 lakh shares = Rs 0.631 (not annualised) | L262, L265 | CONFIRMED |
| PAT YoY | +104.5% | (2,491 − 1,218)/1,218 = 104.52% | L262 | CONFIRMED |
| PBT YoY | +191.8% | (3,554 − 1,218)/1,218 = 191.79% | L260 | CONFIRMED |
| ETR Q1FY27 | 29.9% | 1,063/3,554 = 29.91% | L261, L260 | CONFIRMED |
| ETR Q4FY26 | 44.9% | 3,547/7,896 = 44.92% | L261, L260 | CONFIRMED |
| PPOP YoY | +54.6% | (51.45 − 33.28)/33.28 = 54.60% | L255-256 | CONFIRMED |
| PPOP QoQ | −54.7% | (51.45 − 113.67)/113.67 = −54.74% | L255-256 | CONFIRMED |
| Other income YoY | −11.2% | (34.89 − 39.30)/39.30 = −11.22% | L247 | CONFIRMED |
| Other income QoQ | −49.6% | (34.89 − 69.29)/69.29 = −49.65% | L247 | CONFIRMED |
| Employee cost QoQ | +30.9% | (9,298 − 7,104)/7,104 = 30.88% | L251 | CONFIRMED |
| Provisions YoY | −24.6% | (1,591 − 2,110)/2,110 = −24.60% | L257 | CONFIRMED |
| Credit-cost proxy Q1FY27 | 0.42% | 1,591×4 / ((15,57,166+14,91,806)/2) = 6,364/15,24,486 = 0.417% | L257, L364 | CONFIRMED |
| RoE proxy Q1FY27 | 7.74% | 2,491×4 / ((1,30,887+1,26,455)/2) = 9,964/1,28,671 = 7.74% | L262, L280 | CONFIRMED |
| Net worth Q1FY27 | 1,308.87 | 1,30,887/100 | L280 | CONFIRMED |
| Book equity Q1FY27 | 1,513.21 | (39,470 + 1,11,851)/100 = 1,513.21 (ties to Capital Employed total L334) | L354, L355 | CONFIRMED |
| Net-worth vs book-equity gap | 204.34 Cr / 13.5% | 1,513.21 − 1,308.87 = 204.34; /1,513.21 = 13.5% | L280, L354-355 | CONFIRMED |
| IFR release | 30.68 Cr | 3,068/100 | Note 5, L387 | CONFIRMED |
| Note 11 stressed pool | 110.41 Cr / 0.71% of adv | 11,040.74/100; /15,571.66 = 0.709% | L436, L364 | CONFIRMED |
| Corp/Wholesale seg result | +1.75 / +10.97 / −8.75 | 175/1,097/(875) /100 | L305 | CONFIRMED |
| PAT bridge YoY (sum) | +12.73 (2,491−1,218) | 24.91 − 12.18 = 12.73 | Step 4 | CONFIRMED |
| PAT bridge QoQ (sum) | −18.58 | 24.91 − 43.49 = −18.58 | Step 4 | CONFIRMED |

**Arithmetic verdict: zero mismatches.** All three explicitly-flagged load-bearing metrics reproduce from first principles: cost-to-income 75.79% (16,106/21,251), PCR ex-w/o 74.66% (1 − 7,261/28,657), RoA 0.45% (disclosed; my independent ×4/2-point proxy 0.46%, inside method tolerance). No FAIL on arithmetic. No loop-back to A4 on numbers.

---

## 3. ADVERSARIAL READ

### Structural / resolution checks the task named
- **Audited/unaudited label inversion (page-5 typo) — A4's resolution is CORRECT.** The current quarter (30.06.2026) is labelled Unaudited on the cover letter (L119, L121), the P&L header/status row (L235, L240) and the balance-sheet status row (L352); the auditors issued a *Limited Review*, not an audit (L152-156, L211). Only the page-5 segment status row (L292) prints "Audited" for the Jun-26 column. Three independent places vs one → the page-5 header is the typo; Q1FY27 is Unaudited. FN7 stands.
- **Standalone-only claim — CORRECT.** No consolidated statement anywhere in the 7 pages; header L37-42 states no subsidiaries/associates. S-vs-C PAT gap is structurally uncomputable (N.A.), not a data gap. A4/F2 faithful.
- **Segment-vs-BS Rs 1 lakh difference — CORRECTLY called rounding (FN8).** Seg Total 21,23,765 / 18,70,020 (L319) vs BS 21,23,766 / 18,70,019 (L359/367). 1-lakh delta, immaterial.
- **RoA tripwire adjudication — FAITHFUL.** 0.45% < 0.6% watch level and < FY26 0.53% (L279). "BREACHED, monitoring not exit" is correct for a non-held first-workup name.
- **FLAG-CASH falsifier — FAITHFUL.** Falsifier needs PCR ex-w/o <53.63% AND NNPA >1.11%; actual 74.66% and 0.47% (L275-276, L278) — both legs fail the falsifier, so NOT triggered. Correct, not overstated.
- **Cost-to-income AMBIGUOUS (not RED-FLAG) — correct call.** 75.79% sits between the 75% recovery line and 80% one-off line; ambiguous is the honest classification, not a red-flag.

### Three most positive claims, each with strongest bear counter from the same extract

**Positive claim 1 — "Asset quality is the strongest leg: GNPA 1.82%, NNPA 0.47%, PCR ex-w/o 74.66% and rising; falsifier not triggered."**
Bear counter: absolute GNPA is essentially flat QoQ (28,638 → 28,657 lakh, L275) while the provision charge was cut to 1,591 lakh (−54% QoQ, −25% YoY, L257); the coverage improvement is arithmetic (denominator/mix), and Note 6 (L389-391) confirms the charge is composite, not pure credit cost. **Counter does NOT survive as new** — A4 already carries this in full (FN1, Step 5L "provision-light", Bridge notes). No graft required.

**Positive claim 2 — "PAT +104.5% YoY; core PPOP +54.6% YoY driven by NII not other income."**
Bear counter: the entire PBT→PAT wedge is the nil-tax Q1FY26 base (0% ETR, L261) now at 29.9%; other income actually fell YoY (−11.2%, L247) and QoQ (−49.6%); the PPOP step is off a thin base. **Counter does NOT survive as new** — A4 already deflates the optic thoroughly (FN3, Step 2 answer 4, Bridge A). No graft required.

**Positive claim 3 — "Advances +27.4% YoY clears the 20% growth tripwire; CRAR 19.19% comfortable and rising; funding-mix a watch item but NIM/CoF/tenor 'not disclosed'."** (Step 5L, FN12, Q6, Tripwire 5)
Bear counter — **SURVIVES, and must be grafted into A4:** the tenor of the borrowings surge IS disclosed, in two enumerated ratios A4 never cites. Debt-Equity Ratio (L281, footnote ** = borrowings with residual maturity >1yr / equity) FELL 0.13 → 0.12 → 0.11 across Q1FY26→Q4FY26→Q1FY27, while Total-Debts-to-Total-Assets (L282, footnote *** = total borrowings / total assets) ROSE 2.25% → 3.47% → 3.88%. Back-solving: long-term borrowings ≈ 0.13×1,188.04 = 154.4 Cr (Q1FY26) → 0.11×1,308.87 = 143.9 Cr (Q1FY27), i.e. flat-to-down, against total borrowings 419.96 → 858.71 Cr (+438.75 Cr, L357). **Essentially 100% of the +439 Cr borrowings increase is short-tenor (<1yr residual):** short-term borrowings ~265 Cr → ~715 Cr, roughly +170% YoY. This is a live rollover/repricing risk that SHARPENS FN12 and directly refutes A4's own framing that funding tenor is "undisclosed" (A4 relegates "short-tenor" to a hypothetical *bull* answer in Q6, L288, when the disclosed ratios show the increment is entirely short-tenor — a *bear* fact). Cross-check: 3.88% × 22,126.24 Cr total assets = 858.5 Cr ≈ borrowings 858.71 ✓; 2.25% × 18,700.19 = 420.8 ≈ 419.96 ✓ (ratios tie to the raw lines).

Because this counter is supported by the extract and is absent from A4, per the A5 protocol it must be added to A4 before save. The enumerated rows that carry it (17(vii) L281, 17(viii) L282, plus footnotes ** L223 / *** L224) were correctly captured by A2 but generated no A3 forensic and no A4 citation — a missed forward-signal. Root loop-back: **A3** (produce the tenor/funding-durability forensic from the ratio rows), then **A4** to incorporate it into FN12 / Step 5L / Tripwire 5 and reclassify "short-tenor wholesale funding" from a bull hypothetical to a disclosed bear fact.

---

## VERDICT

**INCOMPLETE.** Coverage and arithmetic both surface the same single gap: two enumerated Analytical Ratios (Debt-Equity 17(vii) L281; Total-Debts-to-Total-Assets 17(viii) L282, with footnotes ** L223 / *** L224) are absent from A4 and carry a surviving bear counter — the entire +104% YoY borrowings increase is short-tenor (<1yr residual), a rollover/repricing risk that sharpens FN12 and corrects A4's "tenor undisclosed" framing. Loop back to **A3** to raise the forward-signal forensic, then **A4** to graft it. Everything else — all 14 notes, both other load-bearing metrics (C/I 75.79%, PCR ex-w/o 74.66%), RoA 0.45%, the page-5 label-inversion resolution, the standalone-only claim, the segment/BS rounding, and the full tripwire adjudication — passes independent re-derivation. Operating Margin (17ix) and Net Profit Margin (17x) are covered-by-derivation and reconcile (10.62%, 5.14%), not a substantive gap.

```yaml
stage: A5-adversary
company: "DHANBANK"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows:
    - "17(vii) Debt-Equity Ratio 0.11x (L281) — enumerated, absent from A4, carries surviving tenor signal"
    - "17(viii) Total-Debts-to-Total-Assets 3.88% (L282) — enumerated, absent from A4, carries surviving tenor signal"
    - "17(ix) Operating Margin 10.62% (L283) — uncited but covered-by-derivation (PPOP/Total Income), immaterial"
    - "17(x) Net Profit Margin 5.14% (L284) — uncited but covered-by-derivation (PAT/Total Income), immaterial"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Borrowings +104% YoY is a watch item but funding tenor / NIM / cost-of-funds are 'not disclosed' (FN12, Q6, Tripwire 5)"
    counter: "Tenor IS disclosed: Debt-Equity (>1yr-residual borrowings/equity) fell 0.13->0.11 while Total-Debts-to-Assets rose 2.25%->3.88%, so ~100% of the +439 Cr borrowings increase is short-tenor (<1yr) — a rollover/repricing risk. A4 relegates 'short-tenor' to a hypothetical bull answer; the ratios show it is a bear fact. Must be grafted into FN12/Step 5L/Tripwire 5."
    source_line: "L281 (Debt-Equity 17vii), L282 (Total-Debts-to-Assets 17viii), L223/L224 (footnotes ** / ***), L357 (Borrowings)"
loop_back_to: "A3"
gap: "A3 raised no forward-signal forensic from enumerated ratio rows 17(vii) L281 and 17(viii) L282; together they show the entire +104% YoY borrowings increase is short-tenor (<1yr residual maturity), a disclosed funding-durability/rollover risk that sharpens FN12 and refutes A4's 'tenor undisclosed' framing. A3 to produce the forensic; A4 to incorporate it (cite Debt-Equity 0.11x and Total-Debts-to-Assets 3.88%, reclassify short-tenor wholesale funding as a disclosed bear fact) before Notion save."
```
