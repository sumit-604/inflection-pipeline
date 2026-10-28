# A3 FORENSIC NOTES | SYNGENE | Q2 FY27 | doctype: PRESENTATION

Agent: A3 forensic notes (claude-opus-5-5). Date: 2026-10-28.
Inputs read: A1 structured file (R001-R350), A1 fulltext (805 lines), A2 ledger (350 R rows plus M01-M09), and the monitoring checklist (runs/syngene-q2fy27/work/monitoring_checklist.md).
Not read: the source PDF and anything under inputs/. No prior-quarter deck was supplied. F5, F15 and F16 dropped-disclosure diffs therefore cannot be run against a prior deck. F17 silence counts are floors (">=1").
Unit: Rs Cr, from slides 27 and 28 ("All figures in Rs. Cr unless otherwise specified", lines 616 and 676). Line numbers refer to the A1 fulltext.

## 0. LEDGER RECONCILIATION (100%)

- R rows: 350 of 350 read in the structured file and at the cited fulltext line. Count: 350/350 = 100%.
- M rows: M01 (line 23), M02 (line 31), M03 (line 488), M04 (line 508), M05 (line 524), M06 (line 546), M07 (line 559), M08 (lines 801/803) and M09 (footer furniture) were all read at their lines. All are non-financial. M08 carries into A3P-09. The others carry no forensic content.
- A2 flags. Each flag was checked against the fulltext:
  - RESTATED rows (p6 vs p27, p10 vs p28, headcount and client counts): values agree across slides. No conflict.
  - AS_PRINTED_DUP R039/R044/R050 (H1FY26 PAT 154 before and after exceptional): this is consistent. Q2FY26 also prints 67/67 (line 673). The FY26 exceptional and gratuity items (R319-R321) therefore sit in H2 FY26. This is not a finding.
  - OUTLIER R205/R284 (forex): see A3P-10.
  - BASIS_DIFF R077/R146: see A3P-09. R144 (61% achieved vs 54.6% target, line 503) uses the same measure on both sides. Neither base year nor target year is stated. Neutral.
  - ZERO_STANDING R149: see F1.
  - TYPO R339/R340: see A3P-09.
  - CONTACT_DIFF R343: see A3P-09.
