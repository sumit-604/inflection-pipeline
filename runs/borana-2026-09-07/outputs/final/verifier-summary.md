# Verifier Summary — Borana Weaves Ltd (BORANA)
Run 2026-09-07. Phase 1 (evidence). Verifiers A, B and D in full; Verifier C's Gate 0 and Emerging Moat portion only. Verifier C's valuation half is deferred to phase 3 because stages 10 and 11 have not run.

## Phase 1 confidence delta

| Component | Score | Verifier | Scope note |
|---|---:|---|---|
| numerical_acceptance | 89 | A (B12a) | 47 figures checked across all nine reports. |
| redflag_coverage | 33 | B (B12b) | 8 fully caught plus half credit for 6 partly caught = 11 of 33. |
| framework_adherence | 92 | C (B12c) | Gate 0 and Emerging Moat only, 55 of 60 rules passed. Valuation half deferred to phase 3. |
| peer_utilisation | 100 | D (B12d) | 12 of 12 peer transcripts substantively engaged. |
| **overall** | **33** | min of the four | Band: FORCED REWORK. |

## Acceptance rates and counts as declared

| Verifier | Model | acceptance_rate | CRITICAL | MAJOR | MINOR | rework_trigger |
|---|---|---:|---:|---:|---:|---|
| A — numerical (B12a) | claude-haiku-4-5 | 89 | 0 | 6 | 1 | false |
| B — red flags (B12b) | claude-opus-4-8 | 24 | 3 | 12 | 3 | **true** |
| C — framework (B12c) | claude-opus-4-8 | 92 | 0 | 0 | 5 | false |
| D — peers (B12d) | claude-sonnet-5 | 83 | 0 | 3 | 4 | false |

Counting note: Verifier B declares major_count 12; its findings list carries 11 MAJOR rows and its missed-flags list carries 13. The rows below reproduce the findings list, with the missed-flags text used for the three CRITICAL rows because it carries the fuller anchors. Verifier A's run 1 checked only 15 figures and returned zero findings; it was re-invoked once with a coverage addendum per the standing pattern, and run 2 governs.

---

## CRITICAL

| Verifier | Location anchor | Finding |
|---|---|---|
| B | Concall pp.7 and 11 vs AR FY2026 p.114 (Note 28) and p.104. Stage location: B05 section 1B / guidance / triggers, renewable savings accepted as "Committed, Quantified" | Renewable saving of Rs 18-20cr/yr stated twice and held under analyst challenge equals 92-102% of total audited Factory Power Expenses (Net) of Rs 19.56cr in FY26; stated substitution is only 70-80% and the hybrid is a third-party PPA project, so the claim exceeds a physically unreachable ceiling. Untested upstream; the figure anchors the payback and IRR arithmetic on a Rs 125cr investment. |
| B | AR FY2026 p.87 (CARO iii(a), verified vs PDF) and p.117 vs Concall p.12; Investor_Presentation_Q1FY27 p.16. Stage location: B05 section 2D / red_flags, Win Star loan treated as an isolated LOW-MEDIUM item | Rs 10,58,56,506 of loans and advances outstanding to five parties at 31-Mar-2026, incl. Rs 3.00cr to promoter-group R&B Denims Ltd (the entity SEBI searched under s.11C(9) three weeks later), against the CFO's on-record denial: "we will invest in our running business only. This is just a purely equity investment. Nothing else". Only two of the five names appear anywhere else; the presented balance sheet shows Investments/loans of Rs 1.46cr. Win Star is the sixth instance, not the first. |
| B | Investor_Presentation_Q3FY26 pp.6, 16 vs Investor_Presentation_Q4FY26 pp.6, 16, 26; Concall p.5. Stage location: B05/B06, no audit of the filed decks' internal consistency | Q4FY26 deck restates FY25 operating metrics as FY26: "80.93% Average Capacity Utilization (FY 25)" becomes "(FY 26)" unchanged to two decimals; Unit 3 82.94% and Unit 4 78.11% identical across period extensions of 3-4 months; installed capacity 39,21,12,000m and loom count 1,208 unchanged after adding 160 looms said to add 5 crore metres. On p.26 every margin on the H2 FY26 P&L page is exactly 2x correct: EBITDA margin printed 49.75% vs actual 24.85%; gross 86.0% vs 42.9%; PAT 33.74% vs 16.86%; H2 FY25 EBITDA 44.58% vs 22.29%. Rupee figures correct, all percentages on half the denominator. |

