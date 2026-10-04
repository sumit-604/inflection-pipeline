# Verifier summary: KISSHT, run 2026-09-19 (phase 1)

Scope: Verifier A (numbers), B (concall red flags), D (peer use), and the Gate 0 plus Emerging Moat half of Verifier C. Verifier C's valuation half runs in phase 3.

## Confidence delta (phase 1)

| Component | Score | Source | Basis |
|---|---|---|---|
| Numerical acceptance | 100 | B12a | 47 material numbers checked; 0 CRITICAL, 0 MAJOR, 2 MINOR |
| Red flag coverage | 67 | B12b | 9 material (CRITICAL plus MAJOR severity items found independently); 6 held upstream (1 caught, 5 partial); 3 missed |
| Framework adherence | 77.5 | B12c | Gate 0 52 rules plus Emerging Moat 28 rules; valuation half pending phase 3 |
| Peer utilisation | 90.9 | B12d | 10 substantive of 11 distinct peer transcripts; 3 of 3 peers used |
| **Overall** | **67** | min of the four | set by red flag coverage; band 60 to 74 downgrades a PROCEED family verdict one level |

Not applicable: none. Pending phase 3: framework adherence valuation half (B10, B11).

## Acceptance rates and counts

| Verifier | Model | Acceptance rate | CRITICAL | MAJOR | MINOR | REWORK trigger |
|---|---|---|---|---|---|---|
| A numerical | claude-haiku-4-5 | 100 | 0 | 0 | 2 | no |
| B red flags | claude-opus-5 | 67 | 0 | 11 | 9 | no |
| C framework (phase 1 half) | claude-opus-5 | 77.5 | 0 | 8 | 13 | no |
| D peers | claude-sonnet-5 | 100 (block); 90.9 used in delta | 0 | 0 | 3 | no |

Verifier B's independent list held one item it rated CRITICAL (I1, the first loss guarantee dodge on both calls). It logged it as MAJOR in its findings because the pipeline caught it in part. Verifier B asks synthesis to carry it as a HIGH item, and the gate recommendation does so.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 1C, 2C | MISSED guidance drift (I4); B05 claims guidance unchanged or repeated identically. Transcript: credit cost 10 to 15% restated as 15%, ROE 19 to 21% as "20% plus", AUM FY27 as "next 12 months" (Q1 [page 5], [page 7], [page 11], [page 14], [page 16]) |
| B | B05 absent | MISSED disbursement fall (Rs 3,812 Cr against Rs 3,954 Cr) while AUM rose 13% on tenure; disbursement guidance refused; Q4 "reduced ~7%" against a 27% QoQ rise (I7; Q4 [page 5], [page 17-18]; Q1 [page 4]) |
| B | B06 Part 2 absent | MISSED peer contradiction of Kissht's "Q1 seasonal" asset quality explanation; SBICARD and POONAWALLA improved in the same quarter (P1; SBICARD Jul-2026 [page 5-6]; POONAWALLA Jul-2026 [page 8], [page 15]) |
| B | B05 2E, LBF-2 | FLDG economics unquantified on both calls with contradictory Q1 answers; B05 records no repeated evasion and treats the mechanics as FACT (I1; Q1 [page 19-20]; Q4 [page 12-13]) |
| B | B05 3C item 2 | Stage 2 2.4 to 3.15%, NNPA 0.29 to 0.36%, CE 97.15 to 96.82% not recorded; "seasonal" answer accepted untested (I3) |
| B | B05 1B, 3D | 249 bps one quarter revenue margin drop against the Q4 "four to six quarters" trajectory not flagged; origination yield refused (I5) |
| B | B05 3C item 4 | CoB KPI method change in an adverse quarter graded "resolved satisfactorily"; 200 to 150 bps and upgrade timing slip not noted (I6) |
| B | B05 3B, 3D, 4D | 45% multi PL customers framed as corroboration, not as exposure to management's named stress pocket (I8) |
| B | B05 4D, 1C, 2A | NOT SUPPORTED: the LAP breakeven inconsistency flag misreads Q4 [page 15]; "a year or two" referred to steady state ROA, not breakeven |
| B | B06 Claim 4, Part 4 | OVERSTATED: cost of borrowing "contradiction"; UGRO CoB falling 7 quarters omitted; SBICARD mixed; POONAWALLA cause misattributed; B05 FCNR reliance does not exist |
| B | B06 Part 5 | NOT SUPPORTED: the POONAWALLA "denial" quote is the analyst's question (Jan-2026 [page 18-19]) |
| C | B01 M1 | Cost to Income basis swapped in for M1 only; M2 and M9 keep the naive proxy. Recomputed M1=5 |
| C | B01 M3 | Computable test scored 0 on archetype judgment; the same ROCE accepted in Block A. Recomputed M3=5 |
| C | B01 M8 | "Purely digital" contradicted by the LAP branch network 98 to 101 (IP1 p.11). Recomputed M8=3 (floor 1) |
| C | B01 moat_class | THIN is not the as written result; propagates into B07 6C. Recomputed STRONG (floor MODERATE); classification AVERAGE unchanged |
| C | B01 deal breaker 6 | Literal ND/EBITDA and IC not computed; CAR/PCR swap asserted, not ruled. Recomputed NOT FOUND; operator ruling |
| C | B07 A3, F1 | Deck and concall only metrics graded documented. Recomputed A3 1.4, F1 0.7 |
| C | B07 G1/H2 | Preferential issue credited twice; portfolio investors are not strategic partners. Recomputed H2 0 (max 1.0) |
| C | B07 2C, capex_embedded_growth_pct | Unapproved preferential and non lending IPO tranche levered. Recomputed 21.9% (29.2% full IPO) against 57.8% |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Gate 0, Data Basis Note (2) | SOURCE FIDELITY. FY23 CFO screener Rs 48.36 Cr against RHP Rs 111.48 Cr; both exist in their sources (screener line 57, RHP p.271); conflict disclosed, basis stated per calculation |
| A | B04 Section 1C | Insurance commission FY25 0.3% of revenue; source 34.42 / 13,374.65 = 0.2576%; rounding at the edge (AR Note 23 p.119) |
| B | B06 Claim 6 | OVERSTATED: POONAWALLA gave no numeric raise rationale; direction of contrast holds |
| B | B05 3D | OVERSTATED registered user "jump": 60m was the model training base (Q4 [page 3-4]) |
| B | B06 2B | OVERSTATED SBICARD yields stable to up; margins came off QoQ (Jul-2026 [page 15-16]) |
| B | B05 | MISSED I11: Q4 other income fall unexplained after two questions (Q4 [page 14-15], [page 22]) |
| B | B05 3A | MISSED I12: 2.5x (CEO) against 5x (CDAO) risk separation on the same call (Q4 [page 5], [page 21]) |
| B | B05 1B | MISSED I13: organic share for Q4 stated as 30% then "27 odd percent" (Q4 [page 6]; Q1 [page 15]) |
| B | B05 | MISSED I14: IPO 25% GCP use described two ways (Q4 [page 8], [page 21]) |
| B | B05 2A | MISSED I15: Q1 ROAE 21.2% on part period IPO equity (net worth Rs 1,343 Cr to Rs 2,245 Cr) |
| B | B05, B06 | MISSED I16: no LAP asset quality disclosure in a ticket band peers mark higher risk (POONAWALLA May-2026 [page 16]; UGROCAP Aug-2026 [page 11]) |
| C | B01 A3 | Mixed ROE bases; median 20.86% sits 0.86pp above the band edge. Recomputed 5 or 4 |
| C | B01 B4 | FY21 required in B4 while A4 accepts FY23. Up to +5 Core, still AVERAGE |
| C | B01 M7 | General market knowledge used. 1 unchanged |
| C | B01 M9 | Prescribed GM proxy not used. 0 unchanged |
| C | B01 M11 | Two year spans labelled three year. Recomputed 1 |
| C | B01 M12 | Scored on judgment. NOT DETERMINABLE |
| C | B01 deal_breakers | Driving years not named for DB2 and DB4 |
| C | B01 M1/M11 | CAGR 13.99% not 14.01%; band unchanged |
| C | B01 B1 against B2/B3 | FY23 CFO from two sources (disclosed); no score effect |
| C | B07 A3/D1 | AUC series credited in both; D1 likely unchanged |
| C | B07 anchors | Line range pseudo pages; one missing page |
| C | B07 C1 | Mixed tier at 1.0x, scoring item not named. Recomputed 2.0 or 1.4 |
| C | B07 C2 | On book 46.4% (Jun-26) relabelled as off book (Jun-25); 0 unchanged |
| D | B06 Claim 4 narrative | "Geopolitical environment" phrase is the analyst's (POONAWALLA-Concall_Jul_2026 p.16); number and direction correct |
| D | B06 Claim 3, UGROCAP Aug-2026 | 24% to 14% figure sits on p.7, not p.4/p.9; Claim 3 stays UNVERIFIABLE |
| D | B06 Part 2E, UGROCAP Feb-2026 | Quote sits on p.10, one page later than cited |

