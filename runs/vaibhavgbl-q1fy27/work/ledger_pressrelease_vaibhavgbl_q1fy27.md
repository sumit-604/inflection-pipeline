# A2 ENUMERATION LEDGER — Vaibhav Global Limited (VAIBHAVGBL), Q1 FY27
Doctype as tasked: `presentation`. Actual document content (per A1 header and body):
NSE/BSE cover letter + management press release (5 pages), NOT a slide deck.
Flagged below as `DOCTYPE_LABEL_MISMATCH`. Categories below are adapted from
the RESULTS FILING enumeration rules (closest fit) since no slides, no
transcript turns, no board-agenda items, and no auditor report exist in this
artifact.

Source: `/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/extract_pressrelease_vaibhavgbl_q1fy27.txt`
Line count: 232 (per A1 header). Page count: 5.

```
=== A2 COUNT TEST ===
category: document_headers               grep_count: 11  sweep_count: 11  match: yes
category: letter_metadata                 grep_count: 4   sweep_count: 4   match: yes
category: signature_block                 grep_count: 1   sweep_count: 1   match: yes
category: page_footers                    grep_count: 5   sweep_count: 5   match: yes
category: page_markers                    grep_count: 5   sweep_count: 5   match: yes
category: dividend_declaration            grep_count: 1   sweep_count: 1   match: yes
category: headline_numbers                grep_count: 3   sweep_count: 3   match: yes
category: financial_table_line_items      grep_count: 7   sweep_count: 7   match: yes
category: table_footnotes                 grep_count: 2   sweep_count: 2   match: yes
category: key_business_metrics            grep_count: 4   sweep_count: 4   match: yes
category: esg_initiatives                 grep_count: 3   sweep_count: 3   match: yes
category: md_quote_attribution            grep_count: 1   sweep_count: 1   match: yes
category: md_quote_paragraphs             grep_count: 8*  sweep_count: 8   match: yes
category: md_quote_numbers                grep_count: 7   sweep_count: 7   match: yes
category: about_section_facts             grep_count: 5   sweep_count: 5   match: yes
category: contacts                        grep_count: 3   sweep_count: 3   match: yes
category: safe_harbor                     grep_count: 1   sweep_count: 1   match: yes
category: zero_standing_items             grep_count: 0   sweep_count: 0   match: yes
TOTAL DISCLOSURE UNITS ENUMERATED: 71
gate_a2: pass
=== END COUNT TEST ===
```
`*md_quote_paragraphs` reconciliation note: raw blank-line grep
(`awk` scan of lines 121-175 for `^$`) returns 9 blank-line separators,
which would imply 10 paragraphs. Manual sweep found 2 of those 9 blanks
(after line 154 "Page | 2" and after line 158 "[page 4]") are PDF
pagination artifacts, not paragraph breaks — the sentence starting at
line 153 ("Our AI-led initiatives across") completes only at line 160
("marketing, merchandising and supply chain continue to scale well...").
Excluding the 2 pagination blanks, both methods converge on 7 true
paragraph separators = 8 paragraphs. Re-swept and reconciled per GATE A2
rule 4 before emission; not a genuine miss.

---

## 1. Document headers / section titles
| # | Line(s) | Text | Flags |
|---|---------|------|-------|
| 1 | 56 | "PRESS RELEASE" | |
| 2 | 58 | "Q1 FY27 Financial Results" (title) | |
| 3 | 59-60 | "Improved Digital Traction, Higher In-House Brand Mix, and Strong Growth Across Markets Drive Performance" (subtitle) | |
| 4 | 64-66 | Dateline intro: "Jaipur, August 04, 2026: Vaibhav Global Limited (VGL)... announced its financial results for the quarter ending June 30, 2026." | |
| 5 | 74 | "Financial Performance Highlights:" (section header) | |
| 6 | 95 | "Key Business Metrics:" (section header) | |
| 7 | 108 | "ESG Initiatives:" (section header) | |
| 8 | 179 | "– ENDS –" | |
| 9 | 181 | "About Vaibhav Global Limited" (section header) | |
| 10 | 194 | "For further information, please contact:" (section header) | |
| 11 | 219 | "Safe Harbor" (section header) | |

