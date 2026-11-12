# VERIFIER C: FRAMEWORK ADHERENCE (B12c), ONWARDTEC, run 2026-11-12

Scope: phase 1. This run audits Gate 0 (B01) and the Emerging Moat scan (B07) only. The valuation half (Verifier C rules 4 and 5 for B11, 7, 11 to 15) waits for B10 and B11 in phase 3. Rule 8 (stage 7 categories 21 and 22) is in scope and is checked here. Rule 6 (B09 downstream block) and rules 9 and 10 (stage 13, B09b at /finalize) are outside this invocation's named scope.

Inputs read: prompts/12-verifiers-pipeline.md (Verifier C section); prompts/01-gate-0-pipeline.md; prompts/07-emerging-moat-pipeline.md; runs/onwardtec-2026-11-12/outputs/reports/01-gate0.md; outputs/blocks/B01-gate0.yaml; outputs/reports/07-emoat.md; outputs/blocks/B07-emoat.yaml. Not read: Master Prompt, Section 1B layers, FTTCP (phase 3 only); source documents (Verifier A owns source fidelity).

Method. I re-derive every score from the inputs as B01 and B07 state them, against the thresholds as the two prompts write them. I take stated numbers as given. A misapplication fails once, at its source rule. Downstream threshold rows pass on the stated inputs, so one error is not counted twice.

Anchor key: "B01 L20" = line 20 of 01-gate0.md. "B01 blk" = B01-gate0.yaml. "B07 L272" = line 272 of 07-emoat.md. "B07 blk" = B07-emoat.yaml. "P01 L39" = line 39 of prompts/01-gate-0-pipeline.md. "P07 L60" = line 60 of prompts/07-emerging-moat-pipeline.md. "(rc)" = recomputed by this verifier from the stated inputs.

## SUMMARY

- 83 rules checked, 73 passed. Acceptance rate 88.0% (rc). Findings: 0 CRITICAL, 4 MAJOR, 9 MINOR.
- Gate 0 arithmetic is clean. Every band, block sum, the core score, the moat count, the matrix and the deal-breakers re-derive to B01's values on B01's stated inputs (B01 L13 to L66).
- All 4 MAJOR findings sit in Gate 0. Three are substitutions of a fixed formula or window (ROCE, FCF, E2). One is a suppression of the rule's own proxy (M9). B01 disclosed each one in data_notes (B01 blk). That disclosure is what lets this audit re-derive them.
- The as-applied GOOD+ (core 74, B01 L43) holds only on B01's proxies. On the rules as written, with B01's stated inputs, three inputs are NOT FOUND and score 0. The result is core 55, AVERAGE (rc). On a uniform-proxy reading the result is core 77, GOOD+ (rc). The spread comes from corpus gaps, not from company results. Part 1C names the documents that close it. I recommend the orchestrator carry this to Halt 1 as an open item.
- Emerging Moat mechanics are clean. All 23 rows, the matrix, the multipliers, the recount and the band re-derive to 12.4, MODEST (B07 L266, L270). The class sits 0.4 above the 12.0 line. Six single-step readings each give NONE. B07 disclosed one of them (B07 L272). No single-step reading lifts the class.
- No finding triggers REWORK. Acceptance is above 60% on a denominator of 83.

---

## PART 1: GATE 0 (B01)

### 1A. Rule-by-rule compliance

