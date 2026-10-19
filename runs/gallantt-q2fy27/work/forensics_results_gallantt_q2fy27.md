# A3 FORENSIC NOTES - GALLANTT (Gallantt Ispat Limited) - Q2 FY27 - doctype: results

Inputs read: A1 structured `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-structured.md` (R001-R449), A1 fulltext `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-fulltext.md` (L1-L1157, statement cells from image transcription L1056-1156), A2 ledger `runs/gallantt-q2fy27/work/ledger_results_gallantt_q2fy27.md`. Prior-quarter fulltext: none. Notion checklist: none. Source PDF and `inputs/` not opened.
Units: Rs lakhs unless stated. "Computed" = arithmetic on filed numbers, not a filed figure. Share count used = 24,128.09 lakhs paid-up / Rs 10 FV = 2,412.809 lakh shares (L1081).

## LEDGER RECONCILIATION
- Ledger rows: 449 (R001-R449, orphan_ids none). Rows read at their cited line: 449. Reconciled: 100%.
- Fulltext spans read: L19-91 (cover letter), L92-421 (pp2-5 duplicate statements, text layer), L423-485 (p6 notes), L486-769 (pp7-9 text layer), L774-868 (p10-11), L870-1054 (auditor reports), L1056-1157 (image transcription).
- Cite-offset notes (quote found in the same paragraph block, no row unlocatable): R399 pincode sits at L874, not L872; R421 pincode at L953, not L951; R048 and R382 meeting date at L433 and L826 (rows cite the paragraph start L429 and L820).
- SUPERSEDED rows (R028, R035, R039, R042, R065, R228, R302, R361) checked against the garbled text layer. Load-bearing cells agree with the transcription, including the associate line on both copies (L153-156 and L542-545 show 169.37 and 8,892.62).
- Statement arithmetic re-footed: P&L all six columns (rounding at most 0.03), balance sheet both dates, cash flow A/B/C both periods. Cash roll 10,165.48 - 10,053.90 = 111.58 ties. Borrowing roll ties: current +6,108.03, non-current -1,679.34, net +4,428.69 = proceeds L1149. Current tax asset rise 2,028.64 = taxes paid 7,929.67 - current tax 5,901.03. DTL rise 486.23 = P&L deferred 480.00 + 6.23 OCI tax (computed at 25.17% on 18.52 net OCI).

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R180-R185, R050, R384 | L1075; L429 | "Share of Profit from Associate \| - \| 169.37 \| - \| - \| 169.37 \| -"; "its sole subsidiary" | AMBIGUOUS | The associate line is live in Q2FY26/H1FY26 (169.37) but nil in the audited FY26 column, although FY26 contains H1FY26. So H2FY26 booked an exact -169.37 offset, or the FY26 column was re-presented. Ask: which associate, when and how it exited, any gain or loss on exit and where it was booked (FY26 investing shows "(Increase)/Decrease in investment" 1,313.07 at L1143). |
| A3-02 | F1 | R289, R297, R312, R316 | L1112, L1116, L1123, L1125 | "dues of micro and small enterprises \| 757.56 \| -"; "Current provisions \| 280.20 \| -"; "Expected credit loss on trade receivables \| 36.16 \| -" | AMBIGUOUS | Four lines were nil in the audited FY26 accounts and turned live in H1FY27. H1FY27 is the first period under the new auditor (A3-05). Nil MSME dues at an audited year-end for a manufacturer with Rs 4,41,892 lakh revenue is a classification question, and Sec 43B(h) payment-timing disallowance depends on it. Ask: were these reclassifications or new policies, and were the FY26 comparatives restated. |
| A3-03 | F2 | R402, R403, R019 | L887; L54 | "We have reviewed the accompanying Statement of Unaudited Standalone Financial Results"; "The full format of the standalone and consolidated financial results" | AMBIGUOUS | The auditor reviewed a standalone statement that this filing does not contain. The S-vs-C gap cannot be computed from filed statements. Proxy from the auditor paragraph: subsidiary loss 0.01 lakhs, so S is about equal to C in FY27. In Q2FY26 the gap was the associate 169.37 = 1.94% of pre-associate PAT (computed). The change is under 5 pp, so the trend trigger does not fire. Reg 33 calls for both sets. A4: confirm the standalone statement is on BSE/NSE. |
| A3-04 | F3 | R429-R441 | L1013-1015; L993 | "total assets of Rs. 627.35 Lakhs ... total revenues of Rs. Nil and Rs. Nil, total net (loss) of Rs. 0.01 Lakhs" | AMBIGUOUS | Suryalaxmi Technologies Pvt Ltd is a non-operating shell. It has nil revenue, holds 627.35 lakhs of assets (0.14% of group, computed) and had a 1.08 lakh cash outflow. There is no going concern paragraph. Note 4 names "real estate operations" (L451). Ask: what assets the shell holds, why it is kept, and any plan to use or wind it up. |
| A3-05 | F5 | R409-R413, R443-R445 | L926; L1032 | "reviewed/audited by the predecessor auditor whose reports dated July 27, 2026, November 03, 2025 and May 05, 2026" | AMBIGUOUS | This is the first review by Singhi & Co. The Q1FY27 review (27 Jul 2026) was by the predecessor, so the change happened between 27 Jul and 19 Oct 2026, probably at the 30 Sep 2026 AGM. The predecessor is not named. This Other Matter paragraph is new by construction. No verbatim diff was possible because no prior extract was supplied. Ask: who the predecessor was, and was it rotation or resignation (a resignation needs a Reg 30 reasons disclosure). First-review quarters carry reclassification risk (see A3-02, A3-09, A3-10). |
| A3-06 | F6 | R017, R018, R019 | L52-55 | "shall be published in all editions of Business Standard"; "shall be available on the websites of the Stock Exchanges" | AMBIGUOUS | There are two dated commitments. Newspaper extract is due within 48h (about 21 Oct 2026). Full standalone and consolidated results go to the exchanges. The filing itself does not meet the second one for the standalone set (A3-03). The lexicon found no project, capacity or commissioning commitment, although CWIP grew 71% (A3-11). |
| A3-07 | F8 | R156-R173 | L1072; L1073 | "Deferred tax \| 277.96 \| (637.18) \| 202.03 \| 480.00 \| (1,470.24) \| (3,830.43)" | FORWARD-SIGNAL | ETR (computed): Q2FY27 27.25%, Q1FY27 24.97%, H1FY27 25.73%, against Q2FY26 15.31%, H1FY26 18.27% and FY26 19.83%. Statutory rate is 25.17%. FY26 carried a 634 bps deferred credit (3,830.43 / 60,403.48), Q2FY26 619 bps. FY27 now books deferred charges. The swing explains part of why Q2 PAT fell 32.0% YoY while PBT fell 19.3%. Base cases must not carry the FY26 ETR forward. Ask: what drove the FY26 DTL release, and why the Q2FY27 ETR is above statutory. No earlier-year tax line exists. |
| A3-08 | F9 | R192-R209 | L1077 | "OCI A. items not reclassified to P&L \| (33.66) \| (114.51) \| 52.18 \| 18.52 \| (9.46) \| 28.74" | NEUTRAL-FACT | Q1FY27 (+52.18) and Q2FY27 (-33.66) each exceed the FY26 full-year OCI (28.74) in size. Q2FY26 (-114.51) was 4x FY26. The mechanical trigger fires, but the amounts are under 0.6% of quarterly PAT. Verify the actuarial assumptions and any FVOCI equity component at the FY26/FY27 Annual Report. |
| A3-09 | F10 | R222-R227, R187, R190, R175, R178 | L1082; L1076 | "Basic and diluted EPS ... \| 2.51 \| 3.62 \| 5.13 \| 7.63 \| 10.82 \| 20.07"; "Profit for the period/year (after associate) \| 6,051.07 \| 8,892.62" | AMBIGUOUS | Paid-up capital is flat at 24,128.09 in all periods, and basic equals diluted (no dilutive instruments). But the comparative EPS uses pre-associate profit. 8,723.25 / 2,412.809 = 3.62, while the reported 8,892.62 gives 3.69. H1FY26 shows 10.82 against 10.89 on the reported profit. Either EPS is misstated, or the associate line was added to the comparatives without re-running EPS. On a consistent basis the YoY EPS change is -31.9%, not the -30.7% shown. The number is small. As a governance data point it fits A3-01 and A3-05. |
| A3-10 | F11 | R270-R275, R213, R056, R057, R292, R370 | L1104; L1080; L458; L1151 | "Other equity \| 3,24,526.04 \| 3,07,495.39"; "recommended a final dividend of Rs. 2/-per equity share"; "Dividend Paid \| - \| (940.46)" | AMBIGUOUS | Net worth ties: 24,128.09 + 3,24,526.04 = 3,48,654.13. The roll-forward does not tie. Opening other equity 3,07,495.39 + H1 TCI 18,436.30 = 3,25,931.69 against a closing 3,24,526.04, so 1,405.65 is unexplained (0.40% of net worth). The Rs 2 dividend (4,825.62 computed) was approved on the balance-sheet date (30 Sep 2026), so it should be a liability at 30 Sep. Neither the equity reduction (1,405.65) nor the rise in other current financial liabilities (+1,304.27) matches it. Candidate items: partial dividend recognition, another reserve movement, a misclassification. There is no third-party net-worth figure to test, so the 5% trigger does not apply. The finding is the internal break. |
| A3-11 | F12 | R234, R235, R347, R348, R120-R122, R232-R237 | L1085; L1141; L1065 | "Capital work in progress \| 59,836.94 \| 34,905.32"; "Purchase of fixed assets (incl intangible assets and CWIP) \| (27,846.60) \| (34,815.06)" | FORWARD-SIGNAL | This is a pre-commissioning build. CWIP rose 24,931.62 (+71.4%) in six months. H1 capex 27,846.60 = 80.0% of FY26 full-year capex in half the time. It ties to CWIP +24,931.62, capital advances +1,895.56 and small PPE additions. The filing names no project, cost or commissioning date. D&A rose 17.9% QoQ (3,011.47 to 3,550.62) while net PPE fell 4,218.09 and intangibles fell 1,369.83. Ask: the project, capacity, total cost, funding mix, commissioning date, and what was capitalised or amortised in Q2. |
| A3-12 | F12 | R258, R259, R354, R353, R256, R257, R286, R309 | L1097; L1144; L1096; L1111 | "Loans \| 26,578.46 \| 29,649.96"; "Movement in loans and advances \| 3,071.49 \| (29,649.96)" | AMBIGUOUS | A current loan book of 29,649.96 was built from nil in FY26 (the FY26 outflow equals the year-end balance). It stands at 26,578.46. Beside it sit 40,165.53 of other bank balances and 50,568.66 of current borrowings. H1 interest income 3,530.19 = 14.2% of H1 PBT, and Q2 other income is 21.8% of Q2 PBT (computed). Ask: the counterparties, related-party status, rate, tenor and security. A steel maker that borrows short and lends short needs that explained. |
| A3-13 | F12 | R254, R255, R345, R321, R286, R276, R374 | L1095; L1140; L1128 | "Cash and cash equivalent \| 111.58 \| 10,165.48"; "Net cash generated from operating activities \| 9,082.36" | FORWARD-SIGNAL | Cash fell 10,053.90 to 111.58. CFO was 9,082.36 against PAT 18,417.78 (49%, computed), after an 11,788.93 inventory build (+21.4%) on flat QoQ revenue. Capex was funded by the cash drawdown plus net borrowing of 4,428.69. Debt shifted to short tenor: current +6,108.03, non-current -1,679.34. Q3 must also fund the 4,825.62 dividend (A3-15). Watch: bank balances or loans drawn down, or current debt up again, in Q3. |
| A3-14 | F12 | R053, R055, R096-R098, R090-R092, R102-R104 | L448-455; L1061; L1060 | "no separate segment disclosures are provided"; "Purchase of stock in trade \| 9,886.58 \| 510.26 \| 878.47" | AMBIGUOUS | Note 4 keeps one segment. Meanwhile stock-in-trade purchases rose 11.3x QoQ and 19.4x YoY. Revenue was flat QoQ (+0.02%). Material cost was 79.0% of revenue, against 72.7% in Q1FY27 and 74.5% in Q2FY26. Computed EBITDA margin was 9.6% in Q2FY27, against 16.2% in Q1FY27 and 13.0% in Q2FY26. Traded goods replaced own output or carried thin margin, and the mix is not disclosed. Ask: the traded volume and product, and the own-manufactured volume and realisation in Q2. |
| A3-15 | F13 | R056-R061, R011, R022 | L457-460; L35 | "approved in the Annual General Meeting dated September 30, 2026"; "COMMENCED AT 04.30 P.M. AND CONCLUDED AT 11:00 P.M." | FORWARD-SIGNAL | The FY26 Annual Report was published before the 30 Sep 2026 AGM, so a Role 6 AR deep dive can be scheduled now. Companies Act s.127 requires the declared dividend to be paid within 30 days, by about 30 Oct 2026. That is a Q3 outflow of 4,825.62 (computed), 5.1x the FY26 dividend outflow of 940.46. The auditor appointment was probably approved at the same AGM. This is inference; confirm it in the AGM outcome. The board sat 6.5h on one disclosed agenda item. No director appointments, fund-raising enablers or record dates are in this filing. |
| A3-16 | F14 | R009, R010, R012, R399, R421, R402 | L34 vs L37; L926; L885; L874 vs L953 | "HELD ON NOVEMBER 03, 2025"; "Monday, 19` October, 2026"; "To the Board of Directors of Gallant Ispat Limited" | NEUTRAL-FACT | The subject-line date 03 Nov 2025 equals the predecessor's Q2FY26 report date (L926), so the outcome letter is last year's template, not fully updated. Other items: the company name is misspelt in the standalone review report (L885), the auditor pincode reads 201 304 at L874 but 201 301 at L953, para 5 says "other auditors" (L1003) for one subsidiary, and P&L item numbering skips 13 (L168-170). The two UDINs differ (L942, L1054), which is expected with one UDIN per report, so that is not a finding. Each item is immaterial alone. Together they are a governance data point (see A3-09). |
| A3-17 | F15 | R050, R384, R429, R430, R181, R184 | L993; L1075 | "Suryalaxmi Technologies Private Limited  Wholly-owned subsidiary" | AMBIGUOUS | No prior-quarter list was supplied, but the filing shows a change in the year-ago perimeter. An associate was equity-accounted in Q2FY26 (169.37) and is not in the current entity list (one wholly-owned subsidiary only). The associate's name, exit date and mode are not stated. Tie this to A3-01 for the accounting. |

## CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 27 zero-standing cells read. Exceptional items (L1069) and OCI-B (L1078) are template lines, nil in every period. The associate line is inconsistent between FY26 and H1FY26 (A3-01). Four lines nil at audited FY26 went live under the new auditor (A3-02). Subsidiary nil lines go to F3. |
| F2 | FINDING | No standalone statements are filed despite the standalone review report. The decomposition rests on the auditor-paragraph proxy. The gap change is under 5 pp (A3-03). |
| F3 | FINDING | The sole subsidiary is a non-operating shell: nil revenue, 627.35 assets, no GC paragraph (A3-04). |
| F4 | PASS | Other-auditor reliance covers a loss of 0.01 lakhs (about 0.0002% of Q2 PAT) and assets of 627.35 (0.14%). This is far under 10%. No prior period is available to trend. |
| F5 | FINDING | A new predecessor-auditor Other Matter paragraph follows the auditor change. There is no going concern EoM. No verbatim diff was possible without a prior extract (A3-05). |
| F6 | FINDING | The lexicon hits are L35 (meeting time, not a commitment), L53, L55 and L162/L549 (template). Two commitments are registered. One is not met inside this filing (A3-06). |
| F7 | PASS | No lexicon hedge hits. The management-materiality statements at L451 and L1024-1026 are not revenue or customer hedges. |
| F8 | FINDING | The ETR normalised from 19.83% (FY26) to 25.73% (H1FY27). The deferred-tax sign flipped from credits to charges. Q2 ETR is above statutory (A3-07). |
| F9 | FINDING | Single-quarter OCI exceeds the FY26 full-year figure in size. The amounts are immaterial (A3-08). |
| F10 | FINDING | Paid-up capital is flat and basic equals diluted. The comparative EPS excludes the associate share (A3-09). |
| F11 | FINDING | Net worth ties, but the other-equity roll-forward misses by 1,405.65. The 30 Sep dividend liability is not visible (A3-10). |
| F12 | FINDING | There are no segments, so the asset-trend rule is applied at group level: CWIP build (A3-11), loan book (A3-12), liquidity drawdown (A3-13), and a single-segment note hiding a trading-mix shift (A3-14). |
| F13 | FINDING | AGM held, so the AR is available and the dividend outflow is due by about 30 Oct 2026. The auditor appointment is probably from the AGM. The meeting was 6.5h long (A3-15). |
| F14 | FINDING | Cover-letter date template, name misspelling, pincode mismatch, "other auditors" plural, numbering skip (A3-16). |
| F15 | FINDING | The year-ago associate is absent from the current perimeter (A3-17). |
| F16 | N.A. | Presentation-only check. The doctype is results. |
| F17 | N.A. | Concall-only check. The doctype is results, and no Notion checklist exists. |

