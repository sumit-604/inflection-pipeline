# VERIFIER C: FRAMEWORK ADHERENCE, CREDENT, run 2026-11-12 (PHASE 1 SCOPE)

Model: claude-opus-5-5 (.claude/agents/verifier-c-framework.md line 5, effort xhigh line 6).
Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10, B11) and Verifier C rules 4 to 7 and 9 to 15 are not run. They are pending phase 3 or the /finalize pass.

Inputs read:
- Rule sources: prompts/01-gate-0-pipeline.md; prompts/07-emerging-moat-pipeline.md; prompts/12-verifiers-pipeline.md (Verifier C section, lines 213 to 390).
- Artifacts: runs/credent-2026-11-12/outputs/reports/01-gate0.md; outputs/blocks/B01-gate0.yaml; outputs/reports/07-emoat.md; outputs/blocks/B07-emoat.yaml.

Verifier A owns the question of whether a number exists in the source. This audit takes each number as B01 or B07 states it. It re-derives the scores from those numbers with the stated thresholds. It does not test any number against a filing.

Anchor convention: "(01-gate0.md l.N)" is a line in the B01 report. "(07-emoat.md l.N)" is a line in the B07 report. "(B07 block l.N)" is a line in B07-emoat.yaml. "(rule src 01 l.N)" and "(rule src 07 l.N)" are lines in the two prompt files.

## SUMMARY

| Framework | Rules checked | PASS | FAIL | CRITICAL | MAJOR | MINOR | Stated result | Re-derived result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gate 0 (B01) | 47 | 45 | 2 | 0 | 0 | 2 | AVERAGE, core 72, moat 21, STRONG | AVERAGE, core 72, moat 21, STRONG (concur) |
| Emerging Moat (B07) | 28 | 21 | 7 | 0 | 0 | 7 | 10.5, NONE | 10.5, NONE (concur) |
| Total | 75 | 66 | 9 | 0 | 0 | 9 | | acceptance 88.0% |

No finding changes a score, a band, a classification or a decision. No REWORK trigger fires: zero CRITICAL, acceptance 88.0% on a denominator of 75, and categories 21 and 22 are present in B07.

## PART 1. GATE 0 (B01) COMPLIANCE

### 1.1 Rule-by-rule table

