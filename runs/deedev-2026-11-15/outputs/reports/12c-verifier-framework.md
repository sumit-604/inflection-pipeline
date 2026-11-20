# VERIFIER C: FRAMEWORK ADHERENCE. DEEDEV, run 2026-11-15 (phase-1 scope)

Model: claude-opus-5-5. Fresh context. Artifact paths only.

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (verifier rules 4, 6, 7, 9 to 15) did not run. Stages 10 and 11 have not run. I did not load the valuation framework documents.

Rule sources read: prompts/12-verifiers-pipeline.md (Verifier C section), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.

Units: All figures in Rs Cr unless the source says otherwise. The source unit is on the face of the document, not in the filename. B01 and B07 quote INR lacs and INR million where the filing prints them. I keep their units.

Anchor key: "B01 §n" = section n of 01-gate0.md. "B07 §n" = section n of 07-emoat.md. "P01 l.n" = prompts/01-gate-0-pipeline.md line n. "P07 l.n" = prompts/07-emerging-moat-pipeline.md line n. "B01 YAML" and "B07 YAML" = the fenced blocks.

I audit rule application. I do not audit company quality or raw numbers (Verifier A owns numbers). I re-derived each score from the inputs the stage states. Where a recompute needs a figure that is not in B01 or B07, I mark it NOT FOUND and refer it to Verifier A.

---

## SUMMARY

| Framework | Rules checked | Pass | Fail | CRITICAL | MAJOR | MINOR |
| --- | --- | --- | --- | --- | --- | --- |
| Gate 0 (B01) | 45 | 40 | 5 | 0 | 2 | 3 |
| Emerging Moat (B07) | 27 | 23 | 4 | 0 | 1 | 3 |
| Valuation (B11) | PENDING | | | | | |
| Total | 72 | 63 | 9 | 0 | 3 | 6 |

Acceptance rate: 63 / 72 = 87.5%.

What holds:
- Gate 0 classification AVOID holds under every reading I tested. Override 6 (ND/EBITDA 3.51x AND interest cover 2.58x, FY26; B01 §8) carries it. Override 6 uses no capital employed and no moat count, so the two MAJOR Gate 0 findings do not touch it.
- B07 combined assessment AVOID holds under both EM bands.

What changes:
- F-EM-1. The rubric-compliant EM total is 12.1 to 12.8, not 10.1. The band moves from NONE to MODEST. B07 already shows 12.8 as its own Reading B (B07 §5). The rubric picks that side, and no future disclosure decides it.
- F-G0-1. B01 replaced the fixed ROCE formula with a proxy. Block A runs 0 to 7 and Core runs 34 to 41, depending on the reading.
- F-G0-2. B01 scores M5 at 3 but also marks the data it needs as PEER DATA NEEDED. On B01's own statement, moats confirmed drop from 2 to 1 and the moat class drops from MODERATE to THIN.

Carry-forward to the phase-3 Verifier C run:
1. Check which EM band (NONE or MODEST) stage 11 feeds into Pillar 3. If the band change moves the destination PE by more than 1x, F-EM-1 becomes CRITICAL.
2. Check that stage 11 does not carry the B01 proxy ROCE (median 7.65%) as a Pillar 1 input. Under Master v3.7 as summarised in CLAUDE.md, the FTTCP ROCE verdict is the sole Pillar 1 authority.

---

## 1. GATE 0 (B01) COMPLIANCE

### 1a. Setup and formula rules

| # | Rule (source) | B01 applied | Re-derived / check | Result |
| --- | --- | --- | --- | --- |
| G01 | Opening line; data confidence tier (P01 l.23-25, l.142-144) | "Data available: 7 years (FY20 to FY26)"; moderate; no downgrade (B01 header) | 7 years sits in the 7-9 band: moderate, no downgrade. history_downgrade false (B01 YAML) | PASS |
| G02 | ROCE = EBIT / (TA - CL), "fixed, do not substitute alternatives"; compute only when the source gives none; state "computed" (P01 l.27-31) | Computed on a proxy: EBIT / (equity + reserves + borrowings) for all 7 years (B01 §2) | Proxy used for FY25 and FY26 too, where the strict inputs exist (B01 §2: results Q4 FY26 p.16). See F-G0-1 | FAIL MAJOR |
| G03 | ROE = PAT / average net worth; closing if opening is absent, stated (P01 l.32-33) | FY20 on closing, stated (B01 §2) | FY21 14.21 / 446.105 = 3.19%; FY26 77.17 / 845.475 = 9.13% (inputs B01 §1) | PASS |
| G04 | WC days formula; basis stated (P01 l.34-38) | Revenue basis, stated (B01 §3 B4) | FY21 146.27 + 135.81 - 57.11 = 224.97; FY26 122.52 + 184.10 - 31.44 = 275.18 (inputs B01 §3) | PASS |
| G05 | FCF = CFO - capex (PPE + intangibles), acquisitions out (P01 l.39-40) | Capex = PPE, CWIP and intangibles purchases, acquisitions excluded (B01 §3) | FY25 16,334.04 + 62.27 INR lacs = 163.96; FY26 18,367.88 + 585.94 INR lacs = 189.54 (B01 §3) | PASS |

### 1b. Block scores (re-derived from the B01 §1 series)

ROCE series as stated (B01 §2): 9.28, 5.43, 5.89, 6.95, 9.02, 7.65, 9.45. I re-checked each: EBIT = PBT + interest (FY26 96.25 + 60.74 = 156.99), CE = net worth + borrowings (FY26 890.38 + 771.19 = 1,661.57), 156.99 / 1,661.57 = 9.45%. All seven tie.

ROE series as stated (B01 §2): 3.05, 3.19, 1.89, 3.10, 5.99, 6.97, 9.13. All seven tie on PAT / average net worth.

