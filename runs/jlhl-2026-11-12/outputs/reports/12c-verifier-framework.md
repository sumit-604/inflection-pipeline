# VERIFIER C (B12c): FRAMEWORK ADHERENCE, PHASE 1 SCOPE

JLHL (Jupiter Life Line Hospitals Ltd), run 2026-11-12. Model claude-opus-5-5, fresh context.

## Scope and inputs

- Scope: phase 1 only. This run audits Gate 0 (B01) and Emerging Moat (B07) compliance. The valuation audit (B10, B11; prompts/12 rules 4 to 7 and 11 to 15) does not run here, and neither do the narrative check (rule 9) or the dossier check (rule 10). Stages 10, 11 and 13 have not run. The valuation section of B12c is PENDING PHASE 3.
- Rule sources read: prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md. Master, the Section 1B layers and FTTCP are not loaded in phase-1 scope (prompts/12 L224-230).
- Artifacts read: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml. Each block matches the YAML at the end of its report, field for field.
- Not read: source PDFs, other verifier outputs, stage reasoning. Verifier A owns the question of whether a number exists in the source. This audit takes each input as the stage states it and re-derives the score from that input with the written threshold.
- Anchor key: "B01 L__" and "B07 L__" are line numbers in outputs/reports/01-gate0.md and outputs/reports/07-emoat.md. "P01 L__" and "P07 L__" are line numbers in prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.

## Result

- Rules checked: 72 (Gate 0: 48, Emerging Moat: 24). PASS 68. FAIL 4: CRITICAL 0, MAJOR 2, MINOR 2.
- Acceptance rate: 94.4% (68 of 72). Gate 0 is 95.8% (46 of 48). Emerging Moat is 91.7% (22 of 24). The REWORK threshold (below 60% on a denominator of 4 or more) is not met.
- The Gate 0 classification is GOOD on every reading. The recomputed core score is 68, not 71 (C-01). The matrix cell stays at Core 60-79 + STRONG = GOOD+, and deal-breaker 2 caps it to GOOD.
- The Emerging Moat band is MODEST on the recompute: 13.9, not 13.6 (C-04). The band depends on a multiplier convention the rubric does not state. On the other reading the total is 11.1, which is NONE. The operator must rule on the convention (C-04, Section F).
- B07 gives capex_embedded_growth_pct as 177. The rule counts only capex under execution. The recomputed figure is 62 (C-02).

## A. GATE 0 (B01) COMPLIANCE

