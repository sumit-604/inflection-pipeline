# A5 ADVERSARY / COMPLETENESS AUDIT — TRANSRAIL LIGHTING (TRANSRAILL / 544317) — Q1 FY27

Fresh-context audit of A4 review (`review_transrail_q1fy27.md`) against A1 extracts and A2 ledgers. All figures re-derived independently from the extract line numbers; A4/A3 cites checked, not trusted. Line anchors below are the A1 extract internal line numbers (match the review's L-anchors) and ledger DP rows.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location in A4 | Present? | Non-empty / real content? |
|---|---|---|---|
| (1) Summary narrative (10-20 lines) | L440-442 | PRESENT | Yes — ~20-line single paragraph; covers revenue, margin, PAT quality, order intake, net debt, triggers, governance, decision. Real content. |
| (2) SECTOR intelligence | L444-446 | PRESENT | Yes — NEP 191,000 CKM, ₹9.15 lakh cr, 500/900 GW, Mission 300, fixed-price 65%, payer mix. |
| (3) BUSINESS-MODEL intelligence | L448-450 | PRESENT | Yes — backward integration, unit economics, model-drift points, SA-vs-CO gap as first-class metric. |
| (4) COMPETITION intelligence | L452-454 | PRESENT | Yes — KEC/Kalpataru/L&T/Skipper/Techno, win/lose axes, provenance note. |

**Audit 0 result: PASS.** All four labelled parts present and substantive.

---

## AUDIT 1 — COVERAGE (independent re-enumeration + orphan check)

Fresh grep/sweep of both extracts diffed against the A2 count tests.

| Category | A2 count | My fresh count | Basis | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — notes | 31 | 31 | 14 SA (L357-469) + 15 CO (L817-1003) + 2 cross-ref footnotes (L344/L806) | none | PASS |
| Results — line items | 90 | 90 | 38 SA table + 49 CO table + 3 geographic-revenue rows (L951/953/955) | none | PASS |
| Results — agenda items | 4 | 4 | Board-outcome items 1-4 (L26/31/41/71) | none | PASS |
| Results — auditor paras | 23 | 23 | SA 1-7 (7) + CO 1-8 incl "S."=5 entity list L554 (8) = 15 top-level; +3 SA sub (7a/b/c) +5 CO sub (8a-e) | none | PASS |
| Results — entities | 17 | 17 | Holding 1 + Subs 6 + JV 9 + Assoc 1 (L557-581; cross-check Note 14 L965-999) | none | PASS |
| Results — annexures / annexure rows | 4 / 13 | 4 / 13 | Ann II 6 (L1027-1058) + III 3 (L1076-1110) + IV 4 (L1125-1136) | none | PASS |
| Results — signatures | 5 | 5 | Board-outcome L98; SA LRR L293; CO LRR L729; SA board L487/1008; CO board L1021 | none | PASS |
| Results — zero_standing | 5 | 5 | SA deferred tax L316; CO deferred tax L768; CO NCI x3 (L790/793/796) | none | PASS |
| Presentation — slides | 32 | 32 | page markers s1-s32 | none | PASS |
| Presentation — data points | 221 | 221 (accepted) | DP001-DP221 read at source; all map coherently to s1-32 | none | PASS |
| Presentation — footnotes / chart-OCR / dividers | 4 / 3 / 5 | 4 / 3 / 5 | F1-F4; C1-C3; five divider slides | none | PASS |

**Flagged-row coverage in A4** (every ledger flag must be cited or reviewed-no-finding):
- ZERO_STANDING deferred tax nil → A4 Step 4 / A3-01 (L223). NCI nil → Step 1B. Covered.
- ENTITY_CHANGE Gactel → Note 7 row, Q9, monitorables. Covered.
- OCR_ERROR "S."→"5." L554 → preamble L11. EPS-diluted garble L817 → Step 1B ND + deck 7.99. Covered.
- OCR_ARTIFACT / SIGNATORY mismatch (TANAY/Monica) → Q16 (A3-F04/F05). Covered.
- JV naming inconsistency (L582 vs L975; L585 vs L979) → Note 14 row, A3-14. Covered.
- Presentation flags DP094/108 (PAT 106 vs 105), DP171/172 (tower capacity), DP133/142 (net-debt definitions), DP068/069 (dual CFO), DP087 (Gactel M&A), DP192 (BESS/data-centre), DP133 (net-debt swing) → all mapped to A3-F## and carried into Steps 2/5/6 and the questions table. Covered.

**Independent geographic-mix re-derivation (A4 Q5 / Note 13, CO L951-955):** In India 552.84→1,098.30 = +98.66% (+98.7% ✓); Outside India 1,084.22→604.15 = −44.28% (−44.3% ✓); Total 1,702.45 ✓. A4's mix-flip claim is extract-accurate.

**Audit 1 result: PASS.** No orphan rows (nothing missing from A4 → no A3 loop). No fresh row absent from ledger (→ no A2 loop). Counts reconcile.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw lines)

