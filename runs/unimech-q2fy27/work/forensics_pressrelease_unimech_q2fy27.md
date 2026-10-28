# A3 FORENSIC NOTES: UNIMECH q2fy27, doctype PRESSRELEASE (presentation-class)

Agent: A3 forensics | model: claude-opus-5-5 | run date: 2026-10-28
Inputs read: A1 structured (R001-R123), A1 fulltext (lines 1-147, all), A2 ledger, Notion monitoring checklist (28-Oct-2026 extract). Comparison only: deck structured (`extracted/unimech-presentation-q2fy27-structured.md`) and results structured (`extracted/unimech-results-q2fy27-structured.md`), cited by file and row. Nothing under inputs/ was opened. Prior-quarter press release: none available.

## LEDGER RECONCILIATION (123 of 123 rows read = 100%)

All 123 structured IDs in the A2 ledger were read at their cited fulltext line. Every value matches the text. Line-cite slips (value correct, line off by 1-4; A1 quality note, not a finding):
- R091 headline sits at line 52, not 56.
- R092 "reinforcing our confidence in the momentum ahead" sits at line 83, not 82.
- R105 period text sits at line 26 (and 32), not 27.
- R055/R056 H1 EBITDA "Rs.882.6 Mn up 130% YoY" sits at line 80, not 79.
- R083 sector list runs lines 113-115. R090 risk list sits at lines 144-145, not 140.
- R015-R046 cite the column-scrambled raw lines 63-71. Values were checked against the render-verified table, lines 106-109. Example: raw line 65 shows "98%" on the Total Revenue row. The verified line 106 shows 81%. A1 flagged this in its header.

Figure tie-out against the results filing (results structured; lakhs to Mn = /10; my arithmetic):
- Revenue from operations Q2 1,230.0 = R445 12,299.83. Q1 1,076.2 = R446. Q2 FY26 619.8 = R447. H1 2,306.2 = R448. H1 FY26 1,249.7 = R449. All tie.
- Total Revenue Q2 1,299.8 = R457 "Total income" 12,997.62. H1 2,449.3 = R460. All tie.
- EBITDA Q2 = PBT R511 4,490.68 + finance R487 203.36 + D&A R493 904.32 - other income R451 697.79 = 4,900.57 lakhs = 490.1 Mn. Ties. Q2 FY26 = 2,067.76 + 139.14 + 634.06 - 986.58 = 1,854.38 = 185.4. Ties. Q1 = 3,668.84 + 193.76 + 795.70 - 732.85 = 3,925.45 = 392.5. Ties. So EBITDA excludes other income and sits before the associate share.
- PAT Q2 317.7 = R541 3,252.83 + R547 (75.35) = 3,177.48. H1 596.4 = R544 6,053.00 + R550 (89.15). Ties. NCI Q2 is (0.26) lakhs (R595). The PAT headline is total PAT, and the NCI difference is immaterial.
- All YoY/QoQ percentages recompute within rounding.
- "~96% of FY26 Revenues": 2,306.2 / FY26 revenue from operations 2,404.9 (deck R268; results R450 24,049.04) = 95.9%. Ties. The basis is revenue from operations, which the release does not state.

No press-release number differs from the deck or the filing. What differs is framing and definitions (below).

## FINDINGS TABLE

