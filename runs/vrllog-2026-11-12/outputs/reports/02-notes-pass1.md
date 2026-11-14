# VRLLOG Stage 2, Notes to Financial Statements, PASS 1 (full extraction)

Company: VRL Logistics Ltd (standalone only, no subsidiaries, no consolidated statements). Source: Annual_Report_2026.txt (FY2025-26). Run date 2026-11-12.
UNIT: every figure is INR LAKHS unless a line says otherwise (Note 1(b)(i), p.175: "reported in Indian Rupees in lakhs"). No figure is converted. Percentages and ratios marked DERIVED are my arithmetic on filed figures.
Anchor form: (Note N, p.X). p.X is the [page X] marker of the .txt (marker precedes its page content). FY26 = year to 31 Mar 2026. FY25 = year to 31 Mar 2025.
Ratings: GREEN = clean, WATCH = watch, RED = red flag.
Scope note: notes cover FY26 only. H1 FY27 margin, post-balance-sheet buyback and H1 FY27 tonnage are NOT FOUND IN DOCUMENT (the notes end at 31 Mar 2026; Note 38, p.226, says no subsequent events, Board approval 18 May 2026, Note 41, p.227).

B00 input gaps carried forward (none changes the notes read): shareholding pattern was empty at collection and was repaired with NSE Sep 2026 XBRL; screener P&L/Quarters/BS/CF sheets empty; no Q2 FY27 results text layer; ICRA rationale 12 months old; sector_cap_row NOT FOUND (HIGH, operator rules at /fttcp gate). Weak text layer applies to Q2 FY27 results and three announcements, not to this AR (B00 input_gaps).

---------------------------------------------------------------
## LOAD-BEARING FACTS CHECK (first priority)

### LBF 1. EBITDA margin step-up and which cost lines moved (FY26 only; H1 FY27 NOT FOUND IN DOCUMENT)
The company prints no EBITDA line. I built one from the face statements (P&L, p.171) and the cost notes. DERIVED, definition: PBT + finance cost + D&A - other income. It sits AFTER Ind AS 116 (lease depreciation and lease interest are below EBITDA; short-term lease rent stays above it).

| Line (INR lakhs) | FY26 | FY25 | Change | % of revenue FY26 / FY25 (DERIVED) |
|---|---|---|---|---|
| Revenue from operations (Note 20, p.209) | 322,111 | 316,095 | +6,016 (+1.9%) | 100 / 100 |
| Freight, handling, servicing cost (Note 22, p.210-211) | 192,248 | 199,814 | -7,566 (-3.8%) | 59.68 / 63.21 |
| of which Diesel cost | 80,821 | 87,055 | -6,234 (-7.2%) | 25.09 / 27.54 |
| of which Lorry hire | 15,571 | 17,662 | -2,091 | 4.83 / 5.59 |
| of which Tyres and flaps | 6,676 | 7,609 | -933 | 2.07 / 2.41 |
| of which Hamali | 20,293 | 21,031 | -738 | 6.30 / 6.65 |
| of which Vehicle running, R&M (net) | 17,376 | 15,592 | +1,784 (+11.4%) | 5.39 / 4.93 |
| of which Rent (short-term leases, Note 32) | 7,987 | 7,548 | +439 | 2.48 / 2.39 |
| of which Bridge and toll | 24,368 | 24,575 | -207 | 7.57 / 7.77 |
| Employee benefits expense (Note 23, p.211) | 58,739 | 54,517 | +4,222 (+7.7%) | 18.24 / 17.25 |
| Other expenses (Note 26, p.211) | 6,102 | 4,345 | +1,757 (+40%) | 1.89 / 1.37 |
| EBITDA excluding other income (DERIVED) | 65,022 | 57,419 | +7,603 | 20.19% / 18.17% |
| Same, adding back loss on PPE sale 656 (FY25: none in expenses) | 65,678 | 57,419 | | 20.39% / 18.17% |

Bridge check (DERIVED): +6,016 revenue +7,566 freight saving -4,222 employee -1,757 other = +7,603. It ties.
Reading from the notes:
- Margin step-up is about +202 bps. Diesel alone fell 245 bps of revenue. The diesel line explains more than the whole step-up. Lorry hire (-76 bps) and tyres (-34 bps) add to it. Employee cost took back +99 bps. (WATCH, mechanism is a cost line, not revenue leverage: revenue grew only 1.9%.)
- The company's own explanation sits in Note 36(A), p.226: "reduction in key operating costs (especially diesel costs), coupled with stable revenue growth by improving freight realisations and disciplined cost management".
- Diesel price per litre, litres burnt and kilometres run are NOT FOUND IN DOCUMENT in the notes. So price versus volume split of the diesel saving cannot be done from the notes. Outside the notes the MD&A (p.86) gives tonnage down 7% for FY26; that is a pointer, not a notes fact.
- Non-cash items inside P&L: gain on lease modification 725 (FY25 308) and unwinding of deposits 253 (FY25 317) in other income (Note 21, p.210); both are excluded from my EBITDA. Loss on sale of PPE 656 in other expenses versus a profit of 797 in other income in FY25 (Notes 21, 26, pp.210-211): the PPE line swung -1,453 between years in the P&L.
- Other expenses +40%: legal and professional 864 vs 377 (+487), travelling 2,030 vs 1,608, advertisement 207 vs 102, bank charges 164 vs 87 (Note 26, p.211).
- Rating WATCH: the step-up is real in the filed P&L, led by diesel. The notes do not show whether it is a price effect (fuel price) or a volume or routing effect. That one observation separates the two readings.

