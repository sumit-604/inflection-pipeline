# A2 COMPLETENESS LEDGER — NEPHROPLUS Q1FY27
Source: extract_agm_nephroplus_q1fy27.txt (filename says "concall_nephroplus_q1fy27.pdf";
A1 header content_mismatch_note confirms actual content is a Regulation 30 filing —
"Summary of proceedings of the 17th AGM of Nephrocare Health Services Limited", held
12-Aug-2026 via VC/OAVM, ref NEPHROPLUS/SE/74. Treated per task instruction as a
Board/AGM-Outcome document. All line numbers below cite the embedded original-document
line numbers (first numeric column in the extract file), not this ledger's own row order.

=== A2 COUNT TEST ===
category: agenda_items (AGM resolutions)         grep_count: 6   sweep_count: 6   match: yes
category: directors_present                      grep_count: 8   sweep_count: 8   match: yes
category: attendees (in attendance)               grep_count: 7   sweep_count: 7   match: yes
category: quorum_records                         grep_count: 1   sweep_count: 1   match: yes
category: meeting_timing (start x2 mentions + end)grep_count: 3   sweep_count: 3   match: yes
category: md_interested_recusal                  grep_count: 2   sweep_count: 2   match: yes
category: auditor_report_remarks                 grep_count: 2   sweep_count: 2   match: yes
category: digital_signature_blocks               grep_count: 2   sweep_count: 2   match: yes
category: other_narrative_procedural_items       grep_count: 20  sweep_count: 20  match: yes
category: numbered_notes (results-style)         grep_count: 0   sweep_count: 0   match: yes  (not present in AGM-proceedings document)
category: financial_table_line_items             grep_count: 0   sweep_count: 0   match: yes  (not present in AGM-proceedings document)
category: zero_standing_line_items               grep_count: 0   sweep_count: 0   match: yes  (not present; no financial table exists to carry zero-standing rows)
category: consolidation_entity_list              grep_count: 0   sweep_count: 0   match: yes  (not present in AGM-proceedings document)
category: director_profile_annexure_table        grep_count: 0   sweep_count: 0   match: yes  (not present as a standalone annexure; DIN disclosed only incidentally for 2 of 8 directors, inside Res 2 and Res 5 text)
category: concall_speaker_turns                  grep_count: 0   sweep_count: 0   match: yes  (not present; document is not a concall transcript despite filename)
category: concall_questions                      grep_count: 0   sweep_count: 0   match: yes  (not present)
category: concall_mgmt_numbers_spoken            grep_count: 0   sweep_count: 0   match: yes  (not present; zero financial figures in document per A1 header)
category: investor_presentation_slides           grep_count: 0   sweep_count: 0   match: yes  (not present; document is not an investor presentation)
gate_a2: pass
=== END COUNT TEST ===

---

## A. AGM RESOLUTIONS (Agenda Items) — 6 rows
Table at lines 131-152 ("S. No. / Particulars of Resolution / Type of Resolution").
Chairman's introduction to the resolutions block at line 123.

| # | Line(s) | Resolution | Type | Flags |
|---|---------|-----------|------|-------|
| Res 1 | 132-134 | Adoption of the Audited Standalone and Consolidated Financial Statements for FY ended March 31, 2026, together with the Auditors' Report and Board's Report thereon | Ordinary | — |
| Res 2 | 135-137 | Re-appointment of Mr. Gaurav Sharma (DIN: 03311656), Nominee Director (Non-Executive category), liable to retire by rotation | Ordinary | — |
| Res 3 | 140 | Approval for the NephroPlus Employee Stock Option Scheme, 2026 | Special | DILUTION, RELATED_PARTY |
| Res 4 | 141-144 | Approve grant of Employee Stock Options to employees of subsidiary, associate company (incorporated in India or outside India), or holding company, under NephroPlus ESOP Scheme 2026 | Special | DILUTION, RELATED_PARTY |
| Res 5 | 145-148 | Approval for clarificatory amendment to the special resolution on remuneration of Mr. Vikram Vuppala (DIN: 02847323), Chairman & Managing Director | Special | RELATED_PARTY, PROMOTER_ECONOMICS |
| Res 6 | 149-152 | Approval for the Promote Incentive Arrangement pursuant to the Promote Agreement dated July 25, 2025, entered by Mr. Vikram Vuppala (Founder, Promoter, Chairman & Managing Director) with certain Shareholders of the Company | Ordinary | RELATED_PARTY, PROMOTER_ECONOMICS |

Note: Res 6 is filed as an "Ordinary" resolution despite being a promoter-economics item (Promote Incentive Arrangement between the Founder/MD and certain shareholders) — resolution-type classification carried verbatim from source; A3/A4 should evaluate whether Ordinary (vs Special) classification is itself a disclosure question, since Res 3-5 (ESOP, remuneration) were filed as Special but Res 6 (promoter incentive economics) was not.

## B. DIRECTORS PRESENT — 8 rows
Table at lines 59-72 ("The following Directors were present").

| Sr. | Line(s) | Name | Role | Attended from | Flags |
|-----|---------|------|------|----------------|-------|
| 1 | 61-62 | Mr. Vikram Vuppala | Chairman and Managing Director; Chairman of Risk Management Committee | Hyderabad | RELATED_PARTY (interested party on Res 5-6) |
| 2 | 63-64 | Mr. Hemant Sultania | Independent Director; Chairman of Audit Committee | Gurugram | — |
| 3 | 65-66 | Mr. Om Prakash Manchanda | Independent Director; Chairman of Nomination and Remuneration Committee | Gurugram | Chaired proceedings for Items 5-6 in place of Vuppala (see section F) |
| 4 | 67-68 | Mr. Gaurav Sharma | Nominee Director; Chairman of Stakeholders Relationship Committee | Mumbai | Subject of Res 2 (own re-appointment) |
| 5 | 69 | Mr. Vishal Vijay Gupta | Nominee Director | Bangalore | — |
| 6 | 70 | Mr. Sunil Kumar Thakur | Nominee Director | Delhi | — |
| 7 | 71 | Ms. Annette Kumlien | Independent Director | France | — |
| 8 | 72 | Dr. Ajay Bakshi | Independent Director | New Delhi | — |

ZERO_STANDING check: no director listed as "absent" / apologies-tendered row is present in the document — all 8 named directors are recorded present; there is no standing "directors absent" line to enumerate as nil.

## C. IN ATTENDANCE — 7 rows
Table at lines 76-87 ("In attendance").

| Sr. | Line(s) | Name | Role | Attended from | Flags |
|-----|---------|------|------|----------------|-------|
| 1 | 78 | Mr. Kamal D Shah | Co-founder | Hyderabad | — |
| 2 | 79 | Mr. Rohit Singh | Group CEO | Hyderabad | — |
| 3 | 80 | Mr. Prashant Goenka | Group CFO | Hyderabad | — |
| 4 | 81 | Mr. Kishore Kathri | Company Secretary & Head Legal | Hyderabad | Also signatory on both digital signature blocks (section H) and authorized recipient of Scrutinizer's report (section I item 16) |
| 5 | 82-83 | Mr. Amit Kumar Bajaj | Partner, B S R and Co., Chartered Accountants — Statutory Auditors | Hyderabad | — |
| 6 | 84-85 | Mr. Vaibhav Dandawate | Partner, Makarand M. Joshi & Co. — Secretarial Auditor | Mumbai | — |
| 7 | 86-87 | Ms. Rashida Hatim Adenwala | Founder Partner, R & A Associates, Company Secretaries — Scrutinizer | Hyderabad | M. No. 4020 disclosed later at line 161 |

## D. QUORUM — 1 row

| Line | Item | Value | Flags |
|------|------|-------|-------|
| 92 | Members attended the Meeting | 74 | — |

## E. MEETING TIMING — 3 rows

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 22 | Meeting start time (cover letter) | Wednesday, August 12, 2026, 2:30 PM IST | — |
| 2 | 49 | Meeting start time (proceedings body, restated) | Wednesday, August 12, 2026, 2.30 pm IST | — |
| 3 | 173-174 | Meeting conclusion time | 3:32 PM IST | Duration ≈ 62 minutes for a 6-resolution AGM including speaker-shareholder Q&A; not flagged as unusually short/long but recorded per instruction to capture start/end as information |

## F. MD-INTERESTED RECUSAL (Items 5-6) — 2 rows

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 123-126 | "In respect of Item Nos. 5 and 6, in which Mr. Vikram Vuppala...was interested, Mr. Om Prakash Manchanda, Independent Director, chaired the proceedings and conducted the business relating to the said items." | RELATED_PARTY, PROMOTER_ECONOMICS |
| 2 | 126-127 | "Upon conclusion of Item Nos. 5 and 6, Mr. Vikram Vuppala resumed the Chair and proceeded with the remaining business of the Meeting." | RELATED_PARTY |

## G. AUDITOR REPORT REMARKS — 2 rows

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 119-120 | "The Notice convening the 17th AGM and the Statutory Auditor's Report were taken as read" (procedural — full text not read aloud) | — |
| 2 | 120-121 | "The Chairman informed the Members that the Statutory Auditor's Report did not contain any qualifications, reservations, adverse remarks or disclaimers" (clean opinion, characterized by Chairman, not the auditor directly in this document) | — |

Note: this is a Chairman's paraphrase of the audit opinion inside AGM proceedings, not the auditor's report itself (the report is not attached to this extract). No Emphasis of Matter / Other Matters / Going Concern paragraphs, entity list, or UDIN numbers are present in this document — those live in the Auditors' Report referenced by Res 1, which is a separate document not supplied in this extract. Flag: SOURCE_DOCUMENT_NOT_SUPPLIED for the underlying Auditors' Report / Board's Report referenced in Res 1.

## H. DIGITAL SIGNATURE BLOCKS — 2 rows

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 33-41 (page 1, cover letter) | Kishore Kathri | Company Secretary & Head Legal, ICSI M. No. F9895 | 2026.08.12 18:13:45 +05'30' | Timestamp is ~2h41m after meeting conclusion (3:32 PM / 15:32 IST) — signed after meeting concluded, as expected; no red flag |
| 2 | 178-186 (page 4, proceedings summary) | Kishore Kathri | Company Secretary & Head Legal, ICSI M. No. F9895 | 2026.08.12 18:14:08 +05'30' | 23 seconds after signature 1; both timestamps postdate meeting conclusion — no red flag |

## I. OTHER NARRATIVE / PROCEDURAL DISCLOSURE ITEMS — 20 rows

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 19-20 | Regulatory basis for this filing: Regulation 30 read with Part A of Schedule III, SEBI LODR Regulations, 2015 | — |
| 2 | 23-24 | AGM Notice date referenced: Notice of the AGM dated June 22, 2026 | — |
| 3 | 43 | "Encl: as above" — enclosure line on cover letter | — |
| 4 | 50-53 | Compliance basis for holding AGM via VC/OAVM: MCA General Circulars + SEBI Circulars + Companies Act, 2013 and Rules thereunder | — |
| 5 | 53-55 | Deemed venue of AGM: Registered Office, 5th Floor, D Block, iLabs Centre, Plot 18, Software Units Layout, Survey No. 64, Madhapur, Shaikpet, Hyderabad – 500081, Telangana | — |
| 6 | 100-101 | CS Kishore Kathri welcomed members and briefed them on the process to participate in the meeting | — |
| 7 | 101-103 | Statutory registers and other required documents made available for inspection on the Company website | — |
| 8 | 103-105 | Proxy appointment facility not applicable (VC/OAVM format); proxy register not available for inspection | — |
| 9 | 105-106 | Members briefed on process for questions & answers and e-voting | — |
| 10 | 108-111 | Chairman welcomed members; Directors who joined via VC introduced themselves and confirmed presence | — |
| 11 | 111-114 | Chairman acknowledged attendance of B S R and Co. (Statutory Auditors), Makarand M. Joshi & Co. (Secretarial Auditor), and Ms. Rashida Hatim Adenwala (Scrutinizer) | — |
| 12 | 114-115 | Requisite quorum confirmed present per statutory requirements; Chairman called meeting to order | — |
| 13 | 117 | "Thereafter, the Chairman delivered his speech" — no content of the speech is captured anywhere in this document | CONTENT_NOT_DISCLOSED (speech substance is NOT FOUND in this extract) |
| 14 | 154-156 | Chairman requested Members who had not cast remote e-votes to vote via e-voting facility during the AGM | — |
| 15 | 156-158 | Chairman invited registered speaker shareholders to express views/raise queries; queries were "duly responded to and appropriately addressed by the Management" (no query content, no Q&A transcript, no speaker names captured) | CONTENT_NOT_DISCLOSED (no record of what was asked or answered) |
| 16 | 160-162 | Ms. Rashida Hatim Adenwala (M. No. 4020) formally confirmed as Scrutinizer for e-voting and remote e-voting, to submit a consolidated report | — |
| 17 | 163-166 | Chairman authorized Mr. Kishore Kathri (CS and Compliance Officer) to receive the Scrutinizer's Consolidated Report, declare the result, and submit to Stock Exchanges within prescribed timelines | — |
| 18 | 166-167 | Resolutions "shall be deemed to be passed on the date of this Meeting" subject to receipt of requisite votes — i.e., voting outcome for all 6 resolutions (including Res 5-6, the promoter-economics items) is NOT YET DISCLOSED in this document | RESULT_PENDING — vote tallies / pass-fail status for all 6 resolutions, including Res 5 (MD remuneration) and Res 6 (Promote Incentive Arrangement), are not in this filing |
| 19 | 169-170 | Chairman thanked Members, Directors and Auditors for participation | — |
| 20 | 172-173 | E-voting facility remained open for 15 minutes after conclusion of proceedings for Members who had not yet voted | — |

---

## J. CATEGORIES NOT PRESENT (count 0, flagged rather than dropped)

| Category | Count | Note |
|----------|-------|------|
| Numbered notes (results-filing style) | 0 | not present in AGM-proceedings document |
| Financial table line items | 0 | not present in AGM-proceedings document; A1 header confirms zero financial figures, unit_convention N/A |
| Zero-standing line items | 0 | not present; no financial table exists to carry a ZERO_STANDING row |
| Consolidation entity list | 0 | not present in AGM-proceedings document |
| Director profile annexure table (full bios/DIN for all 8) | 0 | not present as standalone annexure; DIN disclosed only incidentally for 2 of 8 directors (Gaurav Sharma DIN 03311656 in Res 2; Vikram Vuppala DIN 02847323 in Res 5) |
| Concall speaker turns | 0 | not present; document is not a concall transcript despite the source filename "concall_nephroplus_q1fy27.pdf" |
| Concall questions (analyst Q&A) | 0 | not present |
| Concall management numbers spoken | 0 | not present |
| Investor presentation slides | 0 | not present |

---

## SUMMARY FLAG ROLL-UP

- RELATED_PARTY / PROMOTER_ECONOMICS / DILUTION: Res 3, Res 4, Res 5, Res 6, both MD-recusal rows (section F), Director row 1 (Vikram Vuppala, section B).
- RESULT_PENDING: item I-18 — none of the 6 resolutions (including the two promoter-economics items, Res 5 and Res 6) have disclosed vote outcomes in this document; only the Scrutinizer's future consolidated report will carry pass/fail.
- CONTENT_NOT_DISCLOSED: item I-13 (Chairman's speech content) and item I-15 (speaker-shareholder queries and management responses) — both referenced but substance not captured anywhere in this document.
- SOURCE_DOCUMENT_NOT_SUPPLIED: the Auditors' Report and Board's Report referenced in Res 1 are not attached to this extract; only the Chairman's paraphrase of the audit opinion (section G) is available.
- DOCTYPE_MISMATCH (carried from A1): source filename says "concall_nephroplus_q1fy27.pdf" but content is a Regulation 30 AGM-proceedings filing dated one day after the actual Q1 FY27 results filing (11-Aug-2026) and describing FY26 annual-accounts adoption, not Q1 FY27 quarterly matters. This entire ledger is therefore a ledger of the AGM proceedings document, not of a Q1 FY27 concall — A3/A4 must be told the expected concall transcript for Q1 FY27 has not yet been supplied/enumerated.
