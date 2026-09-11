# PROMPT 6 - VOLUMES, REALISATION, AND THE ORDER BOOK
Company: Insolation Energy Limited (INA Solar). Extraction date: 2026-09-11.
Corpus: runs/ina-2026-09-06 only. Mechanical extraction. Quote first, comment second.

Cited page numbers are the extraction marker pages ("===== PAGE N ====="), never a
transcript's printed footer.

Corpus files used:
- runs/ina-2026-09-06/work/extracted/annual-report__Annual_Report_2026.txt (FY2026 AR, YE 31-Mar-2026)
- runs/ina-2026-09-06/work/extracted/concalls__Concall_Jun_2025_Transcript.txt (call dated 09-Jun-2025, FY25 results)
- runs/ina-2026-09-06/work/extracted/concalls__Concall_Feb_2026_Transcript.txt (call dated 17-Feb-2026, Q3/9M FY26)
- runs/ina-2026-09-06/work/extracted/concalls__Concall_Jun_2026_Transcript.txt (call dated 27-May-2026, Q4/FY26 results)
- runs/ina-2026-09-06/work/extracted/presentation__Investor_Presentation_1.txt (32 pages)
- runs/ina-2026-09-06/inputs/screening/screener-Data_Sheet.csv (third party aggregator, not a filing)

---

## FLAG 0. TWO CORPUS-DESCRIPTION FACTS DO NOT MATCH THE FILE

I must report this before the tables, because it changes what "NOT IN CORPUS" means
for Q1 FY2027.

The task brief states the presentation is "dated Jul-2026 per its own slide 25" and
that there is "no Q1 FY2027 presentation" in the corpus. The file itself says otherwise.

Quote, presentation__Investor_Presentation_1.txt, PAGE 1 (the SEBI Regulation 30 cover
letter that opens the file):
> "21st August, 2026 ... Subject: Disclosure under regulation 30 ... Investor Presentation
> ... we are enclosing herewith the Investor Presenta tion on Un-Audited Financial
> Results (Standalone and Consolidated) of the Company for the quarter ended 30th June,
> 2026. ... Nitesh Sharma Company Secretary & Compliance Officer"

Quote, same file, PAGE 2:
> "INSOLATION ENERGY L TD Investor Presentation | August 2026"

Quote, same file, PAGE 12:
> "Particulars (Rs. Cr) Q1FY27 Q1FY26 YoY % FY 26
> Total Revenue 745.40 362.94 105.37% 2163.52"

Comment. This IS the Q1 FY2027 investor presentation, filed 21-Aug-2026 for the quarter
ended 30-Jun-2026. "Jul 2026" on PAGE 25 is a date label on the "RECENTLY SECURED ORDERS"
box, not the document date. I did not invent a Q1 FY2027 filing; the document is in the
corpus and I quote it. It is still true that the corpus holds no Q1 FY2027 results filing
and no Q1 FY2027 transcript. It is also still true that this presentation discloses NO
Q1 FY2027 MW volume, NO realisation per watt, NO DCR mix and NO Q1 FY2027-dated order
book. Those cells stay NOT IN CORPUS on their own merits, not by assumption.

---

## FLAG 1. WHERE THE VOLUME AND REALISATION DATA LIVES

The Annual Report 2026 contains NO megawatt sold, NO megawatt produced, NO capacity
utilisation percentage and NO realisation per watt. I searched the full 200-page
extraction for "MW", "megawatt", "GW", "gigawatt", "utilisation", "utilization",
"Installed Capacity" and "Actual Production". Every hit is nameplate capacity, an
industry statistic, or a target. There is no Schedule III installed-capacity/actual-
production table in this AR.

So: revenue by stream comes from the AR notes. Volumes, realisations, utilisation,
DCR mix and the order book come from the three concalls and the presentation only.
That is stated here once and referenced in the table below.

## FLAG 2. THE AR'S CONSOLIDATED REVENUE NOTE CARRIES THE WRONG HEADING

The consolidated revenue-from-operations note is printed as "Note No. 25:- Other Income"
(AR PAGE 130). Its content is the Ind AS 115 sale-of-products breakdown, and the next
note, "Note No. 26-: Other Income" (AR PAGE 130), is the real other-income note. The
brief expected revenue disaggregation "around Note 25 consolidated"; Note 25 is indeed
the note, but its own heading is wrong in the filed document. I quote the heading as
printed and do not correct it.

## FLAG 3. NOTE NUMBERS DIFFER FROM THE BRIEF

- Consolidated segment and customer concentration: Note No. 46 (AR PAGE 144), not 45.
- Consolidated Ind AS 115: Note No. 51 (AR PAGES 149-150). Matches the brief.
- Standalone revenue from operations: Note No. 24 (AR PAGE 172). Matches the brief.
- Standalone segment and customer concentration: Note No. 45 (AR PAGE 185).
- Standalone Ind AS 115: Note No. 49 (AR PAGES 187-188). Matches the brief.

---

# PART A. THE TABLE

## A1. BY YEAR - DISCLOSED FIGURES ONLY

All rupee figures are Rs in Lakh on a CONSOLIDATED basis, quoted from AR Note No. 25
(AR PAGE 130), unless the row says otherwise. FY2024 has no comparative in this AR: the
P&L notes carry only FY2025 and FY2026 columns.

| Row | FY2024 | FY2025 | FY2026 | Source anchor |
|---|---|---|---|---|
| MW sold (dispatched) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED as a full-year figure. Quarterly parts only, see A2 | no full-year MW in any corpus document |
| MW produced | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED as a full-year figure. Q3 FY26 only, see A2 | no full-year MW in any corpus document |
| Module capacity (nameplate, year-end) | NOT DISCLOSED | 950 MW as at 09-Jun-2025 (see quote below) | 5.5 GW as at 31-Dec-2025 and at 31-Mar-2026 | Jun-2025 call PAGE 5; Feb-2026 call PAGE 4; AR PAGE 12 |
| Capacity utilisation % | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED. See Part B5 for three conflicting rules of thumb | none |
| Average realisation per watt | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED as a company average. Product price ranges only, see Part B3 | none |
| DCR vs non-DCR split | NOT DISCLOSED | NOT DISCLOSED | "FY26 around 85% non-DCR and 15% DCR" | Jun-2026 call PAGE 18 |
| Revenue from own modules (Finished Goods) | NOT DISCLOSED | 1,00,609.12 | 1,75,721.57 | AR Note 25, PAGE 130 |
| Revenue from resale / trading (Trading Sales) | NOT DISCLOSED | 32,498.69 | 36,491.39 | AR Note 25, PAGE 130 |
| Revenue from EPC | NOT DISCLOSED as an EPC line. Nearest disclosed line is "Installation & Commissioning Services" | 5.68 | 100.06 | AR Note 25, PAGE 130 |
| Revenue from KUSUM power | NOT DISCLOSED as a KUSUM line. Nearest disclosed line is "Sale of Electricity" | - (nil) | 421.72 | AR Note 25, PAGE 130 |
| Total Sale of Products (a) | NOT DISCLOSED | 1,33,107.82 | 2,12,634.68 | AR Note 25, PAGE 130 |
| Total Other Operational Revenue (b) | NOT DISCLOSED | 269.03 | 1,967.45 | AR Note 25, PAGE 130 |
| Total revenue from operations (a+b) | NOT DISCLOSED | 1,33,376.84 | 2,14,602.13 | AR Note 25, PAGE 130 |

### The quote behind the revenue rows

