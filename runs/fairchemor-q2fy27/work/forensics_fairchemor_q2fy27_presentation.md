# A3 FORENSIC NOTES: Fairchem Organics (FAIRCHEMOR) Q2 FY27, doctype PRESENTATION

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-23
Read status: PRE-THESIS READ. No Notion checklist, no companies/FAIRCHEMOR.md, no spear on record.
Inputs read:
- A1 structured: runs/fairchemor-q2fy27/extracted/fairchemor-presentation-q2fy27-structured.md (R001-R457, Rs Mn; loop 1 appended R458-R512)
- A1 fulltext: runs/fairchemor-q2fy27/extracted/fairchemor-presentation-q2fy27-fulltext.md (676 lines)
- A2 ledger: runs/fairchemor-q2fy27/work/ledger_presentation_fairchemor_q2fy27.md (457 rows; loop 1 addendum R458-R512)
- Cross-document (F16 only): runs/fairchemor-q2fy27/extracted/fairchemor-results-q2fy27-structured.md (Rs Lakhs). Results citations below read "results R### / results line L" (line = results fulltext line, as A1 recorded it).
- Prior quarter: none (first quarterly run). Source PDF and inputs/ not opened.

Unit conversions used: deck Rs Mn x0.1 = Rs Cr; filing Rs Lakhs x0.1 = Rs Mn.

---

## 1. LEDGER RECONCILIATION (100%)

457 of 457 ledger rows read in the structured file at their ID and in the fulltext at their cited line. Orphans: none.

| Group | Rows | Outcome |
|---|---|---|
| Cover letter, identity, dates | R001-R002, R322-R329, R395-R399 | Verbatim at lines 19-79. Letter dated October 22, 2026 (line 31). |
| Business slides p4-p13 | R003-R020, R330-R375, R382-R387, R400-R405, R419-R429 | Verbatim. R382 conflates two p4 columns (see note a). |
| Highlights p15 | R021-R036, R376, R388, R407-R408, R430-R432 | Verbatim lines 399-423. |
| Q2 and H1 tables p16-p17 | R037-R111, R409-R410, R433-R439 | LAYOUT_OFFSET confirmed. Values sit in lines 429-443 and 449-463. Every value ties to the filing within rounding (section 5). |
| Historical P&L p18 | R112-R171, R411, R440-R444 | Verbatim lines 469-504. ZERO_STANDING R156, R157, R159 read at line 492. |
| Historical BS p19 | R172-R258, R412, R445-R446 | ORDER_INFERRED confirmed by sums and by the filing. See note b. |
| Cash flow p20 | R259-R276, R413, R447 | Flows sum to zero in every column. Dash rows R271-R273 are rounding (F1). |
| Strategy p21 | R277-R279, R389-R394, R414, R448 | Verbatim lines 547-576. |
| Charts p22 | R280-R307, R415, R449-R451 | Revenue/EBITDA/PAT restate p18. CCC and net D/E positions inferred. R300-R307 left unassigned as A2 instructed. |
| Market data p23 | R308-R321, R377-R378, R416-R418, R452-R455 | Shareholding sums to 100.00%. Dividend 75%/75%/10% ties to filed dividend cash (results R297, R296). |
| Disclaimer p24 | R379-R381, R456-R457 | Verbatim lines 644-674. |

