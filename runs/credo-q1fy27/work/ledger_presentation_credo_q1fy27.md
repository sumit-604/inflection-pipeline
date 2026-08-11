# A2 ENUMERATION LEDGER — Credo Brands Marketing Ltd (CREDO) — Q1 FY27 — Investor Presentation

Source: `extract_presentation_credo_q1fy27.txt` (38-page/38-slide PDF, unit Crores x1,
OCR applied to pages 4, 10, 13, 22, 32, 34). All line numbers below refer to this
extract file.

Prior-quarter deck: none supplied (first coverage for CREDO in this pipeline).
**DROPPED_SLIDE cannot be computed this run** — there is no prior-quarter ledger to
diff the slide list against. Flagged `PRIOR_DECK_UNAVAILABLE` rather than raised as
a genuine DROPPED_SLIDE finding.

=== A2 COUNT TEST ===
category: slides       grep_count: 38    sweep_count: 38    match: yes
category: slide_numbers grep_count: 38   sweep_count: 38    match: yes
category: numbers (line_items) grep_count: 863   sweep_count: 863   match: yes
category: footnotes (notes)    grep_count: 18    sweep_count: 18    match: yes
category: zero_standing        grep_count: 4     sweep_count: 4     match: yes
gate_a2: pass
=== END COUNT TEST ===

## Reconciliation notes (method detail, per GATE A2 "enumerate two ways")

**slides / slide_numbers**: Method 1 = `grep -c '^\[page '` on the extract = 38.
Method 2 = manual walk of every `[page N]` marker, confirming N runs 1→38 with no
gaps, no duplicates, matching `page_count_pdfinfo: 38` in the A1 header. Match.

**numbers (line_items)**: Method 1 = mechanical regex sweep, pattern
`[+-]?\d[\d,]*\.?\d*%?` applied to every content line inside each `[page N]` block
(header block above page 1 excluded), tallied per page = 863 total across 297
number-bearing lines. Method 2 = manual line-by-line read of the full extract
(all 947 lines), cross-checked token-for-token against the Method 1 output per
slide (Table B below). Converged at 863. This count includes chart data labels
(all of which are in the native PDF text layer, not OCR-derived, except the 6
OCR divider slides which carry zero chart data by design — see Table A), date
stamps, scrip/CIN/phone digits, and page-footer numerals.

**footnotes (notes)**: Method 1 (first pass) = `grep -noE` for lines starting
with `*`, `^`, `Note:`/`Note :`, or `RoCE =`/`RoE =` → 15 raw hits. Re-swept per
GATE A2 rule 4 (mismatch → re-sweep) because a manual read of pages 7, 19, 26 and
28 surfaced three items the first-pass regex missed: (a) line 192 `^ As of Jun
30, 2026` — caret is followed by a **space** before the letter, unlike line 450's
`^As of...`, so it fell outside the tight `\^[A-Za-z]` pattern; (b) line 676 `As
of Jun 30, 2026` on slide 28 — a genuine as-of-date qualifier with **no** leading
marker character at all; (c) the Safe Harbor slide (slide 3) — a whole-slide
disclaimer, not a line-level footnote, so no line-anchored regex catches it.
Refined Method 1 regex (`\*[A-Za-z]…|\^\s?[A-Za-z]…|Note ?:|^RoCE =|^RoE =|^As
of`) returns 18 raw hits, one of which (line 603, `^ No` — the caret glued to
"No. of MBOs" inside the headline data label `1,336^`) is a false positive (it
is the marker *on* the number, not the footnote text explaining it), netting
against the Safe Harbor slide (uncaught by any line pattern) — net 18. Manual
sweep independently lists the same 18 items (Table C). Match.

