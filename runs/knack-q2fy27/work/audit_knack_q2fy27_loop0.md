# A5 ADVERSARY / COMPLETENESS AUDIT: Knack Packaging Limited (KNACK) | Q2 FY27

Stage: A5 | Model: claude-opus-5-5 | Audit date: 28-Oct-2026
Inputs read: A4 review; A1 fulltexts (results, deck, concall); A1 structured files (targeted greps only); A2 ledgers (results, deck, concall). No source PDF was opened. Nothing under inputs/ was read. A3 reasoning was not read.

Anchor key: "rev L###" = A4 review line. "res L###" = results fulltext line. "deck L###" = deck fulltext line. "cc L###" = concall fulltext line. "led-res / led-deck / led-cc L##" = A2 ledger line. All money in Rs Crore unless marked "m" (Rs million, x0.1 to Crore).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Plain-language brief (rev L906-949): (1) summary narrative PRESENT, rev L910-911, 19 sentences, about 217 words; (2) sector PRESENT, rev L913-918, 5 bullets; (3) business model PRESENT, rev L920-925, 5 bullets; (4) competition PRESENT, rev L927-930, 3 bullets; (5) forward map PRESENT, rev L932-939, 6 catalysts, each dated and each with a bull and a bear fork. Gate: PASS. No part is a placeholder.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration vs A2 counts

| Doc | Category | A2 count | A5 fresh count | A5 method and anchors | Orphan rows | Status |
|---|---|---|---|---|---|---|
| Results | Numbered notes | 18 | 18 | grep `^\s*[1-9]\. ` over res L343-407 and L685-750, IPO table rows excluded: res L343, 349, 353, 360, 363, 365, 375, 381, 400; L685, 692, 696, 703, 706, 708, 718, 724, 743 | none | PASS |
| Results | Footnotes | 3 | 3 | res L213, L556 (EPS not annualised), L823 (EBITDA*) | none | PASS |
| Results | Agenda items | 3 | 3 | res L54, L63, L79. Item 3 (L79) is absent from the structured file; A2 carries it as M1 (led-res L34) | none | PASS (known A1 gap, carried) |
| Results | Auditor paragraphs | 12 | 12 | 10 numbered (res L123, 131, 138, 147; L428, 438, 446, 459, 464, 489) plus 2 unnumbered (JV sub-para res L497, conclusion res L505). Res L455-457 (Reg 33(8)) sits inside A2's para-3 row (led-res L52) | none | PASS |
| Results | Entities (consolidation) | 2 | 2 | res L461-462, L689-690 | none | PASS |
| Results | Line items (pipe rows) | 198 | 198 | SA P&L 23 (res L187-214), SA BS 35 (L231-271), SA CF 32 (L286-321), SA Note 9: 4 (L404-407), CON P&L 27 (L526-557), CON BS 35 (L574-614), CON CF 33 (L629-665), CON Note 9: 4 (L747-750), press table 5 (L817-821) | none | PASS |
| Results | ZERO_STANDING | 41 | 41 | 25 mid-row dash cells plus 10 trailing dash cells (grep `\| -`), plus 6 Annexure C "0.00" cells (res L957, L1000, L1004) | none | PASS |
| Results | Forward statements | 10 | 10 | res L356, L699, L837, L845, L847, L859, L860, L867, L869, L961 (structured R790-R799). R795 (L859) is past tense but tagged FORWARD by A1; no unit missing | none | PASS |
| Results | ID accountability | 921 | 921 | Section bracket counts in led-res sum to 921 (18+31+25+4+34+18+4+34+14+24+640+25+17+10+10+13); 640 line-item IDs recomputed by statement block | none | PASS |
| Deck | Slides | 36 | 36 | grep `^\[page [0-9]+\]` = 36 | none | PASS |
| Deck | ZERO_STANDING | 15 | 15 | 14 dash cells (deck L491-492: 5; L516, L520; L550-551; L594, L598; L609, L614-615) plus "zero revenue offset" (deck L356) | none | PASS |
| Deck | Slide numbers (spot tests) | p6: 24; p17: 7; p26: 37 | p6: 24; p17: 7; p26: 37 | Token count of deck L87-102, L230-238, L341-356 | none | PASS (spot) |
| Deck | Unrowed numbers | 6 (M01-M06) | 6 | deck L22 "5th", L24 "400051", L25 "25th", L26 "400001", L45 "+05'30'", L704 "14%" | none | PASS (known A1 gap, carried) |
| Concall | Turns | 16 | 16 | Preamble, moderator open, CMD, CFO, Q&A open, 8 analyst turns (cc L133, 177, 244, 293, 349, 423, 473, 519), last-question, closing, close | none | PASS |
| Concall | Questions | 26 | 28 | Read of every analyst turn cc L133-578. Ledger lacks: T05 YoY volume baseline (cc L164-166) and T11 pinch-machine margin test (cc L501-511) | none | FAIL (A5-07, to A2) |
| Concall | Number rows (line-level sweep) | 472 | no line with a digit lacks a row | Every cc line from L54 to L581 that carries a digit after the timestamp was matched to a NUMBER or DATE row line in led-cc L72-546, L775-991. Spot rows confirmed in structured file: L164-166 (R119-R127), L481-482 (R353-R359), L501-517 (R383-R398) | none | PASS |
| Concall | Line-0 rows | 0 | 0 | n/a | none | PASS |