### LBF 2. FY26 tonnage after the price reset
Tonnage is NOT FOUND IN DOCUMENT in the notes. Note 20 (p.209-210) gives revenue only:
- Goods transport services 318,549 (FY25 312,534, +1.9%); courier 1,828 (1,762); scrap 1,734 (1,799) (Note 20, p.209).
- By channel (Note 20(b), p.209-210): FTL 28,081 (26,265, +6.9%); LTL 290,468 (286,269, +1.5%); courier 1,828 (1,762).
- Contract price 321,561 less credit notes 1,074 and discounts 110 = 320,377; FY25 317,726 less 2,880 and 550 = 314,296 (Note 20(c), p.210). Credit notes and discounts fell from 3,430 to 1,184 (DERIVED, -65%). That supports the "price reset": fewer concessions. (WATCH positive, one observation.)
- No customer above 10% of revenue in either year (Note 20(h), p.210). 100% India (Note 20(b)).
- Pointer outside the notes: MD&A p.86 says FY26 tonnage fell 7% YoY, Q1 FY26 was down 13%, Q4 FY26 was +3%, daily tonnage above 11,500 in Q4. Verify at stage 5 and the concalls.
- Revenue +1.9% on tonnage -7% implies realisation per tonne about +9.6% (DERIVED, uses an outside-notes figure).

### LBF 3. Promoter and related parties
Promoter holding (Note 12(c),(d), p.198): Dr. Vijay Sankeshwar 49,561,128 shares (28.33%); Dr. Anand Sankeshwar 54,981,642 (31.43%); Mrs. Vani Sankeshwar 792,978 (0.45%); Mrs. Lalita Sankeshwar 41,634 (0.02%); Mrs. Bharati 3,500; Mrs. Deepa 1,060. Total 105,381,942 shares = 60.24% of 174,936,990 (DERIVED). Percentage change during FY26 and FY25: 0.00% for all. Share counts doubled only because of the 1:1 bonus (Note 12, p.197). Mrs. Deepa appears at 530 pre-bonus shares at 31 Mar 2025 against none at 1 Apr 2024 (new promoter-group name in FY25, trivial size).
- So per the notes there was no promoter sale or purchase in FY25 or FY26. An "earlier promoter stake sale" in the Step-1 brief is NOT FOUND IN DOCUMENT here. It would fall before 1 Apr 2024 or after 31 Mar 2026.
- Pledge: no pledge disclosure in the notes. NOT FOUND IN NOTES. Pointer: Directors' report text says no pledge over promoter shares (txt line 7969-7970).
- Buyback of Rs 280 Cr at Rs 320: NOT FOUND IN DOCUMENT (post balance sheet; Note 38, p.226 shows none to disclose at 18 May 2026). Past buybacks: 28.75 lakh shares in total, 20.00 lakh in FY21 and 8.75 lakh in FY24 (Note 12(f)(ii), p.198). Contingent item (k) mentions "tax paid on buyback" not credited in an income tax processing demand (Note 29(k), p.214), which is the FY24 buyback tax trail.
- Dividends: FY26 paid 17,494 total (Note 34B p.223 and Statement of Changes in Equity, p.172): final FY25 8,747 (INR 10 pre-bonus) plus interim FY26 8,747 (INR 5 on the post-bonus count). The Note 34B table columns are scrambled in the text copy; the 17,494 total ties to the equity statement and to cash paid 17,491 (Cash Flow, p.173). Promoters' share of 17,494 at 60.24% is about 10,538 (DERIVED). FY25 dividends 4,373 (Note 34B). Payout FY26 = 17,494/23,683 = 74% of PAT (DERIVED). No proposed final dividend for FY26 is stated in the notes: NOT FOUND IN NOTES.

Related party note (Note 35, pp.223-224). FY26 AR prints transactions BY NATURE, not by named party.
Related parties listed (Note 35(A), p.223): enterprises where KMP or close family have control or significant influence: Vijayanand Foods Pvt Ltd, VRL Steel Pvt Ltd, Vijayanand Logistics Pvt Ltd (struck off), Vijayanand Infotech Pvt Ltd, Vijayanand Travels Pvt Ltd, VRL Media Pvt Ltd, Vijaykant Dairy and Food Products Ltd, Sankeshwar Minerals Pvt Ltd (formerly Sankeshwar Ventures (India) Pvt Ltd), Sankeshwar Printer Pvt Ltd, Hyperkonnect Technologies Pvt Ltd, VRL Foundation, Aradhana Trust, Shri Ayyappa Bhakta Vrunda Trust, Karnataka Cancer Therapy and Research Institute.
New or changed versus FY25 AR list (FY25 AR Note 43, txt line 12092-12109): Karnataka Cancer Therapy and Research Institute is new on the FY26 list; Welldone Cinemas LLP and VRL Employees Group Gratuity Trust are no longer listed (the trust is still a related party in substance; see Note 15). Sankeshwar Ventures was renamed. (WATCH, disclosure transparency.)

