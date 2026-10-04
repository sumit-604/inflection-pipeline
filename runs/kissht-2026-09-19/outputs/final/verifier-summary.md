# Verifier summary: KISSHT, run 2026-09-19 (phase 3, final)

Supersedes the phase 1 file of the same name. Scope: Verifier A (numbers), B (concall red flags), D (peer use), and both halves of Verifier C: phase 1 (Gate 0 and Emerging Moat) and phase 3 (valuation, expectation ledger, Role 2 decision and sizing, Section 1B chunk fidelity). Every valuation finding refers to a run priced under the unmerged Section 1B v3.11 draft (open item I5).

## Confidence delta (phase 3)

| Component | Score | Source | Basis |
|---|---|---|---|
| Numerical acceptance | 100 | B12a | 47 material numbers checked; 0 CRITICAL, 0 MAJOR, 2 MINOR |
| Red flag coverage | 67 | B12b | 9 material items found independently; 6 held upstream (1 caught, 5 partial); 3 missed |
| Framework adherence | 80.0 | B12c (combined) | Phase 1 62/80 (77.5%) plus phase 3 78/95 (82.1%) = 140/175 |
| Peer utilisation | 90.9 | B12d | 10 substantive of 11 distinct peer transcripts; 3 of 3 peers used |
| **Overall** | **67** | confidence.yaml | Minimum of the four, set by red flag coverage; band 60 to 74 downgrades a PROCEED family verdict one level |

Not applicable: none. Pending: none. REWORK gate: not triggered (no Verifier A CRITICAL; no acceptance rate below 60).

## Acceptance rates and counts

| Verifier | Model | Acceptance rate | CRITICAL | MAJOR | MINOR | REWORK trigger |
|---|---|---|---|---|---|---|
| A numerical | claude-haiku-4-5 | 100 | 0 | 0 | 2 | no |
| B red flags | claude-opus-5 | 67 | 0 | 11 | 9 | no |
| C framework, phase 1 (Gate 0, Emerging Moat) | claude-opus-5 | 77.5 (62/80) | 0 | 8 | 13 | no |
| C framework, phase 3 (valuation, ledger, Role 2, chunk fidelity) | claude-opus-5-5 | 82.1 (78/95) | 0 | 10 | 17 | no |
| C framework, combined | | 80.0 (140/175) | 0 | 18 | 30 | no |
| D peers | claude-sonnet-5 | 100 (block); 90.9 used in delta | 0 | 0 | 3 | no |

Verifier B's independent list held one item it rated CRITICAL (I1, the partner loss cost left unquantified on both calls with contradictory Q1 answers). It logged it as MAJOR because the pipeline caught it in part, and asked synthesis to carry it as a HIGH item.

