# A3 FORENSIC NOTES: Syngene International (SYNGENE) q2fy27, doctype pressrelease

Agent: A3 forensic notes | model: claude-opus-5-5 | date: 2026-10-28
Inputs read: extracted/syngene-pressrelease-q2fy27-structured.md (R001-R879, all rows), extracted/syngene-pressrelease-q2fy27-fulltext.md (L1-L452, all lines), work/ledger_pressrelease_syngene_q2fy27.md (all sections incl. NEW-1/NEW-2), work/monitoring_checklist.md. Prior-quarter fulltext: none available. Source PDF and inputs/ not opened.
Units: pages 2-4 Rs Cr; pages 6-9 Rs Mn (x0.1 to Cr). All arithmetic below is on filed numbers; any figure not in the document is NOT FOUND.

## 0. LEDGER RECONCILIATION

| Item | Result |
|---|---|
| Structured IDs | 879 (R001-R879) |
| IDs in ledger | 879, orphan_ids [] |
| Rows read at cited fulltext line | 879 of 879 + NEW-1/NEW-2 (L32 postal codes) |
| ledger_reconciled_pct | 100 |
| Cross-table tie-outs | p2 Cr highlights tie to p7/p8/p9 Rs Mn after rounding; p7 H1 = p9 Q1+Q2 (rounding of 1-2 Mn only); p8 Q2 = p9 Q2 on every line except one (A3R-15); balance sheet casts and cross-casts on both dates |

A2 flag dispositions:
- MARKER_MERGED R010/R025 (with R837/R838): confirmed. "381" at L89 is 38 + marker "1"; "391" at L109 is 39 + marker "1". Tie: Q2 PAT before exceptional 377 Mn (L365) = Rs 38 Cr; H1 388 Mn (L325) = Rs 39 Cr; 38 - 6 = 32 (L93), 39 - 16 = 23 (L113). A3R-13.
- HEADER_AS_FILED R849/R855: confirmed. p7 columns labelled "FY26 FY27" (L296) carry H1 values (17,851 = 8,745 + 9,106). A3R-14.
- LEADERSHIP_CHANGE R743-R745, R753, R773, R780: A3R-11, A3R-12.
- FOOTNOTE_UNRESOLVED R784: A3R-06.
- QUALITATIVE_GUIDE R770: A3R-19. TIMELINE R774/R775: A3R-03. TIMELINE R785: A3R-04.
- ZERO_STANDING (12 rows): A3R-01 (R220, R304, R674-R683), A3R-02 (R116); R014 is a rounded 0% on Rs 1 Cr PAT (context in A3R-07); R222 is a movement-column dash, no content.
- RESTATED: unit repeats Cr vs Mn only; no value restatement found.

