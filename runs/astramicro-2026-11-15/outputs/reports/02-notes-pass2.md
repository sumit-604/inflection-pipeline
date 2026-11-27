# STAGE 2 NOTES, PASS 2 (WHAT WAS MISSED): Astra Microwave Products Ltd (ASTRAMICRO), run 2026-11-15

Source: runs/astramicro-2026-11-15/inputs/annual-report/Annual_Report_2026.txt (35th Annual Report, FY ended 31 March 2026). Pass 1 read with its ERRATA applied.

ANCHOR CONVENTION (same as Pass 1). "p.N" is the PDF page marker "[page N]" in the .txt (printed page = N minus 3). UNIT: every statement face reads "All amounts are in Rs. Lakhs, except otherwise stated" (Standalone CFS p.209-210, Cons CFS p.283-284). Every figure is Rs Lakhs unless marked. Nothing is converted. "(calc)" is my arithmetic on named anchored inputs. "INFERENCE" marks a reading the document does not state; the arithmetic under it is anchored. Missing data is "NOT FOUND IN DOCUMENT".

Method. I re-read standalone Notes 1 to 47 (pp.212-265) and consolidated Notes 3 to 50 (pp.299-348) against Pass 1, and tied the notes to the cash flow statement line by line. Pass 1 covered the surface of nearly every note. The new material below sits in cross-note tie-outs, small print, and arithmetic that Pass 1 did not run. Items that Pass 1 covered fully are not repeated.

Result: PASS 2 FOUND MATERIAL NEW ITEMS. 19 items follow, then a short list of refinements to Pass 1.

---------------------------------------------------------------------

## A. FIRST-PRIORITY ITEMS (cash conversion, concentration, ARCPL, warrants, demerger, borrowings)

| # | New finding | Anchor | Rating |
|---|---|---|---|
| P2-1 | Navictronics 912.00 sits inside operating cash flow, not investing (section 1) | CFS p.209; Cons CFS p.283 | YELLOW |
| P2-3 | Receivable ageing: the ">3 years" bucket is larger than the whole ">2 years" population of a year earlier (section 3) | Note 44, p.263 | RED |
| P2-4 | Receivable and payable "from due date" columns look like they are not due-date based (section 4) | Notes 44, 45, pp.263-264 | YELLOW |
| P2-5 | ECL: 100% cover only on SICR items; 7,083.37 of ">2 years, considered good" carries 144.14 (section 5) | Notes 39, 44, pp.255-256, 263 | RED |
| P2-8 | ARCPL: capitalised development = 114.7% of its net assets; limit up 2.9x with the AMPL guarantee flat (section 8) | Cons Note 46, pp.341-343; Cons Note 44, p.335 | RED |
| P2-10 | DSCR 1.01 only reproduces if working-capital loan repayment counts as debt service (section 10) | Note 43(xiv)(c), p.262 | YELLOW |

Priority 2 (concentration) and warrants/demerger: nothing new beyond Pass 1 inside the notes. Warrant arithmetic re-checked: 20,13,885 x Rs 864 = Rs 173.99 crore; 25% = Rs 43.50 crore = 4,349.99 Lakhs (Note 13, p.235). It ties.

---------------------------------------------------------------------

## 1. P2-1 CASH FLOW CLASSIFICATION: NAVICTRONICS 912.00 (YELLOW)

Tie-out of the standalone cash flow lines to balance sheet movements, line by line:

| CFS line (p.209) | CFS | Balance sheet movement | Gap | Explained by |
|---|---|---|---|---|
| Inventories | (15.47) | 60,852.99 - 60,837.52 = 15.47 (Note 8, p.232) | 0.00 | ties |
| Provisions | 525.30 | 462.45 (Note 16, p.235) | 62.85 | gratuity OCI gain 62.85 (Note 32, p.248) |
| Other financial liabilities | 595.01 | 1,013.62 (Note 18, p.239) less capital creditors 422.68 | 4.07 | unpaid dividend (CFS dividends 2,092.86 vs Note 41, 2,088.79) |
| Contract liabilities | (274.16) | +1,395.29 less non-cash accrual 1,669.45 | 0.00 | ties (Pass 1) |
| Capex PPE | (7,767.64) | additions 7,265.76 + CWIP 925.04 - capital creditors 422.68 - capital advance 0.48 | 0.00 | ties |
| Other bank balances | (1,240.52) | bank balances +620.60 and deposits above 12 months +619.92 (Notes 10(b), 5) | 0.00 | ties |
| **Other current assets** | **(2,107.13)** | **6,171.01 - 4,975.88 = 1,195.13 (Note 7(b), p.232)** | **912.00** | **not explained** |

