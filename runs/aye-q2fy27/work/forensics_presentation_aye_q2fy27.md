# FORENSICS AYE Q2 FY27 (doctype: presentation) - A3

Source index: runs/aye-q2fy27/extracted/aye-presentation-q2fy27-structured.md (R001-R913)
Fulltext: runs/aye-q2fy27/extracted/aye-presentation-q2fy27-fulltext.md (line numbers below = this file)
Ledger: runs/aye-q2fy27/work/ledger_presentation_aye_q2fy27.md
Prior quarter: runs/aye-q2fy27/work/prior_q1fy27_presentation_fulltext.md (Q1 FY27 deck, 22-Jul-2026; cited "prior L###" = the embedded 5-digit line number)
Cross-reference: runs/aye-q2fy27/work/forensics_results_aye_q2fy27.md (cited "results A3-##")
Monitoring checklist: runs/aye-q2fy27/work/monitoring_checklist_AYE.md
Model: claude-opus-5-5. Source PDF and inputs/ not opened.

Lender variants applied (NBFC-ML, line 258):
- F12 runs on asset quality, provisioning, collection efficiency (CE), income quality and liquidity. The deck has no segment table.
- F13 runs on the board and KMP rosters (slides 18-19) and the cover letter signer.
- F15 runs on the deck's entity rosters (more-than-5% holders, backers, board, management). A deck has no consolidation list.
- F17 runs as a deck silence audit against the Notion checklist, because the orchestrator passed the checklist for it.

## 1. LEDGER RECONCILIATION

| Item | Count | Result |
|---|---|---|
| Structured IDs in ledger (R001-R913) | 913 | 913 read at cited fulltext line (100%) |
| SCRAMBLED_ATTRIBUTION rows (69 NUMBER + 12 QUALIFIER) | 81 | read; no row-to-label mapping inferred for any of them |
| ZERO_STANDING rows (R188-R190, R627, R831) | 5 | read at lines 297, 818, 924 |
| Orphan IDs | 0 | none |

Method notes:
- Where a chart is time-shifted between decks (cost of borrowing, debt raised, CRAR, more-than-5% holders), I compare the SET of printed values with the Q1 deck. I do not assign a value to a label inside a scrambled block.
- Provision coverage uses only the unflagged rows (R513-R529, R537-R541, R548, R552-R556, R558-R559). It also uses the Q1 deck's 30-Jun gross loans (prior L564).

