# MERGE SPEC: Role 5 addendum into work/review_aurum_q2fy27.md (AURUM Q2 FY27)

Author: A4 analyst (claude-opus-5-5), 2026-10-18. merge_state: PENDING MECHANICAL MERGE.
Target file: runs/aurum-q2fy27/work/review_aurum_q2fy27.md (771 lines before the merge).
Rule: Role 4 tables and numbers are not edited. Every change below is an insertion, a replacement of a line that said no concall was on file, or the Step 8.5 block replacement the task asked for. Every changed passage is marked "(Role 5 addendum)".

Operation types:
- REPLACE_SUBSTRING: find FIND (verbatim, occurs once in the file); replace it with REPLACEMENT. Text around it is unchanged.
- REPLACE_LINE: find the one line whose full text equals FIND; replace the whole line with REPLACEMENT.
- REPLACE_BLOCK: from the line that starts with START through the line that starts with END, inclusive; replace with the named file.
- INSERT_AFTER: find the one line that starts with ANCHOR; insert TEXT as new lines directly after it.
- INSERT_BEFORE: find the one line that equals ANCHOR; insert TEXT as new lines directly before it.
All FIND, START, END and ANCHOR strings were checked unique in the 771-line file. Apply in the order listed. No anchor sits inside the U1 block.

Part files (all in runs/aurum-q2fy27/work/role5_parts/):
- 01a_role5_steps0-2.md, 01b_role5_steps3-4.md, 01c_role5_steps5-7.md, 01d_role5_step8-verdict.md: the new ROLE 5 section, in that order.
- 02_step85_replacement.md: the replacement Step 8.5 block.

---

## U1. REPLACE_BLOCK: Step 8.5 (existing table plus ANSWER STATUS column; rows 23-35 added)
START: `## STEP 8.5: QUESTIONS FOR MANAGEMENT (IR email; no concall scheduled in the record)`
END: `Channel recommendation: IR email now, with all 22 questions verbatim.`
REPLACEMENT: the full content of 02_step85_replacement.md.
Note: rows 1-22 keep every original cell verbatim; only the last column is added.

## U2. REPLACE_SUBSTRING: header line 4
FIND: `Role 5 not run: no concall in this run.`
REPLACEMENT:
```
Role 5 run as an addendum on 2026-10-18 (Quarterly Concall Analysis Protocol v1.1; Q2 FY27 call of 16-Oct-2026, machine transcript): see the ROLE 5 section before the PLAIN-LANGUAGE BRIEF (Role 5 addendum).
```

## U3. REPLACE_LINE: header line 5
FIND: `Documents merged: results filing (standalone and consolidated, Reg 33), investor presentation, press release.`
REPLACEMENT:
```
Documents merged: results filing (standalone and consolidated, Reg 33), investor presentation, press release, and (Role 5 addendum) the Q2 FY27 concall transcript (machine transcript; speakers inferred; on any number conflict the filing wins).
```

## U4. INSERT_AFTER: anchor key
ANCHOR: `Anchor key: RES Lnnn`
TEXT:
```
(Role 5 addendum) CALL Lnnn = extracted/aurum-concall-q2fy27-fulltext.md line (machine transcript, inferred speakers; on any number conflict the filing wins); A3C-nn = work/forensics_concall_aurum_q2fy27.md finding.
```

## U5. REPLACE_LINE: prior-quarter questions preamble (corrects "no concall")
FIND: `No Q1 FY27 or Q2 FY27 concall exists in the record. Status is scored against this quarter's three filed documents. EVADED cannot be scored without a live channel.`
REPLACEMENT:
```
Status below is scored against this quarter's three filed documents. (Role 5 addendum) Correction: a Q2 FY27 concall was held on 16-Oct-2026 (CALL L20) and is analysed in the ROLE 5 section. The chairman calls it the 22nd earnings call (CALL L34), so earlier calls exist, but no Q1 FY27 transcript is on file. The call-based status of these 10 questions is in Role 5 Step 3E: 0 answered, 4 partially (Q2, Q3, Q6, Q10), 6 not addressed (Q1, Q4, Q5, Q7, Q8, Q9); the Housing.com base under Q10 was EVADED on a direct question.
```

