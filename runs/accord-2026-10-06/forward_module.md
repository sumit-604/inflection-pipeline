PROVISIONAL FORWARD MODULE, operator request 2026-10-06. Pre-signature: the Mental Model is UNSIGNED and Halt 1 is open. This is NOT a Role 1 valuation and NOT a pipeline decision. The exit multiple comes from the Section 1B framework only. Re-run as Role 1 after the model is signed.

# ACCORD forward module (Accord Transformer & Switchgear Ltd, BSE SME 544710, ACCORDTS)

Run folder runs/accord-2026-10-06. Written 2026-10-06. Scratch arithmetic: work/forward/model.py, calc2.py, peers.py, parse.py (screener pages saved beside them).

## 0. Conventions

Units are Rs Cr unless a cite says otherwise. The AR is in Rs lakh. The prospectus is in Rs thousand. 100 lakh = 1 Cr.

Anchor codes. Page numbers are the `[page N]` markers in the page-marked .txt beside each PDF.
- [AR p.N] inputs/annual-report/Annual_Report_2026.txt, FY26 AR, filed 2026-09-05.
- [Pros p.N] inputs/prospectus/Accord_Prospectus_Feb2026.txt, dated 2026-02-26.
- [Tr LN] inputs/concalls/Concall_Jun_2026_Transcript.txt, call of 2026-06-01, file line N.
- [Deck p.N] inputs/presentation/Investor_Presentation_1.txt, H2 FY26 deck of 2026-06-01.
- [H1upd p.N] announcements/20261005-4575ac94-*.txt, H1 FY27 business update, 2026-10-05. Its figures are "management estimates and are subject to final audit adjustments" [H1upd p.3].
- [Q1upd p.N] announcements/20260727-Q1FY27-business-update.txt, 2026-07-27.
- [Ord YYYYMMDD p.N] order filings in inputs/announcements/.
- (B0x) = stage block or report in outputs/; (B12a), (B12b) = verifier blocks.
- [calc] = my arithmetic on anchored inputs. INFERENCE = my reading, not a filed fact.
- Web facts carry the URL and the access date 2026-10-06.

Binding verifier corrections used throughout:
- Cash excluding all FDs is Rs 7.43 Cr against borrowings of Rs 8.83 Cr (B12a MAJOR 1).
- The "Rs 17 Cr of Aditya Birla orders not filed" claim is NOT SUPPORTED. Rs 19.97 Cr incl GST [Ord 20260629 p.2] is Rs 16.93 Cr ex GST [calc]. Add Rs 20.02 Cr [Ord 20260923-d54c506f p.1]. The sum is Rs 36.95 Cr against Rs 37 Cr [H1upd p.2] (B12b).
- Credibility grade C (B05) and D (B12b) stand side by side.
- The "Tipco" file is Accord's own board outcome with a wrong Subject line (B08).

Share count. 2,05,73,289 shares [AR p.85; AR p.39]. ESOP 2026 adds up to 5,00,000 [Ord 20260926-3aa16089 p.2]. Diluted count = 2,10,73,289 = 2.1073 Cr [calc]. This is the divisor for every EPS below.

Core earnings = operating EBITDA excluding other income, less D&A and interest, taxed at 25.17%. Core PAT = core PBT x 0.7483 [calc; statutory rate 25.17% per B03 2G].

---

## A. Promise-versus-delivery ledger

Scope: every numeric statement on the one call since listing (2026-06-01), plus numeric promises in the prospectus, AR and updates that a later filing tests. Status as at 2026-10-06.

| # | Source and date | Statement (numeric) | Anchor | Later test | Status |
|---|---|---|---|---|---|
| A1 | Call 2026-06-01 | Order book about Rs 156 Cr at 25-May-26 | [Tr L150] | Rs 159 Cr at 22-Jul-26 [Q1upd p.2]; Rs 173 Cr at 30-Sep-26 [H1upd p.2] | HIT |
| A2 | Call | Rs 31 Cr deferred order, 25 of 35 sets made, "around INR21 crores or INR22 crores", revenue "recognized in the current financial year" | [Tr L200-207] | H1 FY27 revenue Rs 52.68 Cr, +90.07% [H1upd p.2] fits. Billing, customer and collection NOT FOUND | PENDING (consistent, not proven) |
| A3 | Call | Second deferred order "around INR3 crores", FY27 | [Tr L208-211] | No filing names it | PENDING |
| A4 | Call | FY27 growth "60% to 80%" = Rs 112.1-126.1 Cr on Rs 70.07 Cr | [Tr L252, L259]; [calc] | H1 Rs 52.68 Cr = 41.8% to 47.0% of that range [calc] | PENDING |
| A5 | Call | FY27 revenue "INR120 crores to INR180 crores" | [Tr L262-264] | H2 FY27 needs Rs 67.32-127.32 Cr [calc]. Section D base H2 is Rs 53.80 Cr. INFERENCE: low end at risk | PENDING (base reading: MISS) |
| A6 | Call | Growth "30% to 50%" from FY28 | [Tr L259-260] | FY28 results, May 2028 | PENDING |
| A7 | Call | EBITDA "13% to 15%", PAT "9% to 11%" (question framed at 2-3 years, B05) | [Tr L479-481] | H1 FY27 margin NOT DISCLOSED [H1upd p.2] | PENDING (Nov-26 results) |
| A8 | Call | Plant: "INR150 crores ... without any hurdles", "up to INR200 crores" | [Tr L274-277] | Capacity arithmetic gives Rs 101.6-150.3 Cr on 900.36 MVA (B04 3D) | PENDING (FY28 test) |
| A9 | Call | Utilisation "75% to 80%" now; "around 90%" at "more than INR120 crores" | [Tr L488-491] | Implied ceilings Rs 88-93 Cr and Rs 133 Cr do not agree with A8 (B05 2C) | PENDING, internally inconsistent |
| A10 | Call | Land "approximately 2.50 lakh" sq ft identified | [Tr L146-147] | 20,300 sq m bought, Rs 8.85 Cr + Rs 1.82 Cr [Ord 20260703 p.1; H1upd p.3]; 2.185 lakh sq ft, 12.6% smaller [calc, B05] | HIT (smaller) |
| A11 | Call | Ground work "after 2 to 3 months", "6 months minimum" to manufacturing | [Tr L284-285] | By 2026-10-06 only land and a building approval exist. Build "9-10 months" from 2026-09-26 [AR p.33] | MISS (slipped about 9 months) |
| A12 | Call | IPO machinery money "for the new plant only" | [Tr L298-299] | Rs 7.00 Cr moved from machinery to building [board 20260903-0bf73e52 p.1-2; AR p.33]; machinery spend nil to 2-Sep-26 [AR p.33] | MISS |
| A13 | Call | MVVNL bid about Rs 125 Cr (of Rs 356 Cr tender) and Torrent about Rs 100 Cr, to open June or early July | [Tr L140-145] | No outcome in [Q1upd] or [H1upd]; no order filing | MISS (silence) |
| A14 | Call | Customer concentration "I will get back to you" | [Tr L423] | No follow-up; AR has no customer table (B03) | MISS |
| A15 | Call | NHEV "approximately INR1,600 crores", "This LOI is already issued" | [Tr L572-575] | No BSE filing of any LOI. [Q1upd p.3] says only "Continued supplying" | MISS (not filed) |
| A16 | Call | NHEV work for "10 to 15" stations by FY27 end | [Tr L584] | Test date 31-Mar-27 | PENDING |
| A17 | Call | Dividend "1 year or 2 years down the line" | [Tr L231-232] | Test FY28 | PENDING |
| A18 | Call | EHV entry "next financial year"; one technical hire "end of February or March" | [Tr L471-474] | No machinery PO; EHV capex NOT FOUND | PENDING |
| A19 | Call | Fixed price if delivery within 3 months; "price variation clause is applicable in 100% supply" beyond; "we will not lose anything into the price variation" | [Tr L319-330, L449-450] | H1 FY27 gross margin against FY26 24.1% (B04). Peers recovered 30% to 60% (B06) | PENDING (Nov-26 results) |
| A20 | Call | FY26 "a year of steady growth and improved profitability" | [Tr L162-163] | FY26 revenue -11.3%, PAT -24.2% [AR p.78; calc] (B12b R1) | MISS (misstatement) |
| A21 | Prospectus 2026-02-26 | Machinery Rs 1,302.67 lakh, all in FY27 | [Pros p.75] (B03) | Nil spent to 2-Sep-26; Rs 700 lakh moved out [AR p.33] | PENDING, slipping |
| A22 | Prospectus | Working capital Rs 275 lakh FY26 and Rs 725 lakh FY27 | [Pros p.75] (B03) | Rs 931.59 lakh used by 2-Sep-26 [AR p.33] | HIT (early) |
| A23 | Prospectus | FY26 receivable days 96, inventory days 83, payable days 56 | prospectus WC table (B03 guidance_table) | Delivered 113 (average basis) and 146 (cost basis) [AR p.64; B03] | MISS |
| A24 | Prospectus | Order book Rs 16,42,575.62 thousand = Rs 164.26 Cr at 18-Jan-26, certified by the auditor | [Pros p.114-115] | Q4 FY26 revenue Rs 24.85 Cr [calc: 70.07 - 45.22, AR p.78, Pros p.110]. Derived 31-Mar-26 book Rs 148.68 Cr (Section C) | PARTIAL (converting slowly) |
| A25 | Prospectus | UGVCL ROBUST 2.0-X PO, Rs 87.50 Cr, dated 17-Jan-26 | [Pros p.115] | Registration of 24-Jun-26 covers 500 kVA only [Ord 20260624-UGVCL p.1]; billing NOT FOUND | PENDING |
| A26 | Prospectus | Schneider EcoXpert to 31-Dec-26; Lucy Electric licence to 28-Sep-27 | [Pros p.124] (B04) | Renewal filings | PENDING |
| A27 | AR 2026-09-05 | Building "within approximately 9-10 months" of member approval (approved 26-Sep-26) | [AR p.33] | About 26-Jun-27 to 26-Jul-27 [calc] | PENDING |
| A28 | AR | "no material changes and commitments ... between the end of the financial year and the date of the report" (report dated 3-Sep-26) | [AR p.39] (B03) | Rs 10.67 Cr land bought 3-Jul-26 [Ord 20260703 p.1] | MISS (statement contradicted) |
| A29 | AR, Q1 update | Installed capacity "1,200+ MVA" | [AR p.6]; [Q1upd p.2] | Certified 900.36 MVA to 31-Dec-25 [Pros p.123] | PENDING (H1 MVA made not disclosed) |
| A30 | Q1 update 2026-07-27 | "new 5,000 MVA transformer manufacturing facility" | [Q1upd p.2] | No capex, no machinery PO filed | PENDING |
| A31 | H1 update 2026-10-05 | Aditya Birla orders Rs 37 Cr ex GST, 119 transformers, "execution within four to five months" | [H1upd p.2] | Filing reconciliation Rs 36.95 Cr (B12b). Execution due about Nov-26 to Feb-27 [calc] | HIT on filing; execution PENDING |

