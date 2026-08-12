# A3 FORENSIC NOTES — INDIQUBE — Q1FY27 — doctype: results (AGM proceedings / governance minutes)

Company: IndiQube Spaces Limited (INDIQUBE)
Source A1 extract: extract_results-agm_indiqube_q1fy27.txt (186 lines, 4 pages, no OCR)
A2 ledger: ledger_results-agm_indiqube_q1fy27.md (Tables 1-7, gate_a2 pass)
Prior-quarter extract: NONE (first pipeline run for INDIQUBE — no verbatim diff possible for F5/F15)
Ledger reconciliation: 100% — every ledger row (14 proceeding items, 3 resolutions, 7 named persons, 6 timing facts, 7 letter items, 1 signature block, 6 N.A. category rows) read verbatim at its cited line before judging.

Doctype framing: this is a Regulation 30 intimation of the 12th AGM — governance minutes, no financial statement, no numbered notes, no line-item table, no consolidation entity list, no auditor paragraph breakdown. Per the checklist doctype rules, the balance-sheet / statement checks (F1-F5, F8-F12, F15) are structurally N.A.; the presentation check (F16) and concall check (F17) are N.A. by doctype. The applicable lens is F6 (forward-commitment phrasing), F7 (hedges), F13 (board outcome / corporate actions) and F14 (drafting inconsistencies). Monitoring-checklist item 4 (board stability / auditor) is the relevant thesis lens for this artifact.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| FND-01 | F6 | Table 4 row 6; Table 1 item 10 | 131-132 | "the voting results would be declared within two working days from the conclusion of the AGM" | FORWARD-SIGNAL | Voting-results filing lands ~Aug 14, 2026. Passage of all three resolutions (incl. Anshuman Das re-appointment and the Secretarial Auditor term) is NOT confirmable from this document; schedule the results filing for A4/Role-5 as the confirming event. |
| FND-02 | F6 | Table 2 Resolution 3 | 152-154 | "as Secretarial Auditor for a period of 5 consecutive years" | NEUTRAL-FACT | Five-year forward term commitment (~FY27-FY31). DISTINCTION: this is the SECRETARIAL auditor, NOT the statutory auditor. The statutory-auditor identity/rotation (thesis carries an unverified Big-4-exit gap) is NOT addressed anywhere in this filing. |
| FND-03 | F13 | Table 1 item 11 | 135-137 | "the Annual Report ... had already been circulated to the Members through electronic means" | FORWARD-SIGNAL | Full FY26 Annual Report already exists and is circulated → trigger a Role 6 AR Deep Dive. The RPT detail (Innoprop / Grub Group promoter entities), prior-auditor identity, and IGAAP-adjusted PAT are resolvable there, not here. |
| FND-04 | F13 | Table 2 Resolution 2; Table 3 person 6 | 149-151 | "To appoint a director in place of Mr. Anshuman Das (DIN: 00420772), who retires by rotation and being eligible, offers himself for re-appointment" | NEUTRAL-FACT | Routine promoter-group director re-appointment via rotation cycle — board continuity of the promoter side, NOT an independent-director non-renewal. Only director with a disclosed DIN in this doc. Governance-neutral per F13 (a re-appointment through the window, not a removal). |
| FND-05 | F13 | Table 1 items 4 & 5; Table 3 persons 3 & 4 | 94-96 / 99-101 | "Mr. A.G. Muralikrishnan, Chairman of the Audit Committee, was unable to attend the Meeting due to prior commitments" | AMBIGUOUS | The Audit Committee Chairman (an Independent Director) was absent, and audit / financial-statement / internal-control queries were fielded instead by Mr. Rishi Das — the Executive/promoter Chairman-CEO who is merely "a member" of the committee. Second director (Sandeep Singhal, NED) also absent (line 95). Board-stability lens (checklist item 4): independent oversight not personally present to answer audit questions at the AGM. → A4 management question. |
| FND-06 | F14 | Table 3 person 5 | 119 vs 166 | "Ms. Meghana Agarwal" (l.119) vs "Ms. Meghna Agarwal" (l.166) | NEUTRAL-FACT | Same Executive Director & COO spelled two ways within one official filing. Individually immaterial; a drafting-quality / document-control data point consistent with the thesis-carried CS-turnover concern (3 CS in 15 months). |
| FND-07 | F13 | Table 3 person 7; Table 1 items 10 & 12 | 129-134 / 152-154 | "Ms. Varsha V Shenoy ... appointed as the Scrutinizer" and "To appoint Ms. Varsha V Shenoy ... as Secretarial Auditor for a period of 5 consecutive years" | AMBIGUOUS | The same individual scrutinizes the very e-voting that includes the resolution for her own 5-year Secretarial Auditor appointment. Both roles are independently disclosed (not a factual error) but the overlap is a governance-quality question → A4. |
| FND-08 | F13 | Table 1 item 11; Table 7 auditor-para row | 136-137 | "the Auditors' Report on the financial statements with unmodified opinion" | NEUTRAL-FACT | Clean unmodified statutory audit opinion on FY26 — checklist item 4 auditor-opinion sub-test reads green. Caveat: inline mention only; no opinion paragraph, no UDIN, no entity-audit-status list in this extract. Confirms the opinion type, not its contents. |

