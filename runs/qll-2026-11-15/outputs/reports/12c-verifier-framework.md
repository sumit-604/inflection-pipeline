# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE. QLL, run 2026-11-15

Verifier: verifier-c-framework. Model: claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter, line 5). Fresh context. Artifacts only.

Scope: Gate 0 (B01) and Emerging Moat (B07) compliance. The valuation audit (B10, B11; verifier rules 4 to 7 and 9 to 15) is PENDING PHASE 3. The valuation framework docs were not loaded.

Inputs read:
- prompts/12-verifiers-pipeline.md, header (lines 1-33) and VERIFIER C section (lines 213-390)
- prompts/01-gate-0-pipeline.md (rule source for B01; "G-rule Lnn" below = line nn of this file)
- prompts/07-emerging-moat-pipeline.md (rule source for B07; "E-rule Lnn" below = line nn of this file)
- outputs/reports/01-gate0.md and outputs/blocks/B01-gate0.yaml
- outputs/reports/07-emoat.md and outputs/blocks/B07-emoat.yaml
- inputs/screening/ (one search only, for check G03: no ROCE row present)

Method. I re-derived every score from the inputs each stage states, with the thresholds in the two rule files. I did not re-read corpus documents. Verifier A owns the question of whether a number is in the source. Every number below carries the stage-report line it comes from; the filing anchor is the one the stage gives on that line. Units are Rs Lakh unless marked.

---------------------------------------------------------------------------
## 0. RESULT

| Framework | Rules checked | Passed | FAIL | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 41 | 38 | 3 | 0 | 0 | 3 |
| Emerging Moat (B07) | 30 | 25 | 5 | 0 | 1 | 4 |
| Valuation (B10, B11) | PENDING PHASE 3 | | | | | |
| Total, phase 1 | 71 | 63 | 8 | 0 | 1 | 7 |

Acceptance rate: 63 / 71 = 88.7%. The denominator is 4 or more, so the rate applies. It is above the 60% REWORK line. Gate 0 portion 38 / 41 = 92.7%. EM portion 25 / 30 = 83.3%.

Decisions: concur.
- Gate 0 AVERAGE holds under every reading I tested. Core runs 42 to 55, all inside the 40-59 band (section 1.4).
- Moat class STRONG holds under every FAIL recomputation. Moat score runs 14 to 18, with 4 moats present in each case.
- EM class NONE (11.0) holds under every FAIL recomputation (10.4 to 11.0).
- The EM total sits 1.0 below the MODEST edge. Three judgment moves inside the rule would cross it, and three would move it further down (section 2.4). B07 showed only one upward move.

The one MAJOR finding: the B07 block field capex_embedded_growth_pct is 72. The 2C formula as written gives 98.

---------------------------------------------------------------------------
## 1. GATE 0 (B01)

### 1.1 Compliance table

