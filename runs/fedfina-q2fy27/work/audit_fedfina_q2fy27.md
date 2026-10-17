# A5 ADVERSARY / COMPLETENESS AUDIT: Fedbank Financial Services Ltd (FEDFINA), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-17
Review under audit: work/review_fedfina_q2fy27.md (754 lines in loop 0; cited below as "review Lnnn")
Inputs read: three A1 fulltexts (all lines), three A1 structured files (all rows), three A2 ledgers (all rows), the A4 review (all lines).
Not opened: the source PDFs, anything under inputs/, A3 forensics, the orchestrator extraction check (XC), the Notion copy.
Cite convention: "Res" = results, "Deck" = presentation, "PR" = press release. "R###" = A1 structured row. "L###" = A1 fulltext line of that document.

Record structure: the loop-0 audit follows unchanged, except that its YAML block is marked superseded. The "Re-audit loop 1" section follows; its YAML block is also marked superseded. The "Re-audit loop 2" section at the end carries the current verdict and the current YAML block.

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate: PASS.

| Part | Heading (review line) | Content test | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" (L597) | 15 lines (L598-L612). Quarterly Results protocol governs, so the 10-20 line band applies. Real figures, two named risks, a decision line and an operator item. | PRESENT |
| 2. Sector intelligence | "### 2. Sector intelligence" (L614) | 7 lines: gold growth source, LTV, unnamed industry change, CoB, rating, secondary data. | PRESENT |
| 3. Business-model intelligence | "### 3. Business-model intelligence" (L623) | 9 lines: mix, spread, three drift vectors, parent funding, missing cash test. | PRESENT |
| 4. Competition intelligence | "### 4. Competition intelligence" (L633) | 6 lines. No peer figures in the run (stated). Named peers are context only, each claim tagged INFERENCE. This is thin but it is real content, not a placeholder. | PRESENT |
| 5. Forward map | "### 5. Forward map" (L640) | One make-or-break metric plus 8 dated catalysts. Each catalyst carries a Bull and a Bear fork. | PRESENT |

---

## AUDIT 1. COVERAGE (fresh pass over the A1 fulltexts, the spine)

Method: I read every line of the three fulltexts. I counted each category against the A1 structured rows and the A2 ledgers. I then tested each ledger row for a citation in A4 or an explicit "reviewed" mark. A4 marks all rows reviewed at category level ("All 38 notes / 0 turns / 45 slides reviewed. Unreviewed rows: none", review L15-L19).

ID accountability: Res R001-R748, Deck R001-R1102 and PR R001-R247 are each covered by contiguous ledger ranges. No structured ID is absent from its ledger.

