# QUARTERLY REVIEW: Aequs Limited (AEQUS), Q2 FY27 (quarter and half year ended 30-Sep-2026)
agent: A4 analyst (claude-opus-5-5) | results and call 26-Oct-2026 | review date 28-Oct-2026 | correction loop 1 applied (see LOOP 1 CHANGE LOG at end)
protocols: Role 4 Quarterly Results Review v1.4 (frameworks/Quarterly_Results_Review_Protocol_v1_4.md); Role 5 Quarterly Concall Analysis v1.1 (frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md). Master, FTTCP, Section 1B and RDE not loaded.
inputs: A1 structured and fulltext (results, presentation, press release, concall), A2 ledgers (4), A3 forensics (4, presentation file incl. LOOP 1 ADDITIONS), A5 audit (loop 1 entries F1, M1, M2, M3, C1), Notion snapshot 28-Oct-2026 (lines 1-190 and 629-755), monitoring checklist. No source PDF, transcript or inputs/ file opened.

## HEADER: DOCUMENT CAVEATS AND ANCHOR KEY

Anchor key. R-L### = results fulltext line. P-L### = presentation fulltext line. PR-L### = press release fulltext line. C-FT### = concall fulltext line (source line + 23). N-L### = Notion snapshot line. MC-L## = monitoring checklist line. R-A3-##, P-A3-##, PR-A3-##, C-A3-## = A3 finding IDs for results, presentation, press release, concall.

Evidence tiers. FILED = statutory results under limited review. MGMT-FILED = management statement inside a filed deck or press release. ASR-UNVERIFIED = concall machine transcript. NOTION-PRIOR = unsigned Notion page content. INFERENCE = A4 arithmetic or reading.

Caveats.
1. Results pages 2-5 and 8-12 were image-only. A1 transcribed them visually after OCR failed (R-L10-L12). A2 tie-outs pass 344 of 346. The two non-ties sit in the consolidated 6M 30-Sep-2025 column: total expenses R441 (gap Rs 2.00 Mn) and cash from operations R843 (gap Rs 2.26 Mn; R777 add-back reads nil). This review uses that column for H1 FY26 comparatives and marks each use. Every load-bearing Q2 FY27 number below was cross-checked against the deck or press release, and each tie is stated at its row.
2. Concall: machine transcript (faster-whisper small.en), management tier, UNVERIFIED. Speakers are inferred. Numbers may be misheard. Source gap 00:19:48 to 00:21:02 (C-FT307-308). Filed documents win on conflict. Every concall-only number carries the tag ASR-UNVERIFIED.
3. Presentation A1 errata applied: consumer revenue Q1 FY27 = 734, Q2 FY27 = 577 Rs Mn (R149/R150 corrected); Hosur Phase 1 is investment start Q4 FY27, commercial production FY29 (R464/R484 corrected); deck unit is Rs Mn (structured file ERRATA, lines 592-597).
4. Units. All filings print Rs Mn (R-L83, R-L372; P-L153). Conversion: Rs Mn x 0.1 = Rs Cr. All analysis below is in Rs Cr unless marked Mn.

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 21 notes / 84 turns / 38 slides (presentation 33 slides plus press release 5 pages). All 21 notes, 84 turns and 38 slides reviewed. Results ledger 1,438 of 1,438 IDs referenced, presentation 566 of 566, press release 171 of 171, concall 386 of 386 (302 R plus 84 T). Orphans: none in any ledger. Unreviewed rows: none.

Findings incorporated: results R-A3-01 to R-A3-26 (26); presentation P-A3-01 to P-A3-24 (24, incl. loop 1 additions P-A3-23 GoK MoU and P-A3-24 top-5 customer concentration); press release PR-A3-01 to PR-A3-18 (18); concall C-A3-01 to C-A3-24 (24). Total 92 findings. Of these, 75 are FORWARD-SIGNAL or AMBIGUOUS, and each maps to at least one Questions-for-Management row (Section QfM, mapping column).

A4 resolutions of A3 ambiguities by arithmetic on filed lines (no new number added):
- P-A3-13, PR-A3-10, C-A3-06 (unallocated about Rs 137 Mn): the filed segment table splits it. Segment eliminations Rs (104.21) Mn plus unallocated corporate expense Rs (32.94) Mn = Rs (137.15) Mn (R-L569, R-L586). Total segment results 277.62 less 32.94 = 244.68 = consolidated EBITDA (R-L570, R-L384). The open question is the eliminations line, which rose from Rs (46.65) Mn in Q2 FY26.
- P-A3-18 ("4% QoQ" on parts): 5,978 less 238 = 5,740; 238 / 5,740 = 4.1%. The 4% is portfolio growth, not growth in parts added (P-L193-197). The web review (N-L678) reads it the same way.

## DECISION STATUS VERIFICATION (before any position framing)

| Item | Notion reading | Anchor |
|---|---|---|
| Decision Status | NOT SET (operator-only) | MC-L3; N-L29 |
| Mental Model | v2, DRAFT, UNSIGNED | N-L29, N-L33 |
| Phase 1 verdict | REWORK (run runs/aequs-2026-09-05) | N-L27 |
| Entry zone / MoS / stop | None on file | N-L29; MC-L3 |
| Promoter Verdict | CAUTION (B08); integrity-vs-structure ruling PENDING (Hasbro) | N-L10 property |
| Gate 0 Classification (property) | AVOID, core 23/100, total 32/160 | N-L10 property |
| Position Size | blank (not held) | N-L10 property |

Framing: this is a thesis check against an UNSIGNED draft model for a NON-HELD name. Position branch: 8A-W. This review never sets or recommends a Decision Status. It flags; the operator decides.

---

# SECTION A: RESULTS REVIEW (ROLE 4)

## STEP 0: PRE-FLIGHT

### 0A. Notion baseline

| Element | Content | Anchor |
|---|---|---|
| One-line thesis (draft) | Three businesses in one shell: aerospace (81% of Q1 FY27 revenue, build-to-spec), consumer electronics at Hubballi (about 15%, ramping), toy moulding at Koppal (about 4%, customer lost) | N-L35-41 |
| Aerospace destination | Cost-advantaged converter with very high switching costs; no pricing power | N-L45 |
| Four-pillar destination PE | None. Stages 10 and 11 did not run | N-L29 |
| Projections (unsigned) | FY27 base revenue 1,690, EBITDA 154, PAT (158); FY28 base revenue 2,218, EBITDA 354, PAT 42. PAT bear/base/bull FY27 (225)/(158)/(92); FY28 (83)/42/105 | N-L90-103 |
| Thesis-broken condition | Falsification line: Q2 FY27 consumer segment EBITDA loss at or wider than Rs 36.1 cr with consumer utilisation still at or below 23% | N-L117 |
| Monitoring checklist | Seven monitorables | N-L107-113; MC-L6-12 |
| Proposed tripwire (not adopted) | Pledge invocation OR facility above Rs 200 Cr OR "investment" identified as an Aequs related party | N-L181-185 |
| Devil's advocate findings | None on file (Stage 15 did not run) | N-L29 |
| Decision Status | NOT SET | MC-L3 |

### 0B. Unit convention
All figures in Rs Millions (R-L83, R-L372, R-L429, R-L488, R-L560). Converted to Rs Crores at x0.1.

### 0C. Share-count changes

| Event | Detail | Anchor | Tier |
|---|---|---|---|
| IPO fresh issue (FY26) | Paid-up capital Rs 6,050.02 Mn at Q2 FY26 to Rs 6,706.66 Mn from FY26 year-end; unchanged through Q2 FY27 | R-L109, R-L415 | FILED |
| Basic shares in issue | 670.67 Mn (Rs 6,706.66 Mn / Rs 10 face value) | R-L109 | FILED (count derived from paid-up) |
| ESOP exercise | Rs 16.29 Mn proceeds in H1 FY27 (consolidated) | R-L534 | FILED |
| ESOP trust treasury shares | Weighted shares implied about 656 Mn ((1,056.20) / (1.61)), below 670.67 Mn | R-A3-17; R-L398, R-L419 | INFERENCE |
| Promoter warrants | Up to 28,071,690 warrants, Rs 6,500 Mn, approved by board 25-Sep-2026 and EGM 22-Oct-2026, "subject to receipt of requisite regulatory approvals"; "proposed to be converted on or before December 31, 2027" | R-L272-275, R-L665-667 | FILED |
| Fully diluted shares if warrants convert | 670.67 + 28.07 = 698.74 Mn | R-L109, R-L272 | INFERENCE |
| ESOP grant 2 lakh options at Rs 235.50 | Recorded only on the web side (26-Oct) | N-L703 | NOTION-PRIOR; not in this corpus |

No split, bonus or buyback. Reported EPS is the share-adjusted EPS.

### 0D. Notes extraction (standalone S1-S10, consolidated C1-C8, C10-C12; no C9 printed)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| S1 / C1 | Basis of preparation | Ind AS 34, Reg 33; includes Aequs Stock Option Plan Trust | ND | All | None |
| S2 / C2 | Review | Audit Committee and Board approved 26-Oct-2026; limited review, unmodified | ND | Q2/H1 FY27 | None |
| S3 / C3 | Comparatives | Q2 FY26 (and standalone H1 FY26) approved by Board but not audited or reviewed | ND | Q2 FY26 | YoY base is unreviewed; lean bear on any YoY claim (R-L244-246, R-L619-621) |
| C4 | H1 FY26 source | Consolidated 6M Sep-2025 figures come from audited special-purpose interim statements made for the IPO | ND | H1 FY26 | H1 FY26 base is audited; Q2 FY26 is not (R-L622-623) |
| S4 | SQuAD impairment reversal | FY26 reversal of past impairment on SQuAD JV investment, Rs 234.39 (unit not printed) | 23.44 (standalone FY26) | FY26 | One-off in FY26 standalone; no consolidated twin (R-L248-249) |
| S5 / C6 | IPO expenses | Rs 476.22 Mn incurred; Rs 39.02 Mn expensed as exceptional, Rs 437.20 Mn against securities premium | 3.90 exceptional | FY26 | FY26 one-off (R-L251-253, R-L652-653) |
| S6 / C7 | Labour Codes | Gratuity impact from wage definition, exceptional: standalone Rs 7.92 Mn, consolidated Rs 37.93 Mn | 3.79 consolidated | FY26 | FY26 one-off (R-L255-261, R-L654-659) |
| C5 | Consolidation list | 22 entities; ATHPL dissolved 17-Sep-2026; AMPL formerly Aequs Toys | ND | Q2 FY27 | Entity change in consumer chain (R-L624-651) |
| S7 / C8 | Amalgamation | Scheme (ASMIPL, AEPPL, AFCPPL into parent), board 23-Apr-2026, rejected by RD order 12-Oct-2026 (after quarter-end); company "evaluating"; "no material impact on the business operations" | ND | Forward | One offset route for subsidiary losses stays blocked; note silent on tax (R-L263-270, R-L660-664) |
| S8 / C10 | Warrants | 28,071,690 warrants, Rs 6,500 Mn, subject to approvals, EGM-approved 22-Oct-2026, "proposed to be converted" by 31-Dec-2027 | 650.0 gross (325.0 due on allotment; balance on conversion; none received) | Forward | Dilution 4.19% on conversion (R-L272-275, R-L665-667) |
| S9 / C11 | Segments | CODM is Executive Chairman and CEO; two segments, Aerospace and Consumer; unallocable or non-recurring items shown as unallocable | ND | All | Segment results carry other income (P-L396) |
| S10 / C12 | Publication | Results on BSE, NSE and company website | ND | n/a | None |
| C9 | (absent) | Printed numbering jumps from 8 to 10 | ND | n/a | Drafting slip (R-L680) |

Exceptional items: nil in every FY27 period (R-L99, R-L389). FY26 consolidated exceptional loss Rs (76.95) Mn = IPO (39.02) + Labour Codes (37.93) (R-L389; R-A3 reconciliation).

Notes that change interpretation: S3/C3 (unreviewed YoY base), C8 (one loss-offset route blocked after quarter-end), C10 (dilution), C5 (consumer entity cleanup linked to the discontinued-operations line R-L395).

Auditor opinion check. Standalone LRR: unmodified; Q2 FY26 comparatives not reviewed (R-L244-246; ledger S-LRR-4). Consolidated LRR: unmodified; paragraph 6 other matter: one unnamed subsidiary reviewed by another auditor whose report "has been furnished to us by the Parent's management"; assets Rs 1,293.62 Mn, revenue Rs 324.99 Mn (Q2) and Rs 712.44 Mn (H1), loss Rs 30.81 Mn (Q2) and Rs 73.86 Mn (H1); "Our conclusion is not modified in respect of this matter" (R-L753-766). No Emphasis of Matter. No going-concern paragraph. Status: unmodified with an other-matter paragraph. AMBER note: the subsidiary is unnamed (R-A3-22).

### 0E. Business type
Standard operating business (precision manufacturing). Steps 1 and 5 apply; lender variants do not.

Checkpoint: Notion fetched with Decision Status (NOT SET), units Rs Mn, share-count changes noted, notes extracted, auditor opinion verified, business type standard.

## STEP 1: DATA EXTRACTION TABLE

### 1-C. Consolidated (Rs Cr; source R-L375-L419)

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 (a) | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations (R-L375) | 281.59 | 395.55 | 409.08 | 537.16 | 804.62 | 1,230.44 | ND |
| Other income (R-L376) | 15.75 | 6.72 | 10.61 | 28.39 | 17.34 | 65.38 | ND |
| Total income (R-L377) | 297.34 | 402.27 | 419.69 | 565.55 | 821.96 | 1,295.82 | ND |
| Cost of materials consumed (R-L378) | 126.36 | 167.35 | 184.62 | 232.69 | 351.98 | 522.31 | ND |
| Change in inventories (R-L379) | (15.35) | 1.19 | (22.53) | (15.44) | (21.35) | (27.52) | ND |
| Employee benefits (R-L380) | 49.29 | 68.99 | 75.79 | 92.76 | 144.78 | 212.18 | ND |
| Impairment on financial assets (R-L381) | (0.09) | (0.04) | (0.05) | 0.23 | (0.09) | (1.11) | ND |
| Finance costs (R-L385) | 25.70 | 18.85 | 20.60 | 35.75 | 39.45 | 92.35 | ND |
| Depreciation and amortisation (R-L386) | 32.60 | 45.34 | 46.53 | 57.16 | 91.87 | 137.69 | ND |
| Other expenses (R-L382) | 92.88 | 143.29 | 157.40 | 171.00 | 300.68 | 435.51 | ND |
| Total expenses (B), excl. finance and D&A (R-L383) | 253.08 | 380.78 | 395.22 | 481.44 | 776.01 | 1,141.37 | ND |
| EBITDA as printed, A-B, incl. OI (R-L384) | 44.25 | 21.49 | 24.47 | 84.11 | 45.95 | 154.45 | ND |
| Share of JV and associate (R-L388) | 2.10 | 2.90 | 1.81 | 3.38 | 4.71 | 11.75 | ND |
| Exceptional items (R-L389) | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | (7.70) | ND |
| Profit before tax, continuing (R-L390) | (11.95) | (39.81) | (40.85) | (5.42) | (80.66) | (71.54) | ND |
| Tax expense (R-L393) | 8.65 | 13.42 | 11.35 | 11.27 | 24.77 | 41.76 | ND |
| of which current tax (R-L391) | 8.37 | 12.52 | 12.08 | 10.99 | 24.60 | 40.03 | ND |
| PAT, continuing (R-L394) | (20.60) | (53.23) | (52.20) | (16.68) | (105.42) | (113.29) | ND |
| Discontinued operations (R-L397) | 0.01 | (0.00) | (0.20) | (0.29) | (0.20) | 0.04 | ND |
| PAT (R-L398) | (20.59) | (53.23) | (52.39) | (16.98) | (105.62) | (113.25) | ND |
| EPS reported, Rs (R-L419) | (0.35) | (0.81) | (0.80) | (0.30) | (1.61) | (1.87) | ND |
| EPS share-adjusted, Rs (no split/bonus; = reported) | (0.35) | (0.81) | (0.80) | (0.30) | (1.61) | (1.87) | ND |

(a) H1 FY26 consolidated column carries the A2 TIE_FAIL on total expenses (R441, gap Rs 2.00 Mn = Rs 0.20 Cr). The printed total ties to EBITDA. Component rows in this column may hold a Rs 0.20 Cr transcription error.
FY27 column: no full-year results yet; ND.

Cross-checks of Q2 FY27 load-bearing numbers against the deck and press release: revenue 4,091 (P-L424; PR-L81) ties to 4,090.79; EBITDA 245 (PR-L85; P-L291) ties to 244.68; PAT (522) (P-L295; PR-L90) ties to continuing PAT (521.96); total PAT incl. discontinued is (523.92) (R-L398). H1 PAT (1,054) (PR-L90) ties to continuing (1,054.24). Consumer revenue 577 and aerospace 3,514 (P-L371, P-L383 per errata; PR-L109, PR-L114) tie to R-L563-564. Consumer EBITDA (401) (PR-L118; P-L383) ties to R-L567.

### 1-C derived metrics (Rs Cr)

| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | Printed EBITDA less OI (excludes JV share) | 28.51 | 14.76 | 13.86 | 55.72 | 28.62 | 89.07 | ND |
| Operating EBITDA margin | Op EBITDA / revenue | 10.12% | 3.73% | 3.39% | 10.37% | 3.56% | 7.24% | ND |
| Reported EBITDA | Printed A-B line, incl. OI | 44.25 | 21.49 | 24.47 | 84.11 | 45.95 | 154.45 | ND |
| Reported EBITDA margin | Reported / revenue | 15.72% | 5.43% | 5.98% | 15.66% | 5.71% | 12.55% | ND |
| Core PBT (ex OI) | PBT less OI | (27.70) | (46.53) | (51.46) | (33.80) | (97.99) | (136.92) | ND |
| Other income / PBT | OI / PBT | NM (PBT<0) | NM (PBT<0) | NM (PBT<0) | NM (PBT<0) | NM (PBT<0) | NM (PBT<0) | ND |
| Effective tax rate | Tax / PBT | -72.3% | -33.7% | -27.8% | -208.0% | -30.7% | -58.4% | ND |
| PAT margin | PAT / revenue | -7.31% | -13.46% | -12.81% | -3.16% | -13.13% | -9.20% | ND |

NM = not meaningful because the denominator is negative. Protocol formula "PBT + D + Finance" would add JV share and exceptional items into EBITDA; this review uses the printed A-B line (R-L384) as reported EBITDA and states that choice.

### 1-S. Standalone (parent; Rs Cr; source R-L86-L112)

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations | 27.82 | 38.52 | 35.55 | 56.25 | 74.07 | 123.86 | ND |
| Other income | 6.55 | 9.33 | 10.31 | 13.29 | 19.64 | 54.53 | ND |
| Total income | 34.37 | 47.85 | 45.86 | 69.54 | 93.71 | 178.39 | ND |
| Cost of materials consumed | 12.83 | 22.05 | 17.87 | 22.37 | 39.92 | 54.31 | ND |
| Change in inventories | (1.58) | (4.33) | (2.87) | 1.77 | (7.20) | (1.29) | ND |
| Employee benefits | 5.84 | 6.31 | 7.52 | 10.72 | 13.83 | 23.62 | ND |
| Finance costs | 2.34 | 0.98 | 1.66 | 4.38 | 2.64 | 8.85 | ND |
| Depreciation | 2.39 | 2.45 | 2.82 | 4.74 | 5.27 | 9.45 | ND |
| Other expenses | 10.60 | 15.18 | 17.39 | 19.84 | 32.58 | 46.24 | ND |
| Total expenses (B) | 27.69 | 39.22 | 39.90 | 54.62 | 79.13 | 122.81 | ND |
| EBITDA as printed | 6.68 | 8.63 | 5.96 | 14.92 | 14.59 | 55.59 | ND |
| Exceptional gain | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 18.75 | ND |
| PBT | 1.95 | 5.20 | 1.48 | 5.80 | 6.68 | 56.03 | ND |
| Tax | 1.78 | 1.14 | (0.31) | 1.78 | 0.82 | 6.23 | ND |
| PAT | 0.17 | 4.07 | 1.79 | 4.02 | 5.86 | 49.80 | ND |
| EPS reported, Rs | 0.00 | 0.06 | 0.03 | 0.07 | 0.09 | 0.82 | ND |
| Operating EBITDA (ex OI) | 0.13 | (0.70) | (4.36) | 1.64 | (5.06) | 1.05 | ND |

Parent profit is intra-group: H1 interest income on amortised-cost assets Rs 13.27 Cr and financial guarantee income Rs 5.95 Cr, both non-cash (R-L181, R-L185). Excluding them, parent H1 PBT is Rs (12.54) Cr. Parent H1 CFO Rs (26.78) Cr (R-L202). Standalone EPS carries no operating signal (R-A3-09).

### 1-G. Standalone vs consolidated PAT gap (first-class metric; A3 F2)

| Period | Standalone PAT (Rs Cr) | Consolidated PAT (Rs Cr) | Gap C less S (Rs Cr) | Gap as % of standalone PAT | Subsidiaries plus eliminations (Rs Cr) | Anchor |
|---|---|---|---|---|---|---|
| Q2 FY26 | 0.17 | (20.59) | (20.76) | -12,358% | (22.86) | R-L104, R-L398; R-A3-07 |
| Q1 FY27 | 4.07 | (53.23) | (57.29) | -1,409% | (60.20) | same |
| Q2 FY27 | 1.79 | (52.39) | (54.18) | -3,025% | (55.99) | same |
| H1 FY26 | 4.02 | (16.98) | (20.99) | -523% | (24.38) | same |
| H1 FY27 | 5.86 | (105.62) | (111.48) | -1,903% | (116.19) | same |
| FY26 | 49.80 | (113.25) | (163.05) | -327% | (174.80) | same |

H1 FY26 gap as % of standalone: (209.94)/40.17 = -523% (INFERENCE; A3 F2 gives the Rs Mn gap). The gap swing is far beyond the 5 pp test. Losses sit outside the parent. Subsidiaries plus eliminations lost Rs 55.99 Cr in Q2 against Rs 22.86 Cr a year earlier: 2.4x YoY (R-A3-07).

Checkpoint: extraction tables complete; every cell filled or ND or NM with legend.

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26; consolidated, Rs Cr)

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from operations | 281.59 | 409.08 | +45.3% | Strong; on the unreviewed Q2 FY26 base |
| Operating EBITDA (ex OI) | 28.51 | 13.86 | -51.4% | Weak |
| Operating EBITDA margin | 10.12% | 3.39% | -673 bps | Weak |
| Reported EBITDA margin (incl OI) | 15.72% | 5.98% | -974 bps | Weak |
| Depreciation | 32.60 | 46.53 | +42.7% | Scaling with revenue |
| Finance costs | 25.70 | 20.60 | -19.8% | Lower YoY (IPO deleveraging); rising QoQ |
| EBIT (operating) = Op EBITDA less D&A | (4.09) | (32.67) | worse by 28.58 | Weak |
| Other income | 15.75 | 10.61 | -32.6% | Lower |
| Core operating PBT (PBT less OI) | (27.70) | (51.46) | worse by 23.76 (-85.8%) | Weak |
| Reported PBT | (11.95) | (40.85) | worse by 28.90 | Weak |
| PAT | (20.59) | (52.39) | worse by 31.80 | Weak |
| EPS (share-adjusted = reported), Rs | (0.35) | (0.80) | worse by 0.45 | Weak; weighted share count rose with IPO |

Diagnostics.
- Revenue grew 45.3% YoY. The prior company guide was 45-50% consolidated (N-L101); Q2 sits at its lower edge. The Notion FY27 base implies +37.4% (1,690 / 1,230). At the Q2 run-rate FY27 lands at 1,622.8, which is +31.9% (INFERENCE).
- Operating EBITDA margin was 3.39% in Q2 FY27 vs 10.12% in Q2 FY26: a 673 bps contraction. Reported margin fell 974 bps (5.98% vs 15.72%). Management says the FY26 base held pre-operative consumer cost (PR-L95-96; P-L337-341), so the base is not like-for-like. The capitalised amount is ND (P-A3-19).
- Core operating PBT did not grow. It worsened from (27.70) to (51.46). Reported PBT and PAT also worsened. No headline growth is hiding a core decline; both fell.
- Gap between core PBT change (-23.76) and PAT change (-31.80): other income fell 5.13, tax rose 2.70, discontinued operations moved 0.21. Sum -8.04 (INFERENCE; ties within rounding).
- D&A grew 42.7% vs revenue 45.3%. No group-level absorption deficit. At segment level the consumer line carries D&A of Rs 27.43 Cr on revenue of Rs 57.67 Cr, or 47.6% of revenue (R-L576, R-L564).
- Other income fell YoY (10.61 vs 15.75) but rose QoQ (10.61 vs 6.72). Management attributes the Q2 rise to forex (C-FT222-224; ASR-UNVERIFIED). Stripping it, operating EBITDA fell 6.2% QoQ (14.76 to 13.86). The sequential "EBITDA up 14%" headline (P-L305) is other income (P-A3-15; C-A3-05).

Checkpoint: YoY table and six diagnostics complete.

## STEP 3: SEQUENTIAL TRAJECTORY (consolidated, Rs Cr)

| Quarter | Revenue | Op EBITDA margin | Core PBT (ex OI) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 (H1 FY26 less Q2 FY26; INFERENCE) | 255.57 | 10.65% | (6.11) | H1 FY26 TIE_FAIL column; Q2 FY26 unreviewed | base |
| Q2 FY26 (R-L375-390) | 281.59 | 10.12% | (27.70) | Comparative unreviewed (R-L619-621) | +10.2% |
| H2 FY26, two quarters combined (FY26 less H1 FY26; Q3/Q4 split ND) | 693.28 (avg 346.64 per quarter) | 4.81% | (103.11) incl. exceptional (7.70); (95.42) ex exceptional, avg (47.71) per quarter | Exceptional (7.70) in FY26; consumer plant commissioned end-Q3 FY26 (N-L101) | avg +23.1% vs Q2 FY26 |
| Q1 FY27 (R-L375-390) | 395.55 | 3.73% | (46.53) | None printed | +14.1% vs H2 avg |
| Q2 FY27 (R-L375-390) | 409.08 | 3.39% | (51.46) | OI forex rise; H1 non-cash gains Rs 12.41 Cr inside EBITDA (R-A3-08); discontinued (0.20) | +3.4% |

Diagnostics.
- Trajectory: revenue stepping up; operating margin dipping; core loss widening. Revenue up 60% from Q1 FY26 to Q2 FY27, while core PBT moved from (6.11) to (51.46).
- One-offs: FY26 exceptional items (IPO cost, Labour Codes). H1 FY27 EBITDA holds Rs 12.41 Cr of non-cash gains: inventory-provision reversal 8.37, liabilities written back 2.07, lease derecognition gain 1.31, disposal gain 0.66 (R-L500, R-L498, R-L510, R-L496). These equal 27.0% of H1 EBITDA (R-A3-08). The Q2/Q1 split is ND. The P&L lines that hold them are ND.
- H1-average test: Q2 revenue of 409.08 exceeds the H1 average of 402.31 by 1.7%. Consumer revenue of 57.67 sits below its H1 average of 65.53. The consumer plant, commissioned at end-Q3 FY26, did not lift its own run-rate in Q2. Red flag on the capex-commissioning test for consumer.
- Implied Q3 FY27 base to hold trajectory: revenue at or above 409.08; consumer revenue at or above 57.67 (Q2) and at 73.39 to recover Q1.

Checkpoint: QoQ table and diagnostics complete.

## STEP 4: OPERATIONAL DECOMPOSITION (PAT bridge, Q2 FY27 vs Q2 FY26, Rs Cr)

| Component | YoY change (Rs Cr) | Share of PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution at prior op margin (127.49 x 10.12%) | +12.91 | -41% | Recurring |
| Margin change contribution ((3.39% less 10.12%) x 409.08) | -27.56 | +87% | Recurring |
| D&A change | -13.93 | +44% | Recurring (post-capex) |
| Finance cost change | +5.10 | -16% | Recurring (post-debt); rising QoQ |
| Other income change | -5.13 | +16% | Non-recurring typically (forex) |
| Share of JV change | -0.29 | +1% | Mixed |
| Effective tax change (tax 11.35 vs 8.65) | -2.70 | +8% | Mixed; recurring while subsidiary losses cannot offset aerospace profit |
| Exceptional items | 0.00 | 0% | Non-recurring |
| Discontinued operations | -0.21 | +1% | Non-recurring |
| Reported PAT YoY change | -31.80 | 100% | |

Arithmetic (Rs Mn): -146.52 op EBITDA (+129.06 revenue, -275.58 margin) -139.29 D&A +51.00 finance -51.32 OI -2.85 JV -26.97 tax -2.04 discontinued = -317.99 = -523.92 less -205.93 (R-L384, R-L376, R-L385, R-L386, R-L388, R-L393, R-L397, R-L398). Ties exactly.

Answers.
- Recurring core operations (op EBITDA, D&A, finance) explain -23.48 of -31.80, or 74%. Other income explains 16%. Tax explains 8%.
- If other income went to zero, Q2 pre-tax loss widens by 10.61. Tax would not fall because the taxed entities are the profitable aerospace ones (C-FT245-247; ASR-UNVERIFIED). Run-rate PAT ex OI is about (63.0) per quarter, (252) annualised (INFERENCE).
- D&A is near steady state for now: 46.53 vs 45.34 QoQ (+2.6%). CWIP rose from 78.66 to 123.56 (R-L434), so D&A will step up as it capitalises. Finance cost is ramping: 20.60 vs 18.85 QoQ (+9.3%) as borrowings rose 157.61 in H1 (R-L460, R-L467). Aerospace segment finance cost rose 53% QoQ (7.79 to 11.94; R-L571).
- Tax: Q2 deferred tax is a credit of 0.73 (R-L392); current tax 12.08 on a loss. Tax on a loss is not new: Q2 FY26 tax 8.65 on PBT (11.95) and FY26 tax 41.76 on PBT (71.54) (R-L390, R-L393), both before the board approved the amalgamation scheme on 23-Apr-2026 (R-L263). No DTA recognised on consumer losses: consolidated DTA 31.58 vs 31.74 at March (R-L441). This is a drag, not an inflation. H1 tax drag vs a statutory credit is about Rs 45.1 Cr (R-A3-15; INFERENCE).

Checkpoint: bridge and answers complete.

