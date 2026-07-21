=== A2 COUNT TEST ===
category: slides            grep_count: 69   sweep_count: 69   match: yes
category: numbers           grep_count: 462  sweep_count: 462  match: yes
category: footnotes         grep_count: 58   sweep_count: 58   match: yes
category: dropped_slides    grep_count: N.A. sweep_count: N.A. match: N.A. (first quarterly run for INDIAMART; no prior-quarter ledger supplied to diff against)
gate_a2: pass
=== END COUNT TEST ===

Methodology notes (read before using this ledger):

- SLIDES: grep pass on `^\[page [0-9]+\]$` markers = 69, matching the A1 header's `page_count_pdfinfo: 69` and `formfeed_count: 69`. Manual page-by-page read confirms 69 distinct slides, none skipped, none merged.
- NUMBERS: enumeration unit = one row per content line (line number as recorded by A1) that carries at least one digit, EXCLUDING (a) the 14-line A1 extraction header, (b) the `[page N]` / `[OCR page N]` marker lines themselves, (c) 56 pure pagination-footer lines (a standalone 1-2 digit slide page-number sitting directly above the "IndiaMART InterMESH Ltd" footer — verified by checking the following 1-3 lines for that footer string AND value <=69), and (d) 7 `[CHART, page N, OCR text: none...]` annotation lines, which are A1's own OCR-verification metadata, not printed slide content. First grep pass using only "any digit-bearing line minus header/markers" returned 525; identifying and subtracting the 56 pagination-footer lines and 7 OCR-metadata lines (both verified against a second, independently-coded grep/python pass) brought the count to 462, which matches the manual page-by-page sweep performed while reading all 69 slides in full. This line-level unit was chosen because every row must carry a line number (Operating Rule 2); a single table row commonly bears several individual numbers (e.g. a 10-column FY21-FY26 + Q4/Q1 + CAGR row), so 462 "numeric lines" corresponds to several times that many individual numeric data points — no individual digit was dropped, all are visible in the Content column of the Numbers table below.
- FOOTNOTES: grep pass 1 (`^\s*[0-9]+\)\s` — numbered footnote markers) = 52. Manual sweep of all 69 slides for fine print NOT matching that pattern found 6 additional qualifying items the first grep pass missed: 4 unnumbered "Figures as on/of [date]" or "figures are approximations" captions (L646, L1663, L1695, L1812), 1 unnumbered asterisk unit-footnote "* Figures in Thousand" (L1021, qualifying the Paying Suppliers*/ARPU*/Top 10% ARPU* rows on the Operational Metrics table), and 1 full-page Safe Harbour disclaimer (page 4) whose closing line ("Unless otherwise stated, all amounts... rounded off to INR crore") qualifies every number in the entire deck. Re-running grep with a broadened pattern (`Figures as|approximations|^\s*\* |Safe Harbour`) recovers all 6 in addition to the 52, giving grep_count 58 = sweep_count 58. This is the GATE A2 re-sweep the operating rules require: the first grep pass under-counted; the manual sweep caught the miss; the grep was corrected to reconcile.
- ZERO_STANDING: one line item found holding zero across every period except the earliest one shown — see the Zero-Standing table below.
- DROPPED_SLIDE: not computable this quarter. No prior-quarter ledger path was supplied (first /run-quarterly cycle for INDIAMART). This category is marked N.A., not zero, so A3/A4 do not mistake "no prior deck" for "confirmed no drops."

---

## TABLE 1 — SLIDES (69 rows: number, title, content type, flags)

