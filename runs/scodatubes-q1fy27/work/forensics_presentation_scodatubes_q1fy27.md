# A3 FORENSIC NOTES — Scoda Tubes Limited (SCODATUBES), Q1 FY27 — DOCTYPE: PRESENTATION (Investor Deck)

Source extract: `runs/scodatubes-q1fy27/work/extract_presentation_scodatubes_q1fy27.txt` (40 pages, 100% coverage)
Ledger: `runs/scodatubes-q1fy27/work/ledger_presentation_scodatubes_q1fy27.md`
Ledger reconciliation: 100% (every Table-1 slide row, every Table-3 number row L83–708, every Table-4 footnote L716–763, and both ZERO_STANDING rows read at cited A1 lines before judging).
Units: Rs Crore (x1), per A1 header and slide qualifiers "INR Crores Unless Otherwise Mentioned".
Doctype rule applied: F16 is the presentation core; F6/F7/F8/F10/F11/F14 run where the deck carries the numbers; F1–F5, F9, F12, F13, F15, F17 marked N.A. with one-line basis (no consolidation, no auditor report, no OCI/segment/board schedules, no concall transcript, no prior deck).
Protocol rule 11 applied: where a deck figure conflicts with the audited results filing, the filed/audited number governs and the contradiction is logged. Deck-only disclosures (CFO, ROCE, days, ratios) are UNAUDITED MANAGEMENT REPRESENTATIONS — labelled so, to be confirmed at audited H1 FY27.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F16-1 | F16 | Slide5 L144–145; Slide25 L867 | p5 L144–145 / p25 L867 | "Cashflow from ... Operations INR -13.8 crores (vs 18.4 crores in FY25)"; historic "Cashflow from operations -13.8 18.4 2.2 20.3" | CONFIRMATORY-NEGATIVE | Deck voluntarily discloses the negative CFO the Reg-33 filing suppressed (cash conversion was ruled INDETERMINATE). Value shown (-13.8) is FY26 ANNUAL, confirmed by the historic table. From the deck's own cashflow rows, cumulative FY23–FY26 CFO/PAT = (20.3+2.2+18.4−13.8)/(10.3+18.3+31.7+38.8) = 27.1/99.1 = **0.27x**, already below the Notion 0.30x thesis-break line before FY27 is added. Management representation; confirm at audited H1. Directly hits Notion trigger-1 and the thesis-break test. |
| F16-2 | F16 | Slide5 L144–183 | p5 "Performance Snapshot – Q1 FY27" L142–183 | title "Performance Snapshot – Q1 FY27"; "Cashflow from Operations ... (vs 18.4 crores in FY25)"; "Return on Equity (ROE) 9.9% (vs 21.1% in FY25)" | AMBIGUOUS | The Q1-titled snapshot mixes Q1 FY27 P&L KPIs (Revenue 124.3 +27.6%, GP 39.8, EBITDA 16.0, PAT 5.3) with FY26 ANNUAL cash-flow / ROE / net-D-E / debtor-day / CCC KPIs, all comped "vs FY25" and unlabelled as annual. Period-blending flatters the snapshot; ask management for the standalone Q1 FY27 CFO and Q1 ROE. |
| F16-3 | F16 | Slide22 L770–774 | p22 L770–774 | RoCE "16.6%" (FY25) / "15.9%" (FY24) / "12.6%" (FY23) / "11.6%" (FY26) | FORWARD-SIGNAL | Deck-disclosed ROCE: FY23 12.6 / FY24 15.9 / FY25 16.6 / FY26 11.6%. FY26 11.6% is materially below the Notion Pillar-1 assumption (~16–17% ROCE mapping to ~16x exit). Flag for A4 pillar re-validation; do NOT re-run valuation. Management representation. |
| F16-4 | F16 | Slide5 L151–153; Slide8 L290–301; Slide36 L1284–1286 | p5 L151–153 / p8 L292 / p36 L1284–1286 | "Gross Profit INR 39.8 crores (+40.0% y-o-y)"; "Gross Profit Margin +283 bps"; cost line "Cost of materials consumed (incl. changes in WIP and finished goods) 84.6 69.0 22.5%" | CONFIRMATORY-NEGATIVE | Deck headlines +283 bps gross-margin gain as a positive while omitting that the cost line is stated NET of WIP/FG changes; the A5 results audit showed the +283 bps is an inventory-build cost-deferral artifact (RM-consumed intensity worsened, FG/WIP build credit rose). The same build is the cash burn in F16-1 (CFO -13.8) and the inventory-days jump in F16-6 (217). Selective disclosure: margin gain foregrounded, inventory/cash caveat suppressed. |
| F16-5 | F16 | Slide8 L273, L292–302; Slide36 L1290–1302 | p8 L273/L292–293 / p36 L1292/L1300–1302 | "EBITDA ... +12.6%" but "EBITDA Margin -172 bps"; "PAT ... -25.9%"; "PAT Margin -305 bps" | CONFIRMATORY-NEGATIVE / NEUTRAL-FACT | The deck's own EBITDA margin -172 bps and PAT -25.9% / -305 bps exactly match the pipeline's corrected results grid — independent confirmation that the earlier 7→1 text-layer correction on the Reg-33 filing was right. Confirmatory of prior correction; no new question. |
| F16-6 | F16 | Slide5 L181–183; Slide22 L750–754, L770–773 | p5 L181–183 / p22 L751 (Inv 217) / L770 (DebtorD 97, CCC 211) / L772–773 | "97 days ... 211 days"; "(vs 76 days in FY25) (vs 164 in FY25)"; Inventory Days "217" (FY26) vs "156/171/163" (FY23–25) | FORWARD-SIGNAL | Deck-disclosed working-capital deterioration: Debtor Days 76→97, CCC 164→211, Inventory Days 163→217 (all FY25→FY26). Worsening on Notion triggers 2 (inv <170) and 7 (receivables ≤ revenue growth). Net Debt/Equity 0.3x (vs 1.1x FY25) and ROE 9.9% (vs 21.1%) are the offsetting reads — leverage improvement is a NEUTRAL-FACT (post-IPO equity infusion, not operating cash), ROE collapse reinforces the negative. Management representation; resolves several results-review NDs with a worsening direction. |
| F16-7 | F16 | Slide23 L801; Slide36 L1295 | p23 L801 / p36 L1295 | "Depreciation & amortization expenses 9.2 18.1 16.4 11.5"; Q1 "Depreciation & amortization expenses 4.1 1.6 162.8%" | AMBIGUOUS | FY26 annual D&A 9.2 is roughly HALF FY25 (18.1) and below FY24 (16.4) and FY23 (11.5), despite Fixed Assets nearly doubling 103.5→194.0 (L820). Yet Q1 FY27 D&A ramps +162.8% (4.1 vs 1.6); 4.1/quarter annualises to ~16.4, i.e. ~1.8x the entire FY26 print. FY26's abnormally low D&A flatters FY26 PBT/PAT (52.7/38.8) by ~Rs7–9 cr on a normalised charge — the same PAT that feeds the valuation pillar. Possible reclassification / prior-period item / component-life revision / extraction error. Management question. |
| F16-8 | F16 | Slide6 L207; Slide16 L536/L569; Slide17 L575–587 | p6 L207 / p16 L536,L569 | "a healthy order pipeline"; "Currently applied for Bureau Veritas Marine (France) and Rina Marine (Italy) standards" | CONFIRMATORY-NEGATIVE | Even in a disclosure-rich deck, catalyst quantification is withheld: order book only qualitative ("healthy order pipeline") with NO value; welded/seamless utilisation % NOT disclosed; customer-concentration % NOT disclosed (sector split and "349 clients" only). Notion triggers 4/5/8 remain unquantified. Marine RINA + BV are "currently applied for", i.e. NOT granted — Notion trigger 6 still pending, not cleared. Sustained silence on deteriorating/unproven catalysts = confirmatory negative. |
| F16-9 | F16 | Slide10 L344; Slide28 L936; Slide12 L420 | p10 L344 / p28 L936 | "20,068 MTPA2 Seamless production capacity"; table "Seamless 10,068 MTPA 20,068 MTPA" (existing / post-expansion) | AMBIGUOUS | Cross-slide inconsistency: Slide10 frames 20,068 MTPA as CURRENT seamless capacity (and Slide12 L420 shows "Increased total seamless capacity to 20,000 MTPA" achieved 2025), but Slide28's comparison table frames 20,068 as the POST-EXPANSION target with 10,068 as EXISTING. Unresolvable from text; directly corrupts any utilisation calc (triggers 4/8). Management question: what is current vs post-expansion seamless capacity? A1 also flags Slide28's rotated-axis year-to-value mapping as unresolved. |
| F6-1 | F6 | Slide6 L204–206 | p6 L204–206 | "expected to be commissioned during H2 FY27"; "committed to achieving our FY27 guidance"; "production ramps up at our seamless facility" | FORWARD-SIGNAL | Dated / dateable commitments: welded-segment commissioning H2 FY27 ("progressing as planned" = underway); FY27 guidance reaffirmed (no numeric target disclosed anywhere in deck — reaffirmation of an unstated number); seamless ramp-up underway. Feeds Role-5 promise-vs-delivery tracker and Notion trigger 4 (welded revenue Q3/Q4 FY27). |
| F7-1 | F7 | Slide6 L192–202; Slide36 L1288; Slide39 L379 | p6 L192–202 / p36 L1288 / p39 L379 | "largely transient in nature"; "confident in our ability to improve operational performance in the coming quarters"; Safe Harbor "can give no assurance" | FORWARD-SIGNAL | Chairman attributes the quarter to freight/RM volatility, a "three to four months" advance-order-booking cycle that "limited our ability to immediately pass on higher input costs", an April gas disruption ("a couple of weeks"), and manpower shortage — all claimed "largely transient". This commentary ANSWERS the results-review open question on the Other-Expenses/margin driver: Other Expenses Q1 +80.9% (21.4 vs 11.8, L1288) is the -172 bps EBITDA-margin driver. Hedged recovery claim is testable next quarter; conservative read: unverified, generate management question. |
| F10-1 | F10 | Slide23 L806, L809; Slide24 L834; Slide12 L436 | p23 L806/L809 / p24 L834 / p12 L436 | "EPS (INR) 6.8 7.6 4.6 2.6"; "Profit after tax 38.8 31.7 18.3 10.3"; "Equity capital and reserves 390.3 150.4"; "Raised INR 220 crores through public issue" | NEUTRAL-FACT | FY25 EPS 7.6 EXCEEDS FY26 EPS 6.8 despite FY26 PAT 38.8 > FY25 31.7 — consistent with IPO share-count dilution (equity+reserves 150.4→390.3, Rs220 cr raise). Partially RESOLVES results-review finding F10-1 (EPS not reconciling to flat paid-up). Deck reports combined "equity capital and reserves", so paid-up cannot be split here; note only. |
| F14-1 | F14 | Slide6 L212–213; Slide20 L668–670; Slide1 L71–73 | p6 L212–213 / p20 L668–670 / p1 L71–73 | "Mr. Samarth B Patel / Chairman & Executive Director"; "SAMARTH B PATEL / Chairperson & ED1"; cover letter "Jagrutkumar Rameshbhai Patel / Managing Director / DIN: 06785595" | AMBIGUOUS | Governance/consistency: deck names Samarth B Patel as "Chairman & Executive Director"; the Reg-33 results filing was signed by "Bharatbhai Patel, Chairman and Whole-time Director" (DIN 08036100). Dual-"Chairman" designation across the two Q1 FY27 documents for the SAME quarter. Deck cover letter resolves the MD as Jagrutkumar Rameshbhai Patel (DIN 06785595), confirming the results-review OCR-uncertain name. Governance question for A4: who chairs the board, and is there a Chairman transition? |
| F14-2 | F14 | Slide7 L230, L239; Slide30 L1092, L1094; Slide3 L112; Slide27 L899 | p7 L230/L239 / p30 L1092/L1094 / p3 L112 / p27 L899 | "57.9" vs "57.0"; "46.6%" vs "45.8%"; "Growth Strategy" vs "Key Strategies" | NEUTRAL-FACT | Drafting/number inconsistencies (individually immaterial, cumulatively a data point): Q1 FY27 export revenue 57.9 (Slide7) vs 57.0 (Slide30), ~1.6% unreconciled; export mix 46.6% (Slide7/17) vs 45.8% (Slide30); agenda item 04 "Growth Strategy" (Slide3) vs section title "Key Strategies" (Slides26/27). A2 NUMBER_DISCREPANCY / naming-mismatch flags adjudicated here — logged, not thesis-moving. |