Extraction hygiene notes (A1/A2 side, not document findings): R878 and R879 are tagged "page 9" but cite L314 and L300, which are on page 7. R831 and R833 context strings cite "lines 78-80" and "lines 98-100"; the footnotes sit at L95-97 and L115-117. No value is affected.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3R-01 | F1 | R220, R304, R674-R687, R859 | L408, L414-416, L190-191 | "Exceptional item (refer note 4, 5, 12 & 13) Rs. Mn - (55) (30) - 212 - - - - - (579) (72) (100) (55)"; "Manpower related cost optimization has been completed" | FORWARD-SIGNAL | The exceptional line is non-zero 4 quarters running (Q3 FY26 579, Q4 FY26 72, Q1 FY27 100, Q2 FY27 55, Rs Mn net). Note 13 cites "frequency" yet keeps the label. The "completed" claim sets a test: any Q3 FY27 termination charge (two research heads leave end Nov and end Dec, L153-154) contradicts it. Headline PAT is "before exceptional" (L88), so a recurring charge keeps flattering the headline. |
| A3R-02 | F1 | R116, R117, R132, R133 | L279, L289 | "Provisions - 180"; "Provisions 832 1,144" | AMBIGUOUS | Non-current provisions fell to nil from 180 Mn; current provisions fell 312 Mn. Total provisions down 492 Mn in H1. Note 12 records a 706 Mn consolidated gratuity charge (L427), so a nil long-term provision needs a reason: plan funding, reclassification, or payout. Question for A4. |
| A3R-03 | F6 | R742, R746, R774, R775, R820, R821 | L159-161 | "process development activities scheduled to begin in India this fiscal, and drug substance manufacturing at Bayview expected to begin in the next financial year" | FORWARD-SIGNAL | Filed language puts first Bayview drug substance manufacturing in FY28 (from 1-Apr-2027). That is past the T4 line ("Bayview operational date past Mar-2027"). A4 rules whether T4 fires. FY27 Bayview revenue from this contract is nil on this text; process development runs in India. |
| A3R-04 | F6 | R868, R725-R730, R785, R803, R804 | L442-445 | "This acquisition will increase the company's total single-use bioreactor capacity to 50,000L"; "costs incurred till 31 March 2025 ... Capital Work in Progress amounting to Rs 2,981 million" | AMBIGUOUS | Note 9 keeps the future tense about 18 months after the Q4 FY25 acquisition, and its CWIP figure is still the 31-Mar-2025 one. No current Bayview CWIP or capitalisation date appears. Checklist item "Bayview figure in the capex / CWIP note?" answers: stale figure only. |
| A3R-05 | F6 | R778, R779, R490, R491 | L190-192, L392 | "Manpower related cost optimization has been completed ... The benefits from these measures will be realized over the coming quarters" | FORWARD-SIGNAL | Status word: completed. Staff costs are 2,801 Mn in Q2 vs 2,814 Mn in Q1 (-0.5%), and 33.6% of revenue vs 26.5-28.3% across FY24. Test for Q3 FY27: staff cost must fall below the Q2 run-rate and the exceptional line must be nil. |
| A3R-06 | F7 | R784, R864, R710-R717 | L432-433 | "The Group continues to monitor the finalisation of Central / State Rules ... and also provide appropriate accounting effect on the basis of such developments, as needed." | AMBIGUOUS | The gratuity obligation was remeasured twice already: +706 Mn in Q3 FY26, -244 Mn in Q4 FY26 (consolidated, L427-430). The note reserves a third remeasurement with no date and no range. It links to the nil long-term provision (A3R-02). |
| A3R-07 | F8 | R644, R645, R658, R659, R214, R215, R014 | L405-406, L324 | "PBT Rs. Mn ... (57) 537"; "Tax (refer note 3 & 8) Rs. Mn ... 67 (160)" | AMBIGUOUS | Q2 FY27 ETR is 29.8% (160/537), 463 bps above statutory 25.17% (Q2 FY26 21.2%). In Q1 FY27 a tax credit of 67 Mn exceeded the pre-tax loss of 57 Mn, so Q1 PAT of 10 Mn (Rs 1 Cr, R011) exists only through the credit. H1 ETR 19.2% vs H1 FY26 17.5%. DTA (net) fell 1,007 to 930 Mn (L252), a deferred charge, not a credit. Tax effect on exceptional items varies from about 18% (Q2: 67 gross, 55 net) to 26% (Q1: 135, 100). Candidate readings: unshielded subsidiary losses (Bayview pre-operation) or a discrete Q1 credit. Question for A4. |
| A3R-08 | F10 | R104, R105 | L270 | "Equity share capital 4,037 4,029" | NEUTRAL-FACT | Paid-up capital rose 8 Mn (+0.2%) in H1. The document names no corporate action, and it gives no basic or diluted EPS, so the EPS spread cannot be tested. A4 runs the ESOP cross-check. |
| A3R-09 | F12 | R136, R137, R070-R075, R086-R093, R096, R097, R122, R123, R088, R089, R064, R065 | L291, L249, L251, L259-262, L264, L284, L260, L245 | "Other current liabilities 4,674 7,808"; "(iv) Bank balances other than (iii) above 8 2,021"; "(i) Borrowings 672 94" | AMBIGUOUS | Other current liabilities fell 3,134 Mn (-40%) in H1. The composition (customer advances or other) is not stated. Cash, bank balances and investments fell from 11,780 to 7,305 Mn. Other financial assets rose 1,348 Mn. Net treasury lines are down 3,127 Mn. Short-term borrowings rose 578 Mn. Receivables released 1,233 Mn. Investment property fell 105 Mn (-33%) with no explanation. CFO is NOT FOUND (no cash flow statement), so T3 (H1 CFO < 70% of op EBITDA) cannot be tested here. A falling advance balance drains cash. If the line holds customer advances, it also means less prepaid work in the pipeline. Lean bear; question for A4. |
| A3R-10 | F12 | R058-R061, R068, R069, R102 | L242-243, L247 | "Capital work-in-progress 11,406 10,404"; "Property, plant and equipment 24,475 25,454" | FORWARD-SIGNAL | CWIP rose 1,002 Mn while PPE fell 979 Mn: build continues, little capitalised. CWIP is 17.1% of total assets and 46.6% of PPE. Capital not yet earning (CWIP + IAUD) is 11,453 Mn vs 10,457 Mn at Mar-2026 (checklist "Rs 1,046 cr" = CWIP 10,404 + IAUD 53). Bayview manufacturing starts in FY28 (A3R-03), which points to a depreciation step-up from FY28. H1 capex is NOT FOUND. |
| A3R-11 | F13 | R753, R780, R823 | L200-202 | "Deepak Jain, Chief Financial Officer, has decided to move on from Syngene for personal reasons, and will pursue an opportunity outside the Company. Deepak will continue in his current role, at least until the close of the third quarter's financial results" | FORWARD-SIGNAL | The CFO leaves in a year with two guidance cuts and a margin reset. The text gives two reasons ("personal reasons" and an outside "opportunity"). His bounded stay ends with Q3 results, so Q4 and the FY27 audited accounts fall to an unnamed successor. Successor and search status are NOT FOUND. Matches the checklist Reg 30 item dated 27-Oct-2026. |
| A3R-12 | F13 | R743, R744, R745, R772, R773, R818, R819 | L149-154 | "Subhendu Kumar, Head of Chemistry and Priyaranjan Pattanaik, Head of Biology, will be moving on from Syngene at the end of November and December respectively" | AMBIGUOUS | Both discovery heads leave while research revenue is the re-engage trigger (R2) and a tripwire (T1). Reading A: the move consolidates under the CSO, a cost and integration step. Reading B: research talent and client relationships leave. The separating observation is research revenue and client retention in Q3/Q4. It also tests the "completed" claim in A3R-05. |
| A3R-13 | F14 | R010, R025, R837, R838 | L88-89, L108-109 | "PAT before exceptional item / 381"; "391" | NEUTRAL-FACT | The text layer merges footnote marker "1" into the figures. True values are Rs 38 Cr (Q2) and Rs 39 Cr (H1). A4 and A5 must not use 381 or 391. |
| A3R-14 | F14 | R849, R855, R142-R225 | L296, L336-337 | "FY26 FY27 Movement" (p7) vs "FY26 FY27 Movement / Q2 Q2 %" (p8) | NEUTRAL-FACT | The p7 table is labelled FY26/FY27 but holds H1 values (15,687 = 7,360 + 8,327). A reader could take H1 as full year. Drafting defect. |
| A3R-15 | F14 | R229, R333 | L339, L379 | "EBITDA from operations Rs. Mn 9,106 ... 1,995" (p8) vs "... 2,064 1,996 2,092" (p9) | NEUTRAL-FACT | Q2 FY26 operating EBITDA is 1,995 on p8 and 1,996 on p9 in the same document. Arithmetic (EBITDA 2,149 - other income 154 = 1,995) supports p8. Immaterial; note it for the cumulative drafting record. |
| A3R-16 | F14 | R013, R027, R160, R161, R244, R245, R394-R407 | L91, L111, L304, L344, L384 | "PAT Margin (%) before exceptional item 4%"; "PAT margin % 7.2 4.4" | NEUTRAL-FACT | PAT margin is computed on reported revenue including other income (377/8,607 = 4.4%), not revenue from operations (377/8,327 = 4.5%). The "%" row carries no asterisk, unlike the "%*" rows. The p2 table shows it beside Revenue from Operations without a basis. The definition is mixed inside one document. |
| A3R-17 | F14 | R859, R864, R714, R715 | L413, L430 | "termination benefits amounting to Rs. 304 (net of tax Rs. 249 Mn) million"; "resulting in a credit of ... Rs. 244 million in the consolidated financial results for the current quarter" | NEUTRAL-FACT | Carried notes are not redrafted. "Current quarter" in Note 12 refers to Q4 FY26 in a Q2 FY27 document. Note 13 misplaces its unit. Note 9 keeps the 31-Mar-2025 future tense (A3R-04). Each is immaterial alone; together they form a governance data point. |
| A3R-18 | F16 | R034, R035, R039, R008, R007, R350, R351 | L42, L74, L131, L87, L380 | "Operating EBITDA margin improves by 6 percentage points"; "EBITDA from operations margin %* ... 12.3 17.7" | NEUTRAL-FACT | The filed change is 540 bps (12.3% to 17.7%). The "6 percentage points" in the title comes from the rounded 12% and 18%. The YoY change is -420 bps (L340) and is not in the title. |
| A3R-19 | F16 | R770, R044, R835, R570-R575, R128, R129, R112, R113, R072, R073, R094, R095 | L134-136, L398, L287, L277, L250, L263 | "Adjusted for the forex hedge loss, the operating EBITDA margin would be in the mid-20s range for the quarter"; "Foreign exchange fluctuation gain/(loss), net ... (48) (118) (233) (209) (501) (614)" | FORWARD-SIGNAL | The add-back is the full net FX line (the table label says "fluctuation", not "hedge"). Q2 adjusted margin = (1,475 + 614)/8,327 = 25.1%, the low end of "mid-20s". Q1 adjusted = 19.1%; Q2 FY26 adjusted = 23.2%. The loss has grown in 5 of the last 6 quarters and reached 7.4% of revenue in Q2. At 30-Sep-2026 current derivative liabilities are 1,043 Mn against current derivative assets of 26 Mn, a net 1,017 Mn mark on hedges maturing within 12 months. Total net derivative liability is 965 Mn (1,247 Mn at Mar-2026). On the filed balance sheet the "adjustment" recurs into FY28. Treat the mid-20s figure as non-reported. |
| A3R-20 | F16 | R034, R038, R310-R323 | L42, L130, L378 | "Syngene reports sequential revenue growth of 13% in Q2 FY27"; "Revenue from operations ... 8,081 9,101 ... 7,897 8,910 ... 7,360 8,327" | AMBIGUOUS | Q1 to Q2 growth was 12.6% in FY24, 12.8% in FY25, 4.1% in FY26 and 13.1% in FY27. The headline 13% matches the seasonal pattern and starts from Q1 FY27 = 7,360 Mn, the lowest quarter in the 14-quarter series. YoY is -8.6% (L338). Q2 to Q3 history is -6.2%, +5.9%, +0.7%, so do not extrapolate the 13%. Question: what share of the QoQ gain is CDMO traction rather than seasonality? |
| A3R-21 | F16 | R250, R251, R295, R296, R166, R167, R211, R212, R040 | L348, L363, L308, L323, L131 | "Other income Rs. Mn 154 280 81.8"; "PBT Rs. Mn 852 537"; "PAT stood at Rs.32 crore" | AMBIGUOUS | Other income is 52% of Q2 PBT (280/537) vs 18% in Q2 FY26. For H1 it exceeds PBT (533 vs 480): H1 pre-tax profit is more than fully other income. Other income rose 82% YoY while the treasury lines fell 3,127 Mn (A3R-09). The composition is NOT FOUND; precedents are interest on tax refunds (Notes 1, 7) and income tax assets rose 460 Mn (L253). EBIT from operations is 358 Mn in Q2 and 143 Mn in H1 (0.9%). Earnings-quality question for A4. |
| A3R-22 | F17 | R768, R777, R038 | L130, L125 | "supported by positive traction in our CDMO business"; "improved performance in our CDMO business" | AMBIGUOUS | The document gives no research vs development and manufacturing revenue split. The CDMO claim is qualitative only. R2 (research >= Rs 610 cr), T1 (< Rs 580 cr) and the "CDMO share > 22%" check cannot be tested from this document. The silence coincides with the exit of both discovery heads (A3R-12). |
| A3R-23 | F17 | R042, R835, R310-R323, R142, R143 | L134-135, L378, L298 | "revenue declined 9%, while operating EBITDA margin stood at 18%, in line with expectations" | FORWARD-SIGNAL | No FY27 revenue guidance appears, only "in line with expectations". Hurdle on the last guidance ("single-digit decline"): FY26 revenue = 37,387 Mn, so FY27 must exceed 33,648 Mn and H2 must exceed 17,961 Mn, a YoY decline under 8.1% against the H2 FY26 base of 19,536 Mn (Q4 FY26 10,365 was a series high). Q2 was -8.6% and H1 -12.1%. H2 must beat the Q2 YoY rate, so T2 (a third cut) stays live. |
| A3R-24 | F17 | R336, R337, R146, R143, R338-R351 | L299, L380 | "EBITDA from operations Rs. Mn 4,059 2,382"; "EBITDA from operations margin %* ... 12.3 17.7" | FORWARD-SIGNAL | For FY27 operating EBITDA margin to reach 25% (T5, FY27 leg), H2 needs at least 0.25 + 1,539.75/H2 revenue: 32.9% at a flat H2 (19,536 Mn), 33.6% at the guidance floor (17,961 Mn). The best H2 in the series is 32.0% (FY25); FY26 H2 was 26.2%. On filed numbers the FY27 leg of T5 is near-certain to fail. The document is silent on any full-year margin view. A4 to confirm the CRISIL definition. |
| A3R-25 | F17 | R746, R747, R748, R045, R057, R755, R867 | L156-157, L164-166, L438-439 | "with a large pharmaceutical customer"; "including an agreement for clinical supplies from its biologics manufacturing facility in Bengaluru (Unit 3)"; "license for one of the drug substance production line" | AMBIGUOUS | The Bayview customer is unnamed and the contract scale (clinical vs commercial, value) is not stated. Unit 3 news is a clinical-supply contract. No utilisation, licensed vs installed litres, or PPQ is given, so R1 is not fired on this text. Note 10 still records one licensed line (as of Q1 FY26). The identity of the two >10% customers is not disclosed. |
| A3R-26 | F17 | R741, R755, R865, R718, R719 | L135, L223, L434-435 | "primarily reflecting lower Zoetis revenues"; "Rs.277 million net ... was written off as unrecoverable balances in receivables" | AMBIGUOUS | Zoetis is named as the main YoY drag with no amount, and no impairment, residual order or compensation item. It is still listed as a marquee customer (L223). Note 11 is carried, and the write-off counterparty is still unnamed. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 12 ZERO_STANDING rows read. The exceptional line has been in use 4 straight quarters (A3R-01). Non-current provisions went to nil (A3R-02). R014/R222 have no content. |
| F2 Standalone vs consolidated | N.A. | Fact sheet is consolidated only (L235, L237). The one S-vs-C datum is Note 12 gratuity, 658 vs 706 Mn (L427): subsidiaries carry 6.8%. No revenue, EBITDA or PAT split to decompose. |
| F3 Shell-entity detection | N.A. | No standalone cost lines in a press release. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph in this doctype. |
| F5 Going concern / EoM scope | N.A. | No auditor report or EoM, and no prior-quarter text to diff. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "expected to be[gin]" L160, "will be" L192 and L212, "has been completed" L190-191; non-lexicon "scheduled to begin" L159 and "will increase" L442. A3R-03, -04, -05; register in section 3. |
| F7 Hedge phrases | FINDING | One lexicon hit, "endeavours" (L204), a false positive in a farewell line. The material hedge is Note 12's open-ended accounting reservation (A3R-06, R784). |
| F8 Tax forensics | FINDING | Q2 ETR 29.8% vs 25.17%. Q1 credit exceeds the Q1 loss. DTA fell 77 Mn (A3R-07). No current-quarter earlier-year tax item; Notes 3 and 8 are historic (Q4 FY24, Q3 FY25). |
| F9 OCI forensics | N.A. | The fact sheet carries no OCI or total comprehensive income. The hedge mark sits on the balance sheet and is covered in A3R-19. |
| F10 Share count and dilution | FINDING | Paid-up capital +8 Mn with no action named. No EPS lines (A3R-08). |
| F11 Reserves and net worth tie-out | PASS | 4,037 + 44,551 = 48,588 and 4,029 + 44,362 = 48,391. Both balance sheets cast. No third-party net worth in context. The H1 equity bridge (+197 Mn vs PAT after exceptional 232 Mn) cannot be resolved here because dividend and OCI are NOT FOUND; the residual is 0.07% of equity. |
| F12 Segment forensics | FINDING | No segment table; single-business company. The liability-unwind and asset-accretion tests were applied to the consolidated balance sheet: other current liabilities -40% with a treasury drawdown (A3R-09); CWIP accretion +1,002 Mn (A3R-10). |
| F13 Board / leadership outcome | FINDING | No AR, AGM or director items. KMP change: CFO exit (A3R-11). Both discovery heads exit (A3R-12). |
| F14 Note drafting inconsistencies | FINDING | Merged footnote markers (A3R-13), p7 header mislabel (A3R-14), 1,995 vs 1,996 (A3R-15), PAT margin basis (A3R-16), stale carried notes (A3R-17). |
| F15 Entity list diffs | N.A. | No consolidation list in a press release, and no prior quarter. Named group entity: Syngene USA Inc. (L441). |
| F16 Dropped / reframed disclosures | FINDING | The dropped-metric diff cannot be tested without the prior press release. Reframing found: rounded "6 pp" (A3R-18), FX add-back (A3R-19), seasonal QoQ headline (A3R-20), other-income-carried PAT (A3R-21). |
| F17 Silence audit | FINDING | See section 4. A3R-22 to A3R-26. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Bayview process development to begin in India (first manufacturing agreement) | by 31-Mar-2027 ("this fiscal") | L159-160, R774 | initiated |
| Bayview drug substance manufacturing to begin | FY28 (1-Apr-2027 to 31-Mar-2028) | L160, R775 | initiated |
| Manpower cost optimisation | done in Q2 FY27 | L190-191 | completed |
| Non-manpower cost initiatives continue | open, undated | L191, R778 | underway |
| Cost benefits "realized over the coming quarters" | undated; test Q3/Q4 FY27 staff and other expenses | L192, R779 | underway |
| CFO stays "at least until the close of the third quarter's financial results" | Q3 FY27 results (Jan-Feb 2027, exact date NOT FOUND) | L202, R780 | initiated |
| Head of Chemistry and Head of Biology exit | end Nov-2026 / end Dec-2026 | L153-154, R773 | initiated |
| CSO takes Discovery Services | effective 1-Oct-2026 | L149-150 | completed |
| Bayview raises single-use bioreactor capacity to 50,000L | undated; future tense carried since Q4 FY25 | L442-443, R785 | initiated (no status change) |
| Labour code: further compliance steps and accounting effect | contingent on Central/State rules | L432-433, R784 | underway |
| CTS laboratory commissioned, Bengaluru | Q2 FY27 | L175 | completed |
| siRNA oligonucleotide programme for global pharma | Q2 FY27 | L169 | completed |
| Unit 3 clinical-supplies agreement | Q2 FY27 | L164-165 | completed (signed) |
| Earnings call 28-Oct-2026 09:00 IST; audio within 24 h; transcript within seven working days | 28-Oct-2026 / ~6-Nov-2026 | L206-212 | initiated (procedural) |