| Slide | Title (as printed) | Content Type | Line (title/start) | Notes / Flags |
|---|---|---|---|---|
| 1 | (untitled — Regulation 30 covering letter to BSE/NSE) | text (regulatory letter, digitally signed) | 15 | Signed by Vasudha Bagri, Compliance Officer, 2026.07.21 15:33:54; SIGNATURE_TIMESTAMP present |
| 2 | Make Doing Business Easy / Earnings Presentation, Quarter Ended June 30, 2026 | photo/cover (title slide) | 54 | |
| 3 | Table of Contents | text (index) | 69 | garbled OCR-adjacent artifact text at L74-75 ("HQIUGAHRL TI G" etc.) coexists with clean TOC entries; native extraction glitch, not a data figure |
| 4 | Safe Harbour | text (legal disclaimer, full page) | 92 | qualifies ALL numbers in the deck (rounding convention at L138); see footnote row 58 |
| 5 | Highlights Q1FY27 | photo (section divider) — OCR'd | 145 | OCR page 5; OCR confirms decorative-only, no incremental data |
| 6 | Q1 FY27 Results Overview (Consolidated) | text/stat blocks (KPI highlight boxes) | 170 | KPI_WATCH: headline consol Revenue/Collections/Deferred Rev/EBITDA/PAT/CFO |
| 7 | Q1 FY27 Results Overview (Standalone) | text/stat blocks | 194 | KPI_WATCH: headline standalone Revenue/Collections/Deferred Rev/EBITDA/PAT/CFO |
| 8 | Q1 FY27 Operational Performance (Standalone) | text/stat blocks | 218 | KPI_WATCH: Paying Suppliers 0% YoY flat, footnote "1,852 paying suppliers declined this quarter" — net supplier attrition disclosed in fine print, not headline |
| 9 | Q1 FY27 Results Overview (Busy) | text/stat blocks | 241 | KPI_WATCH: Busy Infotech Revenue/Billing/Deferred Rev/EBITDA/PAT/CFO; no YoY% shown for EBITDA/PAT/CFO (unlike other blocks) |
| 10 | IndiaMART Business Overview | photo (section divider) — OCR'd | 262 | OCR page 10; decorative-only |
| 11 | Traditional Marketplace to Online Marketplace | diagram | 288 | no numeric data |
| 12 | India's Largest Online B2B Marketplace | diagram | 321 | no numeric data |
| 13 | Services that Empower Businesses | diagram (two-column feature list) | 343 | no numeric data |
| 14 | Well Diversified Across ~98000 Categories | table (24-category % breakdown grid) | 375 | 24 category % values + "57 Industries / 132 Mn Products" callout; footnote basis date June 30, 2026 |
| 15 | End-To-End Value Chain Discovery – Plastic Recycling Machine | photo/diagram | 410 | no numeric data |
| 16 | Well Diversified Across Geographies | chart (donut/pie %) + text | 438 | Buyer% and Supplier% by Metro/Tier II/Rest of India; footnoted basis dates differ (5-yr buyer window vs March 31, 2026 supplier count vs 2011 census population) |
| 17 | 2-way Discovery Marketplace | diagram | 472 | no numeric data |
| 18 | CRM – Lead Manager & Conversational Commerce | diagram/photo | 507 | "~146 mn Replies & Callbacks" headline + "4.0" rating |
| 19 | How RFQ / BuyLead Works | diagram | 539 | no numeric data |
| 20 | Behavioral Data Driven Algorithmic Matchmaking | diagram | 555 | no numeric data |
| 21 | Leveraging AI: Enhancing User Experience | diagram | 580 | no numeric data |
| 22 | Key Competitive Strengths – Brand & Network Effect | text/stat list | 624 | KPI_WATCH: 58% Repeat Buyers, 38% Suppliers-are-Buyers, 4.8 Play Store rating, 26 Mn UBE, 146 Mn Replies, 132 Mn Listed Products, 8.8 Mn Suppliers, 218K Paying Suppliers; mixed basis dates (Q1FY27 figures vs "as of June 30, 2026" vs 90-day calc) |
| 23 | Trusted Ecosystem | diagram | 652 | no numeric data |
| 24 | ROI-driven, Subscription Based Revenue Model & RFQ Quota | table + diagram | 672 | KPI_WATCH: Top 1%/Top 10%/Total paying-supplier ARPU tiering (Top 10% ARPU is a named monitoring KPI) |
| 25 | Enterprise Solutions – Partnering Across a Wide Spectrum | photo (logos) | 700 | no numeric data (trademark disclaimer only) |
| 26 | Constant Innovation & Technology Focus | diagram (timeline, years 2009-2025) | 710 | years are data (product-launch timeline), no metrics |
| 27 | Strategic Outlook | diagram | 735 | no numeric data |
| 28 | Journey Towards Commerce & Business Enablement | diagram | 761 | no numeric data |
| 29 | Accounting - Strategic Fit for IndiaMART | diagram + stat | 793 | "~Rs. 730 crores invested in Accounting space" |
| 30 | Investments in Accounting | diagram/chart (% holdings) | 826 | ~1Mn / ~6Mn(Tally) business counts + 100%*/26%*/28.6%* holding percentages (asterisk = IndiaMART Holding, footnoted) |
| 31 | Other Strategic Investments | diagram (% holdings) | 868 | 11 strategic investment % holdings (22.2% to 34.5%) |
| 32 | Investment Portfolio | table (13-row investee list) | 898 | 2 subsidiaries + 11 strategic investments, each with Total Investment (Cr, at cost) and Shareholding %; sums to Busy 509 + Livekeeping 103 subsidiary investment |
| 33 | Operational Performance (Standalone) | photo (section divider) — NOT OCR'd | 981 | divider page not in the 7-page OCR list; native pdftotext text appears clean/complete regardless |
| 34 | Operational Metrics | table (10-row operational KPI table, FY21-FY26 + Q4FY26 + Q1FY27 + 5yr/3yr CAGR) | 994 | KPI_WATCH: Active Buyers LTM -5% YoY, Unique Business Enquiries -11% YoY, Business Enquiries Delivered -13% YoY, Paying Suppliers 0% YoY, Employees -4% YoY — five of ten rows show YoY decline or flat; Top 10% ARPU +10% YoY is the standout positive |
| 35 | Paying Suppliers | chart (yearly + quarterly trend, net additions) | 1025 | KPI_WATCH: quarterly net addition/reduction bridge shows -1/-2 net reduction in most recent quarters; footnote flags a 1.2K one-time onboarding-driven benefit in Q2FY26 that inflates the comparable base |
| 36 | Financial Performance — Consolidated Section | photo (section divider) — OCR'd | 1059 | OCR page 36; decorative-only |
| 37 | Financial Performance – Consolidated | table (P&L, FY21-FY26 + Q4FY26/Q1FY27 + CAGR) | 1087 | KPI_WATCH: EBITDA Margin 35% (Q1FY27) vs 33% (Q4FY26); Collections 8% YoY; CFO 2% YoY (well below EBITDA/PAT growth — cash conversion divergence) |
| 38 | Abridged Balance Sheet - Consolidated | table (FY21-FY26 + Q4FY26/Q1FY27) | 1116 | Goodwill dash-valued FY21-FY22 then flat at 454 FY23 onward (one-time step, not a standing-zero pattern); Deferred Revenue growth line |
| 39 | Cash Generation & Utilization | table (cash-flow bridge, FY21-FY26 + Q1FY27) | 1154 | ZERO_STANDING: "(i) Proceeds from issue of shares" row = 0 in every period FY22 through Q1FY27 (only the FY21 IPO-year value of 1,052 is non-zero) — see Table 3 below |
| 40 | Collections from Customer - Consolidated | chart (17-quarter trend, Q1FY23-Q1FY27) | 1183 | footnote: Q4 seasonally strongest collections quarter |
| 41 | Legal Entity View | table (Revenue/EBITDA split: IndiaMART / Busy Infotech / Others) | 1213 | KPI_WATCH: Busy Infotech Revenue +47% YoY, EBITDA only 3 Cr vs 6 Cr Q4FY26 (down QoQ); "Others" EBITDA negative every period shown (5, -11, -7, -6) |
| 42 | Financial Performance — Standalone Basis | photo (section divider) — OCR'd | 1247 | OCR page 42; decorative-only |
| 43 | Financial Performance – Standalone | table (P&L, FY21-FY26 + Q4FY26/Q1FY27 + CAGR, incl. Adjusted EBITDA) | 1272 | KPI_WATCH: standalone EBITDA Margin 40% (Q1FY27) vs 37% Q4FY26; Adjusted EBITDA Margin 41%; CFO % of Collections 38%, down from 53% Q4FY26 |
| 44 | Abridged Balance Sheet - Standalone | table (FY21-FY26 + Q4FY26/Q1FY27) | 1301 | mirrors consol structure minus Goodwill line (standalone has no goodwill line item — absence itself is notable vs consol) |
| 45 | Deferred Revenue - Standalone | chart (yearly + quarterly trend + current-portion %) | 1337 | KPI_WATCH (named monitoring KPI): Deferred Revenue 1,858 Cr, 14% YoY; current-portion (12mo) ~60-64% across periods; footnote: ~20% recognized within next 3 months |
| 46 | Revenue from Operations - Standalone | chart (yearly + quarterly trend + % from opening deferred revenue) | 1372 | % of revenue recognized from opening deferred revenue rising 88%→91% |
| 47 | Functional P&L - Standalone | table (Gross Profit/S&M/Tech&Content/G&A/EBITDA/Op Profit bridge, FY21-FY26 + Q4FY26/Q1FY27 + CAGR) | 1405 | footnote references Note 31 of Standalone Financial Statements (cross-document pointer for A3/A4) |
| 48 | Busy Infotech & Livekeeping Technologies | photo (section divider) — NOT OCR'd | 1444 | divider page not in the 7-page OCR list |
| 49 | Busy – Business Accounting Software | diagram + stat | 1457 | "IndiaMART Investment: Rs. 509 Crore, Holding: 100%" |
| 50 | License Sold | chart (yearly + quarterly, incl. new-license-sold overlay, figures in thousand) | 1494 | |
| 51 | Billing | chart (yearly + quarterly, Rs Crore) | 1523 | |
| 52 | Financial Performance (Busy Infotech) | table (Revenue/Total Revenue/Manpower/Other Exp/Total Exp/EBITDA/PAT/Billing/CFO/Deferred Rev, FY22-FY26 + Q4FY26/Q1FY27) | 1555 | KPI_WATCH: Busy Infotech EBITDA Margin fell to 9% (Q1FY27) from 16% (Q4FY26); Net Profit Margin rose to 15% from 9% — margin divergence between EBITDA and PAT lines worth flagging for A3/A4 |
| 53 | Livekeeping – Tally on Mobile & Web | diagram + stat | 1582 | "IndiaMART Investment: Rs. 103 Crore, Holding: 100%" |
| 54 | Environment, Social and Governance | photo (section divider) — OCR'd | 1613 | OCR page 54; decorative-only |
| 55 | Environment, Social and Governance | text/icons with stats | 1639 | ~48% Buyers from Small Cities, 0.03 TCO2e/Mn Turnover, 8.5Mn served free of charge; figures as on March 31, 2026 (i.e., stale vs quarter-end June 30, 2026) |
| 56 | Community Improvement – Education and Infrastructure | text/stats | 1667 | 1.8 Million+ lives impacted; figures as on March 31, 2026 |
| 57 | Nurturing People | text/stats | 1699 | 15% employees with 5+ years, ~28% females (ex sales/servicing), 700+ ESOP-covered employees; mixed basis dates |
| 58 | Independent Director(s) | text (5 director profiles) | 1724 | 63% independent directors, 100% board meetings chaired by independent directors; DIN not stated on this slide (name/role/background only — DIN would be in the annexure of the results filing, not this presentation) |
| 59 | Shareholders and Team | photo (section divider) — OCR'd | 1761 | OCR page 59; decorative-only |
| 60 | Shareholding Pattern | chart (pie %, 4 buckets) + table (5 named institutional holders >1%) | 1788 | Total Equity Shares Outstanding 6,01,43,148 as on June 30, 2026; footnote "figures are approximations"; named holders (Nalanda India, ICICI Prudential MF, UTI MF, Vanguard Group, iShares Core MSCI) shown WITHOUT individual % holding disclosed on-slide |
| 61 | Leadership Team | photo/text (8 leadership profiles) | 1816 | no numeric data beyond implicit tenure/education; CFO Jitin Diwan listed |
| 62 | APPENDIX | photo (section divider) — OCR'd | 1844 | OCR page 62; decorative-only |
| 63 | Collections from Customer - Consolidated (appendix repeat) | chart (17-quarter trend) | 1862 | duplicate of slide 40's data set (consol collections), appendix restates it |
| 64 | Cash Flow From Operations - Consolidated | chart (yearly + quarterly + % of Collections) | 1894 | % of Collections 35% Q1FY27 vs 49% Q4FY26 (seasonal, footnoted) |
| 65 | Collections from Customer – Standalone | chart (17-quarter trend) | 1925 | |
| 66 | Cash Flow From Operations - Standalone | chart (yearly + quarterly + % of Collections) | 1956 | % of Collections 38% Q1FY27 vs 53% Q4FY26 |
| 67 | EBITDA - Standalone | chart (yearly + quarterly + margin %) | 1987 | |
| 68 | Unique Business Enquiries | chart (yearly + quarterly, figures in millions) | 2018 | KPI_WATCH (named monitoring KPI): -11% YoY quarterly, only decline among the appendix repeat-charts; footnote defines "unique buyer" methodology |
| 69 | Thank You (closing / contact slide) | text | 2047 | investors@indiamart.com; no numeric data |

---

## TABLE 2 — DROPPED_SLIDE (vs prior quarter)

N.A. — no prior-quarter ledger path supplied for this ticker's first `/run-quarterly` cycle. A3/A4 should NOT infer "no slides dropped"; this comparison is simply unavailable this run. Re-run this category at the next quarterly cycle once a Q2 FY27 deck and this ledger exist as the prior-quarter baseline.

---

## TABLE 3 — ZERO_STANDING LINE ITEMS

| # | Slide | Line | Line item | Values across periods shown | Flag |
|---|---|---|---|---|---|
| 1 | 39 | 1166 | (i) Proceeds from issue of shares (footnote 4: "Includes proceeds from issue of equity shares on exercise of ESOPs & qualified institutions placement") | FY21: 1,052 · FY22: 0 · FY23: 0 · FY24: 0 · FY25: 0 · FY26: 0 · Q1FY27: 0 | ZERO_STANDING — the line has printed zero in every one of the six most recent periods (FY22 through Q1FY27); the sole non-zero value (FY21, the IPO year) is now five-plus years stale. The row is retained in the deck as a standing template line (per the SOUTHWEST convention: the line exists because a transaction of that type happened once and is being tracked in case it recurs — e.g., a future QIP or ESOP-driven issuance). Do not drop this row from monitoring: any future non-zero print here (QIP, share issuance) is a capital-structure event A4 should catch on first appearance. |