## 2. Cover letter metadata (exchange transmittal, page 1)
| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 1 | 17 | Ref | VGL/CS/2026/70 | |
| 2 | 17 | Date | 04th August, 2026 | |
| 3 | 23 | Symbol (NSE) | VAIBHAVGBL | |
| 4 | 23 | Scrip Code (BSE) | 532156 | |

Addressees: National Stock Exchange of India Limited (line 19) and BSE
Limited (line 19) — both named, one letter. Subject line (line 25):
"Press Release." Enclosure line (line 29): "Q1 FY27 Financial Results."

## 3. Digital signature block
| # | Lines | Signatory | Designation | Membership No. | Timestamp | Flags |
|---|-------|-----------|-------------|-----------------|-----------|-------|
| 1 | 37-44 | Yashasvi Pareek | Company Secretary & Compliance Officer | A39220 | 2026.08.04 23:30:22 +05'30' | Signed 23:30 IST — no board-meeting timing is stated anywhere in this doc, so a before/after-meeting check is NOT FOUND (no board meeting start/end time disclosed in this artifact) |

## 4. Page footers (registered-office boilerplate, repeated per page)
| # | Line | Page | Text variant | Flags |
|---|------|------|---------------|-------|
| 1 | 52-53 | 1 | "Registered Office: E-69, EPIP, Sitapura Industrial Area, Jaipur-302022, Rajasthan, India • Phone: +91-141-2770648; +91-141-2771975 • CIN: L36911RJ1989PLC004945 • Email... • Website..." | Fuller form, page 1 only |
| 2 | 104-105 | 2 | "Regd. Office: ... Tele: 91-141-2771975; CIN: L36911RJ1989PLC004945; Email...; Web..." | Abbreviated form |
| 3 | 156-157 | 3/4 boundary | same abbreviated form | |
| 4 | 215-216 | 4 | same abbreviated form | |
| 5 | 231-232 | 5 | same abbreviated form | |

## 5. Page markers (A1 extract pagination)
| # | Line | Marker |
|---|------|--------|
| 1 | 15 | [page 1] |
| 2 | 55 | [page 2] |
| 3 | 107 | [page 3] |
| 4 | 159 | [page 4] |
| 5 | 218 | [page 5] |

## 6. Dividend declaration
| # | Line | Text | Flags |
|---|------|------|-------|
| 1 | 61 | "Declared interim dividend of Rs. 1.5/equity share" | Record date, payment date, and book-closure dates NOT FOUND in this document |

## 7. Headline performance numbers (dateline banner, page 2)
| # | Line | Metric | Value | Flags |
|---|------|--------|-------|-------|
| 1 | 70 | Revenue | INR 917 Cr, up 13% YoY | |
| 2 | 71 | EBITDA | INR 102 Cr, up 37% YoY | |
| 3 | 72 | PAT | INR 56 Cr, up 50% YoY | |

## 8. Financial Performance Highlights table (lines 76-90)
Columns: Q1FY27 | Q1FY26 | YoY Growth | Q4FY26 | QoQ Growth
| # | Line | Line item | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flags |
|---|------|-----------|--------|--------|-----|--------|-----|-------|
| 1 | 78 | Revenue | 917 | 814 | 13% | 935 | -2% | |
| 2 | 80 | EBITDA | 102 | 75 | 37% | 96 | 6% | |
| 3 | 82 | Gross Margin | 68% | 64% | 417 bps | 64% | 402 bps | |
| 4 | 84 | PAT | 56 | 38 | 50% | 44* | 29% | Q4FY26 PAT of 44 is asterisked, tied to footnote 1 (see below) — the 29% QoQ growth figure for PAT is computed off the footnoted, MAT-credit-adjusted 44, not an as-reported number; NOT independently re-derivable from this document alone |
| 5 | 86 | Net Cash | 287 | 174 | 65% | 296 | (3%) | |
| 6 | 88 | Digital revenue mix | 45% | 43% | 210 bps | 45% | 10 bps | |
| 7 | 90 | In-House Brands | 57% | 36% | 2200 bps | 53% | 420 bps | |