| ID | Rule (G-rule line) | B01 value (01-gate0.md line) | Re-derived from B01's stated inputs | Verdict |
|---|---|---|---|---|
| G01 | Opening "Data available" line (L23-25) | 6 years FY21 to FY26 (line 3) | same | PASS |
| G02 | 5-6 years = lower confidence, flag, no downgrade (L142-144) | lower; flag "may not have seen full cycle" (lines 3, 130); history_downgrade false | same | PASS (O-G9) |
| G03 | ROCE: source figure if supplied, else compute and say "computed" (L29-31) | computed, stated (line 44) | inputs/screening has no ROCE row | PASS |
| G04 | A1 median ROCE (L55) | 15.4% = 3 (line 55) | valid years 10.0, 10.8, 15.4, 22.4, 70.1 (line 48-53); median 15.4% = 3 | PASS (O-G1) |
| G05 | A2 minimum ROCE (L56) | 9.98% = 1 (line 56) | 1,250.88 / 12,533.94 = 9.98%; band 8-11.9 = 1 | PASS |
| G06 | A3 median ROE with earliest-year fallback (L32-33, L57) | FY21 N/M; median 20.4% = 5 (line 57) | FY21 on closing net worth = -29.2%; median 15.9% = 4 | FAIL, MINOR |
| G07 | A4 ROCE trend (L58-59) | -59.3pp = 0 (line 58) | vs FY22 -59.3pp; vs FY23 -11.6pp; both > 5pp = 0 | PASS |
| G08 | B1 cumulative CFO / PAT (L62-63) | 1.20x = 5 (line 64) | 3,329.17 / 2,777.75 = 1.20x = 5 (1.10x on total PAT, same band) | PASS |
| G09 | B2 FCF = CFO - capex, acquisitions excluded (L39-40, L64) | 0 of 6 = 0 (line 65) | FY21 -470.71, FY22 -691.48, FY23 -1,014.31, FY24 -446.15, FY25 -1,285.28, FY26 -3,249.05 = 0 of 6 = 0 | PASS (O-G4) |
| G10 | B3 cumulative FCF / PAT (L65-66) | -2.58x = 0 (line 66) | -7,156.98 / 2,777.75 = -2.58x = 0 | PASS (O-G7) |
| G11 | B4 WC days; basis stated (L34-38, L67-68) | +172.8 days = 0 (line 67) | FY21 -67.5, FY26 105.3, revenue basis stated; change +172.8 = 0 | PASS |
| G12 | C1 revenue CAGR (L41, L71) | 81.3% = 5 (line 75) | (12,451.81 / 635.49)^(1/5) - 1 = 81.3% = 5 | PASS |
| G13 | C2 PAT CAGR (L72) | 144.4% = 5 (line 76) | (1,362.22 / 15.61)^(1/5) - 1 = 144.4% = 5 | PASS |
| G14 | C3 positive YoY years (L73) | 5 of 5 = 5 (line 77) | 5 of 5; the FY25 basis change is checked standalone to standalone (4,586.48 vs 2,918.38) = 5 | PASS |
| G15 | C4 PAT CAGR - revenue CAGR (L74) | +63.1pp = 5 (line 78) | 144.4 - 81.3 = +63.1pp = 5 | PASS |
| G16 | CAGR edge rules (L43-50) | no negative endpoint, no swing | FY21 PAT 15.61 and FY26 PAT 1,362.22 both positive; no loss-to-profit swing; C4 not N/M | PASS |
| G17 | D1 net debt / EBITDA (L77-79) | 2.92x = 1 (line 84) | 8,692.78 / 2,981.26 = 2.92x (2.97x excl. other income) = 1 | PASS (O-G3) |
| G18 | D2 interest cover (L80-82) | 4.81x = 2 (line 85) | 2,312.64 / 480.54 = 4.81x = 2 | PASS |
| G19 | D3 debt / equity (L83-84) | 0.61 = 3 (line 86) | 9,297.55 / 15,242.60 = 0.61 = 3 | PASS |
| G20 | D4 current ratio (L85-86) | 1.04 = 1 (line 87) | 5,875.55 / 5,625.13 = 1.04 = 1 | PASS (O-G2) |
| G21 | E1 promoter holding (L89-90) | 56.46% = 4 (line 93) | band 50-59.9 = 4 | PASS |
| G22 | E2 promoter change over 3 years (L91-92) | -16.89pp over 2.5 years = 0 (line 94) | decrease > 3 = 0; short window disclosed; any longer window into the pre-IPO period cannot lift the score above 0 | PASS |
| G23 | E3 pledge and the NOT FOUND rule (L19-22, L93) | NOT FOUND = 0 (line 95) | NOT FOUND scores 0; DB5 correctly not fired on a missing figure | PASS |
| G24 | E4 contingents / net worth (L94-95) | 46.8% = 0 (line 96) | 7,140.69 / 15,242.60 = 46.8% on the disclosed note total = 0 | PASS |
| G25 | Core sum | 45 (line 102) | 9 + 5 + 20 + 7 + 4 = 45 | PASS |
| G26 | M1 pricing power (L102-104) | +12.1pp, CAGR 81.3% = 5 (line 110) | FY21 72.57 / 635.49 = 11.4%; FY26 2,928.52 / 12,451.81 = 23.5%; full-period endpoints, consolidated at both ends = 5 | PASS (O-G10) |
| G27 | M2 cost advantage (L105-106) | -3.9pp = 0 (line 111) | peer median of 27.4, 28.4, 27.3 = 27.4%; QLL 23.5% is below = 0 | PASS (O-G8) |
| G28 | M3 capital efficiency (L107-108) | FAT 1.69x, ROCE 10.8% = 0 (line 112) | ROCE not > 12% = 0 | PASS |
| G29 | M4 customer stickiness (L109-111) | 3 (line 113) | zero decline years meets "max 1 decline year"; tier 3 carries no receivable test = 3 | PASS |
| G30 | M5 scale, PEER DATA NEEDED (L99-100, L112-113) | 0, PEER DATA NEEDED (line 114) | full segment list not supplied = 0 | PASS |
| G31 | M6 R&D (L114-116) | NOT FOUND = 0 (line 115) | 0 | PASS |
| G32 | M7 regulatory (L117-119) | count NOT FOUND = 0 (line 116) | 0. Tiers 5 and 3 also need margin stable within 3pp or 5pp; margin moved +12.1pp, so the ceiling is 1 even with the count | PASS |
| G33 | M8 distribution (L120-122) | 3 (line 117) | network growing (3 labs added in FY26), CAGR >= 15% = 3 | PASS (O-G6) |
| G34 | M9 brand (L99-100, L123-125) | 1 (line 118) | 0 | FAIL, MINOR |
| G35 | M10 switching costs (L126-128) | 0 (line 119) | grew every year, receivable days +54; no tier condition is met = 0 | PASS (O-G5) |
| G36 | M11 network effects (L129-133) | 3, on the fewer-than-6-years fallback (line 120) | 5 on the series as reported; 3 like-for-like | FAIL, MINOR |
| G37 | M12 negative WC (L134-135) | 0 (line 121) | negative in 1 of 6; median 54.8 days; latest 105.3 = 0 | PASS |
| G38 | Moat score, count, class (L98-99, L137-138) | 15; 4; STRONG (lines 123-124) | 5+0+0+3+0+0+0+3+1+0+3+0 = 15; 4 tests at >= 3 = STRONG | PASS |
| G39 | Classification matrix (L146-149) | AVERAGE (line 130) | core 45 in 40-59 = AVERAGE at every moat class | PASS |
| G40 | Deal-breakers 1 to 9, driving years named (L151-159) | DB2 fired, non-binding, years named (line 132) | DB1 9 not < 8; DB2 5 < 8 fires, max GOOD, non-binding at AVERAGE, FY21-FY26 named; DB3 15.4%; DB4 1.20x; DB5 not evidenced; DB6 2.92x and 4.81x; DB7 no decline; DB8 FY24-FY26 positive; DB9 6 years | PASS |
| G41 | FLAG-GATE0 and YAML template (L161-198) | flag raised; all keys present (B01-gate0.yaml lines 1-39) | same; report copy equals block file; analyst_note about 95 words | PASS |