| Doc | Category | A2 count | Fresh count | Orphan rows (ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Results | Notes and footnotes | 36 | 36 (P&L # 1; Notes 1-11; Note 8 * and second disclosure 2; Note 9 * and footnotes 1-7: 8; Note 10 (I),(II),(iii),(iv) and * : 5; Annexure I notes 1-6; Annexure II footnotes 3) | None formally (category mark). Substantive: the R743/R744 qualifier content is absent where A4 discusses that covenant (finding M6). | PASS (count) |
| Results | Line items (A2 grouping convention) | 339 | 341 material + 4 NA-only template rows | n/a | FAIL. Res L525 "Aggregate principal outstanding of loans transferred" and L526 "Weighted average residual tenor of the loans transferred" (Note 10(I) table) are labelled rows with blank cells. They have no R-ID and no MFS entry (M1, A2). The 4 NA-only Annexure I rows (L761, L768, L788, L790) are immaterial: STYLE S10. |
| Results | ZERO_STANDING | 38 | 38 | none | PASS |
| Results | Agenda items | 6 | 6 (item 1 plus enclosures a-e, L44-L58) | none | PASS |
| Results | Auditor paragraphs | 19 | 19 (review report 1-5, L129-L175; certificate 1-14, L579-L716) | none | PASS |
| Results | Entities | 38 | 38 | none | PASS |
| Results | Signature blocks | 5 | 7 | n/a | FAIL. Res L812 "For Fedbank Fin~ I Services Limited." (Annexure I) and L932 "For Fedbank Financia~ices Limited." with mark at L934 (Annexure II) are not enumerated (M2, A2). |
| Results | Forward / dates | 8 / 35 | 8 / 35 | none | PASS |
| Deck | Slides | 42 | 42 ([page N] markers) | none (5 dividers: slides 4, 9, 20, 32, 37) | PASS |
| Deck | NUMBER rows | 971 | 971; plus one word-number "Nine ... login solutions" (L1135-L1136), not analytical | none | PASS (STYLE S9) |
| Deck | Footnotes and qualifiers | 37 | 37 | none | PASS |
| Deck | Entities | 57 | 57 | none | PASS |
| Deck | Forward statements | 20 | 20 on A1's convention; plus 11 uncaptured decorative taglines (L188, L263, L287, L316, L345, L387, L413, L483, L515, L555, L1242) and the slide 10 "Target Segment" bullet (L248) | none | PASS (STYLE S9) |
| Deck | Dates / ZERO_STANDING | 17 / 1 | 17 / 1 (R1024) | none | PASS |
| PR | Pages / line items | 3 / 25 | 3 / 25 (L80-L94 15 rows, L102-L103 2, L123-L128 6, L135-L136 2) | none | PASS |
| PR | Entities / forward / dates / qualifiers | 14 / 3 / 11 / 5 | 14 / 3 / 11 / 5; plus "Encl.: a/a" (L57) uncaptured | none | PASS (STYLE S9) |

Coverage result: orphan rows 0 (formal). Rows the fresh pass found that the ledger lacks: 4 material (Res L525, L526, L812, L932). FAIL, loop to A2.

---

## AUDIT 2. ARITHMETIC (every derived metric recomputed from raw extracted numbers)

Units: results figures are INR lakh x0.01 = Rs Cr. Deck and PR figures are Rs Cr.

| Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| NII Q2 FY27 / Q1 FY27 / Q2 FY26 | 403.67 / 371.88 / 293.86 (L112) | 692.01-288.34; 644.57-272.69; 507.70-213.84 | Res R001-R003, R037-R039 (L218, L225) | PASS |
| NII FY26 / H1 FY26 / H1 FY27 | 1,229.75 / 562.02 / 775.55 (L112) | 2,109.07-879.32; 993.83-431.81; 1,336.58-561.03 | Res R004-R006, R040-R042 | PASS |
| Other income (fee + FV gain + other), all 6 columns | 28.29 / 25.68 / 27.78 / 117.54 / 59.41 / 53.46 (L115) | e.g. Q2 FY27 23.12+4.28+0.38 = 27.78 | Res R007-R030 (L219-L222) | PASS |
| Opex (employee + D&A + other), all 6 columns | 183.16 / 210.02 / 226.37 / 771.01 / 357.37 / 436.39 (L116) | e.g. Q2 FY27 126.54+15.41+84.42 = 226.37 | Res R049-R066 (L227-L229) | PASS |
| PPOP, all 6 columns | 138.99 / 187.54 / 205.08 / 576.28 / 264.06 / 392.62 (L117) | NII + other income - opex | derived; PR R065-R071 | PASS |
| PPOP - provisions = PBT | ties (L126) | 205.08-27.08 = 178.00; 187.54-34.06 = 153.48; 138.99-31.52 = 107.47; 576.28-115.27 = 461.01 | Res R043-R048, R073-R078 | PASS |
| Total expenses Q2 FY27 | 541.79 (L126) | 288.34+27.08+126.54+15.41+84.42 = 541.79 | Res R067 (L230) | PASS |
| C/I Q2 FY27 / Q1 / Q2 FY26 / FY26 / H1 FY27 | 52.47% / 52.83% / 56.86% / 57.23% / 52.64% (L137, L379, L394) | 226.37/431.45; 210.02/397.56; 183.16/322.15; 771.01/1,347.29; 436.39/829.01 | Deck R855-R860; PR R143 | PASS |
| EPS misprint test | implied 3,673 lakh shares; H1 3,748; capital 3,751; Q2 derived 3.49 (L124, L128) | 13,075/3.56 = 3,672.8; 24,513/6.54 = 3,748.2; 37,514/10 = 3,751.4; 6.54-3.05 = 3.49 | Res R103, R106, R169, R175, R176, R178 (L236, L251, L254) | PASS |
| Credit cost, company basis, Q1 / Q2 | 0.78% / 0.59% (L138) | 136.24/17,561 = 0.776%; 108.32/18,393.5 = 0.589% | Res R043-R044; Deck R913, R914, R917 | PASS |
| Credit cost, avg-AUM basis, Q1 / Q2 | 0.66% / 0.50% (L139) | 136.24/20,644.5 = 0.660%; 108.32/21,585.5 = 0.502% | Deck R426-R428 | PASS |
| Credit cost H1 FY27 annualised | 0.69% (L196) | 122.28/17,707.5 = 0.691% | Res R046; Deck R914, R917 | PASS |
| FY26 credit cost on avg AUM | 0.641% (L154) | 115.27/17,982.5 = 0.641% | Res R048; Deck R422, R423 | PASS |
| RoA Q1 / Q2 derived | 2.61% / 2.84% (L146) | 457.52/17,561 = 2.605%; 523.00/18,393.5 = 2.843% | Res R103, R104 | PASS |
| RoE Q1 / Q2 derived | 15.43% / 16.96% (L147) | 457.52/2,964.43 = 15.43%; 523.00/3,083.86 = 16.96% | Res R420-R422 | PASS |
| YoY: NII / core NII / PPOP / PBT / PAT | +37.4% / +40.9% / +47.6% / +65.6% / +63.1% (L214-L228) | 1.3737; 1.4095; 1.4755; 1.6563; 1.6313 | Res; PR R017, R019 | PASS |
| PPOP/NTI YoY and QoQ | 43.14% to 47.53%, +439 bps; Q1 47.17%, +36 bps (L217, L233) | 138.99/322.15; 205.08/431.45; 187.54/397.56 | Deck R858, R859 | PASS |
| D&A / finance cost / interest income YoY | +18.0% / +34.8% / +36.3% (L218-L219) | 15.41/13.06; 288.34/213.84; 692.01/507.70 | Res R055, R057, R037, R039, R001, R003 | PASS |
| Treasury (FV gain + other income) | 5.70 to 4.66, -18.2% (L222) | 5.09+0.61; 4.28+0.38; 0.8175 | Res R013, R015, R025, R027 | PASS |
| Core PBT and ex-DA core PBT YoY | 101.77 to 173.34, +70.3%; 95.17 to 174.54, +83.4% (L226) | 107.47-5.70; 178.00-4.66; then -6.6 / +1.2 | Res R073, R075; PR R025, R027 | PASS |
| ETR Q2 FY26 / Q2 FY27; ETR cost | 25.42% / 26.54%; -2.00 Cr (L235) | 27.32/107.47; 47.25/178.00; 1.12% x 178.00 = 1.99 | Res R079, R081 | PASS |
| Main wedge, core PBT growth (+70.3%) vs PAT growth (+63.1%) | "ETR is the main wedge" (L235) | Treasury shortfall vs core growth: 4.66 - 5.70 x 1.7033 = -5.05 Cr pre-tax, -3.71 Cr post-tax (4.7 pp). ETR: 183.05 x -1.12% = -2.05 Cr (2.5 pp). Sum -5.76 = 130.75 - 80.15 x 1.7033. Treasury is the main wedge. | Res R013, R015, R025, R027, R073, R075, R079, R081 | FAIL (F3) |
| Step 3 Q1 FY26 derived row | NII 268.16; C/I 58.21%; PPOP 125.07; prov 24.72; PAT 75.01; core 94.39 (L245) | H1 FY26 - Q2 FY26 in each line; core 100.35 - (5.31+0.65) = 94.39 | Res R005, R041, R047, R107, R017, R029 | PASS (cell wording: STYLE S1) |
| Step 3 Q3+Q4 FY26 average | NII 333.87; C/I 56.99%; PPOP 156.11; prov 29.52; PAT 94.22 (L247) | (FY26 - H1 FY26)/2 in each line | Res R006, R048, R108 | PASS |
| Q1 FY27 core PBT | 151.91 (L248) | 153.48 - (1.25+0.32) | Res R014, R026, R074 | PASS |
| QoQ PBT distortion | +24.52: DA +11.7 (48%), provisions +6.98 (28%), core +5.75 (23%) (L253) | 47.7%, 28.5%, 23.4%; residual 0.09 rounding | PR R018, R019, R026, R027 | PASS |
| H1 run-rate | PAT +6.7%; PPOP +4.5% (L254) | 130.75/122.565; 205.08/196.31 | Res R103, R106 | PASS |
| Q3 implied PBT at Q1 provisions | 171.02 (L255) | 205.08-34.06 | Res R044 | PASS |
| PPOP growth for flat Q3 PAT at Q1 provisions | "about 4%" (L255) | (178.00+34.06)/205.08 = 1.0340: 3.4% | Res R073, R044 | FAIL (F1) |
| YoY bridge | +117.60 -7.80 -0.51 -43.21 +4.44 = +70.53; shares 166.7 / -11.1 / -0.7 / -61.3 / 6.3%; tax -17.93 -2.00; PAT +50.60 (L265-L274) | sum 70.52 (0.01 rounding); 70.53 x 25.42% = 17.93; 47.25-27.32 = 19.93 | Res, PR R017-R027 | PASS |
| QoQ bridge | +20.0 +11.7 +2.10 -16.35 +6.98; tax -8.15; ETR 25.48%; PAT +16.37 (L280-L287) | sum 24.43 vs 24.52 (0.09 rounding); 39.10/153.48 = 25.48% | Res, PR | PASS |
| Coverage sensitivity | ECL 262.8 vs 243.5; gap 19.3; credit cost 46.4, about 1.0%; post-tax 14.5, 88% (L289) | 15,381x0.34% + 587x16.53% + 296x38.36% = 262.88; gap 19.38; 46.46 x4 / 18,393.5 = 1.01%; 19.38 x (1-25.17%) = 14.50; 14.50/16.37 = 88.6% | Deck R756-R796 | PASS |
| Total ECL / AUF | 1.37% to 1.50%; stock +21.8 vs charge 27.1 (L290) | 221.7/16,237 = 1.365%; 243.5/16,264 = 1.497% | Deck R792-R796; PR R075 | PASS |
| Deferred-tax ETR effect; current tax share | 298 bps / 313 bps; 29.53% (L297) | 5.31/178.00; 4.80/153.48; 52.56/178.00 | Res R085, R097, R098 | PASS |
| DTA tie | +16.75 ties to P&L plus OCI deferred tax (L297) | 26.13-9.38 = 16.75 = 10.11 + 0.42 + 6.22 | Res R209, R210, R100, R124, R154 | PASS |
| Stage 2 / PCR / CRAR moves | +34.6%, -392 bps; +51.7% YoY; PCR -299 bps; CRAR +25 / -144 bps (L223, L310-L320) | 587/436; 16.53-12.61; 587/387; 38.36-35.37; 20.96-20.71; 22.40-20.96 | Deck R767-R778; Res R424-R426, R440-R441 | PASS |
| Off-book block | AUM +899; AUF +27; gold +726 / -52; gold off-book 15.3% to 20.9%; total 23.2% to 26.2%; x2.05; borrowings -0.6%; other FL +116% (L326-L334) | 15.35% / 20.94%; 23.18% / 26.19%; 1,085/530; 14,602/14,696; 468.19/216.38 | Deck R639-R661, R679-R680, R933-R934; Res R241-R242 | PASS |
| Cash quality | OCF pre-loan build +1,124.27; cash -42% (L336) | -718.88+1,843.15; 773.68/1,339.73 = 0.5775 | Res R306, R290, R189, R190 | PASS |
| D/E headroom | 1.39x NW, about Rs 4,399 Cr (L344) | (6-4.61) x 3,164.96 = 4,399.3 | Res R388, R420, R544 | PASS |
| NW and borrowings YoY | +16.8% / +42.7% (L344) | 3,164.96/2,709.77; 14,602/10,230 | Res R420, R423; Deck R932, R934 | PASS |
| Leverage share of RoE rise | about half (L344) | ln(6.0/5.0) / ln(17.0/12.0) = 52% | Deck R1062-R1064, R1066-R1068 | PASS |
| Gold metrics | AUM +15.1% H1; tonnage +2.4%; AUM per tonne 924 vs 606; per branch 16.9 (L199-L200, L364, L393) | 11,917/10,352; 12.9/12.6; 11,917/12.9; 6,731/11.1; 11,917/706 = 16.88 | Deck R439-R443, R487-R491, R496 | PASS |
| Entity AUM | +9.3% H1; +4.25% QoQ; compounds to +18.8% (L201) | 22,035/20,153; 22,035/21,136; 1.0934 x 1.0425^2 = 1.1884 | Deck R426-R428 | PASS (status conflict: C2) |
| Gold AUM Q2-pace FY27 | about +30.5% (L415) | 1.1512 x 1.0649^2 = 1.3054 | Deck R441-R443 | PASS (status contested: M4) |
| Tonnage Q2-pace FY27 | about +5.7% (L416) | 5.6% unrounded; 5.7% on the rounded 1.6% QoQ | Deck R489-R491 | PASS (rounding) |
| Non-gold AUM H1 | +3.2% (L418) | 10,118/9,801 = 1.0323 | Deck R431, R433 | PASS |
| ST LAP FY24-FY26; MT LAP H1 | -39%; 1,174 (L418-L419) | 904/1,475 = 0.613; 529+645 | Deck R473-R474 (XC values) | PASS |
| TTM PAT / TTM EPS / P/E / P/B / zone vs BVPS | 433.57; 11.58; 13.6x; 1.86x; 0.91x (L433, L447, L449) | 343.60-155.16+245.13; 9.20-4.16+6.54; 157/11.58; 157/84.4; 77/84.4 | Res R106-R108, R178-R180; Deck R060 | PASS (CMP 157 is a Notion input, not auditable here) |
| Monitorable targets | 13.86-14.11 t; Rs 24,184-24,587 Cr (L549-L550) | 12.6 x 1.10 / 1.12; 20,153 x 1.20 / 1.22 | Deck R423, R489 | PASS |
| Note 8 roll-forward; share of AUF | 4,221 lakh; 0.26% (L76) | 4,697-91-385; 42.21/16,264 | Res R373-R385 | PASS |
| Computed TOL/ATNW | 4.79x Mar-26; 4.90x Sep-26 (L508) | (13,900.35+48.33)/(2,926.10-9.38-3.62-0.27) = 4.79; 15,375.40/(3,164.96-26.13-3.22-0.57) = 4.90 | Res R210-R260, R518 | PASS |
| Security cover | 1.24x (L71) | 14,998.92/12,077.26 = 1.2419 | Res R501, R515, R519 | PASS |
| PR SF gap | 7.5% (L517) | (3,165.0-2,926.1)/3,165.0 = 7.55% | PR R107, R111 | PASS |
| Prior-question status count | 0 of 13 full; 7 partial; 6 not addressed (L190) | Partial: rows 1, 2, 5, 6, 7, 8, 10, AR-1 = 8. Not addressed: rows 3, 4, 9, AR-2, AR-3 = 5. | review L176-L188 | FAIL (F2) |
| Filing vs ex-DA interest income | "reconcile exactly" (L106) | 644.57+12.9 = 657.47 vs 657.4 printed | Res R002; Deck R947; PR R002 | PASS (wording: STYLE S2) |

Independent test of the XC corrections A4 adopted (XC itself is outside my input set):
- OCI signs: Q1 OCI (4,666) = (269) + (4,397), and (4,397) = (5,851) + 213 + (271) + 1,512. Q2 FY26 (1,237) = (2,005) + 352 + 416. H1 FY27 (2,004) = (121) + [(6,470) + (112) + 4,077 + 622]. H1 FY26 (457) = (783) + 173 + 153. All tie (Res R110-R162, L237-L249). XC holds.
- Deferred tax H1 FY26: 5,266 - 5,336 = (70) (Res R083, R089). XC holds; A1's (170) is a text-layer misread (L235).
- Slide 22: FY26 MT LAP 2,180 + ST LAP 904 = 3,084 = Deck R406 non-gold disbursement. Quarterly MT + ST tie to R397-R401 in all 5 quarters. XC holds.
- Slide 25: P&L-implied CoB Q2 FY27 = 288.34 x 4 / avg(14,696, 14,602) = 7.87%. Q1 = 272.69 x 4 / avg(13,484, 14,696) = 7.74%. Daily CoB 7.79% (Deck R610). These support CoB 7.9%, not A1's 8.8%. XC holds.

---

## AUDIT 3. ADVERSARIAL READ

The three most positive claims, each countered from the same extracted text.

### Claim 1: "Headline is strong and real at the YoY level ... The YoY gain is recurring in source" (review L234, L294, L751)
Bear counter: the YoY engine is gold, and most gold growth is gold price.
- Gold AUM rose 77% YoY, 6,731 to 11,917 (Deck R439, R443). Gold supplied Rs 5,186 Cr of the Rs 5,899 Cr AUM rise, 88% (non-gold 9,405 to 10,118, R429, R433).
- Gold AUM growth decomposes as follows:
  - tonnage +16.2%, 11.1 to 12.9 t (R487, R491);
  - portfolio LTV +10.2%, 61.7% to 68.0% (R497, R501);
  - implied gold value per gram about +38%: 1.7705 / (1.1622 x 1.1021) = 1.383.
- On a log basis that is about 57% price, 17% LTV and 26% grams.
- The growth was also funded by leverage. Borrowings rose 42.7% and net worth 16.8% (Deck R068, R058).
- So "recurring" holds only at today's gold price and LTV.

Survives: YES. Already in A4: YES, in substance. See the Brief §2 L616 ("Most of that came from a higher gold price and higher loan-to-value"), flag 5 (L577) and 5.5C candidate 2 (L364). Graft: none of substance. Add a cross-reference qualifier at L294 (STYLE S5).

### Claim 2: "Coverage of the whole book rose" (bull counter-observation, review L290; analyst note L751)
Bear counter: the whole-book rise sits in Stage 1. The stressed buckets got thinner cover.
- ECL build by stage, Q1 to Q2 FY27:
  - Stage 1: +12.0 Cr (52.8 to 64.8, Deck R762, R763). The Stage 1 book shrank Rs 168 Cr (15,549 to 15,381, R756, R757).
  - Stage 2: +2.1 Cr (72.0 to 74.1, R774, R775) on +Rs 151 Cr of assets (436 to 587, R768, R769).
  - Stage 3: +7.9 Cr (96.8 to 104.7, R786, R787) on +Rs 44 Cr (252 to 296, R780, R781).
- Stage 1 took 55% of the Rs 21.8 Cr build.
- The Rs 195 Cr of new Stage 2 + Stage 3 assets received Rs 10.0 Cr, a 5.1% marginal coverage.
- Stressed-book coverage fell from 24.5% ((72.0+96.8)/(436+252)) to 20.2% ((74.1+104.7)/(587+296)).
- The 1.37% to 1.50% total ratio does not show that stress is better covered. It shows that more provision went to performing loans.
- This weakens reading (A) "mix shift" as the comfort case. It leaves reading (B) open.

Survives: YES. Already in A4: NO. A4 does not split the build by stage. Graft required at the Step 4 memo (L290), flag 3 (L575) and the Q1 rationale (L487). Finding M3, loop A4.

### Claim 3: "Gold AUM +25-30% FY27 (base Mar-26, price flat): ON TRACK; Q2 pace compounds to about +30.5%" (review L199, L415)
Bear counter: on the trigger's own "price flat" condition, the pace is not on track.
- Q2 gold AUM rose 6.49% (11,191 to 11,917, Deck R442, R443).
- Tonnage rose about 1.6% (12.7 to 12.9 t, R490, R491). LTV was flat (67.9% to 68.0%, R500, R501).
- This implies gold value per gram rose about 4.7% in one quarter. The range is about 3.8-5.5% because tonnage is rounded to 0.1 t. About 70% of Q2 growth was price.
- H1 growth (+15.1%) came from LTV, 60.9% to 68.0% (+11.7%, R499, R501), and tonnage (+2.4%). Price contributed about +0.7%.
- The LTV lever is nearly used up. Portfolio LTV of 68.0% is 4.1 pp below the average origination LTV of 72.1% (Deck R327, L473).
- Price-flat and LTV-flat paths for FY27:
  - H2 growth rides tonnage. At the Q2 rate of 1.6% per quarter, FY27 is 1.1512 x 1.016^2 = +18.8%.
  - Even if the tonnage guide is met (13.86-14.11 t), FY27 is only +23.7% to +25.9%.
- So the +30.5% compounding assumes about 20% a year gold-price inflation. The trigger excludes that.

Survives: YES. Already in A4: NO. A4 names "Growth price/LTV-led" as killing evidence but still rates the trigger ON TRACK. It never tests the price-flat condition. Graft required: the status at L199 and L415 becomes "AT RISK: on track only with a rising gold price or LTV; price-flat pace about +19% to +26%". Finding M4, loop A4. (Loop 1 note: this status wording was too strong. See C3 in the re-audit.)

### Additional positive claim tested: "De-leverage ('we hope') ... DELIVERED in Q2, via assignment" (review L202) and "ON TRACK" (L423)
Bear counter:
- Sep-26 D/E is 4.61x. Mar-26 D/E was also 4.61x (Res R390, L483). So H1 net de-leverage is nil.
- The Q2 fall only reversed Q1's rise to 4.89x.
- On the average basis, leverage rose from 5.9x to 6.0x in Q2 (Deck R1063, R1064). A4 flags this rise itself as LEVERAGE-LED-ROE.

Survives: YES. Already in A4: NO. Finding M5, loop A4.

### MANDATORY ACQUISITION-ECONOMICS PROBE
Not triggered. No document describes an acquisition, a business purchase or a stake buy by the company. Evidence:
- Note 10(iii) and (iv): no loans acquired by assignment and no stressed loans acquired (Res L539-L540).
- Annexure I shows Goodwill as NA (Res L761).
- The only "consideration" line is a disposal: 48 NPA accounts sold to ARCs for Rs 0.03 Cr at nil NBV (Res L524-L529). Its principal-outstanding cell is blank, so no price-to-value multiple can be computed (NOT FOUND).
- "True North joins in as a strategic Partner" (Deck L370-L371, R263) is a historical inbound investment into Fedfina. It carries no price and no earnings figure.
- Treasury purchases (G-secs, mutual funds, Res L371-L376) and PPE purchases are not acquisitions.
- No multiple to state.

---

## FINDINGS (tagged)

### FACTUAL (loop)
- F1 (A4). Review L255: "A flat PAT print in Q3 needs either PPOP growth of about 4%". Recomputed: (178.00 + 34.06) / 205.08 = 1.0340, which is 3.4% (Res R073, R044). Fix the figure to 3.4%.
- F2 (A4). Review L190: "0 of 13 fully answered, 7 partial, 6 not addressed". The table at L176-L188 shows 8 partial (rows 1, 2, 5, 6, 7, 8, 10, AR-1) and 5 not addressed (rows 3, 4, 9, AR-2, AR-3). Fix the count.
- F3 (A4). Review L235: "ETR is the main wedge between PBT and PAT growth", given in answer to the core-PBT (+70.3%) vs PAT (+63.1%) gap.
  - Recomputed treasury wedge: 4.66 - 5.70 x 1.7033 = -5.05 Cr pre-tax, -3.71 Cr post-tax (4.7 pp).
  - Recomputed ETR wedge: -2.05 Cr (2.5 pp).
  - A4 compared the absolute treasury fall (-1.04) with the ETR cost (-2.00). That comparison does not explain a growth-rate gap.
  - Fix: treasury not keeping pace with core growth is the main wedge (64%). ETR is the second wedge (36%).

### MISSING (loop)
- M1 (A2). Results fulltext L525 "Aggregate principal outstanding of loans transferred" and L526 "Weighted average residual tenor of the loans transferred" are labelled Note 10(I) rows with blank cells. A blank cell is not a nil "." cell. Neither row has an R-ID, a ledger row or an MFS entry. Add MFS-4 and MFS-5 with a NOT-DISCLOSED flag. A4 already covers the content (review L79 "principal and tenor rows blank"; Q13 L504), so A3 needs only a reviewed-no-new-finding mark.
- M2 (A2). Results fulltext L812 (Annexure I) and L932, with its mark at L934 (Annexure II), are company signature blocks. Neither is enumerated. The signature count is 7, not 5 (ledger L9, L522-L528). Add both.
- M3 (A4). Surviving bear counter to Claim 2. Stage 1 took Rs 12.0 Cr of the Rs 21.8 Cr ECL build. Stressed assets +Rs 195 Cr got +Rs 10.0 Cr (5.1%). Stressed coverage fell from 24.5% to 20.2% (Deck R756-R787). Graft at L290, flag 3 (L575) and Q1 (L487).
- M4 (A4). Surviving bear counter to Claim 3. Q2 gold AUM growth was about 70% price. H1 growth was LTV-led. Portfolio LTV 68.0% vs origination LTV 72.1%. The price-flat FY27 pace is about +19% to +26% (Deck R327, R441-R443, R489-R491, R499-R501). Re-grade L199 and L415.
- M5 (A4). The de-leverage rows L202 and L423 omit Mar-26 D/E 4.61x (Res R390) and the rise in average leverage to 6.0x (Deck R1064). H1 net de-leverage is nil. Add both.
- M6 (A4). Annexure II row L84 and monitorable 9 (L553) read TOL/ATNW 4.61x as a Sep-26 figure. Footnotes R743 and R744 (Res L843-L844, L868-L869) state it is "Calculated based on audited figures i.e. for 31st March 2026". Only the 07066 ratios use 30-Sep-2026 figures (R745, L893). Graft the basis date. Q17 (L508) should compare the filed 4.61x with the Mar-26 computed 4.79x.

### CONTRADICTION (loop)
- C1 (A4). Q2 sell volume is unreconciled.
  - Brief L608 ("Fedfina sold Rs 1,085 Cr of loans to other lenders"), L181, L331, L363 and Q4 L490 use the deck incremental sell-down of Rs 1,085 Cr (Deck R680, L842).
  - Notes row 10(II) L80 and L90 use the filed assignment of Rs 876.89 Cr (Res R472, L533).
  - The Rs 208 Cr gap is never named.
  - Also, L423 says "Via DA, not CLM; CLM not reported" and L181 says "no CLM data". But the deck funding legend lists both "Direct Assignments" and "CLM" (Deck L795-L798, R587-R593). The Rs 208 Cr excess over filed DA has no stated route.
  - Fix: state both figures and the gap as NOT DISCLOSED. Replace "Via DA, not CLM" with "filed DA Rs 876.89 Cr of a Rs 1,085 Cr sell-down; balance route NOT DISCLOSED; CLM is a listed funding source of unresolved size". Add the gap to the Q4 or Q5 question.
- C2 (A4). The entity AUM +20-22% trigger has two statuses on the same derived +18.8% pace: "ON TRACK at lower edge" (L201) and "DELAYED (marginal)" (L417). Q7 (L493) counts it as behind ("3 of 5 run behind"). +18.8% is below the 20% floor. Use one status (DELAYED) in all three places.

### STYLE (logged, no loop)
- S1. L245: the Q1 FY26 core PBT cell says "ND (treasury split ... not derivable" and then gives "core 94.39 derived". The figure is derivable: 100.35 - (5.31 + 0.65) = 94.39. Replace ND with 94.39.
- S2. L106: "the two reconcile exactly". Q1 FY27 gives 644.57 + 12.9 = 657.47 vs 657.4 printed (Deck R947, PR R002). Write "reconcile within Rs 0.1 Cr".
- S3. L296 says "Finance cost per unit is flat (CoB 7.7% to 7.9%)" and Brief L619 says "Funding costs are stable". Slide-25 CoB rose 20 bps and P&L-implied CoB rose 13 bps (7.74% to 7.87%). Only the daily I-GAAP series is flat (7.80% to 7.79%). Write "up 13-20 bps QoQ on two of three measures; spread still widened 8.6% to 8.8%".
- S4. The ROA +20-30 bps trigger is "ON TRACK" at L197 and "FIRED (on number)" at L420. Use one label.
- S5. L294 "recurring in source": add "at the current gold price and LTV". The decomposition is already in Brief §2 L616, flag 5 and 5.5C.
- S6. Bull/bear symmetry (Rule J). Gold Stage 3 was 0.4% in Q2 FY26 (Deck R737). The 0.1% to 0.5% QoQ move (L312, L577) is +10 bps YoY. State both.
- S7. The A1 PR fulltext header says "doctype: presentation" (PR L3). The A2 PR ledger YAML carries the same label. It should be pressrelease.
- S8. The A2 presentation ledger YAML has "line_items: 1", but its count test has no such category.
- S9. A1 left decorative text uncaptured: 11 slide taglines (Deck L188, L263, L287, L316, L345, L387, L413, L483, L515, L555, L1242), the slide 10 "Target Segment" bullet (L248), "Nine ... login solutions" (L1135) and PR "Encl.: a/a" (PR L57). None carries an analytical number.
- S10. Four NA-only Annexure I template rows are uncaptured: Goodwill (Res L761), Inventories (L768), other debt sharing pari-passu charge (L788) and Other Debt (L790). They hold no values.

---

## VERDICT (loop 0)

VERDICT: INCOMPLETE.

- Failing agent (first in chain): A2. Two MISSING items (M1, M2): four fulltext rows that the ledger lacks.
- A3: no new forensic work. Mark the four new ledger rows reviewed; their content is already in A3-02 and review L79.
- A4: nine items.
  - FACTUAL: F1, F2, F3.
  - MISSING: M3, M4, M5, M6. M3 and M4 are surviving bear counters that must be grafted before save.
  - CONTRADICTION: C1, C2.
- The deliverable gate passes. All five brief parts are present.
- The arithmetic is otherwise clean on every recomputed metric.
- STYLE notes S1-S10 are logged only.

## STYLE NOTES (loop 0)
S1-S10 above. Recorded for the record. No re-run.

Loop-0 YAML block (SUPERSEDED, first by the Re-audit loop 1 block and now by the Re-audit loop 2 block at the end of this file; kept as the record, fenced as text so that no parser reads it as the current block):

```text
stage: A5-adversary
company: "FEDFINA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
loop_back_to: "A2"
findings: F1, F2, F3 (factual, A4); M1, M2 (missing, A2); M3, M4, M5, M6 (missing, A4); C1, C2 (contradiction, A4); S1-S10 (style)
gap: "A2: add ledger rows for Res fulltext L525, L526, L812, L932. A3: mark them reviewed. A4: graft M3, M4, M5, M6; resolve C1, C2; fix F1, F2, F3."
```

---

## RE-AUDIT LOOP 1

Date: 2026-10-17 | model: claude-opus-5-5
Revised artefacts read:
- work/review_fedfina_q2fy27.md (now 810 lines; line numbers below refer to the revised file);
- work/ledger_results_fedfina_q2fy27.md.

The coordinator also lists work/forensics_results_fedfina_q2fy27.md as revised. I did not open it. A5 input discipline excludes A3's reasoning, so I re-derived each item from the extracts. Same A1 inputs as loop 0. No source PDF, no inputs/, no git.

### R0. Deliverable completeness (re-run)
- narrative: PRESENT. L633-L648, 15 lines; the new stressed-cover, sell-down and D/E lines are added.
- sector: PRESENT. L650-L658.
- business_model: PRESENT. L660-L668.
- competition: PRESENT. L670-L675.
- forward_map: PRESENT. L677-L687; 9 dated catalysts, each with a bull and a bear fork. The new gold AUM item is at L683.

Gate: PASS.

### R1. Disposition of every loop-0 finding

| ID | Type | Agent | Loop-0 gap | Loop-1 evidence | Status |
|---|---|---|---|---|---|
| M1 | MISSING | A2 | Res L525, L526 blank Note 10(I) rows not enumerated | Ledger L532-L533 add MFS-4 and MFS-5 with flag "NOT DISCLOSED"; YAML L630 lists both | RESOLVED |
| M2 | MISSING | A2 | Res L812, L932 signature blocks not enumerated | Ledger L534-L535 add SIG-6 and SIG-7; count test L11 and YAML L625 now say signatures 7 | RESOLVED |
| A3 confirm | n/a | A3 | Mark the four new rows reviewed | Review L17 marks all four read and reviewed, no new finding; L80 and Q13 (L537) cite L525 | RESOLVED (on A4's record; the A3 file was not opened) |
| F1 | FACTUAL | A4 | "about 4%" | L256: 3.4%, with the formula | RESOLVED |
| F2 | FACTUAL | A4 | 7 partial / 6 not addressed | L191: 8 partial, 5 not addressed, rows listed; flag 15 (L621) aligned | RESOLVED |
| F3 | FACTUAL | A4 | ETR called the main wedge | L236: treasury Rs 3.71 Cr post-tax, 4.7 pp, 64%; ETR Rs 2.05 Cr, 2.5 pp, 36%. Recompute: 5.70 x 1.7033 = 9.71; 9.71 - 4.66 = 5.05; x 0.7346 = 3.71. PASS. | RESOLVED |
| M3 | MISSING | A4 | Stage-wise ECL build | L296-L304 table recomputes: Stage 2 2.1/151 = 1.4%; Stage 3 7.9/44 = 18.0%; stressed 10.0/195 = 5.1%; 168.8/688 = 24.5%; 178.8/883 = 20.2%. Also grafted at L308-L309, L331, L362, Q1 L520, flag 3 L609, brief L641. | RESOLVED |
| M4 | MISSING | A4 | Gold AUM price-flat decomposition | L436-L443 table recomputes: YoY 68.0/61.7 = +10.2%; H1 68.0/60.9 = +11.7%; Q2 implied price +4.7%; 1.047^4 = 1.20. Re-graded AT RISK at L200 and L447; flag 6 L612; L467; brief L653-L654; forward map L683. | RESOLVED (wording refined in C3) |
| M5 | MISSING | A4 | Mar-26 D/E and average leverage | L151, L182, L203, L367, L455, Q6 L525, flag 10 L616, brief L645 | RESOLVED |
| M6 | MISSING | A4 | R743/R744 basis date | L85, monitorable 9 L587, Q17 L541 (compares the filed 4.61x with 4.79x on the same Mar-26 figures) | RESOLVED (anchor typo at L85: S11) |
| C1 | CONTRADICTION | A4 | Rs 1,085 Cr vs Rs 876.89 Cr, and the CLM wording | L81, L182, L352, L357 (UNRECONCILED, route NOT DISCLOSED, CLM listed as a source of unresolved size), L386, L454-L455, Q4 L523, new Q31 L555, flag 8 L614, brief L644 and L664. "Via DA, not CLM" is removed. 1,085 - 876.89 = 208.11. PASS. | RESOLVED |
| C2 | CONTRADICTION | A4 | Entity AUM status conflict | DELAYED at L202, L449 and Q7 L526 | RESOLVED |
| S1-S6 | STYLE | A4 | as logged | S1 L246; S2 L107; S3 L171, L315, L339, L656; S4 L198 and L452 both ON TRACK; S5 L313; S6 L332, L364, flag 5 L611 | RESOLVED |
| S7-S10 | STYLE | A1/A2 | as logged | The PR and presentation ledgers and A1 files were not revised | OPEN, logged only, no loop |

### R2. Coverage re-run (results ledger)
- Fresh fulltext counts versus the revised ledger:
  - notes 36 / 36;
  - line items 339 groups plus MFS-4/5 for L525/L526;
  - ZERO_STANDING 38 / 38;
  - agenda 6 / 6;
  - auditor paragraphs 19 / 19;
  - entities 38 / 38;
  - signatures 7 / 7;
  - forward and dates 8 / 35.
- Missing from ledger: none. Orphan rows: none; the four new rows are cited at review L17, L80 and L537.
- The presentation and PR ledgers are unchanged from loop 0 and pass.
- Coverage: PASS.

### R3. Arithmetic re-run (new and changed figures only; unchanged rows pass as in loop 0)

| Metric | A4 value (revised line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Sell-down gap | Rs 208.11 Cr (L81, L352) | 1,085 - 876.89 = 208.11 | Deck R680; Res R472 | PASS |
| Core-PBT-to-PAT gap | Rs 5.76 Cr, 7.2 pp (L236) | 80.15 x 1.7033 = 136.52; 136.52 - 130.75 = 5.77 (0.01 rounding); 70.3 - 63.1 = 7.2 | Res R103, R105 | PASS |
| Treasury wedge / ETR wedge | 3.71 (64%) / 2.05 (36%) (L236) | 5.05 x 0.7346 = 3.71; 183.05 x 1.12% = 2.05; 3.71 / 5.76 = 64% | Res R013, R015, R025, R027, R079, R081 | PASS |
| Flat-PAT PPOP growth | 3.4% (L256) | 212.06 / 205.08 = 1.0340 | Res R073, R044 | PASS |
| Stage-wise ECL table | as listed (L299-L304) | see R1, M3 | Deck R756-R787 | PASS |
| Stressed coverage change | -430 bps (L308, L331) | 24.53% - 20.25% = 428 bps | Deck R768-R787 | PASS (rounding) |
| Gold decomposition table | as listed (L439-L443) | see R1, M4; 6.49% QoQ; 4.1 pp = 72.1 - 68.0 | Deck R327, R441-R443, R489-R501 | PASS |
| Gold Stage 3 YoY | +10 bps (L332) | 0.5 - 0.4 | Deck R737, R739 | PASS |
| CoB moves | +20 / -1 / +13 bps; spread +20 bps (L339) | 7.9 - 7.7; 7.79 - 7.80; 7.87 - 7.74; 8.8 - 8.6 | XC values; Deck R609-R610; Res R037-R038 | PASS |
| Growth triggers DELAYED or WEAKENED | "5 of 10" (L476) | 6D L447-L456: DELAYED tonnage (L448), entity AUM (L449), 200 branches (L453), de-leverage (L455) = 4. WEAKENED mortgage (L450), co-lending (L454) = 2. Total 6 of 10, plus gold AUM AT RISK (L447). Flag 16 (L622, L799) lists these six. | review L447-L456 | FAIL (F4) |
| Q7 behind count | 3 of 5 (L526) | entity AUM, tonnage, branches behind; gold AT RISK | review L200-L202 | PASS |

### R4. Adversarial re-read
- The four loop-0 counters are now in the review. The coverage fork is re-weighed (L306-L310). The gold trigger is AT RISK. The de-leverage claim is NOT DELIVERED in H1 and DELAYED.
- No new unchallenged bull claim appears.
- The 8C bull threshold (L505) is stated as the bull fork only, next to a bear fork. That is acceptable.
- Rule J test on the new bear text: one overstatement (C3, below).
- Acquisition probe: still not triggered. No new purchase language appears.

C3 detail (CONTRADICTION, A4):
- Brief L653: "With a flat gold price, the FY27 gold guide of +25-30% looks out of reach; the flat-price path gives about +19% to +26%".
- The top of the quoted range (+25.9%) sits inside the 25-30% band. 6D (L447) grades the trigger AT RISK, not missed. The brief therefore contradicts its own range and the 6D status.
- Exact condition (derived):
  - At a flat price and flat LTV, gold AUM per tonne holds at 11,917 / 12.9 = 923.8 (Deck R443, R491).
  - The 25% floor is 10,352 x 1.25 = Rs 12,940 Cr (R441). That needs 12,940 / 923.8 = 14.0 t of FY27 tonnage.
  - 14.0 t is +11.2% on 12.6 t (R489), inside the top of the 10-12% tonnage guide. H1 tonnage growth was +2.4%.
- A5's loop-0 status wording ("on track only with a rising gold price or LTV", used at L200, L447, L612, L788) was also too strong. At a flat price, tonnage near the top of its guide reaches the floor.
- Fix:
  - L653: "is reachable at a flat price only if FY27 tonnage reaches about 14.0 t (+11.2%), against +2.4% in H1".
  - Keep AT RISK at L200, L447, L612 and L788, but state the same condition.

F4 detail (FACTUAL, A4):
- L476 Step 7 reads "5 of 10 growth triggers DELAYED or WEAKENED (6D)".
- Recount: 6 of 10 (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK.
- Fix the number. Flag 16 already lists the six correctly.

### R5. New STYLE notes (logged, no loop)
- S11. L85 anchors the 07066 D/E basis as "Res R543-R545, L893". R545 is the RPT row "Interest received FD/Current A/c". The basis rows are R543-R544 and R745. Correct the anchor.
- S12. The A2 results ledger YAML `missing_from_structured` (L630) lists MFS-1 to MFS-5 but omits SIG-6 and SIG-7. Section 7 (L534-L535) flags both MISSING_FROM_STRUCTURED. Add them for consistency.

### VERDICT (loop 1)
VERDICT: INCOMPLETE.

- Failing agent: A4 only.
  - F4 (FACTUAL): L476, the count 5 should be 6.
  - C3 (CONTRADICTION): L653 "out of reach" vs the quoted range and the 6D status; align the AT RISK condition at L200, L447, L612 and L788.
- Both are one-line text fixes. Neither changes the protocol verdict (PROCEED WITH FLAGS), the Decision Status or the flag set.
- No A2 or A3 work remains. The deliverable gate and coverage pass.
- All 11 loop-0 loop items and style notes S1-S6 are resolved.
- STYLE: S11 and S12 are new; S7-S10 stay open and logged.
- If the remediation cap bars a second cycle, carry F4 and C3 to the operator as open items, with the exact replacement text above.

### STYLE NOTES (loop 1)
S11 and S12 above. S7-S10 carried from loop 0, open, logged only. No re-run for any STYLE item.

Loop-1 YAML block (SUPERSEDED by the Re-audit loop 2 block at the end of this file; kept as the record, fenced as text so that no parser reads it as the current block):

```text
stage: A5-adversary
company: "FEDFINA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Growth triggers DELAYED or WEAKENED in the 6D table", a4_value: "5 of 10 (review L476)", recomputed: "6 of 10: DELAYED tonnage, entity AUM, 200 branches, de-leverage (L448, L449, L453, L455); WEAKENED mortgage, co-lending (L450, L454); plus gold AUM AT RISK (L447). Flag 16 (L622, L799) already lists these six.", source_line: "review L447-L456"}
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F4 (A4): Step 7 L476 '5 of 10 growth triggers DELAYED or WEAKENED' recounts to 6 of 10 (4 DELAYED, 2 WEAKENED) plus gold AUM AT RISK"
  missing: []
  contradiction:
    - "C3 (A4): Brief L653 says the +25-30% gold guide 'looks out of reach' at a flat gold price, but the same sentence gives a flat-price range of +19% to +26% whose top end (+25.9%) sits inside the band, and 6D L447 grades it AT RISK, not missed. Precise condition (derived, Deck R441-R443, R489-R491): at flat price and LTV, gold AUM per tonne is 923.8 (11,917 / 12.9); the 25% floor (Rs 12,940 Cr) needs FY27 tonnage of about 14.0 t (+11.2% on 12.6 t), inside the top of the 10-12% tonnage guide, vs +2.4% in H1. Align the AT RISK clause at L200, L447, L612, L788 to this condition (A5's loop-0 wording 'on track only with a rising gold price or LTV' was too strong)."
  style:
    - "S11 (new): L85 anchor 'Res R543-R545' should read 'Res R543-R544, R745'; R545 is the RPT FD-interest row"
    - "S12 (new): A2 results ledger YAML missing_from_structured omits SIG-6/SIG-7, which section 7 flags MISSING_FROM_STRUCTURED"
    - "S7 (carried, open): A1 PR fulltext header and A2 PR ledger YAML say doctype presentation"
    - "S8 (carried, open): A2 presentation ledger YAML line_items: 1 has no count-test category"
    - "S9 (carried, open): uncaptured decorative taglines (11 slides), slide 10 bullet, 'Nine' (Deck L1135), PR 'Encl.: a/a' (L57)"
    - "S10 (carried, open): four NA-only Annexure I template rows uncaptured (Res L761, L768, L788, L790)"
loop_back_to: "A4"
gap: "A4 only. (1) F4: review L476, change '5 of 10 growth triggers DELAYED or WEAKENED' to '6 of 10 (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK'. (2) C3: review L653, replace 'looks out of reach' with 'is reachable at a flat price only if FY27 tonnage reaches about 14.0 t (+11.2%), against +2.4% in H1'; align the AT RISK clause at L200, L447, L612 and L788 to the same condition. No A2 or A3 work remains."
style_notes:
  - "S11: L85 anchor R543-R545 to R543-R544, R745"
  - "S12: A2 results YAML missing_from_structured should list SIG-6/SIG-7"
  - "S7-S10 carried from loop 0, open, logged only"
analyst_note: "Loop 1 resolved all 11 loop-0 items (F1-F3, M1-M6, C1-C2) and style notes S1-S6. I re-checked each change against the extracts. The A2 ledger now carries MFS-4/MFS-5 and SIG-6/SIG-7, and the coverage re-run is clean. The A4 grafts recompute: the stage-wise ECL table, the gold decomposition, the treasury wedge, 3.4%, the 8/5 status count, and the Rs 208.11 Cr gap. Two new defects remain, both one-line A4 fixes. The Step 7 trigger count is wrong (6 of 10, not 5). The brief overstates the gold bear ('out of reach'), contradicting its own range, and Rule J holds bear claims to the same bar. Part of C3 corrects A5's own loop-0 wording: the exact flat-price condition is about 14.0 t of FY27 tonnage. Neither defect changes the protocol verdict (PROCEED WITH FLAGS), the Decision Status or any flag. If the loop cap bars a second cycle, carry F4 and C3 to the operator as open items. I did not open the revised A3 forensics file: input discipline excludes A3's reasoning."
```

---

## RE-AUDIT LOOP 2

Date: 2026-10-17 | model: claude-opus-5-5
Revised artefact read: work/review_fedfina_q2fy27.md (now 816 lines; line numbers below refer to this file).
Also read:
- the three A2 ledgers, which are unchanged since loop 1;
- results structured rows R388-R390, R543-R545 and R743-R745, and results fulltext L838-L897;
- presentation structured rows R327, R441-R443, R489-R501 and R756-R796.
Not opened: source PDFs, inputs/, A3 forensics. No git.

Edit footprint:
- The review grew from 810 to 816 lines. The 6 new lines are the LOOP 2 CHANGES block (L705-L709) plus one blank line.
- The body edits replaced text in place at L85, L200, L447, L476, L612 and L653. In the A4 YAML, the edits are at L794, L813 and L814.
- Body line numbers match loop 1. The A4 YAML moved down 6 lines (loop-1 L788 is now L794).

### R0. Deliverable completeness (re-run)
- narrative: PRESENT. L633-L648, 15 lines.
- sector: PRESENT. L650-L658. L653 was rewritten for C3.
- business_model: PRESENT. L660-L668.
- competition: PRESENT. L670-L675.
- forward_map: PRESENT. L677-L687. One make-or-break metric plus 9 dated catalysts, each with a Bull and a Bear fork.

Gate: PASS.

### R1. Disposition of the loop-1 items

| ID | Type | Loop-1 gap | Loop-2 evidence | Status |
|---|---|---|---|---|
| F4 | FACTUAL | L476 "5 of 10" | L476 now reads "6 of 10 (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK (6D)". 6D recount (L447-L456): DELAYED L448, L449, L453, L455 = 4; WEAKENED L450, L454 = 2; AT RISK L447 = 1; ND L451 = 1; ON TRACK L452, L456 = 2; total 10. Flag 16 (L622), YAML flag (L805) and Q7 (L526, "3 of 5 run behind ... gold AUM is at risk") agree. | RESOLVED (cell wording: S13) |
| C3 | CONTRADICTION | L653 "out of reach"; AT RISK clause at L200, L447, L612, L788 | L653: "reachable only if FY27 tonnage reaches about 14.0 t. That is +11.2% on 12.6 t, against +2.4% in H1". The range is kept and tied to the Q2 tonnage pace (+19%) and the full guide (+26%). L200, L447, L612, L794 and the A4 analyst note (L814) carry the same condition. Grep for "out of reach", "on track only" and "rising gold price": zero hits. | RESOLVED |
| S11 | STYLE | L85 anchor | L85 now cites "Res R543-R544, R745, L893". R543 = 4.61x D/E actual, 07066 (fulltext L891). R544 = 6x cap (L891). R745 = "Above ratios are calculated based on figures as on 30th September 2026" (L893-L894). R545 stays cited at L86 (RPT block R545-R573), so no orphan. L367, L587 and L777 already used R543-R544. | RESOLVED |
| S12 | STYLE | A2 YAML missing_from_structured | Results ledger L630 unchanged | OPEN, logged only |
| S7-S10 | STYLE | as logged | PR ledger L124 and presentation ledger L250 still say doctype "presentation". Presentation ledger L257 still has line_items: 1. A1 files unchanged. | OPEN, logged only |
| F1-F3, M1-M6, C1-C2, S1-S6 | mixed | resolved in loop 1 | Outside the loop-2 edit footprint. Spot-checked: L191 (8 / 5), L236 (wedge), L256 (3.4%), L296-L304 (stage table), L203 and L455 (de-leverage), L81 and L352 (Rs 208 Cr gap). Unchanged. | RESOLVED (carried) |

### R2. Coverage re-run
- The three A2 ledgers are unchanged since loop 1 (results ledger L2, L11, L532-L535, L625, L630). The loop-1 counts stand.
- Loop 2 removed one citation, R545 from L85. R545 stays cited at L86.
- Orphan rows: none. Missing from ledger: none.
- Coverage: PASS.

### R3. Arithmetic re-run (touched passages)

| Metric | A4 value (line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| 6D DELAYED or WEAKENED count | 6 of 10 (4 + 2), plus AT RISK (L476) | 4 + 2 = 6; with AT RISK 1, ND 1, ON TRACK 2 the table has 10 rows | review L447-L456 | PASS |
| Gold AUM per tonne, flat price and LTV | used for the 14.0 t condition | 11,917 / 12.9 = 923.8 | Deck R443, R491 | PASS |
| 25% floor | used for the 14.0 t condition | 10,352 x 1.25 = 12,940 | Deck R441 | PASS |
| Tonnage needed for the floor | about 14.0 t (L200, L447, L612, L653, L794, L814) | 12,940 / 923.8 = 14.007 t | derived | PASS |
| Tonnage growth needed | +11.2% on 12.6 t | 14.007 / 12.6 = 1.1117 (+11.1% on the rounded 14.0 t) | Deck R489 | PASS (rounding) |
| Position in the tonnage guide | 13.86-14.11 t (L682) | 12.6 x 1.10 = 13.86; 12.6 x 1.12 = 14.11. 14.0 t is inside the guide, near the top. | Deck R489 | PASS |
| H1 tonnage | +2.4% | 12.9 / 12.6 = 1.0238 | Deck R489, R491 | PASS |
| Flat-price path, Q2 tonnage pace | about +19% (L653) | 1.15118 x 1.016^2 = 1.1883 | Deck R441, R443, R490, R491 | PASS |
| Flat-price path, guide fully met | up to about +26% (L653) | 14.112 x 923.8 / 10,352 = 1.2593 | derived | PASS |
| Q2 price share of gold growth | about 70% (L612, L653, L794) | tonnage 12.9 / 12.7 = 1.01575; LTV 68.0 / 67.9 = 1.00147; price 1.06487 / 1.01724 = 1.0468; log share 0.0458 / 0.0629 = 73% | Deck R442, R443, R490, R491, R500, R501 | PASS |
| A4 note: QoQ PBT gain from DA and provisions | about 76% (L814) | (11.7 + 6.98) / 24.52 = 76.2% | PR R018-R027 | PASS |
| A4 note: cause of the total ECL / AUF rise | "rose only because Stage 1 took 12.0 of the 21.8 Cr build" (L814) | Q1 221.7 / 16,237 = 1.365%. Q2 243.5 / 16,264 = 1.497%. Rise 13.2 bps. With Stage 1 ECL held at 52.8: (243.5 - 12.0) / 16,264 = 1.423%, still +5.8 bps. Split: Stage 1 +7.4 bps (12.0 / 16,264); Stage 2 + 3 +6.0 to 6.1 bps (Rs 9.8-10.0 Cr; the stage rows and printed totals differ by Rs 0.1 Cr); denominator -0.2 bps. Body L304 gives Stage 1 as 55% of the build. | Deck R762-R763, R774-R775, R786-R787, R792-R796; review L294, L302-L304 | FAIL (F5) |

### R4. Adversarial re-read (touched passages)
- C3 softened a bear overstatement. The new text holds the bear claim to the same bar as a bull claim (Rule J). It names the one observation that separates the readings: FY27 tonnage against about 14.0 t.
- Overcorrection test: the brief does not now call the guide likely. It sets 14.0 t against +2.4% in H1 and keeps the +19% Q2-pace path. 6D keeps "The Q2-pace +30.5% needs about 20% a year gold-price inflation, which the trigger excludes" (L443). No new bull claim goes unchallenged.
- Forward map L683 was not edited. Its Bull fork is "tonnage growth carries it with the price flat". Its Bear fork is "it is met only if the gold price keeps rising". The bear world has tonnage below about 14.0 t (L682 bear: 12.9-13.3 t). At 13.3 t and a flat price the path is +18.7% (13.3 x 923.8 / 10,352). So the fork pair agrees with the 14.0 t condition. No finding.
- Rule J on the A4 analyst note, a field loop 2 edited: one bear overstatement (F5, below). The body (L304, L307) gives the right weight. The note does not.
- Acquisition probe: not triggered. Loop 2 added no purchase language.

F5 detail (FACTUAL, A4):
- L814 (A4 YAML analyst_note): "The coverage fork now leans bear: total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build".
- The extract does not support "only". With Stage 1 ECL held at its Q1 level, the ratio still rises from 1.365% to 1.423%. The stressed buckets added Rs 9.8-10.0 Cr, about 6 of the 13.2 bps rise (Deck R762-R796).
- The body is correct: "Stage 1 took Rs 12.0 Cr, 55% of the Rs 21.8 Cr build" (L304).
- The note opens "Loop 1 revision", so this clause most likely dates from loop 1. My loop-1 re-audit missed it. Loop 2 edited the same field.
- Fix: replace "total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build" with "total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build".
- Effect: no body number, flag, protocol verdict (PROCEED WITH FLAGS) or Decision Status changes. The coverage-fork weight at L309 stands.

### R5. New STYLE notes (logged, no loop)
- S13. The L476 cell names gold AT RISK twice and drops the noun "growth triggers". Suggested text: "AUM +36.6% YoY, off-book-led; 6 of 10 growth triggers DELAYED or WEAKENED (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK on a price-flat basis (6D)".
- S14. L814 has two wording issues.
  - (a) The note opens "Loop 1 revision." but carries loop-2 text. Write "Loop 2 revision."
  - (b) "Gold AUM growth fails its own price-flat condition: Q2 was about 70% price, H1 was LTV-led" reads as if the trigger had failed. H1 growth was in fact near price-flat (implied price +0.7%, L200). Suggested text: "Q2 gold AUM growth was about 70% price, so it did not meet the trigger's price-flat condition; H1 was LTV-led, and LTV sits 4 pp below origination".

### VERDICT (loop 2)
VERDICT: INCOMPLETE.

- Failing agent: A4 only.
  - F5 (FACTUAL): L814, the A4 YAML analyst_note. Change "rose only because" to "rose mainly because", and add "(55%)".
- F4, C3 and S11 are resolved. The loop-2 body edits introduced no new error. Every touched figure recomputes.
- The deliverable gate passes. Coverage passes. No A2 or A3 work remains.
- STYLE: S13 and S14 are new. S7-S10 and S12 stay open and are logged only.
- Cap note: F5 is a one-clause fix in the A4 YAML. It changes no figure in the body. If the remediation cap bars a further A4 cycle, carry F5 to the operator as an open item with the replacement text above.

### STYLE NOTES (loop 2)
S13 and S14 above. S7-S10 and S12 carried, open, logged only. No re-run for any STYLE item.

```yaml
stage: A5-adversary
company: "FEDFINA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "A4 analyst_note cause of the total ECL/AUF rise", a4_value: "'total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build' (review L814)", recomputed: "1.365% (221.7/16,237) to 1.497% (243.5/16,264), +13.2 bps. With Stage 1 ECL held at 52.8 the ratio is still 1.423% (231.5/16,264), +5.8 bps. Split: Stage 1 +7.4 bps; Stage 2+3 +6.0 bps (Rs 9.8-10.0 Cr); denominator -0.2 bps. Body L304 gives Stage 1 as 55% of the build.", source_line: "Deck R762-R763, R774-R775, R786-R787, R792-R796; review L294, L302-L304"}
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F5 (A4): review L814 (A4 YAML analyst_note) says total ECL/AUF 'rose only because Stage 1 took 12.0 of the 21.8 Cr build'. The extract does not support 'only': with no Stage 1 build the ratio still rises 1.365% to 1.423%, and the stressed buckets added Rs 9.8-10.0 Cr (about 6 of 13.2 bps). Body L304 is right (55%). The clause most likely dates from loop 1; A5's loop-1 re-audit missed it."
  missing: []
  contradiction: []
  style:
    - "S13 (new): L476 names gold AT RISK twice and drops 'growth triggers'; suggested text in the audit (R5)"
    - "S14 (new): L814 note opens 'Loop 1 revision' but carries loop-2 text; 'Gold AUM growth fails its own price-flat condition' reads as a failed trigger, and H1 was near price-flat (+0.7%); suggested text in the audit (R5)"
    - "S12 (carried, open): A2 results ledger YAML missing_from_structured (L630) omits SIG-6/SIG-7"
    - "S7 (carried, open): A1 PR fulltext header and A2 PR ledger YAML (L124) say doctype presentation"
    - "S8 (carried, open): A2 presentation ledger YAML line_items: 1 (L257) has no count-test category"
    - "S9 (carried, open): uncaptured decorative deck text (11 taglines, slide 10 bullet, 'Nine' at Deck L1135) and PR 'Encl.: a/a' (L57)"
    - "S10 (carried, open): four NA-only Annexure I template rows uncaptured (Res L761, L768, L788, L790)"
loop_back_to: "A4"
gap: "A4 only. F5: review L814 (A4 YAML analyst_note), replace 'total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build' with 'total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build'. No body number, flag, protocol verdict or Decision Status changes. Loop-1 items F4, C3 and S11 are resolved. No A2 or A3 work remains."
style_notes:
  - "S13: L476 cell wording (gold AT RISK stated twice; noun 'growth triggers' dropped)"
  - "S14: L814 note label 'Loop 1 revision' and the gold 'fails its own price-flat condition' wording"
  - "S7-S10 and S12 carried, open, logged only"
analyst_note: "Loop 2 fixed all three loop-1 items. F4: the 6D table recounts to 4 DELAYED and 2 WEAKENED of 10, plus gold AUM AT RISK, and L476 now says so. C3: the brief and every AT RISK clause carry the derived condition. At a flat price and LTV, AUM per tonne is 923.8, so the Rs 12,940 Cr floor needs 14.007 t. S11: L85 cites R543-R544 and R745, and R545 stays cited at L86. The review grew by exactly the 6-line change log, so the body edits were in place. One FACTUAL defect sits in A4's YAML analyst note, a field loop 2 edited. It says the total ECL/AUF rise came 'only' from Stage 1. With no Stage 1 build the ratio still rises 6 bps. The body (L304, 55%) is right. The clause most likely dates from loop 1, and my loop-1 re-audit missed it. Rule J holds this bear overstatement to the same bar as C3. The fix is one word. It changes no figure, flag, protocol verdict or Decision Status. If the cap bars a further A4 cycle, carry F5 to the operator as an open item."
```
