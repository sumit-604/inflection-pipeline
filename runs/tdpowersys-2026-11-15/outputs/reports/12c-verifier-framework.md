# VERIFIER C: FRAMEWORK ADHERENCE, TD Power Systems Ltd (TDPOWERSYS), run 2026-11-15

## 0. Scope and inputs

PHASE 1 SCOPE ONLY. This run audits Gate 0 (B01) and the Emerging Moat scan (B07). The valuation half (B10, B11; verifier rules 4, 5, 7, 11 to 15) runs in phase 3. No valuation framework document was read.

Inputs read:
- prompts/12-verifiers-pipeline.md, Verifier C section (operating rules).
- prompts/01-gate-0-pipeline.md (rule source). Cited as "P01 Lnn".
- prompts/07-emerging-moat-pipeline.md (rule source). Cited as "P07 Lnn".
- outputs/reports/01-gate0.md, cited as "B01 Lnn". Block outputs/blocks/B01-gate0.yaml is identical to the report's block (checked line by line).
- outputs/reports/07-emoat.md, cited as "B07 Lnn". Block outputs/blocks/B07-emoat.yaml is identical to the report's block (checked).

Method. I audit rule application. Verifier A owns whether a number is in the source. I take each stated input as stated and re-derive every score from it with the stated threshold. Every recomputed value names the B01 or B07 line it uses.

Both stage reports open with the Spear load-bearing-fact check (B01 L7-12, B07 L6-15). That is a CLAUDE.md duty, not a P01 or P07 rule, so it is not counted below.

## 1. Result summary

| Item | Value |
| --- | --- |
| Rules checked | 83 (Gate 0 55, Emerging Moat 28) |
| Rules passed | 75 |
| Acceptance rate | 90.4% (75 of 83) |
| Findings | 0 CRITICAL, 1 MAJOR, 7 MINOR |
| Not verifiable, not counted | 1 (E26, the 6D combined matrix is absent from P07) |
| Gate 0 classification AVERAGE | Concur on the reading the stage applied. One rule reading moves it to AVOID (C-G05). Operator ruling needed. |
| EM 18.7, MODEST | Concur. Every consistent multiplier convention lands between 17.5 and 22.7. All are MODEST and below the EM >= 25 UA qualifier. |
| Verifier rule 8 (categories 21 and 22) | Both present, both scored 0 under their gates. No REWORK trigger for stage 7. |

## 2. Gate 0 (B01) compliance table

