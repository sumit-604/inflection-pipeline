# Verifier summary, KABRAEXTRU, run 2026-09-05, rework coverage rerun 2026-09-09 (phase 1)

## Rerun confidence delta, with the run 1 comparison

| Component | Run 1 | Rerun | Verifier | Model | Rerun basis |
|---|---|---|---|---|---|
| Numerical acceptance | 93.3 | 95.6 | B12a | claude-haiku-4-5 | Combined: run 1, 45 figures at 93.3 with 3 MINOR traceability items since closed; targeted rerun, 23 figures at 100 with 0 findings. 65 of 68 clean. 0 MISMATCH and 0 ANCHOR NOT FOUND in either pass |
| Red flag coverage | 23.0 | 46.0 | B12b | claude-opus-4-8 | 52 independent flags found, 24 caught, 7 partially caught, 21 missed; 1 CRITICAL, 13 MAJOR, 16 MINOR; 9 pipeline flags not supported or overstated; credibility grade D concurred. Run 1: 30 found, 7 caught |
| Framework adherence | 93.8 | 97.0 | B12c | claude-opus-4-8 | Phase 1 scope only: 66 Gate 0 rules and 49 Emerging Moat rules; 0 CRITICAL, 0 MAJOR, 3 MINOR; valuation half deferred to phase 3 |
| Peer utilisation | 83.0 | 100.0 | B12d | claude-sonnet-5 | 6 peers audited, 5 substantive confirmed, 0 CRITICAL, 1 MAJOR since corrected, 7 MINOR |
| **Overall** | **23.0** | **46.0** | min of four | | Band: FORCED REWORK (below 60) |

Rework triggers recorded: any verifier acceptance below 60 is true (B12b at 46.0); B12a CRITICAL is false; overall below 60 is true.

Scope notes. Verifier A's rerun pass audited 23 high materiality figures across the rework addendum materials: stage 2 ranks 2 and 5, stage 3 sections A1 to A4, stage 5 items 1 to 4 and its rerun delta, and stage 6's rerun delta items on the Windsor screening file. Sources opened: Annual Report FY2025-26, Annual Report FY2024-25, WINDMACHIN-Data_Sheet.csv. It returned zero findings; all 23 rows are recorded CLEAN and carry source_fidelity true as verifications, not as findings. Verifier C's rerun covered Gate 0 and Emerging Moat only; valuation adherence and the Business Understanding Narrative remain pending phase 3, recorded as scope, not defect.

Verifier D's single MAJOR was corrected in stage 6 after the audit. Claim 10 was relabelled from VERIFIED to PARTIALLY VERIFIED on 2026-09-09, commit 1afcb56, because all three of its anchors are single peer. The B12d block records the pre correction state. Three of verifier D's MINOR page anchors were corrected in the same commit.

---

## CRITICAL (1)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 1 | B12b | Stage 5 sections 1A, 2A, 2D, 4D (absent); source AR FY25 Note 38 p.104, MD&A p.38, chairman p.4; AR FY26 p.4-5 | MISSED: Battery Division revenue fell 52.3 percent FY24 to FY25, Rs 26,616.45 lakh to Rs 12,698.12 lakh, and the segment result swung from plus Rs 651.55 lakh to minus Rs 2,553.28 lakh. Two consecutive annual reports are silent, and the FY25 report calls Geon "gaining traction from EV OEMs" in the same document. A repeated omission across two reporting periods on the division the transition thesis rests on. |

---

