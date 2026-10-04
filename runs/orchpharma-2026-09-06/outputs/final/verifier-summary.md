# VERIFIER SUMMARY — ORCHPHARMA, run 2026-09-06 (phase 1)

Phase 1 verifier findings: A (numerical), B (red flags), D (peers), and the Gate 0 plus Emerging Moat portion of C (framework). Verifier C's valuation adherence section is PENDING PHASE 3 and was deliberately not run, because B10 and B11 do not exist and the valuation framework documents were not loaded. Verifier C rules 4, 6, 7, 11 and 12 are unexercised, and the expectation ledger and business understanding narrative audits are not cleared, only deferred.

## CONFIDENCE DELTA AND ACCEPTANCE RATES

| Component | Verifier | Acceptance | Model | Counts |
|---|---|---|---|---|
| Numerical acceptance | A (B12a, run 2) | 95.2 | claude-haiku-4-5 | 0 CRITICAL, 3 MAJOR, 6 MINOR, 42 numbers checked, 94 of 415 claims at 10.1% coverage |
| Red flag coverage | B (B12b, round 2) | 39 | claude-opus-4-8 | 1 CRITICAL, 11 MAJOR, 6 MINOR; 23 independent flags found, 9 caught, 6 partially caught, 8 missed |
| Framework adherence | C (B12c, phase 1 scope) | 90 | claude-opus-4-8 | 0 CRITICAL, 3 MAJOR, 11 MINOR; Gate 0 49 of 56, Emerging Moat 35 of 37, combined 84 of 93 at 90.3% |
| Peer utilisation | D (B12d) | 91 | claude-sonnet-5 | 0 CRITICAL, 2 MAJOR, 1 MINOR; 11 peers audited, 10 of 11 peer quarter entries correctly handled |
| **OVERALL** | minimum of the four | **39** | | Below 60: forced REWORK |

Verifier C's stated position: concur with the Gate 0 classification, concur with the Emerging Moat classification, concur with the combined assessment, rework_triggered false on its own scope. Verifier B's stated position: concur with the C credibility grade, reached by a partly different route.

---

## CRITICAL

| Verifier | Stage | Location anchor | Finding |
|---|---|---|---|
| B | B05 | Sections 2A / 2E / 4D / timeline_slippages / red_flags. Concall_Feb_2026_Transcript.pdf p.5-6; Concall_Jun_2026_Transcript.pdf p.13; Concall_Aug_2026_Transcript.pdf p.17 | MISSED repeated evasion across three consecutive quarters on the US ANDA pipeline (Teflaro generic, Ceftazidime-Avibactam). Feb_2026 "before our next quarter call... the filing should happen this year" to Jun_2026 "They will be filed through a CMO" with no date, to Aug_2026 "validation batches maybe this year or early next year, and then six months for filing", with the prior filing's FDA objections unresolved. About twelve months of slip, never acknowledged, on the product whose US market size of $300m to $350m B05 itself carries as a value driver, with a 180 day exclusivity window named as at risk at Feb_2026 p.6. No row anywhere in B05 |

---

## VERIFIER A — NUMERICAL (B12a, acceptance 95.2)