## U6. REPLACE_LINE: prior-quarter governance line (corrects "without a concall")
FIND: `Governance signal for the Promoter Verdict log: questions 1, 4, 5 and 10 are unaddressed for the second consecutive quarter. Without a concall this is non-disclosure, not evasion. Flag only.`
REPLACEMENT:
```
Governance signal for the Promoter Verdict log: questions 1, 4, 5 and 10 are unaddressed in the filings for the second consecutive quarter. (Role 5 addendum) The Q2 FY27 call did not close them: 1, 4, 5 and 9 stay NOT ADDRESSED, and the Housing.com base under 10 was declined on a direct question, the first evasion on record (Role 5 Step 3E). Flag only.
```

## U7. INSERT_AFTER: Step 6B watchlist item 3 (note row)
ANCHOR: `| 3 | SM-REIT first scheme filed with AUM |`
TEXT:
```
| 3 (Role 5 addendum) | SM-REIT first scheme filed with AUM | Filed in FY27 | 5th consecutive concall unlaunched, no AUM | The Q2 FY27 call (16-Oct-2026) does not mention SM-REIT, AMSA or AUM (A3C-26). It is the 22nd earnings call (CALL L34). Red-threshold count NOT DETERMINABLE: about 14 calls since the June 2023 registration on Reading A, 1 evidenced on Reading B (Role 5 Step 8C). Supersedes "Concall count untestable" in the row above. | RED (unchanged; red-threshold count NOT DETERMINABLE) |
```

## U8. INSERT_AFTER: Step 6C trigger 3 (note row)
ANCHOR: `| 3. 5th consecutive concall with SM-REIT unlaunched`
TEXT:
```
| 3 (Role 5 addendum). 5th consecutive concall with SM-REIT unlaunched and no AUM | 5 concalls | Supersedes the row above. Q2 FY27 call held 16-Oct-2026; SM-REIT, AMSA and AUM not mentioned in CALL L24-L417 (A3C-26). Chairman: "the 22nd earnings call" (CALL L34). Reading A (count from the June 2023 registration, DECK L443): about 14 calls [INFERENCE: one call a quarter]. Reading B (count from the trigger date, on or before 14-Jul-2026): 1 evidenced, at most 2. Separating observation: the operator's start date for the count (Role 5 Step 8C). | NOT DETERMINABLE (FIRED on Reading A; NOT FIRED on Reading B); AVOID unchanged either way; operator rules |
```

## U9. INSERT_AFTER: Step 8 (note)
ANCHOR: `New gate stated explicitly:`
TEXT:
```

(Role 5 addendum) Step 8 after the Q2 FY27 call: proposed Decision Status stays AVOID, no change. Decision Status is the operator's field and is not written. Trigger 3 is NOT DETERMINABLE on the concall count (FIRED on Reading A, NOT FIRED on Reading B; Role 5 Step 8C); either reading leaves AVOID. Re-entry condition 1 is harder on management's own timeline: Housing.com break-even is 4-6 quarters on the internal target (CALL L237), about Q2-Q4 FY28 [INFERENCE], after the earliest pair (Q3 and Q4 FY27). Proposed addition to condition 1: Housing.com's result on a metric management names (Step 8.5 Q23), with any one-time cost of the Rs120 Cr cut shown separately (Q24).
```

## U10. INSERT_AFTER: Step 9 Key Notes
ANCHOR: `- Key Notes line (proposed):`
TEXT:
```
- (Role 5 addendum) Concall Key Notes line and Promoter Verdict log line: see Role 5 Step 9 (Notion payload items). Decision Status: NOT WRITTEN; proposed AVOID, no change.
```