| id | check | ledger row | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| P-A3-01 | F16 | R013, R014, R121 | 55 | "Consolidated Order Book at 8,546 Mn up 8-times YoY" | AMBIGUOUS | The "8-times" compares unlike bases. The deck splits the Rs 855 Cr total into "Rs. 266 Cr confirmed POs + LTA & Award Letter ~Rs. 589 Cr" (deck R041, R042, R656). Its YoY chart is "Confirmed PO's only" (R658): Rs 105 Cr Sep-25 to Rs 266 Cr Sep-26, +153% (R048-R050). 8,546 / 1,050 Mn = 8.1x (my arithmetic). So the headline divides total book (69% LTA/award letters) by last year's confirmed-PO-only book. Like for like, confirmed POs grew 2.5x, not 8x. Q1 FY27 book on file was Rs 280.3 Cr (checklist line 207), basis not stated. If that was a confirmed-PO figure, confirmed POs fell about 5% QoQ (266 vs 280.3; my arithmetic) while the headline book tripled through LTA/award inclusion. A4 questions: the basis of the Rs 280.3 Cr and Rs 314 Cr prior books; the valuation and tenure rules for the ~Rs 589 Cr LTA/award component. |
| P-A3-02 | F16 | R076, R093 | 92-94 | "Long-term supply agreements and award programs with premier global aerospace OEMs are successfully transitioning Unimech" | AMBIGUOUS | The release names no OEM and gives no value, tenure or minimum volume. This is the same pool the deck books as ~Rs 589 Cr of order book (deck R656). The filed Honeywell LTA (26-Oct) is a framework where Honeywell "may issue purchase orders" (checklist line 387). It carries no value. If such frameworks sit inside the Rs 589 Cr, part of the book has no committed volume. A4 question: which LTAs/award letters make up the Rs 589 Cr? Are they valued at contracted minimums or at management forecast? Is Honeywell included, and at what number? |
| P-A3-03 | F16 | R047-R049, R051, R054, R118 | 74-81 | "supported by healthy demand and robust execution" / "a high-margin order mix, and strong operating leverage" | AMBIGUOUS | The 3-page release never mentions Hobel (no hit in lines 1-147). Hobel was consolidated w.e.f. 01-May-2026 (checklist line 205), so the Q2 FY26 base has none. The 98% YoY and "~96% of FY26 Revenues" (line 77) therefore include an acquisition step-up. FY26 was also a de-growth year (checklist line 209). The 40% margin gets credit to order mix and operating leverage. File: Hobel EBITDA margin >50% (checklist line 68). Part of the margin lift is acquisition mix. The file's Q1 reading was "Margin lift is a mix artifact" (checklist line 206). Q2 40% and H1 38% (deck R028, R030) sit above the FY27 guide of 34-35% (checklist line 259). Either the guide is stale or H2 compresses. A4 questions: organic ex-Hobel revenue growth and margin for Q2; does the 34-35% FY27 guide stand? |
| P-A3-04 | F16 | R054, R119 | 78 | "EBITDA in Q2 stood at Rs.490.1 Mn up 164% YoY with robust margins of 40%" | NEUTRAL-FACT | The undefined margin reconciles. EBITDA excludes other income (tie-out above). 490.1 / 1,230.0 = 39.8% on revenue from operations, rounded to 40%. On the "Total Revenue" line it would be 37.7% (my arithmetic). The deck shows the same 40% (deck R028). No definition change. Use 39.8% on revenue from operations downstream. |
| P-A3-05 | F6 | R078, R094, R111, R113, R064 | 94-96 | "has generated commercial revenues in H1, with a sharp step-up anticipated in H2" | FORWARD-SIGNAL | It is dateable (H2 FY27, Oct-26 to Mar-27) but carries no number. Neither the H1 semiconductor revenue nor the H2 target is given. The customer is unnamed ("global OEM major"). "20-month development pipeline" (line 95) can mean 20 months elapsed or 20 months ahead. The deck gives FAI counts (deck R059 60 proved, R060 20 in pipeline) and a semiconductor order-book share (deck R055 11%), but no revenue. A4: request the H1 semiconductor revenue and the H2 figure or range, so the Q3/Q4 prints can score the "sharp step-up". |
| P-A3-06 | F6 | R095, R096, R112 | 96-97 | "serial production scaling over coming quarters will create a compounding, multi-year revenue runway" | FORWARD-SIGNAL | The commitment carries "will" with no date, programme, part count or revenue. "Coming quarters" is not scoreable. A4: name the programmes moving from prove-out to serial production and the first serial-production quarter. |
| P-A3-07 | F6 | R079, R097 | 99 | "Our automated special-process cell installation is underway" | FORWARD-SIGNAL | Status word: underway. The release gives no capex, completion date or capacity. The deck dates the related goal: "NADCAP certification targeted by FY27-end" (deck R591). Track installation complete, then NADCAP by Mar-2027, on the Role 5 promise ledger. A4: capex amount, commissioning quarter, and whether NADCAP gates any order-book revenue. |
| P-A3-08 | F6 | R080, R098 | 99-101 | "our Middle East expansion via the Saudi Arabia JV ensure we possess the floor space, technical capabilities, and global presence" | AMBIGUOUS | The release speaks in the present tense about capacity that does not yet operate. The filed target for commercial production is late Mar/early Apr 2027. The second SAR 30M tranche is undated (checklist line 289, line 288). The release gives neither. It also omits the 49% partner share (Kanoo), so any Saudi revenue consolidates with NCI. A4: second-tranche date and funding source; production-start date still late Mar/early Apr 2027? (tracker rows on file). |
| P-A3-09 | F14 | R015-R022, R120 | 106 | "Total Revenue \| 1,299.8 \| 718.5 \| 81%" | NEUTRAL-FACT | "Total Revenue" is the filing's "Total income" (results R457), so other income of 69.8 Mn (deck R117) sits inside a line labelled revenue. The 17-point gap between Total Revenue YoY (81%) and revenue from operations YoY (98%) is other income falling 29% YoY (deck R119). Treasury income keeps fading as IPO cash deploys. That supports the file's view and is not new. Use revenue from operations, never "Total Revenue", for growth and margin. |
| P-A3-10 | F17 | (absence; R001-R123) | 49-147 (absence); checklist lines 115-121 | checklist: "\| 6 \| CRISIL rating status \| Reinstated / cooperating \| Non-cooperation persists or downgrade \|" | AMBIGUOUS | Silence audit run against the monitoring checklist and open file items; see table below. A press release is a promotional document, so silence here weighs less than silence on a call. It still extends the CRISIL run the file tracks. The release also omits the cash-conversion data the H1 Pillar 2 upgrade test needs. Route every row to the 28-Oct call question list. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | PASS | Ledger ZERO_STANDING count 0; the 4x8 highlights table has no nil or dash cells. |
| F2 | N.A. | The release shows consolidated highlights only (line 61); no standalone figures. Covered in results A3. |
| F3 | N.A. | No cost lines in a press release. |
| F4 | N.A. | No auditor Other Matters; release is unaudited (line 59). |
| F5 | N.A. | No EoM or going-concern paragraph; no prior-quarter release to diff. |
| F6 | FINDING | Five commitments mined (register below). Four carry no number, and none carries a date inside the release: P-A3-05 to P-A3-08. |
| F7 | PASS | Hedge lexicon hits are only the safe-harbour boilerplate (lines 140-145: "could be construed", "could cause"). No note-style hedge on lumpiness or concentration. |
| F8 | N.A. | No tax line in the release. |
| F9 | N.A. | No OCI. |
| F10 | N.A. | No share count, EPS or dilution data in the release. |
| F11 | N.A. | No net worth or reserves figure in the release. |
| F12 | N.A. | No segment data; the filing is single-segment (results structured header note). |
| F13 | N.A. | Results press release only; no board outcome items. |
| F14 | FINDING | "Total Revenue" label vs filing "Total income" (P-A3-09). Date formats vary (line 18 "October 27, 2026", line 31 "October 27th, 2026", line 57 "27th October, 2026"), which is trivial. Cover letter says "Standalone and Consolidated" (line 25), but only consolidated figures appear. |
| F15 | N.A. | No consolidation list in the release; no prior release to diff. |
| F16 | FINDING | Order-book "8-times" on mixed bases (P-A3-01); LTA/award pool unnamed and unsized (P-A3-02); Hobel omitted from growth and margin attribution (P-A3-03); 40% margin definition reconciled (P-A3-04). |
| F17 | FINDING | Applied to this pressrelease because the orchestrator injected the checklist for it. Silence table below (P-A3-10). |