## 4. WHAT WAS NOT DISCUSSED (F17 silence table)

Count of quarters silent: "1+" = silent in this document; earlier press releases are not available to A3, so the run length is NOT FOUND.

| checklist item | press release treatment | quarters silent | ref |
|---|---|---|---|
| R1 named commercial customer / PPQ / utilisation at Unit 3 or Bayview | PARTIAL: unnamed "large pharmaceutical customer"; Unit 3 clinical supply; no utilisation | 1+ (utilisation) | A3R-25 |
| R2 / T1 research revenue (>= 610 / < 580 cr) | SILENT: no segment split | 1+ | A3R-22 |
| CDMO share > 22% | SILENT | 1+ | A3R-22 |
| T2 FY27 guidance | SILENT: "in line with expectations" only | 1+ | A3R-23 |
| T3 H1 CFO vs op EBITDA | SILENT: no cash flow; balance sheet shows -3,134 Mn other current liabilities | 1+ | A3R-09 |
| T4 Bayview operational date / write-down | ADDRESSED: drug substance start in FY28 (past Mar-2027); no write-down mentioned | 0 | A3R-03 |
| T5 FY27/FY28 op EBITDA margin < 25% | PARTIAL: 18% reported, "mid-20s" adjusted; no full-year view | 1+ (outlook) | A3R-19, A3R-24 |
| T6 related-party receivables / director-linked customers | SILENT | 1+ | none |
| T7 Biocon stake | SILENT | 1+ | none |
| T8 BMS centre headcount | SILENT: BMS named only as a customer (L223); group headcount "over 8,300 ... 5,700+ scientists" (L218) | 1+ | none |
| T9 2027 AGM votes | N.A. this quarter | n/a | none |
| T10 SSSL investor / OCRPS terms | SILENT | 1+ | none |
| Base-path revenue (745 / ~790 / ~840 / ~930 cr) | ADDRESSED: Rs 833 cr (L83), between base and bull, below guidance path | 0 | A3R-23 |
| CWIP / Bayview capitalisation / FY28 depreciation | PARTIAL: CWIP 11,406 Mn; Bayview CWIP stale at Mar-2025; no capitalisation date | 1+ (Bayview CWIP) | A3R-04, A3R-10 |
| Zoetis (Librela) residual / impairment / compensation | PARTIAL: named as YoY drag, no amount | 1+ (quantum) | A3R-26 |
| Two > 10% customers | SILENT | 1+ | A3R-25 |
| Unit 3 licensed vs installed litres; utilisation | SILENT: Note 10 one licensed line, stale | 1+ | A3R-25 |
| Rs 277 Mn write-off counterparty | SILENT: Note 11 carried, unnamed | 1+ | A3R-26 |
| Management change | ADDRESSED: CFO exit plus two discovery heads | 0 | A3R-11, A3R-12 |

