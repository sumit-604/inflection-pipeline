# VERIFIER C (B12c): FRAMEWORK ADHERENCE, PHASE 1 SCOPE
Narmada Gelatines Ltd (SHAWGELTIN), run 2026-11-12. Model: claude-opus-5-5.

## Scope and inputs
- Scope: Gate 0 (B01) and Emerging Moat (B07) compliance only. The valuation audit (B10, B11) is pending phase 3. I did not read the valuation framework documents.
- Rule sources read: prompts/12-verifiers-pipeline.md (VERIFIER C section, L213-390), prompts/01-gate-0-pipeline.md (P01), prompts/07-emerging-moat-pipeline.md (P07).
- Artifacts read: outputs/reports/01-gate0.md (R01), outputs/blocks/B01-gate0.yaml (Y01), outputs/reports/07-emoat.md (R07), outputs/blocks/B07-emoat.yaml (Y07).
- Not read: any other verifier output, any source PDF, B02, B03, B05, B09. Numbers are re-derived only from figures the two artifacts state. Verifier A owns whether a number exists in a source.
- Anchor format in this report: (file, line). P01 and P07 lines are rule lines.
- Stuck rule: not triggered.

## Summary
- 102 rules checked. 87 passed. Acceptance rate 85.3% (above 60%, denominator 102, applicable).
- Gate 0: 59 rules, 54 passed (91.5%). 1 MAJOR, 3 MINOR findings.
- Emerging Moat: 43 rules, 33 passed (76.7%). 1 MAJOR, 7 MINOR findings.
- CRITICAL: 0. No REWORK trigger from this verifier.
- Gate 0 classification GOOD re-derives exactly (core 60, moat THIN, DB1 only). Core 60 sits on the GOOD floor. See O-G0-1.
- em_score 11.7 re-derives on the maker's tiers. The NONE band is not stable. The F2 tier is wrong as written. Corrected alone, it gives 12.0, which is MODEST. See F-EM-1 and the recomputation table.

---

## GATE 0 (B01) COMPLIANCE TABLE