| # | Line (P01 line) | B01 value and score | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G06 | A1 median ROCE (l.55) | 7.65% = 0 | Sorted 5.43, 5.89, 6.95, 7.65, 9.02, 9.28, 9.45. Median 7.65 (<10) = 0 | PASS on stated inputs (F-G0-1) |
| G07 | A2 minimum ROCE (l.56) | 5.43% FY21 = 0 | 38.61 / 711.48 = 5.43 (<8) = 0 | PASS on stated inputs (F-G0-1) |
| G08 | A3 median ROE (l.57) | 3.19% = 0 | Sorted 1.89, 3.05, 3.10, 3.19, 5.99, 6.97, 9.13. Median 3.19 (<12) = 0 | PASS |
| G09 | A4 ROCE trend (l.58-59) | 9.45 vs 9.28 = 5 | Latest >= earliest = 5 | PASS on stated inputs (F-G0-1) |
| | Block A | 5 | 0 + 0 + 0 + 5 = 5 | |
| G10 | B1 cumulative CFO / PAT (l.62-63) | 251.94 / 195.76 = 1.29, 5 | 7-year sums tie (B01 §1); 1.287 (>=1.00) = 5 | PASS |
| G11 | B2 FCF-positive share (l.64) | 2 of 5 = 40%, 0 | FY21 +78.68, FY22 +40.83, FY23 -44.71, FY25 -282.42, FY26 -169.99 (B01 §3). 40% (<50) = 0. FY20 and FY24 capex NOT FOUND, not credited (P01 l.20-22) | PASS |
| G12 | B3 cumulative FCF / PAT (l.65-66) | negative, 0 | -377.61 / 156.18 (same 5 years) = negative = 0 | PASS |
| G13 | B4 WC days change (l.67-68) | +50.2, 0 | 224.97 to 275.18 = +50.2 (>15) = 0. FY21 is the earliest year because FY20 payables are NOT FOUND (B01 §3) | PASS |
| | Block B | 5 | 5 + 0 + 0 + 0 = 5 | |
| G14 | C1 revenue CAGR (l.71) | 7.9%, 1 | (1,142.00 / 722.51)^(1/6) - 1 = 7.93% (5-9.9) = 1 | PASS |
| G15 | C2 PAT CAGR (l.72) | 33.9%, 5 | (77.17 / 13.37)^(1/6) - 1 = 33.9% (>=20) = 5 | PASS |
| G16 | C3 positive YoY revenue years (l.73) | 4 of 6, 1 | FY21 and FY22 fell; 66.7% (50-74) = 1 | PASS |
| G17 | C4 PAT CAGR minus revenue CAGR (l.74) | +26.0pp, 5 | 33.9 - 7.9 = +26.0 (>=+3) = 5 | PASS |
| G18 | CAGR edge rules (l.43-50) | none triggered | Both endpoints positive. PAT positive in all 7 years (B01 §1), so no swing note is due. C4 computable | PASS |
| | Block C | 12 | 1 + 5 + 1 + 5 = 12 | |
| G19 | D1 net debt / EBITDA (l.77-79) | 3.51x, 0 | (771.19 - 84.37) / 195.84 = 3.51 (>3) = 0 | PASS (O-G0-1) |
| G20 | D2 interest cover (l.80-82) | 2.58x, 1 | 156.99 / 60.74 = 2.58 (1.5-2.9) = 1 | PASS |
| G21 | D3 debt / equity (l.83-84) | 0.87, 3 | 771.19 / 890.38 = 0.87 (0.5-1.0) = 3 | PASS |
| G22 | D4 current ratio (l.85-86) | 1.33, 2 | 1,16,038.61 / 86,924.44 INR lacs = 1.33 (1.2-1.49) = 2 | PASS |
| | Block D | 6 | 0 + 1 + 3 + 2 = 6 | |
| G23 | E1 promoter holding (l.89-90) | 65.13%, 5 | >=60 = 5 | PASS |
| G24 | E2 promoter change, 3 years (l.91-92) | -34.87pp pre-Offer, -5.04pp post-Offer, 0 | Both baselines fall more than 3pp = 0. B01 does not read intent, as P01 l.13 requires | PASS |
| G25 | E3 pledge (l.93) | 0%, 5 | = 5 | PASS |
| G26 | E4 contingent liabilities / net worth (l.94-95) | 22,970.21 / 89,043.69 INR lacs = 25.8%, 1 | Score ties. The numerator leaves out items that B01 itself says Note 30B lists. See F-G0-3 | FAIL MINOR |
| | Block E | 11 | 5 + 0 + 5 + 1 = 11 | |
| | Core | 39 | 5 + 5 + 12 + 6 + 11 = 39 | |

### 1c. Moat tests (Block F)

Peer inputs as stated (B01 §7): EBITDA margin DEEDEV 17.15, ANUP 21.48, ISGEC 8.59, RATNAMANI 16.86. GM proxy DEEDEV 58.05, ANUP 52.17, ISGEC 45.36, RATNAMANI 40.36. Mcap (INR Cr) DEEDEV 3,973.32, ANUP 3,455.43, ISGEC 7,248.17, RATNAMANI 17,431.88.