annual-report__Annual_Report_2026.txt, PAGE 130, consolidated, document date FY2025-26
(year ended 31-Mar-2026):
> "Note No. 25:- Other Income (Rs in Lakh)(Rs in Lakh)
> Particulars For the Year ended 31st March 2025 For the Year ended 31st March 2026
> (a) Sale of Products
> Domestic Sales
> Sale of Products(Finished Goods)
> Sale of Products( Trading Sales)
> Sale of Electricity
> Total (a)
> (b) Other Operational Revenue
> Installation & Commissioning Services
> Job Work Income
> Freight On Sales
> Scrap Sales
> Other Income
> Discount Received
> Net Gain on Foreign Currency Transctions
> Total (b)
> Total (a+b)
> 1,00,609.12
> 32,498.69
> -
> 1,33,107.82
> 5.68
> -
> -
> -
> 244.81
> 18.54
> -
> 269.03
> 1,33,376.84
> 1,75,721.57
> 36,491.39
> 421.72
> 2,12,634.68
> 100.06
> 878.68
> 46.55
> 101.88
> 497.39
> 12.28
> 330.61
> 1,967.45
> 2,14,602.13"

Comment. The extraction prints the label column first and then the two value columns in
sequence. The first value block is FY2025 (it foots to the stated Total (a) of
1,33,107.82 and Total (a+b) of 1,33,376.84); the second is FY2026 (foots to 2,12,634.68
and 2,14,602.13). I did not reorder or recompute anything; I read the stated totals.

This is the ONLY stream split in the corpus. It has four streams: own modules, trading,
electricity, and other operational revenue. It does NOT carry an EPC line, a KUSUM line,
an IPP line or an O&M line.

### The Ind AS 115 disaggregation is by GEOGRAPHY, not by stream

annual-report__Annual_Report_2026.txt, PAGE 149, consolidated:
> "Note No. 51:- Disclosures as per Ind AS 115 'Revenue From Contracts with Customers'
> (i) Disaggregate revenue information
> The table below presents disaggregated revenues from contracts with customers for the
> year ended March 31, 2026 on the basis of countries from which entity earns its revenue.
> ... Total 1,33,107.82 2,12,634.68 ... Revenue on the basis of Geographical area
> - Domestic sales - Export sales 1,33,107.82 - 2,12,634.68 -"

Comment. The brief expected a stream split here. There is none. The Ind AS 115 note
disaggregates on one axis only: domestic versus export. Exports are nil in both years.
The stream split is in Note 25, quoted above.

annual-report__Annual_Report_2026.txt, PAGE 150, consolidated, timing of recognition:
> "(iv) Timing of revenue recognition ... Total revenue from contract with customers
> 1,34,362.34 2,16,352.38 ... Goods transferred at a point in time / Services transferred
> at a point in time (Other operating income) 1,34,356.66 5.68 / 2,15,373.64 978.74"

Comment and flag. These totals (1,34,362.34 and 2,16,352.38) equal TOTAL INCOME as stated
in the AR's own Management Discussion (AR PAGE 50), not revenue from operations
(1,33,376.84 and 2,14,602.13). The note labels them "revenue from contract with
customers". The corpus does not reconcile the two. I show both and do not reconcile.

annual-report__Annual_Report_2026.txt, PAGE 150, consolidated, contract balances:
> "(iii) Disclosure of contract balances (Rs in Lakh) Particulars As at 1st April 2024 /
> As at 31st March 2025 / As at 31st March 2026 Trade receivables / Contract Liabilities
> - Advance from customers 5,196.21 1,593.97 11,009.00 2,661.51 28,158.52 5,683.35"

Comment. This is the only place in the AR carrying an FY2024-dated figure relevant here:
trade receivables Rs 5,196.21 lakh as at 01-Apr-2024. It is not a revenue figure.

### Standalone equivalents (a different and much smaller entity)

annual-report__Annual_Report_2026.txt, PAGE 172, standalone:
> "Note No. 24:- Revenue From Operations ... (A) Sale of Products Domestic Sales
> Sale of Products(Finished Goods) Sale of Products( Trading Sales)
> Sale of Products(Manufacturing Sales) Sale of Electricity
> 9,914.28 1,298.59 - - Total (A) 11,212.87
> For the Year ended 31st March 2026 7,816.16 841.92 - 163.58 8,821.66
> (B) Other Operational Revenue Installation & Commissioning Services Job Work Income
> Freight On Sales Scrap Sales Discount Received - - - 88.51 0.98 Total (B) 89.49
> 0.16 878.68 0.13 101.88 - 980.85
> Total (A+B) 11,302.35 9,802.52"

Comment. Standalone FY2025 revenue from operations is Rs 11,302.35 lakh and standalone
FY2026 is Rs 9,802.52 lakh. Standalone revenue FELL year on year while consolidated rose
61%. Sale of Electricity appears standalone at Rs 163.58 lakh in FY2026 against Rs 421.72
lakh consolidated. The standalone entity is roughly 4.6% of consolidated revenue in
FY2026. The consolidated numbers are the operating numbers.

annual-report__Annual_Report_2026.txt, PAGES 187-188, standalone:
> "Note No. 49:- Disclosures as per Ind AS 115 'Revenue From Contracts with Customers'
> ... Revenue on the basis of Geographical area - Domestic sales - Export sales
> 11,212.87 - 8,821.66 -"
> "Total revenue from contract with customers 12,265.19 10,560.24 ... Goods transferred
> at a point in time / Services transferred at a point in time (Other operating income)
> 12,265.19 - 9,681.40 878.84"

## A2. BY QUARTER - EVERY QUARTER DISCLOSED ANYWHERE IN THE CORPUS

| Quarter | MW produced | MW sold / dispatched | Revenue (Rs cr) | Realisation, mix, order book | Source |
|---|---|---|---|---|---|
| Q1 FY2026 (Jun-25) | NOT DISCLOSED separately | NOT DISCLOSED separately. H1 aggregate only | 361.89 (screener) / 362.94 total revenue (presentation) | NOT DISCLOSED | screener-Data_Sheet.csv; presentation PAGE 12 |
| Q2 FY2026 (Sep-25) | NOT DISCLOSED separately | NOT DISCLOSED separately. H1 aggregate only | 414.86 (screener) | NOT DISCLOSED | screener-Data_Sheet.csv |
| H1 FY2026 | NOT DISCLOSED | "Nearly, H1, 360 MW" | 776.75 (screener sum, DERIVED, see A3) | NOT DISCLOSED | Feb-2026 call PAGE 6 |
| Q3 FY2026 (Dec-25) | 356 MW | 364 MW | 575 (call) / 575.34 (screener) | DCR 10-15% of dispatch (as at 17-Feb-2026) | Feb-2026 call PAGES 4, 5, 8 |
| Q4 FY2026 (Mar-26) | NOT DISCLOSED | "more than 500 megawatt in Q4" | 794 (call) / 793.93 (screener) | non-DCR Rs 13-14/W, DCR Rs 20-22/W "last quarter" | Jun-2026 call PAGES 5, 13, 15 |
| FY2026 full year | NOT DISCLOSED | NOT DISCLOSED | 2,146 revenue from ops (call) / 2,146.02 (screener) | 85% non-DCR, 15% DCR | Jun-2026 call PAGES 5, 18 |
| Q1 FY2027 (Jun-26) | NOT IN CORPUS | NOT IN CORPUS | 740.70 sales, 37.04 net profit (SCREENER ONLY) / 745.40 total revenue, 76.87 EBITDA, 38.02 PAT (presentation PAGE 12) | NOT IN CORPUS | see FLAG 0 |

