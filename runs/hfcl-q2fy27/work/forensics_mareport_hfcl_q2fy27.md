# A3 FORENSIC NOTES: HFCL Q2 FY27, doctype presentation (one-off disclosure, doctag mareport: CARE Monitoring Agency Reports, QIP Rs 550 Cr and Preferential Warrants Rs 555 Cr)

Inputs read: A1 structured (runs/hfcl-q2fy27/extracted/hfcl-mareport-q2fy27-structured.md, R001-R411), A1 fulltext (runs/hfcl-q2fy27/extracted/hfcl-mareport-q2fy27-fulltext.md, lines 1-1282 incl. image transcriptions 1238-1282), A2 ledger (runs/hfcl-q2fy27/work/ledger_mareport_hfcl_q2fy27.md), Notion brief sections 4, 7, 8 (runs/hfcl-q2fy27/work/notion-brief.md; memory, not evidence). Prior-quarter fulltext: none supplied. Source PDF and inputs/ not opened.

## LEDGER RECONCILIATION
- Ledger rows: 411 (R001-R411). Rows read in structured file and at cited fulltext line: 411. Reconciled 100%.
- Superseded rows (10) read together with superseding rows: R138->R391, R148->R393, R149->R394, R150->R395, R294->R396, R299->R399, R303->R402, R304->R409, R306->R408, R314->R405. Values taken from the superseding (image-verified) rows.
- ZERO_STANDING: 45 ledger-flagged rows (31 A1 + 14 A2-added) all read; treated under F1.
- Arithmetic re-checked: QIP objects 35+50+105+260+93+7 = 550.00; opening 513.72 + Q2 11.95 = 525.67; unutilised 24.27 (R&D) + 0.06 (issue exp.) = 24.33; deployment 3.31+10.00+10.30+0.92 = 24.53 = 24.33 + 0.20 FDR interest (L503). QIP price 8,79,29,651 x Rs62.55 = ~Rs550.00 Cr; discount 3.29/65.84 = 5.0%. Preferential 7,50,00,000 x Rs74 = Rs555.00 Cr; 25% = Rs18.50 x 7.5 Cr = Rs138.75 Cr; balance Rs416.25 Cr = Rs55.50 per warrant. Objects 175+50+90+140+100 = 555.00. Received 138.75 - used 48.75 = 90.00 unutilised = FD 90.00 (L1066-1067). Unfunded objects: 175 + 50 + (140-48.75) + 100 = 416.25 = warrant balance.
- Line-alignment caveat: page 10 (QIP delay table) was not image-rendered (rendered pages 6-9, 16, 19, 20, 22). The R&D delay cell reading in R197 ("No Delays") is A1's alignment of a multi-column text layer; L510-512 shows one "No Delays" and one "Refer Note 1". See FN-08.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | R253, R254, R352, R353, R354, R355, R357, R363, R373 | L1105-1108, L1282, L1119-1146, L1166 | "Yes, Not Ascertainab le*" (L1282: "Yes, Not Ascertainable*"); "The Company expects to deploy the said proceeds upon completion of the relevant conditions precedent and consummation of the proposed transactions" (reassembled from column text L1119-1146) | FORWARD-SIGNAL | The Rs90 Cr HASPL equity object missed its 30-Sep-2026 deadline with zero use. Deployment is tied to unresolved conditions precedent for the defence consolidation (Board approvals 25-Mar-2026 and 02-Jun-2026, L1115-1117). The consolidation had not closed at quarter end. The revised 31-Dec-2026 date has no stated slack. A second miss is the observation that separates "timing" from "deal in trouble". Ask: which conditions precedent are open, who controls them, and what happens to the Rs90 Cr if the transaction lapses. |
| FN-02 | F13 | R258, R259, R260, R261, R263, R358, R360, R240, R061 | L716-726, L743-745, L747, L684-688 | "vide a resolution passed through circulation on September 25, 2026, approved the extension of the timeline for utilisation of the unutilised amount of ₹90 crore"; shareholder approval: "Not applicable" (L747); "These sections have not been reviewed by the MA" (L687-688) | AMBIGUOUS | The board extended an object deadline by circular resolution five days before the deadline, not at a meeting, and no shareholder approval was sought. The delay reason sits in the "Comments of the Board of Directors" column, which the MA states it did not review. The reason is therefore management-authored, not MA-verified. Ask: why circulation, and does a timeline variation on a preferential-issue object need shareholder approval or an audit committee deviation statement. |
| FN-03 | F1 | R252, R294/R396-R398, R299/R399-R401, R303/R402-R404, R314/R405-R407, R309, R319, R330, R331, R326, R333, R344, R350, R353, R367, R371, R381, R384 | L1056-1060, L1272-1278 | "No amount of the issue was received in Q2FY27." (L1058); "subject to receipt of balance amount of Rs 416.25 crore." (L1060) | FORWARD-SIGNAL | The zero-standing rows anticipate one transaction class: promoter warrant conversion receipts. Rs416.25 Cr of objects (preform Rs175, defence facility Rs50, working capital balance Rs91.25, GCP Rs100) has no cash behind it until conversion. The first dated drawdown, defence facility Rs15.00 Cr by 30-Sep-2027 (L1088-1089), falls before the conversion window end (~25-Nov-2027, computed). Conversion timing therefore sets capex timing. |
| FN-04 | F10 | R027, R028, R029, R034, R035, R036, R245, R247, R327, R328, R329 | L44-50, L1056-1058 | "7,50,00,000 Warrants to persons belonging to the Promoter/Promoter Group category at an issue price of ₹74/-" (L45-46); "Allottee has 18 months from the date of allotment of warrants (25.05.2026) for conversion into equity shares." (L1056-1058) | FORWARD-SIGNAL | 7.5 Cr dilutive warrants are outstanding. Rs55.50 per warrant (Rs416.25 Cr) is due on conversion by ~25-Nov-2027 (computed from stated terms). No receipt occurred in Q2. A4: cross-check basic vs diluted EPS in the Q2 results against this instrument (Notion Q1 FY27 Q9 flagged diluted = basic). Memory correction: Notion promise log carries the balance as ~Rs412.5 Cr; the filed figure is Rs416.25 Cr. |
| FN-05 | F7 | R087, R088, R089, R141, R142, R143, R071 | L230-236, L1253, L179 | "During the previous quarter, the company transferred the issue proceeds from the monitoring account into its CC account." (L230); "there has been comingling of funds (where issue proceeds were mixed with other cash flows), which restricted our ability to directly ascertain them." (L234) | AMBIGUOUS | The MA's verification of QIP R&D spend rests on a Management Certificate and CA certificate, not on bank-trail evidence. The amount moved to the CC account in Q1 FY27 is not stated. Q2 shows Rs8.44 Cr routed via the CC account. If the Q1 transfer exceeded Rs8.44 Cr, the excess is either inside "utilised" or commingled and unreported, because the deployment table (L491-504) holds all unutilised cash in the monitoring account and FDRs. Section 3 still answers utilisation "as per the disclosures in the Offer Document? Yes" (L179). Ask: amount transferred to CC account in Q1, and whether any proceeds remain in it. Lean bear: a cash credit account receipt reduces working-capital borrowing until spent. |
| FN-06 | F7 | R137, R195, R209, R210, R211, R212, R213, R214 | L563-570, L382, L396-402 | "Rs 50.00 crore which has to be completed by FY27" (L563); "If the Net Proceeds are not utilized (in full or in part) for the Objects for the period stated above due to any reason ... the remaining Net Proceeds shall be utilized (in part or full) in subsequent periods" (L567-569) | FORWARD-SIGNAL | Rs24.27 Cr R&D remains for H2 FY27, which needs ~Rs12.1 Cr a quarter. Q2 ran Rs10.98 Cr; the two quarters before ran ~Rs7.4 Cr a quarter (14.75 cumulative). The MA placed the placement-document carry-forward clause directly under the FY27 deadline. That is pre-emptive cover for an R&D slip. The board gave "No comments received" on reasons for idle funds (L396-402). A FY27 miss would be a second object-timeline slip across the two issues. |
| FN-07 | F6 | R102, R115, R139, R140 | L248, L1253 | object: "Funding expenditure towards Research and Development initiatives including acquisition of technologies" (L248); use: "expensed Rs. 10.98 crore towards manpower costs for employees engaged in R&D activities" (L1253) | AMBIGUOUS | All Q2 R&D use was R&D payroll; none went to technology acquisition. Proceeds are funding a recurring cost. When the Rs50 Cr is exhausted, R&D payroll returns to operating cash flow. Ask: is the payroll expensed or capitalised (intangibles under development), and was any technology acquisition (for example preform or defence know-how) planned under this object. |
| FN-08 | F14 | R096, R098, R105, R196, R197 | L248-249, L510-512, L520-525 | "Rs. 15.00 crores by Fiscal 2026" (L248); "Rs. 14.75 crores were incurred till Q1FY27" (L248); delay column: "No Delays ... Refer Note 1" (L510-512) | AMBIGUOUS | The offer document set Rs15.00 Cr R&D by FY26. Cumulative use was only Rs14.75 Cr by end Q1 FY27, so the FY26 tranche was missed by at least Rs0.25 Cr. The A1 reading of the R&D delay cell is "No Delays" (R197). The text layer on p10 is not image-verified and may read "Refer Note 1". Immaterial in rupees. It is a governance data point on how slips are labelled. |
| FN-09 | F14 | R170, R172-R190 | L491-504 | "Earning ... NA" for every row (L491-499) vs "(includes interest earned on FDRs INR 0.20 Crore) is parked in the form of FDR’s as partial margin for letter of credit" (L503); "10.30 October 09, 2026 NA 4.75%" (L497) | AMBIGUOUS | Three points. (1) The table says Earning NA; the footnote shows Rs0.20 Cr interest earned. (2) Rs21.22 Cr of unutilised QIP proceeds, which belong to the R&D object, is lien-marked as LC margin. These funds back the company's trade finance and are not free cash. (3) The Rs10.30 Cr FD matured 09-Oct-2026, ten days before the report date, and its post-maturity status is not stated. Lean bear: pledging issue proceeds as LC margin fits working-capital stress (Notion memory: FY26 CFO minus Rs378 Cr, cash conversion INDETERMINATE). Ask: which LCs, for what imports, and was the Rs10.30 Cr rolled into a deposit or spent. |
| FN-10 | F14 | R234, R250, R251, R256, R265, R268, R273-R275 | L665, L716-726, L753-756, L765-766, L773-776 | "(a) Deviation from the objects: Nil" (L665); "Whether all utilization is as per the disclosures in the Offer No" (L716); viability events: "No" (L765) | AMBIGUOUS | The headline says no deviation. The body says utilisation is NOT as per the offer document. The material-deviation definition covers objects and amounts, not timing (L775-776), so a timeline slip never reaches the headline. The "no unfavorable events affecting viability" answer comes from a Management Certificate (L756-757) while the deal's conditions precedent are unresolved. Reading rule for later quarters: read the delay table, not the deviation headline. Ask: did the audit committee receive a Reg 32 deviation or variation statement for the Rs90 Cr. |
| FN-11 | F14 | R110, R118, R155-R158, R204-R206, R215-R220 | L572-579, L456, L556 | "amount in the offer document: Nil" (L572); "Item Head^" (L574, no ^ definition in the QIP report); GCP row "93.00 93.00 - 93.00" (L456); "Completed in Q4FY26" (L556) | AMBIGUOUS | The QIP report says GCP in the offer document is "Nil", but the objects table carries a Rs93.00 Cr GCP object, fully used in Q4 FY26. No item-wise GCP use appears in this report. The "^" marker is undefined in the QIP report; the preferential report defines it (L1192), which suggests template carry-over. Ask for the Q4 FY26 MA report GCP item-wise table. 83% of QIP proceeds (Rs458 Cr: repayment 105, LTWC 260, GCP 93) went to fungible uses within one quarter. |
| FN-12 | F14 | R231, R241, R276, R315, R341, R362, R379, R387, R390, R321, R331, R332 | L659, L1230, L1052, L1060 | footer "3" on the preferential cover letter (L659) through "15" (L1230); "Rs. 506.25 crores out of which is subject to receipt" (L1060); total unutilised "90.00#" (L1052) | NEUTRAL-FACT | The preferential report pages are numbered 3-15, so pages 1-2 of that document are not in the filing, or the numbering runs from another document. The unutilised total shows two figures (90.00 actual; 506.25 including unreceived money) and one garbled sentence. Individually immaterial; cumulative drafting data point. |
| FN-13 | F6 | R277, R283, R293, R343, R344, R396-R398 | L796-812, L1085-1086, L1272 | "setting up of a preform manufacturing facility through our subsidiary namely HFCL Technologies Private Limited" (L805-808); "Entire amount by July 31, 2028" (L1085-1086) | AMBIGUOUS | Rs175 Cr of promoter warrant money is routed into a subsidiary, HFCL Technologies Pvt Ltd (HTL). The report does not state HTL's ownership. Notion memory flags "HTL minority holding and transfer-price UNVERIFIED" and links HTL to material RPTs. The captive-preform margin step (memory: EBITDA ~25-26% after captive preform) depends on this facility. The facility in turn depends on warrant conversion (FN-03). Ask: HTL shareholding, and the instrument (equity or loan) and terms for the Rs175 Cr. |
| FN-14 | F6 | R101, R124-R130, R192-R194 | L511, L1251 | "Completed in Q2FY27" (L511); "0.97 | 35.00 | 0.00" (L1251) | NEUTRAL-FACT | The QIP OFC capex object (Rs35 Cr) is fully used. This is a milestone confirmation that moves the status from underway to completed. The Rs35 Cr is small against the capacity programme (memory: ~Rs1,800 Cr on OF/OFC/preform lines). It does not confirm the Dec-2026 capacity date. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 45 zero rows read. Template lines for completed QIP objects are benign. Preferential zero rows await warrant conversion of Rs416.25 Cr (FN-03). |
| F2 Standalone vs consolidated | N.A. | MA report carries no P&L or S/C split. |
| F3 Shell-entity detection | N.A. | No cost lines. HASPL and HTL appear only as investee and facility vehicles. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters. The MA explicitly does not audit (L128-129). |
| F5 Going concern / EoM scope | N.A. | No auditor EoM in an MA report. Nearest analogue is the MA commingling qualifier (FN-05). No prior-quarter MA report was supplied, so the verbatim diff is not possible. A4 should obtain the Q1 FY27 MA reports to test whether Note 1 is new. |
| F6 Forward-commitment mining | FINDING | 14 dated object commitments registered below. HASPL object past deadline (FN-01). R&D object is payroll-only (FN-07). Preform via HTL (FN-13). OFC capex completed (FN-14). |
| F7 Hedge mining | FINDING | Carry-forward clause "due to any reason" placed under the R&D deadline (FN-06). Commingling qualifier "restricted our ability to directly ascertain" (FN-05). |
| F8 Tax forensics | N.A. | No tax lines. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | FINDING | QIP 8,79,29,651 shares at Rs62.55 ties to Rs550 Cr. 7.5 Cr promoter warrants are outstanding, Rs416.25 Cr unpaid, window to ~25-Nov-2027 (FN-04). |
| F11 Reserves / net worth tie-out | N.A. | No net worth figure in the document. Rs138.75 Cr warrant money received is a candidate reconciling item for A4's Q2 balance-sheet tie-out. |
| F12 Segment forensics | N.A. | No segment data. |
| F13 Board outcome beyond results | FINDING | Circular resolution 25-Sep-2026 extended the Rs90 Cr deadline to 31-Dec-2026 without shareholder approval. The reason is board-authored and not MA-reviewed (FN-02). Board approved the warrants and the defence consolidation on the same date, 25-Mar-2026 (L44, L1115). |
| F14 Note drafting inconsistencies | FINDING | Five items: R&D FY26 tranche vs "No Delays" (FN-08); Earning NA vs Rs0.20 Cr interest and LC margin (FN-09); deviation Nil vs utilisation "No" (FN-10); QIP GCP "Nil" vs Rs93 Cr and undefined "^" (FN-11); page numbering and garbled footnote (FN-12). |
| F15 Entity list diffs | N.A. | No consolidation list and no prior list. Entities named: HASPL, HTL, SBI deposit accounts. HTL ownership is carried as FN-13. |
| F16 Dropped / reframed disclosures | N.A. | Cross-deck comparison needs the prior MA report; prior-quarter path is "none". Within-document reframing is carried under F14. |
| F17 Silence audit | N.A. | Not a concall. Notion checklist touchpoints are mapped below for A4. |

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word (document word) |
|---|---|---|---|---|
| C1 | QIP OFC capex Rs35.00 Cr (Rs15 Cr FY26 + Rs20 Cr FY27) | FY27 | L242-246, L511 | completed ("Completed in Q2FY27") |
| C2 | QIP R&D Rs50.00 Cr; Rs25.73 Cr used, Rs24.27 Cr left | 31-Mar-2027 (FY27) | L563-565 | underway ("Ongoing") |
| C3 | QIP repayment/prepayment of borrowings Rs105.00 Cr | FY26 | L550 | completed ("Completed in Q4FY26") |
| C4 | QIP long-term working capital Rs260.00 Cr | FY26 | L553 | completed ("Completed in Q4FY26") |
| C5 | QIP GCP Rs93.00 Cr | FY26 | L556 | completed ("Completed in Q4FY26") |
| C6 | QIP issue expenses Rs7.00 Cr; Rs6.94 Cr used | undated | L559 | underway ("Ongoing") |
| C7 | Preferential: invest Rs90.00 Cr in HASPL equity | 30-Sep-2026 original; 31-Dec-2026 revised | L1107, L743-745, L1166-1167 | underway, delayed ("Ongoing, nil utilization"; "Yes, Not Ascertainable") |
| C8 | Deploy HASPL proceeds on completion of conditions precedent and consummation of defence consolidation | undated; bounded by 31-Dec-2026 | L1119-1146 | underway ("expects to deploy") |
| C9 | Preferential: preform facility via HTL Rs175.00 Cr | 31-Jul-2028 | L1085-1086 | initiated ("Ongoing, nil utilization") |
| C10 | Preferential: defence manufacturing facility Rs15.00 Cr | 30-Sep-2027 | L1088-1089 | initiated ("Ongoing, nil utilization") |
| C11 | Preferential: defence facility balance Rs35.00 Cr | FY28 | L1090-1091 | initiated |
| C12 | Preferential: working capital Rs140.00 Cr; Rs48.75 Cr used | FY28 | L1148-1153 | underway ("Ongoing") |
| C13 | Preferential: GCP Rs100.00 Cr | FY28 | L1154-1155 | initiated ("Ongoing, nil utilization") |
| C14 | Promoter warrant conversion; balance Rs416.25 Cr receivable | ~25-Nov-2027 (25.05.2026 + 18 months, computed) | L1056-1058 | initiated (no Q2 receipt, L1058) |