---

## MAJOR

### Verifier A — numerical (6)

| Location anchor | Finding |
|---|---|
| B03 AR Deep Dive, Phase 2; AR FY2026 Board's Report Annexure-6 item 10 p.74 vs Note 40 p.128 | Board's Report states Return on Net Worth FY26 23.03% on "Average Shareholder's Equity" Rs 28,157.50 lakh; Note 40 states ROE 35.01% / 59.45%. The Board's Report labels CLOSING net worth as "Average". Both figures exist in the AR exactly as B03 described. The contradiction is the company's, inside its own annual report, and B03 recorded it explicitly in its discrepancies field. DOWNGRADED from CRITICAL by orchestrator source re-check; does not trigger the REWORK gate. source_fidelity: true. |
| B02 Notes, Finding #6; AR FY2026 Note 8 vs Note 37 | FY25 trade receivables shown as Rs 2,181.54 lakh (Note 8) and Rs 3,922.71 lakh (Note 37 comparative). VERIFIED MISMATCH: the same balance shown as two different amounts. Uncorrected drafting error in the AR; FY26 current-year figures are consistent. source_fidelity: true. |
| B02 Notes, Rank 1 Finding; AR FY2026 Note 28(iii) vs Note 34(K) | FY25 jobwork Rs 447.73 lakh (Note 28) vs Rs 442.98 lakh (Note 34). B02 pass 2 independently confirmed via the FY25 AR that 442.98 lakh is correct, making 447.73 the error. Sits in the cost stack producing the headline margin. source_fidelity: true. |
| B05 promise-delivery tracker item 5; Q3FY26 call p.15 vs Q4FY26 deck p.33 vs Q1FY27 deck p.19 | Unit 4B 160 looms, 96 remaining to be commissioned February 2026. Q4FY26 deck shows 64/160 operational with no completion confirmed. Q1FY27 deck replaces the figure with a new 192-loom tranche; the original commitment is silently abandoned with no reconciliation. source_fidelity: true. |
| B06 peer verification question 3; B05 concall; Q3FY26 call 27-Jan-2026 p.6 | BIS import restriction on Chinese POY/PTY yarn stated as removed in December 2025. FILATEX-Concall_Feb_2026, SANATHAN-Concall_Feb_2026 and a CRISIL analyst on FILATEX all cite 12-13 November 2025. Policy event corroborated, date off by one month. source_fidelity: true. |
| B05 renewable power project slip chain; B04 section 4A risk monitoring | Hybrid power 19.79MW commissioning dates May-2026, June-2026, during 2026, 31-Aug-2026, then phased Sep/Oct-2026. Four documented sequential slips across seven months, each attributed to external factors; uncommissioned as of the 07-Sep-2026 run date. MW, capex and savings figures internally consistent; the delivery timeline is not. source_fidelity: true. |

### Verifier B — red flags (11 rows; major_count declared 12)