| Nature (all counterparties are KMP-influenced enterprises) | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Goods transport services (company revenue) | 337 | 202 | +67% | Note 35(B), p.223 |
| Rental income (company income) | 323 | 226 | +43% | p.223 |
| Sale of spares and services | 18 | 153 | -88% | p.223 |
| Expense incurred on behalf of RP | 1 | 1 | 0% | p.223 |
| Sale of PPE | 10 | 1,488 | -99% | p.223 |
| Sale of scrap/barrels | 3 | 3 | 0% | p.223 |
| Lorry hire (cost) | 76 | 80 | -5% | Note 35(B), p.224 |
| Vehicle running, R&M (cost) | 1 | 1 | 0% | p.224 |
| Travelling and conveyance (cost) | 535 | 113 | +373% | p.224 |
| Printing and stationery (cost) | 81 | 87 | -7% | p.224 |
| Advertisement and promotion (cost) | 4 | 5 | -20% | p.224 |
| Purchase of PPE | 15 | NIL | new | p.224 |
| Rent (cost) | 76 | 13 | +485% | p.224 |
Totals (DERIVED): income-side RPT 692 (FY25 2,073) = 0.21% of revenue 322,111; expense-side RPT 788 (FY25 299) = 0.27% of total expenses 292,690 (P&L, p.171). Small in size.
Balances at year-end (Note 35(C), p.224): rental receivable 32 (34); trade receivable 20 (66); trade payable 9 (11); other current liabilities nil (8). All unsecured; no guarantees given or received (Note 35 note d, p.224). No loans or advances to promoters, directors, KMP or related parties in either year (Note 6 note 4, p.193).
KMP compensation (Note 35, p.224): short-term benefits 1,416 (FY25 1,342); director sitting fees 19 (20); payable at year end 244 (170). Post-employment, other long-term, termination, share-based: nil. The FY25 comparative here is 1,342; the FY25 AR printed KMP salaries of 1,312.58 (FY25 AR txt line 12352): the comparative moved by about 30 (WATCH, minor, may be a regrouping).
Findings that matter:
- Travelling and conveyance with RPs 535 vs 113 (+422). In the FY25 AR the same line was named as Directors' travelling expense paid to Vijayanand Travels Pvt Ltd (112.88) (FY25 AR txt line 12255-12260). [INFERENCE] the FY26 jump is likely the same counterparty; the FY26 note does not say. WATCH.
- FY25 AR named Vijayanand Travels as buyer of PPE for 1,488 (FY25 AR txt line 12180-12185). FY25 total PPE sale proceeds were 1,863 (Cash Flow FY25 column, p.173) and profit on sale of PPE was 797 (Note 21, p.210). So about 80% of FY25 PPE sale proceeds came from a promoter entity (DERIVED from both reports). The FY25 gain of 797 was 3.2% of FY25 PBT 24,995 (DERIVED). FY26 sale to RP was 10. (WATCH, closed in FY26.)
- Rent cost to RPs 76 vs 13 (+63): the FY26 table does not name the landlord. In FY25 the only RP rent-cost line was Vijayanand Travels (13.12) (FY25 AR txt line 12265-12268). Whether any promoter-owned property is leased by VRL under Ind AS 116 (ROU depreciation, interest, lease payments) is NOT FOUND IN DOCUMENT: the RP table has no lease-liability, ROU depreciation or lease-payment line. If such leases exist, Note 35 omits them. (WATCH, question for management.)
- Company as lessor to RPs: investment property part of Varur building leased to VRL Media Pvt Ltd, 9-year cancellable lease from FY22 with 5% escalation every 3 years; rental 59 (FY25 56) (Note 3, p.191). Rental income from RPs 323 of total rental income 630 (Note 21, p.210; Note 32(B), p.216).
- Related-party disclosure became LESS granular: FY25 AR named each party, nature, and promoter dividends and KMP remuneration lines; FY26 AR groups by nature only. Dividends paid to promoters and individual KMP remuneration are not in the FY26 Note 35. (WATCH.)
- Statement in Note 35, p.224: all RPTs are at arm's length with prior Audit Committee approval. Not independently testable from the notes.
- CSR: no related-party CSR payments (Note 31, p.215) despite VRL Foundation being a related party.

### LBF 4. Cash and capex: borrowings, leases, capex, contingent liabilities
Cash flow (Cash Flow Statement, p.173, INR lakhs): CFO 65,437 (FY25 55,479); operating profit before WC 66,739 (58,277); income taxes paid 5,285 (4,900). Investing: capex incl. CWIP, creditors and advances 29,862 (44,879); sale proceeds 369 (1,863); long-term deposits placed 37,100 and liquidated 37,030 within the year (FY25: 10 placed); net investing -29,400 (-42,978). Financing: net short-term borrowings +2,834 (-3,916); long-term borrowings raised 9,844 (26,894); repaid 12,054 (6,195); lease principal 13,429 (12,072); lease interest 6,220 (6,420); dividends 17,491 (4,372); interest and borrowing costs 3,269 (2,934). Net cash movement -3,764; closing cash 1,548 (5,312).
Derived cash view: CFO 65,437 - capex 29,862 - lease principal and interest 19,649 - interest 3,269 = 12,657 free cash after leases and interest (DERIVED). Dividends 17,491 exceeded it by 4,834. Net debt rose from 39,633 to 44,021 (Note 34A, p.222), up 4,388. Gross borrowings were roughly flat (44,945 to 45,569).
- Gearing (Note 34A, p.222): borrowings 45,569 less cash 1,548 = net debt 44,021 vs equity 114,244 = 39% (37%). Excludes lease liabilities. With lease liabilities 69,844 the net debt-plus-lease figure is 113,865 (DERIVED).
- Reported ratios (Note 36, pp.225-226): current ratio 0.49 (0.63); D/E 0.40 (0.41); DSCR 1.60 (1.47); ROE 21.27% (18.02%); ROCE 24.56% (21.40%). Their ROCE denominator excludes lease liabilities (capital employed = tangible net worth + borrowings + DTL, note 7, p.226) while EBIT is after ROU depreciation. Lease-adjusted ROCE, adding lease liabilities to capital employed (DERIVED): FY26 41,286/(168,096+69,844) = 17.3%; FY25 34,478/(161,146+77,863) = 14.4%. (WATCH: disclosed ROCE overstates versus the lease-inclusive base; direction of change is still up.)
- Capex: PPE additions 27,182 (FY25 46,094): land 12,910 (24,290), vehicles 10,037 (12,349), buildings 1,615 (5,491) (Note 2A, p.189). Land gross block 51,883 vs 14,716 at 1 Apr 2024 (+37,167 in two years, DERIVED). Capital commitments gross 7,984 (13,697), net of capital advances and CWIP 2,888 (11,288) (Note 30, p.215). Capital advances 2,846 (901) (Note 7, p.194). CWIP 2,250 (1,508) (Note 2B, p.190). Capex plan FY27 of Rs 220-240 Cr is NOT FOUND IN DOCUMENT.
- Borrowings 45,569 (Note 13, p.199): term loans 21,078 (HDFC 18,102 at 7.60%, Axis 3,110 at 7.35%), vehicle loans 21,657 (Bank of Baroda 9,907 floating 7.90-8.15%; fixed-rate vehicle loans 11,616 at 6.40-8.65%), WC demand loan 284 (8.30%), cash credit 2,493 (8.80%), overdraft 57 (7.35-10.20%). Current 12,155; non-current 33,414. Details in section 7 below.
- Lease liabilities 69,844 (current 15,262; non-current 54,582) vs 77,863 (Note 32, p.216; Balance Sheet, p.170).
- Contingent liabilities 5,303 in total (DERIVED) = 4.6% of net worth 114,244; no single item above 10% of net worth. See section 3.