Verifier C phase 3 did not check the business understanding narrative (rule 9): the Stage 13 output was not among its inputs. Its note reads "any fail = REWORK stage 13".

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| C (ph 3) F1 | B11 §1B.1 row G; pillar_detail.sector_cap_used 22.67; deliberation override 3 | 1/3 x 18x plus 2/3 x 25x is not a row; operator ruled, disclosed; escalates to CRITICAL if the 18x row is assigned (prob-weighted HR PASS to CONDITIONAL). Recomputed: 18x row gives T2 18.0x, T1 18.0x, today T1 Rs 404.0, Y3 T1 Rs 718.4, entry Rs 335.3, HR pw ~1.84; 25x row gives T2 24.5x, T1 18.62x |
| C (ph 3) F2 | B11 §1B.2; destination_pe.own_book_pb_approved | Operator band not earned; no own book slice worksheet line; 0.8x/1.2x pairing to tracks has no Section 1B basis. Recomputed earned 0.65x/0.72x: T1 today Rs 394.6, T2 today Rs 469.0, T1 Y3 Rs 750.7, FV CAGR 23.9%, entry Rs 350.2, HR mid ~2.00 |
| C (ph 3) F3 | B11 §1B.0 A27.1 line; §1B.1 row A; pillar_detail.roce_used 34.0 | ~34% basis NOT FOUND (gate file §2 line 77); surplus cash inside the denominator not tested; CRITICAL if the basis includes surplus cash. Reading ex Rs 208.05 Cr: 45.8%, Pillar 1 27.8x, T1 21.2x (+2.5x), today ~Rs 455, entry ~Rs 381 |
| C (ph 3) F4 | B11 §1B.0 A27.1 line; B10.net_cash_surplus_cr | Cash base NOT FOUND; ~Rs 171.2 Cr IPO net proceeds at the parent unclassified (AR p.98 line 11664 vs AR p.57 AOC-1). If surplus: +Rs 8.2/share on every FV and entry line; strip its treasury income from EPS |
| C (ph 3) F5 | B11 §1B.1 row A; deliberation §5 Slice 2 | 24 + 0.3 x (34 - 33) = 24.3x; disclosed by B11. Recomputed T1 18.47x; today Rs 411.6; Y3 Rs 733.0; entry Rs 342.0 |
| C (ph 3) F6 | B11 §4F; upside_downside_ratio 0.8; verdict card | Partner exit stress (ledger D2) used as the downside; Mar-27 value against an Oct-26 price. Recomputed Year 3: no downside (bear Rs 519.5 > CMP), n.m., >= 2x; valuation date bear lens 2.9x |
| C (ph 3) F7 | B11 §4D-3 ledger rows 1-3; expectation-ledger.md; B10 (no downstream_candidates) | No catalyst cites a B09 candidate and no MODERATE cap applied; B09 lines 58-94 hold six candidates. Cite candidates (no change) or cap row 1 at 0.60: T2 17.1%, residual +0.5%, HR ~1.97 PASS |
| C (ph 3) F8 | B11 §3.3 FLAG-BOOK-BASE-CONFLICT; §2C consolidated equity, BVPS, RoE rows; key assumption +Rs 10.8; open item BOOK | 1,231.98 = Si Creva equity (AR p.57 AOC-1); consolidated 1,342.78 Cr (AR p.98 line 11664; KPI p.10 1,343); the extra book sits at the parent. Own book 2,695.8 stands; Mar-27 consolidated 3,424.0 (BVPS 164.3); RoE FY28 16.7%, FY30 18.7%; +Rs 10.8 sensitivity void; BOOK closes |
| C (ph 3) F9 | B14 verdict card triggers; §7 AVOID row and re-open path; narrative | U/D prong does not fire; the Rs 347.2 re-open condition is not a framework condition. AVOID on Gate 0 AVERAGE alone; strike the U/D trigger and Rs 347.2 |
| C (ph 3) F10 | B14-thesis.yaml line 8 position_size | Machine field Small contradicts AVOID and the card's "None now". Recomputed: position_size "None (AVOID); ceiling Small if re-opened" |
| C (ph 1) | B01 M1 | Cost to Income basis swapped in for M1 only; M2 and M9 keep the naive proxy. Recomputed M1=5 |
| C (ph 1) | B01 M3 | Computable test scored 0 on archetype judgment; the same ROCE accepted in Block A. Recomputed M3=5 |
| C (ph 1) | B01 M8 | "Purely digital" contradicted by the LAP branch network 98 to 101 (IP1 p.11). Recomputed M8=3 (floor 1) |
| C (ph 1) | B01 moat_class | THIN is not the as written result; propagates into B07 6C. Recomputed STRONG (floor MODERATE); classification AVERAGE unchanged |
| C (ph 1) | B01 deal breaker 6 | Literal ND/EBITDA and IC not computed; CAR/PCR swap asserted, not ruled. Recomputed NOT FOUND; operator ruling |
| C (ph 1) | B07 A3, F1 | Deck and concall only metrics graded documented. Recomputed A3 1.4, F1 0.7 |
| C (ph 1) | B07 G1/H2 | Preferential issue double credited; portfolio investors are not strategic partners. Recomputed H2 0 (max 1.0) |
| C (ph 1) | B07 2C / capex_embedded_growth_pct | Unapproved preferential and non lending IPO tranche levered. Recomputed 21.9% (29.2% full IPO) vs 57.8% |
| B | B05 1C, 2C | MISSED guidance drift (I4); B05 claims guidance unchanged or repeated identically (Q4 [page 8-9], [page 11], [page 17]; Q1 [page 5], [page 7], [page 11], [page 14], [page 16]) |
| B | B05 absent | MISSED disbursement fall vs tenure driven AUM and refused disbursement guidance (I7; Q4 [page 5], [page 17-18]; Q1 [page 4]) |
| B | B06 Part 2 absent | MISSED peer contradiction of Kissht "Q1 seasonal" asset quality explanation (P1; SBICARD Jul-2026 [page 5-6]; POONAWALLA Jul-2026 [page 8], [page 15]) |
| B | B05 2E, LBF-2 | FLDG economics unquantified on both calls with contradictory Q1 answers; B05 records no repeated evasion and treats mechanics as FACT (I1) |
| B | B05 3C item 2 | Stage 2 2.4 to 3.15%, NNPA 0.29 to 0.36%, CE 97.15 to 96.82% not recorded; "seasonal" answer accepted untested (I3) |
| B | B05 1B, 3D | 249 bps one quarter revenue margin drop vs the Q4 "four to six quarters" trajectory not flagged; origination yield refused (I5) |
| B | B05 3C item 4 | CoB KPI method change in an adverse quarter graded "resolved satisfactorily"; 200 to 150 bps and upgrade timing slip not noted (I6) |
| B | B05 3B, 3D, 4D | 45% multi PL customers framed as corroboration, not as exposure to management's named stress pocket (I8) |
| B | B05 4D, 1C, 2A | NOT SUPPORTED LAP breakeven inconsistency flag; misreads Q4 [page 15] |
| B | B06 Claim 4, Part 4 | OVERSTATED "single most consequential contradiction"; UGRO CoB falling 7 quarters omitted; SBICARD mixed; POONAWALLA cause misattributed; B05 FCNR reliance nonexistent |
| B | B06 Part 5 | NOT SUPPORTED: POONAWALLA "denial" quote is the analyst's question (Jan-2026 [page 18-19]) |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Gate 0, Data Basis Note (2) | SOURCE FIDELITY. FY23 CFO screener Rs 48.36 Cr vs RHP Rs 111.48 Cr; both confirmed in their sources (screener line 57, RHP p.271); conflict disclosed, basis stated per calculation |
| A | B04 Section 1C | Insurance commission FY25 0.3% of revenue; source 34.42 / 13,374.65 = 0.2576%; rounding at the edge (AR Note 23 p.119) |
| C (ph 3) F11 | B11 §4D-4 hurdle basis line | Current PE on A21 run-rate EPS under a FORWARD label. Forward form 12.03x; HR 2.04 unchanged |
| C (ph 3) F12 | B11 §4H DECISION; YAML decision | WATCHLIST vs Gate 0 AVERAGE AVOID rule. Recomputed AVOID (B14) |
| C (ph 3) F13 | B14 §5 Base/Bull FV 5yr | NOT COMPUTED; Year 4 Rs 875.3 reproduces |
| C (ph 3) F14 | B14 §7 FLAG re-open path | Posture condition carried as an aside. Add: STRUCTURAL disproven or proof gate fired |
| C (ph 3) F15 | chunk 06 line 39 | Omits that A21/A22 run on the 27.3 basis; chunk 10 line 60 carries it. No B11 value change |
| C (ph 3) F16 | chunk 06 line 89; Master §4E line 867 | Cubed vs ^N. No B11 value change (B11 used ^3.487) |
| C (ph 3) F17 | chunk 08 line 38 | ACCELERATING without the OR-12 FIRING reading. No B11 value change |
| C (ph 3) F18 | B11 §2B | Lever bps NOT FOUND; net -48 bps from operator FY28 |
| C (ph 3) F19 | B11 §2C-w basis | Growth pace extrapolation labelled RUN-RATE. Definition run-rate PAT Rs 380.32 Cr |
| C (ph 3) F20 | B11 unresolved input 5 (fade anchor) | FY28 vs 35% does not separate the 20% and 46.9% anchors. Use FY29 AUM growth vs 27.5%, 31-May-2029 |
| C (ph 3) F21 | expectation-ledger.md rows D3, W1 | Probability n/a; annotated OPEN status; uncredited |
| C (ph 3) F22 | B14 §3.5 chain 7 | No ledger row; uncredited |
| C (ph 3) F23 | B11 FLAG-PILLAR2L-READING | Q1 GNPA 2.25% sits at the "below 2.25%" FY27 target (Concall Jun-2026 p.9 line 298), not cited |
| C (ph 3) F24 | B10.bvps_fy26_rs 131.33 | Si Creva equity over OnEMI shares; route to Verifier A. Consolidated FY26 BVPS Rs 143.2 |
| C (ph 3) F25 | B11 §4D-5 FV path today row | Today row = 31-Mar-2027 valuation date |
| C (ph 3) F26 | B11 §1B.1 row D | Capacity cross-check and B07 capex embedded figure not addressed; +0x stands on the slice's own reading |
| C (ph 3) F27 | B10 table | downstream_candidates, Debt Capacity, FTTCP Part B, Market-Implied absent; roce_status conflates T3/T4 |
| C (ph 1) | B01 A3 | Mixed ROE bases; median 20.86% sits 0.86pp above the band edge. Recomputed 5 or 4 |
| C (ph 1) | B01 B4 | FY21 required in B4 while A4 accepts FY23. Up to +5 Core, still AVERAGE |
| C (ph 1) | B01 M7 | General market knowledge used. 1 unchanged |
| C (ph 1) | B01 M9 | Prescribed GM proxy not used. 0 unchanged |
| C (ph 1) | B01 M11 | Two year spans labelled three year. Recomputed 1 |
| C (ph 1) | B01 M12 | Scored on judgment. NOT DETERMINABLE |
| C (ph 1) | B01 deal_breakers | Driving years not named for DB2 and DB4 |
| C (ph 1) | B01 M1/M11 | CAGR 13.99% not 14.01%; band unchanged |
| C (ph 1) | B01 B1 vs B2/B3 | FY23 CFO from two sources (disclosed); no score effect |
| C (ph 1) | B07 A3/D1 | AUC series credited in both; D1 likely unchanged |
| C (ph 1) | B07 anchors | Line range pseudo pages; one missing page |
| C (ph 1) | B07 C1 | Mixed tier at 1.0x, scoring item not named. Recomputed 2.0 or 1.4 |
| C (ph 1) | B07 C2 | On book 46.4% (Jun-26) relabelled off book (Jun-25); 0 unchanged |
| B | B06 Claim 6 | OVERSTATED: POONAWALLA gave no numeric raise rationale; direction of contrast holds |
| B | B05 3D | OVERSTATED registered user "jump": 60m was the model training base (Q4 [page 3-4]) |
| B | B06 2B | OVERSTATED SBICARD yields stable to up; margins came off QoQ (Jul-2026 [page 15-16]) |
| B | B05 | MISSED I11: Q4 other income fall unexplained after two questions (Q4 [page 14-15], [page 22]) |
| B | B05 3A | MISSED I12: 2.5x (CEO) vs 5x (CDAO) risk separation on the same call (Q4 [page 5], [page 21]) |
| B | B05 1B | MISSED I13: organic share for Q4 stated as 30% then "27 odd percent" (Q4 [page 6]; Q1 [page 15]) |
| B | B05 | MISSED I14: IPO 25% GCP use described two ways (Q4 [page 8], [page 21]) |
| B | B05 2A | MISSED I15: Q1 ROAE 21.2% on part period IPO equity (net worth 1,343 to 2,245 Cr) |
| B | B05, B06 | MISSED I16: no LAP asset quality disclosure in a ticket band peers mark higher risk (POONAWALLA May-2026 [page 16]; UGROCAP Aug-2026 [page 11]) |
| D | B06 Claim 4 narrative | "Geopolitical environment" phrase is the analyst's (POONAWALLA-Concall_Jul_2026 p.16); number and direction correct |
| D | B06 Claim 3, UGROCAP Aug-2026 | 24% to 14% figure sits on p.7, not p.4/p.9; Claim 3 stays UNVERIFIABLE |
| D | B06 Part 2E, UGROCAP Feb-2026 | Quote sits on p.10, one page later than cited |

