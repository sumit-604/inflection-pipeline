# CEIGALL — VERIFIER SUMMARY (PHASE 1)

Run: ceigall-2026-09-06 | Ceigall India Ltd | CEIGALL

Scope: phase 1 verifiers only. Verifier A (B12a run 2, numerical), Verifier B
(B12b run 2, red flag coverage), Verifier D (B12d, peer utilisation), and the
Gate 0 plus Emerging Moat portion of Verifier C (B12c). Verifier C's valuation
adherence component is not in this file: stages 10 and 11 have not run and that
audit is pending phase 3.

Superseded verifier passes (B12a run 1, B12b run 1) are retained in
outputs/blocks/ as the record and are not drawn on here, except where the
orchestrator's composite read cites them.

---

## CONFIDENCE DELTA (PHASE 1)

| Component | Value | Verifier | Metric as measured |
|---|---|---|---|
| numerical_acceptance | 75 | A (B12a run 2) | 9 of 12 targeted figures verified clean or substantially clean after the orchestrator source re-check |
| redflag_coverage | 70 | B (B12b run 2) | (20 caught + 10 partially caught) / 43 independent flags |
| framework_adherence | 95 | C (B12c) | 81 of 85 rules passed: Gate 0 51/51, Emerging Moat 30/34 |
| peer_utilisation | 100 | D (B12d) | 3 of 3 peers substantive, 12 of 12 transcripts used |
| **overall** | **70** | minimum of the four | Band 60 to 74: a PROCEED verdict downgrades one level |

## ACCEPTANCE RATES AS PUBLISHED

| Verifier | acceptance_rate | As emitted | Other published rate | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A (B12a run 2, targeted) | 75 | 58 | run 1 broad pass 97.9 over 48 numbers, zero CRITICAL, zero MAJOR | 0 (1 as emitted, cleared) | 1 (3 as emitted, 2 reclassified RESOLUTION-LIMITED) | 4 |
| B (B12b run 2) | 47 | 47 | redflag_coverage 70; CRITICAL and MAJOR alone 61 caught, 90 surfaced | 1 | 11 | 9 |
| C (B12c, phase 1 scope) | 95 | 95 | Gate 0 51/51, Emerging Moat 30/34 | 0 | 0 | 5 |
| D (B12d) | 100 | 100 | peer_utilisation 100 | 0 | 5 | 5 |

Verifier B's strict acceptance_rate of 47 sits below the 60 FLAG RULES floor.
The verifier states the rate follows the rubric literally with no credit for
partial catches, and that the residual is dominated by a twelve item MINOR
tail of which the pipeline carries one. `pipeline_flags_not_supported` is empty
in both verifier B passes. The gate rule tension this creates is unresolved and
is carried to the operator in outputs/final/gate-recommendation.md Section 1.

Verifier A resolution note: three findings are RESOLUTION-LIMITED, meaning the
verifier self described the cell as unlocatable or unreadable at rendered
resolution rather than absent from source. Under the verifier's own brief that
is not a mismatch. They are unconfirmed, not cleared, and not contradicted.

---

## FINDINGS, SORTED CRITICAL FIRST

### CRITICAL

| Verifier | Location anchor | Finding | Disposition |
|---|---|---|---|
| A | Target 10, Annual_Report_2026.pdf sheets 108 and 80, cash flow statements | Claimed standalone +Rs 4,569.40m and consolidated -Rs 912.83m. Source truth: consolidated -912.83m confirmed; standalone rendered as -556.73m, negative not positive. Mismatch on standalone sign and magnitude. `source_fidelity: true` | FLAG CLEARED. Orchestrator re-read sheet 80 at single page render: "Net cash flow from/(used in) Operating Activities (I)" reads 4,569.46 unbracketed for FY26 against (2,709.12) bracketed for FY25, and the statement brackets negatives. The verifier's -556.73m does not appear on that line. Logged in verifier-disagreement-log.md |
| B | B05 section 2E, repeated question tracker. Concall_May_2026 p.9; Concall_Aug_2026 p.7 | MISSED repeated evasion: the margin one off question asked in two consecutive quarters by Mahesh Patil (ICICI Securities), answered both times with an unrelated list of newly started projects, never yes or no. Mahesh Patil appears nowhere in B05 | Accepted. Closed by stage 5 run 3, which added it as a HIGH flag and a valuation input |

### MAJOR

