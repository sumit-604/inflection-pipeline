# HFCL LIMITED (HFCL): Q2 FY27 MERGED QUARTERLY REVIEW (A4 ANALYST)

Quarter: Q2 and H1 FY27, ended 30-Sep-2026. Board and results: 19-Oct-2026.
Protocol: Role 4, Quarterly Results Review Protocol v1.4 (frameworks/Quarterly_Results_Review_Protocol_v1_4.md).
Role 5 (concall): NOT run. The 19-Oct-2026 concall transcript is not yet produced. Every concall section is marked "pending Role 5 addendum".
Role 4 Steps 6.5 and 7: deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts are flagged in place.
Model: claude-opus-5-5. Run date: 2026-10-20. Operator asleep: protocol STOP lines run as flags.
Revision: LOOP 2 (final), after A5 re-audit runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_loop1.md. Loop 1 fixed F1, C1, M4, M5 and cited ledger rows M01-M08 and PM01-PM07. Loop 2 fixes L1-F1 (para 7 subsidiary cash reading) and style notes L1-S1 to L1-S5. Both change logs follow the closing YAML.

This review is one document: Part 1 (preamble, Steps 0-5) is followed directly by Part 2 (Step 5.5 to Step 9, questions, monitorables, Plain-Language Brief, closing YAML, change logs). This agent has no edit or shell tool and its output size is limited, so it writes the two parts as separate files for the orchestrator to join, Part 2 immediately after Part 1, into runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md.

## ANCHOR CONVENTION

| Prefix | Source (A1 fulltext, line number) |
|---|---|
| R-L### | runs/hfcl-q2fy27/extracted/hfcl-results-q2fy27-fulltext.md. Pages 5-8 values cited ONLY at the image-transcription lines L801-L994, never at the superseded OCR lines. |
| P-L### | runs/hfcl-q2fy27/extracted/hfcl-presentation-q2fy27-fulltext.md. Slides 8-10 statement cells are PAIRING_UNRESOLVED and are not used. |
| M-L### | runs/hfcl-q2fy27/extracted/hfcl-mareport-q2fy27-fulltext.md (CARE Monitoring Agency reports, QIP and preferential warrants). |
| [MEMORY] | runs/hfcl-q2fy27/work/notion-brief.md. Memory to weigh, never anchored evidence. |
| [COMPUTED] | Arithmetic on anchored cells, formula shown. |
| [INFERENCE] | Reasoning, not a filed fact. |

A3 finding IDs collide across documents. In this review they carry prefixes: RES- (results forensics), PPT- (presentation forensics), MA- (Monitoring Agency report forensics).

Superseded pointers: A2 has corrected R141 to R1479 (Rs90 Cr warrant FD, R-L869) and R162 to R1486 (statement date, R-L889). This review reads both cells at the fulltext lines. R164 and R165 carry the label "Others segment revenue"; the values 136.07 and 280.32 are Turnkey revenue (R-L841).

---

## LEDGER RECONCILIATION PREAMBLE (contractual, before Step 1)

Ledger contains 10 notes / 0 turns / 25 slides. All 10 notes, all 25 slides and all 25 Monitoring Agency report pages reviewed, including A2-added rows M01-M08 (results) and PM01-PM07 (presentation). Findings incorporated: RES-FN-01 to RES-FN-29, PPT-FN-01 to PPT-FN-21, MA-FN-01 to MA-FN-14.

| Ledger | Rows | Orphans | Count test | Rows read at cited line | Unreviewed rows |
|---|---|---|---|---|---|
| ledger_results_hfcl_q2fy27.md | 1,515 (structured R001-R1507 + A2 rows M01-M08) | none | gate_a2 pass; notes 10 = 10 | 1,515 of 1,515 | none |
| ledger_presentation_hfcl_q2fy27.md | 431 (structured R001-R424 + A2 rows PM01-PM07) | none | gate_a2 pass; slides 25 (5 slides carry no rows: 4, 6, 12, 18, 21) | 431 of 431 | none |
| ledger_mareport_hfcl_q2fy27.md | 411 (R001-R411) | none | gate_a2 pass; pages 25; notes 0 | 411 of 411 | none |

Notes in the results ledger: Note 1, Note 2, Note 3(i), Note 3(ii), Note 4, Note 4(o), Note 5, Note 6, cash-flow note 1, cash-flow note 2 = 10.
Turns: 0. No transcript in this run (Role 5 pending).
Every ledger row is reviewed. The review proceeds.

### A2-added rows (MISSING_FROM_STRUCTURED), each reviewed at its fulltext line

| Row | Line | Content | Use in this review |
|---|---|---|---|
| M01 | R-L57-58 | Reg 47 newspaper publication arranged | Boilerplate. No finding. Board-outcome scope (Step 0D, RES-FN-24). |
| M02 | R-L60 | Results also on www.hfcl.com | Posting notice, not a business commitment. No finding. |
| M03 | R-L80-83 | Enclosures: results and review reports, assets and liabilities, cash flow, press release | Confirms the board outcome covers results only (Step 0D; RES-FN-24; Q32). |
| M04 | R-L42 | Reg 30 read with Para A Part A Schedule III | Board-outcome scope (RES-FN-24). |
| M05 | R-L263, R-L135 | Oswal Sunil partner Membership No. 056931 on both reports | Signatories consistent. No drafting gap. |
| M06 | R-L221-222 | Para 6 shells: total comprehensive income (0.17) Q2, (0.18) H1 | TCI equals NPAT; shells carry no OCI (Step 0D para 6 row). |
| M07 | R-L238 | Para 7 four subsidiaries: net cash flows (0.29), Apr-Sep 2026 | Cash balances fell 0.29; operating cash flow NOT FOUND (Step 5C; RES-FN-28; Q36). |
| M08 | R-L749-750 | PR: "Our advanced optical fiber cable portfolio and data centre connectivity solutions continue to strengthen." | Forward claim, no metric (RES-FN-29; Step 6D trigger 4; Q37). |
| PM01 | P-L215 | Slide 8 token "1.49" (Q1 FY27 diluted EPS) | Matches R-L835 (Step 0C; Step 0F Q9). |
| PM02 | P-L119-120 | "Secured raw materials and advanced cable capabilities strengthen our ability to capture this long-term opportunity." | PPT-FN-17; Q38. |
| PM03 | P-L467-471 col 1 | OF/OFC "higher value realization amid a structural demand upcycle" | PPT-FN-18; Q39. |
| PM04 | P-L467-471 col 2 | PCS/DC "Emerging as a high-growth adjacency to the OFC business, driven by exports and hyper-scalers/ data centers" | PPT-FN-19; Step 6D trigger 4; Q37. |
| PM05 | P-L503-518 col 1 | Value-added products "to aid margins and ease working capital"; hyperscaler OFC; defence value chain | PPT commitments C-19, C-20; PPT-FN-12 extended. |
| PM06 | P-L532-533 | "#1 in OFC and strong market share in Wifi and UBR" | PPT-FN-20; Q40; Brief part 4. |
| PM07 | P-L537-538 | "Actively catering to Domestic telcos and Bharatnet for rapid roll out" | PPT-FN-21; Step 6B item 6; Q41. |

A3 finding counts incorporated:
- Results: 29 findings (7 FORWARD-SIGNAL, 16 AMBIGUOUS, 1 CONFIRMATORY-NEGATIVE, 5 NEUTRAL-FACT).
- Presentation: 21 findings (5 FORWARD-SIGNAL, 14 AMBIGUOUS, 2 NEUTRAL-FACT).
- MA report: 14 findings (4 FORWARD-SIGNAL, 8 AMBIGUOUS, 2 NEUTRAL-FACT).
- 54 FORWARD-SIGNAL or AMBIGUOUS findings in total. Each maps to at least one Questions-for-Management row (Step 8.5C coverage table).

A4 correction to an A3 finding (recorded, not hidden): MA-FN-13 treats "HFCL Technologies Private Limited" as "HTL" and asks for its ownership. The results filing Note 4(h) lists "HFCL Technologies Private Limited (Wholly owned Subsidiary)" (R-L878). HTL Limited is a different entity, listed as "(Subsidiary)", not wholly owned (R-L872). The Rs175 Cr preform object therefore goes to a wholly owned subsidiary. The open part of MA-FN-13 is the instrument (equity or loan) and the transfer price of preform to the parent.

---

## STEP 0: PRE-FLIGHT

### 0A. Notion page (memory, fetched live 2026-10-19 by the orchestrator)

| Item | Notion content [MEMORY] |
|---|---|
| Decision Status | WATCHLIST ("DO NOT INITIATE"). Verified before any position framing. |
| Held? | Not held. Position zero. Avg cost ND. Cap "SMALL (2-3%) max, capped by Promoter CONCERN". |
| Entry zone | Rs60-75 (Entry Price Max 75; MoS price 60; bull-stretch entry Rs99). |
| CMP on page | Rs262 (screener.in, 14-Oct-2026). 52-week range Rs59.8-276. |
| One-line thesis | Buy at Rs60-75 because EPS grows from Rs2.04 (FY26) to Rs6.19 (FY29 base), a 45% PAT CAGR, on the hyperscaler OFC contract, HASPL defence-aerospace consolidation and capacity to 42.36 mn fkm by Dec-2026; destination PE 25x (user override; framework range 14-18x). |
| Four-pillar destination PE | Pillar 1 ROCE base 12x; Pillar 2 cash multiplier 0.85x; GVP +6.0x (legacy) / +6.3x (RRM); strategic premium +2.0x; sector cap blend ~25x; UA 1.25x NOT ELIGIBLE (FII+DII 18.54%); destination 14.4x (RRM v3.2) / 18.2x (legacy); override 25x. |
| Bear/Base/Bull | Base FY27: revenue 6,200; EBITDA margin 17.5%; PAT 520; EPS 3.15; net debt 1,800; ROCE 12.5%. FY27 bear and bull rows not on page (only FY29 EPS bear 2.69, bull 7.36). |
| Thesis-broken triggers | 6 listed (Step 6C). |
| Monitoring checklist | 5 original items plus added items 6-13, the 13-Oct "H1 gate" legs, AR watchpoints (Step 6B). |
| Devil's advocate split | Bear 35 / Base 45 / Bull 20. Probability-weighted return at CMP Rs197: minus 13.8% a year. |
| Promoter Verdict | CONCERN. Ruling pending since 03-Oct: slip #5 (Nivetti #2) moves CONCERN toward AVOID under the operator's own rule. Operator-only. |
| Gate 0 | Core 22/100; Moat 10/60; classification AVOID (backward). |

Prior-quarter questions (15) and the Q1 promise seed log are on the page. The Q1 concall was never scored. Both are tracked in Step 0F and Step 0G below.

### 0B. Unit convention

All filing figures are in Rs Crore ("UNIT: Rs Crore (EPS in Rs)", R-L803; "All amounts in Rs.crore", R-L893). Conversion factor: 1. No conversion applied. Presentation: "All numbers in Rs. Crore" (P-L163). MA report: Rs crore.

### 0C. Share-count changes

| Event | Detail | Anchor | EPS comparability |
|---|---|---|---|
| QIP (FY26) | 8,79,29,651 shares at Rs62.55; ~Rs550.00 Cr | R-L868 | Paid-up capital 144.21 (Q2 FY26) to 153.03 (Q1 FY27) = +6.12% [COMPUTED: 153.03 / 144.21]. YoY EPS growth is diluted by this. |
| ESOP (H1 FY27) | Paid-up 153.03 to 153.04; share-capital proceeds 0.26 | R-L832, R-L979 | Immaterial. |
| Promoter warrants | 7,50,00,000 warrants at Rs74; 25% (Rs138.75 Cr) received 25-May-2026; 75% (Rs55.50 each, Rs416.25 Cr) due within 18 months of allotment | R-L869; M-L1056-1058 (allotment 25.05.2026) | 4.90% potential dilution [COMPUTED: 7.5 / 153.04]. Diluted EPS now below basic: consolidated 2.36 vs 2.37 (R-L834-835). Q1 diluted 1.49 equalled basic (R-L835; deck token PM01, P-L215). |
| Split / bonus / buyback | None disclosed | R-L866-887 | None. |
| Deck share count | 1,53,06,02,463 shares at 30-Sep-2026 | P-L574 | Differs from paid-up Rs153.04 Cr at Re1 by about 2 lakh shares [COMPUTED]. Unexplained (possible ESOP trust or post-period allotment). Small. |

EPS (share-adjusted) equals EPS (reported). No split or bonus occurred. Reported EPS already uses weighted shares after the QIP.

Memory correction: the Notion promise log carries the warrant balance as "~Rs412.5 cr". The filed figure is Rs416.25 Cr (M-L1056; R-L869: 7.5 cr x Rs55.50).

### 0D. Notes extraction (all numbered notes, plus auditor paragraphs that act as notes)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 | Approval | Audit Committee reviewed; Board approved on 19-Oct-2026 (R-L866). Enclosure list confirms results only (M03, R-L80-83). | Nil | Q2/H1 FY27 | None. |
| 2 | Ind AS | Results comply with Ind AS under Section 133 (R-L867). | Nil | All | None. |
| 3(i) | QIP proceeds | Rs550.00 Cr QIP in FY26; Rs525.67 Cr used; Rs24.33 Cr unused, held as FD Rs21.22 Cr (incl. Rs0.20 Cr interest) and Rs3.31 Cr in the monitoring account (R-L868). | 24.33 unused | FY26 issue, H1 FY27 use | Share count +6.12% YoY (Step 0C). MA report: Rs21.22 Cr of this FD is LC margin (M-L503), not free cash (MA-FN-09). |
| 3(ii) | Promoter warrants | 7.5 cr warrants at Rs74 to one promoter and one promoter-group member; Rs138.75 Cr received 25-May-2026; Rs48.75 Cr used; Rs90 Cr in FD (R-L869). Allotment date not stated in the note (RES-FN-25h); MA report states 25.05.2026 (M-L1056-1058). | 138.75 received; 416.25 due | H1 FY27 and to ~25-Nov-2027 [COMPUTED] | Diluted EPS below basic from Q2 (RES-FN-18). Other-equity roll-forward gap of 30.6 (RES-FN-03). |
| 4 | Consolidation list | 15 entities incl. parent; HTL Limited and Raddef are non-wholly-owned subsidiaries; HFCL Advance Systems, HFCL Technologies, HFCL Inc., HFCL B.V. and others are WOS; two JCEs (R-L870-885). | Nil | All | NCI (Rs31.30 Cr Q2, R-L829) can only come from HTL Limited or Raddef (RES-FN-04). |
| 4(o) | Entity deletion | HFCL Pty Limited, Australia (step-down via HFCL B.V.) voluntarily liquidated and deregistered w.e.f. 19-Aug-2026 (R-L885). | No exceptional item (R-L818); reclassifiable OCI Q2 only 0.30 (R-L825) | Q2 FY27 | None material (RES-FN-27). |
| 5 | EPS | EPS not annualised for quarter and half year (R-L886). | Nil | All | Annualise manually where needed. |
| 6 | Regrouping | Prior-period figures regrouped where necessary (R-L887). | Not quantified | Prior periods | Prior columns may differ from the Q1 and Q2 FY26 filings as first printed. No restatement amount given. Conservative read: small comparability risk. |
| CF-1 | Cash flow method | Indirect method, Ind AS 7 (R-L993). | Nil | H1 | None. |
| CF-2 | Brackets | Brackets mean outflow (R-L994). | Nil | H1 | None. |
| Auditor para 6 (consolidated) | Other auditors | 3 subsidiaries (total assets 8.84, revenue nil, Q2 NPAT (0.17), TCI (0.17) Q2 and (0.18) H1 per M06, H1 net cash flows +0.14) and 2 JCEs (share Q2 (0.32)) reviewed by other auditors whose reports management furnished (R-L218-228). | (0.49) of PAT | Q2/H1 | Shells; 0.12% of PAT (RES-FN-08, RES-FN-09). |
| Auditor para 7 (consolidated) | One joint auditor | 4 subsidiaries (total assets 980.98; Q2 revenue 841.57; Q2 NPAT 123.40; H1 NPAT 186.19; H1 net cash flows (0.29) per M07) reviewed by one of the joint auditors; conclusion "based solely on the reports of such joint auditor" (R-L233-241). | 123.40 = 31.30% of Q2 PAT [COMPUTED: 123.40 / 394.22] | Q2/H1 | The fastest-growing profit pool has single-auditor assurance (RES-FN-09). Its H1 cash balances fell 0.29; its operating cash flow is NOT FOUND (RES-FN-28). |
| Auditor para 8 (consolidated) | Foreign subsidiaries | 2 foreign subsidiaries (total assets 1,238.36; Q2 revenue 1,066.16; Q2 NPAT 24.68; H1 net change in cash +36.24) converted to Indian GAAP by parent management (R-L243-253). | 24.68 = 6.26% of Q2 PAT | Q2/H1 | Para 8 revenue = 41.95% of consolidated revenue [COMPUTED: 1,066.16 / 2,541.79]. |

Answers to the four note questions:
- Change in YoY or QoQ interpretation: yes. The QIP lifts the share count +6.12% YoY. The warrants now dilute. The para 7 profit pool doubled QoQ. Note 6 regrouping is not quantified.
- Normalisation needed: no exceptional item in any column (R-L818). Two operating one-offs are named in Step 3 (seasonal employee cost, subsidiary inventory release). No note-level normalisation is required.
- Recurring vs one-off: Note 4(o) is one-off with no P&L effect. The deferred-tax credits are recurring so far (RES-FN-16).
- Thesis assumption change: yes. Para 7 and para 8 concentrate profit outside the parent (Notion Q1 questions 3 and 4). Note 3(ii) confirms the Rs416.25 Cr warrant balance is unpaid.

Auditor opinion check: limited review conclusions on both standalone and consolidated statements are UNMODIFIED (R-L122; R-L255 "is not modified"). No Emphasis of Matter, no Going Concern paragraph, no qualification (A2 ledger section 2; RES F5 PASS). Paras 6-8 are reliance paragraphs. No AMBER flag from the opinion itself. The reliance concentration is carried as RES-FN-09. Signatories are consistent across both reports (M05).

Drafting gaps: nine small inconsistencies in the filing (RES-FN-25), plus press-release EBITDA that includes other income without saying so (RES-FN-26). Cumulative governance data point only.

Board outcome: the letter names only the results, with "inter-alia" (R-L44; M04); the enclosure list (M03) holds results, review reports, assets and liabilities, cash flow and the press release. M01 and M02 are boilerplate. No other board item is filed (RES-FN-24).

### 0E. Business type

Standard operating business (telecom products, OFC, defence products, turnkey EPC). Steps 1 and 5 apply. Lender variant not used.

### 0F. Prior-quarter Questions for Management (Q1 FY27, 22-Jul-2026): answer status from Q2 FILINGS ONLY

The Q1 concall transcript was never scored. The Q2 concall is pending Role 5 addendum. Status below reflects only what the three Q2 documents disclose. The Role 5 addendum must re-mark each row against the 19-Oct call.

