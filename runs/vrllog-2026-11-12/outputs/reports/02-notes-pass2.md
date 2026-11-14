# VRLLOG Stage 2, Notes to Financial Statements, PASS 2 (what pass 1 missed)

Company: VRL Logistics Ltd (standalone). Source: Annual_Report_2026.txt (FY2025-26). Run date 2026-11-12.
UNIT: INR lakhs unless a line says otherwise (Note 1(b)(i), p.175). No figure converted. DERIVED = my arithmetic on filed figures. Anchor form (Note N, p.X) as in pass 1; p.X is the [page X] marker of the .txt.
Method: re-read Notes 1 to 41 against pass 1, plus the Cash Flow Statement (p.173) for tie-outs. Pass 1 covered most notes fully (receivables, borrowings table, leases, RPT table, contingent table, gratuity, deferred tax, ECL, CSR, EPS). Only remainders are below. Items already in pass 1 are skipped.
Ratings: GREEN / WATCH / RED.

---------------------------------------------------------------
## A. Pass 1 open questions, resolved

### A1. Note 13(C) borrowings cash flow of -2,645 versus +624: it ties. No error. GREEN.
- The .txt order of the Note 13(C) table is readable and closes: FY26 borrowings 44,945 + cash flows (2,645) + non-cash 3,269 = 45,569; lease liabilities 77,863 + (19,649) + 11,630 = 69,844 (Note 13(C), p.200). FY25: 28,161 + 13,736 + 3,048 = 44,945; leases 75,704 + (18,492) + 20,651 = 77,863. I did not need to open the PDF page because every row closes arithmetically.
- Why -2,645 differs from +624: the note nets interest paid inside "cash flows". Cash Flow Statement financing lines: 2,834 + 9,844 - 12,054 = +624 (p.173). Less interest and other borrowing costs paid 3,269 (p.173) = -2,645. The 3,269 shown as "non-cash movement" equals interest expense 3,170 plus other borrowing costs 99 (Note 24, p.211). So it is an accrual and payment pair shown on both sides (DERIVED).
- The same convention holds in FY25: net financing flows on borrowings -3,916 + 26,894 - 6,195 = 16,783; less interest expense 3,048 = 13,735, against 13,736 printed (Note 13(C), p.200; p.173). Rounding only.
- Lease row: -19,649 = principal 13,429 + interest 6,220 (p.173). Ties.
- Consequence: carrying borrowings moved by exactly the cash movement (45,569 - 44,945 = 624) with no accrued interest build-up. Pass 1's "Pass 3 to resolve" item is closed.

### A2. Note 34B dividend table (p.223): column assignment confirmed by arithmetic. GREEN.
- Row order in the text: interim FY25 (INR 5), final FY25 (INR 10), interim FY26 (INR 5). Values in order: FY26 column "-", 8,747, 8,747; FY25 column 4,373, "-", "-" (Note 34B, p.223).
- Check: INR 10 x 87,468,495 pre-bonus shares = 8,747; INR 5 x 174,936,990 post-bonus shares = 8,747; INR 5 x 87,468,495 = 4,373. All three tie. So FY26 paid = final FY25 8,747 + interim FY26 8,747 = 17,494 (Cash Flow p.173: 17,491 after unclaimed-dividend adjustment).
- Per post-bonus share, paid in FY26: INR 5 (final FY25, INR 10 pre-bonus) + INR 5 (interim FY26) = INR 10. Paid in FY25: INR 2.50 post-bonus equivalent (DERIVED). Cash dividend per share paid rose 4x year on year.

---------------------------------------------------------------
## B. LOAD-BEARING FACT 1 and 2: new evidence on the margin step-up and tonnage

### B1. The notes do not split diesel price from volume, but the MD&A page does. It points to volume, not fuel price. WATCH (changes the reading of pass 1).
- Source outside the notes, used as a cross-reference only: Management Discussion, fuel paragraph and expense table (txt [page 84]-[page 85], AR pp.77-78): "Fuel consumption qty decreased by 7.3%. Average purchase cost per litre of fuel increased from Rs.85.03 to Rs.85.07"; bulk purchase share 37.54% to 39.50%; tonnage down 7% for the year, Q1 FY26 down 13%, Q4 FY26 up 3% (txt [page 86]).
- Fit with Note 22 (p.210): diesel cost 80,821 vs 87,055 = -7.2%. That equals the -7.3% quantity change at a flat price. So the diesel saving in rupees is a volume effect (DERIVED).
- Per-tonne view, DERIVED, uses MD&A tonnage -7% (so a tonnage index of 0.93; this is an outside-notes input and must be verified at the stage 5 and concall step). Index = FY26 line / FY25 line / 0.93:

| Line (Note 22, 23, 26, pp.210-211) | FY26 / FY25 | Per tonne index |
|---|---|---|
| Revenue from operations (Note 20, p.209) | 1.019 | 1.096 (+9.6%) |
| Diesel cost | 0.928 | 0.998 (flat) |
| Lorry hire | 0.882 | 0.948 |
| Tyres and flaps | 0.877 | 0.943 |
| Hamali | 0.965 | 1.038 |
| Bridge and toll | 0.992 | 1.066 |
| Vehicle running, R&M (net) | 1.114 | 1.198 |
| Stores and spares consumed | 1.078 | 1.159 |
| Total freight, handling, servicing (Note 22) | 0.962 | 1.034 |
| Employee benefits (Note 23) | 1.077 | 1.158 |

- Reading: diesel cost per tonne did not fall. Revenue per tonne rose about 9.6% while total freight cost per tonne rose about 3.4% and employee cost per tonne about 16%. The 245 bps fall in diesel as % of revenue (pass 1) is the result of revenue per tonne rising against flat diesel per tonne. The step-up is a realisation story (freight hikes, dropping low margin business, per MD&A table p.85), not a fuel price story. This also fits Note 36(A): "improving freight realisations" (p.226).
- The one observation that separates the two readings: FY26 tonnage and revenue per tonne by quarter (NOT FOUND in the notes). If the -7% is right, margin quality depends on whether higher rates hold while tonnage recovers (Q4 +3%).
- Company EBITDA definition tie: MD&A prints EBITDA 67,389 and 20.77% on total income (txt [page 84]-[page 85]). 67,389 = my 65,022 + other income 2,367 (Note 21, p.210). So the company EBITDA includes other income, and its ratios use total income 324,478 as base (fuel 80,821 / 324,478 = 24.91%, matches the MD&A). My 20.19% excludes other income. Both are consistent; they differ by definition (DERIVED).

### B2. Revenue growth composition: 37% of FY26 net revenue growth came from fewer credit notes and discounts. WATCH.
- Note 20(c), p.210: contract price 321,561 vs 317,726 = +3,835 (+1.2%). Credit notes and discounts 1,184 vs 3,430 = 2,246 lower. Net contract revenue +6,081 (+1.9%): 3,835 + 2,246 = 6,081.
- So 2,246 / 6,081 = 36.9% of net growth is lower deductions (DERIVED). Deductions fell from 1.08% to 0.37% of contract price (DERIVED). This one-time normalisation cannot repeat: the deduction line is now close to zero.
- Pass 1 reported the 65% fall as "supports the price reset". This adds that billed (gross) growth was only 1.2% on a tonnage fall of about 7% (outside-notes), so billed price per tonne rose about 8.4% (DERIVED: 1.012 / 0.93 = 1.088).

### B3. Maintenance intensity rose in two lines pass 1 only partly covered. WATCH.
- Pass 1 reported Vehicle running, R&M +11.4%. It left out Stores and spares consumed: 7,799 vs 7,235 = +564 (+7.8%) (Note 22, p.211), on lower tonnage.
- Combined R&M and stores: 25,175 / 322,111 = 7.82% of revenue vs 22,827 / 316,095 = 7.22%: +59 bps (DERIVED).
- MD&A reason for R&M: "Increase in driver incentives per km" (txt [page 85]), not repairs. The notes do not show the split of Note 22 "Vehicle running, repairs and maintenance (net)" between driver incentive and repair. NOT FOUND IN DOCUMENT.
- Agency commission 2,821 vs 2,645 (+6.7%) outgrew revenue (+1.9%) (Note 22, p.211): 0.876% vs 0.837% of revenue (+4 bps, DERIVED). Minor.
- Security charges 219 vs 389 (-44%). Claims 183 vs 259. Insurance 2,876 vs 2,939. Vehicle taxes 2,338 vs 2,394. Power 1,037 vs 1,062 (Note 22, p.211). All routine. Note 22 lines sum to 192,248 (checked line by line, DERIVED).

