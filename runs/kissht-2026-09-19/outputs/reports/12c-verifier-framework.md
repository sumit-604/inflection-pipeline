# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, KISSHT (phase 1 scope)

Run date: 2026-09-19 | Model: claude-opus-5 | Scope: Gate 0 (B01) and Emerging Moat (B07) only.
Valuation audit (B10/B11, rules 4, 7, 11-15), the Expectation Ledger (rules 13-14) and the Business Understanding Narrative (rule 9): PENDING PHASE 3. They are not run here.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml; outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.
Verifier C audits rule application. It does not rule on whether a number exists in a source. Verifier A owns that. Where this report re-derives a value, it uses only the inputs B01/B07 state.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

### 1a. Block re-derivation

| Rule | Stated input (B01) | Threshold applied | B01 score | Re-derived | Result |
|---|---|---|---|---|---|
| Opening data line | "Data available: 6 years (FY21 to FY26)" | rule 6 | present | present | PASS |
| A1 Median ROCE | FY23 12.67, FY24 33.12, FY25 28.93, FY26 32.93 | >=25 = 5 | 5 | median (28.93+32.93)/2 = 30.93 -> 5 | PASS |
| A2 Min ROCE | 12.67 | 12-14.9 = 3 | 3 | 3 | PASS |
| A3 Median ROE | -36.39, 6.93, 17.74, 23.97, 28.78, 31.66 | >=20 = 5 | 5 | median (17.74+23.97)/2 = 20.86 -> 5 | FAIL (MINOR, basis): four of six years are company-reported ROE, two are computed on closing net worth. The fixed formula is PAT / average net worth. The median sits 0.86pp above the 20% band edge, so a single-basis series could score 4. Core 51 -> 50 at worst; no classification change. |
| A4 ROCE trend | FY26 32.93 vs FY23 12.67 | latest >= earliest = 5 | 5 | 5 | PASS |
| Block A | | | 18 | 18 | PASS |
| B1 Cum CFO/PAT | CFO sum -1,648.00; PAT sum 671.20 | <0.50 = 0 | 0 | -1,648.00 / 671.20 = -2.46 -> 0 | PASS |
| B2 FCF+ years | FY23 +102.37, FY24 -640.48, FY25 -669.17, FY26 -471.06 | <50% = 0 | 0 | 1 of 4 = 25% -> 0 | PASS |
| B3 Cum FCF/PAT | -1,678.33 / 667.03 | negative = 0 | 0 | -2.52 -> 0 | PASS |
| B4 WC days change | NOT FOUND, scored 0 | rule 5 | 0 | 0 | FAIL (MINOR, window consistency): A4 accepts "earliest available" (FY23), while B4 demands FY21. B01 also contradicts itself on payables coverage ("partially FY23 onward" in B4; "first appears ... FY25-FY26" in M12). A FY25-FY26 comparison was computable on the same earliest-available logic as A4. Maximum effect +5 on Core (51 -> 56); still AVERAGE. |
| Block B | | | 0 | 0 | PASS |
| C1 Revenue CAGR | 175.02 -> 2,208.81, 5 yrs | >=20 = 5 | 5 | (12.62)^(1/5) - 1 = 66.0% -> 5 | PASS |
| C2 PAT CAGR | FY21 PAT -58.45 | N/M = 0 | 0 | 0 | PASS |
| C3 Positive YoY years | 4 of 5 | 75-99 = 3 | 3 | 3 | PASS |
| C4 | C2 N/M | edge rule -> 0 | 0 | 0 | PASS |
| Block C | | | 8 | 8 | PASS |
| D1 CAR (financials) | 25.28% | >=18 = 5 | 5 | 5 | PASS |
| D2 PCR (financials) | 86.15% | >=70 = 5 | 5 | 5 | PASS |
| D3 D/E financials default | default | 3 | 3 | 3 | PASS |
| D4 Current ratio | 31,251.23 / 19,876.56 | 1.5-1.99 = 4 | 4 | 1.572 -> 4 | PASS |
| Block D | | | 17 | 17 | PASS |
| E1 Promoter holding | 24.80% | <30 = 0 | 0 | 0; the professionally-managed alternate correctly not used (2 identified promoter holders) | PASS |
| E2 3-yr change | NOT FOUND (listed 08-May-2026) | rule 5 -> 0 | 0 | 0 | PASS |
| E3 Pledge | 0% | 5 | 5 | 5 | PASS |
| E4 CL / NW | 103.29 / 1,342.78 | 5-15 = 3 | 3 | 7.69% -> 3. The exclusion of the Rs 21,982.06m holding-company guarantee is correct at the consolidated level (subsidiary debt already on the consolidated balance sheet). | PASS |
| Block E | | | 8 | 8 | PASS |
| Core sum | 18+0+8+17+8 | | 51 | 51 | PASS |