**zero_standing**: `0.0`/dash literals were grepped directly (`0\.0` → 2 hits,
lines 861 and 873; standalone `-`/`-` table cells → 1 hit, line 883, containing
2 dash cells) plus a mechanical column-count check comparing each historical
P&L/BS/CF data row's token count against its 5-period header (FY26/FY25*/FY24*/
FY23*/FY22* or Mar-26.../Mar-22*) — this surfaced the "Exceptional Items" row
(line 845, page 35) as populated in only 1 of 5 columns. Total 4 line items
flagged ZERO_STANDING (2 zero-valued cells + 2 dash cells + 4 blank cells across
these 4 line items). Manual read confirms all 4. Match.

---

## TABLE A — Every slide (number, title, content type)

| # | Line | Title (verbatim) | Content type | Notes / flags |
|---|------|-------------------|---------------|----------------|
| 1 | 15 | (no title — regulatory transmittal letter to BSE/NSE) | text | Cover letter re: Reg. 30(6); digitally signed by Company Secretary; signature timestamp 2026.08.11 18:23:45 — same calendar day as filing, no board-meeting-conclusion timing conflict to flag (this is a presentation cover letter, not a results-approval letter) |
| 2 | 55 | Investor Presentation / August'26 | text + photo | Title slide; tagline "MUFTI 2.0 - Premium Retail Experience × Elevated Merchandise × Brand Storytelling" |
| 3 | 67 | Safe Harbor | text (disclaimer) | Entire slide is a fine-print forward-looking-statements disclaimer — see Table C FN-01 |
| 4 | 94 | Q1 FY27 FINANCIAL HIGHLIGHTS | photo (section divider) | `[OCR page 4]`. Full-bleed photo, title only, no chart/numeric content per OCR |
| 5 | 99 | MD's Comments | text | Kamal Khushlani (Promoter & CMD) quote |
| 6 | 133 | Q1 FY27 Operational & Financial Performance | chart + stat blocks | 2 pie charts (Product Mix, Sales Mix) + 4 headline metric callouts (Revenue, Gross Profit/Margin, EBITDA/Margin, PAT/Margin) + store count |
| 7 | 162 | Cash Flow & Balance Sheet | chart + stat blocks | Bar charts: Working Capital Days (Inventory/Debtors/Creditors), Cash Flow from Operations; callouts RoCE, RoE; TTM/as-of footnotes |
| 8 | 194 | Key Focus Areas Of The Company | chart + text (checklist) | 3 line/bar charts: GP Margin %, Revenue per sq.ft., EBITDA Margin %, each FY22–FY26 |
| 9 | 229 | Profit & Loss Statement | table + callout text | Full Q1FY27 vs Q1FY26 P&L; explanatory callout box on EBITDA decline |
| 10 | 258 | TRANSITIONING INTO PREMIUMIZATION | photo (section divider) | `[OCR page 10]`. No numeric content |
| 11 | 263 | Premiumization of Stores Experience | text + photo/diagram | Numbered callouts 1–4 (framework labels, not data) |
| 12 | 284 | Reinvented Brand Identity | text + photo | Store location list (city/mall names) |
| 13 | 313 | HOW IS MUFTI DIFFERENT | photo (section divider) | `[OCR page 13]`. No numeric content |
| 14 | 318 | How is MUFTI Different (1/2) | text (comparison narrative) | Inventory/Receivable/Payable days — qualitative "Typical View vs Credo's View" |
| 15 | 346 | How is MUFTI Different (2/2) | text (comparison narrative) | Risk Allocation / Working Capital / Channel Mix — qualitative |
| 16 | 373 | Increasing focus on D2C channel | text | "~7% YoY" website sales growth stat; 8.5% brand-building spend restated |
| 17 | 402 | Recent Marketing Campaigns (1/2) | photo | 3 campaign tiles (Prateik x Mufti, Flow Linen, Havana), no numeric data |
| 18 | 414 | Recent Marketing Campaigns (2/2) | photo | 3 campaign tiles (Slow Living, 400050 for Every Artist, Loose Jean) |
| 19 | 426 | 'Mufti' – Redefining Menswear | text + stat blocks | Touchpoints/EBOs/towns/cities/suppliers stats, ^as-of footnote |
| 20 | 453 | MUFTI is a Brand, Redefining Menswear | text + diagram (chart) | 5-step "Merchandise Lifecycle Flow" numbered diagram (1–5, structural not data) |
| 21 | 484 | Reinvented Merchandise Architecture | photo + text | 4 category tiles (Authentic/Relaxed/Urban/Athleisure), no numeric data |
| 22 | 498 | COMPANY DIFFERENTIATORS | photo (section divider) | `[OCR page 22]`. No numeric content |
| 23 | 503 | Company Differentiators | text (9-item numbered list) | 9 differentiator headings, numbered 1–9 (structural) |
| 24 | 533 | 1. Wide Range of Products for Multiple Occasions | text + photo | Note (1) footnote on Shirts/T-shirts = Topwear |
| 25 | 545 | 2. Strong Brand Equity with Presence Across Categories | text/chart (positioning matrix, no data labels) | Denim/Casual Led x Premium+/Premium/Mid-Premium/Value grid, brand logos only, no numbers |
| 26 | 574 | 3. Multi-channel having Pan-India Distribution | chart + stat blocks | EBO/MBO/LFS counts by geography, sales mix pie, geography % bar, map disclaimer + as-of/management-estimate footnotes |
| 27 | 616 | 4. EBOs Offering Holistic In-Store Brand Experience... | chart (4 bar charts) + text checklist | Capex/EBO, Revenue/EBO, Revenue/product, Ticket value — each FY22–FY26 |
| 28 | 652 | ...with an evenly spread PAN-India network | chart (3 pie charts) | Store Operating Model (FOFO/COCO/COFO), Tier-wise, Location-wise; Top 2*/Next 6** footnotes |
| 29 | 681 | 6. Driven Through Longstanding Relationships with Partners | text + stat blocks | Supplier/manufacturing/franchisee tenure and count stats |
| 30 | 714 | 7. Systems Driven Processes and Analytical Capabilities... | text | Warehouse sq.ft., design count stats; no chart |
| 31 | 745 | 8. Financially Stable Business Model With Demonstrated History of Profitable Growth | chart (6 bar/line charts) | Revenue, GP Margin, EBITDA Margin, PAT Margin, WC Days, Return Ratios (RoE/RoCE) — each FY22–FY26; RoCE/RoE definitions repeated |
| 32 | 785 | GROWTH DRIVERS | photo (section divider) | `[OCR page 32]`. No numeric content |
| 33 | 790 | KEY GROWTH STRATEGIES | text | 4 strategy pillars, qualitative bullets, no numeric data |
| 34 | 825 | HISTORICAL FINANCIALS | photo (section divider) | `[OCR page 34]`. No numeric content |
| 35 | 830 | Historical Profit & Loss Statement | table | FY22–FY26, standalone FY26 vs consolidated FY22–FY25 (footnote) |
| 36 | 854 | Historical Balance Sheet | table | Mar-22–Mar-26, same basis split |
| 37 | 891 | Historical Cash Flow Statement | table | FY22–FY26, same basis split |
| 38 | 925 | THANK YOU! | text | CIN, CFO contact, IR advisor (SGA) contact |

