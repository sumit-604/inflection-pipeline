# A5 ADVERSARY / COMPLETENESS AUDIT: Tata Communications Limited (TATACOMM), Q2 FY27

Review under audit: runs/tatacomm-q2fy27/work/review_tatacomm_q2fy27.md (A4, 819 lines).
Inputs read: A1 fulltexts and structured files (results, presentation), A2 ledgers (results, presentation), A4 review. No source PDF and nothing under inputs/ was opened. A3 files were not read.
Model: claude-opus-5-5. Audit date 2026-10-17.

Anchor convention (same as A4). "L###" = line in extracted/tatacomm-results-q2fy27-fulltext.md. "P-L###" = line in extracted/tatacomm-presentation-q2fy27-fulltext.md. "R####" / "P-R###" = A1 structured rows. "rev L###" = line in the A4 review file. [DERIVED] = arithmetic on filed numbers.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in review | Content | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" (rev L686) | 6 paragraph lines, about 207 words, 22 sentences (rev L688-693) | PRESENT |
| 2. Sector intelligence | "### 2. Sector intelligence" (rev L695) | DC-to-DC demand, GPU, voice decline, DoT and Labour Code regulation (rev L697) | PRESENT |
| 3. Business-model intelligence | "### 3. Business-model intelligence" (rev L699) | Revenue mix, cost structure, Digital, Campaign Registry, model drift (rev L701) | PRESENT |
| 4. Competition intelligence | "### 4. Competition intelligence" (rev L703) | Moat, weak spots, peer data ND, concentration risk (rev L705) | PRESENT |
| 5. Forward map | "### 5. Forward map" (rev L707) | Make-or-break reading plus 9 catalysts, each with a Bull and a Bear fork (rev L709-718) | PRESENT |

Gate result: PASS. All five parts exist and carry real content. Five catalysts carry a date; four are "date ND" with the reason stated.

---

## 1. COVERAGE AUDIT

Method. I re-ran the enumeration on both A1 fulltexts myself (Grep plus a full read of all 1,569 results lines and 196 deck lines), then diffed against the A2 ledgers and the A1 structured ID ranges.

### 1A. Results filing

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Notes | 18 | 18 (19 note units: consolidated 1, 2-table, 2a-2e, 3, 4, 5, 6 = 11; standalone 1, 2-table, a-e, 3 = 8. Both note-2 tables sit in the line-item ledger at p11/p19; note 3 is split R1689/R1690. 19 - 2 + 1 = 18) | none | PASS |
| Footnotes | 28 (+3 unresolved) | 28 markers/texts (L403, 417, 493-495, 593, 595, 597, 819, 851, 879, 888-890, 904, 909, 917, 918, 928, 935, 938, 940, 948, 955-957, 1387, 1389). The repeat "(Unaudited)*" marker at L454 is acknowledged in R1676 context | none | PASS |
| Line-item rows | 356 | 356 = 339 lines with at least one decimal cell + 17 label-continuation or all-dash rows (p3 L147/151/152/157/161; p4 L189/201/203/204; p10 L473; p12 L591; p13 L643/646/649/650; p17 L851; p18 L879) | none | PASS |
| Line-item count test | grep 330 | 339 (one-decimal basis). A2's 330 counts lines with two or more decimals; the 9 single-decimal lines (L417, L463, L481, L647, L648, L819, L830, L860, L883) are all in the ledger | none | PASS (basis note, STYLE S6) |
| Line-item cells | 1,260 | 1,260 (summed page by page from ledger rows and checked against fulltext column counts) | none | PASS |
| ZERO_STANDING cells | 87 on 36 lines | 87 on 36 lines (86 dash cells re-counted line by line + R1410 "Nil") | none | PASS |
| Agenda items | 3 | 3 ((i) L36, (ii) L45, (iii) L67) | none | PASS |
| Auditor paragraphs | 11 | 14 numbered paragraphs (consolidated 1-9, L1057-1140; standalone 1-5, L1283-1323) + board-letter line L41. Paras 1, 2, 4 (both reports) are scope boilerplate; the conclusion paragraphs (consolidated 5, L1089; standalone 4, L1308) carry no separate row but their substance is in R1653, R1749, R1752, R1765 | none | PASS (basis note, STYLE S6) |
| Entities, consolidation list | 75 | 75 (72 subsidiaries L1181-1256 + 3 associates L1260-1262) | none | PASS |
| Entities, total | 132 | 132 (75 + 57 others; every named regulator, court, counterparty, award body and person in L21-L1548 present in R1418-R1447, R1523-R1549) | none | PASS |
| ENTITY_CHANGE | 10 | 10 (wef: L1215, L1253, L1254, L1255, L1256; upto: L1232, L1233, L1245, L1246, L1251) | none | PASS |
| Dates | 71 | 71 distinct date facts (repeat column headers on continuation pages not rowed) | none | PASS |
| Forward statements | 32 | 32 | none | PASS |
| Signature blocks | 4 | 4 (L96, L1028, L1159, L1335) | none | PASS |
| Structured IDs | 1,778 referenced | 1,778 (NUMBER R001-R1417, ENTITY R1418-R1549, FORWARD R1550-R1581, DATE R1582-R1652, QUALIFIER R1653-R1778; ledger ranges contiguous, footers R156...R1325 placed) | none | PASS |

