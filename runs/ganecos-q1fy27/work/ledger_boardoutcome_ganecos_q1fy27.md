# A2 ENUMERATION LEDGER — GANECOS Q1 FY27 — boardoutcome (Reg 30 re-appointment disclosure)

Source: extract_boardoutcome_ganecos_q1fy27.txt (75 lines, 2 pages, 100% coverage, no OCR pages flagged in header but OCR-grade artifacts present in body text — see DATA_QUALITY flags below)

```
=== A2 COUNT TEST ===
category: agenda_items          grep_count: 1   sweep_count: 1   match: yes
category: annexure_particulars  grep_count: 4   sweep_count: 4   match: yes
category: meeting_time_facts    grep_count: 2   sweep_count: 2   match: yes
category: signatory_blocks      grep_count: 1   sweep_count: 1   match: yes
category: related_party_facts   grep_count: 2   sweep_count: 2   match: yes
category: regulatory_references grep_count: 2   sweep_count: 2   match: yes
category: entities               grep_count: 1   sweep_count: 1   match: yes
category: notes                  grep_count: 0   sweep_count: 0   match: yes  [not present: no financial-statement notes section — governance letter only]
category: line_items             grep_count: 0   sweep_count: 0   match: yes  [not present: no financial table in this filing]
category: zero_standing          grep_count: 0   sweep_count: 0   match: yes  [not applicable: no standing financial line items exist to be nil/zero]
category: auditor_paras          grep_count: 0   sweep_count: 0   match: yes  [not present: no auditor's report attached to this filing]
category: turns                  grep_count: 0   sweep_count: 0   match: yes  [not applicable: doctype is a Board Outcome letter, not a concall transcript]
category: questions              grep_count: 0   sweep_count: 0   match: yes  [not applicable: no Q&A in this doctype]
category: mgmt_numbers           grep_count: 0   sweep_count: 0   match: yes  [not applicable: no spoken numbers in this doctype]
category: slides                 grep_count: 0   sweep_count: 0   match: yes  [not applicable: not an investor presentation]
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used for reconciliation (all run against extract_boardoutcome_ganecos_q1fy27.txt):
- agenda_items: `grep -n -E "has approved|Board of Directors.*meeting"` → 1
- annexure_particulars: `grep -n -E "Reason forchange|Date  of  Appointment|Brief Profile|Disclosure of  relationship"` → 4
- meeting_time_facts: `grep -o -E "commenced|concluded"` → 2 (both tokens fall on one physical line, so a plain line-count grep undercounts at 1; the -o occurrence count of 2 is the correct sweep-matching figure and is the number carried into the gate)
- signatory_blocks: `grep -n -E "Digitally signed by|Company Secretary"` → 1
- related_party_facts: `grep -n -E "son of|Group  Company|Ecoverse"` → 2
- regulatory_references: `grep -n -E "Regulation  30|Master  Circular"` → 2
- entities: `grep -n -E "Ecoverse  Limited"` → 1

---

## Table 1 — Board Outcome Letter: Agenda Item(s)

| # | Line(s) | Agenda item | First 15 words | Flags |
|---|---------|-------------|-----------------|-------|
| 1 | 19-23, 37-39 | Re-appointment of Mr. Sandeep Khandelwal as Senior Vice President, effective October 2026, 5-year term | "on the basis of recommendations of the Nomination and Remuneration Committee and Audit Committee, the Board of Directors..." | RECOMMENDING_COMMITTEES=NRC+Audit Committee |

Note: this is a single-agenda Board Outcome letter. No results/AR approval, AGM notice, record date, dividend, auditor change, scrutinizer, ESOP grant, or capital-raising resolution is present anywhere in the extract — each of these standard agenda categories is explicitly recorded here as **0 / not present** rather than omitted.

| Standard agenda category (per instruction) | Present? | Line(s) |
|---|---|---|
| Results/financial statements approval | 0 / not present | — |
| Annual Report / AGM notice | 0 / not present | — |
| Record date | 0 / not present | — |
| Dividend | 0 / not present | — |
| Director appointment (this one) | 1 / present | 19-23, 37-39 |
| Auditor change | 0 / not present | — |
| Scrutinizer appointment | 0 / not present | — |
| ESOP grant | 0 / not present | — |
| Capital-raising enabling resolution | 0 / not present | — |

## Table 2 — Meeting Metadata

| Fact | Line | Value | Flags |
|---|---|---|---|
| Meeting date | 21 | "at its meeting held today i.e. August 3, 2026" | — |
| Meeting commenced | 43 | 5:15 P.M. | — |
| Meeting concluded | 43 | "l:Q .0. P.M." — garbled/illegible in extraction | DATA_QUALITY (end time not machine-readable; duration of meeting cannot be computed from this extract) |

## Table 3 — Annexure ("Detailed Information ... SEBI Master Circular"): Particulars Table (4 rows)

| Sr. No. | Line(s) | Particular | Description (verbatim/paraphrased) | Flags |
|---|---|---|---|---|
| I (OCR of "1") | 53-54 | Reason for change | "Shri Sandeep Khandelwal is re-appointed as the Senior Vice President of the Company." | DATA_QUALITY (row numeral rendered as "I" not "1") |
| 2 | 55-56 | Date of Appointment & Term of Re-appointment | "Re-appointed with effect from [01st?] October, 2026, for a period of 5 (Five) years." | DATA_QUALITY (source text "oisrOctober,2026" — day digit not cleanly resolvable; letter body at line 22-23 gives only "October 202G" without a day, and also renders the year digit as "202G"; "5 (Pive) years" at line 23 similarly OCR-garbles "Five" as "Pive") |
| 3 | 57-70 | Brief Profile (in case of Appointment) | Age ~50 years (line 57, numeral displaced from its sentence by page-layout wrap); M.B.A. (Marketing), Institute of Management & Entrepreneurship Development (IMED), Pune; 20+ years' experience in trading of Textile Yarns and Fibre; Managing Director of M/s. Ganesha Ecoverse Limited (a Group Company listed at BSE-SME); Senior Management Personnel of the Company since year 2007; responsible for plant administration and operations | DATA_QUALITY (age numeral "50" appears on line 57 detached from "aged about ___ years" on line 58 — a page/column OCR wrap artifact); RELATED_PARTY (directorship in Ganesha Ecoverse Limited, a Group Company) |
| 4 | 71-75 | Disclosure of relationship between the Directors (in case of appointment of a director) | Table cell states "N.A." but is immediately followed parenthetically by: "Shri Sandeep Khandelwal is son of Shri Vishnu Dutt Khandelwal, Executive Vice-Chairman of the Company" | RELATED_PARTY; CONTRADICTION (cell answer "N.A." directly contradicts the relationship disclosed in the same cell's parenthetical — a relationship plainly exists and is disclosed, so "N.A." is not an accurate answer to the particular asked) |

## Table 4 — Related-Party / Relationship Facts (cross-referenced from Table 3, listed standalone per enumeration rule)

| # | Line(s) | Fact | Flags |
|---|---|---|---|
| 1 | 71-75 | Sandeep Khandelwal (appointee) is son of Vishnu Dutt Khandelwal, Executive Vice-Chairman of the Company | RELATED_PARTY, CONTRADICTION (see Table 3 row 4) |
| 2 | 62-65 | Sandeep Khandelwal holds Managing Director position in M/s. Ganesha Ecoverse Limited, described as "a Group Company listed at BSE-SME" | RELATED_PARTY, ENTITY (Ganesha Ecoverse Limited — group company, not part of this filing's own consolidation; no consolidation list exists in this doctype) |

## Table 5 — Regulatory Reference Citations

| # | Line(s) | Citation | Flags |
|---|---|---|---|
| 1 | 15-16, 18-19 | Regulation 30 read with Part A of Schedule III of SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 | — |
| 2 | 26-28 and again 48-50 | SEBI Master Circular No. HO/49/14/14(7)2025CFDPOD2/1/3762/2026 dated January 30, 2026 (cited once in letter body, once in annexure header — same circular, 2 citation instances) | — |

## Table 6 — Digital Signature / Signatory Block

| Field | Line(s) | Value | Flags |
|---|---|---|---|
| Signatory name | 33, 41 | Bharat Kumar Sajnani | — |
| Designation | 42 | Company Secretary-cum-Compliance Officer | — |
| Digital signature DN block | 33-39 | c=IN, o=Personal, title=1333, postalCode=208022, st=Uttar Pradesh, cn=Bharat Kumar Sajnani (pseudonym/serial hash fields present) | — |
| Signature timestamp | 40 | 2026.08.03 20:02:11 +05'30' | Meeting commenced 5:15 P.M. same day (line 43); signature timestamp (20:02:11, i.e., 8:02:11 P.M.) is after the stated commencement time and consistent with same-day post-meeting filing signoff — no red flag (concluded time is illegible per Table 2, so full sequencing cannot be verified beyond "signed same calendar day, after 5:15 P.M. start") |

## Table 7 — Corporate/Boilerplate Facts (non-substantive, enumerated for completeness)

| # | Line | Fact |
|---|---|---|
| 1 | 44 | Regd. Office & Works: Raipur (Rania), Kalpi Road, Distt. Kanpur Dehat-209 304 |
| 2 | 45 | Admn. Office: 113/216-B, Swaroop Nagar, Kanpur-208 002, India |
| 3 | 46 | CIN: L51109UP1987PLC009090 |
| 4 | 13-14 | Scrip Symbol: GANECOS; Scrip Code: 514167 |

## Table 8 — Standard Results-Filing Categories: Explicit Absence Record

Per instruction, every normal results-doc category is recorded below as 0 / not present rather than silently omitted from this ledger.

| Category | Count | Status |
|---|---|---|
| Numbered financial-statement notes | 0 | Not present — this filing carries no financial statements or notes section |
| Financial table line items (incl. zero/nil/dash standing items) | 0 | Not present — no P&L, balance sheet, or segment table anywhere in the extract |
| ZERO_STANDING line items | 0 | Not applicable — no financial table exists in which a standing line item could be nil |
| Auditor report paragraphs (opinion, EOM, Other Matters, Going Concern, UDIN, entity list) | 0 | Not present — no auditor's report attached to this Reg 30 letter |
| Consolidation entity list (subsidiaries/JVs with relationship type) | 0 | Not present — no consolidated financials in this doctype (the one entity mentioned, Ganesha Ecoverse Limited, is a related-party/group-company disclosure inside the annexure profile, not a consolidation-scope entity; captured in Table 4 instead) |
| Concall participants / speaker turns / questions / spoken management numbers | 0 | Not applicable — doctype is a Board Outcome letter, not a transcript |
| Investor presentation slides / slide numbers | 0 | Not applicable — doctype is a Board Outcome letter, not a deck |

---

## Summary Flag Roll-up

- RELATED_PARTY: 2 instances (Table 3 row 4 / Table 4 row 1 — son of Executive Vice-Chairman; Table 3 row 3 / Table 4 row 2 — MD of group company Ganesha Ecoverse Limited)
- CONTRADICTION: 1 instance (Table 3 row 4 — "N.A." answer contradicts the relationship disclosed in the same cell)
- DATA_QUALITY: 4 instances (Table 2 — illegible meeting-conclusion time; Table 3 row 1 — roman-numeral row marker; Table 3 row 2 — garbled effective date/year/term-in-words; Table 3 row 3 — displaced age numeral)
- ENTITY: 1 instance (Ganesha Ecoverse Limited, Table 4 row 2)

## Reconciliation Statement

Every applicable-category grep pass and manual line-by-line sweep produced identical counts (see COUNT TEST block above). The one instance requiring correction during reconciliation was meeting_time_facts: a naive line-count grep for "commenced|concluded" returns 1 because both tokens sit on the same physical line (line 43); the occurrence-count grep (`-o`) and the manual sweep both correctly identify 2 discrete facts (commencement time, conclusion time) on that line. The occurrence count (2) is the figure carried into the gate, and it matches the manual sweep. GATE A2: PASS.