## MAJOR (13 rows listed, 14 recorded across the blocks)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 2 | B12b | Stage 5 section 2A row 2 and stage 6 claim 3 arithmetic; source AR FY26 Note 38 p.105 against P&L p.67 and Note 23 p.95; AR FY25 Note 38 p.104 | MISSED: the FY26 Note 38 changed the segment revenue basis, FY25 comparative Rs 48,983.14 lakh including other income against FY26 Rs 45,099.83 lakh excluding Rs 2,367.55 lakh of it, with no disclosure and no restatement. The 13.2 percent extrusion decline and the 7.2 percent battery growth used by both stages are not like for like. |
| 3 | B12b | Stage 5 (absent); source AR FY26 p.95, p.67, p.17; AR FY25 p.19 | MISSED: the FY26 Note 28 carries FY2023-24 depreciation of Rs 1,557.18 lakh in the FY2024-25 comparative column against Rs 2,027.04 lakh on the face of the same report's profit and loss statement and Directors' Report. Gap Rs 469.86 lakh, 23.2 percent. Verified from the PDF page image. |
| 4 | B12b | Stage 5 flag RECEIVABLES_AGEING_VS_TURNOVER_FRAMING; source AR FY26 Note 9 p.87-88 | PARTIALLY CAUGHT: the ageing arithmetic is right, but the Hero Electric exposure is never set against the provision. Rs 3,039 lakh due from a customer in insolvency against Rs 1,053.44 lakh of allowance for the entire Rs 9,052.43 lakh book. |
| 5 | B12b | Stage 5 flag VAROS_KEY_STRENGTH_COLLAPSE; source AR FY26 Note 39(iii)(iv) p.109, Note 3 p.86, AOC-1 p.23 | MISSED element: a further Rs 318.00 lakh of compulsorily convertible debentures went into Varos during FY26, Rs 934.25 lakh to Rs 1,252.25 lakh, with the Rs 80 lakh equity still at cost, against negative net worth of Rs 556.17 lakh and a 95 percent turnover fall, and no impairment discussion. |
| 6 | B12b | Stage 5 flag MATERIAL_CHANGES_STATEMENT_VS_DOWNGRADE_DATE; source AR FY25 p.22 and p.49 | PARTIALLY CAUGHT: stage 5 flags the FY26 instance only. The identical defect occurred in FY25, item 14 signed 16-May-2025 against the 5-Apr-2025 downgrade. A two year repeat, not a one off. |
| 7 | B12b | Stage 5 section 1C and flag PENTA_JV_PILLAR_DROPPED_SILENTLY; source AR FY25 p.37; AR FY26 p.36-37 | MISSED: the entire Technical Collaboration Key Strength left the FY26 report without comment, including the Battenfeld-Cincinnati tie up "since 1983". Stage 5 instead reports Penta leaving a table Penta was never in. |
| 8 | B12b | Stage 5 section 3B, EV sales bullet; source AR FY25 p.36 against AR FY26 p.35 | NOT SUPPORTED: stage 5 calls the FADA data "internally consistent and independently checkable". Every FY25 figure was restated between the two reports with no note, and the FY25 report's own table and prose differ. |
| 9 | B12b | Stage 6 claim 5, part 4, part 5; source RAJOOENG 22-Oct-2024 p.10 against p.12 | OVERSTATED: "73-74% of H1 FY25 revenue" is the quarterly export share; the same speaker gives 50 to 52 percent for the half year on the preceding page. The part 5 hypothesis pairs a quarterly export share with a half year margin. |
| 10 | B12b | Stage 6 claim 1, parts 2A, 2C, 3; source WINDMACHIN-Data_Sheet.csv rows 11, 22, 50, 57 | OVERSTATED: Windsor's FY26 sales rise is presented as corroboration of a non contracting peer set while the same file shows operating cash flow of minus Rs 59.09 Cr and inventory doubling from Rs 104.75 Cr to Rs 212.20 Cr. Rows 57 and 50 omitted beside rows 58 and 59 that were cited. |
| 11 | B12b | Stage 6 claims 1, 5, 6 and part 2A; source RAJOOENG 16-May-2023 p.4; 18-Apr-2024 p.8; 22-Oct-2024 p.6 and p.13 | MISSED: Rajoo walked back its growth guidance from 15 to 17 percent, to 17 to 20 percent, to 12 to 15 percent across the same three calls stage 6 uses to argue an accelerating industry. |
| 12 | B12b | Stage 6 claims 1, 5, 6 and part 2A; source RAJOOENG 18-Apr-2024 p.5, p.8, p.13, p.16; 6-Nov-2023 p.8 | MISSED: Rajoo Q4 FY24 revenue fell 26.26 percent on customer payment and lifting delays, order book fell from Rs 185 Cr to Rs 140 Cr, and Q4 FY24 export share was 30 percent against 45 percent for the full year. Stage 6 presents only the rising series. |
| 13 | B12b | Stage 6 claims 7, 8, part 2E, part 5; source HBLENGINE AGM 25-Sep-2025 p.17; AR FY26 p.36-37 and p.38 | PARTIALLY CAUGHT: HBL says telecom operators are switching to lithium and "there is no margin in it. So we are not participating". Geon names telecom storage as a growth vector. Stage 6 uses the quote as generic commoditisation context and leaves all battery claims UNVERIFIABLE. |
| 14 | B12d | Stage 6 claim 10 verdict, report and block; source RAJOOENG Q2 FY24, 6-Nov-2023, PDF p.10, p.11, p.12 | Claimed VERIFIED on a single peer with all three anchors from that one peer. Verifier D rule 4 makes a single peer VERIFIED a MAJOR; the verdict should be PARTIALLY VERIFIED. Corrected in stage 6 on 2026-09-09, commit 1afcb56. source_fidelity: false. |