| Verifier | Location anchor | Finding | Disposition |
|---|---|---|---|
| A | Target 1, Note 11 consolidated, sheet 116 | Claimed Rs 4,039m FY24 to Rs 14,132.38m FY26 with nil impairment. Source truth: FY26 Rs 14,132.39m, FY25 Rs 8,733.43m, FY24 not shown in note. FY26 matches within rounding; the FY24 baseline is NOT FOUND in source. `source_fidelity: true` | STANDS. FY26 figure and nil impairment verified. The verified corpus supported statement is FY25 Rs 8,733.43m to FY26 Rs 14,132.39m, +61.8 percent. The tripling framing may not be repeated until the FY25 annual report is obtained |
| A | Target 7, Note 27/28, sheets 119-120 | Claimed reverse factoring Rs 2,952.13m. Source truth: NOT FOUND in rendered Note 27/28 at available resolution. Table anchor present, specific figure unlocatable. `source_fidelity: true` | RECLASSIFIED RESOLUTION-LIMITED, flag NOT cleared. Unconfirmed, not contradicted. Carried to Halt 1. Not to be quoted downstream as verified |
| A | Target 8b, Note 27, sheets 119-120 | Claimed unpaid statutory interest Rs 5.20m to Rs 16.22m. Source truth: NOT FOUND in rendered view, interest detail unlocatable at resolution. `source_fidelity: true` | RECLASSIFIED RESOLUTION-LIMITED, flag NOT cleared. Unconfirmed. Carried to Halt 1. Not to be quoted downstream as verified |
| B | B05 sections 2A and 2C. Concall_Feb_2026 p.14 vs p.5-6 | MISSED: the Feb-2026 claim "we were always guiding 10% to 15%, our growth is much more than that" is false against the same call's 9M FY26 growth of 7.6 percent standalone and 8.7 percent consolidated | Accepted. Closed by stage 5 run 3 as FLAG-MISSTATEMENT |
| B | B05 section 1B guidance table. Concall_May_2026 p.4 and p.11; Concall_Aug_2026 p.5 | MISSED: May-2026 FY27 guidance that renewables contribute 20 to 25 percent of total revenue is absent from B05's guidance table and never tested. Aug-2026 discloses no renewable revenue and Morena and Rewa still lack PPA or transmission | Accepted. Closed by stage 5 run 3 |
| B | B05 sections 1B and 2A. Concall_Aug_2026 p.4 and p.8 | MISSED: Q1 FY27 standalone revenue growth of 10.2 percent against a minimum 15 percent FY27 guidance reaffirmed in the same call; only the 15.7 percent consolidated figure is quoted, the shortfall never addressed | Accepted. Closed by stage 5 run 3 |
| B | B05 sections 2D and 4D. Concall_Aug_2026 p.11 | MISSED: "We have 100% utilized the IPO proceeds in the last quarter of the FY26" plus cessation of royalty income, disclosed only as an aside answering a question about other income, one quarter before an Rs 859cr FY27 equity plan | Accepted. Closed by stage 5 run 3 as FLAG-FUNDING-CAPACITY |
| B | B05 section 1B guidance table. Concall_Feb_2026 p.10; Concall_May_2026 p.6; Concall_Aug_2026 p.11 | MISSED: cash disclosed on a different basis in each of three quarters, Rs 225cr including FD (Dec-25), Rs 241cr unencumbered after erratum (Mar-26), Rs 320cr FDs (Jun-26). The Rs 320cr figure appears nowhere in B05 | Accepted. Closed by stage 5 run 3 |
| B | B05 section 4D. Concall_Nov_2025 p.12; Concall_Aug_2026 p.12 | MISSED: "We have 1.5 years to dilute another 8% also", an unexplained dilution or minimum public shareholding overhang stated once and never repeated on any of three later calls. An Aug-2026 analyst's "post-QIP" premise also left uncorrected | Accepted. Closed by stage 5 run 3 |
| B | B05 section 4D red flag row 5, B05 red_flags, B05 orchestrator note. Concall_May_2026 p.6 | Arithmetic wrong: the erratum is a 71.0 percent overstatement (171/241 = 70.95), not 41.5 percent (171/412 is the restatement down). The stated reason, that 71 percent conflates an absolute rupee change with a percentage, is false. The earlier audit's 71 percent was correct; the severity upgrade to HIGH stands | Accepted against the pipeline. The 71 percent figure was restored by stage 5 run 3 and the HIGH severity stands |
| B | 05-concall.md citation convention paragraph. See B12b report Part 4.3 table | At least nine B05 anchors are one page high in the Nov-2025 and Aug-2026 transcripts, matching the printed "Page N of M" header rather than the [PAGE N] marker the report says it used | Accepted. Stage 5 run 3 corrected about 30 carried forward page citations to the PDF's own [PAGE N] marker; substance unchanged in every case |
| B | 06-peers.md Q4. HGINFRA-Concall_May_2026 p.6 | Peer contrast overstated: HGINFRA's own May-2026 HAM equity schedule fails to reconcile by about Rs 1,000cr (Rs 1,903cr total less Rs 1,210cr infused = Rs 693cr remaining, against Rs 414 + Rs 1,229 + Rs 50 = Rs 1,693cr scheduled), so its drift is not milder than Ceigall's | Accepted against the pipeline by the orchestrator |
| B | B05 section 2B excuse pattern. Concall_Aug_2026 p.4-5 | Under weighted: the Northern Ayodhya collapse to about Rs 42cr is answered with a denial, a rain excuse and a milestone concession in one breath. B05 calls it "plausible and seasonal, not disputed" | Accepted. Re-weighed up by stage 5 run 3 |
| B | B05 section 4D and B06 Q9. Concall_May_2026 p.5 and p.9; HGINFRA-Concall_May_2026 p.6 | Under weighted: Ceigall's best quarterly margin of the year, 14.1 percent standalone in Q4 FY26, lands in the quarter HGINFRA's falls to 9.37 percent on unrecovered escalation, with any input cost impact denied. Neither artifact juxtaposes the two | Accepted. Re-weighed by stage 5 run 3 and by B06 run 2 |
| D | B06 Part 2B. Claimed HGINFRA-Concall_May_2026_Transcript.txt p.17 | Quote real, wrong page. Actual p.11. War situation quote resolving a B05 open item | Anchor offset. Substance correct, no B06 conclusion changes. Corrected in B06 run 2 |
| D | B06 Part 1 Q1 and Part 2C. Claimed HGINFRA-Concall_Aug_2025_Transcript.txt p.14 | Quote real, wrong page. Actual p.10. Ganga Expressway Rs 43cr margin item | Anchor offset. Substance correct. Corrected in B06 run 2 |
| D | B06 Part 1 Q4. Claimed PNCINFRA-Concall_Feb_2026_Transcript.txt p.13, defended as printed page 13 of 18 | Figures real, wrong page. Actual p.5; the cited page contains unrelated content. HAM equity Rs 1,744cr / Rs 1,110cr / Rs 634cr reconciliation | Anchor offset with an 8 page gap. Substance correct. Corrected in B06 run 2 |
| D | B06 Part 1 Q4 and Part 2C. Claimed PNCINFRA-Concall_May_2026_Transcript.txt p.9 | Quote real, wrong page. Actual p.11. "Diversification will pressure margins" quote | Anchor offset. Substance correct. Corrected in B06 run 2 |
| D | B06 industry_cross_read 2A, omission. HGINFRA-Concall_May_2026_Transcript.txt p.6 | HGINFRA's 87 percent FY26 order inflow guidance miss (Rs 10,000cr guided against Rs 1,300cr secured) not surfaced despite direct relevance and proximity to cited material | Genuine omission, not an anchor defect. Carried to Halt 1 as an open item rather than re-running the stage. Bears on B06's own flag that Ceigall's inflow beat in a soft award year needs its own explanation |

