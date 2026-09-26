# TLL (Trident Lifeline Ltd): verifier summary, phase 1, round 2

Run: tll-2026-09-26. Phase 1 scope: Verifier A (numerical, B12a), Verifier B (red flags, B12b), Verifier C (Gate 0 and Emerging Moat portion only, B12c; valuation audit pending phase 3), Verifier D (peers, B12d). Round 2, after one rework round that re-ran stages 1, 5, 6, 7 and 8.

## Confidence delta (phase 1, round 2)

| Component | Score | Basis |
|---|---|---|
| numerical_acceptance | 95.0 (77.5 as printed; 38 of 40 after 7 source-cleared rows) | B12a: 40 figures checked of a material universe of 45; 31 matched as printed; 7 ANCHOR NOT FOUND rows cleared by orchestrator source re-check (verifier-disagreement-log.md); 1 MINOR open |
| redflag_coverage | 81 | B12b: 13 of 16 MATERIAL (3 CRITICAL, 13 MAJOR) caught upstream, partial counted as caught; full catches 11 of 16 (69%) |
| framework_adherence | 91.2 | B12c phase 1: 62 of 68 rules (Gate 0 40 of 42 = 95.2; Emerging Moat 22 of 26 = 84.6) |
| peer_utilisation | 100 | B06: 12 of 12 peer transcripts SUBSTANTIVE; B12d citation acceptance 90 (18 of 20) |
| overall | 81 | set by redflag_coverage; not_applicable: none; 77.5 if numerical is taken as printed |

Band: 75 to 89 NORMAL. No REWORK trigger: no surviving Verifier A CRITICAL, and every verifier acceptance rate is at or above 60%.

Acceptance rates as each verifier printed them: A 77.5; B 81 (69 on full catches only); C 91.2 (Gate 0 95.2, Emerging Moat 84.6); D 90.

Severity counts as printed: A 0 CRITICAL, 8 MAJOR, 1 MINOR (the findings list carries 7 MAJOR rows); B 3 CRITICAL, 13 MAJOR, 6 MINOR on its independent list (22 items: 14 caught, 3 partially caught, 5 missed); C 0 CRITICAL, 1 MAJOR, 8 MINOR; D 0 CRITICAL, 2 MAJOR, 1 MINOR.

Verifier disagreements: seven Verifier A rows cleared by source re-check, each found printed at the cited anchor. See outputs/final/verifier-disagreement-log.md. That log is not rewritten here.

Round 1 for reference: overall 50, set by redflag_coverage 50 (6 of 12 material caught, 3 in full); REWORK (outputs/superseded/confidence-run1-superseded.yaml).

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note |
|---|---|---|
| B | B02 finding 4; B08 3A | R5 PARTIALLY CAUGHT. TLL bought Mediquip shares from existing holders, promoter group members named, at Rs 11.32 (39,67,800 sh, Feb-2025), Rs 63.00 (7,03,000 sh, Dec-2025) and Rs 95.40 (2,61,825 sh, Mar-2026, post 1:5 bonus). Mar-2026 Reg 30 filed the cost as NA. Mediquip ran private placements at undisclosed prices between tranches. A related party value transfer question, not only a goodwill note gap. Anchor: Annual_Report_2026.txt L6745-6751; 20241224-acquisition.txt L27-29, 66-77, 104-112; 20260101-acquisition.txt L16-20, 103; 20260318-acquisition.txt L17-27, 112; 20260303, 20260417, 20260424, 20260609, 20260616 acquisition filings |

The other two Verifier B CRITICAL items on its independent list were caught upstream and carry no finding row.

### MAJOR