| ID | Rule (source) | B01 states | Re-derived from stated inputs | Result |
| --- | --- | --- | --- | --- |
| G01 | Open with data-available line (rule src 01 l.23-25) | "Data available: 3 years (FY24 to FY26). Scoring adapted to 3-year history." (01-gate0.md l.3) | present, wording as specified | PASS |
| G02 | Every extracted number carries an anchor (rule src 01 l.15-18) | most numbers anchored to RHP p.56-60, XBRL, presentation pages | M3 fixed-asset denominator 1,457.08 lakh has no anchor and is not in the base-data table (01-gate0.md l.72, l.8-25). "pre-IPO promoter holding 87.52% (RHP)" has no page (l.62) | FAIL, MINOR (finding G02) |
| G03 | NOT FOUND scored 0, no estimates, PEER DATA NEEDED (rule src 01 l.19-22, l.99-100) | M2, M5, M9 PEER DATA NEEDED = 0; M6 R&D NOT FOUND = 0; M11 selling expense NOT FOUND = 0 (l.71-80) | consistent, no fill found | PASS |
| G04 | ROCE = EBIT / (TA - CL); source figure first, else "computed" (rule src 01 l.29-31) | screener gives no ROCE; computed as (PBT + finance cost) / (TA - CL) (l.4, l.30) | FY24 411.83 / 1,579.46 = 26.07%; FY25 395.48 / 1,717.27 = 23.03%; FY26 2,597.44 / 5,093.75 = 50.99% (inputs l.10-17) | PASS |
| G05 | ROE = PAT / average net worth; closing-only stated (rule src 01 l.32-33) | FY24 closing only, stated (l.34) | FY24 266.44 / 1,365.60 = 19.51%; FY25 224.67 / 1,477.94 = 15.20%; FY26 1,844.78 / 2,984.67 = 61.81% | PASS |
| G06 | WC days formula, basis stated (rule src 01 l.34-38) | revenue basis, no inventory, no COGS, stated (l.43) | FY24 91.65 - 2.67 = 88.98; FY25 83.85 - 2.30 = 81.55; FY26 100.26 - 1.68 = 98.58 | PASS |
| G07 | FCF = CFO - purchases of PPE and intangibles, acquisitions excluded (rule src 01 l.39-40) | FY24 capex -1.06 "(inflow)", FY24 FCF 81.99 (l.24, l.40); acquisition outflow 1,084.01 excluded (l.40) | a purchase figure cannot be negative. The -1.06 line is net of disposals or mislabelled, and no proxy basis is stated. Gross FY24 purchases: NOT FOUND in B01 | FAIL, MINOR (finding G07); B2 and B3 unchanged |
| G08 | CAGR formula and edge rules (rule src 01 l.41-50) | 2-year window, endpoints positive, "No loss-to-profit swing" (l.47-51) | no endpoint is zero or negative; edge rules not triggered; C4 computable | PASS |
| G09 | A1 median ROCE (rule src 01 l.55) | 26.07% = 5 (l.32) | 26.07 >= 25 -> 5 | PASS |
| G10 | A2 minimum ROCE (l.56) | 23.03% = 5 (l.33) | 23.03 >= 15 -> 5 | PASS |
| G11 | A3 median ROE (l.57) | 19.51% = 4 (l.34) | 15 to 19.9 band -> 4 | PASS |
| G12 | A4 ROCE trend (l.58-59) | 50.99 >= 26.07 = 5 (l.35) | latest >= earliest -> 5 | PASS |
| G13 | B1 cumulative CFO / PAT (l.62-63) | -0.014 = 0 (l.39) | (80.93 + 548.10 - 662.34) / (266.44 + 224.67 + 1,844.78) = -33.31 / 2,335.89 = -0.014 -> <0.50 -> 0 | PASS |
| G14 | B2 FCF-positive years (l.64) | 1 of 3 = 0 (l.41) | 33% -> <50 -> 0. Holds on any FY24 gross capex (0 or 1 of 3) | PASS |
| G15 | B3 cumulative FCF / PAT (l.65-66) | -1,269.73, negative = 0 (l.42) | 81.99 - 138.03 - 1,213.69 = -1,269.73 -> 0 | PASS |
| G16 | B4 change in WC days (l.67-68) | +9.60 = 1 (l.43) | 98.58 - 88.98 = +9.60 -> increased 5 to 15 -> 1 | PASS |
| G17 | C1 revenue CAGR (l.71) | 68.2% = 5 (l.47) | (21,416.18 / 7,573.32)^0.5 - 1 = 68.2% -> 5 | PASS |
| G18 | C2 PAT CAGR (l.72) | 163.1% = 5 (l.48) | (1,844.78 / 266.44)^0.5 - 1 = 163.1% -> 5 | PASS |
| G19 | C3 positive YoY years (l.73) | 2 of 2 = 5 (l.49) | +2.9% and +174.8% -> 100% -> 5 | PASS |
| G20 | C4 PAT CAGR minus revenue CAGR (l.74) | +94.9pp = 5 (l.50) | 163.1 - 68.2 = +94.9pp -> 5 | PASS |
| G21 | D1 net debt / EBITDA (l.77-79) | 0.68x = 4 (l.54) | (2,194.75 - 221.02) / (2,459.29 + 138.15 + 310.55 - 26.55) = 1,973.73 / 2,881.44 = 0.68x -> 0 to 1.0x -> 4 | PASS |
| G22 | D2 interest coverage (l.80-82) | 18.80x = 5 (l.55) | 2,597.44 / 138.15 = 18.80x -> 5 | PASS |
| G23 | D3 debt / equity (l.83-84) | 0.501 = 3 (l.56) | 2,194.75 / 4,379.07 = 0.501, above the 0.5 line -> 0.5 to 1.0 band -> 3 | PASS (see O-G3) |
| G24 | D4 current ratio (l.85-86) | 2.06 = 5 (l.57) | 6,305.13 / 3,063.07 = 2.06 -> 5 | PASS |
| G25 | E1 promoter holding (l.89-90) | 63.75% = 5 (l.61) | >= 60 -> 5 | PASS |
| G26 | E2 promoter change over 3 years (l.91-92) | -36.25pp = 0 (l.62) | decrease > 3% -> 0 | PASS (see O-G2) |
| G27 | E3 pledge (l.93) | 0% = 5 (l.63) | 0% -> 5 | PASS |
| G28 | E4 contingent liabilities / net worth (l.94-95) | 1.42% = 5 (l.64) | 62.11 / 4,379.07 = 1.42% -> <5 -> 5 | PASS |
| G29 | M1 pricing power (l.102-104) | 5.74% to 13.45%, +7.7pp, CAGR 68.2% = 5 (l.70) | FY24 (359.08 + 52.75 + 51.29 - 28.37) / 7,573.32 = 5.74%; FY25 504.04 / 7,794.26 = 6.47%; FY26 2,881.44 / 21,416.18 = 13.45%; +7.71pp and CAGR >= 10 -> 5 | PASS |
| G30 | M2 cost advantage vs peers (l.105-106) | PEER DATA NEEDED = 0 (l.71) | rule l.99-100 -> 0 | PASS |
| G31 | M3 capital efficiency (l.107-108) | FAT 14.7x, ROCE 50.99% = 5 (l.72) | the denominator is unanchored (G02). On stated inputs FAT >= 21,416.18 / (8,156.82 - 6,305.13) = 11.57x even if every non-current asset were a fixed asset. ROCE > 20% on FY26 and on the median. -> 5 on any denominator | PASS |
| G32 | M4 customer stickiness (l.109-111) | no decline year, receivable days +8.6 over period = 5 (l.73) | zero decline years; 100.26 - 91.65 = +8.61 over period; FY25 -7.80 and FY26 +8.61 against FY24, both within 10 -> 5 | PASS (see O-G1) |
| G33 | M5 scale (l.112-113) | PEER DATA NEEDED = 0 (l.74) | -> 0 | PASS |
| G34 | M6 technology / R&D (l.114-116) | R&D NOT FOUND = 0 (l.75) | every band needs an R&D ratio -> 0 | PASS |
| G35 | M7 regulatory / licence (l.117-119) | no licence or player count = 0 (l.76) | margin moved +7.71pp, outside both the 3pp and 5pp bands, so bands 5 and 3 fail on any reading; ceiling is 1, not a moat | PASS |
| G36 | M8 distribution (l.120-122) | quantified at one date, no time series, no revenue per outlet = 1 (l.77) | bands 5 and 3 need growth, which is NOT FOUND; the reach is at least "mentioned" -> 1 | PASS |
| G37 | M9 brand (l.123-125) | PEER DATA NEEDED = 0 (l.78) | -> 0 | PASS |
| G38 | M10 switching costs (l.126-128) | revenue grew every year, days +8.6 = 5 (l.79) | rule reads "rose <= 10 days over period"; +8.61 -> 5 | PASS |
| G39 | M11 network effects (l.129-133) | 3 years, selling expense NOT FOUND = 0 (l.80) | bands 3 and 1 need the selling-expense ratio -> 0; fewer-than-6-years case stated | PASS |
| G40 | M12 negative WC (l.134-135) | 81 to 99 days, all > 45 = 0 (l.81) | 81.55 to 98.58 -> > 45 -> 0 | PASS |
| G41 | Block totals and core (l.54-95) | A 19, B 1, C 20, D 17, E 15, core 72, moat 21, grand 93 (l.86) | A 5+5+4+5 = 19; B 0+0+0+1 = 1; C 5+5+5+5 = 20; D 4+5+3+5 = 17; E 5+0+5+5 = 15; core 72; moat 5+0+5+5+0+0+0+1+0+5+0+0 = 21; grand 93 | PASS |
| G42 | Moat present at >= 3; class bands (l.98-99, l.137-138) | M1, M3, M4, M10 = 4, STRONG (l.82) | 4 present -> 4 to 5 -> STRONG | PASS |
| G43 | Data confidence; 3 to 4 years LIMITED, one-tier downgrade (l.142-144) | LIMITED, downgrade applied, history_downgrade true (l.87, YAML l.128) | 3 years -> LIMITED -> downgrade | PASS |
| G44 | Classification matrix (l.146-149) | Core 60-79 + STRONG = GOOD+, downgrade to GOOD (l.87) | 72 in 60 to 79, STRONG -> GOOD+ -> one tier -> GOOD | PASS |
| G45 | Deal-breakers 1 to 9 (l.151-159) | DB4 caps AVERAGE, DB2 caps GOOD (non-binding); final AVERAGE (l.87-89) | DB1 A 19, no. DB2 B 1 < 8, yes, max GOOD. DB3 median ROCE 26.07, no. DB4 -0.014 < 0.50, yes, max AVERAGE. DB5 pledge 0, no. DB6 0.68x and 18.80x, no. DB7 no decline year, no. DB8 PAT positive in all three years, no. DB9 history 3, not < 3, no. Binding cap DB4 -> AVERAGE | PASS |
| G46 | State which years drive each deal-breaker (l.151-154) | both driven by FY26 (l.88); YAML DB2 names FY25 and FY26 FCF (YAML l.127) | both statements are made; the but-for test confirms FY26 alone triggers both (O-G5) | PASS (see O-G5) |
| G47 | YAML block: schema, FLAG-GATE0 condition, totals, analyst_note cap (l.168-198) | all fields present; FLAG-GATE0 set; analyst_note about 100 words (YAML l.141) | classification <= AVERAGE with the FY26 depressor named -> flag required and present; 72 + 21 = 93; note under 200 words | PASS |