---

## CHECKLIST SCORECARD (all 17 — every check marked)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Deck carries summarised historic statements, not statutory templates; the two ZERO_STANDING rows read (p25 L875 FY25 opening-cash dash; p10 L360 FY23 blank YoY) are benign (rounding / no prior-year comparator), not anticipatory exceptional-item lines. |
| F2 Standalone vs consolidated | N.A. | Deck is standalone only (cover letter L54 "Unaudited Standalone Financial Results"); no consolidated column exists to decompose. |
| F3 Shell-entity detection | N.A. | No subsidiary/consolidation disclosure in the deck; no cost lines to compare S-vs-C. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph in a deck; note the ENTIRE deck is unaudited management representation (flagged on every deck-only metric). |
| F5 Going concern / EoM scope | N.A. | No auditor report or EoM language in a presentation; no prior deck to verbatim-diff. |
| F6 Forward-commitment mining | FINDING | F6-1: welded commissioning "expected to be commissioned during H2 FY27" (underway), FY27 guidance reaffirmed, seamless ramp underway (p6 L204–206). |
| F7 Hedge phrase mining | FINDING | F7-1: "largely transient", "confident in our ability to improve ... coming quarters", Safe Harbor "no assurance" (p6 L200–202, p39 L379); explains Other-Expenses +80.9% margin driver. |
| F8 Tax forensics | PASS | ETR by year: FY26 26.4% (13.9/52.7), FY25 24.3%, FY24 29.3%, FY23 27.8%; Q1 FY27 24.3% (1.7/7.0), Q1 FY26 23.7% — all near statutory 25.17%, no "earlier-year" adjustment line, no deferred-tax split disclosed in deck. Nothing anomalous at deck level. |
| F9 OCI forensics | N.A. | No OCI / actuarial line disclosed anywhere in the deck. |
| F10 Share count & dilution | FINDING | F10-1: EPS FY25 7.6 > FY26 6.8 despite higher PAT = IPO dilution (equity+reserves 150.4→390.3, Rs220 cr raise); NEUTRAL-FACT, partially resolves results-review F10-1. |
| F11 Reserves / net-worth tie-out | PASS | Deck reports combined "equity capital and reserves" (390.3 FY26), so paid-up cannot be split; but disclosed Net Debt/Equity ties out: (Borrowings 185.3 − Cash 74.2)/390.3 = 0.28 ≈ 0.3x (FY26); (210.2 − 43.9)/150.4 = 1.11 ≈ 1.1x (FY25). Internal consistency holds. |
| F12 Segment forensics | N.A. | No segment assets/liabilities/revenue table (single reportable segment; welded/seamless split not quantified — withheld, folded into F16-8). |
| F13 Board outcome beyond results | N.A. | No board resolutions / AGM notice / director term dates in a deck. |
| F14 Note-drafting inconsistencies | FINDING | F14-1 governance naming (Samarth B Patel "Chairman & ED" in deck vs Bharatbhai Patel "Chairman & WTD" in filing); F14-2 number/naming discrepancies (57.9 vs 57.0; 46.6% vs 45.8%; "Growth Strategy" vs "Key Strategies"). |
| F15 Entity-list diffs | N.A. | No consolidation entity list; no prior deck to diff. |
| F16 Presentation-specific | FINDING | F16-1 to F16-9: CFO voluntary disclosure (cum CFO/PAT 0.27x), Q1/FY26 period-mixing, ROCE 11.6% vs pillar, selective gross-margin framing, corrected-grid corroboration, WC deterioration, depreciation anomaly, withheld catalysts, capacity cross-slide inconsistency. |
| F17 Concall silence audit | N.A. | This document is a presentation, not a concall transcript; no turn-level silence audit possible. Notion-checklist silence captured under F16-8 (order book / utilisation / concentration withheld) and F16-9 (capacity ambiguity). |

