# VERIFIER C: FRAMEWORK ADHERENCE, SUPREMEPWR (run 2026-10-06), PHASE 1 SCOPE

Model: claude-opus-5-5 (.claude/agents/verifier-c-framework.md L5). Scope: Gate 0 (B01) and Emerging Moat (B07) compliance only. The valuation-adherence audit (B10/B11) is pending phase 3. I did not read any valuation framework document (Master, Section 1B layers, FTTCP).

Rule sources read:
- prompts/12-verifiers-pipeline.md, shared header L1-33 and Verifier C section L213-390.
- prompts/01-gate-0-pipeline.md (full).
- prompts/07-emerging-moat-pipeline.md (full).

Artifacts audited:
- runs/supremepwr-2026-10-06/outputs/reports/01-gate0.md
- runs/supremepwr-2026-10-06/outputs/blocks/B01-gate0.yaml
- runs/supremepwr-2026-10-06/outputs/reports/07-emoat.md
- runs/supremepwr-2026-10-06/outputs/blocks/B07-emoat.yaml

Read for format and flag meaning only: .claude/agents/verifier-c-framework.md (frontmatter); prompts/00-orchestrator.md L591-596 (FLAG-GATE0) and L642-657 (confidence delta); prompts/09-tam-pipeline.md L180-181 (consumer of capex_embedded_growth_pct); audits/PROMPT_AUDIT_2026-10.md L1960-1965 (VER-08, intended narrative field of this block); .claude/commands/run-pipeline.md L295-312 and .claude/commands/finalize.md L164-172 (phase split).

Anchor key:
- P01 = prompts/01-gate-0-pipeline.md, P07 = prompts/07-emerging-moat-pipeline.md, P12 = prompts/12-verifiers-pipeline.md, cited by line.
- R01 = reports/01-gate0.md, Y01 = blocks/B01-gate0.yaml, R07 = reports/07-emoat.md, Y07 = blocks/B07-emoat.yaml, cited by line.
- Method. I take each stated input value as given. Verifier A owns whether a number exists at its source anchor. I re-derive every score, band, total and classification from the stated inputs and the stated thresholds.

---

## 0. RESULT

- Gate 0: 48 rules checked, 45 PASS, 3 FAIL. All 3 fails are MINOR.
- Every Gate 0 block score re-derives exactly: A 15, B 9, C 18, D 14, E 14, core 70, moat 15, grand total 85, moats confirmed 4, STRONG, GOOD (R01 L96-L126; Y01 L16-L24).
- Emerging Moat: 30 rules checked, 29 PASS, 1 FAIL (MINOR).
- The adjusted score 8.3 and band NONE re-derive exactly (R07 L446-L448). No CLAIM-only or INFER-only category scores at the DOC multiplier.
- Combined: 78 checked, 74 PASS. Acceptance 94.9%. The denominator is 78, so the rate applies. The rate is above 60%, so it does not trigger REWORK.
- CRITICAL 0, MAJOR 0, MINOR 4. No finding changes a score band, a classification or a decision.
- Valuation section: pending phase 3.

The most decision-relevant item is an observation, not a fail (O2). Gate 0 GOOD versus AVERAGE rests on M3. M3 clears "FAT >2x" by Rs 0.46 Cr of net block. P01 does not define FAT. The maker used the conventional basis and disclosed the CWIP reading. An operator definition of FAT would close the gap.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

