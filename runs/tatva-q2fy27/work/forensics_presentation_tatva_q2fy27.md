# A3 FORENSIC NOTES: TATVA Q2 FY27, doctype PRESENTATION (Updated Investor Presentation, 42 pp)

Inputs read (no source access):
- A1 structured: runs/tatva-q2fy27/extracted/tatva-presentation-q2fy27-structured.md (R001-R738, read in full)
- A1 fulltext: runs/tatva-q2fy27/extracted/tatva-presentation-q2fy27-fulltext.md (lines 1-1110, read in full, including header version diff and image transcriptions L1106-L1110)
- A2 ledger: runs/tatva-q2fy27/work/ledger_presentation_tatva_q2fy27.md (738 row IDs, 5 version-diff units, 24 superseded IDs)
- Prior-quarter fulltext: none supplied
- Monitoring checklist: runs/tatva-q2fy27/work/notion-brief.md sections 4, 5, 7, 8; companies/TATVA.md ACTIVE TRIPWIRES. These are MEMORY, not evidence. Every number that comes from them is tagged [memory].

Conventions. Rs Mn as printed (x0.1 = Rs Cr). "[A3 computation]" = arithmetic on deck figures only. "[A3 inference]" = a reading of that arithmetic. Line numbers are fulltext lines. p = PDF page (footer page = PDF page minus 2).

## 0. LEDGER RECONCILIATION

| Item | Count | Status |
|---|---|---|
| Ledger row IDs | 738 | 738 read at structured ID and fulltext line; 100% |
| Version diff units V1-V5 | 5 | all read (L16-L19, L23, L34, L41-L49, L65-L66, L76-L81, L397-L415) |
| Superseded IDs (R165-R169, R622-R627, R642-R650, R692-R695) | 24 | read; treated as non-evidence; successors R714-R738 used |
| ZERO_STANDING rows (R288, R289, R291, R292, R293, R449) | 6 | all assessed under F1 |
| LABEL_MISMATCH rows (R543, R550) | 2 | resolved arithmetically under F14 |
| CHART_ORDER_UNRESOLVED p26 (R558-R580) | 23 | kept unattributed, not used for period claims |