| # | Test (P01 line) | B01 score | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G27 | M1 pricing power (l.102-104) | 0 | Margin 12.05 to 17.15 (+5.1pp) but revenue CAGR 7.93 <10, so the 5 and 3 bands fail. Margin did not decline, so the 1 band fails = 0 | PASS |
| G28 | M2 cost advantage (l.105-106) | 1 | Peer median of (21.48, 8.59, 16.86) = 16.86; +0.29pp (within +/-2) = 1 | PASS |
| G29 | M3 capital efficiency (l.107-108) | 0 | FAT 1.75x; proxy ROCE 9.45 fails >12 = 0. On strict FY26 ROCE 14.9%, FAT >1x AND ROCE >12% = 1 | PASS on stated inputs (F-G0-1) |
| G30 | M4 customer stickiness (l.109-111) | 1 | 2 decline years, CAGR positive = 1 | PASS |
| G31 | M5 scale and dominance (l.112-113) | 3 | Rank 3 of 4 mcap, 2 of 4 margin = 3 on the supplied set. B01 also marks the full segment list PEER DATA NEEDED. See F-G0-2 | FAIL MAJOR |
| G32 | M6 technology / R&D (l.114-116) | 0 | R&D NOT FOUND = 0 (P01 l.20-22) | PASS |
| G33 | M7 regulatory / licence (l.117-119) | 0 | Core business unregulated = 0 (O-G0-2) | PASS |
| G34 | M8 distribution (l.120-122) | 0 | No outlet network = 0 | PASS |
| G35 | M9 brand (l.123-125) | 1 | Peer median of (52.17, 45.36, 40.36) = 45.36; +12.69pp. CAGR 7.93 fails both the >=10% and the >=8% bands = 1. Proxy stated | PASS |
| G36 | M10 switching costs (l.126-128) | 1 | Overall growth, 2 decline years = 1 | PASS |
| G37 | M11 network effects (l.129-133) | 5 | 7 years, so the two-window test runs. (1,142.00 / 595.50)^(1/3) - 1 = 24.2% > (595.50 / 722.51)^(1/3) - 1 = -6.2%; selling and admin share 9.29 to 6.91, falling = 5 | PASS (O-G0-3) |
| G38 | M12 negative WC (l.134-135) | 0 | 225 to 275 days (>45) = 0 | PASS |
| | Block F | 12 | 0+1+0+1+3+0+0+0+1+1+5+0 = 12 | |
| G39 | Moat count and class (l.137-138) | 2 present (M5, M11), MODERATE | 2 = MODERATE on the stated scores. 1 = THIN under F-G0-2 | PASS on stated scores (F-G0-2) |

### 1d. Classification, deal-breakers, output

| # | Rule (P01 line) | B01 applied | Check | Result |
| --- | --- | --- | --- | --- |
| G40 | Classification matrix (l.146-149) | Core 39 = AVOID | 39 <40 = AVOID, whatever the moat class | PASS |
| G41 | Deal-breakers 1-9 applied; driving years named (l.151-159) | 6, 3, 1, 2 fired; 4, 5, 7, 8, 9 not | 6: 3.51 >3 AND 2.58 <3 = AVOID. 3: 7.65 <10 = max AVERAGE (proxy). 1: A 5 <8. 2: B 5 <8. 4: 1.29 >=0.50, off. 5: 0%, off. 7: 2 of 6, off. 8: PAT FY24-FY26 positive, off. 9: 7 years, off. Years named: FY26 for 6; FY20-FY26 for 3 (B01 §8) | PASS |
| G42 | FLAG-GATE0 when <= AVERAGE with depressors; block_b_trend with its number (l.175-177, l.191-192) | Both present (B01 YAML) | AVOID with named depressors, so the flag is due. The trend line carries numbers | PASS |
| G43 | Source anchor on every extracted number (l.15-18) | One figure unanchored | M3 denominator 653.78 (B01 §7). See F-G0-4 | FAIL MINOR |
| G44 | Dashboard: all blocks, moat profile bars, classification box, strongest/weakest, decision line (l.163-165) | Block bars, box, strongest/weakest and decision line present; no moat profile bars | See F-G0-5 | FAIL MINOR |
| G45 | YAML block schema (l.168-198) | All keys present, values valid; analyst_note about 75 words (<=200) | | PASS |

### 1e. Gate 0 sensitivity grid (how far the findings move the outcome)

| Reading | Block A | Core | Block F | Moats / class | Matrix class | Deal-breakers firing | Final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| As filed (B01) | 5 | 39 | 12 | 2 / MODERATE | AVOID | 6, 3, 1, 2 | AVOID |
| F-G0-1 reading 1 (strict FY25-FY26 only) | 7 | 41 | 13 | 2 / MODERATE | AVERAGE | 6, 1, 2 | AVOID (override 6) |
| F-G0-1 reading 2 (3-year minimum binds) | 0 | 34 | 12 | 2 / MODERATE | AVOID | 6, 1, 2 (3 not evaluable) | AVOID |
| F-G0-2 reading b only | 5 | 39 | 9 | 1 / THIN | AVOID | 6, 3, 1, 2 | AVOID |
| F-G0-1 reading 1 + F-G0-2 reading b | 7 | 41 | 10 | 1 / THIN | AVERAGE | 6, 1, 2 | AVOID (override 6) |

AVOID moves only if two things happen together: override 6 stops firing AND Core reaches 40 or more. Neither is established in my inputs (O-G0-1).

### 1f. Gate 0 findings