| # | Rule (source) | B01 states (anchor) | Re-derived from stated inputs | Result |
|---|---|---|---|---|
| G0-01 | Open with the data-availability line (P01 L23-25) | "Data available: 4 years (FY23 to FY26). Scoring adapted to 4-year history." (R01 L3) | Present in the required form | PASS |
| G0-02 | ROCE: use the source ROCE, else compute and say "computed" (P01 L29-31) | Data Sheet has no ROCE; computed as (PBT + interest) / (TA - CL) (R01 L36) | FY24 22.93/81.5 = 28.14%; FY25 28.59/105.7 = 27.05%; FY26 31.55/157.2 = 20.07% (R01 L37-39). FY23 NOT FOUND, not estimated (R01 L40) | PASS |
| G0-03 | ROE = PAT / average NW; earliest year on closing NW, stated (P01 L32-33) | FY23 59.9% on closing NW, stated; FY24 30.4%, FY25 22.4%, FY26 19.9% (R01 L42) | 10.82/18.06 = 59.9%; 14.00/45.98 = 30.4%; 18.60/83.2 = 22.4%; 20.44/102.7 = 19.9%. Basis note in O5 | PASS |
| G0-04 | WC days = Rec + Inv - Pay; basis stated (P01 L34-38) | Revenue basis stated (R01 L60; Y01 L31) | FY24 211.2 + 64.9 - 73.0 = 203.1; FY25 110.8 + 77.4 - 77.3 = 110.9; FY26 94.1 + 124.8 - 125.0 = 93.9 | PASS |
| G0-05 | FCF = CFO - capex (P01 L39-40) | FY25 37.69 - 39.78 = -2.09; FY26 25.90 - 57.48 = -31.58 (R01 L56) | Arithmetic matches | PASS |
| G0-06 | A1 median ROCE (P01 L55) | 27.05% -> 5 (R01 L46) | median(28.14, 27.05, 20.07) = 27.05, at or above 25 -> 5 | PASS |
| G0-07 | A2 minimum ROCE (P01 L56) | 20.07% -> 5 (R01 L47) | at or above 15 -> 5 | PASS |
| G0-08 | A3 median ROE (P01 L57) | 26.4% -> 5 (R01 L48) | median of 19.9, 22.4, 30.4, 59.9 = (22.4 + 30.4)/2 = 26.4, at or above 20 -> 5 | PASS |
| G0-09 | A4 ROCE trend (P01 L58-59) | FY26 vs FY24, -8.07pp -> 0 (R01 L49) | 20.07 - 28.14 = -8.07, decline over 5pp -> 0. FY24 is the earliest computable year. A FY23 NOT FOUND would also score 0 (P01 L20-22) | PASS |
| G0-10 | B1 cumulative CFO / cumulative PAT (P01 L62-63) | 58.11 / 63.86 = 0.91 -> 4 (R01 L55) | 5.25 - 10.73 + 37.69 + 25.90 = 58.11; 10.82 + 14.00 + 18.60 + 20.44 = 63.86; 0.910 is in 0.85-0.99 -> 4 | PASS |
| G0-11 | B2 FCF-positive years (P01 L64) | 0 of 2 evaluable years -> 0 (R01 L56) | 0% -> 0. NOT FOUND years score 0 (P01 L20-22). O1 shows 0 is determinate | PASS |
| G0-12 | B3 cumulative FCF / cumulative PAT (P01 L65-66) | -33.67 / 39.04, negative -> 0 (R01 L57) | -2.09 - 31.58 = -33.67; 18.60 + 20.44 = 39.04; negative -> 0 | PASS |
| G0-13 | B4 change in WC days (P01 L67-68) | -109.2 days -> 5 (R01 L58) | 93.9 - 203.1 = -109.2, decrease over 5 days -> 5 | PASS |
| G0-14 | C1 revenue CAGR (P01 L71) | 22.1% -> 5 (R01 L67) | (181.64/99.76)^(1/3) - 1 = 22.1% -> 5 | PASS |
| G0-15 | C2 PAT CAGR (P01 L72) | 23.6% -> 5 (R01 L68) | (20.44/10.82)^(1/3) - 1 = 23.6% -> 5 | PASS |
| G0-16 | C3 positive YoY revenue years (P01 L73) | 3 of 3 -> 5 (R01 L69) | 99.76 < 113.46 < 148.72 < 181.64 (R01 L19), 100% -> 5 | PASS |
| G0-17 | C4 PAT CAGR minus revenue CAGR (P01 L74) | +1.5pp -> 3 (R01 L70) | 23.6 - 22.1 = +1.5, inside the 3pp band -> 3 | PASS |
| G0-18 | CAGR edge rules (P01 L45-50) | Both endpoints positive; "No loss-to-profit swing" (R01 L72; Y01 L29) | No N/M CAGR; no swing; C4 not N/M | PASS |
| G0-19 | D1 net debt / EBITDA (P01 L77-79) | 40.22 / 32.83 = 1.23x -> 3 (R01 L78) | 49.97 - 9.75 = 40.22; 28.52 + 3.03 + 1.74 - 0.46 = 32.83; 1.225x in 1-2x -> 3. With other income kept in EBITDA (33.29) the ratio is 1.21x, same band | PASS |
| G0-20 | D2 EBIT / interest (P01 L80-82) | 10.41x, 10.26x ex other income -> 5 (R01 L79) | 31.55/3.03 = 10.41; 31.09/3.03 = 10.26; both at or above 10 -> 5 | PASS |
| G0-21 | D3 debt / equity (P01 L83-84) | 0.42 -> 4 (R01 L80) | 0.1-0.5 -> 4. Cross-check 49.97/112.9 = 0.44, same band | PASS |
| G0-22 | D4 current ratio (P01 L85-86) | 1.28 -> 2 (R01 L81) | 133.5/104.2 = 1.28, in 1.2-1.49 -> 2 | PASS |
| G0-23 | E1 promoter holding (P01 L89-90) | 57.16% -> 4 (R01 L89) | 50-59.9 -> 4. The AR's 52.07% also scores 4 | PASS |
| G0-24 | E2 three-year change (P01 L91-92) | NOT FOUND -> 0 (R01 L90) | NOT FOUND scores 0 (P01 L20-22). No estimate made. Sensitivity in O6 | PASS |
| G0-25 | E3 pledge (P01 L93) | 0% -> 5 (R01 L91) | 0% -> 5 | PASS |
| G0-26 | E4 contingent liabilities / NW (P01 L94-95) | nil / 112.9 = 0% -> 5 (R01 L92) | below 5% -> 5 | PASS |
| G0-27 | Block totals and core (P01 L54-95) | A 15, B 9, C 18, D 14, E 14, core 70 (R01 L96; Y01 L16-17) | A 5+5+5+0 = 15; B 4+0+0+5 = 9; C 5+5+5+3 = 18; D 3+5+4+2 = 14; E 4+0+5+5 = 14; sum 70 | PASS |
| G0-28 | M1 pricing power (P01 L102-104) | margin -0.12pp, revenue CAGR 22.1% -> 3 (R01 L104) | 18.07 - 18.19 = -0.12 (R01 L100), stable inside 2pp, CAGR at or above 10% -> 3 | PASS |
| G0-29 | M2 cost advantage (P01 L105-106) | PEER DATA NEEDED -> 0 (R01 L105) | Test needs a peer median; not provided -> 0 and marked (P01 L99-100) | PASS |
| G0-30 | M3 capital efficiency (P01 L107-108) | FAT 2.01x, ROCE 20.07% -> 3 (R01 L106) | 181.64/90.36 = 2.010, above 2x; 20.07% above 15% -> 3. Tier 5 fails on FAT not above 3x. FAT is undefined in P01; see O2 | PASS |
| G0-31 | M4 customer stickiness (P01 L109-111) | zero decline years; receivable days not within 10 -> 3 (R01 L107) | Tier 5 fails: 119.3 to 94.1 is -25.2 days. Tier 3 "max 1 decline year" holds at 0 -> 3 | PASS |
| G0-32 | M5 scale (P01 L112-113) | PEER DATA NEEDED -> 0 (R01 L108) | Needs segment market-cap ranks -> 0 and marked | PASS |
| G0-33 | M6 R&D (P01 L114-116; marking rule P01 L99-100) | "R&D spend NOT FOUND in AR; PEER DATA NEEDED" -> 0 (R01 L109; Y01 L37) | Score 0 holds. The mark is wrong: tiers 5 and 3 are company-only tests; only tier 1 uses a peer median. See F1 | FAIL (MINOR) |
| G0-34 | M7 regulatory (P01 L117-119) | "no licence or listed-player count in inputs" -> 0 (R01 L110) | Player count NOT FOUND -> 0 (P01 L20-22). See O4 | PASS |
| G0-35 | M8 distribution (P01 L120-122) | no reach data -> 0 (R01 L111) | Tender sales to utilities and EPCs, no distribution channel (R07 L55) -> "none" -> 0 | PASS |
| G0-36 | M9 brand (P01 L123-125) | PEER DATA NEEDED -> 0 (R01 L112) | Needs a peer gross-margin median -> 0 and marked | PASS |
| G0-37 | M10 switching costs (P01 L126-128) | revenue up every year; receivable days 119.3 to 94.1 -> 5 (R01 L113) | Grew every year; days fell 25.2, so "rose by 10 days or less over the period" holds -> 5. FY24 spike to 211.2 disclosed | PASS |
| G0-38 | M11 network effects (P01 L129-133) | under 6 years; S&A share 2.29% to 2.44%, rising -> 1, "scored conservatively" (R01 L114; Y01 L36) | Under 6 years the rule says score conservatively on the overall trend and state so. Growth above 15% with the ratio rising -> 1. Stated. See O3 | PASS |
| G0-39 | M12 negative WC (P01 L134-135) | 203.1, 110.9, 93.9, all above 45 -> 0 (R01 L115) | above 45 -> 0 | PASS |
| G0-40 | Moat score, present count, class (P01 L98-99, L137-138) | 15; M1, M3, M4, M10 present = 4; STRONG (R01 L117; Y01 L18, L20-21) | 3+0+3+3+0+0+0+0+0+5+1+0 = 15; four tests at 3 or more -> STRONG (4-5) | PASS |
| G0-41 | Grand total (P01 L163-166) | 85 / 160 (R01 L124; Y01 L19) | 70 + 15 = 85 | PASS |
| G0-42 | Classification matrix (P01 L146-149) | core 60-79 + STRONG = GOOD+ (R01 L125) | core 70 in 60-79 with STRONG -> GOOD+ | PASS |
| G0-43 | Data confidence adjustment (P01 L142-144) | 4 years LIMITED, one tier down -> GOOD (R01 L126; Y01 L22, L24) | 3-4 years -> LIMITED -> GOOD+ becomes GOOD | PASS |
| G0-44 | Deal-breakers 1-9 (P01 L151-159) | none fired (R01 L127; Y01 L23) | A 15 not below 8; B 9 not below 8; median ROCE 27.05%; CFO/PAT 0.91; pledge 0%; ND/EBITDA 1.23x; zero revenue-decline years; zero loss years; 4 years. None fires. Block B is 1 point above the deal-breaker 2 line, and O1 shows it is determinate | PASS |
| G0-45 | FLAG-GATE0 trigger (P01 L175-177; prompts/00-orchestrator.md L591-593) | FLAG-GATE0 raised (Y01 L13) with classification GOOD (Y01 L22) | Trigger is classification at or below AVERAGE, or a deal-breaker override. GOOD with none fired -> no flag. See F2 | FAIL (MINOR) |
| G0-46 | Report ends with exactly the template YAML (P01 L163-197) | Report YAML carries 14 keys (R01 L134-149), then a pointer line (R01 L150) | Template has 21 keys. Missing in the report copy: input_gaps, flags, data_years, fy_range, data_notes, block_b_trend, analyst_note (7). The block file Y01 is complete. See F3 | FAIL (MINOR) |
| G0-47 | Block file schema; data_notes; block_b_trend; analyst_note 200-word cap (P01 L168-197) | Y01 L1-41 | All 21 keys present. data_notes carry the swing note, proxy bases and PEER DATA NEEDED items. block_b_trend states a direction and its numbers. analyst_note is about 120 words | PASS |
| G0-48 | Dashboard elements (P01 L163-166) | moat bars (R01 L119-120); classification box (R01 L122-128); strongest and weakest block (R01 L130); decision line (R01 L132) | All present | PASS |