| # | Rule (source) | B01 states | Re-derived from B01 inputs | Result |
| --- | --- | --- | --- | --- |
| G01 | Opening line; scoring adapted to the history (P01 L23-25) | "Data available: 7 years (FY20 to FY26). Scoring adapted to 7-year history" (B01 L3) | Present in the required form | PASS |
| G02 | Data confidence tier; downgrade only at 3-4 years (P01 L142-144) | Moderate, no downgrade (B01 L3) | 7 years is the 7-9 band: moderate, no downgrade | PASS |
| G03 | ROCE = EBIT / (Total Assets - Current Liabilities), "fixed, do not substitute alternatives" (P01 L27-31) | EBIT / (Total assets - Other Liabilities), i.e. equity + borrowings incl. leases, all 7 years; "computed" stated (B01 L18) | Fixed basis shown for FY26 only: 13.82% vs 13.77% (B01 L29). FY21-FY25 NOT RECOMPUTABLE from B01 inputs | FAIL, MINOR (C-03) |
| G04 | ROE = PAT / average net worth; FY20 closing basis stated (P01 L32-33) | 7 values; FY20 on closing (B01 L31-32) | All 7 recompute to 0.01pp, e.g. FY25 193.20 / avg(1,169.04, 1,356.25) = 15.30% (B01 L31, L44) | PASS |
| G05 | WC days = receivable + inventory - payable days; basis stated (P01 L34-38) | Revenue basis for all legs, stated (B01 L57) | 6 rows recompute, e.g. FY21 16.40 + 9.80 - 43.97 = -17.77; FY26 18.38 + 9.33 - 23.25 = +4.46 (B01 L61, L66) | PASS |
| G06 | FCF = CFO - capex (PPE + intangibles, excluding acquisitions) (P01 L39-40) | Capex incl. CWIP and intangibles, excl. acquisitions (B01 L46) | 6 FCF values recompute exactly, e.g. FY26 267.71 - 501.85 = -234.14 (B01 L43, L52, L55) | PASS |
| G07 | CAGR = (End / Start)^(1/years) - 1 (P01 L41) | 6-year windows (B01 L80-81) | Revenue (1,499.79 / 462.95)^(1/6) - 1 = 21.64%; PAT (194.01 / 29.63)^(1/6) - 1 = 36.78%. B01 shows 21.65% and 36.77%: rounding, same bands | PASS |
| G08 | CAGR edge rules (P01 L43-50) | Both endpoints positive; FY21 loss shown as an intermediate year in data_notes; no synthetic CAGR (B01 L81, L184) | The edge rules key to the endpoints. The swing note is "additional" to the N/M case, and the "no synthetic CAGR" clause only bites when the CAGR is N/M. C4 is computed because PAT CAGR is not N/M | PASS |
| G09 | A1 median ROCE (P01 L55) | 15.35% = 3 (B01 L36) | Median of 7 = 4th sorted value, 15.35% (FY22); band 15-19.9 = 3 | PASS |
| G10 | A2 minimum ROCE (P01 L56) | 6.10% = 0 (B01 L37) | FY21 6.10% is below 8 = 0 | PASS |
| G11 | A3 median ROE (P01 L57) | 15.30% = 4 (B01 L38) | Sorted -0.97, 12.52, 13.38, 15.30, 19.20, 22.12, 23.01; median 15.30%; band 15-19.9 = 4 | PASS |
| G12 | A4 ROCE trend, latest vs earliest (P01 L58-59) | 13.77% vs 11.52% = 5 (B01 L39) | +2.25pp; latest >= earliest = 5 | PASS |
| G13 | B1 cumulative CFO / cumulative PAT (P01 L62-63) | 1.62 = 5 (B01 L71) | 1,159.96 / 715.19 = 1.622; >= 1.00 = 5 | PASS |
| G14 | B2 FCF-positive years (P01 L64) | 3 of 6 = 50% = 2 (B01 L72) | FY22, FY23, FY24 positive. 50% sits in 50-74 = 2. Window FY21-FY26 because FY20 capex is NOT FOUND (see O-2) | PASS |
| G15 | B3 cumulative FCF / cumulative PAT (P01 L65-66) | Negative = 0 (B01 L73) | -239.55 / 685.56. The PAT denominator matches the FCF window (715.19 - 29.63 = 685.56). Negative = 0 | PASS |
| G16 | B4 change in WC days (P01 L67-68) | +22.2 days = 0 (B01 L74) | -17.77 (FY21) to +4.46 (FY26) = +22.23; increased > 15 = 0 | PASS |
| G17 | C1 revenue CAGR (P01 L71) | 21.65% = 5 (B01 L80) | 21.64%; >= 20 = 5 | PASS |
| G18 | C2 PAT CAGR (P01 L72) | 36.77% = 5 (B01 L81) | 36.78%; >= 20 = 5 | PASS |
| G19 | C3 positive YoY revenue years (P01 L73) | 6 of 6 = 5 (B01 L82) | 100% = 5 | PASS |
| G20 | C4 PAT CAGR minus revenue CAGR (P01 L74) | +15.1pp = 5 (B01 L83) | 36.78 - 21.64 = +15.1pp; >= +3 = 5 | PASS |
| G21 | D1 net debt / EBITDA (P01 L77-79) | 1.53x = 3 (B01 L91) | (584.24 - 58.17) / 343.44 = 1.532x; 1-2x = 3. P01 does not define net debt (see O-1) | PASS |
| G22 | D2 EBIT / interest (P01 L80-82) | 8.97x = 4 (B01 L92) | 293.10 / 32.66 = 8.97x; 5-9.9 = 4 | PASS |
| G23 | D3 debt / equity (P01 L83-84) | 0.38 = 4 (B01 L93) | 584.24 / 1,544.09 = 0.378; 0.1-0.5 = 4 | PASS |
| G24 | D4 current ratio (P01 L85-86) | 3.02 = 5 (B01 L94) | 6,849.00 / 2,265.75 = 3.02; >= 2.0 = 5 | PASS |
| G25 | E1 promoter holding (P01 L89-90) | 40.91% = 3 (B01 L100) | Band 40-49.9 = 3 | PASS |
| G26 | E2 promoter change over 3 years; a NOT FOUND data point scores 0 (P01 L91-92, L19-22) | 3, "scored on observed flat holding" over Mar-2025 to Sep-2026; "The 3-year-ago point is NOT FOUND on a like basis" (B01 L101) | 0. By B01's own statement the 3-year data point is NOT FOUND | FAIL, MAJOR (C-01) |
| G27 | E3 promoter pledge (P01 L93) | 0% = 5 (B01 L102) | 0% = 5 | PASS |
| G28 | E4 contingent liabilities / net worth (P01 L94-95) | 0.32% = 5 (B01 L103) | 49.26 / 15,440.93 Mn = 0.32%; < 5% = 5 | PASS |
| G29 | Block sums, core, grand total (P01 L54-95; B01 YAML) | A 12, B 7, C 20, D 16, E 16; core 71; grand total 94 (B01 L107, L142) | Sums are correct on B01's scores. With G26 fixed: E 13, core 68, grand total 91 | PASS (arithmetic) |
| G30 | M1 pricing power (P01 L102-104) | +4.67pp, CAGR 21.65% = 5 (B01 L115) | 22.90 - 18.23 = +4.67pp (>= 2) and CAGR >= 10 = 5 | PASS |
| G31 | M2 cost advantage vs peer median (P01 L105-106) | +1.81pp = 1 (B01 L116) | Median of 20.87, 21.09, 25.25 = 21.09% (B01 L111); 22.90 - 21.09 = +1.81pp, inside +/-2 = 1 | PASS |
| G32 | M3 capital efficiency (P01 L107-108) | FAT 1.08x, ROCE 13.77% = 1 (B01 L117) | FAT > 1x and ROCE > 12% = 1 | PASS |
| G33 | M4 customer stickiness (P01 L109-111) | 3 (B01 L118) | Zero decline years. Receivable days moved -16.8, outside the literal +/-10, so the 5 tier fails. "Max 1 decline year" holds = 3 | PASS |
| G34 | M5 scale and dominance; PEER DATA NEEDED rule (P01 L99-100, L112-113) | 0, PEER DATA NEEDED (B01 L119) | The full listed segment is not in the inputs: 0 with PEER DATA NEEDED, as P01 L99-100 directs | PASS |
| G35 | M6 technology / R&D (P01 L114-116) | NOT FOUND = 0 (B01 L120) | 0 | PASS |
| G36 | M7 regulatory / licence (P01 L117-119) | 0, PEER DATA NEEDED (B01 L121) | Listed-player count not in the inputs: 0 | PASS |
| G37 | M8 distribution (P01 L120-122) | Beds +18.7%, CAGR 21.65% = 3 (B01 L122) | Network growing and CAGR >= 15% = 3. Revenue per outlet is absent, so the 5 tier fails | PASS |
| G38 | M9 brand, proxy stated (P01 L123-125) | +1.86pp = 1 (B01 L123) | (80.57 + 77.40) / 2 = 78.99%; JLHL 80.85% is +1.86pp. No tier fits literally; 1 is the natural fill. The score holds for any KIMS value (see O-3) | PASS |
| G39 | M10 switching costs (P01 L126-128) | 5 (B01 L124) | Revenue grew every year. Receivable days fell, which meets "rose <= 10 days" = 5 | PASS |
| G40 | M11 network effects, two-window test (P01 L129-133) | 1 (B01 L125) | 7 years (>= 6), two windows: FY23-26 18.9% < FY20-23 24.5%; selling and admin % rose 26.84 to 28.55; growth > 15% = 1 | PASS |
| G41 | M12 negative WC / float (P01 L134-135) | 3 (B01 L126) | Negative in 3 of 6 years, not a majority, so the 5 tier fails. All six are <= 15 days = 3 (gap fill, see O-3) | PASS |
| G42 | Moat total, count, class (P01 L98-99, L137-138) | 23; 5 present; STRONG (B01 L127) | 5+1+1+3+0+0+0+3+1+5+1+3 = 23. Scores >= 3: M1, M4, M8, M10, M12 = 5. Band 4-5 = STRONG | PASS |
| G43 | Classification matrix (P01 L146-149) | Core 71 + STRONG = GOOD+ (B01 L138) | Core 60-79 + STRONG = GOOD+. Recomputed core 68 gives the same cell | PASS |
| G44 | Deal-breakers 1-9; the driving years stated (P01 L151-159) | #2 fires (Block B 7); FY25, FY26 and the WC drift named; #1 and #3-#9 tested and clear (B01 L139-140) | All nine re-tested on B01 inputs. Only #2 fires | PASS |
| G45 | Final classification after caps (P01 L151-155) | GOOD (B01 L142) | GOOD+ capped by #2 to max GOOD = GOOD | PASS |
| G46 | FLAG-GATE0 only at or below AVERAGE (P01 L175-177) | flags: [] (B01 L168) | GOOD is above AVERAGE. No flag is due | PASS |
| G47 | YAML block: all fields; data_notes carry swings, proxies, PEER DATA NEEDED; block_b_trend carries its number; analyst_note <= 200 words (P01 L168-198) | Complete (B01 L155-195) | All fields present. analyst_note is about 120 words | PASS |
| G48 | Dashboard elements (P01 L163-166) | Blocks, line items, profile bars, classification box, strongest/weakest, final line (B01 L17-143) | Present. The moat bar is one aggregate bar (see O-8) | PASS |