Notes for A4:
- (a) R382 reads lines 95-99 as one item. The layout shows two columns. Column 1: "Proposal to add one new / raw material (falling / under Oleo Chemicals / only) to make value / added products" (lines 96-100). Column 2: "Raw materials / throughput capacity / expansion completed / with minimal capex" (lines 95-98). This report uses the two-column reading and flags it LAYOUT_GARBLED.
- (b) p19 "first/second/third unlabelled value" rows do not map to one line item across periods. Tie-out to the filing (30-Sep-2026, Rs Mn): R188 29 = Non-current Tax Assets (results R172 291.71 lakhs); R191 5 = Other Non-current Assets (results R174 50.92); R190 39 (FY26) = Non-current Tax Assets (results R173 395.92); R229 16 = Lease Liabilities (results R206 158.17); R232 45 = Provisions (results R207 445.87); R233 209 = Deferred Tax Liabilities (results R209 2,092.43). A4 should take labels from the filing.
- (c) A2 dash rows: R184, R185, R224-R226 are header-row layout dashes, not nil values (line 515). Total Non-current Liabilities are 212 / 236 / 270 (R234-R236).

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F1 | R156, R157, R158, R159, R442 | line 492-494, p18 | "-       -     7      0" / "Exceptional Item- New Labour ... code(Net of tax)" | NEUTRAL-FACT | The template keeps a Labour Code exceptional line. FY26 carries 7 (net of tax). Filing grosses it at Rs 88.27 lakhs and calls it "nonrecurring" (results R476, line 515). H1 FY27 is 0. Watch for a true-up when final Code rules notify. Other ZERO_STANDING rows are rounding or layout (scorecard F1). |
| A3P-02 | F6 | R382, R419, R176, R177, R173, R174 | lines 95-98, p4; line 510-511, p19 | "throughput capacity / expansion completed / with minimal capex" | FORWARD-SIGNAL | Status word COMPLETED. The balance sheet agrees: CWIP 184 to 83, PPE 1,962 to 2,048 (line 511 "117    184     83"). Utilisation is now the swing variable for volume. The deck gives no capacity or utilisation figure, so the completion cannot be sized. A4: ask installed capacity (MT) before and after, and Q2 utilisation. |
| A3P-03 | F6 | R390, R448, R384, R385, R333 | lines 562-566, p21 | "we aim to increase the ... export to initially by 25% and ... eventually at 50% of the sales." | FORWARD-SIGNAL | Undated export target. The filed Note 3 says "almost all revenue from domestic sales" (results R471, line 479). The deck also lists six "Existing Markets" (line 164-170). Wording is ambiguous: "by 25%" may mean growth of 25% or a 25% share. A4: ask the current export share, the basis of the 25%, and the year for each step. |
| A3P-04 | F6 | R388, R035, R036 | lines 410-412, p15 | "likely to improve the availability of raw material and in turn our capacity utilization during the year." | FORWARD-SIGNAL | Dated commitment: higher utilisation in FY27, through more acid oil supply after the crude soya duty cut (16.5% to 11.0%). No utilisation baseline exists in the deck, so delivery cannot be tested next quarter unless management gives a number. A4: ask for the H1 utilisation % and the FY27 target. |
| A3P-05 | F7 | R432, R388, R383, R425 | line 408-409, p15; line 305, p10 | "While the macros are uncertain due to middle east crisis, we are consciously optimistic" / "FTA/Likely FTA" / "by evaluating market demand-supply scenario" | AMBIGUOUS | The outlook carries three hedges (uncertain, likely, consciously optimistic). Capacity expansion stays at "evaluating", with no capex committed. The FTA cuts both ways: management frames it as export upside (line 97-101), but the margin driver is "lower imports" (line 406). Cheaper EU/UK imports into India would press that driver. A4: ask which effect management expects to dominate. |
| A3P-06 | F9 | R070, R071, R107, R108, R160-R163 | line 493, p18 | "(1)     (1)    4      -2" | NEUTRAL-FACT | Deck OCI: FY26 +4, H1 FY27 -2. The filing shows Q1 FY27 gross remeasurement "(51.28)" lakhs (results R119, line 257) against the FY26 full year "49.86" (results R123). One quarter exceeded the full prior year with the sign reversed. That points to an actuarial assumption change, possibly the Labour Code wage base from 21-Nov-2025. The amount is about Rs 0.5 Cr, small. Verify the discount rate in the FY27 Annual Report. |
| A3P-07 | F14 | R429, R374, R451, R369, R381, R456, R033, R407 | line 381-383, 29, 582, 349, 673, 658, 399-401 | "Current auditors are KPMG, and audited by one of the Big 4 for the last 9 years" | NEUTRAL-FACT | Cumulative drafting data point. (1) The deck names KPMG. The filing names "M/s B S R and Co" (results R383, line 61), a KPMG network firm. Loose, not wrong. (2) "Last 9 years" runs back to about 2017. The CIN shows a 2019 incorporation (line 29 "L24200GJ2019PLC129759"), so the claim must include the predecessor business. (3) Typos: "EBIDTA" (line 582), "Non-Exectuive" (line 349), "undercoates" (line 186). (4) The IR email is misspelt: "farichem@valoremadvisors.com" (line 673). (5) The disclaimer lists "telecommunications technology and application" (line 658), template text from the IR firm. (6) H1 growth of 41.4% sits under the "Q2 FY27 Financial Performance" heading (line 399-401). Q2 growth was 49.7%. |
| A3P-08 | F16 | R425, R382 (deck); results R412, R373, R375, R482 | deck line 305, p10; results line 68, 588, 601, 611 | "approved the Related Party Transaction for the purchase of 2 separate pieces of land (adjoining to the plant of the Company) from the Chairman & Managing Director of the Company and his relatives" | FORWARD-SIGNAL | Omitted disclosure. The Board approved this the same day as the deck: "Rs. 12.01 Crores", "6,182 Sq. Mtrs.", counterparties "Yes, Promoters of the Company". The deck does not mention it. The deck says capacity expansion stays "evaluating". The land sits next to the plant. Its cost (120.1 Mn) is 2.7x H1 capex cash (results R283, 452.37 lakhs). It reads as a precursor to the next expansion. It is also a related-party transaction with the CMD. A4: ask the intended use, the valuation basis behind "arm's length", and the timing of any capex on the land. |
| A3P-09 | F16 | R206-R208, R246-R248 (deck); results R194, R195, R228, R229 | deck line 525 and 524, p19; results line 324, 372-373 | deck "Other current assets"; results "395.67" Asset Held for Sale, "101.00" Liabilities held for sale | AMBIGUOUS | The deck folds a held-for-sale group into other lines. Assets held for sale are 39.6 Mn (in "Other current assets" 85). Liabilities held for sale are 10.1 Mn (in "Other current liabilities" 62). The asset is unchanged since 31-Mar-2026. The liability moved 100.00 to 101.00 lakhs. Neither document names the asset. A pending sale means a future cash inflow and a possible gain or loss line. A4: ask what is held for sale, the expected price and the expected date. |
| A3P-10 | F16 | R296-R299, R200-R202, R197-R199, R262-R264 | line 600, p22; lines 521-524, p19; line 538, p20 | "128" (Cash Conversion Cycle Days, H1 FY27) / receivables "861    681" then "1002" | FORWARD-SIGNAL | The deck charts its own working-capital slide: CCC 76, 82, 99, 128 days (chart positions inferred). The narrative (lines 401-412) never mentions it. Receivables rose 47% since March (681 to 1,002). Over the same span Q2 revenue fell 5.2% QoQ (results R013 16,692.38 vs R012 17,614.57 lakhs). H1 OCF of 240 rests on an inventory release of 223 Mn (results R254 "2,230.80"). Receivables absorbed 320 Mn (results R259 "(3,200.20)"). Inventory (699) is now the lowest of the three balance-sheet dates, so H2 OCF has no inventory cushion. A3 could not reproduce 99 or 128 days from deck balances, so the method is unknown. A4: ask the CCC method, receivable days by customer class, and why receivables rose while revenue fell QoQ. |
| A3P-11 | F16 | R430, R431, R021-R026, R037-R048 | line 402-403 and 405-406, p15 | "higher price realization primarily due to higher raw material cost and higher import finished product cost" / "better realization in domestic market due to lower imports" | AMBIGUOUS | Management says growth was price-led. The deck has no volume, tonnage, capacity or utilisation figure. Filed cost lines (results R030, R037, R043, R055, R067 vs R032, R039, R045, R060, R072) split the 674 bps EBITDA gain as follows. Gross margin: about 275 bps (23.1% vs 20.3%). Fixed-cost leverage: about 401 bps, since employee, power and other costs rose about 13.5% while revenue rose 49.7%. Reading 1: import-parity spread artifact. It reverses if imports return or input prices fall, for example after the duty cut. Reading 2: a structural mix gain from upgraded products. The test that separates them: Q2 FY27 vs Q2 FY26 volume (MT) and gross spread per tonne. A4: ask for both. |
| A3P-12 | F16 | R425, R016, R401, R262, R265, R268, R237, R238, R292-R294, R309 | line 303-304, p10; lines 538-540, p20; line 521, p19; line 636, p23 | "Majority of the capacity expansion has been undertaken primarily through internal accruals." / "Recently concluded buy-back of INR 340 Mn in Jan-26." | AMBIGUOUS | The "Capital Efficiency" slide frames the business against its own cash flow. FY25: CFO (168), CFI (255), CFF 423 (line 538-540). FY25 capex was debt-funded. FY26: borrowings rose 630 to 837 while the buy-back (340) and the FY25 dividend (97.7, results R297) went out. Net D/E rose 0.20 to 0.32. Roughly 200 Mn of FY26 payouts were funded by debt. Buy-back price was Rs 800 (results R368). CMP is 675.0 (line 636), 15.6% below it. Over FY25 to H1 FY27, cumulative CFO (488) covers investing (436), so the claim holds only on a multi-year view. A4: ask the capital-allocation rule that led to a debt-funded buy-back in a year when PAT was 55 Mn. |
| A3P-13 | F16 | R288-R291, R150, R170, R040, R055, R057, R052, R107, R409 | line 592, p22; line 489, 500, p18; line 427-437, p16 | "62     19.62%" (PAT chart FY26) / "Basic/Diluted EPS (INR per share) ... 4.28" | NEUTRAL-FACT | Label and definition reframes, all small. (1) The p22 chart labels FY26 "PAT" as 62. That figure is pre-exceptional. Filed PAT is 55.4 (results R114 554.05 lakhs). (2) FY26 EPS 4.28 is post-exceptional but sits under the pre-exceptional PAT row. (3) Deck "Total Expenses" (1,494) excludes D&A and finance cost. Filed Total Expenses are 1,534.2 (results R073). (4) Rounding plugs: Q2 FY27 finance cost 11 vs filed 11.8 (results R049), so YoY shows 83.3% vs a filed 93.7%. Depreciation 28 vs filed 28.5. H1 OCI -2 vs filed -1.35 (results R133). (5) Q2 has a YoY column only (line 427). No QoQ column, so the 5.2% QoQ revenue fall is not visible. |