Gate 0 tally: 48 checked, 45 PASS, 3 FAIL (G0-33, G0-45, G0-46).

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule (source) | B07 states (anchor) | Check | Result |
|---|---|---|---|---|
| EM-01 | All six sections in one response (P07 L28) | Sections 1-6 at R07 L32, L72, L131, L384, L416, L473; register at L455 | All present | PASS |
| EM-02 | Three-tier evidence taxonomy on every item (P07 L29-34) | [DOC] / [CLAIM] / [INFER] mapped to the three classes (R07 L11-14); every ledger item tagged (R07 L137-191) | Mapping is one-to-one | PASS |
| EM-03 | Source anchor on every evidence item (P07 L35-36) | Every ledger row carries an anchor (R07 L139-191) | Present. Anchor accuracy belongs to Verifier A | PASS |
| EM-04 | NO EVIDENCE FOUND where none; no force-fit (P07 L39-40) | Stated for A2, A3, A4, B3, C1, D1, D2, E1, E2, F1, F2, H2, H3 (R07 L219-341); I1 and I2 scored 0 with leg-by-leg reasons (R07 L345, L347) | Compliant | PASS |
| EM-05 | Section 1: 1A with status labels, 1B, 1C table (P07 L49-55) | R07 L34-68; three-year mix stated NOT FOUND, not estimated (R07 L61) | Compliant | PASS |
| EM-06 | Sections 2A, 2B, 2D (P07 L57-63) | R07 L74-101, L121-127 | Compliant | PASS |
| EM-07 | 2C: capex x historical FAT, % above current revenue, arithmetic shown (P07 L60-62) | 95-100 x 1.52 = 144-152 Cr, midpoint 148.2, +82% of 181.64 (R07 L112, L117) | 97.5 x 1.52 = 148.2; 148.2/181.64 = 81.6% -> 82. Two readings and the separating observation stated (R07 L119). Year choice in O7 | PASS |
| EM-08 | Section 3: all 22 categories scanned (P07 L65-67) | Families A to I (R07 L193-347) | 22 of 22 | PASS |
| EM-09 | Summary table, 22 rows, four columns (P07 L155-156) | R07 L351-374 | 22 rows with evidence?, type, strength, time | PASS |
| EM-10 | Strong/Moderate count stated (P07 L157) | "2 (A1, B2)" (R07 L376) | Matches Section 5 | PASS |
| EM-11 | Completionist guard and recount line (P07 L41-46, L157-159) | "27 documented items across 13 rows or sections" (R07 L380; Y07 L36) | 6+3+3+3+2+2 = 19, plus D19-D26 = 8, total 27 = ledger D1-D27. Seven scored categories, below the 12 trigger. 13 equals the categories that hold a DOC item (A1, A2, A3, B2, C2, E2, F1, F2, G1, G2, H1, H2, I1) | PASS |
| EM-12 | Section 4: 4A, 4B, 4C (P07 L161-168) | R07 L386-412 | Compliant | PASS |
| EM-13 | Section 5: all 23 rows (P07 L171-174) | R07 L420-444 | 22 categories plus R1 | PASS |
| EM-14 | Likelihood x impact matrix values (P07 L172) | A1 MH 3; B1 ML 1; B2 MM 2; C2 ML 1; G1 ML 1; G2 ML 1; H1 ML 1 (R07 L422-439) | All seven match HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1 | PASS |
| EM-15 | Multiplier matches the stated tier; no CLAIM-only row scored as DOC (P07 L173; P12 L241-244) | A1 0.7 on its CLAIM qualification leg; B1 0.7 CLAIM; B2, C2, G1, G2 1.0 DOC; H1 0.5 INFER (R07 L422-439) | Each multiplier matches the tier of the load-bearing leg in its evidence table (R07 L197-207, L229-233, L243-248, L262-267, L300-305, L313-319, L329-333) | PASS |
| EM-16 | Adjusted total (P07 L173-174) | 8.3 (R07 L446; Y07 L30) | 2.1 + 0.7 + 2.0 + 1.0 + 1.0 + 1.0 + 0.5 = 8.3 | PASS |
| EM-17 | Absolute bands; UA qualifier (P07 L175-181) | NONE; "EM >= 25" not met (R07 L448; Y07 L31) | 8.3 below 12 -> NO MEANINGFUL EMERGING MOAT | PASS |
| EM-18 | I1/I2 contribution stated separately (P07 L180-181) | 0.0 (R07 L446) | Stated | PASS |
| EM-19 | I1 above 0 only with both legs and a DOC (b) leg (P07 L122-138; P12 L292-295) | 0; leg (a) fails, leg (b) absent (R07 L345) | Compliant | PASS |
| EM-20 | I2 above 0 only with a named, specific sacrifice (P07 L139-153; P12 L295-296) | 0; "nothing" must be destroyed (R07 L347) | Compliant | PASS |
| EM-21 | I2 answered for each moat claimed in the scan (P07 L139-141) | Answered "for the one moat claimed (220 kV qualification)" (R07 L347) | The scan claims two Moderate moats, A1 and B2 (R07 L376; Y07 L33-34). B2 is not addressed. I2 stays 0. See F4 | FAIL (MINOR) |
| EM-22 | One improvement, one mechanism (CLAUDE.md NEVER list; R1 scoring P07 L161-174) | 220 kV credited once in A1, R1 = 0 (R07 L412); D16 counted once (R07 L380); Danya not credited (R07 L237) | No double credit found | PASS |
| EM-23 | Optionality Register: schema, rows, carried in YAML (P07 L183-196) | 9 rows (R07 L459-469; Y07 L45-54) | Covers the CLAIM-only B1 items, the INFER-only H1 item, and zero-score forward items (exports, refurbishment, data-centre, 330 kV) | PASS |
| EM-24 | 6A timeline; 6B risks with early warnings (P07 L199-201) | R07 L475-494 | Compliant | PASS |
| EM-25 | 6C uses the injected Gate 0 block (P07 L201-203) | core 70, moat 15, total 85, 4 moats, STRONG, GOOD (R07 L500-505) | Matches Y01 L16-22 | PASS |
| EM-26 | 6D combined classification; HIGH POTENTIAL and TURNAROUND reasoning (P07 L203-208) | GOOD; both rows reasoned and rejected (R07 L513-517) | Reasoning present. The matrix cell is NOT VERIFIED because P07 does not carry the matrix (O9) | PASS (cell not verified) |
| EM-27 | 6E card: evolution map per family, 12-month catalysts, biggest risk (P07 L208-210) | R07 L523-545 | Compliant | PASS |
| EM-28 | F2 cross-references the injected promise-delivery record (P07 L106-107) | B05 record 4 delivered, 4 partial, 3 missed, grade C (R07 L287-294) | Compliant | PASS |
| EM-29 | YAML block (P07 L214-243) | Y07 L1-63; the report ends with the block (R07 L568-632) | All 19 template keys present. em_classification "NONE" is a valid token. active_categories holds only the two Moderate rows. evidence_mix 27/18/8 equals ledger counts D1-D27, C1-C18, I1-I8. analyst_note about 115 words | PASS |
| EM-30 | Categories 21 and 22 present (P12 L292-297) | I1 and I2 rows (R07 L373-374, L442-443) | Present | PASS |

