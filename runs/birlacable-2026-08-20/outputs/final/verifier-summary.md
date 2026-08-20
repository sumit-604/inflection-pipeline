# Verifier summary, phase 1

Company: Birla Cable Ltd (BIRLACABLE). Run date: 2026-08-20. Scope: phase 1. Verifier C's valuation audit is deferred to phase 3 and is not in this file.

## Confidence delta

| Component | Score | Basis |
|---|---|---|
| Numerical acceptance | 100 | B12a: 73 claims checked, 0 findings |
| Red flag coverage | 15.4 | B12b strict: 4 of 26 caught upstream. Half credit variant 21.2 |
| Framework adherence | 90 | B12c phase 1: 78 of 87 rules passed. Valuation pending phase 3 |
| Peer utilisation | 100 | B12d: 12 of 12 peer quarters used substantively |
| **Overall** | **15.4** | Minimum of the four |

## Acceptance rates

| Verifier | Model | Acceptance rate | CRITICAL | MAJOR | MINOR | Rework trigger |
|---|---|---|---|---|---|---|
| A, numerical | claude-haiku-4-5 | 100 | 0 | 0 | 0 | no |
| B, red flags | claude-opus-4-8 | 15 | 5 | 17 | 8 | **yes** |
| C, framework (Gate 0 + Emerging Moat only) | claude-opus-4-8 | 90 | 0 | 4 | 5 | no |
| D, peers | claude-sonnet-5 | 83 | 0 | 2 | 2 | no |

## Verifier A, numerical

73 numbers checked. Zero findings.

| Severity | Location | Note |
|---|---|---|
| — | — | No findings. All major financial statement line items verified across balance sheet, profit and loss, cash flow and notes. Seventy three distinct numerical claims checked across all nine stage reports. Screener data matched to AR FY26 figures. Customer concentration, inventory growth, payables growth and other derived calculations spot checked for arithmetic correctness. Peer concall and web sourced figures marked out of scope per instruction. Zero mismatches, zero anchor not found, zero material unanchored claims. |

No source fidelity finding was raised, so the source fidelity gate did not trigger.

## Verifier B, red flags

26 independent red flags found. 4 caught upstream, 3 partially caught. Acceptance rate 15%. Rework scope: B05-concall and B06-peers.

### CRITICAL

| # | Location | Note |
|---|---|---|
| 1 | B05 report, Sections 2C/2D/4C and B05-concall.yaml red_flags | FY26 operating cash flow of MINUS Rs 2,090.52 lakh (vs +Rs 11,240.13 lakh FY25) never surfaced, while the Directors' Report claims "effective cash flow and working capital management". Per the run's own standing rule, cash conversion this weak cannot resolve silently. |
| 2 | B05 report, Section 1/2/4C | FY26 capex of Rs 191.05 lakh is 12% of depreciation on a PPE base that fell 14.3% with nil CWIP, yet is described twice as capacity expansion. Capex appears nowhere in B05. Peers spend 30x to 300x more. |
| 3 | B06 report, Part 1 Claim 1 and Claim 4 verdicts | HFCL's MD stated on 30 Apr 2026 that OFC prices had "reached to their almost the final level". BCL's board signed the opposite framing on 22 May 2026. The peer statement that most directly complicates BCL's central forward claim is absent from both VERIFIED verdicts. |
| 4 | B06 report, Part 2B industry_cross_read.pricing_inputs | The germanium, helium, preform and polymer input squeeze is missed entirely; only LME copper is named. For a non integrated converter that buys fibre from a group JV, this inverts the sign of the "tailwind" the pipeline verified. |
| 5 | B06 report, Part 1 Claim 2 "Peers silent" and unverifiable[] block | B06 states no peer addresses government fund disbursement pace. HFCL answered it directly on the UP Jal Nigam programme in the Oct 2025 call that B06 marked SUBSTANTIVE. This is the exact injected question and the exact programme family behind guarantor VTL's downgrade. |

### MAJOR