## NOTION CHECKLIST TOUCHPOINTS (for A4; F17 itself N.A.)

| Notion item (memory) | touched by this document? | ref |
|---|---|---|
| Growth trigger 3: HASPL aerospace consolidation, "closing CY26" | Yes. Consolidation CPs open at 30-Sep; proceeds deadline moved to 31-Dec-2026 | FN-01, FN-02 |
| Checklist #9 / promise log: Nivetti completion 31-Dec-2026 (moved from 30-Sep) | Not named in the document. Same original and revised dates as C7 [INFERENCE: possible link, unverified] | FN-01 |
| 14-Sep watch: "whether promoter warrant proceeds fund at Rs74" | Yes. No receipt in Q2; Rs416.25 Cr outstanding | FN-03, FN-04 |
| Promise log: "promoter warrant 75% balance (~Rs412.5 cr) ~Nov-2027" | Yes. Filed balance Rs416.25 Cr; memory figure needs correction | FN-04 |
| Q1 FY27 Q9: diluted EPS equals basic despite warrants | Indirectly. Instrument terms confirmed | FN-04 |
| Cash conversion INDETERMINATE (H1 CFO test) | Indirectly. QIP proceeds lien-marked as LC margin; proceeds held in CC account | FN-05, FN-09 |
| Preform captive margin (memory ~25-26% EBITDA) and HTL minority holding UNVERIFIED | Yes. Rs175 Cr preform object routed via HTL, funded only on conversion | FN-13 |
| Checklist #1-3, #5-8, #10-13; tripwires #1-#5 | Not addressable by an MA report | - |

