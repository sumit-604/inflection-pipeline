# A2 ENUMERATION LEDGER — Pace Digitek Ltd (PACEDIGITK), Q1 FY27, Results Filing

Source: `runs/pacedigitk-q1fy27/work/extract_results_pacedigitk_q1fy27.txt` (552 lines, 10 pages,
unit convention: Millions, conversion to Cr: x0.1). Doc = Board Outcome letter (Reg 30) +
Standalone Unaudited Results + Standalone Limited Review Report + Consolidated Unaudited Results
+ Consolidated Limited Review Report. Line numbers below are the extract file's own line numbers
(1:1 with source PDF text order).

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: notes              grep_count: 15   sweep_count: 15   match: yes
category: line_items         grep_count: 61   sweep_count: 61   match: yes
category: zero_standing      grep_count: 5    sweep_count: 5    match: yes
category: auditor_paras      grep_count: 13   sweep_count: 13   match: yes
category: entities           grep_count: 9    sweep_count: 9    match: yes
category: signature_blocks   grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology per category (reproducible commands run against the extract file):
- agenda_items: `grep -inE "AGM|dividend|record date|director appoint|resign|auditor (appoint|change|resign)|scrutinizer|ESOP|preferential|rights issue|capital rais|considered and approved|inter alia"` restricted to letter body (lines 1-75) → 1 hit line (line 44, "inter alia considered and approved").
- notes: `grep -nE "^[0-9]+\s+[0-9]+\.\s"` (accounts for extract's own leading line-number column) → 15 top-level numbered notes (8 standalone + 7 consolidated).
- line_items: `grep -c -E "[0-9]+\.[0-9]{2}"` restricted to lines 157-191 (standalone table, 25 hits) and lines 437-486 (consolidated table, 36 hits) = 61.
- zero_standing: pass 1 `grep -c -E "\s-\s"` on both table ranges = 3 (lone-dash cells); pass 2 `grep -ic "Other equity"` on both table ranges = 2 (blank-quarter standing rows); combined = 5.
- auditor_paras: pass 1 `grep -nE "^[0-9]+\s+(I\.|[0-9]\.)\s"` restricted to each report's line range = 4 (standalone) + 7 (consolidated) = 11 numbered/roman paragraph markers; pass 2 `grep -inE "Other Matters|We also perfonn"` = 2 unnumbered paragraph starts; combined = 13.
- entities: `grep -c -iE "Parent Company|Subsidiar|Ste.*Down"` on the entity table (lines 317-326) = 9.
- signature_blocks: anchor grep `grep -inE "Digitally|Membership No|DIN-|Whole-Time Director|Company Secretary and Compliance|Partner"` grouped into 5 physically distinct blocks by proximity.

---

## A. BOARD OUTCOME LETTER (Reg 30) — pages 1, lines 26-75

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| A1 | 26 | Ref No. | PDL/2026-27/Q02_21, dated August 05, 2026 | note: "Q02" token in ref no. while this is a Q1 FY27 filing — internal ref sequence, not the quarter label |
| A2 | 30-35 | Addressees | BSE Limited (Scrip Code 544550) and NSE (Symbol PACEDIGITK) | |
| A3 | 39-46 | Agenda item 1 (only item) | Board, at meeting held Wed Aug 05 2026, "has inter alia considered and approved the Unaudited Standalone and Consolidated Financial Results along with the Limited Review Report" for Q1 FY27 | AGENDA_ITEM |
| A4 | 48-50 | Opinion confirmation | Company confirms Limited Review Report is "with unmodified opinion" (both Standalone and Consolidated) | |
| A5 | 56 | Board meeting timing | Commenced 12:10 PM IST, concluded 05:30 PM IST — 5 hours 20 minutes | informational: long meeting for a single-agenda results approval |
| A6 | 65-72 | Signature block 1 | Meghana M P, Company Secretary and Compliance Officer, Membership No. A42534. Digitally signed 2026.08.05 17:36:18 +05'30' | SIGNATURE_BLOCK; timestamp is 6 min after board conclusion (17:30) — no before-conclusion flag |

No other agenda items found in letter body: no AR/AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer, no ESOP grant, no capital-raising enabling resolution. Letter covers only the Reg 33 results approval.

---

## B. STANDALONE AUDITOR REPORT (S S Kothari Mehta & Co. LLP) — pages 2, lines 76-141

| # | Line | Para | First ~15 words | Flags |
|---|------|------|------------------|-------|
| B1 | 82-85 | Title | "Independent Auditor's Review Report on Unaudited Quarterly Standalone Financial Results..." pursuant to Reg 33 | |
| B2 | 95-100 | Para I | "We have reviewed the accompanying statement of unaudited standalone financial results of Pace Digitek..." — scope | AUDITOR_PARA |
| B3 | 102-107 | Para 2 | "This Statement, which is the responsibility of the Company's management and approved by the Company's Board..." — Ind AS 34 basis, Companies Act s.133 | AUDITOR_PARA |
| B4 | 109-115 | Para 3 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — review not an audit | AUDITOR_PARA |
| B5 | 117-121 | Para 4 (conclusion) | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." — unmodified conclusion | AUDITOR_PARA; opinion type = unmodified/unqualified |
| B6 | 124-134 | Signature block 2 | For S S Kothari Mehta & Co. LLP, Firm Reg. 000756N/N500441; Amit Goel, Partner, Membership No. 500607; Date Aug 5 2026; Place Delhi; UDIN 26500607MQTQJW8625 | SIGNATURE_BLOCK |

No Emphasis of Matter, no Other Matters, no Going Concern language in the standalone report — clean 4-paragraph unmodified review, single entity (no consolidation, no component-auditor reliance).

---

## C. STANDALONE FINANCIAL RESULTS — Line items (page 3, lines 157-191)

Periods: Q1FY27 (unaud.) | Q4FY26 (audited, refer note-7) | Q1FY26 (unaud.) | FY26 (audited)

| # | Line | Label | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------|--------|--------|--------|------|-------|
| C1 | 158 | (a) Revenue from operations | 2,642.40 | 4,870.37 | 3,396.65 | 17,108.08 | |
| C2 | 159 | (b) Other income | 188.91 | 168.00 | 59.19 | 468.67 | |
| C3 | 160 | Total income (I) | 2,831.31 | 5,038.37 | 3,455.84 | 17,576.75 | subtotal |
| C4 | 162 | (a) Cost of materials consumed | 478.78 | 2,114.12 | 174.60 | 3,519.68 | |
| C5 | 163 | (b) EPC project expenses | 1,298.83 | 1,639.48 | 2,208.76 | 7,965.60 | |
| C6 | 164 | (c) Purchases of stock-in-trade | - | - | 6.78 | 747.02 | ZERO_STANDING (dash Q1FY27 and Q4FY26) |
| C7 | 165 | (d) Employee benefits expense | 250.37 | 213.23 | 155.84 | 764.29 | |
| C8 | 166 | (e) Finance costs | 78.93 | 151.99 | 88.72 | 322.28 | |
| C9 | 167 | (f) Depreciation and amortisation expense | 31.94 | 25.05 | 10.87 | 72.90 | |
| C10 | 168 | (g) Other expenses | 120.03 | 200.83 | 121.06 | 730.14 | |
| C11 | 169 | Total expenses (II) | 2,258.88 | 4,344.70 | 2,766.63 | 14,121.91 | subtotal |
| C12 | 171 | III. Profit before tax (I-II) | 572.43 | 693.67 | 689.21 | 3,454.84 | |
| C13 | 174 | (a) Current tax | 161.65 | 237.14 | 177.29 | 945.08 | |
| C14 | 175 | (b) Deferred tax charge/(credit) | (14.36) | 46.11 | 1.52 | 40.72 | |
| C15 | 176 | (c) Taxes relating to earlier years | - | 4.24 | - | 4.24 | ZERO_STANDING (dash Q1FY27 and Q1FY26) |
| C16 | 177 | Total tax expense (IV) | 147.29 | 287.49 | 178.81 | 990.04 | subtotal |
| C17 | 178 | V. Profit after tax (III-IV) | 425.14 | 406.18 | 510.40 | 2,464.80 | |
| C18 | 181 | (i) Remeasurement of defined benefit plan gain/(loss) | (0.69) | 3.42 | 0.17 | 2.86 | |
| C19 | 182 | (ii) Income tax relating to these items | 0.17 | (0.86) | (0.04) | (0.72) | |
| C20 | 183 | Total OCI for the period/year (net of tax) | (0.52) | 2.56 | 0.13 | 2.14 | subtotal |
| C21 | 184 | VII. Total comprehensive income (V+VI) | 424.62 | 408.74 | 510.53 | 2,466.94 | |
| C22 | 187 | VIII. Paid up equity share capital (FV Rs 2 each) | 431.70 | 431.70 | 356.88 | 431.70 | |
| C23 | 188 | IX. Other equity | (blank) | (blank) | (blank) | 19,272.52 | ZERO_STANDING (blank in all three quarterly columns — standard annual-only presentation of this balance-sheet item, but nil populated per instructions must still be logged) |
| C24 | 190 | X. Basic EPS (Rs, not annualised) | 1.97 | 2.06 | 2.86 | 12.52 | |
| C25 | 191 | X. Diluted EPS (Rs, not annualised) | 1.97 | 2.06 | 2.86 | 12.52 | |

25 line items, 2 flagged ZERO_STANDING (rows C6, C15) plus row C23 (Other equity, blank-quarter standing item) — 3 ZERO_STANDING rows in this table.

---

## D. STANDALONE NOTES (page 4-5, lines 194-266)

| # | Note | Line | First ~15 words | Flags |
|---|------|------|------------------|-------|
| D1 | 1 | 197-201 | "The above unaudited standalone financial results of the Company for the quarter ended June 30, 2026 have been reviewed..." — Audit Committee/Board approval, limited review under Reg 33 | |
| D2 | 2 | 203-205 | "These unaudited standalone financial results of the Company have been prepared in accordance with the Indian Accounting Standards..." | |
| D3 | 3 | 207-210 | "Where financial results contains both consolidated financial results and standalone financial results of the Company, segment information..." — segment info presented only in consolidated per Ind AS-108 | cross-ref: segment table lives in Consolidated Note 1 |
| D4 | 4 | 212-217 | "During the previous year ended March 31, 2026, the Company has completed its Initial Public Offer (IPO) of..." — IPO Rs 8,191.48 mn, 3,74,09,047 shares, fresh issue "3,73,35,967" shares + 55,080 employee shares, listed 06 Oct 2025 | **NUMBER_MISMATCH**: fresh-issue share count here (3,73,35,967) does not reconcile with the stated total (3,74,09,047 − 55,080 employee shares = 3,73,53,967, matching the Consolidated Note 4 figure at line 510, not this one) — see cross-check note below |
| D5 | 5 | 219-221 | "The total proceeds from issue of shares consisted of IPO proceeds of Rs. 8,191.48 million. The offer expenses..." — net proceeds Rs 7,458.34 mn; intro to utilisation table | EXTRACT_GAP: the utilisation table itself (objects of issue vs utilised/unutilised) referenced at line 222 does not appear in the extract — only sub-clauses (a) and (b) below survived; table content is missing from A1 extract and must be sourced from the PDF directly for A3/A4 |
| D5a | 5(a) | 224-226 | "The amount utilized during the current period is based on the fund utilization certificate issued by independent chartered accountant..." dated Jul 31 2026; monitoring agency report by Crisil dated Aug 05 2026 | sub-item of Note 5 |
| D5b | 5(b) | 228-230 | "The unutilized amounts are lying in bank account of Rs. 1,469.00 million that includes the fund lying in the..." bank account of PREPL Rs 514.94 mn | sub-item of Note 5 |
| D6 | 6 | 232-239 | "During the quarter, the Company subscribed to 79,36,507 Equity Shares pursuant to the rights issue of PREPL..." Rs 500.00 mn, Share Subscription Agreement dated Sep 8 2025; PREPL capex to date Rs 4,860.45 mn for BESS project for MSEDCL | **No consolidated-notes equivalent** — this intercompany subscription (parent into subsidiary PREPL) is disclosed only in the Standalone notes; not repeated in Consolidated notes (expected, since it eliminates on consolidation, but flagged so A3/A4 confirm the elimination rather than assume an omission) |
| D7 | 7 | 241-244 | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figures between the audited..." — Q4FY26 balancing-figure explanation | cross-checked against "(Refer note-7)" tag on the Q4FY26 column header at line 156 — consistent |
| D8 | 8 | 246-248 | "The results for the quarter ended June 30, 2026 are available on the Company's website at www.pacedigitek.com..." | |
| D9 | — | 250-266 | Signature block 3: For and on behalf of the Board — Rajiv Maddisetty, Whole-Time Director, DIN-08495070. Digitally signed 2026.08.05 17:34:25 +05'30'; Place Bangalore; Date Aug 05 2026 | SIGNATURE_BLOCK; timestamp is 4 min after board conclusion (17:30) — no before-conclusion flag |

8 top-level notes + 2 sub-items (5a, 5b) = 10 rows; no unnumbered footnotes/asterisks/daggers found elsewhere in this section (checked by sweep).

---

## E. CONSOLIDATED AUDITOR REPORT (S S Kothari Mehta & Co. LLP) — pages 6-7, lines 268-421

| # | Line | Para | First ~15 words | Flags |
|---|------|------|------------------|-------|
| E1 | 275-278 | Title | "Independent Auditor's Review Report on Unaudited Quarterly Consolidated Financial Results of Pace Digitek..." pursuant to Reg 33 | |
| E2 | 287-293 | Para I | "We have reviewed the accompanying statement of unaudited consolidated financial results of Pace Digitek..." (Parent + subsidiaries incl. step-down = "Group") — scope | AUDITOR_PARA |
| E3 | 295-300 | Para 2 | "This Statement, which is the responsibility of the Parent's management and approved by the Parent's Board of..." — Ind AS 34 basis | AUDITOR_PARA |
| E4 | 302-308 | Para 3 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — review not an audit | AUDITOR_PARA |
| E5 | 310-311 | Para 3 (unnumbered continuation) | "We also performed procedures in accordance with the circular issued by the Securities and Exchange Board of India under Regulation 33(8)..." | AUDITOR_PARA (unnumbered) |
| E6 | 313-327 | Para 4 | "The Statement includes the results of the following entities:-" — entity list (see Section F below) | AUDITOR_PARA; ENTITY_LIST |
| E7 | 339 | Heading | "Other Matters" | AUDITOR_PARA (heading, unnumbered) |
| E8 | 342-353 | Para 5 | "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on the..." consideration of other auditor's report per para 6 — conclusion not modified re: reliance | AUDITOR_PARA |
| E9 | 356-372 | Para 6 | "We did not review the interim financial information / financial results of 1 subsidiary..." reviewed by other/component auditor: revenue Rs NIL, net loss after tax Rs 0.04 mn, total comprehensive loss Rs 0.04 mn for Q1FY27; furnished by Management, based solely on other auditor's report | AUDITOR_PARA; COMPONENT_AUDITOR_RELIANCE — revenue reported as "Rs NIL" for this subsidiary |
| E10 | 374-399 | Para 7 | "The Statement includes the interim financial information / financial results of 2 Subsidiaries (including one step-down subsidiary)..." NOT reviewed by any auditor, unaudited and management-furnished: revenue Rs 5.20 mn, net profit after tax Rs 0.75 mn, total comprehensive income Rs 1.57 mn for Q1FY27; "not material to the Group"; conclusion not modified re: reliance | AUDITOR_PARA; UNAUDITED_MANAGEMENT_FURNISHED — 2 entities (incl. 1 step-down) entirely unreviewed |
| E11 | 401-412 | Signature block 4 | For S S Kothari Mehta & Co. LLP, Firm Reg. 000756N/N500441; Amit Goel, Partner, Membership No. 500607; Date Aug 5 2026; Place Delhi; UDIN 26500607VJFNLO5689 | SIGNATURE_BLOCK; UDIN differs from standalone report's UDIN (26500607MQTQJW8625) — correct/expected, two distinct reports same day same partner |

Opinion type = unmodified/unqualified, "not modified with respect to our reliance on the work done and the reports of other auditors and the financial results/financial information certified by the Management" (line 395-399). No Emphasis of Matter, no Going Concern paragraph. 13 total paragraph units in this report (7 numbered/roman + 2 unnumbered continuation/heading + entity-list para counted once + component-auditor reliance detail folded into paras 6/7 above, not separately).

Auditor reports across both statements = B (4 paras) + E (9 paras) = 13 auditor_paras total.

---

## F. CONSOLIDATION ENTITY LIST (Consolidated Auditor Report, Para 4) — lines 313-327

| # | Line | Entity (as printed, OCR artefacts retained) | Relationship | Review status (cross-ref Section E) | Flags |
|---|------|-----------------------------------------------|--------------|--------------------------------------|-------|
| F1 | 317-318 | Pace Digitek Limited (Formerly Pace Digitek Private Limited / Pace Digitek Infra Private Limited) | Parent Company | Reviewed by principal auditor | |
| F2 | 319 | Lineage Power Private Limited | Subsidiary | Reviewed by principal auditor (by elimination — not named in para 6 or para 7) | |
| F3 | 320 | Pace Renewable Energies Private Limited (PREPL) | Subsidiary | Reviewed by principal auditor (by elimination) | Cross-ref Standalone Note 6 (intercompany rights-issue subscription into PREPL) |
| F4 | 321 | Inso Pace Private Limited | Subsidiary | Reviewed by principal auditor (by elimination) | |
| F5 | 322 | TransGreenx Energy Private Limited | Subsidiary | Reviewed by principal auditor (by elimination) | |
| F6 | 323 | Lineage Defence and Aerospace Private Limited | Subsidiary | Reviewed by principal auditor (by elimination) | |
| F7 | 324 | Pace Ecoplanet Solace Private Limited | Subsidiary | Reviewed by principal auditor (by elimination) | |
| F8 | 325 | Lineage Power Holdings (Singapore) Pte Limited | Subsidiary | One of the entities in the "1 subsidiary reviewed by other auditor" (para 6) OR one of the "2 unreviewed" (para 7) — not individually named against para 6/7; A3/A4 should confirm which entity maps to which review status against source PDF | UNRESOLVED_MAPPING |
| F9 | 326 | Lineage Power Myanmar Limited | Step-Down Subsidiary | Likely one of the "2 Subsidiaries (including one step-down)" unreviewed group in para 7, given it is the only step-down entity listed | UNRESOLVED_MAPPING |

9 entities total (1 Parent + 7 Subsidiaries + 1 Step-Down Subsidiary). No prior-quarter entity list was provided to this run (PRIOR_LEDGER_PATH not supplied) — ENTITY_CHANGE diff cannot be performed this run; flag as N/A rather than silently skipped.

Note: para 6 (1 subsidiary, revenue Rs NIL, reviewed by other/component auditor) and para 7 (2 subsidiaries incl. 1 step-down, revenue Rs 5.20 mn total, unreviewed) together account for 3 of the 9 listed entities by review status; the other 6 (Parent + 5 subsidiaries) are reviewed directly by the principal auditor. The specific entity-to-status mapping for F8/F9 is not stated verbatim in the extract and should be confirmed against the source PDF by A3/A4 (flag UNRESOLVED_MAPPING, not a mechanical failure).

---

## G. CONSOLIDATED FINANCIAL RESULTS — Line items (page 8, lines 437-486)

Periods: Q1FY27 (unaud.) | Q4FY26 (audited, refer note-6) | Q1FY26 (unaud.) | FY26 (audited)

| # | Line | Label | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------|--------|--------|--------|------|-------|
| G1 | 438 | (a) Revenue from operations | 5,553.64 | 10,967.79 | 3,670.79 | 26,412.70 | |
| G2 | 439 | (b) Other income | 283.41 | 201.53 | 56.36 | 461.08 | |
| G3 | 440 | Total income (I) | 5,837.05 | 11,169.32 | 3,727.15 | 26,873.78 | subtotal |
| G4 | 442 | (a) Cost of materials consumed | 3,753.16 | 6,414.71 | 396.55 | 8,384.23 | |
| G5 | 443 | (b) EPC project expenses | 974.54 | 1,755.67 | 2,248.67 | 8,807.61 | |
| G6 | 444 | (c) Purchases of stock-in-trade | 3.25 | 321.69 | 60.58 | 2,783.69 | not zero — has values in all four periods |
| G7 | 445 | (d) Changes in inventories | (732.23) | (15.24) | (205.76) | (328.21) | |
| G8 | 446 | (e) Employee benefits expense | 332.63 | 271.78 | 197.58 | 959.00 | |
| G9 | 447 | (f) Finance costs | 283.41 | 342.87 | 97.23 | 598.23 | |
| G10 | 448 | (g) Depreciation and amortisation expense | 44.37 | 32.28 | 20.87 | 120.04 | |
| G11 | 449 | (h) Other expenses | 361.63 | 587.43 | 172.64 | 1,253.90 | |
| G12 | 450 | Total expenses (II) | 5,020.76 | 9,711.19 | 2,988.36 | 22,578.49 | subtotal |
| G13 | 451 | III. Profit before tax (I-II) | 816.29 | 1,458.13 | 738.79 | 4,295.29 | |
| G14 | 454 | (a) Current tax expense | 191.13 | 278.96 | 192.14 | 1,125.18 | |
| G15 | 455 | (b) Deferred tax (credit)/charge | 0.11 | 112.81 | (0.33) | 90.32 | |
| G16 | 456 | (c) Taxes relating to earlier years | - | 7.15 | - | 7.15 | ZERO_STANDING (dash Q1FY27 and Q1FY26) |
| G17 | 457 | Total tax expense (IV) | 191.24 | 398.92 | 191.81 | 1,222.65 | subtotal |
| G18 | 458 | V. Profit after tax (III-IV) | 625.05 | 1,059.21 | 546.98 | 3,072.64 | |
| G19 | 462 | A(i) Remeasurement of defined benefit plans gain/(loss) | (4.32) | (2.08) | 0.05 | (4.71) | |
| G20 | 463 | A(ii) Income tax relating to these items | 1.09 | 0.52 | (0.01) | 1.18 | |
| G21 | 465 | B(i) Exchange differences on translation of foreign operations | 0.82 | 0.58 | 0.15 | 0.80 | |
| G22 | 466 | Total OCI for the period/year (net of tax) | (2.41) | (0.98) | 0.19 | (2.73) | subtotal |
| G23 | 467 | VII. Total comprehensive income (V+VI) | 622.64 | 1,058.23 | 547.17 | 3,069.91 | |
| G24 | 469 | VIII. Profit attributable to: Owners of the Company | 613.23 | 991.62 | 541.50 | 2,975.68 | |
| G25 | 470 | Profit attributable to: Non-controlling interest | 11.82 | 67.59 | 5.48 | 96.96 | |
| G26 | 471 | Profit after tax for the period/year (total, restated) | 625.05 | 1,059.21 | 546.98 | 3,072.64 | ties to G18 |
| G27 | 473 | IX. OCI attributable to: Owners of the Company | (1.88) | 0.05 | 0.20 | (1.60) | |
| G28 | 474 | OCI attributable to: Non-controlling interest | (0.53) | (1.03) | (0.02) | (1.13) | |
| G29 | 475 | Other comprehensive income for the period/year (total) | (2.41) | (0.98) | 0.19 | (2.73) | ties to G22 |
| G30 | 477 | X. Total comprehensive income attributable to: Owners | 611.35 | 991.68 | 541.70 | 2,974.08 | |
| G31 | 478 | Total comprehensive income attributable to: Non-controlling interest | 11.29 | 66.55 | 5.46 | 95.83 | |
| G32 | 479 | Total comprehensive income attributable (VIII+IX) | 622.64 | 1,058.23 | 547.16 | 3,069.91 | note: FY26 total 547.16 vs G23's FY26 547.17 — 0.01 rounding diff |
| G33 | 481 | Paid-up equity share capital (FV Rs 2 each) | 431.70 | 431.70 | 356.88 | 431.70 | |
| G34 | 482 | Other equity | (blank) | (blank) | (blank) | 21,641.28 | ZERO_STANDING (blank in all three quarterly columns — annual-only presentation) |
| G35 | 485 | XI. Basic EPS (Rs, not annualised) | 2.84 | 5.04 | 3.03 | 15.11 | |
| G36 | 486 | XI. Diluted EPS (Rs, not annualised) | 2.84 | 5.04 | 3.03 | 15.11 | |

36 line items, 2 flagged ZERO_STANDING (rows G16, G34) directly; G32/G23 rounding note is a separate MINOR_ROUNDING flag, not zero-standing.

---

## H. CONSOLIDATED NOTES (pages 9-10, lines 488-552)

| # | Note | Line | First ~15 words | Flags |
|---|------|------|------------------|-------|
| H1 | 1 | 490-494 | "Consolidated segment wise information for the quarter ended June 30, 2026" | **EXTRACT_GAP**: heading present but the segment table itself is entirely absent from the extract (lines 491-494 blank) — segment revenue/results/assets by segment cannot be verified from this extract; A3/A4 must pull segment figures from the source PDF directly. This is also the segment disclosure that Standalone Note 3 (D3 above) explicitly defers to. |
| H2 | 2 | 495-498 | "The above unaudited consolidated financial results of the Company for the quarter ended June 30, 2026 have been..." — Audit Committee/Board approval, limited review under Reg 33 | mirrors D1 |
| H3 | 3 | 500-502 | "These unaudited consolidated financial results of the Company have been prepared in accordance with the Indian Accounting..." | mirrors D2 |
| H4 | 4 | 506-513 | "During the previous year ended March 31, 2026, the Company has completed its Initial Public Offer (IPO) of Rs...." — IPO Rs 8,191.48 mn, 3,74,09,047 shares, fresh issue "3,73,53,967" shares + 55,080 employee shares, listed 06 Oct 2025 | **NUMBER_MISMATCH** vs Standalone Note 4 (D4 above): this figure (3,73,53,967) reconciles arithmetically with the stated total (3,74,09,047 − 55,080 = 3,73,53,967); the Standalone Note 4 figure (3,73,35,967) does not. Standalone Note 4 appears to contain the transposed/incorrect digit sequence. |
| H5 | 5 | 515-517 | "The total proceeds from issue of shares consisted of IPO proceeds of Rs. 8,191.48 million. The offer expenses..." — net proceeds Rs 7,458.34 mn; intro to utilisation table | EXTRACT_GAP: utilisation table (lines 518-521) blank in extract, mirrors D5 |
| H5a | 5(a) | 522-524 | "The amount utilized during the current period is based on the fund utilization certificate issued by independent chartered..." dated Jul 31 2026; Crisil monitoring report dated Aug 05 2026 | sub-item of Note 5; identical wording to D5a |
| H5b | 5(b) | 526-528 | "The unutilized amounts are lying in bank account of Rs. 1,469.00 million that includes the fund lying in the..." bank account of PREPL Rs 514.94 mn | sub-item of Note 5; identical wording to D5b |
| H6 | 6 | 530-532 | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figures between the audited..." — Q4FY26 balancing-figure explanation | cross-checked against "(Refer note-6)" tag on the Q4FY26 column header at line 436 — consistent |
| H7 | 7 | 534-536 | "The results for the quarter ended June 30, 2026 are available on the Company's website at www.pacedigitek.com and..." | mirrors D8 |
| H8 | — | 540-551 | Signature block 5: For and on behalf of the Board — Rajiv Maddisetty, Whole-Time Director, DIN-08495070. Digitally signed 2026.08.05 17:35:20 +05'30'; Place Bangalore; Date Aug 5 2026 | SIGNATURE_BLOCK; timestamp is 5 min after board conclusion (17:30) — no before-conclusion flag |

7 top-level notes + 2 sub-items (5a, 5b) = 9 rows. Note numbering shifted by 1 vs Standalone (segment note occupies slot 1 here, absorbing the slot Standalone used for its "segment info is in consolidated" cross-reference note); Standalone Note 6 (PREPL rights-issue subscription, D6) has no Consolidated counterpart — see D6 flag.

---

## SUMMARY OF FLAGS RAISED

| Flag | Location(s) | Note |
|------|-------------|------|
| AGENDA_ITEM | A3 | Single agenda item in Board Outcome letter |
| ZERO_STANDING | C6, C15, C23, G16, G34 | 5 rows — dash or blank standing items, none dropped |
| SIGNATURE_BLOCK | A6, B6, D9, E11, H8 | 5 signature blocks; all digital timestamps fall after board meeting conclusion (17:30 IST) — no before-conclusion violation |
| AUDITOR_PARA | B2-B5, E2-E10 | 13 total auditor report paragraphs across both reports; both opinions unmodified/unqualified |
| COMPONENT_AUDITOR_RELIANCE | E9 | 1 subsidiary reviewed by other/component auditor, revenue Rs NIL |
| UNAUDITED_MANAGEMENT_FURNISHED | E10 | 2 subsidiaries (incl. 1 step-down) entirely unreviewed, management-furnished, "not material to the Group" |
| ENTITY_LIST / UNRESOLVED_MAPPING | F8, F9 | Entity-to-review-status mapping for 2 of 9 entities not verbatim in extract; confirm against source PDF |
| EXTRACT_GAP | D5 (utilisation table), H1 (segment table), H5 (utilisation table) | 3 tables referenced but not captured in the A1 extract — cannot be verified from this ledger alone |
| NUMBER_MISMATCH | D4 vs H4 | Standalone Note 4 fresh-issue share count (3,73,35,967) does not reconcile with stated IPO total; Consolidated Note 4 (3,73,53,967) does. Likely a transposition error in the Standalone note. |
| MINOR_ROUNDING | G32 vs G23 | FY26 total comprehensive income attributable (547.16) vs total comprehensive income (547.17) — Rs 0.01 mn rounding diff |
| N/A (ENTITY_CHANGE not testable) | Section F | No prior-quarter ledger/entity list supplied to this run |

END OF LEDGER.
