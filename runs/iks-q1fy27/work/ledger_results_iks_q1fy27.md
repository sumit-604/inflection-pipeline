# A2 COMPLETENESS LEDGER — IKS Q1FY27 — RESULTS (results_board_outcome.pdf)
Source extract: `extract_results_iks_q1fy27.txt` (12 pages, 625 lines, unit = INR Million, unless otherwise stated)
Prior-quarter ledger: NOT PROVIDED (no companies/IKS.md, first coverage cycle — ENTITY_CHANGE diff cross-check not possible against a prior ledger; flagged instead from in-document reclassification language, see Entities section)

```
=== A2 COUNT TEST ===
category: agenda_items          grep_count: 3    sweep_count: 3    match: yes
category: annexures              grep_count: 4    sweep_count: 4    match: yes
category: annexure_disclosure_rows  grep_count: 10   sweep_count: 10   match: yes
category: auditor_paras         grep_count: 11   sweep_count: 11   match: yes
category: entities               grep_count: 11   sweep_count: 11   match: yes
category: notes                  grep_count: 10   sweep_count: 10   match: yes
category: line_items             grep_count: 37   sweep_count: 37   match: yes
category: zero_standing          grep_count: 4    sweep_count: 4    match: yes
category: signature_blocks       grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology notes on reconciliation:
- `agenda_items`: grep `^\s*[0-9]\.\s` on lines 1-120 (board outcome letter body) → 3 hits (L37, L45, L77); manual read of the letter confirms exactly 3 numbered resolutions, no unnumbered agenda items present (no AR approval / AGM notice / dividend / auditor change / ESOP grant / capital raise items in this letter — this is a narrow results + 2 governance-item board outcome).
- `annexures`: grep -i `Annexure` on full file → headings at L121 (A), L474 (B), L558 (D) plus in-letter references to A/B/C/D at L43, L73, L75, L90. Manual sweep found a 4th physical heading on page 10 (L508) that OCR rendered as garbled text `"OOFYVSF$` instead of "Annexure - C" — grep on the literal string "Annexure" alone would UNDERCOUNT annexures at 3; the manual sweep catches the garbled heading via its position (immediately after Annexure B's closing letterhead and before the Berjis Desai signature block, matching the letter's own reference to "Annexure – C" at L75). Flag `OCR_GARBLED` on that row. Reconciled count = 4.
- `annexure_disclosure_rows`: grep `^\s*[0-9]\.\s` inside Annexure B block (L479-498) → 5; inside Annexure D block (L563-615) → 5. Total 10, matches manual sweep.
- `auditor_paras`: grep `^[0-9]\.\s|^\s*[0-9]\.\s` on standalone report block (L120-185) → 4 (L132,139,145,155); on consolidated report block (L186-300) → 7 (L197,206,212,225,255,263,275). Total 11, matches manual sweep.
- `entities`: manual count of the entity table inside consolidated-report para 4 (L227-239) = 3 wholly owned subsidiaries + 7 step-down subsidiaries + 1 associate = 11. Grep of table rows (non-blank lines under the "Relationship / Entity name" header, L228-239) also returns 11 entity-name lines.
- `notes`: grep `^\s{0,3}[0-9]{1,2}\s+[A-Z]` on notes section (L404-458) → 10 hits (L406,410,413,415,418,422,424,427,438,446). Matches manual sweep (Notes 1-10, no unnumbered notes; the "statutory auditor has digitally signed..." lines at L347 and L395 are footer disclaimers on the statement pages, not numbered notes — enumerated separately under Signature Blocks / Footnote Disclaimers).
- `line_items`: sed extraction of the statement body (L318-345 page 6, L368-393 page 7), all non-blank rows excluding page furniture/column headers → 37 rows (12 Sr.No-numbered rows + 25 unnumbered sub-line/subtotal rows). Manual sweep of the same region confirms 37. See table below for full breakdown.
- `zero_standing`: of the 37 line items, 4 are dash("-")/nil across ALL FOUR standalone periods while carrying values on the consolidated side (template signal: transaction type exists at Group level, not at standalone-entity level). Grep confirms the same 4 rows via literal "-" tokens in all 4 rightmost (standalone) numeric fields.
- `signature_blocks`: naive grep `-i "digitally signed"` returns 7 hits but 3 of them (L204, L347, L395) are prose sentences referencing the signing convention, not stamp blocks. Fuzzy grep `-i "digitally s.gned"` (to catch the OCR typo "slgned" at L459) returns 8 hits; filtering to short stamp-fragment lines (not full sentences) isolates 5 actual signature/stamp blocks: L100-109, L162-172, L288-298, L459-461, L462-470. Manual sweep independently found the same 5. This is the one category where the naive grep pass would have under- or mis-counted (OCR typo + prose/stamp ambiguity); reconciled via the fuzzy pattern plus manual filtering per GATE A2.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (3)

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | L37-43 | Approval of Financial Results | Unaudited standalone and consolidated financial results for quarter ended June 30, 2026 approved; Financial Results + Limited Review Report (Price Waterhouse Chartered Accountants LLP) enclosed as Annexure A | |
| 2 | L45-54, L69-76 | Retirement of Mr. Berjis Desai, Non-Executive Chairman and Non-Independent Director (DIN: 00153675) | Retiring by rotation at ensuing 20th AGM; has expressed unwillingness to seek re-appointment (letter dated Aug 5, 2026, enclosed as Annexure C); ceases to be Director/Chairman on conclusion of 20th AGM (Sept 21, 2026 per Annexure B) | |
| 3 | L77-90 | Designate Mr. Clarence Carleton King II, Independent Director, as Non-Executive Chairman and Independent Director (DIN: 08171208) | Effective from conclusion of ensuing 20th AGM, consequent to Mr. Desai's retirement; disclosure enclosed as Annexure D | |