### 1.2 Gate 0 findings (FAIL rows)

**G02. Source anchors (rule src 01 l.15-18). MINOR.**
- The M3 row uses a fixed-asset denominator of 1,457.08 lakh (01-gate0.md l.72). The row has no anchor. The base-data table (l.8-25) has no fixed-asset line.
- "pre-IPO promoter holding 87.52% (RHP)" names the document but no page (l.62).
- Recomputed: none needed. M3 = 5 on any denominator, because FAT has a floor of 11.57x on the stated balance sheet (G31). E2 = 0 on any pre-IPO start.
- Effect on decision: none. Owner: stage 1 (Gate 0).

**G07. FCF formula, FY24 capex (rule src 01 l.39-40). MINOR.**
- The rule fixes capex as purchases of PPE and intangibles. A purchase is never negative.
- B01 enters FY24 capex as -1.06 lakh "(inflow)" and adds it to CFO, so FY24 FCF reads 81.99 (01-gate0.md l.24, l.40). That figure is either a net-of-disposals line or a mislabel. B01 does not state it as a proxy.
- Recomputed: the gross FY24 purchase figure is NOT FOUND in B01. On any gross figure of 0 or more, FY24 FCF is 80.93 or lower. B2 stays 0, because 0 or 1 positive year of 3 is below 50%. B3 stays 0, because cumulative FCF is -1,270.79 or lower. Block B stays 1.
- Effect on decision: none. Owner: stage 1 (Gate 0). Verifier A owns the RHP p.58 line itself.

### 1.3 Gate 0 observations (PASS rows, no score change)

- **O-G1. M4 reading.** Rule src 01 l.109-110 says "receivable days stable ±10" with no window. B01 reads it on the period: +8.61 (01-gate0.md l.73). On that reading FY25 and FY26 both sit within 10 days of FY24 (-7.80, +8.61). The year-on-year reading gives FY25 to FY26 +16.41. B01 states that number on l.73. On that reading M4 falls to 3, because zero decline years meets "max 1 decline year". M4 stays a moat (>= 3). The moat score becomes 19 and the grand total 91. Moat class stays STRONG and classification stays AVERAGE. The separating fact is the rule wording; M10 (l.127) says "over period" explicitly, M4 does not.
- **O-G2. E2 window.** The rule asks for the change over 3 years (rule src 01 l.91). B01 starts at 7 Aug 2024, 100% (RHP p.76), about 2.1 years before 30 Sep 2026 (l.62). The Sep 2023 holding is not stated. Any pre-IPO start (100% or 87.52%) gives a fall above 3pp, so E2 = 0 on either reading.
- **O-G3. D3 boundary.** 0.501 is strictly above the shared 0.5 line, so 3 is the literal score (l.56). At 4, the core is 73 and the classification is unchanged.
- **O-G4. M4 and M10 share inputs.** Both tests read revenue-decline years and receivable days. The rubric prescribes both, and B01 discloses the overlap (l.83, YAML l.138). This is rubric design, not a maker error. The FY26 consolidation (three acquisitions, RHP p.59 note 3 per l.4) drives M1, M3, M4 and M10. It also drives B07 H1. Stage 11 must credit this one improvement through one mechanism only (carried forward, Part 4).
- **O-G5. Deal-breaker driving years.** The report says both deal-breakers are driven by FY26 (l.88). The YAML says DB2 is driven by FY25 and FY26 FCF (YAML l.127). On FY24 and FY25 only: B1 629.03 / 491.11 = 1.28 -> 5; B2 1 of 2 = 50% -> 2; B3 -56.04 -> 0; B4 81.55 - 88.98 = -7.43 days -> 5. Block B = 12, above 8. CFO/PAT 1.28, above 0.50. So FY26 alone triggers both deal-breakers. The report wording is the right one for a post-IPO rebase sizing question.
- **O-G6. Presentation ROCE.** B01 does not use the unlabelled presentation chart, 24 / 44 / 50 (l.31). If it were used: median 44 -> A1 5; minimum 24 -> A2 5; A4 5. Block A stays 19.
- **O-G7. analyst_note wording.** The note says "the cash block (1/20) and the 3-year history cap it at AVERAGE" (YAML l.141). Block B < 8 (DB2) caps at GOOD. The AVERAGE cap comes from DB4, cumulative CFO/PAT. The flags field (YAML l.115) and deal_breakers (l.126) state this correctly.

