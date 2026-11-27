# VERIFIER C: FRAMEWORK ADHERENCE (B12c). Walchandnagar Industries Ltd (WALCHANNAG), run 2026-11-12

Scope: PHASE 1 only. This run audits Gate 0 (B01) and the Emerging Moat scan (B07). The valuation audit (rules 4, 5, 7 and 11 to 15, on B10 and B11) is deferred to phase 3, because B10 and B11 do not exist yet. The valuation section of B12c is PENDING. Rules 6 (B09 downstream candidates), 9 (stage 13 narrative) and 10 (B09b at /finalize) are also outside this invocation's scope.

Inputs (fresh context, artifacts only; no upstream reasoning, no other verifier output):
- prompts/12-verifiers-pipeline.md, Verifier C section (rubric)
- prompts/01-gate-0-pipeline.md (rule source for B01)
- prompts/07-emerging-moat-pipeline.md (rule source for B07)
- runs/walchannag-2026-11-12/outputs/reports/01-gate0.md and runs/walchannag-2026-11-12/outputs/blocks/B01-gate0.yaml
- runs/walchannag-2026-11-12/outputs/reports/07-emoat.md and runs/walchannag-2026-11-12/outputs/blocks/B07-emoat.yaml

Method. I re-derive every score from the inputs the stage states, with the thresholds in the rule source. I do not test whether a number exists in a source document. Verifier A owns that question. Anchor convention: every input number below is quoted from the B01 or B07 artifact at the location named in the row. A value marked (recomputed) is my arithmetic on those stated inputs.

## RESULT

| Framework | Rules checked | PASS | FAIL | CRITICAL | MAJOR | MINOR |
| --- | --- | --- | --- | --- | --- | --- |
| B01 Gate 0 | 48 | 44 | 4 | 0 | 0 | 4 |
| B07 Emerging Moat | 36 | 33 | 3 | 0 | 0 | 3 |
| Valuation (B11) | PENDING phase 3 | | | | | |
| Total | 84 | 77 | 7 | 0 | 0 | 7 |

Acceptance rate: 77 of 84 = 91.7% (recomputed). The denominator is 4 or more, so the rate applies. It is above 60%. No REWORK trigger fires. Rule 8 passes (Categories 21 and 22 present and correctly scored), so there is no REWORK for stage 7.

Both headline classifications survive every reading I tested:
- Gate 0 AVOID. Core is 10 as scored and 11 on the one score-moving fail (G12). Every alternative reading tested gives at most 14 (B4 +1, E4 claims-only +3). AVOID is core below 40. Deal-breaker 6 forces AVOID on its own: ND/EBITDA 9.75x with interest cover 0.63x in FY26 (B01 report, Block D). It still holds at 3.95x on EBITDA with other income (recomputed: 143.80 / (14.75 + 21.61)).
- Emerging Moat NONE. The adopted score is 5.2. Every reading that obeys the single-credit rule and the evidence tiers lands between 9.0 and 10.3, below the 12 band edge (row E35).

## PART 1. GATE 0 (B01) COMPLIANCE

Inputs: B01 report raw series table (screener-data, INR Cr) and Blocks A to F; B01-gate0.yaml data_notes and deal_breakers.