| # | Rule (source) | B01 value (anchor) | Re-derived (rc) | Result |
|---|---|---|---|---|
| R01 | Opening data line, min 3 years (P01 L23-25) | "Data available: 10 years (FY2017 to FY2026)" (B01 L3) | present | PASS |
| R02 | Data confidence, history downgrade (P01 L142-144) | full, no downgrade (B01 L3, L66) | 10 yrs = full | PASS |
| R03 | ROCE = EBIT / (Total Assets - Current Liabilities), fixed (P01 L27, L29-31) | (PBT + Interest) / (Total assets - Other Liabilities) (B01 L6) | not as written | FAIL MAJOR (G0-F1) |
| R04 | ROE on average net worth, earliest-year basis stated (P01 L32-33) | FY17 on closing NW stated (B01 L15) | as written | PASS |
| R05 | WC days formula; missing input = NOT FOUND, 0 (P01 L34-38, L19-22) | payables NOT FOUND; B4 0, M12 0 (B01 L22, L61) | as written | PASS |
| R06 | FCF = CFO - Capex, exclude acquisitions, fixed (P01 L39-40) | proxy CFO + CFI, includes FY22 acquisition (B01 L20-23) | not as written | FAIL MAJOR (G0-F2) |
| R07 | CAGR = (End / Start)^(1/years) - 1 (P01 L41) | C1 10.4%, C2 30.3% (B01 L26-27) | (543.85/223.56)^(1/9) - 1 = 10.38%; (44.32/4.10)^(1/9) - 1 = 30.28% | PASS |
| R08 | CAGR edge rules (P01 L43-50) | positive endpoints; "No loss-to-profit swing" (B01 blk data_notes) | no N/M case | PASS |
| R09 | A1 median ROCE bands (P01 L55) | 14.79% = 1 (B01 L13) | (14.56 + 15.02) / 2 = 14.79; 10-14.9 = 1 | PASS |
| R10 | A2 min ROCE (P01 L56) | 10.33% = 1 (B01 L14) | 8-11.9 = 1 | PASS |
| R11 | A3 median ROE (P01 L57) | 13.56% = 2 (B01 L15) | (12.55 + 14.57) / 2 = 13.56; 12-14.9 = 2 | PASS |
| R12 | A4 ROCE trend (P01 L58-59) | 20.43 vs 13.87 = 5 (B01 L16) | latest >= earliest = 5 | PASS |
| R13 | Block A sum | 9 (B01 L5) | 1 + 1 + 2 + 5 = 9 | PASS |
| R14 | B1 cumulative CFO / PAT (P01 L62-63) | 1.51 = 5 (B01 L19) | 263.84 / 175.01 = 1.51; >= 1.00 = 5 | PASS |
| R15 | B2 FCF-positive years (P01 L64) | 90% = 4 (B01 L20) | 9 / 10 on the stated proxy; 75-99 = 4 | PASS |
| R16 | B3 cumulative FCF / PAT (P01 L65-66) | 0.58 = 3 (B01 L21) | 101.36 / 175.01 = 0.579 on the proxy; 0.40-0.59 = 3 | PASS |
| R17 | B4 WC days change (P01 L67-68) | NOT FOUND = 0 (B01 L22) | rule 5 | PASS |
| R18 | Block B sum | 12 (B01 L18) | 5 + 4 + 3 + 0 = 12 | PASS |
| R19 | C1 revenue CAGR (P01 L71) | 10.4% = 3 (B01 L26) | 10-14.9 = 3 | PASS |
| R20 | C2 PAT CAGR (P01 L72) | 30.3% = 5 (B01 L27) | >= 20 = 5 | PASS |
| R21 | C3 positive YoY years (P01 L73) | 8 of 9 = 3 (B01 L28) | 88.9%; 75-99 = 3 | PASS |
| R22 | C4 PAT CAGR minus revenue CAGR (P01 L74) | +19.9pp = 5 (B01 L29) | >= +3pp = 5 | PASS |
| R23 | Block C sum | 16 (B01 L25) | 3 + 5 + 3 + 5 = 16 | PASS |
| R24 | D1 net debt / EBITDA (P01 L77-79) | net cash = 5 (B01 L32) | 39.84 < 110.95 | PASS |
| R25 | D2 EBIT / interest (P01 L80-81) | 20.7x = 5 (B01 L33) | 59.93 / 2.89 = 20.74; >= 10 = 5 | PASS |
| R26 | D3 debt / equity (P01 L83-84) | 0.16 = 4 (B01 L34) | 39.84 / 253.50 = 0.157; 0.1-0.5 = 4 | PASS |
| R27 | D4 current ratio (P01 L85-86) | 3.66 = 5 (B01 L35) | 26,302.17 / 7,180.16 = 3.66; >= 2.0 = 5 | PASS |
| R28 | Block D sum | 19 (B01 L31) | 5 + 5 + 4 + 5 = 19 | PASS |
| R29 | E1 scored value (P01 L89-90) | 40.20% = 3 (B01 L38) | 40-49.9 = 3 | PASS |
| R30 | E1 band in B01's stated sensitivity (P01 L89-90) | "39.54% ... would still score 3" (B01 blk data_notes) | 30-39.9 = 1 | FAIL MINOR (G0-F5) |
| R31 | E2 change over 3 years (P01 L91-92) | +2.08pp over about 2.5 years = 5 (B01 L39) | 3-year start point NOT FOUND | FAIL MAJOR (G0-F3) |
| R32 | E3 pledge (P01 L93) | none = 5 (B01 L40) | 0% = 5 | PASS |
| R33 | E4 contingent liabilities / NW (P01 L94-95) | Nil = 5 (B01 L41) | < 5% = 5 | PASS |
| R34 | Block E sum | 18 (B01 L37) | 3 + 5 + 5 + 5 = 18 | PASS |
| R35 | Core score | 74 (B01 L43) | 9 + 12 + 16 + 19 + 18 = 74 | PASS |
| R36 | M1 pricing power (P01 L102-104) | 5 (B01 L50) | margin 5.01% to 13.21% = +8.20pp; CAGR 10.38% >= 10 | PASS |
| R37 | M2 cost advantage (P01 L105-106) | 0 (B01 L51) | 13.21 vs median 15.49 = -2.28pp, below | PASS |
| R38 | M3 capital efficiency (P01 L107-108) | 5 (B01 L52) | FAT 543.85 / 88.86 = 6.12x > 3; ROCE 20.43 > 20 (FY26) | PASS (finding G0-F6 on basis) |
| R39 | M4 stickiness (P01 L109-111) | 3 (B01 L53) | 1 decline year, recovered | PASS |
| R40 | M5 scale (P01 L112-113, L99-100) | 0, PEER DATA NEEDED (B01 L54) | segment universe not provided = 0 | PASS |
| R41 | M6 R&D (P01 L114-116) | 0 (B01 L55) | R&D NOT FOUND; margin below median | PASS |
| R42 | M7 regulatory (P01 L117-119) | 0 (B01 L56) | unregulated = 0 | PASS |
| R43 | M8 distribution (P01 L120-122) | 0 (B01 L57) | none = 0 | PASS |
| R44 | M9 brand, with the rule's GM proxy (P01 L123-125; P01 L13) | 0, proxy set aside as artifact (B01 L58) | proxy 100% vs 89.2% = +10.8pp; CAGR 10.4% = 5 | FAIL MAJOR (G0-F4) |
| R45 | M10 switching costs (P01 L126-128) | 3 (B01 L59) | all but 1 year; +1.2 days | PASS |
| R46 | M11 network effects (P01 L129-133) | 0 (B01 L60) | 7.2% < 17.5%; not >= 20; not > 15 | PASS |
| R47 | M12 negative WC (P01 L134-135) | 0, NOT FOUND (B01 L61) | rule 5; receivables alone 80.5 days > 45 = 0 either way | PASS |
| R48 | Moat score, count, class (P01 L98-99, L137-138) | 16; 4; STRONG (B01 L63) | 5 + 5 + 3 + 3 = 16; 4 present = STRONG | PASS |
| R49 | Classification matrix (P01 L146-149) | GOOD+ (B01 L66) | core 60-79 + STRONG = GOOD+ | PASS |
| R50 | Grand total | 90 (B01 L66) | 74 + 16 = 90 | PASS |
| R51 | Deal-breakers 1 to 9 (P01 L151-159) | none (B01 L66) | A 9 >= 8; B 12 >= 8; median ROCE 14.79 >= 10; CFO/PAT 1.51; pledge 0; net cash; 1 of 9 declines; PAT positive; 10 yrs | PASS |
| R52 | FLAG-GATE0 trigger (P01 L175-177) | raised at GOOD+ (B01 blk flags) | trigger is classification <= AVERAGE | FAIL MINOR (G0-F7) |
| R53 | YAML block of record, all fields (P01 L168-198) | B01 blk | 21 of 21 fields present | PASS |
| R54 | block_b_trend spec (P01 L191-192) | "stable" with two numbers (B01 blk) | cited CFO/PAT 1.16x to 1.47x reads improving | FAIL MINOR (G0-F8) |
| R55 | analyst_note <= 200 words (P01 L193-197) | about 108 words (B01 blk) | within cap | PASS |
| R56 | Report ends with the full fenced block (P01 L161-166) | 13-field block plus a pointer line (B01 L76-91) | 21 fields required | FAIL MINOR (G0-F9) |