### 1B. Orphan-row test (ledger row absent from A4)
A4 marks every ID reviewed in its preamble (rev L19-23: 921 of 921, 934 of 934, 798 of 798; "Unreviewed rows: none"). I tested each A2-flagged row group against the review:
- Results: M1 (rev L90, L459); UNREVIEWED_COMPARATIVE R851/R873 (rev L86, L94); OTHER_AUDITOR_RELIANCE R320-R325 (rev L94, L454); ZERO_STANDING R496 (rev L308, L441); Annexure C R716-R729 (rev L372, L889); FORWARD R790-R799 (rev L880-893); SOURCE_AS_PRINTED R863/R888 and OCR_UNCERTAIN R005/R006/R730/R757 are rounding or signature items, covered by the blanket mark.
- Deck: M06 (rev L22); R103 (rev L39); FOOTNOTE_UNRESOLVED R711 (rev L367), R726 (rev L461), R740 (rev L402); HIDDEN_SERIES p28-p30 (rev L448); FORWARD p19 (rev L888), p26 (rev L880), p28 (rev L368), p30 (rev L314, L891).
- Concall: ENTITY_VARIANT (rev L491); ASR_DOUBT_NAME (rev L609-637); REPEAT_QUESTION clusters (rev L642-647).
Orphan rows: none.

### 1C. Units missing from the structured file
Seven known units (results M1; deck M01-M06) are absent from A1's structured files. A2 raised all seven and carries them in its ledgers. My sweep found no further unit. The A1 structured-file patch stays open from A2; this audit adds no new A1 item.

---

## 2. ARITHMETIC AUDIT