| # | Rule (prompts/01-gate-0-pipeline.md) | Stage value | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G01 | Op. rule 6: open with "Data available: [X] years ... Scoring adapted to [X]-year history" | "10 years (FY17 to FY26). Scoring adapted to 10-year history." (B01 report line 3) | Present | PASS |
| G02 | ROCE = EBIT / (Total Assets - Current Liabilities); formulas "fixed, do not substitute alternatives"; source ROCE first, else compute and state "computed" | Proxy EBIT / (Equity + Reserves + Borrowings), stated "computed", with AR cross-check on TA - CL for FY24 1.76%, FY25 -8.64%, FY26 5.75% (B01 Block A) | The proxy is a substitution of a fixed formula. Bound on the fixed formula (recomputed): TA - CL = net worth + non-current liabilities, and non-current liabilities cannot be negative, so ROCE <= EBIT / NW. Upper bounds FY17 to FY23: 4.35, 15.07, 23.70, 8.27, 10.50, 18.83, 28.71%. With the AR actuals for FY24 to FY26, A1, A2 and A4 come out the same (rows G03, G04, G06). | FAIL (MINOR). Scores unchanged |
| G03 | A1 median ROCE: <10 = 0 | 3.98% = 0 | Proxy series re-derived, all ten values match; sorted median (3.57 + 4.38) / 2 = 3.98% = 0. Fixed-formula upper-bound median (8.27 + 10.50) / 2 = 9.39% < 10 = 0 (recomputed) | PASS |
| G04 | A2 minimum single-year ROCE: <8 = 0 | -7.41% FY25 = 0 | -7.41% proxy, -8.64% fixed (AR cross-check) = 0 | PASS |
| G05 | A3 ROE = PAT / average NW; closing NW for earliest year, stated | -16.52% = 0; FY17 on closing NW stated | All ten ROE values re-derived and match; sorted median (-19.59 + -13.45) / 2 = -16.52% = 0 | PASS |
| G06 | A4 latest vs earliest: latest >= earliest = 5 | 4.38% vs 1.99% = 5 | Holds on the fixed formula: FY17 <= 4.35% (bound) < FY26 5.75% (AR) = 5 | PASS |
| G07 | Block A sum | 5 | 0 + 0 + 0 + 5 = 5 | PASS |
| G08 | B1 cumulative CFO / cumulative PAT: <0.50 = 0 | -1.30 = 0 | 507.74 / -391.19 = -1.30 (recomputed; both sums re-added and match). Literal band gives 0. The rule has no negative-denominator edge rule (FG-1) | PASS |
| G09 | FCF = CFO - capex | FY24 +9.04, FY25 -19.03, FY26 -36.19 | 10.76 - 1.72, 15.62 - 34.65, -11.08 - 25.11 match | PASS |
| G10 | B2 FCF-positive years: <50% = 0 | 1 of 3 = 33% = 0; FY17 to FY23 capex NOT FOUND, disclosed | 33% < 50 = 0 | PASS |
| G11 | B3 cumulative FCF / cumulative PAT: "<0.20 or negative = 0" | "FCF negative = 0" | Literal arithmetic: -46.18 / -142.52 = +0.32, which sits in the 0.20 to 0.39 band (1). The stage read "or negative" as negative cumulative FCF and scored 0. That reading fits the rule's intent, but the report does not state it (FG-1) | PASS |
| G12 | B4 WC days change, latest vs earliest; op. rule 6 "use whatever history is available"; op. rule 5 NOT FOUND = 0 | FY17 payables NOT FOUND = 0; sensitivity FY24 to FY26 +8.5 days "would band 1" (B01 Block B) | Inconsistent window inside one block. B2 and B3 were scored on the FY24 to FY26 window that exists. B4 had the same window (+8.5 days) and was zeroed instead. A4 used a third treatment (proxy for FY17). Reading 1, strict 10-year window for every metric: B4 0, Block B 0 (as scored). Reading 2, available 3-year window for every metric: B4 1 (increased 5 to 15 days), Block B 1, core 11. Op. rule 6 favours reading 2 | FAIL (MINOR). Recomputed B4 1, Block B 1, core 11. AVOID and deal-breaker 2 unchanged |
| G13 | Block B sum | 0 | 0 as scored (1 on the G12 recompute) | PASS |
| G14 | CAGR formula; C1 revenue CAGR: <5 = 0 | -4.02% = 0 | (275.19 / 397.91)^(1/9) - 1 = -4.02% = 0 | PASS |
| G15 | CAGR edge rule: negative endpoint = N/M, 0 | C2 N/M = 0 | FY17 and FY26 PAT both negative = N/M, 0 | PASS |
| G16 | Loss-to-profit swing note in data_notes | "No loss-to-profit swing across the window" | Endpoints FY17 -79.52 and FY26 -14.66 are both losses. FY23 profit is mid-window. The note correctly does not fire | PASS |
| G17 | C3 positive YoY revenue years: <50% = 0 | 4 of 9 = 44% = 0 | FY18, FY21, FY23, FY26 up; 44.4% = 0 | PASS |
| G18 | C4 = 0 and note when PAT CAGR is N/M | 0, noted | Correct | PASS |
| G19 | D1 net debt / EBITDA: >3x = 0 | 9.75x = 0 | 143.80 / 14.75 = 9.75x = 0; on EBITDA with other income 3.95x, still 0 | PASS |
| G20 | D2 EBIT / interest: <1.5 = 0 | 0.63x = 0 | 25.33 / 39.99 = 0.63x = 0 | PASS |
| G21 | D3 debt / equity: 0.5 to 1.0 = 3 | 0.61 = 3 | 218.90 / 358.79 = 0.61 = 3 | PASS |
| G22 | D4 current ratio: 1.0 to 1.19 = 1 | 1.08 = 1 | 47,678 / 44,109 = 1.08 = 1 | PASS |
| G23 | E1 promoter holding: 30 to 39.9 = 1 | 31.55% = 1 | Correct | PASS |
| G24 | E2 promoter change over 3 years: decreased >3 = 0 | -3.29pp over about 2.75 years = 0; short window disclosed | The drop sits in Q4 FY24, inside any 3-year window ending Sep 2026. The score could differ only if promoter holding moved between Sep and Dec 2023 (NOT FOUND in B01) | PASS |
| G25 | E3 pledge: >15% = 0; deal-breaker 5 | 49.5% of promoter holding = 0 | 15.63 / 31.55 = 49.5%. On the narrower reading (15.63% of the promoter block) it is still above 15 = 0. Both readings fire deal-breaker 5 | PASS |
| G26 | E4 contingent liabilities / NW: >30 = 0 | 57.6% = 0; claims-only 6.7% (band 3) shown | 20,654.64 / 35,879 = 57.6% = 0. Counter guarantees included as disclosed contingent liabilities; open LC and capital commitments excluded, stated | PASS |
| G27 | Core sum | 10 | 5 + 0 + 0 + 4 + 1 = 10 | PASS |
| G28 | M1 pricing power | 12.06% to 5.36%, CAGR -4.02% = 0 | 47.99 / 397.91 and 14.75 / 275.19 match; margin -6.70pp with no growth = 0 | PASS |
| G29 | M2: peer data absent = 0, "PEER DATA NEEDED" | PEER DATA NEEDED = 0 | Rule-compliant | PASS |
| G30 | M3 capital efficiency | FAT 1.04x, ROCE 4.38% = 0 | ROCE fails every tier = 0 | PASS |
| G31 | M4 customer stickiness: 3+ decline years = 0 | 5 decline years = 0 | FY19, FY20, FY22, FY24, FY25 = 0 | PASS |
| G32 | M5 scale | PEER DATA NEEDED = 0 | Rule-compliant | PASS |
| G33 | M6 technology / R&D; op. rule 3 "show every number you extract" | "EBITDA 5.36% fails lower tiers; top tier PEER DATA NEEDED" = 0 (B01 Block F; same text in data_notes) | Tier labels are inverted. The 5 and 3 tiers fail on EBITDA margin (need >= 20% and >= 15%). The 1 tier (R&D/Rev >= 1% AND margin above peer median) is the peer-dependent tier. B01 states no R&D/Rev input. B07 records R&D 0.00% of turnover (B07 Section 3 A2, citing AR 2026 p.51), so the 1 tier fails without peer data | FAIL (MINOR). Score 0 unchanged |
| G34 | M7 regulatory | Listed-player count NOT FOUND = 0 | Rule 5 compliant. Tiers 5 and 3 also fail on the -6.70pp margin change | PASS |
| G35 | M8 distribution | None in data = 0 | Correct | PASS |
| G36 | M9 brand | PEER DATA NEEDED = 0 | Tiers 5 and 3 fail on revenue CAGR in any case; peer data could add at most 1 | PASS |
| G37 | M10 switching costs | Overall decline = 0 | Correct | PASS |
| G38 | M11 network effects (two-window test, >= 6 years) | -5.1% vs +2.6% = 0 | (275.19 / 322.09)^(1/3) - 1 = -5.11%; (322.09 / 298.05)^(1/3) - 1 = +2.62%; growth fails every tier = 0 | PASS |
| G39 | M12 negative WC: >45 days = 0 | 288.7 to 297.2 days = 0; earlier years NOT FOUND | Correct | PASS |
| G40 | Moat present at >= 3; class | 0 present, NONE | 0 = NONE | PASS |
| G41 | Data confidence; history downgrade | 10 years, full, no downgrade | 10+ years = full | PASS |
| G42 | Classification matrix | Core 10 < 40 = AVOID | AVOID at any moat class. The four PEER DATA NEEDED tests cannot change it | PASS |
| G43 | Deal-breakers 1 to 9 applied; driving years stated | 1 to 8 fire, years in B01-gate0.yaml | All eight re-derived: A 5 < 8; B 0 < 8; median ROCE 3.98% (bound 9.39%) < 10; CFO/PAT -1.30 < 0.50; pledge > 15 on both readings; ND/EBITDA 9.75x > 3 and IC 0.63x < 3; revenue down in 5 of 9 YoY steps; PAT negative FY24 to FY26. Number 9 does not apply | PASS |
| G44 | FLAG-GATE0 when classification <= AVERAGE with depressors | Present, depressors by year | Correct | PASS |
| G45 | Report ends with "exactly this fenced YAML block" | Report block carries pointer stubs: input_gaps "see ... B01-gate0.yaml", data_notes "full notes in B01-gate0.yaml", analyst_note "see B01-gate0.yaml", deal_breakers without years, shortened flag reasons. The report text says "years in YAML block", but the years sit only in the separate block file | The block file is complete, so no data is lost. The report copy is not the block | FAIL (MINOR) |
| G46 | analyst_note <= 200 words | About 115 words (block file) | Within cap | PASS |
| G47 | Op. rule 5: NOT FOUND, never estimate | Capex, payables, current liabilities FY17 to FY23 NOT FOUND; peer tests PEER DATA NEEDED | No filled value found | PASS |
| G48 | Quality never halts; flags propagate | "the pipeline does not halt on quality" | Correct | PASS |