### 1b. Block F moat tests

| Test | B01 score | As-written re-derivation | Result |
|---|---|---|---|
| M1 Pricing power | 0 (Cost-to-Income basis) | The rule names EBITDA margin. B01's own naive EBITDA proxy expands 23.1% -> 33.5% (FY24-FY26, B01 Data Basis Note 4). Revenue CAGR FY24-26 >= 10%. As written: 5. | FAIL (MAJOR). B01 substituted a different margin basis for M1 but kept the naive proxy for M2 and M9 in the same block. That is a selective substitution. The choice is disclosed and has economic sense for a lender. But it is not the rule as written. Recomputed M1 = 5. Side note (MINOR): FY24-26 revenue CAGR is (2,208.81/1,700.0)^(1/2) - 1 = 13.99%, not 14.01% as stated in M1 and M11. The band does not change. |
| M2 Cost advantage | 0 | 33.46% vs peer median 58.74% (two peers) -> below -> 0 | PASS |
| M3 Capital efficiency | 0 ("archetype mismatch") | FAT = 2,208.81 / 43.01 = 51.4x (>3x); ROCE 30.93% median / 32.93% FY26 (>20%). As written: 5. | FAIL (MAJOR). Pipeline rule 2 says "No qualitative judgments. Only numbers and the scoring rules provided." The test was computable and B01 scored it 0 on judgment. The same ROCE that B01 accepts in Block A (A1 = 5, A4 = 5) is rejected here. The ROCE mechanic is either valid for the lender or it is not. It cannot be valid where it adds points and invalid where it adds points too. Recomputed M3 = 5. |
| M4 Customer stickiness | 3 | 1 decline year, fully recovered -> 3 | PASS |
| M5 Scale | 0 (PEER DATA NEEDED) | Segment rank not determinable from the provided peers; RHP competitive set is broader | PASS |
| M6 R&D | 0 | NOT FOUND -> 0 | PASS |
| M7 Regulatory | 1 | >10 regulated players -> 1 | FAIL (MINOR, anchor). The player list is sourced partly to "general market knowledge". Pipeline rule 5 requires every figure to come from the provided data. No score change is possible (the 3 tier also needs margin within +/-5pp, which fails on both margin bases). |
| M8 Distribution | 0 ("purely digital") | The AR discloses a LAP branch network (AR p.9, as cited in B07 1A). B07 2D anchors 98 -> 101 branches (IP1 p.11). Revenue CAGR 66%. As written: 3 ("network growing AND rev CAGR >= 15%"). The floor is 1 ("mentioned unquantified") if the growth reading is rejected. | FAIL (MAJOR). "No physical branch/outlet network in the provided evidence" is contradicted by the corpus. Recomputed M8 = 3 (floor 1). |
| M9 Brand | 0 | The rule's stated proxy is (Revenue - Material Cost) / Revenue. B01 used the EBITDA proxy instead. On the prescribed proxy every lender is about 100%, so the result is "at/below peer median" -> 0. | FAIL (MINOR, proxy not the one prescribed; no score change) |
| M10 Switching costs | 0 | Receivable days +15.5; the 3 tier needs "stable"; the 1 tier needs 2+ decline years -> 0 | PASS |
| M11 Network effects | 0 | B01 labels two 2-year spans as "3yr windows". The latest 3-year CAGR (FY23 -> FY26) is about 30%. FY23 revenue is about 1,000 Cr, derived only from B01's own figures: FY24 1,700.0 / 1.70. Verifier A should confirm the exact figure. Selling % rising (23.32 -> 26.19). Tier 1 ("growth >15% but selling % rising") -> 1. | FAIL (MINOR; 0 vs 1, no moat-present effect) |
| M12 Negative WC / float | 0 ("archetype mismatch") | Scored on judgment although FY25-FY26 WC days are computable. From B01's stated figures, FY26 receivable days are 17.24 and payable days are 104.84 / 2,208.81 x 365 = 17.3, so FY26 WC is about -0.1 days. B01 does not state FY25 receivables, so the "majority of years" test cannot be closed here. | FAIL (MINOR; method breaches rule 2, outcome NOT DETERMINABLE from B01) |
| Moat total / class | 4; 1 present; THIN | As written: M1 5 + M3 5 + M4 3 + M7 1 + M8 3 + M11 1 = 18. Present: M1, M3, M4, M8 = 4 -> STRONG. Floor case (M8 = 1): 16, 3 present -> MODERATE. | FAIL (MAJOR). moat_class THIN is not the as-written result. It propagates into B07 6C. |

