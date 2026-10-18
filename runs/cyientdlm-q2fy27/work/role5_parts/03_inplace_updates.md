# ROLE 5 ADDENDUM: IN-PLACE UPDATE SPEC for work/review_cyientdlm_q2fy27.md
Each item gives the exact FIND anchor in the current review and the action. Unlisted lines stay as they are.

## U1. Header, line 4 (APPEND to the end of the line)
FIND: `Protocol loaded: Quarterly Results Review Protocol v1.4 (Role 4) only. Role 5 not run: the 15-Oct-2026 call transcript is not in this run.`
APPEND: ` (Role 5 addendum, 2026-10-18: Quarterly Concall Analysis Protocol v1.1 (Role 5) now run on the 15-Oct-2026 machine transcript; see the ROLE 5 section. Role 4 tables and numbers are unchanged.)`

## U2. Step 8.5 table (REPLACE)
FIND: the table from the header row `| # | Cat | Question | Why It Matters | Bull Answer | Bear Answer | From finding(s) |` through row `| 30 | A | What was Q2 FY27 revenue from Auto & Others ...` (current lines 531-562).
REPLACE WITH: the full content of `role5_parts/02_step85_table_replacement.md` up to and including row 42.
Then, after the existing "Coverage check (every FORWARD-SIGNAL ..." paragraph (current line 564), INSERT a blank line and the "Coverage check, concall findings (Role 5 addendum): ..." paragraph from the end of the same file.

## U3. Channel recommendation (APPEND to the end of the line)
FIND: `Channel recommendation: the 15-Oct-2026 concall has already occurred. Its transcript is not in this run. First run Role 5 on the transcript and mark each question ANSWERED / PARTIALLY / EVADED / NOT ADDRESSED. Send the remainder by IR email with the questions verbatim.`
APPEND: ` (Role 5 addendum: Role 5 has now run; answer status is in the last column. Send the 19 NOT ADDRESSED and 4 EVADED questions, plus Q31-Q42, by IR email before the Q3 FY27 call.)`

## U4. Monitorables row 1 (APPEND inside the Item cell)
FIND: `| 1 | Role 5 on the Q2 FY27 earnings call transcript (questions answer-status) | now (call held 15-Oct-2026; transcript not in run) | Orchestrator note; Step 8.5 |`
REPLACE: `| 1 | Role 5 on the Q2 FY27 earnings call transcript (questions answer-status) (Role 5 addendum: DONE 2026-10-18; see the ROLE 5 section) | now (call held 15-Oct-2026; transcript not in run) | Orchestrator note; Step 8.5 |`

## U5. Monitorables new rows (INSERT after row 17 `| 17 | Q2 FY28 base effect ...`)
```
| 18 | (Role 5 addendum) Q3 FY27: YoY revenue growth >= 30% (H2 pledge; Q3 FY27 >= 394.29 Cr on the deck Q3 FY26 base) | about mid-Jan 2027 [INFERENCE] | cc L361 (P09, CF23) |
| 19 | (Role 5 addendum) Order intake "600 crores plus" in Q3 and in Q4 FY27 (book walk >= Rs 6,000 Mn each) | Q3 FY27 (mid-Jan 2027); Q4 FY27 (Apr-May 2027) [INFERENCE] | cc L256 (P10, CF10) |
| 20 | (Role 5 addendum) Investment intensity lower: combined employee plus other-expense ratio below Q2's 28.72% | Q3 or Q4 FY27 | cc L295 (P07, CF04) |
| 21 | (Role 5 addendum) No net new S&M cost until quarterly revenue reaches about Rs 7,862 Mn (2x Q2) | every quarter, open-ended | cc L288, L297 (P06, CF05) |
| 22 | (Role 5 addendum) FY27 EBITDA margin 9-10% ("close to around 9%"); at 9% H2 runs about 8.5% [INFERENCE] | Q4 FY27 / FY27 results, about Apr-May 2027 [INFERENCE] | cc L230, L244 (P01, CF01) |
| 23 | (Role 5 addendum) AI data centre and robotics update: position, opportunities, pipeline | Q4 FY27 call, about Apr-May 2027 [INFERENCE] | cc L217, L460-L461 (P15, CF18) |
| 24 | (Role 5 addendum) Semicap growth "every quarter" (amount not disclosed) | from Q3 FY27 | cc L238, L459 (P16, CF18) |
| 25 | (Role 5 addendum) Double-digit EBITDA margin "from the Q1 onwards" (read Q1 FY28) | about late Jul 2027 [INFERENCE] | cc L231 (P03, CF24) |
| 26 | (Role 5 addendum) FY28 EBITDA margin double digits / "10 plus" from backlog alone | FY28 (outside window; Q1 FY28 first read) | cc L266, L476 (P02, CF02) |
| 27 | (Role 5 addendum) B2S: four programmes ~$1 bn enter the order book after design and prototype testing; production FY29, full ramp FY30 | undated / FY29-FY30 (outside window) | cc L309-L310, L409-L411, L428-L429 (P13, P14, CF07, CF08) |
| 28 | (Role 5 addendum) Honeywell build-to-print programme back to serial production | undated | cc L405-L407 (P21, CF21) |
| 29 | (Role 5 addendum) Product development stays fully expensed; any capitalisation is a tripwire | ongoing | cc L199, L389-L391, L473 (P22, CF20) |
| 30 | (Role 5 addendum) Pipeline $1.5 bn unweighted; win ratio ~40%; $400-500 Mn order impact | undated | cc L262, L332, L338 (P12, CF09) |
| 31 | (Role 5 addendum) More US revenue traction; large orders from the new sales team | undated | cc L439, L478-L479 (P18, P20, CF13) |
| 32 | (Role 5 addendum) Growth sustains into FY28 | FY28 | cc L56, L298-L299 (P24) |
```