| # | Rule (source) | B01 application | Re-derivation from stated inputs | Result |
| --- | --- | --- | --- | --- |
| G01 | Opening data line (P01 L23-25) | "Data available: 10 years (FY2017 to FY2026)" (B01 L3) | Present | PASS |
| G02 | Data confidence tier (P01 L142-144) | 10 years, full, no downgrade (B01 L101); history_downgrade false | 10+ years = full | PASS |
| G03 | Show every extracted number, anchored (P01 L14-18) | Derived values printed; per-year inputs not printed (B01 L32, L42, L78, L92) | C3, PAT sum, margins, ROE series, M11 CAGRs not re-derivable | FAIL MINOR (C-G03) |
| G04 | NOT FOUND discipline, no estimates (P01 L19-22) | Capex, payables, Sep 2023 promoter, peers marked NOT FOUND, scored 0 (B01 L44-46, L71, L83) | Consistent | PASS |
| G05 | ROCE formula fixed, no substitutes (P01 L27-31) | Proxy CE = equity + reserves + borrowings (B01 L16) | AR basis: FY26 333.72 / 1,083.37 = 30.8%; FY25 239.36 / 871.94 = 27.5% (B01 L16, L28-29) | FAIL MAJOR (C-G05) |
| G06 | ROE on average net worth; earliest year on closing, stated (P01 L32-33) | B01 L32 | As written | PASS |
| G07 | WC days formula, basis stated (P01 L34-38) | Sales basis stated (B01 L46; block data_notes) | FY26 145.9 + 98.9 - 81.0 = 163.8; FY25 124.8 + 107.5 - 65.9 = 166.4 (B01 L46) | PASS |
| G08 | FCF = CFO - (PPE + intangibles), acquisitions out (P01 L39-40) | FY26 10,418.02 + 433.76 lakh = 108.52 cr; leasehold land 214.85 lakh excluded and disclosed (B01 L44-45) | FY26 FCF 20.55 cr; 18.40 cr with the land in; sign unchanged | PASS |
| G09 | CAGR formula (P01 L41) | C1 (B01 L52) | (1,856.23 / 379.93)^(1/9) - 1 = 19.27% | PASS |
| G10 | Negative endpoint: N/M, score 0 (P01 L45-46) | C2 N/M on FY17 PAT -4.43 (B01 L53) | As written | PASS |
| G11 | Loss-to-profit swing noted in data_notes (P01 L47-49) | "loss-to-profit swing, FY18 to FY19" (block data_notes) | FY18 last loss year; FY19 ROE 0.7% positive (B01 L32) | PASS |
| G12 | C4 = 0 and noted when PAT CAGR is N/M (P01 L50) | B01 L55; data_notes | As written | PASS |
| G13 | No synthetic CAGR (P01 L49) | FY20-FY26 PAT CAGR 41.3% printed "for information only" (B01 L53) | Should read N/M only | FAIL MINOR (C-G13) |
| G14 | A1 median ROCE (P01 L55) | 14.6% = 1 (B01 L34) | Sorted series, median (12.6 + 16.6) / 2 = 14.6% (B01 L24-25); band 10-14.9 = 1 | PASS |
| G15 | A2 minimum ROCE (P01 L56) | -0.1% = 0 (B01 L35) | < 8 = 0 | PASS |
| G16 | A3 median ROE (P01 L57) | 12.1% = 2 (B01 L36) | (10.1 + 14.1) / 2 = 12.1% (B01 L32); band 12-14.9 = 2 | PASS |
| G17 | A4 ROCE trend (P01 L58-59) | 30.6% vs 0.6% = 5 (B01 L37) | Latest >= earliest | PASS |
| G18 | Block A total | 8 (B01 L38) | 1 + 0 + 2 + 5 = 8 | PASS |
| G19 | B1 cumulative CFO / PAT (P01 L62-63) | 0.57 = 1 (B01 L43) | CFO re-added = 430.62 (B01 L42); 430.62 / 758.50 = 0.568; band 0.50-0.69 = 1 | PASS |
| G20 | B2 FCF-positive years (P01 L64) | Capex NOT FOUND for 8 of 10 years = 0 (B01 L44) | P01 L20-21 | PASS |
| G21 | B3 cumulative FCF / PAT (P01 L65-66) | 0 (B01 L45) | FY25-FY26 only: 4.10 / 413.35 = 0.01, also 0 | PASS |
| G22 | B4 WC days change (P01 L67-68) | Payables NOT FOUND FY17-FY24 = 0 (B01 L46) | P01 L20-21 | PASS |
| G23 | Block B total | 1 (B01 L47) | 1 + 0 + 0 + 0 = 1 | PASS |
| G24 | C1 revenue CAGR (P01 L71) | 19.3% = 4 | Band 15-19.9 = 4 | PASS |
| G25 | C3 positive YoY years (P01 L73) | 9 of 9 = 5 (B01 L54) | 100% = 5 (count taken as stated; series not printed, see C-G03) | PASS |
| G26 | Block C total | 9 (B01 L56) | 4 + 0 + 5 + 0 = 9 | PASS |
| G27 | D1 net debt / EBITDA (P01 L77-79) | Net cash = 5 (B01 L62) | Borrowings 18.11 cr < cash and bank 198.59 cr; nil at 30 Sep 2026 (B01 L61-62) | PASS |
| G28 | D2 interest cover (P01 L80-81) | 43.9x = 5 (B01 L63) | 333.72 / 7.60 = 43.9x | PASS |
| G29 | D3 debt / equity (P01 L83-84) | 0.00 and 0.02 = 5 (B01 L64) | < 0.1 = 5 | PASS |
| G30 | D4 current ratio (P01 L85-86) | 1.87 = 4 (B01 L65) | 214,475.18 / 114,723.79 = 1.87; FY26 1.95; both in 1.5-1.99 = 4 | PASS |
| G31 | Block D total | 19 (B01 L66) | 5 + 5 + 5 + 4 = 19 | PASS |
| G32 | E1 promoter holding, professionally managed clause (P01 L89-90) | 27.16% = 0; clause not applied, promoter-led; sensitivity shown (B01 L70) | < 30 = 0 | PASS |
| G33 | E2 promoter change over 3 years (P01 L91-92) | Sep 2023 NOT FOUND; Mar 2024 to Sep 2026 -7.26pp = 0 (B01 L71) | 0 on either path (NOT FOUND, or fall > 3) | PASS |
| G34 | E3 pledge (P01 L93) | 0% = 5 (B01 L72) | As written | PASS |
| G35 | E4 contingent liabilities / net worth (P01 L94-95) | 14.7% = 3 (B01 L73) | Sum re-added 15,766.66 lakh = 157.67 cr; / 1,071.76 = 14.71%; band 5-15 = 3 | PASS |
| G36 | Block E total | 8 (B01 L74) | 0 + 0 + 5 + 3 = 8 | PASS |
| G37 | Core score | 45 (B01 L100) | 8 + 1 + 9 + 19 + 8 = 45 | PASS |
| G38 | M1 pricing power (P01 L102-104) | 5 (B01 L82) | Margin 2.8% to 18.1% (B01 L78), >= 2pp; CAGR 19.3% >= 10% | PASS |
| G39 | M2, PEER DATA NEEDED (P01 L99-100) | 0 (B01 L83) | No peer sheets (block input_gaps) | PASS |
| G40 | M3 capital efficiency (P01 L107-108) | 5 (B01 L84) | 1,856.23 / 293.70 = 6.32x; ROCE 30.6%. See O2 | PASS |
| G41 | M4 customer stickiness (P01 L109-111) | 5 (B01 L85) | Zero decline years; endpoint -8.3 days within +/-10. See O1 | PASS |
| G42 | M5, PEER DATA NEEDED | 0 (B01 L86) | As written | PASS |
| G43 | M6 technology / R&D (P01 L114-116) | 0 (B01 L87) | R&D 0.51% < 1% fails every band | PASS |
| G44 | M7 regulatory / licence (P01 L117-119) | 0 (B01 L88) | Unregulated = 0 | PASS |
| G45 | M8 distribution (P01 L120-122) | 0, "no quantified reach in provided numbers" (B01 L89) | Network mentioned in the AR; floor is 1 | FAIL MINOR (C-G45), recomputed 1 |
| G46 | M9, PEER DATA NEEDED | 0 (B01 L90) | As written | PASS |
| G47 | M10 switching costs (P01 L126-128) | 5 (B01 L91) | Grew all 9 years; receivable days fell 8.3 over the period | PASS |
| G48 | M11 network effects (P01 L129-133) | 5, "formula test only" (B01 L92) | 10 years allow the two-window test; 28.6% > 19.2%; selling % 4.03 to 3.86. See O3 | PASS |
| G49 | M12 negative WC (P01 L134-135) | 0 (B01 L93) | FY25 166.4 and FY26 163.8 days; > 45 = 0 on any data | PASS |
| G50 | Moat present at >= 3; class (P01 L99, L137-138) | 5 present, 25 of 60, STRONG (B01 L95) | Count 5 = STRONG (4-5); sum 25 on the scores as given | PASS |
| G51 | Classification matrix (P01 L146-149) | AVERAGE (B01 L102) | Core 40-59 = AVERAGE | PASS |
| G52 | Deal-breakers 1-9 (P01 L151-159) | DB2 fired; others not (B01 L104-107) | DB1 Block A 8, not < 8; DB2 1 < 8; DB3 14.6% >= 10%; DB4 0.57 >= 0.50; DB5 pledge 0; DB6 net cash; DB7 0 of 9 declines; DB8 FY24-FY26 PAT positive; DB9 10 years | PASS |
| G53 | Years driving each deal-breaker stated (P01 L153-154) | B01 L106 | Present | PASS |
| G54 | FLAG-GATE0 when <= AVERAGE with depressors (P01 L175-177) | Raised (block flags) | As written | PASS |
| G55 | Block schema; analyst_note <= 200 words (P01 L168-197) | All fields present; note about 75 words | As written | PASS |

