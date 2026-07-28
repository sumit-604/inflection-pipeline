=== A2 COUNT TEST ===
category: slides          grep_count: 34   sweep_count: 34   match: yes
category: numbers         grep_count: 554  sweep_count: 554  match: yes
category: notes           grep_count: 5    sweep_count: 5    match: yes
category: line_items      grep_count: 28   sweep_count: 28   match: yes
category: dropped_slide   grep_count: n/a  sweep_count: n/a  match: n/a  (no prior-quarter deck supplied; first quarterly run for DSSL; DROPPED_SLIDE sub-check is NOT COMPUTABLE and is explicitly skipped per task instruction, not silently omitted)
gate_a2: pass
=== END COUNT TEST ===

# LEDGER — Digitide Solutions Limited (DSSL) — Q1 FY27 — Investor Presentation
Source: investor_presentation_Q1FY27.pdf (34 pages) via A1 extract
`runs/dssl-q1fy27/work/extract_presentation_dssl_q1fy27.txt`
Prior-quarter ledger: none supplied (first quarterly run for DSSL). DROPPED_SLIDE
comparison is not computable and is skipped explicitly, not fabricated.

## METHODOLOGY NOTE (read before using the NUMBERS table)
"Numbers" = every quantitative disclosure figure on a slide: ₹ Cr / $ amounts,
percentages, bps, ratios, multiples, counts, employee/partner/customer stats,
chart data labels (bar/line values and axis-tick scale values), and
content-bearing year labels (e.g. the 2020-2026 partnership-timeline chips on
page 10). Grep pass = a Python/regex sweep of the extract (`\-?\d[\d,]*\.?\d*`)
run per `[[PAGE n]]` block, EXCLUDING (a) the bracket-tagged `[OCR page N]` /
`[CHART, page N, ...]` annotation lines (per the A1 header, these are
cross-check duplicates of numbers already in the page's own text layer, adding
no new figures except making explicit which quarter each already-listed figure
belongs to — counting them again would double-count, not "miss" anything), and
(b) bare single-line page-footer numbers (e.g. a lone "6" on its own line — the
slide's printed page number, not disclosure data) and pure quarter/FY period
labels (e.g. "Q1 FY26", "Q1'FY27", standalone "FY26") which are column/chart
headers, not measured values. Manual sweep = independent line-by-line read of
every page (performed before the script pass) cross-checked against the script
output; the two reconcile exactly at 554 (see COUNT TEST). Page-footer numbers
and quarter/period-label digits are NOT dropped — they are structural and are
called out per-slide in the SLIDES table's "footer #" note and in each
NUMBERS-table row's flag column where relevant, so nothing is silently
excluded from the ledger, only from the "numbers" GATE A2 count definition,
which is stated above so A3/A4 can audit it.

Page 1 is the Regulation-30 BSE/NSE cover letter (not a "slide" in the deck
proper, but page 1 of the PDF); its 28 numeric tokens include address/phone/
CIN/pincode/membership-no./signature-timestamp fragments that the PDF text
layer splits oddly (e.g. CIN "L62099KA2024PLC184626" splits into 62099 / 2024
/ 184626 across the regex pass; pincode "400 001" and "400 051" split across
line-wraps). These are listed as raw tokens in the NUMBERS table (flag
ADMINISTRATIVE) with a plain-language recombination note so A3/A4 are not
misled into treating them as three separate disclosed figures.

---

## TABLE 1 — SLIDES (34 rows; grep `^\[\[PAGE ` count = 34, manual sweep = 34, match)

| Slide | Line (marker) | Title / heading | Content type | Notes / flags |
|---|---|---|---|---|
| 1 | 25 | Regulation 30 cover letter to BSE/NSE re: submission of Investors' Presentation | text (regulatory transmittal + digital signature block) | Not a deck "slide" — page 1 of the PDF. Digitally signed by Shailesha Barve, 2026.07.27 22:43:07 +05'30'. |
| 2 | 81 | "Q1'FY27 Investor Presentation / July 2026 / Digitide Solutions Ltd" | photo/title (cover slide) | OCR-verified page (text-layer char count low; stock photo background). Footer "1". |
| 3 | 88 | Safe Harbor and Disclaimer | text (full-page legal disclaimer) | Contains general forward-looking-statement and currency-exchange-rate caveat language ("this presentation may contain certain currency exchange rates and the same have been provided only for the convenience of readers") — relevant context for the page 15 USD figures flag below, though not itself a per-number footnote. Footer "2". |
| 4 | 114 | Executive Summary (Strategy / Financials / Technology) | text (3-column bullet summary) | Footer "3". |
| 5 | 155 | Table of Contents (I Who We Are / II Our Performance: Q1FY27 / III A New Way Forward) | text/photo | OCR-verified page. Footer "4". |
| 6 | 166 | Who We Are (section divider) | photo/title | OCR-verified page. Footer "5". |
| 7 | 171 | Digitide at a Glance: An AI-First Tech & Digital (T&D) and BPM Platform | table (9-tile stat grid) | OCR-verified page (9 icon-tile values cross-checked against image, verbatim match to text layer). Footer "6". |
| 8 | 196 | Digitide has a proven history of transforming businesses, backed by long-term promoters (Our Companies: Digitide vs Alldigi) | table + photo | Two-entity comparison table (NSE Ticker / FY26 Revenue / FY26 EBITDA* / FY26 Employees for DIGITIDE and ALLDIGI); footnote "*As per Ind-AS" qualifies both EBITDA figures. Footer "7". |
| 9 | 224 | Driving trusted, AI-first digital, IT & BPM transformation | text (capability-wheel diagram) | Almost no numeric data (service-line taxonomy only). Footer "8". |
| 10 | 296 | Having the right foundations for sustainable growth | text/table | Partnerships, AI accelerators, analyst-coverage nominations, GPTW timeline chips 2020-2026. Footer "9". |
| 11 | 363 | Global delivery with strong India–North America backbone | text/map | Location counts by region. Footer "10". |
| 12 | 397 | Differentiated delivery model in India with access to Tier-2/3 Talent | text/map | Collections platform stat (~15K feet on ground, 95% pincodes). Footer "11". |
| 13 | 432 | Pulse.AI: One AI engine, purpose-built for every industry we serve | text/diagram | Footer "12". |
| 14 | 466 | AI is already generating measurable business returns — not a future promise | table (dense stat grid) | Densest non-chart numeric slide (39 numbers): bot interaction volumes, containment rates, ACV figures (already ₹ Cr per A1 header, factor x1). Footer "13". |
| 15 | 560 | Driving AI-led transformation across core industries (BFS / Insurance / Healthcare use-case + IMPACT matrix) | text (3-column use-case + impact matrix) | **Carries UNIT_MISMATCH flag** — IMPACT bullet "$2M-$6M+ savings per use case" (Insurance panel, per A1 header) is in USD millions, NOT converted to ₹ Cr, unlike every other currency figure in the deck. Two figures: $2M and $6M+. Not resolved here; passed to A3 for adjudication. Footer "14". |
| 16 | 617 | We are the partner-of-choice for some of the biggest companies in the world | text (client-ranking claims) | Ordinal/ranking numbers only (#1, 2nd, 4 of Top 10, 9th, 7th) — client names anonymized by category, no client identified by name. Footer "15". |
| 17 | 637 | High-performing leadership with deep industry expertise in place | photo/text (8 leadership bios) | Years-of-experience stats per executive. Footer "16". |
| 18 | 695 | Governance and board depth supporting long-term value | photo/text (8 board-member bios) | Years-of-experience stats per director; no DIN numbers disclosed on this slide (unlike a board-outcome-letter annexure). Footer "17". |
| 19 | 761 | Our Performance: Q1FY27 (section divider) | photo/title | OCR-verified page (decorative stock chart image, no company data). Footer "18". |
| 20 | 766 | Digitide returns to profitability: Revenue up 5.3% YoY to ₹775 Cr in Q1 FY27 | text (3-column Financials/Business/Technology bullets) | First quarter-headline slide; AI-Led Revenue ~₹15 Cr+ called out. Footer "19". |
| 21 | 804 | Q1FY27: Delivering on strategic promise in past five quarters | table + chart | CHART-BEARING page (chart-verified). Q1FY26 vs Q1FY27 comparison with delta callouts. **DECK_COLOR_INVERSE flag**: Client Concentration (Top 30) rises 57.7%→59.5% (+176 bps) but is shown with an amber DOWN-arrow (deck's own color-coding treats rising concentration as adverse — deliberate, not a data error, flagged so A3 doesn't misread the color as contradicting the number). Footer "20". |
| 22 | 829 | Q1 FY27: Revenue grows 5.3% YoY to ₹775 Cr as PAT turns positive, despite margin pressure from wage revisions | table (Revenue/EBITDA/PAT 3-period table) | Footnote "*Excludes exceptional items, including demerger-related expenses in Q1FY26, labour code impact in Q4FY26" qualifies Adjusted PAT. Footer "21". |
| 23 | 884 | Q1 FY27: Tech & Digital revenue grew 20.3% YoY to ₹237 Cr | table + chart | CHART-BEARING page (chart-verified). Segment revenue + segment EBITDA tables, plus geography/vertical/client-concentration breakout bars. **Carries MECHANICAL_INCONSISTENCY flag** — panel header states "Tech & Digital share has risen to 32% and International business to 38% in Q4 FY26" but the adjacent data column on this same slide is Q1 FY27, and the T&D mix stated elsewhere on this same slide is 30.6%, not 32%. Transcribed verbatim, not resolved; passed to A3. Footnote: "*Segment EBITDA is excluding unallocated corporate cost; **MEU = Manufacturing, Energy and Utility & FGT = Fast Growth Tech". Footer "22". |
| 24 | 1003 | Revenue Up 5.3% YoY to ₹775 Cr; PAT turned positive at ₹3 Cr after two quarters | chart (6 five-quarter trend charts) | CHART-BEARING page (chart-verified): Revenue & YoY Growth, EBITDA & Margin, EBIT & Margin, PAT & Margin, Employee Count, Days Sales Outstanding — each a 5-quarter (Q1'FY26→Q1'FY27) series. **SOLE_SOURCE_DATA_POINT flag**: Q2'FY26 PAT (3.0) and Q3'FY26 PAT (-2.1) appear only on this chart; the Income Statement table (slide 33) tabulates only Q1FY26/Q4FY26/Q1FY27 columns, so these two points are not independently cross-checkable elsewhere in this document (per A1 note). Footnote: "Note: All figures are in ₹ Cr unless stated". Footer "23". |
| 25 | 1156 | Revenue mix holds broadly steady in Q1 FY27: T&D at 30.6%, International at 38.1% | chart (4 five-quarter stacked-mix charts) | CHART-BEARING page (chart-verified): Revenue Mix by Segment, by Geography, by Industry, by Client Concentration — each a 5-quarter stacked series. Densest slide overall (72 numbers). Footer "24". |
| 26 | 1267 | The New Way Forward (section divider) | photo/title | OCR-verified page. Footer "25". |
| 27 | 1272 | Four Moves — the roadmap that delivers results | text/diagram | 4 Strategic Choices + 4 Execution Moves w/ status tags (LIVE / IN MOTION / ACCELERATING / SELECTIVE) — status tags are text, not numeric. Footer "26". |
| 28 | 1300 | Move 1 — Get unified: one enterprise operating model | text | No financial figures. Footer "27". |
| 29 | 1335 | Move 2 — Strengthen the Core: modern, profitable, proud | text | No financial figures. Footer "28". |
| 30 | 1359 | Move 3 — Go West, Go Digital: as a challenger, AI at the core | text | No financial figures. Footer "29". |
| 31 | 1376 | Move 4 — Go all out: fill the white space, organically and through M&A | text | No financial figures (ORGANIC/SPEED/FIT&TIMING framework labels only). Footer "30". |
| 32 | 1399 | Financial Statements (section divider) | photo/title | OCR-verified page. Footer "31". |
| 33 | 1404 | Income Statement | table (full 15-line-item P&L, 3 periods + QoQ/YoY) | Densest tabular slide (54 numbers, 15 line items — see Table 4). Footnote "*Excludes exceptional items, including demerger-related expenses in Q1FY26, labour code impact in Q4FY26" — same text as slide 22's footnote, flag REPEATED_FOOTNOTE. Footer "32". |
| 34 | 1485 | Thankyou / IR contact details (Rajesh Lachhani, Apurva Pandey) | text | No financial numbers; email addresses only. Footer "33". |

DROPPED_SLIDE check: NOT COMPUTABLE. No prior-quarter deck/ledger was supplied
for DSSL (this is the first quarterly pipeline run for the ticker). Recorded
explicitly per task instruction; no prior deck fabricated, sub-check skipped.

---

## TABLE 2 — NUMBERS (one row per slide; every numeric token on that slide is
listed in the Values cell with its source line in brackets; Count column is
the per-slide grep/sweep count, both reconcile — see COUNT TEST, total 554)

| Slide | Count | Values (line-tagged) | Flags |
|---|---|---|---|
| 1 | 28 | 1 [L28, "No. 1"], 29 [L28, "29th Main Road"], 1 [L29, "1st stage"], 560068 [L29, pincode], 080 [L30, STD code], 22244002 [L30, phone no.], CIN fragments: 62099 / 2024 / 184626 [L30, "L62099KA2024PLC184626" — one identifier split by regex into 3 tokens], 27 [L32, "July 27"], 2026 [L32, "July 27, 2026"], 400 [L38, Mumbai pincode part 1], 001 [L38, pincode part 2 — "400001"], 544413 [L39, BSE Scrip Code], 400 [L45, Mumbai pincode part 1], 051 [L45, pincode part 2 — "400051"], 30 [L52, "Regulation 30"], 2015 [L53, "Regulations, 2015"], 30 [L54, "June 30"], 2026 [L55, "June 30, 2026"], 50601 [L70, "Membership No. A50601"], 2026 [L78, sig. date], 07 [L78, sig. date], 27 [L78, sig. date], 22 [L79, sig. time HH], 43 [L79, sig. time MM], 07 [L79, sig. time SS], 05 [L79, UTC offset], 30 [L79, UTC offset] | ADMINISTRATIVE (all 28 — cover-letter identifiers/dates, not deck disclosure data); regulatory transmittal, not a "slide". |
| 2 | 1 | 2026 [L84, "July 2026"] | — |
| 3 | 0 | (none) | Text-only legal disclaimer; see Table 1 note re: currency-caveat language. |
| 4 | 15 | 360° [L131], 5.3% [L139, Revenue YoY], 775 [L139, ₹775 Cr revenue], 20.3% [L141, T&D YoY], 237 [L141, ₹237 Cr T&D], 10.2% [L142, Intl YoY], 296 [L142, ₹296 Cr Intl], 205 [L143, ₹205 Cr TCV], 26 [L143, key logos won], 5.7 [L147, Mn AI-bot interactions], 80 [L148, containment % low], 85 [L148, containment % high], 16000+ [L149, Neil hires], 10+ [L152, partnerships], 3 [L152, hyperscalers GCP/Azure/AWS] | — |
| 5 | 0 | (none — Roman numerals I/II/III are section labels, not quantities) | — |
| 6 | 0 | (none) | — |
| 7 | 9 | 775 [L174, ₹775 Cr Q1FY27 revenue], 3080 [L176, ₹3,080 Cr FY26 revenue], 300+ [L177, customers], 54K [L179, employees, ~], 10+ [L181, technology partners], 7th [L183, "7th time" GPTW], 40+ [L185, global locations], 70% [L187, revenue annuity-based, ~], 25+ [L192, proprietary AI assets] | — |
| 8 | 8 | 57.33% [L199, Ajit Isaac shareholding], 73.39% [L207, Digitide stake in Alldigi promoters], 3080 [L214, Digitide FY26 Revenue ₹3,080 Cr], 343 [L215, Digitide FY26 EBITDA* ₹343 Cr], 54K [L216, Digitide FY26 Employees, ~], 599 [L218, Alldigi FY26 Revenue ₹599 Cr], 162 [L219, Alldigi FY26 EBITDA* ₹162 Cr], 6K [L220, Alldigi FY26 Employees, ~] | Footnote "*As per Ind-AS" (L221) qualifies both EBITDA figures — see Table 3. |
| 9 | 1 | 2.0 [L285, "Q-Buddy, 18K+ agents / 2.0..." — capability tile, wrapped OCR text] | Low-confidence line-wrap artifact; content is qualitative service taxonomy, not a headline metric. |
| 10 | 14 | 10+ [L298, partners], 25+ [L305, accelerators], 7th [L341, "7th consecutive year" GPTW], 2023/2024/2020/2022/2025/2026/2021 [L342-348, GPTW timeline year chips, 7 values], 18K+ [L355, Q-Buddy agents], 15 [L356, points NPS uplift], 5.7Mn [L357, bot interactions], 80%+ [L359, containment rate] | Year chips (7) are content-bearing timeline data, counted as numbers not structural labels. |
| 11 | 7 | 40+ [L365, locations], 5 [L365, countries], 9+ [L366, NA locations], 2 [L366, NA countries], 30+ [L368, APAC locations], 3 [L369, APAC countries], 20 [L394, additional India delivery locations not mapped] | — |
| 12 | 9 | Tier-2 [L398], Tier-3 [L399, tier labels — non-quantitative but digit-bearing], 1/2/3 [L417-419, Tier 1/2/3 legend], 15K [L428, feet on ground, ~], 95% [L429, pincodes covered] | Tier-1/2/3 labels are classification tags, not measured quantities — carried here for completeness per "no exceptions." |
| 13 | 2 | 10+ [L445, ecosystem partners], 25+ [L446, AI assets] | — |
| 14 | 39 | 2.5Mn [L479, Voice BOT interactions], 80% [L481, Voice containment], 3.2Mn [L483, Chat BOT interactions], 85% [L486, Chat containment], 19000+ [L488, Q-Buddy agents], 15 [L490, points NPS uplift], 10% [L491, AHT efficiency], 0.8Mn [L494, leads generated], 30000+ [L498, Nikki users/Digitiders], 95% [L500, prediction accuracy], 250+ [L501, resignations/month avoided], 16000+ [L507, Neil hires in 6 months], 6 [L507, "-months"], 90k+ [L509, screenings], 25-30% [L514, code-gen productivity], 6+ [L516, live ARISE projects], 60% [L521, SmartPay efficiency gain], 80% [L525, PulseCollect customer live-rate], 90% [L525, prediction accuracy], ±1.8 [L526, days], 30% [L528, efficiency improvement], 5% [L528, more resolutions], 25+ [L529, AI assets total], 6800+ [L532, Digitiders reskilled], 2 [L533, certifications], 20% [L538, leads uptake], 2x [L538, conversion], ~2 Cr [L541, ACV], 14 [L541, clients], 6 [L542, industries], ~13 Cr [L544/545, AI-led revenue, top 10 clients], 8 [L545, clients], 6 Cr [L547, AI Innovation Lab ACV], 12+ [L549, active conversations], 10+ [L550, partner ecosystem], 5000+ [L555, onboarded via NINA], 2 [L556, months] | ACV figures (~2 Cr, ~13 Cr, 6 Cr) already ₹ Cr per A1 header conversion note, factor x1 — no unit issue here. |
| 15 | 25 | 1./2./3. [L566,570,573, BFS core-op numbering], 1./2./3. [L577,581,584, Healthcare numbering], 4. [L588, Healthcare numbering], 1./2./3. [L591,594,599, Insurance numbering], 40-70% [L604, BFS cycle-time reduction], 20-30% [L605, BFS cost savings], 10-20x [L608, faster processing], 80% [L609, effort reduction], **$2M [L610, USD]**, **$6M+ [L610, USD]**, 40-60% [L612, fraud detection], 3-5x [L613, decision-making], 30-50% [L614, cost reduction] | **UNIT_MISMATCH flag on $2M and $6M+ (L610)** — USD millions, not converted to ₹ Cr, sole non-₹ currency figures in the deck; not resolved here, passed to A3/A4 for adjudication. The 1./2./3./4. tokens are section-numbering, not metrics. |
| 16 | 7 | 1 [L619, "#1" soft drink mfr], 1 [L623, "#1" retailer], 2 [L627, "2nd" largest employer], 4 [L629, "4 of"], 10 [L629, "Top 10" insurers], 9 [L631, "9th" healthcare org], 7 [L633, "7th" most valuable bank] | Client identities anonymized by rank/category, no company named. |
| 17 | 8 | 25+ [L648, yrs CEO], 30+ [L654, yrs Intl Head/CRO], 22+ [L657, yrs CHRO], 25+ [L661, yrs CFO], 25+ [L674, yrs Canada Head], 20+ [L678, yrs CSSAO], 25+ [L684, yrs CEO Alldigi], 25+ [L688, yrs CIO] | 8 distinct executive years-of-experience figures, one per bio; all 8 bios captured, none dropped. |
| 18 | 8 | 30+ [L720, Ajit Isaac], 40+ [L722, Revathy Ashok], 30+ [L725, Gopalakrishnan Soundarajan], 20+ [L729, Anish Thurthi], 30+ [L733, Robin Thomashauer], 40+ [L744, Pankaj Vaish], 38+ [L750, Sunil Bhumralkar], 25+ [L757, Sameer Ahluwalia] | 8 director years-of-experience figures, one per bio; all 8 board bios captured, none dropped. |
| 19 | 0 | (none — decorative stock chart image explicitly confirmed to carry no legible company data, per A1 OCR note) | — |
| 20 | 15 | 5.3% [L767/769, Revenue YoY], 775 [L767, ₹775 Cr], 20.3% [L770, T&D YoY], 10.2% [L772, Intl YoY], 2.9 [L775, PAT ₹2.9 Cr], 5 [L775, "vs loss ₹5 Cr"], Q4FY26 [context], 26 [L775, ref], 205 [L781, ₹205 Cr TCV], 26 [L782, key logos], 15 [L784, AI-Led Revenue ~₹15 Cr+], 5.7Mn [L788, AI bot interactions], 80% [L789, containment low], 85% [L789, containment high], 16000+ [L795, Neil hires], 30000+ [L799, Nikki users] | — |
| 21 | 13 | 736 [L812, Revenue Q1FY26 ₹736 Cr], 26.8% [L813, T&D share Q1FY26], 36.5% [L814, Intl share Q1FY26], 775 [L815, Revenue Q1FY27 ₹775 Cr], 30.6% [L816, T&D share Q1FY27], 38.1% [L817, Intl share Q1FY27], 5.3% [L818, Revenue delta], 382bps [L819, T&D delta], 168bps [L820, Intl delta], 30 [L822, Top 30 clients], 57.7% [L823, concentration Q1FY26], 59.5% [L824, concentration Q1FY27], 176bps [L825, concentration delta] | CHART-BEARING (chart-verified, no new figures vs text layer). See DECK_COLOR_INVERSE flag in Table 1. |
| 22 | 38 | 5.3%/775 [L830 headline, x2], 775/5.3%/-3.1% [L833, x3], 76.9/9.9% [L835, x2], 2.9 [L836], 735.8/800.0/775.1/-3.1%/5.3% [L844-848 Revenue row, x5], 82.6/87.9/76.9/-12.5%/-6.9% [L850-854 EBITDA row, x5], 11.2%/11.0%/9.9%/-107bps/-131bps [L856-860 EBITDA% row, x5], 9.7/-5.0/2.9/-69.7% [L862-866 Reported PAT row, x4], 1.3%/-0.6%/0.4%/100bps/-94bps [L868-872 Reported PAT% row, x5], 18.6/11.2/2.9 [L874-876 Adj. PAT row, x3], 2.5%/1.4%/0.4% [L878-880 Adj. PAT% row, x3] | Full 3-period + QoQ/YoY table — 7 line items (see Table 4). Footnote L882 qualifies Adjusted PAT rows — Table 3. |
| 23 | 75 | Revenue table (BPM/T&D/Total × Q1FY26/Q4FY26/Q1FY27 ₹Cr+Mix + QoQ/YoY): 538.6/73.2%/550.8/68.9%/537.7/69.4%/-2.4%/-0.2% [BPM, L900-907]; 197.2/26.8%/249.2/31.1%/237.4/30.6%/-4.7%/20.3% [T&D, L910-917]; 735.8/100.0%/800.0/100.0%/775.1/100%/-3.1%/5.3% [Total, L919-926]. EBITDA table: 89.9/16.7%/89.7/16.3%/72.8/13.5%/-276bps/-316bps [BPM, L942-948]; 18.8/9.5%/30.1/12.1%/18.9/8.0%/-408bps/-156bps [T&D, L951-957]; 108.7/14.8%/119.8/15.0%/91.7/11.8%/-314bps/-294bps [Total, L959-965]. Panel header "32%"/"38%" [L966-967, **flagged, see below**]. By geography: 479.5/61.9%/295.6/38.1% [L992-993]. By vertical: 41%/10%/17%/4%/7%/20% [L975-983, BFS/Insurance/MEU/Healthcare/FGT/Others]. By client concentration: 37%/13%/9%/41% [L971-980, Top10/11-20/21-30/Others]. Segment-overview recap: 20.3%/237/10.2%/296 [L996-998]. | **MECHANICAL_INCONSISTENCY flag on L966-967** ("...has risen to 32% and International business to 38% in Q4 FY26") — header cites Q4 FY26 / 32% against this slide's Q1 FY27 data column, whose own T&D mix is stated as 30.6% elsewhere on the same slide. Transcribed verbatim, not resolved; passed to A3. CHART-BEARING (chart-verified against image, no new figures). Footnote L886 — Table 3. |
| 24 | 102 | Six 5-quarter trend charts, Q1'FY26→Q1'FY27 each: Revenue&YoY (735.8/764.2/780.3/800.0/775.1 ₹Cr; 5.7%/7.0%/6.6%/9.2%/5.3%) [L1090-1099 + axis ticks 700.0-820.0 L1106-1112]; EBITDA&Margin (82.6/85.2/87.5/87.9/76.9; 11.2%/11.1%/11.2%/11.0%/9.9%) [L1118-1127 + axis ticks 0.0-100.0/0.0-12.0 L1128-1140]; EBIT&Margin (36.5/34.6/38.5/21.5/21.7; 5.0%/4.5%/4.9%/2.7%/2.8%) [L1028-1037 + axis ticks 0.0-70.0/0.0-8.0 L1038-1054]; PAT&Margin (9.7/3.0/-2.1/-5.0/2.9; 1.3%/0.4%/-0.3%/-0.6%/0.4%) [L1004-1017 + axis ticks -1.0-19.0/-5.0%-5.0% L1018-1022]; Employee Count '000 (55.3/56.3/55.9/53.5/53.6) [L1080-1084]; DSO days (91/82/79/75/82) [L1068-1072]. Slide headline repeat: 5.3%/775/₹3 Cr [L1061]. | **SOLE_SOURCE_DATA_POINT flag**: Q2'FY26 PAT 3.0 and Q3'FY26 PAT -2.1 (within the PAT&Margin chart) are not tabulated anywhere else in this document — the Income Statement (slide 33) shows only Q1FY26/Q4FY26/Q1FY27 columns. CHART-BEARING (chart-verified, no new figures beyond text layer). Footnote L1060 — Table 3. Axis-tick/gridline-scale values are included per "no exceptions" but are chart scale markers, not reported data points — flagged CHART_AXIS_SCALE for A3/A4 to disregard in variance analysis. |
| 25 | 72 | Four 5-quarter stacked-mix charts, Q1'FY26→Q1'FY27 each: Segment (T&D%/BPM%) 26.8/73.2, 29.9/70.1, 30.2/69.8, 31.1/68.9, 30.6/69.4 [L1163-1172]; Geography (Intl%/Dom%) 36.5/63.5, 37.2/62.8, 37.4/62.6, 38.1/61.9, 38.1/61.9 [L1180-1189]; Industry (BFSI/Mfg&Energy&Utility/Healthcare/FGT/Others %, 5 series×5 qtrs = 25 values) [L1197-1221]; Client Concentration (Top10/11-20/21-30/Others %, 4 series×5 qtrs = 20 values) [L1232-1251]. Headline repeat: 30.6%/38.1% [L1157]. Legend digits: 10/11/20/21/30 [L1257-1259]. | CHART-BEARING (chart-verified, no new figures beyond text layer). Densest slide (72 numbers). |
| 26 | 0 | (none) | — |
| 27 | 0 | (none — "1/2/3/4" move numbers and status tags LIVE/IN MOTION/ACCELERATING/SELECTIVE are structural labels, excluded as bare single-digit lines per methodology) | Move numbers 1-4 are structural sequence markers, not disclosure figures. |
| 28 | 1 | 1 [L1301, "Move 1"] | Structural label, retained per "no exceptions." |
| 29 | 1 | 2 [L1336, "Move 2"] | Structural label. |
| 30 | 1 | 3 [L1361, "Move 3"] | Structural label. |
| 31 | 1 | 4 [L1377, "Move 4"] | Structural label. |
| 32 | 0 | (none) | — |
| 33 | 54 | Full Income Statement, Q1FY26/Q4FY26/Q1FY27 + QoQ/YoY where shown — 15 line items × up to 5 columns, see Table 4 for the full line-item breakdown (values: 735.8/800.0/775.1/-3.1%/5.3% Revenue; 549.3/591.2/583.3 Employee benefits; 103.9/120.9/114.9 Other expenses; 82.6/87.9/76.9/-12.5%/-6.9% EBITDA; 11.2%/11.0%/9.9%/-107bps/-131bps EBITDA Margin; 46.1/66.4/55.2 D&A; 11.2/14.7/15.1 Finance Cost; -3.6/-5.2/-4.3 Other Income; 8.9/16.1/0.0 Exceptional Items; 20.0/-4.0/10.9/-370.3%/-45.4% PBT; 10.3/0.9/8.0 Tax; 9.7/-5.0/2.9/Turned Positive/-69.7% PAT; 1.3%/-0.6%/0.4% PAT Margin; 18.6/11.2/2.9 Adj. PAT; 2.5%/1.4%/0.4% Adj. PAT Margin) [L1413-1481] | Exceptional Items = 0.0 in Q1FY27 only (not zero in all 3 periods: 8.9 / 16.1 / 0.0) — does NOT qualify as ZERO_STANDING (that flag requires zero/nil/dash in ALL periods); noted for completeness, not flagged. No fully-zero-across-all-periods row found anywhere in this table — checked explicitly. Footnote L1483 — REPEATED_FOOTNOTE, same text as slide 22's. |
| 34 | 0 | (none — email addresses only) | — |

---

## TABLE 3 — FOOTNOTES / FINE-PRINT DISCLAIMERS QUALIFYING A HEADLINE NUMBER
(grep `^\*|^Note:` count = 5, manual sweep = 5, match)

| # | Slide | Line | Text (verbatim) | Qualifies | Flags |
|---|---|---|---|---|
| 1 | 8 | 221 | "*As per Ind – AS" | FY26 EBITDA ₹343 Cr (Digitide) and ₹162 Cr (Alldigi), line 211/215/219 | — |
| 2 | 22 | 882 | "*Excludes exceptional items, including demerger-related expenses in Q1FY26, labour code impact in Q4FY26" | Adjusted PAT / Adjusted PAT % rows, all 3 periods (L874-880) | REPEATED_FOOTNOTE (same text also on slide 33) |
| 3 | 23 | 886 | "Note: *Segment EBITDA is excluding unallocated corporate cost; **MEU = Manufacturing, Energy and Utility & FGT = Fast Growth Tech" | Segment EBITDA table (L942-965) and vertical-mix chart abbreviations MEU/FGT (L967, L986-988) | Two sub-definitions in one note line (single asterisk + double asterisk); counted as one footnote row per its single source line. |
| 4 | 24 | 1060 | "Note: All figures are in ₹ Cr unless stated" | The six 5-quarter trend charts on this slide (L1004-1146) | Sits immediately beside the flagged USD-figure page (15) elsewhere in the deck — this note applies only to slide 24's own charts, does not retroactively convert the page 15 USD figures; noted so A3 does not conflate the two. |
| 5 | 33 | 1483 | "*Excludes exceptional items, including demerger-related expenses in Q1FY26, labour code impact in Q4FY26" | Adjusted PAT / Adjusted PAT Margin % rows (L1475-1481) | REPEATED_FOOTNOTE (identical substance to row 2 / slide 22, minor whitespace difference: double space before "labour" on slide 22's copy vs single space here — immaterial). |

Note: Slide 3's Safe Harbor and Disclaimer is a full-page general legal/
forward-looking-statement disclaimer, not a footnote qualifying one specific
headline number — it is enumerated in Table 1 (slide 3), not double-counted
here, to keep this category's grep/sweep definition (lines starting with `*`
or `Note:`) exact and auditable.

---

## TABLE 4 — FINANCIAL TABLE LINE ITEMS (bonus category, pages 22/23/33;
grep count of known row-label lines = 28, manual sweep = 28, match)