| # | Location | Note |
|---|---|---|
| 6 | B05 report, Section 2C Transparency rating = 4 | The AR ratio table, cited as evidence of transparency, presents six profitability/return ratios and omits every working capital ratio in the year receivables rose 21.4% and inventories 54.3%. |
| 7 | B05 report, Section 2C Consistency rating = 4 | Directors' Report says OFC order flow was "broadly in line with the previous year"; MD&A in the same document reports an 8.3% decline and "a deep global dearth". Consistency was rated only on amalgamation wording. |
| 8 | B05 report, general | Two unexplained internal numeric inconsistencies in the AR: MD&A PAT of Rs 1,678.78 lakh matching neither audited figure, and FY25 finance cost given on two different bases in two sections with no note. |
| 9 | B05 report, Section 2D and 4D | Impairment loss on financial assets rose 3.5x in FY26 and hit Rs 100.00 lakh in Q1 FY27 alone against nil a year earlier, unexplained, in a 47% single customer business. Not surfaced. |
| 10 | B05 report, Section 2D "What they are not saying" | The four item list omits that BCL sources optical fibre from group entity Birla Furukawa while declaring no material related party transactions and AOC-2 not applicable. |
| 11 | B05 report, Section 2D and 3B | A Rs 5,259.40 lakh quoted investment book, 18.7% of net worth, drives OCI swings larger than PAT (Q4 FY26 total comprehensive income was negative despite positive PAT). The AR ratio table headlines its return but the narrative never discusses it. |
| 12 | B05 report, Section 2D; B06 Part 2E | BCL's record contains no US tariff commentary at all despite about 74% OFC export share, while all three peers quantified FY26 tariff damage. B06 names the risk via Paramount only; B05 does not list it. |
| 13 | B05 report, Section 4D red flag 4; B05 yaml red_flags | The rating flag stops at the CE downgrade. It omits that BCL's unsupported standalone rating is CARE BBB+/A2 and that guarantor VTL is heading above 6x TD/PBILDT with 1.37x 9MFY26 interest coverage, which is the forward exposure BCL holders convert into at 10:115. |
| 14 | B06 report, Part 1 Claim 4 verdict "VERIFIED" | Only HFCL corroborates the price leg. STL states pricing is "stable... no uptick" and refuses to comment on realisation. Verdict should be PARTIALLY VERIFIED. |
| 15 | B06 report, Part 1 Claim 4 evidence | The record pricing verdict omits that a 50 to 100 million fkm slice of demand is military drone driven at "any price", which HFCL refuses to supply and its preform suppliers discourage. |
| 16 | B06 report, Part 1 Claim 1 and Claim 4 evidence | HFCL stopped disclosing blended OFC realisation in Q4 FY26 after two quarters of giving it, refusing three analysts in one call. The pipeline's realisation anchor was withdrawn by its source and this is not noted. |
| 17 | B06 report, Part 1 Claim 2 net read and analyst_note | NOT SUPPORTED. HFCL attributes the warranty period EPC loss to the Army NFS network and names BharatNet as the profitable new work. B06 inverted this and carried the inverted risk into its synthesis recommendation. |
| 18 | B05 report, Section 2D bullet 2 and red flag 1 | NOT SUPPORTED as written. The AR MD&A Risks and Concerns explicitly lists "highly concentrated customers base". The flag's substance survives; the "silent everywhere" assertion, called B05's sharpest finding, does not. |
| 19 | B06 report, Part 1 Claim 3 verdict "CONTRADICTED" and Part 4 | OVERSTATED. STL's decline is data centre/enterprise copper on LME cost, a different product and end market; no peer sells BCL's product at scale; and CARE independently corroborates BCL's copper volume story and VTL's +33% FY25 cable growth on copper. B06 never uses that evidence. |
| 20 | B06 report, Part 2C capex_cycle and yaml industry_cross_read.capex_cycle | OVERSTATED on STL. STL disclaimed significant capacity addition (Nov 2025), the QIP resolution was enabling, 75% of the raise goes to debt reduction, capex is INR 500cr/yr for debottlenecking, and the $100m US facility is connectivity that "doesn't translate into a capacity per se". |
| 21 | B06 report, Part 1 Claim 1 HFCL Q1 FY27 evidence bullet | STL's INR 13,100 crore Q1 intake, its 1.7x framing and its $1.1bn hyperscaler deal are attributed to HFCL. HFCL's own Q1 FY27 disclosure is a ~INR 26,665 crore order book. HFCL does hold a separate $1.1bn contract from Q4 FY26, so the coverage map line stands; the Claim 1 bullet does not. |
| 22 | B06 report, Part 1 Claim 1 and Claim 4 evidence | Analyst statements quoted as management statements twice, both inside VERIFIED verdicts: the "higher realization vs domestic market" line is the analyst's question, and the "15% to 20%" figure is the analyst's proposition to which Nahata replied only "More than that". |