Gate 0 tally: 55 checked, 51 passed, 4 failed (G03, G05, G13, G45).

### 2a. Classification robustness, re-derived from B01's stated inputs

Upside. The core cannot reach 60 under any value the stated data allows:
- B2 is at most 2. CFO is negative in FY17, FY18 and FY21 (B01 L42), so FCF is negative in those years. FY25 FCF is -16.45 cr (B01 L44). At most 6 of 10 years are positive (60%), band 50-74 = 2.
- B3 is at most 3. Cumulative FCF / PAT cannot exceed cumulative CFO / PAT of 0.57 (B01 L43), band 0.40-0.59 = 3.
- B4 is at most 5. A1 to the next band adds 2. C1 to the next band adds 1.
- Ceiling: 45 + 2 + 3 + 5 + 2 + 1 = 58. AVERAGE holds. The E1 professionally managed clause is left out because it does not apply to a promoter-led company (B01 L70).

Downside. The core sits 5 points above the AVOID line (core < 40, P01 L149):
- A3 at 12.1% sits 0.1pp above its band edge (B01 L36). A fall costs 2 points.
- E4 at 14.71% sits 0.29pp below its band edge (B01 L73). A rise costs 2 points.
- Both together give core 41, still AVERAGE.
- The one reading that crosses the line is the strict ROCE reading in C-G05: Block A falls by 6, core 39, AVOID.

## 3. Emerging Moat (B07) compliance table