Count. HIT 4 (A1, A10, A22, A31 filing). MISS 8 (A11, A12, A13, A14, A15, A20, A23, A28). PARTIAL 1 (A24). PENDING 18. B05 scored the call alone at 2 delivered, 5 partial, 2 missed. The wider scope adds the prospectus and AR tests, and they add misses. This ledger supports the D reading (B12b) more than the C reading (B05). The H1 FY27 results decide it. The Aditya Birla row is corrected per B12b: the orders are filed.

---

## B. H1 FY27 decomposition (INFERENCE)

H1 FY27 revenue is Rs 52.68 Cr, up 90.07% [H1upd p.2]. H1 margin, profit and cash are NOT DISCLOSED. The figure is a management estimate.

### B1. The FY26 cost structure

| Item | H1 FY26 | H2 FY26 | FY26 | Anchor |
|---|---|---|---|---|
| Revenue | 27.72 | 42.35 | 70.07 | [Deck p.23]; [AR p.78]; [calc] |
| Materials, direct cost and inventory change | 20.57 (74.2%) | 32.63 (77.0%) | 53.20 (75.9%) | [Deck p.23 "Raw Materials" 3,263.14 lakh]; [AR p.78]; [calc] |
| Gross margin | 25.8% | 23.0% | 24.1% | [calc] |
| Employee + other (fixed) | 4.90 | 5.03 | 9.93 | [Deck p.23 310.46 + 192.21 lakh]; [AR p.78]; [calc, CSR 7.70 lakh included] |
| Operating EBITDA ex other income | 2.25 (8.1%) | 4.70 (11.1%) | 6.95 (9.9%) | [Deck p.23 EBITDA 493.64 less OI 24.09]; [AR p.78]; [calc] |
| D&A | 0.29 | 0.34 | 0.63 | [Deck p.23]; [AR p.78] |
| Finance cost | 0.32 | 0.23 | 0.55 | [Deck p.23]; [AR p.78] |

Fixed cost rose 2.6% half on half (4.90 to 5.03) while revenue rose 52.8% [calc]. B04 measured +4.2% on a basis without CSR. The incremental EBITDA margin was about 18% (B04).

### B2. Raw material trend, Apr-Sep 2026 against FY26

| Input | FY26 (Apr-25 to Mar-26) | H2 FY26 | H1 FY27 (Apr-Sep 26) | Change H1 FY27 vs FY26 | Source |
|---|---|---|---|---|---|
| LME copper cash, USD/t, monthly average | 10,815.73 | 11,976.05 | 13,722.47 | +26.9% (vs H2 FY26 +14.6%) | westmetall.com monthly averages, https://www.westmetall.com/en/markdaten.php?action=averages&field=LME_Cu_cash (2026 table) and the same URL with &year=2025, accessed 2026-10-06; averages [calc] from the twelve and six monthly figures |
| Copper, month path | Apr-25 9,192 to Mar-26 12,499 | | Apr-26 12,891; Jun-26 13,574; Aug-26 14,353; Sep-26 14,483 | | same |
| Electrical steel, India, USD/MT | Q1 2026 (Jan-Mar) about 2,065 [calc from -4.43%] | | Q2 2026 (Apr-Jun) 1,974, "receded", -4.43% q/q | about -4% | IMARC, https://www.imarcgroup.com/news/electrical-steel-price-index-q2-2026, published 2026-09-02, accessed 2026-10-06. The page does not say CRGO or CRNO. Q3 2026 (Jul-Sep): PENDING LIVE VERIFICATION. FY26 average: NOT FOUND |
| Transformer oil | | | Danish: "100% plus rise"; Shilchar: "oil prices have become almost double", oil is "8% to 12%" of transformer cost | about +100% (peer statements, May-26) | Peer transcripts via B06 Q5 (D-M26 p8 L300-308; S-M26 p8 L318-320, p7 L275-277). A dated India transformer-oil or base-oil price series: PENDING LIVE VERIFICATION (the IMARC base-oil page holds no India figure) |

Reading. Copper is about 27% dearer in H1 FY27 than the FY26 average. Oil roughly doubled. CRGO eased slightly. Materials were 70.4% of FY26 revenue (B04). Each 1% unrecovered rise across all materials costs 0.70 points of margin (B04). The metal and oil share of materials is NOT FOUND, so the exposure cannot be sized exactly.

Two things cut the H1 exposure (INFERENCE):
1. Inventory at FY26 cost. About Rs 21-22 Cr of the deferred order was built in FY26 [Tr L202-203]. If it was billed in H1, about 40% to 42% of H1 revenue [calc: 21-22 / 52.68] carries FY26 input cost.
2. Short-cycle repricing. Orders taken after the spike were priced at current cost. About Rs 19.4 Cr of filed H1 orders sit in Accord's own fixed-price window (B12b R6).

Peer read. Shilchar's EBITDA ex other income fell from 33.0% (Q1 FY26) to 21.0% (Q4 FY26) to 16.4% (Q1 FY27). Voltamp fell from 17.1% to 14.8% (B06 Q2, calc on screener data). Shilchar recovered "about 50-60% of the price rise" (B06 Q1). Danish has a PV clause on "around 30%" of its book (B06 Q1).

### B3. H1 FY27 margin and profit range

Inputs: revenue Rs 52.68 Cr; D&A Rs 0.335 Cr and interest Rs 0.226 Cr per half (H2 FY26 run-rate, [Deck p.23]); tax 25.17%. Fixed cost per half from Rs 5.03 Cr (H2 FY26) to Rs 5.53 Cr (+10%, the B04 healthy band); centre Rs 5.24 Cr (+4.2% step, B04).

| Gross margin reading | Fixed Rs 5.03 Cr | Fixed Rs 5.24 Cr | Fixed Rs 5.53 Cr | Core PAT at Rs 5.24 Cr |
|---|---|---|---|---|
| 20.6% (FY25 level; pass-through failed) | 5.82 (11.1%) | 5.61 (10.7%) | 5.32 (10.1%) | 3.78 |
| 22.0% (2 points below H2 FY26) | 6.56 (12.5%) | 6.35 (12.1%) | 6.06 (11.5%) | 4.33 |
| 23.0% (H2 FY26 level) | 7.09 (13.5%) | 6.88 (13.1%) | 6.59 (12.5%) | 4.73 |
| 24.1% (FY26 level; pass-through held) | 7.67 (14.6%) | 7.46 (14.2%) | 7.17 (13.6%) | 5.16 |
| 25.8% (H1 FY26 level) | 8.56 (16.3%) | 8.35 (15.9%) | 8.06 (15.3%) | 5.83 |

