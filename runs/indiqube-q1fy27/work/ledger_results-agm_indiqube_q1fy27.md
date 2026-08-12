# A2 ENUMERATION LEDGER — INDIQUBE Q1FY27 — results (AGM proceedings)

Company: Indiqube Spaces Limited (INDIQUBE)
Doctype: results (AGM proceedings / governance minutes — Regulation 30 intimation of the 12th AGM)
Source file (A1 extract): extract_results-agm_indiqube_q1fy27.txt (186 lines, 4 pages, no OCR)
Prior-quarter ledger: NONE (first pipeline run for INDIQUBE)

Governance-document note: this AGM-proceedings filing carries no financial
statement, no numbered notes, no line-item table, and no consolidation
entity list. Per the A2 doctype instructions ("RESULTS FILING"), the
following categories are therefore **N.A.** for this specific artifact and
are recorded as zero-count / not-applicable rather than omitted:
`notes`, `line_items`, `zero_standing`, `auditor_paras` (detailed
paragraph-level breakdown — the single opinion-type mention is captured
inline in proceeding item 11), `entities` (consolidation list). Concall and
investor-presentation categories (`turns`, `questions`, `mgmt_numbers`,
`slides`, `slide_numbers`) are N.A. — this is not that doctype. The
enumeration below instead applies the Board-Outcome/agenda discipline the
task specifies: every resolution, every named director/KMP with
attendance, every timing fact, every letter/procedural item, and the
signature block, each carrying a line number.

---

## === A2 COUNT TEST ===
```
category: notes                    grep_count: 0   sweep_count: 0   match: yes (N.A. — no notes section in this doctype)
category: line_items               grep_count: 0   sweep_count: 0   match: yes (N.A. — no financial table in this doctype)
category: zero_standing            grep_count: 0   sweep_count: 0   match: yes (N.A. — no financial table, no standing line items)
category: auditor_paras            grep_count: 0   sweep_count: 0   match: yes (N.A. — opinion type mentioned inline only, no paragraph breakdown; captured in proceeding_items row 11)
category: entities                 grep_count: 0   sweep_count: 0   match: yes (N.A. — no consolidation list in this doctype)
category: turns                    grep_count: 0   sweep_count: 0   match: yes (N.A. — not a concall transcript)
category: questions                grep_count: 0   sweep_count: 0   match: yes (N.A. — not a concall transcript)
category: mgmt_numbers             grep_count: 0   sweep_count: 0   match: yes (N.A. — not a concall transcript)
category: slides                   grep_count: 0   sweep_count: 0   match: yes (N.A. — not an investor presentation)
category: slide_numbers            grep_count: 0   sweep_count: 0   match: yes (N.A. — not an investor presentation)
category: agenda_items (proceeding items, Section B, items 1-14)   grep_count: 14   sweep_count: 14   match: yes
category: resolutions (Sr.No table nested in proceeding item 12)   grep_count: 3    sweep_count: 3    match: yes
category: named_person_mentions (line occurrences of Mr./Ms./Mrs. + name)   grep_count: 13   sweep_count: 13   match: yes
category: timing_fact_mentions (A.M./P.M./working day/15-minute tokens)     grep_count: 10   sweep_count: 10   match: yes
category: letter_items (cover-letter recipients/codes/citation/subject/link)  grep_count: 7   sweep_count: 7   match: yes
category: signature_blocks         grep_count: 1   sweep_count: 1   match: yes
gate_a2: pass
```
=== END COUNT TEST ===