Caveat on the Q1 FY2027 revenue and profit: screener-Data_Sheet.csv is a third party
aggregator, not a filing. It carries no volume, no realisation, no mix and no order book.
The presentation figures for Q1 FY2027 are from a filed Regulation 30 disclosure dated
21-Aug-2026 and are un-audited per its own cover letter. No corpus document gives Q1
FY2027 megawatts, realisation, DCR split or a Q1 FY2027-dated order book.

### The quotes behind the quarterly volume cells

concalls__Concall_Feb_2026_Transcript.txt, PAGE 4, call dated 17-Feb-2026, Vikas Jain
(Managing Director), prepared remarks:
> "Production for Q3 FY26 stood at 356 MW with a dispatch of 364 MW, supported by
> consistent execution and healthy demand from commercial and industrial segment."

concalls__Concall_Feb_2026_Transcript.txt, PAGE 5, 17-Feb-2026, Q&A:
> "Disha Bhordia: Yes. Thank you so much for this opportunity. So , just a couple of
> questions. So , for this quarter, I think our production was around 356 MW. Can you tell
> me this number for H1 FY26?
> Ravi Dusad: Yeah. It is Q3 356 MW, and dispatches are 364 MW. For Q1 or H1, we'll get
> back to you."

Comment. The CFO declined the Q1 and H1 split on the call. The Chairman then gave an
approximate H1 figure a moment later.

concalls__Concall_Feb_2026_Transcript.txt, PAGE 6, 17-Feb-2026:
> "Manish Gupta: ... So, if I discuss about the H1 of this year, FY26, we have dispatched
> around the same 350-360 MW of the solar panel because till that time, we have our only
> manufacturing facility for INA -1 and IN A-2."
> "Disha Bhordia: Okay, so just if I want this right, I think H1, the volumes were 360 MW, H1?
> Manish Gupta: Nearly, H1, 360 MW."

Comment. "Nearly" and "around the same 350-360 MW". This is an approximation given orally,
for a six-month period, and it is not split between Q1 and Q2.

concalls__Concall_Jun_2026_Transcript.txt, PAGE 15, call dated 27-May-2026, Manish Gupta
(Chairman):
> "And also dispatch-wise in the last quarter, we have already dispatch more than 500
> megawatt in Q4."

Comment. "More than 500 megawatt" is a floor, not a figure. It is the only Q4 FY2026
volume statement in the corpus.

concalls__Concall_Jun_2026_Transcript.txt, PAGE 4, 27-May-2026, Vikas Jain, prepared
remarks:
> "On the operational front, we witnessed significant growth in both production and sales
> volumes during the year, supported by robust demand across utili ty-scale, rooftop, EPC,
> government, and channel partner segments."

Comment. The FY26 results call describes volume growth in words and gives no FY26 volume
number. FY2026 full-year MW is NOT DISCLOSED.

### Nameplate capacity, dated sequence

| Date | Capacity stated | Quote anchor |
|---|---|---|
| 09-Jun-2025 | 950 MW module (Jaipur), plus a 3 GW Unit 3 under construction | Jun-2025 call PAGE 5 |
| 09-Jun-2025 | Unit 1 + Unit 2 = 950 MW Mono PERC; Unit 3 = 3,000 MW TOPCon; "the complete around 4 GW" | Jun-2025 call PAGE 14 |
| 31-Dec-2025 | 5.5 GW total installed module capacity | Feb-2026 call PAGE 4 |
| 27-May-2026 | "We currently operate 5.5 gigawatt of module manufacturing capacity" | Jun-2026 call PAGE 4 |
| 31-Mar-2026 | "No. of Manufacturing Facilities 5* Rated Capacity 5.5 GW" | AR PAGE 12 |
| 21-Aug-2026 | INA 1 200 MW, INA 2 750 MW, INA 3 4.5 GW; cell 4.5 GW and frame 18,000 MT upcoming | presentation PAGE 19 |

concalls__Concall_Jun_2025_Transcript.txt, PAGE 5, 09-Jun-2025, Manish Gupta:
> "We specialize in producing high -efficiency solar PV modules including Mono PERC and
> TOPCon N-Type technologies from our state-of-the-art facility in Rajasthan having a
> capacity of 950 megawatt. We aim to achieve greater scales; hence we are setting up a
> 3 -gigawatt solar module line in our new Unit 3 at Jaipur."

concalls__Concall_Feb_2026_Transcript.txt, PAGE 4, 17-Feb-2026, Vikas Jain:
> "With the addition of latest 1.5 GW line in December, our total installed module capacity
> stood at 5.5 GW as of 31 December, strengthening our ability to address growing market
> demand."

annual-report__Annual_Report_2026.txt, PAGE 82 and PAGE 83, plant table:
> "1 INA 1 Near Daulatpura Toll Tax, Jaipur-Delhi Bypass, Jaipur - 303805 Rajasthan
> 200 MW Module Manufacturing"
> "2 INA 2 Jatawali Industrial Area, Tehsil Chomu, Jaipur - 303806 Rajasthan 750 MW
> Module Manufacturing"
> "3 INA 3 NH-48, Sawarda, Delhi-Ajmer Expressway, Jaipur - 303348 Rajasthan 4.5 GW
> Module Manufacturing"
> "4 INA 4 & 5 Mohasa-Babai, Narmadapuram, Bhopal, Madhya Pradesh - 411661 Madhya Pradesh
> 4.5 GW Solar Cell & 18,000 MTA Aluminum frame Manufacturing (Under construction)"

Comment and flag. The AR plant table gives INA 1 as 200 MW and INA 2 as 750 MW, summing
with INA 3 to 5.45 GW, which the company calls 5.5 GW. The Jun-2025 call called INA 1 plus
INA 2 "950 megawatts", which matches 200 + 750. The Jun-2025 call called INA 3 "3,000
megawatts"; the AR and the presentation call it 4.5 GW. The corpus states both; I do not
reconcile them.

## A3. DERIVED - NOT DISCLOSED ANYWHERE, SHOWN SEPARATELY, NEVER MIXED WITH THE ABOVE

Nothing in this section is a disclosed figure. Each line names its two inputs and their
anchors. The operator may use these or discard them; a downstream stage must not cite
them as company disclosure.

| DERIVED line | Value | Input 1 (anchor) | Input 2 (anchor) |
|---|---|---|---|
| H1 FY2026 revenue | Rs 776.75 cr | Q1 FY26 sales 361.89 (screener-Data_Sheet.csv, quarter ended 2025-06-30) | Q2 FY26 sales 414.86 (screener-Data_Sheet.csv, quarter ended 2025-09-30) |
| FY2026 own-module share of revenue from operations | 81.88% | Finished Goods 1,75,721.57 (AR Note 25, PAGE 130) | Total revenue from operations 2,14,602.13 (AR Note 25, PAGE 130) |
| FY2025 own-module share of revenue from operations | 75.43% | Finished Goods 1,00,609.12 (AR Note 25, PAGE 130) | Total revenue from operations 1,33,376.84 (AR Note 25, PAGE 130) |
| FY2026 trading share of revenue from operations | 17.00% | Trading Sales 36,491.39 (AR Note 25, PAGE 130) | Total 2,14,602.13 (AR Note 25, PAGE 130) |
| FY2025 trading share of revenue from operations | 24.37% | Trading Sales 32,498.69 (AR Note 25, PAGE 130) | Total 1,33,376.84 (AR Note 25, PAGE 130) |
| Cell plant usable share of nameplate, Feb-2026 basis | 84.4% to 88.9% | 3.8 to 4 GW achievable (Feb-2026 call PAGE 9) | 4.5 GW nameplate (Feb-2026 call PAGE 9) |
| Q1 FY2027 other income | Rs 4.71 cr | Total revenue 745.40 (presentation PAGE 12) | Sales 740.70 (screener-Data_Sheet.csv, quarter ended 2026-06-30) |