### B4. New diesel deposit of 550 on the balance sheet. WATCH (small, but it sits inside load-bearing fact 1).
- Other assets, current: "Diesel deposit" 550 (FY25 nil) (Note 7, p.194). Other deposits of 259 (unchanged) already include "deposits with diesel vendors" (Note 6, p.193).
- The notes do not say who holds the deposit, what it secures, or whether it relates to bulk purchase (MD&A: bulk share up to 39.50%). NOT FOUND IN DOCUMENT. [INFERENCE] a security or prepayment tied to larger bulk fuel buys; cannot be confirmed.
- Same note: "Other advances" (trip advances to drivers, FASTag, insurance asset, employee advances) fell to 622 from 1,455 (-833) (Note 7, p.194), a working capital release feeding CFO. Advance to suppliers 344 (593). The 25 loss allowance on capital advances present at 31 Mar 2025 is nil at 31 Mar 2026 while capital advances rose to 2,846 from 901 (Note 7, p.194). GREEN, minor.

---------------------------------------------------------------
## C. LOAD-BEARING FACT 4: cash, capex, assets, liabilities, new items

### C1. Vehicle disposals: scrap proceeds near the 5% residual, but a 656 loss because assets left before reaching residual. WATCH.
- Note 2A (p.189): FY26 vehicle disposals gross 6,753, accumulated depreciation 5,735 (84.9% depreciated), net book value 1,018. FY25: gross 4,145, accumulated 3,435 (82.9%), NBV 710. Gross disposals +63% year on year.
- Total PPE disposed FY26: gross 6,761, accumulated 5,737, NBV 1,024. Proceeds 369 (Cash Flow, p.173). Loss 1,024 - 369 = 655, against 656 booked in Note 26 (p.211) (DERIVED, ties within 1).
- Proceeds are 5.5% of disposed gross cost, close to the 5% residual policy (Note 1(d)(i), p.179). The 656 loss is 9.7% of disposed gross cost: vehicles left service at about 85% depreciated, not at the 95% implied by a 15-year life with 5% residual (DERIVED).
- Reading: [INFERENCE] fleet renewal is running ahead of the depreciation schedule on part of the fleet, so the 15-year truck life flagged in pass 1 may be longer than actual service life for retired units. The notes give no age profile of retired vehicles. NOT FOUND IN DOCUMENT. The MD&A lists "Loss on sale/scrap of vehicle" under administrative expenses (txt [page 86]).
- FY25 check: PPE NBV disposed 4,734 - 3,669 = 1,065; proceeds 1,863; gain 798 against 797 booked (Note 21, p.210). Of the 1,863, the related-party sale was 1,488 (Note 35, p.223), so the FY25 gain depended on that one sale. (Pass 1 gave the 80% share.)

### C2. FY25 acquisition of a previously leased property, "without additional consideration", links to tax paid on stamp-duty-value difference. WATCH.
- Cash Flow Statement note, non-cash investing (txt [page 174], p.174): "The Company acquired a land and building that was previously held under a lease arrangement... leasehold improvements, have been reclassified to 'Building' without any additional consideration." Note 2A note 4 (p.189): FY25 reclassification of leasehold improvements 1,004 gross (accumulated 674) to Buildings. Pass 1 noted the reclassification only inside the property table figures; it did not connect it.
- Note 27(c), p.212: FY25 tax reconciliation includes "Tax paid on differential amount between SDV and consideration" 675. Note 16, p.206: DTA "Tax under section 56(2)(x)" 383 created in FY25, unchanged in FY26. Section 56(2)(x) concerns property received for less than stamp duty value.
- DERIVED, assumes the statutory rate of 25.17% applies: 675 / 0.2517 = about 2,682 of differential value taxed. This is my arithmetic on a rate assumption; the notes do not print the differential.
- The seller is NOT FOUND IN DOCUMENT. Note 35 shows "Purchase of PPE" with related parties at NIL for FY25 and 15 for FY26 (p.224), and no related-party lease in the party list for FY25. So it was not a related-party purchase on the face of Note 35. [INFERENCE] a landlord relationship converted to ownership; ROU asset disposals of 6,879 gross in FY25 (Note 2A, p.189) may include it. Question for management.
- Rating note: the 675 tax is a one-off in the FY25 base. The FY26 effective tax rate of 25.5% against FY25's 26.8% (pass 1) is cleaner for it.

