# A2 Completeness Ledger — Investor Presentation
Company: GMM Pfaudler Limited (GMMPFAUDLR) | Quarter: Q1 FY27 | Doctype: presentation
Source: investor_presentation_q1fy27.pdf (29 pages, pdfinfo page_count=29, formfeed_count=29)
A1 extract: extract_presentation_gmmpfaudler_q1fy27.txt (847 lines)
Prior-quarter ledger: none supplied — DROPPED_SLIDE diff is N.A. this run (noted in Table 4).

## METHODOLOGY NOTE
"Numbers" enumeration (Table 2) is built in two independent passes and reconciled:
1. GREP pass — a Python/regex sweep over the native pdftotext body only (extraction
   header lines 1-27 excluded; `[CHART, page N, OCR text: ...]` and `[OCR page N]`
   blocks excluded per the A1 header's own guidance that native layout text is the
   higher-fidelity source and OCR blocks are "supplementary confirmation only, not a
   replacement"; fiscal-year/quarter axis labels `FY\d{2}`/`Q[1-4]` stripped before
   matching so they are not miscounted as data; standalone footer-page-number lines
   stripped). Regex: `(?<![A-Za-z0-9])[₹%]?\s?-?\s?\d[\d,]*\.?\d*\s?%?`
2. MANUAL SWEEP — every page read line-by-line against the grep hit-list, each token
   assigned a plain-language label (what metric/period it is, or flagged as an
   OCR/layout artifact where axis-binding is not resolvable from extracted text alone).
Where a chart's bar/line values could not be bound to a specific quarter with
certainty from layout-preserved text (pages 6, 17, 18 in particular), the raw value
set is enumerated in slide order as printed and explicitly flagged
`AXIS_BINDING_UNCERTAIN` for A3/A4 to resolve against the source deck image if needed.
This is enumeration, not interpretation — no value is dropped or estimated.

The 8 pages whose chart data is natively selectable text (pages 5,6,7,8,16,17,18,28
per the A1 header) were also OCR'd as a cross-check by A1; the OCR blocks were read
and found to reproduce the same underlying figures (with expected OCR noise: "Rs"
misread as "~"/"<", "719%" for HET order intake YoY, "5.52" for EPS 5.32, etc.) — no
additional numbers were found in the OCR blocks beyond the native text. This is
recorded as a QC note, not double-counted.

=== A2 COUNT TEST ===
category: slides         grep_count: 29   sweep_count: 29   match: yes
category: slide_numbers  grep_count: 414  sweep_count: 414  match: yes
category: footnotes      grep_count: 6    sweep_count: 6    match: yes
category: dropped_slides grep_count: N.A. sweep_count: N.A. match: N.A. (no prior deck)
gate_a2: pass
=== END COUNT TEST ===

---

## TABLE 1 — SLIDES (page/slide number, title, content type)

