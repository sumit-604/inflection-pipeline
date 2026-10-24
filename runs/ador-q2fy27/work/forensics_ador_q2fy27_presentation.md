# A3 FORENSIC NOTES: ADOR (Ador Welding Limited), Q2 FY27, doctype PRESENTATION

Source document (via A1 only): Ador_Q2FY27_Investor_Presentation_2026-10-22.pdf, 29 pages.
Inputs read: runs/ador-q2fy27/extracted/ador-presentation-q2fy27-structured.md (R001-R470, all rows),
runs/ador-q2fy27/extracted/ador-presentation-q2fy27-fulltext.md (lines 1-833, all), runs/ador-q2fy27/work/ledger_presentation_ador_q2fy27.md.
Cross-reference (headline reconciliation only): runs/ador-q2fy27/extracted/ador-results-q2fy27-structured.md (INR lakhs, x0.01 to Rs Cr).
Prior-quarter deck: none (first run). Notion checklist: none, no companies/ADOR.md, no spear. PRE-THESIS READ.
Source PDF and inputs/ were not opened.
Units: Rs Crores as printed unless a filing row (lakhs) is cited; filing values below are converted to Rs Cr at x0.01.

## 0. LEDGER RECONCILIATION

- A2 ledger accounts for 470 structured IDs (R001-R470, contiguous). I read all 470 at their cited fulltext line. Reconciled: 470 / 470 = 100%.
- Anchor discrepancies found (value present verbatim, line off; non-material, for A1/A2 awareness):
  - R441 ("2024: Ador Fontech M&R Division merger completed") cites line 662; the text is at line 696-698. Line 662 is the 1974 Ador Fontech entry.
  - R003 ("October 2026") cites line 65; line 65 reads "Investor Presentation", the date is at line 67 (R421 cites 67 correctly).
  - R446 ("2011 & 2012") cites line 392; the years sit on line 393.
- A1 coverage note: line 564 carries a third orphan "Financial assets 0.0" (current-asset side) that has no row. R277 (line 556) and R278 (line 572) capture the other two. Non-material heading artefact.
- R469 FOOTNOTE_UNRESOLVED (cash-flow first column period length) is RESOLVED by cross-reference: deck "Net Cash from Operating Activities -8.5" (line 589) equals filing consolidated H1 FY27 "(845)" lakhs (results R809). The column is six months, H1 FY27.

## 0A. DECK vs RESULTS FILING: HEADLINE RECONCILIATION (consolidated)

| Metric | Deck (line) | Filing (row, lakhs -> Rs Cr) | Tie |
|---|---|---|---|
| Revenue Q2 FY27 | 345 (127) | 34,474 -> 344.74 (R474) | yes |
| Revenue YoY Q2 | +22.6% (129) | 344.74 / 281.09 (R476) = +22.6% | yes |
| Revenue H1 FY27 | 654.2 (788) | 65,420 -> 654.20 (R477) | yes |
| PAT Q2 FY27 | 27, +7.7% (133, 135) | 2,694 / 2,501 (R591, R593) = +7.7% | yes |
| PAT H1 FY27 | 54.5, +159.0% (808, 153) | 5,454 / 2,106 (R594, R595) = +159% | yes (see FN-17) |
| EPS Q2 / H1 | 15.5 / 31.3 (133, 810) | basic 15.48 / 31.34 (R660, R663) | yes, basic |
| PBT H1 / FY26 | 73.3 / 115.0 (805) | 7,331 / 11,500 (R570, R572) | yes |
| Onerous cost FY26 | 24.8 (796) | 2,482 (R533); H1 FY26 2,792 (R532) | yes |
| Impairment reversal FY26 | -14.1 (797) | (1,412) (R540) | yes |
| Exceptional FY26 | -2.8 (804) | (275) (R565) | yes |
| Other income H1 | 11.8 (798) | 1,183 (R483) | yes |
| Total equity 30-Sep-26 | 569.6 (550) | 56,962 -> 569.62 (R724) | yes |
| Current borrowings 30-Sep-26 | 27.7 (562) | 2,771 (R738) | yes |
| Trade payables 30-Sep-26 | 145.5 (564) | 3,428 + 11,119 = 14,547 (R742, R744) | yes |
| CWIP 30-Sep-26 | 12.6 (552) | 1,029 -> 10.29 (R682) | NO (FN-13) |
| Right-of-use 30-Sep-26 | 10.3 (553) | 1,256 -> 12.56 (R680) | NO (FN-13) |
| OCF / Investing / Financing H1 | -8.5 / 2.0 / -15.5 (589-591) | (845) / 201 / (1,550) (R809, R827, R841) | yes |

