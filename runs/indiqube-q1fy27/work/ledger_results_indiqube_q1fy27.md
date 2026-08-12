# A2 COMPLETENESS LEDGER — Results Filing
Company: IndiQube Spaces Limited (INDIQUBE)
Quarter: Q1FY27 (quarter ended 30 June 2026)
Doctype: results (Board Outcome letter + Walker Chandiok Limited Review Report + Statement of Unaudited Financial Results + Notes incl. Note 4 IPO-utilisation table + signature blocks)
Source: extract_results_indiqube_q1fy27.txt (285 lines, 5 pages, OCR, page_coverage 100%)
Prior-quarter ledger: NONE (first pipeline run for INDIQUBE — no prior-quarter diff possible; ENTITY_CHANGE / DROPPED_SLIDE style diffs not applicable this run)
Filing scope: **STANDALONE ONLY** — single entity (IndiQube Spaces Limited), single reportable segment (Note 5), no subsidiaries named, no consolidation list, no "Group"/consolidated statement anywhere in the extract.

```
=== A2 COUNT TEST ===
category: notes_numbered      grep_count: 6    sweep_count: 6    match: yes
category: notes_footnotes     grep_count: 4    sweep_count: 4    match: yes
category: line_items_stmt     grep_count: 29   sweep_count: 29   match: yes
category: line_items_ipo_tbl  grep_count: 8    sweep_count: 8    match: yes
category: agenda_items        grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras       grep_count: 4    sweep_count: 4    match: yes
category: signature_blocks    grep_count: 3    sweep_count: 3    match: yes
category: entities            grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep provenance (commands run against the extract, reconciled against manual line-by-line read of lines 1-285):
- Numbered notes: `awk 'NR>=208&&NR<=260' | grep -nE "^\s*[0-9I]+\s+[A-Za-z]"` → 6. NB the literal instructed pattern `^\s*[0-9]+\.\s` (period after number) does NOT match this filing's Notes section at all — it instead matches the *auditor report's* 4 numbered paragraphs (a different disclosure unit; see Table F). The Notes section uses "N␣␣␣text" with no period, and Note 1 is OCR-mis-rendered as Roman numeral "I" — caught only by manual sweep on first pass, confirmed by targeted regex on second pass. Both methods now agree at 6.
- Footnotes under Note 4 table: `awk 'NR>=224&&NR<=248' | grep -nE "^\s*(•|••|#|A)(\s|$)"` → 4. First-pass grep (requiring trailing whitespace) only caught 3; the "A" marker sits alone on line 245 with no trailing character, missed until pattern widened to allow end-of-line. Manual sweep caught all 4 on first pass. Reconciled at 4.
- Statement line items: `awk 'NR>=166&&NR<=199 && NF>0'` → 29 non-blank lines, all captured in Table C, one-for-one against manual read.
- IPO-utilisation table rows: `awk 'NR>=230&&NR<=239 && /[0-9]/'` → 8 (excludes two label-continuation lines with no digits, 232 and 236, which wrap the "Repayment/pre-payment" and "fit-out and interior" object names). Manual sweep independently resolved the same 8 distinct objects+total. Reconciled at 8.
- Agenda items: manual sweep of Board Outcome letter body (lines 16-54) plus grep for approval/dividend/AGM/ESOP/auditor/scrutinizer/postal-ballot vocabulary → only "considered and approved" appears once, tied to the single bundled item (results + Limited Review Report). No AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP grant, or capital-raising resolution language present. Reconciled at 1.
- Auditor paragraphs: `grep -cE "^[0-9]+\.\s"` → 4 (lines 89, 95, 103, 124). Reconciled at 4.
- Signature blocks: manual sweep — Bhasker Dubey (CS, lines 46-54), Lokesh Khemka (auditor partner, lines 134-146), Rishi Das (Chairman/ED/CEO, lines 261-285). Reconciled at 3.

---
## Table A — Numbered Notes (Statement of Financial Results, Notes section, page 5)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| Note 1 | 209 | "The unaudited financial results of the Company for the quarter ended 30 June 2026 have been reviewed..." | OCR_NOTE_NUMBER (rendered "I" not "1") |
| Note 2 | 211 | "These results have been prepared in accordance with the recognition and measurement principles laid down..." | |
| Note 3 | 215 | "The unaudited financial results includes the results for the quarter ended 31 March 2026 being the balancing figure..." | Q4FY26 column is a derived balancing figure (audited FY26 minus reviewed 9M-FY26), not a directly reviewed quarter — carries forward to Table C column note |
| Note 4 | 218 | "During the quarter ended 30 September 2025, the Company has completed the Initial Public Offering ('IPO') of 29,542,340..." | Header note for IPO-utilisation table, see Table D |
| Note 5 | 249 | "The Company primarily operates in a single reportable segment - leasing of managed commercial workspaces of equipped..." | SINGLE_SEGMENT — explicit statement no reportable segments per Ind AS 108 |
| Note 6 | 256 | "The results for the quarter ended 30 June 2026 are available on the National Stock Exchange of India Limited..." | Standard website-availability note |

## Table B — Footnotes under Note 4 IPO-Utilisation Table (page 5)

| Marker | Line(s) | Text (first 15 words) | Flags |
|--------|---------|------------------------|-------|
| • | 240 | "net of share issue expenses of Rs. 455.41 millions." | Qualifies "Utilisation Planned as per prospectus" column header |
| •• | 241-243 | "Pursuant to the Audit Committee's recommendation, the Board of Directors in their meeting held on 20 May 2026 approved seeking shareholders' approval..." | Discloses a SEPARATE board meeting (20 May 2026) approving postal-ballot process for IPO-objects revision, distinct from today's 12 Aug 2026 meeting; postal ballot special resolution passed 24 June 2026. Qualifies "Revised utilisation" column. IPO_OBJECTS_REVISED |
| # | 244 | "the above mentioned unutilised proceeds is temporarily held in deposits/accounts with scheduled banks." | Qualifies "Unutilised as at 30 June 2026" column |
| A | 245-248 | "Following the repayment of borrowings as outlined in the Offer Document, a balance of Rs. 16.95 million remains unutilised..." | Explains Rs 16.95mn reallocation from "Repayment of borrowings" object to "General corporate purposes" object; marks rows 231-232 and 233 in Table D |

## Table C — Statement of Unaudited Financial Results, all rows, all four periods (page 4)
Columns per header (lines 160-165): Col1 = Quarter ended 30 June 2026 [Q1FY27, Unaudited]; Col2 = Quarter ended 31 March 2026 [Q4FY26, Unaudited, Refer Note 3]; Col3 = Quarter ended 30 June 2025 [Q1FY26, Unaudited]; Col4 = Year ended 31 March 2026 [FY26, Audited]. Amounts in Rs. millions.

| Line | SI | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|----|-------------|--------|--------|--------|------|-------|
| 166 | 1 | Income (section header) | — | — | — | — | header row, no own value |
| 167 | | Revenue from operations | 4,226.85 | 4,014.47 | 3,092.93 | 14,508.12 | |
| 168 | | Other income | 261.29 | 242.66 | 148.32 | 767.07 | |
| 169 | | Total income | 4,488.14 | 4,257.13 | 3,241.25 | 15,275.19 | subtotal |
| 171 | 2 | Expenses (section header) | — | — | — | — | header row, no own value |
| 172 | | Purchases of traded goods | 276.61 | 256.31 | 100.53 | 963.10 | |
| 173 | | Changes in inventories of stock-in-trade | (2.38) | 4.68 | – | (6.92) | PARTIAL_DASH — Q1FY26 only is a dash; other three periods have values, so NOT a full ZERO_STANDING row, but the dash is a genuine template signal (company had zero inventory movement that one quarter) and is recorded, not dropped |
| 174 | | Employee benefits expense | 236.42 | 241.97 | 199.71 | 925.72 | |
| 175 | | Finance costs | 1,272.19 | 1,192.03 | 1,099.31 | 4,482.59 | |
| 176 | | Depreciation and amortisation expense | 1,878.93 | 1,770.25 | 1,429.84 | 6,454.29 | |
| 177 | | Other expenses | 1,131.47 | 1,030.84 | 911.49 | 3,812.87 | |
| 178 | | Total expenses | 4,793.24 | 4,496.08 | 3,740.88 | 16,631.65 | subtotal |
| 180 | 3 | Loss before tax for the period/year | (305.10) | (238.95) | (499.63) | (1,356.46) | OCR_CORRUPTION — source brackets rendered as `]` and `'` (e.g. "(305.10]", "(238.95'"); values transcribed here with sign intent preserved, flagged for A1/A3 re-verification against filed PDF |
| 181 | 4 | Tax expense/(credit) (section header) | — | — | — | — | header row |
| 182 | | – Current tax | 81.62 | 87.51 | 38.72 | 217.44 | |
| 183 | | – Deferred tax | (147.90) | (99.94) | (170.80) | (510.48) | |
| 184 | | Total tax expense | (66.28) | (12.43) | (132.08) | (293.04) | OCR_CORRUPTION — source shows "1132.08" (missing open paren/minus) and "(293.04'"; sign/value inferred from column arithmetic, flag for re-verification |
| 185 | 5 | Loss after tax for the period/year | (238.82) | (226.52) | (367.55) | (1,063.42) | OCR_CORRUPTION — source shows "1226.52" for Q4FY26, inferred as "(226.52)" from arithmetic continuity; flag for re-verification |
| 187 | 6 | Other comprehensive income/(loss) (section header) | — | — | — | — | header row |
| 188 | | "Items that will not be reclassified subsequently to profit or loss" (sub-header) | — | — | — | — | OCR_CORRUPTION on label text ("flems 1/wl wi/11101..."); structural sub-header, no own value |
| 189 | | Re-measurement gain/(loss) on defined benefit plans | 3.09 | 4.65 | (4.78) | 12.35 | |
| 190 | | Income tax effect on above | (0.78) | (1.17) | 1.20 | (3.11) | |
| 191 | | Total other comprehensive income/(loss), net of tax | 2.31 | 3.48 | (3.58) | 9.24 | subtotal; OCR_CORRUPTION on Q1FY26 value "(3.58'" |
| 193 | 7 | Total comprehensive loss for the period/year | (236.51) | (223.04) | (371.13) | (1,054.18) | OCR_CORRUPTION — source "1236.511", "(223.04\", "1371.13", "(1,054.181"; values inferred from arithmetic continuity (loss after tax + OCI), flag for re-verification against filed PDF |
| 195 | 8 | Paid-up equity share capital (face value Re. 1/share) | 211.99 | 211.99 | 182.58 | 211.99 | Q1FY26 (pre-IPO) lower than post-IPO periods — consistent with IPO share issuance in Q2FY26 per Note 4 |
| 196 | 9 | Other equity | (blank) | (blank) | (blank) | 4,935.50 | BLANK_STANDING — quarter columns are blank, not a printed zero/dash; standard treatment since Other Equity is a balance-sheet item conventionally reported only at year-end in an interim P&L statement. Distinguished from ZERO_STANDING (no zero/nil/dash glyph present) but recorded per "never drop a nil-appearing row" |
| 197 | 10 | Earnings per equity share in Rs. (not annualised for quarters) (header) | — | — | — | — | OCR_CORRUPTION — "10" rendered as "IO"; header row |
| 198 | | a) Basic | (1.13) | (1.07) | (2.01) | (5.28) | |
| 199 | | b) Diluted | (1.13) | (1.07) | (2.01) | (5.28) | Basic = Diluted every period — no dilutive instruments outstanding signal |

