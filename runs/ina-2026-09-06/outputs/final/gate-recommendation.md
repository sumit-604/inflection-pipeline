# INA (Insolation Energy Ltd) gate recommendation

Run: ina-2026-09-06. Phase 1 (evidence stages 0 to 9 plus verifiers A to D). Stages 10 and 11 have not run. B10 and B11 do not exist. No valuation, no entry zone, no destination PE, no Hurdle verdict appears anywhere in this file. The investment decision is formed in phase 3. This is the gate decision on evidence alone.

## MISSING MATE DOCUMENT (read this first)

**MISSING: the Q1FY27 results filing for the quarter ended 30 June 2026, and its earnings call transcript.**
Expected source: BSE and NSE corporate filings for Insolation Energy Ltd, or the company investor relations page.
Why it is named first: B00.freshness_verdict is CORPUS GAPPED-FRESHNESS. The freshness pair "results-to-concall" is FAIL. The trigger document exists (the Q1FY27 print is evidenced in screener-Data_Sheet.csv, showing sales Rs 740.70cr and PAT Rs 37.04cr against Q4FY26 sales Rs 793.93cr and PAT Rs 70.07cr, so profit roughly halved). Neither its filing nor its call is in the corpus. Every downstream stage in this run reasons about a company whose newest disclosed quarter it cannot read (B00.analyst_note).

The freshness rule independently caps the verdict at PROCEED WITH CAVEATS (B00 FLAG-FRESHNESS). REWORK is more severe than that cap, so REWORK stands and the freshness cap is subsumed, not waived. The document is still required before phase 3.

---

## VERDICT: REWORK

⚠️ PROMOTER FLAG: CONCERN. Top findings: [1] Rs 32.5cr invested in two LLPs (Happy Buildmart LLP, Harmony Buildstate LLP) 90 percent owned by the two promoter director families, with no disclosed rationale and no arm's length pricing statement (AR Note 8, p.121). [2] Factory land title conflict: Note 4 and CARO clause (i)(c) state title deeds are company held, while Note 18A shows the same land mortgaged in the two promoters' personal names (AR p.120, p.126-127).
Transition evidence: (a) Manish Gupta (Chairman) increased personal shareholding by open market purchase during FY26 (MEDIA tier: ScanX / exchange disclosure coverage); (b) Vikas Jain HUF increased its stake by open market purchase during FY26 (MEDIA tier); (c) three new independent directors appointed in FY26 with substantive, verifiable outside credentials, Dr. Subir Bikas Mitra (ex Executive Director GAIL India, dual PhD), Mr. Rajiv Jain (ex NHRC Member, ex Intelligence Bureau Director) and Mr. Shreemat Pandey (ex IAS 1984 batch, IIT Kharagpur), each approved by 99.85 percent or more of shareholder votes by postal ballot (AR p.54, p.73-74); (d) Main Board migration and direct NSE listing completed 9 March 2026, raising the ongoing disclosure and compliance bar above the prior BSE SME platform (AR p.53); (e) FII holding rose from 0.94 percent (Mar 2025) to 1.09 percent (Mar 2026) (MEDIA tier, aggregator data), directionally positive though small.

### The rule that produced REWORK

Two independent rules in prompts/00-orchestrator.md force this verdict. Either alone is sufficient.

1. **Section 5, confidence band.** `overall` is the minimum of the four verifier components. It is 42. The band rule is: below 60 forces REWORK (confidence.yaml band_rule).
2. **Section 4, FLAG RULES.** "any verifier's acceptance_rate falls below 60% ... the synthesis verdict is REWORK regardless of company quality". B12b.acceptance_rate is 34 percent strict (20 caught of 59 independently found flags), 42 percent with partial credit at half for 9 partially caught items, and 49 percent counting partial as caught. All three conventions sit below 60 (B12b.acceptance_rate_note).

Verdict selection rule applied: **rule 1** (prompts/13-synthesis-pipeline.md, verdict selection rules).

### REWORK judges the ANALYSIS, not the company

