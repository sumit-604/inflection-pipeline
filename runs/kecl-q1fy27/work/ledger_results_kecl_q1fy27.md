# A2 COMPLETENESS LEDGER — Kirloskar Electric Company Limited (KECL), Q1 FY27, RESULTS filing

Source: `/home/user/inflection-pipeline/runs/kecl-q1fy27/work/extract_results_kecl_q1fy27.txt`
Prior-quarter ledger: NONE (first pipeline run for KECL; ENTITY_CHANGE / DROPPED_SLIDE style diffs not applicable this run)

```
=== A2 COUNT TEST ===
category: notes                    grep_count: 14  sweep_count: 14  match: yes
category: pnl_line_items           grep_count: 28  sweep_count: 28  match: yes
category: segment_line_items       grep_count: 32  sweep_count: 32  match: yes
category: agenda_items             grep_count: 3   sweep_count: 3   match: yes
category: auditor_paras_standalone grep_count: 10  sweep_count: 10  match: yes
category: auditor_paras_consol     grep_count: 12  sweep_count: 12  match: yes
category: auditor_paras_total      grep_count: 22  sweep_count: 22  match: yes
category: annexure2_rows           grep_count: 3   sweep_count: 3   match: yes
category: annexure3_paragraphs     grep_count: 9   sweep_count: 9   match: yes
category: entities_named           grep_count: 7   sweep_count: 7   match: yes  (see reconciliation note below)
category: signature_blocks         grep_count: 4   sweep_count: 4   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation notes on the two count-test categories that needed a re-sweep before matching:**
- `entities_named`: first grep pass (rigid single-space regex) returned 8 raw string hits and MISSED "Kirloskar Power Equipments Limited" (Note 9) because the source PDF/OCR renders irregular multi-space gaps inside that name (`Kirloskar   Power   Equipments    Limited`). Manual sweep caught it independently. Re-ran grep with `\s+` flexible whitespace: 9 raw string hits. Two of those nine strings are OCR spelling variants of the same two legal entities (`SKG Terra Promenade` vs `SKG Terra Promonede`; `Luxquisite Parkland` vs `Luxqusite Parkland` — flag `SPELLING_VARIANT`), collapsing 9 raw hits to 7 distinct named entities, which now matches the manual sweep of 7. Gate re-verified pass after correction.
- `pnl_line_items`: a naive digit-pattern grep over lines 89-134 returns 29 raw hits, of which 2 are false positives (the year-header row "2026 2026 2025…" and the EPS section header "face value of ₹10/- each)" — the "10" token false-triggers a digit regex) and it silently omits 2 genuine line items that carry no digits at all in the extract ("Adjustments relating to earlier years" — fully blank row; "Deferred tax" — dash-only row). The reconciled grep (all data-zone lines 96-134 minus known non-item artifacts: 1 line-wrap continuation, 4 blank spacer lines, 1 section header) returns 28, matching the manual sweep of 28 distinct disclosed line items (26 digit/dash-bearing + 2 wholly blank ZERO_STANDING rows).

---

## 1. NOTES (numbered notes 1-14, all standalone + consolidated results notes)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 253 | "The above unaudited standalone and consolidated financial results have been reviewed by the Audit Committee..." | — |
| 2 | 256 | "The standalone and consolidated financial results of the Company for the quarter ended June 30, 2026..." | — |
| 3 | 260 | "The Company has prepared these Standalone and Consolidated financial results in accordance with Companies (Indian Accounting Standard) Rules, 2015..." | — |
| 4 | 267 | "The Board of Directors in its meeting held on May 23, 2024, has approved for the merger..." | EOM-linked (auditor EOM(a), both reports) |
| 5 | 281 | "The net worth (after excluding revaluation reserve) of the group... is eroded... going concern basis..." | GOING_CONCERN-linked (auditor KAM, both reports) |
| 6 | 295 | "The Company has filed before the honorable Supreme Court, special leave petition (SLP) in respect of resale tax penalty demand of ₹527 lakhs..." | EOM-linked (auditor EOM(b), both reports) |
| 7 | 305 | "On October 03, 2022, the Company has entered into an Agreement to Sell (ATS) a part of its immovable property..." | Continues onto page 5 (lines 344-354) |
| 8 | 357 | "On March 20, 2024 the Company has entered into an Agreement to Sell part of its immovable property, situated at Gokul Road, Hubbali..." | — |
| 9 | 371 | "On July 16, 2026, Board of Directors of the Company has approved to issue upto 34,68,007 equity shares..." | Subsequent event; preferential issue to promoter group entity Kirloskar Power Equipments Limited; ties to press-release "equity infusion" language (Annexure 3, line 833) |
| 10 | 381 | "Other income for the year ended March 31, 2026 includes profit on receipt on full consideration towards 1.06 acres property..." | Prior-year (FY26) disclosure, not current quarter |
| 11 | 387 | "The Government of India has notified New Labour Codes effective from November 21, 2025... increase in gratuity and leave liability by 809 lakhs..." | Ties to Exceptional items line (P&L row VI) |
| 12 | 395 | "Details of Secured Redeemable Non-Convertible Debentures - NIL" | **ZERO_STANDING** — explicit NIL disclosure line, the note itself is a standing zero-value item |
| 13 | 397 | "Previous period figures have been regrouped wherever necessary to confirm with the current period presentation." | — |
| 14 | 400 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | Standard Q4-derivation disclaimer |

Notes count: grep (`^\s*[0-9]{1,2}\s+[A-Za-z]` restricted to lines 250-406 to exclude segment-table false positives) = 14. Manual sweep = 14 (1 through 14, no gaps). No unnumbered footnotes, asterisks, daggers, or "Note:" prefixes found anywhere else in the extract (checked file-wide).

---

## 2. STANDALONE + CONSOLIDATED STATEMENT OF UNAUDITED FINANCIAL RESULTS — P&L LINE ITEMS (page 2, lines 89-134)

Table presents Standalone and Consolidated side by side, each with 4 value columns (Qtr ended Jun 30 2026, Qtr ended Mar 31 2026, Qtr ended Jun 30 2025, Year ended Mar 31 2026). One ledger row per disclosed line item (all 8 values live on that one source line).

| Sl No | Line | Line item | Flags |
|-------|------|-----------|-------|
| — | 95 | Income from operations: (section header, not a value row) | HEADER |
| I | 96 | Revenue from operations | — |
| II | 97 | Other income | OCR shows "I" not "II" for this row's sl-no glyph — OCR_ARTIFACT, label unambiguous from context |
| III | 98 | Total income (I+II) | OCR sl-no glyph renders as "[" — OCR_ARTIFACT |
| — | 99 | Expenses: (section header) | HEADER |
| a | 100 | Cost of materials consumed | — |
| b | 101-102 | Change in inventories of finished goods, work in progress and stock in trade | — |
| c | 103 | Employee benefit expenses | — |
| d | 104 | Finance costs | — |
| e | 105 | Depreciation and amortisation expenses | — |
| f | 106 | Other expenses | — |
| — | 107 | Total expenses (subtotal) | — |
| V | 108 | Profit/(loss) before exceptional item and tax (III-IV) | — |
| VI | 109 | Exceptional items (Refer note - 11) | **ZERO_STANDING** for both current qtr (Jun-26) and year-ago qtr (Jun-25) columns, standalone and consolidated alike (dash values); only populated in Year ended Mar-26 column (809/809), sourced to Note 11 (Labour Code gratuity/leave impact) |
| VII | 110 | Profit/(loss) before tax (V+VI) | — |
| — | 111 | Tax expense: (section header) | HEADER |
| a | 112 | Current Tax | **ZERO_STANDING** in year-ago qtr (Jun-25) column only (dash); populated elsewhere |
| b | 113 | Adjustments relating to earlier years | **ZERO_STANDING** — row label present, no value at all in any of the 8 columns (fully blank); canonical template-signal row (line exists because such adjustments have occurred or are anticipated, per instruction) |
| c | 114 | Deferred tax | **ZERO_STANDING** — dash in all 8 columns |
| IX | 115 | Profit/(loss) after tax (VII-VIII) | — |
| — | 116 | Other comprehensive income: (section header) | HEADER |
| — | 117 | (i) Items that will not be reclassified to profit or loss (sub-header) | HEADER |
| a | 118 | Remeasurements of the defined benefit plans | **ZERO_STANDING** in both quarter columns (current and year-ago), standalone and consolidated; only populated in Year ended Mar-26 column (79/79) — actuarial remeasurement is an annual-only entry |
| b | 119 | Taxes on above (remeasurement tax) | **ZERO_STANDING** in both quarter columns; only in Year ended column ((22)/(22)) |
| — | 120 | (ii) Items that may be reclassified to profit or loss (sub-header) | HEADER |
| a | 121 | Mark to Market of Investments | — |
| b | 122 | Revaluation gain on land | **ZERO_STANDING** in both quarter columns (dash); only in Year ended column ((366)/(366)) |
| c | 123 | Taxes on above (MTM/revaluation tax) | — |
| — | 124 | Total other comprehensive income (subtotal) | — |
| XI | 126 | Total comprehensive income for the period (IX+X) | — |
| — | 128 | Paid-up equity share capital (face value ₹10/- each) | — |
| — | 130 | Other Equity | **ZERO_STANDING** / blank in all quarter columns (Jun-26, Mar-26-qtr, Jun-25); only populated in Year ended Mar-26 column (6,594) — balance-sheet item disclosed annually only, standard convention |
| — | 132 | Earnings per share (EPS) (face value ₹10/- each) (section header) | HEADER |
| a | 133 | Basic EPS (not annualised) | — |
| b | 134 | Diluted EPS (not annualised) | Year-ended standalone figure OCR-garbled as "1.2/" (should read 1.27, consistent with Basic EPS 1.24 and immaterial dilution) — **OCR_ARTIFACT**, flagged for A3/A4 not to treat as a real discrepancy without source-PDF confirmation |

P&L value-bearing line items enumerated: 28 (7 HEADER/sub-header rows excluded from this count, listed separately above for completeness). ZERO_STANDING flags raised: 7 rows (Exceptional items, Adjustments relating to earlier years, Deferred tax, Remeasurements of defined benefit plans, Taxes on above (remeasurement), Revaluation gain on land, Other Equity) plus partial ZERO_STANDING on Current Tax's year-ago-quarter cell.

---

## 3. SEGMENT REPORTING — REVENUES, RESULTS, ASSETS, LIABILITIES, CAPITAL EMPLOYED (page 3, lines 163-241)

**Data-quality flag: OCR_DEGRADED.** The extract's segment table has standalone and consolidated columns visibly interleaved/misaligned across source lines (e.g. lines 174-179 show values and labels alternating in a pattern inconsistent with the stated column order). Row LABELS are unambiguous; individual VALUE alignment to standalone-vs-consolidated columns should be re-verified against the source PDF by A3/A4 before quoting exact segment figures. Two named operating segments disclosed: Power generation/distribution, Rotating machines, plus a residual "Others" bucket.

| Category (Sl No) | Line | Row | Flags |
|---|------|-----|-------|
| 1 Segment Revenues | 172 | (header) | HEADER |
| | 173-174 | Power generation/ distribution | — |
| | 175-176 | Rotating machines | — |
| | 177-178 | Others | — |
| | 179-180 | Total (subtotal) | — |
| | 181-182 | Less: Inter segment revenues | — |
| | 183-184 | Revenue from operations (= P&L line I, cross-check target) | — |
| 2 Segment Results | 185-187 | (header + "Profit before interest and tax expense" sub-header) | HEADER |
| | 188-189 | Power generation/ distribution | — |
| | 190-191 | Rotating machines | — |
| | 192-193 | Others | — |
| | 194-195 | Total (subtotal) | — |
| | 195-196 | Less: Interest | — |
| | 197-198 | Less: Other unallocable expenditure (net off unallocable Income) | — |
| | 198-199 | Add: Exceptional item | **ZERO_STANDING** in quarter columns (dash), Year-ended column shows (809)/(809) — mirrors P&L line VI |
| | 201-202 | Total profit before tax expense (= P&L line VII, cross-check target) | — |
| 3 Segment Assets | 203-204 | (header) | HEADER |
| | 204-205 | Power generation/ distribution | — |
| | 206-207 | Rotating machines | — |
| | 208-209 | Others | — |
| | 210-211 | Total (subtotal) | — |
| | 212-213 | Add: Unallocable assets | — |
| | 214-215 | Total segment assets | — |
| 4 Segment Liabilities | 216-217 | (header) | HEADER |
| | 217-218 | Power generation/ distribution | — |
| | 219-220 | Rotating machines | — |
| | 221-222 | Others | — |
| | 223-224 | Total (subtotal) | — |
| | 225-226 | Add: Unallocable liabilities | — |
| | 227-228 | Total segment liabilities | — |
| 5 Capital Employed | 229-230 | (header, "Segment Assets-Segment Liabilities") | HEADER |
| | 230-231 | Power generation/ distribution | — |
| | 232-233 | Rotating machines | — |
| | 234-235 | Others | — |
| | 236 | Total capital employed in segments (subtotal, this category's equivalent of the "Total" row used in the other four) | — |
| | 237-238 | Add: Unallocated | — |
| | 239-241 | Total capital employed | — |

Segment value-bearing rows enumerated: 32 (5 category subtotals + 5 category headers excluded from the 32 count + 3-segment × 5 categories = 15 + 7 adjustment/add-back rows + 5 final-total rows + ... reconciled to 32 per count test above; header/sub-header rows listed separately, not counted).

---

## 4. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1, lines 17-77)

Board meeting: commencement **12:46 P.M.**, conclusion **1:05 P.M.** — a **19-minute** meeting (line 36-38). Recorded for the record; no formal flag code applies but this is a short meeting for 3 agenda items including financial results approval and a cost-auditor appointment.

| # | Line | Agenda item | Flags |
|---|------|-------------|-------|
| 1 | 43-45 | Ind AS compliant unaudited standalone and consolidated financial results for quarter ended June 30, 2026, signed by Mr. Vijay Ravindra Kirloskar (DIN 00031253), Executive Chairman, with limited review report — Annexure-1 | — |
| 2 | 47-51 | Appointment of M/s. Rao, Murthy & Associates, Cost Accountants, Bengaluru (FRN 000065), as Cost Auditors for FY 2026-27, per Audit Committee recommendation — disclosure at Annexure-2 | — |
| 3 | 53-54 | Press Release on unaudited (Standalone and Consolidated) Financial Results for Q1 FY2026-27 — Annexure-3 | — |

No further agenda items disclosed (no AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change beyond the cost auditor item above, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution appears in this Board Outcome letter). Note 9 (preferential issue to Kirloskar Power Equipments Limited) was approved at a **prior** board meeting (July 16, 2026, per Note 9 and confirmed by Annexure 3 press release line 811 "approved by the Board of Directors at the previous board meeting") — not an agenda item of today's (Aug 13, 2026) meeting; flagged here only as a cross-reference so A3/A4 do not miss it.

Agenda items count: grep (`^\s*[0-9]\.\s` in lines 1-78) = 3. Manual sweep = 3. Match.

---

## 5. AUDITOR REVIEW REPORT — STANDALONE (K N Prabhashankar & Co., pages 6-7, lines 414-566)

| # | Line | Paragraph content | Explicit numeral in extract? | Flags |
|---|------|--------------------|-------------------------------|-------|
| 1 | 433-437 | Introduction / engagement scope (Regulation 33, SEBI Circular reference) | Yes — "1." | — |
| 2 | 439-444 | Management's responsibility for the Statement; auditor's responsibility to express an opinion | No | **EXTRACTION_GAP** — logically para 2, numeral not captured |
| 3 | 446-453 | Basis of review — SRE 2410 standard, scope-of-review limitations vs audit | No | **EXTRACTION_GAP** — logically para 3; confirmed to exist because para 4 (below) explicitly says "as per paragraph 3 above" |
| 4 | 455-463 | Conclusion — unmodified/clean opinion language ("nothing has come to our attention...") | No | **EXTRACTION_GAP** — logically para 4 |
| 5 | 464-495 | Key Audit Matters heading + Note 5 going-concern KAM, including reliance on restructuring plan / monetization of non-core assets; opinion "not modified" | No (heading "Key Audit Matters:" unnumbered) | **EXTRACTION_GAP**; **GOING_CONCERN language present but opinion explicitly not modified** |
| 6 | 497 | "6. Emphasis of Matter:" heading | Yes — "6." | — |
| 6(a) | 499-521 | EOM(a) — Note 4, Scheme of Amalgamation of 4 subsidiaries per NCLT order dated Apr 30, 2026, appointed date Apr 1, 2024; opinion not modified | (a) lettered | — |
| 6(b) | 523-540 | EOM(b) — Note 6, SLP re: ₹527 lakh resale tax penalty on erstwhile subsidiary Kaytee Switchgear Limited; opinion not modified | (b) lettered | — |
| 7 | 542-548 | "7." — Q4 FY26 figures are balancing figures between full-year audited and 9-month published figures, subject to limited review | Yes — "7." | — |
| — | 553-565 | Signature block: for K N Prabhashankar & Co., Chartered Accountants, Firm Regn 004982S; A. Umesh Patwardhan, Partner, M.No. 222945; Place Bengaluru; Date Aug 13, 2026; UDIN present but OCR-garbled | n/a | **OCR_ARTIFACT** on UDIN string (line 565, unreadable glyphs); entity list reviewed = standalone Company only (no subsidiaries in scope, per report title) |

Standalone auditor paragraphs enumerated: 10 (grep anchor match = 10, manual sweep = 10, match yes). Opinion type: unmodified/unqualified (limited review conclusion). Going-concern language present within KAM but explicitly not treated as a modifying matter. No "Other Matters" paragraph in the standalone report (unlike consolidated, see below).

---

## 6. AUDITOR REVIEW REPORT — CONSOLIDATED (K N Prabhashankar & Co., pages 8-10, lines 569-768)

| # | Line | Paragraph content | Explicit numeral in extract? | Flags |
|---|------|--------------------|-------------------------------|-------|
| 1 | 590-596 | Introduction / engagement scope — Parent + subsidiaries + associates ("Group"), Regulation 33 reference | No | **EXTRACTION_GAP** — logically para 1 (standalone report's counterpart carried "1.", this one does not) |
| 2 | 598-603 | Parent's management responsibility; auditor's responsibility to opine | No | **EXTRACTION_GAP** |
| 3 | 605-612 | Basis of review — SRE 2410 scope-of-review limitations | No | **EXTRACTION_GAP**; confirmed to exist because para 7 (below) references "paragraph 3 above" |
| 4 | 614-616 | Additional procedures performed per SEBI Circular under Regulation 33(8) | No | **EXTRACTION_GAP**; **CONSOLIDATED-ONLY paragraph — no counterpart in the standalone report** |
| 5 | 619-647 | Key Audit Matters heading + Note 5 going-concern KAM (Company, subsidiaries and associate); opinion not modified | No | **EXTRACTION_GAP**; **GOING_CONCERN language present, opinion not modified** |
| 6 | 649 | "5. Emphasis of Matter:" heading | Yes — "5." | Numbering diverges from standalone (standalone EOM = "6.", consolidated EOM = "5.") — cannot be resolved from the extract alone whether this reflects the true source-PDF numbering or a further extraction gap; flagged for A3/A4, not resolved here |
| 5(a) | 651-674 | EOM(a) — Note 4, Scheme of Amalgamation, same substance as standalone EOM(a) | (a) lettered | — |
| 5(b) | 676-692 | EOM(b) — Note 6, SLP re: ₹527 lakh resale tax penalty, same substance as standalone EOM(b) | (b) lettered | — |
| 6 | 695-711 | "6. Other Matters:" — one subsidiary located outside India, financial statements prepared under local GAAP and converted to Ind AS by Parent's management, reviewed by auditor | Yes — "6." | **CONSOLIDATED-ONLY paragraph — no counterpart in standalone report**; foreign subsidiary not named in this paragraph (named as "Kirsons BV" only in para 7 below) |
| 7 | 715-743 | "7." — Conclusion, qualified/"except for" language tied to the Other Matters paragraph; names **Kirsons BV** as the entity whose unaudited results are included; also recaps the NCLT Bengaluru Bench merger order (received May 15, 2026) covering the same 4 amalgamated subsidiaries as standalone Note 4 | Yes — "7." | — |
| 8 | 746-752 | "8." — Q4 FY26 figures are balancing figures between full-year audited and 9-month published figures, subject to limited review | Yes — "8." | — |
| — | 757-768 | Signature block: for K N Prabhashankar & Co., Chartered Accountants, Firm Regn 004982S; A. Umesh Patwardhan, Partner, M.No. 222945; Place Bengaluru; Date Aug 13, 2026; UDIN present but OCR-garbled | n/a | **OCR_ARTIFACT** on UDIN string (line 768) |

Consolidated auditor paragraphs enumerated: 12 (grep anchor match = 12, manual sweep = 12, match yes). Opinion type: the para-7 conclusion uses "except for the effects in respect of the matter stated in the paragraph on Other Matters" phrasing — this reads as a qualification/exception carve-out tied to the foreign-subsidiary conversion procedures, distinct from a clean unmodified opinion; **flagged for A3/A4 interpretation, not resolved here** (A2 enumerates only). No going-concern modification either report.

**Entities covered by review**: standalone report — parent company (KECL) only. Consolidated report — parent + subsidiaries + associate(s), explicitly including Kirsons BV (foreign, unaudited-by-local-standards, management-converted financials reviewed by auditor per Other Matters para). Same statutory auditor (K N Prabhashankar & Co.) and same signing partner (A. Umesh Patwardhan) issued both reports, same date (Aug 13, 2026).

---

## 7. ANNEXURE 1 — FINANCIAL RESULTS + BOTH AUDITOR REPORTS

Annexure 1 (per Board Outcome item 1, line 45) is not a separately labelled section in the extract; it is the collective label for the P&L statement (Section 2 above), segment table (Section 3), Notes (Section 1), and both auditor review reports (Sections 5-6). No separate Annexure-1 heading/table found in the extract distinct from these already-enumerated components — recorded here so the annexure is not silently dropped from the ledger.

## 8. ANNEXURE 2 — COST AUDITOR APPOINTMENT DISCLOSURE (page 11, lines 772-798)

| Sr No | Line | Event | Disclosed information | Flags |
|-------|------|-------|------------------------|-------|
| 1 | 781 | Reasons for Change | Appointment | — |
| 2 | 783-784 | Date of Appointment/cessation & Term | Date of appointment: 13.08.2026; Term: One year (FY 2026-27) | — |
| 3 | 786-790 | Brief profile | Firm established 1994, based in Bengaluru; Partners Mr. N. Ramaskanda (Membership 9750) and Mr. K.R. Murali Krishna (Membership 21622); offers statutory and non-statutory services | — |

Annexure 2 rows: grep (`^\s*[0-9]\.\s` in lines 772-799) = 3. Manual sweep = 3. Match.

## 9. ANNEXURE 3 — PRESS RELEASE (pages 12-13, lines 802-878)

Unit convention flag carried over from A1 header: press-release figures are natively in **Rs Crores** (not Lakhs) — do not reapply the Lakhs-to-Cr conversion factor to any number in this section.

| # | Line | Content block | Key figures cited (as stated, Rs Crores) | Flags |
|---|------|----------------|--------------------------------------------|-------|
| 1 | 807 | Headline: "Kirloskar Electric Company Limited Reports Q1 FY27 Results" | — | — |
| 2 | 809-811 | Dateline + lead: Bengaluru, 13 Aug 2026; results announcement + reference to "a significant capital strengthening initiative approved... at the previous board meeting" | — | Cross-refs Note 9 (preferential issue) |
| 3 | 813-817 | Order booking: order booking ₹184 Cr, +36% QoQ, +28% YoY, book-to-bill 1.79x; led by transformer business at Mysore (highest-ever Q1 intake); cast resin transformer traction in data centre segment | ₹184 Cr; +36% QoQ; +28% YoY; 1.79x book-to-bill | — |
| 4 | 819-824 | Revenue: ₹103.9 Cr vs ₹132.2 Cr in Q1 FY26 (YoY decline); loss before tax ₹5.95 Cr vs profit before tax ₹0.45 Cr in Q1 FY26; attributed to subdued billing / deferred dispatches amid macro and supply chain uncertainty; company expects normalization through the year | ₹103.9 Cr revenue; ₹132.2 Cr PY revenue; (₹5.95 Cr) PBT vs ₹0.45 Cr PY PBT | Revenue figure (₹103.9 Cr = 10,385 lakhs) and PBT figure ((₹5.95 Cr) = (595) lakhs) tie out arithmetically to the Lakhs-denominated P&L (Section 2, lines 96, 110) — cross-check passes |
| 5 | 826-828 | Material cost improved to 69.1% of revenue from 71.9% YoY; finance costs down 17.3% YoY to ₹5.25 Cr | 69.1% vs 71.9% material cost ratio; ₹5.25 Cr finance cost, -17.3% YoY | ₹5.25 Cr finance cost = 525 lakhs, ties to P&L line IV(d) (Section 2, line 104) |
| 6 | 830-835 | Chairman quote (Mr. Vijay Kirloskar, Executive Chairman): temporary external billing constraints; order intake framed as "strongest first quarter we have recorded"; promoters' equity infusion framed as "clear endorsement"; focus on converting order book | — | Ties to Note 9 preferential issue and press-release para 2 reference to prior board meeting |
| 7 | 837-838 | Closing boilerplate: commitment to disciplined financial management and long-term value creation | — | — |
| 8 | 840-859 | "About Kirloskar Electric Company Limited" — incorporated 26 July 1946; product range (motors, alternators, generators, transformers, DG sets); product groups (transformer & distribution, large machine, low voltage machine, power generation); EV motor manufacturing claim; listed NSE 9 Mar 2010, BSE 28 Apr 2010 | — | — |
| 9 | 861-870 | Media contact block: company name, address, phone, fax, customer care, email | — | — |

Recurring page-footer boilerplate (registered office address, phone/fax, customer care, CIN — identical block appears on pages 1, 11, 12, 13 at lines 74-77, 795-798, 845-848, 875-878) noted once here; not treated as a separate disclosure unit per repetition.

Annexure 3 content blocks: grep (distinctive opening-phrase anchors) = 9. Manual sweep = 9. Match.

---

## 10. ENTITY LIST (consolidation scope + related/historical entities named anywhere in the filing)

No prior-quarter ledger exists for KECL — `ENTITY_CHANGE` comparison not applicable this run; every entity below is recorded as baseline for future-quarter diffs.

| Entity | Line(s) | Relationship / status | Flags |
|--------|---------|------------------------|-------|
| Kirsons BV | 721 (also implied 697-711, 733-743) | Foreign subsidiary, currently in consolidation scope; results prepared under local GAAP, converted to Ind AS by Parent's management, reviewed by auditor (consolidated Other Matters para) | Named only in the consolidated auditor report, not in the Notes |
| Unnamed "subsidiary" (singular) | 283, 468, 623 | Note 5 / KAM language refers to "the Company, its subsidiary and its associate" (singular) — likely = Kirsons BV given it is the only currently-active subsidiary evidenced elsewhere, but not explicitly cross-referenced in the extract | **NOT_FOUND** (name not confirmed equal to Kirsons BV in the text) — flagged for A3/A4 |
| Unnamed "associate" (singular) | 283, 468, 623 | Referenced generically, never named | **NOT_FOUND** |
| Kelbuzz Trading Private Limited | 268, 502-503, 654-655, 735-736 | Formerly wholly-owned subsidiary; merged into KECL effective Apr 1, 2024 per NCLT Bengaluru Bench order dated Apr 30, 2026 (received May 15, 2026); historical, no longer a separate consolidation entity | — |
| SKG Terra Promenade / SKG Terra Promonede Private Limited | 268-269 ("Promenade"), 504 & 656 ("Promonede"), 737 ("Promonede") | Same as above (merged subsidiary) | **SPELLING_VARIANT** — "Promenade" (Note 4) vs "Promonede" (both auditor reports); not resolved as to which is correct, flagged for A3/A4 |
| SLPKG Estate Holdings / SLPKG Estate Holding Private Limited | 269, 505, 657-658, 738-739 | Same (merged subsidiary) | **SPELLING_VARIANT** — "Holdings" (Note 4) vs "Holding" (auditor reports) |
| Luxquisite Parkland / Luxqusite Parkland Private Limited | 270 ("Luxquisite"), 503 & 655 ("Luxqusite"), 737 ("Luxqusite") | Same (merged subsidiary) | **SPELLING_VARIANT** — "Luxquisite" (Note 4) vs "Luxqusite" (auditor reports) |
| Kaytee Switchgear Limited | 297 | "Erstwhile subsidiary... since merged with the parent company" — historical, subject of the SLP resale-tax litigation (Note 6 / EOM(b)) | Distinct merger event from the 4-subsidiary NCLT merger above; do not conflate |
| Kirloskar Power Equipments Limited | 375 | Promoter group company; counterparty to the Note 9 preferential equity issue (up to 34,68,007 shares, floor price ₹115.34, aggregating up to ₹40 crore) | Not a consolidation entity — related party / promoter group only; regex initially missed this name due to irregular OCR spacing, caught on manual re-sweep (see reconciliation note at top) |

Distinct named entities: 7 (Kirsons BV, Kelbuzz Trading, SKG Terra Promenade/Promonede, SLPKG Estate Holdings/Holding, Luxquisite/Luxqusite Parkland, Kaytee Switchgear, Kirloskar Power Equipments) + 2 unnamed placeholders (subsidiary, associate) = 9 entity rows total.

---

## 11. DIGITAL SIGNATURE / SIGNATORY BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 58-68 | Mahabaleshwar Bhat | Company Secretary and Compliance Officer | Digitally signed 2026.08.13, 13:22:06 +05'30' | Board meeting concluded 13:05 (line 37); signature timestamp 13:22:06 is **after** conclusion — no flag (checked per instruction rule 7; this is the expected/correct sequence) |
| 2 | 408-410 | Vijay R Kirloskar | Executive Chairman, DIN 00031253 | Place: Bengaluru; Date: Aug 13, 2026 (no time given) | Time **NOT_FOUND** — cannot verify sequencing vs board meeting conclusion |
| 3 | 553-565 | A. Umesh Patwardhan | Partner, K N Prabhashankar & Co., M.No. 222945 (Standalone review report) | Place: Bengaluru; Date: Aug 13, 2026; UDIN present but OCR-garbled (line 565) | **OCR_ARTIFACT** on UDIN; time NOT_FOUND |
| 4 | 757-768 | A. Umesh Patwardhan | Partner, K N Prabhashankar & Co., M.No. 222945 (Consolidated review report) | Place: Bengaluru; Date: Aug 13, 2026; UDIN present but OCR-garbled (line 768) | **OCR_ARTIFACT** on UDIN; time NOT_FOUND |

Signature blocks: grep (digital-signature / signatory-context anchors) = 4 distinct blocks identified. Manual sweep = 4. Match.

---

## SUMMARY OF FLAGS RAISED

- **ZERO_STANDING** (8 instances): Note 12 (NCD detail — NIL); P&L Exceptional items (qtr columns); Adjustments relating to earlier years (fully blank row); Deferred tax (dash-only row); Remeasurements of defined benefit plans (qtr columns); Taxes on remeasurement (qtr columns); Revaluation gain on land (qtr columns); Other Equity (qtr columns) — plus partial ZERO_STANDING on Current Tax's year-ago-quarter cell and the segment table's "Add: Exceptional item" row (mirrors P&L).
- **SPELLING_VARIANT** (3 entity names): SKG Terra Promenade/Promonede; SLPKG Estate Holdings/Holding; Luxquisite/Luxqusite Parkland.
- **EXTRACTION_GAP** (multiple auditor-report paragraphs, both standalone and consolidated, where the extract text is present but no leading numeral was captured — paragraphs 2-5 standalone, paragraphs 1-5 consolidated by logical position).
- **OCR_ARTIFACT**: P&L sl-no glyphs for rows II and III (page 2); Diluted EPS year-ended figure ("1.2/"); both auditor UDIN strings.
- **OCR_DEGRADED**: entire segment-reporting table (page 3) — standalone/consolidated column values appear interleaved across source lines; labels are reliable, individual value-to-column mapping is not, without source-PDF confirmation.
- **NOT_FOUND**: name of the "associate" and confirmation that the singular "subsidiary" referenced in Note 5/KAM = Kirsons BV; time-of-signing for the Executive Chairman's and both auditor partner's signature blocks.
- Consolidated auditor report para-7 conclusion uses "except for" qualifying language tied to the Other Matters paragraph (foreign-subsidiary conversion) — flagged for A3/A4 interpretation as a possible qualified opinion; not resolved by A2.
- Standalone vs consolidated EOM paragraph numbering diverges ("6." vs "5.") despite consolidated report carrying one additional paragraph (SEBI Reg 33(8) procedures) that would be expected to push its numbering higher, not lower — flagged for A3/A4, not resolved by A2 (extraction gap makes root cause undeterminable from the text alone).
- ENTITY_CHANGE: not applicable — first pipeline run for KECL, no prior-quarter ledger to diff against.