**F-G0-1 (MAJOR). ROCE formula replaced by a proxy.**
- Rule: P01 l.27-31: "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" and "ROCE = EBIT ÷ (Total Assets − Current Liabilities)". P01 l.20-22: missing data is NOT FOUND and scores 0. P01 l.23: minimum 3 years.
- What B01 did: capital employed = equity + reserves + borrowings ("TA less Other Liabilities proxy") for all 7 years (B01 §2). This includes FY25 and FY26, where the strict inputs exist. B01 discloses the proxy and prints the strict values: FY26 14.9%, FY25 11.1% (B01 §2, results Q4 FY26 p.16). The disclosure is full. The substitution is still the thing the rule forbids.
- Reading 1 (strict formula where its inputs exist). Two years: median 13.0% gives A1 1; minimum 11.1% gives A2 1; 14.9 vs 11.1 gives A4 5; A3 stays 0. Block A 7, Core 41. Deal-breaker 3 stops firing. Deal-breaker 1 still fires (7 <8). M3 becomes 1, Block F 13.
- Reading 2 (the 3-year minimum binds). Two strict years are under the minimum. A1, A2 and A4 are NOT FOUND and score 0. Block A 0, Core 34.
- Separating observation: does the Prospectus restated balance sheet print total current liabilities for FY21 to FY23? B01 already takes FY21 trade payables from that balance sheet (INR million 774.88, B01 §3 B4) and FY21-FY23 capex from the restated cash flow (B01 §3). If it prints CL, the strict formula runs on 5 years (FY21-FY23, FY25, FY26) and clears the minimum. That would also make B01's statement "current liabilities FY20-FY24: NOT FOUND" (B01 YAML input_gaps) wrong for three of those years. I did not open the prospectus, because it is outside my inputs. Strict FY21-FY23 ROCE: NOT FOUND here. Referred to Verifier A.
- Decision impact: none on the classification (grid 1e). Values that change: Block A, Core, the deal-breaker 3 entry, M3.
- Fix: stage 1 scores the strict series where its inputs exist. The other route is an operator ruling that the equity-plus-debt proxy is an accepted substitute when screener has no ROCE row. The rule text and the run must agree.

**F-G0-2 (MAJOR). M5 scored 3 while marked PEER DATA NEEDED.**
- Rule: P01 l.98-100: "If a test needs peer data that is not provided, score 0 and mark 'PEER DATA NEEDED' (never guess peer figures)." M5 needs the mcap rank "in segment" (P01 l.112-113).
- What B01 did: "Provisional: the supplied set is not the full segment", scored 3 (B01 §7). The data_notes say: "full segment peer list PEER DATA NEEDED" (B01 YAML). The mark and the score contradict each other.
- Reading a: the three supplied peers (ANUP, ISGEC, RATNAMANI) are the scoring segment. M5 3 stands, and the PEER DATA NEEDED mark must go.
- Reading b: B01's own statement governs. M5 0, Block F 9, moats confirmed 1 (M11 only), moat class THIN, grand total 48.
- Separating observation: DEE's mcap rank in the segment peer list this run uses (the stage 6 B06 peer set, not in my inputs).
- Decision impact: none on the classification (Core 39 <40; override 6). Downstream, B07 §6C copies "12 / 60; 2 moats confirmed; class MODERATE" from B01. Under reading b it reads 9 / 60, 1 moat, THIN. B01 also flags M11 as an arithmetic artefact (B01 §7). With M5 at 0, the only moat B01 counts as present is the one it calls an artefact.
- Fix: stage 1 picks one reading and makes the score and the mark agree.

**F-G0-3 (MINOR). E4 numerator labelled "full listed total" but incomplete.**
- B01 §6 sums four items to 22,970.21 INR lacs and calls this "the full listed total". The next lines say "Also listed and not summed: ... a customs demand of 815.09 plus penalty 305.00 INR lacs (Note 30B(e) ...), and others."
- Recompute with Note 30B(e): (22,970.21 + 815.09 + 305.00) / 89,043.69 = 24,090.30 / 89,043.69 = 27.05%. Band 15-30, E4 stays 1. Corporate guarantees for subsidiary loans (668.89, Note 30C) are fairly left out of a consolidated numerator. Even with them, 24,759.19 / 89,043.69 = 27.81%, still 1.
- "Others": amount NOT FOUND in B01. E4 drops to 0 only if the full numerator passes 30% of 89,043.69 = 26,713.11 INR lacs. That needs "others" above 2,622.81 INR lacs (derived). Referred to Verifier A.

**F-G0-4 (MINOR). Unanchored figure.** The M3 FAT denominator 653.78 has no source (B01 §7). P01 l.15-18 requires an anchor on every extracted number. B07 §2C computes FAT on a different base (average net PPE plus CWIP, Rs 625.46 cr, AR p.288). The two denominators are not reconciled. I did not re-derive the value (Verifier A).

**F-G0-5 (MINOR). No moat profile bars.** P01 l.163-165 asks for moat profile bars. B01 §8 shows one "MOAT (F) 12 / 60" line. The per-test scores exist only in the §7 table.

### 1g. Gate 0 observations (no fail)

- **O-G0-1. D-block "latest" basis.** B01 scores D1 to D4 on the FY26 annual balance sheet. It states that the 30 Sep 2026 balance sheet was not re-scored (B01 §5). P01 says "latest quarter" for E1 (l.89) and only "latest" for D1 to D4 (l.77-86). That contrast supports the annual reading, so I record PASS. Override 6 is the deal-breaker that carries AVOID. On a later balance sheet (after the Rs 300 cr preferential issue and the Rs 225 cr debt repayment, B07 §3 G1, Q2 FY27 p.8 note 4), it could stop firing. 30 Sep 2026 net debt and trailing EBITDA and interest: NOT FOUND in my inputs. Even if it stops firing, AVOID moves only if Core also reaches 40 (grid 1e).
- **O-G0-2. M7 segment reading.** Biomass power is tariff-regulated: INR lacs 5,546.64 of 1,14,199.92 revenue (B01 §7, AR Note 31). A segment-level literal reading could give "regulated but >10 players = 1". B01 reads the company as unregulated and scores 0. The moat count does not change (1 <3).
- **O-G0-3. M11 artefact.** B01 scores 5 on the literal two-window test and flags it as an artefact with no network economics (B01 §7, B01 YAML data_notes). P01 l.13 forbids qualitative overrides at this stage, so the score is correct. The flag should travel to the dossier and to stage 11.
- **O-G0-4. B2 NOT FOUND years.** B01 scores only the years it can evaluate (2 of 5 = 40%, score 0). Counting both NOT FOUND years as positive would give 4 of 7 = 57%, score 2 (B01 §3). P01 l.20-22 scores missing data 0, so B01's reading is the one the rule supports.

