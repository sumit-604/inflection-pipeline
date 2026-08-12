# A2 Completeness Ledger — Reg 30 AoA Adoption Disclosure
Company: HCP Plastene Bulkpack Ltd (526717) | Quarter tag: q1fy27 | Doctype: results (Reg 30 event disclosure)
Source: extract_reg30aoa_526717_q1fy27.txt (1-page filing, 68 extract lines incl. header)

## DOCUMENT NATURE NOTE
This is not a quarterly financial results filing or a comprehensive Board Outcome
letter. It is a single-subject Regulation 30 event disclosure: the Board approved
adoption of a new set of Articles of Association at its meeting held 12 August
2026, subject to shareholder (AGM) approval. It contains no financial tables, no
numbered notes, no auditor report, and no consolidation/entity list. The standard
ENUMERATE — RESULTS FILING categories (notes, line items, auditor paragraphs,
entities, annexures) are therefore enumerated and confirmed at zero (N/A), and the
document's actual discrete disclosure units — filing metadata, salutation, body
paragraphs, the single agenda item, the closing block, the digital signature block
(rule 7), and the footer/corporate-detail block — are enumerated in full below so
nothing is dropped.

=== A2 COUNT TEST ===
category: notes                    grep_count: 0   sweep_count: 0   match: yes
category: line_items               grep_count: 0   sweep_count: 0   match: yes
category: filing_metadata_fields   grep_count: 6   sweep_count: 6   match: yes
category: salutation               grep_count: 1   sweep_count: 1   match: yes
category: disclosure_body_paras    grep_count: 2   sweep_count: 2   match: yes
category: agenda_items             grep_count: 1   sweep_count: 1   match: yes
category: closing_block            grep_count: 3   sweep_count: 3   match: yes
category: signature_block          grep_count: 7   sweep_count: 7   match: yes
category: footer_corporate_fields  grep_count: 3   sweep_count: 3   match: yes
category: auditor_paras            grep_count: 0   sweep_count: 0   match: yes
category: entities                 grep_count: 0   sweep_count: 0   match: yes
category: annexures                grep_count: 0   sweep_count: 0   match: yes
gate_a2: pass
=== END COUNT TEST ===

Note on line_items grep: a naive numeric-pair regex (`^\s*[A-Za-z].*[0-9,]{3,}\s+[0-9,]{3,}`)
returns 3 raw hits — line 29 (postal code "Mumbeai - 400 001"), line 59 (OCR
fragment of the garbled signature timestamp), line 68 (registered address +
phone number). Manual sweep confirms none of these are financial statement line
items; this document contains no financial table of any kind (A1 header:
"unit_convention: N/A"). True line_items count is 0/0, reported above.

Note on notes grep: `grep -n -E "^\s*[0-9]+\.\s"` returns 0 matches. Manual sweep
of all 68 extract lines confirms no numbered notes, footnotes (asterisk/dagger),
or "Note:"-prefixed text anywhere in the document.

---

## Table 1 — Filing Metadata Fields
| # | Field | Line(s) | Content | Flags |
|---|---|---|---|---|
| 1 | Letter date | 22 | "12 August 2026" | |
| 2 | Addressee (exchange) | 26 | "BSE Limited" | |
| 3 | Addressee address | 27–30 | "Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai - 400 001, Maharashtra, India" (extract renders city as "Mumbeai") | OCR_GARBLED |
| 4 | Scrip Code | 33 | "526717" | |
| 5 | ISIN | 34 | "INE136C01044" | |
| 6 | Subject line | 36–38 | "Disclosure under Regulation 30 read Schedule III of the Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015" | |

## Table 2 — Salutation
| # | Field | Line | Content | Flags |
|---|---|---|---|---|
| 7 | Salutation | 40 | "Dear Sir/ Madam," | |

## Table 3 — Disclosure Body Paragraphs
| # | Item | Line(s) | First ~15 words | Flags |
|---|---|---|---|---|
| 8 | Para 1 — event disclosure | 43–46 | "Pursuant to Regulation 30 of the SEBI Listing Regulations, we wish to inform you that the Board..." — Board meeting held today (12 Aug 2026) approved adoption of a new set of Articles of Association, subject to Members' approval at the ensuing AGM | AGM_APPROVAL_PENDING |
| 9 | Para 2 — rationale | 48–50 | "The proposed adoption of the new Articles of Association is to align the Articles..." — alignment with Companies Act 2013, rules thereunder, and other applicable regulatory requirements | |

