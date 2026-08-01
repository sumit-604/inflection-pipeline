# A5 ADVERSARY / COMPLETENESS AUDIT — GARGI Q1 FY27

Company: PNGS Gargi Fashion Jewellery Ltd (GARGI, BSE 543709) | Quarter: Q1 FY27 (qtr ended 30-Jun-2026)
Auditor: A5 (adversary), Opus 4.8 | Date: 2026-08-01
Under audit: review_gargi_q1fy27.md (A4)
Fresh-context basis: A4 review + A1 extracts (results, presentation) + A2 ledgers only. I re-derived every unit conversion and every derived metric independently; I did not defer to A4's or A3's cites.

**VERDICT: COMPLETE** (after loop-1 corrections verified in loop-2 re-audit). One non-blocking cite-hygiene correction noted for A4 (does not change any figure or verdict).

---

## LOOP-2 RE-AUDIT (2026-08-01) — verification of A4's applied fixes

A4 applied fixes for the two loop-1 defects and grafted the three bear counters. I re-checked each against the raw extracts.

| # | Loop-1 defect / graft | A4 fix | My independent re-check | Status |
|---|---|---|---|---|
| 1 | Non-EBO YoY was −5.3% (wrong denominator) | Now −6.3% / −6.34% off prior non-EBO base 248.97 Mn | EBO 69 Mn (U16), +186% (U23) -> EBO Q1FY26 24.13 Mn; non-EBO 233.2 Mn vs 248.97 Mn = 233.2/248.97−1 = **−6.34%**. Present at review L230 (−6.34%, 233.2/248.97 shown), L273 (−6.3%), L322 (Q3, 24.90->23.32), L342 (top-3), L378 (verdict), YAML L410 & L442. All read off the prior base, none off total revenue. | **RESOLVED** |
| 2 | "9 gross / 5 net / ~4 undisclosed closures" (unsupported) | Corrected to +9 net (126->135); closures inference removed; item #5 GREEN | FY26 126 (U53) -> Q1FY27 135 (U85) = **+9 net**; corroborated by U86 (9 adds) and U102 (+32 in FY26 = 94+32=126). No closure count exists in either extract, so the removal is correct. "~4 closures" inference gone from L151/L242/L253/L272/L357/L381/L430/L448. Item #5 now **GREEN** (>=5/q). | **RESOLVED** (minor cite issue below) |
| 3a | Graft: PAT-margin pass is OI-dependent | Marked PASS (marginal, OI-DEPENDENT); OI-normalised ~15.05% | Strip excess OI 0.6763 Cr at 25.59% tax: after-tax hit 0.5032 Cr; PAT 5.0496−0.5032 = 4.5464 Cr; 454.64/3021.62 = **15.05%**. Present L229, L240, L260, L378, YAML L442. | **GRAFTED, correct** |
| 3b | Graft: gross margin both directions | +154 bps YoY shown against −389 bps QoQ and below FY26 42.93% | GM Q1FY27 42.203%, Q4FY26 46.091% -> **−389 bps** QoQ; FY26 42.93% > 42.20%. Present L131, L151, L163, L174, L274, YAML L450. | **GRAFTED, correct** |
| 3c | Graft: pref price now underwater | Item #14 moved GREEN->AMBER (Rs 970 vs CMP 632 ≈ −35%) | 632/970−1 = **−34.8% ≈ −35%**. Present L251 (−34.8%), L253, YAML L449. | **GRAFTED, correct** |
| — | FN08 parent-vs-listed halo | Recast as attribution-only; no implied GARGI closure count | Q7 (L326) now asks GARGI-specific closure count with parent-attribution framing; L289/L381/L447 attribution-only; no closure count asserted against GARGI. | **RESOLVED** |

### Non-blocking cite-hygiene correction (for A4; does not affect any figure or verdict)
In Step 3 (review L151) and checklist item 5 (review L242) the "+9 net (126 -> 135)" claim is anchored to "**U86/U102/U113**." **U113 is the wrong data unit** — per the presentation ledger U113 is the "FY26 revenue of Rs 149 crore" capital-efficiency text box (slide 20, line 596), not a store count. The correct anchors are **U85** (135 POS, slide 14) for the endpoint and **U53** (126 POS, slide 12) or **U112** (chart total series) for the FY26 base; U86 (9 adds) and U102 (+32 in FY26) already correctly corroborate. Recommend A4 swap U113 -> U85 (and add U53) at L151/L242. The +9-net figure itself is correct and independently verified, so this is a pointer fix only, not a substance defect — it does not gate the save.