## F17: WHAT WAS NOT DISCUSSED (press release vs monitoring checklist and open file items)

| item | file reference | in release? | consecutive silence (as on file) |
|---|---|---|---|
| CRISIL "Issuer Not Cooperating" (master variable) | checklist line 120; line 11 (17-Sep: "7+ consecutive public documents/concalls unaddressed"; 01-Oct and 26-Oct "silent again") | No | Run continues; exact count after 17-Sep NOT FOUND on file |
| Hobel EBITDA margin (trigger c) | checklist line 117; line 260 ("REFUSED twice") | No (Hobel not named at all) | Q1 deck, Q1 call x2, this release |
| CFO/PAT and H1 cash conversion (Pillar 2 upgrade test) | checklist line 121; line 350 | No | First H1 cash reading; absent from release (results file carries the cash-flow statement) |
| Working capital days | checklist line 119 | No | NOT FOUND count |
| Capacity utilisation | checklist line 118 | No | NOT FOUND count |
| Organic ex-Hobel growth split | checklist line 233, line 269 | No | Requested since Q1 review |
| Honeywell LTA value / PO / FAI date | checklist line 450 | No (OEMs unnamed, line 93) | First document after the 26-Oct filing |
| Saudi JV second tranche date and funding | checklist lines 288-289, 352 | No (line 99-100, no date) | NOT FOUND count |
| Promoter pledge (Preetham S V, WTD) | checklist lines 304-305, 340 | No | First results document after the pledge |
| Rs 750 Cr QIP status | checklist line 214 | No | NOT FOUND count |
| FY27 margin guide 34-35% | checklist line 259 | No (40% printed, guide not restated) | First document after guide |