Emerging Moat tally: 30 checked, 29 PASS, 1 FAIL (EM-21).

---

## 3. FINDINGS (FAIL ROWS)

**F1 (G0-33), MINOR. M6 carries a wrong PEER DATA NEEDED mark.**
- Claimed: M6 = 0, "R&D spend NOT FOUND in AR; PEER DATA NEEDED" (R01 L109). Y01 L37 lists M6 under PEER DATA NEEDED.
- Rule: P01 L99-100 marks PEER DATA NEEDED when a test needs peer data. P01 L114-116 makes tiers 5 and 3 company-only tests (R&D share, EBITDA margin, revenue CAGR). Only tier 1 uses a peer median.
- Recomputed: M6 = 0, unchanged. The binding gap is R&D spend, not peer data. Peer data cannot lift M6 above 1, which is below the "present" bar of 3.
- Cross-stage note: B07 reads "R&D expenditure Nil" in AR Annexure V L.5009-5034 (R07 L157). If Verifier A confirms that line, every M6 tier fails and M6 = 0 is determinate. Whether the line exists is Verifier A's call, not mine.
- Impact: none on Block F (15), moats confirmed (4) or classification (GOOD).
- Fix: stage 1 relabels M6 as "R&D Nil, 0% of revenue" (or "R&D NOT FOUND" if A does not confirm) and drops M6 from the PEER DATA NEEDED list.