I did NOT derive average realisation per watt for any period. Doing so would require a
disclosed MW figure and a disclosed matching revenue figure on the same basis, for the
same scope. The corpus never gives both for the same period on the same scope:
Q3 FY2026 has a dispatch MW and a total revenue, but the revenue includes trading sales,
electricity and other operational revenue, so a quotient would not be a module
realisation. I leave it NOT DISCLOSED.

I did NOT derive capacity utilisation. The MW figures are dispatch figures for a quarter
and the capacity figures are year-end nameplate; the bases do not match.

---

# PART B

## B1. ORDER BOOK - DATED SEQUENCE, THREE BASES, NOT RECONCILED

The corpus states the order book on three different bases across the three calls, plus the
presentation. I present them in date order and name the unit and basis of each. I do not
reconcile them.

| # | Date | Stated figure | UNIT | BASIS as stated | Anchor |
|---|---|---|---|---|---|
| 1 | 09-Jun-2025 | INR 2,500 crores plus | RUPEES | "on consolidated basis across all verticals" | Jun-2025 call PAGE 8 |
| 2 | 17-Feb-2026 | approximately 2.1 GW | GIGAWATTS | prepared remarks, "healthy order book of approximately 2.1 GW" | Feb-2026 call PAGE 5 |
| 3 | 17-Feb-2026 | 2.2 GW | GIGAWATTS | stated by the ANALYST in his own question, same call | Feb-2026 call PAGE 9 |
| 4 | 17-Feb-2026 | 2.1 GW | GIGAWATTS | CFO reply, "gives us a visibility of six to nine months" | Feb-2026 call PAGE 10 |
| 5 | 27-May-2026 | 1.6 GW to 1.8 GW | GIGAWATTS | "this year order book size", i.e. FY27 scope, not a point-in-time stock | Jun-2026 call PAGE 6 |
| 6 | 27-May-2026 | almost 50% | PERCENT OF CAPACITY | "almost 50% of the order book is with booked, capacity is booked" for FY2027 | Jun-2026 call PAGE 13 |
| 7 | 21-Aug-2026 | 2.1 GW+ | GIGAWATTS | presentation headline, no as-at date given | presentation PAGES 10 and 25 |
| 8 | Jul 2026 label | INR 558 cr + INR 362 cr + INR 340 cr + INR 516 cr | RUPEES | four named recently secured orders, not a total order book | presentation PAGE 25 |
| 9 | FY2026 AR | 2.1 GW+ | GIGAWATTS | AR operational momentum page, no as-at date given | AR PAGE 13 |

### The quotes

(1) concalls__Concall_Jun_2025_Transcript.txt, PAGE 8, 09-Jun-2025, prepared remarks:
> "Our company is having a strong order book of INR2,500 crores plus on consolidated basis
> across all verticals including channel partners, government scheme, rooftop solar, EPC
> and developers contracts."

Comment. Rupee basis. No gigawatt equivalent given. Verticals named but not split.

(2) concalls__Concall_Feb_2026_Transcript.txt, PAGE 5, 17-Feb-2026, Vikas Jain:
> "We also continue to maintain strong demand visibility supported by a healthy order book
> of approximately 2.1 GW, providing confidence in sustained capacity utilization and
> growth."

(3) concalls__Concall_Feb_2026_Transcript.txt, PAGE 9, 17-Feb-2026, analyst Tarun Agarwal
(Tata Investment Corporation), in his question:
> "Tarun Agarwal: Yes. Hi, hello. So, my question is pertaining to the order book.
> Currently, as we speak about, we have an order book of 2.2 GW. And the next quarter, we
> will be doing close to 450 to 500 MW of orders will be executed."

Comment. 2.2 GW is the ANALYST's number, not management's. Management corrected it to
2.1 GW in the reply below. I list it because the operator asked for every stated figure.

(4) concalls__Concall_Feb_2026_Transcript.txt, PAGE 10, 17-Feb-2026, Ravi Dusad (CFO):
> "Yeah. So, presently, our order book stands at 2.1 GW , right? So, which will give us a
> clear visibility of next six to nine months. And order book refill is a continuous process
> because we op erate in many market segments. We operate in dealer distribution network.
> We operate in small EPCs. We operate in large EPC s. So, as a function, we cannot create
> large order book on the same time because every customer wants immediate dispatch. So, it
> is a process into the function. The present order book gives us a visibility of six to
> nine months."

(5) concalls__Concall_Jun_2026_Transcript.txt, PAGE 6, 27-May-2026:
> "Vishvender Singh: Sir, I wanted to ask on the current order book size and the execution
> timeline of it for this year and next year?
> Manish Gupta: Sir, this year order book size is nearly 1.6 gigawatt to 1.8 gigawatt, and
> next year with AL CM already we have done M oU with some companies and also M oUs with
> some companies are in pipeline, which may be done within next one or two months with the
> ALMM Part 2, cells for module sales and some companies for the DCR cell sales also."

Comment and flag. Read literally, the order book falls from 2.1 GW on 17-Feb-2026 to
1.6-1.8 GW on 27-May-2026, while the presentation filed 21-Aug-2026 still says "2.1 GW+".
The question asked for "current order book size ... for this year and next year", and the
Chairman answered "this year order book size", so the basis may be a full-year execution
plan rather than a point-in-time backlog. The corpus does not say which. Shown, not
reconciled.

(6) concalls__Concall_Jun_2026_Transcript.txt, PAGE 13, 27-May-2026:
> "Sachin Rajurkar: Yes, hi. Good afternoon all. Out of the total installed capacity that
> we projected in this year, that is financial year '27, how much of that would be a kind of
> a booked with respect to the current order book or the expected order book?
> Ravi Dusad: Sir, since we operate in different segments, so our order books got refilled.
> And regarding long-term orders, our Chairman sir has already told about the long-term
> orders, and remaining orders are on a refilling mode. Since we operates in different
> segment, dealer distribution network is there, small EPC network is there, large EPC is
> there. And almost 50% of the order book is with booked, capacity is booked.
> Sachin Rajurkar: My question is that for a financial year 2027 the total capacity will be
> around 50% book, is that statement correct?
> Manish Gupta: Yes, yes. 50% is book and the balance is the on monthly basis."

Comment. A third basis: percent of FY2027 capacity booked, not gigawatts and not rupees.

(7) presentation__Investor_Presentation_1.txt, PAGE 10 (filed 21-Aug-2026):
> "Robust Order book
> Order book of 2.1 GW+ provides strong revenue visibility and supports sustained execution
> momentum."

presentation__Investor_Presentation_1.txt, PAGE 25:
> "2.1 GW+ order book and orders secured NTPC, L&T, MEIL and REC contracts provide strong
> execution visibility."

(8) presentation__Investor_Presentation_1.txt, PAGE 25:
> "Recently secured large-scale orders already provide clear execution visibility for the
> coming two quarters. GROWTH & EXECUTION CATALYSTS RECENTLY SECURED ORDERS Jul 2026
> 01 NTPC Renewable Energy INR 558 Cr Solar PV module supply - execution through FY27
> 02 New Orders Awarded INR 362 Cr Solar PV Module Supply including MEIL, L & T- Execution
> Through FY27
> 03 Rajasthan RREC Awarded INR 340 Cr Rooftop solar, 3 districts + 25-yr O&M
> 04 IPP + PM-KUSUM (AP) Awarded INR 516 Cr IPP contract + KUSUM Andhra Pradesh order"