## PART 2. EMERGING MOAT (B07) COMPLIANCE

### 2.1 Scorecard re-derivation (rule src 07 l.171-176)

Matrix: HH = 4; HM/MH = 3; HL/MM/LH = 2; ML/LM = 1; LL = 1; no evidence = 0. Multipliers: documented 1.0, claim 0.7, inference 0.5.

| ID | L x I (07-emoat.md l.79-85) | Raw by matrix | Tier stated | Tier consistent with Section 3 text | Adjusted re-derived | B07 adjusted |
| --- | --- | --- | --- | --- | --- | --- |
| B2 | H x L | 2 | DOC | yes, ISO 9001, 13485, 15189 held (deck p.7-8, l.41) | 2.0 | 2.0 |
| B3 | L x M | 1 | CLAIM | yes, density stated, no cost or price effect (l.41) | 0.7 | 0.7 |
| C1 | M x M | 2 | CLAIM | yes, cross-sell per customer NOT FOUND (l.42) | 1.4 | 1.4 |
| C2 | M x M | 2 | DOC | yes, 87.92 / 83.31 / 81.76 / 80.60% (AR p.14, press release p.3, l.42) | 2.0 | 2.0 |
| D2 | M x M | 2 | CLAIM | yes, no participants, volume or digital revenue % (l.43) | 1.4 | 1.4 |
| G1 | M x L | 1 | DOC | yes, post-IPO cash 74.20 Cr (deck p.22, l.46) | 1.0 | 1.0 |
| H1 | H x L | 2 | DOC | yes, three acquisitions (AOC-1 p.58-59 via B03, l.19, l.47) | 2.0 | 2.0 |
| 16 other rows incl. R1, I1, I2 | none | 0 | none | yes, each NO EVIDENCE FOUND or scored 0 with reason (l.40-48, l.73) | 0 | 0 |
| Total | | | | | 10.5 | 10.5 |

Band: 10.5 < 12 -> NO MEANINGFUL EMERGING MOAT (NONE) (rule src 07 l.175-176). Concur.

Band robustness, both sides:
- Upward. MODEST needs +1.5. The only route is to re-tier C1, D2 and B3 to documented: +0.6, +0.6 and +0.3 give exactly 12.0. Section 3 does not support any of the three re-tierings. Cross-sell, platform adoption and density effects are all unevidenced (l.41-43).
- Downward. Without H1 the total is 8.5. Without H1 and G1 it is 7.5. If B2 is read as a claim, the total is 9.9. NONE holds on every reading.

### 2.2 Rule-by-rule table

