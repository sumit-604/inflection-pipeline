# A2 ENUMERATION LEDGER — Asian Energy Services Limited (ASIANENE), Q1 FY27, doctype: pressrelease

Source: /home/user/inflection-pipeline/runs/asianene-q1fy27/work/extract_pressrelease_asianene_q1fy27.txt
Unit convention: Crores (x1), per A1 header line 7-8.
Document type: 4-page narrative press release (covering letter + press release body + About sections). Not a tabular results filing, not a concall, not an investor deck — enumerated per the task-message scope as a narrative disclosure document across four categories: headline financial numbers, management quotes, forward-looking/guidance statements, operational claims.

=== A2 COUNT TEST ===
category: headline_numbers   grep_count: 19   sweep_count: 19   match: yes
category: quotes             grep_count: 2    sweep_count: 2    match: yes
category: forward_statements grep_count: 8    sweep_count: 8    match: yes
category: operational_claims grep_count: 12   sweep_count: 12   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note (grep vs sweep):
- headline_numbers: grep pass 1 = `grep -n -o -E "[0-9][0-9,.]*\s*crore"` (8 hits) + `grep -n -o -E "[0-9][0-9.]*%"` restricted to body lines (15 hits, excludes header metadata "100%" on line 10) + bare chart figures without a "crore"/"%" suffix on lines 95/96/98 (6 tokens: 271.2, 12.8, 21.9, 115.4, 12.1, 5.6) = 29 raw numeric tokens. Sweep collapsed these 29 tokens into 19 discrete "headline number stated" units (a single sentence stating both a Rs-crore value and its YoY % is one unit per instance; each restatement of the same fact in a different location — bullet, narrative para, chart, quote — is enumerated as its own unit since it carries its own line number). Noise tokens excluded from both passes: quarter labels (Q1, FY27, FY26 -> "27"/"26"/"1"), calendar date tokens (13, 2026, 30 from "June 30, 2026" / "August 13, 2026"), and boilerplate identifiers (CIN, phone, BSE scrip code, membership number). 19 = 19, match.
- quotes: grep pass = unicode opening-quote mark "“" (2 hits: line 124, line 139). Sweep = 2 distinct attributed management quote blocks (Dr. Kapil Garg; Mr. Sumit Maheshwari). 2 = 2, match.
- forward_statements: grep pass = `grep -n -i -E "guidance|expect|on track|remain confident|remain unchanged|approval has been received|expected to be completed|well positioned|visibility|preferred bidder|multi-year|multiplying|robust bid pipeline"` (8 matching lines: 75, 77, 78, 115, 119, 131, 144, 146). Sweep = 8 distinct forward-looking/guidance/commitment phrases, one per matched line. 8 = 8, match.
- operational_claims: grep pass = keyword sweep for contracts/projects/capacity/geography terms (order book, merger, Oilmax, GSECL, offshore, mineral mine, Middle East, domestic and international, onshore, seismic, Material Handling, Rapid Loading, CBM, quartzite, agriculture, oil & gas blocks, Samudra Manthan/ORDA Act/Critical Minerals Mission) across the body and About sections, with financial-value lines (order book Rs/₹ figures, already captured in headline_numbers) excluded to avoid double counting. Sweep = 12 distinct non-financial operational/business claims. 12 = 12, match.

---

## TABLE 1 — HEADLINE FINANCIAL NUMBERS (19 rows)

