# A5 ADVERSARY / COMPLETENESS AUDIT — TATVA CHINTAN PHARMA CHEM LIMITED (TATVA), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (saw only A4 review, A1 extracts, A2 ledgers).
Re-derived independently. Units: Rs Mn x 0.1 = Rs Cr.

---

## AUDIT 1 — COVERAGE

Fresh grep/sweep pass over each A1 extract, diffed against the A2 ledgers.

### Results extract

| Category | A2 count | My fresh count | Orphan rows / notes | Status |
|---|---|---|---|---|
| Numbered notes | 13 (7 consol L359-390 + 6 standalone L538-560) | 13 | none | PASS |
| Financial-table line items | 65 (38 consol + 27 standalone) | 65 | none | PASS |
| Zero-standing items | 6 (3 NCI + 2 other-equity + 1 std purchases) | 6 | none | PASS |
| Board-outcome agenda items | 6 (L36-74) | 6 | none | PASS |
| Annexure Sr-rows | 12 (5 director + 7 capacity) | 12 | none | PASS |
| Auditor paragraphs | 10 (6 consol + 4 standalone) | 10 | none | PASS |
| Consolidation entities | 3 (L228-230) | 3 | none | PASS |
| Signature blocks | 5 | 5 | none | PASS |

### Presentation extract

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 36 ([page N] L15..1596) | 36 | none | PASS |
| Numeric tokens | 1,427 | 1,427 (per-page sums reconcile) | none | PASS |
| Reference line items | 64 (7+19+22+16 on slides 6/9/10/34) | 64 | none | PASS |
| Footnotes | 6 | 6 | none | PASS |
| Zero-standing | 2 (P&L exceptional; BS LT-borrowings FY25 dash) | 2 | none | PASS |

### Ledger-row -> A4 citation check
Every material flagged row is either cited or defensibly reviewed-no-finding:
- ONE_TIME_ITEM (exceptional, consol+std L301/L499): cited — Step 0D, Step 3, Step 4, Q5. PASS.
- CURRENT_PERIOD_ZERO (std current tax nil, L502): cited — Step 4, Q6, F8-a. PASS.
- ZERO_STANDING x6: NCI nil (wholly-owned, "Owners of parent" = full PAT, Step 4), std purchases-of-stock nil (Step 1B), other-equity annual-only. Reviewed. PASS.
- AGENDA_SUBJECT_TO_AGM x3 / BORROWING_LIMIT_3X: cited — Q7, Q9, F6-b, monitorables. PASS.
- Deck slides 20/22/23/34: SDA revenue (slide 20) and capacity 791 KL (slide 22) and shareholding/CMP (slide 34) all cited. **Slide 23 R&D-spend decline (128.39 -> 78.32 Mn FY25->FY26; Q1FY27 only 21.5) is not individually surfaced** — folded under A4's blanket "all 36 slides reviewed" and A3-03 (CFC/R&D-since-2018). Low materiality; reviewed-no-finding accepted, not an orphan.
- EXPERIENCE_YEARS_INCONSISTENCY (Patel 31 yrs vs 30, same 1996 join): not surfaced by A4, but the director rows themselves are reviewed (Q9); trivial. Not an orphan.

**COVERAGE VERDICT: PASS.** No orphan rows; no row my fresh pass found that the ledger lacks. Both ledger COUNT TESTs reproduce exactly.

---

## AUDIT 2 — ARITHMETIC

Every derived metric recomputed from raw Rs-Mn source lines. "src" = filing extract line unless noted.

### Step 1 raw-to-Cr conversion (spot of full sweep)
All 20 consolidated and 20 standalone line items x 4 periods reconcile to A4's Cr figures within rounding. No exceptions.

### Consolidated derived (1C) and YoY/QoQ (Steps 2-4)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBTbe+D+Fin-OI) | 32.30 | 22.429+10.566+2.081-2.780 = 32.30 | L300/296/295/287 | PASS |
| Op EBITDA Q1FY26 | 17.33 | 9.101+8.971+0.413-1.155 = 17.33 | L300/296/295/287 | PASS |
| Op EBITDA Q4FY26 | 28.13 | 16.587+9.755+1.438+0.348 = 28.13 | same | PASS |
| Op EBITDA margin Q1FY27 | 19.3% | 32.30/167.06 = 19.33% | — | PASS |
| Op EBITDA margin Q1FY26 | 14.8% | 17.33/116.86 = 14.83% | — | PASS |
| Effective tax rate Q1FY27 | 24.3% | 5.130/21.111 = 24.30% | L306/302 | PASS |
| Effective tax rate Q4FY26 | 37.8% | 6.266/16.587 = 37.78% | same | PASS |
| Core PBT ex-OI Q1FY27 | 18.33 | 21.111-2.780 = 18.33 | L302/287 | PASS |
| Revenue YoY | +42.9% | 50.19/116.86 = +42.96% | L286 | PASS |
| Op EBITDA YoY | +86.3% | 14.964/17.332 = +86.34% | — | PASS |
| Op EBITDA margin YoY | +448 bps | 19.333-14.831 = +450 bps | — | PASS (2 bp, rounding) |
| Finance cost YoY | +403.9% | 1.668/0.413 = +403.9% | L295 | PASS |
| Other income YoY | +140.7% | 1.625/1.155 = +140.7% | L287 | PASS |
| Core PBT ex-OI YoY | +130.7% | 10.385/7.946 = +130.7% | — | PASS |
| Reported PBT YoY | +132.0% | 12.010/9.101 = +132.0% | L302 | PASS |
| PAT YoY | +140.3% | 9.330/6.651 = +140.3% | L307 | PASS |
| Revenue QoQ | +24.5% | 32.911/134.144 = +24.5% | L286 | PASS |
| Op EBITDA margin QoQ | -163 bps | 19.333-20.969 = -164 bps | — | PASS (1 bp, rounding) |
| PAT bridge sum | +9.33 | 14.964-1.595-1.668+1.625-1.318-2.680 = +9.33 | — | PASS (ties) |