### 1c. Classification, confidence, deal-breakers, edge rules

| Rule | B01 | Check | Result |
|---|---|---|---|
| Data confidence | 6 yrs -> "lower", no downgrade | 5-6 = flag only; downgrade only at 3-4 | PASS |
| Classification matrix | Core 51 -> AVERAGE | Core 40-59 = AVERAGE whatever the moat class. The M1/M3/M8 findings do not change it. Grand total would move 55 -> 69 (or 67). | PASS |
| DB1 Block A < 8 | not fired | A = 18 | PASS |
| DB2 Block B < 8 | fired | B = 0 | PASS |
| DB3 median ROCE < 10 | not fired | 30.93 | PASS |
| DB4 CFO/PAT < 0.50 | fired | -2.46 | PASS |
| DB5 pledge > 15 | not fired | 0% | PASS |
| DB6 ND/EBITDA > 3x AND IC < 3x -> AVOID | "does not apply", CAR/PCR substituted | The deal-breaker text has no financials swap. Block D scoring does. B01 did not compute or state the literal ND/EBITDA and EBIT/interest values, and neither is in B01 (NOT FOUND). A literal reading on a lender with D/E 1.78x could reach the AVOID clause. The CAR/PCR substitution is the more defensible reading because Block D swaps the same two metrics for NBFCs. But the substitution was asserted, not ruled. | FAIL (MAJOR; unresolved; operator ruling needed so the literal clause cannot later be read to AVOID) |
| DB7 revenue declined majority | not fired | 1 of 5 | PASS |
| DB8 PAT negative last 3 yrs | not fired | FY24-26 positive | PASS |
| DB9 history < 3 | not fired | 6 yrs | PASS |
| Deal-breaker years stated | ratio stated | The rule says "state WHICH years drive any deal-breaker". The DB2/DB4 entries in deal_breakers[] do not name the driving years (FY24-FY26 CFO outflows). The B1 table lets a reader rebuild them. | FAIL (MINOR) |
| CAGR edge: negative endpoint -> N/M, 0 | C2 N/M | honoured | PASS |
| CAGR edge: loss-to-profit swing note in data_notes | present (FY21 to FY22) | honoured | PASS |
| CAGR edge: C4 = 0 when PAT CAGR N/M | 0, noted | honoured | PASS |
| FLAG-GATE0 on <= AVERAGE with depressors | present | honoured | PASS |
| Anchor rule (rule 4) | anchored except M7 | see M7 | PASS (M7 counted there) |
| YAML schema complete | all fields present; moat_score 4 and grand_total 55 match the table as B01 scored it | | PASS |
| FY23 CFO dual source (observation) | B1 uses screener 48.36; B2/B3 use RHP 111.48 | Disclosed. No score effect (FCF FY23 is positive on either figure). Two sources for one year inside one block. | MINOR finding, not a rule fail |

