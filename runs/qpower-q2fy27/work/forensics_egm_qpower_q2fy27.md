# A3 FORENSIC NOTES: QPOWER Q2 FY27, doctype presentation (EGM outcome 19-Oct-2026; doctag egm)

Agent: A3 forensics | model: claude-opus-5-5 | date: 2026-10-19
Inputs read: A1 structured (runs/qpower-q2fy27/extracted/qpower-egm-q2fy27-structured.md, R001-R068 plus 2 foot notes), A1 fulltext (runs/qpower-q2fy27/extracted/qpower-egm-q2fy27-fulltext.md, 171 lines, all read), A2 ledger (runs/qpower-q2fy27/work/ledger_egm_qpower_q2fy27.md), Notion brief sections 4, 5, 7, 9 (runs/qpower-q2fy27/work/notion-brief.md; memory, not evidence). Prior-quarter fulltext: none passed. Source PDF and inputs/ not opened.
Line numbers below are fulltext line numbers (header lines 1-17; body from line 18).

## 0. LEDGER RECONCILIATION (100%)

| Ledger group | Rows | Read at fulltext line | Result |
|---|---|---|---|
| Numbers | R001-R024 (24) | 25, 27, 35-36, 47, 55, 55, 56, 79, 58-67, 69-78, 106, 110 x3, 113, 113, 115, 117, 122, 123, 136-144, 149, 151, 154-155 | All verbatim values present. R021 anchor per A2 correction (136-144). |
| Entities | R025-R048 (24) | 20, 22, 39, 45-46, 48, 59-66, 70-78, 95-96, 119-120, 107-108, 129, 151-153, 113-118, 142-144, 136-138 | All present. A2 corrections for R025 (L20), R045 (L151-153), R046 (L113-118) confirmed correct. |
| Forward | R049-R053 (5) | 95-96, 106-108, 109-111, 149, 103-105 | All present. |
| Dates | R054-R065 (12) | 19, 29, 43-44, 53, 122, 123, 166, 149, 113-118, 55, 154 | All present except R065. R065 is a task-derived label, not document text (L31 reads `("OAVM").`). A2 note confirmed. R056 time sits on L44, date on L43 (imprecise, immaterial). |
| Qualifiers | R066-R068 (3) | 29-31, 109-111, 124-126 | All present. |
| Agenda items | 3 | 136-144 | Read. Type column mapping unresolved (FN10). |
| A1 foot notes | 2 | 135-139, 140-144 | Read. |
| MISSING_FROM_STRUCTURED | M1-M5 | 90, 33, 145-147, 150-152, 95-98 | All read verbatim; all confirmed present in fulltext. |

Rows read 68 of 68 structured IDs, plus M1-M5, 3 agenda items and 2 notes. Reconciled 100%. No pipeline error; source access was not needed.