FORWARD-SIGNAL (A4 questions): A3P-02, A3P-03, A3P-04, A3P-08, A3P-10.
AMBIGUOUS (A4 questions): A3P-05, A3P-09, A3P-11, A3P-12.

---

## 3. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | A3P-01: the Labour Code exceptional line persists at 0 in H1 FY27. R180, R182, R183 are rounding zeros (filed intangibles 2.71-2.86 lakhs, about 0.3 Mn). R184, R185, R224-R226 are header-row layout dashes. R271-R273 are rounding: each column's flows sum to 0 (FY25 -168-255+423; FY26 416-137-279; H1 240-44-196). Filed H1 net change "(0.78)" lakhs. Period-end cash is about 0.1 Mn on every date, a zero-cash sweep pattern. |
| F2 Standalone vs consolidated | N.A. | Presentation. Standalone only. Filed Note 4: no subsidiary, associate or JV (results R475). |
| F3 Shell-entity detection | N.A. | No consolidation (results R475). |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters in a deck. No components (results R475). |
| F5 Going concern / EoM tracking | N.A. | No EoM or going-concern language in the deck. No prior-quarter text. |
| F6 Forward-commitment mining | FINDING | 12 commitments registered (section 4). Status-bearing items: capacity expansion "completed" (A3P-02); export target (A3P-03); FY27 utilisation (A3P-04). Loop 1 adds 5 standing policies (section 6.4). |
| F7 Hedge mining | FINDING | A3P-05: "uncertain", "Likely FTA", "likely to improve", "evaluating". The disclaimer "subject to the applicable laws" (line 647) is boilerplate and not counted. Loop 1 claim hedges are logged in A3P-21. |
| F8 Tax forensics | PASS | Deck ETR: Q2 FY27 35/137 = 25.5%; H1 FY27 71/273 = 26.0%; FY24 25.8%; FY25 26.4%; FY26 24.4% (pre-exceptional). All within about 1 pt of 25.17%. The deck shows no earlier-year tax line. Pointer for the results-filing A3, outside deck scope: FY26 current tax 6.53 lakhs vs deferred 171.42 lakhs; Q2 FY26 current tax "(10.05)"; H1 FY27 cash-flow "Provision for Non-current Tax Assets" 73.46 lakhs. |
| F9 OCI forensics | FINDING | A3P-06: the Q1 FY27 remeasurement swing exceeds the full FY26 amount with the sign reversed. Immaterial in Rs. Verify assumptions at the AR. |
| F10 Share count and dilution | PASS | Share capital 130 / 126 / 126 (line 510). The change traces to the Jan-26 buy-back of 425,000 shares (line 304; results R370). Shares outstanding 12.6 Mn (line 639). Market cap 8,502.8 / 675.0 = 12.60 Mn, which ties. EPS is "Basic/Diluted" (line 500). Filed basic = diluted (results R148/R154 8.07). Spread is 0. No dilutive instruments. |
| F11 Net worth tie-out | PASS | 126 + 2,692 = 2,818 (filed 28,182.68 lakhs). 126 + 2,505 = 2,631 (filed 26,304.03). 130 + 2,890 = 3,020. H1 roll: 2,505 + TCI 200 - dividend 12.5 (results R296) = 2,692.5, which ties. FY26 roll leaves a residual of about 10.6 Mn (0.4% of net worth, below 5%). Candidate reconciling item: buy-back transaction costs, excluded from the Rs 34 Cr cap (results R477). |
| F12 Segment forensics | N.A. | The deck carries no segment data. The filing has one segment (results R471). Segment trends belong to the results A3. |
| F13 Board outcome | N.A. | The deck carries no board outcome. The same-day RPT land approval is logged under F16 (A3P-08) as a deck omission. |
| F14 Drafting inconsistencies | FINDING | A3P-07: auditor naming and tenure, typos, misspelt IR email, template disclaimer text, period mislabel. Loop 1: A3P-21. |
| F15 Entity list diffs | N.A. | The deck has no consolidation list. The filing names none (results R475). No prior deck. |
| F16 Dropped / reframed disclosures | FINDING | No prior deck exists, so dropped metrics are NOT ASSESSABLE. Cross-document and internal reframes logged: A3P-08 to A3P-13. Loop 1 claim tests: A3P-14 to A3P-20. Return-ratio chart R300-R307 stays unassigned and was not resolved. |
| F17 Concall silence audit | N.A. | Presentation, not a concall. No monitoring checklist on record. |