## U11. INSERT_AFTER: MONITORABLES table
ANCHOR: `| M13 | Operator rulings 16, 17, 40 |`
TEXT:
```
| M14 (Role 5 addendum) | Investor connect "next week"; put Q2, Q6, Q8 and Q23 live | about 23-Oct-2026 (possibly misheard) | CALL L413 (C22) |
| M15 (Role 5 addendum) | Q3 FY27 deck: Housing.com line inside Distribution; organic vs synergy slide; current KPIs kept; beds vs 16,502 | Q3 FY27 results, by about 14-Feb-2027 [INFERENCE: Reg 33] | CALL L172, L294-L295, L308-L311; DECK L169 (C06, C07, C08, C12) |
| M16 (Role 5 addendum) | Housing.com Rs120 Cr cost cut visible in Locon cost; one-time cost of the cuts | Q3 FY27 results | CALL L317-L321 (C03) |
| M17 (Role 5 addendum) | Network occupancy 88% target (82% at Q2) | Dec-2026 (Q3) or Mar-2027 (Q4); year undefined | CALL L276-L277; DECK L173 (C11) |
| M18 (Role 5 addendum) | Synergies visible "in the coming two quarters" | by Q4 FY27 results (about 30-May-2027) | CALL L307-L308 (C05) |
| M19 (Role 5 addendum) | Revenue per team member up each quarter; 56 lakh target | each quarter; 56 lakh by Mar-2027 | CALL L69, L323 (C10) |
| M20 (Role 5 addendum) | KuberX disbursal run rate toward Rs25,000 Cr | each quarter; target Q2-Q4 FY28 | CALL L212-L216, L339 (C09) |
| M21 (Role 5 addendum) | Housing.com break-even (internal 4-6 qtrs, external 6-8 qtrs); profitable in 12-18 months; +Rs150 Cr revenue | Q2-Q4 FY28 internal; to Q2 FY29 external; Sep-2027 to Mar-2028 (beyond the 11-month map) | CALL L61, L234-L239, L321 (C01, C02, C04) |
| M22 (Role 5 addendum) | Locon tax-loss opinion; any DTA recognition | undated | CALL L378-L385 (C15) |
| M23 (Role 5 addendum) | Rent and education payments restart (Housing.com and NestAway) | undated | CALL L341-L342 (C14) |
| M24 (Role 5 addendum) | Channel partners to 50,000; developers to 4,000+ | undated | CALL L361, L363 (C18) |
| M25 (Role 5 addendum) | No inorganic deal "in a short run" | undated (standing) | CALL L333-L334 (C13) |
| M26 (Role 5 addendum) | Operator ruling: trigger 3 count basis (Reading A vs Reading B) | pending | Role 5 Step 8C |
| M27 (Role 5 addendum) | Q3 FY27 concall: first scored promise-vs-delivery; credibility ratio and 6E archetype first computed | about Feb-2027, with Q3 results [INFERENCE] | Role 5 Step 3B, baseline promise log |
```

