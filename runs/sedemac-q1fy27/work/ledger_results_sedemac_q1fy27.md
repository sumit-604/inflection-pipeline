# A2 COMPLETENESS LEDGER — SEDEMAC Q1 FY27 — RESULTS FILING

Source: extract_results_sedemac_q1fy27.txt (6 pages, 312 lines, Crores x1,
standalone only per Note 5, ocr_pages: none)

```
=== A2 COUNT TEST ===
category: agenda_items   grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras  grep_count: 5    sweep_count: 5    match: yes
category: notes          grep_count: 6    sweep_count: 6    match: yes
category: line_items     grep_count: 40   sweep_count: 40   match: yes
  (of which P&L: 23, Segment: 17)
category: signatures     grep_count: 3    sweep_count: 3    match: yes
category: entities       grep_count: 0    sweep_count: 0    match: yes  (Note 5: no subsidiary/associate/JV — standalone only)
gate_a2: pass
=== END COUNT TEST ===
```

## Grep commands used
1. Notes (numbered, "Notes:" section): `grep -n -P "^\d+\t\s*[0-9]+\s{2,}[A-Z]"` restricted to post-line-261 region — 6 hits (lines 263, 271, 285, 288, 291, 293).
2. Board Outcome agenda items: `grep -n -P "^\d+\t\d+\.\s"` restricted to lines 15-77 — 1 hit (line 42).
3. Auditor report paragraphs: same numbered pattern restricted to lines 78-158 — 5 hits (lines 95, 98, 105, 113, 117).
4. P&L table data rows: `grep -c -P "[0-9]+\.[0-9]{2}"` on lines 174-219 — 23 hits.
5. Segment table data rows: same pattern on lines 229-259 — 17 hits.
6. Signature blocks: `grep -n "Digitally signed by"` — 3 hits (lines 56, 143, 304).
7. Entities: manual sweep of Note 5 text — explicit "no subsidiary, associate or joint venture" — 0 entities, consolidation table N/A this quarter (standalone only, per A1 context).

Manual sweep performed by full read of all 312 lines against each grep result; no discrepancies found in any category.

---

## TABLE 1 — BOARD OUTCOME LETTER: AGENDA ITEMS

| # | Line | Item | First 15 words | Flags |
|---|------|------|-----------------|-------|
| 1 | 42-43 | Item 1: Unaudited Financial Results | "Unaudited Financial Results for the quarter ended on June 30, 2026 along with the Limited Review Report" | — |

Meeting timing (line 48): commenced 08:17 p.m., concluded 09:32 p.m. — 75-minute board meeting.
Only one agenda item disclosed. No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution is present in this letter — this is a single-purpose results-only Board Outcome (consistent with a quarterly results-only board meeting, not an AGM-adjacent one). Recorded as `SINGLE_ITEM_MEETING` for A3/A4 awareness (not a defect, just a fact to carry forward).

Signature block (letter): Prasad Rajendra Chavan, Company Secretary and Compliance Officer, Membership No. A49921, digitally signed 2026-07-28 22:00:01 +05:30 (lines 56-63). Signed 28 minutes after board conclusion (09:32 p.m. / 21:32) — no timing flag.

---

## TABLE 2 — LIMITED REVIEW REPORT: PARAGRAPHS

| Para | Line(s) | Content (first 15 words) | Flags |
|------|---------|---------------------------|-------|
| 1 | 95-97 | "We have reviewed the accompanying Statement of unaudited financial results of SEDEMAC Mechatronics Limited" | Scope paragraph; entity reviewed = SEDEMAC Mechatronics Limited standalone only |
| 2 | 98-104 | "This Statement, which is the responsibility of the Company's management and approved by its Board" | Management responsibility; Ind AS 34 framework cited |
| 3 | 105-112 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements" | SRE 2410 basis; explicit "we do not express an audit opinion" |
| 4 | 113-116 | "Attention is drawn to the fact that the figures for the three months ended 31 March 2026" | Functions like an Emphasis-of-Matter para but NOT labeled "Emphasis of Matter" in the text — flag `UNLABELED_EOM_LANGUAGE`. Refers to Q4FY26 balancing figures (cross-references Note 4) |
| 5 | 117-122, 138 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe" | Conclusion: unmodified/unqualified review conclusion, no material misstatement noted |