| Severity | Location anchor | Claimed | Source truth | Note | source_fidelity |
|---|---|---|---|---|---|
| MAJOR | 05-concall.md, Section 1B row 116, Q4 FY26 EBITDA | Rs 42.3 cr | Verifier A read Concall_Jun_2026_Transcript.pdf p.2-3 as "approximately INR23 crores" | Called a 2x discrepancy requiring correction before stage 11. CLEARED by the orchestrator at source, see the disagreement log below | true |
| MAJOR | 09-tam.md, Section 2 Method 3, Covalent revenue and the unorganised sector multiplier | Covalent FY2024 revenue Rs 2,916.1 cr; multiplier 1.3 to 1.6, not cephalosporin specific | ICRA rating snippet via WebSearch, WebFetch blocked; multiplier is the generic instructed default | Verifier A's own note: "This is not a MISMATCH, it is a confidence limitation transparently disclosed by the report". Not a finding | false |
| MAJOR | 06-peers.md, peer financial screening | Peer revenue and financial figures from the screener | Screener Data_Sheet populated for ORCHPHARMA only; peer sheets are empty templates by task design | Verifier A's own note: "CORPUS LIMITATION, NOT REPORT ERROR", and it called the stage's reroute to peer concalls appropriate. Not a finding | false |
| MINOR x6 | Across 02-notes-pass3, 05-concall, 07-emoat, 09-tam rows in the B12a report tables | Rounding and annotation notes on rows that matched source | Each row verdict is MATCHES | The six MINOR labels are attached to verified clean rows (for example Rs 230.74 cr stated as Rs 230.72 cr, Rs 4.664 cr stated as Rs 4.66 cr). B12a does not itemise them as separate findings | false |

Per report acceptance from B12a: 01-gate0 N/A (logic driven, deferred), 02-notes-pass3 93.8%, 03-ardeep 100%, 04-bizmodel 100%, 05-concall 92.9%, 06-peers 75% (corpus limited), 07-emoat 100%, 08-promoter 100%, 09-tam 83.3%.

What Verifier A verified clean against source in run 2: the Rs 447.22 cr corporate guarantee, the Rs 230.72 cr GCLE purchase from Otsuka, the Rs 108.24 cr loan to Orchid Bio-Pharma, the working capital movements (receivables plus 27.7%, inventory plus 41.0%, revenue plus 12.5%), and the consolidation scope correction itself, confirmed across three transcripts. It reported its own coverage honestly at 10.1% after run 1 overstated it at 80%, and gave per report acceptance rather than one average that would hide a weak report.

---

## VERIFIER B — RED FLAGS (B12b, acceptance 39)

CRITICAL row is listed in the CRITICAL section above.