### 1B. Presentation

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Slides | 9 | 9 ([page N] markers) | none | PASS |
| Numbers | 33 | 33 (boilerplate P-L60 plot number and P-L61 pincode deduplicated against P-R006/P-R007) | none | PASS |
| Entities | 25 | 25 | none | PASS |
| Forward | 3 | 3 | none | PASS |
| Dates | 7 | 7 | none | PASS |
| Qualifiers | 6 | 6 | none | PASS |
| Turns / questions | 0 | 0 (no transcript in run) | n/a | n/a |

A1 value error carried: P-R026 records 6 plan levers; P-L122-128 shows 5. A2 flagged it (COUNT_DISCREPANCY) and A4 recorded it (rev L22). Not load-bearing.

### 1C. Ledger to review (orphan test)

| Ledger unit | In ledger | Cited or marked in A4 | Orphans |
|---|---|---|---|
| Notes | 18 | 18 (each in the 0D table, rev L63-81; R1690 classification folded into the C-3 row) | none |
| Slides | 9 | 6 cited (slides 1, 4, 5, 6, 7, 8); slides 2, 3, 9 (title, safe harbour, thank-you) covered by "All ... 9 slides reviewed" (rev L14) | none |
| Turns | 0 | 0 | none |
| All other ledger rows | 1,778 + 74 IDs | Blanket mark "Unreviewed ledger rows: none" (rev L18) | none |

Coverage verdict: PASS. No orphan row and no unit missing from the ledger. Two A2 flags carry no explicit disposition in A4 (SIGNATURE_BEFORE_MEETING_END; four of the ten ENTITY_CHANGE rows). They are logged as STYLE S9. The fifth un-dispositioned ENTITY_CHANGE row, R1508 (Campaign Registry Inc (Canada), upto 14-Jan-2026, L1245), bears on a positive claim and is carried as MISSING under Read 3 below.

---

## 2. ARITHMETIC AUDIT