Count reconciliation. Block B12b records major_count 13. Its findings list enumerates 12 MAJOR rows, shown above as rows 2 to 13. The one row gap between the recorded count and the enumerated list is not reconciled inside the block. Row 14 is verifier D's single MAJOR. Recorded total across blocks: 14. Rows listed here: 13.

---

## MINOR (28 rows listed, 26 recorded across the blocks)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 15 | B12b | Stage 5 section 2A row 1 and the promise delivery row 1; source AR FY26 p.37 Key Strength 7 and p.36; AR FY25 p.38 and p.5 | Outcome wrong: the FY26 report does name four wheelers, at Key Strength 7 and in the company overview. Only the electric light commercial vehicle segment is absent. The promise anchor "p.36/38" is half wrong; the promise is at p.38 and p.5. |
| 16 | B12b | Stage 5 section 2A row 3 and promise delivery row 3; source AR FY25 p.38 | Mis anchored: "well-positioned to capitalize on anticipated growth" is at AR FY25 p.38, Business Outlook, not p.37. All outcome legs verify. |
| 17 | B12b | Stage 5 flag INVENTORY_TURNOVER_REASON_COPIED_VERBATIM; source AR FY26 Note 43(e) p.112 | OVERSTATED: the ratio uses average inventory, which rose about 8.9 percent from Rs 26,432 lakh to Rs 28,776 lakh, so the stated reason is not contradicted. The verbatim copy point and the below threshold reason point stand. |
| 18 | B12b | Stage 5 flag HERITAGE_CLAIM_SHRUNK_AND_CONTRADICTED; source AR FY26 p.72 | OVERSTATED: "more than 15,000 installations" and "over 6 decades", correctly attributed to the Kolsite Group, survive in the FY26 corporate overview note. The letter against management discussion contradiction stands. |
| 19 | B12b | Stage 5 flag PENTA_JV_PILLAR_DROPPED_SILENTLY; source AR FY26 Note 39 p.106; AR FY25 p.37 | OVERSTATED: the FY26 Note 39 discloses the Penta cessation by name and date, and the FY25 collaboration table never listed Penta. The 49.94 percent against "50:50" element stands. |
| 20 | B12b | Stage 5 sections 2B and 2C; source AR FY26 p.51 | OVERSTATED on timing: the 13-May-2026 downgrade falls after the 31-March-2026 year end and moves the long term rating one notch. The two notch sequence A+ to A to A- spans FY25 and FY26. Stage 5's own 4D row states it correctly. |
| 21 | B12b | Stage 5 (absent); source AR FY26 p.87-88 | MISSED: the Note 9 ageing table leaves every "significant increase in credit risk" row blank and classifies Rs 9,031.04 lakh as considered good, contradicting the balance sheet split of Rs 7,998.99 lakh good plus Rs 1,053.44 lakh printed just above it. |
| 22 | B12b | Stage 5 (absent); source AR FY26 p.19 item 10(ii) against p.17 item 2; Note 44 p.112, p.17 item 3, Notice p.6 | MISSED: the Directors' Responsibility Statement certifies a true and fair view "of the profit of the Company" in a year the same report prints a loss of Rs 244.28 lakh; and Note 44 recommends a Rs 0.00 dividend "subject to the approval of Shareholders" against item 3 and an AGM notice with no dividend resolution. |
| 23 | B12b | Stage 5 (absent); source AR FY26 p.17 against p.67 and p.95 | MISSED: the Directors' Report prints standalone FY26 cost of material consumed as Rs 28,966.45 lakh where the profit and loss statement and Note 24 say Rs 28,996.45 lakh, and the table's own total of Rs 47,866.47 lakh only foots at the higher figure. PDF image verified. |
| 24 | B12b | Stage 5 flag KMP_CHURN_UNDISCLOSED_NARRATIVELY; source AR FY26 p.3 and p.30; AR FY25 p.3 | PARTIALLY CAUGHT: the FY26 accounts, AOC-1 and notes are signed by "Uttam Singh, Interim Chief Financial Officer", a name absent from Corporate Information and Annexure-5. Annexure-5 lists Mr Atanu Maity as CEO for FY26 with no resignation footnote although the FY25 report disclosed his exit with effect from 16-May-2025. |
| 25 | B12b | Stage 5 (absent); source AR FY25 p.49 against AR FY26 p.51; AR FY25 p.31 and p.105; AR FY25 p.5 against p.35 | MISSED: cross report and cross section figure gaps. The two reports date the same CRISIL action oppositely. FY25 export revenue is Rs 6,420.67 lakh in Annexure-4 and Rs 6,507.94 lakh in Note 38. The FY25 report gives 2023 and 2024 as base years for the same USD 2.22 bn EV battery figure. |
| 26 | B12b | Stage 5 section 3B, extrusion machinery bullet; source AR FY25 p.34 | MISSED: the FY25 report's own figures do not compute. USD 6.9 bn at 3.9 percent reaches USD 8.7 bn, not USD 10 bn; USD 10 bn to USD 12 bn over five years is 3.7 percent, not 4.7 percent. Stage 5 compares the two years' growth rates but never tests either internally. The FY26 equivalent paragraph does compute. |
| 27 | B12b | Stage 6 claim 10, part 2E(vi), part 4; source RAJOOENG 18-Apr-2024 p.7; 6-Nov-2023 p.10 and p.11 | PARTIALLY CAUGHT and OVERSTATED: Rajoo's own net working capital cycle stretched to 165 days with inventory days about 130 to about 190, and the same officer gives "35% to 40% advance" and "we normally receive 50% advance" in one call. Stage 6's benchmark uses only the favourable figures. |
| 28 | B12b | Stage 6 claims 7 and 8, part 5; source HBLENGINE AGM 25-Sep-2025 p.4 | OVERSTATED: HBL's "we will make a profit from year one" is a forward budget statement made before the roughly Rs 200 Cr investment is complete, presented by stage 6 as a realised outcome. |
| 29 | B12b | Stage 6 claim 6; source RAJOOENG 22-Oct-2024 p.6 and p.15 | OVERSTATED: the roughly 30 percent capacity addition was partly still "under installation" at October 2024. |
| 30 | B12b | Stage 6 claim 5, claim 6, part 2E(i); source RAJOOENG 16-May-2023 p.4 and p.12; 6-Nov-2023 p.4 and p.6; 18-Apr-2024 p.7 | Residual page anchor defects: the FY23 35 percent export share is at p.4 and p.12, not p.11; the Rajkot three plots capacity statement is at p.4 and p.6, not p.5; the Red Sea working capital exchange is at p.7, not p.6-7. All seven anchors the stage 6 rerun says it corrected resolve correctly, as do all three claim 10 quotes. |
| 31 | B12b | Stage 6 missed item; source RAJOOENG 18-Apr-2024 p.9; 22-Oct-2024 p.15 | MISSED: Rajoo's pipeline to order conversion estimate fell from "1:5", about 20 percent, to "8% to 9%". Stage 6 cites the Rs 1,000 Cr pipeline as demand evidence without it, which implies about Rs 85 Cr of expected orders at the later rate. Recorded in the missed list, not in the findings list. |
| 32 | B12b | Stage 6 missed item; source HBLENGINE AGM 25-Sep-2025 p.1-2 | MISSED: HBL volunteers that FY25 sales were flat to mildly declining as its own prior cover had shown, and refuses to call its Rs 3,000 Cr number guidance, saying "Budgeting is the word, I am not forecasting". A governance contrast with the company's undated claims that stage 6 does not draw. Recorded in the missed list, not in the findings list. |
| 33 | B12c | 01-gate0.md, DECISION LINE, final sentence; rule prompts/01-gate-0-pipeline.md operating rule 2 | The decision line recommends a run level REWORK or INSUFFICIENT EVIDENCE posture, which is orchestrator vocabulary, not a Gate 0 output. Recomputed: no change. Classification AVOID stands; core 22 of 100 re derived identical. |
| 34 | B12c | 01-gate0.md FORMULA NOTES "Capital Employed"; propagates to A1, A2, A4, M3 and deal breaker 3; rule FORMULA DEFINITIONS, ROCE | Net Worth plus Borrowings substituted for Total Assets less Current Liabilities under a "do not substitute" instruction; cross validated to Note 43 for FY25 and FY26 only, eight years unchecked. Recomputed: literal basis median ROCE NOT FOUND, not computable from the stated inputs. Proxy median 10.31 percent gives A1 = 1. Bounded effect: M3 could move 0 to 1 and moat score 3 to 4; moat class stays NONE, core 22 and AVOID unchanged, deal breaker 3 stays unfired. |
| 35 | B12c | 07-emoat.md lines 13-15 taxonomy framing paragraph, section 3 H2, section 6A bullet 1; rule prompts/07-emerging-moat-pipeline.md operating rule 2 | The fourth "media-reported" evidence tier survives in the report body after the 2026-09-09 addendum closed the item at block level only. The addendum named these three locations and did not align them. Recomputed: em_score 9 unchanged; the item carries no scoring weight. Block level catalysts and optionality register are correct. |
| 36 | B12d | Stage 6 claim 5, the "73-74% of H1 FY25 revenue" composite figure; source RAJOOENG Q2 FY25 PDF p.10 and p.12 | Cited PDF p.12 for both 73 percent and 74 percent. The 74 percent is stated on p.10, a different, quarterly only exchange; 73 percent and its quote are correctly on p.12. Corrected 2026-09-09. source_fidelity: false. |
| 37 | B12d | Stage 6 claim 6, facility inauguration anchor; source RAJOOENG Q4 FY24 PDF p.3 | Cited PDF p.2-3. The quote is located entirely on p.3; p.2 does not contain it. Corrected 2026-09-09. source_fidelity: false. |
| 38 | B12d | Stage 6 claim 4 and part 2E(i), Red Sea shipping crisis anchor; source RAJOOENG Q4 FY24 PDF p.7 | Cited PDF p.6-7. The quoted material is located entirely on p.7. Corrected 2026-09-09. source_fidelity: false. |
| 39 | B12d | Stage 6 "Sources Re-Read" page count metadata for the Nov-2023 and Apr-2024 transcripts | Claimed 11pp and 15pp. Actual PDF page marker counts run one higher, 12pp and 16pp; an internal footer against total PDF page counting convention difference. No anchor affected. Corrected 2026-09-09. source_fidelity: false. |
| 40 | B12d | Unused but relevant, WINDMACHIN-Data_Sheet.csv row 57, columns 2025-03-31 and 2026-03-31 | Cash from Operating Activity sharply negative and worsening, minus Rs 2.4 Cr in FY25 and minus Rs 59.09 Cr in FY26, despite the plus 72.9 percent FY26 sales growth cited as a corroborating signal in claims 1 and 6. Added to stage 6 as qualifying context on 2026-09-09. |
| 41 | B12d | Unused but relevant, WINDMACHIN-Data_Sheet.csv row 41, columns 2025-03-31 and 2026-03-31 | Borrowings rose from Rs 34.86 Cr in FY25 to Rs 86.04 Cr in FY26, up 147 percent, a financing mix data point for the claim 6 organic against inorganic capex question. Added to stage 6 as qualifying context on 2026-09-09. |
| 42 | B12d | Unused but relevant, RAJOOENG Q2 FY25, 22-Oct-2024, PDF p.8-9 | Second, later corroboration of the order linked advance working capital model, "these are the advance against order booking", regarding the Rs 127 Cr reserve and surplus. Duplicative of claim 10's existing claim anchors, so immaterial to the verdict. |

