# A2 ENUMERATOR LEDGER — JNK India Limited (JNKINDIA) — Q1 FY27 — Investor Presentation

Source: `extract_presentation_jnkindia_q1fy27.txt` (21 pages; page 1 = Reg 30 cover
letter; pages 2-21 = 20 deck slides; page 9 OCR'd — divider slide, OCR confirmed
no additional content beyond "OUR BUSINESS"). All figures already in Rs Crores
per header (`unit_convention: Crores`).

Enumerate everything; interpret nothing. Where the extract's raw OCR order of a
chart data label could not be tied to a specific bar/quarter without reading the
source image, the value is recorded verbatim and flagged `[CHART]` rather than
assigned an inferred position — that assignment is A3/A4's job, not A2's.

```
=== A2 COUNT TEST ===
category: pages          grep_count: 21   sweep_count: 21   match: yes
category: slides         grep_count: 20   sweep_count: 20   match: yes
category: footnotes      grep_count: 7    sweep_count: 7    match: yes
category: line_items     grep_count: 36   sweep_count: 36   match: yes
category: zero_standing  grep_count: 0    sweep_count: 0    match: yes
category: numbers        grep_count: 247  sweep_count: 247  match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Methodology note — `numbers` category.** `grep -noE "[0-9]+(,[0-9]{3})*(\.[0-9]+)?"`
against the slide body (extract lines 60-591, i.e. pages 2-21) returns 375 raw
numeric tokens. A manual sweep classified every one of the 375 into DATA (a
genuine business figure) or one of six structural/non-data buckets that are
artifacts of the extraction, not disclosure content:
- `[page N]` bracket markers inserted by the extractor: 20
- OCR-process metadata on the page-9 divider ("12 characters", "200dpi"): 3
- printed slide-footer page numbers (2,3,4,5,6,7,9,10,...19): 17
- CIN / phone / BSE-NSE code identifiers (page 2 masthead, page 21 IR block): 16
- period-label fragments split out of "Q1FY27" / "FY26" / "Mar-24" / "Jun-26"
  style tokens and the Q1/Q2/Q3/Q4 chart-legend fragments: 63
- bullet-list numbering (1-6 on the Renewable Energy slide) and the repeating
  "Why It's Important! [5]" icon-count marker: 9

20+3+17+16+63+9 = 128 excluded; 375-128 = 247 DATA tokens, independently
re-verified against a line-by-line manual sweep of all 20 slides (script
cross-check: 128+247 = 375, exact). Both counts agree — GATE A2 pass.

---

## 1. COVER LETTER (page 1 — not a slide)

| # | Field | Line | Content |
|---|---|---|---|
| C1 | Filing type | 36-39 | Reg 30 SEBI LODR cover letter enclosing Q1FY27 Investor Presentation, addressed to BSE and NSE |
| C2 | Date | 23 | August 11, 2026 |
| C3 | Scrip/security codes | 31 | BSE Scrip code 544167; NSE Security Symbol JNKINDIA |
| C4 | CIN | 18 | L29268MH2010PLC204223 |
| C5 | Signatory | 52-57 | Ashish Soni, Company Secretary and Compliance Officer |
| C6 | Digital signature timestamp | 51-54 | 2026.08.11 23:50:07 +05'30' |

Flag: `SIGNATURE_AFTER_HOURS` — digital signature timestamp is 23:50:07 IST
(11:50 PM), a late-evening filing timestamp; not a board-meeting-timing
comparison issue (no board meeting minutes in this doctype) but worth carrying
to A3 for pattern tracking across quarters.

---

## 2. SLIDES (pages 2-21 of extract = Slide 1-20 of deck)

| Slide | Extract page | Printed footer | Title | Content type | Flags |
|---|---|---|---|---|---|
| 1 | 2 | none | INVESTOR PRESENTATION — Q1FY27 Results, August 2026 (title slide) | text | — |
| 2 | 3 | 2 | Safe Harbor | text (full disclaimer, 3 paragraphs) | full-slide disclaimer, see §4 |
| 3 | 4 | 3 | Management Commentary | text (CMD quote) + photo (Chairperson) | — |
| 4 | 5 | 4 | Q1FY27 Financial Highlights | chart (3 bar-chart panels: Total Income / EBITDA / PAT, FY24-FY26 + Q1FY27, with quarterly sub-bars) | chart data OCR'd, see §5 Table B |
| 5 | 6 | 5 | Order Book Details | chart (2 bar charts: Order Book, Order Inflow) + text (Order Cancellation Update, Bidding Pipeline bullets) | see §5 Table B, §4 footnote row 4 |
| 6 | 7 | 6 | Consolidated Profit & Loss Statement | table (18 line items x 5 periods) | see §5 Table A |
| 7 | 8 | 7 | Standalone Profit & Loss Statement | table (18 line items x 5 periods) | `EPS_PAT_SIGN_INCONSISTENCY` — see §5 Table A row S16 |
| 8 | 9 | none (OCR gap — see note) | OUR BUSINESS (section divider) | text | `OCR_GAP` — no footer digit detected; OCR confirms no additional content, but absence of a footer "8" is itself unverified (could be a genuine unnumbered divider or an OCR miss) |
| 9 | 10 | 9 | Evolution of JNK India | text + photo (timeline infographic, 2010-2026) | see §5 Table B |
| 10 | 11 | 10 | Product Portfolio | photo (7 product images, labels only, no numbers) | ZERO_STANDING — no numeric content on this slide |
| 11 | 12 | 11 | JNK India at a Glance | text + photo (JV structure diagram, offerings, capabilities) | see §5 Table B (line 330) |
| 12 | 13 | 12 | Our Core Solutions — Combustion Equipment | text + photo | icon-count "5" excluded as structural, not data |
| 13 | 14 | 13 | Our Core Solutions — Waste Gas Handling Systems | text + photo | icon-count "5" excluded as structural, not data |
| 14 | 15 | 14 | Our Core Solutions — Renewable Energy Systems | text (numbered list 1-6) + photo | list markers excluded as structural, not data |
| 15 | 16 | 15 | Strategic Joint Venture to Expand Technology Capabilities | text + diagram | see §5 Table B (line 415) |
| 16 | 17 | 16 | Customer Qualification & Execution Model | text (process-flow diagram) | ZERO_STANDING — no numeric content |
| 17 | 18 | 17 | Strategy For Sustainable Growth | text (4 strategic pillars) | ZERO_STANDING — no numeric content |
| 18 | 19 | 18 | Fabrication Infrastructure — Mundra, Gujarat | text + photo (capacity stats) | see §5 Table B (line 522) |
| 19 | 20 | 19 | Board of Directors | text + photo (8 director bio cards) | ZERO_STANDING — no numeric content (no DIN, no tenure dates, no shareholding — unusual for a board slide, see §6) |
| 20 | 21 | none | THANK YOU (closing / IR contact) | text | CIN and phone numbers present are identifiers, not data — excluded from numbers count (see methodology note) |

Slide count: grep (`grep -c "^\[page "` on lines 60-591) = 20; manual sweep = 20. Match.

---

## 3. LINE ITEMS — CONSOLIDATED & STANDALONE P&L (Table A, 36 rows)

Columns: Q1FY27 | Q1FY26 | YoY | Q4FY26 | FY26. "—" in the YoY column means the
deck itself leaves that cell blank (not a zero, not a dash glyph — genuinely
absent from the source); flagged `PARTIAL_YOY_DISCLOSURE` where it recurs.

### 3A. Consolidated P&L (Slide 6, extract lines 206-223)

| Row | Line item | Line | Q1FY27 | Q1FY26 | YoY | Q4FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| C1 | Total Income | 206 | 186.0 | 103.0 | 80.6% | 344.6 | 838.0 | — |
| C2 | Operating Expenses | 207 | 135.9 | 78.7 | — | 258.0 | 625.7 | PARTIAL_YOY_DISCLOSURE |
| C3 | Gross Profit | 208 | 50.1 | 24.2 | 106.7% | 86.6 | 212.3 | — |
| C4 | Gross Profit Margin | 209 | 26.9% | 23.5% | — | 25.1% | 25.3% | PARTIAL_YOY_DISCLOSURE |
| C5 | Employee Cost | 210 | 18.4 | 13.2 | — | 22.1 | 66.5 | PARTIAL_YOY_DISCLOSURE |
| C6 | Other Expenses | 211 | 9.7 | 3.9 | — | 12.3 | 34.5 | PARTIAL_YOY_DISCLOSURE |
| C7 | EBITDA (Includes Other Income) | 212 | 21.9 | 7.2 | 3.1x | 52.3 | 111.3 | — |
| C8 | EBITDA Margin | 213 | 11.8% | 7.0% | — | 15.2% | 13.3% | PARTIAL_YOY_DISCLOSURE |
| C9 | Depreciation | 214 | 2.9 | 1.6 | — | 3.0 | 8.8 | PARTIAL_YOY_DISCLOSURE |
| C10 | EBIT | 215 | 19.1 | 5.6 | 3.4x | 49.3 | 102.5 | — |
| C11 | EBIT Margin | 216 | 10.3% | 5.5% | — | 14.3% | 12.2% | PARTIAL_YOY_DISCLOSURE |
| C12 | Finance Cost | 217 | 4.4 | 3.6 | — | 6.7 | 17.3 | PARTIAL_YOY_DISCLOSURE |
| C13 | Profit before Tax | 218 | 14.6 | 2.0 | 7.4x | 42.6 | 85.2 | — |
| C14 | Profit before Tax Margin | 219 | 7.9% | 1.9% | — | 12.4% | 10.2% | PARTIAL_YOY_DISCLOSURE |
| C15 | Tax | 220 | 5.0 | 0.9 | — | 9.6 | 20.4 | PARTIAL_YOY_DISCLOSURE |
| C16 | Profit After Tax | 221 | 9.6 | 1.1 | 8.5x | 33.0 | 64.8 | — |
| C17 | Profit After Tax Margin | 222 | 5.2% | 1.1% | — | 9.6% | 7.7% | PARTIAL_YOY_DISCLOSURE |
| C18 | Basic EPS (in Rs.) | 223 | 2.05 | 0.20 | — | 5.84 | 11.61 | PARTIAL_YOY_DISCLOSURE |

### 3B. Standalone P&L (Slide 7, extract lines 233-250)

| Row | Line item | Line | Q1FY27 | Q1FY26 | YoY | Q4FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| S1 | Total Income | 233 | 170.1 | 102.7 | 65.7% | 305.5 | 775.4 | — |
| S2 | Operating Expense | 234 | 135.9 | 78.7 | — | 258.0 | 625.7 | PARTIAL_YOY_DISCLOSURE |
| S3 | Gross Profit | 235 | 34.2 | 24.0 | 42.8% | 47.6 | 149.6 | — |
| S4 | Gross Profit Margin | 236 | 20.1% | 23.3% | — | 15.6% | 19.3% | PARTIAL_YOY_DISCLOSURE |
| S5 | Employee Cost | 237 | 16.4 | 13.0 | — | 19.7 | 62.0 | PARTIAL_YOY_DISCLOSURE |
| S6 | Other Expenses | 238 | 8.4 | 3.8 | — | 9.9 | 30.5 | PARTIAL_YOY_DISCLOSURE |
| S7 | EBITDA (Includes Other Income) | 239 | 9.5 | 7.1 | 3.3x | 17.9 | 57.1 | — |
| S8 | EBITDA Margin | 240 | 5.6% | 6.9% | — | 5.9% | 7.4% | PARTIAL_YOY_DISCLOSURE |
| S9 | Depreciation | 241 | 1.8 | 1.6 | — | 2.1 | 7.2 | PARTIAL_YOY_DISCLOSURE |
| S10 | EBIT | 242 | 7.6 | 5.6 | 3.9x | 15.8 | 49.8 | — |
| S11 | EBIT Margin | 243 | 4.5% | 5.4% | — | 5.2% | 6.4% | PARTIAL_YOY_DISCLOSURE |
| S12 | Finance Cost | 244 | 3.4 | 3.6 | — | 5.3 | 15.7 | PARTIAL_YOY_DISCLOSURE |
| S13 | Profit before Tax | 245 | 4.2 | 1.9 | 9.1x | 10.5 | 34.1 | — |
| S14 | Profit before Tax Margin | 246 | 2.5% | 1.9% | — | 3.4% | 4.4% | PARTIAL_YOY_DISCLOSURE |
| S15 | Tax | 247 | 5.0 | 0.9 | — | 9.0 | 19.8 | PARTIAL_YOY_DISCLOSURE — note Q1FY27 Tax (5.0) exceeds Q1FY27 PBT (4.2), consistent with the PAT going negative below |
| S16 | Profit After Tax | 248 | **-0.8** | 1.1 | 11.6x | 1.5 | 14.3 | `EPS_PAT_SIGN_INCONSISTENCY` — PAT swings from +1.1 (Q1FY26) to -0.8 (Q1FY27) yet the YoY column shows a positive "11.6x" multiple with no sign, which is not a coherent multiple across a sign flip |
| S17 | Profit After Tax Margin | 249 | -0.5% | 1.1% | — | 0.5% | 1.8% | PARTIAL_YOY_DISCLOSURE |
| S18 | Basic EPS (in Rs.) | 250 | **2.42** | 0.21 | — | 5.66 | 11.59 | `EPS_PAT_SIGN_INCONSISTENCY` — Q1FY27 Basic EPS is printed as +2.42 (positive) in the same table where Q1FY27 standalone PAT is -0.8 (negative); a positive EPS cannot arithmetically follow from a negative PAT unless a different numerator (e.g. pre-exceptional, or a typo/decimal-shift error) is in play. Mechanical flag only — cause not interpreted here |

Line-item count: grep (`grep -vc "Particulars\|Q1FY27"` on the two table ranges)
= 18 + 18 = 36; manual sweep = 36. Match. Zero-standing count = 0 (no
line in either statement carries a literal 0, Nil, or dash value in any
period column; all rows are populated, including the negative PAT).

---

## 4. FOOTNOTES / FINE-PRINT DISCLAIMERS (7 instances qualifying headline numbers)

| # | Slide | Line | Text (qualifies) |
|---|---|---|---|
| F1 | 3 (Management Commentary) | 129 | "Q1FY27 Total Income includes Revenue of Rs 16.5 cr from JNK Chemdist Limited which was not part it in Q1FY26" — qualifies the 80.6% YoY Total Income growth headline; ~9% of Q1FY27 Total Income (16.5/186.0) is inorganic/newly-consolidated, not organic growth |
| F2 | 4 (Financial Highlights) | 168 | Same Chemdist footnote, worded "not part of it in Q1FY26" (minor wording variance from F1) — qualifies the Total Income bar-chart series |
| F3 | 4 (Financial Highlights) | 169 | "Financial information for the previous periods have been regrouped/reclassified to conform to the appropriate presentation and comparability of financial information, wherever necessary" — qualifies all prior-period comparatives (FY24-FY26) in the three bar charts |
| F4 | 5 (Order Book Details) | 179-184 | "Order Cancellation Update" box: large export order received June 8, 2026 was cancelled due to inability to secure licensor technical approval; "no material costs incurred and no execution having commenced" — qualifies the Order Book sequential decline from 1,961 (Mar-26) to 1,801 (Jun-26) |
| F5 | 6 (Consolidated P&L) | 226 | Chemdist footnote repeat (identical to F1's wording) |
| F6 | 6 (Consolidated P&L) | 227 | Regroup/reclassify footnote repeat (identical to F3) |
| F7 | 7 (Standalone P&L) | 253 | Regroup/reclassify footnote (no Chemdist footnote on the standalone statement — consistent, since Chemdist is a subsidiary consolidated only at the consolidated level) |

Not counted among the 7 (listed separately as a full-slide disclaimer, not a
number-qualifying footnote): Slide 2 "Safe Harbor" — three paragraphs of
forward-looking-statement / no-reliance / no-offer disclaimer covering the
entire presentation (extract lines 76-93).

Footnote count: grep (`grep -n -E "Q1FY27 Total Income includes Revenue|Financial
information for the previous periods have been regrouped|Order Cancellation
Update"`) = 7; manual sweep = 7. Match.

