# A5 ADVERSARY / COMPLETENESS AUDIT — STYL Q1FY27

Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27
Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-24
Under audit: `review_styl_q1fy27.md` (A4). Re-derived independently from A1
extracts + A2 ledgers only. Unit: filing INR Mn, x0.1 = Rs Cr. On OCR pages
(7/8/11/12) both the primary and [OCR CROSS-CHECK] readings were used.

---

## AXIS 1 — COVERAGE AUDIT (fresh enumeration vs A2 ledger vs A4 citation)

Independent grep/sweep pass, diffed against both A2 ledgers.

| Category | A2 count | My fresh count | Method | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Results — numbered notes | 12 (6C+6S) | 12 | notes-section sweep L571/577/611/616/620/625 + L967/973/1005/1010/1015/1020 | none | PASS |
| Results — statement line items | 60 (32C+28S) | 60 | full sweep L385-500 / L813-905; NCI rows OCR-variant "Controlhng" confirmed | none | PASS |
| Results — auditor paragraphs | 10 (6C+4S) | 10 | C paras 1-6 (L270-349), S paras 1-4 (L718-774) | none | PASS |
| Results — board-agenda items | 5 | 5 | covering letter L52-63; no AGM/dividend/director/auditor/ESOP item exists | none | PASS |
| Results — consolidation entities | 2 | 2 | Rite Infotech (L304), Atoll Solutions (L305) | none | PASS |
| Results — zero-standing rows | 3 | 3 | C-OCI equity instrument (L453), S-Exceptional (L847), S-OCI equity (L875) | none | PASS |
| Results — signature blocks | 5 | 5 | CS (L68-78), MD x2 (L629/1024), Auditor x2 (L351/777) | none | PASS |
| Results — Note-2 IPO sub-rows | 20 | 20 | 5 objects x 2 tables x 2 columns | none | PASS |
| Presentation — slides | 32 | 32 | `^\[page N\]` markers | none | PASS |
| Presentation — slide-6 claims | 12 (S6-01..12) | 12 | L153-188 | none | PASS |
| Presentation — slides 17/18 P&L | 10+10 | 20 | L503-533 / L543-574 | none | PASS |
| Presentation — slide-31 IPO objects | 4 (+Total) | 4+1 | L930-948 | see COV-1 | PASS w/ note |

**Structural confirmations (independently re-verified, not deferred to A2):**
- No Balance Sheet / no Cash Flow Statement in the results filing. My grep for
  `Balance Sheet|Cash Flow|Assets|Liabilities` returns 1 hit, and it is the
  press-release phrase "strengthen cash flows" (L187), not a statement header.
  A2's confirmed-absence and A4's INDETERMINATE-cash treatment are correct.
- Standalone-vs-Consolidated: Consolidated carries 4 rows Standalone lacks (2
  NCI rows + duplicate "7." dual-total). Expected structural gap, correctly
  handled by A4 (F2-01 / F14-01).

**Every A2 flag traced to an A4 disposition:** MISSING_PARA_NUMBER→F14-01;
DUPLICATE_LINE_NUMBER→F14-01; UDIN_ILLEGIBLE→preamble (NOT FOUND);
ZERO_STANDING→F1-01; ENTITY mapping→F2-01; NUMBER_INCONSISTENCY(873.1/873.13)
→pres-F14; LABEL_AMBIGUITY slide15→pres-F16c; COLUMN_ALIGNMENT slide16→pres-F16a;
actuarial OCI→F9-01; segment-data-unaudited→F12-01/X4. No orphan forensic.

**COV-1 (coverage-accuracy gap, loop to A4 — NOT an orphan enumeration row):**
Slide 31 narrative (L950-951) discloses **cash & cash equivalents ~Rs 3,690 Mn
(~Rs 369 Cr), incl ~Rs 1,700 Mn unutilised IPO** — captured in A2 presentation
ledger Table 4 (line 106). A4 reviewed slide 31 (uses the Rs 170.1 Cr unutilised
via F6-01) but then states in Section 3 and triggers 5/6 that **"net debt / net
cash … all ND"**. That blanket ND is contradicted by a reviewed, deck-disclosed
figure: net cash is disclosed (~Rs 369 Cr, unaudited), and debt was fully repaid
(Rs 300 Cr, L606). Cash **conversion** legitimately remains INDETERMINATE (no
CFO, no receivable/inventory days), so the verdict cap is unaffected — but A4
should replace "net cash ND" with the deck figure flagged unaudited. Materiality:
LOW. Not a gate-failing orphan (slide reviewed), but a required A4 correction.