A2 cross-check on A1 entity mapping: A1 R032 ("Mrs Chitra Pandyan | Joint Managing Director per column") and R034 ("Mr Rajendra Iyer | Whole Time Director") rest on a row-by-row read of a misaligned table. See FN07. A2 flagged the layout break but kept the A1 designations.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F13 | R021, R022, R052, R061; A2 flag NO_VOTING_RESULTS | 148-149 | "the consolidated results of the vo ng will be declared within 48 hours of the conclusion of the EGM" | AMBIGUOUS | The document proves no resolution passed. QIP, share swap and promoter RPT stay PROPOSED until the Reg 44 voting result files (due about 21-Oct-2026). If Res 3 is the ordinary resolution, related-party holders do not vote, so non-promoter holders decide it. A4: check the result file before any status change. |
| FN02 | F13 | R011, R050, R021 (Res 2) | 106-108 | "proposed QIP of up to 700 crore, outlining the intended utilisation of proceeds towards the acquisition, working capital requirements, establishment of the Global Design Centre at Sangli and general corporate purposes" | FORWARD-SIGNAL | Enabling resolution foreshadows a funding round of up to 700 crore. Four uses named, no rupee split, no timing. Notion open item "use of ~Rs575 Cr of QIP beyond WSIL cash" (section 9, 25-Sep) is answered by category only. Dilution feeds FN11. |
| FN03 | F13 | R043, R050 | 107-108 | "establishment of the Global Design Centre at Sangli" | FORWARD-SIGNAL | A new named capex use. It is not on the Notion growth-trigger table (section 5). No cost, date or link to the Sangli plant is given. A4: ask cost, timeline, and whether it is separate from Sangli commissioning. |
| FN04 | F13 | M5 (MISSING_FROM_STRUCTURED), R049, R050 | 96-97 | "the proposed QIP for funding the Company's expansion plans and future strategic opportunities, and the promoter financing arrangements" | AMBIGUOUS | "future strategic opportunities" says the QIP is sized for unnamed further deals beyond WSIL. "arrangements" is plural (L97); the CFO explains one facility (L109, "facility"). Two readings: one bridge loan, or more promoter financing than the document details. Separating observation: the EGM notice explanatory statement for Res 3 (not in this document). |
| FN05 | F13 | R012, R013, R051, R067, R047 (Res 3) | 109-111; 142-144 | "unsecured promoter bridge loan facility of up to 175 crore, carrying interest at 9% per annum" / "Related Party Transac on(s) between (a) the Company and (b) the Promoters" | FORWARD-SIGNAL | Promoter money funds the deal before QIP money arrives (L111 "pending receipt of QIP proceeds"). At full draw, interest is Rs15.75 Cr a year (175 x 9%, arithmetic on document figures only). Notion memory (section 9, 07-Sep): FY26 had a Rs70 Cr unsecured Chitra Pandyan loan with terms undisclosed. This is a second promoter loan within about a year, and the first with a stated rate. The same memory records FY26 net cash Rs212 Cr. A4: ask why a net-cash company borrows from promoters at 9%, the drawn amount, and the repayment trigger. |
| FN06 | F14 | R014, R051 | 110-111 | "carrying interest at 9% per annum for 11 years, to facilitate the acquisition pending receipt of QIP proceeds" | AMBIGUOUS | An 11-year term contradicts a bridge that ends when QIP money arrives. Reading A: a drafting error (for example 1 year or 11 months). Reading B: long-dated promoter debt at 9%, so a lasting related-party interest stream. Separating observation: the tenor in the Res 3 explanatory statement, and the loan's maturity bucket in the Q3 FY27 balance sheet. Lean bear: treat as Reading B until the statement is read. |
| FN07 | F14 | R009, R030-R037; A2 note "table layout broken" | 59-67 | "2    Mr Bharanidharan Pandyan" (no designation) / "3    Mrs Chitra Pandyan              Joint Managing Director" / L67 stray "Independent Director" | AMBIGUOUS | The directors table has 8 names and 8 designations, offset by one row. Row-by-row reading (A1): Chitra Pandyan JMD, Rajendra Iyer WTD, 3 independent directors of 8. One-row-shift reading: Bharanidharan Pandyan JMD (agrees with L146 "Joint MD"), Chitra Pandyan WTD (agrees with Notion memory, 30-Sep AGM entry), Rajendra Iyer an Independent Director, 4 of 8. The independent-director count matters because Res 3 is a promoter RPT. A4: confirm board composition from the company's board page or the AGM notice. |
| FN08 | F14 | R010, R038 | 72; 98; 102 | L72 "Mrs Sarika Jadhav                      Chief Financial Officer" vs L102 "Rajesh Jayaraman, Chief Financial Officer" | NEUTRAL-FACT | The attendee table is offset the same way as FN07. Read row by row, it names the wrong CFO. Prose at L98 and L102 settles it: Rajesh Jayaraman is CFO. No forward effect. Counts toward the cumulative drafting tally. |
| FN09 | F14 | R028, R038 | 45, 70; 98, 102; 100 | L70 "Mr Deepak Suryanshi" vs L45 "Suryavanshi"; L98 "Mr Rajesh Jeyaraman" vs L102 "Jayaraman"; L100 "After the compila on of the speech" | NEUTRAL-FACT | Two officer-name misspellings and a wrong word ("compilation" for completion). The CFO hand-off is also recorded twice: the Chairman "invited" him (L98) and the CS "requested" him (L100-102). Each item is immaterial. Together with FN06-FN08 and FN10 there are 5 drafting defects in a 4-page filing. That is a governance data point on disclosure care at the time of a 700 crore raise. |
| FN10 | F14 | R021 (Res 1-3); A2 FOOTNOTE_UNRESOLVED | 136-139 | L136 "...Winwin    Special" / L138 "...share swap).                          Special" / L139 "Ordinary" | AMBIGUOUS | The type column ("Special", "Special", "Ordinary") does not line up with items 1-3 (L136, L140, L142). The document does not say which resolution is ordinary. This links to FN01: the vote threshold and who may vote depend on the type. A4: confirm types from the EGM notice or the voting-result file. |
| FN11 | F10 | R048, R041, R011, R050 (Res 1, Res 2) | 136-138; 140-141 | "Issuance of equity shares to certain selling shareholders of Winwin Speciality Insulators Limited by way of preferential issue (for considera on other than cash/share swap)" | FORWARD-SIGNAL | Two new equity channels sit on one agenda: a preferential share swap and a QIP of up to 700 crore. The document gives no share count, issue price or paid-up capital, so dilution is NOT FOUND in this document. Notion memory (section 9, 25-Sep) gives swap about 1.3% plus QIP about 6%, total about 7% [memory INFERENCE]. A4: test the total against the section 4 dilution amber line (">8% within 24 months") together with ESOP terms (checklist 15). |
| FN12 | F15 | R041, R049; A2 flag ENTITY_CHANGE | 95-96 | "the proposed acquisi on of Winwin Speciality Insulators Limited" | FORWARD-SIGNAL | The consolidation perimeter changes when the deal completes: WSIL becomes a new subsidiary (up to 100% per Notion memory, completion by 31-Mar-27). No consolidation list is in this document. A4: watch the Q3/Q4 FY27 results entity list, and the goodwill on consolidation, because WSIL profit is undisclosed (FN15). |
| FN13 | F17 | M3 (MISSING_FROM_STRUCTURED) | 145-147 | "Mr. Bharanidharan Pandyan, Joint MD answered the queries/ques ons of shareholders." | AMBIGUOUS | A Q&A took place but no question or answer is recorded. Notion memory (section 9, 30-Sep AGM entry) says the same of the 29-Sep AGM: "JMD answered shareholder queries (content not disclosed)". That is 2 consecutive general meetings with undisclosed Q&A. Checklist silences are in section 4 below. A4: put the silent items to IR. |
| FN14 | F13 | R008; M1 (MISSING_FROM_STRUCTURED) | 79; 90 | "35 members attended the Extraordinary General Meeting" / "As the requisite quorum was present" | NEUTRAL-FACT | No quorum count is stated. 35 members attended a 40-minute meeting (L55) that took up a 700 crore QIP and a promoter RPT. Notion memory: 60 members at the 29-Sep AGM. Low engagement; this does not change the outcome, which rests on e-voting (FN01). |
| FN15 | F6 | R053, R041 | 103-105 | "including its strategic ra onale, considera on and expected opera onal benefits" | AMBIGUOUS | The CFO briefed on consideration and "expected operational benefits" but the document gives no figures. Notion memory (section 5, 9): WSIL profit NOT DISCLOSED since the 23-Sep SPA. This is the second filing silent on target profit (SPA outcome, EGM outcome). A4: ask WSIL FY26 EBITDA/PAT, net debt, and the quantified benefits; this feeds checklist item 12. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No financial statements in this document. Ledger has 0 ZERO_STANDING rows (A2 count test: line_items n/a). |
| F2 Standalone vs consolidated decomposition | N.A. | No standalone or consolidated figures. |
| F3 Shell-entity detection | N.A. | No cost lines, no entity financials. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph (A2: auditor_paras 0). |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph; no prior-quarter fulltext passed. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hits: "will be" (L149, L151), "commenc" (L55, L122). "proposed" (L95-97, L103, L106, L109) is read as "proposes to". 7 commitments in the register (section 3). One finding (FN15). |
| F7 Hedge phrase mining | PASS | No hit in the full 171 lines for "may sometimes", "could have an effect", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour". The open phrase "future strategic opportunities" (L97) is not in the lexicon; it is logged under F13 (FN04). |
| F8 Tax forensics | N.A. | No tax lines. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | FINDING | FN11. Two equity-issue resolutions; no share count or paid-up capital in the document. |
| F11 Reserves and net worth tie-out | N.A. | The document carries no Other Equity, paid-up or net worth figure to tie out. |
| F12 Segment forensics | N.A. | No segment data. |
| F13 Board outcome beyond the results | FINDING | FN01-FN05, FN14. Capital-raise enabling resolution, promoter RPT and bridge loan, new Sangli design centre, no voting result. No director term dates in the document. |
| F14 Note drafting inconsistencies | FINDING | FN06-FN10. 5 drafting defects across 4 pages (tenor, two misaligned tables, name spellings, type column). |
| F15 Entity list diffs | FINDING | FN12. Proposed new subsidiary WSIL (A2 ENTITY_CHANGE). No consolidation list in the document; the change is prospective. |
| F16 Dropped and reframed disclosures | N.A. | One-off EGM proceedings. No prior deck of this doctype, and no prior-quarter fulltext was passed, so nothing can be diffed. |
| F17 Silence audit | FINDING | Applied because the document records a shareholder Q&A (L145-147) and the orchestrator supplied the Notion checklist. FN13 and the table in section 4. |