Cells are operating EBITDA ex other income in Rs Cr (margin) [calc, work/forward/calc2.py].

INFERENCE, the most evidenced range: H1 FY27 operating EBITDA Rs 6.1-7.5 Cr, a margin of 11.5% to 14.2%, centre about 13.1%. Core PAT Rs 4.1-5.2 Cr. The centre alone exceeds FY26 full-year core PAT of Rs 4.32 Cr [calc: (605.75 - 28.78) lakh x 0.7483].

Two readings and the separating observation:
- Reading 1: the deferred order carried FY26 cost and new orders were repriced. Gross margin holds near 23% to 24%. Margin 13% to 14%.
- Reading 2: fixed-price orders in hand took the oil and copper rise, as at Shilchar. Gross margin near 20.6% to 22%. Margin 10% to 12%.
- Separating observation: H1 FY27 gross margin after materials, direct cost and inventory change, against 24.1%. Filed with the H1 results, about November 2026.

---

## C. Order book bridge, FY26 by half to H1 FY27

Identity: opening + inflow - execution = closing. Execution = revenue (assumes every rupee of revenue draws on the book, no cancellations, ex GST throughout).

| Half | Opening | Inflow | Execution (revenue) | Closing | Status of each figure |
|---|---|---|---|---|---|
| H1 FY26 (Apr-Sep 25) | NOT FOUND | NOT FOUND | 27.72 [calc: 70.07 - 42.35; AR p.78, Deck p.23] | 26.76 to 36.03 (derived, = H2 opening) | Opening and inflow would be in the DRHP or an H1 FY26 filing; neither is in the corpus |
| H2 FY26 (Oct-25 to Mar-26) | 26.76 to 36.03 (derived) | 155.00 to 164.27 (derived) | 42.35 [Deck p.23] | 148.68 (derived) | See notes 1-3 |
| Anchor inside H2 FY26 | | | | 164.26 at 18-Jan-26 (filed) [Pros p.114-115] | Filed, auditor certificate dated 6-Feb-26 |
| H1 FY27 (Apr-Sep 26) | 148.68 (derived) | 77 (filed) [H1upd p.2] | 52.68 (filed estimate) [H1upd p.2] | 173 (filed) [H1upd p.2] | Interim points: about 156 at 25-May-26 [Tr L150]; 159 at 22-Jul-26 [Q1upd p.2] |

Notes (all [calc]):
1. Closing 31-Mar-26 = 173 - 77 + 52.68 = 148.68.
2. H2 FY26 inflow, lower bound. Orders in the 18-Jan-26 book dated 1-Oct-25 or later carry Rs 153.68 Cr unexecuted plus Rs 1.32 Cr already executed = Rs 155.00 Cr [Pros p.114-115, rows 16-67]. Upper bound. Q4 FY26 revenue is Rs 24.85 Cr. The book fell from 164.26 to 148.68, so post-18-Jan inflow is at most 24.85 - 15.58 = Rs 9.27 Cr. Inflow range Rs 155.00-164.27 Cr.
3. Opening 1-Oct-25 = 148.68 + 42.35 - inflow = Rs 26.76-36.03 Cr. Cross-check: orders dated before 1-Oct-25 still open at 18-Jan-26 were Rs 10.58 Cr, of which Rs 5.74 Cr were dated before 1-Apr-25 [Pros p.114, rows 1-15]. Orders 9 to 17 months old were still unbilled.
4. Two lines dominate the January book. UGVCL ROBUST 2.0-X Rs 87.50 Cr (53%), and LPPL-02 Rs 31.50 Cr (19%, 35 sets; INFERENCE per B03 that it is the deferred order) [Pros p.115].

### C1. Where the Rs 173 Cr executes: H2 FY27 against FY28

The composition of the Rs 173 Cr is NOT DISCLOSED [H1upd p.2]. Filed delivery windows on H1 FY27 orders:

| Order (filing) | Value ex GST | Window | Falls in | Anchor |
|---|---|---|---|---|
| Wind turbine transformers, Gadag-1, "Leading Private Sector EPC" (part of Aditya Birla Rs 37 Cr) | 16.93 [calc] | "within 5 Months" of 29-Jun-26 | H2 FY27 (by about 29-Nov-26) | [Ord 20260629 p.2] |
| 57 wind units 3.6 and 5.5 MVA, Aditya Birla Renewables, Bhuj | 20.02 | "Within 4-5 months from date of PO" (23-Sep-26) | H2 FY27 (Jan to Feb 2027) | [Ord 20260923-d54c506f p.1] |
| Private Sector Electrical Company, 22 transformers; Good Earth | 8.39 + 0.245 = 8.64 | 1 month; 2-3 months | H2 FY27 | [Ord 20260929 p.2-3] |
| Good Earth inverter duty, Karan Power, Global Energy | 5.28 | "Within 2-3 months" | H2 FY27 | [Ord 20260923-84dda8a9 p.1-2] |
| Ultra Mega Power, Ventora | 1.92 | "Within 3 Months" | H2 FY27 | [Ord 20260907 p.1-2] |
| Sunsure; Shalimar | 0.51 + 0.50 = 1.01 | 3 months; 8-10 weeks | H2 FY27 | [Ord 20260904; 20260905] |
| Sum with filed H2 windows | 53.80 [calc] | | H2 FY27 | 31.1% of 173 [calc] |
| UGVCL ROBUST 2.0-X (if still open) | 87.50 | Utility orders run "8 months, 9 months" to "one year" [Tr L319-320], so about Sep-26 to Jan-27 from 17-Jan-26 | H2 FY27 on schedule; but billing NOT FOUND and the registration covers 500 kVA only (Rs 20.12 Cr of the PO) | [Pros p.115]; [Ord 20260624-UGVCL p.1] |
| Remainder | 31.70 [calc: 173 - 53.80 - 87.50] | NOT DISCLOSED | Unclassified | |

Reading. Filed windows put Rs 53.80 Cr (31%) in H2 FY27. UGVCL (51%) is the swing line. Section D's base treats UGVCL as FY28 or later, because no billing or full-rating registration is filed. The bull credits the 500 kVA line (Rs 20.12 Cr) in H2 FY27. On that split, H2 FY27 carries Rs 53.80-73.92 Cr and FY28 inherits Rs 99.1-119.2 Cr of the book [calc].

Capacity flag (INFERENCE). The 119 Aditya Birla units are wind units of 3.6 and 5.5 MVA. The September lot is 57 units. That leaves 62 units of 3.6 MVA in the June lot [calc, if the June filing is the rest of the Rs 37 Cr]. That is 428-537 MVA for Rs 36.95 Cr, Rs 6.9-8.6 lakh per MVA [calc]. Half-year certified capacity is 450.18 MVA [calc: 900.36 / 2; Pros p.123]. The lot alone fills a half-year of certified MVA. Either plant MVA for large units exceeds the basket figure, or the lot slips. The H1 MVA made, NOT DISCLOSED, separates the two.

### C2. Fixed-price against price-variation share

- Accord: NOT DISCLOSED. No clause text, share, weights or lag in any filing (B04).
- Accord's own rule: fixed price within 3 months; PV clause beyond [Tr L319-330]. By that rule, Rs 16.85 Cr of the Rs 53.80 Cr H2-window orders (31%) are fixed price [calc: 8.64 + 5.28 + 1.92 + 1.01]. The Rs 36.95 Cr wind lots (69%) sit at 4-5 months, between the windows the MD described (B12b R6).
- Peer benchmark: Danish "around 30%" of a Rs 500 Cr+ book on PV; recent orders "all on firm" (B06 Q1). Shilchar recovered 50-60% on fixed-price orders (B06 Q1).

---

## D. FY27 and FY28 projections, bear / base / bull (FY29 to FY31 added for the exit, A18.0)

### D1. Revenue build (Amendment 26.1)

Base basis: ORDER-BOOK for FY27, then the Amendment 14 fade.
- FY27 = H1 Rs 52.68 Cr [H1upd p.2] + H2 Rs 53.80 Cr (filed orders with H2 windows, Section C1) = Rs 106.48 Cr [calc].
- Cross-checks: H1 annualised Rs 105.36 Cr [calc]; peer H1 shares give Rs 104-138 Cr (B06); guidance Rs 120-180 Cr [Tr L263]. The base sits below the guidance low end. Grade C/D gives no basis to take guidance at face value.
- H2 capacity cross-check: Rs 53.80 Cr is below the best half on record, H2 FY25 Rs 57.53 Cr [Deck p.23]. The MVA cross-check is ambiguous (Section C1 flag).
- FY28 to FY31: Emerging Moat class is NONE, score 8.0 (B07). Amendment 14: "Fades immediately (industry growth from Year 1)". Industry anchor: 7.6% growth on a Rs 33,000 Cr domestic market (B09). NAMED ASSUMPTION: 7.6% a year from FY28.
- Historical cross-check: revenue CAGR FY23-FY26 19.8% (B03). Base FY26-FY28 CAGR 27.9% [calc]. Divergence 8.1 points, under the 10-point ledger trigger.