Gate 0: 56 rules, 48 PASS, 8 FAIL.

### 1B. Recomputation under three readings

| Item | As applied (B01) | As written on B01's stated inputs (strict NOT FOUND) | Uniform proxy (B01's own proxy approach applied to all gaps) |
|---|---|---|---|
| Block A | 9 (B01 L5) | 2: A1, A2, A4 NOT FOUND = 0; A3 2 | 9 |
| Block B | 12 (B01 L18) | 5: B2, B3 NOT FOUND = 0; B4 0 | 15: B4 3 on receivable days (B01 blk data_notes B4) |
| Block C | 16 | 16 | 16 |
| Block D | 19 | 19 | 19 |
| Block E | 18 | 13: E2 NOT FOUND = 0 | 18 |
| Core | 74 | 55 | 77 |
| Moats present | M1 M3 M4 M10 = 4 | M1 M4 M9 M10 = 4 (M3 0, ROCE NOT FOUND; M9 5) | M1 M3 M4 M9 M10 = 5 |
| Moat score | 16 | 16 | 21 |
| Moat class | STRONG | STRONG | STRONG |
| Matrix result | GOOD+ | AVERAGE (core 40-59) | GOOD+ |
| Deal-breakers | none | DB1 (Block A 2 < 8) and DB2 (Block B 5 < 8): max GOOD | none |
| Classification | GOOD+ | AVERAGE | GOOD+ |
| Grand total | 90 | 71 | 98 |

Each substitution alone, all else as applied (rc):
- ROCE strict alone: Block A 2, M3 0, core 67. DB1 caps at GOOD. Result GOOD.
- FCF strict alone: Block B 5, core 67. DB2 caps at GOOD. Result GOOD.
- E2 strict alone: Block E 13, core 69. Result GOOD+.
- M9 as written alone: moat 21, 5 present. Result GOOD+.

### 1C. Documents that separate the readings

1. Current liabilities, FY17 to FY26: the balance sheets in the annual reports. FY26 and FY25 already sit on AR 2026 p.65, the page B01 used for D4 (B01 L35). The rule also accepts screener's own published ROCE row, anchored (P01 L30-31). Either route lets ROCE run as written.
2. Purchase of PPE and intangibles, and the FY22 acquisition outflow, FY17 to FY26: the cash flow statements in the annual reports. The screener Cash Flow sheet was exported empty (B01 blk input_gaps).
3. Promoter holding at Sep 2023: the Sep 2023 shareholding pattern (B01 blk data_notes E2 says Mar 2023 is not held).

With these, the formulas run as written and the strict reading falls away. The direction is then two-sided (1D).

### 1D. Band-edge register (as applied, both directions)

| Metric | Value (anchor) | Edge | Distance (rc) | Score now | Score across the edge |
|---|---|---|---|---|---|
| A1 median ROCE | 14.79% (B01 L13) | 15.0 | 0.21pp below | 1 | 3 |
| B3 FCF / PAT | 0.58 (B01 L21) | 0.60 | 0.02 below | 3 | 5 |
| E1 promoter | 40.20% (B01 L38) | 40.0 | 0.20pp above | 3 | 1 |
| C1 revenue CAGR | 10.38% (rc from B01 L26) | 10.0 | 0.38pp above | 3 | 1; M1 also falls 5 to 0, moats 3, MODERATE |
| M3 FY26 ROCE | 20.43% (B01 L52) | 20.0 | 0.43pp above | 5 | 3, still present |
| Block A vs DB1 | 9 (B01 L5) | < 8 | 1 point above | no cap | max GOOD |

Read: two edges lie just below a higher band (A1, B3). Four lie just above a lower band (E1, C1 with M1, M3, DB1). Upside exists: the uniform-proxy core 77 plus A1 at 3 and B3 at 5 gives 81 (rc), and core >= 80 with STRONG is EXCELLENT (P01 L147). With the 1C documents in hand, the classification can land from GOOD to EXCELLENT on these edges. Without them, the as-written result is AVERAGE.

### 1E. Gate 0 findings

**G0-F1. MAJOR. ROCE formula substituted (R03).**
- Location: B01 L6, L10, L13-16, L52; B01 blk data_notes (ROCE computed).
- Rule: P01 L27 "fixed, do not substitute alternatives"; P01 L29-31 ROCE = EBIT / (Total Assets - Current Liabilities); P01 L19-22 a missing data point is NOT FOUND and scores 0.
- Claimed: ROCE on (Total assets - Other Liabilities). Median 14.79%, min 10.33%, FY26 20.43%. Block A 9. M3 5.
- Recomputed: as written on B01's stated inputs, current liabilities are NOT FOUND for FY17 to FY24. A1, A2, A4 and M3 score 0. Block A is 2 and DB1 fires (max GOOD). Alone, this gives core 67, GOOD.
- Note: B01 disclosed the substitution. FY26 current liabilities (7,180.16 lakhs) sit on AR 2026 p.65 (B01 L35), so FY26 ROCE as written was computable and was not computed. FY26 drives A4 and M3. The proxy base equals equity plus all borrowings: 253.50 + 39.84 = 293.34 Cr, and 59.93 / 293.34 = 20.43% (rc from B01 L33-34). The as-written base adds non-current non-borrowing liabilities and removes current borrowings. The sign of the difference is NOT FOUND. A1 sits 0.21pp below the 15.0 edge, so the as-written series can lift A1 to 3. M3 stays present while FY26 ROCE exceeds 15%.

**G0-F2. MAJOR. FCF formula substituted (R06).**
- Location: B01 L20-23; B01 blk data_notes (FCF is a PROXY).
- Rule: P01 L27; P01 L39-40 FCF = CFO - Capex (PPE + intangibles), exclude acquisitions; P01 L19-22.
- Claimed: FCF proxy = CFO + CFI. B2 4 (9 of 10 years). B3 3 (101.36 / 175.01 = 0.58). Block B 12.
- Recomputed: as written on B01's stated inputs, capex is NOT FOUND. B2 and B3 score 0. Block B is 5 and DB2 fires (max GOOD). Alone, this gives core 67, GOOD.
- Note: B01 disclosed the substitution and named the exclusion it breached (B01 blk data_notes). The error runs both ways. B3 sits 0.02 below the 0.60 edge. Adding back any FY22 acquisition outflow above 3.65 Cr lifts B3 to 5 (rc: 0.60 x 175.01 - 101.36 = 3.65). The acquisition amount is NOT FOUND in B01. CFI also carries treasury flows that are not capex; their sign is NOT FOUND.