Thresholds the release does let us test (consolidated, filed numbers): trigger (a) H1 revenue from operations Rs 230.6 Cr, above the about Rs 200 Cr H1 pace for Rs 400 Cr (checklist line 346), so not fired. Trigger (b) Q2 EBITDA 39.8%, so not fired. Monitoring row 2 (blended EBITDA >28%) is green. This is a reading for A4, not a verdict.

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Semiconductor revenue "sharp step-up" after H1 commercial revenues | H2 FY27 (Oct-2026 to Mar-2027) | lines 94-96 (R094, R111) | initiated (commercial revenues generated in H1) |
| Serial production scaling into a "compounding, multi-year revenue runway" | "coming quarters"; not dateable | lines 96-97 (R096, R112) | underway ("prove-out happening at full force") |
| Automated special-process cell installation | none in release; deck R591 NADCAP by FY27-end (Mar-2027) | line 99 (R097) | underway |
| Middle East expansion via Saudi JV | none in release; filed production target late Mar/early Apr 2027 (checklist line 289) | lines 99-100 (R098) | underway (first tranche funded 01-Oct, per file) |
| Transition from short-cycle tooling to recurring 'flying part' manufacturing via LTAs/award programs | none | lines 92-94 (R093) | underway ("successfully transitioning") |

## ANALYST NOTE

Every number in the release ties to the filing and the deck. The forensic value is in the framing. Two framings matter for the thesis. First, the "8-times" order book divides a total that is 69% LTA and award letters by last year's confirmed-PO-only base. Like for like, confirmed POs grew 2.5x. If the Q1 Rs 280.3 Cr was confirmed POs, they fell QoQ. The book is now mostly framework value, the kind Honeywell's "may issue" LTA represents. Second, the release credits growth and the 40% margin to demand and operating leverage without naming Hobel, which drives both the YoY base effect and part of the mix. The trigger tests (a) and (b) pass on filed numbers. The unresolved questions are the order-book basis, organic growth, and whether the 34-35% guide still holds.

