=== A2 COUNT TEST ===
category: slides            grep_count: 38    sweep_count: 38    match: yes
category: line_items        grep_count: 171   sweep_count: 171   match: yes   (see RECONCILIATION NOTE below — first-pass sweep was 169, mismatch found, re-swept)
category: zero_standing     grep_count: 22    sweep_count: 22    match: yes
category: footnotes         grep_count: 4     sweep_count: 4     match: yes
gate_a2: pass
=== END COUNT TEST ===

RECONCILIATION NOTE (line_items):
- Grep pass: page 18 digit-row count 15 (raw) − 1 header row − 1 footer page-number = 12; page 19: 17 − 4 = 13; page 20: 17 − 4 = 13. Pages 18-20 subtotal = 38 (grep) = 38 (sweep) on first pass, no mismatch.
- Pages 33-38 (Historical Financials annexure, Restated Consolidated P&L/BS/CF): grep digit-row count 126, PLUS 7 rows that contain NO digit at all (all three period columns are dash "-", e.g. "- Borrowings   -   -   -", "Investment made in subsidiary   -   -   -") which a digit-based grep cannot catch — these were found instead via a separate dash-token grep pass. Grep-reconciled total pages 33-38 = 126 + 7 = 133.
- First manual sweep of pages 33-38 counted 131 rows (miscounted page 35 as 21→originally listed as 20, and page 36 as 25→originally listed as 24 — one row undercounted on each page on first pass). MISMATCH: 131 (sweep) vs 133 (grep). Re-swept pages 35 and 36 line by line against the raw extract text; corrected counts: page 35 = 21 rows, page 36 = 25 rows. Corrected pages 33-38 sweep = 19+16+21+25+26+26 = 133. Now MATCHES grep 133.
- Final line_items total = 38 (pp.18-20) + 133 (pp.33-38) = 171. GATE A2 PASS after re-sweep.

RECONCILIATION NOTE (zero_standing):
- Grep: dash-token pass over pages 33-38 (`grep -nE '(^|[[:space:]])-([[:space:]]|$)'`), then hand-filtered out false positives (label lines beginning "- Lease Liabilities", "- Borrowings" etc. used as bullet-style row labels, not dash values, and the EPS section header line ending in a colon-dash). True zero/dash-valued rows = 22. Manual sweep independently itemized the same 22 rows (listed in Table G/H/I below). MATCH.

RECONCILIATION NOTE (footnotes):
- Grep pattern `Note:|^\s*\*|\^Includes` found 4 distinct footnote/note blocks: p.5 (Adj. ROCE definition), p.9 (Note + ^Includes caption), p.12 (FY26 basis caption), p.38 (*Components of Cash and cash equivalents sub-header). Manual sweep independently found the same 4. A fifth candidate — the plain-text FY26 margin caption on p.11 (line 407) — is NOT asterisk/Note:-marked in the source; it is enumerated below as its own ledger row (Table B) but excluded from the footnote gate count to keep grep/sweep consistent.

=== TABLE A: SLIDE-LEVEL ENUMERATION (all 38 slides) ===

