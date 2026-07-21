# A5 ADVERSARY / COMPLETENESS AUDIT (RE-AUDIT, post-loop-1) — TATVA CHINTAN PHARMA CHEM LIMITED (TATVA), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only. Re-derived independently; A4/A3 cites checked, not deferred to.
Prior audit returned INCOMPLETE (surviving counter: Step 4 tagged the full YoY PAT growth "Recurring / 100%+ / the quarter is real" while 43.1% was subsidiary-sourced and durability-unresolved). This run re-checks all three audits fresh; verdict at end.

Unit convention re-verified against both extract headers: `unit_convention: Millions`, `conversion_factor_to_cr: Millions -> x0.1`. All Rs Cr below = Rs Mn x0.1, re-derived from raw extract lines.

---

## 1. COVERAGE AUDIT (fresh grep/sweep over each A1 extract, diffed vs A2 ledgers, then checked against A4)

### 1A. Results extract (563 lines)

| Category | A2 count | My fresh count | Basis (extract lines) | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Numbered notes | 13 | 13 | Consol L359-390 = notes 1-7 (note 5 = standalone key-numbers, OCR dropped numeral); Standalone L538-560 = notes 1-6 | none — all in A4 Step 0D table (C1-C7, S1-S6) | PASS |
| Financial-table line items | 65 | 65 | Consol 38 (L286-344), Standalone 27 (L484-522); P&L rows tabulated, OCI/NCI/other-equity reviewed-no-finding | none — P&L cited Step 1; OCI/NCI/other-equity via zero-standing + preamble L11-16 | PASS |
| Zero-standing items | 6 | 6 | 3x NCI (L323/328/334), Consol other-equity (L344), Std purchases-stock-in-trade (L490), Std other-equity (L522) | none — reviewed-no-finding; correctly non-material | PASS |
| Board-outcome agenda items | 6 | 6 | L36-74: results(1), Shah-MD(2), Patel-WTD(3), Somani-WTD(4), Dahej-III(5), borrowing-limit(6) | none — items 2-6 in Step 6D/7/8.5/monitorables; item 1 is the results | PASS |
| Annexure Sr-rows | 12 | 12 | Director table 5 rows (L114-165) + capacity table 7 rows (L175-186) | none — director re-appointments (Q9/F13) + capacity 344KL/Rs200Cr/21mo/debt (Step 6D, Q3) cited | PASS |
| Auditor paragraphs | 10 | 10 | Consol report 6 paras (L199-251), Standalone report 4 paras (L413-444) | none — both unmodified, no Other Matters, cited Step 0D + F4-a | PASS |
| Consolidation entities | 3 | 3 | L228-230: Holding + USA WOS + Europe B.V. WOS | none — central to Step 4 subsidiary analysis + F4-a | PASS |
| Signature/signing blocks | 5 | 5 | CS letter (L91), Consol fin Chintan (L397), Std fin Chintan (L569), Consol auditor (L262), Std auditor (L455) | none — F14-a/F14-b in A4 incorporated list (review L16/L449) | PASS |

### 1B. Presentation extract (1613 lines, 36 slides)

| Category | A2 count | My fresh count | Basis | Orphan rows | Status |
|---|---|---|---|---|---|
| Slides | 36 | 36 | 36 `[page N]` markers; matches formfeed/page_count | none — material slides 5/6/7/8/9/10/12/20/22/23/34 all used | PASS |
| Numeric tokens | 1427 | 1427 (per-slide totals accepted) | per-page regex totals reconcile to whole-file sweep | none material | PASS |
| Line items | 64 | 64 | Slide 6 (7) + slide 9 P&L (19) + slide 10 BS (22) + slide 34 (16) | none — slide 6 Step 1 cross-check; slide 9 FY25 base + FY23 exceptional; slide 10 Step 5 BS ref; slide 34 valuation/float | PASS |
| Footnotes | 6 | 6 | Rounding (L423/612/1065), Source CEFIC/IBEF (L1457), Source NSE (L1565), Safe Harbor (L1577-1588) | none — rounding notes used in Step 1C cross-check | PASS |
| Zero-standing | 2 | 2 | Exceptional items FY23-only dash (slide 9), LT borrowings FY25 dash (slide 10) | none — FY23 Rs 3.59 Cr exceptional cited (Q5, YAML); LT borrowings in Step 5 net-debt calc | PASS |

