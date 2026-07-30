=== A2 COUNT TEST ===
category: financial_numbers        grep_count: 26   sweep_count: 26   match: yes
category: segment_claims           grep_count: 5    sweep_count: 5    match: yes
category: operational_metrics      grep_count: 1    sweep_count: 1    match: yes
category: md_commentary_sentences  grep_count: 3    sweep_count: 3    match: yes
category: footnotes_disclaimers    grep_count: 5    sweep_count: 5    match: yes
category: administrative_items     grep_count: 14   sweep_count: 14   match: yes
gate_a2: pass
=== END COUNT TEST ===

Notes on GATE A2 process: first grep pass on the administrative_items
category returned 14 (using anchors `Date:`, `BSE Limited`, `Sub:`, `Unit:
MTAR`, `ISIN:`, `Regulation 30`, `https://mtar.in`, `Digitally signed by
PRIYANKA`, `Encl:`, `About MTAR Technologies`, `Srilekha Jasthi`, `Raju
Reddy`, `Commenting on the results`) against an initial manual sweep of 13
rows that had bundled the digital-signature block (signatory + timestamp)
into a single row. The grep pass surfaced a second `Date:` hit at line 65
(the signature timestamp, distinct from the letter date at line 16 and from
the signatory identity block). Re-swept: split the signature block into
AD8a (signatory identity) and AD8b (signature timestamp) as two rows. Sweep
count rose to 14, matching grep. Gate re-run: pass.

Doctype adaptation note: this is a 4-page SEBI Reg 30(6) Investors Press
Release (narrative). No results table, no notes, no board agenda, no
auditor report, no consolidation list, no concall transcript, and no slide
deck are present in this document, so those categories from the base A2
ruleset are N/A here (0 applicable rows, not counted, not gated). The
document-specific categories enumerated below follow the adapted
PRESENTATION/narrative ruleset in the task brief (financial numbers /
segment claims / operational metrics / MD commentary / footnotes &
disclaimers), plus one additional administrative/transmittal table added
under the base A2 rule "enumerate every discrete disclosure unit" to avoid
dropping the cover-letter and contact-block content that the doctype-
specific categories do not otherwise cover.

Absence observations (not ledger rows — nothing to enumerate, but flagged
for A3/A4 attention since their absence from a Reg 30(6) press release
is itself informative): this release states NO EBITDA margin %, NO PAT
margin %, NO EPS (basic or diluted), NO order book / order inflow figure,
NO capex figure, NO headcount figure, and NO explicit numeric guidance
(only a qualitative reference to "growth guidance" in the MD quote, MD1
below, with no number attached). Confirmed by targeted grep for
margin|EPS|per share|order|capacity|capex|backlog|inflow|headcount|
employee — zero hits in the body text (lines 15-143).

---

## TABLE 1 — FINANCIAL NUMBERS (revenue / EBITDA / PBT / PAT, YoY & QoQ, Rs Cr)

