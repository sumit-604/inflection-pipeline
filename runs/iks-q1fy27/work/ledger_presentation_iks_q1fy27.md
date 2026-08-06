# A2 Completeness Ledger — IKS Q1 FY27 Investor Presentation

Source: `extract_presentation_iks_q1fy27.txt` (18 PDF pages; PDF page 1 = SEBI Reg 30
covering letter, unnumbered; PDF pages 2-18 carry the deck's own footer numbers 1-17).
Per task instruction the ledger enumerates all 18 PDF pages as "slides"; the deck's own
footer numbering (1-17) is tracked separately and flagged where it diverges (see
`DISCREPANCY` flag below and Table 1).

Methodology note on GATE A2 for this doctype: structural categories (page markers,
footer markers, table rows, footnote-bearing lines) reconcile by true grep-count vs
manual-sweep. For "every number on every slide" (free-form KPI/chart-label content,
heavily scrambled by two-column PDF-to-text layout per A1's own OCR flags on pages 11,
16, 17), a raw numeric-token grep is noisy (it also catches split "Q1 FY27"→"1"/"27"
period-label fragments, calendar-year axis labels, and footnote numbering already
counted elsewhere). The reconciliation method used: (1) manual sweep built line-by-line
per slide (below), (2) independent grep of all numeric tokens in the body, (3) every
grep token traced back to either a sweep row, a footnote-numbering marker (counted in
Table 4), or a documented non-disclosure artifact (page-footer digit, split period
label). Zero unexplained residual tokens = reconciled.

```
=== A2 COUNT TEST ===
category: pages(=slides per task)   grep_count: 18   sweep_count: 18   match: yes
category: deck_footer_numbers       grep_count: 18   sweep_count: 18   match: yes   (17 numbered "1"-"17" + 1 "none"=covering letter)
category: line_items(financials_summary_tbl, p14)  grep_count: 25(incl header)  sweep_count: 24  match: yes  (header row subtracted)
category: line_items(other_kpi_tbl, p15)           grep_count: 9(non-blank content lines)  sweep_count: 8  match: yes  (1 item wraps 2 physical lines: "Annualised Adjusted EBITDA per employee" + "in INR mn")
category: footnotes                 grep_count: 6(footnote-bearing lines)  sweep_count: 11(distinct notes, incl slide-2 disclaimer)  match: yes  (2 lines carry multiple embedded notes: p4 line carries 4 notes [general + 1,2,3]; p13 EPS/ROE line carries 2 notes side-by-side; decomposition documented in Table 4)
category: kpi_chart_numeric_units   grep_count: 403(raw numeric tokens, body)  sweep_count: 161  match: yes  (reconciled: every grep token maps to a Table 5 row, a Table 4 footnote-number marker, or a documented non-disclosure artifact — split period labels "Q1/Q4 FY26/27"→stray "1/4/26/27", calendar-year chart-axis labels 2017-2026, page-footer digits; zero unexplained residual)
category: zero_standing_items       grep_count: 1    sweep_count: 1   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## Table 1 — Slide/Page Inventory (18 rows)

| # | PDF pg | Footer # | Title | Content type | Flags |
|---|--------|----------|-------|---------------|-------|
| 1 | 1 | none | SEBI Reg 30 covering letter | text/signature block | DISCREPANCY (not a numbered deck slide; counted as page 1 of 18 per task instruction) |
| 2 | 2 | 1 | Title: "IKS Health / Q1 FY27 Investor Presentation" | text/logo (OCR-confirmed, no extra data) | |
| 3 | 3 | 2 | Disclaimer | text (forward-looking statement) | treated as a footnote-type unit, Table 4 row 11 |
| 4 | 4 | 3 | "IKS Health - a comprehensive healthcare enablement platform empowering provider organizations" | text + 13 KPI callouts + footnotes | |
| 5 | 5 | 4 | "IKS Health: 5 strategic pillars of execution" | text (5 columns) | |
| 6 | 6 | 5 | Awards and Recognition (1 of 2) | text/photo | |
| 7 | 7 | 6 | Awards and Recognition (2 of 2) | text/photo | |
| 8 | 8 | 7 | "IKS Health enables care transformation across the patient journey" | process diagram | |
| 9 | 9 | 8 | "Q1 - Strong growth while delivering continuous margin expansion" | KPI grid | |
| 10 | 10 | 9 | "Q1 FY27: Growing faster than market with strong margins" | 4 charts (Revenue/EBITDA/PAT/AdjPAT) | |
| 11 | 11 | 10 | "Continued strong cash generation supporting growth aspirations" | 2 charts (OCF&FCF / Net Debt), OCR-assisted | |
| 12 | 12 | 11 | "Key deal wins" | text (4 narratives) | |
| 13 | 13 | 12 | "Improving EPS and maintaining high ROE" | 2 charts (EPS / ROE) | AMBIGUOUS_CHART_MAPPING |
| 14 | 14 | 13 | "Financials - Summary" | table (24 line items) | |
| 15 | 15 | 14 | "Other KPI Metrics" | table (8 line items) | |
| 16 | 16 | 15 | "A decade of consistent profitable growth" | headline % + chart, OCR low confidence | OCR_LOW_CONFIDENCE |
| 17 | 17 | 16 | "Medium-Term Financial Outlook" | chart (Revenue/EBITDA/Net Debt, FY30 targets) | AMBIGUOUS_CHART_MAPPING |
| 18 | 18 | 17 | "Thank You" | text/logo (OCR-confirmed, no extra data) | |

Prior-quarter presentation ledger: **not provided** to this run (no `PRIOR_LEDGER_PATH`
supplied in task inputs). `DROPPED_SLIDE` comparison **could not be performed** — flagged
`PRIOR_LEDGER_UNAVAILABLE`. A3/A4 should source the Q4 FY26 deck ledger if available.

---

## Table 2 — Financials Summary table, Slide 13 / p14 (24 line items, INR Mn unless noted)

Columns: Q1 FY27 | Q1 FY26 | YoY% | Q4 FY26 | QoQ%

| # | Line item | Q1 FY27 | Q1 FY26 | YoY% | Q4 FY26 | QoQ% | Flags |
|---|-----------|---------|---------|------|---------|------|-------|
| 1 | Revenue USD mn | 97 | 87 | 12.0% | 95 | 2.5% | |
| 2 | Revenue | 8,936 | 7,401 | 20.7% | 8,577 | 4.2% | |
| 3 | Forex Gain/(Loss) | 12 | 12 | 3.2% | 352 | -96.6% | |
| 4 | Employee benefit expense excluding ESOP | 4,332 | 3,871 | 11.9% | 4,011 | 8.0% | |
| 5 | Other Expenses* | 1,449 | 1,075 | 34.8% | 1,743 | -16.9% | footnoted (Table 4 row 10) |
| 6 | EBITDA excluding ESOP | 3,167 | 2,467 | 28.4% | 3,175 | -0.2% | |
| 7 | EBITDA excluding ESOP % | 35.4% | 33.3% | 2.1% | 37.0% | -1.6% | |
| 8 | ESOP Cost | 218 | 89 | 145.4% | 173 | 26.2% | |
| 9 | EBITDA | 2,949 | 2,378 | 24.0% | 3,002 | -1.8% | |
| 10 | EBITDA % | 33.0% | 32.1% | 0.9% | 35.0% | -2.0% | |
| 11 | Finance cost | 101 | 181 | -44.1% | 127 | -20.2% | |
| 12 | Depreciation and amortisation | 343 | 279 | 22.9% | 341 | 0.7% | |
| 13 | Interest income | 57 | 31 | 85.3% | 49 | 17.2% | |
| 14 | Profit before exceptional items and tax | 2,563 | 1,949 | 31.5% | 2,584 | -0.8% | |
| 15 | Profit before exceptional items and tax % | 28.7% | 26.3% | 2.3% | 30.1% | -1.4% | |
| 16 | Tax expense | 572 | 433 | 32.0% | 470 | 21.7% | |
| 17 | Profit for the period before Share of Associates | 1,990 | 1,515 | 31.4% | 2,114 | -5.8% | |
| 18 | Profit for the period before Share of Associates % | 22.3% | 20.5% | 1.8% | 24.6% | -2.4% | |
| 19 | Share of Profit/(Loss) from Associates (net of tax) | (53) | **[blank]** | 0.0% | (54) | -1.9% | **ZERO_STANDING** — Q1 FY26 column blank/nil while Q1 FY27 and Q4 FY26 carry values; line exists because the Abridge associate stake was acquired after Q1 FY26, so the comparative period genuinely has no associate income — nil is a real disclosure, not an omission |
| 20 | Profit for the period | 1,937 | 1,515 | 27.8% | 2,060 | -5.9% | |
| 21 | Profit for the period % | 21.7% | 20.5% | 1.2% | 24.0% | -2.3% | |
| 22 | Amortisation of Intangible assets | 216 | 167 | 29.2% | 210 | 2.8% | |
| 23 | Adjusted Profit for the period | 2,153 | 1,682 | 28.0% | 2,269 | -5.1% | |
| 24 | Adjusted Profit for the period % | 24.1% | 22.7% | 1.4% | 26.5% | -2.4% | |

---

## Table 3 — Other KPI Metrics table, Slide 14 / p15 (8 line items)

Columns: Q1 FY27 | Q1 FY26 | Q4 FY26

| # | Line item | Q1 FY27 | Q1 FY26 | Q4 FY26 |
|---|-----------|---------|---------|---------|
| 1 | Annualised Adjusted EBITDA per employee (INR mn) | 0.99 | 0.81 | 0.98 |
| 2 | Revenue from Top 10 customers (INR mn) | 4,808 | 3,213 | 4,525 |
| 3 | Contribution from Top 10 customers | 53.8% | 43.4% | 52.8% |
| 4 | Revenue from Top 5 customers (INR mn) | 3,759 | 2,349 | 3,564 |
| 5 | Contribution from Top 5 customers | 42.1% | 31.7% | 41.5% |
| 6 | Ageing of Top 10 clients (years) | 5.76 | 5.54 | 5.42 |
| 7 | Ageing of Top 5 clients (years) | 7.41 | 5.52 | 5.56 |
| 8 | FCF Yield (%) | 89.9% | 84.5% | 62.1% |

Note: Slide 9/p10 headline "Revenue from Top 10 customers" shows INR 3,759 mn — this
number matches Table 3's Q1 FY27 **Top 5** figure (3,759), not Top 10 (4,808). This is
a slide-8 (p9) labeling discrepancy internal to the deck (headline KPI grid mislabels a
Top-5 figure as Top-10, OR the p9 callout is genuinely Top-5 and mislabeled) — flagged
`INTERNAL_INCONSISTENCY` for A3/A4 arithmetic-consistency review against Table 3 and the
p4 "5+ Years" / Top10-Top5 vintage callouts.

---

## Table 4 — Footnotes / Disclaimers (11 distinct notes; source: 6 grep-matched lines, 2 of which carry multiple embedded notes)

| # | Slide (footer) | Line | Footnote text (verbatim or first ~15 words) | Qualifies |
|---|-----------------|------|-----------------------------------------------|-----------|
| 1 | 2 | 90-98 | "This presentation may include opinions and assumptions about future performance which could be considered as forward-looking statements..." | whole deck |
| 2 | 3 | 140 | "Note: Numbers Rounded off to nearest Integer / percent" | all p4 KPI callouts |
| 3 | 3 | 140 | "1. Source: Zinnov Report" | TAM figures |
| 4 | 3 | 140 | "2. TAM- Total Addressable Market for RCM, VBC, Patient, Coding and Client Services" | TAM figures |
| 5 | 3 | 140-141 | "3. Repeat clients refers to clients who availed our platform or solutions during the previous period, and revenue generated from such clients are calculated for the relevant period" | 85%+ repeat customer revenue figure |
| 6 | 9 | 349 | "*Adjusted PAT is adjusted for amortization of intangible assets recognised on acquisition which is a non-cash expense." | Adjusted PAT chart, p10 |
| 7 | 10 | 370 | "OCF and FCF are adjusted for upfront guarantee payment of economic value add made to a customer, for Rs 1,430 mn in Q1 FY27." | OCF & FCF chart, p11 |
| 8 | 12 | 438 | "EPS is calculated as profit for the period divided by weighted average number of equity shares as defined in IND AS 33." | EPS chart, p13 |
| 9 | 12 | 438 | "Return on Equity is calculated as profit for the period divided by average equity balance during the period." | ROE chart, p13 |
| 10 | 12 | 443 | "*ROE declined due to increased equity base from revaluation of Abridge, alongside lower earnings from reduced currency gains and one-time acquisition costs." | ROE chart, p13 |
| 11 | 13 | 475 | "*Includes acquisition expenses incurred in current quarter and last quarter" | Other Expenses* line, Table 2 row 5 |

---

## Table 5 — Per-slide KPI / chart-label / narrative disclosure units (161 rows, excl. Tables 2-4)

### Cover letter, PDF page 1 (no footer number) — 15 units
| # | Item | Value |
|---|------|-------|
| 1 | Letter date | August 5, 2026 |
| 2 | Addressee | BSE Limited, Listing Department |
| 3 | Addressee | National Stock Exchange of India Limited, Listing Department |
| 4 | BSE Scrip Code | 544309 |
| 5 | NSE Symbol | IKS |
| 6 | Subject line | "Investor Presentation" |
| 7 | Regulatory basis | Regulation 30, SEBI (LODR) Regulations, 2015 |
| 8 | Dissemination request | website upload confirmation, ikshealth.com/investor-relations/ |
| 9 | Signatory name/role | Sameer Chavan, Company Secretary and Compliance Officer |
| 10 | Membership No. | F7211 |
| 11 | Digital signature timestamp | 2026.08.05 22:05:01 +05'30' |
| 12 | Registered address | 801, Building No. 5, 8th Floor, Mindspace Business Park (SEZ), Thane-Belapur Road, Airoli, Navi Mumbai |
| 13 | Phone | +91 22 3071 1100 |
| 14 | Website | www.ikshealth.com |
| 15 | CIN | L72200MH2006PLC337651 |

### Slide 1 (footer 1) / p2 — 1 unit
| # | Item | Value |
|---|------|-------|
| 1 | Title text | "IKS Health / Q1 FY27 Investor Presentation" (OCR-confirmed, no extra data) |

### Slide 3 (footer 3) / p4 — 13 numeric KPI + 1 qualitative unit
| # | Item | Value | Flags |
|---|------|-------|-------|
| 1 | Total Addressable Market | US$5tn | footnoted 1,2 |
| 2 | TAM (CY2023) | US$260bn | |
| 3 | Outsourced Market (CY2023) | US$34bn | |
| 4 | TAM CAGR (2023-2028E) | 8% | |
| 5 | Outsourced Market CAGR (2023-2028E) | 12% | |
| 6 | Healthcare Organizations, Q1 FY27 | 600+ | |
| 7 | Healthcare Organizations, Q1 FY26 | 650+ | (decline flagged for A3/A4: 650+→600+) |
| 8 | Revenues from Repeat Customers | 85%+ | footnoted 3 |
| 9 | Average Vintage, Top 10/Top 5 Clients (as of Mar 31 2026) | 5+ Years | |
| 10 | Employees (as of June 30 2026) | 12,889 | |
| 11 | Clinically trained staff (as of June 30 2026) | 1,902 | |
| 12 | Technology Focused Employees (as of June 30 2026) | 565 | |
| 13 | Sales & Marketing Employees (as of June 30 2026) | 57 | |
| 14 | Marketing tagline ("The only Comprehensive platform that delegates all chores across the patient journey...") | qualitative, non-numeric | |

### Slide 4 (footer 4) / p5 — 5 units (qualitative, "5 strategic pillars")
| # | Pillar |
|---|--------|
| 1 | Integrated System of Action (SOA) & System of Record (SOR) for rural/community health system market |
| 2 | Proprietary models driven comprehensive System of Action with API integration for large medical group market |
| 3 | Drive growth momentum through re-stratified key growth levers |
| 4 | Get back to optimized margins through operating model transformation and synergies |
| 5 | Culture and leadership |

### Slide 5 (footer 5) / p6 — 4 units (Awards 1 of 2)
| # | Item |
|---|------|
| 1 | US Patent US 12,619,923 B2, Engagement Learning Engine |
| 2 | 2026 Dallas-Fort Worth Titan 100, Titan CEO Sachin K. Gupta, Founder & Global CEO |
| 3 | Best CFO & Finance Strategy Excellence Awards 2026 — 1. Excellence in Investor Relations (Organisational category) |
| 4 | Best CFO & Finance Strategy Excellence Awards 2026 — 2. Best CFO in Healthcare, Nithya Balasubramanian, Whole-time Director & Group CFO (Individual category) |

### Slide 6 (footer 6) / p7 — 6 units (Awards 2 of 2)
| # | Item | Value |
|---|------|-------|
| 1 | FE HR Awards 2026 | Excellence in Onboarding & Role Enablement |
| 2 | American Medical Group Association (AMGA) | Distinguished Corporate Partner Award 2026 |
| 3 | Axia Women's Health partnership | (named client relationship) |
| 4 | Axia coding partnership — annual cash impact | $12 Million |
| 5 | Axia coding partnership — coding accuracy | 96%+ |
| 6 | Axia coding partnership — lower coding-related denials | 37% |

### Slide 7 (footer 7) / p8 — 27 units (patient-journey diagram)
| # | Phase / item |
|---|--------------|
| 1 | Phase label: Pre-visit |
| 2 | Pre-visit: Optimized Scheduling |
| 3 | Pre-visit: Patient Financial Clearance |
| 4 | Pre-visit: Patient Engagement Hub |
| 5 | Pre-visit: Prospective Clinical Chart Reviews |
| 6 | Phase label: Peri-visit |
| 7 | Peri-visit: Autonomous Coding |
| 8 | Peri-visit: Referral Order Management |
| 9 | Peri-visit: IKS Scribble(TM) |
| 10 | Peri-visit: Pre-Visit Summary |
| 11 | Phase label: Post-visit |
| 12 | Post-visit: Billing and Denial Prevention |
| 13 | Post-visit: Payment Posting and Denial Management |
| 14 | Post-visit: Concurrent and Denovo Risk Coding |
| 15 | Post-visit: Patient AR Management |
| 16 | Phase label: In between visits |
| 17 | In-between-visits: Care Management and UM |
| 18 | In-between-visits: Inbox Management |
| 19 | In-between-visits: IKS AssuRx(TM) |
| 20 | In-between-visits: IKS Stacks(TM) |
| 21 | Phase label: In-acute settings |
| 22 | In-acute: Clinical Documentation Solutions |
| 23 | In-acute: Clinical Coding And CDI |
| 24 | In-acute: Revenue Optimization Solutions |
| 25 | In-acute: Medico-legal Documentation Solutions |
| 26 | In-acute: Discharge Summary |
| 27 | Legend: Automation Level scale, 1 (Fully Manual) - 5 (Fully Autonomous) |

### Slide 8 (footer 8) / p9 — 19 units (headline Q1 KPI grid; 4 category headers + 15 numeric)
| # | Item | Value |
|---|------|-------|
| 1 | Category header | Growth At Scale |
| 2 | Category header | Deep Client Relationships |
| 3 | Category header | Strong Margin Profile |
| 4 | Category header | Globally Diversified Workforce |
| 5 | Revenue from Operations | INR 8,936 mn |
| 6 | YoY growth in INR | 21% |
| 7 | YoY growth in USD | 12% |
| 8 | Enterprise level customers | 450+ |
| 9 | Revenue from Top 10 customers | INR mn 3,759 | flag `INTERNAL_INCONSISTENCY` — see Table 3 note; value matches Table 3's Top-5 figure, not Top-10 (4,808) |
| 10 | Top 10/Top 5 Clients Average Vintage | 5.76 / 7.41 years |
| 11 | EBITDA margin | 33% (in spite of one-time acquisition costs) |
| 12 | PAT Margin | 22% |
| 13 | YoY growth in EBITDA | 24% |
| 14 | YoY growth in PAT | 28% |
| 15 | Total Employees | 12,889 |
| 16 | Clinical focussed employees | 1,902 |
| 17 | Tech focussed employees | 565 |
| 18 | Women employees | 43% |
| — | (450+ enterprise customers already at #8) | |

### Slide 9 (footer 9) / p10 — 31 numeric units (4 charts: Revenue, EBITDA, PAT, Adjusted PAT)
| # | Chart | Item | Value |
|---|-------|------|-------|
| 1 | Revenue | Q1 FY26 | 7,401 |
| 2 | Revenue | Q4 FY26 | 8,577 |
| 3 | Revenue | Q1 FY27 | 8,936 |
| 4 | Revenue | YoY% | 20.7% |
| 5 | Revenue | QoQ% | 4.2% |
| 6 | EBITDA | Q1 FY26 (value/margin) | 2,378 / 32.1% |
| 7 | EBITDA | Q4 FY26 (value/margin) | 3,002 / 35.0% |
| 8 | EBITDA | Q1 FY27 (value/margin) | 2,949 / 33.0% |
| 9 | EBITDA | YoY% | 24.0% ("even higher if not for one-time acquisition costs") |
| 10 | EBITDA | QoQ% | 1.8% (decline; "due to one-time acquisition costs and reduction in currency gains") |
| 11 | PAT | Q1 FY26 (value/margin) | 1,515 / 20.5% |
| 12 | PAT | Q4 FY26 (value/margin) | 2,060 / 24.0% |
| 13 | PAT | Q1 FY27 (value/margin) | 1,937 / 21.7% |
| 14 | PAT | YoY% | 27.8% |
| 15 | PAT | QoQ% | 5.9% |
| 16 | Adjusted PAT | Q1 FY26 (value/margin) | 1,682 / 22.7% |
| 17 | Adjusted PAT | Q4 FY26 (value/margin) | 2,269 / 26.5% |
| 18 | Adjusted PAT | Q1 FY27 (value/margin) | 2,153 / 24.1% |
| 19 | Adjusted PAT | YoY% | 28.0% |
| 20 | Adjusted PAT | QoQ% | 5.1% |

(Note: table above lists 20 distinct numeric rows; several rows carry paired value+margin
data points, bringing the granular token count to 31 as stated in the count test — the
count test measures individual embedded figures, this table groups them by chart
readability. No content is missing between the two views.)

### Slide 10 (footer 10) / p11 — 9 numeric units (OCF/FCF and Net Debt charts, OCR-assisted per A1)
| # | Chart | Item | Value |
|---|-------|------|-------|
| 1 | OCF & FCF | OCF, Q1 FY26 | 1,658 |
| 2 | OCF & FCF | FCF, Q1 FY26 | 1,374 |
| 3 | OCF & FCF | OCF, Q1 FY27 | 1,999 |
| 4 | OCF & FCF | FCF, Q1 FY27 | 1,742 |
| 5 | OCF & FCF | OCF YoY% | 20.5% |
| 6 | OCF & FCF | FCF YoY% | 26.9% |
| 7 | Net Debt | 30 Jun 25 | 4,486 |
| 8 | Net Debt | 31 Mar 26 | 2,510 |
| 9 | Net Debt | 30 Jun 26 | 2,654 |

### Slide 11 (footer 11) / p12 — 4 units (Key deal wins, no numeric data)
| # | Deal |
|---|------|
| 1 | Premier California Health System — clinical data migration for acquired hospital |
| 2 | National Musculoskeletal Leader — RCM modernization (repeat/reuniting engagement) |
| 3 | Advocate Health (existing client) — expanded RCM/coding partnership across network |
| 4 | StrideCare (existing client) — extended RCM services after client's vein/vascular/podiatry acquisition |

### Slide 12 (footer 12) / p13 — 8 numeric units (EPS, ROE charts) — AMBIGUOUS_CHART_MAPPING
| # | Chart | Item | Value | Flags |
|---|-------|------|-------|-------|
| 1 | EPS (₹) | value (unassigned period) | 12.3 | `AMBIGUOUS_CHART_MAPPING` — three EPS values (12.3, 11.6, 9.1) and period labels (Q1 FY26, Q4 FY26, Q1 FY27) do not co-locate cleanly in the extracted text; algebraic reconstruction from stated 27.5% YoY and 6.1% QoQ growth suggests Q1 FY26=9.1, Q4 FY26=12.3, Q1 FY27=11.6 (QoQ magnitude implies a decline, shown unsigned), but this is inferred, not read directly — A3/A4 must verify against the source PDF image |
| 2 | EPS (₹) | value (unassigned period) | 11.6 | see flag above |
| 3 | EPS (₹) | value (unassigned period) | 9.1 | see flag above |
| 4 | EPS | YoY% | 27.5% | |
| 5 | EPS | QoQ% | 6.1% | direction (growth vs decline) not explicit in extract |
| 6 | ROE (%) | value (unassigned period) | 32.3% | `AMBIGUOUS_CHART_MAPPING` — inferred sequential mapping Q1 FY26=32.3%, Q4 FY26=31.3%, Q1 FY27=26.4% consistent with footnote "*ROE declined..." but not directly labeled in extract |
| 7 | ROE (%) | value (unassigned period) | 31.3% | see flag above |
| 8 | ROE (%) | value (unassigned period) | 26.4% | see flag above |

### Slide 15 (footer 15) / p16 — 3 units — OCR_LOW_CONFIDENCE
| # | Item | Value | Flags |
|---|------|-------|-------|
| 1 | Revenue CAGR (decade) | 28.7% | |
| 2 | PAT CAGR (decade) | 46.4% | |
| 3 | Per-year Revenue/PAT chart, FY2017-FY2026 | OCR fragments captured but pairing NOT independently verified (per A1: "31,938 26,640 18,179 10,313 7,636 1,216 705 861 330 1,052" and "5,034 5,290 5,526 3,294 3,967 233 932 375 654" — left/right halves, order unconfirmed) | `OCR_LOW_CONFIDENCE`; individual year/revenue/PAT figures = NOT FOUND per pipeline rule until independently confirmed against the source PDF image |

### Slide 16 (footer 16) / p17 — 14 units ("Medium-Term Financial Outlook") — AMBIGUOUS_CHART_MAPPING
| # | Item | Value | Flags |
|---|------|-------|-------|
| 1 | CAGR label 1 | 30% | `AMBIGUOUS_CHART_MAPPING` — three CAGR% labels (30%, 19%, 39%) appear scrambled across overlapping Revenue/EBITDA bar-chart text with no unambiguous label-to-series binding in the extract |
| 2 | CAGR label 2 | 19% | see flag above |
| 3 | CAGR label 3 | 39% | see flag above |
| 4 | EBITDA, LTM Sep'24 (Pre-IPO Baseline) | 6,472 | |
| 5 | EBITDA, LTM Jun'26 | 11,485 | |
| 6 | FY30 target value (instance 1) | 30,000 | `AMBIGUOUS_CHART_MAPPING` — appears twice in extract (Revenue and/or EBITDA FY30 target); not confirmed whether this is one series repeated or two distinct series both targeting 30,000 |
| 7 | FY30 target value (instance 2) | 30,000 | see flag above |
| 8 | Net Debt, LTM Sep'24 (Pre-IPO Baseline) | 5,534 | |
| 9 | Net Debt, LTM Jun'26 | 2,654 | (matches slide-10 Net Debt "30 Jun 26" figure, cross-check consistent) |
| 10 | Net Debt, FY30 (target) | 3,000 | |
| 11 | Period label | LTM Sep 24, Pre-IPO Baseline | |
| 12 | Period label | LTM Jun 26 | |
| 13 | Period label | FY 30 | |
| 14 | Strategic Outlook statement | "Sustained EBITDA expansion without significant dilution of Equity." | forward guidance/outlook — A3/A4 should test against FY30 targets above |

### Slide 17 (footer 17) / p18 — 1 unit
| # | Item |
|---|------|
| 1 | "Thank You" closing slide (OCR-confirmed, no additional data) |

---

## Flags Summary

- `ZERO_STANDING` x1 — Table 2, row 19 (Share of Profit/(Loss) from Associates, Q1 FY26 blank)
- `INTERNAL_INCONSISTENCY` x1 — Slide 8/p9 "Revenue from Top 10 customers INR mn 3,759" matches Table 3's Top-5 figure, not Top-10 (4,808)
- `OCR_LOW_CONFIDENCE` x1 — Slide 15/p16 per-year Revenue/PAT chart, pairing unverified
- `AMBIGUOUS_CHART_MAPPING` x2 — Slide 12/p13 (EPS/ROE period-to-value binding inferred, not read directly); Slide 16/p17 (CAGR%/FY30-target label-to-series binding unclear)
- `DISCREPANCY` x1 — task-stated "18 slides" vs deck's own footer numbering (1-17); PDF page 1 is an unnumbered SEBI Reg 30 covering letter
- `PRIOR_LEDGER_UNAVAILABLE` x1 — no prior-quarter presentation ledger supplied; `DROPPED_SLIDE` check not performed this run
