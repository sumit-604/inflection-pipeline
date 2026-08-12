# A2 ENUMERATOR LEDGER — HCP Plastene Bulkpack Ltd (526717), Q1FY27
Source: extract_reg30esop_526717_q1fy27.txt (Regulation 30 ESOP allotment disclosure, 3 pages, doc lines 1-131)
Line numbers below are the A1 extract's own embedded document line numbers (not Read-tool cat -n numbers).

```
=== A2 COUNT TEST ===
category: annexure_rows   grep_count: 12   sweep_count: 12   match: yes
category: disclosure_fields (letter body)   grep_count: n/a (no repeating numbered pattern; enumerated by manual sweep only)   sweep_count: 11   match: n/a
category: signature_blocks   grep_count: 1   sweep_count: 1   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep method for annexure_rows: `sed -n '110,144p' <extract> | grep -noP "^\d+\t\s+\d{1,2}\.?\s"` restricted to the Annexure A table body (doc lines 96-130). Raw unrestricted grep across the full file returned 13 hits; the 13th (doc line 133, "9 Hep plastene Bulkpack Ltd" footer/letterhead OCR noise) is not an annexure item and was excluded on manual inspection — reconciled grep count is 12, matching the manual sweep of items S.No. 1-12.

---

## TABLE 1 — COVER LETTER DISCLOSURE FIELDS (Regulation 30 notice body)

| # | Line(s) | Field | Content (verbatim / paraphrase) | Flags |
|---|---------|-------|----------------------------------|-------|
| 1 | 8 | Letter date | 12 August 2026 | |
| 2 | 12-16 | Addressee | BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai - 400 001, Maharashtra, India (address contains OCR typo "Mumbeai") | |
| 3 | 19 | Scrip Code | 526717 | |
| 4 | 20 | ISIN | INE136C01044 | |
| 5 | 22-24 | Subject line | Disclosure under Regulation 30 read with Schedule III of SEBI (LODR) Regulations, 2015 | |
| 6 | 29-35 | Allotment approval statement | Stakeholders Relationship Committee, on 12 August 2026, approved allotment of 16,780 equity shares of face value Rs 10 each, fully paid up, pursuant to exercise of vested stock options at exercise price Rs 10 per option under ESOP Scheme 2022 (as amended) | |
| 7 | 37-38 | Pari-passu statement | Shares allotted rank pari-passu with existing equity shares in all respects | |
| 8 | 40-42 | Paid-up capital — before allotment | Rupees 106,748,370 (10,674,837 shares of Rs 10 each) | |
| 9 | 40-42 | Paid-up capital — after allotment | Rupees 106,916,170 (106,916,170 as printed in source — internally inconsistent with share count arithmetic; see note below) | ARITHMETIC_FLAG |
| 10 | 44-46 | Regulatory basis for Annexure A | SEBI Master Circular No. HO/49/14/14(7)2025-CFD-POD2/1/3762/2026 dated 30 January 2026; details enclosed as Annexure A | |
| 11 | 61-62 | Website / dissemination statement | "The same will be made available on the Company's website i.e. www.hpbl.in. This is for your information, record, and appropriate dissemination." | |

Note on row 9 (ARITHMETIC_FLAG, not interpretation — mechanical cross-check only, for A3/A4 to resolve): source text reads "increased ... to Rupees 106916170 (106916170 shares of rupees 10 each)" — the post-allotment rupee figure and post-allotment share-count figure are printed as the identical number (106916170), which is internally inconsistent (post-allotment shares should read 10,691,617 shares of Rs 10 each = Rs 106,916,170 capital, not 106,916,170 shares). Also note pre-allotment shares (10,674,837) + shares allotted (16,780) = 10,691,617 shares, consistent with the capital figure Rs 106,916,170 but not with the "106916170 shares" wording as printed. Flagged verbatim for downstream reconciliation; not corrected here.

---

## TABLE 2 — ANNEXURE A: DETAILS OF ESOP ALLOTMENT (12 rows, S.No. 1-12)

| S.No. | Line(s) | Particulars | Details | Flags |
|-------|---------|-------------|---------|-------|
| 1 | 96-98 | Brief details of options granted | Not Applicable as the present instance is for allotment of shares upon exercise of options under ESOP Scheme 2022 | ZERO_STANDING (field answered "Not Applicable") |
| 2 | 99-102 | Whether the scheme is in terms of SEBI (SBEB) Regulations, 2021 (if applicable) | Yes | |
| 3 | 103-105 | Total number of shares covered by these options | Total 2,50,000 options covered in the scheme; of that, 16,780 equity shares of face value Rs 10 each exercised for the current allotment | |
| 4 | 106-107 | Exercise Price | Rupees 10 (Rupee Ten Only) per Option | |
| 5 | 109-110 | Time within which option may be exercised | As per ESOP scheme | |
| 6 | 112-113 | Brief details of significant terms | As per ESOP Scheme of the Company | |
| 7 | 115-117 | Subsequent changes or cancellation or exercise of such options | Not Applicable | ZERO_STANDING (field answered "Not Applicable") |
| 8 | 118-119 | Options vested | 17,680 (Seventeen Thousand Six Hundred and Eighty) Options | |
| 9 | 121-122 | Options exercised | 16,780 (Sixteen Thousand, Seven Hundred and Eighty) Options | |
| 10 | 123-124 | Money realized by exercise of options | Rupees 167,800 (One Lakh Sixty-Seven Thousand and Eight Hundred Only) | |
| 11 | 126-128 | Total number of shares arising as a result of exercise of option | 16,780 (Sixteen Thousand, Seven Hundred and Eighty) equity shares, of Face Value Rupees 10 each | |
| 12 | 129-130 | Options lapsed | 29,450 (Twenty-Nine Thousand Four Hundred and Fifty Only) | |

Cross-check note (mechanical, not interpretive): row 3 states 250,000 options total covered by the scheme; row 8 (vested, 17,680) + row 9 (exercised, 16,780) + row 12 (lapsed, 29,450) account for only a small fraction of the 250,000 scheme pool — the remainder (unvested / not-yet-reported) is not disclosed in this Annexure. This is a completeness gap in the source document itself, not a ledger omission; flagged for A3/A4.

---

## TABLE 3 — DIGITAL SIGNATURE BLOCK

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 67-78 | Rishabh Kumar Jain | Company Secretary and Compliance Officer (Membership Number: F7271) | Digitally signed 2026.08.12 17:35:54 +05'30' | Timestamp (17:35:54) is same-day as, and after, the letter date (12 August 2026) and after the Stakeholders Relationship Committee approval referenced in the letter body (line 30: "today i.e. 12 August 2026"); no separate board-meeting start/end time is disclosed in this document (this is a committee-approval notice, not a Board Outcome letter with a stated meeting window), so no SIGNATURE_BEFORE_MEETING_END check is computable from this document alone. |

---

## ENUMERATION CATEGORIES NOT PRESENT IN THIS DOCUMENT (explicitly noted per anti-miss protocol, not silently skipped)

- Numbered notes section (financial-statement style numbered notes): NOT PRESENT — this is a Regulation 30 event disclosure, not a results/financial-statement filing with a notes section.
- Financial statement line items (P&L / balance sheet): NOT PRESENT in this document.
- Board Outcome letter multi-item agenda (AR approval, AGM notice, record date, dividend, director appointments, auditor changes, scrutinizer, capital-raising resolutions): NOT PRESENT — the letter discloses a single Stakeholders Relationship Committee action (ESOP allotment); no other agenda items are stated. Committee is SRC, not the full Board.
- Director profiles / DIN / term dates: NOT PRESENT.
- Auditor report paragraphs (opinion, EOM, Other Matters, Going Concern, entity list, UDIN): NOT PRESENT.
- Consolidation entity list: NOT PRESENT.

---
```yaml
stage: A2-enumerator
company: "526717"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/526717-q1fy27/work/ledger_reg30esop_526717_q1fy27.md"
counts:
  notes: 0
  line_items: 12
  zero_standing: 2
  agenda_items: 1
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ARITHMETIC_FLAG]
gate_a2: pass
mismatch_note: ""
```