**Absent standard line items (no row exists at all, present in neither header nor data form):** no "Exceptional items" line, no "Discontinued operations" line, no "Profit/(loss) on sale of investment / subsidiary / stake" line anywhere between Total expenses (178) and Loss before tax (180), or elsewhere in the statement. This is a structural absence, not a printed zero — flagged `LINE_ITEM_TYPE_ABSENT` for A3/A4 to confirm against segment/related-party notes rather than assume immateriality.

## Table D — Note 4: IPO-Utilisation Table (page 5, lines 226-239)
Amount in Rs. millions unless stated. Columns: Planned per prospectus• | Revised utilisation•• | Utilised up to 30 June 2026 | Unutilised as at 30 June 2026#

| Line | Object | Planned | Revised | Utilised | Unutilised | Flags |
|------|--------|---------|---------|----------|------------|-------|
| 230 | Funding capital expenditure towards establishment of new centers | 4,626.49 | 2,756.49 | 1,276.28 | 1,480.21 | Planned amount cut nearly in half (4,626.49 → 2,756.49) to fund the four new objects added below |
| 231-232 | Repayment/pre-payment of certain borrowings availed by the Company (marker A) | 913.40 | 913.40 | 913.40 | (blank) | FULLY_UTILISED — blank Unutilised cell = nil remaining; Rs 16.95mn of this object's original planned/utilised balance was reallocated to General corporate purposes per footnote A |
| 233 | General corporate purposes (marker A) | 504.70 | 504.70 | 500.69 | 4.01 | Received the Rs 16.95mn reallocation described in footnote A |
| 234 | Funding security deposit for new centers | – | 520.00 | – | 520.00 | NEW_OBJECT_ADDED — nil in original prospectus (dash), added via 24 June 2026 postal ballot; fully unutilised as of 30 June 2026 |
| 235-236 | Funding capital expenditure towards fit-out and interior in non-IndiQube properties | – | 550.00 | – | 550.00 | NEW_OBJECT_ADDED — same as above, fully unutilised |
| 237 | Funding capital expenditure towards renewable power infrastructure | – | 160.00 | – | 160.00 | NEW_OBJECT_ADDED — fully unutilised |
| 238 | Capital deployment in strategic commercial real estate opportunities | – | 640.00 | – | 640.00 | NEW_OBJECT_ADDED — fully unutilised |
| 239 | Total | 6,044.59 | 6,044.59 | 2,690.37 | 3,354.22 | Utilised/Total = 44.5% of net IPO proceeds as at quarter-end; four newly-added objects (234, 235-236, 237, 238) total Rs 1,870mn revised allocation, 0% utilised to date — IPO_OBJECTS_REVISED, worth A4 attention on pace of deployment into these new objects |