**Coverage verdict: COMPLETE.** No orphan ledger row; no row my fresh pass found
that the ledger lacks. A2 enumeration reproduces exactly. One A4 incorporation
correction (COV-1).

---

## AXIS 2 — ARITHMETIC AUDIT (every derived metric recomputed from raw extract)

Recomputed from OCR-cross-check numeric readings (more legible on 7/8/11/12).

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue YoY | +21.1% | (376.47-310.87)/310.87 = +21.10% | 387/511 | OK |
| Revenue QoQ | -6.9% | (376.47-404.18)/404.18 = -6.86% | 387/511 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 94.41 | 817.87+107.80+18.44 = 944.11 Mn | 424/409/407 | OK |
| Reported EBITDA YoY | +28.0% | (94.41-73.75)/73.75 = +28.01% | derived | OK |
| Reported EBITDA QoQ | -24.2% | (94.41-124.52)/124.52 = -24.18% | derived | OK |
| Reported EBITDA margin YoY | +136 bps | 25.08%-23.72% = +136 bps | derived | OK (deck 135) |
| Operating EBITDA Q1FY27 (ex-OI) | 87.31 | 94.41-7.10 = 87.31 | derived/389 | OK |
| Operating EBITDA YoY | +22.3% | (87.31-71.41)/71.41 = +22.27% | derived | OK |
| Operating EBITDA margin YoY | +22 bps | 23.19%-22.97% = +22 bps | derived | OK |
| Other Income YoY | +203.0% | (7.097-2.342)/2.342 = +203.0% | 389/513 | OK |
| Core PBT ex-OI YoY | +41.9% | (74.69-52.63)/52.63 = +41.92% | derived | OK |
| Reported PBT YoY | +48.8% | (81.79-54.97)/54.97 = +48.79% | 424 | OK |
| Reported PBT QoQ | -26.9% | (81.79-111.86)/111.86 = -26.88% | 424 | OK |
| PAT (C) YoY | +63.8% | (60.34-36.84)/36.84 = +63.79% | 443-444 | OK |
| PAT (C) QoQ | -26.2% | (60.34-81.79)/81.79 = -26.23% | 443-444 | OK |
| PAT margin Q1FY27 | 16.03% | 60.34/376.47 = 16.03% | derived | OK |
| Standalone PAT Q1FY27 | 61.75 | 617.45 Mn /10 | 865 | OK |
| Standalone PAT YoY | +68.4% | (61.75-36.68)/36.68 = +68.35% | 865 | OK |
| C-minus-S PAT gap Q1FY27 | -1.41 | 60.34-61.75 = -1.41 | 443-444/865 | OK |
| C-minus-S gap Q1FY26 | +0.16 | 36.84-36.68 = +0.16 (sign-flip) | 443-444/865 | OK |
| C-minus-S gap FY26 | -3.73 | 240.01-243.74 = -3.73 | 443-444/865 | OK |
| ETR Q1FY26 (C) | 33.0% | 181.35/549.74 = 32.99% | 436/424 | OK |
| ETR Q4FY26 (C) | 26.81% | 299.87/1118.63 = 26.81% | 436/424 | OK |
| ETR Q1FY27 (C) | 26.29% | 215.03/817.87 = 26.29% | 436/424 | OK |
| ETR FY26 (C) | 27.05% | 889.31/3287.44 = 27.05% | 436/424 | OK |
| Gross margin Q1FY27 | 41.7% | 156.83/376.47 = 41.66% | 387/397-402/411 | OK |
| Gross margin Q1FY26 | 44.5% | 138.40/310.87 = 44.52% | 387/397-402/411 | OK |
| Gross margin Q4FY26 | 46.9% | 189.65/404.18 = 46.92% | 387/397-402/411 | OK |
| **Gross profit Q4FY26 (Rs Cr)** | **190.66** | **404.18-214.52 = 189.65** | 387/397-402/411; deck 1,897 Mn L445 | **MISMATCH (ARI-1)** |
| PAT bridge total | +23.50 (bridge 23.46) | 60.34-36.84 = +23.50; components sum 23.46 | Section 3 | OK (rounding disclosed) |
| Operating EBITDA Δ (bridge) | +15.90 | 87.31-71.41 = +15.90 | Section 3 | OK |
| Finance-cost YoY tailwind | +5.92 | 7.76-1.84 = +5.92 | 407-408 | OK |
| Subsidiaries net PAT | -0.14 | -2.15+0.77 = -1.38 Mn = -0.14 Cr | 334/340 | OK |
| Op-EBITDA FY26 / margin | 379.26 / 26.32% | 393.84-14.58=379.26; /1441.14=26.32% | derived | OK |
| Reported-EBITDA FY26 / margin | 393.84 / 27.33% | 3287.44+442.15+208.79=3938.4 Mn | derived | OK |
| Payments YoY / QoQ path | +5.6%; 1984→1919→1582 | (1582-1498)/1498=+5.61%; two QoQ declines | slide12 L325 | OK |
| Payments mix share | ~48%→42% | 1498/3108.7=48.2%; 1582/3764.7=42.0% | slide12/6 | OK |
| IoT YoY | +144% | (674-276)/276 = +144.2% | slide14 L395 | OK |
| Other-expense ratio | 13.8% vs 16.7% | 519.8/3764.7=13.8%; 520.1/3108.7=16.7% | slide17 L519 | OK |