### C3. Land purchases and lease terminations move together; the notes do not link them. WATCH, [INFERENCE].
- Land additions: 24,290 (FY25) and 12,910 (FY26) (Note 2A, p.189); gross land 51,883 vs 14,716 at 1 Apr 2024. ROU asset disposals at gross cost: 6,879 (FY25) and 9,907 (FY26) (Note 2A, p.189). Lease liability 77,863 to 69,844 (Note 32, p.216).
- MD&A (txt [page 85]) says capex went to "commercial vehicles and purchase of land and building facilities at critical operational locations". [INFERENCE] the company is moving from leased to owned branch and hub space. Land is not depreciated (Note 1(d)(i), p.179), so rent and ROU cost fall while the capital sits as non-depreciating land. The notes give no site list, no price per sq ft and no seller names. NOT FOUND IN DOCUMENT.
- Why it matters: lease cost is below EBITDA (pass 1), so this shift does not lift EBITDA. It lifts EBIT and net interest-bearing capital employed, and it explains why land is now 22.3% of gross PPE (51,883 / 232,305, DERIVED).

### C4. Net liquidity fell more than the headline. Current ratio 0.49 had no explanation because it missed the 25% test. WATCH.
- Note 36 (p.225): current ratio 0.49 (0.63), a 21.3% fall. Remarks are only required above 25%, so none are printed (Note 36, p.226).
- Drivers visible in the notes (DERIVED): cash and cash equivalents 1,548 vs 5,312 (-3,764) (Note 10, p.196); current borrowings 12,155 vs 8,222 (+3,933) (Note 13, p.199); current lease liabilities 15,262 vs 17,494 (-2,232) (Note 32, p.216).
- Note 13(A)(v)-(vii) (p.199): the working capital loan 284, cash credit 2,493 and overdraft 57 (total 2,834) "As at 31 March 2025, the balance was classified under 'cash and cash equivalents'". Cash less these demand facilities: 1,548 - 2,834 = -1,286 (FY26), against 5,312 at FY25 as printed. On that basis net cash fell about 6,598, not 3,764 (DERIVED). The FY25 amount inside cash is NOT FOUND IN DOCUMENT, so the like-for-like FY25 number cannot be built. Undrawn secured facilities are 12,700 (Note 33(b), p.220).
- Cash Flow Statement, p.173: cash fell 3,764 although CFO was 65,437, because dividends (17,491) and the leased-to-owned land spend came in the same year.

### C5. Other financial liabilities (Note 14) were not extracted in pass 1. WATCH, small.
- Note 14 (p.201): total 7,282 (6,497), +12.1% against revenue +1.9%. Employee related payables 5,283 (4,929); deposits from drivers 1,050 (925, +13.5%), refundable on separation or retirement; deposits from agents and customers 409 (334); other liabilities 423 (252, +68%), "primarily claims payable on death of employees/ drivers and pending TDS settlement with customers"; leased premises deposits 31 non-current and 46 current (26; 1); unclaimed dividend 14 (11); capital creditors 26 (20). No amount is due to the IEPF.
- Employee related payables are 9.0% of employee benefit expense (about 33 days of payroll, DERIVED) and are twice trade payables 2,625 (Note 17, p.207). Part of the low payables-days in pass 1 is this accrual sitting in a different note. This is interest-free float of 5,283 + 1,050 + 409 = 6,742 (DERIVED).
- Driver deposits are carried at transaction value; the company states discounting is not material (Note 33(A) points 6-7, p.217). The stated attrition for drivers is 40% (Note 15, p.202); a 40% attrition base against a 1,050 refundable deposit pool makes a refund outflow every year, not only at retirement. [INFERENCE]; the refund schedule is NOT FOUND IN DOCUMENT.

### C6. Finance cost note (Note 24) has two small points. GREEN/WATCH.
- Note 24 (p.211): interest on financial liabilities at amortised cost 3,170 vs 3,048 (+4.0%); lease interest 6,220 vs 6,420; other borrowing costs 99 vs 8 (12x); interest on agents' deposits 9 vs 7. Total 9,498 vs 9,483.
- Interest at 7.0% on average borrowings of 45,257 (DERIVED) is within the stated rate range of 6.40% to 10.20% (Note 13, p.199). Other borrowing costs +91, with bank charges +77 (164 vs 87, Note 26, p.211): about 168 of extra financing charges tied to the new cash credit, overdraft and working capital lines (INFERENCE; the note does not say).
- Pass 1 had interest paid 3,269 in the cash view; Note 24 ties it exactly (3,170 + 99 = 3,269).