### MINOR

| # | Location | Note |
|---|---|---|
| 23 | B05 report, Section 2A and 2C | The Rs 223.54 lakh Labour Codes gratuity charge, with an explicit warning that estimates may be revised when State rules are notified, is disclosed only in results notes and never in the AR narrative. Both peers quantified the same event. |
| 24 | B05 report, Section 2A row 1 and 4A trigger 1 | The AR dates the revival to late March 2026 although BCL's own Q3 FY26 filing already showed +29.6% revenue, and CARE p.5 attributes the Q3 FY26 improvement partly to "a marginal recovery in high-margin OFC sales", partial evidence for the mechanism B05 called unconfirmable. |
| 25 | B05 report, Section 4C Governance continuity | Managerial remuneration context omitted: Rs 222.98 lakh gross for a part year, 57.17x median, 280 employees, standalone PAT Rs 1,686.78 lakh. |
| 26 | B05 report, Section 2C Transparency | The Directors' Report refers to "the observation of Secretarial Auditor" while the Secretarial Audit Report contains no observation and reports unqualified compliance. |
| 27 | B05 report, Section 2A row 3 (dividend) | B05 places the payment window at "approx. early Sep 2026". The AGM Notice commits to payment "on or before August 31, 2026", a firmer and earlier date the pipeline did not use. |
| 28 | B06 report, Part 3 coverage map, HFCL Q4 FY26 row | HFCL's unbilled revenue rose INR 300cr to INR 600cr while EPC revenue fell, alongside a 50.7% sequential Q4 revenue jump. The pipeline uses these Q4/FY26 figures as magnitude corroboration without noting the analyst's unresolved question. |
| 29 | B06 report, Part 3 coverage map, all four STLTECH rows | All four STL calls are marked SUBSTANTIVE with no reliability caveat, although STL declines to disclose capacity, utilisation, volumes, preform sourcing, realisation and segment splits across every quarter. |
| 30 | B06 report, Part 4 and Part 5 | Omits that STL's ex China share slipped to 7% mid cycle and that its FY26 revenue is still below its March 2020 peak, context that qualifies the "durable, high visibility" framing. |

### Verifier B, credibility grade concurrence

Would grade lower: C+, not B. The single delivery cycle is real, but four disclosure defects sit inside the same document set and none was examined: negative FY26 operating cash flow presented under a claim of effective cash flow management; the Directors' Report contradicting the MD&A on the OFC year; a PAT figure in the MD&A matching neither audited number; and Rs 1.91 crore of capex (12% of depreciation, shrinking asset base) described twice as capacity expansion.

### Verifier B, promise delivery spot checks

5 checked, 4 confirmed, 1 wrong. The wrong one: B06 Claim 2, HFCL BharatNet EPC loss to AMC direction. Both calls attribute the warranty period loss to the Army NFS network; the later call names BharatNet as the profitable work. The direction of the promise does not hold.

## Verifier C, framework adherence (Gate 0 and Emerging Moat only)

Gate 0: 46 of 50 rules passed, 92%. Emerging Moat: 32 of 37 rules passed, 86%. Total 78 of 87, acceptance rate 90%. Valuation audit deferred to phase 3 and excluded from this rate. Rework trigger: no.

No conflation check: PASS. B07 states explicitly it is the Emerging Competitive Advantages scan and not FTTCP; no FTTCP content appears.

### MAJOR