## U12. INSERT_AFTER: FLAGS list
ANCHOR: `16. FLAG-DEFERRED (OR-30):`
TEXT:
```
17. FLAG-TRIGGER-3-COUNT (Role 5 addendum): SM-REIT not mentioned on the 22nd earnings call (CALL L34; A3C-26). Count basis NOT DETERMINABLE: about 14 calls since the June 2023 registration on Reading A (FIRED), 1 evidenced on Reading B (NOT FIRED). Separating observation: the operator's start date for the count. AVOID unchanged either way; the operator rules.
18. FLAG-OI-CLAIM-CONTRADICTED (Role 5 addendum): the call says other income is "mainly treasury and deposit income" (CALL L138); the H1 filing shows at least 51.9% one-time gains and 28.1% treasury and deposit lines (RES L466-L473).
19. FLAG-HOUSING.COM BREAK-EVEN AFTER THE RE-ENTRY PAIR (Role 5 addendum): internal 4-6 quarters, external 6-8 quarters (CALL L237-L238), about Q2-Q4 FY28 on the internal tier [INFERENCE]; base financials declined (CALL L222-L223); Rs120 Cr cut with no stated one-time cost (CALL L318).
20. FLAG-CONCALL NON-ANSWERS (Role 5 addendum): of the 22 Step 8.5 questions, 0 answered, 9 partially, 13 not addressed; of the 10 Q1 FY27 questions, 0 answered, 4 partially, 6 not addressed; Housing.com base EVADED on a direct question (first evasion on record).
21. FLAG-CALL-VS-DECK CONFLICTS (Role 5 addendum): "increasing operating leverage" vs a falling QoQ margin; beds "growing ... by 20 to 30%" vs deck -14% YoY; 45m monthly visits relabelled as monthly active users (Role 5 Step 7A rows 4, 32, 35).
22. FLAG-LEASE-CASH LINE (Role 5 addendum): H1 FY27 "Repayment of lease liability, net of interest" Rs47.77 Cr with interest paid Rs0.02 Cr, while Rs13.23 Cr of finance cost is added back in OCF (RES L464, L501-L502); the call's "covered ... full lease commitments" holds by Rs4.31 Cr on one reading only.
23. FLAG-TAX LOSSES (Role 5 addendum): Locon carry-forward losses of 1,020 Cr, use "yet to be seen" (CALL L378-L383); any later DTA recognition is non-cash PAT.
24. FLAG-NOTION GOODWILL BASELINE STALE (Role 5 addendum, A3C-15): the call's 1,020 Cr is filed total equity Rs1,019.64 Cr (RES L433); the Notion "Rs174.25 Cr = 61% of NW" line implies about Rs285.66 Cr and fits a pre-FY26 balance sheet [INFERENCE]; re-basing item 7 and trigger 4 is the operator's call.
25. FLAG-KUBERX (Role 5 addendum): new home-loan distribution line; 10.4x run-rate target in 4-6 quarters on one month of data; entity and segment unnamed (CALL L212-L216, L338).
26. FLAG-HEDGE-HEAVY CALL (Role 5 addendum): 27 defensive phrases, 16 of them "we believe"; specificity 0.31 on the statement basis; credibility ratio ND; archetype NOT CLASSIFIABLE.
27. FLAG-MACHINE TRANSCRIPT (Role 5 addendum): faster-whisper transcript, speakers inferred, CFO listed but silent; every call figure yields to the filing.
```

## U13. INSERT_AFTER: protocol verdict
ANCHOR: `Protocol verdict: PROCEED WITH FLAGS.`
TEXT:
```

(Role 5 addendum) Role 5 does not change the protocol verdict: PROCEED WITH FLAGS stands. The call adds no evidence that resolves cash conversion (INDETERMINATE-WITH-DIRECTION; the lease-interest cash line is ambiguous, Role 5 Step 7A row 25), so the PROCEED WITH CAVEATS ceiling holds. Trigger 1 stays FIRED; trigger 3 is NOT DETERMINABLE. No mechanical failure: all 65 turns and 341 rows reconciled, and every concall FORWARD-SIGNAL and AMBIGUOUS finding has a question.
```

## U14. INSERT_BEFORE: the new ROLE 5 section
ANCHOR (whole line): `## PLAIN-LANGUAGE BRIEF`
TEXT: the content of 01a_role5_steps0-2.md, then 01b_role5_steps3-4.md, then 01c_role5_steps5-7.md, then 01d_role5_step8-verdict.md, then these three lines:
```

---

```
Result: FLAGS and the protocol verdict, then `---`, then the ROLE 5 section, then `---`, then `## PLAIN-LANGUAGE BRIEF`.

