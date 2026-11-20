# Verifier summary: TD Power Systems Ltd (TDPOWERSYS), Phase 1, run 2026-11-15

## Phase 1 confidence delta

| Component | Score | Verifier block | Basis |
|---|---|---|---|
| Numerical acceptance | 98.6 | B12a (Verifier A) | (582 checked - 8 findings) / 582; mandatory tier 277 of 277 |
| Red-flag coverage | 78 | B12b (Verifier B) | 7 of 9 material verifier-found flags caught in full; 2 partially caught; 0 missed |
| Framework adherence (phase 1) | 90.4 | B12c (Verifier C, phase 1 partial) | 75 of 83 Gate 0 and Emerging Moat rules passed |
| Framework adherence (valuation) | PENDING PHASE 3 | B12c | valuation half (B10, B11) not run |
| Peer utilisation | 100 | B12d (Verifier D) | 12 of 12 peer transcripts used substantively |
| Overall | 78 | confidence.yaml | set by redflag_coverage; band 75-89, normal, note specifics |

REWORK triggers: Verifier A confirmed CRITICAL: false. Any acceptance rate below 60 on a denominator of 4 or more: false. Remediation cycles: 0. Verifier runs: A 1, B 1, C 1, D 1.

## Acceptance rates and coverage

| Verifier | Acceptance rate | CRITICAL | MAJOR | MINOR | Coverage as the verifier stated it |
|---|---|---|---|---|---|
| A (numerical) | 98.6 | 0 | 1 | 7 | 582 numbers checked; mandatory 277 of 277 (whole Gate 0 scorecard; no verdict card or Section 1B pillar input exists yet); sample tier about 305 of about 680 material numbers in 02-09 (roughly 45%), highest materiality first; 5 false positives struck by the verifier itself; 7 findings carry source_fidelity: true |
| B (red flags) | 78 | 0 | 2 | 8 | 25 independent flags found: 18 caught, 6 partially caught, 1 missed; 9 material (1 CRITICAL, 8 MAJOR): 7 caught, 2 partially caught, 0 missed; 78% counts CAUGHT only (100% if PARTIALLY CAUGHT counts); TDPS 3 of 3 transcripts read in full, peers 3 of 12 in full and 9 by topic search; promise-delivery spot checks 5, confirmed 4, wrong 1; credibility grade B: concur |
| C (framework, phase 1) | 90.4 | 0 | 1 | 7 | Gate 0: 55 rules checked, 51 passed; Emerging Moat: 28 rules checked, 24 passed, 1 not verifiable; valuation: PENDING PHASE 3 |
| D (peers) | 100 | 0 | 0 | 2 | 12 peers audited, 12 substantive confirmed, 0 unsupported, all claims addressed, no verdict discipline fails |

Verifier C, valuation half: pending phase 3. Expectation ledger: pending phase 3. Business narrative rule 9 check of this synthesis: pending.

## Findings, sorted by severity

### CRITICAL

None. No verifier logged a CRITICAL finding.

### MAJOR

| Verifier | ID | Location anchor | Finding | Source truth or fix, as the verifier wrote it |
|---|---|---|---|---|
| A | A-1 (source_fidelity: true) | 04-bizmodel.md s1B row 5 and s2B Alstom row; 05-concall.md s3D Customers bullet | Alstom long-term agreement dated 2020 (Pres. slide 5) | Pres. slide 5 prints the Alstom agreement under 2017; 2020 is "Increases footprint in the European and Turkish Market" (PDF page 5 rendered). Wrong year on a non-pillar fact; 07-emoat.md has 2017 correctly |
| B | F1 | B06 Q9; AR FY26 p.82 BRSR; Q4C p.8 NK; Q3C p.3 NK | B06 Q9 CONTRADICTED (no order disruption from US tariff) is OVERSTATED: its weighting premise that TD sells capital equipment to the end buyer is wrong; TD sells to prime-mover OEMs (the Azad position, no disruption), and TD Q3 FY26 inflow was a record Rs 6.56 bn, +61% YoY, 84% export | Reclassify for TD to PARTIALLY VERIFIED (customer-pays corroborated, disruption not shown at TD); keep peer deferral as context; add Q1C p.11 analyst note that FY26 exports were routed via Turkey because of tariff uncertainty |
| B | F2 | Q4C p.7; Q1C p.8, p.9 NK; TRITURBINE Q1 FY27 p.7; B05 3B | Material item partially caught: management moved from "180 degrees reverse" (Q4) to "there are execution delays on the data centre side" (Q1), after first denying it on the same call; B05 3B records it as delays "not at TD". Triveni reports dispatches pushed out for the same reason | Record as tone shift and leading indicator; add tracker kill signal: OEM or customer reports of deferred dispatch or commissioning |
| C | C-G05 | B01 (rule P01 L20-21, L27-31) | Proxy capital employed replaces Total Assets less Current Liabilities (B01 L16); capex and payable gaps in the same scorecard scored NOT FOUND = 0 (B01 L44, L46) | AR basis FY26 30.8%, FY25 27.5% vs proxy 30.6%, 27.4%; no band change on the proxy reading; strict reading Block A 2, core 39, AVOID; operator ruling or screener ROCE row separates |