## U6. Protocol verdict (INSERT a new paragraph after the "Reasons: ..." paragraph, before the `---`)
```
(Role 5 addendum, 2026-10-18) Role 5 does not change the verdict. It stays PROCEED WITH FLAGS. The call adds no mechanical failure: all 97 turns and 303 rows reconcile, and every Role 5 table cell is anchored or ND. Cash conversion stays INDETERMINATE-WITH-DIRECTION (structural). The call gave no CFO figure, no NWC formula and no target, so the cap holds. The protocol override "concall narrative contradicts filing numbers materially" fires on three points: the margin cause, the earnout recurrence and the US arm. The filing is trusted, the credibility issue is noted for Halt 1, and the next-quarter watchlist is tightened (Monitorables 18-32). The credibility ratio and the archetype are ND because this call opens the promise log. Source caveat: machine transcript, inferred speakers; the filing wins on any number conflict.
```

## U7. ROLE 5 section (INSERT)
INSERT the content of `01a_role5_steps0-3.md`, then `01b_role5_steps4-6.md`, then `01c_role5_steps7-9.md`, in that order, after the PROTOCOL VERDICT block's closing `---` and before `## PLAIN-LANGUAGE BRIEF`.

## U8. Plain-language brief: provenance key (APPEND to the end of the line)
FIND: `Provenance key: FILED = this quarter's results filing; MGMT = this quarter's deck or press release; AGENCY = rating agency (via prior Notion); SECONDARY = prior Notion or peer work; INFERENCE = our reasoning. "Prior Notion" marks memory from the Notion page, not this quarter's filings.`
APPEND: ` (Role 5 addendum) CALL = the 15-Oct-2026 earnings call, from a machine transcript with inferred speakers; where CALL and FILED differ, FILED wins.`

## U9. Summary narrative (INSERT these bullets before the bullet `- Verdict: PROCEED WITH FLAGS. The operator decides at Halt 1.`)
```
- (Role 5 addendum) On the 15-Oct call, management guided FY27 EBITDA margin to "close to around 9%", then "9% to 10%" (CALL). It guided FY28 to "double digits" (CALL).
- (Role 5 addendum) It accepted an analyst's 30-35% FY27 revenue growth figure. It said H2 growth will "definitely" exceed 30% (CALL).
- (Role 5 addendum) At 9%, the H2 margin must fall to about 8.5%, below Q2. Only the 10% end fits the claim that investment costs ease from Q3 (INFERENCE).
- (Role 5 addendum) The chairman pledged no new sales and marketing cost until quarterly revenue doubles (CALL; speaker inferred).
- (Role 5 addendum) Design-led (B2S) revenue now starts in FY29 to FY30 (CALL). An analyst asked about the FY27 double-digit target. Management did not answer.
- (Role 5 addendum) Of 30 filing questions, the call answered 1, partly answered 6, evaded 4 and did not address 19.
- (Role 5 addendum) Eight of 23 checked call claims contradict the filing or the deck. The table below lists the main ones.
```
REPLACE the bullet `- Verdict: PROCEED WITH FLAGS. The operator decides at Halt 1.` WITH `- Verdict: PROCEED WITH FLAGS. The operator decides at Halt 1. (Role 5 addendum: unchanged after the call.)`

## U10. Management said vs filing shows (INSERT after the Verdict bullet, before `### 2. Sector intelligence`)
```

#### Management said vs filing shows (Role 5 addendum)
| Management said (CALL) | Filing shows |
|---|---|
| Gross and contribution margin higher YoY; "it's not the revenue mix" (chairman, inferred) | Gross margin 37.41% vs 41.22% (FILED); the deck names revenue mix (MGMT) |
| The margin drop is sales and marketing cost, 100-200 bps | Employee plus other-expense ratio fell 245 bps YoY (FILED) |
| The earnout reversal is "one-time" | Q2 FY26 and Q2 FY27 both carry one (FILED; MGMT deck) |
| Q2 other income is forex and export incentives | The earnout is 80.4% of Q2 other income (FILED) |
| The US business is "doing as per our plans" | US arm EBITDA 1.17%; a loss before the earnout (FILED, derived) |
| Finance cost fell on "lower working capital borrowings" | Gross borrowings up 24.3% in H1; India took new short-term debt (FILED) |
| "positive growth across all key segments" | Auto & Others fell sharply (INFERENCE from MGMT shares) |
| Book-to-bill "over 1.6 times" | The book walk gives 1.55x (INFERENCE from the MGMT book and FILED revenue) |
```

