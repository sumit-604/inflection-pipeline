# A3 FORENSIC NOTES: PITTIENG, doctype RESULTS, Q2 FY27 (quarter and half-year ended 30-Sep-2026)

Agent: A3 forensic notes | Model: claude-opus-5-5 | Date: 2026-10-23
Inputs read: A1 structured (R001-R643, all rows), A1 fulltext (lines 1-696, all), A2 ledger (all sections), Notion context (memory, not evidence).
Not read: source PDF, anything under inputs/. Prior-quarter fulltext: NOT PASSED (the task message names none). Diffs that need it are marked as such.
Units: Rs lakhs unless stated (x0.01 = Rs crores). Basis: STANDALONE only. PIPL and DFPL were amalgamated (appointed date 01-Apr-2026, effective 23-Sep-2026). Prior periods are restated.
Caveat: A1 transcribed pp5-9 from page images. Casting differences of a few paise on those pages may be transcription artefacts. Each such item says so.

---

## 0. LEDGER RECONCILIATION

| Ledger section | Rows | Read at cited line | Result |
|---|---|---|---|
| 1 Notes N1-N7 + FN-a..d | R418-R539, R066-R068, R244, R257-R259, R334-R336, R417, R457, R482-R483, R487, R501, R544 | yes | all read |
| 2 Line items LI001-LI126 | R069-R416, R433-R538 | yes | all read; P&L, BS, CF, recon and segment arithmetic re-footed (see below) |
| 3 Agenda items A1-A6, time, signature | R001-R038 | yes | all read |
| 4 Auditor paras AP1-AP8 | R039-R068 | yes | all read |
| 5 Annexures 1-3, SMP profiles, SIG2 | R540-R643 | yes | all read |
| 6 Entities (42) | as listed | yes | all read |
| 7 Cross-refs X1-X7 | as listed | yes | all ties hold (X1 57,843.80 = 57,843.80; X3 Rs 450 cr and FY 2030-31 match; X4 5,77,500 / 736.72 match; X5 8-Sep-2026 / 1-Apr-2026 match) |

ids_in_structured 643 | ids read by A3 643 | ledger_reconciled_pct 100.

### Re-footing done by A3 (arithmetic, no estimates)
- P&L: every column ties Total Income minus Total expenses = PBT, and Q1 + Q2 = H1 on every line. Exception: the Q2 FY27 expense components sum to 53,527.87 against a printed total of 53,528.07. H1 has the same 0.20 gap (A3-27).
- Tax lines ((a)+(b)+(c) = total) and PAT tie in all six columns.
- BS: assets = liabilities on both dates. Other equity 89,287.10 + paid-up 1,883.10 = 91,170.20 (line 256-258). 83,197.80 + 1,883.10 = 85,080.90.
- Equity roll-forward H1: 83,197.80 + TCI 6,529.01 - dividend 931.50 + SBP 483.02 = 89,278.33 vs 89,287.10. The residual is 8.77, immaterial and unexplained.
- CF: A, B and C subtotals and A+B+C foot in both columns. Closing cash 5,907.64 ties to the BS (line 248). The financing total foots only with lease principal printed as a positive (A3-25).
- Note 4 reconciliations: all 16 reported + adjustment = restated sums tie. The BS recon ties: 2,05,603.93 - 5,435.05 = 2,00,168.88. The CF recon ties.
- Segment: India + Outside India = total revenue in all columns. Segment assets: the Q2 FY26 column sums to 2,00,643.92 against 2,00,643.94 printed (A3-27).