**F2 (G0-45), MINOR. FLAG-GATE0 raised outside its trigger.**
- Claimed: FLAG-GATE0 raised (Y01 L13). Classification is GOOD (Y01 L22). No deal-breaker fired (Y01 L23).
- Rule: P01 L175-177 raises FLAG-GATE0 "if classification <= AVERAGE with historical depressors identified". prompts/00-orchestrator.md L591-593 ties the flag to Gate 0 AVERAGE or a deal-breaker override.
- Recomputed: the trigger is not met. GOOD carries no FLAG-GATE0. The fragility text already sits in data_notes (Y01 L35) and analyst_note (Y01 L41), where it belongs.
- Impact: presentational. B07 carried the flag (Y07 L29). Stage 13 will print FLAG-GATE0 as active with its depressor detail unless corrected.
- Fix: stage 1 drops the flag and keeps the fragility note. Or the operator rules that "fragile to AVERAGE" fires FLAG-GATE0.

**F3 (G0-46), MINOR. The report-embedded YAML is abridged and is not the last element.**
- Claimed: the fenced block in R01 L134-149 has 14 keys. Line R01 L150 follows it ("Full block: ...").
- Rule: P01 L163-166 says the report ends with exactly the template block (P01 L168-197, 21 keys).
- Recomputed: 7 keys are missing from the report copy: input_gaps, flags, data_years, fy_range, data_notes, block_b_trend, analyst_note. The block file Y01 carries all 21 keys, and its 14 shared values match the report copy.
- Impact: none on data. A reader of the report alone does not see the flags or data_notes.
- Fix: stage 1 pastes the full Y01 block as the report's last element.