**Coverage result:** fresh enumeration reproduces every A2 count exactly (no row my pass found that the ledger lacks — no loop-back to A2). Every ledger row is cited in A4 or covered as reviewed-no-finding (no orphan — no loop-back to A3). COVERAGE = PASS.

---

## 2. ARITHMETIC AUDIT (recomputed from raw Mn x0.1; A4 value vs my recompute vs source line)

### 2A. Operating EBITDA (excl OI) = PBTbe + Depr + Fin − OI, and margin

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 | 32.30 | 224.29+105.66+20.81−27.80 = 322.96 Mn = 32.30 | L300/296/295/287 | PASS |
| Consol Op EBITDA Q1FY26 | 17.33 | 91.01+89.71+4.13−11.55 = 173.30 = 17.33 | L300/296/295/287 | PASS |
| Consol Op EBITDA Q4FY26 | 28.13 | 165.87+97.55+14.38−(−3.48) = 281.28 = 28.13 | L300/296/295/287 | PASS |
| Consol Op EBITDA FY26 | 93.16 | 570.09+368.47+28.51−35.49 = 931.58 = 93.16 | L300/296/295/287 | PASS (ties deck 932, L443) |
| Consol Op EBITDA margin Q1FY27 | 19.3% | 322.96/1670.55 = 19.33% | L286 | PASS |
| Consol Op EBITDA margin Q1FY26 | 14.8% | 173.30/1168.64 = 14.83% | L286 | PASS |
| Std Op EBITDA Q1FY27 | 24.03 | 154.12+105.65+20.81−40.33 = 240.25 = 24.03 | L498/495/494/485 | PASS |
| Std Op EBITDA margin Q1FY27 | 16.4% | 240.25/1467.02 = 16.38% | L484 | PASS |

### 2B. ETR, YoY, QoQ, PAT-bridge line items

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Consol ETR Q1FY27 | 24.3% | 51.30/211.11 = 24.30% | L306/302 | PASS |
| Consol ETR Q4FY26 | 37.8% | 62.66/165.87 = 37.78% | L306/302 | PASS |
| Std ETR Q1FY27 | 25.9% | 36.48/140.94 = 25.88% | L504/500 | PASS |
| Revenue YoY | +42.9% | 1670.55/1168.64−1 = +42.96% | L286 | PASS (deck +43%) |
| Op EBITDA YoY | +86.3% | 322.96/173.30−1 = +86.4% | L300/296/295/287 | PASS |
| Op EBITDA margin YoY | +448 bps | 19.33%−14.83% = +4.50pp = +450 bps | L300/296/295/287/286 | PASS (within rounding; A4 448 vs 450, 2 bps, immaterial) |
| PAT YoY | +140.3% | 159.81/66.51−1 = +140.3% | L307 | PASS |
| Revenue QoQ | +24.5% | 1670.55/1341.44−1 = +24.53% | L286 | PASS (deck +25%) |
| Op EBITDA margin QoQ | −163 bps | 20.97%−19.33% = −1.64pp = −163.5 bps | L300/296/295/287/286 | PASS |
| Bridge: Op EBITDA growth | +14.97 | 32.30−17.33 = +14.97 | derived | PASS |
| Bridge: Depr change | −1.60 | 8.97−10.57 = −1.60 | L296 | PASS |
| Bridge: Fin change | −1.67 | 0.41−2.08 = −1.67 | L295 | PASS |
| Bridge: OI change | +1.62 | 2.78−1.16 = +1.62 | L287 | PASS |
| Bridge: Exceptional | −1.32 | 13.18 Mn = 1.32 | L301 | PASS |
| Bridge: Tax change | −2.68 | 2.45−5.13 = −2.68 | L306 | PASS |
| Bridge sum vs reported | +9.33 | components sum = +9.32; reported 15.98−6.65 = +9.33 | L307 | PASS (0.01 rounding drift across rounded components; "ties exactly" loose but immaterial) |