```yaml
stage: A3-forensics
company: "UNIMECH"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/unimech-q2fy27/work/forensics_pressrelease_unimech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
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
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "P-A3-01", check: "F16", line: "55", classification: "AMBIGUOUS", implication: "8-times order book divides total book (Rs 266 Cr confirmed POs + ~Rs 589 Cr LTA/award, deck R656) by prior-year confirmed-PO-only Rs 105 Cr (deck R048); like-for-like confirmed POs +153% (2.5x); if Q1 Rs 280.3 Cr was confirmed POs, confirmed book fell ~5% QoQ"}
  - {id: "P-A3-02", check: "F16", line: "92-94", classification: "AMBIGUOUS", implication: "LTA/award pool unnamed and unsized in release; same pool is ~Rs 589 Cr of book; Honeywell LTA is a 'may issue' framework with no value, so part of the book may carry no committed volume"}
  - {id: "P-A3-03", check: "F16", line: "74-81", classification: "AMBIGUOUS", implication: "Hobel never named; 98% YoY and ~96% of FY26 include an acquisition step-up (consolidated w.e.f. 01-May-2026); 40% margin credited to leverage though Hobel runs >50%; Q2 40% and H1 38% sit above the 34-35% FY27 guide, so either the guide is stale or H2 compresses"}
  - {id: "P-A3-04", check: "F16", line: "78", classification: "NEUTRAL-FACT", implication: "40% = EBITDA ex other income / revenue from operations = 39.8%; reconciles to results R511+R487+R493-R451; no definition change"}
  - {id: "P-A3-05", check: "F6", line: "94-96", classification: "FORWARD-SIGNAL", implication: "Semiconductor H2 FY27 'sharp step-up' has no number and an unnamed customer; '20-month pipeline' is ambiguous; needs an H1 base and H2 figure to score"}
  - {id: "P-A3-06", check: "F6", line: "96-97", classification: "FORWARD-SIGNAL", implication: "Serial production 'over coming quarters' has no date, programme or revenue; not scoreable until management names programmes and a first serial quarter"}
  - {id: "P-A3-07", check: "F6", line: "99", classification: "FORWARD-SIGNAL", implication: "Special-process cell 'underway' with no capex or date in release; deck R591 dates NADCAP by FY27-end; promise-ledger item"}
  - {id: "P-A3-08", check: "F6", line: "99-101", classification: "AMBIGUOUS", implication: "Saudi JV framed as present capacity; filed production target late Mar/early Apr 2027 and second tranche undated; 49% NCI omitted"}
  - {id: "P-A3-09", check: "F14", line: "106", classification: "NEUTRAL-FACT", implication: "'Total Revenue' = filing 'Total income' incl. other income 69.8 Mn; 81% vs 98% YoY gap is other income -29%; use revenue from operations downstream"}
  - {id: "P-A3-10", check: "F17", line: "49-147 (absence); checklist 115-121", classification: "AMBIGUOUS", implication: "Release silent on CRISIL, Hobel margin, CFO/PAT, WC, utilisation, organic split, Honeywell value, Saudi tranche, pledge, QIP, FY27 margin guide; route to 28-Oct call questions"}
forward_signals: ["P-A3-05", "P-A3-06", "P-A3-07"]
ambiguous: ["P-A3-01", "P-A3-02", "P-A3-03", "P-A3-08", "P-A3-10"]
commitments:
  - {commitment: "Semiconductor revenue sharp step-up after H1 commercial revenues", implied_date: "H2 FY27 (Oct-2026 to Mar-2027)", ref: "lines 94-96 (R094, R111)", status_word: "initiated"}
  - {commitment: "Serial production scaling into compounding multi-year revenue runway", implied_date: "coming quarters (not dateable)", ref: "lines 96-97 (R096, R112)", status_word: "underway"}
  - {commitment: "Automated special-process cell installation", implied_date: "none in release; deck R591 NADCAP by FY27-end", ref: "line 99 (R097)", status_word: "underway"}
  - {commitment: "Middle East expansion via Saudi Arabia JV", implied_date: "none in release; filed production late Mar/early Apr 2027", ref: "lines 99-100 (R098)", status_word: "underway"}
  - {commitment: "Transition from tooling to recurring flying-part manufacturing via LTAs/award programs", implied_date: "none", ref: "lines 92-94 (R093)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Every release number ties to the filing (EBITDA = PBT + finance + D&A - other income = 490.1 Mn; PAT incl. associate loss, NCI immaterial). The value is in the framing. The 8-times order book divides a total that is 69% LTA/award letters by last year's confirmed-PO-only base; like-for-like confirmed POs grew 2.5x, and if Q1 Rs 280.3 Cr was confirmed POs they fell QoQ. The book is now mostly framework value, the kind Honeywell's 'may issue' LTA represents, so book-to-revenue conversion is the forward test. The release credits growth and the 40% margin to demand and leverage without naming Hobel, which drives the YoY base effect and part of the mix. Q2 40% and H1 38% sit above the 34-35% FY27 guide, so either the guide is stale or H2 compresses. Triggers (a) and (b) are not fired on filed numbers. F17 applied to a press release because the checklist was injected; silence here weighs less than on a call."
```
