# A3 FORENSIC NOTES: INDOSOLAR q2fy27 (doctype: results)

Company: Indosolar Limited (INDOSOLAR), NSE symbol WAAREEINDO, BSE 533257
Quarter: Q2 FY27 (quarter ended 30-Sep-2026); standalone only (Note 5, line 225)
Units: Rs Lakhs throughout (x0.01 = Rs Crores)
Inputs read: A1 structured (R001-R383), A1 fulltext (289 lines), A2 ledger. No source PDF, nothing under inputs/.
Prior-quarter fulltext: NONE (first quarterly run). Every QoQ verbatim diff (F5, F15, revenue-mix restatement test) is stated as not possible.
Notion monitoring checklist: no Notion checklist passed. No companies/INDOSOLAR.md, no spear on record.
Model: claude-opus-5-5

## 0. LEDGER RECONCILIATION

| item | result |
|---|---|
| Structured IDs in ledger | 383 of 383 (A2: orphan_ids none, match yes) |
| Rows read at cited fulltext line | 383 of 383 = 100% |
| Pointer variances (non-material) | R311 cites line 20 (A1 repair annotation); the ISIN itself sits at line 31. R297 "SRE 2410" spans lines 258-259. R377 cites line 261; "substantially less in scope" sits at line 263. No value mismatch. |
| Arithmetic tie-outs | P&L foots in all 6 columns (income, expenses, PBT, PAT, TCI). 6M Sep-26 = Q1 + Q2 on every P&L line. Balance sheet foots both dates. Cash flow foots (A+B+C = 8,006.10; 109.41 + 8,006.10 = 8,115.51). Other Equity roll-forward 24,540.41 + 4,160.11 TCI = 28,700.52 exact. |
| A2 hand-offs answered | Board end time vs signature: board 16:30-17:30 (line 46); signature carries date only, Oct-21-2026 (line 232); auditor report same date (line 281). No time to compare, no inconsistency. Goods/services split: tested, see A3-13. Financing nil: see A3-02. UDIN: see A3-15. |

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R221, R222, R259, R260, R013-R016 | 176, 197, 80 | "Government grant - subsidy \| (669.16) \| -" | AMBIGUOUS | A new grant line: nil in H1 FY26, 669.16 recognised in H1 FY27 = 12.35% of H1 PBT 5,418.04. Received only 455.54. Tie-out: other current + non-current liabilities moved +8,485.54; CF "other liabilities" +8,699.16; the 213.62 gap equals recognised minus received. So the income is non-cash amortisation of a deferred grant held in liabilities. Grant nature, scheme, remaining balance and amortisation life are not disclosed. Other income Q1 838.70 = 17.7% of Q1 PBT, against 1.11 in Q2 FY26. A4 question: grant name, balance, amortisation schedule, clawback terms on amalgamation. |
| A3-02 | F1 | R265-R270, R049-R054 | 201, 202, 203, 87 | "Repayment of borrowings (net) \| - \| (4,705.21)"; "Finance cost \| - \| (1,865.46)" | AMBIGUOUS | All three Sep-26 financing lines are nil. The balance sheet carries no borrowings line (lines 145-160); only lease liabilities 318.57. The company reads as debt-free. Prior-year 6M cash interest paid 1,865.46 was 18.5x the P&L finance cost of 100.90 (line 87), which points to settlement of interest accrued in earlier periods. No lease principal or lease interest paid in H1 FY27 (current lease liability unchanged 9.81, line 153). A4 question: was any legacy debt or accrued interest settled or waived by the parent, and are lease rentals paid by a group entity? |
| A3-03 | F1 | R079-R084, R381, R374 | 92, 222 | "Exceptional item \| - \| - \| - \| - \| - \| -" | FORWARD-SIGNAL | The line is nil in all six columns while a Sections 230-232 scheme is in progress (Note 4). Scheme costs (legal, valuation, stamp duty, tribunal) have no disclosed home yet. Watch this line and Other expenses (Q2 564.11 vs Q1 271.71, line 89) in Q3 and Q4 FY27. A4 question: estimated scheme cost and where it will be booked. |
| A3-04 | F1 | R153, R154, R255 | 120, 195 | "Capital work in progress \| 120.56 \| -" | NEUTRAL-FACT | CWIP opens from nil; H1 capex 487.19. Small, but capex continues in an entity slated for dissolution. Low weight; ask the project name only if A4 has room. |
| A3-05 | F6 | R374, R337, R338, R351, R323, R324, R292 | 222-224 | "Upon the Scheme becoming effective, Indosolar Limited shall stand dissolved without being wound up." | FORWARD-SIGNAL | Board-approved draft scheme (Sep-23-2026) merges the listed entity into Waaree Energies Limited. The note gives no appointed date, no share exchange ratio, no approval chain and no timeline. It carries no "subject to" conditionality (F7 lexicon nil). The holder's value now runs through an undisclosed swap ratio. The standalone earnings stream has a finite horizon ending at effectiveness. A4 questions: swap ratio and valuer, appointed date, exchange/SEBI filing date, expected tribunal timeline, treatment of minority holders. |
| A3-06 | F8 | R091-R096, R163, R164, R251 | 95, 126, 192 | "Deferred tax assets (net) \| (22.81) \| 1,231.45" | FORWARD-SIGNAL | H1 FY27 tax is 100% deferred: 1,254.26 equals the DTA drawdown 1,231.45 to (22.81) exactly. Cash tax paid 54.12. The template has no Current tax line at all (lines 94-96). The recognised DTA is now exhausted and has flipped to a net liability. From Q3 FY27, profit should attract current (cash) tax at about 25.17%, or the deferred liability grows. Book ETR stays near statutory (Q2 25.21%, Q1 22.86%, H1 23.15%); cash conversion falls by the tax share of PBT. A4 question: remaining unrecognised losses or unabsorbed depreciation, if any, and the expected cash tax rate for H2 FY27. |
| A3-07 | F8 | R095, R096, R105, R107, R108, R144 | 95, 97, 105 | "Deferred Tax \| ... \| (4,683.59) \| (1,231.45)" | NEUTRAL-FACT | Base-period distortion. FY26 ETR -5.26% vs 25.17% statutory = 3,043 bps shield. At statutory rate FY26 PAT would be 17,531.52, not 24,659.91: a book shield of 7,128.39 (28.9% of reported PAT). FY26 EPS 59.27 computes to 42.14 at statutory tax. H1 FY26 ETR -40.27% (6,544 bps); implied Q1 FY26 credit (6,163.51). YoY PAT comparisons (H1 -74.5%, Q2 -89.2%) mix a tax-credit base with a full-tax current period. Any trailing multiple anchored on FY26 EPS overstates normalised earnings. |
| A3-08 | F9 | R109-R114 | 99 | "Items that will not be reclassified into Profit or loss \| (3.67) \| - \| - \| (3.67) \| - \| (0.62)" | NEUTRAL-FACT | Single-quarter OCI (3.67) is 5.9x the full prior year (0.62). Rule-triggered; immaterial (0.7% of Q2 PAT). Points to an actuarial assumption change or first valuation in the half. Verify discount rate and plan assumptions at the FY27 Annual Report, if one is issued before effectiveness. |
| A3-09 | F12 | R169, R170, R209, R210, R179, R180, R237, R247, R233, R031, R025 | 130, 159, 136, 84, 83 | "Inventories \| 22,197.26 \| 2,108.26"; "Other current liabilities \| 8,993.74 \| 794.51" | AMBIGUOUS | Single segment (Note 3), so the balance sheet is the segment. Inventory rose 10.5x; other current liabilities 11.3x (+8,199.23); other current assets 41.8x (+7,245.28). Q2 materials consumed 23,212.20 against goods sale 15,277.09, with stock built by (10,591.83). Reading one: customer advances fund stock for Q3 deliveries; Q3 goods revenue jumps. Reading two: stock built for, or with money from, the parent ahead of the merger, at thin margins. The observation that separates them: Q3 FY27 goods revenue and the drawdown of other current liabilities. Neither the advances nor the other current assets are explained in any note. A4 question: composition of other current liabilities and other current assets, counterparty for advances. |
| A3-10 | F12 | R171, R172, R239, R201-R204, R241, R253 | 132, 186, 155-156, 187, 193 | "(i) Trade receivables \| 1,625.60 \| 20,961.51"; "(Increase)/decrease in Trade receivables \| 15,841.73" | AMBIGUOUS | Balance sheet receivables fell 19,335.91 (-92.2%); cash flow shows 15,841.73, gap 3,494.18. Trade payables rose 1,101.24; cash flow shows +4,826.42, gap 3,725.18. The paired gaps fit a non-cash set-off of about 3,494 between receivables and payables (likely the same counterparty), with a residual 231.00 unexplained. Nothing in the notes discloses it. H1 OCF 7,956.70 (1.91x PAT) rests on the 15,841.73 receivable release and the 8,699.16 liability inflow. Neither repeats. A4 question: was there a receivable-payable set-off, with whom, and for how much? |
| A3-11 | F12 | R001-R012, R025-R036, R073-R078, R013-R015 | 78-84, 91 | "3 Profit before tax (1-2) \| 671.02 \| 4,747.02 \| 6,113.68" | AMBIGUOUS | Single-segment result collapsed. PBT excluding other income: Q2 FY27 3.3% of revenue, Q1 FY27 57.2%, Q2 FY26 30.2%, FY26 34.2%. Materials (consumed plus inventory change) take 82.6% of goods revenue in Q2 FY27, against 68.9% in Q2 FY26 and 75.2% in FY26. Two effects: goods margin compressed about 1,370 bps YoY, and high-margin services fell to 281.54 from 3,136.48. Reading one: input cost spike or inventory valuation timing. Reading two: transfer pricing to the group ahead of the merger. Q3 goods margin separates them. A4 question: customer mix and pricing basis of Q2 goods sales, share sold to Waaree group. |
| A3-12 | F14 | R103-R106, R121-R124, R139-R150, R127-R132 | 101, 105-106, 97 | "(a) Basic (in Rs) \| 1.20 \| 8.80 \| 11.14 \| 10.00 \| 39.21 \| 59.27" | NEUTRAL-FACT | Shares = 4,160.37 / 10 = 416.037 lakh, constant. PAT basis gives Q2 1.2063 (rounds 1.21) and 6M 10.0082 (rounds 10.01). TCI basis gives 1.1974 (1.20) and 9.9994 (10.00), matching the filed cells. No single share count reconciles all six cells on a PAT basis. EPS in the two OCI-bearing columns appears computed on total comprehensive income, which Ind AS 33 does not permit. Rs 0.01 immaterial; a drafting data point for F14. |
| A3-13 | F14 | R001-R012, R025-R030, R376 | 78, 79, 83, 227 | "Sale of Services \| 281.54 \| 5,438.72"; "Figures of the previous reporting period has been reclassified/ regrouped wherever necessary" | AMBIGUOUS | Q1 services 5,438.72 / goods 1,397.42; Q2 services 281.54 / goods 15,277.09. Test result: the 6M column equals Q1 plus Q2 exactly on both lines, so Q1 was not restated in this filing. Materials consumed moved with goods (Q1 2,178.71, Q2 23,212.20), which fits a real switch from conversion or job-work (customer-supplied material) to own-procurement sales. It is not a relabel. Limit: no prior-quarter extract, so Q1 as first reported cannot be checked. Note 6 is generic and silent on the swing. A4 question: what the services line is, who buys it, and why it stopped in Q2. |
| A3-14 | F14 | R163, R249, R336, R280, R289, R328, R310, R313 | 126, 191, 47, 62, 71, 235, 274, 30 | "Deferred tax assets (net) \| (22.81)"; "Cash used from operations \| 8,010.82" | NEUTRAL-FACT | Cumulative drafting points: net deferred tax liability shown as a negative asset (line 126); "Cash used" label on an inflow (line 191); website "https: indosolar.co.in" (line 47) vs "www.indosolar.co.in" (line 71); registered office tel +91-120 (line 62) vs 022 (line 71); firm "SGCO & Co. LLP" (line 235) vs "S G C O & Co. LLP" (line 274); symbol WAAREEINDO (line 30) vs name Indosolar Limited (line 51). Some may be OCR artifacts (lines 47, 62 are text layer). Individually immaterial. With A3-12, a pattern of light drafting control. |
| A3-15 | F14 | R301, R383 | 283 | "UDIN: UNREADABLE (text layer garbled)" | NEUTRAL-FACT | Review report UDIN not readable in the extract. This is an extraction gap, not a proven filing defect. Action for A4 or Claude web: verify the UDIN for partner M.No. 131146 (line 282) on the ICAI UDIN portal. |
| A3-16 | F15 | R323, R324, R310, R318, R319, R320, R327, R375 | 223, 30, 21, 56, 71, 231, 225 | "amalgamation of Indosolar Limited (the "Transferor Company") with Waaree Energies Limited (the "Transferee Company")" | FORWARD-SIGNAL | Relationship change: the listed entity is now a Transferor, the parent the Transferee. Parent-group markers already in the filing: symbol WAAREEINDO (line 30), "group company" tagline (line 21), waaree.com mail (lines 56, 71), signing in Mumbai (line 231) against a New Delhi registered office (line 61). Note 5: no subsidiary, associate or JV (line 225). No prior-quarter entity list, so no diff beyond this change. Same fact as A3-05 seen as an entity change, not counted twice for weight. Implication: the monitoring horizon for INDOSOLAR ends at effectiveness; exposure converts to Waaree Energies. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 34 ZERO_STANDING cells plus R381 reviewed. Exceptional (anticipates one-offs; scheme costs pending, A3-03). Tax of earlier years (assessment true-ups; nil, clean). OCI reclassifiable (hedge reserves; nil, no hedge accounting). Reserves R133-R137 are presentation dashes, not zeros (only the audited year shown). Govt grant, asset sale, financing lines: A3-01, A3-02, A3-04. Asset sale 73.20 at zero book value (lines 175, 196), clean. |
| F2 Standalone vs consolidated | N.A. | Note 5 (line 225): no subsidiary, associate or JV; Ind AS 110 not applicable; standalone only. |
| F3 Shell-entity detection | N.A. | No consolidated statements, no subsidiaries (line 225). No going-concern paragraph to reconcile. |
| F4 Unaudited contribution ratio | PASS | Review report paragraphs 1-4 (lines 247-272) carry no Other Matter paragraph and no component auditor. Unreviewed share of PAT 0%. Prior trend not available (no prior extract). |
| F5 Going concern / EoM tracking | PASS | No EoM or going-concern paragraph; conclusion unmodified (line 267). The report does not mention the Note 4 scheme. Prior-quarter auditor paragraph not available, so the verbatim diff could not run; a Q1 EoM since dropped cannot be ruled out. |
| F6 Forward-commitment phrases | FINDING | Exact lexicon hits: "commenc" once (line 46, "The meeting commenced at IST 16:30", procedural, not a commitment). Semantic hits: Note 4 board approval and "shall stand dissolved" (lines 222-224, A3-05); Reg 47 publication (line 42); website availability (lines 46-47). No other lexicon hits. |
| F7 Hedge phrases | PASS | Zero hits for the eight hedge terms in notes 1-6 (lines 215-227) and the review report. Note 4 states dissolution without any "subject to" approval language; that omission is carried in A3-05, not here. |
| F8 Tax forensics | FINDING | ETR: Q2 FY27 25.21%, Q1 FY27 22.86%, Q2 FY26 24.21%, H1 FY27 23.15%, H1 FY26 -40.27%, FY26 -5.26% vs 25.17%. All tax is deferred; no current tax line. Tax of earlier years nil in all six columns (line 96). DTA exhausted (A3-06); FY26 shield 3,043 bps, 7,128.39 (A3-07). |
| F9 OCI forensics | FINDING | Q2 OCI (3.67) exceeds full FY26 (0.62): A3-08. Reclassifiable OCI nil all columns. |
| F10 Share count and dilution | PASS | Paid-up 4,160.37 in all six columns (line 102) and both balance sheet dates (line 141); no corporate action. Basic equals diluted in every column (lines 105-106), spread 0. EPS basis anomaly sits in F14 (A3-12). Upcoming corporate action is the scheme (A3-05). |
| F11 Reserves and net worth tie-out | PASS | 4,160.37 + 28,700.52 = 32,860.89 (line 143); Mar-26 4,160.37 + 24,540.41 = 28,700.78. Roll-forward equals H1 TCI 4,160.11 exactly, no dividend. Sep-26 Other Equity (28,700.52) sits 0.26 off Mar-26 Total Equity (28,700.78); tested and ruled out as a transposition, because TCI 4,160.11 happens to sit near paid-up 4,160.37. No third-party net worth in context. |
| F12 Segment forensics | FINDING | Single segment (line 220), so the balance sheet and P&L are the segment: A3-09 (inventory and liabilities build), A3-10 (receivable and payable tie gaps), A3-11 (margin collapse). |
| F13 Board outcome beyond results | PASS | Oct-21 outcome transacts results and review report only (lines 37-44). No AR, AGM, record date, dividend, director term, auditor change or fund-raise item. Meeting 16:30-17:30 (line 46); signature and review report both dated Oct-21-2026 (lines 232, 281). The Sep-23 scheme approval is a prior meeting, carried under F6. |
| F14 Note drafting inconsistencies | FINDING | Review wording is consistent: letter says "limited review" (line 41), report says "Limited Review Report" (line 239), statement says "Unaudited". Findings: A3-12 (EPS on TCI), A3-13 (generic Note 6 vs mix swing), A3-14 (presentation and naming points), A3-15 (UDIN). |
| F15 Entity list diffs | FINDING | A3-16: Indosolar becomes Transferor to Waaree Energies. No prior-quarter entity list; no other diff possible. |
| F16 Presentation: dropped disclosures | N.A. | Results filing; no investor presentation in scope. |
| F17 Concall silence audit | N.A. | Results filing; no transcript. No Notion checklist passed. The commitment register below seeds the silence audit for the next concall or results. |

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Amalgamate Indosolar Limited into Waaree Energies Limited under Sections 230-232; Indosolar to stand dissolved without winding up on effectiveness | Not stated. Board approval Sep-23-2026; effectiveness date, appointed date and swap ratio NOT FOUND in this filing | Note 4, lines 222-224 (R374, R337, R338, R351) | initiated |
| Publish the financial results in the newspaper under SEBI LODR Reg 47 | Not stated; follows the Oct-21-2026 board meeting | Outcome letter, line 42 (R335) | initiated |
| Make the information available on the company website | Not stated | Outcome letter, lines 46-47 (R336) | initiated |

