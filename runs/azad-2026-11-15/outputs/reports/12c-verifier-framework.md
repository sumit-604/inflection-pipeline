# Verifier C: Framework Adherence, phase-1 scope. AZAD, run 2026-11-15

Scope: phase 1 only. This run covers the Gate 0 audit (B01) and the Emerging Moat audit (B07). The valuation half does not run, because B10 and B11 do not exist in phase 1. Verifier C rules 4, 5 (valuation part), 6, 7 and 9 to 15 are not run. The valuation section is PENDING PHASE 3.

Inputs read, and nothing else:
- prompts/12-verifiers-pipeline.md (Verifier C section)
- prompts/01-gate-0-pipeline.md (Gate 0 rule source)
- prompts/07-emerging-moat-pipeline.md (Emerging Moat rule source)
- runs/azad-2026-11-15/outputs/reports/01-gate0.md, including its ORCHESTRATOR APPENDIX
- runs/azad-2026-11-15/outputs/blocks/B01-gate0.yaml
- runs/azad-2026-11-15/outputs/reports/07-emoat.md, including its CAVEATS
- runs/azad-2026-11-15/outputs/blocks/B07-emoat.yaml

Not read: source PDFs (Verifier A owns source fidelity), other verifier outputs, B03, B04, B05 and B08 (B07 cites these, but they are not among my inputs).

Method: I re-derived every Gate 0 metric score from the numbers that B01 states, using the thresholds in prompts/01. I re-scored every Emerging Moat row from the evidence that B07 states, using the matrix and taxonomy in prompts/07. I did not test whether any stated number is in its source.

Block parity: B01-gate0.yaml is identical to the YAML in the 01-gate0.md ORCHESTRATOR APPENDIX. B07-emoat.yaml is identical to the YAML fenced inside 07-emoat.md.

Rule counts include four rows whose source is CLAUDE.md, not the two prompts: Gate 0 row 57, and Emerging Moat rows 2, 3 and 21. Each row names its source.

## SUMMARY

- Gate 0: 57 rules checked. 55 PASS, 2 FAIL, both MINOR. Every block score re-derives from the stated inputs. These also re-derive: core 53, moat 11, grand total 64, moat class MODERATE, classification AVERAGE, and deal-breakers DB1, DB2 and DB4. No recomputed value changes a total.
- Emerging Moat: 37 rules checked. 30 PASS, 7 FAIL: 1 MAJOR, 6 MINOR. The MAJOR is F2. B07 records F2 as documented (📄), Weak, with positive filed evidence, but scores it 0. The matrix gives 0 only when there is no evidence. Recomputed EM score: 13.0, still MODEST.
- The MODEST versus NONE band label is fragile in both directions. Under the contestable readings below, the EM total runs from 9.4 to 13.0 (grid in Part 2). Two outputs hold under every reading: the UA "EM >= 25" qualifier is not met, and the 6D combined classification stays AVERAGE.
- CRITICAL findings: 0. Acceptance rate: 85 of 94 rules = 90.4%. The denominator is 4 or more and the rate is above 60%, so this verifier sets no REWORK trigger.

## PART 1: GATE 0 (B01) COMPLIANCE

Line references are to 01-gate0.md unless stated. "Re-derived" means recomputed from the figures B01 states. It does not mean checked against the source.