- A1 citation drift (pipeline note, not a company finding). Several rows cite a line a few lines off their text: R065 (cites 199, text at 201), R102 (cites 270, text at 272), R140 (cites 461, text at 462), R159-R163 (cite 582, which is the note line; the texts sit at lines 568-580) and R343 (cites 795, the YouTube URL; the contacts sit at lines 797-803). The verbatim values are correct. Only the anchors drift.
- Arithmetic re-foot of slides 27 and 28. Reported revenue = revenue from operations + other income in all five periods. EBITDA = reported revenue - cost lines (within Rs 1 Cr rounding) in all five periods. Operating EBITDA = EBITDA - other income in all periods. PAT before exceptional = PBT - tax in all periods. PAT after exceptional reconciles to the footnoted items: 38-6=32, 1-10=-9, 380-38-25=317 and 475+21=496. H1 = Q1+Q2 for revenue (1,569), PAT before exceptional (39), PAT after exceptional (23) and the exceptional item (16). The balance-sheet use of funds ties at both dates. One break: EBITDA - (depreciation and finance cost) does not equal PBT in any period (A3P-08).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F6 | R018, R017 | line 121, slide 6 | "Process development is scheduled to begin in India this year, followed by drug-substance manufacturing at Bayview next year" | FORWARD-SIGNAL | This is the first dated Bayview commitment. Drug-substance manufacturing comes "next year", after an India process-development phase. The deck does not say if "next year" means CY2027 or FY28. On either reading, revenue-producing manufacturing at Bayview most likely starts after Mar-2027. This tests tripwire T4 (Bayview operational date past Mar-2027). A4: get the start month and confirm which year convention applies. |
| A3P-02 | F6 | R019, R020, R021 | lines 119, 125-127, slide 6 | "first manufacturing agreement for the Bayview facility with a large pharmaceutical customer"; "agreement to supply clinical materials from its Bengaluru biologics facility (Unit 3)" | AMBIGUOUS | Re-engage trigger R1 needs a named commercial-scale customer, a PPQ (process performance qualification) or a utilisation figure. The Bayview customer is unnamed and the deck does not state the scale. The Unit 3 contract is clinical, not commercial. R1 has not fired on the deck text. A4 question: is the Bayview agreement clinical or commercial scale, and what are its volume and term? |
| A3P-03 | F6 | R024 | lines 137-140, slide 6 | "Manpower-related optimization has been completed, while other initiatives remain underway, with benefits expected over the coming quarters" | AMBIGUOUS | Status moves: manpower is "completed" and the other initiatives are "underway". The benefit has no figure and no date. Termination cost so far is Rs 25 Cr net of tax in FY26 (line 714) plus Rs 16 Cr in H1 FY27 (line 138), for Rs 41 Cr in total. A4 question: run-rate saving in Rs Cr and the quarter in which it is fully visible. |
| A3P-04 | F7 | R123 (slide 16 text) | line 369, slide 16 | "Supporting talent stability and execution continuity during a demanding operating environment" | AMBIGUOUS | This hedge is outside the lexicon, on the people slide. It sits next to a completed headcount cut (A3P-03). It is a pre-emptive admission of retention and execution strain. Lean bear: attrition in scientific teams would hit research delivery (trigger R2). A4 question: attrition rate for H1 FY27 against FY26. |
| A3P-05 | F8 | R227-R236, R298-R303 | lines 670-671, 738-739, slides 27-28 | "Tax 16 -7 18"; "PBT 54 -6 85" | AMBIGUOUS | ETR (effective tax rate) is 29.6% in Q2 FY27 (16/54), about 446 bps above the statutory 25.17%. In Q1 FY27 the tax credit of Rs 7 Cr is larger than the Rs 6 Cr pre-tax loss, which leaves PAT before exceptional at +1. H1 FY27 ETR is 18.8% (9/48). Other periods: Q2FY26 21.2%, FY26 22.1%, FY25 24.4%. A credit larger than the loss points to deferred-tax recognition or an earlier-year adjustment. The deck does not say which. A4 and the results-filing A3: what is in the Q1 credit, and is the Q2 rate the forward run-rate? |
| A3P-06 | F10 | R330-R332, R335-R338, R341 | lines 774-787, slide 31 | "Free-float market cap (Rs. Cr) 6818"; "Market Cap (Rs. Cr) 14,382"; "Promoter & Promoter Group 53%" | NEUTRAL-FACT | 6,818/14,382 gives 47.4% free float (public plus ESOP Trust, per line 785). That implies promoter holding of about 52.6%, not the printed 53%. Headroom to the 51% control line (tripwire T7) is about 1.6 pp. Shares are printed rounded at 40 Cr. A 14,382 market cap sits well above the ~Rs 9,000 Cr level that Rs 225 x 40 Cr gives (trigger R3). The exact price is NOT FOUND in the deck. There is no EPS, so the basic-vs-diluted spread cannot be assessed. |
| A3P-07 | F11 | R247-R251, R312-R316, R250 | lines 624-630, 743, slides 27-28 | "Net cash/(debt) (3) 1,392"; "Other net assets (2) -554" vs Mar-26 "Net cash/(debt) (4) 1,800 / Other net assets (3) -1,007" | AMBIGUOUS | The tie-out holds at both dates. Over H1, net cash fell by Rs 408 Cr. Net fixed assets fell Rs 25 Cr. Other net assets rose Rs 453 Cr. So the cash went into non-cash net assets, not into fixed assets. Candidate drivers: (a) working-capital build, (b) settlement of forex hedge liabilities (H1 forex loss Rs 111 Cr), (c) paydown of capex creditors or other payables. H1 operating EBITDA is Rs 238 Cr, and 70% of that is Rs 167 Cr. H1 CFO is NOT FOUND in the deck. Lean bear: the direction is adverse for tripwire T3. Shareholders' funds rose only Rs 20 Cr against H1 PAT of Rs 23 Cr, so check the dividend and OCI bridge. A4: test against the results-filing cash flow statement. |
| A3P-08 | F14 | R206-R210, R222-R229, R285-R299 | lines 665, 669, 670, 733, 737, 738, slides 27-28 | "EBITDA 175 116 215"; "Depreciation and Finance Cost 112 112 117"; "PBT 54 -6 85" | AMBIGUOUS | The table does not foot from EBITDA to PBT. EBITDA - (depreciation and finance cost) - PBT leaves an unlabelled gap of Rs 9 Cr (Q2FY27), 10 (Q1FY27), 13 (Q2FY26), 48 (FY26) and 53 (FY25). FY26 and FY25 confirm it is structural, about Rs 50 Cr a year. The deck prints no line for it. A4 and the results-filing A3: which filed line is it (a split finance cost, lease interest, or another charge), and does the "Depreciation and Finance Cost" label understate below-EBITDA charges? |
| A3P-09 | F14 | R259, R340/R339, R077/R146, R343/M08, R254/R318 | lines 652, 784, 222 vs 506, 801 vs 803, 616/676 | "less Total debt ... at the end of the year"; "As on 30st September 2026"; "92% energy from renewable sources" vs "95% of energy procured from renewable energy sources" | NEUTRAL-FACT | Several small drafting defects. (a) The half-year net-cash footnote says "end of the year" (copied from the annual slide). (b) "30st" typo. (c) Renewable share is 92% on slide 10 and 95% on slide 22, both "as on March 31, 2026", with no basis given (total vs procured energy is the likely split). (d) Slide 32 prints two IR emails (lines 801, 803). (e) Slides 27-28 do not say if they are consolidated or standalone. A4: tie the Rs 833 Cr to the consolidated results filing. Each is immaterial alone. Together they are a governance data point. |
| A3P-10 | F16 | R045, R048, R201-R205, R282-R284, R219-R221 | lines 133-135, 664, 732, slide 6/27/28 | "Operating EBITDA margin stood at 18%, in line with expectations ... Adjusted for the forex hedge loss, the operating EBITDA margin for the quarter would be in the mid-20s range" | FORWARD-SIGNAL | This is a non-GAAP reframe. The arithmetic: (147+61)/833 = 25.0% in Q2, and (91+50)/736 = 19.2% in Q1. "Mid-20s" is exactly 25.0%, which is the tripwire T5 line. Reported 18% is 700 bps below it. The forex loss runs 12 (Q2FY26), 50 (Q1FY27), 61 (Q2FY27). H1 FY27 at Rs 111 Cr is 1.8x the whole of FY26 (Rs 61 Cr) and FY25 was Rs 2 Cr. This is a recurring hedge-book cost, not a one-off. It will repeat until the book rolls off. "In line with expectations" shows management expected 18%. A4 question: hedge book notional, average strike and maturity profile, and expected H2 hedge loss. |
| A3P-11 | F16 | R304, R319, R320, R321 | line 714, slide 28 | "Excludes (i) impact of Rs. 38 Cr. (net of tax) pertaining to the net increase in gratuity liabilities on account of newly implemented labour codes, and (ii) expenses of Rs 25 Cr. (net of tax) recognised under Exceptional Items" | AMBIGUOUS | Only item (ii) is described as "recognised under Exceptional Items". Item (i) is not, yet the deck excludes both from "PAT before exceptional items" (Rs 380 Cr). So the deck's "before exceptional" label is wider than the filed exceptional line. FY26 PAT on the filed exceptional basis would be Rs 342 Cr (380-38) if item (i) sits in operating costs. A4 and the results-filing A3: where was the Rs 38 Cr booked in the filed FY26 P&L? |
| A3P-12 | F16 | R075, R084, R118, R119, R124, R125, R186-R190 | lines 222, 357-359, 375, 138, 661 | "8,373 total headcount"; "All figures are as on March 31, 2026"; "Manpower-related optimization has been completed" | AMBIGUOUS | The Q2 FY27 deck keeps the March-2026 headcount (8,373, with 5,778 scientists) after a termination programme that it says is complete. The current headcount is NOT FOUND. Staff costs are flat QoQ (280 vs 281) on revenue up 13%, and down 9% YoY. The size and mix of the cut are not disclosed: scientists vs support, and whether BBRC is affected (tripwire T8). A4 question: Sep-2026 headcount and scientist count. |
| A3P-13 | F17 | R025-R029, R073, R261 | lines 145, 222, slide 6 | "Revenue from Operations: Q2FY27 Rs 833 Cr ... H1FY27 Rs 1,569 Cr, -12% Y-o-Y" | FORWARD-SIGNAL | The deck gives no FY27 guidance. Per the checklist, the guidance was cut to "single-digit decline" on 30-Jul-2026 (tripwire T2). Arithmetic from filed numbers: FY27 must stay above 0.90 x 3,739 = Rs 3,365 Cr. That needs H2 revenue above Rs 1,796 Cr, about Rs 898 Cr a quarter, which is 7.8% above Q2's 833. H1 ran at -12% YoY. The deck does not restate guidance in the quarter in which the bar steepens. A third cut (T2) is the bear read. A4 question: is the FY27 guidance reaffirmed, and what is the H2 bridge? |
| A3P-14 | F17 | R025, R102, R105, R181-R185 | lines 145, 270-299, 660 | "Research Services (CRO)"; "Large Molecule CDMO"; "Small Molecule CDMO" (strategy only; no revenue split) | AMBIGUOUS | The deck gives no split of research vs development and manufacturing (D&M) revenue. Trigger R2, tripwire T1 and the "CDMO share > 22%" check cannot be tested from the deck. Silence count >=1 (no prior deck supplied). Indirect read [INFERENCE]: material cost to revenue fell to 23.9% (199/833) from 26.2% YoY (239/911). That fits a lower manufacturing share, but other readings are possible. Q2 revenue of 833 sits between the checklist base (~790) and bull (~840) paths, and below the guidance path (~930). A4 question: research and D&M revenue for Q2. |
| A3P-15 | F17 | R062, R095 | lines 187, 251-252, slides 9 and 11 | "Expanded into commercial manufacturing in Biologics with Zoetis" | AMBIGUOUS | Zoetis stays as a present-tense credential. The deck gives no Q2 update on Zoetis (Librela) orders, impairment or compensation, which is a named checklist item. Silence count >=1. A4 question: Zoetis residual volumes and any impairment or compensation booked in H1. |
| A3P-16 | F17 | R222-R226, R248, R313, R065 | lines 669, 625, 743, 201 | "Depreciation and Finance Cost 112 112 117"; "Net Fixed assets 4,021" (Mar-26 4,046); "single-use bioreactor capacity to 50,000L" | FORWARD-SIGNAL | D&F is flat QoQ and down YoY. Net fixed assets fell Rs 25 Cr in H1. So no capitalisation step-up is visible yet against the Rs 1,046 Cr CWIP at Mar-2026 (checklist). The depreciation step-up is still ahead once Bayview and Unit 3 capitalise. Capacity is given (50,000 L). Utilisation, licensed vs installed litres, the Bayview carrying value and CWIP are all NOT FOUND in the deck. A4 question: capex for H1, CWIP at Sep-2026, Bayview capitalisation date and FY28 depreciation. |
| A3P-17 | F17 | R343, R010, R345; checklist items | slide 15 line 345; whole deck | "Clients concentrated in US, Europe & Japan" | AMBIGUOUS | The deck is silent on these checklist items. Only geographic concentration is given, not the identity or share of the two >10% customers. Also silent: related-party receivables (T6), the Rs 277 mn write-off counterparty, SSSL / OCRPS (T10), and the CFO exit in the 27-Oct-2026 Reg 30 filing. The deck dated October 2026 names no management change. Each silence count is >=1. See the silence table. |

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | PASS | One ZERO_STANDING row (R149, line 510, "Zero waste to direct landfill") is an ESG KPI, not a financial template line. No nil financial standing line exists in the slide 27/28 tables. |
| F2 | N.A. | The deck carries one unlabelled P&L set and no standalone vs consolidated pair. The missing basis label goes to A3P-09. |
| F3 | N.A. | No standalone cost lines in the deck. Shell detection is a results-filing check. |
| F4 | N.A. | There is no auditor letter in a presentation. |
| F5 | N.A. | No EoM (emphasis of matter) or going-concern paragraph in the deck, and no prior deck was supplied. |
| F6 | FINDING | A3P-01, A3P-02, A3P-03. Commitment register below. |
| F7 | FINDING | A3P-04 (line 369). The only lexicon hit is the safe-harbour "subject to" (line 80), which is boilerplate. No prior deck to diff. |
| F8 | FINDING | A3P-05. The deck carries PBT and tax lines. Q1 credit exceeds the loss. Q2 ETR is 29.6% against 25.17%. |
| F9 | N.A. | The deck has no OCI line. |
| F10 | FINDING | A3P-06. Implied promoter holding is ~52.6%. No EPS, so the dilution spread cannot be assessed. |
| F11 | FINDING | A3P-07. The tie-out holds with a 0% gap at both dates. The composition shift (net cash -408, other net assets +453) is the finding. |
| F12 | N.A. | The deck has no segment assets or liabilities table. |
| F13 | N.A. | The deck has no board outcome, AGM notice or appointment term. |
| F14 | FINDING | A3P-08 (EBITDA-to-PBT gap) and A3P-09 (drafting defects). |
| F15 | N.A. | The deck has no consolidation entity list and no prior deck. |
| F16 | FINDING | A3P-10, A3P-11, A3P-12 (reframes and stale disclosures within the deck). The dropped-slide diff cannot be assessed because no prior deck was supplied. |
| F17 | FINDING | A3P-13 to A3P-17. Applied to the deck per the task message. See the silence table. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Bayview: process development for the first manufacturing customer in India | "this year" (CY2026 or FY27, not stated) | line 121, slide 6 | initiated |
| Bayview: drug-substance manufacturing for that customer | "next year" (CY2027 or FY28, not stated) | line 121, slide 6 | initiated |
| First Bayview manufacturing agreement (unnamed large pharma) | signed in Q2 FY27 | line 119, slide 6 | completed (signing) |
| Unit 3 clinical materials supply agreement and other biologics contracts | signed, delivery undated | line 125, slide 6 | initiated |
| Broader biologics manufacturing pipeline | undated | line 127, slide 6 | aspiration (no status word) |
| Clinical Translational Sciences laboratory, Bengaluru | commissioned in Q2 FY27 | line 130, slide 6 | completed |
| Manpower-related optimisation | done by Q2 FY27 | line 138, slide 6 | completed |
| Other cost initiatives, benefit "over the coming quarters" | undated (H2 FY27 onward) | line 139, slide 6 | underway |
| 1-3-5-year digital roadmap with AI adoption | undated | line 470, slide 21 | aspiration (no status word) |