### 1.2 FAIL detail

**G06. A3 median ROE. MINOR.**
- Rule as written (G-rule L32-33): "if opening net worth unavailable for the earliest year, use closing and state so."
- B01 (line 57) marks FY21 ROE N/M because closing net worth is negative (-53.46, line 33). It takes the median of 5 years = 20.4% and scores A3 = 5.
- As written: FY21 ROE = 15.61 / -53.46 = -29.2%. The median of 6 values (-29.2, 10.6, 11.4, 20.4, 50.5, 246.2) = (11.4 + 20.4) / 2 = 15.9%. Band 15-19.9 = 4.
- Effect: Block A 9 to 8. Core 45 to 44. AVERAGE unchanged. DB1 (Block A < 8) does not fire at 8. B01's own sensitivity (line 57) reaches A3 = 4 by another path (dropping FY22).
- Reading: the fallback did not foresee negative closing net worth. B01's N/M is the sound economic reading, because positive profit on negative equity is not a return. The finding stands because the text has an explicit fallback and B01 did not cite why it set it aside. Operator ruling requested (section 4, gap 1).

**G34. M9 brand. MINOR.**
- B01 (line 118): gross margin proxy QLL 86.6%; LALPATHLAB 80.7%; VIMTALABS FY24 84.7%; KRSNAA blank (PEER DATA NEEDED). Two-peer median 82.7%. QLL +3.9pp. Scored 1 "at the residual 'above peers' tier".
- No M9 tier fits +3.9pp with growth 81.3%. Tier 3 needs >= 5pp. Tier 1 needs "growth below". Tier 0 needs "at/below". QLL meets none.
- The PEER DATA NEEDED rule (G-rule L99-100) says: if a test needs peer data that is not provided, score 0. B01 applied that rule to M5 on a partial peer set (line 114) and did not apply it to M9 on a partial peer set. The treatment is inconsistent.
- As written: M9 = 0. Moat 14 / 60. Count 4. STRONG. B01's own sensitivity (line 136) shows this.
- Symmetric check: under a consistent supplied-set reading, M5 = 1 (4th of 4 sits inside "top 5 mcap") and M9 = 1, moat 16. With full peer data, M9 could reach 3: if KRSNAA's proxy is 80.7% or lower, the three-peer median is 80.7% and QLL leads by 5.9pp. That adds a fifth moat, still STRONG. Operator ruling requested on the tier gap and on partial peer sets (section 4, gaps 2 and 6).

**G36. M11 network effects. MINOR.**
- Rule (G-rule L129-131): "needs >=6 years for the two-window test; if fewer, score conservatively on the overall trend and state so."
- B01 (line 120) has 6 years. It says "Two-window test not computable (no FY20 base)" and applies the fewer-than-6 fallback. M11 = 3.
- The rule's own threshold says 6 years is enough. On the series as reported (line 22):
  - latest window FY24 to FY26: (12,451.81 / 2,918.38)^(1/2) - 1 = 106.6%. On FY23 to FY26: (12,451.81 / 1,913.66)^(1/3) - 1 = 86.7%.
  - prior window FY21 to FY23: (1,913.66 / 635.49)^(1/2) - 1 = 73.5%.
  - latest > prior. Selling and admin share 20.9% (FY21) to 18.2% (FY26), which B01 itself reads as "declining overall" (line 120). Result: tier 5, moat 17.
- Like-for-like check: both windows cross the consolidated / standalone break (line 16), and the latest window holds the first consolidation of acquired subsidiaries. Standalone FY24 to FY26 = (6,762 / 2,918.38)^(1/2) - 1 = 52.2% (FY26 standalone revenue Rs 6,762 Lakh from 07-emoat.md line 81, citing AR26 MD&A p.75). 52.2% < 73.5%, so the test fails and the overall-trend tier 3 applies.
- Effect: M11 is 5 or 3. Moat count 4 and STRONG hold either way. The miss is procedural. B01 should run the test and state the basis-break reading, not invoke the fewer-than-6 fallback with the wrong reason. Operator ruling requested on the window definition at exactly 6 years (section 4, gap 4).

### 1.3 Observations (not scored)