Every derived metric in the A4 tables was recomputed from the raw filed numbers. Column order in A4: Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Operating EBITDA (pre-exc PBT + D&A + FC - OI) | 1,173.62 / 1,230.14 / 1,421.88 / 2,310.43 / 2,652.02 / 4,822.46 | same; Q2 FY27 also = revenue less L139, L140, L143 | L136, L141, L142, L146 | PASS |
| Op EBITDA margin | 19.24 / 18.69 / 21.26 / 19.16 / 19.98 / 19.44% | same | L135 | PASS |
| Reported EBITDA | 1,135.38 / 1,136.72 / 1,401.75 / 2,268.85 / 2,538.47 / 5,026.23 | same | L150 | PASS |
| Operating EBIT = segment total | 494.84 / 490.70 / 680.94 / 965.96 / 1,171.64 / 1,995.72 | same | L247 | PASS |
| Core PBT; reported PBT ex-OI | 292.88 / 304.80 / 483.03 / 587.47 / 787.83 / 1,234.12; 271.88 / 198.44 / 446.49 / 546.03 / 644.93 / 1,136.16 | same | L136, L146, L150 | PASS |
| OI / PBT; ETR; current-tax rate | -6.77/6.12/3.55/-0.03/4.35/20.98%; 32.25/40.69/26.80/27.03/31.15/30.02%; 48.47/54.91/36.14/44.66/42.03/42.58% | same | L136, L150, L153-154 | PASS |
| PAT margins (total, parent); cost ratios (network, employee, other) | all six columns | same | L135, L139-143, L164, L166 | PASS |
| Sensitivity: Op EBITDA + staff charge | 1,075.36 ... 4,707.82 and margins | same | L515 | PASS |
| Standalone Op EBITDA, margins, reported EBITDA, core PBT, OI/PBT, ETR, PAT margin | all six columns | same. Ties to Reg 52(4): ISCR 470.72/94.32 = 4.99 (L915), operating margin 194.54/1,854.12 = 10.49% (L904), net margin (L909) | L621-637 | PASS |
| Segment YoY and margins; Data margin; CR share of segment result | all cells | same | L234-247 | PASS |
| YoY table 2A, 2B (every row) | as stated | same | L135-167, L621-653 | PASS |
| H1 Op EBITDA growth (2C) | +14.79% | +14.78% (341.59 / 2,310.43 = 14.785%) | L139-146 | ROUNDING (STYLE S1) |
| H1 Op EBITDA margin change (2C) | +82 bps | +83 bps unrounded (19.984% - 19.158%) | L135 | ROUNDING (STYLE S1) |
| Gross spread and EBITDA-gain split | 55.48% to 52.43%, -305 bps; 122.02 + 126.24 = 248.26; 50.9% | same | L135, L139, L140, L143 | PASS |
| Step 3 derived quarters (Q1 FY26, H2 FY26) and QoQ rates | as stated | same | L135-146, L515, L520 | PASS |
| PAT bridge (Step 4), every line and share | sum 152.40; tax 67.17 / 25.26 | same | L135-167 | PASS |
| OI-reversion run-rate | PAT 310.98, +69.7% | same | L136, L160 | PASS |
| CFO, CFO/PAT, CFO/Op EBITDA, capex, FCF, FCF after lease and interest | as stated | same | L439-441, L458, L478, L480 | PASS |
| WC change (L431-438) | (963.35) / (813.20) | same | L431-438 | PASS |
| Receivable, inventory, payable days | 61.38 / 63.32; 3.22 / 3.87; 138.69 / 123.02 | same | L335, L338, L384, L135, L139 | PASS |
| **Cash conversion cycle, 30-Sep-2026** | **-61.83 days** | **-55.83 days** (63.32 + 3.87 - 123.02) | L338, L335, L384, L135, L139 (rev L359, L415) | **FAIL (F1)** |
| **CCC change** | **+12.26 days** | **+18.26 days** (-55.83 - (-74.09)) | same | **FAIL (F1)** |
| Gross debt, cash, net debt, lease, ND/EBITDA, ND/equity | 11,197.04; +1,606.60; 1.99x / 2.11x; 2.78x / 3.29x | same | L337-340, L373-374, L382-383, L363 | PASS |
| Standalone 5B (CFO, capex, FCF, WC, days, debt, net debt, D/E) | as stated | same | L730-800, L832-882, L932 | PASS |
| S-vs-C PAT gap; subsidiary revenue share, EBITDA, margin; subsidiary gross debt | as stated | same | L135, L166, L621, L637 | PASS |
| **Subsidiaries-plus-eliminations share of QoQ parent PAT rise (5C)** | **192.08 of 206.80 (93%)** | **185.39 of 206.80 (89.6%)** = (341.03 - 125.86) - (134.23 - 104.45) | L166, L637 (rev L410, L579, L664, L690, L800, L816) | **FAIL (F2)** |
| ROCE (H1 annualised; FY26) | 15.84%; 15.07% | same (capital = total equity + net debt) | L247, L368, L373, L382 | PASS |
| TTM parent PAT, TTM EPS, Q2-annualised divergence | 1,103.79; 38.72; 23.6% | same | L166, L213 | PASS |
| Digital: 107/3,016; annualised 428 vs 886 | 3.55%; 48% | same | P-L138, P-L147, L1384 | PASS |
| Core connectivity growth | +5.95% | same | L1383-1384 | PASS |
| Contingent ratios | DoT 2.21x parent equity, 72.9% standalone NW; VAT 10.8%; associates 68.6% | same | L560, L573, L326, L363, L954 | PASS |
| FY26 ETR ex-DTA credit | 35.11% | same | L150, L153-154, L601 | PASS |
| ESOP dilution | 0.03% | same (0.09 / 285.00) | L200, L481 | PASS |

Arithmetic verdict: FAIL on two derived metrics (F1, F2). Everything else ties to the filed lines within rounding.

---

## 3. ADVERSARIAL READ

### Read 1. Positive claim: the Q2 gain is operating

