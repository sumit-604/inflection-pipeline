# Stage 12d: Verifier D — Peer Coverage Audit — Apex Ecotech Ltd (APEXECO)
Run date: 2026-07-10 | Model: claude-sonnet-5 | Stage: B12d
Inputs: 16 peer transcripts (CEWATER, EIEL, EMSLIMITED, FELIX x 4 quarters each), B06 peer report (runs/apexeco-2026-07-10/outputs/reports/06-peers.md), B05 peer_questions list (5 claims, injected in task).
Note on scope: the stage instruction file (prompts/12-verifiers-pipeline.md) references "12 peer transcripts"; the actual corpus supplied for this run is 16 transcripts (4 peers x 4 quarterly periods each). All 16 were read in full and audited.

Method: every SUBSTANTIVE citation in B06 Part 1 (claim-by-claim) and Part 2 (unprompted cross-read) was traced back to the named peer/quarter/speaker in the source transcript. All 16 transcripts were read end-to-end; Part 3's coverage map (all 16 marked SUBSTANTIVE, none UNUSED/CITED-ONLY) was checked both for citation accuracy and for material left on the table.

---

## PART 1: Coverage audit table — SUBSTANTIVE peers, citation-by-citation

| Peer / Quarter | Citation checked | Verdict | Note |
|---|---|---|---|
| CEWATER Q1 FY26 (Aug 2025) | "spread of small to medium size orders" — Prayas Goel | CONFIRMED | Verbatim match, correct speaker/call. |
| CEWATER Q2 FY26 (Nov 2025) | Guidance cut 18-20%→12-15%; Africa project delay; "one of the leaders" ZLD quote — Prayas Goel | CONFIRMED | Verbatim match. |
| CEWATER Q3 FY26 (Feb 2026) | Guidance cut to ~2%; Kenya delay; SAP re-implementation; CBG financial-closure delays | CONFIRMED | Matches transcript narrative closely. |
| CEWATER Q4 FY26 (May 2026) | Raw material/freight cost quote — Prayas Goel; ₹43cr Q4 shortfall, Sharjah/Middle East disruption; FY26 revenue -6.2% YoY to ₹557.8cr | CONFIRMED | Verbatim matches. |
| CEWATER Q4 FY26 (May 2026) | L1 orders worth ₹143cr incl. >₹100cr steel order, attributed to **"Manish Jain"** | **MAJOR — speaker misattribution.** The ₹143cr/steel-order quote is verbatim in the transcript, but is spoken by **Prayas Goel**, not Manish Jain. CEWATER's management across all 4 calls is Prayas Goel, Prerak Goel, Anish Goel, Sudarshan Kamath, Abhijit Ghalke — no Manish Jain is ever on a CEWATER call. Manish Jain is EIEL's Managing Director. This looks like cross-contamination between two peer transcripts during citation-writing. |
| EIEL Q1 FY26 (Aug 2025) | "$22 billion" global wastewater reuse market — Manish Jain | CONFIRMED | Verbatim. |
| EIEL Q1 FY26 (Aug 2025) | ₹11.15cr cyber fraud disclosure | CONFIRMED | Verbatim, matches exactly incl. recovery amounts. |
| EIEL Q1 FY26 (Aug 2025) | **"about Rs. 15 lakh crores potential of the work... only in urban cities"** against **"only done 3 lakh crores in AMRUT"** — attributed to "EIEL's Manish Jain" | **CRITICAL — fabricated source attribution.** This exact quote is real and verbatim, but it was said by **H.K. Kansal of EMSLIMITED**, in EMSLIMITED's Q1 FY26 call (Sept 3, 2025) — not by EIEL's Manish Jain, and not in EIEL's Aug 2025 call. The EIEL Aug 2025 transcript contains no reference to "15 lakh crore" or "urban cities" anywhere. This is a complete misattribution of company, speaker, and date for a quote used as primary evidence in Claim 1. |
| EIEL Q2 FY26 (Nov 2025) | Order book growth, JJM funding normalization | CONFIRMED | Consistent with transcript. |
| EIEL Q3 FY26 (Feb 2026) | Revenue guidance miss, Delhi re-bidding, Bihar delays, unbilled revenue build-up | CONFIRMED | Matches transcript (Delhi re-bidding, Bihar ₹3,000cr evaluation delay, ECL provisions). |
| EIEL Q4 FY26 (May 2026) | "Given that we do have a global crisis, I am reducing my EBITDA guidance to somewhere around 21% to 22%" — Manish Jain | CONFIRMED | Verbatim. |
| EIEL Q4 FY26 (May 2026) | Raw material cost quote; lithium-ion deferred procurement | CONFIRMED | Verbatim. |
| EIEL Q4 FY26 (May 2026) | "increasing our pre-qualification capabilities for the complex wastewater treatment plants" — Manish Jain | CONFIRMED | Verbatim. |
| EIEL Q4 FY26 (May 2026) | Order book >₹6,814cr; NTPC BESS ₹1,070cr; renewable segment ~₹3,130cr (₹2,051cr execution + ₹1,079cr O&M/IPP) | CONFIRMED | All figures match exactly. |
| EIEL Q4 FY26 (May 2026) | Unbilled revenue 195 days | CONFIRMED | Verbatim ("the UBR days are 195 days"). |
| EMSLIMITED Q1 FY26 (Sept 2025) | Monsoon commentary; JJM vs AMRUT funding distinction; debt-free philosophy quote — H.K. Kansal | CONFIRMED | Verbatim. |
| EMSLIMITED Q2 FY26 (Nov 2025) | 26-27% YoY Q2 revenue decline, monsoon halting digging across six states | CONFIRMED | Verbatim. |
| EMSLIMITED Q2 FY26 (Nov 2025) | "in listed companies, there are no very much our competitors. But in unlisted sectors, there are many 8, 10 sectors of size 8, 10 companies of our size" — H.K. Kansal | CONFIRMED | Verbatim, correctly dated to Nov 2025 in Part 1 Claim 4. **However, Part 3's coverage-map row for EMSLIMITED Q1 FY26 (Sept 2025) also claims this same "fragmented unlisted-competitor landscape" datapoint feeds Claim 4** — that is a quarter mismatch (MINOR, internal inconsistency, not fabrication, since the correct Nov 2025 citation is present and used correctly in Part 1). |
| EMSLIMITED Q3 FY26 (Feb 2026) | Uttarakhand flood disruption continuing into Q3, working capital stretch | CONFIRMED | Matches transcript. |
| EMSLIMITED Q4 FY26 (May 2026) | FY26 revenue ₹608cr standalone vs ~₹1,200-1,300cr guided; West Bengal election disruption (₹780cr project); SPARSH portal payment delay | CONFIRMED | All verbatim/numerically matching. |
| EMSLIMITED Q4 FY26 (May 2026) | Promoter pledge ~7%→~28% across FY26 | CONFIRMED | Progression (7%→11%→24%→28%) tracks across the four calls. |
| EMSLIMITED Q4 FY26 (May 2026) | "it does not take much to be transparent... give a realistic projection henceforth" — attributed generically as investor pushback | **MINOR — spliced quote, two different speakers.** "It does not take much to be transparent" is Azar (individual investor); "give a realistic projection henceforth... only achievable targets and realistic targets" is a separate, later exchange with Sheetal Shah. Both are real, both are from the same May 2026 call, but B06 presents them as one continuous quote. Cosmetic, not fabrication. |
| FELIX Q1 FY26 (Sept 2025) | SME quarterly-reporting confirmation quote — Ritesh Patel | CONFIRMED | Verbatim, exact match ("this time the company came up with quarterly results instead of 6 monthly..."). |
| FELIX Q2 FY26 (Nov 2025) | Va Tech Wabag peer margin comparison (GPM 22% vs Felix 70%; EBITDA 13% vs 22%) | CONFIRMED | Verbatim (Taher Hydrabadwala's question, Ritesh Patel's answer). |
| FELIX Q2 FY26 (Nov 2025) | **"In maximum of the contracts, it is a price variation clause which is applicable... So a part of the cost increase will definitely get offset... it does not take into account the entire price increase in the market... we are required to lower our guidance"** — attributed to Nishant Sharma | **CRITICAL — quote not found.** This exact quote does not appear anywhere in the Nov 21, 2025 FELIX transcript (nor in the Feb 2026 or June 2026 FELIX transcripts checked as alternates). No discussion of "price variation clause" appears in any FELIX transcript reviewed. This is presented in quotation marks as a direct, on-point verbatim answer to the fixed-price-contract-handling sub-question in Claim 2 and cannot be verified as real. |
| FELIX Q3 FY26 (Feb 2026) | Oman LNG contract (~₹45-46cr, 5-year open contract); metal/plastic recycling diversification | CONFIRMED | Verbatim (Abhay Musale/Ankur Gulati exchanges). |
| FELIX Q4 FY26 (June 2026) | FY26 consolidated results: revenue ₹102.21cr (+178%), EBITDA ₹31.88cr (+131%), PAT ₹18.18cr (+100%) | CONFIRMED | All figures verbatim. |
| FELIX Q4 FY26 (June 2026) | "war" disrupting Oman operations; "global liquidity challenge" — Nishant Sharma | CONFIRMED | Verbatim. |
| FELIX Q4 FY26 (June 2026) | CS Hena Shah — 5-6 month main-board migration timeline | CONFIRMED | Verbatim ("It'll take around, 5 to 6 Months"). |