| # | Rule (source) | B07 application | Check | Result |
| --- | --- | --- | --- | --- |
| E01 | All six sections in one response (P07 L28) | Sections 1-6 and the register (B07 L17-390) | Present | PASS |
| E02 | Taxonomy on every evidence item; evidence table per category (P07 L29-34, L66-67) | Several items untagged; one fact on two tiers | See C-E02 | FAIL MINOR (C-E02) |
| E03 | Source anchor on every item (P07 L35-36) | Some rows anchored only to stage reports; three self-reported slips (B07 L461-464) | See C-E03 | FAIL MINOR (C-E03) |
| E04 | NO EVIDENCE FOUND stated; no force-fit (P07 L39-40) | 12 categories stated NO EVIDENCE FOUND (B07 L231-254) | As written | PASS |
| E05 | 22 categories + R1 = 23 scored rows (P07 L171-174; verifier rule 3) | 23 rows (B07 L288-310) | Counted 23 | PASS |
| E06 | Section 3 summary: 22 rows; Strong/Moderate count (P07 L155-157) | 22 rows; count 6 (B07 L231-256) | Counted 22 | PASS |
| E07 | Completionist guard; exact recount line (P07 L41-46, L157-159) | "📄 recount performed: 14 documented items across 9 categories" (B07 L258) | Present; 6 active, under 12 | PASS |
| E08 | Recount internally consistent | 14 items listed (B07 L259-264) across A1, B2, C1, E2, F2, G1, G2, H2, R1 | 14 items, 9 categories; evidence_mix documented 14 | PASS |
| E09 | Raw score from the likelihood x impact matrix (P07 L171-172) | 11 non-zero rows (B07 L288-310) | A1 MM 2, A3 ML 1, B2 HM 3, C1 MM 2, E2 HM 3, F1 ML 1, F2 MM 2, G1 HM 3, G2 MM 2, H2 HM 3, R1 ML 1: all match | PASS |
| E10 | Multiplier where the load-bearing items sit on one tier (P07 L173) | A3 0.7, B2 0.7, C1 0.7, F2 1.0, G1 1.0, G2 0.5, H2 1.0, R1 0.7 | Each matches the tier of the items that carry the score | PASS |
| E11 | Multiplier where items sit on more than one tier (P07 L173) | A1 1.0, E2 0.7, F1 0.7 | No stated convention; A1 and E2 cannot share one | FAIL MINOR (C-E11) |
| E12 | No 🎙️-only category scored as 📄 (verifier rule 3) | 1.0 weights on A1, F2, G1, H2 | Each carries 📄 items in its own table | PASS |
| E13 | Adjusted total (P07 L174) | 18.7 (B07 L311-313) | Re-added: 18.7 | PASS |
| E14 | Band; UA qualifier (P07 L175-180) | MODEST; EM >= 25 not met (B07 L315) | 18.7 in 12-24 | PASS |
| E15 | I1/I2 contribution stated separately (P07 L180-181) | 0.0 of 18.7 (B07 L314) | As written | PASS |
| E16 | Category 21 I1 gate: both legs; 📄 on leg (b) for top band (P07 L122-138; verifier rule 8) | 0; leg (a) a hiring story, leg (b) no evidence (B07 L220) | As written | PASS |
| E17 | Category 22 I2 gate: 0 when nothing must be destroyed (P07 L139-153; verifier rule 8) | 0 (B07 L222-227) | As written | PASS |
| E18 | I2 question answered for each moat claimed (P07 L140-142) | Answered for B2, H2, A1, C1 (B07 L223-226) | Seven scored categories unanswered | FAIL MINOR (C-E18), I2 stays 0 |
| E19 | Single-credit rule (B07 L86; CLAUDE.md one improvement, one mechanism) | Stated allocation honoured | No fact carries weight in two categories; the Siemens 2012 licence row sits in A1 and H2 but neither weight rests on it (B07 L288, L306). Tier mismatch logged under C-E02 | PASS |
| E20 | Section 1: 1A status set and columns, 1B five directions, 1C table (P07 L48-55) | B07 L21-50 | Present | PASS |
| E21 | Section 2: 2A columns, 2B, 2C arithmetic shown, 2D (P07 L57-63) | B07 L54-82 | 50 x 6.59 = 329.6 cr; 329.6 / 1,856.2 = 17.8% (B07 L72-73) | PASS |
| E22 | capex_embedded_growth_pct equals 2C | 17.8 (block) | 17.8 = 17.8 (B07 L73) | PASS |
| E23 | Section 4: 4A, 4B (amount, duration, enrolment, sharing), 4C (P07 L161-168) | B07 L267-280 | Present, NOT FOUND where absent | PASS |
| E24 | Optionality register: table, four columns, in the block (P07 L183-196) | 11 rows in report (B07 L319-331) and block | Present. See O9 on the admission rule | PASS |
| E25 | Section 6A, 6B, 6C, 6E (P07 L198-210) | 6A four windows; 6B covers all six active categories; 6C (B07 L358-361) | 6C core 45, 5 moats STRONG, AVERAGE equal B01 L95-102 | PASS |
| E26 | 6D combined classification per the standard matrix (P07 L203-205) | AVERAGE; FLAG-EM-MATRIX-ABSENT raised (B07 L364) | P07 names the matrix and does not carry it | NOT VERIFIABLE, not counted |
| E27 | active_categories = Strong/Moderate rows only (P07 L227) | 6 rows (block) | Equal to Section 5 Strong/Moderate rows | PASS |
| E28 | Block schema; analyst_note <= 200 words (P07 L216-243) | All fields; note about 136 words | As written | PASS |
| E29 | EM scan not conflated with FTTCP (P07 L3-6; CLAUDE.md) | "It is not FTTCP" (B07 L3) | As written | PASS |

Emerging Moat tally: 28 checked, 24 passed, 4 failed (E02, E03, E11, E18). E26 not verifiable.