**G0-F3. MAJOR. E2 window is 2.5 years, not 3 (R31).**
- Location: B01 L39, L73; B01 blk data_notes (E2).
- Rule: P01 L91-92 promoter holding change over 3 years; P01 L19-22.
- Claimed: E2 5. 38.12% at Mar 2024 (AR 2025 p.147) to 40.20% at Sep 2026 = +2.08pp over about 2.5 years.
- Recomputed: as written, the Sep 2023 holding is NOT FOUND. E2 scores 0 and Block E is 13. Alone, this gives core 69, GOOD+ unchanged.
- Note: B01 disclosed the short window. B01 L73 records 61.71% at Mar 2021 as outside the run's inputs. That places a 23.59pp fall between Mar 2021 and Mar 2024 (rc: 61.71 - 38.12). Any part of that fall inside Sep 2023 to Mar 2024 lowers the true 3-year change. E2 can land anywhere from 0 to 5. Spear load-bearing fact 4 (the promoter-fall mechanism) sits on this window.

**G0-F4. MAJOR. M9 proxy set aside by judgment (R44).**
- Location: B01 L58; B01 blk data_notes (M9).
- Rule: P01 L13 "No qualitative judgments. Only numbers and the scoring rules provided."; P01 L123-125 "GM proxy if needed: (Revenue - Material Cost) / Revenue, state proxy used."
- Claimed: M9 0. The proxy is called a cost-classification artifact.
- Recomputed: as written, the proxy gives 100% against a peer median of 89.2%, which is +10.8pp. Revenue CAGR is 10.4%, at least 10%. M9 = 5. Moat score 21, 5 present, grand total 95. STRONG and GOOD+ do not change.
- Note: B01 disclosed the mechanical result. B01's economic point holds: LTTS also shows 100% (B01 blk data_notes M9). The defect is in the rule text for services firms. The fix is an operator ruling, not a stage judgment. With M9 = 5, the STRONG class no longer rests on M3 (see G0-F6).

**G0-F5. MINOR. E1 sensitivity misstated (R30).**
- Location: B01 blk data_notes (E1).
- Claimed: "39.54% on the fully diluted basis would still score 3."
- Recomputed: 39.54% is in the 30-39.9 band, which scores 1 (P01 L89-90). Block E would be 16 and core 72. GOOD+ does not change.
- Note: the scored value (40.20% undiluted = 3) stands. E1 sits 0.20pp above the 40.0 edge, and the note hides that.

**G0-F6. MINOR. M3 year basis not stated (R38 passes).**
- Location: B01 L52.
- Rule: P01 L107-108 names no year.
- Claimed: M3 5 on FY26 FAT 6.1x and FY26 ROCE 20.43%. The year is not stated.
- Recomputed: on the 10-year median ROCE (14.79%), M3 = 1 and is not present. Moats fall to 3, MODERATE, and core 74 + MODERATE = GOOD (P01 L148). With M9 as written (G0-F4), STRONG holds either way.
- Note: the rule passes on B01's reading. The gap is presentational: a basis that decides the class is not stated. An operator ruling on the M3 year basis would close it.

**G0-F7. MINOR. FLAG-GATE0 raised outside its trigger (R52).**
- Location: B01 blk flags.
- Claimed: FLAG-GATE0 with reason "No classification depressor: classification GOOD+ ...".
- Recomputed: the trigger is classification <= AVERAGE with historical depressors (P01 L175-177). It is not met as applied.
- Note: a consumer keyed on flag type reads a depressor flag that is not one. The watch items belong in data_notes or analyst_note. Under the strict as-written reading (AVERAGE), the flag becomes due, and its depressor is corpus gaps, not history.

**G0-F8. MINOR. block_b_trend label and number disagree (R54).**
- Location: B01 blk block_b_trend.
- Claimed: "stable: CFO/PAT 1.47x in FY26 (65.08/44.32) vs 1.16x in FY25; receivable days 80.5 FY26 vs 81.3 FY25".
- Recomputed: the spec asks for one label and the one number that shows it (P01 L191-192). CFO/PAT rose 0.31x (rc), which reads improving. Receivable days read stable. The field gives two numbers, and the label matches only one.
- Note: this field feeds FLAG-CASH. If "stable" discounts the FY26 PAT depressed by the 3.16 Cr exceptional (B01 blk data_notes), the field should say so.

**G0-F9. MINOR. Report block truncated (R56).**
- Location: B01 L76-91.
- Claimed: the report's fenced block carries 13 of 21 fields, then a pointer line.
- Recomputed: P01 L161-166 asks the report to end with the full block. The full block exists only at B01-gate0.yaml.
- Note: the omitted fields include data_notes, where every substitution in G0-F1 to G0-F4 is disclosed. A reader of the report alone does not see them.

---

## PART 2: EMERGING MOAT (B07)

### 2A. Rule-by-rule compliance