## 9. Table footnotes
| # | Line | Text | Flags |
|---|------|------|-------|
| 1 | 91 | "Note: * PAT is excluding MAT credit of Rs. 47.6 cr" | Ties to row 4 above (Q4FY26 PAT = 44*) |
| 2 | 92 | "2.Numbers are rounded off to nearest figure" | Standing rounding disclaimer |

## 10. Key Business Metrics (lines 96-99)
| # | Line | Metric | Value | Flags |
|---|------|--------|-------|-------|
| 1 | 96 | Unique Customers (TTM) | 677 lakhs | |
| 2 | 97 | New Customer Acquisitions (TTM) | 3.5 lakhs | |
| 3 | 98 | Customer Retention Rate | sustained at 38% | "sustained" implies prior-period value also 38%; prior-period figure itself NOT FOUND in this document |
| 4 | 99 | Repeat Purchase | 23 pieces per customer (TTM) | |

## 11. ESG Initiatives (lines 110-114)
| # | Line(s) | Item | Value | Flags |
|---|---------|------|-------|-------|
| 1 | 110 | 'Your purchase feeds…' meals donated since inception | Over 115 million meals | `NUMBER_DISCREPANCY` — About-section (row 5 of section 15 below, line 190) states "over 113 million meals... since program's inception" for the same cumulative metric. 115mm vs 113mm within the same press release. |
| 2 | 111-113 | Groundwater recharge systems | Two systems installed near SEZ; ~6.7 lakh ltr annual recharge added; total rainwater harvesting capacity now 10,670 KL/Year | |
| 3 | 114 | ESG Rating Upgrade | ICRA ESG Score improved to '74' (Strong) | Prior-period ICRA ESG score NOT FOUND in this document |

## 12. Management quote — attribution
| # | Lines | Speaker | Title | Flags |
|---|-------|---------|-------|-------|
| 1 | 118-119 | Mr. Sunil Agrawal | Managing Director, Vaibhav Global Limited | |

## 13. Management quote — paragraphs (turns within the single quote block)
| # | Lines | First ~12 words | Flags |
|---|-------|------------------|-------|
| 1 | 121-124 | "We are pleased to report a resilient start to FY27, delivering strong..." | Contains 6 stated numbers (see section 14) |
| 2 | 126-131 | "While reported revenue growth benefited from favourable foreign exchange movements..." | Hedge language: constant-currency revenue "remained broadly flat"; attributes softness to Middle East conflict + cautious consumer spending |
| 3 | 133-137 | "Encouragingly, the fundamentals of our business continue to strengthen. Customer..." | Forward-leaning language, no new numbers |
| 4 | 139-143 | "A key highlight of the quarter was the continued expansion of..." | Contains 1 stated number (57% B2C in-house brand mix) |
| 5 | 145-150 | "We have moved all our retail businesses to Shopify Enterprise ECom..." | Platform-migration disclosure (Shopify Enterprise), no numbers |
| 6 | 152-163 | "Operational excellence remains a core focus across the organization. During..." | Spans a page break (page 3/4 boundary at lines 154-159); no numbers |
| 7 | 165-170 | "Importantly, we believe the investments and strategic initiatives undertaken over..." | "Inflection point" framing; forward-commitment language, no numbers |
| 8 | 172-175 | "Supported by a strong balance sheet, robust cash generation, and a..." | Closing paragraph, no numbers |