## Recomputed values (Verifier C, phase 1)

- Gate 0: classification AVERAGE concur. Moat as written 18 points, 4 present, STRONG (floor 16, 3, MODERATE) against B01's 4, 1, THIN. Grand total 69 (floor 67) against 55.
- Emerging Moat: 15.6 to 16.6 against 18.5. MODEST concur. The EM 25 or above UA qualifier is unmet either way.
- Capex embedded growth: 21.9% (executed lending tranche) or 29.2% (full IPO) against 57.8%.
- Operator rulings requested: a Gate 0 lender variant for Blocks A and F, applied to both sides; deal breaker 6 for financials (confirm the CAR/PCR substitution or require literal ND/EBITDA and IC).

## Corrections carried into the narrative and gate recommendation

- LAP breakeven "inconsistency" dropped (Verifier B, NOT SUPPORTED).
- Cost of borrowing peer claim carried as MIXED, not CONTRADICTED (Verifier B, OVERSTATED; Verifier D attribution note).
- Capital raise peer contrast carried with the correction that Poonawalla gave no numeric rationale (Verifier B, MINOR).
- POONAWALLA "denied accelerated write offs" leg of the cross peer hypothesis not used (Verifier B, NOT SUPPORTED).
- Registered user "jump" not used (Verifier B, OVERSTATED).
- Moat class, Emerging Moat score and capex embedded growth quoted with Verifier C's recomputed range where they appear.
- FLDG dodge carried as a HIGH item and as a named missing evidence item on FLAG-CASH (Verifier B, I1).

## Source fidelity and disagreement

One Verifier A finding carries source fidelity: the FY23 CFO conflict. No downstream step leaned on either value as settled, no re-derivation cleared it, and no Verifier C recomputation used it for a score change. Disposition: UNRESOLVED, carried to phase 3 as FLAG-DISAGREEMENT. Disagreements with Verifier A this run: none.
