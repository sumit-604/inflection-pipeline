# A2 ENUMERATION LEDGER — Investor Presentation
Company: Shriram Properties Limited (SPROP) | Quarter: Q1 FY27 (quarter ended June 30, 2026)
Doctype: presentation | Source: presentation_sprop_q1fy27.pdf (26 pages, page_coverage 100%)
Extract: runs/sprop-q1fy27/work/extract_presentation_sprop_q1fy27.txt

```
=== A2 COUNT TEST ===
category: slides                    grep_count: 26   sweep_count: 26   match: yes
category: numeric_disclosure_lines  grep_count: 256  sweep_count: 256  match: yes
category: footnote_markers          grep_count: 5    sweep_count: 5    match: yes
category: dropped_slides            grep_count: 0    sweep_count: 0    match: yes  (prior deck unavailable, see Section 4)
gate_a2: pass
=== END COUNT TEST ===
```

Count-test methodology:
- slides: grep `^\[page [0-9]+\]$` against the extract (26 matches, pages 1-26) reconciled
  against a manual page-by-page read of the full 666-line extract (26 pages walked in
  sequence, none skipped, none merged).
- numeric_disclosure_lines: grep for non-blank body lines (line 15-666, excluding the
  `[page N]` markers themselves) containing at least one digit
  (`awk 'NR>=15&&NR<=666 && /[0-9]/ && !/^\[page [0-9]+\]$/'`) = 256 lines. Manually swept
  the same 256 lines one by one (Section 2 below) to attach slide number, content, and
  flags. This is a line-grain count (a table row or chart-label cluster on one physical
  line = one unit), not an individual-token count; every individual value within each row
  is still listed in the Content column so no digit is silently dropped.
- footnote_markers: grep for the underscore separator-rule that precedes every footnote
  block (`^\s*_{3,}`) = 5 (lines 102, 171, 329, 444, 639), each paired manually with its
  footnote text (lines 103, 172, 330, 445, 640) = 5 footnotes, reconciled.
- dropped_slides: no prior-quarter deck was supplied to this run (prior-quarter ledger
  path = NONE), so the DROPPED_SLIDE check could not be executed. Recorded as a gap, not
  papered over — see Section 4.