| ID | Rule (source) | B07 states | Check | Result |
| --- | --- | --- | --- | --- |
| E01 | All six sections in one response (rule src 07 l.28) | Sections 1 to 6 plus the Optionality Register (07-emoat.md l.14-105) | present | PASS |
| E02 | Evidence taxonomy on every item (l.29-34) | tags DOC / CLAIM / INF throughout | catalysts_12m row "Top-10 share falls below 80.60% and top-1 disclosed" is tagged documented (B07 block l.23). The trend is documented. The forward fall is not | FAIL, MINOR (finding E02) |
| E03 | Source anchor on every evidence item (l.35-36) | header says upstream blocks carry the page anchors (l.4) | several items anchor to B03, B04 or B05 with no document page; two AR items have no page; one item rests on step-1 memory (list in E03) | FAIL, MINOR (finding E03) |
| E04 | Skepticism; NO EVIDENCE FOUND, no force-fit (l.37-40) | 13 categories plus R1 at NO EVIDENCE FOUND or 0 with reason (l.40-48, l.73) | no category credited above its evidence | PASS |
| E05 | Completionist guard: re-examine at 12+ active (l.41-46) | 7 with any evidence, 0 Strong/Moderate; guard not triggered (l.69-70) | 7 < 12 | PASS |
| E06 | Documented-item recount, stated as "[n] items across [m] categories" (l.44-46, l.157-159) | "5 documented items across 4 categories", the fifth being Alltrak ownership under D2 (l.70; B07 block l.19) | Alltrak is one of the three H1 acquisitions (l.10, l.19). It is counted twice, and the fifth item sits in a fifth category | FAIL, MINOR (finding E06) |
| E07 | Section 1: 1A, 1B, 1C (l.48-55) | 1A table, 1B by direction, 1C mix table (l.15-31) | present; 3-year expected mix correctly NOT FOUND | PASS (O-E7) |
| E08 | Section 2: 2A, 2B, 2D (l.57-60, l.63) | Rs 3.00 Cr machinery, nil utilised; no plant; Middle East deferred (l.34-37) | present | PASS |
| E09 | Section 2C: capex under execution x historical FAT, as % of revenue; show the arithmetic (l.60-63) | "Capex-embedded growth: 0% documented"; FAT not computed (l.36; B07 block l.26) | arithmetic not shown; 0 holds only on one of two readings (finding E09) | FAIL, MINOR (finding E09) |
| E10 | All 22 categories plus R1 addressed or NO EVIDENCE (Verifier C rule 3; rule src 07 l.65-67) | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 (l.40-48); R1 (l.73) | 22 + 1 = 23, each addressed | PASS |
| E11 | Section 3 summary table: all 22 rows, count of Strong/Moderate stated (l.155-157) | 16 table rows (l.51-68); count stated (l.69) | A1-A4, E1/E2, H2/H3 and I1/I2 grouped into four rows | FAIL, MINOR (finding E11) |
| E12 | Section 5: full scoring table, all 23 rows (l.171-174) | 7 scored rows plus one row "All other 16 rows incl. R1" (l.77-86) | 7 of 23 rows shown | FAIL, MINOR (finding E12) |
| E13 | Raw scores per the L x I matrix (l.171-173) | 7 rows (l.79-85) | all 7 match (2.1) | PASS |
| E14 | Evidence multipliers (l.173) | 1.0 / 0.7 / 0.5 (l.76) | applied correctly on all 7 rows | PASS |
| E15 | Adjusted total (l.173-174) | 10.5 (l.87-88) | 2.0 + 0.7 + 1.4 + 2.0 + 1.4 + 1.0 + 2.0 = 10.5 | PASS |
| E16 | Classification band (l.175-176) | NONE (l.88; B07 block l.16) | 10.5 < 12 | PASS |
| E17 | Scores consistent with stated tiers; no claim scored as documented (Verifier C rule 3) | claim rows at 0.7, documented rows at 1.0 | no claim-only row carries 1.0 | PASS (O-E8) |
| E18 | I1/I2 contribution stated separately (l.180-181) | "Of which I1/I2: 0." (l.87) | stated | PASS |
| E19 | Category 21 (I1) present; > 0 only with both legs and a documented (b) leg (Verifier C rule 8; rule src 07 l.122-138) | NO EVIDENCE FOUND, no hires, pay data or competitor arithmetic (l.48) | present, scored 0 | PASS |
| E20 | Category 22 (I2) present; > 0 only with a specific named sacrifice (Verifier C rule 8; rule src 07 l.139-153) | "nothing" must be destroyed; a diagnostic chain can insource collection (RHP p.27) (l.48) | present, scored 0 per l.149-150 | PASS (O-E4) |
| E21 | Section 4 R1: 4A, 4B, 4C (l.161-168) | no approvals, no scheme, no moat (l.73) | present | PASS |
| E22 | Optionality register: four columns; scored-0 or claim-only items; carried in YAML (l.183-196) | 7 rows (l.92-100; B07 block l.27-34) | membership and format correct; YAML carries all 7 | PASS |
| E23 | Section 6A timeline windows; 6B risks with early warnings (l.199-201) | 12m, 12-24m, 24-36m, 3-5yr; risks with early signs (l.103) | present | PASS |
| E24 | Section 6C combined table from the injected Gate 0 block (l.201-203) | core 72, moat 21, 4 moats, STRONG, AVERAGE vs EM 10.5 NONE (l.103) | values match B01 YAML l.16-24; written as prose, not a table | PASS (O-E5) |
| E25 | Section 6D combined classification; reasoning on HIGH POTENTIAL / TURNAROUND (l.203-208) | AVERAGE; not HIGH POTENTIAL or TURNAROUND because EXPANSION needs 40+ (l.104) | the rule source names the label set but not the cell map; AVERAGE + NONE -> AVERAGE adds no forward credit and does not demote | PASS |
| E26 | Section 6E card: evolution map, 12-month catalysts, biggest risk (l.208-210) | present (l.105) | map is one line, not per family | PASS (O-E5) |
| E27 | Report ends with the fenced YAML block (l.212-214) | 07-emoat.md ends at 6E, line 105 | the block exists only at outputs/blocks/B07-emoat.yaml | FAIL, MINOR (finding E27) |
| E28 | YAML schema and values match the report (l.216-243) | all 19 fields present (B07 block l.1-42) | em_score, class, active_categories [], register, combined fields match; analyst_note about 95 words. The recount and 2C values carry E06 and E09 | PASS |

### 2.3 Emerging Moat findings (FAIL rows)

**E02. Evidence tier on a forward catalyst (rule src 07 l.29-34). MINOR.**
- catalysts_12m row 3, "Top-10 share falls below 80.60% and top-1 disclosed", is tagged documented (B07 block l.23).
- The documented part is the past trend (AR p.14; press release 2026-10-28 p.3). The forward fall has no committed contract or plan behind it. On the taxonomy it is an inference from the trend.
- Recomputed: evidence_type "inference" for the forward event, with the trend kept as the documented anchor.
- Effect: no B07 score change. catalysts_12m feeds Pillar 3 catalyst proximity (rule src 07 l.231). Stage 11 must not credit this row as a documented catalyst (carried forward, Part 4). Owner: stage 7.