### MINOR

| Verifier | ID | Location anchor | Finding | Source truth or fix, as the verifier wrote it |
|---|---|---|---|---|
| A | A-2 (source_fidelity: true) | 05-concall.md s1B rows FY28 capacity, Debottlenecking capex, FY29-FY30 capacity, Large-generator announcement; s2A row 23 | INR22 billion, INR500 million, INR40 billion and above, "month of August" at Q1C p.3 | All four are on Q1C p.4 (txt lines 154-164); p.3 holds order book, inflow and sales. Figures exist one page later; 04 and 09 anchor p.4 |
| A | A-3 (source_fidelity: true) | 05-concall.md s0A item 1 and s1B Capacity row | NK Q4C p.13: capacity to address INR32 billion for FY28 | Quote is on Q4C p.14 (txt line 597); p.13 has no INR32 billion text. One page off |
| A | A-4 (source_fidelity: true) | 05-concall.md s3A first row and s3D Customers bullet | Siemens 2012 licence and Alstom agreement in presentation p.4 | Timeline is on slide 5; slide 4 is the divider page. One page off; 04 and 07 cite slide 5 |
| A | A-5 (source_fidelity: true) | 07-emoat.md s0 item 1 | Q1C p.5: "it is not written in stone" | Text is on Q1C p.6 (txt line 245). One page off; 09 anchors p.6 |
| A | A-6 (source_fidelity: true) | 09-tam.md s1B | p.6: no market-share number (B04 cites p.9) | Market-share answer is on Q1C p.9 (txt lines 377-381); p.6 has none. Self-contradicting anchor; p.9 half is right |
| A | A-7 (source_fidelity: true) | 04-bizmodel.md s2A competition row and s2B BRUSH row | BRUSH Group, CG Newage, Kirloskar Electric at Pres. slide 15, 17 | CG Newage slide 15, Kirloskar slide 17, BRUSH Group slide 18. BRUSH one slide beyond the cited pair |
| A | A-8 (source_fidelity: false) | 04-bizmodel.md s0 item 4, s4A, s4C; 05-concall.md s0A item 4; 07-emoat.md s0 item 4 | Promoter holding 26.5% at 30 Sep 2026 (Pres. slide 36), paired in 05 with the 30 Sep 2026 shareholding pattern | Slide 36 prints 26.5% on a post-QIP denominator; Reg 31 for 30 Sep 2026 p.3 prints 27.16% (85,207,322 of 313,706,860); 26.51% is in the 12 Oct 2026 pattern. Unlabelled basis; 01 and 08 use 27.16% and explain 26.51% correctly; no score input wrong |
| B | F3 | Q3C p.4-5; Q4C p.4; Q1C p.3-4, p.14; TRITURBINE Q1 FY27 p.3, p.6; TRITURBINE Q4 FY26 p.15 | B06 Q1 labels domestic 10-12% growth PARTIALLY VERIFIED though its net read says the latest quarter reverses it; TD domestic inflow share 21% to 7%; Triveni domestic orders -35.4%, decline broad-based; Q1C says "all segments" buoyant (p.3) and India "fairly subdued" (p.14) | Label CONTRADICTED for the latest quarter, magnitude unanchored; B05 to list the management claim as contradicted by TD's own inflow (segment about 25% of revenue, Q4C p.12) |
| B | F4 | Q3C p.7; Q1C p.10; B05 2A row 9 | B05 2A row 9 (big new US customer) classed missed; neither later call shows non-conversion; Q1C p.10 "no major client additions at the moment" is present-tense | Reclassify UNVERIFIED (silence); counts 11 delivered, 5 partial, 3 missed; grade unchanged |
| B | F5 | Q1C p.13 MV; Q1C p.4; Q4C p.3; AR FY26 p.82 BRSR item 20 | B05 carries MV's "scaling up from 1,750 to 2,600" as headcount fact (1B, 2B, 2E, 3C, 4B item 8) and B06 Q8 partially verifies it; the phrase is ambiguous: 2,600 equals the FY27 revenue guide on the same call; AR shows 1,550 total staff at 31 Mar 2026 (730 employees + 820 workers), which also fits | State both readings; drop headcount 2,600 as a fact; flag B06 Q8 as resting on it |
| B | F6 | Q4C p.9; Q4C p.11 | Speaker attribution: B05 row 2 credits "about INR590 crores" to NK (analyst Ganeshram's words); row 21 credits "INR700 crores ... completely covered" to MV (analyst Garvit Goyal's restatement; MV said "outstanding creditors have been completely covered", then "Yes") | Correct speakers; note CFO used "creditors" for receivables |
| B | F7 (also listed as the one missed item) | Q4C p.3 NK | Missed volunteered negative: 100% of DFPS subsidiary investment (Rs 30 mn) provided in FY26, volunteered in Q4 prepared remarks; absent from B05 and B06 | Add to B05 2D or subsidiary notes beside the Turkey penalty |
| B | F8 | Q3C p.3; Q4C p.3; Q1C p.3; B05 3D | B05 3D roll-forward uses consolidated revenue against an order book and inflow of unstated basis; on B05's standalone Q4 FY26 revenue Rs 534.3 cr the Q3-to-Q4 gap is about -Rs 4 cr not +Rs 51 cr; Q4-to-Q1 gap stays positive, at most Rs 131 cr on standalone total income Rs 630 cr | Name revenue basis as a candidate driver; flag stands in part |
| B | F9 | Q1C p.15, p.17 NK | B05 row 24 says the equity raise was never pre-signalled; the board meeting was notified to the exchange before the Q1 call and an analyst asked about the QIP on it | Reword: not signalled on the Q3 or Q4 calls; pre-notified by board notice before the Q1 call |
| B | F10 | Q3C p.5, p.12; Q4C p.4-5, p.11; Q1C p.4, p.10 | Recorded but not weighed: guidance upside language shrank to "small chance" (I-15); hydro softening and "abroad" vs "not global" (I-17); FX about 90% unhedged by choice (I-19); CFO answer quality (I-24) | Carry as tone notes; FX into margin-bridge sensitivity |
| C | C-G03 | B01 (rule P01 L14) | Per-year revenue, PAT, depreciation, other income, selling and admin, net worth not printed (B01 L32, L42, L78, L92) | None possible; no score change shown |
| C | C-G13 | B01 (rule P01 L47-49) | FY20-FY26 PAT CAGR 41.3% printed for information (B01 L53) | C2 N/M only; strike the 41.3% line; scores unchanged |
| C | C-G45 | B01 (rule P01 L120-122) | M8 scored 0 on no quantified reach (B01 L89) though the AR names sales offices and 68 service centres (AR p.9, p.11 per B07 L38, L133) | M8 1; moat score 26; grand total 71; moats present 5, STRONG, AVERAGE unchanged |
| C | C-E02 | B07 (rule P07 L29, L66-67) | F1, G2, 4B items untagged; A3, F1, G2 lack evidence tables; Siemens 2012 licence on two tiers (B07 L96, L211) | No score change |
| C | C-E03 | B07 (rule P07 L35-36) | Rows anchored only to B03, B05, B08 (B07 L58, L166, L177); three self-reported anchor slips (B07 L461-464) | No score change |
| C | C-E11 | B07 (rule P07 L173) | No mixed-tier convention stated; A1 1.0 on capability items while rarity is claim-tier; E2 0.7 on documented and inference items (B07 L95-100, L153-158) | 17.5 (defining claim) to 22.7 (any documented item); MODEST throughout; EM 25 unmet |
| C | C-E18 | B07 (rule P07 L140-142) | I2 question answered for B2, H2, A1, C1 only (B07 L223-226) | I2 0, unchanged |
| D | D-1 | AZAD Q3 FY26 txt line 492; CGPOWER Q2 FY26 txt line 105-106; TRITURBINE Q1 FY27 txt line 812-813 | Q7 VERIFIED: the first half (OEMs raise prices) rests on CG alone. Azad's gas-turbine price rise came from an analyst question, and Triveni declines to push price. The second half (supplier/OEM pricing difficult) has Azad and Triveni. B06 states this itself (direction only) | PARTIALLY VERIFIED would be the stricter label |
| D | D-2 | CGPOWER Q4 FY26 txt line 128-131; CGPOWER Q2 FY26 txt line 105-107; CGPOWER Q3 FY26 txt line 99 | B06 Part 4, 2B and the cross-peer hypothesis pool CG Power margin gains of 280-380 bps as price-led. CG Q4 FY26 attributes the 287 bps to "efficient order execution and strong operating leverage", not price realization. Q2 (310 bps) and Q3 (378 bps) do cite price realization | None stated beyond the finding |

### Not verifiable

| Verifier | ID | Location anchor | Note, as the verifier wrote it |
|---|---|---|---|
| C | E26 | B07 6D combined classification (rule P07 L203-205) | P07 L203-205 names a standard matrix it does not carry; combined AVERAGE unverified |

### Verifier C classification checks (phase 1)

- Gate 0: "AVERAGE concurs on the stage's disclosed-proxy reading; AVOID (core 39) on the strict NOT FOUND reading of P01 L20-21 and L27-31; separating observation: screener ROCE row FY17-FY26, or an operator ruling on proxies applied to ROCE and capex alike; upside ceiling core 58, so AVERAGE cannot rise."
- Emerging Moat: "18.7 MODEST concurs; 17.5 to 22.7 under consistent multiplier conventions; I1/I2 0.0 in every case."

## Verifier disagreement log

none. No downstream step this run relied on, kept, or cleared a figure that Verifier A flagged. The seven source-fidelity findings stand open as written, and the synthesis files carry the corrected anchors. No outputs/final/verifier-disagreement-log.md file was written.