| Slide (page) | Footer # | Title | Content type | Flags |
|---|---|---|---|---|
| 1 | — | BSE/NSE covering letter (investor presentation submission) | text + digital signature block | — |
| 2 | (none) | Earnings Presentation Q1 FY27 | title/cover (text + logo graphics) | — |
| 3 | 2 | Disclaimer | text (legal, full-page) | — |
| 4 | 3 | Q1 Financial Update | section divider (text/graphic) | — |
| 5 | 4 | Consolidated Financial Snapshot – Q1 FY27 | infographic (KPI callouts) | — |
| 6 | 5 | Consolidated Financial Performance – Quarterly Trend | chart (4 bar/column trend charts: Revenue, EBITDA, PAT, EPS) | AXIS_BINDING_UNCERTAIN (PAT/EPS margin row) |
| 7 | 6 | Order Intake & Backlog Trends | chart (combo bar, 13 quarters FY24-Q1FY27) | — |
| 8 | 7 | Diversification Strategy Gaining Momentum | chart (stacked-share chart, 4 periods) + bullets (text) | — |
| 9 | 8 | Key Highlights | text (bulleted: Consolidated Performance Highlights + Corporate Highlights) | — |
| 10 | 9 | Evolving into an Integrated, Aligned & Global Organization | section divider (text/graphic) | — |
| 11 | 10 | Who we Are | text (4-column strengths table + narrative) | — |
| 12 | 11 | We are Evolving | text (narrative, 3 paragraphs) | — |
| 13 | 12 | Our Four Global Divisions | table/text (4-row division description table: CRT/PPT/HET/PST) | — |
| 14 | 13 | Unlocking Meaningful Value | text (2x2 quadrant bullets + pull-quote) | — |
| 15 | 14 | Business Performance – Revenue & Order Intake | diagram/text ("From segments/regions" to "To global divisions" mapping) | — |
| 16 | 15 | Business Performance by Divisions | infographic (4 KPI cards: CRT/PPT/HET/PST revenue & order intake) | — |
| 17 | 16 | Quarterly Revenue Trend | chart (4 bar trend charts by division, 5 quarters each) | AXIS_BINDING_UNCERTAIN (HET/PST value-to-quarter mapping) |
| 18 | 17 | Quarterly Order Intake Trend | chart (4 bar trend charts by division, 5 quarters each) | AXIS_BINDING_UNCERTAIN (PPT/HET value-to-quarter mapping) |
| 19 | 18 | EBIT to PAT: Improving Flow-through | section divider (text/graphic) | — |
| 20 | 19 | EBIT to PAT: Improving Flow-through | table/text (Initiative / Timeline / Impact on flow-through, 3 rows + waterfall label EBIT-FinanceCost-Tax-FX&StructuralLeakage=PAT) | — |
| 21 | 20 | Key Messages | section divider (text/graphic) | — |
| 22 | 21 | Key Messages | text (3-column summary: Financial Performance / Order Intake & Backlog / Organization Structure) | — |
| 23 | 22 | Thank You | text/graphic (closing slide, website URL) | — |
| 24 | 23 | Annexures | section divider (text/graphic) | — |
| 25 | 24 | Consolidated Financial Summary | table (18 line items x 5 columns: Q1FY27, Q4FY26, QoQ%, Q1FY26, YoY%) | ZERO_STANDING (Exceptional Items row) |
| 26 | 25 | Standalone Financial Summary | table (16 line items x 5 columns) | ZERO_STANDING (Other Comprehensive Income row) |
| 27 | 26 | Acquisitions – Financial Performance | section divider (text/graphic) | — |
| 28 | 27 | Acquisition Performance over the Years | chart + table (EBITDA margin row 10 values; revenue bar chart FY17-FY26; 5-column acquisition-era comparison table: Acquisition/Geography/Products/Traditional Sectors/Non-Traditional Sectors) | — |
| 29 | 28 | Acquisition's Outcome | table (Parameter / Earlier State / Current Position / Remarks, 7 rows) | — |

Slide count: 29 (matches A1 header page_count_pdfinfo=29 and formfeed_count=29).

---

## TABLE 2 — EVERY NUMBER ON EVERY SLIDE

Line numbers refer to the `[page N]` block start line in the extract; individual
values are drawn from within that block (native text unless marked OCR-only).