Pipeline notes (A1/A2 data-integrity items; none blocks this stage; none needs the source):
- PN-1. p26 ESS chart prints "165" twice (L758 and L762). The structured file has one row (R577, L758). The L762 print has no row. The A2 ledger states MISSING_FROM_STRUCTURED: none. p26 shows 24 numeric prints and the structured file holds 23 rows.
- PN-2. R578 ("132") cites L751. At L751 the print is "1,132" (R568). The standalone "132" is at L763.
- PN-3. Off-by-one line cites: R031 "60%-100%" is at L137 (cited L138). R032 "more than 100%" is at L140 (cited L139).
- PN-4. p15/p16 right-hand column block (FY24-H1FY27) is layout-scrambled. The FY26 P&L column sits one row low (L437-L442). A1's period mapping agrees with A3's re-read. Every P&L and balance-sheet subtotal ties (see F11), so the mapping holds.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-P-01 | F16 | V1-V5; R002, R006, R009, R010, R012, R014-R019, R171, R207, R217 | p1 L23, L41, L45, L65-66; p2 L76-L81; header L16-L19 | "there were typographical errors in page no. 12" / "no changes in other financial numbers" | AMBIGUOUS | Same-day restatement. Original Ref 00056, signed 18:05:26. Updated Ref 00057, signed 20:54:24 (about 2h49m later). Two H1FY27 ratios changed: RoE 2.6% to 6.3%, Debt/EBITDA 4.30 to 1.16. Note (2) "annualized" was added. Both changes make the ratios look better. Neither looks like a keystroke error. [A3 computation] Earlier 2.6% = Q2 PAT 215 / closing net worth 8,146.51 = 2.64%. Earlier 4.30 = H1 debt 1,699.95 / H1FY26 EBITDA 395 = 4.30. [A3 inference] These look like wrong-cell spreadsheet links: a disclosure-control weakness, not a data change. Timing [memory]: the call was at 17:00 IST, so the original deck was filed about 1h05m after the call started. Any ratio quoted on the call may be on the original basis. |
| A3-P-02 | F16 | R203-R207, R014, R193-R197, R438-R444, R287 | p14 L397-L401; p2 L78 | "6.3%" (RoE H1FY27, updated) | AMBIGUOUS | The corrected RoE does not tie to the deck's own figures. PAT / closing net worth reproduces FY23 8.8% (454.87/5,147.91), FY24 4.1% (303.54/7,370.82) and FY25 0.8% (57.13/7,388.24). On that basis FY26 = 420.54/7,817.59 = 5.4% (deck prints 7.2%). H1FY27 = 374.32/8,146.51 = 4.6%, or 9.2% annualised (deck prints 6.3%). [A3 inference] FY26 and H1FY27 fit pre-tax profit before exceptional items / closing net worth, truncated (570.09/7,817.59 = 7.29%; 513.69/8,146.51 = 6.31%). The correction did not touch FY26 7.2%. On a like-for-like basis the FY25-to-FY26 RoE recovery is about 1.8 pp smaller than the chart shows. A4: ask for the RoE formula for each column. |
| A3-P-03 | F16 | R213-R217, R016, R019, R171, R183-R187, R178-R182, R445-R451, R466-R472 | p14 L407-L415 | "(2) Debt to EBITDA is annualized figure." | NEUTRAL-FACT | The chart uses two EBITDA bases. [A3 computation] FY23-FY25 tie to EBITDA including other income: 1,702.57/663.25 = 2.57; 143.01/757.05 = 0.19; 363.88/365.28 = 1.00. FY26 and H1FY27 tie to EBITDA excluding other income: 1,203.73/931.58 = 1.29; 1,699.95/(729.85 x 2) = 1.16. The switch raises the later ratios, so the direction is conservative. It is still a basis change inside one chart, at the same FY26 column where the RoE basis changes (A3-P-02). Net debt/EBITDA, annualised, excluding other income = (1,699.95 - 152.05)/1,459.70 = 1.06x (FY26 1.20x). That is still above the 0.65x monitoring band [memory]. |
| A3-P-04 | F1 | R288, R289, R290, R291, R292, R293, R294, R287, R301 | p15 L437-L438 (FY24-FY26 dashes, H1 13.18), L449 (FY21-FY23) | "Exceptional items - - 35.87" ... "13.18" | AMBIGUOUS | The line was nil for FY24, FY25 and FY26. In H1FY27 it carries a 13.18 charge (513.69 - 13.18 = 500.51 PBT). The deck does not say what it is. [A3 computation] p12 PBT Q1 211 + Q2 289 = 500, which equals H1 500.51, so the charge sits in Q1 and Q2 is about nil. This fits the Q1 Rs 1.32 Cr item [memory]. The Q1 question on its nature stays OPEN for a second quarter. A4: ask what it is and whether it recurs. |
| A3-P-05 | F1 | R449, R445-R451, R466-R472, R359-R360 | p16 L490 (FY25 "-"), L494, L509, L517 | "(i) Long-term borrowings" (FY25 "-"; FY26 50.10; H1 44.65) | FORWARD-SIGNAL | The term-debt line was nil in FY25. It came back small in FY26 (50.10) and is now 44.65. Short-term borrowings are 1,655.30, or 97% of total debt of 1,699.95. Short-term borrowings rose 501.67 in H1, all short-term. The Dahej-III Rs 200 Cr build [memory] does not yet show in long-term debt. Expect a term-loan draw under the Rs 1,000 Cr borrowing ceiling [memory]. Leverage then rises from 1.06x net (A3-P-03) before the new capacity earns. |
| A3-P-06 | F6 | R034, R035, R031, R032, R033 | p6 L136-L141 | "We expect it to normalise withing the third quarter." | FORWARD-SIGNAL | A dated commitment, due by 31-Dec-2026. Q2 cost pressure: solvents +60%-100% (L137), freight +100% on some US and Europe lanes (L140). Management already sees "a gradual reversal" (L140). Q3 test: EBITDA margin should recover from 18.7% (407/2,173). If it does not, the "temporary" reading fails (A3-P-13). |
| A3-P-07 | F6 | R036, R037, R508, R509, R066, R065 | p6 L141-L142; p18 L543 | "We foresee the revenue trend growth with similar momentum over the next quarters and EBITDA margin to resume its healthy trajectory." | FORWARD-SIGNAL | The guidance has no number. FY27 numbers are not restated: revenue +25-30%, EBITDA margin 20-22% [memory]. H1 revenue grew 60% (R070), so the revenue guide looks stale. [A3 computation] If H2 revenue = 2 x Q2 = 4,346, then FY27 EBITDA margin of 20-22% needs an H2 margin of 20.9%-24.7%, against 19.0% in H1 and 18.7% in Q2. Capacity: Q2 annualised revenue = 8,692 Mn (Rs 869 Cr). That is already at or above the Q1-call ceiling of Rs 800-850 Cr for the existing footprint [memory], with 791 KL at 31-Mar-2026 (R508). Jolva commissions Q3-Q4 FY28 [memory]. A4: ask how "similar momentum" continues before then (price, mix, debottlenecking?). |
| A3-P-08 | F6 | R053, R054, R055, R359, R360, R374 | p8 L194-L197; p16 CWIP | "our new greenfield project is progressing in line with the planned schedule" | FORWARD-SIGNAL | The deck does not name the project or state the schedule, capex or next milestone. The monitoring GREEN test (equipment PO by Q3 FY27 [memory]) cannot be graded from the deck. The only number is CWIP: 233.48 to 428.27, +194.79 (Rs 19.5 Cr). That is about 10% of the Rs 200 Cr budget [memory] since the 20-Jul groundbreak. Other non-current assets fell 81.28, possibly capital advances moved to CWIP [A3 inference]. |
| A3-P-09 | F6 | R045, R541, R542, R716, R519 | p7 L167-L169; p23 L674; L1106 | "hybrid-battery application is progressing towards commercialisation" | FORWARD-SIGNAL | The deck gives no date. The Q1 call gave "initial Oct-Nov CY2026" [memory]. [A3 computation] ESS Q2 = 3% x 2,173 = about 65 (plus or minus 11 for rounding). Q1 = 132 - 65 = about 67 (Q1 63 per [memory]). ESS was flat QoQ. The FY27 ESS guide of Rs 40-50 Cr [memory] needs 268-368 in H2, at least 2.0x H1. The CMD's "path of consistent growth" for energy storage (L123-L124) is not visible QoQ. |
| A3-P-10 | F6 | R048, R049, R719-R724, R617 | p7 L176-L179; p29 L1108 | "accelerate work on other products in our development pipeline" | FORWARD-SIGNAL | R&D capital and revenue expenditure (image, L1108): FY23 254.67, FY24 101.95, FY25 128.39, FY26 78.32, H1FY27 45.89. [A3 computation] As a share of revenue: H1FY27 1.19% (45.89/3,843.75), FY26 1.55%, FY25 3.35%. In rupees H1 annualised is 91.8, up 17% on FY26. As a share of revenue it keeps falling. The watch item "FY27 R&D <2% of revenue for a second year" [memory] is on course to fire at FY27 close. The "accelerate" language is not matched by spend intensity. |
| A3-P-11 | F7 | R056, R031 | p9 L207-L208; p6 L137 | "customer pricing adjusted progressively where appropriate" | FORWARD-SIGNAL | A hedge on cost pass-through. With solvent costs +60%-100%, "progressively where appropriate" means part of the cost was not passed on in Q2. If solvent normalisation (A3-P-06) slips, the hedge says Q3 margin carries the cost. A4: ask what share of the solvent increase was recovered in Q2 and how long the contract repricing lag is. |
| A3-P-12 | F7 | R050, R051, R052 | p8 L185-L192 | "a segment whose contribution we are working patiently to build" | NEUTRAL-FACT | A timing hedge. It fits "commercialisation not before Q4 CY2028" [memory]. None of the three semiconductor conversion conditions shows in the deck: no signed supply agreement or named design-in, no dedicated capex line, no booked segment revenue [memory]. All five products are still in "development, validation and customer qualification" (L186). |
| A3-P-13 | F7 | R029, R030, R078, R126, R129, R130 | p6 L133-L135; p12 L329-L330 | "EBITDA has remained at nearly similar levels primarily due to two temporary phenomena" | AMBIGUOUS | Management calls the margin shortfall temporary. The 20-22% band is not restated. "Similar levels" means margin: EBITDA itself rose 26% QoQ (323 to 407), while margin went from 19.3% to 18.7%. The cost-leverage claim ("decrease in employee cost by 2% accompanied by decrease in other expenses by 2%", L134) cannot be checked, because the deck has no Q1/Q2 cost split. A4: check the claim against the results filing. Ask whether the 20-22% FY27 band still stands. |
| A3-P-14 | F12 | R714-R718, R524, R531, R542, R549, R065, R066, R162, R715 | p13 L1106; p20 L582; p21 L614; p23 L674; p24 L705 | "SDA 45%" (Q2FY27 split) | FORWARD-SIGNAL | Q2 growth came mostly from SDA. [A3 computation] Q2 = split % x 2,173; Q1 = H1 - Q2: PTC 456 vs 425 (+7%); SDA 978 vs 568 (+72%, range +67% to +78% with rounding); ESS 65 vs 67 (flat); PASC 652 vs 595 (+10%). SDA supplied about 410 of the 502 QoQ revenue gain (about 80%). The Q1 figures agree with [memory] within rounding. SDA share: 45% in Q2, against 41% in FY26 and about 34% in Q1. The "similar momentum" guide (A3-P-07) rests mainly on Euro 7 SDA demand holding up. Customer 1 is 36% of revenue [memory]. Whether Customer 1 is an SDA buyer is NOT FOUND. Segment assets and liabilities are not disclosed. Checklist #3 (SDA FY27 up 20%+ to Rs 250-300 Cr): H1 Rs 154.6 Cr against FY26 Rs 204.5 Cr, ahead of pace. |
| A3-P-15 | F14 | R542, R543, R549, R550, R524, R531 | p23 L676; p24 L707 | "Revenue in Q1FY27" | NEUTRAL-FACT | Wrong period label. [A3 computation] 881 + 1,546 + 132 + 1,247 = 3,806, plus Others about 38 = 3,844 = H1 revenue. PASC 1,247 would be 75% of Q1 revenue (1,671), which is not possible. Both values are H1FY27. The "Updated" filing corrected only p14 and left these two labels wrong. The cover letter says steps were taken against recurrence (L48-L49). This adds to the disclosure-control point in A3-P-01. |
| A3-P-16 | F14 | R438-R444, R503, R361-R367 | p16 L503 | "Tangible net worth" | NEUTRAL-FACT | The label is printed on total equity: 233.92 + 7,912.59 = 8,146.51. Intangibles (65.46) are not deducted. Tangible net worth would be 8,081.05. The difference is immaterial (0.8%). |
| A3-P-17 | F14 | R707, R708, R712 | p41 L1087; p42 L1101; L80, L233, L461 | "the COVID-19 pandemic" / "Copyright ©2021" / "EBIDTA" | NEUTRAL-FACT | Stale boilerplate: the safe harbour still cites COVID-19, the copyright year is 2021, and "EBIDTA" is misspelt on p2, p11 and p15. Each is immaterial. With A3-P-01 and A3-P-15 they form one governance data point: the deck is not checked closely before filing. |
| A3-P-18 | F14 | R734-R738 (successors of R692-R695) | p40 L1067-L1072 vs L1110 | text layer "FPI 19.58%" / image "PUBLIC 19.58%, FPI 4.38%, OTHERS 1.15%" | NEUTRAL-FACT | The text layer puts 19.58% next to the FPI label. The approved render (R736-R738) gives it to PUBLIC. A2 rules make the image successor govern. The FPI figure matters for the ownership read. Claude web should check it against the NSE Sept 2026 shareholding pattern. Promoter 72.02% ties to the AGM promoter block of 16,846,963 / 23,392,055 shares [memory]. |
| A3-P-19 | F17 | R382-R395, R473-R479, R396-R402, R445-R472, R075/R123 | p15-p16 (no cash flow slide); p16 L485-L489, L494-L496 | (absence) the deck carries P&L (p15) and balance sheet (p16) only | AMBIGUOUS | Lean bear. Cash conversion (checklist #1, thesis-broken trigger (a)) is not addressed. CFO is NOT FOUND in the deck. [A3 computation, balance-sheet proxy, not CFO] H1 net working capital rose 806.76: inventory +528.36, receivables +593.46, other current assets +7.20, payables -272.78, other current liabilities -49.48. That is more than H1 EBITDA of 729.85. Debt rose 496.22 and cash rose 64.14. Sources and uses balance to 1,168.38 (see F11). Receivable days = 1,783.77/(3,843.75 x 2) x 365 = 85 days (FY26 consolidated 86 [memory]). The 185-day leg of trigger (a) is not met on consolidated figures. The CFO leg needs the results-filing cash flow statement. This is the second quarter without cash commentary (Q1 call [memory], Q2 deck). If the call is also silent and CFO is weak, it becomes CONFIRMATORY-NEGATIVE. |
| A3-P-20 | F17 | R005-R012, R046-R047, R541-R552, R516 | p6-p9 CMD; p7 L174 | "our pharma product beginning to contribute" | AMBIGUOUS | Several open Q1 items and guidance numbers are not in the deck (table in section 4). The deck uses the singular "pharma product". The Q1 call guided three molecules in FY27 with two more by Q3 end [memory]. The deck says nothing on the two. A4: turn each silent row into a question; the call A3 grades the call. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 6 ZERO_STANDING rows read. The exceptional-items line was nil for 3 years and now holds an undisclosed 13.18 charge (A3-P-04). The long-term borrowings line was nil in FY25 and has come back while debt is 97% short-term (A3-P-05). |
| F2 Standalone vs consolidated | N.A. | The deck is consolidated only (p11-p16). No standalone columns. |
| F3 Shell-entity detection | N.A. | No standalone cost lines to compare. Subsidiaries are named only (R633, R634). |
| F4 Unaudited contribution ratio | N.A. | No auditor report in a presentation. H1FY27 columns are marked "Unaudited" (R344, R501). |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph in a presentation, and no prior deck. |
| F6 Forward-commitment mining | FINDING | 12 commitments registered (section 3). The dated one is solvent/freight normalisation within Q3 (A3-P-06). Five findings carry forward signals (A3-P-06 to A3-P-10). |
| F7 Hedge phrase mining | FINDING | Lexicon hits: "where appropriate" (L208), "temporary" (L135), "intended" (L170), "We believe" x6, "working patiently" (L191). Three findings (A3-P-11 to A3-P-13). The safe harbour (L1081-L1092) is boilerplate. |
| F8 Tax forensics | PASS | Run on the p15 tax line. H1FY27 ETR = 126.19/500.51 = 25.2%, against the 25.17% statutory rate. From p12 (rounded): Q2 about 25.6%, Q1 about 24.2%. No deferred-tax split and no earlier-year tax line in the deck. The FY23 credit (7.08) is history. |
| F9 OCI forensics | N.A. | No OCI line in the deck. The 45.40 gap in other equity (F11) may include OCI. |
| F10 Share count and dilution | PASS | 2,33,92,055 shares (R700) x Rs 10 = 233.92 = equity capital (R430), unchanged since FY24 (after the Aug-2023 QIP, R673). H1 EPS 16.00 = 374.32/23.392. Market cap 1,784.20 x 23.392 = 41,736 (R697) ties. Diluted EPS is not shown, so the basic-diluted spread cannot be trended. |
| F11 Reserves and net-worth tie-out | PASS | 233.92 + 7,912.59 = 8,146.51 (R444). Totals tie: assets 6,499.02 + 4,688.28 = 11,187.30, and equity plus liabilities 8,146.51 + 85.51 + 2,955.28 = 11,187.30. FY26 also ties. H1 sources and uses balance at 1,168.38. Other equity rose 328.92 against PAT of 374.32. The 45.40 gap (0.56% of net worth) is under 5%; candidate items are an FY26 final dividend paid in H1 (about Rs 1.94/share) and OCI/FCTR. CRISIL A-/Stable (R516) gives no net-worth number to compare. |
| F12 Segment forensics | FINDING | Product-category revenue only; segment assets and liabilities are not disclosed. Q2 split derived: SDA-led quarter, ESS flat (A3-P-14). |
| F13 Board outcome beyond results | N.A. | The presentation has no board outcome. p39 lists six directors with no term dates. The 28-Sep AGM MD dissent [memory] is not in the deck. |
| F14 Drafting inconsistencies | FINDING | Wrong period labels left uncorrected in the Updated deck (A3-P-15). "Tangible net worth" label (A3-P-16). Stale boilerplate (A3-P-17). p40 attribution conflict (A3-P-18). |
| F15 Entity list diffs | N.A. | No consolidation list and no prior deck. Entities named: Tatva Chintan USA Inc., Tatva Chintan Europe BV (R633, R634; p38 milestones R660, R665). |
| F16 Dropped and reframed disclosures | FINDING | Same-day restatement of two flattering ratios called "typographical" (A3-P-01). The corrected RoE still does not tie (A3-P-02). Debt/EBITDA mixes bases (A3-P-03). No prior deck, so no dropped-slide diff is possible. |
| F17 Silence audit | FINDING | Run as a deck-level audit against the supplied checklist; the concall A3 grades the call. 18 rows (8 checklist items plus 10 open Q1 items and guidance numbers): 3 addressed (2 only in part), 3 partial, 12 not addressed or not restated (section 4). Cash conversion silent for a second quarter (A3-P-19). |

GATE A3: every check marked. blank_checks: none.

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C1 | Solvent prices and freight "expect it to normalise withing the third quarter" | by 31-Dec-2026 (Q3 FY27) | p6 L140-L141 (R034, R035) | underway ("seeing a gradual reversal", L140) |
| C2 | Revenue "growth with similar momentum over the next quarters" | Q3-Q4 FY27 | p6 L141 (R036) | initiated |
| C3 | "EBITDA margin to resume its healthy trajectory" (no number) | Q3 FY27 onward | p6 L142 (R037) | initiated |
| C4 | "customer pricing adjusted progressively where appropriate" | undated | p9 L208 (R056) | underway |
| C5 | ESS "hybrid-battery application is progressing towards commercialisation" | undated in deck (Oct-Nov CY2026 initial per Q1 call [memory]) | p7 L168 (R045) | underway |
| C6 | ESS "additional products are being scaled up for energy-storage applications" | undated | p7 L169 (R045) | underway |
| C7 | Pharma product "beginning to contribute" | Q2 FY27 | p7 L174 (R047) | completed (first molecule; two more by Q3 end per [memory] not mentioned) |
| C8 | "accelerate work on other products in our development pipeline ... piloting, process development ... commercialisation" | undated ("years ahead", L179) | p7 L176-L179 (R048, R049) | initiated |
| C9 | Semiconductor: five products in "development, validation and customer qualification" | undated ("years ahead", L190) | p8 L185-L191 (R051, R052) | underway |
| C10 | Greenfield "progressing in line with the planned schedule" | schedule not stated (commissioning Q3-Q4 FY28 [memory]) | p8 L194 (R054, R055) | underway |
| C11 | "Capex to boost the capacities and pave the way for higher revenues" | undated | p34 L936-L940 (R638) | underway (boilerplate) |
| C12 | Filing errors: "have taken necessary steps to prevent their recurrence" | next filing (Q3 FY27 deck) | p1 L48-L49 (R009, R010) | completed (claimed; A3-P-15 shows uncorrected labels in this same filing) |

## 4. SILENCE AUDIT: WHAT THE DECK DOES NOT ADDRESS (F17, deck level)

Count = consecutive quarters of silence in management documents seen so far. No prior deck was supplied, so a deck-only count starts at 1. Where [memory] records Q1 call silence, the count is 2.

| Checklist / open item [memory] | Deck status | Evidence | Consecutive silence |
|---|---|---|---|
| #1 Cash conversion: CFO/EBITDA, receivable days, ECL vs concentration | NOT ADDRESSED | No cash flow slide. Balance-sheet proxy: net WC +806.76 > EBITDA 729.85; receivable days about 85 (A3-P-19) | 2 (Q1 call, Q2 deck) |
| #2 ROCE above 8% rising to 15% | NOT ADDRESSED | Deck shows RoE only (p14). [A3 computation] pre-tax ROCE annualised = (513.69 + 47.90) x 2 / (8,146.51 + 1,699.95) = 11.4% | 1 |
| #3 SDA FY27 up 20%+ to Rs 250-300 Cr | ADDRESSED | H1 SDA 1,546 (R531); Q2 share 45% (R715) | 0 |
| #4 EBITDA margin 20-22%, RED below 18% | PARTIAL | Band not restated; "resume its healthy trajectory" (L142). H1 19.0%, Q2 18.7% | 1 (band not restated) |
| #5 Dahej-III milestones (equipment PO by Q3 FY27) | PARTIAL | "progressing in line with the planned schedule" (L194), no milestone; CWIP +194.79 | 1 |
| #6 Rating no downgrade; net debt/EBITDA under 0.65x | ADDRESSED (rating) / PARTIAL (leverage) | CRISIL A-/Stable & A2+ (L563). Gross 1.16x (L411); net 1.06x [A3 computation], above band | 0 / 1 |
| #7 Standalone PBT, parent profit share | NOT ADDRESSED | Consolidated-only deck | 1 |
| #8 Peer demand tone; promoter pay vs PAT | NOT ADDRESSED | p36 industry slide generic | 1 |
| Q1 Q1: nature of Rs 1.32 Cr exceptional | NOT ADDRESSED | H1 line 13.18, no note (A3-P-04) | 2 |
| Customer 1 at 36% of revenue and receivables | NOT ADDRESSED | Customer slide is a logo image (R636) | 2 (AR question, Q2 deck) |
| Subsidiary receivables Rs 25 to 61 Cr | NOT ADDRESSED | Consolidated only | 2 |
| R&D at 1.58% vs semiconductor pipeline | ADDRESSED (number), NOT ADDRESSED (explanation) | H1 45.89 = 1.19% of revenue (L1108); no commentary (A3-P-10) | 1 |
| Rs 1,000 Cr borrowing ceiling use | NOT ADDRESSED | Long-term debt 44.65; no funding plan (A3-P-05) | 2 |
| Two more pharma molecules by Q3 end | NOT ADDRESSED | "our pharma product" singular (L174) | 1 |
| FY27 revenue growth 25-30% | NOT RESTATED | H1 +60% (R070); "similar momentum" (L141) | 1 |
| ESS FY27 Rs 40-50 Cr; hybrid battery Oct-Nov CY2026 | PARTIAL | No number, no date (L168); ESS flat QoQ (A3-P-09) | 1 |
| Capacity ceiling Rs 800-850 Cr on existing footprint | NOT ADDRESSED | Q2 annualised Rs 869 Cr (A3-P-07) | 1 |
| Semiconductor conversion (supply agreement, capex line, revenue) | NOT ADDRESSED | "working patiently" (L191) (A3-P-12) | 1 |

Tripwire read (companies/TATVA.md), deck evidence only:
- Falsification (a), CFO negative plus receivable days above 185: not fired on the days leg (about 85 consolidated). CFO leg NOT FOUND in the deck.
- ROCE below 8% by FY28: not testable from the deck (RoE only). A3 pre-tax proxy 11.4%.
- Jolva 4th slip: not fired ("in line with the planned schedule", L194).
- Rating below BBB+/Stable: not fired (A-/Stable, L563).
- Peers soft vs Tatva recovery: deck silent.

## 5. QUESTIONS SEEDED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
1. A3-P-01/02: Give the formula for RoE and Debt/EBITDA for each p14 column. Why were the original values wrong? Which basis was used for any ratio quoted on the call?
2. A3-P-04: What is the 13.18 exceptional charge? Will it recur?
3. A3-P-05/08: Dahej-III spend to date, term-loan sanction and draw schedule, and peak net debt/EBITDA.
4. A3-P-06/11/13: What share of the Q2 solvent increase was recovered in price? Does the FY27 20-22% EBITDA band still stand? H2 needs 20.9-24.7%.
5. A3-P-07/14: How does revenue keep "similar momentum" at about the existing-footprint ceiling before Jolva? How much of Q2 growth was price and how much volume? How durable is the SDA order book?
6. A3-P-09: ESS was flat QoQ. Is the Rs 40-50 Cr FY27 guide intact? What is the hybrid-battery date?
7. A3-P-10: Why did R&D intensity fall to 1.2% while the pipeline is said to "accelerate"?
8. A3-P-19: H1 CFO and CFO/EBITDA. Net WC rose by more than H1 EBITDA: inventory build for SDA orders, or slow collection?
9. A3-P-20: Status of the two further pharma molecules due by Q3 end.

## 6. YAML BLOCK

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatva-q2fy27/work/forensics_presentation_tatva_q2fy27.md"
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
  F9: N.A.
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-P-01", check: "F16", line: "p1 L41, L45, L65-66; p2 L76-81", classification: "AMBIGUOUS", implication: "Same-day restatement (18:05 to 20:54) of RoE 2.6->6.3% and Debt/EBITDA 4.30->1.16, called typographical; both flattering; earlier values tie to wrong cells (Q2 PAT/NW 2.64%; H1 debt/H1FY26 EBITDA 4.30); original filed after 17:00 call start [memory]"}
  - {id: "A3-P-02", check: "F16", line: "p14 L397-401", classification: "AMBIGUOUS", implication: "Corrected RoE 6.3% fails PAT/closing NW basis that ties FY23-FY25; on that basis FY26 5.4% (printed 7.2%), H1 4.6% (9.2% annualised); FY26/H1 fit pre-tax PBEIT/NW truncated"}
  - {id: "A3-P-03", check: "F16", line: "p14 L407-415", classification: "NEUTRAL-FACT", implication: "Debt/EBITDA uses EBITDA incl other income FY23-FY25, excl other income FY26-H1; net debt/EBITDA 1.06x annualised vs 0.65x band"}
  - {id: "A3-P-04", check: "F1", line: "p15 L437-438, L449", classification: "AMBIGUOUS", implication: "Exceptional items nil FY24-FY26, H1FY27 13.18 charge undisclosed; p12 PBT math puts it in Q1; Q1 open question unanswered second quarter"}
  - {id: "A3-P-05", check: "F1", line: "p16 L490, L494, L509, L517", classification: "FORWARD-SIGNAL", implication: "LT borrowings nil FY25, 44.65 now; 97% of 1,699.95 debt is short-term; Dahej-III term debt not yet drawn, leverage to rise before capacity earns"}
  - {id: "A3-P-06", check: "F6", line: "p6 L136-141", classification: "FORWARD-SIGNAL", implication: "Solvent (+60-100%) and freight (+100%) normalisation dated within Q3 FY27; Q3 margin must recover from 18.7%"}
  - {id: "A3-P-07", check: "F6", line: "p6 L141-142; p18 L543", classification: "FORWARD-SIGNAL", implication: "Unquantified 'similar momentum' and margin guide; H2 needs 20.9-24.7% margin for 20-22% FY27; Q2 annualised Rs 869 Cr at Rs 800-850 Cr footprint ceiling [memory]"}
  - {id: "A3-P-08", check: "F6", line: "p8 L194-197", classification: "FORWARD-SIGNAL", implication: "Greenfield 'in line with planned schedule' with no schedule, capex or milestone; CWIP +194.79 Mn only trace"}
  - {id: "A3-P-09", check: "F6", line: "p7 L167-169; p23 L674; L1106", classification: "FORWARD-SIGNAL", implication: "ESS flat QoQ (~65 vs ~67); FY27 Rs 40-50 Cr guide [memory] needs H2 at least 2.0x H1; hybrid battery undated"}
  - {id: "A3-P-10", check: "F6", line: "p7 L176-179; p29 L1108", classification: "FORWARD-SIGNAL", implication: "R&D 1.19% of H1 revenue (FY26 1.55%) against 'accelerate' pipeline claim; <2%-second-year watch item on course to fire"}
  - {id: "A3-P-11", check: "F7", line: "p9 L207-208; p6 L137", classification: "FORWARD-SIGNAL", implication: "'progressively where appropriate' signals incomplete solvent pass-through; Q3 margin exposed if normalisation slips"}
  - {id: "A3-P-12", check: "F7", line: "p8 L185-192", classification: "NEUTRAL-FACT", implication: "Semiconductor 'working patiently'; no conversion condition met (no supply agreement, capex line or revenue)"}
  - {id: "A3-P-13", check: "F7", line: "p6 L133-135; p12 L329-330", classification: "AMBIGUOUS", implication: "Margin miss framed as 'temporary'; 20-22% band not restated; -2% employee and other cost claim unverifiable from deck"}
  - {id: "A3-P-14", check: "F12", line: "p13 L1106; p20-24", classification: "FORWARD-SIGNAL", implication: "SDA ~+72% QoQ supplied ~80% of the 502 Mn QoQ revenue gain; SDA 45% of Q2; growth guide rests on Euro 7 SDA"}
  - {id: "A3-P-15", check: "F14", line: "p23 L676; p24 L707", classification: "NEUTRAL-FACT", implication: "'Revenue in Q1FY27' labels are H1 values (sum ties to 3,844); left uncorrected in the Updated deck"}
  - {id: "A3-P-16", check: "F14", line: "p16 L503", classification: "NEUTRAL-FACT", implication: "'Tangible net worth' printed on total equity 8,146.51; intangibles 65.46 not deducted"}
  - {id: "A3-P-17", check: "F14", line: "p41 L1087; p42 L1101", classification: "NEUTRAL-FACT", implication: "Stale boilerplate (COVID-19, Copyright 2021, EBIDTA); cumulative disclosure-control data point with P-01 and P-15"}
  - {id: "A3-P-18", check: "F14", line: "p40 L1067-1072 vs L1110", classification: "NEUTRAL-FACT", implication: "Text layer places 19.58% at FPI, image at PUBLIC; verify against NSE Sept 2026 SHP"}
  - {id: "A3-P-19", check: "F17", line: "p15-16; p16 L485-496", classification: "AMBIGUOUS", implication: "No cash flow in deck, CFO NOT FOUND; H1 net WC +806.76 > EBITDA 729.85, debt +496.22; receivable days ~85; second quarter of cash silence"}
  - {id: "A3-P-20", check: "F17", line: "p6-9; p7 L174", classification: "AMBIGUOUS", implication: "12 of 18 checklist/open items not addressed, incl. two pharma molecules by Q3 end, Customer 1 36%, subsidiary receivables, Rs 1,000 Cr ceiling"}
forward_signals: ["A3-P-05", "A3-P-06", "A3-P-07", "A3-P-08", "A3-P-09", "A3-P-10", "A3-P-11", "A3-P-14"]
ambiguous: ["A3-P-01", "A3-P-02", "A3-P-04", "A3-P-13", "A3-P-19", "A3-P-20"]
commitments:
  - {commitment: "Solvent prices and freight to normalise within Q3", implied_date: "by 2026-12-31", ref: "p6 L140-141 (R035)", status_word: "underway"}
  - {commitment: "Revenue growth with similar momentum over the next quarters", implied_date: "Q3-Q4 FY27", ref: "p6 L141 (R036)", status_word: "initiated"}
  - {commitment: "EBITDA margin to resume its healthy trajectory (no number)", implied_date: "Q3 FY27 onward", ref: "p6 L142 (R037)", status_word: "initiated"}
  - {commitment: "Customer pricing adjusted progressively where appropriate", implied_date: "undated", ref: "p9 L208 (R056)", status_word: "underway"}
  - {commitment: "ESS hybrid-battery application progressing towards commercialisation", implied_date: "undated (Oct-Nov CY2026 per Q1 call, memory)", ref: "p7 L168 (R045)", status_word: "underway"}
  - {commitment: "Additional ESS products being scaled up", implied_date: "undated", ref: "p7 L169 (R045)", status_word: "underway"}
  - {commitment: "Pharma product beginning to contribute", implied_date: "Q2 FY27", ref: "p7 L174 (R047)", status_word: "completed"}
  - {commitment: "Accelerate PASC pipeline piloting, process development, commercialisation", implied_date: "undated (years ahead)", ref: "p7 L176-179 (R048)", status_word: "initiated"}
  - {commitment: "Five semiconductor products in development, validation, customer qualification", implied_date: "undated (years ahead)", ref: "p8 L185-191 (R052)", status_word: "underway"}
  - {commitment: "Greenfield project progressing in line with planned schedule", implied_date: "not stated (Q3-Q4 FY28 commissioning, memory)", ref: "p8 L194 (R054)", status_word: "underway"}
  - {commitment: "Capex to boost capacities and higher revenues", implied_date: "undated", ref: "p34 L936-940 (R638)", status_word: "underway"}
  - {commitment: "Steps taken to prevent recurrence of filing errors", implied_date: "next filing (Q3 FY27)", ref: "p1 L48-49", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The restatement is the lead item. Both corrected H1 ratios moved in the flattering direction, and the letter calls the errors typographical. The arithmetic points to wrong-cell links instead: 2.6% equals Q2 PAT over closing net worth, and 4.30 equals H1 debt over H1FY26 EBITDA. The corrected 6.3% still fails the PAT/net-worth basis that reproduces FY23-FY25. On that basis FY26 is 5.4%, not 7.2%. Both p14 ratio series change basis at the FY26 column. The original deck was filed about an hour after the 17:00 call start (timing from memory), so ratios quoted on the call may be on the wrong basis. In operations, Q2 was an SDA quarter: SDA rose about 70% QoQ and carried about 80% of the revenue gain. ESS was flat, and R&D fell to 1.2% of revenue. H1 net working capital rose 807 Mn, more than H1 EBITDA of 730 Mn, and debt rose 496 Mn. The deck has no cash flow statement, so CFO stays NOT FOUND until A4 reads the results filing. Q2 annualised revenue of Rs 869 Cr already sits at the capacity ceiling management gave on the Q1 call."
```
