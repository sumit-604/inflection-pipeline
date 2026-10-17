# A3 FORENSIC NOTES: EIMCOELECO q2fy27, doctype presentation (file tag pressrelease: media release on results)

Inputs read: A1 structured (extracted/eimcoeleco-pressrelease-q2fy27-structured.md), A1 fulltext (extracted/eimcoeleco-pressrelease-q2fy27-fulltext.md), A2 ledger (work/ledger_pressrelease_eimcoeleco_q2fy27.md). Prior-quarter fulltext: ND. Notion monitoring checklist: ND (pre-thesis read, no spear on record). Source PDF and inputs/ not opened.

## LEDGER RECONCILIATION
- Ledger rows: 92 (R001-R092). Rows read at cited fulltext line: 92. Reconciled: 100%.
- Pipeline cite defect (A1, carried into A2): R061 (Ms. Vrushali Thakkar, investor contact) is cited at page 4 line 140. Line 140 is blank. The name sits at fulltext line 160: "For further queries, please contact: Ms. Vrushali Thakkar". Value correct, line wrong. No forensic impact.
- Rounding note: H1 FY27 revenue stack 101 + 34 = 135 (lines 66, 68, 73) vs total 134 (R010). Chart values are rounded Rs crore integers. Growth % values (R013, R014, R023, R024, R033, R034) are consistent with unrounded bases, not with the rounded integers (e.g. 11/5 = +120% vs stated +108.8%). All derived figures below use margin % x revenue where possible and are marked DERIVED, accurate to about Rs 0.5 cr.
- All other line cites verified verbatim.

## DERIVED QUARTER SPLIT (H1 minus Q2; DERIVED from R004-R032)
| Metric (Rs cr) | Q1 FY26 | Q2 FY26 | Q1 FY27 | Q2 FY27 | Q1 YoY | Q2 YoY |
|---|---|---|---|---|---|---|
| Revenue | 68 | 33 | 77 | 57 | +13% | +70.9% (stated) |
| EBITDA (margin x rev) | 12.3 | 5.1 | 14.1 | 10.7 | +15% | +108.8% (stated) |
| PAT (margin x rev) | 14.6 | 5.3 | 15.3 | 7.9 | +5% | +46.5% (stated) |
| PAT minus EBITDA | +2.3 | +0.2 | +1.2 | -2.8 | | |
H1 PAT minus EBITDA: H1 FY26 +2.5 (19.9 vs 17.4); H1 FY27 -1.6 (23.2 vs 24.8). Swing about Rs 4.1 cr.

## FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-1 | F6 | R065, R045, R016, R018, R020, R022 | 117 | "Margins are in line with our targeted range of 18-20%" | FORWARD-SIGNAL | A trackable margin band. Q2 FY27 EBITDA 18.8% and H1 18.5% sit inside it; Q2 FY26 15.4% and H1 FY26 17.2% sat below it. The band is newly reached, not a run-rate. The sentence follows the PAT sentence (line 115); PAT margin 13.8% (R028) is outside it, so which margin is targeted is not stated. Role 5 tracker item: EBITDA margin vs 18-20% each quarter. |
| F6-2 | F6 | R035, R036, R067, R087 | 86, 90, 122-124 | "With a healthy open order pipeline of ₹133 crore ... we are well positioned to sustain our growth momentum" | FORWARD-SIGNAL | Order book Rs 133 cr Sep-26 vs Rs 44 cr Sep-25 = 3.0x. At the H1 FY27 run-rate (Rs 268 cr annualised, DERIVED) it covers about 6 months of revenue. Order inflow is called "healthy" (line 106) but not quantified; opening order book (Mar-26) ND, so H1 inflow and book-to-bill cannot be computed. Execution timeline of the 133 ND. |
| F6-3 | F6 | R069, R070 | 114, 118 | "continuing to invest in capabilities that strengthen our competitive position" | AMBIGUOUS | Investment intent with no amount, asset or date. Line 114 credits "better capacity utilisation". Undisclosed capex is a candidate reading for the D&A side of F14-1. |
| F12-1 | F12 | R002, R003, R005, R006, R008, R009, R011, R012, R059, R089 | 68-78 | "Product    Spares" (legend, line 78; values unlabelled in stacks) | AMBIGUOUS | Revenue split is assigned by chart position only. Reading A (first legend series at stack base = Product): Product 17 -> 37 (+118%), Spares 16 -> 20 (+25%) in Q2; Spares share 48% -> 35% (Q2), 30% -> 25% (H1); Q1 Spares flat at 14 both years (DERIVED). Reading B (reverse): Spares 37 of 57 (65%) in Q2 FY27, up from 52%. Under A, growth is equipment-led and margin rose despite a lower Spares share; under B, the margin rise is mix-led. Separating observation: a labelled split in the results filing or deck. No segment assets or liabilities in document. |
| F14-1 | F14 | R091, R016, R020, R026, R030, R018, R022, R028, R032 | 112-117 | "Our EBITDA for the quarter increased by 108.8% year-on-year to ₹11 crore" | AMBIGUOUS | EBITDA is defined nowhere. PAT margin exceeded EBITDA margin in Q2 FY26 (16.1% vs 15.4%) and H1 FY26 (19.7% vs 17.2%), then fell below it in Q2 FY27 (13.8% vs 18.8%) and H1 FY27 (17.3% vs 18.5%). PAT > EBITDA implies EBITDA excludes Other Income [INFERENCE] and that non-operating income was material in FY26. The PAT-minus-EBITDA cushion swung about Rs 4.1 cr in H1 (DERIVED). Three readings: lower Other Income (treasury drawn down), higher D&A (capacity investment, F6-3), higher tax rate. This is why PAT growth (+17.1% H1) lags EBITDA growth (+43.4% H1). Lean bear: PAT quality now rests more on operations, but the release headlines EBITDA and does not explain the gap. |
| F14-2 | F14 | R086, R073, R077 | 57 | "announced its unaudited financial results for the quarter & half-year ended 30th September 2026" | NEUTRAL-FACT | The release does not state whether figures are standalone or consolidated, and does not mention a limited review. The results filing governs; A4 matches these figures to the filed basis. |
| F16-1 | F16 | R004, R007, R010, R013, R014, R082, R084 | 102-105 | "Our performance in the second quarter of FY27 reflects the sustained momentum in our business" | AMBIGUOUS | The release shows YoY only. DERIVED Q1 FY27 revenue is Rs 77 cr, so Q2 FY27 (Rs 57 cr) is down about 26% QoQ. Q2 FY26 (Rs 33 cr) was itself down about 51% from Q1 FY26 (Rs 68 cr), so the +70.9% headline grows off a weak base. Q1 FY27 grew only +13% YoY revenue and about +5% PAT. Two readings: Q1-heavy seasonality (both years show Q2 < Q1) or lumpy delivery-timed revenue. "Sustained momentum" is not shown quarter on quarter. Separating observation: Q3 FY27 revenue vs Q2 FY27 against the 133 order book. |
| F16-2 | F16 | R092, R046, R036, R087 | 83, 122-123 | "Order Book as on September 30th, 2026 (₹ crore)" vs "healthy open order pipeline of ₹133 crore" | AMBIGUOUS | One number, two labels. "Pipeline" can mean enquiries or bids, not firm orders. Conservative reading: 133 is not confirmed as firm, executable, net-of-GST backlog until defined. The definition (firm vs pipeline, gross vs net of GST, includes spares/service contracts or not) decides whether F6-2 coverage holds. |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | N.A. | Press release has no financial template; A2 zero_standing = 0. |
| F2 | N.A. | One unlabelled set of figures; no standalone vs consolidated pair (basis gap logged at F14-2). |
| F3 | N.A. | No cost lines in document. |
| F4 | N.A. | No auditor report or Other Matters paragraph. |
| F5 | N.A. | No EoM or Going Concern text; prior-quarter fulltext ND. |
| F6 | FINDING | Strict lexicon: zero hits (no "will be", "expected", "commenc", "underway", etc.). Seven undated forward rows (R065-R071) read; three findings F6-1, F6-2, F6-3. |
| F7 | PASS | Hedge lexicon: zero hits ("subject to", "no assurance", "exploring", "evaluating", "endeavour" all absent). No safe-harbour disclaimer either. Nothing to flag. |
| F8 | N.A. | No tax, PBT or deferred-tax line; ETR not computable. Tax is one of the readings named in F14-1. |
| F9 | N.A. | No OCI line. |
| F10 | N.A. | Deck carries no share count or EPS. |
| F11 | N.A. | Deck carries no net worth or reserves. |
| F12 | FINDING | No segment assets or liabilities; the deck carries a Product/Spares revenue stack, assigned by position only (F12-1). |
| F13 | N.A. | No board outcome, AGM, dividend or director text; Reg 30 cover letter only (line 30-32). |
| F14 | FINDING | EBITDA undefined and PAT/EBITDA ordering flips (F14-1); figure basis and review status not stated (F14-2). |
| F15 | N.A. | No consolidation or entity list; prior ND. |
| F16 | FINDING | Dropped disclosures vs prior deck: not assessable (prior ND). Within-deck reframing: YoY-only framing hides QoQ decline (F16-1); order book vs pipeline label (F16-2). |
| F17 | N.A. | Not a concall; Notion checklist ND (pre-thesis read). |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| EBITDA (assumed) margin in the 18-20% targeted range | ongoing, undated | R065, line 117 | none stated (claimed met in Q2/H1 FY27) |
| Sustain growth momentum off Rs 133 cr open order pipeline | undated (order book executes over roughly the next 6 months at H1 run-rate, DERIVED) | R067, lines 122-124 | none stated |
| Continue to invest in capabilities | undated, no amount | R069, lines 117-119 | none stated |
| Strengthen portfolio, broaden capabilities across mining and construction | undated, boilerplate | R071, lines 149-153 | none stated |
| Demand optimism on infrastructure and mining activity | undated | R066, lines 121-122 | none stated |

## QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
- F6-1: Which margin is the 18-20% target, and over what horizon? Is 20% a ceiling?
- F6-2 / F16-2: Is Rs 133 cr firm order book or pipeline? Gross or net of GST? Spares/service included? Execution schedule? H1 order inflow and opening Mar-26 book?
- F6-3: Capex amount and assets behind "invest in capabilities"; capacity added in FY26-FY27?
- F12-1: Product vs Spares values per quarter, labelled.
- F14-1: EBITDA definition; Other Income, D&A, finance cost and tax for Q2 FY26 / Q2 FY27 / H1 both years (match to results filing).
- F16-1: Q1 vs Q2 seasonality pattern; why Q2 FY27 revenue fell from Q1 FY27.

```yaml
stage: A3-forensics
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/eimcoeleco-q2fy27/work/forensics_pressrelease_eimcoeleco_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F6-1", check: "F6", line: "117", classification: "FORWARD-SIGNAL", implication: "18-20% margin band newly reached (Q2 FY27 EBITDA 18.8%, H1 18.5% vs FY26 15.4%/17.2%); which margin is targeted not stated; PAT 13.8% is outside it"}
  - {id: "F6-2", check: "F6", line: "86, 90, 122-124", classification: "FORWARD-SIGNAL", implication: "Order book Rs 133 cr vs Rs 44 cr a year ago (3.0x), about 6 months of H1-run-rate revenue; inflow and execution timeline ND"}
  - {id: "F6-3", check: "F6", line: "114, 118", classification: "AMBIGUOUS", implication: "Investment in capabilities unquantified; candidate D&A driver behind F14-1"}
  - {id: "F12-1", check: "F12", line: "68-78", classification: "AMBIGUOUS", implication: "Product/Spares split by chart position only; reading A equipment-led growth with Spares share 48% to 35% in Q2, reading B mix-led margin gain; labelled split separates them"}
  - {id: "F14-1", check: "F14", line: "112-117", classification: "AMBIGUOUS", implication: "EBITDA undefined; PAT exceeded EBITDA in FY26 periods and fell below it in FY27 periods, about Rs 4.1 cr H1 swing; other income down, D&A up or tax up; explains PAT growth lagging EBITDA growth"}
  - {id: "F14-2", check: "F14", line: "57", classification: "NEUTRAL-FACT", implication: "Standalone/consolidated basis and limited-review status not stated; results filing governs"}
  - {id: "F16-1", check: "F16", line: "102-105", classification: "AMBIGUOUS", implication: "YoY-only framing; derived Q1 FY27 revenue Rs 77 cr so Q2 Rs 57 cr is about 26% lower QoQ; +70.9% grows off weak Q2 FY26 base; Q1 FY27 PAT about +5% YoY"}
  - {id: "F16-2", check: "F16", line: "83, 122-123", classification: "AMBIGUOUS", implication: "133 labelled Order Book in chart and open order pipeline in remarks; firm vs pipeline and GST basis undefined; decides whether F6-2 coverage holds"}
forward_signals: ["F6-1", "F6-2"]
ambiguous: ["F6-3", "F12-1", "F14-1", "F16-1", "F16-2"]
commitments:
  - {commitment: "Margin in 18-20% targeted range", implied_date: "ongoing, undated", ref: "R065 line 117", status_word: "none stated"}
  - {commitment: "Sustain growth momentum off Rs 133 cr open order pipeline", implied_date: "undated (about 6 months of revenue cover, derived)", ref: "R067 lines 122-124", status_word: "none stated"}
  - {commitment: "Continue to invest in capabilities", implied_date: "undated, no amount", ref: "R069 lines 117-119", status_word: "none stated"}
  - {commitment: "Strengthen portfolio and broaden capabilities", implied_date: "undated", ref: "R071 lines 149-153", status_word: "none stated"}
  - {commitment: "Demand optimism on infrastructure and mining", implied_date: "undated", ref: "R066 lines 121-122", status_word: "none stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The release headlines YoY growth off a weak Q2 FY26 base (Rs 33 cr, itself about 51% below Q1 FY26). H1 minus Q2 puts Q1 FY27 revenue at about Rs 77 cr, so Q2 fell about 26% QoQ and Q1 FY27 PAT grew only about 5%. The PAT/EBITDA flip matters most: in FY26 PAT exceeded EBITDA, so EBITDA likely excludes a material other-income line. That cushion shrank about Rs 4.1 cr in H1. PAT therefore grew far slower than EBITDA. A4 should match every figure to the results filing's Other Income, D&A and tax lines. The 3.0x order book is the main forward signal. Its label switch (Order Book vs open order pipeline) must be resolved before it counts as backlog. Pipeline defect: A1 cites R061 at line 140; the name is at line 160."
```