**F4 (EM-21), MINOR. I2 answered for one of two claimed moats.**
- Claimed: "For the one moat claimed (220 kV qualification), the honest answer ... is nothing" (R07 L347).
- Rule: P07 L139-141 asks the I2 question "for each moat claimed anywhere in this scan".
- Recomputed: the scan claims two Moderate moats, A1 (2.1) and B2 (2.0) (R07 L376; Y07 L33-34), plus five Weak rows. B2 has no I2 answer. The maker's own B2 reading supplies it: state empanelments are access tickets open to any qualified vendor (R07 L250), so nothing must be destroyed. I2 stays 0. Total stays 8.3.
- Side note: the I2 sentence "A global OEM already holds the credential" (R07 L347) has no anchor. The AR line cited in the same paragraph (L1003-1006) supports "established manufacturers" only. Anchor accuracy is Verifier A's.
- Fix: stage 7 adds one I2 line for B2 and one line covering the Weak rows.

---

## 4. OBSERVATIONS (NOT COUNTED IN THE ACCEPTANCE RATE)

**O1. Block B is determinate at 9; the "may be understated" note is wrong.** Y01 L30 says B2 and B3 "may be understated" because FY23 and FY24 capex are NOT FOUND. FY24 CFO is -10.73 (R01 L25), so FY24 FCF is negative for any capex of zero or more. FY23 CFO is 5.25 (R01 L25), so FY23 FCF is at most 5.25. Best case for B2 is 1 positive year of 4 = 25%, still below 50% -> 0 (P01 L64). Best case cumulative FCF FY23-FY26 is 5.25 - 10.73 - 2.09 - 31.58 = -39.15, negative -> B3 0 (P01 L65-66). Block B = 9 holds under every FY23-FY24 capex value. Stage 13 should not repeat the "understated" caveat.

**O2. M3 decides GOOD versus AVERAGE on an undefined term with Rs 0.46 Cr of headroom.** FAT >2x needs net block below 181.64/2 = 90.82. Stated net block is 90.36 (R01 L106), so the margin is 0.46 Cr (revenue margin 0.92 Cr). P01 FORMULA DEFINITIONS (L27-41) do not define FAT: not the CWIP treatment, not the year, not closing versus average. The maker's basis (closing net block, CWIP and intangibles under development excluded, latest year) matches the screener convention. The maker disclosed the downside reading: with CWIP 29.35, FAT is 1.52x, M3 = 1, moats 3, MODERATE, classification AVERAGE (Y01 L35). The year dimension runs the other way. FY24 FAT on fixed assets including CWIP is 4.60x (R07 L106), and FY24 ROCE is 28.14% (R01 L37), a tier-5 pair. That reading adds 2 moat points and leaves the class unchanged. Both readings are stated here. Prompts/00-orchestrator.md L591 says Gate 0 AVERAGE caps nothing, so the decision effect is limited. Suggested operator ruling: define FAT in P01 L27-41.

**O3. The M3 fragility line depends on M11.** If M11 read "stable" (S&A share 2.29% to 2.44%, +0.15pp, R01 L114), it scores 3 under P01 L131-132. Moats present would be 5, still STRONG. Then M3 at 1 leaves 4 present (M1, M4, M10, M11), still STRONG and GOOD. P01 L129-131 tells the maker to score conservatively under 6 years, which binds M11 to 1. So the fragility line in Y01 L13 and L35 stands as written.

**O4. M7 statement versus the AR as read by B07.** B01 says "no licence ... in inputs" (R01 L110). B07 reads BIS licence 6700052811 in the AR (R07 L146, L395) and treats it as sector-wide. P01 does not define "regulated segment". If transformer making counts as regulated, the floor is 1 (">10 players", P01 L118-119): moat score 16, grand total 86, moats confirmed 4, classification GOOD, all unchanged. Whether the licence line exists is Verifier A's call.

**O5. ROE basis mix.** Net worth FY24-FY26 includes NCI (Y01 L28), FY23 net worth is screener equity plus reserves, and PAT is attributable. P01 L32-33 does not fix the NCI treatment. A3 median 26.4% sits 6.4pp above the 20% band edge, so the score does not move.