No separate "Other Matters" paragraph. No Going Concern paragraph. Entity list reviewed: SEDEMAC Mechatronics Limited (standalone) only — no subsidiaries to consolidate (Note 5). No unaudited/management-furnished entities named (none apply; whole review is by the statutory auditor).

Report metadata: Auditor B S R & Co. LLP, Firm's Registration No. 101248W/W-100022 (line 142). Partner: Kalpesh Rameshchandra Khandelwal, Membership No. 133124 (line 149-151). UDIN: 26133124NZPRXU7451 (line 152). Report dated 28 July 2026, Pune (line 151-152). Report is 2 pages ("Page 1 of 2" line 130, "Page 2 of 2" line 157).

Signature block (report): Kalpesh Rameshchandra Khandelwal, Partner, digitally signed 2026-07-28 22:26:51 +05:30 (lines 143-150). Signed 54 minutes after board conclusion — no timing flag.

---

## TABLE 3 — STATEMENT OF UNAUDITED FINANCIAL RESULTS (P&L): LINE ITEMS
(Quarter ended 30 June 2026 / 31 March 2026 / 30 June 2025; Year ended 31 March 2026 — INR Crores)

| S.No | Line | Item | Q1FY27 (30-Jun-26) | Q4FY26 (31-Mar-26) | Q1FY26 (30-Jun-25) | FY26 (31-Mar-26) | Flags |
|------|------|------|---------------------|----------------------|----------------------|--------------------|-------|
| I | 174 | Revenue from operations | 309.77 | 287.71 | 217.36 | 1,058.38 | — |
| II | 175 | Other income | 0.86 | 0.63 | 2.60 | 5.27 | — |
| III | 176 | Total income (I+II) | 310.63 | 288.34 | 219.96 | 1,063.65 | — |
| IV | 178 | Expenses (section header, no own value) | — | — | — | — | `SECTION_HEADER` |
| — | 179 | Cost of materials consumed | 200.20 | 169.66 | 142.97 | 662.11 | — |
| — | 180-182 | Changes in inventories of finished goods and work-in-progress | (6.28) | 1.94 | (8.51) | (16.30) | — |
| — | 183 | Employee benefits expense | 24.16 | 20.42 | 19.77 | 86.61 | — |
| — | 184 | Finance costs | 2.32 | 1.31 | 2.43 | 8.53 | — |
| — | 185 | Depreciation and amortization expense | 16.37 | 17.89 | 13.09 | 63.48 | — |
| — | 186 | Other expenses | 32.52 | 35.20 | 20.04 | 109.03 | — |
| — | 187 | Total expenses (IV) | 269.29 | 246.42 | 189.79 | 913.46 | — |
| V | 189 | Profit before tax (III-IV) | 41.34 | 41.92 | 30.17 | 150.19 | — |
| VI | 191 | Tax expense (section header, no own value) | — | — | — | — | `SECTION_HEADER` |
| — | 192 | Current tax (refer note 3) | 4.72 | 7.23 | 5.00 | 24.66 | Cross-ref Note 3 (INR 2.98 cr reversal of excess prior-year tax provision embedded) |
| — | 193 | Deferred tax expense | 3.31 | 2.61 | 8.10 | 21.95 | — |
| — | 194 | Total tax expense | 8.03 | 9.84 | 13.10 | 46.61 | — |
| VII | 196 | Profit for the period/year (V-VI) | 33.31 | 32.08 | 17.07 | 103.58 | — |
| VIII | 198 | Other comprehensive income (section header, no own value) | — | — | — | — | `SECTION_HEADER` |
| — | 199 | "Items that will not be reclassified to profit or loss" (subheader, no own value) | — | — | — | — | `SECTION_HEADER` |
| — | 200 | Remeasurements of defined benefit obligations | (1.58) | 0.76 | (1.69) | (0.39) | — |
| — | 201 | Income-tax related to above item | 0.40 | (0.30) | 0.59 | 0.10 | — |
| — | 202-204 | Other comprehensive income/(expense) for the period/year (net of tax) | (1.18) | 0.46 | (1.10) | (0.29) | — |
| IX | 206-208 | Total comprehensive income for the period/year (VII+VIII) | 32.13 | 32.54 | 15.97 | 103.29 | — |
| — | 210-212 | Paid-up equity share capital (face value INR 10/share) | 44.17 | 44.16 | 0.03 | 44.16 | Q1FY26 value of 0.03 cr reflects pre-IPO capital base before the Mar-2026 IPO/listing (Note 2) — large jump is a known one-time event, not an anomaly |
| — | 214 | Other equity | — (blank) | — (blank) | — (blank) | 405.04 | `ZERO_STANDING` — line exists but is populated only in the annual (year-ended) column per standard SEBI quarterly-results format; blank in all three quarter columns |
| — | 216-217 | Earnings per equity share (nominal value INR 10) (subheader, no own value) | — | — | — | — | `SECTION_HEADER` |
| — | 218 | -Basic (INR) | 7.54 | 7.32 | 4.02 | 23.91 | — |
| — | 219 | -Diluted (INR) | 7.49 | 7.17 | 3.93 | 23.52 | — |
| — | 220 | Footnote: "EPS are not annualised for the interim periods." | n/a | n/a | n/a | n/a | Footnote qualifying EPS headline rows, unnumbered ("*" marker), captured by manual sweep (not part of numbered-notes grep) |