Gate 0 tally: 48 checked, 44 PASS, 4 FAIL (all MINOR). One fail moves a score (G12, core 10 to 11). None moves the classification or the deal-breaker set.

## PART 2. EMERGING MOAT (B07) COMPLIANCE

Inputs: B07 report Sections 0 to 6 and the optionality register; B07-emoat.yaml. Matrix and multipliers from prompts/07 Section 5.

| # | Rule (prompts/07-emerging-moat-pipeline.md; verifier rules 3 and 8) | Stage value | Re-derived | Result |
| --- | --- | --- | --- | --- |
| E01 | Op. rule 1: all six sections, one response | Sections 1 to 6 plus register present | Present | PASS |
| E02 | Op. rule 2: tag every evidence item | Tags across Sections 0 to 4. Acuite narrative graded 🎙️ (conservative reading of filed evidence) | Applied | PASS |
| E03 | Op. rule 3: source anchor on every evidence item | Section 0 row 4c still reads "About 18 months tenure at most". The header erratum says this statement has no source and the CFO hire date is NOT FOUND, but the body text was not struck | One unsourced statement left in the body | FAIL (MINOR). Strike the sentence. No score effect |
| E04 | Op. rule 5: "NO EVIDENCE FOUND", never force-fit | A2, A4, B1, B3, C1, C2, D1, D2, E1, F1, G1, G2, H1, H3, I1, I2; B2 and H2 with reasons | Applied | PASS |
| E05 | Op. rule 6: completionist guard vs the 12 trigger | 4 of 23 scored | Well under 12 | PASS |
| E06 | Section 3: "📄 recount performed: [n] documented items across [m] categories." | "7 documented items across 4 scored categories" | Recount: A1 3 (HS200 award, FY25 Aerospace orders, Q2 FY27 Aerospace inflow), A3 1, E2 2, R1 1 = 7. Matches | PASS |
| E07 | Section 1: 1A with status per item, 1B, 1C | Present | Present | PASS |
| E08 | Section 2: 2A to 2D; 2C arithmetic shown | 32.74 x 0.985 = 32.2 Cr, 11.7% above FY26 | 275.19 / 279.49 = 0.985; 32.25 / 275.19 = 11.7%; 32.2 / 358.33 = 9.0%; 84.00 x 0.985 / 275.19 = 30.1%. Match | PASS |
| E09 | Section 3: all 22 categories, each with evidence or NO EVIDENCE FOUND | All 22 addressed | Complete | PASS |
| E10 | Section 3 summary table: 22 rows, evidence, type, strength, time | Present | Complete | PASS |
| E11 | State the Strong/Moderate count | "1 of 22" (A1) | Correct | PASS |
| E12 | Section 4: 4A, 4B, 4C (R1) | Present; SHANTI Act text marked PENDING LIVE VERIFICATION | Complete | PASS |
| E13 | Section 5: 23-row scorecard and adjusted total | Present | Complete | PASS |
| E14 | L x I matrix (HH 4; HM/MH 3; HL/MM/LH 2; ML/LM 1; LL 1; none 0) | A1 HM 3; A3 ML 1; E2 ML 1; R1 MM 2 | All match the matrix. Note: A1 L=H sits beside the stage's own counter-evidence ("replaceable fabricator" terms). At MM (2 x 0.7 = 1.4) the total is 4.5, NONE unchanged | PASS |
| E15 | Evidence multipliers (📄 1.0, 🎙️ 0.7, 🔍 0.5) | A1 0.7, A3 0.7, E2 1.0, R1 0.7 | Each matches the tier of the load-bearing element. Note: E2 at 1.0 rests on 📄 export growth, a listed E2 indicator; the stage itself finds no supply-chain-shift evidence. At 🔍 0.5 the total is 4.7, NONE unchanged | PASS |
| E16 | Verifier rule 3: no 🎙️-only element scored as 📄 (adopted score) | A1 rarity 🎙️, A3 benefit 🎙️, R1 benefit 🎙️, all at 0.7 | None found in the adopted score | PASS |
| E17 | Adjusted total | 5.2 | 2.1 + 0.7 + 1.0 + 1.4 = 5.2 | PASS |
| E18 | Band: < 12 = NO MEANINGFUL EMERGING MOAT | NONE | Correct | PASS |
| E19 | State I1/I2 contribution separately | 0.0, no crossing via I1/I2 | Present | PASS |
| E20 | Verifier rule 8: Category 21 (I1) present; > 0 only with both legs and a 📄 on leg (b) | Present, 0; both legs fail | Correct | PASS |
| E21 | Verifier rule 8: Category 22 (I2) present; > 0 only with a named, specific sacrifice | Present, 0; "nothing documented" | Correct | PASS |
| E22 | One improvement, one mechanism | B2 zeroed, qualification credited once in A1 | Correct | PASS |
| E23 | Optionality register: four-column table, carried in YAML, never scored | 10 rows in report and block | Complete | PASS |
| E24 | 6A timeline: 12m, 12 to 24m, 24 to 36m, 3 to 5 years | Present | Complete | PASS |
| E25 | 6B risks to top moats with early warnings | Present for A1, R1, E2, plus financial and revenue quality | Complete | PASS |
| E26 | 6C uses the injected Gate 0 block | Core 10, moats 0, AVOID, EM 5.2 NONE | Matches B01-gate0.yaml | PASS |
| E27 | 6D: HIGH POTENTIAL and TURNAROUND rows get full reasoning | Both reasoned | Present. The cell itself is not re-derivable (NC-1) | PASS |
| E28 | 6E card: evolution map per family, 12-month catalysts, biggest risk | Present, nine families | Complete | PASS |
| E29 | Report ends with the exact YAML block; block file matches | Report block and B07-emoat.yaml identical | Correct | PASS |
| E30 | active_categories: Strong/Moderate rows only | A1 only | Correct | PASS |
| E31 | em_classification vocabulary | "NONE" | Correct | PASS |
| E32 | evidence_mix item counts agree with the report | documented 8, claim 9, inference 3; claim list "A1 x2, A3 x1, B2 x1, H2 x1, F2 x2, R1 x2" | The report's own 🎙️ tags in Sections 3 and 4 number about 15: A1 3 (not 2), A3 2 (not 1), B2 1, F2 2, H2 1, R1 6 (not 2: 4A EIL certification 1; 4B SHANTI benefit to WIL 1, private orders 1, defence 1, nuclear 1, space 1). The 🔍 count of 3 mixes Section 0 ratios with F2 and omits other 🔍 tags in Sections 0 to 2 (HS200 per-year figure, Foundry share arithmetic, 2C run-rate inference). The counting basis is not stated | FAIL (MINOR). The stated mix reads more documented than the report. If stage 11 reads evidence_mix for Pillar 3, use the recount |
| E33 | capex_embedded_growth_pct equals 2C | 11.7 | Matches | PASS |
| E34 | analyst_note <= 200 words | About 130 words | Within cap | PASS |
| E35 | Two readings built from framework-legal moves; FLAG-EM states what Reading B needs (single-credit rule; verifier rule 3) | Reading B 14.2 MODEST: A1 HH at 📄 4.0, B2 2.1, F2 1.4, H2 0.7, A3 1.0, E2 2.0, R1 HM at 📄 3.0. FLAG-EM: "needs a double credit of A1 and B2 plus a credit on F2" | Reading B also scores three 🎙️ elements at 📄 weight (A1, A3, R1). Without the double credit it is 12.1, still MODEST, so the flag misstates the condition (recomputed). On Reading B's own L x I calls with legal tiers and no double credit: A1 2.8 + A3 0.7 + E2 2.0 + R1 2.1 + F2 1.4 + H2 0.7 = 9.7, NONE. Variants: H2 unscored per the register rule 9.0; F2 at 📄 1.0 gives 10.3 | FAIL (MINOR). Adopted 5.2 NONE stands. NONE holds under every legal reading (9.0 to 10.3). FLAG-EM should say so |
| E36 | Not conflated with FTTCP | Stated at the head of the report | Correct | PASS |