| Severity | Location anchor | Finding |
|---|---|---|
| MAJOR | B05 preamble "Why this report was redone", plus 1B, 1C, 2B, 3A anchors | The categorical remediation claim that every anchor is the PDF page taken from the page marker is false in at least six places, five of them the printed footer page. Feb_2026 mechanical completion cited p.3, actual p.4; Feb_2026 Rupesh Tatiya staging quote cited p.11, actual p.12; Feb_2026 three players naming and "nobody else setting up a plant" cited p.15, actual p.16, twice; Feb_2026 Russia and CIS war cited p.8, actual p.7; Jun_2026 Europe "about fourfold" cited p.4, actual p.5. All Aug_2026 anchors and about 100 others check clean. Substance survives, the verification claim does not |
| MAJOR | B05 "THE CENTERPIECE FINDING", 4A item 4, 4D row 1, YAML flags and analyst_note | The Rs 50-60 cr Dhanuka FY26 EBITDA loss carries more confidence than the method supports and the FY25 cross check is circular. The FY25 arithmetic implies Dhanuka contributed about minus Rs 5 cr on Rs 500 cr of revenue in a good year; B05 calls that roughly neutral and treats the match as validation, when it reads equally as a Rs 25-40 cr systematic basis bias against management's own 5% to 8% margin at Feb_2026 p.10. Direction endorsed, magnitude not established. Amendment 25 requires both readings and the separating observation to be named; they were not |
| MAJOR | B05 Section 1C Dhanuka merger, 2E Dhanuka EBITDA row, centerpiece. Concall_Jun_2026_Transcript.pdf p.10, Manish Dhanuka to Loveleen Bagga | MISSED: "in terms of percentage, Dhanuka has lower percentage EBITDA, but it will add incremental EBITDA to the overall EBITDA of Orchid. That combined EBITDA number in terms of percentage will have an improvement." Arithmetically impossible as stated. B05's claim that the question was never answered directly understates the record and forgoes the stronger finding |
| MAJOR | B05 Section 2D / 1B / 4A item 1. Concall_Nov_2025_Transcript.pdf p.3 against Concall_Aug_2026_Transcript.pdf p.4 | MISSED: the restated combined Q1 FY26 gross margin of 30% is 13 points below the standalone Q1 FY26 gross margin of 43%, implying a Dhanuka gross margin near 5%, while the full year combined figures imply near 24%. The restated series is internally inconsistent across periods, on the exact inputs the centerpiece rests on, and no analyst raises it |
| MAJOR | B05 Section 1B guidance table, 2D, 4A item 1, YAML flags. Concall_Nov_2025_Transcript.pdf p.10 | MISSED: the only total debt figure in the corpus is unreliable. Rs 47 cr was given only after an analyst asserted debt had risen Rs 1,000 cr, was called "some misunderstanding", came with "We'll just get you the numbers" that never happened, states no basis, and was never restated. B05 uses it as a clean anchor in the Rs 300 cr funding gap arithmetic |
| MAJOR | B05 Section 2A, Q3 FY26 base business margin row; 2C; 4C; promise_delivery row | Basis mismatch correction applied asymmetrically. B05 correctly refuses a combined basis outcome against a standalone basis revenue target one row earlier, then measures the standalone set FY27 margin target against combined Q1 FY27 EBITDA of Rs 25 cr on Rs 304 cr at 8.2% and concludes below both targets. On B05's own method the standalone Q1 FY27 margin is about 12% to 12.5%, at the target. The row feeds the C grade |
| MAJOR | B05 Section 2D sequential reconstruction. Concall_Feb_2026_Transcript.pdf p.10, Manish Dhanuka | Magnitude understated because a disclosed figure was never used. Dhanuka 9M FY26 revenue of Rs 305 cr against Rs 370 cr last year gives Dhanuka Q3 at Rs 109 cr and Q4 at Rs 145 cr directly, reproducing both stated combined anchors exactly. Combined Q4 FY26 is about Rs 376 cr, so Q1 FY27's Rs 304 cr is about a 19% sequential decline, not 13% to 17%, and it also sits below combined Q3 FY26 at Rs 309 cr |
| MAJOR | B05 Section 1C Enmetazobactam, 4A item 3, dropped_triggers. Concall_Jun_2026_Transcript.pdf p.7 | MISSED: the peak sales YEAR was pushed from about 3 years post launch to years 4 to 5 in the same answer that reframed a $200-250m peak into a $1-2bn lifetime figure. A two year extension on the flagship asset's time to peak, undiscussed and unflagged |
| MAJOR | B05 Section 2A promise tracker, timeline_slippages, 4B. Concall_Jun_2026_Transcript.pdf p.15, Mridul Dhanuka to Rupesh Tatiya | MISSED: "if you have to assume something, I would say 50% will be signed in for sure" within six months for five named out licensing markets (Japan, Russia, US, Latin America, Southeast Asia). The most specific and most testable licensing commitment in the corpus, dated to about Nov 2026, with only Russia signed as of the Aug 2026 call. No row anywhere in B05 |
| MAJOR | B05 Section 3A / 4B questions 3 and 4; B06 Part 1 Q3 and Q4. KOPRAN-Concall_Feb_2025_Transcript.pdf p.8, Sanjay Dosi | MISSED peer contradiction of the Pen-G precedent argument underwriting the Rs 750 cr capex: "since India is going very aggressive on development of KSMs... we are seeing a trend where China is dropping prices of KSMs... the next battlefield will shift from APIs to KSMs." Stale at Feb 2025 and must be labelled so, but it is the only peer evidence in the corpus on this mechanism |
| MAJOR | B05 Section 1C triggers that disappeared, 2D, 4D row 3. Concall_Jun_2026_Transcript.pdf p.4, Manish Dhanuka | PARTIALLY CAUGHT and materially incomplete. The debt and cash blackout flag is correct on the search result, independently confirmed as zero hits in both calls, but omits the opening remark that "power and fuel costs, finance costs continued to decline". That is an affirmative falsifiable claim about the cost of leverage made during the blackout, against a screener showing borrowings roughly doubling |
| MINOR | B05 Section 1C Europe evasion sequence, 2E row 3. Concall_Feb_2026_Transcript.pdf p.7 and p.11 | PARTIALLY CAUGHT: the Q3 FY26 call is characterised as pure refusal, omitting two renewed promises on the same call. A promise renewed and broken twice is a stronger finding than one broken and then refused |
| MINOR | B05 Section 1C Europe growth restatement, 4D row 14. Concall_Aug_2026_Transcript.pdf p.4 against p.11 | PARTIALLY CAUGHT: B05 catches "about fourfold" against "175%" for the identical quarter but misses the same call's opening remark of "170% in Q4 of '26". Three different figures for one quarter across two calls |
| MINOR | B05 Section 2D, 4D row 9. Concall_Aug_2026_Transcript.pdf p.14 and p.5 | PARTIALLY CAUGHT: misses a second uncorrected analyst misstatement of headline revenue, "of this 350 revenue" against a reported Rs 304 cr, and misses management's own description of the quarter as "mediocre", which is the strongest management sourced support for B05's own sequential decline read |
| MINOR | B05 dropped_triggers item 3; Section 2C. Concall_Jun_2026_Transcript.pdf p.7 | NOT SUPPORTED as written: the $250m peak figure was reconciled directly when asked. Peak year revenue and lifetime cumulative revenue are different metrics. The real defect in that answer is the undisclosed peak timing extension |
| MINOR | B05 Section 1C 7-ACA, 2A mechanical completion row, 4C | Incomplete framing: the visibility regression reading never states that both later calls, 26-May-2026 and 21-Aug-2026, PREDATE the September 2026 target, so neither could confirm or deny it. The benign reading is not named. B05's underlying staging re-derivation is correct and is the report's best analytical correction |
| MINOR | B05 Section 1C Enmetazobactam US row, 2E row 1. Concall_Aug_2026_Transcript.pdf p.15 | Mild overstatement: "no date" is fair for the US specifically but not for the programme. The same call gives "by end of this financial year... three, four agreements would be in place for three, four more places" |