Pipeline errors for the orchestrator (A1/A2, not document findings):
1. R076 / R077 period labels are swapped. R076 "1,219" is Q1FY27, not Q2FY26. R077 "1,275" is Q2FY26, not Q1FY27. Proof: H1FY27 2,622 (line 206) = 1,219 + 1,403. H1FY26 2,276 (line 208) - 1,275 = 1,001 = Q1FY26 (prior L132). Commentary line 120: "increased 15% quarter-on-quarter to Rs. 1,403" (1,403 / 1,219 = +15.1%). Q1 deck: "Disbursements for the quarter stood at Rs. 1,219 Crore" (prior L099). The slide's "+10%" (line 150) is therefore YoY (1,403 / 1,275). Downstream stages must not use the R076/R077 labels.
2. A1 left four printed numbers out of the structured file. Line 667 has "83  308  6,865": in the Q1 deck these are the 30-Jun Stage 2, Stage 3 and total gross loans (prior L564). Line 807 has "0", the 10+ year vintage potential capacity. The A2 ledger says "MISSING_FROM_STRUCTURED: none". The A2 count test compares the structured file with itself, so it cannot catch a gap against the fulltext.
3. Several A1 line cites are off by one to three lines (example: R072 "6,028" is on line 153, not 150; R076 "1,219" is on line 151). Every value was found within three lines of its cite.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F1 | R627, R628, R188-R190, R204, R596-R607, R629, R631, R661, R667 | 818, 297, 299, 796-806, 855; prior L712 | line 818: "Company has not opened new branches in H1FY27"; line 806: "*assumption is avg. AUM grows to 21 Cr." | AMBIGUOUS | Branches have stayed at 571 since FY2026 (line 299). States added were 0 in FY24, FY25 and FY26 (line 297). Q1 also had no openings (prior L712). The slide sizes existing-branch headroom at "4,000+" crore. Its own arithmetic is 177 x 13 + 221 x 7 + 140 x 4 + 33 x 0 = 4,408 at a 21 cr ceiling. The 3-year vision targets a 28-33% AUM CAGR (line 855). From 7,597 that needs about +8,300 to +10,300 cr (7,597 x 1.28^3 = 15,932; x 1.33^3 = 17,873). The headroom covers less than half. Reading 1: the ceiling rises, because the 10+ year cohort still grows at "~13%" (line 804), so the current network carries the target. Reading 2: the target needs new branches, which adds branch opex against the 7.0-7.5% opex target (line 860). Separating observation: H2 FY27 branch openings and the 10+ cohort's average AUM. |
| A3P-02 | F6 | R663, R380, R282-R284, R567, R575, R580-R582, R577-R579, R588 | 865, 555, 414-420, 721, 743-751; prior L336-341, L477, L619 | line 865: "Increasing mortgage loan shares and deepening AI/ML integration"; line 555: "Well positioned to increase the average tenor of assets" | AMBIGUOUS | Both promises repeat verbatim from Q1 (prior L477, L755). Delivery this quarter: mortgage share (LAP + Saral) is 23.2% at Sep-26 (21.8% + 1.4%) against 23.3% at Jun-26 (21.8% + 1.5%). Underwriting "with AI/ML scores" stays at 32% (line 721; prior L619). The primary ML channel stays at 180 branches for three quarters (line 751). No tenor metric is disclosed. ML disbursement for Q1FY27 is 125 in both decks. The Q2FY27 value is 137 or 212, and R588 marks the period mapping as not determinable, so no growth rate is stated. Ask: what mortgage share does the plan assume for FY27, and what is the ML disbursement for Q2FY27? |
| A3P-03 | F6 | R583, R584, R586 | 757-758; prior L654 | "Upsell team – 154 staff deployed in 133 branches" | NEUTRAL-FACT | Q1: 126 staff in 100 branches (prior L654). The team grew by 28 staff and 33 branches. Mortgage share did not rise (A3P-02), and the deck gives no outcome metric for the team. |
| A3P-04 | F7 | R023, R027, R028, R435, R266 | 114-115, 121-122, 633, 640; prior L093 | "disbursements moderated in drought-affected regions of Maharashtra, Karnataka and Madhya Pradesh" | AMBIGUOUS | This risk framing is new. In Q1 the commentary said only that "the broader macro environment remains uncertain" (prior L093). The key-states slide breaks out Bihar, UP, Rajasthan and Rest States (line 633), so the three named states are inside "Rest States". Rest States Bucket 1 CE went from 57.5% (Jun) to 55.7% (Sep) (line 640). R266 marks the map's state shares as not determinable, so the AUM exposure to these states is NOT FOUND. The new wording gives advance cover for H2 asset quality in these states. Ask for the AUM share, Bucket 1 CE and PAR of MH, KA and MP. |
| A3P-05 | F12 | R513-R528, R537-R539, R559, R560, R709 | 662-665, 670, 679, 881; prior L564-567, L580 | line 679: "PCR as of 30th Sept 2026 is 62.42%"; line 670: "58.07%   63.84%    4.17%" | AMBIGUOUS | On the deck's own 30-Jun basis, total ECL cover fell from 4.17% to 3.85%. Stage 2 cover fell from 58.07% to 47.44% (-1,063 bps), and Stage 3 cover from 63.84% to 62.42%. Implied 30-Jun ECL is 4.17% x 6,865 = 286. At 30-Sep it is 274 (line 663), down about 12 cr while gross loans rose 3.7% (6,865 to 7,119). Keeping June cover on the September book needs 297, which is 23 cr pre-tax and about 17 cr post-tax at 25.17%. That is about 20% of Q2 PAT of 87. Stage 3 gross fell 308 to 299. Q2 credit cost was 82 (line 881) while the ECL stock fell about 12, which implies about 94 cr of write-offs and other charges. Write-offs are NOT FOUND in the deck (results A3-11: H1 write-offs 155.56). Reading 1: the stage mix improved (PAR 30 6.07% to 5.89%, line 569). Reading 2: the GNPA fall is write-off-led, and a coverage release lifts PAT. Gross slippage separates the two readings, and the deck does not disclose it. |
| A3P-06 | F12 | R393-R395, R404-R405, R412-R417, R461-R484, R908 | 577, 640, 995; prior L497, L546, L503-505 | line 640 (UP): "52.1% 50.9% 51.7% 52.6% 48.4% 47.6%" | FORWARD-SIGNAL | Bucket 1 CE fell from 54.5% to 52.8% QoQ (line 577). It is still above 48.4% in Q2FY26, and management calls the September quarter "seasonally weaker" (lines 116-117). By state: UP printed 47.6% in Sep-26, the lowest of the nine months in the two decks (Jan-Mar 58.4/58.8/59.2, prior L546). UP's Q2 average was 49.5% against a Q1 average of 51.6%. Rajasthan's Q2 average was 55.6% against 59.9% in Q1 and 61.9-69.7% in Jan-Mar. Bihar sits near 38%. Bucket 1 means cases under 30 DPD (line 995), so a lower CE feeds PAR 30 and Stage 3 in Q3. In Q1 the deck framed its CE fall as seasonal (prior L503-505). The Q2 deck offers no framing, and UP is not one of the named drought states. This is the leading indicator for the GNPA thesis-broken trigger. |
| A3P-07 | F12 | R678-R685, R719, R721, R056, R823, R824 | 876, 883, 135, 923 | line 876: "Fee & Other Income  48  56 ... 37"; line 135: "marking our highest ever quarterly profit" | FORWARD-SIGNAL | Fee and other income rose by 11 (37 to 48) QoQ. That roughly equals the 10.12 DA gain, which was nil in Q1 (results A3-13). Ex-DA, the line is flat at about 38. YoY it fell 14% (56 to 48), and H1 fell 13% (98 to 85). On ATA it went from 3.20% to 2.23% (line 923). PAT rose 12 QoQ, and the post-tax DA gain of about 7.6 is about 62% of that rise. The ECL release in A3P-05 adds to it. The deck does not mention DA. The "highest ever quarterly profit" holds in Q3 only if DA recurs and cover does not need rebuilding. |
| A3P-08 | F12 | R334-R343, R345-R349, R359, R329-R333, R780-R801, R810, R694-R696 | 503-516, 531, 917-921, 878, 135; prior L423-436, L451 | line 503: "Diversified Lender Base with Reducing Cost of Borrowing"; line 919: "6.74%   7.69% ... 6.46%    28 bps" (finance cost on ATA, Q2FY27 6.74%, Q1FY27 6.46%, +28 bps QoQ) | AMBIGUOUS | The two new CoB values for Q2FY27 (10.63%, 10.04%) are both below the Q1FY27 pair (10.78%, 10.20%). This is a set comparison with prior L427-431; R359 says CoB and incremental CoB cannot be told apart. Yet finance cost on ATA rose 28 bps QoQ. Finance cost rose from 131 to 145 (+10.7%) while AUM grew 3.7%. Debt raised in Q2 was 1,199.4, the new value against prior L434-436. NIM on ATA fell from 15.94% to 15.59% (-35 bps), and the commentary says only that NIM "stood at 15.6%" (line 135). The retail borrowing share inside FIs rose from 12.2% to 14.2% (line 531; prior L451). Same tension as results A3-14. Reading 1: pre-funding for H2. Reading 2: negative carry. Q3 AUM growth against borrowing growth separates them. |
| A3P-09 | F13 | R306-R316, R320, R321, R325, R328, R007, R911, R297-R303 | 459, 470-494, 50, 61, 1006, 432-445; prior L033, L045, L378, L389-391 | line 472: "Nishit Shrivastava"; line 484: "Anuj Jain" (Chief Compliance Officer); line 61: "Company Secretary & Compliance Officer" | AMBIGUOUS | CTO changed from Jinu Joseph (prior L391) to Nishit Shrivastava. A Chief Compliance Officer box (Anuj Jain) is new. "Year 1" tenures rose from one (prior L389) to three (lines 470, 481, 494). R328 marks tenure-to-name attribution as not determinable. The cover letter signer moved from the CFO (prior L033, L045) to the CS (lines 50, 61). The deck still names Gaurav Seth as CFO (lines 459, 1006), which answers part of results A3-16. The MD title changed from "MD & Co-Founder" (prior L378) to "Founder, MD & CEO" (line 459). The 7 board members are unchanged. KMP churn (checklist AMBER) now covers the CFO and CTO seats. |
| A3P-10 | F14 | R575, R576, R172, R259, R596-R599 | 745-746, 261, 347, 798-801; prior L642-643 | line 746: "Branch BAU (Centralised underwriting) – 444 branches" | AMBIGUOUS | 180 + 444 = 624. The deck states 571 branches (lines 261, 347), and the vintage table sums to 177 + 221 + 140 + 33 = 571. Q1: 180 + 391 = 571 (prior L642-643). No branches were opened. Either 444 is an error or the channel definitions now overlap. Ask which. |
| A3P-11 | F14 | R670-R693, R736, R809, R147 | 874-877, 920, 248; prior L763-766 | line 875: "Interest Income  479  371  24%  453  8%" | NEUTRAL-FACT | The growth columns sit on the first three rows, but they compute to Total Income (24%, 8%, 23%), PPoP (54%, 11%, 47%) and PAT (151%, 16%, 148%). In this text layer, interest income YoY (+29.1%, 479/371) and the fee and other income fall (-14% YoY) are not printed. The Q1 deck shows the same pattern (prior L764-766), and this may be text-layer compression (R736). Other drafting defects: "-053 bps" (line 920), and the "#As of 30th September 2026" footnote on slide 10 has no # marker (line 248, R147). |
| A3P-12 | F15 | R873, R861-R872, R876, R167 | 941-953, 276; prior L819-827 | lines 945-950: "Elevation Capital / LGT Capital Invest / CapitalG LP (erstwhile Google Capital) / British International Investment / A91 Emerging Fund / Imp2 Assets" | FORWARD-SIGNAL | Alpha Wave India held 7.8% at 30-Jun (prior L823). It is no longer in the more-than-5% list at 30-Sep, which drops from seven holders to six. The six printed percentages (12.6, 10.0, 7.7, 7.4, 7.2, 5.5) equal Q1's set minus 7.8%, with 10.1% becoming 10.0%. R876 marks holder-to-percentage mapping as not determinable. The largest category value fell from 67.0% (prior L827) to 62.1% (line 945), and its label is not determinable. A pre-IPO holder sold at least 2.8 pp of equity in Q2. Slide 12 still lists "Alpha Wave" as a backer (line 276). The IPO allotment date and lock-up are NOT FOUND in the deck. Watch for supply from the remaining PE holders (about 50% in aggregate on the printed set). |
| A3P-13 | F16 | R024, R025, R076-R079, R131-R133, R642 | 120, 150, 824; prior L099, L715 | line 120: "Disbursements increased 15% quarter-on-quarter to Rs. 1,403" | FORWARD-SIGNAL | In Q1 the commentary framed disbursements as YoY: "growth of 22% year-on-year" (prior L099). In Q2 the commentary uses QoQ (+15%). The YoY figure, +10% (1,403 against 1,275), appears only on the chart (line 150). AUM YoY slowed from 28.0% (prior L715) to 26.03% (line 824). Disbursement growth of 10% against AUM growth of 26% points to slower AUM growth ahead. See pipeline error 1 on R076/R077. |
| A3P-14 | F16 | R637-R657, R069, R128 | 822-837, 142; prior L713-728 | line 824-829: "25.0% - 30.0% ... 14.25% - 14.75% ... 8.25% - 8.75% ... 3.5% - 4.0% ... 4.0% - 4.5%" | AMBIGUOUS | The FY27 guidance repeats the Q1 deck word for word (prior L713-728). Add-gate (iii), "refined FY27 guidance", is not met. H1 against guidance: NIM 15.87% is 112 bps above the top of the band. At equal half-year weights that implies an H2 NIM of about 12.6-13.6%. Opex 8.83% is above the 8.75% top. Credit cost 3.95% is at the top of the band. RoTA 3.90% is below the 4.0% bottom. To reach the 25% AUM floor, H2 AUM must grow 15.9% (7,597 to 8,805). H2 FY26 grew 16.9% (6,028 to 7,044), and no branches are being added. Reading 1: the guidance is stale and conservative. Reading 2: management expects H2 NIM compression. Ask which, and why RoTA guidance does not move with NIM. |
| A3P-15 | F16 | R560, R537-R539, R527, R559, R561 | 665, 670, 679, 681; prior L567, L580, L582 | line 681: "**o/s staff loan are excluded" vs prior L582: "ECL provision is excluding management overlay" | AMBIGUOUS | The overlay footnote is gone, and the 30-Jun figures are restated. Stage 2 cover went from 47.11% to 58.07%, Stage 3 from 63.05% to 63.84%, and total from 4.01% to 4.17%. In the Q2 deck, Stage 3 cover equals PCR (62.42% on lines 665 and 679). In the Q1 deck they differed (63.05% against PCR 63.80%). Reading: the table now includes the overlay, which was about 11 cr at 30-Jun (286 - 275). The ex-overlay view is gone, so the add-gate (i) ex-overlay credit cost test cannot be run from the deck. Ask for the overlay at 30-Jun and 30-Sep, and whether any of it was released in Q2. |
| A3P-16 | F16 | R590-R594 | 777, 783-784; prior L673, L679-680 | line 777: "In H1FY27, per month per Tele-caller productivity was Rs. 1.56 Crores." | AMBIGUOUS | Q1 reported a Q1FY27 figure of 1.75 cr (prior L673). Q2 switches to an H1 basis. At equal headcount, Q2 is about 2 x 1.56 - 1.75 = 1.37 cr, down 22% QoQ. The foreclosure rate also moved to H1: 5.65% for Q1 and 5.74% for H1, which implies about 5.83% for Q2. Repeat share of HL AUM fell 52.6% to 52.0% to 51.4% (line 783; prior L679). The repeat engine is slowing, and the H1 basis blurs the Q2 print. ATS on disbursement rose for LAP (4.9 to 5.4 lakh) and hypothecation (1.5 to 1.6) (lines 414, 420; prior L336, L341). |
| A3P-17 | F16 | R609-R626, R629, R630, R634, R635 | 796-816; prior L691-710 | line 810: "Contribution to growth in AUM (Sep-25 to Sep-26)" | AMBIGUOUS | The window changed from Mar-25 to Jun-26 (prior L699) to Sep-25 to Sep-26. The legend lost "Others*" and the footnote "*Others include AUM under DA purchased" (prior L704, L710). Vintage buckets were redefined from Upto 2Y / 2-4Y / 4+Y to 0-3 / 4-6 / 7-9 / 10+ years. The contribution values are scrambled (R635), so we cannot tell whether purchased DA AUM now sits in another category. Ask: was any portfolio bought in H1 FY27, and where is it reported? |
| A3P-18 | F16 | R388, R805, R813, R818, R826, R840, R104, R119 | 571, 920-926, 175, 186; prior L104, L157, L168, L804-810 | line 921: "4.03%   -21 bps" | NEUTRAL-FACT | The Q2 deck restates Q1FY27 ratios. Credit cost moves from 4.01% to 4.03%, opex from 8.91% to 8.93%, PAT/ATA from 3.71% to 3.69%, RoA on AUM from 4.18% to 4.15%, RoE from 11.68% to 11.60%, and cost-to-income from 50.1% to 50.3%. The footnotes name only the Q2FY26 reclassification (lines 169, 887, 939). The amounts are immaterial, but the Q1 base moved without a note. |
| A3P-19 | F16 | R294, R284 | 426, 420; prior L347 | line 426: "Hypothecation unsecured loans are partly secured against business assets" | NEUTRAL-FACT | This clause is new (prior L347 had only "business loans and non consumption"). The deck now calls 76.8% of AUM (line 420) unsecured. This matters for loss given default on the main book, and it links to results A3-13 (DA pool with 0% tangible security). |
| A3P-20 | F17 | R516-R528, R559, R636-R657; checklist items 1-8 and add-gate | see Section 5 | gross slippage, write-offs, covenant status: no line (NOT FOUND) | CONFIRMATORY-NEGATIVE | Two decks in a row disclose no gross slippage, write-offs, unwaived covenant count, DA income, co-lending book or product-wise Stage 3. The add-gate's bear reading for item (i) applies: slippage was "not disclosed again". The deck does confirm GNPA (line 130), PCR (line 679), Bucket 1 CE (line 577), repeat share (line 783) and guidance (lines 822-829). |