All derived metrics were recomputed from raw lines in Rs m, then converted at x0.1.

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| CON Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 | 40.06 / 56.86 / 32.01 | 356.75+102.20+38.70-97.04 = 400.61m; 452.87+98.60+40.26-23.12 = 568.61m; 280.63+71.89+30.52-62.91 = 320.13m | res L527, L534-535, L538 | PASS |
| CON Op EBITDA H1 FY27 / H1 FY26 / FY26 | 96.92 / 69.80 / 151.96 | 969.22m / 698.00m / 1,519.59m | same | PASS |
| CON Op EBITDA margin Q2 FY27 / Q1 / Q2 FY26 / H1 FY27 / FY26 | 13.59 / 21.66 / 16.57 / 17.39 / 18.45% | 13.59 / 21.66 / 16.57 / 17.39 / 18.45% | res L526 | PASS |
| Reported EBITDA Q2 FY27 / Q1 / Q2 FY26 | 49.77 / 59.17 / 38.30 | 497.65m / 591.73m / 383.04m; ties to press "Total EBITDA*" | res L818 | PASS |
| Footnote-basis margin Q2 FY27 | 16.88% | 497.65 / 2,947.57 = 16.88% | res L817-818, L823 | PASS |
| CON gross margin Q2 FY27 / Q1 / Q2 FY26 / H1 FY27 / FY26 | 34.64 / 42.07 / 41.15 / 38.14 / 41.85% | 1,020.97/2,947.57; 1,104.16/2,624.59; 795.33/1,932.57; 2,125.13/5,572.16; 3,446.24/8,234.34 | res L526, L530-532 | PASS |
| SA Op EBITDA Q2 FY27 / margin | 37.84 / 13.06% | 332.97+102.15+38.94-95.68 = 378.38m; 13.06% | res L187-198 | PASS |
| SA gross margin Q2 FY27 / Q1 / Q2 FY26 | 34.12 / 41.44 / 40.96% | 988.73/2,897.47; 1,064.23/2,568.15; 785.12/1,916.63 | res L187, L191-192 | PASS |
| ETR CON Q2 FY27 (on reported PBT) / pre-JV | 24.32% / 22.54% | 80.40/330.60; 80.40/356.75 | res L541, L543, L547 | PASS |
| ETR SA Q2 FY27 | 22.38% | 74.53/332.97 | res L201, L205 | PASS |
| OI / PBT CON Q2 FY27 / Q1 / Q2 FY26 | 29.35 / 5.53 / 22.56% | 97.04/330.60; 23.12/418.42; 62.91/278.85 | res L527, L543 | PASS |
| SA vs CON PAT gap Q2 FY27 / H1 FY27 / FY26 | (0.82), -3.19% / (1.80), -3.14% / +3.30, +3.69% | -8.24m/258.44; -18.01m/573.49; +33.03m/894.21 | res L206, L548 | PASS |
| SA-CON swing H1 to H1 | 5.83 pp | 2.69 - (-3.14) | rev L188-189 | PASS |
| YoY: revenue / Op EBITDA / D&A / FC / EBIT / OI | +52.52 / +25.14 / +42.16 / +26.80 / +20.21 / +54.25% | 2,947.57/1,932.57; 400.61/320.13; 102.20/71.89; 38.70/30.52; 298.41/248.24; 97.04/62.91 | res L526-538 | PASS |
| YoY: core PBT / core PBT pre-JV / PBT / PAT | +8.16 / +19.29 / +18.56 / +21.24% | 233.56/215.94; 259.71/217.72; 330.60/278.85; 250.20/206.36 | res L538, L543, L548 | PASS |
| QoQ: revenue / PAT / core PBT pre-JV / OI | +12.31 / -18.04 / -39.57 / +319.7% | 2,947.57/2,624.59; 250.20/305.28; 259.71/429.75; 97.04/23.12 | res L526-548 | PASS |
| PAT bridge (8 lines) | +41.77, (19.21), (14.52), (3.03), (0.82), +3.41, (2.44), (1.35), +0.55 = +4.38 | 101.50 x 41.154%; 294.76 x (34.638%-41.154%); 620.36m-475.20m; 30.31m; 8.18m; 34.13m; -24.37m; 5.175 x 25.996%; 33.06 x 1.677 pp. Sum = +4.384 | res L526-548 | PASS |
| OI after tax; OI+ETR share of PAT rise | 2.55; 70.8% | 3.413 x 0.7483 = 2.554; (2.554+0.554)/4.384 = 70.9% | rev L282 | PASS |
| Core PAT Q2 FY27 / Q2 FY26 / Q1 FY27 | 16.82 / 16.11 / 28.71 | 25.971x0.7483-2.615; 21.772x0.7483-0.178; 42.975x0.7483-3.445 | res L527, L538, L542 | PASS |
| Q1 FY26 derived (revenue, margin, core PBT) | 186.30, 20.28%, 26.99 | 1,862.99m; 377.87/1,862.99; 269.93m | res L526-538 (H1 FY26 less Q2 FY26) | PASS |
| H2 FY26 quarterly average (revenue, margin, core PBT) | 221.94, 18.51%, 28.99 | 2,219.39m; 821.59/4,438.78; 289.91m | res L526-538 | PASS |
| CFO H1 FY27 / H1 FY26; CFO/PAT | 22.06 / 38.94; 0.40x / 0.94x | 220.59m/555.48m; 389.44m/412.97m | res L548, L645 | PASS |
| FCF H1 FY27 / H1 FY26 | (5.44) / (6.52) | 220.59-274.99; 389.44-454.68 | res L645, L647 | PASS |
| WC change H1 FY27 / H1 FY26 | (65.28) / (24.55) | -269.31-557.33+173.86; -185.42-275.37+215.26 | res L640-642 | PASS |
| Receivable / inventory / payable days, CCC (Sep-26 vs Mar-26) | 58.55 / 77.43 / 30.02 / 105.96 vs 61.30 / 90.96 / 32.45 / 119.81 | 1,787.77/11,144.32x365; 1,462.54/6,894.06x365; 566.94/6,894.06x365 vs 1,382.99/8,234.34x365; 1,193.23/4,788.10x365; 425.66/4,788.10x365 | res L583-584, L607-608, L526-532 | PASS |
| Gross debt; cash+bank; net cash; ex-earmarked net debt | 191.06; 332.78; (141.73); 182.20 | 299.50+1,611.05; 680.49+2,647.34; 1,910.55-3,327.83; 191.06-(332.78-323.92) | res L585-586, L599, L605, L407 | PASS |
| Realisation Q2 FY27 / Q1 / Q2 FY26 | 261.96 / 239.91 / 194.68 Rs/kg | 2,947.57m/11,252 MT; 2,624.59m/10,940; 1,932.57m/9,927 | res L526; cc L164-166, L356 | PASS |
| EBITDA/kg ex-OI Q2 / Q1 / Q2 FY26; incl-OI Q2 / Q1 | 35.60 / 51.98 / 32.25; 44.23 / 54.09 | 400.61/11.252; 568.61/10.940; 320.13/9.927; 497.65/11.252; 591.73/10.940 | res L526-538, L818 | PASS |
| ROCE checks (annualised Q2) | 17.05% / 26.59% / 20.06%; ROE 13.86% | 1,581.8/9,277.75; 1,581.8/5,949.92; 1,193.64/5,949.92; 1,000.8/7,223.24 | res L534, L538, L527, L596, L599-600, L605-606, L585-586 | PASS |
| TTM revenue / PAT | 1,001.10 / 106.98 | 443.88+557.22; 51.43+55.55 | res L526, L548 | PASS |
| Deck WC "75 days" reproduction | 83 days | (1,787.77+1,462.54-566.94)/11,790.28x365 = 83.07 | res L583-584, L607-608; deck L347 | PASS |
| Rs 54/kg consistency check | 60.8-62.1 Cr; 51.1-52.4 Cr; 17.3-17.8% | 54 x 11,250-11,500 MT; less 9.70; /294.76 | rev L575 | PASS |
| Forward table FY27E revenue (base / R1 / R2) | 1,146.7 / 1,208.9 / 1,097.1 | 557.22+589.51; 557.22x2.1695; 557.22+539.89 | rev L945 | PASS |
| Forward table FY27E PAT (base / R1 / R2) | 112.1 / 131.2 / 103.7 | 112.10 / 131.19 / 103.71 | rev L946 | PASS |
| Forward table FY28E revenue (base / R1 / R2) | 1,244.5 / 1,310.0 / 1,080.0 | 47,500x262; 50,000x262; 45,000x240 | rev L947 | PASS |
| Forward table FY28E PAT (base / R1 / R2) | 122.3 / 166.8 / 81.8 | 122.36 / 166.82 / 81.78 | rev L948 | PASS (rounding) |
| SA period-end EPS YoY | +3.43% | 2.1120/2.0396 = +3.55% (A4 used rounded 2.11/2.04) | res L206, L211 | PASS (rounding basis, STYLE S-01) |
| Core PAT per period-end share YoY | -14.9% | 1.3745/1.6114 = -14.7% | rev L283 | PASS (rounding basis, STYLE S-01) |
| GM YoY change | -651 bps | -652 bps (34.638 - 41.154) | res L526-532 | PASS (rounding basis, STYLE S-01) |
| CON equity increase H1 | +414.15 | 7,223.24-3,081.85 = 4,141.39m = 414.14 | res L596 | PASS (rounding basis, STYLE S-01) |