| ID | Rule (source) | B01 value (anchor) | Recomputed | Result |
|---|---|---|---|---|
| G0-01 | Opening data line, history adaptation (P01 L23-25) | 12 years FY2015 to FY2026 (R01 L3) | 12 years, full | PASS |
| G0-02 | Anchor on every number (P01 L14-18) | Anchors present except M3 denominator (R01 L57) | See F-G0-3 | FAIL MINOR |
| G0-03 | NOT FOUND scored 0, no estimates (P01 L19-22) | M6, M7, M8 NOT FOUND = 0; M2, M5, M9 PEER DATA NEEDED = 0 (R01 L56-63) | Same | PASS |
| G0-04 | ROCE: use source's own figure (P01 L29-31) | Screener ROCE row (R01 L12; Y01 L26) | Same | PASS |
| G0-05 | ROE on average net worth, FY15 closing stated (P01 L32-33) | 15.4, 7.5, 5.3, 6.6, 7.8, 9.7, 5.8, 8.5, 12.6, 14.8, 14.9, 21.5 (R01 L22) | All 12 reproduce from R01 L11, L13 | PASS |
| G0-06 | WC days formula and stated basis (P01 L34-38) | "sales basis" (Y01 L27; R01 L78) | Basis not supportable. See F-G0-2 | FAIL MINOR |
| G0-07 | FCF = CFO minus capex (P01 L39-40) | Screener FCF row (Y01 L28) | Stated | PASS |
| G0-08 | CAGR formula, full available window (P01 L41, L23) | 11 years FY15 to FY26 (R01 L33-34) | Same | PASS |
| G0-09 | CAGR edge rules (P01 L45-50) | All endpoints positive; no loss-to-profit swing (Y01 L34) | No N/M case | PASS |
| G0-10 | A1 median ROCE (P01 L55) | 11.5% = 1 (R01 L20) | (11 + 12) / 2 = 11.5; band 10-14.9 = 1 | PASS |
| G0-11 | A2 minimum ROCE (P01 L56) | 4% FY17 = 0 (R01 L21) | below 8 = 0 | PASS |
| G0-12 | A3 median ROE (P01 L57) | 9.1% = 0 (R01 L22) | (8.45 + 9.74) / 2 = 9.1; below 12 = 0 | PASS |
| G0-13 | A4 ROCE trend (P01 L58-59) | 28 vs 21 = 5 (R01 L23) | latest above earliest = 5 | PASS |
| G0-14 | Block A total | 6 (R01 L19) | 1 + 0 + 0 + 5 = 6 | PASS |
| G0-15 | B1 cumulative CFO / PAT (P01 L62-63) | 122 / 156 = 0.78 = 2 (R01 L26) | Sums reproduce from R01 L11, L14; 0.782; band 0.70-0.84 = 2 | PASS |
| G0-16 | B2 FCF-positive years (P01 L64) | 11 of 12 = 4 (R01 L27) | FY21 "-0" is not positive; 91.7%; band 75-99 = 4 | PASS |
| G0-17 | B3 cumulative FCF / PAT (P01 L65-66) | 79 / 156 = 0.51 = 3 (R01 L28) | 0.506; band 0.40-0.59 = 3 | PASS |
| G0-18 | B4 WC days change (P01 L67-68) | 214 to 166, down 48 = 5 (R01 L29) | 41 + 194 - 21 = 214; 49 + 156 - 39 = 166 (R01 L16); down more than 5 = 5 | PASS |
| G0-19 | Block B total | 14 (R01 L25) | 2 + 4 + 3 + 5 = 14 | PASS |
| G0-20 | C1 revenue CAGR (P01 L71) | 4.4% = 0 (R01 L33) | (215/134)^(1/11) - 1 = 4.39%; below 5 = 0 | PASS |
| G0-21 | C2 PAT CAGR (P01 L72) | 5.2% = 1 (R01 L34) | (28/16)^(1/11) - 1 = 5.22%; band 5-9.9 = 1. See O-G0-1 | PASS |
| G0-22 | C3 positive YoY years (P01 L73) | 8 of 11 = 1 (R01 L35) | Declines FY16, FY17, FY24 reproduce (R01 L9); 72.7%; band 50-74 = 1 | PASS |
| G0-23 | C4 PAT CAGR minus revenue CAGR (P01 L74) | +0.8pp = 3 (R01 L36) | 5.22 - 4.39 = +0.83pp; within 3pp = 3 | PASS |
| G0-24 | Block C total | 5 (R01 L32) | 0 + 1 + 1 + 3 = 5 | PASS |
| G0-25 | D1 net debt / EBITDA (P01 L77-79) | 0.09x = 4 (R01 L39) | 789.08 - 11.32 - 397.16 = 380.60 lakh; 3.81 / 41 = 0.09x = 4. Without bank balances: 7.78 / 41 = 0.19x, still 4 | PASS |
| G0-26 | D2 EBIT / interest (P01 L80-82) | 38.5x = 5 (R01 L40) | (3,819.16 + 101.87) / 101.87 = 38.49x | PASS |
| G0-27 | D3 debt / equity (P01 L83-84) | 0.06 = 5 (R01 L41) | 789.08 / 14,130.66 = 0.056 | PASS |
| G0-28 | D4 current ratio (P01 L85-86) | 3.59 = 5 (R01 L42) | 8,504.73 / 2,367.39 = 3.59 | PASS |
| G0-29 | Block D total | 19 (R01 L38) | 4 + 5 + 5 + 5 = 19 | PASS |
| G0-30 | E1 promoter holding (P01 L89-90) | 75.00% = 5 (R01 L45) | 60 or above = 5 | PASS |
| G0-31 | E2 promoter change over 3 years (P01 L91-92) | -2.65pp = 1, alt 3 disclosed (R01 L46; Y01 L29) | Nearest observed point to the 3-year date; both readings disclosed. See O-G0-1 | PASS |
| G0-32 | E3 pledge (P01 L93) | 0% = 5 (R01 L47) | Same | PASS |
| G0-33 | E4 contingent liabilities / net worth (P01 L94-95) | 1.7% = 5 (R01 L48) | 244.64 / 14,130.66 = 1.73% | PASS |
| G0-34 | Block E total | 16 (R01 L44) | 5 + 1 + 5 + 5 = 16 | PASS |
| G0-35 | Core score | 60 (R01 L50) | 6 + 14 + 5 + 19 + 16 = 60 | PASS |
| G0-36 | M1 pricing power (P01 L102-104) | 0 (R01 L55) | OPM +3pp but CAGR 4.4% below 10%; no band met | PASS |
| G0-37 | M2 cost advantage (P01 L105-106, L99-100) | 0 PEER DATA NEEDED (R01 L56) | Same | PASS |
| G0-38 | M3 capital efficiency (P01 L107-108) | 5 (R01 L57) | FAT above 3x and ROCE 28% above 20% on FY26 values. See F-G0-3, O-G0-2 | PASS |
| G0-39 | M4 customer stickiness (P01 L109-111) | 0 (R01 L58) | 3 decline years = 0 | PASS |
| G0-40 | M5 scale (P01 L112-113) | 0 PEER DATA NEEDED (R01 L59) | Same | PASS |
| G0-41 | M6 technology / R&D (P01 L114-116) | 0 NOT FOUND (R01 L60) | Same | PASS |
| G0-42 | M7 regulatory (P01 L117-119) | 0 NOT FOUND (R01 L61) | Same | PASS |
| G0-43 | M8 distribution (P01 L120-122) | 0 NOT FOUND (R01 L62) | Same | PASS |
| G0-44 | M9 brand (P01 L123-125) | 0 PEER DATA NEEDED (R01 L63) | Same | PASS |
| G0-45 | M10 switching costs (P01 L126-128) | 1 (R01 L64) | Overall growth, 2 or more decline years (3) = 1; receivable days 41 to 49 (R01 L16) | PASS |
| G0-46 | M11 network effects (P01 L129-133) | 0 (R01 L65) | Latest 3-yr 4.0% vs prior 12.5% (stated 12.6%, O-G0-3); CAGR 4.4% fails the 20% and 15% legs | PASS |
| G0-47 | M12 negative WC (P01 L134-135) | 0 (R01 L66) | Every series above 45 days in every year | PASS |
| G0-48 | Moat count and class (P01 L137-138) | 1, THIN (R01 L68) | 1 present = THIN | PASS |
| G0-49 | Moat score and grand total | 6; 66 (R01 L68, L71) | 5 + 1 = 6; 60 + 6 = 66 | PASS |
| G0-50 | Data confidence, history downgrade (P01 L142-144) | 12 years full; history_downgrade false (Y01 L23) | 10 or more years = full | PASS |
| G0-51 | Classification matrix (P01 L146-149) | GOOD (R01 L71) | Core 60-79 plus THIN = GOOD | PASS |
| G0-52 | Deal-breakers 1-9, years named (P01 L151-159) | DB1 only, FY16-FY22 named (R01 L72; Y01 L21-22) | DB1 fires (A = 6 below 8, max GOOD). DB2 to DB9 do not fire: B 14, median ROCE 11.5, CFO/PAT 0.78, pledge 0, ND/EBITDA 0.09x, 3 of 11 declines, PAT positive FY24-FY26, 12 years | PASS |
| G0-53 | FLAG-GATE0 rule (P01 L175-177) | flags: [] (Y01 L11) | Not required at GOOD | PASS |
| G0-54 | block_b_trend with one number (P01 L191-192) | "stable" with two numbers (Y01 L35) | See F-G0-1 | FAIL MAJOR |
| G0-55 | data_notes contents (P01 L189-190) | Swings, proxies, PEER DATA NEEDED (Y01 L24-34) | Present | PASS |
| G0-56 | analyst_note 200 words or fewer (P01 L193-197) | About 120 words (Y01 L36) | Within cap | PASS |
| G0-57 | Dashboard elements (P01 L163-165) | Table, no moat profile bars (R01 L52-68) | See F-G0-4 | FAIL MINOR |
| G0-58 | Report ends with the exact block (P01 L165-166) | Abridged block, then a pointer line (R01 L84-110) | See F-G0-4 | FAIL MINOR |
| G0-59 | Block file schema (P01 L168-198) | All keys present (Y01 L1-36) | Complete | PASS |