Blank checks: none. GATE A3: pass.

---

## 4. COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref (slide / line) | status word |
|---|---|---|---|---|
| C1 | Raw-material throughput capacity expansion, "with minimal capex" | done by 30-Sep-2026 | p4, lines 95-98 (LAYOUT_GARBLED) | completed |
| C2 | Add one new raw material (Oleo Chemicals only) to make value-added products / "Adoption of one more raw material to produce niche chemical" | undated | p4 lines 96-100; p21 lines 570-574 | initiated (proposal) |
| C3 | Raise capacity utilisation in FY27 on better raw-material availability after the duty cut | FY27 (by 31-Mar-2027) | p15, lines 410-412 | expected |
| C4 | Exports "initially by 25% and eventually at 50% of the sales" | undated | p21, lines 558-566 | aim |
| C5 | Enter new global markets; raise export share in all prime products | undated | p6, lines 157-158, 180-181 | underway |
| C6 | Product upgradation: low-titre linoleic acid for oil drilling; distilled dimer; fatty oil upgrade for heating | undated | p21, lines 558-570 | underway ("currently working on", line 549) |
| C7 | New products: bypass fat from PFAD; isostearic acid adoption in cosmetics | undated | p21, lines 558-566 | underway |
| C8 | Energy savings from an energy audit, "significant reduction in energy" (not quantified) | achieved | p21, lines 558-564 | completed |
| C9 | Substitute imported catalyst with domestic catalyst | undated | p21, lines 568-570 | underway |
| C10 | Scrubber system for air emissions, "in place in near future" | undated | p11, lines 319-321 | proposed |
| C11 | Buy-back of INR 340 Mn | Jan-26 | p10, line 304 (results R444, R445: settled 21-Jan-2026, extinguished 27-Jan-2026) | completed |
| C12 | US tariff level and EU/UK FTA "augers well for our export strategy" (external enabler) | undated | p4, lines 97-101 | expected |

---

## 5. DECK VS FILING RECONCILIATION (F16 support)

Deck Rs Mn vs filing Rs Lakhs x0.1. All lines tie within plus or minus 1 unit of rounding except where noted.

| Line | Deck | Filed (Rs Mn) | Result |
|---|---|---|---|
| Revenue Q2 FY27 / Q2 FY26 | 1,669 / 1,115 | 1,669.2 / 1,115.2 | ties |
| Revenue H1 FY27 / H1 FY26 / FY26 | 3,431 / 2,426 / 4,596 | 3,430.7 / 2,425.9 / 4,596.5 | ties |
| EBITDA Q2 FY27 (PBT + fin + D&A - OI) | 175 | 175.4 | ties |
| EBITDA H1 FY27 / H1 FY26 / FY26 | 354 / 94 / 216 | 354.0 / 94.1 / 216.2 | ties |
| Finance cost Q2 FY27 | 11 | 11.8 | rounding plug (A3P-13) |
| Depreciation Q2 FY27 | 28 | 28.5 | rounding plug |
| PBT / Tax / PAT Q2 FY27 | 137 / 35 / 102 | 136.5 / 34.8 / 101.7 | ties |
| PAT H1 FY27 / EPS | 202 / 16.02 | 201.8 / 16.02 | ties |
| PAT FY26 | 62 (pre-exceptional) | 55.4 (post) / 62.0 (pre) | label (A3P-13) |
| OCI H1 FY27 | -2 | -1.35 | rounding plug |
| PPE / CWIP / ROU, 30-Sep | 2,048 / 83 / 19 | 2,047.5 / 82.9 / 19.4 | ties |
| Inventory / Receivables / Cash and bank | 699 / 1,002 / 14 | 699.4 / 1,001.8 / 14.2 | ties |
| Other current assets | 85 | 44.5 + 0.2 + 39.6 HFS = 84.3 | ties; held-for-sale folded in (A3P-09) |
| Total assets | 3,984 | 3,984.3 | ties |
| Equity / Other equity | 126 / 2,692 | 126.0 / 2,692.3 | ties |
| Current borrowings | 686 | 686.5 | ties |
| Other current liabilities | 62 | 51.5 + 10.1 LHFS = 61.6 | ties; held-for-sale folded in (A3P-09) |
| NC liabilities (lease / prov / DTL) | 16 / 45 / 209 | 15.8 / 44.6 / 209.2 | ties |
| CFO / CFI / CFF H1 FY27 | 240 / (44) / (196) | 240.5 / (44.0) / (196.6) | ties |
| Net D/E H1 FY27 | 0.24 | 686.5 / 2,818.3 = 0.24 (borrowings, ex-lease, ex-cash) | ties |

---

## 6. ADDENDUM (loop 1): rows R458-R512

Scope: the 55 rows A1 appended (48 QUALIFIER, 7 FORWARD) and A2 registered in the ledger addendum. Checks run: F6, F7, F14, F16. Findings A3P-01 to A3P-13 are unchanged.

### 6.1 Reconciliation of the loop 1 rows

55 of 55 rows read at their ID and at the cited fulltext line. Ledger addendum reconciled 100%. Orphans: none.

Flag-set note: the coordinator listed CLAIM_TO_TEST on R466, R468, R474, R490, R494, R500, R501, R505. The ledger addendum carries CLAIM_TO_TEST on R462, R466, R468, R474, R483, R490, R492, R500, R501, R505. For R494 the ledger shows "RESTATED ... TEST". I tested the union, 11 rows.