```yaml
stage: A3-forensics
company: "HFCL"
quarter: "Q2 FY27"
doctype: "presentation (one-off disclosure, doctag mareport)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/hfcl-q2fy27/work/forensics_mareport_hfcl_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "L1105-1108, L1282, L1119-1146", classification: "FORWARD-SIGNAL", implication: "Rs90 Cr HASPL object missed 30-Sep-2026, zero used, delay 'Not Ascertainable'; deployment tied to open defence-consolidation conditions precedent; revised 31-Dec-2026 has no stated slack"}
  - {id: "FN-02", check: "F13", line: "L716-726, L747, L684-688", classification: "AMBIGUOUS", implication: "Extension by circular resolution 25-Sep-2026, no shareholder approval; delay reason is board-authored and not MA-reviewed"}
  - {id: "FN-03", check: "F1", line: "L1056-1060, L1272-1278", classification: "FORWARD-SIGNAL", implication: "Rs416.25 Cr of preferential objects (preform 175, defence 50, WC 91.25, GCP 100) unfunded until warrant conversion; defence Rs15 Cr due 30-Sep-2027 precedes ~25-Nov-2027 window end"}
  - {id: "FN-04", check: "F10", line: "L45-50, L1056-1058", classification: "FORWARD-SIGNAL", implication: "7.5 Cr promoter warrants outstanding, Rs55.50/warrant (Rs416.25 Cr) due by ~25-Nov-2027; check diluted EPS; Notion ~Rs412.5 Cr is wrong"}
  - {id: "FN-05", check: "F7", line: "L230-236, L1253", classification: "AMBIGUOUS", implication: "QIP proceeds moved to CC account in Q1 (amount not stated); commingling blocked direct MA verification; reliance on management and CA certificates"}
  - {id: "FN-06", check: "F7", line: "L563-570", classification: "FORWARD-SIGNAL", implication: "Rs24.27 Cr R&D left for H2 FY27 (~Rs12.1 Cr/qtr vs Q2 10.98); carry-forward 'due to any reason' clause placed under the deadline as pre-emptive cover"}
  - {id: "FN-07", check: "F6", line: "L248, L1253", classification: "AMBIGUOUS", implication: "All Q2 R&D use was payroll, none technology acquisition; proceeds fund recurring cost; expensed or capitalised?"}
  - {id: "FN-08", check: "F14", line: "L248-249, L510-512", classification: "AMBIGUOUS", implication: "R&D FY26 tranche Rs15 Cr missed (14.75 cumulative to Q1 FY27) yet delay read as 'No Delays'; p10 alignment not image-verified"}
  - {id: "FN-09", check: "F14", line: "L491-504", classification: "AMBIGUOUS", implication: "Earning NA vs Rs0.20 Cr interest; Rs21.22 Cr R&D proceeds lien-marked as LC margin; Rs10.30 Cr FD matured 09-Oct-2026, status unstated"}
  - {id: "FN-10", check: "F14", line: "L665, L716, L765", classification: "AMBIGUOUS", implication: "Deviation 'Nil' headline vs utilisation 'No'; timing slips sit outside the deviation definition; viability 'No' rests on management certificate"}
  - {id: "FN-11", check: "F14", line: "L572-579, L456, L556", classification: "AMBIGUOUS", implication: "QIP GCP stated 'Nil' vs Rs93 Cr object fully used Q4 FY26; '^' undefined; no item-wise GCP use; 83% of QIP to fungible uses in one quarter"}
  - {id: "FN-12", check: "F14", line: "L659, L1230, L1052, L1060", classification: "NEUTRAL-FACT", implication: "Preferential report paginated 3-15; two unutilised totals (90.00 / 506.25); garbled footnote"}
  - {id: "FN-13", check: "F6", line: "L805-808, L1085-1086", classification: "AMBIGUOUS", implication: "Rs175 Cr preform object routed via HTL, ownership unstated (memory: HTL minority UNVERIFIED); captive-preform margin step rides warrant conversion"}
  - {id: "FN-14", check: "F6", line: "L511, L1251", classification: "NEUTRAL-FACT", implication: "QIP OFC capex Rs35 Cr completed Q2 FY27; small vs capacity programme; does not confirm Dec-2026 capacity date"}
forward_signals: ["FN-01", "FN-03", "FN-04", "FN-06"]
ambiguous: ["FN-02", "FN-05", "FN-07", "FN-08", "FN-09", "FN-10", "FN-11", "FN-13"]
commitments:
  - {commitment: "QIP OFC capex Rs35.00 Cr", implied_date: "FY27", ref: "L511", status_word: "completed"}
  - {commitment: "QIP R&D Rs50.00 Cr (Rs24.27 Cr left)", implied_date: "31-Mar-2027", ref: "L563-565", status_word: "underway"}
  - {commitment: "QIP repayment of borrowings Rs105.00 Cr", implied_date: "FY26", ref: "L550", status_word: "completed"}
  - {commitment: "QIP long-term working capital Rs260.00 Cr", implied_date: "FY26", ref: "L553", status_word: "completed"}
  - {commitment: "QIP GCP Rs93.00 Cr", implied_date: "FY26", ref: "L556", status_word: "completed"}
  - {commitment: "QIP issue expenses Rs7.00 Cr (6.94 used)", implied_date: "undated", ref: "L559", status_word: "underway"}
  - {commitment: "Invest Rs90.00 Cr in HASPL equity", implied_date: "30-Sep-2026 original; 31-Dec-2026 revised", ref: "L1107, L743-745", status_word: "underway"}
  - {commitment: "Deploy HASPL proceeds on completion of conditions precedent for defence consolidation", implied_date: "undated, bounded by 31-Dec-2026", ref: "L1119-1146", status_word: "underway"}
  - {commitment: "Preform facility via HTL Rs175.00 Cr", implied_date: "31-Jul-2028", ref: "L1085-1086", status_word: "initiated"}
  - {commitment: "Defence facility first tranche Rs15.00 Cr", implied_date: "30-Sep-2027", ref: "L1088-1089", status_word: "initiated"}
  - {commitment: "Defence facility balance Rs35.00 Cr", implied_date: "FY28", ref: "L1090-1091", status_word: "initiated"}
  - {commitment: "Preferential working capital Rs140.00 Cr (48.75 used)", implied_date: "FY28", ref: "L1148-1153", status_word: "underway"}
  - {commitment: "Preferential GCP Rs100.00 Cr", implied_date: "FY28", ref: "L1154-1155", status_word: "initiated"}
  - {commitment: "Promoter warrant conversion, Rs416.25 Cr balance", implied_date: "~25-Nov-2027 (computed)", ref: "L1056-1058", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Read this as a funding map. Of Rs555 Cr preferential objects, Rs416.25 Cr (preform 175, defence 50, WC 91.25, GCP 100) has no cash until the promoter converts warrants by ~25-Nov-2027 (computed). The preform facility behind the memory-guided 25-26% captive-preform margin therefore rides promoter conversion timing, and it sits in HTL, whose ownership the report does not state. The Rs90 Cr HASPL object missed 30-Sep-2026. The board extended it to 31-Dec-2026 by circulation on 25-Sep. [INFERENCE] These dates match the Nivetti SPA dates in Notion memory (30-Sep moved to 31-Dec-2026). If the HASPL conditions precedent are the Nivetti closing, one miss on 31-Dec fails two promises. Slip-log treatment is operator-only, so A4 should ask and not count. On the QIP side, proceeds passed through the CC account (commingled; MA could not verify directly), and Rs21.22 Cr earmarked for R&D is lien-marked as LC margin. That fits working-capital strain (memory: FY26 CFO minus Rs378 Cr). Notion's Rs412.5 Cr warrant balance is wrong; the filed figure is Rs416.25 Cr. The p10 delay-cell alignment is not image-verified."
```