- The gap is 912.00 to the paisa. The standalone investing section shows "Payments for investments in subsidiary and joint venture" as nil for FY26 (FY25 12.00). Note 4 (p.230) and Note 31(iii) (p.247) show a 912.00 equity investment in Navictronics Pvt Ltd (carrying 2.00 to 914.00).
- Consolidated repeats it. Cons CFS other current assets (2,014.47) (p.283) against Cons Note 8 movement 6,184.76 - 5,082.29 = 1,102.47 (p.307): gap 912.00. Cons CFS "Investment in equity shares of joint venture" is nil for FY26 (FY25 (2.00)).
- INFERENCE: the Navictronics payment went through "other current assets" in operating cash flow, not investing. If so, FY26 standalone CFO is 912.00 too low: 37,595.92 + 912.00 = 38,507.92 (calc), and investing outflow is 8,601.65 + 912.00 = 9,513.65 (calc). Consolidated CFO would be 39,585.39 (calc). The direction is conservative for CFO. It still shows the cash flow statement is not clean at line level. The company gives no reason (NOT FOUND IN DOCUMENT).
- Question for management: why is the 912.00 Navictronics equity payment not in investing cash flow?

## 2. P2-2 INTEREST RATE SENSITIVITY IS MISCOMPUTED (YELLOW)

- Note 39(c) (p.259) says a 50 bps rise cuts PBT by 13.46 (FY25 15.01) on "floating rate borrowings".
- 13.46 = 0.5% x 2,692.57, where 2,692.57 is the whole FY26 interest expense on term and working capital loans (Note 26 net debt table, p.242: term loans 553.25 + working capital 2,139.32). FY25: 0.5% x 3,002.80 = 15.01 (calc). The equity column ties at x (1 - 25.17%): 10.07 and 11.24.
- So the note applies 0.5% to the interest cost, not 50 bps to the floating principal. On the floating principal at year end (working capital demand loan 15,109.45 + cash credit 4,883.82 = 19,993.27, Note 14, p.236) the same test gives 99.97 (calc), which is 7.4x the disclosed 13.46 and 0.41% of PBT (calc) against the 0.05% implied.
- Term loan reset terms: NOT FOUND IN DOCUMENT (Pass 1). Interest cost is a small share of PBT (finance cost 5,504.34 against PBT 24,504.61). The finding is about disclosure reliability, not about size.

## 3. P2-3 RECEIVABLE AGEING DOES NOT ROLL FORWARD (RED)

Ageing from due date, Note 44 (p.263), standalone:

| | FY25 | FY26 |
|---|---|---|
| 2-3 years: considered good + SICR | 2,335.84 + 133.31 = 2,469.15 | 2,928.76 |
| More than 3 years: considered good + SICR | 1,355.23 + 767.53 = 2,122.76 | 4,154.61 + 1,074.96 = 5,229.57 |
| Total more than 2 years | 4,591.91 | 8,158.33 |

- A balance more than 3 years past due at 31 March 2026 was due before 31 March 2023. At 31 March 2025 it was already more than 2 years past due. So the FY26 ">3 years" bucket can hold at most the whole FY25 ">2 years" population, 4,591.91. It holds 5,229.57, which is 637.66 more (calc). The consolidated schedule shows the same: FY26 more than 3 years 4,154.62 + 1,080.44 = 5,235.06 against FY25 more than 2 years 2,335.84 + 1,359.73 + 133.31 + 767.53 = 4,596.41, excess 638.65 (Cons Note 47, p.346).
- This cannot come from time passing. The document gives no explanation (revised due dates, reclassification, credit notes, re-invoicing, or a changed ageing basis are all possible; none is stated). NOT FOUND IN DOCUMENT.
- Pass 1 said the roll-forward is not reconciled. This sharpens it: the schedule cannot be right on a consistent due-date basis. The 637.66 is 0.9% of gross receivables (calc), small by itself. The weight is on the reliability of every ageing percentage in Pass 1 (29.4% over 6 months; 11.5% over 2 years).

## 4. P2-4 THE "FROM DUE DATE" COLUMNS LOOK LIKE ANOTHER BASIS (YELLOW)