Bear (chunk 07: the lower of historical CAGR - 5%, industry growth, or 1-2 triggers failing):
- FY27: the wind lots slip as the FY26 order did. H2 FY27 = H2 FY26 level Rs 42.35 Cr. FY27 = Rs 95.03 Cr [calc].
- FY28 and FY29: capped at Rs 101.6 Cr, the 900.36 MVA plant at 9M FY26 realisation of Rs 11.29 lakh per MVA (B04 3D). The new plant slips one year.
- FY30 and FY31: +7.6% a year once the new plant runs.

Bull (no guidance at face value on grade C/D):
- FY27: base plus the UGVCL 500 kVA line, Rs 20.12 Cr [Pros p.115; Ord 20260624]. FY27 = Rs 126.60 Cr.
- FY28: 900.36 MVA x 90% guided utilisation [Tr L490] x Rs 16.69 lakh per MVA (FY25 realisation, B04) = Rs 135.24 Cr [calc].
- FY29 to FY31: +30% a year, the low end of the post-FY27 guidance [Tr L259-260]. Labelled: bull only. Needs the new plant at the top of the funded-capacity range (Section E).

### D2. Margin build (Amendment 26.2)

Base bridge from FY26 9.91% [AR p.78; calc]:

| Lever | Effect | Evidence | Confirm-by |
|---|---|---|---|
| Current margin | 9.91% | [AR p.78] | n/a |
| Gross margin: H2 FY26 level 23.0% replaces FY26 24.1% | -110 bps on gross | [Deck p.23]; copper +27%, oil about +100% (Section B2) | H1 FY27 results, Nov-26 |
| Mix shift to wind units | 0 bps. No evidence of margin per kVA by product. Lever dropped | B04 3D | n/a |
| Operating leverage: fixed cost Rs 10.47 Cr in FY27 (H2 FY26 x 2 x 1.042), +8% a year after | +436 bps in FY27 | H2 FY26 fixed +2.6% to +4.2% on revenue +52.8% [Deck p.23; B04]; 8% salary escalation [AR p.93 actuarial note, B03] | H1 FY27 fixed cost at or below Rs 5.53 Cr |
| Base margin FY27 | 13.17% [calc] | | |
| Base margin FY28 to FY31 | 13.13%, 13.09%, 13.06%, 13.02% [calc] | fixed cost grows 8%, revenue 7.6% | |

The lift is +326 bps over FY26, under the 400 bps Rule F trigger.

Bear margin: trailing three-year average operating EBITDA margin ex other income, from filed figures:
- FY24 5.38% [Pros p.86 EBITDA 26,727.95 less other income 609.49, Pros p.182, on revenue 4,85,369.15 thousand, Pros p.110; calc].
- FY25 11.29% [Pros p.86 EBITDA 91,013.90 less other income 1,778.69 on revenue 7,90,225.33; calc]. On the AR comparative basis FY25 is 11.15% [AR p.78; calc].
- FY26 9.91% [AR p.78; calc].
- Average 8.86% [calc] (8.81% with the AR comparative for FY25).
This is not a margin-reset name under OR-11, so the trailing average governs.

Bull margin: gross margin 24.1% (FY26, the "pass-through held" reading) over the base fixed-cost path, with fixed cost scaled to revenue from FY29. Result 15.7% to 15.8% [calc].

Rule conflict, stated: chunk 07 sets the bull margin as the highest of the last five years (FY25 11.29%) or guidance on grade A/B. Both sit below the base bridge. A bull below base is not usable, so the bull uses the evidence bridge above. The orchestrator may want this ruled.

### D3. Lines below EBITDA

- D&A. FY27 Rs 0.67 Cr (H2 FY26 Rs 0.335 Cr x 2) [Deck p.23]. FY28 Rs 0.82 Cr adds the building, Rs 7.00 Cr at 3.17% (30-year Schedule II life [AR p.80 states Schedule II lives]) for 8 months. FY29 Rs 1.29 Cr adds machinery, Rs 6.03 Cr at 6.67% (15-year life). FY30 Rs 1.39 Cr and FY31 Rs 1.49 Cr add depreciation on maintenance capex at the FY26 level of Rs 1.46 Cr [AR p.79]. Bear lags each step one year.
- Interest. Rs 0.55 Cr flat, FY26 level [AR p.78]. Bear Rs 0.59 Cr, the FY25 level [AR p.78].
- Other income. Excluded from core. FY26 other income was Rs 0.29 Cr, mostly FD interest and warehouse charges [AR Note 20 p.90].
- Tax 25.17%. Core PAT = core PBT x 0.7483.
- Shares 2.1073 Cr diluted (Section 0).
- ESOP cost: NOT IN ANY CASE. The grant price is NOT FOUND. Sensitivity: at the Rs 10 floor [AR p.35], intrinsic value at CMP is Rs 3.76 Cr [calc: (85.2 - 10) x 5,00,000]. Over a 3-year vest that is Rs 1.25 Cr a year. FY28 base core EPS would fall by Rs 0.45, about 9% [calc].

### D4. Projection table (Rs Cr; EPS in Rs)

| Line | Bear FY27 | Bear FY28 | Base FY27 | Base FY28 | Bull FY27 | Bull FY28 | Evidence |
|---|---|---|---|---|---|---|---|
| Revenue | 95.03 | 101.60 | 106.48 | 114.57 | 126.60 | 135.24 | D1 |
| Gross margin | n/a (margin set directly) | n/a | 23.0% | 23.0% | 24.1% | 24.1% | D2 |
| Operating EBITDA ex OI | 8.42 | 9.00 | 14.02 | 15.04 | 20.04 | 21.28 | D2 |
| EBITDA margin | 8.86% | 8.86% | 13.17% | 13.13% | 15.83% | 15.74% | D2 |
| D&A | 0.67 | 0.67 | 0.67 | 0.82 | 0.67 | 0.82 | D3 |
| EBIT | 7.75 | 8.33 | 13.35 | 14.22 | 19.37 | 20.46 | [calc] |
| Interest | 0.59 | 0.59 | 0.55 | 0.55 | 0.55 | 0.55 | D3 |
| Core PBT | 7.16 | 7.74 | 12.80 | 13.67 | 18.82 | 19.91 | [calc] |
| Core PAT (x 0.7483) | 5.36 | 5.79 | 9.58 | 10.23 | 14.08 | 14.90 | [calc] |
| Diluted shares (Cr) | 2.1073 | 2.1073 | 2.1073 | 2.1073 | 2.1073 | 2.1073 | Section 0 |
| Core EPS (Rs) | 2.54 | 2.75 | 4.54 | 4.85 | 6.68 | 7.07 | [calc] |

Extension for the exit (A18.0 requires Year 4 and later):

| Line | Bear FY29 | Bear FY30 | Bear FY31 | Base FY29 | Base FY30 | Base FY31 | Bull FY29 | Bull FY30 | Bull FY31 |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | 101.60 | 109.32 | 117.63 | 123.28 | 132.65 | 142.73 | 175.82 | 228.56 | 297.13 |
| EBITDA | 9.00 | 9.69 | 10.42 | 16.14 | 17.32 | 18.58 | 27.67 | 35.97 | 46.76 |
| Core PAT | 5.68 | 5.84 | 6.32 | 10.70 | 11.51 | 12.38 | 19.33 | 25.46 | 33.46 |
| Core EPS (Rs) | 2.70 | 2.77 | 3.00 | 5.08 | 5.46 | 5.87 | 9.17 | 12.08 | 15.88 |

FY26 core EPS for reference: Rs 4.32 Cr / 2.1073 = Rs 2.05 [calc].

### D5. Capacity reconciliation

- Certified 900.36 MVA to 31-Dec-25 [Pros p.123]. Claimed "1,200+" [AR p.6; Q1upd p.2].
- At 100% fill: Rs 101.6 Cr at 9M FY26 realisation (Rs 11.29 lakh per MVA); Rs 150.3 Cr at FY25 realisation (Rs 16.69 lakh) (B04 3D).
- H1 FY27 Rs 52.68 Cr. INFERENCE: if Rs 21-22 Cr of it was FY26-built inventory [Tr L202-203], H1 FY27 new output was Rs 30.7-31.7 Cr. That is 184-281 MVA across the two realisations, 41% to 62% of half-year certified capacity [calc]. H1 revenue overstates H1 plant output. It is not proof of a Rs 105 Cr plant.
- Base FY27 Rs 106.48 Cr needs at least Rs 11.83 lakh per MVA at 100% fill [calc]. Base FY28 Rs 114.57 Cr needs Rs 12.72 lakh at 100% fill, or Rs 14.14 lakh at 90% [calc]. Both sit between the two readings. A UGVCL-heavy FY28 (Rs 17.18 lakh per MVA, B04) supports it. A wind-heavy FY28 (Rs 6.9-8.6 lakh) does not.
- Base FY29 Rs 123.28 Cr exceeds the low-reading ceiling. It needs the new plant or FY25-type realisation.
- Separating observation for all of this: H1 FY27 MVA made and mix. NOT DISCLOSED.