### Standalone derived (1D)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA margin Q1FY27 | 16.4% | 24.03/146.70 = 16.38% | L498/495/494/485/484 | PASS |
| Op EBITDA margin Q4FY26 | 20.0% | 26.54/132.67 = 20.00% | same | PASS |
| Core PBT ex-OI Q1FY27 | 10.06 | 14.094-4.033 = 10.06 | L500/485 | PASS |
| Core PBT ex-OI Q4FY26 | 15.34 | 14.975+0.369 = 15.34 | same | PASS |
| Effective tax rate Q1FY27 | 25.9% | 3.648/14.094 = 25.88% | L504/500 | PASS |
| OI / PBT Q1FY27 | 28.6% | 4.033/14.094 = 28.61% | L485/500 | PASS |

### Standalone-vs-consolidated gap / subsidiary share (Step 4, consol - standalone)

| Period | Metric | A4 value | Recomputed | Status |
|---|---|---|---|---|
| Q1FY27 | Subsidiary revenue | 20.35 | 167.055-146.702 = 20.35 | PASS |
| Q1FY27 | Subsidiary PAT | 5.54 | 15.981-10.446 = 5.535 -> 5.54 | PASS |
| Q1FY27 | Subsidiary % of consol PAT | 34.6% | 5.535/15.981 = 34.63% | PASS |
| Q4FY26 | Subsidiary % of consol PAT | 12.6% | 1.298/10.321 = 12.58% | PASS |
| Q1FY26 | Subsidiary % of consol PAT | 22.8% | 1.518/6.651 = 22.82% | PASS |
| FY26 | Subsidiary % of consol PAT | 7.1% | 2.972/42.054 = 7.07% | PASS |
| Q1FY27 | Parent share of consol PAT | 65.4% | 10.446/15.981 = 65.36% | PASS |

### Balance-sheet reference metrics (Step 5, deck slide 10, Rs Mn -> Cr)

| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| FY26 net debt | ~111.58 | 5.01+115.36-8.79 = 111.58 | PASS |
| FY26 receivable days | ~86 | 119.03/505.86 x365 = 85.9 | PASS |
| FY26 inventory days | ~319 | 196.07/224.54 x365 = 318.7 | PASS |
| COGS (materials+purch+chg-inv) | 224.54 | 262.75+6.49-44.71 = 224.54 | PASS |
| FY26 payable days | ~95 | 58.25/224.54 x365 = 94.7 | PASS |
| SDA Q1FY27 annualised | ~231 | 57.8 x4 = 231.2 | PASS |
| Revenue annualised | ~668 | 167.06 x4 = 668.2 | PASS |

Only sub-rounding noise found (OI/PBT FY25 30.5% vs A4 30.6%; margin YoY 450 vs 448 bps; QoQ -164 vs -163 bps). All within tolerance.

**ARITHMETIC VERDICT: PASS.** No mismatch above rounding. PAT bridge ties to +9.33 Cr.

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive claims in A4, each with the strongest bear counter built only from the extract.

### Claim 1 (Step 2 YoY verdict): "a genuinely strong operating quarter — revenue +43%, operating margin +448 bps YoY, core operating PBT +131%, PAT +140%, all operationally driven."
**Bear counter:** the comparable Q1FY26 was a trough (op margin 14.8%; deck rounds to 15%), and the consolidated uplift is concentrated in the two zero-cost foreign WOS (subsidiary revenue 1.48 -> 20.35 Cr; subsidiary PAT 34.6% of consol). The manufacturing PARENT's own operating EBITDA margin is only 16.4% and its core PBT ex-OI FELL QoQ 15.34 -> 10.06 Cr (standalone L498/L485). So "operationally driven" is materially a subsidiary resale-markup story.
**Survives?** NO — already incorporated. Step 2 verdict names "the subsidiary earnings-quality concentration" as a caution; Step 1D anchor already states standalone core PBT fell QoQ while consol rose. Counter is present in A4.