### Gate 0 findings

**F-G0-1 MAJOR (G0-54). block_b_trend ratio and label.**
- Claimed: "FY26 CFO/EBITDA 79% vs 92% FY25", label "stable" (Y01 L35). The same 79% is in the load-bearing fact check (R01 L77).
- Recomputed on the report's own SA rows: FY26 CFO 25 / EBITDA 41 = 61% (R01 L14, L39). FY25 CFO 17 / (sales 189 x OPM 13% = 24.6) = 69% (R01 L9, L10, L14). Neither stated value reproduces.
- [INFERENCE] The FY26 value fits a post-tax denominator. Tax = PBT 38.19 Cr minus PAT 28 Cr = 10.2 Cr (R01 L40, L11). CFO 24.56 Cr / (41 - 10.2) = 80% (R01 L30). The FY25 leg cannot be tested: FY25 PBT is not in the report.
- The field asks for "the one number that shows it" (P01 L191-192). The field gives two numbers that point in opposite directions. Three-year CFO/PAT 0.95 against 12-year 0.78 reads improving. CFO/EBITDA falling reads deteriorating. Single-year CFO/PAT 1.00 FY25 (17/17) to 0.89 FY26 (25/28) also reads deteriorating (R01 L11, L14). No single number shows "stable".
- Effect: no score or classification changes. The field feeds FLAG-CASH, and cash conversion is a load-bearing fact for this run. Restate the ratio as 61% and 69%, or relabel it as CFO / (EBITDA minus tax). Then pick one label with its one number. Whether any source shows 79%: Verifier A.

**F-G0-2 MINOR (G0-06). Inventory-days basis label.**
- Claimed: inventory days 156 "sales basis" (R01 L78; Y01 L27; Y01 L36).
- Test: 156 / 365 x Rs 215 Cr = Rs 91.9 Cr of inventory. FY26 total current assets are Rs 85.05 Cr (8,504.73 lakh, R01 L42). Inventory cannot exceed total current assets on a closing-balance sales basis. B07 labels the same 156 days "on cost" (R07 L66).
- Rule: state which basis was used (P01 L34-38). The stated basis is not supportable.
- Effect: B4 = 5 holds on both the CCC series (214 to 166) and the screener WC Days series (117 to 97) (R01 L29). M12 = 0 holds on every series. Inventory days is a load-bearing fact (R01 L78). Correct the label before stage 11 reads it.

**F-G0-3 MINOR (G0-02). M3 denominator anchor.**
- Claimed: "FAT 215/41 = 5.2x, ROCE 28% (SA)" (R01 L57).
- The denominator 41 is not named as net block and has no line anchor. It equals the D1 EBITDA figure, Rs 41 Cr (R01 L39).
- Score is robust. B07 states FY26 closing gross block Rs 53.2 Cr (5,321.70 lakh, R07 L40). Net block cannot exceed gross block, so FAT is at least 215 / 53.2 = 4.04x, above 3x. M3 = 5 holds.
- Fix: name and anchor the fixed-asset line.

**F-G0-4 MINOR (G0-57, G0-58). Output format.**
- The dashboard has no moat profile bars (P01 L163-165; R01 L52-68).
- The report's closing YAML omits data_notes and analyst_note, and a pointer line follows it (R01 L84-110). The rule asks the report to end with exactly the block (P01 L165-166). The block file is complete (Y01 L1-36).

### Gate 0 observations (not findings)

**O-G0-1. Core 60 sits on the GOOD floor.** The GOOD band is core 60-79 (P01 L147-149). One point lost anywhere gives core 59, AVERAGE, and a required FLAG-GATE0, because historical depressors are already named (Y01 L22). Two scores sit near a line.
- E2 has three readings. (a) Maker: Dec-2023 77.65% to Sep-2026 75.00% = -2.65pp, score 1, a 2.75-year window (R01 L46). (b) Disclosed alternative: Mar-2023 75.00% base, change 0.00, score 3 (Y01 L29). (c) Strict rule 5: the Sep-2023 point is not available, so NOT FOUND and 0 (P01 L19-22). Reading (c) gives core 59 and AVERAGE.
- Audit view on E2: I keep the maker's reading. Rule 6 directs scoring on the available history (P01 L23-25). Observed points bracket the 3-year date (Mar-2023 and Dec-2023). The maker used the nearer one, which also gives the lower of the two observed scores, and disclosed both. The operator may rule otherwise. That ruling would move Gate 0 to AVERAGE.
- C2 is 5.22% against the 5% line, on whole-crore PAT (R01 L34). C2 drops to 0 only if FY26 PAT / FY15 PAT falls below 1.05^11 = 1.7103. B07 gives CFO/PAT 86.4% on CFO 2,455.67 lakh (R07 L66, L65). That implies FY26 PAT of about 2,842 lakh (Rs 28.42 Cr, derived). The flip threshold is then FY15 PAT above Rs 16.62 Cr. The top of the rounding interval for "16" is 16.49. C2 = 1 holds. The observation that settles it: unrounded FY15 PAT, NOT FOUND in my inputs.