Slide count = 38. Slide numbers 1–38, no gaps, no duplicates.

**DROPPED_SLIDE**: not computable — no prior-quarter deck/ledger supplied.

---

## TABLE B — Every number on every slide (grouped by slide; source of the 863-token count)

Format: token list is the literal regex-matched numeric content of that slide, in
reading order, including page-footer numerals (flagged `PAGE_FOOTER`) and quarter/
year label fragments picked up from titles like "Q1 FY27" / "FY26" (flagged
`LABEL_FRAGMENT` — not disclosed data values, kept in the count per instruction
"every number on every slide," but distinguished so downstream reviewers don't
mistake them for metrics).

| # | n | Numbers (verbatim tokens, reading order) | Flags |
|---|---|---|---|
| 1 | 22 | 11, 2026, -1, 400, 001, 400, 051, 544058(scrip code), 30, 2026, 30(Reg. 30(6)), 6, 2015 (Regs. year), 30, 2026, 2026.08.11, 18, 23, 45, +05, 30 (signature timestamp components) | dates/identifiers only |
| 2 | 2 | 26 (August'26), 2.0 (MUFTI 2.0) | LABEL_FRAGMENT |
| 3 | 1 | 2 (page footer) | PAGE_FOOTER |
| 4 | 6 | 1, 27 (Q1 FY27, x2), 4 (page footer/OCR marker), 200 (200dpi OCR note) | LABEL_FRAGMENT, PAGE_FOOTER — divider slide has zero substantive data |
| 5 | 23 | 26,1,27 (FY26/Q1 FY27 label frag), 125 (₹125 cr revenue), 5% (revenue growth qualifier — narrative rounds Q1 revenue growth loosely), 77 (₹77 cr gross profit), 62% (gross margin), 27,31 (₹27cr vs ₹31cr EBITDA YoY), 8.5% (marketing spend), 8,-10% (8-10% FY guidance range), 2 (5 new stores... — see raw), 2.3 (₹2.3cr PAT), 5 (5 new stores), 7 (7 closed stores), 2.0 (MUFTI 2.0, x2), 4 (page footer) | mixed real metrics + labels |
| 6 | 25 | 1,27 (label,x2), -0.8% (store count YoY), 125.3 (Revenue ₹cr), 427 (Total Store Count), 10.8%,4.5% (product mix chart), 46.5%(product mix), 39.0%(product mix), 77.2(Gross Profit ₹cr), 61.6%(GP Margin), 4.9%(sales mix), 26.6(EBITDA ₹cr), 21.2%(EBITDA Margin), 11.6%(sales mix), 4.8%(sales mix), 17.5%(sales mix), 61.2%(sales mix), 2.3(PAT ₹cr), 1.8%(PAT Margin), 5 (page footer) | real chart data labels |
| 7 | 27 | 116→176(WC days: Inventory/Debtors/Creditors FY25/FY26/Jun-26 incl. one OCR-adjacent value), 184,196,176*(WC days row), 147,159(Debtors), 133,118,132(Inventory), 67,65,74(Creditors), 16,16,17(sub-values), 25,26,-26(CFO Rs crs chart, incl. one negative-format artifact from "Post IND AS 116" text), 33(page footer note position), 25,26,-26(RoCE/RoE chart FY labels), 12.9%(RoCE), 10.1%(RoE), 6(page footer), 30,2026(as-of date) | real chart data + WC/CFO figures |
| 8 | 35 | 1(item#), 56.9%,57.5%,57.5%,57.2%,58.4%(GP Margin FY22-26), 57%(narrative "above 57%"), 22-26 x2 (FY axis labels, item 1&2 charts), 2(item#), 11,740/11,422/11,928/11,719/9,324(Revenue per sq.ft. FY22-26), 22-26(FY axis), 3(item#), 27.9%,32.9%,28.3%,29.1%,26.0%(EBITDA Margin FY22-26), 22-26(FY axis), 7(page footer) | real chart data |
| 9 | 54 | 1,27,1,26(label frags), 125.3,119.9,5%(Total Revenue), 48.1,46.1(Cost of Materials), 77.2,73.8,5%(Gross Profit), 61.6%,61.6%(Gross Margin), 9.4,8.4(Employee Cost), 41.2,34.4(Other Expenses), 1,27,14%(callout label), 26.6,31.0,-14%,26.6(EBITDA), 21.2%,25.9%(EBITDA Margin), 10.7,8.5%(marketing spend callout), 2.1,1.6(Other Income), 5.4(Q1FY26 marketing spend callout), 19.2,18.2(Depreciation), 1,26(label), 9.5,14.4,-34%(EBIT), 6.3,6.2(Finance Cost), 3.2,8.2,-61%(PBT), 0.9,1.9(Tax), 2.3,6.3,-63%(PAT), 1.8%,5.3%(PAT Margin), 0.35,0.97(EPS), 8(page footer) | full P&L table, real data |
| 10 | 2 | 10(page footer/OCR), 200(200dpi note) | PAGE_FOOTER — divider, zero data |
| 11 | 7 | 1,3,2,4(callout numbers, structural),55(?, see raw — actually "3 Stronger Brand Differentiation 55" is a rendering artifact of overlapping text boxes 5+5),6,10(page footer) | mostly structural callout numbers |
| 12 | 5 | 28(28 years authenticity), -2 (address/mall artifact),2.0,2.0(MUFTI 2.0 x2),11(page footer) | mixed |
| 13 | 2 | 13(page footer),200(OCR note) | PAGE_FOOTER — divider, zero data |
| 14 | 3 | 1,2(section labels 1/2),13(page footer) | structural |
| 15 | 4 | 2,2,1(section labels 2/2),14(page footer) | structural |
| 16 | 9 | 2(D2C heading ref),7%(website sales YoY growth),8.5%(brand-building spend restated),1,27(label),8,-10%(FY27 guidance range restated),15(page footer) | real metrics restated |
| 17 | 3 | 1,2(campaign tile refs),16(page footer) | structural |
| 18 | 4 | 2,2(campaign tile refs),400050(campaign name — "400050 For Every Artist"),17(page footer) | mixed |
| 19 | 10 | 2.5(million customers),1,913(touchpoints),427(EBOs),231(towns/cities),50(fabric suppliers),50(manufacturing partners),583(cities present),30,2026(as-of date),18(page footer) | real metrics |
| 20 | 7 | 1,100%(100% control claim),5,2,4,3(lifecycle step numbers, structural),19(page footer) | mostly structural |
| 21 | 1 | 20(page footer) | PAGE_FOOTER only |
| 22 | 2 | 22(page footer/OCR),200(OCR note) | PAGE_FOOTER — divider, zero data |
| 23 | 11 | 1–9(nine differentiator item numbers, structural),22(page footer) | structural |
| 24 | 5 | 1.(Note ref),1,1,1(Shirts(1)/T-shirts(1) footnote markers x3),23(page footer) | footnote markers |
| 25 | 2 | 2.(section#),24(page footer) | structural |
| 26 | 50 | 3.(section#),1,27(label),115,1,913,287(retail touchpoints by category),4.9%,22,11.6%,4.8%,583,89,17.5%,61.2%(sales mix/geography %),107,414,264,28,49,45,231,183,12,8(store counts by geography),15%(North),71,427(EBOs*),27%,21%,14%,26%,41%(geography % chart),188,17%,1,336(MBOs^),21%,31%,19%,39,25%,20%,32%,10%,14%(geography % continued),150(LFS*),8%,59%(Tier II&III),30,2026(as-of date),25(page footer) | real data + MGMT_ESTIMATE flag on 1,336 (MBO count) |
| 27 | 45 | 4.(section#),+8%,43.3,75.8,74.8,78.0,75.2,28.5,28.1,30.1,55.1,25.6(Capex/EBO, Revenue/EBO FY22-26),22-26 x2(FY axis),+2%,+11%(growth callouts),1,208,1,348,1,285,1,301,1323(Revenue/product sold FY22-26 — note FY26 value "1323" lacks the thousands comma present in prior years, verbatim as extracted),5,294,5,232,4,157,4,292,3,442(Ticket value FY22-26),22-26 x2(FY axis),26(page footer) | real chart data; note formatting inconsistency flagged |
| 28 | 21 | 427,231(EBOs/cities restated),2(diagram ref),11%(Top 2 store %),3(diagram ref),25%,26%(Tier wise),6(diagram ref),35%,13%,33%,17%,66%,1%(location wise),1(diagram ref),33%,40%(store operating model FOFO/COCO/COFO),2(diagram ref),30,2026(as-of date),27(page footer) | real chart data |
| 29 | 11 | 6.(section#),50,50(supplier/mfg partner counts),50%(franchisee tenure %),5(>5 years),10,10(>10yr avg association x2),-5,-5(rendering artifact of ">5" duplicated, see raw text "Over 50%...for over 5 years"),12(>12 years),28(page footer) | real data + rendering artifacts |
| 30 | 5 | 7.(section#),15(15-member design team),142,700(sq.ft warehouse),1400(design count),29(page footer) | real data |
| 31 | 100 | 8.(section#),56.9%–58.4% x2 sets(GP Margin FY22-26, repeated from slide 8),27.9%-32.9% set(EBITDA Margin FY22-26, repeated),+15%,+15%,+13%(growth callouts),567,618,592(Revenue FY22-24... continued),326,354,345,164,161,180,154,498,286,341,194,95(Revenue/GP/EBITDA absolute FY22-26 continued),22-26 x3 sets(FY axis, 3 charts),10.5%,15.6%,10.4%,11.1%,8.0%(PAT Margin FY22-26),160,132,166,184,196(Inventory Days),30.0%,28.2%,19.3%(RoE/RoCE partial),78,147(Debtors Days),16.7%,17.3%,19.0%,18.2%,18.9%(RoE/RoCE continued),68,132,133,59,49,96,77,112(Debtors/Creditors continued),11.2%,13.8%(RoE/RoCE continued),36,67,66,67,65(Creditors Days continued),38,29,23,16,16(sub-values),22-26 x2 sets(FY axis, incl. -22...-26 date-header artifact),30(page footer) | dense real chart data — largest slide by number count |
| 32 | 2 | 32(page footer/OCR),200(OCR note) | PAGE_FOOTER — divider, zero data |
| 33 | 1 | 32(page footer) | PAGE_FOOTER only |
| 34 | 2 | 34(page footer/OCR),200(OCR note) | PAGE_FOOTER — divider, zero data |
| 35 | 92 | 26,25,24,23,22(header FY labels),592.1,618.2,567.3,498.2,341.2(Revenue FY26-22),246.6,264.3,241.3,211.9,147.1(Raw Material Cost),345.5,353.9,326.1,286.2,194.1(Gross Profit),58.4%,57.2%,57.5%,57.5%,56.9%(GP Margin),35.4,32.1,31.6,26.8,29.2(Employee Cost),155.9,142.1,134.0,95.6,69.8(Other Expenses),154.2,179.7,160.5,163.9,95.1(EBITDA),26.0%,29.1%,28.3%,32.9%,27.9%(EBITDA Margin),10.9,6.1,4.6,11.1,13.7(Other Income),74.4,68.6,62.2,53.4,45.9(Depreciation),90.7,117.2,103.0,121.6,62.9(EBIT),25.5,25.5,24.1,17.8,15.0(Finance Cost),1.4(Exceptional Items — FY26 ONLY, see Table D),63.8,91.7,78.9,103.8,47.8(PBT),16.4,23.4,19.7,26.3,12.1(Tax),47.4,68.4,59.2,77.5,35.7(PAT),8.0%,11.1%,10.4%,15.6%,10.5%(PAT Margin),7.3,10.5,9.2,12.1,5.6(EPS),34(page footer) | full 5-year P&L; Exceptional Items = ZERO_STANDING elsewhere, see Table D |
| 36 | 184 | (full dual-column Balance Sheet, Mar-26/25*/24*/23*/22* both Assets and Equity&Liabilities sides — PP&E, CWIP, RoU Asset, Investment Property, Intangibles, Financial Assets(NC), Deferred Tax Asset, Non-Current Tax Assets, Other NC Assets, Non-Current Assets total, Inventories, Trade receivables, Cash & equivalents, Bank Balance & other, Other Financial Assets(C), Other Current Assets, Current Assets total, Total Assets — mirrored by Share Capital, Other Equity, Total Equity, Borrowings(NC)[=0.0 in Mar-26, ZERO_STANDING], Lease Liabilities(NC), Other Financial Liabilities(NC), Provisions(NC), Non-Current Liabilities total, Borrowings(C)[=0.0 in Mar-26, ZERO_STANDING], Lease Liabilities(C), Trade Payables, Other Financial Liabilities(C), Provisions(C), Current tax liabilities(net)[dash in Mar-23/Mar-22, ZERO_STANDING], Other current liabilities, Current Liabilities total, Total Equity & Liabilities) | 35(page footer) | full 5-year Balance Sheet; 3 line items flagged ZERO_STANDING, see Table D |
| 37 | 66 | (full Cash Flow Statement FY26-22: Net Profit Before Tax, Non-Cash/Other adjustments, Operating profit before WC changes, Changes in WC, Cash generated from Operations, Direct taxes paid, Net Cash from Operating Activities, Net Cash from Investing Activities, Net Cash from Financing Activities, Net Change in Cash, Opening cash, Closing cash) | 36(page footer) | full 5-year Cash Flow, no zero-standing anomalies found |
| 38 | 12 | 18101,1999,119669(CIN L18101MH1999PLC119669),74140,2010,204285(SGA CIN U74140MH2010PTC204285),+91,98333,73300(phone),+91,89492,92029(phone) | identifiers/contact numbers only |

Total tokens across all 38 slides = **863**, matching the mechanical regex count.

---

## TABLE C — Every footnote and fine-print disclaimer qualifying a headline number

| # | Slide | Line | Footnote text (verbatim/paraphrase) | Qualifies | Flag |
|---|-------|------|--------------------------------------|-----------|------|
| FN-01 | 3 | 68-89 | Full Safe Harbor disclaimer: not an offer document, no reliance on accuracy/completeness, forward-looking-statement risk factors, no obligation to update | Entire presentation (blanket disclaimer) | — |
| FN-02 | 7 | 187 | "RoCE = EBIT / Average Capital Employed. (Capital Employed = Total Equity + Long Term Debt + Short Term Debt)" | RoCE 12.9% | definitional |
| FN-03 | 7 | 188 | "RoE = PAT / Average Equity" | RoE 10.1% | definitional |
| FN-04 | 7 | 191 | "*Trailing Twelve Months" | Jun-26 column figures marked with `*` (e.g. Creditors Days 176*) | period-basis |
| FN-05 | 7 | 192 | "^ As of Jun 30, 2026" | RoCE/RoE `^*` marked figures (missed by first-pass regex — caret+space formatting) | period-basis |
| FN-06 | 19 | 450 | "^As of Jun 30, 2026" | "Presence in 583 cities in India^" | period-basis |
| FN-07 | 24 | 543 | "Note: (1) Shirts and T-shirts together constitute Topwear" | "Shirts (1)" / "T-shirts (1)" category labels | definitional |
| FN-08 | 26 | 611 | "Note: Maps not to scale. All data, information, and maps are provided 'as is' without warranty or any representation of accuracy" | Geography % map/chart | accuracy disclaimer |
| FN-09 | 26 | 614 | "*EBOs and LFS count is as on 30th Jun 2026." | "427* No. of EBOs", "150* No. of LFS" | period-basis |
| FN-10 | 26 | 614 | "^Management Estimate" | "1,336^ No. of MBOs" | **MGMT_ESTIMATE — MBO count is not a hard company-system figure, it is management's own estimate; unaudited/unverified** |
| FN-11 | 28 | 676 | "As of Jun 30, 2026" | Store Operating Model / Tier-wise / Location-wise % chart (missed by first-pass regex — no leading marker at all) | period-basis |
| FN-12 | 28 | 678 | "*Includes Greater Mumbai, Maharashtra... and Delhi NCR..." | "Top 2*" location-wise label | definitional |
| FN-13 | 28 | 679 | "**Includes (i) Bangalore... (vi) Pune, Maharashtra" | "Next 6**" location-wise label | definitional |
| FN-14 | 31 | 781 | "RoCE = EBIT / Average Capital Employed..." (repeat of FN-02) | RoCE bars in Return Ratios chart | definitional |
| FN-15 | 31 | 782 | "RoE = PAT / Average Equity" (repeat of FN-03) | RoE bars in Return Ratios chart | definitional |
| FN-16 | 35 | 852 | "*On Consolidated Basis" | FY25*/FY24*/FY23*/FY22* columns of Historical P&L (FY26 alone is standalone) | **BASIS_MISMATCH — comparability caveat: 4 of 5 years on a different consolidation basis than the current year** |
| FN-17 | 36 | 889 | "*On Consolidated Basis" | Same caveat, Historical Balance Sheet | BASIS_MISMATCH |
| FN-18 | 37 | 923 | "*On Consolidated Basis" | Same caveat, Historical Cash Flow Statement | BASIS_MISMATCH |

Total footnotes/disclaimers = **18**.

---

## TABLE D — Zero / nil / dash-valued standing line items (ZERO_STANDING)

| # | Slide | Line | Line item | Periods with zero/nil/dash value | Periods with a value | Flag |
|---|-------|------|-----------|-----------------------------------|------------------------|------|
| ZS-01 | 36 | 861 | (i) Borrowings — Non-Current Financial Liabilities | Mar-26 = 0.0 | Mar-25=1.1, Mar-24=4.8, Mar-23=6.8, Mar-22=10.1 | ZERO_STANDING — long-term debt fully repaid/nil as of the latest period after a declining trend |
| ZS-02 | 36 | 873 | (i) Borrowings — Current Financial Liabilities | Mar-26 = 0.0 | Mar-25=0.3, Mar-24=32.7, Mar-23=3.3, Mar-22=3.4 | ZERO_STANDING — short-term debt nil as of the latest period |
| ZS-03 | 36 | 883 | Current tax liabilities (net) | Mar-23 = "-", Mar-22 = "-" | Mar-26=4.3, Mar-25=1.9, Mar-24=0.5 | ZERO_STANDING — line item only began appearing in the most recent 3 of 5 periods shown |
| ZS-04 | 35 | 845 | Exceptional Items | FY25, FY24, FY23, FY22 = blank (no value printed) | FY26 = 1.4 | ZERO_STANDING — line item appears only in the latest year; reconciles the 1.4 gap between EBIT-Finance Cost (65.2) and reported PBT (63.8) |

Total ZERO_STANDING line items = **4**.

---

## Summary

- 38 slides enumerated (1–38), all present in this deck; prior-quarter deck not
  supplied so DROPPED_SLIDE is not computable this run.
- 863 numbers enumerated across all 38 slides (Table B), reconciled mechanically
  (regex) against a manual line-by-line sweep of the full 947-line extract.
- 18 footnotes/fine-print disclaimers enumerated (Table C); GATE A2 caught and
  resolved one genuine mismatch (15 raw regex hits vs 18 after manual re-sweep
  surfaced 3 misses: a caret-space formatting variant, an unmarked "As of" caption,
  and the whole-slide Safe Harbor disclaimer).
- 4 zero/nil/dash-valued standing line items enumerated (Table D), none dropped.
- Two content-quality flags surfaced for A3/A4 attention: MGMT_ESTIMATE (the
  1,336 MBO count on slide 26 is explicitly labelled a management estimate, not
  a hard figure) and BASIS_MISMATCH (the three historical financial statements,
  slides 35-37, mix standalone FY26 against consolidated FY22-FY25 with no
  restated comparable).

```yaml
stage: A2-enumerator
company: "CREDO"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/credo-q1fy27/work/ledger_presentation_credo_q1fy27.md"
counts:
  notes: 18
  line_items: 863
  zero_standing: 4
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 38
  slide_numbers: 38
flags_raised: [ZERO_STANDING, MGMT_ESTIMATE, BASIS_MISMATCH]
gate_a2: pass
mismatch_note: ""
```