This is the whole point of the rule and it is stated plainly here so no reader mistakes it. REWORK says the pipeline's own work on two stages cannot be trusted as complete. It says nothing about whether Insolation Energy is a good or bad business. No company quality finding in this run halts anything; flags propagate, the decision stays human.

The evidence base itself is sound. Verifier A checked 18 material claims across verdict card inputs and key financial metrics and found **zero CRITICAL** findings at 83 percent acceptance, with no fabricated number, no anchor not found error and no material unanchored figure (B12a.coverage_note). Verifier C found **zero CRITICAL** at 86 percent framework adherence over 94 rules on Gate 0 and Emerging Moat (B12c). Verifier D found **no fabricated quotes**, every peer quote genuine and correctly attributed, at 91 percent peer utilisation (B12d).

Verifier B, the concall red flag layer, is the sole failure, and it failed on **COVERAGE, not accuracy**. Verifier B spot checked six of B05's promise delivery rows and confirmed all six with zero wrong (B12b.promise_delivery_spot_checks). It found **no unsupported pipeline flag** (B12b.pipeline_flags_not_supported is empty). It concurs that credibility grade D is correct and that the additional evidence removes any case for a higher grade (B12b.credibility_grade_concur). B05 and B06 did not get things wrong. They missed a great deal.

### What must be reworked: STAGES 5 AND 6 ONLY

Not the whole run (confidence.yaml rework_scope). Stages 0 to 4 and 7 to 9 stand.

A rerun of stage 5 (concall) must fix:
1. **Internal arithmetic inside a single call.** The single largest miss class. Seven CRITICALs turn on numbers the same management stated elsewhere in the same document. Named examples: the CFO answering "Yeah" to whether the 2,000 MW FY26 target was on track while H1 was about 360 MW and he cut revenue guidance 40 percent eight pages later (Concall_Feb_2026 p6, p5-6, p13); the FY27 capital plan that does not close, Rs 2,500cr capex and Rs 2,129cr implied debt against a stated Rs 1,500cr peak debt with no equity raise mentioned (Concall_Jun_2026 p9, p10, p11, p20); the Managing Director stating "we are not working as an EPC or IPP" in the same call carrying a 400 MW IPP target, Rs 1,000cr KUSUM IPP capex and a Rs 300cr EPC order (Concall_Jun_2026 p8 against p4 and p9).
2. **Guidance basis switching.** FY27 margin guidance of 14.01 percent PAT (Concall_Jun_2025 p8) reappeared as 14 to 15 percent EBITDA (Concall_Jun_2026 p16-17) with the numerals held constant. On FY26's own 14 percent EBITDA to 9.3 percent PAT relationship that is a 4 to 5 point PAT downgrade, never stated. Not detected.
3. **Promise tracker completeness.** Three misses absent from B05 section 2A: FY26 module volume 2,000 to 2,100 MW delivered at about 1,224 MW, a 41 percent miss; FY26 EPC revenue Rs 400cr delivered as "very small realization"; Units 1 and 2 MonoPERC to TOPCon conversion promised for September 2025. Adding them moves the tally from 1 delivered / 5 partial / 5 missed to 1 delivered / 5 partial / 8 missed.
4. **Capacity basis.** The CFO redefined usable capacity as 50 to 55 percent of nameplate (Concall_Feb_2026 p18), which reduces the 5.5 GW headline to 2.75 to 3.0 GW of real output. Not tested.
5. **Citation basis.** Stage 5 cited each transcript's printed "Page X of Y" footer instead of the extraction "===== PAGE N =====" marker. An unnumbered SEBI cover letter offsets the two by exactly one page on every transcript. Name the extraction marker as the sole anchor authority and bar the printed footer.