**Only one arithmetic mismatch above rounding:**

**ARI-1 — Gross profit Q4FY26 = 190.66 (A4) vs 189.65 (recomputed).** A4 Section
2c "Derived metrics" row `Gross profit (Rev − net materials)`. Q4FY26 net
materials = CoM 2,255.20 + Purchases 14.57 + ΔInv (-124.53) = 2,145.24 Mn =
214.52 Cr; Revenue 404.18 Cr; gross profit = **189.65 Cr**, not 190.66. Deck
slide 15 independently prints Q4FY26 gross profit **1,897 Mn = 189.7 Cr**
(L445), confirming 189.65 and refuting 190.66. Overstatement +1.01 Cr; looks like
a 189.66→190.66 digit slip. **Materiality: LOW / non-load-bearing** — this cell
feeds no headline, no PAT bridge, no trigger; the derived Q4FY26 gross margin
(46.9%) is computed correctly from the true number, and the Q1FY26/Q1FY27 gross-
profit cells (138.40 / 156.83) are both correct. But it is a mismatch above
rounding in a published derived-metrics table, so per protocol it is a FAIL to
be corrected by A4 before save.

Every other figure in A4's tables — headline scorecard, extraction table 2a/2b,
derived table 2c, PAT bridge, FTTCP triggers, and the standalone-vs-consolidated
gaps — reproduces exactly on independent recomputation, including across the
NUMBER_FIDELITY OCR cells (A4 uses primary readings only where the two OCR
readings would not change any answer; the one true dual-reading cell that could
have mattered, S-Dep Q1FY26 110.11/110.14, is immaterial to any metric A4 cites).

**Arithmetic verdict: one correction (ARI-1), otherwise sound.**

---

## AXIS 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the same text)

A4 is already heavily hedged (PROCEED WITH FLAGS). Testing its three most
positive claims for a surviving counter drawn only from the extracts.

**Positive claim 1 — "Revenue +21.1% YoY: Trigger 1 FIRED FAVOURABLY" (§5, L228).**
Strongest bear from same text: the deck itself attributes the growth to
"normalisation of business activity from the **relatively subdued Q1FY26 base**"
(slide 17, L508-509), and slide 16 / filing show FY revenue essentially
flat-to-declining on a 3-year view (FY24 ~15,583 → FY26 14,411; F16a). **Counter
does NOT survive as new:** A4 already carries the flat-to-declining-3yr point
(X1/F16a, Question 14) and the -6.9% QoQ softness. The only incremental item is
that A4 could cite the deck's own "subdued base" admission (L508) against the
FIRED-FAVOURABLY label. Recommended one-line addition; not gate-blocking.

**Positive claim 2 — "EBITDA +28.0% YoY, margin expanded to 25.1% (+135 bps)"
(deck headline, folded into §1).** Strongest bear from same text: expansion is
almost entirely Other Income (+203% YoY); clean operating EBITDA margin only +22
bps; gross margin −286 bps. **Counter does NOT survive:** A4 already makes exactly
this bear case (X2, pres-F16b, Section 3, Flag 1). Fully incorporated.