Gate 0: 52 rules checked, 12 FAIL (5 MAJOR, 7 MINOR), 0 CRITICAL. The classification (AVERAGE) survives every finding.

**Load-bearing Gate 0 finding.** Gate 0 has a lender variant for Block D only. For Blocks A and F, B01 took the literal formula where it scores high (A1, A2, A4 on a ROCE it calls inflated) and set literal tests aside where they would also score high (M1, M3), or scored on judgment (M8, M12). Two readings exist:
- As-written literal: moat class STRONG (18 pts, 4 present).
- Lender-adapted and applied symmetrically: the finance-cost-inflated ROCE is rejected in Block A as well as in M3, so A1/A2/A4 become NOT DETERMINABLE and M3 stays 0.

One observation separates the two readings: an operator ruling on whether Gate 0 Blocks A and F take a lender variant. Neither reading changes the Gate 0 classification (AVERAGE). Both change moat_class, which B07 6C consumes.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Check | Result |
|---|---|---|---|
| EM-1 | All 22 categories + R1 addressed (23 scored rows) | A1-I2 in Section 3, R1 in Section 4, 23 rows in Section 5 | PASS |
| EM-2 | NO EVIDENCE FOUND stated where empty | A1, A2, A4, B1, B2, B3, E1, E2, H3 | PASS |
| EM-3 | Evidence taxonomy applied per item | icons present per item | PASS |
| EM-4 | Source anchors on every evidence item | Several anchors are text-extraction line ranges, not pages: "AR p.7903/12147", "AR p.4446-4505", "AR p.~3255-3311", "AR p.1688-1779". One has no page: "AR p. Note 4(b)". | FAIL (MINOR) |
| EM-5 | Completionist guard applied | 9 non-zero categories (< 12); recount performed; A4 downgraded on recount | PASS |
| EM-6 | Recount line in mandated form | "📄 recount performed: 11 documented items across 8 categories" | PASS |
| EM-7 | L x I matrix mapping | A3 MM=2, C1 MM=2, D1 HH=4, D2 MH=3, F1 LM=1, F2 LM=1, G1 HM=3, H1 LL=1, H2 MM=2: all map correctly | PASS |
| EM-8 | Multiplier matches stated tier | C1 is stated "📄/🎙️" (mixed) but takes 1.0x. B07 does not name which 📄 item carries the MM score. The durability and fee-line legs are 🎙️. | FAIL (MINOR) |
| EM-9 | Scores consistent with the taxonomy (no 🎙️ credited as 📄) | A3: the AUC series (66 -> 74%) is anchored only to investor decks (IP1 p.23, Q4 deck p.24) and concalls. The prompt's taxonomy puts "stated in concall or presentation, not yet backed by committed capital or signed contracts" at 🎙️. A self-reported, unaudited model-performance metric in a filed deck is still a presentation claim. Filing it with BSE does not change its tier. F1: data-scientist headcount (41 -> 48) is also deck-only. | FAIL (MAJOR). Recomputed: A3 2 x 0.7 = 1.4 (-0.6); F1 1 x 0.7 = 0.7 (-0.3). This reading could be separated from B07's reading by one observation: whether the AR (a statutory document) or an independent source carries the AUC series. |
| EM-10 | Adjusted total arithmetic | 2+2+4+3+1+1+3+0.5+2 = 18.5 | PASS |
| EM-11 | Classification band | 18.5 -> 12-24 MODEST | PASS |
| EM-12 | I1 (cat 21): >0 only with both legs, (b) with >=1 📄 | (b) absent -> 0 | PASS |
| EM-13 | I2 (cat 22): >0 only with a specific named sacrifice | "nothing must be destroyed" -> 0, execution lead | PASS |
| EM-14 | I1/I2 contribution stated separately | 0.00 stated | PASS |
| EM-15 | R1 Section 4 (4A-4C) | present, 0 | PASS |
| EM-16 | Section 1 (1A-1C) | present | PASS |
| EM-17 | Section 2 (2A-2D) | present | PASS |
| EM-18 | 2C: capex UNDER EXECUTION x historical FAT = % above current revenue | B07 uses a stated lender form: capital x 2.75x leverage / AUM. The adaptation is reasonable. But the base includes the Rs 832.2 Cr preferential issue, which is board-approved only and pending the 14-Oct-2026 EGM, so it is not "under execution". It also applies leverage to the full Rs 850 Cr IPO, although 25% (Rs 212.5 Cr) is earmarked for tech, brand and general corporate use, not lending equity. | FAIL (MAJOR). Recomputed on the executed lending tranche only: 637.5 x 2.75 / 8,001 = 21.9% (29.2% on the full IPO), vs 57.8% stated. capex_embedded_growth_pct feeds stage 11. |
| EM-19 | Section 3 summary table, all 22 rows | present, with evidence, type, strength, time | PASS |
| EM-20 | Optionality register (table + YAML) | 7 rows, 4 columns, carried in YAML | PASS |
| EM-21 | Section 6 (6A-6E) | present | PASS |
| EM-22 | 6C uses the injected B01 block | Core 51, moat_score 4, 1 confirmed, THIN, AVERAGE: all match B01 as emitted | PASS (the THIN input carries the Gate 0 M1/M3/M8 finding upstream; B07 read it faithfully) |
| EM-23 | 6D combined classification | AVERAGE backward + MODEST forward -> AVERAGE; no HIGH POTENTIAL / TURNAROUND row triggered | PASS |
| EM-24 | One improvement, one mechanism | (a) The Rs 832.2 Cr preferential issue is credited twice: in G1 (war chest, HM = 3) and in H2 (named institutional investors as a "smart money" signal). (b) The AUC series is evidence in both A3 and D1. | FAIL: (a) MAJOR, (b) MINOR. B07 guarded the B3/D2 overlap explicitly but not these two. |
| EM-25 | Evidence fits the category's what-to-look-for list | H2's list is JV with a global leader, exclusivity, tech licensing, co-development, strategic equity investor. MIT endowment, Axis MF, HDFC MF and White Oak are portfolio investors, not strategic ones. A brand ambassador who also holds CCPS is not on the list. C2 substitutes off-book partner concentration for customer concentration. It also labels "46.4% (Jun-25, implied)" as off-book share, but Section 1C gives 46.4% as the ON-book share at Jun-26 (off-book was 49.7% at Mar-26). C2 scores 0 whichever way it is read. | FAIL. H2: MAJOR (merged with EM-24a for severity; one finding). C2 figure: MINOR. Recomputed H2: 0 once the preferential leg is removed and category fit is applied; at most LL = 1 on the Tendulkar leg. |
| EM-26 | YAML schema complete | all fields present; em_classification uses the enum | PASS |
| EM-27 | analyst_note <= 200 words | about 170 words | PASS |
| EM-28 | EM scan not conflated with FTTCP | taxonomy note present | PASS |