Promise delivery spot checks: 5 checked, 4 confirmed, 1 wrong.

---

## VERIFIER C — FRAMEWORK ADHERENCE, GATE 0 AND EMERGING MOAT ONLY (B12c, acceptance 90)

Recomputations: Gate 0 core score 29 stated, 26 if E2 is rescored to 0. Moat class MODERATE stated, THIN if M1 is scored on the scorecard's own C1 revenue CAGR. Emerging Moat score 23.0 stated, 24.3 upper bound under a uniform mixed row multiplier, with MODEST and EM below 25 holding on both readings. Every recomputation leaves the AVOID classification standing.

| Severity | Stage | Location anchor | Claimed | Rule | Recomputed | Note |
|---|---|---|---|---|---|---|
| MAJOR | B01 | block field history_downgrade | true | Data confidence: 10+ years is full, no downgrade | false | YAML contradicts the report body; cannot lower AVOID, would be CRITICAL at any higher core score |
| MAJOR | B01 | E2 promoter holding change | score 3 | Operating rule 5: mark N/A and score 0 where the data point is not available | E2 = 0, Block E = 10, core = 26 | The stage itself labels it a 1 year proxy, not a true 3 year trend; rule 5 was applied at E3 and D4 |
| MAJOR | B01 | M1 pricing power | score 3 on FY23-25 CAGR 17.67% | Block F M1, revenue CAGR at or above 10%, window unspecified | M1 = 0 on C1's 4.97%; moats 2 to 1; moat class MODERATE to THIN; moat score 11 to 8; grand total 40 to 37 | Framework silent on the window; silence obliges the stage to declare its choice, and the alternative flips a field B07 6C reprints |
| MINOR | B01 | A3 median ROE | FY17-FY20 excluded as N/M | ROE formula definition | Median still below 12%, score 0 unchanged | Negative endpoint N/M is a CAGR edge rule, not an ROE rule. The exclusion was disclosed |
| MINOR | B01 | A3 value listing | Five values listed for a six year median | Operating rule 3, show every number extracted | FY2024 ROE 9.92% omitted; stated median 3.86% verified correct | Presentation defect only |
| MINOR | B01 | Block B, B1 against B2/B3 | CFO 18.34/125.99/19.22 at B1, 13.39/130.73/27.48 at B2/B3 | FCF = CFO minus capex, one basis | Cumulative FCF minus 44.69 on the Data_Sheet basis; B2 and B3 score 0 on either | Two CFO values for the same years in one block, unreconciled; likely standalone against consolidated |
| MINOR | B01 | M5 scale and dominance | score 1 plus PEER DATA NEEDED | Block F preamble: missing peer data scores 0 and is marked PEER DATA NEEDED | M5 = 0, moat score minus 1 | M7 applied the identical rule correctly at 0; internal inconsistency |
| MINOR | B01 | D4 current ratio | score 0, FY2026 NOT FOUND | Operating rule 5 | Block D would be 10 and core 34 on FY2025's audited 3.31x; still AVOID | PASS with note, not a fail. Literally compliant and consistent with D1-D3 taking FY2026 as latest |
| MINOR | B01 | E4 contingent liabilities | 1.11% | Basis consistency | Band unaffected | PASS with note, not a fail. Consolidated note 45 over standalone net worth; flagged by the stage; framework silent on basis |
| MINOR | B07 | Section 5, rows E1 and B2 | E1 at 0.7x, B2 at 0.5x while A1/A2/B1 mixed rows take 1.0x | Evidence multipliers 1.0 documented / 0.7 call / 0.5 search | em_score upper bound 24.3 | No stated policy for mixed evidence rows; the error direction is conservative; MODEST and EM below 25 hold on both readings |
| MINOR | B07 | F1, G2, H3 evidence items | Anchored to "AR BRSR section" and "AR narrative, environment section" | Operating rule 3, source anchors (AR p.__) on every evidence item | No score effect | The anchor cannot be located by page; two of the three feed scored rows |
| MINOR | B07 | block field capex_embedded_growth_pct | 161 | Section 2C, field carries the instructed formula figure | 63% adjusted; 156% on the Gate 0 fixed asset denominator | PASS with note, not a fail. Literal compliance, but the stage's own preferred figure is 63 and a block only reader never sees that |
| MINOR | B07 | Section 2C fixed asset turnover | Net Fixed Assets 612.9 (AR p.23) | Cross stage consistency | Gate 0 M3 used Net Block 632.71 from the FY25 screener; FAT 1.50x against 1.457x | PASS with note, not a fail. Both anchored, no conclusion moves |
| MINOR | B07 | block field completionist_recount | Recount line without the leading document mark | Mandated wording "recount performed: [n] documented items across [m] categories" | n/a | PASS with note, not a fail. The report body carries the mandated form correctly |