### Claim 2 (Step 4 bridge): "Essentially 100%+ of the PAT growth is recurring/operational; treasury did not manufacture this beat — the single cleanest confirmation the quarter is real." (echoed Step 2 #3: "headline growth is real and operational, the single cleanest confirmation").
**Bear counter (built from extract):** subsidiary PAT grew 1.52 -> 5.54 Cr YoY = **+4.02 Cr, which is 43.1% of the total +9.33 Cr PAT growth** (consol L307 minus standalone L505). A4 itself flags that these subsidiaries carry ~zero materials/employees/depreciation and their contribution may be "a one-off inventory-in-transit markup / non-arm's-length timing" whose durability is "the top management question" (Q1). The bridge tags the entire +14.97 Cr Op EBITDA growth as "Recurring" without carving out this subsidiary portion. A4 therefore asserts simultaneously that (a) 34.6% of consol PAT is possibly-one-off and unresolved, and (b) "100%+ of PAT growth is recurring." Those cannot both stand: if the subsidiary markup is one-off, ~43% of the YoY PAT growth is NOT recurring, and the "single cleanest confirmation the quarter is real" is overstated.
**Survives?** **YES.** This is an internal contradiction, not covered elsewhere — the bridge's "Recurring" tag and the "100%+ recurring / the quarter is real" conclusion are stated unqualified. **Must be grafted into A4:** the operating-EBITDA-growth line and the bridge conclusion must be split into a parent-recurring component (~+5.3 Cr of the PAT growth) and a subsidiary component (+4.02 Cr, 43%, recurrence UNRESOLVED pending Q1/F2/F3/F4). The "100%+ recurring" / "single cleanest confirmation the quarter is real" language must be downgraded accordingly (at most ~57% is confirmably recurring at the parent this quarter).

### Claim 3 (Step 6B monitor #7): "Standalone PBT Rs 14.09 Cr (>Rs 10 Cr) GREEN; parent PAT share 65.4% (>50%) GREEN — both thresholds met."
**Bear counter:** the GREEN masks parent deterioration — parent share fell QoQ 87.4% -> 65.4%; standalone op EBITDA margin fell QoQ 20.0% -> 16.4%; standalone core PBT ex-OI fell QoQ 15.34 -> 10.06 Cr; and standalone OI (Rs 4.03 Cr) is 28.6% of standalone PBT, so the Rs 14.09 Cr parent PBT is partly Other-Income and the Rs 10.45 Cr parent PAT is flattered by NIL current tax (L502) offset by a Rs 3.65 Cr deferred charge.
**Survives?** NO — already incorporated. A4 marks monitor #7 "GREEN (both thresholds met; watch direction)", the Step 1D anchor flags the standalone QoQ core-PBT fall, and F8-a/Q6 carry the nil-current-tax point.

**ADVERSARIAL VERDICT: one surviving counter (Claim 2).** Per protocol a surviving counter must be grafted into A4 before save; unincorporated, it is a FAIL to A4.

---

## VERDICT

**INCOMPLETE.** Coverage PASS, Arithmetic PASS, but Adversarial produces one surviving bear counter that A4 has not incorporated.

- **Loop back to: A4.**
- **Exact gap:** Step 4 PAT bridge tags the full +Rs 14.97 Cr operating-EBITDA growth "Recurring" and concludes "essentially 100%+ of PAT growth is recurring / the single cleanest confirmation the quarter is real," while Step 4's own subsidiary decomposition shows +Rs 4.02 Cr (43.1% of the +Rs 9.33 Cr YoY PAT growth) comes from the two foreign zero-cost WOS whose recurrence A4 elsewhere flags as UNRESOLVED (Q1, F2/F3/F4). Graft required: split the bridge into parent-recurring (~+5.3 Cr) vs subsidiary-unresolved (+4.02 Cr, 43%) components and downgrade the "100%+ recurring / quarter is real" language to ~57% confirmably-recurring-at-parent pending the H1 subsidiary-durability answer. Arithmetic of the split is exact from consol (L307/L302/L300) minus standalone (L505) lines.

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
  - claim: "Step 4 bridge: 'essentially 100%+ of PAT growth is recurring/operational; treasury did not manufacture this beat; the single cleanest confirmation the quarter is real'"
    counter: "Subsidiary PAT grew 1.52->5.54 Cr YoY = +4.02 Cr = 43.1% of the +9.33 Cr total PAT growth, from two zero-cost foreign WOS whose recurrence A4 itself flags as UNRESOLVED (Q1/F2/F3/F4). Bridge tags full +14.97 Cr Op EBITDA growth 'Recurring' without carving out this portion; '100%+ recurring' cannot coexist with '34.6% possibly one-off'. At most ~57% is confirmably recurring at the parent this quarter."
    source_line: "consol PAT L307 (159.81 Mn) minus standalone PAT L505 (104.46 Mn) vs Q1FY26 L307 (66.51) minus L505 (51.33); bridge Step 4"
loop_back_to: "A4"
gap: "Step 4 PAT bridge overstates recurrence: +Rs 4.02 Cr (43.1% of +Rs 9.33 Cr YoY PAT growth) is subsidiary-sourced with UNRESOLVED durability, yet tagged 'Recurring' and concluded '100%+ recurring / quarter is real'. Graft parent-vs-subsidiary split and downgrade the language before save."
```