A1 transcription defects (two-column merges; A4 should quote the fulltext, not the A1 row):
- R460 inserts "revenue" from the adjacent column (line 100, "Leading manufacturer ... overall revenue"). The fulltext claim reads: "by-products of vegetable oils which are generated in very small quantities of ~ 1.25% (for Acid Oil) and ~0.25% (for DOD) of soft oils processed" (lines 98-104).
- R467 takes "globally" from the adjacent column (lines 212-213, "lowest cost producer globally"). The fulltext reads: "Low cost of raw material as Fairchem purchases waste products from oil refineries" (lines 213-214). The deck also says sourcing is mostly within 500 km (line 228-232).
- R466 merges the heading "One of the Lowest Cost Producer ... Globally" (lines 209, 211) with the side text "enabling Fairchem to be the lowest cost producer globally" (lines 209-213). I test both wordings.

### 6.2 CLAIM_TO_TEST results

| Row | Claim (line) | Test against | Result | Finding |
|---|---|---|---|---|
| R462 | "Strong moat of secure and low-cost raw material supply" (206-208) | line 402-403 "higher raw material cost"; line 411-412 duty cut "likely to improve the availability of raw material"; R460 by-product is ~1.25% / ~0.25% of oil processed | Contradicted by the deck's own p15 text | A3P-14 |
| R466 | "One of the Lowest Cost Producer ... Globally" / "the lowest cost producer globally" (209-213) | EBITDA margin 10.78% / 7.96% / 4.70% / 10.32% (line 477); margin driver "lower imports" (line 406); peer data NOT FOUND in deck | Not supported. Margin pattern looks like a price-taker's | A3P-15 |
| R468 | "Efficient manufacturing process comparable to global peers" (216-217) | Same margin history (R124-R127) | Untestable without peer data; same pattern | A3P-15 |
| R474 | "on short payment cycles" (233-235) | Trade payables 83 / 110 / 113 (line 522); filed payables 1,127.52 lakhs vs H1 COGS 26,466.25 lakhs (results R215, R217, R033, R040) | Confirmed: about 8 days of H1 COGS, 11 days of FY26 COGS | A3P-16 |
| R483 | "Enjoy Leadership Position in the industry due to barriers to entry" (284) | R489 scope qualifier "for substantial part of the overall revenue" (294); R478 "Low switching cost of process lines" (255); no market-share data | Untestable; scope narrowed on the same slide | A3P-21 |
| R490 | "Position to market entire quantity of Prime Products it produces" (295) | Inventories 883 / 922 / 699 (line 521-522); filed FG/WIP drawdown Q1 1,598.10, Q2 287.81 lakhs (results R038, R037); Q2 revenue -5.2% QoQ | Consistent: no unsold build-up. Receivables rose (A3P-10) | A3P-17 |
| R492 | "positioned business well for continued growth and development" (299) | Revenue 6,215 / 5,379 / 4,596; PAT 405 / 220 / 62 (lines 471, 489); H1 FY27 PAT 202 | "Continued" growth conflicts with a 3-year decline. H1 is a recovery | A3P-21 |
| R494 | "Majority of the capacity expansion has been undertaken primarily through internal accruals" (303) | CFO (168) / 416 / 240; CFI (255) / (137) / (44) (lines 538-539); borrowings 630 / 837 / 686 (line 521) | Holds only on a cumulative view | Already A3P-12; no new ID |
| R500 | "Always be adequately capitalized" (313) | Total equity 3,020 / 2,631 / 2,818 (R221-R223); net D/E 0.02 / 0.20 / 0.32 / 0.24 (R292-R295) | Holds on level. Equity fell 13% in FY26 through the buy-back | A3P-19 |
| R501 | "Not overleverage the balance sheet" (315) | Net D/E as above; borrowings/EBITDA FY26 837/216 = 3.9x, H1 annualised 686/708 = 1.0x; finance cost 42 / 37 / 37 / 30 (line 483) | Level holds. FY26 debt/EBITDA stress. Finance cost anomaly | A3P-19, A3P-20 |
| R505 | "Low volatility in the cash flow generation" (323) | CFO (168) / 416 / 240 (line 538); CFO/PAT -0.8x / 6.7x / 1.2x; CCC 76 / 82 / 99 / 128 (line 600-603) | Contradicted by the deck's own cash-flow slide | A3P-18 |

