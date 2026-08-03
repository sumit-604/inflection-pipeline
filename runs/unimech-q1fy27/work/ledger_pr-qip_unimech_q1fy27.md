# A2 ENUMERATOR LEDGER — Unimech Aerospace and Manufacturing Limited (UNIMECH)
Quarter: Q1 FY27 | Doctype: results (Reg 30 press release — QIP fund-raising intimation)
Source: pr_qip_unimech_q1fy27.pdf (2 pages, 96 extract lines, page_coverage 100%)
A1 extract: runs/unimech-q1fy27/work/extract_pr-qip_unimech_q1fy27.txt

```
=== A2 COUNT TEST ===
category: letter_meta         grep_count: 11  sweep_count: 11  match: yes
category: entities             grep_count: 2   sweep_count: 2   match: yes
category: resolution_terms     grep_count: 7   sweep_count: 7   match: yes
category: annexure_table_rows  grep_count: 3   sweep_count: 3   match: yes
category: extraction_notes     grep_count: 1   sweep_count: 1   match: yes
category: signature_block      grep_count: 5   sweep_count: 5   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (all against the extract file, mechanical, no interpretation):
- letter_meta: `grep -n -E "^August|^To,|^Sub:|^Dear Sir|^In furtherance|Board of Directors of Unimech|^Issuance of Equity Shares|^Additional Information|^Kindly acknowledge|^Thanking You|^For Unimech"`
- entities: `grep -noE "National Stock Exchange of India Ltd\.|BSE Limited"`
- resolution_terms: `grep -n -iE "Annual General Meeting|raise further capital|face value of Rs\. 5 each|convertible securities|750,00,00,000|tranches|Chapter VI"`
- annexure_table_rows: `grep -n -E "^\s*[0-9]+\s"` (S.No. column entries in Annexure-I)
- extraction_notes: `grep -n -iE "end of document|no further rows"`
- signature_block: `grep -n -iE "Digitally signed|Date:|Rashmi Gupta|Company Secretary|M\. No"`

---

## Category 1 — Letter Header / Narrative Meta (11 rows)

| # | Line(s) | Content (verbatim / first ~15 words) | Flags |
|---|---------|----------------------------------------|-------|
| 1 | 16 | "August 03, 2026" — letter date | |
| 2 | 18 | "To," — addressee salutation opener | |
| 3 | 24-26 | "Sub: Intimation under Regulation 30 of the Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015 ... Fund Raising" | |
| 4 | 28 | "Dear Sir/Ma'am," | |
| 5 | 30-31 | "In furtherance of our intimation dated July 29, 2026 and pursuant to Regulation 30 and other applicable provisions ... Schedule III thereof" — reference to prior Reg 30 intimation dated Jul 29, 2026 + regulatory basis (Reg 30 + Schedule III) | |
| 6 | 32-34 | "...the Board of Directors of Unimech Aerospace and Manufacturing Limited at its meeting held today, i.e., August 03, 2026, have inter-alia considered and approved the following matter" — board meeting date and approval statement | `MISSING_MEETING_TIMES` — only a date is given for the board meeting; no start/end time disclosed anywhere in the extract (results-filing rule requires recording meeting start/end times where available; here they are simply absent from the source, not merely unextracted) |
| 7 | 36-37 | "Issuance of Equity Shares and/or other eligible securities by way of Qualified Institutions Placement ('QIP'):" — title of the sole agenda matter approved | |
| 8 | 48-50 | "Additional Information as required under Regulation 30 of the SEBI Listing Regulations read with SEBI Master Circular No. HO/49/14/14(7)2025-CFD POD2/I/3762/2026, dated January 30, 2026, is enclosed herewith as 'Annexure-I'" — reference to enclosed Annexure-I with specific circular citation | |
| 9 | 52 | "Kindly acknowledge and take the same on records." | |
| 10 | 54-55 | "Thanking You, Yours Faithfully," — closing valediction | |
| 11 | 57 | "For Unimech Aerospace and Manufacturing Limited" — company signing-block header | |

## Category 2 — Addressee Entities (2 rows)

| # | Line | Entity | Identifier | Flags |
|---|------|--------|------------|-------|
| 1 | 20-21 | National Stock Exchange of India Ltd. | Symbol: UNIMECH | |
| 2 | 20-21 | BSE Limited | Scrip Code: 544322 | |

## Category 3 — QIP Enabling Resolution Terms (7 rows)
(All terms sit inside the single Board-approved matter at lines 36-46; each is a discrete, independently checkable disclosure fact.)

| # | Line(s) | Term | Detail (verbatim) | Flags |
|---|---------|------|---------------------|-------|
| 1 | 39 | Conditionality | "Subject to the approval of the Shareholders at the ensuing Annual General Meeting of the Company" | `CONDITIONAL_ON_SHAREHOLDER_APPROVAL` — this is an enabling resolution only; the raise is not final until AGM approval, no AGM date given anywhere in extract |
| 2 | 40 | Board action | "the Board has approved to raise further capital and to create, offer, issue and allot such number of..." | |
| 3 | 41 | Instrument / face value | "fully paid-up equity shares of the Company of face value of Rs. 5 each (the 'Equity Shares')" | |
| 4 | 42 | Instrument (alt/combination) | "and/or convertible securities or any combination of the Securities thereof in accordance with the applicable laws" | |
| 5 | 43-44 | Aggregate consideration cap | "for an aggregate consideration not exceeding 750,00,00,000 (Rupees Seven Hundred and Fifty Crore Only) or an equivalent amount thereof" | |
| 6 | 44 | Tranches | "in one or more tranches, ... by way of a qualified institutions placement ('QIP') of Securities" | |
| 7 | 44-46 | Regulatory mechanism | "in accordance with the provisions of Chapter VI of the SEBI ICDR Regulations and other applicable laws" | |

## Category 4 — Annexure-I Regulation 30 / Schedule III Disclosure Table (3 rows)

| S.No. | Line(s) | Particulars of Securities | Details of Securities (verbatim) | Flags |
|-------|---------|----------------------------|------------------------------------|-------|
| 1 | 79-80 | Type of securities proposed to be issued (viz. equity shares, convertibles etc.) | "Equity Shares and/or convertible securities or any combination of the Securities thereof" | |
| 2 | 82-90 | Type of issuance (further public offering, rights issue, depository receipts (ADR/GDR), qualified institutions placement, preferential allotment etc.) | "Qualified Institutions Placement ('QIP') in accordance with the provisions of Chapter VI of the Securities and Exchange Board of India (Issue of Capital and Disclosure Requirements) Regulations, 2018, Section 42 and other applicable provisions of the Companies Act, 2013 and other applicable laws, as may be considered appropriate under the applicable laws." | |
| 3 | 92-95 | Total number of securities proposed to be issued or the total amount for which the securities will be issued (approximately) | "For an aggregate consideration not exceeding Rs. 750,00,00,000 (Rupees Seven Hundred and Fifty Crore Only) or an equivalent amount thereof, in one or more tranches" | |

## Category 5 — Extraction / Document-Completeness Note (1 row)

| # | Line | Note | Flags |
|---|------|------|-------|
| 1 | 96 | A1 extraction meta-note: "[end of document - Annexure-I table ends at S.No. 3 as extracted; no further rows present in source PDF]" | `SCHEDULE_III_INCOMPLETE` — a standard Reg 30 / Schedule III QIP Annexure-I disclosure table typically carries further particulars beyond type-of-security / type-of-issuance / size (e.g., relevant date, pricing formula or floor-price basis, whether promoters/promoter group or related parties propose to participate, indicative timeline for completion, object/use of proceeds, existing promoter shareholding). None of these fields appear anywhere in the 2-page, 96-line, 100%-page-coverage extract. A1 confirms this is not an extraction gap (source PDF genuinely ends at S.No. 3). Carry forward to A3/A4: either (a) the company deferred these particulars to a later stage of the QIP process (pricing/floor-price/promoter-participation fields are commonly filled only at launch, not at the enabling-resolution stage), or (b) fields are missing. A3/A4 must not assume interpretation here — this ledger row exists purely to ensure the absence is reviewed, not silently dropped. |

## Category 6 — Digital Signature Block (5 rows)

| # | Line(s) | Element | Content (verbatim) | Flags |
|---|---------|---------|---------------------|-------|
| 1 | 58-61 | Digital signature marker | "Digitally signed by RASHMI GUPTA" | |
| 2 | 62-64 | Signature timestamp | "Date: 2026.08.03 18:18:45 +05'30'" | Cannot be cross-checked against a board-meeting end time (see Category 1, row 6, `MISSING_MEETING_TIMES`) — no meeting end time is disclosed, so the "signature before meeting concluded" check cannot be performed from this document alone |
| 3 | 67 | Signatory printed name | "Rashmi Gupta" | |
| 4 | 68 | Designation | "Company Secretary & Compliance Officer" | |
| 5 | 69 | Membership number | "M. No: A25382" | |

---

## Zero-Standing / Nil / Dash Line Items
Not applicable to this doctype instance: the filing contains no financial-statement table with recurring line items across periods (it is a single-event Reg 30 QIP enabling-resolution intimation with a 3-row Annexure). `zero_standing` count = 0. This is a mechanical non-applicability finding, not a suppressed check.

## Categories Not Applicable to This Document
Numbered financial-statement notes, auditor report paragraphs, consolidation entity list, board-outcome multi-agenda items (dividend, AR approval, director appointments, ESOP, auditor changes — only one agenda matter, the QIP resolution, appears in this filing), concall transcript elements (participants/turns/questions/spoken numbers), and investor-presentation elements (slides) are all not applicable — this is a 2-page Reg 30 intimation letter plus one Annexure. Their absence from this ledger is a doctype-scope finding, not a missed sweep.

---

## Grand Total
11 (letter_meta) + 2 (entities) + 7 (resolution_terms) + 3 (annexure_table_rows) + 1 (extraction_notes) + 5 (signature_block) = **29 enumerated disclosure units**

Flags raised: `MISSING_MEETING_TIMES`, `CONDITIONAL_ON_SHAREHOLDER_APPROVAL`, `SCHEDULE_III_INCOMPLETE`