A rerun of stage 6 (peers) must fix:
1. **Peer verification of OPERATING NORMS, as distinct from peer prices and dates.** B06 verified realisations and regulatory dates cleanly. It did not test utilisation, ramp duration or capex per GW against peers, which is where three of Verifier B's seven CRITICALs sit. Named: INA's wafer and ingot capex of Rs 222 to 267cr per GW is 55 to 62 percent below Premier's Rs 590cr per GW (Jan-2026 p6) and Waaree's Rs 620cr per GW (May-2026 p3), never tested.
2. **Execute the stage 5 hand off.** B05 flagged the Emvee and Premier DCR cell tie up as worth checking against Premier's own concall. Stage 6 never checked it. Premier states it "will not have a lot of cells to sell" once its own cell line runs (Aug-2026 p4) and will skew to internal consumption as ALMM Phase 2 lands (p18). DCR is 15 percent of INA volume and carries the whole price premium. `peer_questions[]` must be a checklist stage 6 ticks, not a suggestion.
3. **Two overstated conclusions.** See the contradicted claims section below.
4. **Anchor discipline.** Verifier D logged two MAJOR citation location errors on load bearing Q1 and Q5 claims, one anchor reused three times including in the highest priority YAML flag. Same printed footer versus extraction marker defect as stage 5.

---

## ACTIVE FLAG BLOCKS

### FLAG-CASH

```
⚠️ CASH CONVERSION FLAG: consolidated operating cash flow swung from +Rs 34.68cr
(FY25) to -Rs 73.13cr (FY26) against PAT of Rs 200.63cr. CFO/PAT -36.5%,
CFO/EBITDA -24.0%. Working capital days rose 31.48 to 62.58. Receivables aged
beyond 6 months rose 5.7% (1-Apr-2024) to 12.1% (FY25) to 39.5% / Rs 111.35cr
(FY26). Direction: deteriorating.
Determination: INDETERMINATE (leaning STRUCTURAL, not established).
```

**Evidence weighed.**

Against GROWTH-INDUCED, the peer test is the decisive item. The letter of credit mechanism INA's management offers as the explanation is real and sector standard: Websol confirmed on its 28 April 2026 call that receivables "backed by letter of credit from prime banks" are "in line with the industry benchmark also" (B06 Q7, Websol 28-Apr-2026 p.19-20). The same peer, using the same mechanism in the same year, converted Rs 303cr of FY26 PAT into Rs 255cr of operating cash, 84 percent (Websol 28-Apr-2026 p.4), and ended the year net cash surplus. INA converted none. The mechanism therefore does not explain a collapse of INA's magnitude (B06.analyst_note, flagged as the priority item for synthesis).

Ageing works against the growth reading on its own logic. A working capital ramp adds new receivables that are current by definition. It does not age an existing book. The share beyond six months nearly tripled in one year and rose sevenfold in two (Note 13, p.122-123). Zero ECL provision sits against every bucket in every year with no disclosed methodology (Note 13, p.122-123). Revenue also concentrates in the last month of each quarter, December Rs 350cr of Q3's Rs 575cr and March Rs 440cr or more of Q4's Rs 794cr, normalised by management as an industry habit (Concall_Jun_2026 p14-15, via B12b MAJOR). And management's own February 2026 claim of about Rs 220cr FY26 cash accruals was contradicted by the audited minus Rs 73.13cr and has never been reconciled on any call (B05 red_flags, HIGH).

For GROWTH-INDUCED, capacity did scale in the same year. The Sawarda 4.5 GW module facility was commissioned inside FY2026, taking total module capacity to 5.5 GW (B03 guidance_table, VERIFIED DELIVERED). Inventory rose 4.9 times and finished goods about 14.7 times against 60.9 percent revenue growth (Note 12, p.121-122). Capex of Rs 430.63cr to Rs 448.05cr tracks Rs 901.43cr of capital commitments cleanly across P and L, cash flow and notes (B03 strengths_top3). The ageing sits entirely at the subsidiary; the listed parent's standalone book stayed at about 6 percent aged beyond six months (Note 12 standalone p.166). A one year build ahead of collections remains a live reading that this corpus cannot close.

**Why the determination is INDETERMINATE and not one of the other two.** B02 pass 3 left the question open on note evidence alone and said so: "The cash-inversion question (Lead 2) is genuinely unresolved from the notes alone; treat as an open item requiring the missing Notes 1-3 policy text and customer-level ageing, not a settled read either way" (B02.analyst_note). B03 independently confirmed the inversion against the Consolidated Statement of Cash Flows (p.117-118) and found that no narrative section anywhere in the annual report explains it, only a mechanical one line ratio table remark (B03 FLAG-CASH). Three pieces of evidence that would settle it are absent from the corpus. Per prompts/00-orchestrator.md Section 4, INDETERMINATE never silently resolves to PROCEED, and the missing evidence is named below.