## U15. INSERT_AFTER: brief part 1, summary narrative
ANCHOR: `On the bull side, the share issues priced Aurum at Rs231.42`
TEXT:
```
(Role 5 addendum) Management held its Q2 call on 16 October [MGMT-CALL*]. It added targets for Housing.com and a new home-loan line, but gave no Housing.com base numbers and did not mention the SM-REIT. Nothing on the call moves AVOID.

* MGMT-CALL: machine transcript, inferred speakers; on any number conflict the filing wins.

### 1A. WHAT MANAGEMENT SAID ON THE CALL (Role 5 addendum)
- Housing.com: management cut about Rs120 Cr of cost in the first week [MGMT-CALL*, CALL L318]. It expects Rs150 Cr more revenue over 4-6 quarters [MGMT-CALL*, CALL L321]. Its break-even target is 4-6 quarters internally and 6-8 quarters externally [MGMT-CALL*, CALL L237-L238]. It would not give Housing.com's current numbers [MGMT-CALL*, CALL L222-L223].
- That timeline matters. The earliest pair of quarters that could lift AVOID is Q3 and Q4 FY27. Management expects Housing.com to lose money through both [INFERENCE].
- KuberX is a new home-loan sourcing line. It sourced Rs200 Cr of loans in September [MGMT-CALL*, CALL L212]. Management targets a Rs25,000 Cr yearly run rate in 4-6 quarters, at a 1-1.2% bank commission [MGMT-CALL*, CALL L216, L338]. No filing shows it yet.
- From Q3, Housing.com sits inside the Distribution segment, not in its own segment [MGMT-CALL*, CALL L172].
- Rental: management says the bed cuts are over and beds will grow. Occupancy is 82%, with an 88% target "by the end of this year" [MGMT-CALL*, CALL L270-L277].
- Tax: Housing.com brings Rs1,020 Cr of tax losses. Management does not yet know how much the group can use [MGMT-CALL*, CALL L378-L383].
- Not mentioned: the SM-REIT, the split of other income, the Rs9.52 Cr loan, receivables ageing, the EPS share count [CALL L24-L417].
- Of the 22 open questions from the filing review, the call fully answered none, partly answered 9 and left 13 untouched [Role 5 Step 8.5].

### 1B. MANAGEMENT SAID VS FILING SHOWS (Role 5 addendum)
- Said: other income is "mainly treasury and deposit income" (CALL L138). Filing: in H1, at least 51.9% of other income was one-time gains, and treasury and deposit lines were 28.1% [FILED, derived; RES L466-L473].
- Said: "increasing operating leverage" (CALL L91). Filing: operating EBITDA margin fell from 27.12% to 26.01% QoQ [FILED, derived].
- Said: "fourth consecutive profitable quarter" (CALL L45). Filing: Q2 PBT of Rs6.82 Cr is below other income of Rs7.12 Cr, and core PBT ex-OI was Rs(0.52) Cr [FILED, derived].
- Said: beds grew 20-30% a year apart from one exit (CALL L267). Deck: beds fell 14% YoY [MGMT; DECK L169].
- Said: 45 million monthly active users (CALL L109). Deck: 45 million monthly visits [MGMT citing Sensortower; DECK L374, L382].
- Said: operating cash "covered ... full lease commitments" (CALL L165). Filing: true by Rs4.31 Cr only if the lease-repayment line includes interest [FILED, derived; RES L501-L502].
- Said: equity "roughly doubled to 1,020 crore" (CALL L150). Filing: total equity Rs1,019.64 Cr against Rs510.06 Cr. Confirmed. The Notion "61% of net worth" line rests on an older balance sheet [INFERENCE; Role 5 Step 7D].
- Every rupee figure read from the statements on the call ties to the filing. The gaps sit in the claims around them [Role 5 Step 7A].
```

## U16. INSERT_AFTER: brief part 2, sector
ANCHOR: `- Not disclosed in any filing this quarter: market share`
TEXT:
```
- (Role 5 addendum) On the call, management said developers spend more on marketing in a slowdown, which helps platforms, and that it has "not seen dip for last several quarters" [MGMT-CALL*, CALL L198, L204]. It cited an unnamed listed portal as EBITDA positive [MGMT-CALL*, CALL L243-L244; PENDING LIVE VERIFICATION]. No peer call was passed to this run.
```

## U17. INSERT_AFTER: brief part 3, business model
ANCHOR: `- Not disclosed: revenue by brand`
TEXT:
```
- (Role 5 addendum) The call adds a new earnings line: KuberX earns a 1-1.2% bank commission on the home loans it sources [MGMT-CALL*, CALL L338]. Its segment is not named; it runs inside the PropTiger team [MGMT-CALL*, CALL L215]. Management says revenue per team member rose from about 40 lakh to 50+ lakh, mostly through cost cuts [MGMT-CALL*, CALL L323-L324]. The AI consumer journey shows no tangible result yet [MGMT-CALL*, CALL L324].
```

## U18. INSERT_AFTER: brief part 4, competition
ANCHOR: `- No peer or competitive data was in prior Notion work`
TEXT:
```
- (Role 5 addendum) Housing.com's lead over its nearest rival is 1.2x on monthly visits, per the deck's Sensortower figure [MGMT; DECK L374-L375, L382]. On the call, the same 1.2x was attached to monthly active users, a different measure [MGMT-CALL*, CALL L109]. An analyst named Square Yards' mortgage arm as the model for KuberX (CALL L208-L210). Peer concalls: UNVERIFIABLE this run.
```