Emerging Moat: 28 rules checked, 6 FAIL (EM-4, EM-8, EM-9, EM-18, EM-24, EM-25). Findings: 3 MAJOR, 4 MINOR, 0 CRITICAL.

**Recomputed EM score.** 18.5 - 0.6 (A3) - 0.3 (F1) - 2.0 (H2) = 15.6. With H2 held at LL 1.0 on the Tendulkar leg: 16.6. The classification stays MODEST (12-24). No threshold is crossed, and the EM >= 25 UA qualifier stays unmet under both readings. The D1 Strong rating and the I1 = 0 and I2 = 0 results stand.

---

## 3. VALUATION (B10/B11): PENDING PHASE 3

Not run in this invocation, by scope. Rules 4, 6 (stage 11 leg), 7, 11, 12, 13, 14 and 15 await the phase-3 verifier pass. So does rule 9 (the stage 13 narrative).

---

## 4. CONSOLIDATED FINDINGS

| # | Sev | Location | Rule | Finding | Recomputed |
|---|---|---|---|---|---|
| 1 | MAJOR | B01 M1 | Block F, M1 text; rule 2 | Cost-to-Income basis swapped in for EBITDA margin in M1 only | M1 = 5 |
| 2 | MAJOR | B01 M3 | rule 2; Block F M3 | Computable test scored 0 on judgment; same ROCE accepted in Block A | M3 = 5 |
| 3 | MAJOR | B01 M8 | Block F M8 | "Purely digital" contradicted by the disclosed LAP branch network (98 -> 101) | M8 = 3 (floor 1) |
| 4 | MAJOR | B01 moat_class | moat classification | THIN is not the as-written result; it propagates into B07 6C | 18 pts / 4 present / STRONG (floor 16 / 3 / MODERATE); classification AVERAGE unchanged |
| 5 | MAJOR | B01 DB6 | deal-breaker 6 | Literal ND/EBITDA and IC not computed; CAR/PCR swap asserted, not ruled | NOT FOUND; operator ruling |
| 6 | MINOR | B01 A3 | ROE formula | Mixed company-reported and computed ROE bases; median 0.86pp above the band edge | 5 or 4 |
| 7 | MINOR | B01 B4 | earliest-available consistency | B4 requires FY21 while A4 accepts FY23; payables coverage stated two ways | up to +5 Core |
| 8 | MINOR | B01 M7 | rule 5 grounding | Peer list partly "general market knowledge" | 1 (unchanged) |
| 9 | MINOR | B01 M9 | M9 proxy | Prescribed GM proxy not used | 0 (unchanged) |
| 10 | MINOR | B01 M11 | M11 windows | 2-year spans labelled 3-year; the FY23-26 CAGR (about 30%) gives tier 1 | 1 |
| 11 | MINOR | B01 M12 | rule 2 | Scored on judgment; FY26 WC days about -0.1; FY25 not stated | NOT DETERMINABLE |
| 12 | MINOR | B01 deal_breakers | override text | Driving years not named for DB2/DB4 | n/a |
| 13 | MINOR | B01 M1/M11 | arithmetic | FY24-26 revenue CAGR is 13.99%, not 14.01% | band unchanged |
| 14 | MINOR | B01 B1 vs B2/B3 | consistency | FY23 CFO taken from two sources inside Block B (disclosed) | no score effect |
| 15 | MAJOR | B07 A3 (and F1) | taxonomy, verifier rule 3 | Deck/concall-only metrics graded 📄 | A3 1.4, F1 0.7 |
| 16 | MAJOR | B07 G1/H2 | one improvement one mechanism; category fit | Preferential issue credited in both G1 and H2; portfolio investors are not strategic partners | H2 0 (max 1.0) |
| 17 | MAJOR | B07 2C / capex_embedded_growth_pct | 2C "under execution" | Unapproved preferential issue and the non-lending IPO tranche levered into capacity | 21.9% (29.2% full IPO) vs 57.8% |
| 18 | MINOR | B07 A3/D1 | one improvement one mechanism | AUC series used as evidence in both | D1 HH likely unchanged |
| 19 | MINOR | B07 anchors | rule 3 anchors | Line-range pseudo-pages; one missing page | n/a |
| 20 | MINOR | B07 C1 | multiplier | Mixed 📄/🎙️ at 1.0x with no named scoring item | 2.0 or 1.4 |
| 21 | MINOR | B07 C2 | internal consistency | 46.4% (on-book Jun-26) relabelled as off-book Jun-25 | 0 (unchanged) |