A4 claim: "Core operating items delivered +190.15, more than the whole +152.40 PAT gain ... On the face of the filing, the gain is operating" (rev L331); Op EBITDA +21.15% YoY, margin +202 bps (rev L221-222).

Strongest bear counter from the extract. The gain is one quarter, in subsidiaries, and larger than revenue can carry. Subsidiary Op EBITDA rose 195.09 QoQ on subsidiary revenue up only 89.54 (4,744.23 to 4,833.77) [DERIVED from L135, L621 and the A4 5C rows]: an incremental margin of about 218%. Data Services result rose 175.18 QoQ on revenue up 107.41 (L235, L243). On the half-year the margin moved only about 83 bps (19.16% to 19.98%). The gross spread fell 305 bps (L135, L139). The standalone Reg 52(4) footnote attributes the parent's own margin rise to "decrease in Operating and other expenses" (L917).

Survives? Yes. Graft needed? No. A4 already carries this counter in substance: cost-led margin with a falling spread (rev L258), subsidiary attribution with no cause stated (rev L410), "one quarter does not make a new run-rate" (rev L281), and the Q3 21.0% / 19.5% test (rev L562-565). Only the attribution number needs correction (F2). The 218% incremental subsidiary margin is a suggested sharpening, not a required graft.

### Read 2. Positive claim: the Digital loss cut is the likeliest recurring explanation

A4 claim: Digital "on the path to breakeven", losses "halved" (P-L132, L1366). The analyst note calls the Digital loss cut "the likeliest recurring explanation, since Digital sits in subsidiaries" (rev L816). Reading A in the cross-read (rev L306).

Strongest bear counter from the extract. The arithmetic caps the Digital explanation at about half of the jump.
- The Q2 Digital loss is INR 107 Cr (P-L138). Q1 shows -6.9% with no rupee value (P-L142).
- If Q1 FY27 Digital revenue did not exceed Q2's 3,016 Cr (L1384), the Q1 loss was at most 208.10 Cr (0.069 x 3,016), so the cut is at most 101.10 Cr [DERIVED bound].
- That is at most 51.8% of the 195.09 Cr QoQ rise in subsidiary EBITDA and at most 57.7% of the 175.18 Cr QoQ rise in the Data Services result (L243). At least about 94 Cr of the subsidiary EBITDA rise sits outside Digital or in one-off credits.
- For the Digital cut to explain the whole 195.09 Cr, Q1 Digital revenue would need to be about 4,378 Cr [DERIVED: (195.09 + 107) / 0.069], 45% above Q2's 3,016 Cr.
- "Digital margin" has no definition (L1366, R1768 FOOTNOTE_UNRESOLVED), so the metric may not match EBITDA or segment result.
- The perimeter moves both ways. Commotion came in from 01-Dec-2025 (L1253-1254), and FY26 shows 136.96 Cr paid for a subsidiary acquisition (L463; linking it to Commotion by date is INFERENCE). Mgage SA de CV left on 01-Oct-2025 (L1251) and Kaleyra Africa on 04-Sep-2026 (L1246).

Survives? Yes. Graft needed? Yes (MISSING, A4). Add the 101.10 Cr bound and the 4,378 Cr requirement to the cross-read. Replace "likeliest recurring explanation" in the analyst note with a bounded statement: Digital can explain about half at most, and the other half needs the Q1 cost-credit answer (Q1 in 8.5A). Add the 136.96 Cr acquisition cash and the Mgage exit to the Q27 perimeter question.

### Read 3. Positive claim: Campaign Registry profit growth

A4 claim: Campaign Registry result +114.38% YoY to 162.03 on revenue +37.14% (rev L204, L500, L531, L586, L447). It is listed as a candidate growth trigger and a Growth Visibility Premium input.

Strongest bear counter from the extract. The +114.38% rests on a depressed base quarter.
- Q1 FY26 CR result was 122.93 [DERIVED: 198.51 - 75.58, L246]. Q2 FY26 fell to 75.58, a 38.5% drop QoQ, while revenue rose from 189.38 to 202.54 [DERIVED, L238]. CR margin went from 64.91% to 37.32%.
- Against the pre-dip quarter (Q1 FY26), Q2 FY27 result is up 31.8%. The Q2 FY27 margin of 58.33% is still below Q1 FY26's 64.91%.
- H1 FY27 vs H1 FY26 result growth is +55.75% (198.51 to 309.17, L246). QoQ growth is +10.1% (147.14 to 162.03).
- The perimeter changed. Campaign Registry Inc (Canada) left consolidation on 14-Jan-2026 (L1245, R1508, A2 ENTITY_CHANGE). So the YoY comparison is not like-for-like, and the effect is ND.
- The same dip depresses the CR share-of-result base (15.27% in Q2 FY26 vs 26.09% in Q1 FY26 [DERIVED: 122.93 / 471.12]). Concentration was already about a quarter of segment profit before Q2 FY26.