All 17 checks marked. No blanks. GATE A3: pass.

## 3. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Ref | Status word |
|---|---|---|---|---|
| C1 | Declare consolidated voting results; display them at the registered office and on the company, BSE, NSE and RTA websites | By about 21-Oct-2026 (48 hours after the 16:40 IST conclusion; e-voting open to about 16:55 IST) | L148-153 (R022, R052, R061, M4) | initiated |
| C2 | QIP of up to 700 crore for the acquisition, working capital, Global Design Centre at Sangli and general corporate purposes | Undated in document | L106-108, L140-141 (R011, R050) | initiated |
| C3 | Establish the Global Design Centre at Sangli (QIP use) | Undated in document | L107-108 (R043) | initiated |
| C4 | Acquire Winwin Speciality Insulators Limited, consideration partly by preferential share swap | Undated in document (Notion memory: completion by 31-Mar-27) | L95-96, L103-105, L136-138 (R041, R048, R049, R053) | initiated |
| C5 | Unsecured promoter bridge loan up to 175 crore, 9% p.a., "for 11 years", to fund the acquisition pending QIP proceeds | Drawdown before QIP receipt; tenor contradictory (FN06) | L109-111 (R012-R014, R051, R067) | initiated |
| C6 | Related-party transaction(s) between the Company and the Promoters / Promoter Group | Undated in document | L142-144 (R047) | initiated |
| C7 | Remote e-voting (16-Oct 09:00 to 18-Oct 17:00 IST) and in-meeting e-voting open 15 minutes after conclusion | 16-Oct to 19-Oct-2026 | L122-126, L154-156 (R019, R020, R058, R059, R024) | completed |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit vs Notion sections 4, 5, 7, 9)

