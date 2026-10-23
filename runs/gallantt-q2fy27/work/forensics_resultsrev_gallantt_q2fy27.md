# A3 FORENSIC NOTES - GALLANTT (Gallantt Ispat Limited) - Q2 FY27 - doctype: results (resultsrev, REVISED board outcome filed 21-Oct-2026)

Inputs read: A1 structured `runs/gallantt-q2fy27/extracted/gallantt-resultsrev-q2fy27-structured.md` (R001-R743), A1 fulltext `runs/gallantt-q2fy27/extracted/gallantt-resultsrev-q2fy27-fulltext.md` (L1-L1259), A2 ledger `runs/gallantt-q2fy27/work/ledger_resultsrev_gallantt_q2fy27.md`. Prior extract: the ORIGINAL 19-Oct filing, same quarter (`extracted/gallantt-results-q2fy27-structured.md`, rows R009, R010, R022, R403 and header notes L6-7 used for the revision diff). Earlier forensics: `work/forensics_results_gallantt_q2fy27.md` (A3-01 to A3-17). Checklist: `work/review_gallantt_q2fy27.md` Step 8.5 (L424-456) and Monitorables (L473-489). No Notion page (PRE-THESIS READ). Loop 1 addition only: presentation and concall structured files searched for the FY26 asset sale. Source PDF and `inputs/` not opened.
Units: Rs lakhs unless stated. "Computed" = arithmetic on filed cells. Share count = 24,128.09 / Rs 10 = 2,412.809 lakh shares (L213). S = standalone (pp2-6, new). C = consolidated (pp7-11, carried unchanged). All line numbers are revised-fulltext lines unless prefixed "R:" (original results fulltext). Scope per task: carried consolidated checks are not redone. F1-F17 run on the standalone pages, plus the S-vs-C bridge, the earlier-finding status table and the revision as a governance event.

## LEDGER RECONCILIATION
- Ledger rows: 743 (R001-R743, orphan_ids none). Rows read at their cited line: 743. Reconciled: 100%.
- New rows R001-R358 read at L24-572. Every standalone statement cell (R035-R178, R187-R257, R263-R337) was read at its image-transcription line (L191-214, L316-350, L444-471, L521-527) and spot-checked against the garbled text layer (L94-164, L218-303, L353-425, L474-498). Load-bearing cells agree, including PAT 48,427.31 (L147) and dividend nil (L486 shows "7", OCR noise; the transcription "-" is taken).
- Carried rows R359-R743 read at their lines (L587-1257). A1's DIFF section (structured L758-767) states every carried cell is identical to the original. Spot checks on the P&L, balance sheet, cash flow and auditor rows agree.
- Cite offsets (quote in the same block, no row unlocatable): R684 dividend note text starts at L949, not L950. The R693 pincode "201 304" is at L975, not L973. The R715 pincode "201 301" is at L1054, not L1052.
- Re-footing (S): P&L foots in all six columns within 0.02. Balance sheet foots exactly at both dates. Cash flow foots. Closing cash 108.56 (L527) = balance-sheet cash (L327). Borrowing roll ties: current +6,108.03, non-current -1,679.34, net +4,428.69 = proceeds (L521). DTL rise 486.22 = P&L deferred 480.00 (L206) + 6.22 OCI tax (computed at 25.17% on 18.52 net OCI).
- PIPELINE NOTE (A1 artefacts, not company findings). (1) R697 context still reads "the standalone statement itself is not in this document". That is false for this file. (2) Fulltext L1258, carried from the original, says "Pages 2-5 carry a duplicate copy of the same consolidated statements". This contradicts L190-528 of this file. Both are stale carries. A4 must not quote them.

## S-vs-C BRIDGE (task item b; F2/F3 basis)

P&L, C minus S (Rs lakhs). Revenue, other income, total income, raw material, stock-in-trade purchases, inventory change, employee cost, finance cost, D&A and tax are identical in all six columns (L191-207 vs L1158-1174).

| line | Q2FY27 | Q2FY26 | Q1FY27 | H1FY27 | H1FY26 | FY26 |
|---|---|---|---|---|---|---|
| Other expenses (L200 vs L1167) | 0.00 | 0.00 | 0.00 | +0.01 | 0.00 | +0.60 |
| PBT (L204 vs L1171) | 0.00 | 0.00 | 0.00 | -0.01 | 0.00 | -0.60 |
| PAT pre-associate (L208 vs L1175) | 0.00 | 0.00 | 0.00 | -0.01 | 0.00 | -0.61 |
| Associate share, C only (L1176) | - | +169.37 | - | - | +169.37 | - |
| PAT after associate (L208 vs L1177) | 0.00 | +169.37 | 0.00 | -0.01 | +169.37 | -0.61 |
| Gap as % of S PAT (computed) | 0.00% | +1.94% | 0.00% | -0.0001% | +0.65% | -0.0013% |
| TCI (L212 vs L1181) | 0.00 | +169.37 | 0.00 | -0.01 | +169.36 | -0.61 |
| EPS, Rs (L214 vs L1183) | 2.51 = 2.51 | 3.62 = 3.62 | 5.13 = 5.13 | 7.63 = 7.63 | 10.82 = 10.82 | 20.07 = 20.07 |

Decomposition: the subsidiary contributes -0.01 (H1FY27) and -0.61 (FY26) through other expenses. The associate contributes +169.37 in Q2/H1FY26 only. The P&L shows no eliminations: revenue, other income and interest income are identical. The gap moved from +1.94% (Q2FY26) to 0.00% (Q2FY27), a 1.94 pp change, below the 5 pp trigger. Rounding note: the auditor states a subsidiary quarter loss of "Rs. 0.01 Lakhs" (L1116). The Q2 columns show S = C = 6,051.07 (L208, L1175). That is a 0.01 rounding difference and immaterial.