## Table 4 — Agenda Item (Board Outcome equivalent, rule 3)
| # | Agenda item | Line | Detail | Flags |
|---|---|---|---|---|
| 10 | Adoption of new Articles of Association | 45 | Sole agenda item in this disclosure; board approval given, conditional on AGM/shareholder approval | AGM_APPROVAL_PENDING; MEETING_TIMES_NOT_FOUND |

Note: this letter discloses only one matter. It is not a comprehensive Board
Outcome letter, so no other standard agenda items (AR approval, dividend,
director appointments, auditor changes, scrutinizer, ESOP grants,
capital-raising resolutions) are present or applicable to cross-check here —
confirmed absent by manual sweep of all 68 lines, not merely unlisted. Per
rule 3, board meeting start/end times should be recorded; neither is disclosed
anywhere in this letter — flagged MEETING_TIMES_NOT_FOUND (NOT FOUND per
CLAUDE.md; not estimated).

## Table 5 — Closing Block
| # | Field | Line | Content | Flags |
|---|---|---|---|---|
| 11 | Closing — thanks | 52 | "Thank you." | |
| 12 | Closing — valediction | 53 | "Yours faithfully" | |
| 13 | Closing — company signoff | 55 | "For HCP PLASTENE BULKPACK LIMITED" | |

## Table 6 — Digital Signature Block (rule 7)
| # | Field | Line | Content | Flags |
|---|---|---|---|---|
| 14 | Digital signature marker | 56 | " .         Digitally signed by" | |
| 15 | Signatory name (OCR fragment 1) | 57 | "Rishabh    oo kumarsain" | OCR_GARBLED |
| 16 | Signature timestamp | 58 | "1 Date: 2026.08.12" (date resolves to 12 Aug 2026 — same calendar date as the board meeting; time-of-day not legibly extracted) | OCR_GARBLED; TIMESTAMP_INCOMPLETE |
| 17 | Signatory name (OCR fragment 2) | 59 | "Kumar Jain 7565 050" | OCR_GARBLED |
| 18 | Signatory name (clean) | 60 | "Rishabh Kumar Jain" | |
| 19 | Designation | 61 | "Company Secretary and Compliance Officer" | |
| 20 | Membership Number | 62 | "Membership Number: F7271" | |

Note: signature date (2026.08.12) matches the board meeting date, but no
time-of-day survives OCR extraction and no board meeting start/end time is
disclosed in the letter (see Table 4), so it cannot be determined whether
signing followed meeting conclusion — flagged MEETING_TIMES_NOT_FOUND rather
than assumed compliant.

## Table 7 — Footer / Corporate Details
| # | Field | Line | Content | Flags |
|---|---|---|---|---|
| 21 | CIN + website | 66 | "CIN: L25200GJ1984PLC050560" / "www.hpbl.in" | |
| 22 | Company name (repeat) + email | 67 | "Hep plastene Bulkpack Ltd" [OCR; official name per letterhead line 16-17 is "HCP Plastene Bulkpack Limited"] / "info@hpbl.in" | OCR_GARBLED |
| 23 | Registered address + phone | 68 | "H.B. Jirawla House, 13, Navbharat Society, Usmanpura, Ahmedabad - Gujarat 380013" / phone rendered as "017927561000" (OCR-garbled; likely 079-27561000 given Ahmedabad STD code 079) | OCR_GARBLED |

---

## SUMMARY
Total enumerated discrete disclosure units: 23
- Filing metadata fields: 6
- Salutation: 1
- Disclosure body paragraphs: 2
- Agenda items: 1
- Closing block: 3
- Digital signature block lines: 7
- Footer/corporate detail lines: 3

Confirmed-absent (N/A) standard categories: numbered notes (0), financial
table line items (0, including no ZERO_STANDING candidates — there are no
standing line items of any kind in this document), auditor report paragraphs
(0), consolidation entity list (0), annexures/director profiles (0).

Flags raised across ledger: OCR_GARBLED (lines 27–30, 57–59, 67, 68),
AGM_APPROVAL_PENDING (lines 43–46, 45), MEETING_TIMES_NOT_FOUND (rule 3 board
meeting start/end times; also bears on signature-timestamp-vs-meeting-end
verification at lines 56–59).