**E03. Anchors that stop at an upstream block or have no page (rule src 07 l.35-36). MINOR.**
Items with a block-only anchor, a missing page, or a memory source:
- "bought from promoter-side sellers for 1,152.23 Lakhs (B03)" (07-emoat.md l.10).
- "B04: 2.81%, 2.75%, 1.20% of FY26 revenue" (l.21); 1C mix percentages "B04" (l.28-30).
- "2,530 labs, 19,000+ pincodes (B04)" (l.41).
- "four service lines sold to a base (AR segment note DOC)", with no page (l.42).
- "Alltrak 172.40 of 199.64 profit in 34 days, B03" (l.43).
- "all revenue domestic (step-1 brief, memory)" (l.44). The step-1 brief is memory, not evidence, as B07's own header says (l.4).
- "ESOP plan 2026 pool 5,64,000 shares ... (AR text ...)", with no page (l.45).
- "13.5-16.0% on most term debt (B03)"; "consolidated 100.3 (B03), 104 H1 derived (B05)" (l.46).
- "1.96x profit for Healthcare (B03)" (l.47).
Recomputed: none. No scored row rests only on these anchors. Each scored row has at least one document page: B2 deck p.7-8, B3 deck p.7, C1 call p.5 and p.11, C2 AR p.14, D2 deck p.8 and call p.14-16, G1 deck p.22, H1 AR p.13-14 and AOC-1 p.58-59. Effect: none. Owner: stage 7.

**E06. Documented-item recount double counts Alltrak (rule src 07 l.44-46, l.157-159). MINOR.**
- B07 states "5 documented items across 4 categories" (07-emoat.md l.70; B07 block l.19). The list is B2 ISO, C2 trend, G1 cash, H1 three acquisitions, plus "Alltrak ownership counted under D2".
- Alltrak is one of the three H1 acquisitions (l.10, l.19). The fifth item duplicates part of the fourth, and it sits in a fifth category (D2).
- Recomputed: 4 distinct documented items across 4 categories (B2, C2, G1, H1) if H1's three acquisitions count as one item. If each acquisition counts as one item, the count is 6 items across 4 categories. Five distinct items is not reachable. evidence_mix.documented = 5 (B07 block l.18) inherits the error.
- The score does not double credit. D2 is tiered as a claim on platform adoption, not on ownership. The guard threshold (12 active categories) is far away. Effect: none. Owner: stage 7.

**E09. Section 2C arithmetic not shown (rule src 07 l.60-63). MINOR.**
- The rule asks for capex under execution x historical FAT, expressed as % above current revenue, with the arithmetic shown. B07 states "0% documented" and does not compute FAT (07-emoat.md l.36; B07 block l.26).
- Reading 1: capex under execution is 0. The Rs 3.00 Cr object has nil utilisation and no orders placed (RHP RF18 via B05, l.34). Then 0 x FAT = 0%. This is the better-evidenced reading, and it matches B07's value. The line should show "0 x FAT = 0".
- Reading 2: the committed Rs 3.00 Cr counts as under execution. FAT is not in B07's injected inputs, because the B01 YAML carries none. The field would then be NOT FOUND, not 0. On B01's FY26 FAT of 14.7x (01-gate0.md l.72, unanchored denominator), it would be 3.00 x 14.7 = 44.1 Cr. That is 20.6% of FY26 revenue of 214.16 Cr (21,416.18 lakh, 01-gate0.md l.9). It applies a services asset turn to imaging machines, so it is a mechanical number.
- Separating observation: orders placed or spend started on the 14 sonography and 4 X-ray machines, in the next IPO-proceeds monitoring filing or H2 FY27 results.
- Effect: none on EM. Stage 11 must not use capex_embedded_growth_pct as a CAPACITY basis without the reading named (carried forward, Part 4). Owner: stage 7.

**E11. Section 3 summary table grouped (rule src 07 l.155). MINOR.**
- The rule asks for all 22 rows. B07 shows 16 rows: A1-A4, "E1, E2", "H2, H3" and "I1, I2" are grouped (07-emoat.md l.53, l.61, l.67, l.68).
- Recomputed: all grouped rows are None / n/a and match the Section 3 text. No value changes. Owner: stage 7.

**E12. Section 5 scorecard not full (rule src 07 l.173-174). MINOR.**
- The rule asks for a full scoring table with all 23 rows. B07 shows 7 scored rows and one row "All other 16 rows incl. R1 | none | 0" (07-emoat.md l.86).
- Recomputed: 7 + 16 = 23 rows covered. Every collapsed row is 0 in Section 3. The total stays 10.5. Owner: stage 7.

**E27. Report does not end with the YAML block (rule src 07 l.212-214). MINOR.**
- 07-emoat.md ends at Section 6E (line 105). The fenced B07-emoat block is not in the report. It exists at outputs/blocks/B07-emoat.yaml and is complete and valid.
- B01 follows the rule; its report ends with its block (01-gate0.md l.102-142). Effect: none, because the block file holds the data. Owner: stage 7.

### 2.4 Emerging Moat observations (PASS rows, no score change)

- **O-E1. H1 basis.** H1 "industry consolidation beneficiary" scores 2.0 on three bolt-ons bought from promoter-side sellers (07-emoat.md l.47). No competitor exit and no regulation is evidenced. The rubric lists bolt-on acquisitions (rule src 07 l.115-117), so the credit is within the rule. B07 calls it generous (l.88). Without it the total is 8.5, still NONE.
- **O-E2. Strength labels and L x I.** C1, C2 and D2 carry M x M, and Section 3 labels them Weak (l.42-43). The rule source sets no map from L x I to strength, so this is not a FAIL. active_categories is [] and follows the labels (B07 block l.17).
- **O-E3. Band robustness.** See 2.1. NONE needs three unsupported re-tierings to cross into MODEST.
- **O-E4. I2 answered at business level.** Rule src 07 l.140 asks the question "for each moat claimed anywhere in this scan". B07 gives one business-level answer (l.48). No row reaches Strong or Moderate, so no moat is claimed. A single answer is a defensible reading. The score of 0 is correct on either reading.
- **O-E5. Section 6 formats.** 6C is prose, not a table. The 6E evolution map is one line, not per family (l.103, l.105). All required fields are present, and the 6C values match B01 YAML l.16-24.
- **O-E6. Kartavya row in catalysts_12m.** "Kartavya Healtheon Rs 4.50 Cr loan repaid or interest received after 2026-11-25" is tagged documented (B07 block l.22). The due date sits in a filed loan, so the tag is defensible. It is a governance tripwire, not a moat or earnings catalyst. Stage 11 should not count it toward Pillar 3 catalyst proximity (Part 4).
- **O-E7. Section 1C columns.** The 1C table has no "profitability impact" column (l.26-30). The margin line below the table covers part of it: "group EBITDA 13% to 15-16% via mix (call p.8)" (l.31). Segment margins are NOT FOUND.
- **O-E8. B2 tier.** The ISO certificates are tagged documented on a deck anchor (deck p.7-8, l.41). A held certificate is a present fact, not a plan, so the documented tag is defensible. As a claim, B2 is 1.4 and the total is 9.9, still NONE.
- **O-E9. Cross-artifact date (out of scope, number domain).** The Alltrak acquisition date is 2026-02-25 in B01 (RHP p.59 note 3, 01-gate0.md l.4) and 2026-02-26 in B07 (AOC-1 via B03, 07-emoat.md l.19). Verifier A owns this. No score depends on it.