GATE A3: PASS — all 17 checks carry exactly one status; no blanks.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Slide / line ref | Status word |
|---|---|---|---|
| Welded-segment capacity expansion commissioned | H2 FY27 | Slide 6 / L205–206 | underway ("progressing as planned") |
| Achieve FY27 guidance (no numeric target stated in deck) | FY27 full year | Slide 6 / L204 | reaffirmed |
| Seamless facility production ramp-up | coming quarters | Slide 6 / L204 | underway |
| Improve operational performance | "coming quarters" | Slide 6 / L202 | intended / confident |
| Marine standards (Bureau Veritas Marine, Rina Marine) | not dated | Slide 16 / L536, L569 | applied-for (NOT granted) |

---

## FORWARD-SIGNAL NARRATIVE

The deck's forensic value is a disclosure delta against the bare Reg-33 filing, and it cuts against the thesis on three fronts.

First, cash. The results filing carried no cash-flow statement and the pipeline ruled cash conversion INDETERMINATE. The deck voluntarily prints CFO -13.8 cr (F16-1). Read the deck's own Historic Cashflow Statement (p25) and cumulative FY23–FY26 CFO/PAT computes to 0.27x — below the 0.30x thesis-break line before FY27 is even added, and this is management's own unaudited framing. The -13.8 is an FY26 ANNUAL figure the deck places on a slide titled "Performance Snapshot – Q1 FY27" beside Q1 P&L KPIs without a period label (F16-2), so the actual standalone Q1 FY27 CFO remains undisclosed. Confirm at audited H1; the direction is a confirmatory negative on Notion trigger-1.

