# A5 ADVERSARY / COMPLETENESS AUDIT: WeWork India Management Ltd (WEWORK), Q2 FY27

Agent: A5 Adversary, model claude-opus-5-5. Date: 2026-10-28.
Review under audit: runs/wework-q2fy27/work/review_wework_q2fy27.md (1,165 lines, read in full).

Inputs read: the five A1 fulltexts and the five A1 structured files (row-ID counts and spot checks) in runs/wework-q2fy27/extracted/. I also read the five A2 ledgers in runs/wework-q2fy27/work/.
Inputs not read: no source PDF, nothing under inputs/, no A3 forensics file, no orchestrator log. Disclosure: one cross-file grep for "MFS-1|orphan" also printed one line each from forensics_letter, forensics_deck and run-log.md. I did not use those lines. Every finding below is re-derived from the fulltexts.

Anchor convention: "results L499" = results fulltext line 499. Deck, letter, press and concall anchors are fulltext lines in the same way. "rev L" = review line.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate): PASS

| Brief part | Location in review | Status | Note |
|---|---|---|---|
| 1. Summary narrative | rev L990-1011 | present | 20 lines (within 10-20); real content, provenance-tagged |
| 2. Sector intelligence | rev L1013-1025 | present | flex share, GCC share, lease-length shift, wage and tariff costs, Labour Codes, campus moves |
| 3. Business-model intelligence | rev L1027-1043 | present | lessee model, cash rent, lock-in terms, Ind AS 116 mechanics, deposit float, managed-office mix |
| 4. Competition intelligence | rev L1045-1060 | present | share claims (modelled), brand, Grade A, structural weak points; states that the peer page was not passed |
| 5. Forward map | rev L1062-1077 | present | make-or-break reading plus 9 catalysts, each with a bull and a bear fork; 7 dated, 1 per-call, 1 "Undated" (dates NOT FOUND in filings; see STYLE S9) |

All five parts are present and non-empty. The gate passes.

---

## 1. COVERAGE AUDIT: PASS (no orphan rows, nothing missing from the ledgers)

Fresh pass method: I ran my own grep pass over each A1 fulltext, then counted units by hand against the fulltext lines. I counted structured row IDs with a separate grep (pattern `^\|?\s*R\d{3,4}`). I diffed both against the A2 ledgers.