Count reconciliation. Block B12b records minor_count 16, which are rows 15 to 30. Rows 31 and 32 are MINOR items recorded in that block's missed list but not carried into its findings list; they are shown here because they carry a severity and an anchor. Block B12c records 3, rows 33 to 35. Block B12d records minor_count 7, which are its 4 findings rows, 36 to 39, plus its 3 unused but relevant rows, 40 to 42. Recorded total across blocks: 26. Rows listed here: 28.

---

## Verifier B pipeline flags recorded NOT SUPPORTED or OVERSTATED (9)

| # | Assessment | Severity | Pipeline flag | Verifier B evidence and anchor |
|---|---|---|---|---|
| 1 | NOT SUPPORTED | MAJOR | Stage 5 section 3B: "EV sales data (FADA, both years): internally consistent and independently checkable" | Every FY25 line restated between the reports with no note: total 19,64,975 to 19,67,397, E-2W 11,49,422 to 11,50,790, E-3W 6,99,063 to 6,98,914, E-4W 1,07,645 to 1,08,873, E-CV 8,844 to 8,820. AR FY25 p.36 against AR FY26 p.35 |
| 2 | OVERSTATED | MAJOR | Stage 6 claim 5, part 4, part 5: "export share ... to 73-74% of H1 FY25 revenue" | 74 percent is the quarterly figure; "if we talk about the total half year, then around 50%-52% is from the export market". The like for like half year series is 35 percent to 45 percent to 50 to 52 percent. RAJOOENG 22-Oct-2024 p.10 |
| 3 | OVERSTATED | MAJOR | Stage 6 claim 1, part 3: Windsor corroborates that a second domestic competitor "was not contracting through FY26" | Row 57 operating cash minus 2.40 in FY25 and minus 59.09 in FY26; row 50 inventory 104.75 to 212.20; row 22 profit before tax still minus 1.31 in FY26. WINDMACHIN-Data_Sheet.csv |
| 4 | OVERSTATED | MINOR | Stage 5 flag PENTA_JV_PILLAR_DROPPED_SILENTLY | The FY25 collaboration table lists only Battenfeld-Cincinnati and Extron Mecanor, never Penta; AR FY26 Note 39 p.106 discloses the cessation by name and date. The 49.94 percent against "50:50" element stands |
| 5 | OVERSTATED | MINOR | Stage 5 flag INVENTORY_TURNOVER_REASON_COPIED_VERBATIM, the "underlying direction reversed" element | Note 43(e) defines the ratio on average inventory, which rose about 8.9 percent. AR FY26 p.112 |
| 6 | OVERSTATED | MINOR | Stage 5 flag HERITAGE_CLAIM_SHRUNK_AND_CONTRADICTED, the "installation count dropped entirely" element | AR FY26 p.72 retains "more than 15,000 installations" and "over 6 decades of experience" |
| 7 | OVERSTATED | MINOR | Stage 5 sections 2B and 2C: "the CRISIL two-step downgrade during FY26" | The action is with effect from 13-May-2026, after the 31-March-2026 year end, and moves the long term rating one notch. AR FY26 p.51 |
| 8 | OVERSTATED | MINOR | Stage 6 claims 7 and 8, part 5: HBL "profitable from year one" on about Rs 200 Cr, presented as a realised outcome | "by the time this fiscal year ends, we would have invested perhaps 200 crores or less. And we will make a profit from year one". Forward budget statement. HBLENGINE AGM 25-Sep-2025 p.4 |
| 9 | OVERSTATED | MINOR | Stage 6 claim 6: "a further ~30% capacity addition completed by Oct-2024" | "we are also further investing in the tooling and machining center" and "which we have installed and which is under installation at this point of time". RAJOOENG 22-Oct-2024 p.6 and p.15 |