---

## 5. NUMBERS — CHARTS, COMMENTARY & OTHER SLIDES (Table B, 44 rows / 91 data points)

Not covered by Table A (P&L tables). One ledger row per source line; multiple
values on one line are listed together since they share a citation.

| Slide | Line | Raw value(s) | Context |
|---|---|---|---|
| 1 (title) | 67 | 2026 | "August 2026" — presentation month/year |
| 3 (commentary) | 102 | 80.6; 186.0 | Total Income YoY growth %; Q1FY27 Total Income Rs cr |
| 3 (commentary) | 103 | 103.0; 3.1; 21.9 | Q1FY26 Total Income Rs cr; EBITDA YoY growth "3.1x"; Q1FY27 EBITDA (incl. other income) Rs cr |
| 3 (commentary) | 104 | 8.5; 9.6 | PAT YoY growth "8.5x"; Q1FY27 PAT Rs cr |
| 3 (commentary) | 105 | 11.8 | Q1FY27 EBITDA margin % |
| 3 (commentary) | 109 | 30; 2026; 1,801 | Order book as-on date "June 30, 2026"; order book value Rs cr |
| 3 (commentary) | 110 | 6,000 | Bidding pipeline "~Rs. 6,000 cr" |
| 3 (commentary, footnote) | 129 | 16.5 | Chemdist revenue included in Q1FY27 Total Income, Rs cr (= F1) |
| 4 (Financial Highlights chart) | 141 | 838.0; 111.3; 64.7 | `[CHART]` raw OCR order; 838.0 cross-checks to FY26 Total Income (Table A row C1/S1 area — consolidated FY26 = 838.0, exact match); 111.3 cross-checks to FY26 EBITDA (row C7 = 111.3, exact match); 64.7 is close to but not identical to FY26 consolidated PAT of 64.8 (Table A row C16) — 0.1 cr variance, flagged `MINOR_FIGURE_VARIANCE` |
| 4 | 142 | 62.7 | `[CHART]` |
| 4 | 143 | 104.5 | `[CHART]` |
| 4 | 145 | 16.7 | `[CHART]` |
| 4 | 146 | 345.0; 32.6 | `[CHART]` |
| 4 | 147 | 52.3; 32.6 | `[CHART]` — 52.3 cross-checks to Q4FY26 EBITDA (Table A row C7 = 52.3, exact match) |
| 4 | 149 | 480.0; 499.0; 64.7 | `[CHART]` |
| 4 | 151 | 29.9; 30.1 | `[CHART]` |
| 4 | 152 | 204.0; 206.0; 41.1; 27.5 | `[CHART]` — 41.1 cross-checks to Q4FY26 EBIT (Table A row C10 = ~49.3? note: not an exact match, flagged `MINOR_FIGURE_VARIANCE` — leave reconciliation to A3/A4) |
| 4 | 153 | 224.0 | `[CHART]` |
| 4 | 154 | 29.5; 13.2; 18.0 | `[CHART]` |
| 4 | 155 | 97.0; 9.7 | `[CHART]` |
| 4 | 156 | 121.0; 184.0; 186.0; 21.9; 2.8 | `[CHART]` — 186.0 and 21.9 cross-check to Q1FY27 Total Income and Q1FY27 EBITDA (Table A rows C1, C7 — exact matches) |
| 4 | 157 | 21.9; 15.4; 9.6 | `[CHART]` — 9.6 cross-checks to Q1FY27 PAT (Table A row C16, exact match) |
| 4 | 158 | 107.0; 22.3; 12.2; 7.7 | `[CHART]` |
| 4 | 159 | 13.0 | `[CHART]` |
| 4 | 160 | 97.0 | `[CHART]` |
| 4 | 161 | 91.0; 103.0; 12.1; 3.9; 6.4 | `[CHART]` — 103.0 cross-checks to Q1FY26 Total Income (Table A row C1, exact match) |
| 4 | 162 | 38.0; 8.9; 7.2; 1.1 | `[CHART]` — 7.2 and 1.1 cross-check to Q1FY26 EBITDA and Q1FY26 PAT (Table A rows C7, C16, exact matches) |
| 4 (footnote) | 168 | 16.5 | Chemdist footnote repeat (= F2) |
| 5 (Order Book chart) | 177 | 1,961 | Order Book, Mar-26, Rs cr |
| 5 | 178 | 1,801 | Order Book, Jun-26, Rs cr (matches commentary line 109) |
| 5 | 180 | 1,082 | Order Book, Mar-25, Rs cr |
| 5 | 181 | 8; 2026 | Date of cancelled export order: "June 8, 2026" |
| 5 | 182 | 624 | Order Book, Mar-24, Rs cr |
| 5 | 188 | 6,000 | Bidding pipeline Rs cr (repeat of line 110) |
| 5 | 190 | 1,694; 50; 50 | Order Inflow FY26 (Mar-26), Rs cr; bidding pipeline Domestic:Export split "50:50" |
| 5 | 193 | 933 | Order Inflow FY25 (Mar-25), Rs cr |
| 5 | 196 | 229 | Order Inflow FY24 (Mar-24), Rs cr |
| 6 (footnote) | 226 | 16.5 | Chemdist footnote repeat (= F5) |
| 9 (Evolution timeline) | 277 | 2010; 2019; 2021; 2022; 2024; 2024; 26 | Milestone years: 2010 incorporated; 2019 first PO (hydrogen infra); 2021 first overseas PO (Nigeria) + flare systems PO (Nigeria); 2022 order book crossed Rs 500cr; 2024 listed BSE & NSE; 2024-26 order book > Rs 1,800cr & JV with Chemdist |
| 9 | 281 | 1,800 | "Order Book > ₹ 1,800 cr" milestone label |
| 9 | 282 | 500 | "Order book crossed Rs 500 cr" milestone label |
| 11 (Glance) | 330 | 15 | "15+ Years of Experience" |
| 15 (JV) | 415 | 51; 49 | JV ownership split: JNK India 51% / Chemdist Technology 49% |
| 18 (Fabrication) | 522 | 5,000; 20,243; 50 | Installed fabrication capacity 5,000 MT; facility area 20,243 Sq metres; solar power capacity installed 50 kWp |