- **O-G1. FY21 ROCE on negative capital employed.** Capital employed FY21 = 1,433.42 - 1,460.03 = -26.61 (line 31-32, 48). The rule is silent on a negative denominator. Literal inclusion gives -149.3%. That makes A1 = 1 (median 13.1%) and A2 = 0, but A4 = 5 because "latest >= earliest" against -149.3%. Block A would be 10 with G06's A3 = 4. That result is absurd, so B01's N/M stands. Operator ruling requested together with G06 (section 4, gap 1).
- **O-G2. Block D "latest".** B01 reads "latest" as FY26 audited (line 82). The 30 Sep 2026 unaudited balance sheet is later. On that reading D4 = 0 (current ratio 0.78) and D3 stays 3 (0.72) (line 89). B01 disclosed this. E1 says "latest quarter" and Block D says only "latest", so the FY26 reading is defensible. Operator ruling optional (section 4, gap 5).
- **O-G3. D1 cash line.** Cash 604.77 includes Rs 348.28 Lakh "debit balance in overdraft account" (line 84, AR26 p.105). If that line is taken out of cash, net debt = 9,041.06 and ND/EBITDA = 3.03x, so D1 = 0. DB6 still does not fire, because interest cover is 4.81x (not < 3x). How the filed line is read belongs to Verifier A. It enters the robustness table only.
- **O-G4. Capex includes CWIP cash outflow.** Consistent with "purchase of PPE" (line 40). Without CWIP, FY24 (+408.86) and FY26 (+142.48) turn FCF-positive. B2 is then 2 of 6 = 33% = 0, and cumulative FCF is -1,755.89, so B3 = 0. Block B does not move.
- **O-G5. M10 rule shape.** A company with zero decline years and receivable days +54 scores 0. A company with 2 or more decline years scores 1 whatever its receivables do. B01 applied the rule as written. Rule design note (section 4, gap 3).
- **O-G6. M8 cross-stage.** B01 counts the Bengaluru pharma lab as an FY26 addition (line 117, AR26 p.69-70). B07 rates its status unreconciled ([CLAIM], 07-emoat.md line 20). Without it the network still grows by 2 (Navi Mumbai, Bhubaneswar II, both DELIVERED in 07-emoat.md lines 190, 192). M8 = 3 holds.
- **O-G7. B3 rounding.** B01 states cumulative FCF -7,157.00 (line 66). The sum of its own yearly FCF is -7,156.98. The gap is 0.02 Lakh, cosmetic, and the score is unaffected.
- **O-G8. Peer set for M2 and M9.** Two of the three peers (KRSNAA, LALPATHLAB) are diagnostics chains. VIMTALABS is the testing-lab peer (line 106). M2 = 0 on VIMTALABS alone too (27.3% vs 23.5%). Peer selection belongs to stage 6 and Verifier D.
- **O-G9. Data-confidence flag sits in prose only.** "May not have seen full cycle" is in the report (lines 3, 130) but not in the YAML flags or data_notes. A downstream stage that reads only the block sees data_years: 6. Carry the flag in the block.
- **O-G10. M1 window.** The rule names no window. Full-period endpoints match A4's "latest vs earliest" convention, so G26 passes. The moat class depends on this choice. On FY23 to FY26 (which crosses the basis break), margin is -4.2pp, M1 = 1, count 3, MODERATE. On FY25 to FY26 like-for-like, margin is +0.4pp, M1 = 3, count 4, STRONG. Classification is AVERAGE in all three.

### 1.4 Robustness of the Gate 0 decision

| Reading | Change | Core | Moat score (present, class) | Classification |
|---|---|---|---|---|
| B01 as filed | none | 45 | 15 (4, STRONG) | AVERAGE |
| G06 A3 as written | A3 5 to 4 | 44 | 15 (4, STRONG) | AVERAGE |
| G34 M9 as written | M9 1 to 0 | 45 | 14 (4, STRONG) | AVERAGE |
| G36 M11, reported series | M11 3 to 5 | 45 | 17 (4, STRONG) | AVERAGE |
| O-G2 D4 at 30 Sep 2026 | D4 1 to 0 | 44 | 15 | AVERAGE |
| O-G3 overdraft line out of cash | D1 1 to 0 | 44 | 15 | AVERAGE |
| Stacked downside (G06, G34, O-G2, O-G3) | | 42 | 14 (4, STRONG) | AVERAGE |
| Stacked upside (E3 0% pledge, E4 external only, G36, M5 and M9 on supplied set) | | 55 | 18 (4, STRONG) | AVERAGE |
| O-G10 M1 on FY23 to FY26 | M1 5 to 1 | 45 | 11 (3, MODERATE) | AVERAGE |

Core < 40 (AVOID) would need 6 more points off the stacked downside. Core >= 60 would need 5 more points on the stacked upside. Neither is in the evidence.

---------------------------------------------------------------------------
## 2. EMERGING MOAT (B07)

### 2.1 Compliance table