Consecutive-quarter counts are limited. The Notion page has no Q1 FY27 reconciliation (brief, line 2), so quarter counts before Q2 FY27 are NOT FOUND. Where memory records a prior silent document, the count is in documents.

| Checklist / commitment item | Source (Notion) | Addressed in EGM outcome? | Consecutive silence | Note |
|---|---|---|---|---|
| 5 Sangli commissioning status (thesis-broken item if post-Mar-27) | s7 #5; s4 thesis-broken | NO. Only "Global Design Centre at Sangli" (L107-108) | 2 documents (29-Sep AGM "no new financial information", this EGM); quarters NOT FOUND | Most material silence. The trial was due Aug 2026 (s5). The Chairman's briefing (L95-97) covers the deal, QIP and financing only. |
| 11 WSIL closure timing | s7 #11 | NO date in document | 1 document | Memory: completion by 31-Mar-27. |
| 12 WSIL operating margins / profit | s7 #12; s5 "profit NOT DISCLOSED" | NO. Benefits named, not quantified (L105) | 2 filings (23-Sep SPA outcome, this EGM) | FN15. |
| 14 Raise utilisation (USD 75M, superseded by 700 crore QIP) | s7 #14; s9 25-Sep open item | PARTIAL. Categories only (L106-108) | n/a | FN02. No rupee split. |
| 10 Promoter pledge | s7 #10 | NO | 1 document | Not expected in EGM proceedings. Relevant because promoters now lend to the company (FN05). |
| 15 ESOP definitive terms | s7 #15 | NO | 1 document | Bears on FN11 total dilution. |
| s4 Promoter background re-verification | s4 thesis-broken | NO | 1 document | The promoter RPT (Res 3) and the bridge loan put this item in play. |
| Promoter loan terms (Rs70 Cr FY26 Chitra Pandyan loan, terms undisclosed) | s9 07-Sep | PARTIAL. The new loan's rate is given (9%); the FY26 loan is not mentioned | n/a | FN05, FN06. |
| 1-4, 6, 7, 9 financial and operating metrics | s7 | NO | n/a | Not expected in EGM proceedings. Silence carries no signal here. |
| 8 Atlanta/peer HVDC qualification | s7 #8; s4 | NO | n/a | Tracked in peer filings, not in a QPOWER EGM. Silence carries no signal here. |
| 16 Internal audit report; 17 cost auditor rotation | s7 | NO | n/a | Not expected in EGM proceedings. |