Emerging Moat tally: 36 checked, 33 PASS, 3 FAIL (all MINOR). None moves the score or the classification.

## FINDINGS (consolidated)

| # | Severity | Location | Finding | Recomputed |
| --- | --- | --- | --- | --- |
| F1 | MINOR | B01 Block A; data_notes ROCE line | ROCE computed on a proxy denominator (Equity + Reserves + Borrowings) against a fixed formula that says "do not substitute alternatives" | A1 0, A2 0, A4 5 proven on the fixed formula through the bound ROCE <= EBIT / NW (median bound 9.39%, FY17 bound 4.35% vs FY26 5.75%). Block A 5, deal-breakers 1 and 3 unchanged |
| F2 | MINOR | B01 Block B, B4; data_notes B4 line | Three treatments of one FY17 to FY23 data gap: proxy (A4), narrowed window (B2, B3), NOT FOUND = 0 (B4) | Strict window: B4 0 (as scored). Available window (op. rule 6): B4 1, Block B 1, core 11. AVOID unchanged |
| F3 | MINOR | B01 Block F, M6; data_notes PEER DATA NEEDED line | Tier labels inverted ("top tier PEER DATA NEEDED"); R&D/Rev input not stated | The 1 tier is the peer-dependent tier and fails on R&D 0.00% (B07 A2). Score 0 unchanged |
| F4 | MINOR | B01 report, fenced YAML block | Report block is a pointer stub, not the block; deal-breaker years named as "in YAML block" are absent from it | Block file B01-gate0.yaml complete. Copy the full block into the report |
| F5 | MINOR | B07 Section 0, row 4c | "About 18 months tenure at most" remains in the body after the erratum declared it unsourced | Strike the sentence. No score effect |
| F6 | MINOR | B07 Section 3 recount line; YAML evidence_mix | claim 9 and inference 3 undercount the report's own tags (about 15 🎙️ in Sections 3 and 4); basis unstated | Restate evidence_mix with its counting basis. No score effect |
| F7 | MINOR | B07 Section 5 two readings; YAML FLAG-EM and analyst_note | Reading B rests on a double credit and three 🎙️-as-📄 tier upgrades; the flag names only the double credit and F2 | Legal generous bound 9.0 to 10.3, NONE. Without the double credit alone Reading B is 12.1. NONE robust |