| # | Page | Title | Content type | Notes / Flags |
|---|------|-------|--------------|----------------|
|1|1|Regulation 30 cover letter to NSE/BSE|text (letter)|CIN L72200KA2008PLC045995; GST 29AABCI8601B1ZW; Trading Symbol IVALUE; Scrip Code 544523; letter date 29-Jul-2026; digital signature Lakshmammanni, Company Secretary & Compliance Officer, Membership No. A51625, signed 2026.07.29 16:55:05 +05'30|
|2|2|Title slide: "Investor Presentation – Q1 FY27 / 29th July 2026"|text/title graphic|THIN_TEXT flag (A1); no numeric data beyond date|
|3|3|Disclaimer|text|no numbers|
|4|4|Agenda (3 items: Company Overview, Financial Overview, Annexure)|text list|no numbers|
|5|5|Company Overview & Snapshot of Q1 FY27 performance|text + Key Figures Snapshot table|Snapshot metrics enumerated in Table B; footnote line159|
|6|6|Journey to an End-to-End Technology Solutions & Services Aggregator|chart (Gross Sales by year, FY09-3MFY27) + timeline text|chart data in Table B|
|7|7|10 Year CAGR (Gross Sales & PAT, FY17-FY26)|dual-axis bar/line chart|AMBIGUOUS_CHART_DATA flag — PAT series year-mapping unclear in extraction (Table B)|
|8|8|iValue – Adds value to OEM, Partner and Customers|diagram (VAD/SI/OEM value props)|"Over 300" solution stack count; step numbers 1-3|
|9|9|iValue – Presence across Four large and fast growing Technology Segments|segment % breakdown|44%/12%/22%/22% of Gross Sales; footnote line325|
|10|10|iValue – AI Strategy & Execution Highlights|text (5 categories)|no quantitative disclosures|
|11|11|Unique Positioning in the Market: True Technology Enabler|diagram (6 numbered nodes) + caption|FY26 GM 9.1%, EBITDA margin 5.1%, PAT margin 3.5% (line407)|
|12|12|What is Unique about iValue|text + metric callouts|9 metrics, footnote line442 ("FY26 basis")|
|13|13|Agenda (Financial Overview divider)|text divider|THIN_TEXT flag (A1); no numbers|
|14|14|Key Financial Highlights – Q1 FY27|4 metric callouts|Gross Sales, Rev from Ops, Operating EBITDA, PAT (Table C)|
|15|15|Financial Performance (Gross Sales Basis)|3-panel chart, Q1FY26 vs Q1FY27|Gross Sales/EBITDA/PAT values + margins (Table C)|
|16|16|Tech Segment Wise Performance & Annuity Business|Revenue Mix table + Annuity chart|SPECIAL ATTENTION — Table D|
|17|17|Working Capital Ratio (Gross Sales Basis)|4-panel chart: Receivables/Payables/Inventory/NWC Days|SPECIAL ATTENTION — Table E (trade payables balance disclosed here)|
|18|18|Financial Highlights – Gross Sales Vs Net Sales|full reconciliation table, 12 line items|Table F|
|19|19|Financials Summary (Gross Sales Basis) – Q1 FY27|full P&L table, 13 line items|SPECIAL ATTENTION — Table G|
|20|20|Financials Summary (Net Sales Basis) – Q1 FY27|full P&L table, 13 line items|Table H|
|21|21|Thank You / contact page|text|names/emails only, no financial numbers|
|22|22|Annexure (divider)|text divider|THIN_TEXT flag (A1); no numbers|
|23|23|Our Strengths (divider)|text divider|THIN_TEXT flag (A1); no numbers|
|24|24|Our Strengths (6 numbered items)|text list|no numeric financial data|
|25|25|Strategic technology partner for enterprises with diverse multi-OEM capabilities|text + metrics|474/45 enterprise customers by OEM tier; SaaS/renewal % FY23 vs FY26 (Table B)|
|26|26|OEM Ecosystem – Preferred Partner with Deep and Expanding Relationships|table (₹ Million, EXCEPTION unit) + 2 charts|EXCEPTION_UNIT flag (page-24-of-A1's-numbering = deck page 26); AMBIGUOUS_CHART_DATA flag on category breakdown (Table B)|
|27|27|Broad, Expanding System Integrator Ecosystem with Strong Retention and Recurring Business|text + charts|SI count, revenue share by tier, retention rates (Table B)|
|28|28|Case Studies (divider)|text divider|THIN_TEXT flag (A1); no numbers|
|29|29|Case study: Large-Scale Technology Refresh Program (Government/Public Sector)|narrative|"11+ OEMs" only quantitative mention|
|30|30|Case study: Multi-Year Strategic Engagement, largest Public Sector Bank|narrative|"12-to-24-month" horizon only quantitative mention|
|31|31|Case study: Large Scale Digital Infrastructure Transformation, largest Public Sector Bank (BFSI)|narrative|"10+ global technology vendors", "10+ OEMs" only quantitative mentions|
|32|32|Historical Financials (divider)|text divider|THIN_TEXT flag (A1); no numbers|
|33|33|Restated Consolidated Profit & Loss Statement (1/2)|financial table, FY24-FY26, ₹'m|UNIT_EXCEPTION_UNFLAGGED_BY_A1 (see below); Table G-PL, 19 rows|
|34|34|Restated Consolidated Profit & Loss Statement (2/2)|financial table, FY24-FY26, ₹'m|continuation; Table G-PL, 16 rows|
|35|35|Restated Consolidated Balance Sheet (1/2) — Assets|financial table, FY24-FY26, ₹'m|UNIT_EXCEPTION_UNFLAGGED_BY_A1; Table H-BS, 21 rows, 4 ZERO_STANDING|
|36|36|Restated Consolidated Balance Sheet (2/2) — Equity & Liabilities|financial table, FY24-FY26, ₹'m|UNIT_EXCEPTION_UNFLAGGED_BY_A1; Table H-BS, 25 rows, 5 ZERO_STANDING (incl. canonical "Investment made in subsidiary"-type item: Share buyback obligation, and non-current Borrowings, both nil in all 3 years)|
|37|37|Restated Consolidated Cash Flow Statement (1/2) — Operating|financial table, FY24-FY26, ₹'m|UNIT_EXCEPTION_UNFLAGGED_BY_A1; Table I-CF, 26 rows, 2 ZERO_STANDING|
|38|38|Restated Consolidated Cash Flow Statement (2/2) — Investing/Financing|financial table, FY24-FY26, ₹'m|UNIT_EXCEPTION_UNFLAGGED_BY_A1; Table I-CF, 26 rows, 9 ZERO_STANDING (incl. canonical "Investment made in subsidiary" = nil all 3 years, the exact SOUTHWEST-analog item)|

DROPPED_SLIDE check: no prior-quarter presentation ledger path was supplied to this run — comparison N/A, not evaluated.

UNIT_EXCEPTION_UNFLAGGED_BY_A1 (cross-cutting flag, all of pages 33-38):
A1's header states the deck's "unit_convention" is Crores dominant, with page 24 (deck page 26, "OEM Ecosystem" table) as the sole ₹-Million exception. This is INCOMPLETE: pages 33-38 (the entire "Historical Financials" annexure — Restated Consolidated P&L, Balance Sheet, and Cash Flow Statement) are explicitly headed "(in ₹'m, except for share data and if otherwise stated)" / "(in ₹'m, except if otherwise stated)" — i.e., ALSO stated in ₹ Million, not ₹ Crore, matching the primary deck's convention used elsewhere (pp.5-20). A3/A4 MUST apply the x0.1 conversion factor to every FY24/FY25/FY26 value in Tables G/H/I below before comparing to the Q1 FY27 quarterly figures on pp.14-20 (which are in ₹ Crore as stated). Flag: UNIT_EXCEPTION_UNFLAGGED_BY_A1.

=== TABLE B: NUMERIC DISCLOSURES — NARRATIVE / CHART SLIDES ===

| Page:Line | Slide | Metric | Value | Unit | Flags |
|---|---|---|---|---|---|
|5:146-152|Key Figures Snapshot|Gross Sales|641.2|₹ Crore| |
|5:147|Key Figures Snapshot|Gross Sales YoY|5.7%|%| |
|5:148|Key Figures Snapshot|Operating EBITDA|20.2|₹ Crore| |
|5:149|Key Figures Snapshot|Operating EBITDA YoY|27.7%|%| |
|5:146|Key Figures Snapshot|PAT|15.7|₹ Crore| |
|5:148|Key Figures Snapshot|PAT YoY|51.7%|%| |
|5:146|Key Figures Snapshot|Adj. ROCE|17.9%|%|footnote line159 defines calc|
|5:152/156|Key Figures Snapshot|Working Capital Days|52|days| |
|5:153/155|Key Figures Snapshot|Annuity Business (% of Gross Sales)|46.4%|%| |
|5:153|Key Figures Snapshot|OEM Partners|115|count|cross-checks to p.26 tenure table sum (22+51+20+22=115)|
|5:152|Key Figures Snapshot|Cash Position adj. for Debt|121|₹ Crore| |
|5:120|Company Overview|Years since founding|18|years| |
|5:126|Company Overview|Applications per enterprise|250+|count (non-financial callout)| |
|6:180-189|Journey chart|Gross Sales by year: FY09|14|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY12|81|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY15|218|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY18|526|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY21|939|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY23|1,811|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY24|2,110|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY25|2,439|₹ Crore| |
|6:180-189|Journey chart|Gross Sales by year: FY26|2,914|₹ Crore| |
|6:189|Journey chart|Gross Sales by year: 3MFY27|641|₹ Crore|(matches Gross Sales 641.2 elsewhere, rounded)|
|6:180|Journey chart|OEM portfolio (early)|6|count| |
|6:181|Journey chart|OEM partners signed up|30+|count| |
|7:217|10 Year CAGR|Gross Sales 10-yr CAGR|23%|%| |
|7:217|10 Year CAGR|PAT 10-yr CAGR|28%|%| |
|7:232-248|10 Year CAGR|Gross Sales by year FY17-FY26|457, 526, 712, 842, 939, 1,296, 1,811, 2,110, 2,439, 2,914|₹ Crore|clean series, year order FY17→FY26|
|7:232-246|10 Year CAGR|PAT by year FY17-FY26 (raw tokens seen, order ambiguous)|10, 18, 26, 31, 36, 37, 60, 60, 71, 85, 102|₹ Crore|AMBIGUOUS_CHART_DATA — pdftotext -layout interleaves the PAT line-series labels with the Gross Sales bar labels; 11 raw tokens found for 10 years (one likely a duplicate/split render of "60"); do NOT assume a year mapping without visual PDF check|
|8:260|Value chain diagram|Pre-tested solution stacks|300+|count| |
|9:299-300|Segment mix|Cybersecurity % of Gross Sales|44%|%|Q1 FY27, per footnote line325|
|9:299-300|Segment mix|Information Lifecycle Mgmt % of Gross Sales|12%|%| |
|9:300|Segment mix|Data Center Infrastructure % of Gross Sales|22%|%| |
|9:300|Segment mix|ALM, Cloud & Others % of Gross Sales|22%|%| |
|11:407|Positioning caption|FY26 Gross Margin|9.1%|%| |
|11:407|Positioning caption|FY26 EBITDA Margin|5.1%|%| |
|11:407|Positioning caption|FY26 PAT Margin|3.5%|%| |
|12:415|Unique callouts|Pre/post sales teams|200+|count| |
|12:415|Unique callouts|Tech certifications|1,000+|count| |
|12:419|Unique callouts|Customers with >2 OEM products|474|count| |
|12:419|Unique callouts|Partner Repeat rate|80%+|%| |
|12:425|Unique callouts|Annuity Revenue|42%+|%|footnote line442: "FY26 basis"|
|12:428-430|Unique callouts|Gross Margin|9.1%|%| |
|12:428-430|Unique callouts|EBITDA Margin|5.1%|%| |
|12:436|Unique callouts|Countries of presence|10|count| |
|12:437|Unique callouts|Years of continuous growth|18|years| |
|25:710-711|Multi-OEM adoption (FY26)|Enterprise customers using 2+ OEMs|474|count| |
|25:715-716|Multi-OEM adoption (FY26)|Enterprise customers using 5+ OEMs|45|count| |
|25:713|SaaS & renewal % of Gross Sales|FY23|34.55%|%| |
|25:712|SaaS & renewal % of Gross Sales|FY26|42.20%|%| |
|25:720|Focus accounts|Key accounts tracked|100|count| |
|25:721|Focus accounts|Pre-integrated multi-OEM stacks|30+|count| |
|26:733-740|OEM Ecosystem intro|Technology team share of headcount|>50%|%| |
|26:738|OEM Ecosystem intro|Employees with technical qualifications|215|count| |
|26:740|OEM Ecosystem intro|Total OEM certifications held|1,011|count| |
|26:737|Partner revenue table (₹ Million, EXCEPTION UNIT)|Cybersecurity OEM revenue FY23|96.49|₹ Million|EXCEPTION_UNIT — convert x0.1 = ₹9.649 Cr|
|26:737|Partner revenue table|Cybersecurity OEM revenue growth FY23→FY26|~1.6x|multiple| |
|26:737|Partner revenue table|Cybersecurity OEM revenue FY26|153.68|₹ Million|EXCEPTION_UNIT — convert x0.1 = ₹15.368 Cr|
|26:740|Partner revenue table|Data Center OEM revenue FY23|41.63|₹ Million|EXCEPTION_UNIT — convert x0.1 = ₹4.163 Cr|
|26:740|Partner revenue table|Data Center OEM revenue growth FY23→FY26|~8.9x|multiple| |
|26:740|Partner revenue table|Data Center OEM revenue FY26|410.43|₹ Million|EXCEPTION_UNIT — convert x0.1 = ₹41.043 Cr|
|26:749-761|OEM count by year (total)|FY23|42|count OEMs| |
|26:749-761|OEM count by year (total)|FY24|45|count OEMs| |
|26:749-761|OEM count by year (total)|FY25|50|count OEMs| |
|26:749-761|OEM count by year (total)|FY26|52|count OEMs| |
|26:748-760|OEM count by category (ALM&others / Data Center Infra / ILM / Cybersecurity) x year|raw tokens: 25, 27, 28, 31, 17, 20, 22, 23, 9, 9, 9, 9|count OEMs|AMBIGUOUS_CHART_DATA — category-to-year mapping cannot be reliably reconstructed from pdftotext -layout output; 12 raw tokens visible for a 4-category x 4-year grid (16 cells expected); do not force a mapping without visual PDF check|
|26:749|Deep Relationships table (FY26)|OEMs with tenure >10 years|22|count OEMs|clean, unambiguous|
|26:753|Deep Relationships table (FY26)|OEMs with tenure 6-10 years|51|count OEMs|clean; sum of 4 tenure bands = 22+51+20+22=115, matches p.5 "115 OEM Partners"|
|26:757|Deep Relationships table (FY26)|OEMs with tenure 3-5 years|20|count OEMs|clean|
|26:760|Deep Relationships table (FY26)|OEMs with tenure 0-2 years|22|count OEMs|clean|
|27:775-778|SI ecosystem|No. of SI partners FY23|567|count| |
|27:775-778|SI ecosystem|No. of SI partners FY26|866|count| |
|27:773|SI channel mix (FY26)|Global SIs — count / revenue share|41 / 30.60%|count / %| |
|27:778|SI channel mix (FY26)|National SIs — count / revenue share|128 / 26.20%|count / %| |
|27:781|SI channel mix (FY26)|Local SIs — count / revenue share|708 / 35.67%|count / %| |
|27:786|SI retention rate|FY23|64.35%|%| |
|27:785|SI retention rate|FY24|73.06%|%| |
|27:784|SI retention rate|FY25|80.73%|%| |
|27:784|SI retention rate|FY26|82.33%|%| |
|27:793|Focus accounts|Focus 100 accounts revenue contribution|~50%|%| |
|29:826|Case study 1|OEMs consolidated into unified solution|11+|count| |
|30:863|Case study 2|Account value build horizon|12-to-24 months|duration| |
|31:895/904/913|Case study 3|Global technology vendors / OEMs consolidated|10+ / 10+|count| |

=== TABLE C: KEY FINANCIAL HIGHLIGHTS & PERFORMANCE CHART (pp. 14-15) ===

| Page:Line | Metric | Q1 FY26 | Q1 FY27 | YoY | Unit |
|---|---|---|---|---|---|
|14:457|Gross Sales|—|641.2|5.7%|₹ Crore|
|14:457-459|Revenue from Operations (net)|—|179.7|(21.1%)|₹ Crore|
|14:464-467|Operating EBITDA|—|20.2|27.7%|₹ Crore; 3.2% on Gross Sales; 11.3% on Net basis|
|14:464-467|PAT|—|15.7|51.7%|₹ Crore; 2.5% on Gross Sales; 8.7% on Net basis|
|15:489-490|Gross Sales|606.4|641.2|5.7%|₹ Crore|
|15:492-493|Operating EBITDA|15.8|20.2|27.7%|₹ Crore|
|15:488|PAT|10.4|15.7|51.7%|₹ Crore|
|15:482|Operating EBITDA margin|2.6%|3.2%|—|%|
|15:482|PAT margin|1.7%|2.5%|—|%|

=== TABLE D: REVENUE MIX BY VERTICAL & ANNUITY BUSINESS (p.16) — SPECIAL ATTENTION ===

| Page:Line | Vertical | % of Gross Sales Q1FY26 | % of Gross Sales Q1FY27 | YoY Growth |
|---|---|---|---|---|
|16:515|Cybersecurity|43.0%|43.9%|8.1%|
|16:518|Data Centre Infrastructure|8.2%|22.1%|182.9%|
|16:520|Information Lifecycle Management|33.2%|12.5%|(60.4%)|
|16:522|ALM, Cloud and Others|15.5%|21.5%|46.6%|

Annuity Business (p.16, line 516-526):
| Metric | Q1 FY26 | Q1 FY27 | Growth |
|---|---|---|---|
|Annuity Business (₹ Crore)|261.5|297.2|13.7%|
|Annuity Business (% of Gross Sales)|43.1%|46.4%|—|

=== TABLE E: WORKING CAPITAL RATIO (p.17) — SPECIAL ATTENTION (trade payables balance source) ===

| Page:Line | Metric | Q1 FY26 | Q1 FY27 | YoY Growth | Unit |
|---|---|---|---|---|---|
|17:536-542|Trade Receivables|925.7|1,102.0|19.0%|₹ Crore|
|17:536-541|Trade Payables|594.3|747.2|25.7%|₹ Crore|
|17:552,557|Inventory|21.6|7.8|—|₹ Crore|
|17:552,562|Net Working Capital Days|53|52|—|days|

TRADE PAYABLES / DPO / RECEIVABLES DAYS DISCLOSURE — explicit finding (see report-back below): the deck discloses the Trade Payables BALANCE at two points in time each quarter (Q1FY26 = ₹594.3 cr, Q1FY27 = ₹747.2 cr, line 536-541) and the Trade Receivables balance (₹925.7 cr / ₹1,102.0 cr) and Inventory (₹21.6 cr / ₹7.8 cr). It does NOT disclose a separately labeled "Days Payable Outstanding," "Creditor Days," or "Receivable/Debtor Days" metric — only a single combined "Net Working Capital Days" figure (53 → 52) is shown. A3/A4 would need to derive DPO/DSO/DIO themselves from the balances above and the Gross Sales / COGS figures on pp.18-19 if required; this deck itself does not label those derived-day metrics.

Cross-reference (not an interpretation, a citation pointer for A3/A4): the FY26 year-end (annual, not quarterly) consolidated Trade Payables balance in the Historical Financials annexure (p.36, Table H below) = current MSME dues 119.89 + current other-creditor dues 7,255.72 = 7,375.61 (₹ Million) = ₹737.56 Cr after x0.1 conversion (non-current Trade Payables FY26 = nil, ZERO_STANDING). This FY26-year-end figure (₹737.56 Cr, as of Mar-2026) is a different point in time than the Q1FY27-quarter-end figure on p.17 (₹747.2 Cr, as of Jun-2026) — both are legitimate citations, do not conflate.

=== TABLE F: GROSS SALES VS NET SALES RECONCILIATION (p.18, 12 line items) ===

| Page:Line | Particulars (₹ Crore) | Q1 FY27 | Q4 FY26 | Q1 FY26 |
|---|---|---|---|---|
|18:570|Hardware (Gross Sales)|140.2|227.8|194.9|
|18:571|Software and Allied support services (Gross Sales)|501.0|521.9|411.5|
|18:572|Gross Sales billed to the Customers (A)|641.2|749.7|606.4|
|18:574|Purchase Cost i.r.o Software and Allied support services|(461.5)|(477.1)|(378.5)|
|18:576|Revenue from operations (B)|179.7|272.6|227.9|
|18:577|Gross COGS (Purchases + Changes in Inventories) (C)|589.2|655.7|565.3|
|18:578|Purchase Cost i.r.o Software and Allied support services (dup. row)|(461.5)|(477.1)|(378.5)|
|18:579|Net COGS (D)|127.7|178.6|186.8|
|18:580|Gross Margin (Gross Basis) (A-C)|52.0|94.0|41.1|
|18:582|Gross Margin (Net Basis) (B-D)|52.0|94.0|41.1|
|18:583|Gross Margin % (Gross Basis)|8.1%|12.5%|6.8%|
|18:584|Gross Margin % (Net Basis)|28.9%|34.5%|18.0%|

=== TABLE G: FINANCIALS SUMMARY — GROSS SALES BASIS (p.19, 13 line items) — SPECIAL ATTENTION (P&L) ===

| Page:Line | Particulars (₹ Crore) | Q1 FY27 | Q4 FY26 | QoQ Growth | Q1 FY26 | YoY Growth |
|---|---|---|---|---|---|---|
|19:596|Gross Sales|641.2|749.7|(14.5%)|606.4|5.7%|
|19:597|Gross Profit|52.0|94.0|(44.7%)|41.1|26.5%|
|19:598|Gross Profit %|8.1%|12.5%|(442bps)|6.8%|133bps|
|19:599|Operating Expense|34.6|39.6|(12.5%)|31.0|11.6%|
|19:600|EBITDA|17.4|54.5|(68.0%)|10.1|72.5%|
|19:601|EBITDA Margin (%)|2.7%|7.3%|(455bps)|1.7%|105bps|
|19:602|Operating Other Income|2.8|4.5|(34.5%)|5.7|(51.0%)|
|19:603|Operating EBITDA|20.2|58.9|(65.6%)|15.8|27.7%|
|19:604|Operating EBITDA (%)|3.2%|7.9%|(468bps)|2.6%|54bps|
|19:605|PBT|20.9|55.7|(62.8%)|13.9|51.2%|
|19:606|PBT Margin (%)|3.3%|7.4%|(423bps)|2.3%|98bps|
|19:607|PAT|15.7|42.3|(63.1%)|10.4|51.7%|
|19:608|PAT Margin (%)|2.5%|5.6%|(324bps)|1.7%|74bps|

=== TABLE H: FINANCIALS SUMMARY — NET SALES BASIS (p.20, 13 line items) ===

| Page:Line | Particulars (₹ Crore) | Q1 FY27 | Q4 FY26 | QoQ Growth | Q1 FY26 | YoY Growth |
|---|---|---|---|---|---|---|
|20:618|Revenue from Operations|179.7|272.6|(34.1%)|227.9|(21.1%)|
|20:619|Gross Profit|52.0|94.0|(44.7%)|41.1|26.5%|
|20:620|Gross Profit %|28.9%|34.5%|(554bps)|18.0%|1091bps|
|20:622|Operating Expense|34.6|39.6|(12.5%)|31.0|11.6%|
|20:623|EBITDA|17.4|54.5|(68.0%)|10.1|72.5%|
|20:624|EBITDA Margin (%)|9.7%|20.0%|(1029bps)|4.4%|526bps|
|20:625|Operating Other Income|2.8|4.5|(34.5%)|5.7|(51.0%)|
|20:627|Operating EBITDA|20.2|58.9|(65.6%)|15.8|27.7%|
|20:629|Operating EBITDA (%)|11.3%|21.6%|(1030bps)|6.9%|431bps|
|20:630|PBT|20.9|55.7|(62.8%)|13.9|51.2%|
|20:631|PBT Margin (%)|11.7%|20.4%|(897bps)|6.1%|557bps|
|20:632|PAT|15.7|42.3|(63.1%)|10.4|51.7%|
|20:633|PAT Margin (%)|8.7%|15.5%|(690bps)|4.5%|420bps|

=== TABLE G-PL: RESTATED CONSOLIDATED P&L STATEMENT (pp.33-34, ₹ Million — apply x0.1 for Cr) — UNIT_EXCEPTION_UNFLAGGED_BY_A1 ===

| Page:Line | Particulars | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|
|33:928|Revenue from Operations|7,802.30|9,226.80|10,555.60| |
|33:929|Other Income|149.50|196.70|194.20| |
|33:930|Total Income|7,951.80|9,423.50|10,749.80| |
|33:932|Purchases of Stock-in-trade|4,977.39|6,652.76|7,831.54|extraction shows "4,977 39" (space not decimal point) — value read as 4,977.39; possible OCR artifact, flag EXTRACTION_ARTIFACT|
|33:933|Changes in inventories of Stock-in-trade|630.44|142.30|60.43| |
|33:934|Employee benefits expense|652.05|687.97|738.91| |
|33:935|Finance Costs|129.13|134.59|112.51| |
|33:936|Depreciation and amortisation expense|68.99|71.62|69.46| |
|33:937|Other expenses|548.12|602.33|581.80| |
|33:938|Total Expenses|7,006.12|8,291.57|9,394.65| |
|33:939|Restated profit before tax and exceptional item|945.68|1,131.93|1,355.15| |
|33:940|Exceptional Items|—|—|51.88|ZERO_STANDING (FY24, FY25)|
|33:941|Restated profit before tax|945.68|1,131.93|1,303.27| |
|33:943|(1) Current tax|253.40|282.11|341.81| |
|33:944|(2) Tax adjustments for earlier years (Net)|-9.41|1.99|-6.63| |
|33:945|(3) Deferred tax|-4.01|-5.17|-15.68| |
|33:946|Total Tax Expense|239.98|278.93|319.50| |
|33:947|Restated profit after tax for the year|705.70|853.00|983.77| |
|33:950|(i) Remeasurements of post employment benefit obligations|-0.03|-0.69|5.70| |
|34:958|(ii) Income tax relating to these items (not-reclassified OCI)|0.17|0.26|-1.44| |
|34:960|(i) Exchange differences on translation of foreign operations|0.21|-0.85|6.80|extraction shows "-.85"|
|34:961|(ii) Income tax relating to these items (reclassifiable OCI)|—|—|—|ZERO_STANDING all 3 years; extraction shows only a single dash with no visible column structure — flag EXTRACTION_GAP, verify against source PDF|
|34:962|Restated Other Comprehensive Income/(loss) for the year|-0.31|-1.62|11.06| |
|34:963|Restated Total Comprehensive Income for the year|705.39|851.38|994.83| |
|34:966|(i) Profit attributable to Owners of Ivalue Infosolutions Ltd|710.28|855.79|982.33| |
|34:967|(ii) Profit attributable to Non-controlling interests|-4.58|-2.79|1.46| |
|34:968|[subtotal check row, profit attributable]|705.70|853.00|983.79|note: differs from line947 "983.77" by 0.02 in FY26 — rounding, flag for A3/A4, not resolved here|
|34:970|(i) OCI attributable to Owners|-0.17|-1.14|10.66| |
|34:971|(ii) OCI attributable to NCI|-0.14|-0.48|0.42| |
|34:972|[subtotal, OCI attributable]|-0.31|-1.62|11.08| |
|34:974|(i) Total Comprehensive Income attributable to Owners|710.11|854.65|992.98| |
|34:975|(ii) Total Comprehensive Income attributable to NCI|-4.72|-3.27|1.88| |
|34:976|[subtotal, TCI attributable]|705.39|851.38|994.86| |
|34:978|Basic EPS (Rs.)|13.27|15.98|18.06|per-share, NOT in ₹ Million — do not apply x0.1|
|34:979|Diluted EPS (Rs.)|13.27|15.98|17.98|per-share, NOT in ₹ Million — do not apply x0.1|

=== TABLE H-BS: RESTATED CONSOLIDATED BALANCE SHEET (pp.35-36, ₹ Million — apply x0.1 for Cr) — UNIT_EXCEPTION_UNFLAGGED_BY_A1 ===

| Page:Line | Particulars | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|
|35:993|Property, Plant and Equipment|99.61|95.84|86.78| |
|35:994|Right-of-use assets|300.74|249.98|193.70| |
|35:995|Goodwill|76.43|76.43|76.43| |
|35:996|Other Intangible assets|4.10|3.03|1.23| |
|35:998|-Loans (non-current)|60.00|60.00|—|ZERO_STANDING (FY26)|
|35:999|-Trade Receivables (non-current)|—|205.24|—|ZERO_STANDING (FY24, FY26)|
|35:1000|-Other financial assets (non-current)|34.16|52.08|60.86| |
|35:1001|Income tax assets (net)|689.52|235.76|768.76| |
|35:1002|Deferred tax assets (net)|57.15|62.58|76.89| |
|35:1003|Other non-current assets|12.44|70.63|72.69| |
|35:1004|Total Non-current assets|1,333.15|1,112.29|1,337.34| |
|35:1006|Inventories|270.41|128.11|67.79| |
|35:1008|-Investments (current)|—|—|1,528.92|ZERO_STANDING (FY24, FY25) — canonical template-signal item (SOUTHWEST-analog)|
|35:1009|-Trade receivables (current)|6,732.11|8,258.61|9,731.40| |
|35:1010|-Cash and cash equivalents|1,279.78|1,178.59|1,196.04| |
|35:1011|-Bank balances other than cash and cash equivalents|66.95|470.18|89.40| |
|35:1012|-Loans (current)|0.01|—|—|ZERO_STANDING (FY25, FY26)|
|35:1013|-Other financial assets (current)|52.01|122.58|119.84| |
|35:1014|Other current assets|308.09|356.37|338.61| |
|35:1015|Total Current assets|8,709.66|10,514.44|13,072.00| |
|35:1016|Total Assets|10,042.51|11,626.73|14,409.34| |
|36:1030|Equity Share capital|42.11|84.22|109.26| |
|36:1031|Instruments entirely equity in nature|12.50|12.50|—|ZERO_STANDING (FY26)|
|36:1032|Other Equity|3,662.25|4,541.40|5,569.49| |
|36:1033|Equity attributable to owners of Ivalue Infosolutions Ltd|3,716.86|4,638.12|5,678.75| |
|36:1034|Non Controlling Interest|-14.51|-17.78|-6.86| |
|36:1035|Total Equity|3,702.35|4,620.34|5,671.89| |
|36:1039|-Borrowings (non-current)|—|—|—|ZERO_STANDING all 3 years|
|36:1040|-Lease Liabilities (non-current)|256.59|213.45|184.17| |
|36:1041|-Trade Payables (non-current)|—|148.97|—|ZERO_STANDING (FY24, FY26)|
|36:1042|Other Financial Liabilities (non-current)|—|15.41|35.96|ZERO_STANDING (FY24)|
|36:1043|Provisions (non-current)|30.24|23.73|54.28| |
|36:1044|Total Non-current liabilities|286.83|401.56|274.41| |
|36:1047|-Share buyback obligation (current)|—|—|—|ZERO_STANDING all 3 years — CANONICAL zero-standing item; template signal that a share-buyback transaction has occurred, is occurring, or is anticipated (SOUTHWEST-analog)|
|36:1048|-Borrowings (current)|451.91|424.51|464.48| |
|36:1049|-Lease Liabilities (current)|60.61|64.23|44.62| |
|36:1051|(i) Trade payables — dues of micro and small enterprises|0.93|0.26|119.89| |
|36:1052|(ii) Trade payables — dues of creditors other than (i)|5,016.25|5,552.25|7,255.72| |
|36:1053|-Other financial liabilities (current)|40.09|79.08|59.45| |
|36:1054|Current tax liabilities (net)|12.46|33.47|35.99| |
|36:1055|Contract liabilities|19.36|38.72|50.47| |
|36:1056|Other current liabilities|399.85|399.22|394.25| |
|36:1057|Provisions (current)|51.77|13.09|37.91| |
|36:1058|Total Current Liabilities|6,053.33|6,604.83|8,462.78| |
|36:1059|Total Liabilities|6,340.16|7,006.39|8,737.19| |
|36:1060|Total Equity and Liabilities|10,042.51|11,626.73|14,409.34| |

Annual (FY26 year-end) Total Trade Payables = 0 (non-current) + 119.89 (MSME) + 7,255.72 (other creditors) = 7,375.61 ₹ Million = ₹737.56 Cr. See cross-reference note under Table E.

=== TABLE I-CF: RESTATED CONSOLIDATED CASH FLOW STATEMENT (pp.37-38, ₹ Million — apply x0.1 for Cr) — UNIT_EXCEPTION_UNFLAGGED_BY_A1 ===

| Page:Line | Particulars | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|
|37:1069|Restated profit before tax|945.68|1,131.93|1,303.30|note: differs from P&L p.34 restated PBT "1,303.27" by 0.03 in FY26 — rounding, flag for A3/A4|
|37:1071|Depreciation and Amortisation expenses|68.99|71.62|69.46| |
|37:1072|Provision for Employee stock appreciation rights|21.14|18.25|28.19| |
|37:1073|Interest Income|-33.19|-80.10|-79.90| |
|37:1074|Net Gain on Investments carried at FVTPL|-1.89|-8.30|-35.27| |
|37:1075|Unwinding of interest on security deposit|-1.17|-1.37|-1.84| |
|37:1076|Gain on Termination of Leases|-1.39|—|—|ZERO_STANDING (FY25, FY26)|
|37:1077|Net Fair value loss/(gain) on derivatives not designated as hedges|-4.30|29.35|-62.73| |
|37:1078|Unrealised (gain)/loss on foreign currency translation|-12.27|-33.34|88.63| |
|37:1079|Finance costs|129.13|134.59|112.51| |
|37:1080|Bad Debts Written off|60.40|83.98|25.89| |
|37:1081|Fair value change in share buyback obligation|—|—|—|ZERO_STANDING all 3 years|
|37:1082|Allowance made/(reversed) for Expected credit loss on trade receivables|0.09|0.82|32.64| |
|37:1083|Operating Profit before Working Capital Changes|1,171.22|1,347.43|1,480.87| |
|37:1085|(Increase)/Decrease in Other financial assets|-1.40|-87.03|45.96| |
|37:1086|(Increase)/Decrease in Inventories|630.44|142.30|60.43| |
|37:1087|(Increase)/Decrease in Trade Receivables|215.22|-1,834.22|-1,311.15| |
|37:1088|(Increase)/Decrease in Other Current and Non-current Assets|804.30|-106.36|15.67| |
|37:1089|Increase/(Decrease) in Trade Payables|-1,427.44|733.34|1,581.76| |
|37:1090|Increase/(Decrease) in Other Financial Liabilities|-19.66|25.05|-2.36| |
|37:1091|Increase/(Decrease) in Provisions|2.52|3.17|53.93| |
|37:1092|Increase/(Decrease) in Contract Liabilities|-6.58|19.36|11.76| |
|37:1093|Increase/(Decrease) in Current Liabilities|30.85|-0.63|-4.97| |
|37:1094|Cash Generated from operations|1,399.47|242.41|1,931.90| |
|37:1095|Less: Income tax payments (net of refunds received)|-742.96|219.73|-852|value "-852" appears truncated (no decimal places, unlike every other row) — flag EXTRACTION_ARTIFACT, verify exact figure against source PDF|
|37:1096|Net Cash flow from/(used in) Operating Activities (A)|656.51|462.14|1,079.90| |
|38:1107|Investment made in subsidiary|—|—|—|ZERO_STANDING all 3 years — CANONICAL zero-standing item (direct SOUTHWEST-analog: "Investment made in subsidiary" nil in every period shown)|
|38:1108|Payments for purchase of investments|-20.00|-350.00|-2,395.00| |
|38:1109|Proceeds from sale of investments|133.43|358.30|901.45| |
|38:1110|Investments in fixed deposits with banks|-2,029.21|-2,040.64|-3,525.63| |
|38:1111|Proceeds from withdrawal of fixed deposits with banks|2,157.71|1,633.66|3,919.86| |
|38:1112|Loan given|-0.21|—|60|ZERO_STANDING (FY25); FY26 value shown without decimal ("60") — possible truncation, flag EXTRACTION_ARTIFACT|
|38:1113|Interest received|33.40|51.27|65.99| |
|38:1114|Purchase of Property, Plant and Equipment (incl. capital advance)|-38.38|-11.16|-2.15| |
|38:1115|Net Cash flow from/(used in) Investing Activities (B)|236.74|-358.57|-975.49| |
|38:1117|(Repayment) of/Proceeds from working capital|-47.55|-27.40|41.47| |
|38:1118|(Repayment) of long term rupee term loan from banks|-5.30|—|—|ZERO_STANDING (FY25, FY26)|
|38:1119|Proceeds from Issue of Equity Share under ESOP scheme and conversion of preference shares|—|—|31.01|ZERO_STANDING (FY24, FY25)|
|38:1120|Repayment of Principal element of Lease Liabilities|-36.83|-42.77|-48.92| |
|38:1121|Finance cost Paid|-129.13|-134.59|-110.61| |
|38:1122|Net Cash Flow from/(Used in) Financing Activities (C)|-218.81|-204.76|-87.04| |
|38:1123|Net (Decrease)/Increase In Cash And Cash Equivalents (A+B+C)|674.44|-101.19|17.36| |
|38:1124|Cash and Cash Equivalents at the beginning of the year|605.34|1,279.78|1,178.59| |
|38:1125|Effects of exchange rate changes on cash and cash equivalents|—|—|—|ZERO_STANDING all 3 years|
|38:1126|Cash & Cash Equivalent at the end of the year*|1,279.78|1,178.59|1,195.70|asterisk refs Components sub-table below; note this differs from Balance Sheet p.35 "Cash and cash equivalents" FY26 = 1,196.04 by 0.34 — rounding/different-scope, flag for A3/A4|
|38:1128|Acquisition of Right of use Assets|66.24|4.86|—|ZERO_STANDING (FY26)|
|38:1129|Disposal of Right of use Assets|-5.81|—|—|ZERO_STANDING (FY25, FY26)|
|38:1130|Fair value change in share buyback obligation (non-cash section)|—|—|—|ZERO_STANDING all 3 years; extraction shows only a single dash with no visible column structure — flag EXTRACTION_GAP|
|38:1132|Cash on Hand|0.13|—|0.30|ZERO_STANDING (FY25)|
|38:1133|In Current Accounts|249.85|1,163.59|610.40| |
|38:1134|Deposit with Banks with less than 3 months original maturity|1,029.80|15.00|585|FY26 value "585" shown without decimal, unlike every other row — flag EXTRACTION_ARTIFACT|
|38:1135|Total|1,279.78|1,178.59|1,195.70| |

=== TABLE J: FOOTNOTES / FINE PRINT ===

| Page:Line | Footnote text (qualifying) |
|---|---|
|5:159|"* Adjusted Capital employed is calculated as the sum of Tangible Net Worth plus Total Net Debt, as reduced by Deferred Tax Assets" — qualifies Adj. ROCE 17.9% on same slide|
|9:325|"Note: The numbers in circles denote % of total Gross sales billed to the customers (Q1 FY27)  ^Includes private, public and hybrid clouds" — qualifies the 44%/12%/22%/22% segment mix|
|12:442|"* The numbers depicted above are for FY26" — qualifies all 9 callout metrics on the slide|
|38:1131|"*Components of Cash and cash equivalents" — sub-table header, ties back to the asterisk on "Cash & Cash Equivalent at the end of the year*" (line 1126)|

Non-gated additional caption (enumerated, not counted in footnote gate — no asterisk/Note: marker in source):
|11:407|"For FY26- iValue commands highest GM of 9.1%, EBITDA Margin of 5.1% & PAT Margin of 3.5% as compared to any other pure play distributor & VAD" — qualifying/contextualizing caption below the positioning diagram|

=== SUMMARY OF FLAGS RAISED ===
- ZERO_STANDING: 22 rows (Tables G-PL/H-BS/I-CF), including the canonical template-signal items "Investment made in subsidiary" (all 3 years nil) and "Share buyback obligation" (both BS and CF views, all 3 years nil).
- UNIT_EXCEPTION_UNFLAGGED_BY_A1: pages 33-38 (Historical Financials annexure — 6 pages, all 3 statements) stated in ₹ Million, not flagged as an exception by A1's header (which named only page 24/deck-p.26 as the Million exception). Requires x0.1 conversion.
- EXCEPTION_UNIT: p.26 OEM partner revenue table, ₹ Million (A1-flagged).
- AMBIGUOUS_CHART_DATA: p.7 PAT-by-year series (11 raw tokens for 10 years); p.26 OEM-count-by-category-by-year grid (12 raw tokens for 16 expected cells).
- EXTRACTION_ARTIFACT: p.33 line932 "4,977 39" (likely 4,977.39); p.37 line1095 "-852" (likely truncated); p.38 line1112 "60" and line1134 "585" (likely truncated, missing decimals).
- EXTRACTION_GAP: p.34 line961 and p.38 line1130, both "(ii)/Fair value change..." rows showing only a single dash where three period-columns are expected.
- Minor rounding discrepancies flagged for A3/A4 (not resolved at enumeration stage): FY26 profit-attributable subtotal 983.79 vs restated PAT 983.77 (Table G-PL); FY26 restated PBT in P&L (1,303.27) vs Cash Flow (1,303.30) (Table I-CF); FY26 cash & cash equivalents, Balance Sheet (1,196.04) vs Cash Flow closing balance (1,195.70) (Table I-CF).
- DROPPED_SLIDE: not evaluated, no prior-quarter ledger supplied.

=== END LEDGER ===

```yaml
stage: A2-enumerator
company: "IVALUE"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/ivalue-q1fy27/work/ledger_presentation_ivalue_q1fy27.md"
counts:
  notes: 0
  line_items: 171
  zero_standing: 22
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 38
  slide_numbers: 38
flags_raised: [ZERO_STANDING, UNIT_EXCEPTION_UNFLAGGED_BY_A1, EXCEPTION_UNIT, AMBIGUOUS_CHART_DATA, EXTRACTION_ARTIFACT, EXTRACTION_GAP]
gate_a2: pass
mismatch_note: ""
```