- Receivables "Not due" is 651.06, equal to the non-current receivable in Note 9(a) (p.232). All current receivables (69,342.41 net of nothing, i.e. 70,174.0 gross, calc) are therefore "past due" from day one. FY25 "Not due" is nil on 79,216.51.
- Payables "Not due" for others is 2,217.69, equal to goods-in-transit (Note 8, p.232). FY25 722.24, equal again (Pass 1).
- MSME payables 1,320.40 are 100% in "less than 1 year" and nil "not due" (Note 45, p.264). Other trade payables past due: 7,840.88 + 31.84 + 26.13 + 75.64 = 7,974.49 = 77.8% of 10,253.45 (calc). Yet the MSME note shows interest due of only 13.56 on principal 1,306.84, 1.04% (calc, Note 17(a), p.239), and no principal paid late in FY26.
- INFERENCE: both ageing schedules are likely built from invoice or booking date, not from due date, despite the caption. The "Not due" column then holds only items the system tags specially. If so, "more than 6 months past due" overstates lateness (the invoices are old, but not necessarily overdue) and the Pass 1 reading of "almost the whole book past due" is too harsh. The document does not confirm the basis (NOT FOUND IN DOCUMENT).
- Question for management: confirm the ageing basis and the contractual payment terms by customer type.

## 5. P2-5 ECL STRUCTURE: COVER IS 100% ON SICR ITEMS AND LITTLE ELSE (RED)

Pass 1 gave 14.9% cover on the ">2 years" bucket. The split by tag is sharper (Notes 39 and 44, pp.255-256, 263):

| | FY25 | FY26 |
|---|---|---|
| More than 2 years, tagged SICR | 900.84 | 1,074.96 |
| ECL on more than 2 years | 900.84 | 1,219.10 |
| ECL above the SICR amount | 0.00 | 144.14 |
| More than 2 years, "considered good" (no SICR tag) | 3,691.07 | 7,083.37 |
| Cover on that "considered good" part (calc) | 0.0% | 2.0% |

- ECL on the ">2 years" bucket equals the SICR amount in FY25 exactly, so the company provides 100% on SICR items and nothing on the other 3,691.07. In FY26 the "considered good" more-than-2-year balance almost doubled (+91.9%, calc) to 7,083.37 with 144.14 of cover.
- Charge of 540.89 by bucket (calc): less than 6 months +131.96; 6 months to 1 year +62.38; 1 to 2 years +28.29; more than 2 years +318.26 (SICR +174.12, other +144.14). 58.8% of the charge (calc) sits in the oldest bucket.
- INFERENCE (implied matrix base). If the stated matrix is the only ECL source, the non-government balances covered are at most: less than 6 months 155.38 / 1% = 15,538 (31.5% of 49,347.75); 6 months to 1 year 66.77 / 2% = 3,338.50 (55.3%); 1 to 2 years 40.33 / 10% = 403.30 (6.1%) (calc). FY25: 2,342.00 (4.7%), 146.33 (2.0%), 109.45 (0.6%) (calc). The rest sits with government or related-party customers, where Note 39 presumes nil or negligible risk and assesses "case to case" (p.255). ARCPL alone is 19,598.78. The report does not give the split. NOT FOUND IN DOCUMENT.
- Reading: the 7,083.37 of old "good" balances rests on the government-customer presumption and on the ARCPL relationship. The cover answers to a policy, not to ageing.

## 6. P2-6 JANYU CCPS: SALE PRICE VERSUS CARRYING BASIS (YELLOW)

Pass 1 recorded proceeds 212.22 and gain 78.71. The notes tie out fully and show more (Notes 46, 20, 22, 4; CFS; pp.229-230, 239-240, 264, 209):

- Consideration for the 28,486 CCPS sold = cash 212.22 (CFS FY26) + advance 317.33 received in FY25 (Note 20 FY25 column, p.239; CFS FY25) = 529.55 (calc).
- Carrying released = 543.58 - 92.74 = 450.84. Gain = 529.55 - 450.84 = 78.71, equal to Note 22 (p.240). Exact tie.
- Price per share = 529.55 Lakhs / 28,486 = about Rs 1,859 (calc).
- Cost basis: the FVTPL block 53.74 / 28,599 shares = Rs 187.9 per share (calc). The unsold held-for-sale block 92.74 / 49,351 shares = Rs 187.9 per share (calc). So both unsold blocks sit at cost.
- The FY25 uplift was 397.32 (Note 22 FY25). The original 77,837 CCPS at Rs 187.9 = 146.3, plus 397.3 gives the FY25 held-for-sale carrying 543.58 (calc). In FY26 the released 450.84 = cost of the 28,486 shares sold, 53.5, plus the entire 397.3 uplift (calc). The whole uplift on 77,837 shares was assigned to the 36.6% that were sold; the other 63.4% went back to cost.
- Indicative scale: 77,950 CCPS held (49,351 + 28,599) x Rs 1,859 = about 1,449.1 against carrying 146.48 (92.74 + 53.74). The difference is 1,302.6 (calc), 5.3% of standalone PBT. This is a scale marker only. Ind AS 109 needs fair value at year end. The valuation technique and inputs for the Level 3 holding are NOT FOUND IN DOCUMENT (section 16), and one sale does not set fair value for the rest.
- The FVTPL line (28,599 shares) shows no fair value change in FY26 (53.74 in both years), in a year with a priced sale of the same series.
- Pass 1 INV-C (held-for-sale older than 12 months) still stands. This adds: the unsold block is not marked to the transaction.