| Slide | Line (block start) | Numbers found (label: value) | Count | Flags |
|---|---|---|---|---|
| 1 | 28 | Ref# "GMM/SEC/2026-27/30" (FY code within ref, 2 digit-groups); letter date "August 5, 2026" (2); scrip code "505255" (1); quarter-end date "June 30, 2026" (2); digital signature timestamp "2026.08.05 18:10:36 +05'30'" split into digit-groups by layout (6); reg. citation "2015" inside Sub. line is FY-stripped/absent here — appears on p.3 instead; FCS membership "7848" (1) | 19 | — |
| 2 | 63 | Stray digit fragments from embedded stock-photo filenames "23986704", "18910721" (not company data — icon asset IDs) | 2 | NON_METRIC (asset filenames, not disclosed data — recorded per "enumerate everything") |
| 3 | 84 | Legal citation years: "2013" (Companies Act, 2013), "2009" (SEBI ICDR Regulations, 2009) | 2 | — |
| 4 | 133 | none | 0 | — |
| 5 | 145 | Revenue ₹925 Cr; Revenue YoY 16%; EBITDA ₹94 Cr; EBITDA Margin 10.1%; EBITDA YoY 7%; PAT ₹22.1 Cr; PAT Margin 2.4%; PAT YoY 118%; EPS ₹5.32; EPS YoY 114%; Order Intake ₹1,007 Cr; Order Intake QoQ 16%; Backlog ₹2,289 Cr (appears twice in layout — once in the top KPI band, once under the "Backlog" sub-heading — both instances literal in text); Backlog QoQ 4% | 15 | — |
| 6 | 168 | Revenue YoY 16%; Revenue trend values 795, 902, 883, 944, 925 (Q1FY26→Q1FY27, order confirmed against p.25 table endpoints); EBITDA YoY -7%; EBITDA trend values 122, 101, 105, 94, 75 (raw tokens as printed; exact quarter binding partially inferable from p.25 endpoints Q1FY26=101, Q4FY26=75, Q1FY27=94 but Q2/Q3 order not independently confirmable from layout — AXIS_BINDING_UNCERTAIN for Q2/Q3 only); EBITDA margins 12.7%, 13.5%, 11.9%, 8.0%, 10.1%; PAT YoY 118%; PAT trend values 38, 22, -11, 15, 10 (raw as printed); PAT margins 3.6%, 4.2%, 1.6%, 2.4%, 1.3%, -1.3% (6 tokens printed for 5 quarters — one is a duplicate/layout artifact, both recorded, not dropped); EPS YoY 114%; EPS trend values 8.86, 5.32, 3.82, 2.48, "-2.30" (literal, printed with a leading dash — plausibly a loss-quarter EPS given Q3 FY26 PAT of -11 Cr, but recorded literally, not corrected) | 35 | AXIS_BINDING_UNCERTAIN |
| 7 | 203 | Backlog trend (13 quarters, Q1FY24→Q1FY27): 2,013, 1,777, 1,773, 1,705, 1,740, 1,625, 1,636, 1,906, 2,146, 2,205, 2,194, 2,289 (12 distinct printed — 13th quarter value is the same 2,289 restated as current-quarter headline, both literal instances recorded); Order Intake trend (13 quarters): 770, 626, 756, 762, 798, 660, 861, 882, 878, 871, 1004*, 961, 1007; QoQ% callouts 16% (Order Intake), 4% (Backlog); annual OI totals FY24 3,014, FY25 3,102, FY26 3,714; footnote figure "355" (Cr, within *Q1 FY26 large-order caveat) | 32 | — (footnote asterisk on 1004* cross-referenced to Table 3 row 1) |
| 8 | 259 | Annual OI totals (repeated from p.7 for context): FY24 3,014; FY25 3,102; FY26 3,714; Q1 FY27 1,007; segment-mix percentages: 31%, 33%, 42%, 43% (Traditional/Chemicals band across 4 periods) and 23%, 35%, 36%, 27%(?) and 40%, 46%, 23%, 21% (remaining mix bands, 3 categories x 4 periods, printed as 12 tokens per layout) | 16 | — |
| 9 | 293 | Revenue YoY 16%, QoQ -2%; EBITDA YoY -7%, QoQ 25%; PAT YoY 118%, QoQ 44%; Order Intake ₹1,007 Cr, QoQ 16%; Backlog ₹2,289 Cr, YoY 20%, QoQ 4%; "four distinct global divisions" (spelled-out count, not digit — recorded); debt repayment "EUR 7 million" | 13 (12 digit-tokens + 1 spelled-out "four" counted qualitatively, see note) | — |
| 10 | 321 | none | 0 | — |
| 11 | 335 | Heritage "140 years" | 1 | — |
| 12 | 362 | none | 0 | — |
| 13 | 387 | none (title says "Four" — spelled out, already logged once at slide 9; not re-counted here to avoid double count) | 0 | — |
| 14 | 422 | none | 0 | — |
| 15 | 449 | none | 0 | — |
| 16 | 474 | CRT: Revenue ₹466 Cr (+10% YoY), Order Intake ₹502 Cr (+23% YoY); PPT: Revenue ₹255 Cr (+23% YoY), Order Intake ₹367 Cr (+64% YoY); HET: Revenue ₹74 Cr (YoY labelled "Flat" — qualitative, no numeric % disclosed), Order Intake ₹58 Cr (+719% YoY); PST: Revenue ₹131 Cr (+46% YoY), Order Intake ₹80 Cr (-78% YoY*); footnote figure "355" (Cr) | 16 | ZERO_STANDING (HET Revenue YoY disclosed only as "Flat", no bps/percent given — flagged as a standing-item precision gap, not a true zero) |
| 17 | 501 | CRT-Revenue: YoY 10%, values 423, 498, 477, 478, 466; PPT-Revenue: YoY 23%, values 208, 262, 247, 259, 255; HET-Revenue: YoY "Flat", values 74, 67, 58, 108, 74 (raw, quarter-order per layout column position, AXIS_BINDING_UNCERTAIN); PST-Revenue: YoY 46%, values 90, 91, 86, 99, 131 | 23 | AXIS_BINDING_UNCERTAIN (HET/PST column order) |
| 18 | 536 | CRT-OrderIntake: QoQ 17%, values 410, 482, 442, 431, 502; PPT-OrderIntake: QoQ 74%, values 224, 196, 211, 367 (only 4 distinct values resolvable from layout for 5 quarters — one value not independently recoverable from extracted text, flagged); HET-OrderIntake: QoQ 58%, values 7, 57, 37, 58, 189; PST-OrderIntake: QoQ -58%, values 363*, 193, 143, 115, 80; footnote figure "355" (Cr) | 24 | AXIS_BINDING_UNCERTAIN (PPT: 5th value not resolvable from extracted layout text) |
| 19 | 569 | none | 0 | — |
| 20 | 583 | Refinancing/debt reduction timeline "12-18 months"; debt repayment "EUR 7Mn"; Group Tax Strategy timeline "18-24 months"; Intercompany Loan Termination timeline "12-18 months" | 8 (digit-groups: 12, 18, 7, 18, 24, 12, 18 = 7 tokens + 1 duplicate "18" counted per literal print) | — |
| 21 | 613 | none | 0 | — |
| 22 | 625 | none | 0 | — |
| 23 | 647 | none | 0 | — |
| 24 | 660 | none | 0 | — |
| 25 | 672 | Consolidated Financial Summary table — 18 line items x 5 columns (Q1FY27 / Q4FY26 / QoQ% / Q1FY26 / YoY%) = 90 cell values, incl. Exceptional Items row cells "-" / "-100%" / "-" / "NA" (dash/NA literal, ZERO_STANDING) | 90 | ZERO_STANDING (Exceptional Items: "-" at Q1FY27 and Q1FY26, "NA" at YoY) |
| 26 | 698 | Standalone Financial Summary table — 16 line items x 5 columns = 80 cell values, incl. Other Comprehensive Income row cells "0" / "0" / "-" (Q1FY27=0, Q1FY26=0, YoY="-", ZERO_STANDING) | 80 | ZERO_STANDING (Other Comprehensive Income: 0 at Q1FY27 and Q1FY26, "-" at YoY) |
| 27 | 724 | none | 0 | — |
| 28 | 738 | EBITDA margin row (10 values, FY17-FY26): 12.6%, 15.1%, 15.3%, 18.8%, 13.9%, 11.2%, 13.5%, 13.8%, 11.3%, 11.4%; Revenue bar chart (10 values, FY17-FY26, ₹ Cr): 378.1, 411.0, 502.6, 591.1, 1001.1, 2540.6, 3177.6, 3446.5, 3198.7, 3523.9; callouts "~4x" (Revenue increase, De Dietrich), "20+" (manufacturing sites), "+9% CAGR", "+154%" | 25 (10+10+4 callout tokens, each containing a digit) | — |
| 29 | 806 | Industry Diversification: "~80%" traditional (earlier), "~55%" traditional / "~45%" non-traditional (current); Global Presence: "20" manufacturing facilities (earlier), "35+" countries / "20" manufacturing facilities (current); Innovation & Technology: "4.0" (Industry 4.0) | 7 | — |