No prior deck was supplied, so no quarter-on-quarter status change (initiated -> underway -> completed) can be verified.

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit vs monitoring checklist)

Silence count = consecutive quarters silent. ">=1" means silent in this deck; earlier decks were not supplied.

| checklist item | deck status | ref | silence count |
|---|---|---|---|
| R1 named commercial-scale customer / PPQ / utilisation | partial: customer unnamed, scale not stated, Unit 3 clinical only | lines 119, 125 | >=1 on name, scale and utilisation |
| R2 / T1 research revenue (>= 610 / < 580) | silent: no research vs D&M split | n/a | >=1 |
| CDMO share > 22% | silent | n/a | >=1 |
| T2 FY27 guidance | silent: no guidance stated | n/a | >=1 |
| T3 H1 CFO vs 70% of operating EBITDA | silent: CFO not given; net cash -408 (A3P-07) | lines 628, 743 | >=1 |
| T4 Bayview operational date / write-down | addressed: DS manufacturing "next year"; no carrying value | line 121 | 0 (date), >=1 (carrying value) |
| T5 operating EBITDA margin < 25% | addressed: 18% reported, "mid-20s" adjusted | lines 133-135, 668 | 0 |
| T6 related-party receivables / director-linked customers | silent | n/a | >=1 |
| T7 Biocon stake | addressed: 53% printed, ~52.6% implied | lines 776-787 | 0 |
| T8 BBRC scientists (< ~650) | silent: BBRC only as history | lines 198, 257 | >=1 |
| T9 2027 AGM votes | not due this quarter | n/a | n/a |
| T10 SSSL / OCRPS | silent | n/a | >=1 |
| Bayview in capex / CWIP; CWIP 1,046; depreciation step-up | silent: NFA only; D&F flat | lines 625, 669 | >=1 |
| Zoetis (Librela) exposure | silent: kept as a credential | lines 187, 252 | >=1 |
| Identity of the two >10% customers | silent: geography only | line 345 | >=1 |
| Unit 3 licensed vs installed litres; utilisation | silent: only the 50,000 L total | line 201 | >=1 |
| Rs 277 mn write-off counterparty | silent | n/a | >=1 |
| CFO exit (Reg 30, 27-Oct-2026) | silent | n/a | >=1 |
| F6 cost-optimisation benefit | addressed in words, no figure | line 139 | 0 (words), >=1 (figure) |

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "SYNGENE"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/syngene-q2fy27/work/forensics_syngene_q2fy27_presentation.md"
ledger_reconciled_pct: 100        # 350/350 R rows + M01-M09 read at cited lines
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3P-01", check: "F6", line: "121", classification: "FORWARD-SIGNAL", implication: "Bayview DS manufacturing 'next year' after India PD 'this year'; revenue start likely after Mar-2027; tests T4; year convention unstated"}
  - {id: "A3P-02", check: "F6", line: "119,125", classification: "AMBIGUOUS", implication: "Bayview customer unnamed and scale unstated; Unit 3 deal is clinical; R1 not fired on deck text"}
  - {id: "A3P-03", check: "F6", line: "138-139", classification: "AMBIGUOUS", implication: "Manpower cut completed, other initiatives underway; benefit unquantified and undated; termination cost Rs 41 Cr net FY26+H1FY27"}
  - {id: "A3P-04", check: "F7", line: "369", classification: "AMBIGUOUS", implication: "'demanding operating environment' hedge on people slide next to completed cut; retention risk to research delivery"}
  - {id: "A3P-05", check: "F8", line: "670-671", classification: "AMBIGUOUS", implication: "Q1 tax credit 7 > loss 6; Q2 ETR 29.6% vs 25.17%; H1 ETR 18.8%; composition of Q1 credit undisclosed"}
  - {id: "A3P-06", check: "F10", line: "774-787", classification: "NEUTRAL-FACT", implication: "Free float 47.4% implies promoter ~52.6% (1.6pp over T7 51%); mcap 14,382 far above R3 level; no EPS for dilution spread"}
  - {id: "A3P-07", check: "F11", line: "624-630,743", classification: "AMBIGUOUS", implication: "Net cash -408 in H1, other net assets +453, NFA -25; cash went to non-cash net assets; H1 CFO NOT FOUND; T3 direction adverse"}
  - {id: "A3P-08", check: "F14", line: "665,669,670,733,737,738", classification: "AMBIGUOUS", implication: "EBITDA - D&F != PBT; unlabelled gap 9/10/13 per quarter, 48 FY26, 53 FY25; below-EBITDA charge not printed"}
  - {id: "A3P-09", check: "F14", line: "652,784,222/506,801/803", classification: "NEUTRAL-FACT", implication: "Drafting defects: 'end of the year' on H1 net cash, '30st', 92% vs 95% renewables, two IR emails, basis label missing"}
  - {id: "A3P-10", check: "F16", line: "133-135,664,732", classification: "FORWARD-SIGNAL", implication: "Adjusted margin (147+61)/833 = 25.0% sits on T5 line, reported 18%; forex loss 12->50->61, H1 111 = 1.8x FY26; recurring hedge-book drag"}
  - {id: "A3P-11", check: "F16", line: "714", classification: "AMBIGUOUS", implication: "FY26 'PAT before exceptional' 380 also excludes Rs 38 Cr gratuity not stated as exceptional; filed-basis PAT may be 342"}
  - {id: "A3P-12", check: "F16", line: "222,357,375,138,661", classification: "AMBIGUOUS", implication: "Mar-26 headcount 8,373 kept after cut completed; current headcount NOT FOUND; staff cost flat QoQ on +13% revenue"}
  - {id: "A3P-13", check: "F17", line: "145,222", classification: "FORWARD-SIGNAL", implication: "No FY27 guidance in deck; single-digit decline needs H2 > Rs 1,796 Cr (~898/qtr, +7.8% vs Q2); T2 third-cut risk"}
  - {id: "A3P-14", check: "F17", line: "145,270-299,660", classification: "AMBIGUOUS", implication: "No research vs D&M split; R2/T1/CDMO share untestable; material/revenue 23.9% vs 26.2% YoY [INFERENCE] lower manufacturing share"}
  - {id: "A3P-15", check: "F17", line: "187,252", classification: "AMBIGUOUS", implication: "Zoetis kept as present credential; no Librela order, impairment or compensation update"}
  - {id: "A3P-16", check: "F17", line: "669,625,743,201", classification: "FORWARD-SIGNAL", implication: "D&F flat, NFA -25; no capitalisation step-up yet vs CWIP 1,046; depreciation step-up ahead; utilisation and CWIP NOT FOUND"}
  - {id: "A3P-17", check: "F17", line: "345", classification: "AMBIGUOUS", implication: "Silent on >10% customer identity, RP receivables, Rs 277 mn write-off, SSSL/OCRPS, CFO exit"}