## 7. P2-7 NAVICTRONICS: THE INTANGIBLE EQUALS ALL THE CAPITAL RAISED (YELLOW)

- Cons Note 46 (pp.343-344): net assets 1,542.10 = 3.80 + 1,824.00 - 285.70 (calc). Intangible 1,626.51 net plus FY26 amortisation 197.49 = 1,824.00 gross (calc). AMPL put in 912.00 (Note 31(iii), p.247). 1,824.00 is exactly 2 x 912.00 (calc; assumes the other 50% partner, Manjeera Digital Systems Pvt Ltd (p.343), paid the same).
- So the entire equity went into one intangible in the year. The seller or licensor is NOT FOUND IN DOCUMENT. The intangible is amortised at 197.49 (10.8% of gross, calc) with no revenue. Deferred tax liability 67.21 and cash of 1.30 follow.
- Whether the seller is a related party of either JV partner: NOT FOUND IN DOCUMENT. Cons Note 32 lists no such party.
- AMPL's total exposure beyond equity: capital commitments of the joint ventures 2,154.53 net of advances 195.97 (Cons Note 46, p.341). The note does not say whose share this is.

## 8. P2-8 ARCPL: BALANCE SHEET DETAIL PASS 1 DID NOT USE (RED)

Cons Note 46 (pp.341-343), 100% of ARCPL:

| ARCPL | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| Other intangible assets | 3,512.62 | 30.03 |
| Intangible assets under development | 5,914.86 | 5,817.71 |
| Total capitalised development / intangibles (calc) | 9,427.48 | 5,847.74 |
| Net assets | 8,220.63 | 6,386.10 |
| Intangibles as % of net assets (calc) | 114.7% | 91.6% |
| Other financial liabilities | 8,831.13 | 277.87 |
| Other current assets | 12,268.81 | 6,260.77 |
| Borrowings (current) | 11,122.02 | 1,896.92 |
| Long term liabilities | nil | 4,877.02 |
| Cash + other bank balances | 3,415.30 + 3,793.97 = 7,209.27 | 10.84 + 528.08 = 538.92 |

- ARCPL's capitalised development exceeds its net assets. If any part failed an impairment test, ARCPL equity would turn negative. AMPL books 923.23 (50% of 1,846.44 profit) and carries 4,129.73 (Pass 1). The impairment test inputs for ARCPL are NOT FOUND IN DOCUMENT.
- ARCPL "other financial liabilities" rose 31.8x (calc) and the FY25 "long term liabilities" 4,877.02 disappeared. The notes do not say what these are or who is owed.
- ARCPL lender limit: 9,000 for the 2025 quarters, 26,500 for March 2026 (Cons Note 44(ii), p.335, per Pass 1 section 13). The limit is 2.9x higher. The AMPL guarantee stays at 8,000.00 (Note 34, p.251), which is 30.2% of 26,500 (calc). Who backs the remaining limit: NOT FOUND IN DOCUMENT.
- ARCPL eliminates: the consolidation adjustment for "unrealised gain and commission on corporate guarantee etc." is +19.41 (FY25 -29.34) (Cons Note 46, p.342). A positive number adds to the carrying value. Against it: AMPL sales to ARCPL 16,009.91 and an ARCPL inventory rise of 12,336.77. No unrealised profit elimination of visible size is shown. (Pass 1 RPT-2 stands; I add the sign point.)
- Cross-reference only (AGM Notice Item 9, PDF pp.83-84; not a note): FY26 transactions with ARCPL Rs 160.09 crore (equals the 16,009.91 sales; no purchases from ARCPL), April to June 2026 transactions Rs 11.07 crore, and a proposed approval of Rs 200 crore for FY27 covering sales/purchases, corporate guarantee and letter of comfort. The notice states "No defaults made" by ARCPL in three years. April to June 2026 at 11.07 is 27.7% of the FY26 quarterly average of 40.02 (calc). Tie to the Q1 FY27 filing when it is read.

## 9. P2-9 ADT: GUARANTEE NUMBERS AND TAX (YELLOW)