Survives? Yes. Graft needed? Yes (MISSING, A4). Every use of "+114.38%" needs the base-quarter qualifier, with H1/H1 +55.75% as the trend figure: rev L204, L447, L500, L531, L586 and YAML L758. Add the Canada deconsolidation to Q8.

### Read 4. Mandatory acquisition-economics probe

The filing describes three purchases or stake moves.

(a) Associate stake buy, H1 FY27: "Purchase of investments in associates (356.10)" (L462). The parent paid it: standalone "Purchase of non-current investments (356.11)" (L850). The target is not named. The three associates are STT Global Data Centres India, Smart ICT Services and United Telecom (L1260-1262). Target PAT, ROCE, debt and cash are all ND. The only earnings proxy is the group's share of profit of all three associates: Q2 FY27 (3.25), H1 FY27 1.10, FY26 32.77 (L158), TTM 16.66 [DERIVED: 32.77 - 17.21 + 1.10].
- The H1 cash call alone is about 21.4x the TTM share of associate profit (356.10 / 16.66).
- The carrying value of 2,331.73 (L326) is about 140x the TTM share (2,331.73 / 16.66 = 139.96x). The earnings yield on book is 0.71%.
- Quality markers are weak. The associates' numbers are management-furnished and unreviewed (L1131-1137), and the Q2 share is a loss.
- The H1 associate cash equals 5.7x H1 FCF of 62.01 [DERIVED, L441, L458]. It went out in the half when net debt rose 1,606.60.
- This is not a cheap, accretive buy. It is the reverse risk: a capital-hungry stake that earns under 1% on book so far.
- Bear survives. A4 has the question (Q12, rev L595) and the flag (rev L675) but states no multiple. MISSING, A4: graft "356.10 = ~21x and carrying value 2,331.73 = ~140x the TTM group share of associate profit 16.66; 0.71% yield on book".

(b) Kaleyra, Inc. transfer to TCNL. The aggregate FMV is USD 92.625m (L1505-1507), paid in 3,17,632 TCNL shares at USD 291.6 each (L1508-1510). That ties to USD 92.62m within rounding. Kaleyra's PAT, ROCE, debt and cash: NOT FOUND. Price/PAT: not computable. The deal is intra-group, "not expected to have any material impact on the consolidated financial position" (L1512-1513). The only open risk is a standalone carrying-value gap, already asked in Q15 (rev L598). No graft.

(c) FY26 "Acquisition of Subsidiary (net off acquired cash) (136.96)" (L463). Linking it to Commotion by date is INFERENCE. Target PAT: NOT FOUND, so no multiple. Carried into the Read 2 graft as a perimeter fact.

---

## FINDINGS (tagged)

FACTUAL (loop A4)
- F1. Cash conversion cycle at 30-Sep-2026. A4 shows -61.83 days and a change of +12.26 days (rev L359), and repeats -61.83 at rev L415. Recomputed from A4's own components: 63.32 + 3.87 - 123.02 = -55.83 days, a change of +18.26 days. Sources: L338, L335, L384, L135, L139.
- F2. Subsidiary attribution of the QoQ parent PAT rise. A4 says subsidiaries plus eliminations supplied 192.08 (93%) of the 206.80 rise (rev L410). Recomputed: (341.03 - 125.86) - (134.23 - 104.45) = 185.39, which is 89.6% (L166, L637). The 93% repeats at rev L579, L664, L690, L800 and L816. The conclusion "a subsidiary event" holds at about 90%.
  - The brief (rev L690) also says "Overseas subsidiaries made the jump (FILED)". The extract does not support "overseas": the subsidiary set includes Indian entities (L1211, L1221, L1241, L1254), and consolidated-less-standalone includes eliminations. Fix: "Subsidiaries (and eliminations) supplied about 90%".