---------------------------------------------------------------
## NOTE-BY-NOTE EXTRACTION

### 1. Accounting policies and changes (Note 1, pp.175-188; Notes 2A-4)
- Basis: Ind AS, historical cost, going concern; policies for FY26 and FY25 "are consistent" (Note 1(b)(i), p.175). GREEN.
- Use of judgements/estimates (Note 1(c), pp.176-178): leases, tax, provisions, useful lives, defined benefit, impairment (VIU), ECL, fair value. No numeric impairment assumptions (growth rate, discount rate) are disclosed and no impairment was recorded: NOT FOUND IN DOCUMENT for assumptions. No goodwill (none on balance sheet, p.170).
- Useful lives (Note 1(d)(i), p.179): trucks 15 years, buses/cars 8, battery vehicles 5, buildings non-factory 60, factory 30, computers 3, servers 6. Company states vehicle lives "different from those specified in Schedule II" supported by technical evaluation. Residual value up to 5% for buildings and vehicles, nil others. Trucks at 15 years with 5% residual is a long life. WATCH (long life flatters depreciation; no change in lives this year: "current and previous year" table). Net block vehicles 91,599 on gross 134,431 (Note 2A, p.189): 31.9% accumulated depreciation (DERIVED).
- No capitalisation threshold disclosed: NOT FOUND IN DOCUMENT. Insurance and permit fees for initial period capitalised into vehicle cost (Note 1(d)(i), p.179). WATCH, minor.
- Revenue (Note 1(d)(xii), pp.187-188): goods transport and courier recognised at a point in time on delivery. GREEN, conservative for a delivery business. The note says contracts have no significant financing component.
- Leases (Notes 1(d)(v), p.181; 32, pp.215-216): ROU assets 59,672 (68,727); lease liability 69,844 (77,863); incremental borrowing rate 8.00% in both years (Note 32, p.216) although bank loan rates fell in FY26 (HDFC 8.60% to 7.60%, Axis 7.60% to 7.35%) (Note 13, p.199). Extension and termination options ignored in the lease term (Note 32, p.215). ROU additions 13,517 (18,878); ROU depreciation 15,190 (15,922); lease interest 6,220 (6,420); total cash outflow for leases 19,648 (18,492); short-term lease expense 7,987 (7,548) (Note 32, p.216). Maturity undiscounted: under 1 year 15,786; 1-5 years 48,880; over 5 years 39,838; total 104,504 (117,665) (Notes 32/33, pp.216, 220). ROU gross block 116,735, accumulated dep 57,063 (Note 2A, p.189). Lease terminations: ROU derecognised 9,907 gross, 7,382 net of accumulated dep 2,525 (DERIVED from Note 2A); gain on lease modification 725 (308) booked in other income (Note 21, p.210). DTL footnote says "termination of significant lease contracts" (Note 16, p.207). Which leases were terminated is NOT FOUND IN DOCUMENT. WATCH: second year of lease-modification gains in a row, and short-term lease rent of 7,987 sits above EBITDA while all other lease cost is below it.
- Recent pronouncements (Note 1(d)(xiv), p.188): Ind AS 118 effective 1 Apr 2027; no recognition impact expected. GREEN.
- Policy changes with quantified P&L impact: NONE disclosed. First-time adoptions: none material (Note 1(d)(xiv), p.188). GREEN.
- ECL matrix (Note 33(c), pp.221-222): FY26 loss rates: under 6 months 0.50% (FY25 0%), 6-12 months 5% (0%), 1-2 years 75% (4%), over 3 years 100%; credit impaired 100%. Rates were raised from nil buckets, a conservative direction. ECL allowance on receivables 255 (224) = 2.9% of gross 8,813 (DERIVED). GREEN. The FY25 rate for 1-2 years was 4% and became 75% on a small base (8).
- Inventories policy: FIFO, mostly stores and spares (Note 1(d)(viii), p.185). GREEN.

### 2. Related party transactions
Fully covered under LBF 3 above (table, RPT % of revenue, new parties, promoter rent, no loans to promoter entities, KMP pay).

### 3. Contingent liabilities (Note 29, pp.213-214) INR lakhs
| Nature | FY26 | FY25 | Stage / assessment |
|---|---|---|---|
| Disputed claims pending in courts (motor accidents, consumer, workmen: footnote (i)) | 359 | 355 | legal opinion based estimate |
| Claims not received against consignments | 70 | 58 | |
| Income tax (footnotes f, j) | 2,198 | 5,020 | appeals; AY2017-18 matters demand 1,226 (gratuity, 80JJAA Form 10DA delay, aircraft expenses, average-margin addition, lease expense) |
| Customs duty (footnote h) | 1,569 | 1,569 | aircraft import exemption; CESTAT Ahmedabad ruled for company in FY24, refund 688 received, Department appealed to Gujarat High Court in FY25; company claims interest on refund |
| Service tax | 690 | 639 | |
| GST | 417 | 408 | |
| Additional bonus payable | nil | 202 | dropped |
| Total (DERIVED) | 5,303 | 8,251 | FY25 AR printed 8,254.66 including bank guarantees 4 (FY25 AR txt line 11317) |
- Total/net worth 114,244 = 4.6% (FY25: 8,251/108,455 = 7.6%) (DERIVED). Largest single item: income tax 2,198 = 1.9% of net worth. No item above 10% (GREEN on size).
- Management position: contesting all; no provision; outflow timing not estimable (footnotes a, b, p.213). Amounts exclude interest and penalty (footnote c). WATCH.
- ITEM OMITTED FROM THE TABLE, RED/WATCH: footnote (k), p.214. A Centralised Processing Centre demand of 5,186 under s.156 for the FY2023-24 assessment (assessed under 143(3) with no additions) arose from non-credit of advance tax, TDS/TCS and buyback tax, and wrong s.234B interest. Company filed a s.154 rectification. Management calls cash outflow "very remote" and records it neither as a liability nor as a contingent liability. Size: 5,186 = 4.5% of net worth (DERIVED); it would roughly double the table total (DERIVED 5,303 + 5,186 = 10,489 = 9.2% of net worth). Income tax contingent fell 5,020 to 2,198 in the same year; whether the 5,020 included an earlier form of this demand is NOT FOUND IN DOCUMENT. Rated WATCH (record could be a clerical error as stated, but the exclusion is a judgement and the rectification outcome is unknown).
- Stamp duty (footnote (g), pp.213-214): Karnataka notice on duty for acknowledgement of delivery of consignments, Article 1(ii) of the Karnataka Stamp Act. High Court Dharwad directed no coercive action on deposit of 25 lakhs; quantum not determined. Management says "no financial liability is expected" and no amount is disclosed even as contingent. WATCH: unquantified exposure on a high-volume documentation practice; the notes give no estimate.
- Guarantees for subsidiaries: no subsidiaries, so none. Bank guarantees: FY25 showed 4 as contingent; FY26 has none in the table, while margin deposits of 57 are under lien against bank guarantees (Note 6, p.193). WATCH, trivial.
- Customs matter also includes a separate 4 differential duty on an aircraft windshield (footnote h, p.214).

