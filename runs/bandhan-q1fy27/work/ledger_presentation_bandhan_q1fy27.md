# A2 ENUMERATION LEDGER — BANDHAN Q1FY27 — Investor Presentation
Source: presentation_bandhan_q1fy27.pdf (48 pages/slides, 13 OCR pages: 2,4,9,20,23,24,27,35,38,39,41,46,48)
A1 extract: /home/user/inflection-pipeline/runs/bandhan-q1fy27/work/extract_presentation_bandhan_q1fy27.txt

```
=== A2 COUNT TEST ===
category: slides         grep_count: 48   sweep_count: 48   match: yes
category: slide_numbers  grep_count: 48   sweep_count: 48   match: yes
category: line_items     grep_count: 87   sweep_count: 87   match: yes
category: zero_standing  grep_count: 8    sweep_count: 8    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology: grep_count for slides/slide_numbers = `grep -n -E "^\[page [0-9]+\]" extract...txt | wc -l` = 48, verified against the manual page-by-page read below (48 distinct `[page N]` sections, N=1..48, no gaps, no dupes). line_items grep_count/sweep_count = row-by-row read of every clean financial/ratio table in the deck (page18 Avg Advances+Deposits, page22 NPA movement, page23 collection-efficiency + paying-profile, page25 EEB stress-pool, page30 non-interest income, page32 P&L, page33 balance sheet, page34 credit rating), cross-checked against `sed`-extracted raw table blocks. zero_standing = every row/value that is nil, dash, or explicitly flat/NIL across all periods shown.

No prior-quarter ledger path was supplied, so `DROPPED_SLIDE` diffing against Q4FY26's deck could not be performed — flagged as `PRIOR_LEDGER_UNAVAILABLE` (mechanical gap, not a company-quality issue).

---
## TABLE 1 — SLIDE INDEX (content type, OCR flag)

| Slide | Footer# | Title | Content type | OCR page? | Flags |
|---|---|---|---|---|---|
| 1 | n/a | Regulatory cover letter (Ref BBL/SEC/096/2026-27) | text/letter | no | — |
| 2 | n/a | Investor Presentation Q1FY27, 21st July 2026 (title) | title/photo | yes | OCR text garbled ("Banc andhan") — logo only, no data loss |
| 3 | 2 | Disclaimer | text | no | — |
| 4 | 3 | Key Highlights (section divider) | photo/divider | yes | no data on slide |
| 5 | 4 | Strategic Highlights: Q1FY27 | infographic | no | — |
| 6 | 5 | Key Financial Highlights: Q1FY27 | infographic (20-metric summary) | no | — |
| 7 | 6 | Extensive Pan-India Network with Deep Market Reach | map/chart | no | MAP_DATA_OCR_DEGRADED (per-state labels overlap) |
| 8 | 7 | Bandhan Bank's Journey On Its Strategic Objectives (4-panel trend chart) | chart | no | OCR_DEGRADED (panels 2-4 y-axis label ordering ambiguous) |
| 9 | 8 | Business & Financial Overview (section divider) | photo/divider | yes | no data on slide |
| 10 | 9 | Gross Advances Mix | chart+table | no | — |
| 11 | 10 | Emerging Entrepreneurs Business (EEB) | chart | no | — |
| 12 | 11 | Housing Finance | chart | no | — |
| 13 | 12 | Retail Assets | chart | no | OCR_UNCERTAIN_ORDER (product-share stack); SOURCE_LABEL_ERROR (disbursement 3rd column printed "Q1FY26", line 549, duplicating col 1 — likely meant Q1FY27) |
| 14 | 13 | Wholesale Banking | chart+pie | no | — |
| 15 | 14 | Geographical Distribution of Loans & Advances | map/chart | no | OCR_UNCERTAIN_ORDER (region-share stack) |
| 16 | 15 | Deposits | chart | no | SOURCE_LABEL_INCONSISTENT (CASA% chart axis reads "Mar'25" not "Jun'25" as base period, line 646) |
| 17 | 16 | Geographical Distribution of Deposits | map/chart | no | OCR_UNCERTAIN_ORDER |
| 18 | 17 | Average Balances – Advances & Deposits | table (clean) | no | SOURCE_LABEL_ERROR (Average Deposits table 5th column header printed "Q1FY26" instead of "Q1FY27", line 706) |
| 19 | 18 | Geographical Distribution of Banking Outlets | chart+table | no | Label check: "Additional 44 Banking Outlets" reconciles to YoY delta (6,388-6,344=44), not QoQ (6,388-6,355=33) — note for A3 |
| 20 | 19 | Asset Quality (section divider) | photo/divider | yes | no data on slide |
| 21 | 20 | Segmental NPA and Credit Cost | chart | no | MISSING_DATA_LABEL (GNPA Jun'26=3.1% not independently visible in this chart's OCR text; confirmed via page22 table cross-check) |
| 22 | 21 | NPA movement | table (clean) | no | — |
| 23 | 22 | EEB Collection Efficiency — **concall asset-quality slide (collection efficiency)** | table+chart | yes | OCR_DUPLICATE (lines 869-897 repeat page body, garbled) |
| 24 | 23 | EEB DPD movement — **concall asset-quality slide (SMA/DPD buckets)** | chart | yes | OCR_DUPLICATE (lines 938-966); DPD_REGIONAL_SPLIT_OCR_DEGRADED |
| 25 | 24 | EEB - Stress Pool and Vintage Analysis — **concall asset-quality slide (vintage/bounce chart)** | chart+table | no | CHART_OCR_DEGRADED (vintage-cohort line values legible, cohort-to-line mapping not reliably reconstructable) |
| 26 | 25 | Asset Quality: Strong focus on borrower affordability | chart | no | CHART_OCR_DEGRADED (Bandhan+N lender-count chart heavily fragmented, lines 1016-1136) |
| 27 | 26 | Financials (section divider) | photo/divider | yes | no data on slide |
| 28 | 27 | Financial Performance (1/2) | chart | no | — |
| 29 | 28 | Financial Performance (2/2) | chart | no | UNCLEAR_METRIC_LABEL (CRAR panel shows a second series 0.8%/0.7%/0.7% not captioned — likely Tier 2 capital add-on; not stated in extract) |
| 30 | 29 | Break up of Non-Interest Income | table (clean) | no | — |
| 31 | 30 | Financial Performance (ROA/Opex/ROE/Cost-Income) | chart | no | OCR_AMBIGUOUS_MAPPING (Opex/Assets panel: 5 values {4.4%,4.3%,3.9%,4.0%,4.0%} legible, period axis mapping uncertain; Q1FY27=4.3% cross-confirmed via slide 6) |
| 32 | 31 | Profit & Loss Statement | table (clean) | no | — |
| 33 | 32 | Balance Sheet | table (clean) | no | — |
| 34 | 33 | Credit Rating | table (clean) | no | — |
| 35 | 34 | Digital Offering and Indices (section divider) | photo/divider | yes | no data on slide |
| 36 | 35 | Digital Adoption Scorecard – Key digital indices | infographic (8 metrics) | no | — |
| 37 | 36 | Elevated mutual fund platform (UI/UX upgrade) | feature/photo | no | no quantitative data on slide |
| 38 | 37 | Digital onboarding — Corporate Salary Account Journey | feature/photo | yes | contains "0 Branch Visits" claim (ZERO_STANDING) |
| 39 | 38 | Deepening Relationship with our Sector Solutions Suite | feature/photo | yes | no quantitative data on slide |
| 40 | 39 | Empowering Merchants with Static QR Linked with POS Terminal | feature/photo | no | no quantitative data on slide |
| 41 | 40 | Our Board & Management (section divider) | photo/divider | yes | no data on slide |
| 42 | 41 | Strong Independent Board (1/2) | annexure/profiles | no | 9 director bios |
| 43 | 42 | Strong Independent Board (2/2) | annexure/profiles | no | 4 director bios |
| 44 | 43 | Experienced and professional team (1/2) — Core Management Team | annexure/profiles | no | 11 management bios |
| 45 | 44 | Experienced and professional team (2/2) — Core Management Team | annexure/profiles | no | 10 management bios |
| 46 | 45 | Awards and accolades (section divider) | photo/divider | yes | no data on slide |
| 47 | 46 | Awards and accolades (detail) | text | no | — |
| 48 | 47 | Thank You / contact | text | yes | — |

Manual sweep count of Table 1 rows = 48. Matches grep_count 48. **GATE A2 (slides): pass.**

---
## TABLE 2 — DISCRETE DATA POINTS PER SLIDE

### Slide 1 (cover letter)
1.1 Ref. No.: BBL/SEC/096/2026-27
1.2 Date: July 21, 2026
1.3 Cross-ref letter: Ref. No. BBL/SEC/095/2026-27 dated July 21, 2026
1.4 BSE Scrip Code: 541153
1.5 NSE Symbol: BANDHANBNK
1.6 Quarter: Q1 ended June 30, 2026
1.7 Signatory: Indranil Banerjee, Company Secretary
1.8 Digital signature timestamp: 2026.07.21 16:19:26 +05'30'

### Slide 5 — Strategic Highlights: Q1FY27
2.1 Branches: 1,988 (35 States and UTs)
2.2 EEB Banking Units: 4,400
2.3 ATMs: 438
2.4 EEB: ₹526.4 bn (~34% share of book)
2.5 Housing & Retail: ₹506.4 bn (~33% share of book)
2.6 Wholesale Banking: ₹512.8 bn (~33% share of book)
2.7 Total Customers: 31.8 mn
2.8 Digital Transaction: 98% of retail transactions are digital
2.9 Digital Onboarding: 92% saving accounts opened digitally (tab assisted/DIY)
2.10 CRAR: 18.2% (incl. profit)
2.11 CET1: 17.5% (incl. profit)
2.12 Retail Deposits: 74% of Total Deposits
2.13 Cost/Income: 61.5%
2.14 Emp Productivity: 8.6% YoY increase in Business/employee
2.15 Training & Upskilling: 347K learning hours
2.16 Footnote: Total Employees as on Jun'26 = 74,744

### Slide 6 — Key Financial Highlights: Q1FY27 (headline metric, value, YoY delta, QoQ delta)
3.1 Gross Advances: ₹1,555.6 bn* | 16.4% YoY | 0.9% QoQ
3.2 Secured Mix: 56.8% | 473 bps YoY | 67 bps QoQ
3.3 Non-EEB Book: ₹1,029.1 bn | 27.4% YoY | 2.6% QoQ
3.4 Share of Non-East (advances): 62.1%^ | 30 bps YoY | 19 bps QoQ
3.5 Total Deposit: ₹1,648.9 bn | 6.6% YoY | -0.9% QoQ
3.6 CASA Ratio: 29.4% | 234 bps YoY | 9 bps QoQ
3.7 Retail Deposits: ₹1,219.6 bn | 15.6% YoY | -0.5% QoQ
3.8 Share of Non-East (deposits): 43.5% | -167 bps YoY | -154 bps QoQ
3.9 GNPA Ratio: 3.1% | -182 bps YoY | -12 bps QoQ
3.10 NNPA Ratio: 0.9% | -43 bps YoY | -4 bps QoQ
3.11 PCR**: 71.1% | -259 bps YoY | 1 bps QoQ
3.12 Credit Cost: 1.8% | -167 bps YoY | -15 bps QoQ
3.13 NII: ₹29.2 bn | 5.9% YoY | 4.5% QoQ
3.14 Total Revenue (Net): ₹35.2 bn | 1.2% YoY | -1.2% QoQ
3.15 Operating Profit: ₹13.6 bn | -18.6% YoY | -5.8% QoQ
3.16 PAT: ₹5.0 bn | 34.9% YoY | -6.1% QoQ
3.17 NIM: 6.2% | -16 bps YoY | 2 bps QoQ
3.18 OPEX/Assets: 4.3% | 41 bps YoY | -9 bps QoQ
3.19 ROA: 1.0% | 20 bps YoY | -11 bps QoQ
3.20 ROE: 7.7% | 179 bps YoY | -82 bps QoQ
3.21 Footnote *: Includes PTC of ₹4.03 bn
3.22 Footnote **: PCR including SR provision at 74.3%, stable QoQ
3.23 Footnote ^: excludes PTC & IBPC

### Slide 7 — Pan-India Network
4.1 Total Banking Outlets: 6,388 (as on 30 Jun'26), across 35 States & UTs
4.2 Share of Banking Outlets by Region (headline totals): Eastern 2,864; Central 830; Southern 1,045(approx); other region totals shown as 2034/299/683/660/647/489 in raw layout — MAP_DATA_OCR_DEGRADED, individual per-state counts (~35 values, e.g. J&K 22, Chandigarh 33, Punjab 44, Haryana 55/62, NCT Delhi 86/87/91/93, Bihar 88/560, Rajasthan 232/233/557/490/491, Gujarat 683, Maharashtra 311, Goa 66/176, Karnataka 172/178, Kerala 26/28, Tamil Nadu 127/133, West Bengal 1,727, others) recorded but not individually attributable to labels with confidence
4.3 Regional groupings legend: East=WB,BR,JH,OD,SK,A&N; Central=CG,MP,UP,UK; South=AP,TS,KA,KL,TN,PY; West=MH,GJ,GA,D&D; NE=ARP,AS,MN,MZ,ML,NL,TR; North=DL,PB,HR,RJ,HP,CH,J&K,LA
4.4 Map data attribution: "Powered by Bing", "© GeoNames, Microsoft, TomTom"

### Slide 8 — Journey On Strategic Objectives (4-panel trend chart, Q1FY25–Q1FY27, 9 quarters each)
5.1 Panel 1 Secured %: 42.9,47.0,48.9,50.5,52.1,54.9,56.2,56.7,56.8 (Q1FY25→Q1FY27)
5.2 Panel 1 Unsecured %: 57.1,53.0,51.1,49.5,47.9,45.1,43.8,43.3,43.2
5.3 Panel 2 Retail-deposit-share series: values present 73.7%,74.0%,72.4%,70.9%,69.1%,68.7%,68.9%,67.8%,68.2% — OCR_DEGRADED, exact quarter mapping not reliable
5.4 Panel 3 GNPA%: 4.2,4.7,4.7,4.7,5.0,5.0,3.3,3.3,3.1 (cross-checks to page22 table)
5.5 Panel 3 NNPA%: 1.1,1.3,1.3,1.3,1.4,1.4,1.0,1.0,0.9
5.6 Panel 3 Credit Cost%: 1.6,1.9,3.9,3.5,3.4,3.3,2.0,1.8 (8 legible values vs 9 quarters — one value not captured, OCR_DEGRADED)
5.7 Panel 4 ROA%/ROE%(RHS) — values present 0.2,0.4,0.8,0.9,0.7,1.0,1.1,1.0 and secondary-axis gridline labels 5%,10%,15%,20% — OCR_DEGRADED, series-to-quarter mapping not reliable

### Slide 10 — Gross Advances Mix (₹ bn)
6.1 Total Gross Advances: Jun'25 1,336.2 | Mar'26 1,542.3 | Jun'26 1,555.6 (16.4% YoY, 0.9% QoQ)
6.2 EEB Group: 528.1 | 539.1 | 526.4
6.3 Housing: 326.6 | 347.9 | 345.4
6.4 Retail: 111.0 | 160.9 | 161.0
6.5 Wholesale Banking Group: 370.5 | 484.5 | 512.8
6.6 IBPC: 0 | 10.0 | 10.0
6.7 Share of Loan Book: Wholesale 27.7%/31.4%/33.0%; Retail 8.3%/10.4%/10.4%; Housing 24.4%/22.6%/22.2%; SBAL 14.3%/11.8%/11.2%; EEB Group 25.2%/23.1%/22.6%; IBPC 0.0%/0.6%/0.6% (Jun'25/Mar'26/Jun'26)
6.8 Footnote: Share of EEB (Group+SBAL) reduced from 39.5% in Jun'25 to 33.8% in Jun'26
6.9 Footnote: Gross advances includes PTC; SBAL is part of EEB portfolio

### Slide 11 — EEB (₹ bn)
7.1 EEB Asset Growth total: Jun'25 528.1 | Mar'26 539.1 | Jun'26 526.4 (YoY -0.3%, QoQ -2.3%)
7.2 — EEB Group sub-split: 336.5 | 357.0 | 352.2
7.3 — SBAL sub-split: 191.6 | 182.1 | 174.2
7.4 Number of Active Borrowers (Mn): Jun'25 12.9 | Mar'26 12.4 | Jun'26 12.9
7.5 EEB Loan Disbursement total: Q1FY26 107.1 | Q4FY26 150.4 | Q1FY27 105.0
7.6 — EEB Group sub-split: 77.2 | 104.6 | 73.7
7.7 — SBAL sub-split: 29.8 | 45.8 | 31.3

### Slide 12 — Housing Finance (₹ bn)
8.1 Housing product total: Jun'25 326.6 | Mar'26 347.9 | Jun'26 345.4 (5.7% YoY, -0.7% QoQ)
8.2 Housing sub-product: 262.1 | 267.6 | 263.0
8.3 LAP: 62.5 | 77.9 | 79.2
8.4 Construction: 2.1 | 2.5 | 3.1
8.5 Borrowers Bifurcation Jun'26: Salaried 42.0%; Self Employed 56.5%; Professionals 1.5%
8.6 Housing Asset Disbursements: Q1FY26 18.2 | Q4FY26 24.6 | Q1FY27 15.0
8.7 Housing: Product wise share — Housing 80.2%/76.9%/76.2%; LAP 19.1%/22.4%/22.9%; Construction 0.6%/0.7%/0.9% (Jun'25/Mar'26/Jun'26)

### Slide 13 — Retail Assets (₹ bn)
9.1 Retail Assets total: Jun'25 111.0 | Mar'26 160.9 | Jun'26 161.0 (45.0% YoY, 0.1% QoQ)
9.2 Vehicle: 22.2 | 26.6 | 28.4(approx, OCR-uncertain ordering)
9.3 Personal: 19.5 | ... | 28.3 (OCR-uncertain ordering)
9.4 Gold: 17.6 | 29.8 | ...
9.5 TD-OD: 9.2 | ...
9.6 Others: 42.5 | 57.4 | 61.1
9.7 Product wise share (values present, mapping OCR-uncertain): 8.3%,10.5%,12.1%,15.9%,18.8%,14.8%,17.5%,18.5%,17.6%,20.0%,16.5%,17.6%,38.3%,35.7%,38.0%
9.8 Retail Disbursements: Q1FY26 19.7 | Q4FY26 32.8 | third column (printed "Q1FY26", likely Q1FY27) 22.7 — SOURCE_LABEL_ERROR flagged

### Slide 14 — Wholesale Banking (₹ bn)
10.1 Wholesale total: Jun'25 370.5 | Mar'26 484.5 | Jun'26 512.8 (38.4% YoY, 5.8% QoQ)
10.2 FIG,H&E: 17.4 | 36.9 | 42.1
10.3 CBG: 123.3 | 186.0 | 203.1
10.4 BBG: 167.9 | 212.3 | 220.5
10.5 ABG: 21.6 | 21.6 | 21.9
10.6 Others: 40.4 | 27.7 | 25.2
10.7 FIG,H&E rating mix (as on 30 Jun'26): AAA 4%, AA+ 19%, AA 24%, AA- 27%, A+ 11%, A 7%, A- 3%, BBB+&Below 3%, Others 0.4%; caption "96% of outstanding are A- & Above"
10.8 CBG rating mix (as on 30 Jun'26): AA-&Above 34%, BBB+ to A+ 42%, BBB&Below 16%, Unrated&Others 8%; caption "76% of outstanding are BBB+ & Above"
10.9 Definitions footnote: FIG,H&E=Financial Institution Group; CBG=Corporate Banking Group (erstwhile MMG); BBG=Business Banking Group; ABG=Aspiring Business Group (erstwhile SEL); Others incl. SME LAP and Agri

### Slide 15 — Geographical Distribution of Loans & Advances
11.1 Share by Region (Jun'25/Mar'26/Jun'26): Eastern 33%/33%/33%; values for NE/Central/Northern/Southern/Western present as 5%,14-15%,9-10%,16-17%,21-22% — OCR_UNCERTAIN_ORDER
11.2 Share by States: West Bengal 42%/42%/42%; Maharashtra ~7%/6%/6%; Bihar ~7%/7%/6%; Gujarat 14%/15%/15%; MP 23%/24%/24%; Others = remainder
11.3 Category-wise distribution (as on 30 Jun'26): values 12%,14%,35%,39% mapped Metro/Urban/Semi Urban/Rural per legend order
11.4 Footnote: Geographical distribution excludes IBPC & PTC

### Slide 16 — Deposits (₹ bn)
12.1 Deposits total: Jun'25 1,546.7 | Mar'26 1,663.4 | Jun'26 1,648.9 (6.6% YoY, -0.9% QoQ)
12.2 CA: 64.7 | 114.8 | 88.9
12.3 SA: 353.9 | 372.7 | 395.9
12.4 TD Retail: 636.6 | 737.9 | 734.8
12.5 TD Others: 491.5 | 438.0 | 429.3
12.6 Retail Deposits % (CASA+Retail TD): Jun'25 68.2% | Mar'26 73.7% | Jun'26 74.0%
12.7 CASA %: base period labeled Mar'25 27.1% | Mar'26 29.3% | Jun'26 29.4% (SOURCE_LABEL_INCONSISTENT — base period differs from the Jun'25 base used elsewhere on this slide)
12.8 Average SA Balance/Account (₹'000) — General Banking: 39.7 | 38.9 | 41.6; EEB: 1.6 | 1.7 | 1.4
12.9 Footnote: EEB deposits contribute 2.4% of Total deposit as of Jun'26

### Slide 17 — Geographical Distribution of Deposits
13.1 Share by Region: Eastern 50%/51%/52%; NE 4%; Central 12%/11%/11%; Northern 12%/11%/11%; Southern 8%/8%/8%; Western 14%/15%/14% (Jun'25/Mar'26/Jun'26)
13.2 Share by States: West Bengal 33%/33%/32%; Maharashtra 4%/4%/5%; UP/NCT Delhi/Odisha values present (7%,4%,6%,11%,13%,12%,4%) — OCR_UNCERTAIN_ORDER; Others 41%/40%/41%
13.3 Category-wise deposit distribution (as on 30 Jun'26): Metro 40%, Urban 37%, Semi Urban 14%, Rural 9%

### Slide 19 — Geographical Distribution of Banking Outlets
14.1 Branches: Jun'25 1,750 | Mar'26 1,955 | Jun'26 1,988
14.2 Banking Units: Jun'25 4,594 | Mar'26 4,400 | Jun'26 4,400 [ZERO_STANDING-adjacent: Mar'26→Jun'26 flat at 4,400]
14.3 Total: Jun'25 6,344 | Mar'26 6,355 | Jun'26 6,388
14.4 Label: "Additional 44 Banking Outlets" (reconciles to YoY 6,388-6,344, not QoQ 6,388-6,355=33 — note for A3)
14.5 Regional Diversification pie (as on 30 Jun'26): 12%,33%,18%,37% (Metro/Urban/Semi Urban/Rural per legend order)
14.6 Share of Banking Outlets by Region — Jun'26: Eastern 45%, NE 10%, Central 16%, Northern 8%, Southern 11%, Western 10%
14.7 — Mar'26: Eastern 45%, NE 10%, Central 17%, Northern 6%, Southern 12%, Western 10%
14.8 — Jun'25: Eastern 45%, NE 10%, Central 16%, Northern 7%, Southern 11%, Western 11%

### Slide 21 — Segmental NPA and Credit Cost
15.1 Segmental GNPA (₹ bn) Jun'25: Total 66.2 = EEB 47.5 + Housing 8.1 + WBG 7.3 + Retail 3.3
15.2 Mar'26: Total 50.2 = EEB 31.1 + Housing 9.8 + WBG 5.8 + Retail 3.5
15.3 Jun'26: Total 48.8 = EEB 31.0 + Housing 8.0 + WBG 6.3 + Retail 3.5
15.4 Credit Cost: Q1FY26 3.5% | Q4FY26 2.0% | Q1FY27 1.8% | FY25 2.9% | FY26 3.0%
15.5 Gross NPA%: Jun'25 5.0% | Mar'26 3.3% | Jun'26 3.1%(cross-check, see MISSING_DATA_LABEL flag) 
15.6 Net NPA%: Jun'25 1.4% | Mar'26 1.0% | Jun'26 0.9%
15.7 PCR incl. SRs: Jun'25 73.7% | Mar'26 74.2% | Jun'26 74.3%
15.8 PCR (standalone): Jun'26 71.1%
15.9 Footnote: Credit cost is including the standard asset provisions

### Slide 22 — NPA movement (₹ bn, clean table) — full row-by-row (see Table 3 for line-item register)
16.1–16.15 See Table 3, rows 1–15
16.16 Footnote: Recoveries & Upgrades include amount received from the ARC sale during the respective quarters

### Slide 23 — EEB Collection Efficiency [concall slide]
17.1 Top states table — West Bengal: Mar'26 98.4%, Jun'26 98.2%, Q4FY26 99.1%, Q1FY27 98.7%
17.2 Assam: Mar'26 99.4%, Jun'26 99.3%, Q4FY26 99.9%, Q1FY27 99.5%
17.3 Rest of India: Mar'26 98.7%, Jun'26 98.5%, Q4FY26 99.3%, Q1FY27 98.9%
17.4 Total: Mar'26 98.6%, Jun'26 98.5%, Q4FY26 99.3%, Q1FY27 98.9%
17.5 Collection Efficiency chart (Month/Quarter, Including NPA/Excluding NPA/Including Arrears) — legible values: 110.2%, 108.4%, 99.3%, 98.9%, 111.8%, 95.4%, 95.4%, 110.0%, 98.6%, 98.5%, 94.7%, 94.7% — OCR_DEGRADED, series-to-label mapping uncertain
17.6 Customer Paying Profile Mar'26: Full Paying 96.3% customers/97.1% receivables; Partial Paying 3.3%/2.5%; Non-Paying 0.4%/0.4%; Total 100.0%/100.0%
17.7 Customer Paying Profile Jun'26: Full Paying 97.3%/97.8%; Partial Paying 1.8%/1.4%; Non-Paying 0.9%/0.8%; Total 100.0%/100.0%
17.8 Footnote: collection efficiency and paying profile calculated excluding NPA portfolio; EEB = Group Loan and Small Business and Agri Loans
17.9 OCR duplicate block (lines 869-897) repeats 17.1-17.8 with corrupted digits — OCR_DUPLICATE, not a distinct disclosure

### Slide 24 — EEB DPD movement [concall slide]
18.1 SMA 0: Jun'25 ₹10.2 bn;1.9% | Mar'26 ₹7.9 bn;1.5% | Jun'26 ₹9.6 bn;1.8%
18.2 SMA 1: Jun'25 ₹5.3 bn;1.0% | Mar'26 ₹4.4 bn;0.8% | Jun'26 ₹4.6 bn;0.9%
18.3 SMA 2: Jun'25 ₹4.8 bn;0.9% | Mar'26 ₹4.2 bn;0.8% | Jun'26 ₹4.2 bn;0.8%
18.4 NPA: Jun'25 ₹47.6 bn;9.0% | Mar'26 ₹31.1 bn;5.8% | Jun'26 ₹31.0 bn;5.9% (cross-checks to slide25 stress-pool NPA row)
18.5 Regional split (West Bengal/Assam/Rest of India) sub-bars present per bucket per period but DPD_REGIONAL_SPLIT_OCR_DEGRADED — bucket totals in 18.1-18.4 are reliable, regional attribution is not
18.6 OCR duplicate block (lines 938-966) — OCR_DUPLICATE

### Slide 25 — EEB Stress Pool and Vintage Analysis
19.1 Vintage Analysis line chart: NPA(%) by Month-on-Book (0-18), 8 cohort lines Q1'2025-Q4'2026; legible value set: 7.0%,6.4%,6.1%,6.0%,5.8%,5.4%,5.4%,5.2%,4.9%,4.9%,4.6%,4.2%,4.2%,4.0%,3.8%,3.5%,3.3%,2.1%,2.0%,1.0%,0.8%,0.0% — CHART_OCR_DEGRADED, cohort-to-line mapping not reliably reconstructable
19.2-19.9 EEB Stress-Pool & Provisions table — see Table 3, rows 16-24
19.10 Footnote (implicit): "PCR % (Outstanding % on Stress pool)" row carries dash "-" for QoQ%/YoY% in FY25/FY26 columns — ZERO_STANDING

### Slide 26 — Asset Quality: Strong focus on borrower affordability
20.1 "Bandhan bank" (sole-lender) share series (9 periods Jun'24-Jun'26): legible values 59.4%,60.8%,61%,62.5%,63.0%,64% — CHART_OCR_DEGRADED
20.2 "Bandhan+1" series: 19%,20.8%,21%,22.0%,22.6%,23.8%
20.3 "Bandhan+2" series: 9%,10%,10.4%,10.7%,10.9%,11.3%
20.4 "Bandhan+3" series: 3.2%,3.3%,5%,5.2%
20.5 "Bandhan+4" series: 0.6%,0.8%,1.9%,2%,2.3%,3%
20.6 "Bandhan+>4" series: 0.2%,0.3%,0.6%
20.7 Caption: "96% of the Portfolio" (Bandhan-only or max-2-lenders)
20.8 Callout: "Sharp decrease in other Lenders QoQ"
20.9 Period axis: June'24, Sep'24, Dec'24, Mar'25, Jun'25, Sept'25, Dec-25, Mar-26, Jun-26 (9 periods)
20.10 Bullet notes: "Majority of the borrowers with loan only with Bandhan or at max two lenders."; "Strong focus towards orderly resolution of leveraged portfolio"

### Slide 28 — Financial Performance (1/2), ₹ bn
21.1 NII: Q1FY26 27.6 | Q4FY26 28.0 | Q1FY27 29.2 (QoQ 4.5%, YoY 5.9%) | FY25 114.9 | FY26 108.3 (YoY -5.8%)
21.2 Operating Profit: Q1FY26 16.7 | Q4FY26 14.4 | Q1FY27 13.6 (QoQ -5.8%, YoY -18.6%) | FY25 73.9 | FY26 58.7 (YoY -20.6%)
21.3 PAT: Q1FY26 3.7 | Q4FY26 5.3 | Q1FY27 5.0 (QoQ -6.1%, YoY 34.9%) | FY25 27.5 | FY26 12.2 (YoY -55.4%)

### Slide 29 — Financial Performance (2/2)
22.1 Spread (Annualized): Q1FY26 Yield 12.7%/CoF 7.0%/Spread 5.7%; Q4FY26 Yield 12.0%/CoF 6.5%/Spread 5.5%; Q1FY27 Yield 12.0%/CoF 6.4%/Spread 5.6%; FY25 Yield 13.5%/CoF 7.1%/Spread 6.4%; FY26 Yield 12.2%/CoF 6.8%/Spread 5.4%
22.2 CRAR (incl. profit): Jun'25 19.4% | Mar'26 18.0% | Jun'26 18.2%
22.3 Secondary CRAR-panel series (uncaptioned): 0.8% | 0.7% | 0.7% — UNCLEAR_METRIC_LABEL
22.4 CET1 (incl. profit): Jun'25 18.6% | Mar'26 17.3% | Jun'26 17.5%
22.5 NIM (Annualized): Q1FY26 6.4% | Q4FY26 6.2% | Q1FY27 6.2% | FY25 7.1% | FY26 6.1%

### Slide 30 — Break up of Non-Interest Income (₹ Mn) — see Table 3 rows 25-33
23.1 Footnote: Q1FY26 other income includes treasury gain of ~₹2.5 bn; excluding treasury income, non-interest income growth would have been ~22% YoY in Q1FY27

### Slide 31 — Financial Performance (ROA/Opex/ROE/Cost-Income)
24.1 ROA (Annualized): Q1FY26 0.8% | Q4FY26 1.1% | Q1FY27 1.0% | FY25 1.5% | FY26 0.6%
24.2 Opex/Average Assets (Annualized): value set {4.4%,4.3%,3.9%,4.0%,4.0%} across Q1FY26/Q4FY26/Q1FY27/FY25/FY26 — OCR_AMBIGUOUS_MAPPING; Q1FY27=4.3% cross-confirmed via slide 6
24.3 ROE (Annualized): Q1FY26 5.9% | Q4FY26 8.5% | Q1FY27 7.7% | FY25 11.6% | FY26 4.8%
24.4 Cost to Income Ratio: Q1FY26 52.1% | Q4FY26 59.6% | Q1FY27 61.5% | FY25 48.9% | FY26 56.8%

### Slide 32 — Profit & Loss Statement (₹ bn, clean table) — see Table 3 rows 34-44

### Slide 33 — Balance Sheet (₹ bn, clean table) — see Table 3 rows 45-59

### Slide 34 — Credit Rating — see Table 3 rows 60-65
25.1 Footnote *: ICRA rating for ₹30 bn only
25.2 Footnote **: ICRA rating for ₹0.75 bn only
25.3 Footnote #: erstwhile GRUH Finance Limited transferred to Bandhan Bank Ltd
25.4 Footnote ^: SR's received against stress loan transferred during quarter ended 31 Dec'25; Net Book value of all SR's is NIL as on March 31, 2026 [ZERO_STANDING]
25.5 Footnote ~: outstanding face value turned ₹1.00, not rated by ARCs as at June 30, 2026
25.6 Note: Gross value of Outstanding SR's are 100% provided

### Slide 36 — Digital Adoption Scorecard
26.1 98% of retail transactions are digital
26.2 90% CBDT Payments digitally
26.3 59% RD Invested digitally
26.4 92% Saving Accounts opened digitally #
26.5 99.9% of GST transactions are digital
26.6 233% QoQ Growth in Total transaction Value from Payment Aggregator Business
26.7 115%* New MF Invested Digitally (YoY Q1 growth)
26.8 28% Online Deposit Contribution to Overall Fixed Deposits
26.9 Footnote: Indices pertaining to Q1FY27; *YoY Q1 growth; #Through Tab/Assisted/DIY

### Slide 38 — Digital onboarding: Corporate Salary Account Journey
27.1 100% Digital Journey
27.2 Video KYC Enabled
27.3 24x7 Anywhere Access
27.4 0 Branch Visits [ZERO_STANDING — explicit zero-value feature claim]
27.5 Instant Application Submission
27.6 Digital Journey Flow: Customer Profiler > Product Selection > Employment Verification > Video KYC > Account Opening

### Slide 42-43 — Board of Directors (13 profiles; see Table 4)
### Slide 44-45 — Core Management Team (21 profiles; see Table 4)

### Slide 47 — Awards and accolades
28.1 ET Edge Best BFSI Brands Award, 2026 (9th Edition, held in Mumbai); also won ET Now Best BFSI Brands Award 2025
28.2 Gallup Exceptional Workplace Award 2025 — "among the only 62 organisations worldwide" recognized; "two time winner"
28.3 DIGIXX Awards 2026 by Adgully — digital lead-generation campaign, "six products categories"

### Slide 48 — Thank You / contact
29.1 Vikash Mundhra, Head – Investor Relations
29.2 investor.relations@bandhanbank.com

Slides with no numeric/discrete data (dividers/pure marketing feature copy — enumerated in Table 1, not repeated here): 2 (title only), 3 (disclaimer text), 4, 9, 20, 27, 35, 37, 39, 40, 41, 46.

---
## TABLE 3 — FINANCIAL-TABLE LINE-ITEM REGISTER (clean tables only; 87 rows = line_items count)

| # | Slide | Table | Line item | Periods covered | Flag |
|---|---|---|---|---|---|
| 1 | 22 | NPA movement | Opening GNPA (A) | Q1FY26..Q1FY27, FY25, FY26 | — |
| 2 | 22 | NPA movement | Fresh Slippages (B) | same | — |
| 3 | 22 | NPA movement | Recoveries & Upgrades | same | — |
| 4 | 22 | NPA movement | Technical Write offs | same | — |
| 5 | 22 | NPA movement | NPA Sale to ARC (D) | same | ZERO_STANDING (dash Q1FY26,Q2FY26,Q4FY26,FY25) |
| 6 | 22 | NPA movement | Technical Additions (other than slippages) (E) | same | ZERO_STANDING (dash ALL periods) |
| 7 | 22 | NPA movement | Closing Gross (F) | same | — |
| 8 | 22 | NPA movement | Provisions | same | — |
| 9 | 22 | NPA movement | Net NPA | same | — |
| 10 | 22 | NPA movement | GNPA Ratio | same | — |
| 11 | 22 | NPA movement | NNPA Ratio | same | — |
| 12 | 22 | NPA movement | Credit Cost | same | — |
| 13 | 22 | NPA movement | PCR | same | — |
| 14 | 22 | NPA movement | PCR (incl. Security Receipts) | same | — |
| 15 | 22 | NPA movement | PCR (incl. Technical write offs) | same | — |
| 16 | 25 | EEB Stress-Pool & Provisions | SMA 1 | Jun'25/Mar'26/Jun'26/QoQ/YoY/FY25/FY26/YoY | — |
| 17 | 25 | EEB Stress-Pool & Provisions | SMA 2 | same | — |
| 18 | 25 | EEB Stress-Pool & Provisions | NPA | same | — |
| 19 | 25 | EEB Stress-Pool & Provisions | EEB Stress-Pool Total | same | — |
| 20 | 25 | EEB Stress-Pool & Provisions | Provision for NPA | same | — |
| 21 | 25 | EEB Stress-Pool & Provisions | Provision for Standard Assets - Normal | same | ZERO_STANDING (YoY flat 0.0%) |
| 22 | 25 | EEB Stress-Pool & Provisions | Additional Provision for Standard Assets | same | ZERO_STANDING (YoY flat 0.0%) |
| 23 | 25 | EEB Stress-Pool & Provisions | EEB Provisions Total | same | — |
| 24 | 25 | EEB Stress-Pool & Provisions | PCR % (Outstanding % on Stress pool) | Jun'25/Mar'26/Jun'26 only | ZERO_STANDING (QoQ/YoY dash) |
| 25 | 30 | Non-Interest Income | Processing Fees | Q1FY26/Q4FY26/Q1FY27/QoQ/YoY/FY25/FY26/YoY | — |
| 26 | 30 | Non-Interest Income | Third Party Income | same | — |
| 27 | 30 | Non-Interest Income | P&L on Investment sale and Revaluation | same | — |
| 28 | 30 | Non-Interest Income | Release of prov on redemption of SR (ARC) | same | — |
| 29 | 30 | Non-Interest Income | Collection fees from ARC | same | — |
| 30 | 30 | Non-Interest Income | Product / Service Charges | same | — |
| 31 | 30 | Non-Interest Income | Bad Debts Recovery (on write-off) | same | — |
| 32 | 30 | Non-Interest Income | Others | same | — |
| 33 | 30 | Non-Interest Income | Total Other Income | same | — |
| 34 | 32 | P&L Statement | Interest Income | Q1FY26/Q4FY26/Q1FY27/QoQ/YoY/FY25/FY26/YoY | — |
| 35 | 32 | P&L Statement | Interest expenses | same | — |
| 36 | 32 | P&L Statement | Net Int. Income (NII) | same | — |
| 37 | 32 | P&L Statement | Non Interest Income | same | — |
| 38 | 32 | P&L Statement | Total Income | same | — |
| 39 | 32 | P&L Statement | Operating Expenses | same | — |
| 40 | 32 | P&L Statement | Operating Profit | same | — |
| 41 | 32 | P&L Statement | Provision (Std. + NPA) | same | — |
| 42 | 32 | P&L Statement | Profit before tax | same | — |
| 43 | 32 | P&L Statement | Tax | same | — |
| 44 | 32 | P&L Statement | Profit after tax | same | — |
| 45 | 33 | Balance Sheet | Capital | 30Jun'25/31Mar'26/30Jun'26/YoY | ZERO_STANDING (flat, YoY 0.0%) |
| 46 | 33 | Balance Sheet | Employees stock options outstanding | same | — |
| 47 | 33 | Balance Sheet | Reserves & Surplus | same | — |
| 48 | 33 | Balance Sheet | Shareholders Funds | same | — |
| 49 | 33 | Balance Sheet | Deposits | same | — |
| 50 | 33 | Balance Sheet | Borrowings | same | — |
| 51 | 33 | Balance Sheet | Other liabilities and provisions | same | — |
| 52 | 33 | Balance Sheet | Total (Capital & Liabilities) | same | — |
| 53 | 33 | Balance Sheet | Cash and balances with RBI | same | — |
| 54 | 33 | Balance Sheet | Balance with Banks and Money at call and short notice | same | — |
| 55 | 33 | Balance Sheet | Investments | same | — |
| 56 | 33 | Balance Sheet | Advances | same | — |
| 57 | 33 | Balance Sheet | Fixed Assets | same | — |
| 58 | 33 | Balance Sheet | Other Assets | same | — |
| 59 | 33 | Balance Sheet | Total (Assets) | same | — |
| 60 | 34 | Credit Rating | Security Receipts - RR2 | as on 30 Jun'26 | — |
| 61 | 34 | Credit Rating | Security Receipts - RR3 | same | — |
| 62 | 34 | Credit Rating | Security Receipts - RR4 | same | — |
| 63 | 34 | Credit Rating | Security Receipts - Unrated | same | ZERO_STANDING (Net Book Value NIL per footnote) |
| 64 | 34 | Credit Rating | Non-Convertible Debenture | same | — |
| 65 | 34 | Credit Rating | Certificate of Deposit | same | — |
| 66 | 23 | Collection Efficiency top-states | West Bengal | Mar'26/Jun'26/Q4FY26/Q1FY27 | — |
| 67 | 23 | Collection Efficiency top-states | Assam | same | — |
| 68 | 23 | Collection Efficiency top-states | Rest of India | same | — |
| 69 | 23 | Collection Efficiency top-states | Total | same | — |
| 70 | 23 | Customer Paying Profile | Full Paying | Mar'26/Jun'26 | — |
| 71 | 23 | Customer Paying Profile | Partial Paying | same | — |
| 72 | 23 | Customer Paying Profile | Non-Paying | same | — |
| 73 | 23 | Customer Paying Profile | Total | same | — |
| 74 | 18 | Average Advances | EEB | Q1FY26..Q1FY27/QoQ/YoY | — |
| 75 | 18 | Average Advances | Housing Finance | same | — |
| 76 | 18 | Average Advances | Retail Assets | same | — |
| 77 | 18 | Average Advances | Wholesale Banking | same | — |
| 78 | 18 | Average Advances | IBPC / Others | same | — |
| 79 | 18 | Average Advances | Total Average Advances | same | — |
| 80 | 18 | Average Deposits | CASA | Q1FY26..Q1FY27/QoQ/YoY | SOURCE_LABEL_ERROR (5th col header printed Q1FY26) |
| 81 | 18 | Average Deposits | - Current Account (CA) | same | same header flag |
| 82 | 18 | Average Deposits | - Savings Account (SA) | same | same header flag |
| 83 | 18 | Average Deposits | Term Deposit | same | same header flag |
| 84 | 18 | Average Deposits | - Retail TD | same | same header flag |
| 85 | 18 | Average Deposits | - Bulk Deposit (incl. CDs) | same | same header flag |
| 86 | 18 | Average Deposits | Total Average Deposits | same | same header flag |
| 87 | 18 | Average Deposits | Total Average Retail Deposits | same | same header flag |

zero_standing rows flagged in Table 3: #5, #6, #21, #22, #24, #45, #63 = 7, plus slide 38's "0 Branch Visits" claim (not a table row, item 27.4 in Table 2) = **8 total zero_standing items**, matching the count test.

---
## TABLE 4 — DIRECTOR / MANAGEMENT PROFILE REGISTER (annexure-style, slides 42-45)

### Board of Directors (slide 42, 1/2) — 9 profiles
1. Debasish Panda — Non-Executive Chairman — 1987-batch IAS officer, ex-Chairman IRDAI, ex-Director RBI/SBI/BoB/LIC
2. Partha Pratim Sengupta — Managing Director & CEO — career banker ~40 yrs, retired SBI Deputy MD & CCO, former MD&CEO Indian Overseas Bank
3. Rajinder Kumar Babbar — Executive Director & Chief Business Officer — 3+ decades, 23+ yrs at HDFC Bank (Transportation/Infra Finance, Rural Banking, Retail Liabilities)
4. Ratan Kumar Kesh — Executive Director & Chief Operating Officer — ~3 decades multi-domain leadership
5. Debashish Mukherjee — Independent Director — 3+ decades at Punjab National Bank/United Bank of India/Canara Bank; former ED Canara Bank
6. Gauri Prosad Sarma — Independent Director — 37+ yrs IT; former CGM (Operations) PNB
7. N V P Tendulkar — Independent Director — finance/accounts/IT/mgmt; former ED-Finance, Hewlett Packard India
8. Subrata Dutta Gupta — Independent Director — Asset-based Financing incl. mortgage finance in Asia; retired Principal Financial Officer, IFC
9. Suhail Chander — Independent Director — 37 yrs banking; retired Head of Corporate & Institutional Banking, IndusInd Bank (2020)

### Board of Directors (slide 43, 2/2) — 4 profiles
10. Veni Thapar — Independent Director — CA & CMA, 29+ yrs audit experience; Independent Director, Bank of India
11. Vijay N Bhatt — Independent Director — accounting/audit/assurance; former Sr. Independent Director, BSR & Co. Chartered Accountants
12. Arun Kumar Singh — RBI (Nominee) Additional Director — appointed effective June 24, 2024; term extended to June 23, 2027 or earlier per RBI order; 35 yrs RBI experience
13. Avijit Mukerji — Non-Executive Non-Independent Director (Nominee of BFHL) — CA, 3+ decades audit/assurance; former Senior Partner, Price Waterhouse

### Core Management Team (slide 44, 1/2) — 11 profiles
14. Partha Pratim Sengupta — MD & CEO (repeat bio, condensed)
15. Rajinder Kumar Babbar — ED & CBO (repeat bio, condensed)
16. Ratan Kumar Kesh — ED & COO (repeat bio, condensed)
17. Rajeev Mantri — Chief Financial Officer — 28+ yrs, ex-CFO Citi India
18. Santanu Banerjee — Head, Human Resources — 31+ yrs, ex-Head HR Business Relationship, Axis Bank
19. Suresh Chandran — Head, Branch Banking/CA/Affluent TPP & Govt Business — 30+ yrs, ex-EVP/Unit Head, IndusInd Bank
20. Satish Kumar — Head, Wholesale Banking — 27+ yrs, ex-National Head Credit-Mid Market, Kotak Mahindra Bank
21. Hirak Sumatiprasad Joshi — Head, Retail Assets — 29+ yrs, ex-Business Head Vehicle Finance, Ujjivan SFB
22. Surajit Roy Chowdhury — Head, Emerging Entrepreneurs Business — 28+ yrs, ex-State Head NE, IndusInd Bank
23. Amitava Goswami — Chief Compliance Officer — 32+ yrs, ex-Axis Bank Retail Banking/Ops leadership
24. Biju E Punnachalil — Chief Risk Officer — 33+ yrs, ex-GM & CRO, South Indian Bank

### Core Management Team (slide 45, 2/2) — 10 profiles
25. Rajesh Kumar Srivastava — Head, Liability & Transaction Operations and Ops Support Group — 30+ yrs, ex-Head Products & PNO, Suryoday Bank
26. Pinaki Halder — Chief Information Officer — 28+ yrs, ex-SVP2 Business Intelligence Unit, Axis Bank
27. Arindam Sarkar — Head, Treasury — 25+ yrs, ex-Head Interest Rates/Corporate Bonds/Equity Trading, Axis Bank
28. Nand Kumar Singh — Head, Credit Administration & Asset Operations — 34+ yrs, ex-Retail Banking Head Patna Circle, Axis Bank
29. Indranil Banerjee — Company Secretary — 27+ yrs, ex-Company Secretary, Energy Development Company
30. Siddhartha Sanyal — Chief Economist & Head Research — 26+ yrs, ex-Director & Chief India Economist, Barclays Bank PLC
31. Sujoy Roy — National Head, Collections (Designate) — 27+ yrs, ex-Cluster Head (Kolkata Central), Axis Bank
32. Ravindra Baburaya Gadiyar — Head, Commercial & Retail Credit — 26+ yrs, ex-National Credit Head-SEG (Credit), Axis Bank
33. Prakash E — Chief of Internal Vigilance (Interim) — 26+ yrs, ex-AGM, Chemplast Sanmar
34. Sandip Kumar Bubna — Chief Audit Executive (Interim) — 16+ yrs, ex-Senior Audit Manager-IS Audit, ICICI Bank

Total distinct profiles across slides 42-45 = 34 rows (13 board + 21 management, note Sengupta/Babbar/Kesh appear twice — once as Board, once as Core Management — both instances rowed above per instruction to enumerate every occurrence).

---
## TABLE 5 — FORWARD-GUIDANCE SCAN (special call-out per task brief)

Grep sweep for guidance/aspiration/target/outlook/exit-rate/medium-term language across the full extract found **no dedicated forward-guidance slide** in this deck: no ROA-aspiration statement, no NIM-path statement, no credit-cost guidance, no stated growth guidance, no opex-to-asset guidance. All Q1FY27-vintage language is historical/current-quarter (trailing NII, PAT, ROA, NIM, credit cost, opex/assets — see slides 6, 21, 28, 29, 31, 32) or product-feature marketing copy (slides 36-40). The only forward-looking text in the whole deck is the boilerplate risk-factor disclaimer on slide 3 (generic forward-looking-statement disclosure, not company guidance).
**Flag: NO_FORWARD_GUIDANCE_SLIDE** — this deck carries none of the guidance categories the task brief asked to watch for; A3/A4 should treat any FY28 ROA/NIM/credit-cost guidance as sourced from the concall transcript only, not this presentation, and should test whether the absence itself is a disclosure signal (prior-quarter decks may be checked for comparison once a prior-ledger path is supplied).

---
## TABLE 6 — CONCALL CROSS-REFERENCE (asset-quality slides named in task brief)

| Task brief label | Deck footer # | Extract page (`[page N]`) | Title | Status |
|---|---|---|---|---|
| "slide 22 (collection efficiency)" | 22 | page 23 | EEB Collection Efficiency | present, enumerated (Table 2 §17, Table 3 rows 66-73) |
| "slide 23 (SMA/DPD buckets)" | 23 | page 24 | EEB DPD movement | present, enumerated (Table 2 §18) — regional split flagged DPD_REGIONAL_SPLIT_OCR_DEGRADED |
| "slide 24 (vintage/bounce chart)" | 24 | page 25 | EEB - Stress Pool and Vintage Analysis | present, enumerated (Table 2 §19, Table 3 rows 16-24) — vintage chart flagged CHART_OCR_DEGRADED |

Note: the deck's own printed footer numbers run one behind the PDF/extract page markers (footer N = extract page N+1), because page 1 (cover letter) and page 2 (title slide) precede the footer-numbered sequence. This ledger uses extract `[page N]` as the slide number throughout Tables 1-2 and cross-references the footer number in Table 6 to reconcile with the task brief's numbering and with concall turn references A3/A4 will use.

---
## FLAGS SUMMARY

ZERO_STANDING (8): NPA Sale to ARC dashes; Technical Additions all-nil row; Provision for Standard Assets-Normal YoY flat; Additional Provision for Standard Assets YoY flat; EEB Stress-Pool PCR% dash; Balance Sheet Capital YoY flat; Credit Rating SR-Unrated Net Book Value NIL; "0 Branch Visits" feature claim (slide 38).

OCR/DATA-QUALITY (not gating, carried for A3/A4): MAP_DATA_OCR_DEGRADED (slide 7), OCR_DEGRADED (slide 8), OCR_UNCERTAIN_ORDER (slides 13, 15, 17), SOURCE_LABEL_ERROR (slide 13 disbursement column, slide 18 Average Deposits header), SOURCE_LABEL_INCONSISTENT (slide 16 CASA% base period), MISSING_DATA_LABEL (slide 21 GNPA Jun'26), OCR_DUPLICATE (slides 23, 24), DPD_REGIONAL_SPLIT_OCR_DEGRADED (slide 24), CHART_OCR_DEGRADED (slides 25, 26), UNCLEAR_METRIC_LABEL (slide 29 CRAR sub-series), OCR_AMBIGUOUS_MAPPING (slide 31 Opex/Assets).

PROCESS: PRIOR_LEDGER_UNAVAILABLE (no prior-quarter ledger supplied — DROPPED_SLIDE diff not performed). NO_FORWARD_GUIDANCE_SLIDE (Table 5).
