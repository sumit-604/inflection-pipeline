# A2 ENUMERATOR LEDGER — GARGI Q1 FY27 (Results Filing)

Company: PNGS Gargi Fashion Jewellery Ltd (GARGI, BSE 543709)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Doctype: results
Source: /home/user/inflection-pipeline/runs/gargi-q1fy27/work/extract_results_gargi_q1fy27.txt
Line-number convention used below: the extract's OWN embedded per-line numbers
(1-275, matching the A1 header's `line_count: 275`), NOT raw physical file
lines of the .txt (which also carry header/page-marker overhead and would
misalign citations). Verified by cross-checking `awk -F'\t' '$1 ~ /^[0-9]+$/'`
against the A1 header's declared line_count (275 = 275, exact match).

```
=== A2 COUNT TEST ===
category: notes           grep_count: 9   sweep_count: 9   match: yes
category: line_items      grep_count: 28  sweep_count: 28  match: yes
category: zero_standing   grep_count: 3   sweep_count: 3   match: yes
category: agenda_items    grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras   grep_count: 4   sweep_count: 4   match: yes
category: entities        grep_count: 0   sweep_count: 0   match: yes (standalone only, no consolidation list)
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note (required transparency, not part of the gate block):**
First-pass grep for `notes` used anchor `^\s*[0-9]+\.\s` and returned 8, not 9.
Manual sweep of lines 190-260 found 9 (notes 1-7 + Company Outlook items 1-2).
Root cause of the 8-vs-9 mismatch: explanatory note 4 (line 213) is prefixed
by an OCR-corrupted bullet glyph (`■`, byte sequence `342 226 240`) before the
literal "4.", so the whitespace-anchored regex failed to match it while the
manual read caught it. Re-ran grep with the anchor relaxed to allow any
non-digit prefix (`[0-9]+[.)]\s` unanchored) — this returned 9, matching the
sweep. GATE A2 result reported above is the reconciled state. Note 4 itself
is enumerated below with flag `OCR_GLYPH_CORRUPTION` since the same glyph
corruption pattern recurs elsewhere in this extract (see Notes table) and is
worth a flag for A3/A4, not just a parsing footnote for A2.

---

## 1. Board Outcome Cover Letter (page 1, embedded lines 1-34)

| # | Item | Line | Detail | Flag |
|---|------|------|--------|------|
| 1 | Agenda item 1 (only item) | 18 | "approved the Unaudited Standalone Financial Results for the quarter ended June 30, 2026" | — |
| — | Agenda items beyond item 1 | — | NONE FOUND. Full-letter sweep (grep for AGM / dividend / appoint / auditor rotation / ESOP / record date / scrutinizer / buyback / rights issue / bonus / resignation / capital-raising, plus manual read of lines 1-34) returns zero additional agenda items. This Board Outcome discloses results approval only. | AGENDA_SINGLE_ITEM |
| — | Board meeting timing | 22 | Commenced 04:00 p.m., ended 5:15 p.m. — duration 1h15m | — |
| — | Ref line (scrip code / symbol) | 12 | "BSE Scrip Code- 543709 ... Symbol- GARG!" ("GARG!" is an OCR artifact for GARGI) | OCR_GLYPH_CORRUPTION |
| — | Encl. reference | 34 | "Encl: Annexure I" — confirms exactly one annexure attached (the auditor's review report) | — |
| — | Signatory block (CS) | 25-32 | Hiranyamai Chaitanya Deshpande, Company Secretary & Compliance Officer, digitally signed. Timestamp: 2026.07.31 17:16:18 +05'30' | see Signature Blocks table (§7) |

Grep basis for "agenda items beyond item 1": `grep -inE 'AGM|dividend|appoint|auditor rotation|ESOP|record date|scrutinizer|buyback|rights issue|bonus share|capital raising|resignation|approv'` across the full 275-line extract returned only line 18/19 (results approval, this letter) plus lines 59 and 197 (unrelated: auditor-report boilerplate and explanatory-note-1 boilerplate about Audit Committee review, not board agenda items). Manual sweep of the full letter body confirms no other resolution is disclosed. agenda_items = 1, sweep = 1, match.

---

## 2. Auditor's Limited Review Report — Annexure I (page 2, embedded lines 45-104)

Auditor: Khandelwal Jain & Associates, Chartered Accountants. Report type: Limited Review (SRE 2410), NOT a statutory audit. Opinion: unmodified / clean (no exceptions noted).

| Para # | Line | First ~15 words | Type | Flag |
|--------|------|------------------|------|------|
| 1 | 53-57 | "We have reviewed the accompanying Statement of Standalone Unaudited Financial Results... for the quarter ended June 30th, 2026" | Scope / engagement identification | — |
| 2 | 59-65 | "This Statement, which is the responsibility of the Company's Management and approved by the Board..." | Management responsibility / basis of preparation (Ind AS 34) | — |
| 3 | 67-76 | "We conducted our review... in accordance with SRE 2410... Accordingly, we do not express an audit opinion" | Basis of review / scope limitation vs. audit | — |
| 4 | 78-86 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." | Conclusion (unmodified) | — |

Additional auditor-report elements enumerated (not numbered paragraphs, but required disclosure units per instruction 5):
| Item | Line | Detail | Flag |
|------|------|--------|------|
| Emphasis of Matter paragraph | — | NONE PRESENT — swept full report text, no EOM heading or language found | — |
| Other Matters paragraph | — | NONE PRESENT | — |
| Going Concern language | — | NONE PRESENT | — |
| Entity list reviewed | 54 | Single entity: PNGS GARGI FASHION JEWELLERY LIMITED (standalone only; no subsidiaries/JVs named as unaudited or management-furnished) | — |
| Signature/attestation block | 87-99 | "For Khandelwal Jain & Associates", partner name OCR-illegible, FRN OCR-garbled ("1.;3W 5"), Membership No. 031177 (legible), UDIN OCR-garbled/illegible ("2.6031 Irr J"R.Wt='ZC 2.'7 t3"), Date: 31-07-2026, Place: Pune | UDIN_ILLEGIBLE |

auditor_paras = 4 (grep on `^\s*[0-9]+\.\s` within lines 45-104 returns exactly 4 matches at 53/59/67/78; manual sweep of the full Annexure I text confirms no 5th numbered paragraph and no unnumbered EOM/Other Matters section). Match.

---

## 3. Statement of Unaudited Standalone Financial Results (page 3, embedded lines 105-190)

Confirmed STANDALONE ONLY. No consolidated figures, no consolidated statement, no reference to subsidiaries/associates anywhere in this table or its footnotes. Title (line 112), cover letter (line 18), and auditor report (lines 50-54) all consistently say "Standalone." Stated explicitly per instruction: **there is no consolidated track in this filing.**

Columns: Q1 FY27 (Jun 30, 2026, Unaudited) | Q4 FY26 (Mar 31, 2026, Audited) | Q1 FY26 (Jun 30, 2025, Unaudited) | FY26 (Mar 31, 2026, Audited, full year).

### 3a. Section headers (structural rows, not counted as line items)
| Line | Header |
|------|--------|
| 123 | Income |
| 129 | Expenses |
| 145 | Tax expense: |
| 154 | Other Comprehensive Income (OCI) |
| 156 | Items that will not be reclassified to profit or loss: |
| 164 | Earnings per equity share: |

### 3b. Line items (data + subtotal rows) — every row, zero/nil rows flagged ZERO_STANDING
| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Row type | Flag |
|---|------|-----------|--------|--------|--------|------|----------|------|
| 1 | 124 | Revenue from operations | 3,021.62 | 2,958.67 | 2,731.10 | 14,940.14 | data | — |
| 2 | 125 | Other income | 188.08 | 118.83 | 120.45 | 534.27 | data | — |
| 3 | 127 | Total Income | 3,209.70 | 3,077.50 | 2,851.55 | 15,474.41 (OCR-garbled) | subtotal | OCR_GLYPH_CORRUPTION |
| 4 | 130 | Purchase of Stock-in-Trade | 2,455.97 | 1,977.15 | 1,857.21 | 10,173.63 | data | — |
| 5 | 131 | Changes in inventories of Stock-in-Trade | (709.57) | (382.14) | (236.62) | (1,646.44) | data | — |
| 6 | 132 | Employee benefits expense | 103.60 | 92.87 | 68.19 | 321.16 | data | — |
| 7 | 133 | Finance cost | 31.28 | 29.12 | 13.86 | 86.90 | data | — |
| 8 | 134 | Depreciation and amortization expense | 75.25 | 52.87 | 27.28 | 157.69 | data | — |
| 9 | 135 | Other expenses | 574.58 | 576.39 | 407.78 | 2,128.69 | data | — |
| 10 | 137 | Total Expenses | 2,531.11 | 2,346.26 | 2,137.70 | 11,221.63 | subtotal | — |
| 11 | 139 | Profit before exceptional item and tax | 678.59 | 731.24 | 713.85 | 4,252.78 | subtotal | — |
| 12 | 141 | Exceptional Item | — (blank) | — (blank) | — (blank) | 15.18 | data | **ZERO_STANDING** (current qtr, prior qtr, prior-year qtr all blank; only annual column populated — template signal for one-off items) |
| 13 | 143 | Profit before tax | 678.59 | 731.24 | 713.85 | 4,237.60 | subtotal | — |
| 14 | 146 | Current tax | 179.91 | 204.96 | 184.44 | 1,106.22 | data | — |
| 15 | 147 | Deferred tax charge / (credit) | (6.28) | 3.95 | (1.91) | (9.93) | data | — |
| 16 | 148 | Previous Period's tax | — (blank) | 8.34 | — (blank) | 8.34 | data | **ZERO_STANDING** (blank in current qtr and prior-year qtr; populated only in Q4FY26 and FY26 annual) |
| 17 | 150 | Total tax expense | 173.63 | 217.25 | 182.53 | 1,104.63 | subtotal | — |
| 18 | 152 | Profit after exceptional item and tax | 504.96 | 513.99 | 531.32 | 3,132.97 (OCR-garbled spacing) | subtotal | OCR_GLYPH_CORRUPTION |
| 19 | 157 | Re-measurement gain/(loss) on defined benefit plans | 0.74 | 1.31 | (0.62) | (0.33) | data | — |
| 20 | 158 | Effect of income tax | (0.19) | (0.33) | 0.16 | 0.08 | data | — |
| 21 | 160 | Other Comprehensive Income, net of tax | 0.55 | 1.00 | (0.47) | (0.25) | subtotal | — |
| 22 | 162 | Total Comprehensive Income, net of tax | 505.51 (OCR-garbled "SOS.St") | 514.97 | 530.85 | 3,132.72 (OCR-garbled spacing) | subtotal | OCR_GLYPH_CORRUPTION |
| 23 | 165 | Basic EPS (in Rs) | 4.82 | 4.91 | 5.13 | 30.05 | data | — |
| 24 | 166 | Diluted EPS (in Rs) | 4.82 | 4.91 | 5.13 | 30.05 | data | — |
| 25 | 168 | Paid up Equity share capital as on reporting date | 1,047.03 | 1,047.03 | 1,035.78 | 1,047.03 | data | — |
| 26 | 169 | Other equity | — (blank) | — (blank) | — (blank) | 13,143.35 | data | **ZERO_STANDING** (standard convention — reserves/surplus shown only for the annual audited column, blank in all quarterly columns) |
| 27 | 170 | Total No. of shares (Weighted Average) | 1,04,70,303 | 1,04,70,303 | 1,03,57,803 | 1,04,24,995 | data | — |
| 28 | 171 | Face value of per share (in Rs) | 10.00 | 10.00 | 10.00 | 10.00 | data | — |

line_items = 28 (grep basis: `awk -F'\t' '$1>=123 && $1<=171 {print $2}' | grep -cE '[0-9]'` on content field only = 28; manual sweep of the same 49-line table range, subtracting 21 header/blank rows, = 28). Match.
zero_standing = 3 (rows 12, 16, 26 above). Match against manual sweep.

### 3c. Table footnotes (asterisk-marked, below the statement, distinct from the numbered explanatory notes on pages 4-5)
| # | Line | Footnote text (start) | Flag |
|---|------|------------------------|------|
| 1 | 173 | "EPS is not annualized for the quarter ended June 30, 2026, quarter ended March 31, 2026, and quarter ended June 30, 2025." | — |
| 2 | 174-175 | "The weighted average number of shares used to calculate earnings per share (EPS) is determined by applying the 'Time Weighting Factor'..." | — |
| 3 | 176 | "Previous period/year figures have been regrouped/rearranged wherever considered necessary." | — |
| — | 177 | "The explanatory notes are an integral part of the financial results" (closing cross-reference statement, not itself a footnote) | — |

### 3d. Signatory block on this page
| Line | Signatory | Detail |
|------|-----------|--------|
| 187-190 | Govind Gadgil, Chairman & Director, DIN 00616617 | "For and on behalf of the Board of Directors", Place: Pune, Date: July 31, 2026. Printed name only, no digital timestamp (contrast with CS block on p.1 which is digitally signed/timestamped). |

---

## 4. Explanatory Notes to the Standalone Financial Results (pages 4-5, embedded lines 192-267)

Two independently numbered sub-series exist in this filing: the main numbered notes (1-7, page 4) and a separately-numbered "Company outlook" sub-series (1-2, page 5) under its own sub-heading. Both are enumerated below; do not conflate their numbering.

| # | Series | Line | First ~15 words | Flag |
|---|--------|------|------------------|------|
| 1 | Main Note 1 | 196-198 | "The above standalone financial results for the quarter ended June 30, 2026 were reviewed by the Audit Committee..." | — |
| 2 | Main Note 2 | 200-206 | "The financial results of PNGS GARGI FASHION JEWELLERY LIMITED... have been prepared in accordance with Ind AS..." | — |
| 3 | Main Note 3 | 208-211 | "The previous period's figures have been considered as per the financial results for the respective period..." | — |
| 4 | Main Note 4 | 213-214 | "The results for the quarter ended June 30, 2026, will be available on the Stock Exchange website..." | **OCR_GLYPH_CORRUPTION** (bullet glyph `■` precedes "4." in source, broke naive grep — see reconciliation note above) |
| 5 | Main Note 5 | 216-219 | "The Company operates in one segment i.e., Trading in fashion/costume jewellery, Gold and Diamond jewellery..." | — |
| 6 | Main Note 6 | 221-222 | "The company has fulfilled its advance tax obligations for the F.Y 2026-27, making payments totalling on 75 lakhs..." | — |
| 7 | Main Note 7 | 224-226 | "As on date of results i.e July 31, 2026, the Company has 36 Shop in Shop (SIS) stores with P.N. Gadgil & Sons..." | — |
| 8 | Company Outlook 1) | 243-249 | "During the previous financial year, the Company issued 90,000 equity shares to the promoters and 22,500 equity shares..." | — |
| 9 | Company Outlook 2) | 251-254 | "Due to the ongoing disturbances in West Asia and their impact on the global economy, there are clear signs of a slowdown..." | — |

notes = 9 (see COUNT TEST reconciliation above for the grep-vs-sweep detail). Match after correction.

Signatory block repeated at end of notes (page 5): Govind Gadgil, Chairman & Director, DIN 00616617, lines 263-267, "For and on behalf of Board of Directors" — same signatory as §3d, second instance in this filing (financial statement page and notes page each carry their own board sign-off block).

---

## 5. Consolidated Figures / Consolidation Entity List

**None found.** This filing discloses standalone results exclusively. No consolidated statement, no list of subsidiaries/associates/JVs, no "unaudited" or "management-furnished" entity carve-outs anywhere in the extract (all 275 lines swept). entities = 0. Not applicable to compare against a prior-quarter entity list since none exists here; no `ENTITY_CHANGE` flag applies (nothing to change from).

---

## 6. Digital Signature / Signatory Blocks (all instances, cross-referenced)

| # | Line(s) | Signatory | Designation | Timestamp | Flag |
|---|---------|-----------|-------------|-----------|------|
| 1 | 25-32 | Hiranyamai Chaitanya Deshpande | Company Secretary & Compliance Officer | Digitally signed 2026.07.31 17:16:18 +05'30' | Board meeting ended 5:15 p.m. (line 22); this signature is timestamped ~1 min 18 sec AFTER meeting conclusion — i.e., NOT before conclusion, so the specific instruction-5.7 trip-flag ("signed before meeting concluded") does not apply. Noted for completeness only; no flag raised. |
| 2 | 87-99 | [name OCR-illegible] | Chartered Accountant, Khandelwal Jain & Associates | Date: 31-07-2026 (no time-of-day given); Place: Pune | UDIN_ILLEGIBLE |
| 3 | 187-190 | Govind Gadgil | Chairman & Director, DIN 00616617 | Date: July 31, 2026 (no time; not digitally signed/timestamped) | — |
| 4 | 263-267 | Govind Gadgil | Chairman & Director, DIN 00616617 | Date: July 31, 2026 (second instance, same signatory, end of explanatory notes page) | — |

---

## 7. Board Meeting Metadata (structural fact, not a line item but material)

| Line | Fact |
|------|------|
| 22 | Board meeting commenced 04:00 p.m., ended 5:15 p.m. — duration 1h 15m for a results-only meeting (single agenda item). |

---

## 8. Items explicitly swept and confirmed NOT PRESENT in this extract
(recorded so absence is documented, not silently skipped)
- Consolidated financial statement / consolidated entity list — NOT PRESENT (standalone only, §5).
- Emphasis of Matter, Other Matters, Going Concern paragraphs in auditor report — NOT PRESENT (§2).
- Any Board Outcome agenda item beyond results approval (AGM, dividend, director appointment/resignation, auditor change, ESOP, record date, scrutinizer, capital-raising resolution) — NOT PRESENT (§1).
- Annexures beyond Annexure I — NOT PRESENT; cover letter (line 34) explicitly encloses only Annexure I.
- Director profile / appointment annexure — NOT PRESENT (no director changes disclosed this quarter).
- Prior-quarter ledger for diffing — NOT PROVIDED to this run (no PRIOR_LEDGER_PATH supplied), so `ENTITY_CHANGE` / `DROPPED_SLIDE`-style prior-period comparisons are not applicable to this doctype/run and are not attempted.

---

## FLAGS SUMMARY
- ZERO_STANDING x3 — lines 141 (Exceptional Item), 148 (Previous Period's tax), 169 (Other equity)
- OCR_GLYPH_CORRUPTION x4 — lines 12 (GARG! for GARGI), 127 (Total Income annual figure), 152 & 162 (spacing artifacts in PAT/TCI annual figures), 213 (bullet glyph obscuring Note 4's numeral)
- UDIN_ILLEGIBLE x1 — line 87-99 (auditor UDIN and partner name OCR-garbled, unresolvable from this extract; recommend A3/A4 source back to original PDF/BSE filing for a clean UDIN read, since UDIN verifiability is a compliance-relevant fact)
- AGENDA_SINGLE_ITEM x1 — line 18 (informational note, not a completeness gap: swept and confirmed no other agenda items exist)