### Regression checks (nothing else moved)
- **Coverage:** preamble unchanged (results 9 notes / 28 line items / 3 zero-standing / 1 agenda / 4 auditor paras / 0 entities / 4 signatory blocks; presentation 33 slides / 221 data-unit rows / 210 content lines). A3-findings list intact, FN13 explicitly noted "accepted with correction" (L21). No orphan row introduced, none removed. Independent re-enumeration still reproduces (Audit 1). **PASS.**
- **Binary test:** still **3 of 4 fail** — CFO/PAT FAIL (FY26 0.352x), comparable growth FAIL (+10.64%), non-EBO FAIL (−6.34%), PAT margin PASS (marginal/OI-dependent). L232. **Intact.**
- **Four Notion REDs:** items 1-4 still RED; item 5 GREEN, item 14 AMBER (both intentional loop-1 corrections). **Consistent.**
- **AMBIGUOUS/FORWARD-SIGNAL -> management question:** count 17 (L338). Every extract-visible guidance/forward/contradiction/reconciliation item maps to a question (Q1/Q4/Q5/Q6/Q7/Q8/Q9/Q10/Q11/Q13/Q14/Q15/Q16/Q17). FN13 is now resolved on primary text (net +9, no closures) and correctly no longer carries a standalone question; its residual POS-count-basis ambiguity is carried by Q8 (FN14, 135/136/138 reconciliation). **Legitimate.**
- **Role 5 N.A.:** unchanged and legitimate — no concall transcript in the artifact set (results + presentation only; 0 turns). **Confirmed.**
- **Protocol verdict:** PROCEED WITH FLAGS, cash conversion INDETERMINATE, HELD — unchanged and correctly caps at PROCEED WITH FLAGS per house rules. **Consistent.**

**No defect survives that blocks save.** The one open item (U113 mis-cite) is a non-blocking pointer correction with the number independently verified correct.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

| Category (doc) | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results — notes | 9 | 9 (main 1-7 + outlook 1-2) | none | PASS |
| Results — line items | 28 | 28 (table L124-171) | none | PASS |
| Results — zero-standing | 3 | 3 (L141/L148/L169) | none | PASS |
| Results — agenda items | 1 | 1 (L18) | none | PASS |
| Results — auditor paras | 4 | 4 (L53/59/67/78) | none | PASS |
| Results — consolidation entities | 0 | 0 | none | PASS |
| Results — signatory blocks | 4 | 4 | none | PASS |
| Presentation — slides | 33 | 33 | none | PASS |
| Presentation — data-unit rows | 221 | 221 (U1-U221) | none | PASS |
| Presentation — numeric content lines | 210 | consistent | n/a | PASS |

No orphan rows; no missing-from-ledger rows. Both A2 gates reproduce independently.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs / Rs Mn)

Full P&L / margin / tax / bridge / cash-quality re-run confirmed in loop-1 (Op EBITDA and margins; ETR; gross profit/margin; all YoY and QoQ %; PAT bridge to −0.26; CFO/PAT 0.352x/0.511x/0.362x; inventory 206.5 / receivable 33.3 / payable 26.8 days; CCC 213.0; PPE +186%; cash gap 727.5−8.6 = 718.9 Mn; FY26 +18.2% reported / ~49% ex-one-time; TTM EPS 29.74 / PE 21.3x; pref 1,12,500 shares; FY23 EPS Rs 4.9 implied vs Rs 10.2). All PASS.

Loop-2 corrected figures, recomputed and CONFIRMED:

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Non-EBO YoY | −6.34% | 233.2/248.97 − 1 = −6.34% (EBO 69 Mn @ +186% -> 24.13 Mn) | U16/U23/U31 | PASS |
| OI-normalised PAT margin | ~15.05% | 4.5464/30.2162 = 15.05% (strip excess OI 0.6763 Cr @ 25.59% tax) | res L125/L143/L150 | PASS |
| Gross margin QoQ | −389 bps | 42.203% − 46.091% = −389 bps | U34 / derived | PASS |
| Pref underwater | ~−35% | 632/970 − 1 = −34.8% | res L244 / pres U215 | PASS |
| Net store adds | +9 | 135 − 126 = +9 | U85/U53/U86/U102 | PASS (cite U113 wrong; number correct) |

**Arithmetic mismatches remaining: none.**

---

## AUDIT 3 — ADVERSARIAL READ

All three loop-1 surviving bear counters have been grafted into A4 and are stated with correct figures (LOOP-2 rows 3a/3b/3c). No new surviving bear counter on re-read: A4's remaining positives (debt-free balance sheet, receivable days ~33d, promoter pref purchase) are already appropriately caveated (item 8 UNKNOWN quarterly; item 14 now AMBER; net-cash confirmed). No further graft required.

---

## VERDICT

**COMPLETE.** loop_back_to: "" (none blocking).

The two loop-1 defects are correctly fixed on the primary document and the three bear counters are grafted with accurate figures, all independently recomputed from the extracts. Coverage remains full, the 3-of-4 binary-test fail is intact, every AMBIGUOUS/FORWARD-SIGNAL finding still carries a management question, and Role 5 N.A. is legitimate. One non-blocking cite-hygiene correction is recommended (Step 3 L151 and item 5 L242: replace the store-count anchor **U113** — the FY26-revenue text box — with **U85** for 135 POS and **U53**/U112 for the 126 base); the +9-net figure is correct regardless. This does not gate the Notion save.

```yaml
stage: A5-adversary
company: "GARGI"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
notes: "Loop-2 re-audit: both loop-1 defects resolved (non-EBO YoY now -6.34% off prior base; store adds +9 net, ~4-closures inference removed, item #5 GREEN) and all three bear counters grafted correctly (PAT-margin OI-normalised ~15.05%; gross margin +154bps YoY vs -389bps QoQ / below FY26 42.93%; pref item #14 GREEN->AMBER at ~-35%). One non-blocking cite fix recommended: review L151/L242 anchor +9-net to U113 (FY26-revenue text box) — should be U85 (135 POS) + U53/U112 (126 base); figure itself verified correct."
```