### 4. Trade receivables (Note 9, pp.195-196; Note 33, pp.221-222)
Gross 8,813 (FY25 9,511); less allowance 255 (224); net 8,558 (9,287) (Note 9, p.195). Components: unsecured good 8,591 (9,225); from related parties 20 (66); credit impaired 202 (220).
Ageing of gross at 31 Mar 2026 (p.195): under 6 months 8,559; 6-12 months 42; 1-2 years 8; 2-3 years nil; over 3 years 2; credit impaired disputed 202 shown in the under-6-months column. Total 8,813. FY25 (p.196): 9,139; 94; 56; nil; 2; disputed credit impaired 220; total 9,511.
- Over 6 months, excluding the credit-impaired 202: 52 = 0.6% of gross (DERIVED); FY25: 152 = 1.6%. IMPROVING. GREEN.
- The credit-impaired disputed 202 (FY25 220) is placed in the "under 6 months" column in both years, which cannot be its true age (a 100% provision suggests it is old). WATCH, presentation. Allowance fully covers it.
- Receivable days (DERIVED, closing net receivables over revenue x 365): FY26 8,558/322,111 = 9.7 days; FY25 9,287/316,095 = 10.7 days; FY24 8,849 (Note 20(d), p.210) over FY24 revenue 288,862.03 (FY25 AR P&L, txt line 9503) = 11.2 days. Trend IMPROVING. Company ratio: turnover 36.10x vs 34.86x (Note 36, p.225). Terms 30 to 90 days (Note 9 note 3). GREEN.
- Customer above 10%: none (Note 20(h), p.210; Note 33, p.221: no concentration, 100% India).
- Related-party receivables: 20 trade (66) plus 32 rental (34) (Note 9, Note 6). Immaterial.
- ECL loss allowance movement: opening 224, created 31, reversed nil, closing 255; bad debts nil (Note 33, p.222). GREEN.

### 5. Inventory (Note 8, p.194)
Total 4,375 (4,290): raw materials 3 (2); certified emission reduction credits 9 (9); stores and spares 4,363 (4,279) (includes in transit 195 (437)). No write-down or reversal in either year. 74,047 unsold CDM credits from 2013-2018 carried at 9. No finished goods in a service business. Inventory is 1.4% of revenue-days-scale (not meaningful). Inventory turnover 22.00x vs 23.75x (Note 36, p.225); the formula uses diesel, tyres and stores consumption over average inventory. Reconciliation of quarterly stock statements to banks: differences of 74 to 86 explained as stationery stock not reported (Note 13(D), p.201); Q4 FY26 return "yet to be filed". GREEN. Receivable statements: no reconciliation reported though receivables are pledged (Note 13(B), p.200): NOT FOUND IN DOCUMENT, WATCH minor.

### 6. Investments, subsidiaries, loans (Notes 5, 6, 7; pp.193-194)
- No subsidiaries, JVs or associates. Investments are 6 only: 20,000 shares of Shamrao Vithal Co-operative Bank (5) and 5,000 shares of Saraswat Co-operative Bank (1), FVTPL, no impairment (Note 5, p.193).
- No loans or ICDs given to anyone in FY26 or FY25 (Note 6 notes 4-5, p.193). GREEN.
- Other financial assets 3,458 non-current and 1,938 current (Note 6, p.193): lease security deposits 3,164 non-current and 1,681 current (4,083; 1,095), allowance 49 (81); other deposits 259; RP rental receivable 32; other receivables 180 (82) (cash collected by agency); margin money with over-12-month maturity 35 (91); margin money under 12 months 24; bank deposits under 12 months 70 with 32 pledged against overdraft. Deposits against legal disputes sit in "Other deposits" 259. GREEN.
- Lease deposit allowance reversals of 32 (FY25 116) lifted earnings through the loss allowance line (Note 33, p.222). Minor.
- Gross long-term deposits made and liquidated inside FY26: 37,100 placed, 37,030 liquidated (Cash Flow, p.173) against interest income on bank deposits of only 152 (Note 21, p.210), and closing bank and margin deposits of only 129 (Note 33 table, p.218). The purpose (overdraft-linked sweeps?) is NOT FOUND IN DOCUMENT. Note 36 ratio B reports "return on investment" of 133.77% (7.08%), "denominator compression" (p.226). WATCH, classification and purpose unexplained.