- Pass 1 RPT-3 found 3,500 against 4,300. A third figure exists: the only ADT lender table in the report shows HDFC Bank at limit 1,500 (Cons Note 44(ii), p.335). ADT cash credit was 493.77 at March 2025 and nil at March 2026 (Cons Note 15, p.311, consolidated cash credit equals standalone 4,883.82). The AMPL guarantee secures ADT's HDFC cash credit (Cons Note 15, p.312).
- The ADT guarantee commission is 36.75 = exactly 1.05% of 3,500 (calc, CFS non-cash line p.210). That supports 3,500 as the live figure. The 4,300 in Note 34 may be a stale approved figure. Not stated.
- ADT profit after tax rose from 38.12 to 752.38 (19.7x) (Cons Note 45, p.338) while AMPL purchases from ADT rose 39.3% (Pass 1). ADT revenue: NOT FOUND IN DOCUMENT.
- Tax: consolidated current tax on profits 6,704.25 vs standalone 6,631.91 (Cons Note 30(c), p.319; Note 29(c), p.244) leaves 72.34 for the subsidiaries (calc). The reconciliation line "DTA not created on set off or carried forward losses from subsidiaries" is (144.57) (FY25 (6.55)), a reduction (Cons Note 30(d), p.320). INFERENCE: ADT's FY26 profit was largely sheltered by earlier tax losses (144.57 / 25.17% = 574.4 of losses used, calc). The loss shelter will not repeat once used.

## 10. P2-10 DSCR 1.01 IS A DEFINITION ARTEFACT (YELLOW; revises Pass 1 BOR-4)

- Note 43(xiv)(c) (p.262): earnings for debt service = PAT + finance cost + non-cash expenditure; debt service = finance cost + principal repayments. No carve-out for revolving working capital loans.
- Using PAT 17,783.73 + finance cost 5,504.34 + depreciation and amortisation 4,309.09 = 27,597.16 (plus ECL 540.89 = 28,138.05) (calc). With debt service = 5,504.34 + term loan repayment 1,937.27 + net working capital repayment 20,815.38 (Pass 1), DSCR is 0.996 (calc), close to the reported 1.01. With term loan repayment only, DSCR is 28,138.05 / 7,441.61 = 3.78 (calc).
- So 1.01 reflects paying down 20,815.38 of working capital loans, not weak term debt cover. The FY25 0.45 does not reproduce from the FY25 cash flow under either reading (calc). Inputs are not shown in the note.
- Pass 1 BOR-4 ("DSCR 1.01 even after the debt fall") should read: the ratio is distorted by the definition. The term loan cover is not the concern the ratio suggests. The concern that stays is lender reporting (Pass 1 BOR-3).

## 11. P2-11 FY25 MATURITY TABLE DOES NOT TIE (YELLOW, low)

- Note 39 (p.257): FY25 borrowings, within 12 months 37,919.96 + 1 to 5 years 4,589.75 = 42,509.71, labelled "total carrying amount". The FY25 balance sheet carrying is 3,936.47 + 37,919.96 = 41,856.43 (Note 14, p.236). Difference 653.28 (calc) in the 1 to 5 year bucket.
- FY26 ties: 6,124.43 + 197.30 = 6,321.73 = non-current carrying. The FY25 column therefore looks undiscounted or includes interest while FY26 does not. Lease liabilities in FY26 are shown at 74.97 against carrying 61.38. The comparatives are on a mixed basis. The company does not say so.

## 12. P2-12 SANCTIONED WORKING CAPITAL LIMITS (cross-reference, not a note)

Pass 1 listed sanctioned working capital limits as NOT FOUND. The Directors' report loan table gives them (PDF pp.192-193, "Open cash credit including WCDL"): sanctioned Rs 765,00,00,000 (FY25 Rs 435,00,00,000), outstanding Rs 199,93,27,646 (FY25 Rs 359,24,82,786). In Lakhs: 76,500 (43,500) and 19,993.28 (35,924.83). The outstanding ties to Note 14 (19,993.27 plus rounding).

- Limits rose 75.9% (calc). FY26 utilisation at year end 26.1% (calc: 19,993.27 / 76,500); FY25 82.6% (calc).
- Undrawn per Note 39 (p.257) 56,514.50 vs 76,500 - 19,993.27 = 56,506.73 (calc), gap 7.77. FY25: 43,500 - 35,924.83 = 7,575.17 against Note 39 5,075.17, gap 2,500.00 (calc). The two disclosures differ by exactly 2,500.00 in FY25; the report does not explain.
- Reading: FY26 headroom is large. The limit increase to 76,500 matches a business that expects bigger working capital swings (Pass 1: receivables, inventory days). It also brings more guarantee and letter of credit capacity: bank guarantee commission is 1,028.69 (Pass 1).

