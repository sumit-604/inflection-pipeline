# A3 FORENSIC NOTES — India Glycols Limited (INDIAGLYCO) | 2026-09 | doctype: presentation (corp)

Inputs read: A1 structured (R001-R291), A1 fulltext (1038 lines), A2 ledger.
Ledger reconciliation: 291 / 291 rows accounted for (100%). No orphan IDs.
Source PDF and inputs/ NOT opened. Prior-quarter deck: none supplied.

Entity under review: residual India Glycols (Entity A) post-demerger. The deck
is a pre-demerger COMBINED-group investor presentation carrying both the
combined group (page 7: IGL Spirits + India Glycols + Ennature) and the
standalone post-demerger India Glycols (page 31). The Clariant JV add-back is
the load-bearing forensic object.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F2 | R038/R142/R291 | slide 7 & 31, line 194/1011/1024 | "Adjusted EBITDA adds back IGL's share of the Clariant JV profits" | AMBIGUOUS | The footnote is arithmetically insufficient. p7 India Glycols EBITDA FY26 = 169; p31 "Adj. EBITDA" FY26 = 330 (same revenue base 1,164). Gap = 161 Cr. IGL's 49% JV share = 46.5 Cr (49% x 95 JV PAT, R136). Even adding back the FULL JV PAT (95) reaches only 264, not 330. At least 66-114 Cr of undisclosed add-backs sit inside "Adj. EBITDA." Headline "INR 330 Cr / 28.4% margin / strong earnings profile" rests on this. A4 to ask management for the full Adj. EBITDA bridge. |
| A2 | F6 | R229/R268/R269/R235/R234 | slide 10 & 18, line 304/499/498 | "Demerger became effective on 1st September 2026 and is expected to be concluded by [24th October 2026]" | FORWARD-SIGNAL | Dated corporate-action calendar. Conclusion 24-Oct-2026 is a near-term catalyst; residual-entity financials become reportable standalone. Aspirations dated: ₹2,000 Cr rev / ₹400 Cr EBITDA in 4-5 yrs; 10X in 10 yrs. Feeds Role 5 promise-vs-delivery tracker. |
| A3 | F7 | R236/R282/R275 | slide 18 & 6, line 524/539/204 | "in advanced discussion with partners · DEVELOPMENT-STAGE"; "no forecasts are made for them here"; footnote "(2) Excluding Clariant JV sale" | AMBIGUOUS | Block 3 (Novel Tech), one of the three 10X-vision pillars, is disclaimed as development-stage with no forecasts. Selective JV scoping: export-mix (~45%) is shown EX-JV, while Adj. EBITDA ADDS the JV back. JV is included where flattering, excluded where not. A4 to ask which headline metrics are JV-inclusive. |
| A4 | F12 | R137/R138/R139/R026 | slide 31 & 7, line 998/1006-1010 | "Strong margin expansion has more than offset revenue moderation" | CONFIRMATORY-NEGATIVE | India Glycols Net Sales fell 1,581 (FY24) -> 1,291 (FY25) -> 1,164 (FY26), down 26% over two years. Management labels it "revenue moderation." Confirms the Notion tripwire (BSPC revenue shrinking while its market grows). Bio-Glycols (tripwire) FY26 = 325 Cr / ~28,750 MT. Margin story is JV-adjusted (see A1); core top line is contracting. |
| A5 | F14 | R065/R131; R172/R175 | slide 14 & 28, line 393/929 | Gases "INR 50 Cr" (p14) vs Industrial Gases "INR 47 Cr" (p28) | NEUTRAL-FACT | Same segment, same FY26, two values (50 vs 47). "India Glycols" name reused for the pre-demerger combined-group segment (EBITDA 169) AND the standalone post-demerger listco (Adj. EBITDA 330). "IGL Spirits Ltd" vs "IGL Spirits Limited." Individually immaterial; cumulatively a drafting/governance data point. Name-reuse compounds A1. |
| A6 | F15 | R230/R172/R175/R176/R061/R062 | slide 12, line 336/343/360 | "resulting in 3 independently listed public companies" | FORWARD-SIGNAL | Structural entity change: one listco splits into IGL Spirits Ltd, India Glycols Ltd, Ennature Bio Pharma Ltd. Swap ratios 1:1 (Spirits), 1:3 (Ennature). Residual IGL perimeter re-cut (retains Bio-Specialty Materials, Sustainable & Performance Chemicals, Gases). Effective 1-Sep-2026. Re-baselines every historical comparison. |
| A7 | F16 | R038 vs R142; R291 | slide 7 vs 31, line 194/1011/1024 | p7 "EBITDA" (unlabelled) relabeled p31 "Adj. EBITDA / Margin1" | AMBIGUOUS | Intra-deck reframing: the residual entity's earnings appear on two bases in ONE deck; the flattering "Adj." basis carries the standalone headline (330 Cr, 28.4%). Cross-quarter dropped-disclosure diff NOT RUNNABLE (no prior deck baseline). A4 to obtain the prior deck for a proper reframe/drop diff next run. |

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| # | check | status | one-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | N.A. | Marketing deck, no financial-statement line-item template; ledger zero_standing count = 0. |
| F2 | Standalone vs consolidated decomposition | FINDING | JV add-back (footnote R291) fails to reconcile the 161 Cr p7-to-p31 EBITDA gap; ≥66 Cr undisclosed (A1). |
| F3 | Shell-entity detection | N.A. | No cost-line detail (CoM / employee benefits / depreciation) in a presentation. |
| F4 | Unaudited contribution ratio | N.A. | No auditor Other Matters paragraph in an investor deck. (JV dependency captured in F2.) |
| F5 | Going concern / EoM scope | N.A. | No auditor EoM and no prior quarter to verbatim-diff. |
| F6 | Forward-commitment phrase mining | FINDING | Dated commitments: demerger effective 1-Sep-2026, conclude 24-Oct-2026; ₹2,000 Cr/₹400 Cr aspiration; 10X/10Y (A2). |
| F7 | Hedge phrase mining | FINDING | Block 3 "development-stage / no forecasts"; export-mix "Excluding Clariant JV sale" selective scoping (A3). |
| F8 | Tax forensics | N.A. | No ETR, deferred-tax, or tax-line data in the deck. |
| F9 | OCI forensics | N.A. | No OCI / actuarial data in the deck. |
| F10 | Share count and dilution | N.A. | No paid-up capital or EPS; demerger swap ratios are not dilutive instruments. |
| F11 | Reserves and net-worth tie-out | N.A. | No balance sheet / other equity / net worth disclosed. |
| F12 | Segment forensics | FINDING | India Glycols segment revenue down 26% FY24-26; "revenue moderation" admitted; no segment assets/liabilities to trend (A4). |
| F13 | Board outcome beyond results | N.A. | No board-meeting outcome / AGM notice / director terms in an investor deck. |
| F14 | Note drafting inconsistencies | FINDING | Gases 50 vs 47 Cr; "India Glycols" name reused for two EBITDA scopes; Ltd/Limited variance (A5). |
| F15 | Entity list diffs | FINDING | Demerger creates 3 listed entities; residual IGL perimeter re-cut, effective 1-Sep-2026 (A6). |
| F16 | Dropped / reframed disclosures | FINDING | Intra-deck EBITDA -> "Adj. EBITDA" reframe; cross-quarter drop diff NOT RUNNABLE, no prior deck (A7). |
| F17 | Concall silence audit | N.A. | Doctype is a presentation, not a transcript. |