## 4. FLAGS FOR A4

FORWARD-SIGNAL (convert to management questions): A3-03, A3-05, A3-06, A3-16
AMBIGUOUS (convert to management questions; lean bear): A3-01, A3-02, A3-09, A3-10, A3-11, A3-13
Verification action (not a management question): A3-15 (UDIN on ICAI portal)

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "INDOSOLAR"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\quarterly-indosolar-q2fy27-2614ff\\runs\\indosolar-q2fy27\\work\\forensics_results_indosolar_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "176, 197, 80", classification: "AMBIGUOUS", implication: "New deferred govt grant; 669.16 non-cash amortisation = 12.35% of H1 PBT; received 455.54; nature, balance, clawback on merger undisclosed"}
  - {id: "A3-02", check: "F1", line: "201, 202, 203, 87", classification: "AMBIGUOUS", implication: "Financing nil, debt-free; prior-year cash interest 1,865.46 = 18.5x P&L 100.90 (legacy accrual settled?); no lease payments in H1"}
  - {id: "A3-03", check: "F1", line: "92, 222", classification: "FORWARD-SIGNAL", implication: "Exceptional nil all columns while scheme in progress; scheme costs to land in Q3/Q4 FY27"}
  - {id: "A3-04", check: "F1", line: "120, 195", classification: "NEUTRAL-FACT", implication: "CWIP opens 120.56, capex 487.19 in an entity slated for dissolution"}
  - {id: "A3-05", check: "F6", line: "222-224", classification: "FORWARD-SIGNAL", implication: "Draft scheme into Waaree Energies; no appointed date, swap ratio, approvals or timeline; holder value runs through undisclosed ratio"}
  - {id: "A3-06", check: "F8", line: "95, 126, 192", classification: "FORWARD-SIGNAL", implication: "DTA 1,231.45 fully consumed to net DTL (22.81); no current tax line; cash tax at ~25.17% from Q3 FY27"}
  - {id: "A3-07", check: "F8", line: "95, 97, 105", classification: "NEUTRAL-FACT", implication: "FY26 ETR -5.26%, shield 3,043 bps / 7,128.39; FY26 EPS 59.27 = 42.14 at statutory tax; YoY PAT bases distorted"}
  - {id: "A3-08", check: "F9", line: "99", classification: "NEUTRAL-FACT", implication: "Q2 OCI (3.67) = 5.9x FY26 (0.62); immaterial; verify actuarial assumptions at AR"}
  - {id: "A3-09", check: "F12", line: "130, 159, 136, 84, 83", classification: "AMBIGUOUS", implication: "Inventory 10.5x, other current liabilities 11.3x, other current assets 41.8x; advance-funded Q3 deliveries vs pre-merger parent build; Q3 goods revenue separates"}
  - {id: "A3-10", check: "F12", line: "132, 186, 155-156, 187, 193", classification: "AMBIGUOUS", implication: "Receivable fall misses CF by 3,494.18, payable rise by 3,725.18; undisclosed non-cash set-off likely; H1 OCF rests on one-off receivable release"}
  - {id: "A3-11", check: "F12", line: "78-84, 91", classification: "AMBIGUOUS", implication: "PBT ex-OI 3.3% of revenue vs 30.2% YoY; goods materials ratio 82.6% vs 68.9%; cost spike vs group transfer pricing"}
  - {id: "A3-12", check: "F14", line: "101, 105-106", classification: "NEUTRAL-FACT", implication: "EPS in Q2 and 6M columns matches TCI not PAT (1.20 vs 1.21; 10.00 vs 10.01); Ind AS 33 drafting slip"}
  - {id: "A3-13", check: "F14", line: "78, 79, 83, 227", classification: "AMBIGUOUS", implication: "Goods/services swing not a restatement in this filing (6M = Q1+Q2); fits job-work to own-procurement switch; Note 6 generic; Q1 as first reported unverified"}
  - {id: "A3-14", check: "F14", line: "126, 191, 47, 62, 71, 235, 274, 30", classification: "NEUTRAL-FACT", implication: "Presentation and naming inconsistencies; cumulative light drafting control"}
  - {id: "A3-15", check: "F14", line: "283", classification: "NEUTRAL-FACT", implication: "UDIN unreadable in extract; verify on ICAI portal"}
  - {id: "A3-16", check: "F15", line: "223, 30, 21, 56, 71, 231, 225", classification: "FORWARD-SIGNAL", implication: "Entity becomes Transferor to parent; monitoring horizon ends at effectiveness; exposure converts to Waaree Energies"}