---

## 2. EMERGING MOAT (B07) COMPLIANCE

### 2a. Structure and coverage

| # | Rule (source) | B07 applied | Check | Result |
| --- | --- | --- | --- | --- |
| E01 | All six sections in one response (P07 l.28) | §1 to §6 and the optionality register present | | PASS |
| E02 | Evidence taxonomy on every item (P07 l.29-34) | DOC / CLAIM / INFER, mapped to the three symbols (B07 header) | | PASS |
| E03 | Source anchor on every evidence item (P07 l.35-36) | Present on table rows (B07 §3) | | PASS |
| E04 | All 23 categories addressed or NO EVIDENCE FOUND (P07 l.39-40, l.65-67; verifier rule 3) | 22 in §3 plus R1 in §4 | A1 to I2 = 22; R1 = 23 | PASS |
| E05 | §3 summary table: every row with evidence, type, strength, time (P07 l.155-157) | 23 rows (B07 §3 summary) | | PASS |
| E06 | Strong/Moderate count stated (P07 l.157) | "2 (B1, B2). Strong: 0." | | PASS |
| E07 | Completionist recount line present and performed (P07 l.41-46, l.157-159; verifier rule 3) | "Recount performed: 21 documented items across 10 categories" (B07 §3) | | PASS |
| E08 | Recount internally consistent | Report residual 10; block residual 9 | See F-EM-2 | FAIL MINOR |
| E09 | Completionist stop line at 12 active categories (P07 l.41-44) | 8 active (B1, B2, E1, E2, F2, G1, H2, R1) | 8; 10 or 11 under F-EM-1; under 12 either way | PASS |

### 2b. Scoring re-derivation (B07 §5)

Matrix (P07 l.171-173): HH 4; HM / MH 3; HL / MM / LH 2; ML / LM 1; LL 1; no evidence 0. Quality: DOC 1.0, CLAIM 0.7, INFER 0.5.

| Row | Cat | B07 L x I | Raw | Quality | B07 adjusted | Check |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | B1 | M x M | 2 | DOC 1.0 | 2.0 | Cell correct; DOC items carry the score (plant, first order, Reg 30 19 Mar 2026) |
| 6 | B2 | H x M | 3 | DOC 1.0 | 3.0 | Cell correct; signed reservation carries it (Reg 30 21 May 2026) |
| 12 | E1 | M x L | 1 | CLAIM 0.7 | 0.7 | Cell correct; the advantage itself is a claim |
| 13 | E2 | M x L | 1 | DOC 1.0 | 1.0 | Cell correct (AR p.314 split) |
| 15 | F2 | M x L | 1 | DOC 1.0 | 1.0 | Cell correct |
| 16 | G1 | M x L | 1 | DOC 1.0 | 1.0 | Cell correct (CARE p.1, Q2 FY27 p.8) |
| 19 | H2 | L x M | 1 | CLAIM 0.7 | 0.7 | Cell correct (O-EM-1) |
| 23 | R1 | M x L | 1 | CLAIM 0.7 | 0.7 | Cell correct; basis conflict, see F-EM-4 |
| 3, 8, 20 | A3, C1, H3 | unscored | 0 | | 0.0 | Evidenced rows given 0; see F-EM-1 |
| | Total | | | | 10.1 | 2.0 + 3.0 + 0.7 + 1.0 + 1.0 + 1.0 + 0.7 + 0.7 = 10.1, ties |

| # | Rule (source) | B07 applied | Check | Result |
| --- | --- | --- | --- | --- |
| E10 | Matrix cell mapping on scored rows (P07 l.171-173) | 8 rows | All 8 cells map correctly | PASS |
| E11 | Evidenced categories take a matrix cell; 0 only for no evidence (P07 l.171-173, l.39-40) | A3, H3, C1 scored 0 as "not moat-grade" | See F-EM-1 | FAIL MAJOR |
| E12 | Quality multipliers 1.0 / 0.7 / 0.5 (P07 l.173) | DOC on B1, B2, E2, F2, G1; CLAIM on E1, H2, R1 | Correct (O-EM-1) | PASS |
| E13 | No CLAIM-only row scored as DOC (verifier rule 3) | None | Each DOC-multiplied row holds at least one DOC item that carries its score | PASS |
| E14 | Adjusted total arithmetic | 10.1 | Ties | PASS |
| E15 | Band from total (P07 l.175-176) | 10.1 = NONE | Correct on 10.1; MODEST on 12.1 to 12.8 | PASS on stated rows (F-EM-1) |
| E16 | I1 / I2 contribution stated separately (P07 l.180-181) | "Family I (I1 + I2) contribution 0.0" (B07 §5) | | PASS |

### 2c. Family I, allocation, capex, register, combined, block