Balance sheet, C minus S, and the implied subsidiary (Rs lakhs; computed):

| line | 30-Sep-2026 | 31-Mar-2026 | reading |
|---|---|---|---|
| PPE (L316 vs L1185) | +180.46 | +86.79 | subsidiary fixed assets |
| CWIP (L317 vs L1186) | +24.38 | +2.36 | subsidiary CWIP |
| Other non-current assets (L322 vs L1191) | +419.37 | 0.00 | subsidiary advance paid in H1 |
| Non-current investments (L320 vs L1189) | -1.00 | -1.00 | parent's equity in subsidiary, eliminated |
| Cash (L327 vs L1196) | +3.02 | +4.11 | subsidiary cash (fall 1.09 vs auditor "1.08", L1118) |
| Loans (L329 vs L1198) | -603.32 | -92.36 | parent loan to subsidiary, eliminated |
| Other current financial assets (L330 vs L1199) | -22.01 | 0.00 | intra-group receivable, eliminated |
| Other equity (L336 vs L1205) | -0.50 | -0.49 | subsidiary cumulative loss |
| DTL (L340 vs L1209) | -0.11 | -0.12 | subsidiary DTA netted |
| Other current liabilities / payables (L347 vs L1216; L345 vs L1214) | +1.52 | +0.50 | subsidiary payables |
| Total assets (L334 vs L1203) | +0.91 | -0.10 | ties |