## 5. A4 HAND-OFF (FORWARD-SIGNAL and AMBIGUOUS ids)

FORWARD-SIGNAL: A3R-01, A3R-03, A3R-05, A3R-10, A3R-11, A3R-19, A3R-23, A3R-24
AMBIGUOUS (convert to management questions): A3R-02, A3R-04, A3R-06, A3R-07, A3R-09, A3R-12, A3R-20, A3R-21, A3R-22, A3R-25, A3R-26

```yaml
stage: A3-forensics
company: "SYNGENE"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/syngene-q2fy27/work/forensics_syngene_q2fy27_pressrelease.md"
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
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3R-01", check: "F1", line: "L408; L414-416; L190-191", classification: "FORWARD-SIGNAL", implication: "Exceptional line non-zero 4 straight quarters (579/72/100/55 Mn net); 'manpower optimisation completed' means any Q3 FY27 termination charge contradicts it; headline PAT is pre-exceptional"}
  - {id: "A3R-02", check: "F1", line: "L279; L289", classification: "AMBIGUOUS", implication: "Non-current provisions 180 -> nil, current 1,144 -> 832 despite 706 Mn labour-code gratuity charge; funding, reclass or payout?"}
  - {id: "A3R-03", check: "F6", line: "L159-161", classification: "FORWARD-SIGNAL", implication: "Bayview drug substance manufacturing 'expected to begin in the next financial year' = FY28, past T4 Mar-2027 line; FY27 Bayview revenue from this contract nil"}
  - {id: "A3R-04", check: "F6", line: "L442-445", classification: "AMBIGUOUS", implication: "Note 9 still future tense on 50,000L with Mar-2025 CWIP 2,981 Mn; no current Bayview CWIP or capitalisation date"}
  - {id: "A3R-05", check: "F6", line: "L190-192; L392", classification: "FORWARD-SIGNAL", implication: "Optimisation 'completed' but staff cost 2,801 vs 2,814 Mn QoQ (33.6% of revenue vs 26.5-28.3% FY24); Q3 staff cost is the test"}
  - {id: "A3R-06", check: "F7", line: "L432-433", classification: "AMBIGUOUS", implication: "Labour-code note reserves a third gratuity remeasurement, undated and unsized (R784)"}
  - {id: "A3R-07", check: "F8", line: "L405-406; L252", classification: "AMBIGUOUS", implication: "Q2 ETR 29.8% vs 25.17%; Q1 tax credit 67 Mn > pre-tax loss 57 Mn; DTA down 77 Mn; possible unshielded subsidiary losses"}
  - {id: "A3R-08", check: "F10", line: "L270", classification: "NEUTRAL-FACT", implication: "Paid-up capital +8 Mn, no corporate action named, no EPS disclosed; A4 ESOP cross-check"}
  - {id: "A3R-09", check: "F12", line: "L291; L249; L259-262; L284", classification: "AMBIGUOUS", implication: "Other current liabilities -3,134 Mn (-40%), net treasury lines -3,127 Mn, borrowings 94 -> 672 Mn; CFO NOT FOUND so T3 untestable; lean bear"}
  - {id: "A3R-10", check: "F12", line: "L242-243", classification: "FORWARD-SIGNAL", implication: "CWIP +1,002 Mn to 11,406 Mn (17.1% of assets) while PPE -979 Mn; FY28 depreciation step-up when Bayview capitalises"}
  - {id: "A3R-11", check: "F13", line: "L200-202", classification: "FORWARD-SIGNAL", implication: "CFO exits after Q3 results; FY27 audited accounts under unnamed successor in a guidance-cut, margin-reset year"}
  - {id: "A3R-12", check: "F13", line: "L149-154", classification: "AMBIGUOUS", implication: "Heads of Chemistry and Biology leave end Nov/Dec while research revenue is R2/T1; consolidation vs talent loss"}
  - {id: "A3R-13", check: "F14", line: "L89; L109", classification: "NEUTRAL-FACT", implication: "MARKER_MERGED: 381 = Rs 38 Cr, 391 = Rs 39 Cr; never use 381/391"}
  - {id: "A3R-14", check: "F14", line: "L296; L336", classification: "NEUTRAL-FACT", implication: "p7 labelled FY26/FY27 but holds H1 values"}
  - {id: "A3R-15", check: "F14", line: "L339; L379", classification: "NEUTRAL-FACT", implication: "Q2 FY26 op EBITDA 1,995 (p8) vs 1,996 (p9) in same document"}
  - {id: "A3R-16", check: "F14", line: "L91; L304; L344", classification: "NEUTRAL-FACT", implication: "PAT margin on reported revenue incl. other income (4.4%), not revenue from operations (4.5%); mixed basis"}
  - {id: "A3R-17", check: "F14", line: "L413; L430", classification: "NEUTRAL-FACT", implication: "Carried notes not redrafted ('current quarter' = Q4 FY26; unit misplaced in Note 13)"}
  - {id: "A3R-18", check: "F16", line: "L42; L87; L380", classification: "NEUTRAL-FACT", implication: "Title '6 percentage points' is rounding; filed change 540 bps QoQ; YoY -420 bps not in title"}
  - {id: "A3R-19", check: "F16", line: "L134-136; L398; L287", classification: "FORWARD-SIGNAL", implication: "Mid-20s = full FX add-back (25.1%); FX loss grew 5 of last 6 quarters to 7.4% of revenue; net current derivative liability 1,017 Mn implies the 'adjustment' recurs over next 12 months"}
  - {id: "A3R-20", check: "F16", line: "L42; L378", classification: "AMBIGUOUS", implication: "13% QoQ matches seasonal Q1->Q2 (12.6%, 12.8% FY24/FY25) off the lowest quarter in 14; YoY -8.6%"}
  - {id: "A3R-21", check: "F16", line: "L348; L363; L308; L323", classification: "AMBIGUOUS", implication: "Other income 52% of Q2 PBT and 111% of H1 PBT, up 82% YoY while treasury fell; composition NOT FOUND"}
  - {id: "A3R-22", check: "F17", line: "L125; L130", classification: "AMBIGUOUS", implication: "No research vs CDMO split; R2, T1 and CDMO>22% untestable from this document"}
  - {id: "A3R-23", check: "F17", line: "L134-135; L378", classification: "FORWARD-SIGNAL", implication: "No FY27 guidance; single-digit-decline floor needs H2 > 17,961 Mn (YoY better than -8.1%) vs Q2 -8.6%; T2 live"}
  - {id: "A3R-24", check: "F17", line: "L299; L380", classification: "FORWARD-SIGNAL", implication: "FY27 op margin 25% needs H2 >= 32.9-33.6% vs best-ever H2 32.0%; FY27 leg of T5 near-certain to fail on filed numbers"}
  - {id: "A3R-25", check: "F17", line: "L156-157; L164-166; L438-439", classification: "AMBIGUOUS", implication: "Bayview customer unnamed, scale unstated; Unit 3 clinical only; no utilisation or litres; R1 not fired; top-2 customers silent"}
  - {id: "A3R-26", check: "F17", line: "L135; L434-435", classification: "AMBIGUOUS", implication: "Zoetis named as YoY drag without amount or impairment; Rs 277 Mn write-off counterparty still unnamed"}
forward_signals: ["A3R-01", "A3R-03", "A3R-05", "A3R-10", "A3R-11", "A3R-19", "A3R-23", "A3R-24"]
ambiguous: ["A3R-02", "A3R-04", "A3R-06", "A3R-07", "A3R-09", "A3R-12", "A3R-20", "A3R-21", "A3R-22", "A3R-25", "A3R-26"]
commitments:
  - {commitment: "Bayview process development begins in India", implied_date: "by 2027-03-31", ref: "L159-160 R774", status_word: "initiated"}
  - {commitment: "Bayview drug substance manufacturing begins", implied_date: "FY28 (2027-04-01 to 2028-03-31)", ref: "L160 R775", status_word: "initiated"}
  - {commitment: "Manpower cost optimisation", implied_date: "Q2 FY27", ref: "L190-191", status_word: "completed"}
  - {commitment: "Non-manpower cost initiatives continue; benefits over coming quarters", implied_date: "undated (test Q3/Q4 FY27)", ref: "L191-192 R778 R779", status_word: "underway"}
  - {commitment: "CFO stays at least until Q3 FY27 results", implied_date: "Q3 FY27 results (date NOT FOUND)", ref: "L202 R780", status_word: "initiated"}
  - {commitment: "Heads of Chemistry and Biology exit", implied_date: "2026-11-30 / 2026-12-31", ref: "L153-154 R773", status_word: "initiated"}
  - {commitment: "CSO assumes Discovery Services", implied_date: "2026-10-01", ref: "L149-150", status_word: "completed"}
  - {commitment: "Bayview lifts single-use bioreactor capacity to 50,000L", implied_date: "undated (future tense since Q4 FY25)", ref: "L442-443 R785", status_word: "initiated"}
  - {commitment: "Labour code compliance steps and accounting effect", implied_date: "contingent on rules", ref: "L432-433 R784", status_word: "underway"}
  - {commitment: "CTS laboratory commissioned", implied_date: "Q2 FY27", ref: "L175", status_word: "completed"}
  - {commitment: "Unit 3 clinical-supplies agreement signed", implied_date: "Q2 FY27", ref: "L164-165", status_word: "completed"}
  - {commitment: "Call 2026-10-28 09:00 IST; transcript within seven working days", implied_date: "2026-10-28 / ~2026-11-06", ref: "L206-212", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "The release sells a QoQ recovery. The filed numbers tell a weaker story. The 13% QoQ matches the seasonal Q1-Q2 pattern. The 6 pp is 540 bps after rounding. The mid-20s margin adds back an FX loss that the balance sheet says will recur: net current derivative liability is 1,017 Mn. Other income exceeds H1 PBT. Three arithmetic tests matter most for A4. First, T5 FY27 needs an H2 margin above any H2 in 14 quarters. Second, the guidance floor needs H2 YoY better than Q2's -8.6%. Third, Bayview manufacturing in FY28 sits past the T4 line. A4 rules on T4; A3 does not. The balance sheet shows other current liabilities -40% and the treasury down 3,127 Mn with borrowings up. CFO is NOT FOUND, so the T3 question goes to the call. The CFO and both discovery heads leave in one release, while research revenue, the R2/T1 metric, goes undisclosed. Use 38/39 Cr, never 381/391."
```