| Location anchor | Finding |
|---|---|
| B05 section 3B; Concall p.6 vs p.10; 2025-12-31_IPO-monitoring-agency-report p.8 | "Not imported" statement not tested. Management told two analysts contradictory things about Chinese raw material in one call; the IPO monitoring report lists nine import transactions of Rs 7.93cr. |
| B05; RHP p.202 and p.175; Credit_Rating_2025-02-11 p.1; Investor_Presentation_Q1FY27 p.6 vs Q3FY26 p.9 | Promoter biographical facts not checked against the RHP. Stated experience roughly doubled from the SEBI offer document (24/13/13 years, total 50) to the Q1FY27 deck ("101 Years of Experience", 51+/25+/25+), against a rating agency's independent "more than 24 years" for Mangilal. |
| B05 sections 2A/2D; AR FY2026 p.56 vs pp.33-34 and p.55; Results_Q4FY26_and_FY26 p.1 | Governance record of the FY26 AR not audited. The AR declares no penalties or strictures while listing eight non-compliances and six exchange observation letters, discloses only the Brickwork rating and omits CARE's ISSUER NOT COOPERATING, and the annual results carry a limited-review report applying Ind AS 34 and SRE 2410 that states "Accordingly, we do not express an audit opinion". Statutory audit fee Rs 1.50 lakh vs tax audit fee Rs 2.50 lakh on Rs 388.59cr revenue. |
| B05 red_flags; Investor_Presentation_Q3FY26 pp.23, 35 vs Q4FY26 pp.23, 34; Q1FY27 p.4 | No flag on the disappearance of the doubling plan or on the tone shift with results. The Rs 350-400cr / 2,000-loom / March-2028 plan is absent from the Q1FY27 deck; loom count moved 1,208 to 1,212 in two quarters; the Q4FY26 deck dropped the Management Commentary slide and IR contacts in the quarter revenue fell 9.5% QoQ (Rs 111.36cr to Rs 100.73cr) with no explanation anywhere; the Q1FY27 deck then headlines "accelerated growth" on revenue flat QoQ for two quarters. |
| B05 red_flags[5] and flags[4]; section 2D; 2026-07-29_Reg30_resignation-secretarial-auditor-2 p.1; 2026-07-29_Reg30_appointment-secretarial-auditor p.1 | NOT SUPPORTED: "two secretarial-auditor resignations six days apart". There was one resignation; the 29-Jul-2026 filing is the Board noting it, filed the same day as the successor's appointment. A routine two-step reported as a pattern. The signal is cited three times. |
| B06 Part 1 Q5, contradicted[] and analyst_note; SANATHAN-Concall_Aug_2026 p.9; Investor_Presentation_Q1FY27 pp.15-16 | OVERSTATED: CONTRADICTED verdict on the 2x-3x asset turn rests on a single peer in a different machine class (72,500 cotton-yarn spindles), against a claim Borana's own audited FY26 supports at 2.65x revenue over net PPE. B06's analyst_note concedes "suggestive rather than dispositive" while the structured verdict records CONTRADICTED and feeds it forward. |
| B06 risks_peers_raise and Part 2E; SANATHAN-Concall_Feb_2026 p.3 vs Concall p.12, all four decks and AR FY2026 | The GST cut on fabrics from 12% to 5%, which a peer says caused value-chain inventory buildup and deferred purchases in the same quarter, is a change on Borana's own product and appears in no Borana document. The same peer reports US-tariff-driven order loss in home textiles and apparel, Borana's own end-uses, against management's "that is not a challenge at all". Neither item is used. |
| B06 Part 1 Q2/Q3; Concall p.4 and Q&A | Price direction verified, management's characterisation not tested. Prepared remarks call the quarter "pricing are stabilized... reduced volatility... more predictable operating condition" while two peers call the same quarter margin pressure in a volatile environment; the same call's Q&A attributes the margin to cheap Chinese imports, so prepared remarks and Q&A give different causes. |
| B05 section 1A trigger row; Concall p.8; AR FY2026 other income | Power and interest subsidy sunset recorded as a quantified trigger, not as a risk. The 2026/27/28 per-unit expiry exists in one document in the corpus (the one call), appears in no deck and no AR. Other income was Rs 8.21cr against PBT of Rs 78.40cr. |
| B05 section 2A row 6 / timeline_slippages; 2026-08-29_Reg30_hybrid-power-update.pdf | Hybrid scope change not captured. The 29-Aug-2026 filing titles the project "9.9 MW Hybrid Power Project" and states the solar component as 7.65 MW against 9.89 MW in every prior company document. A 23% scope cut alongside the fourth delay. |
| B05 section 2A row 4; Investor_Presentation_Q4FY26 pp.32-33; Investor_Presentation_Q1FY27 p.17 | Rooftop solar. The 3.55 MW plant promised for February 2026 is absent from the entire Q4FY26 deck and reappears without a date as "operational" in the Q1FY27 deck. |

### Verifier D — peers (3)