| # | Line(s) | Metric | Value stated | Period / comparator | Basis (as labelled in text) | Flags |
|---|---------|--------|---------------|----------------------|-------------------------------|-------|
| HN1 | 69 | PAT growth (headline title) | "Q1 Profit Surges by 129% To Rs 12.8 Crore" | Q1FY27 vs Q1FY26 (YoY) | Not explicitly labeled standalone/consolidated in this line | — |
| HN2 | 73 | Revenue | Rs 271.2 crore (▲135% YoY) | Q1FY27 vs Q1FY26 | Not explicitly labeled in this bullet (see HN9 for confirmed-consolidated chart restatement) | — |
| HN3 | 73 | EBITDA | Rs 21.9 crore (▲81% YoY) | Q1FY27 vs Q1FY26 | Not explicitly labeled in this bullet | — |
| HN4 | 74 | PAT | Rs 12.8 crore (▲129% YoY) | Q1FY27 vs Q1FY26 | Not explicitly labeled in this bullet | — |
| HN5 | 77 | Order book | Rs 1,754 crore ("provides multi-year revenue visibility") | As of period-end (implied June 30, 2026) | No basis label in this bullet (cf. HN15 which explicitly says "standalone") | — |
| HN6 | 83-84 | Net profit (narrative restatement) | 129% YoY to Rs 12.8 crore | Q1FY27 vs Q1FY26 | Not labeled | duplicate of HN1/HN4 fact, separate occurrence |
| HN7 | 84 | Revenue (narrative restatement) | 135% to Rs 271.2 crore | Q1FY27 vs Q1FY26 | Not labeled | duplicate of HN2 fact, separate occurrence |
| HN8 | 89 | Section basis header | "Performance Highlights Consolidated – Q1 FY27" | Q1FY27 | CONSOLIDATED (explicit) | scopes HN9-HN14 |
| HN9 | 95 | Revenue (chart, current period) | 271.2 | Q1FY27 | CONSOLIDATED (per HN8) | duplicate of HN2/HN7 |
| HN10 | 98 | Revenue (chart, prior period) + growth | 115.4; growth 135% | Q1FY26 | CONSOLIDATED (per HN8) | prior-year absolute value not stated elsewhere |
| HN11 | 96 | EBITDA (chart, current period) | 21.9 | Q1FY27 | CONSOLIDATED (per HN8) | duplicate of HN3 |
| HN12 | 98 | EBITDA (chart, prior period) + growth | 12.1; growth 81% | Q1FY26 | CONSOLIDATED (per HN8) | prior-year absolute value not stated elsewhere |
| HN13 | 95 | PAT (chart, current period) | 12.8 | Q1FY27 | CONSOLIDATED (per HN8) | duplicate of HN4/HN6 |
| HN14 | 98 | PAT (chart, prior period) + growth | 5.6; growth 129% | Q1FY26 | CONSOLIDATED (per HN8) | prior-year absolute value not stated elsewhere |
| HN15 | 117 | Order book | ₹1,754 crore, as of June 30, 2026 | Q1FY27 period-end | STANDALONE (explicit: "Asian Energy's standalone order book") | cf. HN5/HN18 unlabeled restatements of the same figure |
| HN16 | 117-118 | Order book segment split | ~60% Oil & Gas, ~40% Mineral services | As of June 30, 2026 | STANDALONE (inherits HN15 basis) | — |
| HN17 | 142-143 | Revenue/EBITDA/PAT growth (quote restatement, Mr. Sumit Maheshwari) | revenue +135%, EBITDA +81%, PAT +129% | Q1FY27 vs Q1FY26 | Not labeled in quote | duplicate of HN2-HN4/HN9-HN14 facts |
| HN18 | 145 | Order book (quote restatement, Mr. Sumit Maheshwari) | ₹1,754 crore | As of period-end (implied) | Not labeled standalone/consolidated in quote | duplicate of HN5/HN15 |
| HN19 | 171 | OEPL shareholding in AESL | 55.99% | As of press release date (13 Aug 2026), not tied to quarter-end explicitly | Ownership stat, not a P&L figure | — |

## TABLE 2 — MANAGEMENT QUOTES (2 rows)

| # | Line(s) | Speaker | Designation | First 10-15 words | Flags |
|---|---------|---------|-------------|--------------------|-------|
| Q1 | 124-134 (attribution at 131-133) | Dr. Kapil Garg | Managing Director, Asian Energy Services Limited | "We have commenced FY27 on a strong footing, marked by focused execution across our business verticals." | — |
| Q2 | 139-148 (attribution at 146-147) | Mr. Sumit Maheshwari | Group CFO | "Q1 FY27 reflected continued progress across our businesses, with key milestones of securing a major order from GSECL." | — |

## TABLE 3 — FORWARD-LOOKING STATEMENTS, GUIDANCE, COMMITMENT PHRASES (8 rows)

| # | Line(s) | Phrase / commitment | Type | Flags |
|---|---------|----------------------|------|-------|
| FS1 | 75 | "FY27 guidance for both Asian Energy and Kuiper remain unchanged; company on track to achieve growth targets" | Guidance reaffirmation | — |
| FS2 | 77 | "Strong order book of Rs 1,754 crore provides multi-year revenue visibility" | Forward revenue-visibility claim | shares line with HN5 |
| FS3 | 78-79 | "The Company is well positioned to benefit from India's increasing focus on domestic oil & gas production and mineral production" | Forward positioning statement (macro-tailwind framing) | — |
| FS4 | 115-116 | "Approval of Shareholders has been received for the Merger and it is expected to be completed by September/October 2026" | Forward commitment with explicit timeline (M&A completion date) | material dated commitment — completion date is checkable in next quarter's ledger |
| FS5 | 119-120 | "Group continues to expand its asset portfolio, being declared the preferred bidder for an offshore block and a critical mineral mine" | Forward business-development claim (awards pending formal contract, not yet executed) | — |
| FS6 | 124-134 (quote, Dr. Kapil Garg) | "growth opportunities in our businesses are multiplying and we are well positioned to capitalize on them and create long term sustainable value for our stakeholders" | Forward statement in quote | — |
| FS7 | 139-148 (quote, Mr. Sumit Maheshwari), line 144 | "We remain confident of achieving our FY27 guidance for both Asian Energy Services and Kuiper" | Guidance reaffirmation (quote restatement of FS1) | duplicate of FS1 fact, separate occurrence |
| FS8 | 139-148 (quote, Mr. Sumit Maheshwari), line 145-146 | "supported by a robust bid pipeline, providing strong visibility for future revenues" | Forward revenue-visibility claim (quote restatement) | shares theme with FS2 |