## 13. P2-13 GRATUITY AND LEAVE: PASS 1 OPEN POINT ANSWERED

- Pass 1 section 9 said the net effect of attrition 12% to 15% was NOT FOUND. The note answers it (Note 32(vi), p.249): attrition +1% takes DBO to 2,472.28 (-14.94 from 2,487.22); -1% gives 2,503.27. A higher attrition assumption lowers DBO. The demographic assumption change is an OCI gain of 52.02 in FY26 (FY25 41.72) (p.248), 2.1% of closing DBO (calc). So the 3-point attrition rise cut DBO and flattered OCI; the discount rate rise (7.00% to 7.79%) added a financial-assumption gain of 107.31; experience loss was 96.48.
- Actual benefit payments in FY26 were 75.34 (FY25 112.72) against a prior-year expected year-1 payment of 279.47 (calc: 27% of expected), while attrition was assumed up to 15%. The assumption and the experience point in opposite directions. Rate YELLOW (low).
- Leave encashment provision 1,141.23 (834.91 + 306.32), FY25 944.02 (Note 16, p.235). Actuarial assumptions and sensitivity for leave: NOT FOUND IN DOCUMENT (Note 32(a), p.247 only cross-refers). Policy says remeasurements go to P&L (Note 2.18(ii), p.222).

## 14. P2-14 THE MARGIN GAIN IS ALL MATERIAL COST (YELLOW, low)

From Notes 23 and 24 (pp.240-241), standalone:

| | FY26 | FY25 |
|---|---|---|
| Cost of materials consumed | 59,572.86 | 63,623.88 |
| Change in WIP and FG (credit) | (841.20) | (5,007.56) |
| Net material cost (calc) | 58,731.66 | 58,616.32 |
| % of revenue from operations (calc) | 50.82% | 56.13% |

- Net material cost is flat (+0.2%, calc) on revenue up 10.67%. The ratio fell 5.31 points (calc). Employee cost rose 17.4% and other expenses 48.8% (Pass 1), so the material line carries the profit gain: PBT rose 26.7% (calc: 24,504.61 / 19,344.07).
- The notes give no reason (mix, price, the ARCPL sales at 16,009.91, services +64.2%, or lower WIP build). NOT FOUND IN DOCUMENT. FY25 had a WIP build of 5,007.56 that FY26 did not repeat (841.20), so cost absorption timing also moves the ratio. Test with the Q2 FY27 concall when it is filed.

## 15. P2-15 SMALL BALANCES THAT DO NOT MOVE OR ARE NOT EXPLAINED (YELLOW, low)

- Advance for expenses to others: 4,950.71 (FY25 3,994.91), +23.9% (calc), 4.28% of revenue and 3.84% of equity (calc) (Note 7(b), p.232). Consolidated 4,968.56 (4,117.05) (Cons Note 8, p.307). The nature (supplier advances, deposits, staff) is NOT FOUND IN DOCUMENT. It is not in the ageing or ECL tests.
- Prepaid expenses 1,301.32 (513.18 non-current + 788.14 current), FY25 1,314.32. Content NOT FOUND IN DOCUMENT (bank guarantee commission is a candidate; not stated).
- Advance for expenses to Janyu: 21.00 in both years (Note 31(ii), p.246). Income tax refund receivable 84.63 in both years (Note 11, p.233). No movement in a year.
- Capital creditors 554.65 (131.97), 4.2x (calc) (Note 18, p.239): the capex ramp is partly vendor-funded at year end.

## 16. P2-16 FAIR VALUE DISCLOSURE (YELLOW, low)

- Note 38 (pp.253-254) shows every instrument at "Level 3", including cash, bank balances, receivables, borrowings and the forward contract liability 10.30. Cash and borrowings at amortised cost do not need a level; a forward contract valued on observable forward rates is normally Level 2.
- For the two real Level 3 items (Janyu CCPS 53.74 and Fermionic Design 18.08, total 71.82): valuation technique, inputs, and sensitivity are NOT FOUND IN DOCUMENT. No Level 3 reconciliation is given. Fermionic stake % is NOT FOUND (Pass 1).

## 17. P2-17 INTERNAL INCONSISTENCIES IN THE SMALL PRINT (YELLOW, low)