**O6. E2 sensitivity.** E2 NOT FOUND scores 0 correctly (P01 L20-22). If a listing-date baseline showed a change inside 1%, E2 = 3 and core = 73. If an increase of 1% or more, E2 = 5 and core = 75. Both stay in the 60-79 band. Classification unchanged.

**O7. The 2C stage figure is the low lens.** The stage figure 82 uses FY26 FAT 1.52x (R07 L112, L117). The maker states this FAT "understates steady state" because Kannur ran about five weeks in FY26 (R07 L108). Its denominator (119.71) already holds the Kannur assets being projected. P07 L60-62 does not fix the year, and the maker showed the FY25 lens (2.32x, +122% to +128%) and management's peak, plus the separating observation (R07 L119). So the rule is met. The FY24 pre-expansion turn of 4.60x (R07 L106) is not tabulated: 95-100 x 4.60 = 437-460 Cr, +241% to +253% of 181.64. Stage 9 receives only the 82 figure (prompts/09-tam-pipeline.md L180-181). Stage 9 and stage 11 should read 82 as the low lens, not the central one.

**O8. B2 score versus its own reading.** The maker says empanelments "do not lock a customer in" (R07 L250), then scores B2 "Qualification lock-in" at MM 2.0 (R07 L427). The evidence tier (DOC, 1.0) is correct, so rule 3 of P12 is met. The likelihood and impact grades sit with the maker. If either grade were L, B2 = 1.0 and the total = 7.3, still NONE. The symmetric bar applies: a credit whose defining property the maker calls absent deserves the same scrutiny as a bear call without evidence.

**O9. The 6D matrix is not in the rule file.** P07 L203-205 cites "the standard matrix" and lists its labels but does not carry its cells. The maker said so and applied the labels by name (R07 L511). In phase-1 scope I may not load the Master, so the GOOD cell is NOT VERIFIED. Fix options: carry the matrix into P07, or verify the cell at phase 3.

**O10. "Registered options are never scored" wording.** P07 L184-185 defines the register as items that "scored 0 or rest only on CLAIM/INFER evidence", and P07 L196 says "Registered options are watched, never scored". Section 5 scores CLAIM at 0.7x and INFER at 0.5x (P07 L173). B07 scored B1 (0.7, CLAIM-only) and H1 (0.5, INFER-only) and also registered them. I read the register as adding no score of its own, with Section 5 governing, so B07 complies. Under the other reading the total is 8.3 - 0.7 - 0.5 = 7.1, still NONE. The operator may want to clarify the wording.

**O11. Template defect in P12 L379.** The line that should hold the rule 9 narrative field holds an edit instruction instead: '(same line, comment "# rule 9; any fail = REWORK stage 13")'. audits/PROMPT_AUDIT_2026-10.md VER-08 (L1960-1965) shows the intended line: the business_understanding_narrative field with the rule 9 comment. The applied patch replaced the whole line. This block emits the intended key with null values, pending /finalize. Operator fix: restore the field line in P12 L379.

**O12. Input wiring for rules 6, 9 and 10.** Rule 6 needs B09, rule 9 needs the stage 13 synthesis, and rule 10 needs the 09b dossier. Neither INPUTS line (P12 L389-390) names B09, the stage 13 output, or the 09b dossier. The orchestrator should confirm how these three rules receive their artifacts.

**O13. Deferred to Verifier A.** The M11 S&A ratios (R01 L114) have no anchor and no raw series line in R01 L17-32. B01 and B07 differ at rounding level on borrowings (49.97 vs 49.98) and FY25 borrowings (18.75 vs 18.74) (Y01 L39; Y07 L28). B01's analyst_note cites "20-25% utilisation (operator context, unverified)" (Y01 L41). These are source-fidelity questions, not framework questions.

---

## 5. RULES OUTSIDE PHASE-1 SCOPE

| P12 rule | Subject | Status |
|---|---|---|
| 4, 5 | Valuation (B11) growth symmetry and pillar mechanics; severity on destination PE | Pending phase 3 |
| 6 | B09 downstream candidates; stage 11 catalyst citations | Not checked: B09 is not among the phase-1 inputs (O12) |
| 7 | Method plurality (B11) | Pending phase 3 |
| 8 | Categories 21 and 22 in B07 | Checked in phase 1 (EM-19, EM-20, EM-30): PASS |
| 9 | Business Understanding Narrative (stage 13) | Pending /finalize |
| 10 | Halt 1 dossier (B09b) | Fires at /finalize; phase-1 structural check sits in run-pipeline step 6b |
| 11, 12 | Role 1 exit construction; Amendment 19 FV path | Pending phase 3 |
| 13, 14 | Expectation Ledger and decomposition gates | Pending phase 3 |
| 15 | Skill-to-source fidelity (section-1b) | Pending phase 3 |

## 6. VALUATION

Pending phase 3. B10 and B11 do not exist yet. Not run. No valuation framework document was read.

## 7. ACCEPTANCE ARITHMETIC