Reconciliation method: for every non-N.A. category a first-pass `grep -n`
(or `grep -o` where a single line carries more than one discrete item,
e.g. the letter's two-column recipient/scrip-code lines) was run against
the extract, then a second independent manual line-by-line read of the
same section was performed and tallied by hand. All six applicable
categories matched on the first pass; no re-sweep was required.

---

## TABLE 1 — Proceeding items (Annexure-A, Section B, items 1-14)

| # | Line | Item (first ~15 words) | Flags |
|---|------|--------------------------|-------|
| 1 | 85 | Mr. Bhasker Dubey, Company Secretary & Compliance Officer, welcomed the Members to the 12th AGM | |
| 2 | 88 | The Meeting was chaired by Mr. Rishi Das, Chairman, Executive Director and Chief Executive Officer | |
| 3 | 90 | The requisite quorum being present, the Chairperson called the AGM in order and commenced proceedings | |
| 4 | 92-98 | CS introduced directors, KMPs and invitees present virtually; informed Mr. A.G. Muralikrishnan (Independent Director) and Mr. Sandeep Singhal (Non-Executive Director) could not attend due to prior commitments; Statutory and Secretarial Auditors' reps joined via VC | DIRECTOR_ABSENT |
| 5 | 99-103 | CS informed that Mr. A.G. Muralikrishnan, Audit Committee Chairman, unable to attend; Mr. Rishi Das (Audit Committee member) to respond to audit/financial-statement/internal-control queries | DIRECTOR_ABSENT |
| 6 | 114-117 | Members informed statutory registers/documents referred to in AGM Notice available for inspection on company website or via email request | |
| 7 | 118-120 | Mr. Rishi Das (Chairman/ED/CEO), followed by Ms. Meghana Agarwal (Executive Director & COO), addressed the shareholders | NAME_INCONSISTENCY (see Table 3 note) |
| 8 | 121-124 | Remote e-voting commenced 09:00 A.M. IST Sat Aug 8 2026, concluded 5:00 P.M. IST Tue Aug 11 2026; e-voting facility also available at the Meeting for those not yet voted | |
| 9 | 125-128 | CS informed members present at AGM who had not e-voted remotely would get opportunity to vote during AGM and up to 15 minutes after conclusion via MUFG Intime platform | |
| 10 | 129-134 | Ms. Varsha V Shenoy, Company Secretary in Practice, appointed Scrutinizer for remote e-voting and AGM e-voting; results to be declared within 2 working days of AGM conclusion, intimated to exchanges and published on company/MUFG Intime websites | |
| 11 | 135-139 | CS informed Annual Report (incl. Notice, Secretarial Auditors' Report, Auditors' Report on financial statements with unmodified opinion) already circulated electronically and, with Members' consent, taken as read | |
| 12 | 140-155 | CS briefed members on 3 resolutions proposed in the AGM Notice (see Table 2) | |
| 13 | 164-167 | Registered speaker-Members given opportunity to express views/ask questions; Mr. Rishi Das and Ms. Meghna Agarwal responded to queries | NAME_INCONSISTENCY |
| 14 | 169-176 | CS thanked Members and Directors for participation; vote of thanks given; e-voting facility remained open an additional 15 minutes post-AGM; AGM concluded 10:53 A.M. IST | |

Section headers framing this table (not separately enumerated as items):
line 73 "A. Date, time and venue of the Annual General Meeting"; line 83
"B. Summary of proceedings".

---

## TABLE 2 — Resolutions (Sr. No. table nested inside proceeding item 12)

| Sr. No. | Line | Resolution | Type | Flags |
|---|------|------------|------|-------|
| 1 | 145-148 | To receive, consider and adopt audited financial statements of the Company for FY ended March 31, 2026, together with Board and Auditors' Reports thereon | Ordinary Resolution | |
| 2 | 149-151 | To appoint a director in place of Mr. Anshuman Das (DIN: 00420772), who retires by rotation and, being eligible, offers himself for re-appointment | Ordinary Resolution | |
| 3 | 152-154 | To appoint Ms. Varsha V Shenoy, Practising Company Secretary, as Secretarial Auditor for a period of 5 consecutive years | Ordinary Resolution | |

Note: no Special Resolution is proposed in this AGM. Outcome/vote tally for
each resolution is NOT FOUND in this document — proceedings summary states
results "would be declared within two working days" (item 10, line
131-132); the voting-results filing is a separate disclosure not present
in this extract (flag for A3/A4: pending outcome, resolution passage not
yet confirmable from this document).

---

## TABLE 3 — Named directors, KMPs and other individuals (distinct persons, with attendance)

| # | Person | Role | Attendance | Line(s) referenced | Flags |
|---|--------|------|-----------|---------------------|-------|
| 1 | Bhasker Dubey | Company Secretary & Compliance Officer | Present (welcomed members, chaired procedural narration, signed the intimation letter) | 46-53, 85, 92-93, 99, 109(footer, n/a), 114, 125, 129, 135, 140, 169 | |
| 2 | Rishi Das | Chairman, Executive Director & Chief Executive Officer; Audit Committee member | Present (chaired meeting, addressed shareholders, responded to audit/financial queries in place of absent Audit Committee Chairman, responded to member queries) | 88-89, 101, 118, 165 | |
| 3 | Avalur Gopalaratnam Muralikrishnan (A.G. Muralikrishnan) | Independent Director; Chairman of the Audit Committee | ABSENT — "could not attend the AGM due to prior commitments" (line 94-96); separately noted "unable to attend the Meeting due to prior commitments" as Audit Committee Chairman (line 99-101) | 94-95, 100 | DIRECTOR_ABSENT |
| 4 | Sandeep Singhal | Non-Executive Director | ABSENT — "could not attend the AGM due to prior commitments" | 95 | DIRECTOR_ABSENT |
| 5 | Meghana Agarwal / Meghna Agarwal (spelling varies in source) | Executive Director & Chief Operating Officer | Present (addressed shareholders, responded to member queries) | 119, 166 | NAME_INCONSISTENCY (line 119 spells "Meghana", line 166 spells "Meghna" — same person, source document internal inconsistency, not a pipeline transcription error; flag for A3) |
| 6 | Anshuman Das (DIN: 00420772) | Director retiring by rotation, subject of Resolution 2 (re-appointment) | Not stated as present/absent in the narrative proceedings; named only within the resolution table | 149-151 | DIN disclosed for this director only; DIN NOT FOUND in this document for the other five named individuals |
| 7 | Varsha V Shenoy | Company Secretary in Practice; appointed Scrutinizer for e-voting (item 10); also the proposed Secretarial Auditor under Resolution 3 | Present (performing Scrutinizer role); joined per line 97 reference to "representatives of ... Secretarial Auditors" (unnamed generic mention likely includes her firm) | 129-134, 152-154 | Dual role in one meeting (Scrutinizer of the vote AND the candidate being voted on for Secretarial Auditor appointment) — note for A3/A4 governance-quality review, not flagged as a factual error since both roles are independently disclosed |

Generic/unnamed attendee mentions (not individually named, recorded for
completeness): "representatives of the Statutory Auditors and the
Secretarial Auditors joined the Meeting through Video Conferencing from
their respective locations" (line 96-98) — firm names NOT FOUND in this
extract.

Distinct-person count: 7. Underlying line-level mention count (grep/sweep
reconciled category above): 13.

---

## TABLE 4 — Timing facts (meeting start/end, e-voting window, results timeline)

| # | Fact | Value | Line(s) | Flags |
|---|------|-------|---------|-------|
| 1 | AGM commencement time | 10:00 A.M. IST, Wednesday August 12, 2026 | 35, 69, 79 | Consistent across all 3 mentions (cover letter + Annexure-A section A + section A body) |
| 2 | AGM conclusion time | 10:53 A.M. IST (including e-voting time at the AGM) | 36, 79, 175 | Consistent across all 3 mentions. Elapsed meeting duration: 53 minutes. |
| 3 | Remote e-voting window opens | 09:00 A.M. IST, Saturday August 8, 2026 | 121-122 | |
| 4 | Remote e-voting window closes | 5:00 P.M. IST, Tuesday August 11, 2026 | 122-123 | |
| 5 | Post-AGM supplementary e-voting window | Additional 15 minutes after AGM conclusion, via e-voting platform | 127, 173-174 | |
| 6 | Voting results declaration timeline | Within 2 working days of AGM conclusion; intimated to Stock Exchanges, published on company website and MUFG Intime website | 131-134 | Result itself NOT FOUND in this document (pending, separate filing) |

Line-level mention count (grep/sweep reconciled category): 10 (two of the
six facts — AGM start/end — are each mentioned on more than one line).

---

## TABLE 5 — Cover-letter / procedural items (page 1, Regulation 30 intimation)

| # | Item | Value | Line | Flags |
|---|------|-------|------|-------|
| 1 | Recipient 1 | BSE Limited (20th Floor, P.J. Towers, Dalal Street, Mumbai 400001) | 19 | |
| 2 | Recipient 2 | National Stock Exchange of India Limited (Exchange Plaza, C-1, Block G, BKC, Bandra (E), Mumbai 400051) | 19 | |
| 3 | BSE Scrip Code | 544454 | 23 | |
| 4 | NSE Scrip Symbol | INDIQUBE | 23 | |
| 5 | Subject line | "Summary of proceedings of the 12th Annual General Meeting of the Company held on August 12, 2026" | 26-27 | |
| 6 | Regulatory basis cited | Regulation 30, SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 | 31-32 | |
| 7 | Website intimation reference | https://indiqube.com/investor/ | 39-40 | |

---

## TABLE 6 — Signature block

| # | Signatory | Designation | Signature type | Timestamp | Line | Flags |
|---|-----------|-------------|-----------------|-----------|------|-------|
| 1 | Bhasker Dubey | Company Secretary & Compliance Officer | Digital signature (DSC) | 2026.08.12, 16:53:35 +05'30" | 46-53 | Timestamp is same-day, ~6 hours after AGM conclusion (10:53 A.M. IST) — consistent with same-day regulatory filing of the proceedings summary; NOT a "signed before meeting concluded" violation |

---

## TABLE 7 — N.A. categories (stated explicitly per doctype discipline)

| Category | Status | Basis |
|----------|--------|-------|
| Numbered notes (financial statement notes) | N.A. | No notes section; this is a governance-minutes document, not a results/financial-statement extract |
| Financial table line items (incl. ZERO_STANDING) | N.A. | No financial statement or table present in this extract |
| Auditor report paragraphs (opinion type breakdown, EOM, Other Matters, Going Concern, UDIN, entity-audit-status list) | N.A. — partial exception | Only a single inline mention exists: "Auditors' Report on the financial statements with unmodified opinion" (proceeding item 11, line 136-137). No paragraph-level detail, no UDIN, no entity list is reproduced in this AGM-proceedings summary; full auditor report is a separate document not in this extract |
| Consolidation entity list | N.A. | Not applicable to an AGM-proceedings summary; no entity list present |
| Concall transcript categories (participants, turns, questions, mgmt numbers, hedge/commitment phrases) | N.A. | Doctype is not a concall transcript |
| Investor presentation categories (slides, slide numbers, DROPPED_SLIDE) | N.A. | Doctype is not an investor presentation |

---

## INFORMATIONAL (not gated — repeated boilerplate, not a discrete disclosure unit)

Company letterhead / footer block (company name, former names, registered
office address, CIN L45400KA2015PLC133523, email, website, phone) repeats
identically once per page at lines 58-63, 107-112, 157-162, 181-186 (4
occurrences across the 4-page document). Not enumerated as a disclosure
row since it carries no variable disclosure content page to page.

---

## SUMMARY ROLL-UP

| Category | Count |
|----------|-------|
| Proceeding items (Section B, 1-14) | 14 |
| Resolutions (Ordinary: 3, Special: 0) | 3 |
| Named-person mentions (line occurrences) | 13 |
| Distinct named persons (directors/KMPs/other) | 7 |
| Directors absent (flagged) | 2 (A.G. Muralikrishnan, Sandeep Singhal) |
| Timing-fact mentions (line occurrences) | 10 |
| Distinct timing facts | 6 |
| Letter/procedural items (cover letter) | 7 |
| Signature blocks | 1 |
| Notes / line items / zero-standing / entities / auditor paras (detail) / turns / questions / mgmt numbers / slides / slide numbers | 0 (N.A., doctype does not carry these) |

Flags raised across this ledger: DIRECTOR_ABSENT (x2: A.G. Muralikrishnan,
Sandeep Singhal), NAME_INCONSISTENCY (x1: Meghana/Meghna Agarwal spelling
variance in source document).
