# A2 Enumeration Ledger — Paisalo Digital Ltd, Q1 FY27, Board Outcome Intimation
Source: `runs/paisalo-q1fy27/work/extract_results_paisalo_q1fy27_boardintimation.txt`
(122 lines, 2 pages; SEBI Reg 30 Board Outcome intimation, NOT a quarterly financial
results filing — no P&L/balance-sheet line items exist in this document, so the
`line_items`/`zero_standing`/`auditor_paras`/`entities` categories from the
standard results template are N/A for this doctype instance and are recorded
as N/A below rather than silently omitted.)

```
=== A2 COUNT TEST ===
category: top_level_agenda_items     grep_count: 3   sweep_count: 3   match: yes
category: embedded_sub_disclosures   grep_count: 3   sweep_count: 3   match: yes
category: annexure_table_rows        grep_count: 5   sweep_count: 5   match: yes
category: board_meeting_times        grep_count: 2   sweep_count: 2   match: yes
category: digital_signature_blocks   grep_count: 2   sweep_count: 2   match: yes
category: routing_recipients         grep_count: 4   sweep_count: 4   match: yes
category: document_identifiers       grep_count: 3   sweep_count: 3   match: yes
category: line_items (financial)     grep_count: N/A sweep_count: N/A match: n/a (doctype has none)
category: notes                      grep_count: N/A sweep_count: N/A match: n/a (doctype has none)
category: auditor_paras              grep_count: N/A sweep_count: N/A match: n/a (doctype has none)
category: entities                   grep_count: N/A sweep_count: N/A match: n/a (doctype has none)
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (against the extract file):
- `grep -n -E "^\s*[0-9]+\.\s+[A-Z]" <extract> | awk -F: '$1<71'` -> 3 (excludes the
  CC list at line 72, which reuses "1." / "2." numbering for addressees, not agenda
  items)
- `grep -o -E "^\s*(i|ii)\)\s"` (director sub-actions) -> 2, plus
  `grep -n -i "dividend"` on the letter body -> 1 (line 45) = 3 embedded sub-disclosures
- `grep -n -E "^\s{0,3}[0-9]\s+[A-Z]"` (Annexure Sr. No. rows) -> 5
- `grep -o -E "[0-9]{1,2}:[0-9]{2} [AP]\.M\."` -> 2 (start, end)
- `grep -n -i "digitally signed"` -> 2
- `grep -o -E "BSE Limited|National Stock Exchange of India Limited|Afrinex Exchange Listing Centre|India International Exchange \(IFSC\) Ltd\."` -> 4
- `grep -n -E "Scrip Code|NCDs-|CPs-"` -> 3

---

## 1. Top-level Board Outcome agenda items (letter body, lines 15-71)

| # | Line(s) | Agenda item | First 15 words | Flags |
|---|---------|-------------|-----------------|-------|
| 1 | 38-40 | Fixation of 34th AGM date | "Fixed the date of the 34th Annual General Meeting (AGM) of the Company to be held" | — |
| 2 | 43-46 | Fixation of Book Closure dates | "Fixed the Book Closure dates, from September 15, 2026, to September 21, 2026 (both dates" | — |
| 3 | 48-54 | Recommend the appointment/re-appointment of Director (parent item; contains two sub-actions i/ii, see Section 2) | "Considered, approved, and recommended to the shareholders for their approval in the 34th AGM, the" | — |

Note: only 3 top-level numbered agenda items appear. No AR/financial-results
approval, no auditor appointment/change, no scrutinizer appointment, no ESOP
grant, no capital-raising enabling resolution is present in this Board
Outcome — confirmed by manual sweep of the full 122-line extract, not
inferred. `detected_quarter` per the A1 header is itself flagged UNKNOWN
because this document carries no Q1 FY27 financial content at all.

## 2. Embedded sub-disclosures within agenda items

| # | Line(s) | Item | Sub-disclosure | First 15 words | Flags |
|---|---------|------|-----------------|-----------------|-------|
| 2a | 44-46 | (within item 2) | Dividend reference | "for the 34th AGM and final Dividend payment for FY 2025-26, subject to approval of" | Note: FY2025-26 final dividend, NOT a Q1FY27 item; book closure window doubles as record-date mechanism for both AGM voting and dividend payment |
| 3a | 51-52 | (within item 3) | Director action (i): retirement by rotation and re-appointment as ordinary Director | "Mr. Santanu Agarwal (DIN: 07069797), as a Director who is liable to retire by rotation" | DIN: 07069797 |
| 3b | 53-54 | (within item 3) | Director action (ii): re-appointment as Whole Time Director / Deputy Managing Director for a further term | "Mr. Santanu Agarwal (DIN: 07069797) as Whole Time Director designated as Deputy Managing Director for" | DIN: 07069797; new term May 06, 2027 - May 05, 2032; RELATED_PARTY (son of MD, see Annexure row 4) |

## 3. Board meeting timing

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 60 | Meeting start time | 11:30 A.M. | — |
| 2 | 60 | Meeting end time | 12:25 P.M. | Duration ~55 minutes for a meeting covering AGM fixation, book closure/dividend reference, and a director re-appointment recommendation — a short meeting, noted for reference, not flagged as anomalous |

## 4. Digital signature blocks

| # | Line(s) | Signatory | Designation | Timestamp | Document location | Flags |
|---|---------|-----------|-------------|-----------|--------------------|-------|
| 1 | 63-68 | MANENDRA SINGH | Company Secretary | 2026.08.05 12:28:27 +05'30' | End of covering letter (page 1) | Timestamp is 3 minutes AFTER the board meeting concluded (12:25 P.M.) — expected sequencing, not a flag |
| 2 | 119-123 | MANENDRA SINGH | (Company Secretary, per letter; not re-stated in Annexure block) | 2026.08.05 12:28:37 +05'30' | End of Annexure I (page 2) | 10 seconds after signature #1; both timestamps post-date meeting conclusion — no BACKDATED_SIGNATURE flag warranted |

## 5. Annexure I — Director disclosure table (Regulation 30 / SEBI Circular dated Jan 30, 2026)

Table covers a single director (Mr. Santanu Agarwal, DIN 07069797) across two
concurrent proposed actions (rotation retirement/re-appointment as ordinary
Director, and re-appointment as Deputy Managing Director). Rows 1-2 carry
distinct content per action; rows 3-5 apply to the director as a whole.

| Sr. No | Line(s) | Disclosure requirement | Content (rotation re-appointment / DMD re-appointment) | Flags |
|--------|---------|--------------------------|----------------------------------------------------------|-------|
| 1 | 82-91 | Reason for change (appointment/resignation/removal/death/otherwise) | Rotation: retiring by rotation under Sec. 152, Companies Act 2013, offered himself for re-appointment. DMD: re-appointment under Sec. 196, Companies Act 2013, on NRC recommendation | DUAL_CONTENT (one row, two distinct legal bases) |
| 2 | 94-97 | Date of appointment/re-appointment | Rotation: effective 34th AGM, Sept 21, 2026. DMD: subject to shareholder approval, term May 6, 2027 - May 5, 2032 | DUAL_CONTENT; term start (May 2027) is ~9 months after this board meeting and ~8 months after the AGM — a forward-dated term commencement |
| 3 | 99-103 | Brief profile (in case of appointment) | Deputy Managing Director; B.Com and law degrees, Amity University Noida; ~10 years experience in business planning, operations, IT strategy, risk management | — |
| 4 | 104-107 | Disclosure of relationships between directors | Santanu Agarwal is the son of Mr. Sunil Purushottam Agarwal, Managing Director of the Company | RELATED_PARTY — promoter-family succession appointment |
| 5 | 108-118 | Information per BSE Circular LIST/COMP/14/2018-19 and NSE Circulars (debarment status) | Not debarred from holding office of Director by SEBI or any other Authority | — |

## 6. Letter routing / addressees and CC recipients

| # | Line(s) | Recipient | Type | Flags |
|---|---------|-----------|------|-------|
| 1 | 17-21 | BSE Limited, Dept. of Corporate Relationship, Mumbai | Primary addressee | — |
| 2 | 17-20 | National Stock Exchange of India Limited, Listing Dept., BKC | Primary addressee | — |
| 3 | 72 | Afrinex Exchange Listing Centre | CC | — |
| 4 | 72 | India International Exchange (IFSC) Ltd. | CC | — |

## 7. Document identifiers (scrip/security codes referenced)

| # | Line(s) | Identifier type | Value | Flags |
|---|---------|-------------------|-------|-------|
| 1 | 23 | Equity scrip code / symbol | BSE Equity-532900; NSE SCRIP SYMBOL PAISALO | — |
| 2 | 24-25 | NCD series codes | 975107, 975202, 975251, 975329, 975437, 975640, 975865, 976752, 977004, 977097, 977278, 977279, 977358, 977371, 977643 (15 series) | — |
| 3 | 26 | CP series codes | 731429, 731434, 731455, 731624, 732088 (5 series) | — |

---

## Categories not present in this document (confirmed by full manual sweep, not omitted)
- Financial results / numbered notes / financial-table line items (incl. zero/nil/dash standing items) — N/A, this filing carries no financial figures (per A1 header, `unit_convention: N/A`)
- Auditor report paragraphs (opinion, EOM, Other Matters, Going Concern, UDIN) — N/A, no auditor report attached
- Consolidation entity list — N/A, no subsidiary/consolidation table in this document
- AR approval, auditor appointment/change, scrutinizer appointment, ESOP grants, capital-raising enabling resolutions — none of these agenda items appear; only AGM date, book closure/dividend reference, and one director appointment/re-appointment item are present

## Total enumerated disclosure units
3 (top-level agenda items) + 3 (embedded sub-disclosures) + 2 (meeting times) +
2 (signature blocks) + 5 (Annexure rows) + 4 (routing recipients) + 3 (document
identifiers) = **22 rows**, all carrying a line number, zero rows dropped.