forward_signals: ["A3P-01", "A3P-10", "A3P-13", "A3P-16"]
ambiguous: ["A3P-02", "A3P-03", "A3P-04", "A3P-05", "A3P-07", "A3P-08", "A3P-11", "A3P-12", "A3P-14", "A3P-15", "A3P-17"]
commitments:
  - {commitment: "Bayview process development in India for first manufacturing customer", implied_date: "this year (CY2026 or FY27, unstated)", ref: "line 121", status_word: "initiated"}
  - {commitment: "Bayview drug-substance manufacturing for that customer", implied_date: "next year (CY2027 or FY28, unstated)", ref: "line 121", status_word: "initiated"}
  - {commitment: "First Bayview manufacturing agreement signed (unnamed large pharma)", implied_date: "Q2 FY27", ref: "line 119", status_word: "completed"}
  - {commitment: "Unit 3 clinical materials supply agreement", implied_date: "undated", ref: "line 125", status_word: "initiated"}
  - {commitment: "Clinical Translational Sciences laboratory commissioned", implied_date: "Q2 FY27", ref: "line 130", status_word: "completed"}
  - {commitment: "Manpower-related optimisation", implied_date: "by Q2 FY27", ref: "line 138", status_word: "completed"}
  - {commitment: "Other cost initiatives, benefits over coming quarters", implied_date: "undated, H2 FY27 onward", ref: "line 139", status_word: "underway"}
  - {commitment: "1-3-5-year digital roadmap with AI adoption", implied_date: "undated", ref: "line 470", status_word: "none (aspiration)"}
gate_a3: pass
blank_checks: []
analyst_note: "No prior deck was supplied, so F16 dropped-slide diffs and F17 silence counts are floors (>=1). Three items carry the most weight. First, A3P-08: the deck table never foots from EBITDA to PBT. About Rs 50 Cr a year of charge is unprinted, so the results-filing A3 must name the line. Second, A3P-10 with A3P-13: the 'mid-20s' adjusted margin is exactly 25.0%, the T5 line, while the reported margin is 18%. Forex hedge losses are recurring (H1 Rs 111 Cr vs FY26 Rs 61 Cr). With no guidance restated, H2 needs about Rs 898 Cr a quarter to hold 'single-digit decline'. Third, A3P-07: net cash fell Rs 408 Cr in H1 while fixed assets fell. The cash went into non-cash net assets, so T3 leans adverse until the filed cash flow statement shows CFO. A3P-01 'next year' plus A3P-16 flat depreciation say Bayview earns and depreciates after Mar-2027. Read T4 against whatever 'operational' means in the tripwire. Implied promoter holding is about 52.6%, not 53%."
```