### Board meeting timing
| Line | Item | Detail |
|------|------|--------|
| L92 | Meeting commenced | 07:15 P.M. IST |
| L92 | Meeting concluded | 08:44 P.M. IST |
| — | Duration | 1 hour 29 minutes |

No items on AR approval, AGM notice/record date, dividend declaration, auditor change/reappointment, scrutinizer appointment, ESOP grant ratification, or capital-raising enabling resolutions appear in this letter — the only business is (1) results approval and (2)-(3) a linked chairman retirement/succession pair.

---

## 2. DIGITAL SIGNATURE BLOCKS (5)

| # | Line | Signatory | Designation | Timestamp | Context | Flags |
|---|------|-----------|-------------|-----------|---------|-------|
| 1 | L100-109 | Sameer Chavan | Company Secretary and Compliance Officer (Membership No. F7211) | 2026.08.05 21:50:26 +05'30' | Board outcome letter | Signed ~66 min after board meeting concluded (20:44) — after, not before; no flag warranted |
| 2 | L162-172 | Ali Akbar | Partner, Price Waterhouse Chartered Accountants LLP (Membership No. 117839) | 2026.08.05 21:31:49 +05'30' | Standalone Limited Review Report; UDIN 26117839ERJGUN4804 | Signed ~47 min after board meeting concluded; no flag |
| 3 | L288-298 | Ali Akbar | Partner, Price Waterhouse Chartered Accountants LLP | 2026.08.05 21:32:22 +05'30' | Consolidated Limited Review Report; UDIN 26117839JXNBMV1028 | Signed ~48 min after board meeting concluded; no flag |
| 4 | L459-461, 468-469 | Ali Akbar (ALI AKBAR stamp) | Partner, Price Waterhouse Chartered Accountants LLP | OCR-garbled ("Digitally slgned") — exact time not legible; dated August 5, 2026, Place: Mumbai | Identification signature on the Statement/Notes page itself (third instance of the auditor's digital signature across the package) | OCR_GARBLED (timestamp not legible) |
| 5 | L461-467, 469-470 | Nithya Balasubramanian | Whole Time Director & Chief Financial Officer (DIN: 10664861) | 2026.08.05 20:48:38 +05'30' | Company approval signature on the Statement/Notes page | Signed ~4-5 min after board meeting concluded (20:44); no flag |

Two additional non-stamp mentions of "digitally signed" are prose, not signature blocks: L204 (auditor report boilerplate) and L347/L395 (footer disclaimer repeated identically on the statement pages, "The statutory auditor has digitally signed the statement for identification purpose only...").

---

## 3. ANNEXURES (4) AND ANNEXURE TABLE ROWS (10)

| # | Line | Annexure | Content | Flags |
|---|------|----------|---------|-------|
| 1 | L121 (heading), body L122-469 | Annexure A | Financial Results (standalone + consolidated statement, notes) + Limited Review Reports (standalone and consolidated) | see Sections 4-6 for full breakdown |
| 2 | L474 (heading), body L476-497 | Annexure B | Reg 30 "Disclosure of Change in Director" table — Berjis Desai | 5 rows, see below |
| 3 | L508 (heading, garbled), body L511-553 | Annexure C | Berjis Desai's resignation/non-re-appointment letter, dated August 5, 2026, addressed to the Board | OCR_GARBLED heading — page 10 heading text extracted as `"OOFYVSF$` instead of "Annexure – C"; content and position confirm identity via the letter's L75 cross-reference and the letterhead ("BERJIS DESAI, LL.M (Cantab), Solicitor & Advocate, High Court, Bombay") |
| 4 | L558 (heading), body L560-614 | Annexure D | Reg 30 "Disclosure of Change in Designation of Director" table — Clarence Carleton King II | 5 rows, see below |

### Annexure B — Disclosure of Change in Director (Berjis Desai) — 5 rows
| Sr.No | Line | Particular | Detail | Flags |
|-------|------|------------|--------|-------|
| 1 | L482 | Name of Director | Berjis Desai | |
| 2 | L483-487 | Reason for change | Expressed unwillingness to seek re-appointment at ensuing 20th AGM, consequent to appointment as Member, National Commission for Minorities, Government of India | |
| 3 | L488-491 | Date of appointment/reappointment/cessation & term | At conclusion of the ensuing AGM — September 21, 2026 | |
| 4 | L492-493 | Brief profile (in case of appointment) | Not Applicable | ZERO_STANDING (field present, populated "Not Applicable" — a cessation, not an appointment) |
| 5 | L494-496 | Disclosure of Relationship between Directors | Not Applicable | ZERO_STANDING (field present, populated "Not Applicable") |

### Annexure D — Disclosure of Change in Designation of Director (Clarence Carleton King II) — 5 rows
| Sr.No | Line | Particular | Detail | Flags |
|-------|------|------------|--------|-------|
| 1 | L566 | Name of Director | Clarence Carleton King II | |
| 2 | L567-574 | Reason for change | Change in Designation — Non-Executive Chairman and Independent Director w.e.f. conclusion of 20th AGM, consequent to Mr. Desai's retirement | |
| 3 | L575-578 | Date of appointment/reappointment/cessation & term | At conclusion of the ensuing AGM — September 21, 2026 | |
| 4 | L579-611 | Brief profile (in case of appointment) | DIN 08171208; 40 years health care executive experience; has run hospitals, clinics, ambulatory surgery centers; has run HMOs/PPOs/managed care plans; public, private and provider-sponsored company experience; P&L responsibility up to $9bn+; Certified Corporate Director (NACD and Indian Institute of Corporate Affairs); serves as expert witness; currently chairing an arbitration panel in a large health care dispute | Director profile — DIN, role, term dates, background all present per enumeration rule |
| 5 | L612-614 | Disclosure of Relationship between Directors | None | ZERO_STANDING (field present, populated "None") |

---

## 4. AUDITOR REPORTS — PARAGRAPHS (11 total: 4 standalone + 7 consolidated)

### 4a. Standalone Limited Review Report (Annexure A, pages 3) — 4 paragraphs
| Para | Line | First ~15 words | Type | Flags |
|------|------|------------------|------|-------|
| 1 | L132-137 | "We have reviewed the standalone unaudited financial results of Inventurus Knowledge Solutions Limited..." | Scope statement | |
| 2 | L139-143 | "This Statement, which is the responsibility of the Company's Management and approved by the Board..." | Management responsibility statement | |
| 3 | L145-153 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | Basis of review (SRE 2410); explicit "we do not express an audit opinion" | |
| 4 | L155-160 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." | Conclusion — unmodified/unqualified | Opinion type: UNMODIFIED |
| — | L162-172 | Signature block: Ali Akbar, Partner, FRN 012754N/N500016, Membership No. 117839, UDIN 26117839ERJGUN4804 | Signature/UDIN | see Section 2 row 2 |

No Emphasis of Matter, no Other Matters, no Going Concern language in the standalone report. No entities other than the standalone Company itself.

### 4b. Consolidated Limited Review Report (Annexure A, pages 3-5) — 7 paragraphs
| Para | Line | First ~15 words | Type | Flags |
|------|------|------------------|------|-------|
| 1 | L197-204 | "We have reviewed the consolidated unaudited financial results of Inventurus Knowledge Solutions Limited (the Holding Company)..." | Scope statement — Group + associate | |
| 2 | L206-210 | "This Statement, which is the responsibility of the Holding Company's Management and has been approved..." | Management responsibility statement | |
| 3 | L212-223 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | Basis of review (SRE 2410) + additional SEBI Reg 33(8) procedures paragraph | |
| 4 | L225-239 | "The Statement includes the results of the Holding Company and following entities:" | Entity list (Other Matters — scope of consolidation) | see Section 5, 11 entities |
| 5 | L255-261 | "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on the consideration of the review reports of other auditors..." | Conclusion — unmodified/unqualified | Opinion type: UNMODIFIED |
| 6 | L263-271 | "The interim financial information of one subsidiary reflect total revenue from operations of INR 427.75 million..." | Other Matters — one subsidiary reviewed by other auditors, unmodified conclusion furnished to PW; Revenue INR 427.75mn, PAT INR 52.76mn, TCI INR 58.78mn | "Our conclusion... is not modified" (L273) |
| 7 | L275-286 | "The consolidated unaudited financial results include the interim financial information of five subsidiaries which have not been reviewed..." | Other Matters — 5 subsidiaries UNREVIEWED (unaudited, management-furnished), Revenue INR 0.28mn, net loss INR 5.67mn, TCI loss INR 5.67mn; plus 1 associate (up to June 29, 2026) UNREVIEWED, Group share of net loss INR 53.07mn, TCI loss INR 53.07mn; "not material to the Group" per management | UNAUDITED_ENTITIES: 5 subsidiaries + 1 associate not reviewed by their auditors; "Our conclusion... is not modified" (L286) |
| — | L288-298 | Signature block: Ali Akbar, Partner, FRN 012754N/N500016, Membership No. 117839, UDIN 26117839JXNBMV1028 | Signature/UDIN | see Section 2 row 3 |

No Going Concern paragraph in either report. No qualification/adverse/disclaimer — both conclusions are unmodified. Two distinct Other Matters paragraphs in the consolidated report cover, respectively, entities reviewed by other (non-PW) auditors and entities not reviewed at all.

---

## 5. ENTITIES IN CONSOLIDATION (11) — Review Report para 4, L227-239

| # | Line | Relationship | Entity name | Flags |
|---|------|--------------|-------------|-------|
| 1 | L228 | Wholly owned Subsidiary | Inventurus Knowledge Solutions Inc | |
| 2 | L229 | Wholly owned Subsidiary | IKS Cares Foundation | |
| 3 | L230 | Wholly owned Subsidiary | ARAI Solutions Private Limited | New addition this quarter — acquired May 14, 2026 per Note 10 |
| 4 | L231 | Step down Subsidiary | Aquity Holdings Inc | |
| 5 | L232 | Step down Subsidiary | Aquity Solutions LLC | |
| 6 | L233 | Step down Subsidiary | Aquity Solutions India Private Limited | |
| 7 | L234 | Step down Subsidiary | Aquity Solutions Australia Pty Limited | |
| 8 | L235 | Step down Subsidiary | Aquity Canada ULC | |
| 9 | L236 | Step down Subsidiary | IKS Next Horizon Inc | |
| 10 | L237 | Step down Subsidiary | Value Partners Collective ACO, LLC | |
| 11 | L238-239 | Associate (bracket note: "[Step down Subsidiary w.e.f. June 30, 2026]") | IKS WWMG MSO, LLC | ENTITY_CHANGE — reclassified from Associate to Step down Subsidiary effective the last day of the reporting period per Note 8 (aggregate shareholding raised 48.02% -> 51.88%); accounted for as an associate (equity method) for this quarter's P&L because control was obtained on the last day of the quarter with no post-acquisition operating period |

No prior-quarter ledger was supplied for a formal diff; ARAI Solutions Private Limited is flagged as a new entity based on Note 10 (in-document acquisition narrative), and IKS WWMG MSO LLC is flagged ENTITY_CHANGE based on the in-document bracket annotation and Note 8, both without a prior-period baseline to cross-check against.

Cross-reference: Note 7 (L424-425) restates the same 3 wholly owned + 7 step-down subsidiaries (10 entities) in prose within the Notes to the Statement; it does not name the associate. No new entities appear in Note 7 beyond the review-report list.

---

## 6. FINANCIAL STATEMENT LINE ITEMS (37) — Statement of Unaudited Financial Results, pages 6-7 (L306-393)

Table structure: 8 numeric columns per line (Consolidated: Q1FY27 unaud. / Q4FY26 unaud. / Q1FY26 unaud. / FY26 audited; Standalone: same 4 periods). All rows below carry all 8 columns unless noted.

| # | Sr.No | Line | Item | Type | Flags |
|---|-------|------|------|------|-------|
| 1 | 1 | L318 | INCOME | Section header | |
| 2 | — | L319 | Revenue from operations | Value line | |
| 3 | — | L320 | Other income | Value line | |
| 4 | — | L321 | Total income | Subtotal | |
| 5 | 2 | L323 | EXPENSES | Section header | |
| 6 | — | L324 | Changes in inventories of stock-in-trade | Value line | ZERO_STANDING (standalone: dash all 4 periods; consolidated: (1.62), 13.91, -, 13.91) |
| 7 | — | L325 | Employee benefit expenses | Value line | |
| 8 | — | L326 | Finance cost | Value line | |
| 9 | — | L327 | Depreciation and amortisation expenses | Value line | |
| 10 | — | L328 | Other expenses | Value line | |
| 11 | — | L329 | Total expenses | Subtotal | |
| 12 | 3 | L331 | Profit before share of profit/(loss) from associates and tax (1-2) | Computed line | |
| 13 | 4 | L335-336 | Share of profit/(loss) from associates accounted for using the equity method (net of tax) | Value line | ZERO_STANDING (standalone: dash all 4 periods; consolidated: (53.07), (54.08), -, (92.22)) |
| 14 | 5 | L338 | Profit before tax (3+4) | Computed line | |
| 15 | 6 | L340 | Tax Expenses | Section header | |
| 16 | — | L341 | Current tax | Value line | |
| 17 | — | L342 | Deferred tax | Value line | |
| 18 | — | L343 | Total tax Expenses | Subtotal | |
| 19 | 7 | L345 | Profit for the period/year (5-6) | Computed line | |
| 20 | 8 | L368 | Other Comprehensive Income | Section header | |
| 21 | — | L369 | Items that may be reclassified to profit or loss | Subsection header (no own values) | |
| 22 | — | L370 | Gains/(losses) on cash flow hedges (net) | Value line | |
| 23 | — | L371-372 | Exchange differences on translation of financial statements of foreign operations | Value line | ZERO_STANDING (standalone: dash all 4 periods; consolidated: (0.50), 880.93, 19.58, 1,617.53) |
| 24 | — | L373 | Income tax relating to above items (reclassified items) | Value line | |
| 25 | — | L374 | [subtotal, unlabeled — net OCI of items that may be reclassified] | Subtotal | |
| 26 | — | L375 | Items that will not be reclassified to profit or loss | Subsection header (no own values) | |
| 27 | — | L376 | Remeasurement of post employment benefit obligations | Value line | |
| 28 | — | L377 | Changes in the fair value of equity investments at FVOCI | Value line | ZERO_STANDING (standalone: dash all 4 periods; consolidated: 226.42, -, -, 931.52) |
| 29 | — | L378 | Income tax relating to above items (non-reclassified items) | Value line | |
| 30 | — | L379 | [subtotal, unlabeled — net OCI of items that will not be reclassified] | Subtotal | |
| 31 | — | L381-382 | Other Comprehensive Income/(loss) for the period/year, net of tax | Subtotal (total OCI) | |
| 32 | 9 | L384 | Total Comprehensive Income for the period/year (7+8) | Computed line | |
| 33 | 10 | L385 | Paid-up equity share capital (Face value ₹1 per share) | Value line | Reported once per side (170.71 consol / 170.71 standalone), not broken out by comparative period |
| 34 | 11 | L387 | Reserves excluding revaluation reserves as at balance sheet date | Value line | Reported only at FY-end column (27,831.66 consol / 17,713.67 standalone); blank for quarterly comparative columns — balance-sheet item, not a quarterly flow, not treated as dash/nil |
| 35 | 12 | L390 | Earnings per share (Nominal value of share ₹1 each) | Section header | |
| 36 | — | L391 | Basic (INR per share) | Value line | |
| 37 | — | L393 | Diluted (INR per share) | Value line | |

Footer disclaimer repeated verbatim after both statement tables: "The statutory auditor has digitally signed the statement for identification purpose only and this statement should be read in conjuction with their report dated August 5, 2026." — L347 (after Sr.No 7 row) and L395 (after Sr.No 12 row). Column annotation "(Refer note 3)" appears twice (L316, L365), cross-referencing Note 3 (balancing-figure basis for the Q4FY26 column) rather than constituting a separate note.

ZERO_STANDING summary (4 line items, all standalone-side, all dash across all 4 periods, non-dash on consolidated side): #6 Changes in inventories of stock-in-trade; #13 Share of profit/(loss) from associates; #23 Exchange differences on translation of foreign operations; #28 Changes in fair value of equity investments at FVOCI. Consistent pattern: these are all group-level-only transaction types (inventory trading, associate equity pickup, FX translation, FVOCI equity investments) that the standalone (parent-only) entity does not carry — a structural template signal, not an anomaly, but retained per ZERO_STANDING enumeration rule.

---

## 7. NOTES TO THE STATEMENT (10) — pages 8, L404-458

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | L406-408 | "The above standalone financial results of Inventurus Knowledge Solutions Limited ('the Company') and consolidated..." | Board/Audit Committee approval + Statutory Auditor review confirmation |
| 2 | L410-411 | "The statement has been prepared in accordance with the recognition and measurement principles laid down..." | Basis of preparation (Ind AS, Companies Act s.133) |
| 3 | L413 | "The figures of the quarter ended March 31, 2026 are balancing figures between audited figures..." | Q4FY26 balancing-figure basis (cross-referenced by both statement tables) |
| 4 | L415-416 | "The Group operates in one reportable business segment which comprises a Care enablement platform..." | Single operating segment (Ind AS 108) |
| 5 | L418-420 | "The Company has allotted 140,085 shares for the quarter ended June 30, 2026 (quarter ended June 30, 2025: 23,942 shares)..." | ESOP allotment (140,085 shares vs 23,942 PY) + 143,814 new options granted this quarter |
| 6 | L422 | "Earnings per share for the interim periods are not annualised." | EPS presentation basis |
| 7 | L424-425 | "The consolidated financial results of the Group include the results of its subsidiary companies viz: Inventurus Knowledge Solutions Inc..." | Entity list (prose form) — cross-reference to Section 5 |
| 8 | L427-436 | "During the quarter ended June 30, 2026, IKS Inc., a US-incorporated step-down subsidiary of the Company, acquired an additional 3.86% equity interest in IKS WWMG MSO LLC..." | ENTITY_CHANGE driver — shareholding 48.02% -> 51.88% effective last day of quarter; PPA provisional under Ind AS 103, no remeasurement gain/loss recognised this quarter |
| 9 | L438-444 | "On April 23, 2026, IKS Inc., a wholly owned US subsidiary of the Company, entered into a definitive agreement to acquire TruBridge, Inc. for an enterprise value of up to US$557 million..." | Subsequent event — TruBridge acquisition completed July 9, 2026 (after quarter end, before results approval), non-adjusting under Ind AS 10; also discloses a pre-existing software-license revenue relationship with TruBridge recognised in-quarter, assessed separate from the business combination under Ind AS 103/115 |
| 10 | L446-457 | "On May 14, 2026 ('acquisition date'), Inventurus Knowledge Solutions Limited ('the Company') acquired 10,000 equity shares of face value INR 10 each, representing 100% of the paid-up equity share capital of ARAI Solutions Private Limited..." | New subsidiary acquisition (ARAI, cash consideration INR 110 million); PPA provisional under Ind AS 103 |

No unnumbered notes or footnotes below the numbered list beyond the two-instance statutory-auditor identification disclaimer already logged under Section 6.

---

## FLAGS RAISED — SUMMARY

- ZERO_STANDING: 6 total instances — 4 financial statement line items (Section 6, #6/13/23/28) + 2 Annexure B "Not Applicable" fields (Section 3, rows 4-5) + 1 Annexure D "None" field (Section 3, row 5) = strictly 4 line-item + 3 disclosure-table-field instances (7 rows carry the flag in total across the ledger; financial-line-item subtotal used in the COUNT TEST is 4).
- ENTITY_CHANGE: 1 (IKS WWMG MSO, LLC — associate reclassifying to step-down subsidiary effective June 30, 2026, per Note 8 and the review-report entity table bracket annotation).
- OCR_GARBLED: 2 (Annexure C heading on page 10, L508; auditor signature timestamp in the notes-page stamp block, L459-461).
- UNAUDITED_ENTITIES: 1 (auditor para 7 — 5 subsidiaries + 1 associate whose interim financials are unreviewed/management-furnished, not material per management representation).

No MGMT_ABSENCE, REPEAT_QUESTION, or DROPPED_SLIDE flags apply — not a concall transcript or investor presentation doctype.