| # | Q1 question (short) [MEMORY] | Q2 filed evidence | Status (filings only) |
|---|---|---|---|
| 1 | Hyperscaler Export-OFC revenue in Rs Cr; share of order book | Deck gives exports "63% of revenues" (P-L507), base period unstated; book "57% ... from export" (P-L314). No Export-OFC rupee figure. | NOT ADDRESSED |
| 2 | FY27 guide a floor or aspiration? | Guide raised to "at least 80%"; word changed from aspiration to "we now expect" (R-L743; P-L111). Basis still unstated (RES-FN-10). | PARTIALLY ANSWERED |
| 3 | Which subsidiary earns the consolidated PAT excess; margin; transfer pricing | Gap widened to 126.20 (47.09%). Para 7 four subsidiaries earned 123.40 (R-L236). Entities not named. | NOT ADDRESSED |
| 4 | Auditor paras 7-8; confirm 3 HFCL B.V. step-downs captured | Para 8 covers HFCL B.V. "as per consolidated financial results" (R-L197); HFCL Pty liquidated (R-L885). | PARTIALLY ANSWERED |
| 5 | BharatNet III revenue, PBT margin, receivables | Not named in the results. Deck: "Actively catering to Domestic telcos and Bharatnet for rapid roll out" (PM07, P-L537-538), no figure. Turnkey revenue 136.07, result (122.58) (R-L841, R-L846). | NOT ADDRESSED |
| 6 | DSO, TR/TTM, >6-month ageing; inventory deferral | Balance sheet gives receivable rupees (R-L902, R-L909). No ageing, DSO or unbilled figure. | NOT ADDRESSED |
| 7 | Is 25-26% the steady-state ETR? | Q2 ETR 26.81% consolidated, 25.24% standalone (Step 1). Data consistent; no statement. | PARTIALLY ANSWERED |
| 8 | Q1 OCI +72.16: source? | Q2 consolidated OCI items not reclassified reversed to (13.71) (R-L823). Source not stated (RES-FN-17). | NOT ADDRESSED |
| 9 | Diluted EPS equals basic despite warrants | Q2 diluted 2.36 vs basic 2.37 consolidated; 1.74 vs 1.75 standalone (R-L834-835). Q1 diluted 1.49 (PM01, P-L215). | ANSWERED (by the numbers) |
| 10 | Rs215 Cr DC-connectivity facility: funding, revenue, margin | Absent from the deck (PPT-FN-11). DC connectivity described only as "high-growth adjacency" (PM04) and "continue to strengthen" (M08). | NOT ADDRESSED |
| 11 | Defence book via entity to be acquired: target, consideration, structure, close | Deck: ~Rs1,850 Cr total, ~Rs1,600 Cr via "an entity proposed to be acquired" (P-L469-470). PR: acquisition "expected to be completed during the current quarter" (R-L754). Target, consideration and structure not named. | PARTIALLY ANSWERED |
| 12 | Promoter holding 28.29%; confirm pledge zero | Holding 28.29% at 30-Sep-2026 (P-L569). Pledge not stated. | PARTIALLY ANSWERED |
| 13 | Reaffirm capacity completion Dec-2026 | Deck shows only "Expanding by July 2028" and "Current: 28 / 39 mn fkm" (P-L428-434). Dec-2026 step absent (PPT-FN-10). | NOT ADDRESSED (date dropped) |
| 14 | Export share base period; durability | "63%" again without base period (P-L507, P-L535). | NOT ADDRESSED |
| 15 | Order book executable split and margins | Category split 4,090 / 5,070 / 19,751 and customer split 10,105 / 18,806 (P-L302-312). No execution schedule, no margins. | PARTIALLY ANSWERED |

Score: 1 ANSWERED, 6 PARTIALLY ANSWERED, 8 NOT ADDRESSED in the filings. Questions 1, 5 and 6 were the Q1 top three; all three remain NOT ADDRESSED in the filings. Repeated non-address across Q1 and Q2 is a governance signal under the protocol, but the Q2 concall may have answered them. Final status waits for the Role 5 addendum.

### 0G. Q1 promise seed log scored against Q2 filings (first scoring; Q1 concall never scored)

| Seed commitment [MEMORY] | Q2 filed evidence | Status |
|---|---|---|
| FY27 revenue growth 40% (aspiration, hedged) | Raised to "at least 80%" (R-L700; P-L111). H1 consolidated growth +132.81% (R-L724). | RAISED; H1 delivery at the new guide's run-rate |
| Rs215 Cr DC facility, Sep-2027 | Absent from deck and PR. | NOT REAFFIRMED (disclosure dropped) |
| OFC 42.3/43, OF 33.9/34 mn fkm by Dec-2026 (undated on Q1 deck) | Deck: OF "Current: 28", OFC "Current: 39", both "Expanding by July 2028" (P-L428-434). | NOT REAFFIRMED; OF still at pre-expansion level |
| Preform 300 MT, Rs580 Cr, Jul-2029 | Now 600 MT, Rs1,250 Cr, "By October 2028" (P-L436-442). | REFRAMED (bigger, earlier) |
| MMHG Phase-1 Rs275 Cr, undated | "Rs230 Cr As Phase1" (P-L436-439). | REFRAMED (smaller), still undated |
| Aerospace acquisition proposed | "Expected to be completed during the current quarter" (R-L754). HASPL Rs90 Cr object missed 30-Sep, extended to 31-Dec-2026 (M-L1095-1108). Price not disclosed. | DELAYED (object deadline extended) |
| EBITDA margin 22-25% by FY29 | ">27% by FY29" (P-L503-504). | RAISED |
| Exports 60%+ FY27 onward | "65%+ from FY27 onwards" and "more than 70% ... by FY27" on one slide (P-L502-508). | RAISED; internally inconsistent (PPT-FN-06) |
| Promoter warrant 75% balance ~Rs412.5 Cr ~Nov-2027 | Rs416.25 Cr, 18 months from 25.05.2026; no Q2 receipt (M-L1056-1058). | ON TRACK (memory figure corrected) |
| Nivetti closure (now 31-Dec-2026) | Not named in any Q2 document. | SILENT |

Pattern [INFERENCE]: headline targets went up (revenue, margin, exports). Dated physical milestones went quiet (Dec-2026 capacity step, Rs215 Cr DC facility) or moved (HASPL object deadline). New qualitative claims carry no metric (secured raw materials PM02, value realization PM03, DC adjacency PM04 and M08). H1 numbers support the raised revenue headline. The dropped dates are promise-log entries for the operator. Slip-count treatment is operator-only.

Checkpoint (no wait): Notion fetched with Decision Status WATCHLIST verified; units Rs Crore (factor 1); share-count changes noted; all 10 notes and 3 auditor reliance paragraphs extracted; opinion unmodified; business type standard.

---

## STEP 1: DATA EXTRACTION TABLE (STANDARD BUSINESS)

Period columns: Q2 FY26 = Q[N] FY[YY-1]; Q1 FY27 = Q[N-1] FY[YY]; Q2 FY27 = Q[N] FY[YY]; FY26 = FY[YY-1]. FY27 is not complete, so the FY[YY] column is ND. H1 columns are added because Q2 is a half-year print. All values from R-L804 to R-L835 unless stated.

### 1A. CONSOLIDATED (Rs Cr)

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from Operations (R-L804) | 1,043.34 | 1,914.98 | 2,541.79 | 4,949.27 | ND | 1,914.36 | 4,456.77 |
| Other Income (R-L805) | 13.04 | 31.15 | 27.46 | 65.25 | ND | 27.57 | 58.61 |
| Total Income (R-L806) | 1,056.38 | 1,946.13 | 2,569.25 | 5,014.52 | ND | 1,941.93 | 4,515.38 |
| Cost of Materials/Services Consumed (R-L807) | 417.11 | 969.22 | 1,377.07 | 1,903.15 | ND | 864.91 | 2,346.29 |
| Purchases of Stock-in-Trade (R-L808) | 388.18 | 370.87 | 171.13 | 1,756.74 | ND | 607.56 | 542.00 |
| Change in Inventories (R-L809) | (161.02) | (168.54) | 21.47 | (457.98) | ND | (193.11) | (147.07) |
| Employee Benefits Expense (R-L810) | 94.24 | 147.06 | 130.34 | 445.26 | ND | 199.59 | 277.40 |
| Finance Costs (R-L811) | 60.90 | 62.48 | 65.34 | 242.06 | ND | 116.52 | 127.82 |
| Depreciation, Impairment, Amortisation (R-L812) | 35.93 | 51.25 | 53.72 | 157.38 | ND | 68.13 | 104.97 |
| Other Expenses (R-L813) | 114.50 | 182.25 | 211.24 | 540.60 | ND | 216.68 | 393.49 |
| Total Expenses (R-L814) | 949.84 | 1,614.59 | 2,030.31 | 4,587.21 | ND | 1,880.28 | 3,644.90 |
| Profit before JCE share and tax, line III (R-L815) | 106.54 | 331.54 | 538.94 | 427.31 | ND | 61.65 | 870.48 |
| Share of JCE profit/(loss) (R-L816) | (0.20) | (0.02) | (0.34) | 0.37 | ND | (0.01) | (0.36) |
| Exceptional items (R-L818) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | ND | 0.00 (nil) | 0.00 (nil) |
| Profit Before Tax (R-L819) | 106.34 | 331.52 | 538.60 | 427.68 | ND | 61.64 | 870.12 |
| Current tax (R-L820) | 5.03 | 91.42 | 151.87 | 104.35 | ND | 6.12 | 243.29 |
| Deferred tax (R-L821) | 29.39 | (5.54) | (7.49) | (6.11) | ND | 12.90 | (13.03) |
| Tax Expense [COMPUTED: current + deferred] | 34.42 | 85.88 | 144.38 | 98.24 | ND | 19.02 | 230.26 |
| PAT (R-L822) | 71.92 | 245.64 | 394.22 | 329.44 | ND | 42.62 | 639.86 |
| PAT to owners (R-L828) | 67.86 | 228.60 | 362.91 | 311.74 | ND | 35.62 | 591.51 |
| PAT to NCI (R-L829) | 4.05 | 17.04 | 31.30 | 17.70 | ND | 7.00 | 48.34 |
| OCI after tax (R-L826) | (7.79) | 72.16 | (13.57) | (29.12) | ND | 31.13 | 58.59 |
| EPS basic, Rs (R-L834) | 0.47 | 1.49 | 2.37 | 2.13 | ND | 0.25 | 3.86 |
| EPS diluted, Rs (R-L835) | 0.47 | 1.49 | 2.36 | 2.13 | ND | 0.25 | 3.85 |
| EPS (share-adjusted), Rs | 0.47 | 1.49 | 2.37 | 2.13 | ND | 0.25 | 3.86 |

Tie checks [COMPUTED]: Q2 FY27 PBT 538.60 less tax 144.38 = 394.22. Q1 331.52 less 85.88 = 245.64. Q2 FY26 106.34 less 34.42 = 71.92. Owners plus NCI: 362.91 + 31.30 = 394.21 (0.01 rounding).

### 1B. CONSOLIDATED DERIVED METRICS

Formula note: Operating EBITDA uses line III (profit before JCE share, R-L815), so the JCE equity result is stripped together with other income. Reported EBITDA uses PBT after JCE share (R-L819), per the protocol formula. The press release's EBITDA (658.00, R-L716) equals PBT + D + finance + JCE loss add-back, and it includes other income (RES-FN-26).

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | line III + D + FC - OI | 190.33 | 414.12 | 630.54 | 761.50 | ND | 218.73 | 1,044.66 |
| Operating EBITDA Margin | Op EBITDA / Rev | 18.24% | 21.63% | 24.81% | 15.39% | ND | 11.43% | 23.44% |
| Reported EBITDA | PBT + D + FC | 203.17 | 445.25 | 657.66 | 827.12 | ND | 246.29 | 1,102.91 |
| Reported EBITDA Margin | Rep EBITDA / Rev | 19.47% | 23.25% | 25.87% | 16.71% | ND | 12.87% | 24.75% |
| Press-release EBITDA (R-L716, R-L725) | as printed | 203.37 | 445.27 | 658.00 | ND | ND | 246.30 | 1,103.27 |
| Core PBT (ex-OI) | PBT - OI | 93.30 | 300.37 | 511.14 | 362.43 | ND | 34.07 | 811.51 |
| Other Income / PBT | OI / PBT | 12.26% | 9.40% | 5.10% | 15.26% | ND | 44.73% | 6.74% |
| Effective Tax Rate | Tax / PBT | 32.37% | 25.90% | 26.81% | 22.97% | ND | 30.86% | 26.46% |
| PAT Margin | PAT / Rev | 6.89% | 12.83% | 15.51% | 6.66% | ND | 2.23% | 14.36% |
| Gross margin | (Rev - materials - purchases - change in inventories) / Rev | 38.25% | 38.82% | 38.25% | 35.31% | ND | 33.17% | 38.49% |
| Employee cost / Rev | R-L810 / R-L804 | 9.03% | 7.68% | 5.13% | 9.00% | ND | 10.43% | 6.22% |
| Other expenses / Rev | R-L813 / R-L804 | 10.97% | 9.52% | 8.31% | 10.92% | ND | 11.32% | 8.83% |

Arithmetic shown for Q2 FY27 [COMPUTED]: Op EBITDA 538.94 + 53.72 + 65.34 - 27.46 = 630.54; 630.54 / 2,541.79 = 24.81%. Reported 538.60 + 53.72 + 65.34 = 657.66; 25.87%. Gross profit 2,541.79 - 1,377.07 - 171.13 - 21.47 = 972.12; 38.25%. FY26 gross profit 4,949.27 - 1,903.15 - 1,756.74 + 457.98 = 1,747.36; 35.31%. H1 FY27 gross profit 4,456.77 - 2,346.29 - 542.00 + 147.07 = 1,715.55; 38.49%. H1 FY26 1,914.36 - 864.91 - 607.56 + 193.11 = 635.00; 33.17%.

Operating vs reported (non-negotiable rule): Q2 FY27 operating EBITDA margin 24.81% (excluding other income); reported EBITDA margin 25.87% (including other income); press-release figure 25.89%.

### 1C. STANDALONE (Rs Cr)

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from Operations (R-L804) | 1,003.13 | 1,607.80 | 2,177.76 | 4,527.54 | ND | 1,792.41 | 3,785.56 |
| Other Income (R-L805) | 15.07 | 32.54 | 25.30 | 67.46 | ND | 29.16 | 57.84 |
| Total Income (R-L806) | 1,018.20 | 1,640.34 | 2,203.06 | 4,595.00 | ND | 1,821.57 | 3,843.40 |
| Cost of Materials/Services Consumed (R-L807) | 358.58 | 725.17 | 1,366.86 | 1,907.10 | ND | 781.17 | 2,092.03 |
| Purchases of Stock-in-Trade (R-L808) | 343.37 | 365.44 | 153.36 | 1,623.03 | ND | 578.14 | 518.80 |
| Change in Inventories (R-L809) | (19.03) | (40.93) | (21.66) | (406.94) | ND | (59.54) | (62.59) |
| Employee Benefits Expense (R-L810) | 70.30 | 110.80 | 86.56 | 340.91 | ND | 154.46 | 197.36 |
| Finance Costs (R-L811) | 52.97 | 53.21 | 56.33 | 209.97 | ND | 100.71 | 109.54 |
| Depreciation (R-L812) | 31.41 | 43.02 | 44.24 | 137.99 | ND | 59.55 | 87.26 |
| Other Expenses (R-L813) | 90.89 | 143.51 | 158.86 | 460.80 | ND | 180.26 | 302.37 |
| Total Expenses (R-L814) | 928.49 | 1,400.22 | 1,844.55 | 4,272.86 | ND | 1,794.75 | 3,244.77 |
| Exceptional items (R-L818) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | ND | 0.00 (nil) | 0.00 (nil) |
| Profit Before Tax (R-L819) | 89.71 | 240.12 | 358.51 | 322.14 | ND | 26.82 | 598.63 |
| Current tax (R-L820) | 0.00 (nil) | 65.27 | 97.12 | 79.82 | ND | 0.00 (nil) | 162.39 |
| Deferred tax (R-L821) | 28.27 | (4.36) | (6.63) | (10.55) | ND | 7.72 | (10.99) |
| Tax Expense [COMPUTED] | 28.27 | 60.91 | 90.49 | 69.27 | ND | 7.72 | 151.40 |
| PAT (R-L822) | 61.44 | 179.21 | 268.02 | 252.87 | ND | 19.10 | 447.23 |
| OCI after tax (R-L826) | (5.95) | 73.84 | (13.87) | (17.18) | ND | 33.60 | 59.97 |
| EPS basic, Rs (R-L834) | 0.42 | 1.17 | 1.75 | 1.72 | ND | 0.13 | 2.92 |
| EPS diluted, Rs (R-L835) | 0.42 | 1.17 | 1.74 | 1.72 | ND | 0.13 | 2.91 |
| EPS (share-adjusted), Rs | 0.42 | 1.17 | 1.75 | 1.72 | ND | 0.13 | 2.92 |

### 1D. STANDALONE DERIVED METRICS

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 159.02 | 303.81 | 433.78 | 602.64 | ND | 157.92 | 737.59 |
| Operating EBITDA Margin | / Rev | 15.85% | 18.90% | 19.92% | 13.31% | ND | 8.81% | 19.48% |
| Reported EBITDA | PBT + D + FC | 174.09 | 336.35 | 459.08 | 670.10 | ND | 187.08 | 795.43 |
| Reported EBITDA Margin | / Rev | 17.35% | 20.92% | 21.08% | 14.80% | ND | 10.44% | 21.01% |
| Core PBT (ex-OI) | PBT - OI | 74.64 | 207.58 | 333.21 | 254.68 | ND | (2.34) | 540.79 |
| Other Income / PBT | OI / PBT | 16.80% | 13.55% | 7.06% | 20.94% | ND | 108.72% | 9.66% |
| Effective Tax Rate | Tax / PBT | 31.51% | 25.37% | 25.24% | 21.50% | ND | 28.78% | 25.29% |
| PAT Margin | PAT / Rev | 6.12% | 11.15% | 12.31% | 5.59% | ND | 1.07% | 11.81% |
| Gross margin | as 1B | 31.92% | 34.71% | 31.19% | 31.02% | ND | 27.48% | 32.69% |

Arithmetic [COMPUTED]: Q2 FY27 op EBITDA 358.51 + 44.24 + 56.33 - 25.30 = 433.78. Standalone Q2 gross profit 2,177.76 - 1,366.86 - 153.36 + 21.66 = 679.20; 31.19%. Q1 1,607.80 - 725.17 - 365.44 + 40.93 = 558.12; 34.71%. FY26 4,527.54 - 1,907.10 - 1,623.03 + 406.94 = 1,404.35; 31.02%. H1 FY27 3,785.56 - 2,092.03 - 518.80 + 62.59 = 1,237.32; 32.69%. H1 FY26 1,792.41 - 781.17 - 578.14 + 59.54 = 492.64; 27.48%. Q2 FY26 1,003.13 - 358.58 - 343.37 + 19.03 = 320.21; 31.92%.