P&L data-bearing line items: 23 (grep and sweep both = 23). Section-header rows (no own value): 5 (IV, VI, VIII, "Items that will not be reclassified...", "Earnings per equity share"). One footnote (line 220, asterisk-marked, unnumbered).

---

## TABLE 4 — SEGMENT-WISE STATEMENT: LINE ITEMS
(Quarter ended 30 June 2026 / 31 March 2026 / 30 June 2025; Year ended 31 March 2026 — INR Crores)

| Section | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| A | 236 | Segment revenue from operations (header, no own value) | — | — | — | — | `SECTION_HEADER` |
| A | 237 | -Mobility | 281.04 | 258.39 | 183.26 | 910.57 | — |
| A | 238 | -Industrial | 28.73 | 29.32 | 34.10 | 147.81 | — |
| A | 239 | Total revenue from operations | 309.77 | 287.71 | 217.36 | 1,058.38 | Ties to P&L line I |
| B | 241 | Segment results (header, no own value) | — | — | — | — | `SECTION_HEADER` |
| B | 242 | -Mobility | 39.09 | 38.08 | 26.85 | 129.98 | — |
| B | 243 | -Industrial | 3.96 | 4.45 | 4.84 | 22.96 | — |
| B | 244 | Total | 43.05 | 42.53 | 31.69 | 152.94 | — |
| B | 245 | Less: Unallocable expenses | (2.31) | (1.15) | (2.32) | (7.70) | — |
| B | 246 | Add: Unallocable income | 0.60 | 0.54 | 0.80 | 4.95 | — |
| B | 247 | Profit before tax | 41.34 | 41.92 | 30.17 | 150.19 | Ties to P&L line V |
| C | 249 | Segment assets (header, no own value) | — | — | — | — | `SECTION_HEADER` |
| C | 250 | -Mobility | 835.56 | 654.05 | 439.16 | 654.05 | — |
| C | 251 | -Industrial | 78.95 | 74.25 | 65.98 | 74.25 | — |
| C | 252 | -Unallocable | 28.55 | 85.40 | 47.04 | 85.40 | — |
| C | 253 | Total assets | 943.06 | 813.70 | 552.18 | 813.70 | — |
| D | 255 | Segment liabilities (header, no own value) | — | — | — | — | `SECTION_HEADER` |
| D | 256 | -Mobility | 303.63 | 259.60 | 142.73 | 259.60 | — |
| D | 257 | -Industrial | 23.64 | 36.16 | 22.57 | 36.16 | — |
| D | 258 | -Unallocable | 122.49 | 68.74 | 64.12 | 68.74 | — |
| D | 259 | Total liabilities | 449.76 | 364.50 | 229.42 | 364.50 | — |

Segment data-bearing line items: 17 (grep and sweep both = 17). Section-header rows: 4 (A, B, C, D). Two reportable segments named: Mobility, Industrial (plus an "Unallocable" residual line in the assets/liabilities/results sections, not a third operating segment).

Combined P&L + Segment data-bearing line items: 23 + 17 = 40.

---

## TABLE 5 — NOTES TO FINANCIAL RESULTS

