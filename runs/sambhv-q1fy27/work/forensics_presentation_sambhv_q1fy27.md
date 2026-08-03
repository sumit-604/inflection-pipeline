# A3 FORENSIC NOTES — INVESTOR PRESENTATION — SAMBHV (Sambhv Steel Tubes Ltd) — Q1 FY27

Doctype: presentation (43 slides / 43 PDF pages). Source extract:
`extract_presentation_sambhv_q1fy27.txt`. Reconciliation contract:
`ledger_presentation_sambhv_q1fy27.md`.
Model: claude-opus-4-8. Prior-quarter deck: NONE (first pipeline run — this deck is the Q2FY27 baseline).

## LEDGER RECONCILIATION STATEMENT
100% of the A2 ledger was read verbatim at its cited lines before judging:
Table 1 (43-slide inventory), Table 2 (all 1,111 atomic numbers, slide by slide),
Table 3 (all 16 ZERO_STANDING clusters), Table 4 (all footnotes/qualifiers),
Table 5 (footer pagination). Every A2 flag (NUMERIC_DISCREPANCY, CHART_ONLY_DATA,
ZERO_STANDING, the 7 OCR slides + 2 OCR diagrams) was re-checked against the
extract lines rather than taken on trust. `ledger_reconciled_pct: 100`.

Doctype applicability (per instruction + task): F16 applies; F6/F10/F11 apply
because the deck carries those numbers; F8 applies because the deck prints Tax
Expense + PBT (slide 37); balance-sheet-only checks F2/F3/F4/F5/F9/F12/F13/F15
are N.A. because the deck prints no consolidated financials, no auditor report,
no OCI, no segment assets/liabilities, no board resolutions, and no
consolidation entity list; F17 is N.A. (no concall this run). DROPPED_SLIDE and
reframed-vs-prior diffs under F16 are NOT computable this run (no prior deck) —
stated explicitly; this deck is the baseline for the Q2FY27 diff.

---

## KEY THESIS-GATE READOUT (hunted per task; details in findings table)
- (1) EBITDA/tonne binding gate — CLEARED. Q1FY27 Op.EBITDA/T = **INR 9,355**
  (incl.) / **INR 10,002** ex-sponge iron (L201/L207) vs FY26 6,964 / 7,517
  (L1033/L1039). Trigger is <Rs 6,000/T for 2 consecutive quarters; Q1FY27 sits
  ~56% above the line. (Context: slide-35 trend FY23 7,422 / FY24 7,161 / FY25
  **5,321** / FY26 6,964 — FY25 dipped below 6,000, now recovered.) See FND-09.