| Document | Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | pages ([page N] markers) | 12 | 12 | - | PASS |
| Results | numbered notes, SA + CA | 21 | 21: SA 1)-2) + 3-10 (results L194, L250, L316-358); CA 1)-2) + 3, 4, unnumbered 5 (L676), 6-11 (L535-704) | 0 | PASS |
| Results | financial line items | 232 | 232: SA P&L 25 (L158-187), SA BS 36 (L199-244), SA CF 44 (L254-303), CA P&L 35 (L486-528), CA BS 43 (L540-592), CA CF 46 (L602-653), Note 11 3 (L709-711) | 0 | PASS |
| Results | agenda items | 2 | 2 (L52, L60) | 0 | PASS |
| Results | auditor paragraphs | 10 | 10: SA 1-4 (L101-126), CA 1-6 (L387-442) | 0 | PASS |
| Results | consolidation entities | 4 | 4 (L419-424) | 0 | PASS |
| Results | structured row IDs | 1,112 | 1,112 | 0 | PASS |
| Concall | 10-minute time blocks | 7 | 7 | - | PASS |
| Concall | speaker turns | 56 | 56 (sub-second interjections at L649-653 and L816-819 fold into T22/T36 under A2's convention) | 0 | PASS |
| Concall | analyst questions | 19 | 19: L246, L304, L348, L404, L526, L581, L660, L674, L686, L734, L743, L789, L848, L877, L897, L913, L921, L926, L936 | 0 | PASS |
| Concall | participants | 13 rows | 11 distinct people (CEO, finance speaker, moderator, 8 analysts); A2's 2 extra rows are name variants (R237, R262 "Clifford") | 0 | PASS (explained) |
| Concall | structured row IDs | 470 | 470 | 0 | PASS |
| Deck | slides | 40 | 40 | 0 | PASS |
| Deck | structured row IDs | 1,392 | 1,392 | 0 | PASS |
| Letter | pages | 31 | 31 | 0 | PASS |
| Letter | structured row IDs | 1,570 | 1,570 | 0 | PASS. A2 logged MFS-1 (p31 Note 8 paid-up capital not split into rows) in ledger section 8. The ledger does not lack it, and the values already sit at R965/R966/R1177-R1182. No loop. |
| Press | pages | 5 | 5 | 0 | PASS |
| Press | structured row IDs | 197 | 197 | 0 | PASS |
| A4 vs ledgers | ledger units reviewed | 21 notes / 56 turns / 76 slides | A4 0D covers all 21 notes; 4A covers all 19 questions; A4 marks "Unreviewed ledger rows: none" (rev L30) | 0 | PASS |
| A4 vs A3 | finding IDs incorporated | 97 | 97 listed; 83 FS/AMB + 2 CN mapped to questions | 0 | PASS (L-F1-a missing from the mapping table but mapped in Q12: STYLE S4) |

Fresh-pass spot checks: I took figures from the fulltexts that A4 did not use and searched for each one in the structured files. All were present: press 97% (R085), 40.8% (R061, R091), 13.0 msf (R068), Q2 FCFF 61.9 (press R054; concall R162), concall "67%" contracted escalation (R176, flagged ASR), 1.2 million campus (R227), and 1.2-1.5x (R200). missing_from_ledger: none.

---

## 2. ARITHMETIC AUDIT: PASS (no mismatch above rounding)

I recomputed from raw Rs Million lines (x0.1 to Rs Cr). I checked every line-item cell in tables 1-C and 1-S (138 CA and 126 SA cells) against results L158-187 and L486-528. All match within 0.01 Cr.

| Metric | A4 value | Recomputed (A5) | Source line | Status |
|---|---|---|---|---|
| CA Op EBITDA Q2 FY27 | 490.14 | 195.82+3,142.49+1,749.13-110.98-75.03 = 4,901.43 Mn = 490.14 | results L487-499 | PASS |
| CA Op EBITDA Q1 FY27 / Q2 FY26 | 437.98 / 380.08 | 437.98 / 380.08 | L487-499 | PASS |
| CA Op EBITDA H1 FY27 / H1 FY26 / FY26 | 928.12 / 715.84 / 1,573.56 | 928.12 / 715.84 / 1,573.56 | L487-499 | PASS |
| CA Op EBITDA margin Q2 FY27 / Q2 FY26 | 63.8% / 66.1% | 63.83% / 66.14% | derived | PASS |
| CA margin change YoY | -231 bps | -230 bps | derived | PASS (rounding; S1) |
| CA Reported EBITDA Q1 FY27 | 454.88 | 454.89 | L494, L495, L499 | PASS (rounding) |
| CA core PBT ex OI, FI (Q2 FY27 / Q1 / Q2 FY26 / H1 FY27 / H1 FY26 / FY26) | 0.98 / (20.95) / (4.33) / (19.96) / (28.48) / 4.84 | identical | L487, L488, L499 | PASS |
| CA (OI+FI)/PBT Q2 FY27 / H1 FY27 | 91.0% / 215.1% | 90.95% / 215.10% | L487, L488, L503 | PASS |
| CA ETR FY26 | (41.6%) | (41.63%) | L503, L507 | PASS |
| CA PAT margin Q2 FY27 / Q2 FY26 | 2.66% / 1.12% | 2.66% / 1.115% | L486, L508 | PASS (rounding) |
| SA Op EBITDA Q2 FY27 / Q2 FY26 / FY26 | 489.86 / 380.70 / 1,572.29 | identical | results L159-170 | PASS |
| SA (OI+FI)/PBT FY26 | 99.4% | 99.3% (497.04/500.44) | L159, L160, L172 | PASS (last digit; S1) |
| SA margin change YoY | -244 bps | -243 bps | derived | PASS (rounding; S1) |
| SA vs CA PAT gap Q2 FY27 (Rs Cr / %) | 1.00 / +5.1% | 0.999 / +5.14% | L177, L508 | PASS |
| SA vs CA gap swing YoY | 18.4 pp | 5.14 - (-13.28) = 18.42 pp | L177, L508 | PASS |
| Subsidiaries + eliminations Q2 FY27 / H1 FY27 | 0.13 / 0.56 | 0.13 / 0.56 | L500, L447 | PASS |
| Revenue YoY (CA / SA) | +33.6% / +33.6% | +33.61% / +33.55% | L486, L158 | PASS |
| Op EBITDA YoY (CA) | +29.0% | +28.96% | derived | PASS |
| D&A YoY / Finance cost YoY | +35.9% / +14.2% | +35.92% / +14.18% | L495, L494 | PASS |
| Op EBIT YoY | +18.1% | +18.15% (Cr) / +18.16% (Mn) | derived | PASS (rounding) |
| Reported PBT YoY / PAT YoY | +227.7% / +218.9% | +227.8% / +219.0% (raw Mn) | L503, L508 | PASS (rounding) |
| EPS diluted YoY | +208.5% | +208.5% | L528 | PASS |
| IGAAP-EQ: total revenue, EBITDA, PAT YoY | +31.6%, +37.6%, +67.4% | +31.63%, +37.58%, +67.43% | deck L327-330; letter L662-698 | PASS |
| IGAAP-EQ margin change | +92 bps | +92 bps (21.19% vs 20.27%) | deck L593, L327 | PASS |
| IGAAP-EQ EBITDA ex finance and other income | 112.8 to 160.7, +42.5% | 118.4-5.6, 162.9-2.2; +42.46% | deck L705; letter L664 | PASS |
| IGAAP-EQ PAT at 25.17% | 49.2 | 49.24 | deck L327 | PASS |
| Ind AS-to-IGAAP PAT adjustment | 33.2 to 45.3, +36% | 33.2 / 45.3 (PBT-before-associate level), +36.4% | letter L684 | PASS |
| Rent-adjusted Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 | 186.1 (24.2%) / 154.1 (22.5%) / 128.8 (22.4%) | 186.14 (24.24%) / 154.08 (22.53%) / 128.78 (22.41%) | deck L794, L797 | PASS |
| Rent-adjusted YoY | +44.5%, +184 bps | +44.54%, +183 bps | derived | PASS (rounding; S1) |
| Q1 FY26 [derived] revenue / margin / core PBT | 535.31 / 62.7% / (24.15) | identical | L486-499 | PASS |
| H2 FY26 block revenue / margin / core PBT | 1,330.17 / 64.5% / 33.32 | identical | L486-499 | PASS |
| Revenue QoQ Q2 FY27 | +12.3% | +12.29% | L486 | PASS |
| IGAAP-EQ margin Q1 FY26 | 15.0% | (200.0-118.4)/(1,127.3-584.0) = 15.02% | deck L619, L599; letter L727 | PASS |
| PAT bridge: revenue at prior margin / margin change | +127.73 / (17.67) | 193.14 x 66.135% = 127.73; 767.84 x -2.302 pp = (17.67) | derived | PASS (label says -2.31 pp; S1) |
| PAT bridge: D&A / FC / OI / FI / associate / tax | (83.04) / (21.72) / +10.58 / (2.82) / +1.14 / (0.19) | identical | L494-507 | PASS |
| PAT bridge sum vs reported | +14.03 | components 14.01 + rounding 0.02 = 14.03 | L508 | PASS |
| Recurring core / OI+FI share | +5.30 (37.8%) / +7.76 (55.3%) | identical | derived | PASS (arithmetic; see adversarial claim 1 for composition) |
| SA bridge | +12.05; core +4.33 (35.9%) | identical | L164-177 | PASS |
| H1 OI composition | 18.44 vs OI 18.46 | 4.70+5.25+2.83+5.24+0.10+0.32 = 18.44 | L607-613 | PASS |
| CFO H1 FY27 / H1 FY26, YoY | 1,026.16 / 697.92, +47.0% | identical, +47.03% | L627 | PASS |
| Lease cash (principal + interest) | 588.01 / 495.80 | 2,758.58+3,121.53 Mn; 2,460.85+2,497.10 Mn | L643-644 | PASS |
| Lease-adjusted CFO | 438.15 / 202.12, +116.8% | identical | derived | PASS |
| FCF after lease, capex, ROU | (3.99) / (73.52) | 1,026.16-588.01-363.77-78.37; 697.92-495.80-207.69-67.95 | L627-644 | PASS |
| WC change (sum of L617-624) | +126.54 / (10.08) | 10,655.03-9,389.64; 7,187.23-7,288.06 | L615, L625 | PASS |
| Receivable days Mar-26 / Sep-26 | 12.7 / 8.8 | 12.66 / 8.78 | L558, L486 | PASS |
| Payable days / CCC | 40.8 / 33.6; (28.1) / (24.8) | 40.79 / 33.61; (28.13) / (24.83) | L585-586, L491-497 | PASS |
| Lease liabilities Mar-26 / Sep-26 | 5,217.53 / 5,233.12 | identical | L575, L583 | PASS |
| Borrowings | 332.77 / 390.21, +17.3% | identical, +17.26% | L574, L582 | PASS |
| Cash + other bank + current investments | 318.47 / 390.40 | 318.47 / 390.41 | L557-560 | PASS (rounding) |
| Net debt ex leases | 14.30 / (0.19) | 14.30 / (0.20) raw | derived | PASS (rounding) |
| DTA / equity | 90.0% | 307.71 / 342.07 = 89.96% | L550, L571 | PASS |
| SA FCF after lease, capex, ROU; SA net debt | (5.58) / (74.15); 6.67 / 19.44 | identical | results L213-303 | PASS |
| Trailing-four-quarter CA PAT; deferred-tax credit inside it | 99.03; 22.39 | 74.92+7.74+16.37 = 99.03; H2 FY26 22.22 + H1 FY27 0.18 = 22.39 | L506, L508 | PASS |
| Lease-inclusive ROCE cross-check | 12.6% | 703.56 / 5,575.00 = 12.62% | derived | PASS |
| Lease liabilities / equity; / annualised IGAAP-EQ EBITDA | 15.3x; 8.0x | 15.30x; 8.03x | L571-583; deck L327 | PASS |
| Book equity ex DTA | 34.4 | 34.36 | L550, L571 | PASS |
| ESOP dilution; exercise price | 2.58%; ~Rs 49 | 2.58%; Rs 49.18 (171.75 Mn / 3,492,205) | L184, L640, L693 | PASS |
| Other-auditor PAT share Q2 / H1 | 5.9% / 11.4% | 5.89% / 11.39% | L446-452, L508 | PASS |
| Net-cash gap to filed | 22.9 | 413.3 - 390.4 = 22.9 | deck L677 | PASS |
| Company FCFF vs full-basis rebuild | 16.0 vs (3.99) | gap 19.99 = finance-lease payout 11.4 + (78.37 - 69.8) = 19.97 | deck L663-667, L796; results L631 | Arithmetic PASS; interpretation is FACTUAL F1 |
| Centre-level EBITDA implied base | 753.5 | 214.0 / 0.284 = 753.5 | deck L577 | PASS |
| Opex-adjustment residual range | 0.8-15.2 | Q2 FY27 328.1-298.2-29.1 = 0.8; H1 FY26 533.1-482.3-35.6 = 15.2 | letter L668, L729, L783, L796, L810-811 | PASS |
| Rent-to-revenue, accrual / cash (Q2 FY27, Q1, Q2 FY26) | 42.8 / 45.7 / 46.9; 38.9 / 40.5 / 42.5 | 42.81 / 45.66 / 46.85; 38.90 / 40.51 / 42.46 | deck L710, L795, L526-528 | PASS |
| Core revenue per member YoY | -0.7% | (657.7/121.7) / (499.5/91.8) - 1 = -0.68% | deck L528, L500-503 | PASS |
| Q25 negative carry | ~3.7 pts | 9.98% (borrowing interest paid, annualised) - 6.32% (MF + FVTPL gains on average MF book) = 3.66 | L641, L608-609, L557 | PASS |
| Concall: Q&A share / quantified share / specificity / hedge count | 69% / 91.7% / 0.52 / 13 | 69.4% / 33/36 / 11/21 / 13 (each line verified) | concall L239, L948, L374-946 | PASS |
| 8C members needed at 83.7% on 149.8k | 125.4k (+3.7k) | 125.38k | deck L314, L319 | PASS |
| H2 FY27 capex room | ~136 | 500 - 363.8 = 136.2 | concall L927 | PASS |

Arithmetic verdict: no mismatch above rounding. Six last-digit rounding differences are logged under STYLE S1.

---

## 3. ADVERSARIAL READ: three most positive claims, three surviving counters

Acquisition-economics probe: NOT TRIGGERED. No document describes an acquisition, a business purchase or a stake buy. A grep for acqui/stake/consideration returns only the PPE "Acquisition of property, plant and equipment" cash-flow lines (results L280, L629; letter L1723, L1852). The 10 MWp solar plant (results L60-65) is capex. The "largest deal ever" (concall L370-373) is a customer lease. The adjacent-business intent (concall L387-400) has no counterparty, amount or date. The H1 FY26 purchase of non-current investments (2.17 Cr, results L634) is a prior period, and no document describes it. No purchase multiple can be computed, and none is claimed.

### Claim 1 (most positive): core Ind AS profit is recovering and the recurring core drove the PAT rise
A4 text: "Core Operating PBT (ex OI and FI) (4.33) to 0.98: turned barely positive" (rev L208). Also "revenue STEPPING UP; core Ind AS profit RECOVERING" (rev L270), and "recurring core (revenue + margin - D&A - finance cost) = +5.30 Cr, 37.8% of the PAT change" (rev L296).

Strongest bear counter (from the same extract): the reconciliation tables show an Ind AS-only adjustment on the revenue line (letter L662; deck L704-706). Ind AS revenue sat 3.7 Cr below the IGAAP-EQ (billed) line in Q2 FY26, 3.5 Cr below in Q1 FY27 and 1.3 Cr above in Q2 FY27. The YoY swing is +5.0 Cr; the QoQ swing is +4.8 Cr. The documents never define this adjustment. The press note (L191-192) describes the IGAAP-EQ basis as excluding "non-cash rent straight-lining". The adjustment has no matching cost line, so it reaches Ind AS PBT one for one. On billed revenue [derived]:
- Revenue growth is 32.5% (deck L537), not 33.6%.
- Core PBT ex OI and FI is (0.32) Cr in Q2 FY27 against (0.63) Cr in Q2 FY26 and (17.45) Cr in Q1 FY27.
- The "recurring core" is about +0.3 Cr, not +5.30 Cr. About 94% of it is the revenue-adjustment swing.
- With OI and FI, 12.76 Cr of the 14.21 Cr PBT rise (90%) comes from items outside billed operating profit.
- On H1, the swing is +4.1 Cr (H1 FY26 -6.3, H1 FY27 -2.2; letter L723). Billed-basis H1 core improves 4.42 Cr, not 8.52 Cr.
Two readings: (bear) a non-cash accrual from member incentives on the new-centre fill, which reverses over the contract term; (bull) an immaterial definitional item, 0.17% of Q2 revenue. Separating observation: the sign and size of this line in Q3 FY27, and its definition (add to Q12).
Survives: YES. Not in the review: a grep for "(1.3)", "3.7 Cr" and "revenue adjustment" finds no instance. GRAFT into Step 2 diagnostic 3, the Step 4 mandatory answers, Section C and brief section 1. TYPE: MISSING.

### Claim 2: lease-adjusted free cash flow is near breakeven and improving
A4 text: "Lease-adjusted FCF after capex and ROU additions: (3.99) Cr in H1 vs (73.52) Cr a year ago: near breakeven, improving" (rev L940). Also "Direction: improving" (rev L356), and brief L1004-1005.

Strongest bear counter: the WC swing accounts for the whole 69.53 Cr improvement. WC moved from (10.08) to +126.54 Cr (results L615, L625), a 136.62 Cr swing. A4 itself calls this inflow growth-linked float that stops when growth stops (rev L352). Excluding WC [derived from results L615-644]:
- H1 FY26: 708.00 - 495.80 - 207.69 - 67.95 = (63.44) Cr.
- H1 FY27: 899.62 - 588.01 - 363.77 - 78.37 = (130.53) Cr.
- The ex-float measure worsened by 67.09 Cr.
- Lease-adjusted CFO before WC was 96.4% of rent-adjusted operating EBITDA in H1 FY26 (212.20 / 220.04). It was 91.6% in H1 FY27 (311.61 / 340.11). Higher cash tax (39.34 vs 20.80 Cr, L626) is part of that.
Two readings: (bull) deposits and upfront customisation cash rise structurally with longer contracts, at a stated 1.2-1.5x FCFO/EBITDA (concall L665-673); (bear) the float reverses when seat growth slows, since deposits are taken "purely on any expansion of seats" (concall L677-679). Separating observation: the member security-deposit balance and the H2 FY27 WC line when Nov-Mar desk adds slow (A4 Q3 already asks).
Survives: YES. A4 names the float but never states the ex-float direction, and it labels the cash-conversion direction "improving". GRAFT into Step 5 (cash-conversion paragraph and direction label), Section C and brief section 1. TYPE: MISSING.

### Claim 3: the operating spread improves on a cash-rent basis ("real operating leverage")
A4 text: "Cash rent fell from 42.5% to 38.9% of revenue YoY. That is real operating leverage on a cash basis" (rev L1037-1038). Also the rent-adjusted margin "24.2% ... +184 bps ... On a cash-rent basis the operating margin improved" (rev L242), and "operating spread is improving on a cash-rent basis" (rev L953).

Strongest bear counter: management says landlord rent-free periods expire in Q3, when rentals start "hitting the P&L in full force" (concall L723-730). Cash rent paid to landlords rose 21.4% YoY, from 245.6 to 298.2 Cr (deck L795). Operational area rose 27.1% (deck L310) and desks 26.9%. Period-end cash rent per operational sq ft therefore fell about 4.5% [derived]. Part of the Q2 cash-rent ratio is a timing effect from the 18.4k H1 openings, and it reverses in Q3. Two readings: (bear) rent-free timing; (bull) a cheaper-city mix, with desks YoY up 94.1% in Hyderabad and 133.7% in Chennai against 7.9% in Bengaluru and 5.3% in Mumbai (deck L404-408). Separating observation: Q3 FY27 cash rent (A) per operational sq ft.
Survives: YES. Partly in the review already: Step 3 (rev L273), watch item 3 (rev L407) and Q7 carry the rent-free expiry. It is absent at the three places where the positive claim is made (brief section 3, Section C net-thesis line, analyst_note). GRAFT the qualifier and the per-sq-ft figure there. TYPE: MISSING.

---

## 4. OTHER FINDINGS (FACTUAL / CONTRADICTION)

**F1. FACTUAL: FCFF is classed as "does not rebuild" and its formula as missing evidence. The extract discloses the formula and the bridge closes.**
A4 (rev L356 item 2, L484 Q2, L948, L1001-1002, flags L1148) says the company FCFO and FCFF formulas are missing. It lists FCFF with net cash, ROCE and order-book cover as headline claims that "do not rebuild from the filed statements". Deck p28 (L660-667) gives the formula line by line: CFO 1,026.2 - "lease liability outflow" (576.6) - "actual brokerage outflow" (69.8) = FCFO 379.8; FCFO - capex 363.8 = FCFF 16.0. Deck L795-797 shows that 576.6 is rent paid to landlords (A) only; the finance-lease payout (B) of 11.4 Cr sits outside it. The gap to A4's full-basis rebuild (3.99) is 19.99 Cr = B 11.4 + ROU-addition payments above the brokerage line (78.37 - 69.8 = 8.57) = 19.97 Cr. That ties within rounding. CFO, capex and lease cash tie to filed lines (results L627, L629, L643-644); only the A/B split and the brokerage figure are management-tier. Fix: classify FCFF as "rebuilds; the company definition leaves out 20.0 Cr of lease-related cash (11.4 Cr finance-lease payout, 8.6 Cr ROU payments)". On a full basis FCFF is (4.0) Cr. Narrow Q2 to two asks: why finance-lease payouts sit outside FCFO, and what the 8.6 Cr of non-brokerage ROU payments is. Keep net cash, ROCE and order book as the KPIs that do not rebuild. Loop: A4.

**C1. CONTRADICTION: capacity measurement-date "ambiguity".**
The flags (rev L1154) list a "capacity measurement-date ambiguity". The Q5 bear answer (rev L487) posits "Capacity includes October desks (Q2 add ~7.2k, not 11.7k)". Three sources place 145.3k at 30-Sep:
- press L88-90: "taking operational capacity to 145.3k desks ... with a further 4.5k desks operationalised in the first week of October";
- deck L429-435: Mar-26 126.9k plus the 18.4k H1 adds = Sep-26 145.3k;
- concall L701-706: "over and above this [1]45,000 that you're seeing, which ended in September 30th". A4 reads this line itself in header item 2 (rev L9).
A4 also computes 145.3k + 4.5k = 149.8k at Step 8C (rev L473) and M3. Fix: drop the ambiguity from flags and from the Q5 bear answer. Keep Q5's request for same-basis March/June occupancy and H1-cohort occupancy. Loop: A4.

**C2. CONTRADICTION: "few new ROU in H1" against Step 3's front-loading explanation.**
Step 5-C (rev L326) marks ROU assets "Ageing; few new ROU in H1". Step 3 (rev L270) attributes the core-profit dip to front-loaded Ind AS cost on new leases from the 18.4k H1 desks. The extract settles it in Step 3's favour. Net ROU additions in H1 = 4,503.09 - 4,593.90 + H1 ROU depreciation 438.3 = about 347.5 Cr [derived; results L542, letter L735]. Net new lease liabilities = 15.59 + principal repaid 275.86 = about 291.5 Cr [derived; results L575, L583, L643]. The lease book stayed flat because principal repayment offset new recognition, not because few leases were added. Fix: replace the cell verdict with the derived additions. Loop: A4.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. Coverage and arithmetic pass, and the brief gate passes. The loop fires on these findings:
- F1 FACTUAL: FCFF mis-classed as non-rebuilding; formula present at deck L660-667.
- C1 CONTRADICTION: capacity-date ambiguity against press L88-90, deck L429-435, concall L701-706 and A4's own 149.8k.
- C2 CONTRADICTION: "few new ROU" against ~347.5 Cr derived net ROU additions.
- M1 MISSING: surviving counter 1 (revenue-adjustment swing, 94% of the recurring core).
- M2 MISSING: surviving counter 2 (FCF improvement is entirely WC float; ex-float (63.44) to (130.53) Cr).
- M3 MISSING: surviving counter 3 (cash-rent leverage partly landlord rent-free timing).
No A2 or A3 re-run is needed. The probable effect on the protocol verdict (PROCEED WITH FLAGS) is none; the A4 re-run states it.

---

## STYLE NOTES (logged, no loop)

- S1. Rounding, all within one unit of the last digit:
  - SA FY26 (OI+FI)/PBT 99.4% recomputes to 99.3%.
  - CA YoY margin change -231 bps is -230; SA -244 is -243.
  - Rent-adjusted +184 bps is +183.
  - The PAT-bridge label says -2.31 pp, but the 17.67 Cr figure uses -2.30 pp.
  - Recompute from raw Rs Million for consistency.
- S2. Brief L999-1000: "Without that income, core pretax profit was about Rs 1.0 Cr". The 0.98 also strips the 0.87 Cr associate share (20.45 - 18.60 = 1.85). Say so in the sentence.
- S3. Brief L988 says every figure comes from this quarter's documents. L1010 (Rs 641, 86.6x) comes from screener.in. Tag that line SECONDARY, not an analysis input.
- S4. L-F1-a is absent from the finding-to-question mapping table (rev L519-562), which shows 16 letter rows against the stated 17. The Q12 "From findings" column does map it.
- S5. The preamble does not name A2 letter MFS-1, although 0C/0D cover its content. Name it for transparency.
- S6. Section B claim 4 (rev L616) equates ~10 msf with ~26% of space. Deck L247-250 shows 7.5 MSF branded = 26%, while 10/29 = 34%. Use the deck basis or flag the call's inconsistency.
- S7. Section B 4A #12 says the analyst's 2.9x was "left uncorrected (deck: 2.7x)". Deck L472 shows 2.9x at Jun-26 and L488 a 2.9x incremental ratio, so the analyst's figure is defensible.
- S8. Q6 could cite the call's contracted-escalation figure as the renewal benchmark (concall L315, ASR "67%", R176 flagged possible mishearing).
- S9. Forward-map row "Undated" should read NOT FOUND, per house convention (M12-M14 already do).
- S10. A4 YAML docs_merged lists three doctypes while the review merges five documents. List deck, letter and press separately.

---

## SUGGESTED GRAFT TEXT FOR A4 (to make the loop cheap; A4 owns final wording)

- Step 4 and Section C, after the recurring-core answer: "Of the 193.14 Cr YoY Ind AS revenue rise, 5.0 Cr is a swing in an undefined Ind AS-only revenue adjustment. It was 3.7 Cr below billed revenue in Q2 FY26 and 1.3 Cr above in Q2 FY27 (letter L662; deck L704-706). On billed revenue, growth is 32.5%. Core PBT ex OI and FI is (0.32) Cr vs (0.63) Cr a year ago, and the recurring core is about +0.3 Cr [derived]."
- Step 5 and Section C, cash paragraph: "The H1 improvement is the WC float. Ex-WC, lease-adjusted FCF after capex and ROU additions moved from (63.44) to (130.53) Cr [derived]. Direction: improving only through growth-linked float; deteriorating ex-float."
- Brief section 3, replacing L1037-1038: "Cash rent fell from 42.5% to 38.9% of revenue YoY [INFERENCE from MGMT]. Part of this is timing. Landlord rent-free periods end in Q3, management says [MGMT, ASR]. Cash rent rose 21.4% while operational area rose 27.1% [MGMT]. Q3 cash rent per square foot decides it."
- Brief section 1, replacing L1001-1002: "Three headline claims do not rebuild from the filed statements: net cash, ROCE and order book cover. Free cash flow to the firm rebuilds only by leaving out Rs 20.0 Cr of lease-related cash. On a full basis it was about minus Rs 4.0 Cr in H1 [INFERENCE]."

---

```yaml
stage: A5-adversary
company: "WEWORK"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Core Ind AS profit recovering; Q2 core PBT ex OI/FI turned positive at 0.98 Cr; recurring core +5.30 Cr of the +14.03 Cr PAT change (rev L208, L270, L296)", counter: "5.0 Cr of the YoY Ind AS revenue rise is a swing in an undefined Ind AS-only revenue adjustment (3.7 Cr below billed IGAAP-EQ revenue in Q2 FY26, 1.3 Cr above in Q2 FY27). On billed revenue, growth is 32.5%, core PBT ex OI/FI is (0.32) vs (0.63) Cr, and the recurring core is about +0.3 Cr; 94% of the recurring core is the swing", source_line: "letter L662, L723; deck L704-706, L537; press L191-192; results L486-499", type: MISSING}
  - {claim: "Lease-adjusted FCF after capex and ROU additions near breakeven and improving, (73.52) to (3.99) Cr; cash-conversion direction improving (rev L356, L940, L1004-1005)", counter: "The WC swing of (10.08) to +126.54 Cr, which A4 itself calls growth-linked float, accounts for the whole improvement. Ex-WC the measure moved from (63.44) to (130.53) Cr; lease-adjusted CFO before WC fell from 96.4% to 91.6% of rent-adjusted operating EBITDA", source_line: "results L615, L625-631, L643-644; concall L665-679", type: MISSING}
  - {claim: "Operating spread improving on a cash-rent basis: cash rent 42.5% to 38.9% of revenue, real operating leverage on a cash basis (rev L242, L953, L1037-1038)", counter: "Management says landlord rent-free periods expire in Q3 and rentals then hit the P&L in full force; cash rent rose 21.4% YoY while operational area rose 27.1%, so Q2 cash rent per sq ft is partly timing. The qualifier sits in Step 3, 6B and Q7 but not where the claim is made", source_line: "concall L723-730; deck L310, L795; deck L404-408 (bull mix reading)", type: MISSING}
findings_by_type:
  factual:
    - "F1: FCFF classed as not rebuilding and its formula as missing (rev L356 item 2, L484, L948, L1001-1002, L1148). Deck L660-667 gives the formula: CFO 1,026.2 - rent (A) 576.6 - brokerage 69.8 = FCFO 379.8; - capex 363.8 = FCFF 16.0. The gap to full-basis (3.99) is finance-lease payout 11.4 (deck L796) + ROU payments above brokerage 8.57 = 19.97. Reclassify as a definitional exclusion; narrow Q2"
  missing:
    - "M1: surviving counter 1, Ind AS-only revenue adjustment swing of 5.0 Cr YoY (letter L662) not in the review; it is about 94% of the recurring core +5.30 Cr"
    - "M2: surviving counter 2, ex-WC lease-adjusted FCF after capex and ROU (63.44) to (130.53) Cr not in the review; the cash-conversion direction label must reflect it"
    - "M3: surviving counter 3, rent-free timing qualifier (concall L723-730) and cash rent +21.4% vs area +27.1% (deck L795, L310) absent from brief section 3, Section C and analyst_note"
  contradiction:
    - "C1: capacity measurement-date ambiguity (flags L1154; Q5 bear answer L487) vs press L88-90, deck L429-435 (126.9k + 18.4k = 145.3k at Sep-26) and concall L701-706, and A4's own 145.3k + 4.5k = 149.8k (rev L473, M3)"
    - "C2: Step 5-C 'few new ROU in H1' (rev L326) vs Step 3 front-loading explanation (rev L270); derived net ROU additions about 347.5 Cr (results L542; letter L735 H1 ROU depreciation 438.3) and net new lease liabilities about 291.5 Cr (results L575, L583, L643)"
  style:
    - "S1: last-digit rounding: SA FY26 (OI+FI)/PBT 99.4 vs 99.3%; CA margin -231 vs -230 bps; SA -244 vs -243 bps; rent-adjusted +184 vs +183 bps; bridge label -2.31 pp vs -2.30 pp used"
    - "S2: brief L999-1000 'core pretax profit about Rs 1.0 Cr' also strips the 0.87 Cr associate (20.45 - 18.60 = 1.85)"
    - "S3: brief L988 says every figure comes from this quarter's documents, but L1010 CMP and PE come from screener.in; tag SECONDARY"
    - "S4: L-F1-a missing from the finding-to-question mapping table (mapped in Q12); table shows 16 letter rows vs 17 stated"
    - "S5: preamble does not name A2 letter MFS-1 (content covered at 0C/0D)"
    - "S6: Section B claim 4 equates ~10 msf with 26% of space; deck L247-250 shows 7.5 MSF branded = 26%"
    - "S7: 4A #12 'analyst 2.9x left uncorrected'; deck L472 (Jun-26 2.9x) and L488 (2.9x incremental) make it defensible"
    - "S8: Q6 could cite the call's contracted escalation (concall L315, ASR 67%, R176 possible mishearing)"
    - "S9: forward-map row 'Undated' should read NOT FOUND"
    - "S10: A4 YAML docs_merged lists 3 doctypes for 5 documents"
loop_back_to: "A4"
gap: "A4 re-run: (F1 FACTUAL) reclassify FCFF as rebuilding on the deck p28 formula (L660-667), with a 20.0 Cr definitional exclusion (finance-lease payout 11.4, deck L796, plus ROU payments above brokerage 8.6); fix rev L356 item 2, Q2, L948, L1001-1002, L1148. (C1 CONTRADICTION) drop the capacity measurement-date ambiguity from flags L1154 and the Q5 bear answer; press L88-90, deck L429-435 and concall L701-706 place 145.3k at 30-Sep. (C2 CONTRADICTION) replace 'few new ROU in H1' (rev L326) with derived net ROU additions about 347.5 Cr. (M1-M3 MISSING) graft the three surviving bear counters into Steps 2-5, Section C, brief sections 1 and 3, and analyst_note."
style_notes:
  - "S1 rounding last digits (99.3%, -230 bps, -243 bps, +183 bps, -2.30 pp label)"
  - "S2 brief core-PBT sentence omits the associate strip"
  - "S3 tag CMP/PE line SECONDARY (screener.in)"
  - "S4 add L-F1-a to the mapping table"
  - "S5 name letter MFS-1 in the preamble"
  - "S6 claim 4 space basis 7.5 MSF branded"
  - "S7 analyst 2.9x is defensible"
  - "S8 cite contracted escalation (ASR 67%) in Q6"
  - "S9 Undated to NOT FOUND"
  - "S10 docs_merged lists five documents"
analyst_note: "Coverage and arithmetic are clean. My fresh counts match A2 on every unit, structured row totals match all five ledgers, and every derived metric recomputes within rounding. The failure is interpretive. Three of A4's most positive readings each rest on one undisclosed or temporary item. Core Ind AS profit turning positive rests on a 5.0 Cr swing in an undefined Ind AS-only revenue adjustment (letter L662). FCF improving rests on a 126.5 Cr working-capital float that A4 itself calls growth-linked; ex-float the measure fell from (63.4) to (130.5) Cr. Cash-rent leverage rests partly on landlord rent-free periods that management says end in Q3. These grafts likely leave PROCEED WITH FLAGS unchanged. They change what the quarter proved: volume yes, operating profit and cash improvement not yet. One finding cuts the other way. The company FCFF of 16.0 Cr rebuilds from filed lines on the deck p28 formula. The 20.0 Cr gap to A4's (4.0) Cr comes from leaving out finance-lease payouts and ROU payments; it is not an unreconciled KPI. No acquisition is described, so the acquisition probe did not trigger."
```