## U19. INSERT_AFTER: brief part 5, make-or-break bear fork
ANCHOR: `- Bear fork: a third loss in a row`
TEXT:
```
- (Role 5 addendum) The call makes the bull fork harder: management's own internal Housing.com break-even target is 4-6 quarters, so Housing.com is expected to lose money in Q3 [MGMT-CALL*; INFERENCE].
```

## U20. INSERT_AFTER: brief part 5, concall catalysts
ANCHOR: `- Locon PPA final (by 29-Sep-2027).`
TEXT:
```

Concall catalysts (Role 5 addendum) [MGMT-CALL*]:
- Investor connect "next week" (about 23-Oct-2026, possibly misheard). Bull: Housing.com numbers and the Rs9.52 Cr borrower given. Bear: no connect, or the same silence.
- Q3 FY27 results and deck (by about 14-Feb-2027). Bull: a Housing.com line inside Distribution, the organic vs synergy slide, beds above 16,502, and the Rs120 Cr cut visible with its one-time cost shown. Bear: Housing.com folded in with no split, KPIs dropped, a buried one-time charge.
- Occupancy target of 88% (Dec-2026 or Mar-2027). Bull: 88% reached with beds growing. Bear: occupancy stays near 82%, or rises only because beds shrink.
- Synergies "in the coming two quarters" and revenue per team member at 56 lakh (Q4 FY27 results, by about 30-May-2027). Bull: a filed synergy figure and a defined metric. Bear: no synergy figure; the metric moves only on headcount.
- KuberX run rate (each quarter, target Q2-Q4 FY28). Bull: disbursals rise toward Rs25,000 Cr a year, with revenue in a named segment. Bear: no monthly data, or revenue hidden inside Distribution.
- Housing.com break-even, internal 4-6 quarters (about Q2-Q4 FY28, beyond this map). Bull: losses shrink each quarter from Q3. Bear: the target slides to the 6-8 quarter external tier.
```

## U21. Closing YAML of the review (substring edits and insertions)

U21a. INSERT_AFTER
ANCHOR: `loop_iteration: 2`
TEXT:
```
role5_addendum: "2026-10-18; Q2 FY27 concall of 16-Oct-2026 (machine transcript); block work/blocks/a4-role5.yaml"
```

U21b. REPLACE_SUBSTRING
FIND: `docs_merged: [results, presentation, pressrelease]`
REPLACEMENT: `docs_merged: [results, presentation, pressrelease, concall]`

U21c. REPLACE_LINE
FIND: `  turns: 0`
REPLACEMENT: `  turns: 65`

U21d. REPLACE_SUBSTRING
FIND: `A3-13, A3-14]`
REPLACEMENT: `A3-13, A3-14, A3C-01, A3C-02, A3C-03, A3C-04, A3C-05, A3C-06, A3C-07, A3C-08, A3C-09, A3C-10, A3C-11, A3C-12, A3C-13, A3C-14, A3C-15, A3C-16, A3C-17, A3C-18, A3C-19, A3C-20, A3C-21, A3C-22, A3C-23, A3C-24, A3C-25, A3C-26, A3C-27, A3C-28, A3C-29, A3C-30, A3C-31]`