| ID | Rule (E-rule line) | B07 (07-emoat.md line) | Verdict |
|---|---|---|---|
| E01 | All six sections, one response (L28) | Sections 1 to 6 present (lines 12-349) | PASS |
| E02 | Taxonomy on every single evidence item (L29-34) | several items carry no tag | FAIL, MINOR |
| E03 | Source anchor on every evidence item (L35-36) | anchors present on scored evidence; accuracy belongs to Verifier A | PASS |
| E04 | "NO EVIDENCE FOUND", no force-fit (L39-40) | 12 categories state NO EVIDENCE FOUND (A2, A3, A4, B1, B3, D1, D2, E1, F1, G1, G2, H3); G1 and G2 record contrary evidence and score 0 | PASS |
| E05 | Completionist guard and recount line (L41-46, L157-159) | 9 categories with evidence, below the 12 alarm; "[DOC] recount performed: 10 documented items across 5 categories" (line 182) | PASS (O-E2) |
| E06 | Section 1: 1A, 1B, 1C (L48-55) | lines 14-51; 3-year mix NOT FOUND stated | PASS |
| E07 | Section 2: 2A, 2B, 2D (L57-63) | lines 56-104; capacity and "% over current" stated NOT FOUND (line 69) | PASS |
| E08 | 2C: total capex under execution x historical FAT (L60-62) | headline 72%, block field 72 | FAIL, MAJOR |
| E09 | All 22 categories plus R1 addressed (L65-153) | lines 111-178 | PASS |
| E10 | Section 3 summary table, all rows, Strong/Moderate count (L155-159) | 23 rows (lines 154-178); count 2 (line 180) | PASS |
| E11 | R1 scored on R1-scope evidence (L161-168) | R1 scored on three customer work orders | FAIL, MINOR |
| E12 | Category 21 (I1) present; > 0 only with both legs and the (b) leg DOC (L122-138; verifier rule 8) | present; 0; neither leg evidenced (line 149) | PASS |
| E13 | Category 22 (I2) present; > 0 only with a named, specific sacrifice (L139-153; verifier rule 8) | present; 0; "nothing must be destroyed" (line 150) | PASS |
| E14 | Section 4: 4A, 4B, 4C (L161-168) | lines 215-232 | PASS |
| E15 | Likelihood x impact matrix values (L171-172) | A1 ML 1, B2 HM 3, C1 ML 1, C2 MM 2, E2 LM 1, F2 LL 1, H1 ML 1, H2 ML 1, R1 MM 2 (lines 241-263); all match | PASS (O-E3) |
| E16 | Evidence multipliers (L173) | DOC 1.0 on B2, F2, H1, R1; CLAIM 0.7 on A1, C1, C2, H2; INFER 0.5 on E2 | PASS |
| E17 | No CLAIM-only category scored as DOC (verifier rule 3) | every DOC-scored row has a filed item (B2 NABCB release; F2 filed comparisons; H1 acquisition notes; R1 order filings) | PASS |
| E18 | Adjusted total (L174) | 11.0 (line 264) | PASS: 0.7+3.0+0.7+1.4+0.5+1.0+1.0+0.7+2.0 = 11.0 |
| E19 | Band (L175-176) | < 12 = NO MEANINGFUL EMERGING MOAT; block "NONE" | PASS |
| E20 | I1/I2 contribution stated separately; checkpoint note (L177-181) | 0.0; no crossing via I1/I2 (line 268) | PASS |
| E21 | "EM >= 25" UA qualifier | "not met" (line 272) | PASS |
| E22 | Optionality register: rows scored 0 or CLAIM/INFER only; table form (L183-192) | 11 rows (lines 276-288) | PASS (O-E6) |
| E23 | Register carried in the block as optionality_register[] (L194-196) | block holds 10 of 11 rows | FAIL, MINOR |
| E24 | F2 cross-reference to the promise-delivery record (L106-107) | no concall; capex-completion record substitutes, and B05 credibility C is cross-referenced (line 186) | PASS |
| E25 | 6A, 6B (L199-201) | lines 293-309 | PASS |
| E26 | 6C uses the injected Gate 0 block (L201-203) | core 45; 15 / 4 / STRONG; AVERAGE (lines 315-319) match B01 | PASS |
| E27 | 6D combined classification; HIGH POTENTIAL and TURNAROUND reasoning (L203-208) | AVERAGE; both excluded with reasons (line 325) | PASS |
| E28 | 6E card: moat evolution map, 12-month catalysts, biggest risk (L208-210) | lines 327-349 | PASS |
| E29 | Report ends with the fenced YAML block (L212-214) | block missing from the stage's report; orchestrator erratum (line 361) | FAIL, MINOR |
| E30 | YAML keys per template; active_categories only Strong/Moderate (L216-243) | all keys present; active = B2, R1 (B07-emoat.yaml lines 1-51) | PASS |

### 2.2 FAIL detail

**E08. Section 2C capex-embedded growth. MAJOR.**
- Rule (E-rule L60-62): "total capex under execution x historical fixed asset turnover = implied incremental revenue, expressed as % above current revenue."
- B07 step 2 (line 83) itself defines capex under execution as CWIP Rs 6,977.28 Lakh at 30 Sep 2026. Case A (line 89) applies the rule as written: 6,977.28 x 1.743 = 12,158.6 Lakh = 97.6% of FY26 revenue 12,451.81 Lakh.
- B07 makes case B the headline (line 90, 94). Case B subtracts Barwala land and building 1,813.01 Lakh and gives 72.3%. The block carries capex_embedded_growth_pct: 72 (B07-emoat.yaml line 32). The 49% to 98% range sits only in a YAML comment, which a parser may drop.
- Why the subtraction does not hold as written:
  - The 1,813.01 is a 31 Mar 2026 figure. B07 itself records its 30 Sep 2026 value as NOT FOUND (block line 11). A stale component comes off a current total.
  - The FAT denominator is total closing net PPE 7,145.72 (line 78). Taking land and building out of the numerator only puts the numerator and denominator on different asset bases. [INFERENCE: net PPE normally includes land and buildings; the PPE note is not among my inputs.]
- Recomputed: capex_embedded_growth_pct = 98 (97.6). The field understates the as-written figure by 25.3 points.
- Effect: EM score and class do not move, because 2C is not scored. The field is a block value that stage 11 may read as capacity evidence (verifier rule 4 names CAPACITY as a 26.1 base-case basis). The figure is a full-ramp ceiling, as B07 says (line 94), so the decision likely survives. Fix: carry 98 as the headline and cases B to D as named sensitivities.

**E02. Evidence taxonomy not applied to every item. MINOR.**
- Rule (E-rule L29-34): the taxonomy applies "to every single piece of evidence".
- Items with no [DOC] / [CLAIM] / [INFER] tag:
  - A3, gross margin 78% to 87% (line 114, deck p.11).
  - A4, business lines 7 to 15 (line 115, deck p.41).
  - B2, defence test standards JSS 55555 and MIL 810 (line 119, deck May 2026 p.29).
  - F1, the no-ESOP statement (line 135, AR26 p.64).
  - R1 4B, the PPP labs (line 228, deck p.19 and AR25 p.19).