## B. EMERGING MOAT (B07) COMPLIANCE

| # | Rule (source) | B07 states | Re-derived | Result |
| --- | --- | --- | --- | --- |
| E01 | Six sections and the optionality register in one response (P07 L28, L48-210) | Sections 1-6 and the register (B07 L20-342) | All present | PASS |
| E02 | Each of 22 categories: evidence, or NO EVIDENCE FOUND; no force-fit (P07 L39-40, L65-67) | 12 rows NO EVIDENCE FOUND (A1, A2, A4, B3, C1, C2, D1, D2, E2, G2, H1, H2); 8 with evidence; I1 and I2 scored 0 with reasons (B07 L111-171) | 22 of 22 addressed | PASS |
| E03 | R1 in Section 4: 4A, 4B, 4C (P07 L161-168) | Present (B07 L207-228) | All three parts present | PASS |
| E04 | A taxonomy mark and an anchor on each evidence item (P07 L29-36) | Marks and anchors through Sections 1-4 | Present on the scored items | PASS |
| E05 | Section 3 summary: 22 rows with evidence, type, strength, time (P07 L155-157) | 22 rows (B07 L175-198) | Complete | PASS |
| E06 | Strong/Moderate count stated (P07 L157-158) | 2: E1, F2 (B07 L200) | Matches the table | PASS |
| E07 | Completionist guard and the 📄 recount line (P07 L41-46, L158-159) | 9 of 23 rows active, below the 12 trigger; recount itemised (B07 L202; YAML completionist_recount) | Itemised list: F2 2 + E1 3 + R1 1 + G1 2 + B1 1 + B2 1 + H3 1 + F1 1 = 12 items in 8 categories | PASS |
| E08 | Scorecard, all 23 rows (P07 L171-174) | 23 rows (B07 L234-258) | Complete | PASS |
| E09 | Likelihood x impact matrix values (P07 L171-172) | 9 scored rows (B07 L238-258) | A3 ML 1, B1 ML 1, B2 HL 2, E1 HM 3, F1 MM 2, F2 MM 2, G1 ML 1, H3 ML 1, R1 HL 2; 14 rows 0. All match the matrix | PASS |
| E10 | Evidence multiplier applied on one basis (P07 L172-174; prompts/12 L241-244) | B1 at 0.7 on the claimed benefit; E1 and R1 at 1.0 on the documented fact (B07 L240, L247, L258) | B1 at 1.0 on the basis B07 uses for E1 and R1; total 13.9 | FAIL, MINOR (C-04) |
| E11 | No 🎙️-only or 🔍-only row scored as 📄 (prompts/12 L243-244) | F1 🎙️ 0.7; A3 🔍 0.5 (B07 L238, L249) | Neither row is graded up | PASS |
| E12 | Adjusted total (P07 L174) | 13.6 (B07 L261) | 0.5 + 0.7 + 2.0 + 3.0 + 1.4 + 2.0 + 1.0 + 1.0 + 2.0 = 13.6 | PASS |
| E13 | I1/I2 contribution stated separately (P07 L180-181) | 0.0 (B07 L260) | Stated | PASS |
| E14 | Band (P07 L175-176) | 13.6 = MODEST (B07 L263) | Band 12-24 = MODEST. Recomputed 13.9 = MODEST | PASS |
| E15 | Category 21 (I1) present; above 0 only with both legs and a 📄 source on leg (b) (P07 L122-138; prompts/12 L292-295) | 0. Leg (a) not evidenced; leg (b) contradicted by the CEO (B07 L170) | 0 is the only score the rule allows on this evidence | PASS |
| E16 | Category 22 (I2) present; above 0 only with a named, specific sacrifice (P07 L139-153; prompts/12 L295-297) | 0. The answer to "what must it destroy" is "nothing" (B07 L171) | P07 L149-150 scores that answer 0 | PASS |
| E17 | 2C: capex under execution x historical FAT, as % above current revenue, arithmetic shown (P07 L59-62) | 2,129 Cr (Pune South, Mira Road, BKC, Thane) x 1.245 = 2,650 Cr = 177% (B07 L92-94) | Only Pune South is under execution (B07 L64-67, L100): 750 x 1.245 = 933.8 Cr = 62.3% | FAIL, MAJOR (C-02) |
| E18 | Optionality register: table and YAML, four fields per row (P07 L183-196) | 9 rows in both places (B07 L271-281; YAML) | Complete | PASS |
| E19 | 6C uses the injected Gate 0 block (P07 L202-203) | Core 71, moat 23 STRONG with 5, GOOD (B07 L306-312) | Matches B01. It updates to core 68 if C-01 is applied | PASS |
| E20 | 6D: HIGH POTENTIAL and TURNAROUND rows get full reasoning (P07 L203-208) | Both rows reasoned and failed with numbers (B07 L319-320) | Reasoning present. The mapping itself cannot be checked (see O-7) | PASS |
| E21 | YAML block: all fields; active_categories Strong/Moderate only; em_classification in the enum; analyst_note <= 200 words (P07 L216-243) | Complete (B07 L344-396) | E1 and F2 only; "MODEST" is in the enum; analyst_note is about 115 words | PASS |
| E22 | Section 1: 1A with status and evidence type, 1B, 1C (P07 L49-55) | Present (B07 L22-54) | Present. Two 1A labels fall outside the P07 set (see O-6) | PASS |
| E23 | Section 2: 2A table, 2B per facility, 2D (P07 L57-63) | Present (B07 L58-107) | Present | PASS |
| E24 | Section 6: 6A four windows, 6B, 6E map, 12-month catalysts, biggest risk (P07 L199-210) | Present (B07 L285-340) | Present | PASS |