Result: 0 mismatches above rounding. Four rounding-basis items are logged under STYLE S-01.

---

## 3. ADVERSARIAL READ

### P1. Most positive claim: the ~Rs 150 Cr/yr contract carries HIGH confidence as a "minimum" (rev L562), is a confidence indicator (rev L743) and the one "undisclosed material positive" (rev L836).
Strongest bear counter from the extract:
- The filed deck says "~1,500 Mn Approximate order value per annum" (deck L219), not a minimum. It also says "new order and renewal" (deck L215).
- "Minimum" and "bottom of the 150 crores" are ASR only (cc L406-412). The prepared remarks say "worth about 150 crore per year" (cc L88-89).
- The customer is existing (cc L398). The term ends December 2028 (deck L220), so about 9 of 36 months had run by the 2-Oct-2026 announcement (A4's own inference, rev L32).
- The deck claims "no material dependency on any segment" (deck L240-241). One contract near 18.2% of FY26 revenue (rev L337) contradicts that framing.
Counter survives: YES. A4 tiers an ASR-only floor as HIGH and cites the deck as confirmation. The deck confirms size order and term, not a floor.
Graft (A5-03, MISSING, to A4): Step 2 order-book row (rev L562) and 6D (rev L743) should read "~Rs 150 Cr/yr approximate (deck L219, FILED); 'minimum' is MGMT/ASR only (cc L406-412). Confidence HIGH for existence, size order and Dec-2028 end; LOW for a value floor." Add the deck L240-241 "no material dependency" claim to the concentration watch item (rev L371).

### P2. Most positive claim: the working-capital build is growth- and price-induced on the days test (rev L312), and the 55 Cr receivables outflow is CONFIRMED as the export receivable cycle (rev L691, L768).
Strongest bear counter from the extract:
- The cash-flow line is "Trade and other receivables" 557.33m = 55.73 Cr (res L641). It is not trade receivables alone.
- Trade receivables rose 404.78m = 40.48 Cr (res L584). Other current assets rose 150.27m = 15.03 Cr, +53.5% (res L589). Current other financial assets rose 13.21m (res L588).
- Management's reason, a longer export receivable cycle (cc L437-440), can cover at most the 40.48 Cr trade build. About 15 Cr has no stated cause. That is 68% of H1 CFO (15.03 / 22.06).
- The days test (rev L297-300) covers trade receivables, inventory and payables only, so it cannot see this build. A4 lists the other-current-assets rise (rev L308) but does not connect it to the CFO shortfall.
- I also tested the days comparison for a seasonal bias. Sep-26 days use H1 x 2, a seasonally weaker half (cc L374-375). That bias raises Sep-26 days, so the days improvement survives. This part of the counter fails.
Counter survives: YES (the 15 Cr split), NO (the days test itself).
Graft (A5-04, MISSING, to A4): in Step 5 and 7A, state "of the 55.73 Cr 'trade and other receivables' outflow (res L641), trade receivables explain 40.48 Cr (res L584); other current assets explain about 15.03 Cr (+53.5%, res L589), cause not stated." Reclassify the 7A receivables row from CONFIRMED to PARTIALLY CONFIRMED. Add the other-current-assets split to Question 8 (rev L446).

### P3. Most positive claim: the indicative forward table base, FY28E PAT 122.3 Cr on Rs 43.67/kg (H1 FY27 average), with Reading 1 at 166.8 Cr on Rs 51.98/kg (Q1 FY27) (rev L948).
Strongest bear counter from the extract:
- Both the base and Reading 1 draw on Q1 FY27. Q1 carried a 316.12m (31.61 Cr) FG/WIP build credit (res L532). Q2 carried 2.69m.
- A4's own Step 3 says the Q1 build at rising input costs helps the Q1 margin (rev L258), and its own gate requires the inventory-change credit under 5 Cr (rev L429).
- The forward table does not carry that caveat. Half the base and all of Reading 1 inherit an upward bias. The absorbed-cost share of the build is NOT FOUND.
Counter survives: YES, as a qualifier. The numbers stay; the basis note is missing.
Graft (A5-05, MISSING, to A4): one line under the forward table: "The base (Rs 43.67/kg) and Reading 1 (Rs 51.98/kg) include Q1 FY27, which carried a 31.61 Cr FG/WIP build credit (res L532) that Step 3 says flatters the by-nature margin. Size of the effect NOT FOUND. Both readings carry an upward bias of unknown size."

### Mandatory acquisition-economics probe (stake buy: Sayem Knack JV, 50%)
- Consideration: USD 0.5m capital commitment paid 6-Aug-2025 (res L369); cash "Purchase of equity investment" 43.96m SA = Rs 4.40 Cr (res L305); SA carrying value 45.59m = Rs 4.56 Cr (res L234).
- Target earnings: Knack's share of JV result FY26 (9.41m) = (0.94) Cr; H1 FY27 (60.60m) = (6.06) Cr (res L542). Price / target PAT = Rs 4.40 Cr / negative earnings = NOT MEANINGFUL (loss-making).
- Quality markers: ROCE negative; JV debt NOT FOUND; JV cash NOT FOUND; customer tenure: the partner was "a key strategic customer" (res L368) and exited the JV on 30-Dec-2025 (res L370-371), eight months after formation.
- Stress test: cumulative loss share 7.00 Cr = 1.59x the 4.40 Cr paid, in about 14 months. Consolidated carrying value is nil (res L577). JV sells about 80 MT/month against 400 MT/month installed (cc L462-463).
- Reading: this is not a "cheap, accretive" deal. The bear reading is already in A4 (rev L441-442, L455-456, L1033). No new graft from the probe itself; A5-06 below adds filed evidence to the funding question.

---

## 4. OTHER FINDINGS (outside the three adversarial reads)

A5-01 (CONTRADICTION, to A4). "Very small portion" (cc L486-487) is used as India margin evidence, but the extract places it in a Mexico passage.
- Context: cc L481-485 discuss "installed capacity is only 400, 400 metric ton per month", a "green field project", and interest cost from "long machinery waiting". That is the Mexico JV. The analyst then says "No I'm talking about the India part" (cc L492).
- A4's own Q&A row says "Answer moves to Mexico" (rev L631).
- Yet A4 uses the phrase as India margin evidence at rev L384 (6D killing evidence), rev L690 (5A "negative surprise ... Undercuts 'restore margin from Q3'"), rev L798 (8A WEAKENED basis), rev L867 (Section C) and rev L946 (FY27E PAT basis).
- The India answer itself is cc L478-480: "very difficult to achieve that all the losses in the one quarter but the third quarter will be the winning situation and ... little bit loss also covered".
- Fix: attribute cc L486-487 to the Mexico JV, or mark it ambiguous ASR with both readings. Rest the India "partial recovery" reading on cc L478-480 and cc L547-559 ("not 100%"; 3-4% got when 5% asked). Recast the 5A row. The 15.5% H2 margin base (rev L946) can stand on those lines.

A5-02 (FACTUAL, to A4). All Q2 other income is labelled treasury income, but filed interest is smaller.
- H1 FY27 interest income is 61.33m = 6.13 Cr (res L631). Q2 OI is 97.04m (res L527). So at least 35.71m (3.57 Cr, 36.8%) of Q2 OI is not interest, even if all H1 interest fell in Q2.
- Q2 interest is therefore at most Rs 5.45/kg (61.33m / 11,252 MT), not "about Rs 8.6/kg".
- Affected text: rev L209 ("Treasury income on parked IPO cash"), rev L395 ("treasury on a depleting cash pile"), rev L440 and rev L575 ("treasury income ... about Rs 8.6/kg"), rev L663, and rev L911 ("counts interest income").
- Fix: call it other income; state interest at most Rs 5.45/kg; keep Question 9 for the split. Note that the FY28 OI halving (rev L942) applies FD-draw logic to all OI, including a non-interest part. The 70.8% PAT-bridge share (rev L282) stands because it uses total OI.

A5-06 (MISSING, to A4). Filed evidence that bears on Question 3 ("Against which balance was the excess 2.61 Cr booked?", rev L441) is not used.
- SA other non-current assets 511.54m (res L237); CON 493.33m (res L580). Both were 402.53m at 31-Mar-2026.
- CON sits 18.21m (1.82 Cr) below SA at 30-Sep-2026. Apart from the equity-method line itself (res L577), it is the only asset line where CON is below SA.
- Two readings: (a) about 1.82 Cr of the 2.61 Cr excess JV loss was applied to a long-term interest in the JV held in other non-current assets; (b) an advance to the subsidiary was eliminated. Separating observation: the FY27 annual report note on other non-current assets and related-party balances.
- Fix: add the line pair and both readings to Question 3 (rev L441) and to the JV flag (rev L1033).

A5-07 (MISSING, to A2). The concall question ledger lacks two questions my fresh pass found.
- (i) T05 YoY volume baseline: "what would be the same number last quarter last year ... Do you see in quarter Q2 as per 26?" (cc L164-165), answered "26 was 9,927" (cc L166).
- (ii) T11 pinch-machine margin test: "last year you had only three pinch bottom machines ... third quarter margin should logically be much higher ... Am I on the right track?" (cc L501-511), answered "you are perfectly okay" (cc L511-518).
- Ledger count 26 (led-cc L41-69); fresh count 28. A4 already added (ii) as T11-Q5 (rev L634) and cites (i)'s content (rev L234, L364). A4's 4A inventory still lacks a row for (i), so its grade count (rev L639) moves to 28 rows once (i) is added.

A5-08 (FACTUAL, to A2). The concall question ledger mis-codes two replies.
- T09-Q2 is coded "NUMBER (3%; 9,927 prior)" (led-cc L55). The reply is "YY volume growth is 13%" (cc L363); 9,927 is said in T05 (cc L166).
- T10-Q3 is coded "NUMBER (69-72,000 MT after expansion)" (led-cc L61). The reply (cc L462) gives Mexico capacity only; 69-72k comes from T06 (cc L234).
- A4 already overrides both (rev L30, L623, L629). The ledger still carries the errors.

Tested and dropped (not a finding): QoQ seasonality. FY26 op EBITDA margin also fell from Q1 to Q2 (20.28% to 16.57%, derived, unreviewed). But FY26 gross margin was flat (Q1 41.35%, Q2 41.15%, from res L526-532), so that dip was opex-led. The FY27 QoQ fall is gross-margin led (-743 bps of -807 bps). A4's gross-margin gate (rev L428-431) is the right metric.

---

## FINDINGS REGISTER

| ID | Type | Loop to | Gap | Anchors |
|---|---|---|---|---|
| A5-01 | CONTRADICTION | A4 | "Very small portion" (Mexico JV context) used as India margin evidence in 5 cells | cc L481-492; rev L384, L631, L690, L798, L867, L946 |
| A5-02 | FACTUAL | A4 | All Q2 OI called treasury; filed H1 interest 6.13 Cr caps Q2 interest at Rs 5.45/kg, not Rs 8.6/kg | res L527, L631; rev L209, L395, L440, L575, L663, L911 |
| A5-03 | MISSING | A4 | Surviving bear counter P1: contract is "approximate" (filed), "minimum" is ASR only; HIGH confidence mis-tiered | deck L215, L219, L240-241; cc L88-89, L406-412; rev L562, L743 |
| A5-04 | MISSING | A4 | Surviving bear counter P2: ~15 Cr of the 55.73 Cr receivables outflow is other current assets, not export cycle | res L584, L588-589, L641; cc L437-440; rev L312, L691, L768 |
| A5-05 | MISSING | A4 | Surviving bear counter P3: forward base and Reading 1 inherit the Q1 inventory-build effect; caveat absent | res L532; rev L258, L429, L948 |
| A5-06 | MISSING | A4 | CON vs SA other non-current assets gap 1.82 Cr not used in the JV funding question | res L237, L577, L580; rev L441, L1033 |
| A5-07 | MISSING | A2 | Question ledger lacks 2 questions (fresh 28 vs 26); A4 4A lacks the T05 row | cc L164-166, L501-518; led-cc L41-69; rev L634, L639 |
| A5-08 | FACTUAL | A2 | Question ledger mis-codes T09-Q2 (13%, not 3%) and T10-Q3 (DEFLECTED, not NUMBER) | cc L166, L234, L363, L462; led-cc L55, L61 |

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agent: A4 (A5-01 CONTRADICTION; A5-02 FACTUAL; A5-03, A5-04, A5-05, A5-06 MISSING). Each fix is a text edit with the anchors above. No arithmetic re-run is needed; every derived metric ties.
- Also failing: A2 ledger (A5-07 MISSING; A5-08 FACTUAL). The fix is a concall question-ledger patch: add cc L164-166 and cc L501-511 as questions; recode T09-Q2 to 13% (cc L363) and T10-Q3 to DEFLECTED (cc L462). A4 already carries this content except the T05 4A row. Apply the patch in the same remediation cycle. No A3 re-run is needed, because no new interpretation is involved.
- Routing: loop_back_to = A4 (six of eight loop findings), with the A2 ledger patch named in the gap.

---

## STYLE NOTES (logged, no loop)

- S-01. Rounded-input derivations. rev L231 SA period-end EPS YoY +3.43% (2.11/2.04); unrounded +3.55%. rev L283 core PAT per share -14.9%; unrounded -14.7%. rev L763 GM YoY -651 bps; unrounded -652 bps. rev L85 equity +414.15 Cr; unrounded 414.14 Cr. Derive from unrounded inputs, as the CON EPS row already does (rev L215).
- S-02. rev L385 "Utilisation % declined (cc L214-215)" reads as a fall. Management declined to state it, and gave 60-70% for the new machines (cc L189-191, L199). Write "not stated".
- S-03. rev L917 tags "FY26 H2 revenue was 16.9% above H1" as FILED. It is derived from res L526, so tag it INFERENCE.
- S-04. rev L119 anchors the pre-exceptional PBT row to "L538/L541". The values are L538 (FY26 127.08 = 1,270.81m); L541 is post-exceptional (1,260.04m). Anchor to L538 only.

---

```yaml
stage: A5-adversary
company: "KNACK"
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
  missing_from_ledger:
    - "concall T05 question: YoY volume baseline 'same number last quarter last year ... Q2 as per 26?' (cc L164-165), answer 9,927 MT (cc L166)"
    - "concall T11 question: 3 vs 5 pinch-bottom machines, should Q3 margin beat last year's Q3 (cc L501-511), answer 'perfectly okay' (cc L511-518)"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "~Rs 150 Cr/yr contract is a HIGH-confidence minimum confirmed by deck (rev L562, L743, L836)", counter: "Deck files '~1,500 Mn Approximate order value per annum' and 'new order and renewal'; 'minimum' is ASR only; prepared remarks say 'about'; existing customer; deck also claims 'no material dependency' against an ~18.2% contract", source_line: "deck L215, L219, L240-241; cc L88-89, L398, L406-412", type: "MISSING"}
  - {claim: "WC build is growth/price-induced; 55 Cr receivables outflow CONFIRMED as export cycle (rev L312, L691, L768)", counter: "CF line is trade AND other receivables 55.73 Cr; trade receivables rose 40.48 Cr; other current assets rose 15.03 Cr (+53.5%) with no stated cause, 68% of H1 CFO", source_line: "res L584, L588-589, L641; cc L437-440", type: "MISSING"}
  - {claim: "Forward table base FY28E PAT 122.3 Cr on Rs 43.67/kg; Reading 1 166.8 Cr on Rs 51.98/kg (rev L948)", counter: "Both draw on Q1 FY27, which carried a 31.61 Cr FG/WIP build credit that A4's Step 3 says flatters the by-nature margin; caveat absent from the table; size NOT FOUND", source_line: "res L532; rev L258, L429", type: "MISSING"}
findings_by_type:
  factual:
    - {id: "A5-02", target: "A4", gap: "Q2 OI 9.70 Cr labelled treasury throughout; filed H1 interest income 6.13 Cr (res L631) caps Q2 interest at Rs 5.45/kg, not Rs 8.6/kg; at least 3.57 Cr of Q2 OI is non-interest (rev L209, L395, L440, L575, L663, L911)"}
    - {id: "A5-08", target: "A2", gap: "Question ledger codes T09-Q2 as 3%/9,927 (reply is 13%, cc L363; 9,927 is T05 cc L166) and T10-Q3 as NUMBER 69-72k (reply is Mexico capacity, cc L462) (led-cc L55, L61)"}
  missing:
    - {id: "A5-03", target: "A4", gap: "Contract 'approximate' (deck L219) vs ASR 'minimum' (cc L406-412); HIGH confidence for a floor is unsupported (rev L562, L743)"}
    - {id: "A5-04", target: "A4", gap: "About 15.03 Cr of the 55.73 Cr receivables outflow is other current assets (res L589, L641), not export cycle; 7A CONFIRMED overstates (rev L691, L768, L312)"}
    - {id: "A5-05", target: "A4", gap: "Forward table base and Reading 1 inherit Q1 FY27 inventory-build effect (res L532; rev L258); qualifier absent (rev L948)"}
    - {id: "A5-06", target: "A4", gap: "CON other non-current assets 1.82 Cr below SA at 30-Sep-2026, nil gap at 31-Mar-2026 (res L237, L580); not used in JV funding Question 3 (rev L441) or flag (rev L1033)"}
    - {id: "A5-07", target: "A2", gap: "Concall question ledger lacks cc L164-166 (T05) and cc L501-511 (T11); fresh count 28 vs 26; A4 4A lacks the T05 row (rev L639)"}
  contradiction:
    - {id: "A5-01", target: "A4", gap: "'Very small portion' (cc L486-487, Mexico JV context per cc L481-485, L492 and A4's own rev L631) used as India margin evidence at rev L384, L690, L798, L867, L946"}
  style:
    - {id: "S-01", gap: "Rounded-input derivations: rev L231 +3.43% (unrounded +3.55%), rev L283 -14.9% (-14.7%), rev L763 -651 bps (-652), rev L85 414.15 (414.14)"}
    - {id: "S-02", gap: "rev L385 'Utilisation % declined' reads as a fall; management declined to state it (cc L214-215), gave 60-70% (cc L189-191)"}
    - {id: "S-03", gap: "rev L917 'FY26 H2 revenue 16.9% above H1' tagged FILED; it is derived, tag INFERENCE"}
    - {id: "S-04", gap: "rev L119 anchor 'L538/L541'; values are L538 only"}
loop_back_to: "A4"
gap: "A4: (1) A5-01 CONTRADICTION: re-attribute 'very small portion' cc L486-487 to the Mexico JV at rev L384, L690, L798, L867, L946; rest India partial recovery on cc L478-480 and L547-559. (2) A5-02 FACTUAL: relabel Q2 OI as other income; interest at most Rs 5.45/kg (res L631), not Rs 8.6/kg. (3) A5-03 MISSING: contract is '~1,500 Mn approximate' (deck L219); 'minimum' is ASR only; confidence HIGH for term, LOW for floor. (4) A5-04 MISSING: 55.73 Cr outflow = 40.48 Cr trade receivables + about 15.03 Cr other current assets (res L584, L589, L641); 7A to PARTIALLY CONFIRMED; add to Q8. (5) A5-05 MISSING: caveat that forward base and Reading 1 inherit the Q1 31.61 Cr build credit (res L532). (6) A5-06 MISSING: add CON vs SA other non-current assets gap 1.82 Cr (res L237, L580) with two readings to Q3 and the JV flag. A2 ledger patch in the same cycle, no A3 re-run: (7) A5-07 MISSING: add questions cc L164-166 (T05) and cc L501-511 (T11); A4 adds the T05 row to 4A. (8) A5-08 FACTUAL: recode T09-Q2 to 13% (cc L363) and T10-Q3 to DEFLECTED (cc L462)."
style_notes:
  - "S-01 rounded-input derivations (rev L231, L283, L763, L85); use unrounded inputs"
  - "S-02 rev L385 'declined' ambiguous; write 'not stated'"
  - "S-03 rev L917 derived H2/H1 ratio tagged FILED; tag INFERENCE"
  - "S-04 rev L119 anchor L538/L541; use L538"
analyst_note: "Routing: loop_back_to is A4 because six of eight loop findings change A4 text. The two A2 items are ledger-only (two unlisted questions, two mis-coded replies), and A4 already carries their content except one 4A row, so patch the concall question ledger in the same remediation cycle without an A3 re-run. Arithmetic: every derived metric was recomputed from raw lines and ties within rounding. Seasonality was tested and dropped: FY26 op EBITDA margin also fell Q1 to Q2 (20.28% to 16.57%), but FY26 gross margin was flat (41.35% to 41.15%), so the FY27 QoQ fall is gross-margin led and A4's gross-margin gate stands. Symmetry: A5-01 and A5-02 make A4 more bearish than the extract supports. The fix is evidence attribution; the 15.5% H2 margin base can stand on cc L478-480 and L547-559. Acquisition probe: JV stake Rs 4.40 Cr for 50%, earnings negative, multiple not meaningful; cumulative loss share 7.00 Cr = 1.59x consideration. That bear reading is already in A4."
```