---

## E. FY28 capacity check and the new plant

Can the existing plant deliver FY28?
- Base FY28 Rs 114.57 Cr: yes only on mixed-to-distribution realisation (D5). On the 9M FY26 mix the ceiling is Rs 101.6 Cr, which is the bear.
- Bull FY28 Rs 135.24 Cr: yes only on FY25 realisation at 90% fill [Tr L490].

New plant, Khairthal-Tijara:

| Item | Amount | Status | Anchor |
|---|---|---|---|
| Land, 20,300 sq m | 8.85 + 1.82 = 10.67 | Bought 3-Jul-26. Costs are 20.6% of price [calc]. Payment source NOT FOUND. Land is not an IPO object | [Ord 20260703 p.1]; [AR p.33]; (B08) |
| Building | 7.00 | IPO money moved from machinery, approved 26-Sep-26. "9-10 months" | [AR p.33]; [board 20260903-0bf73e52 p.1-2] |
| Machinery | 6.03 (1,302.67 - 700.00 lakh) | IPO object remains. PO nil. Nil spent to 2-Sep-26 | [AR p.33] |
| Working capital residual | 0.68 | IPO | [AR p.33] |
| IPO unused at 2-Sep-26 | 13.71 | Sum of the three IPO lines | [AR p.33] |
| EHV plant and "5,000 MVA" facility capex | NOT FOUND | Claim only | [Q1upd p.2]; [Tr L471-474] |

Funding:
- Building and machinery: IPO money, Rs 13.03 Cr [AR p.33].
- Land: NOT FOUND. Ex-IPO cash at 31-Mar-26 was Rs 1.93 Cr [calc: 22.33 - 20.40]. Cash ex all FDs was Rs 7.43 Cr against borrowings Rs 8.83 Cr (B12a). INFERENCE: the land needed borrowings or a temporary use of IPO money. The bank trail is the open item (B08 tripwire).
- 5,000 MVA: at Shilchar's capex intensity, Rs 120 Cr for 6,500 MVA = Rs 1.85 lakh per MVA (B06 Q8), 5,000 MVA costs about Rs 92 Cr [calc]. Funded today: Rs 13.03 Cr. Gap about Rs 79 Cr [calc]. Debt or equity: NOT FOUND. INFERENCE: a raise is likely before the 5,000 MVA claim can exist. The diluted share count above does not include it.
- Funded capacity: Rs 13.03 Cr / Rs 1.85 lakh per MVA = about 704 MVA [calc, peer intensity]. At Rs 11.29-16.69 lakh per MVA, full fill gives Rs 79.5-117.5 Cr a year [calc].

Implied start date:
- Building complete about 26-Jun-27 to 26-Jul-27 [AR p.33; calc].
- Machinery lead time: NOT FOUND. No PO.
- Peers: Shilchar 12 to 18 months from decision to production; Danish phases ran 4 months or more late; a new rating needs a type test of 6 to 9 months (B06 Q8).
- INFERENCE: production on existing ratings not before Q3 FY28 (Oct-Dec 2027), and only if machinery is ordered by about April 2027. EHV revenue not before FY29 to FY30.

FY28 revenue the new plant can add:
- Base: nil. No commissioning filing and no machinery PO, so Rule B gives no CAPACITY credit.
- Bull: about Rs 9.9-14.6 Cr if 704 MVA runs one quarter at 50% [calc, INFERENCE]. Not added to the bull FY28 row, which already assumes the existing plant at FY25 realisation.
- From FY29, the base 7.6% path and the bear recovery both need this plant.

---

## F. Forward valuation at CMP

CMP Rs 85.2 and market cap Rs 175.0 Cr (screener, 2026-10-06, manifest.yaml). Operator said about Rs 86 and Rs 177 Cr.

EV at the latest filed balance sheet, 31-Mar-26:
- Borrowings Rs 8.83 Cr [AR p.77: 47.22 + 836.24 lakh]. Cash and bank Rs 22.33 Cr [AR p.77], of which Rs 20.40 Cr is unspent IPO money [AR p.73 CARO x(a); B02].
- EV (a), all cash: 175.0 + 8.83 - 22.33 = Rs 161.50 Cr [calc].
- EV (b), IPO money treated as committed to capex: 175.0 + 8.83 - 1.93 = Rs 181.90 Cr [calc].
- Caveat: Rs 10.67 Cr of land was bought after 31-Mar-26 with a source NOT FOUND. EV (b) is the closer reading of today's position.

| Case and year | Core EPS | P/E at Rs 85.2 | Mcap / EBIT | EV(a) / EBIT | EV(b) / EBIT |
|---|---|---|---|---|---|
| Trailing FY26 (core) | 2.05 | 41.6x | 27.7x | 25.6x | 28.8x |
| Bear FY27 | 2.54 | 33.5x | 22.6x | 20.8x | 23.5x |
| Bear FY28 | 2.75 | 31.0x | 21.0x | 19.4x | 21.8x |
| Base FY27 | 4.54 | 18.7x | 13.1x | 12.1x | 13.6x |
| Base FY28 | 4.85 | 17.5x | 12.3x | 11.4x | 12.8x |
| Bull FY27 | 6.68 | 12.8x | 9.0x | 8.3x | 9.4x |
| Bull FY28 | 7.07 | 12.0x | 8.6x | 7.9x | 8.9x |

FY26 core EBIT = Rs 6.95 Cr - Rs 0.63 Cr = Rs 6.32 Cr [AR p.78; calc].