### MINOR

| Verifier | Location anchor | Finding | Disposition |
|---|---|---|---|
| A | Target 5, Note 63 sheet 130 and CARO sheet 76 | Claimed Rs 89.65m, 3 vendors, 6 employees, 4 sites, FIR 22-Jan-2026. Source truth: amount Rs 89.65m confirmed, FIR date confirmed, four sites confirmed; vendor and employee counts described qualitatively | Amount and date verified exactly. Counts plausible but unextracted |
| A | Target 8a, Note 27 sheets 119-120, payables | Claimed MSME Rs 409.93m to Rs 1,039.51m. Source truth: both figures confirmed | Payables verified exactly |
| A | Target 11, Annexure-3 sheets 44-45 | Claimed CMD Rs 125.52m at 6,276x. Source truth: table present, values unreadable at rendered resolution. `source_fidelity: true` | RECLASSIFIED RESOLUTION-LIMITED, flag NOT cleared. Unconfirmed. Carried to Halt 1. Not to be quoted downstream as verified |
| B | B05 Section 1. Concall_Nov_2025 p.6, p.9, p.10 | MISSED: Nov-2025 bid pipeline stated at Rs 14,320cr while its own components sum to Rs 14,382cr, quoted as Rs 14,000cr elsewhere in the same call, and an analyst's Rs 16,000cr left uncorrected | Accepted. Closed by stage 5 run 3 |
| B | B05 section 3B and B06 2A. Concall_Feb_2026 p.3; PNCINFRA-Concall_May_2026 p.5 | MISSED: Ceigall's MoRTH FY27 allocation of about Rs 3.1 trillion against PNCINFRA's Rs 2.9 trillion for the same year, both stated as +8 percent, never cross checked | Open. Part of the twelve item MINOR tail; the pipeline carries one of the twelve |
| B | B05 section 2B. Concall_May_2026 p.12 | MISSED: "one INR21,160 crores project" is a 10x error for the Rs 2,160cr Sahebganj award, correct on p.3 of the same file, left uncorrected in the same filed transcript that carries a written cash erratum | Accepted. Closed by stage 5 run 3 |
| B | B05 section 2A, Ramban-Banihal row. Concall_Nov_2025 p.11 | MISSED: the Ramban-Banihal figures do not cohere inside one exchange. Rs 385cr balance for both projects against Rs 369cr for one alone; 20 percent of tunnel work equals Rs 180cr; 54 percent physically against 45 percent financially complete | Accepted. Closed by stage 5 run 3 |
| B | B05 section 2F.5. Concall_Feb_2026 p.4, p.9 | MISSED: Feb-2026 leaves an analyst's "INR3,500 crores order book of solar and BESS" uncorrected against the Rs 3,168cr cumulative renewable orders stated in the same call | Accepted. Closed by stage 5 run 3 |
| B | B05 section 2A. Concall_Feb_2026 p.4, p.11 | MISSED: Feb-2026 claims "seven of our projects have completed ahead of schedule" while the same call discloses Jalbehra is late awaiting an EOT with bonus eligibility unresolved; the EOT is never revisited in May-2026 or Aug-2026 | Accepted. Closed by stage 5 run 3 |
| B | 06-peers.md Q10, Q6, Q5. PNCINFRA-Concall_Aug_2026 p.7, p.8, p.9 | B06 repeats the printed header off by one in the PNCINFRA Aug-2026 file at three anchors: p.8 should be p.7, p.9 should be p.8, p.10 should be p.9 | Accepted. Corrected in B06 run 2 |
| B | 06-peers.md Q5, Part 4, and B06 flags | B06 still describes Ceigall's governance silence as "3-call" in five places against a four call B05 run 2 | Accepted. The four call figure governs; see gate-recommendation.md Section 5 |
| B | 06-peers.md 2A and Part 3. KNRCON-Concall_Jun_2026 p.3; PNCINFRA-Concall_May_2026 p.4 | MISSED: KNRCON's 7,500km and PNCINFRA's 4,500km FY26 NHAI targets used side by side without noting the conflict. The awarded figures, 3,100km and 3,124km, do agree | Open. Part of the twelve item MINOR tail |
| C | B07 Section 2C / capex_embedded_growth_pct | Mandated capex times fixed asset turnover arithmetic not shown; justified as force fit avoidance but the block carries numeric 0 for not applicable. Recomputed: about 1.0 percent on a CWIP basis (Rs 3.58cr times 11.79x), about 9 to 10 percent on FY27 guided capex of Rs 30 to 35cr | No decision impact |
| C | B07 report L132, completionist recount line | States 4 categories is below the 3 to 6 completionist base rate; 4 sits inside 3 to 6. Recomputed: 4 categories with evidence, inside base rate; 0 reach Strong or Moderate | No decision impact |
| C | B07 block evidence_mix | claim count of 5 understates the management claim items tagged in the report body, which run to 7 or more distinct. Recomputed: claim 7 or more; documented 6 reconciles correctly to the recount | No decision impact |
| C | B07 block flags[1] against report YAML | The orchestrator repair altered the documented evidence glyph to the word "documented" in the FLAG-EMOAT-NETTED reason, beyond the disclosed single closing brace. No judgement changed | UPHELD against the orchestrator. Glyph restored and the repair note corrected to disclose both changes. Logged in verifier-disagreement-log.md |
| C | B01 Block F, M3 | ADVISORY. The M3 rule does not name the ROCE basis. The stage used FY26 (16.76 percent) and scored 3, stating the basis; median ROCE (22.72 percent) would score 5. Recomputed: M3 = 5 gives Block F 10/60 and grand total 47/160. moats_confirmed 2, moat_class MODERATE, core 37 and the AVOID classification are all unchanged | No decision impact |
| D | B06 Part 1 Q1. Claimed HGINFRA-Concall_May_2026_Transcript.txt p.6 | Quote real, wrong page. Actual p.5. "Temporarily increasing overall leverage" | Anchor offset. Corrected in B06 run 2 |
| D | B06 Part 1 Q7. Claimed HGINFRA-Concall_Feb_2026_Transcript.txt p.7 | Quote real, wrong page. Actual p.8. "No additional exceptional item" margin denial | Anchor offset. Corrected in B06 run 2 |
| D | B06 Part 1 Q6. Claimed KNRCON-Concall_Aug_2025_Transcript.txt p.8 | Figures real, wrong page. Actual p.7. Irrigation and HAM debtor figures | Anchor offset. Corrected in B06 run 2 |
| D | B06 Part 1 Q2. Claimed PNCINFRA-Concall_Feb_2026_Transcript.txt p.3 | Quote real, wrong page. Actual p.4. 377km against 504km | Anchor offset. Corrected in B06 run 2 |
| D | B06 Part 1 Q2. Claimed PNCINFRA-Concall_Aug_2026_Transcript.txt p.2 | Quote real, wrong page. Actual p.3. 107km awarded | Anchor offset. Corrected in B06 run 2 |

