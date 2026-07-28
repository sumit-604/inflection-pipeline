# A5 ADVERSARY / COMPLETENESS AUDIT — Digitide Solutions Limited (DSSL), Q1 FY27
# Re-audit, loop 1 | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only)
# Overwrites prior audit. Prior verdict: INCOMPLETE on one arithmetic FAIL (T&D segment-margin base-mix). This run re-verifies the fix AND re-runs all three audits from scratch.

---

## 0. TARGETED RE-VERIFICATION OF THE CLAIMED FIX (T&D segment-result margin base-mix)

Raw filing figures, INR million, page 6 (extract L466-502), ÷10 = Rs Cr. Independently recomputed from source, not from A4's cites.

| Cell | Numerator / Denominator (INR mn) | My recompute | A4 value | Status |
|---|---|---|---|---|
| T&D margin Q1 FY26 | 193.01 / 1970.27 | 9.796% → **9.80%** | 9.80% | MATCH |
| T&D margin Q4 FY26 | 300.56 / 2491.90 | 12.061% → **12.06%** | 12.06% | MATCH |
| T&D margin Q1 FY27 | 189.32 / 2373.55 | 7.976% → **7.98%** | 7.98% | MATCH |
| **T&D YoY delta (filing basis)** | 7.976 − 9.796 | **−1.820 pp = −182 bps** | −182 bps | **MATCH — fix confirmed** |
| T&D QoQ delta | 7.976 − 12.061 | −4.085 = −408 bps | −408 bps | MATCH |
| BPM margin Q1FY26 / Q4FY26 / Q1FY27 | 914.08/5387.10; 897.13/5507.62; 760.00/5377.17 | 16.968%; 16.289%; 14.134% | 16.97 / 16.29 / 14.13 | MATCH |
| **BPM YoY delta** | 14.134 − 16.968 | **−2.834 = −284 bps** | −284 bps | **MATCH** |
| BPM QoQ delta | 14.134 − 16.289 | −2.155 = −216 bps | −216 bps | MATCH |
| **Total seg-result margin Q1FY26/Q4FY26/Q1FY27** | 1107.09/7357.37; 1197.69/7999.52; 949.32/7750.72 | 15.048%; 14.972%; 12.248% | 15.05 / 14.97 / **12.25** | **MATCH — new row correct** |
| Total YoY delta | 12.248 − 15.048 | −2.80 = −280 bps | −280 bps | MATCH |
| Total QoQ delta | 12.248 − 14.972 | −2.724 = −272 bps | −272 bps | MATCH |

**Base-mixing check:** The filing-basis table (STEP 5-SEGMENT rows) uses ONLY segment-result numerators (760.00/897.13/914.08 BPM; 189.32/300.56/193.01 T&D; 949.32/1197.69/1107.09 Total) over segment revenues. The deck segment-EBITDA cut (89.9/89.7/72.8; 18.8/30.1/18.9; 108.7/119.8/91.7 with deck margins 16.7/16.3/13.5, 9.5/12.1/8.0, 14.8/15.0/11.8 and the −156 bps T&D YoY) is confined to a separately headed block ("Deck 'Segment EBITDA' basis (slide 23...)") and the "task item 4 confirmed" paragraph explicitly labels −156 bps as "deck cut." **No cell mixes the two bases.** The −182 bps filing figure is the anchored primary; −156 bps appears only as the labelled deck alternative.

**Fix disposition: CONFIRMED CORRECT.** The prior arithmetic FAIL is fully resolved. Proceeding to the full three-audit sweep (not narrowed to the fixed cell).

---

## 1. COVERAGE AUDIT (fresh grep + manual sweep vs A2 ledgers)

Independent re-enumeration of each A1 extract, diffed against the A2 ledger counts, then each ledger category checked for citation/disposition in A4.