### 3a. EM score robustness across consistent multiplier conventions

| Convention | Changed rows | Adjusted total | Active categories | Band |
| --- | --- | --- | --- | --- |
| As scored by stage 7 | none | 18.7 (B07 L311) | 6 | MODEST |
| Defining claim sets the tier | A1 2 x 0.7 = 1.4; E2 3 x 0.5 = 1.5 | 17.5 | 4 (G1, H2, B2, F2) | MODEST |
| Any 📄 item sets the tier | B2 3.0; C1 2.0; E2 3.0; F1 1.0; G2 2.0; R1 1.0 | 22.7 | 8 | MODEST |

Every row is in the 12-24 band and below the EM >= 25 UA qualifier. The I1/I2 contribution stays 0.0 in every row.

## 4. Findings

### C-G05 (MAJOR). B01 Block A. ROCE formula substituted; formula gaps handled two ways

- Rule. "FORMULA DEFINITIONS (fixed, do not substitute alternatives)". "ROCE = EBIT ÷ (Total Assets − Current Liabilities) ... If the data source provides its own ROCE (screener.in does), use the source's figure and anchor it; compute only when absent" (P01 L27-31). "If a data point is not available, mark it 'NOT FOUND' and score it 0" (P01 L20-21).
- Applied. "Capital employed = Equity share capital + Reserves + Borrowings (proxy, as current liabilities are not split in the Data Sheet)" (B01 L16). The proxy is disclosed and cross-checked at FY26 (1,083.37 vs 1,089.87 cr) and FY25 (871.94 vs 872.53 cr) (B01 L16).
- The same scorecard handled other gaps the strict way. Capex FY17-FY24 and trade payables FY17-FY24 scored NOT FOUND = 0 (B01 L44, L46). The FY25-FY26 two-year WC window was shown "reference only" and not scored (B01 L46). A substitution of the same kind existed for capex: net block and CWIP movement plus depreciation, from Data Sheet lines the stage already uses (net block 293.70, B01 L84; depreciation 22.99, B01 L62). The stage did not use it.
- Recomputed where the fixed formula can run: FY26 333.72 / 1,083.37 = 30.8% (proxy 30.6%). FY25 239.36 / 871.94 = 27.5% (proxy 27.4%). No band changes in A2, A4 or M3. A1 (14.6%) moves a band only if FY21 and FY22 capital employed sits about 2.8% below the proxy. The testable gaps are 0.07% (FY25) and 0.60% (FY26).
- Reading 1, applied by the stage. A disclosed proxy that agrees with the fixed formula where both exist is acceptable. Block A 8, core 45, AVERAGE.
- Reading 2, the letter of P01 L20-21 and L27-31, applied the way the stage applied it to payables. ROCE is NOT FOUND for FY17-FY24. A1 = 0, A2 = 0, A4 = 0. Block A = 2. Core = 2 + 1 + 9 + 19 + 8 = 39, which is AVOID (P01 L149). If capex were proxied the way ROCE was, B2 <= 2 and B3 <= 3, core <= 50, AVERAGE.
- Separating observation. The screener ROCE row for FY17-FY26, the prompt's first-choice source (P01 L30). It settles A1, A2 and A4 with no proxy. Without it, an operator ruling is needed on whether a cross-checked proxy may replace a fixed formula when a Data Sheet line is unsplit. The ruling should apply to ROCE and capex alike.
- Severity MAJOR. The rule was not applied as written. The testable evidence supports the proxy values. The classification changes only under Reading 2, and that reading is the operator's to rule, so it is flagged here and not graded as a confirmed decision change.
- Downstream reach. B07 6C and 6D take core 45 and AVERAGE from B01 (B07 L358-364). A Reading 2 ruling would change both.

### C-G03 (MINOR). B01. Extracted numbers not shown

- Rule. "Show every number you extract and the score for each metric" (P01 L14).
- Applied. The report prints derived values: ROE % (B01 L32), the CFO series and a PAT sum only (B01 L42), EBITDA margin % (B01 L78), and window CAGRs (B01 L92). The per-year revenue, PAT, depreciation, other income, selling and admin and net worth are not printed.
- Effect. C3 "9 of 9" (B01 L54), the PAT sum 758.50 (B01 L42), the margin series, the ROE series and the M11 CAGRs cannot be re-derived from the report. No score change is shown.
- Fix. Print the annual revenue, PAT, depreciation, other income and selling-and-admin rows with the screener-data anchor.

### C-G13 (MINOR). B01 C2. Synthetic CAGR printed

- Rule. "If PAT swung from loss to profit across the window, additionally note ...; do not attempt a synthetic CAGR" (P01 L47-49).
- Applied. "FY20 to FY26 (6 yrs, 29.94 to 238.77) is 41.3%, shown for information only" (B01 L53). A CAGR re-windowed to avoid a negative endpoint is the synthetic CAGR the rule bars.
- Effect. No score change (C2 0, C4 0). The block does not carry the figure.
- Recomputed. C2 reads N/M only. Strike the 41.3% line, so no later stage anchors a base case on it (CLAUDE.md: never anchor a base case to the audited past).