Deferred, not cleared: valuation rules_checked 0, status PENDING PHASE 3. Expectation ledger not audited, status PENDING PHASE 3. Business understanding narrative audit status PENDING PHASE 3, recorded at the time as "stage 13 has not run".

---

## VERIFIER D — PEER UTILISATION (B12d, acceptance 91)

| Severity | Location anchor | Claimed | Source truth | Note |
|---|---|---|---|---|
| MAJOR | B06 Part 1 Q3 net read, Q4 net read, reading note | "No peer transcript in the corpus mentions 7-ACA, cephalosporin key starting materials... at any point", "All three peers silent on 7-ACA specifically", "no direct peer analogue in any of the 11 transcripts" | KOPRAN-Concall_Feb_2025_Transcript.pdf p.7-8, Surendra Somani names "Cephalosporins" explicitly inside the same fermentation and KSM passage B06 already cites for Q4, inside a call B06 marks SUBSTANTIVE | Completeness miss, not fabrication. Does not flip either UNVERIFIABLE verdict, but the absolute "no mention anywhere" framing is factually wrong |
| MAJOR | B06 Part 2E and risks_peers_raise, working capital line | Inventory days rising from about 94 to about 145-155 days across FY26 | 94 to 124 days is the distinct "inventory days to sales" metric, and it rose; 155 to 145 days is the separate quarterly "working capital days of sales" disclosure, and it fell | B06 conflates the two into one apparently rising range. The underlying qualitative finding, analyst scrutiny on inventory against reported profit, is accurately quoted elsewhere in the same section and is not in dispute |
| MINOR | B06 Part 1 multiple citations: NEULANDLAB Feb 2026 p.2, GRANULES Nov 2025 p.5, GRANULES Jan 2026 p.12, GRANULES May 2026 p.7, GRANULES Jul 2026 p.5 | Page numbers per B06's own anchors | Each is one PDF page behind the actual PDF page marker, matching the transcript's internal running footer number instead | Systemic anchor convention inconsistency. Content and speaker independently confirmed correct at the true page in every case |

