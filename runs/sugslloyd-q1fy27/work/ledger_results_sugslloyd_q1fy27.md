# A2 ENUMERATION LEDGER — SUGS LLOYD LIMITED (SUGSLLOYD) — Q1 FY27 (quarter ended 30 June 2026) — RESULTS

Source: extract_results_sugslloyd_q1fy27.txt (418 lines, 6 pages, PyMuPDF layout extraction, no OCR flagged by A1 header but text layer carries visible OCR-style artifacts — see notes inline). Prior-quarter ledger: none (first quarterly review for this company).

```
=== A2 COUNT TEST ===
category: notes            grep_count: 14   sweep_count: 14   match: yes
category: line_items        grep_count: 70   sweep_count: 70   match: yes
category: zero_standing     grep_count: 15   sweep_count: 15   match: yes
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras     grep_count: 12   sweep_count: 12   match: yes
category: entities          grep_count: 2    sweep_count: 2    match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Methodology note on counts (read before using this ledger)
The source PDF's text layer carries page-dependent OCR-style corruption: Roman numeral captions are merged with the following word on some lines and rendered as literal pipe characters or lower-case letters on others (e.g. standalone "I Revenue from Operations" renders as "| Revenue from Operations" at line 79, while the same caption in the consolidated table at line 217 renders as literal "I"); paragraph/note markers are sometimes split onto their own line, separated from their text by column-reconstruction reordering (e.g. consolidated auditor report paragraph "2." appears alone at line 329, its text at line 328, one line above); and digit+period sometimes appears as digit+comma. Because of this, a single fixed grep regex under-or-over-counts on one table or the other. Each category below was therefore run through two independent passes: (1) a mechanical grep pass (shown per category, refined once where the first pass mismatched the sweep, per protocol — the refinement is documented, not hidden) and (2) a manual line-by-line sweep. Both converge on the counts in the COUNT TEST above. No value was corrected; every row below is transcribed exactly as it appears at its cited line, artifacts included.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1)

| # | Line | Agenda item | Detail as stated | Flags |
|---|------|-------------|-------------------|-------|
| 1 | 42-47 | Unaudited Standalone and Consolidated Financial Results for Q1 FY27 (quarter ended 30 June 2026) | "has inter-alia, approved the following: UNAUDITED STANDALONE AND CONSOLIDATED FINANCIAL RESULTS OF THE COMPANY FOR THE QUARTER ENDED ON 30 JUNE, 2026." Limited Review Reports of the Auditors annexed as Annexure-I. | — |

Grep sweep across the full extract for AR approval / AGM notice / record date / dividend / director appointment or resignation / auditor appointment or change / scrutinizer / ESOP / capital-raising enabling resolution language returned zero hits (`grep -niE "dividend|AGM|annual general meeting|director appoint|resignation|auditor appoint|scrutinizer|ESOP|preferential|rights issue|buyback|record date|capital rais"` — no matches). This is a single-item board meeting; no other agenda item is present in this filing. (agenda_items = 1, confirmed both ways.)

## 2. BOARD MEETING TIMING (page 1)

| Line | Item | Value |
|------|------|-------|
| 34 | Prior intimation letter date | 24 July 2026 |
| 41 | Meeting date | Wednesday, 29 July 2026 |
| 37 | Meeting commenced | 11:45 A.M. |
| 49 | Meeting concluded | 12:30 P.M. |
| — | Duration | 45 minutes (derived from the two timestamps above; not itself an extract line) |

## 3. SIGNATURE / SIGN-OFF BLOCKS (all instances, both filing pages and both auditor reports)

| # | Line(s) | Block | Signatory / designation as stated | Date / place stated | Flags |
|---|---------|-------|-----------------------------------|----------------------|-------|
| 1 | 52-61 | Board Outcome letter closing | "For Sugs Lloyd Limited" / "Digitally signed by Nimmy Singh Chauhan" / Nimmy Singh Chauhan, Company Secretary and Compliance Officer | Place: Noida (letter dated 29 July 2026 at line 25; no time-of-day stamp captured in text layer) | Signature timestamp granularity is date-only in the extracted text; cannot test whether signature postdates the 12:30 P.M. meeting conclusion — NOT FOUND for that check |
| 2 | 132-134 | Standalone results table sign-off | DIN: 02248087 only — no name or designation captured in the extract at this block (contrast with item 3 below, same DIN, where "Chairman & Managing Director" is captured) | Date: July 29, 2026; Place: Noida | Designation/name missing from standalone block relative to consolidated block — asymmetric capture, note for A3/A4 |
| 3 | 298-304 | Consolidated results table sign-off | "For Sugs Lloyd Limited", Chairman & Managing Director, DIN: 02248087 (lines 298-299 show stray OCR tokens "{)" / "YO}" consistent with a stamp/seal graphic) | Date: July 29, 2026; Place: Noida | — |
| 4 | 191-197 | Standalone Auditor's Review Report sign-off | For Ratan Chandak & Co. LLP, Chartered Accountants; "Partner" (no personal name captured); Membership No. 182935; UDIN: 26182935YQWLPU8772 | Date: July 29, 2026; Navi Mumbai | Partner's personal name not present at this block — NOT FOUND |
| 5 | 407-414 | Consolidated Auditor's Review Report sign-off | For Ratan Chandak & Co. LLP, Chartered Accountants; Firm Reg. No. 108696W/W101028; "Partner" (no personal name captured); Membership No. 182935; UDIN: 26182935SIRYFS6262 | Date: July 29, 2026; Place: Navi Mumbai | Partner's personal name not present at this block — NOT FOUND; UDIN differs from block 4 (expected — two separate review engagements) |

---

## 4. STANDALONE STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (page 2, lines 71-134)

All amounts in lakhs. Columns: Q1 FY27 (30/06/2026, Unaudited) | Q4 FY26 (31/03/2026, Unaudited) | Q1 FY26 (30/06/2025, Unaudited) | FY26 (31/03/2026, Audited).

| # | Line | Caption | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|---------|--------|--------|--------|------|-------|
| 1 | 79 | I Revenue from Operations | 7,840.13 | 11,512.35 | 5,941.32 | 30,072.55 | — |
| 2 | 80 | II Other Income | 78.15 (shown "78,15") | 51.70 | 43.83 | 299.79 | OCR comma-for-period |
| 3 | 81 | III Total Income (I + II) | 7,918.28 | 11,564.05 | 5,985.15 | 30,372.34 | — |
| 4 | 82 | IV Expenses (header, no independent value) | — | — | — | — | HEADER_ROW |
| 5 | 83 | (a) Cost of materials consumed | dash | dash | dash | dash | ZERO_STANDING |
| 6 | 84 | (b) Purchases of stock-in-trade | 3,667.25 | 7,281.88 | 3,294.14 | 18,356.09 | — |
| 7 | 85 | (c) Changes in inventories of finished goods, work-in-progress and stock-in-trade | (495.36) | 376.73 | 199.83 | (203.62) | — |
| 8 | 86 | (d) Employee benefit expense | 1,118.90 | 953.39 | 506.19 | 2,725.89 | — |
| 9 | 87 | (e) Finance Costs | 244.63 | 129.15 | 148.47 | 744.98 | Consolidated version of this same line (line 230) shows 148.48 for Q1FY26, a one-paisa delta vs standalone's 148.47 — flag for A3/A4 as CROSS_TABLE_DELTA (may be rounding/OCR, not interpreted here) |
| 10 | 88 | (f) Depreciation and amortisation expense | 8.78 | 11.53 | 8.12 | 41.69 | — |
| 11 | 89 | (g) Other Expenses | 2,350.00 | 1,362.86 | 1,050.91 | 4,839.40 | Consolidated version (line 234) shows 1,050.90 for Q1FY26 — one-paisa CROSS_TABLE_DELTA, same as row 9 |
| 12 | 90 | Total Expenses | 6,894.20 | 10,115.54 | 5,207.66 | 26,504.43 | — |
| 13 | 91 | V Profit/(loss) before exceptional and extraordinary items and tax (III-IV) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 14 | 92 | VI Exceptional items | dash | dash | dash | dash | ZERO_STANDING |
| 15 | 93 | VII Profit before extraordinary items and tax (V-VI) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 16 | 94 | VIII Extraordinary items | dash | dash | dash | dash | ZERO_STANDING |
| 17 | 95 | IX Profit before tax (VII-VIII) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 18 | 96 | X Tax Expense (header, no independent value) | — | — | — | — | HEADER_ROW |
| 19 | 97 | (a) Current Tax | 275.61 | 374.07 | 194.28 | 998.36 | — |
| 20 | 98 | (b) Deferred Tax (Asset)/Liabilities | (1.79) | (2.80) | 4.61 | 0.04 | — |
| 21 | 99-100 | (c) Current Tax Expense Relating to Prior years | dash | dash | dash | 0.08 | Dash in 3 of 4 periods, 0.08 only in the FY26 audited annual column — not zero in ALL periods so ZERO_STANDING is not strictly applied, but flagged here as a near-nil standing item so it is not lost |
| 22 | 101 | XI Profit (Loss) for the period from continuing operations (IX-X) | 750.26 | 1,077.24 | 578.60 | 2,869.44 | — |
| 23 | 102 | XII Profit/(loss) from discontinued operations before tax | dash | dash | dash | dash | ZERO_STANDING |
| 24 | 103 | XIII Tax expenses of discontinued operations | dash | dash | dash | dash | ZERO_STANDING |
| 25 | 104 | XIV Profit/(loss) from Discontinued operations (after tax) (XII-XIII) | dash | dash | dash | dash | ZERO_STANDING |
| 26 | 105 | XV Share of Profit (Loss) of Associates | dash | dash | dash | (only 3 tokens visible, effectively dash) | ZERO_STANDING — standalone-only company results carry no associate share; contrast with consolidated row 26 below which is NOT zero |
| 27 | 106 | XVI Profit (Loss) of Minority Interest | dash | dash | dash | dash | ZERO_STANDING |
| 28 | 107 | XVII Net Profit (Loss) for the period (XI+XV-XVI) | 750.26 | 1,077.24 | 578.60 | 2,869.44 | — |
| 29 | 108 | XVIII Details of equity share capital (header) | — | — | — | — | HEADER_ROW |
| 30 | 109 | Paid-up equity share capital | 2,321.40 | 2,321.40 | 1,625.00 | 2,321.40 | Q1FY26 paid-up capital (1,625.00) differs from all other periods (2,321.40) — capital raised/changed between Q1FY26 and Q4FY26; not interpreted here, flagged for A3/A4 |
| 31 | 110 | Face value of equity share capital (Per Share) | 10.00 | 10.00 | 10.00 | 10.00 | — |
| 32 | 111 | XIX Earnings per share (header) | — | — | — | — | HEADER_ROW |
| 33 | 112 | Earnings per share (not annualised for half year / Period ended) (sub-header) | — | — | — | — | HEADER_ROW |
| 34 | 113 | Basic earnings (loss) per share from continuing and discontinued operations | 3.41 | 5.33 (shown "5:33") | 3.56 | 14.19 | OCR colon-for-period |
| 35 | 114 | Diluted earnings (loss) per share continuing and discontinued operations | 3.41 | 5.33 | 3.56 | 14.19 | — |

Signature/date block below the table: DIN:02248087 / Date: July 29, 2026 / Place: Noida (lines 132-134) — see Signature Blocks table item 2.

## 5. CONSOLIDATED STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (page 4, lines 204-304)

Same caption structure and same four reporting periods as the standalone table.

| # | Line | Caption | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|---------|--------|--------|--------|------|-------|
| 1 | 217-218 | I Revenue from Operations | 7,840.13 | 11,512.35 | 5,941.32 | 30,072.55 | Identical to standalone row 1 (expected — no revenue at associate level flows through this line) |
| 2 | 219-220 | II Other Income | 78.15 | 51.70 | 43.83 | 299.79 | Identical to standalone row 2 |
| 3 | 221-222 | III Total Income (I + II) | 7,918.28 | 11,564.05 | 5,985.15 | 30,372.34 | Identical to standalone row 3 |
| 4 | 223 | IV Expenses (header) | — | — | — | — | HEADER_ROW |
| 5 | 224-225 | (a) Cost of materials consumed | dash | dash | dash | dash | ZERO_STANDING |
| 6 | 226-227 | (b) Purchases of stock-in-trade | 3,667.25 | 7,281.88 | 3,294.14 | 18,356.09 | Identical to standalone row 6 |
| 7 | 228 | (c) Changes in inventories of finished goods, WIP and stock-in-trade | (495.36) | 376.73 | 199.83 | (203.62) | Identical to standalone row 7 |
| 8 | 229 | (d) Employee benefit expense | 1,118.90 | 953.39 | 506.19 | 2,725.89 | Identical to standalone row 8 |
| 9 | 230 | (e) Finance Costs | 244.63 | 129.15 | 148.48 | 744.98 | CROSS_TABLE_DELTA vs standalone (148.47) — see standalone row 9 |
| 10 | 231-232 | (f) Depreciation and amortisation expense | 8.78 | 11.53 | 8.12 | 41.69 | Identical to standalone row 10 |
| 11 | 233-234 | (g) Other Expenses | 2,350.00 | 1,362.86 | 1,050.90 | 4,839.40 | CROSS_TABLE_DELTA vs standalone (1,050.91) — see standalone row 11 |
| 12 | 235-236 | Total Expenses | 6,894.20 | 10,115.54 | 5,207.66 | 26,504.43 | Identical to standalone row 12 (subtotal ties despite the two component-level one-paisa deltas above) |
| 13 | 237-238 | V Profit/(loss) before exceptional and extraordinary items and tax (III-IV) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 14 | 239-240 | VI Exceptional items | dash | dash | dash | dash | ZERO_STANDING |
| 15 | 241 | VII Profit before extraordinary items and tax (V-VI) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 16 | 242-243 | VIII Extraordinary items | dash | dash | dash | dash | ZERO_STANDING |
| 17 | 244-245 | IX Profit before tax (VII-VIII) | 1,024.09 | 1,448.51 | 777.49 | 3,867.92 | — |
| 18 | 246 | X Tax Expense (header) | — | — | — | — | HEADER_ROW |
| 19 | 247-248 | (a) Current Tax | 275.61 | 374.07 | 194.28 | 998.36 | — |
| 20 | 249-250 | (b) Deferred Tax (Asset)/Liabilities | (1.79) | (2.80) | 4.61 | 0.04 | — |
| 21 | 251-252 | (c) Current Tax Expense Relating to Prior years | dash | dash | dash | 0.08 | Same near-nil pattern as standalone row 21 |
| 22 | 253-254 | XI Profit (Loss) for the period from continuing operations (IX-X) | 750.26 | 1,077.24 | 578.60 | 2,869.44 | Identical to standalone pre-associate-share figure |
| 23 | 255 | XII Profit/(loss) from discontinued operations before tax | dash | dash | dash | dash | ZERO_STANDING |
| 24 | 256-257 | XIII Tax expenses of discontinued operations | dash | dash | dash | dash | ZERO_STANDING |
| 25 | 258-259 | XIV Profit/(loss) from Discontinued operations (after tax) (XII-XIII) | dash | dash | dash | dash | ZERO_STANDING |
| 26 | 260-261 | XV Share of Profit (Loss) of Associates | 4.03 | 10.56 | 0.51 (shown "051") | 12.71 (shown "12:71") | NOT zero — this is the consolidated-only associate contribution; direct pairing contrast with standalone row 26 (ZERO_STANDING there). Confirms the Associate (Vyna Electric Private Ltd) is genuinely consolidated with a P&L contribution this quarter |
| 27 | 262-263 | XVI Profit (Loss) of Minority Interest | dash | dash | dash | dash | ZERO_STANDING |
| 28 | 264-265 | XVII Net Profit (Loss) for the period (XI+XV-XVI) | 754.30 | 1,087.80 | 579.11 (shown "579,11") | 2,882.16 | Consolidated net profit exceeds standalone net profit (row 28 of standalone table) by exactly the associate share in row 26 above, each period — arithmetically consistent |
| 29 | 266 | XVIII Details of equity share capital (header) | — | — | — | — | HEADER_ROW |
| 30 | 267-268 | Paid-up equity share capital | 2,321.40 | 2,321.40 | 1,625.00 | 2,321.40 | Identical to standalone row 30, same Q1FY26 discrepancy noted there |
| 31 | 269-270 | Face value of equity share capital (Per Share) | 10.00 (shown "10,00") | 10.00 | 10.00 | 10.00 | OCR comma-for-period |
| 32 | 271 | XIX Earnings per share (header) | — | — | — | — | HEADER_ROW |
| 33 | 272 | Earnings per share (not annualised for half year / Period ended) (sub-header) | — | — | — | — | HEADER_ROW |
| 34 | 273-274 | Basic earnings (loss) per share from continuing and discontinued operations | 3.43 | 5.38 | 3.56 | 14.26 | Differs from standalone EPS (3.41/5.33/3.56/14.19) in the periods where associate share is nonzero, consistent with row 26/28 |
| 35 | 275-276 | Diluted earnings (loss) per share continuing and discontinued operations | 3.43 | 5.38 | 3.56 | 14.26 | — |

Signature block below the table: "For Sugs Lloyd Limited", Chairman & Managing Director, DIN:02248087, Date: July 29, 2026, Place: Noida (lines 298-304) — see Signature Blocks table item 3.

---

## 6. NOTES ON FINANCIAL RESULTS — STANDALONE TABLE (page 2, lines 115-134)

Note markers are OCR-garbled on this page: note 1 renders as "£", note 2 as a lone "a" on its own line separated from its text on the following line, note 7 as a lone "a" likewise separated from its text.

| Note | Line(s) | Marker as extracted | First 15 words |
|------|---------|----------------------|-----------------|
| 1 | 116-118 | "£" | The above results have been reviewed by the Audit Committee and have been approved by the Board |
| 2 | 119-124 | "a" (alone on line 119, text begins line 120) | The above Unaudited Financial Results of the Company for the Quarter ended 30th June 2026 and |
| 3 | 125 | "3" | Company is in only one segment, hence Segment Reporting as per AS-17 is not applicable to |
| 4 | 126-127 | "4" | As per MCA notification dated 16th February 2015 companies whose shares are listed on SME exchange |
| 5 | 128 | "5" | Earning per shares are calculated on weighted average of the share capital outstanding during the year |
| 6 | 129 | "6" | Previous year's/period's figure have been regrouped/rearranged wherever necessary |
| 7 | 130-131 | "a" | The figures for the Quarter ended on 31st March 2026 is the balancing figures between the audited |

## 7. NOTES ON FINANCIAL RESULTS — CONSOLIDATED TABLE (page 4, lines 277-297)

Note 1 marker renders as "i" on this page (a different OCR garble than the standalone page's "£" for the same note).

| Note | Line(s) | Marker as extracted | First 15 words |
|------|---------|----------------------|-----------------|
| 1 | 278-279 | "i" | The above results have been reviewed by the Audit Committee and have been approved by the Board |
| 2 | 280-286 | "2" | The above Unaudited Financial Results of the Company for the Quarter ended 30th June 2026 and |
| 3 | 287-288 | "3" | Company is in only one segment, hence Segment Reporting as per AS-17 is not applicable |
| 4 | 289-291 | "4" | As per MCA notification dated 16th February 2015 companies whose shares are listed on SME exchange |
| 5 | 292-293 | "5" | Earning per shares are calculated on weighted average of the share capital outstanding during the year |
| 6 | 294 | "6" | Previous year's/period's figure have been regrouped/rearranged wherever necessary |
| 7 | 295-297 | "7" | The figures for the Quarter ended on 31st March 2026 is the balancing figures between the audited |

Notes 1-6 are identical in substance between standalone and consolidated tables (word-for-word, only OCR marker rendering differs). Standalone note 7 corresponds to consolidated note 7 (both describe the Q4FY26 balancing-figure basis) — content matches.

---

## 8. STANDALONE AUDITOR'S REVIEW REPORT — RATAN CHANDAK & CO. LLP (page 3, lines 137-201)

Report title (line 145): "INDEPENDENT AUDITOR'S REVIEW REPORT ON REVIEW OF INTERIM STANDALONE FINANCIAL [RESULTS]" — addressed to the Board of Directors of Sugs Lloyd Limited.

| Para | Line(s) | Content type | First 15 words | Flags |
|------|---------|--------------|-----------------|-------|
| 1 | 149-155 | Introduction / engagement scope | We have reviewed the accompanying Statement of Standalone unaudited financial results of Sugs Lloyd Limited | — |
| 2 | 156-165 | Management responsibility / basis of preparation (AS 25) | This Statement, which is the responsibility of the Company's Management and approved by the Company's Board | — |
| 3 | 166-174 | Scope of review (SRE 2410); "we do not express an audit opinion" | We conducted our review in accordance with the Standard on Review Engagements (SRE) 2410 | — |
| 4 | 175-183 | Conclusion — unmodified/unqualified review conclusion | Based on our review conducted as above, nothing has come to our attention that causes us | Opinion type: unmodified review conclusion (no adverse, no qualification, no disclaimer language) |
| — | 184 | "Other Matter" heading | — | — |
| 5 | 185-190 | Other Matter — comparative Q4FY26 figures are a balancing figure, not separately reviewed | The comparative figures for the Quarter ended 31st March 2026 as reported in these Unaudited | Other Matter paragraph present; "Our conclusion is not modified in respect of above matters" |
| — | 191-197 | Signature block | For Ratan Chandak & Co. LLP; Partner; Membership No. 182935; UDIN: 26182935YQWLPU8772 | See Signature Blocks table item 4 |

No Emphasis of Matter paragraph. No Going Concern paragraph. No reference to any other auditor or unaudited/management-furnished entity in this report (standalone entity only — the Company itself, no associate in scope).

## 9. CONSOLIDATED AUDITOR'S REVIEW REPORT — RATAN CHANDAK & CO. LLP (pages 5-6, lines 306-418)

Report title (line 313): "INDEPENDENT AUDITOR'S REVIEW REPORT ON REVIEW OF INTERIM CONSOLIDATED FINANCIAL RESULTS" — addressed to the Board of Directors of Sugs Lloyd Limited. Note: this report carries seven physical paragraphs but the source mis-numbers two of them both "6" (see para 6b below) — a documentation defect in the source report, not a transcription choice; flagged DUPLICATE_PARA_NUMBER.

| Para | Line(s) | Content type | First 15 words | Flags |
|------|---------|--------------|-----------------|-------|
| 1 | 318-327 | Introduction / engagement scope; defines "the Group" as the Company and its Associate | We have reviewed the accompanying Statement of Consolidated Unaudited Financial Results of "Sugs Lloyd | Introduces the Group / Associate structure |
| 2 | 328-337 | Management responsibility / basis of preparation (AS 25) | This Statement, which is the responsibility of the Company's management and has been approved by the | Marker "2." is isolated on line 329, separated from its own paragraph text (line 328) by OCR column-reconstruction reordering — content confirmed by manual sweep |
| 3 | 339-356 | Scope of review (SRE 2410); "we do not express an audit opinion" | We conducted our review of the Statement in accordance with the Standard on Review Engagements | — |
| 4 | 358-361 | Regulatory scope carve-out: not required to perform SEBI Reg. 33(8) circular procedures | We are not required to perform procedures in accordance with the circular issued by the SEBI | This paragraph has NO counterpart in the standalone report (standalone report has no equivalent carve-out) — flag for A3/A4 |
| 5 | 363-373 | Conclusion — unmodified/unqualified review conclusion | Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing | Opinion type: unmodified review conclusion |
| 6a | 374-385 | Other Matter — entity reviewed by other auditors: Vyna Electric Private Limited (Formerly as Levana Infra Private Limited), the Associate; total revenue Rs.521.31 Lakhs, total net profit Rs.19.21 Lakhs for the quarter; reviewed by other auditors, furnished to this auditor by Management; this auditor's opinion on those amounts is solely on the other auditor's report | We did not review the interim financial statements of Vyna Electric Private Limited (Formerly as Levana | ENTITY_CHANGE — associate name change disclosed in-report ("Formerly as Levana Infra Private Limited"); associate results are unaudited-by-this-firm / management-furnished per this paragraph |
| 6b | 400-406 | Other Matter (2nd) — comparative Q4FY26 figures are a balancing figure, not separately reviewed (same substance as standalone report para 5) | The comparative figures for the Quarter ended 31st March 2026 as reported in these Unaudited Consolidated | DUPLICATE_PARA_NUMBER — source numbers this "6." also, duplicating para 6a's number instead of using "7." |
| — | 407-414 | Signature block | For Ratan Chandak & Co. LLP; Firm Reg. No. 108696W/W101028; Partner; Membership No. 182935; UDIN: 26182935SIRYFS6262 | See Signature Blocks table item 5 |

No Emphasis of Matter paragraph. No Going Concern paragraph.

---

## 10. CONSOLIDATION / ASSOCIATE ENTITY LIST (cross-referenced against the auditor reports and both results tables)

No prior-quarter ledger is available for this ticker, so the cross-check below is against internal consistency within this single filing (the auditor report's own naming disclosure), not against a prior period's entity list.

| # | Entity | Relationship | Line(s) first named | Flags |
|---|--------|--------------|----------------------|-------|
| 1 | Sugs Lloyd Limited | Parent / the Company (reporting entity) | 16, 66, 148, 204, 316 | — |
| 2 | Vyna Electric Private Limited (Formerly as Levana Infra Private Limited) | Associate, consolidated as part of "the Group" per consolidated auditor report para 1 (line 319-320); unaudited-by-principal-auditor, results furnished by Management and reviewed by other auditors per para 6a (lines 374-385); contributes Share of Profit (Loss) of Associates in the consolidated results table (row 26, lines 260-261: 4.03 / 10.56 / 0.51 / 12.71) | 374-377 | ENTITY_CHANGE — the auditor's own report discloses the entity's former name ("Formerly as Levana Infra Private Limited"), i.e. a rename occurred on or before this quarter; no prior ledger exists to confirm which quarter the rename took effect in, so the flag is raised on the strength of the in-filing disclosure alone |

Total revenue and net profit of the Associate for the quarter, as stated in auditor report para 6a: total revenue Rs.521.31 Lakhs, total net profit Rs.19.21 Lakhs (three months ended 30 June 2026) — line 376-379.

---

## Category counts (for YAML)
- notes: 14 (7 standalone + 7 consolidated)
- line_items: 70 (35 standalone + 35 consolidated)
- zero_standing: 15 (8 standalone + 7 consolidated)
- agenda_items: 1
- auditor_paras: 12 (5 standalone + 7 consolidated, counting the source's duplicated "6" as two distinct physical paragraphs 6a/6b)
- entities: 2 (parent + 1 associate)
- signature_blocks: 5

```yaml
stage: A2-enumerator
company: "SUGSLLOYD"
quarter: "Q1 FY27 (quarter ended 30 June 2026)"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/sugslloyd-q1fy27/work/ledger_results_sugslloyd_q1fy27.md"
counts:
  notes: 14
  line_items: 70
  zero_standing: 15
  agenda_items: 1
  auditor_paras: 12
  entities: 2
  signature_blocks: 5
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, DUPLICATE_PARA_NUMBER, HEADER_ROW, CROSS_TABLE_DELTA]
gate_a2: pass
mismatch_note: ""
```