No CRITICAL or MAJOR finding. No recomputed destination PE or decision (valuation out of scope).

## NOT CHECKABLE FROM MY INPUTS (excluded from the denominator)

- NC-1. B07 6D combined cell. prompts/07 6D names "the standard matrix (EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL / GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID)" but defines no cells. AVOID fits Gate 0 AVOID with EM NONE on the plain meaning of the row names. The body carries a wording tension: "TURNAROUND does apply as a description" stands next to "the matrix has no HIGH POTENTIAL or TURNAROUND row to argue" (B07 6D).
- NC-2. B07 F2 cross-reference to the injected B05 promise-delivery record. B05 is not among my inputs. B07 states that no concall record exists (NO-CONCALL MODE) and tests F2 on AR, ICRA and press-release statements instead.

## FRAMEWORK GAPS FOR OPERATOR RULING (not stage fails, not counted)

- FG-1. prompts/01 has CAGR edge rules but no sign rule for ratio metrics. B1 (507.74 / -391.19 = -1.30) and deal-breaker 4 fire on a literal reading, although cumulative CFO exceeds cumulative losses. B3 on two negatives is +0.32, which is band 1 on literal arithmetic; the stage scored 0. Both scores are defensible. A ruling like the CAGR edge rule would remove the ambiguity.
- FG-2. prompts/07 6D cites "the standard matrix" without its cells. The combined classification cannot be re-derived from the rule source.
- FG-3. prompts/07 sets a 🎙️ 0.7 multiplier, and its register says "Registered options are watched, never scored". It does not say whether a 🎙️-only category scores at 0.7 or registers at 0. The stage registered H2 and C1 at 0. Scoring both at LM x 0.7 gives about 6.6 (recomputed), NONE unchanged.
- FG-4. prompts/07 evidence_mix says "item counts" without a scope (all sections, or scored categories only) or a unit (row or tag). This is the root of F6.
- FG-5. prompts/12 line 379, the B12c template, holds the non-YAML placeholder "(same line, comment "# rule 9; any fail = REWORK stage 13")". It is an artifact of audit item VER-08 (audits/PROMPT_AUDIT_2026-10.md line 1962). The intended line is the business_understanding_narrative map with the rule 9 comment. I emitted that line, with PENDING values.