### 2C. NEW parent-vs-subsidiary split (verified specifically per task)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Consol PAT Q1FY26 / Q1FY27 | 6.65 / 15.98 | 66.51 / 159.81 Mn x0.1 | L307 | PASS |
| Standalone PAT Q1FY26 / Q1FY27 | 5.13 / 10.45 | 51.33 / 104.46 Mn x0.1 | L505 | PASS |
| Parent piece (std growth) | +5.31 | 104.46−51.33 = 53.13 Mn = +5.31 | L505 | PASS |
| Subsidiary piece (consol−std growth) | +4.02 | (159.81−104.46)−(66.51−51.33) = 5.54−1.52 = +4.02 | L307−L505 | PASS |
| Check parent+subsidiary | +9.33 | 5.31+4.02 = 9.33 | — | PASS |
| Parent share | 56.9% | 5.31/9.33 = 56.9% | — | PASS |
| Subsidiary share | 43.1% | 4.02/9.33 = 43.1% | — | PASS |
| Subsidiary PAT % of consol Q1FY26 | 22.8% | 1.52/6.65 = 22.8% | L307/505 | PASS |
| Subsidiary PAT % of consol Q4FY26 | 12.6% | (10.32−9.02)/10.32 = 1.30/10.32 = 12.6% | L307/505 | PASS |
| Subsidiary PAT % of consol Q1FY27 | 34.6% | 5.54/15.98 = 34.6% | L307/505 | PASS |
| Subsidiary PAT % of consol FY26 | 7.1% | (42.05−39.08)/42.05 = 2.97/42.05 = 7.1% | L307/505 | PASS |
| Subsidiary revenue Q1FY27 | 20.35 | 1670.55−1467.02 = 203.53 Mn = 20.35 | L286/484 | PASS |
| Subsidiary revenue Q4FY26 | 1.48 | 1341.44−1326.65 = 14.79 Mn = 1.48 | L286/484 | PASS |

**Arithmetic result:** the new split is arithmetically correct on both periods and every derived share (parent = std growth; subsidiary = consol−std growth; shares of the +Rs 9.33 Cr total tie). Two sub-rounding drifts noted (+448 vs +450 bps; bridge 9.32 vs stated 9.33) — both below any material threshold; neither changes a conclusion. No arithmetic FAIL; no loop-back to A4 on arithmetic.

---

## 3. ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

### Claim 1 — "PAT +140% YoY driven by operations, not treasury; a strong, real operating quarter."
Strongest counter (the prior surviving one): 43.1% (+Rs 4.02 Cr of +Rs 9.33 Cr) is subsidiary-sourced (consol L307 − std L505) through two zero-cost foreign distribution WOS whose revenue leapt Rs 1.48 → 20.35 Cr in one quarter (L286/L484), with unresolved durability/transfer-price basis.
**Status: GRAFTED (genuinely, not cosmetically).** Step 4 now carries the parent-vs-subsidiary bridge, explicitly WITHDRAWS the "quarter is real / 100%+ recurring" framing (review L223), Step 2 diagnostic #3 defers recurrence to Step 4 (L167), and flags-block item 2 + YAML `pat_growth_recurrence_split` mirror the 56.9%/43.1% split with the subsidiary tagged UNRESOLVED. Step 4 no longer conflicts with the flags block. This counter does NOT survive as new — it is incorporated.

### Claim 2 — "Operating EBITDA margin +448 bps YoY to 19.3% = genuine operating leverage."
Strongest counter: sequentially the margin FELL 21.0% → 19.3% (−163 bps, L300/296/295/287/286) on +24.5% QoQ revenue; 19.3% sits BELOW the FY27 20-22% guide (not restated); the YoY expansion is amplified by a depressed Q1FY26 comparable (14.8%).
**Status: GRAFTED.** Covered in Step 3 (margin fade, A3-09), monitor #4 (AMBER), and flags-block item 5. Does not survive as new.