| # | Rule (source) | Stated in B01 | Re-derived | Result |
|---|---|---|---|---|
| 1 | Opening data line (01 op rule 6) | "Data available: 6 years (FY21 to FY26). Scoring adapted to 6-year history" (l.3) | Present | PASS |
| 2 | Data confidence: 5-6 years = lower, flag "may not have seen full cycle" (01 Classification) | Lower, flag stated (l.3; data_notes) | 6 years = lower | PASS |
| 3 | History downgrade only at 3-4 years | history_downgrade: false | false | PASS |
| 4 | ROCE: use the source figure if it exists, else compute and say "computed" (01 Formula) | Computed; screener Data Sheet has no ROCE (l.24; input_gaps) | EBIT = PBT + interest: 21.59, 53.76, 65.54, 128.06, 142.42, 218.13. ROCE 15.04, 20.96, 14.86, 18.32, 8.73, 11.50 (B01 Block A table) | PASS |
| 5 | ROE on average net worth; earliest year on closing net worth, stated | FY21 on closing net worth, stated (l.37) | 12.65, 27.94, 5.23, 13.80, 8.57, 9.09. Median 10.87 | PASS |
| 6 | WC days formula; COGS basis only if COGS is explicit; basis stated | Revenue basis stated (l.45; data_notes) | FY21: 156.4 + 102.0 - 111.0 = 147.4. FY26: 188.7 + 199.2 - 51.6 = 336.3. Payable days from the stated payables in Mn agree (111.0, 51.6) | PASS |
| 7 | FCF = CFO - capex (PPE + intangibles), acquisitions excluded | Capex from cash flow statements, Mn / 10 (l.17, l.21) | Mn to Cr conversions agree. Six FCF values agree | PASS. Note: the capex line's make-up (PPE plus intangibles) is not itemised. No FCF year is near zero, so the score is not sensitive to it |
| 8 | CAGR formula and window | FY21 to FY26, 5 years | Revenue 37.5%, PAT 63.1% | PASS |
| 9 | CAGR edge rules (negative endpoints; loss-to-profit swing; C4 when N/M) | Both endpoints positive; no swing, noted in data_notes | Not triggered | PASS |
| 10 | A1 median ROCE | 14.95, score 1 (l.35) | (14.86 + 15.04) / 2 = 14.95 (14.953 before rounding). It falls in the gap between "10-14.9" and "15-19.9" | PASS. The gap is disclosed and has no written rule. The other reading gives 3: Block A 5, core 55, grand 66. AVERAGE is unchanged and DB1 still fires (5 < 8) |
| 11 | A2 minimum ROCE | 8.73 (FY25), score 1 | Band 8-11.9 | PASS |
| 12 | A3 median ROE | 10.87, score 0 | Below 12 | PASS |
| 13 | A4 ROCE trend | -3.54pp, score 1 | 11.50 - 15.04; band 3-5pp | PASS |
| 14 | Block A total | 3 | 1 + 1 + 0 + 1 | PASS |
| 15 | B1 cumulative CFO / PAT | -0.17, score 0 | -56.75 / 328.21 = -0.173 | PASS |
| 16 | B2 FCF-positive years | 0 of 6, score 0 | All six negative | PASS |
| 17 | B3 cumulative FCF / PAT | Negative, score 0 | Sum -1,220.97 agrees | PASS |
| 18 | B4 WC days change | +188.9 days, score 0 | 336.3 - 147.4 | PASS |
| 19 | Block B total | 0 | 0 + 0 + 0 + 0 | PASS |
| 20 | C1 revenue CAGR | 37.5%, score 5 | (602.98 / 122.72)^(1/5) - 1 = 37.5% | PASS |
| 21 | C2 PAT CAGR | 63.1%, score 5 | (132.88 / 11.50)^(1/5) - 1 = 63.1% | PASS |
| 22 | C3 positive YoY revenue years | 5 of 5, score 5 | All five years up | PASS |
| 23 | C4 PAT CAGR - revenue CAGR | +25.6pp, score 5 | 63.1 - 37.5 | PASS |
| 24 | Block C total | 20 | 5 x 4 | PASS |
| 25 | D1 net debt / EBITDA | 1.29x, score 3 | (474.32 - 184.59) / 225.32 = 1.286 | PASS. Note: the rule does not define net debt; B01 states its basis (borrowings including leases, less cash and bank). Score 4 needs net debt at or below 225.32 Cr, which is 64.41 Cr more cash-like assets than stated |
| 26 | D2 interest coverage | 7.08x, score 4 | 218.13 / 30.82 = 7.08. Without other income 5.60, same band | PASS |
| 27 | D3 debt / equity | 0.31, score 4 | 474.32 / 1,528.90 = 0.310 | PASS |
| 28 | D4 current ratio | 3.27, score 5 | 9,892.99 / 3,026.71 = 3.27. The Sep 2026 reference 2.49 also scores 5 | PASS. Note: "latest" read as FY26 audited, the same basis as the annual series. The Sep 2026 reading changes no D score on the figures given |
| 29 | Block D total | 16 | 3 + 4 + 4 + 5 | PASS |
| 30 | E1 promoter holding | 55.84%, score 4 | Band 50-59.9 | PASS |
| 31 | E2 promoter change over 3 years | -9.0pp, score 0 | Window Dec 2023 to Sep 2026 (2.75 years). Sep 2023 is NOT FOUND and disclosed. The basis mix (one promoter at the start, promoter group at the end) can only make the fall larger, so 0 is robust | PASS |
| 32 | E3 pledge | 0%, score 5 | | PASS |
| 33 | E4 contingent liabilities / net worth | 1.92%, score 5 | 19.67 + 2.13 + 220.94 + 50.59 = 293.33 Mn; / 15,288.36 = 1.92% | PASS |
| 34 | Block E total | 14 | 4 + 0 + 5 + 5 | PASS |
| 35 | Core score | 53 | 3 + 0 + 20 + 16 + 14 | PASS |
| 36 | M1 pricing power | 5 | Margin 22.94% to 37.37% = +14.43pp; revenue CAGR 37.5% | PASS. Note: the two endpoints use two derivations (FY21: sales less expense rows; FY26: sum of four quarterly operating-profit rows). The 12.4pp margin above the 2pp test makes the score insensitive to this |
| 37 | M2 cost advantage | 0, PEER DATA NEEDED | Rule: score 0 and mark | PASS |
| 38 | M3 capital efficiency | 0 | FAT 0.77x is below 1x, and ROCE 11.5% is below 12%. Every tier fails | PASS. Note: the 779.34 Cr denominator has no stated basis. B07 uses net PPE of 763.23 Cr (0.790x). Both are below 1x |
| 39 | M4 customer stickiness | 3 | Zero decline years. Receivable days +32.3 fails the 5-point tier. The 3-point tier ("max 1 decline year") holds and has no receivable condition | PASS |
| 40 | M5 scale | 0, PEER DATA NEEDED | | PASS |
| 41 | M6 R&D | 0 | R&D NIL fails every tier, whatever the peer data | PASS |
| 42 | M7 regulatory | 0, "unregulated" (l.78) | The determination has no anchor or basis. B07 Section 4A records the CEMILAC/DGAQA status as NOT FOUND | FAIL, MINOR. M7 stays 0: NOT FOUND scores 0 (01 op rule 5), and "regulated but >10 players" gives at most 1, with no change to the moats-present count |
| 43 | M8 distribution | 0 | B2B, no network | PASS |
| 44 | M9 brand | 0, PEER DATA NEEDED | | PASS |
| 45 | M10 switching costs | 0 | Revenue grew every year. The +32.3 day receivable rise fails the 5-point tier. The 3-point tier needs "stable". The 1-point tier needs 2+ decline years | PASS, applied as written. A ladder anomaly goes to the operator (note 2) |
| 46 | M11 network effects | 3. "Two-window test impossible" at 6 years; fallback used (l.82; data_notes) | The rule says the two-window test "needs >=6 years". 6 years meets that | FAIL, MINOR. Recomputed: the latest 3-year CAGR (FY23 to FY26, 33.8%) is below the prior window (FY21 to FY24, 40.6%; or FY21 to FY23, 43.2%), so the 5-point tier fails. The 3-point tier (CAGR >= 20%, S&A proxy 6.26% to 3.71%, declining) gives 3. Score unchanged |
| 47 | M12 float | 0 | WC days above 45 in all six years | PASS |
| 48 | Moat total, count, class | 11; 3 present (M1, M4, M11); MODERATE | 5 + 3 + 3 = 11. 2-3 present = MODERATE | PASS |
| 49 | Grand total | 64 | 53 + 11 | PASS |
| 50 | Classification matrix | AVERAGE | Core 40-59 = AVERAGE, whatever the moat class | PASS |
| 51 | Deal-breakers, with the years that drive them | DB1, DB2, DB4 fired; 3, 5, 6, 7, 8, 9 not; years named | DB1: A = 3 < 8. DB2: B = 0 < 8. DB4: -0.17 < 0.50. DB3: 14.95 >= 10. DB6: 1.29x and 7.08x. DB8: PAT positive FY24 to FY26. The binding cap is AVERAGE, the same as the classification | PASS |
| 52 | FLAG-GATE0 when classification is AVERAGE or lower with depressors | Raised; depressors and years named | | PASS |
| 53 | PEER DATA NEEDED and NOT FOUND discipline | M2, M5 and M9 are 0 and marked. E2 start date declared NOT FOUND | No peer figure guessed | PASS |
| 54 | data_notes content (swings, proxies, peer items) | All three classes present | | PASS |
| 55 | Output: dashboard plus closing YAML | Scorecard, moat table, classification, strongest and weakest block, decision line. YAML via ORCHESTRATOR APPENDIX, identical to the block file | Moat profile shown as a table, not as bars; content complete | PASS |
| 56 | block_b_trend and analyst_note cap of 200 words | "deteriorating" with numbers; note about 113 words | | PASS |
| 57 | Load-bearing facts carried (CLAUDE.md spear gate) | Four facts (l.90-94) | Present, but placed after the scorecard, not before | PASS |

