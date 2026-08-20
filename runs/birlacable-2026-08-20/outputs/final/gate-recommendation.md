REWORK

# Gate recommendation, phase 1

Company: Birla Cable Ltd (BIRLACABLE). Run date: 2026-08-20. Scope: phase 1 evidence only. Valuation runs in phase 3, so this file carries no decision, no entry zone and no exit multiple.

## What this verdict judges

REWORK judges this run's analysis. It does not judge the company. The evidence stages produced a usable record on the balance sheet, the merger and the promoter. Two evidence stages did not audit what they were given, and the red flag verifier found the gap large enough that the run cannot be closed on their output.

Two binding inputs force the verdict under selection rule 1:

- Overall confidence is 15.4, below the 60 floor.
- Verifier B's acceptance rate is 15%, below the 60% floor.

Either one alone forces REWORK. Company quality does not enter this test.

## Rework scope

Verifier B named the scope. A rerun must fix exactly this.

| Stage | Sections to redo | Against what |
|---|---|---|
| B05-concall | 2C, 2D, 4D | The FY26 audited cash flow statement and balance sheet, plus the annual report's internal consistency across Directors' Report, MD&A and notes |
| B06-peers | Claim 2, Claim 3, Claim 4 verdicts | The 12 supplied peer transcripts, read for statements that complicate BCL's claims, not only for statements that confirm them |
| B06-peers | Part 2B and Part 2C cross reads | Input cost commentary (fibre, preform, germanium, helium, polymer) and the STL capacity claims |

Verifier B's root cause, stated in its own words: in no concall mode the pipeline treated four company documents as a communication record and mined them for statements, but never audited the audited numbers behind those statements. Four of the five red flags stage 5 produced are the rating agency's own risk list restated.

## FLAG-CASH: ACTIVE

**Determination: INDETERMINATE.**

Cited evidence:

- FY26 operating cash flow minus Rs 20.91 Cr against PAT of Rs 16.87 Cr, after plus Rs 112.40 Cr in FY25 (B02 finding 2, Cash Flow Statement p.76; B03 correction to the FY25 comparative, p.76 standalone / p.122 consolidated).
- DSCR 0.39x FY26 and 0.40x FY25, both below 1.0x, disclosed by the company itself (B02 finding 2, Note 49(f) p.110-111).
- Working capital consumed Rs 62.22 Cr in FY26, funded by Rs 58.39 Cr of fresh short term borrowing (B12b critical 1, FY26R p.5; AR p.27).
- Receivables absorbed Rs 32.6 Cr and inventory Rs 27.8 Cr; receivable days 92.2 to 96.1; working capital days 104.2 to 118.9 (B03 flag; B01 block_b_trend).
- Free cash flow swung from plus Rs 84.66 Cr in FY25 to minus Rs 23.42 Cr in FY26 (B01 block_b_trend).
- 62.3% of Rs 131.32 Cr borrowings sit in the payable on demand bucket, up from 21.5% (B02 finding 6, Note 46(c) p.109-110).
- Capex of Rs 1.91 Cr is 12% of depreciation of Rs 15.79 Cr; PPE fell 14.3%; CWIP nil; two annual report sections call this capacity expansion (B12b critical 2, AR p.27; AR p.46 MD&A (f); FY26R p.4).
- Rs 24.79 Cr overseas export receivable aged 2 to 3 years and more, no named counterparty, carried on management representation (B02 finding 4, Note 9(2) p.89).
- Impairment loss on financial assets FY25 Rs 0.50 Cr, FY26 Rs 1.72 Cr, Q1 FY27 Rs 1.00 Cr in one quarter against nil a year earlier (B12b major, Q3R p.2; FY26R p.3; Q1R p.2).

Rating agency verbatim, CARE Ratings press release dated 2026-04-01, p.6:

> "BCL's operations remain working capital intensive, as reflected in its operating cycle of 125 days in FY25, despite improving from 134 days in FY24."

Why INDETERMINATE and not STRUCTURAL or GROWTH-INDUCED. FY25 operating cash flow was strongly positive at plus Rs 112.40 Cr, so a two year window does not establish a structural failure. Growth induced does not fit either: capex was 12% of depreciation, CWIP was nil and the asset base shrank 14%, so no capacity build absorbed the cash. The stale Rs 24.79 Cr receivable rolls forward at a flat rupee amount rather than clearing, which points at collection, not at growth. The record does not settle it.

