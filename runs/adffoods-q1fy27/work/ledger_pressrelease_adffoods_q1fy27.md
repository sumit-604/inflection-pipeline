# A2 Enumeration Ledger — ADF Foods Limited (ADFFOODS) — Q1 FY27 — Doctype: presentation (press release)

Source: `extract_pressrelease_adffoods_q1fy27.txt` (4-page Q1 FY27 earnings press release, management narrative)
Prior-quarter ledger: not provided — DROPPED_SLIDE / prior-period diff checks not applicable this run.

Methodology note: this document is a narrative press release, not a structured
filing/table-heavy annexure set or a concall transcript. Enumeration below
follows the task instruction to treat each highlights-table row (per period
column) and each numbered/paragraphed commentary point as an enumerable
unit. Objectively-patterned categories (checkmark bullets, table row labels,
quote sentences) were verified with a `grep`/script pass against the raw
text. Structural/boilerplate categories (cover letter fields, callout boxes,
About/Contact/Safe Harbor blocks) were verified by individually confirming
each item's anchor text is present exactly once in its section (manual
sweep), cross-checked line by line against the full extract read.

```
=== A2 COUNT TEST ===
category: cover_letter_items        grep_count: 11   sweep_count: 11   match: yes
category: header_title_items        grep_count: 3    sweep_count: 3    match: yes
category: callout_boxes             grep_count: 4    sweep_count: 4    match: yes
category: line_items (fin. tables)  grep_count: 10   sweep_count: 10   match: yes
category: highlight_bullets         grep_count: 7    sweep_count: 7    match: yes
category: quote_units (full+claims) grep_count: 14   sweep_count: 14   match: yes
category: about_company_items       grep_count: 2    sweep_count: 2    match: yes
category: contact_items             grep_count: 5    sweep_count: 5    match: yes
category: safe_harbor_items         grep_count: 1    sweep_count: 1    match: yes
--------------------------------------------------------------------------
TOTAL DISCLOSURE UNITS: 57  (11+3+4+10+7+14+2+5+1)
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used for verification (representative):
- `grep -c "✓" extract` → 7 (matches 6 Key Financial Highlights + 1 Key Business Highlight bullet)
- `grep -c -E "^(Revenue from Operations|EBITDA Margin|EBITDA|PAT Margin|PAT)\s" extract` → 10 (5 consolidated + 5 standalone row labels)
- Quote sentence split script (decimal-point-safe, splitting also on `, while` and `and the receipt of` compound joins) → 13 raw sentence/claim fragments; +1 for the full quote as an overarching unit = 14
- `grep -n -E "29th July, 2026|National Stock Exchange|Symbol: ADFFOODS|Sub: Press Release|Regulation 30 of the|has been uploaded|Yours faithfully|SHALAKA|Encl: As above|Regd Off:"` → anchors individually confirmed unique to their respective cover-letter items (11 items; NSE+BSE addressee columns share physical lines 19-24 and are enumerated as one combined addressee item, not split, to avoid a false line-count split)

---

## 1. Filing Cover Letter (page 1) — Regulation 30 transmittal

| # | Item | Line(s) | Content (first ~15 words / detail) | Flags |
|---|------|---------|--------------------------------------|-------|
| 1.1 | Letter date | 17 | "29th July, 2026" | |
| 1.2 | Addressee block (NSE + BSE, two-column) | 19-24 | National Stock Exchange of India Ltd, Exchange Plaza, BKC, Mumbai / BSE Ltd, Dept of Corporate Services, PJ Towers, Dalal Street, Mumbai | |
| 1.3 | Symbol / Scrip Code | 25 | Symbol: ADFFOODS; Scrip Code: 519183 | |
| 1.4 | Subject line | 27 | "Sub: Press Release of Q1 FY 2026-27 Financials." | |
| 1.5 | Regulatory basis + enclosure statement | 31-33 | Pursuant to Regulation 30 of SEBI (LODR) Regulations, 2015, enclose Press Release of Q1 FY26-27 Financials dated 29th July, 2026 | |
| 1.6 | Website upload statement | 35 | Aforementioned uploaded on Company's website at www.adf-foods.com | |
| 1.7 | Records request statement | 37 | "You are requested to take the above information on your records." | |
| 1.8 | Closing / salutation block | 39-42 | Thanking You, Yours faithfully, For ADF Foods Limited | |
| 1.9 | Digital signature block | 43-49 | Shalaka Swapnil Ovalekar, digitally signed, date 2026.07.29 21:20:01 +05'30", designation Company Secretary | Signature timestamp 21:20:01 IST on 29-Jul-2026 — check against board/authorization timing if available elsewhere in filing set |
| 1.10 | Enclosure note | 51 | "Encl: As above" | |
| 1.11 | Registered/Corp Office footer address block (incl. CIN) | 56-59 | Regd Off Nadiad (incl. CIN L15400GJ1990PLC014265 on this footer occurrence), Corp Off Marathon Innova, Lower Parel, Mumbai, contact numbers/emails | |

## 2. Press Release Header / Title / Banner / Dateline (page 2 top)

| # | Item | Line(s) | Content | Flags |
|---|------|---------|---------|-------|
| 2.1 | Title | 65 | "ADF Foods Limited Reports Q1 FY27 Financials" | |
| 2.2 | Growth banner claim | 67 | "4th Consecutive Quarter of Strong Double-Digit Growth, up 25.9% YoY" | Duplicate metric — cross-ref 3.1, 4.1, 6.1, 8.1 |
| 2.3 | Dateline + one-line company description | 69-70 | "Mumbai, 29th July 2026: ADF Foods Limited, a leading manufacturer of prepared ethnic foods, announced Financial Results for the first quarter ended 30th June 2026." | |

## 3. Headline Callout Boxes (page 2, top summary tiles)

| # | Item | Line(s) | Value | YoY | Flags |
|---|------|---------|-------|-----|-------|
| 3.1 | Revenue from Operations (callout) | 73, 75, 76 | Rs. 167.3 Cr | +25.9% | Duplicate of table row 4.1 / bullet 6.1 / quote 8.1 |
| 3.2 | EBITDA (callout) | 73, 75, 76 | Rs. 29.7 Cr | +26.0% | Duplicate of table row 4.2 / bullet 6.2 / quote 8.10 |
| 3.3 | Profit After Tax (callout) | 73, 75, 76 | Rs. 17.3 Cr | +13.4% | Duplicate of table row 4.4 / bullet 6.3 |
| 3.4 | Footnote / basis qualifier (asterisk) | 79 | "*Q1FY27 Consolidated Figures on a Y-o-Y basis" — qualifies all three callout boxes above | Governs 3.1-3.3; without it the callout tiles are ambiguous re: consol vs standalone |

## 4. Key Consolidated Financial Performance table (lines 82-89)

Header row (line 84): Particulars (Rs. Cr) | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | Q-o-Q

| # | Line item | Line | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | Q-o-Q | Flags |
|---|-----------|------|---------|---------|-------|---------|-------|-------|
| 4.1 | Revenue from Operations | 85 | 167.3 | 132.9 | 25.9% | 196.7 | (15.0)% | |
| 4.2 | EBITDA | 86 | 29.7 | 23.5 | 26.0% | 34.3 | (13.5)% | |
| 4.3 | EBITDA Margin | 87 | 17.7% | 17.7% | 0 bps | 17.4% | 30 bps | **ZERO_STANDING** — Y-o-Y delta = 0 bps (margin unchanged Q1FY27 vs Q1FY26); flagged so the flat reading is not silently dropped |
| 4.4 | PAT | 88 | 17.3 | 15.2 | 13.4% | 25.9 | (33.3)% | |
| 4.5 | PAT Margin | 89 | 10.3% | 11.5% | (120) bps | 13.2% | (290) bps | |

## 5. Key Standalone Financial Performance table (lines 92-99)

Header row (line 94): Particulars (Rs. Cr) | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | Q-o-Q

| # | Line item | Line | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | Q-o-Q | Flags |
|---|-----------|------|---------|---------|-------|---------|-------|-------|
| 5.1 | Revenue from Operations | 95 | 120.9 | 100.3 | 20.5% | 150.3 | (19.5)% | |
| 5.2 | EBITDA | 96 | 27.5 | 22.5 | 22.6% | 36.5 | (24.7)% | |
| 5.3 | EBITDA Margin | 97 | 22.8% | 22.4% | 40 bps | 24.3% | (150) bps | |
| 5.4 | PAT | 98 | 18.3 | 17.0 | 7.6% | 30.1 | (39.3)% | |
| 5.5 | PAT Margin | 99 | 15.1% | 16.9% | (180) bps | 20.0% | (490) bps | |

Note: consolidated PAT growth (13.4%) trails consolidated revenue/EBITDA growth (25.9%/26.0%) and standalone PAT growth (7.6%) trails standalone revenue/EBITDA growth (20.5%/22.6%) in both columns — margin-vs-growth divergence visible directly in the table; flagged here for A3/A4 attention, not interpreted further by A2.

## 6. Key Financial Highlights bullets (page 3, lines 107-113)

| # | Line | Claim (verbatim gist) | Flags |
|---|------|------------------------|-------|
| 6.1 | 108 | Consolidated revenue grew 25.9% y-o-y to Rs. 167.3 Cr | Duplicate of 2.2 / 3.1 / 4.1 / 8.1 |
| 6.2 | 109 | Consolidated EBITDA increased 26.0% to Rs. 29.7 Cr, margin 17.7% | Duplicate of 3.2 / 4.2 / 4.3 / 8.10 |
| 6.3 | 110 | Consolidated PAT increased 13.4% to Rs. 17.3 Cr, margin 10.3% | Duplicate of 3.3 / 4.4 / 4.5 |
| 6.4 | 111 | Standalone Revenue increased 20.5% y-o-y at Rs. 120.9 Cr | Duplicate of 5.1 |
| 6.5 | 112 | Standalone EBITDA increased 22.6% y-o-y at Rs. 27.5 Cr, margin 22.8% | Duplicate of 5.2 / 5.3 |
| 6.6 | 113 | Standalone PAT increased 7.6% y-o-y at Rs. 18.3 Cr, margin 15.1% | Duplicate of 5.4 / 5.5 |

## 7. Key Business Highlights bullets (page 3, lines 115-118)

| # | Line | Claim | Flags |
|---|------|-------|-------|
| 7.1 | 116-118 | AEO-T3 certified — strengthens export operations, enabling faster customs clearances, streamlined compliance, and working capital efficiency | Sole non-financial business highlight bullet this quarter; only one item under this header (checked — no others present). Duplicate of quote claim 8.9 |

## 8. Bimal Thakkar (Chairman & Managing Director) quote (page 3, lines 120-145)

| # | Line(s) | Unit | Content (gist) | Flags |
|---|---------|------|------------------|-------|
| 8.0 | 121-144 | Full quote (single unit, verbatim) | Entire attributed quotation from Mr. Bimal Thakkar, Chairman & Managing Director, in full — required as one ledger unit per task instructions | |
| 8.1 | 121-123 | Claim/metric | Delivered another quarter of strong double-digit growth in Q1FY27; consol revenue +25.9% YoY to ₹167.3 crore; 4th consecutive quarter of robust growth | Duplicate of 2.2/3.1/4.1/6.1 |
| 8.2 | 123-125 | Claim | Growth drivers: deeper shelf-space penetration, continued category diversification, new product listings, strong execution across key international markets | |
| 8.3 | 125-127 | Claim (hedge) | Growth achieved despite geopolitical uncertainties: ongoing West Asia conflict, trade-route disruptions, vessel shortages, elevated freight costs | Hedge phrase — feeds A3 hedge lexicon |
| 8.4 | 127-128 | Claim | Robust order book; shipping and container constraints limiting full conversion of customer demand into revenue | Notable: demand exceeds shippable capacity — order-book vs revenue-conversion gap named by management |
| 8.5 | 129 | Claim | Brands continue to gain traction across markets | |
| 8.6 | 129-131 | Claim — brand: Ashoka | Sustained strong growth, robust diaspora demand, deeper penetration across key international markets | |
| 8.7 | 131-132 | Claim — brand: Truly Indian | Continued strong momentum through expanded distribution and increasing consumer adoption | |
| 8.8 | 132-134 | Claim — Surat facility | Strengthened operational capabilities; commencement of commercial deliveries from Surat greenfield facility | New capacity-in-production disclosure — cross-check against capex/capacity tracker if available |
| 8.9 | 134-135 | Claim — AEO-T3 | Receipt of AEO-T3 certification; enhances export efficiency via faster customs clearances, streamlined compliance, improved working capital management | Duplicate of business highlight 7.1 |
| 8.10 | 136-138 | Claim/metric | Profitability healthy; EBITDA +26.0% YoY to ₹29.7 crore, margin maintained at 17.7%; drivers: favourable product mix, frozen foods momentum, operational efficiencies, disciplined cost management | Duplicate of 3.2/4.2/4.3/6.2 |
| 8.11 | 138-141 | Claim (forward commitment) | Global demand for authentic/convenient/value-added Indian food products continues to grow; focus on strengthening brands, expanding distribution footprint, scaling new capacities, driving sustainable long-term growth | Forward-commitment phrase — feeds A3 lexicon |
| 8.12 | 141-143 | Claim (hedge) | Geopolitical developments, freight cost volatility, vessel availability continue to present uncertainties; "remain cautiously optimistic" | Hedge phrase — feeds A3 lexicon |
| 8.13 | 143-144 | Claim (forward-looking) | Diversified operations, strong execution capabilities, expanding market presence position the company to capitalize on emerging opportunities | Forward-looking / non-specific claim, no quantified commitment |

## 9. About ADF Foods Ltd (page 4, lines 149-154)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 9.1 | 150-152 | Business/product description: consumer-focused company, leading manufacturer of prepared ethnic foods; offers frozen foods, RTE, RTC, sauces, pickles, pastes, dips | Standard boilerplate, unchanged company description |
| 9.2 | 152-154 | Brand count & distribution footprint: 5 prominent brands; products available in 60+ countries; distribution network across North America, UK, EU, Middle East & Asia Pacific | Boilerplate — compare against prior quarter's "About" block for any change in brand/country count if prior ledger available (none provided this run) |

## 10. Contact Details (page 4, lines 157-172)

| # | Line(s) | Contact | Detail | Flags |
|---|---------|---------|--------|-------|
| 10.1 | 165 | CIN | L15400GJ1990PLC014265 (explicit contact-section occurrence) | |
| 10.2 | 168, 171 | ADF Foods Ltd — Srinivas Ayyagari, CFO | srinivas@adf-foods.com | |
| 10.3 | 164, 166 | Investor Relations (EY LLP) — Sumedh Desai | sumedh.desai@in.ey.com | |
| 10.4 | 167, 169 | Investor Relations (EY LLP) — Sukhin Naphade | sukhin.s.naphade@in.ey.com | |
| 10.5 | 170, 172 | Investor Relations (EY LLP) — Vikash Verma | vikash.verma1@in.ey.com | |

## 11. Safe Harbor Statement (page 4, lines 175-183)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 11.1 | 176-183 | Standard forward-looking-statement disclaimer: assumptions, risks/uncertainties, list of factors that could cause actual results to differ (industry downtrend, political/economic environment changes, tax laws, litigation, labour relations, exchange rate fluctuations, technological changes, investment/business income, cash flow projections, interest, other costs); no obligation to update | Boilerplate legal disclaimer, enumerated as single unit per standard treatment of safe-harbor language |

---

## Summary

Total disclosure units enumerated: **57**
- Cover letter items: 11
- Header/title/banner/dateline items: 3
- Headline callout box items: 4
- Consolidated financial highlights table line items: 5
- Standalone financial highlights table line items: 5
- Key Financial Highlights bullets: 6
- Key Business Highlights bullets: 1
- Bimal Thakkar quote units (1 full quote + 13 distinct claims/metrics): 14
- About ADF Foods Ltd items: 2
- Contact detail items: 5
- Safe Harbor Statement: 1

Flags raised: **ZERO_STANDING** (1 instance — consolidated EBITDA Margin Y-o-Y = 0 bps, line 87)

No numbered notes, no auditor paragraphs, no board agenda items, no
consolidation entity list, no concall turns/questions, no slide numbers, no
prior-quarter ledger for DROPPED_SLIDE/ENTITY_CHANGE comparison — none of
these are present in or applicable to this document type/inputs.

Numerous line items are deliberately cross-referenced as duplicates
(the three headline metrics — revenue, EBITDA, PAT — appear in the banner,
the callout boxes, both highlights-bullet lists, and the CMD quote). Each
occurrence is still enumerated as its own row per the anti-miss mandate;
duplication is noted in the Flags column for A3/A4 rather than collapsed.