---

## VERIFIER A TARGETS RETURNING NO FINDING

Recorded because verifier A run 2 was a targeted adversarial pass over the
twelve hardest figures, not a representative sample, and the clean results
carry the run's core evidence.

| Target | Anchor | Claimed | Source truth |
|---|---|---|---|
| 2 | Note 7 consolidated, sheet 116 | RUSCA Rs 14,578.90m, +40.5 percent YoY | Rs 14,578.91m FY26, Rs 10,379.80m FY25, growth 40.47 percent. Matches within rounding |
| 3 | Note 46(ii) standalone, sheet 92 | Contingent liabilities Rs 17,554.78m at 83.7 percent of net worth | Sum of sub items Rs 17,555.28m, ratio 83.64 percent. Confirmed within rounding |
| 4 | Notes 45(ii) and 46(ii), sheets 121 and 92 | Consolidated FY25 Rs 3,411.75m, standalone Rs 8,403.35m bank guarantees | Both exact. The anomaly is real: consolidated below standalone, unreconciled |
| 6 | Note 19(a)/(b), sheet 117 | Held for sale assets Rs 5,431.08m, liabilities Rs 3,302.65m | Both exact. AOC-1 tie out confirmed |
| 9 | Note 12, sheet 116 | Receivables over 6 months 9.4 percent to 28 percent, balance -18.8 percent YoY | Dual ageing tables present; percentages and balance fall confirmed |
| 12 | Key Highlights, sheet 6 | Order book Rs 1,85,542.86m, 4.8x book to bill | Exact |

---

## STAGE REMEDIATION RECORD

| Stage | Runs | Reason |
|---|---|---|
| Stage 5 (concall) | 3 | Run 1 scoped to 3 of 4 transcripts under the input contract cap. Run 2 added the fourth plus cross call reconciliation. Run 3 closed the second audit's named residual gaps |
| Stage 6 (peers) | 2 | Run 2 fixed 18 citation anchors, re-ruled Q5 from UNVERIFIABLE to CONTRADICTED, and added three peer tests |
| Verifier A | 2 | Run 1 self declared it had not re-verified the notes stage AR citations. Run 2 targeted the twelve hardest figures |
| Verifier B | 2 | Run 1 measured 48 percent coverage against the pre remediation artifacts. Run 2 measured 70 percent against the remediated ones. Not run a third time: its independent flag list grew from 33 to 43 between passes, so a third pass measures a moving denominator |

Verifier disagreements this run: five against Verifier A findings, one against
the orchestrator. One Verifier A flag cleared on a source re-check, three held
as unconfirmed, one held with its framing corrected. Full rows in
outputs/final/verifier-disagreement-log.md.