### C-G45 (MINOR). B01 M8. Floor band misread

- Rule. "M8 Distribution: ... mentioned unquantified = 1 | none or purely digital = 0" (P01 L120-122).
- Applied. 0, on "no quantified reach in provided numbers" (B01 L89). The 1-band scores a mention with no number. A missing number does not make the network "none".
- Evidence in the run. The stage read the AR (it cites AR p.194, p.198, p.230, p.238). That AR names sales offices in Frankfurt, Ohio and Japan (AR p.9, per B07 L38) and 68 service centres (AR p.11, per B07 L133). Network growth is not evidenced, so bands 3 and 5 fail.
- Recomputed. M8 = 1. Moat score 26, grand total 71. Moats present stay 5, class STRONG, classification AVERAGE.
- Verifier A should confirm the two AR anchors. If the operator reads M8 as a consumer-channel test only, 0 stands.

### C-E02 (MINOR). B07. Evidence taxonomy not on every item

- Rule. The taxonomy is "applied to every single piece of evidence" (P07 L29). Each category gets an "evidence table or NO EVIDENCE FOUND" (P07 L66-67).
- Untagged items. F1: ESAR grants (AR p.38) and the R&D and senior-management bullet (B07 L165-166). G2: four bullets under one category-level 🔍 (B07 L196-200). 4B policy text (B07 L278).
- No evidence table. A3, F1 and G2 use prose or bullets (B07 L104, L162-167, L195-200).
- One fact, two tiers. The Siemens 2-pole licence (2012) is 📄 in A1 (B07 L96, AR p.10; Pres. slide 5) and 🎙️ in H2 (B07 L211, Pres. slide 5; B04).
- Effect. No weight rests on the untagged items or on the licence row (A1 weight basis B07 L288; H2 weight basis B07 L306). No score change.

### C-E03 (MINOR). B07. Weak and wrong anchors

- Rule. Anchors take the form (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __) (P07 L35-36).
- Rows anchored only to an upstream stage report: the F2 "Misses" row, tagged 📄, anchor "B05" (B07 L177); F1 senior-management events, "(B08)" (B07 L166); the 2A prior-year guide of Rs 120 cr, "(B03)" (B07 L58).
- The orchestrator errata records three anchor slips the stage reported itself (B07 L461-464). Slip 2 attributes an analyst's question to management as a 🎙️ claim (B07 L46).
- Effect. No score depends on any of them (B07 L461). No score change.

### C-E11 (MINOR). B07 Section 5. Mixed-tier multiplier convention unstated and uneven

- Rule. Three discrete weights: 📄 1.0, 🎙️ 0.7, 🔍 0.5 (P07 L173). P07 gives no rule for a category whose items sit on more than one tier. The stage states no convention.
- A1 takes 1.0 on 📄 items that prove capability. The rarity A1 scores rests on 🎙️ wording and a NOT FOUND global manufacturer count (B07 L95-100).
- E2 takes 0.7, the 🎙️ weight. Its items are 📄 (exports) and 🔍 (the China+1 cause). The stage itself says management names a different cause (B07 L153-158).
- These two weights cannot follow one rule. Section 3a shows the recomputed range: 17.5 to 22.7, MODEST at every point, below EM 25 at every point.
- Separating observation for E2: a filed statement (customer, order filing or AR) that names supply moving away from China.
- Operator item. P07 L171-174 should state the mixed-tier rule.

### C-E18 (MINOR). B07 I2. Question not asked of every claimed moat

- Rule. "For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy in its own P&L or org to copy this?" (P07 L140-142).
- Applied. Answered for B2, H2, A1 and C1 (B07 L223-226). Not answered for G1 and E2 (active) or for A3, F1, G2 and R1 (Weak). F2 carries an execution-lead line in its own section (B07 L180).
- Effect. On the stage's own readings none of the unanswered categories names a sacrifice. Recomputed I2 = 0, unchanged.

## 5. Observations (no rule failure; for the operator or the orchestrator)