## Table E — Board Outcome Letter: Agenda Items (page 1)

| Line | Item | Detail | Flags |
|------|------|--------|-------|
| 34-38 | Item 1 (only disclosed item) | Board considered and approved (a) unaudited financial results for quarter ended 30 June 2026, and (b) took on record the Limited Review Report with unmodified opinion from Statutory Auditors | Single bundled agenda item |
| 34-35 | Meeting timing | Commenced 04:03 PM (IST), concluded 04:16 PM (IST) — 13 minutes | SHORT_BOARD_MEETING (13 min) — no other agenda items to explain duration; consistent with a single-item results-approval meeting |

**No other agenda items disclosed** — no AR/annual report approval, no AGM notice or record date, no dividend declaration, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution. Flagged `SINGLE_AGENDA_ITEM` (completeness observation, not a defect — many results-only board meetings are single-item).

## Table F — Walker Chandiok & Co LLP Independent Auditor's Review Report (pages 2-3)

| Line | Paragraph | Content | Flags |
|------|-----------|---------|-------|
| 82-84 | Title | "Independent Auditor's Review Report on Unaudited Quarterly Financial Results...pursuant to Regulation 33..." | |
| 86-87 | Addressee | "To the Board of Directors of IndiQube Spaces Limited (formerly...)" | Single entity addressed — STANDALONE_ONLY |
| 89-93 | Para 1 | Introduction — statement reviewed for quarter ended 30 June 2026, pursuant to Reg 33 | Entity reviewed: IndiQube Spaces Limited only, no subsidiaries/JVs/associates named |
| 95-101 | Para 2 | Management/Board responsibility; Ind AS 34 basis of preparation; auditor's responsibility to express a conclusion | |
| 103-111 | Para 3 | Scope — SRE 2410 review standard; explicitly states review is "substantially less in scope than an audit" and "we do not express an audit opinion" | Standard scope-limitation language, not a qualification |
| 124-129 | Para 4 (Conclusion/Opinion) | "nothing has come to our attention that causes us to believe that the accompanying Statement...has not disclosed the information required...or that it contains any material misstatement" | **Opinion type: UNMODIFIED / UNQUALIFIED review conclusion** |
| — | Emphasis of Matter | **ABSENT** — no EoM paragraph anywhere in report | Explicitly confirmed absent (grep for "emphasis of matter": zero hits) |
| — | Other Matters | **ABSENT** — no Other Matters paragraph | Explicitly confirmed absent (grep for "other matter": zero hits) |
| — | Going Concern | **ABSENT** — no going-concern language, qualification, or material uncertainty note | Explicitly confirmed absent (grep for "going concern": zero hits) |
| — | Entities reviewed | IndiQube Spaces Limited (standalone) only | No "subsidiary"/"consolidat" text anywhere in extract — confirms STANDALONE_ONLY, no unaudited/management-furnished component entities to flag |
| 134-136 | Signature block header | "For Walker Chandiok & Co LLP, Chartered Accountants, Firm Registration No: 001076N/N500013" | |
| 140-143 | Signatory | Lokesh Khemka, Partner, Membership No. 067878, **UDIN: 26067878FTHRZP6916** | UDIN present and well-formed (16 characters, matches membership no. prefix pattern) |
| 145-146 | Place/Date | Bengaluru, 12 August 2026 | Same date as board meeting — auditor sign-off same day as approval, expected for a same-day review-and-approve cycle |
| 151 | Footer repeat "Chartered Accountants" | Letterhead page-break artifact | Not a substantive paragraph, noted for completeness only |