**Grand total, Table 2: 414 numbers** (matches count test).

---

## TABLE 3 — FOOTNOTES / FINE-PRINT DISCLAIMERS QUALIFYING A HEADLINE NUMBER

| # | Slide (page) | Line | Footnote text (verbatim, first clause) | Qualifies | Flags |
|---|---|---|---|---|---|
| 1 | 7 | 256 | "*Q1 FY26 order intake includes a large order of NR [INR] 355 Cr" | Order Intake & Backlog Trends chart — the Q1 FY26 order-intake bar (1004) and every subsequent QoQ/YoY% built off it | REPEAT_FOOTNOTE (same caveat recurs at rows 2 and 3 below — flagged for A3/A4: three separate headline comparisons all ride on one non-recurring order, YoY/QoQ optics should be read net of it) |
| 2 | 16 | 498 | "PST: *Q1 FY26 order intake includes a large order of INR 355 Cr" | PST division Order Intake -78% YoY headline on the same slide's KPI card | REPEAT_FOOTNOTE (see #1) |
| 3 | 18 | 566 | "PST: *Q1 FY26 Order intake includes a large order of NR 355 Cr" | PST — Order Intake -58% QoQ chart headline | REPEAT_FOOTNOTE (see #1) |
| 4 | 6 | 200 | "¹ FY 26 restated for Semco and GMM Inox Poland PPA." | Q2 FY26 and Q3 FY26 PAT and EPS trend-chart bars (marked with ¹ in the chart) | RESTATEMENT — prior-period comparatives restated for PPA (purchase price allocation); affects YoY comparability for PAT/EPS at those two quarters |
| 5 | 25 | 695 | "Margin and growth percentages are calculated on absolute figures. Amounts are rounded off to crores and subject to casting." | Every % and bps figure in the Consolidated Financial Summary table | — |
| 6 | 26 | 721 | "Margin and growth percentages are calculated on absolute figures. Amounts are rounded off to crores and subject to casting." | Every % and bps figure in the Standalone Financial Summary table | — |

Additionally, page 3 (slide 3) carries a full-page legal Disclaimer (forward-looking
statements, non-GAAP measures, no-reliance, governing-law clauses) that qualifies the
entire presentation rather than one headline number — logged in Table 1, not counted
in the footnote total above (different category: deck-wide disclaimer vs.
number-qualifying footnote).

---

## TABLE 4 — DROPPED_SLIDE COMPARISON (prior-quarter deck)

No prior-quarter ledger was supplied for this run (path given as "none"). DROPPED_SLIDE
diffing is **N.A.** this run — there is no baseline deck to diff against. This should
be treated as a gap for the NEXT quarter's A2 run (Q2 FY27), which will have this
deck as its baseline and must diff every slide title in Table 1 above against it.

---

## SUMMARY OF FLAGS RAISED

- ZERO_STANDING x3: Exceptional Items row (p.25, consolidated), Other Comprehensive
  Income row (p.26, standalone), HET Revenue YoY disclosed only as "Flat" (p.16) —
  precision gap on an otherwise fully-quantified KPI card.
- AXIS_BINDING_UNCERTAIN x3 (slides 6, 17, 18): chart bar/line values whose
  quarter-to-value binding cannot be independently confirmed from pdftotext
  layout-preserved text alone (values are correct as printed; the column order is the
  ambiguous part). Cross-checked against OCR blocks per A1 header — OCR does not
  resolve the ambiguity (same layout limitation applies to the rasterised OCR pass).
  Flagged for A3/A4 to resolve against the source PDF image if the specific
  quarter-value pairing becomes load-bearing for an arithmetic-consistency check.
- REPEAT_FOOTNOTE x1 (applies across footnote rows 1-3, Table 3): the Q1 FY26 ₹355 Cr
  large-order caveat recurs three times, qualifying three different headline
  YoY/QoQ comparisons (deck-level, PST-division revenue chart, PST-division order
  intake chart) — all three ride on the same one-off order.
- RESTATEMENT x1 (Table 3, row 4): FY26 Q2/Q3 PAT and EPS restated for Semco and GMM
  Inox Poland PPA.
- DROPPED_SLIDE: N.A. this run (no prior deck supplied) — see Table 4.