| # | Rule (source) | B07 applied | Check | Result |
| --- | --- | --- | --- | --- |
| E17 | Categories 21 and 22 present (verifier rule 8) | I1 and I2 in §3; rows 21 and 22 in §5 | | PASS |
| E18 | I1 above 0 only with both legs evidenced, (b) leg with at least 1 DOC (verifier rule 8; P07 l.122-138) | 0: "NO EVIDENCE FOUND on either leg" | | PASS |
| E19 | I2 above 0 only with a specific named sacrifice (verifier rule 8; P07 l.139-153) | 0: "nothing must be destroyed" | | PASS |
| E20 | I2 answered for each moat claimed (P07 l.139-141) | Answered for seamless, Thailand reservation, Anjar | See F-EM-3 | FAIL MINOR |
| E21 | One improvement, one mechanism (CLAUDE.md; B07 §3 allocation rule) | Seamless in B1 only, reservation in B2 only, approvals declared B2 only | Seamless and reservation clean. Approval stack reused as R1's basis. See F-EM-4 | FAIL MINOR |
| E22 | 2C arithmetic shown (P07 l.60-62) | Rs 87.48 cr x 1.83 = Rs 159.7 cr, 14.0% (B07 §2C) | 1,142.0 / 625.46 = 1.826; 87.48 x 1.826 = 159.7; / 1,142.0 = 14.0%. Case B 179.46 x 1.826 = 327.6, 28.7%. Overlap with CWIP flagged NOT FOUND | PASS |
| E23 | Optionality register: table and block; register items never scored (P07 l.183-196) | 11 table rows, 10 block rows (two seamless rows merged); "No row relies on an item that is also in the optionality register" (B07 §5) | B1 and B2 scores rest on the plant and the signed reservation, not on the registered GE, Siemens, Mitsubishi or seamless-demand items | PASS |
| E24 | §6C uses the injected Gate 0 block (P07 l.202-203) | Core 39; 12 / 60; 2 moats; MODERATE; AVOID | Matches B01 YAML | PASS |
| E25 | §6D combined classification from the named set (P07 l.203-208) | AVOID | Holds under NONE and MODEST (O-EM-2) | PASS |
| E26 | YAML schema keys and tokens (P07 l.214-243) | All keys present; em_classification "NONE" is a valid token | Extra key capex_for_stage9 (O-EM-3) | PASS |
| E27 | analyst_note <=200 words (P07 l.239) | About 140 words | | PASS |

### 2d. Emerging Moat findings

**F-EM-1 (MAJOR). Evidenced categories zeroed outside the matrix. The band is MODEST, not NONE.**
- Rule: P07 l.171-173 sets the raw score "from the likelihood × impact matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0)". Only "no evidence" scores 0. The lowest cell for an evidenced category is LL = 1. The rubric has no cell for "evidence present, not moat-grade".
- What B07 did: A3, H3 and C1 carry evidence but are "Weak, unscored" (B07 §3 summary; §5 rows 3, 8, 20).
  - A3: VFDs, CNC plasma software with a stated cost saving ("3 lakh on 100-ton"), vision cameras on cobot and robot (DOC, AR p.57-58). These fit the category's own list: "automation", "unit cost declining" (P07 l.73-74).
  - H3: 3 MW rooftop solar and 191,067 t CO2e avoided under CDM (DOC, AR p.21). These fit "renewables %" (P07 l.119-120).
  - C1: repeat-customer statement (CLAIM, AR p.5, deck slide 5) and CARE's repeat-client list (CARE p.2). These fit "embedded relationships" loosely (P07 l.86-89).
- Consistency: B07 scores other Weak rows at the floor. G1 is described as "balance-sheet repair ... Weak" and scores 1.0. E1 (Weak) scores 0.7. E2 (Weak) scores 1.0 (B07 §3, §5). B07 gives three rows of the same strength a score and zeroes three others.
- Recompute: A3 LL 1 x DOC 1.0 = 1.0. H3 LL 1 x DOC 1.0 = 1.0. Total 12.1, MODEST. With C1 LL 1 x CLAIM 0.7 = 0.7, the total is 12.8, MODEST (P07 l.175-176: 12-24 = MODEST). The band moves on the two documented rows alone. C1 is the contested row, and it does not decide the band.
- Rows this rule does not lift: C2 and G2 (the documented evidence runs against the category; for G2, H1 FY27 CFO is negative, Q2 FY27 p.7). F1 (the ESOP item has no technical-staff split and headcount fell, Q1 call p.6). A1 (credited in B1 under the one-mechanism rule). These stay 0.
- B07's two readings: B07 prints Reading A 10.1 (NONE) and Reading B 12.8 (MODEST) (B07 §5, B07 YAML flags). It names Anjar utilisation above 60% plus positive H2 FY27 CFO as the separating observation. That observation moves F2 and G2. It does not separate A from B, which differ only on how the rubric treats A3, C1 and H3. No future disclosure settles a rubric question. The matrix settles it, and it gives Reading B.
- Guard check: active categories become 10 (A3, H3 added) or 11 (C1 added), under the stop line of 12. active_categories (Strong/Moderate only) stays B1, B2.
- Decision impact: B07 combined AVOID holds. MODEST is not a strong forward score, so it creates no HIGH POTENTIAL or TURNAROUND row (B07 §6D). The "EM >= 25" UA qualifier is not reached under either reading. em_score and em_classification feed stage 11 Pillar 3. I cannot test the Pillar 3 effect in phase 1. Escalation: at phase 3, if stage 11 uses NONE and MODEST would move the destination PE by more than 1x, this finding becomes CRITICAL.
- Fix: stage 7 restates em_score 12.1 (12.8 if C1 is scored) and em_classification MODEST. The other route is an operator ruling that adds a "not moat-grade = 0" cell to the rubric. If the ruling comes, G1's "balance-sheet repair" score needs the same test.

**F-EM-2 (MINOR). Recount line internally inconsistent.**
- B07 §3 says "The 10 remaining documented items are adverse (C2), not moat-grade (A3), or negative-direction F2 rows." B07 YAML completionist_recount says "the other 9". 21 - 12 = 9, so the block is right.
- The residual is C2 2, A3 1, F2 2, G1 2, E1 1, F1 1 = 9. The report sentence names C2, A3 and F2 only.
- H3's two AR p.21 items are tagged DOC in the §3 summary, but they sit outside the recount. F1's inline ESOP item sits inside it. The count rule ("tabulated rows", B07 §3) is applied unevenly. G2's Ganeko item (Reg 30 23 Jun 2026) carries no tag.
- Impact: none. The guard outcome does not change.