Peers audited 11, substantive entries confirmed 10, substantive unsupported none, unused but relevant none, claims all addressed true, verdict discipline fails none.

---

## VERIFIER DISAGREEMENT LOG (carried in full)

Every point where a downstream step's conclusion conflicts with a Verifier A source fidelity finding. Not a REWORK trigger. Standing evidence on whether the out of family numerical check catches what the others miss, or produces noise.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-06 | orchpharma-2026-09-06 | Q4 FY26 EBITDA, Rs 42.3 cr, claimed in 05-concall.md | MISMATCH, source_fidelity true. Verifier A read the source as "approximately INR23 crores" at Concall_Jun_2026_Transcript.pdf p.2-3 and called the report figure a 2x error requiring correction before stage 11 | Orchestrator re-read the source. The transcript reads "Our EBITDA for Q4 stood at approximately INR42.3 crores compared to approximately INR40 crores in Q4 of '25" at Concall_Jun_2026_Transcript.pdf p.3, confirmed in the clean embedded text layer and by an independent extraction. Stage 5's figure is correct and correctly anchored | FLAG CLEARED, source re-check found the number at a correct anchor, re-checked by the orchestrator session, 2026-09-06 | Verifier A misquoted the source. The surrounding sentence also carries Q4 FY25 EBITDA about Rs 40 cr, FY26 revenue Rs 811 cr against Rs 922 cr, and FY26 EBITDA Rs 101 cr against Rs 155 cr, all consistent with stage 5. This is the LESSONS catalogued Verifier A failure mode: a false finding on a figure that matches its source |

### Two further Verifier A severity mislabels this run, not disagreements

Neither is a disagreement, because neither is a source fidelity finding. Both are recorded because they inflate the MAJOR count and would distort the confidence delta if read at face value.

1. 09-tam.md Method 3, Covalent revenue and the unorganised sector multiplier. Verifier A labelled it MAJOR and then wrote in its own note that it "is not a MISMATCH, it is a confidence limitation transparently disclosed by the report". A stage that flags its own low confidence, names the blocked source and states the limit of its method has followed the rules. Not a finding.
2. 06-peers.md peer financial screening. Verifier A labelled it MAJOR and then wrote in its own note "CORPUS LIMITATION, NOT REPORT ERROR" and called the stage's workaround appropriate. The peer screener exports are empty templates, which stage 0 recorded and every stage was told. Not a finding.

CORRECTED VERIFIER A COUNTS FOR THIS RUN: 0 CRITICAL, 0 MAJOR surviving scrutiny, 6 MINOR. The stated acceptance rate of 95.2% is therefore a floor, not a ceiling. The confidence delta uses the stated figure and this note records why the true numerical fidelity is higher.