## 14. Management quote — every stated number
| # | Line | Number | Context | Flags |
|---|------|--------|---------|-------|
| 1 | 122 | 13% | Revenue growth YoY, quoted | Matches headline number (section 7, row 1) and table (section 8, row 1) |
| 2 | 122 | ₹917 crore | Revenue, quoted | Matches headline/table |
| 3 | 122 | 37% | EBITDA growth YoY, quoted | Matches headline/table |
| 4 | 123 | ₹102 crore | EBITDA, quoted | Matches headline/table |
| 5 | 123 | 50% | PAT growth YoY, quoted | Matches headline/table |
| 6 | 123 | ₹56 crore | PAT, quoted | Matches headline/table |
| 7 | 140 | 57% | In-house brands contribution to B2C revenue, quoted | Matches table row "In-House Brands" Q1FY27 = 57% (section 8, row 7); quote specifies this is of "B2C revenue" specifically, a qualifier not present in the table label itself |

## 15. About Vaibhav Global Limited — facts (lines 181-191)
| # | Line(s) | Fact | Flags |
|---|---------|------|-------|
| 1 | 182-183 | Listing identifiers: BSE 532156, NSE VAIBHAVGBL, ISIN INE884A01027 | |
| 2 | 184 | Household reach: ~129 million households (FTE) | |
| 3 | 185 | TV network brand list: Shop LC (US), Shop TJC & Ideal World (UK), Shop LC (Germany) | |
| 4 | 186-187 | E-commerce website list: shoplc.com, mindfulsouls.com (US); tjc.co.uk, idealworld.tv, rachelgalley.com (UK); shoplc.de (Germany) | |
| 5 | 189-191 | Meal program: over 113 million meals provided (US/UK/Germany/India) since program's inception, run rate ~59,000 meals/school day | `NUMBER_DISCREPANCY` — see section 11, row 1 (115 million figure, line 110) |

## 16. Contacts (lines 197-208)
| # | Lines | Entity/person | Role | Flags |
|---|-------|----------------|------|-------|
| 1 | 197-199 | Vivek Jain, Vaibhav Global Ltd. | Head - Investor Relations | |
| 2 | 197, 198-203 | Muskaan Badlani, Vaibhav Global Ltd. | Corporate Communications | |
| 3 | 205-208 | Ernst & Young LLP (Sumedh Desai / Vikash Verma) | External contact listed on the press release (role/capacity, e.g. PR advisor vs statutory auditor, NOT FOUND — this document does not label the capacity in which EY is listed) | Statutory-auditor status not stated in this artifact |

## 17. Safe Harbor
| # | Lines | Text (paraphrase-free, full paragraph) | Flags |
|---|-------|------------------------------------------|-------|
| 1 | 219-224 | Standard forward-looking-statement disclaimer covering government actions, political/economic developments, technological risks; VGL disclaims responsibility for actions taken on such statements and disclaims any obligation to update | |

## 18. Zero / nil / dash-valued standing items
None found in this document. Every numeric line item in the Financial
Performance Highlights table (section 8) carries a non-zero, non-dash
value in all five reported periods/deltas shown. Swept the full table,
all bullet-point metrics, and all narrative numbers for template zero
rows (e.g., a standing "NIL" or "-" line implying an anticipated/past
transaction type) — none present. `ZERO_STANDING` flag: not applicable
this quarter.

---

## Flags summary
- `DOCTYPE_LABEL_MISMATCH`: task doctype = "presentation"; actual artifact = NSE/BSE cover letter + management press release, no slides.
- `NUMBER_DISCREPANCY` (x2 rows, same underlying fact): cumulative meals donated stated as "over 115 million" (line 110, ESG section) vs "over 113 million" (line 190, About section) — both captioned "since inception" / "since program's inception," same press release, same date.
- `ZERO_STANDING`: none applicable — explicitly swept, none found.