No other line item across the 10 financial/operational tables in this deck (pages 34, 37, 38, 39, 41, 43, 44, 47, 52) prints zero/nil/dash across ALL periods shown. Individual zero or dash cells DO occur elsewhere (e.g., Goodwill dash-valued FY21-FY22 on the consolidated balance sheet before stepping to 454 from FY23 onward; scattered "0" cells in the Q1FY27 column of the Cash Generation & Utilization table for Capital expenditure, Strategic Investments, and Capital distributed to Shareholders) but these are single-period zeros within an otherwise populated series, not standing-zero rows, and are captured in the Numbers table (Table 4) rather than flagged separately here.

---

## TABLE 4 — NUMBERS ON EVERY SLIDE (462 rows; grep_count = sweep_count = 462, see Count Test methodology above)

Each row = one content line (as extracted by A1, line number preserved) carrying numeric data, in slide order. Internal whitespace has been collapsed to single spaces for readability; no characters were removed. Superscript footnote-reference digits that print on their own extraction line inside a table (e.g. a lone "1", "2", "3", "4" beside a column header) are retained here as their own row because they are a distinct number on the slide, and are cross-referenced to their footnote text in Table 5.

| Slide | Line | Content (numeric data on slide) |
|---|---|---|
| 1 | 16 | July 21, 2026 |
| 1 | 20 | (BSE: 542726) (NSE: INDIAMART) |
| 1 | 26 | Results of the Company for the quarter ended June 30, 2026 |
| 1 | 30 | Pursuant to Regulation 30 of SEBI (Listing Obligations and Disclosure Requirements) Regulations, |
| 1 | 31 | 2015, please find enclosed herewith Investor Presentation on Audited Consolidated and |
| 1 | 32 | Standalone Financial Results of the Company for the quarter ended June 30, 2026. |
| 1 | 45 | Bagri Date: 2026.07.21 |
| 1 | 46 | 15:33:54 +05'30' |
| 1 | 50 | Membership No: A28500 |
| 2 | 59 | JUNE 30, 2026 |
| 2 | 61 | India's largest online B2B marketplace |
| 3 | 74 | ERH THSI G– HQL4I G&H TF SY 2–4 Q |
| 3 | 75 | - 215 F Y 2 7 4 |
| 3 | 77 | INDIAMART BUSINESS OVERVIEW 9 |
| 3 | 79 | S TA N D A L O N E O P E R AT I O N A L P E R F O R M A N C E 32 |
| 3 | 81 | FINANCIAL PERFORMANCE 35 |
| 3 | 83 | BUSY INFOTECH & LIVEKEEPING TECHNOLOGIES 47 |
| 3 | 84 | ESG 53 |
| 3 | 85 | APPENDIX 61 |
| 4 | 107 | This presentation is not a prospectus, a statement in lieu of a prospectus, an offering circular, an advertisement or an offer document under the Companies Act, 2013, and the rules made |
| 4 | 108 | thereunder, as amended, the Securities and Exchange Board of India ( Issue of Capital and Disclosure Requirements) Regulations, 2018, as amended, or any other applicable law in India. |
| 4 | 132 | The securities of the Company have not been and will not be registered under the U.S. Securities Act of 1933 (as amended, the "U.S. Securities Act") or any state securities laws in the |
| 4 | 135 | confirm that you are either (i) both a "qualified institutional buyer" as defined in Rule 144A under the U.S. Securities Act and a "qualified purchaser" as defined under the U.S. Investment |
| 4 | 136 | Company Act of 1940 in reliance upon section 3(c)(7) of the U.S. Investment Company Act of 1940, or (ii) a non-U.S. Person outside the United States. By receiving this presentation, you |
| 5 | 152 | Q1FY27 |
| 5 | 161 | QIFY27 (OCR rendering of "Q1FY27") |
| 6 | 171 | Q1 FY27 Results Overview (Consolidated) |
| 6 | 176 | 414 Cr 463 Cr 2,014 Cr (Revenue / Collections / Deferred Revenue) |
| 6 | 177 | 11% YoY 8% YoY 16% YoY |
| 6 | 184 | 146 Cr 172 Cr 163 Cr (EBITDA / Net Profit / CFO) |
| 6 | 185 | 35% Margin 33% Margin 35% of Collections |
| 6 | 186 | 10% YoY 12% YoY 2% YoY |
| 7 | 195 | Q1 FY27 Results Overview (Standalone) |
| 7 | 200 | 376 Cr 402 Cr 1,858 Cr (Revenue / Collections / Deferred Revenue) |
| 7 | 201 | 9% YoY 8% YoY 14% YoY |
| 7 | 208 | 149 Cr 176 Cr 153 Cr (EBITDA / Net Profit / CFO) |
| 7 | 209 | 40% Margin 38% Margin 38% of Collections |
| 7 | 210 | 11% YoY 6% YoY 6% YoY |
| 8 | 219 | Q1 FY27 Operational Performance (Standalone) |
| 8 | 222 | Paying Suppliers / Indian Supplier Storefronts / Active Buyers1 (headers) |
| 8 | 224 | 218 K 8.8 Mn 41 Mn |
| 8 | 225 | 0% YoY 5% YoY 5% YoY |
| 8 | 231 | ₹ 69 K 132 Mn 26 Mn (ARPU / Live Product Listings / Unique Business Enquiries) |
| 8 | 232 | 9% YoY 8% YoY 11% YoY |
| 8 | 235 | 1,852 paying suppliers declined this quarter |
| 8 | 237 | footnote marker "1) Last 12 Months" |
| 9 | 242 | Q1 FY27 Results Overview (Busy) |
| 9 | 248 | 36 Cr 59 Cr 146 Cr (Revenue / Billing / Deferred Revenue & Advances) |
| 9 | 249 | 47% YoY 10% YoY 44% YoY |
| 9 | 256 | 3 Cr 6 Cr 16 Cr (EBITDA / Net Profit / CFO — no YoY% shown) |
| 10 | 276 | "22" fragment in OCR-decorative text ("22 aE -_ =_") — not a data value |
| 12 | 322 | India's Largest Online B2B Marketplace (title, no metric) |
| 12 | 327 | "2-way" (label, not a metric) |
| 14 | 376 | Well Diversified Across ~98000 Categories |
| 14 | 382 | 8% 7% 6% 5% 5% 5% 5% 4% (row 1 of 3, categories 1-8) |
| 14 | 391 | 4% 3% 3% 3% 2% 2% 2% 2% (row 2 of 3, categories 9-16) |
| 14 | 400 | 2% 2% 2% 2% 2% 2% 2% 1% (row 3 of 3, categories 17-24) |
| 14 | 404 | footnote marker "1) % above are for total paying supplier," |
| 14 | 405 | "as on June 30, 2026" (footnote continuation) |
| 14 | 406 | 57 Industries 132 Mn Products |
| 16 | 441 | Buyers1 % / Paying Suppliers % / Metro Cities (8) (headers) |
| 16 | 448 | Tier II Cities (69) |
| 16 | 449 | Cities 52% (Metro Cities Paying-Supplier %) |
| 16 | 450 | Metro 24% (Tier II Cities Buyer %) Population > 500,000, excluding the cities |
| 16 | 452 | 29% (Metro Cities Buyer %) |
| 16 | 454 | (~4,000) (Rest of India town count) |
| 16 | 456 | Population <500,000 |
| 16 | 459 | Rest of India 30% (Rest of India Paying-Supplier %) |
| 16 | 460 | India 17% (Rest of India Buyer %) |
| 16 | 461 | 48% (Rest of India Buyer % cont.) ~ 5,400 Sales & Servicing team |
| 16 | 463 | ~100 Channel Sales Partner Locations |
| 16 | 466 | footnote marker "1) Basis aggregate buyers who have submitted enquiries during the last 5 years" |
| 16 | 467 | footnote marker "2) Figures as on March 31, 2026" |
| 16 | 468 | footnote marker "3) Population as per 2011 census" |
| 16 | 469 | "15 15" (page-number duplication artifact / slide footer number printed twice) |
| 17 | 473 | 2-way Discovery Marketplace (title, no metric) |
| 18 | 509 | ~146 mn Replies1 & Callbacks2 during Q1 FY27 |
| 18 | 514 | 4.0 (Play Store / app rating shown on this slide's Reviews & Ratings icon) |
| 18 | 532 | footnote marker "1) Total Replies via desktop, Mobile site, Email & App" |
| 18 | 535 | footnote marker "2) Total Callbacks via Mobile site & App" |
| 22 | 628 | 58% Repeat Buyers2 / 26 Mn Unique Business Enquiries1 |
| 22 | 629 | 38% Suppliers are Buyers / 146 Mn Replies & Callbacks1 |
| 22 | 630 | 4.8 Play Store Rating / RFQ selection |
| 22 | 641 | 132 Mn Listed Products / 8.8 Mn Suppliers |
| 22 | 642 | 218K Paying Suppliers |
| 22 | 646 | "Figures as of June 30, 2026" (unnumbered caption — see Table 5, footnote 53) |
| 22 | 647 | footnote marker "1) Figures for Q1 FY27" |
| 22 | 648 | footnote marker "2) Calculated for 90 days" |
| 24 | 675 | Paying suppliers / ARPU1 (Rs.) / % of Revenue (headers) |
| 24 | 679 | Top 1% ~2K 1,135K 16% |
| 24 | 681 | Top 10% ~22K 349K 51% |
| 24 | 682 | 218K 69K 100% |
| 24 | 695 | footnote marker "1) ARPU represents Revenue from operations..." |
| 24 | 696 | footnote marker "2) RFQ Quota:- Silver Monthly: Daily 1 Weekly 7..." |
| 25 | 706 | footnote marker "1) All trademarks, logos & brand names..." (no numeric data on slide body) |
| 26 | 713 | 2009 2013 2022 2024 (timeline years) |
| 26 | 714 | 2018 (timeline year) |
| 26 | 722 | 2010 2015 2019 2023 2025 (timeline years) |
| 29 | 816 | ~ Rs. 730 crores invested in Accounting space |
| 30 | 829 | ~ 1 Mn businesses ~ 6 Mn1 businesses on Tally |
| 30 | 837 | 100%* (IndiaMART Holding, Large enterprise tier) |
| 30 | 843 | 26%* (Medium enterprise tier) |
| 30 | 849 | 100%* (Cloud service tier) |
| 30 | 851 | 28.6%* (Small enterprise tier) |
| 30 | 863 | footnote marker "1) Source Media reports" |
| 30 | 864 | footnote marker "2) All trademarks... *IndiaMART Holding" |
| 31 | 879 | 22.2% 10.3% 32.5% 9.6% 18.7% 34.5% (6 strategic investment % holdings, row 1) |
| 31 | 889 | 23.2% 26% 10% 14.2% 13.1% (5 strategic investment % holdings, row 2) |
| 32 | 900 | Total Investment1 (in Crore) / Shareholding Aggregate (%) (headers) |
| 32 | 904 | 1 Busy Infotech 509 100.0% |
| 32 | 905 | 2 Livekeeping Technologies 103 100.0% |
| 32 | 913 | 1 Fleetx Technologies 161 22.2% |
| 32 | 914 | 2 IB MonotaRO 118 18.7% |
| 32 | 915 | 3 Baldor Technologies 113 10.3% |
| 32 | 916 | 4 Simply Vyapar Apps 108 28.6% |
| 32 | 922 | 5 Mobisy Technologies (row number, company name only on this line) |
| 32 | 923 | 72 32.5% (Mobisy Technologies investment/holding, continued from L922) |
| 32 | 929 | 6 Mynd Solutions 53 9.6% |
| 32 | 935 | 7 Truckhall 38 34.5% |
| 32 | 946 | 8 Agillos E-Commerce 26 23.2% |
| 32 | 959 | 9 Edgewise Technologies 18 26.0% |
| 32 | 965 | 10 Zimyo Consulting 17 10.0% |
| 32 | 966 | 11 Adansa Solutions 14 26.0% |
| 32 | 967 | 12 Legistify Services 9 14.2% |
| 32 | 975 | 13 Instant Procurement Services 1 13.1% |
| 32 | 977 | footnote marker "1) At Cost" |
| 34 | 998 | Q4FY26 Q1FY27 YoY / FY21 FY22 FY23 FY24 FY25 FY26 (table column headers) |
| 34 | 999 | 5 Year 3 Year (CAGR column headers) |
| 34 | 1000 | 230 234 9% Registered Buyers 125 149 170 194 211 230 13% 10% |
| 34 | 1002 | 41 41 (5%) Active Buyers - Last 12 Months 35 38 37 39 43 41 3% 4% |
| 34 | 1004 | 27 26 (11%) Unique Business Enquiries 96 97 88 93 106 114 4% 9% |
| 34 | 1006 | 86 85 (13%) Business Enquiries Delivered 610 550 479 520 458 370 (10%) (8%) |
| 34 | 1008 | 8.7 8.8 5% Indian Supplier Storefronts 6.5 7.1 7.5 7.9 8.4 8.7 6% 5% |
| 34 | 1010 | 129 132 8% Live Product Listings 72 83 95 108 119 129 12% 11% |
| 34 | 1012 | 220 218 0% Paying Suppliers* 152 169 203 214 217 220 8% 3% |
| 34 | 1014 | 67 69 9% ARPU* 44 44 46 53 61 66 9% 12% |
| 34 | 1016 | 333 349 10% Top 10% ARPU* 181 194 214 247 289 321 12% 15% |
| 34 | 1018 | 6,222 6,066 (4%) Employees (Nos) 2,701 3,672 4,583 5,384 6,102 6,222 18% 11% |
| 35 | 1031 | 8 (CAGR %, first digit — split across lines with "%" below) |
| 35 | 1032 | % 0% (CAGR "%" symbol + Quarterly YoY "0%") |
| 35 | 1036 | 214 217 220 222 (yearly bar chart values, part 1) |
| 35 | 1037 | 2 3 (net-addition data-labels) |
| 35 | 1038 | 203 12 1 |
| 35 | 1040 | 3 221 |
| 35 | 1041 | 220 218 |
| 35 | 1042 | 169 34 -1 |
| 35 | 1043 | 152 218 -1 -2 |
| 35 | 1044 | 5 17 1 |
| 35 | 1049 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 35 | 1052 | 44 44 46 53 61 66 ARPU 64 65 67 67 69 (ARPU overlay series) |
| 35 | 1055 | footnote marker "1) Excludes a one-time benefit of around 1.2K..." |
| 37 | 1092 | Q4FY26 Q1FY27 YoY / FY21-FY26 (column headers) |
| 37 | 1093 | 5 Year 3 Year (CAGR column headers) |
| 37 | 1094 | 404 414 11% Revenue from Operations 670 753 985 1,197 1,388 1,569 19% 17% |
| 37 | 1095 | (34) 107 15% Other Income1 87 112 181 211 272 204 |
| 37 | 1096 | 370 521 12% Total Income 756 866 1,166 1,407 1,661 1,773 19% 15% |
| 37 | 1097 | 178 174 8% Manpower Cost 205 268 425 544 601 693 28% 18% |
| 37 | 1098 | 94 94 Other Expenses2 136 178 293 321 265 346 |
| 37 | 1099 | 272 268 12% Total Expenses 341 446 718 865 866 1,039 25% 13% |
| 37 | 1100 | 133 146 10% EBITDA 328 308 268 331 523 530 10% 26% |
| 37 | 1101 | 33% 35% EBITDA Margin(%) 49% 41% 27% 28% 38% 34% |
| 37 | 1102 | 49 81 Others3 135 122 165 208 245 259 |
| 37 | 1103 | 50 172 12% Net Profit 280 298 284 334 551 475 11% 19% |
| 37 | 1104 | 14% 33% Net Profit Margin(%) 37% 34% 24% 24% 33% 27% |
| 37 | 1105 | 8 29 12% EPS4 (Rs.) 48 49 46 55 92 79 10% 19% |
| 37 | 1106 | 595 463 8% Collections from Customers 711 934 1,219 1,474 1,626 1,857 21% 15% |
| 37 | 1107 | 290 163 2% Cash flow from Operations 323 402 476 559 623 694 17% 13% |
| 37 | 1108 | 49% 35% % of Collections 45% 43% 39% 38% 38% 37% |
| 37 | 1109 | footnote marker "1) Includes fair value gains/(losses)..." |
| 37 | 1110 | footnote marker "2) Includes Outsourced Sales Cost..." |
| 37 | 1111 | footnote marker "3) Others include – Depreciation, Amortization..." |
| 37 | 1112 | footnote marker "4) EPS has been adjusted... bonus issuance in Q1FY24" |
| 38 | 1120 | Q4 FY26 Q1 FY27 / FY21-FY26 (column headers) |
| 38 | 1121 | "1" (superscript footnote-reference digit beside Fixed Assets row) |
| 38 | 1122 | 40 35 Fixed Assets 65 56 99 82 61 40 |
| 38 | 1124 | 454 454 Goodwill - - 454 454 454 454 |
| 38 | 1125 | "2" (superscript footnote-reference digit beside Other Assets row) |
| 38 | 1126 | 87 80 Other Assets 44 52 51 48 67 87 |
| 38 | 1128 | 3,280 3,553 Cash & Investments 2,365 2,419 2,335 2,340 2,886 3,280 |
| 38 | 1130 | 763 741 Strategic Investments 37 421 512 524 665 763 |
| 38 | 1132 | 4,625 4,862 Total Assets 2,511 2,949 3,445 3,449 4,134 4,625 |
| 38 | 1134 | 2,400 2,220 Capital & Reserves 1,611 1,874 2,059 1,736 2,185 2,400 |
| 38 | 1135 | "3" (superscript footnote-reference digit beside Deferred Revenue row) |
| 38 | 1136 | 1,965 2,014 Deferred Revenue 726 907 1,162 1,440 1,678 1,965 |
| 38 | 1138 | 67 100 Tax Liabilities 21 16 24 48 53 67 |
| 38 | 1140 | 23 22 Lease Liabilities 63 56 46 41 33 23 |
| 38 | 1141 | "4" (superscript footnote-reference digit beside Other Liabilities row) |
| 38 | 1142 | 169 507 Other Liabilities 90 96 154 184 185 169 |
| 38 | 1144 | 4,625 4,862 Total Liabilities 2,511 2,949 3,445 3,449 4,134 4,625 |
| 38 | 1147 | footnote marker "1) Includes fixed assets, intangible assets & right of use assets" |
| 38 | 1148 | footnote marker "2) Includes security deposits, recoverable from payment gateway..." |
| 38 | 1149 | footnote marker "3) Includes customer advances" |
| 38 | 1150 | footnote marker "4) Includes provisions & payables, statutory liabilities..." |
| 39 | 1158 | Particulars FY21-FY26 Q1FY27 (column headers) |
| 39 | 1159 | Opening Cash & Treasury Investments 931 2,365 2,419 2,335 2,340 2,886 3,280 |
| 39 | 1160 | Cash flow from operating activities 323 402 476 559 623 694 163 |
| 39 | 1161 | Cash flow from investing activities1 14 (273) (331) 32 (18) 10 16 |
| 39 | 1162 | (i) Non-Operating Income2 21 127 255 71 135 92 16 |
| 39 | 1163 | (ii) Capital expenditure3 3 (4) (16) (14) (8) (7) 0 |
| 39 | 1164 | (iii) Strategic Investments (10) (395) (570) (25) (144) (75) 0 |
| 39 | 1165 | Cash Flow from Financing Activities 1,038 (58) (143) (695) (148) (340) (3) |
| 39 | 1166 | (i) Proceeds from issue of shares4 1,052 0 0 0 0 0 0 — ZERO_STANDING (see Table 3) |
| 39 | 1167 | (ii) Other financing activities5 (12) (13) (13) (14) (28) (40) (3) |
| 39 | 1168 | (iii) Capital distributed to Shareholders6 (1) (46) (130) (681) (120) (300) 0 |
| 39 | 1169 | ∆ in Fair Value Gain on Treasury 60 (18) (85) 109 89 30 96 |
| 39 | 1171 | Closing Cash & Treasury Investments 2,365 2,419 2,335 2,340 2,886 3,280 3,553 |
| 39 | 1173 | ~₹1,650 Crore Capital Returned to Shareholders6 |
| 39 | 1174 | footnote marker "1) Adjusted for change in Investments, FDR..." |
| 39 | 1175 | footnote marker "2) Includes realized income from treasury investments..." |
| 39 | 1176 | footnote marker "3) Includes purchase & sale of property, plant and equipment..." |
| 39 | 1177 | footnote marker "4) Includes proceeds from issue of equity shares on exercise of ESOPs & QIP" |
| 39 | 1178 | footnote marker "5) Includes cash flow from repayment of lease liability..." |
| 39 | 1179 | footnote marker "6) Includes dividend paid & buyback inclusive of tax; ~1,650 Cr..." |
| 40 | 1190 | 595 (Q4FY23 quarterly collections bar) |
| 40 | 1191 | 541 |
| 40 | 1192 | 484 |
| 40 | 1193 | 463 |
| 40 | 1194 | 418 430 426 |
| 40 | 1195 | 406 |
| 40 | 1196 | 366 356 363 |
| 40 | 1197 | 321 337 332 |
| 40 | 1198 | 283 |
| 40 | 1199 | 254 264 |
| 40 | 1204 | Q1 FY23 through Q1 FY27 (17-quarter x-axis labels) |
| 40 | 1209 | footnote marker "1) Fourth Quarter of the year has traditionally been the best quarter..." |
| 41 | 1218 | Financial Metrics FY25 FY26 Q4FY26 Q1FY27 YoY (headers) |
| 41 | 1220 | Revenue from Operations 1,388 1,569 404 414 11% |
| 41 | 1222 | IndiaMART 1,320 1,443 368 376 9% |
| 41 | 1224 | Busy Infotech 66 119 34 36 47% |
| 41 | 1226 | Others1 2 7 2 3 |
| 41 | 1228 | EBITDA 523 530 133 146 10% |
| 41 | 1230 | IndiaMART 513 520 135 149 |
| 41 | 1232 | Busy Infotech 5 21 6 3 |
| 41 | 1234 | Others1 5 (11) (7) (6) |
| 41 | 1238 | ~90% of Revenue is contributed by IndiaMART standalone business |
| 41 | 1243 | footnote marker "1) Others include: Other Subsidiaries and Inter Company Adjustments" |
| 43 | 1276 | Q4FY26 Q1FY27 YoY / FY21-FY26 (column headers) |
| 43 | 1277 | 5 Year 3 Year (CAGR headers) |
| 43 | 1278 | 368 376 9% Revenue from Operations 665 751 939 1,139 1,320 1,443 17% 15% |
| 43 | 1279 | (34) 88 4% Other Income1 85 108 113 170 284 191 |
| 43 | 1280 | 334 464 8% Total Income 750 859 1,052 1,309 1,604 1,634 17% 16% |
| 43 | 1281 | 162 157 6% Manpower Cost 199 263 399 507 553 634 26% 17% |
| 43 | 1282 | 72 69 Other Expenses2 133 176 278 298 254 288 |
| 43 | 1283 | 234 227 7% Total Expenses 332 439 677 805 807 923 23% 11% |
| 43 | 1284 | 142 156 10% Adjusted EBITDA3 339 322 288 358 530 555 10% 24% |
| 43 | 1285 | 39% 41% Adjusted EBITDA Margin(%) 51% 43% 31% 31% 40% 38% |
| 43 | 1286 | 135 149 11% EBITDA 333 312 262 334 513 520 9% 26% |
| 43 | 1287 | 37% 40% EBITDA Margin(%) 50% 42% 28% 29% 39% 36% |
| 43 | 1288 | 31 61 Others4 132 110 102 141 190 186 |
| 43 | 1289 | 69 176 6% Net Profit 287 310 272 362 607 525 13% 24% |
| 43 | 1290 | 21% 38% Net Profit Margin(%) 38% 36% 26% 28% 38% 32% |
| 43 | 1291 | 546 402 8% Collections from Customers 707 932 1,167 1,399 1,526 1,674 19% 13% |
| 43 | 1292 | 287 153 6% Cash flow from Operations 326 407 464 545 614 668 15% 13% |
| 43 | 1293 | 53% 38% % of Collections 46% 44% 40% 39% 40% 40% |
| 43 | 1294 | footnote marker "1) Includes fair value gains/(losses)..." |
| 43 | 1295 | footnote marker "2) Includes Outsourced Sales Cost..." |
| 43 | 1296 | footnote marker "3) Excluding employee share-based payment expense" |
| 43 | 1297 | footnote marker "4) Others include – Depreciation, Amortization..." |
| 44 | 1305 | Q4FY26 Q1FY27 / FY21-FY26 (column headers) |
| 44 | 1306 | "1" (superscript footnote-reference digit beside Fixed Assets row) |
| 44 | 1307 | 21 19 Fixed Assets 65 56 53 48 33 21 |
| 44 | 1308 | "2" (superscript footnote-reference digit beside Other Assets row) |
| 44 | 1309 | 41 26 Other Assets 41 49 33 38 43 41 |
| 44 | 1311 | 3,066 3,316 Cash & Investments 2,359 2,414 2,202 2,186 2,720 3,066 |
| 44 | 1312 | "3" (superscript footnote-reference digit beside Strategic Investments row) |
| 44 | 1313 | 1,474 1,460 Strategic Investments 50 446 1,073 1,095 1,293 1,474 |
| 44 | 1315 | 4,602 4,822 Total Assets 2,516 2,965 3,361 3,367 4,090 4,602 |
| 44 | 1317 | 2,542 2,365 Capital & Reserves 1,617 1,892 2,064 1,770 2,276 2,542 |
| 44 | 1318 | "4" (superscript footnote-reference digit beside Deferred Revenue row) |
| 44 | 1319 | 1,832 1,858 Deferred Revenue 726 907 1,134 1,395 1,600 1,832 |
| 44 | 1321 | 53 85 Tax Liabilities 21 16 4 21 37 53 |
| 44 | 1323 | 23 22 Lease Liabilities 63 56 46 41 33 23 |
| 44 | 1324 | "5" (superscript footnote-reference digit beside Other Liabilities row) |
| 44 | 1325 | 152 492 Other Liabilities 89 94 113 140 143 152 |
| 44 | 1327 | 4,602 4,822 Total Liabilities 2,516 2,965 3,361 3,367 4,090 4,602 |
| 44 | 1329 | footnote marker "1) Includes fixed assets, intangible assets & right of use assets" |
| 44 | 1330 | footnote marker "2) Includes security deposits, recoverable from payment gateway..." |
| 44 | 1331 | footnote marker "3) Includes investment in subsidiaries & associates and others." |
| 44 | 1332 | footnote marker "4) Includes customer advances" |
| 44 | 1333 | footnote marker "5) Includes provisions and payables, statutory liabilities..." |
| 45 | 1343 | 20% 14% (CAGR / YoY headline) |
| 45 | 1347 | 1,832 1,832 1,858 |
| 45 | 1348 | 1,628 1,633 1,654 |
| 45 | 1349 | 1,600 |
| 45 | 1350 | 1,395 |
| 45 | 1352 | 1,134 |
| 45 | 1353 | 907 |
| 45 | 1354 | 726 |
| 45 | 1355 | 62% 60% (current-portion %, Q4/Q1 overlay) |
| 45 | 1356 | 62% 61% 62% 62% (current-portion %, Q1-Q4FY26 overlay) |
| 45 | 1357 | 64% 63% |
| 45 | 1358 | 63% |
| 45 | 1359 | 64% 63% |
| 45 | 1361 | Q1FY26-Q1FY27 (quarterly x-axis) |
| 45 | 1362 | FY21-FY26 (yearly x-axis) |
| 45 | 1364 | ~20% of deferred revenue gets recognized within next 3 months |
| 45 | 1366 | footnote marker "1) Deferred revenue refers to contract liabilities..." |
| 45 | 1367 | "Current Portion (12 Months)" (legend label) |
| 46 | 1378 | 17% 9% (CAGR / YoY headline) |
| 46 | 1380 | 1,443 |
| 46 | 1381 | 1,320 376 |
| 46 | 1382 | 360 368 368 |
| 46 | 1383 | 346 |
| 46 | 1384 | 1,139 |
| 46 | 1386 | 939 |
| 46 | 1388 | 751 |
| 46 | 1389 | 665 |
| 46 | 1391 | 89% 89% 91% (% of revenue recognized from opening deferred revenue) |
| 46 | 1392 | 88% 88% |
| 46 | 1397 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 47 | 1409 | Q4FY26 Q1FY27 YoY / FY21-FY26 (column headers) |
| 47 | 1410 | 5 Year 3 Year (CAGR headers) |
| 47 | 1411 | 368 376 9% Revenue from Operations 665 751 939 1,139 1,320 1,443 17% 15% |
| 47 | 1413 | (91) (85) 8% Customer service cost (122) (160) (237) (309) (303) (343) 23% 13% |
| 47 | 1414 | "1" (superscript footnote-reference digit beside Gross Profit row) |
| 47 | 1415 | 278 290 9% Gross Profit 543 591 702 830 1,017 1,100 15% 16% |
| 47 | 1417 | 75% 77% Gross Margin 82% 79% 75% 73% 77% 76% |
| 47 | 1419 | (59) (54) (1%) Selling & Marketing (82) (112) (189) (211) (181) (229) 23% 7% |
| 47 | 1421 | 16% 14% % of Revenue 12% 15% 20% 18% 14% 16% |
| 47 | 1423 | (57) (58) 11% Technology & Content (85) (111) (175) (199) (201) (226) 22% 9% |
| 47 | 1425 | 16% 15% % of Revenue 13% 15% 19% 17% 15% 16% |
| 47 | 1427 | (27) (29) 13% General & Administration (43) (56) (76) (87) (122) (125) 24% 18% |
| 47 | 1429 | 135 149 11% EBITDA 333 312 262 334 513 520 9% 26% |
| 47 | 1431 | 37% 40% EBITDA Margin 50% 42% 28% 29% 39% 36% |
| 47 | 1433 | (3) (3) (26%) Depreciation & Amortisation (16) (12) (19) (25) (21) (14) (3%) (10%) |
| 47 | 1435 | 131 147 12% Operating Profit 317 300 242 309 493 506 10% 28% |
| 47 | 1437 | 36% 39% Operating Margin 48% 40% 26% 27% 37% 35% |
| 47 | 1439 | footnote marker "1) Gross Profit means surplus over customer service cost" |
| 47 | 1440 | footnote marker "2) Refer to Note No. 31 in Standalone Financial Statements for Q1FY27..." |
| 49 | 1490 | IndiaMART Investment: Rs. 509 Crore, Holding: 100% |
| 50 | 1499 | 10% 11% (CAGR / YoY headline) |
| 50 | 1501 | 454 |
| 50 | 1502 | 442 12 |
| 50 | 1503 | 396 45 442 |
| 50 | 1504 | 364 33 431 11 |
| 50 | 1505 | 331 33 421 10 |
| 50 | 1506 | 30 12 |
| 50 | 1507 | 301 409 |
| 50 | 1508 | 278 23 |
| 50 | 1509 | 26 12 |
| 50 | 1514 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 51 | 1529 | 36% 10% (CAGR / YoY headline) |
| 51 | 1534 | 170 59 |
| 51 | 1535 | 53 |
| 51 | 1536 | 45 |
| 51 | 1537 | 38 |
| 51 | 1538 | 94 33 |
| 51 | 1540 | 70 |
| 51 | 1541 | 48 |
| 51 | 1542 | 37 42 |
| 51 | 1547 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 52 | 1559 | Q4FY26 Q1FY27 YoY / FY22-FY26 CAGR (column headers) |
| 52 | 1560 | 34 36 47% Revenue from Operations 35 43 54 66 119 35% |
| 52 | 1561 | 34 42 47% Total Revenue 38 47 62 76 128 35% |
| 52 | 1562 | 12 13 44% Manpower Expenses 18 22 31 39 42 24% |
| 52 | 1563 | 17 20 Other Expenses1 9 11 16 22 56 |
| 52 | 1564 | 29 33 64% Total Expenses 27 33 47 61 98 38% |
| 52 | 1565 | 5 3 EBITDA 9 10 7 5 21 24% |
| 52 | 1566 | 16% 9% EBITDA Margin(%) 25% 24% 13% 7% 17% |
| 52 | 1567 | 3 3 Others2 4 4 12 3 10 |
| 52 | 1568 | 3 6 Net Profit 8 10 3 12 20 25% |
| 52 | 1569 | 9% 15% Net Profit Margin(%) 21% 22% 5% 15% 16% |
| 52 | 1570 | 45 59 Billing 42 48 70 94 170 42% |
| 52 | 1571 | 10 16 Cash flow from Operations 10 21 24 23 49 49% |
| 52 | 1572 | 124 146 Deferred Revenue 22 27 44 72 124 54% |
| 52 | 1577 | footnote marker "1) Includes Marketing & Sales Promotion, and Other Operating Expense" |
| 52 | 1578 | footnote marker "2) Others include – Depreciation, Finance Cost & Tax Expense" |
| 53 | 1609 | IndiaMART Investment: Rs. 103 Crore, Holding: 100% |
| 54 | 1634 | "2" fragment in OCR-decorative text ("2 @") — not a data value |
| 55 | 1644 | 100% Free Assistance to Buyers |
| 55 | 1646 | ~48% Buyers from Small Cities |
| 55 | 1654 | Emissions of 0.03 TCO2e per Mn Turnover |
| 55 | 1656 | IGBC2 (footnote-marker superscript, not a value) LEED Gold; 8.5Mn served free of charge |
| 55 | 1663 | "Figures as on March 31, 2026" (unnumbered caption — see Table 5, footnote 55) |
| 56 | 1669 | 1.8 Million+ lives impacted |
| 56 | 1672 | 97,000+ Students / 1,50,000 Children |
| 56 | 1676 | 95 Social Welfare & 1500 Basic (Schools count) |
| 56 | 1678 | 1,500 ideas Received |
| 56 | 1684 | 26K + Students |
| 56 | 1685 | 1,200+ Students (Underprivileged, MM Hills) |
| 56 | 1690 | in 45+ Schools |
| 56 | 1695 | "Figures as on March 31, 2026" (unnumbered caption — see Table 5, footnote 56) |
| 57 | 1704 | 15% Employees (with 5+ years) |
| 57 | 1705 | with 5+ years |
| 57 | 1707 | 700+ employees |
| 57 | 1708 | covered in ESOP1 |
| 57 | 1713 | ~28% |
| 57 | 1714 | Females2 |
| 57 | 1718 | footnote marker "1) Employees covered under Indiamart Employee Stock Benefit Scheme 2015 and 2018..." |
| 57 | 1719 | footnote marker "2) Females working in verticals other than sales and servicing" |
| 57 | 1720 | footnote marker "3) Figures as on March 31, 2026" |
| 58 | 1757 | 63% Independent directors / 100% Board Meetings chaired by Independent directors |
| 60 | 1790 | 6,01,43,148 total equity shares outstanding is on the next line; "greater than 1%" threshold stated here |
| 60 | 1791 | on June 30, 2026 - 6,01,43,148 of the total number of shares |
| 60 | 1794 | 19% (shareholding bucket, likely Foreign Institutions/Portfolio Investors) |
| 60 | 1798 | 12% 49% UTI Mutual Fund (shareholding buckets: Mutual Funds/AIF/Insurance and Promoters) |
| 60 | 1802 | 20% (shareholding bucket, Others) |
| 63 | 1868 | 21% 8% (CAGR / YoY headline, consol collections appendix repeat) |
| 63 | 1872 | 595 |
| 63 | 1873 | 1,857 |
| 63 | 1874 | 1,626 |
| 63 | 1875 | 463 |
| 63 | 1876 | 1,474 430 426 |
| 63 | 1877 | 406 |
| 63 | 1878 | 1,219 |
| 63 | 1880 | 934 |
| 63 | 1881 | 711 |
| 63 | 1886 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 64 | 1902 | 290 |
| 64 | 1903 | 694 |
| 64 | 1904 | 623 |
| 64 | 1905 | 559 |
| 64 | 1906 | 476 |
| 64 | 1907 | 161 163 |
| 64 | 1908 | 402 |
| 64 | 1909 | 323 129 |
| 64 | 1910 | 114 |
| 64 | 1915 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 64 | 1918 | 45% 43% 39% 38% 38% 37% 37% 28% 30% 49% 35% (% of Collections series, all periods) |
| 64 | 1921 | footnote marker "1) Fourth Quarter of the financial year traditionally has high Cash flow from Operations..." |
| 65 | 1931 | 19% 8% (CAGR / YoY headline) |
| 65 | 1935 | 546 |
| 65 | 1936 | 1,674 |
| 65 | 1937 | 1,526 |
| 65 | 1938 | 1,399 |
| 65 | 1939 | 390 402 |
| 65 | 1940 | 1,167 374 365 |
| 65 | 1941 | 932 |
| 65 | 1943 | 707 |
| 65 | 1948 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 66 | 1962 | 15% 6% (CAGR / YoY headline) |
| 66 | 1966 | 287 |
| 66 | 1967 | 668 |
| 66 | 1968 | 614 |
| 66 | 1969 | 545 |
| 66 | 1970 | 464 |
| 66 | 1971 | 407 153 |
| 66 | 1972 | 144 |
| 66 | 1973 | 326 128 |
| 66 | 1974 | 109 |
| 66 | 1979 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 66 | 1981 | 46% 44% 40% 39% 40% 40% Collections 39% 30% 33% 53% 38% (% of Collections series, all periods) |
| 66 | 1983 | footnote marker "1) Fourth Quarter of the financial year traditionally has high Cash flow from Operations..." |
| 67 | 1993 | % 9 11% (CAGR "%9" fragment + Quarterly YoY 11%) |
| 67 | 1998 | 513 520 149 |
| 67 | 1999 | 135 136 135 |
| 67 | 2000 | 115 |
| 67 | 2001 | 333 334 |
| 67 | 2002 | 312 |
| 67 | 2003 | 262 |
| 67 | 2008 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 67 | 2011 | 50% 42% 28% 29% 39% 36% 39% 32% 37% 37% 40% (EBITDA Margins series, all periods) |
| 68 | 2024 | 4% (11)% (CAGR / YoY headline) |
| 68 | 2028 | 114 |
| 68 | 2029 | 106 |
| 68 | 2030 | 96 97 31 |
| 68 | 2031 | 93 |
| 68 | 2032 | 88 29 |
| 68 | 2033 | 28 27 |
| 68 | 2034 | 26 |
| 68 | 2039 | FY21-FY26 / Q1FY26-Q1FY27 (x-axis labels) |
| 68 | 2042 | footnote marker "1) Buyer posting an enquiry is one unique buyer for that day..." |

(462 rows total, verified against the Count Test above.)

---

## TABLE 5 — FOOTNOTES / FINE PRINT QUALIFYING HEADLINE NUMBERS (58 rows)

### 5A. Numbered footnotes (52 — grep pattern `^\s*[0-9]+\)\s`)

| # | Slide | Line | Footnote text |
|---|---|---|---|
| 1 | 8 | 237 | 1) Last 12 Months |
| 2 | 14 | 404 | 1) % above are for total paying supplier, as on June 30, 2026 |
| 3 | 16 | 466 | 1) Basis aggregate buyers who have submitted enquiries during the last 5 years |
| 4 | 16 | 467 | 2) Figures as on March 31, 2026 |
| 5 | 16 | 468 | 3) Population as per 2011 census |
| 6 | 18 | 532 | 1) Total Replies via desktop, Mobile site, Email & App |
| 7 | 18 | 535 | 2) Total Callbacks via Mobile site & App |
| 8 | 22 | 647 | 1) Figures for Q1 FY27 |
| 9 | 22 | 648 | 2) Calculated for 90 days |
| 10 | 24 | 695 | 1) ARPU represents Revenue from operations for the current quarter divided by Paying supplier at period end & the same has been multiplied by 4 to represent annualised run-rate |
| 11 | 24 | 696 | 2) RFQ Quota:- Silver Monthly: Daily - 1 Weekly - 7; Silver Annual/MYR: Daily - 1 Weekly - 10; Gold: Daily 1 to 2 Weekly 14 to 30; Platinum: Daily 1 to 4 Weekly 30 to 100 |
| 12 | 25 | 706 | 1) All trademarks, logos & brand names are the property of their respective owners |
| 13 | 30 | 863 | 1) Source Media reports |
| 14 | 30 | 864 | 2) All trademarks, logos & brand names are the property of their respective owners; *IndiaMART Holding |
| 15 | 32 | 977 | 1) At Cost |
| 16 | 35 | 1055 | 1) Excludes a one-time benefit of around 1.2K due to simplification of onboarding process for silver subscription packages. Total net additions for Q2FY26 are 4K — qualifies the Paying Suppliers net-add chart; directly relevant to interpreting the "0% YoY" flat print on slide 8/34 |
| 17 | 37 | 1109 | 1) Other Income includes fair value gains/(losses) from financial assets, interest income, dividend income, and other non-operating gains |
| 18 | 37 | 1110 | 2) Other Expenses includes Outsourced Sales Cost and Other Operating Expense |
| 19 | 37 | 1111 | 3) Others (below EBITDA) include Depreciation, Amortization, Finance Cost, Exceptional Item, Tax Expense & Associates Loss |
| 20 | 37 | 1112 | 4) EPS has been adjusted in all years & quarters to give effect of bonus issuance in Q1FY24 |
| 21 | 38 | 1147 | 1) Fixed Assets includes fixed assets, intangible assets & right of use assets |
| 22 | 38 | 1148 | 2) Other Assets includes security deposits, recoverable from payment gateway, prepaid expenses and remaining assets combined |
| 23 | 38 | 1149 | 3) Deferred Revenue includes customer advances |
| 24 | 38 | 1150 | 4) Other Liabilities includes provisions & payables, statutory liabilities & other financial liabilities |
| 25 | 39 | 1174 | 1) Adjusted for change in Investments, FDR, Inter corporate deposit & others during the period |
| 26 | 39 | 1175 | 2) Includes realized income from treasury investments & net investments in FDRs, Inter Corporate deposits & gain from sale of stake in associates and other investments |
| 27 | 39 | 1176 | 3) Includes purchase & sale of property, plant and equipment & other intangible assets & refundable security deposit for listing on stock exchange |
| 28 | 39 | 1177 | 4) Includes proceeds from issue of equity shares on exercise of ESOPs & qualified institutions placement — directly qualifies the ZERO_STANDING row (Table 3) |
| 29 | 39 | 1178 | 5) Includes cash flow from repayment of lease liability, interest expense & purchase of further shares in subsidiary |
| 30 | 39 | 1179 | 6) Includes dividend paid & buyback inclusive of tax; ~1,650 Cr Capital returned to shareholder includes dividend payout for FY26, concluded in July 2026 — reconciles the "~₹1,650 Crore Capital Returned" headline to the underlying dividend+buyback composition |
| 31 | 40 | 1209 | 1) Fourth Quarter of the year has traditionally been the best quarter in terms of collections from customer for that financial year |
| 32 | 41 | 1243 | 1) Others include: Other Subsidiaries and Inter Company Adjustments |
| 33 | 43 | 1294 | 1) Other Income includes fair value gains/(losses) from financial assets, interest income, dividend income, and other non-operating gains |
| 34 | 43 | 1295 | 2) Other Expenses includes Outsourced Sales Cost and Other Operating Expense |
| 35 | 43 | 1296 | 3) Adjusted EBITDA excludes employee share-based payment expense — qualifies the Adjusted EBITDA / Adjusted EBITDA Margin rows specifically (41% vs reported 40% EBITDA margin) |
| 36 | 43 | 1297 | 4) Others (below EBITDA) include Depreciation, Amortization, Finance Cost, Exceptional Item & Tax Expense |
| 37 | 44 | 1329 | 1) Fixed Assets includes fixed assets, intangible assets & right of use assets |
| 38 | 44 | 1330 | 2) Other Assets includes security deposits, recoverable from payment gateway, prepaid expenses and remaining assets combined |
| 39 | 44 | 1331 | 3) Strategic Investments includes investment in subsidiaries & associates and others |
| 40 | 44 | 1332 | 4) Deferred Revenue includes customer advances |
| 41 | 44 | 1333 | 5) Other Liabilities includes provisions and payables, statutory liabilities & other financial liabilities |
| 42 | 45 | 1366 | 1) Deferred revenue refers to contract liabilities in the financial statements including advances from customers |
| 43 | 47 | 1439 | 1) Gross Profit means surplus over customer service cost |
| 44 | 47 | 1440 | 2) Refer to Note No. 31 in Standalone Financial Statements for Q1FY27 for details on the basis of classification of function-wise results — CROSS-DOCUMENT POINTER: A3/A4 should reconcile this against the Standalone Financial Statements ledger's Note 31 when both are enumerated |
| 45 | 52 | 1577 | 1) Other Expenses (Busy Infotech) includes Marketing & Sales Promotion, and Other Operating Expense |
| 46 | 52 | 1578 | 2) Others (below EBITDA, Busy Infotech) include Depreciation, Finance Cost & Tax Expense |
| 47 | 57 | 1718 | 1) Employees covered under Indiamart Employee Stock Benefit Scheme 2015 and 2018 who vested stocks till date — qualifies "700+ employees covered in ESOP" |
| 48 | 57 | 1719 | 2) Females working in verticals other than sales and servicing — qualifies "~28% Females" (excludes the largest headcount function, materially affects interpretation of the ratio) |
| 49 | 57 | 1720 | 3) Figures as on March 31, 2026 |
| 50 | 64 | 1921 | 1) Fourth Quarter of the financial year traditionally has high Cash flow from Operations due to seasonal impact of Collections from Customers |
| 51 | 66 | 1983 | 1) Fourth Quarter of the financial year traditionally has high Cash flow from Operations due to seasonal impact of Collections from Customers (repeat of #50, standalone version) |
| 52 | 68 | 2042 | 1) Buyer posting an enquiry is one unique buyer for that day. If the same buyer posts another enquiry on a different day, he is considered as a different unique buyer — methodology note for the Unique Business Enquiries KPI |