Implied subsidiary gross assets at 30-Sep = 180.46 + 24.38 + 419.37 + 3.02 + 0.01 receivable + 0.11 DTA = 627.35, equal to the auditor's "total assets of Rs. 627.35 Lakhs" (L1114). Parent funding is 603.32 loan + 22.01 receivable + 1.00 equity = 626.33, or 99.7% of the subsidiary's assets (computed). Cash flow cross-check: C capex 27,846.60 (L1242) less S capex 27,311.52 (L465) = 535.08 subsidiary capex in H1. C loans movement 3,071.49 (L1245) less S 2,560.54 (L468) = 510.95 = the intra-group loan increase.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3R-01 | F1 | R243-R244, R252-R253, R269-R270, R273-R274, R107-R112, R149-R154 | L344; L348; L447; L449 | "Trade payables: dues of micro and small enterprises \| 757.56 \| -"; "Current provisions \| 280.20 \| -"; "Expected credit loss on trade receivables \| 36.16 \| -" | AMBIGUOUS | The four lines that were nil at audited FY26 and live in H1FY27 (A3-02) are identical in the standalone set. They sit in the parent, not the subsidiary. The audited FY26 standalone comparatives were not restated: MSME dues and current provisions are still nil at 31-Mar-2026. So either these are new classifications under the new auditor, or FY26 was understated. Exceptional items (L203) and OCI-B (L210) are template lines, nil in all six columns. The H1 "Proceed from sale of property, plant & equipment" is nil, against 11,030.50 in FY26 (L466). That FY26 asset sale is not repeated (see A3R-15). |
| A3R-02 | F2 | R137-R142, R173-R178 vs R468-R485, R516-R521 | L208; L1175-1177; L214; L1183 | "Profit for the period/year (7-8) \| ... \| 48,427.31"; "Share of Profit from Associate \| - \| 169.37 \| - \| - \| 169.37 \| -" | AMBIGUOUS | The S-vs-C gap is near zero in FY27 and below the 5 pp trigger (bridge above). The standalone set proves one more thing. Audited FY26 C PAT (48,426.70) = S PAT (48,427.31) less the subsidiary loss 0.61. FY26 other income is identical in S and C (L192, L1159), so no different disposal gain or loss was booked in C. The audited FY26 consolidated therefore carries no associate result at all. Yet the H1FY26 comparative, which sits inside FY26, carries +169.37. The two columns cannot both be right unless H2FY26 booked exactly -169.37 with no disclosure. Ask: which column is right, and was the H1FY26 comparative re-presented. |
| A3R-03 | F3 | R187-R192, R195-R196, R199-R200, R209-R216, R305, R311 vs R526-R555, R641, R647; R727, R734 | L316-330 vs L1185-1199; L465 vs L1242; L1114 | "total assets of Rs. 627.35 Lakhs ... total revenues of Rs. Nil" | AMBIGUOUS | P&L cost lines are identical in S and C (L194-200 vs L1161-1167), so the subsidiary has no operations. That confirms the shell for the P&L. The balance sheet says it is not dormant. Suryalaxmi Technologies spent 535.08 on assets in H1 (computed, L1242 less L465): PPE +93.67, CWIP +22.02 and a new 419.37 non-current advance. The parent funded this with a loan that rose 6.5x, from 92.36 to 603.32 (computed). The subsidiary books a 0.01 loss on 180.46 of PPE, so no depreciation shows. That fits land [INFERENCE]. Note 4 names "real estate operations" (L553). There is no going concern paragraph. The amounts are small: 1.9% of group H1 capex and 0.14% of group assets. Ask: what the subsidiary is buying, the purpose, and whether the parent loan is interest-bearing. |
| A3R-04 | F3 | R216 vs R554; R315 vs R651; R189-R190 vs R528-R529 | L330 vs L1199; L470 vs L1247; L317 vs L1186 | "Other financial assets (current) \| 32,631.38"; "Interest received \| 2,900.17" vs "\| 2,922.18" | AMBIGUOUS | A 22.01 intra-group receivable appeared in H1. It is eliminated from C's balance sheet, but C shows 22.01 more "interest received" than S. Interest income is identical in S and C (3,530.19, L446, L1223). The subsidiary's CWIP rose 22.02 in H1. One reading [INFERENCE]: the parent charged 22.01 of interest on the intra-group loan, the subsidiary capitalised it into CWIP, and consolidation eliminated the receivable but not the income or the capitalised cost. That would overstate C PBT and C CWIP by about 22.01 (0.09% of H1 PBT). The amount is immaterial. It is a consolidation-quality data point in the first quarter under the new auditor. Ask: the nature of the 22.01, and whether intra-group interest is eliminated. |
| A3R-05 | F6 | R017, R018, R350-R355, R328 | L56-61; L557-559; L523 | "shall be available on the websites of the Stock Exchanges"; "approved in the Annual General Meeting dated September 30, 2026"; "Dividend Paid \| - \| (940.46)" | AMBIGUOUS | Commitment status changes. The full standalone set promised on the exchange sites is now filed, but on 21-Oct 16:56, not on 19-Oct (status: completed, late; see A3R-12). There is still no evidence of the Reg 47 newspaper extract. The dividend is approved but unpaid at 30-Sep. No lexicon hit names a project, capacity or commissioning date, although parent CWIP rose 24,909.60 (+71.4%, L317). The lexicon found nothing else in pp2-6. |
| A3R-06 | F8 | R119-R136, R235-R236, R217-R218 | L205-207; L340; L331 | "Deferred tax \| 277.96 \| (637.18) \| 202.03 \| 480.00 \| (1,470.24) \| (3,830.43)" | FORWARD-SIGNAL | Standalone tax lines equal consolidated in every column, so the whole FY26 deferred credit sits in the parent. Standalone ETR (computed): Q2FY27 27.25%, Q1FY27 24.97%, H1FY27 25.73%, against Q2FY26 15.31%, H1FY26 18.27% and FY26 19.83%. The FY26 deferred credit is 634 bps of S PBT (3,830.43 / 60,404.08). Current tax assets rose 2,028.64 (L331), equal to taxes paid 7,929.67 (L463) less current tax 5,901.03. H1 advance tax ran ahead of the H1 charge. A3-07 is confirmed. Do not carry the FY26 ETR forward. |
| A3R-07 | F9 | R143-R160 | L209-211 | "OCI A. items not reclassified to P&L \| (33.66) \| (114.51) \| 52.18 \| 18.52 \| (9.46) \| 28.74" | NEUTRAL-FACT | Standalone OCI equals consolidated in every column, so the subsidiary has no OCI. The mechanical trigger still fires: each FY27 quarter exceeds the FY26 full-year OCI in size. The amounts are under 0.6% of quarterly PAT. Verify the actuarial assumptions in the FY26 Annual Report (A3-08). |
| A3R-08 | F10 | R167-R178 vs R516-R521; R140-R141 | L213-214; L1183; L1177 | "Basic and diluted EPS (not annualised), Rs \| 2.51 \| 3.62 \| 5.13 \| 7.63 \| 10.82 \| 20.07" | AMBIGUOUS | Paid-up capital is 24,128.09 in all columns, and basic equals diluted. No dilution. Standalone EPS ties to standalone PAT in every column: 8,723.25 / 2,412.809 = 3.62. Consolidated EPS equals standalone EPS in every column, including Q2FY26 and H1FY26, where consolidated profit after associate is 8,892.62 (3.69) and 26,272.05 (10.89). The consolidated comparative EPS row was therefore computed on standalone profit. This is the mechanism behind A3-09. It is unfixed in the revision. |
| A3R-09 | F11 | R225-R230, R248-R251, R350-R351, R328-R329 | L335-337; L346; L557; L523 | "Other equity \| 3,24,526.54 \| 3,07,495.88"; "Other financial liabilities (current) \| 3,023.79 \| 1,719.51" | AMBIGUOUS | Net worth ties: 24,128.09 + 3,24,526.54 = 3,48,654.63 (L337). The roll-forward does not. Opening 3,07,495.88 + H1 TCI 18,436.31 = 3,25,932.19, against a closing 3,24,526.54. The 1,405.65 gap is identical to the consolidated gap, so the break sits in the parent. It equals Rs 0.58/share. The Rs 2 dividend approved on 30-Sep (4,825.62, computed) is not visible: other financial liabilities rose only 1,304.28. The FY26 dividend outflow of 940.46 (L523) equals Rs 0.39/share, also not a round per-share figure. A partial waiver by some holders is one candidate [INFERENCE]. There is no third-party net-worth figure, so the 5% test does not apply. Ask: reconcile the 1,405.65, the dividend liability at 30-Sep, and any waiver. |
| A3R-10 | F12 | R189-R190, R203-R204, R209-R214, R231-R232, R241-R242, R279, R303, R305, R311-R312 | L317; L324; L327; L329; L464; L465; L468 | "Capital work in progress \| 59,812.56 \| 34,902.96"; "Cash and cash equivalent \| 108.56 \| 10,161.37"; "Movement in loans and advances \| 2,560.54 \| (29,742.32)" | FORWARD-SIGNAL | There are no segments (Note 4, L550-555), so the asset-trend rule runs at entity level. The parent carries 98.1% of group H1 capex (27,311.52 of 27,846.60), 99.9% of the CWIP rise (24,909.60 of 24,931.62), all of the inventory build (+11,788.93, +21.4%) and the cash drawdown to 108.56. S CFO/PAT = 49.3% (9,081.33 / 18,417.79). The standalone loan book was also built from nil in FY26: the FY26 movement (29,742.32) equals the 31-Mar balance. It now holds 603.32 lent to the subsidiary (2.2%). The third-party book is 26,578.46. S net debt is 16,589.15 (computed: borrowings 59,197.39 less cash, other bank balances and current investments). A3-11, A3-12 and A3-13 are confirmed in the parent. |
| A3R-11 | F13 | R350-R355, R010, R012 | L557-559; L39; L45 | "recommended a final dividend of Rs. 2/-per equity Share"; "COMMENCED AT 04.30 P.M. AND CONCLUDED AT 11:00 P.M." | FORWARD-SIGNAL | The revision adds no board item. There is still one agenda item (results) and a 6.5h meeting. The standalone Note 5 confirms the dividend is a parent obligation. The cash call of 4,825.62 (computed) is due by about 30-Oct-2026 under Companies Act s.127, against standalone cash of 108.56 and other bank balances of 40,165.53. Q3 cash flow tests this. The FY26 Annual Report is available for a Role 6 deep dive. |
| A3R-12 | F14 | R009, R020, R026 vs original R009, R022, R403; R033, R184, R261, R322 | L38; L75; L26; L215; structured L760-761 | "HELD ON OCTOBER 19, 2026"; "Date: 2026.10.21 15:51:24 +05'30'" vs original "NOVEMBER 03, 2025", "2026.10.19 23:11:37" | AMBIGUOUS | THE REVISION AS A GOVERNANCE DATA POINT. Two things were wrong in the 19-Oct filing. Pages 2-6 duplicated the consolidated statements in place of the standalone set (original structured L6-7). The subject line carried last year's date. The standalone statements carry a handwritten "19/10/26" (L215; R186, R262, R323), so they existed at the meeting. The fault was file assembly, not a restatement. Consolidated cells are unchanged (structured L762-767). The standalone set reached BSE at 16:56 on 21-Oct, about 41h56m after the meeting closed at 23:00 on 19-Oct (computed). The original was signed 11 minutes after close. The revised letter keeps the date "October 19, 2026" (L26). It does not say it is a revision and gives no reason (L38-64). This is the fourth filing-hygiene item in one quarter, after the template date, the name misspelling and the pincode mismatch (A3-16). Ask: whether the exchange queried the filing or the company found the error, and whether any Reg 33 delay penalty applies. |
| A3R-13 | F14 | R034, R028, R271, R326 | L160-162; L448; L522 | "12. \|Paid-up equity share capital"; "14. \|Eaming per share (EPS)"; "Interest expenses \| 1,711.35"; "Interest paid \| (1,711.35)" | NEUTRAL-FACT | Drafting items in the new pages. P&L numbering skips 13 in the standalone set too (L160-162), as in the consolidated one (L657-659). Item 13 of the standard format is usually "other equity" for the year column [INFERENCE]; it is not shown. Interest paid equals interest expense to the paisa in both periods (L448/L522; 3,919.51 FY26). That suggests a plugged cash-flow line, not a computed one. The standalone review report still misspells "Gallant Ispat Limited" (L986). Pincodes still differ (L975 "201 304" vs L1054 "201 301"). Each item is immaterial alone. Together with A3R-12 they make a governance data point. |
| A3R-14 | F15 | R195-R196, R309-R310, R305-R306, R334-R335 vs R534-R535, R645-R646, R641-R642, R670-R671; R723 | L320 vs L1189; L467 vs L1244; L465 vs L1242; L526 vs L1255; L1094 | "Suryalaxmi Technologies Private Limited  Wholly-owned subsidiary"; "(Increase)/Decrease in investment \| 15.63 \| 1,312.07" vs "\| 1,313.07" | AMBIGUOUS | The current perimeter is unchanged: one subsidiary (L1094). The S-vs-C deltas show that the perimeter changed twice in FY26 [INFERENCE]. (1) Suryalaxmi appears to have joined in FY26. The parent's 1.00 equity outflow is eliminated in FY26 (1,312.07 vs 1,313.07). FY26 subsidiary capex (89.15 = 34,815.06 - 34,725.91) equals its whole 31-Mar PPE + CWIP. Opening FY26 cash is identical (532.55). (2) The associate was gone by 31-Mar-2026. S and C non-current investments differ only by the 1.00 subsidiary stake at both dates, so C holds no equity-accounted carrying value. The associate is not Suryalaxmi. A subsidiary with about 93 of assets at 31-Mar could not produce a 169.37 share of profit [INFERENCE]. Ask: the associate's name and exit date, and the date Suryalaxmi was acquired or incorporated. |

## CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 19 new zero-standing cells read. Exceptional items and OCI-B are template lines. The four FY26-nil lines that went live in H1 sit in the parent, and the FY26 standalone comparatives were not restated (A3R-01). |
| F2 | FINDING | Full S-vs-C bridge for all six columns. The gap change is 1.94 pp, below the trigger. The audited FY26 consolidated has no associate result, which conflicts with the H1FY26 comparative +169.37 (A3R-02). |
| F3 | FINDING | Identical P&L cost lines confirm no operations. The subsidiary is an asset-buying vehicle funded 99.7% by the parent (A3R-03). There is a possible uneliminated intra-group 22.01 (A3R-04). |
| F4 | PASS | The standalone report has no other-auditor reliance. The consolidated reliance covers a 0.01 loss and 627.35 of assets (0.14%), far below 10%. Carried unchanged. |
| F5 | PASS | There is no going concern EoM. The standalone report's predecessor-auditor paragraph (L1025-1030) is identical to the original filing. A3-05 is carried open. No Q1 extract was supplied for a quarter-on-quarter diff. |
| F6 | FINDING | The standalone exchange-filing commitment was met 2 days late. The newspaper extract is not evidenced. The dividend is approved and unpaid. No project milestone is named (A3R-05). |
| F7 | PASS | Lexicon run over L1-586: no hedge hits. "will be reclassified" (L154) is the OCI caption. Note 4 "immaterial" (L553) is a segment test, not a revenue or customer hedge. |
| F8 | FINDING | S tax equals C tax in every column. The FY26 634 bps deferred credit sits in the parent. ETR is now 25.73% (A3R-06). |
| F9 | FINDING | S OCI equals C OCI. The quarterly swing exceeds FY26 in size but is immaterial (A3R-07). |
| F10 | FINDING | No dilution. Consolidated comparative EPS equals standalone EPS, so it ignores the associate share (A3R-08). |
| F11 | FINDING | S net worth ties. The 1,405.65 roll-forward break is in the parent. The 4,825.62 dividend liability is not visible (A3R-09). |
| F12 | FINDING | No segments. The parent carries 98% of capex, the cash drawdown and the third-party loan book. 603.32 of S loans are intra-group (A3R-10). The undisclosed FY26 parent PPE sale of 11,030.50 is added in Loop 1 (A3R-15). |
| F13 | FINDING | No new board item. The dividend cash call of 4,825.62 falls due by about 30-Oct-2026 (A3R-11). |
| F14 | FINDING | The revision fixes a file-assembly error 42h late with no stated reason (A3R-12). Numbering skip, plugged interest-paid line, misspelling and pincode remain (A3R-13). |
| F15 | FINDING | The current perimeter is unchanged. The S-vs-C deltas place Suryalaxmi's entry and the associate's exit both in FY26 (A3R-14). |
| F16 | N.A. | Presentation-only check. The doctype is results. |
| F17 | N.A. | Concall-only check. The doctype is results. The checklist status table below records answer status for the A4 questions and monitorables. |