Missing evidence, named:

1. Receivables ageing split by customer, specifically whether the 45.0% customer drives the Rs 32.6 Cr receivable increase. The annual report gives buckets only (B02, Note 9 p.88-89).
2. Identity of, and independent recoverability evidence for, the Rs 24.79 Cr overseas receivable beyond management representation (B02 finding 4).
3. Any explanation for raw material inventory rising 87.8% against revenue growth of 16.5%. No narrative exists in the annual report (B02 finding 11, Note 8 p.88).
4. FY23 and FY24 capex, trade payables and current liabilities, so cash conversion can be tested over four years instead of two (B01 input_gaps and data_notes).
5. A published cash flow statement between annual reports. The Q1 FY27 filing carries none (B05 quarters_analysed).
6. Management explanation of the FY26 swing. No earnings calls exist for this company (B00 no_concall_mode true).

Binding consequence: any future PROCEED on this ticker caps at PROCEED WITH CAVEATS until the cash determination resolves. That cap stands whatever the valuation produces in phase 3.

## FLAG-GATE0: ACTIVE

Core score 39 out of 100 as published. Core score 27 under Verifier C's strict recomputation. Classification AVOID in both variants. Moat score 0 out of 60, moats confirmed 0 of 12, grand total 39 out of 160 (B01; B12c recomputed_gate0_core_score).

Block scores as published: A 5, B 13, C 0, D 11, E 10 (B01 blocks).

Depressor causes:

- Revenue CAGR minus 0.89% and PAT CAGR minus 19.94% across FY23 to FY26 (B01 flag).
- Revenue declined in two of the three year on year steps, FY24 and FY25 (B01 deal_breakers).
- Median ROCE 7.55% on the FY25-FY26 formula accurate subset, which trips the sub 10% deal breaker (B01 deal_breakers).
- Block A scored 5, below the 8 threshold, on sub 12% median ROCE and ROE (B01 deal_breakers).
- Zero of 12 moat tests scored 3 or above, so moat_score is 0 (B01 moat_score).
- Block C scored 0.

Verifier C's three MAJOR recomputations that take 39 to 27: A4 ROCE trend scored 5 on a one year window whose earliest endpoint is N/A, recomputed to 0; B2 FCF positive proportion used a 2 year denominator instead of the 4 year history, recomputed to 0; B3 cumulative FCF over cumulative PAT used the FY25-FY26 subset while B1 used four years, recomputed to 0 (B12c fails G-10, G-14, G-15).

Note the framework verifier's own caveat: the classification is AVOID in every variant tested, so the recomputation changes the score, not the outcome.

## Promoter findings

Verifier is CAUTION, not DEAL BREAKER, so no formal FLAG-PROMOTER block is mandatory. Scorecard: 6 clean, 3 caution, 1 red. Deal breakers: none (B08).

Top findings:

1. The 22 year Priyamvada Devi Birla estate and succession dispute is still live, with Supreme Court appeals pending against the ruling that lets Harsh V. Lodha continue as MP Birla Group chairman (B08, AR p.46; court record 12 March 2026).
2. The BCL into VTL amalgamation at 10:115 is a related party transaction with promoter entities on both sides, VTL at 19.33% and Universal Cables at 13.00%. No independent proxy adviser covered it. BCL shares fell 25% to 39% over the six to twelve months around the announcement (B08, AR p.11-12, p.26).
3. CEO R. Sridharan resigned on 19 January 2026 after about 21 years with no reason disclosed anywhere in the annual report. Internal CFO Somesh Laddha was promoted into a combined Manager and CFO role four months later on 22 May 2026 (B08, AR Directors' Report p.26).
4. Director Dhan Raj Bansal, aged 87, attended 1 of 5 board meetings in FY26 and is proposed for re appointment by special resolution (B08, AR p.46; Notice Item 4 p.15).
5. VTL guarantees BCL's secured borrowings with no fee disclosed. VTL has separately pledged 12.5 lakh BCL shares, 4.17% of BCL equity, with SBI for its own working capital, unchanged in FY26 (B08, AR Notes 17(i), 21(ii) p.93-94; Regulation 31(4) disclosure).

**transition_evidence: NONE FOUND.** The promoter stage recorded an empty list. No evidence of improving promoter conduct was found in any source this run.

Carry forward: after the merger, BCL holders become VTL holders, so VTL's own promoter quality becomes the live question. No VTL promoter check was run here.

## Confidence delta, phase 1

| Component | Score | Basis |
|---|---|---|
| Numerical acceptance | 100 | B12a: 73 claims checked, 0 findings, 0 anchor failures |
| Red flag coverage | 15.4 | B12b strict: 4 of 26 verifier found flags caught upstream. Half credit variant 21.2 |
| Framework adherence | 90 | B12c phase 1 only: 78 of 87 rules passed, Gate 0 92% and Emerging Moat 86%. Valuation audit pending phase 3 |
| Peer utilisation | 100 | B12d: 12 of 12 supplied peer quarters used substantively |
| **Overall** | **15.4** | Minimum of the four |

Weakest component: red flag coverage at 15.4. Verifier B found 26 independent red flags across the company documents and the 12 peer transcripts. The evidence stages caught 4 and partially caught 3. Five of the misses are CRITICAL, and two of those sit on the audited cash flow statement and the capex line, which the evidence stages never opened.

## Contradicted and corrected claims

These are the peer stage verdicts as corrected by Verifier B and Verifier D. Each is a priority monitoring item.

| Claim as filed | Corrected position | Anchor |
|---|---|---|
| Claim 3, structured copper LAN surge as FY26 growth engine, filed CONTRADICTED and called the single most consequential contradiction | OVERSTATED. STL's decline is data centre and enterprise copper on LME cost, a different product and end market. HFCL is silent. Paramount lists LAN as a catalogue item only. CARE independently corroborates BCL's copper volume growth of about 12% at about 94% utilisation, and VTL's FY25 cable segment up 33% on copper demand. Correct verdict UNVERIFIABLE or PARTIALLY CONTRADICTED | B12b pipeline_flags_overstated; STL May-2026 p.9; CARE p.4, p.5 |
| Claim 4, global OFC pricing at record levels, filed VERIFIED on two independent peers | OVERSTATED. Only HFCL corroborates the price leg. STL says pricing is stable with no uptick (Jan 2026) and refuses to comment on realisation (Jul 2026). Correct verdict PARTIALLY VERIFIED | B12b; STL Jan-2026 p.13; STL Jul-2026 p.13 |
| Claim 4 evidence base | Omits that a 50 to 100 million fkm slice of the demand behind the price spike is military drone driven, which HFCL refuses to supply and its preform suppliers discourage | B12b major; HFCL May-2026 p.12 |
| Claim 1 and Claim 4, BCL's forward pricing view | Directly contradicted by HFCL's MD on 30 April 2026: prices "have reached to their almost the final level... there will not be any further increase in the prices". BCL's board signed the opposite claim on 22 May 2026 | B12b critical 3; HFCL May-2026 p.12; AR p.45 |
| Claim 2, filed unverifiable on the ground that no peer addresses government fund disbursement pace | NOT SUPPORTED. HFCL answered it directly on UP Jal Nigam: non payment by state authorities because they are not receiving central funds, and execution has slowed. Same programme family that drove guarantor VTL's downgrade | B12b critical 5; HFCL Oct-2025 p.17; CARE p.1 |
| Claim 2 net read, BharatNet EPC warranty period loss carried forward as a template risk for BCL | NOT SUPPORTED. HFCL attributes the warranty period loss to the Army NFS network and names BharatNet as the profitable new EPC work. The peer stage inverted this and carried the inverted risk into its recommendation | B12b pipeline_flags_not_supported; B12d major 2; HFCL May-2026 p.11; HFCL Feb-2026 p.14 |
| Part 2C capex cycle, STL as part of an industry wide capacity race | OVERSTATED. STL said it does not intend to add significant capacity (Nov 2025), the QIP resolution was enabling only, 75% of the raise goes to debt reduction, capex is INR 500 cr a year for upgrades and debottlenecking, and the $100m US facility "doesn't really translate into a capacity per se" | B12b pipeline_flags_overstated; STL Nov-2025 p.15; STL Jul-2026 p.8, p.14, p.17 |
| Claim 1, HFCL Q1 FY27 evidence bullet | ATTRIBUTION ERROR. The INR 13,100 crore Q1 intake, the 1.7x framing and the $1.1bn hyperscaler deal belong to STL, not HFCL. HFCL's own Q1 FY27 disclosure is an order book of about INR 26,665 crore. HFCL does separately hold a $1.1bn contract from Q4 FY26 | B12b; B12d major 1; STL Jul-2026 p.5 vs HFCL Jul-2026 p.3 |
| Claim 1 and Claim 4, two quoted management statements | ATTRIBUTION ERROR. Both are analyst words quoted as management answers. The higher realisation versus domestic market line is the analyst's question. The 15% to 20% figure is the analyst's proposition, answered only with "More than that" after three refusals | B12b; HFCL Jul-2026 p.8-9; HFCL May-2026 p.24 |
| Stage 5 red flag 1, customer concentration "undisclosed by BCL itself" | NOT SUPPORTED as written. AR MD&A Risks and Concerns lists "highly concentrated customers base". The substance survives, because BCL never quantifies it and the 94% and 47% figures come only from CARE, but the assertion stage 5 called its sharpest finding is factually wrong | B12b pipeline_flags_not_supported; AR p.48 |

Two claims survive correction intact: fibre demand and pricing revival strengthening into FY27, verified on HFCL and STL, and the timing caveat that HFCL's revival narrative starts about five months before BCL's claimed late March 2026 inflection, which makes BCL a lagging beneficiary (B06 verified; B12b promise_delivery_spot_checks, confirmed against HFCL Oct-2025 p.2-3).

## Monitorables

Eight items, deduplicated across the annual report, business model and communication stages.

1. NCLT hearing dates and any scheme order. Watch exchange filings and the NCLT cause list for a sanction, a rejection, a modification of the 10 VTL per 115 BCL ratio, or a minority shareholder challenge. CARE puts completion at roughly January to March 2027. This tests whether a standalone Birla Cable thesis exists at all, because sanction dissolves the company.

2. Operating cash flow in the next published cash flow statement, half yearly or the FY27 annual report. Watch for positive OCF and CFO over PAT above 0.7 times. FY26 was minus Rs 20.91 Cr on PAT of Rs 16.87 Cr. This is the single test that decides whether the earnings recovery is cash real, and it is what resolves the INDETERMINATE cash flag.

3. Segment split of FY27 revenue, in the annual report or any quarterly filing that publishes one. Watch for optical fibre revenue actually growing rather than aggregate revenue growing. Fibre fell 8.3% in FY26 while total revenue rose 16.5%. This tests whether the fibre revival management claimed is real at company level or whether copper is still carrying everything.

4. Single customer share of revenue, in the annual report customer concentration note and any quarterly disclosure. It was 45.0% of FY26 revenue, up from 39.6%. Watch for a move above 45%, or any sign the customer has reduced offtake. Loss of this relationship is near immediate in results.

5. Impairment loss on financial assets in each quarterly result. Q1 FY27 booked Rs 1.00 Cr in one quarter against nil in Q1 FY26; FY26 total was Rs 1.72 Cr against Rs 0.50 Cr in FY25. Rising impairment in a business with 45% concentration tests receivable quality directly, and the company has never explained the line.

6. CARE rating actions resolving the Rating Watch Developing status, and the guarantor's own metrics. BCL's unsupported standalone rating is BBB+ / A2 and the A(CE) rating rests on VTL, which showed 1.37x interest coverage for 9M FY26 with TD over PBILDT expected above 6 times. Watch CARE press releases. BCL holders convert into this credit at 10:115.

7. Current borrowings against revenue growth, plus the payable on demand share of debt. FY26 borrowings rose 35.6% against revenue growth of 16.5%, and 62.3% of Rs 131.32 Cr is payable on demand. Watch the balance sheet in the next half yearly and annual filing. This tests whether working capital is being funded by lender forbearance.

8. Raw material cost as a share of revenue, in the quarterly profit and loss. FY26 baseline is 82.3%; Q1 FY27 fell to 74.3%. Watch whether that holds, given peers report bare fibre up from Rs 250 to over Rs 300 per km, preform costs up 20 to 25%, and germanium supply controlled from China. BCL makes no fibre and buys it from group entity Birla Furukawa, which no company document names.

## Falsification

The single next quarter print that does most damage: a Q2 FY27 result that shows revenue growth holding while the impairment loss on financial assets rises again and no cash flow statement accompanies it. That combination says the FY26 to FY27 revenue recovery is being bought with receivables from one concentrated buyer, which is the exact failure the FY26 cash flow already showed once and which nothing in the record has yet ruled out.

## Publish check

No publish candidate this analysis.