---

## PART 2: UNUSED / CITED-ONLY peers

None. B06's Part 3 coverage map marks all 16 transcripts SUBSTANTIVE and states "All 16 transcripts were substantively used; none were cited-only or unused." Having read all 16 transcripts in full, I confirm this framing is directionally accurate — every transcript does contain material that is genuinely used somewhere in B06 Parts 1-2, and no transcript sat idle. There is no peer/quarter I would recategorize as UNUSED or CITED-ONLY.

Spot-check for left-on-the-table material (per Rule 3, applied even though no peer is formally UNUSED): nothing rises to a MAJOR miss. Two MINOR industry-context items not picked up by B06:
- CEWATER Q1 FY26 (Aug 2025): management states "India is one of the leaders in zero-liquid discharge and recycling" and cites a "50% operating cost advantage" claim vs global players (Nov 2025 call) — B06 uses the "leaders" framing for Claim 1 but does not flag the unsupported "50% operating cost advantage" figure, which is a comparable unaudited claim to the one under scrutiny in Claim 1. MINOR industry-context miss.
- EIEL Q1 FY26 (Aug 2025): Sandip Sabharwal's exchange on receivable cycle (~90 days) and the "50-60 companies of our size can be saturated with the workload" TAM framing (this is actually from EMSLIMITED, not EIEL — see CRITICAL finding above) was available but not cross-referenced against Apex's own receivable-cycle disclosures. MINOR.