### A2 flags resolved
| Flag | Row | Resolution |
|---|---|---|
| FOOTNOTE_UNRESOLVED | R059 | Line 174 reads "l 10758W/Wl00377". The page-5 stamp transcription at line 225 reads "FRN 110758W/W100377". Resolved as an l-for-1 text-layer substitution. FRN 110758W/W100377. |
| FOOTNOTE_UNRESOLVED | R062 | Line 177 reads "222"OOctober, 2026". This is the same doubled-glyph artefact seen on pp3-4 ("PPIPL", "DDFPL", line 162). Most probable reading: 22nd October 2026 [INFERENCE]. It agrees with Note 1 (line 337-338) and the results signing date (line 410). Not a finding. |
| FOOTNOTE_UNRESOLVED | R064 | UDIN "26122131RYIEQP8126" (line 179). Format is consistent: YY 26 + membership 122131 (matches line 178) + 10 characters = 18 characters. ICAI portal check: PENDING LIVE VERIFICATION. |
| FOOTNOTE_UNRESOLVED | R502 | The segment last column is labelled "Half-Year Ended 31.03.2026" (line 392). The values are full-year (1,91,280.36 = line 187 FY column). Drafting error, finding A3-23. |
| FOOTNOTE_UNRESOLVED | R577 | Annexure 2 layout is scrambled (lines 467-501): labels b)-h) do not sit against their values. Reading by content gives (b) "Yes", (c) 5,77,500 shares, (d) one share per option, (e) the pricing text, (f-j) Not Applicable. Layout only, no finding. |
| ARITH_CHECK | R556/R558 vs R559-R562 | Sheet metal: 1,08,000 + NA -> 1,60,000, so the whole +52,000 MT (+48.1%) is the new proposal. Machine hours: the table calls 10,80,000 an "addition" (line 433-434). As an addition, the post figure would be 18,93,600, which does not tie to 13,14,000. As a level (narrative line 424-425), the new proposal adds 2,34,000 hours (+21.7%). Finding A3-26. |

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | LI015 R153-R158 | 202 | "6 Extraordinary items \| - \| - \| - \| - \| - \| -" | NEUTRAL-FACT | Ind AS 1 does not allow items to be presented as extraordinary, so this line is a legacy template relic. Nothing can land here. It is one more governance data point for the F14 cluster. |
| A3-02 | F1 | LI013 R141-R146 | 200 | "4 Exceptional items \| - \| - \| - \| - \| - \| -" | AMBIGUOUS | The amalgamation became effective inside the quarter, but no scheme cost (stamp duty, NCLT, integration) is shown separately. The Maharashtra SGST Section 67 search of 8-Oct-2026 (Notion memory) is the live candidate for this line in H2. Ask where scheme costs sit and whether any demand or deposit under protest has arisen. |
| A3-03 | F1 | LI005 R093-R098; LI025-LI026 R213-R224 | 192, 216 | "(b) Purchase of Stock-in-trade \| 181.62 \| 192.77 \| - \| 374.39 \| - \| 1,966.72"; "Fair value of Changes in Cashflow Hedge \| 144.67 \| 205.43 \| - \| 350.10 \| - \| (367.53)" | NEUTRAL-FACT | Two transaction classes were nil in H1 FY26 and started in H2 FY26: traded goods (FY26 1,966.72, all in H2; now about 182-193 per quarter) and cash-flow hedge accounting (FY26 -367.53, H1 FY27 +350.10). Hedge reserve reclassifications will reach the P&L as hedged exports settle. |
| A3-04 | F2 | LI110-LI117 R433-R481 | 358-368 (quote 360) | "Profit after tax \| 2,084.15 \| 866.04 \| 2,950.19 \| 3,558.25 \| 451.17 \| 4,009.42" | AMBIGUOUS | The former subsidiaries' PAT, as a share of reported old-PEL PAT, moved from 12.7% (Q2 FY26) to 41.6% (Q1 FY27). That is +28.9 pp, or +11.3 pp against Q1 FY26 (30.2%). Old-PEL Q1 PBT fell 15.7% YoY while the subsidiaries' PBT rose 59.7%. From Q2 FY27 this split is no longer disclosed. Ask what drove the subsidiaries' profit (foundry or castings?) and whether management will keep disclosing it. Table in section 4. |
| A3-05 | F4 | FN-a R068; LI114-LI117 R458-R481 | 185, 364 | "Year ended 31.03.2026: Un-Audited Reported \| Adjustments due to Scheme of Amalgamation \| Un-Audited Restated" | AMBIGUOUS | The current period is fully reviewed (no Other Matters paragraph, standalone). The comparative base is a different matter. Restatement adjustments are 17.2% of restated FY26 PAT (2,028.20 / 11,780.75) and 29.4% of restated Q1 FY27 PAT (866.04 / 2,950.19). The review report does not say who audited or reviewed those PIPL/DFPL figures, and the filing labels FY26 both "Audited" and "Un-Audited". Every YoY growth rate rests on this base. |
| A3-06 | F5 | AP6 R050-R058 | 155-170 (quote 170) | "Our Conclusion is not modified in respect of this matter." | NEUTRAL-FACT | New EoM paragraph on the amalgamation and the Appendix C restatement, with the conclusion unmodified. A verbatim diff against the Q1 FY27 review report is not possible because no prior-quarter fulltext was passed. Diff it in Q3 FY27: if the EoM persists with a changed scope (for example goodwill or restatement scope), that is a finding. |
| A3-07 | F6 | A4 R015-R019; ANX1 R563-R567 | 51, 447 | "Approved a capex of ₹450 crores to increase manufacturing capacities"; "Internal accruals and Debt" | FORWARD-SIGNAL | Rs 450 Cr, phased to FY 2030-31, with no split between accruals and debt (line 447). Scale: 49.4% of net worth (Rs 911.7 Cr, line 258) and 3.8x FY26 restated PAT (Rs 117.8 Cr). It sits on top of H1 capex cash of Rs 256.8 Cr (line 310) and computed net debt of Rs 538.7 Cr. It adds +48.1% lamination capacity while lamination utilisation is ~78% (line 427). |
| A3-08 | F6 | ANX1 R550-R552 | 424-425 | "approved expansion currently underway to enhance machining capacity to 10,80,000 machining hours by Q1 2029-30" | AMBIGUOUS | Status word is "underway". Completion is Q1 FY30. Notion memory carries "castings to 36,000 MT by Q1 FY29" for the Rs 290 Cr program. If that is the same program, this is a one-year slip. Lean bear: ask whether the Q1 2029-30 machining date replaces an earlier Q1 FY29 milestone. |
| A3-09 | F6 | N4 R423-R428 | 345-349 (quote 348) | "became effective on 23rd September 2026 upon filing of the certified copy of the order" | NEUTRAL-FACT | Milestone completed: Board approved 5-Feb-2026 (line 345), NCLT order 8-Sep-2026, effective 23-Sep-2026. This closes the Notion amalgamation monitoring item. |
| A3-10 | F8 | LI018 R171-R176 | 206 | "(b) Tax relating to earlier years charge / (Credit) \| (88.05) \| - \| (106.75) \| (88.05) \| (106.75) \| (130.90)" | NEUTRAL-FACT | Non-zero in Q2 of both years and in FY26. This is a recurring Q2 return true-up credit. Treat it as non-recurring in run-rate tax. |
| A3-11 | F8 | LI017-LI020 R165-R188 | 205-208 (quote 207) | "(c) Deferred tax charge / (Credit) \| 48.41 \| (134.90) \| 252.79 \| (86.49) \| 454.72 \| 904.15" | FORWARD-SIGNAL | H1 ETR is 22.20% against the 25.17% statutory rate, a 297 bps shield: earlier-years credit 108 bps, deferred credit 106 bps (all from the Q1 credit of 134.90), current tax below statutory 82 bps. Q2 printed 25.13%, but 27.07% before the earlier-years credit. FY26 was 29.70%. Deferred tax flipped from a charge (FY26 904.15) to a credit. The 25% tax guide in H2 carries step-up risk. Ask what created the Q1 deferred credit (merger, regime switch). |
| A3-12 | F9 | LI022-LI027 R195-R230 | 212, 218 (quote 212) | "Remeasurement of the net defined benefit liability/assets \| (154.37) \| 58.48 \| 117.59 \| (95.89) \| 98.43 \| 217.50" | AMBIGUOUS | The Q2 actuarial loss of 154.37 equals 71% of the full FY26 gain, and the QoQ swing (212.85) equals 98% of FY26. Total OCI swung 204.74 between Q1 and Q2 (+197.49 to -7.25), which exceeds full-year FY26 OCI (112.27 in magnitude). The amalgamation in the same quarter makes harmonisation of actuarial assumptions a candidate cause. Verify assumptions at the FY27 Annual Report. |
| A3-13 | F10 | N5 R494-R499; ANX2 R573-R583, R587-R592 | 385-386, 492-493 | "the grant of options is anti-dilutive"; "a discount of 23.03% to the closing market price of ₹ 957.20" | AMBIGUOUS | Paid-up capital is unchanged at 1,883.10 in every column (line 220), and basic = diluted EPS in every column (lines 223-224). But options at 736.72 against a market of 957.20 are in the money, and Ind AS 33 treats in-the-money options as dilutive. The "anti-dilutive" claim needs support; outstanding option count NOT FOUND. Pool 13,00,000 = 3.45% of 3,76,62,000 shares. The trust holds 7,40,000 (line 383), Grant 2 is 5,77,500, and the trust "can either acquire ... or the Company will issue shares" (lines 510-512). PBO 25% vests at end of Year 2 on conditions not disclosed (line 522-524). |
| A3-14 | F10 | ANX2 R574, R581 | 488-490 | "equity shares remains broadly comparable to that at the time of the first grant" | AMBIGUOUS | 957.20 is 29.9% above the 736.72 exercise price. The grant-1 market price is NOT FOUND in this filing. "Broadly comparable" holds only if grant 1 was also priced at a deep discount. This is the governance angle on repricing consistency, and it raises the SBP expense run-rate. |
| A3-15 | F11 | LI033-LI041 R260-R277; LI118 R484-R486 | 233-241, 375 (quote 375) | "Total Assets and Liabilities \| 2,05,603.93 \| (5,435.05) \| 2,00,168.88" | AMBIGUOUS | The statutory tie-out passes. But the restated BS has no goodwill line (only intangibles of 519.36, line 235), and restated total assets are Rs 54.4 Cr below the pre-merger standalone figure even though two operating subsidiaries were added. Notion memory carries ~Rs 130 Cr consolidated goodwill (open CGU item). The reported-to-restated equity reconciliation is NOT FOUND. Ask whether the goodwill was adjusted against reserves under Appendix C and what the net-worth effect was. |
| A3-16 | F12 | LI042 R278-R279; LI062-LI063 R318-R321; LI085 R367 | 244, 274, 304 (quote 274) | "Dues to others \| 46,691.27 \| 23,609.24" | AMBIGUOUS | This is a single-segment company, so the segment is the entity. Trade payables rose 23,151.68 (+95.2%, of which "others" rose +97.8%). The CF working-capital release was 16,484.12, while inventory rose 8,378.91 and receivables rose 1,065.25. The whole release is supplier credit. If the payables are LC acceptances (pending operator ruling), they are debt-like. Computed net debt: borrowings 64,042.80 less cash 5,907.64, other bank 4,265.48 and current investments 2.08 = 53,867.60 (Rs 538.7 Cr), against the Rs 491 Cr tracker line. Mar-26 on the same basis: Rs 552.1 Cr (Notion: Rs 555 Cr). A4 adjudicates the tracker. |
| A3-17 | F12 | LI122 R509-R514; LI125 R527-R532 | 395, 399 (quote 399) | "b) Outside India \| 6,719.94 \| 6,463.20 \| 14,854.56" | AMBIGUOUS | Outside-India segment assets fell 54.8% YoY while Outside-India revenue rose 14.2% (13,512.55 to 15,432.79). Candidates: export receivables factored or discounted (which would flatter both the WC release and net debt), an overseas inventory drawdown, or a Note 7 regrouping. Segment liabilities are not disclosed. |
| A3-18 | F12 | LI034 R262-R263; LI040 R274-R275; LI090 R377-R378; LI008 R111-R112 | 234, 241, 310, 195 (quote 234) | "(b) Capital work-in-progress \| 12,032.05 \| 4,981.23" | FORWARD-SIGNAL | CWIP rose 141.5% and other non-current assets (capital advances) rose 251.6% in six months. H1 capex cash was 25,683.05, 3.15x H1 FY26. Finance costs fell 27.8% QoQ (2,262.51 to 1,632.83), while gross borrowings fell only 8.4% from Mar-26. Capitalised borrowing cost could account for up to 70% of the Q2 PBT rise of 903.82. Depreciation and interest step up on commissioning. Ask how much borrowing cost was capitalised. |
| A3-19 | F13 | A6 R025-R029; ANX3a R623-R629 | 66, 584 | "Deputy Chief Executive Officer"; "Date of Redesignation: 22nd October 2026" | AMBIGUOUS | A new Deputy CEO layer is created under the MD&CEO. The former CG Power stampings head becomes Deputy COO. No term of appointment is stated. There is no AR, AGM or director change, so no Role 6 event is triggered. Ask whether this is succession planning or bandwidth for the Rs 450 Cr build, and what the Deputy CEO's remit is. |
| A3-20 | F13 | N4/AP6 R053; ANX3b R631-R636 | 161, 640-641 | "Pitti Industries Private Limited (formerly Bagadia Chaitra Industries Private Limited)"; "supporting integration and growth initiatives" | AMBIGUOUS | Name match only [INFERENCE, not evidence]. The new COO of the Motor & Generator business is Shri Chaitra Sundaresh: Deputy COO since May 2024, two decades in laminations, credited with integration. The amalgamated entity was Bagadia Chaitra, and the Karnataka lamination operations are now being consolidated. Ask whether he has any link to the former owners (consideration, earn-out, related party). Lean bear; do not resolve here. |
| A3-21 | F14 | N5 R498; N4 R430 | 385 vs 353 | "the Company and its subsidiaries have adhered to the requirements of IND AS 102" vs "the Company has no subsidiaries as at the reporting date" | NEUTRAL-FACT | Stale note text carried over from the pre-merger template. Immaterial on its own; counts toward the drafting cluster. |
| A3-22 | F14 | FN-a R068; R259; LI118 R484 | 185, 364, 374 | "Year Ended 31.03.2026 Audited Restated" vs "Year ended 31.03.2026: Un-Audited Reported" | NEUTRAL-FACT | The same FY26 period is labelled Audited (P&L header, BS recon) and Un-Audited (P&L recon). The reported FY26 figures were audited, but the restated ones carry unaudited merger adjustments. The assurance angle is in A3-05. |
| A3-23 | F14 | N6 R502, R508/R514/R520/R526/R532/R538 | 392 | "Half-Year Ended 31.03.2026 Audited Restated" | NEUTRAL-FACT | The column holds full-year values (1,91,280.36 = line 187 FY). Labelling error. |
| A3-24 | F14 | ANX2v R619-R621; LI083 R363-R364 | 558-562, 302 | "first grant approved by the Nomination and Remuneration Committee at its Meeting held on 13th March 2026"; "Share based payment expenses(net) \| 483.02 \| 547.59" | AMBIGUOUS | The H1 FY26 (Apr-Sep 2025) SBP expense of 547.59 predates a grant-1 date of 13-Mar-2026. The filing contradicts itself. Notion memory says March 2025 (the filing wins, but its own numbers point to 2025). Likely a year typo in the Annexure. Ask management to confirm the grant-1 date and the vesting clock. |
| A3-25 | F14 | LI097 R391-R392; LI077 R351; LI079 R355 | 318, 296, 298 (quote 318) | "Cash Payments for Principal portion of lease liability \| 578.15 \| 653.41" | AMBIGUOUS | A payment is printed positive, and the financing total foots only with it as an inflow (-12,020.21 ties). OCI remeasurement and hedge items (lines 296, 298) also sit inside the operating adjustments to PBT. If principal is an outflow, the working-capital line or CFO is overstated by 1,156.30 in H1 FY27, with the statement still footing to BS cash. The image transcription cannot explain this, because the total confirms the sign. Ask for the lease cash-flow presentation. |
| A3-26 | F14 | ANX1 R549-R562 | 424-425, 432-439 | "On-going Capacity addition to be completed by Q1 2029-30" (header) vs "enhance machining capacity to 10,80,000 machining hours" | AMBIGUOUS | The header calls 10,80,000 an addition. The narrative and the 13,14,000 post figure only reconcile if it is a level. That puts the Rs 450 Cr machining add at 2,34,000 hours (+21.7%), not more. The lamination add is +52,000 MT (+48.1%). Confirm the capacity split behind the Rs 450 Cr. |
| A3-27 | F14 | LI004-LI011 R087-R134; LI124 R523, R525 | 191-198, 398 | "Total expenses \| 53,528.07"; "1,85,789.36 \| 2,17,982.52 \| 1,85,789.38" | NEUTRAL-FACT | The Q2 FY27 and H1 FY27 expense components cast 0.20 below the printed totals. The same-date (30-Sep-2025) India segment assets differ by 0.02 between columns. Immaterial. These may be artefacts of A1's image transcription of pp5-9. |
| A3-28 | F15 | N4 R053-R054, R429-R430 | 351-353 (quote 351) | "PIPL and DFPL, being wholly-owned subsidiaries of the Company, stand dissolved without winding up" | NEUTRAL-FACT | Two entities deleted, and the reporting basis moves from consolidated to standalone (same perimeter: restated Q1 FY27 revenue of Rs 529.1 Cr matches Notion's Rs 529 Cr). The tracker label "consolidated net debt" must be redefined as standalone. Separate visibility of the foundry (DFPL) and Karnataka lamination (PIPL) ends unless management discloses it voluntarily. |

Count: 28 findings. FORWARD-SIGNAL 3, AMBIGUOUS 15, NEUTRAL-FACT 10, CONFIRMATORY-NEGATIVE 0.

---

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 35 ZERO_STANDING tags across 13 lines reviewed. Extraordinary-items relic (A3-01). Exceptional line nil through a merger quarter, with the SGST search as candidate (A3-02). Trading and hedge classes switched on in H2 FY26 (A3-03). |
| F2 Standalone vs consolidated | FINDING | No consolidated statement this quarter. Decomposition run on the Note 4 reconciliation (old PEL vs restated, the former consolidated perimeter). The subsidiaries' share of PAT widened +28.9 pp (A3-04). |
| F3 Shell-entity detection | PASS | No consolidated cost lines to compare. Note 4 shows PIPL/DFPL were operating, not shells (income adjustment 8,735.69 in Q1 FY27, line 358). No Going Concern EoM. |
| F4 Unaudited contribution | FINDING | Current period 0% (no Other Matters, standalone). The restated comparative base (17.2% of FY26 PAT, 29.4% of Q1 FY27 PAT) has an unstated assurance status (A3-05). |
| F5 EoM scope tracking | FINDING | New EoM on the amalgamation, conclusion unmodified. Prior-quarter verbatim diff not possible: input not passed (A3-06). |
| F6 Forward-commitment mining | FINDING | 10 commitments registered (section 3). Rs 450 Cr capex (A3-07). Machining date Q1 2029-30 (A3-08). Amalgamation completed (A3-09). |
| F7 Hedge phrase mining | PASS | Only lexicon hit is "subject to the achievement of performance conditions" (line 522, ESOP boilerplate). No new hedge on revenue lumpiness or customer concentration in the notes. |
| F8 Tax forensics | FINDING | Earlier-years tax non-zero (A3-10). H1 ETR 22.20% vs 25.17%, a 297 bps shield; Q2 underlying 27.07% (A3-11). |
| F9 OCI forensics | FINDING | Actuarial sign flip, Q2 loss 154.37. QoQ total OCI swing 204.74 exceeds FY26 full-year OCI 112.27 (A3-12). |
| F10 Share count and dilution | FINDING | Paid-up flat, basic = diluted, but the "anti-dilutive" claim conflicts with in-the-money options. Grant 2 pricing rationale (A3-13, A3-14). |
| F11 Reserves and net worth tie-out | FINDING | Statutory tie holds (91,170.20). No goodwill line in the restated BS, against ~Rs 130 Cr in Notion memory. Equity reconciliation NOT FOUND (A3-15). |
| F12 Segment forensics | FINDING | Single segment, so entity-level build analysed. Payables-funded WC release and net debt (A3-16). Outside-India assets -54.8% (A3-17). CWIP build and possible interest capitalisation (A3-18). |
| F13 Board outcome beyond results | FINDING | No AR, AGM or director item. Capex, ESOP grant, Deputy CEO layer (A3-19). Name-match question (A3-20). Dividend record date 2-Nov-2026 registered. |
| F14 Note drafting inconsistencies | FINDING | Seven items: subsidiaries text, FY26 label, segment column label, grant-1 date, lease sign, capacity table header, casting (A3-21 to A3-27). |
| F15 Entity list diffs | FINDING | PIPL and DFPL dissolved, consolidation ends (A3-28). |
| F16 Presentation dropped/reframed | N.A. | Doctype results. |
| F17 Concall silence audit | N.A. | Doctype results. |

PASS 2 | FINDING 13 | N.A. 2 | blank 0. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Ref (line / row) | Status word |
|---|---|---|---|---|
| C1 | Interim dividend Rs 2/- (40%) per Rs 5 share, record date Monday 2-Nov-2026 | paid on or before 21-Nov-2026 | lines 42-49; R008-R014, R421 | initiated (declared) |
| C2 | Capex Rs 450 Cr: raise capacities and value-add; consolidate fragmented Karnataka lamination ops into one facility | phased to FY 2030-31 | lines 51-53, 441-459; R015-R019, R563-R571 | initiated (Board approved) |
| C3 | Post-proposed capacity 1,60,000 MT sheet metal and 13,14,000 machine hours | by FY 2030-31 | lines 436-439; R556, R558 | initiated |
| C4 | On-going machining expansion to 10,80,000 machine hours | Q1 2029-30 | lines 424-425; R550-R552 | underway |
| C5 | Financing of C2: internal accruals and debt, split not stated | with C2 | line 447; R567 | initiated |
| C6 | Amalgamation of PIPL and DFPL into PEL | effective 23-Sep-2026 (appointed 1-Apr-2026) | lines 345-353; R423-R430 | completed |
| C7 | ESOP Grant 2: 5,77,500 options at Rs 736.72; first vesting no earlier than one year after grant; PBO 25% at end of Year 2, TBO starts Year 3 | first vest about Oct-2027 (PBO), schedule to about Oct-2034; exercise to 5 years after final vest | lines 55-57, 515, 522-556; R020-R021, R588-R618 | initiated |
| C8 | Trust route: trust buys shares secondary or Company issues shares to Trust | undated | lines 509-512; R587 | initiated |
| C9 | Re-designation: Agarwala to Deputy CEO, Sundaresh to COO M&G | effective 22-Oct-2026 | lines 59-69; R025-R027 | completed |
| C10 | Patil promoted to Deputy COO and joins SMP | effective 22-Oct-2026 | lines 71-74, 687-691; R028-R029 | completed |

Status-change check: C4 "underway" and C6 "completed" are the milestone words. The prior-quarter status of C4 cannot be checked (prior fulltext not passed). The memory date conflict is carried as A3-08.

---

## 4. SUPPORTING TABLES

### F2 decomposition (Note 4: reported old-PEL vs adjustment = former subsidiaries net of eliminations)

| Period | Income adj / reported | PBT adj / reported | PAT adj / reported | Subsidiary PBT margin | Old-PEL PBT margin |
|---|---|---|---|---|---|
| Q1 FY26 (H1 minus Q2, derived) | 19.2% | 24.5% | 30.2% | 9.6% | 7.5% |
| Q2 FY26 | 19.4% | 13.1% | 12.7% | 7.7% | 11.4% |
| H1 FY26 | 19.3% | 17.5% | 18.5% | 8.6% | 9.5% |
| H2 FY26 (FY minus H1, derived) | 20.5% | 21.9% | 23.6% | 8.2% | 7.7% |
| FY26 | 19.9% | 19.4% | 20.8% | 8.4% | 8.6% |
| Q1 FY27 | 19.7% | 46.3% | 41.6% | 13.1% | 5.6% |

Caveat: the adjustment is net of intercompany eliminations (for example dividends from subsidiaries), so it is not a pure subsidiary contribution. Q2 FY27 and H1 FY27 are merged and have no split.

### F8 tax

| Period | PBT | Total tax | ETR | ETR before earlier-years credit |
|---|---|---|---|---|
| Q2 FY27 | 4,525.92 | 1,137.34 | 25.13% | 27.07% |
| Q1 FY27 | 3,622.10 | 671.91 | 18.55% | 18.55% |
| Q2 FY26 | 5,386.68 | 1,377.26 | 25.57% | 27.55% |
| H1 FY27 | 8,148.02 | 1,809.25 | 22.20% | 23.29% |
| H1 FY26 | 9,041.18 | 2,743.52 | 30.34% | 31.53% |
| FY26 | 16,758.11 | 4,977.36 | 29.70% | 30.48% |

DTL (net) 2,365.23 to 2,327.34 (line 266). The P&L deferred credit is 86.49 and the OCI deferred tax is a net charge of 63.97. The 15.37 residual against the BS movement is unexplained and immaterial.

### Monitoring-checklist data visible in this filing (for A4; F17 itself is N.A. on results)
- Net debt row: computed Rs 538.7 Cr at 30-Sep-2026 (A3-16 basis), against the Rs 491 Cr line. Basis caveats: standalone now equals the former consolidated perimeter; lease liabilities of Rs 113.9 Cr are excluded; payables under the pending ruling.
- Castings and machined volume row: NOT FOUND in the results filing (no tonnage disclosed).
- Export railway row: Outside India revenue is Rs 154.3 Cr in Q2 FY27, against Rs 137.5 Cr in Q1 FY27 and Rs 135.1 Cr in Q2 FY26 (line 395). That is total exports, not railway only, which is the pending operator ruling.
- Maharashtra SGST search (8-Oct-2026): no note, no contingent-liability text, no subsequent-event note in this filing. See A3-02.
- Amalgamation: completed, effective 23-Sep-2026 (A3-09).
- Notion differences logged (the filing wins): FY26 net debt Rs 555 Cr (Notion) vs Rs 552.1 Cr computed; ESOP grant 1 March 2025 (Notion) vs 13-Mar-2026 (line 562), with the filing's own SBP line supporting 2025 (A3-24).

---

```yaml
stage: A3-forensics
company: "PITTIENG"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/pittieng-q2fy27/work/forensics_results_pittieng_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
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
  - {id: "A3-01", check: "F1", line: "202", classification: "NEUTRAL-FACT", implication: "Extraordinary items line is an Ind AS 1 template relic; nothing can land there"}
  - {id: "A3-02", check: "F1", line: "200", classification: "AMBIGUOUS", implication: "Exceptional nil through merger quarter; scheme costs not shown; SGST search (8-Oct-2026) is the H2 candidate"}
  - {id: "A3-03", check: "F1", line: "192, 216", classification: "NEUTRAL-FACT", implication: "Traded goods and cash-flow hedge accounting both started in H2 FY26; hedge reserve recycles to P&L"}
  - {id: "A3-04", check: "F2", line: "358-368", classification: "AMBIGUOUS", implication: "Ex-subsidiary PAT share of old-PEL PAT 12.7% Q2 FY26 to 41.6% Q1 FY27 (+28.9 pp); split no longer disclosed after merger"}
  - {id: "A3-05", check: "F4", line: "185, 364", classification: "AMBIGUOUS", implication: "Restated comparatives (17.2% FY26 PAT, 29.4% Q1 FY27 PAT) have unstated assurance; YoY base rests on them"}
  - {id: "A3-06", check: "F5", line: "155-170", classification: "NEUTRAL-FACT", implication: "New EoM on amalgamation, conclusion unmodified; prior-quarter verbatim diff not possible, recheck scope in Q3"}
  - {id: "A3-07", check: "F6", line: "51, 447", classification: "FORWARD-SIGNAL", implication: "Rs 450 Cr capex to FY2030-31, 49% of net worth, debt/accrual split not given, on top of Rs 257 Cr H1 capex"}
  - {id: "A3-08", check: "F6", line: "424-425", classification: "AMBIGUOUS", implication: "Machining expansion to 10,80,000 hrs by Q1 2029-30; possible one-year slip vs Q1 FY29 in memory"}
  - {id: "A3-09", check: "F6", line: "348", classification: "NEUTRAL-FACT", implication: "Amalgamation milestone completed, effective 23-Sep-2026"}
  - {id: "A3-10", check: "F8", line: "206", classification: "NEUTRAL-FACT", implication: "Earlier-years tax credit recurs each Q2 (88.05, 106.75); exclude from run-rate"}
  - {id: "A3-11", check: "F8", line: "205-208", classification: "FORWARD-SIGNAL", implication: "H1 ETR 22.20% vs 25.17% (297 bps shield); Q2 underlying 27.07%; H2 ETR step-up risk vs 25% guide"}
  - {id: "A3-12", check: "F9", line: "212, 218", classification: "AMBIGUOUS", implication: "Actuarial loss 154.37 in Q2 after gains; OCI swing exceeds FY26 total; verify assumptions at AR"}
  - {id: "A3-13", check: "F10", line: "385-386, 492-493", classification: "AMBIGUOUS", implication: "Anti-dilutive claim vs in-the-money options at 23.03% discount; trust may issue new shares; PBO conditions undisclosed"}
  - {id: "A3-14", check: "F10", line: "488-490", classification: "AMBIGUOUS", implication: "Market 29.9% above exercise price called broadly comparable; grant-1 market price NOT FOUND"}
  - {id: "A3-15", check: "F11", line: "233-241, 375", classification: "AMBIGUOUS", implication: "No goodwill line in restated BS vs ~Rs 130 Cr in memory; restated assets Rs 54.4 Cr below reported; equity recon NOT FOUND"}
  - {id: "A3-16", check: "F12", line: "244, 274, 304", classification: "AMBIGUOUS", implication: "Payables +23,151.68 fund whole WC release; inventory up 8,378.91; computed net debt Rs 538.7 Cr vs Rs 491 Cr tracker"}
  - {id: "A3-17", check: "F12", line: "395, 399", classification: "AMBIGUOUS", implication: "Outside-India assets -54.8% YoY while export revenue +14.2%; factoring or regrouping?"}
  - {id: "A3-18", check: "F12", line: "195, 234, 241, 310", classification: "FORWARD-SIGNAL", implication: "CWIP +141%, capital advances +252%; finance cost -27.8% QoQ suggests interest capitalisation; D&A and interest step up on commissioning"}
  - {id: "A3-19", check: "F13", line: "66, 584", classification: "AMBIGUOUS", implication: "New Deputy CEO layer, no term stated; succession or bandwidth for capex build"}
  - {id: "A3-20", check: "F13", line: "161, 640-641", classification: "AMBIGUOUS", implication: "Name match Chaitra Sundaresh / Bagadia Chaitra [INFERENCE]; ask for any link to former owners"}
  - {id: "A3-21", check: "F14", line: "385, 353", classification: "NEUTRAL-FACT", implication: "Note 5 says Company and its subsidiaries; Note 4 says no subsidiaries"}
  - {id: "A3-22", check: "F14", line: "185, 364, 374", classification: "NEUTRAL-FACT", implication: "FY26 labelled Audited and Un-Audited for the same period"}
  - {id: "A3-23", check: "F14", line: "392", classification: "NEUTRAL-FACT", implication: "Segment column labelled Half-Year Ended 31.03.2026 holds full-year values"}
  - {id: "A3-24", check: "F14", line: "558-562, 302", classification: "AMBIGUOUS", implication: "Grant-1 date 13-Mar-2026 conflicts with SBP expense 547.59 in H1 FY26; likely 2025"}
  - {id: "A3-25", check: "F14", line: "318, 296, 298", classification: "AMBIGUOUS", implication: "Lease principal payment printed as inflow and foots so; CFO or WC line may be overstated by 1,156.30"}
  - {id: "A3-26", check: "F14", line: "424-425, 432-439", classification: "AMBIGUOUS", implication: "Capacity header calls 10,80,000 an addition; ties only as level; Rs 450 Cr adds 2,34,000 hrs and 52,000 MT"}
  - {id: "A3-27", check: "F14", line: "191-198, 398", classification: "NEUTRAL-FACT", implication: "Expense casting gap 0.20 (Q2, H1) and 0.02 segment-asset gap; immaterial, possible transcription artefact"}
  - {id: "A3-28", check: "F15", line: "351-353", classification: "NEUTRAL-FACT", implication: "PIPL and DFPL dissolved; consolidation ends; tracker basis to standalone; foundry visibility lost"}
forward_signals: ["A3-07", "A3-11", "A3-18"]
ambiguous: ["A3-02", "A3-04", "A3-05", "A3-08", "A3-12", "A3-13", "A3-14", "A3-15", "A3-16", "A3-17", "A3-19", "A3-20", "A3-24", "A3-25", "A3-26"]
commitments:
  - {commitment: "Interim dividend Rs 2/- per share, record date 2-Nov-2026", implied_date: "on or before 21-Nov-2026", ref: "lines 42-49", status_word: "initiated"}
  - {commitment: "Capex Rs 450 Cr incl. Karnataka lamination consolidation", implied_date: "phased to FY 2030-31", ref: "lines 51-53, 441-445", status_word: "initiated"}
  - {commitment: "Post-proposed capacity 1,60,000 MT sheet metal, 13,14,000 machine hours", implied_date: "FY 2030-31", ref: "lines 436-439", status_word: "initiated"}
  - {commitment: "Machining expansion to 10,80,000 machine hours", implied_date: "Q1 2029-30", ref: "lines 424-425", status_word: "underway"}
  - {commitment: "Capex financing from internal accruals and debt, no split", implied_date: "with capex", ref: "line 447", status_word: "initiated"}
  - {commitment: "Amalgamation of PIPL and DFPL into PEL", implied_date: "effective 23-Sep-2026", ref: "lines 345-353", status_word: "completed"}
  - {commitment: "ESOP Grant 2, 5,77,500 options at Rs 736.72, PBO 25% at Year 2", implied_date: "first vest about Oct-2027; schedule to about Oct-2034", ref: "lines 55-57, 515-556", status_word: "initiated"}
  - {commitment: "Trust route: secondary purchase or fresh issue to Trust", implied_date: "undated", ref: "lines 509-512", status_word: "initiated"}
  - {commitment: "Agarwala to Deputy CEO; Sundaresh to COO M&G", implied_date: "22-Oct-2026", ref: "lines 59-69", status_word: "completed"}
  - {commitment: "Patil promoted to Deputy COO, joins SMP", implied_date: "22-Oct-2026", ref: "lines 71-74", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Restated standalone equals the former consolidated perimeter: Q1 FY27 restated revenue Rs 529.1 Cr matches Notion's Rs 529 Cr. The load-bearing forensic fact is cash. H1 CFO Rs 323.0 Cr rests on trade payables up Rs 231.5 Cr while inventory rose Rs 83.8 Cr. Computed net debt (borrowings less cash, other bank balances, current investments) is Rs 538.7 Cr against the Rs 491 Cr tracker line, and Rs 552.1 Cr at Mar-26 on the same basis. If the payables are LC acceptances (pending operator ruling), debt-like net debt is higher. Q2 PBT rose Rs 9.0 Cr QoQ while finance cost fell Rs 6.3 Cr as CWIP more than doubled; capitalised interest may explain most of the rise. Q2 ETR 25.1% hides a 27.1% rate before the earlier-years credit. After the merger, the former subsidiaries' profit (41.6% of old-PEL PAT in Q1 FY27) cannot be separated. Outside India revenue Rs 154.3 Cr breaks the Rs 135-139 Cr plateau, but it is total exports, not railway only. Castings volume and SGST status: NOT FOUND in this filing. No prior-quarter fulltext was passed, so F5/F15 rest on Note 4 only."
```
