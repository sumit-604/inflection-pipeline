=== FILE: gate-recommendation.md ===

PROCEED WITH FLAGS

This is the phase 1 gate decision on evidence alone. It judges the analysis and the evidence record, not a buy or sell call. All valuation dependent elements (rating, entry range, margin of safety, destination PE, hurdle) are excluded and are pending phase 3.

## How the verdict was reached

FLAG-CASH is active, which under the standard path lands at PROCEED WITH FLAGS. The cash flag resolves INDETERMINATE, and per CLAUDE.md an INDETERMINATE cash conversion never resolves silently to PROCEED and caps the verdict at PROCEED WITH CAVEATS with the missing evidence named. Overall confidence sits at 63, inside the 60 to 74 band, which downgrades any PROCEED family verdict one level. Applying the cap and then the one level band downgrade lands the verdict at PROCEED WITH FLAGS. No forced REWORK applies: no Verifier A CRITICAL, and no verifier acceptance rate below 60.

## Confidence delta

| Component | Score | Source | Note |
|---|---|---|---|
| Numerical accuracy | 93.6 | B12a | 44 of 47 numbers clean, 0 CRITICAL, 0 MAJOR, 3 MINOR |
| Red flag coverage | 63 | B12b | binding component; 12 of 19 concall red flags caught upstream, 4 MAJOR misses on cash conversion and revenue quality |
| Framework adherence | 96.7 | B12c | Gate 0 and Emerging Moat scope only; valuation component pending phase 3 |
| Peer utilisation | 92 | B12d | 11 of 12 transcripts substantive, all 4 peers contributed |
| Overall | 63 | min of available | Band 60 to 74; PROCEED family downgrades one level; not forced REWORK at or above 60 |

Weakest component: red flag coverage at 63. Verifier B logged four MAJOR misses, all directionally negative on cash and revenue quality, and all reinforcing the FLAG-CASH raised by the accounting and prospectus stages.

## Active flags

### FLAG-CASH — determination: INDETERMINATE