Raw consol (L746-770) and standalone (L297-342) numbers taken directly from the extract.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA consol Q1FY26 | 199.60 | 146.83+14.62+49.55−11.40 = 199.60 | L763/757/756/748 | MATCH |
| Op EBITDA consol Q4FY26 | 206.55 | 143.82+19.59+54.05−10.91 = 206.55 | same | MATCH |
| Op EBITDA consol Q1FY27 | 202.59 | 144.01+19.49+55.72−16.63 = 202.59 | same | MATCH |
| Op EBITDA consol FY26 | 820.32 | 584.34+66.37+218.68−49.07 = 820.32 | same | MATCH |
| Op EBITDA margin (rev-ops) Q1FY27 | 11.90% | 202.59/1,702.45 = 11.900% | L746 | MATCH |
| Op EBITDA margin (deck basis) Q1FY27 | 11.67% | 202.59/1,736.03 = 11.670% | L746/747 | MATCH |
| Op EBITDA standalone Q1FY27 | 204.37 | 146.68+19.36+55.70−17.37 = 204.37 | L311/308/307/299 | MATCH |
| Op EBITDA standalone FY26 (ex-exc) | 826.49 | 591.97+65.92+218.67−50.07 = 826.49 | same | MATCH |
| Reported EBITDA consol Q1FY26 | 210.99 | 146.83+14.62+49.55 = 211.00 | L763/757/756 | 0.01 rounding — immaterial |
| Core PBT ex-OI consol Q1FY27 | 127.38 | 144.01−16.63 = 127.38 | L765/748 | MATCH |
| Core PBT ex-OI standalone Q1FY27 | 129.31 | 146.68−17.37 = 129.31 | L313/299 | MATCH |
| OI/PBT consol Q1FY27 | 11.55% | 16.63/144.01 = 11.548% | L748/765 | MATCH |
| ETR consol Q1FY27 | 25.09% | 36.13/144.01 = 25.088% | L766/765 | MATCH |
| ETR standalone Q1FY27 | 24.63% | 36.13/146.68 = 24.632% (< 25.17% statutory ✓) | L314/313 | MATCH |
| ETR consol Q4FY26 | 32.68% | 47.00/143.82 = 32.680% | L766/765 | MATCH |
| PAT margin consol Q1FY27 | 6.34% | 107.88/1,702.45 = 6.337% | L770/746 | MATCH |
| Revenue YoY consol | +3.99% | 65.39/1,637.06 = 3.994% | L746 | MATCH |
| Op EBITDA YoY | +1.50% | 2.99/199.60 = 1.498% | derived | MATCH |
| Depreciation YoY | +33.31% | 4.87/14.62 = 33.31% | L757 | MATCH |
| Finance cost YoY | +12.45% | 6.17/49.55 = 12.45% | L756 | MATCH |
| EBIT (OpEBITDA−D) YoY | −1.02% | 183.10 vs 184.98 = −1.016% | derived | MATCH |
| Other income YoY | +45.88% | 5.23/11.40 = 45.877% | L748 | MATCH |
| Core op PBT YoY consol | −5.94% | −8.05/135.43 = −5.944% | derived | MATCH |
| Core op PBT YoY standalone | −6.15% | −8.47/137.78 = −6.147% | derived | MATCH |
| Reported PBT YoY | −1.92% | −2.82/146.83 = −1.920% | L765 | MATCH |
| PAT YoY | +2.56% | 2.69/105.19 = 2.557% | L770 | MATCH |
| PAT bridge: core −8.05 + OI +5.23 = PBT −2.82; +tax +5.51 = PAT +2.69 | as stated | −8.05+5.23=−2.82; −2.82+5.51=+2.69 | L748/766/770 | MATCH (JV −0.43 row is embedded in OpEBITDA, presentational only; headline subtotal correct) |
| Normalised PAT (OI reverts, ETR ~28.4%) | ~99.3 | (144.01−5.23)×0.716 = 99.37 | derived | MATCH |
| Net debt Q1FY27 | 466.42 | 58.92+716.97−228.18−81.29 = 466.42 | DP129-133 | MATCH |
| Net debt change QoQ | +292.22 / +168% | 466.42−174.2=292.22; /174.2=167.8% | DP133 | MATCH |
| ICR (trigger 4) | 3.64x | 202.59/55.72 = 3.636x | L756 | MATCH |
| SA-vs-CO PAT gap Q1FY27 | −2.67 / −2.42% | 110.55−107.88=2.67; /110.55=2.42% | L318/770 | MATCH |
| SA-vs-CO gaps Q4/Q1FY26/FY26 | −3.20 / −2.93 / −7.71 | 3.20 / 2.93 / 7.71 | L318/770 | MATCH |
| Book-to-bill (quarter) | 0.60x | 1,034/1,736 = 0.60x | DP114/DP099 | MATCH |
| Niger branch margin | 36% | 5.60/15.57 = 35.97% | L242-244 | MATCH |
| Branch-reviewed PAT share | 34.6% | 38.25/110.55 = 34.6% | L217-219/L318 | MATCH |
| Q1FY26 vs Q1FY25 base growth | +81% | 1,660/916 = +81.2% | DP091 | MATCH |