### 7. Borrowings (Note 13, pp.199-201; Note 33, pp.220-222; Note 34, p.222)
Instrument table (INR lakhs, 31 Mar 2026; FY25 in brackets):
| Instrument | Non-current | Current | Rate and security |
|---|---|---|---|
| Term loans (banks) | 18,584 (21,077) | 2,494 (843) | HDFC Bank 18,102 (18,633): mortgage on land and building, Dabaspet Bengaluru, 108 EMIs of 171, Repo plus spread, 7.60% (8.60%); Axis Bank 3,110 (3,420): mortgage, Bangrakulur Mangaluru, 108 EMIs of 36 plus terminal 23, Repo plus 2.10%, 7.35% (7.60%) |
| Vehicle loans (banks) | 14,830 (15,646) | 6,827 (7,379) | Bank of Baroda 9,907 (13,370) floating MCLR 7.90-8.15%, 6-40 EMIs; fixed-rate loans 11,616 (9,522) Axis, Federal, HDFC, Kotak, Saraswat, 6.40-8.65%, 1-50 EMIs; hypothecation of vehicles |
| WC demand loan (ICICI) | nil | 284 (nil) | 6-month MCLR, 8.30% (9.25%); mortgage Bangrakulur |
| Cash credit (SVC Co-op Bank) | nil | 2,493 (nil) | PLR minus 5.10%, 8.80% (9.50%); hypothecation of stock and book debts plus buildings at Kalaburagi, Davangere, Gadag |
| Overdraft (various banks) | nil | 57 (nil) | 7.35-10.20% (6.10-11.45%); lien on deposits plus building at Dharwad |
| Total | 33,414 (36,723) | 12,155 (8,222) | 45,569 (44,945) |
- Interest mix (Note 33(a), p.219-220): fixed-rate vehicle loans 11,584 (9,491); variable: term 21,078, vehicle 10,073, WC 284, CC 2,493, OD 57. Floating share about 75% (DERIVED). 50 bps move = 169.92 pre-tax (177.27) (p.220).
- Covenants: debt-equity and DSCR "etc"; "in compliance with all the debt covenants" (Note 34, p.222). Covenant thresholds NOT FOUND IN DOCUMENT. No default, no wilful-defaulter status (Note 13 notes c, d, p.199). No waivers disclosed. No related-party borrowings (Note 35 shows none). GREEN.
- Term changes: WC, cash credit and overdraft balances now sit in borrowings; "as at 31 March 2025 the balance was classified under cash and cash equivalents" (Note 13 A(v)-(vii), p.199) while the FY25 column in the table shows nil. This is a presentation basis change with no restatement quantified. WATCH. FY26 net debt of 44,021 is computed on gross cash of 1,548; had the 2,834 of demand facilities still netted against cash, cash would be minus 1,286 (DERIVED).
- Principal sums versus carrying: term loan principal 21,212 versus carrying 21,078 and vehicle loan principal 21,523 versus carrying 21,657: both differ by 134, opposite signs, total ties at 45,569 (DERIVED). Minor.
- Maturity (Note 33(b), p.220), undiscounted: on demand 2,834; under 1 year 9,321; 1-5 years 24,805; over 5 years 8,609; total 45,569 (equals carrying: no interest flows included, so this understates true undiscounted outflows). WATCH minor. Five-year schedule by year NOT FOUND IN DOCUMENT.
- Undrawn cash credit and overdraft facilities 12,700 (Note 33(b), p.220).
- Assets pledged: 70,779 (72,703): receivables 8,558, inventories 4,375, vehicles 30,333, Dabaspet land and building 22,768, Bangrakulur 4,376 (Note 13(B), p.200).
- Financing reconciliation (Note 13(C), p.200, garbled in text copy): borrowings 44,945 to 45,569 (cash flow -2,645, non-cash 3,269); lease liabilities 77,863 to 69,844 (cash flow -19,649, non-cash +11,630). The borrowings cash flow -2,645 does not equal the Cash Flow Statement net of 2,834 + 9,844 - 12,054 = +624 (DERIVED); the reconciliation row appears to carry a different sign or scope. Pass 3 to resolve against the PDF.

### 8. Trade payables (Note 17, pp.207-208)
Total 2,625 (3,086): MSME 32 (16); others 2,593 (3,070); RP payables 9 (11). Ageing FY26: unbilled 1,578; under 6 months 934 (MSME 32 plus others 902); 6-12 months 98; 1-2 years 15; over 3 years 0 (p.208). FY25: unbilled 1,780; 1,304; none beyond 3 years 2. MSME interest due or paid: nil; no overdue principal (Note 17, p.207-208). Payable days: turnover 69.46x vs 88.54x (Note 36, p.225), about 5.3 vs 4.1 days (DERIVED). Terms 30-45 days. GREEN. Payables are very low relative to cost of 198,350 (DERIVED): the business pays quickly (diesel, toll, hamali are near-cash).