| # | Rule (source) | B07 (anchor) | Re-derived (rc) | Result |
|---|---|---|---|---|
| EM-R01 | Six sections plus register present (P07 L28) | Sections 1-6 and register (B07 L12-354) | all present, in order | PASS |
| EM-R02 | Evidence tag on every evidence item (P07 L29-34) | DOC / CLM / INF tags (B07 L3, Sections 1-4) | tags present on scored-row items | PASS |
| EM-R03 | Source anchor on every evidence item (P07 L35-36) | anchors present | presence only; fidelity is Verifier A's | PASS |
| EM-R04 | NO EVIDENCE FOUND, no force-fit (P07 L39-40) | 16 rows at none (B07 L99-185) | as written | PASS |
| EM-R05 | 22 categories plus R1 addressed (P07 L65-153, L161-168) | 22 in Section 3, R1 in Section 4 (B07 L97-233) | 23 of 23 | PASS |
| EM-R06 | Section 3 summary table, all rows, four columns (P07 L155-157) | 23 rows (B07 L189-213) | complete | PASS |
| EM-R07 | Strong/Moderate count stated (P07 L157-158) | 0 Strong, 2 Moderate (B07 L215) | B2, C1 Moderate | PASS |
| EM-R08 | Recount line in prescribed form (P07 L158-159) | "recount performed: 11 documented items across 6 categories" (B07 L217) | 11 items listed; they map to C1, B2, G1, F2, F1, R1 | PASS |
| EM-R09 | Completionist guard, 12 or more active (P07 L41-46) | 6 active (B07 L215) | below 12; inside the 3-6 base rate | PASS |
| EM-R10 | Likelihood x impact matrix (P07 L171-172) | B2 MM 2, C1 HM 3, F1 MM 2, F2 MM 2, G1 MM 2, R1 HL 2 (B07 L248-265) | values match the matrix | PASS |
| EM-R11 | Multipliers match tags (P07 L172-173) | DOC 1.0 on B2, C1, F2, G1, R1; CLM 0.7 on F1 | match | PASS |
| EM-R12 | No CLM-only row scored as DOC (Verifier C rule 3) | B2 DOC rests on deck-stated signed contracts, disclosed as the weakest DOC (B07 L217) | no CLM-only row at 1.0 | PASS (see EM-F1) |
| EM-R13 | Adjusted total | 12.4 (B07 L266) | 2.0 + 3.0 + 1.4 + 2.0 + 2.0 + 2.0 = 12.4 | PASS |
| EM-R14 | Classification band (P07 L175-176) | MODEST (B07 L270) | 12.4 in 12-24 = MODEST | PASS (see EM-F1, EM-F2) |
| EM-R15 | I1/I2 contribution stated separately (P07 L180-181) | 0.0 (B07 L268) | stated | PASS |
| EM-R16 | Verifier C rule 8: categories 21 and 22 present; I1 > 0 only with both legs and DOC on (b); I2 > 0 only with a named sacrifice | I1 0, I2 0 (B07 L184-185, L263-264) | present; both 0; no gate to test | PASS |
| EM-R17 | I2 question answered for each moat claimed (P07 L139-141) | answered for C1 and B2 only (B07 L185) | 4 of 6 scored rows unanswered | FAIL MINOR (EM-F3) |
| EM-R18 | Section 1: 1A statuses, 1B, 1C (P07 L48-55) | B07 L14-47 | present | PASS |
| EM-R19 | Section 2: 2A, 2B, 2D (P07 L57-63) | B07 L53-89 | present | PASS |
| EM-R20 | 2C arithmetic shown (P07 L60-62) | 25 x 11.37 = 284.3; 284.3 / 543.85 = 52.3% (B07 L80-83) | 284.25 / 543.85 = 52.27% | PASS |
| EM-R21 | 2C input is capex under execution, tagged per the taxonomy (P07 L60; L29; L37-38) | Rs 25 Cr, which B07 L64 calls "a spoken intent" | DOC committed figure Rs 3.31 Cr gives 6.9% | FAIL MINOR (EM-F4) |
| EM-R22 | Section 4: 4A, 4B with competitor-share column, 4C (P07 L161-168) | B07 L223-233 | present | PASS |
| EM-R23 | Optionality register: zero-scored or CLM/INF-only items, four columns, carried in block (P07 L183-196) | 8 rows in report and block (B07 L280-289; B07 blk) | match | PASS |
| EM-R24 | 6A to 6C; 6C uses the injected B01 values (P07 L199-203) | 74; 16/60; 4; STRONG; GOOD+ (B07 L319-321) | match B01 blk | PASS |
| EM-R25 | 6D with HIGH POTENTIAL and TURNAROUND reasoned; 6E card (P07 L203-210) | B07 L325-354 | present; matrix text not in my rule sources, checked for internal consistency | PASS |
| EM-R26 | YAML fields, enums, active_categories Strong/Moderate only (P07 L216-243) | B07 blk | all fields; "MODEST" valid; B2, C1 only | PASS |
| EM-R27 | analyst_note <= 200 words (P07 L239-242) | B07 blk | within cap | PASS |

Emerging Moat: 27 rules, 25 PASS, 2 FAIL.

### 2B. Recomputation

Scored rows (rc): B2 MM 2 x 1.0 = 2.0; C1 HM 3 x 1.0 = 3.0; F1 MM 2 x 0.7 = 1.4; F2 MM 2 x 1.0 = 2.0; G1 MM 2 x 1.0 = 2.0; R1 HL 2 x 1.0 = 2.0; 17 rows at 0. Total 12.4. Band 12-24 = MODEST. I concur with em_score 12.4 and em_classification MODEST (B07 blk). The single-credit split between B2 (tenor) and C1 (client count, revenue per client) is stated (B07 L118) and honoured in the scorecard.

### 2C. Boundary sensitivity, both directions