Comment. Four named rupee orders totalling Rs 1,776 cr by the document's own arithmetic.
The document does NOT state that total and does not say these sit inside or outside the
2.1 GW+. I do not add them into any disclosed column.

(9) annual-report__Annual_Report_2026.txt, PAGE 13:
> "Robust Order book
> Order book of 2.1 GW+ provides strong revenue visibility and supports sustained execution
> momentum."

### Order book split by customer type or DCR status

There is NO split of the order book by DCR status anywhere in the corpus. NOT DISCLOSED.

The nearest thing to a customer-type split is a SALES mix, not an order book split, and the
Chairman gave it twice in the same call:

concalls__Concall_Jun_2026_Transcript.txt, PAGE 14, 27-May-2026:
> "Sachin Rajurkar: Okay, so one small follow-up questions I asked last time also that what
> is the percentage of the total order book with respect to the B2B and B2C, let's say retail
> and the industrial or EPC?
> Manish Gupta: Sir, I guess around total capacity we have in utility sector it is around
> 65%. For KUSUM project it is around 15%. For PM Surya Ghar around 5%. For OEM is around
> 5%, and the balance the miscellaneous is around 10%.
> Sachin Rajurkar: Okay, so retail is constituting around 10%-15% not more than that. Is that
> correct understanding?
> Manish Gupta: Yes sir, 10% to 15%."

concalls__Concall_Jun_2026_Transcript.txt, PAGE 19, 27-May-2026:
> "Pavan Kumar: Okay. And for the second, I want to know what about the EPC or can you give
> me the bifurcation for FY26 in terms of module sold and EPC projects done for the revenue?
> Manish Gupta: Sir, I told you sir, Yes, FY26, I earlier said I will again tell you sir, in
> Utility sector is around 65%, KUSUM is around 15%, PM Surya Ghar is around 5%, OEM is
> around 5% and the miscellaneous is other balance 10%."

Comment. The analyst asked for a revenue bifurcation between modules sold and EPC. The
answer given is a channel mix. Note the first version says "total capacity" and the second
says "FY26"; the basis (capacity, order book, or revenue) is stated differently in the two
answers, in the same call. A module-versus-EPC revenue bifurcation is NOT DISCLOSED.

## B2. CUSTOMER CONCENTRATION

annual-report__Annual_Report_2026.txt, PAGE 144, CONSOLIDATED, Note No. 46, quoted exactly:
> "Note No. 46:- Disclosure as per Ind AS 108 ' Operating segment
> i. Operating segments are reported in a manner consistent with the internal reporting
> provided to the Chief Operating Decision Maker ("CODM") of the Company. The CODM, who is
> responsible for allocating resources and assessing performance of the operating segments,
> has been identified as the Chief Finance Officer of the Company. The Group operates only
> in one Business Segment i.e. "Manufacturing & Trading of Solar Photovoltaic Modules",
> hence does not have any reportable Segments as per Ind AS 108 "Operating Segments".
> ii. Further, from one customer the Group (Solarworld Energy Solutions Ltd) has revenue of
> Rs 26,518.78 Lakh (March 31, 2025: Nil) which is more than 10% of the total revenue from
> operations.
> iii. Information about Geographical revenue and non-current asset."

The three items the operator asked for:
- Top customer AMOUNT: Rs 26,518.78 Lakh, FY2026. Named: Solarworld Energy Solutions Ltd.
- Top customer PERCENTAGE: NOT DISCLOSED as a number. The note says only "more than 10% of
  the total revenue from operations". The AR states no percentage for this customer.
- PRIOR YEAR COMPARATIVE: "(March 31, 2025: Nil)". Stated as Nil.

Comment. Solarworld Energy Solutions Ltd went from nil to the group's only above-10%
customer in one year. Against the disclosed consolidated revenue from operations of
Rs 2,14,602.13 lakh the amount is 12.36 percent, but that quotient is DERIVED and is
recorded in section A3 logic, not here; the AR does not state it.

TOP FIVE CUSTOMERS as a share of revenue: NOT DISCLOSED. Ind AS 108 requires only the
above-10% customers, and the AR gives one. A top-five concentration table would normally
sit in the same Note 46 (consolidated) / Note 45 (standalone), or in the Management
Discussion and Analysis risk section. It is in neither.

The AR does assert low concentration in prose, without numbers.
annual-report__Annual_Report_2026.txt, PAGE 143, consolidated financial risk note:
> "monitored. The Group has no concentration of credit risk as the customer base is widely
> distributed"

Comment and flag. The credit-risk note says the Group "has no concentration of credit
risk" while Note 46 discloses a single customer above 10 percent of revenue from nil a
year earlier. Both statements are in the same financial statements. Shown, not reconciled.

annual-report__Annual_Report_2026.txt, PAGE 185, STANDALONE, Note No. 45, quoted exactly:
> "ii. Further, from one customer (Insolation Green Energy Limited) the Company has revenue
> of Rs 7816.16 Lakhs (March 31, 2025: 37.16 Crore) which is 79.74% of the total revenue
> from operations."

Comment. The standalone above-10% customer is the company's own wholly owned subsidiary,
Insolation Green Energy Limited, at 79.74% of standalone revenue from operations. This is
an intra-group figure and it eliminates on consolidation. The prior year comparative is
given in a different unit (Rs 37.16 Crore against Rs 7816.16 Lakhs) inside the same
sentence. Quoted as printed.

## B3. MODULE ASP AND PRICE COMMENTARY - EVERY STATEMENT, DATED

### 09-Jun-2025, Jun-2025 call, PAGE 9, Manish Gupta (Chairman)
> "For DCR market, that market should remain not be effective up to next year because the
> cell manufacturing capacity will not add this year so much. Next year, the addition of the
> cells will be in our country up to 50-gigawatts. So, margins as far as for DCR and non -DCR
> will be near about the same because we work on the delta of our manufacturing. Whatever the
> cell price of the DCR and other raw material, our delta and our margin is fixed and that
> conclusion the price of the market, the selling price of the module market.
> The same non -DCR price, cell price plus other raw material and our manufacturing, the
> final cost of the non -DCR panel in the market. But no doubt, the availability of the DCR
> cell right now is challenging in our country."

Comment. Delta pricing claimed: the company says it earns a fixed spread over cell cost, so
the DCR and non-DCR module prices differ only by the cell price. No rupee per watt given.

### 17-Feb-2026, Feb-2026 call, PAGE 8, Manish Gupta, on DCR share and on realisation
> "Manish Gupta: Sir, right now, in the DCR, we have around 10-15% of our dispatch for DCR.
> And the balance is for, you can say, C&I, IPP , EPC, and our dealer distributor network.
> And some we are doing OEM for our old customer for -- in that, we are making solar panel
> in their plant. We are doing white labeling, but that is very less now."

> "Sabri Hazarika: And, it's a follow-up to this question. How is the realizations like in
> these segments? Any ballpark rate? I don't want the exact number.
> Manish Gupta: Sir, DCR and non DCR price, no doubt there is a price difference there.
> Whatever the difference is, all due to the DCR cell price available in the Indian market
> right now. So, realization, if we can say both, solar panel, either DCR or non DCR , we are
> working on our, you can say, the differentiation, or you can say our margins, whatever the
> manufacturing cost we are having for -- either for DCR or non DCR, is same. The difference
> is only for the price of the solar cell what we get from the Indian solar cell
> manufacturer. Otherwise, realization is nearly the same for both."