## ROUTED TO VERIFIER A (numbers; not scored here)

- RA-1. B07 Section 3 F2, "Positive" paragraph: "operating profit of ₹7 to ₹15 Cr a quarter" for the four quarters from Q3 FY26. B01-gate0.yaml analyst_note gives Q3 FY26 operating profit 4.15 Cr (4.15 + 15.30 + 7.34 + 8.80 = 35.59). B07 6D "Operating margin is 9 to 10%": on B01's quarterly figures the quarters run 5.1% to 16.4% (recomputed); 9.9% is the four-quarter average (35.59 / 358.33).
- RA-2. B01 raw series table header "PBT=PAT", while FY17 shows PBT -54.19 and PAT -79.52. A3 and B1 use PAT. Scores hold either way.
- RA-3. B07 Section 0 row 4c, "about 18 months tenure" (F5).

## VALUATION AUDIT: PENDING PHASE 3

Rules 4, 5, 7 and 11 to 15 were not run. B10 and B11 are absent. The valuation, expectation_ledger and business_understanding_narrative fields in the block hold template defaults with empty fails lists. They are not findings.

```yaml
stage: B12c
company: "WALCHANNAG"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete  # PHASE 1 scope: Gate 0 (B01) + Emerging Moat (B07) only; valuation half deferred to phase 3
gate0: {rules_checked: 48, fails: ["G02 ROCE proxy EBIT/(Equity+Reserves+Borrowings) substituted for fixed EBIT/(TA-CL); A1 0, A2 0, A4 5 proven on bound ROCE <= EBIT/NW (median bound 9.39%); scores unchanged (MINOR)", "G12 B4 zeroed as NOT FOUND while B2/B3 used the FY24-FY26 window; on the available window B4 1, Block B 1, core 11; AVOID and deal-breakers unchanged (MINOR)", "G33 M6 tier labels inverted and R&D/Rev input not stated; tier 1 is the peer-dependent tier and fails on R&D 0.00% per B07; score 0 unchanged (MINOR)", "G45 report fenced YAML is a pointer stub (input_gaps, data_notes, analyst_note, deal_breakers without years); B01-gate0.yaml complete (MINOR)"]}
emoat: {rules_checked: 36, fails: ["E03 Section 0 row 4c 'about 18 months tenure' left in body after the erratum declared it unsourced (MINOR)", "E32 evidence_mix claim 9 / inference 3 undercount the report's own tags (about 15 claim tags in Sections 3-4); counting basis unstated (MINOR)", "E35 Reading B 14.2 rests on a double credit plus three claim-as-documented tier upgrades; legal generous bound 9.0-10.3 NONE; FLAG-EM misstates the condition (12.1 without the double credit) (MINOR)"]}
valuation: {rules_checked: 0, fails: []}  # PENDING phase 3: B10/B11 absent, not run
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; any fail = REWORK stage 11; PENDING phase 3, template defaults, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 9; any fail = REWORK stage 13; PENDING (stage 13 not run), template defaults, not findings
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B01 Block A; B01-gate0.yaml data_notes ROCE line", rule: "prompts/01 FORMULA DEFINITIONS: ROCE = EBIT / (TA - CL), fixed", stage_value: "proxy EBIT / (Equity + Reserves + Borrowings); A1 0, A2 0, A4 5", recomputed: "fixed-formula bound ROCE <= EBIT/NW: median bound 9.39% (A1 0), FY25 -8.64% (A2 0), FY17 <= 4.35% < FY26 5.75% (A4 5); Block A 5 unchanged", note: "method deviation, disclosed with AR cross-check; no score effect"}
  - {severity: "MINOR", location: "B01 Block B, B4; B01-gate0.yaml data_notes B4 line", rule: "op. rule 6 use whatever history is available; op. rule 5 NOT FOUND = 0", stage_value: "B4 0 (FY17 payables NOT FOUND); sensitivity +8.5 days stated", recomputed: "available-window reading: B4 1, Block B 1, core 11; strict-window reading: B4 0 as scored", note: "three treatments of one FY17-FY23 data gap (A4 proxy, B2/B3 narrowed window, B4 NOT FOUND); classification AVOID unchanged"}
  - {severity: "MINOR", location: "B01 Block F, M6; B01-gate0.yaml data_notes PEER DATA NEEDED line", rule: "M6 tiers; op. rule 3 show every number", stage_value: "'EBITDA 5.36% fails lower tiers; top tier PEER DATA NEEDED' = 0", recomputed: "tiers 5 and 3 fail on EBITDA margin; tier 1 is peer-dependent and fails on R&D 0.00% (B07 A2, AR 2026 p.51); score 0", note: "presentational; R&D/Rev input missing from B01"}
  - {severity: "MINOR", location: "B01 report fenced YAML block", rule: "prompts/01 OUTPUT: end with exactly this fenced YAML block", stage_value: "pointer stubs; deal_breakers without years", recomputed: "n/a; B01-gate0.yaml holds the full block", note: "report text says years are in the YAML block; they are only in the block file"}
  - {severity: "MINOR", location: "B07 Section 0 row 4c", rule: "prompts/07 op. rule 3 source anchors on every evidence item", stage_value: "'About 18 months tenure at most'", recomputed: "strike; CFO hire date NOT FOUND per the header erratum", note: "erratum declared, body not corrected; no score effect"}
  - {severity: "MINOR", location: "B07 Section 3 recount line; B07-emoat.yaml evidence_mix", rule: "prompts/07 evidence_mix item counts", stage_value: "documented 8, claim 9, inference 3", recomputed: "about 15 claim tags in Sections 3-4 (A1 3, A3 2, B2 1, F2 2, H2 1, R1 6); inference tags in Sections 0-2 exceed 3", note: "basis unstated; stated mix reads more documented than the report"}
  - {severity: "MINOR", location: "B07 Section 5 two readings; B07-emoat.yaml FLAG-EM and analyst_note", rule: "single-credit rule; verifier rule 3 evidence tiers", stage_value: "Reading B 14.2 MODEST, 'needs a double credit of A1 and B2 plus a credit on F2'", recomputed: "without double credit 12.1; legal tiers and no double credit 9.7 (range 9.0-10.3), NONE", note: "adopted 5.2 NONE stands; flag understates what Reading B needs"}
critical_count: 0
major_count: 0
minor_count: 7
acceptance_rate: 91.7             # rules passed / rules checked, %: 77 / 84 (gate0 44/48, emoat 33/36); valuation pending
```
