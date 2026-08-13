# A5 ADVERSARY / COMPLETENESS AUDIT — DSSL Q1 FY27
Auditor: A5 (Opus 4.8). Inputs seen: A4 review, A1 extract, A2 ledger only. All numbers below independently re-derived from the corrected page-5 block (extract lines 465-493 Rs crore / 431-461 Rs lakh) and the page-6 segment table (lines 358-389). A4's cites were checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present at review lines 398-424, all four parts non-empty and provenance-labelled:

| Part | Location | Present | Note |
|---|---|---|---|
| Summary narrative | ln 400-412 | PRESENT | ~11 lines + explicit provenance line (filing vs Notion/prior) |
| Sector intelligence | ln 414-416 | PRESENT | RBI/NPCI/order-book labelled Notion; revenue −4.6% labelled filing |
| Business-model intelligence | ln 418-420 | PRESENT | DaaS/as-a-service, dep/finance step-up, TWAS decline, all sourced |
| Competition intelligence | ln 422-424 | PRESENT | peer/moat labelled Notion; margin-from-mix caveat from filing |

Gate 0: PASS.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

Fresh grep/sweep over the extract, diffed against the A2 count test.

| Category | A2 count | My fresh count | Source lines | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 5 | 5 | 315-331 (1,2},3,4,5 — note 2 is `2}`) | none | MATCH |
| agenda_items | 2 | 2 | 38-41 (results approval; interim dividend) | none | MATCH |
| auditor_paras | 11 | 11 | STD 86-106 (3); CON 137-198 (8, incl unnumbered SEBI addendum + closing; page-4 letterhead 166-169 excluded) | none | MATCH |
| entities | 3 | 3 | 173-175 (parent + PTE + Cybercons) | none | MATCH |
| line_items | 36 | 36 | page-5 combined statement | none | MATCH |
| segment_rows | 13 | 13 | 369-389 | none | MATCH |
| signature_blocks | 5 | 5 | 54-63, 111-121, 201-211, 333-343, 394-396 | none | MATCH |

Orphan-row test (ledger row present, absent from A4): every category is either cited in A4 or explicitly carried under the review's line-14 "All reviewed. No ledger row is unreviewed." Specific coverage confirmed: all 5 notes (Step 0D table), both agenda items (results + Note 3 dividend/monitorables), auditor opinion + Other Matter + both UDINs (Step 0D, 0.51), all 3 entities (F1-01 PTE, F2-01 Cybercons, parent), all 36 line items (Step 1A/1B), all 13 segment rows incl the segment-assets non-disclosure (Step 3 ln185; TWAS Step 6D), 5 signatures reviewed-no-finding.

Missing-from-ledger test (my fresh pass found a unit the ledger lacks): none. My independent counts equal the ledger on every category.

COVERAGE: PASS. No orphan rows (→ A3 clean), nothing missing from ledger (→ A2 clean).

---

## AUDIT 2 — ARITHMETIC (recomputed from corrected page-5 block; every A4 derived cell)

Base CON/STD Rs-crore rows in A4 Step 1A/1B tie cell-for-cell to extract lines 465-491. Derived metrics recomputed:

| Metric | Basis | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|---|
| Op EBITDA (PBT+Dep+Fin−OI) Q1FY27 | CON | 40.1886 | 26.4519+8.0892+7.204−1.5565 = 40.1886 | 475,472,471,466 | OK |
| Op EBITDA Q1FY26 | CON | 31.7795 | 31.7795 | 475,472,471,466 | OK |
| Op EBITDA margin Q1FY27 | CON | 12.81% | 40.1886/313.6883 = 12.81% | 465 | OK |
| Op EBITDA margin Q1FY26 | CON | 9.66% | 31.7795/328.8517 = 9.66% | 465 | OK |
| Op EBITDA Q1FY27 | STD | 39.9256 | 26.1889+8.0892+7.204−1.5565 = 39.9256 | 475,472,471,466 | OK |
| Op EBITDA margin Q1FY27 | STD | 12.83% | 39.9256/311.1933 = 12.83% | 465 | OK |
| Op EBITDA margin Q4FY26 | STD | 9.04% | 36.3715/402.1238 = 9.04% | — | OK |
| Reported EBITDA margin Q1FY27 | CON | 13.31% | 41.7451/313.6883 = 13.31% | — | OK |
| Core PBT ex-OI Q1FY27 | CON | 24.8954 | 26.4519−1.5565 = 24.8954 | 475,466 | OK |
| Core PBT ex-OI Q1FY26 | CON | 25.3613 | 26.2809−0.9196 = 25.3613 | 475,466 | OK |
| Core PBT ex-OI Q1FY27 | STD | 24.6324 | 26.1889−1.5565 = 24.6324 | 475,466 | OK |
| ETR Q1FY27 | CON | 25.16% | 6.6564/26.4519 = 25.16% | 476,475 | OK |
| ETR FY26 | CON | 25.55% | 29.1089/113.9213 = 25.55% | 476,475 | OK |
| PAT margin Q1FY27 | CON | 6.31% | 19.7955/313.6883 = 6.31% | 477,465 | OK |
| FY26 Op EBITDA margin | CON | 10.25% | 145.9284/1424.2834 = 10.25% | — | OK (ties Notion baseline) |
| **YoY Revenue** | CON | −4.61% | (313.6883−328.8517)/328.8517 = −4.61% | 465 | OK |
| YoY Revenue | STD | −5.32% | (311.1933−328.6926)/328.6926 = −5.32% | 465 | OK |
| YoY Op EBITDA | CON | +26.46% | 8.4091/31.7795 = +26.46% | — | OK |
| YoY Op EBITDA margin | CON | +315 bps | 12.812−9.664 = +3.15pp | — | OK |
| YoY Depreciation | CON | +447.8% / ×5.48 | 6.6125/1.4767 = +447.8%; 8.0892/1.4767 = 5.48× | 472 | OK |
| YoY Finance | CON | +45.8% | 2.2625/4.9415 = +45.8% | 471 | OK |
| YoY EBIT(operating) | CON | +5.93% | (32.0994−30.3028)/30.3028 = +5.93% | — | OK |
| YoY Other Income | CON | +69.3% | 0.6369/0.9196 = +69.3% | 466 | OK |
| **YoY Core Operating PBT** | CON | −1.84% | −0.4659/25.3613 = −1.84% | — | OK |
| YoY Core Operating PBT | STD | −2.71% | −0.6859/25.3183 = −2.71% | — | OK |
| YoY Reported PBT | CON | +0.65% | 0.171/26.2809 = +0.65% | 475 | OK |
| YoY PAT | CON | +0.77% | 0.1504/19.6451 = +0.77% | 477 | OK |
| YoY PAT | STD | −0.25% | −0.0483/19.6117 = −0.25% | 477 | OK |
| Gross (mat+inv) % rev Q1FY26 | CON | 85.90% | 282.4946/328.8517 = 85.90% | 468,469 | OK |
| Gross (mat+inv) % rev Q1FY27 | CON | 80.62% | 252.9084/313.6883 = 80.62% (−528 bps) | 468,469 | OK |
| S-vs-C PAT gap Q1FY27 | — | +0.2321 (+1.19%) | 19.7955−19.5634 = 0.2321; /19.5634 = +1.19% | 477 | OK |
| S-vs-C PAT gap Q4FY26 | — | −0.1388 (−0.73%) | 18.9903−19.1291 = −0.1388; /19.1291 = −0.73% | 477 | OK |
| S-vs-C PAT gap Q1FY26 | — | +0.0334 (+0.17%) | 19.6451−19.6117 = 0.0334 | 477 | OK |
| PAT bridge sum | CON | +0.1504 | −15.1634+29.5862−2.6727−3.3410−2.2625−6.6125+0.6369−0.0206 = +0.1504 | 465-477 | OK |
| TWAS revenue YoY | seg | −20.7% | (307.77−387.93)/387.93 = −20.66% | 370 (both cols present) | OK |

**Flagged casting cell (F14-01) verified independently:** CON Q1FY26 "TCI attrib to Shareholders" filed 1,966.53 lakh. PAT-Shareholders 1,961.74 + OCI-Shareholders (−4.79) = 1,956.95 → filed exceeds tie by 1,966.53 − 1,956.95 = **9.58 lakh**. Cross-check: 1,966.53 + NCI 2.77 = 1,969.30 vs page's own TCI total 1,959.72 → same 9.58 lakh gap; TCI total itself ties (1,964.51 − 4.79 = 1,959.72). A4's characterisation (isolated single-cell error on a restated comparative, not silently corrected, routed to F14-01/Q7) reproduces exactly. Extract lines 457/489, 494-511.

ARITHMETIC: PASS. Zero mismatches above rounding across the entire headline table, both books, YoY deltas, PAT bridge, S-vs-C gap and the casting cell.

Non-failing observations (framing, not error — logged, no loop-back):
1. Reported CON basic EPS 15.54 reconciles to **total** PAT (19.7955/1.27371 = 15.54), not owner-attributable PAT (19.7349/1.27371 = 15.49). This is the filing's EPS basis; A4 carried filed EPS verbatim, so no A4 arithmetic error.
2. A4's S-vs-C gap uses total-PAT (0.2321, incl NCI) rather than owner-attributable (CON-shareholders − STD = 0.1715). A4's choice is internally consistent because it explicitly ties the gap to the Other-Matter aggregate subsidiary PAT of 0.2322 cr; defensible, disclosed, not a discrepancy.

