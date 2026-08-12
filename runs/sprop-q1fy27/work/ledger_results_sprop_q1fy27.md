# A2 COMPLETENESS LEDGER — Shriram Properties Limited (SPROP), Q1 FY27 (results)

Source: `extract_results_sprop_q1fy27.txt` (526 lines, 10 pages; page 1 native
text; pages 2-10 OCR/tesseract, pages 4 and 9 visually verified per header).

```
=== A2 COUNT TEST ===
category: notes         grep_count: 17  sweep_count: 17  match: yes
category: line_items    grep_count: 59  sweep_count: 59  match: yes
category: zero_standing grep_count: 7   sweep_count: 7   match: yes
category: agenda_items  grep_count: 2   sweep_count: 2   match: yes
category: auditor_paras grep_count: 11  sweep_count: 11  match: yes
category: entities      grep_count: 31  sweep_count: 31  match: yes
category: signatures    grep_count: 5   sweep_count: 5   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (reproducible against the extract file):
- notes (numbered + footnote): `grep -n -E "^[0-9]+\)|^\(\*\)|^Certain amounts"`
- line_items (standalone L182-220, consolidated L414-467): `grep -n -E "( {2,}[0-9(.,\-][^ ]*){2,}|\[blank\]"`
- zero_standing: `grep -n -E "\[blank\]"` (4 rows) + `grep -n -E "  -( |$)"` on table bodies (3 rows) = 7
- agenda_items: `grep -n -E "^\s+[0-9]+\."` on page 1 (L33-95)
- auditor_paras: `grep -n -E "^[0-9]+\."` restricted to L96-358 (excludes Annexure 1 entity list)
- entities: `grep -n -E "^[0-9]+\."` restricted to L359-398 (Annexure 1)
- signatures: manual sweep for "Digitally signed" / "Disitally signed" (OCR variant) blocks, cross-checked by line range

Manual sweep note: the line_items grep initially undercounted (34 vs 35 for
the consolidated table) because one row — "Non-controlling interest" under
"Other comprehensive (loss)/income attributable to" (line 454) — is dash
("-") in all four periods and contains no digit at all, so a digit-only
regex misses it. The pattern was widened to catch bare-dash table rows
before reconciling. This is itself the ZERO_STANDING signal the recipe
exists to catch — recorded below, not dropped.

---

## TABLE 1 — NUMBERED AND FOOTNOTE NOTES (13 numbered + 4 footnote = 17)

### Standalone financial results — "Notes to standalone unaudited financial results" (page 5)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| S-N1 | 231 | The above standalone unaudited financial results of Shriram Properties Limited ('the Company'), for the quarter ended | — |
| S-N2 | 236 | The statutory auditors of the Company have carried out a limited review of the above | — |
| S-N3 | 240 | These standalone financial results have been reviewed by the Audit Committee and approved by the | — |
| S-N4 | 243 | The Company is primarily engaged in the business of real estate development, which is considered | Single-segment, single-geography disclosure |
| S-N5 | 246-256 | The Enforcement Directorate conducted a search activity at the Company's business premises on 23 October | ED search-operation note; cross-referenced by auditor EoM para 5 (standalone) |
| S-N6 | 257-258 | The standalone financial results for the quarter ended 31 March 2026 are the balancing figures | Explains the "[Refer note 6]" tag on the Q4 FY26 column header (line 180) |

### Standalone footnotes (unnumbered, below table / P&L)

| # | Line | Text | Flags |
|---|------|------|-------|
| S-FN1 | 217, 222 | "(*) EPS for the quarters not annualized" — qualifies Basic/Diluted EPS rows | — |

### Consolidated financial results — "Notes to consolidated unaudited financial results" (page 10)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| C-N1 | 479 | The above consolidated unaudited financial results of Shriram Properties Limited (the Holding Company), its subsidiaries | — |
| C-N2 | 485 | The statutory auditors of the Holding Company have carried out a limited review of the | — |
| C-N3 | 489 | These consolidated financial results have been reviewed by the Audit Committee and approved by the | — |
| C-N4 | 492 | The Group is primarily engaged in the business of real estate development, which is considered | Single-segment, single-geography disclosure |
| C-N5 | 495-505 | The Enforcement Directorate conducted a search activity at the Group's business premises on 23 October | ED search-operation note; cross-referenced by auditor EoM para 5 (consolidated) |
| C-N6 | 506 | The Holding Company has 26 subsidiaries (including step-down subsidiaries) and 5 Joint-Ventures as on 30 | Reconciles exactly with Annexure 1 entity list (26 + 5 = 31) |
| C-N7 | 508-509 | The consolidated financial results for the quarter ended 31 March 2026 are the balancing figures | Explains the "[Refer note 7]" tag on the Q4 FY26 column header (line 412) |

### Consolidated footnotes (unnumbered, below table / Annexure)

| # | Line | Text | Flags |
|---|------|------|-------|
| C-FN1 | 465, 469 | "(*) EPS for the quarters not annualised" — qualifies Basic/Diluted EPS rows | — |
| C-FN2 | 470 | "Certain amounts that are required to be presented and do not appear due to rounding off are expressed as '0'." | Explains "(0)" NCI entries at lines 449/459 as rounding artifacts, not true zero |
| A1-FN1 | 391 | "(*) subsidiary with effect from 09 February 2026" — qualifies entity #26 (Shrivision Upscale Spaces Pvt Ltd) in Annexure 1 | ENTITY_CHANGE (document-internal evidence; no prior-quarter ledger available to formally cross-check) |

Notes total: 6 + 1 + 7 + 3 = 17.

---

## TABLE 2 — STANDALONE P&L LINE ITEMS (24 rows, incl. subtotals)

Columns: Q1 FY27 (30-Jun-26, unaudited) / Q4 FY26 (31-Mar-26, [Refer note 6]) / Q1 FY25 (30-Jun-25, unaudited) / FY26 (31-Mar-26, audited)

| # | Line | Item | Q1 FY27 | Q4 FY26 | Q1 FY25 | FY26 | Flags |
|---|------|------|---------|---------|---------|------|-------|
| 1 | 183 | Revenue from operations | 4,150 | 6,477 | 2,645 | 19,398 | — |
| 2 | 184 | Other income | 4,811 | 7,082 | 1,506 | 13,219 | — |
| 3 | 185 | Total income [subtotal] | 8,961 | 13,559 | 4,151 | 32,617 | — |
| 4 | 188 | Land cost | 7,305 | 32 | 12,712 | 15,713 | — |
| 5 | 189 | Material and contract cost | 3,387 | 1,666 | 4,474 | 9,941 | — |
| 6 | 190 | Changes in inventories | (8,542) | 1,209 | (16,307) | (14,094) | — |
| 7 | 191 | Employee benefits expenses | 2,373 | 2,202 | 2,216 | 9,141 | — |
| 8 | 192 | Finance costs | 1,189 | 1,209 | 854 | 3,841 | — |
| 9 | 193 | Depreciation and amortisation expense | 94 | 95 | 87 | 379 | — |
| 10 | 194 | Impairment losses | 2 | 64 | 3 | 74 | — |
| 11 | 195 | Other expenses | 1,698 | 1,855 | 1,790 | 7,144 | — |
| 12 | 196 | Total expenses [subtotal] | 7,506 | 8,332 | 5,829 | 32,139 | — |
| 13 | 198 | Profit/(loss) before tax | 1,455 | 5,227 | (1,678) | 478 | — |
| 14 | 201 | Current tax (incl. taxes for earlier years) | - | - | (400) | (400) | ZERO_STANDING (dash in current and prior quarter) |
| 15 | 202 | Deferred tax | 173 | 1,366 | (383) | 122 | — |
| 16 | 203 | Total tax expense/(credit) [subtotal] | 173 | 1,366 | (783) | (278) | — |
| 17 | 205 | Profit/(loss) for the period/year | 1,282 | 3,861 | (895) | 756 | — |
| 18 | 209 | Re-measurement (loss)/gain on defined benefit plans, net of taxes | (11) | 38 | (5) | (43) | — |
| 19 | 210 | Total OCI for the period/year [subtotal] | (11) | 38 | (5) | (43) | — |
| 20 | 212 | Total comprehensive income/(loss) for the period/year | 1,271 | 3,899 | (900) | 713 | — |
| 21 | 214 | Paid up share capital (₹10 par, fully paid) | [blank] | [blank] | [blank] | 17,065 | ZERO_STANDING (interim columns blank; SEBI format discloses this line for the annual column only — not a transactional zero) |
| 22 | 215 | Other equity | [blank] | [blank] | [blank] | 1,42,767 | ZERO_STANDING (same interim-blank convention) |
| 23 | 219 | Basic EPS (₹) | 0.75 | 2.26 | (0.53) | 0.44 | — |
| 24 | 220 | Diluted EPS (₹) | 0.75 | 2.26 | (0.53) | 0.44 | — |

---

## TABLE 3 — CONSOLIDATED P&L LINE ITEMS (35 rows, incl. subtotals and attribution splits)

| # | Line | Item | Q1 FY27 | Q4 FY26 | Q1 FY25 | FY26 | Flags |
|---|------|------|---------|---------|---------|------|-------|
| 1 | 415 | Revenue from operations | 22,428 | 64,088 | 24,232 | 1,26,741 | — |
| 2 | 416 | Other income | 4,676 | 2,185 | 1,922 | 8,952 | — |
| 3 | 417 | Total income [subtotal] | 27,104 | 66,273 | 26,154 | 1,35,693 | — |
| 4 | 420 | Land cost | 7,377 | 13,726 | 16,972 | 33,731 | — |
| 5 | 421 | Material and construction cost | 9,609 | 9,777 | 15,286 | 49,529 | — |
| 6 | 422 | Changes in inventories | (156) | 22,484 | (16,185) | 6,955 | — |
| 7 | 423 | Employee benefits expense | 2,687 | 2,551 | 2,503 | 10,528 | — |
| 8 | 424 | Finance costs | 2,120 | 1,891 | 2,226 | 8,621 | — |
| 9 | 425 | Depreciation and amortization expenses | 261 | 260 | 234 | 1,005 | — |
| 10 | 426 | Impairment losses | 2 | 355 | 5 | 368 | — |
| 11 | 427 | Other expenses | 3,395 | 6,493 | 3,414 | 16,894 | — |
| 12 | 428 | Total expenses [subtotal] | 25,295 | 57,537 | 24,455 | 1,27,631 | — |
| 13 | 430 | Profit before share of (loss)/profit of JVs [subtotal] | 1,809 | 8,736 | 1,699 | 8,062 | — |
| 14 | 431 | Share of (loss)/profit of joint ventures (net) | (385) | (1,751) | 486 | (259) | — |
| 15 | 432 | Profit before tax [subtotal] | 1,424 | 6,985 | 2,185 | 7,803 | — |
| 16 | 435 | Current tax (incl. taxes for earlier years) | 207 | (1,456) | 119 | (591) | — |
| 17 | 436 | Deferred tax | 113 | 588 | 7 | (1,687) | — |
| 18 | 437 | Total tax expense/(credit) [subtotal] | 320 | (868) | 126 | (2,278) | — |
| 19 | 438 | Profit for the period/year | 1,104 | 7,853 | 2,059 | 10,081 | — |
| 20 | 442 | Re-measurement of (losses)/income on defined benefit plans, net of taxes | (16) | 86 | (8) | (69) | — |
| 21 | 443 | Other comprehensive (loss)/income for the period/year [subtotal] | (16) | 86 | (8) | (69) | — |
| 22 | 445 | Total comprehensive income for the period/year | 1,088 | 7,939 | 2,051 | 10,012 | — |
| 23 | 448 | Net profit attributable to: Owners of the Holding Company | 1,104 | 7,854 | 2,059 | 10,082 | — |
| 24 | 449 | Net profit attributable to: Non-controlling interest | (0) | (1) | (0) | (1) | rounding to zero per footnote C-FN2, not a true nil |
| 25 | 450 | Net profit attributable to [subtotal] | 1,104 | 7,853 | 2,059 | 10,081 | — |
| 26 | 453 | OCI attributable to: Owners of the Holding Company | (16) | 86 | (8) | (69) | — |
| 27 | 454 | OCI attributable to: Non-controlling interest | - | - | - | - | ZERO_STANDING — dash in ALL FOUR periods; missed by digit-only grep, caught only in manual sweep (see reconciliation note above) |
| 28 | 455 | OCI attributable to [subtotal] | (16) | 86 | (8) | (69) | — |
| 29 | 458 | Total comprehensive income attributable to: Owners of the Holding Company | 1,088 | 7,940 | 2,051 | 10,013 | — |
| 30 | 459 | Total comprehensive income attributable to: Non-controlling interest | - | (1) | (0) | (1) | ZERO_STANDING (dash in current quarter only) |
| 31 | 460 | Total comprehensive income attributable to [subtotal] | 1,088 | 7,939 | 2,051 | 10,012 | — |
| 32 | 462 | Paid up share capital (₹10 par, fully paid) | [blank] | [blank] | [blank] | 17,065 | ZERO_STANDING (interim columns blank, same convention as standalone) |
| 33 | 463 | Other equity | [blank] | [blank] | [blank] | 1,28,927 | ZERO_STANDING (same interim-blank convention) |
| 34 | 466 | Basic EPS (₹) | 0.65 | 4.60 | 1.21 | 5.91 | — |
| 35 | 467 | Diluted EPS (₹) | 0.65 | 4.60 | 1.21 | 5.91 | — |

Note: consolidated Other equity FY26 (1,28,927) differs from standalone
Other equity FY26 (1,42,767) — expected, consolidated nets out
non-controlling/JV effects; flagged here only for A3/A4 traceability, not
interpreted.

ZERO_STANDING total across Tables 2+3: standalone rows 14, 21, 22 (3) +
consolidated rows 27, 30, 32, 33 (4) = 7 (matches count test).

---

## TABLE 4 — BOARD OUTCOME AGENDA ITEMS (page 1)

Board meeting: commenced 06:30 P.M., concluded 07:20 P.M., 12 August 2026
(line 47-48) — a 50-minute meeting covering both the quarterly results
approval and the AGM convening resolution.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 51-55 | Unaudited Financial Results (Standalone and Consolidated) for Q1 FY27 | Approved along with the Limited Review Report of the Statutory Auditors, enclosed | — |
| 2 | 57-66 | Convening of the Annual General Meeting | 5th AGM post-IPO, via VC/OAVM per MCA/SEBI circulars; Annual Report and AGM Notice to follow separately within prescribed timeline | No record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution appears anywhere in this letter — checked and confirmed absent, not merely unlisted |

Agenda items total: 2.

---

## TABLE 5 — AUDITOR LIMITED REVIEW REPORTS (11 paragraphs: 5 standalone + 6 consolidated)

Both reports: Walker Chandiok & Co LLP, Chartered Accountants, Firm
Registration No. 001076N/N500013, signed by Vishal Suresh (Partner,
Membership No. 285794). Both conclusions are **unmodified** (review
conclusion, not audit opinion — reports explicitly state "we do not express
an audit opinion", para 3 in each). **No Going Concern paragraph appears in
either report** — noted as an absence, not assumed.

### Standalone review report (pages 2-3, lines 96-165)

| Para | Line | Type | Content | Flags |
|------|------|------|---------|-------|
| 1 | 110-113 | Scope/introduction | Reviewed standalone statement for quarter ended 30 June 2026, submitted per Reg 33 | — |
| 2 | 115-120 | Management responsibility | Statement is management's responsibility, approved by Board, prepared per Ind AS 34 | — |
| 3 | 122-129 | Review methodology | SRE 2410; review is substantially less in scope than an audit; no audit opinion expressed | — |
| 4 | 131-136 | Conclusion | Unmodified — nothing came to attention indicating non-disclosure or material misstatement per Reg 33 | — |
| 5 | 147-152 | **Emphasis of Matter** | Draws attention to note 5 (ED search operation, Oct 2024); no communication of findings received; conclusion NOT modified | Cross-refs standalone note S-N5 |

No "Other Matter" paragraph in the standalone report (no sub-entities to review standalone).

Signature block (lines 153-165): Vishal Suresh, Partner, Membership No.
285794, UDIN **26285794CQTCAV7292**, Bengaluru, 12 August 2026. Digital
signature timestamp 2026.08.12 **19:14:02 +05'30'** (line 158-159).

### Consolidated review report (pages 6-8, lines 270-358; Annexure 1 lines 359-398)

| Para | Line | Type | Content | Flags |
|------|------|------|---------|-------|
| 1 | 283-288 | Scope/introduction | Reviewed consolidated statement of Holding Company + subsidiaries + JVs (Group), per Annexure 1 list, quarter ended 30 June 2026 | — |
| 2 | 290-295 | Management responsibility | Statement is Holding Company management's responsibility, approved by Board, prepared per Ind AS 34 | — |
| 3 | 297-306 | Review methodology | SRE 2410; also performed procedures per SEBI circular under Reg 33(8); no audit opinion expressed | — |
| 4 | 308-313 | Conclusion | Unmodified — nothing came to attention indicating non-disclosure or material misstatement per Reg 33 | — |
| 5 | 325-330 | **Emphasis of Matter** | Draws attention to note 5 (ED search operation, Group's premises, Oct 2024); no findings communicated; conclusion NOT modified | Cross-refs consolidated note C-N5 |
| 6 | 333-343 | **Other Matter** | Did not review interim results of **18 subsidiaries** (total revenue ₹7,266 lakh, total net loss after tax ₹274 lakh, total comprehensive loss ₹274 lakh for the quarter) and **4 joint ventures** (Group share of net profit ₹771 lakh, total comprehensive income ₹771 lakh); reviewed by other auditors, reports furnished to principal auditor; principal auditor's conclusion based solely on those other auditors' reports; conclusion NOT modified w.r.t. this reliance | **18 unreviewed subsidiaries** — of 26 total subsidiaries in Annexure 1, 8 were reviewed directly by Walker Chandiok, 18 were not (reviewed by other auditors); of 5 JVs, 1 reviewed directly, 4 not (arithmetic derived from Annexure 1 total minus Other Matter para counts, not separately itemized by name in the report) |

Signature block (lines 344-358): Vishal Suresh, Partner, Membership No.
285794, UDIN **26285794ZBFNXN3045** (distinct from the standalone UDIN, as
required), Bengaluru, 12 August 2026. Digital signature timestamp field is
OCR-garbled: "Date: 2026.08.12 / SURESH 6:1425 +05'30'" (lines 349-351) —
recorded exactly as extracted; NOT FOUND as a clean value. Given the
standalone report's clean timestamp of 19:14:02, a plausible reading is
~19:14:25, but this is not asserted as fact. Flag: OCR_UNCERTAIN.

Entity list (Annexure 1, page 8, lines 359-398): 26 subsidiaries + 5 joint
ventures = 31 entities total, enumerated in Table 6.

---

## TABLE 6 — ANNEXURE 1: ENTITIES INCLUDED IN THE CONSOLIDATED STATEMENT (31 rows)

Cross-check: prior-quarter ledger NOT available in repo (per task input),
so no formal prior-vs-current diff was possible. One entity carries an
internal footnote evidencing a recent addition (flagged below on
document-internal evidence alone).

### A) Subsidiaries (26)

| # | Line | Entity | Reviewed by principal auditor? | Flags |
|---|------|--------|-------------------------------|-------|
| 1 | 365 | Bengal Shriram Hitech City Private Limited | Not individually stated (18 of 26 unreviewed per Other Matter para; not named) | — |
| 2 | 366 | SPL Estates Private Limited | " | — |
| 3 | 367 | Shriprop Developers Private Limited | " | — |
| 4 | 368 | Global Entropolis (Vizag) Private Limited | " | — |
| 5 | 369 | Shriprop Structures Private Limited | " | — |
| 6 | 370 | SPL Constructors Private Limited | " | — |
| 7 | 371 | Shriprop Constructors Private Limited | " | — |
| 8 | 372 | Shriprop Homes Private Limited | " | — |
| 9 | 373 | Shriprop Projects Private Limited | " | — |
| 10 | 374 | Shriprop Builders Private Limited | " | — |
| 11 | 375 | SPL Realtors Private Limited | " | — |
| 12 | 376 | Shrivision Homes Private Limited | " | — |
| 13 | 377 | Shriram Upscale Spaces Private Limited | " | — |
| 14 | 378 | Shriprop Properties Private Limited | " | — |
| 15 | 379 | Shriram Living Space Private Limited | " | — |
| 16 | 380 | SPL Palms Developers Private Limited | " | — |
| 17 | 381 | Shrivision Projects Private Limited | " | — |
| 18 | 382 | Shriprop Infrastructures Private Limited | " | — |
| 19 | 383 | Shrivision Structures Private Limited | " | — |
| 20 | 384 | Shrivision Estates Private Limited | " | — |
| 21 | 385 | Shrivision Malls Private Limited | " | — |
| 22 | 386 | Shrivision Hitech City Private Limited | " | — |
| 23 | 387 | Shriprop Malls Private Limited | " | — |
| 24 | 388 | SPL Homes Private Limited | " | — |
| 25 | 389 | SPL Housing Projects Private Limited | " | — |
| 26 | 390-391 | Shrivision Upscale Spaces Private Limited | Not stated | **ENTITY_CHANGE** — footnoted "(*) subsidiary with effect from 09 February 2026", i.e. added as a subsidiary within roughly the last two quarters; no prior ledger available in this repo to confirm absence in the immediately preceding quarter's list, flagged on document-internal evidence only |

The report's Other Matter paragraph (Table 5, para 6) does not name which
18 of the 26 subsidiaries were unreviewed; this ledger records that
sub-entity-level attribution as NOT FOUND (not disclosed in this filing),
not estimated.

### B) Joint Ventures (5)

| # | Line | Entity | Flags |
|---|------|--------|-------|
| 1 | 393 | Shrivision Towers Private Limited | — |
| 2 | 394 | SPL Towers Private Limited | — |
| 3 | 395 | Shriprop Living Space Private Limited | — |
| 4 | 396 | Shriprop Hitech City Private Limited | — |
| 5 | 397 | Shrivision Elevation Private Limited | — |

Entities total: 26 + 5 = 31. Reconciles exactly against note C-N6 ("26
subsidiaries...and 5 Joint-Ventures", line 506).

Observation (not a substantive flag): the Annexure 1 heading "List of
entities included in the Statement" appears twice consecutively (lines
362-363), an apparent OCR/source duplication of the header line, not a
duplicated entity.

---

## TABLE 7 — DIGITAL SIGNATURE BLOCKS (5)

Board meeting window for reference: commenced 18:30, concluded **19:20**
(19:20:00), 12 August 2026.

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|------|-----------|-------------|----------|-----------|-------|
| 1 | 74-85 | K. Ramaswamy (ACS 28580) | Company Secretary & Compliance Officer | Reg 30/33 Board Outcome cover letter | 2026.08.12 19:28:31 +05'30' | After board conclusion (19:20) — expected, no flag |
| 2 | 153-163 | Vishal Suresh (Membership No. 285794) | Partner, Walker Chandiok & Co LLP | Standalone Limited Review Report | 2026.08.12 **19:14:02** +05'30' | **SIGNATURE_TIMING** — signed 6 minutes BEFORE the board meeting concluded (19:20) |
| 3 | 260-269 | Murali M (DIN 00030096) | Chairman and Managing Director | Standalone financial results / notes | 2026.08.12 **19:02:02** +05'30' (OCR-garbled "202608:12 19:02:02") | **SIGNATURE_TIMING** — signed 18 minutes BEFORE the board meeting concluded (19:20) |
| 4 | 344-355 | Vishal Suresh (Membership No. 285794) | Partner, Walker Chandiok & Co LLP | Consolidated Limited Review Report | OCR-garbled: "6:1425 +05'30'" (date 2026.08.12) | **OCR_UNCERTAIN** + likely **SIGNATURE_TIMING** (a clean reading would put this before 19:20 too, consistent with signature #2, but the exact minute is NOT FOUND — not estimated) |
| 5 | 511-524 | Murali M (DIN 00030096) | Chairman & Managing Director | Consolidated financial results / notes | 2026.08.12 **19:02:24** +05'30' | **SIGNATURE_TIMING** — signed 18 minutes BEFORE the board meeting concluded (19:20) |

Signature blocks total: 5. Four of five carry a timestamp before the stated
board-meeting conclusion time (one further OCR-uncertain but consistent
with the same pattern); only the Company Secretary's cover-letter signature
(filed after the meeting, as expected) postdates it. This pattern —
auditor and CMD signatures on the results/review report predating the
board's own stated approval time — is surfaced here as a mechanical
timestamp fact for A3/A4 to weigh; no interpretation is offered.

---

## CATEGORIES NOT APPLICABLE TO THIS DOCTYPE (results filing)

Concall-transcript categories (participants, speaker turns, questions,
spoken management numbers, forward-commitment/hedge phrases) and investor-
presentation categories (slides, slide numbers, dropped slides, footnotes
per slide) do not apply — this document is a results filing (Reg 30/33
Board Outcome letter + standalone/consolidated financials + notes + two
Limited Review Reports + Annexure 1). Counted as 0 in the closing YAML per
the template's "per applicable category" instruction.

---

```yaml
stage: A2-enumerator
company: "SPROP"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/sprop-q1fy27/work/ledger_results_sprop_q1fy27.md"
counts:
  notes: 17
  line_items: 59
  zero_standing: 7
  agenda_items: 2
  auditor_paras: 11
  entities: 31
  signatures: 5
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, SIGNATURE_TIMING, OCR_UNCERTAIN]
gate_a2: pass
mismatch_note: ""
```