Note on parent margin (RES-FN-04): standalone gross margin fell 352 bps QoQ (34.71% to 31.19%) while consolidated held near 38.25%. The parent sells to subsidiaries; Rs1,543.70 Cr of subsidiary revenue was eliminated in Q2 (RES-FN-04). Profit is accruing below the parent.

Checkpoint (no wait): every cell filled or ND. FY27 full-year column ND because the year is not complete.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### 2A. Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY % change [COMPUTED] | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 1,043.34 | 2,541.79 | +143.62% (2,541.79 / 1,043.34 = 2.4362) | Strong |
| Operating EBITDA | 190.33 | 630.54 | +231.29% (630.54 / 190.33 = 3.3129) | Strong |
| Operating EBITDA Margin (pp) | 18.24% | 24.81% | +6.57 pp (+657 bps) | Expanded; gross margin flat, all from operating leverage |
| Depreciation | 35.93 | 53.72 | +49.51% | Slower than revenue; no absorption deficit yet |
| Finance Costs | 60.90 | 65.34 | +7.29% | Slower than revenue |
| EBIT (operating) = Op EBITDA - D | 154.40 | 576.82 | +273.59% | Strong |
| Other Income | 13.04 | 27.46 | +110.58% | Small share of PBT |
| Core Operating PBT (PBT - OI) | 93.30 | 511.14 | +447.85% (511.14 / 93.30 = 5.4785) | Strong; faster than reported PBT |
| Reported PBT | 106.34 | 538.60 | +406.49% | Strong |
| PAT | 71.92 | 394.22 | +448.14% | Strong |
| PAT to owners | 67.86 | 362.91 | +434.79% | Strong |
| EPS (share-adjusted, basic) | 0.47 | 2.37 | +404.26% | Below owner PAT growth because of +6.12% QIP share count |

### 2B. Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY % change [COMPUTED] | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 1,003.13 | 2,177.76 | +117.10% | Strong |
| Operating EBITDA | 159.02 | 433.78 | +172.78% | Strong |
| Operating EBITDA Margin (pp) | 15.85% | 19.92% | +4.07 pp (+407 bps) | Expanded; lower level than consolidated |
| Depreciation | 31.41 | 44.24 | +40.85% | Slower than revenue |
| Finance Costs | 52.97 | 56.33 | +6.34% | Slower than revenue |
| EBIT (operating) | 127.61 | 389.54 | +205.26% | Strong |
| Other Income | 15.07 | 25.30 | +67.88% | Small |
| Core Operating PBT (PBT - OI) | 74.64 | 333.21 | +346.42% | Strong |
| Reported PBT | 89.71 | 358.51 | +299.63% | Strong |
| PAT | 61.44 | 268.02 | +336.23% | Strong |
| EPS (share-adjusted, basic) | 0.42 | 1.75 | +316.67% | Strong |

### 2C. Segment result walk, consolidated (R-L839-848)

| Segment | Rev Q2 FY26 | Rev Q2 FY27 | Rev YoY | Result Q2 FY26 | Result Q2 FY27 | Result margin Q2 FY26 | Result margin Q2 FY27 | Result change |
|---|---|---|---|---|---|---|---|---|
| Telecom Products | 490.10 | 2,321.98 | +373.78% | 122.54 | 716.24 | 25.00% | 30.85% | +593.70 |
| Defence Products and Services | 29.73 | 54.94 | +84.80% | 1.86 | 3.45 | 6.26% | 6.28% | +1.59 |
| Turnkey Contracts and Services | 506.77 | 136.07 | -73.15% | 35.92 | (122.58) | 7.09% | -90.09% | (158.50) |
| Others | 16.74 | 28.80 | +72.04% | (0.03) | 3.13 | -0.18% | 10.87% | +3.16 |
| Total | 1,043.34 | 2,541.79 | +143.62% | 160.29 | 600.24 | 15.36% | 23.61% | +439.95 |

Telecom Products share of consolidated revenue: 91.35% [COMPUTED: 2,321.98 / 2,541.79]. Turnkey share: 5.35%. QoQ: Telecom revenue +46.08% (1,589.53 to 2,321.98), result margin 30.44% to 30.85%; Turnkey revenue -51.46% (280.32 to 136.07), result (87.53) to (122.58); Defence revenue 23.74 to 54.94, result (8.04) to 3.45.

### 2D. Six mandatory diagnostic answers

1. Did revenue grow YoY? Yes. Consolidated +143.62% (Q2 FY27 vs Q2 FY26). H1 +132.81% (R-L724). Against the old Notion base: FY27 revenue 6,200 implies +25.3% on FY26 4,949.27 [COMPUTED]; H1 runs far above it. Against the new company guide (at least 80%, R-L700): H1 is AT the guide on run-rate, not above it. H1 x 2 = 8,913.54 vs guide floor 8,908.69 [COMPUTED: 4,949.27 x 1.8]. The guide embeds sharp deceleration. It needs H2 FY27 revenue of 4,451.92 against H2 FY26 of 3,034.91, so H2 YoY growth of +46.69% [COMPUTED: 4,451.92 / 3,034.91] against +132.81% in H1. Q2 alone (2,541.79) runs above the guide's implied H2 pace of 2,225.96 a quarter.
2. Operating EBITDA margin: Q2 FY27 margin of 24.81% vs Q2 FY26 margin of 18.24% = +657 bps (operating basis). Reported basis: 25.87% vs 19.47% = +640 bps. Consolidated gross margin is flat YoY at 38.25% vs 38.25%. The full gain is operating leverage: employee cost fell from 9.03% to 5.13% of revenue (+390 bps), other expenses from 10.97% to 8.31% (+266 bps). By segment, Telecom Products carries it (result margin 25.00% to 30.85%), and the Turnkey loss drags it.
3. Did core operating PBT grow YoY? Yes. 93.30 to 511.14, +447.85%. Core PBT grew faster than reported PBT (+406.49%). The test passes at the consolidated operating level. The caveats sit in where the profit lands (47.09% outside the parent, Step 5C) and in cash (Step 5), not in the P&L arithmetic.
4. Gap between core PBT growth and PAT growth: PAT grew +448.14%, close to core PBT. Deltas [COMPUTED]: other income +14.42 pre-tax; finance cost (4.44); JCE share (0.14); depreciation (17.79); tax (109.96), of which tax at the prior ETR on incremental PBT is (139.91) and the ETR fall from 32.37% to 26.81% adds +29.95. No exceptional items. Detail in Step 4.
5. Are D&A and finance costs scaling faster than revenue? No. D&A +49.51% and finance +7.29% against revenue +143.62%. No absorption deficit today. Warning: the Rs1,800 Cr capex sits mostly in other non-current assets (+276.72 consolidated in H1, R-L905; read as capital advances [INFERENCE from the cash-flow label, R-L970]) and CWIP (+53.29, R-L895). D&A steps up when these commission (July to October 2028 per P-L432, P-L442). [INFERENCE] ROCE compresses then unless volume follows.
6. Is Other Income concentration changing? Falling. OI/PBT 12.26% (Q2 FY26) to 5.10% (Q2 FY27); H1 6.74% vs FY26 15.26%. Treasury income does not mask the trajectory. Note: Rs21.22 Cr of QIP FD is LC margin (M-L503) and Rs90 Cr warrant money sits in FD (R-L869); part of other income is interest on raised capital, not operations.

Standalone answers in brief: revenue +117.10%; operating margin 15.85% to 19.92% (+407 bps); core PBT +346.42%; standalone gross margin 31.92% to 31.19% (-73 bps YoY), so the parent's margin gain is also opex leverage. The consolidated operating margin is 489 bps above the standalone margin in Q2 (24.81% vs 19.92%); it was 239 bps above a year ago (18.24% vs 15.85%) [COMPUTED].

Checkpoint (no wait): YoY tables and six answers shown.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

Q3 FY26 and Q4 FY26 are not separately disclosed in this filing. The H2 FY26 pair is derived as FY26 less H1 FY26. Q1 FY26 is derived as H1 FY26 less Q2 FY26 [COMPUTED from R-L804-819].

### 3A. Consolidated

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI) | One-offs Flagged | QoQ Run-Rate |
|---|---|---|---|---|---|
| Q1 FY26 (derived) | 871.02 | 3.26% (Op EBITDA 28.40) | (59.23) | None in notes | Base |
| Q2 FY26 | 1,043.34 | 18.24% | 93.30 | None | +19.78% |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND |
| H2 FY26 combined (derived; Q3+Q4) | 3,034.91 (avg 1,517.46 a quarter) | 17.88% (Op EBITDA 542.77) | 328.36 | None in notes | avg +45.44% vs Q2 FY26 |
| Q1 FY27 | 1,914.98 | 21.63% | 300.37 | Q1 subsidiary inventory build ~127.61 at cost (RES-FN-06); Q1 consolidated OCI items not reclassified +74.49 pre-tax (R-L823), total OCI +72.16 after tax (R-L826), below PAT (RES-FN-17) | vs H2 FY26 avg +26.20% |
| Q2 FY27 | 2,541.79 | 24.81% | 511.14 | Seasonal employee cost fall, about 66 bps of margin (RES-FN-07); subsidiary inventory release ~43.13 at cost (RES-FN-06); Turnkey loss (122.58) | +32.73% |

Arithmetic [COMPUTED]: Q1 FY26 revenue 1,914.36 - 1,043.34 = 871.02; line III 61.65 - 106.54 = (44.89); D 68.13 - 35.93 = 32.20; FC 116.52 - 60.90 = 55.62; OI 27.57 - 13.04 = 14.53; Op EBITDA (44.89) + 32.20 + 55.62 - 14.53 = 28.40; core PBT (61.64 - 106.34) - 14.53 = (59.23). H2 FY26 revenue 4,949.27 - 1,914.36 = 3,034.91; line III 427.31 - 61.65 = 365.66; D 157.38 - 68.13 = 89.25; FC 242.06 - 116.52 = 125.54; OI 65.25 - 27.57 = 37.68; Op EBITDA 542.77; margin 17.88%; core PBT (427.68 - 61.64) - 37.68 = 328.36. Inventory release at cost: 21.47 consolidated less (21.66) standalone change in inventories (R-L809) = 43.13.

### 3B. Standalone

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI) | One-offs Flagged | QoQ Run-Rate |
|---|---|---|---|---|---|
| Q1 FY26 (derived) | 789.28 | -0.14% (Op EBITDA (1.10)) | (76.98) | None | Base |
| Q2 FY26 | 1,003.13 | 15.85% | 74.64 | None | +27.09% |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND |
| H2 FY26 combined (derived) | 2,735.13 (avg 1,367.57) | 16.26% (Op EBITDA 444.72) | 257.02 | None | avg +36.33% vs Q2 FY26 |
| Q1 FY27 | 1,607.80 | 18.90% | 207.58 | Standalone OCI items not reclassified +74.24 (R-L823), below PAT | vs H2 FY26 avg +17.57% |
| Q2 FY27 | 2,177.76 | 19.92% | 333.21 | Seasonal employee fall 24.24 (-21.9% QoQ, RES-FN-07) | +35.45% |

Arithmetic [COMPUTED]: Q1 FY26 standalone revenue 1,792.41 - 1,003.13 = 789.28; PBT 26.82 - 89.71 = (62.89); D 59.55 - 31.41 = 28.14; FC 100.71 - 52.97 = 47.74; OI 29.16 - 15.07 = 14.09; Op EBITDA (62.89) + 28.14 + 47.74 - 14.09 = (1.10); margin -0.14%; core PBT (62.89) - 14.09 = (76.98). H2 FY26: revenue 4,527.54 - 1,792.41 = 2,735.13; PBT 322.14 - 26.82 = 295.32; D 137.99 - 59.55 = 78.44; FC 209.97 - 100.71 = 109.26; OI 67.46 - 29.16 = 38.30; Op EBITDA 295.32 + 78.44 + 109.26 - 38.30 = 444.72; margin 16.26%; core PBT 295.32 - 38.30 = 257.02.

### 3C. Diagnostics

- Trajectory: STEPPING UP on both bases. Consolidated revenue rose at every reading: Q1 FY26 871.02, Q2 FY26 1,043.34, H2 FY26 average 1,517.46, Q1 FY27 1,914.98, Q2 FY27 2,541.79. Operating margin rose at each step from Q2 FY26.
- Distortions: Q2 FY27 carries two favourable one-offs and one unfavourable item. Seasonal employee cost (about 66 bps of margin, RES-FN-07). Subsidiary finished-goods and WIP release of about 43.13 at cost after a Q1 build of about 127.61 at cost (RES-FN-06), so part of the Q2 revenue jump is stock built in Q1. Turnkey loss deepened to (122.58). No exceptional item in any column.
- Latest quarter vs H1 average: Q2 consolidated revenue 2,541.79 is +14.06% above the H1 average 2,228.39 [COMPUTED: 4,456.77 / 2]. Capex commissioning test: not yet applicable. Capex is in advances and CWIP. The QIP OFC capex object (Rs35 Cr) completed in Q2 (MA-FN-14, M-L242-246). Capacity is unchanged at OF 28 and OFC 39 mn fkm "Current" (P-L434).
- Implied Q3 base: to maintain trajectory, Q3 consolidated revenue at or above 2,541.79. The company guide on the consolidated basis needs only 2,225.96 a quarter in H2 (RES-FN-10): 4,949.27 x 1.8 = 8,908.69; less H1 4,456.77 = 4,451.92; / 2 = 2,225.96, which is 12.43% below Q2. On the standalone basis the guide needs 2,182.01 a quarter, about equal to the standalone Q2 run rate (2,177.76). The basis is unstated. The two readings differ by whether H2 may fall.

Checkpoint (no wait): QoQ tables and diagnostics shown.

---

## STEP 4: OPERATIONAL DECOMPOSITION: PAT BRIDGE (consolidated, Q2 FY27 vs Q2 FY26)

| Component | YoY Change (Rs Cr) | Share of PAT change (%) | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (delta revenue 1,498.45 x prior gross margin 38.249%) | +573.15 | 177.8% | Recurring |
| Margin change contribution (gross margin 38.249% to 38.245% on Q2 FY27 revenue) | (0.10) | 0.0% | Recurring |
| Operating cost change (employee +36.10, other expenses +96.74) | (132.84) | -41.2% | Recurring |
| = Operating EBITDA change (check: 630.54 - 190.33) | +440.21 | 136.6% | Recurring |
| D&A change | (17.79) | -5.5% | Recurring (post-capex; rises when capex commissions) |
| Finance cost change | (4.44) | -1.4% | Recurring (post-debt) |
| Other Income change | +14.42 | 4.5% | NON-RECURRING typically (part is interest on issue proceeds) |
| JCE share change | (0.14) | 0.0% | Mixed |
| = PBT change (check: 538.60 - 106.34) | +432.26 | 134.1% | |
| Tax on incremental PBT at prior ETR 32.368% | (139.91) | -43.4% | Recurring |
| Effective tax rate change (32.37% to 26.81% on Q2 FY27 PBT) | +29.95 | 9.3% | Mixed (prior-year deferred charge 29.39 vs current credit 7.49) |
| Exceptional items | 0.00 | 0.0% | NON-RECURRING (nil both periods) |
| **Reported PAT YoY change (check: 394.22 - 71.92)** | **+322.30** | **100.0%** | |

Arithmetic [COMPUTED]: prior gross margin 399.07 / 1,043.34 = 0.382493; 1,498.45 x 0.382493 = 573.15. Q2 FY27 gross profit 972.12 = 399.07 + 573.15 - 0.10. Tax at prior ETR: 432.26 x 0.32368 = 139.91. ETR effect: 538.60 x 0.32368 = 174.33 less actual 144.38 = 29.95. Sum: 573.15 - 0.10 - 132.84 - 17.79 - 4.44 + 14.42 - 0.14 - 139.91 + 29.95 = 322.30.

Mandatory questions:
1. Recurring vs non-recurring share of PAT change: other income after tax at the Q2 ETR is about 10.55 (14.42 x (1 - 0.2681)), or 3.3% of the change. The ETR fall adds 29.95 (9.3%). The remaining 281.80 (87.4%) comes from core operations [COMPUTED]. The PAT change is mostly recurring operating gain on the P&L. Cash backing is weaker (Step 5).
2. If Other Income reverts to the prior-year level (13.04): PBT falls 14.42; PAT falls about 10.55 to about 383.67 [COMPUTED]. Run-rate PAT holds near Rs384 Cr a quarter on Q2 operations.
3. D&A and finance costs at steady state? No. D&A is ramping (Q2 FY26 35.93, Q1 51.25, Q2 53.72) and will step up again when the Rs1,800 Cr programme commissions (July-October 2028, P-L432, P-L442). Gross borrowings rose 126.76 in H1 (Step 5). Finance cost will rise as capex draws debt (RES-FN-14). Steady state is not reached; the filing gives no capex phasing, so the steady-state D&A is ND.
4. Tax adjustments: deferred tax credits of (7.49) consolidated and (6.63) standalone in Q2 lower the ETR by 139 bps and 185 bps (RES-FN-16). The current-tax-only rate is 28.20% consolidated and 27.09% standalone. If the credits stop, PAT falls about 7.49 a quarter [COMPUTED]. In Q2 FY26 a deferred charge of 29.39 lifted the prior ETR to 32.37%; that flatters the YoY PAT comparison by the 29.95 ETR effect. Cash tax lags the P&L charge in H1 (Step 5A, tax-accrual rows).

Segment view of the same bridge (2C): Telecom result +593.70 and Turnkey (158.50). Without the Turnkey swing, segment result growth would be +598.45 [COMPUTED: 439.95 + 158.50]. The Turnkey loss is the single largest drag on reported PAT.

Standalone bridge in brief [COMPUTED]: PAT change +206.58 (268.02 - 61.44). Op EBITDA +274.76; D&A (12.83); finance (3.36); OI +10.23; PBT +268.80; tax (62.22), of which the ETR fall from 31.51% to 25.24% adds +22.49 (358.51 x 0.31513 = 112.98, less actual 90.49).

Checkpoint (no wait): bridge and answers shown.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 actuals at Q2, Reg 33 half-yearly statements)