| Location anchor | Finding |
|---|---|
| B06 Part 1 Q3 and Part 3 coverage map, FILATEX Q1 FY27 row; correct location FILATEX-Concall_May_2026 (extraction p.10, printed p.9) | CRISIL-analyst quote cited as "FILATEX-Concall_Aug_2026, p.9-10" does not appear in that transcript. It is verbatim in FILATEX-Concall_May_2026, a different call by a different analyst context. Substance survives; the source-file and call-quarter attribution is wrong. The Q3 CONTRADICTED verdict still stands on its two correctly anchored peers. |
| B06 Part 1 Q1 (central UNVERIFIABLE verdict), input_gaps and analyst_note; SANGAMIND-Concall_Aug_2024_Transcript p.17 (printed p.16 of 18) | The Aug-2024 Sangam call contains quantified, management-sourced margin colour directly relevant to Q1's 23-25% claim: yarn margin about 10% long-run average on a 3-20% range, fabric value-addition adding an incremental 4-5 points over the yarn base, garmenting 15-20% at full utilisation. B06 states in four separate places that no peer, including SANGAM, discloses any such figure. UNVERIFIABLE likely remains the correct overall verdict given definitional mismatches, but the absence claim is overstated and the figure should have been engaged explicitly. |
| B06 Part 1 Q4 "Peers silent" line and Part 3 coverage map, SANGAMIND Q4 FY26 row; SANGAMIND-Concall_Apr_2026_Transcript p.12 (printed p.11 of 18) | B06 states SANGAMIND "does not discuss anti-dumping duty, QCO or BIS in any of its four transcripts" and is "silent on... BIS/QCO by name". False: an analyst names "the quality control order" twice and management answers on the record that its removal had no material cost effect for SANGAM. The Borana/Surat-silence half of the claim is accurate; the BIS/QCO-silence half is wrong. |

---

## MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A | B02 Notes, Finding #12 working capital analysis; AR FY2026 Note 14(a), p.110 | Lease liability FY26 Rs 130.80 lakh vs FY25 Rs 150.12 lakh recorded as unanchored. CLEARED on orchestrator source re-check: both figures are present at AR p.110 ("130.80    150.12"). The verifier's grep did not reach them. B02's figures are correct and anchored. Logged as a verifier disagreement. source_fidelity: false. |
| B | B05 sections 1C and 2D; AR FY2026 p.126 | NOT SUPPORTED: AR stated as approved 14-Aug-2026, "seven months after the call". The AR records approval on 14th May 2026; the interval is 3.5 months. The underlying argument (margin driver absent from the AR) survives. |
| B | B05 section 2A row 3; Concall p.6 | Management guided GROSS margin ("gross margin profit may be better than this one also"); B05 anchors the promise to 24.32%, the EBITDA margin. Both outcomes were favourable, so the delivered verdict stands. |
| B | B05; Concall pp.13, 5 and 8; Investor_Presentation_Q3FY26 p.13 | Segment and production figures not cross-checked. Yarn share given as "around 7%" on the call vs 9% (9M FY26) and 12% (FY25) in the same week's deck; FY25 production given as 18.6 crore metres and 18.36 crore metres on the same call. |
| C | 07-emoat.md Section 5, H3 scorecard row | Likelihood x impact label contradicts its own description: cell labelled HM (=3) while describing medium likelihood and medium impact, which is MM (=2). On the stage's own words H3 raw = 2, adjusted = 1.4, em_score = 2.4 not 3.1. Flattering direction, magnitude 0.7 on a scale whose nearest threshold is 9 points away. Classification, active_categories and combined assessment all unchanged. |
| C | B07-emoat.yaml evidence_mix | inference:2 is unsupported by the report; the [INF] tag appears only in the taxonomy definition and never tags an item. documented:11 (whole-report count) sits beside completionist_recount's 5 (Section 3 scope) with no stated scope difference. No scored row rests on inference, so no output changes. |
| C | 07-emoat.md Section 6D and prompts/07-emerging-moat-pipeline.md | 6D instructs the stage to apply "the standard matrix" but prompts/07 never reproduces that matrix. The stage substituted the EM>=25 UA qualifier as its combination rule and declared the substitution openly. Outcome robust; the substitution can only refuse an uplift, never grant one. A rule gap in the prompt as much as a stage defect. |
| C | B01-gate0.yaml flags[] / data_notes[] | The data-confidence rule for the 5-6 year band requires the flag "may not have seen full cycle". It is stated in the report body but carried nowhere in the block: flags[] is empty and no data_notes entry mentions it. A downstream stage reading only the block loses it. |
| C | B01-gate0.yaml deal_breakers[] | The prompt requires stating WHICH years drive any deal-breaker. The entry names the block and the score but not the years. The driving years (FY26 capex Rs 178.98cr against CFO Rs 36.96cr; 1 of 5 years FCF-positive) appear in the report body and analyst_note, not in the field the instruction points at. |
| D | B06 report opening paragraph | Claims all six peer investor presentations were "read in full"; only 3 of 6 are ever cited. Direct read of both SANATHAN presentations confirms no unique content was lost, so this is a coverage-claim overstatement rather than a missed finding. |
| D | B06 Part 1 Q1, SANGAMIND quote attribution | "SANGAMIND Q4FY26 call, close to 10% for Q2FY26, p.9" misattributes the quote to the Q4FY26 (Apr-2026) call. The quote and the 8-12% divisional-margin range beside it are spoken during the Nov-2025 (Q2FY26) call, at the same page number cited. Content and page anchor correct; the source-call label is wrong. |
| D | B06 Part 2 / Q6 area, FILATEX presentation citation | Anchor "FILATEX-Investor_Presentation_Q1FY27, p.slide on trade" is not a valid page reference; the correct location is extraction p.12, printed p.11. The underlying claim (about 20-25% CAGR EU export growth to about USD 100bn by 2030) is accurately quoted at that location. |