---

## PART 3: Verdict-discipline audit (per B05 peer_questions, 5 claims)

| # | Claim | B06 verdict | Peers cited | Discipline check |
|---|---|---|---|---|
| 1 | ZLD/water-recycling penetration % consistency | UNVERIFIABLE | None (peers silent on the specific %) — cites TAM figures instead, one of which (the "15 lakh crore" quote) is misattributed (see CRITICAL above) | Verdict itself is appropriate given genuine peer silence on penetration %; not "upgraded from silence." But the supporting TAM evidence offered as color is fabricated in its sourcing. |
| 2 | 25-40% raw material cost inflation, H2 FY26, fixed-price handling | PARTIALLY VERIFIED (direction only) | CEWATER (2 calls) + EIEL (1 call) for direction/magnitude/timing; FELIX (1 call, price-variation-clause quote) for contract-handling mechanism | Direction claim rests on ≥2 independent peers (CEWATER + EIEL) — correctly not scored VERIFIED given magnitude/timing divergence. The contract-mechanism sub-claim rests on a single peer (FELIX) with a quote that could not be verified as real (CRITICAL finding above) — this sub-claim should not have been presented as "useful, directly on-point evidence" without a verifiable anchor. |
| 3 | Top 1/3/5 customer concentration & peer disclosure practice | UNVERIFIABLE | All 4 peers, silent | Verdict appropriate; genuine silence, not upgraded. |
| 4 | Market consolidation | PARTIALLY VERIFIED (weak) | EIEL + CEWATER (own book mix) vs EMSLIMITED (contradicting) | Correctly uses ≥2 peers and correctly does NOT claim VERIFIED given the contradicting EMSLIMITED evidence; verdict discipline is sound here. |
| 5 | SME six-month carve-out, voluntary quarterly disclosure | PARTIALLY VERIFIED (single peer, explicitly flagged as such) | FELIX only (correctly the only SME-listed peer in the set) | Correct application of the two-peer rule — B06 explicitly states "cannot be scored VERIFIED under the two-peer rule" for a single-peer data point. This is the discipline working exactly as intended. |

No claim was upgraded from silence to a positive verdict anywhere in B06. No VERIFIED claim rests on a single peer (there are zero VERIFIED claims in this report — the two-peer rule is applied correctly throughout, including the FELIX/SME case where B06 explicitly self-limits to PARTIALLY VERIFIED).

All 5 claims from the injected peer_questions list received a verdict. None were skipped.

---

## Overall assessment

B06's verdict discipline (Part 4, triangulation summary) is sound: conservative UNVERIFIABLE/PARTIALLY VERIFIED calls, correct application of the two-peer rule, no verdicts upgraded from silence, and an honest flag that the raw-material-cost claim's magnitude/timing diverge from peer evidence. The peer coverage is genuinely broad and none of the 16 transcripts sit unused.