## PART 3. VERIFIER C RULES OUT OF PHASE-1 SCOPE

| Rule | Subject | Status |
| --- | --- | --- |
| 4, 5 | Valuation (B11) growth symmetry, pillar mechanics, severity | pending phase 3 |
| 6 | B09 downstream candidates | not run: B09 is not an input in this scope |
| 7 | Method plurality (B11) | pending phase 3 |
| 9 | Business Understanding Narrative (stage 13) | pending phase 3 / finalize |
| 10 | Halt 1 dossier (B09b) | fires at the /finalize pass; the phase-1 check is mechanical in run-pipeline step 6b |
| 11, 12 | Role 1 exit construction, Amendment 19 FV path | pending phase 3 |
| 13, 14 | Expectation Ledger and decomposition gates | pending phase 3 |
| 15 | Skill-to-source fidelity (section-1b) | pending phase 3 |

Rules 2, 3 and 8 are covered in Parts 1 and 2.

## PART 4. CARRY-FORWARD FOR THE PHASE-3 VALUATION AUDIT

These are not phase-1 findings. They name points where a B01 or B07 value could be misused downstream.
1. One improvement, one mechanism. The FY26 consolidation of three acquired entities drives Gate 0 M1, M3, M4 and M10 (01-gate0.md l.83) and B07 H1 (07-emoat.md l.47). Stage 11 must credit it once.
2. UA qualifier. EM is 10.5 (B07 block l.15). The "EM >= 25" UA qualifier (rule src 07 l.12-13) is not met on this scan.
3. Pillar 3 catalyst inputs. catalysts_12m row 3 is an inference, not documented (E02). Row 2, the Kartavya repayment, is a tripwire, not a catalyst (O-E6).
4. CAPACITY basis. capex_embedded_growth_pct = 0 rests on reading 1 of E09. Reading 2 is NOT FOUND, or 20.6% on an unanchored FAT. The separating observation is machine orders placed.

## PART 5. TEMPLATE NOTE FOR THE OPERATOR

Line 379 of prompts/12-verifiers-pipeline.md is a placeholder, "(same line, comment "# rule 9; any fail = REWORK stage 13")", not a YAML key. This block writes `business_narrative: {status: "pending phase 3", fails: "pending phase 3"}` with the rule 9 comment so the file parses. A one-line fix to the template would name the key.

## YAML BLOCK