| ID | Location | Issue | Recomputed |
|---|---|---|---|
| G-10 | B01 Block A, A4 | 1 year ROCE trend window scored 5 where the earliest endpoint is N/A; rule 5 scores it 0 and rule 6 sets a 3 year floor | A4 = 0 |
| G-14 | B01 Block B, B2 | FCF positive proportion computed on a 2 year denominator, not the 4 year history | 1 of 4 = 25%, B2 = 0 |
| G-15 | B01 Block B, B3 | Cumulative FCF over cumulative PAT computed on the FY25-FY26 subset while B1 used the full 4 years; excludes the two weak CFO years | B3 = 0; core 39 to 27, classification AVOID unchanged |
| E-17 | B07 Section 5, H2 | Likelihood x impact matrix: H2 scored HH=4 for an amalgamation in which BCL is dissolved; category fit is a stretch and the High impact leg rests on Scheme synergy language the report itself labels aspirational in 6B, while a documented 1.0x multiplier is applied | em_score 10.0 to 9.0 (HM) or 6.0 (out of category); classification NONE unchanged in both |

### MINOR

| ID | Location | Issue |
|---|---|---|
| G-05 | B01 formula note | Report computes ROCE and labels it computed, but never states whether the screener source carried a ROCE row that was checked first |
| E-12 | B07 Section 3 tables | Required "time to materialise" column absent from all family tables; present only for H2 in the block |
| E-22 | B07 optionality register | Three optionality register rows are the same merger synergies that supply H2's scored impact leg; registered options are watched, never scored |
| E-30 | B07 catalysts_12m item 3 | Catalyst 3 typed documented on third party industry data, inconsistent with the report's own exclusions at 1A and E2; stage 11 must not read it as a company specific documented catalyst |
| E-31 | B07 evidence_mix | Reports scored category counts (6/0/0) rather than item counts; claim and inference items appear in 1A, 1C, C1 and 6B but are recorded as zero |

Recomputed headline figures: Gate 0 core score 39 as published, 27 under strict rule 5 recomputation, classification AVOID unchanged. Emerging Moat score 10.0 as published, 9.0 or 6.0 under the H2 recomputation, classification NONE unchanged.

## Verifier D, peer handling

12 peers audited, 12 confirmed substantive, 0 unsupported, 0 unused but relevant. All claims addressed. No verdict discipline fails. Acceptance rate 83%, peer utilisation 100%.

### MAJOR

| # | Location | Note |
|---|---|---|
| 1 | 06-peers.md Part 1 Claim 1, HFCL Q1 FY27 evidence bullet + B06-peers.yaml peer_coverage_map HFCL Q1 FY27 | Quote "Q1 order intake INR13,100 crore, 1.7x the whole of the prior fiscal year's booking" is attributed to HFCL's Jul 2026 call but does not appear in that transcript; it is verbatim from STL Technologies' Jul 2026 transcript, anchored by a landmark multiyear $1.1 billion deal. Cross company data contamination inside a SUBSTANTIVE citation. |
| 2 | 06-peers.md Part 1 Claim 2 + Part 2E risks_peers_raise + analyst_note | The HFCL Q4 FY26 "warranty period" EPC loss to AMC profit mechanic is attributed to BharatNet, but the transcript states the loss was "majorly due to this Army's network" (NFS), a different government contract; the BharatNet EPC line quoted immediately after is described as already profitable. B06's Part 2E risk item and analyst_note both carry this mislabeled mechanic forward as a template risk for BCL's own BharatNet exposure. |

### MINOR

| # | Location | Note |
|---|---|---|
| 3 | 06-peers.md Part 1 Claim 2, HFCL Q2 FY26 Punjab/BSNL quote | Cited as p.18; quote sits under the transcript's own "Page 17 of 21" header. Quote text itself is accurate. |
| 4 | 06-peers.md Part 1 Claim 3, STL Q2 FY26 copper to fiber quote | Cited as p.13-14; quote sits under the transcript's own "Page 15 of 18" header. Quote text itself is accurate. |

## Verifier disagreement

None this run. Verifier A raised no source fidelity finding, so no downstream step conflicted with one.