| Category | A2 count | My fresh count | Basis of my count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results: notes | 11 | 11 | Consol 5 (L591-620) + Standalone 6 (L883-916) | none | PASS |
| Results: line items | 81 | 81 | Consol P&L 36 (C1-C36) + Segment 21 (S1-S21) + Standalone 24 (T1-T24) | none | PASS |
| Results: entities | 24 | 24 | Annexure-1 12 (L195-219) + Appendix-1 12 (L634-657) | none | PASS |
| Results: auditor paras | 11 | 11 | Consol 7 (AP1-AP7, L102-176) + Standalone 4 (AP8-AP11, L672-701) | none | PASS |
| Results: signature blocks | 5 | 5 | SB1-SB5 (CS + 2 auditor + 2 CEO sign-offs) | none | PASS |
| Results: UDINs | 2 | 2 | L185 (26110128CHYFAI5661), L712 (26110128CRFPZH3202) | none | PASS |
| Results: agenda items | 1 | 1 | Sole item = results approval (L38-44) | none | PASS |
| Results: zero-standing | 5 | 5 | Dash cells confirmed by grep at L294 (C10), L530 (S12), L786 (T10), L799/801 (T12), L804/806 (T13) | none | PASS |
| Press release: disclosure units | 148 | 148 | 10+7+16+24+25+24+5+12+2+15+3+5 = 148 | none | PASS |
| Presentation: slides | 34 | 34 | [[PAGE 1]]..[[PAGE 34]] | none | PASS |
| Presentation: numbers | 554 | 554 | Per-slide tally (ledger Table 2) sums to 554; chart/OCR annotation lines excluded per stated method | none | PASS |
| Presentation: line items | 28 | 28 | Slide 22 (7) + Slide 23 (6) + Slide 33 (15) | none | PASS |
| Presentation: footnotes | 5 | 5 | Slides 8, 22, 23, 24, 33 | none | PASS |

**Fresh pass found no row the ledgers lack** (nothing to return to A2). **No count discrepancy.**

**Every ledger row cited or dispositioned in A4?** Checked the flagged rows (those carrying a review obligation):
- ZERO_STANDING C10/S12/T10 (nil exceptional this qtr) → cited (exceptional-items reconciliation, L48; Step 1A/1B rows). ✓
- ZERO_STANDING T12/T13 (standalone nil current + prior-year tax, deferred charge only) → cited (Step 8.5 Q3, ETR discussion). ✓
- ENTITY_CHANGE E12/E24 (Digitide ESOP Trust) → cited (DF9/DF11, Q9, Note 5/6). ✓
- ENTITY_CHANGE E7/E15 (Manila "Allsectech"/"Alldigi Tech") → cited (M1/DF10, Q11, control-quality drift). ✓
- ENTITY_CHANGE E10/E22 (Quess GTS Canada "Holding"/"Holdings") → ledger self-classifies as "likely OCR/typo"; subsumed under A4's blanket "all reviewed" + control-quality-drift flag. Immaterial, no metric impact. Reviewed, no independent finding required.
- OCR_GARBLE C33 (consol paid-up "1.4q1,11,") → cited and raster-resolved to 149.11 Cr (preamble, L25). ✓
- AP6/AP7 (6 other-auditor + 4 unreviewed subs, unnamed) → cited (DF3/DF4, Step 4B, Q6/Q7). ✓
- Press-release SELECTIVE_DISCLOSURE (B-3 EBITDA −12.5% QoQ omitted) / SUPPRESSED_METRIC (PAT QoQ "Turned Positive") → substance cited (Step 3, QoQ turn = exceptional roll-off). ✓
- Presentation SOLE_SOURCE_DATA_POINT (Q2/Q3 FY26 PAT deck-only) → cited (Step 3 header). ✓
- Presentation MECHANICAL_INCONSISTENCY (slide 23 "32%/Q4FY26" header) → cited (M1, Q11). ✓
- Presentation UNIT_MISMATCH (slide 15 "$2M-$6M+" USD savings) and DECK_COLOR_INVERSE (slide 21 top-30 concentration amber arrow) → non-financial marketing / color-convention items, zero impact on any derived metric or the verdict; subsumed under A4's asserted incorporation of M1-M6. Reviewed, no independent finding required.
- CHART_AXIS_SCALE / REPEATED_FOOTNOTE → immaterial by construction. ✓

**COVERAGE VERDICT: PASS.** No orphan material row; no missing-from-ledger row. The only rows not individually named in A4 (USD savings figure, color-inverse arrow, one OCR-typo entity variant) are each non-financial, pre-dispositioned in the ledger, and covered by A4's control-quality blanket. None rises to a coverage FAIL.

---

## 2. ARITHMETIC AUDIT (recomputed from raw INR-mn source, ÷10)