Second, returns and the valuation pillar. Deck-disclosed ROCE falls to 11.6% in FY26 (F16-3), against the Pillar-1 assumption of ~16–17% mapping to ~16x. ROE simultaneously collapses 21.1%→9.9% (F16-6). And FY26 PAT is flattered by an abnormally low depreciation charge (9.2 cr, half of FY25's 18.1, while gross block nearly doubles), even as Q1 FY27 depreciation ramps +162.8% (F16-7) — normalising D&A would cut FY26 PBT by ~Rs7–9 cr. A4 should re-validate the pillar; do not re-run valuation here.

Third, earnings quality and selective framing. The deck headlines Gross Profit +40.0% and gross margin +283 bps as a win (F16-4) while the cost line is stated net of WIP/FG changes and the same inventory build shows up as the CFO burn (F16-1) and the inventory-days jump to 217 (F16-6). The deck's own EBITDA margin -172 bps and PAT -25.9% independently corroborate the pipeline's corrected grid (F16-5). Working capital worsens across the board (Debtor Days 76→97, CCC 164→211); the only genuine improvement, net-D/E 0.3x, is post-IPO equity, not operating cash.

The Chairman's commentary (F6-1, F7-1) supplies the causal story the filing lacked — freight and RM volatility, a three-to-four-month pass-through lag, an April gas outage, manpower shortage — and pins the -172 bps EBITDA-margin hit to Other Expenses +80.9%. It claims these are "largely transient" and reaffirms an unstated FY27 guidance number, with welded commissioning promised for H2 FY27. Conservative read: these are testable next-quarter claims, not resolved facts. Catalyst quantification is still withheld even here (order-book value, utilisation %, customer concentration — F16-8), marine approvals remain "applied for" not granted (trigger 6 pending), and current vs post-expansion seamless capacity is internally inconsistent (F16-9). Governance shows a dual-"Chairman" designation across the two same-quarter documents (F14-1).

Net: the deck discloses more than the filing and almost everything it newly discloses reads bearish or ambiguous. Decision Status AVOID/ZERO is unchallenged; several Notion re-engagement triggers move the wrong way or stay unquantified.

---

## ITEMS FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: F16-3 (ROCE 11.6% vs pillar), F16-6 (WC deterioration), F6-1 (H2 FY27 commissioning + reaffirmed guidance), F7-1 (transient-headwind / recovery claim to test).
AMBIGUOUS: F16-2 (Q1/FY26 period-mixing — request standalone Q1 CFO/ROE), F16-7 (depreciation anomaly), F16-9 (seamless capacity 10,068 vs 20,068), F14-1 (dual-Chairman designation).

---

```yaml
stage: A3-forensics
company: "SCODATUBES"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "runs/scodatubes-q1fy27/work/forensics_presentation_scodatubes_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F16-1", check: "F16", line: "p5 L144-145; p25 L867", classification: "CONFIRMATORY-NEGATIVE", implication: "Deck voluntarily discloses CFO -13.8 (FY26 annual) that Reg-33 filing suppressed; cum FY23-26 CFO/PAT=0.27x, below 0.30x thesis-break. Management representation; confirm at audited H1."}
  - {id: "F16-2", check: "F16", line: "p5 L142-183", classification: "AMBIGUOUS", implication: "Q1-titled snapshot blends Q1 FY27 P&L KPIs with FY26 annual CFO/ROE/WC KPIs unlabelled; request standalone Q1 FY27 CFO and ROE."}
  - {id: "F16-3", check: "F16", line: "p22 L770-774", classification: "FORWARD-SIGNAL", implication: "ROCE FY26 11.6% vs Pillar-1 assumption ~16-17%/~16x; A4 pillar re-validation, no valuation re-run."}
  - {id: "F16-4", check: "F16", line: "p5 L151-153; p8 L292; p36 L1284-1286", classification: "CONFIRMATORY-NEGATIVE", implication: "Headlines +283 bps gross-margin gain; cost line net of WIP/FG build (inventory-build cost-deferral artifact); caveat suppressed. Same build is the CFO burn."}
  - {id: "F16-5", check: "F16", line: "p8 L273,L292-293; p36 L1292,L1300-1302", classification: "CONFIRMATORY-NEGATIVE", implication: "Deck EBITDA -172 bps and PAT -25.9%/-305 bps match pipeline corrected grid; confirms earlier 7->1 correction. No new question."}
  - {id: "F16-6", check: "F16", line: "p5 L181-183; p22 L751,L770-773", classification: "FORWARD-SIGNAL", implication: "Debtor Days 76->97, CCC 164->211, Inventory Days 163->217 (FY25->FY26) worsen triggers 2/7; net-D/E 0.3x improvement is post-IPO equity, neutral."}
  - {id: "F16-7", check: "F16", line: "p23 L801; p36 L1295", classification: "AMBIGUOUS", implication: "FY26 D&A 9.2 halved vs FY25 18.1 despite gross block ~doubling; Q1 FY27 D&A +162.8%. Low FY26 D&A flatters PBT ~Rs7-9cr feeding pillar. Management question."}
  - {id: "F16-8", check: "F16", line: "p6 L207; p16 L536,L569", classification: "CONFIRMATORY-NEGATIVE", implication: "Order-book value, utilisation %, customer concentration withheld (triggers 4/5/8 unquantified); marine RINA+BV 'applied for' not granted (trigger 6 pending)."}
  - {id: "F16-9", check: "F16", line: "p10 L344; p28 L936", classification: "AMBIGUOUS", implication: "Seamless 20,068 MTPA framed current (Slide10/12) vs post-expansion target with 10,068 existing (Slide28); corrupts utilisation calc. Management question."}
  - {id: "F6-1", check: "F6", line: "p6 L204-206", classification: "FORWARD-SIGNAL", implication: "Welded commissioning H2 FY27 (underway); FY27 guidance reaffirmed (no numeric target); seamless ramp underway. Feeds promise-vs-delivery + trigger 4."}
  - {id: "F7-1", check: "F7", line: "p6 L192-202; p36 L1288; p39 L379", classification: "FORWARD-SIGNAL", implication: "Headwinds claimed 'largely transient'; explains Other-Expenses +80.9% margin driver; recovery claim testable next quarter; conservative read = generate question."}
  - {id: "F10-1", check: "F10", line: "p23 L806,L809; p24 L834; p12 L436", classification: "NEUTRAL-FACT", implication: "EPS FY25 7.6>FY26 6.8 despite higher PAT = IPO dilution (Rs220cr raise; equity+reserves 150.4->390.3); partially resolves results-review F10-1."}
  - {id: "F14-1", check: "F14", line: "p6 L212-213; p20 L668-670; p1 L71-73", classification: "AMBIGUOUS", implication: "Deck names Samarth B Patel 'Chairman & Executive Director' vs filing's Bharatbhai Patel 'Chairman & WTD' (DIN 08036100); MD Jagrutkumar (DIN 06785595) confirmed. Governance question re Chairman."}
  - {id: "F14-2", check: "F14", line: "p7 L230,L239; p30 L1092,L1094; p3 L112; p27 L899", classification: "NEUTRAL-FACT", implication: "Export rev 57.9 vs 57.0; export mix 46.6% vs 45.8%; 'Growth Strategy' vs 'Key Strategies'. A2 NUMBER_DISCREPANCY/naming flags adjudicated; logged, not thesis-moving."}
forward_signals: ["F16-3", "F16-6", "F6-1", "F7-1"]
ambiguous: ["F16-2", "F16-7", "F16-9", "F14-1"]
commitments:
  - {commitment: "Welded-segment capacity expansion commissioned", implied_date: "H2 FY27", ref: "Slide6 L205-206", status_word: "underway"}
  - {commitment: "Achieve FY27 guidance (no numeric target stated)", implied_date: "FY27", ref: "Slide6 L204", status_word: "reaffirmed"}
  - {commitment: "Seamless facility production ramp-up", implied_date: "coming quarters", ref: "Slide6 L204", status_word: "underway"}
  - {commitment: "Improve operational performance", implied_date: "coming quarters", ref: "Slide6 L202", status_word: "intended"}
  - {commitment: "Marine standards (Bureau Veritas Marine, Rina Marine)", implied_date: "undated", ref: "Slide16 L536,L569", status_word: "applied-for"}
gate_a3: pass
blank_checks: []
```