Gate 0: 57 checked, 55 PASS, 2 FAIL (rows 42 and 46, both MINOR, no score change).

## PART 2: EMERGING MOAT (B07) COMPLIANCE

Line references are to 07-emoat.md unless stated.

| # | Rule (source) | Stated in B07 | Result |
|---|---|---|---|
| 1 | All six sections in one response (07 op rule 1) | Sections 1 to 6, plus Section 0 | PASS |
| 2 | Not FTTCP, never conflated (07 taxonomy note; CLAUDE.md) | Stated at l.3 | PASS |
| 3 | Load-bearing facts checked first (CLAUDE.md spear gate) | Section 0, four facts | PASS |
| 4 | Section 1: 1A statuses from the allowed set, 1B, 1C table | Present, with NOT FOUND fills | PASS |
| 5 | Section 2A columns: project, Rs Cr, funding, status, commissioning, capacity addition, % over current | No "% over current" column (l.51-58) | FAIL, MINOR |
| 6 | Section 2B utilisation per facility | NOT FOUND per plant, stated | PASS |
| 7 | Section 2C arithmetic shown | CWIP Mn 2,124.90 x 0.790 = Mn 1,678.7. That is 27.8% of FY26 revenue and 23.1% of H1 FY27 annualised. Re-derived: 6,029.75 / 7,632.31 = 0.790; 1,678.7 / 6,029.75 = 27.8% | PASS. Note: "capex under execution" is read as CWIP only. Adding the unspent QIP capex object (Mn 755.40, B01 data_notes) gives Mn 2,880.30 x 0.790 = Mn 2,275.4, or 37.7% |
| 8 | Section 2D new geography | Saudi MoU, 🎙️ only | PASS |
| 9 | All 23 categories addressed | 22 rows in the Section 3 table, plus R1 in Sections 4 and 5 | PASS |
| 10 | NO EVIDENCE FOUND discipline, no force-fit (07 op rule 5) | 17 rows NO EVIDENCE FOUND (15 in families A to H, plus I1 and I2). Adverse evidence named where found | PASS |
| 11 | Section 3 summary table plus Strong/Moderate count | 22 rows with evidence, type, strength and time. Count 3 (A1, B2, C1) | PASS |
| 12 | Evidence taxonomy applied correctly to every item (07 op rule 2) | The B2 item "customer-specific plants require ... delta qualification" comes from the Q2 concall (Q2C [page 15] lines 611-619) and is tagged 📄. The taxonomy puts a concall statement at 🎙️. The Safran MOU is tagged 📄 (l.26); an MOU is not a signed contract. 1A rows Arabelle and Landing gear have no type mark in the Evidence column (l.29-30) | FAIL, MINOR. No score change: B2 stays 📄 on four filed agreements, and Safran scores 0 |
| 13 | Source anchor on every evidence item (07 op rule 3) | Anchors present. CAVEATS disclose the .txt line numbers and the carried anchors. One line has no anchor ("The July record's four 30-48 month, 1,700+ component claims stand", l.114), and it is not scored | PASS |
| 14 | Completionist guard and the recount line in the written form | "📄 recount performed: 9 documented items across 4 scored categories". Nine items listed. 4 active categories, below the 12 trigger | PASS |
| 15 | Section 4 (R1): 4A, 4B, 4C | Present. 4B is NOT FOUND | PASS |
| 16 | Section 5 matrix as written | HH=4, HM/MH=3, HL/MM/LH=2, ML/LM/LL=1, none=0 (l.147) | PASS |
| 17 | Evidence multipliers | 📄 1.0 on A1, B2, C1 and R1 | PASS |
| 18 | Adjusted total | 3.0 + 4.0 + 3.0 + 2.0 = 12.0 | PASS |
| 19 | Full scoring table, all 23 rows | Six rows shown. 17 rows collapsed into "All 17 other rows" (l.157) | FAIL, MINOR. The collapsed line hides F2, the one zero row that has documented evidence |
| 20 | Score consistent with the stated evidence tier and strength (Verifier C rule 3) | See finding F-1 | FAIL, MAJOR. Recomputed F2 1.0; EM 13.0 |
| 21 | Single credit: one improvement, one mechanism (CLAUDE.md; the stage's own H2 ruling, l.269) | See finding F-2 | FAIL, MINOR. EM range 11.0 to 12.0 |
| 22 | R1 tier consistent with its evidence | The 📄 items are the BHEL rate contract (ANN 2026-10-12) and the DRDO engine delivery (ANN 2026-07-22). The policy leg rests on the deck (Q2P [page 10], CEA/NTPC/BHEL indigenisation chain), and 4B finds no named scheme | PASS. The filed items document enrolment in an indigenisation programme, which fits 4B "import substitution measures". Observation: at 🎙️ 0.7, R1 = 1.4 and EM = 11.4 (grid below) |
| 23 | Classification band | 12.0 is MODEST (12-24) | PASS |
| 24 | I1/I2 contribution stated separately for the review checkpoint | 0.0 (l.160) | PASS |
| 25 | Category 21, I1: above 0 only if both legs are evidenced, with leg (b) on a 📄 source (Verifier C rule 8) | Both legs NOT FOUND; score 0 | PASS |
| 26 | Category 22, I2: above 0 only if the named sacrifice is specific (Verifier C rule 8) | No sacrifice named; score 0 | PASS |
| 27 | I2 question answered "for each moat claimed anywhere in this scan" (07 Family I) | One collective answer for "Azad's position" (l.133) | FAIL, MINOR. I2 stays 0. Separate answers for A1, B2 and C1 are absent |
| 28 | Optionality register: four-column table; block matches report | The report has a July-status table (item, status, anchor) and a one-line list of 10 "current register" items "carried in the block" (l.177). The block carries 8 rows. Missing: the Baker Hughes oil and gas revenue line, and the OEM advance (USD 4.5 Mn). The four-column table is not in the report | FAIL, MINOR. The oil and gas line survives in catalysts_12m (Q4 FY27). The OEM advance survives only in the FLAG-CASH reason |
| 29 | Registered options are watched, never scored | Saudi, Safran, RR, Phase 2, landing gear, Arabelle and ATGG follow-on all score 0. MHI hot-section revenue is registered while the LTCPA is scored. These are distinct items | PASS |
| 30 | 6A timeline, four windows | Present | PASS |
| 31 | 6B risks with early warnings | Five risks with warnings. Two readings and the separating observation stated | PASS |
| 32 | 6C uses the injected Gate 0 block | Core 53, 3 moats, moat 11, MODERATE, grand 64, AVERAGE. All match B01 | PASS |
| 33 | 6D combined classification, with HIGH POTENTIAL and TURNAROUND reasoning | AVERAGE. The reasons HIGH POTENTIAL and TURNAROUND are not met are given | PASS. The standard matrix is not in the rule source, so I checked 6D only against the hint the source states |
| 34 | 6E final card | Present. Catalysts given by reference to the block | PASS |
| 35 | YAML schema | All keys present. em_classification "MODEST" is in the enum. active_categories holds only Strong/Moderate rows (R1, Weak, is excluded). analyst_note is about 125 words | PASS |
| 36 | Threshold-edge disclosure | FLAG-EM-THRESHOLD-EDGE raised | PASS. It names one reading only. The grid below adds the others |
| 37 | UA qualifier statement | "EM >= 25 not met" (l.163) | PASS |

Emerging Moat: 37 checked, 30 PASS, 7 FAIL (1 MAJOR, 6 MINOR).

### Finding F-1 (MAJOR): F2 is scored below the matrix floor

- Stated: the Section 3 table records F2 as "Mixed, scored 0 | 📄 | Weak" (l.94). The F2 evidence includes filed credit items: FY26 growth of +31.8% against about 30% guidance (AR26 [page 38]), and six plants built (l.127). The Section 5 score is 0, inside "All 17 other rows" (l.157).
- Rule: the 07 Section 5 matrix gives 0 only for "no evidence". Every evidenced row scores at least 1 (LL, ML or LM). The stage's own Weak 📄 row, R1, scores 2. So the stage scores its two Weak rows two different ways.
- Recomputed: F2 likelihood Low, impact Low or Medium, gives 1 x 📄 1.0 = 1.0. EM = 13.0, still MODEST. On this reading the stage's edge case (C1 at impact Low) gives 12.0, MODEST, not 11, NONE.
- The other reading: the evidence is mostly adverse, so there is no evidence of a forming execution moat, and 0 is right. On that reading, Section 3 must label F2 None, as it labels C2, G1 and G2. The stage chose neither form consistently. "Shown as a drag, not credited" (l.129) is not a mechanism in the rubric.
- Severity: the misapplication changes the score within the band and changes the edge flag's downside reading. No classification or decision changes. That makes it MAJOR under Verifier C rule 5.

### Finding F-2 (MINOR): A1 and B2 share their lead evidence with no separation line

- Stated: the MHI 8-year single-source LTCPA (ANN 2026-03-26) is the lead item in A1 (l.106) and the first item in B2 (l.112). A1's other 📄 item, the AS9100D and Nadcap certificates (l.107), is a B2 rubric item ("IATF/AS9100/NADCAP/cGMP certs"). The stage applied the single-credit rule to H2 against B2 (analyst_note), but gives no line on why A1 and B2 may both draw on the MHI filing.
- Recomputed range: if capability (A1) and lock-in (B2) are stated as separate mechanisms, A1 stays 3.0 and EM stays 12.0. If the MHI filing is held in B2 only, A1 rests on the certificates (📄) plus the 🎙️ qualification timeline of 30-48 months. At M x M = 2.0, EM is 11.0, NONE.
- B2 and C1 also share the Baker Hughes 2026-04-23 filing and the dedicated plants. That overlap has no score effect: B2 is at HH = 4 on its four filed multi-year agreements alone.
- Fix: one line in A1 that names the mechanism A1 credits and the mechanism B2 credits.

### Emerging Moat sensitivity grid (recomputed from the B07 Section 5 rows)

| Reading | A1 | B2 | C1 | R1 | F2 | Total | Class |
|---|---|---|---|---|---|---|---|
| As scored by B07 | 3.0 | 4.0 | 3.0 | 2.0 | 0 | 12.0 | MODEST |
| F2 at matrix floor (F-1) | 3.0 | 4.0 | 3.0 | 2.0 | 1.0 | 13.0 | MODEST |
| C1 impact Low (the stage's own edge case) | 3.0 | 4.0 | 2.0 | 2.0 | 0 | 11.0 | NONE |
| C1 Low with F2 floor | 3.0 | 4.0 | 2.0 | 2.0 | 1.0 | 12.0 | MODEST |
| A1 on unshared evidence, M x M (F-2) | 2.0 | 4.0 | 3.0 | 2.0 | 0 | 11.0 | NONE |
| A1 M x M with F2 floor | 2.0 | 4.0 | 3.0 | 2.0 | 1.0 | 12.0 | MODEST |
| R1 policy leg at 🎙️ 0.7 (row 22 observation) | 3.0 | 4.0 | 3.0 | 1.4 | 0 | 11.4 | NONE |
| R1 at 🎙️ with F2 floor | 3.0 | 4.0 | 3.0 | 1.4 | 1.0 | 12.4 | MODEST |
| All three downside readings, F2 at 0 | 2.0 | 4.0 | 2.0 | 1.4 | 0 | 9.4 | NONE |
| All three downside readings, F2 floor | 2.0 | 4.0 | 2.0 | 1.4 | 1.0 | 10.4 | NONE |

Two readings and the separating observation. Reading MODEST: the filed contracts and plants form a real but small emerging position. Reading NONE: the scan double-uses its lead filing, and C1 has no filed volume terms. Two items separate them. The first is a filed take-or-pay or minimum-volume term on any dedicated plant (C1 impact; NOT FOUND in B07 input_gaps). The second is a stated separate mechanism for the MHI filing in A1. These two hold under every reading: the UA "EM >= 25" qualifier is not met (maximum 13.0), and 6D stays AVERAGE (no reading reaches STRENGTHENING or EXPANSION).

## PART 3: VALUATION (B10, B11): PENDING PHASE 3

Not run. B10 and B11 do not exist in phase 1. The phase-1 task excludes Verifier C rules 4, 5 (valuation part), 6 (B09 downstream candidates: B09 is not among my inputs), 7, and 9 to 15. The expectation-ledger fields in the block are null, which means not checked. Null is not a fail.

## ROUTED TO VERIFIER A (source and basis questions, not counted here)

1. Top-5 customer concentration. B01 gives two readings, 28.4% inclusive or 47.0% "top 5 other than above" (AR2026 p.242), and asks a verifier to settle it (B01 data_notes). B07 Section 0 carries 47.02% only. This is a source-reading question. No Gate 0 score uses it.
2. Net debt. B07 G1 states "net debt Rs Mn 4,740.69 calc" with no date or basis (l.95). B01 FY26 net debt is 289.73 Cr (Mn 2,897.3). The basis is not labelled. No score effect: G1 is 0 on either figure, and D1 is scored on FY26.
3. Fixed-asset denominator. B01 M3 uses 779.34 Cr with no stated basis. B07 2C uses net PPE Mn 7,632.31. No score effect: both turnovers are below 1x.

## OPERATOR NOTES (rubric and template defects, not stage fails)

1. Gate 0 band gaps. The A1 bands leave values from 14.9 to 15 unassigned. B01 scored the lower band and disclosed the other reading. A written gap rule would settle it. On this run the gap moves core 53 to 55, with AVERAGE unchanged.
2. M10 ladder. A company that grew every year with receivables up more than 10 days scores 0. A company with 2 or more decline years scores 1. B01 applied the rule as written.
3. M11 windows. The rule says the two-window test "needs >=6 years", but 6 annual points cannot hold two separate 3-year CAGRs. The rule should name the windows.
4. EM matrix. It has no line for adverse or mixed evidence. B07 treated adverse evidence as NO EVIDENCE (C2, G1, G2) and also scored mixed evidence 0 (F2). A ruling would close finding F-1 for future runs.
5. B12c template, prompts/12-verifiers-pipeline.md line 379, reads: (same line, comment "# rule 9; any fail = REWORK stage 13"). That is not valid YAML and names no key. My block carries rule 9 as a comment only, so no key name is invented. A ruling on the intended key is needed before phase 3.
6. The template defaults for expectation_ledger (present: false and similar) would read as fails in a phase-1 block. I emitted nulls, which mean not checked.

## B12c BLOCK

```yaml
stage: B12c
company: "AZAD"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
# scope: phase 1 only. Gate 0 (B01) and Emerging Moat (B07) audited; valuation half pending phase 3.
gate0: {rules_checked: 57, fails: ["M7 'unregulated' asserted with no basis or anchor (MINOR; M7 = 0 unchanged)", "M11 under-6-year fallback invoked at 6 years (MINOR; recomputed two-window test gives M11 = 3, unchanged)"]}
emoat: {rules_checked: 37, fails: ["F2 scored 0 while recorded as documented Weak with positive filed evidence (MAJOR; recomputed F2 1.0, em_score 13.0, MODEST unchanged)", "A1 and B2 both credit the MHI LTCPA with no separate-mechanism line (MINOR; em_score range 11.0 to 12.0)", "Evidence taxonomy: Q2 concall item and Safran MOU tagged documented, two 1A rows untagged (MINOR; no score change)", "Section 5 collapses 17 of 23 rows into one line (MINOR)", "Section 2A lacks the % over current column (MINOR)", "I2 answered once for the company, not per claimed moat (MINOR; I2 = 0 unchanged)", "Optionality register: report names 10 items carried in the block, block carries 8; four-column table absent from report (MINOR)"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 not in phase-1 scope; Verifier C rules 4-7 and 9-15 not run
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; PENDING PHASE 3; null = not checked, never a fail
# rule 9 (Business Understanding Narrative; any fail = REWORK stage 13): not in phase-1 scope. Template line 379 is malformed and names no key, so none is emitted.
recomputed_destination_pe: ""  # not applicable in phase 1
recomputed_decision: ""        # not applicable in phase 1
findings:
  - {severity: "MAJOR", framework: "emoat", rule: "Verifier C rule 3 / 07 Section 5 matrix: score consistent with stated evidence tier", location: "07-emoat.md S3 row F2 (l.94); F2 evidence (l.126-129); S5 (l.157)", stated: "F2 recorded documented, Weak, Mixed; scored 0", recomputed: "F2 = 1.0 (LL or LM = 1 x documented 1.0); em_score 13.0, MODEST unchanged; the C1-Low edge case becomes 12.0 MODEST, not 11 NONE", note: "Matrix gives 0 only for no evidence; the stage's own Weak documented row R1 scores 2. The other reading (adverse-dominated evidence = no evidence of a forming moat) needs F2 labelled None in S3, as C2, G1 and G2 are."}
  - {severity: "MINOR", framework: "emoat", rule: "Single credit, one improvement one mechanism (CLAUDE.md; stage's own H2 ruling)", location: "07-emoat.md A1 (l.105-109); B2 (l.112-115); C1 (l.118)", stated: "MHI LTCPA (ANN 2026-03-26) credited in A1 and B2; no separation stated; A1 certificates are a B2 rubric item", recomputed: "A1 3.0 if distinct mechanisms are stated; 2.0 (M x M) if the MHI filing is held in B2 only; em_score 11.0 to 12.0", note: "B2/C1 overlap (Baker Hughes 2026-04-23 filing, dedicated plants) has no score effect: B2 is at HH = 4 on four filed agreements."}
  - {severity: "MINOR", framework: "emoat", rule: "07 op rule 2 evidence taxonomy", location: "07-emoat.md B2 (l.113); 1A Safran (l.26); 1A Arabelle and Landing gear (l.29-30)", stated: "Q2 concall statement tagged documented; MOU tagged documented; two rows untagged", recomputed: "no score change", note: "B2 stays documented on four filed agreements; Safran scores 0."}
  - {severity: "MINOR", framework: "emoat", rule: "07 Section 5 full scoring table, all 23 rows", location: "07-emoat.md S5 (l.157)", stated: "17 rows collapsed into one line", recomputed: "n/a", note: "The collapsed line hides F2, the one zero row with documented evidence."}
  - {severity: "MINOR", framework: "emoat", rule: "07 Section 2A table columns", location: "07-emoat.md 2A (l.51-58)", stated: "% over current column absent", recomputed: "n/a", note: "Write NOT FOUND where no base exists."}
  - {severity: "MINOR", framework: "emoat", rule: "07 Family I, I2: answer for each moat claimed", location: "07-emoat.md I2 (l.133)", stated: "One collective answer for the company", recomputed: "I2 = 0 unchanged", note: "Separate answers for A1, B2 and C1 are absent."}
  - {severity: "MINOR", framework: "emoat", rule: "07 Optionality register form; report-block parity", location: "07-emoat.md register (l.165-177); B07-emoat.yaml optionality_register", stated: "Report names 10 current items carried in the block; block carries 8; four-column table absent from report", recomputed: "Add Baker Hughes oil and gas revenue line and OEM advance (USD 4.5 Mn) to the register", note: "Oil and gas line survives in catalysts_12m; OEM advance only in the FLAG-CASH reason."}
  - {severity: "MINOR", framework: "gate0", rule: "01 op rule 5 grounded claims; M7", location: "01-gate0.md Block F M7 (l.78)", stated: "unregulated, no basis or anchor", recomputed: "M7 = 0 unchanged (NOT FOUND scores 0; regulated with more than 10 players gives at most 1, no moats-present change)", note: "B07 S4A records CEMILAC/DGAQA status NOT FOUND."}
  - {severity: "MINOR", framework: "gate0", rule: "01 M11: two-window test needs >=6 years", location: "01-gate0.md Block F M11 (l.82); B01 data_notes", stated: "6 years only, two-window test impossible, fallback used", recomputed: "M11 = 3 unchanged: latest 3-yr revenue CAGR FY23-FY26 33.8% is below prior FY21-FY24 40.6% (or FY21-FY23 43.2%), so tier 5 fails and tier 3 holds", note: "Rule threshold is >=6 years; 6 meets it."}
critical_count: 0
major_count: 1
minor_count: 8
acceptance_rate: 90.4             # rules passed / rules checked = 85 / 94, %
```