---

## Source-fidelity corrections applied (corrections.yaml governs over every stage block)

| ID | Subject | Corrected fact | Anchor | Raised by | Disposition |
|---|---|---|---|---|---|
| C1 | Secretarial auditor churn, July 2026 | ONE resignation, not two. The 29-Jul-2026 filing is the Board noting the 24-Jul-2026 resignation, filed the same day as the successor's appointment. | 2026-07-24_Reg30_resignation-secretarial-auditor.pdf p.1; 2026-07-29_Reg30_resignation-secretarial-auditor-2.pdf p.1 | Verifier B | GATE HELD — claim corrected at source; the "two resignations" signal is withdrawn. |
| C2 | Reason for the resignation | A reason IS stated: "Due to pre-occupation with professional assignments and unavoidable professional commitments". The letter adds "I further confirm that there are no disputes, differences, or pending issues between me/us and the Company which have led to this resignation." | 2026-07-24_Reg30_resignation-secretarial-auditor.pdf p.3 | Orchestrator | GATE HELD — "no reason stated" is withdrawn. |
| C3 | Length of the mandate | The appointment was "for the financial year 2025-26 and 2026-27", a TWO-year term, not five. | 2026-07-24_Reg30_resignation-secretarial-auditor.pdf p.3 | Orchestrator | GATE HELD — figure corrected. The B08 deal-breaker is not withdrawn (still a resignation inside three years) but its stated basis is corrected; weight is for the operator to reset at Halt 1. |
| C4 | FY26 annual report approval date | Approved 14th May 2026, not 14-Aug-2026. Interval from the 27-Jan-2026 call is 3.5 months, not seven. | annual-report/Annual_Report_FY2026.pdf p.126 | Verifier B | GATE HELD — figure corrected. The underlying finding (margin driver absent from the AR) is unaffected and stands. |

Net effect as recorded: the July 2026 secretarial auditor sequence is materially less alarming than the corpus record framed it. The framing entered the run from the operator's own manifest.yaml and companies/BORANA.md and propagated into four stage blocks before a verifier caught it. The correction does not touch the SEBI Section 11C(9) search, the board-overlap finding, the withheld internal audit reports, or the six unfurnished exchange letters, which are separately anchored and stand.

## Verifier statements on scope

Verifier A: "No finding in this audit says a pipeline stage got a number wrong. Every MAJOR is a defect in the company's own filings or execution record that the stages found and reported correctly. The source-fidelity gate is therefore held, not breached."

Verifier B: "The low coverage is a breadth finding, not a fabrication finding. B05 and B06 are accurate within the scope each worked... rework B05's scope, not its method. B05's promise-delivery discipline is sound (5/5 spot checks confirmed) and its slip-chain work is the best single piece of analysis in either report."

Verifier C: "Both stages reached unflattering conclusions honestly. Every discretionary call ran against the stage's own headline... The single flattering-direction error found is worth 0.7 points on a 9-point margin. No method bending detected."

Verifier D: peers_audited 12, substantive_confirmed 12, substantive_unsupported none, claims_all_addressed true. One verdict-discipline fail recorded: the Q5 CONTRADICTED tag carries no qualifier in the YAML although the cross-machine-class caveat is stated in prose every time.