| # | Line(s) | Metric | Period | Value (verbatim) | Flags |
|---|---------|--------|--------|-------------------|-------|
| FN1 | 77-78 | Revenue | YoY headline | "130.4% increase in revenues YoY" | RECONCILE_VS_FILING |
| FN2 | 77-78 | EBITDA | YoY headline | "199.7% increase in EBITDA YoY" | RECONCILE_VS_FILING |
| FN3 | 90 | Revenue from Operations | Q1 FY27 | "Rs. 360.7 Cr." | RECONCILE_VS_FILING |
| FN4 | 90-91 | Revenue from Operations | Q1 FY26 (comparator) | "Rs. 156.6 Cr." | RECONCILE_VS_FILING |
| FN5 | 91 | Revenue from Operations | YoY change | "130.4% increase YoY" | RECONCILE_VS_FILING |
| FN6 | 92 | EBITDA | Q1 FY27 | "Rs. 85.1 Cr." | RECONCILE_VS_FILING |
| FN7 | 92 | EBITDA | Q1 FY26 (comparator) | "Rs. 28.4 Cr." | RECONCILE_VS_FILING |
| FN8 | 93 | EBITDA | YoY change | "199.7% increase YoY" | RECONCILE_VS_FILING |
| FN9 | 94 | Profit Before Tax | Q1 FY27 | "Rs. 67.4 Cr." | RECONCILE_VS_FILING |
| FN10 | 94-95 | Profit Before Tax | Q1 FY26 (comparator) | "Rs. 14.8 Cr." | RECONCILE_VS_FILING |
| FN11 | 95 | Profit Before Tax | YoY change | "355.0% increase YoY" | RECONCILE_VS_FILING |
| FN12 | 96 | Profit After Tax | Q1 FY27 | "Rs. 50.2 Cr" | RECONCILE_VS_FILING |
| FN13 | 96-97 | Profit After Tax | Q1 FY26 (comparator) | "Rs. 10.8 Cr." | RECONCILE_VS_FILING |
| FN14 | 97 | Profit After Tax | YoY change | "364.5% increase YoY" | RECONCILE_VS_FILING |
| FN15 | 102 | Revenue from Operations | Q1 FY27 (QoQ restatement) | "Rs. 360.7 Cr." | RECONCILE_VS_FILING (must tie to FN3) |
| FN16 | 102-103 | Revenue from Operations | Q4 FY26 (comparator) | "Rs. 306.1 Cr." | RECONCILE_VS_FILING |
| FN17 | 103 | Revenue from Operations | QoQ change | "17.9% increase QoQ" | RECONCILE_VS_FILING |
| FN18 | 104 | EBITDA | Q1 FY27 (QoQ restatement) | "Rs. 85.1 Cr." | RECONCILE_VS_FILING (must tie to FN6) |
| FN19 | 104 | EBITDA | Q4 FY26 (comparator) | "Rs. 61.8 Cr." | RECONCILE_VS_FILING |
| FN20 | 105 | EBITDA | QoQ change | "37.6% increase QoQ" | RECONCILE_VS_FILING |
| FN21 | 106 | Profit Before Tax | Q1 FY27 (QoQ restatement) | "Rs. 67.4 Cr." | RECONCILE_VS_FILING (must tie to FN9) |
| FN22 | 106-107 | Profit Before Tax | Q4 FY26 (comparator) | "Rs. 59.5 Cr." | RECONCILE_VS_FILING |
| FN23 | 107 | Profit Before Tax | QoQ change | "13.2% increase QoQ" | RECONCILE_VS_FILING |
| FN24 | 108 | Profit After Tax | Q1 FY27 (QoQ restatement) | "Rs. 50.2 Cr" | RECONCILE_VS_FILING (must tie to FN12) |
| FN25 | 108 | Profit After Tax | Q4 FY26 (comparator) | "Rs. 44.3 Cr." | RECONCILE_VS_FILING |
| FN26 | 108-109 | Profit After Tax | QoQ change | "13.4% increase QoQ" | RECONCILE_VS_FILING |

Grep basis: `grep -o "Rs\."` on body (lines 15-143) = 16 occurrences; `grep -o "%"` on body = 10 occurrences (2 headline + 8 bullet-change). 16 + 10 = 26 = sweep count.

## TABLE 2 — SEGMENT / BUSINESS-VERTICAL CLAIMS

| # | Line(s) | Claim (verbatim / paraphrase kept literal) | Flags |
|---|---------|---------------------------------------------|-------|
| SG1 | 77 | "MTAR reports highest ever revenue in Q1 FY 27" | RECONCILE_VS_FILING (superlative claim — verify against historical quarterly revenue series) |
| SG2 | 80-81 | "a leading manufacturer engaged in manufacturing and development of mission critical precision engineered systems" | — |
| SG3 | 82-83 | "catering to Clean Energy – Civil Nuclear Power, Fuel Cells, Hydel & Others, Aerospace and Defence sectors" (page 2 body) | — |
| SG4 | 120-121 | "MTAR caters to Clean Energy – Civil Nuclear Power, Fuel Cells, Hydel & Others, Aerospace and Defence sectors" (page 4 "About" section) | DUPLICATE of SG3, same 5-sector list, no segment-wise revenue split given anywhere in this document |
| SG5 | 121-122 | "The Company has a long-standing relationship of over four decades with leading Indian Organizations and global OEMs" | — |