**Positive claim 3 — "PAT +63.8% YoY, PAT margin 16.0% (+418 bps)" (§1 / §3).**
Strongest bear from same text: management's own remark (slide 17, **L529-532**)
benchmarks the 16.0% margin against the **FY26 full-year average of 16.7%** — so
current-quarter PAT margin sits **below** last year's full-year level despite the
+418 bps YoY optics off a tax-depressed Q1FY26 base. A4 dismantles the *growth
rate* (finance-cost collapse + ETR normalisation + Other Income) and even carries
FY26 PAT margin 16.65% in Section 2c, but **never states the direct sequential-vs-
annual point that 16.0% < 16.7%**, which is a cleaner, management-admitted
expression of the same earnings-quality concern. **Counter SURVIVES (BEAR-1).**
It must be grafted into A4 Section 3 / Flag 3 before save. Materiality: LOW-MODERATE
— it corroborates and sharpens an existing flag; it does not change the verdict.

---

## DISCREPANCY LIST

| ID | A4 claim | My recomputation / finding | Line cite | Loop | Materiality |
|---|---|---|---|---|---|
| ARI-1 | Gross profit Q4FY26 = **190.66** Cr (§2c) | **189.65** Cr (404.18 − 214.52); deck prints 1,897 Mn = 189.7 Cr | res 387/397-402/411; deck L445 | A4 | LOW (non-load-bearing; GM% correct) |
| BEAR-1 | PAT +63.8% / margin 16.0% flattered, but sequential-vs-annual not stated | 16.0% Q1FY27 margin is **below FY26 full-year 16.7%** — management's own benchmark; surviving bear counter to graft | deck L529-532; A4 §3 | A4 | LOW-MOD (sharpens existing flag) |
| COV-1 | "net debt / net cash … all ND" (§3, triggers 5/6) | Deck discloses cash ~Rs 3,690 Mn (~Rs 369 Cr) incl ~Rs 1,700 Mn unutilised IPO; net cash IS disclosed (unaudited). Cash *conversion* still INDETERMINATE | deck L950-951 | A4 | LOW (verdict cap unchanged) |

All three loop to **A4** only. A2 enumeration is exact (no loop to A2). No
unreviewed forensic row (no loop to A3). None of the three alters the
PROCEED WITH FLAGS verdict, the INDETERMINATE cash-conversion cap, or the
UNCHANGED (HELD) Decision Status — they are bounded corrections/additions.

---

## GATE VERDICT

**INCOMPLETE** — loop back to **A4** for three bounded fixes before Notion save:
1. **ARI-1:** correct Gross profit Q4FY26 in Section 2c from 190.66 to 189.65 Cr.
2. **BEAR-1:** graft the surviving bear counter — Q1FY27 PAT margin 16.0% is
   below the FY26 full-year average 16.7% (deck L529-532) — into Section 3 / Flag 3.
3. **COV-1:** replace the "net cash ND" statement with the deck-disclosed cash
   ~Rs 369 Cr (incl ~Rs 170 Cr unutilised IPO, deck L951, unaudited); retain the
   cash-**conversion** INDETERMINATE cap (still no CFO / receivable / inventory days).

Coverage is otherwise complete (fresh enumeration reproduces A2 exactly; no
orphan row; no ledger gap) and arithmetic is otherwise sound (all headline,
bridge, ETR, margin, and standalone-vs-consolidated figures confirmed). Once A4
applies the three corrections, the review is fit to proceed.

---

```yaml
stage: A5-adversary
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Gross profit Q4FY26 (Rs Cr)", a4_value: 190.66, recomputed: 189.65, source_line: "results 387/397-402/411; deck L445 (1,897 Mn)"}
surviving_bear_counters:
  - {claim: "PAT +63.8% YoY, PAT margin 16.0% (+418 bps)", counter: "Q1FY27 PAT margin 16.0% is below FY26 full-year average 16.7% (management's own benchmark) — sequential/annual profitability not improved despite YoY optics", source_line: "deck L529-532"}
loop_back_to: "A4"
gap: "A4 to fix three bounded items before save: (1) correct Section 2c Gross profit Q4FY26 190.66 -> 189.65 Cr; (2) graft surviving bear counter PAT margin 16.0% < FY26 16.7% (deck L529-532) into Section 3/Flag 3; (3) replace 'net cash ND' with deck-disclosed cash ~Rs 369 Cr incl ~Rs 170 Cr unutilised IPO (deck L951, unaudited) while retaining cash-conversion INDETERMINATE cap. No loop to A2 (enumeration exact) or A3 (no unreviewed forensic). Verdict PROCEED WITH FLAGS and HELD Decision Status otherwise supported."
```