### 9. Provisions (Note 15, pp.201-205)
- Gratuity: DBO 8,591 (7,181), plan assets 1,830 (2,211), net liability 6,761 (4,970) (Note 15(b), p.203). Funded ratio 21.3% (30.8%) (DERIVED). Staff plan is funded through VRL Employees Group Gratuity Trust, drivers and hamals unfunded (p.201). Plan assets are 100% insurer managed (p.203).
- Roll-forward of plan assets (p.203): opening 2,212 + expected return 130 + return excluding interest 10 - benefits paid 522 = 1,830. There is NO employer contribution in FY26 (and none in FY25: 2,738 + 160 + 19 - 705 = 2,212). Yet FY25 note expected a contribution of 1,230 in FY26 and FY26 note expects 754 in FY27 (p.205). WATCH: the funded plan is being drawn down, not topped up.
- DBO movement: service cost 1,165; interest 453; actuarial loss 523; paid from fund 522; paid directly 209 (p.203). Charged to P&L 1,488 (1,244) (p.204); OCI loss 513 (58), of which financial assumptions 400, experience 123, plan asset return -10 (p.204).
- Assumptions (p.202): discount rate 7.32% (6.69%) staff, 6.70% (6.54%) drivers and hamals; salary growth staff 6.00% (5.00%), drivers and hamals 3.00% (0.05%); attrition staff 14%, drivers 40%; mortality IALM 2012-14. Drivers' salary growth was 0.05% in FY25. WATCH: raising to 3.00% adds to DBO and was a driver of the actuarial loss.
- Sensitivity (p.204): discount rate +/-1%: -455 / +509; salary growth +/-1%: +478 / -435.
- Maturity profile of DBO (undiscounted) FY26: 1,383; 4,114; 10,387 (over 6 years) = 15,884; FY25: 1,028; 2,479; 3,675 = 7,182 which equals the PV DBO of 7,181 (p.204). The two years are on different bases. WATCH, minor.
- Duration: staff 7.15 years, drivers 3.38 years (p.204).
- Provisions on balance sheet: non-current gratuity 5,455 (3,224), compensated absences 1,631 (1,466); current gratuity 1,306 (1,746), compensated absences 442 (357) (Note 15, p.201). Compensated absences 2,073 (1,823) (p.205).
- Defined contribution: PF 3,580 (3,459), ESI 602 (762), labour welfare 21 (14) (p.201).
- Warranty, decommissioning, onerous contract provisions: NONE disclosed. Litigation provision: NONE; all litigation treated as contingent (Note 29, p.213).
- Cross-note slips: Note 23 says gratuity expense 1,488 and cites "note 14(b)" (the gratuity note is Note 15(b)) and "note 15(f)" which does not exist (Note 23, p.211); FY25 gratuity cost is 1,244 in Note 15 but 1,246 in Note 23 (p.204 vs p.211). Trivial. GREEN/WATCH.

### 10. Deferred tax and income tax (Notes 16, 19, 27; pp.206-207, 209, 212)
- Net DTL 8,306 (7,777): DTL on depreciation 14,658 (13,146) and ROU 15,018 (16,566); DTA on lease liabilities 18,179 (19,233), employee provisions 2,723 (2,227), loss allowance 85 (92), s.56(2)(x) tax 383 (383) (Note 16, p.206). Deferred tax charge 658 (1,073); OCI credit 129 (15) (p.206).
- DTA of 383 for "tax under section 56(2)(x)" was created in FY25 (p.206). The FY25 tax reconciliation includes "tax paid on differential amount between SDV and consideration" 675 (Note 27(c), p.212), i.e. tax paid on a property bought below stamp duty value. The DTA is realisable only if that tax gives a future deduction; the note gives no timing. WATCH, small.
- Tax expense 8,105 (6,703). Effective rate 25.50% (DERIVED: 8,105/31,788) vs statutory 25.17%; FY25 26.8% (6,703/24,995). Reconciling items: prior-year adjustment -63 (+60), permanent disallowance 102 (95), other 70 (-398) (Note 27(c), p.212). GREEN.
- Current tax 7,510 (5,570) vs cash tax paid 5,285 (4,900) (Cash Flow, p.173). Income tax net position moved from net asset 1,689 to net liability 437 (Note 19, p.209).
- No MAT credit, no unrecognised DTA, no tax losses disclosed. GREEN. Tax regime: normal rate 25.17% (new regime), no tax holiday.
- No Pillar Two impact (Note 1(d)(xiv), p.188).

### 11. Revenue details (Note 20, pp.209-210)
See LBF 2. Additional: contract liabilities (revenue received in advance) 1,273 (920), fully recognised within one year; opening balance fully recognised each year (Note 20(e),(f), p.210). Sale of scrap 1,734 (1,799) as other operating revenue (p.209). No unbilled receivables (Note 9 ageing, p.195). GREEN.
Other income 2,367 (2,422) (Note 21, p.210): rental 630 (366); bank interest 152 (6); margin deposit interest 3; tax refund interest 117 (5); dividend 1 (1); profit on PPE sale nil (797); fair-value unwinding of deposits 253 (317); provision write-back nil (136); lease modification gain 725 (308); miscellaneous 486 (486). Non-cash share (lease modification plus unwinding) 978 = 41% of other income and 3.1% of PBT (DERIVED). WATCH.