Totals: CRITICAL 0 | MAJOR 8 | MINOR 13. No finding flips a Gate 0 classification, the EM band, or a decision. Nothing here triggers REWORK. Two items need an operator ruling: the lender variant for Gate 0 Blocks A and F, and the DB6 literal clause.

Acceptance: rules checked 80 (Gate 0 52 + EM 28); passed 62; acceptance_rate 77.5%.

stage: B12c
company: "KISSHT"
run_date: "2026-09-19"
model: claude-opus-5
status: complete
scope: "phase 1 (Gate 0 B01 + Emerging Moat B07); valuation pending phase 3"
gate0: {rules_checked: 52, fails: ["M1 MAJOR: Cost-to-Income swapped for EBITDA margin in M1 only; as-written M1=5", "M3 MAJOR: computable test scored 0 on judgment (rule 2); FAT 51.4x, ROCE 30.93%; as-written M3=5", "M8 MAJOR: 'purely digital' contradicted by LAP branch network 98->101; as-written M8=3 (floor 1)", "moat_class MAJOR: as-written 18 pts / 4 present / STRONG (floor 16/3/MODERATE) vs THIN; classification AVERAGE unchanged", "DB6 MAJOR: literal ND/EBITDA and IC not computed (NOT FOUND); CAR/PCR swap asserted not ruled; operator ruling needed", "A3 MINOR: mixed ROE bases, median 20.86 sits 0.86pp above band edge", "B4 MINOR: earliest-available window applied inconsistently vs A4", "M7 MINOR: peer count partly general market knowledge", "M9 MINOR: prescribed GM proxy not used; score unchanged", "M11 MINOR: 2-yr spans labelled 3-yr; FY23-26 CAGR ~30% gives 1", "M12 MINOR: scored on judgment; FY26 WC ~-0.1 days, FY25 not stated; NOT DETERMINABLE", "deal_breakers MINOR: driving years not named for DB2/DB4"]}
emoat: {rules_checked: 28, fails: ["EM-9 MAJOR: A3 AUC series and F1 headcount rest on deck/concall only, graded documented; recomputed A3 1.4, F1 0.7", "EM-24/25 MAJOR: Rs 832.2 Cr preferential credited in G1 and H2; portfolio investors not strategic partners; recomputed H2 0 (max 1.0)", "EM-18 MAJOR: 2C levers unapproved preferential and non-lending IPO tranche; recomputed 21.9% (29.2% full IPO) vs 57.8%", "EM-24 MINOR: AUC series evidence in both A3 and D1", "EM-4 MINOR: AR anchors are text line ranges, one missing page", "EM-8 MINOR: C1 mixed tier at 1.0x without named scoring item", "EM-25 MINOR: C2 uses 46.4% on-book Jun-26 as off-book Jun-25"]}
valuation: {rules_checked: 0, fails: [], note: "pending phase 3"}
expectation_ledger: {note: "pending phase 3 (rules 13-14 not in phase-1 scope)"}
business_understanding_narrative: {note: "pending phase 3 (rule 9, stage 13 not yet run)"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: "classification AVERAGE concur; moat as-written 18 pts / 4 present / STRONG (floor 16 / 3 / MODERATE) vs B01 4 / 1 / THIN; grand_total 69 (floor 67) vs 55"
recomputed_em: "15.6 to 16.6 vs 18.5; MODEST concur; EM>=25 UA qualifier unmet either way"
recomputed_capex_embedded_growth_pct: "21.9 (executed lending tranche) or 29.2 (full IPO) vs 57.8"
operator_rulings_requested: ["Gate 0 lender variant for Blocks A and F, applied symmetrically (literal ROCE either valid in both A1/A2/A4 and M3, or in neither)", "Deal-breaker 6 for financials: confirm CAR/PCR substitution or require literal ND/EBITDA and IC"]
findings:
  - {severity: MAJOR, location: "B01 M1", rule: "Block F M1; pipeline rule 2", note: "Cost-to-Income basis swapped in for M1 only; M2/M9 keep naive proxy", recomputed: "M1=5"}
  - {severity: MAJOR, location: "B01 M3", rule: "pipeline rule 2", note: "computable test scored 0 on archetype judgment; same ROCE accepted in Block A", recomputed: "M3=5"}
  - {severity: MAJOR, location: "B01 M8", rule: "Block F M8", note: "LAP branch network disclosed (AR p.9 per B07; 98->101 IP1 p.11)", recomputed: "M8=3 (floor 1)"}
  - {severity: MAJOR, location: "B01 moat_class", rule: "moat classification", note: "THIN not the as-written result; propagates into B07 6C", recomputed: "STRONG (floor MODERATE); classification AVERAGE unchanged"}
  - {severity: MAJOR, location: "B01 deal-breaker 6", rule: "deal-breaker overrides", note: "literal test not computed; swap asserted", recomputed: "NOT FOUND; operator ruling"}
  - {severity: MINOR, location: "B01 A3", rule: "ROE formula", note: "mixed bases; 0.86pp above band edge", recomputed: "5 or 4"}
  - {severity: MINOR, location: "B01 B4", rule: "window consistency", note: "FY21 required in B4 while A4 accepts FY23", recomputed: "up to +5 Core, still AVERAGE"}
  - {severity: MINOR, location: "B01 M7", rule: "pipeline rule 5", note: "general market knowledge used", recomputed: "1 unchanged"}
  - {severity: MINOR, location: "B01 M9", rule: "M9 proxy", note: "prescribed GM proxy not used", recomputed: "0 unchanged"}
  - {severity: MINOR, location: "B01 M11", rule: "M11 two-window test", note: "2-yr spans labelled 3-yr", recomputed: "1"}
  - {severity: MINOR, location: "B01 M12", rule: "pipeline rule 2", note: "scored on judgment", recomputed: "NOT DETERMINABLE"}
  - {severity: MINOR, location: "B01 deal_breakers", rule: "state driving years", note: "years not named for DB2/DB4", recomputed: ""}
  - {severity: MINOR, location: "B01 M1/M11", rule: "CAGR formula", note: "13.99% not 14.01%", recomputed: "band unchanged"}
  - {severity: MINOR, location: "B01 B1 vs B2/B3", rule: "single basis", note: "FY23 CFO from two sources (disclosed)", recomputed: "no score effect"}
  - {severity: MAJOR, location: "B07 A3, F1", rule: "evidence taxonomy (verifier rule 3)", note: "deck/concall-only metrics graded documented", recomputed: "A3 1.4, F1 0.7"}
  - {severity: MAJOR, location: "B07 G1/H2", rule: "one improvement one mechanism; H2 category list", note: "preferential issue double-credited; portfolio investors not strategic partners", recomputed: "H2 0 (max 1.0)"}
  - {severity: MAJOR, location: "B07 2C / capex_embedded_growth_pct", rule: "2C under-execution base", note: "unapproved preferential and non-lending IPO tranche levered", recomputed: "21.9% (29.2%) vs 57.8%"}
  - {severity: MINOR, location: "B07 A3/D1", rule: "one improvement one mechanism", note: "AUC series in both", recomputed: "D1 likely unchanged"}
  - {severity: MINOR, location: "B07 anchors", rule: "source anchors", note: "line-range pseudo-pages; one missing page", recomputed: ""}
  - {severity: MINOR, location: "B07 C1", rule: "multiplier vs tier", note: "mixed tier at 1.0x, scoring item not named", recomputed: "2.0 or 1.4"}
  - {severity: MINOR, location: "B07 C2", rule: "internal consistency", note: "on-book 46.4% relabelled off-book Jun-25", recomputed: "0 unchanged"}
critical_count: 0
major_count: 8
minor_count: 13
rework_triggered: false
acceptance_rate: 77.5