Grep basis: keyword anchors "Clean Energy" (2 hits: lines 82, 120), "highest ever" (1: line 77), "leading manufacturer" (1: line 80), "long-standing" (1: line 121) = 5 = sweep count.

Observation for A4: no segment-wise (Clean Energy / Civil Nuclear / Aerospace / Defence) revenue, order book, or margin figures are disclosed anywhere in this press release — only the qualitative sector list appears twice (SG3, SG4). No product-vs-project split and no export revenue figure are stated.

## TABLE 3 — OPERATIONAL METRICS

| # | Line(s) | Metric (verbatim) | Flags |
|---|---------|--------------------|-------|
| OM1 | 119 | "MTAR has sixteen strategically based manufacturing units including an export-oriented unit each based in Hyderabad, Telangana" | RECONCILE_VS_FILING (facility count — cross-check vs prior disclosures / annual report) |

Grep basis: "sixteen" = 1 hit (line 119) = sweep count. No order book/inflow, capacity (volume/units), capex, headcount, or numeric guidance figures found anywhere in the body (confirmed absent by targeted grep — see Absence observations above).

## TABLE 4 — MANAGING DIRECTOR COMMENTARY (Mr. Parvat Srinivas Reddy, page 3)

| # | Line(s) | Sentence (verbatim) | Flags |
|---|---------|----------------------|-------|
| MD1 | 112-113 | "We have delivered another strong quarter, with our quarterly performance remaining in line with the growth guidance provided for the current fiscal year." | FORWARD (references guidance for the current fiscal year; no guidance number itself is stated here) |
| MD2 | 113-114 | "Beyond the quarterly numbers, what is particularly encouraging is the direction in which the Company is progressing." | HEDGE (qualitative sentiment, no commitment or number) |
| MD3 | 114-116 | "We believe we are at an inflection point, with each of our key business verticals positioned for the next phase of growth." | FORWARD, HEDGE ("we believe"; "positioned for the next phase of growth" is a forward-looking, unquantified claim) |

Grep basis: 3 sentence-terminal periods inside the quoted block (lines 112-116, ending "...current fiscal year.", "...is progressing.", "...next phase of growth.”") = 3 = sweep count. Speaker attribution line ("Commenting on the results, Mr. Parvat Srinivas Reddy, Managing Director, MTAR Technologies, said,") is enumerated separately as AD13 in Table 6, since it is the article's framing, not the MD's own sentence.

## TABLE 5 — FOOTNOTES / DISCLAIMER / FORWARD-LOOKING-STATEMENTS PARAGRAPH (page 4)

| # | Line(s) | Text (verbatim) | Flags |
|---|---------|-------------------|-------|
| FD1 | 134 | "DISCLAIMER:" (section header) | — |
| FD2 | 138 | "Certain statements that are made in the Press Release may be forward-looking statements." | FORWARD |
| FD3 | 138-140 | "Such forward-looking statements are subject to certain risks and uncertainties like significant changes in economic environment in India and overseas, tax laws, inflation, litigation, etc." | FORWARD, HEDGE |
| FD4 | 140 | "Actual results might differ substantially from those expressed or implied." | HEDGE |
| FD5 | 140-144 | "MTAR Technologies Ltd. will not be in any way responsible for any action taken based on such statements and discussions; and undertakes no obligation to publicly update these forward-looking statements to reflect subsequent events or circumstances" | HEDGE |