**Missing evidence, named, with where to obtain it.**

| # | Missing item | Why it settles the question | Where to obtain it |
|---|---|---|---|
| 1 | Notes 1 to 3, Material Accounting Policies. Absent from the entire 200 page AR extraction though both balance sheets and the audit report cross reference them; verified by two extractors, no image only pages (B00 gap `annual-report-notes-1-3-absent`, HIGH; B02 top_findings rank 12) | Revenue recognition policy and ECL methodology are both unreadable. Without the ECL policy the zero provision against a 39.5 percent aged book cannot be judged | The filed FY2026 annual report on BSE or NSE corporate filings, or the company investor relations page |
| 2 | Any credit rating rationale. Zero rating PDFs in the corpus and none exists for the FY26 borrowing step up from Rs 108cr to Rs 888cr (B00 gap `rating`, MEDIUM) | The orchestrator's FLAG-CASH block calls for the rating agency verbatim working capital commentary. No such quote can be reproduced from this corpus. NOT FOUND | The rating agency rationale page for Insolation Energy Ltd (CARE, CRISIL, ICRA or India Ratings); CARE Ratings already acts as IPO proceeds monitoring agency per CARO |
| 3 | Receivables ageing by customer, specifically the Rs 265.19cr Solarworld Energy Solutions Ltd balance at 12.4 percent of FY26 revenue and NIL in FY25 (Note 46, p.144) | Customer concentration is the leading hypothesis for the severity of the collapse (B09 downstream candidate, B06.analyst_note). No ageing by customer is disclosed anywhere | Direct management query at Halt 1, or the FY2027 annual report trade receivables note |
| 4 | The Q1FY27 results filing and its cash flow statement, quarter ended 30 June 2026 | One quarter of post FY26 collections data resolves the ramp reading directly | BSE and NSE corporate filings, or the company investor relations page. Same document as the freshness gap above |

**The single metric that resolves the determination.** Trade receivables aged beyond six months, as a share of the consolidated trade receivables book, in the next disclosed ageing schedule. Below about 20 percent resolves toward GROWTH-INDUCED. At or above the FY26 level of 39.5 percent resolves toward STRUCTURAL. Where to find it: the trade receivables ageing note in the FY2027 annual report, or the half year filing if the company discloses ageing at H1. This metric is carried into the monitorables list below and is the run's falsification metric.

### FLAG-PROMOTER

Stated in full inside the verdict line above, per prompts/00-orchestrator.md Section 4, which requires the block inside the verdict line and never in an appendix. Verdict CONCERN. Scorecard 3 clean / 3 caution / 4 red. Deal breaker recorded not enforced: multiple mid term independent director exits within about 2.5 years (Alpesh Fatehsingh Purohit resigned 10 February 2024 citing "pre-occupancy with other assignments"; Pallavi Mishra ceased 30 June 2026 citing "professional commitments elsewhere", also NRC Chair at exit). B08 status is `partial`: four searches were skipped for lack of MCA, ICAI and BSE PDF tool access this session (B08.searches_skipped). Twenty six searches were performed and the legal and regulatory record came back clean.

Two further findings sit behind the top two named in the verdict line: AOC-2 (Annexure III, p.64) states related party disclosure is "Not applicable" for both arm's length and non arm's length categories while Note 41 (p.135-137) discloses a full page of named, quantified promoter and promoter family transactions; and Payal Gupta, Manish Gupta's spouse, sits on the Nomination and Remuneration Committee that recommends the promoters' own remuneration, labelled "Independent Director (Non-Executive)" in the committee tables at p.77 and correctly labelled non independent in the main board table at p.73 of the same document.

The unverified name coincidence between a partner at the outgoing statutory auditor and Manish Gupta's late father is recorded as a lead only and must not be carried forward as fact without ICAI corroboration (B08.analyst_note).

### FLAG-GATE0