| Note # | Line(s) | First 15 words | Flags |
|--------|---------|------------------|-------|
| 1 | 263-269 | "The above financial results have been reviewed by the Audit Committee and thereafter approved" | States Ind-AS basis, references unqualified review conclusion by statutory auditors |
| 2 | 271-276 | "During the quarter and year ended 31 March 2026, the Company has completed its Initial Public Offering" | Historical IPO disclosure (completed prior quarter, listed 11 March 2026); IPO was pure offer-for-sale (80,43,300 shares, INR 1,087.45 cr) — no fresh capital to the company |
| 3 | 285-286 | "Income tax expense for the quarter ended 30 June 2026 includes a reversal of excess tax" | Reversal of INR 2.98 cr excess prior-year tax provision embedded in current-tax line (line 192) — non-recurring, affects PAT comparability |
| 4 | 288-289 | "The figures for the quarter ended 31 March 2026 is the balancing figures, between audited financial" | Explains Q4FY26 column derivation (balancing figure between FY26 audited annual and 9M FY26 audited); cross-referenced at top of both P&L and segment tables ("Refer note 4", lines 173, 235) and in Review Report para 4 |
| 5 | 291 | "The Company has no subsidiary, associate or joint venture companies as on 30 June 2026." | Confirms standalone-only filing; 0 entities to enumerate in consolidation table this quarter |
| 6 | 293-294 | "The above financial results are available on the Company's website (www.sedemac.com) and also on the websites" | Standard availability/boilerplate note |

Numbered notes total: 6 (grep and sweep both = 6). No unnumbered notes or footnotes found below the numbered-notes block itself; the one unnumbered footnote in the filing is the EPS asterisk footnote at line 220 (captured in Table 3), which sits under the P&L table, not under the "Notes:" heading.

---

## TABLE 6 — DIGITAL SIGNATURE BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp | Document | Flags |
|---|---------|-----------|-------------|-----------|----------|-------|
| 1 | 56-63 | Prasad Rajendra Chavan | Company Secretary and Compliance Officer, Membership No. A49921 | 2026-07-28 22:00:01 +05:30 | Board Outcome letter | Signed 28 min after board conclusion (21:32) — no timing flag |
| 2 | 143-151 | Kalpesh Rameshchandra Khandelwal | Partner, B S R & Co. LLP, Membership No. 133124 | 2026-07-28 22:26:51 +05:30 | Limited Review Report; UDIN 26133124NZPRXU7451 | Signed 54 min after board conclusion — no timing flag |
| 3 | 304-311 | Amit Arun Dixit | Joint Managing Director, DIN 01288169 | 2026-07-28 22:04:49 +05:30 | Statement of Unaudited Financial Results | Signed 32 min after board conclusion — no timing flag |

Signature blocks total: 3 (grep and sweep both = 3). All three post-date board meeting conclusion (21:32) — no `PREMATURE_SIGNATURE` flag applicable.

---

## TABLE 7 — CONSOLIDATION ENTITIES

None. Note 5 (line 291): "The Company has no subsidiary, associate or joint venture companies as on 30 June 2026." No consolidated statement exists this quarter (per A1 context and doctype = standalone results only). Entities enumerated: 0. No prior-quarter entity list was supplied for diff (`PRIOR_LEDGER_PATH` not provided / not applicable), so `ENTITY_CHANGE` cannot be evaluated this run — flag `NO_PRIOR_LEDGER_FOR_ENTITY_DIFF` for A3/A4 awareness.

---

## SUMMARY FLAGS RAISED
- `ZERO_STANDING` — "Other equity" line (P&L table, line 214): blank in all three quarter columns, populated only in year-ended column (standard format, not an anomaly, but a standing zero/blank line per ledger rule).
- `SECTION_HEADER` — 9 structural header/subheader rows with no own numeric value (5 in P&L table, 4 in segment table); listed for completeness, not counted in the 40 data-bearing line items.
- `UNLABELED_EOM_LANGUAGE` — Review Report paragraph 4 functions like an Emphasis of Matter paragraph (draws attention to Q4FY26 balancing-figure derivation) but is not headed "Emphasis of Matter" in the text.
- `SINGLE_ITEM_MEETING` — Board Outcome letter carries exactly one agenda item (results approval); no other corporate actions this quarter.
- `NO_PRIOR_LEDGER_FOR_ENTITY_DIFF` — no prior-quarter ledger path supplied to test `ENTITY_CHANGE`.

No `MGMT_ABSENCE`, `ENTITY_CHANGE`, `REPEAT_QUESTION`, or `DROPPED_SLIDE` flags applicable — this is a results filing, not a concall transcript or investor presentation (those are separate doctypes/extracts under this same ticker-quarter, out of scope for this ledger).