Grep basis: `^DISCLAIMER` header (1) + 4 sentence-terminal periods within the disclaimer paragraph (lines 138-144) = 5 = sweep count.

## TABLE 6 — ADMINISTRATIVE / TRANSMITTAL ITEMS (cover letter to BSE/NSE, page 1; masthead & contacts, page 4)

Added under the base A2 rule to enumerate every discrete disclosure unit; not one of the five doctype-specific categories in the task brief but present in the source document and not otherwise covered.

| # | Line(s) | Item (verbatim / description) | Flags |
|---|---------|--------------------------------|-------|
| AD1 | 16 | Letter date: "Date: 29th July, 2026" | — |
| AD2 | 19-22 | Addressees: BSE Limited (Scrip Code 543270) and National Stock Exchange of India Limited (Symbol MTARTECH) | — |
| AD3 | 26-27 | Subject line: "Investors Press Release on the Un-audited financial results for the quarter ended 30.06.2026" | — |
| AD4 | 29 | "Unit: MTAR Technologies Limited" | — |
| AD5 | 30 | "ISIN: INE864I01014" | — |
| AD6 | 33-35 | Regulatory citation: "Pursuant to Regulation 30(6) of the SEBI (LODR) Regulations 2015" | — |
| AD7 | 37-38 | Website reference: "https://mtar.in/" | — |
| AD8a | 44-64 | Signatory identity block: Priyanka Agarwal, Company Secretary and Compliance Officer, digitally signed (DN detail incl. postal address, serial number) | — |
| AD8b | 65 | Signature timestamp: "Date: 2026.07.29 18:50:19 +05'30'" | — (no board-meeting time is disclosed in this press release to cross-check against, unlike the results-filing signature-timestamp check in the base ruleset; flag deferred to A1 results-filing ledger if one exists) |
| AD9 | 73 | "Encl: As above" | — |
| AD10 | 118 | "About" section masthead: "About MTAR Technologies Ltd (www.mtar.in) BSE: 543270; NSE: MTARTECH" | — |
| AD11 | 127-131 | Contact: Srilekha Jasthi, Head, Strategy & Investor Relations, MTAR Technologies Ltd, Tel: +91-040 4455 3333, srilekha@mtar.in | — |
| AD12 | 127-131 | Contact: Raju Reddy, Concept Public Relations, M: 9346076750, raju.m@conceptpr.com | — |
| AD13 | 111-112 | MD-quote attribution: "Commenting on the results, Mr. Parvat Srinivas Reddy, Managing Director, MTAR Technologies, said," | — |

Grep basis (re-swept after first-pass mismatch, see GATE A2 process note above): anchors `Date:`(x2: lines 16, 65), `BSE Limited`(1), `Sub:`(1), `Unit:    MTAR`(1), `ISIN:`(1), `Regulation 30`(1), `https://mtar\.in`(1), `Digitally signed by PRIYANKA`(1), `Encl:`(1), `About MTAR Technologies`(1), `Srilekha Jasthi`(1), `Raju Reddy`(1), `Commenting on the results`(1) = 14 = sweep count.

---

## LEDGER SUMMARY

- Total rows enumerated: 54 (26 financial numbers + 5 segment claims + 1 operational metric + 3 MD commentary sentences + 5 footnotes/disclaimer + 14 administrative items)
- ZERO_STANDING rows: 0 (no financial table with dash/nil-valued standing items exists in this narrative doctype — nothing to flag)
- All 26 financial-number rows carry RECONCILE_VS_FILING (this press release is the pre-cursor disclosure; every number must tie to the Reg 33 results filing / financial statements when that filing's A1/A2 ledger is built)
- FORWARD flags: MD1, MD3, FD2, FD3 (4 rows)
- HEDGE flags: MD2, MD3, FD3, FD4, FD5 (5 rows)
- No prior-quarter ledger was supplied (PRIOR_LEDGER_PATH: NONE) — DROPPED_SLIDE / prior-period diff checks are N/A for this run.