## Table G — Single Segment Note (page 5, Note 5) — cross-reference to Table A

| Line | Content | Flags |
|------|---------|-------|
| 249-250 | "The Company primarily operates in a single reportable segment - leasing of managed commercial workspaces of equipped premises. Accordingly, there are no reportable segments as per Ind AS 108." | SINGLE_SEGMENT confirmed; no segment-wise revenue/profit/asset table present or required |

## Table H — Entities / Consolidation Scope

| Line(s) | Entity | Relationship | Flags |
|---------|--------|--------------|-------|
| 59, 86-87, 153 | IndiQube Spaces Limited (formerly IndiQube Spaces Private Limited, Innovent Spaces Private Limited) | Sole reporting entity | STANDALONE_ONLY — no subsidiaries, associates, JVs, or "Group"/consolidated statement named or implied anywhere in the 285-line extract. No prior-quarter entity list exists to diff against (PRIOR_LEDGER_PATH = NONE), so `ENTITY_CHANGE` is not applicable this run but should be the first check the next quarter's A2 runs against this ledger. |

## Table I — Digital Signature Blocks

| Line(s) | Signatory | Designation | Timestamp | Flags |
|---------|-----------|-------------|-----------|-------|
| 46-54 | Bhasker Dubey | Company Secretary & Compliance Officer | Digitally signed, 2026.08.12 17:04:18 +05'30' (5:04:18 PM IST) | Signed ~48 minutes AFTER board meeting concluded (04:16 PM) — expected/normal sequencing (letter drafted and filed after meeting closes), not a flag of concern, recorded per instruction to check signature-vs-meeting-time relationship |
| 134-146 | Lokesh Khemka | Partner, Walker Chandiok & Co LLP | Bengaluru, 12 August 2026 (no intraday timestamp captured in OCR) | UDIN 26067878FTHRZP6916 present; no HH:MM timestamp on the auditor's report itself (normal — audit reports typically carry date only, not time) |
| 261-285 | Rishi Das | Chairman, Executive Director and Chief Executive Officer, DIN: 00420103 | Place: Bengaluru (OCR-garbled "13cngalt1m"), 12 August 2026; signature block appears to be a scanned/graphic seal (lines 262-283 render as OCR artifacts, not machine-readable digital-signature metadata) | ABSENT_TIMESTAMP — unlike Bhasker Dubey's block, no digital-signature date/time metadata was extracted for Rishi Das's signature on the Statement itself; likely a wet/image signature rather than a PKI digital signature. Worth a source-PDF re-check by A1/A3 to confirm whether timestamp metadata exists in the original file and was simply not OCR-captured. |

---
## Additional completeness observations (not separately numbered rows, carried for A3/A4)
- Q4FY26 column throughout Table C is NOT an independently reviewed quarter — it is a balancing figure (audited FY26 less reviewed 9M-FY26) per Note 3 (line 215). Any quarter-over-quarter arithmetic A4 performs using the Q4FY26 column should carry this caveat.
- OCR_CORRUPTION affects bracket/sign rendering on 6 of the 29 statement rows (180, 184, 185, 191, 193, and label text on 188/197). Values in Table C reflect the pipeline's best-effort sign inference from column arithmetic (income - expenses = loss before tax; loss before tax - tax = loss after tax; loss after tax + OCI = total comprehensive loss) and are flagged for A1/A3 to re-verify against the source PDF directly rather than the OCR text layer.
- No annexures, no director-profile tables, no AGM/scrutinizer/ESOP disclosures present in this results filing package — filing is limited to Board Outcome letter + auditor's review report + Statement + Notes. Flagged `ANNEXURE_ABSENT` / `DIRECTOR_PROFILES_ABSENT` so A3/A4 do not search for content that isn't in this doctype's scope this quarter.