Derived checks (computed from filing rows, not printed on the deck):
- H1 FY26 EBITDA excl. other income, before onerous cost = PBT 28.63 - OI 9.28 + D&A 9.53 + finance 1.47 + onerous 27.92 = 58.27 (R571, R484, R526, R520, R532). Deck H1 FY27 73.4 / 58.27 = +26.0%, matches line 147. The deck EBITDA base EXCLUDES the onerous charge. The deck PAT base INCLUDES it.
- Q1 FY27 EBITDA excl. OI = 36.93 - 7.02 + 4.99 + 0.81 = 35.71 on revenue 309.46 = 11.5% (R568, R481, R523, R517, R475). Q2 FY27 = 37.72 on 344.74 = 10.9%.
- Q1 FY27 gross margin approx (230.7 - 118) / 309.5 = 36.4% (deck lines 790, 127; Q2 GP printed rounded). Q2 34.2% (line 127).
- H2 FY26 consolidated PAT = 81.98 - 21.06 = 60.92 (R596, R595). H2 FY26 one-offs pre-tax: impairment reversal +14.12 (R540, H1 nil R539), onerous write-back +3.10 (27.92 to 24.82), exceptional -2.75 (R565, H1 nil R564). Net +14.47.
- Equity roll-forward: 554.45 (R725) + total comprehensive income 54.02 (R612) - dividend paid 40.03 (R837) = 568.44 vs 569.62 printed. Residual +1.18 (0.2%).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F1 | R106, R108, R464 | line 796, 824 (slide 25) | "Onerous Cost & Liquidated Damages 0.0 24.8 0.0" ... "the project itself is still being executed." | FORWARD-SIGNAL | The standing line stays live because the project is open. It anticipates a further overrun charge or an LD settlement or write-back at close. The FY26 charge already fell from 27.92 (H1 FY26, R532) to 24.82 (FY26, R533): Rs 3.1 Cr reversed in H2 FY26. Direction of the next entry is unknown; lean bear. |
| FN-02 | F1 | R109, R111, R153, R465 | line 797, 831-832 (slide 25) | "The company recovered Rs. 14.1 Cr of that old receivable in FY26" | AMBIGUOUS | "of that" leaves open whether a provided Kuwait balance remains. A further recovery is a gain through the same standing line; a write-off is a loss. Balance NOT FOUND in deck. |
| FN-03 | F1 | R130, R131, R132 | line 804 (slide 25) | "Exceptional Items Gain / (Loss) 0.0 -2.8 -11.4" | NEUTRAL-FACT | Exceptional losses two years running (FY25 -11.4, FY26 -2.8); nature not on deck. Results filing note 4 governs; the results-filing A3 reads it. |
| FN-04 | F1 | R166, R202, R203, R204, R207, R277, R278 | lines 555, 568, 569, 556, 572 (slide 26) | "Other liabilities 0.0 0.0 0.0" | NEUTRAL-FACT | Template artefacts. Non-current borrowings 0.0 at 30-Sep-26 while current borrowings rose to 27.7 (FN-18). No transaction class anticipated beyond the debt shift. |
| FN-05 | F6 | R418, R447, R464, R151, R152, R389 | line 815-816, 818-819, 824 (slide 25) | "(targeted for completion by June 2025)" ... "Rs. 15.0 Cr for potential liquidated damages" | FORWARD-SIGNAL | A dated commitment missed by 15+ months as of 22-Oct-2026 (line 18). The Rs 15.0 Cr LD provision equals 27.5% of H1 FY27 PAT (54.5, line 808). Non-current provisions rose 9.3 to 20.2 to 20.9 (line 558) [INFERENCE: the LD provision sits there]. Closure brings cash LD payment or a write-back. |
| FN-06 | F6 | R403 | line 115-116 (slide 4) | "We continue to evaluate acquisition opportunities to accelerate growth in this segment." | FORWARD-SIGNAL | Undated M&A intent in automation. H1 OCF is -8.5 (line 589) and current borrowings 27.7 (line 562); funding route and size not stated. |
| FN-07 | F6 | R396, R424 | line 118 (slide 4) | "We remain confident of carrying this momentum through the rest of FY27." | FORWARD-SIGNAL | Dateable to 31-Mar-2027 and testable against 23% H1 revenue growth. The H2 FY26 profit base carries +14.47 Cr net one-off gains (section 0A), so H2 YoY profit optics start adverse. |
| FN-08 | F7 | R404, R323 | line 105-107 (slide 4) | "remains our primary export market, and we continue to monitor developments in the region closely" | AMBIGUOUS | A hedge on the primary export market. The deck gives no export revenue share or Middle East trend. Pairs with the geopolitical hedge at line 103. |
| FN-09 | F7 | R398, R325 | line 107 (slide 4) | "exploring new opportunities in European markets" | AMBIGUOUS | Exploratory, no target, no date. Two readings: growth extension, or diversification away from Middle East risk (FN-08). |
| FN-10 | F7 | R397, R454 | line 101-103 (slide 4) | "We continue to take calibrated pricing actions and to monitor raw material and geopolitical developments closely." | FORWARD-SIGNAL | "Calibrated" means partial pass-through. Q2 gross margin fell 440 bps YoY (line 129) on steel inflation (line 101). H2 margin depends on the pass-through lag. |
| FN-11 | F8 | R133-R135, R139-R141 | line 805, 807 (slide 25) | "Tax 18.8 33.0 26.5" | AMBIGUOUS | ETR 25.6% H1 FY27, 28.7% FY26, 30.6% FY25 vs statutory 25.17%: FY26 +350 bps, FY25 +540 bps. Filing H1 FY26 deferred tax credit 4.74 (R583) is 17% of the 27.92 onerous charge, below statutory. If H2 ETR reverts to the FY26 level, H1-equivalent PAT is about 2.3 lower [INFERENCE: 73.3 x 3.1%]. Driver NOT FOUND in deck. |
| FN-12 | F10 | R029, R045, R148, R157-R159 | line 133, 551 (slides 5, 26) | "Earnings Per Share ... Rs. 15.5" | NEUTRAL-FACT | Paid-up capital 17.4 flat at all three dates. Filing basic/diluted: Q2 FY27 15.48/15.43 (R660, R667), H1 FY27 31.34/31.25 (R663, R670), FY26 47.11/47.06; Q2 FY26 and H1 FY26 nil spread (R662/R669, R664/R671). A dilutive instrument appeared in H2 FY26. The deck prints one unlabelled EPS. A4 cross-checks the instrument (ESOP or other). |
| FN-13 | F14 | R220, R223 | line 552-553 (slide 26) | "CWIP 12.6 3.2 4.1" / "Right of use asset 10.3 12.4 11.5" | NEUTRAL-FACT | The 30-Sep-26 values are transposed vs the filing: CWIP 10.29 (R682), ROU 12.56 (R680). The 31-Mar-26 column ties. Correct CWIP is 10.3. Downstream stages must use the filing value. |
| FN-14 | F14 | R306, R469 | line 582, 592 (slide 27) | "Net Decrease in Cash and Cash equivalents -22.0 12.0 26.2" | NEUTRAL-FACT | The label is wrong for the FY26 and FY25 increases. The first column reads "30th Sep-26" with no period length (line 582); the filing resolves it as H1 FY27 (R809). |
| FN-15 | F14 | R363, R446, R450, R004, R009 | line 391-393, 787, 98, 102 (slides 19, 25, 4) | "Mid-Sized Companies in Asia 2011 & 2012" | NEUTRAL-FACT | A 14-year-old award on a 2026 awards slide. P&L columns mix unaudited H1 FY27 with audited FY26/FY25, no audit-status label (line 787). The message rounds 22.6% to "23%" and 8.6% to "9%" (lines 98, 102 vs 129). Each is small; together they are a drafting-care data point. |
| FN-16 | F16 | R011, R023, R024, R008, R020 | line 102 vs 134-136, 129 (slides 4, 5) | "H1 FY27 EBITDA margin held steady at around 11%" | FORWARD-SIGNAL | The H1 frame masks a Q2 decline. Q2 EBITDA margin 10.9%, -140 bps YoY (line 134-136). Q1 FY27 11.5% (filing-derived, section 0A), so -60 bps QoQ. Gross margin about 36.4% Q1 to 34.2% Q2. H1 11.2% is below the FY26 11.6% (line 795). Input-cost squeeze is live in the exit-rate quarter. |
| FN-17 | F16 | R042, R046, R044, R459 | line 153, 156 (slide 6) | "+159.0% YoY" | FORWARD-SIGNAL | The base is H1 FY26 PAT 21.06 after the 27.92 onerous charge (R595, R532). Slide 6 carries no footnote, and EBITDA growth on the same slide uses a pre-onerous base (section 0A). Underlying H1 PAT growth is about +30% [INFERENCE: 21.06 + 27.92 x (1 - 0.2517) = 41.95]. H2 FY27 compares against a base lifted by the +14.47 net one-off gains. |
| FN-18 | F16 | R297, R288, R291, R184, R185, R190, R191, R250, R251, R259, R260 | line 586-589, 562, 564, 563, 567 (slides 26, 27) | "Net Cash from Operating Activities -8.5" | AMBIGUOUS | Management's message is silent on cash. H1 PAT 54.5 vs OCF -8.5; WC -73.0. Trade payables 193.7 to 145.5; filing non-MSME creditors 174.49 to 111.19 (R745, R744). Inventory 151.9 to 177.1. Cash 42.3 to 20.4. Dividend paid 40.03 (R837) against new borrowings 27.0 (R839). Reading A: pre-buying steel or early payment for discounts. Reading B: supplier credit tightening. The separating observation is the Q3 payables and inventory level. |
| FN-19 | F16 | R220, R221 | line 552 (slide 26) | "CWIP 12.6 3.2" | AMBIGUOUS | CWIP 3.2 to 10.3 (corrected, FN-13), 3.2x in six months. Filing H1 capex 16.15 (R811). The deck states no capex plan and no capacity addition; stated capacity is 90,000 MT and 30,000 units (lines 617-620). |
| FN-20 | F16 | R271, R468 | line 573-574 (slide 26) | "Other current assets (incl. asset classified as held for sale) 44.8 26.8 25.5" | AMBIGUOUS | +18.0 (+67%) in H1. The label signals an asset held for sale; the filing line "(c) Other current assets" 44.85 (R714) shows no held-for-sale split in A1 rows. Which asset, what value, what timing: NOT FOUND. |