**F-EM-3 (MINOR). I2 not answered for every claimed moat.**
- P07 l.139-141: "For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy".
- B07 §3 I2 answers for the seamless plant (B1), the Thailand reservation (B2) and Anjar (E1). It does not answer for E2 exports, F2 execution, G1 war chest, H2 partnerships, R1 approvals or the B2 certification stack.
- Impact: none. I2 = 0 stands. A score above 0 needs a named, specific sacrifice with at least one DOC source (P07 l.150-153), and no such item appears anywhere in B07.

**F-EM-4 (MINOR). Approval stack assigned to B2, then used as R1's basis.**
- B07 §3 opens with "The certification and approval stack is credited in B2 (not R1)."
- B07 §4A then lists the NTPC approval (AR p.7), the further seamless approvals (Q4 call p.12) and the Siemens clearance (Q1 call p.5). All three already sit in the B2 table. B07 §4C rests R1 on them: "Vendor approvals are the only entry barrier". R1 scores ML 1 x CLAIM 0.7 = 0.7 (B07 §5 row 23).
- Recompute under the matrix floor: R1 keeps 0.7 on its own evidence. That is the §4B policy items (CLAIM: Q3 call p.2, deck slide 30, Q1 call p.4) and the nuclear export pre-qualification (CLAIM, Q1 call p.11), at LL 1 x 0.7. No numeric change.
- Under B07's own logic (evidence that is not moat-grade stays unscored), the shared tailwinds would be unscored ("Policy tailwinds are shared", B07 §4C). R1 would then rest only on the B2 items, so it would score 0 and the total would be 9.4. B07 contradicts itself under its own reading. The matrix reading removes the conflict.
- Fix: restate R1's basis as the §4B items and the nuclear export pre-qualification. Drop the B2 approvals from §4A, or mark them "credited in B2".

### 2e. Emerging Moat observations (no fail)

- **O-EM-1. Mixed-evidence multiplier.** P07 does not say which multiplier applies when one category holds both DOC and CLAIM items. B07 uses the tier of the item that carries the score. That gives DOC for B1 and B2 (plant, contract) and CLAIM for E1 (the advantage is a claim) and H2 (the framework has "no committed order value", Reg 30 16 Oct 2026, and the GE LOI carries the impact). B07 applies this the same way on every row. DOC on H2 would add 0.3 (10.4, or 13.1 under F-EM-1) and would not change the band.
- **O-EM-2. 6D matrix text missing from the prompt.** P07 l.202-204 refers to "the standard matrix" and lists its rows, but it does not print the cells. B07 says so (B07 §6D). AVOID holds under NONE and MODEST. This is a gap in the prompt, reported for an operator fix. It is not a stage 7 fail.
- **O-EM-3. Extra block key.** P07 l.214 asks for "exactly this fenced YAML block". B07 YAML adds capex_for_stage9. Every schema key is present with a valid token, and the extra key is additive and anchored. I do not count it as a fail. The orchestrator's parser decides whether it is accepted.
- **O-EM-4. Load-bearing facts checked first.** B07 §0 checks the Spear facts before its own work, as the CLAUDE.md Spear gate requires.

---

## 3. VALUATION (B11): PENDING

Not run. Phase-1 scope. Stages 10 and 11 have not run. Verifier rules 4, 6, 7 and 9 to 15 wait for the phase-3 run. The expectation_ledger and business_narrative entries in the block are null with status PENDING. They do not mean pass or fail.

---

## 4. BLOCK