## 3. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 | FINDING | 5 ZERO_STANDING rows read. A3P-01 covers no new branches and no new states against the 3-year AUM target. R831 (line 924) is a template dash on the leverage bps cell, with nothing behind it. |
| F2 | N.A. | Deck has no standalone or consolidated statements. |
| F3 | N.A. | No consolidated cost lines; no Going Concern language. |
| F4 | N.A. | No auditor report or Other Matter paragraph in a deck (see results A3 F4). |
| F5 | N.A. | No EoM or Going Concern paragraph in either deck. |
| F6 | FINDING | Lexicon hits at lines 142, 555, 758, 759, 849, 855. A3P-02 (mortgage share and tenor promises repeated with no delivery) and A3P-03 (upsell team underway). Register below. |
| F7 | FINDING | The safe harbor (lines 85-91) matches Q1 (prior L067-073). No lexicon hedge is new. A3P-04 covers the new drought framing in the commentary. |
| F8 | PASS | Deck ETR (rounded): Q2 25.0% (29/116), Q1 23.5% (23/98), H1 24.8% (53/214), Q2FY26 16.7% (7/42). Close to statutory 25.17% in FY27. Deferred tax is not shown in the deck (see results A3 F8). |
| F9 | N.A. | No OCI in the deck. |
| F10 | PASS | Basic vs diluted EPS spread: Q2 0.85% (3.51/3.48), Q1 0.66% (3.02/3.00), H1 0.61% (6.53/6.49), against Q2FY26 1.67% and H1FY26 1.76%. The QoQ change is inside the 0.01 rounding. The denominator question sits in results A3-10. |
| F11 | PASS | Total equity of 2,695 (lines 184, 266, 548, 905) ties to the filing's 49.02 + 2,645.59 = 2,694.61 (results A3 F11). BVPS of Rs 110 x 24.51 cr shares = 2,696. Total assets 8,774 = total liabilities 8,774 (lines 898, 906). RoE 13.09% = PAT/ATA 4.04% x leverage 3.24 (lines 929-935). Deck D/E is 2.17x (line 937) against the filing's Reg 52(4) 2.25x. The gap is the definition: total equity 2,695 against Reg 52(4) net worth 2,621.80, a 2.7% difference, below 5%. Latest CRAR is 41.0% against 42.4% at Jun-26 (set comparison, line 537; prior L456). |
| F12 | FINDING | Lender variant: A3P-05 (ECL cover thinning), A3P-06 (Bucket 1 CE in UP and Rajasthan), A3P-07 (DA gain and fee income behind the record PAT), A3P-08 (CoB down, finance cost on ATA up). |
| F13 | FINDING | Board unchanged. A3P-09 covers the CTO change, the new CCO, three Year-1 tenures, and the signer moving from CFO to CS. The deck carries no AR, AGM or fund-raise item. |
| F14 | FINDING | A3P-10 (BAU 444 + primary 180 is not 571), A3P-11 (P&L growth columns offset, "-053 bps", orphan footnote). |
| F15 | FINDING | Entity rosters: A3P-12 (Alpha Wave India leaves the more-than-5% list). Backers, board, technology vendors and CSR partners are unchanged. The management roster change is logged under F13. |
| F16 | FINDING | A3P-13 (disbursement framing moves to QoQ), A3P-14 (guidance repeated, not refined), A3P-15 (overlay footnote dropped, 30-Jun restated), A3P-16 (period basis switched to H1), A3P-17 (DA-purchased category dropped, window and buckets redefined), A3P-18 (Q1 ratios restated), A3P-19 (unsecured clause added). No slide was dropped; the deck added slides 9, 10 and 25 (H1 views). |
| F17 | FINDING | Deck silence audit against the checklist (Section 5). A3P-20. |