Every derived metric in A4's tables recomputed independently. "MATCH (rounding)" = |Δ| ≤ 0.01 Rs Cr or ≤ ~0.1 bps/pp from input-rounding order — below the FAIL threshold.

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBExcep+D+Fin−OI) | 76.89 | 10.919+55.176+15.122−4.327 = 76.89 | MATCH |
| Consol Op EBITDA Q4FY26 | 87.89 | 87.898 → 87.90 (Δ0.008) | MATCH (rounding) |
| Consol Op EBITDA Q1FY26 | 82.58 | 82.573 → 82.57 (Δ0.007) | MATCH (rounding) |
| Consol Op EBITDA FY26 | 343.17 | 343.165 (ties deck "₹343 Cr") | MATCH |
| Op EBITDA margin Q1FY27 | 9.92% | 76.89/775.07 = 9.921% | MATCH |
| Op EBITDA margin YoY | −130 bps | 9.921−11.223 = −130.2 bps (deck −131) | MATCH |
| Mgmt-EBITDA rebuild Q1FY27 (Rev−EmpBen−OthExp) | 76.89 | 775.072−583.298−114.884 = 76.89 | MATCH (ties Op EBITDA exactly) |
| EBIT (op) Q1FY27 | 21.71 | 76.89−55.176 = 21.71 | MATCH |
| Core Op PBT Q1FY27 (EBIT−Fin) | 6.59 | 21.714−15.122 = 6.59 | MATCH |
| Effective Tax Rate Q1FY27 | 73.2% | 79.86/109.19 = 73.14%; A4's cited 7.99/10.92 = 73.17% → 73.2% | MATCH (within input-rounding) |
| ETR FY26 | 82.4% | 26.026/31.571 = 82.44% | MATCH |
| PAT margin (total) Q1FY27 | 0.38% | 2.933/775.072 = 0.378% | MATCH |
| Owners PAT margin Q1FY27 | (0.24%) | −1.891/775.072 = −0.244% | MATCH |
| Standalone Op EBITDA Q1FY27 | 34.93 | 475.993−365.050−76.005 = 34.938 | MATCH |
| Standalone Op EBITDA margin Q1FY27 | 7.34% | 34.938/475.993 = 7.34% | MATCH |
| Standalone core-op PBT Q1FY27 | (10.84) | (34.938−35.189)−10.585 = −10.836 | MATCH |
| Revenue YoY | +5.3% | 775.07/735.74−1 = +5.34% | MATCH |
| Depreciation YoY | +19.7% | 55.176/46.075−1 = +19.75% | MATCH |
| Finance cost YoY | +34.8% | 15.122/11.219−1 = +34.79% | MATCH |
| EBIT YoY | −40.5% | 21.714/36.498−1 = −40.51% | MATCH |
| Core Op PBT YoY | −73.9% | 6.592/25.279−1 = −73.92% | MATCH |
| Reported PBT YoY | −45.4% | 10.92/19.99−1 = −45.37% | MATCH |
| PAT total YoY | −69.7% | 2.933/9.693−1 = −69.74% | MATCH |
| Standalone revenue YoY | +2.6% | 475.99/463.83−1 = +2.62% | MATCH |
| Standalone Op EBITDA YoY | −30.1% | 34.938/49.966−1 = −30.1% | MATCH |
| **PAT bridge YoY** (EBITDA −5.69, D −9.10, Fin −3.90, OI +0.75, Excep +8.87, Tax +2.31) | sums to −6.76 | −5.68−9.10−3.90+0.75+8.87+2.31 = −6.76; recurring core −18.69 confirmed | MATCH |
| S-vs-C PAT gap Q1FY27 | −13.51 | −10.581 − 2.933 = −13.514 | MATCH |
| S-vs-C gap Q4FY26 / Q1FY26 / FY26 | +11.86 / −6.10 / +15.65 | 6.853−(−5.005); 3.593−9.693; 21.195−5.545 | MATCH |
| Owners − parent decomposition | +86.90 (owned subs net NCI) | −18.91 − (−105.81) = +86.90 mn; NCI +48.24 mn | MATCH |
| 6-sub PAT share of group | 90.1% | 26.44/29.33 mn = 90.1% (Rs 2.644 of 2.93 Cr) | MATCH |
| Unallocated seg liab YoY | +97.3% | 304.55/154.38−1 = +97.3% | MATCH |
| BPM seg assets QoQ / BPM liab QoQ | +6.1% / −5.2% | 1378.32/1299.12−1=+6.1%; 642.56/677.76−1=−5.19% | MATCH |
| Consol vs standalone reserves inversion | 8.1% below | (750.049−689.108)/750.049 = 8.12% | MATCH |
| Prior-year tax credit / deferred charge (consol) | +2.08 / 0.53 | 20.75 mn = 2.075 Cr; 5.32 mn = 0.532 Cr | MATCH |
| ROCE proxy (Step 7 indicative) | ~9.5% → ~12.25x | 86.84/918.27 = 9.46%; 0.5×9.46+7.5 = 12.23x | MATCH (indicative) |