## EARLIER FINDINGS: STATUS AFTER THE REVISED FILING (task item c)

| earlier id | status | line cite | basis |
|---|---|---|---|
| A3-01 associate nil FY26 vs 169.37 H1FY26 | CHANGED (narrowed, open) | L208 vs L1175; L320 vs L1189 | The audited FY26 consolidated carries no associate result and no carrying value at 31-Mar. The H1FY26 comparative is the inconsistent column. Identity and exit are still unknown (A3R-02, A3R-14). |
| A3-02 four lines live under new auditor | LEFT OPEN (located) | L344; L348; L447; L449 | Identical in S, so they are parent items. FY26 standalone comparatives are still nil (A3R-01). |
| A3-03 standalone statements absent | CLOSED | L190-214; L315-350; L443-471; L520-528; L533-572 | Standalone P&L, balance sheet, cash flow and notes are now filed. The real bridge replaces the proxy, and the gap stays below 5 pp. The late filing goes to A3R-12. |
| A3-04 subsidiary is a non-operating shell | CHANGED | L316-330 vs L1185-1199; L465 vs L1242 | It has no operations but is not dormant. H1 asset buying was 535.08, funded by a 603.32 parent loan (A3R-03, A3R-04). |
| A3-05 auditor change, predecessor unnamed | LEFT OPEN | L1025-1030 | The paragraph is unchanged. There is no new disclosure. |
| A3-06 commitments; standalone not on exchange | CHANGED (part closed) | L56-61; structured L1 | The standalone set was filed 21-Oct. The newspaper extract is unevidenced. There is still no project commitment (A3R-05). |
| A3-07 ETR normalised, FY26 deferred credit | LEFT OPEN (confirmed in parent) | L205-207 | S tax equals C tax (A3R-06). |
| A3-08 OCI swing | LEFT OPEN | L209-211 | S equals C (A3R-07). |
| A3-09 comparative EPS on pre-associate PAT | CHANGED (mechanism found) | L214 vs L1183 | C EPS equals S EPS in all columns. Not corrected (A3R-08). |
| A3-10 other-equity roll-forward break 1,405.65; dividend liability | LEFT OPEN (located) | L336; L346 | The same 1,405.65 break appears in S. The dividend is still not visible (A3R-09). |
| A3-11 CWIP +71% with no project | LEFT OPEN | L317; L465 | The parent holds 24,909.60 of the 24,931.62 rise (A3R-10). |
| A3-12 loan book built from nil | CHANGED (refined) | L329 vs L1198; L468 | 603.32 of S loans is intra-group. The third-party book of 26,578.46 has undisclosed counterparties (A3R-10). The same-year PPE sale is in A3R-15. |
| A3-13 cash drawdown, CFO 49% of PAT | LEFT OPEN | L327; L464 | S cash 108.56, S CFO 9,081.33 (A3R-10). |
| A3-14 traded-goods surge, single segment | LEFT OPEN | L195; L550-555 | S equals C. Note 4 is unchanged. |
| A3-15 AGM, dividend due, AR available | LEFT OPEN | L557-559; L523 | Nil paid at 30-Sep. Payment is due by about 30-Oct (A3R-11). |
| A3-16 filing hygiene | CHANGED | L38 (fixed); L986; L975 vs L1054; L160-162 | The subject-line date is corrected. Misspelling, pincode and numbering skip remain. The revision adds a new item (A3R-12, A3R-13). |
| A3-17 associate absent from perimeter | CHANGED (narrowed) | L320 vs L1189; L467 vs L1244 | The associate was gone by 31-Mar-2026, and Suryalaxmi joined in FY26 [INFERENCE] (A3R-14). |

Tally: CLOSED 1 (A3-03). CHANGED 7 (A3-01, A3-04, A3-06, A3-09, A3-12, A3-16, A3-17). LEFT OPEN 9 (A3-02, A3-05, A3-07, A3-08, A3-10, A3-11, A3-13, A3-14, A3-15).

## CHECKLIST STATUS: STEP 8.5 QUESTIONS AND MONITORABLES (review L424-489)