```yaml
stage: B12c
company: "DEEDEV"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
gate0: {rules_checked: 45, fails: ["G02 ROCE formula substituted: equity+reserves+borrowings proxy used for all 7 years, incl. FY25-FY26 where strict TA-CL inputs exist (MAJOR, F-G0-1)", "G26 E4 numerator labelled full listed total but omits listed Note 30B(e) items; score unchanged (MINOR, F-G0-3)", "G31 M5 scored 3 while B01 marks the full segment list PEER DATA NEEDED (MAJOR, F-G0-2)", "G43 M3 FAT denominator 653.78 carries no source anchor (MINOR, F-G0-4)", "G44 dashboard has no moat profile bars (MINOR, F-G0-5)"]}
emoat: {rules_checked: 27, fails: ["E08 completionist recount internally inconsistent: report says 10 residual documented items, block says 9; H3 DOC items outside the count (MINOR, F-EM-2)", "E11 evidenced categories A3 (DOC), H3 (DOC), C1 (CLAIM) zeroed outside the matrix; matrix floor LL=1 gives 12.1-12.8 MODEST, not 10.1 NONE (MAJOR, F-EM-1)", "E20 I2 answered for 3 claimed moats only (B1, B2 reservation, E1); E2, F2, G1, H2, R1 and the B2 certification stack unanswered; I2 0 stands (MINOR, F-EM-3)", "E21 approval stack declared B2-only, yet R1 4C rests on vendor approvals repeated from the B2 table; R1 0.7 sustainable on 4B items, no numeric change (MINOR, F-EM-4)"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING: phase-3 scope; stages 10 and 11 not run; valuation framework docs not loaded"}
expectation_ledger: {status: "PENDING: phase-3 scope", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "PENDING: stage 13 not run", present: null, fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # out of phase-1 scope
recomputed_decision: ""        # concur: Gate 0 AVOID and B07 combined AVOID stand under every reading tested
findings:
  - {id: "F-G0-1", stage: "01 Gate 0", rule: "P01 FORMULA DEFINITIONS: ROCE = EBIT / (TA - CL), fixed, do not substitute alternatives", severity: "MAJOR", stated: "Proxy CE = equity + reserves + borrowings for FY20-FY26; median ROCE 7.65%, A1 0, A2 0, A4 5, Block A 5, Core 39, deal-breaker 3 fired, M3 0", recomputed: "Reading 1 (strict where inputs exist, FY25 11.1% and FY26 14.9%): A1 1, A2 1, A4 5, Block A 7, Core 41, deal-breaker 3 off, M3 1, Block F 13. Reading 2 (3-year minimum binds): A1/A2/A4 NOT FOUND scored 0, Block A 0, Core 34. Strict FY21-FY23 ROCE NOT FOUND here; B01 already cites the Prospectus restated balance sheet for FY21 payables, so CL for FY21-FY23 may be in the corpus (referred to Verifier A)", decision_impact: "none: AVOID holds via override 6 (ND/EBITDA 3.51x AND IC 2.58x), which uses no capital employed"}
  - {id: "F-G0-2", stage: "01 Gate 0", rule: "P01 Block F: if a test needs peer data that is not provided, score 0 and mark PEER DATA NEEDED", severity: "MAJOR", stated: "M5 3 on 3 auto-selected peers (mcap rank 3 of 4, margin rank 2 of 4), while data_notes mark the full segment peer list PEER DATA NEEDED", recomputed: "Reading b (B01's own statement governs): M5 0, Block F 9, moats_confirmed 1 (M11), moat_class THIN, grand_total 48. Reading a (3 peers ruled the segment): M5 3 stands and the PEER DATA NEEDED mark must go. Separating observation: DEE's mcap rank in the run's segment peer list (B06, not in my inputs)", decision_impact: "none: Core 39 < 40 and override 6 hold AVOID; B07 Section 6C moat line would read 9/60, 1 moat, THIN"}
  - {id: "F-G0-3", stage: "01 Gate 0", rule: "P01 E4 contingent liabilities / net worth", severity: "MINOR", stated: "22,970.21 / 89,043.69 INR lacs = 25.8%, labelled the full listed total, with Note 30B(e) and others listed and not summed", recomputed: "With Note 30B(e) 815.09 + 305.00: 24,090.30 / 89,043.69 = 27.05%, E4 1 unchanged. 'Others' amount NOT FOUND in B01; E4 falls to 0 only if they exceed 2,622.81 INR lacs (referred to Verifier A)", decision_impact: "none"}
  - {id: "F-G0-4", stage: "01 Gate 0", rule: "P01 rule 4: source anchor on every extracted number", severity: "MINOR", stated: "M3 FAT 1,142.00 / 653.78 = 1.75x; 653.78 unanchored", recomputed: "anchor required; value not re-derived (numbers belong to Verifier A)", decision_impact: "none"}
  - {id: "F-G0-5", stage: "01 Gate 0", rule: "P01 OUTPUT: dashboard with moat profile bars", severity: "MINOR", stated: "dashboard shows one MOAT (F) 12/60 line", recomputed: "per-test bars M1-M12 missing; scores exist in the Section 7 table", decision_impact: "none"}
  - {id: "F-EM-1", stage: "07 Emerging Moat", rule: "P07 Section 5 matrix (HH=4 ... LL=1, no evidence=0); verifier rule 3", severity: "MAJOR", stated: "A3 (DOC, AR p.57-58), H3 (DOC, AR p.21), C1 (CLAIM, AR p.5, CARE p.2) evidenced but scored 0 as not moat-grade, while Weak rows G1, E1, E2 take the matrix floor; em_score 10.1, NONE", recomputed: "A3 LL 1 x 1.0 + H3 LL 1 x 1.0 = 12.1, MODEST; with C1 LL 1 x 0.7 = 12.8, MODEST. B07's named separating observation (Anjar utilisation plus H2 CFO) moves F2/G2 and does not separate these readings; the rubric does", decision_impact: "B07 combined AVOID unchanged; em_classification NONE to MODEST feeds stage 11 Pillar 3. Phase-3 Verifier C: CRITICAL if the band change moves the destination PE by more than 1x"}
  - {id: "F-EM-2", stage: "07 Emerging Moat", rule: "P07 completionist guard recount; verifier rule 3", severity: "MINOR", stated: "report Section 3: 10 remaining documented items; block completionist_recount: 9", recomputed: "21 - 12 = 9 (block correct). Residual is C2 2, A3 1, F2 2, G1 2, E1 1, F1 1, not only C2, A3, F2. H3's AR p.21 items (tagged DOC in the Section 3 summary) sit outside the count while F1's inline item sits inside", decision_impact: "none: active categories 8 (10-11 under F-EM-1) stay under the stop line of 12"}
  - {id: "F-EM-3", stage: "07 Emerging Moat", rule: "P07 I2: for each moat claimed anywhere in the scan, name what the competitor must destroy", severity: "MINOR", stated: "answered for seamless (B1), Thailand reservation (B2), Anjar (E1)", recomputed: "unanswered: E2 exports, F2 execution, G1 war chest, H2 partnerships, R1 approvals, B2 certification stack. I2 0 stands: no named specific sacrifice with a DOC source appears anywhere in B07", decision_impact: "none"}
  - {id: "F-EM-4", stage: "07 Emerging Moat", rule: "one improvement, one mechanism (CLAUDE.md; B07 Section 3 allocation rule)", severity: "MINOR", stated: "B07 says the certification and approval stack is credited in B2 not R1; R1 4C rests on vendor approvals; 4A repeats NTPC approval (AR p.7), further seamless approvals (Q4 call p.12) and Siemens clearance (Q1 call p.5) from the B2 table; R1 0.7", recomputed: "R1 0.7 sustainable at LL x CLAIM on its own Section 4B policy items and the nuclear export pre-qualification (Q1 call p.11); no numeric change. Under B07's own not-moat-grade-unscored logic R1 would be 0 and the total 9.4", decision_impact: "none"}
critical_count: 0
major_count: 3
minor_count: 6
acceptance_rate: 87.5             # 63 passed / 72 checked (gate0 40/45, emoat 23/27)
```