---

## AUDIT 3 — ADVERSARIAL READ

### 3a. Rule / house-limit compliance checks (all pass)
- **Every FORWARD-SIGNAL/AMBIGUOUS finding → a management question.** A3-tagged F1-01, F2-01, F3-01, F6-01, F12-01 (plus F10-01, F14-01) each map to a Step-8.5 row: F3-01→Q1, F6-01→Q3+Q4, F12-01→Q4, F2-01→Q5, F10-01→Q6, F14-01→Q7, F1-01→Q8, receivables-gap→Q2. **8 rows, every FS/AMB finding covered.** Rule HOLDS.
- **No UNKNOWN monitorable silently upgraded.** Step 6B leaves monitorables 2, 3, 4, and the leverage half of 5 UNKNOWN/cannot-clear, and monitorable-6 RPT balances UNKNOWN; Step 8 keeps the receivables leg unverifiable. Only monitorable 1 (margin) reads GREEN, which is supported. No upgrade.
- **INDETERMINATE cash conversion did NOT resolve to PROCEED.** Verdict = PROCEED WITH CAVEATS, explicitly capped by the INDETERMINATE cash-conversion with named missing evidence (CFO, receivables ageing, ECL, net debt, PPE/CWIP). Compliant with the house rule.
- **Decision Status not re-rated on company quality.** Stays WATCHLIST / BUY ON DIPS; no thesis-broken trigger fired; buy gate correctly held half-open (margin GREEN, receivables uncleared). Compliant.

### 3b. Three most-positive claims — strongest bear counter from the same extract

| # | A4 positive claim | Strongest bear counter (from extract) | Survives? |
|---|---|---|---|
| 1 | Margin leg GREEN: op EBITDA margin 12.81% clears ≥11%; "on the margin test alone this quarter passed" (ln 335, 404) | The +315 bps is NOT operating leverage: materials+inventory fell 528 bps (driven by the Changes-in-Inventories swing +40.24cr→−3.61cr, lines 469), while employee+other opex WORSENED ~213 bps; the gain is mix/procurement + fixed-asset absorption, and it did NOT reach PBT (core PBT −1.84%). | Already grafted — Step 2 diag 3/5, Step 8B, brief. Not surviving-new. |
| 2 | Op EBITDA +26.46% YoY "expanded materially" (ln 134) | Below the EBITDA line the gain evaporates: EBIT(operating) only +5.93%, core operating PBT −1.84% CON / −2.71% STD; dep ×5.48 (+6.61cr) and finance +45.8% (+2.26cr) consume the entire lift on flat revenue (−4.6%). | Already grafted — Step 2 diag 3/5, Step 4. Not surviving-new. |
| 3 | Consolidated PAT +0.77%, "flat print"; no thesis-broken trigger fired, margin cleared = thesis-supportive (ln 141, 295) | Standalone PAT actually FELL −0.25%; the positive consolidated print rests on a subsidiary swing (+0.2321cr, ~7× Q1FY26) plus Other Income (+0.6369) and a lower tax rate — strip Other Income and PAT drops below prior year (~19.16 vs 19.6451). The "flat" headline is non-core help dressing a soft standalone quarter. | Already grafted — Step 4 mandatory Qs, Step 4B, brief. Not surviving-new. |

All three bear counters are already incorporated in A4's review with the same numbers I re-derived. **No surviving un-grafted bear counter** → nothing must be forced into A4 before save. A4's symmetric bull/bear treatment is unusually complete.

Additional independent hunt (things A4 could have overstated/missed): checked the TWAS −20.7% comparator (real — page-6 segment Q1FY26 column 387.93, lines 370), the Q4FY26 actuarial 0.3828cr sitting in a comparative not this quarter (correct, line 478), Other-Matter aggregates 249.50/23.22 lakh (correct, lines 186-189), paid-up-capital +1.18 lakh ≈11,800 shares (correct, line 491). No overstatement found.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, provenance-labelled).
- Coverage: PASS (7/7 categories match my fresh count; no orphan rows; nothing missing from ledger).
- Arithmetic: PASS (every derived cell, both books, all YoY deltas, PAT bridge, S-vs-C gap and the 9.58-lakh casting cell reproduce exactly).
- Adversarial: PASS (FS/AMB→question rule holds across 8 rows; INDETERMINATE capped at CAVEATS; no UNKNOWN upgraded; Decision Status not re-rated; three positive claims' bear counters already incorporated).

Only COMPLETE proceeds to Notion save.

```yaml
stage: A5-adversary
company: "DSSL"
quarter: "Q1 FY27"
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