---

## CHECKLIST SCORECARD (all 17, no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | N.A. | No financial table; ledger row 29 records zero_standing = 0 (governance minutes, no line items). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No standalone/consolidated financials in an AGM-proceedings summary. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines and no consolidation entity list to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" and no PAT figure; only an inline "unmodified opinion" mention (l.136-137, see FND-08). No ratio computable. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No going-concern / EoM paragraph present; and no prior-quarter extract for a verbatim diff (first run). |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | Dateable commitments present: voting results "would be declared within two working days" (l.131) and 5-year Secretarial Auditor term (l.153). See FND-01, FND-02 and Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Hedge lexicon ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may", "could have an effect") swept case-insensitive across all 186 lines; zero hits. Procedural minutes carry no pre-emptive legal hedges. |
| F8 TAX FORENSICS | N.A. | No tax line, no ETR, no deferred-tax data in this doctype. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data present. |
| F10 SHARE COUNT AND DILUTION | N.A. | No paid-up capital or EPS figures; no corporate action changing share count in this doc. |
| F11 RESERVES AND NET WORTH TIE-OUT | N.A. | No Other Equity / paid-up figures to reconcile. |
| F12 SEGMENT FORENSICS | N.A. | No segment table present. |
| F13 BOARD OUTCOME BEYOND THE RESULTS | FINDING | AR already circulated → AR Deep Dive event (FND-03); Anshuman Das rotation re-appointment (FND-04); Audit Committee Chair absence with executive fielding audit queries (FND-05); Scrutinizer/candidate overlap (FND-07); clean opinion + FY26 adoption (FND-08). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Meghana/Meghna Agarwal name spelled two ways in one filing (l.119 vs l.166) — FND-06. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list, and no prior-quarter list to diff. |
| F16 PRESENTATION-SPECIFIC | N.A. | Not an investor presentation. |
| F17 CONCALL-SPECIFIC SILENCE AUDIT | N.A. | Not a concall transcript. (Note: statutory-auditor identity and RPT metrics are silent here but carry no line number; deferred to the AR Deep Dive per FND-03 rather than forced as a finding.) |

Applicability accounting: 11 checks N.A. (F1-F5, F8-F12, F15-F17), 1 PASS (F7), 3 FINDING (F6, F13, F14). No blanks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / item ref | status word |
|------------|--------------|-----------------|-------------|
| Voting results to be declared and intimated to exchanges | Within 2 working days of AGM close → ~Aug 14, 2026 | Item 10, line 131-132 | initiated / pending |
| Secretarial Auditor (Ms. Varsha V Shenoy) appointment for 5 consecutive years | ~FY27-FY31 term | Resolution 3, line 152-154 | proposed (subject to e-vote outcome) |
| Re-appointment of Mr. Anshuman Das, director retiring by rotation | Current rotation cycle | Resolution 2, line 149-151 | proposed (subject to e-vote outcome) |
| Adoption of FY26 audited financial statements + Board/Auditors' Reports | FY ended Mar 31, 2026 | Resolution 1, line 145-148 | proposed (subject to e-vote outcome) |
| Annual Report (incl. Notice, Secretarial + Statutory Auditor Reports) circulated, taken as read | Done pre-AGM | Item 11, line 135-139 | completed |

---

## FORWARD-SIGNAL / AMBIGUOUS FLAGS FOR A4

- FORWARD-SIGNAL: FND-01 (voting-results filing incoming ~Aug 14, 2026 — resolution passage not yet confirmable), FND-03 (FY26 Annual Report already circulated → schedule Role 6 AR Deep Dive; RPT / prior-auditor / IGAAP-PAT resolvable there).
- AMBIGUOUS (→ A4 management questions): FND-05 (Audit Committee Chairman absent from AGM; executive/promoter CEO fielded audit queries; second director also absent — board-stability lens), FND-07 (Scrutinizer of the e-voting is simultaneously the candidate being appointed Secretarial Auditor for 5 years — conflict/governance-quality question).

Thesis-lens note (checklist item 4, board stability / auditor): auditor-opinion sub-test is green (unmodified, FND-08) and the change is to the SECRETARIAL auditor only, not the statutory auditor (FND-02) — no statutory-auditor resignation/qualification is signalled here. The board-stability sub-test is the softer read: two directors absent, including the Independent Audit Committee Chairman, whose audit questions were answered by the promoter Executive Chairman-CEO. Not a red trip on its own, but it feeds the standing governance file (promoter concentration 60.10%, CS turnover) as an AMBIGUOUS watch item.