## 4. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|
| FY27 AUM growth 25.0-30.0% YoY | 31-Mar-2027 | line 824 (R637); prior L715 | underway (H1 26.03%; unchanged guide) |
| FY27 NIM 14.25-14.75% | 31-Mar-2027 | line 825 (R638) | underway (H1 15.87%, above band) |
| FY27 opex 8.25-8.75% | 31-Mar-2027 | line 827 (R639) | underway (H1 8.83%, above band) |
| FY27 credit cost 3.5-4.0% | 31-Mar-2027 | line 828 (R640); line 131 (R045) | underway (H1 3.95%, top of band) |
| FY27 return on total assets 4.0-4.5% | 31-Mar-2027 | line 829 (R641) | underway (H1 3.90%, below band) |
| "delivering on our FY27 guidance" | 31-Mar-2027 | line 142 (R069) | underway |
| H2 focus: build on progress, sustain productivity and asset quality | H2 FY27 | line 141 (R068) | initiated |
| 3-year normalized credit cost 3.25-3.75% | about FY30 ("next three years") | line 845 (R659); prior L733-735 | initiated (repeated) |
| 3-year RoA 4.0-4.5%, RoE 17.0-20% | about FY30 | lines 849-851 (R660) | initiated (repeated; H1 RoE 12.34%) |
| 3-year AUM CAGR 28-33% | about FY30 | line 855 (R661) | initiated (repeated; see A3P-01) |
| 3-year opex 7.0-7.5% via branch maturation and automation | about FY30 | line 860 (R662) | initiated (repeated) |
| Increase mortgage loan share; deepen AI/ML in underwriting | not dated | line 865 (R663) | initiated (share 23.3% to 23.2%; AI/ML 32% flat) |
| Increase the average tenor of assets | not dated | line 555 (R380); prior L477 | initiated (repeated; no metric) |
| Upsell ML loans to HL repeat customers (154 staff, 133 branches) | not dated | lines 757-758 (R586); prior L654 | underway (from 126 / 100) |
| OER falls as ML AUM per branch grows | not dated | line 759 (R585) | initiated |
| Existing branches add Rs 4,000+ cr AUM | "medium term" | lines 799-801 (R631) | initiated (new this deck) |
| HUL CSR donation INR 50 lakh for 1-Oct-2026 to 31-Mar-2027 | 31-Mar-2027 | line 977 (R885, R887) | completed (received) |