**Audit 2 result: PASS.** Every derived metric reproduces from raw lines. The only variance is a 0.01 rounding artifact on "Reported EBITDA consol Q1FY26" (211.00 vs A4's 210.99), below rounding tolerance and not load-bearing. No arithmetic FAIL.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims vs strongest extract-sourced bear counter)

A4 is already heavily bearish; two of three positives survive their own counters only because A4 pre-empts them. One counter is NOT in the review and survives.

**Positive claim 1 — "Credit rating UPGRADED to IND AA-/Stable Aug-2026; ICR ~3.6x; trigger 4 not fired" (Step 6C L309, brief L442).**
Bear counter (from DP136-139, L756, DP130): CRISIL was already AA-/Stable and stays unchanged; the "upgrade" is India Ratings aligning to the level CRISIL held, not a genuine notch improvement in standing; and the 3.64x ICR uses OpEBITDA/finance cost while finance costs are +12.5% YoY with ST borrowings +₹144.74 Cr QoQ, so cover compresses if the borrowing build persists. **Does NOT survive as an addition** — the deck text literally says "upgraded," and A4 already flags rising finance cost, the ST-borrowing build and the net-debt spike (Steps 2, 5). Already incorporated.

**Positive claim 2 — "Order book ₹16,035 Cr, 2.3x book-to-bill, provides revenue visibility" (Step 6D L317, brief L442).**
Bear counter (from DP043 vs DP117/DP119): the 2.3x is a backward-looking ratio on a book that **shrank this quarter for the first time in five years.** Closing order book rose every year FY22→FY26 (5,908→9,619→10,100→14,551→**16,313**, DP043) and then FELL to 16,035 incl-L1 / **15,635 ex-L1** at 30-Jun-2026 (DP117/DP119). It reconciles cleanly: 16,313 + 1,034 intake − 1,702 revenue = 15,645 ≈ 15,635 ex-L1. So the book is being drawn down, not replenished — a sharper statement of the RED intake signal than "visibility remains 2.3x." **SURVIVES.** A4 cites 16,035 but never 16,313 and never states the QoQ order-book contraction (grep-confirmed absent from the review). Must be grafted into A4 (Step 6D growth-trigger row and/or the brief), reinforcing "growth trigger WEAKENED."

**Positive claim 3 — "Op EBITDA margin holds inside 11.5-12.5% band (11.9%); no thesis-broken trigger fired; WEAKENED not broken" (Step 2 L165, Step 6C).**
Bear counter (from L757, DP144, derived EBIT): the margin only "holds" on the operating-EBITDA line; EBIT (post-D&A) already went negative YoY (−1.02%), D&A is +33% absorbing ahead of volume, ROCE fell 25.76%→23.58% (DP144), and the reported margin is flattered by the India-mix flip and sub-statutory ETR. **Does NOT survive as an addition** — A4 makes every one of these points explicitly (Steps 2, 4, 6, Pillar table). Already incorporated.

**Audit 3 result: ONE SURVIVING COUNTER** → order-book QoQ contraction (16,313 → 16,035/15,635), extract-sourced (DP043/DP117/DP119), absent from A4. Must be added before save. Loop back to A4.

---

## VERDICT

**INCOMPLETE.**
- Audit 0 PASS, Audit 1 PASS (no orphan rows; counts reconcile), Audit 2 PASS (no arithmetic FAIL beyond 0.01 rounding).
- Audit 3 produced one surviving bear counter not present in the review.

**loop_back_to: A4.**
**Gap:** Graft the surviving bear counter into the review — the un-executed order book DECLINED sequentially for the first time in five years, from ₹16,313 Cr (FY26 close, DP043) to ₹16,035 Cr incl-L1 / ₹15,635 Cr ex-L1 at 30-Jun-2026 (DP117/DP119), reconciling with intake ₹1,034 Cr < revenue ₹1,702 Cr. A4 cites only the 16,035 figure and the 2.3x ratio and never surfaces the QoQ contraction; add it to Step 6D (Order-book-conversion trigger) and the summary narrative as a strengthening of the RED order-intake / WEAKENED growth-trigger read. Everything else is save-ready.

```yaml
stage: A5-adversary
company: "TRANSRAILL"
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
  - claim: "Order book Rs16,035cr / 2.3x book-to-bill provides revenue visibility (Step 6D L317, brief L442)"
    counter: "Un-executed order book DECLINED QoQ for the first time in 5 years: FY26 close 16,313 (DP043) to 16,035 incl-L1 / 15,635 ex-L1 at 30-Jun-2026 (DP117/DP119); reconciles as 16,313 + 1,034 intake - 1,702 revenue = 15,645. Book is drawn down, not replenished - sharpens the RED intake signal. A4 never cites 16,313 or the contraction."
    source_line: "DP043 / DP117 / DP119 (deck s8, s16); intake DP114 L1,034; revenue L746 1,702.45"
loop_back_to: "A4"
gap: "Graft the surviving bear counter: order book fell QoQ for the first time in 5 years (16,313 FY26 -> 16,035/15,635 at 30-Jun-2026, reconciling with intake<revenue). Add to Step 6D growth-trigger row and the summary narrative. All other audits pass; review is otherwise save-ready."
```