## C. FINDINGS

### C-01. MAJOR. Gate 0 E2 is scored on a window the rule does not allow

- Rule. E2 is "Promoter holding change over 3 years" (P01 L91-92). P01 L19-22: "If a data point is not available, mark it 'NOT FOUND' and score it 0." P01 L23-25 sets 3 years as the minimum history.
- What B01 did. It scored E2 = 3 "on observed flat holding", 40.91% at 31-Mar-2025 and 40.91% at 30-Sep-2026, an 18-month window. It also states: "The 3-year-ago point is NOT FOUND on a like basis" (B01 L101). The input gap repeats this (B01 L163).
- Recomputed. E2 = 0. Block E 16 to 13. Core 71 to 68. Grand total 94 to 91.
- Decision effect. None. Core 68 sits in the same 60-79 band. STRONG gives GOOD+, and deal-breaker 2 caps it to GOOD.
- Two readings. Reading A: the RHP pre-offer figure (40.69%, three promoter entities, Aug-2023) is usable. It gives +0.22pp, inside +/-1, so E2 = 3. B01 rejected that figure because it is pre-offer and covers fewer entities than the promoter group. That objection holds. Reading B: no like-basis point exists, so the rule gives 0.
- Separating observation. Find the promoter and promoter group holding in the shareholding pattern for the quarter ended 30-Sep-2023, the first quarter after listing (NSE/BSE filing). Let that value be X%. If X is 39.91% or below, E2 = 5. Between 39.91% and 41.91%, E2 = 3 and core 71 returns. From 41.91% to 43.91%, E2 = 1. Above 43.91%, E2 = 0.
- Downstream. B07 6C and combined_reasoning quote core 71 (B07 L308, L388). They change to 68. No classification changes.