```yaml
stage: B12c
company: "CREDENT"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
# scope: phase 1 only (B01 Gate 0 + B07 Emerging Moat). Valuation half (B10, B11; Verifier C rules 4-7, 9-15) pending phase 3.
gate0:
  rules_checked: 47
  fails:
    - "G02 source anchors, Gate 0 op rule 4 (MINOR): M3 fixed-asset denominator 1,457.08 lakh unanchored and absent from base table; pre-IPO promoter 87.52% cites RHP with no page. No score change."
    - "G07 FCF formula (MINOR): FY24 capex entered as -1.06 lakh inflow; purchases cannot be negative and no proxy basis stated. B2 = 0 and B3 = 0 on any gross figure. No score change."
emoat:
  rules_checked: 28
  fails:
    - "E02 evidence taxonomy (MINOR): catalysts_12m row 'Top-10 share falls below 80.60%' tagged documented; the trend is documented, the forward fall is an inference."
    - "E03 source anchors (MINOR): items anchored only to upstream blocks B03/B04/B05, two AR items with no page, one item on step-1 memory. No scored row rests only on these."
    - "E06 completionist recount (MINOR): '5 documented items across 4 categories' counts Alltrak twice (inside H1 and under D2); distinct count 4 items across 4 categories (B2, C2, G1, H1). No score change."
    - "E09 Section 2C (MINOR): arithmetic not shown; capex_embedded_growth_pct 0 holds only on the capex-under-execution = 0 reading."
    - "E11 Section 3 summary table (MINOR): 22 categories shown in 16 rows (A1-A4, E1/E2, H2/H3, I1/I2 grouped)."
    - "E12 Section 5 scorecard (MINOR): 7 of 23 rows shown; 16 zero rows collapsed into one."
    - "E27 output rule (MINOR): 07-emoat.md ends at 6E without the fenced YAML block; block exists only at outputs/blocks/B07-emoat.yaml."
valuation: {rules_checked: "pending phase 3", fails: "pending phase 3"}
expectation_ledger: {present: "pending phase 3", downside_row: "pending phase 3", all_rows_confirm_by: "pending phase 3", all_rows_metric_threshold: "pending phase 3", prob_in_range: "pending phase 3", decay_status_valid: "pending phase 3", off_ledger_credit: "pending phase 3", residual_pct_cmp: "pending phase 3", residual_starter_cap_ok: "pending phase 3", fails: "pending phase 3"}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "pending phase 3", fails: "pending phase 3"}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: "pending phase 3"
recomputed_decision: "pending phase 3"
findings:
  - id: "G02"
    framework: "Gate 0 (B01)"
    rule: "01-gate-0-pipeline.md op rule 4, source anchors mandatory"
    severity: "MINOR"
    finding: "M3 FAT denominator 1,457.08 lakh carries no anchor and is not in the base-data table (01-gate0.md l.72); pre-IPO promoter holding 87.52% cites RHP with no page (l.62)."
    recomputed: "M3 = 5 on any denominator: FAT floor 21,416.18 / (8,156.82 - 6,305.13) = 11.57x; E2 = 0 on any pre-IPO start."
    decision_effect: "none"
    owner: "stage 1 (Gate 0)"
  - id: "G07"
    framework: "Gate 0 (B01)"
    rule: "01-gate-0-pipeline.md FCF definition, capex = purchases of PPE and intangibles"
    severity: "MINOR"
    finding: "FY24 capex entered as -1.06 lakh (inflow), giving FY24 FCF 81.99 (01-gate0.md l.24, l.40); a purchase cannot be negative and no proxy basis is stated."
    recomputed: "Gross FY24 purchases NOT FOUND in B01; FY24 FCF <= 80.93 on any gross figure; B2 = 0 (0 or 1 of 3), B3 = 0 (cumulative FCF <= -1,270.79); Block B stays 1."
    decision_effect: "none"
    owner: "stage 1 (Gate 0)"
  - id: "E02"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md op rule 2, evidence taxonomy on every item"
    severity: "MINOR"
    finding: "catalysts_12m row 'Top-10 share falls below 80.60% and top-1 disclosed' tagged documented (B07 block l.23); only the past trend is documented."
    recomputed: "evidence_type inference for the forward event; trend stays the documented anchor (AR p.14; press release 2026-10-28 p.3)."
    decision_effect: "none in B07; stage 11 must not credit it as a documented Pillar 3 catalyst"
    owner: "stage 7"
  - id: "E03"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md op rule 3, source anchors on every evidence item"
    severity: "MINOR"
    finding: "Block-only anchors (B03/B04/B05) at 07-emoat.md l.10, l.21, l.28-30, l.41, l.43, l.46, l.47; AR items with no page at l.42 and l.45; step-1 memory used at l.44."
    recomputed: "none; every scored row has at least one document page anchor (B2 deck p.7-8, B3 deck p.7, C1 call p.5/p.11, C2 AR p.14, D2 deck p.8 and call p.14-16, G1 deck p.22, H1 AR p.13-14 and AOC-1 p.58-59)."
    decision_effect: "none"
    owner: "stage 7"
  - id: "E06"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md op rule 6 and Section 3, documented-item recount"
    severity: "MINOR"
    finding: "Recount '5 documented items across 4 categories' (07-emoat.md l.70; B07 block l.19) counts Alltrak ownership under D2 although Alltrak is one of the three H1 acquisitions (l.10, l.19); evidence_mix.documented = 5 inherits it."
    recomputed: "4 distinct documented items across 4 categories (B2, C2, G1, H1), or 6 items across 4 if each acquisition counts; 5 is not reachable. Score unchanged: D2 is tiered as a claim."
    decision_effect: "none"
    owner: "stage 7"
  - id: "E09"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md Section 2C, capex under execution x historical FAT, show the arithmetic"
    severity: "MINOR"
    finding: "capex_embedded_growth_pct 0 stated without the arithmetic and without FAT (07-emoat.md l.36; B07 block l.26)."
    recomputed: "Reading 1 (better evidenced): capex under execution 0 (nil utilised, no orders) x FAT = 0%. Reading 2: committed 3.00 Cr counts; FAT not in B07 inputs, so NOT FOUND; on B01 FY26 FAT 14.7x (unanchored) 3.00 x 14.7 = 44.1 Cr = 20.6% of 214.16 Cr. Separator: machine orders placed or spend started (IPO monitoring filing, H2 FY27)."
    decision_effect: "none in B07; stage 11 must name the reading before any CAPACITY basis use"
    owner: "stage 7"
  - id: "E11"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md Section 3 summary table, all 22 rows"
    severity: "MINOR"
    finding: "Summary table has 16 rows; A1-A4, E1/E2, H2/H3, I1/I2 grouped (07-emoat.md l.51-68)."
    recomputed: "all grouped rows None / n/a, consistent with Section 3 text; no value change."
    decision_effect: "none"
    owner: "stage 7"
  - id: "E12"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md Section 5, full scoring table, all 23 rows"
    severity: "MINOR"
    finding: "Scorecard shows 7 scored rows and one row 'All other 16 rows incl. R1' (07-emoat.md l.77-86)."
    recomputed: "7 + 16 = 23 rows covered; collapsed rows all 0; total stays 10.5."
    decision_effect: "none"
    owner: "stage 7"
  - id: "E27"
    framework: "Emerging Moat (B07)"
    rule: "07-emerging-moat-pipeline.md OUTPUT, report ends with the fenced YAML block"
    severity: "MINOR"
    finding: "07-emoat.md ends at Section 6E (line 105) with no fenced block; the block exists only at outputs/blocks/B07-emoat.yaml."
    recomputed: "block file complete and valid; no data lost."
    decision_effect: "none"
    owner: "stage 7"
critical_count: 0
major_count: 0
minor_count: 9
acceptance_rate: 88.0             # 66 passed of 75 checked (gate0 45 of 47, emoat 21 of 28); phase-1 scope only
```