forward_signals: ["A3-03", "A3-05", "A3-06", "A3-16"]
ambiguous: ["A3-01", "A3-02", "A3-09", "A3-10", "A3-11", "A3-13"]
commitments:
  - {commitment: "Amalgamate Indosolar into Waaree Energies (Sections 230-232); Indosolar dissolved without winding up on effectiveness", implied_date: "Not stated; board approval 2026-09-23; effectiveness, appointed date, swap ratio NOT FOUND", ref: "Note 4, lines 222-224", status_word: "initiated"}
  - {commitment: "Publish results in newspaper under SEBI LODR Reg 47", implied_date: "Not stated; after 2026-10-21 board meeting", ref: "Outcome letter, line 42", status_word: "initiated"}
  - {commitment: "Make results available on company website", implied_date: "Not stated", ref: "Outcome letter, lines 46-47", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Note 4 (line 222) puts a board-approved draft scheme to merge Indosolar into Waaree Energies. The filing gives no appointed date, swap ratio or timeline, so holder value runs through an undisclosed ratio. Q2 economics broke: PBT excluding other income was 3.3% of revenue against 30.2% a year ago. In the same quarter inventory rose 10.5x and other current liabilities 11.3x. Reading one: advance-funded stock for Q3 deliveries. Reading two: thin-margin goods moved to the group before the merger. Q3 goods revenue and the drawdown of other current liabilities separate them. H1 OCF of 7,956.70 rests on a 15,841.73 receivable release that does not repeat. The recognised DTA is gone (1,231.45 to -22.81), so cash tax starts. FY26 PAT 24,659.91 carried a 7,128.39 book shield against statutory tax (EPS 42.14 at 25.17%, not 59.27). Receivable and payable movements miss the cash flow by about 3,494 and 3,725, consistent with an undisclosed set-off. The goods/services swing is not a restatement inside this filing (6M equals Q1 plus Q2). Q1 as first reported is unverified. EPS in two columns matches TCI, not PAT."
```