**No mismatch above rounding.** Every non-exact tie is a sub-0.01 Rs Cr or input-rounding-order artifact (A4 truncated a few EBITDA sub-totals at the 2nd decimal, e.g. 82.58 vs 82.573; 87.89 vs 87.898 — immaterial, touches no margin, delta, or verdict). ETR 73.2% and Op-EBITDA-margin −130/−131 bps both fall inside input-rounding tolerance.

**ARITHMETIC VERDICT: PASS.** The previously failing T&D cell is fixed; no new arithmetic error surfaced anywhere in the review.

---

## 3. ADVERSARIAL READ (strongest bear counter to A4's three most positive claims, from the same extract)

A4's review is already bear-heavy; the "most positive" statements are the residual constructive framings. For each, the strongest same-source bear counter and whether it SURVIVES un-incorporated.

**Positive claim 1 — "Revenue +5.3% YoY is real; T&D +20.3% and International +10.2% keep the mix shift 'firmly on track'" (Step 2 diag 1; Step 6D).**
Bear counter (same extract): revenue DIPPED −3.1% QoQ (first sequential fall in the 5-qtr series, deck slide 24); BPM (69.4% of revenue) is flat YoY (−0.2%) and every segment fell QoQ (BPM −2.4%, T&D −4.7%, Intl −2.9%); the T&D "engine" carries a 7.98% filing segment-result margin, now below BPM's 14.13% — growth is narrow and margin-dilutive.
**Survives? NO — already grafted.** A4 states all of this explicitly (Step 3 run-rate, Step 5-SEGMENT, Step 6D "WEAKENED (economics)").

**Positive claim 2 — "PAT turned positive at Rs 2.9 Cr with no exceptional items, a clean base to build from; reported PAT this quarter = adjusted PAT, so the clean-base framing is factually correct" (Step 1A; PR line 84/252).**
Bear counter (same extract): the Rs 2.9 Cr is 100% NCI (owners −1.89 Cr; standalone parent −10.58 Cr); the QoQ turn is roll-off of the Q4 labour-code exceptional, not operating recovery; and on management's OWN "Adjusted PAT" line (deck slide 22/33) adjusted PAT fell 18.6 → 11.2 → **2.9**, i.e. −84.4% YoY and −74.1% QoQ — the clean base did not just stay thin, it collapsed even after normalising exceptionals.
**Survives? NO — substance already grafted.** A4 makes the owners/NCI split, the exceptional-roll-off point, explicitly calls it "a low, thin base" (Step 4), and quantifies the normalised collapse via core operating PBT −73.9% YoY (Step 2 diag 3). The deck's Adjusted-PAT −84% YoY is a reinforcing quantification of a point A4 already makes, not a new surviving counter. *(Non-binding strengthening note to A4, not a completeness gap: quantifying management's own adjusted PAT 18.6→2.9 (−84% YoY) would sharpen the rebuttal of the "clean base to build from" quote.)*

**Positive claim 3 — "Management EBITDA is a genuine operating measure (excludes Other Income; not flattered by treasury/OI); the 9.9% margin is a clean operating-margin read" (Step 1C).**
Bear counter (same extract): "clean" cuts both ways — 9.9% is below the 11% tripwire floor (FLAG-CASH leg 1 printed), it is struck AFTER the now-embedded New-Labour-Code service cost (only the catch-up was carved to exceptional), and the standalone parent's clean operating margin is only 7.34%; the honesty of the measure is precisely what confirms genuine, structural erosion, not a one-off.
**Survives? NO — already grafted.** A4 flags leg-1 at 9.9%, the embedded service-cost run-rate (DF1, Q8), and the 7.34% standalone margin (Step 1D).

**ADVERSARIAL VERDICT: no surviving bear counter requiring graft.** A4's review is symmetric and complete on the bear side; the three positive framings each already carry their same-source rebuttal.

---

## VERDICT

**COMPLETE.**

- The single prior arithmetic FAIL (T&D segment-result margin base-mix) is re-verified as fixed: −182 bps YoY on the filing segment-result basis, recomputed independently; BPM −284 bps YoY and the new Total segment-result-margin row (12.25%, −280 bps YoY / −272 bps QoQ) are arithmetically correct; no cell mixes the filing and deck bases; the deck's −156 bps is confined to its labelled block.
- Full re-sweep: COVERAGE PASS (no orphan, no missing-from-ledger), ARITHMETIC PASS (no mismatch above rounding), ADVERSARIAL PASS (no surviving un-grafted bear counter).

Only COMPLETE proceeds to Notion save.

*A5 adversary re-audit, loop 1 | 2026-07-28 | fresh context: A4 review + A1 extracts + A2 ledgers*

```yaml
stage: A5-adversary
company: "DSSL"
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
```