- Note 40 (p.259) says "there are no externally imposed capital requirements" and in the next paragraph says the company adjusts capital for "the requirements of the financial covenants". The two sentences conflict. Specific covenants stay NOT FOUND (Pass 1 BOR-6).
- Note 36 (p.252) lists cash and cash equivalents 16,456.80 as pledged; Note 10(a) (p.233) says no repatriation restrictions. The pledge of the full balance, including the 16,000.00 year-end deposit, is not explained.
- Janyu is classed an associate at 6.13% (FY25 8.45%) (Cons Note 46, p.344). The basis for significant influence at that level (board seat, technical dependence) is NOT FOUND IN DOCUMENT. It is held at FVTPL, not equity accounted.
- Janyu summary is "Unaudited" (Pass 1 INV-D). Its FY26 PBT is 1,422.10 and tax 806.32 (calc from Cons Note 46, pp.345-346), 56.7% of PBT (calc).

## 18. P2-18 USD RECEIVABLES AND THE FX GAIN (YELLOW)

- The unrealised FX gain removed in the cash flow, 918.25, can be rebuilt: receivable translation +1,097.39 (CFS receivables line 9,488.85 less balance sheet gross decline 8,391.46) less payable translation 179.14 (balance sheet payable rise 4,014.98 less CFS 3,835.84) = 918.25 (calc). It ties.
- So the FX gain is a translation gain on USD receivables, 88.7% unrealised (918.25 of 1,035.04, calc). USD receivables 12,810.31 are 18.1% of gross receivables (calc: 12,810.31 / 70,825.05) and 59.3x outside-India revenue of 215.93 (calc). Pass 1 asked who owes them. The notes still do not say. Whether ARCPL's 19,579.28 includes USD-denominated invoices: NOT FOUND IN DOCUMENT. This matters because a rupee rise would reverse the gain and the receivable (5% USD move = 494.23 on PBT, Note 39, p.258).

## 19. P2-19 NOTES THAT HAD NOTHING NEW

Standalone Notes 1.1 to 2.24 (policies, beyond the points in sections 4, 16 and 17), 3.1 to 3.4 (property, plant and equipment, CWIP, intangibles, leases), 5, 6, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 25, 26, 27, 28, 29, 30, 33, 35, 37, 41, 42, 43(i) to (xiii), 47 and the consolidated Notes that mirror them (3 to 13, 16 to 29, 31 to 34, 36 to 43, 48 to 50): re-read; the figures tie to Pass 1 and to the cash flow statement; nothing material to add. Specific re-checks that tied: equity roll-forward (71,133.32 + 17,783.73 - 2,088.79 + 47.03 = 86,875.29, Note 13(iii)); gratuity DBO and plan asset roll-forwards (2,487.22; 1,121.70); segment non-current assets 27,794.86 = PPE 25,600.30 + intangibles 574.42 + CWIP 925.04 + ROU 58.35 + other non-current assets 636.75 (Note 33(b)); consolidated profit 19,297.08 = 17,783.73 + 752.38 + 4.07 - 10.53 + 923.23 - 142.85 - 12.95 (Cons Note 45, pp.338-340); trade payable and receivable totals across Notes 9, 17, 39, 44, 45.

---------------------------------------------------------------------

## REFINEMENTS TO PASS 1 (for Pass 3 to carry)

1. BOR-4 (DSCR): see section 10. Downgrade the concern from term cover to definition.
2. Section 9 (attrition direction): answered in section 13.
3. Section 7 (sanctioned limits NOT FOUND): partly answered by the Directors' report table, section 12.
4. Section 4.3 ECL: use the SICR split in section 5. The ">2 years 14.9% cover" is a blend of 100% on SICR and 2.0% on the rest.
5. Section 4.2 percentages: read them with the roll-forward break in section 3 and the ageing-basis doubt in section 4.
6. Section 12.2 (USD receivables): composition in section 18.
7. Section 12.5 CF-1: CFO of 37,595.92 is understated by 912.00 on the tie-out in section 1 (INFERENCE). The working capital release of 13,324.69 (35.4% of CFO) and the two-year conversion of 86.2% are unchanged in direction. If the 912.00 is reclassified, FY26 CFO is 38,507.92 and the two-year CFO to PAT conversion is (38,507.92 - 9,893.82) / 32,122.27 = 89.1% (calc).

---------------------------------------------------------------------

## PASS 2 NEW FINDINGS SUMMARY (new items only, ranked)

