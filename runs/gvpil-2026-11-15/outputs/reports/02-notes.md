# Stage 2 Notes Triple Pass: PASS 3 (pattern pass) and CONSOLIDATION
Company: GE Power India Limited (GVPIL) | Run date: 2026-11-15 | Model: claude-sonnet-5-5

## Conventions
- UNIT: INR million ("INR M"), as printed on the face of both annual reports ("All amounts in H million"). Nothing is converted. Stage 10 converts once.
- PAGE: "p.N" is the "[page N]" marker in Annual_Report_2026.txt (AR26). "L N" is a line number in that text file. Printed folio = marker minus 3. AR25 = Annual_Report_2025.txt.
- "(calc)" is my arithmetic on anchored inputs. "(inference)" is my reading, not a filed statement. Pages outside the Notes (Notice, Board's Report) are marked "outside notes".
- Ratings: GREEN clean, YELLOW watch, RED red flag.

## PASS 3: PATTERN PASS

### 3.0 The three items Pass 2 left open

#### 3.0.1 Where the group royalty outside the P&L royalty line is booked: NOT STATED, and the notes do not let me place it
- Facts. The P&L line "Royalty and trademark fee" is INR M 125.7 (FY25 INR M 121.5), inside Other expenses (Note 33, p.168, L 11755). The related-party table prints INR M 435.7 (305.1 + 110.1 + 20.5) for FY26 under the same heading (Note 36, p.180, L 12383 to 12393). Gap INR M 310.0 (calc). Pass 2 found the gap in three years (about 381, 382, 310).
- Search result. The word "royalty" appears only twice in the standalone set: Note 33 and Note 36 (L 11755, L 12383). The words trademark, technology fee, know-how and licence fee give no other expense line. Accounting policy Note 2.12 and Note 29 (cost of materials and erection services INR M 7,765.2) say nothing about royalty. So the filing names no booking location.
- Candidates the notes allow (all inference, none confirmed):
  1. Project cost, inside "Project materials and erection services" INR M 2,528.0 or raw materials INR M 5,237.2 (Note 29, p.167). Under cost-to-cost this would pass into cost of sales as incurred.
  2. "Reimbursement of expenses" INR M 362.7 (FY25 256.3) inside Other expenses (Note 33, p.168). This line is not tied to royalty by any text.
  3. Amounts in Note 36 on a different basis (gross of tax, or invoiced and not charged in the year). The Note 36 header says "Particulars", no basis is given.
- Reading the filing supports. The royalty burden on the P&L is at least INR M 125.7 and at most INR M 435.7 (calc). The notes cannot narrow it. A real cost sits somewhere in the P&L, because the related-party table is a transaction table and the parties are paid by contract. A cost that is real and sits in cost of materials does not change profit before exceptional items. A cost that is in the table but not in the P&L would have to be capitalised into inventory or contract assets, which the notes do not show. I rate this YELLOW (disclosure gap), not RED (no sign of profit overstatement).
- The Step-1 lead "Rs 13.21 cr for FY25" ties to neither figure (INR M 121.5 and INR M 514.5). It stays unverified.
- Pass 1 and Pass 2 agree on the gap. Pass 2 adds that it is structural over three years. I accept that.

#### 3.0.2 The repeated "slump sale" deductions in the provision roll-forwards: label cannot be right for the full amount; P&L effect NOT STATED
- Facts (Note 26, p.164 to 165, L 11569 to 11610).
  - Warranty, FY26: opening INR M 879.1; addition net of reversal INR M (114.2); "Less: Liabilities transferred under slump sale (refer note 47)" INR M (185.0); closing INR M 579.9. FY25 column: 1,189.3; (125.2); (185.0); 879.1.
  - Loss orders, FY26: opening INR M 216.9; "Reversal during the year, net of addition" INR M 144.6; slump sale INR M (137.7); closing INR M 223.8. FY25: 396.8; (42.2); (137.7); 216.9.
  - Contingencies and others: slump-sale line "-" in both years.
- The slump sales closed on 30 Sep 2024 and 31 Mar 2025, both in FY25 (Note 47(i), (ii), p.194). A FY26 transfer under those sales is not possible.
- Tests I ran.
  1. Arithmetic. FY26 warranty 879.1 - 114.2 - 185.0 = 579.9 and loss orders 216.9 + 144.6 - 137.7 = 223.8 (calc). Both tie to the balance sheet (p.131; Note 21, 26). If the deduction were removed, the closing balances would not tie. So the deduction is a real movement of INR M 185.0 and INR M 137.7 in the FY26 balances. Only the label is in doubt.
  2. Value match. The two values equal the FY25 values to the first decimal in both columns. Real transfers in two different years do not usually match to the first decimal. That points to a copy-forward of the label and the number (inference).
  3. Durgapur capacity. Held-for-sale provisions are INR M 172.8 non-current and INR M 107.5 current, INR M 280.3 in total (Note 47(v)(a), p.195, L 13292 and 13319). The two deductions total INR M 322.7 (calc). That is INR M 42.4 above the whole Durgapur provision block, and the block also holds employee provisions. So Durgapur cannot explain both lines.
  4. Gas and Hydro blocks. Gas provisions 55.6 + 225.1 = 280.7 and Hydro 309.9 + 518.5 = 828.4 (Note 47(v)(b), (c), p.196 to 197, L 13392 to 13508, calc). Neither equals 185.0, 137.7 or 322.7. The FY25 transfers were not these two lines alone.
  5. Sign of the loss-order row. The label reads "Reversal during the year, net of addition". In FY25 the entry is (42.2), which lowers the balance. In FY26 the entry is +144.6, which raises it. The same label carries opposite signs, so FY26 is a net addition of INR M 144.6 on arithmetic (calc).
- Two readings, one separating observation.
  - Reading A (utilisation or reclass): the deductions are real non-cash movements (claims utilised against the provision, or provisions moved to held for sale) with a wrong label. No P&L effect.
  - Reading B (release): the deductions are releases to the P&L labelled by mistake. The FY26 warranty reduction is INR M 299.2 (calc), which would support profit.
  - Separating observation: the movement of the warranty provision by head in the Q1 and Q2 FY27 reports, or the management answer on what the INR M 185.0 and INR M 137.7 are. The filing cannot separate them.
- What the filing supports. Reading A is more likely for the Durgapur part, because provisions did move to held for sale (non-current provisions fell INR M 380.3, balance sheet; cash flow adjustment INR M (380.1), p.133). Reading B cannot be excluded for the INR M 42.4 or more above Durgapur capacity. I carry the P&L effect as NOT STATED and bound it at between nil and INR M 299.2 on the warranty side (calc). I do not call it earnings management. It is a label and tie-out defect with an unknown size.
- Pass 1 said "up to INR M 299.2 of possible support". Pass 2 repeated it. Pass 3 narrows: the loss-order row moved the other way by INR M 144.6, so if both rows were P&L releases the net bound is smaller than 299.2 (299.2 less the loss-order net addition of 144.6 is INR M 154.6, calc, only if the loss-order addition were a P&L charge, which the note does not say). The band is NOT STATED, kept YELLOW.

#### 3.0.3 The INR M 247.0 internal billing from Durgapur: the filing's own structure shows continuing cost carries no matching charge
- Facts. Note 47(vi), p.198 (L 13525 to 13565): gross revenue INR M 247.0 less internal revenue INR M (247.0) = net revenue nil. Footnote: "Revenue from operations of the Durgapur undertaking is only from internal billing to the Company and does not pertain to external customers, hence, the same has been deducted". Durgapur expenses INR M 548.0 (15.1 + 374.4 + 0.9 + 3.9 + 153.7, calc, ties). Loss before exceptional INR M (548.0). Discontinued cash flow starts at loss before tax INR M (451.0) = (698.0) + 247.0 (calc).
- Why GVPIL is one legal entity. This is a standalone entity. Durgapur is a division of it. "Internal billing" between a division and the rest of the same legal entity is not a transaction with a third party and cancels in the entity's P&L.
- Test that settles the reading (calc). Total standalone profit before tax FY26 = continuing INR M 3,123.3 + discontinued INR M (698.0) = INR M 2,425.3, which equals the profit before tax in the tax reconciliation (Note 48, p.200). For FY25, Pass 2 B4 found that only cost lines moved between the AR25 original P&L and the AR26 re-presentation (cost of materials by INR M 17.4, employee cost by INR M 399.4, other expenses by INR M 181.6, depreciation by INR M 6.4; total INR M 604.8) and no revenue line moved. AR25 was a whole-entity P&L with no divisional billing in its revenue. So the entity had no internal revenue in its revenue line and no internal purchase in its cost-of-materials line. The re-presentation moved only Durgapur's own external costs.
- Conclusion supported by the filing. Continuing cost of materials INR M 7,765.2 does not include the INR M 247.0. The INR M 247.0 is a memo line in the discontinued cash flow. The question Pass 2 left open resolves to NO charge in continuing cost.
- What follows (inference, flagged). Durgapur makes goods worth INR M 247.0 (at transfer price) for the continuing business. Its full cost, INR M 548.0 in FY26 (INR M 604.8 in FY25), sits in discontinued operations. The continuing P&L therefore shows revenue that Durgapur helped earn, with none of Durgapur's cost against it. After the demerger, GVPIL must buy those goods from JSW Energy, make them elsewhere or stop. The cost would then enter the continuing P&L. The filing gives no price for such a supply arrangement. NOT FOUND IN DOCUMENT.
- Scale (calc). INR M 247.0 is 1.9% of revenue INR M 12,692.7 and 7.3% of profit before exceptional items INR M 3,399.0. If the full INR M 548.0 were instead borne by continuing, the profit before exceptional items would be INR M 2,851.0. These are bounds, not forecasts.
- Rating YELLOW. Upgrade from the Pass 2 "open" status: closed on structure. The residual risk is post-demerger cost, not misstatement.

### 3.1 Contradictions between notes and numbers that do not match the statements

| # | Pattern | Evidence | Rating |
|---|---|---|---|
| P3-1 | ICD security: Notes silent, Notice says secured by GE Vernova Inc. | Note 16 (p.158) and Note 36 (p.181) give no security. Notice (outside notes) states "The said loan is secured through Parent Corporate Guarantee from GE Vernova Inc." (L 21301). The same Notice asks members to approve a new guarantee of INR M 10,000 "to the Company for an amount lent under the Cash pool arrangement" (L 19881; L 21419 to 21422, "100% coverage"). A resolution to approve a guarantee for the lending implies the guarantee is proposed or being renewed. The Notes and the Notice do not say whether the present INR M 4,500.0 is covered today. | YELLOW |
| P3-2 | ICD absent from Note 42 and the Note 43 credit text | Pass 2 A4 stands. I re-checked: the Note 43(A)(ii)(a) "H 360 million" ties to Note 8 + Note 17 less deposits, excluding the loan (calc). Note 42 amortised-cost total INR M 12,140.0 excludes it. | YELLOW |
| P3-3 | Notice internal arithmetic on the ICD rate | The Notice states a current rate "~6.71%" (L 21304) and elsewhere "~8.00%" against 6.07% + 0.64% (Pass 2 B1). Note 16 says 5.49% to 6.35%. Three rates for one loan. | YELLOW (minor) |
| P3-4 | Guarantee direction: Note 36 label vs Notice | Note 36 says "Corporate Guarantee issued" under GE Vernova Inc. (p.182, L 12522 to 12524). The Notice says the parent gives guarantees to the banks for the Company's limits (L 21576 to 21577). The Note label reads as if the Company issued it. The Notice settles the direction as received. Pass 2 B2 stands. The label is a disclosure defect. | YELLOW |
| P3-5 | Note 53 BHEL reversal quoted three ways | 1,050.5 / 1,016.6 / 1,123.8. Pass 2 B7 reconciled the pieces: gross BHEL release, net P&L line, allowance closing minus opening. INR M 46.1 stays unexplained after bad debts INR M 61.1 (calc). | YELLOW |
| P3-6 | Deferred tax note adds the DTL | Unrecognised INR M 1,983.6 = 1,895.2 + 88.4 (calc). Pass 2 B10 stands. | YELLOW (footing) |
| P3-7 | NGSL footnote | The "H124.8 million / H 57.5 million" footnote is unchanged from AR25. Carried error. Pass 2 stands. | GREEN (no P&L effect) |
| P3-8 | Plan assets INR M 677.1 (p.171) vs INR M 668.1 (p.170) | A INR M 9.0 gap inside Note 34 (Pass 1). Not explained. | YELLOW (minor) |
| P3-9 | Cash-flow FX add-back INR M 492.2 vs Note 33 net FX loss INR M 42.5 | Pass 1 flagged. Pass 3 re-read: the cash flow adjustment is unrealised FX on the whole entity including balance sheet items (derivative mark-to-market, payables). No note reconciles it. | YELLOW |
| P3-10 | Tax note "continuing and discontinued" mixed | Note 48 reconciles total profit before tax INR M 2,425.3 (p.200). Note 47 tax INR M 61.7 split: current INR M 61.7 incl. discontinued (0.6). Ties. | GREEN |

### 3.2 Deliberately vague or minimal disclosure (compared with the detail given elsewhere)
- Contingent liabilities (Note 39, p.185): four category totals INR M 4,575.9, no case, forum or stage; against a Note 51 or Note 52 level of detail for insurance claims. Largest item INR M 2,036.7 is 37.5% of net worth (calc).
- Provision for contingencies and others INR M 1,901.3 (Note 26): "mainly probable claims". No case behind it. The provision is 35.0% of equity (calc).
- Customer concentration: top two customers 38.6% (Note 35, p.176), names and balances NOT DISCLOSED.
- Durgapur demerger: consideration and accounting NOT in the notes (Note 47(iii)); the share ratio is outside notes (Board's Report p.28).
- Parent guarantee peak INR M 20,432 is in the Notice only (L 21581); Note 36 shows only the year-end INR M 7,977.6.
- RPO scope (Note 27, p.166): "not practical to define" timing; scope of Durgapur and intra-group orders NOT STATED.

### 3.3 Restatements and reclassifications
- FY25 continuing result: loss before tax INR M (380.2) in AR25 became profit INR M 224.6 in AR26 by moving INR M 604.8 of Durgapur cost (Pass 2 B4). FY24 continuing was not re-presented (loss INR M (1,423.7), AR25 p.168).
- FY25 line re-presentations: royalty 132.1 to 121.5; reimbursement 270.0 to 256.3; EDP 286.6 to 248.7; security 35.2 to 23.2 (Pass 2).
- Note 36 FY25 column was NOT re-presented (still carries Gas and Hydro flows). Pass 1 YoY percentages on related-party flows are not like-for-like. Pass 2 A2 stands and I adopt it.
- Note 26 FY26 column repeats FY25 "slump sale" values (3.0.2).

### 3.4 Events after the balance sheet date
- Dividend of INR 7 per share, INR M 470.6, recommended 11 May 2026 (Note 61, p.204). The equity statement shows no dividend in either year (p.135). Cash cost is 10.0% of FY26 CFO (calc).
- CFO resignation effective 13 May 2026 and company secretary resignation effective 2 Apr 2026 (Note 36, p.177). Two statutory KMP posts open at the date of the accounts (11 May 2026).
- BSE "no adverse observations" and NSE "no objection" for the JSW scheme, 1 Apr 2026 (Board's Report p.28, outside notes).
- No event is stated to alter the figures. No separate subsequent-events note exists.

### 3.5 Going concern language
- NONE adverse. The only adverse-sounding items are in routine form. The auditor's CARO clause (xix) reports no material uncertainty on meeting liabilities for a year (auditor's report p.130 to 131, outside notes; L 8837). Clause (xvii) records cash losses of INR 824.15 million in the preceding year (auditor's report p.130, outside notes; Pass 1). The Board's Report (L 1685) states no order impacting going-concern status. The phrase "going concern" elsewhere refers to the slump-sale and demerger transfers.
- The Board's DTA text ("delay in order backlog execution", "lower order intake than expected", Note 9 p.155) is weaker business language than any going-concern text, and it sits beside a year with INR M 3,399.0 profit before exceptional items.

### 3.6 Where Pass 1 and Pass 2 disagree: the reading the filing supports

| Topic | Pass 1 | Pass 2 | Reading Pass 3 adopts | Why |
|---|---|---|---|---|
| ICD INR M 4,500.0 rating | RED | YELLOW (disclosure); RED to YELLOW on economics | YELLOW with a disclosure-defect flag. The balance is 21.4% of total assets (calc). | Notice (outside notes, L 21301, L 21419) says secured by a BBB parent guarantee; Notes silent. The Notes alone would leave RED. The coverage of the existing balance is not confirmed. |
| Net cash | INR M 8,803.1 with nil debt | INR M 8,473.1 with ICD, 3,973.1 without; debt INR M 330.0 | Pass 2. | Notice (L 21570 to 21571) says INR M 330 of fund-based limits utilised, and Note 43 undrawn bank limit INR M 280.0 equals 610 - 330. Equal figures support the bank-draw reading. The Notes do not name the lender. |
| RPO fall 38.9% | RED | YELLOW on trend (Mar-24 15,870; Mar-25 26,623; Mar-26 16,278) | Pass 2 on trend, with the order-flow question kept. Implied FY26 additions INR M 2,347.7 (calc; book-to-bill 0.18). | AR25 shows the Mar-25 base was a spike. But Mar-26 sits at 1.28 times revenue against 1.53 times at Mar-24, and the derived inflow is low. YELLOW with a flag, not RED. |
| Related-party YoY | Used raw | Not like-for-like | Pass 2. | FY25 Note 36 column was not re-presented. |
| Core margin | 12.4% single figure | 12.4% to 16.1% range | Range stands: 12.4% (all other income out) to 16.1% (cost recoveries and rent kept), against 4.5% in FY25 on the 16.1% basis (calc). | The cross-charge income INR M 318.4 equals the group payments INR M 318.4 in Note 36 (L 12395 to 12400), which supports keeping recoveries in the 16.1% basis. The FY25 pair does not match, so the match may be chance. |
| Unrecognised DTA | INR M 1,983.6, down INR M 599.0 | Footing error; netted 1,806.8, down INR M 471.6 | Pass 2. | Arithmetic ties exactly in FY26 and FY25 (calc). |
| NGSL footnote | stale | carried error from AR25 | Pass 2. | Same text in AR25 (L 16924). |
| Provision "slump sale" | label wrong, P&L effect not stated | deduction exceeds Durgapur block, up to INR M 299.2 | See 3.0.2. Label cannot be right in full; P&L effect NOT STATED. | Closing balances tie only with the deduction; value is identical in both years; INR M 322.7 exceeds INR M 280.3. |

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | INR M 4,500.0 demand ICD to LM Wind Power Blades (India), a fellow subsidiary, at the old approved cap; 21.4% of total assets, 106% of cash and equivalents (calc). Absent from Note 42 and the Note 43 credit text. Notice (outside notes) says a GE Vernova Inc. guarantee (BBB / BBB+) secures it and asks to raise the cap to INR M 10,000. | 16, 36, 42, 43; Notice L 21301, L 19881 | YELLOW (RED on the Notes alone) | Largest non-operating asset, an unrated group borrower, no ECL assessment in the notes. The Step-1 "net cash" depends on it. |
| 2 | Profit before exceptional items INR M 3,399.0 includes a receivable-loss reversal INR M 1,016.6 (BHEL), write-backs INR M 240.9, insurance INR M 184.2 and group-sourced income INR M 851.9 (calc). The ECL swing (1,320.0) plus other income (+433.5) is 55.3% of the INR M 3,174.4 step-up from FY25. Core margin 4.5% (FY25) to 12.4% to 16.1% (FY26) (calc). | 28, 33, 36, 53 | RED | The reported 27.0% margin is not run-rate. Real gains exist in material cost (67.3% to 60.2% of revenue) and employee cost (18.5% to 14.5%). |
| 3 | CFO INR M 4,692.5 is a working-capital release: receivables +5,136.0, offset by customer advances and billing in excess down INR M 2,106.6 (calc). Receivable unwind is two years old: gross 18,950.3, 13,489.2, 8,260.5; retention 11,965.9, 8,574.1, 4,751.7. | 13, 25; cash flow p.133 | YELLOW | The collection cannot repeat at this scale. Aged over 6 months share rose 8.4% to 15.9%; the sticky part remains. |
| 4 | RPO INR M 16,278 (Mar-26), INR M 26,623 (Mar-25), INR M 15,870 (Mar-24). Derived FY26 additions about INR M 2,347.7, book-to-bill 0.18 (calc). Scope not stated. | 27 | YELLOW (flag) | Revenue grew 21.2% on a book that is back at the Mar-24 level. Order flow decides whether FY26 margin repeats. |
| 5 | Durgapur: continuing P&L bears none of Durgapur's cost (INR M 548.0 FY26; INR M 604.8 FY25). FY25 continuing profit became INR M 224.6 only after the move. Internal billing INR M 247.0 is not in continuing cost. Post-demerger cost to supply those goods NOT FOUND. | 47(iii), (v), (vi) | YELLOW | Continuing margin is flattered relative to the business as run. A supply cost can return after the JSW demerger. |
| 6 | Parent dependency: guarantee given by GE Vernova Inc. for bank lines INR M 7,977.6 used (49.9% of INR M 16,000 needed, calc); peak INR M 20,432. Debt is INR M 330.0 bank fund-based draw inside held-for-sale, not nil. Net cash INR M 8,473.1 with ICD, INR M 3,973.1 without (calc). | 36, 43, 46, 47(v); Notice L 21569 to 21583 | YELLOW | All bid capacity rests on one guarantor. Note 36 label says "issued"; the Notice shows received. |
| 7 | Royalty: P&L line INR M 125.7 against related-party table INR M 435.7; gap INR M 310.0 (INR M 380.9 FY24, INR M 382.4 FY25). Booking location NOT STATED. | 33, 36 | YELLOW | Group royalty burden is not visible in one line. Profit effect unknown but real cost is likely inside cost of materials (inference). |
| 8 | Provision roll-forwards repeat the FY25 "slump sale" deductions (warranty INR M 185.0; loss orders INR M 137.7). Total INR M 322.7 exceeds the Durgapur provision block INR M 280.3. Warranty provision down 34.0% (calc) while revenue rose 21.2%. P&L effect NOT STATED. | 26, 47(v) | YELLOW | Possible release up to INR M 299.2 on warranty; cannot be proved or excluded. |
| 9 | Contingent liabilities INR M 4,575.9 (84.2% of net worth; sales tax INR M 2,036.7 alone 37.5%), no case or forum detail, no provision beyond INR M 1,901.3 for "probable claims". | 39, 26 | YELLOW | Equity rebuilt (INR M 573.5 to 5,437.7) so the ratio fell, but the amounts grew 5.6% and 7.1%. |
| 10 | Customer concentration: top two customers 38.6% of revenue (34.8% FY25); NGSL JV INR M 1,111.6 (8.8%, 4.2 times FY25), receivable INR M 703.0, advances INR M 833.0 above the INR M 677.9 advance line (JV 53.1% of gross advances, calc). | 35, 36, 25 | YELLOW | The JV is customer, supplier, receivable and advance giver. Names of the top two not disclosed. |
| 11 | Hydro sold for INR 1 with net liabilities INR M 2,978.9; policy choice (Note 2.20) booked gain INR M 2,369.9 and capital reserve INR M 609.0. Durgapur demerger to JSW: negative net assets INR M (548.7); accounting not stated. | 2.20, 47 | YELLOW | Common-control policy lets management choose the P&L or equity route. Closed names are FY25 events. |
| 12 | Inventory +69.9% against revenue +21.2% (71 days against 46, calc); raw materials +120.7%. Payables overdue share fell 65.9% to 41.3%. FX payables INR M 535.9 over 6 months without stated RBI approval. | 12, 23 | YELLOW | Stock build and payables cleanup absorb cash next year. |
| 13 | Unrecognised DTA pool INR M 1,806.8 (netted; note shows 1,983.6) kept off the books because of "lower order intake than expected" (Board); effective tax rate 2.5% (calc). | 9, 48 | YELLOW | Cash tax is low only while losses last. Board language on orders sits against the profit headline. |
| 14 | Labour Codes exceptional INR M 425.7 (275.7 continuing, 150.0 discontinued) booked on draft rules; gratuity past service cost INR M 320.7. PF trust exemption surrendered from 1 Apr 2026, transfer pending. Attrition assumption 5.58% against 8.09%. | 34, 47(iv), 59 | YELLOW | Open-ended; final rules can add cost. |
| 15 | Other expenses ex-ECL +26.3% (INR M +340.0): miscellaneous INR M 299.3 against 20.7, legal INR M 234.8 against 77.3, unexplained; allowance on doubtful supplier advances +INR M 89.9. Two statutory KMP posts open. | 33, 18, 36 | YELLOW | Unexplained cost jumps lower reliance on line detail; governance gap at the accounts date. |

### B. ACCOUNTING QUALITY SCORE: 6 / 10

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Cost-to-cost over time, KAM on cost to complete. Revenue from prior-period estimates +INR M 70.3 (FY25 INR M (501.0)). RPO scope not stated. |
| Expense capitalisation honesty | 8 | Capex INR M 21.3 outflow; PPE additions INR M 37.9; no capitalisation of costs seen. Plant lives up to 50 years on a INR M 93.8 net block. |
| Provisioning adequacy | 5 | Receivable allowance 7.7% of gross at the bottom of the 7.3% to 13.1% stated range; INR M 976.1 aged over 6 months good-classed; warranty down 34.0%; slump-sale label unresolved; contingencies "probable claims" with no cases. |
| RPT fairness | 5 | Heavy group flows; Hydro at INR 1; INR M 4,500.0 loan outside Notes 42 and 43; royalty gap unexplained; guarantee label inverted. Parent support is real. |
| Disclosure transparency | 5 | No contingent liability detail, no customer names, FY25 related-party column not re-presented, footing error in Note 9, carried NGSL footnote error. Notice fills several gaps. |
| Consistency with prior years | 6 | FY25 re-presentation favourable to continuing optic; label copy-forward in Note 26; policies unchanged. |
| OVERALL | 6 | Balance sheet is clean (no debt of substance, no impairment). Earnings quality and tie-out defects hold the score down. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Order base: RPO back at Mar-24 level, derived FY26 additions INR M 2,347.7 | High | Q1 and Q2 FY27 order inflow and RPO; concall (NOT FOUND for Q1, Q2 FY27) | FY27 revenue and margin |
| FY26 margin not run-rate: reversal, write-backs and group income are 55.3% of the step-up | High | Core margin 12.4% to 16.1% (calc) in H1 FY27 results without those items | H1 FY27 results |
| Group ICD INR M 4,500.0 (cap to INR M 10,000) | Medium-high | Guarantee in place for the loan; Note 42 and 43 treatment in FY27 notes; balance against cap | Next AGM vote and FY27 notes |
| Parent dependency for bank lines (INR M 16,000 needed) | Medium | Guarantee renewals; any change in GE Vernova Inc. support; undrawn bank limit INR M 280.0 | Any bid season |
| Post-demerger cost of Durgapur supply (INR M 247.0 of goods; INR M 548.0 of cost) | Medium | Supply agreement with JSW Energy; employee numbers moved; cost-of-materials trend after completion | On completion, within 12 months of year end |
| Contingent liabilities INR M 4,575.9 and provision INR M 1,901.3 | Medium | Case outcomes; forum detail; growth rate (+7.1%) | Any year; unquantifiable timing |
| Working-capital reversal: inventory +69.9%, customer advances and billing in excess down INR M 2,106.6 | Medium | Inventory days; CFO excluding settlement receipts | FY27 CFO |
| HPGC INR M 1,607.0 held in trust, Supreme Court pending since 2016 | Medium | Supreme Court listing; interest cost INR M 53.7 | Binary event; timing unknown |
| Labour Codes and PF transfer open-ended | Low-medium | Final rules; PF transfer and any shortfall | FY27 |
| DTA not recognised; tax shield finite | Low-medium | Loss pool INR M 1,147.4 brought-forward; expiry schedule NOT FOUND | When profits exceed the pool |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Is the INR M 4,500.0 cash-pool deposit with LM Wind covered today by a GE Vernova Inc. Parent Corporate Guarantee, and why is the loan absent from Note 42 and the Note 43 credit text?
2. What orders did the Company receive in FY26, and does the INR M 16,278 RPO include Durgapur or intra-group orders? Derived additions are about INR M 2,348.
3. Where is the INR M 310.0 of group royalty, shown in Note 36 but not in the INR M 125.7 P&L line, booked, and why has the gap held at about INR M 380 in FY24 and FY25?
4. What are the INR M 185.0 warranty and INR M 137.7 loss-order deductions labelled "slump sale" in the FY26 roll-forwards, and what P&L effect do they carry?
5. After the Durgapur demerger, who will make the goods billed at INR M 247.0 internally, at what price, and which cost line will carry INR M 548.0 of Durgapur cost?

### E. NOTES-BASED RED FLAGS

Earnings management and aggressive accounting: none proved. Items near the line:
- Reversal of loss allowance INR M 1,016.6 inside profit before exceptional items (tied to BHEL cash INR M 3,430.6 against INR M 3,400 agreed, Note 53 p.202). Cash-backed, not discretionary. It is non-recurring.
- Provision "slump sale" copy-forward: INR M 322.7 of movement with a wrong label; P&L effect NOT STATED. A reading B release would add up to INR M 299.2 to FY26 profit.
- FY25 comparative moved by INR M 604.8 of Durgapur cost to give continuing profit of INR M 224.6; the same lens removes INR M 548.0 of cost from FY26.
- Common-control policy (Note 2.20) allowed a gain of INR M 2,369.9 on an INR 1 sale. FY25 event, closed.
- ICD omitted from the financial instrument classification and credit-risk text.
- Undisclosed risk indicators: contingent liability detail, top two customer names, RPO scope, royalty booking, Durgapur consideration.
- No going-concern, covenant or impairment signal. No related-party loan to promoter family.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: the FY26 profit step-up leans on a receivable reversal, other income and a Durgapur cost shift, while the order base (RPO INR M 16,278) is back at the Mar-24 level. Key strength: no debt of substance, receivables unwinding with cash received (INR M 3,430.6 from BHEL), and no going-concern or impairment signal. Overall accounting quality: 6/10.

PASS 3 FINDINGS SUMMARY (new in this pass): (1) the INR M 247.0 internal billing is not in continuing cost, shown by the entity-level tie of profit before tax and the cost-only FY25 re-presentation; post-demerger supply cost is the real exposure. (2) The loss-order row carries opposite signs under one label, so FY26 is a net addition of INR M 144.6. (3) The "slump sale" deductions cannot be Durgapur in full (INR M 322.7 against 280.3). (4) The royalty booking location cannot be found anywhere in the notes. (5) The ICD guarantee is proposed or renewed in the Notice, so coverage of the present balance is unconfirmed.

```yaml
stage: B02-notes
company: "GVPIL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "concalls: no Q1 FY27 or Q2 FY27 earnings-call transcript"
  - "shareholding: screener-derived table only; filed pattern and pledge detail absent"
  - "screening: only Data_Sheet CSVs populated"
  - "research: none; prospectus not expected (long-listed)"
  - "notes: FY24 comparatives from AR25 as first reported (include Gas/Hydro); not like-for-like with continuing FY25/FY26"
  - "notes: continuing-basis FY25 related-party table NOT FOUND (Note 36 FY25 column not re-presented)"
  - "notes: contingent liability stage/forum, customer names, Durgapur demerger consideration and accounting, MAT credit, loss expiry schedule NOT FOUND IN DOCUMENT"
  - "notes: royalty booking location for the INR M 310.0 gap NOT STATED; P&L effect of Note 26 slump-sale deductions NOT STATED; post-demerger Durgapur supply price NOT FOUND"
  - "notes: whether the Parent Corporate Guarantee covers the existing INR M 4,500.0 ICD is not stated in the Notes (Notice, outside notes, reads as yes); GVPIL order inflow NOT FOUND (RPO-derived only)"
flags:
  - {type: FLAG-RPT, reason: "ICD INR M 4,500.0 to LM Wind Power Blades (India) at the approved cap (cap to be raised to INR M 10,000); absent from Note 42 and Note 43 credit text; Notice (outside notes) says GE Vernova Inc. guarantee secures it; coverage of present balance not confirmed; guarantee label in Note 36 reads as issued but is received; royalty gap INR M 310.0 unreconciled"}
  - {type: FLAG-EARNINGS, reason: "55.3% of the INR M 3,174.4 profit step-up is the ECL swing (1,320.0) plus other income (433.5); group-sourced income INR M 851.9 = 25.1% of profit before exceptional items; core margin 4.5% FY25 to 12.4%-16.1% FY26 (calc); FY25 continuing result re-presented by INR M 604.8 of Durgapur cost"}
  - {type: FLAG-ORDERS, reason: "RPO INR M 15,870 / 26,623 / 16,278 (Mar-24/25/26); derived FY26 order additions INR M 2,347.7, book-to-bill 0.18 (calc; RPO scope not stated)"}
  - {type: FLAG-PROVISION, reason: "Note 26 FY26 warranty (185.0) and loss-order (137.7) 'slump sale' deductions repeat FY25 values; total 322.7 exceeds Durgapur provision block 280.3; closing balances tie only with them; P&L effect NOT STATED; loss-order row sign inverted between years"}
  - {type: FLAG-DEMERGER, reason: "Durgapur cost INR M 548.0 FY26 (604.8 FY25) sits outside continuing P&L; INR M 247.0 internal billing not charged to continuing cost; post-demerger supply cost NOT FOUND; consideration and accounting of net liabilities INR M 548.7 not in Notes"}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "INR M 4,500.0 demand ICD to LM Wind Power Blades (India) at the approved cap; 21.4% of total assets, 106% of cash (calc); absent from Note 42 and Note 43 credit text; Notice (outside notes) says GE Vernova Inc. guarantee secures it, cap to rise to INR M 10,000", note_ref: "Notes 16, 36, 42, 43 p.158, p.181, p.186-189; Notice L 21301, L 19881", rating: "YELLOW (RED on Notes alone)", why: "Largest non-operating asset, unrated group borrower, no ECL assessment in the Notes; Step-1 net cash depends on it"}
  - {rank: 2, finding: "Profit before exceptional items INR M 3,399.0 includes reversal INR M 1,016.6, write-backs INR M 240.9, insurance INR M 184.2, group-sourced income INR M 851.9; ECL swing + other income = 55.3% of the INR M 3,174.4 step-up; core margin 4.5% FY25 to 12.4%-16.1% FY26 (calc)", note_ref: "Notes 28, 33, 36, 53 p.167-168, p.180-181, p.202", rating: RED, why: "Reported 27.0% margin is not run-rate; real gains in material cost 67.3% to 60.2% and employee cost 18.5% to 14.5% of revenue"}
  - {rank: 3, finding: "CFO INR M 4,692.5 is a working-capital release: receivables +5,136.0 vs advances and billing in excess down 2,106.6; receivable unwind two years old (gross 18,950.3 / 13,489.2 / 8,260.5)", note_ref: "Notes 13, 25 p.156-157, p.164; cash flow p.133", rating: YELLOW, why: "Cannot repeat at this scale; aged >6m share 8.4% to 15.9%"}
  - {rank: 4, finding: "RPO INR M 15,870 / 26,623 / 16,278; derived FY26 order additions INR M 2,347.7, book-to-bill 0.18 (calc)", note_ref: "Note 27 p.166; AR25 L 12521", rating: YELLOW, why: "Book is back at Mar-24 level while revenue grew 21.2%; scope not stated"}
  - {rank: 5, finding: "Durgapur cost INR M 548.0 (FY25 604.8) sits outside continuing P&L; INR M 247.0 internal billing not charged to continuing cost; post-demerger supply cost NOT FOUND", note_ref: "Note 47(iii), (v), (vi) p.194-198", rating: YELLOW, why: "Continuing margin flattered relative to business as run; cost can return after JSW demerger"}
  - {rank: 6, finding: "Parent guarantee for bank lines INR M 7,977.6 used (49.9% of INR M 16,000 needed; peak 20,432); debt is INR M 330.0 bank fund-based draw, not nil; net cash INR M 8,473.1 with ICD, 3,973.1 without", note_ref: "Notes 36, 43, 46, 47(v) p.182, p.190, p.193, p.195; Notice L 21569-21583", rating: YELLOW, why: "All bid capacity rests on one guarantor; Note 36 label reads as issued, Notice shows received"}
  - {rank: 7, finding: "Royalty: P&L INR M 125.7 vs related-party table INR M 435.7; gap INR M 310.0 (380.9 FY24, 382.4 FY25); booking location NOT STATED", note_ref: "Notes 33, 36 p.168, p.180", rating: YELLOW, why: "Group royalty burden not visible in one line; likely inside cost of materials (inference)"}
  - {rank: 8, finding: "Note 26 'slump sale' deductions (warranty 185.0, loss orders 137.7) repeat FY25 values; total 322.7 > Durgapur block 280.3; warranty provision -34.0%; P&L effect NOT STATED", note_ref: "Notes 26, 47(v) p.164-165, p.195", rating: YELLOW, why: "Possible release up to INR M 299.2 on warranty; cannot be proved or excluded"}
  - {rank: 9, finding: "Contingent liabilities INR M 4,575.9 = 84.2% of net worth; sales tax 2,036.7 = 37.5%; no case or forum detail; provision for contingencies INR M 1,901.3", note_ref: "Notes 39, 26 p.185, p.165", rating: YELLOW, why: "Amounts grew 5.6% and 7.1%; ratio fell only because equity rebuilt"}
  - {rank: 10, finding: "Top two customers 38.6% (34.8% FY25); NGSL JV revenue INR M 1,111.6 (8.8%), receivable 703.0, advances 833.0 above the 677.9 advance line", note_ref: "Notes 35, 36, 25 p.176, p.181-183, p.164", rating: YELLOW, why: "JV is customer, supplier, receivable and advance giver; names not disclosed"}
  - {rank: 11, finding: "Hydro sold for INR 1 (net liabilities INR M 2,978.9); Note 2.20 policy booked gain 2,369.9 and capital reserve 609.0; Durgapur net liabilities INR M 548.7, accounting not stated", note_ref: "Notes 2.20, 47 p.148, p.194-195", rating: YELLOW, why: "Common-control policy choice; FY25 event, closed"}
  - {rank: 12, finding: "Inventory +69.9% vs revenue +21.2% (71 vs 46 days, calc); FX payables INR M 535.9 over 6 months without stated RBI approval", note_ref: "Notes 12, 23 p.156, p.163", rating: YELLOW, why: "Stock build absorbs cash; regulatory exposure small"}
  - {rank: 13, finding: "Unrecognised DTA pool INR M 1,806.8 netted (note shows 1,983.6, DTL added); Board cites lower order intake; effective tax rate 2.5% (calc)", note_ref: "Notes 9, 48 p.154-155, p.200", rating: YELLOW, why: "Low cash tax only while losses last; Board order language sits against profit headline"}
  - {rank: 14, finding: "Labour Codes exceptional INR M 425.7 on draft rules; gratuity past service INR M 320.7; PF trust exemption surrendered, transfer pending; attrition assumption 5.58% vs 8.09%", note_ref: "Notes 34, 47(iv), 59 p.169-175, p.195, p.204", rating: YELLOW, why: "Open-ended cost; possible shortfall on PF transfer"}
  - {rank: 15, finding: "Other expenses ex-ECL +26.3% (miscellaneous 299.3 vs 20.7; legal 234.8 vs 77.3 unexplained); CFO and company secretary posts open at accounts date", note_ref: "Notes 33, 36 p.165, p.177", rating: YELLOW, why: "Unexplained cost jumps and a governance gap"}
red_flags:
  - "Profit step-up INR M 3,174.4 is 55.3% ECL swing plus other income; reported 27.0% margin is not run-rate (core 12.4%-16.1% calc)"
  - "RPO back to Mar-24 level; derived FY26 order additions INR M 2,347.7 (book-to-bill 0.18)"
questions_for_mgmt:
  - "Is the INR M 4,500.0 cash-pool deposit with LM Wind covered today by the GE Vernova Inc. Parent Corporate Guarantee, and why is the loan absent from Note 42 and the Note 43 credit text?"
  - "What orders were received in FY26, and does the INR M 16,278 RPO include Durgapur or intra-group orders? Derived additions are about INR M 2,348."
  - "Where is the INR M 310.0 of group royalty, shown in Note 36 but not in the INR M 125.7 P&L line, booked, and why has the gap held at about INR M 380 in FY24 and FY25?"
  - "What are the INR M 185.0 warranty and INR M 137.7 loss-order deductions labelled slump sale in the FY26 roll-forwards, and what P&L effect do they carry?"
  - "After the Durgapur demerger, who will make the goods billed at INR M 247.0 internally, at what price, and which cost line will carry INR M 548.0 of Durgapur cost?"
receivables_trend: "improving, two-year unwind: gross INR M 18,950.3 (Mar-24) / 13,489.2 / 8,260.5; net days 597/409/219 (calc; FY24 not like-for-like); aged >6m INR M 1,597.7 (8.4%) / 2,132.9 (15.8%) / 1,314.1 (15.9%); retention 11,965.9 / 8,574.1 / 4,751.7; allowance 1,959.1 / 1,759.7 / 635.9; FY26 release tied to BHEL cash INR M 3,430.6 (one-time size)"
restatements_found:
  - "FY25 continuing profit before tax re-presented from INR M (380.2) (AR25 p.168) to INR M 224.6 (AR26 p.132): INR M 604.8 of Durgapur cost moved to discontinued (employee 399.4, other expenses 181.6, depreciation 6.4, materials 17.4)"
  - "FY25 line re-presentations: royalty 132.1 to 121.5, reimbursement 270.0 to 256.3, EDP 286.6 to 248.7, security 35.2 to 23.2"
  - "Note 36 FY25 comparatives NOT re-presented (still include Gas/Hydro flows); Note 26 FY26 column repeats FY25 slump-sale deductions (185.0, 137.7)"
going_concern_language: "NONE adverse. CARO clause (xix) no material uncertainty (auditor's report p.130-131, outside notes); 'going concern' elsewhere refers to the slump-sale and demerger transfers"
analyst_note: "Pass 3 closed the three open items. (1) Royalty booking: no note names it; the word appears only in Notes 33 and 36; real cost likely inside cost of materials (inference), profit effect unproven. (2) Slump-sale deductions: closing balances tie only with them, values equal FY25 to one decimal, total 322.7 exceeds Durgapur block 280.3; the loss-order row flips sign under one label; P&L effect NOT STATED, bound nil to 299.2 on warranty. (3) INR M 247.0: continuing cost carries no matching charge (entity-level PBT ties 3,123.3 - 698.0 = 2,425.3; FY25 re-presentation moved cost lines only). The exposure is post-demerger supply cost, not misstatement. ICD: YELLOW on the Notice guarantee (outside notes); RED on the Notes alone. Net cash 8,473.1 with ICD, 3,973.1 without."
```


---
ORCHESTRATOR ERRATUM (2026-11-16, appended from Verifier A finding B12a): "55.3% of the INR M 3,174.4 step-up" computes to 55.2% ((1,320.0 + 433.5) / 3,174.4). Stage 3 already uses 55.2%.