### 5B. Unnumbered captions and disclaimers (6 — found only by manual sweep, folded into the reconciled grep pattern; see Count Test methodology)

| # | Slide | Line | Text | Qualifies |
|---|---|---|---|---|
| 53 | 22 | 646 | "Figures as of June 30, 2026" | The entire Key Competitive Strengths stat block (58% Repeat Buyers, 4.8 rating, 218K Paying Suppliers, etc.) — note this basis date differs from the "Q1 FY27" and "90 days" bases stated in footnotes 8-9 on the same slide, i.e. three different measurement windows coexist on one slide |
| 54 | 34 | 1021 | "* Figures in Thousand" | The three asterisked rows on the Operational Metrics table: Paying Suppliers*, ARPU*, Top 10% ARPU* |
| 55 | 55 | 1663 | "Figures as on March 31, 2026" | ESG slide stats (~48% Buyers from Small Cities, 0.03 TCO2e/Mn Turnover, 8.5Mn served) — stale by one full quarter vs the June 30, 2026 quarter-end being reported |
| 56 | 56 | 1695 | "Figures as on March 31, 2026" | Community Improvement stats (1.8 Million+ lives impacted, 97,000+ students, etc.) — same staleness as #55 |
| 57 | 60 | 1812 | "The figures are approximations" | Shareholding Pattern pie-chart percentages (Promoters 49%, FII/FPI, MF/AIF/Insurance, Others) |
| 58 | 4 | 92-138 | Safe Harbour disclaimer (full page); closing operative line at L138: "Unless otherwise stated, all the amounts in the presentation have been rounded off to INR crore." | Qualifies literally every number in the deck — the deck-wide unit and rounding convention, plus the standard forward-looking-statement and no-reliance disclaimers that qualify every guidance-adjacent or trend statement in the presentation |