### 6.3 New findings

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-14 | F16 | R462, R460, R502, R430, R388 | lines 206-208, p7; lines 402-403, 411-412, p15; lines 102-104, p4 | "Strong moat of / secure and low-cost / raw material supply" vs "likely to improve the availability of raw / material and in turn our capacity utilization" | AMBIGUOUS | The p7 moat claim says supply is secure and low-cost. The p15 text says revenue rose on "higher raw material cost". It also makes utilisation depend on better raw-material "availability". The input is a by-product of about 1.25% / 0.25% of oil refined (lines 102-104), so refinery throughput caps supply. Reading 1: supply is secure in access but capped in volume, so the moat is cost, not quantity. Reading 2: supply is the binding constraint, so the moat claim overstates. What separates them: the share of acid oil and DOD bought under long-term contract vs spot, and H1 raw-material tonnage vs capacity. A4: ask both. |
| A3P-15 | F16 | R466, R468, R488, R124-R127, R431 | lines 209-213 and 216-217, p7; line 477, p18; line 405-406, p15 | "the lowest cost / producer / globally" vs "10.78%  7.96%  4.70%  10.32%" | AMBIGUOUS | EBITDA margin fell from 10.78% to 4.70% over FY24-FY26 and recovered to 10.32% in H1 FY27. PAT margin hit 1.35% in FY26 (line 491). Management credits the recovery to "lower imports" (line 406). A global lowest-cost producer should hold margin when imports compete. This margin moves with import pressure, which is how a price-taker behaves. The deck gives no peer cost or margin data. Reading 1: lowest cost holds, but import-parity pricing passes the advantage to customers. Reading 2: the claim overstates the cost position. What separates them: conversion cost per tonne vs named peers, and FY26 spread per tonne vs import-landed price. Ties to A3P-11. |
| A3P-16 | F16 | R474, R240-R242, R296-R299 | lines 233-235, p7; line 522, p19 | "on an 'as-is-where-is' basis at the factory gate on short payment cycles" | NEUTRAL-FACT | Claim confirmed. Trade payables are 113 against 30-Sep receivables of 1,002 and inventory of 699. That is about 8 days of H1 COGS (filed). Filed MSE payables fell from 70.75 to 3.07 lakhs (results R216, R215). The business gets almost no supplier credit. So working capital grows with price inflation and lands on cash-credit borrowings (686). That is why the CCC (A3P-10) roughly equals inventory days plus receivable days. |
| A3P-17 | F16 | R490, R197-R199 | line 295, p10; lines 521-522, p19 | "Position to market entire quantity of Prime Products it produces" | NEUTRAL-FACT | Consistent with the numbers. Inventory fell 922 to 699 in H1. Filed FG/WIP inventories were drawn down in both quarters (Q1 1,598.10, Q2 287.81 lakhs). Volume looks supply-bound, not demand-bound, which supports A3P-04 and A3P-14. One caveat: receivables rose 47% (A3P-10), so part of what was "marketed" may sit on longer credit. The A4 question already sits under A3P-10. |
| A3P-18 | F16 | R505, R262-R264, R296-R299 | line 323, p11; line 538, p20 | "Low volatility in the cash flow generation" vs "(168)   416      240" | AMBIGUOUS | The governance policy conflicts with the deck's own cash flows. CFO swung from (168) in FY25 to 416 in FY26, a 584 Mn swing against PAT of 220 and 62. CFO/PAT ran -0.8x, 6.7x and 1.2x. H1 FY27 CFO rests on a one-off inventory release (A3P-10). The CCC has risen four periods in a row. A4: ask how management measures "volatility", and what CFO it expects in H2 once the inventory release stops. |
| A3P-19 | F16 | R500, R501, R221-R223, R292-R295, R237-R239 | line 313, 315, p11; line 521, p19; line 598-607, p22 | "Always be adequately capitalized" / "Not overleverage the balance sheet" | NEUTRAL-FACT | The level holds. Net D/E peaked at 0.32 (FY26). H1 FY27 interest cover is 354/30 = 11.8x. FY26 was the stress point. Borrowings were 3.9x EBITDA (837/216). Interest cover was 5.8x. Equity fell 3,020 to 2,631 because of the buy-back. The policy held on level but slipped on direction in the year of the debt-funded payout (A3P-12). |
| A3P-20 | F16 | R501, R136-R139, R092, R093, R237-R239 | line 483, p18; line 457, p17 (LAYOUT_OFFSET) | "Finance Cost  42  37  37  30" | AMBIGUOUS | H1 FY27 finance cost was 30, against 16 in H1 FY26 (+87.5%) and 37 for all of FY26. Borrowings meanwhile fell from 837 to 686. On average borrowings, the implied annualised cost is about 7.9% for H1 FY27 vs about 5.0% for FY26 (an inference from deck balances). Filed quarterly finance cost fell from 183.79 lakhs in Q1 to 118.05 lakhs in Q2 (results R050, R049). Candidate drivers: a rate reset, receivable discounting, or interest on tax. None is disclosed. A4: ask what drove the H1 finance cost, and the Q2 exit rate on cash credit. |
| A3P-21 | F14 | R460, R466, R464, R482, R465, R484, R483, R489, R492, R504, R472 | lines 102-104, p4 vs 137-139, p5; 209-213, p7; 284, 294, 299, p10; 320, p11; 228-232, p7 | "~0.25% (for DOD) of soft oils processed" vs "Hard Oil ... Deodorizer Distillate ... (0.25% by-product)" | NEUTRAL-FACT | Cumulative claim drafting, adding to A3P-07. (1) p4 ties DOD to soft oils (line 103-104). The p5 flow chart puts DOD under Hard Oil (Palm/Coconut) (lines 137-139). (2) The p7 heading hedges with "One of the Lowest Cost Producer" (line 209). Its own side text says "the lowest cost producer globally" (lines 210-213). (3) p7 and p10 repeat identical wording (R464/R482, R465/R484). (4) "Leadership Position ... due to barriers to entry" (line 284) sits beside the narrower "for substantial part of the overall revenue" (line 294) and "Low switching cost of process lines" (line 255). No market-share figure appears. (5) "continued growth" (line 299) conflicts with the FY24-FY26 decline: revenue 6,215 to 4,596, PAT 405 to 62. (6) "Transparent communications with all the stakeholders" (line 320) conflicts with the deck's omission of the same-day RPT (A3P-08). (7) Scope hedge: the 500 km sourcing claim applies "in case of domestic sales" (line 230). Other hedges: "Near-zero" (lines 260, 331); "Majority ... primarily" (line 303). |

Loop 1 FORWARD-SIGNAL: none new. Loop 1 AMBIGUOUS (A4 questions): A3P-14, A3P-15, A3P-18, A3P-20.

### 6.4 Commitment register additions (F6, standing policies)

| # | commitment | implied date | ref (slide / line) | status word |
|---|---|---|---|---|
| C13 | "Always be adequately capitalized" / "Not overleverage the balance sheet" | standing | p11, lines 313, 315 (R500, R501) | policy (tested A3P-19) |
| C14 | "Secure sources of sustainable raw material supply" | standing | p11, lines 316-318 (R502) | policy (tested A3P-14) |
| C15 | "Invest in backward and forward integration" | undated | p11, line 319 (R503); cross-ref C2 | policy |
| C16 | "Transparent communications with all the stakeholders" | standing | p11, line 320 (R504) | policy (see A3P-21 item 6) |
| C17 | "Low volatility in the cash flow generation" | standing | p11, line 323 (R505) | policy (tested A3P-18) |

R496 (capacity expansion "by evaluating market demand-supply scenario", line 305) is already covered in A3P-05. R498 (Zero Liquid Discharge) and R499 (GPCB disposal) are environmental status claims. Neither contradicts the deck. The scrubber remains C10.

---