- Gate 0: 45 / 48 = 93.8%.
- Emerging Moat: 29 / 30 = 96.7%.
- Phase-1 combined: 74 / 78 = 94.9%. Denominator 78 (4 or more), so the rate applies (P12 L11-14). Above 60%: no REWORK trigger.
- Severity: CRITICAL 0, MAJOR 0, MINOR 4.

```yaml
stage: B12c
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete  # phase-1 scope complete (Gate 0 + Emerging Moat); valuation half pending phase 3
gate0: {rules_checked: 48, fails: ["G0-33 M6 marked PEER DATA NEEDED; tiers 5 and 3 need no peer data; score 0 unchanged (MINOR)", "G0-45 FLAG-GATE0 raised on classification GOOD; trigger is <= AVERAGE or a deal-breaker override (MINOR)", "G0-46 report-embedded YAML carries 14 of 21 template keys and is not the final element; block file complete (MINOR)"]}
emoat: {rules_checked: 30, fails: ["EM-21 I2 answered for the 220 kV moat only; B2 (Moderate) not addressed; I2 = 0 unchanged (MINOR)"]}
valuation: {rules_checked: 0, fails: []}  # pending phase 3: B10/B11 not yet produced; valuation framework docs not loaded
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; pending phase 3; any fail = REWORK stage 11
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}  # rule 9; any fail = REWORK stage 13; pending /finalize (field restored per PROMPT_AUDIT VER-08, see O11)
recomputed_destination_pe: ""  # pending phase 3
recomputed_decision: ""        # pending phase 3
findings:
  - id: "F1"
    rule_row: "G0-33"
    stage: "B01"
    severity: "MINOR"
    rule: "P01 L99-100 (mark PEER DATA NEEDED only when the test needs peer data); P01 L114-116 (M6 tiers 5 and 3 are company-only; only tier 1 uses a peer median)"
    claimed: "M6 = 0, 'R&D spend NOT FOUND in AR; PEER DATA NEEDED' (01-gate0.md L109; B01-gate0.yaml L37)"
    recomputed: "M6 = 0, unchanged. Binding gap is R&D spend, not peer data. B07 reads R&D expenditure Nil in AR Annexure V L.5009-5034 (07-emoat.md L157); if Verifier A confirms, every M6 tier fails and M6 = 0 is determinate"
    impact: "none on Block F (15), moats confirmed (4) or classification (GOOD)"
    fix: "stage 1: relabel M6 'R&D Nil, 0% of revenue' (or 'R&D NOT FOUND' if A does not confirm); remove M6 from the PEER DATA NEEDED list"
  - id: "F2"
    rule_row: "G0-45"
    stage: "B01"
    severity: "MINOR"
    rule: "P01 L175-177 (FLAG-GATE0 if classification <= AVERAGE with historical depressors); prompts/00-orchestrator.md L591-593"
    claimed: "FLAG-GATE0 raised (B01-gate0.yaml L13) with classification GOOD (L22) and no deal-breaker (L23)"
    recomputed: "trigger not met; GOOD carries no FLAG-GATE0. Fragility text already in data_notes (B01-gate0.yaml L35) and analyst_note (L41)"
    impact: "presentational; B07 carried the flag (B07-emoat.yaml L29), so stage 13 will print FLAG-GATE0 as active unless corrected"
    fix: "stage 1: drop the flag and keep the fragility note, or operator rules that 'fragile to AVERAGE' fires FLAG-GATE0"
  - id: "F3"
    rule_row: "G0-46"
    stage: "B01"
    severity: "MINOR"
    rule: "P01 L163-166 (report ends with exactly the template YAML block, P01 L168-197, 21 keys)"
    claimed: "report YAML (01-gate0.md L134-149) has 14 keys and is followed by a pointer line (L150)"
    recomputed: "7 keys missing from the report copy: input_gaps, flags, data_years, fy_range, data_notes, block_b_trend, analyst_note. Block file B01-gate0.yaml has all 21 keys; shared values match"
    impact: "none on data; a reader of the report alone misses flags and data_notes"
    fix: "stage 1: paste the full B01-gate0.yaml block as the report's last element"
  - id: "F4"
    rule_row: "EM-21"
    stage: "B07"
    severity: "MINOR"
    rule: "P07 L139-141 (I2 question asked for each moat claimed anywhere in the scan)"
    claimed: "I2 answered 'for the one moat claimed (220 kV qualification)' (07-emoat.md L347)"
    recomputed: "scan claims two Moderate moats, A1 2.1 and B2 2.0 (07-emoat.md L376; B07-emoat.yaml L33-34). B2 unanswered; maker's own B2 reading (L250, access tickets open to any qualified vendor) gives 'nothing must be destroyed'. I2 = 0 and total 8.3 unchanged"
    impact: "none on em_score (8.3) or band (NONE)"
    fix: "stage 7: add an I2 line for B2 and one line covering the five Weak rows"
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 94.9  # 74 passed / 78 checked (Gate 0 45/48, Emerging Moat 29/30); phase-1 scope; denominator >= 4 so applicable
```