## COMMITMENT REGISTER (F6, plus dateable board facts)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Publish the results extract in all editions of Business Standard (English) and a Hindi newspaper (Reg 47) | about 21 Oct 2026 (48h from meeting) | Cover letter L52-54 | initiated (stated, not yet evidenced) |
| Full-format standalone and consolidated results available on BSE/NSE websites | with filing, 19 Oct 2026 | Cover letter L54-57 | initiated (standalone set absent from this document) |
| Pay the FY26 final dividend of Rs 2/share (4,825.62 lakhs computed) | by about 30 Oct 2026 (Companies Act s.127, 30 days from 30 Sep 2026 declaration) | Note 5 L457-460; CF L1151 nil paid H1 | underway (approved, unpaid at 30 Sep) |
| Capital project in CWIP (59,836.94) | NOT FOUND (no project, cost or date disclosed) | BS L1085; CF L1141 | underway (spend evidenced, no stated milestone) |

## FLAGS FOR A4 (management questions)
FORWARD-SIGNAL: A3-07, A3-11, A3-13, A3-15. AMBIGUOUS: A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-09, A3-10, A3-12, A3-14, A3-17.

```yaml
stage: A3-forensics
company: "GALLANTT"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/gallantt-q2fy27/work/forensics_results_gallantt_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L1075; L429", classification: "AMBIGUOUS", implication: "Associate share 169.37 in Q2/H1FY26 but nil in audited FY26 column; H2FY26 offset or re-presentation; ask identity, exit, gain/loss booking"}
  - {id: "A3-02", check: "F1", line: "L1112; L1116; L1123; L1125", classification: "AMBIGUOUS", implication: "MSME payables 757.56, current provisions 280.20, FV gain 65.29, ECL 36.16 all nil at audited FY26, live in first new-auditor period; reclassification or new policy; 43B(h) relevance"}
  - {id: "A3-03", check: "F2", line: "L887; L54", classification: "AMBIGUOUS", implication: "Standalone review report but no standalone statements filed; S-vs-C proxy gap ~0 in FY27 vs 1.94% of PAT in Q2FY26 (<5pp); confirm standalone on exchanges (Reg 33)"}
  - {id: "A3-04", check: "F3", line: "L1013-1015", classification: "AMBIGUOUS", implication: "Suryalaxmi Technologies is a nil-revenue shell holding 627.35 lakhs assets; ask what it holds and plan"}
  - {id: "A3-05", check: "F5", line: "L926; L1032", classification: "AMBIGUOUS", implication: "Auditor changed between 27 Jul and 19 Oct 2026; predecessor unnamed; rotation vs resignation; first-review reclass risk"}
  - {id: "A3-06", check: "F6", line: "L52-55", classification: "AMBIGUOUS", implication: "Committed standalone+consolidated results on exchange sites; standalone absent here; no project commitment despite CWIP +71%"}
  - {id: "A3-07", check: "F8", line: "L1072; L1073", classification: "FORWARD-SIGNAL", implication: "ETR 25.73% H1FY27 (Q2 27.25%) vs 19.83% FY26 with 634 bps deferred credit; PAT -32.0% YoY vs PBT -19.3%; do not carry FY26 ETR forward"}
  - {id: "A3-08", check: "F9", line: "L1077", classification: "NEUTRAL-FACT", implication: "Quarterly OCI (+52.18, -33.66) exceeds FY26 full year 28.74; immaterial; verify assumptions at AR"}
  - {id: "A3-09", check: "F10", line: "L1082; L1076", classification: "AMBIGUOUS", implication: "No dilution (paid-up flat, basic=diluted) but comparative EPS 3.62/10.82 computed on pre-associate PAT (3.69/10.89 on reported)"}
  - {id: "A3-10", check: "F11", line: "L1104; L1080; L458; L1151", classification: "AMBIGUOUS", implication: "Other equity roll-forward misses by 1,405.65; Rs 2 dividend (4,825.62) approved on BS date not visible as liability or cash outflow"}
  - {id: "A3-11", check: "F12", line: "L1085; L1141; L1065", classification: "FORWARD-SIGNAL", implication: "CWIP +24,931.62 (+71.4%) in 6m, H1 capex 80% of FY26; no project/cost/COD disclosed; D&A +17.9% QoQ with PPE down"}
  - {id: "A3-12", check: "F12", line: "L1097; L1144; L1111", classification: "AMBIGUOUS", implication: "Loan book 26,578.46 built from nil in FY26 beside 50,568.66 current borrowings; interest income 14.2% of H1 PBT; ask counterparties, related-party status"}
  - {id: "A3-13", check: "F12", line: "L1095; L1140; L1128", classification: "FORWARD-SIGNAL", implication: "Cash 10,165.48 to 111.58; CFO 49% of PAT after 11,788.93 inventory build; debt shifting short; Q3 must fund dividend 4,825.62"}
  - {id: "A3-14", check: "F12", line: "L448-455; L1061; L1060", classification: "AMBIGUOUS", implication: "Single-segment note while stock-in-trade purchases 11.3x QoQ on flat revenue; material cost 79.0% vs 72.7%; computed EBITDA margin 9.6% vs 16.2% Q1"}
  - {id: "A3-15", check: "F13", line: "L457-460; L35", classification: "FORWARD-SIGNAL", implication: "AGM held 30 Sep so FY26 AR available for Role 6; dividend payable by ~30 Oct 2026 (s.127), 5.1x FY26 outflow; auditor appointment likely at AGM (confirm)"}
  - {id: "A3-16", check: "F14", line: "L34; L37; L885; L874; L953", classification: "NEUTRAL-FACT", implication: "Cover letter carries 03 Nov 2025 (last year's Q2 date); 'Gallant' misspelt; auditor pincode mismatch; cumulative governance data point"}
  - {id: "A3-17", check: "F15", line: "L993; L1075", classification: "AMBIGUOUS", implication: "Year-ago associate absent from current perimeter; name, exit date and mode not stated"}
forward_signals: ["A3-07", "A3-11", "A3-13", "A3-15"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-04", "A3-05", "A3-06", "A3-09", "A3-10", "A3-12", "A3-14", "A3-17"]
commitments:
  - {commitment: "Publish results extract in Business Standard and Hindi daily (Reg 47)", implied_date: "~2026-10-21", ref: "Cover letter L52-54", status_word: "initiated"}
  - {commitment: "Full standalone and consolidated results on BSE/NSE websites", implied_date: "2026-10-19", ref: "Cover letter L54-57", status_word: "initiated"}
  - {commitment: "Pay FY26 final dividend Rs 2/share (4,825.62 lakhs computed)", implied_date: "~2026-10-30 (s.127)", ref: "Note 5 L457-460; CF L1151", status_word: "underway"}
  - {commitment: "Capital project in CWIP 59,836.94", implied_date: "NOT FOUND", ref: "BS L1085; CF L1141", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Consolidated-only results filing. The standalone set is missing despite a standalone review report. Three threads for A4. (1) Q2 earnings quality fell. Computed EBITDA margin was 9.6% against 16.2% in Q1. Material cost rose to 79.0% of revenue from 72.7%. Stock-in-trade purchases rose 11.3x on flat revenue. Tax normalised to 25.7% from FY26's 19.8%, so PAT fell 32% YoY on a 19% PBT fall. (2) The liquidity squeeze looks like a choice, not a shortfall. Cash is 111.58 lakhs, but 40,165.53 of bank balances and a 26,578.46 inter-corporate loan book sit beside 50,568.66 of short-term debt. CWIP rose 71% with no project disclosed. A 4,825.62 lakh dividend falls due by about 30 Oct 2026. The loan counterparties are the top question. (3) This is the first review by a new auditor, and the predecessor is unnamed. Four lines that were nil at audited FY26 went live. Other equity misses its roll-forward by 1,405.65. Comparative EPS ignores the associate share. The cover letter carries last year's date. Each item is small. Together they say the books were re-cut this quarter. Lean bear until management explains."
```