### C-02. MAJOR. 2C counts capex that is not under execution

- Rule. 2C is "total capex under execution x historical fixed asset turnover = implied incremental revenue, expressed as % above current revenue" (P07 L59-62).
- What B07 did. It counted 2,129 Cr: Pune South 750, Mira Road 400, BKC 954 and Thane 25 (B07 L92). Its own 2A status column gives Pune South "Under construction", Mira Road "Regulatory stage", BKC "Lease accepted, registration pending" and Thane "LOI received" (B07 L64-67). Its own read says: "Only Pune South (about 35% of the counted capex) is under construction today" (B07 L100). The YAML field then carries 177 (B07 L376).
- Recomputed. Pune South 750 Cr x 1.245 (B07 L90) = 933.8 Cr. On the FY26 total income of 1,499.8 Cr (B07 L94) that is 62.3%. The range runs from 49.8% (Pune South build only, 600 Cr, land out) to 64.3% (Thane's 25 Cr added). B07's own bed-day method on Pune South's 500 beds gives 500 x 84.4% x 365 x 64.8% x Rs 71,800 = 716.6 Cr, or 47.8% (inputs from B07 L98).
- Decision effect. None in phase 1. The YAML headline is about 2.8 times the rule's figure. Stage 11 or stage 13 could read 177% as embedded capacity growth on a CAPACITY revenue basis. 177% is the announced-pipeline figure. It can stay as a labelled pipeline line beside 62%.
- Confirming observation. Mira Road, BKC and Thane each enter the 2C count when construction starts. A Reg 30 filing or a concall statement of construction start will show it.
- Downstream. FLAG-GROWTH-IS-CAPACITY (B07 L357) quotes "115% to 177%". On the rule's basis that is 48% to 62% under execution, with 115% to 177% for the full pipeline.

### C-03. MINOR. ROCE uses a substitute denominator

- Rule. "ROCE = EBIT / (Total Assets - Current Liabilities)" under "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" (P01 L27-31).
- What B01 did. It used Total assets - Other Liabilities, which equals equity + borrowings incl. leases, for all seven years. The reason given is that the screener Data_Sheet does not split current liabilities (B01 L18). B01 disclosed the substitution and cross-checked FY26 on the fixed basis: 13.82% vs 13.77% (B01 L29).
- Why it is a FAIL. The split exists in documents B01 already used for payables: RHP p.75 (FY21-FY23), the AR 2025 balance sheet (FY24) and AR 2026 p.191 (FY25, FY26) (B01 L57). Only FY20 lacks a fixed-basis figure.
- Recomputed. NOT RECOMPUTABLE from B01's stated inputs for FY21-FY25. FY26 on the fixed basis is 13.82%, the same band.
- Band risk. The A1 median is FY22 at 15.35% (B01 L36), 0.35pp above the 15% boundary. If FY22 capital employed on the fixed basis is above 807.1 Cr (B01 basis 788.81 Cr), FY22 falls below 15.0%. A1 then moves from 3 to 1, Block A to 10, and core loses 2. A2 moves only if FY21 capital employed falls below 506.6 Cr (B01 basis 664.51 Cr). A4 moves only if the earliest year rises above the latest.
- Decision effect. None. The worst case with C-01 is core 66, still in 60-79.
- Confirming observation. FY22 total assets less current liabilities from the RHP restated balance sheet. A value at or below 807.1 Cr keeps A1 = 3.

### C-04. MINOR. The evidence multiplier is applied on two bases

- Rule. "Multiply by evidence quality (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x)" (P07 L172-174). Verifier check: "evidence multipliers applied correctly; ... scores consistent with the stated evidence tiers" (prompts/12 L241-244).
- What B07 did. E1 and R1 take 1.0 on the documented indicator fact: the land bank (BKC lease, Pune South land, freehold sites) and the Thane LOI (B07 L247, L258). B07's own inference list names the advantage readings of both rows as 🔍: "micro-market scarcity as first-mover edge (E1)" and "bed-licence scarcity (R1)" (B07 L205). B1 takes 0.7 on the claimed margin benefit (B07 L240), although its indicator fact is documented: the IV plant was acquired, with goodwill of Rs Cr 5.1 (B07 L118). "Captive sources" is the first item on the B1 list (P07 L78-79).
- Recomputed on the basis B07 uses for most rows (the fact basis): B1 = 1 x 1.0 = 1.0. The total is 13.9, still MODEST.
- Two readings of the rubric. Fact basis: the multiplier grades the evidence piece. The total is 13.9, MODEST. Advantage basis: the multiplier grades the evidence for the advantage. E1 and R1 then go to 0.5, and the total is 13.6 - 1.5 - 1.0 = 11.1, which is NONE. It is 10.5 if B2's entry-gate effect, which rests on a call statement (B07 L119), is also graded 🎙️.
- Which reading the text supports. The taxonomy applies "to every single piece of evidence" (P07 L29). 📄 is defined by facts such as "contract signed" and "plant under construction" (P07 L30-32). Both support the fact basis. The rubric does not say this outright.
- Decision effect. None on the fact basis. On the advantage basis the band flips from MODEST to NONE, which changes the Pillar 3 EM input at stage 11.
- Separating item. An operator ruling on what the multiplier grades. No market observation separates the two readings.

## D. SENSITIVITY OF THE TWO CLASSIFICATIONS

Gate 0 core (all cells are 60-79 + STRONG = GOOD+, capped to GOOD by deal-breaker 2):

| Reading | Core | Classification |
| --- | --- | --- |
| Reported (B01 L107) | 71 | GOOD |
| C-01 applied (E2 = 0) | 68 | GOOD |
| C-01 + C-03 worst case (A1 = 1) | 66 | GOOD |
| C-01 + O-1 (D1 = 4 with liquid investments netted) | 69 | GOOD |

Emerging Moat total (bands: >= 12 MODEST, < 12 NONE; P07 L175-176):

| Reading | Total | Band |
| --- | --- | --- |
| Reported (B07 L261) | 13.6 | MODEST |
| C-04 recompute (B1 at 📄) | 13.9 | MODEST |
| C-04 + O-5 (F1 at LM = 1) | 13.2 | MODEST |
| B07 own fragility test: remove B2 or R1 (B07 L355) | 11.6 (11.9 with C-04) | NONE |
| Advantage basis (E1, R1 at 🔍) | 11.1 | NONE |

B07's FLAG-THRESHOLD-FRAGILE (B07 L355) stands and is correctly computed. C-04 adds a second route below the floor. That route is a rubric reading, not a fact.

## E. OBSERVATIONS (no FAIL)

- O-1. D1 net debt basis. P01 L77 does not define net debt. B01 netted cash and bank only: 1.53x, score 3 (B01 L91). With the 485.8 Cr of liquid current investments netted it is 0.12x, score 4 (B01 L91, L187). On management's ex-lease basis, Mar-26 shows net cash of about Rs 45 Cr (B07 L161), which would score 5. Core moves +1 or +2. Classification does not change. B01 disclosed both bases, so the rule as written is met.
- O-2. B2 window. FY20 capex is NOT FOUND, so B01 scored FY21-FY26 (B01 L53, L72). P01 L23-25 supports using the available window. If the FY20 gap were counted as a non-positive year, the rate would be 3 of 7 = 42.9%, score 0, and Block B would be 5. Block B is already below 8, so classification does not change.
- O-3. Tier gaps in P01. M9: a gross margin above the peer median by less than 5pp, with growth of 8% or more, fits no tier literally. B01 gave 1. M12: a mix of negative and 0-15 day years fits no tier literally. B01 gave 3. Both fills are the natural reading. M9 also holds whatever the missing KIMS figure is. A three-peer median cannot exceed 80.57% or fall below 77.40%, so JLHL's 80.85% is always above the median and always less than 5pp above it (B01 L123).
- O-4. M4 and M10 read falling receivable days in opposite directions. M4's "stable +/-10" fails on -16.8 days. M10's "rose <= 10" passes on it (B01 L118, L124). Both follow the text literally. B01 flags M10 as arithmetic (B01 L191).
- O-5. F1 likelihood. F1's positive leg is 🎙️ only. Its documented items are adverse: 24.1% turnover and no ESOP (B07 L145). B07 rates it Weak but gives it MM = 2, the same raw score as F2, which B07 rates Moderate (B07 L190-191, L249-250). At LM = 1 the row is 0.7 and the total 12.9 (13.2 with C-04). The band does not change. This is a judgment, not a breach of a rule.
- O-6. Presentation. Section 3 uses evidence tables for E1 and F2 only. The weak rows use anchored bullets with tier marks (P07 L66-67). In 1A, "IN PROCESS" and "UNDER CONSTRUCTION" fall outside the P07 L50-51 status set (B07 L30, L34). 1C has no separate profitability-impact column (P07 L54-55). The content is present in each case.
- O-7. The 6D "standard matrix" is not defined in P07 (L202-208). B07 says so and maps on the label definitions (B07 L318). The mapping GOOD + MODEST = GOOD cannot be checked inside the phase-1 rule sources.
- O-8. The dashboard shows one aggregate moat bar (23/60, B01 L135). The per-test scores are in the table (B01 L113-126).
- O-9. I2 is answered once for the whole scan, not once per claimed moat (P07 L140). The answer covers both Moderate moats. For E1, a competitor "must destroy nothing" to build in the same micro-market. For F2, it is "execution lead, not configuration" (B07 L171). The score of 0 stands either way.

## F. ITEMS FOR THE OPERATOR (prompt and template defects, not findings against this run)

These are framework or prompt amendments. Under CLAUDE.md they travel on a separate branch and PR, never on this run's PR. This verifier changes no file outside the run folder.

1. prompts/12-verifiers-pipeline.md L379 holds patch-instruction text, "(same line, comment "# rule 9; any fail = REWORK stage 13")", where a YAML line belongs. audits/PROMPT_AUDIT_2026-10.md L1962-1964 (VER-08) shows the intended line: the business_understanding_narrative field with a rule 9 comment. The B12c block below emits that intended line.
2. prompts/01 L77: define net debt (whether liquid current investments and lease liabilities count). See O-1.
3. prompts/07 L172-174: state what the evidence multiplier grades (the indicator fact or the advantage reading). See C-04. For JLHL the band depends on it.
4. prompts/07 L202-208: put the 6D combined matrix in the stage file, or point to its source. See O-7.
5. prompts/01 L123-124 (M9) and L134-135 (M12): close the tier gaps. See O-3.

## G. RULES NOT RUN IN PHASE 1

- prompts/12 rule 4 (valuation, B11), rule 5 (valuation severity), rule 7 (method plurality), rules 11-14 (Role 1 exit construction, Amendment 19 FV path, Expectation Ledger, ledger gates), rule 15 (skill-to-source fidelity): stage 11 has not run. PENDING PHASE 3.
- Rule 6 (B09 downstream candidates and stage 11 catalyst citations): B09 is not among the phase-1 inputs, and the stage 11 half cannot run yet. PENDING PHASE 3.
- Rule 9 (Business Understanding Narrative): stage 13 has not run. PENDING /finalize.
- Rule 10 (B09b dossier): it fires at the /finalize verifier pass. The phase-1 structural check belongs to run-pipeline step 6b, not to this verifier.
- Rules 1, 2, 3 and 8 ran (tables A and B).

```yaml
stage: B12c
company: "JLHL"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase1"  # gate0 + emoat only; valuation, ledger and narrative pending
gate0:
  rules_checked: 48
  fails:
    - {rule: "G26 E2 promoter change over 3 years; NOT FOUND scores 0 (prompts/01 L91-92, L19-22)", severity: MAJOR, reported: 3, recomputed: 0, effect: "Block E 16 -> 13; core 71 -> 68; grand total 94 -> 91; classification GOOD unchanged"}
    - {rule: "G03 ROCE fixed formula EBIT / (TA - CL), no substitution (prompts/01 L27-31)", severity: MINOR, reported: "EBIT / (TA - other liabilities), FY20-FY26", recomputed: "NOT RECOMPUTABLE from B01 inputs for FY21-FY25; FY26 fixed basis 13.82%, same band", effect: "A1 median FY22 15.35% is 0.35pp over the 15% boundary; worst case A1 3 -> 1, core -2; classification unchanged"}
emoat:
  rules_checked: 24
  fails:
    - {rule: "E17 2C counts capex under execution only (prompts/07 L59-62)", severity: MAJOR, reported: 177, recomputed: 62, effect: "only Pune South (750 Cr) is under execution; 750 x 1.245 = 933.8 Cr = 62.3% of FY26 1,499.8 Cr; range 50-64; bed-day cross-check 48; 177 is the announced pipeline"}
    - {rule: "E10 evidence multiplier on one basis across rows (prompts/07 L172-174)", severity: MINOR, reported: "B1 at 0.7 on the claimed benefit while E1 and R1 take 1.0 on the documented fact; total 13.6", recomputed: "B1 at 1.0 (IV plant acquired, documented captive source); total 13.9, MODEST", effect: "band unchanged on the fact basis; advantage basis (E1, R1 at 0.5) gives 11.1, NONE; operator ruling needed"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}  # stages 10 and 11 not run; B10/B11 audit deferred
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; NOT CHECKED in phase 1 (stage 11 not run), defaults only; any fail = REWORK stage 11
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 9; NOT CHECKED in phase 1 (stage 13 not run), defaults only; any fail = REWORK stage 13
recomputed_destination_pe: ""  # blank: valuation out of phase-1 scope
recomputed_decision: ""        # blank: no decision exists in phase 1; Gate 0 GOOD and EM MODEST both stand on recompute
findings:
  - {id: "C-01", scope: gate0, severity: MAJOR, rule: "E2 promoter change over 3 years; NOT FOUND scores 0 (prompts/01 L91-92, L19-22)", claimed: "E2 = 3 on an 18-month window, Mar-2025 to Sep-2026; B01 itself calls the 3-year point NOT FOUND (B01 L101)", recomputed: "E2 = 0; Block E 13; core 68; grand total 91", decision_effect: "none: Core 60-79 + STRONG = GOOD+, capped to GOOD by deal-breaker 2", confirming_observation: "promoter group % in the 30-Sep-2023 shareholding pattern (first post-listing quarter): 39.91-41.91% restores E2 = 3 and core 71"}
  - {id: "C-02", scope: emoat, severity: MAJOR, rule: "2C counts capex under execution only (prompts/07 L59-62)", claimed: "capex_embedded_growth_pct 177 on 2,129 Cr: Pune South, Mira Road, BKC, Thane (B07 L92-94, L376)", recomputed: "62: Pune South 750 Cr x 1.245 = 933.8 Cr on FY26 1,499.8 Cr; range 50-64; bed-day cross-check 48", decision_effect: "none in phase 1; risk that stage 11 or 13 reads 177 as embedded capacity growth", confirming_observation: "construction start at Mira Road, BKC or Thane (Reg 30 or concall) adds that project to the 2C count"}
  - {id: "C-03", scope: gate0, severity: MINOR, rule: "ROCE fixed formula EBIT / (TA - CL), no substitution (prompts/01 L27-31)", claimed: "EBIT / (TA - other liabilities) for FY20-FY26 (B01 L18); CL split exists in RHP p.75, AR 2025, AR 2026 p.191 for FY21-FY26", recomputed: "NOT RECOMPUTABLE from B01 inputs for FY21-FY25; FY26 fixed basis 13.82%, same band (B01 L29)", decision_effect: "none; worst case A1 3 -> 1, core -2 (66 with C-01), GOOD unchanged", confirming_observation: "FY22 TA - CL from the RHP restated balance sheet: at or below 807.1 Cr keeps FY22 ROCE at or above 15.0% and A1 = 3"}
  - {id: "C-04", scope: emoat, severity: MINOR, rule: "evidence multiplier on one basis across rows (prompts/07 L172-174; prompts/12 L241-244)", claimed: "B1 at 0.7 on the claimed benefit; E1 and R1 at 1.0 on the documented fact although B07 L205 names their advantage readings as inference; total 13.6", recomputed: "B1 at 1.0 on the fact basis; total 13.9, MODEST", decision_effect: "none on the fact basis; advantage basis gives 11.1 (10.5 with B2 at 0.7), NONE, which changes the Pillar 3 EM input", confirming_observation: "operator ruling on what the multiplier grades (indicator fact or advantage reading); prompt gap at prompts/07 L172-174"}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 94.4             # 68 passed / 72 checked; gate0 46/48, emoat 22/24
```
