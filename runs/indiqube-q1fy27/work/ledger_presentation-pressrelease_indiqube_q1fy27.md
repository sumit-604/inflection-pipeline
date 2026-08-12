# A2 ENUMERATOR LEDGER — IndiQube Spaces Limited (INDIQUBE), Q1FY27, doctype: presentation
Source file note: A1 header labels doctype "presentation" but the extract content is the
Q1FY27 press release / Regulation 30 filing (press_release.pdf, 4 pages, 176 extracted lines).
Enumerated as the press-release document it actually is. Prior-quarter ledger: NONE (first
pipeline run for INDIQUBE) — no DROPPED_SLIDE / prior-period diff possible this run.

```
=== A2 COUNT TEST ===
category: cover_letter_fields          grep_count: 15   sweep_count: 15   match: yes
category: press_dateline               grep_count: 1    sweep_count: 1    match: yes
category: headline_numbers             grep_count: 4    sweep_count: 4    match: yes
category: mgmt_quote_numbers           grep_count: 16   sweep_count: 16   match: yes
category: kpi_financial_highlights     grep_count: 4    sweep_count: 4    match: yes
category: kpi_operational_highlights   grep_count: 5    sweep_count: 5    match: yes
category: credit_rating_lines          grep_count: 1    sweep_count: 1    match: yes
category: qualitative_claims           grep_count: 1    sweep_count: 1    match: yes
category: narrative_numbers            grep_count: 4    sweep_count: 4    match: yes
category: table_metadata               grep_count: 1    sweep_count: 1    match: yes
category: table_rows                   grep_count: 16   sweep_count: 16   match: yes
category: table_cells                  grep_count: 96   sweep_count: 96   match: yes
category: zero_standing_cells          grep_count: 13   sweep_count: 13   match: yes
category: variance_footnote            grep_count: 5    sweep_count: 5    match: yes
category: financial_statements_fields  grep_count: 2    sweep_count: 2    match: yes
category: concall_fields               grep_count: 7    sweep_count: 7    match: yes
category: about_fields                 grep_count: 5    sweep_count: 5    match: yes
category: contact_fields               grep_count: 9    sweep_count: 9    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology note: for each category, a mechanical `grep -oE`/`grep -c` pass on the
extract file with a category-specific anchor pattern (numeric-token regex for the KPI/quote/
narrative/table categories; unique label-string alternation for the metadata/prose categories)
was run against the isolated line range, and its match count compared against an independent
manual line-by-line read of the same range. All 18 categories matched on first pass; no
re-sweep was required.

---

## 1. Regulatory cover letter (page 1, lines 15-53)

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 15 | Letter date | August 12, 2026 | |
| 2 | 18-21 | Addressee 1 | BSE Limited, 20th Floor, P.J. Towers, Dalal Street, Mumbai - 400001 | |
| 3 | 19-21 | Addressee 2 | National Stock Exchange of India Limited, Exchange Plaza, C-1, Block G, Bandra Kurla Complex, Bandra (E), Mumbai - 400 051 | |
| 4 | 22 | BSE Scrip Code | 544454 | |
| 5 | 22 | NSE Scrip Symbol | INDIQUBE | |
| 6 | 25-26 | Subject line | Press Release on Financial Results of Indiqube Spaces Limited ("Indiqube") for the quarter ended June 30, 2026 | |
| 7 | 30-32 | Regulatory basis | Regulation 30 of SEBI (LODR) Regulations, 2015; quarter ended June 30, 2026 (restated) | |
| 8 | 37-40 | Digital signature block | Digitally signed by BHASKER DUBEY, Date: 2026.08.12, 17:50:22 +05'30' | |
| 9 | 42-43 | Signatory name & designation | Bhasker Dubey, Company Secretary & Compliance Officer | |
| 10 | 48-49 | Company name + former names | Indiqube Spaces Limited (formerly Indiqube Spaces Private Limited, Innovent Spaces Private Limited) | |
| 11 | 49 | Company email | vinfo@indiqube.com | |
| 12 | 50 | Company website | www.indiqube.com | |
| 13 | 50-52 | Registered/Corporate Office address | Plot # 53, Careernet Campus, Kariyammanna Agrahara Road, Devarabisanahalli, Outer Ring Road, Bangalore, Karnataka, India, 560103 | |
| 14 | 51 | Company phone | +91 9900092210 | |
| 15 | 53 | CIN | L45400KA2015PLC133523 | |

## 2. Press release dateline (line 59-60)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 59-60 | "Bengaluru, August 12, 2026 – IndiQube Spaces Limited, one of India's leading Integrated Managed Spaces Platform, today announced its financial results for Q1 FY27." | |

## 3. Headline numbers (lines 55-56)

| # | Line | Metric | Value | Flags |
|---|------|--------|-------|-------|
| 1 | 55 | Revenue (headline) | ₹428 Cr | matches KPI bullet line 86 |
| 2 | 56 | Revenue YoY growth (headline) | 37% | matches KPI bullet line 86 |
| 3 | 56 | PAT growth (headline) | Up 91% | matches KPI bullet line 92 |
| 4 | 56 | PAT (headline) | ₹35 Cr | matches KPI bullet line 92 |

Note: headline text carries the superlative claim "Highest Ever Quarterly Revenue" attached to
item 1 — unverifiable historical superlative, carried as management framing, not evidenced in
this document.

## 4. Management-attributed numbers in quotes

### 4a. Rishi Das, Cofounder & CEO (lines 62-71)

| # | Line | Number | Context | Flags |
|---|------|--------|---------|-------|
| 1 | 63 | ₹428 crore | highest ever quarterly revenue | matches line 86 |
| 2 | 64 | 37% | YoY revenue growth | matches line 86 |
| 3 | 67 | 34% | EBITDA growth | matches line 88 |
| 4 | 67 | ₹87 crore | EBITDA | matches line 88 |
| 5 | 67 | 59% | EBIT growth | matches line 90 |
| 6 | 67 | ₹55 crore | EBIT | matches line 90 |
| 7 | 67 | 91% | PAT growth | matches line 92 |
| 8 | 67-68 | ₹35 crore | PAT | matches line 92 |
| 9 | 68 | 20% | EBITDA margin | matches line 88 |
| 10 | 68 | 13% | EBIT margin | matches line 90 |
| 11 | 69 | 8% | PAT margin | matches line 92 |

### 4b. Meghna Agarwal, Co-founder (lines 73-82)

| # | Line | Number | Context | Flags |
|---|------|--------|---------|-------|
| 1 | 75 | 90% | steady state occupancy | matches operational bullet line 104 |
| 2 | 75 | 86% | overall occupancy | not separately listed as an operational bullet — QUOTE_ONLY_NUMBER |
| 3 | 78 | ₹72 crore | VAS revenue | not separately listed as an operational bullet — QUOTE_ONLY_NUMBER |
| 4 | 79 | 11% | VAS contribution to operating revenue, prior period | QUOTE_ONLY_NUMBER |
| 5 | 79 | 17% | VAS contribution to operating revenue, current period | QUOTE_ONLY_NUMBER |

## 5. Q1FY27 Key Financial Highlights (lines 86-92)

| # | Line | KPI | Flags |
|---|------|-----|-------|
| 1 | 86 | Revenue: ₹428 Cr, growing at 37% YoY | |
| 2 | 88 | EBITDA: ₹87 Cr, YoY growth 34% \| EBITDA Margin: 20% | |
| 3 | 90 | EBIT: ₹55 Cr, growing 59% YoY \| EBIT Margin: 13% | |
| 4 | 92 | Profit After Tax: ₹35 Cr, YoY growth 91% \| PAT Margin: 8% | |

## 6. Q1FY27 Key Operational Highlights (lines 96-104)

| # | Line | KPI | Flags |
|---|------|-----|-------|
| 1 | 96 | Area Under Management: increased by 1.91 Mn sq. ft. YoY, to 10.61 Mn sq. ft. | |
| 2 | 98 | Seat Capacity: increased by 43 K seats to 236 K Seats | |
| 3 | 100 | Center Additions: added 17 new centers YoY | |
| 4 | 102 | Current Portfolio: 137 properties across 17 cities pan-India | |
| 5 | 104 | Occupancy: healthy 90% steady state center occupancy | |

Note: "overall occupancy 86%" (Meghna quote, line 75) and "VAS revenue ₹72 Cr / VAS
contribution 11%→17%" (Meghna quote, lines 78-79) are NOT restated as standalone operational
bullets in this list — flag `QUOTE_ONLY_NUMBER` carried from section 4b.

## 7. Credit rating (line 106)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 106 | Credit Rating: CRISIL 'A+' (Stable) rating, reaffirming financial strength | no rating agency detail beyond CRISIL A+ Stable; no prior rating cited for comparison |

## 8. Qualitative management claim preceding the table (lines 110-112)

| # | Line | Claim | Flags |
|---|------|-------|-------|
| 1 | 110-112 | "While the company reported strong operating performance with an estimated current tax expense of ₹8.14 Cr in Q1 FY27, a notional loss was recognised under Ind AS reporting, which is primarily due to Ind AS accounting adjustments." | management framing of the Ind AS net loss as "notional" — interpretive claim, not itself a number |

## 9. Consolidated Financial Highlights narrative numbers (lines 110-113)

| # | Line | Number | Context | Flags |
|---|------|--------|---------|-------|
| 1 | 111 | ₹8.14 Cr | estimated current tax expense, Q1 FY27 | |
| 2 | 113 | 61% | Ind AS EBITDA margin | |
| 3 | 113 | ₹258 Cr | Ind AS EBITDA (absolute) | |
| 4 | 113 | ₹24 Cr | Ind AS net loss | matches table row "Profit/(loss) after tax", Q1FY27 Ind AS column = (24) |

## 10. Reconciliation table — structure (lines 114-117)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 114-117 | Column header structure: two period blocks (Q1 FY27, Q1 FY26), each with three columns (Ind AS, Ind AS Adj., IGAAP-Equivalent) | |

## 11. Reconciliation table — every row, every cell (lines 118-135)

Columns: Q1FY27-IndAS / Q1FY27-IndAS-Adj / Q1FY27-IGAAP-Eq / Q1FY26-IndAS / Q1FY26-IndAS-Adj / Q1FY26-IGAAP-Eq.
Every cell value is enumerated below; cells valued exactly 0 are flagged `ZERO_STANDING` inline.

| # | Line | Particulars | Q1FY27 IndAS | Q1FY27 IndAS Adj. | Q1FY27 IGAAP Eq. | Q1FY26 IndAS | Q1FY26 IndAS Adj. | Q1FY26 IGAAP Eq. | Cell flags |
|---|------|-------------|--------------|--------------------|--------------------|--------------|---------------------|---------------------|------------|
| 1 | 118 | Revenue from operations | 423 | (6) | 428 | 309 | (4) | 313 | |
| 2 | 119 | Other income | 26 | 18 | 8 | 15 | 15 | 0 | Q1FY26-IGAAP-Eq=0 ZERO_STANDING |
| 3 | 120 | Total Income | 449 | 13 | 436 | 324 | 11 | 313 | |
| 4 | 121 | Purchases of traded goods | 27 | 0 | 27 | 10 | 0 | 10 | Q1FY27-IndAS-Adj=0 ZERO_STANDING; Q1FY26-IndAS-Adj=0 ZERO_STANDING |
| 5 | 122 | Employee benefit expense | 24 | 0 | 24 | 20 | 0 | 20 | Q1FY27-IndAS-Adj=0 ZERO_STANDING; Q1FY26-IndAS-Adj=0 ZERO_STANDING |
| 6 | 123 | Finance costs | 127 | 116 | 11 | 110 | 100 | 10 | |
| 7 | 124 | — Interest on borrowings | 11 | 0 | 11 | 10 | 0 | 10 | Q1FY27-IndAS-Adj=0 ZERO_STANDING; Q1FY26-IndAS-Adj=0 ZERO_STANDING |
| 8 | 125 | — Interest on lease liabilities | 116 | 116 | 0 | 100 | 100 | 0 | Q1FY27-IGAAP-Eq=0 ZERO_STANDING; Q1FY26-IGAAP-Eq=0 ZERO_STANDING |
| 9 | 126 | Depreciation & Amortization expense | 188 | 148 | 40 | 143 | 113 | 30 | |
| 10 | 127-129 | — Property, Plant, Equipment & Intangible Asset | 40 | 0 | 40 | 30 | 0 | 30 | Q1FY27-IndAS-Adj=0 ZERO_STANDING; Q1FY26-IndAS-Adj=0 ZERO_STANDING |
| 11 | 130 | — ROU (Right-of-use Assets) | 148 | 148 | 0 | 113 | 113 | 0 | Q1FY27-IGAAP-Eq=0 ZERO_STANDING; Q1FY26-IGAAP-Eq=0 ZERO_STANDING |
| 12 | 131 | Other expenses | 113 | 178 | 291 | 91 | (127) | 218 | |
| 13 | 132 | Total expenses | 479 | 86 | 393 | 374 | 86 | 289 | |
| 14 | 133 | Profit / (loss) before tax | (30) | (74) | 43 | (50) | (74) | 25 | |
| 15 | 134 | Tax expense | (7) | (15) | 8 | (13) | (19) | 6 | |
| 16 | 135 | Profit / (loss) after tax | (24) | (59) | 35 | (37) | (55) | 19 | matches narrative line 113 net loss ₹24 Cr |

Row count: 16. Cell count: 16 x 6 = 96. Zero-valued cells: 13 (rows 2, 4, 5, 7, 8, 10, 11 — every
row carries at least one ZERO_STANDING cell except rows 1, 3, 6, 9, 12, 13, 14, 15, 16). All 13
zero cells sit in the "Ind AS Adj." or "IGAAP-Equivalent" columns, consistent with the Ind AS 116
lease-accounting split explained in section 12 below (these are not missing disclosures — they
are the mechanical zero that results from splitting a wholly-IndAS-116 line item, e.g. interest
on lease liabilities has IGAAP-Equivalent = 0 by construction since IGAAP does not recognise a
separate lease-interest line).

## 12. Variance / reconciliation footnote (lines 137-144)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 137-138 | "The variance between Ind AS and IGAAP-equivalent reporting arises mainly from non-cash accounting impacts, primarily on account of Ind AS 116, such as;" | |
| 2 | 139 | Bullet: Depreciation on Right-of-Use (ROU) assets | |
| 3 | 140 | Bullet: Interest on lease liabilities | |
| 4 | 141-142 | "These adjustments are purely accounting in nature and do not affect the company's underlying operating strength. IndiQube's core business, continues to demonstrate robust profitability and cash generation." | interpretive management claim |
| 5 | 143-144 | Pointer: "Refer to the Investor Presentation for a detailed reconciliation between Ind AS and IGAAP equivalent financials." | cross-references a document not present in this extract |

## 13. Financial Statements section (lines 147-150)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 148-149 | "Results for the quarter ended Jun 30, 2026, prepared under Ind AS, along with segment results, are available in the Investor Relations section of our website" | segment results referenced but not present in this extract |
| 2 | 150 | URL: https://indiqube.com/investor/ | |

## 14. Quarterly Conference Call section (lines 153-160)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 154 | Call date/time: Thursday, Aug 13, 2026, at 2:00 PM (IST) | |
| 2 | 154-156 | Purpose: discuss Financial Results and performance for quarter ended Jun 30, 2026 | |
| 3 | 157 | Dial-in number 1: 91 22 6280 1366 | |
| 4 | 157 | Dial-in number 2: +91 22 7115 8267 | |
| 5 | 157 | "Click Here" universal access link reference | link target not resolvable from text extract |
| 6 | 158-159 | Statement: analyst(s)/institutional investor(s) presentation will be submitted to Stock Exchanges | |
| 7 | 160 | URL (presentation hosting): https://indiqube.com/investor/ | duplicate URL of item 13.2, distinct mention |

## 15. About IndiQube (lines 163-168)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 164-165 | Description: "IndiQube is one of India's leading integrated managed spaces platforms, bringing together real estate, technology, operations, sustainability and employee experience." | |
| 2 | 165 | Business unit: Grow | |
| 3 | 165-166 | Business units: DesignQube and IndiQare | |
| 4 | 166-167 | Client segments: GCCs, Indian conglomerates, unicorns and high growth startups | |
| 5 | 168 | Closing scope statement: "across their PAN India requirements" | |

## 16. Contact Information (lines 169-176)

| # | Line | Column | Field | Value | Flags |
|---|------|--------|-------|-------|-------|
| 1 | 172 | IndiQube IR | Entity name | Indiqube Spaces Limited | |
| 2 | 173 | IndiQube IR | CIN | L45400KA2015PLC133523 | matches cover-letter CIN line 53 |
| 3 | 174 | IndiQube IR | Email | cs.compliance@indiqube.com | distinct from cover-letter email vinfo@indiqube.com (line 49) |
| 4 | 175 | IndiQube IR | Website | https://indiqube.com/ | |
| 5 | 172 | IR Representative | Name | Mr. Anuj Sonpal | |
| 6 | 173 | IR Representative | Firm | Valorem Advisors | |
| 7 | 174 | IR Representative | Tel | +91-22-4903-9500 | |
| 8 | 175 | IR Representative | Email | indi@valoremadvisors.com | |
| 9 | 176 | IR Representative | Kit link | https://www.valoremadvisors.com/indiqube | |

---

## Flags summary

- `ZERO_STANDING` — 13 instances, all in reconciliation table cells (section 11), rows 2, 4, 5,
  7, 8, 10, 11. Mechanical zeros from the Ind AS 116 lease-accounting split (IGAAP does not
  carry a separate lease-interest/ROU line; several Ind AS Adj. columns are zero for line items
  IGAAP does not adjust). Not silently dropped — carried per row above.
- `QUOTE_ONLY_NUMBER` — 3 instances (section 4b, items 2-4: overall occupancy 86%, VAS revenue
  ₹72 Cr, VAS contribution 11%→17%): numbers spoken by management in the Meghna Agarwal quote
  that do not appear as standalone bullets in the Key Operational Highlights list. A3/A4 should
  check whether this is a completeness gap in the bullet list or an intentional quote-only
  disclosure.
- No `ENTITY_CHANGE`, `MGMT_ABSENCE`, `REPEAT_QUESTION`, or `DROPPED_SLIDE` flags apply — this
  doctype carries no entity list, no concall transcript turns, and no prior-quarter ledger
  (PRIOR_LEDGER_PATH = NONE) to diff against.

---

```yaml
stage: A2-enumerator
company: "INDIQUBE"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/ledger_presentation-pressrelease_indiqube_q1fy27.md"
counts:
  notes: 5                         # variance/reconciliation footnote items (section 12)
  line_items: 16                   # reconciliation table rows (section 11)
  zero_standing: 13                # zero-valued reconciliation-table cells (section 11)
  agenda_items: 0                  # not applicable (no board-outcome letter in this doc)
  auditor_paras: 0                 # not applicable (no auditor report in this doc)
  entities: 0                      # not applicable (no consolidation entity list in this doc)
  turns: 0                         # not applicable (no concall transcript in this doc)
  questions: 0                     # not applicable (no concall transcript in this doc)
  mgmt_numbers: 16                 # numbers in Rishi Das + Meghna Agarwal quotes (section 4)
  slides: 0                        # not applicable (source is a press release, not a slide deck)
  slide_numbers: 0
  table_cells: 96                  # every cell, reconciliation table (section 11)
  kpi_financial_highlights: 4      # section 5
  kpi_operational_highlights: 5    # section 6
  headline_numbers: 4              # section 3
  narrative_numbers: 4             # section 9
  credit_rating_lines: 1           # section 7
  cover_letter_fields: 15          # section 1
  financial_statements_fields: 2   # section 13
  concall_fields: 7                # section 14
  about_fields: 5                  # section 15
  contact_fields: 9                # section 16
  press_dateline: 1                # section 2
  qualitative_claims: 1            # section 8
  table_metadata: 1                # section 10
flags_raised: [ZERO_STANDING, QUOTE_ONLY_NUMBER]
gate_a2: pass
mismatch_note: ""
```