- (2) SS 200-/300-series realisations (monitoring #13) — **NOT DISCLOSED** in the
  deck. Blended EBITDA/ton and segment volumes are given; per-series SS
  realisation is absent. See FND-05 (A4 must source).
- (3) Kesda Phase-I SS-coil commissioning — **"targeted for commissioning by
  Q4FY27"** (L237-238, L326). Q4FY27 is BEFORE the Q1FY28 thesis-break line, so
  on-schedule per the deck, BUT equipment erection is only ~20-40% and Testing &
  Commissioning is uniformly "TBC" on slide 12. See FND-02.
- (4) Net Debt / ND-EBITDA — Net Debt/Op.EBITDA **1.00x** (Q1FY27, annualized
  basis per footnote L225) vs 0.78x FY26 (L1039). Under the 2.0x trigger.
  Absolute Net Debt not printed for Q1FY27. See FND-06.
- (5) Captive power — 25MW existing (16MW WHRB + 9MW AFBC, L771-772); adding
  25MW Kesda + 30MW Sarora + 8MW rooftop solar (L240/244/248). PLUS an
  unreconciled "POWER PLANT - 20MW" site-layout label on slide 10 (L271). See
  FND-04.
- (6) Volume mix VAP vs intermediate — Q1FY27 deck (L222): Intermediate 6,580 /
  Structural 56,617 / SS 14,760 / Pre-Gal(GP) 29,814 / Total 107,771 MT.
  RECONCILES to the 2-Jul BSE release: VAP sub-total 56,617+14,760+29,814 =
  **1,01,191** and total **1,07,771** both tie exactly; intermediate 6,580
  (-49.3% YoY) confirmed. No restatement discrepancy. (See FND-11 note.)

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | T3 L1290; T2 L1256/1258/1270 | slide 39, L1290 | "Add: Cash and cash equivalents pursuant to business combinations" — dash all four years | AMBIGUOUS | Whole-row nil M&A template line anticipates a business combination; deck is standalone-only yet the cash flow carries subsidiary flows (Investment in subsidiary FY25 652 L1256; Loan given to subsidiary FY26 (8) L1258; Repayment of Loan from Subsidiary FY26 (273) L1270). An unconsolidated subsidiary exists but its P&L is invisible in this standalone deck; a future population of L1290 = acquisition signal. A4 question. |
| FND-02 | F6 | T2 L237-238, L314-349, L326 | slides 9 & 12, L237-238 | "targeted for commissioning by Q4FY27"; slide 12 "Testing and Commissioning … Q4FY27 … TBC" | FORWARD-SIGNAL | Binding-gate #3: Kesda Phase-I SS coils (0.36 MMTPA, CAPEX 8,100 Mn) + 25MW Kesda power both targeted Q4FY27; all six execution divisions converge on Q4FY27 with equipment erection ~20-40% and testing "TBC". Single-quarter execution cliff; Q4FY27 target leaves only ~1 quarter of buffer before the Q1FY28 thesis-break line — slip risk is the live watch item. A4 milestone question. |
| FND-03 | F16 | T2 L751-758 | slide 26 | Bloom/Slabs (MS) "300,000 … 280,000"; HR Coil (MS) "390,000 … 370,000"; SS lines 60,000→80,000 | FORWARD-SIGNAL | Between the FY2026 column and the 30-Jun-26 column, 20,000 MTPA each of MS Bloom/Slabs and MS HR Coil capacity is re-tasked to Stainless-Steel (SS lines rise 60,000→80,000). Shared-melt/roll totals are unchanged (Bloom 360k, HR 450k), so this is a deliberate mix shift into higher-value SS, not a capacity loss — supports the SS-realisation thesis. Watch SS utilisation next quarter. |
| FND-04 | F16 | T2 L271 (CHART_ONLY_DATA) | slide 10, L271 | "POWER PLANT - 20MW" (site-layout label) | AMBIGUOUS | The master-plan drawing prints a 20MW plant that reconciles with none of the disclosed additions (25MW Kesda / 30MW Sarora / 8MW solar). Either a distinct 4th power asset, a preliminary/legacy drawing figure, or a mislabel of the 25MW Kesda Phase-I plant. Slide also separately labels "SPACE FOR FUTURE POWER PLANT". A4 management question. |
| FND-05 | F16 | (absent-metric) | deck-wide | — (not disclosed) | AMBIGUOUS | Monitoring #13 SS per-series realisations (200-series ≥Rs 1,15,000/MT; 300-series ≥Rs 1,75,000/MT) are NOT in the deck; only blended EBITDA/ton and segment volumes appear. Also absent: promoter pledge, FII+DII (no shareholding slide, monitoring #14), corporate guarantees ~Rs 1,610 Cr, land advance Rs 11.5 Cr, RPT trend, audit-trail status. A4 must source these from the results filing / AR. (Not "dropped" — no prior deck to diff; flagged as baseline gaps.) |
| FND-06 | F16 | T2 L207; T4 L225 | slide 8, L207/L225 | "1.00x  Net Debt / Op. EBITDA*" ; footnote "*as on 30th June'26, annualized basis" | AMBIGUOUS | Q1FY27 ND/Op.EBITDA 1.00x is struck on an ANNUALIZED (Q1×4) denominator — a generous basis — and the absolute Net Debt rupee figure is not printed (no Q1FY27 balance sheet in the deck). Derived FY26 net debt ≈1,873-1,941 Mn (gross borrowings 3,713 L1224/L1231 less liquids 1,840 L1233/L1234/L1231), broadly consistent with the stated 0.78x. Absolute Q1FY27 net debt is not derivable here; capex drawdown for the Q4FY27 build is likely lifting it. 1.00x still well under the 2.0x trigger. A4: request trailing-basis ratio + absolute net debt. |
| FND-07 | F10 | T2 L463, L1219, L1280, L507 | slide 15 L463; slide 38 L1219 | Reported EPS "1.92  1.39" (+38%) vs PAT "566  334" (+69%) | NEUTRAL-FACT | EPS growth materially lags PAT growth (Q1FY27 +38% EPS vs +69% PAT; FY26 +111% EPS vs +147% PAT, L463) because of IPO share expansion — Share Capital 2,410→2,947 (L1219) via equity issue 4,400 Mn FY26 (L1280; IPO "raised INR 440 Cr" L507). Per-share dilution is IPO base-effect; normalizes from Q2FY27 (IPO anniversary). Only "Reported" EPS is shown — no diluted EPS, so a dilutive-instrument spread cannot be tested from the deck. |
| FND-08 | F14 | T2 L181, L189; L1236, L227 | slides 7, 8, 38 | "1,18,000 MTPA at Kuthrel Unit II" (L181) vs "58,000 MTPA to 1,16,000 MTPA at Kuthrel" (L189); "Othe Current Assets" (L1236); "not reorganised as Revenue" (L227) | AMBIGUOUS | The SS CR-coil capacity carries two adjacent figures — CTE for a 1,18,000 MTPA facility at Kuthrel Unit II vs CTO doubling an existing line to 1,16,000 MTPA at Kuthrel; 116,000 is used everywhere else (slides 21/25/26). Likely two distinct approvals (new Unit-II facility vs existing-line doubling) but the 118k/116k gap should be confirmed. Typos ("Othe", "reorganised"→recognised) are immaterial individually, a minor governance/drafting data point cumulatively. A4: confirm the 118k vs 116k are separate facilities. |
| FND-09 | F16 | T2 L201, L207, L1127-1130 | slides 8 & 35 | "INR 9,355 Op. EBITDA / T" ; slide-35 trend "7,422 … 5,321 … 6,964" | NEUTRAL-FACT (thesis-supporting) | EBITDA/tonne binding gate CLEARED at 9,355 (incl.)/10,002 (ex-sponge) vs 6,000 trigger. Historical trend shows FY25 dipped to 5,321 (below trigger) before recovering to 6,964 FY26 and 9,355 Q1FY27 — the metric is volatile, so the "2 consecutive quarters" clause matters; one strong quarter is not the all-clear, but Q1FY27 is unambiguously above the line. |
| FND-10 | F16 | T2 L359-361, L416, L1075 (NUMERIC_DISCREPANCY) | slides 13/14/34 | "26.80%" (L361) ; "28.96%" (L416) ; "28.65%" (L1075) | NEUTRAL-FACT (A2 flag resolved) | The three GP-margin values are THREE DIFFERENT PERIODS, not a conflict: Q1FY27 quarterly GP margin = 28.96% (slide 13 chart value 2,120/7,322 AND slide 14 L416 agree); FY26 annual = 28.65% (slide 34, 6,913/24,132 L1064/L1075); 26.80% is Q3FY26 quarterly (slide 13, 1,579/5,891). A2's NUMERIC_DISCREPANCY was an extraction-ORDER artifact (slide-13 margin series was captured out of chart sequence). No genuine discrepancy. |
| FND-11 | F16 | T2 L222 | slide 8, L222 | Sales Volume "6,580 … 56,617 … 14,760 … 29,814 … 107,771 MT" | NEUTRAL-FACT | Deck volumes reconcile EXACTLY to the 2-Jul BSE release (VAP sub-total 1,01,191 = 56,617+14,760+29,814; grand total 1,07,771; intermediate 6,580). No restatement. Note the deck's own qualifier (L227): "Sales Volume figures include certain sales that are not reorganised [recognised] as Revenue" — sales volume ≠ revenue-recognised volume, so do not derive realisation directly from these totals. |

---

## CHECKLIST SCORECARD (all 17 — no blanks; GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1  Zero-value standing line items | FINDING | L1290 business-combination nil-row (all 4 yrs) + subsidiary flows in a standalone-only deck → FND-01. Slide-26 SS-line dashes are benign pre-existence nils (SS "Manufacturing started FY2025", footnote L745). |
| F2  Standalone vs Consolidated | N.A. | Deck is 100% standalone (every footnote "Standalone Financial Performance"); no consolidated figures printed to decompose, though a subsidiary demonstrably exists (FND-01). |
| F3  Shell-entity detection | N.A. | Requires standalone-vs-consolidated cost lines; consolidated not printed. |
| F4  Unaudited contribution ratio | N.A. | No auditor "Other Matters" in a presentation. |
| F5  Going concern / EoM scope | N.A. | No auditor report / EoM paragraph in a presentation; no prior deck to verbatim-diff. |
| F6  Forward-commitment mining | FINDING | Rich commitment set; Q4FY27 commissioning cliff across 6 divisions + 2 CAPEX bullets → FND-02; full register below. |
| F7  Hedge phrase mining | PASS | Only standard slide-3 disclaimer boilerplate ("risks and uncertainties that could cause actual results to differ", "does not undertake to update", L104-109) and "explore opportunities" (L1364). No substantive newly-added hedge on revenue lumpiness / customer concentration; no prior deck to detect additions. |
| F8  Tax forensics | PASS | Deck prints Tax Expense + PBT (slide 37). ETR: FY26 485/1,918=25.3%, FY25 26.5%, FY24 25.5%, FY23 25.5%, Q1FY27 ~26.4% (769-566)/769 — all near statutory 25.17%. No "earlier-year" tax line; DTL grows normally 142→386 (L1228). |
| F9  OCI forensics | N.A. | No statement of comprehensive income / actuarial remeasurement disclosed in the deck. |
| F10 Share count & dilution | FINDING | EPS growth lags PAT growth on IPO share expansion; share-capital change traces to the 4,400 Mn equity issue → FND-07. No diluted EPS disclosed. |
| F11 Reserves & net worth tie-out | PASS | Share Capital + Other Equity = Total Equity every year (FY26 2,947+7,608=10,555≈10,554; FY25 4,960; FY24 4,383; FY23 2,104 — L1219-1221). Ties within rounding; no third-party net-worth figure in deck to reconcile against. |
| F12 Segment forensics | N.A. | No segment assets/liabilities tables (only product-category volumes + capacity). WIP growth 857→1,872 (L1220) is a capex proxy, noted under FND-02/F16. |
| F13 Board outcome beyond results | N.A. | Presentation, not a board-outcome filing; no AGM notice, record date, or director appointment/term dates (director bios only, slides 31-32). |
| F14 Note drafting inconsistencies | FINDING | SS CR-coil 1,18,000 vs 1,16,000 label gap + typos ("Othe", "reorganised") → FND-08. |
| F15 Entity list diffs | N.A. | No consolidation entity list printed; no prior deck to diff. |
| F16 Dropped & reframed disclosures | FINDING | DROPPED not computable (no prior deck — baseline stated). Reframes/gaps within-deck: MS→SS reallocation (FND-03), 20MW mystery (FND-04), SS realisation + monitoring items absent (FND-05), net-debt basis (FND-06), EBITDA-gate readout (FND-09), GP-margin resolution (FND-10), volume tie-out (FND-11). |
| F17 Concall silence audit | N.A. | No concall this run. Monitoring-checklist items not carried by the deck are routed to A4 via FND-05, not scored here. |

---

## COMMITMENT REGISTER (F6)

| Commitment | Implied date | Slide/line ref | Status word |
|---|---|---|---|
| Kesda Phase-I SS Coils 0.36 MMTPA (CAPEX 8,100 Mn) | Q4FY27 | slide 9 L237-238; slide 41 L1326 | targeted / underway |
| 25 MW Power Plant, Kesda Phase-I (CAPEX 1,250 Mn) | Q4FY27 | slide 9 L240-242 | setting up / targeted |
| 30 MW Power Plant, Sarora Unit-III (CAPEX 1,500 Mn) | undated | slide 9 L244-246; slide 42 L1361 | adding |
| 8 MW Behind-the-meter Rooftop Solar, Kuthrel (CAPEX 250 Mn) | undated | slide 9 L248-251; slide 42 L1368 | setting up |
| ERW Pipes & Tubes brownfield DFT +1,50,000 MTPA (CAPEX 500 Mn) | undated | slide 9 L254-256; slide 41 L1331 | undertaking |
| Finished-product capacity 0.68 → >2.0 MMTPA | next 4-5 years | slide 5 L153-154 | targeted |
| SS CR-coil CTE, 1,18,000 MTPA, Kuthrel Unit II | granted (regulatory milestone) | slide 7 L181 | completed (CTE) |
| SS CR-coil CTO, doubling 58,000 → 1,16,000 MTPA, Kuthrel | granted | slide 7 L189 | completed (CTO) |
| Kesda greenfield: 4,21,600 SQM acquired, EC received, execution in progress | ongoing | slide 27 L822-826 | underway |
| Execution schedule — 6 divisions "Testing and Commissioning" | Q4FY27 | slide 12 L314/323/338/340/349 | TBC (to be commenced) |
| 18 new MoU → 28 total SS-pipe partners ("Sambhv" co-branding) | Q1FY27 achieved | slide 7 L187/190 | completed |
| Ramp up SS HRAP/CR coils, GP coils & pipes | FY26 | slide 41 L1324-1325 | completed |
| Commissioned Kuthrel facility | FY25 | slide 41 L1314 | completed |
| Increase distributors — Kerala/TN/AP/Goa/Maharashtra | undated | slide 41 L1325-1327 | plans to |
| Expand international footprint | undated | slide 41 L1330-1332 | planning |

---

## A4 HANDOFF — FLAGGED FOR MANAGEMENT QUESTIONS
FORWARD-SIGNAL: FND-02 (Q4FY27 commissioning cliff / Kesda gate), FND-03 (MS→SS
capacity reallocation).
AMBIGUOUS → convert to management questions: FND-01 (unconsolidated subsidiary /
business-combination nil), FND-04 (20MW site-plan reconciliation), FND-05 (SS
per-series realisations + monitoring items absent from deck), FND-06 (absolute
net debt + annualized-basis ND/EBITDA), FND-08 (118k vs 116k SS CR-coil).

## GATE A3
All 17 checks marked exactly one of PASS / FINDING / N.A. No blanks. gate_a3: pass.

```yaml
stage: A3-forensics
company: "SAMBHV"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sambhv-q1fy27/work/forensics_presentation_sambhv_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
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
  - {id: "FND-01", check: "F1", line: "slide 39 L1290 (T3); L1256/L1258/L1270", classification: "AMBIGUOUS", implication: "Business-combination nil-row + subsidiary flows in a standalone-only deck; unconsolidated subsidiary invisible; L1290 population = acquisition signal"}
  - {id: "FND-02", check: "F6", line: "slides 9 & 12 L237-238, L314-349, L326", classification: "FORWARD-SIGNAL", implication: "Kesda Phase-I SS coils + 6-division Testing/Commissioning all target Q4FY27 with ~20-40% erection and TBC status; slip risk vs Q1FY28 break line"}
  - {id: "FND-03", check: "F16", line: "slide 26 L751-758", classification: "FORWARD-SIGNAL", implication: "20k MTPA each of MS Bloom/Slabs and MS HR Coil re-tasked to SS (totals unchanged) — deliberate mix shift into higher-value stainless"}
  - {id: "FND-04", check: "F16", line: "slide 10 L271", classification: "AMBIGUOUS", implication: "Site-plan 20MW power plant reconciles with none of 25/30/8 MW disclosed additions; distinct 4th asset or legacy/mislabel — A4 question"}
  - {id: "FND-05", check: "F16", line: "deck-wide (absent metrics)", classification: "AMBIGUOUS", implication: "SS 200-/300-series realisations, promoter pledge, FII+DII, corporate guarantees, land advance, RPT, audit-trail all absent from deck; A4 sources from results/AR"}
  - {id: "FND-06", check: "F16", line: "slide 8 L207/L225", classification: "AMBIGUOUS", implication: "ND/Op.EBITDA 1.00x on annualized basis; absolute Q1FY27 net debt not printed; under 2.0x trigger but capex drawdown likely lifting it — request trailing basis + absolute"}
  - {id: "FND-07", check: "F10", line: "slide 15 L463; slide 38 L1219; L1280/L507", classification: "NEUTRAL-FACT", implication: "EPS growth lags PAT growth on IPO share expansion; no diluted EPS disclosed; base normalizes from Q2FY27"}
  - {id: "FND-08", check: "F14", line: "slide 7 L181/L189; L1236; L227", classification: "AMBIGUOUS", implication: "SS CR-coil 1,18,000 (CTE, Unit II) vs 1,16,000 (CTO) label gap; confirm two separate facilities; immaterial typos noted"}
  - {id: "FND-09", check: "F16", line: "slides 8 & 35 L201/L207/L1127-1130", classification: "NEUTRAL-FACT", implication: "EBITDA/tonne gate cleared at 9,355 vs 6,000 trigger; FY25 had dipped to 5,321, so metric is volatile — 2-consecutive-quarter clause still governs"}
  - {id: "FND-10", check: "F16", line: "slides 13/14/34 L361/L416/L1075", classification: "NEUTRAL-FACT", implication: "A2 GP-margin NUMERIC_DISCREPANCY resolved: three different periods (Q1FY27 28.96%, FY26 28.65%, Q3FY26 26.80%), extraction-order artifact, no real conflict"}
  - {id: "FND-11", check: "F16", line: "slide 8 L222", classification: "NEUTRAL-FACT", implication: "Deck volumes reconcile exactly to 2-Jul BSE release; sales volume includes non-revenue-recognised sales (L227), do not derive realisation directly"}
forward_signals: ["FND-02", "FND-03"]
ambiguous: ["FND-01", "FND-04", "FND-05", "FND-06", "FND-08"]
commitments:
  - {commitment: "Kesda Phase-I SS Coils 0.36 MMTPA (CAPEX 8,100 Mn)", implied_date: "Q4FY27", ref: "slide 9 L237-238; L1326", status_word: "targeted/underway"}
  - {commitment: "25 MW Power Plant Kesda Phase-I (CAPEX 1,250 Mn)", implied_date: "Q4FY27", ref: "slide 9 L240-242", status_word: "setting up"}
  - {commitment: "30 MW Power Plant Sarora Unit-III (CAPEX 1,500 Mn)", implied_date: "undated", ref: "slide 9 L244-246; L1361", status_word: "adding"}
  - {commitment: "8 MW Rooftop Solar Kuthrel (CAPEX 250 Mn)", implied_date: "undated", ref: "slide 9 L248-251; L1368", status_word: "setting up"}
  - {commitment: "ERW brownfield DFT +1,50,000 MTPA (CAPEX 500 Mn)", implied_date: "undated", ref: "slide 9 L254-256; L1331", status_word: "undertaking"}
  - {commitment: "Finished capacity 0.68 to >2.0 MMTPA", implied_date: "next 4-5 years", ref: "slide 5 L153-154", status_word: "targeted"}
  - {commitment: "SS CR-coil CTE 1,18,000 MTPA Kuthrel Unit II", implied_date: "granted", ref: "slide 7 L181", status_word: "completed"}
  - {commitment: "SS CR-coil CTO doubling to 1,16,000 MTPA Kuthrel", implied_date: "granted", ref: "slide 7 L189", status_word: "completed"}
  - {commitment: "Kesda greenfield: land acquired, EC received, execution in progress", implied_date: "ongoing", ref: "slide 27 L822-826", status_word: "underway"}
  - {commitment: "6-division Testing & Commissioning", implied_date: "Q4FY27", ref: "slide 12 L314/323/338/340/349", status_word: "TBC"}
  - {commitment: "18 new MoU to 28 total SS-pipe partners", implied_date: "Q1FY27", ref: "slide 7 L187/190", status_word: "completed"}
  - {commitment: "Increase distributors Kerala/TN/AP/Goa/Maharashtra", implied_date: "undated", ref: "slide 41 L1325-1327", status_word: "plans to"}
  - {commitment: "Expand international footprint", implied_date: "undated", ref: "slide 41 L1330-1332", status_word: "planning"}
gate_a3: pass
blank_checks: []
```