```
⚠️ GATE 0 FLAG: classification AVERAGE. Core score 54/100. Moat score 15/60.
Grand total 69/160. Moats confirmed 4/12, moat class STRONG.
Blocks: A 14, B 2, C 20, D 13, E 5.
```

Depressor detail, in full. Block B scored 2 of 20. Two deal breaker triggers fired: Block B below 8 (actual 2), which caps classification at GOOD and has no net effect since the class is already AVERAGE; and cumulative five year CFO/PAT below 0.50 (actual 0.194), which caps classification at AVERAGE. Both depressors are concentrated entirely in FY2026. CFO swung from plus Rs 113.10cr (FY2025) to minus Rs 73.13cr (FY2026) while PAT rose from Rs 126.20cr to Rs 200.22cr. Working capital days rose from 31.48 to 62.58, driven by inventory (Rs 76.98cr to Rs 379.05cr) and receivables (Rs 110.09cr to Rs 281.59cr) both outrunning payables growth. FY2022 to FY2025, on the standalone basis of that period, was healthy: FY2025 alone converted at 0.90x PAT.

Are the depressors historical? No. They are the newest year in the series, which is the opposite of the post IPO rebase or legacy cleanup pattern the flag is designed to record. Gate 0 flags two further items: the unresolved intra group contingent guarantee overhang of about Rs 1,654cr at 205 percent of net worth (Note 42), and a consolidation scope restatement that makes the five year growth CAGR not fully like for like (AR restates the 1 April 2024 opening balance sheet for six subsidiaries incorporated July 2024 to August 2025; restated FY2024 total assets Rs 274.69cr and FY2025 CWIP Rs 52.88cr do not match screener's unrestated Rs 262.78cr and Rs 46.10cr).

Gate 0 AVERAGE caps nothing by itself. Position sizing logic in Role 2 handles the override; the pipeline surfaces it.

Verifier C recomputation, carried for the record and not applied: moat score 16 and grand total 70 under an alternate M7 reading; moat count 4 and classification AVERAGE unchanged either way. Verifier C concurs with core score 54 and with classification AVERAGE.

### FLAG-GUARANTEE

```
⚠️ GUARANTEE FLAG: corporate and counter guarantees of Rs 1,654.01cr as at
31-Mar-2026, up 16.6x year on year, backing subsidiary borrowings including a
Rs 1,134cr IREDA facility. 205% of consolidated net worth. 825% of consolidated
PAT. 3.0x the listed parent's own standalone total assets of Rs 544.04cr. No
covenant disclosure anywhere.
Anchor: AR Note 42(i), p.137 (verified exactly by B02, B03 and Verifier A).
```

The structure includes a reverse leg: wholly owned subsidiary Insolation Green Energy Pvt Ltd guarantees a Rs 24.96cr AU Bank facility taken by the parent itself (Note 42, p.137). The exposure will rise mechanically as the IREDA facility draws: Rs 468.89cr of aggregate secured non current borrowings stands against a Rs 1,134cr sanction, with the first repayment due December 2027 (Note 18A, p.124-127). Capital commitments are Rs 901.43cr against roughly Rs 807cr of net worth (Note 42(b), p.138), up from Rs 152.08cr in FY25 and Rs 1.28cr in FY24.

Verifier A ruled the CARO cross reference: the CARO clause (iii) figure of Rs 15.78cr (p.156) and Note 42(i)'s Rs 1,654.01cr (p.137) are **both correct at different consolidation scopes**, standalone parent only direct guarantee versus consolidated group total. Not a discrepancy. Stage 3's flag was reasonable because the AR gives no cross reference between the two. The substantive concern is unaffected: the parent guarantees Rs 1,654.01cr against Rs 544.04cr of its own assets. The guarantee is not fresh off balance sheet risk to be double counted, since the underlying Rs 887.91cr of group borrowings already sits on the consolidated balance sheet (B01 data_notes).

### FLAG-RPT

```
⚠️ RELATED PARTY FLAG: Rs 32.5cr to Rs 34.5cr invested in two LLPs, Happy
Buildmart LLP and Harmony Buildstate LLP, each 90% owned by one promoter
director couple, with 10% held by the company's own wholly owned subsidiary.
No arm's length pricing statement. No stated business rationale. Internal
table versus narrative figure inconsistency.
Anchor: AR Note 8 (Investments), p.121. LLPs dated 26-Feb-2025.
Compounding item: AOC-2 (Annexure III, p.64) states RPT disclosure is "Not
applicable" while Note 41 (p.135-137) lists real, named, quantified RPTs
including sales and purchases with Fluidcon Engineers, rent to Manish Gupta
and Vikas Jain, consultancy to Mahendra Kumar Jain, staff training to Navya
Gupta, loans to VM Portfolio, personal guarantees and director remuneration.
```

### B07 EMERGING MOAT FLAGS

Emerging moat score 9 of 92 against a 12 point floor. Classification NONE. Combined with Gate 0 AVERAGE the combined assessment stays AVERAGE, not the GOOD or AVERAGE plus EXPANSION setup this pipeline hunts. Five flags, each anchored to the company's own annual report BRSR, which makes them self contradictions rather than analyst opinion.

```
⚠️ FLAG-EMOAT-RD-ZERO: R&D expense disclosed at 0.00% of total R&D plus capex
investment for FY2026 (0.00083% FY2025), AR p.96-97. Falsifies every R&D
driven or innovation driven moat claim in the concalls and the investor
presentation, including "strong focus on research and development" (Jun-2025
call).

⚠️ FLAG-EMOAT-EXPORTS-ZERO: exports disclosed at NIL percent of turnover, AR
p.87. Directly contradicts the China plus one and export beneficiary framing
in investor presentation slides 20 to 24.

⚠️ FLAG-EMOAT-DEALER-DECLINE: dealer and distributor count fell 93 to 82 and
dealer channel sales share fell 12.44% to 11.61% of total sales, FY25 to FY26,
AR p.96. Contradicts the "1000+ channel partners" distribution narrative
repeated in the presentation and on the Jun-2026 call, and the "diversified
demand reduces customer concentration risk" claim (slide 18).

⚠️ FLAG-EMOAT-CAPACITY-CUT-UNDISCLOSED: aluminium frame capacity at
Narmadapuram was stated as 54,000 metric tons on the Jun-2025 call and appears
as 18,000 MTA in every later call, the presentation and the AR. A 67 percent
cut never flagged as a revision anywhere in the corpus.

⚠️ FLAG-EMOAT-EXECUTION-CROSSREF: F2 execution moat and every forward capex
dependent category (B1, H2, R1) inherit the B05 Grade D promise delivery
record and should be read at a material discount to the company's own framing.
```

Verifier C recomputation, carried for the record: em_score 8 rather than 9 on the H1 matrix value, and capex_embedded_growth_pct 528 rather than 428 on the correct 2C denominator. Classification NONE is unchanged at either score. The reported evidence_mix of documented 11 / claim 24 / inference 3 cannot be reconstructed from the report body and must be treated as unsupported; the individual BRSR contradictions underneath it remain separately anchored.

---

## PHASE 1 CONFIDENCE DELTA

| Component | Verifier | Score | Basis |
|---|---|---|---|
| numerical_acceptance | B12a | 83 | 18 material claims checked. 0 CRITICAL, 2 MAJOR, 1 MINOR. No fabricated number, no anchor not found, no material unanchored figure |
| redflag_coverage | B12b | 42 | 59 independently found flags. 20 caught upstream, 9 partially caught, credited at half: (20 + 4.5) / 59 = 42%. 7 CRITICAL, 17 MAJOR, 5 MINOR missed |
| framework_adherence | B12c | 86 | **PARTIAL SCORE.** Gate 0 88.5% (46 of 52 rules) plus Emerging Moat 83.3% (35 of 42). 0 CRITICAL, 2 MAJOR, 11 MINOR |
| **valuation adherence** | B12c | **PENDING PHASE 3** | **Not scored. Verifier C rules 4, 7, 11 and 12 could not run: stages 10 and 11 do not execute in phase 1, so B10 and B11 do not exist. The 86 above is NOT a whole pipeline framework score** |
| business understanding narrative audit | B12c | NOT APPLICABLE IN PHASE 1 | Stage 13 had not run when B12c ran. Not a fail, not a REWORK trigger. Deferred with the valuation audit |
| peer_utilisation | B12d | 91 | 10 of 11 peer transcripts used substantively by stage 6. 0 CRITICAL, 2 MAJOR, 2 MINOR. No fabricated quotes |
| **overall** | minimum of the four | **42** | Band: below 60, forced REWORK |

The weakest component is redflag_coverage at 42, and it is the only one that fails. It sits 41 points below the next lowest. The failure is concentrated in two named areas and nowhere else: internal arithmetic within a single call, and peer verification of operating norms as opposed to peer prices and dates.

Caution on reading the 86: it covers Gate 0 and Emerging Moat only. Two of Verifier C's four valuation rules govern the Section 1B destination PE and the Hurdle, neither of which exists in this run. Do not carry 86 forward as the run's framework adherence once phase 3 runs.

---

## CONTRADICTED CLAIMS

These are priority monitoring items and the first verification targets for phase 3.

**Three INA claims contradicted by peer evidence (B06.contradicted).**

| # | INA claim | Contradicting peer evidence | Anchor |
|---|---|---|---|
| 1 | 142 GW of national ALMM cell capacity, the load bearing figure behind management's no overcapacity argument | Websol discloses 24 GW of ALMM cell capacity approved; the 145 GW figure applies to modules, not cells. Waaree relevant cell capacity about 30 GW, Premier actual 27 to 30 GW. Reads as a cell versus module conflation in INA's own claim, not a verified industry fact | Websol, 30-Jan-2026 call, p.19. Corroborated independently by B09, which sizes the implied Rs 170,400cr cell market claim against a conservative Rs 36,000cr estimate, ratio 4.73x, read inflated |
| 2 | ALCM / ALMM Part 2 effective date of January 2026 (INA's alternate stated date; it also gave 1 June 2026) | Waaree, Premier and Websol all confirm 1 June 2026 as the governing date at the time | Waaree, 30-Apr-2026 call, p.28; Premier, 29-Oct-2025 call, p.16. Superseding update: peer calls dated after INA's corpus closes push the date to December 2026 (Websol 11-Aug-2026, Premier Aug-2026), which is new negative information for the cell integration margin timeline that no INA stage could have caught |
| 3 | Receivables growth from the shift to letter of credit terms reflects a sector wide cash conversion problem | Websol used LC backed receivables in the same year and converted 84 percent of FY26 PAT to operating cash (Rs 255cr on Rs 303cr PAT) | Websol, 28-Apr-2026 call, p.4 and p.19-20. This is the decisive input to the FLAG-CASH determination above |

**Two B06 conclusions ruled OVERSTATED by Verifier B (B12b.pipeline_flags_overstated).** Both must be corrected in the stage 6 rerun and neither may carry into phase 3 as written.

| # | B06 conclusion | Why it is overstated | Anchor |
|---|---|---|---|
| 4 | B06 Q2: the realisation match "removes pricing as a plausible source of INA's margin or cash flow underperformance" | Its own anchor shows Waaree at Rs 15 to 16 per watt non DCR in the same quarter INA reported Rs 13 to 14 per watt. Verifier B derives Rs 150 to 250cr of gap on about 1 GW of non DCR volume, against FY26 EBITDA of Rs 305cr. Pricing is not removed | Waaree, May-2026 call, p.9 |
| 5 | B06 Q3: INA's cell ramp assumption sits "within this general 4-12 month ramp window" | The comparators used are brownfield debottlenecks and a line upgrade, not a greenfield line. Premier states new lines take 6 to 18 months to stabilise and two years to build and ramp. INA's own Chairman and CFO contradict each other on the ramp inside one call | Premier Jan-2026 p.15; Premier Aug-2026 p.18; Concall_Jun_2026 p.7 against p.9 |

Anchor caveat on all B06 rows: Verifier D logged two MAJOR citation location errors and two MINOR ones in B06, traced to citing the transcript's printed "Page X of Y" footer instead of the extraction "===== PAGE N =====" marker, offset by exactly one page by an unnumbered SEBI cover letter. The quotes are genuine and correctly attributed. The page pointers need re anchoring in the rerun.

---

## MONITORABLES

Merged and deduplicated from B03.monitorables (10 items) and B04.must_track_metrics (5 items), capped at 8 per the stage rules.

1. **Receivables aged beyond six months, as a share of the consolidated trade receivables book.** FY26 is 39.5 percent, Rs 111.35cr of Rs 281.59cr, up from 12.1 percent in FY25 and 5.7 percent at 1 April 2024. Below about 20 percent resolves the cash question toward a growth ramp; at or above 39.5 percent resolves it toward a structural revenue quality problem. Also watch whether it spreads from the subsidiary to the parent, whose book stayed near 6 percent. Find it in the trade receivables ageing note of the next annual report. This is the run's falsification metric.
2. **Consolidated operating cash flow and the CFO/PAT and CFO/EBITDA ratios.** FY26 is minus Rs 73.13cr against Rs 200.63cr PAT. Watch for a return to positive cash flow, or both ratios back above 0.7, or a stated management explanation if it stays negative. No narrative section in the FY26 annual report addresses the inversion at all. Find it in the quarterly results and the next Consolidated Statement of Cash Flows.
3. **Sale of Electricity, the IPP revenue line.** FY26 is Rs 4.22cr, 0.2 percent of consolidated revenue, against a 400 MW KUSUM target with about 38 to 40 MW commissioned by the Q4 FY26 call and Rs 1,000cr of KUSUM capex committed. Healthy is a run rate consistent with commissioned MW times load factor times tariff. Staying near Rs 4 to 5cr for multiple quarters past stated commissioning dates says the IPP narrative is not monetising. Find it in the revenue disaggregation note.
4. **Narmadapuram 4.5 GW cell facility commissioning date, against the stated Q4 FY27 target.** The corpus carries three inconsistent dates, Q3 FY27, Q4 FY27 and December 2026, two of them in the same call. This tests delivery credibility on the one forward category with real capital behind it, and it is the single variable the entire margin case rests on. Track it alongside the aluminium frame facility, guided Q1 FY27 on the call and September 2026 in the presentation. Find it in company announcements and the manufacturing facilities section of the next annual report.
5. **Group EBITDA margin.** FY26 is 14.0 percent, up from 6.3 percent in FY22. Healthy is continuing that rise. Flat or falling once the cell plant commissions kills the backward integration thesis, because integration is the only stated reason margin should move. Watch it against the peer benchmark: Waaree's margin fell about 590 basis points on silver, copper and freight in the same quarter INA held flat with no commodity commentary, while INA's own raw material cost rose about 190 percent.
6. **Corporate guarantee outstanding and IREDA facility drawdown.** FY26 guarantee is Rs 1,654.01cr, already 205 percent of net worth and 825 percent of PAT. Secured non current borrowings of Rs 468.89cr sit against a Rs 1,134cr sanction, so both leverage and the parent's contingent exposure rise mechanically as the facility draws before its first repayment in December 2027. Watch also the parent guarantee to parent assets ratio, healthy below 1x and already 3.0x. Find it in the contingent liabilities note and the borrowings note.
7. **Solarworld Energy Solutions Ltd, the receivable and its ageing.** Rs 265.19cr, 12.4 percent of FY26 revenue, NIL in FY25, never named by management or asked about by any analyst on any of the three calls. Watch for any ageing by customer breakdown or a change in this customer's revenue share. This tests the directors' own claim of "reduced customer concentration risk", which stage 3 found contradicted by this very disclosure. Find it in the customer concentration note, or ask directly.
8. **The FY27 auditor's Key Audit Matters.** ARS and Co. replaces Badaya and Co. on ordinary Section 139 rotation, and was appointed internal auditor in the same board meeting cycle it was proposed as statutory auditor. Zero KAM were reported for FY26, a year in which inventory grew 4.9 times, receivables 2.56 times and guarantees 16.6 times. Any KAM on revenue recognition, receivables or ECL, or the guarantee and related party structure, is the first independent test of whether the zero KAM pattern was auditor specific. Find it in the FY27 annual report auditor's report.

---

## PUBLISH CHECK

No publish candidate this analysis.