The material problem is citation integrity on two specific quotes used as primary evidence: the EIEL Aug-2025 "15 lakh crore/AMRUT" TAM quote is actually EMSLIMITED's H.K. Kansal from a different call three weeks later, and the FELIX Nov-2025 "price variation clause" quote could not be located anywhere in the FELIX transcript corpus. A third citation (CEWATER May-2026 L1/steel order) is correctly sourced to the right call but wrongly attributed to "Manish Jain," a name that belongs to a different peer company (EIEL) entirely — a naming cross-contamination error. These are the kind of errors a downstream reader would not catch without independently re-opening the source PDFs, and two of them sit inside claims (1 and 2) that synthesis is likely to treat as peer-corroborated color.

---

```yaml
stage: B12d
company: "APEXECO"
run_date: "2026-07-10"
model: claude-sonnet-5
status: complete
peers_audited: 16
substantive_confirmed: 13
substantive_unsupported:
  - "EIEL Q1 FY26 (Aug 2025) — '15 lakh crore urban / 3 lakh crore AMRUT' quote fabricated-sourced; actual speaker is EMSLIMITED's H.K. Kansal, EMSLIMITED Q1 FY26 (Sept 2025) call, not EIEL/Manish Jain"
  - "FELIX Q2 FY26 (Nov 2025) — 'price variation clause' quote attributed to Nishant Sharma not found anywhere in the FELIX transcript corpus (checked Sept 2025, Nov 2025, Feb 2026, Jun 2026)"
  - "CEWATER Q4 FY26 (May 2026) — L1/₹143cr steel-order quote is real and correctly dated but misattributed to 'Manish Jain,' who is EIEL's MD, not a CEWATER speaker; actual speaker is Prayas Goel"
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "CRITICAL", location: "B06 Claim 1, Peer evidence row / Part 3 coverage map, EIEL Q1 FY26 row", claimed: "EIEL's Manish Jain, Q1 FY26 call (Aug 2025): 'about Rs. 15 lakh crores potential of the work... only in urban cities' / 'only done 3 lakh crores in AMRUT'", source_truth: "Quote is real but spoken by EMSLIMITED's H.K. Kansal in EMSLIMITED's Q1 FY26 call (Sept 3, 2025); not present anywhere in the EIEL Aug 2025 transcript", note: "Complete misattribution of company, speaker, and date for a quote used as primary TAM evidence in Claim 1"}
  - {severity: "CRITICAL", location: "B06 Claim 2, Peer evidence row, FELIX Q2 FY26 (Nov 2025) citation", claimed: "Nishant Sharma quote on price variation clauses offsetting cost increases, cited as 'directly on-point evidence of standard peer practice'", source_truth: "No such quote or discussion of price variation clauses appears in the FELIX Nov 21 2025 transcript, or in the Sept 2025, Feb 2026, or Jun 2026 FELIX transcripts", note: "Presented in quotation marks as verbatim; could not be located in the source corpus"}
  - {severity: "MAJOR", location: "B06 Claim 4, Peer evidence row, CEWATER Q4 FY26 (May 2026) citation", claimed: "L1 status on ₹143cr orders incl. >₹100cr steel order, attributed to 'Manish Jain'", source_truth: "Quote is verbatim and correctly dated to CEWATER's May 2026 call, but the actual speaker is Prayas Goel; 'Manish Jain' does not appear on any CEWATER call across all four transcripts and is in fact EIEL's Managing Director", note: "Speaker name cross-contaminated from a different peer company; underlying data and call/quarter attribution are otherwise correct"}
  - {severity: "MINOR", location: "B06 Part 3 coverage map, EMSLIMITED Q1 FY26 (Sept 2025) row vs Part 1 Claim 4 text", claimed: "Part 3 attributes the 'fragmented unlisted-competitor landscape' datapoint to the Sept 2025 (Q1) call", source_truth: "The actual quote ('8, 10 sectors of size 8, 10 companies of our size') is from the Nov 2025 (Q2) call, correctly cited in Part 1's Claim 4 text", note: "Internal inconsistency within B06 itself; the correct citation exists elsewhere in the same report so this is not a fabrication"}
  - {severity: "MINOR", location: "B06 Claim 4 net-read paragraph, EMSLIMITED Q4 FY26 (May 2026) citation", claimed: "'it does not take much to be transparent... give a realistic projection henceforth' presented as a single continuous investor quote", source_truth: "These are two separate remarks from two different individual investors (Azar and Sheetal Shah) in the same call, spliced together with an ellipsis", note: "Both fragments are real and correctly dated; splicing without speaker differentiation is a presentation issue, not fabrication"}
critical_count: 2
major_count: 1
minor_count: 2
acceptance_rate: 81
```
