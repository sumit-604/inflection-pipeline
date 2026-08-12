# A2 Enumeration Ledger — 526717 (HCP Plastene Bulkpack Ltd), Q1FY27
Doctype: results (Regulation 30 event disclosure — CFO resignation, 3 pages)
Source: /home/user/inflection-pipeline/runs/526717-q1fy27/work/extract_reg30cfo_526717_q1fy27.txt

Note on doctype fit: this is not a quarterly financial results filing. It carries
no P&L/balance-sheet line items, no numbered accounting notes, no Board Outcome
agenda, no auditor report, no consolidation entity list, no concall transcript,
no investor-presentation slides. Rules 1, 3, 5, 6 of the RESULTS FILING
enumeration template therefore yield zero applicable rows (recorded as 0, not
omitted). Rule 2 (every table line item, including nil-valued standing items)
applies to the Annexure A table. Rule 7 (signature blocks) applies to all three
signature/countersignature instances. The two prose letters (BSE letter, CFO's
personal resignation letter) are enumerated field-by-field per the task
instruction ("every disclosure field").

```
=== A2 COUNT TEST ===
category: disclosure_letter_fields (BSE Reg 30 letter, page 1)   grep_count: 17  sweep_count: 17  match: yes
category: annexure_a_fields (Annexure A table, page 2)           grep_count: 6   sweep_count: 6   match: yes
category: resignation_letter_fields (CFO's personal letter, p3)  grep_count: 14  sweep_count: 14  match: yes
category: signature_blocks (all 3 pages)                         grep_count: 3   sweep_count: 3   match: yes
category: notes (numbered accounting notes)                      grep_count: 0   sweep_count: 0   match: yes (n/a — no financial notes in this filing)
category: line_items (financial table rows)                      grep_count: 0   sweep_count: 0   match: yes (n/a — no financial tables; Annexure A tracked separately above)
category: agenda_items (Board Outcome letter)                    grep_count: 0   sweep_count: 0   match: yes (n/a — no Board Outcome letter attached to this event disclosure)
category: auditor_paras                                          grep_count: 0   sweep_count: 0   match: yes (n/a — no auditor report)
category: entities (consolidation list)                          grep_count: 0   sweep_count: 0   match: yes (n/a — no consolidation list)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on the count test: for the two prose letters and the
signature blocks, "grep_count" is a scoped `grep -n -E` pass (patterns and
raw hits shown below each table) anchored to the start line of each discrete
field/paragraph within the relevant page range of the extract; continuation
lines are folded into the same row (line number = anchor line). "sweep_count"
is an independent line-by-line manual read of the same page range. The
Annexure A grep pass (the GATE A2 target named in the task) used the row
pattern `^[0-9]+\.?\s+[A-Z]` scoped to lines 95-108 (the table body) — this
excludes two false-positive matches elsewhere in the document (line 79 "9 Hep
Plastene..." footer boilerplate, and line 134 "1 further confirm..." which is
an OCR misread of "I further confirm"). First pass on the personal
resignation letter (Table 3) mismatched 13 (grep) vs 14 (sweep) because the
initial grep pattern used a strict `^` anchor that missed the indented
countersignature header line 147 ("FOR, HCP P[LASTEN]E BULKPACK LIMITED");
re-run with a `^\s*` leading-whitespace allowance caught it, bringing grep to
14 and reconciling against the manual sweep. All four categories now match.

---

## Table 1 — Main Disclosure Letter Fields (BSE Reg 30 covering letter, page 1)
Grep pattern (scoped lines 27-81, allowing leading whitespace):
`^\s*(12t August 2026|To|BSE Limited|Scrip Code:|ISIN:|Subject:|Dear Sir|Pursuant to Regulation|Annexure A\.|Thank you\.|Yours faithfully|For HCP)` plus unanchored `Rishabh|Company Secretary and Compliance Officer|Membership Number:|CIN:|www\.hpbl\.in`

| # | Line | Field | Content (verbatim, truncated where multi-line) | Flags |
|---|------|-------|--------------------------------------------------|-------|
| 1 | 34 | Letter date | "12t August 2026" [OCR: "12th August 2026"] | OCR_ARTIFACT |
| 2 | 36 | Addressee salutation | "To" | |
| 3 | 38-42 | Addressee block | "BSE Limited / Phiroze Jeejeebhoy Towers / Dalal Street / Mumbeai - 400 001 / Maharashtra, India" [OCR: "Mumbai"] | OCR_ARTIFACT |
| 4 | 45 | Scrip Code | "526717" | |
| 5 | 46 | ISIN | "INE136C01044" | |
| 6 | 48-50 | Subject line | "Disclosure under Regulation 30 read Schedule III of the Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015 ("SEBI Listing Regulations")" | |
| 7 | 52 | Salutation | "Dear Sir/ Madam," | |
| 8 | 55-58 | Body statement | Regulatory citation (Reg 30) + resignation announcement: Mr. Dhrumil PranavKumar Shah, CFO, "has tendered his resignation from the position of Chief Financial Officer... vide his resignation letter dated 12T August2026, for further career opportunity." | OCR_ARTIFACT |
| 9 | 60-62 | Reference to Annexure A | Cross-reference to enclosed Annexure A carrying the SEBI-mandated resignation-detail fields | |
| 10 | 66 | Closing | "Thank you." | |
| 11 | 67 | Valediction | "Yours faithfully" | |
| 12 | 69 | Company signature-block header | "For HCP PLASTENE BULKPACK LIMITED" | |
| 13 | 71 | Signature image (OCR of handwritten signature) | "Rishabh 2oty / Kumar Jain e s" [garbled OCR of signature] | OCR_ARTIFACT |
| 14 | 73 | Signatory printed name | "Rishabh Kumar Jain" | |
| 15 | 74 | Signatory designation | "Company Secretary and Compliance Officer" | |
| 16 | 75 | Membership Number | "F7271" | |
| 17 | 78-80 | Footer / letterhead block | CIN: L25200GJ1984PLC050560; website www.hpbl.in; email info@hpbl.in; registered address H.B. Jirawla House, 13, Navbharat Society, Usmanpura, Ahmedabad, Gujarat 380013; phone 0179 27561000 | |

Sweep count: 17. Grep count: 17. Match: yes.

---

## Table 2 — Annexure A Fields (SEBI-mandated resignation-detail table, page 2)
**This is the GATE A2 primary target named in the task.**
Grep pattern (scoped lines 95-108, table body only): `^[0-9]+\.?\s+[A-Z]`

| Sr.No. (as printed) | Line | Field label | Information given | Flags |
|---|------|-------------|--------------------|-------|
| 1 | 96 | Name of Director / KMP | "Mr. Dhrumil PranavKumar Shah" | |
| 2 | 97-100 | Reason for Change (viz. appointment, resignation, removal, death or otherwise) | "Mr. Dhrumil Shah has resigned from the post of Chief Financial Officer w.e.f. 12t August 2026 for further career opportunity." [verbatim, OCR: "12th August 2026"] | OCR_ARTIFACT |
| 3. | 101-102 | Date of appointment/cessation (as applicable) & term of appointment | "12% August, 2026" [OCR: "12th August 2026"]; no term-of-appointment value given (cessation, not appointment) | OCR_ARTIFACT |
| 4. | 103 | Brief Profile (in case of appointment) | "NA" | ZERO_STANDING |
| 5. | 104-106 | The disclosure of relationships between director (in case of appointment of a director) | "NA" | ZERO_STANDING |
| 5. (mislabeled — should be Sr.No. 6) | 107 | Resignation letter | "Attached" | NUMBERING_ANOMALY |

Sweep count: 6. Grep count: 6. Match: yes.

Flag detail — `NUMBERING_ANOMALY`: the printed Annexure A table has two rows
both labeled Sr.No. "5." (the relationships-disclosure row at line 104 and the
"Resignation letter" row at line 107); the second is a sequencing error in the
source filing (should read "6."). Enumerated verbatim as printed; not
corrected.

Flag detail — `ZERO_STANDING` (rows 4 and 5): both are template fields that
exist in Annexure A to cover the appointment case (brief profile,
director-relationship disclosure) and are populated "NA" here because this is
a resignation, not an appointment. Recorded per the operating rule rather than
dropped.

---

## Table 3 — CFO's Personal Resignation Letter Fields (page 3)
Grep pattern (scoped lines 116-152, allowing leading whitespace):
`^\s*(Date:|To|the Board of Directors|Subject:|Dear Sir,|With reference to|1 further confirm|I am grateful|Thanking you|Yours faithfully|FOR, HCP|Dhrumil Shah|Chief Financial Officer)` plus unanchored `DIRECTO`

| # | Line | Field | Content (verbatim, truncated where multi-line) | Flags |
|---|------|-------|--------------------------------------------------|-------|
| 1 | 117 | Letter date | "Date: 12/08/2026" | |
| 2 | 119 | Addressee salutation | "To" | |
| 3 | 120-124 | Addressee block | "the Board of Directors of / HCP Plastene Bulkpack Limited / ].B. Jirawal House, Navbharat Soc., / Nr. Panchsil Bus Stand, / Usmanpura, Ahmedabad -380013" [OCR: "H.B. Jirawal House"] | OCR_ARTIFACT |
| 4 | 126 | Subject line | "Resignation from the office of Chief Financial Officer (CFO)" | |
| 5 | 129 | Salutation | "Dear Sir," | |
| 6 | 130-132 | Body paragraph 1 — resignation statement | "With reference to the above subject, I hereby tender my resignation from the post of Chief Financial Officer (CFO) of the Company from 12/08/2026 for turther [OCR: further] career opportunity. I request you to take the same on record." | OCR_ARTIFACT |
| 7 | 134-135 | Body paragraph 2 — no-material-reason confirmation | "I further confirm that there is no material reason other than mentioned above for my resignation." [OCR misread: source text shows "1 further confirm", i.e. "I" rendered as digit "1"] | OCR_ARTIFACT |
| 8 | 137-140 | Body paragraph 3 — gratitude / thanks | "I am grateful to the Company, shareholders, Board of Directors and all other concerned for giving me an opportunity to serve the Company and also thankful for the co-operation extended to me by all of you to enable me to perform my duties in a best possible manner." | |
| 9 | 142 | Closing | "Thanking you" | |
| 10 | 144 | Valediction + garbled countersignature mark | "Yours faithfully" + illegible OCR fragment "Ac ngdz&" (right-hand-side signature image) | OCR_ARTIFACT |
| 11 | 147 | Company countersignature block header | "FOR, HCP P[LASTEN]E BULKPACK LIMITED" [OCR-truncated] | OCR_ARTIFACT |
| 12 | 148 | Signatory (CFO) printed name | "Dhrumil Shah" + adjacent illegible OCR mark ("I") | OCR_ARTIFACT |
| 13 | 150 | Signatory (CFO) designation | "Chief Financial Officer" | |
| 14 | 151 | Company countersignature designation fragment | "DIRECTO!" [OCR-truncated, evidently "DIRECTOR"]; no name given for the countersigning director | OCR_ARTIFACT, SIGNATORY_UNIDENTIFIED |

Sweep count: 14. Grep count: 14. Match: yes.

Flag detail — `SIGNATORY_UNIDENTIFIED`: the company's countersignature block
on the CFO's personal letter (right-hand side, lines 144-151) gives no
printed name for the countersigning director — only a garbled designation
fragment "DIRECTO!". Which director countersigned is NOT FOUND in this
extract.

---

## Table 4 — Signature / Countersignature Blocks (rule 7, all pages)
Grep pattern (whole document, unanchored): `Company Secretary and Compliance Officer|^Dhrumil Shah|^Chief Financial Officer$|DIRECTO` — 4 raw line hits (lines 74, 148, 150, 151) collapsing to 3 logical blocks (lines 148 and 150 are the name and designation of one CFO signature block).

| # | Page | Lines | Signatory | Designation | Timestamp | Flags |
|---|------|-------|-----------|-------------|-----------|-------|
| 1 | 1 | 69-75 | Rishabh Kumar Jain (Membership F7271) | Company Secretary and Compliance Officer | NOT FOUND — only the letter date (12 August 2026) is given; no separate signing/digital-signature timestamp in the extract | NO_TIMESTAMP |
| 2 | 3 | 148-150 | Dhrumil Shah | Chief Financial Officer (resigning) | NOT FOUND — only the letter date (12/08/2026) is given; no separate signing/digital-signature timestamp | NO_TIMESTAMP |
| 3 | 3 | 144-151 | NOT FOUND (name illegible/absent) | "DIRECTO!" [OCR-truncated, evidently Director] — countersigning the CFO's personal letter "FOR, HCP PLASTENE BULKPACK LIMITED" | NOT FOUND | NO_TIMESTAMP, SIGNATORY_UNIDENTIFIED |

Sweep count: 3. Grep count: 3 (logical blocks; 4 raw grep line-hits, reconciled as noted above). Match: yes.

Note: rule 7 flags "a results signature timestamp before the board meeting
concluded" as suspicious. This document contains no board-meeting timing
reference at all (it is a standalone Reg 30 event disclosure, not a Board
Outcome letter), so that specific cross-check does not apply; the absence of
any signature timestamp anywhere in the filing is itself flagged
(`NO_TIMESTAMP`) as a gap for A3/A4 to weigh.

---

## Categories with zero applicable rows (recorded per instruction, not omitted)
- Numbered accounting/explanatory notes (rule 1): 0 — this is not a financial results filing.
- Financial table line items (rule 2, beyond Annexure A already tracked in Table 2): 0.
- Board Outcome letter agenda items (rule 3): 0 — no Board Outcome letter is attached to this event disclosure; only the CFO resignation letter and its Annexure A.
- Auditor report paragraphs (rule 5): 0.
- Consolidation entity list (rule 6): 0.

---

## Flags raised (roll-up)
- `ZERO_STANDING` — Annexure A rows 4 and 5 ("Brief Profile" and "disclosure of relationships", both NA).
- `NUMBERING_ANOMALY` — Annexure A has two rows both printed as Sr.No. "5." (relationships-disclosure row and Resignation-letter row); the second should read "6."
- `OCR_ARTIFACT` — multiple instances across all three pages (dates rendered "12t"/"12%" instead of "12th", "Mumbeai" for "Mumbai", "appeintment"/"remeval" for "appointment"/"removal", "turther" for "further", "1 further confirm" for "I further confirm", garbled signature-image OCR fragments, "DIRECTO!" truncation). Listed per row above; does not change any substantive fact but affects verbatim-transcription fidelity.
- `SIGNATORY_UNIDENTIFIED` — the director countersigning the CFO's personal resignation letter (page 3) is not named in the extract.
- `NO_TIMESTAMP` — none of the three signature blocks in this filing carries a digital-signature timestamp; only the letter dates (12 August 2026 / 12/08/2026) are given.

## Total rows enumerated across all tables: 40
(Table 1: 17 + Table 2: 6 + Table 3: 14 + Table 4: 3 = 40. Table 4 rows are a
cross-reference summary of signature-block content already captured within
Tables 1 and 3, so the ledger's unique-line-number field count is 37 [Table 1
+ Table 2 + Table 3]; Table 4 is retained as a separate rule-7-mandated table
per instruction and is not double-counted toward `line_items` in the YAML
summary below.)