No silence item is a confirmatory negative. No deteriorating metric is known from this document; lean bear and ask, per rule 6.

```yaml
stage: A3-forensics
company: "QPOWER"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/qpower-q2fy27/work/forensics_egm_qpower_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN01", check: "F13", line: "148-149", classification: "AMBIGUOUS", implication: "No voting result in document; QIP, swap and promoter RPT stay proposed until Reg 44 result (due ~21-Oct-2026); if Res 3 is ordinary, non-related holders decide it"}
  - {id: "FN02", check: "F13", line: "106-108", classification: "FORWARD-SIGNAL", implication: "QIP up to 700 crore enabling resolution; four uses named, no rupee split or timing; Notion ~Rs575 Cr open item answered by category only"}
  - {id: "FN03", check: "F13", line: "107-108", classification: "FORWARD-SIGNAL", implication: "New named capex use: Global Design Centre at Sangli; not on Notion trigger table; no cost or date"}
  - {id: "FN04", check: "F13", line: "96-97", classification: "AMBIGUOUS", implication: "'future strategic opportunities' implies QIP sized for unnamed further deals; plural 'promoter financing arrangements' vs one facility at L109"}
  - {id: "FN05", check: "F13", line: "109-111; 142-144", classification: "FORWARD-SIGNAL", implication: "Unsecured promoter bridge up to 175 crore at 9% = up to Rs15.75 Cr/yr interest at full draw; second promoter loan in ~1 year (FY26 Rs70 Cr, memory); net-cash company borrowing from promoters"}
  - {id: "FN06", check: "F14", line: "110-111", classification: "AMBIGUOUS", implication: "'9% per annum for 11 years' contradicts a bridge ending on QIP receipt; drafting error vs long-dated promoter debt; lean bear until Res 3 explanatory statement read"}
  - {id: "FN07", check: "F14", line: "59-67", classification: "AMBIGUOUS", implication: "Director table offset by one row; independent directors 3 or 4 of 8; shift reading matches L146 JMD and memory WTD; matters for promoter RPT oversight"}
  - {id: "FN08", check: "F14", line: "72; 98; 102", classification: "NEUTRAL-FACT", implication: "Attendee table offset; L72 places CFO beside Sarika Jadhav; prose L98/L102 confirms Rajesh Jayaraman is CFO"}
  - {id: "FN09", check: "F14", line: "45, 70; 98, 102; 100", classification: "NEUTRAL-FACT", implication: "Officer-name misspellings (Suryanshi, Jeyaraman), 'compilation' for completion, duplicated CFO hand-off; cumulative 5 drafting defects in 4 pages"}
  - {id: "FN10", check: "F14", line: "136-139", classification: "AMBIGUOUS", implication: "Resolution type column Special/Special/Ordinary not aligned to items 1-3; which is ordinary unresolved; sets vote threshold and voter eligibility"}
  - {id: "FN11", check: "F10", line: "136-138; 140-141", classification: "FORWARD-SIGNAL", implication: "Two equity channels (preferential swap + QIP up to 700 crore); share count and paid-up NOT FOUND in document; memory ~7% total; test vs >8%/24-month amber with ESOP"}
  - {id: "FN12", check: "F15", line: "95-96", classification: "FORWARD-SIGNAL", implication: "WSIL becomes a new subsidiary on completion; consolidation perimeter and goodwill change in Q3/Q4 FY27 results"}
  - {id: "FN13", check: "F17", line: "145-147", classification: "AMBIGUOUS", implication: "Q&A held, content unrecorded; second consecutive general meeting with undisclosed Q&A; Sangli commissioning, WSIL profit and closure timing silent"}
  - {id: "FN14", check: "F13", line: "79; 90", classification: "NEUTRAL-FACT", implication: "35 members attended, quorum count not stated, 40-minute meeting; outcome rests on e-voting"}
  - {id: "FN15", check: "F6", line: "103-105", classification: "AMBIGUOUS", implication: "'expected operational benefits' unquantified; WSIL profit undisclosed for second filing; feeds checklist item 12"}
forward_signals: ["FN02", "FN03", "FN05", "FN11", "FN12"]
ambiguous: ["FN01", "FN04", "FN06", "FN07", "FN10", "FN13", "FN15"]
commitments:
  - {commitment: "Declare consolidated voting results; display at registered office and company, BSE, NSE, RTA websites", implied_date: "by ~2026-10-21 (48h after 16:40 IST 19-Oct conclusion)", ref: "L148-153", status_word: "initiated"}
  - {commitment: "QIP up to 700 crore for acquisition, working capital, Global Design Centre at Sangli, general corporate purposes", implied_date: "undated in document", ref: "L106-108, L140-141", status_word: "initiated"}
  - {commitment: "Establish Global Design Centre at Sangli (QIP use)", implied_date: "undated in document", ref: "L107-108", status_word: "initiated"}
  - {commitment: "Acquire Winwin Speciality Insulators Limited, partly by preferential share swap", implied_date: "undated in document (memory: by 2027-03-31)", ref: "L95-96, L103-105, L136-138", status_word: "initiated"}
  - {commitment: "Unsecured promoter bridge loan up to 175 crore, 9% p.a., 'for 11 years', pending QIP proceeds", implied_date: "drawdown before QIP receipt; tenor contradictory", ref: "L109-111", status_word: "initiated"}
  - {commitment: "Related-party transaction(s) between Company and Promoters / Promoter Group", implied_date: "undated in document", ref: "L142-144", status_word: "initiated"}
  - {commitment: "Remote e-voting 16-18 Oct and in-meeting e-voting open 15 minutes after conclusion", implied_date: "2026-10-16 to 2026-10-19", ref: "L122-126, L154-156", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The document proves no resolution passed. It carries no vote counts (L148-149). Treat the QIP, swap and RPT as proposed until the Reg 44 result files. The forensic weight sits in promoter financing. The bridge loan has stated terms (175 crore, 9%, unsecured, L109-111); the FY26 Rs70 Cr Chitra Pandyan loan had none (memory). Reading A: a short bridge to close the WSIL cash leg before the QIP, with '11 years' a drafting error. Reading B: long-dated promoter debt at 9% in a company with Rs212 Cr FY26 net cash (memory). The separating observation is the Res 3 explanatory statement tenor and the drawn amount at the Q3 FY27 balance sheet. 'Future strategic opportunities' and the plural 'arrangements' (L97) suggest the 700 crore is sized beyond WSIL. The Sangli design centre (L107-108) is an unpriced new use. The offset director table (L59-67) leaves independent directors at 3 or 4 of 8, which matters for a promoter RPT. Sangli commissioning, a thesis-broken item, gets no mention."
```