- O1. M4 reading (B01 L85). P01 L109-110 says "receivable days stable ±10" and names no window. The stage used endpoints (-8.3 days) and disclosed the interim range of 99.5 to 181.8 and the FY25 to FY26 rise of 21.1. On a range reading, M4 = 3: still present, moat score -2, class unchanged.
- O2. M3 year (B01 L84). P01 L107 names no ROCE year. The stage used FY26 (30.6%). On the median ROCE (14.6%), M3 = 1: moats present 4, still STRONG. With O1, O3 and C-G45 on their strict readings together, the moat score is 18, 4 moats present, STRONG, and the classification stays AVERAGE.
- O3. M11 basis (B01 L92). The stage used "selling and admin" for "selling exp %". The report shows it, but block data_notes say "selling %" and do not list it as a proxy (P01 L189). Selling % is 4.03 (FY23) and 3.86 (FY26) with FY25 at 4.42. On a strict trend reading, the 3-band applies (CAGR >= 20%, selling % stable): still present.
- O4. D block dates (B01 L60-65). D1 and D2 use FY26. D3 and D4 use 30 Sep 2026. Every band is the same on both dates.
- O5. Band edges for Verifier A's mandatory tier: A3 12.1% (0.1pp above 12.0), A1 14.6% (0.4pp below 15.0), E4 14.71% (0.29pp below 15.0), C1 19.3% (0.7pp below 20.0). None moves the class alone (Section 2a).
- O6. block_b_trend "improving" (B01 block) starts from the FY25 trough. FY24 CFO / PAT is 84.00 / 118.35 = 71.0% (B01 L42, L107). So FY24 to FY26 runs 71.0%, 22.6%, 54.1%. The H1 FY27 100.8% rests on +297.65 cr of other payables of NOT FOUND nature (B01 L11). The field names no window, so this is not a rule failure. A later FLAG-CASH reader should not take "improving" as resolved cash conversion.
- O7. Corpus question for the orchestrator. B07 L58 cites a prior-year AR through B03. If the FY25 AR is in the corpus, FY24 capex, payables, total assets and current liabilities exist. That changes the C-G05 picture and the B2-B4 windows. I cannot check this from my inputs.
- O8. G1 and G2 both draw on the H1 FY27 rise in other current liabilities: a caveat in G1 (B07 L193), "customer advances up" in G2 (B07 L197). G1's basis (nil borrowings, AA-, Rs 675 cr equity, B07 L188-190) does not need it, so I find no double credit. If a later stage cites the H1 cash build as G1 strength, that would credit the advances twice.
- O9. Operator item, P07 text. The register takes items that "rest only on 🎙️/🔍 evidence" (P07 L184) and says they are "watched, never scored" (P07 L195-196). But P07 L173 scores 🎙️ items at 0.7. So the INNIO commitment (B2), Business Excellence (A3), the service flywheel (C1) and the motor qualifications (R1) sit both in scored rows and in the register. The register row "Cash quality of the war chest" (B07 L331) is a check on a 📄-scored category (G1), not an optionality. It does no harm, because it lands in the monitoring checklist. P07 should say which reading binds.
- O10. Operator item, P07 text. P07 L203-205 names a "standard matrix" with eight labels and does not carry the matrix. Stage 7 flagged this (FLAG-EM-MATRIX-ABSENT). The combined label AVERAGE is NOT VERIFIABLE in phase-1 scope. Put the matrix in P07 or name its source file.
- O11. B07 1A item 4 labels the API 541 motors "LAUNCHED-recent" while volume waits for customer approvals (B07 L26). "IN TRIALS" or "REGULATORY PENDING" fits the stated facts better. The A1 weight is unaffected, because the Rs 192 cr order is 📄 on its own (B07 L94).
- O12. Cross-report number, Verifier A domain. Promoter holding at 30 Sep 2026: B07 L15 gives 26.5% (Pres. slide 36). B01 L12 gives 27.16% (Reg 31 p.3) and calls 26.51% a post-QIP figure. E1 = 0 on either value.
- O13. The B07 report no longer ends with its YAML block, because the orchestrator errata follows it (B07 L460-464). The block file is intact and identical. No action.

## 6. Rules not in phase-1 scope

| Verifier C rule | Reason not checked here |
| --- | --- |
| 4, 5 (valuation audit and its severity rule) | B11 not among inputs; phase 3 |
| 6 (B09 downstream candidates; stage 11 catalysts) | B09 and B11 not among my phase-1 inputs |
| 7 (method plurality in B11) | Phase 3 |
| 9 (Business Understanding Narrative, stage 13) | Stage 13 not run |
| 10 (B09b dossier) | Fires at the /finalize verifier pass; phase-1 check is mechanical in run-pipeline step 6b |
| 11, 12 (Role 1 exit construction; Amendment 19 FV path) | Phase 3 |
| 13, 14 (Expectation Ledger; ledger and decomposition gates) | Phase 3 |
| 15 (section-1b skill-to-source fidelity) | Valuation scope only |

## 7. Block