| item | status | basis (line) |
|---|---|---|
| Q1 related-party share of loans | partly | 603.32 lent to the wholly-owned subsidiary (L329 vs L1198). Third-party counterparties for 26,578.46 are undisclosed. |
| Q2 related-party other current financial assets | partly | 22.01 intra-group (L330 vs L1199). The rest of 32,609.37 is undisclosed. |
| Q3 traded-goods revenue and margin | open | S purchases equal C (L195). |
| Q4 own-manufactured volumes | open | No volume data. |
| Q5 CWIP project and date | open | Located in the parent (L317). Not named. |
| Q6 lien on other bank balances | open | L328 unchanged. |
| Q7 predecessor auditor | open | L1025-1030 unchanged. |
| Q8 other-equity 1,405.65 gap | partly | Located in the parent (L336). Not explained. |
| Q9 dividend payment date and funding | open | Nil paid at 30-Sep (L523). |
| Q10 associate identity and exit | partly | No associate in audited FY26 C and none at 31-Mar (L1175, L320 vs L1189). Name open. |
| Q11 standalone filed on BSE/NSE | answered | Filed 21-Oct-2026 16:56 in this revision (structured L1; L75), 2 days after the meeting. |
| Q12 FY27 ETR | open | S equals C (L205-207). |
| Q13 four lines a reclassification | open | Parent items. FY26 S comparatives nil (L344, L348). |
| Q14 Q2 D&A rise | open | S D&A equals C (L199). Not a subsidiary item. |
| Q15 Suryalaxmi assets and plan | partly | PPE 180.46, CWIP 24.38, advance 419.37, cash 3.02, funded by a 603.32 parent loan (bridge). Purpose open. |
| Q16 top-10 customer share | open | Not in filing. |
| Q17 AGM approval of Singhi | open | Not in filing. |
| M1 standalone visible on BSE/NSE | answered | Filed 21-Oct (late). |
| M2 Reg 47 newspaper extract | open | Not evidenced. |
| M3 Q2 shareholding / pledge | open | Not in filing. |
| M4 earnings call | open | Not in filing. |
| M5 FY26 dividend paid | open | Due about 30-Oct. Nil at 30-Sep (L523). |
| M6 AGM outcome, auditor term | open | Not in filing. |
| M7 FY26 Annual Report deep dive | open | Not in filing. |
| M8 Q3 FY27 results | open | Due by 14-Feb-2027. |
| M9 CWIP commissioning | open | NOT FOUND. |
| M10 FY27 audited results | open | Due by 30-May-2027. |
| M11 Q1 FY28 results | open | Due by 14-Aug-2027. |
| M12 FY27 AR and AGM | open | Due by 30-Sep-2027. |
| M13 filing hygiene | partly | Date fixed (L38). A re-filing was needed, and the misspelling and pincode remain (A3R-12, A3R-13). |

Totals: answered 2, partly 7, open 21.

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Publish the results extract in Business Standard (English) and a Hindi daily (Reg 47) | about 21-Oct-2026 | Cover letter L56-58 | initiated (not evidenced) |
| Full standalone and consolidated results on BSE/NSE websites | 19-Oct-2026 | Cover letter L58-61 | completed (late: 21-Oct-2026 16:56, standalone set) |
| Pay the FY26 final dividend of Rs 2/share (4,825.62 lakhs computed) | by about 30-Oct-2026 (s.127) | Note 5 L557-559; CF L523 | underway (approved 30-Sep, unpaid at 30-Sep) |
| Capital project in parent CWIP (59,812.56) | NOT FOUND | BS L317; CF L465 | underway (spend evidenced, no milestone) |
| Subsidiary asset build (Suryalaxmi, 627.35 assets) | NOT FOUND | L1114; bridge L316-330 vs L1185-1199 | underway (spend evidenced, purpose not stated) |

## FLAGS FOR A4 (management questions)
FORWARD-SIGNAL: A3R-06, A3R-10, A3R-11. AMBIGUOUS: A3R-01, A3R-02, A3R-03, A3R-04, A3R-05, A3R-08, A3R-09, A3R-12, A3R-14, A3R-15. New questions beyond the existing Q1-Q17: whether the H1FY26 associate comparative or the audited FY26 consolidated is right (A3R-02); the nature of the 22.01 intra-group item and whether intra-group interest is eliminated (A3R-04); dividend waiver and liability at 30-Sep (A3R-09); whether the revision was exchange-prompted and whether any Reg 33 delay penalty applies (A3R-12); when Suryalaxmi joined the group (A3R-14); the FY26 PPE sale (A3R-15).
Amendment 17 note: Gallantt is a commodity converter. The parent figures above (S cash, S CFO/PAT, S loans, working-capital rupee moves) are spot readings. They are flagged for monitoring and must not feed Section 1B or FTTCP.

## Loop 1 addition (A5 M3)

A5 loop 1 (M3, HIGH) found that no forensic finding covers the FY26 sale of property, plant and equipment. This section adds it. Search scope for the presentation and call: `extracted/gallantt-presentation-q2fy27-structured.md` and `extracted/gallantt-concall-q2fy27-structured.md`. I searched for: sale of, disposal, divest, monetise, sold, proceeds, property, plant and equipment, PPE, land, real estate, non-core, 110.3, 11,030.

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3R-15 | F12 | S: R275-R276, R307-R308, R309-R314, R324-R325; C: R611-R612, R643-R650; original: R317-R318, R349-R350 | RR L450, L466 (S); RR L1227, L1243 (C); R:L1126, R:L1142 (original C) | "Proceed from sale of property, plant & equipment \| - \| 11,030.50"; "Loss on sale of property, plant & equipments \| - \| 24.36" | AMBIGUOUS | See the four parts below. Lean bear: a large block sold at book value in the same year that a loan book of the same size was built has to be explained before any thesis work. |