Evidence weighed:
- Trade receivables rose 35.7% in six months, Rs 2,809.39mn at March 2025 to Rs 3,813.86mn at September 2025, against broadly flat implied revenue (B02, Note 12 p.344-345).
- ECL allowance swung from a Rs 11.13mn net release in FY25 to a Rs 76.15mn net addition in H1 FY26 (B02, Note 45(b)(i) p.372).
- H1 FY26 reported operating cash flow was negative Rs 2,005.95mn; the operating result remained a Rs 174.59mn loss; the first half profit rested on Rs 291.09mn of other income equal to 250% of PBT (B03, Annexure III p.324; Note 30 p.353).
- FY26 adjusted FCF Rs 38 Cr is only about 24% of adjusted EBITDA Rs 156 Cr; 9M reported OCF was negative Rs 76 Cr; the positive story rests on an adjusted OCF that strips IPO and ESOP buyback cash (B12b, Feb call p.5-6; May call p.9).
- One time pre-IPO ESOP and SAR cash settlements of about Rs 1,351.78mn plus IPO effects distort H1 (B02, Finding #4 p.365-370).
- Asset light SaaS, net cash Rs 1,664 Cr, zero debt (B04; B05, Q4 FY26 call).

Rating agency working capital rationale: NOT FOUND. No credit rating PDF was provided (B00, input_gaps).

Why INDETERMINATE: receivables grew 35.7% against flat revenue, which does not fit a clean growth induced working capital build, yet the same half is heavily distorted by one time pre-IPO ESOP and SAR cash settlements and IPO effects. Growth induced deterioration and structural deterioration cannot be cleanly separated on the evidence in hand. Missing evidence that keeps this open: the credit rating rationale detail, and the full year FY26 receivables ageing schedule.

Resolving metric: reported operating cash flow, not adjusted, in the first clean quarter free of IPO and ESOP settlement cash, read against trade receivables growth versus revenue growth. It resolves toward growth induced if reported OCF turns positive with OCF to adjusted EBITDA near 0.6 while receivables growth falls back to at or below revenue growth. It resolves toward structural if reported OCF stays negative and receivables keep outpacing flat to slow revenue with continuing ECL additions.

### FLAG-GATE0 — active and legitimate

Classification AVERAGE, core 44, moat 12, grand total 56 of 160 (B01). Depressors: median ROCE negative 26.22%, negative PAT in FY24 and FY25, cumulative CFO to PAT 0.19, all inside the FY22 to FY25 pre-IPO window and tied to non cash ESOP charges and a CCPS liability classification artifact in the screener borrowings line (B01, deal_breakers; data_notes). FY26, the first clean post-IPO full year, scored Block D 20 of 20, net cash, and a return to profit; only one such clean year exists so far. Verifier C confirmed this is genuine driver attribution, not laundering, with driver years named and self limited (B12c, positive_confirmations). This flag caps nothing.

Decision sensitive note: the AVERAGE classification, rather than AVOID, rests on the C2 endpoint CAGR convention crediting a 28.18% PAT CAGR across the loss window. Scored zero, the core would fall to 39 and the classification to AVOID (B12c, B01 Block C finding).

### FLAG-PROMOTER — not active

B08 verdict is TRUSTWORTHY with zero deal breakers, so no promoter flag fires; per Section 4, FLAG-PROMOTER is reserved for CONCERN or AVOID only. The stage 3 FLAG-PROMOTER-PRELIM does not promote. The governance items carry as caveats and monitorables instead: the Vinculum Advisors related party stake purchase at Rs 25 a share versus the Rs 361 offer, lifting promoter plus group from 21.72% to 31.74% (B08, adverse_findings); the three year unremediated Rule 11(g) audit trail and books of account modification (B08); company level transfer pricing and tax disputes of Rs 1,175.07mn, 13.7% of net worth (B08; B03); board independence at the regulatory floor, 2 of 6 (B08).

## Contradicted claims and internal inconsistencies

- Peer stage found zero contradictions of Amagi's claims across the twelve transcripts covering Affle, Newgen, RateGain and Tata Elxsi; the net narrative effect is complicates, not contradicts.
- Internal inconsistency, same February 2026 earnings call: Vijay described a perpetual license that drove H1 front loading, while Baskar stated there was no such overhang, February 2026 call p.11 versus p.18. This is an intra call inconsistency, not a peer contradiction.
- Framing correction: the comparison that RateGain disclosed a customer loss and NRR decline more openly than Amagi handled its own top five renegotiation holds, but the lost client and NRR figures were first raised by analysts in the RateGain November 11 2025 call, not volunteered by management.

## Monitorables

1. Trade receivables growth versus revenue growth, each quarter, from the receivables note in results. Healthy at or below revenue growth; a red mark if receivables outpace revenue two quarters running. This is the FLAG-CASH resolver and tests credit quality and cash conversion.
2. Reported operating cash flow, not adjusted, and OCF to adjusted EBITDA, in the first quarter clear of IPO and ESOP settlement cash, from the cash flow statement. Tests whether the profit turn converts to real cash.
3. Constant currency net revenue retention, from the earnings KPI table. 126% in FY26; a red mark below 120%. Tests retention and organic growth quality after stripping FX.
4. Net logo adds and the count of $1M plus ARR customers, from the KPI annexure. Adds decelerated 67 to 29 and went net negative in Q4; tests the new business engine.
5. Top ten customer concentration and largest customer share, from the results notes. 40.2% and 14.06% at H1 FY26; a red mark above 45% or a top one customer above 15%. Tests concentration risk beneath the strongest scored moat.
6. Adjusted EBITDA margin trajectory, from earnings. About 10% in FY26; tests the operating leverage thesis toward the cited SaaS benchmark.
7. Rule 11(g) audit trail remediation, from the FY26 statutory audit report. Three years unremediated; tests whether FY26 is the first clean report and the reliability of every downstream number.
8. Deployment of the Rs 1,664 Cr cash with disclosed size discipline, or the first NEWSPULSE and marketplace revenue disclosure, from exchange filings and concalls. Tests capital allocation and optionality conversion.

## Falsification

The single most damaging next quarter print is the first clean post-IPO quarter reporting negative operating cash flow again with trade receivables still growing faster than revenue, because it would convert the INDETERMINATE cash question into structural deterioration rather than a one time IPO and ESOP distortion.

## Publish check

No publish candidate this analysis.