### 17-Feb-2026, Feb-2026 call, PAGES 8-9, Ravi Dusad (CFO), declining to give an ASP
> "Ravi Dusad: The average realization depends upon one more thing, what kind of blending we
> are doing. For example, if we are doing 10% blending, the average realization will be
> somewhat different. And if we hire the blending, the realization will be different. So, it
> is really difficult to say what is the -- going forward, what is the average realization.
> It all depends upon what is the blending of DCR and non DCR."

Comment. The CFO was asked for a ballpark realisation and declined. No Feb-2026 rupee per
watt exists in the corpus.

### 17-Feb-2026, Feb-2026 call, PAGE 10, Manish Gupta, on raw-material price volatility
> "And also, one more thing, what happened in last quarter or last to last quarter, it's a
> huge rapidly changes in the polysilicon complete prices from polysilicon to solar cell and
> all supply chain. The prices have changed so much in last few months, so you cannot
> possible to maintain so long of a period of the order. So, it's a huge problem in this
> sector right now."
> "So right now, it's very difficult, anyone, to maintain one year or two yearlong order
> books with the fixed price. So, we are trying that order book should be fixed price,
> whatever raw material we are in our control. So, up to that extent of the time, we are
> trying to book fixed price order. Otherwise, on future order with the adjustable price as
> per the raw material availability in the China and in India."

### 27-May-2026, Jun-2026 call, PAGE 13, Manish Gupta - THE ONLY RUPEE PER WATT IN THE CORPUS
> "Kapil Adwani: ... The first one is on the realization per watt. So how has been the
> realization so far in the last quarter and how do you see the realization moving forward
> in FY27?
> Ravi Dusad: Sir, the realization is basically depends upon what kind of blending we are
> doing in DCR and non-DCR.
> Manish Gupta: You just want to price?
> Kapil Adwani: The average realization, Yes.
> Manish Gupta: Price is you can say the last quarter the price non-DCR is around INR13 to
> INR14 per watt and DCR is from INR20 to INR22 per watt. That is Mono PERC and TOPCon."

Comment. Critical distinction. The analyst asked for average REALISATION. The Chairman
answered with PRICE ranges by product ("You just want to price?"). These are market price
ranges for the quarter ended 31-Mar-2026, not the company's achieved blended realisation.
The company's average realisation per watt remains NOT DISCLOSED.

### 27-May-2026, Jun-2026 call, PAGES 16-17, Manish Gupta, the fuller price breakdown
> "Mitesh Mehta: Thank you again for taking my question. I just want I am looking for
> break-up of realization per watt in all the segments like DCR, non-DCR and IPP, all the
> segment realization per watt?
> Manish Gupta: Sir, as I earlier said that price of non -DCR is right now is from INR13 to
> INR 14 per watt TOPCon."
> "Manish Gupta: And DCR is from INR20 to INR22. The Mono PERC is price INR20 to INR21 and
> TOPCon price is somewhere INR21 to INR22 in some locations it's INR22.5 also."
> "Manish Gupta: This is the DCR panel price."

Price table as stated on 27-May-2026 (prices, NOT achieved realisations):

| Product | Price per watt as stated | Anchor |
|---|---|---|
| Non-DCR TOPCon | INR 13 to INR 14 | Jun-2026 call PAGES 13 and 16 |
| DCR (both types, headline) | INR 20 to INR 22 | Jun-2026 call PAGES 13 and 16 |
| DCR Mono PERC | INR 20 to INR 21 | Jun-2026 call PAGE 16 |
| DCR TOPCon | INR 21 to INR 22, "in some locations it's INR22.5 also" | Jun-2026 call PAGE 16 |
| IPP segment realisation per watt | NOT DISCLOSED. Asked for, not answered | Jun-2026 call PAGE 16 |

### 27-May-2026, Jun-2026 call, PAGE 6, Manish Gupta, on margin pressure from input prices
> "Definitely. Maybe some margin should be on pressure sid e, but we believe that on delta
> basis , some margin, we will absorb and some margin, we will pass on through our customers
> also. So, that depend on the market call . And till now we are supplying the material as
> per our previous order book and our future order book, maybe for some orders, we adjust
> prices with our customer and some price, maybe we will absorb."

### 27-May-2026, Jun-2026 call, PAGE 6, Manish Gupta, on the price escalation clause
> "Generally, price escalation clause is maximum is based on the dollar price basis, so we
> are trying to escalate price with our customers. But whatever the price we have finalized
> from our customer, in the backup of that we have already tried to arrange the all raw
> material for that purchase order. At least two to three months' raw material , will be
> kept in our factory , so that whatever the current order we are taken or we are supplying
> to our customer, that is backup with the raw material price also."

Comment. The analyst asked what share of the order book carries a price escalation clause.
The answer names the mechanism and the two-to-three month raw material cover. The SHARE is
NOT DISCLOSED.

### 27-May-2026, Jun-2026 call, PAGE 14, Vikas Jain, on non-ALMM price pressure
> "Sir, in the market there are non-ALMM compliant modules, orders are already available to
> the tune of maybe 30 -gigawatt or so. And in the next six months , we would be starting our
> cell factory then this pressure won't be applicable on us. And we have already secured
> mostly we have already secured the orders for the next six months during till our cell
> capacity is on."

### 27-May-2026, Jun-2026 call, PAGE 18, Manish Gupta, FY2026 DCR mix
> "Kapil Adwani: Okay. So majorly it will be done from the internal accruals only. ... And
> sir, can you please bifurcate , the non-DCR and DCR bi furcation for the sales in FY26?
> Manish Gupta: FY26 around 85% non-DCR and 15% DCR. Hello?"

Comment. "Around". The basis (megawatts or rupees) is not stated. This is the only
full-year DCR split in the corpus and it is consistent with the Feb-2026 point-in-time
statement of 10-15% of dispatch.

## B4. SEGMENT - IND AS 108

CONFIRMED: a single reportable segment. The consolidated note is Note No. 46 (AR PAGE 144),
not Note 45 as the brief expected; Note 45 is the standalone equivalent (AR PAGE 185).

Exact quote, consolidated, annual-report__Annual_Report_2026.txt, PAGE 144:
> "Note No. 46:- Disclosure as per Ind AS 108 ' Operating segment
> i. Operating segments are reported in a manner consistent with the internal reporting
> provided to the Chief Operating Decision Maker ("CODM") of the Company. The CODM, who is
> responsible for allocating resources and assessing performance of the operating segments,
> has been identified as the Chief Finance Officer of the Company. The Group operates only
> in one Business Segment i.e. "Manufacturing & Trading of Solar Photovoltaic Modules",
> hence does not have any reportable Segments as per Ind AS 108 "Operating Segments"."

Exact quote, standalone, annual-report__Annual_Report_2026.txt, PAGE 185:
> "Note No. 45:- Disclosure as per Ind AS 108 ' Operating segment
> i. Operating segments are reported in a manner consistent with the internal reporting
> provided to the Chief Operating Decision Maker ("CODM") of the Company. The CODM, who is
> responsible for allocating resources and assessing performance of the operating segments,
> has been identified as the Chief Finance Officer of the Company. The Company operates only
> in one Business Segment i.e. "Manufacturing & Trading of Solar Photovoltaic Modules",
> hence does not have any reportable Segments as per Ind AS 108 "Operating Segments"."

### The stated reason, and what is missing