- Two of these items carry weight in a score: the B2 defence-standards item and the R1 PPP-lab item. The PPP item's tier decides the E11 recomputation.
- The text tags in place of emoji glyphs are declared at line 7 and used consistently. That substitution is cosmetic and is not counted (O-E7).

**E11. R1 scored on evidence outside R1's scope. MINOR.**
- Rule (E-rule L161-168): R1 covers 4A regulatory approvals and 4B government policy tailwinds (PLI, tax incentives, import substitution measures, procurement preference, sector schemes, infrastructure support).
- B07 4C (line 232): "Score R1 as Moderate, because three filed contracts exist." The recount (line 182) assigns R1's 3 DOC items to IOC order 1, IOC order 2 and the BRDC order. The analyst_note (block line 51) keys R1's impact rating to the size of those orders.
- Customer work orders are not approvals and not policy tailwinds. B07's own 4B (line 228) says "Competitors can bid for the same tenders: shared benefit", so no procurement preference is shown.
- The one R1-scope DOC approval in 4A (NABCB 17020, 25 Jun 2026, line 219) is already B2's scored DOC basis (recount, line 182). Scoring it again in R1 would credit one item through two categories. B07 did not do that, but it means R1 has no DOC basis of its own.
- Recomputed on the R1-scope evidence that remains: coal TPA empanelment (deck May 2025 p.11, [CLAIM], line 221) and the PPP labs (untagged, line 228). R1 = 1.4 (M x M x 0.7) or 2.0 (if the AR25 p.19 PPP statement is read as DOC, a launched operation). Total 10.4 to 11.0.
- Effect: class NONE unchanged. At 1.4, B07's own grade rule (line 109) ranks R1 Weak. active_categories would then fall to B2 alone. The three orders belong under 1A (the LPO line) or C1.

**E23. Optionality register not carried in full. MINOR.**
- Rule (E-rule L194-196): the register is "Carried in the B07 block as optionality_register[]. Synthesis merges register items into the monitoring checklist."
- The report table has 11 rows (lines 276-288). The block has 10 (B07-emoat.yaml lines 33-43).
- Missing from the block: "Digital / AI compliance services". Converting evidence: digital revenue disclosed, client dashboard usage. First appears: AR27 MD&A. Window: 12-24 months (line 287).
- Effect: the item drops out of the synthesis monitoring checklist. Fix: add the row to the block.

**E29. Output contract. MINOR.**
- Rule (E-rule L212-214): "Full six-section report, then end with exactly this fenced YAML block."
- The stage wrote its report without the block. The orchestrator appended a verbatim copy of outputs/blocks/B07-emoat.yaml (line 361-416). I compared the copy with the block file line by line, and they match.
- Effect: no content effect. The record stands as an output-contract miss by stage 7.

### 2.3 Observations (not scored)

- **O-E1. Threshold position.** The total of 11.0 sits 1.0 below the MODEST edge. See 2.4.
- **O-E2. Recount and scorecard tiers disagree.**
  - The recount (line 182) counts E2 as 1 DOC item (exports Rs 333.06 Lakh), but Section 5 scores E2 at INFER 0.5 (line 253).
  - The C2 summary row reads "CLAIM (DOC baseline)" (line 164), but the recount does not count the C2 baseline as DOC.
  - Result: the recount names 5 DOC categories, while the scorecard scores 4 at DOC.
  - Both scored tiers are the conservative reading of thin evidence, so they are not FAILs.
- **O-E3. B2 likelihood against B07's own text.** B07 calls accreditation "table stakes" and "not unusual" (line 119). It says "a global TIC major can apply for the same scope" (line 150) and "Accreditation is not scarce" (line 306). It still rates B2 likelihood High (H x M = 3, line 246). This is a judgment inside the matrix, not a rule breach. The downward move is in 2.4.
- **O-E4. Strength thresholds are the stage's own.** The Strong / Moderate / Weak cut-offs (line 109) are B07's rule. The prompt asks for strength and defines no thresholds. B07 stated its rule and applied it consistently (section 4, gap 7).
- **O-E5. FAT basis differs across stages.** B07 uses 1.743x on net PPE (line 78). B01 M3 uses 1.69x on net PPE plus intangibles (01-gate0.md line 112). This has no score effect, because M3 = 0 either way.
- **O-E6. Register and scored evidence.** The IAC and LPO register rows sit beside the evidence scored in B2 and R1. Each register row names the unscored forward step (revenue scale-up), so there is no double credit.
- **O-E7. Glyphs.** B07 declares [DOC] / [CLAIM] / [INFER] at line 7 and uses them consistently. The substitution is cosmetic.
- **O-E8. "Historical" FAT.** 2C uses single-year FY26 FAT. FY25 FAT (1.190x, line 80) is distorted by part-year consolidation. Cases C and D (lines 91-92) cover the lower FAT readings.
- **O-E9. Cross-stage lab count.** See O-G6.

### 2.4 Threshold sensitivity of the EM class (judgment moves inside the rule, symmetric)