---
## SECTION 1: SLIDES (26 of 26)
| Slide | Line | Title / Heading | Content Type | Notes / Flags |
|-------|------|------------------|---------------|----------------|
| 1 | 14 | (Covering letter to NSE/BSE — Reg. 30 intimation) | text (regulatory cover letter) | Not a deck slide per se; the filing wrapper. Digital signature block present (K. Ramaswamy, Company Secretary, 2026.08.12 20:51:11 +05'30'). BOILERPLATE_ID heavy. |
| 2 | 64 | Investor Presentation — Q1 \| FY27 Results | text/photo (title slide) | Artist's impression photo (Shriram Stellar, Chennai); dated August 12, 2026. |
| 3 | 75 | (Untitled — legal disclaimer) | text (fine-print disclaimer, full page) | Forward-looking-statements / no-reliance disclaimer. No numeric content besides trailing footer "1". See Section 3, item F0 — flagged NO_TYPOGRAPHIC_MARKER (full-page disclaimer with no footnote symbol, qualifies every number in the rest of the deck). |
| 4 | 91 | Shriram Properties Overview | text/table (4-pillar overview) | KPI icons: 26+ yrs, 52 completed projects, 33+ msf delivered, 32,000+ customers, 23% referral volumes^ (footnoted), Debt Equity 0.3x, CRISIL A- (Positive). |
| 5 | 112 | Q1\|FY27 Performance Highlights | photo (section divider) | Artist's impression (Shriram Sapphire, Bangalore). No data content. |
| 6 | 118 | Q1 FY27: Strong Operational Start; Strengthening Growth Visibility | text (narrative commentary) | Three launches, Kolkata value-unlock narrative. No tabulated numbers. |
| 7 | 144 | KPI Snapshot: Q1\|FY27 | table/chart (KPI tiles) | Sales Value 484, Sales Volume 0.85, Collections 365, Handovers 690; Revenues 271, Gross Profit 56, EBITDA 42, Net Profit 11; YoY% tiles 10/4/8/7%; PBT ₹18 Crs callout. Footnoted (Note: line 172). |
| 8 | 175 | Performance Highlights: Q1\|FY27 | text (3-column: Operational / Financial / BD highlights) | Repeats KPI figures in narrative form; adds ~40% Q1 revenue from Kolkata, ₹650 Crs GDV addition, 7+ msf projects nearing closure. |
| 9 | 206 | Q1 FY27 Launches – Strong Launch Momentum | table (launches) + text (strategic highlights) | 3-row launch table (Stellar, Southbrook, Green Meadows) + Total row; ~20% sold at launch week (Stellar), ~55% sold within 30 days (Southbrook). |
| 10 | 238 | High Powered launch highlights in Chennai & Kolkata during Q1 | text/photo (2 project cards) | Stellar: 135 units, ~₹320 Crs GDV. Southbrook: 296 units, ~₹130 Crs GDV, 16 acres. |
| 11 | 252 | Project Pipeline & Business Development Overview | chart/table (bar chart + 3 tables) | Pipeline bar chart (33.7/16.0/17.7 msf and Own/JDA/JV/DM splits), project-count row, Pipeline Unsold GDV table, Upcoming Projects Ownership GDV table, BD pipeline callouts (650+ Crs, 7+ msf, 20+ msf, 18-24 months). |
| 12 | 295 | Financial Highlights: Q1\|FY27 | photo (section divider) | Artist's impression (Shriram Esquire, Bangalore). No data content. |
| 13 | 301 | Financial Highlights: Profit & Loss – Q1\|FY27 | table (P&L, 4 periods) | Full P&L: Income from Ops through Net Profit, Q1FY27/Q1FY26/Q4FY26/FY26. Contains the one ZERO_STANDING cell (Unwinding Impact, Q1FY27 = "-"). Footnoted with asterisk (line 330). |
| 14 | 337 | Financial Highlights: Profit & Loss – Q1\|FY27 (continued) | text (bullet commentary) | Narrative restating Gross Profit ₹56 Crs, EBITDA ₹42 Crs, margins 25%/15%, JV loss ₹4 Crs, 4% non-compete fee cessation, Net Profit ₹11 Crs. |
| 15 | 366 | Consolidated Cash Flows: Q1\|FY27 (Excl. DM & JV cashflows) | table + chart (cash flow statement + 2 bar-chart panels) | Full CFS table (3 periods) plus "Collection Trends" and "FCF before Inv. / New Project Inv. trends" bar charts with FY24-Q1FY27 data labels (OCR/native mixed layout — see Section 2 CHART_LABEL rows). |
| 16 | 414 | Debt Profile: Healthy Gearing with Competitive Cost | table + chart (debt table + 2 bar charts) | Gross External Debt¹/Cash/Net Debt/Total Equity/Net Debt-Equity across Jun'26/Mar'26/Mar'25/Mar'24, plus Gross-and-Net-Debt and Net-Debt-Equity trend charts. Footnoted (superscript 1, line 445). |
| 17 | 449 | FY27 Guidance & Outlook | photo (section divider) | Artist's impression (Shriram Spectrum, Pune). No data content. |
| 18 | 454 | FY27 Outlook: Guidance Remains Unchanged | table/text (8 guidance tiles) | Sales Volume 5.0-5.5 msf, Sales Value 3,300-3,500 Crs, Collections 2,100-2,200 Crs, Handovers 3,750-3,800 units, plus YoY growth ranges; Completion 7-8 projects, Delivery 4.0-4.5 msf, Pipeline addition 7.0-8.0 msf, GDV addition 5,000-6,000 Crs. |
| 19 | 483 | FY27 New Project Launch Calendar: 10+ New Launch Potential | table (11-row launch calendar) | 11 named projects with Area/Launch Area/Quarter/Revised Estimate/Status; Total row 7.23/5.93 msf. |
| 20 | 509 | FY27 Handovers: High Confidence on FY targets driven by On-track Project Progress | text/graphic (funnel-style handover potential) | Q2 OC and H2 OC revenue-potential call-outs + combined total; text-extraction column order is ambiguous (see Section 2, LAYOUT_AMBIGUOUS). |
| 21 | 529 | Our Mission FY28 – On Steady Trajectory for Achieving | chart/table + OCR graphic | Pipeline-to-revenue funnel (33.7/16.0/17.7/13.1/2.9/17.4 msf tree), FY28 Mission Target tile (Sales Value/Revenues/Earnings), Revenue Potential tiles (8.8 msf/₹4,800+ Crs and 17.4 msf/₹9,000+ Crs), "~₹14,000 Crs in 5-7 years" callout, plus the OCR-flagged "MISSION 1234" circular graphic (qualitative labels only, no numbers — see header ocr_pages note and Section 2 row 220). |
| 22 | 567 | Thank You | photo/text (closing slide) | Artist's impression (Shriram Skybloom Villas, Kolkata / Shriram Serenity, Bangalore — dual caption). Footer shows duplicated "20 20" (OCR/extraction artifact, not content). |
| 23 | 576 | Annexures | text (section divider) | Native text extraction below 100-char threshold; full-page OCR fallback confirms section-divider only, no missed content (see header ocr_pages note and Section 2 row 223). |
| 24 | 586 | Annexure-1: Projects Snapshot by Development Models | table (4-column x 3-tier project stats) | Own/Joint Development/Joint Venture/Development Management columns x Completed/Ongoing/Upcoming rows, each with project count and msf. |
| 25 | 615 | Annexure-2: Consolidated Cash Flows – With and Without JV Cashflows | table (dual CFS: Consolidated vs Enterprise 100%) | Same 17-line-item cash flow structure as slide 15, run twice (SPL Consolidated CFS vs SPL Enterprise 100% ex-DM), 3 periods each. Footnoted (superscript 1, line 640). |
| 26 | 644 | For further information, please contact | text (contact/IR block) | Company and IR-advisor (SGA) contact details; CINs, emails, phone numbers (BOILERPLATE_ID). |

---
## SECTION 2: EVERY NUMBER ON EVERY SLIDE (line-grain sweep, 256 of 256 rows)
Every non-blank body line (page 1 through page 26, i.e. extract lines 15-666) that carries
at least one digit is listed below with its slide number and full content, so that every
individual value inside multi-value rows (table cells, chart-label clusters, KPI tiles) is
captured. Flags: `BOILERPLATE_ID` = registration/contact number, not a KPI;
`ZERO_STANDING` = dash/nil value in a standing line item;
`CHART_LABEL` = bar/funnel chart data label (OCR-adjacent — pages 15, 16, 21 charts render
with native-text data labels whose reading order the extractor could not fully preserve;
values are captured but slide-side column attribution should be treated as indicative,
not exact, for those rows); `LAYOUT_AMBIGUOUS` = page 20 two-column funnel graphic whose
text order does not reliably map value-to-column; `NO_NUMERIC_OCR/OCR_GRAPHIC` = page 21
"MISSION 1234" circular graphic, OCR'd, confirmed qualitative-only; `OCR_FALLBACK_PAGE` =
page 23, full-page OCR fallback (native extraction < 100 chars); `OCR_ARTIFACT_DUP_FOOTER`
= page 22 duplicated footer digits, an extraction artifact not content;
`FOOTNOTE_MARKER` = footnote separator or footnote text line (cross-referenced in Section 3).