## U11. Sector intelligence (INSERT before the bullet `- Not disclosed: segment revenue in rupees, the chip-equipment share, and component price effects.`)
```
- (Role 5 addendum) On the call, AI data centres and robotics are at the "just started exploring" stage. Chip-equipment work has booked revenue for two quarters; the amount was not given (CALL).
- (Role 5 addendum) Management named memory-market supply shortages. It did not name component cost (CALL).
```

## U12. Business-model intelligence (INSERT before the bullet `- Not disclosed: design-led (B2S) revenue share, US entity split, customer advance terms.`)
```
- (Role 5 addendum) Four B2S programmes worth "close to $1 billion" over 7-9 years sit outside the order book. Only part is signed (CALL).
- (Role 5 addendum) Product development is fully expensed. Management keeps the option to capitalise it (CALL).
```

## U13. Competition intelligence (INSERT before the bullet `- Risk to watch: if peers pass on component costs faster, Cyient DLM's gross margin gap widens (INFERENCE).`)
```
- (Role 5 addendum) The Honeywell programme is build-to-print, not design-led. Serial production slipped on engineering changes, with no new date (CALL).
```

## U14. Forward map
(a) APPEND to the end of the "Make-or-break reading: ..." paragraph: ` (Role 5 addendum) The same results also test the H2 growth pledge (Q3 YoY at or above 30%) and intake of 600 Cr plus.`
(b) REPLACE row `| Now | Role 5 on the 15-Oct-2026 call | Management gives a component-cost split and an earnout residual | Questions on the earnout and margin are evaded |`
WITH `| Now (Role 5 addendum: done 2026-10-18) | Role 5 on the 15-Oct-2026 call | Management gives a component-cost split and an earnout residual | Questions on the earnout and margin are evaded (outcome: bear fork; no component split, earnout omitted) |`
(c) INSERT after that row:
```
| About mid-Jan 2027 (Role 5 addendum) | Q3 FY27 call: first score of the baseline promise log | Q3 revenue up 30% or more YoY; intake 600 Cr plus by the book walk; sales and marketing cost flat | Growth below 30%; intake below 600 Cr; sales and marketing cost rises |
| About Apr to May 2027 (Role 5 addendum) | Q4 FY27 call: AI data centre and robotics update; FY27 margin vs 9-10% | Named pipeline and orders; FY27 margin near 10% | Still "exploring"; FY27 margin at or below 9% |
| About late Jul 2027 (Role 5 addendum) | Q1 FY28: the "double-digit from Q1" pledge | Q1 FY28 margin at or above 10% | Below 10% |
```

## U15. Closing YAML of the review
- `docs_merged: [results, presentation]   # ...` -> `docs_merged: [results, presentation, concall]   # Role 5 addendum 2026-10-18: concall added`
- under `ledger_reconciliation:` change `turns: 0` -> `turns: 97   # Role 5 addendum: concall ledger (Role 4 ledgers carry 0 turns)`
- `a3_findings_incorporated:` append `CF01, CF02, CF03, CF04, CF05, CF06, CF07, CF08, CF09, CF10, CF11, CF12, CF13, CF14, CF15, CF16, CF17, CF18, CF19, CF20, CF21, CF22, CF23, CF24, CF25` inside the list.
- `questions_for_management:` append the twelve Q31-Q42 items from `work/blocks/a4-role5.yaml` (questions_for_management).
- `monitorables:` change item 1's `item` to `"Role 5 on the 15-Oct-2026 call transcript; mark question answer status (Role 5 addendum: DONE 2026-10-18)"`, then append the fifteen items from `work/blocks/a4-role5.yaml` (monitorables).
- `flags:` replace `- "Role 5 pending: 15-Oct-2026 call transcript not in this run"` with `- "Role 5 addendum complete 2026-10-18 (machine transcript, speakers inferred); verdict unchanged"`, then append the twelve concall flags from `work/blocks/a4-role5.yaml` (flags).
- after `plain_language_brief_included: true` add:
```
role5_verdict: "PROCEED WITH FLAGS (unchanged); concall impact WEAKENED; credibility ND (baseline log); archetype UNCLASSIFIED"   # Role 5 addendum
answer_status_counts: {ANSWERED: 1, PARTIALLY: 6, EVADED: 4, NOT_ADDRESSED: 19}   # Role 5 addendum
new_question_ids: [Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40, Q41, Q42]   # Role 5 addendum
oi_1_corrected: true   # Role 5 addendum
```
- `analyst_note` (Role 4) stays as it is. Add `role5_analyst_note:` with the analyst_note text from `work/blocks/a4-role5.yaml`.