## 5. F17 DECK SILENCE AUDIT ("What Was NOT Discussed")

Decks available: Q1 FY27 (22-Jul-2026) and Q2 FY27 (21-Oct-2026). Counts cover these two decks only.

| Checklist / open item | In Q2 deck? | Line | Consecutive decks silent |
|---|---|---|---|
| Add-gate (i) gross slippage | NOT FOUND | none | 2 |
| Add-gate (i) ex-overlay credit cost | NOT FOUND; overlay footnote dropped (A3P-15) | 681 | 1 (Q1 deck showed ECL ex-overlay) |
| Write-offs | NOT FOUND | none | 2 |
| Item 7 / add-gate (iv) unwaived covenant instances | NOT FOUND | none | 2 |
| Item 2 DA % of income | NOT FOUND; DA not named; DA-purchased legend dropped (A3P-17) | none | 2 |
| Rs 455 cr borrowings without security (results A3-06) | NOT FOUND | none | 2 |
| Co-lending book, 19.9% NPL (results A3-12) | NOT FOUND | none | 2 |
| Mortgage Stage 3 +175% YoY (checklist open) | NOT FOUND; no product-wise asset quality | none | 2 |
| Auditor change SSKM to MSKA (results A3-24) | NOT FOUND | none | 1 |
| AGM 1-Sep scrutinizer report and dissent % | NOT FOUND | none | 1 |
| KMP churn | Roster changed with no narrative (A3P-09) | 459-494 | 1 |
| Drought-state AUM, CE, PAR | NOT FOUND (A3P-04) | none | 1 |