Cross-deck F16 diffs (dropped metrics, changed baselines, softened guidance) are NOT TESTABLE: no prior deck. The order-book definition test does not apply: the deck prints no order book.

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | FINDING | 12 ZERO_STANDING rows read. Onerous and impairment-reversal lines stay live with the project open and the Kuwait balance unclear (FN-01 to FN-04). |
| F2 | N.A. | The deck is consolidated only (lines 138, 156). The S-vs-C decomposition runs in the results-filing A3. Deck consolidated headlines tie to filing consolidated (section 0A). |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor Other Matters in the deck. |
| F5 | N.A. | No EoM or going-concern paragraph in the deck; no prior deck. |
| F6 | FINDING | Commitments extracted, one missed dated commitment (FN-05 to FN-07); register below. |
| F7 | FINDING | Hedges on the primary export market, Europe, pricing and M&A (FN-08 to FN-10). Safe-harbor "subject to" at line 82 is boilerplate. |
| F8 | FINDING | ETR 25.6/28.7/30.6% vs 25.17% (FN-11). No prior-year tax adjustment line in the deck. |
| F9 | N.A. | The deck carries no OCI line. |
| F10 | FINDING | Paid-up flat; diluted EPS spread appears from H2 FY26 per filing (FN-12). |
| F11 | PASS | 17.4 + 552.2 = 569.6 (lines 550-552) = filing 569.62 (R724), gap 0.0%. Roll-forward residual +1.18 (0.2%) [INFERENCE: share-based payment reserve, consistent with FN-12]. |
| F12 | N.A. | No segment assets or liabilities in the deck; runs in the results-filing A3. |
| F13 | PASS | Interim dividend Rs 7.50 (line 117) matches filing R015 (record date 30-Oct-2026, R017). No AR, AGM or fund-raise item. The board slide (lines 433-466: 10 directors, 5 independent) prints no term dates; no prior deck to diff. |
| F14 | FINDING | CWIP/ROU transposition, cash-flow label, stale award, unlabelled audit status, upward rounding (FN-13 to FN-15). |
| F15 | N.A. | The deck carries no consolidation list; no prior deck. |
| F16 | FINDING | Within-deck reframes: H1 margin frame, +159% PAT base, silence on negative OCF and new debt, unexplained CWIP and held-for-sale (FN-16 to FN-20). Cross-deck diffs NOT TESTABLE. |
| F17 | N.A. | Not a concall. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Flares & Process Equipment turnkey project completion | June 2025 (missed) | slide 25, line 815-816, 824 (R418, R447) | underway ("still being executed") |
| Interim dividend Rs 7.50 per share | record 30-Oct-2026, pay by 20-Nov-2026 (filing R017, R018) | slide 4, line 117 (R014) | completed (declared) |
| Carry momentum through the rest of FY27 | 31-Mar-2027 | slide 4, line 118 (R396) | initiated (confidence statement) |
| Evaluate acquisitions in automation | undated | slide 4, line 115-116 (R403) | initiated ("evaluate") |
| Expand international distributor network; explore Europe | undated | slide 4, line 107 (R398) | initiated ("exploring") |
| Calibrated pricing actions vs raw material inflation | ongoing, H2 FY27 | slide 4, line 102-103 (R397) | underway |
| Scale technology-led equipment, Ador WelDoS, robotics and cobots | undated | slide 4, lines 108-116 (R399, R402) | underway |
| Axbot 101 cobotic solution | done | slide 17, line 363 (R352) | completed ("Launched") |
| CNC bevel and H2 cutting solutions | done | slide 17, line 367-368 | completed ("available for customer experience") |
| Ador Fontech M&R Division merger | 2024 | slide 8, line 696-698 (R441) | completed |
| Upload presentation to website | Oct 2026 | page 1, line 33 (R395) | administrative |