These nine overlap the findings tables above; they are the same verifier B positions recorded in a separate block field.

---

## Counts

| Verifier | CRITICAL | MAJOR | MINOR | Acceptance (rerun) | Acceptance (run 1) |
|---|---|---|---|---|---|
| B12a numerical | 0 | 0 | 0 | 100 on 23 figures; 95.6 combined | 93.3 on 45 figures |
| B12b red flags | 1 | 13 | 16 | 46.0 | 23.0 |
| B12c framework (Gate 0 and Emerging Moat only) | 0 | 0 | 3 | 97.0 | 93.8 |
| B12d peers | 0 | 1 | 7 | 100.0 | 83.0 |
| **Total recorded** | **1** | **14** | **26** | overall 46.0 | overall 23.0 |
| **Total rows listed above** | **1** | **13** | **28** | | |

Other verifier positions recorded without a severity row. Verifier B concurs with credibility grade D and states it would grade lower if the scale allowed, citing the unnarrated 52.3 percent battery revenue collapse against a same document "gaining traction" claim, the wrong year depreciation comparative, the undisclosed segment revenue basis change, a Rs 3,039 lakh insolvent customer receivable against Rs 1,053.44 lakh of allowance for the whole book, and a two year repeat of the "no material changes" defect. Verifier B spot checked 5 promise delivery rows and confirmed 4, with 1 wrong. Verifier D found all claims addressed. Verifier A's rerun coverage note records that every number examined that was anchored to a corpus document was found verbatim on the cited page, with two rounding tolerances noted as immaterial and not counted as mismatches.

Verifier disagreement log: none this run (no B12a source-fidelity MISMATCH or ANCHOR NOT FOUND in either pass)