Addressed in the deck (for A4):

| Item | Q2 deck reading | Line |
|---|---|---|
| 1 GNPA trend | 4.20% (Q1 4.49%); trigger needs an upward reversal, not fired | 130 |
| 3 AUM growth YoY | 26.03% (Q1 28.0%); trigger is below 20%, not fired | 824 |
| 4 FY27 PAT >= Rs 270 cr | H1 161, run-rate 322; Q2 includes DA gain and ECL release (A3P-05, A3P-07) | 883 |
| 5 Credit cost band | Q2 3.82%, H1 3.95% (Q1 restated 4.03%) | 571, 589 |
| 6 PCR >= 60% / add-gate (ii) | 62.42%, down from 63.80%; basis changed (A3P-15) | 679 |
| 8 Over-lending metrics | Repeat share 51.4% (falling); AUM per active loan about Rs 1.10 lakh, flat (7,597 cr / 6,92,676 loans against 7,324 cr / 6,69,261); ATS on disbursement up (LAP 4.9 to 5.4 lakh); GNPA falling, so trigger not fired | 783, 414-420 |
| Add-gate (iii) refined FY27 guidance | Not refined; repeated verbatim (A3P-14) | 822-837 |
| Bucket 1 CE falling | 52.8% (Q1 54.5%); UP Sep 47.6% (A3P-06) | 577, 640 |
| Disbursement +10% YoY | Confirmed on chart; commentary uses QoQ +15% (A3P-13) | 120, 150 |