---

## KPI MONITORING CROSS-REFERENCE (for the standing monitoring checklist — not a separate flag category, cross-referenced from Tables 1 and 4 above)

| KPI | Q1FY27 value | YoY | Slide(s) / Line(s) | Direction flag |
|---|---|---|---|---|
| Net Paying Suppliers | 218K | 0% YoY | Slide 8 (L224-225, L235), Slide 22 (L642), Slide 24 (L682), Slide 34 (L1012) | FLAT — and slide 8's fine print discloses 1,852 suppliers declined this quarter net; slide 35's footnote also flags a one-time 1.2K Q2FY26 onboarding benefit that inflates the YoY comparable base, meaning underlying growth is arguably weaker than the printed 0% |
| Active Buyers (LTM) | 41 Mn | -5% YoY | Slide 8 (L224-225 — printed as +5% Yoy on slide 8, but Slide 34 (L1002) shows -5% YoY | DISCREPANCY: slide 8 states "41 Mn / 5% YoY" without a sign, formatted as growth; slide 34's table explicitly shows "(5%)" (negative) for the same Active Buyers - Last 12 Months line, same 41 Mn figure. A3/A4 should reconcile — likely the slide-8 "5% YoY" is presented without the parenthesis-negative convention used in the table, and actually is the same -5% decline, but this needs explicit confirmation, not assumption |
| Unique Business Enquiries | 26 Mn (Q1FY27 quarterly) | -11% YoY | Slide 8 (L231-232, printed "11% YoY" without sign), Slide 22 (L628), Slide 34 (L1004, "(11%)"), Slide 68 (L2024, L2034, entire chart) | DECLINE — same sign-convention ambiguity as Active Buyers above; slide 34 and slide 68 both explicitly show negative (11%)/(11)% |
| Top 10% ARPU | Rs 349K (annualised) | +10% YoY | Slide 24 (L681), Slide 34 (L1016) | POSITIVE — best-performing named monitoring KPI this quarter |
| Standalone EBITDA Margin | 40% (reported) / 41% (Adjusted, ex-ESOP expense) | up from 37%/39% Q4FY26 | Slide 7 (L209), Slide 43 (L1286-1287, L1284-1285), Slide 47 (L1429-1431) | POSITIVE QoQ — note two different EBITDA margin figures coexist (reported vs adjusted); A3/A4 should use the one consistent with prior-quarter convention when trending |
| Busy Infotech metrics | Revenue 36 Cr (+47% YoY); EBITDA 3 Cr (EBITDA Margin 9%, down from 16% Q4FY26); Net Profit 6 Cr (margin 15%, up from 9% Q4FY26); Billing 59 Cr; Deferred Revenue 146 Cr (+44% YoY) | mixed | Slide 9 (L248-256), Slide 41 (L1224, L1232), Slide 52 (L1560-1572) | MIXED — revenue and deferred revenue growing fast, but EBITDA margin compressed sharply QoQ (16%→9%) while net margin improved (9%→15%); the EBITDA/PAT margin divergence (both moving opposite directions QoQ) needs a look at the "Others2" below-EBITDA line (L1567: 3/3/4/4/12/3/10) for what's driving PAT above EBITDA trend |
| Collections (Consolidated) | 463 Cr | +8% YoY | Slide 6 (L176-177), Slide 37 (L1106), Slide 40 (whole chart), Slide 63 (duplicate chart) | POSITIVE but decelerating vs Revenue growth (11% YoY) and well below EBITDA/PAT growth — CFO as % of Collections fell to 35% from 49% Q4FY26 (seasonal per footnote, but still the lowest %-of-Collections print in the trailing 5 quarters shown at L1918: 37/28/30/49/35) |
| Collections (Standalone) | 402 Cr | +8% YoY | Slide 7 (L200-201), Slide 43 (L1291), Slide 65 (chart) | Same pattern as consolidated; CFO % of Collections fell to 38% from 53% Q4FY26 (L1981: 39/30/33/53/38) |
| Deferred Revenue (Consolidated) | 2,014 Cr | +16% YoY | Slide 6 (L176-177), Slide 38 (L1136) | POSITIVE — fastest-growing of the six consol headline metrics on slide 6 |
| Deferred Revenue (Standalone) | 1,858 Cr | +14% YoY | Slide 7 (L200-201), Slide 44 (L1319), Slide 45 (whole chart) | POSITIVE; current-portion (12mo) share stable at 60-64% across the last 5 quarters shown |

---

## SUMMARY

- 69 slides enumerated, 0 unaccounted, DROPPED_SLIDE comparison N.A. (first quarterly cycle, no prior deck).
- 462 numeric content lines enumerated across all 69 slides (line-level granularity; each row commonly carries multiple individual data points, all visible verbatim in Table 4).
- 58 footnotes/fine-print items enumerated: 52 numbered, 6 unnumbered (4 basis-date captions, 1 units-asterisk caption, 1 full-page Safe Harbour disclaimer).
- 1 ZERO_STANDING line item flagged: "Proceeds from issue of shares" — zero every period FY22 through Q1FY27, template line retained since the FY21 IPO print.
- 7 of the deck's 9 section-divider slides were independently OCR-verified per the A1 header (pages 5, 10, 36, 42, 54, 59, 62); 2 divider slides (pages 33, 48) were not in the OCR list — flagged for awareness, not as a defect, since native text on both reads clean and complete.
- 1 sign-convention discrepancy flagged for A3/A4 to resolve: Active Buyers LTM and Unique Business Enquiries YoY% are printed without a minus sign on slides 8/18/22 (highlight-box style) but with explicit negative parentheses on slides 34/68 (table/chart style) for the same underlying decline — same figures, inconsistent presentation, worth an explicit reconciliation note rather than an assumption of consistency.