U21e. INSERT_AFTER (questions_for_management)
ANCHOR: `  - {q: "Q2 FY26 capitalised development amount, capitalisation policy, amortisation inside D&A`
TEXT:
```
  - {q: "(Role 5) Housing.com target metric (EBITDA or PBT before/after PPA amortisation), start quarter of the 4-6 / 6-8 quarter count, and FY26 / Q2 FY27 base result", from_finding_id: "A3C-03"}
  - {q: "(Role 5) Rs120 Cr Housing.com cut: annual or cumulative; one-time cost, quarter and P&L line; pre-deal cost base", from_finding_id: "A3C-04"}
  - {q: "(Role 5) Q3 FY27 deck yes/no: Housing.com line inside Distribution; organic vs synergy slide; Distribution YoY ex-PropTiger and ex-Housing.com; current KPIs kept", from_finding_id: "A3C-05, A3C-06, A3C-27"}
  - {q: "(Role 5) Where is H1 FY27 lease interest paid; does the Rs47.77 Cr lease repayment line include it", from_finding_id: "A3C-08"}
  - {q: "(Role 5) KuberX legal entity and segment; gross vs net take rate; Q2 revenue; Oct and Nov disbursals; replaces SM-REIT as Capital engine?", from_finding_id: "A3C-09, A3C-22"}
  - {q: "(Role 5) Define revenue per team member (revenue and headcount basis); Q2 and Q3 values with and without Housing.com", from_finding_id: "A3C-10"}
  - {q: "(Role 5) Locon Rs1,020 Cr losses: type, expiry, change-of-ownership limits; merger plan; unrecognised DTA at 30-Sep-2026", from_finding_id: "A3C-12"}
  - {q: "(Role 5) Goodwill by CGU at Mar-26 (Rs207.17 Cr) and Sep-26 (Rs549.45 Cr); amount in negative-net-worth subsidiaries; Locon goodwill in Distribution or unallocated", from_finding_id: "A3C-15, A3C-16"}
  - {q: "(Role 5) Housing.com MAU vs visits with source and period; competitor basis for 1.2x", from_finding_id: "A3C-18"}
  - {q: "(Role 5) 88% occupancy target date; beds and signed units by brand for Q2 FY26, Q1 FY27, Q2 FY27; Mar-2027 bed target", from_finding_id: "A3C-19"}
  - {q: "(Role 5) Confirm the +1270 bps PBT margin base includes discontinued operations", from_finding_id: "A3C-20"}
  - {q: "(Role 5) Integration subcommittee members, independents, terms of reference, first report date, formal status", from_finding_id: "A3C-23"}
  - {q: "(Role 5) Calls since June 2023 SM-REIT registration that stated a launch date or AUM; FY27 scheme plan and entity", from_finding_id: "A3C-26"}
```

U21f. INSERT_AFTER (monitorables)
ANCHOR: `  - {item: "Operator rulings 16, 17, 40", implied_date: "pending"`
TEXT:
```
  - {item: "(Role 5) Investor connect next week; put Q2, Q6, Q8, Q23 live", implied_date: "~2026-10-23 (possibly misheard)", source_ref: "CALL L413"}
  - {item: "(Role 5) Q3 FY27 deck: Housing.com line in Distribution; organic vs synergy slide; KPIs kept; beds vs 16,502", implied_date: "Q3 FY27 results, by ~2027-02-14", source_ref: "CALL L172, L294-L295, L308-L311; DECK L169"}
  - {item: "(Role 5) Rs120 Cr Housing.com cut visible; one-time cost", implied_date: "Q3 FY27 results", source_ref: "CALL L317-L321"}
  - {item: "(Role 5) Occupancy 88% target (82% at Q2)", implied_date: "Dec-2026 or Mar-2027 (undefined)", source_ref: "CALL L276-L277; DECK L173"}
  - {item: "(Role 5) Synergies visible in two quarters", implied_date: "by Q4 FY27 results, ~2027-05-30", source_ref: "CALL L307-L308"}
  - {item: "(Role 5) Revenue per team member up QoQ; 56 lakh", implied_date: "each quarter; 56 lakh by 2027-03-31", source_ref: "CALL L69, L323"}
  - {item: "(Role 5) KuberX run rate toward Rs25,000 Cr", implied_date: "each quarter; target Q2-Q4 FY28", source_ref: "CALL L212-L216, L339"}
  - {item: "(Role 5) Housing.com break-even internal 4-6 / external 6-8 qtrs; profitable 12-18 months; +Rs150 Cr revenue", implied_date: "Q2-Q4 FY28 internal; to Q2 FY29 external", source_ref: "CALL L61, L234-L239, L321"}
  - {item: "(Role 5) Locon tax-loss opinion; DTA recognition", implied_date: "undated", source_ref: "CALL L378-L385"}
  - {item: "(Role 5) Rent and education payments restart", implied_date: "undated", source_ref: "CALL L341-L342"}
  - {item: "(Role 5) Channel partners 50,000; developers 4,000+", implied_date: "undated", source_ref: "CALL L361, L363"}
  - {item: "(Role 5) No inorganic deal in the short run", implied_date: "undated (standing)", source_ref: "CALL L333-L334"}
  - {item: "(Role 5) Operator ruling on trigger 3 count basis", implied_date: "pending", source_ref: "Role 5 Step 8C"}
  - {item: "(Role 5) Q3 FY27 concall: first scored credibility ratio and archetype", implied_date: "~2027-02, with Q3 results", source_ref: "Role 5 Step 3B"}
```