## Operator rulings requested by the verifiers

- Verifier C phase 3: partner slice cap row (F1); own book slice method under A27.2 (F2); capital base of the ~34% partner RoE and surplus cash inclusion (F3); A27.1 classification of the ~Rs 171 Cr parent held IPO remainder (F4); close BOOK on the AR figures (F8).
- Verifier C phase 3, recomputed values awaiting operator action: F9 (strike the U/D trigger and Rs 347.2) and F10 (position_size field).
- Verifier C phase 1: Gate 0 lender variant for Blocks A and F, applied symmetrically (G0V); deal breaker 6 for financials (confirm the CAR/PCR substitution or require literal ND/EBITDA and IC).

## Verifier C phase 3 recomputed values

- Destination: partner slice Track 2 18.0x (18x row) or 24.5x (single 25x row) against the approved 22.67x blend; governing Track 1 18.0x to 18.62x against 18.62x (within 1x); formula Pillar 1 24.3x (Track 1 18.47x) against 24.5x. Own book earned P/B 0.65x (r 15.5%) / 0.72x (r 14%) at Mar-27 against the approved 0.8x / 1.2x.
- Decision: AVOID (F12, concurring with B14).
- Expectation ledger: present, downside row present, all rows carry confirm-by and metric thresholds, probabilities in range, decay status valid, no off ledger credit, residual -2.4% of market value, starter cap OK.

## Recomputed values (Verifier C phase 1)

- Gate 0: classification AVERAGE concur. Moat as written 18 points, 4 present, STRONG (floor 16, 3, MODERATE) against B01's 4, 1, THIN. Grand total 69 (floor 67) against 55.
- Emerging Moat: 15.6 to 16.6 against 18.5. MODEST concur. The EM 25 or above UA qualifier is unmet either way.
- Capex embedded growth: 21.9% (executed lending tranche) or 29.2% (full IPO) against 57.8%.

## Source fidelity and disagreement

One Verifier A finding carries source fidelity: the FY23 CFO conflict. No downstream step leaned on either value as settled. The gate held; see outputs/final/verifier-disagreement-log.md.