- F3. Rev L331 says "consolidated net credit cost swung adversely by 110.79 in H1 yet other expenses fell". On the H1 basis the sentence uses, other expenses rose 57.24, from 1,817.41 to 1,874.65 (L143). They fell only in Q2 YoY (-35.42) and QoQ (-63.07). Fix the period. The underlying point (other costs absorbed most of the credit swing) survives on the H1 numbers.

MISSING (loop A4)
- M1. Campaign Registry base effect and perimeter change (Read 3). Sources: L238, L246, L1245.
- M2. Digital ceiling, the 4,378 Cr requirement, and the two-way perimeter (Read 2). Sources: P-L138, P-L142, L1384, L1366, L463, L1246, L1251, L1253-1254.
- M3. Associate stake-buy multiple (Read 4a). Sources: L158, L326, L462, L850, L1131-1137.
- M4. Rev L410 and L667 say the standalone Reg 52(4) ratios "improved". That holds only for the leverage ratios (D/E, asset cover, debt to assets).
  - The bad-debts-to-receivables ratio rose from 1.90% (FY26, full year) to 8.57% (H1, not annualised) (L940). The current ratio fell from 0.57 to 0.36 (L938).
  - The parent wrote off 116.73 of the 161.23 consolidated H1 bad debts (72%), against a 111.81 allowance reversal (L825, L829, L419). The defaulted receivable sits mainly at the parent and was largely provided earlier.
  - Add this to flag 10 and Q10 (rev L593, L672).

CONTRADICTION: none.

STYLE (logged, no loop): S1-S13 under STYLE NOTES below.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.
- Exact gap, FACTUAL: F1 (CCC -61.83 should be -55.83; change +12.26 should be +18.26), F2 (192.08 / 93% should be 185.39 / 89.6% in six places; drop "Overseas" from the brief), F3 (H1 other-expenses direction).
- Exact gap, MISSING: graft the three surviving bear counters (M1 Campaign Registry base effect and Canada perimeter; M2 Digital 101.10 Cr ceiling and 4,378 Cr requirement; M3 associate stake-buy multiple of about 140x TTM share) and the M4 Reg 52(4) bad-debt qualifier.
- All fixes come from the existing extract. No A2 or A3 re-run is needed: coverage is clean and no new forensic reading is required.
- None of the findings changes the protocol verdict PROCEED WITH FLAGS or the cash classification INDETERMINATE-WITH-DIRECTION.

---

## STYLE NOTES (logged, no re-run)

- S1. Step 2C rounding (rev L250-251). H1 Op EBITDA growth is 14.78%, not 14.79%. The margin change is +83 bps unrounded, not +82 bps. Both are rounding-level.
- S2. 0D C-2d (rev L68) says "of which 25.67 PPE impairment". L417 and L495 say the 25.67 "Includes impairment". Restore "includes".
- S3. Flag 7 and the YAML flag (rev L669, L805) say the note is "silent on the outcome". The note states "the Group awaits the National Court's decision" (L572). Quote that.
- S4. The brief says "Profit for shareholders nearly doubled" (rev L688). The rise is +86.3%; write "rose 86%".
- S5. The brief's "not from better pricing" (rev L689) carries no tier tag. Pricing is not disclosed, so tag it INFERENCE from the -305 bps spread.
- S6. A2 count-test bases. Line-item grep_count 330 counts lines with two or more decimal tokens; 9 single-decimal lines exist. Auditor-paragraph count 11 excludes scope boilerplate and the conclusion paragraphs. A2 should state both bases.
- S7. The A2 ledger labels p16/L776 "LIABILITIES". The cells there (R1039-R1040) hold the standalone equity totals 10,306.04 / 10,578.69 (L776). Relabel the row.
- S8. A1 did not emit two repeat column qualifiers as rows: p5/L231 "(refer note 5)" on the segment table and p10/L454 "(Unaudited)*". The facts are held at R1654, R1660, R1666 and in the R1676 context. No information is lost.
- S9. Four A2 flags have no explicit disposition in A4. Add one line each, "reviewed, no finding":
  - SIGNATURE_BEFORE_MEETING_END. CEO 12:58:01 (L1028), auditor 13:05:38 / 13:04:44 (L1159, L1335), meeting close 13:45 (L33). The approval, CEO signature, review-report order is normal while items (ii) and (iii) continued.
  - ENTITY_CHANGE rows R1482, R1495, R1514, R1518.
  - ANONYMISED_CLIENT P-R055 and P-R056.
  - Slides 2, 3 and 9.