## 4. FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: FN-01, FN-05, FN-06, FN-07, FN-10, FN-16, FN-17 (7).
AMBIGUOUS: FN-02, FN-08, FN-09, FN-11, FN-18, FN-19, FN-20 (7).
NEUTRAL-FACT: FN-03, FN-04, FN-12 (A4 ESOP cross-check), FN-13, FN-14, FN-15 (6).
CONFIRMATORY-NEGATIVE: none. No prior quarter exists to establish sustained silence.

```yaml
stage: A3-forensics
company: "ADOR"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/ador-q2fy27/work/forensics_ador_q2fy27_presentation.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F1", line: "796, 824", classification: "FORWARD-SIGNAL", implication: "Onerous/LD line live while project open; next entry is charge or write-back; FY26 charge already cut 27.92 to 24.82"}
  - {id: "FN-02", check: "F1", line: "797, 831-832", classification: "AMBIGUOUS", implication: "Residual provided Kuwait receivable NOT FOUND; further recovery gain or write-off possible"}
  - {id: "FN-03", check: "F1", line: "804", classification: "NEUTRAL-FACT", implication: "Exceptional losses FY25 -11.4, FY26 -2.8; nature in filing note 4"}
  - {id: "FN-04", check: "F1", line: "555, 556, 568, 569, 572", classification: "NEUTRAL-FACT", implication: "Template zero lines; NC borrowings 0.0 as debt moved to current"}
  - {id: "FN-05", check: "F6", line: "815-816, 818-819, 824", classification: "FORWARD-SIGNAL", implication: "Flares project 15+ months past June 2025 target; Rs 15.0 Cr potential LDs = 27.5% of H1 PAT; cash LD or write-back at close"}
  - {id: "FN-06", check: "F6", line: "115-116", classification: "FORWARD-SIGNAL", implication: "Undated automation M&A intent with negative H1 OCF and new 27.7 Cr debt"}
  - {id: "FN-07", check: "F6", line: "118", classification: "FORWARD-SIGNAL", implication: "FY27 momentum claim testable by 31-Mar-2027; H2 FY26 base carries +14.47 Cr net one-off gains"}
  - {id: "FN-08", check: "F7", line: "105-107", classification: "AMBIGUOUS", implication: "Hedge on primary export market (Middle East); export share NOT FOUND"}
  - {id: "FN-09", check: "F7", line: "107", classification: "AMBIGUOUS", implication: "Europe exploration undated; growth vs Middle East de-risking"}
  - {id: "FN-10", check: "F7", line: "101-103", classification: "FORWARD-SIGNAL", implication: "Calibrated (partial) pass-through after -440 bps Q2 gross margin; H2 margin hinges on lag"}
  - {id: "FN-11", check: "F8", line: "805, 807", classification: "AMBIGUOUS", implication: "ETR 25.6/28.7/30.6% vs 25.17%; reversion to FY26 rate costs ~2.3 Cr on H1-equivalent PAT"}
  - {id: "FN-12", check: "F10", line: "133, 551", classification: "NEUTRAL-FACT", implication: "Paid-up flat; filing diluted spread appears from H2 FY26 (15.48/15.43 Q2); A4 ESOP cross-check"}
  - {id: "FN-13", check: "F14", line: "552-553", classification: "NEUTRAL-FACT", implication: "Sep-26 CWIP/ROU transposed vs filing (CWIP 10.29, ROU 12.56); use filing values"}
  - {id: "FN-14", check: "F14", line: "582, 592", classification: "NEUTRAL-FACT", implication: "Net Decrease label on increases; first CF column is H1 FY27 per filing R809"}
  - {id: "FN-15", check: "F14", line: "391-393, 787, 98, 102", classification: "NEUTRAL-FACT", implication: "Stale 2011-12 award, unlabelled audit status, upward rounding; drafting-care data point"}
  - {id: "FN-16", check: "F16", line: "102, 129, 134-136", classification: "FORWARD-SIGNAL", implication: "H1 'held steady' masks Q2 EBITDA margin 10.9% (-140 bps YoY, -60 bps QoQ); exit-rate squeeze"}
  - {id: "FN-17", check: "F16", line: "153, 156", classification: "FORWARD-SIGNAL", implication: "+159% H1 PAT is base effect of 27.92 Cr onerous charge; underlying ~+30% [INFERENCE]; H2 base flattered"}
  - {id: "FN-18", check: "F16", line: "562, 564, 567, 586-589", classification: "AMBIGUOUS", implication: "OCF -8.5 vs PAT 54.5; payables -48.2, inventory +25.2; dividend 40.03 partly debt-funded; deck silent"}
  - {id: "FN-19", check: "F16", line: "552", classification: "AMBIGUOUS", implication: "CWIP 3.2 to 10.3 in H1 with no capex plan or capacity addition on deck"}
  - {id: "FN-20", check: "F16", line: "573-574", classification: "AMBIGUOUS", implication: "Other current assets +18.0 incl. held-for-sale asset; asset, value, timing NOT FOUND"}
forward_signals: ["FN-01", "FN-05", "FN-06", "FN-07", "FN-10", "FN-16", "FN-17"]
ambiguous: ["FN-02", "FN-08", "FN-09", "FN-11", "FN-18", "FN-19", "FN-20"]
commitments:
  - {commitment: "Flares & Process Equipment turnkey project completion", implied_date: "June 2025 (missed)", ref: "slide 25 line 815-816, 824", status_word: "underway"}
  - {commitment: "Interim dividend Rs 7.50/share", implied_date: "record 30-Oct-2026; pay by 20-Nov-2026", ref: "slide 4 line 117; filing R017-R018", status_word: "completed"}
  - {commitment: "Carry momentum through rest of FY27", implied_date: "31-Mar-2027", ref: "slide 4 line 118", status_word: "initiated"}
  - {commitment: "Evaluate acquisitions in automation", implied_date: "undated", ref: "slide 4 line 115-116", status_word: "initiated"}
  - {commitment: "Expand distributor network; explore Europe", implied_date: "undated", ref: "slide 4 line 107", status_word: "initiated"}
  - {commitment: "Calibrated pricing actions vs input inflation", implied_date: "H2 FY27", ref: "slide 4 line 102-103", status_word: "underway"}
  - {commitment: "Scale tech-led equipment, WelDoS, robotics", implied_date: "undated", ref: "slide 4 line 108-116", status_word: "underway"}
  - {commitment: "Axbot 101 cobot launch", implied_date: "done", ref: "slide 17 line 363", status_word: "completed"}
  - {commitment: "Ador Fontech M&R Division merger", implied_date: "2024", ref: "slide 8 line 696-698", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Headline numbers tie to the consolidated filing, except a Sep-26 CWIP/ROU transposition (FN-13). The deck's growth story rests on two framing choices. First, H1 PAT +159% is a base effect: H1 FY26 absorbed a 27.92 Cr onerous charge, while H1 EBITDA growth (+26%) is stated on a pre-onerous base. Underlying PAT growth is about +30%. Second, 'H1 margin held steady' hides a Q2 exit rate of 10.9%, down 60 bps QoQ and 140 bps YoY, as steel inflation outran 'calibrated' pricing. The cash side is the sharper signal. H1 OCF was -8.5 against PAT 54.5. Non-MSME payables fell 36%. The 40 Cr dividend was partly funded by 27 Cr of new short-term debt. The deck says nothing on it. H2 FY26 carried +14.5 Cr of net one-off gains, so H2 FY27 YoY profit optics start adverse. The open Flares project (15 Cr potential LDs, 15+ months late) is the swing item in either direction. Cross-deck F16 diffs are not testable on a first run."
```