Statuses: 7 FINDING (F2, F6, F7, F12, F14, F15, F16); 10 N.A.; 0 blank. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Demerger became effective | 1-Sep-2026 | R268 / line 304 | completed |
| Demerger expected to be concluded | 24-Oct-2026 | R229 / R269 / line 304 | underway |
| Assets, liabilities, contracts, employees transferred to resulting companies | by conclusion (24-Oct-2026) | R227 / line 295 | underway |
| ₹2,000 Cr net revenue & ₹400 Cr EBITDA aspiration | next 4-5 years (~FY30-31) | R235 / line 499 | aspiration |
| 10X sales and profits | ten years (~FY36) | R234 / line 498 | aspiration |
| NPDI projects in performance chemicals | near- to medium-term | R220 / line 202 | intended |
| CCUS / novel catalysis / CO2 valorisation with partners | undated (DEVELOPMENT-STAGE) | R236 / line 524 | in discussion |

---

## RECONCILIATION LOG

- Ledger flags addressed: BASIS_DIFFERENCE (R032/R035/R038/R043/R044/R045 and
  R140-R145) -> F2 finding A1. FOOTNOTE_UNRESOLVED (R291) -> F2/F16. 
  DATE_SEQUENCE_NOTE (R268/R229/R269) -> F6 commitment register (effective
  1-Sep precedes concluded 24-Oct; internally consistent, no finding).
- ZERO_STANDING sweep (ledger section 7): none found; F1 N.A. confirmed.
- MISSING_FROM_STRUCTURED (ledger section 8): none; no coverage gap.
- Numeric ties verified in fulltext: p14 Bio-Specialty 546 = Bio-Glycols 325 +
  Glycol Ethers 221 (✓); p14 S&PC 474 ≈ Perf Chem 56 + Clariant JV 419 (475,
  rounding); Gases 50 (p14) vs 47 (p28) DOES NOT tie -> F14.