```yaml
stage: B12c
company: "TDPOWERSYS"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "PHASE 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation half (B10, B11) pending phase 3"
gate0: {rules_checked: 55, passed: 51, fails: ["G03 show-every-number (P01 L14): per-year revenue, PAT, depreciation, other income, selling and admin not printed; C3, PAT sum, margins, ROE and M11 CAGRs not re-derivable; no score change (MINOR)", "G05 ROCE formula substituted (P01 L27-31): proxy CE = equity + reserves + borrowings (B01 L16) while capex and payable gaps scored NOT FOUND = 0; strict reading gives Block A 2, core 39, AVOID; proxy reading core 45, AVERAGE (MAJOR)", "G13 synthetic CAGR printed (P01 L49): FY20-FY26 PAT CAGR 41.3% at B01 L53; C2 should read N/M only; no score change (MINOR)", "G45 M8 scored 0 (P01 L120-122): network mentioned in the AR (p.9, p.11 per B07 L38, L133); recomputed M8 1, moat score 26, grand total 71; class unchanged (MINOR)"], classification_check: "AVERAGE concurs on the stage's disclosed-proxy reading; AVOID (core 39) on the strict NOT FOUND reading of P01 L20-21 and L27-31; separating observation: screener ROCE row FY17-FY26, or an operator ruling on proxies applied to ROCE and capex alike; upside ceiling core 58, so AVERAGE cannot rise"}
emoat: {rules_checked: 28, passed: 24, not_verifiable: ["E26 6D combined classification: P07 L203-205 names a standard matrix it does not carry; combined AVERAGE unverified"], fails: ["E02 taxonomy not on every item (P07 L29, L66-67): F1, G2 and 4B items untagged; A3, F1, G2 without evidence tables; Siemens 2012 licence documented in A1 and claim in H2; no score change (MINOR)", "E03 anchors (P07 L35-36): rows anchored only to B03, B05, B08 (B07 L58, L166, L177); three self-reported slips in the errata (B07 L461-464); no score change (MINOR)", "E11 mixed-tier multiplier convention unstated and uneven (P07 L173): A1 1.0 vs E2 0.7; consistent conventions give 17.5 to 22.7, all MODEST, all below EM 25 (MINOR)", "E18 I2 question answered for B2, H2, A1, C1 only (P07 L140-142); G1, E2, A3, F1, G2, R1 unanswered; I2 stays 0 (MINOR)"], em_score_check: "18.7 MODEST concurs; 17.5 to 22.7 under consistent multiplier conventions; I1/I2 0.0 in every case"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}
expectation_ledger: {status: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "PENDING (rule 9 checks the stage 13 synthesis)", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # pending phase 3 (valuation scope)
recomputed_decision: ""        # pending phase 3 (valuation scope); the Gate 0 class question sits in gate0.classification_check
findings:
  - {id: "C-G05", block: "B01", rule: "P01 L20-21, L27-31: ROCE formula fixed; NOT FOUND scores 0", severity: MAJOR, issue: "Proxy capital employed replaces Total Assets less Current Liabilities (B01 L16); capex and payable gaps in the same scorecard scored NOT FOUND = 0 (B01 L44, L46)", recomputed: "AR basis FY26 30.8%, FY25 27.5% vs proxy 30.6%, 27.4%; no band change on the proxy reading; strict reading Block A 2, core 39, AVOID; operator ruling or screener ROCE row separates"}
  - {id: "C-G03", block: "B01", rule: "P01 L14: show every number extracted", severity: MINOR, issue: "Per-year revenue, PAT, depreciation, other income, selling and admin, net worth not printed (B01 L32, L42, L78, L92)", recomputed: "none possible; no score change shown"}
  - {id: "C-G13", block: "B01", rule: "P01 L47-49: no synthetic CAGR after a loss-to-profit swing", severity: MINOR, issue: "FY20-FY26 PAT CAGR 41.3% printed for information (B01 L53)", recomputed: "C2 N/M only; strike the 41.3% line; scores unchanged"}
  - {id: "C-G45", block: "B01", rule: "P01 L120-122: M8 mentioned unquantified = 1", severity: MINOR, issue: "M8 scored 0 on no quantified reach (B01 L89) though the AR names sales offices and 68 service centres (AR p.9, p.11 per B07 L38, L133)", recomputed: "M8 1; moat score 26; grand total 71; moats present 5, STRONG, AVERAGE unchanged"}
  - {id: "C-E02", block: "B07", rule: "P07 L29, L66-67: taxonomy on every item; evidence table per category", severity: MINOR, issue: "F1, G2, 4B items untagged; A3, F1, G2 lack evidence tables; Siemens 2012 licence on two tiers (B07 L96, L211)", recomputed: "no score change"}
  - {id: "C-E03", block: "B07", rule: "P07 L35-36: primary-source anchor on every item", severity: MINOR, issue: "Rows anchored only to B03, B05, B08 (B07 L58, L166, L177); three self-reported anchor slips (B07 L461-464)", recomputed: "no score change"}
  - {id: "C-E11", block: "B07", rule: "P07 L173: evidence multipliers 1.0, 0.7, 0.5", severity: MINOR, issue: "No mixed-tier convention stated; A1 1.0 on capability items while rarity is claim-tier; E2 0.7 on documented and inference items (B07 L95-100, L153-158)", recomputed: "17.5 (defining claim) to 22.7 (any documented item); MODEST throughout; EM 25 unmet"}
  - {id: "C-E18", block: "B07", rule: "P07 L140-142: I2 question for each moat claimed", severity: MINOR, issue: "Answered for B2, H2, A1, C1 only (B07 L223-226)", recomputed: "I2 0, unchanged"}
critical_count: 0
major_count: 1
minor_count: 7
acceptance_rate: 90.4             # rules passed ÷ rules checked, % (75 of 83)
```