U21g. INSERT_AFTER (flags)
ANCHOR: `  - "FLAG-DEFERRED (OR-30): Steps 6.5 and 7 deferred to /fttcp and Role 1"`
TEXT:
```
  - "FLAG-TRIGGER-3-COUNT (Role 5): SM-REIT not mentioned on the 22nd call; count basis NOT DETERMINABLE (about 14 calls since Jun-2023 on Reading A, FIRED; 1 evidenced on Reading B, NOT FIRED); operator rules; AVOID unchanged"
  - "FLAG-OI-CLAIM-CONTRADICTED (Role 5): 'mainly treasury and deposit income' (CALL L138) vs H1 >=51.9% one-time, 28.1% treasury and deposit (RES L466-L473)"
  - "FLAG-HOUSING.COM BREAK-EVEN AFTER RE-ENTRY PAIR (Role 5): internal 4-6 qtrs (~Q2-Q4 FY28), external 6-8 qtrs; base declined; Rs120 Cr cut with no stated one-time cost"
  - "FLAG-CONCALL NON-ANSWERS (Role 5): Step 8.5 rows 1-22: 0 answered, 9 partial, 13 not addressed; Q1 list: 0 / 4 / 6; Housing.com base EVADED"
  - "FLAG-CALL-VS-DECK CONFLICTS (Role 5): operating leverage vs falling QoQ margin; beds +20-30% vs deck -14%; 45m visits relabelled as MAU"
  - "FLAG-LEASE-CASH LINE (Role 5): Rs47.77 Cr 'net of interest' repayment, Rs0.02 Cr interest paid, Rs13.23 Cr finance cost added back; lease-cover claim holds by Rs4.31 Cr on one reading only"
  - "FLAG-TAX LOSSES (Role 5): Locon Rs1,020 Cr losses, use 'yet to be seen'; later DTA recognition would be non-cash PAT"
  - "FLAG-NOTION GOODWILL BASELINE STALE (Role 5, A3C-15): call 1,020 Cr = filed total equity Rs1,019.64 Cr; Notion 61%-of-NW line implies ~Rs285.66 Cr, pre-FY26 basis [INFERENCE]"
  - "FLAG-KUBERX (Role 5): 10.4x run-rate target in 4-6 qtrs on one month; entity and segment unnamed"
  - "FLAG-HEDGE-HEAVY CALL (Role 5): 27 defensive phrases; specificity 0.31; credibility ND; archetype NOT CLASSIFIABLE"
  - "FLAG-MACHINE TRANSCRIPT (Role 5): speakers inferred; CFO listed but silent; filing wins on every number conflict"
```

Unchanged on purpose: every Role 4 table cell and number; protocol_verdict, cash_conversion, decision_status_verified, position_branch, sc_gap_pat_pct and analyst_note in the review YAML (the Role 5 analyst note lives in work/blocks/a4-role5.yaml).

## POST-MERGE CHECKS (for the orchestrator)
1. `grep -c "(Role 5 addendum)"` on the review returns at least 30.
2. The strings "Role 5 not run", "No Q1 FY27 or Q2 FY27 concall exists", "Without a concall this is non-disclosure", "no concall scheduled in the record" and "No concall is on file for Q2 FY27" no longer occur.
3. "## ROLE 5: CONCALL ANALYSIS" occurs once, after "Protocol verdict:" and before "## PLAIN-LANGUAGE BRIEF".
4. The Step 8.5 table has 35 data rows and 8 columns.
5. The review still ends with one fenced YAML block.