| Rank | Finding | Note anchor | Rating |
|---|---|---|---|
| 1 | Receivable ageing breaks: ">3 years" 5,229.57 exceeds the whole FY25 ">2 years" 4,591.91 by 637.66; the schedules do not roll forward | Note 44, p.263; Cons Note 47, p.346 | RED |
| 2 | ECL covers SICR items at 100% and the other 7,083.37 of ">2 years, good" at 2.0% (FY25 0.0% on 3,691.07); matrix covers at most 31.5% of the under-6-month bucket | Notes 39, 44, pp.255-256, 263 | RED |
| 3 | ARCPL: capitalised intangibles 9,427.48 = 114.7% of its net assets; lender limit 9,000 to 26,500 with the AMPL guarantee flat at 8,000.00; other financial liabilities 31.8x | Cons Note 46, pp.341-343; Cons Note 44, p.335 | RED |
| 4 | 912.00 Navictronics equity payment is inside operating cash flow (exact tie in standalone and consolidated); CFO understated | CFS p.209; Cons CFS p.283; Note 4, p.230 | YELLOW |
| 5 | Ageing columns look invoice-date based, not due-date based ("Not due" equals the non-current receivable and goods-in-transit) | Notes 9, 44, 45, 8 | YELLOW |
| 6 | Janyu: 28,486 CCPS sold at about Rs 1,859 per share (529.55 total incl. 317.33 advance); 77,950 remaining CCPS carried at about Rs 187.9 per share; indicative scale 1,302.6 (5.3% of PBT) | Notes 46, 20, 22, 4; CFS | YELLOW |
| 7 | Navictronics: intangible 1,824.00 gross equals 2 x 912.00 of equity; vendor not disclosed; 197.49 amortisation with no revenue | Cons Note 46, pp.343-344 | YELLOW |
| 8 | Interest rate sensitivity is 0.5% of interest cost (13.46), not 50 bps on floating debt (99.97 on closing floating principal) | Note 39(c), p.259; Note 26, p.242 | YELLOW |
| 9 | DSCR 1.01 reproduces only with net working capital loan repayment (20,815.38) in debt service; term cover would be 3.78 | Note 43(xiv)(c), p.262 | YELLOW |
| 10 | ADT guarantee: 1,500 limit vs 3,500 vs 4,300, with ADT drawings nil; commission = 1.05% of 3,500; ADT PAT 19.7x helped by loss set-off | Note 34, p.251; Note 31, p.246; Cons Notes 15, 30, 44, 45 | YELLOW |
| 11 | Net material cost flat at 58,731.66 on revenue +10.67%; ratio 50.82% vs 56.13% drives the margin gain; no reason given | Notes 23, 24, pp.240-241 | YELLOW |
| 12 | USD receivables 12,810.31 (18.1% of gross) drive 88.7% unrealised FX gain; counterparty and ARCPL link not disclosed | Note 39, p.258; CFS p.209 | YELLOW |
| 13 | FY25 maturity table does not tie (42,509.71 vs 41,856.43; gap 653.28) | Note 39, p.257 | YELLOW |
| 14 | Advance for expenses to others 4,950.71 (+23.9%) with nature undisclosed; static Janyu advance and tax refund | Notes 7, 11, 31 | YELLOW |
| 15 | Fair value hierarchy: all Level 3; no inputs for Janyu CCPS or Fermionic; Note 40 and Note 36 small-print conflicts; associate status at 6.13% unexplained | Notes 38, 40, 36, 10(a); Cons Note 46 | YELLOW |
| 16 | Sanctioned working capital limits 76,500 (FY25 43,500) from the Directors' report; Note 39 undrawn differs by 2,500.00 in FY25 | Directors' report pp.192-193; Note 39, p.257 | YELLOW (cross-reference) |

Items for the final block (carry to Pass 3): receivables_trend should say "improving on balance, with the ageing schedule internally inconsistent (P2-3)"; the FLAG-CASH test stays open on ARCPL (19,579.28) and the old-balance cover (P2-5).

Management questions arising (new): (1) Why is the Navictronics 912.00 not in investing cash flow? (2) What is the ageing basis, and why does the more-than-3-year bucket exceed the prior year's more-than-2-year total? (3) Who supplied the 1,824.00 intangible to Navictronics? (4) Why are the unsold Janyu CCPS at cost after a sale at about Rs 1,859 per share? (5) What is behind ARCPL's 8,831.13 other financial liabilities and 26,500 limit, and who else guarantees it?

---
## ERRATA (appended by the orchestrator from the stage agent reply; these govern over the text above)

1. Section 4, first bullet, carries a garbled figure ("69,342.41 net of nothing, i.e. 70,174.0 gross"). The correct figure is current gross receivables of 70,173.99 (Rs Lakhs; Note 9(b), p.232), all of it past "due" on the report columns, since "Not due" 651.06 is the non-current item.
2. Coverage statement. The header and section 19 say the consolidated notes were re-read in full. Cons Notes 39 to 43 (financial instruments, risk, capital, ratios) were NOT re-read in this pass; they were read only through the Pass 1 extracts. All other consolidated notes cited were read at source. Pass 3 skims Cons Notes 39 to 43 for differences from the standalone versions.