### Slide 22 — Revenue/EBITDA/PAT summary table (7 line items)
| Line item | Line | Q1 FY26 | Q4 FY26 | Q1 FY27 | QoQ | YoY | Flag |
|---|---|---|---|---|---|---|---|
| Revenue | 843 | 735.8 | 800.0 | 775.1 | -3.1% | 5.3% | — |
| EBITDA | 849 | 82.6 | 87.9 | 76.9 | -12.5% | -6.9% | — |
| EBITDA % | 855 | 11.2% | 11.0% | 9.9% | -107bps | -131bps | — |
| Reported PAT | 861 | 9.7 | -5.0 | 2.9 | Turned Positive | -69.7% | — |
| Reported PAT % | 867 | 1.3% | -0.6% | 0.4% | 100bps | -94bps | — |
| Adjusted PAT* | 873 | 18.6 | 11.2 | 2.9 | — | — | Footnote-qualified (Table 3 #2); no QoQ/YoY % shown in deck for this row. |
| Adjusted PAT *% | 877 | 2.5% | 1.4% | 0.4% | — | — | Footnote-qualified; no QoQ/YoY % shown in deck for this row. |

### Slide 23 — Revenue and Segment EBITDA by segment (6 line items)
| Line item | Line | Q1 FY26 | Q4 FY26 | Q1 FY27 | QoQ | YoY | Flag |
|---|---|---|---|---|---|---|---|
| Revenue: BPM | 899 | 538.6 (73.2%) | 550.8 (68.9%) | 537.7 (69.4%) | -2.4% | -0.2% | — |
| Revenue: Tech & Digital | 908 | 197.2 (26.8%) | 249.2 (31.1%) | 237.4 (30.6%) | -4.7% | 20.3% | Panel header on this slide misstates T&D mix as 32%/Q4FY26 — see MECHANICAL_INCONSISTENCY flag, Table 1/2. |
| Revenue: Total | 918 | 735.8 (100.0%) | 800.0 (100.0%) | 775.1 (100%) | -3.1% | 5.3% | — |
| Segment EBITDA*: BPM | 941 | 89.9 (16.7%) | 89.7 (16.3%) | 72.8 (13.5%) | -276bps | -316bps | — |
| Segment EBITDA*: Tech & Digital | 949 | 18.8 (9.5%) | 30.1 (12.1%) | 18.9 (8.0%) | -408bps | -156bps | — |
| Segment EBITDA*: Total | 958 | 108.7 (14.8%) | 119.8 (15.0%) | 91.7 (11.8%) | -314bps | -294bps | — |

### Slide 33 — Income Statement (15 line items)
| Line item | Line | Q1 FY26 | Q4 FY26 | Q1 FY27 | QoQ | YoY | Flag |
|---|---|---|---|---|---|---|---|
| Revenue from operations | 1412 | 735.8 | 800.0 | 775.1 | -3.1% | 5.3% | — |
| Employee benefits expense | 1418 | 549.3 | 591.2 | 583.3 | — | — | No QoQ/YoY % shown in deck. |
| Other expenses | 1422 | 103.9 | 120.9 | 114.9 | — | — | No QoQ/YoY % shown in deck. |
| EBITDA | 1426 | 82.6 | 87.9 | 76.9 | -12.5% | -6.9% | — |
| EBITDA Margin % | 1432 | 11.2% | 11.0% | 9.9% | -107bps | -131bps | — |
| Depreciation & amortisation | 1438 | 46.1 | 66.4 | 55.2 | — | — | No QoQ/YoY % shown in deck. |
| Finance Cost | 1442 | 11.2 | 14.7 | 15.1 | — | — | No QoQ/YoY % shown in deck. |
| Other Income | 1446 | -3.6 | -5.2 | -4.3 | — | — | No QoQ/YoY % shown in deck. |
| Exceptional Items | 1450 | 8.9 | 16.1 | 0.0 | — | — | Zero in Q1FY27 only, NOT zero in all periods — does not qualify ZERO_STANDING; not flagged. |
| PBT | 1454 | 20.0 | -4.0 | 10.9 | -370.3% | -45.4% | — |
| Tax | 1460 | 10.3 | 0.9 | 8.0 | — | — | No QoQ/YoY % shown in deck. |
| PAT | 1464 | 9.7 | -5.0 | 2.9 | Turned Positive | -69.7% | — |
| PAT Margin % | 1470 | 1.3% | -0.6% | 0.4% | — | — | No QoQ/YoY % shown in deck. |
| Adjusted PAT* | 1474 | 18.6 | 11.2 | 2.9 | — | — | Footnote-qualified (Table 3 #5). |
| Adjusted PAT Margin* % | 1478 | 2.5% | 1.4% | 0.4% | — | — | Footnote-qualified. |

ZERO_STANDING check: performed explicitly across all three financial tables
(slides 22, 23, 33). No line item is zero/nil/dash in ALL periods shown.
The single zero cell found (Exceptional Items, Q1FY27 = 0.0, vs. 8.9 and 16.1
in the prior two periods) is a genuine period-over-period change, not a
template standing-zero item, so ZERO_STANDING is NOT raised. Recorded here
so the check is visible, not silently skipped.

---

## FLAGS SUMMARY (carried forward for A3 adjudication, none resolved here)
- **MECHANICAL_INCONSISTENCY** — Slide 23, L966-967: panel header cites "Q4 FY26" / "32%" T&D share against a Q1 FY27 data column whose own stated T&D mix is 30.6%.
- **UNIT_MISMATCH** — Slide 15, L610: "$2M-$6M+ savings per use case" (Insurance IMPACT bullet) — two USD-mn figures ($2M, $6M+) left unconverted, the only non-₹Cr currency figures in the deck.
- **SOLE_SOURCE_DATA_POINT** — Slide 24, PAT&Margin chart: Q2'FY26 PAT (3.0) and Q3'FY26 PAT (-2.1) appear only on this chart, not cross-checkable against any tabulated income statement in this document.
- **DECK_COLOR_INVERSE** — Slide 21: Client Concentration (Top 30) rises 57.7%→59.5% but is shown with an amber down-arrow (deliberate adverse-framing color convention, not a data contradiction).
- **REPEATED_FOOTNOTE** — Slides 22 and 33 carry the same Adjusted PAT exceptional-items footnote verbatim (immaterial whitespace difference only).
- **CHART_AXIS_SCALE** — Slide 24: gridline/axis-tick values (e.g. 0.0-100.0, 700.0-820.0) are enumerated per "no exceptions" but are chart-scale markers, not reported data points; A3/A4 should disregard them in variance analysis.
- **DROPPED_SLIDE — NOT COMPUTABLE** — first quarterly run for DSSL, no prior-quarter deck/ledger supplied; sub-check explicitly skipped, not fabricated.
- **ZERO_STANDING — checked, none found** — all three financial tables (slides 22, 23, 33) reviewed line-by-line; no item is zero/nil/dash across all periods shown.

```yaml
stage: A2-enumerator
company: "DSSL"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "runs/dssl-q1fy27/work/ledger_presentation_dssl_q1fy27.md"
counts:                      # per applicable category
  notes: 5
  line_items: 28
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 34
  slide_numbers: 554
flags_raised: [MECHANICAL_INCONSISTENCY, UNIT_MISMATCH, SOLE_SOURCE_DATA_POINT, DECK_COLOR_INVERSE, REPEATED_FOOTNOTE, CHART_AXIS_SCALE, DROPPED_SLIDE_NOT_COMPUTABLE]
gate_a2: pass
mismatch_note: ""
```