```yaml
stage: A3-forensics
company: "FAIRCHEMOR"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
forensics_path: "runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_presentation.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3P-01", check: "F1", line: "deck 492-494 (p18) '-       -     7      0'", classification: "NEUTRAL-FACT", implication: "Labour Code exceptional line kept at 0 in H1 FY27; filing calls FY26 charge nonrecurring; watch for true-up when final rules notify"}
  - {id: "A3P-02", check: "F6", line: "deck 95-98 (p4) 'throughput capacity / expansion completed / with minimal capex'; 511 'CWIP 117 184 83'", classification: "FORWARD-SIGNAL", implication: "Capacity expansion completed; utilisation is now the volume swing; no capacity or utilisation figure disclosed"}
  - {id: "A3P-03", check: "F6", line: "deck 562-566 (p21) 'initially by 25% and eventually at 50% of the sales'; results line 479 Note 3", classification: "FORWARD-SIGNAL", implication: "Export target 25%-50% of sales vs filed 'almost all revenue from domestic sales'; basis and dates unstated"}
  - {id: "A3P-04", check: "F6", line: "deck 410-412 (p15) 'in turn our capacity utilization during the year'", classification: "FORWARD-SIGNAL", implication: "FY27-dated utilisation commitment with no baseline; untestable unless management gives a number"}
  - {id: "A3P-05", check: "F7", line: "deck 408-409 (p15) 'macros are uncertain due to middle east crisis'; 305 (p10) 'by evaluating market demand-supply scenario'", classification: "AMBIGUOUS", implication: "Hedged outlook; no expansion capex committed; FTA may cut import-parity margin as well as help exports"}
  - {id: "A3P-06", check: "F9", line: "deck 493 (p18) '(1) (1) 4 -2'; results line 257 Q1 FY27 '(51.28)' vs FY26 '49.86'", classification: "NEUTRAL-FACT", implication: "Single-quarter actuarial swing exceeds full prior year; about Rs 0.5 Cr; verify discount rate at FY27 AR"}
  - {id: "A3P-07", check: "F14", line: "deck 381-383 'audited by one of the Big 4 for the last 9 years'; 29, 582, 349, 673, 658, 399-401", classification: "NEUTRAL-FACT", implication: "Cumulative drafting looseness: auditor named KPMG vs filed B S R and Co, tenure predates 2019 CIN, typos, misspelt IR email, telecom boilerplate, H1 figure under Q2 heading"}
  - {id: "A3P-08", check: "F16", line: "results line 68 'purchase of 2 separate pieces of land (adjoining to the plant ...) from the Chairman & Managing Director ... and his relatives'; deck 305", classification: "FORWARD-SIGNAL", implication: "Deck omits same-day Rs 12.01 Cr promoter RPT land buy adjoining plant (2.7x H1 capex); likely next expansion site; RPT governance question"}
  - {id: "A3P-09", check: "F16", line: "deck 525/524 (p19) 'Other current assets'; results line 324 '395.67' AHFS, line 372 '101.00' LHFS", classification: "AMBIGUOUS", implication: "Held-for-sale group (39.6 Mn asset, 10.1 Mn liability) invisible in deck; pending disposal, future cash and gain/loss line"}
  - {id: "A3P-10", check: "F16", line: "deck 600 (p22) '128'; 521-524 receivables '861 681' to '1002'; results line 418 '2,230.80', line 421 '(3,200.20)'", classification: "FORWARD-SIGNAL", implication: "CCC 76-82-99-128 days; receivables +47% while Q2 revenue -5.2% QoQ; H1 OCF 240 leans on 223 Mn inventory release; H2 OCF has no inventory cushion"}
  - {id: "A3P-11", check: "F16", line: "deck 402-403 (p15) 'higher price realization primarily due to higher raw material cost and higher import finished product cost'; 405-406 'due to lower imports'", classification: "AMBIGUOUS", implication: "Price-led growth, no volume disclosed; 674 bps EBITDA gain = ~275 bps gross margin + ~401 bps fixed-cost leverage; import-parity artifact vs structural mix; separator = MT volume and spread per tonne"}
  - {id: "A3P-12", check: "F16", line: "deck 303-304 (p10) 'primarily through internal accruals' / 'buy-back of INR 340 Mn'; 538-540 (p20) FY25 '(168) (255) 423'; 636 '675.0'", classification: "AMBIGUOUS", implication: "Capital-efficiency framing vs debt-funded FY25 capex and ~200 Mn debt-funded FY26 payouts; buy-back at Rs 800 vs CMP 675; net D/E 0.20 to 0.32"}
  - {id: "A3P-13", check: "F16", line: "deck 592 (p22) '62     19.62%'; 500 (p18) EPS '4.28'; 427-437 (p16)", classification: "NEUTRAL-FACT", implication: "FY26 'PAT' chart is pre-exceptional (filed 55.4); deck Total Expenses excludes D&A and finance; rounding plugs (finance cost 11 vs 11.8, YoY 83.3% vs 93.7%); no QoQ column hides -5.2% QoQ revenue"}
  - {id: "A3P-14", check: "F16", line: "deck 206-208 (p7) 'secure and low-cost / raw material supply' vs 411-412 (p15) 'likely to improve the availability of raw / material'", classification: "AMBIGUOUS", implication: "Moat claim of secure supply vs admitted availability constraint and RM-cost-driven pricing; by-product share caps supply; separator = contracted vs spot share and RM tonnage vs capacity"}
  - {id: "A3P-15", check: "F16", line: "deck 209-213 (p7) 'the lowest cost / producer / globally'; 216-217 'comparable to global peers'; 477 (p18) '10.78%  7.96%  4.70%  10.32%'", classification: "AMBIGUOUS", implication: "Lowest-global-cost claim vs import-sensitive margin swing (10.78% to 4.70% to 10.32%); no peer data; separator = conversion cost per tonne vs peers and spread vs import-landed price"}
  - {id: "A3P-16", check: "F16", line: "deck 233-235 (p7) 'on short payment cycles'; 522 (p19) payables '83     110   113'", classification: "NEUTRAL-FACT", implication: "Claim confirmed: payables ~8 days of H1 COGS; no supplier credit, so price-led WC growth lands on cash-credit borrowings"}
  - {id: "A3P-17", check: "F16", line: "deck 295 (p10) 'Position to market entire quantity of Prime Products it produces'; 521-522 (p19) inventories", classification: "NEUTRAL-FACT", implication: "Consistent: inventory 922 to 699, FG/WIP drawn down both quarters; volume supply-bound not demand-bound; receivables caveat sits in A3P-10"}
  - {id: "A3P-18", check: "F16", line: "deck 323 (p11) 'Low volatility in the cash flow generation' vs 538 (p20) '(168)   416      240'", classification: "AMBIGUOUS", implication: "Policy contradicted by own CFO swing (CFO/PAT -0.8x, 6.7x, 1.2x) and rising CCC; H2 CFO without inventory release is the test"}
  - {id: "A3P-19", check: "F16", line: "deck 313/315 (p11) 'Always be adequately capitalized' / 'Not overleverage the balance sheet'; 521 (p19) borrowings '630    837   686'", classification: "NEUTRAL-FACT", implication: "Leverage policy holds on level (net D/E peak 0.32, H1 interest cover 11.8x); FY26 stress at 3.9x debt/EBITDA with equity cut by buy-back"}
  - {id: "A3P-20", check: "F16", line: "deck 483 (p18) 'Finance Cost  42  37  37  30'; 457 (p17) H1 FY26 '16'", classification: "AMBIGUOUS", implication: "H1 finance cost +87.5% YoY while borrowings fell 837 to 686; implied cost ~7.9% vs ~5.0% FY26 (inference); cause undisclosed (rate reset, receivable discounting, tax interest)"}
  - {id: "A3P-21", check: "F14", line: "deck 103-104 (p4) 'of soft oils processed' vs 137-139 (p5) 'Hard Oil ... (0.25% by-product)'; 209-213, 284, 294, 299, 320, 230", classification: "NEUTRAL-FACT", implication: "Claim drafting: DOD source inconsistent p4 vs p5; 'One of the Lowest' vs 'the lowest'; duplicate p7/p10 wording; unquantified leadership claim; 'continued growth' vs FY24-FY26 decline; 'Transparent communications' vs RPT omission"}
forward_signals: ["A3P-02", "A3P-03", "A3P-04", "A3P-08", "A3P-10"]
ambiguous: ["A3P-05", "A3P-09", "A3P-11", "A3P-12", "A3P-14", "A3P-15", "A3P-18", "A3P-20"]
commitments:
  - {commitment: "Raw-material throughput capacity expansion with minimal capex", implied_date: "completed by 30-Sep-2026", ref: "deck p4 lines 95-98 (LAYOUT_GARBLED)", status_word: "completed"}
  - {commitment: "Add one new raw material (Oleo Chemicals only) for value-added / niche chemical", implied_date: "undated", ref: "deck p4 lines 96-100; p21 lines 570-574", status_word: "initiated"}
  - {commitment: "Higher capacity utilisation in FY27 from raw-material availability after crude soya duty cut", implied_date: "FY27 (by 31-Mar-2027)", ref: "deck p15 lines 410-412", status_word: "expected"}
  - {commitment: "Exports initially by 25% and eventually 50% of sales", implied_date: "undated", ref: "deck p21 lines 558-566", status_word: "aim"}
  - {commitment: "Enter new global markets; raise export share in all prime products", implied_date: "undated", ref: "deck p6 lines 157-158, 180-181", status_word: "underway"}
  - {commitment: "Product upgradation: low-titre linoleic acid (oil drilling), distilled dimer, fatty oil for heating", implied_date: "undated", ref: "deck p21 lines 549, 558-570", status_word: "underway"}
  - {commitment: "New products: bypass fat from PFAD; isostearic acid in cosmetics", implied_date: "undated", ref: "deck p21 lines 558-566", status_word: "underway"}
  - {commitment: "Energy savings via energy audit (unquantified)", implied_date: "achieved", ref: "deck p21 lines 558-564", status_word: "completed"}
  - {commitment: "Substitute imported catalyst with domestic catalyst", implied_date: "undated", ref: "deck p21 lines 568-570", status_word: "underway"}
  - {commitment: "Scrubber system for air emissions", implied_date: "near future (undated)", ref: "deck p11 lines 319-321", status_word: "proposed"}
  - {commitment: "Buy-back INR 340 Mn", implied_date: "Jan-26", ref: "deck p10 line 304; results R444/R445", status_word: "completed"}
  - {commitment: "US tariff and EU/UK FTA support export strategy (external enabler)", implied_date: "undated", ref: "deck p4 lines 97-101", status_word: "expected"}
  - {commitment: "Always be adequately capitalized; not overleverage the balance sheet", implied_date: "standing", ref: "deck p11 lines 313, 315 (R500, R501)", status_word: "policy"}
  - {commitment: "Secure sources of sustainable raw material supply", implied_date: "standing", ref: "deck p11 lines 316-318 (R502)", status_word: "policy"}
  - {commitment: "Invest in backward and forward integration", implied_date: "undated", ref: "deck p11 line 319 (R503)", status_word: "policy"}
  - {commitment: "Transparent communications with all the stakeholders", implied_date: "standing", ref: "deck p11 line 320 (R504)", status_word: "policy"}
  - {commitment: "Low volatility in the cash flow generation", implied_date: "standing", ref: "deck p11 line 323 (R505)", status_word: "policy"}
gate_a3: pass
blank_checks: []
analyst_note: "Core read: H1 growth is price-led in management's own words (line 402). The deck has no volume, capacity or utilisation figure, so the 674 bps EBITDA gain cannot be split into spread and volume. Filed cost lines put about 275 bps in gross margin and about 401 bps in fixed-cost leverage on price-inflated revenue. That leverage reverses if import parity falls through the FTA or the duty cut. Second thread: working capital. CCC is 128 days. Receivables rose 47% since March while Q2 revenue fell 5% QoQ. H1 OCF of 240 Mn leans on a 223 Mn inventory release. Third: the deck omits the same-day promoter land purchase (Rs 12.01 Cr, adjoining the plant) while it calls capacity expansion 'evaluating'. A1 caveat: p19 ORDER_INFERRED rows mix line items across periods; A4 should use filing labels. R300-R307 stay unassigned. Deck and filing reconcile within rounding. Loop 1: the deck's own CFO, raw-material and margin lines contradict three claims (low cash-flow volatility, secure supply, lowest global cost)."
```