## TABLE 4 — OPERATIONAL METRICS / CLAIMS (contracts, projects, capacity, geography) (12 rows)

| # | Line(s) | Claim | Category | Flags |
|---|---------|-------|----------|-------|
| OC1 | 86 | "contributions from both domestic and international operations" | Geography (revenue driver) | no split % given — narrative only |
| OC2 | 119-120 | "Group continues to expand its asset portfolio, being declared the preferred bidder for an offshore block and a critical mineral mine" | Project/contract pipeline (pre-award status) | not yet a signed contract — "preferred bidder" only |
| OC3 | 129-130 (in Dr. Kapil Garg quote) | Named policy tailwinds: "Samudra Manthan, ORDA Act and Critical Minerals Mission" | Regulatory/policy environment reference | — |
| OC4 | 140 (in Mr. Sumit Maheshwari quote) | "securing a major order from GSECL" | Contract win | no value or scope disclosed for this order |
| OC5 | 141 (in Mr. Sumit Maheshwari quote) | "strong execution across all verticals despite volatile Middle East situation" | Operating environment / geography risk exposure | acknowledges Middle East volatility as an operating headwind |
| OC6 | 161-163 | Oil & Gas service scope: "2D and 3D Seismic Geographical Data Acquisition, Operations and Maintenance of Onshore and Offshore Oil and Gas Production Facilities, production enhancement services" | Capacity / service-line description | boilerplate "About" section |
| OC7 | 163-164 | Mining services scope: "supply and installation of Material Handling Plants and Rapid Loading Systems" | Capacity / service-line description | boilerplate "About" section |
| OC8 | 164-167 | "Since its acquisition by Oilmax Energy Private Limited (OEPL), AESL has diversified its business verticals to capture more value across the energy and upstream oil and gas value chains" | Corporate structure / ownership history | boilerplate "About" section |
| OC9 | 171-173 | OEPL business description: "engaged in the business of exploration, development, and production of oil & gas assets... focuses on developing oil & gas blocks in India with discovered and proven oil & gas reserves" | Parent-company operations | boilerplate "About Oilmax" section |
| OC10 | 174-175 | OEPL asset portfolio: "diversified portfolio of onshore oil and gas assets with varied participating interests in 5 (five) oil & gas blocks (including one Coal Bed Methane (CBM) block)" | Asset count / geography (India, onshore) | — |
| OC11 | 175-176 | OEPL mineral-sector expansion: "acquired a quartzite block in India" | Asset / diversification claim | — |
| OC12 | 176-177 | OEPL agriculture interest: "has an interest in advanced agriculture through its subsidiary" | Diversification claim | no name, stake %, or value disclosed for this subsidiary interest |

---

## APPENDIX — COVER LETTER / FILING ADMINISTRATION (context only, not gated under Table 1-4 count test)

| Item | Line(s) | Detail |
|------|---------|--------|
| Filing recipients | 18-25 | BSE Limited (Scrip Code 530355) and National Stock Exchange (Trading Symbol ASIANENE) |
| Regulatory reference | 28-31 | Regulation 30, SEBI (LODR) Regulations, 2015 |
| Subject period | 28 | "Financial Results for the quarter ended 30th June, 2026" |
| Signatory | 45-55 | Shweta Jain, Company Secretary, Membership No. 23368 |
| Digital signature timestamp | 46-50 | 2026.08.13 17:23:20 +05'30' — press release dateline (line 82) is also "Mumbai, August 13, 2026", so signature timestamp is same-day; no board-meeting-time cross-check possible since this document does not disclose board meeting start/end times (not a Board Outcome letter) |
| Investor/media contacts | 180-188 | Company IR (investor.relations@asianenergy.com); Adfactors PR — Media: Vikas Srivastava (9867065257); IR: Parth Chauhan (9082323003, teamasianenergy@adfactorspr.com) |

## ZERO-STANDING ITEMS

None identified. This is a narrative press release with no tabular note structure; no line item is presented with a zero/nil/dash value across periods. zero_standing count = 0. (Per operating rule 3, this is recorded explicitly rather than silently omitted — there is no nil disclosure to flag in this doctype/document.)