| # | Line | Slide | Content (value / label) | Flags |
|---|------|-------|--------------------------|-------|
| 1 | 15 | 1 | August 12, 2026 | BOILERPLATE_ID |
| 2 | 19 | 1 | Exchange Plaza, 5th Floor Plot C 1 – G Block  Phiroze Jeejeebhoy Towers | BOILERPLATE_ID |
| 3 | 21 | 1 | Mumbai 400 051  Mumbai 400 001 | BOILERPLATE_ID |
| 4 | 22 | 1 | Scrip Code: SHRIRAMPPS  Scrip Code: 543419 | BOILERPLATE_ID |
| 5 | 28 | 1 | Pursuant to the provisions of Regulation 30 of SEBI (Listing Obligations and Disclosure Requirements) | BOILERPLATE_ID |
| 6 | 29 | 1 | Regulations, 2015, please �ind enclosed the Investor Presentation on the Unaudited Financial Results (Standalone | BOILERPLATE_ID |
| 7 | 30 | 1 | & Consolidated) of the Company for the quarter ended June 30, 2026. | BOILERPLATE_ID |
| 8 | 42 | 1 | Swamy Date:  2026.08.12 | BOILERPLATE_ID |
| 9 | 43 | 1 | 20:51:11 +05'30' | BOILERPLATE_ID |
| 10 | 47 | 1 | ACS 28580 | BOILERPLATE_ID |
| 11 | 56 | 1 | ‘Shriram House’, No. 31, T Chowdaiah Road,  Lakshmi Neela Rite Choice Centre, 1 Floor, | BOILERPLATE_ID |
| 12 | 57 | 1 | Sadashivanagar, Bengaluru - 560 080  #9, Bazulla Road, T. Nagar, Chennai – 600 017 | BOILERPLATE_ID |
| 13 | 60 | 1 | P: +91-80-40229999 / F: +91-80-41236222 / W: www.shriramproperties.com | BOILERPLATE_ID |
| 14 | 61 | 1 | CIN No. : L72200TN2000PLC044560 Email: cs.spl@shriramproperties.com | BOILERPLATE_ID |
| 15 | 66 | 2 | Q1 / FY27 Results |  |
| 16 | 72 | 2 | August 12,2026 |  |
| 17 | 88 | 3 | responsible for such third-party statements and projections.  1 |  |
| 18 | 97 | 4 | 26+ Years of Trust &  52 Completed Projects  32,000+ Happy Customers  Debt Equity of 0.3x |  |
| 19 | 98 | 4 | Excellence  33+ msf Delivered  23% Referral Volumes^  CRISIL A- (Positive) Rated |  |
| 20 | 103 | 4 | ^FY26 Sales volume contribution | FOOTNOTE_MARKER |
| 21 | 109 | 4 | 2 |  |
| 22 | 113 | 5 | Q1/ FY27 Performance Highlights |  |
| 23 | 115 | 5 | 3 |  |
| 24 | 119 | 6 | Q1 FY27: Strong Operational Start; Strengthening Growth Visibility |  |
| 25 | 129 | 6 | •  Bengaluru and Pune approvals are progressing well, on track for multiple launches in early H2 |  |
| 26 | 134 | 6 | •  FY26's amicable resolution continues to unlock monetization opportunities and support accelerated launches |  |
| 27 | 141 | 6 | Q1 performance remained modest, Full year outcome to remain robust with skewed H2 launches and completions  4 |  |
| 28 | 145 | 7 | KPI Snapshot : Q1/ FY27 |  |
| 29 | 148 | 7 | 10% YoY  4%YoY  8% YoY  7% YoY |  |
| 30 | 149 | 7 | Q1 KPI |  |
| 31 | 154 | 7 | 484  0.85  365  690 |  |
| 32 | 158 | 7 | Q1 P&L |  |
| 33 | 163 | 7 | 271  56  42  11 |  |
| 34 | 168 | 7 | •  Revenue growth moderated due to (i) large handovers base of Q4 and (ii) Skewed handover mix towards Kolkata projects |  |
| 35 | 169 | 7 | •  EBITDA flat; Pre-tax profit marginally higher at ₹18 Crs and Net Profit at ₹11 Crs |  |
| 36 | 170 | 7 | •  Robust revenue momentum through second half of FY27, supported by strong handover pipeline visibility |  |
| 37 | 171 | 7 | ________________  5 | FOOTNOTE_MARKER |
| 38 | 172 | 7 | Note: Data presented herein reflects aggregate for the Company, covering all projects under all development formats viz., Own, JV/JDA and DM; 1 msf = Million Square Feet; | FOOTNOTE_MARKER |
| 39 | 176 | 8 | Performance Highlights: Q1/ FY27 |  |
| 40 | 181 | 8 | • Good start to FY27 with 3 launches —2 new  • Revenue recognition driven by legacy  • Added one new project (~0.7 msf) with an |  |
| 41 | 182 | 8 | projects and a new phase launch  Kolkata projects (~40% of Q1 revenues)  estimated GDV potential of ₹ 650 Crs, |  |
| 42 | 183 | 8 | • More launches in H2; on-track for FY  • Revenue stood at ₹271 Crs, while EBITDA  further strengthening the development |  |
| 43 | 184 | 8 | guidance  and PAT were ₹42 Crs and ₹11 Crs,  pipeline |  |
| 44 | 186 | 8 | • Highest-ever Q1 sales at ₹484 Crs (0.85 msf  respectively  • Projects aggregating over 7 msf are |  |
| 45 | 189 | 8 | • Collections grew 8% YoY to ₹365 Crs  prominently in H2  Successful launch of plots and villas in quick |  |
| 46 | 191 | 8 | • Handover of 690 units. Healthy handover |  |
| 47 | 192 | 8 | structural; Margins to recover during H2  value of monetization of Kolkata land bank |  |
| 48 | 203 | 8 | 6 |  |
| 49 | 207 | 9 | Q1 FY27 Launches – Strong Launch Momentum |  |
| 50 | 208 | 9 | Launches – Q1 FY27 |  |
| 51 | 210 | 9 | Project details  Region  Launch type  Product  Q1 Launches - Strategic Highlights |  |
| 52 | 212 | 9 | Shriram Stellar  Chennai  New  Apartment  0.3  0.3 |  |
| 53 | 214 | 9 | Shriram Southbrook  Kolkata  New  Plots  0.4  0.4  ➢ Our premium residential project offering at |  |
| 54 | 215 | 9 | Shriram Green Meadows  Chennai  Phase  Apartment  0.2  0.2  Koyambedu, Chennai |  |
| 55 | 217 | 9 | Total  0.9  0.9 |  |
| 56 | 219 | 9 | End June launch, hence limited impact in Q1 |  |
| 57 | 222 | 9 | ➢ ~20% of project sold during launch week |  |
| 58 | 230 | 9 | ➢ Exceptional launch response with ~55% of |  |
| 59 | 231 | 9 | inventory sold within 30 days of launch. |  |
| 60 | 235 | 9 | Premiumization and portfolio diversification led launches, backed by strong customer demand  7 |  |
| 61 | 239 | 10 | High Powered launch highlights in Chennai & Kolkata during Q1 |  |
| 62 | 245 | 10 | ❖ 135 Units, ₹~320 Crs GDV  ❖ 296 Units, ₹~130 Crs GDV |  |
| 63 | 247 | 10 | greenery and seamless connectivity in heart of Koyambedu  spanning 16 acres, featuring land parcels with six exclusive |  |
| 64 | 249 | 10 | 8 |  |
| 65 | 254 | 11 | Project Pipeline (msf)  BD Pipeline likely addition in next 3-6 months |  |
| 66 | 255 | 11 | 33.7 | CHART_LABEL |
| 67 | 256 | 11 | Upcoming – 17.7 msf | CHART_LABEL |
| 68 | 258 | 11 | Ongoing – 16.0 msf  17.7  Project Area  GDV Additon | CHART_LABEL |
| 69 | 259 | 11 | 16.0 | CHART_LABEL |
| 70 | 261 | 11 | 8.7 | CHART_LABEL |
| 71 | 262 | 11 | 6.7 | CHART_LABEL |
| 72 | 263 | 11 | 5.4  5.2 | CHART_LABEL |
| 73 | 265 | 11 | 2.3 | CHART_LABEL |
| 74 | 266 | 11 | 1.6 | CHART_LABEL |
| 75 | 267 | 11 | 2.8  7.3+  6,000+ | CHART_LABEL |
| 76 | 268 | 11 | 1.0 | CHART_LABEL |
| 77 | 272 | 11 | #  9  6  3  3  21  7  9  1  3  20  41 | CHART_LABEL |
| 78 | 274 | 11 | Pipeline Unsold GDV  Upcoming Projects 17.7 msf GDV |  |
| 79 | 275 | 11 | Project Area  Unsold GDV  GDV  ✓ 1 Project with GDV potential of ₹ 650+ Crs added |  |
| 80 | 278 | 11 | ✓ 7+ msf addition progressing well, likely addition in next |  |
| 81 | 279 | 11 | Ongoing Projects  16.0  - Own  4,910  3-6 months |  |
| 82 | 281 | 11 | Less: Sold  13.1  - JDA  4,850  ✓ Pune Pipeline addition gaining momentum |  |
| 83 | 283 | 11 | Unsold  2.9  1,970  - JV  580  ✓ 20+ msf under various stages of evaluation to enhance |  |
| 84 | 285 | 11 | Add: Upcoming Projects  17.7  11,560  - DM  1,220  objective during the year |  |
| 85 | 287 | 11 | Total GDV Potential  20.6  13,530  Total GDV – Upcoming Projects  11,560 |  |
| 86 | 291 | 11 | Management remain confident and committed to nearly double upcoming project pipeline in 18-24 months |  |
| 87 | 292 | 11 | 9 |  |
| 88 | 296 | 12 | Financial Highlights : Q1/FY27 |  |
| 89 | 298 | 12 | 10 |  |
| 90 | 302 | 13 | Financial Highlights: Profit & Loss – Q1/FY27 |  |
| 91 | 303 | 13 | Particulars (₹ Crs)  Q1 FY27  Q1 FY26  Q4 FY26  FY26 |  |
| 92 | 304 | 13 | Income from Operations  224.3  242.3  640.9  1,267.4 |  |
| 93 | 305 | 13 | ✓ Revenues at ₹ 271 Crs |  |
| 94 | 306 | 13 | Other Operating Revenues  39.3  12.4  15.0  59.6 |  |
| 95 | 307 | 13 | up +4% YoY |  |
| 96 | 308 | 13 | Total Operating Revenues  263.6  254.7  655.9  1,327.0 |  |
| 97 | 309 | 13 | Other Income  7.5  6.8  6.8  29.9 |  |
| 98 | 310 | 13 | Total Revenues  271.1  261.5  662.7  1,356.9 |  |
| 99 | 311 | 13 | ✓ ₹ 56 Crs Gross Profit |  |
| 100 | 312 | 13 | Cost of Revenue  168.3  160.7  459.9  902.2 |  |
| 101 | 313 | 13 | ✓ 25% Gross Profit Margin |  |
| 102 | 314 | 13 | Employee Benefit Expense  26.9  25.0  25.5  105.3 |  |
| 103 | 315 | 13 | Other Expenses  34.0  34.2  68.5  172.6 |  |
| 104 | 316 | 13 | Total expenses  229.2  219.9  553.9  1,180.1 |  |
| 105 | 317 | 13 | EBITDA  41.9  41.6  108.8  176.8  ✓ EBITDA at ₹ 42 Crs |  |
| 106 | 318 | 13 | Finance costs  21.2  22.3  18.9  86.2 |  |
| 107 | 319 | 13 | - Interest expense & other finance cost  21.2  20.8  18.1  80.6 |  |
| 108 | 320 | 13 | - Unwinding Impact (non-cash / GoWB Royalty)  -  1.5  0.8  5.6 | ZERO_STANDING |
| 109 | 322 | 13 | Depreciation  2.6  2.3  2.6  10.0 |  |
| 110 | 324 | 13 | Profit Before Tax and Share of JVs  18.1  17.0  87.3  80.6 |  |
| 111 | 325 | 13 | Add: Share of profit/(loss) of JVs  (3.9)  4.9  (17.5)  (2.6) |  |
| 112 | 326 | 13 | Less: Tax expense  (3.2)  1.3  (8.7)  (22.8)  ✓ Pre-tax profit marginally higher |  |
| 113 | 327 | 13 | ✓ Net Profit at ₹ 11 Crs |  |
| 114 | 328 | 13 | Net Profit  11.0  20.6  78.5  100.8 |  |
| 115 | 332 | 13 | •  Revenue growth remained modest coming on the back of aggressive handovers achieved during Q4 FY26 and skewed Q1 product mix towards lower |  |
| 116 | 334 | 13 | •  Margin impact largely attributable to product mix rather than structural factors  11 |  |
| 117 | 338 | 14 | Financial Highlights: Profit & Loss – Q1/FY27 (continued) |  |
| 118 | 339 | 14 | o Revenue growth remained modest, reflecting limited scheduled project completions during Q1 and continued revenue recognition |  |
| 119 | 342 | 14 | o Q1 revenues were primarily driven by spill-over handovers from FY26 completed projects and recently completed Kolkata projects— |  |
| 120 | 345 | 14 | o Gross Profit stood at ₹ 56 Crs, with EBITDA at ₹ 42 Crs; margins at 25% and 15%, respectively |  |
| 121 | 349 | 14 | o JV loss stood at ₹ 4 Crs in Q1 FY27, reflecting higher sales and administrative expenses at 122 West project partly offset by |  |
| 122 | 352 | 14 | o Finance costs remained flat, supported by the cessation of non-cash charges relating to the 4% non-compete fee in Kolkata |  |
| 123 | 356 | 14 | o Net Profit stood at ₹ 11 Crs in Q1, with scheduled project completions providing strong visibility for improving revenue and earnings |  |
| 124 | 357 | 14 | momentum through the balance of FY27 |  |
| 125 | 362 | 14 | Steady start to FY27, with strong visibility on scheduled project completions, financial momentum to remain strong for the year. |  |
| 126 | 363 | 14 | 12 |  |
| 127 | 367 | 15 | Consolidated Cash Flows: Q1/FY27 (Excl. DM & JV cashflows) |  |
| 128 | 369 | 15 | Particulars (₹ In Crs)  Q1 FY27  Q1 FY26  FY26  Collection Trends (₹ In Crs) |  |
| 129 | 371 | 15 | Operating Inflows  229  221  1,049 |  |
| 130 | 372 | 15 | Construction  (94)  (111)  (434)  1,661 | CHART_LABEL |
| 131 | 374 | 15 | Marketing & Admin Overheads  (54)  (53)  (248)  196 | CHART_LABEL |
| 132 | 376 | 15 | Other Operating outflows  (27)  (33)  (96)  393 | CHART_LABEL |
| 133 | 377 | 15 | 365 | CHART_LABEL |
| 134 | 378 | 15 | Operating Outflows  (175)  (197)  (778)  338 | CHART_LABEL |
| 135 | 379 | 15 | 60 | CHART_LABEL |
| 136 | 380 | 15 | 39 | CHART_LABEL |
| 137 | 381 | 15 | Cash Flow from Operations  54  24  271  100  82 | CHART_LABEL |
| 138 | 382 | 15 | Loan Drawls  106  20  482  1,072 | CHART_LABEL |
| 139 | 384 | 15 | Loan Repayment  (56)  (97)  (519)  205  217 | CHART_LABEL |
| 140 | 386 | 15 | Net flow from Borrowings  50  (77)  (37) | CHART_LABEL |
| 141 | 387 | 15 | Q1FY27  Q1FY26  FY26 |  |
| 142 | 388 | 15 | Interest expense, net  (17)  (15)  (63) | CHART_LABEL |
| 143 | 390 | 15 | Other financing cashflows  48  10  53 | CHART_LABEL |
| 144 | 391 | 15 | Cash Flow from Financing  81  (82)  (47) | CHART_LABEL |
| 145 | 393 | 15 | FCF Before New Project Investment  135  (58)  224 | CHART_LABEL |
| 146 | 394 | 15 | 372 | CHART_LABEL |
| 147 | 395 | 15 | 273 | CHART_LABEL |
| 148 | 396 | 15 | Less: New Project Investment  (88)  (75)  (372) | CHART_LABEL |
| 149 | 397 | 15 | 224 | CHART_LABEL |
| 150 | 398 | 15 | Net Free Cash flow  47  (133)  (148) | CHART_LABEL |
| 151 | 399 | 15 | Opening Cash & Cash Equivalents  172  320  320  156 | CHART_LABEL |
| 152 | 400 | 15 | 135 | CHART_LABEL |
| 153 | 401 | 15 | Closing Cash & Cash Equivalents  219  187  172  143 | CHART_LABEL |
| 154 | 403 | 15 | 86  88 | CHART_LABEL |
| 155 | 407 | 15 | ✓ New project investment of ₹ 88 Crs during Q1 FY27  FY24  FY25  FY26  Q1 FY27  FY24  FY25  FY26  Q1 FY27 | CHART_LABEL |
| 156 | 411 | 15 | Strategic cash deployment towards project execution and new investments to drive future cash flow generation  13 |  |
| 157 | 418 | 16 | ✓ Comfortable debt position with Net Debt of ₹ 432 Crs |  |
| 158 | 419 | 16 | Particulars (₹ in Crs)  Jun’26  Mar’26  Mar’25  Mar’24  ✓ Debt-Equity remains healthy at 0.3x |  |
| 159 | 420 | 16 | Gross External Debt1  651  610  646  631  ✓ Cost of debt stood ~11+% and remains competitive |  |
| 160 | 421 | 16 | Cash & Cash Equivalents  219  172  320  190  ✓ Cost of debt remains competitive and gained the benefit of rate |  |
| 161 | 422 | 16 | Net Debt  432  438  326  441  reductions |  |
| 162 | 423 | 16 | Total Equity  1471  1,460  1,356  1,277  ✓ Backed by A- Positive outlook credit rating from CRISIL |  |
| 163 | 424 | 16 | Net Debt/Equity  0.29  0.30  0.24  0.35 |  |
| 164 | 428 | 16 | 631  646  651 | CHART_LABEL |
| 165 | 429 | 16 | 610 | CHART_LABEL |
| 166 | 430 | 16 | 0.35 | CHART_LABEL |
| 167 | 431 | 16 | 441  438  432  0.30  0.29 | CHART_LABEL |
| 168 | 432 | 16 | 0.24 | CHART_LABEL |
| 169 | 433 | 16 | 326 | CHART_LABEL |
| 170 | 438 | 16 | Mar'24  Mar'25  Mar'26  Jun'26  Mar'24  Mar'25  Mar'26  Jun'26 | CHART_LABEL |
| 171 | 445 | 16 | 1 As per consolidated financial statements excluding inter-company debt from JVs | FOOTNOTE_MARKER |
| 172 | 446 | 16 | 14 |  |
| 173 | 450 | 17 | FY27 Guidance & Outlook |  |
| 174 | 451 | 17 | Artist’s impression of Shriram Spectrum, Pune  15 |  |
| 175 | 455 | 18 | FY27 Outlook: Guidance Remains Unchanged |  |
| 176 | 461 | 18 | 5.0-5.5  3,300-3,500  2,100-2,200  3,750-3,800 |  |
| 177 | 464 | 18 | 20%-33% YoY  40% - 49% YoY  26% - 32% YoY  8% - 10% YoY |  |
| 178 | 471 | 18 | 7-8  4.0-4.5  7.0-8.0  5,000-6,000 |  |
| 179 | 476 | 18 | Management confidence underpinned by an impressive H2 launch lineup and on-track FY27 project completions |  |
| 180 | 477 | 18 | ❑  FY27 KPIs positioned to outperform FY26, backed by scheduled launches and project completions |  |
| 181 | 478 | 18 | ❑  FY27 guidance remains firmly on track, supported by diversified sales across key markets |  |
| 182 | 480 | 18 | 16 |  |
| 183 | 484 | 19 | FY27 New Project Launch Calendar : 10+ New Launch Potential |  |
| 184 | 485 | 19 | New Project Launches – FY27 |  |
| 185 | 491 | 19 | Kolkata Plots  Kolkata  Plots  0.42  0.42  Q1  Done  Launched |  |
| 186 | 492 | 19 | Koyambedu  Chennai  Apartment  0.26  0.26  Q1  Done  Launched |  |
| 187 | 493 | 19 | Gateway C Zone  Chennai  Apartment  0.91  0.91  Q2  Q2  Plans submitted, Approvals awaited |  |
| 188 | 494 | 19 | Manjari  Pune  Apartment  2.30  1.00  Q2  Q3  Approvals awaited, Documentation linked to approvals |  |
| 189 | 495 | 19 | Bannerghatta Road  Bangalore  Villament  0.30  0.30  Q3  Q3  Plans submitted, Approvals awaited |  |
| 190 | 496 | 19 | Yelahanka  Bangalore  Villa  0.19  0.19  Q3  Q3  Plans submitted, Approvals awaited |  |
| 191 | 497 | 19 | Hinjewadi  Pune  Apartment  0.69  0.69  Q3  Q3  Plan submission in progress |  |
| 192 | 498 | 19 | Yelahanka  Bangalore  Apartment  0.57  0.57  Q4  Q4  Plan submission in progress |  |
| 193 | 499 | 19 | Yelahanka  Bangalore  Rowhouses  0.52  0.52  Q4  Q4  Plan submission in progress |  |
| 194 | 500 | 19 | Doddagubbi  Bangalore  Apartment  0.56  0.56  Q4  Q4  Plan submission in progress |  |
| 195 | 501 | 19 | Sarjapura  Bangalore  Apartment  0.51  0.51  Q4  Q4  Approval works commenced |  |
| 196 | 502 | 19 | 7.23  5.93 |  |
| 197 | 504 | 19 | •  Approval Process progressing steadily, scheduled Bangalore launches during H2 to contribute significantly for FY27 |  |
| 198 | 505 | 19 | •  ~6msf new supply along with new phase launches in existing projects to drive sales growth momentum in FY27 |  |
| 199 | 506 | 19 | •  With most of the project approval work progressing steadily, approval delay insulation provided to avoid slippages  17 |  |
| 200 | 510 | 20 | FY27 Handovers: High Confidence on FY targets driven by On-track Project Progress |  |
| 201 | 511 | 20 | Revenue recognition from recent completions likely during remainder of FY27 |  |
| 202 | 515 | 20 | 5+Projects, 410+ Units ₹ 400+ Crs | LAYOUT_AMBIGUOUS |
| 203 | 516 | 20 | Q2 OC Projects – Revenue potential  H2 OC Projects – Revenue potential | LAYOUT_AMBIGUOUS |
| 204 | 519 | 20 | 2Projects, 400+ Units ₹160+ Crs  5+Projects, 2,100+ Units ₹1,000+ Crs | LAYOUT_AMBIGUOUS |
| 205 | 524 | 20 | 2,900+ Units ₹ 1,560+ Crs | LAYOUT_AMBIGUOUS |
| 206 | 526 | 20 | Proactive planning and with e-Khata buffers already factored, FY27 revenue recognition to remain robust  18 |  |
| 207 | 530 | 21 | Our Mission FY28 – On Steady Trajectory for Achieving |  |
| 208 | 534 | 21 | 33.7 msf | CHART_LABEL |
| 209 | 537 | 21 | 16.0 msf  17.7 msf | CHART_LABEL |
| 210 | 541 | 21 | 13.1 msf  2.9 msf  17.4 msf | CHART_LABEL |
| 211 | 546 | 21 | 7.2 msf  5.9 msf  2.9 msf  17.4 msf | CHART_LABEL |
| 212 | 547 | 21 | FY28 Mission Target  Revenue |  |
| 213 | 555 | 21 | •  Sales Value:  ₹ 5,000+ Crs |  |
| 214 | 556 | 21 | •  Revenues:  ₹ 2,500+ Crs |  |
| 215 | 558 | 21 | •  Earnings (PBT): ₹ 250+ Crs |  |
| 216 | 559 | 21 | 8.8 msf  17.4 msf | CHART_LABEL |
| 217 | 560 | 21 | ₹ 4,800+ Crs  ₹ 9,000+ Crs | CHART_LABEL |
| 218 | 562 | 21 | ~₹ 14,000 Crs of Revenue to be recognised in 5-7 years |  |
| 219 | 563 | 21 | 19 |  |
| 220 | 565 | 21 | [CHART, page 21, OCR text: circular "MISSION 1234" graphic beside the funnel chart. Visual inspection (tesseract could not render the curved text) reads four ring-labeled segments, clockwise from top: "Oneness", "Doubling Sales", "Tripling Revenue", "Quadruple Profit". Qualitative mission-pillar labels only; no numeric values attached beyond the "1234" sequence marker.] | NO_NUMERIC_OCR/OCR_GRAPHIC |
| 221 | 573 | 22 | Villas, Kolkata Bangalore  20 20 | OCR_ARTIFACT_DUP_FOOTER |
| 222 | 582 | 23 | 21 |  |
| 223 | 584 | 23 | [OCR page 23: page under 100 extracted characters, rasterised at 150 DPI and OCR'd with tesseract. OCR output: "Annexures" / page footer "21" (printed slide number). Confirms section-divider slide with no additional numeric or textual content beyond what pdftotext already captured.] | OCR_FALLBACK_PAGE |
| 224 | 587 | 24 | Annexure-1: Projects Snapshot by Development Models |  |
| 225 | 598 | 24 | ✓ 9 projects  ✓ 26 projects  ✓ 5 projects  ✓ 12 projects |  |
| 226 | 599 | 24 | ✓ 8.7 msf.  ✓ 12.9 msf.  ✓ 4.9 msf.  ✓ 6.3 msf. |  |
| 227 | 602 | 24 | ✓ 9 Projects  ✓ 6 Projects  ✓ 3 Projects  ✓ 3 Projects |  |
| 228 | 603 | 24 | ✓ 6.7 msf.  ✓ 5.4 msf.  ✓ 2.3 msf.  ✓ 1.6 msf. |  |
| 229 | 606 | 24 | ✓ 7 Projects  ✓ 9 Projects  ✓ 1 Project  ✓ 3 Project |  |
| 230 | 607 | 24 | ✓ 8.7 msf.  ✓ 5.2 msf.  ✓ 1.0 msf.  ✓ 2.8 msf. |  |
| 231 | 612 | 24 | 22 |  |
| 232 | 616 | 25 | Annexure-2: Consolidated Cash Flows – With and Without JV Cashflows |  |
| 233 | 618 | 25 | Particulars  SPL Consolidated (CFS)  SPL Enterprise (100%)1 (Excl DM) |  |
| 234 | 620 | 25 | Amount in Rs. Crs  Q1 FY27  Q1 FY26  FY26  Q1 FY27  Q1 FY26  FY26 |  |
| 235 | 621 | 25 | Operating Inflow  229  221  1,049  329  300  1,427 |  |
| 236 | 622 | 25 | Construction  (94)  (111)  (434)  (138)  (143)  (629) |  |
| 237 | 623 | 25 | Mktg. & Admin Overheads  (54)  (53)  (248)  (59)  (57)  (273) |  |
| 238 | 624 | 25 | Other Operating outflows  (27)  (33)  (96)  (31)  (36)  (110) |  |
| 239 | 625 | 25 | Operating Outflow  (175)  (197)  (778)  (228)  (236)  (1012) |  |
| 240 | 626 | 25 | Cash flow from Operations  54  24  271  101  64  415 |  |
| 241 | 627 | 25 | Loan Drawls  106  20  482  101  26  512 |  |
| 242 | 628 | 25 | Loan Repayment  (56)  (97)  (519)  (81)  (113)  (593) |  |
| 243 | 629 | 25 | Net flow from Borrowings  50  (77)  (37)  20  (87)  (81) |  |
| 244 | 630 | 25 | Interest expense, net  (17)  (15)  (63)  (22)  (22)  (91) |  |
| 245 | 631 | 25 | Other financing cashflows  48  10  53  (13)  (16)  21 |  |
| 246 | 632 | 25 | Cash flow from Financing  81  (82)  (47)  (15)  (125)  (151) |  |
| 247 | 633 | 25 | FCF before New Project Inv.  135  (58)  224  86  (61)  264 |  |
| 248 | 634 | 25 | Less: New Project Inv.  (88)  (75)  (372)  (89)  (79)  (390) |  |
| 249 | 635 | 25 | Net Free Cash flow  47  (133)  (148)  (3)  (140)  (126) |  |
| 250 | 636 | 25 | Opening Cash & Cash Equiv.  172  320  320  263  389  389 |  |
| 251 | 637 | 25 | Closing Cash & Cash Equiv.  219  187  172  260  249  263 |  |
| 252 | 640 | 25 | 1 Enterprise Cashflows include SPL CFS Cashflows plus 100% share of JVs. Excludes DM project cashflows | FOOTNOTE_MARKER |
| 253 | 641 | 25 | 23 |  |
| 254 | 655 | 26 | CIN – L72200TN2000PLC044560  CIN - U74140MH2010PTC204285 | BOILERPLATE_ID |
| 255 | 659 | 26 | +91 98214 38864 / +91 91687 23907 | BOILERPLATE_ID |
| 256 | 665 | 26 | 24 |  |

---
## SECTION 3: FOOTNOTES & FINE-PRINT DISCLAIMERS QUALIFYING A HEADLINE NUMBER (6 items)
| # | Slide | Marker line(s) | Text line | Footnote text (verbatim/summarized) | Qualifies | Flags |
|---|-------|------------------|-----------|----------------------------------------|-----------|-------|
| F0 | 3 | n/a (no typographic marker) | 76-88 | Full forward-looking-statements / no-reliance / no-representation-or-warranty legal disclaimer covering the entire Presentation. | Every headline number in slides 4-26 (the disclaimer explicitly disclaims accuracy/completeness of all figures). | NO_TYPOGRAPHIC_MARKER — a full-page narrative disclaimer, not a footnote symbol; found only by manual sweep, excluded from the grep-based footnote_markers count test (Section 0) for that reason, listed here for completeness. |
| F1 | 4 | 102 | 103 | "^FY26 Sales volume contribution" | "23% Referral Volumes^" (line 98) | FOOTNOTE_MARKER |
| F2 | 7 | 171 | 172 | "Note: Data presented herein reflects aggregate for the Company, covering all projects under all development formats viz., Own, JV/JDA and DM; 1 msf = Million Square Feet;" | All KPI Snapshot tiles on slide 7 (Sales Value/Volume/Collections/Handovers, Revenues/Gross Profit/EBITDA/Net Profit) | FOOTNOTE_MARKER |
| F3 | 13 | 329 | 330 | "* Other Operating Revenues include fair value gains in JV Projects and monetization of development rights etc." | "Other Operating Revenues" line item, ₹39.3 Crs Q1FY27 (line 306) | FOOTNOTE_MARKER |
| F4 | 16 | 444 | 445 | "1 As per consolidated financial statements excluding inter-company debt from JVs" | "Gross External Debt¹" row, ₹651 Crs Jun'26 (line 420) | FOOTNOTE_MARKER |
| F5 | 25 | 639 | 640 | "1 Enterprise Cashflows include SPL CFS Cashflows plus 100% share of JVs. Excludes DM project cashflows" | "SPL Enterprise (100%)¹ (Excl DM)" column header (line 618) | FOOTNOTE_MARKER |

Count test basis: F1-F5 (5 items) are the typographically marked footnotes reconciled in
the COUNT TEST header (grep on the underscore separator rule `^\s*_{3,}` = 5, paired
1:1 with footnote text by manual sweep = 5, match yes). F0 is an additional fine-print
disclaimer found by manual sweep only — it has no footnote symbol to grep for (it is not a
footnote to a specific number, it is a page-length disclaimer covering the whole deck) —
carried here as a 6th item rather than folded into the reconciled count, so the count test
stays clean and auditable.

---
## SECTION 4: DROPPED_SLIDE CHECK — NOT PERFORMED (prior deck unavailable)
Prior-quarter ledger path supplied to this run: NONE. No prior-quarter investor
presentation ledger exists in the repo for SPROP to diff against. Consequently:
- The DROPPED_SLIDE check required by the ENUMERATE — INVESTOR PRESENTATION recipe
  (item 3: "Every slide present in the prior quarter's deck but absent now =
  DROPPED_SLIDE") could not be executed this run.
- This is recorded as a coverage gap, not silently skipped: A3/A4 should treat the
  DROPPED_SLIDE dimension as UNTESTED for Q1 FY27, not as "no slides were dropped."
  The moment a prior-quarter presentation ledger becomes available (e.g. Q4 FY26 deck,
  if enumerated retroactively), this diff should be run before any claim of disclosure
  continuity is made.
- Flag: `DROPPED_SLIDE_CHECK_UNAVAILABLE`.

---
## SECTION 5: FLAG SUMMARY
| Flag | Count | Where |
|------|-------|-------|
| BOILERPLATE_ID | 16 | Slide 1 (14 lines: date, addresses, scrip codes, Reg 30 ref, signature date, ACS no., registered-office address, phone/fax, CIN+email) and Slide 26 (2 lines: dual CIN, IR-advisor phone numbers) |
| ZERO_STANDING | 1 | Slide 13, line 320 — "Unwinding Impact (non-cash / GoWB Royalty)" shows "-" for Q1 FY27 while non-zero in Q1 FY26 (1.5), Q4 FY26 (0.8) and FY26 (5.6); the dash is not dropped from the ledger |
| CHART_LABEL | 50 | Slide 11 (pipeline bar chart, 12 rows), Slide 15 (Collection Trends + FCF/Investment trend charts, 25 rows), Slide 16 (Gross/Net Debt + Net Debt-Equity trend charts, 7 rows), Slide 21 (funnel chart, 6 rows) — see Section 2 for exact line-level attribution |
| LAYOUT_AMBIGUOUS | 4 | Slide 20, lines 515/516/519/524 — Q2 OC vs H2 OC revenue-potential values; text-extraction order does not cleanly map value to column, flagged for A3/A4 to verify against the source PDF's visual layout before quoting a specific column figure |
| NO_NUMERIC_OCR/OCR_GRAPHIC | 1 | Slide 21, line 565 — "MISSION 1234" circular graphic; OCR confirms 4 qualitative pillar labels (Oneness / Doubling Sales / Tripling Revenue / Quadruple Profit), no numeric content beyond the "1234" sequence marker itself |
| OCR_FALLBACK_PAGE | 1 | Slide 23, line 584 — full-page OCR fallback (native text < 100 chars); OCR confirms section-divider only |
| OCR_ARTIFACT_DUP_FOOTER | 1 | Slide 22, line 573 — duplicated "20 20" footer digit, an extraction artifact |
| FOOTNOTE_MARKER | 10 | Section 3, items F1-F5 (marker + text lines: 102/103, 171/172, 329/330, 444/445, 639/640) |
| NO_TYPOGRAPHIC_MARKER | 1 | Section 3, item F0 — slide 3 full-page disclaimer |
| DROPPED_SLIDE_CHECK_UNAVAILABLE | 1 | Section 4 — no prior-quarter deck supplied |

END OF LEDGER