```yaml
stage: A3-forensics
company: "AYE"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/aye-q2fy27/work/forensics_presentation_aye_q2fy27.md"
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
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3P-01", check: "F1", line: "818, 297, 299, 796-806, 855; prior L712", classification: "AMBIGUOUS", implication: "No new branches in H1FY27 or since FY26; existing-branch headroom 4,408 cr at 21 cr ceiling covers under half of the +8,300 to +10,300 cr the 28-33% 3-year CAGR needs; either the ceiling rises or branch opex returns"}
  - {id: "A3P-02", check: "F6", line: "865, 555, 414-420, 721, 751; prior L336-341, L477, L619", classification: "AMBIGUOUS", implication: "Mortgage-share and tenor promises repeated; mortgage share 23.3% to 23.2%, AI/ML underwriting 32% flat, primary ML channel 180 branches for 3 quarters"}
  - {id: "A3P-03", check: "F6", line: "757-758; prior L654", classification: "NEUTRAL-FACT", implication: "Upsell team 126/100 to 154/133 staff/branches; no outcome metric"}
  - {id: "A3P-04", check: "F7", line: "114-115, 121-122, 633, 640; prior L093", classification: "AMBIGUOUS", implication: "New drought framing names MH, KA, MP; those states sit inside Rest States; exposure NOT FOUND (R266); pre-emptive cover for H2 asset quality"}
  - {id: "A3P-05", check: "F12", line: "662-665, 670, 679, 881; prior L564-567, L580", classification: "AMBIGUOUS", implication: "Same-basis ECL cover 4.17% to 3.85%, Stage 2 58.07% to 47.44%; ECL stock about -12 cr on +3.7% loans; holding June cover costs about 17 cr post-tax, about 20% of Q2 PAT; implied write-offs and other about 94 cr; slippage not disclosed"}
  - {id: "A3P-06", check: "F12", line: "577, 640, 995; prior L497, L546", classification: "FORWARD-SIGNAL", implication: "Bucket 1 CE 54.5% to 52.8%; UP Sep 47.6% lowest of nine months shown, Rajasthan Q2 avg 55.6% vs 59.9%; feeds PAR 30 and Stage 3 in Q3; leading indicator for GNPA trigger"}
  - {id: "A3P-07", check: "F12", line: "876, 883, 135, 923", classification: "FORWARD-SIGNAL", implication: "Fee and other income +11 QoQ equals DA gain 10.12 (results A3-13); DA about 62% of PAT QoQ rise; fee -14% YoY; record PAT depends on DA recurrence and no cover rebuild"}
  - {id: "A3P-08", check: "F12", line: "503-516, 531, 917-921, 878; prior L423-436", classification: "AMBIGUOUS", implication: "CoB pair down vs Q1 but finance cost on ATA +28 bps, finance cost +10.7% vs AUM +3.7%, NIM on ATA -35 bps; negative carry or pre-funding"}
  - {id: "A3P-09", check: "F13", line: "459, 470-494, 50, 61, 1006; prior L033, L045, L378, L389-391", classification: "AMBIGUOUS", implication: "CTO replaced, CCO added, Year-1 tenures 1 to 3, cover signer CFO to CS; deck still names Gaurav Seth CFO; KMP churn now CFO and CTO"}
  - {id: "A3P-10", check: "F14", line: "745-746, 261, 347, 798-801; prior L642-643", classification: "AMBIGUOUS", implication: "Primary 180 + BAU 444 = 624 vs 571 branches; Q1 180 + 391 = 571; error or overlapping channel definition"}
  - {id: "A3P-11", check: "F14", line: "874-877, 920, 248; prior L763-766", classification: "NEUTRAL-FACT", implication: "P&L growth columns print against wrong rows; interest income +29.1% and fee -14% YoY not printed; -053 bps typo; orphan # footnote"}
  - {id: "A3P-12", check: "F15", line: "941-953, 276; prior L819-827", classification: "FORWARD-SIGNAL", implication: "Alpha Wave India (7.8% at Jun) leaves the more-than-5% list; largest category 67.0% to 62.1%; PE supply overhang; lock-up date NOT FOUND"}
  - {id: "A3P-13", check: "F16", line: "120, 150, 824; prior L099, L715", classification: "FORWARD-SIGNAL", implication: "Commentary switches disbursement framing from YoY (+22% Q1) to QoQ (+15%); YoY is +10%; AUM YoY 28.0% to 26.03%; slower AUM growth ahead"}
  - {id: "A3P-14", check: "F16", line: "822-837, 142; prior L713-728", classification: "AMBIGUOUS", implication: "Guidance repeated verbatim, not refined; H1 NIM 112 bps above band implies H2 NIM about 12.6-13.6%; opex above, RoTA below band; 25% AUM floor needs H2 +15.9% with no new branches"}
  - {id: "A3P-15", check: "F16", line: "665, 670, 679, 681; prior L567, L580, L582", classification: "AMBIGUOUS", implication: "Excluding-management-overlay footnote dropped; 30-Jun restated to 58.07/63.84/4.17%; implied Jun overlay about 11 cr; ex-overlay add-gate test cannot run"}
  - {id: "A3P-16", check: "F16", line: "777, 783-784; prior L673, L679-680", classification: "AMBIGUOUS", implication: "Tele-caller productivity and foreclosure moved to H1 basis; implied Q2 productivity about 1.37 cr (-22% QoQ), foreclosure about 5.83%; repeat share 52.6 to 51.4%"}
  - {id: "A3P-17", check: "F16", line: "796-816; prior L691-710", classification: "AMBIGUOUS", implication: "Growth-contribution window and vintage buckets redefined; DA-purchased category and footnote dropped; purchased AUM location not determinable"}
  - {id: "A3P-18", check: "F16", line: "571, 920-926, 175, 186; prior L104, L157, L804-810", classification: "NEUTRAL-FACT", implication: "Q1FY27 ratios restated (credit cost 4.01 to 4.03%, RoE 11.68 to 11.60%) with no Q1 reclassification note"}
  - {id: "A3P-19", check: "F16", line: "426, 420; prior L347", classification: "NEUTRAL-FACT", implication: "Deck now calls hypothecation loans (76.8% of AUM) unsecured, partly secured on business assets; LGD relevance"}
  - {id: "A3P-20", check: "F17", line: "Section 5; 130, 577, 679, 783, 822-829", classification: "CONFIRMATORY-NEGATIVE", implication: "Two decks silent on gross slippage, write-offs, covenant count, DA income, co-lending, product-wise Stage 3; add-gate (i) bear reading applies"}
forward_signals: ["A3P-06", "A3P-07", "A3P-12", "A3P-13"]
ambiguous: ["A3P-01", "A3P-02", "A3P-04", "A3P-05", "A3P-08", "A3P-09", "A3P-10", "A3P-14", "A3P-15", "A3P-16", "A3P-17"]
commitments:
  - {commitment: "FY27 AUM growth 25.0-30.0% YoY", implied_date: "2027-03-31", ref: "line 824 (R637)", status_word: "underway"}
  - {commitment: "FY27 NIM 14.25-14.75%", implied_date: "2027-03-31", ref: "line 825 (R638)", status_word: "underway"}
  - {commitment: "FY27 opex 8.25-8.75%", implied_date: "2027-03-31", ref: "line 827 (R639)", status_word: "underway"}
  - {commitment: "FY27 credit cost 3.5-4.0%", implied_date: "2027-03-31", ref: "line 828 (R640); line 131 (R045)", status_word: "underway"}
  - {commitment: "FY27 return on total assets 4.0-4.5%", implied_date: "2027-03-31", ref: "line 829 (R641)", status_word: "underway"}
  - {commitment: "Delivering on FY27 guidance", implied_date: "2027-03-31", ref: "line 142 (R069)", status_word: "underway"}
  - {commitment: "H2 focus on productivity and asset quality", implied_date: "H2 FY27", ref: "line 141 (R068)", status_word: "initiated"}
  - {commitment: "3-year normalized credit cost 3.25-3.75%", implied_date: "about FY30", ref: "line 845 (R659)", status_word: "initiated"}
  - {commitment: "3-year RoA 4.0-4.5% and RoE 17.0-20%", implied_date: "about FY30", ref: "lines 849-851 (R660)", status_word: "initiated"}
  - {commitment: "3-year AUM CAGR 28-33%", implied_date: "about FY30", ref: "line 855 (R661)", status_word: "initiated"}
  - {commitment: "3-year opex 7.0-7.5%", implied_date: "about FY30", ref: "line 860 (R662)", status_word: "initiated"}
  - {commitment: "Increase mortgage loan share; deepen AI/ML underwriting", implied_date: "not dated", ref: "line 865 (R663)", status_word: "initiated"}
  - {commitment: "Increase average tenor of assets", implied_date: "not dated", ref: "line 555 (R380); prior L477", status_word: "initiated"}
  - {commitment: "Upsell ML loans to HL repeat customers (154 staff, 133 branches)", implied_date: "not dated", ref: "lines 757-758 (R586); prior L654", status_word: "underway"}
  - {commitment: "OER falls as ML AUM per branch grows", implied_date: "not dated", ref: "line 759 (R585)", status_word: "initiated"}
  - {commitment: "Existing branches add Rs 4,000+ cr AUM", implied_date: "medium term", ref: "lines 799-801 (R631)", status_word: "initiated"}
  - {commitment: "HUL CSR donation INR 50 lakh for Oct-2026 to Mar-2027", implied_date: "2027-03-31", ref: "line 977 (R885, R887)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck fills part of the filing gap. PCR 62.42% and Bucket 1 CE 52.8% are disclosed. Gross slippage, write-offs, covenant count and DA income are not, for two decks running. Central point: on the deck's own 30-Jun basis, ECL cover fell from 4.17% to 3.85%. The ECL stock fell about Rs 12 cr while loans grew 3.7%. Holding June cover would have cost about Rs 17 cr post-tax, about 20% of Q2 PAT. The Rs 10.12 cr DA gain plus this release more than explains the Rs 12 cr QoQ PAT rise behind the 'highest ever' claim. The deck also dropped its 'excluding management overlay' footnote, so the add-gate ex-overlay test cannot run. Bucket 1 CE is the leading signal: UP printed 47.6% in September, its lowest of nine months. Guidance was repeated, not refined, while H1 NIM ran 112 bps above the band. Alpha Wave left the more-than-5% list. Pipeline errors: A1 swapped the R076/R077 labels (1,219 is Q1FY27), and A1 omitted line 667 (83, 308, 6,865) and line 807 (0)."
```