### Claim 3 — "Parent (standalone) supplies 65.4% of consol PAT (> the >50% monitor #7 threshold), and its +Rs 5.31 Cr is 'confirmably recurring at the parent this quarter (manufacturing P&L, arm's-length).'"
Strongest counter FROM THE SAME EXTRACT: the parent's own +Rs 5.31 Cr PAT growth is inflated by NON-RECURRING Other Income. Standalone Other Income (L485) rose Q1FY26 1.37 → Q1FY27 4.03 Cr = **+Rs 2.66 Cr YoY**, and standalone OI is **28.6% of standalone PBT** (4.03/14.09, L485/L500) vs 19.4% a year ago. A4's own line-item bridge tags Other Income "NON-RECURRING," yet the entity split re-absorbs the full standalone growth (which re-includes that OI) into the "confirmably recurring" parent bucket. Strip the parent OI surge (~Rs 2.66 Cr pretax; ~Rs 1.97 Cr post-tax at the 25.9% std ETR) and only ~Rs 3.3 Cr — roughly **36% of the +Rs 9.33 Cr, not ~57%** — is parent manufacturing-recurring. Corroborating: standalone core PBT ex-OI (the cleaner parent read) actually FELL QoQ 15.34 → 10.06 Cr (A4's own Step 1D), and standalone current tax was NIL this quarter (L502) with a Rs 3.65 Cr deferred charge carrying 100% of the tax line — a zero cash-tax quarter that further flatters parent PAT.
**Status: SURVIVES — must be grafted into A4.** The facts (L485 standalone OI, L500 std PBT, L502 nil current tax) are all in the extract and even in A4's own tables, but A4 never nets them out of the headline "at most ~57% confirmably recurring / parent = manufacturing P&L" claim. This produces an internal inconsistency between A4's two Step 4 decompositions (line-item bridge tags OI non-recurring; entity bridge silently re-includes it) and overstates durably-recurring earnings by ~Rs 2 Cr / ~21 pts of the +9.33 Cr. It is the same class of quality-of-earnings issue as the original bear counter, one level deeper (parent Other Income rather than subsidiary markup), and material to the quarter's central question.

---

## VERDICT

**INCOMPLETE.** Coverage PASS (all A2 counts reproduced; no orphan rows; no missing rows). Arithmetic PASS (the new parent/subsidiary split verified correct on both periods and every share; only immaterial sub-rounding drifts). But one adversarial counter survives and is not yet incorporated in A4.

- **Loop back to: A4.**
- **Exact gap:** Step 4's "parent (standalone) +Rs 5.31 Cr is confirmably recurring (manufacturing P&L)" and the derived "at most ~57% of the +Rs 9.33 Cr PAT growth is confirmably recurring" do NOT net out the parent's own NON-RECURRING Other Income, which A4's own line-item bridge tags non-recurring. Standalone Other Income rose Rs 1.37 → 4.03 Cr YoY (+Rs 2.66 Cr, L485), 28.6% of standalone PBT (L485/L500). Stripping it (with the nil standalone current tax, L502, as corroboration) drops the durably-recurring parent share to ~36% of +Rs 9.33 Cr. A4 must (a) reduce the "confirmably recurring parent" piece by the non-recurring standalone OI, (b) reconcile the two Step 4 decompositions so OI is not tagged non-recurring in one and recurring in the other, and (c) revise the "~57% confirmably recurring" headline and flags-block item 2. Re-submit for A5 re-audit before any Notion save.

```yaml
stage: A5-adversary
company: "TATVA"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Parent standalone +Rs 5.31 Cr is 'confirmably recurring (manufacturing P&L)'; ~57% of +Rs 9.33 Cr PAT growth confirmably recurring"
    counter: "Parent +Rs 5.31 Cr includes non-recurring standalone Other Income growth of +Rs 2.66 Cr (1.37->4.03 Cr, 28.6% of standalone PBT), which A4's own line-item bridge tags non-recurring; net of it only ~Rs 3.3 Cr (~36% of +9.33), not ~57%, is parent manufacturing-recurring. The two Step 4 decompositions conflict (OI non-recurring in the line bridge, re-absorbed as recurring in the entity split). Nil standalone current tax (L502) further flatters parent PAT."
    source_line: "L485 (std Other Income 13.69->40.33 Mn); L500 (std PBT 140.94 Mn); L502 (std current tax nil); review Step 4 L216-223"
loop_back_to: "A4"
gap: "Step 4 'parent confirmably recurring +Rs 5.31 Cr / ~57% recurring' does not net out the parent's own non-recurring standalone Other Income (+Rs 2.66 Cr YoY, 28.6% of std PBT, L485) — tagged non-recurring in A4's own line-item bridge yet re-included in the entity split. Net durably-recurring parent share is ~36% of +Rs 9.33 Cr. A4 must strip parent OI, reconcile the two Step 4 decompositions, and revise the ~57% headline and flags-block item 2."
```