**1. What the filings show (both sets).**
- Standalone FY26 proceeds: 11,030.50 (L466). Consolidated: 11,030.49 (L1243; original R:L1142). The 0.01 gap is rounding, so the parent made the sale, not the subsidiary.
- Loss on sale: 24.36 in both sets (L450, L1227; original R:L1126). That is 0.22% of proceeds (computed). Implied carrying value is about 11,054.86 (computed, proceeds plus loss), so the asset was sold at book.
- There is no exceptional item in FY26 in either set (L203, L1170). The loss sits in ordinary expense lines.
- H1FY27 proceeds are nil (L466, L1243). The sale does not repeat, so H1 capex of 27,311.52 (S, L465) has no disposal offset.
- Size (computed, standalone): 6.2% of 31-Mar-2026 PPE (1,77,243.99, L316), 31.8% of FY26 capex (34,725.91, L465) and 18.3% of FY26 CFO (60,226.56, L464).

**2. Same-year cash flow context (FY26).**
- Loans and advances: outflow 29,742.32 S (L468) / 29,649.96 C (L1245; original R:L1144), built from nil. The 31-Mar balance equals the outflow (L329, L1198).
- Investments: decrease (inflow) 1,312.07 S (L467) / 1,313.07 C (L1244; original R:L1143). That is about Rs 13.1 Cr exited. The 1.00 gap is the subsidiary stake (A3R-14).
- Bank deposits over 3 months: outflow 14,868.42 (L469). Proceeds from borrowings: 17,002.18 (L521).
- The audited FY26 consolidated carries no associate result and no associate carrying value at 31-Mar-2026 (A3R-02, A3R-14).
- PPE sale proceeds 11,030.50 plus new borrowing 17,002.18 = 28,032.68. That is 94.3% of the 29,742.32 loan book built in the same year (computed). This is a size match only. The filing does not trace any use of funds [INFERENCE].

**3. What is not disclosed.** The filings do not name the asset sold (plant, land or real-estate holding; Note 4 names "real estate operations", L553). They do not name the buyer or state its related-party status. They do not give the sale date or say whether a Reg 30 disclosure was made. They do not state the use of proceeds, or whether the sale is linked to the associate exit or the investment exit. They do not say whether any capacity or captive power left with the asset.

**4. Presentation and call.** Neither one mentions the sale.
- Presentation: no hit. The deck lists "300 Cr | land bank" (presentation structured R091, page 11, line 236) with no disposal or monetisation line. It notes the Q2 FY26 associate share of 1.69 Cr (R455, R755, page 22, line 492) but gives no name and no exit.
- Concall: no hit on sale, disposal, proceeds or PPE. The only related text is "greenfield depends on land acquisition and state government incentives" (concall structured R176, line 103, [00:05:57]).
- Silence count: 1 quarter. This is the first filing set in this run that shows the FY26 comparative.

**Questions for A4.**
- What asset was sold in FY26 for 11,030.50, to whom, and on what date?
- Is the buyer a related party, and was the price set by an independent valuation?
- Was the full consideration received in cash? The cash flow shows it as received.
- Did the proceeds fund the FY26 loan book, and do any of the borrowers link to the buyer?
- Did the sale take any capacity or power out of the FY27 base?

Checklist effect: F12 stays FINDING. This adds one AMBIGUOUS finding. Related open items: A3-12 / Q1 (loan counterparties) and A3-17 / Q10 (associate exit). Amendment 17: FY26 cash flow carries this one-off 11,030.50 investing inflow. It must not be read as a recurring funding source.