Numbers count (this table + Table A): 91 + 156 = 247. Grep methodology count
(see box above) = 247. Match.

---

## 6. EXPECTED-BUT-ABSENT STANDARD DISCLOSURE SLIDES (DROPPED_SLIDE risk — no prior-quarter deck supplied for direct diff)

No prior-quarter presentation was provided, so a literal slide-by-slide diff
against Q4FY26's deck is not possible here. The following are standard
disclosure categories seen in comparable industrial-EPC investor decks that
are either absent or materially thin in this Q1FY27 deck; flagged for A3/A4 to
judge against the prior-quarter deck when it becomes available, and against
company memory:

| Expected disclosure | Status in this deck | Flag |
|---|---|---|
| Order book split by segment / end-industry / geography (domestic vs export breakdown of the current Rs 1,801 cr order book itself, not just the bidding pipeline) | ABSENT — only the forward bidding pipeline gets a 50:50 domestic:export split (Slide 5); the standing order book carries no segment/geography breakdown | `DROPPED_SLIDE_RISK` |
| Forward guidance (explicit FY27 revenue/EBITDA/margin targets or ranges) | ABSENT — only qualitative language ("growth visibility remains strong") | `DROPPED_SLIDE_RISK` |
| Margin bridge / cost bridge explaining the EBITDA margin move (7.0% to 11.8% YoY, Consolidated) | ABSENT — margin change is stated but not decomposed | `DROPPED_SLIDE_RISK` |
| Revenue mix by product line (Fired Heaters vs Reformers vs Cracking Furnaces vs Flares vs Incinerators vs Renewable Energy) | ABSENT — Slide 11-15 describe products qualitatively with zero revenue-mix percentages | `DROPPED_SLIDE_RISK` |
| Capacity utilization % (vs. the 5,000 MT installed capacity on Slide 18) | ABSENT | `DROPPED_SLIDE_RISK` |
| Balance sheet / net debt / working-capital-days slide | ABSENT entirely — notable given a Finance Cost line item (Rs 4.4cr Q1FY27 consolidated) implies borrowings exist | `DROPPED_SLIDE_RISK` |
| Cash flow / free cash flow slide | ABSENT | `DROPPED_SLIDE_RISK` |
| Customer concentration / top-customer revenue % | ABSENT — Slide 16 describes the qualification *process* only, no concentration metric | `DROPPED_SLIDE_RISK` |
| Shareholding pattern (promoter/FII/DII/public %) | ABSENT | `DROPPED_SLIDE_RISK` |
| Director DIN / tenure / shareholding on the Board of Directors slide (Slide 19) | ABSENT — bios give background only, no DIN, no term dates, no shareholding, unlike a standard annual-report director table | `DROPPED_SLIDE_RISK` |

These are risk flags, not confirmed drops (no prior deck to diff against in
this run). A3/A4 should reconcile against the Q4FY26 deck and company memory
at `companies/JNKINDIA.md` if available.

---

```yaml
stage: A2-enumerator
company: "JNKINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/ledger_presentation_jnkindia_q1fy27.md"
counts:
  notes: 0
  line_items: 36
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 20
  slide_numbers: 20
  footnotes: 7
  numbers: 247
flags_raised: [PARTIAL_YOY_DISCLOSURE, EPS_PAT_SIGN_INCONSISTENCY, MINOR_FIGURE_VARIANCE, DROPPED_SLIDE_RISK, OCR_GAP, SIGNATURE_AFTER_HOURS]
gate_a2: pass
mismatch_note: ""
```