The note gives ONE reason, and only in the form of a conclusion: the Group "operates only
in one Business Segment i.e. 'Manufacturing & Trading of Solar Photovoltaic Modules'".
It identifies the CODM as the Chief Financial Officer.

The specific reason the operator asked for - why EPC, IPP and O&M are NOT reported
separately - is NOT DISCLOSED. The note never names EPC, IPP or O&M. It does not say
whether those activities were assessed as operating segments and failed the aggregation or
quantitative thresholds of Ind AS 108, or whether the CODM simply does not receive
discrete financial information for them. That reasoning would normally sit inside Note
No. 46 (consolidated) / Note No. 45 (standalone) itself, in the same paragraph i.

The AUDITOR states nothing on segments. I searched the whole AR extraction for "segment"
in any auditor context: the word appears in the two notes above and nowhere in the
Independent Auditor's Report or in any Key Audit Matter. There is no auditor comment,
qualification or emphasis on the single-segment conclusion. NOT DISCLOSED.

The BOARD states nothing on segments either. The Directors' Report carries no segment
paragraph. NOT DISCLOSED.

### One further gap inside the segment note

Both segment notes end with:
> "iii. Information about Geographical revenue and non-current asset."

and then move straight to the next note (Note No. 47 consolidated, AR PAGE 144; Note No. 46
standalone, AR PAGE 185). The heading is printed with NO table under it in the extracted
text. The geographical breakdown promised by item iii is not present at that anchor. The
geography split does appear elsewhere, in the Ind AS 115 notes (consolidated Note 51,
AR PAGE 149; standalone Note 49, AR PAGE 187), both showing domestic sales equal to total
and export sales nil.

Comment on why this matters for Part A. Because there is one reportable segment, the AR
gives NO EPC revenue line, NO IPP revenue line, NO O&M revenue line, NO profitability by
stream and NO capital employed by stream. The Note 25 sale-of-products split is the only
stream-level revenue disclosure that exists, and it is a product-type split (finished
goods, trading, electricity), not a business-line split.

## B5. CAPACITY UTILISATION AND USABLE SHARE OF NAMEPLATE

The operator asked for the Feb-2026 statement on usable capacity as a share of nameplate,
plus every other corpus figure that speaks to the same question, so that agreement or
disagreement is visible. There are FIVE such figures. THREE are in the Feb-2026 call
alone. They do not agree. I show all five in date order and do not reconcile them.

| # | Date | Figure | Scope as stated | Speaker | Anchor |
|---|---|---|---|---|---|
| 1 | 17-Feb-2026 | "nearly 70%. Not more than 70%" | INDUSTRY-WIDE, any module maker | Manish Gupta | Feb-2026 call PAGE 12 |
| 2 | 17-Feb-2026 | 3.8 to 4 GW out of 4.5 GW nameplate | THE 4.5 GW CELL PLANT, at full ramp | Vikas Jain | Feb-2026 call PAGE 9 |
| 3 | 17-Feb-2026 | "50% to 55% can be utilized capacity" | INA's OWN module units, "as per normal standards" | Ravi Dusad | Feb-2026 call PAGE 18 |
| 4 | 27-May-2026 | "around 60% to 65%" | MODULE manufacturing efficiency - stated by the ANALYST, not management | Nirav Khandhar | Jun-2026 call PAGE 20 |
| 5 | 27-May-2026 | "more than 80%", i.e. 3.6 GW of 4.5 GW | THE CELL PLANT, "plant efficiency" | Vikas Jain | Jun-2026 call PAGE 20 |

### (1) The industry-wide 70%, Feb-2026 call, PAGE 12, Manish Gupta
> "And if we say that our -- any one company, any company who is showing their manufacturing
> capacity, all companies are working annual maximum, the efficiency of the machines is
> nearly 70%. No t more than 70% machines are performing at their maximum manufacturing
> capacity.
> So effectively, 70 to 75 GW of the manufacturing capacity right now we have actually in our
> country for TOPCon, M10R, or G12R, manufacturing capacity."

Comment. This is the Chairman's stated general rule for the industry, used to argue there
is no Indian overcapacity. He applies it to "any one company, any company", which includes
INA. It is not presented as an INA-specific number.

### (2) The cell plant 3.8 to 4 GW of 4.5 GW, Feb-2026 call, PAGE 9, Vikas Jain
> "Sabri Hazarika: ... And based on this capacity, 4.5 GW, which is the nameplate capacity,
> I guess, how long will you take to achieve optimum utilization? And what would be the peak
> utilization level for this cell plant?
> Vikas Jain: After commissioning, it will take almost three months to get the plant to ramp
> up to its full capacity, and we hope to produce almost 3.8 to 4 GW of cells from this plant
> if capacity utilized on full scale."

Comment. The question uses the words "nameplate capacity" and asks for the PEAK utilisation
level. The answer gives 3.8 to 4 GW against a stated 4.5 GW nameplate. This is the Feb-2026
statement on usable capacity as a share of nameplate. The percentage is not stated; the
quotient is DERIVED and recorded in section A3 as 84.4% to 88.9%.

### (3) INA's own 50% to 55%, Feb-2026 call, PAGE 18, Ravi Dusad
> "Priyanshu Maheshwari : Sure, thank you. Further can you please shed some light over the
> capacity utilization of all the three units separately? Because since you already mentioned
> the unit, the third unit came in commencement in September or in October. So, if you can
> just shed some light over the all the three capacity, total capacity and its utilization.
> Ravi Dusad: The capacity utilization, as per normal standards, capacity -- out of total
> installed capacity, 50% to 55% can be utilized capacity, right. So, from Unit 1, we have
> less utilization. Unit 2 we have fully -- Unit 2 is fully utilized for first six months and
> moderately utilized in Q2. And Unit 3 is now more utilized because of the TOPCon facility we
> have, which has better yield, and better demand side. So, Unit 3 is more utilized as
> compared to Unit 1 and 2. And going forward, this will be the trend."

Comment and flag. THIS IS THE MATERIAL DISAGREEMENT. On the same call, at the same date,
the Chairman says the industry rule is "nearly 70%" and "not more than 70%", while the CFO
says the norm for INA's own installed module capacity is "50% to 55% can be utilized
capacity". The gap is 15 to 20 percentage points on the same question about the same
company's module plants. The CFO also gives no unit-level percentage despite being asked
for one three times in the question: Unit 1 "less", Unit 2 "fully ... for first six months",
Unit 3 "more". No numbers. Unit-level utilisation is NOT DISCLOSED.

### (4) The analyst's 60% to 65%, Jun-2026 call, PAGE 20, Nirav Khandhar
> "Nirav Khandhar: Yes. Hi. So the question is , in module manufacturing the efficiency is
> around 60 % to 65% is what I have understood. So what is the efficiency we are looking in
> solar cell when the line gets operationalized?"

Comment. The analyst's own premise, prefaced "is what I have understood". Management did
not confirm or correct the 60-65% module figure; they answered only about the cell plant.
Listed because it is a stated figure on the same question, but it is NOT management's.

### (5) The cell plant 80% / 3.6 GW, Jun-2026 call, PAGE 20, Vikas Jain
> "Vikas Jain: Usually the solar cell efficiencies are much higher than the modules. We are
> targeting for more than 80% of the plant efficiency.
> Nirav Khandhar: Okay. So the balance would be available for the like, the other players we
> can sell the solar cell apart from using the captive, right?
> Vikas Jain: No, no. I am talking about the plant efficiency.
> Manish Gupta: The manufacturing efficiency.
> Vikas Jain: Manufacturing efficiency. Suppose if the plant capacity is 4.5 gigawatt, out of
> that 80% would be the practically the actual production output, 3.6 gigawatt."