### 5A. Consolidated (CF R-L942-991; BS R-L894-938)

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (H1), reported | (43.60) H1 FY26 | 455.27 H1 FY27 | +498.87 | Positive; first positive half since FY26 CFO (378.13) [MEMORY] |
| Current tax charged (R-L820) vs income taxes paid (R-L966) | charged 6.12; paid 17.09 | charged 243.29; paid 119.89 | unpaid in H1 FY27: 123.40 | H1 FY27 CFO carries 123.40 of current tax charged but not yet paid. In H1 FY26 tax paid exceeded the charge by 10.97, so the YoY swing is flattered too |
| Current tax liabilities (net) (R-L933) / current tax assets (R-L914) | 59.99 / 12.75 (31-Mar-26) | 194.03 / 23.38 | +134.04 / +10.63; net +123.41 | Balance sheet ties to the unpaid 123.40 |
| CFO with tax counted when charged [COMPUTED: CFO + tax paid - current tax charged] | (32.63) [-43.60 + 17.09 - 6.12] | 331.87 [455.27 + 119.89 - 243.29] | +364.50 | Cash reading if tax were paid as it accrues |
| CFO/PAT ratio (H1), reported | (1.02) [-43.60 / 42.62] | 0.71 [455.27 / 639.86] | +1.73 | Between the 0.65 and 0.80 band markers |
| CFO/PAT ratio (H1), tax counted when charged | (0.77) [-32.63 / 42.62] | 0.52 [331.87 / 639.86] | +1.29 | BELOW the 0.65 marker |
| Capex (payments for PPE incl. CWIP and capital advances, R-L970, + intangibles, R-L971) | 197.20 (133.74 + 63.46) | 449.15 (436.27 + 12.88) | +251.95 | Front-loaded; other non-current assets +276.72 (R-L905), read as capital advances [INFERENCE from the R-L970 label] |
| FCF (CFO - Capex), reported | (240.80) | 6.12 | +246.92 | About breakeven |
| FCF, tax counted when charged | (229.83) [-32.63 - 197.20] | (117.28) [331.87 - 449.15] | +112.55 | Negative |
| Working capital change (CF statement) | (266.66) | (509.11) | (242.45) | WC absorbed 79.6% of PAT [COMPUTED: 509.11 / 639.86]. Receivables (403.61), inventories (127.99), other current assets (317.30) absorbed 848.90; payables +178.51, other financial assets +109.43, other current liabilities +138.77 offset 426.71 (R-L954-963) |
| Receivable days (total receivables incl. non-current, on TTM revenue) | 183.04 (31-Mar-26: 2,481.98 / 4,949.27 x 365) | 140.78 (30-Sep-26: 2,889.58 / 7,491.68 x 365) | -42.26 days | Improving; above Notion red line 130 on this basis |
| Receivable days (current receivables only, TTM) | 163.14 (2,212.18 / 4,949.27 x 365) | 128.14 (2,630.03 / 7,491.68 x 365) | -35.00 days | Matches Notion's FY26 ~163 basis; between green 110 and red 130 |
| TR / TTM revenue (total) | 50.15% | 38.57% | -11.58 pp | Inside Notion green (<=45%) |
| Inventory days (on TTM COGS) | 161.41 (1,415.99 / 3,201.91 x 365) | 120.84 (1,543.98 / 4,663.77 x 365) | -40.57 days | Improving |
| Payable days (on TTM COGS) | 114.84 (1,007.44 / 3,201.91 x 365) | 92.82 (1,185.95 / 4,663.77 x 365) | -22.02 days | Fewer supplier days |
| Cash Conversion Cycle (total receivables basis) | 229.61 | 168.80 | -60.81 days | Improving, still long |
| Other current assets (R-L915) | 1,830.65 | 2,147.96 | +317.31 | UNEXPLAINED; may hold unbilled/contract assets (RES-FN-05) |
| PPE (R-L894) | 913.36 | 941.34 | +27.98 | Little commissioned |
| CWIP (R-L895) | 85.01 | 138.30 | +53.29 | Building |
| Other non-current assets (R-L905) | 46.77 | 323.49 | +276.72 | Capex advances [INFERENCE from R-L970 label] |
| Intangibles under development (R-L899) | 401.29 | 407.53 | +6.24 | Stalled build (RES-FN-23) |
| Gross borrowings (NC R-L923 + current R-L928) | 1,713.37 | 1,840.13 | +126.76 | Up |
| Operational buyers' credit (R-L930) | 151.95 | 69.43 | (82.52) | Down |
| Cash + other bank balances (R-L910, R-L911) | 468.42 (37.67 + 430.75) | 594.76 (184.97 + 409.79) | +126.34 | Part is restricted (LC margin, issue-proceed FDs) |
| Net Debt A (borrowings - cash - other bank balances) | 1,244.95 | 1,245.37 | +0.42 | Flat |
| Net Debt B (A + operational buyers' credit) | 1,396.90 | 1,314.80 | (82.10) | Down |
| Promoter Pledge | ND (not disclosed) | ND (not disclosed; holding 28.29%, P-L569) | ND | UNKNOWN |

TTM bases [COMPUTED]: TTM revenue = FY26 4,949.27 - H1 FY26 1,914.36 + H1 FY27 4,456.77 = 7,491.68. COGS = materials + purchases + change in inventories. FY26 COGS 1,903.15 + 1,756.74 - 457.98 = 3,201.91. H1 FY26 COGS 864.91 + 607.56 - 193.11 = 1,279.36. H1 FY27 COGS 2,346.29 + 542.00 - 147.07 = 2,741.22. TTM COGS = 3,201.91 - 1,279.36 + 2,741.22 = 4,663.77. Total receivables at 30-Sep = 2,630.03 + 259.55 = 2,889.58; at 31-Mar = 2,212.18 + 269.80 = 2,481.98.

Basis caution: TTM days understate run-rate improvement when revenue grows fast, and they overstate days if Q2 revenue was lumpy. On an H1-annualised basis, current receivable days are about 108.00 [COMPUTED: 2,630.03 / 4,456.77 x 183]. The TTM basis is the conservative reading and is used for verdicts.

Tax-timing note: the 123.40 unpaid at 30-Sep (R-L933) falls due under the remaining advance-tax instalments by year-end [INFERENCE]. The timing benefit is expected to reverse in H2 FY27. That is a specific, filed driver for a weaker H2 CFO.

### 5B. Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (H1), reported | (72.59) | 238.07 | +310.66 | Positive |
| Current tax charged (R-L820) vs paid (R-L966) | charged nil; paid 16.50 | charged 162.39; paid 60.05 | unpaid 102.34 | Balance sheet: current tax liabilities 47.05 to 154.03 (+106.98), current tax assets 8.61 to 13.24 (+4.63); net +102.35 (R-L933, R-L914) |
| CFO with tax counted when charged [COMPUTED] | (56.09) [-72.59 + 16.50 - 0.00] | 135.73 [238.07 + 60.05 - 162.39] | +191.82 | |
| CFO/PAT ratio (H1), reported | (3.80) [-72.59 / 19.10] | 0.53 [238.07 / 447.23] | +4.33 | Below the 0.65 marker |
| CFO/PAT ratio (H1), tax counted when charged | (2.94) [-56.09 / 19.10] | 0.30 [135.73 / 447.23] | +3.24 | Well below the 0.65 marker |
| Capex (PPE incl. CWIP and advances + intangibles) | 176.50 (113.05 + 63.45) | 393.82 (381.22 + 12.60) | +217.32 | Most group capex is in the parent |
| FCF (CFO - Capex), reported | (249.09) | (155.75) | +93.34 | Negative |
| FCF, tax counted when charged | (232.59) [-56.09 - 176.50] | (258.09) [135.73 - 393.82] | (25.50) | Negative |
| Working capital change | (229.64) | (475.59) | (245.95) | Receivables (507.84) the main drain (R-L954) |
| Receivable days (total, TTM) | 167.88 (2,082.40 / 4,527.54 x 365) | 143.38 (2,561.51 / 6,520.69 x 365) | -24.50 days | Improving, above 130 |
| Inventory days (TTM COGS) | 136.31 (1,166.33 / 3,123.19 x 365) | 103.49 (1,239.53 / 4,371.66 x 365) | -32.82 days | Improving |
| Payable days (TTM COGS) | 107.98 (923.96 / 3,123.19 x 365) | 105.24 (1,260.50 / 4,371.66 x 365) | -2.74 days | Flat |
| Cash Conversion Cycle | 196.21 | 141.63 | -54.58 days | Improving |
| PPE | 730.49 | 720.63 | (9.86) | Flat |
| CWIP | 55.83 | 103.88 | +48.05 | Building |
| Other non-current assets (advances, [INFERENCE]) | 20.54 | 292.74 | +272.20 | Capex sits here |
| Gross borrowings | 1,489.02 (334.52 + 1,154.50) | 1,696.95 (593.94 + 1,103.01) | +207.93 | Up; long-term share up |
| Net Debt A | 1,087.34 (1,489.02 - 17.44 - 384.24) | 1,257.45 (1,696.95 - 128.66 - 310.84) | +170.11 | Up |
| Net Debt B (incl. buyers' credit 147.65 / 63.40) | 1,234.99 | 1,320.85 | +85.86 | Up |
| Promoter Pledge | ND | ND | ND | UNKNOWN |

TTM standalone [COMPUTED]: revenue 4,527.54 - 1,792.41 + 3,785.56 = 6,520.69. COGS FY26 3,123.19; H1 FY26 1,299.77; H1 FY27 2,548.24; TTM 4,371.66. Total standalone receivables: 30-Sep 2,301.96 + 259.55 = 2,561.51; 31-Mar 1,812.60 + 269.80 = 2,082.40.

### 5C. Standalone vs consolidated gap (first-class metric, from RES-FN-04 / F2)

| Period | Standalone PAT | Consolidated PAT | Gap (C - S) | Gap % of standalone PAT | Owners' PAT gap % [(owners - S) / S] |
|---|---|---|---|---|---|
| Q2 FY26 | 61.44 | 71.92 | 10.48 | 17.06% | 10.45% |
| Q1 FY27 | 179.21 | 245.64 | 66.43 | 37.07% | 27.56% |
| Q2 FY27 | 268.02 | 394.22 | 126.20 | 47.09% | 35.40% |
| H1 FY26 | 19.10 | 42.62 | 23.52 | 123.14% | 86.49% |
| H1 FY27 | 447.23 | 639.86 | 192.63 | 43.07% | 32.26% |
| FY26 | 252.87 | 329.44 | 76.57 | 30.28% | 23.28% |

Other gaps, Q2 FY27 [COMPUTED]: revenue gap 364.03 (16.72% of standalone); PBT gap 180.09 (50.23%); operating EBITDA margin gap +489 bps; CFO gap H1 217.20 (91.23% of standalone CFO).

Reading: the gap rose +10.0 pp QoQ and +30.0 pp YoY. It crosses the 5 pp test (RES-FN-04). Q2 subsidiary pools: para 7 four subsidiaries NPAT 123.40 (31.30% of group PAT); para 8 foreign subsidiaries 24.68; para 6 shells (0.17); JCE (0.34); consolidation adjustments (21.37). NCI took 31.30 (7.94% of PAT), which can only come from HTL Limited or Raddef (R-L872-873). The Notion Q1 figure for the para 7-8 share (46.9%) differs from the H1-less-Q2 derived Q1 figure (34.3%); the two cannot be reconciled without the Q1 fulltext (RES method note).

Subsidiary cash (RES-FN-28, M07): the four para 7 subsidiaries earned H1 NPAT 186.19 (R-L236), and their cash and cash equivalents fell 0.29 in H1 (R-L238). The filed figure is the net change in cash after investing and financing flows. Their operating cash flow is NOT FOUND, so how much of the profit became cash is not known. The para 8 foreign subsidiaries' cash rose 36.24 (R-L248-249); the shells' rose 0.14 (R-L223). The three sum to +36.09, which ties within 0.01 to the group-minus-parent change in cash of 36.08 [COMPUTED: 147.30 - 111.22, R-L989]. The parent received no dividends (R-L975). At the non-parent level, H1 cash also went to visible uses [COMPUTED, consolidated less standalone]: net bank deposits placed 52.33 (R-L974); net external borrowings repaid 80.69 (R-L980-981); capex 55.33 (R-L970-971). The filing does not split these uses among the para 6, 7 and 8 entities. Three readings fit:
- Reading A: the para 7 profit sits as a receivable from the parent (standalone trade payables exceed consolidated by 74.55, R-L931).
- Reading B: the subsidiaries spent it on their own working capital.
- Reading C: the subsidiaries converted the profit to cash and then placed deposits, repaid debt or spent on capex.
Separating observation: the para 7 subsidiaries' own CFO and their intra-group receivable from HFCL (Q36).

### 5D. Mandatory questions

1. Is CFO/PAT meeting the Pillar 2 assumption? The Notion cash multiplier is 0.85x, built on a 4-year CFO/PAT of 0.18 [MEMORY]. Two readings for H1 FY27:
   - Reported: consolidated 0.71 (between the 0.65 and 0.80 markers); standalone 0.53.
   - Tax counted when charged: consolidated 0.52 and standalone 0.30, both BELOW the 0.65 marker. H1 CFO carries 123.40 (consolidated) and 102.34 (standalone) of current tax charged but unpaid (R-L820, R-L966, R-L933). On this basis the YoY CFO swing is +364.50, against +498.87 reported.
   PILLAR FLAG (Pillar 2): both readings sit above the 4-year 0.18 history; only the reported reading clears 0.65. One half-year only. Recompute deferred to /fttcp and Role 1, which must carry both readings.
2. Is the WC drag structural or growth-induced? Test: if growth stopped, would days stay high? Evidence for growth-induced: receivable days fell 42.26 (total) and inventory days fell 40.57 on the conservative TTM basis while revenue doubled; TR/TTM fell to 38.57%. Evidence against: (a) other current assets rose 317.31 and are not broken out (RES-FN-05); (b) receivable ageing is undisclosed, and FY26 had Rs488 Cr over 6 months and Rs127 Cr over 3 years [MEMORY]; (c) receivable days on the total basis (140.78) are still above the Notion red line of 130; (d) the parent pledges issue proceeds as LC margin (MA-FN-09) and moved QIP money into its cash-credit account (MA-FN-05); (e) Turnkey net capital rose to 2,545.16 while revenue fell (RES-FN-19); (f) part of H1 CFO is unpaid current tax (123.40), not working-capital release; (g) the para 7 subsidiaries' cash balances fell 0.29 and their operating cash flow is NOT FOUND (RES-FN-28). No CARE structural-WC view is in the inputs. Classification: INDETERMINATE-WITH-DIRECTION (improving on days; weaker on the tax-accrual reading). Missing evidence named: receivable ageing at 30-Sep-2026; unbilled/contract-asset breakup of other current assets; full-year FY27 CFO after H2 advance tax; para 7 subsidiary CFO; any CARE commentary on WC. House rule: this caps the verdict at PROCEED WITH CAVEATS or lower.
3. Did CWIP capitalise as expected? No major commissioning was due in H1 on filed evidence. PPE +27.98, CWIP +53.29, other non-current assets +276.72 (consolidated). The Dec-2026 interim capacity step [MEMORY] is not reaffirmed in the deck (PPT-FN-10). Rs capitalised in H1: ND (no capitalisation figure in the filing).
4. Did net debt move within the projected range? Notion FY27 estimate is 1,800 [MEMORY], basis not stated. Gross borrowings 1,840.13 sit at that level; Net Debt A 1,245.37 sits well below it. The Notion basis is unknown, so the comparison is basis-uncertain. Gross borrowings rose 126.76 in H1 while the Rs416.25 Cr warrant balance is still unpaid. On the tax-accrual reading H1 FCF is (117.28), so borrowing funded part of the half. [INFERENCE] More debt is likely as capex advances turn into assets (RES-FN-14).

Cash conversion classification for this review: INDETERMINATE-WITH-DIRECTION. It does not resolve to PROCEED.

Checkpoint (no wait): cash-quality tables and answers shown.


---

# PART 2: STEP 5.5 TO CLOSING YAML (Loop 2 revision)

Part 1 (preamble, Steps 0-5) precedes this part in the same document. Anchor convention as in Part 1 (R-L results fulltext, P-L presentation fulltext, M-L MA report fulltext, [MEMORY] Notion brief, [COMPUTED], [INFERENCE]). Ledger rows M01-M08 and PM01-PM07 are cited by ID.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull

Tracker rows were NOT supplied to this run. The orchestrator passed the Notion thesis brief only. No Downstream Signal Tracker query result is in the inputs.

| Signal Name | Type | Cadence | Latest Observation Date and Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied) | ND | ND | ND | ND | ND | ND |

Flag: the count of tracker signals for HFCL is unknown. The protocol's "fewer than three signals" test cannot run. OR-17 needs three EXTERNAL tracker signals per entity at the /fttcp Role 5.5 gate. The operator or Claude web must pull the rows before /fttcp.

### 5.5B. Target reported vs signals

Target reported: STRONG on the P&L (consolidated revenue +143.62% YoY, core PBT +447.85% YoY; Part 1 Step 2).
Signals said: ND.
Matrix outcome: cannot be assigned. The quarter stands as one data point without signal cross-check.

### 5.5C. New signals surfaced

No new signal is written by this run (writes go only through the operator-approval gate). Candidate payload rows for operator review:
1. Aerospace target's export order book: "confirmed unexecuted export order book of Rs.~1,600 crores through proposed aerospace business being acquired" (P-L534-536). Customer unnamed. Case B candidate (new dependency) once the target is named.
2. International hyperscaler and telecom operator conversions: "Opportunities with international hyperscalers and telecom operators are steadily converting into firm contracts" (R-L742). Customer unnamed. Case A candidate against any existing hyperscaler capex row.

### 5.5D. Feed to Step 6

No signal-weighted override. Step 6 rests on the single-quarter print, with that limit stated.

---

## ROLE 5: CONCALL ANALYSIS (pending Role 5 addendum)

The 19-Oct-2026 concall (16:30 IST, Nuvama; Nahata, V.R. Jain, Baid, Amit Agarwal [MEMORY]) transcript is still being produced. These sections are pending the Role 5 addendum:
- Q&A extraction, management numbers and commitment register from the call: pending Role 5 addendum.
- Silence audit against the Notion checklist (F17): pending Role 5 addendum. This decides tripwire #4 (Step 6C).
- Re-marking of the 15 Q1 questions (Part 1 Step 0F) and the 42 Q2 questions below as ANSWERED / PARTIALLY / EVADED / NOT ADDRESSED: pending Role 5 addendum.
- Role 5 Step 8D: deferred to /fttcp and Role 1 (OR-30).
- Promise-vs-delivery tracker update for the Q1 seed log: the filing-level scoring is in Part 1 Step 0G; the call-level scoring is pending Role 5 addendum.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections (FY27, consolidated)

The Notion page carries FY27 Base only. FY27 Bear and Bull are not on the page.

| Metric | Bear Proj | Base Proj [MEMORY] | Bull Proj | Actual (anchored) | Lands In |
|---|---|---|---|---|---|
| Revenue (FY27) | ND | 6,200 (alt. builds 6,400 and 6,850-7,050) | ND | H1 4,456.77 (R-L804) = 71.9% of base in six months; H1 x 2 = 8,913.54, equal to the company guide floor 8,908.69 [COMPUTED: 4,949.27 x 1.8]; guide implies H2 YoY +46.69% vs H1 +132.81% | ABOVE BASE; AT GUIDE on run-rate |
| EBITDA Margin | ND | 17.5% (Notion FY26 16.7% matches reported basis incl. OI, 16.71%) | ND | H1 reported 24.75%; H1 operating 23.44% (Part 1 1B) | ABOVE BASE (both bases) |
| PAT | ND | 520 | ND | H1 639.86 (R-L822) = 123.0% of full-year base | ABOVE BASE |
| EPS | ND | 3.15 | ND | H1 basic 3.86 (R-L834) | ABOVE BASE |
| Net Debt | ND | 1,800 (basis unstated) | ND | Gross borrowings 1,840.13; Net Debt A 1,245.37; Net Debt B 1,314.80 (Part 1 5A) | AT BASE (gross) / BETTER (net); basis uncertain |
| ROCE | ND | 12.5% | ND | H1 annualised pre-tax ROCE 28.0% incl. OI, 26.35% ex-OI [COMPUTED: (870.12 + 127.82) x 2 = 1,995.88 / average capital employed 7,128.77 (Sep 5,755.44 + 1,840.13; Mar 4,948.59 + 1,713.37)] | ABOVE BASE (spot reading; not a Pillar 1 input) |

Longer-dated cross-check: TTM basic EPS = 2.13 - 0.25 + 3.86 = Rs5.74 [COMPUTED from R-L834]. That is 92.7% of the Notion FY29 base EPS Rs6.19. The Notion projections are stale on the upside against the old base. Against the new guide, H1 is on pace, not ahead. PILLAR FLAG for /fttcp and Role 1.

Probability re-weighting rule: NOT triggered. No metric lands below bear.

### 6B. Watchlist item status (every Notion checklist item, scored against filings)

| # | Watchlist Item [MEMORY] | Green Threshold | Red Threshold | This Quarter Reading (anchored) | Status |
|---|---|---|---|---|---|
| G1 | Q2 revenue gate (13-Oct) | about Rs2,000 Cr or more | below about Rs2,000 Cr | 2,541.79 (R-L804) | GREEN |
| G2 | EPC losses vs guide Rs80-90 Cr a quarter [MEMORY, broker] | loss at or below 80-90 | loss above band | Turnkey result (122.58) (R-L846); 32.58 to 42.58 above band | RED |
| G3 | Cash conversion, first CFO since FY26 (378.13) | CFO positive | CFO negative | H1 CFO 455.27 reported (R-L967), CFO/PAT 0.71; with tax counted when charged CFO 331.87, CFO/PAT 0.52 (Part 1 5A) | GREEN on the threshold (positive on both readings); quality qualifier: tax-accrual reading below 0.65 |
| G4 | Tripwire #4 second-quarter receivables test | ageing and unbilled disclosed; no unexplained unbilled rise above Rs200 Cr | second silent quarter, or unexplained unbilled rise above Rs200 Cr | Ageing, DSO, unbilled not disclosed in results, PR or deck (PPT-FN-12). Other current assets +317.31 consolidated, unlabelled (R-L915; RES-FN-05). Call pending | AMBER (pending Role 5 addendum; at risk) |
| G5 | Export-OFC revenue, cleanest metric | at or above 1,800 a quarter | below 1,200 a quarter | Not disclosed. Exports "63% of revenues" (P-L507), base period unstated; if Q2 base, 1,601.33 total exports, all products [COMPUTED: 0.63 x 2,541.79] | UNKNOWN |
| 1 | Hyperscaler pace | export OFC at or above 1,800 a quarter | below 1,200 a quarter, hedging or demurrage | As G5 | UNKNOWN |
| 2 | Receivables ageing | DSO at or below 110d, TR/TTM at or below 45%, over-6m below 15% | DSO above 130d, TR/TTM above 55%, over-6m above 25%, deferral | DSO 140.78 (total, TTM) / 128.14 (current only); TR/TTM 38.57%; ageing ND (Part 1 5A) | AMBER (mixed; ageing undisclosed) |
| 3 | Telecom product PBT margin | at or above 17% | below 14% two quarters | Segment result margin 30.85% consolidated, 26.70% standalone (R-L839, R-L844). Basis: segment result before interest | GREEN |
| 4 | Defence delivery | fuze approval by Q2 FY27; MMHG tender won; BMP-2 sample accepted | fuze fails third trial; MMHG to MIL; BMP-2 rejected | No fuze approval stated; MMHG named as product and Rs230 Cr Phase-1 facility (P-L436-439); "serial production commences on the back of receipt of multiple Indian defence contracts" (P-L538-544), contracts unnamed; BMP-2 silent | AMBER (green deadline passed without the event; no red event filed) |
| 5 | Promoter holding and pledge | at or above 28%, zero pledge | below 26% or any pledge | Holding 28.29% (P-L569); pledge not disclosed | GREEN holding / UNKNOWN pledge |
| 6 | BharatNet III revenue and WC absorption | EPC + O&M ramp visible; receivables not outpacing | hidden in "other"; receivables outpace | BharatNet not named in results; deck "Actively catering to Domestic telcos and Bharatnet for rapid roll out" (PM07, P-L537-538) with no figure, beside "deliberately shifting from low-profit turnkey work" (P-L514-515) (PPT-FN-21); Turnkey revenue 136.07 (-51.46% QoQ); Turnkey net capital 2,477.30 to 2,545.16 [COMPUTED from R-L855, R-L861] | RED |
| 7 | BharatNet III PBT margin | at or above 7% | vague or below 5% | Turnkey result margin -90.09% (R-L841, R-L846) | RED |
| 8 | Mobilisation and LC terms | mobilisation at or above 7%, LC at or above 40% | none, pure receivable | Not disclosed | UNKNOWN |
| 9 | Nivetti closure | closed by 30-Sep-2026 | second extension, lower consideration, or silence past 15-Oct | [MEMORY] SPA addendum 1-Oct-2026 moved completion to 31-Dec-2026. Q2 documents do not name Nivetti. HASPL Rs90 Cr object also moved 30-Sep to 31-Dec-2026 (M-L1095-1108) | RED (memory event; filings silent past 15-Oct) |
| 10 | 10-Jul export order: incremental vs second customer | incremental | same customer re-papered | Not disclosed | UNKNOWN |
| 11 | Contract PBT | at or above 8% | below 6% | Not disclosed by contract | UNKNOWN |
| 12 | Payment terms | LC at or above 50% | below | Not disclosed | UNKNOWN |
| 13 | Dec-2026 execution | on schedule | slip | Not disclosed | UNKNOWN |
| AR-1 | Turnkey segment PBIT recovery | loss narrowing | loss widening | (87.53) to (122.58); H1 (210.11) exceeds FY26 full-year (113.01) (R-L846) | RED |
| AR-2 | CFO turning positive | positive | negative | 455.27 reported; 331.87 with tax counted when charged | GREEN (positive on both readings) |
| AR-3 | Receivables over 6 months | at or below 25% | above 25% | Not disclosed | UNKNOWN |
| AR-4 | HASPL structure for external stake | wholly owned, no external stake | external stake or value-transfer structure | HASPL listed as WOS (R-L876); deck: "evaluating various strategic options" (P-L127) | AMBER |
| S-1 | 14-Sep watch: funding split per tranche | split disclosed | no split | Not disclosed (PPT-FN-11) | UNKNOWN |
| S-2 | FY27 capex actual vs Rs1,800 Cr | phasing disclosed | silent | H1 consolidated capex cash 449.15 (Part 1 5A); no phasing | AMBER |
| S-3 | Warrant proceeds fund at Rs74 | conversion receipts | none | No Q2 receipt; Rs416.25 Cr due (M-L1056-1058) | AMBER |

Counts (item 5 split into holding and pledge, 26 readings): GREEN 5, AMBER 6, RED 5, UNKNOWN 10.

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition [MEMORY] | Threshold | Current Reading (anchored) | FIRED? |
|---|---|---|---|
| 1. Hyperscaler contract delivery | below 60% pro-rata by H1 FY28 | Export-OFC not disclosed; test date H1 FY28 not reached | NO (untestable until H1 FY28; data absent) |
| 2. Promoter holding | below 25% | 28.29% (P-L569) | NO |
| 3. Promoter pledge | any initiation | Not disclosed in results, PR, deck or MA report | NO on evidence; UNCONFIRMED |
| 4. Receivables silence / unbilled | two consecutive quarters of receivables silence, OR above Rs200 Cr unexplained unbilled increase | Q1 was silent [MEMORY]. Q2 filings: receivable rupees on the balance sheet only; no ageing, DSO or unbilled. Other current assets +317.31 consolidated (non-parent +260.66), unlabelled (RES-FN-05). 19-Oct call pending | NO on filed evidence. AT RISK. Fires if the Role 5 addendum shows the call was silent on ageing and unbilled, or if management confirms the +317.31 as unbilled without explanation |
| 5. CARE rating | downgrade below A-/A2+ | No rating action in the inputs. CARE appears only as Monitoring Agency | NO (no new evidence) |
| 6. Restructuring value transfer | SRC announces structure that transfers OFC/defence value to a private entity at a discount | "we are evaluating various strategic options with the objective of sharpening business focus, improving capital allocation" (P-L127-128). No structure announced. HASPL is a WOS (R-L876) | NO. PROXIMITY FLAG (PPT-FN-01) |

Devil's-advocate early-warning signals [MEMORY]: Q1 export OFC below 1,200 (untestable); EBITDA margin below 16% (no: 24.81% operating); receivables/TTM above 55% (no: 38.57%); fuze third trial fails (no evidence); promoter below 27.5% (no); restructuring transfers value (not announced); receivables ageing deferred or opaque (YES, opaque again); OFC realisation declining (ND; deck claims "higher value realization", PM03, no metric). One of eight early-warning signals is lit.

No trigger has FIRED. Two sit at risk (#4, #6). Under 8A-W a fired trigger would mean AVOID; the operator decides.

### 6D. Growth trigger status

| Trigger [MEMORY] | Original Confidence | Confirming Evidence (Q2) | Killing Evidence (Q2) | Updated Status |
|---|---|---|---|---|
| 1. Hyperscaler OFC contract (Rs10,159 Cr, FY27-FY31) | Primary | Telecom Products revenue 2,321.98, +46.08% QoQ, result margin 30.85% (R-L839, R-L844); para 8 foreign subsidiaries revenue 1,066.16 (R-L246); exports "63%" (P-L507); book 57% export (P-L314) | Export-OFC rupee figure withheld a second quarter; kill test "margin below 12% PBT" not met; "secured raw materials" has no terms (PM02, PPT-FN-17) | ON TRACK (indirect evidence only) |
| 2. Capacity to 42.36 mn fkm OFC / 33.9 mn fkm OF by Dec-2026 | Medium | QIP OFC capex object completed Q2 (M-L242-246); other non-current assets +276.72 (R-L905) | Deck shows OF "Current: 28" and only July-2028 end states (P-L428-434); Dec-2026 step absent (PPT-FN-10) | DELAYED (interim milestone not reaffirmed) |
| 3. HASPL aerospace consolidation (CY26 close) | Medium | PR: completion "expected ... during the current quarter" (R-L754) | Rs90 Cr HASPL object missed 30-Sep-2026, zero use, delay "Not Ascertainable", extended to 31-Dec-2026 by circular resolution (M-L1095-1108, M-L1282); target book ~1,600 (P-L469-470) vs ~2,000 [MEMORY]; price and target financials not disclosed (6E) | DELAYED |
| 4. PCS/MPO interconnect; Rs215 Cr DC facility (Sep-2027) | Medium | PCS/DC "Emerging as a high-growth adjacency to the OFC business" (PM04, P-L467-471); "data centre connectivity solutions continue to strengthen" (M08, R-L749-750) | No DC-connectivity revenue, order book or margin (RES-FN-29, PPT-FN-19); Rs215 Cr facility absent from deck (PPT-FN-11) | ON TRACK on narrative only; facility UNVERIFIED |
| 5. Defence indigenisation | Low-medium | Defence revenue 54.94, result +3.45 (R-L840, R-L845); "serial production commences" (P-L541); MMHG Rs230 Cr facility (P-L436); "move towards higher value-added offerings in defence and aerospace value chain" (PM05) | H1 defence 78.68 = 15.7% of Rs500 Cr aspiration; H2 needs 3.83x the Q2 rate (RES-FN-11); own book ~250 [COMPUTED: 1,850 - 1,600] (PPT-FN-07); no fuze approval | DELAYED |

### 6E. Acquisition-economics probe (aerospace / defence consolidation)

| Item | Filed evidence | Reading |
|---|---|---|
| Target name | Not named. Phrased as "entity proposed to be acquired" (P-L469-470), "proposed aerospace business being acquired" (P-L534-536), "Proposed Acquisitions" (P-L473-474) | NOT FOUND |
| Consideration (price) | Not stated in results, PR, deck or MA report. The only purchase-side rupee figure is the Rs90 Cr preferential object "To Invest into equity shares of HFCL Advance Systems Private Limited" (M-L1107). The filings do not say whether Rs90 Cr is the consideration | NOT FOUND |
| Target revenue, PAT, ROCE, net debt or cash | Not stated | NOT FOUND |
| Customers and tenure behind the ~Rs1,600 Cr export book | Not stated | NOT FOUND |
| Purchase multiple (price / target PAT) | ND / ND | NOT COMPUTABLE |
| Share of defence book in the unowned entity | ~1,600 of ~1,850 (P-L469-470) | 86.5% [COMPUTED: 1,600 / 1,850] |
| Acquisition cash paid in H1 | Nil (R-L968); goodwill unchanged at 26.17 (R-L897) | Not closed at 30-Sep |
| Closing condition | "conditions precedent relating to the proposed transactions for consolidation of the defence business" (M-L1097-1146); deadline moved 30-Sep to 31-Dec-2026, delay "Not Ascertainable" (M-L1282) | Slipped once |

Consequence: no accretion is credited anywhere in this review. The deck counts the target's book as HFCL "confirmed" visibility before close. An order book is not earnings, and without price and target profit the "cheap or dear" question cannot be asked. Management question: Q6. The 31-Dec forward-map bull fork carries a price condition (Brief part 5). /fttcp and Role 1 must not credit the target's book or profit until price and target financials are filed.

---

## STEP 6.5: EXPECTATION LEDGER AND A21 BASE REFRESH: deferred to /fttcp and Role 1 (OR-30)

Facts flagged for the deferred refresh (no recompute here):

| Fact | Value | Anchor | Pillar / use |
|---|---|---|---|
| Q2 annualised consolidated revenue | 10,167.16 | [COMPUTED: 2,541.79 x 4] | A21 base candidate |
| Q2 annualised consolidated PAT | 1,576.88 | [COMPUTED: 394.22 x 4] | A21 base candidate |
| TTM consolidated revenue | 7,491.68 | Part 1 5A | Trailing-4Q base (lumpy-business option) |
| TTM consolidated PAT | 926.68 | [COMPUTED: 329.44 - 42.62 + 639.86] | Trailing-4Q base |
| TTM basic EPS | 5.74 | [COMPUTED: 2.13 - 0.25 + 3.86] | vs Notion FY27 base 3.15 and FY29 base 6.19 |
| Company guide FY27 revenue floor | 8,908.69; implied H2 YoY +46.69% | [COMPUTED]; R-L700 | Cross-check for any annualised base (H1 x 2 sits at the guide) |
| One-offs to adjust before annualising | seasonal employee fall about 16.72; subsidiary inventory release about 43.13 at cost (R-L809); deferred tax credit 7.49; other income 27.46 | RES-FN-07, RES-FN-06, R-L821, R-L805 | A21 adjustment list |
| Cash-timing item (not P&L) | current tax charged but unpaid in H1: 123.40 consolidated | R-L820, R-L966, R-L933 | Pillar 2 reading, not the earnings base |
| Unpriced acquisition | target book ~1,600; price and PAT NOT FOUND | 6E | Exclude from any base |
| Divergence vs Notion base | Q2 annualised PAT and TTM PAT each exceed the Notion FY27 base PAT 520 by more than 25% | [COMPUTED] | Protocol 6.5A: state which base governs (deferred) |
| Expectation Ledger (6.5B) | Not supplied to this run | ND | Ageing of credited rows deferred |

---

## STEP 7: FOUR-PILLAR RE-VALIDATION: deferred to /fttcp and Role 1 (OR-30)

Pillar-relevant facts flagged (no pillar is revised here):

| Pillar / Input | Notion assumption [MEMORY] | This quarter's fact (anchored) | Flag |
|---|---|---|---|
| Pillar 1 ROCE base | 12x on FY26 ROCE 9.86% | H1 annualised pre-tax ROCE 28.0% (26.35% ex-OI) [COMPUTED, Step 6A]; spot reading | FTTCP ROCE forward verdict is the sole authority; spot ROCE is context only |
| Pillar 2 cash multiplier | 0.85x on 4-yr CFO/PAT 0.18 | H1 CFO/PAT reported 0.71 consolidated / 0.53 standalone; with tax counted when charged 0.52 consolidated / 0.30 standalone; FCF +6.12 reported / (117.28) tax-accrual (Part 1 5A, 5B) | Reported reading sits in the 0.65-0.80 zone; tax-accrual reading sits below 0.65. One half-year only. Carry both readings; the remaining advance-tax instalments reverse the timing benefit |
| Growth Visibility Premium | +6.0x / +6.3x | Order book 28,911 (R-L681) vs 26,665 Q1 (P-L302) = +8.42%; implied Q2 inflow about 4,788 [INFERENCE: 28,911 - 26,665 + 2,541.79, assumes all revenue runs off the book]; guide at least 80% (R-L700), which H1 meets on run-rate; book mix vs revenue mix (PPT-FN-05); ~1,600 of the defence book sits in an unowned, unpriced entity (6E) | Visibility up; mix risk and unowned book named |
| Strategic Premium | +2.0x | "Evaluating various strategic options" (P-L127); HASPL object slip (M-L1095-1108); acquisition unpriced (6E); 31.30% of PAT on single-joint-auditor review (R-L236); that pool's cash balances fell 0.29 and its CFO is NOT FOUND (RES-FN-28) | Governance and structure flags |
| UA Multiplier | NOT ELIGIBLE (FII+DII 18.54%) | FII/FPI 17.24% + DII/MF 10.38% = 27.62% at 30-Sep-2026 (P-L569-573) | Institutional base changed; re-test qualifiers |
| Sector Cap blend | OFC/Cables 55% x25, other telecom 15% x30, EPC 25% x20, defence 5% x38 | Q2 revenue mix: Telecom Products 91.35%, Turnkey 5.35%, Defence 2.16%, Others 1.13% [COMPUTED from R-L839-842]; OFC vs other telecom split ND | EPC weight 25% looks stale |
| Hurdle Ratio recheck | CONDITIONAL; passes only at Rs60-75 | CMP Rs262 [MEMORY, 14-Oct]; Rs226.65 at 30-Sep [COMPUTED: 34,691.10 / 153.06, P-L571-574]; trailing PE 45.6x at Rs262, 39.5x at Rs226.65 on TTM EPS 5.74 [COMPUTED] | Recompute deferred |

---

## STEP 8: POSITION DECISION

Decision Status verified from Step 0A: WATCHLIST ("DO NOT INITIATE"). Not held. Branch: 8A-W.

### 8A-W. Watchlist decision logic

- Any thesis-broken trigger FIRED? No (Step 6C). Two at risk: #4 pending the Role 5 addendum; #6 proximity.
- Actuals vs projections: AT or ABOVE BASE on revenue pace, margin, PAT, EPS and ROCE (Step 6A). AT the new company guide on revenue run-rate.
- Protocol action: confirm or tighten the entry zone. Check the pre-committed BUY gate.
- Pre-committed BUY gate [MEMORY]: price in Rs60-75 AND entry tighteners (a) Export-OFC revenue disclosed and at or above 1,800 a quarter, (b) receivables/DSO disclosed and in green, (c) pledge confirmed zero; AND STLTECH exited or trimmed at the same time.
  - Price: NOT MET (Rs262 [MEMORY]; Rs226.65 at 30-Sep [COMPUTED]).
  - (a) NOT MET (not disclosed).
  - (b) NOT MET (company did not disclose; computed DSO 140.78 above green 110).
  - (c) NOT MET (pledge not disclosed).
  - No BUY gate threshold was met.
- Entry zone: CONFIRMED at Rs60-75 pending recompute. The base projections are stale on the upside (H1 PAT 639.86 above FY27 base 520; TTM EPS 5.74 vs FY29 base 6.19). The recompute belongs to /fttcp and Role 1 (OR-30). It must carry both cash readings and credit nothing for the unpriced acquisition (6E). The Notion Rs100 alert ("formal model refresh") is already justified by the numbers, without the price trigger.
- Proposed Decision Status: NO CHANGE. WATCHLIST, DO NOT INITIATE. The operator sets it.
- Next decision gate: the Role 5 addendum on the 19-Oct call (tripwire #4), then 31-Dec-2026 (HASPL Rs90 Cr deadline and aerospace close), then Q3 FY27 results.

### 8B. Add-back / trim trigger refinement

- Original add-back trigger [MEMORY]: alerts at Rs100 (model refresh) and Rs75 (begin SMALL accumulation in tranches); tighteners (a), (b), (c); STLTECH condition.
- Revised add-back trigger (proposal; operator decides): keep (a), (b), (c) and the STLTECH condition. Add (d) the strategic-options outcome is filed and leaves listed holders with 100% of OFC and Defence economics; (e) the aerospace acquisition closes by 31-Dec-2026 with consideration and target revenue and PAT filed, and the HASPL Rs90 Cr is deployed, or a filed reason is given; (f) receivables ageing and unbilled revenue are disclosed at the FY27 year-end balance sheet; (g) full-year FY27 CFO/PAT, after H2 advance tax, is at or above 0.65.
- Original trim ladder: not applicable (not held). Risk-matrix rules stand: trim if telecom product PBT margin below 14% for two quarters; hard exit on any value-transfer structure; hard stop on any pledge.
- Revised trim ladder: none.

### 8C. Single cleanest metric for next quarter

Metric: Q3 FY27 consolidated Telecom Products segment revenue (segment table, same line as R-L839).
- Why this one: Export-OFC revenue is the thesis metric but was withheld two quarters running. Telecom Products is always filed, holds the OFC and hyperscaler engine (91.35% of Q2 revenue), and separates the two readings of the guide (H2 held vs H2 down).
- Bull threshold: at or above Rs2,321.98 Cr (Q2 held), with segment result margin at or above 30%.
- Bear threshold: below Rs2,006.15 Cr [COMPUTED: consolidated H2 guide pace 2,225.96 less Q2 non-Telecom revenue 219.81]. That puts the quarter below the guide pace and supports the reading that Q2 included a one-time stock release (RES-FN-06).

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

### 8.5A. Core questions (template, ranked by thesis materiality)

| # | Question | Why It Matters | Bull Answer | Bear Answer | Cat. | From finding |
|---|---|---|---|---|---|---|
| 1 | Slide 5 says you are "evaluating various strategic options" because each vertical has a distinct working-capital profile. Does any option under evaluation leave listed HFCL shareholders with less than 100% of the OFC, Defence or Aerospace economics? Yes or no. | Thesis-broken trigger #6; demerger flip history [MEMORY] | "No." Any change is a mirror-shareholding carve-out of Turnkey/EPC only | "Yes", or a promoter-linked vehicle or strategic partner at HASPL level, or no answer | G | PPT-FN-01, PPT-FN-13, RES-FN-24 |
| 2 | At 30-Sep-2026, how much of trade receivables (Rs2,889.58 Cr incl. non-current) is over 6 months old, and how much unbilled revenue sits inside other current assets of Rs2,147.96 Cr (up Rs317.31 Cr in H1)? | Tripwire #4 second-quarter test | Over-6m below 15%; unbilled flat or below FY26 Rs604 Cr [MEMORY] | Unbilled up more than Rs200 Cr, or no numbers again | D | RES-FN-05, PPT-FN-12, RES-FN-22 |
| 3 | Consolidated PAT Rs394.22 Cr exceeds standalone Rs268.02 Cr by Rs126.20 Cr (47.09%); four subsidiaries reviewed by one joint auditor earned Rs123.40 Cr. Which entity earned the largest share, and what gross margin does the parent earn on goods it sells to that entity? | Profit location, transfer pricing, NCI leakage | HFCL Inc./B.V. export arm at a documented arm's-length markup | HTL Limited (non-wholly-owned) or an undisclosed basis | A | RES-FN-04, RES-FN-09, RES-FN-22 |
| 4 | Is the "at least 80%" FY27 growth measured on consolidated FY26 revenue of Rs4,949.27 Cr? If yes, H2 needs only Rs2,225.96 Cr a quarter, 12.43% below Q2, and H2 YoY growth of 46.69% against 132.81% in H1. Do you expect Q3 revenue below Q2's Rs2,541.79 Cr? Yes or no. | Separates "floor" from "H2 step-down" | Consolidated basis; Q3 at or above Q2; the guide is a floor | Q3 lower; part of Q2 was one-time | B | RES-FN-10, PPT-FN-02 |
| 5 | Which conditions precedent for the defence consolidation were open at 30-Sep-2026, and will the Rs90 Cr HASPL equity investment be deployed by 31-Dec-2026? Yes or no. | Second slip on the same object; growth trigger 3 | Yes; CPs named and in hand; closing date firm | No, or another extension, or CPs outside company control | E | RES-FN-12, MA-FN-01, MA-FN-10, RES-FN-02 |
| 6 | What is the total consideration for the aerospace acquisition, and what were the target's last full-year revenue, PAT, net debt or cash, and ROCE? Which customers, and what contract tenure, sit behind the ~Rs1,600 Cr export book? | 86.5% of the defence book sits in an unowned, unpriced entity; multiple NOT COMPUTABLE (6E) | Price and target financials filed; implied PE at or below HFCL's own; named customers with multi-year tenure | No price before close, or a price that implies a multiple above HFCL's own, or an unnamed customer base | E | A5-M5; PPT-FN-07, PPT-FN-09, MA-FN-01, RES-FN-12 |
| 7 | Turnkey lost Rs122.58 Cr on Rs136.07 Cr revenue, above the Rs80-90 Cr guide. In which quarter will the Turnkey segment result reach zero? | H1 Turnkey loss Rs210.11 Cr exceeds FY26 full year | A named quarter in FY27 with BharatNet III billing | No date; losses into FY28 | C | RES-FN-20 (with RES-FN-19) |
| 8 | What was Q2 export OFC revenue to hyperscalers, in Rs Cr? | Notion's cleanest metric; withheld two quarters | At or above Rs1,800 Cr | Below Rs1,200 Cr, or withheld a third time | B | PPT-FN-05 |
| 9 | Will the warrant holders pay the Rs416.25 Cr balance and convert all 7.5 cr warrants before 25-Nov-2027? Yes or no, and in which quarter? | Rs416.25 Cr of preferential objects (preform Rs175 Cr, defence, WC, GCP) has no cash until conversion | Yes, full conversion by a named quarter | Partial, late, or "depends on price" | F | RES-FN-18, MA-FN-03, MA-FN-04, PPT-FN-14 |

### 8.5B. Extended questions (IR email; every remaining A3 FORWARD-SIGNAL or AMBIGUOUS finding)

| # | Question | Cat. | From finding |
|---|---|---|---|
| 10 | Turnkey segment liabilities fell Rs185.25 Cr QoQ to Rs903.22 Cr. How much was customer or mobilisation advances consumed, and how much was vendor payables paid? | D | RES-FN-20 |
| 11 | Subsidiaries released about Rs43 Cr (at cost) of finished goods and WIP in Q2 after a Q1 build of about Rs128 Cr. How much of Q2 revenue was shipment of stock built in Q1? | A | RES-FN-06 |
| 12 | Name the aerospace target or targets. Does the Rs28,911 Cr "confirmed" order book include the target's ~Rs1,600 Cr book? Yes or no. | E | PPT-FN-09, PPT-FN-13 |
| 13 | H1 defence revenue was Rs78.68 Cr. How much of the ~Rs500 Cr FY27 defence aspiration depends on closing the acquisition inside FY27, in Rs Cr? | B | RES-FN-11, PPT-FN-07, RES-FN-21 |
| 14 | The target's defence book was ~Rs2,000 Cr in Q1 [MEMORY] and is ~Rs1,600 Cr now. How much was executed, and how much was cancelled or re-scoped? | E | PPT-FN-08 |
| 15 | For the ~Rs1,800 Cr capex plan plus the Rs230 Cr MMHG Phase-1, what is the split between debt, internal accruals and warrant money, and the FY27 capex amount? | F | RES-FN-14, PPT-FN-11 |
| 16 | Which is the FY27 export guide: "more than 70%" or "65%+"? Is the 63% the Q2 share or the H1 share? | B | PPT-FN-06, PPT-FN-05 |
| 17 | How much of the Rs28,911 Cr order book executes in FY27 and in FY28, in Rs Cr each? | B | RES-FN-13, PPT-FN-05, PPT-FN-09 |
| 18 | Is the ">27% by FY29" EBITDA margin target measured including other income, as the Q2 25.89% figure is? Yes or no. | C | PPT-FN-03, PPT-FN-04 |
| 19 | Will OF capacity reach 33.9 mn fkm and OFC 42.36 mn fkm by Dec-2026, as stated earlier? Yes or no. | B | PPT-FN-10 |
| 20 | Who is the buyer of the standalone held-for-sale group (net Rs41.26 Cr at 30-Sep), and is it a group entity? | A | RES-FN-01 |
| 21 | Which item debited other equity by about Rs30.6 Cr in H1 (for example a Re0.20 dividend declared and unpaid)? | D | RES-FN-03 |
| 22 | Which temporary differences produce the recurring deferred-tax credit (Rs7.49 Cr consolidated in Q2), and in which year do they end? | C | RES-FN-16 |
| 23 | Which investment produced the Q1 consolidated OCI gain (Rs74.49 Cr items not reclassified) and the Rs13.71 Cr Q2 reversal, and how is it valued? | D | RES-FN-17 |
| 24 | Which products make up the Rs407.48 Cr intangibles under development, and in which quarter does capitalisation start? | F | RES-FN-23 |
| 25 | Is the R&D payroll funded from QIP money (Rs10.98 Cr in Q2) expensed or capitalised? | D | MA-FN-07 |
| 26 | Will the remaining Rs24.27 Cr QIP R&D money be used by 31-Mar-2027? Yes or no. | B | MA-FN-06, MA-FN-08 |
| 27 | How much QIP money moved into the cash-credit account in Q1 FY27, and how much remains there? | D | MA-FN-05 |
| 28 | Was the Rs10.30 Cr FD that matured 09-Oct-2026 re-deposited or spent, and which LCs does the Rs21.22 Cr QIP FD secure? | D | MA-FN-09 |
| 29 | Provide the item-wise use of the Rs93 Cr QIP general corporate purposes money spent in Q4 FY26. | G | MA-FN-11 |
| 30 | Will the Rs175 Cr preform money go to HFCL Technologies Pvt Ltd as equity or as a loan, and will preform be sold to the parent at cost-plus? | F | MA-FN-13 |
| 31 | Why was the Rs90 Cr deadline extended by circular resolution on 25-Sep-2026, and did the audit committee receive a Reg 32 deviation or variation statement? Yes or no. | G | MA-FN-02, MA-FN-10 |
| 32 | Did the 19-Oct-2026 board approve any item other than the results? Yes or no; if yes, which. | G | RES-FN-24 |
| 33 | In which fiscal year do you expect the Rs10,000 Cr revenue milestone, and is the Rs500 Cr defence figure a forecast or an aspiration? | B | RES-FN-15 |
| 34 | Confirm promoter pledge is zero at 30-Sep-2026. Yes or no. | G | Notion Q1 question 12 (carry-forward) |
| 35 | Defence segment net assets are Rs279.91 Cr against Q2 revenue Rs54.94 Cr. What further investment is planned in FY27, in Rs Cr? | F | RES-FN-21 |
| 36 | The four subsidiaries under auditor para 7 earned H1 NPAT of Rs186.19 Cr while their cash balances fell Rs0.29 Cr. What was their H1 operating cash flow, and how much do they hold as receivable from HFCL at 30-Sep-2026? | D | RES-FN-28 |
| 37 | What were Q2 data-centre connectivity (PCS/DC) revenue and order book, in Rs Cr? | B | RES-FN-29, PPT-FN-19 |
| 38 | "Secured raw materials": with which suppliers, for what volume and tenor, and at fixed or market-linked prices? | E | PPT-FN-17 |
| 39 | What was Q2 OFC realisation per fkm against Q1, and what share of OFC volume is under long-term contracts priced below spot? | C | PPT-FN-18 |
| 40 | Is "#1 in OFC" an India claim or a global one, and what source and market-share percentage support it? | G | PPT-FN-20 |
| 41 | How much BharatNet III revenue did Q2 book, and how much BharatNet order book remains, while you shift away from low-profit turnkey work? | E | PPT-FN-21 |
| 42 | H1 current tax charged was Rs243.29 Cr against Rs119.89 Cr paid. How much advance tax falls due in H2 FY27, in Rs Cr? | D | A5-M4 (cash reading; no A3 ID) |

### 8.5C. Coverage of A3 FORWARD-SIGNAL and AMBIGUOUS findings (54 of 54)

| Doc | Finding -> question(s) |
|---|---|
| Results (23) | RES-FN-01 Q20; RES-FN-02 Q5; RES-FN-03 Q21; RES-FN-04 Q3; RES-FN-05 Q2; RES-FN-06 Q11; RES-FN-09 Q3; RES-FN-10 Q4; RES-FN-11 Q13; RES-FN-12 Q5, Q6; RES-FN-13 Q17; RES-FN-14 Q15; RES-FN-15 Q33; RES-FN-16 Q22; RES-FN-17 Q23; RES-FN-18 Q9; RES-FN-20 Q7, Q10; RES-FN-21 Q13, Q35; RES-FN-22 Q2, Q3; RES-FN-23 Q24; RES-FN-24 Q1, Q32; RES-FN-28 Q36; RES-FN-29 Q37 |
| Presentation (19) | PPT-FN-01 Q1; PPT-FN-02 Q4; PPT-FN-03 Q18; PPT-FN-04 Q18; PPT-FN-05 Q8, Q16, Q17; PPT-FN-06 Q16; PPT-FN-07 Q6, Q13; PPT-FN-08 Q14; PPT-FN-09 Q6, Q12, Q17; PPT-FN-10 Q19; PPT-FN-11 Q15; PPT-FN-12 Q2; PPT-FN-13 Q1, Q12; PPT-FN-14 Q9; PPT-FN-17 Q38; PPT-FN-18 Q39; PPT-FN-19 Q37; PPT-FN-20 Q40; PPT-FN-21 Q41 |
| MA report (12) | MA-FN-01 Q5, Q6; MA-FN-02 Q31; MA-FN-03 Q9; MA-FN-04 Q9; MA-FN-05 Q27; MA-FN-06 Q26; MA-FN-07 Q25; MA-FN-08 Q26; MA-FN-09 Q28; MA-FN-10 Q5, Q31; MA-FN-11 Q29; MA-FN-13 Q30 |

NEUTRAL-FACT and CONFIRMATORY-NEGATIVE findings are processed in the body: RES-FN-07 (Step 3), RES-FN-08 (Step 0D), RES-FN-19 (Q7, Step 6B), RES-FN-25 and RES-FN-26 (Step 0D, 1B), RES-FN-27 (Step 0D), PPT-FN-15 and PPT-FN-16 (governance data points), MA-FN-12 (drafting), MA-FN-14 (Step 6D).

### 8.5D. Top 3 by likelihood of thesis-changing information

- Bull probability: Q4 (guide basis and Q3 vs Q2). A "Q3 at or above Q2" answer makes the raised guide a floor and lifts the base case.
- Bear confirmation: Q2 (ageing and unbilled). Silence or an unexplained unbilled rise above Rs200 Cr fires tripwire #4.
- Transparency test: Q1 (strategic options). A vague answer on structure, given the demerger history [MEMORY], is itself the signal. Q6 (acquisition price) is the second transparency test.

### 8.5E. Channel

The 19-Oct-2026 concall already took place; the transcript is pending. Step 1: the Role 5 addendum marks each of the 42 questions and the 15 Q1 questions as ANSWERED / PARTIALLY / EVADED / NOT ADDRESSED. Step 2: send every question not answered specifically as an IR email, verbatim, to Manoj Baid and Amit Agarwal (contacts at R-L793-795).

---

## MONITORABLES AND CATALYST LIST (seeded from the A3 commitment registers and Board Outcome forward items)

| # | Item | Implied date | Source |
|---|---|---|---|
| M1 | Role 5 addendum: 19-Oct call silence audit on receivables ageing and unbilled (tripwire #4) | Pending (this cycle) | Step 6C; PPT-FN-12 |
| M2 | Rs90 Cr HASPL equity investment deployed (revised deadline) | 31-Dec-2026 | M-L1095-1108, M-L1166-1167 (MA C7) |
| M3 | Aerospace acquisition completion "during the current quarter", with consideration and target financials filed | by 31-Dec-2026 | R-L754 (RES C3); 6E |
| M4 | Nivetti completion (possible link to M2/M3, [INFERENCE]) | 31-Dec-2026 | [MEMORY] |
| M5 | OF 33.9 / OFC 42.36 mn fkm interim step | Dec-2026 | [MEMORY]; absent from deck (PPT-FN-10) |
| M6 | Payment of the 123.40 H1 unpaid current tax | H2 FY27: falls due under the remaining advance-tax instalments by year-end [INFERENCE] | R-L820, R-L966, R-L933 |
| M7 | Q3 FY27 results: Telecom Products revenue vs Rs2,321.98 / Rs2,006.15 Cr; first non-zero exceptional item; entity-list addition; goodwill | Date not filed (Q3 results, about Jan-Feb 2027 on cadence [INFERENCE]) | Step 8C; RES-FN-02, RES-FN-12, RES-FN-27 |
| M8 | Strategic-options outcome | Undated | P-L124-129 (PPT C-06) |
| M9 | Held-for-sale disposal completes (gain or loss vs net 41.26) | Undated | R-L917, R-L937 (RES-FN-01) |
| M10 | FY27 revenue at least 80% over FY26 (at least 8,908.69 consolidated) | 31-Mar-2027 | R-L700, R-L743; P-L111 (RES C1, PPT C-01) |
| M11 | Defence revenue ~Rs500 Cr | 31-Mar-2027 | R-L709-710; P-L123 (RES C2, PPT C-05) |
| M12 | Exports 65%+ / more than 70%; ~90% product revenue | FY27 | P-L502-508 (PPT C-13, C-14) |
| M13 | QIP R&D Rs24.27 Cr used | 31-Mar-2027 | M-L563-565 (MA C2) |
| M14 | FY27 year-end balance sheet and full-year CFO (cash re-test after advance tax; ageing disclosure) | Q4 FY27 results, date not filed | Part 1 5D |
| M15 | Defence facility first tranche Rs15 Cr (preferential object) | 30-Sep-2027 | M-L1088-1089 (MA C10) |
| M16 | Rs215 Cr DC-connectivity facility | Sep-2027 [MEMORY] | Absent from deck (PPT-FN-11) |
| M17 | Warrant conversion; Rs416.25 Cr balance received | by ~25-Nov-2027 [COMPUTED: 25.05.2026 + 18 months] | M-L1056-1058; R-L869 (MA C14, RES C8) |
| M18 | Preferential WC Rs140 Cr, GCP Rs100 Cr, defence balance Rs35 Cr | FY28 | M-L1090-1091, M-L1148-1155 (MA C11-C13) |
| M19 | Preform object Rs175 Cr via HFCL Technologies | 31-Jul-2028 | M-L1085-1086 (MA C9) |
| M20 | OF 43.1 / OFC 62 mn fkm | July 2028 | P-L428-434 (PPT C-07, C-08) |
| M21 | Preform 600 MT, capex Rs1,250 Cr | October 2028 | P-L436-442 (PPT C-09) |
| M22 | EBITDA margin above 27%; Rs10,000 Cr revenue "much earlier" than FY29 | FY29 | P-L503-504; R-L747-748 (PPT C-02, C-12; RES C7) |
| M23 | MMHG Phase-1 Rs230 Cr; Andhra ammunition and MP preform facilities | Undated | P-L436-439; R-L779-780 (RES C5, C6) |
| M24 | Order book Rs28,911 Cr visibility "six to seven years and beyond" | FY27 to ~FY33-34 | R-L681, R-L697 (RES C12) |
| M25 | Qualitative claims with no metric: OFC portfolio and DC connectivity "continue to strengthen" (M08); secured raw materials (PM02); value realization (PM03); value-added products to "ease working capital" (PM05) | Undated | RES C13; PPT C-18 to C-20 |
| M26 | Operator rulings pending: Promoter Verdict CONCERN toward AVOID after slip #5 | Operator | [MEMORY] |

Board Outcome forward items: the 19-Oct letter names only the results, "inter-alia" (R-L44; M04); the enclosure list (M03) confirms it; meeting 11:00-11:40 (R-L33-35). No other forward item filed (RES-FN-24).

---

## STEP 9: NOTION UPDATE (payload only; not written by A4)

- Decision Status: NOT written. Proposed: no change (WATCHLIST, DO NOT INITIATE). No trigger fired.
- Position Size: no change (not held).
- EM Score: no change proposed.
- Promoter Verdict: no change by A4. The pending operator ruling (slip #5) stands. New data points for that ruling: HASPL Rs90 Cr object extension by circular resolution (MA-FN-01, MA-FN-02); Dec-2026 capacity step and Rs215 Cr facility dropped from the deck; acquisition unpriced (6E).
- Key Notes line (proposed, date-prefixed): "20-Oct-2026 Q2 FY27 Role 4 [FILED]: consol revenue Rs2,541.79 Cr (+143.62% YoY), op EBITDA 24.81%, PAT Rs394.22 Cr. H1 at the new >=80% guide on run-rate (guide implies H2 YoY +46.69%). H1 CFO Rs455.27 Cr (CFO/PAT 0.71 reported; 0.52 with Rs123.40 Cr unpaid current tax counted). Turnkey loss Rs122.58 Cr. Deck: 'evaluating various strategic options' (trigger #6 proximity). HASPL Rs90 Cr object missed 30-Sep, moved to 31-Dec; acquisition unpriced. Receivables ageing/unbilled undisclosed: tripwire #4 pending Role 5. Verdict PROCEED WITH FLAGS. No trigger fired. Decision unchanged: WATCHLIST, DO NOT INITIATE (operator-only)."
- Memory corrections for the page: warrant balance Rs416.25 Cr (not ~Rs412.5 Cr); FII+DII 27.62% at 30-Sep-2026 (not 18.54%); HFCL Technologies Pvt Ltd is a wholly owned subsidiary (R-L878), distinct from HTL Limited.
- Sections to append: this review in full, plus the Role 5 addendum when produced.

---

## VERDICT CARD

| Field | Value |
|---|---|
| Protocol verdict | PROCEED WITH FLAGS |
| Catalyst status | ON TRACK (revenue engine); DELAYED (HASPL, capacity interim step, defence) |
| Thesis status | INTACT on operations; WEAKENED on governance, cash quality and disclosure |
| Cash conversion | INDETERMINATE-WITH-DIRECTION. Reported CFO/PAT 0.71; 0.52 with unpaid current tax counted. Missing: receivable ageing, unbilled breakup, full-year CFO after advance tax, para 7 subsidiary CFO, CARE WC view |
| Decision Status verified | WATCHLIST ("DO NOT INITIATE"), not held |
| Position branch | 8A-W |
| Auditor opinion | Unmodified limited review, both bases; no EoM |
| Business type | Standard |

Flags (decision stays with the operator):
1. Trigger #6 proximity: "evaluating various strategic options" (P-L127). Not fired.
2. Tripwire #4 at risk: ageing and unbilled undisclosed; other current assets +317.31; decided by the Role 5 addendum.
3. HASPL Rs90 Cr object missed 30-Sep-2026; extended to 31-Dec-2026 by circular resolution (M-L1095-1108). Slip-log treatment is operator-only.
4. Acquisition unpriced: target, consideration and target profit NOT FOUND; multiple NOT COMPUTABLE; 86.5% of the defence book sits in the unowned entity. No accretion credited.
5. Cash quality: H1 CFO includes Rs123.40 Cr of current tax charged but unpaid. CFO/PAT 0.71 reported vs 0.52 consolidated / 0.30 standalone with tax counted when charged.
6. Turnkey loss (122.58) above the Rs80-90 Cr guide [MEMORY]; H1 loss (210.11) exceeds FY26 full year.
7. Standalone-consolidated PAT gap 47.09% (Q1 37.07%); 31.30% of group PAT rests on one joint auditor's review. That pool's cash balances fell 0.29 in H1 and its operating cash flow is NOT FOUND (RES-FN-28; Q36).
8. Notion projections stale on the upside: H1 PAT 639.86 above FY27 base 520; TTM EPS 5.74 = 92.7% of FY29 base 6.19. Re-base at /fttcp and Role 1. H1 is at, not above, the new guide.
9. Guide basis unstated: the consolidated reading lets H2 run 12.43% below Q2 and implies H2 YoY +46.69%.
10. Disclosure pattern: targets raised (revenue, margin, exports), dated milestones dropped (Dec-2026 capacity, Rs215 Cr facility), qualitative claims with no metric (M08, PM02-PM05).
11. Tracker rows not supplied; OR-17 three-signal floor untested.
12. Role 5 pending; Steps 6.5 and 7 deferred (OR-30).

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (Q2 results, press release, deck), AGENCY (CARE Monitoring Agency report), MGMT (management claim in a filed document), SECONDARY (broker), INFERENCE. Each figure also says whether it is from this quarter's filings [Q2] or from prior Notion work [Notion].

### 1. Summary narrative

HFCL had its biggest quarter on record. Revenue was Rs2,541.79 Cr, up 143.62% on last year (FILED, Q2). Operating margin, without other income, rose to 24.81% from 18.24% (FILED, Q2, computed). Profit after tax was Rs394.22 Cr, more than five times last year (FILED, Q2). The gain came from scale. Gross margin did not change. Staff and overhead costs fell as a share of sales.

The new guide is at least 80% growth for FY27 (MGMT, Q2). The first half already runs at that pace, not above it (FILED, Q2, computed). The guide allows the second half to grow 46.69%, against 132.81% in the first half.

Cash turned, but less than it looks. The company reported Rs455.27 Cr of operating cash in the half year (FILED, Q2). Rs123.40 Cr of that is tax charged but not yet paid (FILED, Q2, computed). Counted when charged, cash was 52% of profit, not 71%. Capex took the rest, so free cash was about zero, or negative on the tax-accrual reading.

Three things cloud the print. First, the deck says the board is "evaluating various strategic options" for its businesses (MGMT, Q2). On this name, that wording sits close to the demerger history and to trigger #6 (Notion). Second, the company again gave no receivable ageing and no unbilled figure (FILED, Q2). A line that can hold unbilled work rose Rs317.31 Cr in six months. Third, the defence deal slipped and has no price. Rs90 Cr meant for HASPL by 30-Sep was not spent, and the deadline moved to 31-Dec-2026 (AGENCY, Q2). No document names the target or what HFCL will pay.

The Turnkey business lost Rs122.58 Cr on Rs136.07 Cr of sales (FILED, Q2). More profit now sits in subsidiaries: group profit is 47.09% above the parent's (FILED, Q2, computed).

For the decision: no trigger fired. The name stays on WATCHLIST, DO NOT INITIATE. The price is far above the Rs60-75 entry zone (Notion). The old projections are now too low, and /fttcp and Role 1 must redo them.

### 2. Sector intelligence

Optical fibre cable demand has two drivers in the filings. One is AI and hyperscale data centres. The other is telecom networks, at home and abroad (MGMT, Q2). Exports were 63% of revenue on an unstated base (MGMT, Q2). The order book is 57% export (MGMT, Q2). The deck calls the market a "structural demand upcycle" but gives no price or volume figure (MGMT, Q2).

Government work is the other leg. BharatNet III is a state rural broadband programme (Notion). In HFCL's books it sits in Turnkey, which is shrinking and losing money (FILED, Q2). The company says it is "deliberately shifting from low-profit turnkey work" and also "actively catering to ... Bharatnet" (MGMT, Q2). Those two lines pull in different directions.

Defence is a policy-driven market. The deck cites HAL preferred-supplier status and DRDO technology transfer (MGMT, Q2). Revenue is still small: Rs78.68 Cr in the half year (FILED, Q2).

Tailwind: data-centre fibre demand and private customers at about 92% of revenue (MGMT, Q2). Headwind: the order book is about 35% government (MGMT, Q2, computed), which can pull the mix back toward slow-paying work (INFERENCE).

### 3. Business-model intelligence

HFCL earns most of its money by making and selling fibre, cable and telecom products. That segment was 91.35% of Q2 revenue at a 30.85% segment margin (FILED, Q2, computed). Exports go through overseas subsidiaries. Two foreign subsidiaries booked Rs1,066.16 Cr of revenue in Q2 (FILED, Q2).

The model is drifting in three ways this quarter. Profit is moving below the parent: parent gross margin fell to 31.19% while group gross margin held at 38.25% (FILED, Q2, computed). The four subsidiaries with the fastest profit growth earned Rs186.19 Cr in the half year, while their cash balances fell Rs0.29 Cr (FILED, Q2). Their operating cash flow is not disclosed, so how much of that profit turned into cash is unknown. Capex is front-loaded: Rs276.72 Cr went into other non-current assets, read as capital advances, before any new plant runs (FILED, Q2; advance label INFERENCE). The new preform plant is meant to lift margins, but it waits on Rs416.25 Cr of promoter warrant money (AGENCY, Q2).

Working capital looks better. Receivable days fell to 140.78 from 183.04 on a trailing basis (FILED, Q2, computed). That is still long. Without ageing data, the improvement cannot be confirmed as structural.

The EBITDA figure in the press release includes other income. The operating figure is about one point lower (FILED, Q2, computed).

### 4. Competition intelligence

HFCL claims to be the number one optical fibre cable supplier in India (MGMT, Q2, slide 13). Slide 20 repeats "#1 in OFC" without "in India" and adds "strong market share in Wifi and UBR" with no number (MGMT, Q2). It says it supplies "majority of Hyper-scalers" and most global Tier 1 telecom customers (MGMT, Q2). These are company claims, not third-party data.

The direct listed peer on file is Sterlite Technologies (STLTECH), which the operator already holds (Notion). The thesis allows an HFCL entry only if STLTECH is cut at the same time (Notion). Peer results for this quarter are not in the inputs.

Where HFCL looks stronger: backward integration into preform, which few cable makers own (MGMT, Q2), and a 30.85% telecom segment margin (FILED, Q2). Where it looks weaker: the loss-making EPC arm, long receivable cycles, and a defence business that relies on a target it does not yet own and has not priced (FILED and MGMT, Q2).

Competitive risk to watch: long-term hyperscaler contracts were said to carry margins 1-2 points below spot (Notion). If spot fibre prices fall, the margin gain in segment results can reverse (INFERENCE). Global fibre makers are not named in the inputs.

### 5. Forward map (next about 10-11 months)

Make-or-break next reading: Q3 FY27 consolidated Telecom Products revenue. Bull at or above Rs2,321.98 Cr. Bear below Rs2,006.15 Cr. Results date not filed; about January-February 2027 on past cadence (INFERENCE).

- Role 5 addendum on the 19-Oct call (pending). Bull: management gives ageing and unbilled figures. Bear: silence again, and tripwire #4 fires.
- 31-Dec-2026, HASPL Rs90 Cr and aerospace close. Bull: the deal closes, the target is named, and the price and target profit are filed so the purchase multiple can be checked. Bear: a second extension, or a close with no price disclosed, and the defence plan rests on a book HFCL cannot value.
- Dec-2026, interim capacity step. Bull: OF and OFC reach the earlier Dec-2026 levels. Bear: the step quietly folds into July 2028.
- Strategic-options outcome (undated). Bull: Turnkey is carved out with the same shareholders. Bear: OFC or defence value moves to a vehicle where listed holders own less, and trigger #6 fires.
- Q3 FY27 results (about Jan-Feb 2027). Bull: Q3 revenue holds at Q2's Rs2,541.79 Cr and Turnkey loss narrows. Bear: revenue falls toward the Rs2,225.96 Cr guide pace and Q2's stock release proves one-time.
- 31-Mar-2027, FY27 close. Bull: revenue at or above Rs8,908.69 Cr and defence near Rs500 Cr. Bear: defence far short and the QIP R&D money of Rs24.27 Cr unspent.
- Q4 FY27 results and full-year cash flow (date not filed). Bull: full-year CFO/PAT stays near 0.71 after the second-half tax payments. Bear: advance tax on the Rs123.40 Cr first-half accrual and working capital pull full-year CFO/PAT toward 0.52 or lower.
- 30-Sep-2027, first Rs15 Cr defence facility tranche. Bull: spent on time. Bear: deferred, waiting on warrant money.

---

```yaml
stage: A4-analyst
company: "HFCL"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, presentation, mareport]
ledger_reconciliation:
  notes: 10
  turns: 0
  slides: 25
  all_reviewed: true
  a3_findings_incorporated: [RES-FN-01, RES-FN-02, RES-FN-03, RES-FN-04, RES-FN-05, RES-FN-06, RES-FN-07, RES-FN-08, RES-FN-09, RES-FN-10, RES-FN-11, RES-FN-12, RES-FN-13, RES-FN-14, RES-FN-15, RES-FN-16, RES-FN-17, RES-FN-18, RES-FN-19, RES-FN-20, RES-FN-21, RES-FN-22, RES-FN-23, RES-FN-24, RES-FN-25, RES-FN-26, RES-FN-27, RES-FN-28, RES-FN-29, PPT-FN-01, PPT-FN-02, PPT-FN-03, PPT-FN-04, PPT-FN-05, PPT-FN-06, PPT-FN-07, PPT-FN-08, PPT-FN-09, PPT-FN-10, PPT-FN-11, PPT-FN-12, PPT-FN-13, PPT-FN-14, PPT-FN-15, PPT-FN-16, PPT-FN-17, PPT-FN-18, PPT-FN-19, PPT-FN-20, PPT-FN-21, MA-FN-01, MA-FN-02, MA-FN-03, MA-FN-04, MA-FN-05, MA-FN-06, MA-FN-07, MA-FN-08, MA-FN-09, MA-FN-10, MA-FN-11, MA-FN-12, MA-FN-13, MA-FN-14]
  ledger_rows_reviewed: {results: 1515, presentation: 431, mareport: 411, a2_added: [M01, M02, M03, M04, M05, M06, M07, M08, PM01, PM02, PM03, PM04, PM05, PM06, PM07]}
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST (DO NOT INITIATE); not held"
position_branch: "8A-W"
sc_gap_pat_pct: ["Q2FY26: 17.06", "Q1FY27: 37.07", "Q2FY27: 47.09", "H1FY26: 123.14", "H1FY27: 43.07", "FY26: 30.28"]
questions_for_management:
  - {q: "Q1 Does any strategic option leave listed holders with <100% of OFC/Defence/Aerospace economics? Y/N", from_finding_id: "PPT-FN-01, PPT-FN-13, RES-FN-24"}
  - {q: "Q2 Receivables >6m and unbilled inside other current assets Rs2,147.96 Cr (+317.31 H1)?", from_finding_id: "RES-FN-05, PPT-FN-12, RES-FN-22"}
  - {q: "Q3 Which subsidiary earns most of the Rs126.20 Cr C-minus-S PAT; parent margin on sales to it?", from_finding_id: "RES-FN-04, RES-FN-09, RES-FN-22"}
  - {q: "Q4 Is the >=80% guide on consolidated FY26 Rs4,949.27 Cr (H2 YoY +46.69%); is Q3 below Q2 Rs2,541.79 Cr? Y/N", from_finding_id: "RES-FN-10, PPT-FN-02"}
  - {q: "Q5 Which defence-consolidation CPs open at 30-Sep; Rs90 Cr HASPL deployed by 31-Dec-2026? Y/N", from_finding_id: "RES-FN-12, MA-FN-01, MA-FN-10, RES-FN-02"}
  - {q: "Q6 Aerospace acquisition consideration; target revenue, PAT, net debt/cash, ROCE; customers and tenure behind ~Rs1,600 Cr book?", from_finding_id: "A5-M5, PPT-FN-07, PPT-FN-09, MA-FN-01, RES-FN-12"}
  - {q: "Q7 Which quarter does Turnkey result reach zero (Q2 loss Rs122.58 Cr)?", from_finding_id: "RES-FN-20"}
  - {q: "Q8 Q2 export OFC revenue to hyperscalers in Rs Cr?", from_finding_id: "PPT-FN-05"}
  - {q: "Q9 Full warrant conversion and Rs416.25 Cr receipt before 25-Nov-2027? Y/N and quarter", from_finding_id: "RES-FN-18, MA-FN-03, MA-FN-04, PPT-FN-14"}
  - {q: "Q10 Turnkey liabilities -185.25 QoQ: advances consumed vs payables paid?", from_finding_id: "RES-FN-20"}
  - {q: "Q11 How much Q2 revenue was Q1-built subsidiary stock (~Rs43 Cr inventory release at cost)?", from_finding_id: "RES-FN-06"}
  - {q: "Q12 Name the aerospace target(s); does Rs28,911 Cr book include its ~Rs1,600 Cr? Y/N", from_finding_id: "PPT-FN-09, PPT-FN-13"}
  - {q: "Q13 Rs Cr of Rs500 Cr FY27 defence aspiration that depends on the acquisition closing in FY27?", from_finding_id: "RES-FN-11, PPT-FN-07, RES-FN-21"}
  - {q: "Q14 Target defence book ~2,000 to ~1,600: executed vs cancelled?", from_finding_id: "PPT-FN-08"}
  - {q: "Q15 Debt/accruals/warrant split of Rs1,800 Cr + Rs230 Cr capex; FY27 capex?", from_finding_id: "RES-FN-14, PPT-FN-11"}
  - {q: "Q16 FY27 export guide >70% or 65%+; is 63% Q2 or H1?", from_finding_id: "PPT-FN-06, PPT-FN-05"}
  - {q: "Q17 Order book executing in FY27 and FY28, Rs Cr each?", from_finding_id: "RES-FN-13, PPT-FN-05, PPT-FN-09"}
  - {q: "Q18 Is >27% FY29 EBITDA target incl. other income? Y/N", from_finding_id: "PPT-FN-03, PPT-FN-04"}
  - {q: "Q19 OF 33.9 / OFC 42.36 mn fkm by Dec-2026? Y/N", from_finding_id: "PPT-FN-10"}
  - {q: "Q20 Buyer of held-for-sale group (net Rs41.26 Cr); group entity?", from_finding_id: "RES-FN-01"}
  - {q: "Q21 Item behind ~Rs30.6 Cr other-equity debit in H1?", from_finding_id: "RES-FN-03"}
  - {q: "Q22 Source and end-year of recurring deferred-tax credit (Rs7.49 Cr Q2)?", from_finding_id: "RES-FN-16"}
  - {q: "Q23 Which investment drove Q1 consolidated OCI +74.49 and Q2 -13.71; valuation basis?", from_finding_id: "RES-FN-17"}
  - {q: "Q24 Products in Rs407.48 Cr intangibles under development; capitalisation quarter?", from_finding_id: "RES-FN-23"}
  - {q: "Q25 QIP-funded R&D payroll expensed or capitalised?", from_finding_id: "MA-FN-07"}
  - {q: "Q26 Remaining Rs24.27 Cr QIP R&D used by 31-Mar-2027? Y/N", from_finding_id: "MA-FN-06, MA-FN-08"}
  - {q: "Q27 QIP money moved to CC account in Q1 FY27 and balance left there?", from_finding_id: "MA-FN-05"}
  - {q: "Q28 Rs10.30 Cr FD matured 09-Oct-2026: re-deposited or spent; LCs secured by Rs21.22 Cr FD?", from_finding_id: "MA-FN-09"}
  - {q: "Q29 Item-wise use of Rs93 Cr QIP GCP (Q4 FY26)?", from_finding_id: "MA-FN-11"}
  - {q: "Q30 Rs175 Cr to HFCL Technologies as equity or loan; preform at cost-plus to parent?", from_finding_id: "MA-FN-13"}
  - {q: "Q31 Why circular resolution for Rs90 Cr extension; Reg 32 statement to audit committee? Y/N", from_finding_id: "MA-FN-02, MA-FN-10"}
  - {q: "Q32 Any 19-Oct board item besides results? Y/N", from_finding_id: "RES-FN-24"}
  - {q: "Q33 FY of Rs10,000 Cr milestone; is Rs500 Cr defence a forecast?", from_finding_id: "RES-FN-15"}
  - {q: "Q34 Promoter pledge zero at 30-Sep-2026? Y/N", from_finding_id: "Notion Q1 Q12 carry-forward"}
  - {q: "Q35 Planned FY27 defence investment beyond Rs279.91 Cr net segment assets?", from_finding_id: "RES-FN-21"}
  - {q: "Q36 Para 7 subsidiaries: H1 CFO and receivable from HFCL (NPAT 186.19; cash balances fell 0.29)?", from_finding_id: "RES-FN-28"}
  - {q: "Q37 Q2 PCS/DC connectivity revenue and order book, Rs Cr?", from_finding_id: "RES-FN-29, PPT-FN-19"}
  - {q: "Q38 'Secured raw materials': suppliers, volume, tenor, fixed or market price?", from_finding_id: "PPT-FN-17"}
  - {q: "Q39 Q2 OFC realisation per fkm vs Q1; share of volume on long-term contracts below spot?", from_finding_id: "PPT-FN-18"}
  - {q: "Q40 '#1 in OFC': India or global; source and share %?", from_finding_id: "PPT-FN-20"}
  - {q: "Q41 Q2 BharatNet III revenue and remaining BharatNet book, Rs Cr?", from_finding_id: "PPT-FN-21"}
  - {q: "Q42 Advance tax due in H2 FY27 (H1 charged 243.29, paid 119.89)?", from_finding_id: "A5-M4"}
monitorables:
  - {item: "Role 5 addendum: call silence on ageing/unbilled (tripwire #4)", implied_date: "pending", source_ref: "Step 6C; PPT-FN-12"}
  - {item: "Rs90 Cr HASPL investment deployed", implied_date: "2026-12-31", source_ref: "M-L1095-1108, M-L1166-1167"}
  - {item: "Aerospace acquisition completion with consideration and target financials filed", implied_date: "2026-12-31", source_ref: "R-L754; Step 6E"}
  - {item: "Nivetti completion (possible link, INFERENCE)", implied_date: "2026-12-31", source_ref: "Notion memory"}
  - {item: "OF 33.9 / OFC 42.36 mn fkm interim step", implied_date: "2026-12", source_ref: "Notion memory; PPT-FN-10"}
  - {item: "Payment of Rs123.40 Cr H1 unpaid current tax", implied_date: "H2 FY27 (remaining advance-tax instalments by year-end, INFERENCE)", source_ref: "R-L820, R-L966, R-L933"}
  - {item: "Q3 FY27 Telecom Products revenue vs 2,321.98 bull / 2,006.15 bear; first exceptional item; entity addition", implied_date: "Q3 results, date not filed", source_ref: "Step 8C; R-L839"}
  - {item: "Strategic-options outcome", implied_date: "undated", source_ref: "P-L124-129"}
  - {item: "Held-for-sale disposal completion", implied_date: "undated", source_ref: "R-L917, R-L937"}
  - {item: "FY27 revenue >= 8,908.69 consolidated (>=80%)", implied_date: "2027-03-31", source_ref: "R-L700, R-L743"}
  - {item: "Defence revenue ~Rs500 Cr", implied_date: "2027-03-31", source_ref: "R-L709-710; P-L123"}
  - {item: "Exports 65%+ / >70%; ~90% product revenue", implied_date: "FY27", source_ref: "P-L502-508"}
  - {item: "QIP R&D Rs24.27 Cr used", implied_date: "2027-03-31", source_ref: "M-L563-565"}
  - {item: "FY27 year-end CFO after advance tax and ageing disclosure", implied_date: "Q4 FY27 results, date not filed", source_ref: "Part 1 Step 5D"}
  - {item: "Defence facility Rs15 Cr first tranche", implied_date: "2027-09-30", source_ref: "M-L1088-1089"}
  - {item: "Rs215 Cr DC-connectivity facility", implied_date: "2027-09", source_ref: "Notion memory; PPT-FN-11"}
  - {item: "Warrant conversion, Rs416.25 Cr", implied_date: "~2027-11-25 (computed)", source_ref: "M-L1056-1058; R-L869"}
  - {item: "Preferential WC Rs140 Cr, GCP Rs100 Cr, defence Rs35 Cr", implied_date: "FY28", source_ref: "M-L1090-1091, M-L1148-1155"}
  - {item: "Preform Rs175 Cr via HFCL Technologies", implied_date: "2028-07-31", source_ref: "M-L1085-1086"}
  - {item: "OF 43.1 / OFC 62 mn fkm", implied_date: "2028-07", source_ref: "P-L428-434"}
  - {item: "Preform 600 MT, Rs1,250 Cr", implied_date: "2028-10", source_ref: "P-L436-442"}
  - {item: "EBITDA >27%; Rs10,000 Cr before FY29", implied_date: "FY29", source_ref: "P-L503-504; R-L747-748"}
  - {item: "MMHG Phase-1 Rs230 Cr; AP ammunition and MP preform facilities", implied_date: "undated", source_ref: "P-L436-439; R-L779-780"}
  - {item: "Order book Rs28,911 Cr visibility 6-7 years", implied_date: "FY27 to ~FY33-34", source_ref: "R-L681, R-L697"}
  - {item: "Unquantified claims to baseline: OFC/DC strengthen (M08), secured raw materials (PM02), value realization (PM03), WC easing (PM05)", implied_date: "undated", source_ref: "RES C13; PPT C-18 to C-20"}
  - {item: "Operator ruling: Promoter Verdict CONCERN toward AVOID (slip #5)", implied_date: "operator", source_ref: "Notion memory"}
flags:
  - "Trigger #6 proximity: deck 'evaluating various strategic options' (P-L127); not fired"
  - "Tripwire #4 at risk: ageing/unbilled undisclosed; other current assets +317.31; decided by Role 5 addendum"
  - "HASPL Rs90 Cr object missed 30-Sep-2026; extended to 31-Dec-2026 by circular resolution; slip-log ruling operator-only"
  - "Acquisition unpriced: target, consideration, target PAT NOT FOUND; multiple NOT COMPUTABLE; 86.5% of defence book in unowned entity; no accretion credited"
  - "Cash quality: H1 CFO includes Rs123.40 Cr current tax charged not paid; CFO/PAT 0.71 reported vs 0.52 cons / 0.30 SA tax-accrual"
  - "Turnkey loss 122.58 above Rs80-90 Cr guide (memory); H1 loss 210.11 > FY26 full year"
  - "S/C PAT gap 47.09% (Q1 37.07%); 31.30% of PAT on single joint auditor review; that pool's cash balances fell 0.29 and its CFO is NOT FOUND (RES-FN-28)"
  - "Notion projections stale on upside vs old base; H1 only AT new guide on run-rate; guide implies H2 YoY +46.69%; re-base at /fttcp and Role 1"
  - "Guide basis unstated: consolidated reading allows H2 12.43% below Q2"
  - "Disclosure pattern: targets raised, dated milestones dropped, qualitative claims with no metric (M08, PM02-PM05)"
  - "Memory corrections: warrant balance 416.25 not 412.5; FII+DII 27.62% not 18.54%; HFCL Technologies is a WOS, not HTL Limited"
  - "Tracker rows not supplied; OR-17 three-signal floor untested"
  - "Role 5 pending; Role 4 Steps 6.5 and 7 and Role 5 Step 8D deferred (OR-30)"
plain_language_brief_included: true
analyst_note: "P&L strength is real: core PBT grew faster than reported PBT, gross margin is flat, and the margin gain is operating leverage carried by Telecom Products at 30.85%. H1 sits at the new 80% guide on run-rate, not above it; the guide lets H2 grow 46.69%. Cash is weaker than reported: Rs123.40 Cr of H1 current tax was charged but unpaid, so CFO/PAT is 0.52, not 0.71, once tax is counted. The para 7 subsidiaries' cash fell 0.29, but their CFO is not filed, so profit-to-cash for that pool is unknown, not zero; Q36 separates the three readings. The defence acquisition is unpriced; no accretion is credited. Governance and disclosure hold the verdict at PROCEED WITH FLAGS: strategic-options language near trigger #6, ageing withheld again (tripwire #4 turns on the call), HASPL slip. Scoring is filings-only; the Role 5 addendum must re-mark 57 questions."
review_path: "runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md (single document; this agent wrote Part 1 to that path and Part 2 to review_hfcl_q2fy27.part2.md for the orchestrator to join)"
loop_iteration: 2
```

---

## LOOP 1 CHANGE LOG

| A5 item | Change | Where |
|---|---|---|
| F1 (FACTUAL) | Step 3A consolidated Q1 FY27 OCI now reads +74.49 pre-tax items not reclassified (R-L823) / +72.16 total OCI after tax (R-L826). The standalone 74.24 moved to Step 3B, labelled standalone. Q23 updated to 74.49 | Part 1 Step 3A, 3B; Part 2 Q23 |
| C1 (CONTRADICTION) | Step 2D answer 1 restated: H1 is AT the new guide on run-rate (H1 x 2 8,913.54 vs 8,908.69); guide implies H2 YoY +46.69% vs H1 +132.81%; H1 runs far above the old Notion base only. Step 6A revenue row now "ABOVE BASE; AT GUIDE". Step 0G, 6.5, 8A-W, Q4, Key Notes, flags, brief aligned | Part 1 Step 2D, 0G; Part 2 Steps 6A, 6.5, 8A-W, 8.5, 9, verdict card, brief |
| M4 (MISSING) | Tax-accrual cash reading added beside the reported one: current tax 243.29 charged vs 119.89 paid; 123.40 unpaid; balance sheet net +123.41. CFO/PAT 0.71 reported vs 0.52 consolidated / 0.30 standalone; FCF 6.12 vs (117.28) consolidated. Pillar 2 flag and the 0.65 marker statement carry both readings. 6B G3 and AR-2 qualified. Q42 added. Q4 FY27 forward fork names the tax driver. Add-back tightener (g) added | Part 1 Step 5A, 5B, 5D; Part 2 Steps 6B, 6.5, 7, 8B, 8.5, monitorables M6/M14, verdict card, brief |
| M5 (MISSING) | Step 6E acquisition-economics probe added: target, consideration and target financials NOT FOUND; multiple NOT COMPUTABLE; 86.5% of the ~1,850 defence book in the unowned entity; no accretion credited. Core Q6 asks price and target financials. 31-Dec bull fork now needs a filed price and target profit. Add-back tightener (e) carries the same condition | Part 2 Steps 6D, 6E, 7, 8A-W, 8B, 8.5 Q6, monitorables M3, brief part 5 |
| M3 and A2 rows | M01-M08 and PM01-PM07 listed and cited in a preamble table and in body steps; ledger row counts 1,515 / 431 / 411 | Part 1 preamble, 0C, 0D, 0F, 0G; Part 2 Steps 6B, 6D, monitorables M25 |
| New A3 findings | RES-FN-28 -> Step 5C, Q36; RES-FN-29 -> Q37; PPT-FN-17 -> Q38; PPT-FN-18 -> Q39; PPT-FN-19 -> Q37; PPT-FN-20 -> Q40; PPT-FN-21 -> Q41 and 6B item 6. Coverage now 54 of 54 | Part 1 5C; Part 2 8.5B, 8.5C |
| Question renumbering | Old core Q6-Q8 are now Q7-Q9; old extended Q9-Q34 are now Q10-Q35; new Q36-Q42 | Part 2 Step 8.5 |
| C2 (A2 pointers) | Preamble now states the corrected pointers R141 -> R1479, R162 -> R1486 | Part 1 anchor convention |
| S1 | "+14.07%" corrected to "+14.06%" | Part 1 Step 3C |
| S2 | Slide note corrected: 5 slides carry no rows (4, 6, 12, 18, 21) | Part 1 preamble |
| S3 | "Capital advances" labelled INFERENCE from the R-L970 cash-flow label wherever the R-L905 line is cited, including the brief | Part 1 Steps 2D, 5A, 5B, 5D; Part 2 brief part 3 |
| Unchanged | Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION; Decision Status WATCHLIST (no change proposed); branch 8A-W; 6B counts GREEN 5, AMBER 6, RED 5, UNKNOWN 10; "pending Role 5 addendum" markers kept | |

## LOOP 2 CHANGE LOG

| Re-audit item | Change | Where |
|---|---|---|
| L1-F1 (FACTUAL) | The para 7 net cash flow (0.29) (R-L238) is now read as a change in cash balances after investing and financing flows: "cash balances fell 0.29; operating cash flow NOT FOUND". Removed "no cash in H1", "produced no cash", "has not yet shown up as cash anywhere in the group", "added no cash", and the para 8 "turned 46.14 of NPAT into +36.24 of net cash" wording (para 8 now reads "cash rose 36.24"). Added Reading C: profit converted, then spent on non-parent deposits 52.33 (R-L974), net external debt repayment 80.69 (R-L980-981) and capex 55.33 (R-L970-971), not split by paragraph. Q36 still separates the three readings | Part 1 preamble M07 row, Step 0D para 7 and para 8 rows, Step 5C, Step 5D(g); Part 2 Step 7 Strategic Premium row, verdict flag 7, brief part 3, YAML flag, Q36 wording, analyst note |
| L1-S1 | Removed the pointer to a separate Part 2 file from the document text. The header now says Part 2 follows Part 1 directly; the part-file split is stated only as the write method | Part 1 header and end; Part 2 header; review_path |
| L1-S2 | Prior-period tax-accrual cells filled: consolidated CFO (32.63), CFO/PAT (0.77), FCF (229.83); standalone CFO (56.09), CFO/PAT (2.94), FCF (232.59). Change columns filled: consolidated CFO +364.50, CFO/PAT +1.29 (from rounded 0.52 and (0.77); +1.28 unrounded), FCF +112.55; standalone CFO +191.82, CFO/PAT +3.24, FCF (25.50). Step 5D Q1 states the +364.50 vs +498.87 swing | Part 1 Step 5A, 5B, 5D |
| L1-S3 | 5D(f) "deferred tax payment" replaced by "unpaid current tax"; tax rows say "current tax charged but unpaid" | Part 1 Step 5A, 5D; Part 2 flag 5, Key Notes, verdict card |
| L1-S4 | Tax-timing inference narrowed to "falls due under the remaining advance-tax instalments by year-end" | Part 1 Step 5A note; Part 2 Step 7 Pillar 2 row, monitorable M6, YAML monitorable |
| L1-S5 | "43.13" labelled an inventory release at cost (21.47 consolidated less (21.66) standalone change in inventories, R-L809); the Q1 127.61 build labelled at cost as well | Part 1 Step 3A, 3C, 0D answers; Part 2 Step 6.5, Q11 |
| Unchanged | Every other number, status and conclusion. Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION; Decision Status WATCHLIST (no change proposed); branch 8A-W; 42 questions; 54 of 54 coverage; "pending Role 5 addendum" markers kept | |