| Reading | Row change | Total (rc) | Class |
|---|---|---|---|
| As scored | none | 12.4 | MODEST |
| B2 at CLM | 2.0 to 1.4 | 11.8 | NONE |
| F1 one matrix step lower | 1.4 to 0.7 | 11.7 | NONE |
| F2 one matrix step lower | 2.0 to 1.0 | 11.4 | NONE |
| G1 one matrix step lower | 2.0 to 1.0 | 11.4 | NONE |
| G1 stripped | 2.0 to 0 | 10.4 | NONE |
| R1 stripped | 2.0 to 0 | 10.4 | NONE |
| G1 and R1 stripped (B07's reading two, B07 L272) | 4.0 to 0 | 8.4 | NONE |
| C1 one step higher (HH) | 3.0 to 4.0 | 13.4 | MODEST |
| B2 one step higher (HM) | 2.0 to 3.0 | 13.4 | MODEST |
| STRENGTHENING threshold | needs +12.6 | 25.0 | no single step reaches it |

Read: the class can fall on any one of six single-step readings and cannot rise on any one. B07 stated only the joint G1 plus R1 reading.

### 2D. Emerging Moat findings

**EM-F1. MINOR. Boundary sensitivity incomplete (EM-R14 passes).**
- Location: B07 L241-272; B07 blk flags FLAG-EM-THIN.
- Rule: P07 L170-176 (bands); Verifier C rule 3 (scores consistent with stated evidence).
- Claimed: one sensitivity. Strip G1 and R1 and the total is 8.4, NONE.
- Recomputed: six single-step readings each give NONE (2C table). No single step lifts the class.
- Note: the mechanics pass. Three rows graded Weak (F1, F2, G1; B07 L214, L215, L216) carry raw MM 2, the same raw as the Moderate B2. P07 sets no mapping from strength to the matrix, so this is a calibration gap, not a rule fail. B07 L217 calls B2's deck-stated contracts "the weakest" documented item in the set, and B2 at CLM alone drops the class. Carry MODEST as a boundary class and widen the FLAG-EM-THIN reason to name all six readings.

**EM-F2. MINOR. The named separator does not separate the two readings.**
- Location: B07 L272; B07 blk analyst_note.
- Rule: none in P07. The stage chose the two-readings device. I grade it because the separator enters the monitoring list.
- Claimed: the separator is "a second Rs 30 Cr-plus multi-year contract ... with the top-5 share not rising".
- Recomputed: that observation moves B2 and C1. It does not test whether G1 and R1 are forming moats. G1's own test is net cash growing while investing (P07 L109-111). FY26 met it: net cash 127.3 Cr with capex funded from CFO (B07 L173). H1 FY27 did not: 97.1 Cr after the buyback and dividend (B07 L173). The G1 separator is FY27 year-end net cash against FY27 capex and payouts. R1's reading turns on a framework question: does a shared, non-exclusive tailwind score above 0 (B07 L229, L233)? That needs an operator ruling, not an observation.

**EM-F3. MINOR. I2 answered for 2 of 6 scored rows (EM-R17).**
- Location: B07 L185.
- Rule: P07 L139-141 "For each moat claimed anywhere in this scan".
- Claimed: I2 0, answered for wallet share, the ODC and the renewal (C1, B2).
- Recomputed: six rows score above 0 (B07 L248-265). Four carry no I2 answer: F1, F2, G1, R1. The score stays 0. R1 is shared by every UK operator (B07 L229), and nothing in the scan names a sacrifice for F1, F2 or G1.

**EM-F4. MINOR. 2C input is a CLM figure; the DOC alternative is not shown (EM-R21).**
- Location: B07 L58, L61, L64, L80-85; B07 blk capex_embedded_growth_pct.
- Rule: P07 L60-62 "total capex under execution"; P07 L29 taxonomy on every piece of evidence; P07 L37-38 hard evidence over promises.
- Claimed: 52.3% = Rs 25 Cr x 11.37 / 543.85.
- Recomputed: B07's own 2A calls the Rs 25 Cr "a spoken intent" and the only committed capex Rs 3.31 Cr (AR26 p.87 note 26b, via B07 L61). On the committed figure: 3.31 x 11.37 = 37.6 Cr, which is 6.9% of FY26 revenue (rc).
- Note: FLAG-CAPEX-METHOD names the method problem (turnover on a headcount business), not the evidence tier. The block value carries no tag. Phase-3 pointer: stage 11 must not take 52.3% as a CAPACITY basis.

---

## PART 3: VALUATION (B10, B11): PENDING PHASE 3

Not run. B10 and B11 do not exist yet. Deferred to phase 3: Verifier C rules 4 and 5 (B11), 7 (method plurality), 11 (v3.8 exit construction), 12 (Amendment 19 FV path), 13 and 14 (Expectation Ledger and decomposition gates), 15 (skill-to-source fidelity). The valuation, expectation_ledger and business_understanding_narrative keys in the block carry status pending with null values, so the orchestrator reads no false fail.

---

## PART 4: OBSERVATIONS, NOT GRADED

- O1. Template defect. prompts/12-verifiers-pipeline.md line 379 reads `(same line, comment "# rule 9; any fail = REWORK stage 13")`. It is not a YAML key. I supply a `business_understanding_narrative` key with status pending in its place. Operator fix.
- O2. B01 L11 shows ROE 9.67% for both FY17 and FY20. Number fidelity belongs to Verifier A. Neither value affects the A3 median.
- O3. The B07 report copy of FLAG-CAPEX-METHOD says "PPE turnaround 11.37x" (B07 L372). The block file says "PPE turnover" (B07 blk). The block file is the copy of record. Cosmetic.
- O4. B07 6D rests on B01 GOOD+ (B07 L327). If Halt 1 re-scores B01 (Part 1B), 6D follows: GOOD or AVERAGE backward with MODEST forward.
- O5. B07 analyst_note says "Peers not read here, so I1/I2 score 0 on absence of any test". B07 L184 uses peer margins via B01 for the I1 (b) leg. Both routes give 0.
- O6. Phase-3 pointers: (a) capex_embedded_growth_pct 52.3 rests on a CLM capex figure and a method B07 calls non-informative (EM-F4). (b) G1 credits the net-cash cushion that Gate 0 Block D already scores, and B07 L173 says so. Check one improvement, one mechanism wherever EM feeds Pillar 3. (c) EM 12.4 is below the EM >= 25 UA qualifier (P07 L12-13). (d) If the Gate 0 classification changes at Halt 1, re-check any Section 1B input keyed to it.
- O7. Framework-text items for the operator. None is a stage error. (a) The M9 GM proxy gives 100% to any services firm without a material-cost line (G0-F4). (b) M3 names no year (G0-F6). (c) P01 does not say whether a disclosed, filed proxy may stand in for a missing input of a fixed formula. B01 used a proxy for three gaps (ROCE, FCF, E2) and NOT FOUND for the fourth (payables). A ruling on (c) settles the Part 1B spread.
- O8. Credit to the maker. B01 disclosed every substitution with its mechanical alternative. B07 stated its credit split and its weakest documented item. Without that disclosure, Part 1B and Part 2C could not be computed.

---

## COVERAGE STATEMENT

- Gate 0: 56 rules. Every scored metric (24), each block sum (5), core, moat sum and class, matrix, grand total, data confidence, deal-breakers (one rule for all nine tests), CAGR formula and edge rules, the four formula definitions (ROCE, ROE, WC days, FCF), the two stated sensitivities B01 relied on (E1, E2 window), and the YAML spec items (block of record, FLAG-GATE0 trigger, block_b_trend, analyst_note cap, report block). 48 PASS, 8 FAIL.
- Emerging Moat: 27 rules. Section presence, taxonomy and anchors, NO EVIDENCE handling, 23-row coverage, summary table, strength count, recount line, completionist guard, matrix and multipliers on all 6 scored rows, total, band, I1/I2 statement, Verifier C rule 8, I2 coverage, Sections 1, 2 (2C twice: arithmetic and input), 4 and 6, register, YAML and the analyst_note cap. 25 PASS, 2 FAIL.
- Total: 83 rules checked, 73 passed. Acceptance rate 73 / 83 = 88.0% (rc).
- Findings (13) and fails (10) differ on purpose. G0-F6, EM-F1 and EM-F2 are graded presentational findings on rules that pass. No rule failed for them.
- Numbers are taken as B01 and B07 state them. I opened no source document. Source fidelity is Verifier A's.

```yaml
stage: B12c
company: "ONWARDTEC"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation half deferred to phase 3 (B10/B11 not yet produced)"
gate0:
  rules_checked: 56
  rules_passed: 48
  fails:
    - "G0-R03 ROCE formula substituted: (PBT + Interest) / (Total assets - Other Liabilities) in place of EBIT / (Total Assets - Current Liabilities); FY26 current liabilities on AR 2026 p.65 not used (MAJOR, G0-F1)"
    - "G0-R06 FCF formula substituted: CFO + CFI, includes the FY22 acquisition the rule excludes; capex NOT FOUND (MAJOR, G0-F2)"
    - "G0-R31 E2 window 2.5 years (Mar 2024 to Sep 2026), not 3; Sep 2023 start NOT FOUND (MAJOR, G0-F3)"
    - "G0-R44 M9: the rule's own GM proxy set aside by qualitative judgment; as written M9 = 5 (MAJOR, G0-F4)"
    - "G0-R30 E1 sensitivity note: 39.54% scores 1 (30-39.9 band), not 3 (MINOR, G0-F5)"
    - "G0-R52 FLAG-GATE0 raised at GOOD+; trigger is classification <= AVERAGE (MINOR, G0-F7)"
    - "G0-R54 block_b_trend label 'stable' disagrees with its cited CFO/PAT 1.16x to 1.47x; spec asks one number (MINOR, G0-F8)"
    - "G0-R56 report ends with a 13-of-21-field block plus a pointer line, not the full block (MINOR, G0-F9)"
  as_applied: "core 74 (A 9, B 12, C 16, D 19, E 18); moat 16, 4 present, STRONG; GOOD+; grand total 90; arithmetic concurs"
  as_written_strict: "core 55 (A 2, B 5, C 16, D 19, E 13); moat 16, 4 present (M1 M4 M9 M10), STRONG; matrix AVERAGE; DB1 and DB2 fire; AVERAGE; grand total 71"
  uniform_proxy: "core 77 (B4 3); moat 21, 5 present, STRONG; GOOD+; grand total 98"
  separating_documents: "FY17-FY26 AR balance sheets (current liabilities) or screener's published ROCE row; FY17-FY26 AR cash flow statements (PPE and intangible purchases, FY22 acquisition outflow); Sep 2023 shareholding pattern"
  halt1_open_item: "Gate 0 classification spans AVERAGE (as written, corpus gaps) to GOOD+ (as applied); with the separating documents the band edges allow GOOD to EXCELLENT"
emoat:
  rules_checked: 27
  rules_passed: 25
  fails:
    - "EM-R17 I2 cannibalization question answered for B2 and C1 only; F1, F2, G1, R1 unanswered; score stays 0 (MINOR, EM-F3)"
    - "EM-R21 2C input is the Rs 25 Cr CLM figure B07's own 2A calls a spoken intent; on the DOC Rs 3.31 Cr committed figure 2C is 6.9%, not 52.3%; block value untagged (MINOR, EM-F4)"
  em_score_recomputed: 12.4
  em_class_recomputed: "MODEST (concur); boundary, 0.4 above 12.0; six single-step readings give NONE; no single step lifts the class"
valuation: {rules_checked: 0, fails: [], status: "pending phase 3: B10/B11 not yet produced"}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; not checked in phase 1
business_understanding_narrative: {status: "pending: stage 13 not yet produced; rule 9 fires at /finalize", fails: []}  # rule 9; any fail = REWORK stage 13; key supplied because template line 379 is malformed
recomputed_destination_pe: ""  # phase 3
recomputed_decision: ""        # phase 3
findings:
  - id: "G0-F1"
    severity: MAJOR
    location: "B01 L6, L10, L13-16, L52; B01 blk data_notes (ROCE computed)"
    rule: "P01 L27 fixed formulas; P01 L29-31 ROCE = EBIT / (Total Assets - Current Liabilities); P01 L19-22 missing input = NOT FOUND, 0"
    claimed: "ROCE on (Total assets - Other Liabilities); median 14.79%, min 10.33%, FY26 20.43%; Block A 9; M3 5"
    recomputed: "as written on B01 stated inputs: current liabilities NOT FOUND FY17-FY24; A1, A2, A4, M3 = 0; Block A 2; DB1 fires (max GOOD); alone core 67, GOOD"
    note: "Disclosed. FY26 current liabilities 7,180.16 lakhs are on AR 2026 p.65, used by B01 for D4, so FY26 ROCE as written was computable; FY26 drives A4 and M3. Proxy base = 253.50 + 39.84 = 293.34 Cr (rc). A1 sits 0.21pp below the 15.0 edge. M3 stays present while FY26 ROCE exceeds 15%."
  - id: "G0-F2"
    severity: MAJOR
    location: "B01 L20-23; B01 blk data_notes (FCF is a PROXY)"
    rule: "P01 L27; P01 L39-40 FCF = CFO - Capex, exclude acquisitions; P01 L19-22"
    claimed: "FCF proxy CFO + CFI; B2 4 (9 of 10), B3 3 (101.36 / 175.01 = 0.58); Block B 12"
    recomputed: "as written on B01 stated inputs: capex NOT FOUND; B2 = 0, B3 = 0; Block B 5; DB2 fires (max GOOD); alone core 67, GOOD"
    note: "Disclosed; B01 names the exclusion it breached. Two-sided: B3 sits 0.02 below the 0.60 edge; adding back any FY22 acquisition outflow above 3.65 Cr (rc) lifts B3 to 5. Acquisition amount NOT FOUND in B01."
  - id: "G0-F3"
    severity: MAJOR
    location: "B01 L39, L73; B01 blk data_notes (E2)"
    rule: "P01 L91-92 change over 3 years; P01 L19-22"
    claimed: "E2 5: 38.12% Mar 2024 (AR 2025 p.147) to 40.20% Sep 2026, +2.08pp over about 2.5 years"
    recomputed: "as written: Sep 2023 holding NOT FOUND; E2 = 0; Block E 13; alone core 69, GOOD+ unchanged"
    note: "Disclosed. B01 L73 records 61.71% at Mar 2021, a 23.59pp fall to Mar 2024 (rc); any part inside Sep 2023 to Mar 2024 lowers the true 3-year change; E2 can land from 0 to 5. Spear load-bearing fact 4 sits on this window."
  - id: "G0-F4"
    severity: MAJOR
    location: "B01 L58; B01 blk data_notes (M9)"
    rule: "P01 L13 no qualitative judgments; P01 L123-125 GM proxy if needed, state proxy used"
    claimed: "M9 0: proxy set aside as a cost-classification artifact"
    recomputed: "as written: proxy 100% vs peer median 89.2% = +10.8pp, revenue CAGR 10.4%; M9 = 5; moat 21, 5 present, grand total 95; STRONG and GOOD+ unchanged"
    note: "Disclosed with the mechanical result. B01's economic point holds (LTTS also 100%); the defect is in the rule text for services firms, so the fix is an operator ruling. With M9 = 5, STRONG no longer rests on M3."
  - id: "G0-F5"
    severity: MINOR
    location: "B01 blk data_notes (E1)"
    rule: "P01 L89-90 E1 bands"
    claimed: "39.54% on the fully diluted basis would still score 3"
    recomputed: "39.54% is in 30-39.9 = 1; Block E 16, core 72, GOOD+ unchanged"
    note: "Scored value 40.20% undiluted = 3 stands; E1 sits 0.20pp above the 40.0 edge and the note hides it."
  - id: "G0-F6"
    severity: MINOR
    location: "B01 L52"
    rule: "P01 L107-108 (no year named); rule passes on the stated reading"
    claimed: "M3 5 on FY26 FAT 6.1x and FY26 ROCE 20.43%; year not stated"
    recomputed: "on the 10-year median ROCE 14.79%, M3 = 1, moats 3, MODERATE, classification GOOD; with M9 as written STRONG holds either way"
    note: "Presentational: a class-deciding basis is not stated. Operator ruling invited on the M3 year basis."
  - id: "G0-F7"
    severity: MINOR
    location: "B01 blk flags"
    rule: "P01 L175-177 FLAG-GATE0 only if classification <= AVERAGE with historical depressors"
    claimed: "FLAG-GATE0 with reason 'No classification depressor: classification GOOD+'"
    recomputed: "trigger not met as applied; watch items belong in data_notes"
    note: "A consumer keyed on flag type reads a depressor flag that is not one. Under the strict as-written reading (AVERAGE) the flag becomes due, depressor = corpus gaps."
  - id: "G0-F8"
    severity: MINOR
    location: "B01 blk block_b_trend"
    rule: "P01 L191-192 label plus the one number that shows it"
    claimed: "stable: CFO/PAT 1.47x FY26 vs 1.16x FY25; receivable days 80.5 vs 81.3"
    recomputed: "CFO/PAT up 0.31x (rc) reads improving; receivable days read stable; two numbers, label matches one"
    note: "Feeds FLAG-CASH. If 'stable' discounts the FY26 PAT depressed by the 3.16 Cr exceptional, say so."
  - id: "G0-F9"
    severity: MINOR
    location: "B01 L76-91"
    rule: "P01 L161-166 end with exactly this fenced YAML block"
    claimed: "report block carries 13 of 21 fields, then a pointer line"
    recomputed: "full 21-field block exists only at B01-gate0.yaml"
    note: "The omitted fields include data_notes, where G0-F1 to G0-F4 are disclosed; a reader of the report alone does not see them."
  - id: "EM-F1"
    severity: MINOR
    location: "B07 L241-272; B07 blk flags FLAG-EM-THIN"
    rule: "P07 L170-176 bands; Verifier C rule 3; rule passes"
    claimed: "one sensitivity: strip G1 and R1 = 8.4, NONE"
    recomputed: "12.4 is 0.4 above 12.0; six single-step readings give NONE: B2 at CLM 11.8; F1 one step lower 11.7; F2 or G1 one step lower 11.4; G1 or R1 stripped 10.4; no single step lifts the class (STRENGTHENING needs +12.6)"
    note: "Weak rows F1, F2, G1 carry raw MM 2, the same raw as the Moderate B2; P07 sets no strength-to-matrix mapping, so calibration gap, not rule fail. Carry MODEST as a boundary class; widen the FLAG-EM-THIN reason."
  - id: "EM-F2"
    severity: MINOR
    location: "B07 L272; B07 blk analyst_note"
    rule: "none in P07 (stage chose the two-readings device); graded because the separator enters the monitoring list"
    claimed: "separator: a second Rs 30 Cr-plus multi-year contract with the top-5 share not rising"
    recomputed: "that observation moves B2 and C1, not G1 or R1; G1 separator is its own test (P07 L109-111): FY27 year-end net cash against FY27 capex and payouts (FY26 met it at 127.3 Cr; H1 FY27 97.1 Cr did not); R1 needs an operator ruling on whether a shared tailwind scores above 0"
    note: "Wrong separator would enter the monitoring checklist."
  - id: "EM-F3"
    severity: MINOR
    location: "B07 L185"
    rule: "P07 L139-141 I2 question for each moat claimed anywhere in the scan"
    claimed: "I2 0, answered for C1 and B2 only"
    recomputed: "6 scored rows; F1, F2, G1, R1 unanswered; score stays 0 (R1 shared by every UK operator, B07 L229; no sacrifice named for F1, F2, G1)"
    note: "No score effect."
  - id: "EM-F4"
    severity: MINOR
    location: "B07 L58, L61, L64, L80-85; B07 blk capex_embedded_growth_pct"
    rule: "P07 L60-62 capex under execution; P07 L29 taxonomy on every piece of evidence; P07 L37-38 hard evidence over promises"
    claimed: "52.3% = Rs 25 Cr x 11.37 / 543.85"
    recomputed: "on the committed DOC figure Rs 3.31 Cr (AR26 p.87 note 26b via B07 L61): 3.31 x 11.37 = 37.6 Cr, 6.9% of FY26 revenue (rc)"
    note: "B07 L64 calls the Rs 25 Cr a spoken intent. FLAG-CAPEX-METHOD names the method, not the evidence tier; block value untagged. Phase 3: stage 11 must not take 52.3% as a CAPACITY basis."
critical_count: 0
major_count: 4
minor_count: 9
acceptance_rate: 88.0             # rules passed / rules checked, % (73 / 83)
```