## STEP 5: CASH QUALITY AND BALANCE SHEET (consolidated, H1 cash flow; Rs Cr)

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (R-L523) | H1 FY26 47.90 (b) | H1 FY27 (80.83) | -128.73 | RED |
| CFO/PAT | H1 FY26 NM (PAT (16.98), CFO positive) | H1 FY27 NM (both negative) | n/a | Below every Pillar 2 band; flag to /fttcp |
| Capex, PPE acquisition (R-L524) | H1 FY26 199.94 | H1 FY27 164.83 | -35.11 | Deck nets disposals: 159.7 (P-L501; R-L525) |
| FCF (CFO less PPE capex) | H1 FY26 (152.04) | H1 FY27 (245.66) | -93.62 | RED |
| Working-capital change (sum of WC lines R-L511-L520) | H1 FY26 (18.99) | H1 FY27 (102.76) | -83.77 | RED |
| Receivable days (on revenue; H1 annualised) | 31-Mar-26 78.5 | 30-Sep-26 67.8 | -10.7 | GREEN (denominator effect) |
| Inventory days (on revenue) | 168.3 | 155.0 | -13.3 | AMBER; absolute +115.75 |
| Payable days (on revenue) | 95.6 | 86.8 | -8.8 | AMBER |
| Cash conversion cycle | 151.2 | 136.0 | -15.2 | Days improve only through annualised H1 revenue (P-A3-17) |
| Absolute NWC (receivables + inventory less trade payables) | 509.71 | 599.28 | +89.57 (+17.6%) | RED |
| PPE (R-L432) | 773.21 | 797.22 | +24.01 | n/a |
| CWIP (R-L434) | 78.66 | 123.56 | +44.90 | Building; not capitalised |
| Gross borrowings (R-L460 + R-L467) | 403.58 | 561.19 | +157.61 (+39%) | RED |
| Cash and bank (R-L447 + R-L448) | 356.65 | 199.85 | -156.80 | RED |
| Net debt ex leases | 46.93 | 361.34 | +314.41 | RED |
| Lease liabilities (R-L461 + R-L468) | 297.35 | 275.23 | -22.12 | n/a |
| Net debt incl. leases | 344.28 | 636.57 | +292.29 | RED |
| Net debt / equity ex leases (equity R-L459) | 0.03 | 0.26 | +0.23 | AMBER |
| Net debt / equity incl. leases | 0.23 | 0.46 | +0.23 | Matches deck 0.2 to 0.5 (P-L1186-1187) |
| Promoter pledge | ND in this corpus (Notion: 100% of the Foundation's 14.99% stake pledged 21-Sep-2026, N-L162-163) | ND in this corpus | ND | Tripwire test below |

(b) H1 FY26 cash from operations carries the A2 TIE_FAIL (R843 printed 541.96 vs components 539.70; R777 likely 2.26). Printed CFO (A) 479.02 used.

Days use revenue as the denominator to match management's stated method (C-FT255-257; ASR) and the deck (P-L1193). COGS-based days: ND (the filing gives no gross-margin COGS line).

Operating cash before working capital was +34.68 Cr in H1 (cash from operations (68.09) less WC (102.76)); the WC build turned it negative (INFERENCE from R-L511-L521). Taxes paid 12.74 (R-L522).

Standalone cash: CFO (26.78) (R-L202); PPE (10.18) (R-L203); borrowings 30.00 vs 11.51 (R-L147, R-L152); cash and bank 77.28 vs 128.94 (R-L137-138). Parent net cash 47.28 vs 117.42.

Mandatory questions.
- CFO/PAT does not meet any Pillar 2 band. Both terms are negative. FY26 CFO was also negative at (98.75) (N-L111). Two consecutive negative half/full-year readings. Flag for /fttcp.
- WC drag: structural or growth-induced? Management says receivables (+34.14) and inventory (+115.75) are "both driven by aerospace growth" (C-FT254-255; ASR-UNVERIFIED). Consumer revenue fell 21% QoQ in the same half, and no segment WC split is filed. Test: if growth stopped, would days stay high? Inventory days at 155 sit above the 120-day target management names (C-FT543). Classification: INDETERMINATE-WITH-DIRECTION (negative). Missing evidence: segment inventory split and the Q3 inventory reading. No rating-agency commentary in this corpus (CARE BBB- on file in Notion, N-L130, not refreshed).
- CWIP did not capitalise. It rose 44.90. Capex went to aerospace: aerospace segment assets +121.75 in H1 vs consumer -39.07 (R-L590-591).
- No projected net-debt range exists in Notion. Net debt ex leases rose 314.41 in six months. The Rs 325 Cr warrant upfront roughly equals that rise. The upfront was not received in H1 (R-L533 nil). The second Rs 325 Cr is due only on conversion and is not a committed inflow at CMP (6C-bis).

Cash conversion verdict: INDETERMINATE-WITH-DIRECTION (negative). Caps the review at PROCEED WITH CAVEATS or below. Named missing evidence: segment WC split, Q3 inventory days, warrant upfront receipt date.

Checkpoint: cash table and answers complete.

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

5.5A. Tracker rows not supplied. The Notion property lists three linked Downstream Signals rows (N-L10); their content was not passed to this run. Count of signals readable this run: 0. Flag: fewer than three readable signals; reopen Role 5.5 at /fttcp (OR-17 floor applies there).

5.5B. Reconciliation not possible without tracker rows. Target reported: WEAK (consumer down, core loss wider, CFO negative); aerospace STRONG. Signal side: ND.

5.5C. New dependencies surfaced this quarter (payload candidates only; written only through the run's operator-approval gate; Decision Status never written):

| Proposed signal | Case | Reason | Anchor |
|---|---|---|---|
| Consumer breakeven re-date and consumer utilisation | B (new) | Falsification line fired; breakeven date withdrawn | R-L567; P-L184; P-L265 |
| Net debt and warrant upfront receipt; warrant conversion | B (new) | Net debt ex leases +314.41 Cr; upfront not received; balance optional below Rs 231.55 | R-L460-467; R-L533; R-L274-275 |
| Toy replacement customer ramp (Mattel per Notion; "metal" in ASR) | B (new) | Old customer phases out Q3; new customer "almost completely" Q4 | C-FT494-504; N-L47 |
| Safran six-entity agreements, value and start | A (add to existing Safran row) | Post-quarter agreements; commercialisation FY29 | P-L198-202; C-FT453-458 |
| Term-loan drawdown ("over Rs 800 Cr") | B (new) | Funding stack exceeds stated FY27 capex | C-FT767 |
| GoK MoU Rs 28,560 Mn: phasing, investing entity, funding | B (new) | Undated headline investment, 2.05x Sep-26 equity (P-A3-23) | P-L560-564 |
| Top-5 customer group share (63% of H1 FY27 revenue) | B (new) | Concentration with no segment split or trend (P-A3-24) | P-L775-778 |

5.5D. Step 6 proceeds on target-company numbers only. No signal weighting is possible this run.

## STEP 6: RECONCILIATION VS THESIS (unsigned draft model)

### 6A. Variance vs Notion projections (FY27; Rs Cr)

| Metric | Bear proj | Base proj | Bull proj | Actual / run-rate | Lands in |
|---|---|---|---|---|---|
| Revenue FY27 | ND (spread "only 13%", N-L103; values not given) | 1,690 (N-L94) | ND | H1 804.62 (R-L375); Q2 run-rate FY27 1,622.8 (INFERENCE) | Below base by 4.0%; bear value ND |
| EBITDA FY27 (Notion basis incl OI; FY26A 154 = R-L384 154.45) | ND | 154 (N-L95) | ND | H1 45.95; Q2 run-rate FY27 94.9 (INFERENCE) | Below base by 38%; bear value ND |
| EBITDA margin FY27 | ND | 9.1% (154/1,690) | ND | H1 5.71%; Q2 5.98% | Below base |
| PAT FY27 | (225) (N-L103) | (158) (N-L97) | (92) (N-L103) | H1 (105.62) (R-L398); Q2 run-rate FY27 (210.4) (INFERENCE) | Between bear and base, 78% of the way to bear |
| EPS FY27, Rs | ND | (2.36) (N-L99) | ND | H1 (1.61) (R-L419); run-rate (3.14) on 67.07 Cr shares | Below base |
| Net debt | ND (no projection) | ND | ND | 361.34 ex leases; 636.57 incl leases | ND |
| ROCE | ND | ND | ND | Deck ROCE -5% H1 annualised (P-L1200-1202) | ND |

Probability re-weighting rule: below bear on 2+ metrics for 2 consecutive quarters is not testable; bear values exist for PAT only, and PAT sits between bear and base. Rule not triggered on the evidence available.

### 6B. Watchlist item status

| # | Watchlist item | Green threshold | Red threshold | This quarter reading | Status |
|---|---|---|---|---|---|
| 1 | Consumer utilisation (N-L107) | Rising toward 40-50% FY27 exit | Falls further below 22% | 17% Q2 FY27 [MGMT-FILED, P-L184; basis incl. subsidiaries and JVs, P-L208]. Q1 22% [NOTION-PRIOR, N-L107; ASR analyst, undisputed, C-FT416; basis comparability unconfirmed]. "900 bps YoY", sign not printed (P-L190) | RED |
| 2 | Aerospace margin ex other income, two clean quarters at or above 20% (N-L108) | Two quarters at or above 20% ex OI | Below 20% ex OI | Reported segment margin 22.29% (R-L563, R-L566); page's harshest method (strip all consolidated OI) 19.27% (783.24 less 106.13, / 3,514.11); Q1 same method 20.59%. Segment OI allocation ND (P-L396) | RED on the page's method (conservative bias); reported basis passes; true value ND |
| 3 | Consumer capex commissioning (N-L109) | Capex phases down on the miss; no reversal | Consumer capex resumes before utilisation recovers | Consumer segment assets fell 1,286.86 to 1,247.80 in H1 (R-L591); H1 capex "predominantly towards aerospace"; consumer capex only on utilisation (C-FT365-372; ASR) | GREEN (did what it said) |
| 4 | New aerospace part numbers (N-L110) | Recovery from 86 | Below 86 | 238 added in Q2; portfolio 5,978 (P-L193-196; PR-L135-136) | GREEN |
| 5 | Operating cash vs capex (N-L111) | CFO covers capex | CFO negative | H1 CFO (80.83) vs PPE capex 164.83 (R-L523-524). Q2 alone (80.83) less Q1 (41.4) = (39.4) CFO vs about 81.8 capex (INFERENCE; Q1 base is MGMT-narrated per N-L111) | RED |
| 6 | DTA on merged-entity losses (N-L112) | DTA recognised on merged losses | Not recognised after merger | Amalgamation rejected 12-Oct-2026, after quarter-end (R-L265-266); DTA flat 31.58 vs 31.74 (R-L441) | UNKNOWN (test cannot run while the scheme is blocked) |
| 7 | FY27 auditor report, CARO, CFO seat (N-L113; MC-L12) | Clean FY27 audit; KMP filing or CFO certification | Qualification; no KMP filing | FY27 audit not due. LRR unmodified (R-L242, R-L618). CFO named in press release (PR-L158), deck (P-L204, R563) and on call (C-FT116). No Reg 30 KMP filing in corpus. Results signed by MD (R-L286, R-L674). No CFO certification | AMBER |

### 6C. Thesis-broken trigger check

| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| Falsification line, leg 1: consumer segment EBITDA loss (N-L117) | Loss at or wider than Rs 36.1 Cr | Rs (40.14) Cr: segment results Consumer (401.41) Mn (R-L567) [FILED]; ties to press release (401) (PR-L118) and deck (P-L383) | YES |
| Falsification line, leg 2: consumer utilisation (N-L117) | At or below 23% | 17% (P-L184) [MGMT-FILED]; analyst on call "22 to 17%", not disputed (C-FT415-416) [ASR-UNVERIFIED] | YES |
| Falsification line, combined | Both legs | Both legs met | FIRED |

Both legs fire. The loss leg rests on the statutory segment table. The utilisation leg rests on the filed deck's 17%; the threshold test needs only that figure. Its basis "includes subsidiaries and JVs" (P-L208). The 22% Q1 comparison is NOTION-PRIOR and ASR; its basis comparability cannot be proven without the prior deck. Conservative reading: FIRED.

Protocol consequence (8A-W): a fired condition maps to "reclassify to AVOID; record what would need to reverse". The name has no Decision Status, no position and an unsigned model. FLAG ONLY. This review does not recommend a status. The operator decides.

What would need to reverse: consumer segment revenue back above Rs 73.4 Cr per quarter with utilisation above the 22% Q1 record [NOTION-PRIOR, N-L107], and a newly named breakeven quarter (see 8C).

### 6C-bis. Proposed pledge tripwire (not adopted; N-L181-185)

| Limb | Threshold | Reading | Status |
|---|---|---|---|
| Invocation of the pledge | Any invocation | No pledge disclosure in the corpus | NOT FIRED (no evidence) |
| Facility grows past Rs 200 Cr | Any disclosure | No disclosure in the corpus | UNTESTABLE |
| "Investment" identified as an Aequs related party | Any identification | Warrants not yet allotted; "subject to receipt of requisite regulatory approvals" (R-L273); no upfront in H1 cash flow (R-L533); funding source of the Rs 325 Cr upfront not disclosed | UNTESTABLE |
| Overall | Any one limb | | NOT FIRED; two limbs UNTESTABLE |

Price context (INFERENCE): pledged block 10,05,13,070 shares (N-L162) x CMP Rs 212 = Rs 2,130.9 Cr, cover 10.7x the Rs 200 Cr facility, 6.6x the Rs 325 Cr upfront, 3.3x the full Rs 650 Cr. CMP Rs 212 sits 8.4% below the Rs 231.55 warrant price (N-L16); the issue price is 9.2% above market.

Warrant bear counter (A5 M3). Only Rs 3,250 Mn (50%) is due on allotment (C-FT269-270, ASR; N-L16). The balance comes only on conversion. The filed notes say the warrants "are proposed to be converted on or before December 31, 2027" (R-L274-275, R-L666-667) [FILED]. At CMP Rs 212, below the Rs 231.55 issue price, the second Rs 325 Cr is an option for the promoter, not committed cash. The promoter's "irrespective of market price" commitment letter is recorded only on the Notion page (N-L16) [NOTION-PRIOR]; it is not in this corpus. The filed word "proposed" is weaker, and filed evidence wins on conflict. If the warrants are not converted, the promoter forfeits the upfront and the company receives Rs 325 Cr, not Rs 650 Cr. Every funding-versus-capex comparison in this review that uses Rs 650 Cr carries this qualifier.

### 6C-ter. Spear load-bearing facts (MC-L28-31). FIRED = the fact as written no longer holds.

| Spear fact | Reading this quarter | Status |
|---|---|---|
| 1. FY27 aerospace revenue +25-30% at segment EBITDA margin above 20% and about 20% manufacturing ROCE | H1 aerospace revenue +42.1% YoY (673.57 vs 473.95; R-L563); Q2 +44.2%. Segment margin incl OI 22.47% H1, 22.29% Q2; harsh floor 19.27% Q2. Aerospace segment ROCE 22% H1 FY27 annualised (P-L1210-1213, per P-A3 reading) | NOT FIRED (holds on reported basis; margin ex OI ND) |
| 2. Consumer EBITDA negative, yet about Rs 500 cr of Rs 660 cr FY27 capex earmarked for consumer | Consumer EBITDA (40.14) Cr Q2 (R-L567). FY27 capex now "much lesser" than 660, H2 about equal to H1 about 160 Cr, larger share to aerospace (C-FT347-372; ASR-UNVERIFIED). Consumer segment assets fell (R-L591) | FIRED (superseded: the consumer capex earmark no longer holds) |
| 3. Cash conversion and balance sheet: losses, debt, interest, OCF vs capex, receivables and inventory | H1 CFO (80.83), FCF (245.66), net debt ex leases +314.41, inventory +115.75, finance cost rising QoQ (R-L523-524, R-L445, R-L385) | FIRED (risk materialised, adverse) |
| 4. USD 1,004 mn aerospace order book; 15-year Safran A320 agreement, deliveries FY28 | Order book USD 1,096 Mn, +9% QoQ (P-L193-198; PR-L131) [MGMT-FILED]; tenure above 15 years restated (P-L159-160). Deliveries FY28 not restated; new Safran capabilities "commercialization in FY 29" (C-FT458; ASR) | NOT FIRED on order book; FY28 delivery date UNTESTABLE |

### 6D. Growth trigger status (drawn from the Notion mental model and monitorables)

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| Aerospace growth on the order book (N-L39, N-L103) | High (80% of revenue, 8-year book) | H1 +42.1% (R-L563); order book +9% QoQ (P-L194); 238 parts (P-L193); utilisation 69% (P-L184) | Op margin incl OI 22.3% vs 25.9% YoY (R-L563, R-L566); aero finance cost +53% QoQ (R-L571); top 5 customer groups 63% of H1 revenue (P-L775-777) | ON TRACK |
| Consumer electronics ramp to Q4 FY27 EBITDA breakeven (N-L107) | Gated on utilisation | Customer "working with us" (C-FT436-444; ASR) | Breakeven date withdrawn (P-L265; C-FT179); revenue -21% QoQ (R-L564); utilisation 17% (P-L184) | WEAKENED (date dead; no replacement) |
| Toy line customer replacement (Mattel) (N-L47) | Low (customer of more than 90% left, N-L71) | Old customer phases out Q3; new customer "almost completely" Q4 (C-FT494-504; ASR) | Raw material shortages and logistics (P-L275; C-FT431-434) | DELAYED |
| Amalgamation and S.72A tax shelter (N-L71, N-L121) | Medium, about Rs 50-70 Cr once | None | RD rejection 12-Oct-2026, after quarter-end (R-L265); "evaluating", no route (R-L268) | DELAYED (rejected; route open) |
| Hosur aero-engine and landing-gear ecosystem with Safran (N-L10 Key Notes 13-Oct) | Long-dated | Safran six entities (P-L198-200); Phase 1 investment Q4 FY27; commercial production FY29 (P-L240-246 per errata) | No value, tenure or capex disclosed | ON TRACK (long-dated; no FY27-28 earnings) |
| Aerospace part additions as moat proxy (N-L110) | Questioned after 433 to 86 | 238 in Q2 (P-L193) | None | ON TRACK |

Checkpoint: 6A to 6D complete. The operator reviews at Step 8.

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

Deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts flagged for that session:
- A21 run-rate base inputs (FILED): Q2 FY27 revenue 409.08, op EBITDA 13.86, PAT (52.39); annualised revenue 1,636.3, PAT (209.6) (INFERENCE). One-offs to adjust: forex other income (Q2 10.61), H1 non-cash EBITDA gains 12.41, discontinued (0.20). Consumer is lumpy; a trailing-4-quarter base is ND because Q3 and Q4 FY26 are not split.
- Expectation ledger: no ledger rows were passed. If the Q4 FY27 consumer breakeven was ever ledgered, it is withdrawn without a date and fails its confirm-by at Q4 FY27 results.
- The refreshed base diverges from the Notion FY27 base by more than 25% on PAT ((210.4) vs (158): -33%) and EBITDA (94.9 vs 154: -38%).

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

Deferred to /fttcp and Role 1 (OR-30). No destination PE exists (N-L29). Pillar-relevant facts flagged:

| Pillar / input | Fact this quarter | Anchor | Direction |
|---|---|---|---|
| ROCE base (Pillar 1; FTTCP sole authority) | Group ROCE -5% H1 annualised vs 2% FY26; aerospace segment ROCE 22% vs 20%; consumer -25% vs -15% | P-L1200-1213 | Group down; aerospace up |
| Cash multiplier (Pillar 2) | CFO/PAT NM; H1 CFO (80.83); FY26 CFO (98.75) | R-L523; N-L111 | Below the lowest band |
| Growth visibility premium | Order book USD 1,096 Mn +9% QoQ; Hosur commercial FY29; Safran six entities | P-L193-200; P-L240-246 | Visibility up, but earnings timing FY29+ |
| Strategic premium | First serial-production contract above 15 years (Safran A320 wheels) | P-L159-160 | Single-credit rule applies at /fttcp |
| Customer concentration (risk input) | Top 5 customer groups 63% of H1 FY27 revenue; 15 OEM customer groups; no segment split or trend | P-L775-778 (P-A3-24) | ND trend; bounds Pillar 3 and sizing |
| Capital intensity ahead (risk input) | GoK MoU for investment of Rs 28,560 Mn, undated, entity and funding NOT FOUND | P-L560-564 (P-A3-23) | Possible capex beyond any guided envelope |
| UA multiplier | Institutional holding not in this corpus (Notion: filed public institutions 26.17% at 15-Oct, N-L10) | N-L10 | ND this run |
| Sector cap | No reclassification evidence | n/a | Hold |
| Hurdle ratio | CMP Rs 212; EPS negative FY27E and FY28E | brief table | NM; deferred |

---

# SECTION B: CONCALL ANALYSIS (ROLE 5)

Source: ASR machine transcript, management tier, UNVERIFIED. Every number in this section without a filed anchor is ASR-UNVERIFIED.

## STEP 0: PRE-FLIGHT

0A. Notion baseline as in Section A 0A. Previous concall log: not passed (ND 'prior log not passed'). Prior Questions-for-Management table: not passed (ND 'not passed').

0B. Participants

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Manav Paul, EY ("ENY", C-FT30; IR contact list P-R566) | External IR firm, not a broker |
| CMD / Chairman | Aravind Melligeri, Executive Chairman and CEO (C-FT37) | Promoter present; spoke opening and Q&A (C-FT43-120, C-FT326-335) |
| Managing Director | Rajeev Kaul, Co-Founder and MD (C-FT38) | Spoke operations (C-FT122-190) |
| CEO | Same as Chairman | n/a |
| CFO | Reenah Joseph (C-FT38; "Reena") | Presented financials; ASR garbles the name as "Dina"/"Raghuja" (C-FT60, C-FT191); identity INFERRED |
| COO / Other senior | Harish Bang, Deputy CFO (C-FT39) | Answered capex (C-FT364) |
| IR advisor | EY (Diwakar Pingle, Kunal Bhoite, Manav Paul per deck contacts) | External firm |

Yellow flags: none on promoter absence. New CFO on call; introduced by the Chairman (C-FT116). No Reg 30 KMP filing seen in the corpus. Deputy CFO answered a capex question; that is a finance topic, not a yellow flag.

0C. Structure. Call 26-Oct-2026 18:00 IST (C-FT4). Results letter signed 16:09 IST the same day (R-L57): same-day call ("canned"). Duration 3,362 s, about 56 minutes (C-FT4). Q&A from 00:18:38 (C-FT295) to about 00:55:38 (C-FT771): about 37 minutes, 66% of the call. Analysts: 10 named (ledger participants R178-R195). 74-second source gap at C-FT307-308.

0D. Safe harbour: standard forward-looking caveat (C-FT33-35). No new caveat category. Deck safe harbour (slide 3) also standard.

0E. Standard operating business.

## STEP 1: OPENING REMARKS CLAIMS INVENTORY

| # | Claim | Type | Quantified? | Source line |
|---|---|---|---|---|
| 1 | H1 consolidated revenue +50% YoY to Rs 8,046 Mn | Backward | YES | C-FT62-63 |
| 2 | Aerospace +42%; consumer revenue more than doubled (H1) | Backward | YES | C-FT64-65 |
| 3 | Consumer Q2 volume ramp slower than anticipated; qualifications longer, supply chain | Backward | NO | C-FT69-73 |
| 4 | "A shift in the timing, not a change in the underlying opportunity" | Strategic | NO | C-FT74-75 |
| 5 | Recalibrating consumer EBITDA breakeven, earlier indicated Q4 FY27 | Forward Guidance (withdrawn) | YES (old date) / NO (new) | C-FT76-78 |
| 6 | Phase consumer investments in line with ramp and customer schedules | Forward Soft | NO | C-FT83-85 |
| 7 | Order book USD 1.1 bn, up 9% this quarter | Customer/Order | YES | C-FT89-90 |
| 8 | Post-quarter long-term agreement with six Safran entities incl. landing gear for Hosur | Customer/Order | YES (six) | C-FT94-99 |
| 9 | Hosur ground-breaking done | Operational | YES (binary) | C-FT100 |
| 10 | "Winning programs faster than we had planned" | Strategic | NO | C-FT107-108 |
| 11 | Aerospace "on track for the year" | Forward Soft | NO | C-FT111 |
| 12 | CFO Reena Joseph has joined | Operational | YES (binary) | C-FT116 |
| 13 | 238 parts added, 4% sequentially, 5,978 total | Operational | YES | C-FT127-128 |
| 14 | 9 CNC machines added, 229 total | Operational | YES | C-FT134-135 |
| 15 | Aerospace utilisation 69%, India 76% | Operational | YES | C-FT138-139 |
| 16 | Hosur first phase Q4 FY27; commercial production FY29 | Operational | YES (ASR "Q4, 527", "F529") | C-FT149-150 |
| 17 | Toys: existing customer phasing off; ramp with new key customer | Customer/Order | NO | C-FT167-170 |
| 18 | Milestone recalibrated; "Rather than give you a new date today" | Forward Guidance | NO | C-FT179-183 |
| 19 | Q2 revenue Rs 4,091 Mn, +45% YoY, +3% QoQ | Backward | YES | C-FT196 |
| 20 | Aerospace segment EBITDA +24% to Rs 783 Mn, margin about 22% | Backward | YES | C-FT200-201 |
| 21 | "Our consumer business continue to scale. Q2 revenue grew 52% year on year" | Backward | YES (YoY only) | C-FT204-205 |
| 22 | Consumer segment EBITDA loss Rs 401 Mn | Backward | YES | C-FT207 |
| 23 | EBITDA +14% QoQ, "partly supported by other income" (67 to 106 Mn, forex) | Backward | YES | C-FT222-224 |
| 24 | JVs "continued to deliver stable margins and cash flows"; JV-inclusive EBITDA Rs 331 Mn | Backward | YES | C-FT230-232 |
| 25 | H1 YoY: D&A +347 Mn, tax +135 Mn (aero current tax), finance +37 Mn | Backward | YES | C-FT241-249 |
| 26 | Receivables +341 Mn, inventory +1,157 Mn, "both driven by aerospace growth" | Backward | YES | C-FT254-255 |
| 27 | NWC days 136 vs 151; receivable days "268 from 78" (A3: about 68) | Backward | YES (ASR garble) | C-FT255-257 |
| 28 | Borrowings +1,576 Mn; ND/E 0.5 vs 0.2 | Backward | YES | C-FT260-263 |
| 29 | Warrants Rs 6,500 Mn; Rs 3,250 Mn upfront on allotment; balance by end-December next year | Forward Guidance | YES | C-FT264-272 |
| 30 | Amalgamation not approved under fast track "on technical grounds"; evaluating; no material impact on operations | Strategic | NO | C-FT279-285 |
| 31 | Priorities: operating efficiency, "strengthening cash conversion" | Forward Soft | NO | C-FT288-290 |

Diagnostics.
- Quantified 22 of 31 claims (71%). Unquantified 9 (29%). Most quantified claims are backward-looking.
- New vs prior: new are Safran six entities, Hosur dates, warrant upfront terms, the recalibration. Reaffirmed: order book trend, aerospace on track. Prior concall text not passed; full reaffirmation test ND.
- Quietly dropped: the consumer revenue guide (+125-150%, N-L101) and the 45-50% consolidated guide were not restated. The H1 FY28 group PAT breakeven (N-L107) was not mentioned. The Rs 500 Cr consumer capex earmark was not restated in the opening.
- Internal contradiction: "Our consumer business continue to scale" (C-FT204) sits next to a 21% QoQ revenue fall (R-L564) and a wider loss. Also "qualification took longer" (C-FT160) vs "It's not a qualification issue, qualification has happened" (C-FT716).

## STEP 2: FORWARD GUIDANCE EXTRACTION

| Metric | This quarter's guidance | Last quarter's guidance | Two quarters ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth FY27, consolidated | None given; consumer "give us some time and we will come back" (C-FT308-309); aerospace "pretty much on track" (C-FT310), "You're on target" (C-FT378) | 45-50% consolidated; consumer +125-150% (N-L101, NOTION-PRIOR) | ND (prior log not passed) | Withdrawn (consumer) / Maintained, unquantified (aerospace) | LOW |
| Revenue growth FY28 | None | ND | ND | n/a | n/a |
| Long-range | 4-6x growth by 2031 (C-FT328; "5 x" at C-FT756) | ND | ND | Maintained | LOW (inconsistent restatement) |
| EBITDA margin band | None | ND | ND | n/a | n/a |
| Consumer EBITDA breakeven | No date; "Rather than give you a new date today" (C-FT179) | Q4 FY27 (P-L265; C-FT78) | ND | Withdrawn | n/a |
| Consumer breakeven utilisation | About 50% utilisation = EBITDA breakeven (C-FT346, C-FT406) | 40-50% FY27 exit target (N-L107) | ND | Maintained | MEDIUM |
| Consumer PAT positive | FY30 (C-FT409; ASR "fat") | ND | ND | New (ASR) | LOW |
| Order book / pipeline | USD 1,096 Mn (P-L193); execution 5-7 years (C-FT394) | USD 1,004 Mn (MC-L31) | ND | Up 9% | HIGH on level, LOW on timing |
| Capex envelope FY27 | "Much lesser" than Rs 660 Cr; H1 about Rs 160 Cr, H2 "almost equal" (C-FT365-368) | Rs 660 Cr, about Rs 500 Cr consumer (MC-L30) | ND | Lowered (about Rs 320 Cr implied) | MEDIUM |
| Capex beyond FY27 | Not guided on the call. Deck shows a GoK MoU "for investment of Rs 28,560 Mn", undated, entity and phasing NOT FOUND (P-L560-564) | ND | ND | New (deck only) | LOW |
| Utilisation target / timeline | 40-50% (C-FT344) | 40-50% FY27 exit (N-L107) | ND | Maintained (vs 17% actual) | LOW |
| Strategic execution: Hosur | Investment Phase 1 from Q4 FY27; commercial production FY29 (P-L240-246 per errata; C-FT149-150) | ND | ND | New | MEDIUM (labelled "indicative") |
| Working capital / CCC | Inventory to about 120 days; normalising about Q1 FY28 (C-FT541-543) | ND | ND | New | MEDIUM |
| Net debt / funding | Warrants Rs 650 Cr (Rs 325 Cr upfront; balance only on conversion, "proposed", R-L274-275); "over 800 crore term loans"; FY28 capital raise "may be required" (C-FT269-272, C-FT767, C-FT334-335) | FY28 external equity raise (C-FT321, analyst recall) | ND | Widened (more funding sources) | MEDIUM |
| Segment: toys | Old customer phases out this quarter; new customer "almost completely" by Q4 (C-FT494-504) | ND | ND | New | MEDIUM |
| New contract milestones | Safran-related new capabilities commercialise FY29 (C-FT458) | Safran deliveries FY28 (MC-L31) | ND | Pushed out for the new scope; wheels date not restated | LOW |
| Warrant use of proceeds | Rs 289 Cr capex; Rs 100 Cr WC; Rs 100 Cr JV and strategic; balance GCP (C-FT760-765) | ND | ND | New | HIGH (ASR) |
| Dividend / payout | None | ND | ND | n/a | n/a |

Diagnostics.
- Guidance widened. The consumer date was withdrawn. The consumer and consolidated revenue guides were not restated.
- Prior guidance dropped: the consumer revenue guide and the H1 FY28 group PAT breakeven were not acknowledged. The Q4 FY27 breakeven withdrawal was acknowledged explicitly.
- Internal consistency fails. A 40-50% utilisation target "still remains" (C-FT344) while utilisation fell to 17% and the breakeven date was withdrawn. Funding (Rs 650 Cr warrants plus over Rs 800 Cr term loans plus a possible FY28 raise) far exceeds FY27 capex of about Rs 320 Cr (C-A3-10). Rs 161 Cr of the warrant money has no named use (C-A3-11).
- Two qualifiers bound that funding reading. First, the Rs 650 Cr assumes conversion. Only Rs 325 Cr is due on allotment, and the balance is a promoter option while CMP sits below Rs 231.55 (6C-bis; R-L274-275). Second, the deck shows a GoK MoU for investment of Rs 28,560 Mn (Rs 2,856 Cr) (P-L560-562; P-A3-23). It has no date, investing entity, site, phasing or funding source on the deck. It equals 2.05x Sep-26 total equity and 17.9x H1 capex (P-A3-23). If Aequs funds a material share itself, the stated funding stack does not cover it; if partners or the state fund it, it is an ecosystem headline, not Aequs capex. Conservative reading: an unfunded intent until phasing and source are stated. Separating observation: a phased schedule naming the investing entity and the funding source.
- Against the Notion projections: FY27 revenue and EBITDA guidance absent; the run-rate sits below base on revenue and EBITDA, between bear and base on PAT.
- Refused: FY27 revenue and EBITDA numbers (C-FT308-309, C-FT377-378), FY27-29 revenue ballpark (C-FT755-757), consumer breakeven revenue (C-FT519-521), loss split by sub-line (C-FT529-530), titanium volume (C-FT659-661), CE material (C-FT625).

## STEP 3: PROMISE VS DELIVERY AUDIT

3A-3E: ND 'prior log not passed'. No credibility ratio is computed.

Informational only, unscored: commitments recorded in Notion and tested by this quarter.

| Commitment on record | Source | This quarter | Status if scored later |
|---|---|---|---|
| Consumer EBITDA breakeven Q4 FY27 | N-L107; P-L265 | Withdrawn with acknowledgment, no new date (C-FT179) | DELAYED (first delay, no new date) |
| Consumer utilisation 40-50% FY27 exit | N-L107 | 17% in Q2 (P-L184); target reiterated (C-FT344) | UNCLEAR until Q4 FY27 |
| FY27 capex Rs 660 Cr, about 500 consumer | MC-L30 | Cut, acknowledged (C-FT368) | n/a (revision, acknowledged) |
| Amalgamation of three WOS | N-L121 | Rejected by RD; "evaluating" (R-L265-268) | DELAYED |
| Consumer revenue guide +125-150% | N-L101 | Not restated | Candidate DROPPED (no acknowledgment) |
| H1 FY28 group PAT breakeven | N-L107 | Not mentioned | Candidate DROPPED (no acknowledgment) |

Two candidate DROPPED items sit in this quarter. If the prior log confirms them as quantified commitments, the 3B rule (two DROPPEDs in the trailing four concalls) triggers an automatic one-grade downgrade. Flag for the operator.

3E. Prior-quarter questions: ND 'not passed'.

## STEP 4: Q&A DECOMPOSITION

### 4A. Q&A inventory

| # | Analyst and firm | Question (1 line) | Category | Response grade | Substance |
|---|---|---|---|---|---|
| 1 | Renu Bates, IIFL ("IFL Capital") | CE yield and failure rate; revised FY27 revenue and EBITDA guidance by segment (C-FT301-305) | Forward Guidance | D (consumer) / C (aerospace) | "Give us some time and we will come back"; aerospace "pretty much on track" (C-FT308-311). Source gap removed part of the answer |
| 2 | Renu Bates | Is the FY28 external equity raise still needed after the warrants? (C-FT320-325) | Financial | B | "Significant capital requirement"; FY28 raise "may be required" for 2031 (C-FT326-335) |
| 3 | Deepak, Kotak | Consumer scenarios; year-end utilisation target; still spend Rs 500 Cr? (C-FT338-342) | Forward Guidance | B | 40-50%, "around 50 percent" (C-FT344-346); capex recalibrated, larger share to aerospace (C-FT347-350) |
| 4 | Deepak | Overall FY27 capex (C-FT357-363) | Financial | A | H1 about Rs 160 Cr, H2 almost equal; 660 "much lesser"; no consumer capital unless utilisation rises (C-FT365-373) |
| 5 | Deepak | Consumer scenarios, again (C-FT354-356) | Forward Guidance | D | "Take some time to come back" (C-FT374-376) |
| 6 | Deepak | Aerospace revenue and EBITDA guidance (C-FT377) | Forward Guidance | C | "You're on target" (C-FT378), no number |
| 7 | Akash Sengri, ICICI Securities | Why aerospace EBITDA lags revenue (C-FT381-384) | Financial | B | Higher other income share last year; SG&A; titanium content (C-FT386-393) |
| 8 | Akash Sengri | Order book execution timing (C-FT384-385, C-FT397-399) | Customer/Order | B | 5-7 years typical; one 15-year contract (C-FT394-396, C-FT400-403) |
| 9 | Akash Sengri | Consumer breakeven utilisation (C-FT404-407) | Financial | B | About 50%; consumer PAT positive FY30 (C-FT406-410; ASR) |
| 10 | Gaurav Naguri, Avendus | Real bottleneck; utilisation 22% to 17% (C-FT415-422) | Operational | B | Product-update qualification, in-house capability, toy supply chain, weather logistics (C-FT425-435) |
| 11 | Gaurav Naguri | OEM pressure or business risk if ramp lags (C-FT422-425) | Customer/Order | C | Customer demand intact; "working with us" (C-FT436-444) |
| 12 | Gaurav Naguri | Are new Safran orders outside the order book? (C-FT447-452) | Customer/Order | C | New capabilities, Hosur, commercialisation FY29; inclusion not answered (C-FT453-458) |
| 13 | Gaurav Naguri | Hosur land and JV partners (C-FT461-469) | Strategic | B | Replicate Belagavi with JV partners (C-FT470-474) |
| 14 | Analyst, Nomura ("Noma") | When old toy customer reaches zero and new customer offsets (C-FT481-493) | Customer/Order | B | Old customer phases out this quarter; new customer Q3 onwards, Q4 "almost completely" (C-FT494-504) |
| 15 | Priyanka Biswas, GM Financial | Consumer breakeven sales level in Rs Mn; fixed-cost share (C-FT511-516) | Financial | D | "We don't really have not evaluated that", come back via Harish (C-FT517-521) |
| 16 | Priyanka Biswas | Loss split ATP vs toys (C-FT523-527) | Financial | C | "Majority is attributable to the ATP" (C-FT529-530), no number |
| 17 | Priyanka Biswas | Inventory unwind timeline (C-FT531-536) | Financial | B | 6-9 months; about Q1 FY28; about 120 days (C-FT537-545) |
| 18 | Priyanka Biswas | Air freight availability (C-FT546-547) | Operational | C | "New normal", some cost increase (C-FT548-551) |
| 19 | Sanitya, Unicorn Assets | Why qualification cycles were not anticipated (C-FT554-568) | Operational | C | Learning curve; recalibrate and come back (C-FT570-590) |
| 20 | Sanitya | Customer shift to additive manufacturing (C-FT593-597, C-FT608-616) | Strategic | C | "We don't believe so"; not adding the capability (C-FT598-607, C-FT617-620) |
| 21 | Sanitya | CE material (C-FT621-624) | Operational | E | "I can't talk about that" (C-FT625) |
| 22 | Analyst, Ashika group | Titanium consumption run-rate (C-FT634-645) | Operational | C | "I don't have that segregation"; among largest buyers (C-FT658-662) |
| 23 | Analyst, Ashika group | Why consumer hits group EBITDA; aero EBITDA slower than revenue (C-FT646-657) | Financial | B | Consumer capital about equal to aerospace; no pricing pressure; pass-through; SG&A build (C-FT680-704) |
| 24 | Analyst, Ashika group | Titanium source; margin impact of more titanium (C-FT705-712) | Operational | B | Aerospace grade; "it should not" hurt margin (C-FT707-712) |
| 25 | Suraj Malu, Kathmaran | Steps to speed CE qualification (C-FT714-724) | Operational | C | "It's not a qualification issue, qualification has happened" (C-FT716) |
| 26 | Amitajit Yadav, KJMC | Consumer delay or structural; breakeven revenue and utilisation; cash before breakeven (C-FT729-735) | Financial | C | Fixed cost base; volume fell; rest temporary (C-FT741-750); no breakeven or cash number |
| 27 | Amitajit Yadav | FY27-29 revenue ballpark (C-FT736-738, C-FT755-756) | Forward Guidance | D | "We have guided 2031 ... 5 x" (C-FT756-757) |
| 28 | Amitajit Yadav | Use of the Rs 650 Cr (C-FT739-740, C-FT757-760) | Financial | A | 289 capex; 100 WC; 100 JV and strategic; balance GCP; over Rs 800 Cr term loans (C-FT760-767) |

Grade count: A 2, B 11, C 11, D 4, E 1 (on 29 graded responses; row 1 counts twice, D for consumer and C for aerospace). C-or-worse share: 16 of 29 (55%).

### 4B. Question pattern analysis
- Most repeated: consumer breakeven (Deepak, Akash, Priyanka, Amitajit: 4 analysts) and consumer scenarios (Renu, Deepak). The market does not trust the first answer.
- Topic management did not want to discuss: consumer quantification. Every consumer number request (breakeven revenue, loss split, scenarios, year-end landing, cash burn) graded C or D.
- Buy-side vs sell-side: sell-side 6 (IIFL, Kotak, ICICI Securities, Avendus, Nomura, KJMC); buy-side or other 4 (Unicorn Assets, GM Financial, Ashika, Kathmaran). Buy-side present.
- No hosting broker. The first question (IIFL) was substantive.
- Pushback: Ashika analyst ("I still feel ... it's still not answered", C-FT650-652); Sanitya on additive (C-FT608-610); Amitajit "delay or structural" (C-FT730).

### 4C. Three most important exchanges

Exchange 15 (consumer breakeven sales level).
- Question: "at what consumer sales level, let's say in rupee million terms that you can probably achieve let's say an EBITDA break event ... what is the extent of fixed or semi fixed cost" (C-FT512-515).
- Response: "the consolidated basis of revenue, we don't really have not evaluated that, maybe we'll have to come back to separately on that, maybe you should connect with the Harish" (C-FT519-521).
- Said: consumer is assessed sub-line by sub-line.
- Not said: any breakeven revenue, any fixed-cost number, any date.
- Implication: management has no stated breakeven revenue for a segment losing Rs 40 Cr a quarter. The falsification line fired and no recovery path is quantified.
- Follow-up: "What quarterly consumer revenue in Rs Mn takes segment EBITDA to zero at today's cost base?"

Exchange 4 plus 28 plus 2 (capex and funding).
- Question: overall FY27 capex (C-FT357-363); use of the Rs 650 Cr (C-FT739-740); FY28 raise (C-FT320-325).
- Response: "first half of the year, we have done about 160 crores of CapEx ... our initial guidance what we had given 660 crores, we may end up doing much lesser than that" (C-FT365-368); "about 289 crores ... capital expenditure ... about 100 crores ... working capital ... another 100 crores towards JV investments ... Balance would be general corporate" (C-FT761-765); "We are going to do over 800 crore term loans" (C-FT767); "our 28 we still see the potential capital rates that may be required" (C-FT334-335).
- Said: FY27 capex about Rs 320 Cr; a large funding stack.
- Not said: the post-FY27 capex envelope; the use of the Rs 161 Cr balance; term-loan sanction and timing; the GoK MoU for Rs 28,560 Mn shown in the deck (P-L560-562), its period and the Aequs share; that the warrant balance depends on conversion.
- Implication: funding sized for an unguided FY28-29 Hosur build. Leverage and dilution risk rise ahead of any Hosur revenue (FY29). The GoK MoU could add a further capital call that no stated source covers.
- Follow-up: "What is the FY28 and FY29 capex envelope for Hosur Phase 1, and how much of the GoK MoU is Aequs capex?"

Exchange 7 plus 23 (aerospace EBITDA lag).
- Question: "revenue jump had been much higher than the EBITDA" (C-FT381-382); "it's still not answered because 86% of your revenues actually aerospace" (C-FT650-653).
- Response: "the highering other income share right in the previous year was higher and also this year we have added the HDA cost" (C-FT388-389); "There is no pricing pressure because it's a long-term contract. Our materials are passed through" (C-FT692-694).
- Said: segment EBITDA carries other income; SG&A build; titanium content.
- Not said: aerospace margin ex other income; the OI allocation.
- Implication: monitorable 2 cannot clear on disclosed data. The aerospace leg holds on reported numbers only.
- Follow-up: "What was aerospace segment EBITDA margin excluding other income in Q1 and Q2 FY27?"

## STEP 5: NEW INFORMATION AUDIT

### 5A. New disclosures

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| FY27 capex about Rs 320 Cr vs Rs 660 Cr guide (C-FT365-368) | New capex | YES | Spear fact 2 superseded; less consumer capex; less FY28 D&A from consumer |
| Warrant use 289 / 100 / 100 / balance (C-FT760-765) | New capex / funding | YES | WC and JV uses confirm loss-funding role; split assumes full Rs 650 Cr |
| Over Rs 800 Cr term loans (C-FT767) | New capex / funding | YES | Leverage rises; finance cost rises |
| FY28 external raise still possible (C-FT334-335) | Forward catalyst | YES | Further dilution risk |
| About 50% utilisation = consumer EBITDA breakeven (C-FT406) | New capability metric | YES | Gap from 17% is about 33 pp |
| Consumer PAT positive FY30 (C-FT409; ASR) | Forward catalyst | YES | Consumer drag through FY29 |
| Majority of consumer loss in ATP (CE) (C-FT529-530) | Negative surprise | YES | The CE plant, not toys, drives the loss |
| Toy customer transition timeline Q3-Q4 (C-FT494-504) | Customer | YES | Q3 overlap gap on a fixed cost base |
| Inventory target about 120 days by about Q1 FY28 (C-FT541-543) | Forward catalyst | YES | Testable WC commitment |
| Hosur Phase 1 Q4 FY27; commercial FY29 (C-FT149-150) | New capex / plant | YES | No Hosur earnings before FY29 |
| Safran new scope commercialises FY29 (C-FT458) | Customer | YES | Spear fact 4 FY28 delivery not reconfirmed |
| CFO joined (C-FT116) | New senior management | NO (known from deck) | Monitorable 7 partial |
| Consumer capital deployed about equal to aerospace (C-FT683-684) | Negative surprise | YES | Consumer segment assets 1,247.80 vs aerospace 1,500.09 (R-L590-591) confirm the scale |

### 5B. What was NOT discussed

| Expected topic | Why it should have been discussed | Significance of silence |
|---|---|---|
| H1 FY28 group PAT breakeven (N-L107) | Rested on the withdrawn consumer date | AMBER to RED (thesis-relevant; prior guidance) |
| Aerospace margin ex other income | Monitorable 2; analyst pressed twice | AMBER |
| Operating cash flow figure | Monitorable 5; CFO (80.83) in filing | AMBER ("This is also reflected in our cash flow", C-FT259, with no number) |
| DTA on merged losses / tax drag size | Monitorable 6; H1 tax 24.77 Cr on a loss | AMBER |
| Amalgamation route (S.233 refile or NCLT S.232) and appointed date | Tracker item; rejection 12-Oct | AMBER |
| Promoter pledge and warrant funding source; conversion intent below the issue price | Proposed tripwire; balance is optional at CMP | AMBER |
| GoK MoU Rs 28,560 Mn (P-L560-562) | Deck headline with no period, entity or funding; analysts asked about capex and funding | AMBER |
| Top-5 customer concentration 63% (P-L775-777) | Deck metric; no segment split or trend | AMBER |
| Safran award value | Tracker item | AMBER |
| IPO lock-in expiry about Dec-2026 and institutional holding | Tracker item | Routine to AMBER |
| Aequs Cookware JV Rs 30.05 Cr receivable | Tracker item; due about now (N-L134) | AMBER |
| Consumer asset impairment test | Consumer segment assets Rs 1,247.80 Cr at 17% utilisation (R-L591) | RED (FY27 audit exposure) |
| Unnamed subsidiary under other auditor | LRR para 6 (R-L753-766) | AMBER |
| Hasbro by name | Open integrity ruling (N-L76-84) | AMBER (the old customer is unnamed on the call) |
| MOA medical-instruments clause | Flagged as a Q2 call question (N-L123) | Routine |
| Labour Court cases against ASMIPL (a ground for the S.233 rejection; N-L10 Key Notes 14-Oct) | Bears on the refile route | AMBER |
| 74-second source gap (C-FT307-308) | Part of the FY27 guidance answer lost | Not counted as silence |

## STEP 6: TONE AND SPECIFICITY

### 6A. Tone comparison (prior concall text not passed; prior phrasing from Notion where recorded)

| Topic | Prior phrase | This concall phrase | Direction |
|---|---|---|---|
| Consumer breakeven | "Q4 FY27" (N-L107; P-L265) | "recalibrating ... Rather than give you a new date today" (C-FT179) | DOWNGRADED |
| Consumer revenue guide | "+125 to 150%" (N-L101) | "give us some time and we will come back" (C-FT308-309) | DROPPED |
| Consumer utilisation target | "40 to 50% FY27 exit" (N-L107) | "heading 40 to 50 percent so that still remains" (C-FT344) | MAINTAINED (against 17%) |
| Capex | Rs 660 Cr (MC-L30) | "may end up doing much lesser" (C-FT368) | LOWERED |
| Aerospace wins | "winning programmes faster than planned" (N-L17) | "accelerating faster than what we anticipated" (C-FT332-333) | MAINTAINED |
| Amalgamation | Postal ballot passed; CAA-11 pending (N-L121) | "not approved under the fast-track route on technical grounds" (C-FT281-282) | DOWNGRADED |
| Consumer framing | n/a | "timing ... not a change in the underlying opportunity" (C-FT74-75) | New hedge |

### 6B. Specificity score (A4 classification of distinct forward statements, deduplicated)
- Quantified forward statements: 16 (Hosur Q4 FY27; Hosur FY29; 40-50% target; 50% breakeven; H2 capex about H1; capex below 660; Rs 325 Cr upfront and Dec-2027 balance; 4-6x by 2031; 5-7 year execution; Safran scope FY29; toy transition Q3-Q4; inventory 120 days by about Q1 FY28; consumer PAT FY30; warrant use split; over Rs 800 Cr term loans; 12-18 month deployment). Backward items (order book +9%, six Safran entities) excluded.
- Unquantified forward statements: 16 (breakeven recalibration; come back on year-end landing; aerospace on track/on target; phase investments to ramp; invest behind aerospace demand; larger share to aerospace; no consumer capital until utilisation rises; scenarios to come; breakeven revenue to come; keep you updated; strengthen cash conversion; replicate Belagavi with JV partners; titanium pass-through; customer working with us; learning curve improves; not adding additive capability).
- Specificity ratio: 16 / 32 = 0.50. Excluding three ASR-garbled items (Q4 "527", "F529", "fat" FY30): 13 / 29 = 0.45. Reading: 0.45 to 0.50, moderate specificity (0.3-0.5 band), at its upper edge.

### 6C. Defensive language count
"come back" x4 (C-FT309, C-FT375, C-FT520, C-FT588-589); "Rather than give you a new date today" x1 (C-FT179); "we don't really have not evaluated that" x1 (C-FT519-520); "I don't have that segregation" x1 (C-FT659); "can't dispose" (disclose) x1 (C-FT660-661); "I can't talk about that" x1 (C-FT625). Total 9. Above 5: hedge-heavy call. Prior count: ND.

### 6D. Confidence indicators
Named milestones with dates (Hosur Q4 FY27 and FY29; toy transition Q4; inventory Q1 FY28). Specific funding split (warrant use). Explicit acknowledgment of the missed breakeven, but no recovery timeline. Promoter answered strategic and funding questions directly (C-FT326-335).

### 6E. Management archetype
Specificity 0.45 to 0.50 (at or below 0.5). Credibility ratio: ND (prior log not passed). Archetype: NOT CLASSIFIABLE this run. Watch: if the prior log yields a ratio below 60%, specificity at or below 0.5 places management in the EVASIVE quadrant; the two candidate DROPPEDs add to that risk. At 60% or above it would read MEASURED & CREDIBLE.

## STEP 7: CROSS-REFERENCE

### 7A. Concall narrative vs filing

| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| Q2 net loss Rs 522 Mn, "broadly stable" vs 532 (C-FT237-238) | Continuing PAT (521.96) vs (532.28); total (523.92) (R-L394, R-L398) | CONFIRMED |
| EBITDA +14% QoQ, "partly supported by other income" (C-FT222-224) | Op EBITDA ex OI fell 147.64 to 138.55 Mn (-6.2%) (R-L376, R-L384) | PARTIALLY CONFIRMED: "partly" understates; all of the rise is OI |
| "Our consumer business continue to scale" (C-FT204) | Consumer revenue 733.86 to 576.68 Mn, -21.4% QoQ (R-L564) | CONTRADICTED on QoQ |
| Receivables +341 Mn, inventory +1,157 Mn (C-FT254) | +341.42 and +1,157.45 Mn (R-L445-446) | CONFIRMED on amounts; "driven by aerospace growth" UNVERIFIABLE (no segment WC split) |
| Borrowings +1,576 Mn (C-FT260-261) | 5,611.90 less 4,035.78 = 1,576.12 Mn (R-L460, R-L467) | CONFIRMED |
| ND/E 0.5 vs 0.2 (C-FT262) | 0.46 vs 0.23 incl. leases; 0.26 vs 0.03 ex leases | CONFIRMED only on a lease-inclusive basis (definition not stated) |
| Tax +135 Mn on aero current tax (C-FT245-247) | 247.68 less 112.67 = 135.01 Mn (R-L393) | CONFIRMED on amount |
| D&A +347 Mn; finance +37 Mn (C-FT242, C-FT248) | +347.19; +36.98 Mn (R-L386, R-L385) | CONFIRMED |
| JVs "stable margins" (C-FT230) | JV share of profit 29.02 to 18.11 Mn QoQ (-37.6%) (R-L388) | CONTRADICTED (JV profit share fell) |
| Amalgamation "no material impact on ongoing business operations" (C-FT284-285) | Note wording identical (R-L268-270); group ETR -30.7% H1 (R-L390, R-L393); tax on a loss also in Q2 FY26 and FY26, before the scheme (R-L393, R-L263) | PARTIALLY CONFIRMED: true for operations; the tax drag predates the scheme and the blocked merger leaves one offset route closed |
| Warrants "Rs 3,250 Mn payable upfront ... balance ... going to be paid by end of December next year" (C-FT269-272) | Filed: "proposed to be converted on or before December 31, 2027" (R-L274-275) | PARTIALLY CONFIRMED: date matches; the filing does not commit the balance |
| "Strengthening cash conversion" (C-FT289) | H1 CFO (808.31) Mn (R-L523) | CONTRADICTED |
| Consumer capital about equal to aerospace (C-FT683-684) | Segment assets 12,477.95 vs 15,000.89 Mn (R-L590-591) | CONFIRMED (consumer 45% of segment assets) |
| No pricing pressure; materials pass-through (C-FT692-694) | Aerospace segment margin 22.3% vs 25.9% YoY (R-L563, R-L566) | UNVERIFIABLE (mix, OI share and SG&A also moved) |
| Aerospace utilisation 69%, India 76% (C-FT138-139) | Deck 69%, India 76% (P-L184-187) | CONFIRMED (deck, management tier) |
| Cash balance Rs 1,710 Mn "closed the year" (C-FT260) | 1,709.70 Mn at 30-Sep (R-L447) | CONFIRMED (ASR says "year" for half-year) |

### 7B. Peer concall cross-check
UNVERIFIABLE this run (peer concalls not passed). Prior Notion context only: AZAD and UNIMECH post blended margins in the 30s vs Aequs 20-27% (N-L45; NOTION-PRIOR, tier SECONDARY).

### 7C. External channel checks
UNVERIFIABLE this run. Notion carries CARE BBB-;Stable on Rs 25 Cr of facilities, unfetched (N-L130).

## STEP 8: THESIS AND POSITION UPDATE

8A. Growth trigger status: as Section A 6D. Concall moves: consumer CE ramp WEAKENED (no breakeven revenue, majority of loss in ATP); toy replacement DELAYED; Hosur ON TRACK (FY29).

8B. Concall-specific watchlist rows

| # | Watchlist item | This concall reading | Status |
|---|---|---|---|
| 1 | Consumer utilisation | No management Q2 figure; analyst "22 to 17%" undisputed (C-FT416, ASR); target 40-50% reiterated | RED |
| 2 | Aerospace margin ex OI | Not given; segment margin carries OI (C-FT388) | RED (page method) |
| 3 | Consumer capex | Phased down; no capital until utilisation rises (C-FT372) | GREEN |
| 4 | Part numbers | 238 (C-FT127) | GREEN |
| 5 | OCF vs capex | No number given (C-FT259) | RED (filing) |
| 6 | DTA on merged losses | Not discussed | UNKNOWN |
| 7 | CFO seat | CFO joined (C-FT116); filing not referenced | AMBER |

8C. Thesis-broken check (concall): the falsification line is FIRED on filed evidence (Section A 6C). The concall adds an undisputed analyst reading of 17% and no management rebuttal. No other condition on file.

8D. Four-pillar concall adjustments: deferred to /fttcp and Role 1 (OR-30). Pillar-relevant facts flagged:
- Pillar 1 / FTTCP ROCE: consumer capital "as much as our aerospace" (C-FT683-684) at negative returns; FY27 capex cut to about Rs 320 Cr (C-FT365-368); GoK MoU Rs 28,560 Mn undated (P-L560-562).
- Pillar 2: WC framed as aerospace growth (C-FT254-255); inventory target 120 days by about Q1 FY28 (C-FT541-543); no OCF number.
- Pillar 3 (EM): Safran six entities; Hosur FY29; not adding additive capability (C-FT617-620); top 5 customer groups 63% of H1 revenue (P-L775-777).
- Strategic premium: 15-year serial contract; single-credit rule applies.

8E. Position decision. Decision Status verified NOT SET; non-held name; branch 8A-W.
- Thesis-broken FIRED: the protocol's mechanical output is "reclassify to AVOID; record what would need to reverse". FLAG ONLY. Not a recommendation. The operator decides.
- Concall overrides: credibility ratio ND, so the below-60% rule cannot be tested. Two candidate DROPPED items (consumer revenue guide; H1 FY28 group PAT breakeven) are flagged for the prior-log check. No undisclosed material risk beyond the filing. Narrative contradicts filing on consumer "scale", JV "stable" and "cash conversion": trust the filing; note the credibility issue; tighten the next-quarter watchlist.
- Add-back/trim triggers: none on file (no position, no entry zone). Refinement: none possible without a signed model.

8C (Role 4). Single cleanest metric for Q3 FY27: consumer segment revenue in the filed segment table.
- Bull threshold: at or above Rs 73.4 Cr (Q1 FY27 level, R-L564), with a named breakeven quarter.
- Bear threshold: below Rs 57.7 Cr (Q2 FY27, R-L564), or a consumer segment EBITDA loss wider than Rs (40.1) Cr.
- Between: ambiguous; read with utilisation (deck) and the toy transition status.

8F. Updated questions for the next review: the QfM register below is the forward list.

---

# QUESTIONS FOR MANAGEMENT (Role 4 Step 8.5 and Role 5 Step 8F, merged)

Ordered by importance within the original 40; rows 41-44 are loop 1 additions. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one row (mapping column).

| # | Question | Cat | Why it matters | Bull answer | Bear answer | From finding IDs |
|---|---|---|---|---|---|---|
| 1 | Which quarter is the new consumer EBITDA breakeven target, given a Q2 consumer segment loss of Rs 401 Mn at 17% utilisation? | B | Falsification line fired; the date fed H1 FY28 group PAT breakeven | A named quarter within FY28 with a utilisation path | No date again at Q3 | C-A3-01, P-A3-03, P-A3-05, PR-A3-03, PR-A3-04, C-A3-17 |
| 2 | What quarterly consumer revenue in Rs Mn gives segment EBITDA breakeven at today's cost base? | C | Management says about 50% utilisation is breakeven but has "not evaluated" revenue | A number near 2x Q2 revenue with a fixed-cost split | "Not evaluated" again | C-A3-03, C-A3-04, C-A3-17, R-A3-18 |
| 3 | Of the Rs 157 Mn QoQ fall in consumer revenue (734 to 577), how much came from toys and how much from consumer electronics? | A | Separates a one-time toy customer swap from a CE plant problem | Mostly toys (transition) | Mostly CE | P-A3-10, P-A3-16, PR-A3-02, C-A3-24, R-A3-18 |
| 4 | Was the 900 bps YoY change in consumer utilisation a decline, and is the 17% on the same basis (incl. subsidiaries and JVs) as the 22% Q1 figure? | A | Basis of the falsification line's utilisation leg | Same basis; decline confirmed and explained | Basis changed between quarters | P-A3-20, R-A3-18 |
| 5 | Has the company tested consumer assets (segment assets Rs 12,478 Mn) for impairment at 30-Sep-2026, and what headroom did the test show? | D | Any FY27 audit impairment lands on the exceptional line | Test done, headroom stated | No test, or headroom thin | R-A3-02 |
| 6 | What H1 FY27 loss did AEPPL and AFCPPL each post? | D | Subsidiary losses (plus eliminations) rose to Rs 559.9 Mn in Q2 from 228.6 Mn | Losses concentrated and falling | Broad and rising | R-A3-07 |
| 7 | Will the old toy customer have zero revenue in Q4 FY27, and what share of Q3 toy revenue will the new key customer provide? | E | Q3 overlap gap on a fixed cost base | New customer above half of Q3 toy revenue | Gap widens the Q3 loss | C-A3-16 |
| 8 | Is the consumer electronics customer moving any current part to additive manufacturing before FY29, yes or no? | E | Technology obsolescence risk on the CE capacity | No | Yes, or refusal | C-A3-20 |
| 9 | How much of Q2 other income of Rs 106 Mn is forex gain? | C | All of the QoQ EBITDA rise is other income | Small forex share | Most of it forex | P-A3-15, C-A3-05, PR-A3-05 |
| 10 | What is aerospace segment EBITDA margin excluding other income for Q1 and Q2 FY27? | C | Monitorable 2 needs two clean quarters at or above 20% | At or above 20% both quarters | Below 20% in Q2 | P-A3-12, C-A3-07, PR-A3-05, PR-A3-10, R-A3-19 |
| 11 | Does rising titanium content lower the aerospace EBITDA margin percentage in FY27, yes or no? | C | Two management answers conflict | No, with evidence | Yes | C-A3-08 |
| 12 | What does the Q2 segment-results elimination of Rs 104.2 Mn (Rs 46.7 Mn a year ago) consist of? | C | Eliminations plus unallocated took Rs 137 Mn off segment EBITDA | Inter-segment margin, will reverse | Recurring cost | C-A3-06, PR-A3-10, P-A3-13 |
| 13 | Which P&L lines hold the H1 non-cash gains (inventory-provision reversal Rs 83.7 Mn, write-backs Rs 20.7 Mn, lease derecognition Rs 13.1 Mn, disposal gain Rs 6.6 Mn), and will any recur in H2? | D | 27% of H1 EBITDA | Mostly in other income, non-recurring and disclosed | Inside operating lines, overstating core EBITDA | R-A3-08 |
| 14 | Which facility's lease was derecognised for the Rs 13.1 Mn gain, and in which segment? | D | Possible consumer footprint cut | Aerospace relocation | Consumer exit | R-A3-06 |
| 15 | What FY27 tax charge does the company expect while the amalgamation is pending? | D | H1 tax Rs 247.7 Mn on a Rs 806.6 Mn pre-tax loss | Lower in H2; route fixed soon | Same or rising drag | R-A3-15, P-A3-06, C-A3-12 |
| 16 | Will the company refile under S.233 or apply to NCLT under S.232, and by which date? | G | Tax shelter and DTA depend on it; board took no route decision on 26-Oct | Route and filing date named | "Evaluating" again at Q3 | R-A3-13, R-A3-14, C-A3-14, R-A3-23 |
| 17 | What is the source of the parent's low current tax (Rs 0.11 Mn in Q2 after Rs 11.75 Mn in Q1), and when does it expire? | D | Parent ETR 12.3% H1 vs 25.17% statutory | Known SEZ deduction with a long tail | Expiring shield | R-A3-16 |
| 18 | On what date will the Rs 3,250 Mn warrant upfront be received, and is any of it funded by the 360 One Prime facility? | F/G | Bridges net debt +Rs 3,144 Mn; tests the proposed pledge tripwire | Received after approval, own funds | Funded by the pledge facility, or delayed | R-A3-12, P-A3-04, P-A3-07, PR-A3-07, P-A3-01, P-A3-09 |
| 19 | What does the unallocated Rs 161 Cr of the warrant money fund? | F | No named use for about 25% | Named project | General corporate purposes only | C-A3-11, PR-A3-08 |
| 20 | What is the sanctioned amount, lender and drawdown schedule of the "over Rs 800 Cr" term loans? | F | Finance cost and leverage path | Sanctioned, phased to capex | Undrawn plan, rate unknown | C-A3-10, R-A3-19, P-A3-09 |
| 21 | What is the Hosur Phase 1 capex envelope for FY28 and FY29? | F | Funding outruns FY27 capex; Hosur earns from FY29 | Envelope and phasing given | Not given | C-A3-09, C-A3-18, P-A3-02, PR-A3-12, PR-A3-15 |
| 22 | Is an FY28 external equity raise planned, yes or no? | F | Dilution on top of warrants | No | Yes, size open | C-A3-10 |
| 23 | What amount of parent guarantees for subsidiary borrowings was outstanding at 30-Sep-2026, and which subsidiaries do they cover? | D | Parent other NC financial liabilities +Rs 190 Mn; parent income relies on guarantee fees | Small, aerospace subsidiaries | Large, consumer subsidiaries | R-A3-10 |
| 24 | Which subsidiary loan carried the Rs 173.4 Mn impairment in H1 FY26, why did FY26 net to nil, and what test covers the Rs 2,096 Mn related-party loans? | D | Recoverability of parent loans to loss-making subsidiaries | Aerospace subsidiary, cured | Consumer subsidiary, recurring | R-A3-03 |
| 25 | Which JV or associate received the Rs 93.0 Mn invested in H1, and has the Aequs Cookware Rs 30.05 Cr receivable been collected? | E/F | Cash into JVs while consumer JV losses doubled | Aerospace JV; receivable collected | Consumer JV; receivable rolled | R-A3-11 |
| 26 | Which JV drove the fall in JV profit share from Rs 29.0 Mn to Rs 18.1 Mn QoQ? | E | Contradicts "stable margins" | One-off at one JV | Broad margin decline | C-A3-15, PR-A3-09, R-A3-11 |
| 27 | Does the USD 1,096 Mn order book include the post-quarter Safran agreements, yes or no, and what is their value? | E | Visibility claim and spear fact 4 | Excluded, value stated | Included, value withheld | P-A3-22, PR-A3-13, C-A3-18 |
| 28 | In which fiscal year do Safran A320 wheels serial deliveries start? | B | Spear fact 4 says FY28; call says new scope FY29 | FY28 | FY29 or later | C-A3-18 |
| 29 | What drove the 61% fall in current contract liabilities (Rs 338 Mn to Rs 133 Mn), and in which segment? | D | Advance-backed order intake may be slowing | Delivery against old advances | New advances drying up | R-A3-21 |
| 30 | How much of the YoY fall in aerospace segment liabilities (Rs 7,455 Mn to Rs 5,582 Mn) was debt repayment? | D | Separates IPO deleveraging from WC unwind | Mostly debt repaid | Mostly payables unwind | R-A3-20 |
| 31 | What is the segment split of the Rs 1,157 Mn H1 inventory rise, and what inventory days do you expect at 31-Mar-2027? | D | Cash conversion is INDETERMINATE; NWC +18% | Aerospace, falling toward 120 days | Consumer stock building | C-A3-21, P-A3-17, C-A3-22, R-A3-19 |
| 32 | Which subsidiary is reviewed by another auditor (Q2 revenue Rs 325 Mn), who is that auditor, and is the arrangement new this quarter? | G | Auditor reliance on a management-furnished report | Named, long-standing | New and unnamed | R-A3-22 |
| 33 | On what date was Reenah Joseph appointed CFO, and was the Reg 30 KMP intimation filed? | G | Monitorable 7; results signed by MD | Date and filing reference | No filing | R-A3-23, PR-A3-14 |
| 34 | Which operation is reported as discontinued (Rs 1.96 Mn loss in Q2), and is any further exit cost or FCTR recycling due? | G | Unnamed in the notes; likely ATHPL | ATHPL, closed out | Further exits pending | R-A3-01, R-A3-25 |
| 35 | Why was Aequs Toys Pvt Ltd renamed Aequs Manufacturing Pvt Ltd, and from what date? | G | Possible change of purpose for the toy vehicle | Broader manufacturing scope | Toy exit | R-A3-26 |
| 36 | How much consumer electronics pre-operative cost was capitalised in FY26, and will Hosur pre-operative cost be capitalised? | C | YoY margin base not like-for-like | Amount disclosed | Not disclosed | P-A3-19 |
| 37 | Is "parts added" (238) a count of new part numbers, and is "4% QoQ" growth of the 5,978 portfolio? | A | Moat-proxy definition after the 433 to 86 swing | Confirmed | Definition changed | P-A3-18 |
| 38 | Why does the press release show "(>100) bps" for a 974 bps EBITDA margin fall and an unsigned consumer QoQ change? | G | Disclosure quality pattern | Corrected in Q3 | Repeated | PR-A3-11, P-A3-16 |
| 39 | What quarterly EBITDA does management need for group PAT breakeven, and in which fiscal year? | B | Below-EBITDA charges about Rs 767 Mn a quarter vs EBITDA Rs 245 Mn | A year named with an EBITDA path | No answer | PR-A3-06, C-A3-01 |
| 40 | Will future press releases carry consumer utilisation, segment capex and the half-year cash flow? | G | Eleven checklist items absent from the release | Yes | No | PR-A3-16, C-A3-22 |
| 41 | When was the GoK MoU signed, and over how many years does the Rs 28,560 Mn investment run? | F | Undated headline investment equal to 2.05x Sep-26 equity | Dated, multi-year, phased | No period given | P-A3-23 |
| 42 | How much of the Rs 28,560 Mn is Aequs Limited's own capex, and what funds it beyond the Rs 6,500 Mn warrants? | F | Stated funding covers FY27 capex and Hosur, not this MoU | Mostly partner or state money | Mostly Aequs capex, unfunded | P-A3-23 |
| 43 | How do the top 5 customer groups (63% of H1 FY27 revenue) split between aerospace and consumer, and what share does the largest group hold? | E | Concentration location and single-group exposure | All aerospace, largest below 20% | Consumer CE customer in the top five, or one group above 25% | P-A3-24 |
| 44 | What was the top-5 customer group share in H1 FY26 and FY26? | E | Concentration trend cannot be tested from the deck | Falling | Rising | P-A3-24 |

Top 3 by likelihood of thesis-changing information:
- Q1 (breakeven quarter): a named quarter changes the bull probability; a second "no date" confirms the bear reading.
- Q3 (toy vs CE split of the revenue fall): a CE-led fall confirms the bear (plant economics) reading.
- Q18 (warrant upfront date and funding): tests management and promoter transparency against the pledge tripwire.

Channel recommendation: the concall has already occurred without these answers. Send an IR email to EY (IR contacts, deck slide 33) with all questions; prioritise Q1, Q2, Q3, Q10, Q18, Q42. Re-ask unanswered rows at the Q3 FY27 call (about late Jan to Feb 2027).

---

# MONITORABLES AND CATALYST LIST (seeded by A3 F6 commitment registers and F13 board items)

| Item | Implied date | Source ref |
|---|---|---|
| Q3 FY27 results: consumer segment revenue vs Rs 73.4 Cr; utilisation vs the 22% Q1 record [NOTION-PRIOR; ASR]; named breakeven quarter | About late Jan to mid Feb 2027 | R-L564; P-L184; N-L107; N-L726 |
| Warrant allotment after regulatory approvals; Rs 325 Cr upfront receipt | About Nov to Dec 2026 (approvals pending) | R-L273-274; C-FT269 |
| Warrant conversion: balance Rs 325 Cr due only on conversion; "proposed to be converted" (filed); optional while CMP is below Rs 231.55; non-conversion forfeits the upfront and leaves Rs 325 Cr received, not Rs 650 Cr | On or before 31-Dec-2027 | R-L274-275, R-L666-667; C-FT269-272 |
| Amalgamation route (refile S.233 or NCLT S.232) | Undated; Notion falsifier deadline Q3 FY27 | R-L268; N-L695 |
| Old toy customer phase-out; new customer almost complete | Q3 FY27 and Q4 FY27 | C-FT494-504 |
| IPO lock-in expiry, pledged locked-in promoter shares | About Dec-2026 | N-L171, N-L177 |
| Hosur Investment Phase 1 start | From Q4 FY27 | P-L240-246 (errata) |
| GoK MoU Rs 28,560 Mn: date, period, investing entity, funding source | Undated (2026 column, layout-inferred) | P-L560-564 (P-A3-23) |
| Top-5 customer group share (63% of H1 FY27): segment split and trend in next deck | Q3 FY27 deck, about Jan-Feb 2027 | P-L775-778 (P-A3-24) |
| FY27 capex outturn about Rs 320 Cr vs Rs 660 Cr | FY27 results, about May 2027 | C-FT365-368 |
| FY27 audit report, CARO, DTA recognition | About May 2027 | N-L112-113 |
| Inventory about 120 days | About Q1 FY28 | C-FT541-543 |
| Term loans over Rs 800 Cr | Undated | C-FT767 |
| FY28 external capital raise | FY28 | C-FT334-335 |
| Hosur commercial production; Safran new scope commercial | FY29 | P-L240-246; C-FT458 |
| Consumer PAT positive | FY30 (ASR) | C-FT409 |
| 4-6x growth | 2031 | C-FT328 |
| CFO Reg 30 KMP filing | Immediate | PR-L158; MC-L12 |
| Labour Court hearing (ASMIPL) cited in the S.233 rejection | 28-Oct-2026 (Notion record) | N-L10 Key Notes 14-Oct |

---

# SECTION C: COMBINED VERDICT

- Filing-derived signals: revenue +45.3% YoY; aerospace +44.2% YoY. Operating EBITDA -51.4% YoY and -6.2% QoQ. Core PBT worse. Consumer revenue -21.4% QoQ; consumer segment EBITDA (40.14) Cr. H1 CFO (80.83) Cr; net debt ex leases +314.41 Cr. Group tax charge on a loss, as in Q2 FY26 and FY26. Losses outside the parent 2.4x YoY.
- Concall-derived signals: consumer breakeven date withdrawn; no quantified recovery path; FY27 capex cut to about Rs 320 Cr; funding stack above stated capex (assumes warrant conversion; balance optional at CMP); GoK MoU Rs 28,560 Mn unaddressed; hedge-heavy (9 defensive phrases); consumer questions graded C or D.
- Reconciliation: the concall contradicts the filing on consumer "scale", JV "stable margins" and "strengthening cash conversion". The filing wins.
- Net thesis impact: WEAKENED. The falsification line FIRED on both legs. The aerospace leg holds on reported numbers; its ex-OI margin is unproven.
- Position decision: 8A-W. Fired condition flagged. No Decision Status recommended. Operator decides.
- Watchpoints next quarter: the 8C metric (consumer segment revenue), the warrant upfront receipt, the amalgamation route, the aerospace ex-OI margin.

Role 4 verdict: PROCEED WITH FLAGS. Evidence is filed and sufficient. Flags propagate. Cash conversion INDETERMINATE-WITH-DIRECTION caps the review below PROCEED in any case.
Role 5 verdict: PROCEED WITH FLAGS (ASR-UNVERIFIED source; credibility ratio ND). Concall Verdict block: Management credibility this quarter ND (prior log not passed); trailing ratio ND; archetype not classifiable; Role 1 track-record input ND; net concall impact WEAKENED; position decision: entry-zone update not possible (no zone on file), flag only.

## NOTION WEB-SIDE ENTRY OF 26-OCT-2026 (N-L629-755): AGREEMENTS AND DISAGREEMENTS

Tested against the filings. Not adopted.

| Web claim | This review | Result |
|---|---|---|
| Segment table: revenue 409.1/395.5/281.6; aero 351.4/322.2/243.7; consumer 57.7/73.4/37.9; aero EBITDA 78.3/73.1/63.0; consumer EBITDA (40.1)/(36.1)/(7.7); consumer after D&A, finance, JV (91.7)/(85.5)/(37.5) (N-L639-646) | Ties to R-L563-582 | AGREE |
| PAT Q2 (52.2) (N-L647) | Continuing PAT (52.20); total incl. discontinued (52.39) (R-L394, R-L398) | MINOR: web uses continuing |
| Falsification line fires on both legs (N-L655-658) | Same, with the utilisation basis caveat (P-L208) the web omits | AGREE, with caveat |
| Utilisation "17% against 23% ... lower than the 22% logged for Q1" (N-L656) | 17% filed (P-L184); 22% is the Notion record and an ASR analyst statement, not on the Q2 deck | AGREE on the leg; tier of 22% corrected |
| Consumer revenue -21.4% QoQ; margin -49% to -70% (N-L660) | -21.4%; -49.3% to -69.6% | AGREE |
| H1 PAT (105.4); FY27 about (210) if H2 repeats Q2 (N-L670) | (105.62) total; run-rate (210.4) | AGREE |
| Aero harsh floor 19.3%, Q1 20.6% (N-L676) | 19.27%, 20.59% | AGREE |
| Aero result after D&A, finance, JV flat at 53.1 vs 53.4; aero finance cost +53% QoQ (N-L677) | 53.06 vs 53.37; 7.79 to 11.94 (R-L571, R-L581) | AGREE |
| Parts "4% QoQ" is portfolio growth (N-L678) | 238/5,740 = 4.1% | AGREE |
| Net debt ex leases about 47 to 361; CFO (80.8); capex 164.8; inventory +106.7 (cash flow) (N-L683-685) | 46.93 to 361.34; (80.83); 164.83; 106.69 (R-L512) | AGREE |
| "The Rs 325 Cr warrant upfront roughly equals the H1 increase in net debt" (N-L685) | Agree; the second Rs 325 Cr is optional below Rs 231.55 ("proposed", R-L274-275) | AGREE, with the optionality the web omits |
| CWIP 78.7 to 123.6 (N-L687) | 78.66 to 123.56 | AGREE |
| "The call audio itself was not reviewed; there is no transcript" (N-L635) | ASR transcript now read: adds capex cut, warrant use split, Rs 800 Cr term loans, consumer PAT FY30, toy timeline, inventory target, additive-manufacturing exchange | WEB INCOMPLETE (superseded by this run) |
| EBITDA "Up 14% QoQ" not challenged on OI | Op EBITDA fell 6.2% QoQ; all of the rise is OI | DISAGREE (web missed) |
| Not covered by web: H1 non-cash EBITDA gains 27%; tax drag; S-vs-C gap; parent guarantee build; other-auditor subsidiary; contract-liability fall; JV share fall; GoK MoU; top-5 concentration 63% | This review covers each | ADDITIONS |
| ESOP grant 2 lakh options at Rs 235.50 (N-L703) | Not in this corpus | UNVERIFIABLE this run |
| CMP Rs 242 "likely pre-results" (N-L730) | CMP Rs 212 on 28-Oct: -12.4% vs 242; 8.4% below the Rs 231.55 warrant price; warrants out of the money | UPDATE |
| "FY28 base should be re-run, not carried" (N-L672) | Indicative roll-forward FY28E PAT about (178), below the Notion bear (83) | AGREE in direction; this review quantifies |

---

# PLAIN-LANGUAGE BRIEF

Provenance key: [FILED] statutory results; [MGMT-FILED] deck or press release; [ASR] concall machine transcript, unverified; [NOTION] prior unsigned Notion work; [INFERENCE] A4 arithmetic. "This quarter" marks figures from the Q2 FY27 filings; "prior" marks Notion or peer work.

## 1. SUMMARY NARRATIVE

Revenue rose 45% YoY to Rs 409 Cr in Q2 FY27 [FILED, R-L375]. Aerospace drove it, up 44% to Rs 351 Cr [FILED, R-L563]. Consumer revenue fell 21% in one quarter, from Rs 73.4 Cr to Rs 57.7 Cr [FILED, R-L564]. The consumer segment lost Rs 40.1 Cr at the EBITDA level [FILED, R-L567]. Consumer plant use was 17% [MGMT-FILED, P-L184]. It was 22% in Q1 [ASR, C-FT416, analyst, undisputed; NOTION, N-L107; basis comparability unconfirmed]. That is the test the draft model set. Both legs of the falsification line fired. Management withdrew its Q4 FY27 consumer breakeven date and gave no new one [MGMT-FILED, P-L265]. Group operating EBITDA fell 6% from Q1 to Rs 13.9 Cr [INFERENCE]. The reported 14% rise came from forex other income. Net loss was Rs 52.4 Cr [FILED, R-L398]. Operating cash flow for the half was negative Rs 80.8 Cr [FILED, R-L523]. Net debt rose from Rs 47 Cr to Rs 361 Cr in six months [INFERENCE]. The group pays tax on a loss. Profitable aerospace units pay current tax, and subsidiary losses earn no tax credit [FILED, R-L391-393; ASR, C-FT245-247]. This also happened in Q2 FY26 and FY26 [FILED, R-L390, R-L393]. On 12-Oct-2026, after the quarter, the regulator rejected the merger. That blocks one route to offset the losses [FILED, R-L265-268]. Aerospace still holds up on reported numbers. The decision status is not set and the model is unsigned. The fired line is a flag for the operator, not an action.

## 2. SECTOR INTELLIGENCE

Aerospace demand reads healthy. The order book rose 9% to USD 1,096 Mn [MGMT-FILED, P-L193]. Aerospace plant use is 69%, and 76% in India [MGMT-FILED, P-L184]. Programmes run five to seven years [ASR, C-FT394]. Safran expanded to six group entities after quarter-end [MGMT-FILED, P-L198]. That work starts earning at Hosur in FY29 [ASR, C-FT458]. Consumer electronics runs on yearly product updates. Each update needs a new qualification cycle [ASR, C-FT717-720]. Aequs misjudged that cycle this quarter. Toy volumes depend on one customer at a time. The old customer leaves in Q3 and the new one ramps by Q4 [ASR, C-FT494-504]. Raw material shortages and weather hit toy logistics [MGMT-FILED, P-L275]. Peer concalls were not available this run [prior Notion: AZAD and UNIMECH margins in the 30s, N-L45].

## 3. BUSINESS-MODEL INTELLIGENCE

Aequs makes money from aerospace machining and assemblies under long contracts. Material costs pass through to customers [ASR, C-FT694]. Aerospace earns a segment margin near 22% with other income inside [FILED, R-L563, R-L566]. That margin was 26% a year ago. Consumer is two plants with a fixed cost base: electronics at Hubballi and toys at Koppal [NOTION, N-L43]. Consumer capital now roughly equals aerospace capital [ASR, C-FT683; FILED segment assets R-L590-591]. At 17% use, that capital loses money. Management says breakeven needs about 50% use [ASR, C-FT406]. The model drifted this quarter. Capex moved to aerospace. FY27 capex will be about Rs 320 Cr, not Rs 660 Cr [ASR, C-FT365-368]. The deck also shows an MoU with Karnataka for Rs 2,856 Cr of investment, with no date, entity or funding source [MGMT-FILED, P-L560-562]. Losses sit in subsidiaries, not the parent [FILED, R-L104, R-L398]. Parent profit is intra-group interest and guarantee fees [FILED, R-L181, R-L185]. Undisclosed: segment other income, segment cash flow, consumer breakeven revenue.

## 4. COMPETITION INTELLIGENCE

Aequs wins on an integrated single-site ecosystem at Belagavi [MGMT-FILED, P-L212]. Forging and surface treatment come from co-located JVs. Qualification lock-in protects volume, not price [NOTION, N-L45]. Peers AZAD and UNIMECH earn margins in the 30s [NOTION, N-L45; tier SECONDARY]. Aequs is structurally weaker on price power and on margin. Five customer groups gave 63% of H1 FY27 revenue [MGMT-FILED, P-L775-777]. The deck gives no segment split, no largest-customer share and no prior-period figure. If all five are aerospace, they hold about 75% of aerospace revenue [INFERENCE, 63/84]. Safran alone is now six entities, so one group's buying decision carries weight. In consumer electronics, the risk is a customer shift in process technology. An analyst asked about a move to additive manufacturing [ASR, C-FT612-616]. Management denied it without evidence [ASR, C-FT617]. In toys, Aequs has lost one anchor customer and depends on one replacement. The competitive risk to watch is customer concentration in both segments. A second watch item is JV margins: JV profit share fell 38% from Q1 [FILED, R-L388].

## 5. FORWARD MAP (next 10-11 months)

Make-or-break reading: Q3 FY27 consumer segment revenue, about late January to mid February 2027. Bull: at or above Rs 73.4 Cr with a named breakeven quarter. Bear: below Rs 57.7 Cr, or no date again.

| Catalyst | Date | Bull fork | Bear fork |
|---|---|---|---|
| Warrant allotment and Rs 325 Cr upfront | About Nov-Dec 2026 | Received from own funds; net debt eases | Delayed, or funded from the pledge facility |
| IPO lock-in expiry | About Dec 2026 | Pledged block stays; no supply overhang | Early holders sell; pledge cover falls with price |
| Amalgamation route | Undated; Notion deadline Q3 FY27 | Route filed; one offset route opens on a date | "Evaluating" again; tax drag continues |
| Toy customer transition | Q3 to Q4 FY27 | New customer fills the gap by Q4 | Q3 gap widens the consumer loss |
| Q3 FY27 results | About Jan-Feb 2027 | Consumer revenue at or above Rs 73.4 Cr; breakeven quarter named | Consumer revenue below Rs 57.7 Cr; no date |
| Hosur Investment Phase 1 | From Q4 FY27 | Capex envelope named, funded | Unguided spend raises leverage |
| GoK MoU disclosure | Undated | Mostly partner or state money, phased | Mostly Aequs capex with no funding source |
| FY27 results and audit | About May 2027 | Clean audit; no consumer impairment | Impairment on consumer assets; CARO remarks |
| Inventory target | About Q1 FY28 | About 120 days | Days stay near 155 |
| Warrant conversion | By 31-Dec-2027 | Promoter converts; second Rs 325 Cr arrives | Price stays below Rs 231.55; promoter lets warrants lapse; only Rs 325 Cr received |

## INDICATIVE FY27E AND FY28E (not a Role 1 valuation; no Section 1B exit multiple)

Basis: the unsigned Notion projections (N-L90-103) rolled forward for H1 FY27 actuals and this quarter's guidance changes. Where the Notion base relied on the withdrawn consumer breakeven, the Q2 run-rate replaces it. No ramp is credited without a dated basis.

| Rs Cr | Notion FY27 base | FY27E | Basis and tier | Notion FY28 base | FY28E | Basis and tier |
|---|---|---|---|---|---|---|
| Aerospace revenue | 1,340 | 1,376.4 | H1 673.57 [FILED R-L563] + H2 at Q2 run-rate 2 x 351.41 [INFERENCE]; mgmt "on target" [ASR C-FT378] | 1,675 | 1,675 | Notion base held; no FY28 aero guidance change [NOTION N-L92] |
| Consumer revenue | 350 | 246.4 | H1 131.05 [FILED R-L564] + H2 at Q2 run-rate 2 x 57.67 [INFERENCE]; guide withdrawn [ASR C-FT308] | 543 | 230.7 | Q2 run-rate x 4 [INFERENCE]; breakeven path withdrawn, no dated basis for a ramp |
| Total revenue | 1,690 | 1,622.8 | Sum | 2,218 | 1,905.7 | Sum |
| EBITDA (incl. OI, Notion basis) | 154 | 94.9 | H1 45.95 [FILED R-L384] + H2 at Q2 run-rate 2 x 24.47 [INFERENCE] | 354 | 157.9 | Aero 22.29% x 1,675 = 373.3 [FILED margin R-L563/566]; consumer Q2 loss x 4 = (160.6) [FILED R-L567]; eliminations and unallocated Q2 x 4 = (54.9) [FILED R-L569, R-L586] [INFERENCE] |
| D&A | ND | ND (in PAT run-rate) | n/a | ND | 215.0 | Notion assumption [NOTION N-L135]; Q2 run-rate 186.1 [FILED R-L386] |
| Finance cost | ND | ND (in PAT run-rate) | n/a | ND | 82.4 | Q2 x 4 [FILED R-L385; INFERENCE]; term loans over Rs 800 Cr would raise it [ASR C-FT767] |
| JV share | ND | ND | n/a | ND | 7.2 | Q2 x 4 [FILED R-L388; INFERENCE] |
| Tax | ND | ND (in PAT run-rate) | n/a | ND | 45.4 | Q2 x 4 [FILED R-L393; INFERENCE]; rises with aerospace profit while subsidiary losses cannot offset it |
| PAT | (158) | (210.4) | H1 (105.62) [FILED R-L398] + H2 at Q2 run-rate 2 x (52.39) [INFERENCE] | 42 | (177.7) | 157.9 - 215.0 - 82.4 + 7.2 - 45.4 [INFERENCE]; at Q2 D&A run-rate 186.1, PAT (148.8) |

Share count and per-share figures.

| Item | Value | Basis |
|---|---|---|
| Basic shares in issue | 670.67 Mn (67.07 Cr) | Paid-up Rs 6,706.66 Mn / Rs 10 [FILED R-L109, R-L415] |
| Weighted shares used in EPS (implied) | About 656 Mn | (1,056.20) / (1.61) [INFERENCE; R-A3-17]; ESOP trust treasury shares |
| Warrants | 28,071,690 at Rs 231.55, "proposed to be converted" by 31-Dec-2027 | [FILED R-L272-275; price NOTION N-L16] |
| Fully diluted shares if warrants convert | 698.74 Mn (69.87 Cr) | 670.67 + 28.07 [INFERENCE]; conversion optional while CMP is below Rs 231.55 |
| Other ESOP options outstanding | ND | Not in this corpus |
| Market cap at CMP Rs 212 | Rs 14,169 Cr (screener.in, 28-Oct-2026 08:48 IST) | Operator-supplied; 670.67 Mn x 212 = Rs 14,218 Cr (0.3% higher) |
| FY27E EPS, basic / diluted | Rs (3.14) / Rs (3.01) | (210.4) / 67.07; / 69.87 [INFERENCE] |
| FY28E EPS, basic / diluted | Rs (2.65) / Rs (2.54) | (177.7) / 67.07; / 69.87 [INFERENCE] |
| Forward PE FY27E / FY28E at Rs 212 | NM / NM | PAT negative |
| Cross-check, Notion FY27 base EPS | Rs (2.36) | [NOTION N-L99] |

Two readings of the quarter.
- Reading A (timing). The consumer miss is a qualification delay and a toy customer swap. Raw material and weather issues are temporary. Aerospace grows 44% with a larger order book. The promoter commits Rs 325 Cr on allotment at Rs 231.55. Consumer use recovers once the new toy customer and the updated CE product ramp.
- Bear counter inside Reading A. Only Rs 325 Cr is due on allotment [ASR, C-FT269-270]. The filing says the warrants are "proposed to be converted" by 31-Dec-2027 [FILED, R-L274-275]. At Rs 212, below Rs 231.55, the second Rs 325 Cr is an option, not committed cash. The "irrespective of market price" letter sits only on the Notion page [NOTION, N-L16]. Reading A holds only if the promoter converts.
- Reading B (structural). The consumer plants carry a fixed cost base that 17% use cannot cover. Management says the majority of the loss sits in the electronics plant, not toys [ASR, C-FT529-530]. Management has no breakeven revenue figure. Funding exceeds stated capex, yet an undated Rs 2,856 Cr MoU has no named source. Tax drag and finance cost rise. FY28 stays loss-making.
- The one observation that separates them: Q3 FY27 consumer segment revenue in the filed segment table. At or above Rs 73.4 Cr with a named breakeven quarter supports Reading A. Below Rs 57.7 Cr, or no date, supports Reading B.

```yaml
stage: A4-analyst
company: "AEQUS"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
correction_loop: 1
docs_merged: [results, concall, presentation, pressrelease]
ledger_reconciliation:
  notes: 21
  turns: 84
  slides: 38
  all_reviewed: true
  a3_findings_incorporated: ["R-A3-01..R-A3-26", "P-A3-01..P-A3-24", "PR-A3-01..PR-A3-18", "C-A3-01..C-A3-24"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "NOT SET (operator-only); Mental Model v2 DRAFT UNSIGNED; Phase 1 REWORK; not held"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2FY26", gap_rs_cr: -20.76, pct_of_standalone_pat: "-12358%"}
  - {period: "Q1FY27", gap_rs_cr: -57.29, pct_of_standalone_pat: "-1409%"}
  - {period: "Q2FY27", gap_rs_cr: -54.18, pct_of_standalone_pat: "-3025%"}
  - {period: "H1FY26", gap_rs_cr: -20.99, pct_of_standalone_pat: "-523%"}
  - {period: "H1FY27", gap_rs_cr: -111.48, pct_of_standalone_pat: "-1903%"}
  - {period: "FY26", gap_rs_cr: -163.05, pct_of_standalone_pat: "-327%"}
questions_for_management:
  - {q: "New consumer EBITDA breakeven quarter after Q2 loss Rs 401 Mn at 17% utilisation", from_finding_id: "C-A3-01, P-A3-03, P-A3-05, PR-A3-03, PR-A3-04, C-A3-17"}
  - {q: "Consumer quarterly revenue (Rs Mn) for segment EBITDA breakeven at today's cost base", from_finding_id: "C-A3-03, C-A3-04, C-A3-17, R-A3-18"}
  - {q: "Split of Rs 157 Mn QoQ consumer revenue fall: toys vs consumer electronics", from_finding_id: "P-A3-10, P-A3-16, PR-A3-02, C-A3-24, R-A3-18"}
  - {q: "Sign of 900 bps YoY consumer utilisation change; same basis for 17% and 22%", from_finding_id: "P-A3-20, R-A3-18"}
  - {q: "Impairment test on consumer assets Rs 12,478 Mn at 30-Sep-2026 and headroom", from_finding_id: "R-A3-02"}
  - {q: "H1 FY27 loss of AEPPL and AFCPPL", from_finding_id: "R-A3-07"}
  - {q: "Old toy customer at zero by Q4; new customer share of Q3 toy revenue", from_finding_id: "C-A3-16"}
  - {q: "CE customer moving parts to additive manufacturing before FY29, yes/no", from_finding_id: "C-A3-20"}
  - {q: "Forex share of Q2 other income Rs 106 Mn", from_finding_id: "P-A3-15, C-A3-05, PR-A3-05"}
  - {q: "Aerospace segment EBITDA margin ex other income Q1 and Q2 FY27", from_finding_id: "P-A3-12, C-A3-07, PR-A3-05, PR-A3-10, R-A3-19"}
  - {q: "Does rising titanium content lower aerospace margin % in FY27, yes/no", from_finding_id: "C-A3-08"}
  - {q: "Content of Q2 segment elimination Rs 104.2 Mn", from_finding_id: "C-A3-06, PR-A3-10, P-A3-13"}
  - {q: "P&L lines holding H1 non-cash gains Rs 124 Mn and H2 recurrence", from_finding_id: "R-A3-08"}
  - {q: "Facility and segment of lease derecognised for Rs 13.1 Mn gain", from_finding_id: "R-A3-06"}
  - {q: "Expected FY27 tax charge while amalgamation pending", from_finding_id: "R-A3-15, P-A3-06, C-A3-12"}
  - {q: "Refile S.233 or NCLT S.232, and by which date", from_finding_id: "R-A3-13, R-A3-14, C-A3-14, R-A3-23"}
  - {q: "Source and expiry of parent low current tax", from_finding_id: "R-A3-16"}
  - {q: "Date of Rs 3,250 Mn warrant upfront; any funding from 360 One Prime facility", from_finding_id: "R-A3-12, P-A3-04, P-A3-07, PR-A3-07, P-A3-01, P-A3-09"}
  - {q: "Use of unallocated Rs 161 Cr of warrant money", from_finding_id: "C-A3-11, PR-A3-08"}
  - {q: "Sanction, lender and drawdown of over Rs 800 Cr term loans", from_finding_id: "C-A3-10, R-A3-19, P-A3-09"}
  - {q: "Hosur Phase 1 capex envelope FY28 and FY29", from_finding_id: "C-A3-09, C-A3-18, P-A3-02, PR-A3-12, PR-A3-15"}
  - {q: "FY28 external equity raise planned, yes/no", from_finding_id: "C-A3-10"}
  - {q: "Parent guarantees for subsidiary borrowings outstanding and covered subsidiaries", from_finding_id: "R-A3-10"}
  - {q: "Subsidiary behind Rs 173.4 Mn H1 FY26 loan impairment; recoverability of Rs 2,096 Mn loans", from_finding_id: "R-A3-03"}
  - {q: "JV receiving Rs 93.0 Mn in H1; Cookware Rs 30.05 Cr receivable collected?", from_finding_id: "R-A3-11"}
  - {q: "JV behind JV profit share fall Rs 29.0 Mn to 18.1 Mn QoQ", from_finding_id: "C-A3-15, PR-A3-09, R-A3-11"}
  - {q: "Order book USD 1,096 Mn includes post-quarter Safran agreements, yes/no; value", from_finding_id: "P-A3-22, PR-A3-13, C-A3-18"}
  - {q: "Fiscal year of Safran A320 wheels serial delivery start", from_finding_id: "C-A3-18"}
  - {q: "Driver and segment of 61% fall in current contract liabilities", from_finding_id: "R-A3-21"}
  - {q: "Debt repayment share of aerospace segment liability fall YoY", from_finding_id: "R-A3-20"}
  - {q: "Segment split of Rs 1,157 Mn H1 inventory rise; inventory days at 31-Mar-2027", from_finding_id: "C-A3-21, P-A3-17, C-A3-22, R-A3-19"}
  - {q: "Name of subsidiary under other auditor, the auditor, and whether new", from_finding_id: "R-A3-22"}
  - {q: "CFO appointment date and Reg 30 KMP filing", from_finding_id: "R-A3-23, PR-A3-14"}
  - {q: "Discontinued operation identity (Rs 1.96 Mn) and further exit cost", from_finding_id: "R-A3-01, R-A3-25"}
  - {q: "Purpose and date of Aequs Toys to Aequs Manufacturing rename", from_finding_id: "R-A3-26"}
  - {q: "FY26 CE pre-operative cost capitalised; Hosur treatment", from_finding_id: "P-A3-19"}
  - {q: "Confirm parts-added definition and 4% as portfolio growth", from_finding_id: "P-A3-18"}
  - {q: "Press release margin labels '(>100) bps' and unsigned consumer QoQ", from_finding_id: "PR-A3-11, P-A3-16"}
  - {q: "Quarterly EBITDA and fiscal year for group PAT breakeven", from_finding_id: "PR-A3-06, C-A3-01"}
  - {q: "Future press releases to carry utilisation, segment capex, half-year cash flow", from_finding_id: "PR-A3-16, C-A3-22"}
  - {q: "GoK MoU Rs 28,560 Mn: signing date and investment period", from_finding_id: "P-A3-23"}
  - {q: "Aequs Limited's own share of the GoK MoU and its funding beyond the Rs 6,500 Mn warrants", from_finding_id: "P-A3-23"}
  - {q: "Top 5 customer groups (63% of H1 FY27): aerospace vs consumer split and largest group share", from_finding_id: "P-A3-24"}
  - {q: "Top 5 customer group share in H1 FY26 and FY26", from_finding_id: "P-A3-24"}
monitorables:
  - {item: "Q3 FY27 consumer segment revenue vs Rs 73.4 Cr / Rs 57.7 Cr; utilisation vs 22% Q1 record (NOTION/ASR); named breakeven quarter", implied_date: "2027-01/02", source_ref: "R-L564; P-L184; N-L107"}
  - {item: "Warrant allotment and Rs 325 Cr upfront receipt", implied_date: "2026-11/12 (approvals pending)", source_ref: "R-L273-274; C-FT269"}
  - {item: "Warrant conversion; balance Rs 325 Cr optional while CMP below Rs 231.55 ('proposed to be converted')", implied_date: "2027-12-31", source_ref: "R-L274-275; R-L666-667"}
  - {item: "Amalgamation route decision (S.233 refile or NCLT S.232)", implied_date: "undated; Notion deadline Q3 FY27", source_ref: "R-L268; N-L695"}
  - {item: "Toy customer transition complete", implied_date: "Q4 FY27", source_ref: "C-FT494-504"}
  - {item: "IPO lock-in expiry incl. pledged promoter shares", implied_date: "about 2026-12", source_ref: "N-L171; N-L177"}
  - {item: "Hosur Investment Phase 1 start", implied_date: "Q4 FY27", source_ref: "P-L240-246 (errata)"}
  - {item: "GoK MoU Rs 28,560 Mn: date, period, investing entity, funding", implied_date: "undated", source_ref: "P-L560-564 (P-A3-23)"}
  - {item: "Top-5 customer group share 63%: segment split and trend", implied_date: "Q3 FY27 deck, 2027-01/02", source_ref: "P-L775-778 (P-A3-24)"}
  - {item: "FY27 capex outturn about Rs 320 Cr vs Rs 660 Cr", implied_date: "about 2027-05", source_ref: "C-FT365-368"}
  - {item: "FY27 audit, CARO, DTA recognition, consumer impairment", implied_date: "about 2027-05", source_ref: "N-L112-113; R-L591"}
  - {item: "Inventory about 120 days", implied_date: "about Q1 FY28", source_ref: "C-FT541-543"}
  - {item: "Term loans over Rs 800 Cr drawdown", implied_date: "undated", source_ref: "C-FT767"}
  - {item: "FY28 external capital raise", implied_date: "FY28", source_ref: "C-FT334-335"}
  - {item: "Hosur commercial production; Safran new scope", implied_date: "FY29", source_ref: "P-L240-246; C-FT458"}
  - {item: "CFO Reg 30 KMP filing", implied_date: "immediate", source_ref: "PR-L158; MC-L12"}
flags:
  - "FALSIFICATION LINE FIRED on both legs: consumer segment EBITDA Rs (40.14) Cr vs 36.1 (R-L567, FILED); utilisation 17% vs 23% (P-L184, MGMT-FILED, basis incl subs and JVs P-L208); Q1 22% is NOTION/ASR only"
  - "8A-W mechanical output on a fired condition is 'reclassify to AVOID'; flagged only, no Decision Status recommended; operator decides"
  - "Consumer EBITDA breakeven Q4 FY27 withdrawn, no new date (P-L265; C-FT179); consumer revenue -21.4% QoQ (R-L564)"
  - "Operating EBITDA ex OI fell 6.2% QoQ to Rs 13.86 Cr; reported +14% is forex other income"
  - "H1 EBITDA includes Rs 12.41 Cr non-cash gains (27%) incl. inventory-provision reversal Rs 8.37 Cr (R-L500)"
  - "Cash INDETERMINATE-WITH-DIRECTION: H1 CFO Rs (80.83) Cr, FCF (245.66), net debt ex leases 46.93 to 361.34 Cr"
  - "Group tax on a loss: H1 tax Rs 24.77 Cr on PBT (80.66); also Q2 FY26 and FY26, before the 23-Apr-2026 scheme (R-L390, R-L393, R-L263); post-quarter rejection 12-Oct-2026 blocks one offset route (R-L265)"
  - "Monitorable 2 not clean: aero margin 22.29% reported, 19.27% on page's harsh method; true ex-OI ND"
  - "Losses outside parent: subsidiaries plus eliminations Rs (55.99) Cr Q2 vs (22.86) YoY"
  - "Indicative FY28E PAT about Rs (178) Cr vs Notion base 42 and bear (83): FY28 base chain broken"
  - "Warrants out of the money at CMP 212 vs 231.55; only Rs 325 Cr due on allotment; balance optional ('proposed to be converted', R-L274-275); upfront not received; pledge tripwire limbs 2-3 UNTESTABLE"
  - "GoK MoU Rs 28,560 Mn (P-L560-562): undated, entity and funding NOT FOUND; 2.05x Sep-26 equity"
  - "Top 5 customer groups 63% of H1 FY27 revenue (P-L775-777); no segment split or trend"
  - "Two candidate DROPPED commitments (consumer revenue guide; H1 FY28 group PAT breakeven) pending prior-log check"
  - "Concall ASR-UNVERIFIED; 74 s source gap; credibility ratio and archetype ND (prior log not passed)"
  - "Tracker rows not supplied; Step 5.5 reconciliation not possible; seven new-signal payload candidates"
  - "A2 TIE_FAILs in consolidated H1 FY26 column (R441, R843) affect comparatives only"
plain_language_brief_included: true
analyst_note: "Loop 1 changed no verdict, no falsification status and no FY27E/FY28E total. The quarter splits cleanly. Aerospace delivered: revenue +44% YoY, order book +9%, parts back to 238. Consumer failed the draft model's own test on both legs: a statutory segment line and the filed 17% deck tile. The 22% Q1 comparison is Notion/ASR only and is not needed for the threshold. Hidden weaknesses: operating EBITDA ex other income fell QoQ; 27% of H1 EBITDA is non-cash gains; CFO negative; net debt up Rs 314 Cr. Tax on a loss predates the merger scheme; the post-quarter rejection only keeps one offset route shut. Funding reads weaker after loop 1: only Rs 325 Cr of the warrants is committed on allotment, and an undated Rs 2,856 Cr GoK MoU has no named source. Concentration: five customer groups give 63% of revenue. FY28E credits no consumer ramp; at the Q2 D&A run-rate it is about (149). Neither figure is a valuation."
review_path: "runs/aequs-q2fy27/work/review_aequs_q2fy27.md"
```

---

# LOOP 1 CHANGE LOG (A5 audit runs/aequs-q2fy27/work/audit_aequs_q2fy27.md)

| Fix | Audit ref | Location changed (section; pre-loop line per audit) | Change |
|---|---|---|---|
| F1 FACTUAL | A5 F1, A4-L870 | Brief 1 Summary Narrative (A4-L870) | Removed "because the merger of loss-making units was rejected". Now states: group pays tax on a loss; aerospace units pay current tax and subsidiary losses earn no credit (R-L391-393; C-FT245-247); same in Q2 FY26 and FY26 (R-L390, R-L393); 12-Oct-2026 rejection is post-quarter and blocks one offset route (R-L265-268) |
| F1 sweep | A5 F1 "anywhere else" | Step 0D note S7/C8 row and the "notes that change interpretation" line; Step 4 tax row and tax answer; 6B row 6; 6D amalgamation row; 7A amalgamation row; Section C bullet 1; Forward Map amalgamation row; FY28E tax basis; YAML tax flag | Causal or implied-causal wording replaced with dated filed facts; pre-scheme tax on a loss (scheme approved 23-Apr-2026, R-L263) stated |
| M1 MISSING | A5 M1; P-A3-23 | Preamble counts; Step 2 (Role 5) guidance table new "Capex beyond FY27" row and diagnostics (A4-L520); 4C exchange 2 "Not said" and implication (A4-L600-603); 5B row; Step 7 pillar table row; 8D; 5.5C row; Monitorables row; Brief 3 Business-Model line; Forward Map row; Reading B; QfM 41-42 (next to QfM 19-22); Section C; YAML | GoK MoU Rs 28,560 Mn (P-L560-564) incorporated as an undated, unfunded capital intent with no entity or phasing |
| M2 MISSING | A5 M2; P-A3-24 | Preamble counts; 6D aerospace row; Step 7 pillar table row; 8D; 5B row; 5.5C row; Monitorables row; Brief 4 Competition Intelligence (A4-L882); QfM 43-44; Section C web table; YAML | Top 5 customer groups 63% of H1 FY27 revenue (P-L775-778) incorporated; concentration now named across both segments |
| M3 MISSING | A5 M3, Claim 3 | 0C warrant row; 0D S8/C10 row; Step 5 net-debt answer; 6C-bis new "Warrant bear counter" paragraph (A4-L378); Step 2 funding row and diagnostics; 7A new warrant row; Monitorables warrant-conversion row (A4-L809); Forward Map new conversion row; Reading A bear counter (A4-L931); share-count table; Section C; web table; YAML | Only Rs 325 Cr due on allotment; filed "proposed to be converted" (R-L274-275, R-L666-667); at CMP Rs 212 below Rs 231.55 the second Rs 325 Cr is optional; "irrespective of market price" is NOTION-PRIOR only; Reading A now "commits Rs 325 Cr on allotment" |
| C1 CONTRADICTION | A5 C1, A4-L870 | Brief 1 Summary Narrative (A4-L870); 6B row 1; 6C text below table; 6C "what would need to reverse"; 8B row 1; Monitorables Q3 row; web table new row; YAML flag 1 and monitorable 1 | "22% to 17% [MGMT-FILED, P-L184]" re-tiered: 17% MGMT-FILED (P-L184); 22% NOTION-PRIOR (N-L107) and ASR analyst, undisputed (C-FT416), basis comparability unconfirmed |
| S1 style (arithmetic display) | A5 S1, A4-L908 | FY28E table, EBITDA basis | Eliminations and unallocated (54.8) corrected to (54.9) ((104.21 + 32.94) x 4 = 548.6 Mn); total 157.9 unchanged |

Impact check.
- Verdict card: unchanged. Role 4 and Role 5 verdicts stay PROCEED WITH FLAGS. Cash conversion stays INDETERMINATE-WITH-DIRECTION. Position branch stays 8A-W. No headline number on the card moved.
- Falsification line: unchanged, FIRED on both legs. The utilisation leg rests on the filed 17% alone; the 22% re-tier (C1) does not touch the 23% threshold test.
- FY27E/FY28E table: no total moved. FY27E revenue 1,622.8, EBITDA 94.9, PAT (210.4); FY28E revenue 1,905.7, EBITDA 157.9, PAT (177.7). One component display corrected (S1). M3 changes the funding reading, not the P&L roll-forward. M1 (GoK MoU) is unquantified as Aequs capex, so it adds no number to the table.