Comment and flag. The same executive on the same asset moved from "3.8 to 4 GW" of 4.5 GW
on 17-Feb-2026 to "80% ... 3.6 gigawatt" of 4.5 GW on 27-May-2026. Both are stated as the
practical output of the 4.5 GW cell plant at full scale. Shown, not reconciled. Note also
that this exchange establishes that management treats module plant efficiency and cell plant
efficiency as different numbers, with modules the lower of the two.

### Forward utilisation guidance, for completeness

concalls__Concall_Jun_2026_Transcript.txt, PAGE 9, 27-May-2026, Ravi Dusad, on the cell
plant after Q4 FY2027 commissioning:
> "Hemanshu Srivastava: Okay, so after Q4 the capacity utilization will be like within next
> two quarters will be close to like 70% to 80% or it will be like 50%-60%?
> Ravi Dusad: No, no, in next two quarters the capacity will be maximum 60% to 70%."

concalls__Concall_Feb_2026_Transcript.txt, PAGE 13, 17-Feb-2026, Ravi Dusad, on why FY2026
revenue guidance was missed:
> "We had already communicated in October and November to our investors that there is a delay
> due to delay in production capacity, ramping up of production capacity due to monsoon and
> other factors which are beyond our co ntrol. So, before September, we have only 1 GW of
> production capacity. The new capacity addition will come in after September only. So, until
> and unless we do not have capacity addition, we cannot achieve the revenue guidance."

Comment. Useful for reading H1 FY2026 dispatch of about 360 MW: the CFO states the company
held only 1 GW of production capacity before September 2025.

annual-report__Annual_Report_2026.txt, PAGE 50, Management Discussion, the only AR sentence
touching utilisation:
> "EBITDA increased by 76.50% primarily due to improved product mix, higher operating
> efficiencies, disciplined cost management, and better capacity utilisation, resulting in
> expansion of EBITDA margins 124 bps on YOY basis."

Comment. "Better capacity utilisation" in prose. No percentage. The AR gives no utilisation
number anywhere.

---

# NOT DISCLOSED REGISTER

Every item the operator asked for that the corpus does not contain, with the document and
section where it would normally sit if it existed.

| Missing item | Where it would normally sit |
|---|---|
| MW sold, FY2024 / FY2025 / FY2026 full year | Concall prepared remarks (operational highlights), or an investor presentation operational slide. Not in the AR: this AR has no Schedule III installed-capacity and actual-production table |
| MW produced, FY2024 / FY2025 / FY2026 full year | Same as above |
| MW sold or produced, Q1 FY2026 and Q2 FY2026 separately | Feb-2026 call. The CFO was asked directly and said "For Q1 or H1, we'll get back to you" (PAGE 5). Only an H1 approximation was given |
| MW sold or produced, Q4 FY2026 exact | Jun-2026 call prepared remarks. Only "more than 500 megawatt" given (PAGE 15) |
| Any MW figure for Q1 FY2027 | Q1 FY2027 results filing and transcript, neither of which is in the corpus. The Q1 FY2027 presentation that IS in the corpus (21-Aug-2026) carries no MW |
| Capacity utilisation percentage, actual, any period | AR Management Discussion, or concall. Five rules of thumb exist (Part B5); no actual achieved figure |
| Utilisation by unit (INA 1, INA 2, INA 3) | Feb-2026 call PAGE 18, where it was asked and answered only in words: "less", "fully", "more" |
| Average realisation per watt, achieved, any period | Concall. Asked twice (Feb-2026 PAGE 8, Jun-2026 PAGE 13). The CFO called it "really difficult to say"; the Chairman answered with product price ranges instead |
| IPP segment realisation per watt | Jun-2026 call PAGE 16. Asked as part of "all the segment realization per watt"; not answered |
| DCR vs non-DCR split, FY2024 and FY2025 | Concall or presentation. Only FY2026 (85/15) and a Feb-2026 point-in-time (10-15% of dispatch) exist |
| DCR vs non-DCR split of the ORDER BOOK, any date | Concall or presentation. Never given on any basis |
| Share of order book carrying a price escalation clause | Jun-2026 call PAGE 6. Asked directly; the mechanism was described, the share was not |
| Revenue from EPC, as an EPC line, any year | AR Note 25 consolidated (PAGE 130) or Note 24 standalone (PAGE 172). The only adjacent line is "Installation & Commissioning Services" (Rs 5.68 lakh FY25, Rs 100.06 lakh FY26). Asked on the Jun-2026 call (PAGE 19) and answered with a channel mix instead |
| Revenue from KUSUM power, as a KUSUM line, any year | Same notes. The only adjacent line is "Sale of Electricity" (nil FY25, Rs 421.72 lakh FY26). The AR never links it to KUSUM |
| Revenue from IPP, O&M, as separate lines | Same notes, and the segment note (consolidated Note 46, PAGE 144). Blocked by the single-segment conclusion |
| Any FY2024 revenue split by stream | AR Note 25 (PAGE 130) comparative column. This AR carries only FY2025 and FY2026 in the P&L notes; no FY2024 comparative exists for revenue |
| Top five customers as a share of revenue | AR Note 46 consolidated (PAGE 144) or Note 45 standalone (PAGE 185), or the MDA risk section. Only the single above-10% customer is given, as Ind AS 108 requires |
| Top customer as a stated PERCENTAGE, consolidated | AR Note 46 (PAGE 144). Only "more than 10%" and the rupee amount are given. The standalone note by contrast does state 79.74% |
| Reason why EPC, IPP and O&M are not separate operating segments | AR Note 46 paragraph i (PAGE 144) and Note 45 paragraph i (PAGE 185). Neither names those activities |
| Auditor or board comment on the single-segment conclusion | Independent Auditor's Report (Key Audit Matters) and the Directors' Report. Silent on segments throughout |
| Geographical revenue and non-current asset table promised by Note 46 item iii | AR PAGE 144, directly under "iii. Information about Geographical revenue and non-current asset." The heading is printed with no table under it |
| Order book split by customer type, on a consistent basis | Jun-2026 call PAGES 14 and 19. The Chairman gave the same 65/15/5/5/10 split twice, once as "total capacity" and once as "FY26", so the basis is not fixed |

---

# VERIFICATION QUESTION

I quoted most from runs/ina-2026-09-06/work/extracted/concalls__Concall_Jun_2026_Transcript.txt,
the FY2026 results call whose own header inside the document reads "Insolation Energy
Limited / May 27, 2026", cited at extraction marker PAGES 4, 5, 6, 9, 10, 13, 14, 15, 16,
18, 19 and 20.

The question: does the operator confirm that this file, dated 27-May-2026 on its own
header and listed in the brief as "concalls__Concall_Jun_2026_Transcript.txt (FY26 results
call, 27-May-2026)", is the correct and complete Q4 and FY2026 earnings call transcript,
and that its 20 extraction pages are the whole document? I ask because this single file is
the sole corpus source for four load-bearing facts that appear nowhere else: the FY2026
DCR split of 85/15 (PAGE 18), the Q4 FY2026 dispatch of "more than 500 megawatt" (PAGE 15),
the only rupee-per-watt prices in the corpus (PAGES 13 and 16), and the order book stated
as 1.6 to 1.8 GW (PAGE 6), which is the figure that conflicts with the 2.1 GW+ printed in
both the FY2026 Annual Report (PAGE 13) and the 21-Aug-2026 investor presentation
(PAGES 10 and 25).