| Reading | Change | Total | Class |
|---|---|---|---|
| B07 as filed | none | 11.0 | NONE |
| R1 impact High (B07's own sensitivity, line 270) | R1 2.0 to 3.0 | 12.0 | MODEST |
| C2 at DOC multiplier (prospectus top-5 25.24% to 21.50%, line 124) | 1.4 to 2.0 | 11.6 | NONE |
| E2 at DOC multiplier (recount counts it DOC, line 182) | 0.5 to 1.0 | 11.5 | NONE |
| C2 and E2 both at DOC | +1.1 | 12.1 | MODEST |
| E11 recomputation, R1 on CLAIM-tier R1-scope evidence | 2.0 to 1.4 | 10.4 | NONE |
| B2 likelihood Medium, per B07's own "table stakes / not scarce" text | 3.0 to 2.0 | 10.0 | NONE |
| F2 at 0 (B07: "F2 does not show an execution moat", line 210) | 1.0 to 0 | 10.0 | NONE |

The class turns on single judgment calls in both directions. B07 showed only the upward R1 move. Two readings remain:
- Reading 1: the scan is honestly sparse, and NONE is right.
- Reading 2: two thin DOC items (the C2 baseline, the E2 export figure) earn full weight, and the class is MODEST.

The observation that separates them is a current customer-concentration disclosure and an export figure with a prior-year comparative, both from the FY27 AR. The "EM >= 25" UA qualifier fails under every reading.

---------------------------------------------------------------------------
## 3. VALUATION (B10, B11): PENDING PHASE 3

Not run. Stages 10 and 11 have not run, and the valuation framework docs were not loaded. Deferred to phase 3:
- rule 4: growth symmetry checks and pillar mechanics
- rule 5: valuation severity grading
- rule 6: B09 downstream candidates and stage 11 catalyst citations. B09 is not among the phase-1 inputs.
- rule 7: method plurality
- rule 9: Business Understanding Narrative, stage 13
- rule 10: B09b dossier at /finalize
- rule 11: v3.8 exit construction
- rule 12: Amendment 19 FV path
- rule 13: Expectation Ledger schema
- rule 14: off-ledger credit and residual starter cap
- rule 15: skill-to-source fidelity

Rules 1 to 3 and rule 8 ran in this phase.

---------------------------------------------------------------------------
## 4. RULE GAPS FOR OPERATOR RULING (rule text, not stage error)

1. Negative denominators. The ROE earliest-year fallback ("use closing") and the ROCE formula do not cover negative net worth or negative capital employed (G06, O-G1).
2. M9 tier gap. "Above peers by under 5pp with growth >= 8%" has no tier (G34).
3. M10 shape. Zero decline years with rising receivables scores below 2 or more decline years (O-G5).
4. M11 window at exactly 6 years. Is each window 3 data points (2 intervals) or a 3-interval CAGR, which needs 7 years? (G36)
5. Block D "latest". Is it the latest fiscal-year balance sheet or the latest reported balance sheet (O-G2)?
6. PEER DATA NEEDED on a partial peer set. Score 0, or score on the supplied set (G34 with M5)?
7. Stage 7 strength grades. The prompt asks for Strong / Moderate / Weak and defines no cut-offs (O-E4).
8. Stage 7 2C. How land and building inside CWIP is treated, and whether FAT means single-year or multi-year (E08, O-E8).

---------------------------------------------------------------------------
## 5. RUN NOTES

- Stuck rule not triggered. No action repeated without change.
- No Verifier A source-fidelity question was touched. Where a reading depends on a filed line (O-G3), it is named for Verifier A and enters robustness only.
- No finding is CRITICAL. No finding changes the Gate 0 classification, the moat class, the EM class or the combined assessment. recomputed_decision is blank (concur).

---------------------------------------------------------------------------
## 6. YAML BLOCK

```yaml
stage: B12c
company: "QLL"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation audit (B10, B11) pending phase 3"
gate0: {rules_checked: 41, rules_passed: 38, fails: ["G06", "G34", "G36"]}
emoat: {rules_checked: 30, rules_passed: 25, fails: ["E02", "E08", "E11", "E23", "E29"]}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "pending (stage 13 not run)", present: null, five_questions: null, prose_only: null, downstream_refs_or_sentence: null, no_valuation_vocab: null, fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # not applicable in phase 1 (stage 11 not run)
recomputed_decision: ""        # concur: Gate 0 AVERAGE, moat STRONG, EM NONE, combined AVERAGE survive every FAIL recomputation
findings:
  - id: "G06"
    framework: "Gate 0"
    rule: "A3 median ROE; earliest-year fallback 'use closing and state so' (prompts/01-gate-0-pipeline.md L32-33)"
    severity: MINOR
    location: "outputs/reports/01-gate0.md section 3, line 57"
    claimed: "FY21 ROE N/M on negative closing net worth; median of 5 = 20.4%; A3 = 5"
    recomputed: "FY21 ROE on closing = 15.61 / -53.46 = -29.2%; median of 6 = 15.9%; A3 = 4; Block A 8; core 44"
    effect: "AVERAGE unchanged; DB1 not fired at Block A 8. Fallback did not foresee negative net worth; B01 N/M is the sound economic reading; operator ruling requested on negative denominators (ROE and ROCE)."
  - id: "G34"
    framework: "Gate 0"
    rule: "M9 brand tiers (L123-125) and PEER DATA NEEDED rule (L99-100)"
    severity: MINOR
    location: "outputs/reports/01-gate0.md section 9, M9 row line 118; M5 row line 114"
    claimed: "M9 = 1 at a 'residual above peers' tier on a two-peer median 82.7% (KRSNAA blank); QLL 86.6%, +3.9pp"
    recomputed: "M9 = 0: no tier fits +3.9pp with growth 81.3%, and missing KRSNAA data triggers PEER DATA NEEDED = 0, as B01 applied to M5; moat 14/60; 4 present; STRONG"
    effect: "Moat class unchanged. Supplied-set reading for both tests gives M5 1, M9 1, moat 16. Full peer data could lift M9 to 3 (KRSNAA proxy at or below 80.7%), a fifth moat, still STRONG."
  - id: "G36"
    framework: "Gate 0"
    rule: "M11 two-window test 'needs >=6 years'; fallback only 'if fewer' (L129-133)"
    severity: MINOR
    location: "outputs/reports/01-gate0.md section 9, M11 row line 120"
    claimed: "two-window test not computable (no FY20 base); fewer-than-6 fallback used at 6 years; M11 = 3"
    recomputed: "reported series: FY24-FY26 CAGR 106.6% (FY23-FY26 86.7%) > FY21-FY23 73.5%, selling and admin 20.9% to 18.2% declining on B01's own reading: M11 = 5, moat 17. Like-for-like standalone FY24-FY26 52.2% (FY26 standalone Rs 6,762 Lakh, 07-emoat.md line 81) < 73.5%: tier 3"
    effect: "4 moats present and STRONG either way. Run the test and state the basis-break reading; operator ruling requested on the window definition at exactly 6 years."
  - id: "E02"
    framework: "Emerging Moat"
    rule: "evidence taxonomy applied to every single piece of evidence (prompts/07-emerging-moat-pipeline.md L29-34)"
    severity: MINOR
    location: "outputs/reports/07-emoat.md lines 114, 115, 119, 135, 228"
    claimed: "items untagged: A3 gross margin (deck p.11); A4 business lines (deck p.41); B2 defence standards JSS 55555 / MIL 810 (deck May 2026 p.29); F1 no-ESOP statement (AR26 p.64); R1 4B PPP labs (deck p.19, AR25 p.19)"
    recomputed: "each item needs a DOC, CLAIM or INFER tag; the B2 and R1 items bear on scores, and the PPP tier decides the E11 range"
    effect: "No score change by itself. Text tags in place of emoji glyphs are declared (line 7) and not counted."
  - id: "E08"
    framework: "Emerging Moat"
    rule: "2C: total capex under execution x historical fixed asset turnover, as % above current revenue (L60-62)"
    severity: MAJOR
    location: "outputs/reports/07-emoat.md section 2C lines 83-94; outputs/blocks/B07-emoat.yaml line 32"
    claimed: "capex_embedded_growth_pct 72 (case B: CWIP 6,977.28 less Barwala land and building 1,813.01 = 5,164.27 Lakh x 1.743 = 8,999.3 Lakh)"
    recomputed: "98 (case A: total CWIP 6,977.28 Lakh at 30 Sep 2026 x FY26 FAT 1.743 = 12,158.6 Lakh = 97.6% of FY26 revenue 12,451.81 Lakh)"
    effect: "Field understates the as-written figure by 25.3 points. The 1,813.01 is a 31 Mar 2026 value whose 30 Sep 2026 value is NOT FOUND, and the FAT denominator is total net PPE. EM score and class unaffected; stage 11 may read the field as capacity evidence. Carry 98 as headline, cases B to D as sensitivities."
  - id: "E11"
    framework: "Emerging Moat"
    rule: "R1 scope: 4A regulatory approvals, 4B government policy tailwinds (L161-168)"
    severity: MINOR
    location: "outputs/reports/07-emoat.md 4C line 232, recount line 182, 4B line 228; B07-emoat.yaml analyst_note line 51"
    claimed: "R1 Moderate, M x M = 2 x DOC 1.0 = 2.0, scored 'because three filed contracts exist' (IOC order 1, IOC order 2, BRDC order)"
    recomputed: "customer orders are neither approvals nor policy tailwinds (4B: shared benefit, open tenders); the R1-scope DOC approval (NABCB 17020) is already B2's scored basis; on remaining R1-scope evidence (coal TPA empanelment CLAIM; PPP labs untagged) R1 = 1.4 to 2.0; total 10.4 to 11.0"
    effect: "Class NONE unchanged. At 1.4, B07's own grade rule ranks R1 Weak and active_categories falls to B2 alone. Move the orders to 1A (LPO) or C1."
  - id: "E23"
    framework: "Emerging Moat"
    rule: "optionality register carried in the block as optionality_register[] (L194-196)"
    severity: MINOR
    location: "outputs/reports/07-emoat.md lines 276-288 (11 rows); outputs/blocks/B07-emoat.yaml lines 33-43 (10 rows)"
    claimed: "10 register rows in the block"
    recomputed: "11 rows; missing 'Digital / AI compliance services' (digital revenue disclosed, client dashboard usage; AR27 MD&A; 12-24 months), report line 287"
    effect: "Item drops out of the synthesis monitoring checklist. Add the row to the block."
  - id: "E29"
    framework: "Emerging Moat"
    rule: "report ends with the fenced YAML block (L212-214)"
    severity: MINOR
    location: "outputs/reports/07-emoat.md line 361 (orchestrator erratum)"
    claimed: "stage report written without the closing YAML block"
    recomputed: "orchestrator appended a verbatim copy of outputs/blocks/B07-emoat.yaml; copy matches the block file line for line"
    effect: "No content effect; output-contract miss by stage 7 on record."
critical_count: 0
major_count: 1
minor_count: 7
acceptance_rate: 88.7             # rules passed / rules checked, %: 63 / 71 (Gate 0 38/41 = 92.7; EM 25/30 = 83.3); valuation pending phase 3
```