**O-G0-2. M3 period basis.** The rule text does not say spot year or median (P01 L107-108). The maker used FY26 ROCE 28%. On the 12-year median ROCE of 11.5% (R01 L20), M3 = 0, because it fails even the FAT above 1x AND ROCE above 12% leg. Then moats = 0 (NONE), moat score 1, grand total 61. Classification stays GOOD (core 60-79 plus any class other than STRONG or FORTRESS). Downstream note: the one confirmed moat rests on a single year.

**O-G0-3. Cosmetic recomputes.** M11 prior window (191/134)^(1/3) - 1 = 12.5%, stated 12.6% (R01 L65). FY17 CCC 52 + 192 - 52 = 192, stated 193 (R01 L16-17). Neither changes a score.

---

## EMERGING MOAT (B07) COMPLIANCE TABLE

Tier names used here: documented (weight 1.0), claim (0.7), inference (0.5), per P07 L29-34 and L172-173.

| ID | Rule (source) | B07 value (anchor) | Recomputed | Result |
|---|---|---|---|---|
| EM-01 | Not FTTCP (P07 L3-6) | "It is not FTTCP" (R07 L3) | Same | PASS |
| EM-02 | All six sections in one response (P07 L28) | Sections 1-6 and register (R07 L8-176) | Present | PASS |
| EM-03 | Section 1: 1A status, 1B directions, 1C mix (P07 L48-55) | R07 L10, L13-19, L22-26 | Present | PASS |
| EM-04 | 2A capex table (P07 L58-59) | 2 rows, 7 columns (R07 L31-34) | Present | PASS |
| EM-05 | 2B utilisation per facility (P07 L59-60) | One site, NOT FOUND (R07 L37) | Present | PASS |
| EM-06 | 2C arithmetic shown (P07 L60-63) | 4,773.44; 4.51x; 69.1% (R07 L40) | 21,541.15 / 4,773.44 = 4.513x; 3,300 x 4.513 = 14,892 lakh = 69.1% | PASS |
| EM-07 | Block field from 2C (P07 L233) | 22 (Y07 L26) | See F-EM-4 | FAIL MINOR |
| EM-08 | 2D new geography (P07 L63) | None named (R07 L45) | Present | PASS |
| EM-09 | 22 categories addressed or NO EVIDENCE FOUND (P07 L66-67) | 22 of 22 (R07 L51-71) | Complete | PASS |
| EM-10 | R1 Section 4, 4A to 4C (P07 L161-168) | R07 L103-105 | Present | PASS |
| EM-11 | Evidence tier per taxonomy definition (P07 L29-34) | F2 claim tier (R07 L64) | See F-EM-1 | FAIL MAJOR |
| EM-12 | One weight basis for mixed-tier categories | A3 vs H1, H2 (R07 L53, L67, L68) | See F-EM-2 | FAIL MINOR |
| EM-13 | Source anchor on every evidence item (P07 L35-36) | Stage-report anchors (R07 L24-25, L55, L65, L66, L163) | See F-EM-7 | FAIL MINOR |
| EM-14 | No force-fit (P07 L39-40) | 13 categories NO EVIDENCE or 0 | Sparse, as the guard expects | PASS |
| EM-15 | Completionist guard (P07 L41-46) | 9 scored, below 12 (R07 L99) | Not triggered | PASS |
| EM-16 | Recount line in required form (P07 L157-159) | "7 documented items across 6 categories" (R07 L99; Y07 L19) | A3 x2, B2, E2, G1, H1, H2 = 7 items in 6 categories. See O-EM-3 | PASS |
| EM-17 | Summary table, 22 rows, all columns (P07 L155-156) | R07 L74-97 | 22 rows | PASS |
| EM-18 | Strong/Moderate count stated (P07 L156-157) | 0 of 22 (R07 L99) | Same | PASS |
| EM-19 | Likelihood x impact matrix values (P07 L171-172) | HL 2, MM 2, ML 1, LM 1 (R07 L111-119) | Matrix values reproduce | PASS |
| EM-20 | Likelihood x impact consistent with stated evidence | B2 MM (R07 L56, L113) | See F-EM-3 | FAIL MINOR |
| EM-21 | Multiplier arithmetic (P07 L172-173) | 9 rows (R07 L111-119) | All 9 reproduce | PASS |
| EM-22 | Adjusted total | 11.7 (R07 L123) | 2.0 + 1.4 + 2.0 + 0.7 + 1.0 + 0.7 + 2.0 + 0.5 + 1.4 = 11.7 | PASS |
| EM-23 | Band on the stated total (P07 L175-176) | below 12 = NONE (R07 L123) | Correct on the maker's tiers | PASS |
| EM-24 | Scoring table, all 23 rows (P07 L173-174) | 9 rows plus 2 grouped rows (R07 L111-121) | See F-EM-8 | FAIL MINOR |
| EM-25 | Family I contribution stated separately (P07 L180-181) | 0.0 (R07 L123) | Same | PASS |
| EM-26 | Category 21 present; above 0 only with both legs and a documented (b) leg (P07 L122-138; P12 L292-295) | 0, both legs absent (R07 L70) | Rule met | PASS |
| EM-27 | Category 22 present; above 0 only with a specific sacrifice (P07 L139-153; P12 L296-297) | 0 (R07 L71) | Rule met | PASS |
| EM-28 | I2 answered for each moat claimed (P07 L139-141) | 3 of 9 named (R07 L71) | See F-EM-5 | FAIL MINOR |
| EM-29 | One improvement, one mechanism | Solar and UF in A3 only; exports in E2 only; PJG in H2 consultancy only (R07 L49, L64, L69) | No double credit. A3 (power) and B1 (materials) are different cost lines. H1 (IGCL stake) and H2 (PJG stake in NGL) are different stakes | PASS |
| EM-30 | Register table form and block carry (P07 L183-196) | 6 rows, 4 columns; Y07 L27-33 | Present | PASS |
| EM-31 | Register coverage (P07 L184) | H1 absent | See F-EM-6 | FAIL MINOR |
| EM-32 | 6A timeline, four windows (P07 L199-200) | R07 L139-144 | Present | PASS |
| EM-33 | 6B risks with early warnings (P07 L200-201) | 5 rows (R07 L147-153) | Present | PASS |
| EM-34 | 6C uses the injected B01 (P07 L201-203) | 60; 6/1 THIN; 66 GOOD; DB1 (R07 L157-161) | Matches Y01 L14-22 | PASS |
| EM-35 | 6D label in set, reasoning given (P07 L203-208) | GOOD, turnaround reasoning (R07 L163) | Label in the set. Mapping NOT VERIFIABLE (O-EM-4) | PASS |
| EM-36 | 6E map per family (P07 L208-209) | Families A, B, C, E, F, G, H (R07 L166-174) | See F-EM-8 | FAIL MINOR |
| EM-37 | 6E catalysts and biggest risk (P07 L209-210) | R07 L175-176 | Present | PASS |
| EM-38 | Block schema (P07 L216-243) | All keys (Y07 L1-41) | Complete | PASS |
| EM-39 | em_classification value; active_categories only Strong/Moderate (P07 L226-228) | NONE; [] (Y07 L16-17) | Consistent with summary table | PASS |
| EM-40 | evidence_mix matches text | 7 / 5 / 3 (Y07 L18; R07 L99) | Matches | PASS |
| EM-41 | catalysts_12m fields (P07 L231-232) | 5 rows, all four fields (Y07 L21-25) | Present | PASS |
| EM-42 | analyst_note 200 words or fewer (P07 L239-242) | About 145 words (Y07 L41) | Within cap | PASS |
| EM-43 | Report ends with the exact block (P07 L214) | Abridged block, then a pointer line (R07 L178-191) | See F-EM-8 | FAIL MINOR |