- S10. A1 P-R026 holds the value 6; the slide shows 5 levers (P-L122-128). A4 already records this; it is an A1 QA note.
- S11. The A2 deck ledger paraphrases the slide 4 title. The verbatim title is "THE TEAM IS IN PLACE" (P-L85).
- S12. The summary narrative is 6 paragraph lines, about 207 words. It falls in the 10-20 line band only when wrapped. One sentence per line would make the count plain.
- S13. Diagnostic 1 (rev L257) leaves the inter-segment elimination change out of the revenue decomposition: +38.96, from (51.81) to (12.85), L239. Without it the named components sum to 549.19, not 588.14.

---

```yaml
stage: A5-adversary
company: "TATACOMM"
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
  - {metric: "Consolidated cash conversion cycle at 30-Sep-2026 and its change (Step 5A, Step 5D)", a4_value: "-61.83 days; change +12.26 days", recomputed: "-55.83 days (63.32 + 3.87 - 123.02); change +18.26 days", source_line: "L338, L335, L384, L135, L139; review L359, L415"}
  - {metric: "Subsidiaries-plus-eliminations share of the 206.80 QoQ parent PAT rise (Step 5C)", a4_value: "192.08 (93%)", recomputed: "185.39 (89.6%) = (341.03 - 125.86) - (134.23 - 104.45)", source_line: "L166, L637; review L410, L579, L664, L690, L800, L816"}
surviving_bear_counters:
  - {claim: "Campaign Registry result +114.38% YoY as a growth trigger (review L204, L447, L500, L531, L586)", counter: "Base effect: Q2 FY26 CR result 75.58 was 38.5% below Q1 FY26 122.93 (margin 37.32% vs 64.91%); Q2 FY27 is +31.8% vs Q1 FY26 and its 58.33% margin is still below 64.91%; H1/H1 +55.75%; QoQ +10.1%; Campaign Registry Inc (Canada) deconsolidated 14-Jan-2026, so YoY is not like-for-like", source_line: "L238, L246, L1245", type: MISSING}
  - {claim: "Digital loss cut is the likeliest recurring explanation of the Q2 subsidiary profit jump (review L306, L816)", counter: "If Q1 Digital revenue did not exceed Q2's 3,016, the -6.9% to -3.6% move is worth at most 101.10 Cr, at most 51.8% of the 195.09 QoQ subsidiary EBITDA rise and 57.7% of the 175.18 Data result rise; explaining all of it needs Q1 Digital revenue of about 4,378 Cr; margin undefined; perimeter moves both ways (Commotion in, 136.96 acquisition cash; Mgage and Kaleyra Africa out)", source_line: "P-L138, P-L142, L1384, L1366, L243, L463, L1246, L1251, L1253-1254", type: MISSING}
  - {claim: "Associate stake buy 356.10 in H1 FY27 (mandatory acquisition probe; review L595, L675)", counter: "Target unnamed, PAT ND; H1 cash call = ~21.4x and carrying value 2,331.73 = ~140x the TTM group share of associate profit 16.66 (0.71% yield on book); associates management-furnished and unreviewed; Q2 share a loss; cash call = 5.7x H1 FCF while net debt rose 1,606.60", source_line: "L158, L326, L441, L458, L462, L850, L1131-1137", type: MISSING}
findings_by_type:
  factual:
    - "F1 CCC at 30-Sep-2026 is -55.83 days (change +18.26), not -61.83 (+12.26); review L359, L415; source L335, L338, L384, L135, L139"
    - "F2 Subsidiaries plus eliminations supplied 185.39 (89.6%) of the 206.80 QoQ parent PAT rise, not 192.08 (93%); six places (review L410, L579, L664, L690, L800, L816); brief 'Overseas subsidiaries' unsupported (Indian subsidiaries at L1211, L1221, L1241, L1254)"
    - "F3 Review L331 'yet other expenses fell' is false on the H1 basis used: H1 other expenses rose 57.24 (1,817.41 to 1,874.65, L143); they fell only in Q2"
  missing:
    - "M1 Campaign Registry +114.38% YoY lacks the Q2 FY26 base-quarter dip and the Canada deconsolidation qualifier (L238, L246, L1245)"
    - "M2 Digital explanation lacks the 101.10 Cr ceiling and 4,378 Cr requirement; analyst_note 'likeliest' unsupported; 136.96 FY26 acquisition cash and Mgage exit missing from the perimeter question (P-L138, P-L142, L1384, L463, L1251)"
    - "M3 Associate stake-buy multiple not stated: ~21x cash call and ~140x carrying value vs TTM share 16.66 (L158, L326, L462)"
    - "M4 'Standalone Reg 52(4) ratios improved' omits bad-debts-to-receivables 1.90% to 8.57% (L940) and current ratio 0.57 to 0.36 (L938); parent wrote off 116.73 of 161.23 H1 bad debts against a 111.81 allowance reversal (L825, L829, L419)"
  contradiction: []
  style:
    - "S1 2C rounding: 14.78% not 14.79%; +83 bps unrounded not +82"
    - "S2 C-2d drop of 'Includes' on the 25.67 impairment (L417, L495)"
    - "S3 VAT note is not silent: 'the Group awaits the National Court's decision' (L572)"
    - "S4 'nearly doubled' for +86.3% parent PAT"
    - "S5 'not from better pricing' needs an INFERENCE tag"
    - "S6 A2 count-test bases unstated (line items two-decimal basis 330 vs 339; auditor paras 11 vs 14 numbered)"
    - "S7 A2 ledger p16/L776 labelled LIABILITIES but holds standalone equity totals"
    - "S8 A1 repeat column qualifiers p5/L231 and p10/L454 not rowed; facts held elsewhere"
    - "S9 Missing one-line dispositions: SIGNATURE_BEFORE_MEETING_END, ENTITY_CHANGE R1482/R1495/R1514/R1518, ANONYMISED_CLIENT P-R055/P-R056, slides 2, 3, 9"
    - "S10 A1 P-R026 value 6 vs 5 levers (already recorded by A4)"
    - "S11 A2 slide 4 title paraphrased; verbatim 'THE TEAM IS IN PLACE' (P-L85)"
    - "S12 Summary narrative is 6 paragraph lines (~207 words); state one sentence per line"
    - "S13 Diagnostic 1 omits inter-segment elimination +38.96 (L239) from the revenue decomposition"
loop_back_to: "A4"
gap: "FACTUAL: fix CCC to -55.83 days (+18.26) at review L359/L415; fix subsidiary attribution to 185.39 (89.6%) in six places and drop 'Overseas' from the brief; fix the H1 other-expenses direction at L331. MISSING: graft the Campaign Registry base-effect and Canada-perimeter counter, the Digital 101.10 Cr ceiling and 4,378 Cr requirement (replace 'likeliest' in analyst_note), the associate stake-buy multiple (~140x TTM share 16.66), and the Reg 52(4) bad-debt ratio 8.57% qualifier. No A2 or A3 re-run needed."
style_notes:
  - "S1 2C rounding (14.78%, +83 bps)"
  - "S2 restore 'includes' on 25.67 impairment"
  - "S3 VAT note says the Group awaits the decision"
  - "S4 'rose 86%' not 'nearly doubled'"
  - "S5 tag 'not from better pricing' as INFERENCE"
  - "S6 A2 should state count-test bases"
  - "S7 A2 relabel p16/L776"
  - "S8 A1 repeat column qualifiers not rowed, no information lost"
  - "S9 add reviewed-no-finding dispositions for un-dispositioned A2 flags and slides 2, 3, 9"
  - "S10 A1 P-R026 value error already recorded"
  - "S11 A2 slide 4 verbatim title"
  - "S12 summary narrative line count"
  - "S13 add inter-segment +38.96 to the revenue decomposition"
analyst_note: "All five brief parts are present. Coverage is clean: a fresh pass over both fulltexts reproduces every A2 category, and the two count gaps reconcile by counting basis (A2 counts lines with two or more decimals; nine single-decimal lines sit in the ledger). The failure is A4 work only. Two derived numbers are wrong: the cash conversion cycle is -55.83 days, not -61.83, and subsidiaries supplied 185.39 (89.6%) of the 206.80 QoQ parent PAT rise, not 192.08 (93%). The 93% runs through the brief, flags and analyst note; the 'subsidiary event' conclusion holds at about 90%. Three bear counters survive. Campaign Registry's +114.38% YoY rests on a Q2 FY26 result 38.5% below Q1 FY26; H1/H1 is +55.75%. The Digital margin move can explain at most about 101 Cr of the 195.09 Cr QoQ subsidiary EBITDA rise unless Q1 Digital revenue exceeded Q2's, so it cannot be the 'likeliest' main cause. The 356.10 Cr associate stake buy sits at about 140x the trailing group share of associate profit. None of this changes PROCEED WITH FLAGS."
```