```yaml
stage: A3-forensics
company: "GALLANTT"
quarter: "q2fy27"
doctype: "resultsrev"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/gallantt-q2fy27/work/forensics_resultsrev_gallantt_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
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
  - {id: "A3R-01", check: "F1", line: "L344; L348; L447; L449", classification: "AMBIGUOUS", implication: "Four FY26-nil lines live in H1 sit in the parent; FY26 standalone comparatives not restated; reclass vs FY26 understatement (carries A3-02)"}
  - {id: "A3R-02", check: "F2", line: "L208; L1175-1177; L192; L1159", classification: "AMBIGUOUS", implication: "S-vs-C gap 1.94% to 0.00% (<5pp); audited FY26 C has no associate result, conflicting with H1FY26 comparative +169.37"}
  - {id: "A3R-03", check: "F3", line: "L316-330 vs L1185-1199; L465 vs L1242; L1114", classification: "AMBIGUOUS", implication: "Suryalaxmi not dormant: H1 asset buy 535.08 (PPE, CWIP, 419.37 advance) funded by parent loan 92.36 to 603.32; nil revenue; likely land [INFERENCE]"}
  - {id: "A3R-04", check: "F3", line: "L330 vs L1199; L470 vs L1247; L446 vs L1223", classification: "AMBIGUOUS", implication: "22.01 intra-group receivable eliminated but C interest received +22.01 and interest income unchanged; possible uneliminated capitalised intra-group interest [INFERENCE], 0.09% of H1 PBT"}
  - {id: "A3R-05", check: "F6", line: "L56-61; L557-559; L523", classification: "AMBIGUOUS", implication: "Standalone exchange filing met 2 days late; newspaper extract unevidenced; dividend unpaid at 30-Sep; no project milestone despite parent CWIP +71.4%"}
  - {id: "A3R-06", check: "F8", line: "L205-207; L340; L331", classification: "FORWARD-SIGNAL", implication: "S tax = C tax; FY26 634 bps deferred credit sits in parent; H1 ETR 25.73% (Q2 27.25%); do not carry FY26 ETR forward"}
  - {id: "A3R-07", check: "F9", line: "L209-211", classification: "NEUTRAL-FACT", implication: "S OCI = C OCI; quarterly swing exceeds FY26 full year in size; immaterial; verify assumptions at AR"}
  - {id: "A3R-08", check: "F10", line: "L213-214; L1183; L1177", classification: "AMBIGUOUS", implication: "No dilution; C EPS equals S EPS in every column so C comparative EPS ignores associate (3.62 vs 3.69; 10.82 vs 10.89); not corrected in revision"}
  - {id: "A3R-09", check: "F11", line: "L335-337; L346; L557; L523", classification: "AMBIGUOUS", implication: "Parent other-equity roll-forward break 1,405.65 (Rs 0.58/share) identical to C; 4,825.62 dividend liability not visible; FY26 outflow 940.46 = Rs 0.39/share; waiver candidate [INFERENCE]"}
  - {id: "A3R-10", check: "F12", line: "L317; L324; L327; L329; L464; L465; L468", classification: "FORWARD-SIGNAL", implication: "Parent carries 98.1% of capex, 99.9% of CWIP rise, inventory +21.4%, cash 108.56, CFO/PAT 49.3%; S loans include 603.32 intra-group; third-party book 26,578.46"}
  - {id: "A3R-11", check: "F13", line: "L557-559; L39; L45", classification: "FORWARD-SIGNAL", implication: "No new board item; parent dividend cash call 4,825.62 due ~30-Oct-2026 vs cash 108.56; test in Q3 cash flow"}
  - {id: "A3R-12", check: "F14", line: "L38; L75; L26; L215; structured L760-761", classification: "AMBIGUOUS", implication: "Revision fixed file assembly (pp2-6 duplicated consolidated) and last year's subject date; standalone reached BSE ~41h56m after meeting close; letter states no revision or reason; fourth hygiene item this quarter"}
  - {id: "A3R-13", check: "F14", line: "L160-162; L448; L522; L986; L975; L1054", classification: "NEUTRAL-FACT", implication: "Item 13 skipped in standalone P&L too; interest paid equals interest expense to the paisa (plug); misspelling and pincode mismatch remain"}
  - {id: "A3R-14", check: "F15", line: "L320 vs L1189; L467 vs L1244; L465 vs L1242; L526 vs L1255; L1094", classification: "AMBIGUOUS", implication: "Perimeter unchanged now; S-vs-C deltas place Suryalaxmi entry and associate exit both in FY26 [INFERENCE]; associate is not Suryalaxmi"}
  - {id: "A3R-15", check: "F12", line: "RR L450, L466 (S); RR L1227, L1243 (C); R:L1126, R:L1142; context L467-469, L521, L1244-1246, R:L1143-1144", classification: "AMBIGUOUS", implication: "Loop 1 (A5 M3). Parent sold PPE in FY26 for 11,030.50 at a 24.36 loss (0.22%, at book; 6.2% of PPE). Same year: loan book built from nil to 29,742.32, investments exited 1,312.07, associate gone. Proceeds plus borrowings = 94.3% of the loan book [INFERENCE, size only]. Asset, buyer, related-party status, date and use of proceeds not disclosed. No mention in deck or call. No H1 repeat."}
forward_signals: ["A3R-06", "A3R-10", "A3R-11"]
ambiguous: ["A3R-01", "A3R-02", "A3R-03", "A3R-04", "A3R-05", "A3R-08", "A3R-09", "A3R-12", "A3R-14", "A3R-15"]
commitments:
  - {commitment: "Publish results extract in Business Standard and Hindi daily (Reg 47)", implied_date: "~2026-10-21", ref: "Cover letter L56-58", status_word: "initiated"}
  - {commitment: "Full standalone and consolidated results on BSE/NSE websites", implied_date: "2026-10-19 (met 2026-10-21 16:56)", ref: "Cover letter L58-61", status_word: "completed"}
  - {commitment: "Pay FY26 final dividend Rs 2/share (4,825.62 lakhs computed)", implied_date: "~2026-10-30 (s.127)", ref: "Note 5 L557-559; CF L523", status_word: "underway"}
  - {commitment: "Capital project in parent CWIP 59,812.56", implied_date: "NOT FOUND", ref: "BS L317; CF L465", status_word: "underway"}
  - {commitment: "Subsidiary asset build (Suryalaxmi, 627.35 assets)", implied_date: "NOT FOUND", ref: "L1114; L316-330 vs L1185-1199", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The revision adds the standalone set and leaves every consolidated cell unchanged. It fixes a file-assembly error: original pp2-6 duplicated the consolidated pages. It also fixes last year's subject-line date. The standalone set reached BSE about 42h after the meeting, and the letter gives no reason. It is clerical, not a restatement, but it is the fourth hygiene item this quarter. The S-vs-C gap is near zero. First, Suryalaxmi is not dormant. It bought 535 lakhs of assets in H1 on a 603 lakh parent loan. It appears to have joined the group in FY26 [INFERENCE]. Second, the audited FY26 consolidated carries no associate result and no associate carrying value, so the 169.37 in the H1FY26 comparative does not reconcile. Consolidated EPS equals standalone EPS in every column. A 22.01 intra-group item may be capitalised interest that consolidation did not eliminate [INFERENCE]. The other-equity break and the missing dividend liability sit in the parent. Loop 1 adds A3R-15: an undisclosed FY26 parent PPE sale of 11,030.50 at book. Closed: A3-03. Changed: seven. Open: nine. A4 must not quote A1's stale R697 context or fulltext L1258."
```