### EM recomputation: band readings

The maker's likelihood x impact is held in every row. Only the tier or the named row changes.

| Reading | Rows changed (adjusted) | Total | Band (P07 L175-176) |
|---|---|---|---|
| Maker as filed | none | 11.7 | NONE |
| F2 at documented tier (as-written definition, F-EM-1) | F2 0.7 to 1.0 | 12.0 | MODEST |
| F2 at inference tier | F2 0.7 to 0.5 | 11.5 | NONE |
| H2 at documented tier (maker's own sensitivity, R07 L123) | H2 1.4 to 2.0 | 12.3 | MODEST |
| Uniform per-item convention (F-EM-2) | F2 1.0, H1 1.0, H2 2.0 | 13.1 | MODEST |
| Uniform weakest-link convention, maker's stated links (F-EM-2) | A3 1.0, F2 0.5 | 10.5 | NONE |
| B2 at LM (F-EM-3) | B2 2.0 to 1.0 | 10.7 | NONE |

Reading the table: the levers that raise the score are F2 (+0.3), H1 (+0.5) and H2 (+0.6). The levers that lower it are A3 (-1.0), B2 (-1.0) and F2 under weakest-link (-0.2). The band edge is 12. The scan sits on it under any reading. The maker's analyst note says the same: "treat NONE as the floor of a thin MODEST" (Y07 L41). The maker's band-edge flag names only H2 (Y07 L12).

### EM findings

**F-EM-1 MAJOR (EM-11). F2 tier contradicts the taxonomy definition.**
- Claimed: "F2 Execution moat ... claim weight ... Score ML x 0.7" (R07 L64). evidence_mix counts "Note 4 no-overrun statement" as a claim (R07 L99).
- Rule: the claim tier means "stated in concall or presentation, not yet backed by committed capital or signed contracts" (P07 L32-33).
- This run has no concall and no presentation (R07 L4). The F2 evidence is (i) a filed AR Note 4 statement that CWIP has no cost overrun or time delay, on capital already spent (R07 L64, AR Note 4 p.61), and (ii) an inference from CWIP movement: "so projects complete inside a year" (R07 L64). Item (i) is documented by definition. Item (ii) is inference by definition. Neither is a claim.
- Recomputed: F2 at documented = 1 x 1.0 = 1.0. Total 12.0 = MODEST. F2 at inference = 0.5. Total 11.5 = NONE.
- Effect: the as-written tier alone moves em_classification from NONE to MODEST. The band-edge flag (Y07 L12) does not name F2. The combined GOOD likely survives, because the 6D reasoning rests on the absence of EXPANSION (R07 L163), and MODEST is not EXPANSION. The destination-PE effect is NOT ASSESSABLE in phase 1, because Section 1B is not loaded. The phase-3 audit must test Pillar 3 on both NONE and MODEST. It must re-grade this finding to CRITICAL if the two readings move destination PE by more than 1x (P12 L280-282).

**F-EM-2 MINOR (EM-12). Mixed-tier weight convention is not uniform.**
- The rubric does not say how to weight a category whose items sit in more than one tier (P07 L171-174).
- The maker uses two conventions. A3 takes the documented weight. Yet its saving's attribution is inferred ("favours a company-specific effect"), and the MD&A credits coal price, not solar (R07 L53). H1 and H2 take the tier of the benefit link (inference, claim). Yet each holds a documented item: the IGCL stake (Note 6 p.62) and the PJG consultancy line (Note 37 p.73) (R07 L67, L68).
- Recomputed: uniform per-item convention gives 13.1 (MODEST). Uniform weakest-link convention gives 10.5 (NONE). See the table above.
- Effect: the band turns on a convention the rubric does not state. I recommend an operator ruling on mixed-tier categories. The maker should state the convention in the scorecard.

**F-EM-3 MINOR (EM-20). B2 likelihood x impact conflicts with the report's own text.**
- Claimed: B2 MM = 2 x 1.0 = 2.0 (R07 L56, L113).
- The same report says "Existing, retained, not new; no design-in or sole-source language" (R07 L56). It says "Table stakes, not a lock-in" (R07 L150). It says certifications "can be copied without destroying any P&L line" (R07 L71). The scan scores moats "currently FORMING that do not fully show in historical financials yet" (P07 L21-24).
- Recomputed: at LM, B2 = 1.0. Total 10.7 = NONE.
- Effect: the band does not change with this fix alone. I record it because the bar is symmetric. If F-EM-1 is applied, this finding must be weighed with it.

**F-EM-4 MINOR (EM-07). capex_embedded_growth_pct is not the 2C formula output.**
- Rule: 2C = capex under execution x historical fixed asset turnover, as % above current revenue. The block field is "from 2C" (P07 L60-63, L233).
- Formula: 3,300 lakh x 4.513x = 14,892 lakh = 69.1% of FY26 revenue 21,541.15 lakh (R07 L40). On the AR-documented spent or contracted base of 1,723.03 lakh (R07 L35): 7,776 lakh = 36.1%. The block carries 22, the capacity cross-check of 21.8% (R07 L42; Y07 L26).
- The maker discloses both figures with reasons (R07 L41-43; Y07 L41). The Rs 33 Cr base rests on a CARE claim (R07 L33).
- Effect: carry the formula figure, or label both in the block, so stage 11 does not read 22 as the 2C formula output.

**F-EM-5 MINOR (EM-28). I2 is not answered for each moat.**
- Rule: "For each moat claimed anywhere in this scan, answer" (P07 L139-141).
- The answer names three items: certifications, a solar plant and a group consultancy (R07 L71). That covers B2, A3 and H2 of nine scored categories. B1, C1, E2, F2, G1 and H1 are not tested.
- C1 matters most. The rubric counts "incumbents protected by decades-old institutional customer relationships" (P07 L145-147). The report records five decades of operation (R07 L51) and named capsule-maker customers with repeat orders (R07 L58).
- Effect: I2 = 0 likely holds. C1 rests on a claim only, and no specific sacrifice is named (P12 L296-297).

**F-EM-6 MINOR (EM-31). Optionality register omits H1.**
- Scope: forward advantages that "scored 0 or rest only on" claim or inference evidence (P07 L184).
- H1 rests on inference only (R07 L67) and is not registered (R07 L127-134; Y07 L27-33). F2, as the maker tiered it, rests on a claim and is not registered either. The maker registers other claim-tier categories (B1, C1, H2), so the omission breaks the maker's own pattern.
- Effect: monitoring gap only. Add H1.

**F-EM-7 MINOR (EM-13). Anchors cite stage reports or note numbers.**
- Rule: a source anchor on every evidence item (P07 L35-36).
- Examples: gelatine 70.8% "(B05 triggers 6, from Note 26)" and the DCP and gelatine price effects "(B03)" (R07 L24-25). Net price effect "+84 lakh of 1,540 lakh" (R07 L163). G2 payable days and CFO/PAT 86.4% "(B02 FLAG-WC)" (R07 L66). B1 raw-material stock "B03 Note 10" and G1 "Notes 18, 44", with no page (R07 L55, L65).
- Effect: weak anchors. Whether the figures exist in a source: Verifier A.

**F-EM-8 MINOR (EM-24, EM-36, EM-43). Output format.**
- The scorecard groups 14 zero categories into two rows (R07 L120-121). The rule asks for all 23 rows (P07 L173-174). Every category is still named.
- The 6E moat evolution map omits families D and I (R07 L166-174). The rule asks for the map per family (P07 L208-209).
- The report's closing YAML is abridged, and a pointer line follows it (R07 L178-191). The rule asks the report to end with exactly the block (P07 L214). The block file is complete (Y07 L1-41).

### EM observations (not findings)

**O-EM-1. 2A sum.** 528.97 + 1,205.00 = 1,733.97 lakh. The report states 1,723.03 lakh (R07 L33, L35). That is 52.5% against the stated 52% of Rs 33 Cr. No rule depends on it. Routed to Verifier A.

**O-EM-2. Page conventions.** B07 uses PDF pages, with printed page = PDF minus 3 (R07 L4). B01 uses printed pages (R01 L4). On those anchors, Note 35 sits at printed p.69 (B07, PDF p.72, R07 L33) and Note 36 at printed p.68 (B01, R01 L48). A higher note number sits on an earlier page. Routed to Verifier A.

**O-EM-3. Recount and summary row.** The summary row shows H2 as "claim (+documented stake)" (R07 L94). The 7-item recount lists only the H2 consultancy line (R07 L99). If the PJG stake counts as a separate documented item, the recount is 8 items in 6 categories. No score effect.

**O-EM-4. 6D matrix.** P07 names the label set (P07 L203-205) but does not define the mapping. GOOD is in the set. Whether GOOD plus MODEST maps to GOOD or GOOD+ is NOT VERIFIABLE from the rule source. This matters only if F-EM-1 is applied.

**O-EM-5. Cross-stage FAT.** B01 M3 uses FAT 5.2x on a denominator of 41 (R01 L57). B07 2C uses 4.51x on average gross block (R07 L40). The bases differ and B07 states its basis. No rule conflict. F-G0-3 asks B01 to state its basis.

---

## VALUATION (B10, B11): PENDING PHASE 3
Not audited. The valuation framework documents were not read. Rules 4, 5 (valuation part), 7, 11, 12, 13, 14 and 15 run in phase 3. recomputed_destination_pe and recomputed_decision are blank. Blank here does not mean concurrence.

## Rules not run in this scope
- Rule 6 (B09 downstream candidates): the task scope is B01 and B07 only, and B09 is not in my inputs.
- Rule 9 (Business Understanding Narrative): stage 13 has not run.
- Rule 10 (B09b dossier): fires at the /finalize verifier pass. The phase-1 check is mechanical, inside run-pipeline step 6b.

## Carry-forward for phase 3
1. Test Pillar 3 on both em readings, NONE (11.7) and MODEST (12.0 to 13.1). Re-grade F-EM-1 to CRITICAL if destination PE moves by more than 1x.
2. Check that stage 11 does not read capex_embedded_growth_pct 22 as the 2C formula figure (F-EM-4).
3. Check that stage 11 does not read the inventory-days basis label as stated (F-G0-2) or the CFO/EBITDA figure as stated (F-G0-1).
4. M3 rests on the FY26 spot year (O-G0-2). Check that no spot-year ROCE feeds Section 1B if the name is classed CONVERTER (v3.7 Amendment 17).

```yaml
stage: B12c
company: "SHAWGELTIN"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
gate0: {rules_checked: 59, fails: ["G0-02 M3 FAT denominator weak anchor (MINOR, F-G0-3)", "G0-06 inventory-days basis label not supportable (MINOR, F-G0-2)", "G0-54 block_b_trend: CFO/EBITDA not reproducible, label not shown by one number (MAJOR, F-G0-1)", "G0-57 dashboard lacks moat profile bars (MINOR, F-G0-4)", "G0-58 report closing YAML abridged (MINOR, F-G0-4)"], boundary_note: "Core 60 is the exact floor of the GOOD band. E2 has three readings: 1 (maker, Dec-2023 base), 3 (Mar-2023 base, disclosed), 0 (strict rule-5 NOT FOUND for Sep-2023) which gives core 59 = AVERAGE plus FLAG-GATE0. Audit keeps the maker reading (rule 6, observed points bracket the date). C2 5.22% vs 5% line holds on the FY26 PAT implied by B07. Operator may rule on E2."}
emoat: {rules_checked: 43, fails: ["EM-07 capex_embedded_growth_pct is not the 2C formula output (MINOR, F-EM-4)", "EM-11 F2 tiered as claim with no concall or presentation source (MAJOR, F-EM-1)", "EM-12 mixed-tier weight convention not uniform (MINOR, F-EM-2)", "EM-13 anchors cite stage reports or note numbers, not source pages (MINOR, F-EM-7)", "EM-20 B2 likelihood x impact conflicts with report text (MINOR, F-EM-3)", "EM-24 scorecard groups 14 zero rows into 2 (MINOR, F-EM-8)", "EM-28 I2 not answered for each moat (MINOR, F-EM-5)", "EM-31 optionality register omits H1 (MINOR, F-EM-6)", "EM-36 6E map omits families D and I (MINOR, F-EM-8)", "EM-43 report closing YAML abridged (MINOR, F-EM-8)"], band_note: "em_score 11.7 is not stable at NONE. F2 at the as-written documented tier alone gives 12.0 = MODEST. Uniform per-item convention gives 13.1 = MODEST; uniform weakest-link convention gives 10.5 = NONE; B2 at LM gives 10.7 = NONE. Rubric is silent on mixed-tier categories. Phase 3 Pillar 3 audit must carry both NONE and MODEST readings."}
valuation: {rules_checked: 0, fails: [], scope: "pending phase 3"}
expectation_ledger: {scope: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; not audited in phase 1, null is not a fail
business_understanding_narrative: {scope: "not in phase 1 (stage 13 not run)", present: null, all_five_questions: null, prose_only: null, b09_candidates_named: null, no_valuation_language: null, fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # pending phase 3; blank here is NOT concurrence
recomputed_decision: ""        # pending phase 3; blank here is NOT concurrence
findings:
  - {id: "F-G0-1", artifact: "B01", rule: "G0-54", severity: "MAJOR", claimed: "block_b_trend and load-bearing check: FY26 CFO/EBITDA 79% vs 92% FY25, label stable (B01-gate0.yaml L35; 01-gate0.md L77)", recomputed: "Report's own SA rows: FY26 25/41 = 61%; FY25 17/(189 x 13% = 24.6) = 69%. FY26 stated value fits a post-tax denominator, 24.56/(41 - 10.2) = 80% [INFERENCE]; FY25 PBT not in report. Field asks for one number: 3-yr CFO/PAT 0.95 vs 12-yr 0.78 reads improving; CFO/PAT 1.00 FY25 to 0.89 FY26 reads deteriorating; neither shows stable.", effect: "No score or classification change. Field feeds FLAG-CASH. Restate or relabel the ratio; pick one label with its one number. Whether any source shows 79%: Verifier A."}
  - {id: "F-G0-2", artifact: "B01", rule: "G0-06", severity: "MINOR", claimed: "Inventory days 156, sales basis (01-gate0.md L78; B01-gate0.yaml L27, L36)", recomputed: "156/365 x Rs 215 Cr = Rs 91.9 Cr inventory, above FY26 total current assets Rs 85.05 Cr (8,504.73 lakh, 01-gate0.md L42). B07 G2 labels the same 156 days on cost (07-emoat.md L66).", effect: "Basis statement (prompts/01 L34-38) not supportable. B4 = 5 and M12 = 0 hold on every series. Correct the label before stage 11 reads inventory days."}
  - {id: "F-G0-3", artifact: "B01", rule: "G0-02", severity: "MINOR", claimed: "M3 FAT 215/41 = 5.2x, anchor (SA) only (01-gate0.md L57)", recomputed: "Denominator 41 equals the D1 EBITDA figure (01-gate0.md L39) and is not named as net block. FY26 closing gross block Rs 53.2 Cr (07-emoat.md L40) gives FAT >= 4.04x > 3x, so M3 = 5 holds.", effect: "Weak anchor only. Name and anchor the fixed-asset line."}
  - {id: "F-G0-4", artifact: "B01", rule: "G0-57, G0-58", severity: "MINOR", claimed: "Dashboard and closing block (01-gate0.md L52-68, L84-110)", recomputed: "No moat profile bars (prompts/01 L163-165). Report's closing YAML omits data_notes and analyst_note and a pointer line follows it (prompts/01 L165-166). Block file complete.", effect: "Presentational."}
  - {id: "F-EM-1", artifact: "B07", rule: "EM-11", severity: "MAJOR", claimed: "F2 scored ML x 0.7 claim tier; evidence_mix counts the Note 4 no-overrun statement as a claim (07-emoat.md L64, L99)", recomputed: "Claim tier = stated in concall or presentation, not yet backed by committed capital (prompts/07 L32-33). Run is NO-CONCALL, no presentation (07-emoat.md L4). F2 rests on a filed AR Note 4 disclosure on spent capital (documented) and a CWIP-movement inference (inference). F2 documented = 1.0, total 12.0 = MODEST; F2 inference = 0.5, total 11.5 = NONE.", effect: "em_classification flips on the as-written tier alone. Band-edge flag (B07-emoat.yaml L12) names H2 only. Combined GOOD likely survives (07-emoat.md L163). Destination-PE effect NOT ASSESSABLE in phase 1; phase 3 re-grades to CRITICAL if the NONE/MODEST reading moves destination PE by more than 1x."}
  - {id: "F-EM-2", artifact: "B07", rule: "EM-12", severity: "MINOR", claimed: "A3 tiered documented despite inferred attribution and MD&A crediting coal (07-emoat.md L53); H1 inference and H2 claim tiered by the benefit link despite documented items (L67, L68)", recomputed: "Uniform per-item convention: F2 1.0, H1 1.0, H2 2.0, total 13.1 = MODEST. Uniform weakest-link convention on the maker's own stated links: A3 1.0, F2 0.5, total 10.5 = NONE. Maker L x I held.", effect: "Rubric (prompts/07 L171-174) silent on mixed-tier categories; the band turns on the convention. Operator ruling recommended; maker states the convention."}
  - {id: "F-EM-3", artifact: "B07", rule: "EM-20", severity: "MINOR", claimed: "B2 scored MM = 2.0 documented (07-emoat.md L56, L113)", recomputed: "Same report: existing, retained, not new (L56); table stakes, not a lock-in (L150); certifications copyable without destroying any P&L line (L71). Scan scores moats currently forming (prompts/07 L21-24). At LM, B2 = 1.0, total 10.7 = NONE.", effect: "Symmetric counterweight to F-EM-1. Band unchanged in isolation."}
  - {id: "F-EM-4", artifact: "B07", rule: "EM-07", severity: "MINOR", claimed: "capex_embedded_growth_pct 22 (B07-emoat.yaml L26)", recomputed: "2C formula: 3,300 lakh x 4.513x = 14,892 lakh = 69.1% of FY26 revenue 21,541.15 lakh (07-emoat.md L40). On AR-documented spent or contracted 1,723.03 lakh (L35): 7,776 lakh = 36.1%. Block carries the capacity cross-check 21.8% (L42).", effect: "Field is defined as the 2C output (prompts/07 L60-63, L233). Both figures disclosed (L41-43; analyst_note). Carry the formula figure or label both so stage 11 does not read 22 as the formula output."}
  - {id: "F-EM-5", artifact: "B07", rule: "EM-28", severity: "MINOR", claimed: "I2 answers for certifications, solar, consultancy (07-emoat.md L71)", recomputed: "Rule asks for each moat claimed (prompts/07 L139-141): 3 of 9 scored categories answered. C1 not tested against the decades-old institutional customer relationship direction (prompts/07 L145-147; 07-emoat.md L51, L58).", effect: "I2 = 0 likely holds: C1 is claim-only and no specific sacrifice is named."}
  - {id: "F-EM-6", artifact: "B07", rule: "EM-31", severity: "MINOR", claimed: "Register holds 6 rows (07-emoat.md L127-134; B07-emoat.yaml L27-33)", recomputed: "H1 rests on inference only (07-emoat.md L67) and is absent; F2 (claim as tiered) absent. Scope: scored 0 or resting only on claim or inference (prompts/07 L184). B1, C1, H2 are registered.", effect: "Monitoring gap only. Add H1."}
  - {id: "F-EM-7", artifact: "B07", rule: "EM-13", severity: "MINOR", claimed: "Anchors cite B02, B03, B05 or a note number without page (07-emoat.md L24-25, L55, L65, L66, L163)", recomputed: "Rule: source anchor on every evidence item (prompts/07 L35-36).", effect: "Weak anchors. Existence of the figures: Verifier A."}
  - {id: "F-EM-8", artifact: "B07", rule: "EM-24, EM-36, EM-43", severity: "MINOR", claimed: "Scorecard L120-121, 6E L166-174, closing block L178-191 (07-emoat.md)", recomputed: "14 zero categories in 2 grouped rows, rule asks all 23 rows (prompts/07 L173-174); 6E omits families D and I (prompts/07 L208-209); report's closing YAML abridged with a pointer line after it (prompts/07 L214). Block file complete.", effect: "Presentational. All 23 categories are named."}
critical_count: 0
major_count: 2
minor_count: 10
acceptance_rate: 85.3             # rules passed / rules checked, %: 87 of 102 (gate0 54/59 = 91.5%; emoat 33/43 = 76.7%); denominator >= 4, rate applicable, above 60%
```