| Verifier | Location | Note | Status |
|---|---|---|---|
| A | B02 Notes finding rank 7 (Claim Income) | FY26 541.05L, FY25 522.17L; AR Note 22 not extracted; unanchored due to extraction limit | CLEARED: Annual_Report_2026.pdf p110 |
| A | B04 Section 1C: TNS Pharma revenue FY26 | 5.77 Cr (576.52L); AOC-1 not extracted | CLEARED: Annual_Report_2026.pdf p40, AOC-1 row 10 |
| A | B04 Section 1C: Trident Mediquip revenue FY26 | 27.32 Cr; AOC-1 not extracted | CLEARED: Annual_Report_2026.pdf p40, AOC-1 row 10 |
| A | B04 Section 1C: TLL Parenterals revenue FY26 | Rs 0; AOC-1 not extracted; material for LBF3 | CLEARED: Annual_Report_2026.pdf p40, AOC-1 row 10 |
| A | B04 Section 1C: TLL Elements revenue FY26 | Rs 2.46L; AOC-1 not extracted | CLEARED: Annual_Report_2026.pdf p40, AOC-1 rows 10 and 13 |
| A | B02 Notes finding rank 6: TNS Pharma investment | Rs 153L to Rs 255L; Note 11 not extracted | CLEARED: Annual_Report_2026.pdf p64 |
| A | B02 Notes finding rank 15: TLL Parenterals term loan | Yes Bank 1,067.47L non-current + 186.44L current; Note 3 not extracted | CLEARED: Annual_Report_2026.pdf p99 |
| B | B08 1A, 3E, REWORK item 1 | R8 PARTIALLY CAUGHT. CFO since 17-Jul-2024, not 2025; CFO through the whole FY25 audit by A Bafna & Associates; signed the FY25 financial statements. Anchor: Annual_Report_2025.txt L1331-1332, 3024-3025, 4600-4609; 20250417-EGM-notice.txt L488-492 | open, Halt 1 |
| B | B08 3E | R9 MISSED. CFO held 30,600 shares as KMP and took 24,000 warrants; Bootstrap Combinator LLP (UBO "Harddik Ashish Bafna") took 36,000 warrants, both non promoter. Separating question: partnership exit date against these holdings. Anchor: 20250417-EGM-notice.txt L387, 393, 611, 618, 667, 679, 747 | open, Halt 1 |
| B | B03 6A, 6B, 8; B05 4A | R6 MISSED. Mediquip turnover fell Rs 35.08 Cr (FY22) to Rs 20.58 Cr (FY24) before TLL bought it from promoter linked holders; FY26 Rs 27.31 Cr still below FY22. Anchor: 20241224-acquisition.txt L120-126; 20260616-acquisition.txt L114-117 | open, Halt 1 |
| B | B05 1B, 4A; B08 3A | R7 MISSED. Promoter group co-owns Parenterals (49% outside TLL) and Mediquip (about 41% outside TLL); TLL guarantees subsidiary debt in full. Economic share of the Rs 200 Cr and Rs 70 Cr peaks to TLL holders is 51% and 58.67%. Anchor: 20241126-acquisition.txt L65-75, 108-111; 20260616-acquisition.txt L19; 20250225-corporate-guarantee.txt L17-47 | open, Halt 1 |
| B | B03 LBF4, 5D, Phase 8 monitorables | NOT SUPPORTED. "True FY25 promoter 65.22%, fall of 2.37pp." FY25 filed figure 63.04%; defect is a mislabelled heading. Anchor: Annual_Report_2025.txt L5095-5096; Annual_Report_2026.txt L10551, 10637-10638; 20250417-EGM-notice.txt L715 | open, Halt 1 |
| C (Emerging Moat) | B07-emoat.yaml catalysts_12m[0], [1] (also [2], [3] expectation legs) | evidence_type documented; recomputed claim for Parenterals Rs 200 Cr and Wellness FY27 commercialisation (deck p13, p14); documented applies to the AOC-1 nil turnover test only. Feeds Pillar 3 | open, Halt 1 |
| D | B06-peers.md Q3 row | Quote cited to INNOVACAP Nov-2025 L590-597, 607, 623-627; found verbatim in INNOVACAP Feb-2026 L589-627. Load bearing for the Q3 PARTIALLY VERIFIED verdict; wrong call attributed | open, Halt 1 |
| D | B06-peers.md Q4 row | Quote cited to CAPLIPOINT May-2026 L338; found verbatim in CAPLIPOINT Nov-2025 L316. Does not flip the UNVERIFIABLE verdict | open, Halt 1 |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Block A: EBIT FY25 | Claimed 17.76 Cr (13.62 + 4.14); AR consolidated P&L PBT 13.61 + interest 3.99 = 17.60 Cr. Gap 0.15 Cr, under 1% impact on the ROCE band; B01 classification unchanged |
| B | B05 item 8, 4A priority 4, 4D | OVERSTATED. Registration stock is a lead indicator; current year export mix cannot falsify it |
| B | B06 Q1, Part 3, Part 4 | OVERSTATED. SENORES 90 to 94 days is a net working capital cycle, a different basis from receivable days (SENORES Jan-2026 L1310-1315) |
| B | B02 pass 1 EPS note | R17 MISSED. Standalone EPS 15.37 in the Board's Report; audited results print 15.50 (20260507-FY26-H2-results.txt L347) |
| B | B08 3C | R22 MISSED. Promoter group took 59.9% of the warrants (5,98,200 of 9,99,000), not the market or other allottees (20250417-EGM-notice.txt L372-401) |
| B | B03 5E | R18 PARTIALLY CAUGHT. Two award Reg 30 filings with press releases through IR firm NeoAtlas (20-Aug, 08-Sep-2026) and an Arihant conference (25-Sep) bracket the BSE surveillance query of 23-Sep-2026, answered with a boilerplate reply |
| C (Gate 0) | 01-gate0.md Block F M5; B01 moat_score | M5 = 1 on a 4 name set where TLL ranks last; recomputed M5 = 0, moat 14, MODERATE and AVERAGE unchanged |
| C (Gate 0) | 01-gate0.md classification deal breaker check; B01 deal_breakers | Driving years not stated. #4 driven by FY22, FY23, FY25 negative CFO; FY23 alone minus 19.00 Cr; ex FY23 ratio minus 0.086, trigger holds |
| C (Gate 0) | 01-gate0.md Block D D1 | D1 = 1 on operating EBITDA 28.11 Cr (2.45x); on all in EBITDA 37.38 Cr the ratio is 1.84x, D1 = 3, core 52 to 54, classification unchanged. PASS WITH NOTE |
| C (Gate 0) | 01-gate0.md Block E E4 | E4 = 3 at 5.17% on the Rs 96.68 Cr parent equity basis; 4.98% on the screener basis and 4.80% with minority interest give E4 = 5; core max 56, still AVERAGE. PASS WITH NOTE |
| C (Emerging Moat) | 07-emoat.md Sections 1B, 1C, 2A, 3 C2, 6B | Anchors to other stages, a rework item and an approximate AR page (p. ~46); replace with primary AR page, note or filing anchors |
| C (Emerging Moat) | B07-emoat.yaml evidence_mix vs completionist_recount | Documented 5 against a recount of 4; reconcile; em_score unaffected |
| C (Emerging Moat) | 07-emoat.md 6C, 6D, 6E; B07 combined_reasoning | M1 and M4 said to sit on the E1 registration platform without an inference label; flag a possible one improvement, two mechanisms overlap for stage 11 |
| C (Emerging Moat) | 07-emoat.md Section 3 E1 and Section 5 E1 row | E1 3.0 is literal compliant, but no first mover or peer absence evidence; at inference tier E1 = 1.5, em_score 6.7, band NONE unchanged. PASS WITH NOTE |
| D | B06-peers.yaml peer_coverage_map, SENORES Q2 FY26 Nov-2025 row | 80 to 90 days is the analyst's framing of the H1 level (L1131); the CFO answers it will move to 90 to 100 days (L1136). Direction inverted; no Part 1 verdict affected |

### Pipeline flag assessments with no severity assigned (Verifier B)

| Location | Note |
|---|---|
| B02 finding 4 | "No purchase consideration disclosure" for Mediquip goodwill is partly wrong: Note 11 prints per share prices for every tranche (Annual_Report_2026.txt L6745-6749). The related party question in the CRITICAL row above stands |

Verifier B spot checks: promise delivery 4 checked, 4 confirmed, 0 wrong. Credibility grade: concurs at D.

Verifier C recomputed card: core 52 (54 to 56 on alternative D1 and E4 bases), moat 14 after M5, MODERATE, AVERAGE; deal breaker #4 binding on every basis. Recomputed em_score: 8.2 concur on stated inputs (6.7 if the E1 first mover leg is taken at inference tier); NONE band holds either way.

Verifier D: 12 of 12 peer transcripts SUBSTANTIVE; claims all addressed; no verdict discipline fails.

Carried open source fidelity items (run 1, for stage 11): FY25 consolidated CFO minus 10.24 Cr (FY25 AR) against minus 3.99 Cr (FY26 AR comparative); segment note receivables 4,947.50 lakh against Note 17 7,365.39 lakh.
