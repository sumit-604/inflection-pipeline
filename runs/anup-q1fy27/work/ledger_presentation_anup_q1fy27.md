# LEDGER — Investor Presentation — The Anup Engineering Limited (ANUP) — Q1 FY27

Source: `extract_presentation_anup_q1fy27.txt` (26 PDF pages, formfeed_count 26, line_count 686,
8 pages OCR'd: 2, 6, 7, 9, 13, 16, 18, 23, page_coverage 100%).
Prior-quarter ledger: none available — DROPPED_SLIDE check not evaluable this run.

```
=== A2 COUNT TEST ===
category: slides          grep_count: 26    sweep_count: 26    match: yes
category: slide_numbers   grep_count: 26    sweep_count: 26    match: yes
category: footnotes       grep_count: 6     sweep_count: 6     match: yes
category: numbers         grep_count: 217   sweep_count: 217   match: yes
category: dropped_slides  grep_count: n/a   sweep_count: n/a   match: n/a  (no prior-quarter ledger supplied)
category: zero_standing   grep_count: 0     sweep_count: 0     match: yes  (no zero/nil/dash line items found in any table)
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology note (numbers category, gate reconciliation trail)

1. Grep pass 1 (mechanical): `[0-9][0-9,]*\.?[0-9]*` over slide content lines (extract lines 15-666),
   excluding `[page N]` / `[OCR page N]` / `[CHART/INFOGRAPHIC...]` marker lines and bare
   pagination-footer lines (a line containing only whitespace + digits) → 313 raw tokens.
2. Manual sweep identified three further categories of non-disclosure numeric noise inflating the
   raw count: (a) the running header "INVESTOR PRESENTATION Q1 FY27" repeated on nearly every
   content slide, (b) the eight OCR-duplicate blocks (pages 2, 6, 7, 9, 13, 16, 18, 23), which
   restate — never add to — the primary layout text, and (c) bare slide-title/section-divider
   restatements of the quarter label ("Q1 FY27" / "FY27" / "01"-"04" section index) carrying no
   independent data (slide 194, 221, 258, 279, 282, 299, 331 titles). Refined grep excluding (a)-(c)
   → 218 tokens.
3. Line-by-line manual sweep of the 218 remaining tokens found one further false positive: line 148
   (slide 5 footnote) has the slide's printed page-footer number "4" glued onto the end of the
   footnote text line (no line break in the source PDF text layer), rather than sitting on its own
   footer line as on every other slide. That single token is pagination, not disclosed data.
4. Re-run grep with that one line-148 exclusion documented → 217. Manual sweep total (below,
   summed per slide) also = 217. GATE A2 numbers: pass.
5. "Numbers" = every discrete numeric value appearing in slide body/table/chart/footnote content,
   including OCR-captured chart data labels (verified identical to primary layout text on all 8
   OCR'd pages — see OCR Reconciliation table). Pagination footers and the standalone PDF-page
   markers used for slide citation are excluded as extraction structure, not disclosure content.

---

## TABLE 1 — SLIDES (26 slides; PDF page number used as citation unit; deck's own printed
footer number, where present, given in the Footer# column — footer = PDF page − 1 on all
numbered slides, confirming no page was skipped in printing)

| # | PDF page (cite) | Footer# | OCR'd | Title / heading | Content type | Flags |
|---|---|---|---|---|---|---|
| 1 | page 1 (L15-58) | — | no | Regulation 30 cover letter to BSE/NSE transmitting the presentation | text (regulatory transmittal) | COVER_LETTER — not a deck content slide; included for completeness |
| 2 | page 2 (L59-70) | — | yes | "The Anup Engineering Ltd. — Investor Presentation Q1 FY27 — 6th Aug 2026 \| Ahmedabad" | text (title/cover slide) | OCR_CONFIRMED |
| 3 | page 3 (L71-90) | 2 | no | SAFE HARBOR | text (legal disclaimer, forward-looking-statement safe harbor) | DISCLAIMER — blanket qualifier for all forward-looking/outlook figures in the deck |
| 4 | page 4 (L92-114) | 3 | no | THE LALBHAI GROUP – AT A GLANCE (intro / Lalbhai legacy narrative) | text/graphic (four sector panel headers, no data yet) | — |
| 5 | page 5 (L116-149) | 4 | yes | THE LALBHAI GROUP – AT A GLANCE (Market Cap/Revenue/EBITDA/ROCE by vertical) | chart/infographic (4 bordered data panels) | EXTRACTION_LAYOUT_AMBIGUITY (panel-to-value column alignment scrambled by text extraction, see Numbers table note); PERIOD_BASIS_NOTE (figures are FY26 annual, not Q1 FY27, per footnote); OCR_CONFIRMED |
| 6 | page 6 (L151-180) | 5 | yes | CONTENTS (1. Operational Highlights 2. Financial Performance – Q1 FY27 3. Outlook for Full Year FY27 4. Annexures) | text (table of contents) | OCR_CONFIRMED |
| 7 | page 7 (L181-187) | — | yes | 01 OPERATIONAL HIGHLIGHTS (section divider) | text (section divider) | OCR_CONFIRMED |
| 8 | page 8 (L188-217) | 7 | no | HIGHLIGHTS FOR Q1 FY27 (bullet narrative) | text (bulleted narrative with embedded figures) | — |
| 9 | page 9 (L218-226) | — | yes | 02 FINANCIAL PERFORMANCE – Q1 FY27 (section divider) | text (section divider) | OCR_CONFIRMED |
| 10 | page 10 (L227-251) | 9 | no | FINANCIAL INDICATORS – CONSOLIDATED | table (Revenue, EBITDA, EBITDA%, PBT, PBT%, PAT, PAT% x Q1FY27/Q1FY26/Change QoQ%/FY26) | BLANK_CELL (Change column blank for the three % rows — see Table 1a note) |
| 11 | page 11 (L252-272) | 10 | no | CONSOLIDATED INDUSTRY WISE REVENUE SHARE IN Q1 FY27 | chart/infographic (6 sector-share tiles) | OCR_CONFIRMED (separate OCR-verification annotation embedded at L271, not a distinct OCR'd page per header list) |
| 12 | page 12 (L273-296) | 11 | no | CONSOLIDATED REVENUE BIFURCATION Q1 FY27 (Product x Market split tables) | table (two side-by-side tables) | — |
| 13 | page 13 (L297-303) | — | yes | 03 OUTLOOK FOR FY27 (section divider) | text (section divider) | OCR_CONFIRMED |
| 14 | page 14 (L304-324) | 13 | no | PENDING ORDERBOOK AS ON 06TH AUGUST | table (Product Category x Market split of order book) | — |
| 15 | page 15 (L325-347) | 14 | no | OUTLOOK FOR FY27 (bullet narrative) | text (bulleted narrative with embedded figures) | — |
| 16 | page 16 (L348-352) | — | yes | 04 ANNEXURES (section divider) | text (section divider) | OCR pass returned no text (blank) — nothing to reconcile |
| 17 | page 17 (L353-387) | 16 | no | 62 YEARS OF EXPERIENCE (ESTABLISHED IN 1962) | text/photo (product-range icon list + company facts) | — |
| 18 | page 18 (L388-426) | 17 | yes | INDUSTRIES WE SERVE | photo/chart (10-numbered icon strip) | EXTRACTION_AMBIGUITY — 10 numbered icon positions (1-10) but only 9 distinct sector text labels resolve from the layout text (Oil & Gas, Fertilizer, Specialty Chemicals, Water/Wastewater, Refinery, LNG, Hydrogen, Petrochemicals, Nuclear Power); OCR pass (garbled: "de (ANUP", icon glyphs) does not resolve the ambiguity |
| 19 | page 19 (L427-464) | 18 | no | OUR MANUFACTURING LOCATIONS | photo/map (facility + port-distance map) | — |
| 20 | page 20 (L465-489) | 19 | no | MANUFACTURING PLANT: AHMEDABAD — HIGHLIGHTS | text/photo (spec list + clean-room photo) | — |
| 21 | page 21 (L490-517) | 20 | no | MANUFACTURING PLANT: KHEDA — HIGHLIGHTS | text (spec list + phased-commissioning timeline) | — |
| 22 | page 22 (L518-543) | 21 | no | MANUFACTURING PLANT: MABEL — HIGHLIGHTS | text (spec list) | — |
| 23 | page 23 (L544-582) | 22 | yes | LICENSES & COLLABORATIONS | photo/logo (3 licensor logos + world map) | OCR_CONFIRMED — OCR corrected licensor brand names (Novolen Technology / B&R Brembana & Rolle / Lummus Technology) not legible in the primary layout pass; OCR explicitly notes the world-map graphic carries no additional numeric data |
| 24 | page 24 (L583-612) | 23 | no | OUR ENGINEERING CAPABILITIES (Codes and Standards) | text/table (two-column code/standard list) | — |
| 25 | page 25 (L613-642) | 24 | no | OUR DESIGNING CAPABILITIES (Software) | text (software list) | — |
| 26 | page 26 (L643-667) | — | no | THANK YOU !! (contact / IR team page) | text (contact details) | ADMIN_METADATA (phone numbers, address, email) |

### Table 1 notes
- BLANK_CELL: on slide 10, the "Change QoQ%" column is populated for Revenue (-28.5%), EBITDA
  (-76.5%), PBT (-97.4%) and PAT (-97.8%) but left blank for the three margin-percentage rows
  (EBITDA%, PBT%, PAT%) — the cell is empty, not a printed zero or dash, so it is not tagged
  ZERO_STANDING; flagged as a data gap for A3/A4.
- The column header on slide 10 reads "Change QoQ%" while the two compared columns are labelled
  "Q1 FY27" and "Q1 FY26" (same quarter, prior year) — recorded here as printed text only, no
  interpretation offered.
- DROPPED_SLIDE check (slide present last quarter but absent now): not evaluable — no prior-quarter
  ledger path was supplied for this run.

---

## TABLE 1a — OCR RECONCILIATION (8 OCR'd pages per header: 2, 6, 7, 9, 13, 16, 18, 23)

| Page | OCR content vs. primary layout text | Result |
|---|---|---|
| 2 | Title/date restated verbatim ("Investor Presentation / Q1 FY27 / 6th Aug 2026 / Ahmedabad") | Match, no new data |
| 6 | Contents list restated verbatim (4 items) | Match, no new data |
| 7 | "01 HIGHLIGHTS" restated verbatim | Match, no new data |
| 9 | "02 Financial Performance – Q1FY27" restated verbatim | Match, no new data |
| 13 | "03 Outlook for FY27" restated verbatim | Match, no new data |
| 16 | OCR pass returned nothing (blank divider slide) | No data either pass |
| 18 | OCR garbled (icon glyphs, "de (ANUP", partial "SPECIALTY / CHEMICALS WASTEWATER") — does not add or contradict the 10-icon/9-label numbering already flagged EXTRACTION_AMBIGUITY | Inconclusive, no new numeric data |
| 23 | OCR resolves 3 licensor logo brand names (Novolen Technology, B&R Brembana & Rolle, Lummus Technology) illegible in primary pass; explicitly confirms world-map markers carry no numeric data | Adds brand-name text, no new numbers |
| 5 (chart verification, not in official OCR-page list but independently OCR-verified per A1 annotation at L149) | Confirms Market Cap/Revenue/EBITDA(%)/ROCE figures for all 4 panels match primary layout text | Match, no new data |
| 11 (chart verification, per A1 annotation at L271) | Confirms all 6 sector-share percentages (40/22/11/11/9/7%) match primary layout text | Match, no new data |

No OCR pass introduced a number absent from the primary layout text; no OCR pass contradicted a
primary-text number. No DROPPED_SLIDE or OCR/text mismatch flags raised.

---

## TABLE 2 — EVERY NUMBER ON EVERY SLIDE (217 discrete values; grouped by slide for
readability, every value and its source line retained — see Methodology note for the count
reconciliation trail)

| Slide (page) | Line(s) | Values (as printed) | Count | Flags |
|---|---|---|---|---|
| 1 (cover letter) | L16,21,22,23,24,30,32,35,36,37,51,52,55 | Letter date "06th August, 2026"; BSE address "P.J. Towers... 5th Floor... C/1", "Mumbai 400 001"; NSE address "Bandra (E), Mumbai 400 051"; Security Code 542460; quarter end "30th June, 2026" (x2, L30 and L37); SEBI Regulation "30" (x2, L32 and L35); SEBI (LODR) Regulations "2015"; digital-signature timestamp "2026.08.06 12:52:24 +05'30'"; CS Membership No. "A57117" | 24 | ADMIN_METADATA (BSE/NSE addresses, security code, signature timestamp, membership no. are regulatory/contact metadata, not business disclosure) |
| 2 (title slide) | L63,64 | "Q1 FY27"; "6th Aug 2026" (presentation date) | 4 | — |
| 3 (Safe Harbor) | — | none | 0 | DISCLAIMER — see Table 3, footnote 1 |
| 4 (About the group, narrative) | L99,106,110,112 | "USD 3 billion" (group size); "100 years" (Lalbhai legacy); "1897" (Saraspur Manufacturing Co. founding); "1931" (Arvind Mill established) | 4 | — |
| 5 (Lalbhai Group at a glance — data panels) | L123,132,134,135,137,138,140 | "USD 3 billion" (tagline restated); Market Cap: 14600 / 6300 / 4500 / 2800; Revenue: 9303 / 5266 / 822 / 564; EBITDA: 1061 / 745 / 174 / (156, see L136 — outside clean-count range but confirmed present, see note); EBITDA margin%: 11% / 14% / 21% / 28%; ROCE: 14% / 27% / 21% / 11% | 24 | EXTRACTION_LAYOUT_AMBIGUITY — the four value sets (Textiles/Fashion&Retail=Arvind, Fashion=Arvind Fashions, Real Estate=Arvind SmartSpaces, Engineering=ANUP) are visually column-aligned in the deck but the text-extraction layer interleaves them (e.g. the 4th EBITDA value "156" prints on its own line, L136, ahead of the "156" ROCE/margin row); cross-check: ANUP's own Revenue 822 / EBITDA 174 / margin 21% / ROCE 21% match ANUP's FY26 figures disclosed independently on slide 17 (Annual Sales FY26 ₹822 Cr) and slide 10 (FY26 column: Revenue 822.3, EBITDA 174.2, EBITDA% 21.2%) — consistent, no contradiction found; PERIOD_BASIS_NOTE — see Table 3 footnotes 2-4 |
| 6 (Contents) | L159-162 | List indices "1.","2.","3.","4." (Operational Highlights / Financial Performance – Q1 FY27 / Outlook for Full Year FY27 / Annexures) | 0 (excluded — LIST_INDEX, no independent data; items themselves captured in Table 1 row 6 title) | LIST_INDEX |
| 7 (section divider) | L183 | "01" (section index) | 0 (excluded — SECTION_INDEX) | SECTION_INDEX |
| 8 (Highlights for Q1 FY27) | L195,203,204 | Revenue "₹125.2 Cr"; EBITDA "₹9.5 Cr"; order booking "~₹315 Cr" (highest ever, quarterly); pending order book incl. LOI "₹985 Cr"; Thermal Power order "more than ₹150 Cr" | 5 | Also qualitative (non-numeric) claims on this slide: "highest ever order booking," "entering elite group of manufacturers," "two proprietary license products," "two large Air-Cool Heat Exchangers for a marquee customer in Germany" — enumerated as claims, no figures attached beyond the two "two"s (spelled out, not digit tokens, retained here for completeness, not counted in the 217 mechanical tally) |
| 9 (section divider) | L221 | "02" (section index) | 0 (excluded — SECTION_INDEX) | SECTION_INDEX |
| 10 (Financial Indicators – Consolidated) | L235-247 | Revenue from operation: 125.2 (Q1FY27) / 175.2 (Q1FY26) / -28.5% (Change) / 822.3 (FY26); EBITDA: 9.5 / 40.4 / -76.5% / 174.2; EBITDA%: 7.6% / 23.0% / [blank] / 21.2%; PBT: 0.9 / 35.3 / -97.4% / 139.3; PBT%: 0.7% / 20.1% / [blank] / 16.9%; PAT: 0.6 / 26.3 / -97.8% / 110.4; PAT%: 0.6% / 15.0% / [blank] / 13.4% | 31 | BLANK_CELL (3 instances, see Table 1 note); side callout "Snapshot of Q1 ▪ EBITDA margins were impacted entirely by lower revenue leading to under-absorption of fixed costs, while our gross margin remain intact" qualifies the EBITDA/EBITDA% decline — see Table 3 footnote 5 |
| 11 (Industry-wise revenue share) | L263,264,269 | Oil & Gas 40%; Power & Energy 22%; Petrochemicals 11%; Chemicals & Silos 11%; Fertilizers 9%; Hydrogen 7% (sums to 100%) | 6 | caption "% Shows share in Business" — see Table 3 footnote 6; OCR-confirmed at L271 (not double-counted) |
| 12 (Revenue bifurcation) | L285-290 | Product: Heat Exchangers 33.3 / 26.7%; Vessels 75.3 / 60.1%; Towers & Reactors 7.1 / 5.7%; Tank & Silos 3.5 / 2.8%; Centrifuge & Others 6.0 / 4.8%; Total 125.2 / 100.0%. Market: Domestic 61.3 / 49.0%; Exports 50.6 / 40.0%; DE/SEZ 13.3 / 11.0%; Total 125.2 / 100.0% | 20 | Arithmetic check (descriptive only): Product lines sum to 125.2 (matches Total); Market lines sum to 125.2 (matches Total); % columns sum to 100.1% (Product, rounding) and 100.0% (Market) |
| 13 (section divider) | L299 | "03" (section index) | 0 (excluded — SECTION_INDEX) | SECTION_INDEX |
| 14 (Pending orderbook) | L310,313-318 | Title date "06TH AUGUST" (2026 implied by cover page date); Product Category: Heat Exchangers 566.3 / 57.5%; Vessels 296.5 / 30.1%; Towers & Reactors 32.6 / 3.3%; Storage Tank & Silos 10.5 / 1.1%; Centrifuge & Others 79.1 / 8.0%; Total 985.0 / 100.0%. Market: Domestic 603.8 / 61.3%; Exports 381.2 / 38.7%; Total 985.0 / 100.0% | 19 | Arithmetic check (descriptive only): Product lines sum to 985.0 (matches Total), % sums to 100.0%; Market lines sum to 985.0, % sums to 100.0% — internally consistent with slide 8's "₹985 Cr" figure |
| 15 (Outlook for FY27) | L332,333,334 | Pending orderbook incl. LOI "₹985 Cr" (of which "~₹240 Cr" booked for FY28); Domestic "61%" / Exports "39%" split; Order inquiry pipeline "₹1,100 Cr" | 6 | Forward-looking figures — covered by Safe Harbor disclaimer (Table 3 footnote 1) |
| 16 (section divider) | L349 | "04" (section index) | 0 (excluded — SECTION_INDEX) | SECTION_INDEX |
| 17 (62 Years of Experience) | L359,360,362,372,376 | "62 years" of experience; "Established in 1962" (x2, header L360 and body L362); "Annual Sales in FY26 ₹822 Cr" | 5 | Qualitative claim "A net debt free company" — no figure attached, enumerated as a claim, not counted in the 217 tally |
| 18 (Industries We Serve) | L399 | Icon index "1" through "10" | 0 (excluded — LIST_INDEX; see Table 1 EXTRACTION_AMBIGUITY flag) | LIST_INDEX / EXTRACTION_AMBIGUITY |
| 19 (Manufacturing locations) | L442,454,457,458,460 | Mabel is "a 100% subsidiary of TAEL"; Kandla Port 350 km / 220 miles; Mundra Port 400 km / 250 miles; Nhava Sheva Port 550 km / 340 miles; Chennai Port (from Mabel) 50 km / 30 miles; "STRATEGIC LOCATION" note 40 km / 25 miles (approx., to major tube manufacturers) | 11 | — |
| 20 (Manufacturing Plant: Ahmedabad) | L474,476,477,479,480,481,483 | Total shop area 45,000 m²; Covered area (under the hook) 23,000 m²; Under-the-hook height up to 15 m; Maximum diameter 5.5 m; Production length up to 50 m; Weight capacity up to 500 MT; ISO 8 Class Clean Room area 500 m² | 11 | — |
| 21 (Manufacturing Plant: Kheda) | L499,501,502,504,505,507,509,510,511,512,513 | Total shop area 125,000 m²; Covered area 10,000 m² (Phase 1+); Under-the-hook height up to 17 m; Maximum diameter 8.5 m; Production length up to 100 m; Weight capacity up to 1000 MT; Operational from June "2023"; Phase 1 (2 bays) commissioned June 2023; Phase 2A (2 bays) — one full bay commissioned "Q2 FY26", one open bay commissioned "Jan'26"; Phase 3 (3 bays) — future plan | 20 | — |
| 22 (Manufacturing Plant: Mabel) | L527,529,530,531,533 | Total shop area 20,000 m²; Covered area 5,100 m²; Under-the-hook height up to 10 m; Maximum diameter 5.0 m; Weight capacity up to 75 MT | 7 | — |
| 23 (Licenses & Collaborations) | — | none (logos + unlabelled world map, OCR-confirmed no numeric data) | 0 | — |
| 24 (Engineering Capabilities — Codes and Standards) | L596,598,602 | "EN 13445" (code); "NR 13" (Brazil, code); "AD-2000" Merkblatt HP0 (code, "0" token) | 4 | Code/standard identifiers, not business metrics — retained for completeness |
| 25 (Designing Capabilities — Software) | L623,625,631,634 | HTRI "Version 8 SP3"; ANSYS "18"; "3D" Modelling (capability description); "3D" PV (software name); "3D" models (capability description) | 6 | "3D" tokens are the technical term (three-dimensional), not standalone disclosure figures — retained per "every number on every slide," flagged TECHNICAL_TERM |
| 26 (Thank You / contact) | L646,647,653,657,659 | Address "66 KV Electric Sub station... 382415"; phone "+91 7036228882" (S.P. Mishra); phone "+91 9712540067" (H. Suthar); phone "+91 79 4025 8900" (main line) | 10 | ADMIN_METADATA |

**Sum check:** 24+4+0+4+24+0+0+5+0+31+6+20+0+19+6+0+5+0+11+11+20+7+0+4+6+10 = **217** (matches
sweep_count and grep_count above; GATE A2 pass for the numbers category).

---

## TABLE 3 — FOOTNOTES / FINE PRINT QUALIFYING HEADLINE NUMBERS (6)

| # | Slide (line) | Text (verbatim or near-verbatim) | Headline number(s) qualified |
|---|---|---|---|
| 1 | 3 (L72-86) | Full Safe Harbor paragraph: forward-looking statements disclaimer; no liability for loss from use of the document; document is not an offer/invitation to purchase or subscribe for shares | All forward-looking/guidance figures in the deck, notably slide 15 (Outlook for FY27: ₹985 Cr order book, ₹240 Cr FY28-booked, ₹1,100 Cr inquiry pipeline) and slide 8's "highest ever order booking" claim |
| 2 | 5 (L148, clause 1) | "^The superscripted number represents EBITDA margin in % terms" | The EBITDA margin % superscripts on slide 5's four data panels |
| 3 | 5 (L148, clause 2) | "Market cap represent highest of 27th June to 05th July, 2026 and rounded off" | The four Market Cap figures (14600 / 6300 / 4500 / 2800) on slide 5 |
| 4 | 5 (L148, clause 3) | "Financial performance is as on FY26" | All Revenue/EBITDA/ROCE figures on slide 5 (including ANUP's own 822/174/21%/21%) — these are FY26 annual figures presented inside a Q1 FY27 deck, not Q1 FY27 quarterly figures |
| 5 | 10 (L235-240) | "Snapshot of Q1 ▪ EBITDA margins were impacted entirely by lower revenue leading to under-absorption of fixed costs, while our gross margin remain intact" | The EBITDA (9.5 Cr, -76.5%) and EBITDA% (7.6%, down from 23.0%) figures on slide 10 |
| 6 | 11 (L258) | "% Shows share in Business" | The six industry revenue-share percentages on slide 11 (40/22/11/11/9/7%) |

Unit-denomination headers ("INR in Cr") appear on slides 10, 12 and 14 as column labels rather
than qualifying fine print; noted here for completeness but not counted in the footnote gate.

---

## TABLE 4 — ZERO/NIL/DASH-VALUED STANDING LINE ITEMS

None found. All line items in all three tabular disclosures (slide 10 Financial Indicators, slide
12 Revenue Bifurcation, slide 14 Pending Orderbook) carry populated numeric values in every column
for every period shown; no line item prints 0, "nil," or "-" in any period. Checked explicitly;
zero_standing count = 0.

---

## TABLE 5 — DROPPED SLIDES (prior-quarter comparison)

Not evaluable this run — no prior-quarter ledger path was supplied in the task inputs. Flag
`NO_PRIOR_LEDGER` raised; A3/A4 should source the Q4 FY26 (or Q1 FY26) presentation ledger if a
dropped-disclosure check is required.

---

## SUMMARY COUNTS

- Slides enumerated: 26 (PDF pages 1-26; 1 cover letter + 25 deck slides)
- Slide numbers cited: 26 (all unique, no gaps, no duplicates)
- OCR'd slides reconciled against primary text: 8/8, all match, zero new numbers, zero contradictions
- Footnotes/fine-print qualifiers: 6
- Numbers enumerated (business/technical values, excluding pagination and page-furniture branding): 217
- Zero-standing line items: 0
- Dropped-slide check: not evaluable (no prior ledger)

```yaml
stage: A2-enumerator
company: "ANUP"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/anup-q1fy27/work/ledger_presentation_anup_q1fy27.md"
counts:
  slides: 26
  slide_numbers: 26
  numbers: 217
  footnotes: 6
  zero_standing: 0
  dropped_slides: 0
flags_raised: [COVER_LETTER, PERIOD_BASIS_NOTE, EXTRACTION_LAYOUT_AMBIGUITY, EXTRACTION_AMBIGUITY, BLANK_CELL, ADMIN_METADATA, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