Live peer table. Source: screener.in company pages fetched with curl, 8-second spacing, on 2026-10-06 (saved in work/forward/*.html). Market cap is live. Debt and cash are 31-Mar-26 (balance sheet; cash from the "Cash Equivalents" line of the Other Assets schedule). EBIT = operating profit - depreciation, which excludes other income.

| Peer | Basis | Mcap | Debt | Cash | TTM op profit | Dep | EBIT (op) | PBT + int | EV / EBIT | Mcap / EBIT | P/E (screener) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Transformers & Rectifiers (TARIL) | consolidated, TTM to Jun-26 | 8,516 | 457 | 141 | 388 | 29 | 359 | 416 | 24.6x | 23.7x | 32.9x |
| Voltamp (VOLTAMP) | standalone, TTM to Jun-26 | 10,668 | 1 | 74 | 363 | 15 | 348 | 421 | 30.4x (27.6x net of Rs 995 Cr investments) | 30.7x | 33.6x |
| Shilchar (SHILCTECH) | standalone, TTM to Jun-26 | 4,681 | 0 | 44 | 160 | 4 | 156 | 184 | 29.7x (28.4x net of Rs 202 Cr investments) | 30.0x | 34.0x |
| Danish Power (DANISH) | consolidated, FY26 (half-yearly reporter) | 1,989 | 2 | 92 | 92 | 7 | 85 | 92 | 22.3x | 23.4x | 28.8x |
| Indo Tech (INDOTECH) | standalone, TTM to Jun-26 | 3,558 | 5 | 114 | 128 | 5 | 123 | 135 | 28.0x | 28.9x | 35.8x |
| Supreme Power (SUPREMEPWR) | FY26 annual (no TTM column) | 598 | 46 | 9.74 | 29 | 2 | 27 | 29 | 23.5x | 22.1x | 28.6x |
| Median | | | | | | | | | 26.3x | 26.3x | 33.3x |

Reading:
- On trailing earnings, Accord's EV(a)/EBIT of 25.6x sits at the peer median, 26.3x. Peers earn 14% to 29% EBITDA and 21% to 51% ROCE (screener ROCE: TARIL 23.3, VOLTAMP 23.5, SHILCTECH 50.7, DANISH 22.2, INDOTECH 40.4, SUPREMEPWR 21.5). Accord earns 9.9% and 22% operational ROCE.
- On base FY28, Accord trades at 11.4x to 12.8x EV/EBIT. The discount to peers is the market not paying for the FY27-FY28 earnings yet. On bear FY28, 19.4x to 21.8x.
- The peer P/E median of 33.3x is above the 25x sector cap. Any relative reading is capped at 25x. The excess is a cap-review flag under Amendments 20.6 and 20.7, never priced in.
- Step 1C (adjusted peer base, governing-multiple test) is Role 1 work and is not done here. This table is live and dated, but it is not a Section 1B input.

---

## G. Entry price

### G1. Section 1B destination P/E, pillar by pillar (Track 2, additive)

Opening gates:
- CONVERTER gate (A17.0). (a) Inputs are quoted commodities: yes. (b) Tender pricing with no IP: yes (B04 price-taker). (c) Gross margin co-moves with input price: mixed. H1 to H2 FY26 copper rose 24% [calc, westmetall] and gross margin fell from 25.8% to 23.0% [calc]. FY25 to FY26 gross margin rose 3.5 points while copper rose. Ambiguous, so CONVERTER by the OR-6 default, ambiguity stated. Effect: Pillar 1 must use through-cycle ROCE, and rupee WC trends cannot feed Pillar 2.
- FTTCP has not run. FTTCP ROCE forward verdict: NOT FOUND. Module B2: NOT FOUND. Every pillar line below is provisional.

Row A, Pillar 1, ROCE base:
- Statutory FY26 ROCE 13.25%: EBIT Rs 660.79 lakh on capital employed Rs 4,985.27 lakh (total assets 8,365.58 less current liabilities 3,380.31) [AR p.77-78; calc].
- Route A applies. Idle IPO money Rs 2,040.21 lakh is 40.9% of capital employed, above 20% [calc]. The deployment plan has a filed timeline inside 24 months [AR p.33].
- Operational ROCE: strip IPO money (Rs 2,040.21 lakh) and FD interest (Rs 11.25 lakh, AR Note 20 p.90). Rs 649.54 / Rs 2,945.06 lakh = 22.06% [calc]. Route B is also present (deferral-depressed numerator) and is suppressed per single credit.
- Converter through-cycle: the listed history is under one year. The rule takes the midpoint of current and trough. The operational 22.06% is itself the lowest of the four filed years (FY23-FY25 33.0%, 39.8%, 37.8%, B01). The input stays 22.06%.
- Base PE = 0.5 x 22.06 + 7.5 = 18.53, rounded 18.5x.
- If FTTCP later reads RECOVERING above 60% with strong catalysts, the midpoint with the FY29 operational ROCE applies. That ROCE is not computed here.

Row B, Pillar 2, cash multiplier:
- Cumulative CFO/PAT FY23-FY26 = -0.18 (B01). Band: "below 30% or CFO negative" = 0.80x.
- Structural test: INDETERMINATE (FLAG-CASH). OR-5 is open: no multiplier rule exists for INDETERMINATE.
- Governing reading: 0.80x band, no offset. The offset needs a growth-induced finding that H1 FY27 cash flow has not yet given.
- Reading S, 0.70x: UGVCL is a state DISCOM, Tier 3. If it exceeds 25% of revenue, the 0.65-0.75x structural rule binds "regardless of growth". In base FY28 the UGVCL PO alone could be most of revenue (Section C1).
- Reading G, 0.90x: growth-induced, with the +0.10 offset for base core PAT CAGR FY26-FY29 of 35.3% [calc].
- Separating observation: H1 FY27 CFO against PAT, closing receivables against Rs 28.9 Cr, and UGVCL's share of billing.

Row C = 18.5 x 0.80 = 14.80x.

Row D, Pillar 3:
- A16 gate: operational ROCE 22.06% exceeds the 13.5% default (OR-21). Eligible, provisional until B2 runs.
- 3a: two criteria qualify on filed evidence. (i) Capex-embedded growth: (7.00 + 6.03) x fixed-asset turnover 8.81x / 70.07 = 164% [calc; B12a FAT; AR p.33]. (ii) Order book not credited in base FY27 revenue: Rs 119.2 Cr = 1.70x FY26 revenue [calc]. Single-credit split: the Rs 53.80 Cr credited in FY27 base revenue is excluded from this test. The SOM criterion fails the capacity cross-check. The grade criterion fails.
- 3a award: +2x on grade C (cap +2x); +0x on grade D.
- 3b: EM 8.0 < 25 = +0x (B07).
- 3c: book / revenue = 2.47x on FY26, under 2.5x; 1.82x on TTM Rs 95.03 Cr [calc] = +0x.
- D = +2.0x (grade C) or +0x (grade D).

Row E, Strategic premium: no strategic scarcity filed = +0x.

Row F = 14.80 + 2.0 = 16.80x (grade C). Row F2: UA does not apply. Listed 2026-03-02, under 12 months; EM 8.0 < 25 (B00). F2 = 16.80x.

Row G, sector cap: "Cables / Industrial products" 25x (manifest). No UA, so no quality uplift. G2: no Category-Break Override (no binding contract, no competitor-absence source). G3 = 25x.

**Row H = min(16.80, 25) = 16.80x.** Range ±7.5%: 15.5x to 18.0x [calc, rounded to 0.5x]. The cap does not bind.

Sensitivity of H to the two open readings:

| Pillar 2 reading | Grade C (3a +2x) | Grade D (3a +0x) |
|---|---|---|
| 0.70x (Tier 3 DISCOM) | 14.95x | 12.95x |
| 0.80x (band, governing) | **16.80x** | 14.80x |
| 0.90x (growth-induced) | 18.65x | 16.65x |

Track 1 (RRM) cross-check:
- r = 14% small/micro base. No numeric durability or governance adjustment exists in frameworks/ (chunk 15 NOT FOUND). Complexity +0.5 is arguable on the ABL Electricals RPT density; not applied.
- RRM = 1 + (13.5 - 14.0) x 0.12 = 0.94. Track 1 = 14.80 x 0.94 = 13.91x [calc].
- Divergence from Track 2: 17.2%, above 15%. OR-1 is open; as written, the more conservative track sets the entry zone.

A18.0 Year 4-5 story: EM NONE usually triggers a one-turn exit haircut. The Tijara land and building are filed, so the base carries a Year 4-5 capacity story and no haircut. Flag: if no machinery PO is filed by 31-Mar-27, apply the haircut. H becomes 15.80x and the Track 2 entry Rs 47.5 [calc].

### G2. Exit basis and the exit year (A18.1)

- Earnings basis: one-year forward, both ends.
- At entry (Oct-2026), the forward year is H2 FY27 plus H1 FY28. Half-year profit is not disclosed, so FY28 stands in for it (the operator's named basis). This makes the entry P/E look slightly lower.
- At exit (Oct-2029, 3 years later), the same offset points to FY31. Exit price = H x FY31 core EPS. That is why D4 runs to FY31.
- No option slice enters the exit. NHEV (claim, not filed), the Moscow MoU and EHV have no filed resolution event. Under A18.2 each is narrative at zero value.

### G3. Entry price table (base EPS FY31 Rs 5.87)

| Line | Track 2 (H 16.80x) | Track 1 (13.91x) |
|---|---|---|
| Exit fair value, end Year 3 = H x FY31 EPS | 98.7 | 81.7 |
| Entry for 25% CAGR = exit / 1.953 | **50.5** | **41.8** |
| Entry for 30% CAGR = exit / 2.197 | 44.9 | 37.2 |
| Alternative: exit on FY30 EPS (Rs 5.46) | 91.7, entry 47.0 | 76.0, entry 38.9 |
| Fair value today = H x FY28 EPS (Rs 4.85) | 81.6 | 67.5 |

[calc, work/forward/calc2.py]

Entry zone: **Rs 41.8 to Rs 50.5.** As written under OR-1, the Track 1 bottom governs. CMP Rs 85.2 is 69% above the Track 2 entry and 4.4% above the base fair value today [calc].

Bear and bull exit values (Track 2 H on each case's FY31 EPS):
- Bear: 16.80 x 3.00 = Rs 50.4. On the lowest H cell (12.95x), Rs 38.8.
- Base: Rs 98.7.
- Bull: 16.80 x 15.88 = Rs 266.8. On the 18.65x cell, Rs 296.2. The cap does not bind.

Returns from CMP Rs 85.2 over 3 years [calc]:
- Bear -16.1% a year. Base +5.0% a year. Bull +46.3% a year.
- Weighted, grade C (35/45/20): weighted exit value Rs 115.4, 10.6% a year on the weighted value; weighted CAGR 5.9%.
- Grade D (45/40/15): weighted exit value Rs 102.2, 6.2% a year; weighted CAGR 1.7%.
- Upside / downside (4F): (98.7 - 85.2) / (85.2 - 50.4) = 0.39x, against the 2x test. FAILS.

Hurdle Ratio (feasibility only, OR-2):
- Base EPS CAGR FY28-FY31 6.56%; current P/E on FY28 = 17.55x.
- HR(base) = 1.0656^3 x (16.80 / 17.55) = 1.16. HR(bull, grade C/D = base + 5 points) = 1.33. Threshold Tier A 1.953.
- Band: **STOP** (infeasible even on bull). It caps no verdict.
- Tier: A, hurdle 25%. Tier B fails on promoter CAUTION and FLAG-CASH.

### G4. Amendment 19 FV CAGR and return source

- FV path, base, Track 2 [calc]: today Rs 81.6 (FY28 EPS); end-Year-1 Rs 85.3 (FY29); end-Year-2 Rs 91.7 (FY30); end-Year-3 Rs 98.7 (FY31). Net debt held at the 31-Mar-26 figure.
- **FV CAGR over the hold: 6.6% (today Rs 81.6 to end-Year-3 Rs 98.7, Track 2, base case). DISCOUNT-CLOSER.**
- Decomposition: 100% of fair value is core earnings; no option slice. Growth drag is the EM NONE fade to 7.6%. No re-rating lever remains: the forward P/E of 17.5x already sits above H of 16.8x.
- Zone reachability: the entry needs a 41% to 51% fall from CMP [calc]. Price drift alone makes that market-unlikely. The realistic path is an event-driven FV step: an H1 FY27 margin of 13% or more with positive CFO, plus a filed machinery PO. That would lift the fade class and Pillar 2. It is not in the base.
- Thesis line in DISCOUNT-CLOSER form: the return is the discount closing from about Rs 85 to Rs 99, not the business compounding.

Provisional transition-matrix read (Stage 13 applies it): proof gate NOT FIRED; ugliness ARTIFACT (provisional, dossier B5); recognition gap CLOSED on base (17.5x forward against 16.8x destination; R2 neighbourhood 15x to 17x). That cell is PRICED NARRATIVE (TRAP). The gap is open only on bull earnings (12.0x).

Price decomposition at Rs 85.2 (A24, provisional, Track 2 H):
- T1 (trailing core EPS Rs 2.05 x 16.80) Rs 34.4 = 40%.
- Base increment to FY28 at H: Rs 47.1 = 55%. FTTCP C.2 probabilities NOT FOUND, so the T2/T3 split cannot be made.
- Residual about 4% if the whole increment is treated as p ≥ 0.50; larger if not.

---

## H. Red-flag check

| # | Finding | Anchor | Severity | What clears it |
|---|---|---|---|---|
| H1 | ABL Electricals (MD's proprietorship) is lender (loan Rs 150 lakh taken FY26, Rs 69.64 lakh owed), supplier (Rs 64.15 lakh bought, Rs 67.59 lakh payable) and personal guarantor. The FY25 loan column fails its own arithmetic | [AR p.81-82]; AOC-2 [AR p.54]; [Pros p.177-178] (B03, B02 rank 8) | MEDIUM | H1 FY27 RPT note: ABL loan at or below Rs 69.64 lakh, terms stated |
| H2 | Antelp Corporation ("KMP relative has an interest"): sale Rs 29.44 lakh, all unpaid at 31-Mar-26 | [AR p.82]; [AR p.54] | LOW-MEDIUM | Collection shown in H1 FY27; MCA ownership check |
| H3 | Short-term loans and advances Rs 0.64 Cr to Rs 8.90 Cr. Vendor advances Rs 6.24 Cr (up Rs 5.40 Cr in Q4), supplier unnamed, no ageing. CARO iii says nil | [AR Note 17 p.90]; [AR p.72-73] (B01 LBF-2, B02 rank 2) | HIGH | Vendor advances below Rs 3 Cr at 30-Sep-26, matched by inventory inflow, supplier named |
| H4 | Stock in transit Rs 6.20 Cr in inventory but in neither the RM nor the FG note | [AR p.77 inventory 2,434.87 lakh]; Notes 21, 23 (B03 3C) | HIGH | Transit converted or cleared in the 30-Sep-26 inventory note |
| H5 | IPO objects altered: Rs 7.00 Cr (53.7% of the machinery object) moved to building. The reason contradicts the prospectus, which placed machinery in the existing unit with 1,424 sq m free against 700 sq m needed | [AR p.33, p.50-51]; [Pros p.75]; (B12b R5) | MEDIUM-HIGH | Building milestones and a machinery PO filed; no second change |
| H6 | ESOP 2026: 5,00,000 options (2.43% of shares), price "not less than face value" Rs 10. Intrinsic at CMP Rs 3.76 Cr = 84% of FY26 PAT [calc] | [AR p.35]; [Ord 20260926-3aa16089 p.2] | MEDIUM | First grant filed at or near market price |
| H7 | Inventory days: operator 179 (reproduces only on RM consumed, 180.2, B01); AR ratio 145 (turnover 2.51, [AR p.64]); cost basis 146 (B03); revenue basis 127. FY25 cost basis 83 | [AR p.64]; (B01, B03) | MEDIUM | 120 days or fewer on cost basis at 30-Sep-26 |
| H8 | Receivable days 113 on average basis (turnover 3.22) against 81 in FY25. Closing basis 78 days [calc: 1,501.48 / 7,006.92 x 365]. Over 6 months Rs 0.83 Cr, +214%, nil provision. Retention Rs 5.00 Cr unaged | [AR p.64]; [AR Note 15 p.89] (B03) | MEDIUM | Closing receivables at or below Rs 28.9 Cr and positive CFO in H1 FY27 |
| H9 | Audit trail: CARO xiv(a) says internal audit is "adequate"; the Directors' Report says it "needs to be strengthened". The internal auditor was the CFO who left on 16-Jan-26; successor NOT FOUND. KAM wording "considerably" | [AR p.74] vs [AR p.47]; [AR p.45]; [AR p.68] (B03) | MEDIUM | Named independent internal auditor; corrected statement |
| H10 | Auditor switch: Kumar Vijay Gupta & Co resigned 7-Aug-24 "due to pre-occupation"; successor P.K. Lakhani & Co shares the address and email; audit fee +209% | [Pros p.57]; [AR p.92] (B08) | MEDIUM-HIGH | ADT-3 text and ICAI firm records (PENDING LIVE VERIFICATION) |
| H11 | Promoter pledge: 0% at the prospectus date. Post-listing pledge: NOT FOUND (shareholding folder empty) | [Pros p.69, p.73]; (B00, B08) | UNKNOWN | Sep-26 shareholding pattern on BSE |
| H12 | Warranty bank guarantees Rs 5.32 Cr (118% of PAT) with no warranty provision | [AR p.83] (B03) | MEDIUM | Provision booked, or BG growth below revenue growth |
| H13 | Bill-discount interest +350%; discounted bills undisclosed. MSME payables Rs 14.95 Cr, +135%; Section 43B(h) window undisclosed | [AR p.88]; (B02 rank 10) | MEDIUM | Contingent note on bills discounted; MSME ageing |
| H14 | MD's DIN disqualification window 2016-2021 overlaps his 2019 board entry | [Pros p.33 risk factor 8, p.138] (B08) | MEDIUM | MCA DIN history (PENDING LIVE VERIFICATION) |
| H15 | Two largest order filings (Rs 39.99 Cr, 51.9% of H1 inflow) withhold the customer; the promoter-interest "No" cannot be tested | [Ord 20260629 p.2]; [Ord 20260923-d54c506f p.1] (B04, B08) | MEDIUM | Customer named in a later filing or concentration table |
| H16 | Land Rs 10.67 Cr bought 3-Jul-26, before the 26-Sep-26 approval; costs 20.6% of price; payment source NOT FOUND; the Directors' Report says no material change | [Ord 20260703 p.1]; [AR p.39] (B08) | MEDIUM | Bank trail against the IPO utilisation statement |
| H17 | Capacity claim 1,200+ MVA against certified 900.36 MVA, in the same deck | [AR p.6]; [Pros p.123]; (B04) | MEDIUM | Chartered engineer certificate above 900.36 MVA |
| H18 | CHG-1 not filed on a vehicle charge, repeated in the secretarial audit | [AR p.44, p.50-51] (B08) | LOW | Filing completed |

---

## I. PRE-BUY CHECKLIST for 7-Oct-2026

### I1. The H1 FY27 operating EBITDA margin that breaks the thesis

Derivation:
- Proof gate (a): H1 FY27 EBITDA ex other income at or above 12% (dossier B3; B05 confirm signal).
- Falsifier: below 10% with revenue up (dossier B6; B05 kill signal).
- Section D bear margin: 8.86%.
- Mechanics: at Rs 52.68 Cr and fixed cost of Rs 5.24 Cr a half, a 9.9% margin means gross margin of 19.8% [calc: (0.099 x 52.68 + 5.24) / 52.68]. That is below FY25's 20.6%. Pass-through and operating leverage would both have failed on +90% revenue.

| H1 FY27 operating EBITDA margin (ex other income) | Meaning |
|---|---|
| **Below 9.9%** | **THESIS BREAK.** No operating leverage on +90% revenue. Gross margin below about 19.8%. Exit or do not enter |
| Below 8.86% | Bear case realised. Section D bear governs |
| 9.9% to 12.0% | Unresolved. Hold at starter or zero; wait for H2 FY27 |
| 12.0% or above | Proof gate (a) met. Still needs CFO above 50% of H1 PAT and receivables at or below Rs 28.9 Cr |

Cash kill, independent of margin: H1 FY27 CFO below zero with closing receivables above Rs 28.9 Cr (dossier 4c single point of failure).

### I2. Position size under the framework

Inputs:
- A25 fast-growth: YES. H1 FY27 revenue +90.07% [H1upd p.2] is above 40%. Margin of safety is position size, not a price haircut.
- A25 starter: Small, 2% to 3%, when T1 + T2 ≥ 75% of CMP and the residual ≤ 25%. Provisional T1 + base increment = 95% (Section G4), but the C.2 probabilities are NOT FOUND.
- Dispersion cap: (bull - bear) / base at the exit = (266.8 - 50.4) / 98.7 = 219% [calc]. Above 80% caps at Small regardless of conviction.
- OR-18 evidence scale, shown for reference: mostly 🎙️ evidence, catalyst inside 12 months, so 30% to 40% MoS. On the Rs 50.5 entry that is Rs 30.3 to Rs 35.4 [calc]. It does not bind a fast-growth name.
- Gate 0 AVERAGE (deal-breaker 4, B01). Promoter CAUTION (B08). Credibility C (B05) or D (B12b). FLAG-CASH INDETERMINATE caps the run at PROCEED WITH CAVEATS.
- Capital base: NOT FOUND. Size is stated as % of portfolio.
- SME lot: trading lot 3,000 shares [Pros p.241]; BSE may modify it. At Rs 85.2 one lot is Rs 2.56 lakh [calc]. A 2% position holds one lot only if the portfolio is Rs 1.28 Cr or more [calc].

Suggestion (a flag; the decision stays with the operator):
- Framework ceiling: **2% of portfolio**, the A25 starter floor. Every modifier (CAUTION, AVERAGE, C/D, INDETERMINATE cash, dispersion above 80%) points to the floor, not the 3% top.
- At CMP Rs 85.2 the framework gives no support for a position above zero. Base return is 5.0% a year against a 25% hurdle, 4F fails, the Hurdle band is STOP, and the transition read is PRICED NARRATIVE.
- If the operator buys on 7-Oct anyway: one 3,000-share lot within the 2% ceiling, no adds until the H1 results clear I1.
- First add: only after margin ≥ 12% and positive CFO, or at prices toward Rs 41.8-50.5.

### I3. First 30 days (7-Oct to 6-Nov-2026)

| Item | What to look for | Where and when |
|---|---|---|
| H1 FY27 results date | Board-meeting intimation. Results due within 45 days of 30-Sep, by about 14-Nov-26 (reading of LODR Reg 33 for SME half-years; exact date NOT FOUND) | BSE 544710 announcements |
| Sep-26 shareholding pattern | Promoter 61.97% unchanged; pledge 0%; FII + DII level; anchor exits | BSE, due about 21-Oct-26 (reading of LODR Reg 31; verify) |
| Order filings | New Reg 30 orders; any customer names on the wind lots; any UGVCL billing or MVVNL/Torrent outcome | BSE, event-driven |
| ESOP grant | First grant price against Rs 10 floor and market | BSE SBEB disclosure, no date set |
| H1 results (if out by 6-Nov) | Operating EBITDA margin (I1); gross margin vs 24.1%; fixed cost per half ≤ Rs 5.53 Cr | Results filing |
| Receivables | Closing ≤ Rs 28.9 Cr; over-6-month bucket below Rs 0.83 Cr | Results balance sheet |
| Vendor advance and transit stock unwind | Advances below Rs 3 Cr; transit stock nil or converted | Results notes |
| CFO | Positive and above 50% of H1 PAT | H1 cash flow statement |
| IPO utilisation statement | Building spend started; unused balance; no second object change | Filed with results (LODR Reg 32 reading) |
| Cash credit | Below Rs 3 Cr while IPO money is idle (31-Mar-26: Rs 6.21 Cr) | Borrowings note (B03) |

---

## Numbers not anchored in this module (NOT FOUND, PENDING, or assumption)

- H1 FY27 EBITDA, PAT, gross margin, fixed cost, CFO, receivables, MVA made: NOT DISCLOSED (H1 results, about November 2026).
- Order book composition at 30-Sep-26 and status of the UGVCL Rs 87.50 Cr PO: NOT DISCLOSED.
- Order book at 1-Apr-25 and H1 FY26 inflow: NOT FOUND. 1-Oct-25 opening and 31-Mar-26 closing are derived, not filed.
- PV-clause share of the book: NOT DISCLOSED. Accord's metal and oil share of materials: NOT FOUND.
- CRGO Q3 2026 price, FY26 India CRGO average, India transformer-oil price series: PENDING LIVE VERIFICATION.
- Machinery lead time and PO, EHV and 5,000 MVA capex, land payment source: NOT FOUND.
- FTTCP verdicts (ROCE forward, Module B2, C.2 probabilities): NOT RUN. Pillar 1 and Pillar 3 lines are provisional.
- Numeric r adjustments for Track 1: NOT FOUND in frameworks/.
- ESOP grant price and post-listing pledge: NOT FOUND.
- Projection assumptions, named: industry growth 7.6% (B09) from FY28; fixed-cost growth 8% (AR actuarial salary escalation); Schedule II lives for the building and machinery; bull growth 30% (guidance low end, bull only); funded capacity about 704 MVA (Shilchar capex intensity, B06).
- Exact SME results and shareholding filing deadlines: readings of LODR, not verified in the corpus.

---

## RULINGS NEEDED

Verification: fresh-context Verifier A check of this file, 0 CRITICAL, 0 MAJOR, 9 MINOR (basis labels, anchors, rounding); 462 of 462 mandatory numbers in D, F, G, I checked; nothing moves the entry price, exit P/E, FY28 EPS or break margin (outputs/reports/12a-forward-module-check.md).

Each ruling answers in one line. Recommendation first.

1. Unsigned-model valuation (CLAUDE.md bars valuation before sign-off). Accept this module as a provisional sizing input only, and re-run Role 1 after signing? Recommend: YES.
2. Halt 1 decision (KILL / SHALLOW WATCH / PROCEED). Recommend: SHALLOW WATCH until the H1 FY27 results (Nov-2026). At CMP Rs 85.2 the provisional entry zone is Rs 41.8-50.5, and the base return from CMP is 5.0% a year.
3. If you buy on 7-Oct anyway: size. Recommend: one lot only (3,000 shares, about Rs 2.56 lakh), inside a 2% cap. No adds until the H1 FY27 operating EBITDA margin is 9.9% or more and H1 CFO is positive.
4. Growth after FY27: the base fades to 7.6% (A14, Emerging Moat NONE) against management's 30-50%. Recommend: keep the fade until a machinery PO for the new plant is filed. This one input moves the entry price most.
5. Pillar 2 cash multiplier: 0.70x / 0.80x / 0.90x. Recommend: 0.80x until the H1 FY27 cash flow is filed.
6. Credibility grade: C (stage 5) or D (Verifier B). Recommend: D until the H1 gross margin reconciles with the price-variation claim. That gives an exit P/E of 14.80x, not 16.80x.
7. Chunk 07 bull-margin rule gives a bull margin below the base for this name; an evidence bridge replaced it. Recommend: accept the bridge, and log the rule gap for /compost.
8. OR-1, which track sets the entry zone: Track 2 Rs 50.5 or Track 1 Rs 41.8. Recommend: show both, with Track 1 as the floor.
9. CONVERTER classification (OR-6 default, Amendment 17). Recommend: keep it until the price-variation clause text and its share of the book are seen.
10. Sector cap row: Cables / Industrial products 25x. The live peer P/E median of 33.3x is above the cap and is flagged for cap review only. Recommend: keep 25x (it does not bind here).
11. Document cap: the 18 order-win notices count as one item and the AGM filings as one bundle; peer documents sit outside the cap. Recommend: accept.
12. concalls_available set to TRUE on one transcript (the collector set it false). Recommend: accept.
13. Corpus gaps. Recommend: push the Sep-2026 shareholding pattern (pledge and the promoter's 61.97%) before any buy; accept rating rationale NOT FOUND.
14. Mental Model draft: line 2 (renewable units) claims R1 to R3, two rungs with no filed proof. Recommend: sign R1 to R2 for both lines.
15. Promoter tripwires (ADT-3 for the 2024 auditor switch, the bank trail for the Rs 10.67 Cr land payment, the first ESOP grant price). Recommend: verify all three live in claude.ai before any add. Any adverse result lifts CAUTION to CONCERN.