### 12. Other critical notes
- Exceptional items: none presented. Recurring non-cash items listed above (lease modification gains FY25 308, FY26 725).
- Goodwill and intangibles (Notes 4, p.192): computer software net 23 (31); no goodwill.
- Investment property (Note 3, p.191): net 81, fair value 357 (364), level 3, external registered valuer.
- Capital work in progress (Note 2B, p.190): 2,250 (1,508), all under one year except 3 in 1-2 years; no overdue or over-cost projects.
- Capital commitments: see LBF 4.
- Foreign currency: "not applicable"; transactions predominantly in INR (Note 33(a), p.219). No hedging. GREEN.
- Fair value (Note 33(A), pp.216-219): only unquoted equity of 6 at Level 3; no transfers between levels. GREEN.
- Segment (Note 37, p.226): single segment, all assets in India. Courier 1,828 is not a segment.
- EPS (Note 28, p.212-213): basic equals diluted at 13.54 (10.46 restated for bonus) on 174,936,990 shares; profit 23,683 (18,292). No dilutive instruments; no equity reserved for options (Note 12(e), p.198). No ESOP, share-based payment nil in KMP note (p.224). GREEN.
- Events after balance sheet date (Note 38, p.226): none. GREEN as written, but see B00: later announcements concern the buyback, a director resignation and results. Notes cannot show them.
- Going concern: "accrual and going concern basis" (Note 1(b)(ii), p.175); "safeguard its ability to continue as a going concern" (Note 34, p.222). No material uncertainty language anywhere. GREEN.
- CSR (Note 31, p.215): required 405 (377); adjusted 394 (340); spent 441 (351); no shortfall; excess carried 47 (11) to be used by 31 Mar 2027. P&L expense 405 (Note 26, p.211). No RP CSR. GREEN.
- Share capital (Note 12, pp.197-198): 1:1 bonus allotted 18 Aug 2025 by capitalising capital redemption reserve 378, securities premium 3,694 and general reserve 4,691 (8,763 incl. share issue expense 16, Statement of Changes in Equity, p.172). Paid-up 87,468,495 to 174,936,990 shares. Authorised capital reclassified: 125,000,000 equity plus 11,200,000 CCPS of INR 100 became 237,000,000 equity shares (p.197). Equity shareholders above 5%: promoters; HDFC Dividend Yield Fund 9.77% (17,082,852 shares) (FY25: HDFC Small Cap Fund 9.66%) (p.198). No securities premium remains (nil, p.172). Direct debits to reserves bypassing P&L: bonus capitalisation and dividends only.
- Equity: share capital 17,494; other equity 96,750 (99,708); total 114,244 (108,455) (Balance Sheet, p.170). General reserve 14,844 after transfer 2,368 (p.172).
- Dividends: see LBF 3.
- Audit trail (Note 40, pp.226-227): accounting software has edit log at application level, but at database level the audit trail feature "was not enabled" for FY26. RED/WATCH: a non-compliance with the MCA audit trail rule for direct data changes. Rated WATCH (disclosed, auditor mentions are outside this pass).
- Auditor (Note 26, p.211-212): audit and review fee, current auditors 75 (nil), predecessor auditors 21 (83). Statutory auditor Walker Chandiok & Co LLP (signature p.227). The split implies a first-year audit by a new firm. WATCH (new auditor, first year).
- Struck-off companies: related party Vijayanand Logistics Pvt Ltd is "struck off", but Note 39(b), p.226 says no transaction or balance with struck off companies. Consistent. GREEN.
- Regrouping (Note 41, p.227): previous year figures regrouped, "not material". Specific restatements found in this pass: see Restatements below.
- Ratio comparatives (Note 36, pp.225-226): the FY26 AR shows FY25 debt-equity 0.41 and DSCR 1.47, whereas the FY25 AR printed debt-equity 1.13 and DSCR 0.40 (FY25 AR txt line 12367-12371). The FY26 basis excludes lease liabilities from "debt" (Note 36 note 1, p.226); the FY25 basis included them. Current ratio FY25 0.64 versus 0.63 comparative. RED/WATCH for comparability: the improvement in D/E and DSCR in the FY26 AR is partly a definition change. I rate WATCH. Net profit ratio 7.35% (5.79%) and ROCE 24.56% (21.40%) are explained in Note 36 (A) (p.226).

---------------------------------------------------------------
## RESTATEMENTS AND RECLASSIFICATIONS FOUND (pass 1)
1. WC, cash credit, overdraft: FY25 balance "classified under cash and cash equivalents", FY26 under borrowings (Note 13 A(v)-(vii), p.199). FY25 column not restated for presentation, effect not quantified.
2. Ratio comparatives re-based: D/E 1.13 to 0.41 and DSCR 0.40 to 1.47 for FY25 (see item above).
3. KMP compensation FY25 comparative 1,342 versus 1,312.58 printed in FY25 AR (p.224).
4. Loss/profit on PPE moved: FY25 profit in other income (797), FY26 loss in other expenses (656) (Notes 21, 26).
5. EPS FY25 restated to 10.46 for the bonus (Note 28, p.213).

## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE
| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY26 EBITDA margin about 20.2% vs 18.2% (DERIVED). Diesel fell 245 bps of revenue, more than the whole step-up; revenue grew only 1.9%; employee cost rose 99 bps. Notes give no price/volume split. | Notes 20, 22, 23, 26 (pp.209-211); Note 36(A), p.226 | WATCH |
| 2 | CPC income tax demand 5,186 (4.5% of net worth) is kept out of the contingent liability table as "very remote"; contingent total 5,303 would roughly double. | Note 29(k), p.214 | WATCH |
| 3 | Free cash after leases and interest 12,657 against dividends 17,491; net debt up 4,388 to 44,021 (excludes lease liabilities 69,844). Disclosed ROCE 24.56% excludes leases; lease-inclusive about 17.3%. | Cash Flow p.173; Notes 34, 36 (pp.222, 225-226) | WATCH |
| 4 | RP disclosure got thinner: parties no longer named; RP travelling cost 535 vs 113; RP rent cost 76 vs 13; possible lease-type RP dealings not shown; FY25 sale of PPE 1,488 to a promoter entity produced the bulk of FY25's 797 PPE gain. Sizes are small (0.2-0.3% of revenue). | Note 35, pp.223-224; FY25 AR Note 43 | WATCH |
| 5 | Promoter holding unchanged at 60.24% through FY26; no pledge in notes; buyback of Rs 280 Cr and any promoter participation are after the notes date. | Note 12(d), p.198; Note 38, p.226 | GREEN (post-date items NOT FOUND) |
| 6 | Lease burden: lease liability 69,844, ROU 59,672, short-term rent 7,987 above EBITDA; second consecutive lease modification gain (725; 308); IBR flat at 8.00% | Notes 21, 32 (pp.210, 215-216) | WATCH |
| 7 | Gratuity funded ratio 21%, no employer contribution in FY26 or FY25 despite a stated expectation of 1,230; drivers' salary growth assumption 3.00% from 0.05% | Note 15(b), pp.202-205 | WATCH |
| 8 | Receivables clean and improving: 9.7 days, over six months 0.6% of gross; ECL rates raised | Notes 9, 33 (pp.195-196, 221-222) | GREEN |
| 9 | Capex fell to 29,862 from 44,879; land is now 51,883 of gross block (from 14,716 at 1 Apr 2024); capital commitments net 2,888 | Note 2A, 30 (pp.189, 215) | GREEN/WATCH |
| 10 | Audit trail not enabled at database level; new auditor first year; legal fees doubled; stamp duty matter unquantified | Notes 40, 26, 29(g) (pp.226-227, 211, 213-214) | WATCH |

## Questions raised for pass 2 and 3 to test
- Does the PDF page for Note 13(C) (p.200) show the borrowings cash flow of -2,645 or +624? Resolve the mismatch.
- Does the PDF page for Note 34B (p.223) assign the dividend columns as read?
- Do the earlier-page auditors' report and CARO paragraphs (outside notes) mention the audit trail or CPC demand? Out of scope for this stage; hand to the relevant stage.