---------------------------------------------------------------
## D. Smaller cross-note items

- CSR cross-check: P&L CSR expense 405 (Note 26, p.211) equals the amount required (Note 31, p.215), while cash spent was 441. The 36 excess is parked as an asset: "Excess CSR spends carried forward" 47 vs 11 (+36) (Note 7, p.194). Consistent. GREEN.
- Director sitting fees: 22 in Note 26 (24) (p.211) versus 19 in the KMP table (20) (Note 35, p.224). The table covers only independent and non-executive directors (Note 35); the gap of 3 is not explained. GREEN, trivial.
- Lessor side (Note 32(B), p.216): the company "subleased some space out of its leased premises". Rental income 630 (+72%); undiscounted receipts next year 861 (+37% vs 630); total future receipts 3,760 vs 4,460 (DERIVED). Within the 323 from related parties, there is no breakdown by property (Note 35, p.223). GREEN.
- Contract liabilities (revenue received in advance) rose 38% to 1,273 (920), against revenue +1.9% (Note 18, p.201; Note 20(e), p.210). Opening balance fully recognised each year. GREEN.
- Gratuity note boilerplate says the board "employs the use of annuities and longevity swaps" (Note 15, p.202) while plan assets are 100% insurer-managed funds (p.203). No swap or annuity is shown anywhere in the notes. GREEN, boilerplate.
- Reconciliation of interest rate sensitivity: floating borrowings 33,985 (FY26) x 0.5% = 169.9 and 35,454 (FY25) x 0.5% = 177.3 tie to Note 33(a) (p.219-220). GREEN.
- Income taxes paid in investing: 49 (12) (Cash Flow, p.173), tax on interest income classified out of operations. Trivial.

---------------------------------------------------------------
## PASS 2 NEW FINDINGS SUMMARY (new items only)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Diesel saving is volume, not price: diesel -7.2% against fuel quantity -7.3% and price Rs 85.03 to Rs 85.07 (MD&A cross-reference). Per tonne, diesel is flat, revenue per tonne +9.6%, total freight cost per tonne +3.4%, employee cost per tonne +16% (outside-notes tonnage -7%). The margin step-up is a realisation story. | Note 22, 23 (pp.210-211); MD&A txt [page 84]-[page 86] | WATCH |
| 2 | 37% of net revenue growth (2,246 of 6,081) came from lower credit notes and discounts; contract price grew only 1.2%. Not repeatable. | Note 20(c), p.210 | WATCH |
| 3 | Maintenance intensity: R&M plus stores and spares +59 bps of revenue; stores and spares +7.8% not covered in pass 1. | Note 22, p.211 | WATCH |
| 4 | FY25 leased property acquired "without additional consideration", tax of 675 on stamp-duty-value difference; seller NOT FOUND; not a Note 35 related-party purchase. | CFS note p.174; Note 2A note 4 p.189; Note 27(c) p.212; Note 16 p.206 | WATCH |
| 5 | Vehicle disposals: gross 6,753 (+63%), NBV 1,018, proceeds 369, loss 656; retired at about 85% depreciated, against the 15-year life. | Note 2A p.189; Note 26 p.211 | WATCH |
| 6 | Net cash less demand facilities -1,286 vs 5,312; current ratio 0.49 had no remark (below 25% test). | Notes 10, 13, 36 (pp.196, 199, 225) | WATCH |
| 7 | Land purchases and lease terminations move together (inference); land is 22.3% of gross PPE. | Note 2A p.189; Note 32 p.216 | WATCH |
| 8 | Other financial liabilities 7,282 (+12%); employee payables 5,283 and driver deposits 1,050 form float of 6,742. | Note 14, p.201 | WATCH |
| 9 | New diesel deposit 550; trip and other advances down 833. | Note 7, p.194 | WATCH (small) |
| 10 | Note 13(C) and Note 34B tie. Pass 1 open items closed. EBITDA 67,389 in MD&A equals notes-derived 65,022 plus other income 2,367. | Note 13(C) p.200; Note 34B p.223; Cash Flow p.173 | GREEN |

Restatements or reclassifications added by pass 2: none beyond pass 1. The FY25 leasehold improvements reclassification to Buildings (1,004 gross) is a FY25 item (Note 2A note 4, p.189).
Going concern language: none found in the notes beyond pass 1's "ability to continue as a going concern" (Note 34, p.222), which is capital-policy boilerplate.
